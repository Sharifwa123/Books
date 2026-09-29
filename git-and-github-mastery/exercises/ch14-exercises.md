# Chapter 14 exercises — Configuration Scopes and Environments

Attempt each exercise before you open `solutions/ch14-solutions.md`. Work in a new practice folder, and do not change settings you do not understand.

## Level 1 — Guided

**1.1 Where does it come from?** In any repository, run `git config --show-origin --show-scope user.email`. *Expected result:* one line with a scope, a file and your address.

**1.2 Local beats global.** Create a repository (`mkdir scope-lab`, `cd scope-lab`, `git init`). Set a *different* local email with `git config --local user.email "lab@example.org"`. Show the effective value, then all values with `--get-all`. *Expected result:* the effective value is the local one; `--get-all` lists both.

**1.3 One command only.** Use `git -c user.email="temp@example.invalid" config user.email` and then `git config user.email` without `-c`. *Expected result:* the first prints the temporary value; the second prints the stored value.

## Level 2 — Partially guided

**2.1 Remove and restore.** Remove the local value from exercise 1.2 with `--unset`. Predict, then check, which value is now effective. What does the exit code of `git config user.email` tell you when *no* value exists at any scope?

**2.2 Hide the global file.** Run `GIT_CONFIG_GLOBAL=/dev/null git config user.email`. Explain what you saw. (In Command Prompt or PowerShell the syntax for a temporary environment variable differs; use Git Bash for this exercise.)

## Level 3 — Independent

**3.1** Set up two folders, `~/work/` and `~/personal/`, and configure Git so that repositories under `work` use a work email and everything else uses your personal one, with a conditional include (section 14.6). Prove it with `--show-origin`.

## Level 4 — Professional scenario

**4.1** A new team member's commits are signed on their laptop but the CI system rejects your unsigned commits from a shared build server. Describe how you would find out which settings differ between the machines, and where you would change the setting so that only the build server is affected.

## Level 5 — Troubleshooting

**5.1** A colleague's `git commit -m "Update"` fails with `fatal: either user.signingkey or gpg.ssh.defaultKeyCommand needs to be configured`, although they have not touched signing. Give three diagnostic steps in order, and the safest way to commit while you investigate.

**5.2** Two people run `git pull` on the same repository. One gets a merge, the other gets an error about divergent branches. Which setting family (section 14.5.1) is the likeliest cause, and what command shows the difference?

**5.3** You are writing a script that runs `git commit`. It works on your laptop but fails on the build server. Name three settings that may differ, and how to make the script independent of them.
