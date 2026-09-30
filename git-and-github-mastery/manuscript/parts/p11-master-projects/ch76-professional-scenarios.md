---
key: scenarios
number: 76
tag: Core
first_read: later
status: draft
requires: [pr, wfsec, releases, reflog]
ledger: [R348]
---
# Chapter 76 — Professional Scenarios 1-12 [Core]

**In this chapter**

- twelve situations you will meet at work, each solved step by step
- the safe way and the dangerous way for each
- a habit: read the state before and after every change

> **How to read this chapter.** Every scenario was **run and recorded** in Bash and zsh on Git 2.43.0 (and re-run in CI on newer Git). The "remote" is a local bare repository standing in for GitHub, and the "colleague" or "maintainer" is a second clone; on GitHub, the steps that a person clicks (a merge, a review) are described in words, from the earlier chapters. **Nothing here ran on GitHub.** Commit names shown in the outputs are stable only because the recordings use fixed dates; on your computer they will differ. All names and prices are made up; the API key in scenario 8 is a made-up value.

**Before you start.** Chapters 45<!--ref:pr-->, 60<!--ref:wfsec-->, 66<!--ref:releases--> and 26<!--ref:reflog-->, and Part III and IV of the book.

**How each scenario is laid out.** *Situation*, *Goal*, the recorded *Steps*, *What happened* (read the output line by line), and *If it goes wrong*.

---

## Scenario 1. Fix a bug on a branch and get it merged

**Situation.** The menu lists rolls at the wrong price. You have no permission to change `main` directly; the team merges through pull requests (Chapter 45<!--ref:pr-->).

**Goal.** Make the fix on a topic branch, publish it, and see it merged and cleaned up.

**Steps.**

```text
$ git clone -q hub.git work
$ cd work
$ git switch -q -c fix-roll-price
$ sed -i 's/Rolls: 3.00/Rolls: 3.20/' menu.md
$ git commit -q -am "Correct the price of rolls"
$ git push -q -u origin fix-roll-price
$ git log --format=%s main..fix-roll-price
Correct the price of rolls
$ git clone -q ../hub.git ../maintainer
$ git -C ../maintainer -c user.name=Maintainer -c user.email=maintainer@example.org merge -q --no-ff -m "Merge fix-roll-price" origin/fix-roll-price
$ git -C ../maintainer push -q origin main
$ git fetch -q
$ git switch -q main
$ git merge -q --ff-only origin/main
$ git branch -d fix-roll-price
Deleted branch fix-roll-price (was cd06e61).
$ git push -q origin --delete fix-roll-price
$ git log --format=%s
Merge fix-roll-price
Correct the price of rolls
Add the menu
```

*Recorded in Bash; `ch76-scenarios/expected-sc-bugfix.bash.txt`.*

**What happened.** The first `git log` line proves the branch holds exactly one new commit. The second clone plays the maintainer's part: on GitHub the maintainer would click **Merge**, and this local merge with `--no-ff` records the same kind of merge commit (Chapter 21<!--ref:merging-->). Back on your side, `--ff-only` moves `main` forward without inventing a new commit, and `git branch -d` refuses to delete a branch that is not merged, which is why it is the safe deletion.

**If it goes wrong.** If `git branch -d` refuses, do not use `-D` at once: check that the work really is merged (`git log main..branch`). If the push is rejected, fetch and look before forcing anything (Chapter 23<!--ref:remotes-->).

---

## Scenario 2. Correct your own last commit before anyone has it

**Situation.** You committed with a typo in the message and a wrong value, and you have not pushed.

**Goal.** Rewrite the last commit safely, then push.

**Steps.**

```text
$ git clone -q hub.git work
$ cd work
$ sed -i 's/Rolls: 3.00/Rolls: 3.2/' menu.md
$ git commit -q -am "Corect the price of rolls"
$ git log -1 --format=%s
Corect the price of rolls
$ sed -i 's/Rolls: 3.2$/Rolls: 3.20/' menu.md
$ git commit -q --amend -a -m "Correct the price of rolls"
$ git log --format=%s
Correct the price of rolls
Add the menu
$ git push -q origin main
$ git status -sb
## main...origin/main
```

*Recorded in Bash; `ch76-scenarios/expected-sc-amend.bash.txt`.*

