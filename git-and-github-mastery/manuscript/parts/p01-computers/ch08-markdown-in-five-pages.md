---
key: markdown
number: 8
tag: Core
first_read: full
status: draft
requires: [editors, text]
ledger: [R131, R132]
---
# Chapter 8 — Markdown in Five Pages [Core]

**In this chapter**

- what Markdown is and why nearly every Git project uses it
- the twelve pieces of syntax you will use every day, each shown with the real result
- the mistakes that trip up nearly everyone, and what really happens when you make them
- how to write your first `README.md`

**Before you start.** Chapter 3<!--ref:editors--> (plain text, text editors) and Chapter 4<!--ref:text--> (line endings and invisible characters). You do not need a terminal for this chapter.

---

## 8.1 What Markdown is

Chapter 3<!--ref:editors--> said that a word processor saves formatting, and that this makes a file hard for Git to compare. But people still want headings, lists, links and emphasis in their notes and documentation. Markdown is the compromise.

> **New term: Markdown.** A way of writing formatted documents in plain text, using simple marks such as `#` for a heading and `*` for emphasis, which a program can turn into a formatted page.

A Markdown file is an ordinary text file, usually named with the extension `.md`. You write the marks; a program called a **renderer** converts them into what readers see.

> **New term: renderer.** A program that reads a marked-up text file and produces the formatted result for display.

There are two views of one document:

| View | What you see | Who uses it |
|---|---|---|
| **Source** | The plain text with its marks | The author, and Git |
| **Rendered** | Headings, bold text, lists, links | Readers |

**Why this matters for Git.** The source is plain text, so Git can show line-by-line differences, and everyone can read it even without a renderer. A Markdown file called `README.md` in a project is treated specially by services such as GitHub: they show it, rendered, on the project's front page (Chapter 42<!--ref:readme-->). Issues, pull requests and documentation use it too. This book's chapters are written in Markdown.

**When not to use Markdown.** For a page with complex layout, printed forms, or heavy graphics, use a tool built for it. Markdown is good for text-centred documents.

> **How to read the examples.** Each example below shows the **source** you type, and the **HTML** that a standard CommonMark renderer produced from it (see section 8.6). You do not need to understand HTML: read the tags as labels. `<h1>` is a main heading, `<p>` a paragraph, `<ul>` a bulleted list, `<li>` one item of a list, `<em>` emphasis, `<strong>` strong emphasis.

---

## 8.2 The syntax you will use every day

### 8.2.1 Headings

A line that starts with one to six `#` characters, then a space, is a heading. More `#` means a smaller heading.

<!--md-case:heading-->
**Source**
````markdown
# Sunrise Bakery

## Menu

### Breads
````

**Rendered as HTML by a CommonMark renderer**
```html
<h1>Sunrise Bakery</h1>
<h2>Menu</h2>
<h3>Breads</h3>
```

### 8.2.2 Paragraphs and line breaks

A **blank line** separates paragraphs. A single line break inside a paragraph is *not* a break: the lines join into one paragraph.

<!--md-case:paragraphs-->
**Source**
````markdown
Fresh bread every morning.

We open at six.
````

**Rendered as HTML by a CommonMark renderer**
```html
<p>Fresh bread every morning.</p>
<p>We open at six.</p>
```

<!--md-case:one-paragraph-two-lines-->
**Source**
````markdown
Fresh bread
every morning.
````

**Rendered as HTML by a CommonMark renderer**
```html
<p>Fresh bread
every morning.</p>
```

Notice the second example: two source lines became one paragraph. To force a line break *within* a paragraph, end the line with two spaces:

<!--md-case:hard-break-two-spaces-->
**Source**
````markdown
Fresh bread  
every morning.
````

**Rendered as HTML by a CommonMark renderer**
```html
<p>Fresh bread<br />
every morning.</p>
```

The two trailing spaces are **invisible**, which is exactly the kind of hidden difference Chapter 4<!--ref:text--> warned about. Many authors prefer a blank line and a new paragraph instead.

### 8.2.3 Emphasis

One pair of asterisks makes *emphasis* (usually shown in italics); two make **strong emphasis** (usually bold); three make both.

<!--md-case:emphasis-->
**Source**
````markdown
This is *italic*, this is **bold**, and this is ***both***.
````

