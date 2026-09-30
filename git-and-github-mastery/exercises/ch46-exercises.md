# Chapter 46 exercises — Code Review

Attempt each exercise before you open `solutions/ch46-solutions.md`. Exercises 1 to 3 need only your computer; 4 and 5 are practice with a partner or with your own earlier work.

## Level 1 — Guided

**1.1 Three decisions.** Write the three decisions of a review and one sentence for each.

**1.2 A co-author.** In `bakery-menu`, fix a typo in a commit whose message ends with `Co-authored-by: Sam Reviewer <sam@example.org>`. Show the trailer with `git log -1 --format='%(trailers:key=Co-authored-by,valueonly)'`.

## Level 2 — Partially guided

**2.1 Count the credit.** Run `git shortlog -sne --group=author --group=trailer:co-authored-by HEAD`. Who is counted, and how many times?

**2.2 Rewrite a comment.** Turn "this is wrong" into a specific, kind, actionable comment about a line of `menu.md` of your choice.

## Level 3 — Independent

**3.1 A checklist.** Write your own six-item review checklist, in order of importance, for a project you know.

**3.2 Must or nit.** Take five imaginary comments on a change (for example a missing test, a spelling mistake in a comment, a bug, a variable name, a missing null check). Mark each *must fix* or *nit*, and explain.

## Level 4 — Professional scenario

**4.1 A review round.** Ask a friend to review a small change of yours and answer every comment. Afterwards write what you learned about how you write pull request descriptions.

## Level 5 — Troubleshooting

**5.1** A reviewer approved a pull request on Monday. On Tuesday the author pushed three more commits and merged. What went wrong with the process, and what habit prevents it?

**5.2** A learner's suggestion was applied, but the reviewer is not shown as a contributor on the platform. Give two possible reasons from this chapter and Chapter 37<!--ref:ghaccount-->.
