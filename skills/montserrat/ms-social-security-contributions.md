---
name: ms-social-security-contributions
description: >
  Montserrat Social Security Fund contributions for 2026. Covers the rates from 1 January
  2026 (employee 7%, employer 8% including 1% employment injury, 15% in all), the ceiling
  of EC$4,000 a month or EC$923 a week, earnings counted to the nearest dollar, what
  counts as insurable earnings (Christmas bonuses and retirement lump sums out), age weeks
  from 16 to pensionable age 65, the self-employed rate of 12% on a selected income
  category, and payment at month end or within one month. Trigger phrases include
  Montserrat social security, Montserrat SSF contributions, Montserrat payroll.
version: 1.0
jurisdiction: MS
tax_year: 2026
last_updated: 2026-11-14
category: international
type: computation
domain: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Montserrat social security contributions

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Contributions under the Social Security Act, Cap. 18.09 (revised to 1 January 2025) and its Contributions Regulations, administered by the Montserrat Social Security Fund, in 2026. Covers employees, employers and the self-employed rate. Amounts are EC$. Income tax on emoluments (PAYE) is under s.51 of the Income and Corporation Tax Act and outside this skill.

## Ask the client first

1. Date of birth (contributions run from the week the worker turns 16 to the week they reach 65).
2. Weekly or monthly pay, with every component (overtime, housing allowance, commission, shift pay, production bonus, service charge, employer-paid liabilities, holiday pay, gratuities).
3. Any Christmas bonus or retirement lump sum?
4. For the self-employed: the income category selected on registration.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Employee, from 1 January 2026 | 7% of insurable earnings | [Social Security Act Cap. 18.09, Contributions Regulations Schedule](https://parliament.ms/wp-content/uploads/2026/05/18.09-Social-Security-Act.pdf) |
| Employer, from 1 January 2026 | 8% (7% + 1% employment injury) | same |
| Ceiling | EC$4,000 a month or EC$923 a week, earnings calculated to the nearest dollar | same |
| 2026 monthly table | Employee 7%, employer 8%; for example 4,000 gives 280.00, 320.00, total 600.00 | [Social Security Fund monthly rate tables 2026](https://socialsecurity.ms/wp-content/uploads/2025/12/Monthly-Rates-2026.pdf) |
| Self-employed, 1 January 2026 and after | 12% (11.5% in 2025) | [Social Security Act Cap. 18.09, Contributions Regulations reg.6(2)](https://parliament.ms/wp-content/uploads/2026/05/18.09-Social-Security-Act.pdf) |
| Self-employed income categories, reg.7 | EC$600, 1,200, 1,800, 2,400, 3,000, 3,600 or 4,000 | same |
| Pensionable age | 65 | [Social Security Act Cap. 18.09, s.2](https://parliament.ms/wp-content/uploads/2026/05/18.09-Social-Security-Act.pdf) |
| Payment, reg.12 | At the end of the month wages are paid, or within one month after | same |

### Steps

1. **Age weeks:** from the week the worker turns 16 to the week they reach 65; if the birthday is a Monday that week is excluded (reg.5). Weeks start on a Monday.
2. **Insurable earnings:** all cash earnings in the list; exclude retirement lump sums and Christmas bonuses or similar payments. A production bonus paid in December is not a Christmas bonus by date alone.
3. **Cap** at 4,000 a month or 923 a week; keep the two limits separate.
4. **Contributions:** 7% employee and 8% employer; do not add the 1% injury on top of the 8%.
5. **Pay** at month end or within one month after; on termination pay outstanding contributions too.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Worker over 65 | Ordinary schedule shows nil; reg.5(c) deals separately with employment injury after pensionable age; confirm with the Fund | [Cap. 18.09, reg.5](https://parliament.ms/wp-content/uploads/2026/05/18.09-Social-Security-Act.pdf) |
| Weekly worker on 1,200 | Base 923 | same |
| Earnings with cents | Earnings are calculated to the nearest dollar; contribution amounts keep cents (see the Fund table) | [Fund 2026 table](https://socialsecurity.ms/wp-content/uploads/2025/12/Monthly-Rates-2026.pdf) |
| January contributions | Payable no later than the end of February | [Cap. 18.09, reg.12](https://parliament.ms/wp-content/uploads/2026/05/18.09-Social-Security-Act.pdf) |

## Worked cases

### Case 1: monthly and weekly employees

Monthly 3,000: employee 210, employer 240, total 450. Monthly 5,500 capped at 4,000: 280 and 320, total 600. Weekly 1,200 capped at 923: 64.61 and 73.84, total 138.45.

```oa-check
name: Montserrat social security 2026, monthly 3,000 and 5,500, weekly 1,200
inputs:
  m_low: 3000
  m_high: 5500
  week: 1200
steps:
  - low_employee: min(m_low, 4000) * 0.07
  - low_employer: min(m_low, 4000) * 0.08
  - high_total: min(m_high, 4000) * 0.15
  - week_employee: min(week, 923) * 0.07
  - week_employer: min(week, 923) * 0.08
  - week_total: week_employee + week_employer
expected:
  low_employee: 210
  low_employer: 240
  high_total: 600
  week_employee: 64.61
  week_employer: 73.84
  week_total: 138.45
```

### Case 2 (decision): which self-employed income category?

A self-employed person picks a category under reg.7. At the 2,400 category the contribution is 12% = 288 a period; at the 4,000 top category it is 480. The higher category raises the earnings on which benefits are based; the extra cost is 192 a period. Choose the category that most closely represents real earnings, as reg.7 requires.

```oa-check
name: Montserrat self-employed, 2,400 against 4,000 category at 12%
inputs:
  low_category: 2400
  high_category: 4000
steps:
  - low_contribution: low_category * 0.12
  - high_contribution: high_category * 0.12
  - extra: high_contribution - low_contribution
expected:
  low_contribution: 288
  high_contribution: 480
  extra: 192
```

## When to refuse or refer

- Voluntary contributors, multiple employments, irregular pay and benefits.
- Employment injury cover after 65.
- Whether reg.7 categories are weekly or monthly in practice (the regulation says weekly income): confirm with the Fund before computing a year.

## Filing and payment

1. Register the employer and employees with the Fund.
2. Pay employee and employer contributions with the contribution statement at month end or within one month after (reg.12).
3. Reconcile worker numbers, contribution weeks, the wage base and both shares; keep payment evidence.

## Completion checklist

- Age weeks applied; Christmas bonus and retirement lump sums excluded.
- Ceiling 4,000 a month or 923 a week.
- 7% and 8% (injury inside the 8%); paid within one month.

## Sources

| Source | URL | Read on |
|---|---|---|
| Social Security Act Cap. 18.09, revised to 1 January 2025, with the Contributions Regulations: read for s.2 (pensionable age 65), reg.5 age weeks, reg.6(2) self-employed rates, reg.7 income categories, reg.12 payment, the earnings list and the Schedule rows for 2026 (7%, 8% with 1% injury, 4,000 and 923) | https://parliament.ms/wp-content/uploads/2026/05/18.09-Social-Security-Act.pdf | 2026-11-14 |
| Social Security Fund monthly rate tables, 1 January to 31 December 2026: read for the 7% and 8% columns and the rows for 3,000, 3,500 and 4,000 | https://socialsecurity.ms/wp-content/uploads/2025/12/Monthly-Rates-2026.pdf | 2026-11-14 |

Not yet confirmed: amendments after 1 January 2025; late payment penalties; whether self-employed categories are applied weekly or monthly; employment injury contributions after 65.
