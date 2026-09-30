# Part VII review (Chapters 52-61), 2026-09-30

All ten chapters are `status: draft`. Chapters 55, 58, 59 and 61 are [Deep]; 52-54, 56, 57 and 60 are Core.

## 1. Technical review
- CI/CD concepts (52), YAML (53), workflow anatomy (54), expressions (55), practical workflows (56), debugging (57), reusable workflows/environments/Pages artifact (58), runners and limits (59), workflow security (60), external CI (61).
- Locally reproducible parts were recorded in Bash and zsh: a local pipeline script, PyYAML 6.0.1 parsing (including `no` becoming False and the key `on` becoming True), workflow-file structure, expression-context text handling, cron and matrix arithmetic, a skip-trace, artifact packaging, the matrix limit, and a script-injection reproduction with its environment-variable defence.
- GitHub-side behaviour (running workflows, checks, environments, OIDC) was **not run** on a live account and is marked so in every chapter's checking table.

## 2. Beginner comprehension review
Each chapter follows the pattern of earlier Parts. Chapter 55 and 58-59 are dense; [Deep] tags and "first read: later" let a beginner skip them.

## 3. Command verification
Recordings are re-run in CI on the runner's Git and on Git v2.56.0. Chapters 54-61 add no Git commands beyond `git check-ref-format`.

## 4. Cross-references
`resolve_refs.py --check`, `check_links.py`, `check_refs`: no problems.

## 5. Research / source review
Ledger rows R279-R306. GitHub rows were checked against the `github/docs` repository at commit `2eaab0b` (29 September 2026) and remain `needs_reverification=yes`. No product claims are made about other CI systems.

## 6. Security review
Chapter 60 states least privilege, pinning, injection and untrusted-pull-request rules from GitHub's documentation. This book's workflow now pins its actions to full commit SHAs and has read-only contents permission. All recorded secrets are made up; `check_secrets.py` finds nothing.

## 7. Editorial review
British spelling; no banned phrases; consistent callouts. Project 10 is in Chapter 58.

## Open items
1. Live-account pass for workflow behaviour, environments and OIDC (gate D).
2. The 32 verification markers in Parts I-II and others remain individual dependencies.
3. Pilot read of Chapters 55, 58 and 59.
