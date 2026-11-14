---
name: kn-social-security-contributions
description: >
  Saint Kitts and Nevis social security contributions for 2026. Covers the employee 5%
  and employer 5% plus 1% employment injury (11% in all) for ages 16 to 62, the 1% only
  outside that range, the EC$6,500 monthly insurable earnings ceiling, the age-week rule
  in regulation 5, insurable earnings and the December bonus exclusion, self-employed at
  10% of the selected income category, and payment at month end or within one month
  after. Trigger phrases include St Kitts social security, Nevis social security
  contributions, SKN social security ceiling.
version: 1.0
jurisdiction: KN
tax_year: 2026
last_updated: 2026-11-14
category: international
type: computation
domain: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Saint Kitts and Nevis social security contributions

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Contributions under the Social Security Act, Chapter 22.10 (revised to 31 December 2017) and the Social Security (Contributions) Regulations, as administered by the St Christopher and Nevis Social Security Board, in 2026. Covers employees, employers and the self-employed rate. Amounts are EC$. The Housing and Social Development Levy and the severance contribution have no ceiling and are in [kn-housing-social-development-levy](kn-housing-social-development-levy.md).

## Ask the client first

1. Date of birth: is the worker under 16, 16 to 62, or over 62?
2. Monthly insurable earnings with every component (overtime, housing allowance, commission, shift pay, production bonus, service charge, employer-paid liabilities, holiday pay, gratuities).
3. Any December bonus, retirement lump sum or other gratuity?
4. Employer registration number; for the self-employed, the selected income category.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Employee, ages 16 to 62 | 5% deducted from wages | [Board contributions page](https://socialsecurity.kn/contributions-2/) |
| Employer, ages 16 to 62 | 5% plus 1% employment injury (11% in all) | same |
| Under 16 and over 62 | Only the 1% employment injury contribution | same |
| Ceiling | EC$6,500 a month (Schedule 2, from 1 January 1998) | [Social Security Act Cap. 22.10, Contributions Regulations Schedule 2](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-22_10-Social-Security-Act.pdf) |
| Self-employed, 16 to 62 | 10% of the selectable income category, subject to the ceiling | same |
| Age weeks, reg.5 | Contribution due for the week a worker reaches 16 and the week they reach 62, but none if they reach 62 on the Monday of that week | same |
| Payment, reg.14(1) | At the end of the month wages are paid, or within one month after | same |
| Excluded from earnings | Lump sums paid on retirement and any bonus paid in December | [Board contributions page](https://socialsecurity.kn/contributions-2/) |

### Steps

1. **Age:** apply reg.5 by contribution week (weeks start on a Monday).
2. **Insurable earnings:** all cash earnings in the list above; exclude retirement lump sums and December bonuses. Ordinary December wages are not excluded because of the month.
3. **Cap** at EC$6,500 a month.
4. **Contributions:** employee 5%, employer 6% (5% + 1%), for ages 16 to 62; employer 1% only outside that range.
5. **Pay** with the statement of wages (Form C3) by the end of the following month at the latest; file a nil return where nothing is due.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Worker earns 9,000 a month | Social security base 6,500; the housing levy still applies to all 9,000 | [Board employers' guide](https://socialsecurity.kn/wp-content/uploads/2018/05/Employers-Guide-2018.pdf) |
| Worker turns 62 on a Monday | No contribution for that week (only the 1% employer injury from then) | [Act Cap. 22.10, reg.5](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-22_10-Social-Security-Act.pdf) |
| January wages | Due end of January, may be paid by end of February | [Board employers' guide](https://socialsecurity.kn/wp-content/uploads/2018/05/Employers-Guide-2018.pdf) |
| Employee omitted from a statement | Supplementary statement (reg.12) | [Act Cap. 22.10](https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-22_10-Social-Security-Act.pdf) |
| Late payment | Penalty of 10% then 1% a month (the guide applies the same method to the levy) | [Board employers' guide](https://socialsecurity.kn/wp-content/uploads/2018/05/Employers-Guide-2018.pdf) |

## Worked cases

### Case 1: aged 40 at three pay levels

At 4,000: employee 200, employer 240, total 440. At 9,000 the base is 6,500: employee 325, employer 390, total 715.

```oa-check
name: SKN social security, 4,000 and 9,000 a month
inputs:
  pay_low: 4000
  pay_high: 9000
  ceiling: 6500
steps:
  - low_employee: min(pay_low, ceiling) * 0.05
  - low_employer: min(pay_low, ceiling) * 0.06
  - high_employee: min(pay_high, ceiling) * 0.05
  - high_employer: min(pay_high, ceiling) * 0.06
  - high_total: high_employee + high_employer
expected:
  low_employee: 200
  low_employer: 240
  high_employee: 325
  high_employer: 390
  high_total: 715
```

### Case 2 (decision): pay the December extra as a bonus or as salary?

An employee on 4,000 a month gets an extra 2,000 in December. Paid as a December bonus, it is excluded: contributions stay 200 employee and 240 employer. Paid as extra salary, the base is 6,000: 300 and 360. The label must match what the payment really is.

```oa-check
name: SKN December extra, bonus against salary
inputs:
  pay: 4000
  extra: 2000
  ceiling: 6500
steps:
  - bonus_employee: min(pay, ceiling) * 0.05
  - bonus_employer: min(pay, ceiling) * 0.06
  - salary_employee: min(pay + extra, ceiling) * 0.05
  - salary_employer: min(pay + extra, ceiling) * 0.06
expected:
  bonus_employee: 200
  bonus_employer: 240
  salary_employee: 300
  salary_employer: 360
```

## When to refuse or refer

- Multiple employers, partial periods, unpaid leave, special coverage.
- Benefits and pension eligibility; voluntary contributions.
- Any change after the 2017 revision (no later instrument checked).

## Filing and payment

1. Register the employer and use the allocated employer number ([Board employers page](https://socialsecurity.kn/employers-2/)).
2. Each month send the statement of wages and contributions (C3) with payment by the end of the following month (reg.14); send a nil statement if nothing is due.
3. Reconcile worker numbers, earnings, contribution weeks, deductions and the employer cost to the return.

## Completion checklist

- Age weeks applied; December bonus and retirement lump sums excluded.
- 6,500 ceiling applied to social security only.
- 5% and 6%; paid within one month after month end.

## Sources

| Source | URL | Read on |
|---|---|---|
| Social Security Act Cap. 22.10 (revised to 31 Dec 2017), Contributions Regulations: read for reg.5 age weeks, reg.14 payment, the self-employed 10% schedule and the Schedule 2 ceiling of EC$6,500 a month | https://lawcommission.gov.kn/wp-content/documents/Act17TOC/Ch-22_10-Social-Security-Act.pdf | 2026-11-14 |
| Board contributions page: read for the 5% + 5% + 1% (11%) rates, the 1% outside ages 16 to 62, and the insurable earnings list with the retirement and December bonus exclusions | https://socialsecurity.kn/contributions-2/ | 2026-11-14 |
| Board employers' guide 2018: read for payment timing, the 6,500 ceiling against no ceiling for the levy, and penalties | https://socialsecurity.kn/wp-content/uploads/2018/05/Employers-Guide-2018.pdf | 2026-11-14 |
| Board employers page: read for employer registration and the employer number | https://socialsecurity.kn/employers-2/ | 2026-11-14 |

Not yet confirmed: amendments after 31 December 2017 (none checked); the social security late penalty in the regulations themselves (the guide describes it with the levy); the self-employed income categories.
