# Chapter 52 exercises — CI/CD Concepts

Attempt each exercise before you open `solutions/ch52-solutions.md`. Exercises 1 to 4 need only your computer.

## Level 1 — Guided

**1.1 Definitions.** In one sentence each, say what continuous integration and continuous deployment are.

**1.2 Run a script.** In `bakery-menu`, write a script `ci.sh` that checks that `menu.md` has no tab characters, and prints `PASS`. Run it and show its exit code with `echo "exit code: $?"`.

## Level 2 — Partially guided

**2.1 Add a stage.** Add a test stage that fails when any line starting with `- ` has no price ending in two decimals. Make it fail on purpose, and show that the exit code is not 0.

**2.2 Stop early.** Add a build stage that writes `dist/menu.txt`. Show that after a failing test stage the build stage did not run and `dist` was not (re)made.

## Level 3 — Independent

**3.1 A fourth stage.** Add a lint rule of your own (for example, no line longer than 80 characters). Where in the order should it go, and why?

**3.2 Exit codes in a chain.** In your shell, run `false && echo yes` and `true && echo yes`. What does each print, and what does this teach about how a script decides to continue?

## Level 4 — Professional scenario

**4.1 A pipeline on paper.** For a small web project (HTML, CSS and a form), list the stages you would put in a pipeline, in order, with the check for each and what would count as a failure.

## Level 5 — Troubleshooting

**5.1** A team's checks take 50 minutes and developers have started merging without waiting. Name two changes from this chapter that would help.

**5.2** A check fails one run in five with no code change. What is this called, and why is it harmful?
