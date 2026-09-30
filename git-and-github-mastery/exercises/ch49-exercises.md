# Chapter 49 exercises — Collaboration and Access

Attempt each exercise before you open `solutions/ch49-solutions.md`. Exercises 1 to 3 need only your computer.

## Level 1 — Guided

**1.1 Roles.** List the five roles of an organisation repository from least to most access.

**1.2 A fork stand-in.** Create a bare repository `upstream.git` with one commit, and make `fork.git` with `git clone --bare upstream.git fork.git`. Clone the fork to `my-clone`. Run `git remote -v`.

## Level 2 — Partially guided

**2.1 Add the upstream.** In `my-clone`, add a remote `upstream` pointing to `../upstream.git`. Run `git remote -v` again.

**2.2 Catch up.** Add a commit to the upstream through a second clone. In `my-clone`, run `git fetch upstream`, then `git merge --ff-only upstream/main`, then `git push origin main`. Show `git log --oneline --graph --all`.

## Level 3 — Independent

**3.1 A drifted main.** Make a commit directly on `my-clone`'s `main`, and add a different commit to the upstream. Try `git merge --ff-only upstream/main`. What happens, and what does it teach?

**3.2 CODEOWNERS.** Write a `CODEOWNERS` file that makes `@example-owner` the owner of everything and `@ada` the owner of `menu.md`. Where may the file live, and which copy does a pull request use?

## Level 4 — Professional scenario

**4.1 Roles for a team.** A project has a maintainer, three regular developers, a designer who only comments and triages issues, and a visitor from another company who only reads. Assign a role to each and say why.

## Level 5 — Troubleshooting

**5.1** A maintainer says code owners are never requested on pull requests to the `release` branch, although they work for `main`. Give a likely reason.

**5.2** A team wants shared issue templates for all repositories of the organisation, but one repository already has its own `.github/ISSUE_TEMPLATE` folder with a template. What will that repository show?
