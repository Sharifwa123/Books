# Chapter 17 solutions

## Level 1
**1.1** Your `git log --oneline` should list three commits, newest first.

**1.2** `git log`: full hash, author, date and message. `--oneline`: one line per commit. `--stat`: adds the files changed and how big. `-p -1`: adds the actual changes of the newest commit.

## Level 2
**2.1** Unstaged: `git diff` shows the change; `git diff --staged` shows nothing; `git diff HEAD` shows the change. After staging: `git diff` shows nothing; `git diff --staged` shows the change; `git diff HEAD` shows the change. The picture: `git diff` compares working tree and index; `--staged` compares index and last commit; `HEAD` compares working tree and last commit.

**2.2** `git rev-parse HEAD~1`, `git rev-parse HEAD^` and `git rev-parse <short-hash>` print the same 40-character hash.

## Level 3
Example: `git diff <first-hash> HEAD` shows the total difference; `git log --oneline <first-hash>..HEAD` lists the commits in between; `git show <hash>` shows each one.

## Level 4
**4.1** Find Monday's last commit with `git log --oneline` (and, if needed, the date shown by `git log`), then `git diff --stat <that-commit> HEAD` for a summary and `git diff <that-commit> HEAD` for the detail; `git log --oneline <that-commit>..HEAD` lists the commits since.

## Level 5
**5.1** After `git add`, the change is in the index and the working tree equals the index, so `git diff` (which compares them) is empty. `git diff --staged` shows the change.

**5.2** Git is showing the output through a pager, waiting for a key. Press `q` to quit (the space bar shows the next page).

**5.3** The first character of a diff line is the marker: `-` means removed, `+` means added, a space means unchanged. The rest is the line's own text: here the line is a Markdown list item that starts with `- White loaf`, so the line begins `-` (marker) then `- White loaf` (the text).
