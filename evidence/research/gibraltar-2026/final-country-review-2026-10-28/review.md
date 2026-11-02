# Gibraltar: independent country new-material review

**Changes required at candidate `42fe0cf1ceaa767ac1853921ba1e1ba8cdf4ae65`.** All 333 ledger rows were reviewed. There are three actionable findings affecting four rows: two precise individual-Guide corrections and one payroll evidence correction. No additional actionable finding was identified in corporate or transaction-tax material. This is an independent AI source/editorial review of source-cited drafts, not professional attestation or a country-complete finding.

Reviewed on 28 October 2026 by a separate reviewer agent with no writer context at dispatch. No delegation, Guide edits, commits, pushes, external comments/messages, live filings/payments or paid API work occurred. Writer repair messages received during review do not change this pinned initial disposition. Closure requires an exact repair revision.

## Scope and checked population

| Candidate | Rule rows checked | Source proof units | Quote snippets checked |
|---|---:|---:|---:|
| Corporate `gi-corporate-tax` v0.19 | 118 | 118 | 372 text |
| Individual `gi-individual-income-tax` v0.10 | 60 | 87 | 457 text |
| Payroll `gi-payroll-social-insurance` v0.15 | 105 | 117 | 586 text plus 51 visual |
| Transaction tax `gi-transaction-tax-transition` v0.9 | 50 | 63 | 502 text |
| Total | **333** | **385** | **1,917 text plus 51 visual** |

[The complete row results](row-check-results.json) list every checked ID, claim, exact candidate, canonical-ledger location, proof, official URL, source hash, quote count, semantic disposition and finding. Corporate combines its 19 `rows` with its 99 `inherited_source_matched_rows`. Four rows require repair; the other 329 are supported within their stated assumptions and limits.

Read `OWNERS.md`, `AGENTS.md` and `docs/skill-template.md`; applied primary-source, nine-section, two-main-example, preservation and independent-review requirements. Read the pack README and finite ordinary-check records. The earlier accepted interest/foreign-exit methods and their 32 review/research files were checked for preservation, not reopened or treated as acceptance of these four new candidates.

## Findings

### GI-R1, P2: preserve the IT1 taxpayer-type/year distinction

Location: `skills/international/gibraltar/gi-individual-income-tax.md:271`; canonical individual ledger `IND-60`, line 70; proofs `IT1p1` and `ITGyear`.

The Guide describes the current IT1 allowance/election part as applying to the year commencing 1 July 2026 without the form's taxpayer-type distinction. Complete rendered page 1 says:

- PAYE/HEPSS: year commencing 1 July 2026.
- Other: year ending 30 June 2026.

This matters for trade, partnership, rental, trust/foundation and dividend cases routed as Other. The [official IT1, page 1](https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Employers/Tax_ReturnForm2026.pdf) and [official guidance, income/allowance-year explanation](https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Tax%20Returns/Tax%20Return%20Guidance%202026_.pdf) support that distinction. The saved IT1 SHA-256 is `0424f1e3bc81a6ea7040cba4892561bd88abcbcbaedd1a38a2977fce72b4efc6`.

Correction: state both periods explicitly in the Guide and IND-60. Preserve the correct 2025/26 income period, current maintenance/interim PDF route, 30 November 2026 receipt deadline, category mailboxes, ID and representative-authority conditions. This is not evidence of release of the future return for the year ending June 2027.

### GI-R2, P2: identify the claimant in the custody-deduction condition

Location: `skills/international/gibraltar/gi-individual-income-tax.md:159`; canonical ledger `IND-40`, line 50; proof `A12`.

