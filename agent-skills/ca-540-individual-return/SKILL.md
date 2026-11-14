---
name: ca-540-individual-return
description: "Prepare California Form 540 for tax year 2026 for a full-year California resident, focused on sole proprietors and single-member LLC owners who file federal Schedule C. Starts from federal AGI and works through Schedule CA (540) subtractions and additions, the items California does not follow (bonus depreciation, the One Big Beautiful Bill Act, section 199A, HSA deductions, the federal SALT and mortgage limits), the California section 179 limit on form FTB 3885A, standard or itemized deduction, the tax from the table or the 2026 rate schedules, exemption credits, the Behavioral Health Services Tax, the AMT small-business exclusion, the renter's credit and CalEITC, payments and filing. Figures live in ca-income-tax. Trigger on \"California Form 540\", \"California state return\", \"Schedule CA\", \"California adjustments\", \"California does not conform\", \"file California taxes self-employed\". Full-year residents only; part-year and nonresidents go to ca-residency-leaving-california."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ca-540-individual-return"
  jurisdiction: "US-CA"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# California Form 540 for a resident sole proprietor or single-member LLC owner, tax year 2026

> **Source-cited draft.** Built from the 2025 California 540 Personal Income Tax Booklet and Form 540, the 2025 Schedule CA (540), Schedule P (540) and form FTB 3885A instructions, FTB Pub. 1001 (2025), the 2026 California Tax Rate Schedules, the 2026 Form 540-ES instructions, the FTB extension page and R&TC 17024.5 and 17043, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Form 540 starts from federal AGI (line 13). Every difference between federal and California law goes on Schedule CA (540): column B subtracts, column C adds. For 2025 and later years California follows the Internal Revenue Code as of January 1, 2025, so it does **not** follow the One Big Beautiful Bill Act of July 2025, and it still refuses bonus depreciation, limits section 179 to $25,000, gives no QBI deduction and no HSA deduction. The tax comes from the FTB tax table (taxable income $100,000 or less) or the 2026 rate schedules in `ca-income-tax`, less exemption credits, plus 1% on taxable income over $1,000,000. The 2026 return is due April 15, 2027; filing (not paying) is automatically extended to October 15, 2027.

## Scope and who this is for

In scope: a full-year California resident filing Form 540 for tax year 2026, who reports a business on federal Schedule C, directly or through a single-member LLC that is disregarded for federal tax. The skill starts from a finished federal return.

| Topic | Where it goes |
| --- | --- |
| The figures (brackets, exemption credits, standard deduction, credit limits, AMT amounts) | `ca-income-tax` |
| 2026 estimated payments, Form 540-ES, form FTB 5805 | `ca-estimated-tax-540es` |
| Health coverage penalty, form FTB 3853, Form 540 line 92 | `ca-form-3853-coverage` |
| Part-year and nonresidents, Form 540NR | `ca-residency-leaving-california` |
| The LLC's own $800 annual tax, LLC fee and Form 568 | `ca-llc-fee-and-tax`, `ca-smllc-form-568` |
| Pass-through entity elective tax | `ca-pte-elective-tax` |
| Employee SDI and payroll | `ca-payroll` |
| The federal return, Schedule C and SE | `us-schedule-c-and-se-computation` |
| The order the whole package is built in | `us-ca-return-assembly` |

## Ask the client first