**Rendered as HTML by a CommonMark renderer**
```html
<p>This is <em>italic</em>, this is <strong>bold</strong>, and this is <em><strong>both</strong></em>.</p>
```

Underscores inside a word are left alone:

<!--md-case:underscore-in-word-->
**Source**
````markdown
Use the file_name_here.txt file.
````

**Rendered as HTML by a CommonMark renderer**
```html
<p>Use the file_name_here.txt file.</p>
```

### 8.2.4 Lists

Start each item with `-`, `*` or `+` for a bulleted list, or with `1.`, `2.`, `3.` for a numbered one. Indent an item by two spaces to nest it.

<!--md-case:unordered-list-->
**Source**
````markdown
- White loaf
- Whole-wheat loaf
- Rolls
````

**Rendered as HTML by a CommonMark renderer**
```html
<ul>
<li>White loaf</li>
<li>Whole-wheat loaf</li>
<li>Rolls</li>
</ul>
```

<!--md-case:ordered-list-->
**Source**
````markdown
1. Mix
2. Knead
3. Bake
````

**Rendered as HTML by a CommonMark renderer**
```html
<ol>
<li>Mix</li>
<li>Knead</li>
<li>Bake</li>
</ol>
```

<!--md-case:nested-list-->
**Source**
````markdown
- Breads
  - White loaf
  - Whole-wheat loaf
- Cakes
````

**Rendered as HTML by a CommonMark renderer**
```html
<ul>
<li>Breads
<ul>
<li>White loaf</li>
<li>Whole-wheat loaf</li>
</ul>
</li>
<li>Cakes</li>
</ul>
```

### 8.2.5 Links and images

A link is `[the words you see](where it goes)`. An image is the same with a leading `!`, and its words are the **alternative text**, shown when the image cannot be, and read aloud to people who cannot see it.

<!--md-case:link-->
**Source**
````markdown
Visit [our menu](menu.html) today.
````

**Rendered as HTML by a CommonMark renderer**
```html
<p>Visit <a href="menu.html">our menu</a> today.</p>
```

<!--md-case:image-->
**Source**
````markdown
![Sunrise Bakery logo](images/logo.svg)
````

**Rendered as HTML by a CommonMark renderer**
```html
<p><img src="images/logo.svg" alt="Sunrise Bakery logo" /></p>
```

Paths in links and images are the **relative paths** of Chapter 2<!--ref:files-->. A link such as `menu.html` means "the file called `menu.html` next to this one".

### 8.2.6 Code

Put a word in single backticks to show it as code. Fence a block of lines between three backticks, optionally naming the language, to show several lines exactly as typed.

<!--md-case:inline-code-->
**Source**
````markdown
Run `git status` now.
````

**Rendered as HTML by a CommonMark renderer**
```html
<p>Run <code>git status</code> now.</p>
```

<!--md-case:code-block-->
**Source**
````markdown
```bash
git status
```
````

**Rendered as HTML by a CommonMark renderer**
```html
<pre><code class="language-bash">git status
</code></pre>
```

A block indented by four spaces is also treated as code:

<!--md-case:code-block-indent-->
**Source**
````markdown
    git status
````

**Rendered as HTML by a CommonMark renderer**
```html
<pre><code>git status
</code></pre>
```

### 8.2.7 Quotes and rules

<!--md-case:blockquote-->
**Source**
````markdown
> Fresh bread every morning.
````

**Rendered as HTML by a CommonMark renderer**
```html
<blockquote>
<p>Fresh bread every morning.</p>
</blockquote>
```

<!--md-case:rule-->
**Source**
````markdown
Above

---

Below
````

**Rendered as HTML by a CommonMark renderer**
```html
<p>Above</p>
<hr />
<p>Below</p>
```

### 8.2.8 Tables

A table uses `|` to separate columns, and a second row of dashes under the header. Tables are **not** part of the core Markdown specification but an extension that most renderers, including GitHub's, support (Chapter 42<!--ref:readme-->).

<!--md-case:table-->
**Source**
````markdown
| Item | Price |
|------|-------|
| Loaf | 2.50 |
| Rolls | 3.00 |
````

