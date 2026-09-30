# Chapter 40 exercises — Touring the GitHub Interface

Attempt each exercise before you open `solutions/ch40-solutions.md`. Exercises 1 to 3 need only your own computer; 4 and 5 need a browser and any repository that you may view (your own, or a public one).

## Level 1 — Guided

**1.1 The history of one file.** In `bakery-menu`, run `git log --oneline -- menu.md`. Which part of a repository page does this correspond to?

**1.2 A snapshot.** Run `git archive --format=tar --prefix=bakery/ HEAD | tar -t`. Is there a `.git` folder in the list?

## Level 2 — Partially guided

**2.1 The comparison.** Run `git diff --stat HEAD~2 HEAD`. Which view of a platform shows the same information?

**2.2 A tag as a release.** Create an annotated tag `v1.0` and list the tags. Why is a "release" on a platform built on a tag (Chapter 29<!--ref:tags-->)?

## Level 3 — Independent

**3.1 Make a table.** For each part of a repository page (files, branches, tags, history, compare, blame, download, clone address), write the Git command that gives the same information.

**3.2 Git or platform?** Sort these into "in a clone" and "not in a clone": commits, branches, tags, issues, pull requests, the wiki, the `.gitignore` file, workflow files.

## Level 4 — Professional scenario

**4.1 The tour.** Do the tour in section 40.5 on any repository. For each of the eight items, write one line and the matching Git command. Note anything that did not match this chapter.

## Level 5 — Troubleshooting

**5.1** A learner downloads the archive of a project and runs `git log`. Git says it is not a repository. Explain.

**5.2** A learner follows a tutorial that says "click the third icon at the top", but there is no such icon. What should they do?

**5.3** A learner cannot find the Actions tab on a colleague's repository and thinks that it was deleted. Give two other explanations.
