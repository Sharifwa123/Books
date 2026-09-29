# Part I review (Chapters 1-8), 2026-09-29

Status of all eight chapters: **draft** (status stays `draft` until the release gate passes). Manuscript size: about 25,443 words plus exercises and solutions.

## 1. Technical review
- Every command, byte value, error message and rendered result quoted in Chapters 2, 4, 5, 7 and 8 comes from a recorded run (`verification/`), checked by `tools/check_transcripts.py` and `tools/check_md_examples.py`.
- **Defect found and fixed during review:** Chapter 7 claimed that `rmdir` refuses non-empty folders without a recording. A recording was added (`session-errors.txt`), and the chapter now quotes it.
- **Defect found and fixed:** hard-coded chapter numbers (some wrong, e.g. `.gitignore` is Chapter 18, not 17) were replaced by checked references (`tools/resolve_refs.py`).
- **Defect found and fixed earlier:** my first Chapter 8 draft would have taught that a list needs a blank line before it. A real CommonMark renderer accepted the list without one, so the chapter now recommends the blank line as a portable habit and states what was actually observed.
- Untested product statements are marked *Verification pending* in the text and `Needs re-verification` in the ledger (see section 5).

## 2. Beginner comprehension review
`tools/check_term_order.py` lists every glossary term used before the chapter that defines it. 28 warnings at first; the ordinary-word cases were glossed in place (browser, terminal, encoding, plain text, Git Bash). The 13 that remain are deliberate forward pointers that carry an explicit chapter reference (for example "Chapter 7 introduces the terminal"). No chapter relies on an undefined term for its own explanations.
Open item for a human pilot: a real absolute beginner should read Chapters 1-3 and report where they stopped understanding. This review cannot substitute for that.

## 3. Command verification
Interactive Bash 5.2 and zsh 5.9 transcripts (10 sessions) plus docx, URL, local-server, mojibake, Git line-ending, Markdown and starter-file checks all pass locally and in CI on the GitHub runner (which has newer coreutils and Git 2.55.0). Windows PowerShell, Command Prompt and Git Bash are **not** executed anywhere (no Windows environment).

## 4. Internal cross-reference review
`tools/resolve_refs.py --check`: no stale or unannotated chapter numbers. `tools/check_links.py`: no broken relative links. Glossary: 85 terms; every term in a chapter's *New Vocabulary* exists with the right first chapter.

## 5. Research / source review
Ledger ids cited by Part I chapters, by evidence class:

| Evidence class | Rows | Ids |
|---|---|---|
| Not applicable | 1 | R110 |
| Needs re-verification | 12 | R111, R113, R114, R115, R122, R123, R124, R126, R127, R128, R129, R132 |
| Locally tested | 11 | R112, R116, R117, R118, R119, R120, R121, R125, R130, R131, R133 |

Release gate (`check_manuscript.py --release`) will fail until every "Needs re-verification" row above is officially verified. Blocked by network policy: Microsoft, Apple, GNU manuals, Unicode, IETF standards, CommonMark and GitHub documentation.

## 6. Security review
No secrets in the repository (`tools/check_secrets.py`). Chapters 1, 6 and 7 teach safe installation, phishing recognition, private-key handling and "do not paste commands you do not understand". Every destructive command is preceded by a caution; deletion is demonstrated only in a sandbox folder. Exercises use no real credentials.

## 7. Editorial review
British spelling is used consistently in prose (checked by grep); banned filler phrases are blocked by the checker; each chapter follows the template and has exercises at five levels with separate solutions. Suggested for a later pass: shorter sentences in Chapters 5 and 6, and a pilot read for tone.

## Open items carried forward
1. Verify the 12 unverified Part I ledger rows when official sources are reachable.
2. Run the Windows shell equivalents (Chapter 7, section 7.11) on a real Windows machine and complete Appendix M.
3. Insert the real download location for the companion files (placeholder in Chapter 3).
4. Beginner pilot read.