**Rendered as HTML by a CommonMark renderer**
```html
<table>
<thead>
<tr>
<th>Item</th>
<th>Price</th>
</tr>
</thead>
<tbody>
<tr>
<td>Loaf</td>
<td>2.50</td>
</tr>
<tr>
<td>Rolls</td>
<td>3.00</td>
</tr>
</tbody>
</table>
```

### 8.2.9 Escaping

To show a mark literally, put a backslash before it:

<!--md-case:escape-->
**Source**
````markdown
Cost: 3 \* 2 = 6
````

**Rendered as HTML by a CommonMark renderer**
```html
<p>Cost: 3 * 2 = 6</p>
```

### 8.2.10 HTML inside Markdown

Markdown allows raw HTML tags for the rare things it cannot express:

<!--md-case:html-inline-->
**Source**
````markdown
Text with <b>bold</b> HTML.
````

**Rendered as HTML by a CommonMark renderer**
```html
<p>Text with <b>bold</b> HTML.</p>
```

---

## 8.3 What goes wrong

These are the mistakes that beginners make most, with the result of each, tested on a real renderer.

**1. A table without its dashed second row is not a table.** It stays as plain text:

<!--md-case:table-no-separator-->
**Source**
````markdown
| Item | Price |
| Loaf | 2.50 |
````

**Rendered as HTML by a CommonMark renderer**
```html
<p>| Item | Price |
| Loaf | 2.50 |</p>
```

**2. Expecting a single line break to be a line break.** It is not (see the two-line example above).

**3. A list right after a paragraph line.** Many authors forget the blank line:

<!--md-case:list-needs-blank-line-->
**Source**
````markdown
Ingredients:
- flour
- water
````

**Rendered as HTML by a CommonMark renderer**
```html
<p>Ingredients:</p>
<ul>
<li>flour</li>
<li>water</li>
</ul>
```

This standard renderer accepted the list even without a blank line. Other renderers, and older versions of Markdown, may not. **The safe habit: always leave a blank line before a list, a table or a code block.** It is harmless, and it works everywhere.

**4. Expecting a bare web address to become a link.** In plain CommonMark, it does not:

<!--md-case:bare-url-->
**Source**
````markdown
See https://example.org for details.
````

**Rendered as HTML by a CommonMark renderer**
```html
<p>See https://example.org for details.</p>
```

To be safe, write the link explicitly (`[the site](https://example.org)`), or wrap the address in angle brackets so that the renderer knows it is a link:

<!--md-case:autolink-->
**Source**
````markdown
See <https://example.org> for details.
````

**Rendered as HTML by a CommonMark renderer**
```html
<p>See <a href="https://example.org">https://example.org</a> for details.</p>
```

> **Checked against a source [R132].** GitHub's published Markdown specification (version 0.29, 2019) lists autolinks, tables, task lists and strikethrough as extensions to CommonMark, including the recognition of a bare `www.` or `http` address as a link. What GitHub's website shows today was not observed in this book's test environment, and the demonstration above is of plain CommonMark only.

---

## 8.4 Flavours of Markdown

There is more than one Markdown. The original description was informal, so different programs made different choices, and people wrote **CommonMark**, a precise written specification, to fix that.

> **New term: CommonMark.** A precise, written specification of the core Markdown syntax, so that different renderers produce the same result.

Services then add their own extras on top. GitHub's version is called **GitHub Flavored Markdown**; among other things, it adds tables, task lists and automatic links. The practical lesson: **the core syntax in this chapter works everywhere; extras may not.** When the book reaches GitHub, it will say which features are GitHub's own, after checking them.

---

## 8.5 Your first README

A `README.md` is the front page of a project. It says what the project is and how to use it. Here is a starter for the Sunrise Bakery project. Read it as source, then look at the HTML that came out:

<!--md-case:readme-example-->
**Source**
````markdown
# Sunrise Bakery

A small website for a *fictional* neighbourhood bakery, used as the running example in a textbook.

## Pages

- `index.html`: the home page
- `menu.html`: the menu
- `contact.html`: how to find us

## Opening hours

| Day | Hours |
|-----|-------|
| Monday to Saturday | 06:00 to 18:00 |
| Sunday | closed |

## Licence

See the licence file when one is added.
````

