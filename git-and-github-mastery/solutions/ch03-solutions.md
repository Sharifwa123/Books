# Chapter 3 solutions

## Level 1
**1.1, 1.2** depend on your computer and editor. If line numbers are missing, search the editor's settings for "line numbers".

## Level 2
**2.1**
| File | Text or binary | Group |
|---|---|---|
| `index.html`, `menu.html`, `contact.html` | text | source files |
| `css/style.css` | text | source file |
| `images/logo.svg` | text | source file and asset |
| `README.md` | text | documentation |

**2.2** The page shows, but the logo is missing (a broken-image symbol or its alternative text). `index.html` refers to `images/logo.svg`, a relative path, which is resolved from the page's own folder. The `images` folder is no longer there, so the path leads nowhere.

## Level 3
**3.1** A good note says: a `.docx` file is a packaged container, not lines of text; Git can store each version but shows only that the file changed; a plain text format shows the exact lines added and removed; so keep files you want to compare closely as plain text.

## Level 4
**4.1** A workable recommendation: keep the schedule as a plain text or Markdown table in a repository, edited by a small number of people, with changes reviewed through pull requests (Chapter 45<!--ref:pr-->); note that an occasional printed or formatted copy can still be exported. One thing better in a word processor: layout and printing for people who need a formatted handout. If six non-technical people must edit at the same time, a shared online document may serve them better than Git; that is a legitimate alternative.

## Level 5
**5.1** Most likely the word processor added formatting or curly quotation marks, or saved in its own packaged format instead of plain text. Confirm by opening the file in a text editor: unfamiliar characters or a garbled start (such as `PK`) point to this. Fix: restore the original file and edit it only in a text or code editor.

**5.2** (1) Did you save? Look for an unsaved marker in the editor tab. (2) Did you edit the same file the browser is showing (check the folder and file name; you might have edited a copy)? (3) Did you reload, and is the browser showing a stored older copy? Try a forced reload or reopen the file.
