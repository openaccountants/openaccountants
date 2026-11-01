---
name: cf-payroll-social
description: >
  Use this Central African Republic payroll Guide for 2026 research on employee IRPP withholding, monthly versus small-employer remittance and annual employer summaries. It routes the actual salary tax calculation to the individual income Guide and clearly separates tax withholding from CNSS contributions. Search triggers include salary tax, PAYE, employer return, five employees, quarterly remittance, CNSS, social security and payroll cessation. Conflicting old social rates and ceilings are expressly withheld because the official CNSS and Labour Ministry sources could not be opened successfully. The payroll calendar is a conditional code baseline, not a complete operative 2026 payroll or contribution schedule.
jurisdiction: CF
category: payroll
tax_year: 2026
tax_year_notes: "2026 research draft; conditional code baseline and named enacted amendments, not full operative coverage"
tier: 2
last_updated: 2026-11-01
version: 0.1
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Central African Republic payroll withholding and social-security holds v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Source status:** Employers withholding tax from salary and resident recipients of foreign-paid salary. SC coverage remains incomplete; this Guide does not authorise calculating, declaring or paying CNSS. Independent pack review is pending. Do not treat this draft as an accountant sign-off or permission to file.

## Who this applies to

Employer payroll withholding uses monthly net salary and the annual employee scale brought down to a month. Use the salary base and bands owned by the individual Guide; do not substitute old conflicting CNSS percentages into the base. [CGI art. 110](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger W01).

## Rates, bands and thresholds

| Item and conditions | Tax year / source |
|---|---|
| The CGI baseline states employer remittance no later than the 15th of each month. Employers with at most five workers may remit quarterly by the 15th of the following month; the exception concerns remittance, not permission to omit withholding from pay. Confirm current filing instructions and period attribution. | 2026 research scope; CGI arts. 110–112 [official text](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf); ledger W02 |

## The base

Obtain each worker’s classification, gross pay/benefits and verified exempt items/deductions. Determine net taxable salary using [individual income tax](cf-income-tax.md), then apply the scale for the correct period. Withhold from pay and classify employer remittance frequency by the statutory worker threshold. Reconcile the annual named summary to actual tax withheld and paid. Keep CNSS liabilities separate until its contribution base, ceiling, split and reporting law are authenticated.

## Deadlines and filing

Each remittance is accompanied by an administration-provided slip in two copies. Employer annual summary of named employee IRPP withholdings goes in before 31 January. Do not confuse it with the employee annual income return. [CGI arts. 113, 119](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger W03).

On business cession/cessation, retained tax is remitted within ten days of the event under article 112. Foreign-paid CAR-resident salary recipients have the article 111 personal instalment obligation; foreign payment does not remove payroll-income tax. [CGI arts. 111–112](https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf) (ledger W04).

Obtain the actual administration slip and current remittance instructions. Retain payroll register, employee identifiers, payment and submission acknowledgements. The current tax form/boxes, submission channel, CNSS form and contribution due dates were not opened and stop live filing. For departures, read [cross-border](cf-cross-border.md).

## Penalties and interest

Use [tax overview](cf-tax-overview.md) for the read general penalty text and unresolved priority of older special penalties. No CNSS late-payment percentage is asserted.

## Cross-border points

Foreign-paid resident salary remains a distinct article 111 route. Posting, pension coverage coordination, foreign contribution deductions and treaty employment relief require their own verified conditions.

## Two worked examples that recompute

All amounts below are XAF. Inputs are fictional. Code-baseline cases are conditional on confirming the cited provisions remain applicable to the actual 2026 case. Arithmetic checks do not verify current law.

### 1. Monthly tax from a supplied annual liability

Assume a full-year fixed payroll after all salary rules are checked, with computed annual employee IRPP XAF 152,160. Bringing that liability to twelve identical months gives XAF 12,680 each. This arithmetic does not independently determine gross-to-net deductions or CNSS.

```oa-check
name: Monthly tax from a supplied annual liability
inputs:
  annual_tax: 152160
  months: 12
steps:
  - monthly_tax: annual_tax/months
expected:
  monthly_tax: 12680
```

### 2. Five or six workers changes remittance route

Assume each worker has XAF 12,680 properly computed monthly withholding, the quoted calendar still applies, and the workforce is unchanged for a full quarter. Five workers give quarterly remittance of 190,200 under the exception. Six workers give 76,080 per monthly remittance; withholding continues in both cases.

```oa-check
name: Five or six workers changes remittance route
inputs:
  per_worker: 12680
  small_workers: 5
  larger_workers: 6
steps:
  - small_quarter: per_worker*small_workers*3
  - larger_month: per_worker*larger_workers
expected:
  small_quarter: 190200
  larger_month: 76080
```

## Ask the client first

- Employment or another worker relationship and actual pay period?
- Salary, benefits, exempt items and verified deductible contributions?
- Number of workers and eligibility for the small-employer remittance rule?
- Foreign payers, postings, exits or business cessation?
- CNSS registration, authoritative rate/base/ceiling notice and current forms?

## Sources

| Source | URL | Read on / scope |
|---|---|---|
| DGID official CGI edition marked updated 2023 (cover also says mise à jour 2022) | https://www.finances.gouv.cf/sites/default/files/2023-05/CGI%20RCA%202017%20mise%20%C3%A0%20jour%202023.pdf | 2026-11-01; Read cited articles and neighbouring scope/definitions/exceptions; not all 442 pages. Mixed edition dates and later-law consolidation unresolved. |

Not yet confirmed: Current payroll amendments and period-attribution instructions; all CNSS rates, branches, wage base/ceiling and filing/payment calendar; employer 19%, pension 4%, family 11%, injury 2%, employee 1.6% and XAF 600,000 claims from the old draft; training/apprenticeship tax around 2%; a universal 15th CNSS deadline. Official CNSS page returned 404 in browser and the Labour Ministry PDF failed TLS; neither was read as law.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