**What happened.** `--amend` replaced the last commit with a new one that has the corrected message and content. Because nothing was pushed, nobody else holds the old commit, so rewriting is safe (Chapter 25<!--ref:undo-->). After the push the status shows `main...origin/main` with no difference.

**If it goes wrong.** Never amend a commit that others already have: your rewritten commit and theirs would differ, and a forced push would disturb them (Chapter 27<!--ref:rebase-->).

---

## Scenario 3. Undo a bad change that is already on the shared branch

**Situation.** A wrong price was pushed to `main` and others have already fetched it.

**Goal.** Undo it in a way that keeps history honest and does not disturb anyone.

**Steps.**

```text
$ git clone -q hub.git work
$ cd work
$ sed -i 's/White loaf: 2.50/White loaf: 25.00/' menu.md
$ git commit -q -am "Change the loaf price"
$ git push -q origin main
$ git revert --no-edit HEAD
[main 2fc2497] Revert "Change the loaf price"
 Date: Mon Jan 5 09:13:00 2026 +0000
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git push -q origin main
$ git log --format=%s
Revert "Change the loaf price"
Change the loaf price
Add the menu
$ cat menu.md
# Sunrise Bakery menu

- White loaf: 2.50
- Rolls: 3.00
```

*Recorded in Bash; `ch76-scenarios/expected-sc-revert.bash.txt`.*

**What happened.** `git revert` made a **new commit** that undoes the earlier one, so the history reads: the change, then its reversal. The file is back to its old content, and the push is an ordinary one because history only grew (Chapter 25<!--ref:undo-->).

**If it goes wrong.** The dangerous alternative is to reset `main` and force-push, which rewrites what others already have. Use it only on your own private branches.

---

## Scenario 4. Get back a branch you deleted

**Situation.** You deleted a branch with `-D` and then realised it held your only copy of a commit.

**Goal.** Find the lost commit through the reflog and give it a branch again.

**Steps.**

```text
$ git clone -q hub.git work
$ cd work
$ git switch -q -c tea-idea
$ printf -- "- Tea: 1.50\n" >> menu.md
$ git commit -q -am "Add tea"
$ git switch -q main
$ git branch -D tea-idea
Deleted branch tea-idea (was 11bdfb7).
$ git branch
* main
$ sha=$(git reflog --format='%H %gs' | grep 'commit: Add tea' | awk '{print $1}')
$ git branch tea-idea "$sha"
$ git log -1 --format=%s tea-idea
Add tea
```

*Recorded in Bash; `ch76-scenarios/expected-sc-recover.bash.txt`.*

**What happened.** `git branch -D` removed the name, but the commit still existed, and the reflog (Chapter 26<!--ref:reflog-->) recorded it when it was made. The script looked up its full name by the message and created a new branch there. The last line proves the commit is back.

**If it goes wrong.** The reflog is local and expires (Chapter 26<!--ref:reflog-->): recover soon. If you never committed the work, the reflog cannot help.

---

## Scenario 5. Two people changed the same line

**Situation.** Ada and Ben each changed the price of rolls, differently. Ada pushed first.

**Goal.** Combine the two changes deliberately and publish the result.

**Steps.**

```text
$ git clone -q hub.git ada
$ git clone -q hub.git ben
$ cd ada
$ sed -i 's/Rolls: 3.00/Rolls: 3.20/' menu.md
$ git commit -q -am "Rolls cost 3.20"
$ git push -q origin main
$ cd ../ben
$ sed -i 's/Rolls: 3.00/Rolls: 3.50/' menu.md
$ git commit -q -am "Rolls cost 3.50"
$ git fetch -q
$ git -c advice.mergeConflict=false merge origin/main
Auto-merging menu.md
CONFLICT (content): Merge conflict in menu.md
Automatic merge failed; fix conflicts and then commit the result.
$ cat menu.md
# Sunrise Bakery menu

- White loaf: 2.50
<<<<<<< HEAD
- Rolls: 3.50
=======
- Rolls: 3.20
>>>>>>> origin/main
$ printf "# Sunrise Bakery menu\n\n- White loaf: 2.50\n- Rolls: 3.30\n" > menu.md
$ git add menu.md
$ git commit -q --no-edit
$ git log --format=%s
Merge remote-tracking branch 'origin/main'
Rolls cost 3.50
Rolls cost 3.20
Add the menu
$ git push -q origin main
```

