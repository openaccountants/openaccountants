---
name: ky-payroll-social
description: "Cayman Islands employer payroll for 2026. No income tax, no PAYE and no state social security; the employer's legal payroll costs are the private pension under the National Pensions Act (employer at least 5%, employee up to 5%, on earnings to CI$87,000 a year, paid by the 15th of the next month; self-employed 10%), standard health insurance (employer pays, may recover at most 50% of the premium), the national minimum wage of CI$8.75 an hour from 1 January 2026, and work permit fees for non-Caymanians. Trigger on Cayman payroll, Cayman pension contributions, National Pensions Act, Cayman health insurance employer, Cayman minimum wage. Built from Cayman legislation; not reviewed by an accountant."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ky-payroll-social"
  jurisdiction: "KY"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Cayman Islands payroll: pensions, health insurance and minimum wage

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employers in the Cayman Islands in 2026, and self-employed persons. Amounts are CI$. The Department of Labour and Pensions supervises pensions and labour standards.

There is no income tax, so no PAYE is withheld, and there is no government social security contribution. The legal payroll costs are pension contributions to an approved private plan, health insurance premiums, and work permit fees for non-Caymanian staff.

## Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
|---|---|---|---|
| Who must be in a pension plan | All employees aged 18 to the normal pension age of 65 | s. 25(1); s. 2 for age 65 | National Pensions Act (2024 Revision): https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1996/1996-0010/1996-0010_2024%20Revision.pdf |
| Exception | Non-Caymanian, non-permanent-resident employees working in the Islands for a continuous period of nine months or less, and household domestics | s. 25(2); the 2016 change to six months has not commenced | same |
| Employer contribution, defined contribution plan | At least 5% of earnings | Up to the year's maximum pensionable earnings, s. 47(3)(b) | same |
| Employee contribution | Not more than 5% without consent | If the employer pays more than 5%, the employee pays only what brings the total to 10%, s. 47(3)(a), (c) | same |
| Year's maximum pensionable earnings | eighty-seven thousand dollars (CI$) | Or another amount prescribed; s. 2 definition | same |
| Self-employed | 10% of earnings to the year's maximum | s. 47(2) | same |
| Contribution date deadline | 15th day of the month after the month of service | Regardless of pay period, s. 48(2) | same |
| Health insurance, employee recovery | Employer may recover not more than fifty per cent of the premium | Standard health insurance contract, s. 7 | Health Insurance Act (2021 Revision): https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1997/1997-0015/1997-0015_2021%20Revision.pdf |
| National minimum basic wage | CI$8.75 an hour | From 1 January 2026 (was CI$6) | Labour (National Minimum Basic Wage) (Amendment) Order 2025, SL 60 of 2025: https://legislation.gov.ky/cms/images/LEGISLATION/AMENDING/2025/2025-0060S/2025-0060S.pdf |
| Minimum wage, gratuity-earning employees | CI$6.56 an hour | From 1 January 2026 (was CI$4.50) | same |
| Benefits counted towards minimum wage | No more than CI$2.19 an hour | Para 3(1) and (2), from 1 January 2026 (was CI$1.50) | same |
| Income tax withheld | None | No income tax Act | Cayman legislation, current by title: https://legislation.gov.ky/cms/legislation/current/by-title.html |

## The base

1. Pensionable earnings: the employee's earnings for the month, with the annual total capped at CI$87,000.
2. Employer pays at least 5%; deducts the employee's 5% (unless the employer pays more).
3. Remit both to the employee's approved pension plan by the 15th of the next month.
4. Health insurance: the employer pays the premium for each employee and may deduct up to half of it from pay (more rules for high-risk persons and dependants under s. 7 and 8).
5. Minimum wage: check that hourly pay is at least CI$8.75 (CI$6.56 for gratuity-earning staff).

## Deadlines and filing

| Obligation | When |
|---|---|
| Pension contributions | By the 15th of the month after the month worked ("contribution date deadline") |
| Delinquent contribution report by the administrator to the Director | If unpaid by the 15th of the following month; notice to the Director by the 20th |

