---
name: ma-income-tax
description: Compute Massachusetts resident personal income tax for 2026 on Form 1, for employees, sole proprietors and single-member LLC owners. Covers the Part A, Part B and Part C income classes, the 5% rate, 8.5% on short-term capital gains, 12% on long-term collectible gains, the personal exemptions, the rent and FICA deductions, and the 4% surtax on taxable income over the 2026 threshold of $1,107,750. Trigger on "Massachusetts income tax", "MA income tax", "Form 1", "Mass DOR", "M.G.L. c. 62", "millionaires tax", "Fair Share surtax", "MA surtax". Load us-tax-workflow-base first. Massachusetts only, federal figures are in the federal skills.
version: "1.0"
jurisdiction: US-MA
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Massachusetts personal income tax, tax year 2026

> **Source-cited draft.** Built from the Massachusetts Department of Revenue (DOR) pages on tax rates, the 4% surtax, personal exemptions, the rent deduction and who must file, the 2026 Form 1-ES, the January 2026 Circular M, the DOR pass-through entity excise page and M.G.L. c. 62, sections 3 and 4, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026, Massachusetts taxes Part B income (wages, business income, rents, pensions) and Part A interest and dividends at **5%**, Part A short-term capital gains at **8.5%**, Part C long-term capital gains at **5%**, and long-term gains on collectibles at **12%** (with a 50% deduction). On top, a **4% surtax** applies to the part of total taxable income (Part A plus Part B plus Part C, any negative part counted as zero) above **$1,107,750**. The threshold is the same for a single filer and a married couple filing jointly. There is no standard deduction: a single filer gets a **$4,400** personal exemption, a married couple filing jointly **$8,800**, a head of household **$6,800**, plus **$1,000** per dependent. Massachusetts has no local income tax.

## Scope

