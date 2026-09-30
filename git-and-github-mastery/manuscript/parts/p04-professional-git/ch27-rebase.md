---
key: rebase
number: 27
tag: Deep
first_read: later
status: draft
requires: [conflicts, reflog, remotes]
ledger: [R190, R191, R192]
---
# Chapter 27 — Rebase [Deep]

**In this chapter**

- what rebase does, and how it differs from merge
- `git rebase <branch>`: replay your commits on a new base
- rebase conflicts, and `--abort` and `--continue`
- `git rebase -i`: combining commits
- the golden rule: never rebase commits that others already have

> **Deep.** This chapter is marked **[Deep]**. You can skip it on a first read and return after Chapter 34<!--ref:workflows-->. Merge (Chapter 21<!--ref:merging-->) is enough to work with Git.

**Before you start.** Chapter 21<!--ref:merging-->, Chapter 22<!--ref:conflicts-->, Chapter 26<!--ref:reflog--> and Chapter 23<!--ref:remotes-->. The recordings use `bakery-menu` and were run in Bash and zsh on Git 2.43.0, then re-run in CI on Git 2.55.0.

---

## 27.1 The problem rebase solves

Chapter 21<!--ref:merging--> joined two diverged branches with a **merge commit**. That is honest, and it leaves a history with many small merges. Some teams prefer a **straight line**, where the work of a branch appears *after* the work that was already on `main`. **Rebase** does that.

> **New term: rebase.** Take the commits of one branch and replay them, one by one, on top of another commit. The replayed commits are **new commits**, with new hashes.

---

## 27.2 Rebase a branch onto `main`

The same starting situation as the three-way merge: `main` got "Add opening hours", `add-tea` got "Add tea". They have diverged:

```text
$ git switch -c add-tea
Switched to a new branch 'add-tea'
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -am "Add tea"
[add-tea 73ad7ed] Add tea
 1 file changed, 1 insertion(+)
$ git switch main
Switched to branch 'main'
$ printf 'Open Monday to Saturday.\n' > hours.md
$ git add hours.md
$ git commit -m "Add opening hours"
[main 1e5eef8] Add opening hours
 1 file changed, 1 insertion(+)
 create mode 100644 hours.md
$ git log --oneline --all --graph
* 1e5eef8 (HEAD -> main) Add opening hours
| * 73ad7ed (add-tea) Add tea
|/
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch27-rebase/expected-rebase.bash.txt`.*

Now, standing on `add-tea`, rebase it onto `main`:

```text
$ git switch add-tea
Switched to branch 'add-tea'
$ git rebase main
Successfully rebased and updated refs/heads/add-tea.
```

*Recorded in Bash; `ch27-rebase/expected-rebase.bash.txt`.*

Read what happened. Git took the commit "Add tea", set it aside, moved to the tip of `main`, and applied it there again. The graph is now a straight line:

```text
$ git log --oneline --all --graph
* 2cc423d (HEAD -> add-tea) Add tea
* 1e5eef8 (main) Add opening hours
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch27-rebase/expected-rebase.bash.txt`.*

Look at the hash. Before: `73ad7ed Add tea`. After: `2cc423d Add tea`. **The commit was not moved; it was copied.** The content of the change is the same, but its parent is different, so it is a different commit, with a different hash. The old commit still exists (Chapter 26<!--ref:reflog-->), but no branch points to it.

Now `main` can absorb the branch with a plain fast-forward (Chapter 21<!--ref:merging-->):

```text
$ git switch main
Switched to branch 'main'
$ git merge add-tea
Updating 1e5eef8..2cc423d
Fast-forward
 menu.md | 1 +
 1 file changed, 1 insertion(+)
$ git log --oneline --graph
* 2cc423d (HEAD -> main, add-tea) Add tea
* 1e5eef8 Add opening hours
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch27-rebase/expected-rebase.bash.txt`.*

There is no merge commit: the history reads as if the tea had been added after the opening hours.

**Merge or rebase?** They produce the same *content*. Merge keeps the true shape of the work, including the fork; rebase gives a tidy line but *rewrites* the branch's commits. Chapter 34<!--ref:workflows--> compares the styles.

