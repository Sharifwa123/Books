# Chapter 42 solutions

## Level 1
**1.1** What the project does; why it is useful; how to get started; where to get help; who maintains it.

**1.2** Answers vary. Check that the first two sentences say what the project is.

## Level 2
**2.1** `grep -o` prints `](docs/CONTRIBUTING.md)`, and `test -f docs/CONTRIBUTING.md && echo found` prints `found`.

**2.2** `git status --short` shows a rename (`R  docs/CONTRIBUTING.md -> docs/HELP.md`). It does not say that a link in the README now points to a file that does not exist: a link is plain text and Git does not track it.

## Level 3
**3.1** Answers vary. The install line and a short example should appear before any long explanation.

**3.2** For example:
```bash
grep -o '](\([^)]*\))' README.md | sed 's/^](//; s/)$//' | while read -r t; do
  case "$t" in http*) continue ;; esac
  [ -f "$t" ] || echo "missing: $t"
done
```

## Level 4
**4.1** Answers vary. A common fix is to move the "what it is" sentence to the very top and the install steps directly under it.

## Level 5
**5.1** The file was renamed or moved, and links are only text, so nothing in Git updates them. Search the repository for the old path (`git grep "docs/setup.md"`) and fix each result.

**5.2** Topics use lowercase letters, numbers and hyphens, so the capital letters are wrong; and topic names are always public, so an internal tool's name should not be published as one. (Also, at 24 characters it is within the 50-character limit, so length is not the problem.)
