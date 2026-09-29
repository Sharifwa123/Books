#!/usr/bin/env python3
"""Manuscript structure/consistency checks. Use --release for the publication gate.
Checks per chapter file: front matter vs toc_data, title line, checkpoint headings order, banned filler phrases,
ledger ids exist, New Vocabulary terms exist in glossary with matching first chapter, exercises+solutions files exist,
mermaid blocks have a nearby text description marker, verification-pending markers counted."""
import csv, glob, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import toc_data as T
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
release = "--release" in sys.argv
num = {c[1]: i + 1 for i, c in enumerate(T.C)}; ch = {c[1]: c for c in T.C}
ledger = {r["id"]: r for r in csv.DictReader(open(os.path.join(root, "research", "research-ledger.csv")))}
gloss = {}
for r in csv.DictReader(open(os.path.join(root, "glossary", "glossary-master.csv"))):
    gloss[r["term"].strip().lower()] = r
CHECK = ["What You Learned", "New Vocabulary", "Commands Learned", "Common Mistakes", "Practice", "Self-Test", "Before Moving On"]
BANNED = [r"\betc\.", r"\band so on\b", r"\band so forth\b", r"\bas we all know\b", r"\bobviously\b", r"\bsimply just\b", r"\bjust simply\b"]
errs, warns, pending = [], [], 0
def fm(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m: return None, text
    d = {}
    for line in m.group(1).split("\n"):
        line = line.split("#")[0].rstrip()
        if ":" not in line: continue
        k, v = line.split(":", 1); v = v.strip()
        if v.startswith("["): v = [x.strip() for x in v.strip("[]").split(",") if x.strip()]
        d[k.strip()] = v
    return d, text[m.end():]
files = sorted(glob.glob(os.path.join(root, "manuscript", "parts", "*", "ch*.md")))
seen = set()
for p in files:
    rel = os.path.relpath(p, root); text = open(p, errors="replace").read()
    d, body = fm(text)
    if d is None: errs.append(f"{rel}: missing front matter"); continue
    k = d.get("key")
    if k not in ch: errs.append(f"{rel}: unknown key {k}"); continue
    seen.add(k); c = ch[k]
    if int(d.get("number", -1)) != num[k]: errs.append(f"{rel}: number {d.get('number')} != {num[k]}")
    if d.get("tag") != c[3]: errs.append(f"{rel}: tag {d.get('tag')} != {c[3]}")
    if d.get("first_read") != c[4]: errs.append(f"{rel}: first_read mismatch")
    if d.get("status") not in ("draft", "reviewed", "verified"): errs.append(f"{rel}: bad status")
    if sorted(d.get("requires", [])) != sorted(c[5]): errs.append(f"{rel}: requires {d.get('requires')} != {c[5]}")
    if f"ch{num[k]:02d}-" not in os.path.basename(p): errs.append(f"{rel}: filename must start ch{num[k]:02d}-")
    m = re.search(r"^# Chapter (\d+) — (.+?)\s+\[(Core|Deep)\]\s*$", body, re.M)
    if not m or int(m.group(1)) != num[k] or m.group(2) != c[2] or m.group(3) != c[3]: errs.append(f"{rel}: title line must be '# Chapter {num[k]} — {c[2]} [{c[3]}]'")
    heads = re.findall(r"^## (.+?)\s*$", body, re.M)
    idx = [heads.index(h) if h in heads else -1 for h in CHECK]
    if -1 in idx or idx != sorted(idx): errs.append(f"{rel}: checkpoint headings missing/out of order: {[h for h,i in zip(CHECK,idx) if i==-1]}")
    for h in ("How this chapter was checked", "Where this leads"):
        if h not in heads: errs.append(f"{rel}: missing '## {h}'")
    prose = re.sub(r"```.*?```", "", body, flags=re.S)
    for rx in BANNED:
        for mm in re.finditer(rx, prose, re.I): errs.append(f"{rel}: banned filler phrase '{mm.group(0)}'")
    for lid in d.get("ledger", []):
        if lid not in ledger: errs.append(f"{rel}: unknown ledger id {lid}")
        elif release and not ledger[lid]["evidence_class"].startswith(("Officially", "Both", "Time-sensitive (verified)", "Not applicable")): errs.append(f"{rel}: release gate: {lid} not officially verified")
    sec = re.search(r"^## New Vocabulary\s*\n(.*?)(?=^## )", body, re.S | re.M)
    terms = re.findall(r"^- \*\*(.+?)\*\*", sec.group(1), re.M) if sec else []
    for t in terms:
        g = gloss.get(t.strip().lower())
        if not g: errs.append(f"{rel}: vocabulary term '{t}' missing in glossary")
        elif g["first_chapter_key"] != k: errs.append(f"{rel}: glossary first_chapter for '{t}' is {g['first_chapter_key']}")
    for t in re.findall(r"> \*\*New term: (.+?)\.\*\*", body):
        if t.strip().lower() not in gloss: errs.append(f"{rel}: 'New term: {t}' missing in glossary")
    pending += len(re.findall(r"Verification pending", body))
    if d.get("status") == "draft" and release: errs.append(f"{rel}: release gate: status draft")
    for f, label in (("exercises", "exercises"), ("solutions", "solutions")):
        q = os.path.join(root, f, f"ch{num[k]:02d}-{label}.md")
        if not os.path.exists(q): errs.append(f"{rel}: missing {os.path.relpath(q, root)}")
        elif f == "exercises":
            ex = open(q).read()
            for lv in ("Level 1", "Level 2", "Level 3", "Level 4", "Level 5"):
                if lv not in ex: errs.append(f"{os.path.relpath(q, root)}: missing {lv}")
    for mm in re.finditer(r"```mermaid.*?```\s*\n\s*\n?(.{0,4})", body, re.S):
        pass
    if "```mermaid" in body and "*Diagram description:*" not in body: errs.append(f"{rel}: mermaid diagram without '*Diagram description:*' text alternative")
for r in glob.glob(os.path.join(root, "manuscript", "parts", "*", "*.md")):
    if not os.path.basename(r).startswith("ch"): warns.append(f"non-chapter file in parts: {os.path.relpath(r, root)}")
print(f"chapters drafted: {len(seen)} / {len(T.C)} | glossary terms: {len(gloss)} | verification-pending markers: {pending}")
for w in warns: print(" warn:", w)
for e in errs: print(" -", e)
if release and pending: print(f" - release gate: {pending} 'Verification pending' markers remain"); errs.append("pending")
sys.exit(1 if errs else 0)
