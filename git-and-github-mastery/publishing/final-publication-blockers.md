# Final Publication Blockers

Status at 30 September 2026. Everything that can be done without a person has been done. What remains needs the author (or, for some items, a lawyer, an agency or a printer). Nothing below stops further unattended work on the manuscript, tooling or checks.

## A. Needs the author's decision or confirmation

| # | Blocker | Why it cannot be settled by the project | What is ready |
|---|---|---|---|
| 1 | **Rights holder.** Is SHARIF TECHNOLOGIES the author's trading name, or a separate legal person? If separate, there must be a written basis (assignment, employment terms or similar) for it to hold the copyright and to grant the licences. | The relationship is a legal fact. The project found no registry or document (`publisher-imprint-profile.md`). It will not manufacture a basis. | The pages are prepared exactly as instructed. An alternative wording naming the author is in `publisher-imprint-profile.md`. |
| 2 | **Final licence wording sign-off.** Confirm the wording on the copyright page is what the author wants to publish. | It is proposed wording, not legal advice; the Creative Commons text was checked by the author, not by this project (`creativecommons.org` is unreachable). | `rights-and-licensing.md`, `LICENSE-TEXT.md`, `LICENSE-CODE`, `LICENSE.md`. |
| 3 | **AI assistance and authorship.** The repository history records that this book was produced with AI assistance (commit trailers). Decide what the book says about it, and confirm with qualified advice what that means for copyright ownership, for registration, and for the licence grant ("only for material the rights holder has authority to grant"). | Some legal systems do not give copyright to machine-generated material, and registration offices may ask for disclosure. This is a legal and ethical decision for the author, and the readers are owed honesty. The project will not hide it and will not assert an ownership conclusion. | The title page says "Written by Sharif Tingane Issah"; the author must decide whether that stays exactly as it is. The clean export contains no working notes. A one-sentence disclosure can be added to the copyright page once the author chooses the wording. |
| 4 | **Publication authorisation.** Explicit permission to publish or release the finished book. | Reserved to the author. | All build and validation pipelines. |
| 5 | **Website and contact.** Confirm `www.shariftechnologies.online` is the official, live site. Decide whether to give a contact address. | The site could not be opened here. No address was supplied, and a personal address found in a public package record was deliberately not used. | The page prints the website the author's profile lists. |
| 6 | **Biography sign-off.** Read the three biographies in `author-biographies.md` and confirm or correct them, and add any credential or employment the author wants stated, with a source. | The biography is built from public evidence only; the author knows what else is true. | Short, standard and extended versions. |

## B. Needs an outside party

| # | Blocker | Who |
|---|---|---|
| 7 | ISBN for each sold format (`isbn-metadata-checklist.md`) | The ISBN agency for the registrant's territory, after the registrant is settled |
| 8 | Print specification: trim size, paper, binding, printer; then back cover, spine and wrap | The author and a printer |
| 9 | Legal review of the licence structure, the rights holder, the third-party register open points (ShareAlike sources) | A qualified adviser |
| 10 | A real screen-reader test and a reading test with a beginner | A person with the tools |
| 11 | A run of the book's GitHub-side procedures on a live account (the "live-account pass") | The author's account |
| 12 | Kindle and other retailers' own upload requirements | Their sites, which are unreachable from the authoring environment |

## C. Known limits, not blockers

- 79 ledger rows are still marked unverified (55 are early planning rows superseded by later chapter-level rows); many need hosts that cannot be reached here. Appendix N lists them, and the chapters carry 25 verification-pending markers.
- No list of tables; no byte-reproducible PDFs.
- The book is not third-party accessibility certified.
- The empty-commit revert exercise stays blocked until its cause is confirmed.

## D. Not blockers any more

Author biography (written from evidence), publisher profile (written, with the legal status left open), licence wording (prepared), third-party rights register (prepared), ISBN checklist (prepared), stale repository status text (updated), the six references to `research/…` paths (audited, `research-file-references-audit.md`).
