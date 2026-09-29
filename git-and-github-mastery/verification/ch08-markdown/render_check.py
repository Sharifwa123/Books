#!/usr/bin/env python3
"""Render each Markdown snippet with markdown-it-py (CommonMark preset + tables) and compare to recorded HTML.
This checks how the syntax taught in Chapter 8 is interpreted by a CommonMark-based renderer; GitHub's own
renderer is a separate, unverified matter (see ledger). Regenerate expectations with --update."""
import json, os, sys
from markdown_it import MarkdownIt
here = os.path.dirname(__file__)
md = MarkdownIt("commonmark").enable("table")
cases = json.load(open(os.path.join(here, "cases.json")))
exp_path = os.path.join(here, "expected-html.json")
out = {c["id"]: md.render(c["md"]) for c in cases}
if "--update" in sys.argv:
    json.dump(out, open(exp_path, "w"), indent=1, ensure_ascii=False); print("updated", len(out)); sys.exit(0)
exp = json.load(open(exp_path)); bad = 0
for k, v in out.items():
    if exp.get(k) != v: print(f"DIFF {k}\n expected: {exp.get(k)!r}\n actual:   {v!r}"); bad += 1
print(f"markdown cases checked: {len(out)}, differing: {bad}"); sys.exit(1 if bad else 0)
