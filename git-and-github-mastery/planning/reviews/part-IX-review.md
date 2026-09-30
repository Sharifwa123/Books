# Part IX review (Chapters 64-67), 2026-09-30

All four chapters are `status: draft`. Chapters 64-66 are Core; Chapter 67 (with Project 11) is Deep.

## 1. Technical review
- **64 How Open Source Works:** public vs source-available vs open source; roles; the contribution flow; `CONTRIBUTING.md`, code of conduct, community profile; `good first issue`; sign-off (`git commit -s`, `Signed-off-by`, trailers format) recorded.
- **65 Copyright and Licences:** copyright vs licence; GitHub's default-copyright statement; the seven distinctions; MIT, BSD-2/3, Apache-2.0, MPL-2.0, LGPL-3.0, GPL-3.0 by permissions, conditions and limitations; SPDX identifiers (including the deprecated `GPL-3.0`); Creative Commons elements. **No licence text for this book is inserted** (gate A); the chapter says the book's licence is undecided and that it is not legal advice.
- **66 Releases:** releases vs tags; Semantic Versioning 2.0.0; generated release notes and `.github/release.yml`; source archives; immutable releases; automation cautions. Recorded: tag sorting, notes from history, `git describe`, `git archive`, release-notes file structure.
- **67 Creating an Open-Source Project (Project 11):** a tiny library with tests, `.gitignore`, community files, a check script and an annotated `v0.1.0` tag. Recorded; the licence is left to the learner.

## 2. Beginner comprehension review
The chapters keep short paragraphs and small recordings. Chapter 65 is dense with names; the seven-question list and the table are the anchor. A pilot read is needed.

## 3. Command verification
Four new recordings (`ch64-oss`, `ch66-releases`, `ch67-ossproject`) in Bash and zsh, re-run in CI on the runner's Git and on Git v2.56.0. Chapter 65 has no recording. One near-miss caught during recording: Python's `__pycache__` folders were committed until a `.gitignore` line was added; the chapter uses this as a lesson.

## 4. Cross-references
`resolve_refs.py --check`, `check_links.py`, `check_refs`: no problems.

## 5. Research / source review
Ledger rows R314-R324. GitHub statements were checked against `github/docs` at commit `2eaab0b`. The licence summaries (R318) come from choosealicense.com data, a **secondary** source; the official pages (gnu.org, apache.org, mozilla.org, opensource.org, creativecommons.org) could not be read, so R093 stays open. SPDX identifiers were checked against the SPDX licence list 3.29.0; the Creative Commons definitions against the SPDX copy of the legal code. Semantic Versioning was read from its specification. **Unconfirmed:** Creative Commons' own advice about software (R099, secondary source only).

## 6. Security review
The sign-off is explained as text, not a signature. `SECURITY.md` examples use a non-existent address. The chapters tell learners not to copy licence text from memory. No secrets in recordings.

## 7. Editorial review
British spelling; no banned filler phrases; consistent callouts; the "not legal advice" notice is at the top of Chapter 65.

## Open items
1. Gate A: the licence of this book and its code samples; nothing is to be inserted until a person decides.
2. Verify licence summaries against official texts when the hosts are reachable (R093).
3. Live-account pass for community-profile, release and sign-off-policy features (gate D).
4. Pilot read of Chapters 65 and 67.
