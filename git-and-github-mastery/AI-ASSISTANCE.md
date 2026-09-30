# AI Assistance: how this book and its repository were made

**This book was written with an AI assistant.** The assistant is Claude, made by Anthropic, used through Claude Code, working in sessions with the author, Sharif Tingane Issah. This page says where the assistant worked, what the author decided, how the repository records it, and what remains uncertain. The printed book carries a shorter statement (copyright page, Preface, author page and Appendix N); this page is the full version.

## Who did what

| Area | What the AI assistant did | What the author did and decided |
|---|---|---|
| Plans and architecture | Drafted the concept, learner profile, 81-chapter outline, curriculum, dependency map, gap analysis and plans from the author's brief | Gave the brief and the rules (run commands, label evidence, invent nothing); approved the architecture |
| Chapter text | Drafted all 81 chapters, the front matter, the preface and the back matter | Set the scope, title, subtitle, brand and slogan; carries responsibility for the book |
| Exercises, solutions, projects, challenges, assessment | Wrote all of them and the assessment's setup and checking scripts | Set the requirement that each chapter has practice and a capstone |
| Glossary and appendices | Wrote the glossary data and the appendices, and the scripts that generate the terminology maps and the sources log | Approved the list of appendices |
| Code samples and companion files | Wrote every script, the Sunrise Bakery starter files and the check tools | Chose the MIT licence for code |
| Command recordings | Ran the commands in a sandbox (Bash and zsh, several Git versions) and recorded the output that the book prints | Nothing was run by the author on a live GitHub account, on Windows or on macOS; those statements in the book are labelled |
| Research and verification | Fetched and read official sources, kept the research ledger (356 rows), wrote the verification scripts and assigned each claim its evidence class | Required that nothing be invented and that unverified claims stay visible |
| Editorial read-through | Read all 81 chapters and the appendices and made the corrections | Required the read-through |
| Build and checks | Wrote the PDF, EPUB, clean-export and package builders, the validators' set-up and the continuous-integration workflow | Required the formats and the brand and publisher distinctions |
| Cover and diagrams | Drew the draft cover (SVG) and wrote the diagram sources | May replace the cover |
| Author and publisher information | Researched the public sources it could reach, drafted the biographies, the imprint profile and the publication documents, and recorded what could not be established | Gave the authorisation to research; supplied a research dossier (from sources the assistant could not reach) that the biographies use; must confirm the biography and the facts in it |
| Licensing and rights documents | Drafted the copyright page, licence notices, rights register and checklists to the author's wording | Chose CC BY-NC-SA 4.0 for the text and MIT for code; chose SHARIF TECHNOLOGIES as holder and imprint |
| Repository administration | Created branches and pull requests, ran the checks, fixed failures and merged pull requests, using GitHub tools under the author's standing authorisation | Owns the repository and the account; decides on publication and on the default branch |

## How the repository records it

- Until 30 September 2026 (pull request 23), the assistant's commits carry the author name "Claude", so GitHub lists Claude as a contributor. Those commits, and the pull requests and merge commits around them, remain unchanged: history was not rewritten.
- From 30 September 2026, new commits are authored under the author's identity and carry a `Co-Authored-By: Claude` trailer and a link to the working session, so Claude stays credited as co-author.
- The merge commits of pull requests 1 to 23 were created by GitHub under the author's account.

## What the AI assistant could not do, and mistakes

The assistant had no live GitHub account session, no Windows or macOS machine, and could not reach several websites (Wikipedia, Microsoft, Creative Commons, the author's own site and others). The book says so where it matters and keeps a list of unverified claims (Appendix N). An AI assistant can be wrong, and some errors were found and corrected during the read-through (for example a wrong PowerShell alias, wrong chapter references and wording that claimed a step the author had not done). Readers should use the checking labels and the current official documentation.

## Open legal and rights questions (not settled here)

1. How much copyright subsists in text and code produced with AI assistance, and who holds it, depends on the law of the country and is not settled by this page. Advice from a qualified person is needed before the copyright notice and the licence grants are published.
2. Copyright registration offices and some retailers ask whether AI-generated material is included; the answer for this book is yes, and the extent is described above.
3. The assistant's training data is not known to the author or to this project, so it cannot be said that no third-party text or code influenced the output. The third-party rights register lists what is known to be quoted.

## Keeping this page true

Update it when the way of working changes, when the assistant's role in a new area begins, or when the author replaces the assistant's work in an area (for example a designed cover).
