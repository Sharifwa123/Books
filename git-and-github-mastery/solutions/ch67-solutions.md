# Chapter 67 solutions

## Level 1
**1.1** What is it? README. May I use it? Licence. How do I try it? README (install and usage). How do I help? `CONTRIBUTING.md` and the code of conduct. What about a security problem? `SECURITY.md`.

**1.2** `LICENSE` and `CODE_OF_CONDUCT.md`. The licence is the author's decision, made from an official text; a code of conduct is a promise the maintainer must be able to keep.

## Level 2
**2.1** After the steps of the recording, `git tag -n1` shows `v0.1.0` with its message and `git ls-files` lists `.gitignore`, `CONTRIBUTING.md`, `README.md`, `SECURITY.md`, `src/wordcount.py` and `tests/test_wordcount.py`.

**2.2** `count_words(" one two ")` returns 2, because `split()` ignores leading and trailing white space, so the test passes. A test such as `self.assertEqual(count_words(" one two "), 2)` is correct.

## Level 3
**3.1** Answers depend on the idea. A good answer shows the new function and tests, a README example that was run, and the same community files.

**3.2** `for f in .gitignore README.md tests; do test -e "$f" && echo "present: $f" || echo "MISSING: $f"; done`

## Level 4
**4.1** Typical improvements: a one-sentence purpose at the top of the README, a working usage example, a visible licence, and a link to `CONTRIBUTING.md`.

## Level 5
**5.1** Add `__pycache__/` to `.gitignore`. If they are already committed, remove them from the index with `git rm -r --cached` and commit (Chapter 18<!--ref:tracking--> on removing tracked files without deleting them).

**5.2** Tell them that without a licence the default copyright applies and you cannot give permission by chat, and that you will decide on a licence. Then choose one from an official text (Chapter 65<!--ref:licences-->), add it, and reply with a link.
