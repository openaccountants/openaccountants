# Independent Slovakia F11/F23 VAT delta review

PASS on the source, computation and no-loss checks for the two frozen Guides below. Two review findings were fixed and rechecked. This review covers the F11 forms and F23 publication-rate delta only; it does not attest the rest of the Slovakia pack or adopt authorship of any other active PIT/CIT changes or original pack findings.

| Final Guide | Version | SHA-256 |
|---|---|---|
| slovakia-vat-return.md | 2.3 | `3736801e9f36dd741fdd1294d5ec10af84038f0432468dbdb885c283921b62ac` |
| slovakia-vat-registration-4-7-7a.md | 1.3 | `f9639a246420161adbe0f4d1fbc452c98fa13fb3c6feecde7944578a2ff3ec30` |

Baseline: commit `265f91ff`. Review date: 27 October 2026. Complete baseline/final snapshots, exact diffs and metadata checks are in this directory. No Guide or Git edits were made by this reviewer; root applied the corrections.

## Actual primary-source checks

Seven actual source bodies were freshly downloaded with normal TLS and independently hashed: the official active catalog, DPHv25 PDF, KVDPHv25 form607 HTML, REGDPv24 form589 HTML, statutory Annexes 7/7a PDFs and the current 2026 VAT Act HTML. All three form bodies and both annex PDFs match the retained source bodies byte-for-byte. The catalog is a living page and is independently retained rather than treated as a static hash invariant. Fresh official web opens also confirmed form versions and bodies. Source URLs, raw hashes, sizes and exact read scopes are in `actual-primary-read-receipts.json` and `fresh-source-receipts.json`.

