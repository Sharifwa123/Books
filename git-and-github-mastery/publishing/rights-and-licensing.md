# Copyright and Licensing Metadata

Prepared 30 September 2026 to the author's instruction. **Proposed publication wording, not legal advice.** Before publication, the wording must be checked against the final ownership and rights situation (`final-publication-blockers.md`, items 1 and 2).

## Decisions as instructed

| Item | Decision | Source of the decision |
|---|---|---|
| Copyright holder | SHARIF TECHNOLOGIES | Author's instruction, confirmed again 30 September 2026. Legal basis not documented (see `publisher-imprint-profile.md`); the book is published by the author personally under the imprint. |
| Copyright year | 2026 | Author's instruction |
| Book text licence | Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0), SPDX `CC-BY-NC-SA-4.0` | Author's instruction |
| Canonical licence URL | https://creativecommons.org/licenses/by-nc-sa/4.0/ | Author's instruction |
| Code samples licence | MIT License, SPDX `MIT` | Author's instruction |
| Complete legal code in the book | **Not reproduced.** A human-readable notice and the canonical link are used. | Author's instruction |

## What was and was not checked

| Claim | Evidence | Class |
|---|---|---|
| The Creative Commons legal code has been checked against the official text | The author states it was independently checked. `creativecommons.org` is **not reachable** from the authoring environment, so this project did not re-check it. | Author's statement |
| The SPDX copy of the CC BY-NC-SA 4.0 legal code defines License Elements, NonCommercial and ShareAlike (quotations used in Chapter 65) | Read from the SPDX licence-list repository earlier in the project (ledger R320) | Read, secondary source |
| SPDX identifiers `CC-BY-NC-SA-4.0` and `MIT` exist | SPDX licence list 3.29.0 (ledger R319) | Read |
| The MIT licence text used in `LICENSE-CODE` | The SPDX copy of the MIT text (`text/MIT.txt` in the SPDX licence-list-data repository), fetched 30 September 2026 and recorded in `research/sources-manifest.csv` (SHA-256 in the manifest). The year and holder placeholders were filled as instructed. | Read, secondary source; the official `opensource.org` page was not reachable |

## Files created for the licences

| File | Content |
|---|---|
| `LICENSE-TEXT.md` (in the book folder) | A short notice: the book text is under CC BY-NC-SA 4.0, the canonical URL, the copyright line, what the licence does not cover. It does **not** contain the legal code. |
| `LICENSE-CODE` | The MIT License text for the code samples, with "Copyright (c) 2026 SHARIF TECHNOLOGIES". |
| `LICENSE.md` | A plain index saying which licence applies to which folder. |
| `companion/LICENSE.md` | States that the companion files are under MIT. The bakery starter's own README is left byte-for-byte as recorded, because the book's recorded command sessions (Chapters 16 and 18) include its contents and commit names; its old "MIT (intended)" line is declared superseded there. |

## Which material is under which licence

| Material | Licence | Note |
|---|---|---|
| Book prose (chapters, appendices, front and back matter, exercises, solutions, glossary) | CC BY-NC-SA 4.0 | Original text only |
| Code samples inside chapters and in `companion/`, `tools/`, `verification/` scripts and the recorded-session scripts | MIT | "Unless a particular example identifies another licence or a third-party source" |
| Diagrams (Mermaid sources) and the draft cover (`publishing/cover`) | Original to the book. Licensed with the book text (CC BY-NC-SA 4.0); the cover is designed by the book project and may be replaced. | Author's decision; flagged in the rights register |
| Quotations from third-party documentation and specifications | **Not covered** by either licence; their own terms apply | `third-party-rights-register.md` |
| Names, logos and trademarks of others | **Not licensed** by anyone here | Trademark notice in the copyright page |
| The SHARIF TECHNOLOGIES name and any logo | **Not licensed** by either licence: the licences cover the text and code only | Trademark status not established |

## Copyright page wording (as used in the book)

> Copyright © 2026 SHARIF TECHNOLOGIES. All rights reserved except for the permissions expressly granted under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International Public License.
>
> This book's original text is licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (CC BY-NC-SA 4.0): https://creativecommons.org/licenses/by-nc-sa/4.0/
>
> Under this license, readers may share and adapt the licensed book material for noncommercial purposes, provided that the applicable attribution and ShareAlike requirements are followed. Commercial use requires separate permission from the rights holder.
>
> Code examples contained in this book are separately licensed under the MIT License unless a particular example identifies another applicable licence or third-party source.
>
> The licence applies only to material for which the stated rights holder has authority to grant the licence. Third-party material, trademarks, screenshots, quotations, logos, and other material identified as belonging to their respective owners are not automatically covered by this licence and may be subject to separate rights or permissions.
>
> This licensing notice is a plain-language summary and does not replace the terms of the applicable Creative Commons or MIT licence.

Small edits made to the instructed text: "Sharif Technologies" is written "SHARIF TECHNOLOGIES" to match the title page and all other uses of the name; nothing else is changed.

## The distinctions the pages must keep

The book is **copyrighted**. It is not "copyright-free", "public domain", "free of copyright" or "owned by everyone". The licence grants stated permissions. The book may be freely available online; that does not remove copyright.

| # | Distinction | Position in the licensing pages |
|---|---|---|
| 1 | Copyright ownership | SHARIF TECHNOLOGIES (as instructed). Choosing a licence does not transfer or remove ownership. |
| 2 | Permission to read | Free to read. |
| 3 | Downloading | Free to download. |
| 4 | Redistribution | Allowed for noncommercial purposes with attribution, under the same licence (ShareAlike). |
| 5 | Modification | Allowed for noncommercial purposes with attribution; adaptations carry the same licence. |
| 6 | Commercial use | Not granted by the licence; separate permission from the rights holder is required. |
| 7 | Code reuse | Code samples are under the MIT License, separately from the prose. |

These seven are stated in the book's copyright page and in Chapter 65.

## Points a lawyer should see (not resolved here)

1. Who holds the rights: the author or a separate SHARIF TECHNOLOGIES (see `publisher-imprint-profile.md`).
2. How the AI assistance disclosed in `AI-ASSISTANCE.md` affects ownership and the licence grant; whether any part of the text or code is not protected or not owned by the stated holder because of how it was produced (`final-publication-blockers.md`, item 3).
3. What counts as "NonCommercial" in the situations the author cares about (classes with fees, sites with advertising, corporate training). The licence's own definition governs.
4. Adoption effects of a NonCommercial licence (some repositories and publishers accept only licences that allow commercial use); the author has chosen knowingly.
5. Third-party material listed in `third-party-rights-register.md`, notably any ShareAlike-licensed source.
