#!/usr/bin/env python3
"""Builds a Word (.docx) edition of the complete manuscript from the clean export (Markdown), for submissions that ask for
a Word file (for example an ISBN application). It does not use the PDF or the EPUB: the source is the same clean export
that feeds them. Headings, paragraphs, bold/italic/code, links, lists, tables, code blocks, quotations and the rendered
diagrams are kept; page numbers are in the footer; the document has title, author, language and keywords set.
usage: build_docx.py [--book publishing/build/clean/book.md] [--out FILE.docx]
Needs: python-docx, markdown-it-py, and (for diagrams) Chromium plus the SVGs written by tools/render_diagrams.py."""
import glob, hashlib, os, re, subprocess, sys
from docx import Document
from docx.enum.section import WD_ORIENT
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Cm, Pt, RGBColor
from markdown_it import MarkdownIt

root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
args = sys.argv[1:]
def opt(name, default):
    return args[args.index(name) + 1] if name in args else default
BOOK = opt("--book", os.path.join(root, "publishing", "build", "clean", "book.md"))
OUT = opt("--out", os.path.join(root, "publishing", "build", "git-and-github-from-zero-to-mastery.docx"))
DIAG = os.path.join(root, "publishing", "build", "diagrams")
TITLE = "Git & GitHub: From Zero to Mastery"
AUTHOR = "Sharif Issah Tingane"
SUB = "A Complete Beginner-to-Expert Guide to Version Control, Collaboration, Automation, Security, and Modern Software Development"

def svg_to_png(svg, png):
    chrome = (glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome") or [None])[0]
    if not chrome: return False
    s = open(svg, encoding="utf-8").read(3000)
    vb = re.search(r'viewBox="([\d. -]+)"', s)
    if not vb: return False
    w, h = int(float(vb.group(1).split()[2])) + 4, int(float(vb.group(1).split()[3])) + 4
    page = png[:-4] + ".html"
    open(page, "w").write(f'<html><body style="margin:0;background:#fff"><img src="file://{svg}" style="width:{w - 4}px;display:block;margin:2px"></body></html>')
    subprocess.run([chrome, "--headless", "--no-sandbox", "--hide-scrollbars", "--force-device-scale-factor=2", f"--window-size={w},{h}",
                    f"--screenshot={png}", "file://" + page], capture_output=True, timeout=90)
    os.remove(page)
    return os.path.exists(png)

doc = Document()
sec = doc.sections[0]
sec.page_width, sec.page_height = Cm(21.0), Cm(29.7)
sec.left_margin = sec.right_margin = Cm(2.2); sec.top_margin = Cm(2.2); sec.bottom_margin = Cm(2.4)
BODY_W = 21.0 - 4.4
st = doc.styles
st["Normal"].font.name = "Liberation Serif"; st["Normal"].font.size = Pt(11)
st["Normal"].element.rPr.rFonts.set(qn("w:eastAsia"), "Liberation Serif")
st["Normal"].paragraph_format.space_after = Pt(6); st["Normal"].paragraph_format.line_spacing = 1.15
for name, size, before, after in (("Heading 1", 20, 0, 10), ("Heading 2", 15, 14, 6), ("Heading 3", 12.5, 10, 4), ("Heading 4", 11, 8, 3), ("Heading 5", 11, 6, 3), ("Heading 6", 11, 6, 3)):
    s = st[name]; s.font.name = "Liberation Sans"; s.font.size = Pt(size); s.font.bold = True; s.font.color.rgb = RGBColor(0x14, 0x21, 0x3D)
    s.element.rPr.rFonts.set(qn("w:eastAsia"), "Liberation Sans"); s.element.rPr.rFonts.set(qn("w:ascii"), "Liberation Sans"); s.element.rPr.rFonts.set(qn("w:hAnsi"), "Liberation Sans")
    s.paragraph_format.space_before = Pt(before); s.paragraph_format.space_after = Pt(after); s.paragraph_format.keep_with_next = True
st["Heading 1"].paragraph_format.page_break_before = True

cp = doc.core_properties
cp.title = TITLE; cp.subject = SUB; cp.author = AUTHOR; cp.language = "en-GB"
cp.keywords = "Git, GitHub, version control, GitHub Actions, security, open source, CI/CD, tutorial"
cp.comments = "Published by Sharif Issah Tingane under the SHARIF TECHNOLOGIES imprint. Text CC BY-NC-SA 4.0; code MIT."

def field(run, instr):
    for t, txt in (("begin", None), (None, instr), ("end", None)):
        if t:
            e = OxmlElement("w:fldChar"); e.set(qn("w:fldCharType"), t); run._r.append(e)
        else:
            e = OxmlElement("w:instrText"); e.set(qn("xml:space"), "preserve"); e.text = txt; run._r.append(e)
fp = sec.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
r = fp.add_run(); r.font.size = Pt(9); field(r, "PAGE")

PPR_ORDER = ["pStyle", "keepNext", "keepLines", "pageBreakBefore", "framePr", "widowControl", "numPr", "suppressLineNumbers", "pBdr", "shd", "tabs",
             "suppressAutoHyphens", "kinsoku", "wordWrap", "overflowPunct", "topLinePunct", "autoSpaceDE", "autoSpaceDN", "bidi", "adjustRightInd",
             "snapToGrid", "spacing", "ind", "contextualSpacing", "mirrorIndents", "suppressOverlap", "jc", "textDirection", "textAlignment",
             "textboxTightWrap", "outlineLvl", "divId", "cnfStyle", "rPr", "sectPr", "pPrChange"]
def ppr_insert(pr, el):
    """insert el into a w:pPr at the position the schema requires"""
    name = el.tag.split("}")[1]; after = PPR_ORDER[PPR_ORDER.index(name) + 1:]
    for child in pr:
        if child.tag.split("}")[1] in after:
            child.addprevious(el); return
    pr.append(el)

def shade(el, fill):
    pr = el.get_or_add_pPr()
    sh = OxmlElement("w:shd"); sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), fill); ppr_insert(pr, sh)
