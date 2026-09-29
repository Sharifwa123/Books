# 14 — GitHub Feature Section Template and UI Rules

Every GitHub feature section uses these headings, in this order. A heading may be short, but none may be silently skipped; if it does not apply, say so. No heading may state a *current fact* until the ledger row for it is verified.

1. **What it is**
2. **Why it exists**
3. **How it relates to Git** (what is Git, what is GitHub-only)
4. **How to use it** (concept first; then the UI path, marked version-dependent; then the CLI/API route if any)
5. **Who can use it** (account type, organisation context)
6. **Permissions required** (role/repository permission)
7. **Plan and visibility limitations**
8. **Security considerations**
9. **Common mistakes**
10. **Alternatives**
11. **When it is useful**
12. **When it may be unnecessary**

Footer of every such section: `Verified: [DATE] · Conditions: [account/visibility/org/plan] · Ledger: [row ids]`. Until verified it reads `Verified: [NOT YET VERIFIED]`.

## UI rules
- Teach the underlying concept before the interface.
- Interface instructions carry a **UI-VERSION NOTE** callout: "Menu names and locations change. If you cannot find it, search the official docs for <concept name>."
- Prefer stable anchors (feature names, URLs of documented pages, `gh`/API equivalents) over pixel-level directions.
- Never write UI steps from memory; each step traces to a verified ledger row and the date is shown.
- No screenshots until verified; screenshots are dated and treated as illustrations.
