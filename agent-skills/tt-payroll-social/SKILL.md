---
name: tt-payroll-social
description: "Trinidad and Tobago employer payroll for 2026, PAYE income tax, health surcharge and National Insurance (NIS). Gives the NIS rate of 16.2% of insurable earnings from 5 January 2026 (NIBTT: subject to all legislative approvals; 19.2% from 4 January 2027), shared one third employee and two thirds employer, the 16 earnings classes with the top class from TT$13,600 a month, health surcharge of TT$8.25 or TT$4.80 a week, PAYE at 25% and 30% after the TT$90,000 personal allowance, the TD1 and TD4, remittance by the 15th, the annual PAYE summary by the end of February and the late payment charges. Trigger on Trinidad payroll, PAYE Trinidad, NIS Trinidad, NIBTT, health surcharge, TD1, TD4. Built from NIBTT, the Income Tax Act and IRD pages; not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/tt-payroll-social"
  jurisdiction: "TT"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Trinidad and Tobago Payroll and Social Contributions v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employers in Trinidad and Tobago paying emoluments in 2026, and their employees. PAYE and health surcharge are remitted to the Board of Inland Revenue (IRD); National Insurance is administered by the National Insurance Board of Trinidad and Tobago (NIBTT). Amounts are TT$.

- **In:** PAYE on emoluments, health surcharge, employee and employer NIS by earnings class.
- **Out:** the employee's annual return (use `tt-income-tax`), voluntary NIS contributions beyond the table reference, NIS benefits.

## Rates, bands and thresholds

| Item | Amount | Conditions | Source |
|---|---|---|---|
| NIS total contribution rate | 16.2% of insurable earnings | From 5 January 2026; NIBTT's table and PDF say "subject to all legislative approvals" and no enacting legal notice was found on NIBTT's legislation page (13.2% from 5 September 2016): see Not yet confirmed | NIBTT, earning classes and contribution rates: https://www.nibtt.net/Contribution_Rates/rates.html |
| NIS rate from 2027 | 19.2% | From 4 January 2027 | same |
| NIS 2026, class I | Weekly earnings TT$200 to 339.99 (monthly TT$867 to 1,472.99): employee TT$14.60, employer TT$29.20 a week | Lowest class; 2026 table subject to all legislative approvals | NIBTT, 2026 contribution table: https://www.nibtt.net/Contribution_Rates/NISContributions_20260105.pdf |
| NIS 2026, class XIV | Weekly TT$2,630 to 2,919.99 (monthly TT$11,397 to 12,652.99): employee TT$149.90, employer TT$299.80 | | same |
| NIS 2026, class XV | Weekly TT$2,920 to 3,137.99 (monthly TT$12,653 to 13,599.99): employee TT$163.60, employer TT$327.20 | | same |
| NIS 2026, class XVI (ceiling) | Weekly TT$3,138 and over (monthly TT$13,600 and over): employee TT$169.50, employer TT$339.00, total TT$508.50 a week | Highest class | same |
| Health surcharge, higher rate | TT$8.25 a week | Weekly emoluments over TT$109.00 or monthly over TT$469.99 | IRD, corporations page: https://www.ird.gov.tt/corporations |
| Health surcharge, lower rate | TT$4.80 a week | All other employed persons; none for under 16, 60 and over, or pension-only income | same |
| PAYE rates | 25% of chargeable income up to TT$1,000,000, 30% above | Annualised from the TD1 | Income Tax Act, Chap. 75:01, Third Schedule: https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.01-Income-Tax-Act--2024.pdf |
| Personal allowance | ninety thousand dollars a year (TT$90k) | Resident employees (s. 17) | same |
| PAYE and health surcharge remittance | By the 15th of the month after deduction, with the monthly return | | IRD, self-employed and sole traders (employer duties): https://www.ird.gov.tt/self-employed-sole-trader |
| Annual PAYE summary and TD4 certificates | By the last day of February of the following year | All employees | same |
| Late PAYE on pension or annuity refunds withheld | Penalty plus 20% a year interest | Income Tax Act provisions on deducted tax not remitted by the 15th | Income Tax Act, Chap. 75:01: https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.01-Income-Tax-Act--2024.pdf |

The full 16-class table is in the NIBTT 2026 PDF; the employee pays one third and the employer two thirds of each weekly contribution.

### PAYE formula (IRD)

```
total annual income - total tax deductions (TD1) = chargeable income
chargeable income x tax rate = tax on chargeable income
tax on chargeable income - tax credits = income tax liability
income tax liability / number of pay periods = tax per pay period
```

## The base

- **NIS** is a fixed weekly amount per earnings class, chosen from the employee's actual earnings; insurable earnings above the class XVI floor do not raise the contribution.
- **PAYE** uses the employee's TD1 (or IRD-approved TD1 where claims need prior approval: tertiary education, first home, alimony, annuity or pension, venture capital). A new TD1 is due within 7 days of a change.
- **Every worker**, including part-time and casual, needs a BIR number.
- **Health surcharge** depends on the level of emoluments, not a percentage.

## Deadlines and filing

