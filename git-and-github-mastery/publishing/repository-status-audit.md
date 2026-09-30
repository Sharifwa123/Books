# Repository Status Audit

Audited 30 September 2026 through the GitHub connection and the local clone. Repository: `Sharifwa123/Books` (public). The authoritative branch is `main`; nothing is read from any other branch as a source of truth.

## State found

| Item | Finding |
|---|---|
| Default branch | `main`, at the merge commit of pull request 22 (`5cfb166`) when the audit began |
| Other branches | `ccr-761e9a6b-sigmi1` (the session's working branch, reset to `main` after each merge); no other branch |
| Pull requests | 22 in total, **all merged** (PR 1, the planning and architecture work, to PR 22, the editorial read-through); **none open** |
| Commits | 164 on `main` between 29 and 30 September 2026 |
| CI | `.github/workflows/validate.yml`, five jobs: structure and references; Git command tests; chapter transcripts in Bash and zsh; chapter transcripts on Git 2.56.0 built from source; PDF/EPUB edition build with veraPDF and EPUBCheck. All five passed on the last merged head |
| Manuscript | 81 chapters in 13 parts; appendices A to N; exercises (81 chapters' worth) and solutions; glossary; index; front matter; back matter |
| Research | Ledger of 356 rows; sources manifest with hashes; Git manual checks (67); CommonMark conformance (655 examples) |
| Publication files | PDF and EPUB builders, clean export, package builder, draft cover, plans for formats, PDF build and metadata |
| Generated artefacts | `publishing/build/` is produced by the builders; it is an output folder, not source |
| Licence files | None before this audit. Added: `LICENSE.md`, `LICENSE-TEXT.md`, `LICENSE-CODE` (see `rights-and-licensing.md`) |
| Stale status text found | Root `README.md` ("Research and architecture phase ... drafting not started"); the book `README.md` (version 0.3.0, "no chapters drafted", "Part I in progress", "docs.github.com not reachable", licences "unverified"); `publishing/metadata.md` (same); `research/README.md` (109-row report); the copyright page and author page ("undecided", placeholders for the biography); Chapter 65 ("decision has not been made"); Appendix N ("contains no licence statement"); the PDF check that required the word "undecided"; the planning documents (historical) |
| Unresolved markers in the book text | Seven intentional placeholders remain in the clean export before this audit; after it: the ISBN, publication date, date of final technical verification and publisher e-mail. No TODO, FIXME or drafting marker is present in the manuscript (the word TODO appears in Chapter 32 only as a hook example) |
| References to `research/…` in the book text | Six; audited in `research-file-references-audit.md` |

## Changes made in this audit

- Root and book READMEs, `publishing/metadata.md` and `research/README.md` now describe the real state. `planning/README.md` marks the planning folder as historical.
- Copyright page, author page, preface rule 7, Chapter 3 download location, Chapter 65 and Appendix N updated; the PDF check now looks for the licence statement instead of the word "undecided".
- EPUB metadata carries the imprint and rights statement; the package metadata carries the imprint, copyright, licences and the short biography.
- Author, publisher, rights, ISBN and publication documents added to `publishing/` (list in `final-publication-blockers.md`).

## Not changed

- Planning documents and the review notes under `planning/reviews/` keep their original wording (history).
- No ISBN, legal publisher, address or credential was added.
