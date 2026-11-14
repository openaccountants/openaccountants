---
name: co-corporate-tax
description: Colorado C corporation income tax in 2026, including the published estimated-tax rate, federal-to-state reconciliation, nexus boundaries, DR 0112 filing and estimated payments. Group changes from 2026 and full special-industry calculations remain explicit gaps.
version: 1.0
jurisdiction: US-CO
category: state-tax
type: situation-rules
tax_year: 2026
last_updated: 2026-11-13
tier: 2
domain: corporate-tax
---

# Colorado corporate income tax v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick reference:** published 2026 DR 0112EP uses 4.4%; annual DR 0112 is due on the fifteenth day of the fifth month after year-end. Corporate estimates generally start above $5,000 net tax. Confirm the final annual rate/packet and the changed 2026 group rules. Built from the law; Not yet approved.

## Who this applies to

Domestic C corporations and foreign C corporations doing business in Colorado. Federal classification matters; prepare the federal result in `us-form-1120-c-corp`. S corporations, partnerships and SALT Parity elections need their separate Colorado return analysis. Exempt organizations can still have taxable unrelated business income. See [DOR corporate rules, Parts 1-3](https://tax.colorado.gov/corporate-income-tax-guide).

## Rates, bands and thresholds

| Item | Amount / condition | Official source |
|---|---|---|
| Published 2026 estimated corporate rate | 4.4% on the reconciled Colorado base; final annual rate/any TABOR adjustment requires confirmation | [2026 DR 0112EP, worksheet](https://tax.colorado.gov/sites/default/files/documents/DR0112EP_2026.pdf) |
| Substantial nexus, out-of-state corporation | Property >$50,000, payroll >$50,000, sales >$500,000, or at least 25% of total property/payroll/sales in Colorado; statutory definitions apply | [DOR Part 1; Rule 39-22-301(1)](https://tax.colorado.gov/corporate-income-tax-guide) |
| Estimated-tax trigger | Expected net Colorado liability exceeds $5,000 | [2026 DR 0112EP](https://tax.colorado.gov/sites/default/files/documents/DR0112EP_2026.pdf) |
| Required annual estimates | Generally lesser of 70% current net liability or eligible 100% prior liability; prior year must be a filed full 12-month year and large-corporation restrictions apply | [2026 DR 0112EP](https://tax.colorado.gov/sites/default/files/documents/DR0112EP_2026.pdf) |
| Ordinary installment dates | Fifteenth day of months 4, 6, 9 and 12; calendar year April 15, June 15, September 15, December 15 | [2026 DR 0112EP](https://tax.colorado.gov/sites/default/files/documents/DR0112EP_2026.pdf) |
| Annual filing | Fifteenth day of fifth month after year-end; automatic six-month filing extension; next business day rule | [DOR Part 10; §39-22-601](https://tax.colorado.gov/corporate-income-tax-guide) |

Property/payroll/sales thresholds are not the sales-tax nexus rule. An entity organized or commercially domiciled in Colorado has substantial nexus without testing those out-of-state thresholds. Apply Public Law 86-272 separately using `us-pl-86-272-income-tax-nexus`; this federal protection does not follow merely from low Colorado receipts.

## The base

Start with federal taxable income, make Colorado additions/subtractions, then allocate/apportion and apply Colorado losses and credits. [DOR Parts 3-8](https://tax.colorado.gov/corporate-income-tax-guide) explain the sequence. Colorado and certain foreign income taxes deducted federally are added back; another state's income tax is not automatically the same adjustment. Add back the federal NOL deduction and determine a separate Colorado NOL deduction. A reconciled Colorado taxable base is not gross receipts.

Apportionment is generally market based. Related-party transactions, foreign-source income, special industries and alternative methods require a complete schedule and current rule. Retain Schedule RF support and the state/federal bridge; this skill does not supply a universal apportionment percentage.

**2026 group boundary.** DOR Part 2 expressly confines its old three-of-six unity tests to years beginning **before January 1, 2026**, and directs later years to §39-22-303(11.5). Do not use the old tests as a 2026 group determination. The new group regime, foreign-jurisdiction inclusions and 2026 deduction-conformity changes are pending full reading here.

**Losses.** DOR Part 8 provides Colorado carryforward and limitation rules, including no carryback, vintage-dependent carryforward periods and the state application of federal limitations. Do not import a federal loss balance unchanged. Detailed vintage, ownership-change and group computations remain partial.

## Deadlines and filing

Use DR 0112 with supporting schedules through Revenue Online, authorized e-filing or the allowed paper route. The annual deadline is separate from the estimate dates. Preserve filing acceptance and payment confirmations under the same Colorado Account Number.

The [2026 estimate instructions](https://tax.colorado.gov/sites/default/files/documents/DR0112EP_2026.pdf) require the same separate/consolidated/combined method and account as the eventual annual return. Notify DOR in writing before filing if estimate accounts differ. Electronic payments do not require sending the paper DR 0112EP.

Eligible ordinary corporations usually pay four equal quarters of the required annual amount. Large corporations may use prior liability for the first installment subject to second-installment catch-up; they cannot assume a whole-year prior-tax safe harbour. Short-year and annualized rules have their own payment periods. Use DR 0205 for underpayments.

[Part 10](https://tax.colorado.gov/corporate-income-tax-guide) requires an amended DR 0112X following federal changes, generally within 180 days of the specified finalization or amended-federal filing event. A filing extension does not extend payment.

## Penalties and interest

[DOR Part 9](https://tax.colorado.gov/corporate-income-tax-guide) publishes an 11% calendar-2026 estimated-tax interest rate and describes per-installment underpayment. The annual payment/filing penalty, discounted-interest tests and extension-payment computation were not fully verified for this skill. Do not apply an individual penalty formula automatically to a corporation.

## Cross-border points

Check Colorado nexus, federal protection and allocation/apportionment independently. Classify foreign-source income and foreign group members under the applicable year before using exclusions or add-backs. Complete PTET/SALT Parity, insurance/captive and financial-industry work remains outside this basic corporate computation.

## Two worked examples that recompute

**Ordinary estimate computation.** Invented eligible corporation has $300,000 already reconciled Colorado taxable income, no credits and $8,000 prior net tax on a filed 12-month return. It is eligible to use prior liability. At the published estimated rate, tax is $13,200; 70% is $9,240, so the smaller prior amount is $8,000, or $2,000 per ordinary quarter. This does not establish final annual tax if a later rate adjustment applies.

```oa-check
name: Colorado ordinary corporate annual estimate choice
inputs:
  reconciled_colorado_income: 300000
  eligible_prior_tax: 8000
steps:
  estimated_tax: reconciled_colorado_income * 0.044
  current_option: estimated_tax * 0.70
  required_annual: min(current_option, eligible_prior_tax)
  ordinary_quarter: required_annual / 4
expected:
  estimated_tax: 13200
  current_option: 9240
  required_annual: 8000
  ordinary_quarter: 2000
```

**Trigger, both sides.** Invented reconciled bases of $100,000 and $120,000 yield $4,400 and $5,280 before credits. Only the latter exceeds the $5,000 estimate trigger. Testing liability is different from choosing the required annual payment.

```oa-check
name: Colorado corporate estimate trigger boundary
inputs:
  lower_base: 100000
  higher_base: 120000
steps:
  lower_tax: lower_base * 0.044
  higher_tax: higher_base * 0.044
  lower_excess: max(0, lower_tax - 5000)
  higher_excess: max(0, higher_tax - 5000)
expected:
  lower_tax: 4400
  higher_tax: 5280
  lower_excess: 0
  higher_excess: 280
```

## Ask the client first

- What tax year, accounting period and federal/entity classification apply?
- What Colorado organization, domicile, property, payroll, receipts and protected activities exist?
- Which related entities, foreign jurisdictions and group elections apply?
- What federal-to-state modifications, allocation/apportionment, losses and credits are supported?
- What prior filed-year liability, large-corporation status, payments and notices apply?

## Sources

| Source | URL | Read for | Read on |
|---|---|---|---|
| DOR corporate rules | https://tax.colorado.gov/corporate-income-tax-guide | Read for Parts 1-4 classification/nexus, old-versus-2026 group boundary, base/add-back sequence; Part 8 loss boundary; Parts 9-10 estimates, filing and amendments | 2026-11-13 |
| 2026 DR 0112EP | https://tax.colorado.gov/sites/default/files/documents/DR0112EP_2026.pdf | Read for instructions/worksheet on rate, trigger, eligible prior-tax choice, large-corporation catch-up, account consistency and installment dates | 2026-11-13 |
| DOR DR 0112EP catalogue | https://tax.colorado.gov/DR0112EP | Read for actual 2026 download; stale page prose names 2024, so the dated PDF controls this skill's estimate figures | 2026-11-13 |

Not yet confirmed: final annual 2026 DR 0112 packet/rate and any TABOR change; full §39-22-303(11.5) combined regime, special-session foreign/deduction changes, related-party adjustments, complete apportionment, NOL vintages/ownership changes, credits, PTET and specialist regimes; annual penalties and extension-payment tests. These gaps remain README partials.
