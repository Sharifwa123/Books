---
key: trouble
number: 78
tag: Core
first_read: later
status: draft
requires: [capstone]
ledger: [R350]
---
# Chapter 78 — Troubleshooting Handbook [Core]

**In this chapter**

- a method for reading any error message
- fifteen common Git errors, each **produced on purpose and recorded**
- for each: meaning, cause, how to diagnose, the safe fix, the dangerous fix, prevention
- errors this book could not reproduce, and where to look

> **How to read this chapter.** Every recording ran in Bash and zsh on Git 2.43.0 and is re-run in CI on newer Git. The recordings show **only the lines that matter**: they keep the `fatal:`, `error:` or first line of a message and leave out the "hint:" lines, whose wording changes from version to version (your Git may print more, or different, text; the meaning stays). Paths and names are made up. **Errors that need a network, an account or a password (for example refused SSH keys or HTTP 403) could not be reproduced offline** and are described in the last section without recordings.

**Before you start.** Chapter 77<!--ref:capstone--> and Part III.

---

## 78.1 A method for reading errors

1. **Read the first line and the last line.** The first says what failed; the last often says what to try.
2. **Run `git status`.** It answers half of all questions: which branch, what is staged, what is in conflict.
3. **Do not run the first fix that you find.** Search results and old answers suggest `--force`, `reset --hard` and `rm -rf`. Read the "dangerous fix" column before you act.
4. **Look before you change anything**: `git log --oneline --graph --all`, `git diff`, `git remote -v`.
5. **Make a safety copy when in doubt**: `git branch backup` costs nothing, and the reflog (Chapter 26<!--ref:reflog-->) is your second net.
6. **Change one thing at a time**, and run `git status` again.

---

## 78.2 fatal: not a git repository (or any of the parent directories): .git

**Message.** `fatal: not a git repository (or any of the parent directories): .git`

**Recording.**

```text
$ echo "== E1: not a git repository"
== E1: not a git repository
$ mkdir empty && cd empty
$ git status 2>&1 | grep -E '^fatal'
fatal: not a git repository (or any of the parent directories): .git
$ cd ..
```

*Recorded in Bash; `ch78-trouble/expected-handbook.bash.txt`.*

**Meaning.** Git looked in this folder and every parent for a `.git` folder and found none.

**Cause.** You are in the wrong folder, or the folder was never made a repository, or `.git` was deleted.

**Diagnose.** `pwd` and `ls -a` show where you are; `git rev-parse --show-toplevel` names the repository if there is one.

**Safe fix.** `cd` into the project folder; or `git init` if this really is a new project; or clone it.

**Dangerous fix.** Running `git init` in your home folder or another large folder "to make the error go away": it turns an unrelated folder into a repository.

**Prevention.** Open the terminal in the project folder; show the current branch in your prompt (Chapter 7<!--ref:terminal-->).

---

## 78.3 fatal: pathspec 'x' did not match any files

**Message.** `fatal: pathspec 'x' did not match any files / error: pathspec 'x' did not match any file(s) known to git`

**Recording.**

```text
$ echo "== E2: pathspec did not match"
== E2: pathspec did not match
$ git clone -q hub.git w2
$ cd w2
$ git add missing.txt 2>&1 | grep -E '^fatal'
fatal: pathspec 'missing.txt' did not match any files
$ git checkout no-such-branch 2>&1 | grep -E '^error'
error: pathspec 'no-such-branch' did not match any file(s) known to git
$ cd ..
```

*Recorded in Bash; `ch78-trouble/expected-handbook.bash.txt`.*

**Meaning.** Git was given a name (a file, or a branch for `checkout`) that it cannot find.

**Cause.** A typo, the wrong folder, a file that does not exist yet, or a branch that exists only on the remote and has not been fetched.

**Diagnose.** `git status`, `ls`, `git branch -a` and `git fetch` show what exists.

**Safe fix.** Correct the name; `git fetch` and try again for a remote branch.

**Dangerous fix.** Creating an empty file or branch with the wanted name just to silence the error.

**Prevention.** Use tab completion; run `git status` before `git add` (Chapter 19<!--ref:commits-->).

---

