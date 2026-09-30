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

## Live state check (30 September 2026, 17:45 UTC)

Evidence taken from `git ls-remote`, the local clone and the GitHub connection, not from README text or cached pages.

| Question | Finding | Evidence |
|---|---|---|
| Default branch on GitHub | **`ccr-761e9a6b-sigmi1`**, not `main` | repository record (`default_branch`); `git ls-remote --symref origin HEAD` |
| Why the public page shows that branch | It is the default branch: it was the first branch pushed, and it was never switched. All pull requests targeted `main`, so `main` is where the merged work is | PR base branches; branch list |
| `main` | `5cfb166`, the merge commit of pull request 22 | `git ls-remote` |
| Pull request 22 | Merged. Source `ccr-761e9a6b-sigmi1` at `9c4789b`, target `main`, merge commit `5cfb166`, merged 2026-09-30 17:04:48 UTC, 59 files changed, 10 commits | PR record; `git show 5cfb166` |
| Is PR 22 on `main`? | Yes. `9c4789b` is an ancestor of `main`, and the tree of `main` is identical to the tree of `9c4789b` | `git merge-base --is-ancestor`; `git diff` (no output) |
| Local clone against GitHub | In step: local branch, its remote-tracking branch and the remote are the same commit | `git status`, `git rev-parse` |
| Why the default branch showed "164 commits", "0 open pull requests" and the old README status | At that moment the default branch held the same 164 commits as `main`, and **no pull request was open** (pull request 23 was opened afterwards). The README status was **genuinely stale on every branch**: no earlier pull request had updated it | `git log`; PR list; README history |
| Open pull requests now | 1: pull request 23 (this audit and the author/publisher material), branch `ccr-761e9a6b-sigmi1` into `main` | PR list |
| Workflows | One: "Validate book" (`.github/workflows/validate.yml`), state **active**. Triggers: pushes to `main`, every pull request, and manual start. It references no obsolete branch. The last run on `main` (push of the PR 22 merge, run 124) **succeeded**; the pull-request run for PR 23 was in progress. Runs on pushes to the default branch `ccr-761e9a6b-sigmi1` do not start (not in the trigger list): its changes are validated through pull requests | `actions_list` |
| Required checks executing? | Yes, all five jobs run on each pull request. No branch protection or required-check setting was examined (not visible through the available tools) | run records |

**Explanation, in the audit's words:** not a stale cache and not a merge into another branch. Two separate causes: (1) the README status text was out of date in the repository itself, and is corrected in pull request 23; (2) the default branch of the repository is the work branch, while the authoritative branch is `main`.

## Default branch: the one action that needs the owner

| | |
|---|---|
| Current default branch | `ccr-761e9a6b-sigmi1` |
| Intended default branch | `main` |
| Action required | Repository **Settings > Branches > Default branch**: switch to `main` and confirm. The available tooling can read the repository record but has no operation that changes repository settings, and the session's credentials were not used for a direct settings call |
| Interim measure | After each merge the work branch is fast-forwarded to `main` (no history is rewritten, nothing is deleted), so the public page of the default branch shows the same content as `main` |

## What exists now (counted from the files, not from status text)

| Item | Count |
|---|---|
| Chapters drafted / planned | 81 / 81, in 13 parts |
| Appendices | 14 (A to N) |
| Exercise files / solution files | 81 / 81 (one exercise, `EX-revert-empty-commit`, is blocked by design and not published) |
| Glossary terms | 287 |
| Manuscript size | about 196,000 words in the chapters; about 272,000 words in the clean export (with exercises, solutions, glossary and appendices) |
| Recorded-session folders in `verification/` | 72 |
| Research ledger rows | 356 (79 marked unverified, 55 of them superseded planning rows); 25 verification-pending markers in chapters |
| Architecture | Complete (`planning/11-toc-v2-renumbered.md`, machine-checked); kept as history |
| Editorial read-through | Complete (all 81 chapters and the hand-written appendices) |
| Automated validation | Static checks, 67 Git-manual checks, 655 CommonMark examples, recorded-session re-runs on two Git versions, PDF/UA-1 and PDF/A-2b validation, EPUBCheck: all in CI |
| Publication material | PDF (screen and print profiles), EPUB, clean export, package builder, draft front cover, author/publisher/licensing documents (this folder) |
| Outstanding blockers | `final-publication-blockers.md` |

The book is **not** described as published or finished for release: it is a complete draft with a finished read-through, in publication preparation.

## Changes made in this audit

- Root and book READMEs, `publishing/metadata.md` and `research/README.md` now describe the real state. `planning/README.md` marks the planning folder as historical.
- Copyright page, author page, preface rule 7, Chapter 3 download location, Chapter 65 and Appendix N updated; the PDF check now looks for the licence statement instead of the word "undecided".
- EPUB metadata carries the imprint and rights statement; the package metadata carries the imprint, copyright, licences and the short biography.
- Author, publisher, rights, ISBN and publication documents added to `publishing/` (list in `final-publication-blockers.md`).

## Not changed

- Planning documents and the review notes under `planning/reviews/` keep their original wording (history).
- No ISBN, legal publisher, address or credential was added.
