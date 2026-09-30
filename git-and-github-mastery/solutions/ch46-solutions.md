# Chapter 46 solutions

## Level 1
**1.1** Comment: general feedback without approving or requesting changes. Approve: the changes are ready to merge. Request changes: feedback the author should address before merging.

**1.2** The command prints `Sam Reviewer <sam@example.org>`.

## Level 2
**2.1** Ada is counted for each commit she authored, and the reviewer once for the commit with the trailer (in the recording: 2 and 1).

**2.2** For example: "Line 4: 'slise' looks like a typo for 'slice'. Could you check the spelling?"

## Level 3
**3.1** Answers vary. A sensible order: purpose, correctness, safety, tests and checks, clarity, style.

**3.2** Missing test, bug and missing null check: must fix. Spelling in a comment and variable name: nits, unless the name is misleading.

## Level 4
**4.1** Answers vary.

## Level 5
**5.1** The approval was about the earlier version of the change; new commits were merged without a fresh look. Look again after every push before approving, and repositories can require re-approval after new commits (Chapter 50<!--ref:protect-->).

**5.2** The email in the `Co-authored-by` line may not be associated with the reviewer's account (Chapter 37<!--ref:ghaccount--> explains email matching), or it may be a different address from the one the account confirmed.
