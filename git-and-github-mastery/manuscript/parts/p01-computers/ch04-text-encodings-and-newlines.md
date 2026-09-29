---
key: text
number: 4
tag: Core
first_read: full
status: draft
requires: [editors]
ledger: [R118, R119]
---
# Chapter 4 — Text, Encodings and Newlines [Core]

**In this chapter**

- how a computer stores letters as numbers, and what "encoding" means
- what UTF-8 is, and why it is the safe default
- why text sometimes turns into strange symbols, and how to fix it
- the invisible characters that end lines, and why two computers can disagree about them
- other invisible trouble: tabs, spaces and trailing spaces

**Before you start.** Chapter 3<!--ref:editors-->: you know what a plain text file is, and that Git can show readable differences for text but not for packaged binary files.

> **Look, don't type.** Some boxes in this chapter show commands, on lines that begin with `$`, followed by what the computer printed. You are *not* asked to type them yet. The terminal is introduced in Chapter 7<!--ref:terminal-->, where you can repeat every one of these. (The programs that read such commands are called *shells*; this book tests two of them, Bash and zsh.) For now, read the results: they are real output recorded in the book's test environment, and they show you what is hidden inside ordinary files.

---

## 4.1 From letters to numbers to bytes

A computer can only store numbers (Chapter 1<!--ref:computer--> said that everything is stored as bits and bytes). So to store the letter `A`, people had to agree on a number for it. Two ideas follow.

1. Every character (a letter, digit, punctuation mark, emoji, or a space) is given a number, in a shared list.
2. To save the character in a file, its number is turned into one or more bytes, following a rule.

An analogy: think of a book of secret codes. Page one says "A is 65, B is 66…". To send a message you look up each letter's number and write the numbers down. The person who reads it needs the same book. If they use a different book, the message comes out as nonsense.

> **New term: character.** A single unit of text: a letter, digit, punctuation mark, symbol, emoji, or space.

> **New term: encoding.** The rule that turns characters into bytes when they are saved, and back into characters when they are read.

The important lesson is already visible: **to read a text file correctly, you need to know how it was encoded.**

---

## 4.2 ASCII, Unicode and UTF-8

Three names will keep appearing, so it is worth meeting them once, calmly.

| Name | What it is | Size of the idea |
|---|---|---|
| **ASCII** | An old, small list of 128 characters: English letters, digits and common punctuation, plus some control codes | Enough for plain English |
| **Unicode** | A huge list that gives every character in the world's writing systems (and many symbols and emoji) its own number | Covers nearly every language |
| **UTF-8** | A way of writing Unicode numbers as bytes | Uses 1 byte for the basic English characters and 2 to 4 bytes for others |

> **New term: Unicode.** A universal list that assigns a number, called a code point, to each character of the world's writing systems, symbols and emoji.
>
> **New term: UTF-8.** The most widely used encoding of Unicode. It stores the basic English characters in one byte each and other characters in two to four bytes.

UTF-8 has one property that made it popular: text made only of basic English characters is stored **exactly as ASCII** would store it, byte for byte. So old English-only files are already valid UTF-8, and the new system can still store every other language.

### 4.2.1 See it: one letter, two bytes

Here is a real recording. A one-word file, `café`, is created and its bytes are displayed in hexadecimal (a compact way of writing byte values that uses the digits 0–9 and letters a–f). Each pair of characters is one byte.

```text
$ printf 'caf\303\251\n' > cafe.txt
$ cat cafe.txt
café
$ od -An -tx1 cafe.txt
 63 61 66 c3 a9 0a
$ wc -c cafe.txt
6 cafe.txt
```

*Example output; identical in the tested Bash and zsh.*

Read the bytes:

- `63 61 66` are the three characters `c`, `a`, `f`, one byte each, exactly as ASCII stores them.
- `c3 a9` is the single character `é`. In UTF-8 it takes **two** bytes.
- `0a` is the invisible **line break** at the end of the line (section 4.4).

So the file has four visible characters but **six bytes**. A counter of bytes and a counter of characters give different answers. Ordinary English text is the special case in which they are equal.

For an emoji, one character takes four bytes:

```text
$ printf '\360\237\215\236\n' | od -An -tx1
 f0 9f 8d 9e 0a
```

