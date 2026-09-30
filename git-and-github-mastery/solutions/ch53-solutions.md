# Chapter 53 solutions

## Level 1
**1.1** `name: Sunrise Bakery`, `open: true`, `loaf: 2.80` parse to `{'name': 'Sunrise Bakery', 'open': True, 'loaf': 2.8}`.

**1.2** `items:` followed by three lines each starting with two spaces, a dash and a space parse to a map with a list.

## Level 2
**2.1** A map nested with two-space indentation; a list inside a map inside a list needs each level indented more than its parent.

**2.2** `3.10` is a number, so it becomes `3.1`; quoted, it stays the text `3.10`.

## Level 3
**3.1** PyYAML gives `False` for unquoted `no` and `'no'` for the quoted form. Write `"no"` in quotes to be safe.

**3.2** (a) `ScannerError`; (b) `ParserError`; (c) a missing space after the colon makes the whole line a plain string, not a key: value pair, so the result is a text value or an error depending on the rest of the file.

## Level 4
**4.1** Tabs gone; siblings aligned and children indented more than parents; space after every colon and dash; ambiguous values quoted; colons inside values quoted.

## Level 5
**5.1** `3.10` matches the number pattern and becomes `3.1`. Write `python: "3.10"`.

**5.2** Check which YAML version the linter follows, and how GitHub's documentation writes the key (`on:` as an ordinary key). Do not change a working workflow because of a linter that follows different rules.
