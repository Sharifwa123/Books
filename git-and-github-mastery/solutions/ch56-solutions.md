# Chapter 56 solutions

## Level 1
**1.1** Six: the loop over `version` is outer and the loop over `os` inner, giving the order in the documentation.

**1.2** At minutes 2 and 10 of hours 4 and 5, every day (UTC).

## Level 2
**2.1** `*/20` gives 0, 20, 40; `20/15` gives 20, 35, 50.

**2.2** 3 times 2 times 2 is 12 jobs. Each combination uses a runner and time, so matrices grow quickly.

## Level 3
**3.1** `on: pull_request` and two jobs with no `needs`; jobs run in parallel by default.

**3.2** The first step runs `echo 'PRICE=2.80' >> $GITHUB_ENV`. Steps are separate processes, so environment variables are not preserved, but the file that `$GITHUB_ENV` names is shared and GitHub reads it for later steps.

## Level 4
**4.1** For example `17 6 * * 1` (Monday at 06:17 UTC). It needs to read pull requests and create an issue; give the token only those permissions (Chapter 60<!--ref:wfsec-->).

## Level 5
**5.1** Except for `GITHUB_TOKEN`, secrets are not passed to the runner when a workflow is triggered from a forked repository.

**5.2** In a public repository, scheduled workflows are automatically disabled when there has been no repository activity for 60 days; a user with write permission who changes the cron schedule in a commit reactivates it.

**5.3** Cache poisoning: caches are shared by branch or tag and restored as-is, so treat restored files as untrusted; GitHub gives workflows that run for low-trust triggers read-only access to caches in the default branch's scope.
