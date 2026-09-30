# Part V review (Chapters 36-41), 2026-09-30

Chapters 36-40 were drafted earlier and re-verified this session against GitHub's own documentation; Chapter 41 (Notifications, Stars and Watching) was drafted this session. All six are `status: draft`.

## 1. Technical review
- **Sources.** Statements about GitHub are checked against the open source of GitHub's documentation (`github/docs`, commit `2eaab0b`, 29 September 2026) and, for legal terms, `site-policy` (commit `b9578b5`); both are in `research/sources-manifest.csv`. No live account was used.
- **Git behind the platform, recorded:** remote URLs and `set-url` (36, 38), SSH key generation and SSH signing (38), publishing to an empty remote and the unrelated-histories refusal (39), the Git equivalents of a repository page (40). Chapter 41 is platform-only and has no recorded commands.
- **Conflicts found.** None between the sources and the recordings. Username character rules and the optional `.git` suffix were not found in the sources and are not relied on (R226, R228).

## 2. Beginner comprehension review
Each chapter states how it was checked and that interface layouts were not seen on a live account. Chapter 38 is the longest and should be pilot-read.

## 3. Command verification
All Part V transcripts pass in Bash and zsh locally and in CI on the runner's Git and on Git v2.56.0.

## 4. Cross-references
`resolve_refs.py --check`, `check_links.py` and `check_refs`: no problems.

## 5. Research / source review
Rows R224-R246 cover Part V. GitHub rows are `Officially verified (docs only)` or `Both`, with `needs_reverification = yes`. **Open, each independent:** plan and price availability; username character rules (R228); optional `.git` suffix (R226); wording of buttons on a live account.

## 6. Security review
All credentials and addresses in recordings are made up. Chapter 38 states the platform's guidance on tokens, SSH keys and two-factor sign-in from the documentation. `check_secrets.py` finds nothing.

## 7. Editorial review
British spelling; no banned filler phrases; quotations from GitHub's documentation are short and attributed.

## Open items
1. Re-verify every GitHub row before release.
2. A live-account pass for interface layouts (gate D).
3. Pilot read of Chapter 38.
