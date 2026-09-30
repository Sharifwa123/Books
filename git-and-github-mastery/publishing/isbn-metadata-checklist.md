# ISBN Metadata Checklist

**No ISBN has been assigned. None is stated anywhere in the book, and none may be invented or guessed.** This file keeps three things apart.

## 1. ISBN to be obtained (not started: needs the author)

| Question | State |
|---|---|
| Which party is the registrant (the publisher the ISBN is issued to)? | **Open.** It must be a person or entity that can be identified to the ISBN agency. SHARIF TECHNOLOGIES's legal identity is not established (`publisher-imprint-profile.md`). |
| Which ISBN agency serves the registrant's country or territory? | **Not researched** (agency sites are outside the reachable hosts). The author must identify it. |
| One ISBN per format? | Each separately sold format (print edition, EPUB, PDF, any other) normally needs its own ISBN; free downloads may not. **Confirm with the agency**; this project states no rule. |
| Who pays, and the lead time | Not known. |
| Barcode | Produced by the printer or the agency's tooling only after an ISBN exists. |

## 2. ISBN application metadata (ready; fill nothing that is unknown)

| Field | Value | State |
|---|---|---|
| Title | Git & GitHub: From Zero to Mastery | Ready |
| Subtitle | A Complete Beginner-to-Expert Guide to Version Control, Collaboration, Automation, Security, and Modern Software Development | Ready |
| Author / contributor role | Sharif Issah Tingane, author. Public records also show the order Sharif Issah Tingane (ORCID: family name Tingane); **the author decides the order used for ISBN and library records** | Ready, order to confirm |
| Other contributors | None to list (no editor, illustrator or translator is recorded; the use of AI assistance is addressed in `final-publication-blockers.md` item 3) | Ready |
| Publisher / imprint | SHARIF TECHNOLOGIES (imprint); legal registrant **to be confirmed** | Open |
| Copyright holder | SHARIF TECHNOLOGIES, as instructed; **legal basis to be confirmed** | Open |
| Edition | 1st edition | Ready |
| Language | English (`en`) | Ready |
| Format(s) | PDF (screen, A4), PDF (print, 170 mm x 240 mm draft), EPUB (reflowable), editable Markdown source; each needs a decision whether it is sold or given away | Open |
| Publication date | Not set | Open |
| Country / territory of publication | Not stated here. The author's public profile names Ghana; the registrant's country is the registrant's to state | Open |
| Territorial rights | Not decided (worldwide is typical for a free download; decide) | Open |
| Subject / category | Computing: software development, version control, Git, GitHub. BISAC: COM051230 (Software Development and Engineering: General) is a candidate; **codes not verified here**. Thema: UMZ (software engineering) is a candidate; **not verified** | Candidate |
| Keywords | git, github, version control, beginners, open source, continuous integration, github actions, security, collaboration | Ready |
| Audience | Complete beginners to advanced readers | Ready |
| Description (short) | See `publication-metadata-checklist.md` | Ready |
| Page count | Not fixed: depends on trim size and typesetting. The print draft's count changes with each build | Open |
| Price | Not decided | Open |
| Licence statement | CC BY-NC-SA 4.0 (text), MIT (code), as instructed | Ready, pending the rights review |
| Series | None | Ready |

## 3. ISBN actually assigned

| Format | ISBN | Assigned on | Assigned by |
|---|---|---|---|
| (none yet) | — | — | — |

Only this table may receive an ISBN, and only after an agency has issued it. Then update: the copyright page, the package metadata, the EPUB identifier, the cover, the retailer records.

## 4. The full manuscript for the ISBN application (prepared 30 September 2026)

The agency asks for the complete manuscript. The package is built by `tools/build_package.sh` into `publishing/build/package/` (a build folder, not committed). A copy of the finished files is committed in `publishing/release/` so that they can be downloaded from GitHub:

| File | Use |
|---|---|
| `ebook/git-and-github-from-zero-to-mastery-screen.pdf` | The complete book as one PDF (tagged, PDF/UA-1 checked), the usual file to send with an application |
| `ebook/git-and-github-from-zero-to-mastery.docx` | The complete book as a Word file (headings, tables, code, diagrams; validated against the Word XML schema, **not opened in Word or LibreOffice**, which are unavailable here) |
| `ebook/git-and-github-from-zero-to-mastery.epub` | The reflowable ebook (EPUBCheck: no messages) |
| `manuscript/book.md` and `MANIFEST.txt` | The complete text as one Markdown file, with a SHA-256 per source file |
| `cover/cover-front.png` and `.svg` | The front cover (1600 x 2560) |
| `metadata/publication-metadata.json` | Title, author, imprint, copyright, licences, AI-assistance statement; ISBN left empty |
| `SHA256SUMS` | Checksums of every file in the package |

The book is an electronic book only: there is no print edition, trim size or back cover. The author submits the files; the project cannot contact the agency. When an ISBN is issued, record it in section 3 and update the copyright page, the package metadata, the EPUB identifier and the retailer records.
