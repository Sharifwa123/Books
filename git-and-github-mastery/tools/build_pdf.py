#!/usr/bin/env python3
"""Builds the PDF edition of the book with WeasyPrint.
Usage: build_pdf.py [--profile screen|print] [--out FILE] [--limit N] [--variant pdf/ua-1|none]
  --limit N   build only the first N chapters (for quick tests)
Features: metadata, bookmarks (parts > chapters > sections), a linked table of contents with page numbers, internal links for
cross-references, running headers, roman page numbers for the front matter, an index with page numbers, embedded fonts, tagged PDF (PDF/UA variant),
document language. Nothing is invented: placeholders stay placeholders."""
import argparse, csv, glob, os, re, sys, html, datetime, collections
sys.path.insert(0, os.path.dirname(__file__))
import toc_data as T
from markdown_it import MarkdownIt
import weasyprint
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ap = argparse.ArgumentParser()
ap.add_argument("--profile", default="screen", choices=["screen", "print"])
ap.add_argument("--out", default=None)
ap.add_argument("--limit", type=int, default=0)
ap.add_argument("--variant", default="pdf/ua-1")
a = ap.parse_args()
out = a.out or os.path.join(root, "publishing", "build", f"git-and-github-from-zero-to-mastery-{a.profile}.pdf")
os.makedirs(os.path.dirname(out), exist_ok=True)

md = MarkdownIt("commonmark").enable("table")
def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:60]
def strip_front(text):
    m = re.match(r"---\n(.*?)\n---\n", text, flags=re.S)
    meta = {}
    if m:
        for l in m.group(1).split("\n"):
            if ":" in l: k, v = l.split(":", 1); meta[k.strip()] = v.strip()
        text = text[m.end():]
    return meta, text
import hashlib
DIAG = os.path.join(root, "publishing", "build", "diagrams")
def diagram(m, text, end):
    code = m.group(1); k = hashlib.sha1(code.encode()).hexdigest()[:12]
    svg = os.path.join(DIAG, k + ".svg")
    if not os.path.exists(svg): return "\n\n<p><em>[diagram not rendered]</em></p>\n\n"
    d = re.search(r"\*Diagram description:\*\s*(.*)", text[end:end + 1500])
    alt = html.escape(re.sub(r"[`*]", "", d.group(1)).strip(), quote=True) if d else "Diagram"
    return f'\n\n<figure class="diagram"><img src="file://{svg}" alt="{alt}"></figure>\n\n'
def prep(text):
    text = re.sub(r"```mermaid\n(.*?)```", lambda m: diagram(m, text, m.end()), text, flags=re.S)
    parts = re.split(r"(```.*?```)", text, flags=re.S)
    res = []
    for p in parts:
        if p.startswith("```"): res.append(p); continue
        p = re.sub(r"(\d+)<!--ref:([a-z_0-9]+)-->", lambda m: f"[{m.group(1)}](#ch-{m.group(2)})", p)
        p = re.sub(r"<!--.*?-->", "", p, flags=re.S)
        p = p.replace("⚠️ ", "").replace("⚠️", "")
        res.append(p)
    return "".join(res)
def render(text, prefix, h1class, h2level_class=""):
    tokens = md.parse(prep(text))
    used = collections.Counter()
    for i, t in enumerate(tokens):
        if t.type == "heading_open":
            title = tokens[i + 1].content
            if t.tag == "h1":
                t.attrSet("class", h1class)
            else:
                s = f"{prefix}-{slug(title)}"; used[s] += 1
                if used[s] > 1: s += f"-{used[s]}"
                t.attrSet("id", s)
    return md.renderer.render(tokens, md.options, {})

C = T.C
num = {c[1]: i + 1 for i, c in enumerate(C)}
chapter_files = {}
for f in glob.glob(os.path.join(root, "manuscript", "parts", "*", "ch*.md")):
    m = re.match(r"ch(\d+)-", os.path.basename(f)); chapter_files[int(m.group(1))] = f
sections, toc = [], []
def add_toc(level, label, href): toc.append((level, label, href))

# Front matter
front_html = []
for f in sorted(glob.glob(os.path.join(root, "manuscript", "front-matter", "*.md"))):
    name = os.path.basename(f)
    text = open(f, encoding="utf-8").read()
    if name.startswith("00-"):
        body = render(text, "title", "top")
        front_html.append(f'<section class="titlepage" id="titlepage">{body}</section>')
    elif name.startswith("02-"):
        front_html.append("@@TOC@@")
    else:
        body = render(text, "front-" + slug(name), "top")
        h = re.search(r"# (.*)", text).group(1)
        add_toc(1, h, "#front-" + slug(name))
        front_html.append(f'<section class="front-section" id="front-{slug(name)}">{body}</section>')

