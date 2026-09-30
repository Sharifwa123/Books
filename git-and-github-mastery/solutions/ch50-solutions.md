# Chapter 50 solutions

## Level 1
**1.1** `git -C hub.git config receive.denyNonFastForwards true` and `git -C hub.git config receive.denyDeletes true`.

**1.2** The server prints `remote: error: denying non-fast-forward refs/heads/main (you should pull first)` and the push shows `[remote rejected] main -> main (non-fast-forward)`. The `remote:` line was written by the server side.

## Level 2
**2.1** The deletion: `denying ref deletion for refs/heads/main` and `(deletion prohibited)`.

**2.2** With `receive.denyDeletes` false the deletion of `scratch` succeeds; the non-fast-forward rule is separate and still applies.

## Level 3
**3.1** Block force pushes: `receive.denyNonFastForwards`; restrict deletions: `receive.denyDeletes`; require a pull request and require passing checks: platform features (branch protection or rulesets), not Git server settings.

**3.2** Rules are aggregated and the most restrictive version applies: signed commits and three reviews.

## Level 4
**4.1** For example: require a pull request with one review; require passing checks; block force pushes and deletions; require conversation resolution; only repository administrators may bypass, and each bypass is noted in the pull request.

## Level 5
**5.1** By default the restrictions of a branch protection rule do not apply to people with admin permissions, unless the rule is set to apply to administrators too.

**5.2** *Evaluate* (where offered): it monitors which actions would violate the rules without enforcing them.
