# Preface

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