## Penalties and interest

- A contribution not received by the contribution date deadline is delinquent; the plan administrator must collect it with interest and report it to the Director (s. 48(3) to (6)).
- Offences under the Act carry fines on summary conviction (for example CI$20,000 or two years' imprisonment for some offences); refer enforcement matters.

## Cross-border points

- Non-Caymanian staff need work permits; fees vary by occupation (not confirmed here).
- Non-Caymanian, non-permanent-resident staff are outside the pension requirement for their first nine months of continuous work.

## Two worked examples that recompute

### Employee at CI$60,000 a year

```oa-check
name: KY pension employee 60000, 2026
inputs:
  salary: 60000
  cap: 87000
steps:
  - pensionable: min(salary, cap)
  - employer: pensionable * 0.05
  - employee: pensionable * 0.05
  - total: employer + employee
  - monthly_total: total / 12
expected:
  employer: 3000
  employee: 3000
  total: 6000
  monthly_total: 500
```

CI$500 a month is remitted by the 15th of the next month. No income tax is deducted.

### Decision: senior hire at CI$120,000, employer pays more than 5%?

The salary is above the cap, so contributions stop at CI$87,000. If the employer chooses to pay 7%, the employee only pays 3%.

```oa-check
name: KY pension above cap, employer 5% vs 7%
inputs:
  salary: 120000
  cap: 87000
steps:
  - pensionable: min(salary, cap)
  - standard_employer: pensionable * 0.05
  - standard_employee: pensionable * 0.05
  - enhanced_employer: pensionable * 0.07
  - enhanced_employee: pensionable * 0.10 - enhanced_employer
  - extra_employer_cost: enhanced_employer - standard_employer
expected:
  pensionable: 87000
  standard_employer: 4350
  standard_employee: 4350
  enhanced_employer: 6090
  enhanced_employee: 2610
  extra_employer_cost: 1740
```

The enhanced deal costs the employer CI$1,740 more and gives the employee CI$1,740 more take-home pay; the total going into the plan stays CI$8,700.

## Ask the client first

1. Each employee's age, salary, and whether Caymanian, permanent resident or on a work permit (and since when).
2. Is anyone a household domestic?
3. Which approved pension plan, and does the employer pay more than 5%?
4. Health insurance premium per employee, and how much is deducted from pay?
5. Hourly rates for the lowest paid staff, and do any earn gratuities?

## Sources

| Source | URL | Read on |
|---|---|---|
| National Pensions Act (2024 Revision): read for ss. 2, 25, 47 and 48 (membership, 9-month exception, 5% and 10% rates, eighty-seven thousand dollars maximum, 15th day deadline, delinquent contributions) | https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1996/1996-0010/1996-0010_2024%20Revision.pdf | 2026-11-14 |
| Health Insurance Act (2021 Revision): read for s. 7, the employer's right to recover at most fifty per cent of the premium | https://legislation.gov.ky/cms/images/LEGISLATION/PRINCIPAL/1997/1997-0015/1997-0015_2021%20Revision.pdf | 2026-11-14 |
| Labour (National Minimum Basic Wage) (Amendment) Order 2025, SL 60 of 2025: read for CI$8.75, CI$6.56 and CI$2.19 from 1 January 2026 | https://legislation.gov.ky/cms/images/LEGISLATION/AMENDING/2025/2025-0060S/2025-0060S.pdf | 2026-11-14 |
| Cayman legislation, current by title: read to confirm no income tax or social security Act | https://legislation.gov.ky/cms/legislation/current/by-title.html | 2026-11-14 |

Not yet confirmed: work permit fee amounts; whether any regulation prescribes a different maximum pensionable earnings figure than CI$87,000 (none found); the standard health insurance premium amounts; the Health Insurance Act amendments listed for 2026 (the linked file was a different regulation).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ky-payroll-social` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ky-payroll-social. If neither is available, confirm every figure against the official source pages cited above before relying on it.
