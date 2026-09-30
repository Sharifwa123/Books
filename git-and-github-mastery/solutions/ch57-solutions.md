# Chapter 57 solutions

## Level 1
**1.1** Did it start at all? Did the file load? Which job or step failed, and what did it print? Does it fail only there?

**1.2** `trace: built-in: git rev-parse --git-dir` (after removing the time stamp and source location).

## Level 2
**2.1** `git commit -am "Change [skip ci]"` and `git commit -am "Change" -m "skip-checks: true"`; `git log -1 --format=%B | git interpret-trailers --parse` prints `skip-checks: true`.

**2.2** The cause is `FAIL test: a line has no price`; the last line only says the process exited with code 1.

## Level 3
**3.1** `issues` runs only from the default branch, so a workflow file that exists only on another branch will not trigger; merge it into the default branch.

**3.2** No. A re-run tests the same commit and the same ref as the original run, so it would not test your fix. Look at the new run started by your push.

## Level 4
**4.1** Note the failures, read the logs of failing and passing runs, look for timing, network or ordering causes, fix or isolate the cause, and do not simply re-run until green.

## Level 5
**5.1** Workflows do not run on `pull_request` activity when the pull request has a merge conflict; resolve the conflict.

**5.2** Use `!cancelled()`, the inverse of `cancelled()`, which does not return true on cancellation.

**5.3** A skipped workflow leaves its checks pending, and a pull request that requires them cannot merge. Push a commit without the skip string so the checks run, or change the rules that require them (with the right permission).
