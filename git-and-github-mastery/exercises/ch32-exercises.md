# Chapter 32 exercises — Customising Git

Attempt each exercise before you open `solutions/ch32-solutions.md`. Use `bakery-menu` (rebuild it from Chapter 17<!--ref:history_view--> if needed). Use only made-up credentials, and remove any file you create for them.

## Level 1 — Guided

**1.1 An alias.** Define `alias.st` as `status --short` and use `git st`. Where is the alias stored?

**1.2 Explain it.** Run `git help st`. What does Git print?

## Level 2 — Partially guided

**2.1 A shell alias.** Define an alias that starts with `!` and prints a message. Run it.

**2.2 List them.** List all your aliases with `git config --get-regexp '^alias\.'`.

## Level 3 — Independent

**3.1 A hook.** Write a `pre-commit` hook that refuses a commit when `menu.md` contains `TODO`. Make it executable and test it. What exit status does it use, and what does the failed commit leave in the working folder?

**3.2 Skip it and clone it.** Commit with `--no-verify`. Then clone the repository and check whether the hook came with it.

## Level 4 — Professional scenario

**4.1 Line endings.** Add `.gitattributes` with `*.md text eol=lf`. Create a file with CRLF line endings, add it, and read `git ls-files --eol`. Explain each column.

**4.2 rerere.** Turn on `rerere`, cause a conflict, resolve it and commit. Undo the merge with `git reset --hard HEAD~1` and merge again. What does Git say, and why is the status still `UU`?

## Level 5 — Troubleshooting

**5.1** A team wants to *guarantee* that no commit contains `TODO`. Is a `pre-commit` hook enough? Why not?

**5.2** A colleague set `credential.helper store` and used a real token. What is the risk, and what should they do?

**5.3** A learner copied a `pre-commit` hook from a forum post and it runs on every commit. What is the risk?
