# Chapter 24 exercises — Stash and Small Tools

Attempt each exercise before you open `solutions/ch24-solutions.md`. Use `bakery-menu` (rebuild it from Chapter 17<!--ref:history_view--> if needed).

## Level 1 — Guided

**1.1 Stash and pop.** Edit `menu.md` without committing. Run `git stash`, check `git status --short` and `git stash list`, then `git stash pop`.

**1.2 Tag a commit.** Create a lightweight tag `v0.1` and an annotated tag `v1.0`. Run `git log --oneline --decorate`.

## Level 2 — Partially guided

**2.1 Untracked files.** Create `ideas.txt`, then run `git stash`. Is `ideas.txt` still there? Repeat with `git stash -u`.

**2.2 Dry-run clean.** Create a scratch file and a scratch folder. Run `git clean -n`, then `git clean -n -d`. Explain the difference.

## Level 3 — Independent

**3.1 Search.** Use `git grep -n` to find the line with the rolls, then search an older commit for the price of the white loaf.

**3.2 Blame.** Use `git blame -s -L 3,3 menu.md` and then `git show` on the commit hash it prints. What did that commit change?

## Level 4 — Professional scenario

**4.1 Interrupted work.** You are halfway through a menu edit on `main`. A colleague asks for a fix on another branch. Show the commands that keep your edit safe, switch, and return, without making a commit for the unfinished edit.

## Level 5 — Troubleshooting

**5.1** A learner stashed work two days ago and cannot remember what it was. Which commands show the entry and its content?

**5.2** A learner ran `git clean -f` and lost an important untracked file. Can Git recover it? Why or why not?

**5.3** A learner deleted a tag with `git tag -d v1.0` and fears the release commit is gone. Is it?
