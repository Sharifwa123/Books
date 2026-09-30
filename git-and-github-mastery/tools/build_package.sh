#!/usr/bin/env bash
# Assembles the publication package under publishing/build/package/ from the manuscript:
#   manuscript/ (clean text export + manifest)   ebook/ (EPUB, PDFs)   cover/   metadata/
# It builds every format from the same manuscript. It does NOT publish anything (gate B) and does not invent
# any identifier: the ISBN and the legal publisher remain placeholders until they are assigned and decided.
# Needs the diagrams pre-rendered (tools/render_diagrams.py) and the packages named in .github/workflows/validate.yml.
set -eu
cd "$(dirname "$0")/.."
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-1790000000}"
out=publishing/build/package
rm -rf "$out"; mkdir -p "$out/manuscript" "$out/ebook" "$out/cover" "$out/metadata"
python3 tools/export_clean.py --out "$out/manuscript"
python3 tools/build_epub.py --out "$out/ebook/git-and-github-from-zero-to-mastery.epub"
python3 tools/build_pdf.py --profile screen --out "$out/ebook/git-and-github-from-zero-to-mastery-screen.pdf"
python3 tools/build_pdf.py --profile print --out "$out/ebook/git-and-github-from-zero-to-mastery-print.pdf"
python3 tools/build_pdf.py --profile print --variant pdf/a-2b --out "$out/ebook/git-and-github-from-zero-to-mastery-print-pdfa-2b.pdf"
cp publishing/cover/cover-front.svg publishing/cover/cover-front.png "$out/cover/"
rm -f "$out"/ebook/*.html   # intermediate files written by the PDF builder
python3 - "$out" <<'PY'
import json, sys, hashlib, os, glob
out = sys.argv[1]
meta = {
  "title": "Git & GitHub: From Zero to Mastery",
  "subtitle": "A Complete Beginner-to-Expert Guide to Version Control, Collaboration, Automation, Security, and Modern Software Development",
  "author": "Sharif Tingane Issah",
  "language": "en-GB",
  "edition": "1st Edition",
  "brand": "SHARIF TECHNOLOGIES",
  "slogan": "Knowledge Is Power",
  "keywords": ["Git", "GitHub", "version control", "GitHub Actions", "open source"],
  "isbn": None, "legal_publisher_or_imprint": None, "copyright_holder": None, "licence": None,
  "publisher_address": None, "publication_date": None, "author_biography": None,
  "status_of_null_fields": "Not decided or not yet supplied. They are deliberately empty and must not be invented.",
  "files": {os.path.relpath(f, out): hashlib.sha256(open(f, "rb").read()).hexdigest() for f in sorted(glob.glob(out + "/ebook/*") + glob.glob(out + "/cover/*"))},
}
json.dump(meta, open(out + "/metadata/publication-metadata.json", "w"), indent=2, ensure_ascii=False)
PY
(cd "$out" && find . -type f ! -name SHA256SUMS | sort | xargs sha256sum > SHA256SUMS)
echo "package written to $out"; cat "$out/SHA256SUMS"
