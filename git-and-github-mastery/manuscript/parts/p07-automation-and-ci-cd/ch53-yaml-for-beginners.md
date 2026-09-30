---
key: yaml
number: 53
tag: Core
first_read: full
status: draft
requires: [cicd, text]
ledger: [R281, R282]
---
# Chapter 53 — YAML for Beginners [Core]

**In this chapter**

- what YAML is, and why workflows are written in it
- the three building blocks: maps, lists and scalars
- indentation, comments and multi-line text
- the surprises: `no`, `3.10` and the key `on`
- how to read a YAML error

> **How to read this chapter.** Every YAML example was parsed by a real parser and the result is shown. The parser is **PyYAML 6.0.1**, which reads some words (`no`, `on`) as Booleans, a behaviour that comes from the older YAML **1.1** rules; the chapter says where that matters, and checks the current YAML **1.2.2** specification (from its open repository) for what it says. GitHub reads workflow files with its own tools, so a result here shows how *a* parser behaves, not how GitHub's does.

**Before you start.** Chapter 52<!--ref:cicd--> and Chapter 4<!--ref:text--> (why tabs and spaces are different characters). The recording ran in Bash and zsh with Python 3 and PyYAML, and was re-run in CI.

---

## 53.1 What YAML is

> **New term: YAML.** A text format for structured data (settings, lists, nested values) that is meant to be readable by people. Its structure is written with indentation and simple punctuation, not with brackets.

Configuration for automation lives in files: which checks to run, on what event, on which machine. YAML is the format of GitHub Actions workflows (Chapter 54<!--ref:actions-->), and it is also used by issue forms (Chapter 44<!--ref:issues-->) and many other tools. A mistake in it means a workflow that does not run, so it is worth learning carefully.

The current specification is **YAML 1.2.2** (revision of 1 October 2021), published in the open `yaml/yaml-spec` repository. It says that in block styles "structure is determined by indentation", where indentation is "zero or more space characters at the start of a line", and that "to maintain portability, tab characters must not be used in indentation".

> **Checked against the YAML specification (R281).** The quotations are from YAML 1.2.2, "Indentation Spaces". The specification defines comments as beginning with a hash sign (`#`), and a *Core schema* that resolves plain values by pattern: `null`, `true`/`false` (in the spellings `true`, `True`, `TRUE`, `false`, `False`, `FALSE` only), integers, floats, and otherwise strings. The specification recommends the Core schema as the default.

---

## 53.2 Three building blocks

A **scalar** is a single value: text, a number, true or false, or null. A **map** (also called a mapping or dictionary) is a set of `key: value` pairs. A **list** (a sequence) is items introduced by `- `. Maps and lists nest by **indentation**. All of the following were parsed by the parser; the line after each `$` command is what it produced, with each result written in Python's notation:

```text
$ printf 'name: Sunrise Bakery\nopen: true\nprices:\n  loaf: 2.80\n  rolls: 3\n' | python3 y.py
{'name': 'Sunrise Bakery', 'open': True, 'prices': {'loaf': 2.8, 'rolls': 3}}
$ printf 'items:\n  - White loaf\n  - Rolls\n' | python3 y.py
{'items': ['White loaf', 'Rolls']}
```

*Recorded in Bash; `ch53-yaml/expected-parse.bash.txt`.*

The first document is a map with three keys. The value of `open` is a real true/false value (`True`), `loaf: 2.80` became the number `2.8`, and `rolls: 3` the whole number `3`. `prices` is itself a map, nested by two spaces of indentation. The second is a map whose `items` value is a list of two strings.

Rules that follow from this:

1. **Indent with spaces, never tabs.** Two spaces per level is the usual habit. What matters is that siblings line up exactly.
2. **`key: value` needs a space after the colon.**
3. **`- item` needs a space after the dash.**
4. **A comment starts with `#`** and runs to the end of the line.
5. **Order in a list matters; order of keys in a map should not.** The specification says that "mapping key order" should not be referenced when the data is built, so do not write a file that only works if keys come in a certain order.

---

## 53.3 Strings and numbers: the surprises

YAML decides the *type* of a plain (unquoted) value by looking at it. Usually that is what you want, and sometimes it is a trap. Four cases, parsed:

```text
$ printf 'version: 3.10\n' | python3 y.py
{'version': 3.1}
$ printf 'version: "3.10"\n' | python3 y.py
{'version': '3.10'}
$ printf 'answer: no\n' | python3 y.py
{'answer': False}
$ printf 'answer: "no"\n' | python3 y.py
{'answer': 'no'}
```

*Recorded in Bash; `ch53-yaml/expected-parse.bash.txt`.*

