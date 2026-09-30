# 06 — Publishing and Front-Matter Plan

> **Update:** decisions now recorded in `../publishing/metadata.md` (title, subtitle, intended licences: book text CC BY-NC-SA 4.0, code MIT — both wording UNVERIFIED and not yet inserted). The 'How to use this book' front-matter must explain the Core/Deep tags and First-Read Path (`12-first-read-path-and-tags.md`) and the Git Bash convention, and the Preface carries the methodology (`../publishing/author-methodology.md`).

**Rule:** no invented legal identifiers. Anything not supplied stays a bracketed placeholder.

## Metadata (supplied)
- Author: Sharif Issah Tingane
- Publisher / rights holder / brand: SHARIF TECHNOLOGIES
- Slogan: *Knowledge Is Power*

## Placeholders (not supplied — do not fill by guessing)
[ISBN TO BE ASSIGNED] · [PUBLICATION DATE] · [YEAR] · [EDITION] · [SHARIF TECHNOLOGIES REGISTERED ADDRESS] · [OFFICIAL PUBLISHER ADDRESS] · [OFFICIAL WEBSITE] · [OFFICIAL PUBLISHING EMAIL] · [CONTACT INFORMATION] · [MONTH YEAR of technical verification] · [MANUSCRIPT VERSION] · [LICENCE CHOICE] · [AUTHOR BIOGRAPHY — publisher to supply verified facts]

## Front-matter templates (to be written into `manuscript/front-matter/`)
1. **Half title / Title page** – title, subtitle, "Written by Sharif Issah Tingane", "Published by SHARIF TECHNOLOGIES", *Knowledge Is Power*.
2. **Copyright page** – "Copyright © [YEAR] SHARIF TECHNOLOGIES. All rights reserved." (unless the publisher selects another licence); author/publisher lines; edition; ISBN placeholder; date placeholder; statement that third-party names/marks belong to their owners; statement that the text is original and that quoted third-party material (licence texts etc.) remains under its own terms.
3. **Copyright explainer (short)** – copyright generally arises automatically when an original work is created; registration or deposit systems exist in some jurisdictions and may add benefits; consult local rules. Public availability ≠ copyright-free.
4. **Edition/version statement** – 1st Edition; Technical information verified: [MONTH YEAR]; Manuscript version: [VERSION]; note that Git/GitHub change and pointing to official docs.
5. **Disclaimer** – educational; commands change system state; understand before running; security operations need care; no guarantee of identical behaviour across OS/versions/configs/future releases; licensing text is educational, not legal advice; GitHub policies/features change.
6. **Trademark and non-affiliation notice** – Git, GitHub, Microsoft, Linux, Windows, macOS, Docker, GitLab, Bitbucket and other names may be trademarks of their owners; no endorsement, sponsorship or affiliation implied.
7. **Licensing statement** – slot filled once the publisher decides (see 07). Default until then: all rights reserved.
8. **Dedication, Foreword (placeholder), Preface, How to use, Who it's for, Roadmap, Prerequisites, Equipment/software list, TOC.**
9. **Author section** – placeholder only; no qualifications, employment, awards or memberships unless supplied.
10. **Publisher section** – SHARIF TECHNOLOGIES, slogan, placeholders for address, website, email, contact, edition, date, ISBN.

## Format targets
Single Markdown source → Pandoc (or equivalent) → PDF (print + screen), EPUB, HTML. Diagrams as Mermaid/SVG with text alternatives. Decision pending on the toolchain.

## Index plan
Index terms generated from glossary CSV plus command names and GitHub feature names; hand-curated page-reference index for print/PDF; searchable in EPUB/web.