| Step | What | When |
|---|---|---|
| 1 | Register for a PAYE account and a health surcharge account with the IRD; register as an employer with NIBTT | Before the first payroll |
| 2 | Deduct PAYE, health surcharge and employee NIS each pay period | Pay day |
| 3 | File the monthly PAYE and health surcharge return and pay | By the 15th of the following month |
| 4 | Pay NIS for each contribution week | See Not yet confirmed for the NIBTT due date |
| 5 | Annual PAYE summary to IRD; TD4 certificates to employees | By the last day of February 2027 for 2026 |

## Penalties and interest

- Tax deducted and not remitted by the 15th attracts a penalty and interest at 20% a year under the Income Tax Act's withholding provisions.
- NIS late payment charges: see Not yet confirmed.

## Cross-border points

- Non-resident employees generally have no personal allowance (see `tt-income-tax`).
- Social security agreements: not covered; check NIBTT.

## Two worked examples that recompute

### Example 1: Employee on TT$180,000 a year, 12 monthly pays

Chargeable income TT$180,000 - TT$90,000 = TT$90,000; tax TT$22,500 a year, TT$1,875 a month. Monthly pay TT$15,000 is in NIS class XVI of NIBTT's 2026 table (subject to all legislative approvals, see Not yet confirmed): employee TT$169.50 and employer TT$339.00 a week; a month with four contribution weeks gives TT$678.00 and TT$1,356.00. Health surcharge TT$8.25 a week, TT$33.00 for four weeks.

```oa-check
name: TT 2026 monthly payroll, salary 180k a year, four-week month
inputs:
  annual_salary: 180000
  allowance: 90000
  weeks: 4
steps:
  - chargeable: annual_salary - allowance
  - annual_tax: min(chargeable, 1000000) * 0.25 + max(chargeable - 1000000, 0) * 0.30
  - monthly_paye: annual_tax / 12
  - nis_employee: 169.50 * weeks
  - nis_employer: 339.00 * weeks
  - health_surcharge: 8.25 * weeks
expected:
  chargeable: 90000
  annual_tax: 22500
  monthly_paye: 1875
  nis_employee: 678
  nis_employer: 1356
  health_surcharge: 33
```

### Example 2: How the class XVI contribution splits, and the employer's cost for a year

At 16.2% (NIBTT's 2026 table, subject to all legislative approvals; see Not yet confirmed) the class XVI weekly total is TT$508.50: the employee pays one third (TT$169.50) and the employer two thirds (TT$339.00). A year of 52 contribution weeks costs the employer TT$17,628 at the 2026 rate; budget for the 19.2% table from 4 January 2027.

```oa-check
name: TT 2026 NIS class XVI shares and annual employer cost
inputs:
  total_week: 508.50
  weeks_year: 52
steps:
  - employee_week: total_week / 3
  - employer_week: total_week * 2 / 3
  - employer_year: employer_week * weeks_year
expected:
  employee_week: 169.50
  employer_week: 339.00
  employer_year: 17628
```

## Ask the client first

1. Each employee's pay frequency, earnings and age (health surcharge exemptions under 16 and from 60).
2. TD1 for each employee, and IRD approval where claims need it.
3. Number of contribution weeks in each pay month (NIS is weekly).
4. Are all workers registered with BIR numbers and NIS numbers?
5. Any non-resident employees?
6. Were monthly returns filed and paid by the 15th?

## Sources

| Source | URL | Read on |
|---|---|---|
| NIBTT, earning classes, contribution rates and benefit rates page: read for the 16.2% rate from 5 January 2026 (subject to legislative approvals) and 19.2% from 4 January 2027 | https://www.nibtt.net/Contribution_Rates/rates.html | 2026-11-14 |
| NIBTT, earnings classes and contributions from 5 January 2026: read in full for the 16 classes and the employee and employer weekly amounts | https://www.nibtt.net/Contribution_Rates/NISContributions_20260105.pdf | 2026-11-14 |
| NIBTT, Acts and amendments page: read for the contribution orders and legal notices listed (latest contribution amendment 2008; none for 2025 or 2026) | https://www.nibtt.net/Amendments/NIBTTAct_amend.html | 2026-11-14 |
| IRD, corporations page: read for PAYE computation, health surcharge rates and exemptions | https://www.ird.gov.tt/corporations | 2026-11-14 |
| IRD, self-employed and sole traders page: read for employer duties, the 15th monthly deadline and the end of February annual summary | https://www.ird.gov.tt/self-employed-sole-trader | 2026-11-14 |
| Income Tax Act, Chap. 75:01 (2024 consolidation): read for s. 17, the Third Schedule and the withholding remittance and interest provisions | https://www.ird.gov.tt/Media/Default/IRDLegislation/Ch2024_75.01-Income-Tax-Act--2024.pdf | 2026-11-14 |

Not yet confirmed: whether the 16.2% NIS rate and the 2026 class amounts received all legislative approvals (NIBTT's 2026 PDF still says "subject to all legislative approvals"; NIBTT's legislation page, read 14 Nov 2026, lists no 2025 or 2026 contribution order or legal notice); employers paying at the 2026 table follow NIBTT's published rates; the NIBTT payment due date for contributions (earlier version: by the 15th of the following month) and NIS late payment surcharges; the earlier version's statement that employee NIS is deductible for income tax; how the monthly number of contribution weeks is counted for a monthly payroll; the penalty percentage for late PAYE remittance by employers.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `tt-payroll-social` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/tt-payroll-social. If neither is available, confirm every figure against the official source pages cited above before relying on it.
