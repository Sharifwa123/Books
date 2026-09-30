# Part VIII review (Chapters 62-63), 2026-09-30

Both chapters are `status: draft` and Core.

## 1. Technical review
Chapter 62 covers the dependency graph, Dependabot (alerts, security updates, version updates), secret scanning, push protection, code scanning and CodeQL (concept), advisories, `SECURITY.md`, private vulnerability reporting and security overview. Chapter 63 covers least privilege for credentials, secret levels, signed commits on GitHub, checksums and attestations, the supply chain, and the difference between Git's and GitHub's security. Workflow security (pinning, injection, token permissions) was in Chapter 60.

## 2. Beginner comprehension review
Each feature is described in one paragraph and in the documentation's words; availability by plan is deliberately not summarised because it changes.

## 3. Command verification
Two local recordings (Bash and zsh): a `dependabot.yml` example from the documentation parsed with PyYAML and a `SECURITY.md` tracked in Git (Chapter 62); a SHA-256 checksum made, verified, then failing after a change (Chapter 63, Linux `sha256sum` only; macOS needs `shasum -a 256`, stated in the text).

## 4. Cross-references
`resolve_refs.py --check`, `check_links.py`, `check_refs`: no problems.

## 5. Research / source review
Ledger rows R307-R313 checked against `github/docs` at commit `2eaab0b` (29 September 2026); all keep `needs_reverification=yes`. **Not established:** which features are available for which plan and repository visibility; the settings screens; the exact behaviour of each feature on a live account.

## 6. Security review
No secrets, no invented incidents. The `SECURITY.md` example uses a non-existent address and says so. The text states that scanning finds known patterns only, that a signature shows a key and not a good change, and that a checksum beside the file proves little.

## 7. Editorial review
British spelling; no banned phrases; consistent callouts.

## Open items
1. Live-account pass for every feature (gate D).
2. Plan availability and current defaults.
3. SSH-signing on GitHub, vigilant mode: not run.
