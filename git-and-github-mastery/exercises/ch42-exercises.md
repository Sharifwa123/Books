# Chapter 42 exercises — Professional Repositories and READMEs

Attempt each exercise before you open `solutions/ch42-solutions.md`. Exercises 1 to 3 need only your computer.

## Level 1 — Guided

**1.1 Five questions.** Write down the five questions a README should answer.

**1.2 A first README.** In `bakery-menu`, create `README.md` with a title, a two-sentence description and headings "Use it" and "Who looks after it". Commit it.

## Level 2 — Partially guided

**2.1 A relative link.** Add `docs/CONTRIBUTING.md`, and link to it from the README with a relative link. Use `grep -o '](.*)' README.md` and `test -f` to check that the target exists.

**2.2 Break it.** Rename the target with `git mv`. Run your check again. What does `git status --short` say, and what does it not say?

## Level 3 — Independent

**3.1 A library README.** Write a README for a small library of your own with an install line and a minimal working example near the top.

**3.2 A link checker.** Write a shell loop that reads every `](...)` target in `README.md` that does not start with `http` and prints `missing: <target>` for each one that is not a file.

## Level 4 — Professional scenario

**4.1 A stranger's test.** Give your README to someone who has not seen the project. Ask them to say, after one minute, what it is and how to try it. Rewrite the opening until they can.

## Level 5 — Troubleshooting

**5.1** After a clean-up, every link in a project's README to `docs/setup.md` leads nowhere, although `git log` shows nothing wrong. Explain, and say how to find every affected link.

**5.2** A team added the topic `Internal-Billing-Tool-v2` to a public repository. Name two things that are wrong with it.
