---
name: tc-national-insurance
description: >
  Turks and Caicos National Insurance Board contributions for 2026. Covers private sector
  employees (5.5% employee and 6.5% employer on insurable earnings up to USD 4,000 a
  month), public officers, the self-employed rate of 11% of elected weekly income from
  1 April 2026 under Legal Notice 3 of 2026 and its new payment window, voluntary
  contributors at 10%, registration from age 16 to 65, the monthly payment and grace
  period, and the online payment portal. Trigger phrases include NIB contributions, Turks
  and Caicos national insurance, TCI social security, NIB self-employed 11%.
version: "1.0"
jurisdiction: TC
tax_year: 2026
last_updated: 2026-11-14
category: payroll
type: computation
domain: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Turks and Caicos national insurance contributions v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

National Insurance Board (NIB) contributions in the Turks and Caicos Islands for 2026, under the National Insurance Ordinance and the National Insurance (Contributions) Regulations as amended. Covers private sector employees and employers, the self-employed and voluntary contributors, with the public officer rate noted. Amounts are US dollars. National Health Insurance is a separate charge with a different ceiling: [tc-national-health-insurance](tc-national-health-insurance.md). There is no income tax on wages in the Turks and Caicos Islands.

## Ask the client first

1. Is the person a private sector employee, a public officer, self-employed or a voluntary contributor?
2. Monthly insurable earnings (for the self-employed, the weekly income elected with the Board).
3. Age (registration covers people aged 16 to 65 who are gainfully employed).
4. Are the employer and employee registered with the NIB?
5. For which month is the payment being made?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Private sector, employer share | 6.5% of insurable earnings | [NIB contribution rates](https://www.tcinib.tc/contribution-rates/) |
| Private sector, employee share | 5.5% of insurable earnings (12% total) | same |
| Insurable earnings ceiling | USD 4,000 a month; earnings above it are not subject to contributions | same |
| Public officers, total | 9.15% (rates in effect from 1 April 2024 after the 9th and 10th actuarial reviews) | [NIB about us](https://www.tcinib.tc/about-us/) |
| Self-employed, from 1 April 2026 | 11% of the weekly income elected under reg.15, for each contribution week (reg.14 as substituted) | [LN 3 of 2026](https://www.gov.tc/agc/component/edocman/3-of-2026-national-insurance-contributions-amendment-regulations-2026/fdocument?Itemid=9999) |
| Self-employed payment window | Contributions for weeks in any month may be paid in any month, but not later than the end of the contribution year (reg.16(1) as substituted) | same |
| Voluntary contributors | 10% of declared income agreed with the Board | [NIB contribution rates](https://www.tcinib.tc/contribution-rates/) |
| Employer payment timing | Monthly, with a 30-day (one-month) grace period: the current month pays for the previous month | same |
| Replacement registration card | USD 20.00 | [NIB FAQ](https://www.tcinib.tc/faq/) |

### Steps

1. **Register** the employer and every employee aged 16 to 65 gainfully employed in the Islands ([NIB FAQ](https://www.tcinib.tc/faq/)).
2. **Insurable earnings:** monthly pay, capped at USD 4,000.
3. **Private sector:** employee 5.5% (deducted from pay) and employer 6.5% of capped earnings. The employer remits both shares.
4. **Self-employed:** 11% of the elected weekly income for each contribution week from 1 April 2026. Long-term benefits are computed from total contributions paid in the contribution year; short-term benefits use the previous year's average weekly insurable earnings, and a self-employed person whose previous-year contributions are below the qualifying sum is disqualified from short-term benefits (regs.14A and 14B).
5. **Pay** monthly, the current month for the previous month, in person or through the NIB online payment portal.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Employee earning USD 6,000 a month | Base capped at 4,000: USD 220 employee, 260 employer | [NIB contribution rates](https://www.tcinib.tc/contribution-rates/) |
| Self-employed rate shown as 10% in some Board pages | 10% is the voluntary contributor rate and the April 2024 self-employed rate; from 1 April 2026 the self-employed rate is 11% | [LN 3 of 2026](https://www.gov.tc/agc/component/edocman/3-of-2026-national-insurance-contributions-amendment-regulations-2026/fdocument?Itemid=9999); [NIB about us](https://www.tcinib.tc/about-us/) |
| Self-employed person who pays late in the year | Allowed until the end of the contribution year, but short-term benefits depend on the qualifying sum for the previous year | LN 3 of 2026 regs.14B, 16 |
| Health insurance | Separate NHIP charge, 3% plus 3% to USD 7,800 | [tc-national-health-insurance](tc-national-health-insurance.md) |

## Worked cases

### Case 1: private sector employee, two salary levels

At USD 3,000 a month: employee 165, employer 195, total 360. At USD 6,000 a month the base is capped at 4,000: employee 220, employer 260, total 480.

```oa-check
name: TCI NIB private sector contributions, 3,000 and 6,000 a month
inputs:
  pay_low: 3000
  pay_high: 6000
  ceiling: 4000
steps:
  - low_employee: min(pay_low, ceiling) * 0.055
  - low_employer: min(pay_low, ceiling) * 0.065
  - high_employee: min(pay_high, ceiling) * 0.055
  - high_employer: min(pay_high, ceiling) * 0.065
  - high_total: high_employee + high_employer
expected:
  low_employee: 165
  low_employer: 195
  high_employee: 220
  high_employer: 260
  high_total: 480
```

### Case 2 (decision): which weekly income should a self-employed person elect?

Electing USD 800 a week costs 11% = 88 a week, 4,576 over 52 weeks. Electing 1,000 costs 110 a week, 5,720 a year, 1,144 more. The higher election raises the contributions paid, from which long-term benefits are computed, and the average weekly insurable earnings for short-term benefits. Choose on the benefit cover wanted; the cost difference is 11% of the extra income elected.

```oa-check
name: TCI NIB self-employed election, 800 against 1,000 a week, from April 2026
inputs:
  low_election: 800
  high_election: 1000
  weeks: 52
steps:
  - low_weekly: low_election * 0.11
  - high_weekly: high_election * 0.11
  - low_year: low_weekly * weeks
  - high_year: high_weekly * weeks
  - extra_cost: high_year - low_year
expected:
  low_weekly: 88
  high_weekly: 110
  low_year: 4576
  high_year: 5720
  extra_cost: 1144
```

## When to refuse or refer

- Public officers: only the 9.15% total is confirmed; the split is not set out here.
- Whether the USD 4,000 monthly ceiling caps the self-employed elected income: not confirmed; ask the Board.
- Benefit claims and appeals (appeals go to the Appeals Tribunal within 21 days of the decision): out of scope.
- Late payment penalties and interest: not confirmed here.

## Filing and payment

1. Register as an employer at an NIB office using the employer registration form; register each employee.
2. Each month pay the previous month's contributions (employee and employer shares) with the contribution schedule, at an office or through the online payment portal ([NIB FAQ](https://www.tcinib.tc/faq/)).
3. Self-employed persons pay the 11% weekly contributions in any month up to the end of the contribution year ([LN 3 of 2026](https://www.gov.tc/agc/component/edocman/3-of-2026-national-insurance-contributions-amendment-regulations-2026/fdocument?Itemid=9999)).
4. Controls: match worker numbers to the schedule, reconcile the wage base to payroll, keep the two shares apart in the ledger, keep the schedule and receipt.

## Completion checklist

- Contributor category set; ceiling applied.
- 5.5% and 6.5% for private sector; 11% for the self-employed from April 2026.
- Paid monthly within the grace period.
- NHIP computed separately.

## Sources

| Source | URL | Read on |
|---|---|---|
| NIB contribution rates page: read for the private sector shares, the self-employed and voluntary rates, the USD 4,000 ceiling and payment timing | https://www.tcinib.tc/contribution-rates/ | 2026-11-14 |
| NIB about us: read for the 1 April 2024 rates (12% private sector, 9.15% public officers, 10% self-employed) | https://www.tcinib.tc/about-us/ | 2026-11-14 |
| NIB FAQ: read for registration ages, employer registration, the online portal, appeals and the card fee | https://www.tcinib.tc/faq/ | 2026-11-14 |
| Legal Notice 3 of 2026, National Insurance (Contributions) (Amendment) Regulations 2026: read for the 11% self-employed rate from 1 April 2026, regs.14A, 14B and 16 | https://www.gov.tc/agc/component/edocman/3-of-2026-national-insurance-contributions-amendment-regulations-2026/fdocument?Itemid=9999 | 2026-11-14 |

Not yet confirmed: the public officer split between officer and Government; whether the ceiling applies to self-employed elected income; late payment penalties and interest; the National Insurance Ordinance and principal Contributions Regulations text (not opened; the rates rest on the Board's pages and LN 3 of 2026); weekly ceilings and age boundaries for contributions beyond registration.
