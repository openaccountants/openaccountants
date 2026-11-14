---
name: mm-payroll-social
description: "Myanmar payroll for 2026 (FY 2026-27, 1 April 2026 to 31 March 2027). Covers Social Security Board contributions (health and social care 2% employer plus 2% employee, 2.5% each for workers over 60 at entry, employment injury 1% employer only), payment by the 15th of the following month and the 10% per 30 days late fine, salary income tax withholding by the employer under the Union Taxation Law 2026 brackets and the 4.8 million kyat exemption, and the annual salary statement due 30 June. Use for questions about Myanmar payroll, SSB contributions, PAYE, salary tax deduction or annual salary statements."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mm-payroll-social"
  jurisdiction: "MM"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Myanmar Payroll and Social Security v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employers in Myanmar running payroll in FY 2026-27 (1 April 2026 to 31 March 2027), for two obligations:

1. **Social security contributions** to the Social Security Board (SSB) under the Social Security Law 2012, at the rates SSB publishes in its contribution calculation sheet.
2. **Salary income tax withholding** for the Internal Revenue Department (IRD) under the Income Tax Law s 16 and the Union Taxation Law 2026. The tax computation itself is in [mm-income-tax](mm-income-tax.md).

## Rates, bands and thresholds

| Item | Amount and conditions | Tax year | Official URL |
|---|---|---|---|
| Health and social care insurance, worker aged 60 or under at entry | Employer 2% plus worker 2% of monthly wages | 2026 | https://www.ssb.gov.mm/Portal/assets/attachment/Contribution_Calculation%28Formula%29.pdf |
| Health and social care insurance, worker over 60 at entry | Employer 2.5% plus worker 2.5% | 2026 | same |
| Employment injury benefit insurance | Employer only 1% | 2026 | same |
| Total, worker 60 or under at entry | 5% (employer 3%, worker 2%; computed: health 2% each plus employment injury 1% employer only) | 2026 | same |
| Total, worker over 60 at entry | 6% (employer 3.5%, worker 2.5%; computed: health 2.5% each plus employment injury 1% employer only) | 2026 | same |
| Payment due | Monthly, not later than the 15th of the following month | 2026 | same |
| Late payment fine | 10% of the month's contribution for each 30 days late, pro rata by day (SSB table runs to 150 days, 50%) | 2026 | https://www.ssb.gov.mm/Portal/assets/attachment/Fine_Calculation%28Formula%29.pdf |
| Salary exempt from income tax | Up to 4.8 million kyats a year; above that, tax on total income | FY 2026-27 | https://www.ird.gov.mm/storage/laws/6a6b496e035ea-utl2026.pdf |
| Salary tax deduction | In as nearly equal instalments as possible over the year, paid to the Union Government within the prescribed period (Income Tax Law s 16(a), (c)) | FY 2026-27 | https://www.ird.gov.mm/storage/laws/68b55a57275e0-Income%20Tax%20Law%20(1).pdf |
| Annual salary statement | Within 3 months after the end of the income year (s 18) | FY 2026-27 | same |
| Annual salary statement due, FY 2025-26 | 30 June 2026; late filing penalty the greater of 5% plus 1% a month and K 100,000 | FY 2025-26 | https://www.ird.gov.mm/announcement-lists/96 |

## The base

**SSB.** Contributions are a percentage of the worker's monthly wages, worked separately for each scheme and added. SSB's own example: wages 300,000 kyats, employer 9,000 and worker 6,000, total 15,000, paid by the 15th of the next month. Whether a wage ceiling applies is not stated on the SSB sheet (see Not yet confirmed).

**Salary tax, each month.**

