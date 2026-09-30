# Chapter 80 exercises — Advanced Challenges

The six challenges are in the chapter. These tasks extend them. Attempt each before you open `solutions/ch80-solutions.md`.

## Level 1 — Guided

**1.1 Explain your solution.** For challenge 1, write one sentence for each command you used, and say what the outer project actually stores about a submodule.

## Level 2 — Partially guided

**2.1 Extension 1: two submodules.** Extend challenge 1: add a second inner repository `theme` to `app`, update both to their newest commits, and make **one** commit in `app` that records both. Then say what a colleague must run after `git pull` to get the new inner versions.

## Level 3 — Independent

**3.1 Extension 2: keep two folders.** Extend challenge 2: produce a new repository that contains `site` and `tools`, each in its own folder, but not anything else you add to `mono` (create a third folder `notes` first to test it). Check the commit count.

## Level 4 — Professional scenario

**4.1 Turn the design into checks.** Take your workflow design from challenge 4 and write, for each of its seven parts, one automated check or one written rule that would let a reviewer see whether the team follows it.

## Level 5 — Troubleshooting

**5.1 Extension 3: a flaky test.** Extend challenge 5: make the test script fail **randomly** in one commit (for example, depending on the last digit of a number in the file). Explain why bisect can then give a wrong answer, and how you would make the test reliable.
