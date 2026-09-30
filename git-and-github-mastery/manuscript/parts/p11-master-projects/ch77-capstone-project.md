---
key: capstone
number: 77
tag: Core
first_read: later
status: draft
requires: [scenarios]
ledger: [R349]
---
# Chapter 77 — Capstone Project [Core]

**In this chapter**

- **Project 12**: a 23-step professional simulation, from an empty repository to a released, audited project
- every step recorded, and what to do on GitHub at each step
- a checklist to assess yourself

> **How to read this chapter.** This is the last project. It joins everything from Parts III to X. **The 23 steps were run and recorded** in Bash and zsh on Git 2.43.0 and are re-run in CI on newer Git. A local bare repository stands in for GitHub, and the "colleagues" are extra clones. **Nothing was run on GitHub**: the right-hand column of each step says what to do on GitHub, from the earlier chapters, and doing it needs your own account (gate D of the book's plan). Names and prices are made up; the token in step 21 is a made-up value. **The project has no licence, because that is the owner's decision** (Chapter 65<!--ref:licences-->); when you do this for real, choose one.

**Before you start.** Chapter 76<!--ref:scenarios--> and the chapters it links. Set aside two to three hours. Type the commands yourself, in a sandbox folder.

**How to use the recording.** Read a step, run its commands in your sandbox, compare your output with the recording (commit names will differ), then do the GitHub column if you have an account.

---

## Step 1. Create the shared repository and your clone

Step 1 creates the shared repository and your working copy. Here a bare repository stands in for GitHub.

```text
$ echo "== Step 1: Create the shared repository and your clone"
== Step 1: Create the shared repository and your clone
$ git init -q --bare hub.git
$ git -C hub.git symbolic-ref HEAD refs/heads/main
$ git clone -q hub.git bakery 2>/dev/null
$ cd bakery
$ git status -sb
## No commits yet on main...origin/main [gone]
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: create an empty repository (Chapter 39<!--ref:ghrepo-->) and clone it; do not let the website add files yet, so that your first push is simple.


## Step 2. First files, tests and the ignore file

Files, tests and an ignore file. The tests ran and printed `OK`; generated files are ignored (Chapter 67<!--ref:ossproject-->).

```text
$ echo "== Step 2: First files, tests and the ignore file"
== Step 2: First files, tests and the ignore file
$ mkdir -p src tests
$ printf 'def total(prices):\n    return round(sum(prices), 2)\n' > src/orders.py
$ printf 'import unittest\nfrom orders import total\n\n\nclass TotalTest(unittest.TestCase):\n    def test_total(self):\n        self.assertEqual(total([2.5, 3.0]), 5.5)\n\n    def test_empty(self):\n        self.assertEqual(total([]), 0)\n' > tests/test_orders.py
$ printf '__pycache__/\n.env\n' > .gitignore
$ PYTHONPATH=src python3 -m unittest discover -s tests 2>&1 | grep -x OK
OK
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** Nothing to do on GitHub yet.


## Step 3. Documentation and community files

A README with an example that is true, `CONTRIBUTING.md` and `SECURITY.md` (Chapters 42<!--ref:readme-->, 64<!--ref:oss-->, 62<!--ref:ghsec-->).

```text
$ echo "== Step 3: Documentation and community files"
== Step 3: Documentation and community files
$ printf '# Bakery orders\n\nAdds up the prices of an order.\n\n    from orders import total\n    total([2.5, 3.0])  # 5.5\n' > README.md
$ printf '# Contributing\n\nOpen an issue first. Run sh ci.sh before you open a pull request.\n' > CONTRIBUTING.md
$ printf '# Security policy\n\nReport vulnerabilities privately to security@example.org.\n' > SECURITY.md
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** Later, check the repository's community profile.


## Step 4. A local pipeline you can run anywhere

A **pipeline you can run anywhere**: `ci.sh` runs the tests and checks that the required files exist. It reports honestly that no `LICENSE` exists: **the licence is the owner's decision** (Chapter 65<!--ref:licences-->), and this book adds none.

```text
$ echo "== Step 4: A local pipeline you can run anywhere"
== Step 4: A local pipeline you can run anywhere
$ printf 'PYTHONPATH=src python3 -m unittest discover -s tests >/dev/null 2>&1 && echo "tests: ok" || { echo "tests: FAILED"; exit 1; }\nfor f in README.md CONTRIBUTING.md SECURITY.md .gitignore; do test -f "$f" && echo "present: $f" || { echo "MISSING: $f"; exit 1; }; done\ntest -f LICENSE && echo "present: LICENSE" || echo "note: no LICENSE yet (the owner decides)"\n' > ci.sh
$ sh ci.sh
tests: ok
present: README.md
present: CONTRIBUTING.md
present: SECURITY.md
present: .gitignore
note: no LICENSE yet (the owner decides)
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub the same script becomes a workflow step (Chapters 52<!--ref:cicd--> and 56<!--ref:workflows_practice-->); pin actions to commits and set minimal permissions (Chapter 60<!--ref:wfsec-->).


## Step 5. First commit and push

The first commit and push. `status -sb` shows `main` and its remote in step.

```text
$ echo "== Step 5: First commit and push"
== Step 5: First commit and push
$ git add -A
$ git commit -q -m "Add the order total, tests, documentation and a local pipeline"
$ git push -q -u origin main
$ git status -sb
## main...origin/main
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: look at the commit list and the files.


## Step 6. A server rule that protects the shared branch

A **server rule** that refuses history rewrites on the shared repository. It stands in for branch protection.

```text
$ echo "== Step 6: A server rule that protects the shared branch"
== Step 6: A server rule that protects the shared branch
$ git -C ../hub.git config receive.denyNonFastForwards true
$ git -C ../hub.git config --get receive.denyNonFastForwards
true
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: configure a branch protection rule or ruleset (Chapter 50<!--ref:protect-->): require a pull request, require the checks, block force pushes.


## Step 7. A feature branch and a test that fails first

A feature branch, and a **test that fails first**. `FAILED` here is the point: the test proves the feature is missing.

```text
$ echo "== Step 7: A feature branch and a test that fails first"
== Step 7: A feature branch and a test that fails first
$ git switch -q -c feature/discount
$ printf '\n    def test_discount(self):\n        self.assertEqual(total([10, 10], 0.1), 18.0)\n' >> tests/test_orders.py
$ PYTHONPATH=src python3 -m unittest discover -s tests 2>&1 | grep -E "^(OK|FAILED)"
FAILED (errors=1)
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** Nothing to do on GitHub yet.


## Step 8. Make the test pass and commit

The smallest change that makes the test pass, run through the pipeline, committed and published.

```text
$ echo "== Step 8: Make the test pass and commit"
== Step 8: Make the test pass and commit
$ printf 'def total(prices, discount=0):\n    return round(sum(prices) * (1 - discount), 2)\n' > src/orders.py
$ sh ci.sh
tests: ok
present: README.md
present: CONTRIBUTING.md
present: SECURITY.md
present: .gitignore
note: no LICENSE yet (the owner decides)
$ git commit -q -am "Support a discount in total()"
$ git push -q -u origin feature/discount
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: open a pull request from the branch (Chapter 45<!--ref:pr-->); link the issue that asked for the feature (Chapter 44<!--ref:issues-->).


## Step 9. A colleague reviews the branch on their computer

A colleague's view: clone, read who changed what, read the diff statistics, run the pipeline on the branch (Chapter 46<!--ref:review-->).

```text
$ echo "== Step 9: A colleague reviews the branch on their computer"
== Step 9: A colleague reviews the branch on their computer
$ git clone -q ../hub.git ../reviewer
$ cd ../reviewer
$ git log --format='%an: %s' main..origin/feature/discount
Ada Learner: Support a discount in total()
$ git diff --stat main...origin/feature/discount
 src/orders.py        | 4 ++--
 tests/test_orders.py | 3 +++
 2 files changed, 5 insertions(+), 2 deletions(-)
$ git switch -q --detach origin/feature/discount
$ sh ci.sh
tests: ok
present: README.md
present: CONTRIBUTING.md
present: SECURITY.md
present: .gitignore
note: no LICENSE yet (the owner decides)
$ git switch -q main
$ cd ../bakery
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: the reviewer uses the Files changed tab and writes comments; the checks appear on the pull request.


## Step 10. Review feedback: add a follow-up commit

Feedback becomes a follow-up commit on the same branch; the pull request updates by itself.

```text
$ echo "== Step 10: Review feedback: add a follow-up commit"
== Step 10: Review feedback: add a follow-up commit
$ printf '\n    def test_no_discount(self):\n        self.assertEqual(total([10, 10], 0), 20.0)\n' >> tests/test_orders.py
$ git commit -q -am "Test the case without a discount"
$ git push -q origin feature/discount
$ git log --format=%s main..feature/discount
Test the case without a discount
Support a discount in total()
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: reply to each comment and resolve threads when addressed.


## Step 11. Meanwhile, main moved: a second developer changes the docs

Meanwhile `main` moved: a second developer changed the README.

```text
$ echo "== Step 11: Meanwhile, main moved: a second developer changes the docs"
== Step 11: Meanwhile, main moved: a second developer changes the docs
$ git clone -q ../hub.git ../ben
$ git -C ../ben switch -q main
$ printf 'See CONTRIBUTING.md to help.\n\n' | cat - ../ben/README.md > ../ben/README.new && mv ../ben/README.new ../ben/README.md
$ git -C ../ben commit -q -am "Point the README to the contributing guide"
$ git -C ../ben push -q origin main
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** This happens all the time.


## Step 12. Bring main into your branch and check again

You bring `main` into your branch, run the pipeline again and push. The merge went through without a conflict because the changes touched different places.

```text
$ echo "== Step 12: Bring main into your branch and check again"
== Step 12: Bring main into your branch and check again
$ git fetch -q
$ git merge -q --no-edit origin/main
$ sh ci.sh
tests: ok
present: README.md
present: CONTRIBUTING.md
present: SECURITY.md
present: .gitignore
note: no LICENSE yet (the owner decides)
$ git push -q origin feature/discount
$ git log --format=%s -4
Merge remote-tracking branch 'origin/main' into feature/discount
Point the README to the contributing guide
Test the case without a discount
Support a discount in total()
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub the pull request shows whether it can be merged; some teams prefer rebase, which Chapter 27<!--ref:rebase--> explains.


## Step 13. A conflict: both changed the same line

A real conflict: both changed the rounding line. You chose your version (`--ours`), marked it resolved and committed. In real work you would read both sides and talk to the other author (Chapter 22<!--ref:conflicts-->).

```text
$ echo "== Step 13: A conflict: both changed the same line"
== Step 13: A conflict: both changed the same line
$ printf 'def total(prices, discount=0):\n    return round(sum(prices) * (1 - discount), 2)  # rounds to cents\n' > ../ben/src/orders.py
$ git -C ../ben commit -q -am "Comment the rounding"
$ git -C ../ben push -q origin main
$ git fetch -q
$ sed -i 's/(1 - discount), 2)/(1 - discount), 2)  # cents/' src/orders.py
$ git commit -q -am "Comment the rounding differently"
$ git -c advice.mergeConflict=false merge origin/main
Auto-merging src/orders.py
CONFLICT (content): Merge conflict in src/orders.py
Automatic merge failed; fix conflicts and then commit the result.
$ git checkout -q --ours src/orders.py
$ git add src/orders.py
$ git commit -q --no-edit
$ sh ci.sh
tests: ok
present: README.md
present: CONTRIBUTING.md
present: SECURITY.md
present: .gitignore
note: no LICENSE yet (the owner decides)
$ git push -q origin feature/discount
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: the conflict editor or the local steps above.


## Step 14. Maintainer merges the pull request (squash)

The maintainer's **squash merge** puts all the branch's commits into one commit on `main` and deletes the remote branch (Chapter 45<!--ref:pr--> on strategies).

```text
$ echo "== Step 14: Maintainer merges the pull request (squash)"
== Step 14: Maintainer merges the pull request (squash)
$ git clone -q ../hub.git ../maintainer
$ cd ../maintainer
$ git -c user.name=Maintainer -c user.email=maintainer@example.org merge -q --squash origin/feature/discount
Squash commit -- not updating HEAD
$ git -c user.name=Maintainer -c user.email=maintainer@example.org commit -q -m "Add discount support (#1)"
$ git push -q origin main
$ git push -q origin --delete feature/discount
$ cd ../bakery
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: choose *Squash and merge* on the pull request, if the repository allows it.


## Step 15. Clean up and update your main

You update your `main` with `--ff-only`, prune deleted remote branches and delete your local branch. `-D` was needed because a squash merge leaves the branch's own commits unmerged in Git's eyes; check first that the work is in `main`.

```text
$ echo "== Step 15: Clean up and update your main"
== Step 15: Clean up and update your main
$ git switch -q main
$ git fetch -q --prune
$ git merge -q --ff-only origin/main
$ git branch -D feature/discount
Deleted branch feature/discount (was 14445d8).
$ git log --format=%s
Add discount support (#1)
Comment the rounding
Point the README to the contributing guide
Add the order total, tests, documentation and a local pipeline
$ sh ci.sh
tests: ok
present: README.md
present: CONTRIBUTING.md
present: SECURITY.md
present: .gitignore
note: no LICENSE yet (the owner decides)
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: use *Delete branch* if you did not already.


## Step 16. Tag the first release

The first release: an **annotated tag** on the merged commit, pushed (Chapter 66<!--ref:releases-->).

```text
$ echo "== Step 16: Tag the first release"
== Step 16: Tag the first release
$ git tag -a v0.1.0 -m "Version 0.1.0: initial development"
$ git push -q origin v0.1.0
$ git tag -n1
v0.1.0          Version 0.1.0: initial development
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: create a release from the tag with notes.


## Step 17. Package the release and publish a checksum

A source archive with a version prefix, and a **checksum** that is verified (Chapter 63<!--ref:secpractice-->). `sha256sum` is the Linux name.

```text
$ echo "== Step 17: Package the release and publish a checksum"
== Step 17: Package the release and publish a checksum
$ git archive --format=tar.gz --prefix=bakery-0.1.0/ -o ../bakery-0.1.0.tar.gz v0.1.0
$ tar -tzf ../bakery-0.1.0.tar.gz | head -4
bakery-0.1.0/
bakery-0.1.0/.gitignore
bakery-0.1.0/CONTRIBUTING.md
bakery-0.1.0/README.md
$ (cd .. && sha256sum bakery-0.1.0.tar.gz > bakery-0.1.0.tar.gz.sha256 && sha256sum -c bakery-0.1.0.tar.gz.sha256)
bakery-0.1.0.tar.gz: OK
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: attach the archive and the checksum to the release.


## Step 18. A bug report: discounts above 100 percent

A bug report becomes a **failing test** first.

```text
$ echo "== Step 18: A bug report: discounts above 100 percent"
== Step 18: A bug report: discounts above 100 percent
$ printf '\n    def test_bad_discount(self):\n        with self.assertRaises(ValueError):\n            total([10], 1.5)\n' >> tests/test_orders.py
$ PYTHONPATH=src python3 -m unittest discover -s tests 2>&1 | grep -E "^(OK|FAILED)"
FAILED (failures=1)
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: the issue links to the fix through the pull request.


## Step 19. Fix it and release 0.1.1

The fix, the pipeline, the commit, the tag `v0.1.1`. `git tag --sort=version:refname` lists tags by version.

```text
$ echo "== Step 19: Fix it and release 0.1.1"
== Step 19: Fix it and release 0.1.1
$ printf 'def total(prices, discount=0):\n    if not 0 <= discount <= 1:\n        raise ValueError("discount must be between 0 and 1")\n    return round(sum(prices) * (1 - discount), 2)\n' > src/orders.py
$ sh ci.sh
tests: ok
present: README.md
present: CONTRIBUTING.md
present: SECURITY.md
present: .gitignore
note: no LICENSE yet (the owner decides)
$ git commit -q -am "Reject discounts outside 0 to 1"
$ git push -q origin main
$ git tag -a v0.1.1 -m "Version 0.1.1"
$ git push -q origin v0.1.1
$ git tag --sort=version:refname
v0.1.0
v0.1.1
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: publish release 0.1.1 with a note about what it fixes.


## Step 20. A bad change reaches main, and you revert it

A bad change reaches `main`; the pipeline fails; you **revert** (Chapter 25<!--ref:undo-->), and the pipeline passes again. History shows both the mistake and its correction.

```text
$ echo "== Step 20: A bad change reaches main, and you revert it"
== Step 20: A bad change reaches main, and you revert it
$ printf 'def total(prices, discount=0):\n    return round(sum(prices))\n' > src/orders.py
$ git commit -q -am "Round to whole numbers"
$ git push -q origin main
$ sh ci.sh || true
tests: FAILED
$ git revert --no-edit HEAD > /dev/null
$ git push -q origin main
$ sh ci.sh
tests: ok
present: README.md
present: CONTRIBUTING.md
present: SECURITY.md
present: .gitignore
note: no LICENSE yet (the owner decides)
$ git log --format=%s -3
Revert "Round to whole numbers"
Round to whole numbers
Reject discounts outside 0 to 1
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: a required check would have blocked the merge in the first place.


## Step 21. A secret is committed by mistake

A secret is committed by mistake and caught **before the push**: the commits `Add local settings` and `Stop tracking .env` are still local (`ahead 2` at the end). The search shows that the secret remains in history. Because it never left your computer, you can still drop those two commits (Chapter 25<!--ref:undo--> on `reset`); had it been pushed, the first action would be to revoke the key (Chapter 33<!--ref:gitsec-->). Note that `git add -f` was needed because `.env` was ignored: **a forced add is a warning sign**.

```text
$ echo "== Step 21: A secret is committed by mistake"
== Step 21: A secret is committed by mistake
$ printf 'TOKEN=not-a-real-token\n' > .env
$ git add -f .env
$ git commit -q -m "Add local settings"
$ git rm -q --cached .env
$ git commit -q -m "Stop tracking .env"
$ git log --format=%s -S'not-a-real-token'
Stop tracking .env
Add local settings
$ git ls-files | grep -c '^.env$' || true
0
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: secret scanning and push protection (Chapter 62<!--ref:ghsec-->) act at this point.


## Step 22. Release notes from the history

**Release notes** from the history between two tags (Chapter 66<!--ref:releases-->).

```text
$ echo "== Step 22: Release notes from the history"
== Step 22: Release notes from the history
$ git log --format='- %s' v0.1.0..v0.1.1
- Reject discounts outside 0 to 1
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: generated notes list merged pull requests.


## Step 23. Final audit

**Final audit**: who committed, how many tags the remote holds (`--refs` hides the peeled duplicates), the branch status and the pipeline. Two commits are deliberately not pushed.

```text
$ echo "== Step 23: Final audit"
== Step 23: Final audit
$ git shortlog -sn --no-merges main
     8	Ada Learner
     1	Maintainer
$ git ls-remote --tags --refs origin | wc -l | tr -d ' '
2
$ git status -sb
## main...origin/main [ahead 2]
$ sh ci.sh
tests: ok
present: README.md
present: CONTRIBUTING.md
present: SECURITY.md
present: .gitignore
note: no LICENSE yet (the owner decides)
```

*Recorded in Bash; `ch77-capstone/expected-capstone.bash.txt`.*

**On GitHub.** On GitHub: check Insights and the Security tab (Chapters 51<!--ref:insights--> and 62<!--ref:ghsec-->).


---

## The self-assessment checklist

Tick each item honestly. An item you cannot show is a topic to revisit.

- [ ] I can create a repository, clone it, and explain `origin` (Chapters 23<!--ref:remotes-->, 39<!--ref:ghrepo-->).
- [ ] I wrote a test that failed first, then made it pass (step 7, 8).
- [ ] I wrote a README whose example is true (step 3).
- [ ] My pipeline runs locally with one command (step 4).
- [ ] I can explain what branch protection prevents (step 6, Chapter 50<!--ref:protect-->).
- [ ] I opened, reviewed and merged a change through a pull request, and I know the merge strategies (steps 8 to 15).
- [ ] I resolved a conflict by reading both sides (step 13).
- [ ] I tagged a release and can name what a checksum adds (steps 16 and 17).
- [ ] I turned a bug into a failing test and released a fix (steps 18 and 19).
- [ ] I undid a bad change on the shared branch without rewriting history (step 20).
- [ ] I know what remains after a secret is committed, and what to do first (step 21).
- [ ] I can produce release notes and audit a repository (steps 22 and 23).
- [ ] I have chosen (or decided to postpone) a licence, knowing it is my decision.

## What to add next

The simulation stops short of things you should try on GitHub: a real pull request with review comments, a workflow that runs `ci.sh` with pinned actions and minimal permissions, branch protection or a ruleset, Dependabot and secret scanning, a release with generated notes, and a `LICENSE` of your choice.

---

## Checkpoint

## What You Learned

- A professional workflow is a loop: test first, small branch, pipeline, review, merge, tag, release, monitor.
- Every step has a Git command and a GitHub counterpart; you can now do both.
- Mistakes are normal: revert on shared branches, catch secrets before pushing, and read the state before and after.

## New Vocabulary

No new terms.

## Commands Learned

No new commands.

## Common Mistakes

1. **Skipping the failing-test step** and trusting a test that never failed.
2. **Forcing a file into Git** that the ignore file excluded.
3. **Merging without the pipeline.**
4. **Pushing before looking at what you are about to push.**
5. **Assuming a licence is not needed.**

## Practice

Do the exercises in [`exercises/ch77-exercises.md`](../../../exercises/ch77-exercises.md).

## Self-Test

1. Why does step 7 want the test to fail?
2. What does the server rule of step 6 stop?
3. Why did step 14 leave the branch's own commits unmerged in Git's eyes?
4. Why is the secret of step 21 not yet a disaster?
5. What does `--refs` do in step 23?

## Before Moving On

You are ready for Chapter 78<!--ref:trouble--> if you can:

- [ ] repeat the simulation on a different idea
- [ ] explain each step to a beginner

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The 23 recorded steps | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0, Python 3; CI on newer Git | R349 |
| The GitHub column | From earlier chapters; not run on GitHub | none |

## Where this leads

Part XII is the troubleshooting handbook: Chapter 78<!--ref:trouble--> lists errors, their causes and safe fixes.
