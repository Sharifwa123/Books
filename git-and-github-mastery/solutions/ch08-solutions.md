# Chapter 8 solutions

## Level 1
**1.1**
````markdown
# Study notes

Today I learned what Markdown is.

- headings
- lists
- links
````

**1.2** `[our menu](menu.html)` and `![Sunrise Bakery logo](images/logo.svg)`.

## Level 2
**2.1**
````markdown
| Item | Price |
|------|-------|
| Loaf | 2.50 |
| Rolls | 3.00 |
| Cake slice | 2.00 |
````
Without the dashed row, the lines render as plain text, not as a table.

**2.2** Two lines with no blank line: one paragraph (the lines join). With a blank line between: two paragraphs.

## Level 3
Any README meeting the list is correct. Check: a `#` title, a paragraph, a `##` section, `1.` `2.` `3.` steps, and a fenced code block.

## Level 4
**4.1** A six-row Markdown table with a header row and the dashed second row is a correct answer. Better for tracking: Git shows exactly which rows changed. Still better in a `.docx`: a formatted, printable rota with colours and layout for people who will not use Git.

## Level 5
**5.1** Add a blank line between `Ingredients:` and the first dash. It is a good habit because it works in every renderer and costs nothing.

**5.2** (1) The dashed second row is missing or malformed. (2) The renderer does not support tables (they are an extension), or there is no blank line before the table.

**5.3** A path that depended on where the project sat (for example an absolute path such as `/home/me/project/menu.html`). Use a relative path from the file that contains the link (Chapter 2<!--ref:files-->).
