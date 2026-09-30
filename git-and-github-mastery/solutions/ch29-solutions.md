# Chapter 29 solutions

## Level 1
**1.1** `git tag -a v0.1.0 <hash> -m "First draft"`; `git show v0.1.0` prints the tag's details, then the commit.

**1.2** `git tag -a v1.0.0 -m "First public menu"`; `git tag` lists both.

## Level 2
**2.1** Plain order puts `v1.0.0-rc.1` after `v1.0.0`; `--sort=version:refname` alone does the same; with `-c versionsort.suffix=-rc` the release candidate comes first.

**2.2** `git describe` prints `v1.0.0` on the tagged commit; the second prints `v0.1.0`.

## Level 3
**3.1** `git ls-remote --tags origin` lists only `v1.0.0` (two lines: the tag object and the peeled commit `^{}`).

**3.2** After `--tags`, every local tag is there. An annotated tag shows twice (the tag object and the `^{}` commit); a lightweight tag shows once.

## Level 4
**4.1** Do not move or re-use the tag; others have already fetched it, and their copies would not change. Create a new correct tag, for example `git tag -a v1.0.1 <right-commit> -m "..."`, push it, and tell the team.

## Level 5
**5.1** `git tag -d` deletes only the local tag. Remove it on the remote with `git push origin --delete <tag>`.

**5.2** Delete the unwanted tags on the remote (`git push origin --delete <tag>` for each) if nobody has used them, but people may already have fetched them. The lesson is to push named tags rather than `--tags`, and to check `git tag` first.

**5.3** `git tag` sorts alphabetically, so `1.10` comes before `1.2`. Use `git tag --sort=version:refname`.
