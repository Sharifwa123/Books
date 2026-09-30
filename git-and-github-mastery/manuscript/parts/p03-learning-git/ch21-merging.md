---
key: merging
number: 21
tag: Core
first_read: full
status: draft
requires: [branching]
ledger: [R173, R174, R175]
---
# Chapter 21 — Merging [Core]

**In this chapter**

- what merging means, and which branch you must be on
- the *fast-forward* merge, which is only a pointer moving
- the *three-way* merge, which creates a merge commit
- `--no-ff` and `--squash`, and what each does to the shape of history
- **Project 4**: work with branches on the Sunrise Bakery site

**Before you start.** Chapter 20<!--ref:branching--> (branches, switching, the graph view) and Chapter 17<!--ref:history_view--> (`git log`, `git diff`). The recordings use the `bakery-menu` repository.

Every recording was run in Bash and zsh on Git 2.43.0 and re-run in CI on Git 2.55.0.

---

## 21.1 What merging means

Chapter 20<!--ref:branching--> made lines of work. **Merging** brings them back together.

A **merge** combines the changes of one branch into another, so that the receiving branch contains the work of both. Earlier chapters used the word loosely; this chapter shows exactly what Git does.

Two things to fix in your mind before typing anything.

1. **The direction.** You merge *a branch* **into the branch you are on**. The command is `git merge <source>`, and it changes the **current** branch. The source branch is not changed. So to bring `add-tea` into `main`, you first `git switch main`, then run `git merge add-tea`.
2. **The situation decides the result.** Depending on how the two branches have moved, Git does one of two very different things: it either just moves a pointer (fast-forward), or it builds a new commit (a true merge).

---

## 21.2 Fast-forward: when nothing has diverged

Suppose `main` has not moved since you branched, and all the new work is on `add-tea`:

```text
$ cd bakery-menu
$ git switch -c add-tea
Switched to a new branch 'add-tea'
$ printf '# Sunrise Bakery menu\n\n- White loaf: 2.80\n- Rolls (six): 3.00\n- Coconut cake (slice): 4.00\n- Tea: 1.50\n' > menu.md
$ git commit -am "Add tea to the menu"
[add-tea a1ed54d] Add tea to the menu
 1 file changed, 1 insertion(+)
$ git switch main
Switched to branch 'main'
```

*Recorded in Bash; `ch21-merging/expected-ff.bash.txt`.*

The history is a straight line: `add-tea` is simply *ahead of* `main`:

```text
$ git log --oneline --all --graph
* a1ed54d (add-tea) Add tea to the menu
* 81f772e (HEAD -> main) Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch21-merging/expected-ff.bash.txt`.*

Now merge `add-tea` into `main`:

```text
$ git merge add-tea
Updating 81f772e..a1ed54d
Fast-forward
 menu.md | 1 +
 1 file changed, 1 insertion(+)
```

*Recorded in Bash; `ch21-merging/expected-ff.bash.txt`.*

Read the output. `Updating 81f772e..a1ed54d` names the two commits: where `main` was and where it will be. `Fast-forward` says what Git did: **it moved the branch pointer forward** along the existing line. No new commit was created; nothing needed combining, because `main` had nothing that `add-tea` did not already contain.

```text
$ git log --oneline --all --graph
* a1ed54d (HEAD -> main, add-tea) Add tea to the menu
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch21-merging/expected-ff.bash.txt`.*

Now `main` and `add-tea` point to the same commit (`HEAD -> main, add-tea`). Two commands confirm that the branch is finished with, and delete it:

```text
$ git branch --merged
  add-tea
* main
$ git branch -d add-tea
Deleted branch add-tea (was a1ed54d).
```

*Recorded in Bash; `ch21-merging/expected-ff.bash.txt`.*

`git branch --merged` lists the branches whose work is already contained in the current branch; `git branch -d add-tea` succeeded, where in Chapter 20<!--ref:branching--> it had refused, because the tea commit is now part of `main`.

> **New term: fast-forward.** A merge in which the receiving branch simply moves forward to the source branch's commit, because it has not diverged. No merge commit is created.

---

## 21.3 Diverged history: the three-way merge

Real projects rarely stay in a straight line. While tea was being added on `add-tea`, someone added the opening hours on `main`. Now **both** branches have commits that the other lacks: the histories have **diverged**.

> **New term: diverged.** Two branches have diverged when each has commits that the other does not have.

```text
$ printf 'Open Monday to Saturday.\n' > hours.md
$ git add hours.md
$ git commit -m "Add opening hours"
[main 1e5eef8] Add opening hours
 1 file changed, 1 insertion(+)
 create mode 100644 hours.md
```