def border_left(p, color="999999"):
    pr = p._p.get_or_add_pPr(); b = OxmlElement("w:pBdr"); l = OxmlElement("w:left")
    for k, v in (("val", "single"), ("sz", "18"), ("space", "6"), ("color", color)): l.set(qn("w:" + k), v)
    b.append(l); ppr_insert(pr, b)

def add_inline(p, tokens, base_bold=False, base_italic=False, size=None):
    bold, ital, link = base_bold, base_italic, None
    for t in tokens:
        ty = t.type
        if ty == "strong_open": bold = True
        elif ty == "strong_close": bold = base_bold
        elif ty == "em_open": ital = True
        elif ty == "em_close": ital = base_italic
        elif ty == "link_open": link = t.attrGet("href")
        elif ty == "link_close": link = None
        elif ty in ("text", "html_inline"):
            run = p.add_run(t.content); run.bold = bold or None; run.italic = ital or None
            if size: run.font.size = Pt(size)
            if link: run.font.color.rgb = RGBColor(0x1F, 0x4E, 0x9C); run.font.underline = True
        elif ty == "code_inline":
            run = p.add_run(t.content); run.font.name = "Liberation Mono"; run.font.size = Pt((size or 11) - 1.5)
            run._r.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), "Liberation Mono"); run.bold = bold or None
            sh = OxmlElement("w:shd"); sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), "EFEFEF"); run._r.get_or_add_rPr().append(sh)
        elif ty == "softbreak": p.add_run(" ")
        elif ty == "hardbreak": p.add_run().add_break()
        elif ty == "image": p.add_run("[image: " + (t.content or "") + "]").italic = True
        if ty == "link_close" and False: pass

def add_code(text, lang=""):
    lines = text.rstrip("\n").split("\n")
    p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(2); p.paragraph_format.space_after = Pt(8); p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.left_indent = Cm(0.2); shade(p._p, "F2F2F2")
    for i, ln in enumerate(lines):
        run = p.add_run(ln); run.font.name = "Liberation Mono"; run.font.size = Pt(8.5)
        run._r.get_or_add_rPr().rFonts.set(qn("w:eastAsia"), "Liberation Mono")
        if i < len(lines) - 1: run.add_break()

def add_table(rows, header_n):
    ncol = max(len(r) for r in rows)
    tb = doc.add_table(rows=len(rows), cols=ncol); tb.style = "Table Grid"; tb.alignment = WD_TABLE_ALIGNMENT.CENTER
    tb.autofit = True
    for i, cells in enumerate(rows):
        for j in range(ncol):
            cell = tb.cell(i, j); cell.text = ""
            p = cell.paragraphs[0]; p.paragraph_format.space_after = Pt(1); p.paragraph_format.line_spacing = 1.0
            if j < len(cells): add_inline(p, cells[j], base_bold=(i < header_n), size=9)
            if i < header_n:
                tcPr = cell._tc.get_or_add_tcPr(); sh = OxmlElement("w:shd"); sh.set(qn("w:val"), "clear"); sh.set(qn("w:color"), "auto"); sh.set(qn("w:fill"), "E3E8F0"); tcPr.append(sh)
        if i < header_n:
            trPr = tb.rows[i]._tr.get_or_add_trPr(); h = OxmlElement("w:tblHeader"); trPr.append(h)
    doc.add_paragraph().paragraph_format.space_after = Pt(2)

