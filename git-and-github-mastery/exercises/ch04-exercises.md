# Chapter 4 exercises — Text, Encodings and Newlines

Attempt each exercise before you open `solutions/ch04-solutions.md`. These exercises use only your editor; the terminal comes in Chapter 7<!--ref:terminal-->, where you can repeat the recorded commands.

## Level 1 — Guided

**1.1 Find the indicators.** Open any text file in your editor. Write down the encoding and the line-ending style it reports (for example "UTF-8" and "LF"). *Expected result:* two words or abbreviations.

**1.2 Show whitespace.** Turn on "show whitespace" and look at a file with indented lines. *Expected result:* dots or arrows mark the spaces or tabs.

## Level 2 — Partially guided

**2.1 Count bytes.** Using section 4.2.1 as a model, work out how many bytes the UTF-8 file containing exactly the text `naïve` (with a line break at the end) occupies. Hint: only the `ï` needs two bytes.

**2.2 Read the bytes.** A file's bytes are `48 69 0d 0a`. Write the text it contains and name its line-ending style. Hint: `48` is `H`, `69` is `i`.

## Level 3 — Independent

**3.1** Explain in your own words, in four sentences, why a file that looks identical on two computers might still be reported as changed by Git.

## Level 4 — Professional scenario

**4.1** A team of four works on a website. Two use Windows and two use Linux. Code reviews are full of "changes" nobody made. Propose, in a short list, the conventions the team should agree (encoding, line endings, whitespace, final line break), and say how each would be checked.

## Level 5 — Troubleshooting

**5.1** A visitor reports that the bakery page shows `CafÃ© Special` where the menu says `Café Special`. Explain the cause, the evidence you would look for in the file, and the fix.

**5.2** A small script works on a Linux server but, after being edited on a Windows laptop and copied back, fails with a message mentioning `^M`. Explain why, and give two ways to prevent a repeat.
