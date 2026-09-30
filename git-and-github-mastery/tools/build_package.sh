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
cp publishing/metadata.md "$out/metadata/publication-metadata.md"
(cd "$out" && find . -type f ! -name SHA256SUMS | sort | xargs sha256sum > SHA256SUMS)
echo "package written to $out"; cat "$out/SHA256SUMS"