## 78.4 Author identity unknown

**Message.** `Author identity unknown`

**Recording.**

```text
$ echo "== E3: identity unknown"
== E3: identity unknown
$ git clone -q hub.git w3
$ cd w3
$ printf 'x\n' > a.txt
$ git add a.txt
$ git commit -m "Add a" 2>&1 | grep -E '^Author identity unknown'
Author identity unknown
$ cd ..
```

*Recorded in Bash; `ch78-trouble/expected-handbook.bash.txt`.*

**Meaning.** Git will not create a commit without a name and an email address to record.

**Cause.** You have not set `user.name` and `user.email` on this computer (Chapter 14<!--ref:config-->).

**Diagnose.** `git config --get user.name` and `--get user.email` print nothing.

**Safe fix.** Set them once with `git config --global user.name "Your Name"` and `git config --global user.email "you@example.org"`, then repeat the commit.

**Dangerous fix.** Committing with someone else's identity, or with an address you do not want public: the address is part of every commit forever.

**Prevention.** Do the first-time configuration as soon as you install Git (Chapter 14<!--ref:config-->).

---

## 78.5 On branch main ... nothing to commit

**Message.** `On branch main ... nothing to commit / no changes added to commit`

**Recording.**

```text
$ echo "== E4: nothing to commit"
== E4: nothing to commit
$ git config --global user.name "Ada Learner"
$ git config --global user.email "ada@example.org"
$ git clone -q hub.git w4
$ cd w4
$ git commit -m "Nothing" 2>&1 | head -2
On branch main
Your branch is up to date with 'origin/main'.
$ printf 'new\n' > new.txt
$ git commit -m "Nothing" 2>&1 | head -3
On branch main
Your branch is up to date with 'origin/main'.

$ cd ..
```

*Recorded in Bash; `ch78-trouble/expected-handbook.bash.txt`.*

**Meaning.** There was nothing staged, so no commit was made.

**Cause.** You forgot `git add`, or the change was already committed, or the new file is untracked (the second try shows it under "Untracked files").

**Diagnose.** `git status` lists changed, staged and untracked files.

**Safe fix.** `git add FILE` and commit again; for a tracked file changed in place `git commit -am` also works.

**Dangerous fix.** Using `--allow-empty` to force a commit that records nothing.

**Prevention.** Read `git status` before committing.

---

## 78.6 error: Your local changes to the following files would be overwritten by checkout

**Message.** `error: Your local changes to the following files would be overwritten by checkout`

**Recording.**

```text
$ echo "== E5: checkout would overwrite"
== E5: checkout would overwrite
$ git clone -q hub.git w5
$ cd w5
$ git switch -q -c other
$ printf -- '- Rolls: 3.00\n' >> menu.md
$ git commit -q -am "Rolls"
$ git switch -q main
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git switch other 2>&1 | grep -E '^error'
error: Your local changes to the following files would be overwritten by checkout:
$ git stash -q
$ git switch -q other
$ git stash pop 2>&1 | grep -E '^(CONFLICT|Auto-merging)'
Auto-merging menu.md
CONFLICT (content): Merge conflict in menu.md
$ cd ..
```

*Recorded in Bash; `ch78-trouble/expected-handbook.bash.txt`.*

**Meaning.** Switching branches would destroy edits that are not committed.

**Cause.** You have uncommitted changes in a file that differs between the two branches.

**Diagnose.** `git status` and `git diff` show your changes.

**Safe fix.** Commit them, or `git stash` them and bring them back with `git stash pop` (the recording shows a conflict on `pop`, which you resolve like any conflict), then switch.

**Dangerous fix.** `git checkout -f` or `git reset --hard`: both throw your changes away without a trace.

**Prevention.** Commit or stash before switching (Chapter 24<!--ref:stash-->).

---

## 78.7 ! [rejected] main -> main (fetch first)

**Message.** `! [rejected] main -> main (fetch first) / error: failed to push some refs`

**Recording.**

