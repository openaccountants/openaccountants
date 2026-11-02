# Independent Guinea first-draft review, 1 November 2026

Candidate: `ea0fe54f95ca0059c989faabc9195a12a2497208`. Pinned comparison baseline: `a7888d0d6c1f7cb0fed13d8d3f6b7e05f1d12297`. Reviewed by a fresh Codex review agent, independent of the writer. This is a source review, not accountant attestation.

**Result: HOLD for one narrow currentness-control fix.** The 25 legal ledger rows accurately transcribe the March enacted provisions, and all four examples recompute. The two jobs are sufficiently bounded as rate selection from a confirmed CFU base and VAT invoice-field/arithmetic controls. They are not complete liability, valuation, VAT-treatment or filing jobs. All seven country domains must remain partial.

## Finding requiring correction

**P2: turn the known temporal uncertainty into a stop condition in both workpapers.** `gn-property-tax.md` line 20 says to use the replacement where applicable, while lines 35–38 proceed from scope/exemption and valuation inputs to multiplication. `gn-vat-invoice-control.md` line 20 requires the invoicing duty to apply, while lines 47–51 proceed to field controls. Neither operational sequence expressly requires evidence that the March version governs the period or invoice being tested, and neither stops when that cannot be established. Merely listing the October rectification as unconfirmed does not give the model an action when that live uncertainty matters.

Add an explicit prerequisite in each scope and first step: independently establish the governing version for the relevant period/invoice, including whether the October rectification changes it; if that has not been established, keep any result a hypothetical test of the March text and stop before treating it as a compliance conclusion or requesting a correction on a legal basis. This is a control on the admitted source gap, not a demand for a complete consolidated CGI. Do not invent an amendment or say that no later amendment exists. The hypothetical examples should expressly assume the March text governs, including the VAT examples.

