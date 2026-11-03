# Independent historical Mali CSS source-baseline review

Date: 2026-11-01. Frozen candidate: `d360fed18e2526f13183b488aec10205d4b50a97`. Base: `db5bf4ff7d4b078421b4fedd483d9b9b91cd71a6`.

**Disposition: not approved pending correction of inaccurate source page links.** No historical rule or arithmetic error was found in the 21 ledger rows. This is solely review of the enacted 2025 ordinance baseline and its stated exclusions. It is not approval of 2026 treatment, an accountant attestation, a full-year 2025 amendment-chain opinion, a portal walkthrough, permission to publish, or a complete-country review. No enacted 2026 Annex U was obtained or assumed unchanged.

## Finding requiring the writer's correction

**R1, P2: incorrect PDF page locators.** In `skills/mali/ml-solidarity-contribution.md`, all 20 ordinance links in lines 22–73 end in `mali-jo-2025-03.pdf#page=8`. PDF page 8 is gazette page 88 and concerns stadium ordinances, not CSS. Ordinance 2025-007 begins on PDF page 9 / gazette page 89; its operative CSS articles 1–9 are on PDF page 10 / gazette page 90, and its final article 20 is on PDF page 11 / gazette page 91. Link ordinary CSS rules to `#page=10`; the duration citation can point to that chapter and separately to `#page=11` for article 20. The chapter I/II boundary is on PDF page 10, with the alcohol base and final provision continuing on page 11. The finance-law article 1 citation on line 26 ends in `mali-jo-2025-33-5.pdf#page=3`, but article 1 is on PDF page 4 / gazette page 1408. Use `#page=4`. The ratification locator `mali-jo-2025-18.pdf#page=12` correctly opens gazette page 720. The underlying official PDF URLs and cited act/article identities are correct.

Affected ledger rows: 1–4, 6, 8–20 through their Guide source links. No correction to ledger substantive figures is requested. The writer must make the link changes; this reviewer did not edit Guide content or original ledgers.

## All ledger rows checked

The reviewer read the supplied official texts, including the full Ordinance 2025-007 (articles 1–20 and neighbouring chapter), Loi 2025-022's ratification, and finance-law articles 1 and 46 with surrounding provisions. All three official PDF URLs were opened independently on 2026-11-01. Local PDF hashes match the writer's manifest. CSS page 10 was rendered and visually checked, and page-specific extraction confirmed the locator error. Both official DGI pages were opened and read on 2026-11-01. The announcement is corroboration only; it does not displace the gazette.

| Ledger ID | Actual source check | Result within historical baseline |
|---|---|---|
| 1 | Ordinance arts. 1–3, all adjacent scope text | Matches; IBIC/IS scope and debtor identification preserved |
| 2 | Arts. 2–4 | Matches; turnover base supports the loss distinction |
| 3 | Arts. 2–4 | Matches; rate and limited absence-of-threshold statement |
| 4 | Complete arts. 1–20, CSS chapter and final art. 20 | Matches; no CSS fixed term, sunset or delayed commencement stated; first partial period left open |
| 5 | Loi 2025-022, article unique, gazette 720 | Matches; unconditional ratification, no altered text |
| 6 | Loi 2025-056 art. 1, gazette 1408 | Matches; generic authority does not establish unchanged CSS |
| 7 | Loi 2025-056 art. 46 and adjoining arts. 43–49 | Matches; Annex U referenced; enacted annex not supplied/read; no current approval |
| 8 | Ordinance art. 5 alongside arts. 2 and 7 | Matches; both tax point and exigibility borrowed, no assumed universal cash/invoice rule |
| 9 | Art. 6 | Matches; paid contribution deductible for profit tax; unpaid timing withheld |
| 10 | Art. 7, both paragraphs | Matches; domestic VAT deadline/procedure and DGI form |
| 11 | Art. 8 paragraph 1 with art. 7 | Matches; prior-month operations, first 15 days |
| 12 | Art. 8 paragraph 2 with paragraphs 3–6 | Matches; without-notice late declaration branch |
| 13 | Art. 8 paragraph 3 with paragraph 5 | Matches; after-notice late declaration distinguished from continued non-filing |
| 14 | Art. 8 paragraph 4 and its context | Matches for two late-declaration branches; broader interactions explicitly unresolved |
| 15 | Art. 8 paragraph 5 | Matches; 10-day trigger, administrative assessment and increase |
| 16 | Art. 8 paragraph 6 | Matches; nil late declaration has stated fixed penalty |
| 17 | Art. 8 paragraphs 7–8 | Matches; compromised-tax base and bad-faith condition retained |
| 18 | Art. 9 in full | Matches; DGI functions and VAT procedures/guarantees |
| 19 | Arts. 2–3, 5, 7 and 9 | Matches as a refusal to infer relief; no positive export/treaty/PE rule invented |
| 20 | Both ordinance chapters, especially arts. 10–20 | Matches; alcohol levy scope, exemptions and volume base not imported into CSS |
| 21 | DGI digital-services page, dated 2026-08-03 | Matches; generic declaration/payment service only, no claimed CSS menu or boxes |

