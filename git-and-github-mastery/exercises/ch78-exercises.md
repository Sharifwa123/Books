# Chapter 78 exercises — Troubleshooting Handbook

Attempt each exercise before you open `solutions/ch78-solutions.md`. Work in a sandbox with a local bare repository as the remote. **Do not try the dangerous fixes on a repository that matters.**

## Level 1 — Guided

**1.1 The method.** List the six steps of the method in section 78.1.

**1.2 Match.** Match each message to its meaning: (a) "not a git repository", (b) "Author identity unknown", (c) "refusing to merge unrelated histories", (d) "Unable to create index.lock".

## Level 2 — Partially guided

**2.1 Produce three.** Cause and record, in your sandbox, three errors of your choice from the handbook. Show the message and the safe fix.

**2.2 Rejected push.** With two clones of one bare repository, produce a rejected push and fix it with a merge. Then produce it again and fix it with a rebase. Compare the histories.

## Level 3 — Independent

**3.1 A new entry.** Find an error message that is not in the handbook (for example from a mistyped command), reproduce it, and write an entry with all seven fields.

**3.2 Dangerous or not.** For each command say whether it is safe, risky or destructive, and why: `git checkout -f`, `git stash`, `git push --force-with-lease`, `git branch -d`, `git clean -fd`.

## Level 4 — Professional scenario

**4.1 A colleague's message.** A colleague writes: "I got `failed to push some refs`, so I used `--force` and now Ana says her work is missing." Write the reply: what happened, how to recover Ana's commits (Chapter 26<!--ref:reflog-->) and how to prevent a repeat (Chapter 50<!--ref:protect-->).

## Level 5 — Troubleshooting

**5.1** `.gitignore` lists `notes.txt` but `git status` still shows changes to it. Explain and fix.

**5.2** `git status` says "HEAD detached at" and you have made two commits. How do you keep them?