1. **Resident all year, and the filing status?** California normally follows the federal filing status. Registered domestic partners (RDPs) and some military or nonresident spouses are the exceptions. A part-year year goes to Form 540NR.
2. **The complete federal return**: Form 1040 with Schedules 1, 1-A, A, C, D, E and SE, and Forms 4562, 8995 and 8889, plus W-2s showing California wages and SDI withheld.
3. **A fixed-asset register with California basis and California depreciation to date**, including anything expensed federally under section 179 or bonus depreciation, the total cost of section 179 property placed in service in the year, and any research and experimental costs.
4. **Gross receipts from all trades or businesses**, including pass-through shares. Under $1,000,000, business items stay out of the California AMT.
5. **HSA contributions** (including the employer's, W-2 box 12 code W), HSA interest, dividends, gains and distributions.
6. **Rent paid on a California home, children's ages, SSNs or ITINs, investment income**: the renter's credit, CalEITC and Young Child Tax Credit tests. Also California estimated payments with dates, prior-year overpayment applied, and any California NOL, excess business loss or credit carryovers.

## The method, step by step

1. **Confirm scope and year.** Full-year resident, Schedule C or disregarded single-member LLC, tax year 2026. Where a 2026 indexed amount is not yet published, carry the 2025 amount from `ca-income-tax` and flag it.
2. **Start from federal AGI** (Form 1040 line 11) on Form 540 line 13.
3. **Schedule CA (540), Part I (income).** Enter the business depreciation difference from form FTB 3885A on Section B line 3, the HSA items, Social Security and the other items in the table below. Form 540 line 14 takes Part I line 27 column B; line 16 takes column C. If there are no differences, Schedule CA is not filed.
4. **Schedule CA (540), Part II (deductions).** Compare California itemized deductions with the California standard deduction and use the larger. On a married/RDP filing separately return both spouses use the same method. The client may itemize for California while taking the federal standard deduction, and the other way round; when itemizing only for California, attach a federal Schedule A completed for that purpose. Deductions taken below federal AGI (the QBI deduction and the Schedule 1-A deductions) never reach California and need no entry.
5. **Taxable income** is line 17 less line 18 (line 19). Up to $100,000, read the tax from the FTB tax table; above that, use the 2026 rate schedule for the filing status (`ca-income-tax`). Line 31.
6. **Exemption credits** on line 32, reduced when federal AGI is over the limit. Then the nonrefundable credits, including the renter's credit on line 46. Line 48 is tax after credits.
7. **Other taxes.** Schedule P (540) for the AMT (line 61), the Behavioral Health Services Tax on line 62 when taxable income is over $1,000,000, and line 63 other taxes. Line 64 is total tax.
8. **Payments and refundable credits.** Withholding (line 71), estimated and extension payments (line 72), CalEITC (line 75), YCTC (line 76) and FYTC (line 77) on form FTB 3514.
9. **Use tax and health coverage.** Line 91 use tax ("Do not leave blank"), line 92 the individual shared responsibility penalty or the full-year coverage box (`ca-form-3853-coverage`).
10. **Balance.** Lines 93 to 100 net payments, use tax and the penalty against total tax; line 111 is the amount owed, line 113 any estimated tax penalty from form FTB 5805, line 115 the refund.
11. **File and pay** by the dates in "Filing and payment", and set up the 2027 estimated payments.

### Rates, bands and thresholds

The indexed figures are in `ca-income-tax`. The rules below are the California deduction and adjustment limits this method applies.

| Item | California rule or figure | Source |
| --- | --- | --- |
| Federal SALT limit ($40,000; $20,000 separate) | California has no such limit. Add back, on Schedule CA Part II line 5e column C, the amount federal law actually disallowed | [2025 Schedule CA (540) instructions, line 5e](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html) |
| State income tax, SDI and general sales tax | Not deductible. Remove on Part II line 5a, column B | [2025 Schedule CA (540) instructions, line 5a](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html) |
| Foreign income taxes | Not deductible. Line 6, column B | same |
| Home mortgage acquisition debt | California keeps the $1,000,000 limit ($500,000 separate), not the federal $750,000 ($375,000). Adjust on line 8, column C | [2025 Schedule CA (540) instructions, line 8](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html) |
| Home equity interest | California allows interest on up to $100,000 ($50,000 separate) of home equity debt that federal law suspends | same |
| Qualified conservation contributions | California limit 30% of federal AGI, against 50% federally. Difference on line 12, column B | [2025 Schedule CA (540) instructions](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html) |
| Miscellaneous deductions subject to the 2% floor | Allowed (California did not follow the federal suspension). Part II lines 19 to 22 | same |
| Behavioral Health Services Tax | 1% of taxable income over $1,000,000, any filing status | [R&TC 17043](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17043) |
| California section 179 | $25,000, less the cost of section 179 property over $200,000; capped at business income | [2025 FTB 3885A instructions](https://www.ftb.ca.gov/forms/2025/2025-3885a-instructions.html) |

### What California does not follow

| Federal item | California treatment | Where | Source |
| --- | --- | --- | --- |
| Bonus depreciation, section 168(k), including the OBBBA's permanent 100% for property acquired after January 19, 2025 | Not allowed at any percentage. Recompute California depreciation without it | form FTB 3885A, then Schedule CA Section B line 3 | [FTB Pub. 1001 (2025)](https://www.ftb.ca.gov/forms/2025/2025-1001-publication.pdf) |
| Section 179 | California limit (rates table above). No section 179 for off-the-shelf software or qualified real property; any amount over the business-income cap carries forward. California basis is reduced by the California section 179 amount | form FTB 3885A Part II | [2025 FTB 3885A instructions](https://www.ftb.ca.gov/forms/2025/2025-3885a-instructions.html) |
| Research costs, section 174 and the OBBBA's section 174A | California follows section 174 as it read on January 1, 2015 | form FTB 3885A | [FTB Pub. 1001 (2025)](https://www.ftb.ca.gov/forms/2025/2025-1001-publication.pdf) |
| QBI deduction (section 199A) and Schedule 1-A deductions | Not allowed; they sit below federal AGI, so no Schedule CA entry | None | [2025 Schedule CA (540) instructions](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html) |
| HSA contribution deduction | Not allowed: the federal deduction goes on Section C line 13, column B; the employer contribution (W-2 box 12 code W) on line 1h, column C | Schedule CA Part I | same |
| HSA earnings and distributions | Interest and dividends taxed as earned (column C). A non-qualified distribution taxed federally is not taxed by California (line 8f, column B) | Schedule CA Part I | same |
| Educator expenses | Not allowed (line 11, column B) | Schedule CA Part I | same |
| Moving expenses | Allowed for everyone, not only the armed forces (form FTB 3913) | Section C line 14 | same |
| Excess business loss, section 461(l) | California's own limit and form FTB 3461 (figures in `ca-income-tax`) | Line 8p | [FTB Pub. 1001 (2025)](https://www.ftb.ca.gov/forms/2025/2025-1001-publication.pdf) |
| Social Security and Tier 1 railroad retirement | Fully excluded: the taxable federal amount goes in column B | Line 6 | [2025 Schedule CA (540) instructions](https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html) |
| California lottery winnings | Excluded (other states' lotteries are not) | Line 8b, column B | same |
| Alimony | From 2025 California follows the federal repeal for agreements executed after December 31, 2025 (or modified after it to say so); older agreements keep the old treatment and may need an adjustment | Lines 2a and 11 of Part I | same |

**NOL suspension.** For taxable years beginning in 2024, 2025 and 2026 the California NOL carryover deduction is suspended, except below $1,000,000 of net business income or modified AGI and for disaster losses. The NOL is still computed on form FTB 3805V and carried forward ([2025 Schedule P (540) instructions](https://www.ftb.ca.gov/forms/2025/2025-540-p-instructions.html)).

**2026 federal Schedule A changes.** The OBBBA changes to federal itemized deductions that begin in 2026 (a floor on charitable gifts, a cap on wagering losses, a cap for top-bracket taxpayers) flow into Schedule CA column A. Because California generally does not conform, expect column B or C adjustments; confirm when the 2026 Schedule CA (540) instructions are published.

**Credits.** The renter's credit, CalEITC, YCTC and FYTC are tested on their conditions, not only the income limits (`ca-income-tax` holds both). For a self-employed client, CalEITC earned income is Schedule C profit **minus** the deductible half of self-employment tax, not profit alone (form FTB 3514 booklet, worksheet 3). The $5,000,000 business credit limit does not touch these personal credits.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Taxable income exactly $1,000,000 | No Behavioral Health Services Tax: it applies only in excess of $1,000,000 | [R&TC 17043](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17043) |
| Joint return, taxable income $1,050,000 | Behavioral Health Services Tax $500 on $50,000; the threshold is not doubled | same |
| Business gross receipts $999,999 against $1,000,000 | Below $1,000,000 business items are excluded from AMTI; at $1,000,000 they are included | [2025 Form 540 booklet](https://www.ftb.ca.gov/forms/2025/2025-540-booklet.pdf) |
| Section 179 property placed in service costs $225,000 or more | California section 179 limit is nil | [2025 FTB 3885A instructions](https://www.ftb.ca.gov/forms/2025/2025-3885a-instructions.html) |
| Spouse itemizes on a separate return | This spouse must itemize too | [2025 Form 540 booklet, line 18](https://www.ftb.ca.gov/forms/2025/2025-540-booklet.pdf) |
| Someone else can claim the client as a dependent | Use the California standard deduction worksheet for dependents in the booklet | same |
| Taxable income $100,000 or less | Tax table, not the schedules | [2026 California Tax Rate Schedules](https://www.ftb.ca.gov/forms/2026/2026-540-tax-rate-schedules.pdf) |

### Defaults when a fact is missing

| Missing fact | Default | Why |
| --- | --- | --- |
| No California depreciation history for an asset | Do not copy federal depreciation; rebuild California basis or refer | Bonus depreciation and section 179 differ, so federal Form 4562 is wrong for California |
| Business gross receipts unknown | Assume $1,000,000 or more until shown otherwise and run Schedule P | The AMT exclusion is a benefit the client must qualify for |
| 2026 indexed amount not published | Use the 2025 amount from `ca-income-tax` and flag it on the workpaper | The FTB had not released 2026 amounts on 2026-11-13 |
| Health coverage by month unknown | Do not tick the line 92 full-year coverage box | A wrong tick hides a penalty |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Large federal bonus depreciation or section 179 in the year | A big Schedule CA addition and a separate California asset record |
| HSA held | California taxes the earnings every year |
| SDI or state income tax in federal Schedule A | Must come out for California |
| Mortgage over $750,000 | California may allow more interest than federal |
| An LLC with no Form 568 history | The $800 annual tax and Form 568 may be unfiled (`ca-llc-fee-and-tax`) |

## Worked cases

### Case 1: section 179 over the California limit (computation)

Machinery costing $210,000 was placed in service in 2026 and expensed in full under federal section 179. Schedule C business income before section 179 is well above $15,000. The California section 179 limit is $25,000 less ($210,000 less $200,000) = $15,000. The other $195,000 is depreciated under California rules on form FTB 3885A with no bonus depreciation. The Schedule CA Section B line 3 column C addition is the federal deduction less the California section 179 amount and the California first-year depreciation; with an assumed California first-year depreciation of $27,866 (7-year property, half-year convention, 14.29%), the addition is $167,134.

```oa-check
name: CA section 179 limit and Schedule CA addition (2026)
inputs:
  cost: 210000
  federal_deduction: 210000
  ca_rate: 0.1429
steps:
  - ca_179: max(25000 - max(cost - 200000, 0), 0)
  - ca_basis: cost - ca_179
  - ca_depreciation: round(ca_basis * ca_rate, 0)
  - addition: federal_deduction - ca_179 - ca_depreciation
expected:
  ca_179: 15000
  ca_basis: 195000
  ca_depreciation: 27866
  addition: 167134
```

The 14.29% first-year rate is an assumption for the example (federal MACRS 7-year table); California follows MACRS for individuals but confirm the method on form FTB 3885A for the asset.

### Case 2: itemize for California while taking the federal standard deduction (decision)

A single client took the federal standard deduction. Her potential itemized amounts are: state income tax $4,000, SDI withheld $520, property tax $5,000, mortgage interest $8,000 (loan of $900,000, so federal would have limited it and California does not). For California, state income tax and SDI are not deductible, so California itemized deductions are $13,000. The California standard deduction (2025 amount, pending the 2026 figure) is $5,706. Itemizing for California is larger by $7,294; at the 9.3% bracket that is about $678 of tax. She itemizes for California only and attaches a federal Schedule A completed for California.

```oa-check
name: CA itemize or standard deduction decision (2026, 2025 standard deduction)
inputs:
  state_income_tax: 4000
  sdi: 520
  property_tax: 5000
  mortgage_interest: 8000
  ca_standard: 5706
  marginal_rate: 0.093
steps:
  - ca_itemized: property_tax + mortgage_interest
  - deduction: max(ca_itemized, ca_standard)
  - extra: deduction - ca_standard
  - tax_saved: round(extra * marginal_rate, 2)
expected:
  ca_itemized: 13000
  deduction: 13000
  extra: 7294
  tax_saved: 678.34
```

## When to refuse or refer

- Refer if the client was not a California resident all year, or a spouse was a nonresident on a joint return (Form 540NR).
- Refer RDP returns that need the RDP adjustments worksheet (FTB Pub. 737), and community-property splits.
- Refer business gross receipts of $1,000,000 or more with preference items (full Schedule P AMT), and any NOL use when income is $1,000,000 or more (suspension, form FTB 3805V).
- Refer assets with no California depreciation history, research costs under the 2015 version of section 174, and any excess business loss.
- Do not state a 2026 standard deduction, exemption credit or credit income limit as final until the FTB publishes it; give the labelled 2025 amount.
- Refer if California enacts further conformity legislation for 2026 after 2026-11-13; recheck R&TC 17024.5 and the FTB conformity page first.

## Filing and payment

| Step | When and where | Source |
| --- | --- | --- |
| File Form 540 for 2026 | April 15, 2027; e-file through CalFile or software at ftb.ca.gov, or mail | [2025 Form 540 booklet](https://www.ftb.ca.gov/forms/2025/2025-540-booklet.pdf) |
| Automatic extension to file | Six months, no form needed: October 15, 2027. Not an extension to pay | [FTB extension to file](https://www.ftb.ca.gov/file/when-to-file/extension-to-file.html) |
| Pay any balance | April 15, 2027; extension payments on form FTB 3519 or Web Pay | same |
| Mandatory e-pay | After any estimate or extension payment over $20,000, or a return with total tax over $80,000, every later payment must be electronic; otherwise a 1% penalty | [2026 Form 540-ES instructions](https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.pdf) |
| Late payment penalty | 5% of the unpaid tax plus 0.5% for each month or part of a month unpaid; reasonable cause is presumed if 90% of the tax is paid by the original due date | [2025 Form 540 booklet](https://www.ftb.ca.gov/forms/2025/2025-540-booklet.pdf) |
| Late filing penalty | Filed after the extended date: up to 25% of the unpaid tax; more than 60 days late, a minimum of $135 or the balance due if less | same |
| Interest | Compounds daily, rate set twice a year, cannot be waived | same |
| 2027 estimated tax | 30% April 15, 40% June 15, nothing in September, 30% January 15 | `ca-estimated-tax-540es` |

**2025 returns still open.** A 2025 return was due April 15, 2026; the automatic extension ran to October 15, 2026, with payment due April 15, 2026. Use the 2025 amounts in `ca-income-tax` and the 2025 tax rate schedules.

## Completion checklist

- [ ] Resident all year; filing status matches federal, or the exception is documented.
- [ ] Form 540 line 13 equals federal AGI.
- [ ] Schedule CA column B and column C entries tie to support (FTB 3885A, HSA, Social Security, lottery).
- [ ] No QBI or Schedule 1-A deduction carried into California.
- [ ] California section 179 recomputed with the $200,000 phase-out and the business-income cap; no bonus depreciation; California asset records updated.
- [ ] Itemized deductions: SDI and state income tax removed, mortgage and home equity limits applied, high-income limitation checked.
- [ ] Tax from the table or the 2026 schedules; exemption credits reduced if federal AGI is over the limit.
- [ ] Behavioral Health Services Tax checked over $1,000,000; AMT gross receipts test documented.
- [ ] Renter's credit, CalEITC, YCTC and FYTC tested on their conditions.
- [ ] Use tax line 91 completed; line 92 coverage box or penalty supported.
- [ ] Payments and the estimated tax penalty reconciled; 2027 installments scheduled.
- [ ] Every 2025 amount used for 2026 flagged for replacement.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 2025 Form 540. Read for the line map (lines 13 to 19, 31, 32, 46 to 48, 61 to 64, 71 to 78, 91 to 115). | https://www.ftb.ca.gov/forms/2025/2025-540.pdf | 2026-11-13 |
| 2025 California 540 Personal Income Tax Booklet. Read for line 18, line 32, the AMT gross receipts test, the late filing and late payment penalties, interest and the important dates. | https://www.ftb.ca.gov/forms/2025/2025-540-booklet.pdf | 2026-11-13 |
| 2025 Schedule CA (540) instructions. Read for the IRC date, the OBBBA statement, lines 1h, 5a, 5e, 6, 8, 8b, 8f, 11, 12, 13, 14 and 19 to 22, and alimony. | https://www.ftb.ca.gov/forms/2025/2025-540-ca-instructions.html | 2026-11-13 |
| 2025 Schedule P (540) instructions. Read for the NOL suspension and the business credit limit. | https://www.ftb.ca.gov/forms/2025/2025-540-p-instructions.html | 2026-11-13 |
| 2025 FTB 3885A instructions. Read for the California section 179 worksheet. | https://www.ftb.ca.gov/forms/2025/2025-3885a-instructions.html | 2026-11-13 |
| FTB Pub. 1001 (2025). Read for bonus depreciation, sections 174 and 174A, and the excess business loss. | https://www.ftb.ca.gov/forms/2025/2025-1001-publication.pdf | 2026-11-13 |
| 2026 California Tax Rate Schedules. Read for the $100,000 tax-table rule. | https://www.ftb.ca.gov/forms/2026/2026-540-tax-rate-schedules.pdf | 2026-11-13 |
| 2026 Instructions for Form 540-ES. Read for mandatory electronic payments. | https://www.ftb.ca.gov/forms/2026/2026-540-es-instructions.pdf | 2026-11-13 |
| FTB extension to file. Read for the automatic six-month extension and payment date. | https://www.ftb.ca.gov/file/when-to-file/extension-to-file.html | 2026-11-13 |
| R&TC 17043 (through Firecrawl). Read for the 1% tax over $1,000,000. | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17043 | 2026-11-13 |
| R&TC 17024.5 (through Firecrawl). Read for the January 1, 2025 specified date. | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17024.5 | 2026-11-13 |

Not yet confirmed: the 2026 Form 540 booklet and 2026 Schedule CA (540) instructions were not published on 2026-11-13, so line numbers are from the 2025 Form 540 and may move; the 2026 indexed amounts (see `ca-income-tax`); California's response to the 2026 federal Schedule A changes; the general California limit on cash charitable gifts (v1 stated 50% of federal AGI; the 2025 Schedule CA text read here confirmed only the 30% conservation easement limit, so the 50% figure is removed); the 14.29% first-year rate in Case 1 is an illustrative assumption, not an FTB figure.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ca-540-individual-return` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ca-540-individual-return. If neither is available, confirm every figure against the official source pages cited above before relying on it.
