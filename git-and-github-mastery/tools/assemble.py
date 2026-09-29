#!/usr/bin/env python3
"""Author's helper: expand transcript markers in a chapter template into recorded output blocks.
Marker forms (alone on a line, optionally after '> ' inside a callout):
    {{T name a-b}}    lines a..b (1-based, inclusive) of verification/*/expected-<name>.bash.txt
    {{TZ name a-b}}   the same from the zsh recording
    {{T name@alt a-b}} the recorded variant for another Git version (expected-<name>.<shell>.alt.txt)
The result is a normal fenced ```text block followed by a caption. tools/check_transcripts.py then verifies
every line of every block against the recordings, so a wrong range cannot slip into the book.
Usage: assemble.py template.md output.md"""
import glob, os, re, sys
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
def path(name, shell):
    alt = name.endswith("@alt"); name = name[:-4] if alt else name   # name@alt: the recorded variant for another Git version
    hits = glob.glob(os.path.join(root, "verification", "*", f"expected-{name}.{shell}{'.alt' if alt else ''}.txt"))
    if len(hits) != 1: raise SystemExit(f"recording name {name!r} matches {len(hits)} files")
    return hits[0]
def expand(m):
    quote, kind, name, a, b = m.group(1), m.group(2), m.group(3), int(m.group(4)), int(m.group(5))
    shell = "zsh" if kind == "TZ" else "bash"
    p = path(name, shell); lines = open(p).read().split("\n")
    if b > len(lines): raise SystemExit(f"{name}: range {a}-{b} beyond {len(lines)} lines")
    body = ["```text"] + lines[a - 1:b] + ["```", "", f"*Recorded in {'zsh' if shell == 'zsh' else 'Bash'}; `{os.path.relpath(p, os.path.join(root, 'verification'))}`.*"]
    return "\n".join((quote + l).rstrip() if quote else l for l in body)
tpl = open(sys.argv[1], encoding="utf-8").read()
out = re.sub(r"(?m)^((?:> )?)\{\{(TZ?) (\w[\w@-]*) (\d+)-(\d+)\}\}", expand, tpl)
open(sys.argv[2], "w", encoding="utf-8").write(out)
print("assembled", sys.argv[2], len(out.split()), "words")
