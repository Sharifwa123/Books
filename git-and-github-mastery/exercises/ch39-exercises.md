# Chapter 39 exercises — Your First GitHub Repository

Attempt each exercise before you open `solutions/ch39-solutions.md`. **Every exercise can be done with local bare repositories** (`git init --bare <name>.git`) in place of a hosting platform, and you may repeat them on a real platform if you have an account. Use `bakery-menu` (rebuild it from Chapter 17<!--ref:history_view--> if needed).

## Level 1 — Guided

**1.1 Route A.** Create a bare repository `new-repo.git`, clone it, add a `README.md`, commit and push with `-u`. What warning appears when you clone, and why?

**1.2 Check the link.** Run `git status -sb` and `git log --oneline`. What does `## main...origin/main` tell you?

## Level 2 — Partially guided

**2.1 Route B.** In `bakery-menu`, run `git branch -M main`, add another empty bare repository as `origin`, and push with `-u`. Use `git ls-remote --heads origin` to compare its hash with `git rev-parse main`.

**2.2 Why empty?** Explain in two sentences why the hosted repository should be empty in Route B.

## Level 3 — Independent

**3.1 Cause the rejection.** Make a bare repository that already contains a commit (clone it, commit a README, push, delete the clone). Then add it as `origin` of `bakery-menu` and push. Read the message.

**3.2 Resolve it.** Bring the remote's work in with `git pull --no-rebase --allow-unrelated-histories`. Draw the graph with `git log --oneline --graph` and push.

## Level 4 — Professional scenario

**4.1 Project 3.** Do Project 3 (section 39.7) with a local bare repository, then write three lines saying which steps were Git and which would be platform steps on a hosting service.

## Level 5 — Troubleshooting

**5.1** A learner ticked "add a README" and then tried to push an existing project. What message will they see, and what are two ways to proceed?

**5.2** A learner pushed, but the web page shows an old version. Give two possible reasons.

**5.3** A learner made a repository public and then noticed a file with a password in an early commit. What should they do first (Chapter 33<!--ref:gitsec-->)?