# Parts and chapters
body_html = []
by_part = collections.OrderedDict()
for i, c in enumerate(C): by_part.setdefault(c[0], []).append(i + 1)
count = 0
chapter_text = {}
for pi, (pn, pt) in enumerate(T.PARTS):
    stop = False
    for n in by_part.get(pi, []):
        if a.limit and n > a.limit: stop = True; break
    if a.limit and not any(n <= a.limit for n in by_part.get(pi, [])): continue
    body_html.append(f'<h1 class="part" id="part-{pn}">Part {pn} — {html.escape(pt)}</h1>')
    add_toc(1, f"Part {pn} — {pt}", f"#part-{pn}")
    for n in by_part.get(pi, []):
        if a.limit and n > a.limit: break
        key = C[n - 1][1]
        text = open(chapter_files[n], encoding="utf-8").read()
        meta, text = strip_front(text)
        chapter_text[key] = text
        h = render(text, key, "chapter")
        h = h.replace('<h1 class="chapter">', f'<h1 class="chapter" id="ch-{key}">', 1)
        title = re.search(r"# (.*)", text).group(1)
        add_toc(2, title, f"#ch-{key}")
        body_html.append(f'<section class="chapter-body">{h}</section>')

# Appendices and back matter
back_html = []
if not a.limit:
    for f in sorted(glob.glob(os.path.join(root, "manuscript", "appendices", "*.md"))):
        text = open(f, encoding="utf-8").read()
        ident = "appx-" + os.path.basename(f).split("-")[1]
        h = render(text, ident, "top")
        h = h.replace('<h1 class="top">', f'<h1 class="top" id="{ident}">', 1)
        add_toc(1, re.search(r"# (.*)", text).group(1), "#" + ident)
        back_html.append(f'<section class="appendix">{h}</section>')
    for name in ["glossary", "INDEX", "author-and-publisher"]:
        if name == "INDEX":
            # index of terms: term -> chapters that mention it
            rows = sorted(csv.DictReader(open(os.path.join(root, "glossary", "glossary-master.csv"), encoding="utf-8")), key=lambda r: r["term"].lower())
            items = []
            for r in rows:
                term = r["term"]
                pat = re.compile(r"(?<![A-Za-z])" + re.escape(term) + r"(?![A-Za-z])", re.I)
                hits = [k for k, t in chapter_text.items() if pat.search(t)]
                if not hits: continue
                links = ", ".join(f'<a href="#ch-{k}" class="pg"></a>' for k in hits[:10])
                items.append(f'<p class="idx"><strong>{html.escape(term)}</strong> {links}</p>')
            h = '<h1 class="top" id="index">Index of terms</h1><p>Each entry lists the chapters that mention the term, with page numbers. Command names are indexed in Appendix A.</p>' + "\n".join(items)
            add_toc(1, "Index of terms", "#index")
            back_html.append(f'<section class="index">{h}</section>')
            continue
        f = os.path.join(root, "manuscript", "back-matter", name + ".md")
        text = open(f, encoding="utf-8").read()
        h = render(text, "back-" + name, "top")
        h = h.replace('<h1 class="top">', f'<h1 class="top" id="back-{name}">', 1)
        add_toc(1, re.search(r"# (.*)", text).group(1), f"#back-{name}")
        back_html.append(f'<section class="back">{h}</section>')

toc_items = "".join(f'<li class="l{lv}"><a href="{href}">{html.escape(label)}</a></li>' for lv, label, href in toc)
toc_html = f'<section class="front-section" id="contents"><h1 class="top">Contents</h1><ul class="toc">{toc_items}</ul></section>'
front = "\n".join(toc_html if x == "@@TOC@@" else x for x in front_html)