The law and decree establish enactment, not a conclusion that every 2026 period uses the same text. The independently opened [DGB projects page](https://dgb.gov.gn/projets-de-lois-de-finances/) lists a rectifying project. The [29 October Assembly account](https://assembleenationale.gov.gn/plfr-2026-intercom/) describes examination. The [1 November embassy article](https://sn.ambaguinee.org/?p=119469) reports adoption of the receipts portion on 31 October. These are leads, not the actual promulgated amendment. No conclusion about its final promulgation or its effect on CGI265/383 VI is made in this review.

## Source actually opened and read

A fresh independent download of the [official DGB law bundle](https://dgb.gov.gn/wp-content/uploads/2026/04/Loi-de-Finances-Initiale-2026.pdf) returned HTTP 200, 10,628,785 bytes, SHA-256 `676d0032a8c1eb447081af70a91700bd4ec484070e3e458f2305d4307298f33b`, identical to the writer's capture. The [DGB 2026 page](https://dgb.gov.gn/2026-lf/) independently opened and links to that law PDF. I rendered the freshly downloaded PDF with Poppler and visually read pages 19,20,21,24,27,28, as well as reading neighbouring law pages 19,22–24 through the existing private OCR. No finding rests only on an HTTP status or search snippet.

Page 20 fully states article 13's replacement of CGI383 VI; page 21 completes its list and fully states article 14's CGI265 replacement. Page 24 bears the law signature/date and publication/repeal clause. Page 27 bears the signed D/2026/0103/PRG/SGG decree, dated 31 March 2026, promulgating L/2026/010/CNT of that date. Its article 2 says the decree takes effect at signature. Page 28 separately cites the same law, decree and dates. The decree's effect-at-signature language is not used as proof of retroactivity or a complete tax-period allocation.

Full PDFs, HTML, OCR and rendered images remain outside Git in the sibling `review-sources/` directory. `sources.json` contains hashes and access results only. The embassy capture hash differs from the writer's HTML because its response is dynamic; the independently read substantive article still reports the same adoption event. Assembly direct HTTP returned 403, but the web tool opened the official article and its substantive paragraphs.

## All 25 ledger rows

Each row below was checked against the rendered statute, including its conditions and surrounding replacement text. `P` denotes the property ledger, `V` the VAT invoice ledger. A pass means accurate against the March source; it does not resolve the currentness hold above.

| Row | Provision visually checked | Finding |
|---|---|---|
| P1 | Decree arts.1–2, p.27, law signature p.24, corroboration p.28 | Pass: law number/date, promulgation, signed date; no retroactivity inference |
| P2 | CGI265 first bullet, p.21 | Pass: owner-occupied residential, 2%, actual annual rental value |
| P3 | CGI265 second bullet, p.21 | Pass: owner-occupied professional, 10%, actual annual rental value |
| P4 | CGI265 third bullet, p.21 | Pass: rented, 15%, actual annual rental value |
| P5 | CGI265 fourth bullet, p.21 | Pass: completed and unoccupied, 5%, estimated annual rental value |
| P6 | All four CGI265 bullets, p.21 | Pass: rental value is annual; actual/estimated distinction retained; no purchase-price denominator |
| V1 | Decree arts.1–2, p.27, law signature p.24, corroboration p.28 | Pass: same limited enactment conclusion as P1 |
| V2 | CGI383 VI 1°, p.20 | Pass: supplier name/address |
| V3 | 2°, p.20 | Pass: acquirer/recipient name/address |
| V4 | 3°, p.20 | Pass: supplier NIF and VAT key |
| V5 | 4°, p.20 | Pass: recipient NIF/key only for services for which recipient liable under 373 bis II |
| V6 | 5°, p.20 | Pass: 373 bis reference and customer-liability statement when customer liable |
| V7 | 6°, p.20 | Pass: fiscal representative condition, its NIF/key/name/address, 373 quinquies reference |
| V8 | 7°, p.20 | Pass: unique number, chronological and continuous sequence |
| V9 | 8°, p.20 | Pass: invoice date |
| V10 | 9° a/b, p.20 | Pass: supply/service date and advance-payment date, if different from invoice date |
| V11 | 10°, p.20 | Pass: for each supply, quantity/precise description/unit price excluding tax and applicable rate or Code exemption reference |
| V12 | 11°, p.20 | Pass: transaction-linked discounts acquired and quantifiable at transaction |
| V13 | 12°, p.20 | Pass: total VAT exigible on transaction |
| V14 | 13°, p.20 | Pass: total excluding tax |
| V15 | 14°, p.21 | Pass: total including all taxes |
| V16 | 15°, p.21 | Pass: debit election condition and exact mandated wording/reference |
| V17 | 16°, p.21 | Pass: margin regime condition and exact mandated wording/reference |
| V18 | VI opening, p.20, all items | Pass: mandatory and distinct information; conditional fields not universal |
| V19 | 12°–14°, pp.20–21 | Pass: separate tax/net/all-tax totals; arithmetic control does not establish a VAT rate |

Short French anchors checked include `valeur locative réelle annuelle`, `valeur locative annuelle estimée`, `une séquence chronologique et continue`, and `lorsque le client est redevable de la TVA`. The exact debit and margin legends in the Guide match the scanned wording, subject only to typographic apostrophe/quotation marks. None of the cross-referenced eligibility articles is silently treated as read or established.

## Four independently recomputed cases

| Case | Independent recomputation | Result |
|---|---|---|
| Residential CFU | GNF60,000,000 × 0.02 | GNF1,200,000 |
| Vacancy versus rental | GNF120,000,000 × 0.05 = GNF6,000,000; × 0.15 = GNF18,000,000; difference | GNF12,000,000 |
| Invoice totals | 20,000,000 + 30,000,000 net; 3,600,000 + 5,400,000 tax; net + tax | GNF50,000,000 / 9,000,000 / 59,000,000 |
| Invoice discrepancy decision | 40,000,000 + 7,200,000 = 47,200,000; abs(48,000,000 − 47,200,000) | GNF800,000, return for correction under workflow |

The CFU comparison is correctly limited to one tax component, with no invented valuation method. VAT amounts are supplied validated inputs, not an asserted 18% statutory rate. The second VAT case is a control decision. The currentness assumption should be explicit in the VAT cases before they are used as examples for a live invoice.

## Preservation and scope

All six legacy files were independently compared as complete bytes against the pinned baseline and frozen candidate; all are identical. Complete frontmatter and the entire suffix after `<!-- openaccountants-cta-block -->` match. File SHA-256 values and the common CTA-suffix hash appear in `preservation.json`. No legacy figure is reverified by this review.

The 65-row destination map contains all 59 old bullet-topic labels plus one context row for each of the six files. Automated exact label comparison passed for every file, and I read the old bodies and map, including company-law fees/capital, mining/minimum-tax/withholding, the individual band-period issue, CNSS branch splits/ceiling, the overview currency/calendar assertions and VAT cross-border claims. Their stated destination remains the byte-identical historical file; none is relabelled as current law. Lost content restored: 0. No content was removed or rewritten in this batch.

README honestly keeps IT-IND, IT-CORP, VAT, SC, PR, TP and XB partial. The VAT `covered_by` pair distinguishes the historical VAT summary from the new invoice-control job. CFU is listed as a bounded job and does not claim a completed seven-domain cell. Unknown scope, exemptions, valuation, deadlines, forms, sanctions and cross-border rules are expressly held out. This review does not demand missing filing instructions for a job that intentionally stops at an internal workpaper.

## Independent executable checks

`checks.json` records the exact commands and output from this reviewer. Both new Guides pass all 15 shape checks. Scoped validator passes with the same two routing warnings: property slug is outside its seven-domain classifier, and VAT already contains the distinct legacy job. Strict metadata integrity reports 0 errors/warnings/notices. All four `oa-check` blocks pass. Pinned baseline-to-candidate whitespace check passes.

These checks do not settle the currentness control finding. No full-repository test run, generated index/package build, live MCP serving check, complete consolidated CGI review, or full seven-domain legal research was performed. No draft/ledger/initial receipt was edited. No commit, push, PR, external comment, attestation or issue closure was made. Only this review-evidence directory was added.
