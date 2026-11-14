---
name: vc-national-insurance
description: "Saint Vincent and the Grenadines National Insurance Services (NIS) contributions for 2026. Covers the 14% rate (6.5% employee, 7.5% employer) on insurable earnings up to EC$1,200 a week, EC$5,200 a month or EC$62,400 a year, the 0.5% employment injury contribution, insurable earnings including bonuses and payments in kind, registration within 7 days on Form R3, payment within one month after month end with the turnaround schedule or Form C2, the 10% surcharge and 1% a month compound interest, and the year-end Form C1A. Trigger phrases include SVG NIS, St Vincent national insurance, NIS contributions St Vincent."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/vc-national-insurance"
  jurisdiction: "VC"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Saint Vincent and the Grenadines national insurance

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Contributions to the National Insurance Services (NIS) of Saint Vincent and the Grenadines in 2026 under the National Insurance Act, Cap. 296, as published in the NIS employers' guide. Covers employees and employers, ceilings, earnings, remittance and penalties. Amounts are EC$. Self-employed and voluntary contributions, benefits and special age groups are outside it. PAYE income tax is due by the 15th of the next month ([IRD taxes page](https://ird.gov.vc/index.php/taxes)).

## Ask the client first

1. Pay frequency and gross pay for each period, with every component (overtime, shift pay, arrears, holiday pay, family allowances, bonuses, commission, service charge, payments in kind, danger money).
2. How many employees (more than 10 means Form C2)?
3. Age: is anyone turning 16 or reaching retirement age this period?
4. Does any employee work for more than one employer in the same week?
5. Employer registration number; any employee on NIS sickness or maternity benefit?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Total rate | 14% of insurable earnings | [NIS employers' guide](https://www.nissvg.org/employers-guide/) |
| Employee share | 6.5% | same |
| Employer share | 7.5% | same |
| Ceiling | EC$5,200 a month or EC$1,200 a week (the guide also gives the yearly equivalent) | same |
| Employment injury | Employers pay .5% of insurable earnings for all employees | same |
| Employer registration | Within 7 days of employing the first employee, Form R3 | same |
| Payment | Within one month after the end of the month | same |
| Late payment | 10% surcharge on the contributions payable, plus 1% compound interest for each month or part month outstanding | same |
| Refund of contributions paid in error | Within two years of submission, on application | same |

### Steps

1. **Register** within 7 days of the first employee (Form R3).
2. **Insurable earnings:** salary or wages plus every listed component, payments in kind included.
3. **Cap** by pay period: 1,200 a week or 5,200 a month (62,400 a year). Do not turn the weekly cap into a four-week month.
4. **Contributions:** 6.5% employee and 7.5% employer; the employer may not recover its share from the employee.
5. **Remit** within one month after month end with the turnaround contribution schedule (and Form C2 if more than 10 employees), or through eSubmit.
6. **Year end:** Form C1A for all employees; outstanding schedules by 31 March of the next year.

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Employee turns 16 or retirement age in a week | Contribution due for that full week; none if the retirement date is a Monday | [NIS employers' guide](https://www.nissvg.org/employers-guide/) |
| Employee on NIS sickness or maternity benefit for a full week | No contribution for that week | same |
| Paid vacation, sick or maternity leave with wages | Contributions due | same |
| Two employers in the same week | Each pays on its own wages | same |
| Underpayment | NIS notice; settle within one month | same |
| Overpayment | Credited to the next month; refunds after year-end reconciliation | same |
| Employee leaves | Return the earnings record within 14 days | same |

## Worked cases

### Case 1: monthly and weekly workers

Monthly 3,000: employee 195, employer 225, total 420. Monthly 6,500 capped at 5,200: 338 and 390, total 728. Weekly 1,500 capped at 1,200: 78 and 90.

```oa-check
name: SVG NIS 2026, monthly 3,000 and 6,500, weekly 1,500
inputs:
  m_low: 3000
  m_high: 6500
  w_high: 1500
steps:
  - low_employee: min(m_low, 5200) * 0.065
  - low_employer: min(m_low, 5200) * 0.075
  - high_employee: min(m_high, 5200) * 0.065
  - high_employer: min(m_high, 5200) * 0.075
  - high_total: high_employee + high_employer
  - week_employee: min(w_high, 1200) * 0.065
  - week_employer: min(w_high, 1200) * 0.075
expected:
  low_employee: 195
  low_employer: 225
  high_employee: 338
  high_employer: 390
  high_total: 728
  week_employee: 78
  week_employer: 90
```

### Case 2 (decision): pay on time or a month late?

Contributions of 728 for a month. Paid within one month after month end: 728. Paid one month late: 10% surcharge of 72.80 plus 1% interest on the total, about 8.01, so roughly 808.81. The surcharge alone is worth paying on time for.

```oa-check
name: SVG NIS late payment on 728, one month outstanding
inputs:
  due: 728
steps:
  - surcharge: due * 0.10
  - with_surcharge: due + surcharge
  - interest: round(with_surcharge * 0.01, 2)
  - total: with_surcharge + interest
expected:
  surcharge: 72.8
  with_surcharge: 800.8
  interest: 8.01
  total: 808.81
```

## When to refuse or refer

- Self-employed and voluntary contributions, benefits.
- The exact base of the 1% compound interest (the guide does not say whether it runs on the surcharge too; Case 2 assumes it does).
- Principal employer and agency arrangements.

## Filing and payment

1. Pay by post or in person at the Kingstown or Union Island offices, or submit through eSubmit ([NIS employers' guide](https://www.nissvg.org/employers-guide/)).
2. The schedule shows employer and employee names and numbers, the month, weekly earnings for weekly workers, gross pay, insurable earnings and the 14% total.
3. Submit Form C1A at year end; report a work injury in writing within 10 days.

## Completion checklist

- All components in; ceiling by pay period.
- 6.5% and 7.5%; employer share not recovered from staff.
- Paid within one month after month end; C1A filed.

## Sources

| Source | URL | Read on |
|---|---|---|
| NIS employers' guide page: read for registration (Form R3, 7 days), the 14% rate and split, the EC$62,400, 5,200 and 1,200 ceilings, insurable earnings, remittance and Form C2, the 10% surcharge and 1% compound interest, age weeks, multiple employers, refunds, 0.5% employment injury and Form C1A | https://www.nissvg.org/employers-guide/ | 2026-11-14 |
| IRD taxes page: read for PAYE remittance by the 15th of the next month | https://ird.gov.vc/index.php/taxes | 2026-11-14 |

Not yet confirmed: the National Insurance Act and Contributions Regulations as amended (not reconciled); whether the 0.5% injury contribution is inside or on top of the employer's 7.5% (the guide lists it separately); the interest base.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `vc-national-insurance` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/vc-national-insurance. If neither is available, confirm every figure against the official source pages cited above before relying on it.