css_page = {
 "screen": "@page { size: A4; margin: 22mm 20mm 24mm 20mm; }",
 "print": "@page { size: 170mm 240mm; margin: 20mm 16mm 22mm 20mm; } @page :left { margin: 20mm 20mm 22mm 16mm; }",
}[a.profile]
color = "#1a1a1a" if a.profile == "print" else "#14213d"
link = "#000" if a.profile == "print" else "#0b4f9e"
css = css_page + """
@page { @top-center { content: string(running); font: 8pt 'DejaVu Sans', sans-serif; color: #555; }
        @bottom-center { content: counter(page); font: 9pt 'DejaVu Sans', sans-serif; } }
@page front { @bottom-center { content: counter(page, lower-roman); font: 9pt 'DejaVu Sans', sans-serif; } @top-center { content: none; } }
@page titlepg { @top-center { content: none; } @bottom-center { content: none; } }
html { font-family: 'DejaVu Serif', serif; font-size: 9.6pt; line-height: 1.45; color: #111; }
body { widows: 3; orphans: 3; }
.titlepage { page: titlepg; text-align: center; padding-top: 55mm; }
.titlepage h1 { font: bold 26pt 'DejaVu Sans', sans-serif; color: COLOR; }
.titlepage h2 { font: 13pt 'DejaVu Sans', sans-serif; font-weight: normal; margin: 12mm 10mm; }
.front-section { page: front; }
.front-section h1, h1.top { font: bold 20pt 'DejaVu Sans', sans-serif; color: COLOR; page-break-before: always; bookmark-level: 1; bookmark-label: content(text); string-set: running content(text); }
.titlepage h1 { page-break-before: auto; bookmark-level: none; }
h1.part { font: bold 24pt 'DejaVu Sans', sans-serif; color: COLOR; page-break-before: always; padding-top: 70mm; text-align: center; bookmark-level: 1; string-set: running content(text); }
h1.chapter { font: bold 18pt 'DejaVu Sans', sans-serif; color: COLOR; page-break-before: always; bookmark-level: 2; bookmark-label: content(text); string-set: running content(text); margin-bottom: 6mm; }
.chapter-body h2 { font: bold 13pt 'DejaVu Sans', sans-serif; color: COLOR; bookmark-level: 3; margin-top: 8mm; page-break-after: avoid; }
.chapter-body h3 { font: bold 11pt 'DejaVu Sans', sans-serif; bookmark-level: 4; page-break-after: avoid; }
.appendix h2, .back h2, .index h2, .front-section h2 { font: bold 13pt 'DejaVu Sans', sans-serif; color: COLOR; bookmark-level: 2; margin-top: 7mm; page-break-after: avoid; }
.appendix h3, .back h3 { font: bold 11pt 'DejaVu Sans', sans-serif; bookmark-level: 3; }
.body-start { counter-reset: page 1; }
a { color: LINK; text-decoration: none; }
code, pre { font-family: 'DejaVu Sans Mono', monospace; font-size: 8.2pt; }
pre { background: #f3f3f3; border-left: 2.5pt solid #999; padding: 3mm; white-space: pre-wrap; overflow-wrap: anywhere; page-break-inside: auto; }
code { overflow-wrap: anywhere; }
blockquote { border-left: 3pt solid #888; margin: 4mm 0; padding: 1mm 4mm; background: #f7f7f7; page-break-inside: avoid; }
table { border-collapse: collapse; width: 100%; margin: 4mm 0; font-size: 8.4pt; table-layout: auto; }
th, td { border: 0.5pt solid #999; padding: 1.5mm 2mm; vertical-align: top; overflow-wrap: anywhere; }
th { background: #e8e8e8; font-family: 'DejaVu Sans', sans-serif; }
tr { page-break-inside: avoid; }
figure.diagram { margin: 4mm 0; text-align: center; page-break-inside: avoid; }
figure.diagram img { max-width: 100%; max-height: 90mm; }
ul.toc { list-style: none; padding: 0; }
ul.toc li { margin: 0.6mm 0; }
ul.toc li.l1 { font-weight: bold; margin-top: 3mm; font-family: 'DejaVu Sans', sans-serif; }
ul.toc li.l2 { padding-left: 6mm; }
ul.toc a::after { content: leader('.') target-counter(attr(href), page); }
a.pg::after { content: target-counter(attr(href), page); }
p.idx { margin: 0.5mm 0; font-size: 8.6pt; }
""".replace("COLOR", color).replace("LINK", link)
# the first part starts the arabic numbering
body = "\n".join(body_html).replace('<h1 class="part"', '<h1 class="part body-start"', 1)
epoch = int(os.environ.get("SOURCE_DATE_EPOCH", "0")) or int(datetime.datetime.now(datetime.timezone.utc).timestamp())
STAMP = datetime.datetime.fromtimestamp(epoch, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
doc = f"""<!doctype html><html lang="en-GB"><head><meta charset="utf-8">
<title>Git &amp; GitHub: From Zero to Mastery</title>
<meta name="author" content="Sharif Tingane Issah">
<meta name="description" content="A Complete Beginner-to-Expert Guide to Version Control, Collaboration, Automation, Security, and Modern Software Development. Published by SHARIF TECHNOLOGIES.">
<meta name="keywords" content="Git, GitHub, version control, GitHub Actions, security, open source, CI/CD, tutorial">
<meta name="generator" content="tools/build_pdf.py (WeasyPrint {weasyprint.__version__})">
<meta name="dcterms.created" content="{STAMP}"><meta name="dcterms.modified" content="{STAMP}">
<style>{css}</style></head><body>
{front}
{body}
{"".join(back_html)}
</body></html>"""
open(out.replace(".pdf", ".html"), "w", encoding="utf-8").write(doc)
variant = None if a.variant == "none" else a.variant
print("rendering", out, "profile", a.profile, "variant", variant)
ident = hashlib.sha256(doc.encode()).digest()[:16] if os.environ.get('SOURCE_DATE_EPOCH') else None
pdf = weasyprint.HTML(string=doc, base_url=root).write_pdf(out, pdf_variant=variant, **({'pdf_identifier': ident} if ident else {}))
print("done", os.path.getsize(out), "bytes")
