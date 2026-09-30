#!/usr/bin/env python3
"""Exports the finished book text only (no planning, research notes, ledger data, tooling or drafting markers) as one
Markdown file plus a manifest, and fails if development artefacts are found in the text.
Output: publishing/build/clean/book.md and MANIFEST.txt.  Usage: export_clean.py [--out DIR]
Included: manuscript/front-matter, parts, appendices, back-matter.  Excluded by construction: planning/, research/,
verification/, tools/, .github/. Exercises are appended to their chapters and the solutions form one back-matter section.
Placeholders that are intentionally part of the text (ISBN, address, author biography) are listed, not hidden."""
import glob, hashlib, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import bookparts as BP
import toc_data as T
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
out = os.path.join(root, "publishing", "build", "clean")
if "--out" in sys.argv: out = sys.argv[sys.argv.index("--out") + 1]
os.makedirs(out, exist_ok=True)
M = os.path.join(root, "manuscript")
def key(f):
    b = os.path.basename(f); m = re.match(r"(?:ch)?(\d+)", b); return int(m.group(1)) if m else 999
files = sorted(glob.glob(f"{M}/front-matter/*.md"))
files += sorted(glob.glob(f"{M}/parts/*/ch*.md"), key=key)
files += sorted(glob.glob(f"{M}/appendices/*.md"))
files += ["@solutions", f"{M}/back-matter/glossary.md", f"{M}/back-matter/author-and-publisher.md"]
FORBIDDEN = [(r"STOPPED HERE", "drafting marker"), (r"\bTBD\b|FIXME|lorem ipsum", "unfinished text"), (r"session_[0-9A-Za-z]{8,}|Claude-Session|Co-Authored-By", "working-session identifier or commit trailer"),
             (r"gate [A-F]\b", "internal process gate"), (r"planning/", "internal repository path"), (r"\[\[[a-z0-9_]+\]\]", "unresolved cross-reference"),
             ]
WARN = []
INFO = r"research/[a-z-]+"   # references to the public evidence files are kept by decision: see publishing/research-file-references-audit.md
problems, warns, parts, manifest = [], [], [], []
named = 0
for f in files:
    t = BP.solutions_text([(i + 1, c[2]) for i, c in enumerate(T.C)]) if f == "@solutions" else open(f, encoding="utf-8").read()
    mm = re.search(r"/ch(\d+)-", f)
    if mm: t = BP.with_exercises(int(mm.group(1)), re.sub(r"\A---\n.*?\n---\n", "", t, flags=re.S))
    t = re.sub(r"\A---\n.*?\n---\n", "", t, flags=re.S)
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    rel = "solutions" if f == "@solutions" else os.path.relpath(f, root)
    for pat, why in FORBIDDEN:
        for m in re.finditer(pat, t, flags=re.M):
            line = t[:m.start()].count("\n") + 1
            problems.append(f"{rel}:{line}: {why}: {m.group(0)!r}")
    named += len(re.findall(INFO, t))
    for pat, why in WARN:
        for m in re.finditer(pat, t): warns.append(f"{rel}:{t[:m.start()].count(chr(10)) + 1}: {why}: {m.group(0)!r}")
    parts.append(t.strip()); manifest.append(f"{hashlib.sha256(t.encode()).hexdigest()}  {rel}")
book = "\n\n".join(parts) + "\n"
open(os.path.join(out, "book.md"), "w", encoding="utf-8").write(book)
ph = sorted(set(re.findall(r"\*{0,2}\[[^\]\n]*(?:TO BE [A-Z]+|to be supplied|PLACEHOLDER|placeholder)[^\]\n]*\]", book)))
open(os.path.join(out, "MANIFEST.txt"), "w").write("\n".join(manifest) + "\n")
print(f"exported {len(files)} files, {len(book.split())} words -> {os.path.relpath(out, root)}/book.md")
print("intentional placeholders present:", len(ph))
print(f"{named} reference(s) to public evidence files under research/ (kept by decision)")
for p in ph[:20]: print("  ", p)
if warns:
    print(f"{len(warns)} warning(s):")
    for w in warns: print("  ", w)
if problems:
    print(f"{len(problems)} development artefact(s) found in the book text:")
    for p in problems: print("  ", p)
    sys.exit(1)
print("clean export: no development artefacts found")
