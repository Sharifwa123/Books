---
key: playbooks
number: 79
tag: Core
first_read: later
status: draft
requires: [trouble]
ledger: [R351, R352]
---
# Chapter 79 — Recovery Playbooks [Core]

**In this chapter**

- five step-by-step recoveries: a pushed secret, lost commits, a bad merge, a failed rebase, a commit on the wrong branch
- each recorded, with the reason for every step
- what each recovery cannot undo

> **How to read this chapter.** The five playbooks were **run and recorded** in Bash and zsh on Git 2.43.0 with `git-filter-repo` 2.47.0, and re-run in CI. A local bare repository stands in for GitHub, and the five playbooks share it, so **later ones start from what earlier ones left behind** (you will see the commit "Stop tracking .env" in the history of later playbooks). The statements about what GitHub keeps after a history rewrite come from GitHub's documentation on removing sensitive data (`github/docs` at commit `2eaab0b`, 29 September 2026) and were **not run on GitHub**. The key in playbook 1 is made up.

**Before you start.** Chapter 78<!--ref:trouble--> (the method) and Chapter 26<!--ref:reflog-->.

**The rules that apply to every playbook.**

1. **Stop and read** the state (`git status`, `git log --oneline --graph --all`) before you type a fix.
2. **Make a safety branch** (`git branch backup`) when you are about to do anything that moves history.
3. **Prefer undoing forwards** (revert, a new commit) to rewriting when others have the commits.
4. **Tell your team** before you rewrite anything shared.

---

## Playbook 1. A secret was pushed

**Situation.** A file with a credential was committed and pushed to the shared repository.

**The order matters.** GitHub's documentation is direct: "if the sensitive data you need to remove is a secret (e.g. password/token/credential), as is often the case, then as a first step you need to revoke and/or rotate that secret. Once the secret is revoked or rotated, it can no longer be used for access, and that may be sufficient to solve your problem. Going through the extra steps to rewrite the history and remove the secret may not be warranted." So:

1. **Revoke** the credential at the service that issued it. This is outside Git and comes first.
2. Stop tracking the file and ignore it (an ordinary commit).
3. Only if you must, **rewrite history** to remove the file everywhere, then push the rewritten history.
4. Deal with the copies you cannot reach.

```text
$ echo "== P1: A secret was pushed"
== P1: A secret was pushed
$ git clone -q hub.git work
$ cd work
$ printf 'API_KEY=not-a-real-key\n' > .env
$ git add .env
$ git commit -q -m "Add configuration"
$ git push -q origin main
$ echo "1. REVOKE the key at the service that issued it (outside Git)"
1. REVOKE the key at the service that issued it (outside Git)
$ git rm -q .env
$ printf '.env\n' > .gitignore
$ git add .gitignore
$ git commit -q -m "Stop tracking .env"
$ git push -q origin main
$ git log --format=%s -S'not-a-real-key'
Stop tracking .env
Add configuration
$ git filter-repo --sensitive-data-removal --invert-paths --path .env --force
NOTICE: Fetching all refs from origin to make sure we rewrite
        all history that may reference the sensitive data, via
      git fetch -q --prune --update-head-ok --refmap "" origin +refs/*:refs/*
Parsed 4 commits
New history written in <n> seconds; now repacking/cleaning...
You rewrote 2 (of 4) commits.

NOTE: First Changed Commit(s) is/are:
  c6f19902e8d163fd177ad0064c2ceca5b2bf778e
NOTE: LFS object orphaning not checked (LFS not in use)

Repacking your repo and cleaning out old unneeded objects
HEAD is now at aa630cc Stop tracking .env
Completely finished after <n> seconds.

NEXT STEPS FOR YOUR SENSITIVE DATA REMOVAL:
  * If you are doing your rewrite in multiple steps, ignore these next steps
    until you have completed all your invocations of git-filter-repo.
  * See the "Sensitive Data Removal" subsection of the "DISCUSSION" section
    of the manual for more details about any of the steps below.
  * Inspect this repository and verify that the sensitive data is indeed
    completely removed from all commits.
  * Force push the rewritten history to the server:
      git push --force --mirror origin
  * Contact the server admins for additional steps they need to take; the
    First Changed Commit(s) may come in handy here.
  * Have other colleagues with a clone either discard their clone and reclone
    OR follow the detailed steps in the manual to repeatedly rebase and
    purge the sensitive data from their copy.  Again, the First Changed
    Commit(s) may come in handy.
  * See the "Prevent repeats and avoid future sensitive data spills" section
    of the manual.

$ git log --format=%s -S'not-a-real-key'
$ git push -q --force --mirror origin
$ git clone -q ../hub.git ../fresh
$ git -C ../fresh log --all --format=%s -S'not-a-real-key'
$ cd ..
```

