#!/usr/bin/env python3
"""Check that relative Markdown links and image references resolve to files/anchors-free paths.
External (http/https/mailto) links are NOT fetched here (see research notes: no network relay is used)."""
import os, re, sys
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
pat = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
bad = 0; n = 0
for base, dirs, files in os.walk(root):
    dirs[:] = [d for d in dirs if d not in (".git", "results", "__pycache__")]
    for f in files:
        if not f.endswith(".md"): continue
        p = os.path.join(base, f)
        text = open(p, errors="replace").read()
        text = re.sub(r"````.*?````", "", text, flags=re.S)
        text = re.sub(r"```.*?```", "", text, flags=re.S)  # ignore code blocks
        text = re.sub(r"`[^`\n]*`", "", text)  # ignore inline code
        for m in pat.finditer(text):
            t = m.group(1)
            if re.match(r"^[a-z]+:", t) or t.startswith("#"): continue
            n += 1
            path = os.path.normpath(os.path.join(base, t.split("#")[0]))
            if not os.path.exists(path):
                print(f"BROKEN {os.path.relpath(p, root)} -> {t}"); bad += 1
print(f"links checked: {n}, broken: {bad}")
sys.exit(1 if bad else 0)
