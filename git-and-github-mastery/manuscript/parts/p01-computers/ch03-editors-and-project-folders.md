---
key: editors
number: 3
tag: Core
first_read: full
status: draft
requires: [files]
ledger: [R117, R133]
---
# Chapter 3 — Editors and Project Folders [Core]

**In this chapter**

- why some files are "plain text" and others are not, and why Git cares
- the difference between a word processor and a text editor
- what to look for in a code editor
- what a "software project" is, using a small website as the running example
- how to get the Sunrise Bakery starter files ready for the rest of the book

**Before you start.** Chapter 2<!--ref:files--> (files, folders, paths, extensions). You should be able to create a folder and see file extensions.

---

## 3.1 Two kinds of file contents

Chapter 2<!--ref:files--> said that a file is a named collection of information. The *kind* of information inside decides which programs can open it and, later, how well Git can help you with it.

For this book, you need only two kinds.

> **New term: plain text.** Information stored as ordinary characters (letters, digits, punctuation, spaces and line breaks) with nothing else added: no fonts, no colours, no pictures, no page layout.

> **New term: binary file.** Any file whose contents are not plain text: photographs, music, compressed archives, word-processor documents and programs are all binary files.

A **text file** is a file made of plain text. When you open one in a suitable program you see exactly the characters that are in it, and nothing hidden.

### 3.1.1 What is inside a word-processor document?

A document from a word-processor program looks like text on a page, but the file is more than the words. It also holds fonts, spacing, page size, styles, and sometimes a history of tracked changes. To keep all of that, the file is *packaged*.

The test below, run in the book's test environment, creates a one-sentence document and compares it with a plain text file that holds the same sentence:

```text
plain text file: 27 bytes; starts with: b'Fresh bread '
word-processor file starts with bytes: b'PK' (the ZIP signature 'PK')
is it a ZIP archive? True
contains parts (first four, sorted): [Content_Types].xml, _rels/.rels, customXml/_rels/item1.xml.rels, customXml/item1.xml
has word/document.xml: True
visible text is about 26 bytes; the file holds far more than the text
file is larger than its text: True
```

*Example output from `verification/ch03-editors/docx_vs_txt.py` (produced with a widely used Python library for creating `.docx` files; you do not need to run it).*

Read the result. The plain text file is 27 bytes: the 26 characters of the sentence plus a line break. The word-processor file begins with the two bytes `PK`, which mark a **ZIP archive**, a container that packs several files into one. Inside the container are separate parts, one of which (`word/document.xml`) holds the words, wrapped in markup. The sentence is a tiny part of a much larger package.

> **New term: ZIP archive.** A single file that contains other files in compressed form. Many document formats, including modern word-processor formats, use a ZIP archive as their outer package.

> **Verification pending [R117].** The test above shows what one library produces. The published standards that define the word-processor format have not yet been consulted, so the statement "modern word-processor files are packaged as ZIP archives of XML parts" is tested for one tool but not yet checked against the standard.

