---
key: conflicts
number: 22
tag: Core
first_read: full
status: draft
requires: [merging]
ledger: [R176, R177, R356]
---
# Chapter 22 — Merge Conflicts [Core]

**In this chapter**

- why Git sometimes cannot merge on its own
- how to read the markers Git writes into your file
- how to resolve a conflict by hand, and how to conclude the merge
- how to walk away with `git merge --abort`
- a clearer marker style, `diff3`
- **Project 6**: resolve a real conflict on the Sunrise Bakery site

**Before you start.** Chapter 21<!--ref:merging-->. The recordings use the `bakery-menu` repository and were run in Bash and zsh on Git 2.43.0 and re-run in CI on Git 2.55.0.

---

## 22.1 Why conflicts happen

In Chapter 21<!--ref:merging--> Git combined two branches by itself. It can do that when the branches changed **different** parts of the files. When both branches changed the **same lines** in different ways, Git cannot know which change you want. It does not guess. It stops and asks you.

> **New term: merge conflict.** A situation in which Git cannot combine two sets of changes automatically because both changed the same part of a file, or one changed what the other removed. A conflict is not an error in your work; it is Git asking a question only you can answer.

Here is the smallest example. The white loaf costs 2.80. On the branch `raise-bread` someone makes it 3.00:

```text
$ git switch -c raise-bread
Switched to a new branch 'raise-bread'
$ printf '# Sunrise Bakery menu\n\n- White loaf: 3.00\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n' > menu.md
$ git commit -am "Raise the white loaf to 3.00"
[raise-bread 73e14f7] Raise the white loaf to 3.00
 1 file changed, 1 insertion(+), 1 deletion(-)
```

*Recorded in Bash; `ch22-conflicts/expected-conflict.bash.txt`.*

Meanwhile, on `main`, someone else makes the same line 2.90:

```text
$ git switch main
Switched to branch 'main'
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.90\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n' > menu.md
$ git commit -am "Raise the white loaf to 2.90"
[main 4afeda6] Raise the white loaf to 2.90
 1 file changed, 1 insertion(+), 1 deletion(-)
```

*Recorded in Bash; `ch22-conflicts/expected-conflict.bash.txt`.*

Both commits changed the same line, starting from the same ancestor. Now merge:

```text
$ git merge raise-bread
Auto-merging menu.md
CONFLICT (content): Merge conflict in menu.md
Automatic merge failed; fix conflicts and then commit the result.
```

*Recorded in Bash; `ch22-conflicts/expected-conflict.bash.txt`.*

Read the three lines. `Auto-merging menu.md` says Git tried. `CONFLICT (content): Merge conflict in menu.md` names the problem and the file. `Automatic merge failed; fix conflicts and then commit the result.` says what you must do. The merge is now **half done**: Git stopped in the middle and is waiting.

> **⚠️ CAUTION.** A conflict does not lose anything. Both versions are safe in the history. Do not delete branches, do not run `git reset --hard` in a hurry, and do not close the terminal in fear. Read what Git says.

---

## 22.2 Ask Git what state you are in

```text
$ git status
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add <file>..." to mark resolution)
	both modified:   menu.md

no changes added to commit (use "git add" and/or "git commit -a")
```

*Recorded in Bash; `ch22-conflicts/expected-conflict.bash.txt`.*

`You have unmerged paths` means the merge is unfinished. The status gives you your two ways out: fix the conflicts and commit, or `git merge --abort`. The file `menu.md` is listed under **Unmerged paths** as `both modified`: both branches changed it.

To list only the conflicted files (useful when there are many):

```text
$ git diff --name-only --diff-filter=U
menu.md
```

*Recorded in Bash; `ch22-conflicts/expected-conflict.bash.txt`.*

---

## 22.3 Read the markers

Open the file. Git has written both versions into it:

