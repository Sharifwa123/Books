# Chapter 19 exercises — Writing Good Commits

Attempt each exercise before you open `solutions/ch19-solutions.md`. Use your `bakery-menu` repository from Chapter 17<!--ref:history_view--> (or rebuild it), and never amend a commit you have shared.

## Level 1 — Guided

**1.1 Improve a message.** Change `menu.md` (add a lemon tart at 3.50), commit it with the message `stuff`, then fix the message with `git commit --amend -m "..."`. Show the log before and after, and note that the hash changed.

**1.2 A forgotten file.** Create `notes.txt`, stage it, and add it to the last commit with `git commit --amend --no-edit`. Use `git show --stat --oneline HEAD` to check that one commit now holds both files.

## Level 2 — Partially guided

**2.1 Two commits from one afternoon.** Change the price of rolls in `menu.md` and create a new file `hours.md`. Make two commits, one for each. Show them with `git log --oneline --stat -2`.

**2.2 Body text.** Make a commit with a subject and a body using two `-m` options. Show it with `git log -1`. What separates subject from body?

**2.3 Whose commit?** Make a commit that credits another (real, consenting, or fictional) person as author. Show both identities with `git log -1 --format=fuller`.

## Level 3 — Independent

**3.1** Rewrite these five messages so a colleague could tell what each commit did: `fix`, `wip`, `changes`, `update page`, `more stuff and also the css`. Invent plausible details about the Sunrise Bakery site, and say which of them should really be split into two commits.

## Level 4 — Professional scenario

**4.1** Your team's history contains `Merge fixes`, `stuff`, `asdf` and a commit that changes 40 files across four unrelated features. You are asked to propose commit guidelines for the team. Write a one-page proposal covering the subject, body, size of commits, when to amend, and what to review before committing. Say which parts are Git rules and which are conventions.

## Level 5 — Troubleshooting

**5.1** A learner amended a commit that they had already given to a colleague (Chapter 23<!--ref:remotes--> will show how). The colleague now has a commit that does not exist in the learner's history. Explain why, and what advice you would give.

**5.2** A learner ran `git commit --amend` and thinks they destroyed the original commit. Show them how to prove it still exists, and name the chapter that shows how to get it back.

**5.3** A learner used `git commit -a -m "Update prices"` and later discovered it also committed an unrelated experiment in another tracked file. What happened, and how would they avoid it?
