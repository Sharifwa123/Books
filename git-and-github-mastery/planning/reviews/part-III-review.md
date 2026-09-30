# Part III review (Chapters 13-24), 2026-09-30

All twelve chapters are `status: draft`. Chapters 13-24 were drafted from recorded Bash and zsh sessions (`verification/ch13-*` to `ch24-*`); every `$ ` line in the manuscript is checked against those recordings by `tools/check_transcripts.py`, and the recordings are re-run in CI on the runner's Git (2.55.0).

## 1. Technical review
- All command output in the chapters is real: recorded on Git 2.43.0 with deterministic dates, so commit hashes are reproducible, and re-run on Git 2.55.0 in CI.
- Version differences found by CI and handled with `.alt` recordings rather than hidden: advice text for `git branch -d` on an unmerged branch (Ch 20, 21), invalid branch names (Ch 20) and the initial-branch hint (Ch 16). No behavioural difference was found.
- Ch 22 states that an unrelated uncommitted edit survives `git merge --abort`; this was tested. The documented caveat about overlapping edits is marked as not checked against the official page.
- The merge strategy name printed (`ort`) is recorded on both versions tested; older versions were not tested.
- **Not tested:** Windows, macOS, PowerShell, Command Prompt. Chapter 13's installation steps for those platforms remain *Verification pending*.

## 2. Beginner comprehension review
- Every chapter follows the same order: motivation, one small demonstration, the recorded output read line by line, a caution, a summary.
- `tools/check_term_order.py`: the remaining warnings are (a) the front-matter key `tag:` (a false positive) and (b) forward pointers that carry an explicit chapter reference. One real gap was found and fixed: Ch 21's checklist mentioned stashing without a pointer to Chapter 24.
- Chapters 13-15 are dense. A pilot read by a real beginner is still needed.

## 3. Command verification
`verification/run_all.sh` (all 96+ transcripts, bash and zsh): no failures locally. CI: three jobs green on the merged head. Recorded but *not shown in prose*: nothing is left unrecorded (`unrecorded lines: 0`).

## 4. Cross-references
`resolve_refs.py --check`, `check_links.py`, `check_refs`: no problems. Forward references to Chapters 27, 28, 31-32 and 40-41 use `Chapter [[key]]` and follow the outline order.

## 5. Research / source review
Ledger rows R142-R183 cover Part III. All are *Locally tested* (Git documentation not consulted, because official hosts are unreachable). Nothing in Part III depends on GitHub behaviour; the hosting platform first appears in Chapter 35.

## 6. Security review
- Ch 14 warns about credentials in remote URLs and config; Ch 18 shows a committed (fake) secret surviving deletion and defers the removal procedure to the security chapter.
- Ch 23 warns against `--force` to get past a rejected push; Ch 24 marks `git clean -f` as irreversible and teaches `-n` first.
- `check_secrets.py`: no findings.

## 7. Editorial review
British spelling; no banned filler phrases; consistent callouts. Chapter length is uneven (Ch 16 and 20 are long). Projects 1-6 are embedded in Chapters 16-24.

## Open items
1. Determine the current upstream Git release, re-run every test on it, and update the baseline.
2. Verify Part III's Git-documentation claims when official hosts are reachable.
3. Windows and macOS runs (Chapter 13 installation; Appendix M).
4. Pilot read by a beginner.
5. `EX-revert-empty-commit` stays blocked; Chapter 25 (Undoing) must not use it.
