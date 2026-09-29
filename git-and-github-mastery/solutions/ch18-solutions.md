# Chapter 18 solutions

## Level 1
**1.1** `.gitignore` containing `*.log`, `*.tmp`, `.env`. `git status --short` shows `?? .gitignore`; with `--ignored` it also shows `!! .env`, `!! build.log`, `!! notes.tmp`.

**1.2** `git mv menu.html carte.html`, `git rm contact.html`, `git commit -m "Rename the menu page and remove the contact page"`. The stat shows a rename with 0 lines changed and a 27-line deletion.

## Level 2
**2.1** With `todo.txt` (no leading slash) the rule matches `todo.txt` in any folder, so `docs/todo.txt` becomes ignored too.

**2.2** `git add scratch.txt`, `git commit`, `printf 'scratch.txt\n' > .gitignore`; `git status --short` shows only `?? .gitignore` (still tracked). Then `git rm --cached scratch.txt` and commit; the file stays on disk and is now ignored.

**2.3** `git config --global core.excludesFile ~/.gitignore_global`, write the patterns into that file, create `.DS_Store` in a new repository, and `git check-ignore -v .DS_Store` shows the global file as the source.

## Level 3
**3.1** Example: `assets/raw/`, `dist/`, `*.log`, `.env`. An exception like `!assets/raw/logo-final.psd` does **not** work while the folder `assets/raw/` itself is ignored, because Git does not look inside an ignored folder (recorded in section 18.4.3). Fix: ignore the *contents* instead of the folder (`assets/raw/*` then `!assets/raw/logo-final.psd`). Test with `git check-ignore -v`.

## Level 4
**4.1** Add `node_modules/` to `.gitignore`; remove it from tracking with `git rm -r --cached node_modules` and commit; tell the colleague that dependencies are downloaded again from the project's list, not committed; before their next commit ask them to run `git status` and `git diff --staged`. Note that the files remain in earlier history (size), which Chapter 31<!--ref:bigrepos--> addresses.

## Level 5
**5.1** `secrets.txt` was already tracked, so ignoring has no effect. Proof: `git ls-files secrets.txt` prints the name. Fix: `git rm --cached secrets.txt`, commit; and if it holds a real secret, follow the incident steps (Chapter 33<!--ref:gitsec-->).

**5.2** The key is still in the earlier commit and readable with `git show <commit>:.env` or `git log -p`, and in every clone. First: treat the key as stolen and **revoke or replace it** immediately. Second: add `.env` to `.gitignore` (and check no other copy exists) before considering any cleaning of history (Chapter 33<!--ref:gitsec-->).

**5.3** (1) The pattern is in a different `.gitignore` (a subfolder or another repository); (2) it has a typo or trailing space; (3) a later `!` exception un-ignored the file; (4) the path does not match (for example `app.log` is inside a folder and the rule is anchored elsewhere); (5) the name is different in case.