*Recorded in Bash; `ch79-playbooks/expected-recover.bash.txt`.*

**What the recording showed.** After step 2, the search (`-S`) still found the key in two commits: removing a file in a new commit does not remove it from history. `git filter-repo` (a separate tool, Chapter 33<!--ref:gitsec-->) rewrote the history without the file; the documented form is `--sensitive-data-removal --invert-paths --path FILE`, which needs a version that has the flag (2.47 or later, per the documentation) and, unlike its default behaviour, keeps the `origin` remote and fetches all refs first so that the rewrite covers everything. It prints "NEXT STEPS", including the forced push, which is what `git push --force --mirror origin` did. A **fresh clone** of the shared repository afterwards no longer contains the key.

**What the rewrite cannot do.** GitHub's documentation lists the side effects and limits. Among them: hashes of the affected commits **and all later commits change**, breaking tools that depend on them; open pull requests get confusing; signatures on rewritten commits are lost; branch protection that blocks force pushes has to be turned off temporarily; and "If a fellow developer has a clone from before your rewrite, and after your rewrite simply runs `git pull` followed by `git push`, the sensitive data will return", so colleagues must **discard their clones and clone again** (or follow the manual's cleaning steps). If you only rewrite and force-push, the commits "may still be accessible elsewhere": in clones and forks, "directly via their SHA-1 hashes in cached views on GitHub", and through pull requests that reference them. Fully removing cached views and pull-request references needs a request to GitHub Support, with the number of affected pull requests and the "First Changed Commit(s)" that the tool reports. Forks keep the data unless their owners remove it.

**Verdict.** The rewrite is a large operation with a small guarantee. Revocation is the real fix. Then add push protection (Chapter 62<!--ref:ghsec-->) to stop it recurring.

> **Checked against GitHub's documentation (R351) and locally tested.** "Removing sensitive data from a repository". The Support process was not exercised.

---

## Playbook 2. Commits seem to be lost after a hard reset

**Situation.** You ran `git reset --hard HEAD~2` and two commits disappeared from `git log`.

```text
$ echo "== P2: Commits seem to be lost after a hard reset"
== P2: Commits seem to be lost after a hard reset
$ git clone -q hub.git p2
$ cd p2
$ printf -- "- Coffee: 2.00\n" >> menu.md
$ git commit -q -am "Add coffee"
$ printf -- "- Scone: 2.20\n" >> menu.md
$ git commit -q -am "Add scone"
$ git reset -q --hard HEAD~2
$ git log --format=%s
Stop tracking .env
Add tea
Add the menu
$ git reflog --format='%gd %gs' -n 4
HEAD@{0} reset: moving to HEAD~2
HEAD@{1} commit: Add scone
HEAD@{2} commit: Add coffee
HEAD@{3} clone: from /home/learner/hub.git
$ git reset -q --hard 'HEAD@{1}'
$ git log --format=%s
Add scone
Add coffee
Stop tracking .env
Add tea
Add the menu
$ cd ..
```

*Recorded in Bash; `ch79-playbooks/expected-recover.bash.txt`.*

