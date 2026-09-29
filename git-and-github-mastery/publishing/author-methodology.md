# Author's Methodology (source for the Preface's "How this book was checked")

1. **Commands are run, not remembered.** Every command and flag printed in the book is executed in an isolated sandbox and checked against the documentation for the version tested. (Example from this project: a flag assumed to exist on `git revert` did not; the test failed and the assumption was discarded.)
2. **Versions and dates are recorded.** Git behaviour is tied to a tested Git version; GitHub behaviour to a verification date and to the account type, repository visibility, organisation context and plan under which it was observed. Nothing is generalised beyond those conditions.
3. **Isolated test environments.** Verification scripts ignore the host's Git configuration (system/global scopes are redirected) because inherited configuration changes Git's behaviour.
4. **Official sources first.** Git behaviour is checked against Git's own documentation; GitHub behaviour against GitHub Docs; licences against the licence issuers' own texts. Third-party summaries are not substitutes.
5. **Evidence classes.** Each claim in the research ledger is one of: officially verified; locally tested; both; time-sensitive; needs re-verification; not applicable. A locally tested claim is not called officially verified.
6. **Undocumented behaviour is investigated before it is taught.** Surprising results (for example reverting an empty commit) are understood, or the exercise is not published.
7. **UI is taught as concept first.** Interface paths are verified and labelled version-dependent; no important idea rests solely on a button location.
8. **Re-verification before publication.** The book's "Technical information verified" date is set only after all time-sensitive rows are re-checked.