```text
$ echo "== E6: push rejected"
== E6: push rejected
$ git clone -q hub.git a6
$ git clone -q hub.git b6
$ cd a6
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -q -am "Tea"
$ git push -q origin main
$ cd ../b6
$ printf -- '- Coffee: 2.00\n' >> menu.md
$ git commit -q -am "Coffee"
$ git push origin main 2>&1 | grep -E '^ ! \[rejected\]|^error'
 ! [rejected]        main -> main (fetch first)
error: failed to push some refs to '/home/learner/hub.git'
$ cd ..
```

*Recorded in Bash; `ch78-trouble/expected-handbook.bash.txt`.*

**Meaning.** The remote has commits that you do not have, so Git refuses to overwrite them.

**Cause.** Someone else pushed first (the recording plays two clones).

**Diagnose.** `git fetch` then `git log --oneline main..origin/main` shows what you are missing.

**Safe fix.** `git pull --no-rebase` (a merge) or `git pull --rebase` after reading the difference (Chapters 23<!--ref:remotes--> and 27<!--ref:rebase-->), resolve conflicts, push again.

**Dangerous fix.** `git push --force`: it overwrites your colleague's commits. If you must, use `--force-with-lease` and only on your own branch.

**Prevention.** Pull before you start work and before you push; protect shared branches (Chapter 50<!--ref:protect-->). The exact wording ("fetch first" or "non-fast-forward") depends on the Git version.

---

## 78.8 fatal: refusing to merge unrelated histories

**Message.** `fatal: refusing to merge unrelated histories`

**Recording.**

```text
$ echo "== E7: unrelated histories"
== E7: unrelated histories
$ git init -q solo && cd solo
$ printf 'x\n' > x.txt && git add x.txt && git commit -q -m "Solo"
$ git remote add origin ../hub.git
$ git fetch -q origin
$ git merge origin/main 2>&1 | grep -E '^fatal'
fatal: refusing to merge unrelated histories
$ cd ..
```

*Recorded in Bash; `ch78-trouble/expected-handbook.bash.txt`.*

**Meaning.** The two histories have no common ancestor, so Git will not guess how to join them.

**Cause.** You made a repository with `git init` and added a remote that has its own first commit (or two projects that were created separately).

**Diagnose.** `git log --oneline --all --graph` shows two separate roots.

**Safe fix.** If one side is only a scratch start, discard it and clone the remote instead; if both matter, decide which is the base and rebase or merge with `--allow-unrelated-histories` knowingly.

**Dangerous fix.** Adding `--allow-unrelated-histories` without looking: it can produce a confusing history with duplicate files.

**Prevention.** Clone an existing repository instead of `init` plus `remote add`; create the remote empty (Chapter 39<!--ref:ghrepo-->).

---

## 78.9 error: remote origin already exists

**Message.** `error: remote origin already exists / fatal: '../nowhere.git' does not appear to be a git repository`

**Recording.**

```text
$ echo "== E8: remote exists / bad remote"
== E8: remote exists / bad remote
$ git clone -q hub.git w8
$ cd w8
$ git remote add origin ../hub.git 2>&1 | grep -E '^error'
error: remote origin already exists.
$ git remote add backup ../nowhere.git
$ git fetch backup 2>&1 | grep -E '^fatal'
fatal: '../nowhere.git' does not appear to be a git repository
fatal: Could not read from remote repository.
$ cd ..
```

*Recorded in Bash; `ch78-trouble/expected-handbook.bash.txt`.*

**Meaning.** The first: you tried to add a remote name that is taken. The second: the address of the remote is wrong or unreachable.

**Cause.** You cloned (which already created `origin`), or you mistyped a path or URL.

**Diagnose.** `git remote -v` lists names and addresses.

**Safe fix.** Use another name, or `git remote set-url origin NEWURL`.

**Dangerous fix.** Deleting and re-adding remotes at random, which can leave you pushing to the wrong place.

**Prevention.** Check `git remote -v` before the first push (Chapter 23<!--ref:remotes-->).

---

## 78.10 fatal: a branch named 'idea' already exists

**Message.** `fatal: a branch named 'idea' already exists / error: the branch 'idea' is not fully merged`

**Recording.**

