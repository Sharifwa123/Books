#!/usr/bin/env python3
"""Builds a reflowable EPUB 3 from the manuscript (never from the PDF): real headings, real tables and code text,
a navigation document, internal links, accessibility metadata, diagrams as SVG images with alternative text.
Output: publishing/build/git-and-github-from-zero-to-mastery.epub, then a structural self-check.
Usage: build_epub.py [--out FILE]      Needs: markdown-it-py; diagrams pre-rendered by tools/render_diagrams.py (optional).
The cover is publishing/cover/cover-front.png when present. Validate with EPUBCheck (see the CI job)."""
import datetime, glob, hashlib, html, os, re, sys, uuid, zipfile
import xml.etree.ElementTree as ET
from markdown_it import MarkdownIt
sys.path.insert(0, os.path.dirname(__file__))
import toc_data as T, bookparts as BP
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
out = os.path.join(root, "publishing", "build", "git-and-github-from-zero-to-mastery.epub")
if "--out" in sys.argv: out = sys.argv[sys.argv.index("--out") + 1]
os.makedirs(os.path.dirname(out), exist_ok=True)
M = os.path.join(root, "manuscript"); DIAG = os.path.join(root, "publishing", "build", "diagrams")
TITLE = "Git & GitHub: From Zero to Mastery"
SUB = "A Complete Beginner-to-Expert Guide to Version Control, Collaboration, Automation, Security, and Modern Software Development"
AUTHOR = "Sharif Issah Tingane"
epoch = int(os.environ.get("SOURCE_DATE_EPOCH", "0")) or int(datetime.datetime.now(datetime.timezone.utc).timestamp())
STAMP = datetime.datetime.fromtimestamp(epoch, datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
md = MarkdownIt("commonmark", {"xhtmlOut": True}).enable("table")
def slug(s): return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:50] or "x"
def strip_front(t): return re.sub(r"\A---\n.*?\n---\n", "", t, flags=re.S)

# ---- gather sources in reading order
num = {c[1]: i + 1 for i, c in enumerate(T.C)}
chap = {}
for f in glob.glob(f"{M}/parts/*/ch*.md"): chap[int(re.match(r"ch(\d+)-", os.path.basename(f)).group(1))] = f
entries = []  # (kind, file_name, source path or None, label)
for f in sorted(glob.glob(f"{M}/front-matter/*.md")):
    entries.append(("front", "front-" + slug(os.path.basename(f)[3:-3]), f))
for pi, (pn, pt) in enumerate(T.PARTS):
    entries.append(("part", f"part-{pn.lower()}", (pn, pt)))
    for i, c in enumerate(T.C):
        if c[0] == pi: entries.append(("chapter", f"ch{i + 1:02d}-{c[1]}", chap[i + 1]))
for f in sorted(glob.glob(f"{M}/appendices/*.md")):
    entries.append(("appendix", "appx-" + os.path.basename(f).split("-")[1], f))
entries.append(("back", "back-solutions", "@solutions"))
for n in ("glossary", "author-and-publisher"):
    entries.append(("back", "back-" + n, f"{M}/back-matter/{n}.md"))
key_file = {c[1]: f"ch{i + 1:02d}-{c[1]}.xhtml" for i, c in enumerate(T.C)}

figures, images = [], {}
def diagram(m, text):
    code = m.group(1); k = hashlib.sha1(code.encode()).hexdigest()[:12]
    svg = os.path.join(DIAG, k + ".svg")
    if not os.path.exists(svg): return "\n\n<p><em>[diagram not rendered]</em></p>\n\n"
    d = re.search(r"\*Diagram description:\*\s*(.*)", text[m.end():m.end() + 1500])
    alt = html.escape(re.sub(r"[`*]", "", d.group(1)).strip(), quote=True) if d else "Diagram"
    images[k] = svg
    return f'\n\n<figure><img src="../images/{k}.svg" alt="{alt}" /></figure>\n\n'
