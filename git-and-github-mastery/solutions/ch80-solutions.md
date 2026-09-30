# Chapter 80 solutions

Reference solutions were run and recorded (`verification/ch80-challenges`). Commit names differ on your computer.

## Challenge 1
```shell
cd app
git -c protocol.file.allow=always submodule update --remote vendor/lib
git status --short      # shows " M vendor/lib": the pointer changed
git commit -am "Update lib to version 2"
```
`cat vendor/lib/lib.txt` prints `version 2`. The outer project stores the inner commit's name, so updating means committing the new pointer.

## Challenge 2
```shell
git clone mono site-only
cd site-only
git filter-repo --subdirectory-filter site
git log --format=%s        # Change site again / Change site / Start
ls                         # index.html
git rev-list --count HEAD  # 3
```
Work on a clone because the tool rewrites history and removes the `origin` remote. The commit "Change tools" touched no site file and disappears.

## Challenge 3
```shell
git clone --depth 1 --no-checkout file://$PWD/big slim
cd slim
git sparse-checkout set docs
git checkout main
git rev-list --count HEAD   # 1
ls                          # docs
```
The `file://` address makes Git use the real transport, which honours `--depth`; a plain path is copied directly.

## Challenge 4 — rubric
Award one point per part that is present, consistent with the others and justified in a sentence; six or seven points is a good design.

1. **Branches and merges:** short-lived topic branches from `main`, pull requests, one merge strategy stated (Chapters 45<!--ref:pr--> and 21<!--ref:merging-->).
2. **Automated checks:** tests and linters on every pull request, plus security checks; local script runnable by contributors (Chapters 52<!--ref:cicd-->, 54<!--ref:actions-->, 77<!--ref:capstone-->).
3. **Protection and review:** required checks and at least one review, no force pushes to `main`, code owners for sensitive folders (Chapters 46<!--ref:review--> and 50<!--ref:protect-->).
4. **Releases:** annotated tags, semantic versioning, notes, checksums (Chapters 29<!--ref:tags--> and 66<!--ref:releases-->).
5. **Hotfix:** branch from the release tag, fix, new patch tag, carry the fix to `main` with `cherry-pick -x` (Chapter 76<!--ref:scenarios-->).
6. **Secrets and dependencies:** push protection, secret scanning, dependency alerts, least-privilege tokens, pinned actions (Chapters 60<!--ref:wfsec-->, 62<!--ref:ghsec-->, 63<!--ref:secpractice-->).
7. **Newcomers:** README, `CONTRIBUTING.md`, code of conduct, `good first issue` labels (Chapters 42<!--ref:readme--> and 64<!--ref:oss-->).

Because the application handles customers' data, a strong answer stresses secrets handling and review.

## Challenge 5
```shell
printf 'grep -qx ok state.txt\n' > ../test.sh
git bisect start HEAD HEAD~12
git bisect run sh ../test.sh
git bisect reset
```
Git reports "Change state" as the first bad commit. The test uses `-x` (whole-line match): with `grep -q ok`, the word `broken` also contains `ok` and the test would wrongly pass everywhere.

## Challenge 6
```shell
git fsck --lost-found        # dangling commit <name>
git log -1 <name>            # Precious work
git branch rescued <name>
```
`fsck` lists objects that nothing reaches, without needing the reflog. Garbage collection would eventually remove them, so rescue soon.

## Exercise 1.1
The update command fetches the newest inner commit and moves the inner working tree to it; `git status` shows the pointer as modified; the commit in the outer project records the new inner commit name. The outer project stores only the name of one commit of the inner repository (and its path), not the inner files.

## Exercise 2.1
Add the second submodule the same way, run `git submodule update --remote` for both, and commit once with `git commit -am`. A colleague runs `git submodule update --init` after `git pull` so that the inner working trees match the recorded commits.

## Exercise 3.1
`git filter-repo --path site --path tools` on a fresh clone keeps only those folders in place. The commits that touched only `notes` disappear, so the count is lower than in `mono`.

## Exercise 5.1
Bisect assumes that a commit is either good or bad deterministically. A test that fails randomly can mark a good commit bad, so bisect converges on a wrong commit. Make the test deterministic, or run it several times and treat any failure as bad, and check the result by testing the neighbouring commits.

## Exercise 4.1
For example: (1) branch rule: protection requires pull requests; (2) checks: the workflow file runs `ci.sh` on each pull request; (3) review: a rule requires one approval and code-owner review for sensitive folders; (4) releases: a check that the tag matches the version file; (5) hotfix: a documented branch name pattern and a rule that hotfixes are cherry-picked to `main`; (6) secrets: push protection enabled and a scheduled dependency update; (7) newcomers: a check that README, contributing guide and code of conduct exist (as in the capstone's pipeline).
