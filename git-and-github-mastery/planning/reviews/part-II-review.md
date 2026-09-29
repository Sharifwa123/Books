# Part II review (Chapters 9-12), 2026-09-29

All four chapters are `status: draft`.

## 1. Technical review
- Chapter 9's evidence (five differing "menu" files, `diff` reports, the silent-overwrite collision) is recorded from interactive Bash and zsh runs and re-run in CI; the chapter quotes the recordings through the transcript check. The claim that "no error appeared" is shown by the recording, not asserted.
- Chapters 10-12 contain no command output. Their factual statements are about history, design and products, and are the least verified part of the book so far: **every** named product, history claim and cause is marked *Verification pending* and lives in ledger rows R136-R141 (five of them *Needs re-verification* or *Time-sensitive (unverified)*, one *Locally tested*). Chapter 10 deliberately states no exact dates and no quotations.
- One defect caught by the automated checks: the outline title "Centralized" conflicted with the book's British spelling; fixed at the source (`toc_data.py`).

## 2. Beginner comprehension review
`tools/check_term_order.py` shows only forward pointers that carry an explicit chapter reference (for example "GitHub, introduced in Chapter 12"). The word *Git* is used before Chapter 12 (the book's title, Chapter 1's "Where Git fits", Chapter 9's examples); it is defined informally in Chapter 1 and formally in Chapter 12, and is therefore allowlisted. Chapter 11 introduces *repository* informally and points to Chapter 15 for the exact meaning.

## 3. Command verification
Recordings pass in Bash 5.2 and zsh 5.9, locally and on the GitHub runner. `diff` is a system tool, not a shell builtin; availability in Git Bash on Windows is **not verified** (the chapter tells the learner to note it if absent).

## 4. Cross-references
`tools/resolve_refs.py --check`, `check_links.py`: no problems. Chapter 9's prerequisites were corrected in the outline (it uses the terminal).

## 5. Research / source review
Open rows: R134 (generic backup/sync statements), R136-R141. None can be verified until official sources are reachable.

## 6. Security review
No secrets; the chapters warn about silent data loss and about not treating synchronisation or backups as version control. The independence/non-affiliation notice appears in Chapter 12.

## 7. Editorial review
British spelling throughout; no banned filler phrases; Chapter 10 is marked optional on the first read. A pilot read is still needed for tone.

## Open items
1. Verify R134, R136-R141 against primary sources.
2. Check `diff` availability in Git Bash.
3. Pilot read.