def prep(text):
    text = re.sub(r"```mermaid\n(.*?)```", lambda m: diagram(m, text), text, flags=re.S)
    parts = re.split(r"(```.*?```)", text, flags=re.S); res = []
    for p in parts:
        if not p.startswith("```"):
            p = re.sub(r"(\d+)<!--ref:([a-z_0-9]+)-->", lambda m: f"[{m.group(1)}]({key_file.get(m.group(2), 'missing.xhtml')})", p)
            p = re.sub(r"<!--.*?-->", "", p, flags=re.S)
            p = p.replace("⚠️ ", "").replace("⚠️", "")
        res.append(p)
    return "".join(res)

def render(text):
    tokens = md.parse(prep(text)); used = {}; heads = []
    for i, t in enumerate(tokens):
        if t.type == "heading_open":
            title = tokens[i + 1].content; s = slug(title); used[s] = used.get(s, 0) + 1
            if used[s] > 1: s += f"-{used[s]}"
            t.attrSet("id", s); heads.append((int(t.tag[1]), re.sub(r"[`*]", "", title), s))
    return md.renderer.render(tokens, md.options, {}), heads

CSS = """html{font-family:serif;line-height:1.5}body{margin:0 5%}
h1,h2,h3,h4{font-family:sans-serif;line-height:1.25;page-break-after:avoid;break-after:avoid}
h1{font-size:1.6em;margin:1.4em 0 .6em}h2{font-size:1.25em;margin-top:1.6em}h3{font-size:1.1em}
pre{white-space:pre-wrap;overflow-wrap:anywhere;background:#f3f3f3;padding:.6em .8em;border-left:.25em solid #999;font-size:.85em}
code{font-family:monospace;overflow-wrap:anywhere}
blockquote{margin:1em 0;padding:.2em 1em;border-left:.25em solid #888;background:#f7f7f7}
table{border-collapse:collapse;width:100%;font-size:.9em;margin:1em 0}th,td{border:1px solid #999;padding:.3em .5em;vertical-align:top;overflow-wrap:anywhere}
th{background:#e8e8e8;font-family:sans-serif}figure{margin:1em 0;text-align:center}figure img{max-width:100%;height:auto}
.part-title{text-align:center;margin-top:30%}nav ol{list-style:none;padding-left:1em}nav>ol{padding-left:0}
@media (prefers-color-scheme: dark){html{background:#111;color:#e6e6e6}pre,blockquote{background:#222}th{background:#2a2a2a}a{color:#8ab4f8}}"""

def xhtml(title, body, epub_type=None):
    et = f' epub:type="{epub_type}"' if epub_type else ""
    return ('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" '
            f'lang="en-GB" xml:lang="en-GB"><head><meta charset="utf-8" /><title>{html.escape(title)}</title>'
            f'<link rel="stylesheet" type="text/css" href="../style.css" /></head><body{et}>{body}</body></html>')

docs, nav_items = {}, []   # file -> xhtml ; nav: (level, label, href)
COVER = os.path.join(root, "publishing", "cover", "cover-front.png")
if os.path.exists(COVER):
    docs["cover.xhtml"] = xhtml("Cover", f'<section epub:type="cover" style="text-align:center"><img src="../images/cover.png" alt="Cover: {html.escape(TITLE, quote=True)}, by {AUTHOR}" style="max-width:100%;height:auto" /></section>', "cover")
for kind, name, src in entries:
    fn = name + ".xhtml"
    if kind == "part":
        pn, pt = src
        docs[fn] = xhtml(f"Part {pn} — {pt}", f'<section epub:type="part"><h1 class="part-title" id="top">Part {pn} — {html.escape(pt)}</h1></section>', "bodymatter")
        nav_items.append((1, f"Part {pn} — {pt}", fn + "#top")); continue
    text = strip_front(open(src, encoding="utf-8").read()) if src != "@solutions" else BP.solutions_text([(i + 1, c[2]) for i, c in enumerate(T.C)])
    if kind == "chapter": text = BP.with_exercises(int(re.match(r"ch(\d+)", name).group(1)), text)
    body, heads = render(text)
    title = next((h[1] for h in heads if h[0] == 1), name)
    et = {"front": "frontmatter", "chapter": "chapter", "appendix": "appendix", "back": "backmatter"}[kind]
    docs[fn] = xhtml(title, f'<section epub:type="{et}">{body}</section>', "bodymatter" if kind == "chapter" else et)
    lvl = 2 if kind == "chapter" else 1
    nav_items.append((lvl, title, fn + (f"#{heads[0][2]}" if heads else "")))
    for hl, ht, hid in heads:
        if hl == 2 and kind in ("chapter", "appendix"): nav_items.append((lvl + 1, ht, f"{fn}#{hid}"))