*Recorded in Bash; `ch76-scenarios/expected-sc-conflict.bash.txt`.*

**What happened.** Ben's `merge` stopped with a conflict and left markers in the file (Chapter 22<!--ref:conflicts-->). Ben decided on a value that suits both, wrote the file without markers, ran `git add` to say it was resolved, and committed; the merge commit records both parents. `advice.mergeConflict=false` only hides Git's hint text so that the output is the same on every version.

**If it goes wrong.** The most important step is the decision, not the commands: talk to the other author when the meaning is unclear. If you get lost, `git merge --abort` returns to the state before the merge.

---

## Scenario 6. Prepare a contribution for someone else's project

**Situation.** You want to add tea to a project's menu. The project's guide asks for a passing check and a sign-off (Chapter 64<!--ref:oss-->).

**Goal.** Branch, change, check, sign off and publish the branch, ready for a pull request.

**Steps.**

```text
$ git clone -q hub.git fork
$ cd fork
$ git switch -q -c add-tea
$ printf -- "- Tea: 1.50\n" >> menu.md
$ sh check.sh
check: ok
$ git commit -q -s -am "Add tea to the menu"
$ git log -1 --format=%B
Add tea to the menu

Signed-off-by: Ada Learner <ada@example.org>

$ git push -q -u origin add-tea
$ git ls-remote --heads origin
b5895b45037f31bbdf8262b45c73140c2d40747d	refs/heads/add-tea
75f410ae298df20e7637e6c4692195c081e54673	refs/heads/main
```

*Recorded in Bash; `ch76-scenarios/expected-sc-contribute.bash.txt`.*

**What happened.** The check script ran before the commit. `-s` added the `Signed-off-by` line (text, not a signature; Chapter 64<!--ref:oss-->). `git ls-remote` shows the two branches on the remote; the full names are commit hashes, which are the same on every machine because the recordings use fixed dates. On GitHub you would now open a pull request from `add-tea` (Chapter 45<!--ref:pr-->).

**If it goes wrong.** If the project asks for a different flow (for example a fork), follow its guide; the rule is always the same: small change, tests first, sign-off only if you have the right to submit.

---

## Scenario 7. Tidy messy commits before asking for review

**Situation.** Your branch has three commits called `WIP`, `more` and `fix typo`. Reviewers will read them.

**Goal.** Turn them into one meaningful commit, without an interactive editor.

**Steps.**

```text
$ git clone -q hub.git work
$ cd work
$ git switch -q -c menu-update
$ printf -- "- Tea: 1.50\n" >> menu.md
$ git commit -q -am "WIP"
$ printf -- "- Coffee: 2.00\n" >> menu.md
$ git commit -q -am "more"
$ printf -- "- Scone: 2.20\n" >> menu.md
$ git commit -q -am "fix typo"
$ git log --format=%s main..HEAD
fix typo
more
WIP
$ git reset -q --soft main
$ git commit -q -m "Add tea, coffee and scones to the menu"
$ git log --format=%s main..HEAD
Add tea, coffee and scones to the menu
```

*Recorded in Bash; `ch76-scenarios/expected-sc-squash.bash.txt`.*

**What happened.** `git reset --soft main` moved the branch pointer back to `main` while **keeping all the changes staged**, and one new commit replaced the three. This is the same result as squashing in an interactive rebase (Chapter 27<!--ref:rebase-->) with fewer moving parts.

**If it goes wrong.** Do this only on a branch that nobody else has fetched. If you pushed it, a forced push is needed and changes what others see: use `--force-with-lease` (Chapter 27<!--ref:rebase-->) and tell them.

---

## Scenario 8. A secret was committed by mistake

**Situation.** A file with an API key (a made-up one here) was committed. Nothing has been pushed.

**Goal.** Stop tracking the file, keep it out in future, and understand what remains.

**Steps.**

```text
$ git clone -q hub.git work
$ cd work
$ printf 'API_KEY=not-a-real-key\n' > .env
$ git add .env
$ git commit -q -m "Add configuration"
$ git rm -q --cached .env
$ printf '.env\n' > .gitignore
$ git add .gitignore
$ git commit -q -m "Stop tracking .env"
$ git ls-files
.gitignore
check.sh
menu.md
$ git log --format=%s -S'not-a-real-key'
Stop tracking .env
Add configuration
$ git show --format=%s HEAD~1:.env
API_KEY=not-a-real-key
```

