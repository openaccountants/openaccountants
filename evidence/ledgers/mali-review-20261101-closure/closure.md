# Independent closure of historical Mali CSS review R1

Review date: 2026-11-01.

**Accepted candidate: `03052d5dbd3fc013bb610ce76f70fd13fb40b5d6`, strictly for the enacted 2025 CSS source baseline reviewed in `../mali-review-20261101/review.md`. R1 is closed.** This is not approval of a complete 2025 amendment chain, current 2026 treatment, a filing or portal walkthrough, publication, a completed country pack or accountant attestation. The enacted 2026 fiscal Annex U and any relevant later amendment remain unverified. The 2026 hold is unchanged and remains mandatory.

Guide file: `skills/mali/ml-solidarity-contribution.md`, version and title 0.2. SHA-256: `3de6adbda1bf24717975b0016f63d7d9ca026bfd7b5bb77f92f76ae0c852d87a`.

## Independent repair verification

The reviewer compared the entire Guide against rejected candidate `d360fed18e2526f13183b488aec10205d4b50a97`. Applying only the following explicit transformations to that old blob reproduces the new file exactly:

1. All 20 CSS ordinance source anchors changed from PDF page 8 to page 10.
2. The duration citation now links articles 1–9 to page 10 and final article 20 separately to page 11.
3. Finance-law article 1 now links to page 4.
4. Frontmatter version and title advanced from 0.1 to 0.2.
5. The top warning accurately says the historical year label does not prove retrieval or publication enforcement.

No figure, tax rule, example, input, output or computation changed. The two oa-check blocks are byte-identical. The initial 21-row substantive source review therefore remains applicable within its original limits.

Page-specific extraction of the same unchanged official PDFs independently confirms: ordinance PDF page 10 is gazette 90 and holds CSS articles 1–9; page 11 is gazette 91 and holds final article 20; finance-law PDF page 4 is gazette 1408 and holds article 1. No PDF, page image or full extraction was placed in Git. The initial review already opened all three official source URLs and visually checked CSS page 10. No additional law research or missing-annex search was required for this focused closure.

## Preserved evidence and limits

The old-topic map, rule ledger and README retain their initial reviewed SHA-256 values. All six legacy files retain the initial hashes. The private initial writer receipt, read manifest and all three source PDFs retain the exact initial SHA-256 values recorded by the reviewer. The original rejected review, its candidate identifier and finding remain in their separate directory; closure is additive. The closure snapshot records hashes for all eight initial review records as committed in the accepted candidate. These records were not edited during closure.

The Guide retains `tax_year: 2025`, its historical description and its explicit prohibition on using the baseline for a client's 2026 rate, liability or filing. It now correctly distinguishes that instruction from technical enforcement. The passing annual validator is not evidence of current-year approval. No MCP partial retrieval, publication enforcement, production database or authenticated portal was tested.

## Scoped validation

All executed with the supplied validation-deps PYTHONPATH:

- `skill_checks.py`: all 15 checks pass.
- `check-examples.py --require`: 2 oa-check blocks, 0 failures, 0 missing.
- `validate-guides.py --changed-only --no-index-check`: passes; the existing different-job SC warning remains.
- `git diff --check d360fed18e2526f13183b488aec10205d4b50a97 03052d5dbd3fc013bb610ce76f70fd13fb40b5d6`: passes.

The exact-diff, page-token, receipt and unchanged-file assertions all pass. `closure-observed.json` holds the accepted SHA, candidate and source hashes, preserved-record hashes and assertion results. Actual command output is saved beside it. Full-tree validation and coverage were not rerun because this closure changes only reviewed source locators, a warning's precision and version metadata; the initial full no-index validation and coverage results remain preserved.

No Guide content, ledger or initial receipt was edited by this reviewer. No commit, push, PR, comment, issue operation or attestation was performed. No current-year or country-completion approval is given.
