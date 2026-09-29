#!/usr/bin/env python3
"""Chapter cross-references in manuscript, exercises and solutions.
Authoring:  write  Chapter [[key]]  (key from tools/toc_data.py).
--expand :  rewrites [[key]] -> NN<!--ref:key-->   (number derived from the outline; invisible annotation)
--fix    :  re-syncs every NN<!--ref:key--> with the current outline (run after any renumbering)
--check  :  (default) fails on: leftover [[key]], stale numbers, unknown keys, or unannotated 'Chapter N' mentions.
Rule: write the word Chapter before every number ('Chapter 4 and Chapter 7', never 'Chapters 4 and 7')."""
import glob, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import toc_data as T
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
num = {c[1]: i + 1 for i, c in enumerate(T.C)}
mode = "--expand" if "--expand" in sys.argv else "--fix" if "--fix" in sys.argv else "--check"
files = [f for pat in ("manuscript/**/*.md", "exercises/*.md", "solutions/*.md") for f in glob.glob(os.path.join(root, pat), recursive=True)]
ANN = re.compile(r"(\d+)<!--ref:([a-z_0-9]+)-->")
errs = 0
for f in sorted(files):
    text = open(f, encoding="utf-8").read(); orig = text
    body_no_code = re.sub(r"```.*?```", lambda m: m.group(0), text, flags=re.S)
    if mode in ("--expand", "--fix"):
        def ex(m):
            k = m.group(1)
            if k not in num: print(f"{f}: unknown key [[{k}]]"); return m.group(0)
            return f"{num[k]}<!--ref:{k}-->"
        text = re.sub(r"\[\[([a-z_0-9]+)\]\]", ex, text)
        text = ANN.sub(lambda m: f"{num[m.group(2)]}<!--ref:{m.group(2)}-->" if m.group(2) in num else m.group(0), text)
        if text != orig: open(f, "w", encoding="utf-8").write(text); print("updated", os.path.relpath(f, root))
        continue
    # check
    rel = os.path.relpath(f, root)
    prose = re.sub(r"```.*?```", "", text, flags=re.S)
    prose = "\n".join(l for l in prose.split("\n") if not l.startswith("#"))  # headings are not references
    for m in re.finditer(r"\[\[([a-z_0-9]+)\]\]", prose): print(f"{rel}: unexpanded [[{m.group(1)}]] (run tools/resolve_refs.py --expand)"); errs += 1
    for m in ANN.finditer(prose):
        if m.group(2) not in num: print(f"{rel}: unknown ref key {m.group(2)}"); errs += 1
        elif int(m.group(1)) != num[m.group(2)]: print(f"{rel}: stale number {m.group(1)} for {m.group(2)} (should be {num[m.group(2)]})"); errs += 1
    for m in re.finditer(r"\bChapters?\s+(\d+)(?!\d)(?!<!--ref:)", prose):
        print(f"{rel}: unannotated chapter number '{m.group(0)}' (use Chapter [[key]])"); errs += 1
print(f"cross-reference files: {len(files)}, problems: {errs}")
sys.exit(1 if errs else 0)
