#!/usr/bin/env python3
"""Every fenced ```text block in the manuscript that starts with '$ ' is a recorded command transcript.
Each of its lines must occur in a recorded output file under verification/ (expected-*.txt, recorded-*.txt).
This stops typed-from-memory or drifted output from entering the book."""
import glob, os, re, sys
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
recorded = set()
for pat in ("expected-*.txt", "recorded-*.txt", "results/**/*.txt"):
    for f in glob.glob(os.path.join(root, "verification", "**", pat), recursive=True):
        recorded.update(l.rstrip("\n") for l in open(f, errors="replace"))
bad = blocks = 0
for f in sorted(glob.glob(os.path.join(root, "manuscript", "**", "*.md"), recursive=True)):
    text = open(f, encoding="utf-8").read()
    for m in re.finditer(r"```text\n(.*?)```", text, re.S):
        body = m.group(1).rstrip("\n").split("\n")
        if not body or not body[0].startswith("$ "): continue
        blocks += 1
        for line in body:
            if line.strip() == "" or line in recorded: continue
            if re.match(r"git version \d+\.\d+\.\d+", line) and "git version <version>" in recorded: continue
            print(f"NOT RECORDED {os.path.relpath(f, root)}: {line!r}"); bad += 1
print(f"transcript blocks checked: {blocks}, unrecorded lines: {bad}")
sys.exit(1 if bad else 0)