*Recorded in Bash; `ch76-scenarios/expected-sc-secret.bash.txt`.*

**What happened.** The commands removed the file from tracking and added it to `.gitignore`. But the search (`-S`) still finds the key in **two commits**, and `git show` prints it from history. Removing a file in a later commit does not remove it from earlier ones (Chapter 33<!--ref:gitsec-->).

**If it goes wrong.** **Revoke the real key first**, before any clean-up: assume anyone who could see the repository has seen it. Only then rewrite history if you must (Chapter 33<!--ref:gitsec--> and Chapter 63<!--ref:secpractice-->), and remember that forks and clones keep the old commits.

---

## Scenario 9. Release a fix while new work is in progress

**Situation.** Version 1.0.0 is out, `main` already contains work for the next release, and a price bug must be fixed in the released version.

**Goal.** Fix it from the release tag, tag 1.0.1, and carry the fix to `main`.

**Steps.**

```text
$ git clone -q hub.git work
$ cd work
$ git tag -a v1.0.0 -m "Version 1.0.0"
$ printf "Specials for the next release\n" > specials.md
$ git add specials.md
$ git commit -q -m "Add specials (next release)"
$ git switch -q -c hotfix-1.0 v1.0.0
$ sed -i 's/Rolls: 3.00/Rolls: 3.20/' menu.md
$ git commit -q -am "Fix the price of rolls"
$ git tag -a v1.0.1 -m "Version 1.0.1"
$ git switch -q main
$ git cherry-pick -x hotfix-1.0 > /dev/null
$ git tag --sort=version:refname
v1.0.0
v1.0.1
$ git log --format=%s
Fix the price of rolls
Add specials (next release)
Add the menu
```

*Recorded in Bash; `ch76-scenarios/expected-sc-hotfix.bash.txt`.*

**What happened.** The hotfix branch started at the **tag**, so it holds none of the next release's work. After tagging `v1.0.1` the script copied the fix onto `main` with `cherry-pick -x` (Chapters 29<!--ref:tags--> and 27<!--ref:rebase-->), which records where the commit came from. The final log shows the fix and the specials on `main`, and the tags are sorted by version (Chapter 66<!--ref:releases-->).

**If it goes wrong.** If the cherry-pick conflicts, resolve it like a merge. Never move a published tag; publish a new patch version.

---

## Scenario 10. Find when a wrong value entered the file

**Situation.** Rolls cost 30.00 in the menu, and nobody knows since when.

**Goal.** Find the commit that added that text, and see what it changed.

**Steps.**

```text
$ git clone -q hub.git work
$ cd work
$ sed -i 's/Rolls: 3.00/Rolls: 30.00/' menu.md
$ git commit -q -am "Update rolls"
$ printf -- "- Tea: 1.50\n" >> menu.md
$ git commit -q -am "Add tea"
$ git log --format=%s -S'Rolls: 30.00'
Update rolls
$ git show --stat --format=%s HEAD~1
Update rolls

 menu.md | 2 +-
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git diff HEAD~2 HEAD~1
diff --git a/menu.md b/menu.md
index 9a3ace1..1509dce 100644
--- a/menu.md
+++ b/menu.md
@@ -1,4 +1,4 @@
 # Sunrise Bakery menu

 - White loaf: 2.50
-- Rolls: 3.00
+- Rolls: 30.00
```

*Recorded in Bash; `ch76-scenarios/expected-sc-pickaxe.bash.txt`.*

**What happened.** `git log -S'text'` lists the commits that changed how many times the text occurs, so the first result is where it appeared (Chapter 17<!--ref:history_view-->). `git show --stat` and `git diff` show the change. Bisect (Chapter 28<!--ref:tools-->) is the alternative when you can test each version automatically.

**If it goes wrong.** The search finds where text was added or removed, not why. Read the commit message and, on GitHub, the linked pull request.

---

## Scenario 11. Interrupted by an urgent fix

**Situation.** You are halfway through an edit when a colleague asks for a quick fix.

**Goal.** Put the half-done work aside, fix, and come back.

**Steps.**

