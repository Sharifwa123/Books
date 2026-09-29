# Chapter 23 exercises — Remotes

Attempt each exercise before you open `solutions/ch23-solutions.md`. Work in an empty folder, and use a bare repository as the shared remote.

## Level 1 — Guided

**1.1 Build the hub.** Create `shared/bakery.git` with `git init --bare`, then clone it as `alice`. Which warning does Git print, and why?

**1.2 Publish.** As Alice, commit a `menu.md` and run `git push -u origin main`. Run `git branch -vv` before and after. What changed?

## Level 2 — Partially guided

**2.1 Second clone.** Clone the hub as `bob`. Run `git log --oneline` and `git remote -v` in Bob's clone.

**2.2 Fetch, then pull.** As Alice, change a price and push. As Bob, run `git status`, then `git fetch`, then `git status` again, then `git pull`. Explain each of the three status messages.

## Level 3 — Independent

**3.1 A rejected push.** Make Alice and Bob each commit a different file. Push Alice's first. Push Bob's second. Record the exact rejection line.

**3.2 Recover.** Bring Bob's clone up to date without using `--force`, then push. Show the final graph.

## Level 4 — Professional scenario

**4.1 Add a backup remote.** Add a second bare repository `backup.git` as a remote called `backup`. Push `main` to it, then confirm with `git branch -r` that `backup/main` exists. Rename the remote to `mirror`, then remove it.

## Level 5 — Troubleshooting

**5.1** A learner says: "`git status` says I'm up to date, but my colleague pushed an hour ago." Explain, and give the command sequence that shows the truth.

**5.2** A learner runs `git pull` and gets `fatal: Need to specify how to reconcile divergent branches`. What does this mean, and what are three ways to proceed?

**5.3** A learner wants to get past a rejected push with `git push --force`. Explain what would be lost, and give the safe alternative.
