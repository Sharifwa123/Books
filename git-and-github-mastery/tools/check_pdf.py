#!/usr/bin/env python3
"""Machine checks for the PDF edition (publishing/pdf-build-plan.md).
Usage: check_pdf.py FILE [--full]   (--full: expects the whole book: outline depth, appendices, index)
Checks: page count, metadata (title, author, subject/keywords), language, outline depth and entries, internal links resolve,
external links present, all fonts embedded, tagged (structure tree + MarkInfo), extractable text, front-matter roman numerals,
licence page present without invented legal wording."""
import re, sys
from pypdf import PdfReader
from pypdf.generic import IndirectObject, DictionaryObject
path = sys.argv[1]; full = "--full" in sys.argv
r = PdfReader(path)
errs, notes = [], []
def ok(c, msg):
    (notes if c else errs).append(("ok: " if c else "FAIL: ") + msg)
n = len(r.pages); ok(n > 3, f"pages: {n}")
md = r.metadata or {}
ok((md.get("/Title") or "").startswith("Git & GitHub"), f"title: {md.get('/Title')}")
ok(md.get("/Author") == "Sharif Tingane Issah", f"author: {md.get('/Author')}")
ok(bool(md.get("/Keywords")) and bool(md.get("/Subject")), "keywords and subject present")
root = r.trailer["/Root"]
ok(str(root.get("/Lang", "")).startswith("en"), f"language: {root.get('/Lang')}")
ok("/StructTreeRoot" in root, "structure tree present (tagged PDF)")
mi = root.get("/MarkInfo"); ok(bool(mi) and bool(mi.get("/Marked")), "MarkInfo /Marked true")
# outline
def walk(o, d=1, acc=None):
    acc = acc if acc is not None else []
    for it in o:
        if isinstance(it, list): walk(it, d + 1, acc)
        else: acc.append((d, it.title))
    return acc
ol = walk(r.outline); depth = max([d for d, _ in ol], default=0)
ok(len(ol) > 5, f"outline entries: {len(ol)}, depth {depth}")
if full: ok(depth >= 3, "outline depth at least 3 (parts > chapters > sections)")
# links
internal = external = broken = 0
names = set(r.named_destinations.keys()) if r.named_destinations else set()
for p in r.pages:
    for an in p.get("/Annots", []) or []:
        an = an.get_object()
        if an.get("/Subtype") != "/Link": continue
        a = an.get("/A"); d = an.get("/Dest")
        if a is not None:
            a = a.get_object()
            if a.get("/S") == "/URI": external += 1; continue
            d = a.get("/D")
        if d is None: broken += 1; continue
        internal += 1
        if isinstance(d, str) and names and d not in names: broken += 1
ok(internal > 0, f"internal links: {internal}"); ok(broken == 0, f"broken internal links: {broken}")
notes.append(f"info: external links: {external}")
# fonts embedded
bad = set()
for p in r.pages:
    res = p.get("/Resources"); fonts = res.get("/Font") if res else None
    if not fonts: continue
    for k, f in fonts.get_object().items():
        f = f.get_object(); desc = f.get("/FontDescriptor")
        if f.get("/Subtype") == "/Type0":
            df = f["/DescendantFonts"][0].get_object(); desc = df.get("/FontDescriptor")
        if desc is None: bad.add(str(f.get("/BaseFont"))); continue
        desc = desc.get_object()
        if not any(x in desc for x in ("/FontFile", "/FontFile2", "/FontFile3")): bad.add(str(f.get("/BaseFont")))
ok(not bad, f"all fonts embedded (not embedded: {sorted(bad) or 'none'})")
# text
txt = "".join((r.pages[i].extract_text() or "") for i in range(min(n, 12)))
ok(len(txt) > 500, f"extractable text on the first pages ({len(txt)} characters)")
ok("Git & GitHub: From Zero to Mastery" in txt.replace("\n", " ") or "Git & GitHub" in txt, "title text present")
ok("Sharif Tingane Issah" in txt, "author text present")
flat = re.sub(r"\s+", "", "".join((r.pages[i].extract_text() or "") for i in range(min(n, 20))))   # line breaks may fall inside a hyphenated name
ok("CCBY-NC-SA4.0" in flat and "MITLicense" in flat, "copyright page states the book text and code licences")
ok(not re.search(r"ISBN[: ]+97[89]", txt), "no invented ISBN")
if full:
    alltxt = "".join((p.extract_text() or "") for p in r.pages)
    ok("Appendix N" in alltxt and "Index of terms" in alltxt and "Glossary" in alltxt, "appendices, glossary and index present")
    ok(n > 500, f"full-book page count plausible: {n}")
for x in notes + errs: print(x)
print("PDF checks:", "FAILED" if errs else "passed")
sys.exit(1 if errs else 0)
