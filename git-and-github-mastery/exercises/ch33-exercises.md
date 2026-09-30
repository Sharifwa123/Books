# Chapter 33 exercises — Git Security

Attempt each exercise before you open `solutions/ch33-solutions.md`. **Use only made-up secrets, in a practice repository that you never push anywhere.** For Level 3 you need `git-filter-repo` (a separate program); for Level 4 you need GnuPG.

## Level 1 — Guided

**1.1 Leave a trace.** In a practice repository, commit a file `.env` containing `API_KEY=not-a-real-key`, then delete it and commit the deletion. Use `git show HEAD~1:.env` to read the key.

**1.2 Find it.** Use `git log --all --oneline -S"not-a-real-key"`. Which commits does it list, and why both?

## Level 2 — Partially guided

**2.1 Prevention.** Put `.env` in `.gitignore`, recreate the file, and run `git status --short` and `git check-ignore -v .env`. What do they show?

**2.2 The override.** Try `git add .env`, then `git add -f .env`. What is the difference? Why is this a weakness of `.gitignore`?

## Level 3 — Independent

**3.1 Rewrite.** In the practice repository from 1.1, run `git filter-repo --path .env --invert-paths --force`. What happened to the two commits and to the hashes?

**3.2 What did it not fix?** List three things that the rewrite did not undo, even if the repository had been shared.

## Level 4 — Professional scenario

**4.1 The order of steps.** A colleague has just pushed a real token to a shared repository. Put these steps in the right order and say why: rewrite history; tell the team; revoke the token; check the service's logs; add a prevention.

**4.2 Sign a commit.** Create a throw-away GPG key, configure `user.signingkey`, make one signed and one unsigned commit, and show them with `git log --format='%G? %s'`.

## Level 5 — Troubleshooting

**5.1** A learner says: "I deleted the file and pushed, so the secret is gone." Explain what is wrong, and what to do first.

**5.2** A learner rewrote a shared branch's history and force-pushed. A teammate now gets conflicts on every pull. Explain why, and what the teammate must not do.

**5.3** A learner sees `G` in `%G?` and concludes that the code is safe. What does the signature actually show?
