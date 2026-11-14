---
name: tc-national-health-insurance
description: >
  Turks and Caicos National Health Insurance Plan contributions for employers and
  employees in 2026. Covers the 3% employee and 3% employer shares, the USD 25 monthly
  minimum per party, the USD 7,800 monthly and USD 1,800 weekly earnings ceilings, which
  allowances count, two or more employers and the refund, combined employed and
  self-employed earnings, and when to pay (the Board's 7th and 14th dates, the 3% monthly
  late fee and the 2024 amendment to the statutory payment date). Trigger phrases include
  NHIP contributions, Turks and Caicos health insurance payroll, NHIB 3%, TCI NHI ceiling.
version: "1.0"
jurisdiction: TC
tax_year: 2026
last_updated: 2026-11-14
category: payroll
type: computation
domain: tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
---

# Turks and Caicos national health insurance contributions v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Contributions to the National Health Insurance Plan (NHIP), run by the National Health Insurance Board, for employees and employers in 2026, under the National Health Insurance Ordinance, Cap. 8.10, and its Contributions Regulations (revised edition showing the law at 31 March 2021, with the 2024 amendment). Amounts are US dollars. National Insurance Board contributions are a separate charge with a different ceiling: [tc-national-insurance](tc-national-insurance.md). The Turks and Caicos Islands levy no income tax on wages.

## Ask the client first

