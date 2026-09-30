# Chapter 59 solutions

## Level 1
**1.1** Hosted: GitHub provides and maintains it, and it starts clean. Self-hosted: you deploy, update and secure it, and it need not be clean for each job.

**1.2** `echo $((3*3*2))` is 18, well within 256.

## Level 2
**2.1** 18 times n exceeds 256 when n is 15 or more (18 times 14 is 252; 18 times 15 is 270).

**2.2** `concurrency:` then `group: ${{ github.workflow }}-${{ github.ref }}` and `cancel-in-progress: true`.

## Level 3
**3.1** Cancelling a deployment part-way can leave production half-updated. Prefer letting the running deployment finish and queueing or dropping the newer one, with `cancel-in-progress: false`.

**3.2** Any four of: untrusted code could read the keys; the machine is not clean between jobs; a compromised job can persist; secrets passed on command lines can be seen by other jobs; the runner may serve several repositories.

## Level 4
**4.1** The documentation says self-hosted runners "should almost never be used for public repositories" because any user can open a pull request and compromise the environment. Use GitHub-hosted runners, and reduce minutes by caching and by cancelling outdated runs.

## Level 5
**5.1** A newer push in the same concurrency group with `cancel-in-progress`; or a documented limit (for example the 6-hour job limit).

**5.2** The 500 KB workflow file limit; move shared logic into a reusable workflow or a composite action.