**Why this matters for Git.** Git is superb at tracking plain text, and it can show you *exactly which lines changed*. For a packaged binary file it can still keep every version, but by default it cannot show a readable difference: it can only say "this file changed". This is why the projects in this book use text files, and why documents that you want to track closely (for example this book's own chapters) are written in a text format called Markdown (Chapter 8<!--ref:markdown-->) instead of a word-processor format.

**When not to use plain text.** If you need pictures, complicated layout, or colleagues who expect a word-processor file, use one, and use Git for what it does best, keeping every version. Choose plain text where you can, and where readable differences matter.

---

## 3.2 Editors

> **New term: text editor.** A program for creating and changing plain text files.

> **New term: word processor.** A program for writing formatted documents, with fonts, page layout and pictures, that normally saves in a packaged (binary) format.

The two look similar and are used differently.

| | Text editor | Word processor |
|---|---|---|
| Saves | Only the characters you type | Characters plus formatting and page information |
| Result | Plain text file | Packaged binary file |
| Good for | Code, notes, configuration, Markdown | Letters, reports, anything printed |
| Git can show line-by-line differences | Yes | No |

### 3.2.1 Code editors

A **code editor** is a text editor with extra help for writing code and other structured text.

> **New term: code editor.** A text editor with features for structured text such as software: coloured text, line numbers, tools for searching many files, and often a built-in terminal (a window for typing commands, introduced in Chapter 7<!--ref:terminal-->).

The features that will help you in this book:

- **Line numbers.** Git messages refer to lines. Seeing numbers makes them easy to follow.
- **Syntax highlighting.** The editor colours words according to their role, so mistakes stand out.

  > **New term: syntax highlighting.** Colouring different parts of text (for example, tags, words and comments) so that its structure is easy to see.

- **Show invisible characters.** You can display spaces, tabs and line endings. Chapter 4<!--ref:text--> explains why you will want this.
- **Choice of encoding and line endings.** You can say how characters are stored in the file (Chapter 4<!--ref:text--> explains both terms).
- **Open a whole folder.** You see all the files of a project in a side panel.
- **Search across files.** You can find every use of a word in the project.

### 3.2.2 Choosing one

This book does not depend on any particular editor, and it does not recommend a brand. Many good ones exist for every operating system, and free ones are available. Pick one that:

1. is available for your operating system and is maintained by its makers (check when the last update was released);
2. can open a folder and show line numbers;
3. lets you choose **UTF-8** encoding (Chapter 4<!--ref:text-->) and see line endings;
4. you feel comfortable using.

> **Security note.** An editor is a program you install. Apply the rules from Chapter 1<!--ref:computer-->: download it from its makers' own website or your system's official source. Extensions that some editors let you add are more programs; add only those you need, from the official catalogue.

**A trap to avoid.** Do not write code or configuration files in a word processor. Word processors may replace straight quotation marks with curly ones ("like this"), add invisible formatting, and change dashes, and any of these can make a program refuse to run. If a file that should be plain text will not work, check first that it was not edited in a word processor.

---

## 3.3 Saving and opening

When you *open* a file, the editor copies it from storage into memory (Chapter 1<!--ref:computer-->). When you *save*, it copies your changes from memory back to storage. Until you save, your changes exist only in memory and would be lost in a power cut.

Watch for these signals:

- Most editors mark an unsaved file, often with a dot or asterisk beside its name in the tab.
- **Save** overwrites the file with your changes. **Save As** creates a *new* file (choose the name and folder carefully) and leaves the original untouched.
- Some editors **auto-save**. This is convenient, but it means every keystroke may go to storage. That is one more reason to keep history with Git, which records *deliberate* versions.

> **UI-VERSION NOTE.** Menu names and keyboard shortcuts differ between editors and operating systems. If you cannot find "Save As" or the encoding setting, search the editor's help for those words.

---

## 3.4 What a software project is

> **New term: software project.** A collection of files, kept together in one folder, that make up one piece of work: a website, an application, a set of documents, or a tool.

You have used the word "project" loosely before. Here it has a precise meaning, because Git will track *one project folder at a time*.

The files of a project fall into a few groups. Learning to see the groups now will make Chapter 18<!--ref:tracking--> (deciding which files Git should track) easy.

| Group | Meaning | Example in the Sunrise Bakery site |
|---|---|---|
| **Source files** | Written by people; the real work | `index.html`, `menu.html`, `contact.html`, `css/style.css`, `images/logo.svg` |
| **Documentation** | Explains the project | `README.md` |
| **Assets** | Pictures, sounds, fonts | `images/logo.svg` |
| **Configuration** | Settings that tune the project | (none yet) |
| **Generated files** | Made automatically from source files by a tool | (none yet; a later chapter adds some) |
| **Dependencies** | Other people's software your project uses | (none) |

> **New term: source code (source files).** The files, written by people, from which a project is made. For a website, these include the pages and stylesheets.

Generated files and dependencies can be huge and can be rebuilt, so they usually should *not* be tracked. You will see how to tell Git to ignore them.

---

## 3.5 The Sunrise Bakery project

The book's running example is a small website for a fictional business, **Sunrise Bakery**. It has three pages, a stylesheet and a logo, and it is the project you will track, branch, share and automate for the rest of the book.

You do not need to write code. You need to understand what kind of files these are, so that when Git talks about them, you know what you are looking at.

| File | Kind | What it does |
|---|---|---|
| `index.html`, `menu.html`, `contact.html` | HTML | The pages: their words and structure |
| `css/style.css` | CSS | The appearance: colours, spacing |
| `images/logo.svg` | SVG | A small picture, stored as text |

> **New term: HTML.** A text format for web pages. It marks up text with tags such as `<h1>` (a main heading) so that a browser (the program for viewing web pages) knows how to display it.
>
> **New term: CSS.** A text format that describes how web pages should look: colours, fonts, spacing.

Here is the start of `index.html`. Read the idea: everything is text, and the tags in angle brackets describe the words.

```html
<header>
  <img src="images/logo.svg" alt="Sunrise Bakery logo" width="80" height="80">
  <h1>Sunrise Bakery</h1>
  <nav>
    <a href="index.html">Home</a>
    <a href="menu.html">Menu</a>
    <a href="contact.html">Contact</a>
  </nav>
</header>
<main>
  <h2>Fresh bread every morning</h2>
  <p>We bake bread, rolls and small cakes from six o'clock, every day except Sunday.</p>
</main>
```

Notice the paths: `images/logo.svg` and `menu.html` are **relative paths** (Chapter 2<!--ref:files-->). The page finds its logo by directions from where the page itself lives. If you moved `index.html` out of its folder without moving the `images` folder, the logo would disappear. That is an everyday example of why *the whole folder, kept together,* is the project.

The starter files have been checked mechanically: every page has balanced tags, every link between pages and every reference to the stylesheet and logo points at a file that exists, and the logo is well-formed.

> **Verification pending [R133].** The starter files were checked by a script of the book's own (`verification/companion-starter/check_starter.py`). They have not yet been opened in a range of browsers and screen readers.

### 3.5.1 Getting the starter files

The starter files come with the book, in the folder `companion/sunrise-bakery-starter`. Because you have not installed Git yet, the simplest way to obtain them is as a single ZIP archive.

> **[BOOK DOWNLOAD LOCATION: to be supplied by the publisher.]** This placeholder marks where the edition will tell you where to download the companion files. Until then, use the copy that came with your edition.

Once you have the ZIP archive:

1. Put it inside your practice folder, `sharif-git-lab` (Chapter 2<!--ref:files-->).
2. **Extract** it (also called "unzip"): most file managers offer "Extract" or "Extract all" when you click the archive. The exact name of the command varies.
3. Rename the extracted folder `sunrise-bakery`, if it has a different name.

> **Try it.** Open `sunrise-bakery/index.html` by double-clicking it. Your web browser should open it as a local page: a heading, a short paragraph and three menu links, styled with a warm yellow bar.
>
> Now open `index.html` in your **text editor** instead (usually a right-click and "Open with"). Change the words "Fresh bread every morning" to "Fresh bread and rolls every morning". Save the file. Switch to the browser window and reload the page.
>
> *Expected result:* the browser shows your new words. This is the whole loop of software work: edit text, save, look at the result.

> **Deep.** The page opened straight from your storage; no server was involved. Chapter 5<!--ref:internet--> explains what a web server adds.

---

## 3.6 Why a project is a folder, and why that matters next

You have now seen the idea that runs through the rest of the book: **a project is a folder of mostly text files, kept together, that change over time**.

Change is the problem. Imagine that you edit `menu.html` today, your friend edits it tomorrow, and next week you realise that last Tuesday's version had a price you need. Without a history, you have a copy of a copy of a copy called `menu_final_v2_REAL.html`. Part II explains the problem, and Part III solves it with Git.

---

## Checkpoint

## What You Learned

- Plain text files contain only characters; word-processor documents are packaged binary files whose text is a small part of the whole.
- Git can show readable line-by-line differences for text files but only "changed" for binary files.
- A text editor saves plain text; a code editor adds line numbers, colouring, invisible-character display and folder tools.
- Do not edit code or configuration in a word processor.
- Opening copies a file from storage into memory; saving copies it back.
- A software project is a folder of files: source files, documentation, assets, configuration, generated files and dependencies.
- The Sunrise Bakery project is a three-page website made of HTML, CSS and SVG text files, with a README.

## New Vocabulary

- **Plain text**: information stored as ordinary characters with no formatting.
- **Binary file**: a file that is not plain text, such as a photo or word-processor document.
- **ZIP archive**: one file that holds other files in compressed form.
- **Text editor**: a program for plain text files.
- **Word processor**: a program for formatted documents.
- **Code editor**: a text editor with features for writing structured text and software.
- **Syntax highlighting**: colouring parts of text by their role.
- **Software project**: the folder of files that makes up one piece of work.
- **Source code (source files)**: the human-written files from which a project is made.
- **HTML**: a text format that marks up web pages.
- **CSS**: a text format that describes how web pages look.

## Commands Learned

None. (Opening, editing and saving files in a graphical editor need no commands.)

## Common Mistakes

1. **Editing code in a word processor.** Curly quotes and hidden formatting can break the file.
2. **Forgetting to save, then expecting the browser to show the change.** Save, then reload.
3. **Moving one file out of its project folder.** Relative paths such as `images/logo.svg` will no longer find their targets.
4. **Choosing "Save As" and losing track of which file is which.** Prefer "Save" for the project files and a history tool for versions.
5. **Renaming a file's extension to change its type** (Chapter 2<!--ref:files-->).

## Practice

Do the exercises in [`exercises/ch03-exercises.md`](../../../exercises/ch03-exercises.md).

## Self-Test

1. Give two differences between a text editor and a word processor.
2. Why does Git show readable differences for `menu.html` but only "changed" for a `.docx` file?
3. What is a software project, in one sentence?
4. Sort these into source files, documentation, assets and generated files: `README.md`, `style.css`, `logo.svg`, a folder of files produced automatically by a build tool.
5. The logo disappears when you move `index.html` to another folder. Why?

## Before Moving On

You are ready for Chapter 4<!--ref:text--> if you can:

- [ ] open a folder in a text editor and see line numbers
- [ ] edit `index.html`, save it, and see the change in the browser
- [ ] say why a word-processor file is not plain text
- [ ] name the files in the Sunrise Bakery project and what each does

## How this chapter was checked

| Claim | Evidence class | Ledger |
|---|---|---|
| A word-processor document generated by a common library is a ZIP archive containing `word/document.xml`, far larger than its text | Locally tested (`verification/ch03-editors/docx_vs_txt.py`, python-docx 1.2.0); standard not yet consulted | R117 |
| The starter files have balanced tags, resolving links and a well-formed logo | Locally tested (`verification/companion-starter/check_starter.py`, run in CI) | R133 |
| Editor features and cautions (curly quotes, encoding choice) | General guidance; no product-specific claim is made | none |

## Where this leads

Chapter 4<!--ref:text--> looks *inside* text files: characters, encodings and line endings, the invisible details that sometimes make the same file behave differently on two computers. Chapter 7<!--ref:terminal--> introduces the terminal, and Chapter 8<!--ref:markdown--> introduces Markdown, the text format in which READMEs and this book are written.
