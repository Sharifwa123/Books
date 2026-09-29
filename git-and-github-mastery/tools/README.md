# Tools
- `toc_data.py` — single source of truth for the outline (numbers are derived, never typed).
- `build_planning.py` — renders planning docs that contain chapter numbers (`11`, `03`, `12`, `05`, `13`, `chapter-map.json`).
- `check_refs.py` — validates ordering, Core/Deep consistency, cross-references, registry and ledger ids.
Workflow: edit `toc_data.py` → `python3 tools/build_planning.py` → `python3 tools/check_refs.py`.
Manuscript sources will refer to chapters by key tokens (curly-brace ch:key form); a resolver step will be added when drafting starts.
