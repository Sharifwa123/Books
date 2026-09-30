# Chapter 32 solutions

## Level 1
**1.1** In the user (global) configuration, `~/.gitconfig`, when defined with `--global`.

**1.2** `'st' is aliased to 'status --short'`.

## Level 2
**2.1** For example `git config --global alias.hello '!echo hello'`; `git hello` prints `hello`.

**2.2** It prints one line per alias, `alias.<name> <definition>`.

## Level 3
**3.1** The hook exits with a non-zero status (1); no commit is made and the change stays in the working folder, as ` M` in `git status --short`.

**3.2** `git commit --no-verify` skips the hook. A clone does not receive it: hooks are not copied.

## Level 4
**4.1** `i/lf` is the line ending in the index (what is stored), `w/crlf` is the line ending in the working file, and `attr/text eol=lf` is the attribute rule in force.

**4.2** Git prints `Resolved '<file>' using previous resolution.` The status stays `UU` because Git leaves it to you to check the result, stage it and commit.

## Level 5
**5.1** No. A local hook can be skipped with `--no-verify` and is not copied to other clones. The rule must also be checked on the server (Chapter 54<!--ref:actions-->).

**5.2** The token is stored in plain text in a file; anyone who can read the file can use the token. Revoke the token, switch to the operating system's protected helper, and delete the file (Chapter 33<!--ref:gitsec-->).

**5.3** Hooks run code on your computer with your permissions, so an untrusted hook could do anything. Read the script before using it, or remove it.
