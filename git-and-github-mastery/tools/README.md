# Tools

Outline and checks
- `toc_data.py`: single source of truth for the outline (numbers are derived, never typed).
- `build_planning.py`, `check_refs.py`: render planning documents that contain chapter numbers, and validate ordering, Core/Deep consistency, cross-references, the registry and ledger ids.
- `resolve_refs.py`: expands the key-based chapter cross-references in the manuscript to numbers.
- `check_all.sh`: runs all the static checks (structure, links, ledger, secrets, transcripts, export).

Generated text
- `build_frontmatter.py`, `build_backmatter.py`, `glossary_add.py`: front matter, appendices E, F and N, the glossary and the author page.

Recordings and ledger
- `run_session.py`, `check_transcripts.py`: re-run recorded command sessions and compare them with the text.
- `fetch_source.py`, `ledger_add.py`, `ledger_verify.py`: fetch sources with hashes and maintain the research ledger.

Editions
- `build_pdf.py`, `build_epub.py`, `export_clean.py`, `build_package.sh`, `check_pdf.py`, `verapdf_check.sh`: PDF, EPUB, clean export, packaging and validation.

Typical workflow for a change: edit the manuscript or `toc_data.py`, regenerate with the `build_*` scripts where a generated file is affected, run `tools/check_all.sh`.
