---
name: lc-national-insurance
description: >
  Saint Lucia National Insurance Corporation (NIC) contributions for 2026. Covers the
  5% employee and 5% employer contribution, the ceiling of the first EC$5,000 of monthly
  earnings, what counts as gross earnings (overtime, allowances, commission, shift pay,
  service charge, holiday pay, travel allowances over EC$500 a month) and what does not
  (Christmas and production bonuses, severance, terminal gratuities, pay in lieu of leave,
  tips and stipends), payment by the 7th of the next month with Form C3, and multiple
  employers. Trigger phrases include Saint Lucia NIC, St Lucia national insurance, Form C3.
version: 1.0
jurisdiction: LC
tax_year: 2026
last_updated: 2026-11-14
category: international
type: computation
domain: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Saint Lucia national insurance contributions

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Contributions to the National Insurance Corporation (NIC) of Saint Lucia in 2026 for ordinary employees, as published by NIC. Covers the rates, ceiling, earnings base, payment and Form C3. Amounts are EC$. It does not calculate PAYE, benefits or net pay. Self-employed and voluntary contributions need their own assessed base. Income tax deductions: [lc-personal-tax-deductions](lc-personal-tax-deductions.md).

## Ask the client first

1. Is the worker an employee in covered employment? Registered with NIC (non-nationals: work permit or CARICOM Skills Certificate)?
2. Monthly pay with every component: basic, overtime, allowances, commission, shift pay, service charge, holiday pay, travel allowance, bonuses.
3. Does the employee have another employer?
4. Month the contributions relate to.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Employee contribution | 5% of gross wages | [NIC employers](https://www.stlucianic.org/employers) |
| Employer contribution | 5% of gross wages | same |
| Monthly ceiling | Deductions on all amounts up to and including the first EC$5,000 of earnings in a month | [NIC FAQ](https://www.stlucianic.org/faq) |
| Travelling allowance | Included only above EC$500 a month | [NIC employers](https://www.stlucianic.org/employers) |
| Payment date | On or before the 7th of the month after the month the contributions relate to | same |

### Steps

1. **Gross earnings:** basic salary plus overtime, all allowances, commission or profit on sales, night or shift pay, service charge, holiday pay, and travelling allowances over EC$500 a month.
2. **Exclude** Christmas bonuses, annual production bonuses, severance, terminal gratuities, payments in lieu of leave, tips, and meal, uniform and laundry stipends. Decide by what the payment is, not its payroll label.
3. **Cap** at EC$5,000 a month.
4. **Contributions:** 5% employee and 5% employer of the capped base.
5. **Pay** by the 7th of the next month with Form C3 showing both shares; the totals must agree with the payment.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Two employers | Each deducts; contributions above the yearly maximum are refunded | [NIC FAQ](https://www.stlucianic.org/faq) |
| June contributions | Due on or before 7 July | [NIC employers](https://www.stlucianic.org/employers) |
| Travel allowance above EC$500 a month | Include it; the employers page does not say whether only the excess counts, so treat the whole amount as included until NIC confirms | same |
| Non-national employee | Still registered and covered; nationality alone is no exemption | [NIC employees](https://www.stlucianic.org/employees) |

## Worked cases

### Case 1: under and over the ceiling

At EC$3,600: employee 180, employer 180, total 360. At EC$6,200 the base is 5,000: 250 each, total 500.

```oa-check
name: Saint Lucia NIC at 3,600 and 6,200 a month
inputs:
  pay_low: 3600
  pay_high: 6200
  ceiling: 5000
steps:
  - low_each: min(pay_low, ceiling) * 0.05
  - high_each: min(pay_high, ceiling) * 0.05
  - high_total: high_each * 2
expected:
  low_each: 180
  high_each: 250
  high_total: 500
```

### Case 2 (decision): is the December bonus insurable?

An employee earns EC$4,000 basic and EC$500 overtime, and receives a EC$1,000 Christmas bonus. The bonus is excluded, so the base is 4,500 and each side pays 225. Treating the bonus as insurable would raise the base to 5,000 (capped) and each side to 250, over-deducting 25. If the "bonus" is really monthly pay relabelled, it is included.

```oa-check
name: Saint Lucia NIC with an excluded Christmas bonus
inputs:
  basic: 4000
  overtime: 500
  bonus: 1000
  ceiling: 5000
steps:
  - base: min(basic + overtime, ceiling)
  - each: base * 0.05
  - wrong_each: min(basic + overtime + bonus, ceiling) * 0.05
  - over_deduction: wrong_each - each
expected:
  base: 4500
  each: 225
  wrong_each: 250
  over_deduction: 25
```

## When to refuse or refer

- Self-employed and voluntary contributors, benefits, reciprocal agreements.
- Age limits, partial months and irregular periods.
- Late payment penalties: not stated on the NIC pages read.

## Filing and payment

1. Register the employer and each employee with NIC.
2. Each month complete Form C3 (employer name, address, registration number, each employee's earnings and 5% + 5% contributions) and pay by the 7th of the next month ([NIC employers](https://www.stlucianic.org/employers)).
3. Reconcile the earnings schedule, deductions, employer expense and the amount remitted; keep the official receipt.

## Completion checklist

- Included and excluded payments sorted by nature.
- EC$5,000 cap applied.
- 5% + 5%; C3 agrees with payment; paid by the 7th.

## Sources

| Source | URL | Read on |
|---|---|---|
| NIC employers page: read for the 5% + 5% rates, the 7th of the month due date, gross wages inclusions (travel over EC$500) and exclusions (bonuses, severance, gratuities, lieu of leave, tips, stipends) and Form C3 | https://www.stlucianic.org/employers | 2026-11-14 |
| NIC FAQ: read for the first EC$5,000 a month ceiling, insurable earnings, multiple employers and refunds | https://www.stlucianic.org/faq | 2026-11-14 |
| NIC employees page: read for registration documents for non-nationals | https://www.stlucianic.org/employees | 2026-11-14 |

Not yet confirmed: the National Insurance Act and regulations (not opened); late payment penalties; whether the travel allowance counts in full or only above EC$500; the yearly maximum used for multiple-employer refunds; self-employed rates.
