# Chapter 9 solutions

## Level 1
**1.1** Five files: `menu.txt`, `menu_v2.txt`, `menu_final.txt`, `menu_final_v2.txt`, `menu_final_REAL.txt`.

**1.2** `2c2` means line 2 of the first file was changed into line 2 of the second; `<` marks the first file's version of the line and `>` the second's. `2a3` means a line was added after line 2 of the first file to make the second; `>` shows the added line.

## Level 2
**2.1** Bob's copy did not contain Alice's change, and a plain file copy replaces the destination entirely. Neither file knows about the other's changes, so nothing could be flagged.

**2.2** (a) which is current (1); (b) why it changed (3); (c) who did what (6); (d) can I go back (4).

## Level 3
**3.1** Possible rules: one person edits at a time, announced in a shared message; always copy the shared file down before editing and only then copy it back; add a date and initials to every file name; keep a log of changes. Failures: someone forgets to announce, or copies an old file back; the log is not updated; the naming becomes inconsistent.

## Level 4
**4.1** Two people edit different copies at nearly the same time, or someone saves an old copy over the new one; the folder synchronises whichever save arrived last, so the earlier change is replaced (or a second "conflicted" copy appears and is ignored). A synchronised folder records the latest state and, in some services, a time-based history; it does not record reasons or combine changes intelligently. Recommendation: move the price list to a text file under version control with named, explained versions, or agree an editing rota in the meantime.

## Level 5
**5.1** By hand: compare the three files (with `diff`), then create a new file containing the cake line and the new bread price, and copy it to the shared location. A tool should compare all three versions automatically, identify that the two changes are on different lines, and combine them without human error, reporting a conflict only when the same line was changed differently in both.

**5.2** A backup keeps moments, not meaningful named versions; it records no reasons; it does not combine two people's work; and it may keep only a few recent copies.