The reference to uncertain wider penalty interactions is a limit, not approval of any competing interpretation. The second example deliberately avoids those combinations. No research beyond supplied laws was needed to resolve a tax-rule failure. No search chasing missing Annex U was performed in this review.

## Recomputed cases

Independent arithmetic and the repository executable checker agree:

- Case 1: 20,000,000 × 0.005 = 100,000; 20,000,000 − 25,000,000 = −5,000,000; deducting CSS paid gives −5,100,000. No separate profit/minimum tax is computed.
- Case 2: 200,000,000 × 0.005 = 1,000,000; max(1,000,000 × 0.05, 25,000) = 50,000; max(1,000,000 × 0.25, 25,000) = 250,000; totals 1,050,000 and 1,250,000; difference 200,000. The assumed notice branch is explicit and continued non-filing is excluded.

## Legacy and scope preservation

All six old Guide byte streams match both the frozen base and writer hashes, including platform metadata and CTA. The complete destination map contains all 75 legacy headings and bold topic labels: formation 14, corporate 12, income 15, payroll/social 13, overview 11, VAT 10. None of the old bodies contains a table. Spot checks included formation auditor/compliance, income family relief, corporate non-resident withholding, payroll ceiling, overview minimum tax and VAT reverse charge. Those old claims remain unverified; preservation does not recertify them. Lost content restored: 0 (new separate CSS job; no legacy body change).

The top warning at line 18 prohibits stating a 2026 rate, calculating 2026 liability or instructing a 2026 filing. The year is 2025 in frontmatter, the description is historical, the rates-table header and filing section repeat the limit, examples are expressly baseline-only, Sources end with a current-year stop, and README claims no new current coverage. This is a clear instruction to a reader with the full Guide. It is not demonstrated technical enforcement: `tax_year_notes` allows the annual validator to pass, and no MCP retrieval/partial-response or production publication system was tested. Do not convert the passing validator into 2026 approval.

## Validation and exact limitations

- `skill_checks.py` on the new Guide: 15 checks pass.
- `check-examples.py --require` on the new Guide: 2 blocks, 0 failures, 0 missing.
- `validate-guides.py --changed-only --no-index-check`: passes; one warning that the ML SC domain also holds a different payroll/social job.
- `validate-guides.py --no-index-check`: passes; 10 warning groups from unchanged legacy material. Seven Guides checked.
- `coverage-report.py --json`: exit 0; Mali complete=false, all seven core domains remain partial/missing. Global totals are limited by this sparse Mali worktree and are not a full-repository coverage conclusion.
- `git diff --check HEAD^ HEAD`: passes.
- Initial bare validator help attempt without the supplied PYTHONPATH failed because PyYAML was unavailable. With PYTHONPATH, `--help` is not implemented and runs full validation: that invocation failed only on stale generated index/llms inventory, with the legacy warnings. The explicit no-index checks above were then run successfully. No generated file was changed.
- No production/database/MCP test, authenticated portal test, 2026 source approval, accountant attestation, complete 2025 amendment-chain review, commit, push, PR, comment or issue operation was performed. No source PDF, page render or full OCR/text extraction was copied into Git. Original writer receipts were preserved unchanged.

Candidate and private-source hashes, receipt hashes and byte-comparison results are in `candidate-observed.json`; actual successful validation logs are adjacent. Corrected content needs a new candidate hash and a focused recheck before this historical baseline is accepted.
