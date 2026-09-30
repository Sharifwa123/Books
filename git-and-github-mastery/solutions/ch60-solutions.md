# Chapter 60 solutions

## Level 1
**1.1** `HACKED` printed before the "checking" line: the pasted title closed the quotation and added a command.

**1.2** The script printed the whole title as text and ran nothing, because the value travelled in an environment variable instead of being pasted into the script text.

## Level 2
**2.1** Yes: quotes, semicolons and `$` are allowed by Git's rules for names. A branch name, like a commit message, is text chosen by someone else and must not be pasted into a script.

**2.2** Untrusted: `github.event.issue.title`, `github.head_ref`, `github.event.pull_request.body`. `github.sha` is a hash made by Git, so it has a fixed safe shape.

## Level 3
**3.1** Use `env:` with `TITLE: ${{ github.event.pull_request.title }}` and `run: echo "Hello $TITLE"`.

**3.2** A tag can be moved to different code later, while a commit name identifies its content and cannot be moved without a hash collision. Before copying a SHA, check that it comes from the action's own repository and not from a fork. Also read the action's code, or trust its creator.

## Level 4
**4.1** "This trigger runs with secrets and possibly write access, and checking out the pull request runs a stranger's code there. GitHub's documentation warns against this combination. Use the `pull_request` trigger without secrets, or split the work so untrusted code never runs in the privileged workflow."

## Level 5
**5.1** Delete the log, rotate the secret, then find how it reached the log (for example a derived value that was not registered as a secret).

**5.2** Add `permissions: contents: read` at the top level of the workflow file.
