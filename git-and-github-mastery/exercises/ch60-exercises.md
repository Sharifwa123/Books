# Chapter 60 exercises — Securing Workflows

Attempt each exercise before you open `solutions/ch60-solutions.md`. Exercises 1.1 to 2.2 use only your terminal; nothing needs a GitHub account.

## Level 1 — Guided

**1.1 Reproduce it.** In an empty folder, set `title='x"; echo HACKED; #'`. Build `vulnerable.sh` with `printf 'title="%s"\necho "checking: $title"\n' "$title" > vulnerable.sh`, read it with `cat`, and run it with `sh`. What extra line printed?

**1.2 Defend it.** Write `safe.sh` containing `echo "checking: $TITLE"` and run `TITLE="$title" sh safe.sh`. What is different?

## Level 2 — Partially guided

**2.1 A hostile branch name.** Ask `git check-ref-format --branch` about a name that contains a semicolon and a `$`. Does Git accept it? What does that tell you about branch names in workflows?

**2.2 Find the untrusted value.** For each context, say whether you would treat it as untrusted: `github.event.issue.title`, `github.sha`, `github.head_ref`, `github.event.pull_request.body`.

## Level 3 — Independent

**3.1 Rewrite a step.** Rewrite this step so that it is not injectable: `run: echo "Hello ${{ github.event.pull_request.title }}"`.

**3.2 Pin an action.** Explain, in three sentences, why `uses: some/action@v2` is riskier than a full commit SHA, and what you must check before copying a SHA.

## Level 4 — Professional scenario

**4.1 A review.** A colleague proposes a workflow on `pull_request_target` that checks out the pull request branch and runs `npm test` with a deploy secret available. Write the review comment, using the rules of this chapter.

## Level 5 — Troubleshooting

**5.1** A secret shows in a log as a long unmasked string. Give the order of actions from this chapter.

**5.2** A workflow only needs to read the repository but the token has write access. Which key do you add, and where?