| Check | Actual primary evidence and conclusion |
|---|---|
| Period-valid identifiers | The [official catalog](https://www.financnasprava.sk/sk/katalog-formularov) identifies DPHv25 from 1 July 2025, KVDPHv25 from 1 January 2025 and REGDPv24 from 1 January 2025. The Guide correctly separates version suffix from the filing period and limits the catalog observation to the read date. |
| DPH output matrix | Actual [DPHv25, MF/007833/2025-731](https://pfseform.financnasprava.sk/Formulare/VzoryTlaciv/DPHv25.pdf), pages 2 and 3, was independently text-extracted and visually inspected. All 19% / 5% / 23% pairs match: ordinary supplies 01/02, 01a/02a, 03/04; EU acquisitions 05/06, 05a/06a, 07/08; recipient liability 09/10, 09a/10a, 09b/10b; second acquirer 11/12, 11a/12a, 11b/12b; qualifying import self-assessment 11c/12c, 11d/12d, 11e/12e. |
| Other DPH rows | Actual form labels match exempt total 13 and subsets 14/15, special tax 16, output total 17; input totals 18/18a/19 and domestic/customs/self-assessed-import subsets 20/20a/21, 22/22a/23, 23a/23b/23c; correction lines 24–29, registration deduction 30, traveller refunds 31, liability/excess 32/33, prior excess offset 34, payable 35 and supplementary differences 36/37. The Guide correctly warns against double-counting subsets or treating an account credit as current input entitlement. |
| KV sections and boundaries | Actual [KVDPHv25 form607](https://pfseform.financnasprava.sk/Formulare/eFormVzor/DP/form.607.html) confirms A.1/A.2, B.1/B.2, C.1/C.2 and D.1/D.2 descriptions. B.3.1 is strictly below EUR 3,000 of deducted VAT on the relevant simplified invoices for the period; B.3.2 is EUR 3,000 or more, grouped by supplier. The form's explanatory notes confirm supplementary code 1 deletes a record and code 2 adds a new record. |
| Registration selection | Actual [REGDPv24 form589 Annex 1](https://pfseform.financnasprava.sk/Formulare/eFormVzor/REG/form.589.html) has the described mandatory event selections, separate §4(5)/(7) notices, ordinary §4(7) application with §4(6)(a), §4(8)(a)/(b) elections, §7(1)/(2), §7a and §4(11) notice. The [current Act §4(6)–(13)](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-4) confirms that selecting a form box does not change the statutory timing, prior-decision-delivery condition or interim-registration mechanics. |
| Printed publication gates | Actual [Annex 7](https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2004/222/20260101_5815198-2.pdf), operative page 5, was independently rendered and visually read. The ex4901 gate excludes advertising/advertising notices individually or together over 50%; ex4902 also excludes erotic content over 10%. The final Guide explicitly names those tariff categories, avoiding a blanket extension of their gates to distinct picture-book, music or physical-medium categories. |
| Online/audio gate | Actual [Annex 7a](https://static.slov-lex.sk/pdf/prilohy/SK/ZZ/2004/222/20260101_5747469-2.pdf), its complete one-page table, was independently rendered and read. CPA 58.11.30 online books exclude advertising over 50%; the stated audio-recording route excludes narration of online-book content below 50%. Thus the equality boundaries in the Guide are correct. The [current Act §27(3)](https://static.slov-lex.sk/static/SK/ZZ/2004/222/20260101.html#paragraf-27) ties Annex 7 points 2/3 and Annex 7a point 2 to 5%. |

## Independent findings and closure

| Review finding | Fix checked in final bytes | Status |
|---|---|---|
| SKFORM1: the new REGDP source row was outside the existing table, initially separated by prose and then still by an intervening blank line. | Row is now directly contiguous with the prior source row; its exact wording and URLs remain. | Closed |
| SKFORM2: generic “printed books” advertising wording obscured the precise tariff/CPA category boundaries. | Final rates rows explicitly identify ex4901, ex4902 and CPA 58.11.30. No additional rate was invented. | Closed |

No unresolved tax-content or mapping defect was found in this delta.

## Independent computations and no-loss

`recompute.py` uses independent Decimal arithmetic without importing the writer's controls. Restaurant output is EUR 9,200 + 500 + 380 = 10,080; minus EUR 4,600 deductible input gives EUR 5,480 in 32/35 with the stated no-correction/no-offset facts. Consultancy output is EUR 6,900 + 460 = 7,360; deductible input is 460 + 2,875 + 1,150 = 4,485; liability is EUR 2,875. The input-rate split remains dependent on actual invoices rather than an invented allocation. KV invoice classification in the examples agrees with the actual sections.

Both registration examples were independently recomputed: the EUR 200 service produces EUR 46, non-payer cost EUR 246 and zero net VAT for the equivalent fully eligible payer service. Prior turnover is EUR 49,500; ordinary variant EUR 54,000; net-price crossing variant EUR 63,500 with EUR 3,220 VAT and EUR 17,220 total. Extracting VAT from fixed EUR 14,000 gives EUR 11,382.11 net and EUR 2,617.89 VAT; that arithmetic is not treated as resolving the registration circularity.

Three independent KV boundary controls and ten publication-content boundary controls pass, including exactly EUR 3,000, exactly 50% advertising, exactly 10% erotic content and exactly 50% qualifying narration. Content percentages assume the stated actual tariff/CPA classification; the arithmetic does not classify an unrelated product.

Each Guide retains exactly two byte-identical original `oa-check` blocks. The final checker reports two files, four blocks, zero failures and zero missing; focused diff checking passes. All original source URLs, methods, examples, platform metadata, team attribution, contributor byline and complete CTA suffix remain. Only the respective version changes among frontmatter keys. Each Guide retains nine substantive H2 sections and six intake questions. Lost content restored: 0; no prior substantive method was removed. The publication scopes were corrected, and the obsolete unknown-form reservations were replaced by verified mappings.

## Explicit limits and format provenance

The annual §50 zero-included-supplies-denominator reservation remains explicit. So do the unresolved application of first-breach relief to the control-statement fine, the fixed-gross crossing-price registration circularity and the date-dependent ECB-rate reservation. This review does not settle those issues or any other original pack finding.

The process history must be described accurately: F11's format-options record preceded its edit. F23's format-options record was saved in the same operation **after** the rates edit. That is a retrospective record, not a prior draft-options step. This timing is recorded from the root operation history supplied with the task; the reviewer does not infer sequencing merely from filesystem timestamps. The F23 draft-first sequencing deviation is disclosed and is not retrospectively claimed compliant. The source/content/no-loss PASS does not erase that historical process fact.

No whole-pack PASS, accountant sign-off or tier upgrade is made.
