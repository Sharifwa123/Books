#!/usr/bin/env python3
"""Markdown examples in Chapter 8 are generated from verification/ch08-markdown (cases.json + expected-html.json).
Each example begins with a marker  <!--md-case:ID-->  followed by a four-backtick markdown block and a ```html block.
This check fails if either block differs from the recorded case (so the book cannot drift from what the renderer really did)."""
import glob, json, os, re, sys
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
cases = {c["id"]: c["md"] for c in json.load(open(os.path.join(root, "verification/ch08-markdown/cases.json")))}
html = json.load(open(os.path.join(root, "verification/ch08-markdown/expected-html.json")))
bad = n = 0
for f in glob.glob(os.path.join(root, "manuscript", "**", "*.md"), recursive=True):
    t = open(f, encoding="utf-8").read()
    for m in re.finditer(r"<!--md-case:([a-z0-9-]+)-->\s*\n\*\*Source\*\*\n````markdown\n(.*?)````\n\n\*\*Rendered as HTML.*?\*\*\n```html\n(.*?)```", t, re.S):
        n += 1; cid = m.group(1)
        if cid not in cases: print(f"unknown case {cid}"); bad += 1; continue
        if m.group(2) != cases[cid]: print(f"{os.path.relpath(f, root)}: markdown block for {cid} differs"); bad += 1
        if m.group(3) != html[cid]: print(f"{os.path.relpath(f, root)}: html block for {cid} differs"); bad += 1
print(f"markdown examples checked: {n}, problems: {bad}"); sys.exit(1 if bad else 0)
