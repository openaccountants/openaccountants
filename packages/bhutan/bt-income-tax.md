---
name: bt-income-tax
description: "Compute 2026 individual income tax, residence, employment and education reliefs, final withholding and annual filing in Bhutan."
jurisdiction: BT
tax_year: 2026
last_updated: 2026-11-16
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
version: "2.2"
type: situation-rules
---

# Bhutan Personal Income Tax (2026) | v2.2

For 2026, classify the income and residence first, separate exempt and final-withholding amounts, then apply the progressive bands to ordinary taxable income. The new Act applies from 1 January 2026; it does not rewrite an earlier income year. [ss.2-5](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.16-20](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [Schedule 1 paragraph 1](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

## Who this applies to

An individual is resident if domiciled in Bhutan, unless a permanent home is outside Bhutan throughout the year and no permanent home is in Bhutan; or present in Bhutan during the income year, with that presence falling within periods aggregating at least 183 days in any 12-month period commencing or ending in the year; or a Bhutan Government employee or official posted abroad. A part-day counts. The normal whole-year rule has an exception for residence arising only through the day test, which starts at the beginning of the relevant period. [ss.226-232](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

Resident business income is assessed irrespective of source. Employment, investment and other income, and a non-resident’s business income, are confined to Bhutan sources under ss.19-20. Citizenship alone is not the residence test. Use [the business skill](bt-corporate-income-tax.md) for individual business and presumptive treatment. [ss.16-20](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

## Rates, bands and thresholds

| Item | Rule for 2026 | Official source |
|---|---|---|
| Taxable income up to Nu.300,000 | Nil tax; 0% is derived from “Nil”. | [Schedule 1 paragraph 1](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf) |
| Over Nu.300,000 to Nu.500,000 | 5% of the excess over Nu.300,000. | [Schedule 1 paragraph 1](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf) |
| Over Nu.500,000 to Nu.750,000 | Nu.10,000 plus 10% of the excess over Nu.500,000. | [Schedule 1 paragraph 1](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf) |
| Over Nu.750,000 to Nu.1,200,000 | Nu.35,000 plus 15% of the excess over Nu.750,000. | [Schedule 1 paragraph 1](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf) |
| Over Nu.1,200,000 to Nu.2,000,000 | Nu.102,500 plus 20% of the excess over Nu.1,200,000. | [Schedule 1 paragraph 1](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf) |
| Over Nu.2,000,000 to Nu.3,500,000 | Nu.262,500 plus 25% of the excess over Nu.2,000,000. | [Schedule 1 paragraph 1](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf) |
| Over Nu.3,500,000 | Nu.637,500 plus 30% of the excess over Nu.3,500,000. | [Schedule 1 paragraph 1](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf) |
| Resident employment deduction | Lower of 15% of total employment income and Nu.150,000 (15% is in words on the page). This is the annual deduction; do not separately deduct employee PF/GIS under the former regime. | [ss.21-24, 44](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf) |
| Resident education relief | Qualifying documented expenses: lower of actual expenses and Nu.350,000. Without clear documentary evidence: Nu.50,000. Apply the child/own-education and course conditions below; do not invent a separate Nu.350,000 allowance for every child. | [Schedule 6 paragraphs 1,10-12](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [rr.47-54](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf) |
| First primary home | Resident Bhutan citizen: lower of qualifying interest actually paid and Nu.200,000; loan must fund acquisition, construction or major renovation of the first home used as the primary residence. | [Schedule 6 paragraphs 2-3](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [rr.55-58](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf) |
| Taxable individual investment interest/dividends | 10% withholding (in words on the page), subject to the exemption and payer exceptions below; final for investment income. Business-connected interest/dividends have a different finality rule. | [ss.266-284;Schedule 1 paragraph 7](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [rr.154-164](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf) |

## The base

Keep employment, business, investment and other income separate. Employment includes cash salary, bonuses, allowances and taxable benefits; test the specific exclusions in s.24 before deduction. Rent and royalties belong to investment unless effectively connected with a business. Resident cultivation and direct sale of cash crops qualify for the Schedule 3 exemption, but post-harvest storage/transport services and intermediaries or resellers do not inherit it. [ss.16-20](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.21-24, 44](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.27(8), 29-32](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [Schedule 3 paragraphs 5,7-9,12,14](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

For a non-business individual, Schedule 3 exempts fixed-deposit interest up to Nu.400,000 and dividends up to Nu.300,000 in the income year. Government-bond interest and the specified incremental-deposit or withdrawal-at-will accounts have their own exemptions. Do not treat all interest as progressive income or mechanically charge withholding on an exempt amount: s.268(4) excludes exempt payments. Rule 158(10)’s interest/dividend wording must be read with that statutory exemption; do not infer a tax charge from the exception to a regulatory no-withholding list. [Schedule 3 paragraphs 5,7-9,12,14](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.266-284;Schedule 1 paragraph 7](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [rr.154-164](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf)

Education relief covers the resident’s own or biological/legally adopted dependent child’s qualifying education. Rule 47 limits costs to tuition, examinations, boarding/accommodation and fees paid to licensed daycare or Early Childhood Care and Development (ECCD) centres. Study other than daycare/ECCD must last at least 6 months (in words on the page) and lead to formal certification. A dependent child’s tertiary/professional programme must be recognized by the competent authority and lead to the first degree, diploma or initial professional/vocational licence or qualification; later postgraduate, advanced or continuing-professional courses are excluded. Only 1 parent may claim for a particular child in an income year (in words on the page). For a child under 18 who must file, a biological/adoptive parent required to file claims the expenses; the child may claim self-education only if no such parent must file by virtue of s.293. Claim only costs not covered by scholarships or other assistance, in the payment year, including advance payments. Retain receipts and proof that the claimant parent paid foreign-study costs. [Schedule 6 paragraphs 1,10-12](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [rr.47-54](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf)

For homeownership relief, retain ownership, qualifying-loan and interest-payment records. The residence must be lawfully owned, the main habitual home, and not primarily income-producing; only one primary residence is allowed at a time. Joint owners apply the limit to their own qualifying interest paid. This is not an automatic deduction of a personal home loan against rental income. Total Schedule 6 relief cannot exceed total assessable income and unused relief is not carried forward or back. [Schedule 6 paragraphs 2-3](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [rr.55-58](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf); [Schedule 6 paragraphs 1,10-12](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

Historical boundary: the former Act’s surcharge depended on the annual PIT amount, not gross income. Its PartIII s.14 A specified 10% where annual PIT was at least Nu.1,000,000 (10% is in words on the page). This is a historical provision, not an additional charge in the new Schedule 1 table. Earlier education, employee PF/GIS and rental-loan claims require their own year’s evidence; do not carry them forward merely because the old skill listed them. [PartIII 14 A](https://www.drc.gov.bt/wp-content/uploads/2024/11/Income-Tax-Act-of-the-Kingdom-of-Bhutan-2001_Fourth-Edition.pdf); [Schedule 1 paragraph 1](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

## Deadlines and filing

For ordinary 2026 annual income, the statutory return deadline is the last day of April following the income year, with assessment tax payable on that date: 30 April 2027 is derived for a calendar-year 2026 return. A resident individual with no business income and total income not exceeding Nu.300,000 is exempt from filing under s.293, subject to a DRC requirement to file or an election to file; the non-resident exception requires only final-withholding payments and no ordinary tax liability. [ss.263, 290-295](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

The 2025-2026 filing cycle is different: DRC’s 29 December 2025 notice set the 2025 PIT window at 1 January to 28 February 2026, and BIT/CIT/EO at 1 January to 31 March 2026. The old skill’s March deadline for PIT was wrong. Those dates do not govern income year 2026. [paragraphs 1-2](https://www.drc.gov.bt/wp-content/uploads/2025/12/Tax-Filing-Notification_IY-2025_final.pdf)

Prepare identity and TPN, residence evidence, all income-head schedules, relief receipts and withholding/prepayment records. In AnnexureIV ITR 1, PartA identifies the filer and residence; PartB combines employment ScheduleA, business ScheduleB, investment ScheduleC and other ScheduleD, then reliefs and taxes paid. Recompute statutory tax independently: the printed PartB net-tax formula is not a reliable substitute for liability minus allowable credits. Keep final-withholding income outside the ordinary computation and do not credit the same tax twice. [AnnexureIV,individualPartB/companyPartsB-C](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf); [ss.16-20](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [ss.266-284;Schedule 1 paragraph 7](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

As read on 15 November 2026, DRC announces the income module of BITS from 1 January 2027, replacing RAMIS. Existing RAMIS TPNs continue through the transition or further notice; new numbers are being communicated. The announced early-December new-TPN application route is future, not a live November filing instruction. Use the notice and preserve registration, submission and payment acknowledgements; the 2027 live form fields and final payment-reference screen remain unconfirmed. [both image pages](https://www.drc.gov.bt/transition-to-the-bhutan-integrated-taxation-system-income-tax-module/)

## Penalties and interest

Late filing under s.664 is Nu.100 per day for a person other than a company, subject to any permitted filing extension; a s.600 notice does not create a second penalty for the same filing failure. Late payment under ss.442-450 attracts 15% per annum simple interest (in words on the page) from the due date to payment, capped at the underlying tax liability. A filing extension does not itself erase payment interest. [ss.442-450, 664-666](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

## Cross-border points

Establish source, residence, payer and whether a Bhutan permanent establishment or significant economic presence is involved before treating a non-resident payment as final. Section 280 excludes PE, significant-economic-presence and Bhutan-asset payments from the normal non-resident finality rule. If tax was not withheld from a final payment, s.282 can require prepayment and assessment. No treaty rate is certified here. [ss.266-284;Schedule 1 paragraph 7](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

## Two worked examples that recompute

A resident has only taxable employment of Nu.600,000, with no exclusions, other reliefs or credits. The annual deduction is Nu.90,000, taxable income Nu.510,000 and tax Nu.11,000, all derived. [ss.21-24, 44](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [Schedule 1 paragraph 1](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

```oa-check
name: Resident employment annual computation
inputs:
  employment: 600000
steps:
  deduction: min(employment * 0.15, 150000)
  taxable: employment - deduction
  tax: 10000 + (taxable - 500000) * 0.10
expected:
  deduction: 90000
  taxable: 510000
  tax: 11000
```

A resident’s Nu.1,200,000 employment income gives the capped Nu.150,000 deduction. Qualifying documented education expenses of Nu.400,000 support Nu.350,000 relief, leaving taxable income Nu.700,000 and tax Nu.30,000. With no clear documentary evidence, the statutory education branch allows Nu.50,000, leaving Nu.1,000,000 and tax Nu.72,500. The Nu.42,500 difference is derived; the course and parent conditions are assumed met in both branches. This comparison does not authorize an undocumented actual-cost claim. [ss.21-24, 44](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [Schedule 6 paragraphs 1,10-12](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf); [rr.47-54](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf); [Schedule 1 paragraph 1](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf)

```oa-check
name: Education evidence changes annual tax
inputs:
  employment: 1200000
  education_paid: 400000
steps:
  employment_deduction: min(employment * 0.15, 150000)
  documented_relief: min(education_paid, 350000)
  documented_taxable: employment - employment_deduction - documented_relief
  documented_tax: 10000 + (documented_taxable - 500000) * 0.10
  no_documents_taxable: employment - employment_deduction - 50000
  no_documents_tax: 35000 + (no_documents_taxable - 750000) * 0.15
  difference: no_documents_tax - documented_tax
expected:
  documented_taxable: 700000
  documented_tax: 30000
  no_documents_taxable: 1000000
  no_documents_tax: 72500
  difference: 42500
```

## Ask the client first

- Which income year and approved accounting period?
- Domicile, permanent homes, travel days and any Government posting?
- Every income source, payer, business connection and final-withholding certificate?
- Education course, dependent/parent claimant, receipts, scholarships and payment year?
- Citizenship, ownership, first-home use and interest actually paid?
- TPN, prior filings, tax paid and any DRC notice?

## Sources

| Source | Read for | Read date |
|---|---|---|
| [Income Tax Act of Bhutan 2025](https://www.drc.gov.bt/wp-content/uploads/2025/09/Income-Tax-Act-of-Bhutan-2025.pdf) | Read for ss.1-64, 204-207, 226-240, 262-300, 324-326, 442-450, 664-674, 706(40); Schedules 1-3 and 6. | 2026-11-15 |
| [Rules on the Income Tax Act 2025](https://www.drc.gov.bt/wp-content/uploads/2026/01/Rules-on-the-Income-Tax-Act-of-Bhutan-2025.pdf) | Read for rr.47-58, 151-164; Annexures I-II and IV, relevant individual and company computation fields. | 2026-11-15 |
| [Historical Income Tax Act 2001, Fourth Edition](https://www.drc.gov.bt/wp-content/uploads/2024/11/Income-Tax-Act-of-the-Kingdom-of-Bhutan-2001_Fourth-Edition.pdf) | Read for Part I s.45; Part II s.12; Part III ss.4-5, 7, 12, 14 A-15,17; historical provisions only. | 2026-11-15 |
| [DRC income-year 2025 filing notice,29 December 2025](https://www.drc.gov.bt/wp-content/uploads/2025/12/Tax-Filing-Notification_IY-2025_final.pdf) | Read for both pages: filing windows, inactive entities, RAMIS/BETA, completion status and payment voucher. | 2026-11-15 |
| [DRC income-module transition notice,10 November 2026](https://www.drc.gov.bt/transition-to-the-bhutan-integrated-taxation-system-income-tax-module/) | Read for both image pages: January transition, TPN notices and December application timing. | 2026-11-15 |

Not yet confirmed: the old skill’s seven-band table as a statement of 2025 law; historical employee PF/GIS limits and rental-loan conditions; any per-child multiplication of the education cap; treaty-specific relief; the final 2027 live BITS return/payment fields. None is certified by this 2026 computation.
