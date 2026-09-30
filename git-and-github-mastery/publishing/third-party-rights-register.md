# Third-Party Rights Register

Audit of 30 September 2026. **Not legal advice.** For each category of material: what it is, where it comes from, the status, and what the book does about it. Third-party material is **never** covered by the book's CC BY-NC-SA 4.0 or MIT grant unless its owner's terms allow it, and each exclusion below is stated.

Status words: **original** (made for this book by the book project), **licensed** (used under a licence the source itself states), **quoted** (short quotation with a named source), **facts only** (facts and short command names, no protected text copied), **not used** (nothing in the book), **to check** (an open point for the author or a lawyer).

## A. Visual and interface material

| Item | Found in the book | Status | Treatment |
|---|---|---|---|
| Screenshots of Git, GitHub or any other interface | **None.** The book deliberately describes screens in words and labels them as not seen on a live account | not used | Nothing to license. If screenshots are ever added, each needs its own rights check (GitHub's interface is GitHub's material). |
| Logos of Git, GitHub, Microsoft, Docker, GitLab, Bitbucket, Creative Commons, Linux, etc. | **None.** Names appear as text only | not used | Trademark notice on the copyright page. |
| Diagrams | Mermaid sources in the chapters, rendered by the build | original | Licensed with the book text. They show Git concepts (commit graphs, flows), not copied figures. |
| "Sunrise Bakery" logo (`companion/sunrise-bakery-starter/images/logo.svg`) and the fictional bakery site | The running example | original | Fictional; under MIT as a code sample; any resemblance to a real business is unintended. The address and telephone number in it are placeholders. |
| Front cover (`publishing/cover`) | Draft cover, SVG and PNG | original | Typographic design with a commit graph; uses no third-party image. May be replaced by a designed cover, whose rights need their own check. The cover font is named in the SVG as DejaVu Sans with generic fallbacks. |
| Fonts embedded in the PDFs | DejaVu Serif, DejaVu Sans, DejaVu Sans Mono (subsets embedded by the PDF builder) | licensed | Read from the local package's copyright file (Debian `fonts-dejavu-core` 2.37): Bitstream Vera licence plus public-domain DejaVu changes. The licence says its **copyright and trademark notices and permission notice must be included in all copies of the font software**. A font credit line is on the copyright page. The EPUB embeds no font. |

## B. Quoted and adapted text

| Source | Where it appears | Its stated licence (as read) | Status and treatment |
|---|---|---|---|
| GitHub documentation (`github/docs`) | Many short quotations in Chapters 35 to 75, always with the page name and, in the checking boxes, the commit (`2eaab0b`) | The repository's `LICENSE` file is **CC BY 4.0** (read, 30 Sept 2026; recorded in the sources manifest). The repository also has an MIT `LICENSE-CODE` for code. The repository's notes about logos and trademarks were **not read** | **quoted, attribution given.** CC BY 4.0 requires credit and an indication of changes; the book names the source and quotes exactly. Not covered by the book's licence. To check: a short attribution line in Appendix N (added). GitHub logos and marks are excluded from that licence; the book uses none. |
| Git documentation and source (manual pages, howto "Revert a faulty merge") | Short quotations and command descriptions in many chapters | Git's `README` says Git is under the GNU GPL version 2 and that **parts have different licences** (read). The licence of each documentation file was **not** read | **quoted, to check.** Kept to short quotations with the version named. Not covered by the book's licence. Do not reproduce long passages. |
| Semantic Versioning 2.0.0 | Short quotations in Chapter 66 | **CC BY 3.0** (stated at the end of the specification text; read) | **quoted, attribution given** (specification named). Not covered by the book's licence. |
| CommonMark specification | Conformance counts and references in Chapter 8 (the book runs its 655 examples; it does not reproduce the specification text at length) | **CC BY-SA 4.0** for the specification (read in the repository's `LICENSE`); software under BSD 2-Clause | **to check.** ShareAlike material cannot be relicensed under a NonCommercial licence. Keep to short quotations and the facts (the number of examples, the version). If any example text is reproduced, list it and check. |
| YAML specification (`yaml/yaml-spec`) | Chapter 53: a short passage on Boolean spellings | The repository's licence file was not found at the path tried (HTTP 404); licence **not established** | **quoted, to check.** Short, named quotation only. |
| choosealicense.com data (GitHub) | Chapter 65: permissions, conditions and limitations summarised | Repository `LICENSE.md` is **MIT** (read) | **facts only / summary**, source named. |
| SPDX licence list and the SPDX copy of the CC BY-NC-SA 4.0 legal code | Chapter 65: identifiers, a few phrases quoted from the legal code | The licence-list data's own licence was not read (the path tried returned 404); the legal code's own terms were not read | **quoted, to check.** A few short phrases, the source named. The legal code is not reproduced. |
| Apache-2.0, GPL, LGPL, MPL texts | Chapter 65 names and summarises them | Licence texts are not copied into the book | **facts only.** |
| PowerShell and Command Prompt references | Appendix M: command and alias names | Not read for licence; the book copies names and parameters, not documentation text | **facts only.** |
| Microsoft, Apple and other vendor documentation | Not read; blocked hosts. Their marks appear as text | — | **not used** beyond naming the products. |
| The Git `README`, other project README files | Not quoted | — | **not used.** |

## C. Code

| Item | Status | Treatment |
|---|---|---|
| Code written for the book (scripts, exercises, recordings, `tools/`, `companion/`) | **original** | MIT for code samples, as instructed. |
| Workflow examples taken from GitHub documentation (Chapter 56 recipes 4 and 5, Chapter 58 deploy job, Chapter 60 injection example) | **quoted** from `github/docs` (CC BY 4.0 content; the repository's code is MIT) | The chapter names each as the documentation's example. The book's MIT grant covers only what the book wrote. |
| A pinned action commit name | A reference, not copied code | — |
| Test values published in GitHub's webhook documentation (Chapter 74) | **quoted** public test values | Named as the documentation's. |
| Third-party tools used by the book's build (WeasyPrint, markdown-it-py, veraPDF, EPUBCheck, Mermaid, git-filter-repo, PyYAML, `gh`) | **Tools, not distributed in the book** | Their licences apply to the tools only. The repository does not contain their source. |
| Code copied from Stack Overflow, blogs, AI tools' output or other people's projects | **None is known.** The book's commands were written for it and run | Recorded only as the author's statement; see `final-publication-blockers.md` item 3 for the AI-assistance point. |

## D. Names and trademarks

| Name | Treatment |
|---|---|
| Git, GitHub, Microsoft, Windows, Linux, macOS, Docker, GitLab, Bitbucket, Creative Commons, npm, PowerShell, Visual Studio Code, Copilot, and others | Used only to name the products they denote. Copyright page: "may be trademarks of their respective owners". No claim that any is or is not registered: **no specific trademark claim is made, and none was verified.** |
| The non-affiliation statement | Stays as already written: independent work, not affiliated with, endorsed by or sponsored by Git, GitHub, Microsoft or other third parties. |
| SHARIF TECHNOLOGIES | The author's name and brand for the book. Not licensed by the CC or MIT grants. Trademark status not established. |

## E. Open points

1. Decide and record whether the diagrams and cover are licensed with the text (proposed: yes) or kept all-rights-reserved.
2. Check any reproduced CommonMark text (ShareAlike conflict with NonCommercial) and the licences of the Git documentation files and the YAML specification text that is quoted.
3. Attribution line for GitHub documentation quotations: added to Appendix N.
4. If screenshots, logos or a designed cover are added later, update this register first.