# navigation document (nested lists by level)
# simple, valid nesting: build a tree
def build(items):
    root_ = {"c": [], "l": 0}; st = [root_]
    for lv, label, href in items:
        node = {"label": label, "href": href, "c": [], "l": lv}
        while st[-1]["l"] >= lv: st.pop()
        st[-1]["c"].append(node); st.append(node)
    return root_
def ol(n): return "<ol>" + "".join(f'<li><a href="text/{c["href"]}">{html.escape(c["label"])}</a>{ol(c) if c["c"] else ""}</li>' for c in n["c"]) + "</ol>"
cover_landmark = '<li><a epub:type="cover" href="text/cover.xhtml">Cover</a></li>' if os.path.exists(COVER) else ""
first_body = next(f for k, f, s in entries if k == "part") + ".xhtml"
nav = ('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" lang="en-GB" xml:lang="en-GB">'
       f'<head><meta charset="utf-8" /><title>Contents</title><link rel="stylesheet" type="text/css" href="style.css" /></head><body>'
       f'<nav epub:type="toc" id="toc" role="doc-toc"><h1>Contents</h1>{ol(build(nav_items))}</nav>'
       f'<nav epub:type="landmarks" hidden="hidden"><h2>Guide</h2><ol>{cover_landmark}<li><a epub:type="titlepage" href="text/front-title-page.xhtml">Title page</a></li>'
       f'<li><a epub:type="toc" href="nav.xhtml#toc">Contents</a></li><li><a epub:type="bodymatter" href="text/{first_body}">Start of the book</a></li></ol></nav></body></html>')

# package
book_id = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, "urn:git-and-github-from-zero-to-mastery:sharif-tingane-issah"))
items = [f'<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>', '<item id="css" href="style.css" media-type="text/css"/>']
spine = ['<itemref idref="nav" linear="no"/>']
for i, fn in enumerate(docs):
    items.append(f'<item id="d{i}" href="text/{fn}" media-type="application/xhtml+xml"/>'); spine.append(f'<itemref idref="d{i}"/>')
if os.path.exists(COVER): items.append('<item id="cover-image" href="images/cover.png" media-type="image/png" properties="cover-image"/>')
for k in sorted(images): items.append(f'<item id="img-{k}" href="images/{k}.svg" media-type="image/svg+xml"/>')
opf = f'''<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="en-GB" prefix="schema: http://schema.org/">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="bookid">{book_id}</dc:identifier>
<dc:title id="t1">{html.escape(TITLE)}</dc:title><meta refines="#t1" property="title-type">main</meta>
<dc:title id="t2">{html.escape(SUB)}</dc:title><meta refines="#t2" property="title-type">subtitle</meta>
<dc:creator id="a1">{AUTHOR}</dc:creator><meta refines="#a1" property="role" scheme="marc:relators">aut</meta>
<dc:language>en-GB</dc:language>
<dc:publisher>SHARIF TECHNOLOGIES</dc:publisher>
<dc:contributor>Claude (AI assistant by Anthropic, used through Claude Code): drafting, research, code and build tooling, under the author's direction</dc:contributor>
<dc:rights>Copyright © 2026 SHARIF TECHNOLOGIES. Text: CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/). Code samples: MIT License. Third-party material is not covered.</dc:rights>
<dc:subject>Git</dc:subject><dc:subject>GitHub</dc:subject><dc:subject>Version control</dc:subject><dc:subject>GitHub Actions</dc:subject><dc:subject>Open source</dc:subject>
<dc:description>{html.escape(SUB)}</dc:description>
<meta property="dcterms:modified">{STAMP}</meta>
<meta property="schema:accessMode">textual</meta><meta property="schema:accessMode">visual</meta>
<meta property="schema:accessModeSufficient">textual</meta>
<meta property="schema:accessibilityFeature">structuralNavigation</meta><meta property="schema:accessibilityFeature">tableOfContents</meta>
<meta property="schema:accessibilityFeature">readingOrder</meta><meta property="schema:accessibilityFeature">alternativeText</meta>
<meta property="schema:accessibilityHazard">none</meta>
<meta property="schema:accessibilitySummary">Reflowable text with a table of contents, real headings and tables, code as text, and text descriptions for diagrams. This has not been audited or certified by a third party.</meta>
</metadata>
<manifest>{"".join(items)}</manifest>
<spine>{"".join(spine)}</spine>
</package>'''
container = '<?xml version="1.0"?><container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles></container>'

