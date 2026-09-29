# Chapter 18 exercises — Tracking, Ignoring, Renaming, Deleting

Attempt each exercise before you open `solutions/ch18-solutions.md`. Use your `sunrise-bakery` project (or a copy). Use only made-up secrets.

## Level 1 — Guided

**1.1 Ignore three files.** Create `build.log`, `notes.tmp` and `.env` (the last containing `PAYMENT_API_KEY=FAKE_TOKEN_DO_NOT_USE_0000`). Write a `.gitignore` for them, then run `git status --short`, `git check-ignore -v build.log notes.tmp .env` and `git status --short --ignored`. Commit the `.gitignore`. *Expected result:* the three files are `!!`; the commit contains only `.gitignore`.

**1.2 Rename and delete.** With `git mv`, rename `menu.html` to `carte.html`; with `git rm`, delete `contact.html`; commit both in one commit. Then use `git log --oneline --stat -1` to read the result.

## Level 2 — Partially guided

**2.1 Test the patterns.** Reproduce the pattern test of section 18.4 in a scratch repository. Change `/todo.txt` to `todo.txt` and predict, then check, what changes for `docs/todo.txt`.

**2.2 Untrack a file.** Commit a file `scratch.txt`, add it to `.gitignore`, and show that Git still tracks it. Then untrack it with `git rm --cached` without deleting it from disk.

**2.3 A global rule.** Create your own global ignore file with `.DS_Store` and `*.swp`, and prove with `git check-ignore -v` that it applies in a new repository.

## Level 3 — Independent

**3.1** Write a `.gitignore` for a small web project that has an `assets/raw/` folder of large originals (ignore it), a `dist/` build folder, `*.log`, `.env`, and one file `assets/raw/logo-final.psd` that must be *kept* even though its folder is ignored. Test it with `git check-ignore -v` and explain any surprise. (Hint: read section 18.4 about exceptions and about ignored folders.)

## Level 4 — Professional scenario

**4.1** A new colleague's first commit contains a folder `node_modules/` with 30,000 files. Write a short plan: how to remove it from the repository going forward, what to put in `.gitignore`, how to tell the colleague, and what you would check before their next commit. (Chapter 31<!--ref:bigrepos--> will add tools for cleaning history; for now, plan only what this chapter allows.)

## Level 5 — Troubleshooting

**5.1** A learner added `secrets.txt` to `.gitignore` but `git status` still lists it as modified. Give the diagnosis, the command that proves it, and the fix.

**5.2** A learner committed `.env` containing a real API key, then deleted the file and committed again. They say the problem is solved. Explain why it is not, and list the first two things they must do, in order.

**5.3** `git check-ignore -v app.log` prints nothing, yet the learner is sure `*.log` is in `.gitignore`. Give three possible reasons.