| Field | Value |
| --- | --- |
| Jurisdiction | Massachusetts (US-MA) |
| Tax authority | [Massachusetts Department of Revenue](https://www.mass.gov/orgs/massachusetts-department-of-revenue) |
| Portal | [MassTaxConnect](https://mtc.dor.state.ma.us/mtc/_/) |
| Law | [M.G.L. c. 62](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter62/Section4) (taxation of incomes), c. 62B (withholding and estimates), c. 62C (administration) |
| Main form | Form 1 (resident return); [Form 1-ES](https://www.mass.gov/doc/2026-form-1-es-estimated-tax-payment-vouchers-instructions-and-worksheets/download) (estimates) |

Covers full-year residents filing Form 1: wage earners, sole proprietors and owners of single-member LLCs disregarded for federal tax whose Schedule C profit lands in Part B. Covers the 4% surtax for every chapter 62 taxpayer, and the credit a member claims for a pass-through entity excise paid on their behalf.

Not covered: nonresident and part-year returns on Form 1-NR/PY beyond the surtax point below; trusts and estates (Form 2); the entity side of the pass-through entity excise (see `ma-corporate-excise`); employer withholding (see `us-ma-payroll`); estate tax. Federal income tax, self-employment tax and FICA are in the federal skills (`us-schedule-c-and-se-computation`, `us-form-1040-individual-return`); Massachusetts figures only are stated here.

## Ask the client first

1. Residency for the whole of 2026: home in Massachusetts all year, or a Massachusetts home kept and more than 183 days spent in the state? If neither, this is a Form 1-NR/PY case.
2. Federal filing status. A couple filing jointly federally must file jointly in Massachusetts.
3. The income split: wages and business profit (Part B), interest and dividends (Part A), short-term gains (Part A), long-term gains (Part C), long-term gains on collectibles.
4. Rent paid on a Massachusetts principal residence, dependents, age 65 or blindness at 31 December 2026.
5. Whether total taxable income may pass $1,107,750 (surtax, electronic filing, estimate planning), and whether a pass-through entity the client owns elected the chapter 63D or 63E excise.
6. Health coverage for each month of 2026 (Schedule HC).

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure | Condition | Source |
| --- | --- | --- | --- |
| Part B income: wages, business, rents, pensions and other income | 5.00% | All Part B taxable income | [DOR tax rates](https://www.mass.gov/info-details/massachusetts-tax-rates) |
| Part A interest and dividends | 5.00% | Interest and dividends other than Massachusetts bank interest | [DOR tax rates](https://www.mass.gov/info-details/massachusetts-tax-rates) |
| Part A short-term capital gains | 8.5% | Capital assets held 1 year or less | [DOR tax rates](https://www.mass.gov/info-details/massachusetts-tax-rates); [M.G.L. c. 62, s. 4](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter62/Section4) |
| Long-term gains on collectibles | 12.00%, subject to a 50% deduction | Collectibles held more than 1 year | [DOR tax rates](https://www.mass.gov/info-details/massachusetts-tax-rates) |
| Part C long-term capital gains | 5.00% | Capital assets held more than 1 year, other than collectibles | [DOR tax rates](https://www.mass.gov/info-details/massachusetts-tax-rates) |
| 4% surtax threshold | $1,107,750 | Tax year 2026; one threshold per return, joint returns included | [DOR 4% surtax](https://www.mass.gov/info-details/4-surtax-on-taxable-income-over-1000000) |
| 4% surtax threshold, earlier years | $1,083,150 (2025); $1,053,750 (2024); $1,000,000 (2023) | For amended or late returns only | [DOR 4% surtax](https://www.mass.gov/info-details/4-surtax-on-taxable-income-over-1000000) |
| Personal exemption, single or married filing separately | $4,400 | Allowed whether or not a federal exemption is allowed | [DOR personal exemptions](https://www.mass.gov/info-details/massachusetts-personal-income-tax-exemptions) |
| Personal exemption, head of household | $6,800 | Head of household status | [DOR personal exemptions](https://www.mass.gov/info-details/massachusetts-personal-income-tax-exemptions) |
| Personal exemption, married filing jointly | $8,800 | Joint return | [DOR personal exemptions](https://www.mass.gov/info-details/massachusetts-personal-income-tax-exemptions) |
| Dependent exemption | $1,000 each | Qualifying child or qualifying relative, not you or your spouse | [DOR personal exemptions](https://www.mass.gov/info-details/massachusetts-personal-income-tax-exemptions) |
| Age 65 or over exemption | $700 each | Age 65 on or before 31 December 2026; each spouse on a joint return | [DOR personal exemptions](https://www.mass.gov/info-details/massachusetts-personal-income-tax-exemptions) |
| Blindness exemption | $2,200 each | Legally blind at the end of the year | [DOR personal exemptions](https://www.mass.gov/info-details/massachusetts-personal-income-tax-exemptions) |
| Rent deduction | 50% of rent paid, at most $4,000 ($2,000 per return if married filing separately) | Rent to a landlord for a Massachusetts principal residence | [DOR rent deduction](https://www.mass.gov/info-details/deductions-on-rent-paid-in-massachusetts) |
| Deduction for Social Security (FICA), Medicare and public retirement contributions | At most $2,000 a year | Amounts withheld for FICA, Medicare, Massachusetts, US or Railroad Retirement systems | [M.G.L. c. 62, s. 3](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter62/Section3); [Circular M 2026](https://www.mass.gov/doc/massachusetts-circular-m-income-tax-withholding-tables-at-50-effective-january-1-2026/download) |
| Filing threshold | Massachusetts gross income of more than $8,000 | Full-year and part-year residents | [DOR who must file](https://www.mass.gov/info-details/who-must-file-a-massachusetts-personal-income-tax-return) |
| Estimated tax trigger | More than $400 of tax on income not subject to withholding | Form 1-ES, 2026 | [2026 Form 1-ES](https://www.mass.gov/doc/2026-form-1-es-estimated-tax-payment-vouchers-instructions-and-worksheets/download) |
| Extension payment | 80% of the tax due, surtax included, by the original due date | For a valid automatic extension | [DOR 4% surtax](https://www.mass.gov/info-details/4-surtax-on-taxable-income-over-1000000) |
| Pass-through entity excise credit | 90% of the member's share of chapter 63D or 63E excise actually paid | Qualified member of an electing entity | [DOR elective PTE excise](https://www.mass.gov/info-details/elective-pass-through-entity-excise) |

### Step 1. Classify each item of income

| Class | What goes in it |
| --- | --- |
| Part A | Short-term capital gains, long-term gains on collectibles, interest and dividends other than Massachusetts bank interest |
| Part B | Everything not in Part A or Part C: wages, Schedule C profit, rents, pensions, Massachusetts bank interest |
| Part C | Long-term capital gains other than collectibles |

Typical bank-feed and document patterns: freelance or 1099-NEC income and Schedule E rents go to Part B; brokerage short-term gains to Part A at 8.5%; brokerage long-term gains to Part C at 5%; interest and dividends to Part A at 5%; pensions to Part B; Social Security is not taxed.

Schedule C profit of a sole proprietor or disregarded single-member LLC is Part B income; Massachusetts follows the federal home office and self-employed health insurance and retirement treatment as Part B items. Interest on US obligations is not taxed. Interest on another state's bonds is taxed; interest on Massachusetts bonds is not. Massachusetts does not use the federal qualified business income deduction.

### Step 2. Compute Part B taxable income

Part B income, less Part B deductions (the FICA and retirement deduction up to $2,000, the rent deduction, the self-employed health insurance and retirement deductions as allowed), less exemptions (personal, dependent, age, blindness, adoption fees). Part B losses may offset business-related capital gains only as chapter 62 allows; otherwise one part does not reduce another.

### Step 3. Compute Part A and Part C taxable income

Part A: interest and dividends at 5%, short-term gains at 8.5%, long-term collectible gains at 12% after the 50% deduction. Part C: long-term gains at 5%.

### Step 4. Add the 4% surtax

Add Part A, Part B and Part C taxable income, treating any negative part as zero. Subtract $1,107,750. Multiply the excess by 4%. Nonresidents and part-year residents measure the same way on their Massachusetts-source taxable income on Form 1-NR/PY.

### Step 5. Credits and payments

Subtract credits: credit for taxes paid to other jurisdictions (the surtax raises the Massachusetts tax on doubly taxed income, but the surtax may not simply be added to that income), the 90% credit for chapter 63D or 63E excise paid by an electing entity, and the refundable credits. Then subtract withholding and Form 1-ES payments.

### How the result flows on

Total tax is entered on Form 1 with the surtax shown separately. Taxpayers subject to the surtax must file and pay electronically. Health coverage is reported on Schedule HC: Massachusetts has its own individual coverage mandate, separate from the federal rules, and self-employed people buying their own cover should check it.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Married couple filing jointly federally | Must file jointly in Massachusetts from 2024, with no exception for surtax payers, even with different residency | [DOR 4% surtax](https://www.mass.gov/info-details/4-surtax-on-taxable-income-over-1000000) |
| Joint return over the threshold | One $1,107,750 threshold for the couple, not two | [DOR 4% surtax](https://www.mass.gov/info-details/4-surtax-on-taxable-income-over-1000000) |
| A part with a loss | Counted as zero when adding the parts for the surtax | [DOR 4% surtax](https://www.mass.gov/info-details/4-surtax-on-taxable-income-over-1000000) |
| Bonus or other supplemental wages above the threshold | Employer withholds 9% on the part above the threshold (see `us-ma-payroll`) | [DOR 4% surtax](https://www.mass.gov/info-details/4-surtax-on-taxable-income-over-1000000) |
| Owner of an entity that elected the chapter 63E excise (2026 on) | Member claims 90% of their share of the 4% excise as a credit; must file a return to claim it | [DOR elective PTE excise](https://www.mass.gov/info-details/elective-pass-through-entity-excise) |
| Sole proprietor or single-member LLC wanting the PTE excise | Not eligible: not a pass-through entity | [DOR elective PTE excise](https://www.mass.gov/info-details/elective-pass-through-entity-excise) |
| Dependent who files their own return | Still a Massachusetts dependent if the dependency tests are met | [DOR personal exemptions](https://www.mass.gov/info-details/massachusetts-personal-income-tax-exemptions) |
| Gross income $8,000 or less | No return required, but file to claim refundable credits such as the earned income credit | [DOR who must file](https://www.mass.gov/info-details/who-must-file-a-massachusetts-personal-income-tax-return) |

### Defaults when a fact is missing

| Missing fact | Default | Why |
| --- | --- | --- |
| Holding period of a gain | Treat as short-term (8.5%, [DOR tax rates](https://www.mass.gov/info-details/massachusetts-tax-rates)) until shown otherwise | The higher rate, so no understatement |
| Rent receipts | No rent deduction | The deduction needs rent actually paid on a principal residence |
| FICA withheld | Use the Form W-2 boxes 4 and 6 total, capped at $2,000 ([M.G.L. c. 62, s. 3](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter62/Section3)) | The cap applies per taxpayer |
| Whether income tops the threshold | Run the surtax step anyway | The surtax also changes the extension and estimate rules |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| One large gain in 2026 | Can push taxable income over $1,107,750 ([DOR 4% surtax](https://www.mass.gov/info-details/4-surtax-on-taxable-income-over-1000000)); consider timing (worked case 2) |
| Gaps in health coverage | Schedule HC penalty, which needs a reviewer |
| Income from another state | Other jurisdiction credit worksheets apply; surtax interaction |
| Bonus near year end for a high earner | Withholding at 9% ([DOR 4% surtax](https://www.mass.gov/info-details/4-surtax-on-taxable-income-over-1000000)) may still leave the surtax underpaid |

## Worked cases

**Case 1, single filer over the surtax threshold.** A single Massachusetts resident has 2026 wages of USD 400,000 (FICA withheld well above USD 2,000), interest and dividends of USD 30,000, a short-term gain of USD 80,000 and a long-term stock gain of USD 900,000. No rent, no dependents. Part B taxable income is 400,000 less the USD 2,000 FICA deduction less the USD 4,400 exemption = USD 393,600. Total taxable income is USD 1,403,600, so USD 295,850 is above the threshold and the surtax is USD 11,834. The 5% tax on Part B, Part A interest and Part C is USD 66,180; the 8.5% tax on the short-term gain is USD 6,800. Total Massachusetts tax before credits is USD 84,814.

```oa-check
name: Single filer with gains over the 2026 surtax threshold
inputs:
  wages: 400000
  fica_deduction: 2000
  personal_exemption: 4400
  interest_dividends: 30000
  short_term_gain: 80000
  long_term_gain: 900000
  threshold: 1107750
steps:
  - part_b: wages - fica_deduction - personal_exemption
  - taxable_total: part_b + interest_dividends + short_term_gain + long_term_gain
  - surtax: max(taxable_total - threshold, 0) * 0.04
  - tax_at_5: (part_b + interest_dividends + long_term_gain) * 0.05
  - tax_at_8_5: short_term_gain * 0.085
  - total_tax: tax_at_5 + tax_at_8_5 + surtax
expected:
  part_b: 393600.00
  taxable_total: 1403600.00
  surtax: 11834.00
  tax_at_5: 66180.00
  tax_at_8_5: 6800.00
  total_tax: 84814.00
```

**Case 2, decision: realize the whole gain in 2026, or only up to the threshold?** Same person. Without the long-term gain, taxable income is USD 503,600. The room under the threshold is 1,107,750 less 503,600 = USD 604,150. Realizing the full USD 900,000 in 2026 costs USD 11,834 of surtax; realizing only USD 604,150 in 2026 costs none, and the remaining USD 295,850 is taxed in a later year at 5%, plus surtax only if that year's total also tops that year's threshold. The figure that decides it is the 4% on the excess, set against the market risk and federal cost of waiting.

```oa-check
name: Gain timing against the 2026 surtax threshold
inputs:
  other_taxable: 503600
  long_term_gain: 900000
  threshold: 1107750
steps:
  - room_under_threshold: threshold - other_taxable
  - surtax_all_in_2026: max(other_taxable + long_term_gain - threshold, 0) * 0.04
  - gain_realized_capped: min(long_term_gain, room_under_threshold)
  - surtax_capped: max(other_taxable + gain_realized_capped - threshold, 0) * 0.04
  - gain_deferred: long_term_gain - gain_realized_capped
expected:
  room_under_threshold: 604150.00
  surtax_all_in_2026: 11834.00
  gain_realized_capped: 604150.00
  surtax_capped: 0.00
  gain_deferred: 295850.00
```

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| REF-MA-01 | Nonresident or part-year resident | Refer: Form 1-NR/PY with source rules and exemption ratios |
| REF-MA-02 | Hard Part A, Part B, Part C classification (installment gains, trade or business capital losses) | Flag for reviewer |
| REF-MA-03 | Income near the surtax threshold with timing or entity planning | Flag for reviewer: surtax planning and chapter 63E election |
| REF-MA-04 | Complex credits (brownfields, life sciences, film) | Flag for reviewer |
| REF-MA-05 | Schedule HC penalty (gaps in health coverage) | Flag for reviewer |
| REF-MA-06 | Married couple with different residency status, filing jointly because of the 2024 rule | Refer: DOR joint-filing guidance for that case |

## Filing and payment

- **Return:** Form 1, filed through MassTaxConnect or approved software. Anyone subject to the surtax must file and pay electronically.
- **Estimates (Form 1-ES):** required where more than $400 of tax is expected on income not subject to withholding. 2026 installments are due April 15, 2026; June 15, 2026; September 15, 2026; and January 15, 2027. Include the surtax in the estimate; underpayment is computed on Form M-2210, which also counts the surtax.
- **Extension:** automatic, provided 80% of the tax due, including the surtax, is paid by the original due date.
- **Withholding:** employers withhold under Circular M; see `us-ma-payroll`.

## Completion checklist

- [ ] Residency and federal filing status confirmed; joint federal means joint Massachusetts.
- [ ] Every income item placed in Part A, Part B or Part C, with holding periods.
- [ ] FICA deduction capped at $2,000; rent deduction at 50% and $4,000.
- [ ] Exemptions match filing status, dependents, age and blindness.
- [ ] Surtax computed on the sum of positive parts less $1,107,750.
- [ ] PTE excise credit at 90% of the member's share, where an entity elected.
- [ ] Estimates and extension payment include the surtax; electronic filing if surtax applies.
- [ ] Schedule HC completed.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR, Tax Rates (updated 30 Dec 2025). Read for 5.00%, 8.5%, 12.00% with 50% deduction, and the 2026 surtax threshold $1,107,750. | https://www.mass.gov/info-details/massachusetts-tax-rates | 2026-11-13 |
| DOR, Massachusetts 4% Surtax on Taxable Income (updated 1 Jun 2026). Read for thresholds 2023 to 2026, the Part A, B, C sum with negatives as zero, joint filing from 2024, 80% extension payment and the other jurisdiction credit. | https://www.mass.gov/info-details/4-surtax-on-taxable-income-over-1000000 | 2026-11-13 |
| DOR, Personal Income Tax Exemptions (updated 30 Oct 2026). Read for $4,400, $6,800, $8,800, $1,000, $700 and $2,200. | https://www.mass.gov/info-details/massachusetts-personal-income-tax-exemptions | 2026-11-13 |
| DOR, Deductions on Rent Paid in Massachusetts. Read for 50% of rent, $4,000 cap and $2,000 for married filing separately. | https://www.mass.gov/info-details/deductions-on-rent-paid-in-massachusetts | 2026-11-13 |
| DOR, Who Must File a Personal Income Tax Return. Read for the $8,000 gross income test and the 183-day residency test. | https://www.mass.gov/info-details/who-must-file-a-massachusetts-personal-income-tax-return | 2026-11-13 |
| DOR, Gross, adjusted gross and taxable income. Read for the Part A, Part B and Part C definitions. | https://www.mass.gov/info-details/gross-adjusted-gross-and-taxable-income | 2026-11-13 |
| DOR, 2026 Form 1-ES. Read for the $400 trigger, the 2026 installment dates and electronic filing for surtax payers. | https://www.mass.gov/doc/2026-form-1-es-estimated-tax-payment-vouchers-instructions-and-worksheets/download | 2026-11-13 |
| DOR, Circular M effective 1 January 2026. Read for the $2,000 FICA and retirement deduction and the $1,107,750 withholding threshold. | https://www.mass.gov/doc/massachusetts-circular-m-income-tax-withholding-tables-at-50-effective-january-1-2026/download | 2026-11-13 |
| DOR, Elective Pass-through Entity Excise (updated 31 Jul 2026). Read for the 90% member credit and the new chapter 63E excise from 2026. | https://www.mass.gov/info-details/elective-pass-through-entity-excise | 2026-11-13 |
| M.G.L. c. 62, s. 4. Read for the 8.5% short-term gain rate and the 4(d) surtax base. | https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter62/Section4 | 2026-11-13 |
| M.G.L. c. 62, s. 3. Read for the $2,000 cap on the retirement and FICA deduction. | https://malegislature.gov/Laws/GeneralLaws/PartI/TitleIX/Chapter62/Section3 | 2026-11-13 |

Not yet confirmed: the 2026 Form 1 and its instructions were not published when read, so no 2026 Form 1 line numbers are quoted and the 2026 Form 1 due date is taken as April 15, 2027 on the 2025-2026 filing cycle pattern; the Schedule HC 2026 penalty table was not read.
