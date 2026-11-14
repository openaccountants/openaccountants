---
name: id-income-tax
description: Idaho individual income tax for residents, including self-employed taxpayers, Form 40 computation and filing. Covers the verified 2025-2026 filing cycle and identifies missing annual 2026 figures rather than projecting them from payroll tables. Routes part-year and nonresident returns separately.
version: 1.0
jurisdiction: US-ID
category: state-tax
type: situation-rules
tax_year: 2026
tax_year_notes: "2025-2026 filing cycle; final annual 2026 schedule not confirmed"
tier: 2
last_updated: 2026-11-13
---

# Idaho individual income tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick reference:** this is the **2025-2026 filing cycle**, for annual tax year 2025 filed in 2026. The Commission's annual schedule still identifies 2025. The indexed annual 2026 bands and final forms have not been confirmed. The 2026 employer withholding table in `id-payroll` is a different computation. Built from the law; Not yet approved.

## Who this applies to

Full-year Idaho residents use Form 40, including sole traders carrying federal business results into their personal return. Idaho taxes residents' worldwide income. Domicile, or keeping an Idaho home all year and spending more than 270 days there, can establish residency. Part-year residents and nonresidents use Form 43; this skill routes them without supplying its allocation calculation. See [individual income basics](https://tax.idaho.gov/taxes/income-tax/individual-income/online-guide/).

## Rates, bands and thresholds