md = MarkdownIt("commonmark").enable("table")
text = open(BOOK, encoding="utf-8").read()
tokens = md.parse(text)
n_img = n_tab = n_code = 0
i = 0
def collect_until(i, close):
    depth = 0; j = i
    while True:
        t = tokens[j]
        if t.type == close.replace("_close", "_open"): depth += 1
        if t.type == close:
            depth -= 1
            if depth == 0: return j
        j += 1

def render_block(i, indent=0, in_quote=False, list_ctx=None):
    """renders tokens[i] (a block open or leaf) and returns the next index"""
    global n_img, n_tab, n_code
    t = tokens[i]; ty = t.type
    if ty == "heading_open":
        lvl = min(int(t.tag[1]), 6); inl = tokens[i + 1]
        p = doc.add_paragraph(style=f"Heading {lvl}"); add_inline(p, inl.children)
        return i + 3
    if ty == "paragraph_open":
        inl = tokens[i + 1]
        if list_ctx is not None:
            kind, num, level = list_ctx
            p = doc.add_paragraph(); p.paragraph_format.left_indent = Cm(0.9 + 0.8 * level); p.paragraph_format.first_line_indent = Cm(-0.6)
            p.paragraph_format.space_after = Pt(3)
            p.add_run(("•" if kind == "b" else f"{num}.") + "\t")
            p.paragraph_format.tab_stops.add_tab_stop(Cm(0.9 + 0.8 * level))
        else:
            p = doc.add_paragraph()
            if in_quote: p.paragraph_format.left_indent = Cm(0.8); border_left(p)
        # a paragraph that is only an image
        add_inline(p, inl.children)
        return i + 3
    if ty in ("fence", "code_block"):
        info = (t.info or "").strip().split()[0] if t.info else ""
        if info == "mermaid":
            k = hashlib.sha1(t.content.encode()).hexdigest()[:12]
            png = os.path.join(DIAG, k + ".png"); svg = os.path.join(DIAG, k + ".svg")
            if not os.path.exists(png) and os.path.exists(svg): svg_to_png(svg, png)
            if os.path.exists(png):
                p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                p.add_run().add_picture(png, width=Cm(min(BODY_W, 15.5))); n_img += 1
                return i + 1
        add_code(t.content, info); n_code += 1
        return i + 1
    if ty == "html_block":
        add_code(t.content); return i + 1
    if ty == "hr":
        p = doc.add_paragraph(); p.paragraph_format.space_after = Pt(2)
        pr = p._p.get_or_add_pPr(); b = OxmlElement("w:pBdr"); bt = OxmlElement("w:bottom")
        for k, v in (("val", "single"), ("sz", "6"), ("space", "1"), ("color", "AAAAAA")): bt.set(qn("w:" + k), v)
        b.append(bt); ppr_insert(pr, b); return i + 1
    if ty == "blockquote_open":
        end = collect_until(i, "blockquote_close"); j = i + 1
        while j < end: j = render_block(j, indent, True, list_ctx)
        return end + 1
    if ty in ("bullet_list_open", "ordered_list_open"):
        close = ty.replace("_open", "_close"); end = collect_until(i, close)
        level = 0 if list_ctx is None else list_ctx[2] + 1
        num = int(t.attrGet("start") or 1) if ty == "ordered_list_open" else 0
        j = i + 1
        while j < end:
            # list_item_open ... list_item_close
            ie = collect_until(j, "list_item_close"); k = j + 1
            ctx = ("b" if ty == "bullet_list_open" else "o", num, level)
            first = True
            while k < ie:
                if tokens[k].type == "paragraph_open" and first:
                    k = render_block(k, indent, in_quote, ctx); first = False
                else:
                    k = render_block(k, indent, in_quote, ctx if tokens[k].type in ("bullet_list_open", "ordered_list_open") else None)
                    first = False
            num += 1; j = ie + 1
        return end + 1
    if ty == "table_open":
        end = collect_until(i, "table_close"); rows = []; header_n = 0; cur = None; j = i + 1
        while j < end:
            tt = tokens[j]
            if tt.type == "thead_open": in_head = True
            elif tt.type == "thead_close": header_n = len(rows)
            elif tt.type == "tr_open": cur = []
            elif tt.type == "tr_close": rows.append(cur)
            elif tt.type in ("th_open", "td_open"): cur.append(tokens[j + 1].children or [])
            j += 1
        add_table(rows, header_n); n_tab += 1
        return end + 1
    return i + 1

while i < len(tokens):
    i = render_block(i)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
z = doc.settings.element.find(qn("w:zoom"))
if z is not None and z.get(qn("w:percent")) is None: z.set(qn("w:percent"), "100")
doc.save(OUT)
print(f"wrote {os.path.relpath(OUT, root)}: {n_tab} tables, {n_code} code blocks, {n_img} diagrams")
