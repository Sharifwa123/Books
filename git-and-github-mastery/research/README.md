# Research — Status Report

> **Current status (30 September 2026).** The ledger now has **356 rows**: 127 "both officially verified and locally tested", 113 "officially verified (docs only)", 34 "locally tested", 56 "time-sensitive (unverified)", 23 "needs re-verification" and 3 "not applicable". **79 rows are still marked unverified** (55 of them early planning rows superseded by later rows); Appendix N of the book lists them. Git was checked against the Git 2.56.0 manual (`git-manual-checks.py`, 67 checks) and the recorded sessions are re-run in CI on the runner's Git and on Git 2.56.0 built from source. GitHub claims were checked against the `github/docs` repository at commit `2eaab0b`; nothing was run on a live account. `sources-manifest.csv` holds the hash of every fetched source. The sections below are the **historical report of 29 September 2026** and describe the state at that date (for example, only 109 ledger rows and blocked hosts that have since been worked around through GitHub-hosted raw sources).

**Technical information verified: [DATE]** — deliberately NOT filled in. Research is **not complete**; the book-level date is set only after every time-sensitive ledger row is verified.

## Evidence classes (used in `research-ledger.csv`)
Officially verified · Locally tested · Both officially verified and locally tested · Time-sensitive · Needs re-verification · Not applicable. A locally tested claim is never called officially verified. Where "official" means the documentation *packaged with a specific Git version* (not the live git-scm.com manual), the row says so in `verification_scope` and stays `needs_reverification = yes`.

## Source access (checked 2026-09-29)
| Host | Reachable? | Effect |
|------|-----------|--------|
| www.apache.org | **Yes** | Apache-2.0 text verified (`licences/apache-2.0-verification.md`) |
| docs.github.com, github.blog | No (egress policy) | **All GitHub claims unverified** |
| git-scm.com | No | current Git reference/release notes unavailable |
| creativecommons.org | No | **CC BY-NC-SA 4.0 name/identifier/terms unverified** |
| opensource.org, spdx.org | No | MIT text and SPDX identifiers unverified |
| semver.org, www.gnu.org | No | SemVer spec, GPL/LGPL texts unverified |
| archive.ubuntu.com | Yes | Used to obtain the Git 2.43.0 upstream docs (`git-doc`, `git-man`) and `git-lfs` 3.4.1 — **version-bound**, not current |

I cannot change the environment's network policy. Hosts to add (minimum set you specified): docs.github.com, github.blog, git-scm.com, creativecommons.org, opensource.org, spdx.org, semver.org, www.gnu.org (www.apache.org already works). Optional, for Appendix M and the shell chapter: learn.microsoft.com (PowerShell/Command Prompt), support.apple.com (macOS shell).

## What has been checked
| Check | Script | Result (Git 2.43.0) |
|-------|--------|--------------------|
| Core behaviour in a throwaway sandbox (host config ignored) | `git-verification/verify-git-basics.sh` | 51 pass / 0 fail |
| Config scopes, `includeIf`, environment influence, rebase todo help text, Git LFS pointers | `git-verification/verify-config-and-lfs.sh` | 28 pass / 0 fail |
| Claims vs the upstream docs packaged with Git 2.43.0 | `git-verification/verify-against-docs.py` | 82 pass / 0 fail |
| Apache-2.0 official text | manual, `licences/` | verified |

`git-verification/run-all.sh` re-runs everything with whichever `git` is on PATH and stores results per Git version under `results/`; `git-version-matrix.csv` records runs. **These are regression tests, not the publication baseline** — see `git-version-test-plan.md`.

## Ledger (109 rows)
Migrated from 94 rows; added the evidence-class, scope, conditions (account type, repository visibility, organization context, permissions, plan limitations, feature availability) and re-verification columns, plus 15 rows for licences and new v2 topics. Counts: Time-sensitive (unverified) 55 · Needs re-verification 21 · Both 19 · Locally tested 7 · Officially verified (docs only) 7. **All 55 GitHub rows remain unverified; their condition columns read `TO RECORD`.**

## Findings
1. `git revert` has **no `-q`/`--quiet` option** (usage text, runtime exit 129, and absent from the 2.43.0 docs). Methodology point: commands are executed and verified, not recalled.
2. Reverting an **empty commit fails** on 2.43.0 (exit 1, "nothing to commit"). The git-revert docs are silent on it; git-cherry-pick docs say empty cherry-picks fail by default. Cause/intent unconfirmed → `EX-revert-empty-commit` is **BLOCKED** in `exercises/registry.csv`.
3. The 2.43.0 docs label **`git switch` and `git restore` EXPERIMENTAL**. Check the current release's wording before deciding how to present them.
4. Interactive-rebase todo commands are described in **prose** in the 2.43.0 rebase docs; the exact command list is printed in the editor's todo help (verified at runtime: pick, reword, edit, squash, fixup, exec, break, drop, label, reset, merge).
5. **Configuration**: precedence system < global < local < worktree (worktree needs `extensions.worktreeConfig`); `--show-origin`/`--show-scope` reveal the winner; an **inherited `commit.gpgsign=true` with a broken signer makes a plain `git commit` fail** (fix for one command: `-c commit.gpgsign=false`); `GIT_CONFIG_NOSYSTEM=1` hides the system scope even when `GIT_CONFIG_SYSTEM` is set; `GIT_CONFIG_GLOBAL=/dev/null` isolates from the global scope. My first draft of a NOSYSTEM test was wrong, not Git — recorded as a reminder to test the test.
6. A **local bare repository works as a remote**, enabling account-free remote exercises.
7. **Git LFS 3.4.1**: install, track (`.gitattributes`) and pointer-file commits work locally; server behaviour and quotas untested.
8. `git filter-branch` docs (2.43.0) warn about pitfalls and point to `git-filter-repo`; the tools themselves (filter-repo, BFG) are **not** verified.

## Still open
Everything GitHub · current Git release and re-run of all scripts on it · CC/MIT/SPDX/SemVer/GPL texts · credential helpers, end-to-end signing, hooks and attributes *execution* · Windows/macOS behaviour · current UI labels.
