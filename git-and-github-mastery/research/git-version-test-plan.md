# Git Version Testing Plan (publication baseline)

Current baseline in this repo: **Git 2.43.0** (Ubuntu 24.04 distribution build, git-lfs 3.4.1). This is *useful regression evidence*, not the publication baseline: distribution builds lag upstream.

## Steps before publication
1. **Determine the current supported Git release** from the official Git release notes/downloads (git-scm.com). *Blocked now; do not guess a version number.*
2. **Obtain that version** (official source tarball or an official/trusted package channel) and record how it was obtained and its checksum.
3. **Run the three scripts unchanged** against it: `verify-git-basics.sh`, `verify-config-and-lfs.sh`, and re-run `verify-against-docs.py` against *that version's* documentation.
4. **Record** version, date, OS, result in `git-version-matrix.csv` (one row per version per script) and keep raw output under `results/git-<version>/`.
5. **Investigate every discrepancy** between versions: is it a behaviour change, a documentation change, or a test defect? Record the cause in the ledger; update the book only after understanding it.
6. **Re-run every exercise** in `exercises/registry.csv` marked for publication, on the publication baseline; update `verified_on_git`.
7. Also test on **Windows (Git Bash)** and **macOS** where behaviour may differ (line endings, credential helpers, file permissions, paths). Not yet possible in this Linux sandbox.
8. Optionally test one older supported release to state a minimum version for each command that needs one (e.g. `git switch`/`git restore`).

## Runner
`run-all.sh` runs all checks with whichever `git` is first on `PATH` and stores results under `results/git-<version>/`.

## Open questions to close in step 5
- Is `git switch`/`git restore` still labelled experimental in current docs?
- Reverting an *empty* commit: fails on 2.43.0 with "nothing to commit" (exit 1); confirm on the baseline and find the documented/intended behaviour before any exercise depends on it.
- Any changes to default branch naming, hash function default, or `git pull` defaults announced in release notes.