1. Estimate the employee's annual salary for FY 2026-27.
2. If 4.8 million kyats or less: no tax.
3. If more: annual tax = brackets on (annual salary less reliefs: 20% basic relief to 10 million, spouse, children, parents living with the employee, life insurance, the employee's SSB contributions), per [mm-income-tax](mm-income-tax.md).
4. Deduct one-twelfth (or the remaining instalments) each month; correct over- or under-deduction in later months.
5. Pay to the IRD and keep the challans. The employee's SSB contribution is deducted from pay as well.
6. After 31 March, file the annual salary statement by 30 June. Salary-only employees file nothing themselves.

**Non-resident foreign employees** get no reliefs: tax at the brackets on total salary.

## Deadlines and filing

- SSB: register the establishment and workers with SSB; pay monthly by the 15th of the next month.
- IRD: withhold salary tax monthly; annual salary statement by 30 June 2027 for FY 2026-27, electronically for Large and Medium Taxpayer Office employers (IRD notice of 28 April 2026).

## Penalties and interest

- SSB late payment: 10% of the contribution per 30 days late, pro rata (SSB example: 200,000 kyats 15 days late, fine 10,000).
- Late annual salary statement: greater of 5% of tax owing plus 1% a month and K 100,000.
- Failure to deduct or pay salary tax: employer deemed a defaulter (Income Tax Law s 16(d)).

## Cross-border points

- Foreign employees resident 183 days or more get the reliefs; non-residents do not.
- Myanmar citizens working abroad pay under the special rules in [mm-income-tax](mm-income-tax.md) (s 22 of the Union Taxation Law 2026), not through a Myanmar payroll.
- Social security agreements with other countries are not covered on the SSB pages read.

## Two worked examples that recompute

**Example 1. Worker aged 35, monthly wages 300,000 kyats (SSB's own example).** Employer: 2% + 1% = 9,000. Worker: 2% = 6,000. Total to SSB 15,000 by the 15th. Annual salary 3,600,000 is under 4.8 million: no income tax. Net pay 294,000.

```oa-check
name: Myanmar SSB, wages 300,000 kyats, worker under 60
inputs:
  wages: 300000
steps:
  - employer: wages * 0.02 + wages * 0.01
  - worker: wages * 0.02
  - total_ssb: employer + worker
  - income_tax: 0
  - net_pay: wages - worker - income_tax
expected:
  employer: 9000.00
  worker: 6000.00
  total_ssb: 15000.00
  net_pay: 294000.00
```

**Example 2. Manager, salary 1,000,000 kyats a month, married with one child, SSB paid 15 days late on a 50,000 kyat contribution.** Annual tax per [mm-income-tax](mm-income-tax.md) Example 1 is 305,000, so monthly deduction about 25,416.67. SSB late fine 10% x 15/30 x 50,000 = 2,500.

```oa-check
name: Myanmar monthly salary tax and SSB late fine
inputs:
  annual_tax: 305000
  contribution: 50000
  days_late: 15
steps:
  - monthly_tax: round(annual_tax / 12, 2)
  - fine: contribution * 0.10 * days_late / 30
expected:
  monthly_tax: 25416.67
  fine: 2500.00
```

## Ask the client first

1. Number of workers and each worker's age at entry into SSB coverage.
2. Monthly wages of each worker.
3. For salary tax: annual salary, spouse, children, parents living with the employee, life insurance.
4. Are any employees non-resident foreigners (under 183 days)?
5. Is the employer assessed at a Large or Medium Taxpayer Office (electronic filing)?

## Sources

| Source | What was read | URL | Read on |
|---|---|---|---|
| SSB, contribution calculation sheet (Burmese PDF) | Read for the 2% plus 2%, 2.5% plus 2.5% and 1% rates, the 300,000 kyat example, the 15th-of-month deadline | https://www.ssb.gov.mm/Portal/assets/attachment/Contribution_Calculation%28Formula%29.pdf | 2026-11-14 |
| SSB, fine calculation sheet (PDF) | Read for the 10% per 30 days fine table to 150 days | https://www.ssb.gov.mm/Portal/assets/attachment/Fine_Calculation%28Formula%29.pdf | 2026-11-14 |
| Union Taxation Law 2026, English (IRD) | Read for the 4.8 million salary exemption (s 19) | https://www.ird.gov.mm/storage/laws/6a6b496e035ea-utl2026.pdf | 2026-11-14 |
| Income Tax Law (IRD English text) | Read for s 16 salary deduction and s 18 annual salary statement | https://www.ird.gov.mm/storage/laws/68b55a57275e0-Income%20Tax%20Law%20(1).pdf | 2026-11-14 |
| IRD notice to file returns, annual salary statements and CT returns (28 April 2026) | Read for the 30 June 2026 due date and penalty | https://www.ird.gov.mm/announcement-lists/96 | 2026-11-14 |

Not yet confirmed: the SSB insurable wage ceiling (the old file's 300,000 kyat cap, 9,000 and 6,000 maxima came from a vendor blog; the SSB sheet uses 300,000 as an example, not as a cap); the employer size from which SSB registration is compulsory (old file: 5 or more workers, from a firm site); the IRD deadline for paying monthly salary tax (old file: 15 days, from a firm site); SSB family assistance, invalidity and unemployment schemes and their rates.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mm-payroll-social` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mm-payroll-social. If neither is available, confirm every figure against the official source pages cited above before relying on it.
