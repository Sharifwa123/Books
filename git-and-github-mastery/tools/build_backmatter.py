#!/usr/bin/env python3
"""Builds the back matter that is generated from data files:
  manuscript/back-matter/glossary.md          (all glossary terms, alphabetical)
  manuscript/appendices/appendix-e-git-terminology-map.md
  manuscript/appendices/appendix-f-github-terminology-map.md
  manuscript/appendices/appendix-n-sources-and-verification-log.md
Run from anywhere; then run tools/resolve_refs.py --expand."""
import csv, os, sys, collections
sys.path.insert(0, os.path.dirname(__file__))
import toc_data as T
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
num = {c[1]: i + 1 for i, c in enumerate(T.C)}
part_of = {c[1]: c[0] for c in T.C}
gl = sorted(csv.DictReader(open(os.path.join(root, "glossary", "glossary-master.csv"), encoding="utf-8")), key=lambda r: r["term"].lower())
def w(rel, text):
    p = os.path.join(root, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(text); print("wrote", rel, len(text.split()), "words")
def cell(s): return s.replace("|", "/").replace("\n", " ")

# Glossary
L = ["# Glossary", "", "Every term that the book defines, in alphabetical order. Each entry gives a simple definition, a technical one, an example, related terms and the chapter where the term is first explained.", ""]
cur = ""
for r in gl:
    ch = r["term"][0].upper()
    if ch != cur: cur = ch; L += [f"## {cur}", ""]
    esc = lambda x: x.replace("<", "\\<")   # a bare <name> would be swallowed as an HTML tag
    L += [f"**{r['term']}.** {esc(r['simple_definition'])}", "", f"*Technically:* {esc(r['technical_definition'])} *Example:* {esc(r['example'])}", "",
          f"*Related:* {r['related'] or 'none listed'}. *First explained in* Chapter [[{r['first_chapter_key']}]].", ""]
w("manuscript/back-matter/glossary.md", "\n".join(L))

# Terminology maps
def table(rows):
    out = ["| Term | Meaning in one line | First explained |", "|---|---|---|"]
    for r in rows: out.append(f"| {cell(r['term'])} | {cell(r['simple_definition'])} | Chapter [[{r['first_chapter_key']}]] |")
    return out
git_rows = [r for r in gl if r["first_chapter_key"] in part_of and part_of[r["first_chapter_key"]] <= 3]
gh_rows = [r for r in gl if r["first_chapter_key"] in part_of and part_of[r["first_chapter_key"]] >= 4]
w("manuscript/appendices/appendix-e-git-terminology-map.md", "\n".join(["# Appendix E — Git Terminology Map", "",
  f"The {len(git_rows)} terms first explained in Parts I to IV (computers, version control, Git itself), with a one-line meaning and the chapter to read. Terms about GitHub are in Appendix F. The full definitions are in the Glossary.", ""] + table(git_rows)))
w("manuscript/appendices/appendix-f-github-terminology-map.md", "\n".join(["# Appendix F — GitHub Terminology Map", "",
  f"The {len(gh_rows)} terms first explained from Part V onwards (GitHub and what is built on it). **GitHub's names and features change**; where a term depends on the platform, the chapter says which documentation it was checked against. The full definitions are in the Glossary.", ""] + table(gh_rows)))

# Sources and verification log
R = list(csv.DictReader(open(os.path.join(root, "research", "research-ledger.csv"), encoding="utf-8")))
cls = collections.Counter(r["evidence_class"] for r in R)
open_rows = [r for r in R if r["status"].startswith("UNVERIFIED")]
M = list(csv.DictReader(open(os.path.join(root, "research", "sources-manifest.csv"), encoding="utf-8")))
hosts = collections.Counter(r["url"].split("/")[2] for r in M if r["url"].startswith("http"))
L = ["# Appendix N — Sources and Verification Log", "",
 "This book separates what was **checked** from what was **assumed**. Every claim that could be wrong was entered in a research ledger with an evidence class. This appendix summarises the ledger and lists what remains open. The full ledger is the file `research/research-ledger.csv` in the book's repository, and the list of fetched sources with their SHA-256 values is `research/sources-manifest.csv`.", "",
 "## N.1 Evidence classes", "", "| Evidence class | Rows | Meaning |", "|---|---|---|"]
meaning = {"Officially verified (docs only)": "compared with an official source; not run", "Both officially verified and locally tested": "compared with an official source and run on the author's computer", "Locally tested": "run on the author's computer; no official source consulted", "Time-sensitive (unverified)": "about a platform that changes; not yet checked", "Needs re-verification": "checked once; must be checked again before publication", "Not applicable": "a general concept with no product claim"}
for k, v in cls.most_common(): L.append(f"| {k} | {v} | {meaning.get(k, '')} |")
L += ["", f"Total rows: {len(R)}.", "",
 "## N.2 What was tested, and where", "",
 "- **Git:** every command shown was run in Bash and zsh on Git 2.43.0 (the Linux package on the author's computer) and re-run in continuous integration on the runner's Git (2.55.0) and on Git 2.56.0 built from source. Where newer versions print different text, alternate recordings are kept and noted.",
 "- **GitHub:** statements were compared with the `github/docs` repository at commit `2eaab0b` (29 September 2026) and the `github/site-policy` repository, both read from their public sources. **No statement about GitHub was checked on a live account**; the book says so wherever it matters (a signed-in account of the plan).",
 "- **Licences:** licence summaries come from GitHub's `choosealicense.com` data and the SPDX licence list (secondary sources); the official pages could not be read. **The book contains no licence statement for itself**, because that is a decision for its rights holder.",
 "- **Other tools:** the GitHub CLI 2.102.0 (checksum-verified download), `git-filter-repo` 2.47.0, PyYAML 6.0.1, OpenSSL.", "",
 "## N.3 Where the sources came from", "", "| Host | Files fetched |", "|---|---|"]
for h, n in hosts.most_common(): L.append(f"| {h} | {n} |")
L += ["", "Files fetched with the book's tool are hashed in the manifest, so a reader can check that a source has not changed since it was read.", "",
 f"## N.4 What is still open ({len(open_rows)} ledger rows)", "",
 "These rows were planned during research and could not be verified from an official source at the time (the official hosts were blocked, or the claim needs a live account). Many are covered in part by later, chapter-level rows; they remain open until each claim is checked. Treat each as an **individual dependency**, not as a reason to distrust the rest.", "",
 "| Row | Topic | Claim to verify |", "|---|---|---|"]
for r in open_rows: L.append(f"| {r['id']} | {cell(r['topic'])} | {cell(r['claim_to_verify'][:120])} |")
L += ["", "## N.5 How to use this log", "", "1. Before relying on a fact about GitHub, find its chapter's ledger row and read its status and date.", "2. Prefer GitHub's current documentation for your plan over this book for anything time-sensitive.", "3. If you find an error, the ledger tells you where the claim came from, so it can be corrected at the source."]
w("manuscript/appendices/appendix-n-sources-and-verification-log.md", "\n".join(L))
