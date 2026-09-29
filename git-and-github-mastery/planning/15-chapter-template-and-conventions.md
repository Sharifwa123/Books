# 15 — Chapter Template and Manuscript Conventions

Enforced by `tools/check_manuscript.py` (run in CI).

## File locations
- Chapter: `manuscript/parts/pNN-<slug>/chNN-<key-slug>.md` (NN = part / chapter number, zero-padded)
- Exercises: `exercises/chNN-exercises.md` (five levels) · Solutions: `solutions/chNN-solutions.md`
- Diagrams: `diagrams/chNN-<name>.mmd` (Mermaid text source, embedded in the chapter as a fenced `mermaid` block with a text description)
- Glossary source of truth: `glossary/glossary-master.csv`
- Verification scripts for chapter commands: `verification/chNN-<key>/` (script + recorded output; re-run in CI)

## Front matter (required)
```
---
key: computer            # must exist in tools/toc_data.py
number: 1                # must equal the generated chapter number
tag: Core                # Core | Deep (must equal toc_data)
first_read: full         # full | part | later (must equal toc_data)
status: draft            # draft | reviewed | verified
requires: []             # must equal toc_data prerequisites
ledger: [R110, R111]     # research-ledger ids that this chapter's claims rely on
---
```

## Body
1. `# Chapter N — Title [Core]`
2. **In this chapter** (bullets) and **Before you start** (what earlier chapters must have taught).
3. Numbered sections `N.1`, `N.2` … Each concept follows: what → why → problem solved → real-life picture → analogy → technical explanation → example → try it → expected result → common mistakes → recovery → when to use / not use → alternatives → connection to earlier chapters → professional use. A section may compress the sequence but never omits *why*, *what can go wrong* and *how to recover*.
4. Checkpoint, in this exact order: `## What You Learned`, `## New Vocabulary`, `## Commands Learned`, `## Common Mistakes`, `## Practice`, `## Self-Test`, `## Before Moving On`.
5. `## How this chapter was checked` (claim → evidence class → ledger id) and `## Where this leads`.

## Callouts (blockquotes starting with a bold label)
- `> **New term: X.**` first definition of a term (must also be in the glossary with `first_chapter` = this chapter).
- `> **⚠️ CAUTION.**` destructive or history-rewriting actions; say exactly what can be lost.
- `> **Security note.**`
- `> **UI-VERSION NOTE.**` interface details that change; concept first.
- `> **Verification pending [R###].**` claim not yet officially verified; counted by the release gate.
- `> **Try it.**` a hands-on step in the sandbox; followed by *Expected result*.
- `> **Deep.**` optional [Deep] material inside a Core chapter.

## Language rules
Clear international English; define a term before relying on it; no filler; no "etc." / "and so on" in place of teaching (enforced); no invented facts; UK/US spelling: this book uses **British** spelling except in quoted commands, product names and file formats (e.g. `color` in CSS stays as is).

## Platform convention
Primary shell: **bash** (Git Bash on Windows; Terminal on macOS/Linux). Commands that differ on PowerShell/Command Prompt are shown separately and carry a verification label. Commands are shown in fenced `bash` blocks; program output in fenced `text` blocks headed *Example output*.

## Sample project
Fictional small business **Sunrise Bakery** (folder `sunrise-bakery`, files in `companion/sunrise-bakery-starter/`). No real business is meant.

## Release gate
`python3 tools/check_manuscript.py --release` fails while any `Verification pending` marker remains, any chapter is `draft`, or any chapter `ledger` id is not officially verified. CI runs the non-release mode.
