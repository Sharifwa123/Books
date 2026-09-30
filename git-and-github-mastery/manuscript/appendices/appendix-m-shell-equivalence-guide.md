# Appendix M — Git Bash / PowerShell / Command Prompt Equivalence Guide

Git commands are the same in every shell. What differs is the surrounding shell: file commands, variables, quoting, paths and line endings. This appendix extends the table of Chapter 7<!--ref:terminal-->.

> **Partly checked [R127].** The PowerShell cmdlet names, aliases and the `-Force` and `-Recurse` parameters shown here were checked against Microsoft's PowerShell 7.5 reference (the `MicrosoftDocs/PowerShell-Docs` repository); an earlier draft wrongly listed `mkdir` as an alias of `New-Item`, and the reference lists only `ni`. **Nothing was run on Windows**, and the Command Prompt column was not checked against Microsoft's documentation. Check each entry on your own machine. The Bash and zsh column was run throughout the book.

## M.1 File and folder commands

| Task | Bash / zsh / Git Bash | PowerShell | Command Prompt |
|---|---|---|---|
| Where am I? | `pwd` | `Get-Location` (alias `pwd`) | `cd` |
| List files | `ls` (`ls -a` shows hidden) | `Get-ChildItem` (alias `ls`; `-Force` shows hidden) | `dir` (`dir /a`) |
| Change folder | `cd folder` | `Set-Location folder` (alias `cd`) | `cd folder` |
| Make a folder | `mkdir folder` | `New-Item -ItemType Directory folder` (alias `ni`) | `mkdir folder` |
| Show a file | `cat file` | `Get-Content file` (alias `cat`) | `type file` |
| Copy | `cp a b` | `Copy-Item a b` | `copy a b` |
| Move or rename | `mv a b` | `Move-Item a b` | `move a b` or `ren a b` |
| Delete a file | `rm file` | `Remove-Item file` | `del file` |
| Delete a folder and its contents | `rm -r folder` | `Remove-Item -Recurse folder` | `rmdir /s folder` |
| Search text in files | `grep TEXT file` | `Select-String TEXT file` | `findstr TEXT file` |

**Deleting is permanent in all three.** Check the path before you press Enter (Chapter 7<!--ref:terminal-->).

## M.2 Variables, quoting and paths

| Topic | Bash / zsh / Git Bash | PowerShell | Command Prompt |
|---|---|---|---|
| Show a variable | `echo "$HOME"` | `$env:USERPROFILE` | `echo %USERPROFILE%` |
| Set a variable for one command | `NAME=value command` | `$env:NAME = "value"` first | `set NAME=value` first |
| Quote text with spaces | `'single'` or `"double"` | `'single'` or `"double"` | `"double"` |
| Path separator | `/` | `\` (and `/` often works) | `\` |
| Home folder | `~` | `~` | `%USERPROFILE%` |
| Chain commands | `a && b` | `a; b` (newer versions also accept `&&`) | `a & b` or `a && b` |

**Git itself accepts `/` in paths on every system.** The book's Git commands use `/`.

## M.3 Things that differ for Git

- **Line endings.** Windows tools often use CRLF, and Linux and macOS use LF; Git can convert (`core.autocrlf`, `.gitattributes`). Chapters 4<!--ref:text--> and 32<!--ref:custom--> explain and record the effect.
- **Quotes in commit messages.** Use double quotes on Windows shells; single quotes do not group text in Command Prompt.
- **Executable scripts.** The recordings use `sh SCRIPT` to run scripts; on Windows use Git Bash for these.
- **Symbolic links.** Their creation on Windows may need special permission; the book's deployment recording (Chapter 72<!--ref:deploy-->) uses Linux.
- **`sha256sum`** (Chapter 63<!--ref:secpractice-->) is Linux; macOS has `shasum -a 256`; PowerShell has `Get-FileHash`.

## M.4 Which shell should I use?

The book uses one path: **Bash or zsh syntax**. On Windows, the simplest way to follow it is **Git Bash**, which is installed with Git for Windows. Git is not Git Bash: Git is the tool; Git Bash is a shell (Chapter 7<!--ref:terminal-->).