*Example output. The four bytes `f0 9f 8d 9e` are one character, a loaf of bread; the fifth byte is the line break.*

> **Verification pending [R118].** These demonstrations were run on real tools, so the byte values shown are facts about UTF-8 as implemented in the test environment. The statements that describe *history and popularity* (that ASCII has 128 characters, that UTF-8 is the most widely used encoding) are from general knowledge and will be checked against the Unicode Consortium's own publications before release.

**When to use UTF-8:** almost always, for any new file. Choose it in your editor (Chapter 3<!--ref:editors-->) and keep it.

**Alternatives and older encodings.** Other encodings exist, mostly older ones designed for a single language or region. You will meet them only in old files. If a file is not UTF-8, the safest action is to *convert* it deliberately with a tool, not to edit it in place.

---

## 4.3 When the wrong book is used: garbled text

Because the reader must know the encoding, mistakes appear as **garbled text**: `cafÃ©` instead of `café`. The technical name is *mojibake*, a Japanese word meaning "character change".

> **New term: mojibake.** Text that appears as strange symbols because it was read using a different encoding from the one used to write it.

Here is a controlled reproduction of exactly that problem. The same word is saved in two encodings and then read with the wrong one:

```text
the word:                 café
stored as UTF-8 bytes:    63 61 66 c3 a9   (5 bytes for 4 characters)
the same bytes read as Latin-1: cafÃ©
stored as Latin-1 bytes:  63 61 66 e9   (4 bytes)
Latin-1 bytes read as UTF-8:    UnicodeDecodeError (unexpected end of data)
with errors replaced:      caf�
emoji U+1F35E as UTF-8:   f0 9f 8d 9e   (4 bytes for 1 character)
```

*Example output from `verification/ch04-text/mojibake.py`. You do not need to run it. "Latin-1" is one of the older encodings.*

Two different failures appear:

1. The UTF-8 bytes `c3 a9` were read as if each byte were a separate character, giving `Ã©`.
2. The single byte `e9` is not a valid piece of UTF-8 text at all. Some programs refuse to continue; others print a replacement mark, `�`, and carry on, so **the original character is lost**.

**What to do when you see garbled text.**

1. Do not retype and re-save. That can make the damage permanent.
2. Look in your editor for the encoding it *thinks* the file uses (often shown in the status bar).
3. If you know the correct encoding, reopen the file with it (most editors have "Reopen with encoding").
4. Convert once, to UTF-8, and save.

**How this affects Git.** Git stores bytes. If two people save the same text in different encodings, Git sees different bytes and reports every affected line as changed. Agreeing on UTF-8 for the whole project prevents that. (Chapter 14<!--ref:config--> shows the Git settings involved.)

---

## 4.4 Line endings

When you press the Enter key, the editor inserts an invisible character that marks the end of a line: a **line break** (also called a **newline**).

> **New term: line ending (newline).** The invisible character or characters that mark the end of a line of text.

The complication is that two conventions exist, and the reason is historical. On a mechanical typewriter, ending a line took two separate movements: return the carriage to the left (*carriage return*, abbreviated CR), and roll the paper up one line (*line feed*, abbreviated LF). Early computer systems copied those two ideas, and they made different choices:

| Convention | Characters | Written | Traditionally used by |
|---|---|---|---|
| **LF** | one: line feed | `\n` | Linux, macOS and other Unix-like systems |
| **CRLF** | two: carriage return then line feed | `\r\n` | Windows |

> **Verification pending [R119].** The two conventions and their bytes are demonstrated below. Which convention each system uses *by default today*, and how modern programs on each system cope, is from general knowledge and awaits documentation-level verification.

### 4.4.1 See it: two extra bytes per line

Two files hold the same two lines, `one` and `two`. One uses LF, the other CRLF.

```text
$ printf 'one\ntwo\n' > unix.txt
$ printf 'one\r\ntwo\r\n' > windows.txt
$ od -c unix.txt
0000000   o   n   e  \n   t   w   o  \n
0000010
$ od -c windows.txt
0000000   o   n   e  \r  \n   t   w   o  \r  \n
0000012
$ wc -l unix.txt
2 unix.txt
$ wc -c unix.txt
8 unix.txt
$ wc -c windows.txt
10 windows.txt
```

