# Research — Status Report

**Technical information verified: [DATE]** — deliberately NOT filled in. The research phase is **not complete**.

## What was possible and what was not
| Source | Result |
|--------|--------|
| docs.github.com | **Blocked** by the session's egress proxy (organisation network policy) |
| git-scm.com | **Blocked** |
| creativecommons.org | **Blocked** |
| Local Git 2.43.0 binary | Available → used for empirical command verification |
| Local man pages / `git help <cmd>` | Not installed (minimised image); only `-h` usage text works |
| Git LFS, `gh` CLI | Not installed |

Consequence: **zero GitHub claims and zero licence-text claims are verified.** Every one is in `research-ledger.csv` with status `UNVERIFIED`. Nothing about GitHub may be drafted until those rows are filled from official sources.

## What was verified (Git, locally, version 2.43.0)
`git-verification/verify-git-basics.sh` runs in a throwaway directory (host Git config ignored) and checks 51 behaviours. Result: all pass (`verify-git-basics.output.txt`), covering init/default branch, status/add/commit/diff (incl. `--staged`), relative refs, `restore`, `switch`, fast-forward merge, conflict markers and `merge --abort`, `reset --soft/--hard` plus reflog recovery, `revert`, scripted interactive-rebase squash, stash, lightweight vs annotated tags, worktree, grep, blame, object types (blob/tree), `--depth` and `--filter=blob:none` clones, sparse-checkout, a local bare repository used as a remote (push -u, upstream tracking, fetch vs pull, `--force-with-lease`), and existence of the remaining commands/flags the book plans to teach.

### Findings worth teaching or watching
1. `git revert` has no `-q` flag (exit 129). My own first test script got this wrong — a reminder that commands must be run, not recalled.
2. Reverting an **empty** commit fails in this version (my test hit it; cause not yet confirmed against the docs). Do not build an exercise on it until confirmed.
3. A **local bare repository works as a remote**, so Part III can teach remotes with no account and no network. This is a structural improvement (see `../planning/10-architecture-review.md`).
4. The sandbox's host config forced commit signing (`commit.gpgsign true`, SSH format, custom program). Verification scripts must isolate config (`GIT_CONFIG_GLOBAL=/dev/null`) — also a good teaching example of config scopes.
5. **Version gap:** Git 2.43.0 (Debian) is older than the current release. Behaviour described in the book must be re-tested on the newest stable Git before publication, and planned changes in future major versions must be checked in the official release notes.

## Not verified at all (still open)
Git LFS, credential helpers, signing end-to-end (verification with allowed-signers), history-rewriting tools for secrets (filter-repo / BFG), official Git wording, current Git version, SHA-256 status; **everything GitHub**; licence texts; SemVer spec version.

## To unblock
Add these hosts to the environment's allowed domains (Network access → Edit environment): `docs.github.com`, `github.blog`, `git-scm.com`, `creativecommons.org`, `opensource.org`, `spdx.org`, `semver.org`, `www.gnu.org`, `www.apache.org`, `docs.git-scm.com` (and `api.github.com` / `cli.github.com` if `gh` docs are wanted). Also install `git-lfs` and `gh` in the environment setup script if you want them tested.

## Files
- `research-ledger.csv` — 94 rows, columns: id, knowledge_type, topic, claim_to_verify, official_source, url, date_verified, conditions_plan_visibility, notes, stability, status. Stable Git knowledge is separated from time-sensitive GitHub information via `knowledge_type`.
- `git-verification/` — script and its recorded output.
