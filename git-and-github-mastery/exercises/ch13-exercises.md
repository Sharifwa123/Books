# Chapter 13 exercises — Installing Git

Attempt each exercise before you open `solutions/ch13-solutions.md`. Use your practice folder; nothing here can damage your computer.

## Level 1 — Guided

**1.1 Check.** Open a new terminal and run `git --version`. *Expected result:* a line starting `git version` followed by numbers. If you see "command not found", follow section 13.4 or 13.5 for your system, then check again from a **new** terminal.

**1.2 Locate.** Run `command -v git` (in Command Prompt: `where git`). Write down where the program was found.

**1.3 Identify yourself.** Run the three `git config --global` commands of section 13.7 with your own name and address, then `git config --global --list`. *Expected result:* your three settings, with the setting name `init.defaultbranch` in lower case.

## Level 2 — Partially guided

**2.1 Read the summary.** Run `git commit -h` and find the option that lets you supply the message on the command line. Hint: look for `-m`. Write it down with its one-line description.

**2.2 Which help?** For each need, say whether `git help <command>`, `git <command> -h` or the online documentation is best, and why: (a) you want the full reference for `git merge` and manual pages are installed; (b) you are on a train with no manual pages; (c) you want to compare behaviour across versions.

## Level 3 — Independent

**3.1** Explain to a friend, in four sentences, why they need to set `user.name` and `user.email` before their first commit, and what "global" means.

## Level 4 — Professional scenario

**4.1** Your organization has 20 new employees who will each install Git. Write a one-page checklist for them: where to download it from, how to verify the installation, which three settings to make, and what to do if `git` is "not found". Add one item about safe installation from Chapter 1<!--ref:computer-->.

## Level 5 — Troubleshooting

**5.1** A learner installed Git, opened the *same* terminal window that was already open, and typed `git --version`. The message says the command is not found. Explain why, and give the fix.

**5.2** A learner runs `git --version` and sees an older version than the one they just installed. What might be happening, and which command shows which program actually runs?
