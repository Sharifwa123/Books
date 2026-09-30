# Chapter 77 solutions

## Level 1
**1.1** After the steps, `git status -sb` shows `## main...origin/main` with nothing ahead or behind.

**1.2** The first line runs the tests and stops with status 1 on failure; the loop checks that the required files exist and stops with status 1 if one is missing; the last line only reports a missing `LICENSE`. A CI system treats a non-zero exit status as a failed check.

## Level 2
**2.1** Write the failing test and show `FAILED`; write the minimum code; show `OK` (or the pipeline's `tests: ok`).

**2.2** For example: "Please name the constant." "Add a test for zero." "Explain the rounding in the README." Each answered by a commit with a clear message.

## Level 3
**3.1** Answers vary. Typical changes: file names, test commands for another language, the check list in `ci.sh`.

**3.2** Answers vary. Typical differences: the layout of pages, wording of buttons, options offered by a repository's merge settings.

## Level 4
**4.1** The handover should follow the steps: test first, branch, pipeline, review, merge strategy, tag and release, revert rather than rewrite, secrets and what to do first, audit.

## Level 5
**5.1** The branch and `main` changed the same lines and the branch was not up to date. Bring `main` into the branch (or rebase), resolve the conflict by reading both sides, run the pipeline, push, then merge again.

**5.2** Revoke or rotate the key first; then stop tracking the file and add it to `.gitignore`; remove it from history only if needed and after telling the team; check where else the key was used and for signs of misuse; add push protection so that it does not recur.
