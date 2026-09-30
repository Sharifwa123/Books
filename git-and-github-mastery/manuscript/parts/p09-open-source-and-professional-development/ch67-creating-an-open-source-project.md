---
key: ossproject
number: 67
tag: Deep
first_read: later
status: draft
requires: [licences, readme, releases]
ledger: [R324]
---
# Chapter 67 — Creating an Open-Source Project [Deep]

**In this chapter**

- **Project 11**: create a small, documented open-source library
- project structure, documentation and community files
- choosing and stating a licence (your decision, not this book's)
- a first release and a maintenance routine

> **How to read this chapter.** This is a **Deep** chapter and can be read later. Everything about Git and the local layout was recorded in Bash and zsh (Git 2.43.0, Python 3) and re-run in CI. Statements about GitHub features refer to earlier chapters, which cite GitHub's documentation. **Nothing on GitHub was run for this chapter.** Chapter 65<!--ref:licences--> said that this book is not legal advice; **the project you create needs a licence chosen by you**, and this chapter deliberately contains no licence text.

**Before you start.** Chapter 65<!--ref:licences-->, Chapter 42<!--ref:readme--> and Chapter 66<!--ref:releases-->.

---

## 67.1 What "open-source project" asks of you

An open-source project is more than public code (Chapter 64<!--ref:oss-->). A visitor should be able to answer five questions in a minute:

1. **What is it?** (the README)
2. **May I use it?** (the licence)
3. **How do I try it?** (install and usage in the README)
4. **How do I help?** (`CONTRIBUTING.md`, code of conduct)
5. **What if I find a security problem?** (`SECURITY.md`)

GitHub's community profile checklist (Chapter 64<!--ref:oss-->) looks for the same files.

---

## 67.2 Project 11: a small library

> **Project 11.** *Goal:* publish a tiny library with tests, documentation, a licence you chose, community files and a first tagged release. *Time:* about 90 minutes. *You need:* Git, Python 3 (any current version; the example uses only its standard library), a GitHub account for the last steps.

The idea is deliberately small so that the project structure is the lesson. This chapter uses `wordcount`, a function that counts the words in a text. You may replace it with a small idea of your own; keep the same steps.

1. **Create the repository and folders.**
2. **Write the code and two tests**, and run them.
3. **Add a `.gitignore`.** Generated files must not enter the repository.
4. **Write the README** with a usage example that is correct.
5. **Add the community files.** Then check which are missing.
6. **Choose and add a licence.** See section 67.4.
7. **Commit and tag** the first version.
8. **Push, add a workflow, and create the release** (section 67.5).
9. **Check the result as a stranger would.**

The recording covers steps 1 to 5 and 7:

```text
$ git init -q wordcount && cd wordcount
$ mkdir -p src tests .github
$ printf 'def count_words(text):\n    """Return the number of words in text."""\n    return len(text.split())\n' > src/wordcount.py
$ printf 'import unittest\nfrom wordcount import count_words\n\n\nclass CountWordsTest(unittest.TestCase):\n    def test_empty(self):\n        self.assertEqual(count_words(""), 0)\n\n    def test_sentence(self):\n        self.assertEqual(count_words("one two  three"), 3)\n\n\nif __name__ == "__main__":\n    unittest.main()\n' > tests/test_wordcount.py
$ PYTHONPATH=src python3 -m unittest discover -s tests 2>&1 | grep -x OK
OK
```

*Recorded in Bash; `ch67-ossproject/expected-library.bash.txt`.*

The tests ran and printed `OK` (only that line is kept, because the full report contains the running time, which changes on every run). The code is tiny on purpose: `text.split()` splits on any run of spaces, so `"one two  three"` has three words.

Now the ignore file, the README and the community files:

```text
$ printf '__pycache__/\n' > .gitignore
$ printf '# wordcount\n\nCounts the words in a piece of text.\n\n    from wordcount import count_words\n    count_words("one two three")  # 3\n' > README.md
$ printf '# Contributing\n\nOpen an issue first. Run the tests before you send a pull request.\n' > CONTRIBUTING.md
$ printf '# Security policy\n\nReport vulnerabilities privately to security@example.org.\n' > SECURITY.md
```

*Recorded in Bash; `ch67-ossproject/expected-library.bash.txt`.*

Next, a small check script in the shell. It only tests whether each file is present, and it reports **honestly** that two are missing:

```text
$ for f in README.md LICENSE CONTRIBUTING.md CODE_OF_CONDUCT.md SECURITY.md; do test -f "$f" && echo "present: $f" || echo "MISSING: $f"; done
present: README.md
MISSING: LICENSE
present: CONTRIBUTING.md
MISSING: CODE_OF_CONDUCT.md
present: SECURITY.md
```

*Recorded in Bash; `ch67-ossproject/expected-library.bash.txt`.*

`LICENSE` and `CODE_OF_CONDUCT.md` are missing on purpose. **The recording does not create them, because a licence is your decision (Chapter 65<!--ref:licences-->) and a code of conduct is a promise you must be able to keep** (Chapter 64<!--ref:oss-->). The check is a habit: run something like it before every release.

Finally, the first commit, a tag, and the list of tracked files:

```text
$ git add -A && git commit -q -m "Add wordcount library, tests and community files"
$ git tag -a v0.1.0 -m "Version 0.1.0: initial development"
$ git tag -n1
v0.1.0          Version 0.1.0: initial development
$ git ls-files
.gitignore
CONTRIBUTING.md
README.md
SECURITY.md
src/wordcount.py
tests/test_wordcount.py
```

*Recorded in Bash; `ch67-ossproject/expected-library.bash.txt`.*

Two details deserve attention:

- `git ls-files` shows **no** `__pycache__` folder, because the `.gitignore` line kept it out. Without it, Python's generated files would be committed, and they depend on the Python version (a lesson from an earlier draft of this recording, in which the file name contained `cpython-311`).
- The tag is **annotated** and named `v0.1.0`: by Semantic Versioning (Chapter 66<!--ref:releases-->), major version zero "is for initial development" and its API "SHOULD NOT be considered stable". Starting at 0.1.0 is an honest promise.

---

## 67.3 Documentation that a stranger can follow

The README example must be **true**. The best habit is to make the README example a test, or to run it by hand before each release. A README that says `count_words("one two three")` returns 3 is a promise, and the recording's second test proves the same sentence works.

Documentation checklist for a first release:

- The **name** and one-sentence purpose.
- How to **install** (for this tiny library: copy `src/wordcount.py`, or the way your language's package manager works; do not claim an installation method you have not tried).
- One **usage example**.
- How to **run the tests**.
- The **licence** and how to **contribute** (links).
- The **status** ("early development; the API may change").

---

## 67.4 The licence: your decision

Chapter 65<!--ref:licences--> explained the options. For this project:

1. **Decide** what you want others to be able to do. If you are unsure, read the chapter again and ask someone qualified: a wrong choice is hard to undo, because people who received your code under a licence keep the rights it gave them.
2. **Get the text from an official source**, such as the licence's own page, or GitHub's licence template tool (Chapter 64<!--ref:oss-->, "Adding a license to a repository": create a file named `LICENSE` and choose a template). Never type a licence from memory.
3. **Put your own name** in the copyright line if the template asks for one, and the correct year.
4. **Say it in the README** in one line, with a link to the file.
5. **Re-run the check script**: it should now print `present: LICENSE`.

**No licence is a licence decision too:** GitHub's documentation says that without a licence "the default copyright laws apply". People will not be allowed to reuse your library.

For the code of conduct, GitHub's documentation advises: "Consider carefully whether you are willing and able to enforce it." If you choose one from a template, follow its attribution guidelines.

---

## 67.5 First release

After the recording, on your computer and GitHub:

1. Create the repository on GitHub without any files (Chapter 39<!--ref:ghrepo-->).
2. Add the remote and push the branch **and** the tag: `git push -u origin main` and `git push origin v0.1.0`.
3. Add a workflow that runs the tests on every push and pull request (Chapter 56<!--ref:workflows_practice-->), and pin any action to a commit (Chapter 60<!--ref:wfsec-->).
4. Create a release from the tag, with notes (Chapter 66<!--ref:releases-->).
5. Open the repository in a private browsing window, as a stranger would. Can you find the licence? Can you run the example?

---

## 67.6 Maintenance

A published project is a small commitment:

- **Triage issues** (Chapter 44<!--ref:issues-->): labels such as `good first issue` help newcomers.
- **Review pull requests** with kindness and a clear rule for what you accept (Chapter 46<!--ref:review-->).
- **Turn on the security features** you can (Chapter 62<!--ref:ghsec-->), and keep dependencies current.
- **Release regularly**, with a version number that follows your scheme.
- **Say what you will not do.** A README line such as "no feature requests for X" saves everyone's time.
- **Be honest about your capacity.** If you can no longer maintain it, say so in the README. GitHub has settings for closing down a repository; read the current documentation before using them.

---

## Checkpoint

## What You Learned

- A project should answer five questions quickly: what, may I, how, how to help, security.
- A tiny library with tests, a `.gitignore`, a README and community files is a complete start.
- A check script can tell you which community files are missing.
- The licence is your decision, made from official texts, and is not part of this book.
- A first release is an annotated `v0.1.0` tag, honest about being early.

## New Vocabulary

No new terms.

## Commands Learned

`python3 -m unittest discover -s tests`, `test -f`, `git tag -n1`, `git ls-files`.

## Common Mistakes

1. **Publishing without a licence and expecting reuse.**
2. **Committing generated files such as `__pycache__`.**
3. **A README example that no longer works.**
4. **Adopting a code of conduct you will not enforce.**
5. **Claiming an installation method you have not tried.**

## Practice

Do the exercises in [`exercises/ch67-exercises.md`](../../../exercises/ch67-exercises.md). Project 11 is in section 67.2.

## Self-Test

1. Which five questions should a project answer quickly?
2. Why does the recording end with a missing `LICENSE`?
3. Why is `__pycache__` ignored?
4. Why start at version 0.1.0?
5. What must you do before choosing a code of conduct?

## Before Moving On

You are ready for Chapter 68<!--ref:orgs--> if you can:

- [ ] lay out a small project with tests and community files
- [ ] explain why the licence is your decision
- [ ] tag a first release

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The library, tests, ignore file, community files, check script, tag and tracked-file list | Locally tested: Bash 5.2 and zsh 5.9, Git 2.43.0, Python 3.11; CI on newer Git and its Python | R324 (local side) |
| Statements about GitHub features | Cited in Chapters 64<!--ref:oss-->, 65<!--ref:licences--> and 66<!--ref:releases-->; not re-checked or run here | R314-R323 |
| Expected outcome of Project 11 on GitHub | Not observed; written from the earlier chapters | none |

## Where this leads

Part X, "Advanced GitHub", starts with Chapter 68<!--ref:orgs-->: organizations, teams and enterprise concepts.
