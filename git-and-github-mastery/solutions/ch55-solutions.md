# Chapter 55 solutions

## Level 1
**1.1** `git symbolic-ref HEAD` gives `refs/heads/feature-tea` (`github.ref`); `git rev-parse --abbrev-ref HEAD` gives `feature-tea` (`github.ref_name`); `git rev-parse HEAD` gives the commit SHA (`github.sha`).

**1.2** `refs/tags/v1.0`.

## Level 2
**2.1** The line `refs/tags/v1.0`, for a tag.

**2.2** It runs only when the run came from the branch `main`. With `'main'`, the condition would never be true because `github.ref` is the fully-formed ref `refs/heads/main`.

## Level 3
**3.1** (a) `if: ${{ github.event_name == 'push' }}`; (b) `if: ${{ !cancelled() }}`; (c) `if: ${{ failure() }}`.

**3.2** `'Main' == 'main'` is true (string case is ignored); `1 == '1'` is true (the string is parsed as the number 1); `null == 0` is true (null is coerced to 0).

## Level 4
**4.1** A step output is a string, so convert it: `fromJSON(steps.x.outputs.count) > 9`.

## Level 5
**5.1** Dereferencing a nonexistent property evaluates to an empty string; it does not fail. The real property is `github.actor`.

**5.2** If the checkout fails critically, an `always()` step can keep going and the workflow may hang until it times out; use `!cancelled()` instead where suitable.