The table says “a spouse/partner must not be entitled to rule 7 relief.” [Allowances Rules 12, printed page 22](https://www.gibraltarlaws.gov.gi/uploads/legislations/income-tax/1992s016/1992s016(23-03-26).pdf) instead tests the claimant: “if a spouse or civil partner, he is not entitled” to claim under rule 7. The Guide can be read as testing the other partner's entitlement. The source SHA-256 is `b3254638de0d50d6547bf7efc77e09ca8042f8bf27f941d533b2c5040bb947e0`.

Correction: state that, if the claimant is a spouse/civil partner, **the claimant** must not be entitled under rule 7. Make IND-40 equally precise. The £5,800 amount and separate joint-custody conditions are supported and need no change.

### GI-R3, P2: replace a contents-page proof with the operative page

Location: canonical payroll ledger `### Proof SGadmin`, line 1361; linked rows `PAY-P057` and `PAY-P059`, lines 59 and 61. Related Guide text is `gi-payroll-social-insurance.md:322` and its £150 reconciliation illustration.

SGadmin quotes only contents entries ending in page 8. Those words exist in the PDF, so a quote-presence test passes, but they do not establish any payment deadline, portal, rate-change authority or assessment/refund condition.

I independently read complete physical page 8 of the [official self-employed booklet](https://www.gibraltar.gov.gi/uploads/Income%20Tax%20Office/Self-Employed/Self-Employed%20Guide%20to%20Social%20Insurance%20post%201st%20July%202025.pdf). It supports the Guide: monthly payment within fifteen days after month-end, the payment portal, written ITO authority before using a different contribution rate, and annual earnings/profits assessment with refund/collection. Its SHA-256 is `1ce3b5b26ca05d8f51c4f92f4ccc1fb8f95d7bc577e6c2cc21c04618b8245ad8`.

Correction: select the operative body occurrence and replace SGadmin with exact page-8 quotations in JSON and canonical Markdown. **No Guide method or arithmetic change is needed.** This finding illustrates why matching quotations alone is not independent source review.

## Source and context verification

Independently extracted text from cached raw PDFs with `pdftotext`, read official HTML/XML, and checked every text quotation against its own URL-paired source. All recorded raw hashes checked matched; no quote-match exception remains. Layout whitespace and repeating headers were normalised; quotations from another document were never substituted. The contents-only SGadmin exception is separately marked as a context failure.

Independently read the CT4 XLS statically with xlrd 2.0.2: all **75 populated cells** agree with the saved extraction. Raw OLE metadata independently confirms the 5 March 2015 save date. The current official link, published postal instructions, separate CT1/CT2 and general-query mailboxes, application timing and Commissioner-decision/surcharge conditions were distinguished. A save date was not turned into legal expiry or a tested filing.

Inspected complete payroll contribution, daily and monthly table images and UK social-security Order pages 10 and 12–15. All **51 visual snippets** agree, including the 2026/27 class/frequency limits, daily code-24 £0.96, grey-cell instruction, monthly code-35 £125.89, employee SI £162.35 and employer SI £243.65. Scanned agreement transcriptions were checked visually; OCR was not quotation authority. Conditions for single-system coverage, 24-month anticipated duration, similar self-employment, dual-territory allocation and employer obligations were preserved.

Inspected complete current IT1 page 1, including its type, year and mailbox tables. Also compared both complete warehousing page-3 renders: regulation 4(3)'s “between one month and nine months” differs from guidance 1.1.4's strict endpoint wording. The transaction-tax Guide preserves that distinction and does not decide the endpoints. The aid-law chain, gross-grant-equivalent/aggregation conditions, special-procedure scope, refund-clock conditions, initial relief period and separate commercial-export refund limitation were checked against their supplied primary sources. No broad new research campaign was started.

## Preservation, arithmetic and validation

[Preservation and shape evidence](preservation-and-shape.json) independently compares the original split `43206e99`, accepted head `b98e7f01` and pinned candidate:

- All **18 original Guide slugs**, protected platform metadata and existing CTAs are preserved.
- All **121 original research records** and **32 frozen accepted research files** remain byte-exact.
- All **47 original executable blocks** remain byte-exact across main Guides and linked supplements.
- All **346 original paragraph destinations** are accounted for. [Twenty-four topic spot-checks](original-topic-spotchecks.json) cover ordinary and edge methods, changed limitations and moved controls. Lost content restored: **0**; none was identified as lost.
- Each of the four rewritten main tax Guides has the **nine canonical sections and exactly two main `oa-check` blocks**.

[Independent example results](example-check-summary.json): **61 executable checks across 28 files, zero failures**. [Additional independent prose arithmetic](prose-arithmetic-results.json): **129 calculations, zero failures**, including CT4 forecasts, rent caps, allowances, loss pools, benefit valuations, contribution classes/periods, surcharges, aid deduction and date-window arithmetic. Assumed eligibility, classification, rates and period facts remain assumptions; arithmetic is not a legal ruling.

Pinned 18-Guide schema validation has **zero errors**, with the inherited minimum-tax `tax_year: 2024` freshness warning. Strict metadata validation against the accepted head checks **four changed Guides with zero errors, warnings or notices**. The **129 repository unit tests pass** with canonical local temporary paths. Repository PR-mode validation (`--no-index-check`) also passes, retaining repository-wide backlog warnings. That broad check ran during the writer's repair worktree; the pinned 18 inputs and examples were validated separately from saved commit bytes.

An initial `validate-guides.py --help` invocation ran full validation because the script does not implement that flag; full mode reported stale generated `index.json` counts. Generated inventories were not edited. `git fetch origin` failed because `github.com` did not resolve in the sandbox; this review uses the exact local commit and saved official-source identities. Remote state is checked separately by the parent task.

## Remaining country scope and disposition

The README correctly leaves **all seven tax domains partial**. Corporate allocation/extended-period/disposal/Gazette questions, individual part-year and relief/credit interactions, payroll recovery/allocation/schedule and benefit-reference questions, customs refund/extension/endpoint and case-specific aid/commodity/transition questions remain unresolved. They must not be erased by accepting these ordinary methods.

The finite record/notice/foreign-credit check remains appropriately bounded: positive statutory documentation duties are already addressed; an unlocated separate local-file form does not prove an exemption. CT1/CT100 do not establish a distinct domestic foreign-credit claim/correction channel. Existing foreign-exit and specialised reporting limits remain genuine. No new contradiction was identified between the reviewed ordinary methods and the retained sibling references.

**The pinned four-Guide candidate is not yet accepted because GI-R1–GI-R3 remain open at that commit.** Corporate v0.19 and transaction-tax v0.9 have no actionable new-material finding within this review's source-cited-draft scope; individual wording and payroll ledger evidence require the bounded repairs above. A closure review must identify the exact repair head and preserve this completed review evidence.

Any later acceptance is limited to independent AI source/editorial acceptance of the four ordinary-method drafts and their explicit limitations. It is not full-country completion, professional or accountant attestation, clearance for a taxpayer's facts, merge authorisation, or closure of issue #398.
