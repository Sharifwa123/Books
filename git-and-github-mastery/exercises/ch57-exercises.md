# Chapter 57 exercises — Debugging and Re-running Workflows

Attempt each exercise before you open `solutions/ch57-solutions.md`. Exercises 1 to 3 need only your computer.

## Level 1 — Guided

**1.1 The method.** Write the four questions of section 57.1 in order.

**1.2 Ask Git to explain.** Run `GIT_TRACE=1 git rev-parse --git-dir` in a repository. What does the first line say?

## Level 2 — Partially guided

**2.1 A skip request.** Make two commits, one with `[skip ci]` in the subject and one with a `skip-checks: true` trailer. Show the trailer with `git interpret-trailers --parse`.

**2.2 Read the log.** Find the first red step in a failed run of any repository you can see (or in the sample below) and say which line caused the failure: `Run sh ci.sh` / `FAIL test: a line has no price` / `Error: Process completed with exit code 1.`

## Level 3 — Independent

**3.1 A trigger checklist.** A workflow with `on: issues` is in a branch called `new-workflow` and never runs. Give the reason from section 57.3 and the fix.

**3.2 Re-run or new run?** You pushed a fix commit after a run failed. Should you re-run the failed run? Explain using what a re-run uses.

## Level 4 — Professional scenario

**4.1 A flaky check.** A check fails one time in five. Write the steps you would take, and what you would not do.

## Level 5 — Troubleshooting

**5.1** A pull request has a merge conflict and its workflows are not running. Explain and fix.

**5.2** A job with `if: ${{ always() }}` keeps running after a cancel. What does the documentation suggest instead?

**5.3** A required check stays "Pending" forever after a commit message containing `[skip ci]`. Explain, and give two ways to get the pull request mergeable.