**What happened.** `reset --hard` moved the branch back two commits and threw away uncommitted changes, but the two commits were still stored. The **reflog** (Chapter 26<!--ref:reflog-->) recorded every move of `HEAD`: `HEAD@{1}` is where you were before the reset. `git reset --hard 'HEAD@{1}'` returned the branch to that place, and the log shows the commits again.

**Limits.** The reflog is local to your clone and entries expire; commits that were never committed (only edited) are gone. Recover soon, and do not run `git gc --prune=now` in between.

---

## Playbook 3. A bad merge reached the shared branch

**Situation.** A branch with a wrong price was merged into `main` and pushed; others have fetched it.

```text
$ echo "== P3: A bad merge reached the shared branch"
== P3: A bad merge reached the shared branch
$ git clone -q hub.git p3
$ cd p3
$ git switch -q -c risky
$ printf -- "- Coffee: 20.00\n" >> menu.md
$ git commit -q -am "Add coffee at a wrong price"
$ git switch -q main
$ printf 'Open daily.\n' > hours.md
$ git add hours.md
$ git commit -q -m "Add opening hours"
$ git merge -q --no-ff -m "Merge risky" risky
$ git push -q origin main
$ git log --format=%s
Merge risky
Add opening hours
Add coffee at a wrong price
Stop tracking .env
Add tea
Add the menu
$ git revert -m 1 --no-edit HEAD > /dev/null
$ git push -q origin main
$ git log --format=%s
Revert "Merge risky"
Merge risky
Add opening hours
Add coffee at a wrong price
Stop tracking .env
Add tea
Add the menu
$ cat menu.md
# Sunrise Bakery menu

- White loaf: 2.50
- Rolls: 3.00
- Tea: 1.50
$ ls
hours.md  menu.md
$ cd ..
```

*Recorded in Bash; `ch79-playbooks/expected-recover.bash.txt`.*

**What happened.** `git revert -m 1` created a **new commit that undoes the merge**, and the push was ordinary because history only grew. `-m 1` tells Git to treat the first parent (the `main` side) as the mainline, so the changes brought in by the branch are removed. The final `menu.md` no longer has the wrong line. **But `hours.md`, which was added on `main` before the merge, is still there**, as it should be: only what the merge brought in was undone.

**Caution about merging again.** After reverting a merge, Git considers the branch's commits as already merged, so merging the same branch later will **not** bring its changes back. To reapply them, revert the revert, or make new commits. Git's howto "Revert a faulty merge" (Git 2.56.0) explains why: reverting a merge "undoes the data changes" but "it doesn't undo history", so a later merge of the fixed branch "will not" contain the reverted changes, and the way out is to revert the revert first. This was read, not run here.

**Never** "fix" this by resetting `main` and force-pushing when others have the merge.

---

## Playbook 4. A rebase went wrong

**Situation.** You started `git rebase main` on your branch and it stopped with a conflict.

```text
$ echo "== P4: A rebase went wrong"
== P4: A rebase went wrong
$ git clone -q hub.git p4
$ cd p4
$ git switch -q -c feature
$ sed -i 's/Rolls: 3.00/Rolls: 3.20/' menu.md
$ git commit -q -am "Rolls 3.20"
$ git switch -q main
$ sed -i 's/Rolls: 3.00/Rolls: 3.50/' menu.md
$ git commit -q -am "Rolls 3.50"
$ git switch -q feature
$ git -c advice.mergeConflict=false rebase main 2>&1 | grep -E '^CONFLICT'
CONFLICT (content): Merge conflict in menu.md
$ git status -sb | head -1
## HEAD (no branch)
$ git rebase --abort
$ git status -sb | head -1
## feature
$ git log --format=%s
Rolls 3.20
Revert "Merge risky"
Merge risky
Add opening hours
Add coffee at a wrong price
Stop tracking .env
Add tea
Add the menu
$ cd ..
```

*Recorded in Bash; `ch79-playbooks/expected-recover.bash.txt`.*

**What happened.** The first search line shows the conflict. `git status -sb` printed `## HEAD (no branch)`: in the middle of a rebase Git checks out the commits one by one, so you are not on your branch. `git rebase --abort` **returned everything to how it was before the rebase**, including the branch name (the next status line) and the branch's own commit at the top of the log.

