# 00 — Book Concept and Target Learner

## Concept
A single, self-contained textbook that takes a reader with no computer background to professional-level Git and GitHub practice. It teaches *understanding* (the model behind Git, the reasons behind GitHub features) before *commands*, and it uses practical, realistic projects rather than toy files.

## Title candidates
Working title must not imply GitHub affiliation and should avoid generic "AI-book" phrasing.

| # | Title | Subtitle | Notes |
|---|-------|----------|-------|
| 1 (recommended) | **Git & GitHub: From Zero to Mastery** | A Practical, Beginner-to-Professional Guide to Version Control, Collaboration and Automation | Clear, searchable; matches the user's suggestion |
| 2 | **Version Control from First Principles** | Learn Git and GitHub by Understanding How They Work | More distinctive; less searchable |
| 3 | **Track, Branch, Ship** | Git and GitHub for Complete Beginners and Working Professionals | Memorable; needs a strong subtitle |

**Decision (recorded):** title 1 selected, with the long subtitle in publishing/metadata.md.

## Presentation
- Written by Sharif Issah Tingane
- Published by SHARIF TECHNOLOGIES
- *Knowledge Is Power*
- Includes a non-affiliation notice (see 07).

## Target learner profile
**Primary:** an adult or older student who has used a phone or computer casually but has never used a terminal, written code, or heard of version control.

**Secondary:** self-taught developers who use a handful of memorised Git commands and want real understanding; junior developers preparing for team work; small-business/technical staff who maintain documentation or websites.

**Assumptions (minimum):** can read technical English at a general level; has access to a computer (Windows, macOS or Linux) and internet; can install software with administrator permission.

**Explicitly NOT assumed:** programming, terminal use, networking knowledge, English technical vocabulary, prior use of any developer tool.

**Learner anxieties the book must address:** fear of breaking things, fear of the terminal, vocabulary overload, fear of losing work. Response: a safe-practice sandbox convention, an early recovery mindset ("Git rarely loses committed work"), and gradual vocabulary.

## Pedagogical approach
Each concept follows the prompt's sequence: what → why → problem solved → real-life look → analogy → technical explanation → example → exercise → expected result → common mistakes → recovery → when to use / not use → alternatives → connections → professional usage. Chapters may compress the sequence but must not skip *why*, *mistakes* and *recovery*.

## Conventions the book will use
- **New term:** callout at first introduction, mirrored in the glossary.
- **⚠️ CAUTION** callout for destructive/history-rewriting commands (`reset --hard`, `clean`, `push --force`, `push --force-with-lease`, `rebase`, history filtering).
- **UI-VERSION NOTE** callout wherever a GitHub screen may change; teach the concept first.
- **Verified-on** tag on each GitHub-feature section (date filled in only after checking official docs).
- Commands in fenced code blocks; output shown separately and marked as *example output*.
- Diagrams in text/Mermaid/SVG so they render in print, PDF, EPUB and web.
- A sandbox directory `~/sharif-git-lab/` is used for all exercises so nothing touches real work.

## Book-wide safety rule
No exercise asks the learner to publish a real secret. Secret-leak exercises use clearly fake tokens (e.g. `FAKE_TOKEN_DO_NOT_USE_0000`) and never real credentials.