*Example output; identical in the tested Bash and zsh.* (The `od -c` command prints each byte, showing invisible characters as `\n` for line feed and `\r` for carriage return.)

Read it. The LF file is 8 bytes; the CRLF file is 10, because each of the two lines has one extra invisible character. To a person looking at an editor, the two files look identical. To Git, which compares bytes, **they are different files.**

### 4.4.2 Why line endings cause real trouble

**Trouble 1: noisy differences.** If you open a file on Windows and your editor quietly converts every LF to CRLF, then Git will see every line as changed, even though you altered nothing visible. Someone reviewing your work sees hundreds of "changes" and cannot find the real one.

Here is a real recording of that effect. A two-line file was saved with LF endings and recorded by Git, then the same visible text was saved again with CRLF endings. The command summarises what Git thinks has changed:

```text
 f.txt | 4 ++--
 1 file changed, 2 insertions(+), 2 deletions(-)
```

*Example output from Git (which you will install in Chapter 13<!--ref:install-->). Two lines were "removed" and two "added", although a person would say that nothing changed. Recorded by `verification/ch04-text/git_line_endings.sh`.*

**Trouble 2: programs that stop working.** Some programs are strict. In the test below, a small script is written twice. One has LF line endings, the other has CRLF. Both are meant to print a greeting:

```text
$ ./lf.sh
hello from LF
$ ./crlf.sh
bash: ./crlf.sh: cannot execute: required file not found
$ grep -c "$(printf '\r')" crlf.sh
2
$ grep -c "$(printf '\r')" lf.sh
0
```

*Example output in Bash; the same experiment in zsh gives `zsh: ./crlf.sh: bad interpreter: /bin/sh^M: no such file or directory`. (The last two commands count the lines containing a carriage return.)*

The error message does not mention line endings. The reason is that the first line of the script names the program to run it with, `/bin/sh`, and the invisible carriage return at the end of that line becomes part of the name. The computer looks for a program called "`/bin/sh` followed by CR", finds nothing, and complains that the file is missing. The messages are different in the two shells, and the true cause is invisible unless you know to look.

Error messages that mention `^M` are a strong clue. `^M` is a common way of writing the carriage-return character.

**The lesson.** Line endings are not a matter of taste when files travel between computers. Decide on one convention *per project* and let the tools enforce it. You will do that with Git settings in Chapter 14<!--ref:config--> and with a file called `.gitattributes` in Chapter 32<!--ref:custom-->.

---

## 4.5 Other invisible characters

Three more invisible things can make otherwise identical text differ.

| Invisible thing | What it is | Trouble it causes |
|---|---|---|
| **Tab** | A single character that jumps to the next column | Looks like several spaces, but is different from spaces; mixing them makes files look misaligned in other editors |
| **Trailing spaces** | Spaces at the end of a line, after the last visible character | Invisible, but change the bytes; Git reports them as changes |
| **Missing final line break** | The last line has no line break at the end | Some tools warn, and Git marks it in its output with the note `\ No newline at end of file` |

Here they are, in bytes:

```text
$ printf 'a\tb\n' | od -c
0000000   a  \t   b  \n
0000004
$ printf 'a b\n' | od -c
0000000   a       b  \n
0000004
$ printf 'end   \n' | od -c
0000000   e   n   d              \n
0000007
```

*Example output. The first line holds a tab (`\t`), the second an ordinary space, and the third has three trailing spaces after `end`.*

A tab and a space look alike on screen, but they are different bytes. For that reason, code editors can **show whitespace**: dots for spaces, arrows for tabs. Turn it on while you learn.

---

## 4.6 Text or binary? A quick way to decide

A file is *text* if its bytes are meant to be read as characters in some encoding. It is *binary* if they are not: a photograph, a music file, a ZIP archive, a program. You met the ZIP signature `PK` in Chapter 3<!--ref:editors-->.

Signs of a binary file: your editor shows unreadable symbols, or offers to "open as binary"; the file is large compared with its visible content; or Git reports "Binary files differ". Handle binary files carefully in a project: do not edit them in a text editor and re-save them.

---

## 4.7 A checklist for text files in a project

Adopt these habits now; later chapters will show the Git settings that support them.