# ---- write the zip (mimetype first, stored; fixed timestamps)
dt = datetime.datetime.fromtimestamp(epoch, datetime.timezone.utc).timetuple()[:6]
def put(z, name, data, stored=False):
    zi = zipfile.ZipInfo(name, date_time=dt); zi.compress_type = zipfile.ZIP_STORED if stored else zipfile.ZIP_DEFLATED
    zi.external_attr = 0o644 << 16; z.writestr(zi, data)
with zipfile.ZipFile(out, "w") as z:
    put(z, "mimetype", "application/epub+zip", stored=True)
    put(z, "META-INF/container.xml", container); put(z, "OEBPS/content.opf", opf); put(z, "OEBPS/nav.xhtml", nav); put(z, "OEBPS/style.css", CSS)
    for fn, d in docs.items(): put(z, f"OEBPS/text/{fn}", d)
    for k, p in sorted(images.items()): put(z, f"OEBPS/images/{k}.svg", open(p, "rb").read())
    if os.path.exists(COVER): put(z, "OEBPS/images/cover.png", open(COVER, "rb").read())
print("wrote", os.path.relpath(out, root), os.path.getsize(out), "bytes;", len(docs), "documents,", len(images), "images")

# ---- structural self-check
problems = []
with zipfile.ZipFile(out) as z:
    names = set(z.namelist())
    if z.namelist()[0] != "mimetype": problems.append("mimetype is not the first entry")
    ids = {}
    for n in names:
        if n.endswith((".xhtml", ".opf", ".xml")):
            try: tree_ = ET.fromstring(z.read(n))
            except ET.ParseError as e: problems.append(f"{n}: not well-formed XML: {e}"); continue
            if n.endswith(".xhtml"): ids[n] = {e.get("id") for e in tree_.iter() if e.get("id")}
    for n in [n for n in names if n.endswith(".xhtml")]:
        base = os.path.dirname(n)
        for m in re.finditer(r'(?:href|src)="([^"]+)"', z.read(n).decode("utf-8")):
            u = m.group(1)
            if re.match(r"[a-z]+:", u) or u.startswith("#"):
                if u.startswith("#") and u[1:] not in ids.get(n, set()): problems.append(f"{n}: dangling fragment {u}")
                continue
            path, _, frag = u.partition("#"); target = os.path.normpath(os.path.join(base, path)).replace(os.sep, "/")
            if target not in names: problems.append(f"{n}: link to missing file {u}")
            elif frag and target.endswith(".xhtml") and frag not in ids.get(target, set()): problems.append(f"{n}: link to missing anchor {u}")
    for n in names:
        if n.endswith(".xhtml") and b"<img" in z.read(n):
            if re.search(rb"<img(?![^>]*\balt=)", z.read(n)): problems.append(f"{n}: image without alt text")
print("epub self-check:", "passed" if not problems else f"{len(problems)} problem(s)")
for p in problems[:30]: print("  ", p)
sys.exit(1 if problems else 0)