**Rendered as HTML by a CommonMark renderer**
```html
<h1>Sunrise Bakery</h1>
<p>A small website for a <em>fictional</em> neighbourhood bakery, used as the running example in a textbook.</p>
<h2>Pages</h2>
<ul>
<li><code>index.html</code>: the home page</li>
<li><code>menu.html</code>: the menu</li>
<li><code>contact.html</code>: how to find us</li>
</ul>
<h2>Opening hours</h2>
<table>
<thead>
<tr>
<th>Day</th>
<th>Hours</th>
</tr>
</thead>
<tbody>
<tr>
<td>Monday to Saturday</td>
<td>06:00 to 18:00</td>
</tr>
<tr>
<td>Sunday</td>
<td>closed</td>
</tr>
</tbody>
</table>
<h2>Licence</h2>
<p>See the licence file when one is added.</p>
```

> **Try it.** In your `sunrise-bakery` folder, create a text file named `README.md` (replace the existing one from Chapter 7<!--ref:terminal--> if there is one) with your own version of the source above. Use your editor's Markdown preview if it has one (search its help for "Markdown preview"). Change one word, save, and watch the preview change. Make one of the mistakes from section 8.3 on purpose, and see what happens.
>
> *Expected result:* headings, a list and a table appear in the preview. The mistakes appear as the examples above show.

---

## 8.6 How the examples were made

Every example in this chapter was generated by a real program, not typed from memory: **markdown-it**, a widely used CommonMark renderer written in Python, with its table extension switched on. The book's build compares the source and HTML shown here with the recorded results, and fails if they differ. Other renderers may print a slightly different HTML for the same source (for example a space before a closing tag); the *structure* is what matters.

---

## Checkpoint

## What You Learned

- Markdown is plain text with simple marks that a renderer turns into a formatted page; files usually end in `.md`.
- The core syntax: headings, paragraphs, emphasis, lists, links, images, code, quotes, rules, tables and escapes.
- A single line break does not start a new paragraph; a blank line does.
- A table needs its dashed second row; leave blank lines before lists, tables and code blocks.
- CommonMark is a precise specification; services such as GitHub add extras.
- A `README.md` is a project's front page.

## New Vocabulary

- **Markdown**: a way of writing formatted text using plain-text marks.
- **Renderer**: a program that turns marked-up text into a formatted result.
- **CommonMark**: a precise written specification of the core Markdown syntax.

## Commands Learned

None.

## Common Mistakes

1. **Forgetting the dashed row in a table.**
2. **Expecting one line break to start a new paragraph.**
3. **No blank line before a list, table or code block.**
4. **Expecting a bare address to be a link** on every renderer.
5. **Trailing spaces used for line breaks** (invisible, easily lost).
6. **Writing documentation in a word processor** when the project needs readable differences.

## Practice

Do the exercises in [`exercises/ch08-exercises.md`](../../../exercises/ch08-exercises.md).

## Self-Test

1. What is the difference between source and rendered views?
2. Write the Markdown for a second-level heading, a bulleted list of two items, and a link to `menu.html` with the text "our menu".
3. Two lines are typed one below the other with no blank line. How many paragraphs result?
4. Why does a table without a dashed second row not work?
5. What does CommonMark solve?

## Before Moving On

You are ready for Chapter 9<!--ref:problem--> if you can:

- [ ] write a heading, a list, a link, a code block and a table from memory
- [ ] explain why Markdown suits Git better than a word-processor file
- [ ] name two mistakes that break Markdown and how to avoid them
- [ ] create and preview a `README.md`

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| The source-to-HTML results of every example | Both: rendered with markdown-it-py 4.2.0 (CommonMark preset, tables on); the book's build compares every example with the recorded output (`tools/check_md_examples.py`, `verification/ch08-markdown`); the same renderer reproduces all 655 examples of the CommonMark specification, version 0.31.2 (`research/commonmark-conformance.py`) | R131 |
| GitHub's extras (automatic links, task lists, tables) | Officially verified (docs only): GitHub's Markdown specification, version 0.29; GitHub's live rendering not observed | R132 |

## Where this leads

Chapter 9<!--ref:problem--> begins Part II, which explains the problem that version control solves. Chapter 42<!--ref:readme--> returns to README files in depth, and to what GitHub adds to Markdown.