```text
$ echo "== E9: branch exists / not merged"
== E9: branch exists / not merged
$ git clone -q hub.git w9
$ cd w9
$ git switch -q -c idea
$ printf 'i\n' > idea.txt && git add idea.txt && git commit -q -m "Idea"
$ git switch -q main
$ git branch idea 2>&1 | grep -E '^fatal'
fatal: a branch named 'idea' already exists
$ git branch -d idea 2>&1 | grep -E '^error' | sed 's/[.]$//'
error: the branch 'idea' is not fully merged
$ cd ..
```

*Recorded in Bash; `ch78-trouble/expected-handbook.bash.txt`.*

**Meaning.** The first: the name is taken. The second: `-d` refuses to delete a branch that has commits nobody else has.

**Cause.** You reused a name; or the branch was never merged (or was squash-merged, which Git cannot see).

**Diagnose.** `git branch -vv` and `git log main..idea` show the unmerged commits.

**Safe fix.** Choose another name; merge the branch first, or confirm the work is elsewhere.

**Dangerous fix.** `git branch -D idea` without looking: the commits are then only reachable through the reflog for a while (Chapter 26<!--ref:reflog-->).

**Prevention.** Delete branches only after their pull request is merged (Chapter 20<!--ref:branching-->).

---

## 78.11 fatal: ambiguous argument 'x': unknown revision or path not in the working tree

**Message.** `fatal: ambiguous argument 'x': unknown revision or path not in the working tree`

**Recording.**

```text
$ echo "== E10: bad revision"
== E10: bad revision
$ git clone -q hub.git w10
$ cd w10
$ git log no-such-ref 2>&1 | grep -E '^fatal'
fatal: ambiguous argument 'no-such-ref': unknown revision or path not in the working tree.
$ git show HEAD~5 2>&1 | grep -E '^fatal'
fatal: ambiguous argument 'HEAD~5': unknown revision or path not in the working tree.
$ cd ..
```

*Recorded in Bash; `ch78-trouble/expected-handbook.bash.txt`.*

**Meaning.** Git cannot tell what `x` is: not a branch, tag, commit or file.

**Cause.** A typo, a branch that has not been fetched, or `HEAD~5` in a repository with fewer commits.

**Diagnose.** `git branch -a`, `git tag`, `git log --oneline` show what is available.

**Safe fix.** Correct the name; `git fetch`; use `--` before a file name to say that it is a file.

**Dangerous fix.** Passing a made-up hash, or guessing.

**Prevention.** Copy names from `git branch` or `git log`.

---

## 78.12 fatal: Unable to create '.git/index.lock': File exists

**Message.** `fatal: Unable to create '.git/index.lock': File exists`

**Recording.**

```text
$ echo "== E11: index.lock"
== E11: index.lock
$ git clone -q hub.git w11
$ cd w11
$ touch .git/index.lock
$ git add -A 2>&1 | head -1 | cut -c1-60
fatal: Unable to create '/home/learner/w1
$ rm .git/index.lock
$ git status -sb
## main...origin/main
$ cd ..
```

*Recorded in Bash; `ch78-trouble/expected-handbook.bash.txt`.*

**Meaning.** Git keeps a lock file while it changes the index; another Git process appears to be running, or crashed and left the file.