---

## 27.3 When rebase hits a conflict

Both branches changed the same line, as in Chapter 22<!--ref:conflicts-->:

```text
$ git switch -c raise-bread
Switched to a new branch 'raise-bread'
$ printf '# Sunrise Bakery menu\n\n- White loaf: 3.00\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n' > menu.md
$ git commit -am "Raise the white loaf to 3.00"
[raise-bread 73e14f7] Raise the white loaf to 3.00
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git switch main
Switched to branch 'main'
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.90\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n' > menu.md
$ git commit -am "Raise the white loaf to 2.90"
[main 4afeda6] Raise the white loaf to 2.90
 1 file changed, 1 insertion(+), 1 deletion(-)
$ git switch raise-bread
Switched to branch 'raise-bread'
```

*Recorded in Bash; `ch27-rebase/expected-rebase-conflict.bash.txt`.*

Rebase applies your commits **one at a time**, and each may conflict:

```text
$ git rebase main
Auto-merging menu.md
CONFLICT (content): Merge conflict in menu.md
error: could not apply 73e14f7... Raise the white loaf to 3.00
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply 73e14f7... Raise the white loaf to 3.00
```

*Recorded in Bash; `ch27-rebase/expected-rebase-conflict.bash.txt`.*

Git stops in the middle and says which commit it could not apply, and it lists the ways out. *(On newer Git versions, 2.55.0 was tested, the output has one more hint line about `advice.mergeConflict`, and the commit subject is shown with a `# ` before it, as in `Could not apply 73e14f7... # Raise the white loaf to 3.00`. The meaning is the same.)* Ask for the state:

```text
$ git status
interactive rebase in progress; onto 4afeda6
Last command done (1 command done):
   pick 73e14f7 Raise the white loaf to 3.00
No commands remaining.
You are currently rebasing branch 'raise-bread' on '4afeda6'.
  (fix conflicts and then run "git rebase --continue")
  (use "git rebase --skip" to skip this patch)
  (use "git rebase --abort" to check out the original branch)

Unmerged paths:
  (use "git restore --staged <file>..." to unstage)
  (use "git add <file>..." to mark resolution)
	both modified:   menu.md

no changes added to commit (use "git add" and/or "git commit -a")
$ git diff --name-only --diff-filter=U
menu.md
```

*Recorded in Bash; `ch27-rebase/expected-rebase-conflict.bash.txt`.*

