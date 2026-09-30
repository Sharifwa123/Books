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

**Published by SHARIF TECHNOLOGIES**

*Knowledge Is Power*

1st Edition
""")

w("manuscript/front-matter/01-copyright-page.md", """# Copyright and Notices

Copyright © [YEAR] SHARIF TECHNOLOGIES. All rights reserved.

> **Licence: undecided.** The publisher intends to release the book text and its code samples under licences that permit reading, downloading and sharing on stated conditions. **The wording of any licence has not been inserted, because it has not yet been verified and decided.** Until the publisher adds it here, treat the book as protected by copyright with all rights reserved. Copyright is not removed by making a work public or free to read: **the book is not "copyright-free"**. Chapter [[licences]] explains the difference between copyright and a licence and the seven questions to ask of any work: who owns it, and whether you may read it, download it, redistribute it, modify it, use it commercially, or reuse its code.

| | |
|---|---|
| Title | Git & GitHub: From Zero to Mastery |
| Author | Sharif Tingane Issah |
| Publisher | SHARIF TECHNOLOGIES |
| Edition | 1st Edition |
| ISBN | [ISBN TO BE ASSIGNED] |
| Publication date | [PUBLICATION DATE] |
| Technical information verified | [MONTH YEAR OF FINAL VERIFICATION] (see Appendix N for what was checked and what remains open) |
| Publisher address | [SHARIF TECHNOLOGIES REGISTERED ADDRESS] |
| Website and contact | [OFFICIAL WEBSITE] · [OFFICIAL PUBLISHING EMAIL] |

## Disclaimer

This book is educational. Commands change the state of your computer and your repositories: understand a command before you run it, use a practice folder, and make backups. Operations involving secrets, history rewriting and access control need particular care. Behaviour can differ between operating systems, versions, configurations and future releases of Git and GitHub. The book was tested on the versions named in Appendix N; the platform's own current documentation prevails. **Nothing in this book is legal advice**, and the chapter on licences explains how licences are described, not what they mean for your situation.

## Trademarks and non-affiliation

This book is an independent educational publication by SHARIF TECHNOLOGIES. It is not affiliated with, endorsed by, sponsored by, or published by Git, GitHub, Microsoft, or any other third party mentioned. Git, GitHub, Microsoft, Linux, Windows, macOS, Docker, GitLab, Bitbucket and other names may be trademarks of their respective owners.

## Third-party material

Where the book quotes short passages from official documentation, it names the source; those passages remain under their own terms. Names, prices and addresses in examples are made up.
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
7. **Nothing is invented.** Where a fact was not supplied or could not be verified (an ISBN, an address, a licence wording, a biography), the book leaves a visible placeholder.

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
 "## What you need", "",
 "A computer (Windows, macOS or Linux), a text editor, a terminal, an internet connection for the later parts, and a GitHub account from Part V onwards. Chapter [[install]] installs Git. Some tools of later chapters are installed when needed.", "",
 "## If you are short of time", "",
 "Read the First-Read Path, do its projects, and run the assessment (Chapter [[assessment]]). Then read the rest as you need it.", ""]
w("manuscript/front-matter/04-how-to-use-this-book.md", "\n".join(L))

w("manuscript/back-matter/author-and-publisher.md", """# Author and Publisher

## The author

**Sharif Tingane Issah.**

[AUTHOR BIOGRAPHY: to be supplied by the publisher. No qualifications, employment, awards or memberships are stated here, because none were supplied.]

## The publisher

**SHARIF TECHNOLOGIES**

*Knowledge Is Power*

[Address, website, email and contact details: to be supplied by the publisher.]

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
