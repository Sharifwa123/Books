# Chapter 29 exercises — Tags and Versioning

Attempt each exercise before you open `solutions/ch29-solutions.md`. Use `bakery-menu` (rebuild it from Chapter 17<!--ref:history_view--> if needed) and a bare repository as the remote (Chapter 23<!--ref:remotes-->).

## Level 1 — Guided

**1.1 Tag the first commit.** Find the hash of the first commit with `git log --oneline`. Tag it `v0.1.0` with `git tag -a`. Show it with `git show v0.1.0`.

**1.2 Tag the latest commit.** Tag `HEAD` as `v1.0.0`. List the tags.

## Level 2 — Partially guided

**2.1 A pre-release.** Add a lightweight tag `v1.0.0-rc.1` on the commit before `HEAD`. List the tags with `git tag`. Is the order sensible? Try `--sort=version:refname` and then `-c versionsort.suffix=-rc`.

**2.2 Describe.** Run `git describe`. Then run `git describe --tags <first-commit-hash>`.

## Level 3 — Independent

**3.1 Push one tag.** Create the bare repository, add it as `origin`, push `main`, then push only `v1.0.0`. Use `git ls-remote --tags origin` to show that only it arrived.

**3.2 Push them all.** Push the remaining tags with `--tags`. How many lines does `ls-remote` show for an annotated tag, and why?

## Level 4 — Professional scenario

**4.1 A wrong release.** You published `v1.0.0` on the wrong commit. The team has already fetched it. What do you do? Write the commands, and say why you do not move the tag.

## Level 5 — Troubleshooting

**5.1** A learner deleted a tag with `git tag -d` and says the release "is still on the server". Explain and give the fix.

**5.2** A learner pushed with `git push origin --tags` and now dozens of old test tags are on the shared repository. What are the options, and what is the lesson?

**5.3** A learner sorts tags with `git tag` and sees `v1.10.0` before `v1.2.0`. Why, and what is the fix?