| Item | Verified period and condition | Official source |
|---|---|---|
| Ordinary tax rate | 5.3% for tax year 2025, applied to taxable income above the status-specific zero-rate amount | [Annual rate schedule](https://tax.idaho.gov/taxes/income-tax/individual-income/individual-income-tax-rate-schedule/) |
| Single / married filing separately | 2025 zero-rate amount $4,811; use the excess, not gross income | [Form 40 instructions, line 20 worksheet](https://tax.idaho.gov/wp-content/uploads/forms/EFO00089/EFO00089_03-02-2026.pdf) |
| Joint / head of household / qualifying surviving spouse | 2025 zero-rate amount $9,622 | [Form 40 instructions, line 20 worksheet](https://tax.idaho.gov/wp-content/uploads/forms/EFO00089/EFO00089_03-02-2026.pdf) |
| Part-year filing test | More than $2,500 combined gross income from all sources while resident and Idaho sources while nonresident | [Commission residency and filing tests](https://tax.idaho.gov/taxes/income-tax/individual-income/online-guide/) |
| Nonresident filing test | More than $2,500 gross Idaho-source income | [Commission residency and filing tests](https://tax.idaho.gov/taxes/income-tax/individual-income/online-guide/) |
| 2025 annual return and payment | April 15, 2026; this is not the deadline for a 2026 annual return | [Filing and paying](https://tax.idaho.gov/taxes/income-tax/individual-income/filing-and-paying/) |

## The base

Complete the federal computation first using the relevant federal owner skill, including `us-schedule-c-and-se-computation` for sole traders. Federal bands, deductions and contribution figures are not repeated here.

For the [2025 Form 40](https://tax.idaho.gov/wp-content/uploads/forms/EFO00089/EFO00089_03-02-2026.pdf), carry federal AGI to line 7; Form 39R additions/subtractions to lines 8/10. Lines 13-17 reconcile itemized or standard deductions. Line 18 combines the federal qualified-business-income and Schedule 1-A deductions; use the revised instructions even though the printed label is shorter. Line 19 is Idaho taxable income; the line 20 worksheet applies the rate and zero-rate amount. Credits, other taxes and payments follow; this is not a complete credit computation.

| Boundary | Treatment | Source |
|---|---|---|
| Full-year resident with another state's income | Worldwide income remains in scope; evaluate the other-state tax credit rather than excluding income automatically | [Individual basics](https://tax.idaho.gov/taxes/income-tax/individual-income/online-guide/) |
| Part-year resident / nonresident | Route to Form 43; do not apply the full-year computation to unallocated income | [Individual basics](https://tax.idaho.gov/taxes/income-tax/individual-income/online-guide/) |
| 2026 annual return | Stop before final tax calculation until the annual schedule, adjustments and forms are confirmed | [Published annual schedule identifies 2025](https://tax.idaho.gov/taxes/income-tax/individual-income/individual-income-tax-rate-schedule/) |

## Deadlines and filing

For the verified 2025-2026 filing cycle, use the [Commission's income filing process](https://tax.idaho.gov/taxes/income-tax/individual-income/filing-and-paying/): e-file through authorized tax software or submit the correct paper return. TAP **cannot file an income return**. It can accept payment; Quick Pay is another payment route. Retain the acceptance, full return, attachments and payment receipt separately. An extension to file does not extend payment; extension qualification is not computed here.

## Penalties and interest

Late payment can accrue interest despite a filing extension. Current penalty percentages, interest rate and extension-payment qualification have not been confirmed for this skill; do not calculate them from memory. The [Commission filing page](https://tax.idaho.gov/taxes/income-tax/individual-income/filing-and-paying/) distinguishes filing from payment extensions.

## Cross-border points

Establish domicile, dates and Idaho-source income before selecting Form 40 or Form 43. International treaty, foreign-tax-credit and expatriation work belongs with the relevant federal skill; Idaho conformity and state credits require separate analysis. This skill supplies no treaty exemption.

## Two worked examples that recompute

**Basic 2025 resident case.** Invented single taxpayer has $40,000 of already reconciled Form 40 line 19 taxable income. The pre-credit line 20 computation is ($40,000 - $4,811) x 5.3% = $1,865.017, rounded to $1,865. This is not the balance due after other taxes, credits and payments.

```oa-check
name: Idaho single pre-credit tax 2025-2026 filing cycle
inputs:
  taxable_income: 40000
steps:
  excess: max(0, taxable_income - 4811)
  pre_credit_tax: round(excess * 0.053, 0)
expected:
  pre_credit_tax: 1865
```

**Head-of-household boundary.** Invented qualifying head of household has $8,000 taxable income. The $9,622 amount produces zero pre-credit tax. Misclassifying the filer as single would produce $169.017, rounded $169. Determine the legal filing status; the taxpayer cannot choose a status solely for its result. Both cases use the [2025 line 20 worksheet](https://tax.idaho.gov/wp-content/uploads/forms/EFO00089/EFO00089_03-02-2026.pdf).

```oa-check
name: Idaho head-of-household zero-rate boundary 2025
inputs:
  taxable_income: 8000
steps:
  correct_tax: round(max(0, taxable_income - 9622) * 0.053, 0)
  wrong_single_tax: round(max(0, taxable_income - 4811) * 0.053, 0)
expected:
  correct_tax: 0
  wrong_single_tax: 169
```

## Ask the client first

- Which annual tax year, original/amended return and filing status apply?
- Where was the taxpayer domiciled, and where did they keep a home and spend their days?
- What federal return, business schedules and Idaho modifications support taxable income?
- What Idaho-source income arose while nonresident or part-year resident?
- What credits, other-state taxes, withholding and payments need reconciliation?

## Sources

| Source | URL | Read for | Read on |
|---|---|---|---|
| Commission individual basics; Code Title 63, Chapter 30 | https://tax.idaho.gov/taxes/income-tax/individual-income/online-guide/ | Read for residence, worldwide/source income and part-year/nonresident filing tests | 2026-11-13 |
| Commission annual schedule | https://tax.idaho.gov/taxes/income-tax/individual-income/individual-income-tax-rate-schedule/ | Read for the explicitly dated 2025 rate and bands; page does not establish annual 2026 indexed amounts | 2026-11-13 |
| Form 40 and revised instructions, 2025 | https://tax.idaho.gov/wp-content/uploads/forms/EFO00089/EFO00089_03-02-2026.pdf | Read for form lines 7-20, Schedule 1-A treatment and status-specific line 20 worksheet | 2026-11-13 |
| Commission filing and paying | https://tax.idaho.gov/taxes/income-tax/individual-income/filing-and-paying/ | Read for the 2025 return deadline, software/paper filing, TAP limitation and payment extension distinction | 2026-11-13 |

Not yet confirmed: final annual 2026 rate schedule, indexed zero-rate amounts, filing thresholds, deductions, adjustments, credits, forms and filing deadline; full Form 43 allocation; full Form 39R modifications and credits, food-credit computation, estimated payments, extension qualification and penalty/interest schedules. Direct access to the legislature's current income-tax section was blocked; the dated Commission figures above remain labelled 2025-2026 filing cycle.