*Recorded in Bash; `ch21-merging/expected-threeway.bash.txt`.*

```text
$ git log --oneline --all --graph
* 1e5eef8 (HEAD -> main) Add opening hours
| * a1ed54d (add-tea) Add tea to the menu
|/
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch21-merging/expected-threeway.bash.txt`.*

The graph shows the shape, with two lines splitting from `81f772e`: `main` went on to "Add opening hours" and `add-tea` went on to "Add tea to the menu". Git cannot fast-forward now, because moving `main` to `add-tea` would throw away the opening hours. It must **combine** the two.

```text
$ git merge --no-edit add-tea
Merge made by the 'ort' strategy.
 menu.md | 1 +
 1 file changed, 1 insertion(+)
```

*Recorded in Bash; `ch21-merging/expected-threeway.bash.txt`.*

Read the output. `Merge made by the 'ort' strategy.` says a merge commit was created. (*"ort"* is the name of Git's default algorithm for combining changes. The recordings show the name used by both versions tested here; older versions of Git used another name, and the name is not something you need to remember.) The summary shows the change that came in from `add-tea`.

The flag `--no-edit` matters here: **a merge commit needs a message**, and normally Git opens your editor with a suggested one (`Merge branch 'add-tea'`) for you to accept or change. `--no-edit` accepts the suggestion without opening the editor. It is used in the recordings only so that they run without an editor; in your own work you may simply save and close the editor.

The new history:

```text
$ git log --oneline --all --graph
*   94d0fc6 (HEAD -> main) Merge branch 'add-tea'
|\
| * a1ed54d (add-tea) Add tea to the menu
* | 1e5eef8 Add opening hours
|/
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch21-merging/expected-threeway.bash.txt`.*

The graph now **joins** two lines. The top commit, `94d0fc6 Merge branch 'add-tea'`, is a **merge commit**.

> **New term: merge commit.** A commit that has two (or more) parents. It records the point at which two lines of work were combined.

The two lines on the left of the graph are its two parents: `1e5eef8` (the `main` side) and `a1ed54d` (the `add-tea` side). Git worked out what to combine by looking at three commits: the two branch tips *and* their **common ancestor**, `81f772e`, the last commit they share. That is why this is called a **three-way merge**: it compares each tip with the shared starting point to see what each branch changed.

Two commands find merge commits:

```text
$ git show --stat --oneline HEAD
94d0fc6 (HEAD -> main) Merge branch 'add-tea'

 menu.md | 1 +
 1 file changed, 1 insertion(+)
$ git log --oneline --merges
94d0fc6 (HEAD -> main) Merge branch 'add-tea'
```

*Recorded in Bash; `ch21-merging/expected-threeway.bash.txt`.*

`git log --merges` lists only merge commits. `git show --stat --oneline HEAD` shows that the merge commit's summary lists the file that came in from the other branch.

---

## 21.4 `--no-ff`: keep the record of a branch

Sometimes a fast-forward *would* be possible, but you want a merge commit anyway, so that the history shows "these commits were a unit of work". That is the option `--no-ff` ("no fast-forward"):

```text
$ git switch main
Switched to branch 'main'
$ git merge --no-ff add-tea -m "Merge the hot drinks"
Merge made by the 'ort' strategy.
 menu.md | 2 ++
 1 file changed, 2 insertions(+)
```

*Recorded in Bash; `ch21-merging/expected-noff-squash.bash.txt`.*

`-m "Merge the hot drinks"` supplied the merge message. Here `add-tea` held two commits (tea and coffee). The graph:

```text
$ git log --oneline --graph
*   45e4d88 (HEAD -> main) Merge the hot drinks
|\
| * 0bbfb6b (add-tea) Add coffee to the menu
| * a1ed54d Add tea to the menu
|/
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch21-merging/expected-noff-squash.bash.txt`.*

The merge commit `45e4d88 Merge the hot drinks` groups the two commits of `add-tea` visibly. Without `--no-ff`, Git would have moved `main` forward and the two commits would have sat in a straight line with no sign that they were once a separate branch.

**Trade-off.** `--no-ff` preserves *where work came from*, at the cost of extra merge commits and a busier history. Straight-line history (fast-forward) is easier to read but forgets the branch. Teams pick one on purpose (Chapter 34<!--ref:workflows-->).

---

## 21.5 `--squash`: many commits become one

> **New term: squash.** To combine several commits into one.

A third option takes all the commits of a branch and turns their combined change into **one new commit** on the receiving branch, with no link to the original branch. Here `add-juice` has two commits (juice, lemonade) that create a new file, and they are squashed into `main`:

```text
$ git switch -c add-juice
Switched to a new branch 'add-juice'
$ printf 'Juice: 2.20\n' > cold-drinks.md
$ git add cold-drinks.md
$ git commit -m "Add juice"
[add-juice 8e389ad] Add juice
 1 file changed, 1 insertion(+)
 create mode 100644 cold-drinks.md
$ printf 'Juice: 2.20\nLemonade: 2.00\n' > cold-drinks.md
$ git commit -am "Add lemonade"
[add-juice 663bebc] Add lemonade
 1 file changed, 1 insertion(+)
```

*Recorded in Bash; `ch21-merging/expected-noff-squash.bash.txt`.*

Now switch back and squash:

```text
$ git switch main
Switched to branch 'main'
$ git merge --squash add-juice
Updating 45e4d88..663bebc
Fast-forward
Squash commit -- not updating HEAD
 cold-drinks.md | 2 ++
 1 file changed, 2 insertions(+)
 create mode 100644 cold-drinks.md
$ git status --short
A  cold-drinks.md
$ git commit -m "Add cold drinks"
[main 6178945] Add cold drinks
 1 file changed, 2 insertions(+)
 create mode 100644 cold-drinks.md
```

*Recorded in Bash; `ch21-merging/expected-noff-squash.bash.txt`.*

Read the output carefully:

- (The `Fast-forward` line here is Git describing the *staged change*, not a fast-forward of the branch.) `Squash commit -- not updating HEAD` says that `--squash` does **not** create the commit itself. It *stages* the combined change and stops.
- `git status --short` shows `A  cold-drinks.md`: the new file is staged.
- **You** then commit it: `git commit -m "Add cold drinks"` created one commit containing both changes.

```text
$ git log --oneline --graph
* 6178945 (HEAD -> main) Add cold drinks
*   45e4d88 Merge the hot drinks
|\
| * 0bbfb6b (add-tea) Add coffee to the menu
| * a1ed54d Add tea to the menu
|/
* 81f772e Add coconut cake
* 9f10b43 Raise the price of the white loaf
* 8a52ffe Add the menu
```

*Recorded in Bash; `ch21-merging/expected-noff-squash.bash.txt`.*

The graph shows one new commit at the top, `6178945 Add cold drinks`, and **no line joining it to the branch** `add-juice`. As far as Git's history is concerned, this is an ordinary commit.

That has a consequence:

```text
$ git branch -d add-juice
error: the branch 'add-juice' is not fully merged.
If you are sure you want to delete it, run 'git branch -D add-juice'
$ git branch -D add-juice
Deleted branch add-juice (was 663bebc).
```

*Recorded in Bash; `ch21-merging/expected-noff-squash.bash.txt`.*

`git branch -d add-juice` **refused**: Git does not see the branch's commits inside `main`, because the squash made a *new* commit with a different identity. The work *is* in `main`, but Git cannot prove it, so `-d` treats the branch as unmerged. You may then delete it with `-D` (after checking that you really did squash it).

*On the newer Git (2.55.0), the refusal message adds a `hint:` line, as in Chapter 20<!--ref:branching-->:*

```text
$ git branch -d add-juice
error: the branch 'add-juice' is not fully merged
hint: If you are sure you want to delete it, run 'git branch -D add-juice'
hint: Disable this message with "git config set advice.forceDeleteBranch false"
```

*Recorded in Bash; `ch21-merging/expected-noff-squash.bash.alt.txt`.*

**Trade-off.** `--squash` gives a clean, one-commit-per-feature history and hides messy work-in-progress commits. It also **discards** the individual commits and the record of the branch. This is one of the merge options that hosting platforms offer (Chapter 45<!--ref:pr-->).

---

## 21.6 Choosing

| Merge style | What happens | History shape | Use when |
|---|---|---|---|
| **Fast-forward** (automatic when possible) | Pointer moves | Straight line | The branch has not diverged; you want linear history |
| **Merge commit** (three-way; or `--no-ff`) | New commit with two parents | Lines split and join | You want to record that the work was a unit; branches have diverged |
| **Squash** | One new commit with the combined change | Straight line, no trace of the branch | The branch's small commits are noise; you want one entry per feature |

There is no universally best choice. The right one depends on what your team wants the history to say, and Chapter 34<!--ref:workflows--> returns to it. Whatever the style, the *content* of `main` afterwards is the same.

---

## 21.7 A merge checklist

1. **Commit or stash** your work (`git status` clean).
2. **Switch to the branch that should receive** the work: `git switch main`.
3. **Merge:** `git merge <branch>`.
4. **Read the output.** Did it fast-forward, make a merge commit, or report a conflict (Chapter 22<!--ref:conflicts-->)?
5. **Look at the result:** `git log --oneline --graph`.
6. **Delete the finished branch:** `git branch -d <branch>`.

> **Deep.** If a merge goes wrong, you can leave it with `git merge --abort` while it is unfinished, or undo a finished merge (Chapter 25<!--ref:undo-->). Do not panic and do not delete anything: the work is safe in the history.

---

## 21.8 Project 4: work with branches

> **Project 4.** *Goal:* use branches on the Sunrise Bakery site, and bring the work back into `main` in two different ways. *Time:* about 30 minutes. *You need:* the `sunrise-bakery` repository with its commits, and a clean `git status`.

1. Create a branch `add-cakes-page` and switch to it. Add a new file `cakes.html` (copy `menu.html` and change its heading to "Cakes"). Commit it.
2. Switch back to `main`. Check with `ls` that `cakes.html` is **not** there. Create a second branch, `update-hours`, and in it change the "six o'clock" text in `index.html` to "half past five". Commit it. Switch back to `main`.
3. Run `git log --oneline --all --graph`. You should see `main` and two branches each one commit ahead.
4. Merge `add-cakes-page` into `main`. Which kind of merge was it?
5. Merge `update-hours` into `main`. Which kind was it this time, and why is it different?
6. Look at the graph, and delete both branches with `git branch -d`.

*Expected result:* the first merge fast-forwards (`main` had not moved). After it, `main` has moved, so `update-hours` has diverged: the second merge creates a merge commit. The graph shows one merge. Both `-d` deletions succeed.

*Checkpoint questions:* Why did the second merge differ from the first? What would change if you had run `git merge --no-ff` for the first? What is the common ancestor for the second merge?

Chapter 22<!--ref:conflicts--> asks what happens when both branches change the *same line*.

---

## Checkpoint

## What You Learned

- Merging combines one branch into the branch you are on; the source is not changed.
- A **fast-forward** merge only moves a pointer; no merge commit.
- Diverged branches need a **three-way merge**, which compares each tip with the common ancestor and creates a **merge commit** with two parents.
- `--no-ff` forces a merge commit; `--squash` stages the combined change for one new commit and leaves no link to the branch.
- `git branch -d` refuses after a squash, because Git cannot see the branch's commits in the target.
- Choose a merge style by what you want history to say.

## New Vocabulary

- **Fast-forward**: a merge that only moves the receiving branch forward.
- **Diverged**: each of two branches has commits the other lacks.
- **Merge commit**: a commit with two or more parents.
- **Squash**: combining several commits into one.

## Commands Learned

`git merge <branch>`, `git merge --no-ff`, `git merge --squash`, `git merge --no-edit`, `git branch --merged`, `git log --merges`, `git log --oneline --graph`.

## Common Mistakes

1. **Merging in the wrong direction** (being on the wrong branch).
2. **Merging with uncommitted changes.**
3. **Expecting a squash merge to leave a link to the branch.**
4. **Deleting a branch with `-D` without checking that its work is in the target.**
5. **Being surprised by a merge commit** and not reading the output.

## Practice

Do the exercises in [`exercises/ch21-exercises.md`](../../../exercises/ch21-exercises.md), including Project 4 (section 21.8).

## Self-Test

1. You are on `main` and run `git merge add-tea`. Which branch changes?
2. What does `Fast-forward` in the output mean?
3. Why can the tea branch not be fast-forwarded in section 21.3?
4. What is a merge commit, and how many parents does it have?
5. What does `git merge --squash` leave for you to do?
6. Why did `git branch -d` refuse after the squash?

## Before Moving On

You are ready for Chapter 22<!--ref:conflicts--> if you can:

- [ ] perform a fast-forward merge and a three-way merge and tell them apart
- [ ] read a graph with a merge commit
- [ ] explain what `--no-ff` and `--squash` do
- [ ] delete a merged branch safely

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Fast-forward merge, `--merged`, `-d` afterwards | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0; identical on CI's Git 2.55.0 | R173 |
| Three-way merge, merge commit, `--merges`, the `ort` strategy line | Locally tested (as above); the strategy naming across versions not investigated | R174 |
| `--no-ff` and `--squash`, and the `-d` refusal after a squash | Locally tested (as above); the refusal hint differs between 2.43.0 and 2.55.0 (both recorded) | R175 |

## Where this leads

Chapter 22<!--ref:conflicts--> handles merges that cannot be completed automatically. Chapter 23<!--ref:remotes--> shows how merging and sharing fit together, and Chapter 27<!--ref:rebase--> shows another way to combine work. Chapter 45<!--ref:pr--> shows how a hosting platform offers these merge styles behind a button.
