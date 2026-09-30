#!/usr/bin/env python3
"""Builds front matter and back-matter shells from publishing/metadata.md and tools/toc_data.py:
  manuscript/front-matter/00-title-page.md, 01-copyright-page.md, 02-contents.md, 03-preface.md, 04-how-to-use-this-book.md
  manuscript/back-matter/author-and-publisher.md
Placeholders stay bracketed: nothing is invented (ISBN, address, dates, legal identifiers, biography)."""
import os, sys, collections
sys.path.insert(0, os.path.dirname(__file__))
import toc_data as T
root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
def w(rel, text):
    p = os.path.join(root, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(text); print("wrote", rel, len(text.split()), "words")
C = T.C
num = {c[1]: i + 1 for i, c in enumerate(C)}

w("manuscript/front-matter/00-title-page.md", """# Git & GitHub: From Zero to Mastery

## A Complete Beginner-to-Expert Guide to Version Control, Collaboration, Automation, Security, and Modern Software Development

**Written by Sharif Tingane Issah**

**SHARIF TECHNOLOGIES**

*Knowledge Is Power*

1st Edition
""")

w("manuscript/front-matter/01-copyright-page.md", """# Copyright and Notices

Copyright © 2026 SHARIF TECHNOLOGIES. All rights reserved except for the permissions expressly granted under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License.

This book's original text is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0):

<https://creativecommons.org/licenses/by-nc-sa/4.0/>

Under this license, readers may share and adapt the licensed book material for noncommercial purposes, provided that the applicable attribution and ShareAlike requirements are followed. Commercial use requires separate permission from the rights holder.

Code examples contained in this book are separately licensed under the MIT License unless a particular example identifies another applicable licence or third-party source.

The licence applies only to material for which the stated rights holder has authority to grant the licence. Third-party material, trademarks, screenshots, quotations, logos, and other material identified as belonging to their respective owners are not automatically covered by this licence and may be subject to separate rights or permissions.

This licensing notice is a plain-language summary and does not replace the terms of the applicable Creative Commons or MIT licence.

## What the licence does and does not mean

**The book is copyrighted.** It is not "copyright-free", not in the public domain and not owned by everyone. Making a book free to read or to download does not remove copyright; a licence is a set of permissions that the rights holder grants. Keep these questions apart, as Chapter [[licences]] teaches: who owns the work; whether you may read it, download it, redistribute it, modify it, use it commercially, or reuse its code. For this book the answers are: the rights holder is named above; you may read and download it; you may redistribute and adapt the text for noncommercial purposes under the conditions of the licence; commercial use needs permission; and the code examples may be reused under the MIT License.

| | |
|---|---|
| Title | Git & GitHub: From Zero to Mastery |
| Author | Sharif Tingane Issah |
| Published | Under the SHARIF TECHNOLOGIES imprint |
| Edition | 1st Edition |
| ISBN | [ISBN TO BE ASSIGNED] |
| Publication date | [PUBLICATION DATE] |
| Technical information verified | [MONTH YEAR OF FINAL VERIFICATION] (see Appendix N for what was checked and what remains open) |
| Website | www.shariftechnologies.online |
| Contact | [OFFICIAL PUBLISHING EMAIL] |

## Disclaimer

This book is educational. Commands change the state of your computer and your repositories: understand a command before you run it, use a practice folder, and make backups. Operations involving secrets, history rewriting and access control need particular care. Behaviour can differ between operating systems, versions, configurations and future releases of Git and GitHub. The book was tested on the versions named in Appendix N; the platform's own current documentation prevails. **Nothing in this book is legal advice**, and the chapter on licences explains how licences are described, not what they mean for your situation.

## Trademarks and non-affiliation

This book is an independent educational work by Sharif Tingane Issah, issued under the SHARIF TECHNOLOGIES name. It is not affiliated with, endorsed by, sponsored by, or published by Git, GitHub, Microsoft, or any other third party mentioned. Git, GitHub, Microsoft, Linux, Windows, macOS, Docker, GitLab, Bitbucket and other names may be trademarks of their respective owners, and this book claims no rights in them. The name SHARIF TECHNOLOGIES is not licensed by the licences above.

## Third-party material

Where the book quotes short passages from official documentation, it names the source; those passages remain under their own terms and are not covered by this book's licence. Names, prices and addresses in examples are made up.

The PDF editions are set in the DejaVu fonts. Copyright (c) 2003 by Bitstream, Inc. All Rights Reserved. Bitstream Vera is a trademark of Bitstream, Inc. DejaVu changes are in the public domain.
""")

# Contents
L = ["# Contents", ""]
L += ["**Front matter:** Copyright and Notices · Preface · How to Use This Book", ""]
by_part = collections.OrderedDict()
for i, c in enumerate(C): by_part.setdefault(c[0], []).append((i + 1, c))
for pi, (pn, pt) in enumerate(T.PARTS):
    L += [f"## Part {pn} — {pt}", ""]
    for n, c in by_part.get(pi, []):
        L.append(f"- Chapter {n}<!--ref:{c[1]}-->. {c[2]} [{c[3]}]")
    L.append("")
L += ["## Appendices", ""] + [f"- Appendix {a}. {t}" for a, t in T.APPENDICES] + ["", "## Back matter", "", "- Glossary", "- Index of terms and commands", "- Author and publisher", ""]
w("manuscript/front-matter/02-contents.md", "\n".join(L))

w("manuscript/front-matter/03-preface.md", """# Preface

Most books on Git and GitHub tell you what to type. This one tries to give you a way to know that what you type works, and to know how much to trust what it says.

## Who this book is for

For someone who has never used version control, and perhaps has never used a terminal. It starts with what a computer is, what a file is and what a path is, and ends with recovery playbooks, security, automation and a final assessment. If you already use Git, the chapters are still useful as a check of your understanding, and the **Deep** chapters go further.

## How this book was checked

The book follows a small set of rules, written down before the chapters:

1. **Commands are run, not remembered.** Every command shown was executed in a sandbox, in Bash and in zsh, and the output in the book is the recorded output. A machine check compares each recorded line in the text with the recording, and the recordings are re-run in continuous integration on newer versions of Git.
2. **Versions and dates are recorded.** Git behaviour is tied to the version tested; GitHub behaviour to the date and the documentation it was read from. Nothing is generalised beyond that.
3. **Official sources first.** Git behaviour was compared with Git's own documentation and source; GitHub behaviour with GitHub's documentation. Summaries by third parties are not substitutes, and when only one was available the text says so.
4. **Every claim has an evidence class:** officially verified, locally tested, both, time-sensitive, or needing re-verification. A locally tested claim is never called officially verified.
5. **Surprises are investigated before they are taught.** Where Git's behaviour and its manual disagreed, the book followed the behaviour and said so.
6. **Interface is taught as an idea first.** Screens change; principles last.
7. **Nothing is invented.** Where a fact was not supplied or could not be verified (an ISBN, a publication date, a contact address), the book leaves a visible placeholder. The author's biography states only what public evidence supports.

**What this book did not do.** Nothing was run on a live GitHub account by hand: statements about GitHub come from its documentation, and every chapter says so. Windows and macOS environments were not available for testing. Appendix N lists exactly what was checked, with what, and what is still open.

## A word on trust

Use the book the way it asks you to use everything else: run the commands, read the output, look at the date and compare with the current documentation. If you find that something differs, trust the source and let the book's ledger tell you where its claim came from.

*Sharif Tingane Issah*
""")

full = [(n, c) for n, c in [(i + 1, c) for i, c in enumerate(C)] if c[4] == "full"]
part = [(n, c) for n, c in [(i + 1, c) for i, c in enumerate(C)] if c[4] == "part"]
core = sum(1 for c in C if c[3] == "Core"); deep = sum(1 for c in C if c[3] == "Deep")
L = ["# How to Use This Book", "",
 f"The book has {len(C)} chapters in {len(T.PARTS)} parts, {len(T.APPENDICES)} appendices, a glossary and an index. Chapters are tagged **[Core]** ({core} of them) or **[Deep]** ({deep} of them).", "",
 "## Core and Deep", "",
 "- **[Core]** chapters are needed to progress. If you skip one, later chapters may not make sense.",
 "- **[Deep]** chapters matter for mastery but not for a first pass. You can skip a Deep chapter (or a section tagged Deep inside a Core chapter) and return to it later. No Core chapter depends on a Deep chapter.", "",
 "## Three ways to read", "",
 "1. **First-Read Path:** the shortest coherent route from no knowledge to using Git and GitHub for real work (below).",
 "2. **Second pass:** the remaining Core chapters.",
 "3. **Mastery pass:** all Deep chapters, then the challenges and the assessment.", "",
 f"## The First-Read Path", "",
 f"Read these {len(full)} chapters in full, and the sections named in the next table.", "",
 "| Order | Chapter | Tag |", "|---|---|---|"]
for k, (n, c) in enumerate(full, 1): L.append(f"| {k} | Chapter {n}<!--ref:{c[1]}-->. {c[2]} | {c[3]} |")
L += ["", "Read the first sections of these Core chapters on a first pass, and return later for the rest:", "", "| Chapter | Read first |", "|---|---|"]
for n, c in part: L.append(f"| Chapter {n}<!--ref:{c[1]}-->. {c[2]} | the opening sections and the summary |")
L += ["", "## Conventions", "",
 "- **Commands** appear in code blocks. A line that starts with `$ ` is a command you type (without the `$ `); the lines below it are the recorded output. Names, dates and hashes in the output differ on your computer.",
 "- **Bash and zsh.** The book uses one path: Bash or zsh syntax. On Windows, use **Git Bash**, which is installed with Git for Windows. *Git is not Git Bash*: Git is the tool, Git Bash is a shell. Appendix M compares the shells.",
 "- **Callouts.** *New term* introduces a word; *Caution* marks something that can lose work; *Security note* marks a security lesson; *Checked against...* says which source a claim was compared with.",
 "- **Practice.** Each chapter ends with a checkpoint, and has exercises in `exercises/` and solutions in `solutions/`. Try before you read the solutions.",
 "- **Projects.** Twelve projects are spread through the book; the last is the capstone.",
 "- **A practice folder.** Do everything in a folder you can throw away.", "",
 "## The companion repository", "",
 "The recorded command sessions, the research ledger, the verification scripts, the exercises and the files the chapters ask you to download are published in the book's companion repository: https://github.com/Sharifwa123/Books (folder `git-and-github-mastery`). The text of the book says when it names a file from there.", "",
 "## What you need", "",
 "A computer (Windows, macOS or Linux), a text editor, a terminal, an internet connection for the later parts, and a GitHub account from Part V onwards. Chapter [[install]] installs Git. Some tools of later chapters are installed when needed.", "",
 "## If you are short of time", "",
 "Read the First-Read Path, do its projects, and run the assessment (Chapter [[assessment]]). Then read the rest as you need it.", ""]
w("manuscript/front-matter/04-how-to-use-this-book.md", "\n".join(L))

w("manuscript/back-matter/author-and-publisher.md", """# Author and Publisher

## The author

Sharif Tingane Issah is the founder of SHARIF TECHNOLOGIES, the name under which Sharif writes and publishes software and books. Based in Ghana, Sharif describes the work on a public GitHub profile as software, artificial intelligence and cybersecurity, with the aim of building practical technology.

One project is Sharif NOVA, a programming language and toolchain that Sharif began as an independent project. It has an interpreter, a compiler for web pages and a web server mode, is released under the MIT licence, and was published on npm in September 2026. It is still at an early version number, and this note makes no claim about its use by others.

This book comes from the same habit. Every command in it was run and recorded, every statement about Git or GitHub is tied to the source it was checked against, and what could not be checked is written down. The working record is published beside the book, in its repository, so that readers can follow it.

## The imprint

**SHARIF TECHNOLOGIES** is the name under which Sharif Tingane Issah writes and publishes software and books. This book is published under the SHARIF TECHNOLOGIES imprint. The name is not licensed by the book's licences.

*Knowledge Is Power*

Website: www.shariftechnologies.online

## Final competency checklist

You have finished the book when you can tick every line. The assessment in Chapter [[assessment]] checks many of them for you.

- [ ] I can explain what a repository, a commit, a branch and a remote are.
- [ ] I can make a change on a branch, publish it and have it reviewed and merged.
- [ ] I can resolve a conflict by reading both sides.
- [ ] I can undo a mistake safely, and tell when a fix would be dangerous.
- [ ] I can recover lost commits with the reflog.
- [ ] I can keep secrets out of a repository, and I know what to do first if one leaks.
- [ ] I can write a small workflow that runs tests, with least privilege and pinned actions.
- [ ] I can tag and describe a release.
- [ ] I know the difference between a licence and copyright, and I know that choosing a licence is my decision.
- [ ] I read the current documentation before I rely on a fact about a platform.
""")

# expand the [[key]] cross-references in the generated files so that they are committed final
import subprocess, sys, os
subprocess.run([sys.executable, os.path.join(os.path.dirname(os.path.abspath(__file__)), "resolve_refs.py"), "--expand"], check=True)