**Cause.** Another Git command (or an editor's Git integration) is running, or a previous command was killed.

**Diagnose.** Look for running Git processes first; then check whether the lock file is old.

**Safe fix.** Wait for the other process; if you are sure that none is running, delete `.git/index.lock` (the recording does).

**Dangerous fix.** Deleting the lock while a Git command is running, which can corrupt the index.

**Prevention.** Do not run two Git commands at once; let a crashed command finish or restart the computer.

---

## 78.13 A file is still tracked after you added it to .gitignore

**Message.** `A file is still tracked after you added it to .gitignore`

**Recording.**

```text
$ echo "== E12: gitignore not working"
== E12: gitignore not working
$ git clone -q hub.git w12
$ cd w12
$ printf 'secret\n' > notes.txt
$ git add notes.txt && git commit -q -m "Add notes"
$ printf 'notes.txt\n' > .gitignore
$ printf 'more\n' >> notes.txt
$ git status --short
 M notes.txt
?? .gitignore
$ git rm -q --cached notes.txt
$ git status --short
D  notes.txt
?? .gitignore
$ cd ..
```

*Recorded in Bash; `ch78-trouble/expected-handbook.bash.txt`.*

**Meaning.** `.gitignore` only affects files that Git does not yet track.

**Cause.** The file was committed before it was ignored.

**Diagnose.** `git ls-files FILE` prints the name if it is tracked.

**Safe fix.** `git rm --cached FILE` stops tracking it and keeps the file on disk; commit.

**Dangerous fix.** Deleting the file from disk with plain `git rm`, or forcing it in again with `git add -f`.

**Prevention.** Write `.gitignore` before the first `git add` (Chapter 18<!--ref:tracking-->). If the file held a secret, see Chapter 33<!--ref:gitsec-->.

---

## 78.14 HEAD detached at abc1234

**Message.** `HEAD detached at abc1234`

**Recording.**

```text
$ echo "== E13: detached HEAD"
== E13: detached HEAD
$ git clone -q hub.git w13
$ cd w13
$ git switch -q --detach HEAD
$ git branch --show-current | wc -c | tr -d ' '
0
$ git status | head -1
HEAD detached at bbc2826
$ git switch -q -c rescue
$ git branch --show-current
rescue
$ cd ..
```

*Recorded in Bash; `ch78-trouble/expected-handbook.bash.txt`.*

**Meaning.** You are looking at a commit, not at a branch, so new commits would belong to no branch.

**Cause.** You checked out a commit, a tag or a remote branch directly.

**Diagnose.** `git branch --show-current` prints nothing.

**Safe fix.** To keep work made here, `git switch -c NAME`; to leave, `git switch main`.

**Dangerous fix.** Making commits and then switching away without a branch: they become hard to find (Chapter 26<!--ref:reflog-->).

**Prevention.** Use `git switch -c NAME` when you want to work; use detached mode to look.

---

## 78.15 CONFLICT (content): Merge conflict in menu.md

**Message.** `CONFLICT (content): Merge conflict in menu.md / Automatic merge failed`

**Recording.**

```text
$ echo "== E14: merge conflict"
== E14: merge conflict
$ git clone -q hub.git p14
$ git clone -q hub.git q14
$ cd p14
$ sed -i 's/2.50/2.60/' menu.md
$ git commit -q -am "Price up"
$ git push -q origin main
$ cd ../q14
$ sed -i 's/2.50/2.70/' menu.md
$ git commit -q -am "Price different"
$ git -c advice.mergeConflict=false pull -q --no-rebase --no-edit 2>&1 | grep -E '^(CONFLICT|Automatic)'
CONFLICT (content): Merge conflict in menu.md
Automatic merge failed; fix conflicts and then commit the result.
$ git status --short
UU menu.md
$ git merge --abort
$ git status --short | wc -l | tr -d ' '
0
$ cd ..
```

*Recorded in Bash; `ch78-trouble/expected-handbook.bash.txt`.*

**Meaning.** Two changes touched the same lines and Git needs you to decide.

**Cause.** Two people changed the same place.

**Diagnose.** `git status` marks the file `UU`; the file contains `<<<<<<<`, `=======` and `>>>>>>>`.

**Safe fix.** Edit the file to the intended result, `git add`, `git commit`; or `git merge --abort` to go back (the recording does this and status is clean).

**Dangerous fix.** Keeping the markers, or choosing one side blindly with `--ours`/`--theirs` without reading the other.

**Prevention.** Small branches, frequent updates from `main`, talking to the other author (Chapter 22<!--ref:conflicts-->).

---

## 78.16 fatal: Need to specify how to reconcile divergent branches

**Message.** `fatal: Need to specify how to reconcile divergent branches`

**Recording.**

```text
$ echo "== E15: pull with diverged branches"
== E15: pull with diverged branches
$ git clone -q hub.git p15
$ git clone -q hub.git q15
$ cd p15
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -q -am "Tea"
$ git push -q origin main
$ cd ../q15
$ printf -- '- Coffee: 2.00\n' >> menu.md
$ git commit -q -am "Coffee"
$ git pull 2>&1 | grep -E '^fatal'
fatal: Need to specify how to reconcile divergent branches.
$ cd ..
```

*Recorded in Bash; `ch78-trouble/expected-handbook.bash.txt`.*

**Meaning.** Your branch and the remote's each have commits the other lacks, and Git will not choose merge or rebase for you.

**Cause.** You committed locally while others pushed, and no `pull.rebase` or `pull.ff` setting exists.

**Diagnose.** `git status` says the branches have diverged.

**Safe fix.** Choose: `git pull --no-rebase` (merge), `git pull --rebase`, or set `git config pull.rebase false` (or true) once (Chapter 23<!--ref:remotes-->).

**Dangerous fix.** Forcing your version over the remote's.

**Prevention.** Decide your default once and write it in your configuration.

---

## 78.17 Errors that could not be reproduced here

These need a network, an account or a service, so no recording exists. **Treat the causes below as common patterns, not as verified diagnoses.** Read the current GitHub documentation (Chapter 35<!--ref:readdocs-->) for the exact text on your system.

| What you see (approximately) | Usual cause | First safe step |
|---|---|---|
| `Permission denied (publickey)` | The SSH key is missing, not loaded or not registered with your account (Chapter 38<!--ref:ghauth-->) | `ssh -T` to the host shows whether the key is accepted; check the key is added to your account |
| `Authentication failed` over HTTPS | An expired, revoked or wrong token or password (Chapter 38<!--ref:ghauth-->); which credentials a host accepts is in its current documentation | Create a new token with the least scopes, or use a credential helper |
| `remote: Repository not found` or HTTP 403 or 404 | The address is wrong, the repository is private and you lack access, or you are signed in as another account | `git remote -v`; check that you are signed in as the right account |
| A push rejected because it contains a secret | Push protection found a credential (Chapter 62<!--ref:ghsec-->) | Remove the secret, and revoke it if it was ever exposed |
| A push rejected by branch protection | A rule needs a pull request or checks (Chapter 50<!--ref:protect-->) | Open a pull request |
| A file too large for the remote | The platform limits file size (see its current documentation) | Remove the file from the commit; consider Git LFS (Chapter 31<!--ref:bigrepos-->) |
| `fatal: unable to access ... Could not resolve host` | No network or a proxy problem | Check the connection; `ping` or the browser |
| Line-ending warnings | Windows and Linux line endings (Chapters 4<!--ref:text--> and 32<!--ref:custom-->) | Read the warning; set `core.autocrlf` or `.gitattributes` deliberately |

---

## Checkpoint

## What You Learned

- Read the first and last lines of an error, run `git status`, and do not accept the first fix you find.
- Every error has a safe fix and a dangerous fix; the dangerous one usually destroys work or overwrites others'.
- `-d` is safer than `-D`, `--force-with-lease` is safer than `--force`, and `stash` is safer than `checkout -f`.
- Some errors depend on the network or your account; look them up in the current documentation.

## New Vocabulary

No new terms.

## Commands Learned

No new commands; this chapter uses many earlier ones.

## Common Mistakes

1. **Forcing a push to make an error disappear.**
2. **Running `git init` where a repository already exists (or should).**
3. **Deleting `index.lock` while Git is running.**
4. **Believing that `.gitignore` removes a tracked file.**
5. **Copying a fix from a forum without reading it.**

## Practice

Do the exercises in [`exercises/ch78-exercises.md`](../../../exercises/ch78-exercises.md).

## Self-Test

1. What is the first command to run when you do not understand a state?
2. Which safe fix corresponds to the error "Your local changes would be overwritten"?
3. Why is `git branch -D` dangerous?
4. What does `git rm --cached` do?
5. Why does a push get rejected with "fetch first"?

## Before Moving On

You are ready for Chapter 79<!--ref:playbooks--> if you can:

- [ ] read an error message with the method of section 78.1
- [ ] name the dangerous fix for five of the errors

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The fifteen error messages, their triggers and the safe fixes shown | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on newer Git (hint lines are omitted because they vary) | R350 |
| The table of errors that could not be reproduced | Common patterns, **not verified** here | none |

## Where this leads

Chapter 79<!--ref:playbooks--> gives step-by-step recoveries for the worst cases: secrets, lost commits, bad merges, failed rebases and wrong branches.
