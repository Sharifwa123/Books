# Chapter 23 solutions

## Level 1
**1.1** `warning: You appear to have cloned an empty repository.` The hub has no commits yet.

**1.2** Before the push, `git branch -vv` shows `[origin/main: gone]` because the remote branch does not exist yet. After `push -u`, it shows `[origin/main]`, and `git status` says `Your branch is up to date with 'origin/main'`.

## Level 2
**2.1** Bob sees Alice's commit with `HEAD -> main, origin/main, origin/HEAD`, and the same remote address as Alice.

**2.2** Before the fetch: `up to date` (Git has not asked the remote). After the fetch: `behind 'origin/main' by 1 commit, and can be fast-forwarded`. After the pull: up to date, with a fast-forward merge.

## Level 3
**3.1** `! [rejected] main -> main (fetch first)`, followed by `error: failed to push some refs`.

**3.2** `git fetch`, `git pull --no-rebase --no-edit` (or `git pull` after choosing a strategy), then `git push`. The graph shows a merge commit with two parents.

## Level 4
**4.1** `git init --bare backup.git`, `git remote add backup ../backup.git`, `git push backup main`, `git branch -r` lists `backup/main`, `git remote rename backup mirror`, `git remote remove mirror`. Removing the remote also removes its remote-tracking branches.

## Level 5
**5.1** `git status` compares with the last fetched state and does not contact the remote. Run `git fetch`, then `git status`; it will report `behind`.

**5.2** The local and remote branches have diverged and Git will not choose for you. Three ways: `git pull --no-rebase` (merge), `git pull --rebase` (rebase, Chapter 27<!--ref:rebase-->), or `git pull --ff-only` (refuses unless a fast-forward is possible). A setting such as `pull.rebase false` makes the choice permanent.

**5.3** A forced push would make the remote branch match yours exactly, discarding the colleague's commit from the shared branch. The safe alternative is to fetch, integrate with a merge, and push normally.