```text
$ cat menu.md
# Sunrise Bakery menu

<<<<<<< HEAD
- White loaf: 2.90
=======
- White loaf: 3.00
>>>>>>> raise-bread
- Rolls (six): 3.00
- Coconut cake (slice): 4.00
```

*Recorded in Bash; `ch22-conflicts/expected-conflict.bash.txt`.*

> **New term: conflict markers.** The lines Git inserts into a file at a conflict: `<<<<<<<`, `=======` and `>>>>>>>`. They are not part of your content. They must all be removed before you finish.

Read it as three parts:

| Marker line | Meaning |
|---|---|
| `<<<<<<< HEAD` | Start. What follows is **your** side: the branch you are on (`main`) |
| `=======` | The divider between the two versions |
| `>>>>>>> raise-bread` | End. What came just before is the **other** side, from the branch you merged in |

Everything outside the markers (the heading, the rolls, the cake) was merged cleanly and needs nothing. Only the lines between `<<<<<<<` and `>>>>>>>` need your decision.

---

## 22.4 Resolve it

**Resolving** means editing the file until it holds exactly what you want, with **no markers left**. You have three choices: keep your side, keep theirs, or write something new. Here the two people agree to settle on 2.95, so the resolved file is:

```text
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.95\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n' > menu.md
```

*Recorded in Bash; `ch22-conflicts/expected-conflict.bash.txt`.*

The recording overwrote the file in one command; in real work you would open it in your editor, delete the three marker lines and the version you do not want, and adjust the rest by hand. Then tell Git you are done with that file by **staging** it:

```text
$ git add menu.md
$ git status
On branch main
All conflicts fixed but you are still merging.
  (use "git commit" to conclude merge)

Changes to be committed:
	modified:   menu.md

```

*Recorded in Bash; `ch22-conflicts/expected-conflict.bash.txt`.*

Git now says `All conflicts fixed but you are still merging`. Committing finishes the merge:

```text
$ git commit -m "Merge raise-bread, settling on 2.95"
[main cce1095] Merge raise-bread, settling on 2.95
$ git log --oneline --graph
*   cce1095 (HEAD -> main) Merge raise-bread, settling on 2.95
|\
| * 73e14f7 (raise-bread) Raise the white loaf to 3.00
* | 4afeda6 Raise the white loaf to 2.90
|/
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch22-conflicts/expected-conflict.bash.txt`.*

The graph is the same shape as a normal three-way merge (Chapter 21<!--ref:merging-->): two parents, one merge commit. The merge commit is where the conflict was settled, and it records your decision.

> **⚠️ CAUTION.** Git does not check that the markers are gone. If you stage a file that still contains `<<<<<<<`, Git will happily commit it, and your menu will contain junk lines. Before you `git add`, search the file for `<<<<<<<`, `=======` and `>>>>>>>`, and read it once as a reader would.

---

## 22.5 Changing your mind: `git merge --abort`

If the conflict is bigger than you expected, or you are not sure what you are doing, you can undo the *unfinished* merge and return to how things were before you typed `git merge`:

```text
$ git merge --abort
$ git status
On branch main
nothing to commit, working tree clean
```

*Recorded in Bash; `ch22-conflicts/expected-abort.bash.txt`.*

The working tree is clean. The file has your side's content again:

```text
$ cat menu.md
# Sunrise Bakery menu

- White loaf: 2.90
- Rolls (six): 3.00
- Coconut cake (slice): 4.00
```

*Recorded in Bash; `ch22-conflicts/expected-abort.bash.txt`.*

And the history is as before, with the two branches still diverged:

```text
$ git log --oneline --graph --all
* 4afeda6 (HEAD -> main) Raise the white loaf to 2.90
| * 73e14f7 (raise-bread) Raise the white loaf to 3.00
|/
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch22-conflicts/expected-abort.bash.txt`.*

Nothing was lost, and you can try the merge again later. `--abort` works only while the merge is unfinished. Once you have committed the merge, you must undo it another way (Chapter 25<!--ref:undo-->).