1. Is the person an employee, self-employed, or both in the same month?
2. Is the employee paid monthly or weekly (or another period)?
3. Gross earnings for the period, and any transport, telephone, housing or other allowances, bonuses or gratuities.
4. Does the employee work for more than one employer in the same month?
5. When will the salary information and payment reach the Board?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Total contribution | 6% of earnings for the week or month (Contributions Regulations reg.4(1)) | [NHI Ordinance Cap. 8.10, revised edition](https://www.gov.tc/agc/component/edocman/08-10-national-health-insurance-ordinance-2/fdocument?Itemid=9999) |
| Employee share | 3% of earnings | same |
| Employer share | 3% of earnings | same |
| Minimum contribution per month | USD 50, of which USD 25 employer and USD 25 employee (reg.4(2)) | same |
| Earnings ceiling, paid monthly | USD 7,800 a month with any one employer (reg.6(b)) | same |
| Earnings ceiling, paid weekly or otherwise not monthly | USD 1,800 a week (reg.6(a)) | same |
| Transport allowance | Counts only above USD 230 a month (reg.5(1)(d)) | same |
| Telephone allowance | Counts only above USD 60 a month (reg.5(1)(e)) | same |
| Employed and self-employed in the same period | Contributions on both up to USD 7,800 a month combined (reg.8) | same |
| Board submission date | Salary information and payment due by the 7th; payments accepted to the 14th (next business day if the 14th is a weekend or holiday) | [NHIB billing](https://tcinhip.tc/billing/) |
| Late fee | 3% a month for payments not made within the allotted time | same |
| Statutory payment date after the 2024 amendment | Monthly earnings: by the end of the calendar month after the contribution month; weekly earnings: by the end of the month after the month the weeks begin (LN 4 of 2024, from 1 February 2024) | [LN 4 of 2024](https://www.gov.tc/agc/component/edocman/4-of-2024-national-health-insurance-contributions-amendment-regulations-2024/fdocument?Itemid=9999) |

### Steps

1. **Build earnings** (reg.5): gross pay including overtime, cost-of-living, family and housing allowances, long-service rewards, service charges, production bonus or incentive pay, commission, gratuities (but not retirement lump sums or a Christmas bonus or similar payment), dirty or dangerous work pay, night or shift pay and holiday pay; transport allowance above USD 230 a month and telephone allowance above USD 60 a month. Payments made late are counted in the period they are paid.
2. **Cap** at USD 7,800 a month (USD 1,800 a week for non-monthly pay) per employer.
3. **Compute each share** at 3% of capped earnings, with a floor of USD 25 a month each.
4. **Two or more employers** (reg.7): each source pays up to its maximum; a person whose total earnings are above the maximum is refunded the excess.
5. **Employed and self-employed** (reg.8): contributions on both, up to USD 7,800 a month combined.
6. **Pay** with the statement of contributions (reg.9). Follow the Board's 7th and 14th dates, which are earlier than the amended statutory date, to avoid the 3% monthly late fee.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Earnings USD 500 a month | Floor applies: USD 25 each, not 15 | [NHI Ordinance reg.4(2)](https://www.gov.tc/agc/component/edocman/08-10-national-health-insurance-ordinance-2/fdocument?Itemid=9999) |
| Earnings USD 10,000 a month, one employer | Capped at 7,800: USD 234 each | same, reg.6 |
| Christmas bonus | Excluded from earnings | same, reg.5(1)(j) |
| Husband and wife both employees | Each contributes as if not married | same, reg.3(4) |
| Employee receives no cash pay | The Chief Executive Officer sets the contribution from comparable earnings | same, reg.5(3) |
| Board date and statutory date differ | Pay by the Board's date; the late fee is the Board's | [NHIB billing](https://tcinhip.tc/billing/); [LN 4 of 2024](https://www.gov.tc/agc/component/edocman/4-of-2024-national-health-insurance-contributions-amendment-regulations-2024/fdocument?Itemid=9999) |

## Worked cases

### Case 1: salary with transport and telephone allowances

Salary USD 3,000, transport allowance 300 and telephone allowance 100 in a month. Earnings = 3,000 + (300 - 230) + (100 - 60) = 3,110. Each share is 3% = 93.30, above the 25 floor and below the ceiling; total 186.60.

```oa-check
name: TCI NHIP contribution with allowances, monthly
inputs:
  salary: 3000
  transport: 300
  telephone: 100
steps:
  - earnings: salary + max(0, transport - 230) + max(0, telephone - 60)
  - capped: min(earnings, 7800)
  - each_share: max(25, capped * 0.03)
  - total: each_share * 2
expected:
  earnings: 3110
  each_share: 93.30
  total: 186.60
```

### Case 2 (decision): two employers, claim the refund or not

An employee earns USD 6,000 a month from one employer and 4,000 from another. Each employer deducts 3%: 180 and 120, total 300. The maximum on 7,800 is 234, so the employee should apply to the Board for a refund of 66 a month (792 over twelve months). With one employer paying all 10,000, the cap applies directly and the deduction is 234.

```oa-check
name: TCI NHIP two employers and the refund
inputs:
  job_a: 6000
  job_b: 4000
steps:
  - deducted: min(job_a, 7800) * 0.03 + min(job_b, 7800) * 0.03
  - maximum: 7800 * 0.03
  - monthly_refund: max(0, deducted - maximum)
  - yearly_refund: monthly_refund * 12
expected:
  deducted: 300
  maximum: 234
  monthly_refund: 66
  yearly_refund: 792
```

## When to refuse or refer

- Self-employed contribution rules and voluntary, student or pensioner contributions: not set out here; ask the Board.
- Benefit and coverage questions (treatment abroad, the coverage limits): out of scope.
- A rate or cap change announced but not enacted (a review of rates and caps was discussed in the House of Assembly on 1 June 2026): do not apply until a legal notice is in force.

## Filing and payment

1. Register the employer and each employee with the Board (registration forms on tcinhip.tc).
2. Each month send the salary information by the 7th and pay by the 14th, with the statement of contributions; employees can check their contributions online ([NHIB billing](https://tcinhip.tc/billing/)).
3. Late payment attracts a 3% monthly late fee.
4. Keep for each employee the identification, start and end dates and each payment of earnings and its period (reg.10).

## Completion checklist

- Earnings built under reg.5, allowances above their thresholds only.
- Ceiling and USD 25 floor applied per employer.
- Refund checked for people with two employers.
- Paid by the Board's dates; statement filed.

## Sources

| Source | URL | Read on |
|---|---|---|
| National Health Insurance Ordinance, Cap. 8.10, revised edition at 31 March 2021, with the Contributions Regulations (gov.tc Attorney General's Chambers): read regs.3 to 10 for the rates, minimum, earnings, ceilings, multiple employments and payment | https://www.gov.tc/agc/component/edocman/08-10-national-health-insurance-ordinance-2/fdocument?Itemid=9999 | 2026-11-14 |
| Legal Notice 4 of 2024, NHI (Contributions) (Amendment) Regulations 2024: read for the substituted payment date from 1 February 2024 | https://www.gov.tc/agc/component/edocman/4-of-2024-national-health-insurance-contributions-amendment-regulations-2024/fdocument?Itemid=9999 | 2026-11-14 |
| National Health Insurance Board, billing page: read for the 7th and 14th dates, the weekend rule and the 3% monthly late fee | https://tcinhip.tc/billing/ | 2026-11-14 |

Not yet confirmed: whether any contribution rate or ceiling changed after the 31 March 2021 revised edition other than by LN 4 of 2024 (the Attorney General's subsidiary legislation lists for 2024 to 2026 were read for NHI items; only LN 4 and 5 of 2024 appeared, and LN 5 concerns registration); LN 4 of 2024 names the Registration Regulations as the principal regulations while amending the payment rule, so how the Board applies it is not confirmed; self-employed rates.