```text
$ git clone -q hub.git work
$ cd work
$ printf -- "- Tea: 1.50\n" >> menu.md
$ git stash push -q -m "tea in progress"
$ git status --short
$ git switch -q -c fix-typo
$ sed -i 's/White loaf/White loaves/' menu.md
$ git commit -q -am "Fix the name of the loaf"
$ git switch -q main
$ git stash list | grep -c .
1
$ git stash pop -q
$ git status --short
 M menu.md
$ git log --format=%s --all
Fix the name of the loaf
Add the menu
```

*Recorded in Bash; `ch76-scenarios/expected-sc-stash.bash.txt`.*

**What happened.** `git stash push` saved the uncommitted change and cleaned the working tree (status printed nothing). After the fix on its own branch, `stash pop` brought the unfinished work back (Chapter 24<!--ref:stash-->).

**If it goes wrong.** A stash is local and easy to forget: give it a message, list it with `git stash list`, and do not leave work there for weeks.

---

## Scenario 12. Review a colleague's change on your own computer

**Situation.** A colleague pushed `add-tea`. You want to read and try it before approving.

**Goal.** Fetch the branch, read what changed, run the check, and go back.

**Steps.**

```text
$ git clone -q hub.git author
$ cd author
$ git switch -q -c add-tea
$ printf -- "- Tea: 1.50\n" >> menu.md
$ git commit -q -am "Add tea"
$ git push -q -u origin add-tea
$ cd ..
$ git clone -q hub.git reviewer
$ cd reviewer
$ git fetch -q origin
$ git log --format='%an: %s' main..origin/add-tea
Ada Learner: Add tea
$ git diff --stat main...origin/add-tea
 menu.md | 1 +
 1 file changed, 1 insertion(+)
$ git switch -q --detach origin/add-tea
$ sh check.sh
check: ok
$ tail -1 menu.md
- Tea: 1.50
$ git switch -q main
```

*Recorded in Bash; `ch76-scenarios/expected-sc-review.bash.txt`.*

**What happened.** Nothing was merged. `fetch` brought the branch, `log` and `diff --stat main...origin/add-tea` showed what it adds relative to `main` (the three dots compare from the common ancestor; Chapter 17<!--ref:history_view-->). `switch --detach` let you look at the branch without creating a local branch, and the check script ran on that version (Chapter 46<!--ref:review-->).

**If it goes wrong.** Do not run code from a stranger's branch that you have not read (Chapter 60<!--ref:wfsec-->). Write review comments on the pull request, not only in your head.

---

## Checkpoint

## What You Learned

- The safe tool depends on whether others already have the commit: amend, squash and reset for private work; revert for shared work.
- The reflog and pickaxe search find what seems lost or hidden.
- Conflicts need a decision, not just commands; `--abort` is available for as long as the merge or rebase is still in progress.
- A committed secret stays in history: revoke it first.
- Hotfixes start from the release tag, and fixes are carried across with `cherry-pick -x`.
- Reading the state (`status`, `log`, `diff`) before and after each step is the habit that prevents most mistakes.

## New Vocabulary

No new terms.

## Commands Learned

No new commands; this chapter combines the earlier ones.

## Common Mistakes

1. **Rewriting shared history** when a revert would do.
2. **Skipping the read-before-and-after habit.**
3. **Treating the removal of a secret from the latest commit as enough.**
4. **Moving a published tag** instead of releasing a new version.
5. **Running unread code from someone else's branch.**

## Practice

Do the exercises in [`exercises/ch76-exercises.md`](../../../exercises/ch76-exercises.md).

## Self-Test

1. Which scenarios use a forced push, and why do none of the recorded ones need it?
2. Why is `git revert` right for a shared bad commit?
3. Where does the recovery in scenario 4 get the commit's name from?
4. What does `--soft` keep when you reset?
5. Why start a hotfix from the tag?

## Before Moving On

You are ready for Chapter 77<!--ref:capstone--> if you can:

- [ ] choose amend, revert, squash or reset for a given situation
- [ ] recover a deleted branch
- [ ] explain what remains after removing a secret in a later commit

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| All twelve recorded sessions | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on newer Git | R348 |
| What a maintainer would do on GitHub (merge, review) | Described from earlier chapters; not run on GitHub | none |

## Where this leads

Chapter 77<!--ref:capstone--> joins these skills in one long simulation.
