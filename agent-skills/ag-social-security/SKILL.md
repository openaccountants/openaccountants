---
name: ag-social-security
description: "Antigua and Barbuda Social Security Board contributions for 2026. Covers the statutory maximum rates reached on 1 January 2025 (private sector 7% employee and 9% employer, public service 6% and 9%), the contribution ceiling of EC$1,500 a week or EC$6,500 a month, the self-employed rate of 10%, pensionable age 65, the earnings base, and the monthly remittance due 14 days after month end. Trigger phrases include Antigua social security, ABSSB contributions, Antigua payroll social security, contribution ceiling."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ag-social-security"
  jurisdiction: "AG"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Antigua and Barbuda social security contributions

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Contributions to the Antigua and Barbuda Social Security Board (ABSSB) in 2026 under the Social Security (Collection of Contributions) Regulations 2013 (SI 15 of 2013) as amended by SI 60 of 2016. Covers private sector and public service employees and employers, the self-employed rate, the ceiling, the earnings base and the monthly remittance. Amounts are EC$. The Medical Benefits Scheme is a separate charge with its own rates and no shared ceiling: [ag-medical-benefits](ag-medical-benefits.md). ABST is in [ag-abst](ag-abst.md).

## Ask the client first

1. Is the worker in the public service (including a statutory board) or the private sector, or self-employed?
2. Pay frequency (weekly or monthly) and gross earnings for the period, with every component (overtime, commission, housing allowance, bonus, service charge, holiday pay).
3. Date of birth: is the worker under 16, or at or near pensionable age (65)?
4. Do any payments relate to an earlier or later wage period (delayed or set-aside payments)?
5. Is the employer registered with the Board, and has every employee a social security number?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure and conditions | Official source |
|---|---|---|
| Private sector, from 1 January 2025 | 16% of wages up to the ceiling: 7% employee, 9% employer (SI 60/2016 Schedule, 2025 row) | [SI 60 of 2016](https://socialsecurity.gov.ag/wp-content/uploads/2021/03/no-60-of-2016-collection-of-contributions-amendment.pdf) |
| Public service, from 1 January 2025 | 15% of wages up to the ceiling: 6% employee, 9% employer | same |
| Contribution ceiling | EC$1,500 a week and EC$6,500 a month | same |
| Self-employed rate | 10% (unchanged in 2025) | [ABSSB media release, 31 December 2024](https://socialsecurity.gov.ag/media-release-pension-contribution-rate-adjustments/) |
| Pensionable age | 65 from 1 January 2025 (SI 61 of 2016) | same |
| Remittance deadline | No later than 14 days after the end of each month (reg.9) | [SI 15 of 2013](https://socialsecurity.gov.ag/wp-content/uploads/2021/03/no-15-of-2013-collection-of-contributions-regulations.pdf) |

### Steps

1. **Cover.** Contributions apply from age 16 up to pensionable age (65). Under the new regulation 4(5) a contribution is due for the week in which the person reaches 16, and for the week in which they reach pensionable age, but not if they reach pensionable age on the Monday of that week and are not employed after it. Apply this week rule rather than a whole-month exemption.
2. **Earnings base (reg.4(2)).** Gross cash earnings including overtime, commissions, housing allowances, bonuses, service charges and holiday pay. Allocate delayed or set-aside payments to the wage period they belong to under the provisos.
3. **Cap** the base at EC$6,500 a month or EC$1,500 a week, after adding every component.
4. **Rates.** Private sector 7% employee and 9% employer; public service 6% and 9%. The 2025 rates are the statutory maximum: SI 60 of 2016 sets no further step after 1 January 2025.
5. **Remit** both shares with the monthly remittance form by the 14th day after month end. If the form is missing by the 14th, the Director may assess the contributions (reg.9(5)).

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Employee earning EC$8,000 a month | Base capped at 6,500 | [SI 60 of 2016](https://socialsecurity.gov.ag/wp-content/uploads/2021/03/no-60-of-2016-collection-of-contributions-amendment.pdf) |
| Under-deduction found later | Recover only as regulations 7 to 9 allow; do not take arbitrary historic amounts from the next salary | [SI 15 of 2013](https://socialsecurity.gov.ag/wp-content/uploads/2021/03/no-15-of-2013-collection-of-contributions-regulations.pdf) |
| Overpayment made in good faith | The employer may recover it under reg.9(3), but only to the extent it accounted to the employee for any over-deduction | same |
| Short payment | The Director advises the employer and sets a date to pay the difference (reg.9(4)) | same |
| Worker reaches 65 on the Monday of a week and stops work | No contribution for that week (reg.4(5) proviso) | SI 60 of 2016 |
| Medical Benefits on the same wages | Separate scheme, separate base and return | [ag-medical-benefits](ag-medical-benefits.md) |

## Worked cases

### Case 1: private sector employee, two salary levels

At EC$4,000 a month: employee 280, employer 360, total 640. At EC$8,000 the base is capped at 6,500: employee 455, employer 585, total 1,040.

```oa-check
name: ABSSB private sector, 4,000 and 8,000 a month (2026)
inputs:
  pay_low: 4000
  pay_high: 8000
  ceiling: 6500
steps:
  - low_employee: min(pay_low, ceiling) * 0.07
  - low_employer: min(pay_low, ceiling) * 0.09
  - high_employee: min(pay_high, ceiling) * 0.07
  - high_employer: min(pay_high, ceiling) * 0.09
  - high_total: high_employee + high_employer
expected:
  low_employee: 280
  low_employer: 360
  high_employee: 455
  high_employer: 585
  high_total: 1040
```

### Case 2 (decision): public service or private sector rate?

A statutory board employee earns EC$8,000 a month. The public service definition includes a statutory board, so the employee pays 6% of 6,500 = 390, not 455; the employer pays 585 either way. Classifying the worker as private sector would over-deduct 65 a month from the employee.

```oa-check
name: ABSSB public service against private sector at 8,000 a month
inputs:
  pay: 8000
  ceiling: 6500
steps:
  - base: min(pay, ceiling)
  - public_employee: base * 0.06
  - private_employee: base * 0.07
  - employer: base * 0.09
  - public_total: public_employee + employer
  - over_deduction: private_employee - public_employee
expected:
  base: 6500
  public_employee: 390
  private_employee: 455
  employer: 585
  public_total: 975
  over_deduction: 65
```

## When to refuse or refer

- Self-employed contributions: only the 10% rate is confirmed; the base, ceiling and payment timing are not set out here.
- Multiple employers, irregular pay, expatriate cover, reciprocal agreements, benefit claims, penalties and payment arrangements: refer to the Board.
- Workers under 16 or past pensionable age at period edges: apply reg.4(5) and confirm with the Board if unclear.

## Filing and payment

1. Register the employer and each employee with the Board.
2. Each month deduct the employee share, add the employer share, and submit the remittance form with payment no later than 14 days after month end (reg.9).
3. Keep the official receipt and reconcile it to the payroll liability account; keep the Medical Benefits liability separate.

## Completion checklist

- Sector set (public service includes statutory boards).
- Every earnings component in the base; ceiling applied after.
- 7% and 9% private, 6% and 9% public.
- Age rules applied; remitted by the 14th.

## Sources

| Source | URL | Read on |
|---|---|---|
| SI 60 of 2016, Social Security (Collection of Contributions) (Amendment) Regulations: read (scanned, OCR) for the new regulation 4(5) week rule, the yearly rate schedule ending with the 2025 row (public 6% + 9% = 15%, private 7% + 9% = 16%) and the EC$1,500 weekly and EC$6,500 monthly maximum | https://socialsecurity.gov.ag/wp-content/uploads/2021/03/no-60-of-2016-collection-of-contributions-amendment.pdf | 2026-11-14 |
| SI 15 of 2013, Social Security (Collection of Contributions) Regulations: read (scanned, OCR, pages 3 to 9) for the public service definition (includes a statutory board), the regulation 4(2) earnings items and regulation 9, payment within fourteen days after month end, overpayments, short payments and assessment | https://socialsecurity.gov.ag/wp-content/uploads/2021/03/no-15-of-2013-collection-of-contributions-regulations.pdf | 2026-11-14 |
| ABSSB media release, 31 December 2024: read for the 2025 rates (15% public, 16% private), the self-employed rate staying at 10% and pensionable age 65 | https://socialsecurity.gov.ag/media-release-pension-contribution-rate-adjustments/ | 2026-11-14 |

Not yet confirmed: the self-employed contribution base, ceiling and payment date; the reg.4(2) provisos on delayed and set-aside payments (OCR text too noisy to quote); late payment penalties and interest; any 2026 change to the ceiling (none found on the Board's site).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ag-social-security` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ag-social-security. If neither is available, confirm every figure against the official source pages cited above before relying on it.