**Your choices in a stopped rebase.** Resolve the conflict, `git add` the file and `git rebase --continue`; or skip the commit (`--skip`) if it is no longer needed; or abort. Abort is always safe. If you have already finished the rebase and regret it, the reflog has the old tip (Playbook 2).

**Caution.** Rebase rewrites commits. Do it only on commits nobody else has (Chapter 27<!--ref:rebase-->).

---

## Playbook 5. A commit was made on the wrong branch

**Situation.** You committed on `main` when you meant to be on a feature branch, and you have not pushed.

```text
$ echo "== P5: A commit was made on the wrong branch"
== P5: A commit was made on the wrong branch
$ git clone -q hub.git p5
$ cd p5
$ printf -- "- Coffee: 2.00\n" >> menu.md
$ git commit -q -am "Add coffee"
$ git branch feature/coffee
$ git reset -q --hard origin/main
$ git log --format=%s
Revert "Merge risky"
Merge risky
Add opening hours
Add coffee at a wrong price
Stop tracking .env
Add tea
Add the menu
$ git log --format=%s feature/coffee
Add coffee
Revert "Merge risky"
Merge risky
Add opening hours
Add coffee at a wrong price
Stop tracking .env
Add tea
Add the menu
$ git switch -q feature/coffee
$ git push -q -u origin feature/coffee
$ git status -sb | head -1
## feature/coffee...origin/feature/coffee
$ cd ..
```

*Recorded in Bash; `ch79-playbooks/expected-recover.bash.txt`.*

**What happened.** `git branch feature/coffee` created a new branch **at the current commit**, so the commit now has two names. `git reset --hard origin/main` moved `main` back to the remote's version, which is safe because the commit is kept by the other branch (the two logs show it). Then you switched to the new branch and pushed it. The last line shows the branch and its remote in step.

**Never** reset before you have given the commit a second name. If you already did, use the reflog (Playbook 2).

---

## Checkpoint

## What You Learned

- Revoke a leaked secret first; a history rewrite is optional, large and incomplete.
- The reflog undoes a hard reset if you act soon.
- Revert a merge with `-m 1`; remember that re-merging needs care.
- `git rebase --abort` returns to the state before the rebase.
- Give a wrongly placed commit a second name before moving the branch back.

## New Vocabulary

No new terms.

## Commands Learned

`git filter-repo --sensitive-data-removal --invert-paths --path`, `git push --force --mirror`, `git revert -m 1`, `git rebase --abort`.

## Common Mistakes

1. **Rewriting history before revoking the key.**
2. **Force-pushing a rewritten history without telling the team.**
3. **Resetting `main` after a bad merge instead of reverting.**
4. **Continuing a rebase you do not understand instead of aborting.**
5. **Resetting a branch before saving the commit that is on it.**

## Practice

Do the exercises in [`exercises/ch79-exercises.md`](../../../exercises/ch79-exercises.md).

## Self-Test

1. What is the first action when a secret is pushed?
2. Where does `HEAD@{1}` point after a reset?
3. Why does `revert` need `-m 1` for a merge commit?
4. What does `git rebase --abort` restore?
5. Why is Playbook 5 safe?

## Before Moving On

You are ready for Chapter 80<!--ref:challenges--> if you can:

- [ ] carry out each playbook without the book
- [ ] name what each recovery cannot undo

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The five recorded recoveries | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0, git-filter-repo 2.47.0; CI on newer Git | R351, R352 |
| What remains after a rewrite on GitHub, and the Support step | Checked against `github/docs` (commit `2eaab0b`); **not run on GitHub** | R351 |
| Reverting a merge and merging again | Read in Git's howto "Revert a faulty merge" (Git 2.56.0); **not run** | R352 |

## Where this leads

Part XIII, "Mastery", begins with Chapter 80<!--ref:challenges-->: harder tasks that combine these recoveries.
