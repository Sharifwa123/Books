# Publication Metadata Checklist

Status at 30 September 2026. "Ready" means a value exists and is supported; "Open" means a person must decide or supply it.

## Descriptive metadata

| Field | Value | State |
|---|---|---|
| Title | Git & GitHub: From Zero to Mastery | Ready |
| Subtitle | A Complete Beginner-to-Expert Guide to Version Control, Collaboration, Automation, Security, and Modern Software Development | Ready |
| Author | Sharif Issah Tingane | Ready |
| Imprint | SHARIF TECHNOLOGIES (*Knowledge Is Power*) | Ready |
| Legal publisher | not established | Open |
| Copyright | © 2026 SHARIF TECHNOLOGIES, as instructed | Ready as instructed; legal basis open |
| Licences | Text: CC BY-NC-SA 4.0 (`https://creativecommons.org/licenses/by-nc-sa/4.0/`); code: MIT | Ready, pending the rights review |
| Edition | 1st edition | Ready |
| Language | English | Ready |
| ISBN | none assigned | Open (`isbn-metadata-checklist.md`) |
| Publication date | not set | Open; needs the publication authorisation |
| Website | `www.shariftechnologies.online`, the address on the author's profile; not opened by this project | Author to confirm it is live and official |
| Contact e-mail | none supplied | Open; optional |
| Postal address | none supplied | Open; optional (the book carries none) |

## Short description (retailer, up to about 50 words)

A beginner-to-advanced guide to Git and GitHub. It starts with what a computer and a file are, then covers everyday Git, collaboration, automation, security, open-source practice and recovery. Every command was run and recorded, and every claim is labelled with how it was checked.

## Long description (about 130 words)

*Git & GitHub: From Zero to Mastery* teaches version control to people who have never used it, and goes on to the practices of professional teams. It begins with computers, files, paths and the terminal, then teaches Git by doing: commits, branches, merging, undoing and recovering, tags and history. It moves to GitHub: repositories, issues, pull requests, reviews, protection rules and organizations, then to automation with GitHub Actions, security, open-source practice, releases, deployment and troubleshooting, and ends with a capstone project and a practical assessment. The commands in the book were run in a sandbox and their output recorded; statements about Git and GitHub are tied to the source they were checked against, and an appendix lists what could not be checked. The book is published under the SHARIF TECHNOLOGIES imprint and is licensed for noncommercial sharing and adaptation.

(The last sentence depends on the rights review and is removed if the licence decision changes.)

## AI-assistance disclosure

| Item | State |
|---|---|
| Statement in the book (copyright page, Preface, author page, Appendix N) and in `AI-ASSISTANCE.md` | Done |
| EPUB `dc:contributor` and package metadata name the AI assistant | Done |
| Retailer upload forms and copyright-registration applications may ask whether AI-generated material is included; the truthful answer is yes, as described in `AI-ASSISTANCE.md` | To answer at upload or filing; requirements not checked (sites unreachable) |

## Format and file metadata

| Item | State |
|---|---|
| Reflowable EPUB (built from the manuscript, not from the PDF), EPUBCheck-validated in CI | Ready |
| Screen PDF (A4) and print-profile PDF (170 x 240 mm), PDF/UA-1 validated by veraPDF in CI | Ready |
| PDF/A-2b archive build validated in CI | Ready |
| Editable source (Markdown) and clean export without planning notes (the AI-assistance statement stays in the book text) | Ready (`tools/export_clean.py`) |
| Kindle: from the EPUB | Amazon's upload requirements not checked (site unreachable) |
| Cover: front cover, draft | Ready as a draft; back cover, spine and wrap need trim size, page count and ISBN |
| Accessibility metadata in the EPUB | States that the book is not third-party certified |
| Identifier in the EPUB | Not an ISBN; to be replaced when one exists |

## Placeholders still in the book text

ISBN, publication date, publisher address, publisher e-mail and the date of final technical verification. They are visible placeholders by design; they are filled only with real values (`final-publication-blockers.md`).
