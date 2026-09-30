#!/usr/bin/env bash
# Assembles the publication package under publishing/build/package/ from the manuscript:
#   manuscript/ (clean text export + manifest)   ebook/ (EPUB, PDFs)   cover/   metadata/
# It builds the electronic-book formats from the same manuscript (the book is an ebook only; no print edition).
# It does NOT upload or publish anything and does not invent any identifier: the ISBN stays empty until one is assigned.
# Needs the diagrams pre-rendered (tools/render_diagrams.py) and the packages named in .github/workflows/validate.yml.
set -eu
cd "$(dirname "$0")/.."
export SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-1790000000}"
out=publishing/build/package
rm -rf "$out"; mkdir -p "$out/manuscript" "$out/ebook" "$out/cover" "$out/metadata"
python3 tools/export_clean.py --out "$out/manuscript"
python3 tools/build_epub.py --out "$out/ebook/git-and-github-from-zero-to-mastery.epub"
python3 tools/build_pdf.py --profile screen --out "$out/ebook/git-and-github-from-zero-to-mastery-screen.pdf"
cp publishing/cover/cover-front.svg publishing/cover/cover-front.png "$out/cover/"
rm -f "$out"/ebook/*.html   # intermediate files written by the PDF builder
python3 - "$out" <<'PY'
import json, sys, hashlib, os, glob
out = sys.argv[1]
meta = {
  "title": "Git & GitHub: From Zero to Mastery",
  "subtitle": "A Complete Beginner-to-Expert Guide to Version Control, Collaboration, Automation, Security, and Modern Software Development",
  "author": "Sharif Issah Tingane",
  "language": "en-GB",
  "edition": "1st Edition",
  "brand": "SHARIF TECHNOLOGIES",
  "slogan": "Knowledge Is Power",
  "keywords": ["Git", "GitHub", "version control", "GitHub Actions", "open source"],
  "imprint": "SHARIF TECHNOLOGIES",
  "copyright": "Copyright (c) 2026 SHARIF TECHNOLOGIES",
  "copyright_holder_note": "As instructed by the author; the legal basis for the holder is to be confirmed.",
  "licences": {"text": "CC BY-NC-SA 4.0 (https://creativecommons.org/licenses/by-nc-sa/4.0/)", "code_samples": "MIT"},
  "website": "www.shariftechnologies.online",
  "ai_assistance": "Written with the help of an AI assistant, Claude (Anthropic, via Claude Code), under the author's direction; see AI-ASSISTANCE.md. Claude is credited as contributor and co-author.",
  "author_biography_short": 'Sharif Issah Tingane builds software from Wenchi, Ghana, and founded SHARIF TECHNOLOGIES. Public projects include SAIBA, an AI business assistant; Sharif NOVA, an open-source programming language; and CodeCast, an Android app. A public ORCID record lists interests in software development, AI, cybersecurity and networking. This book, for first-time learners, was written with the help of an AI assistant, Claude.',
  "isbn": None, "legal_publisher": None, "publisher_address": None, "publication_date": None,
  "status_of_null_fields": "Not assigned, not established or not yet supplied. They are deliberately empty and must not be invented.",
  "files": {os.path.relpath(f, out): hashlib.sha256(open(f, "rb").read()).hexdigest() for f in sorted(glob.glob(out + "/ebook/*") + glob.glob(out + "/cover/*"))},
}
json.dump(meta, open(out + "/metadata/publication-metadata.json", "w"), indent=2, ensure_ascii=False)
PY
(cd "$out" && find . -type f ! -name SHA256SUMS | sort | xargs sha256sum > SHA256SUMS)
echo "package written to $out"; cat "$out/SHA256SUMS"
