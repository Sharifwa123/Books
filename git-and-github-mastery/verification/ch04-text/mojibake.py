#!/usr/bin/env python3
"""Show what happens when text is written in one encoding and read as another. Deterministic; --check compares to expected."""
import os, sys
word = "café"
hexs = lambda b: " ".join(f"{x:02x}" for x in b)
utf8, latin1 = word.encode("utf-8"), word.encode("latin-1")
try:
    latin1.decode("utf-8"); strict = "no error"
except UnicodeDecodeError as e:
    strict = f"UnicodeDecodeError ({e.reason})"
bread = chr(0x1F35E).encode("utf-8")
out = [
 f"the word:                 {word}",
 f"stored as UTF-8 bytes:    {hexs(utf8)}   ({len(utf8)} bytes for {len(word)} characters)",
 f"the same bytes read as Latin-1: {utf8.decode('latin-1')}",
 f"stored as Latin-1 bytes:  {hexs(latin1)}   ({len(latin1)} bytes)",
 f"Latin-1 bytes read as UTF-8:    {strict}",
 f"with errors replaced:      {latin1.decode('utf-8', 'replace')}",
 f"emoji U+1F35E as UTF-8:   {hexs(bread)}   ({len(bread)} bytes for 1 character)",
]
text = "\n".join(out) + "\n"
if "--check" in sys.argv:
    exp = open(os.path.join(os.path.dirname(__file__), "expected-mojibake.txt")).read()
    if exp != text: print("DIFF\n" + text); sys.exit(1)
    print("OK mojibake"); sys.exit(0)
sys.stdout.write(text)
