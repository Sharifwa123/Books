# Publication Formats Plan (EPUB, PDF, source, cover, metadata)

**Decision of 30 September 2026: the book is an electronic book only.** EPUB and the screen PDF are the release formats; the print PDF profile, back cover, spine and trim size are out of scope unless the author later adds a print edition.

Status (2026-09-30): implemented for the ebook formats; see the table below. Nothing here overrides the master plan; it records the format principles so they are applied when the manuscript reaches the publication stage. The PDF edition is already built (see `pdf-build-plan.md`).

## Principle
CONTENT -> STRUCTURE -> ACCESSIBILITY -> NAVIGATION -> REFLOWABLE PRESENTATION -> VISUAL DESIGN.
The Markdown manuscript (`manuscript/`) is the single authoritative source. No format is derived from another format's layout: EPUB is not made from the PDF, and the PDF is not the source of the ebook.

## Formats
| Output | Kind | Source | Notes |
|---|---|---|---|
| PDF (screen A4, print 170 x 240 mm) | Fixed layout | Manuscript via `tools/build_pdf.py` | Done; selectable text, bookmarks, metadata, links, tagged (PDF/UA-1 variant). Open: external validator, PDF/A. |
| EPUB 3 | Reflowable | Manuscript via a new `tools/build_epub.py` (to write at publication stage) | Semantic XHTML, real headings, navigation document, `epub:type` for parts, chapters, notes and appendices. |
| Kindle-compatible ebook | Uploaded as EPUB | Same EPUB | Amazon's current upload guidance must be re-verified when this stage is reached (evidence class: vendor documentation); no legacy format is created just to have another extension. |
| Editable source | Markdown plus the structured data in `tools/toc_data.py` | The repository | Headings, code, tables, figures, captions and references stay distinct structures. |
| Cover | Separate high-resolution asset | To be designed | Not embedded in the manuscript source. Front cover only until a legal publisher, ISBN and trim sizes exist. |
| Metadata | `publishing/metadata.md` | Human-supplied fields | Feeds PDF, EPUB and store metadata. |

## EPUB requirements (to be machine-checked when built)
- Reflowable text with no fixed page size or absolute positioning; reader-controlled font size and settings; responsive CSS in relative units.
- Code stays selectable text in `pre`/`code` (long lines scroll or wrap by CSS, not images); tables stay real tables with header cells; headings are real `h1`-`h6`; diagrams are images (SVG with PNG fallback where a target requires it) with alternative text and captions, never full-page images.
- Functional navigation document (table of contents), landmarks, internal cross-reference links, glossary and note links, language `en-GB`, accessibility metadata (schema.org accessibility properties, `dc:language`, unique identifier).
- Design identity kept in CSS: typography, chapter openers, callouts, code styling, special sections.
- Checks: EPUBCheck (needs a verified source and version), an accessibility review, and a test in at least a phone-size and an e-reader-size viewer. Any of these that cannot be run is recorded as not run.

## Publication package (conceptual)
```
publication/
  manuscript/   editable and structured source
  ebook/        book.epub, book.pdf
  cover/        high-resolution cover
  metadata/     publication metadata
```
Exact layout and names to follow the master plan when the stage is reached.

## Clean manuscript for copyright registration
A separate export contains only the published book: cover, title page, copyright page, author information, contents, main text, references, about the author and end matter. It must exclude research notes, TODO lists, planning, repository architecture, drafting instructions and AI working notes. A check will list what the export contains and fail if any `planning/`, `research/` or ledger-internal material is present. The registration itself is a human action (gate D).

## Identity and legal
- Author, consistently: Sharif Issah Tingane.
- SHARIF TECHNOLOGIES is the intended brand identity. The legal publisher or imprint is undecided and is not asserted as a legal fact anywhere until the rights holder decides (gates A and B).
- ISBN, address and author biography stay placeholders until officially assigned or supplied. Licence wording stays undecided (gate A).

## Implementation status (2026-09-30)
| Item | Status |
|---|---|
| EPUB 3, reflowable, built from the manuscript (`tools/build_epub.py`) | done; EPUBCheck 5.2.1 reports no errors or warnings (run in CI); includes the cover, a navigation document, landmarks, accessibility metadata and diagrams as SVG with text alternatives |
| Kindle-compatible ebook | not built: the EPUB is the upload format, and Amazon's current requirements were not checked (no access to their documentation) |
| PDF screen and print editions, tagged, PDF/UA-1 | done; validated with veraPDF |
| PDF/A-2b archival edition | done as a separate untagged file; validated with veraPDF |
| Clean export of the book text only (`tools/export_clean.py`) | done; fails on development artefacts; lists placeholders and evidence-file citations |
| Cover | **draft** typographic front cover (`publishing/cover/`); no back cover, spine or print wrap (they need trim size, page count and an ISBN) |
| Publication package (`tools/build_package.sh`) | done as a script; nothing is published |
| Editable source | the Markdown manuscript and `tools/toc_data.py` in the repository |
| ISBN, legal publisher, copyright holder, licence wording, address, author biography | **not decided or not supplied**; placeholders remain (gates A, B, D) |