- `version: 3.10` became the **number 3.1**: the trailing zero is gone. A version like `3.10` must be written in quotes, `"3.10"`, to stay text. This trap is in YAML 1.1 and 1.2 alike, because `3.10` matches the pattern for a number.
- `answer: no` became **False** in this parser, which follows the older YAML 1.1 habit of reading words such as `yes`, `no`, `on` and `off` as Booleans (that habit was not checked against a 1.1 source here; the recording shows it). The Core schema of the **1.2.2** specification recognises only `true`, `True`, `TRUE`, `false`, `False` and `FALSE` as Booleans, so `no` is a string there. Different tools follow different versions, so when in doubt, **quote the value**: `"no"`.
- `"no"` in quotes is always the text `no`.

The same rule explains why quoting is the safe habit for anything that must stay text: version numbers, words like `no`, values starting with special characters, and anything that looks like a number but is an identifier (a ZIP code with a leading zero, for instance).

**Multi-line text.** The specification's block scalars keep line breaks (`|`) or fold them into spaces (`>`). They are used for shell commands that run over several lines (Chapter 54<!--ref:actions-->).

---

## 53.4 Reading a YAML error

Two of the most common mistakes, parsed:

```text
$ printf 'menu:\n  - loaf\n - rolls\n' | python3 y.py
ERROR: ParserError
$ printf 'menu:\n\t- loaf\n' | python3 y.py
ERROR: ScannerError
```

*Recorded in Bash; `ch53-yaml/expected-parse.bash.txt`.*

The first has a list item indented by two spaces and the next by one space: the second `-` does not line up with the first, and the parser stops with a `ParserError`. The second uses a **tab** to indent, which the specification forbids, and the parser stops with a `ScannerError`. The class of the error (and, in a real tool, its line number) tells you where to look.

A checklist when a YAML file "does nothing":

1. Are all tabs gone? (A good editor shows whitespace, Chapter 3<!--ref:editors-->.)
2. Do siblings line up exactly, and is each child indented more than its parent?
3. Is there a space after every `:` and `-`?
4. Are values that look like numbers or booleans but should be text in quotes?
5. Is a colon inside a value making the parser think it is a new key? Quote the value.

---

## 53.5 A word about `on`

Chapter 54<!--ref:actions--> starts every workflow with a key called `on`. Look at the last recorded line:

```text
$ printf 'on: push\n' | python3 y.py
{True: 'push'}
```

*Recorded in Bash; `ch53-yaml/expected-parse.bash.txt`.*

This parser read the key `on` as the Boolean **True** (the same habit that turned `no` into false), and the result is a map whose key is `True`. That is a fact about *this* parser. GitHub's own documentation writes `on:` as an ordinary key in every workflow, so GitHub's tools do not treat it that way. The lesson is general: **another YAML tool, such as an editor plug-in or a linter, may read `on` differently from GitHub.** If a linter complains about `on`, check which YAML version it follows before changing your workflow.

> **Checked against the recorded run (R282).** The parse results above come from PyYAML 6.0.1 on the runner and locally. What GitHub's parser does with `on` is not tested here; its documentation uses `on:` as a plain key (Chapter 54<!--ref:actions-->).

---

## Checkpoint

## What You Learned

- YAML has scalars, maps and lists, nested by indentation with spaces, never tabs.
- A plain value's type is guessed: `3.10` becomes `3.1`, and some parsers read `no` as false.
- Quote values that must stay text.
- A `ParserError` or `ScannerError` usually means bad alignment or a tab.
- Different YAML tools follow different rules: one parser read the key `on` as a Boolean.

## New Vocabulary

**YAML** (introduced above).

## Commands Learned

`python3 -c 'import yaml'`-style parsing (used to check files), `printf ... | python3 y.py`.

## Common Mistakes

1. **A tab for indentation.**
2. **An unquoted version number** such as `3.10`.
3. **An unquoted `no`, `yes`, `on` or `off`.**
4. **Children that do not line up with their siblings.**
5. **Trusting one parser's behaviour for all tools.**

## Practice

Do the exercises in [`exercises/ch53-exercises.md`](../../../exercises/ch53-exercises.md).

## Self-Test

1. What are the three building blocks of YAML?
2. Why is `version: 3.10` a problem?
3. Why does the chapter recommend quoting `"no"`?
4. What does a `ScannerError` on a line that starts with a tab tell you?
5. How would you write a two-item list under the key `steps`?

## Before Moving On

You are ready for Chapter 54<!--ref:actions--> if you can:

- [ ] write a small map with a nested list
- [ ] spot a tab or a misaligned line
- [ ] decide when to quote a value

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Parse results, error classes, `3.10`, `no`, `on` | Locally tested with PyYAML 6.0.1 and Python 3: Bash 5.2 and zsh 5.9; CI | R282 |
| Indentation rule, no tabs, comments, Core schema and Boolean spellings in YAML 1.2.2 | Officially verified against the YAML 1.2.2 specification (open repository) | R281 |
| What GitHub's parser does with `on` | **Not tested** | R282 |

## Where this leads

Chapter 54<!--ref:actions--> uses YAML to write real workflows, and Chapter 57<!--ref:wfdebug--> shows how to read the errors GitHub reports.
