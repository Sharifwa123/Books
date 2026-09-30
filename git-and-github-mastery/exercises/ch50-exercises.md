# Chapter 50 exercises — Branch Protection and Rulesets

Attempt each exercise before you open `solutions/ch50-solutions.md`. Exercises 1 to 3 need only your computer.

## Level 1 — Guided

**1.1 A server that refuses.** Create a bare repository `hub.git` with one commit on `main`, and set `receive.denyNonFastForwards` and `receive.denyDeletes` to `true`. Clone it.

**1.2 Try to force.** In the clone, amend the commit and run `git push --force origin main`. What does the message say, and which side wrote it?

## Level 2 — Partially guided

**2.1 Delete.** Try `git push origin --delete main`. What is refused?

**2.2 Only one.** Turn off `receive.denyDeletes` (set it to `false`) and repeat 2.1 on a *copy* of the branch (push a branch `scratch` first). What changes?

## Level 3 — Independent

**3.1 Which is which?** Match each to a Git server setting or a platform feature: block force pushes; restrict deletions; require a pull request; require passing checks.

**3.2 Layering.** One ruleset requires two reviews and signed commits on `main`. Another requires three reviews. What applies to `main`?

## Level 4 — Professional scenario

**4.1 A first policy.** Write a five-line protection policy for a team of six that keeps `main` safe, and say who may bypass it.

## Level 5 — Troubleshooting

**5.1** An administrator force-pushes to a protected branch and it works. Give a likely reason from section 50.3.

**5.2** A new ruleset breaks the team's workflow on its first day. Which enforcement status should it have started in?
