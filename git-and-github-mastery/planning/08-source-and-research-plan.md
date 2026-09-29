# 08 — Source and Research Plan

**Status: partly performed — see `../research/README.md`.** (Git checked locally against 2.43.0 and its packaged upstream docs; GitHub and most licence texts unverified because the official hosts are blocked.) No GitHub feature, plan limit, price or UI detail may be written until verified against the official source below, and the verification date recorded.

## Source hierarchy
1. Official Git documentation (git-scm.com docs, reference manual, Pro Git *as a reference to read, never to copy*), Git release notes.
2. Official GitHub Docs (docs.github.com) and GitHub changelog.
3. Official licence texts (opensource.org, gnu.org, apache.org, creativecommons.org), SPDX list.
4. Semantic Versioning specification (semver.org); YAML specification (yaml.org).
5. Official OS/vendor docs for install steps (Windows, macOS, Linux distributions).
6. Only then, reputable secondary sources; never outdated tutorials when an official page exists.

## Verification workflow
For every volatile topic: read official page → note URL + date read → paraphrase (no copying) → tag section "Verified on [date]" → add to `sources-log.csv` (topic, URL, date, edition-relevant version, note).

## Volatile topic list (must be re-verified before drafting)
| Area | What to verify |
|------|----------------|
| Accounts | 2FA/passkey options, recovery, plan tiers |
| Repos | visibility types, defaults, default-branch behaviour, features by plan |
| Rulesets vs branch protection | current capabilities and plan/visibility limits |
| Actions | hosted runners, usage limits/billing, caching, artifact retention, reusable workflows, environments, OIDC, permissions defaults |
| Security | Dependabot, code scanning/CodeQL, secret scanning/push protection availability by visibility/plan, advisories, private vulnerability reporting |
| Pages | publishing sources, custom domains, HTTPS, limits |
| Codespaces | pricing/quotas, dev container support |
| Packages | supported ecosystems, auth, visibility |
| Projects | views, fields, automation, iterations |
| Discussions, Insights | current features |
| CLI/API | `gh` commands, REST/GraphQL, token types (fine-grained vs classic) |
| Enterprise | Cloud vs Server concepts |
| Git itself | any option/command behaviour differences between versions (e.g. `switch`/`restore`, default branch config, SSH signing) — record the Git version tested |

## Command verification
All commands are run in a clean sandbox on Linux, and (where they differ) noted for Windows/macOS; record Git version; capture real output for "expected output" blocks. No invented flags: every command is checked against `git help <cmd>` or `gh help`.

## Originality control
- Write from understanding, in original wording and original examples.
- No copying from docs, books, courses or blogs; no imitation of any author's distinctive style.
- Licence texts are referenced and summarised, not reproduced (except brief quotes permitted by the licence).

## Sources and Further Reading (back matter)
Populated from `sources-log.csv`; official links only, kept short.