> **Checked against the documentation (R356).** The `git merge` manual (Git 2.56.0) says that `git merge --abort` "will abort the merge process and try to reconstruct the pre-merge state", but that if there were uncommitted changes when the merge started, and especially if they were changed further after it started, it "will in some cases be unable to reconstruct the original (pre-merge) changes". It warns that running `git merge` with non-trivial uncommitted changes "is discouraged", and recommends to "always commit or stash your changes before running `git merge`". (In a quick test here, an uncommitted edit to a *different* file did survive `--abort`; the manual's warning is the rule to follow.) The safe habit is the same: start every merge with a clean `git status`.

---

## 22.6 A clearer marker style: `diff3`

The default markers show two versions, and you must guess what the line said before. The setting `merge.conflictStyle` can change that. With `diff3`, Git also shows the **common ancestor**:

```text
$ git config merge.conflictStyle diff3
```

*Recorded in Bash; `ch22-conflicts/expected-diff3.bash.txt`.*

Repeat the same conflict:

```text
$ git merge raise-bread
Auto-merging menu.md
CONFLICT (content): Merge conflict in menu.md
Automatic merge failed; fix conflicts and then commit the result.
```

*Recorded in Bash; `ch22-conflicts/expected-diff3.bash.txt`.*

```text
$ cat menu.md
# Sunrise Bakery menu

<<<<<<< HEAD
- White loaf: 2.90
||||||| 81f772e
- White loaf: 2.80
=======
- White loaf: 3.00
>>>>>>> raise-bread
- Rolls (six): 3.00
- Coconut cake (slice): 4.00
```

*Recorded in Bash; `ch22-conflicts/expected-diff3.bash.txt`.*

There is a new section between `|||||||` and `=======`: the original line, `White loaf: 2.80`. Now you can see what each side changed: `main` went from 2.80 to 2.90; `raise-bread` went from 2.80 to 3.00. That often makes the decision obvious. The recording then aborts the merge:

```text
$ git merge --abort
```

*Recorded in Bash; `ch22-conflicts/expected-diff3.bash.txt`.*

> **Checked against the documentation (R177).** Git's `merge.conflictStyle` documentation (Git 2.56.0) says the default is `merge`, which shows the two sides; `diff3` "adds a `|||||||` marker and the original text before the `=======` marker"; and a third style, `zdiff3`, "is similar to `diff3` but removes matching lines on the two sides from the conflict region when those matching lines appear near either the beginning or the end of a conflict region". The documentation also says the `merge` style "tends to produce smaller conflict regions than diff3". A change of the default is not announced in Git 2.56.0's `BreakingChanges` document. This book recorded `merge` and `diff3`, not `zdiff3`.

Whichever style you choose, remember: the extra section is only for reading. You still delete all the marker lines.

---

## 22.7 Reducing the pain

- **Merge often.** Small, frequent merges make small conflicts.
- **Keep branches short.** The longer two branches live apart, the more they can collide.
- **Keep commits focused** (Chapter 19<!--ref:commits-->). A commit that changes one thing is easy to reason about when it conflicts.
- **Talk.** Two people editing the same line is often a coordination problem, not a Git problem.
- **Start from a clean tree** so `--abort` has an easy job.

Editors and dedicated merge tools can show the two sides next to each other. They change the *view*, not the process: you still end with a clean file, `git add`, and `git commit`.

---

## 22.8 A conflict checklist

1. **Stay calm.** Read the output and `git status`.
2. **Find the files:** `git diff --name-only --diff-filter=U`.
3. **Open each file** and find the markers.
4. **Decide** what the final content should be. Ask the other author if needed.
5. **Edit**: remove the markers and the unwanted lines.
6. **Check** that no `<<<<<<<`, `=======`, `>>>>>>>` remain.
7. **Stage** each resolved file: `git add <file>`.
8. **Commit** to finish the merge: `git commit`.
9. **Or abort**: `git merge --abort`, at any time before step 8.

---

## 22.9 Project 6: resolve a merge conflict

> **Project 6.** *Goal:* cause, read and resolve a real conflict on the Sunrise Bakery site, and practise leaving one. *Time:* about 30 minutes. *You need:* the `sunrise-bakery` repository with a few commits and a clean `git status`.

1. Create a branch `heading-warm` and change the first heading of `index.html` to "Warm bread, every morning". Commit. Switch back to `main`.
2. Create a branch `heading-fresh` and change the **same heading** to "Fresh bread, every morning". Commit. Switch back to `main`.
3. Merge `heading-warm` into `main` (a fast-forward). Then merge `heading-fresh`. Read what Git says.
4. Open `index.html`. Find the markers, and say which side is `HEAD`.
5. Run `git merge --abort`. Check with `git status` that everything is as before.
6. Merge again. This time write a heading that combines both ideas, remove all markers, `git add index.html`, and commit.
7. Show the graph with `git log --oneline --graph --all`.

*Expected result:* the first merge fast-forwards, the second stops with `CONFLICT (content)`, the abort restores the previous state, and the second attempt ends in a merge commit that holds your combined heading.

*Checkpoint questions:* Why did the first merge not conflict? How did you make sure that no marker was left in the file? What would have changed if you had used `git config merge.conflictStyle diff3` first?

---

## Checkpoint

## What You Learned

- A conflict arises when both branches change the same lines differently; Git stops rather than guessing.
- The merge is left unfinished, and `git status` says what to do.
- Markers show your side (`HEAD`), a divider, and the other side.
- You resolve by editing the file, staging it, and committing.
- `git merge --abort` returns you to before the merge.
- `merge.conflictStyle diff3` also shows the common ancestor.

## New Vocabulary

- **Merge conflict**: Git cannot combine changes automatically and asks you to decide.
- **Conflict markers**: the `<<<<<<<`, `=======` and `>>>>>>>` lines Git writes into a conflicted file.

## Commands Learned

`git merge --abort`, `git diff --name-only --diff-filter=U`, `git config merge.conflictStyle diff3`.

## Common Mistakes

1. **Committing with the markers still in the file.**
2. **Panicking and deleting the branch or running a destructive reset.**
3. **Keeping one side without reading the other.**
4. **Forgetting `git add` after editing**, so the file stays unmerged.
5. **Starting a merge with uncommitted work.**

## Practice

Do the exercises in [`exercises/ch22-exercises.md`](../../../exercises/ch22-exercises.md), including Project 6 (section 22.9).

## Self-Test

1. Why did Git stop in section 22.1 but not in Chapter 21<!--ref:merging-->?
2. What does `<<<<<<< HEAD` mark, and which branch is on that side?
3. What must be true of the file before you run `git add`?
4. How do you leave an unfinished merge?
5. What extra information does `diff3` add?

## Before Moving On

You are ready for Chapter 23<!--ref:remotes--> if you can:

- [ ] cause a conflict on purpose and read its markers
- [ ] resolve it and finish the merge
- [ ] abort a conflicted merge
- [ ] explain what `HEAD` means inside the markers

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Conflict output, status, markers, resolution and merge commit | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; identical on CI's Git 2.55.0. Some concept and option statements for this row were also checked in the Git 2.56.0 manual (git-merge); the ledger row says which. | R176 |
| `git merge --abort` may be unable to restore uncommitted changes present when the merge started | Officially verified (docs only): the `git merge` manual, Git 2.56.0 | R356 |
| `--abort` restores the pre-merge state; `diff3` shows the ancestor | Locally tested (as above); the three styles and the default checked in the `merge.conflictStyle` documentation; `zdiff3` not run | R177 |

## Where this leads

Chapter 23<!--ref:remotes--> moves work between repositories, where conflicts also appear when histories diverge. Chapter 27<!--ref:rebase--> shows conflicts in a different setting, and Chapter 45<!--ref:pr--> shows how a hosting platform reports them.