1. Save every file as **UTF-8**.
2. Agree one **line ending** convention for the project and check what your editor is set to.
3. **Show whitespace** while editing.
4. End every file with a line break.
5. Avoid **trailing spaces**.
6. Choose **tabs or spaces** for indentation and use one consistently within a file.

> **Try it.** Open `sunrise-bakery/index.html` in your code editor. Find these three things: (1) the encoding indicator (often at the bottom right of the window); (2) the line-ending indicator (it may say `LF` or `CRLF`); (3) the setting that shows whitespace. Turn on "show whitespace" and look at the indentation of the `<header>` block.
>
> *Expected result:* the editor states the encoding (ideally UTF-8) and line ending, and dots or arrows appear where there are spaces or tabs. Write down what you found.

> **UI-VERSION NOTE.** Where these indicators and settings are located differs by editor and version. If you cannot find them, search the editor's help for "encoding", "line endings" and "render whitespace".

---

## Checkpoint

## What You Learned

- Computers store characters as numbers; an encoding is the rule that turns characters into bytes.
- Unicode lists characters; UTF-8 is the widely used way to store them; English characters take one byte, others two to four.
- Reading a file with the wrong encoding produces garbled text (mojibake) or errors.
- A line ending is an invisible character; LF and CRLF are the two conventions, and they differ by one byte per line.
- Files that look the same can differ in bytes, and Git compares bytes.
- Tabs, trailing spaces and a missing final line break are also invisible differences.
- A simple checklist keeps text files consistent.

## New Vocabulary

- **Character**: a single unit of text such as a letter, digit, symbol or space.
- **Encoding**: the rule that turns characters into bytes and back.
- **Unicode**: a universal list that gives every character a number.
- **UTF-8**: the most widely used encoding of Unicode; one byte for basic English characters, two to four for others.
- **Mojibake**: garbled text caused by reading with the wrong encoding.
- **Line ending (newline)**: the invisible character or characters that end a line.

## Commands Learned

None to type yet. You *read* the output of `printf`, `od`, `wc` and `grep` (Chapter 7<!--ref:terminal--> introduces the terminal in which they run).

## Common Mistakes

1. **Assuming that same-looking files are identical.** Their bytes may differ.
2. **Fixing garbled text by retyping and saving.** Reopen with the correct encoding instead.
3. **Ignoring line endings when sharing files between Windows and other systems.** Agree a convention early.
4. **Mixing tabs and spaces in one file.**
5. **Editing a binary file in a text editor.**

## Practice

Do the exercises in [`exercises/ch04-exercises.md`](../../../exercises/ch04-exercises.md).

## Self-Test

1. What is an encoding, in one sentence?
2. The file `cafe.txt` shows four characters and is six bytes long. Where do the two extra bytes come from?
3. What do LF and CRLF stand for, and how do the two files in section 4.4.1 differ in size?
4. A script fails with an error mentioning `^M`. What is the most likely cause?
5. Give two reasons why two files that look identical on screen might be reported by Git as different.

## Before Moving On

You are ready for Chapter 7<!--ref:terminal--> if you can:

- [ ] explain what UTF-8 is without using the word "encoding" more than once
- [ ] find the encoding and line-ending indicators in your editor
- [ ] describe why a CRLF file and an LF file are different files
- [ ] turn on "show whitespace" in your editor

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| Byte values of `café` (5 bytes UTF-8), the four-byte emoji, and the read-as-wrong-encoding outcomes | Locally tested: `verification/ch04-text/session-bytes.txt` (Bash and zsh, interactive), `mojibake.py` (re-run in CI); Unicode Standard not yet consulted | R118 |
| LF versus CRLF bytes, sizes, the failing CRLF script and its two shell-specific messages | Locally tested: `session-bytes.txt`, `session-crlf-trouble.txt` (Bash 5.2 and zsh 5.9; also passes on the CI runner); which systems use which by default: unverified | R119 |
| Tabs, spaces and trailing spaces appear as distinct bytes | Locally tested (`session-bytes.txt`) | R118 |

## Where this leads

Chapter 7<!--ref:terminal--> finally gives you the terminal, in which you can repeat every command shown here. Chapter 8<!--ref:markdown--> introduces Markdown, a plain text format. Chapter 14<!--ref:config--> shows the Git settings that manage line endings, and Chapter 32<!--ref:custom--> explains `.gitattributes`.