Two details differ from a merge conflict. The status says `interactive rebase in progress` (even though this rebase was not interactive; the name is Git's), and it names the commit being replayed. And, confusingly, which side is which is **reversed**: the "current" side (`HEAD`) is `main` (the base you are rebasing onto), and the side being applied is *your* commit.

You can walk away:

```text
$ git rebase --abort
$ git status
On branch raise-bread
nothing to commit, working tree clean
$ git log --oneline --all --graph
```

*Recorded in Bash; `ch27-rebase/expected-rebase-conflict.bash.txt`.*

`git rebase --abort` puts the branch back as it was before you started:

```text
* 4afeda6 (main) Raise the white loaf to 2.90
| * 73e14f7 (HEAD -> raise-bread) Raise the white loaf to 3.00
|/
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch27-rebase/expected-rebase-conflict.bash.txt`.*

Or you can resolve it. Start again, and this time fix the file, stage it, and continue:

```text
$ git rebase main
Auto-merging menu.md
CONFLICT (content): Merge conflict in menu.md
error: could not apply 73e14f7... Raise the white loaf to 3.00
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply 73e14f7... Raise the white loaf to 3.00
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.95\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n' > menu.md
$ git add menu.md
$ git rebase --continue
```

*Recorded in Bash; `ch27-rebase/expected-rebase-conflict.bash.txt`.*

(`hint: Waiting for your editor to close the file...` appears because Git opens an editor for the commit message; the recording's editor closes at once. In your own terminal you would see your editor open, and you would save and close it.)

```text
hint: Waiting for your editor to close the file...
[detached HEAD 608311e] Raise the white loaf to 3.00
 1 file changed, 1 insertion(+), 1 deletion(-)
Successfully rebased and updated refs/heads/raise-bread.
$ git log --oneline --all --graph
* 608311e (HEAD -> raise-bread) Raise the white loaf to 3.00
* 4afeda6 (main) Raise the white loaf to 2.90
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch27-rebase/expected-rebase-conflict.bash.txt`.*

The result is a straight line again: "Raise the white loaf to 3.00" now sits on top of `main`, and its content is the resolution you chose (2.95).

**The rebase checklist for conflicts:**

1. Read `git status`.
2. Edit the file; remove the markers (Chapter 22<!--ref:conflicts-->).
3. `git add <file>`.
4. `git rebase --continue`.
5. Repeat for each commit that conflicts, or `git rebase --abort` to stop.

---

## 27.4 Interactive rebase: combining commits

`git rebase -i` (interactive) lets you edit a list of commits before they are replayed: keep, combine, reword, reorder or drop. A common use is to tidy several small commits into one before sharing them.

In a rebase, to **squash** a commit is to combine it into the one before it. (Chapter 21<!--ref:merging--> used the word for `git merge --squash`; the effect is similar, the mechanism different.)

Three small commits were made:

```text
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -am "Add tea"
[main 60cb0bb] Add tea
 1 file changed, 1 insertion(+)
$ printf -- '- Coffee: 2.00\n' >> menu.md
$ git commit -am "Add coffee"
[main bf6d066] Add coffee
 1 file changed, 1 insertion(+)
$ printf -- '- Juice: 2.20\n' >> menu.md
$ git commit -am "Add juice"
[main bde8e38] Add juice
 1 file changed, 1 insertion(+)
$ git log --oneline
bde8e38 (HEAD -> main) Add juice
bf6d066 Add coffee
60cb0bb Add tea
81f772e Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
```

*Recorded in Bash; `ch27-rebase/expected-squash.bash.txt`.*

Normally, `git rebase -i HEAD~3` opens your editor with a list such as `pick <hash> Add tea`, one line per commit. You change `pick` to `squash` on the lines that should be folded into the first. The recording cannot open an editor, so it does the same edit with a program (`sed`), through the variable `GIT_SEQUENCE_EDITOR`. In your own work you edit the list by hand.

```text
$ GIT_SEQUENCE_EDITOR="sed -i -e '2s/^pick/squash/' -e '3s/^pick/squash/'" git rebase -i HEAD~3
hint: Waiting for your editor to close the file...
hint: Waiting for your editor to close the file...
[detached HEAD 69d6e2b] Add tea
 Date: Mon Jan 5 09:09:00 2026 +0000
 1 file changed, 3 insertions(+)
Successfully rebased and updated refs/heads/main.
```

*Recorded in Bash; `ch27-rebase/expected-squash.bash.txt`.*

The recorded run changed the second and third lines from `pick` to `squash`. Git combined all three commits into one. It also gave you a chance to edit the combined message (the editor was closed at once here):

```text
$ git log --oneline
69d6e2b (HEAD -> main) Add tea
81f772e Add coconut cake
9f10b43 Raise the price of the white loaf
8a52ffe Add the menu
$ git log -1 --format=%B
Add tea

Add coffee

Add juice

```

*Recorded in Bash; `ch27-rebase/expected-squash.bash.txt`.*

```text
$ git show --stat --oneline HEAD
69d6e2b (HEAD -> main) Add tea
 menu.md | 3 +++
 1 file changed, 3 insertions(+)
```

*Recorded in Bash; `ch27-rebase/expected-squash.bash.txt`.*

The three commits are now one, and the message shows all three original messages.

### The other actions

The list of commands in the editor is longer than `pick` and `squash`. According to Git's documentation (checked against Git 2.56.0):

| Command | What it does |
|---|---|
| `pick` | use the commit as it is |
| `reword` | use the commit, but stop to let you edit its message |
| `edit` | stop after applying the commit, so that you can change the files or the message, amend, and continue |
| `squash` | fold the commit into the one before it, and combine the messages |
| `fixup` | fold the commit into the one before it, and **discard** its message |
| `drop` | remove the commit (or delete its line) |
| `break` | stop at this point, without applying a commit |

You can also **reorder** the commits by moving lines. The recordings below drive the todo list with `sed` (through `GIT_SEQUENCE_EDITOR`) instead of an editor, so that they can run unattended. Three small commits touch three different files: tea, coffee and juice:

```text
$ cd bakery-menu
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -qam "Add tea"
$ printf 'Coffee: 2.00\n' > coffee.md
$ git add coffee.md
$ git commit -qm "Add coffee"
$ printf 'Juice: 2.20\n' > juice.md
$ git add juice.md
$ git commit -qm "Add juice"
$ git log --oneline -3
b68f4e3 (HEAD -> main) Add juice
28638f5 Add coffee
60cb0bb Add tea
```

*Recorded in Bash; `ch27-rebase/expected-interactive-actions.bash.txt`.*

**Drop** the second commit (coffee): change `pick` to `drop` on line 2:

```text
$ GIT_SEQUENCE_EDITOR="sed -i '2s/^pick/drop/'" git rebase -i HEAD~3
hint: Waiting for your editor to close the file...
Successfully rebased and updated refs/heads/main.
$ git log --oneline -3
ecea039 (HEAD -> main) Add juice
60cb0bb Add tea
81f772e Add coconut cake
```

*Recorded in Bash; `ch27-rebase/expected-interactive-actions.bash.txt`.*

Coffee is gone from the history (and from the files). The other two commits were replayed with new hashes. **Reorder** the two that remain: move the first line to the end:

```text
$ GIT_SEQUENCE_EDITOR="sed -i '1{h;d};\$G'" git rebase -i HEAD~2
hint: Waiting for your editor to close the file...
Successfully rebased and updated refs/heads/main.
$ git log --oneline -3
f80220e (HEAD -> main) Add tea
41c5eb6 Add juice
81f772e Add coconut cake
```

*Recorded in Bash; `ch27-rebase/expected-interactive-actions.bash.txt`.*

Tea and juice have swapped places. **Reword** the oldest commit: the recording also gives Git a message-editing program through `GIT_EDITOR`, which replaces the message:

```text
$ GIT_SEQUENCE_EDITOR="sed -i '1s/^pick/reword/'" GIT_EDITOR="sed -i '1s/.*/Add juice to the drinks menu/'" git rebase -i HEAD~2
hint: Waiting for your editor to close the file...
hint: Waiting for your editor to close the file...
[detached HEAD 4cf07c0] Add juice to the drinks menu
 Date: Mon Jan 5 09:13:00 2026 +0000
 1 file changed, 1 insertion(+)
 create mode 100644 juice.md
Successfully rebased and updated refs/heads/main.
$ git log --oneline -3
bd7866c (HEAD -> main) Add tea
4cf07c0 Add juice to the drinks menu
81f772e Add coconut cake
```

*Recorded in Bash; `ch27-rebase/expected-interactive-actions.bash.txt`.*

The message changed, and, again, so did every hash from that commit onward.

> **⚠️ CAUTION.** Dropping a commit removes its *changes*, and later commits may depend on them. Here coffee and juice touched **different files**, so the drop was clean. When the later commits build on the dropped one, the replay **conflicts**. Three commits appended to the same file, and the middle one dropped:

```text
$ GIT_SEQUENCE_EDITOR="sed -i '2s/^pick/drop/'" git rebase -i HEAD~3
hint: Waiting for your editor to close the file...
Auto-merging menu.md
CONFLICT (content): Merge conflict in menu.md
error: could not apply bde8e38... Add juice
hint: Resolve all conflicts manually, mark them as resolved with
hint: "git add/rm <conflicted_files>", then run "git rebase --continue".
hint: You can instead skip this commit: run "git rebase --skip".
hint: To abort and get back to the state before "git rebase", run "git rebase --abort".
Could not apply bde8e38... Add juice
```

*Recorded in Bash; `ch27-rebase/expected-drop-conflict.bash.txt`.*

> **Your Git may word this differently.** Git 2.55.0 and 2.56.0 (recorded and re-run in CI) print one more hint line, `Disable this message with "git config set advice.mergeConflict false"`, and name the dropped commit as `# Add juice` in the `Could not apply` line. The meaning is the same.

```text
$ git status --short
UU menu.md
$ git rebase --abort
$ git log --oneline -3
bde8e38 (HEAD -> main) Add juice
bf6d066 Add coffee
60cb0bb Add tea
```

*Recorded in Bash; `ch27-rebase/expected-drop-conflict.bash.txt`.*

`git rebase --abort` (section 27.3) put everything back. The message is the conflict from Chapter 22<!--ref:conflicts-->: the juice commit expected the coffee line to be there.

The real editor flow (the list opens in your editor and you edit it by hand) is what these `sed` commands imitate; the commands in the list are the ones above.

---

## 27.5 The golden rule

Because rebase **replaces commits with new ones**, it is safe only for commits that nobody else has.

> **⚠️ CAUTION. Never rebase commits that you have already shared** (pushed to a place where others may have pulled them). Rebasing them creates *different* commits with the same content. Your colleagues still have the old ones; the two versions of history then have to be reconciled, and that is painful and easy to get wrong. Rebase your **own, local, unpublished** work. For shared work, use merge or `git revert` (Chapter 25<!--ref:undo-->).

A rebased branch that was already pushed can only be pushed again by **forcing** the push, which overwrites the remote's branch. Chapter 33<!--ref:gitsec--> returns to the dangers of forced pushes.

### Two safer companions: `git pull --rebase` and `--force-with-lease`

**`git pull --rebase`** does a `fetch` and then *rebases* your local commits on top of what arrived, instead of merging. It is the way to avoid the merge commit that Chapter 23<!--ref:remotes--> created when two people pushed at once. Alice pushes a commit; Bob, who has a local commit of his own, pulls with `--rebase` and then pushes:

```text
$ cd alice
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -qam "Add tea"
$ git push -q origin main
$ cd ../bob
$ printf 'Open Monday to Saturday.\n' > hours.md
$ git add hours.md
$ git commit -qm "Add opening hours"
```

*Recorded in Bash; `ch27-rebase/expected-pull-rebase.bash.txt`.*

```text
$ git pull --rebase
From /home/learner/hub
   81f772e..965e160  main       -> origin/main
Successfully rebased and updated refs/heads/main.
$ git log --oneline --graph
* 872b896 (HEAD -> main) Add opening hours
* 965e160 (origin/main, origin/HEAD) Add tea
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
$ git push origin main
To /home/learner/hub.git
   965e160..872b896  main -> main
```

*Recorded in Bash; `ch27-rebase/expected-pull-rebase.bash.txt`.*

The history stays a straight line, with Bob's commit on top and a new hash (`872b896`), and the push is now a plain fast-forward. This only rewrote Bob's **own, unpublished** commit, so the golden rule holds. (Git's `git pull` documentation lists `--rebase` and the settings `pull.rebase` and `branch.<name>.rebase` that make it the default.)

**`git push --force-with-lease`** is a forced push with a safety check. Suppose Alice has pushed a branch `topic` and then amends her commit. A plain push is refused, because the remote branch is not an ancestor of hers:

```text
$ cd alice
$ git switch -c topic
Switched to a new branch 'topic'
$ printf -- '- Tea: 1.50\n' >> menu.md
$ git commit -qam "Add tea"
$ git push -q -u origin topic
$ git commit -q --amend -m "Add tea to the menu"
$ git push origin topic
To /home/learner/hub.git
 ! [rejected]        topic -> topic (non-fast-forward)
error: failed to push some refs to '/home/learner/hub.git'
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

*Recorded in Bash; `ch27-rebase/expected-force-with-lease.bash.txt`.*

`--force-with-lease` says: "overwrite the remote branch, **but only if it is still where I last saw it**":

```text
$ git push --force-with-lease origin topic
To /home/learner/hub.git
 + cece341...19c0972 topic -> topic (forced update)
```

*Recorded in Bash; `ch27-rebase/expected-force-with-lease.bash.txt`.*

`+ cece341...19c0972 ... (forced update)` shows that the remote branch was replaced. Now let Bob add a commit to `topic` behind Alice's back, and let Alice amend again *without fetching*:

```text
$ cd ../bob
$ git fetch -q
$ git switch -q topic
$ printf -- '- Coffee: 2.00\n' >> menu.md
$ git commit -qam "Add coffee"
$ git push -q origin topic
$ cd ../alice
$ git commit -q --amend -m "Add tea, again"
$ git push --force-with-lease origin topic
To /home/learner/hub.git
 ! [rejected]        topic -> topic (stale info)
error: failed to push some refs to '/home/learner/hub.git'
```

*Recorded in Bash; `ch27-rebase/expected-force-with-lease.bash.txt`.*

The lease protects Bob: Alice's push is **rejected with `stale info`**, because the remote branch is no longer at the commit that her remote-tracking branch remembers. A plain `--force` would have destroyed Bob's commit. Git's documentation calls it "like taking a 'lease' on the ref without explicitly locking it".

> **⚠️ CAUTION.** The protection compares the remote branch with your *remote-tracking branch*. If you run `git fetch` first, that note is updated and the lease will be granted, even though it means overwriting the commit that you have just fetched. Fetch, **look** at what arrived, and only then decide to force. The documentation also states that the forms of the option other than `--force-with-lease=<ref>:<expected>` are "still experimental", so treat the plain form as a helpful check and not a guarantee.

If a rebase goes wrong and you have already finished it, the reflog (Chapter 26<!--ref:reflog-->) still holds the state from before: find the entry from before `rebase (start)` and reset to it.

---

## Checkpoint

## What You Learned

- Rebase replays a branch's commits on top of another commit, giving a straight history.
- The replayed commits are *new* commits with new hashes; the originals remain until they expire.
- A rebase can conflict once per commit; resolve, `git add`, `git rebase --continue`, or `git rebase --abort`.
- `git rebase -i` edits the list of commits; `squash` combines them.
- Never rebase commits that others already have.

## New Vocabulary

- **Rebase**: replay commits on top of another commit, producing new commits.

## Commands Learned

`git rebase <branch>`, `git rebase --abort`, `git rebase --continue`, `git rebase -i`.

## Common Mistakes

1. **Rebasing shared commits.**
2. **Confusing which side is which in a rebase conflict.**
3. **Forgetting `git rebase --continue` after resolving.**
4. **Being surprised that hashes change.**
5. **Rebasing with uncommitted work in the tree.**

## Practice

Do the exercises in [`exercises/ch27-exercises.md`](../../../exercises/ch27-exercises.md).

## Self-Test

1. What happens to the hash of a commit when it is rebased, and why?
2. Which branch do you stand on when you run `git rebase main` to bring `add-tea` up to date?
3. What are the three ways out of a rebase conflict?
4. What does `squash` do in an interactive rebase?
5. State the golden rule of rebase.

## Before Moving On

You are ready for Chapter 28<!--ref:tools--> if you can:

- [ ] rebase a local branch onto `main`
- [ ] abort a rebase and resolve one
- [ ] explain why rebasing shared commits is dangerous
- [ ] combine commits with a squash

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Rebase of a diverged branch, new hashes, fast-forward afterwards | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; CI on Git 2.55.0 | R190 |
| Rebase conflict, `--abort`, `--continue` | Locally tested (as above) | R190 |
| Interactive `squash`, `drop`, reorder and `reword` (todo list edited by a program), and the drop conflict | Locally tested (as above); the list of commands checked against the Git 2.56.0 documentation | R192 |
| `pull --rebase`, `--force-with-lease` (rejection with `stale info`) | Locally tested (as above); semantics checked against the `git pull` and `git push` documentation (Git 2.56.0) | R191 |

## Where this leads

Chapter 28<!--ref:tools--> adds cherry-pick, bisect and patches, which also copy commits. Chapter 34<!--ref:workflows--> compares merge-based and rebase-based team workflows, and Chapter 33<!--ref:gitsec--> returns to forced pushes.
