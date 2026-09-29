# Chapter 4 solutions

## Level 1
**1.1** and **1.2** depend on your editor. A well-configured project shows UTF-8 and either LF or CRLF (whichever the project chose).

## Level 2
**2.1** `naïve` has five characters. Four are basic English characters (one byte each) and `ï` takes two bytes, so the word is 6 bytes, plus 1 byte for the line break: **7 bytes**.

**2.2** The bytes are `H`, `i`, carriage return, line feed: the text `Hi` followed by a **CRLF** line ending.

## Level 3
**3.1** A good answer: Git compares the bytes of a file, not what a person sees. Line endings, tabs versus spaces, trailing spaces, a missing final line break and encodings are all bytes that do not show on screen. Changing any of them changes the file, so Git reports it as changed.

## Level 4
**4.1** Example: (1) UTF-8 everywhere; (2) one line-ending convention for the repository (LF is a common choice), enforced by a setting in the repository rather than by each person's habits (Chapter 14<!--ref:config--> and Chapter 32<!--ref:custom-->); (3) show whitespace on; (4) files end with a line break; (5) no trailing spaces. Checks: a shared configuration file, a review checklist and automated checks in pull requests (Chapter 54<!--ref:actions-->).

## Level 5
**5.1** The page's bytes are UTF-8 (`é` is `c3 a9`), but the page is being read as if it were an older single-byte encoding, so each byte shows as its own character (`Ã` and `©`). Evidence: the file's own bytes show `c3 a9`; the browser or page declares no encoding or the wrong one. Fix: save as UTF-8 and declare UTF-8 in the page (the starter pages contain a line that does this).

**5.2** Editing on Windows changed the line endings to CRLF. The first line of the script names its interpreter, and the invisible carriage return became part of the name, so the system could not find it. Prevention: configure the editor to save that file with LF endings, and set a repository rule (Chapter 32<!--ref:custom-->) so that scripts always keep LF.
