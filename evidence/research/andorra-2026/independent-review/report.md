# Independent Andorra whole-pack review

Reviewed on 27 October 2026. Candidate **32d4e3e8c3121fa37fa7648b5343116dacd08cc4**. Published baseline **5254033fda891adceb3c98aec1f508e3b21f85f5**. Merge checkpoint **43a766a09b91b45392ee0522e5f69d9e2e6306b2**.

**Decision: request changes before country publication.** Four P2 findings below require correction or the expressly offered accurate scope limitation. The computational controls pass. No Guide was edited by this reviewer, and no commit, push, merge, external message or CLA action was performed.

This was one fresh review of all six computational Guides and the README, after reading this checkout's AGENTS.md and docs/skill-template.md. I read the entire original bodies, not only the writer's outline, and compared them with the candidate and removed-and-why.md. The two unchanged 2025 formation/overview files are supporting documents, not evidence of 2026 computational coverage. Evidence is in computations.json, preservation.json and coverage-andorra.json beside this report. Findings refer to candidate line numbers.

## Findings

### F1 — P2 — Digitalisation credit wrongly has a EUR 1 million minimum

- **File:** skills/international/andorra/ad-corporate-income-tax.md:95.
- **Problem:** “with the EUR 1 million minimum and prior certification” denies relief to smaller qualifying projects. The threshold changes the certification requirement; it does not establish a minimum qualifying project cost.
- **Primary source:** [IS Law 95/2010 art. 44(2)](https://www.portaljuridicandorra.ad/L2010095), independently fetched and checked against the retained article text. Annex III supplies eligible project classes.
- **Exact fix:** Replace that clause with: “The digitalisation credit is 2% of qualifying Annex III project costs. Prior tax-administration certification is required when the deduction base is EUR 1 million or more; this is not a minimum project size.” Keep the existing same-expenditure incompatibility and combined-floor rules.
- **Publication:** Blocks until corrected. Apply the corrected companion method wherever IRPF/PE imports it.

### F2 — P2 — Resident movable-capital withholding was lost in the rewrite

- **File:** skills/international/andorra/ad-income-tax.md:70; original income lines 477–484, especially 482.
- **Problem:** The new filing section routes employment withholding but drops the original resident investment-withholding subject. A reference to actual forms in the writer's removal inventory does not preserve the statutory method. It is neither carried into another Guide nor precisely listed as unconfirmed.
- **Primary sources:** [IRPF arts. 50(2), 50(6), 50(9), 51(4)–(7)](https://www.portaljuridicandorra.ad/L2014005); [regulation arts. 37–39](https://www.portaljuridicandorra.ad/R20231229D). Both the general rate and the option are established without waiting for a future form.
- **Exact fix:** Add a compact movable-capital withholding paragraph: ordinary taxable gross receipts have 10% withholding; the taxpayer can elect the article 37 EUR 3,000 reduction through the official communication, tracking all payers to avoid duplication and promptly updating changed eligibility. Apply the statutory foreign-tax reduction for relevant foreign-security custodians and the exempt-income exception. Give quarterly remittance and January summary, with the financial/insurance-entity audit-report exception, under regulation 39. Extend the Sources read scope through arts. 37–39 and correct the preservation inventory. Do not copy the old “only if total below EUR 3,000” shorthand as the full procedure.
- **Publication:** Blocks until restored. This is the **one lost substantive original topic group** identified by the full-body comparison.

### F3 — P2 — Salaried partners' minimum contribution base is missing

- **File:** skills/international/andorra/ad-payroll-social.md:50–56.
- **Problem:** The ordinary actual-pay calculation and below-minimum health-complement discussion omit the separate minimum base for partners included in the salaried/assimilated category. Such a partner could be assessed on actual low pay plus a health-only complement instead of the statutory base floor.
- **Primary source:** [Social Security Law 17/2008 arts. 18, 98(4), 103(1)](https://www.portaljuridicandorra.ad/L2008017), including an independent fetch of art. 98(4).
- **Exact fix:** After the ordinary base paragraph add: “For a partner included in the salaried or assimilated category under article 18, article 98(4) requires a contribution base at least equal to the official monthly minimum wage, even where entitled global pay is lower. Apply the relevant 2026 wage period. This base floor is separate from the article 99 health complement.” Include partner status in the classification workpaper and Sources scope.
- **Publication:** Blocks until corrected. No change is needed to the two existing examples, whose facts are different.

### F4 — P2 — Current ordinary CASS-pension relief is excluded as a historic transition

- **Files:** skills/international/andorra/ad-income-tax.md:44,171; README.md:12,24.
- **Problem:** The Guide advertises pension computation but excludes historic pension rules wholesale. The current fifth additional provision still governs CASS pensions for a broad existing pensioner cohort, and changes taxable pension income. This is not an optional specialist scheme.
- **Primary source:** [IRPF fifth additional provision, read with the 1 January 2015 application date](https://www.portaljuridicandorra.ad/L2014005). Also checked the Government's retained IRPF 2025 manual pension section; the current law controls the 2026 treatment.
- **Exact fix:** Add: “For covered CASS pensions/benefits where contributions began before 1 January 2015, reduce the receipt by 1% per pre-2015 contribution year, rounding a fraction of a year up. Eligibility requires at least fifteen CASS contribution years when the benefit starts; the reduction is capped at 30% of the receipt.” Obtain the contribution history and apply before the ordinary net-income calculation. Remove this rule from the generic historic-pension exclusion and add the provision to Sources. Alternatively, explicitly add this missing ordinary pension computation to README's IT-IND partial reason and narrow the advertised pension scope.
- **Publication:** Blocks the present narrow partial/scope claim until one of those fixes is made. It is not counted as lost original content because the original did not supply this method.

### P3 precision improvement — Employment-credit maintenance period

At corporate line 95, “Maintain qualifying employment for one year” should say “Maintain the incremental average workforce, and the required enhanced-category worker count, during the year following the tax-period close.” [IS art. 44(1)](https://www.portaljuridicandorra.ad/L2010095) and [regulation art. 33(2)](https://www.portaljuridicandorra.ad/R20231229C) anchor the period at closing, rather than each hire date. This clarification is recommended with F1's paragraph edit, but is not a separate publication blocker.

## Primary evidence actually checked

The writer's conclusions were not treated as authority. I used the retained raw HTML/text/article extracts and official PDFs in ../work/sources, and independently fetched the key laws, registers, authority pages, ruling and treaty syntheses online. Some authority pages include navigation; only relevant substantive text was used. The web fetch of R20150527A failed; its retained primary text and the live CASS authority page supplied that read. No CAPTCHA was bypassed.

| Authority | Provisions/read scope checked |
|---|---|
| [IRPF Law 5/2014](https://www.portaljuridicandorra.ad/L2014005) and [version register](https://www.portaljuridicandorra.ad/L2014005_F) | Residence, exemptions, income classes, work and sole-trader expenses, objective/rental options, property, loss pools, personal/family/home/pension reductions, bonus, credits, withholding, returns/refunds, sanctions; fifth additional provision. Key text independently fetched. |
| [IRPF regulation](https://www.portaljuridicandorra.ad/R20231229D) | Arts. 14, 18–19, 20–40: reinvestment approval, pension instrument, advances, withholding and communications, ordinary adjustment and investment withholding. |
| [IS Law 95/2010](https://www.portaljuridicandorra.ad/L2010095) and [register](https://www.portaljuridicandorra.ad/L2010095_F) | Arts. 6–23, 38–46, filing/refund/sanctions and Annex I; related-party/CbCR provisions and property surcharge. Key text and art. 44 independently fetched. |
| [IS regulation](https://www.portaljuridicandorra.ad/R20231229C) | Arts. 3, 7–14, 32–34, 37–38, 45: transparency, pricing, CbCR, holding, credits, advances, filing. |
| [IRNR Law 94/2010](https://www.portaljuridicandorra.ad/L2010094) and [regulation](https://www.portaljuridicandorra.ad/R20231229B) | Source/PE and separate-accrual framework, exemption/base/rates, property, PE overrides/cessation, withholding, representative and refund/sanction rules; regulation arts. 17–34. Law independently fetched. |
| [IGI Law 11/2012](https://www.portaljuridicandorra.ad/L2012011) and [regulation](https://www.portaljuridicandorra.ad/R20140702A) | Status/aggregation, rates, place/accrual/base, imports/reverse charge, deduction/vehicles/blocked inputs, corrections/refunds/closure, filing and sanctions; regulation threshold/options, returns and invoices. Law independently fetched. |
| [Social Law 17/2008](https://www.portaljuridicandorra.ad/L2008017), [contribution regulation](https://www.portaljuridicandorra.ad/R20150527A), [CASS employee page](https://www.cass.ad/cotitzacions-recarrecs-sancions), [CASS self-employed page](https://www.cass.ad/cotitzacions-del-treballadors-per-compte-propi) | Classification and registration; arts. 93–104, 108–109, 205, 223 quinquies, sanctions; regulation arts. 7,15,18–21,25,29–30. Law/CASS pages independently fetched. |
| [January minimum circular](https://www.cass.ad/sites/default/files/arxius/Circular%20informativa%20Salari%20m%C3%ADnim%202026.pdf), [July minimum circular](https://www.cass.ad/sites/default/files/arxius/Circular%20informativa%20salari%20m%C3%ADnim%20a%20partir%20de%20l%271%20de%20juliol%20del%202026_0.pdf), [average-wage announcement](https://www.govern.ad/ca/w/el-salari-mitja-de-l-any-2026-se-situa-en-2-672-52-euros), [health-complement sheet](https://www.cass.ad/sites/default/files/arxius/CASS_COMPLEMENT%20ART99%20COMPTE%20PROPI%20fitxa%2002-02-2026.pdf) | Dated wage values/effective periods, average-reference year, full-month complement method and partial-month authority instruction. Average announcement independently fetched. |
| [General Tax Law](https://www.portaljuridicandorra.ad/L2014021), [2026 Budget](https://www.portaljuridicandorra.ad/L2026001), [Labour Law](https://www.portaljuridicandorra.ad/L2018031) | General arts. 23–25, 125–132; budget art.17; labour pay, in-kind, affiliation and fine provisions. Budget independently fetched. |
| [Law 5/2025](https://www.portaljuridicandorra.ad/L2025005), [Law 5/2023](https://www.portaljuridicandorra.ad/L2023005) | Housing amendments 78–80, fifth transition; direct-tax application/transitional provisions. Housing law independently fetched. |
| [CV0366-2026](https://www.govern.ad/ca/l/8302354), [CV0312-2024](https://www.govern.ad/ca/l/4194426), [benefits response](https://www.govern.ad/ca/l/4193406) | Actual response versus taxpayer's proposed interpretation, migration/participation result and its equivalent-facts limit; inventory-car/private-use versus investment assets; employment benefit classification. Migration ruling independently fetched. |
| [Spain authority synthesis](https://www.hacienda.gob.es/SGT/NormativaDoctrina/tributaria/cdi/textos-sinteticos/cdi-ts-andorra-sp.pdf), [France authority synthesis](https://www.impots.gouv.fr/sites/default/files/media/10_conventions/andorre/version-consolidee-de-la-convention-avec-andorre-modifiee-par-la-convention-multilaterale.pdf), [Spain authentic treaty](https://www.boe.es/buscar/act.php?id=BOE-A-2015-13248), [Government directory](https://www.govern.ad/ca/tematiques/impostos-taxes-i-duana/impostos-en-andorra/convenis-per-evitar-la-doble-imposicio) | MLI application notes, authority/authentic-text hierarchy and selected arts. 4–7,12,14–15. Both syntheses independently fetched. No exhaustive treaty/exchange matrix certified. |

The portal labels its consolidations as lacking official legal status. The candidate says that correctly; it must not call them authentic gazette enactments. Current registers and the cited amendments/application provisions support the periods reviewed. Authority syntheses expressly defer to authentic treaty/MLI texts. The selected Spain/France methods match the checked texts; no new treaty finding arose.

## Remaining limits and ordinary coverage

Keep the **existing IT-IND partial**. IRPF art.35 establishes the annual dependant-income test; art.36 looks to circumstances at accrual. Both dated 2026 wage circulars are available, and the Government's 2025 manual demonstrates an annual comparator for that year. I did not find a primary authority resolving the exact comparator where 2026 wages changed mid-year. Weighted annual pay and a year-end monthly wage annualised are different figures; neither was silently certified. This is a real identified limit, not a gap created merely because a 2027 form is unavailable.

The two/four-year wording in article 5(r) is actually present. The candidate correctly supplies the four-year substantive condition, flags the inconsistent closing reference and routes disputed relief through prior approval. I found no basis to replace either with an invented harmonised period.

CASS regulation 29's old daily surcharge conflicts with the current statutory schedule. Its interest text cannot be described as though the whole article had vanished. The candidate accurately calls it partly superseded and declines a complete enforcement-interest calculation; it does not wrongly use tax interest. The live CASS page separately presents older and post-July-2022 surcharge material. That mix is not sufficient evidence to certify a universal current enforcement assessment or silently assign a starting date/base. Keep the precise stated limit; no new SC partial is demanded solely for this bounded enforcement issue.

Other ordinary methods checked are supplied: actual annual IRPF base/bonus/credit reconciliation; sole-trader and rental rules; ordinary IS adjustments, losses/floor, participation/PE and settlement; ordinary IGI location/base/input/refund/closure; employee and self-employed contribution/withholding workflow; TP independent-price evidence and statutory reporting; IRNR non-PE/PE/property/departure/refunds and selected treaty methods. F1–F4 identify the concrete corrections to that assessment. CbCR live exchange matrices, special IGI schemes and genuinely specialist/sector regimes can remain named outside scope. Absence of a future form alone does not prevent use of a verified statutory method. The country cannot be described as fully complete while the documented annual dependant benchmark remains unresolved.

## Content preservation and rule 11

The byte-exact original archives match baseline. The merge checkpoint did not change any original country file. The income candidate is **46.44% shorter by bytes**, triggering rule 11. Other computational candidates do not exceed the 25% shrink trigger (payroll is 18.25% shorter; the other four grew).

Independent whole-body comparison supports the writer's removal classification for repeated bank/vendor heuristics, duplicate worksheet layouts, obsolete/unsupported rate claims and corrected assumptions. Every original computational topic group is retained in the new ordinary methods, routed to its correct companion, or expressly identified as unsupported/outside scope **except the resident movable-capital withholding group in F2**. The six old income narratives and twelve payroll example/test scenarios are not treated as valid regression expectations where their law assumptions were wrong; their subjects remain in the current base and companion methods and their exact original text remains archived. This is substantive comparison, not approval based on an outline.

| Original material read | Independent disposition |
|---|---|
| Income: quick reference, CASS tables/defaults, receipt/expense/software/utilities/travel/exclusion tables, bank formats, all six examples, rules 5.1–5.11, edge cases 6.1–6.9, worksheet, glossary/onboarding, treaties/other taxes/penalties, all tests/prohibitions | Preserved/corrected or expressly unsupported in the new income, payroll, IGI, corporate and XB routes; **F2 requires one restoration**. |
| Payroll: salary/withholding/deduction/savings/gain tables, nonresident methods, CASS/retired/base/ceiling/floor, wages/defaults/inputs, patterns/forms/filing/registration, penalties, six examples and six tests, workbook/glossary/payslips/onboarding/prohibitions | Subjects retained with current methods or precise unsupported-item list; faulty gross-salary bands, forms and post-hire grace assumptions rejected rather than recertified. |
| IGI: all quick figures/box codes/defaults/red flags, registration/refusals, nine vendor groups, six examples, classification/input/import/vehicle/entertainment/customs/traveller/property/mixed-use rules, workbook/onboarding/gaps | Legal subjects retained/corrected, or specialist scope and unsupported old claims identified. Vendor/box labels are not legal evidence. |
| Corporate: all original base, advance/refund, IP/nexus/authorisation, holding/participation, losses/floor/ownership, expense and withholding topics, five controls | Subjects retained. Three controls moved unchanged; two remain unchanged in Guide. |
| TP: complete original relation, market value, documentation, financing, agreement/deemed acceptance/effect/report/modification, CbCR content/scope/notification/report/confidentiality, both controls | Retained; ordinary method/enforcement expanded. Both controls unchanged. |
| XB: complete original source, PE/representative/liability, non-PE base/exemption/property, accrual/withholding/declaration/records/refunds, three controls | Retained and ordinary PE/treaty methods expanded. Rent control moved unchanged; service/property controls unchanged. |

**Lost content restored: 0**

That count records actual reviewer edits, which were expressly prohibited. **One lost original topic group is pending writer restoration (F2)**. After the writer restores and verifies it, record “Lost content restored: 1” with the fixing commit and lines. Do not copy a zero count into a claim that no content was lost. F3/F4 are scope defects, not additional losses from the original.

All six Guide slugs, existing dependency values, team bylines/trust labels, platform-owned fields and CTA suffix bytes are unchanged. Formation, overview and the three earlier Andorra research files are untouched. No tier-1 attestation was introduced. All **ten original oa-check blocks** survive byte-exact: six in the Guides and four in supplementary research.

## Verification results

- `check-examples.py` on the six Guides plus three supplementary files: **9 files, 20 controls, 0 failures, 0 missing**. Exactly two controls in each Guide. All expected fields were recomputed using Decimal arithmetic; scenario law/facts checked separately. `computations.json` records every result.
- Four boundary methods pass: combined loss/credit floor, PE cessation gain, ordinary 25% health complement across July, and company migration share gain.
- `validate-guides.py --no-index-check`: **passed**, checking 2,263 Guides and 6,122 generated package frontmatter blocks. Existing repository warning groups: 795 missing Sources, 5 stale, 5 jurisdiction exceptions. No generated files were edited. Index freshness was intentionally excluded by this required command.
- `coverage-report.py --json`: exit 0; Andorra has six domains present, IT-IND missing from the complete set because of its explicit partial, `complete: false`, and no accountant-reviewed Guides. The mechanical report counts eight files; the two supporting documents are excluded from this legal review's current-year evidence.
- Protection/archive/control-preservation checks: passed. Review helper initially passed complete Markdown to the frontmatter-only parser and failed; corrected its input to the frontmatter block, reran, and all checks passed. This helper failure did not touch candidate files.
- No endpoint/database/filing submission was made. No CLA consent was given. `resp.txt` was neither read, deleted nor staged.

The writer should fix F1–F4, incorporate the P3 clarification, rerun the targeted checks, and record the exact repair commit with this report. This report approves no merge of the uncorrected candidate and does not certify the remaining IT-IND benchmark.
