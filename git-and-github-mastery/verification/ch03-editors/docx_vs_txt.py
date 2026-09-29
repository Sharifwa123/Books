#!/usr/bin/env python3
"""Show why a word-processor file is not plain text: a .docx is a ZIP container holding XML parts,
while a .txt file's bytes are just its characters. Prints a deterministic report; --check compares to expected."""
import io, sys, zipfile, tempfile, os
import docx
d = docx.Document(); d.add_paragraph("Fresh bread every morning.")
buf = io.BytesIO(); d.save(buf); raw = buf.getvalue()
txt = "Fresh bread every morning.\n".encode()
out = []
out.append(f"plain text file: {len(txt)} bytes; starts with: {txt[:12]!r}")
out.append(f"word-processor file starts with bytes: {raw[:2]!r} (the ZIP signature 'PK')")
out.append(f"is it a ZIP archive? {zipfile.is_zipfile(io.BytesIO(raw))}")
names = sorted(zipfile.ZipFile(io.BytesIO(raw)).namelist())
out.append("contains parts (first four, sorted): " + ", ".join(names[:4]))
out.append("has word/document.xml: " + str("word/document.xml" in names))
out.append("visible text is about %d bytes; the file holds far more than the text" % len("Fresh bread every morning."))
out.append("file is larger than its text: " + str(len(raw) > 10 * len(txt)))
text = "\n".join(out) + "\n"
if "--check" in sys.argv:
    exp = open(os.path.join(os.path.dirname(__file__), "expected-docx.txt")).read()
    if exp != text: print("DIFF\n" + text); sys.exit(1)
    print("OK docx_vs_txt"); sys.exit(0)
sys.stdout.write(text)
