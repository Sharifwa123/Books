# Chapter 73 solutions

## Level 1
**1.1** `git` works on a repository and its history (examples: commit, merge, push). `gh` works on things GitHub adds (examples: pull requests, issues, releases, workflow runs).

**1.2** `gh --version`. Commands and output change between versions, and an old `gh` may lack commands.

## Level 2
**2.1** `gh alias set prd "pr create --draft"`, `gh alias list | grep prd`, `gh alias delete prd`.

**2.2** `gh config set editor "code -w"` and `gh config get editor`. The `-w` flag makes the editor command wait until you close the file, so `gh` can read what you wrote.

## Level 3
**3.1** For example: `if gh auth status >/dev/null 2>&1; then echo ready; else echo "please log in"; fi`.

**3.2** `GH_TELEMETRY=log gh config get editor 2>&1 | grep '"type"'` shows `command_invocation`. Disable with `export GH_TELEMETRY=false` (or `DO_NOT_TRACK=true`), or with `gh config set telemetry disabled`. The environment variable takes precedence over the configuration value.

## Level 4
**4.1** For example: a step with `env: GH_TOKEN: ${{ secrets.GITHUB_TOKEN }}` and `run: gh run list`. Restrict the workflow's token to the read permission that the command needs, because a compromised step can use whatever the token allows (Chapter 60<!--ref:wfsec-->).

## Level 5
**5.1** Run `gh auth login` (interactive, for a person), or set the `GH_TOKEN` environment variable. In a workflow prefer `GH_TOKEN` set from the built-in `GITHUB_TOKEN`, with least privilege.

**5.2** The command is newer than the installed version, or it is provided by an extension that is not installed. Check `gh --version` and `gh --help`.
