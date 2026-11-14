---
name: in-corporate-tax
description: "Indiana corporate adjusted gross income tax in 2026, including the continuing 4.9% rate, federal-to-state base, IT-20 filing deadline, estimated payments and financial-institution franchise-tax boundary. Final annual forms, detailed apportionment and pass-through computations remain explicit gaps."
version: 1.0
jurisdiction: US-IN
category: state-tax
type: situation-rules
tax_year: 2026
tier: 2
last_updated: 2026-11-13
---

# Indiana corporate income tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick reference:** corporate AGI rate 4.9%; IT-20 is due in the fifth month after year-end. Financial institutions have a separate FIT-20 franchise-tax regime. Annual 2026 forms were not confirmed. Built from the law; Not yet approved.

## Who this applies to

Corporations with Indiana-source income or other filing obligations. Classify the entity, nexus, group status and special industry before computation. Partnerships, S corporations and PTET elections require separate return analysis; a corporate legal name alone does not select IT-20. The [DOR corporate catalogue](https://www.in.gov/dor/tax-forms/corporate/current-corporatepartnership/) separates IT-20, IT-20S, IT-65 and FIT-20.

## Rates, bands and thresholds

| Item | Amount and conditions | Official source |
|---|---|---|
| Ordinary corporate AGI tax | 4.9% for periods after June 30, 2021, including the current continuing rate | [Bulletin 12; IC 6-3-2-1(c)](https://www.in.gov/dor/files/reference/ib12.pdf) |
| Financial-institution franchise tax | 4.9% after calendar 2022; separate FIT-20 base/regime | [Bulletin 12; IC 6-5.5](https://www.in.gov/dor/files/reference/ib12.pdf) |
| Corporate estimate trigger | Estimated AGI tax exceeds $2,500 for the year | [Bulletin 11](https://www.in.gov/dor/files/reference/ib11.pdf) |
| Estimate installments | Due the 20th of the fourth, sixth, ninth and twelfth months of the tax year | [Bulletin 11](https://www.in.gov/dor/files/reference/ib11.pdf) |
| Estimated payment electronic requirement | Required payment exceeds $5,000 | [Bulletin 11](https://www.in.gov/dor/files/reference/ib11.pdf) |
| IT-20 annual filing | 15th day of fifth month after year-end; confirm calendar adjustment | [Bulletin 12 filing requirements](https://www.in.gov/dor/files/reference/ib12.pdf) |

## The base

Prepare the federal result in `us-form-1120-c-corp`. Federal figures remain there. [Bulletin 12](https://www.in.gov/dor/files/reference/ib12.pdf), corporate AGI computation, starts with net federal taxable income and adjustments under IC 6-3-1-3.5(b), (d) or (e). Allocate/apportion and reconcile losses and credits before determining tax; an already agreed Indiana taxable base may be multiplied by the rate, but gross receipts are not that base.

The [forms catalogue](https://www.in.gov/dor/tax-forms/corporate/current-corporatepartnership/) names Schedule E for apportionment, Schedule F for nonbusiness allocation, IT-20NOL for losses and IT-20PIC for intangible/related-interest disclosure. Its available IT-20 booklet is dated 2025; do not relabel its fields as a final 2026 return.

| Boundary | Treatment | Source |
|---|---|---|
| Financial institution | Route to FIT-20; this skill does not compute the franchise base | [Bulletin 12](https://www.in.gov/dor/files/reference/ib12.pdf) |
| Consolidated group | Election and group qualification require separate analysis | [Bulletin 12](https://www.in.gov/dor/files/reference/ib12.pdf) |
| S corporation or partnership | IT-20S/IT-65 and possible PTET/composite obligations, not automatic C corporation treatment | [DOR corporate catalogue](https://www.in.gov/dor/tax-forms/corporate/current-corporatepartnership/) |
| Historic utility receipts tax | Repealed from July 2022; historical unpaid periods can remain due | [Bulletin 12](https://www.in.gov/dor/files/reference/ib12.pdf) |

## Deadlines and filing

Use the correct annual return and supporting schedules through authorized filing software or an allowed paper route. Separately record filing acceptance and payment. [INTIME](https://intime.dor.in.gov/) manages payments/accounts; select the corporate tax period and retain the confirmation. The [catalogue](https://www.in.gov/dor/tax-forms/corporate/current-corporatepartnership/) explains corporate estimates and E-6 account setup.

[Bulletin 11](https://www.in.gov/dor/files/reference/ib11.pdf) permits estimates through INTIME without a paper IT-6. Paper estimated accounts are opened with E-6. Compute required installments under the current-year, prior-year or annualized rules that actually apply; do not take the trigger as the installment amount. The annual return deadline differs from installment deadlines.

## Penalties and interest

Estimate underpayment and annual payment/filing failures are distinct. A current validated extension-payment calculation, numerical penalty schedule and interest rate are not supplied here. Confirm the e-filing threshold/exceptions and final annual packet before preparing a filing.

## Cross-border points

Multistate income requires allocation/apportionment, nexus and possible Public Law 86-272 analysis. Related-party adjustments and consolidated elections are not resolved by this basic rate calculation. The federal owner `us-pl-86-272-income-tax-nexus` supplies the federal framework; Indiana's application needs state facts and current law.

## Two worked examples that recompute

**Basic tax.** Invented ordinary corporation has $100,000 of already reconciled Indiana taxable income and no credits. At 4.9%, tax is $4,900, exceeding the $2,500 estimate trigger. This is not a gross-receipts computation.

```oa-check
name: Indiana ordinary corporate tax 2026
inputs:
  indiana_taxable_income: 100000
steps:
  tax: indiana_taxable_income * 0.049
  excess_over_estimate_trigger: tax - 2500
expected:
  tax: 4900
  excess_over_estimate_trigger: 2400
```

**Estimate trigger boundary.** On invented reconciled bases of $50,000 and $52,000, tax is $2,450 and $2,548. Only the latter exceeds the statutory trigger. The $2,500 boundary is a condition, not a deductible allowance. This example does not elect or compute an installment safe harbour. Sources: [Bulletins 12](https://www.in.gov/dor/files/reference/ib12.pdf) and [11](https://www.in.gov/dor/files/reference/ib11.pdf).

```oa-check
name: Indiana corporate estimate trigger boundary
inputs:
  lower_base: 50000
  higher_base: 52000
steps:
  lower_tax: lower_base * 0.049
  higher_tax: higher_base * 0.049
  higher_excess: higher_tax - 2500
expected:
  lower_tax: 2450
  higher_tax: 2548
  higher_excess: 48
```

## Ask the client first

- Which annual period, federal entity classification and Indiana registration apply?
- What Indiana activities, sources, nexus and group/industry status exist?
- What federal-to-Indiana reconciliation, allocation, losses and credits support the base?
- What prior/current tax, estimates and annualization facts determine installments?
- What elections, extensions, notices and payments need reconciliation?

## Sources

| Source | URL | Read for | Read for on |
|---|---|---|---|
| Bulletin 12; IC 6-3 and 6-5.5 | https://www.in.gov/dor/files/reference/ib12.pdf | Read for rate tables, corporate-base definition, financial-institution boundary, utility repeal, filing deadline and consolidated-election discussion | 2026-11-13 |
| Bulletin 11 | https://www.in.gov/dor/files/reference/ib11.pdf | Read for pages 1-3 for estimate trigger, installment dates, electronic threshold, IT-6 and E-6 | 2026-11-13 |
| DOR corporate forms catalogue | https://www.in.gov/dor/tax-forms/corporate/current-corporatepartnership/ | Read for annual 2025 form labels, schedules, return types and estimate-payment/account setup | 2026-11-13 |

Not yet confirmed: final annual 2026 form lines/conformity adjustments and e-filing exceptions; complete nexus/apportionment, special industries/FIT-20, consolidated reporting, losses, related-party adjustments and credits; full PTET/composite/pass-through obligations; installment safe harbours, extension tests and numerical penalty/interest schedules. The available 2025 IT-20 download returned 403 and is not claimed as read.
