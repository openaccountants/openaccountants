---
name: jm-payroll-social
description: >
  Jamaica employer payroll for 2026, PAYE income tax and the statutory
  contributions an employer deducts and pays (NIS, NHT, Education Tax) plus the
  employer-only HEART contribution. Gives the monthly threshold of J$149,948 to
  March 2026 and J$158,530 from April 2026, the J$500,000 monthly break for 30%,
  the rates and bases, the S01 monthly remittance by the 14th and the S02 annual
  return by 31 March, and the late-payment charges. Trigger on Jamaica payroll,
  PAYE Jamaica, S01, S02, statutory deductions, NIS, NHT, Education Tax, HEART
  levy, TAJ employer. Built from Tax Administration Jamaica publications; not
  reviewed by an accountant.
version: 1.0
jurisdiction: JM
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: payroll
tier: 2
domain: payroll
type: computation
---

# Jamaica Payroll and Social Contributions v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Employers in Jamaica paying emoluments in 2026, and their employees. The authority is Tax Administration Jamaica (TAJ), which collects PAYE, NIS, NHT, Education Tax and HEART together. Amounts are Jamaican dollars (J$).

- **In:** employers of resident employees; the monthly computation of each deduction; remittance and the annual return.
- **Out:** the employee's own annual return and the self-employed contribution rates (use `jm-income-tax`); benefit-in-kind valuation tables beyond what is stated here; pension scheme approval.

Definitions TAJ uses: **gross emoluments** are all income from employment, in cash or kind (salary, wages, fees, allowances, benefits). **Statutory income** is gross emoluments less allowable deductions (NIS, approved pension fund or retirement scheme, Employee Share Ownership Plan purchases) and exemptions (age, pension, disability).

## Rates, bands and thresholds

| Item | Employee | Employer | Base and conditions | Source |
|---|---|---|---|---|
| NIS | 3% | 3% | Gross emoluments not exceeding J$5,000,000 a year (5,000,000/12 a month, which TAJ prints as J$416,666.66, so at most J$12,500 a month each side) | TAJ, payroll taxes and statutory contributions (April 2025 edition): https://www.jamaicatax.gov.jm/documents/10194/53547865/Payroll+Taxes+and+Statutory+Contributions+%28Employee+Employer%29.pdf/bef9095b-fb2d-db4a-5de4-b19405bd8631 |
| NHT | 2% | 3% | Gross emoluments, no ceiling | same |
| Education Tax | 2.25% | 3.5% | Statutory income | same |
| HEART | none | 3% | Gross emoluments, where the employer's payroll exceeds J$173,328 a year (one twelfth a month, computed) | same |
| PAYE, threshold 1 January to 31 March 2026 | J$149,948 a month at 0% | n/a | Annual rate J$1,799,376 | same |
| PAYE, threshold from 1 April 2026 | J$158,530 a month at 0% | n/a | Annual rate J$1,902,360 | same |
| PAYE rate, above the threshold | 25% | n/a | Statutory income above the threshold up to J$500,000 a month (J$6M a year) | TAJ, rates, threshold and exemptions 2013 to 2028: https://www.jamaicatax.gov.jm/documents/10194/15307403/INDIVIDUAL_INCOME_TAX_RATES_THRESHOLD_AND_EXEMPTIONS_2013-2028.pdf/c0987986-f35c-7106-85a4-d488a6f52627 |
| PAYE rate, top | 30% | n/a | Statutory income above J$500,000 a month (J$6M a year) | same |
| Effective 2026 annual threshold | J$1,876,614 | n/a | For the annual true-up | same |
| Monthly remittance (S01) | n/a | due | Within 14 days after the end of the month of deduction (by the 14th) | TAJ, employer's guide (December 2019): https://www.jamaicatax.gov.jm/documents/10194/14559577/Employers_guide_13122019.pdf/9d09b82e-e215-6aaa-72c8-7b8a3dd7f061 |
| Annual return (S02) | n/a | due | 31 March of the following year, online | same |
| Late PAYE remittance | n/a | 50% a year increase | Income Tax Act s. 41(2)(a), from the day after the due date | same |
| Late S02 | n/a | J$5,000 a month or part | While the return is outstanding | same |
| Interest on late NHT and NIS | n/a | 20% | As the guide's table states | same |

The 30% band starts at J$500,000 of monthly statutory income, not J$500,000 above the threshold.

### Monthly formula

```
NIS (employee)      = 3% x min(gross, 416,666.67)       ; employer the same
statutory income SI = gross - NIS - approved pension - other allowable deductions
Education Tax       = 2.25% x SI (employee), 3.5% x SI (employer)
NHT                 = 2% x gross (employee), 3% x gross (employer)
PAYE                = 25% x (min(SI, 500,000) - monthly threshold, not below 0)
                    + 30% x (SI - 500,000, not below 0)
HEART (employer)    = 3% x gross, if the monthly wage bill exceeds 14,444
net pay             = gross - pension - NIS - Education Tax - NHT - PAYE
```

## The base

- **Gross emoluments** include cash and benefits in kind. A loan to an employee at below the rate the Minister determines is a taxable benefit: the difference between interest at the determined rate (up to a maximum of 9%) and the concessionary interest (TAJ employer's guide).
- **Statutory income** is the base for PAYE and Education Tax. NIS paid and approved pension contributions come off first.
- **NHT and HEART** use gross emoluments.
- **Employer contributions** (NIS, NHT, Education Tax, HEART) are business costs of the employer and are not deducted from pay.
- **Education Tax has no threshold**: an employee under the income tax threshold still pays it.
- **Earlier version's HEART condition** ("3 or more employees") is replaced by TAJ's payroll-cost test above.

## Deadlines and filing

| Step | Form | When |
|---|---|---|
| 1 | Register as an employer (TRN branch extension for payroll) | Before the first payroll |
| 2 | Deduct PAYE, NIS, NHT and Education Tax each pay period | Each pay day |
| 3 | S01, employer's monthly remittance of deductions, with payment | By the 14th of the following month |
| 4 | S02, employer's annual return of gross emoluments and deductions, online | 31 March 2027 for 2026 |

Payment online through the TAJ portal or Direct Funds Transfer, or at a tax office.

## Penalties and interest

- **PAYE paid late** is increased at 50% a year from the day after it was due (Income Tax Act s. 41(2)(a)). Where the employer did not deduct, the Commissioner General may set a rate up to 50% a year (s. 41(2)(b)). Only the Minister of Finance can remit PAYE.
- **Interest** under Income Tax Act s. 79(1)(b) runs from the day after the collection date to payment, at a rate the Minister prescribes by order; the 2019 guide shows 16.62681% a year for PAYE and Education Tax, charged on principal plus penalty. The 2026 rate is not confirmed.
- **NHT and NIS** late: 20% interest, no penalty (2019 guide).
- **S02 late:** J$5,000 for each month or part month outstanding.

## Cross-border points

- A non-resident employee is not entitled to the threshold (see `jm-income-tax`); PAYE at 25% from the first dollar unless a treaty applies.
- Jamaican nationals employed by embassies or overseas employers are treated as self-employed and account for their own taxes and contributions (see `jm-income-tax`).

## Two worked examples that recompute

### Example 1: April 2026 pay, gross J$500,000, no pension

NIS 3% capped at J$12,500. Statutory income J$487,500. Education Tax J$10,968.75. NHT J$10,000. PAYE 25% of (J$487,500 - J$158,530) = J$82,242.50. Employer: NIS J$12,500, NHT J$15,000, Education Tax 3.5% of J$487,500 = J$17,062.50, HEART J$15,000.

```oa-check
name: JM April 2026 monthly payroll, gross 500k
inputs:
  gross: 500000
  threshold: 158530
steps:
  - nis: min(gross * 0.03, 12500)
  - si: gross - nis
  - ed_tax: si * 0.0225
  - nht: gross * 0.02
  - paye: max(min(si, 500000) - threshold, 0) * 0.25 + max(si - 500000, 0) * 0.30
  - net_pay: gross - nis - ed_tax - nht - paye
  - employer_cost: nis + gross * 0.03 + si * 0.035 + gross * 0.03
expected:
  nis: 12500
  si: 487500
  ed_tax: 10968.75
  nht: 10000
  paye: 82242.50
  net_pay: 384288.75
  employer_cost: 59562.50
```

### Example 2: Should an employee on J$900,000 a month put 10% into an approved scheme?

Without the contribution, statutory income is J$887,500 and PAYE J$201,617.50. With J$90,000 to an approved scheme, statutory income is J$797,500 and PAYE J$174,617.50. PAYE falls by J$27,000, which is 30% of the contribution, because the whole contribution comes off income taxed at the top rate.

```oa-check
name: JM April 2026, approved pension 10% or not, gross 900k
inputs:
  gross: 900000
  pension: 90000
  threshold: 158530
steps:
  - nis: min(gross * 0.03, 12500)
  - si_without: gross - nis
  - paye_without: max(min(si_without, 500000) - threshold, 0) * 0.25 + max(si_without - 500000, 0) * 0.30
  - si_with: gross - nis - pension
  - paye_with: max(min(si_with, 500000) - threshold, 0) * 0.25 + max(si_with - 500000, 0) * 0.30
  - saving: paye_without - paye_with
expected:
  si_without: 887500
  paye_without: 201617.50
  si_with: 797500
  paye_with: 174617.50
  saving: 27000
```

## Ask the client first

1. What is the pay period and the date paid (before or after 1 April 2026 decides the monthly threshold)?
2. Gross emoluments for each employee, including benefits in kind and employee loans.
3. Approved pension or retirement scheme contributions, and any age, pension or disability exemption.
4. Is any employee non-resident?
5. What is the total monthly wage bill (HEART test)?
6. Were earlier S01 remittances and the last S02 filed and paid on time?

## Sources

| Source | URL | Read on |
|---|---|---|
| TAJ, payroll taxes and statutory contributions, employee and employer (April 2025 edition): read for the rates and bases table, the HEART payroll test, the threshold steps and monthly amounts for 2024 to 2027 and the worked scenarios | https://www.jamaicatax.gov.jm/documents/10194/53547865/Payroll+Taxes+and+Statutory+Contributions+%28Employee+Employer%29.pdf/bef9095b-fb2d-db4a-5de4-b19405bd8631 | 2026-11-14 |
| TAJ, payroll taxes and contribution rates (December 2025 upload of the earlier edition): read for the same rates table; its threshold table stops at 2025 and was not relied on for 2026 | https://www.jamaicatax.gov.jm/documents/10194/105112/Pay+Roll+Taxes+and+Contribution+Rates-Employer+and+Employees_Dec2025.pdf/1d5554a1-b0e6-13bd-d16b-073c8216b753 | 2026-11-14 |
| TAJ, individual income tax rates, threshold and exemptions 2013 to 2028: read for the 25% and 30% rates, the J$500,000 monthly break and the effective 2026 threshold | https://www.jamaicatax.gov.jm/documents/10194/15307403/INDIVIDUAL_INCOME_TAX_RATES_THRESHOLD_AND_EXEMPTIONS_2013-2028.pdf/c0987986-f35c-7106-85a4-d488a6f52627 | 2026-11-14 |
| TAJ, employer's guide (13 December 2019): read for S01 and S02 due dates, Income Tax Act ss. 41 and 79 charges, the late-payment table, the S02 penalty and the employee loan benefit | https://www.jamaicatax.gov.jm/documents/10194/14559577/Employers_guide_13122019.pdf/9d09b82e-e215-6aaa-72c8-7b8a3dd7f061 | 2026-11-14 |
| TAJ, income tax and statutory contributions for self-employed individuals (updated November 2026): read for the HEART monthly wage bill of J$14,444 | https://www.jamaicatax.gov.jm/documents/10194/20399532/4-Income+Tax+and+Self+Employed+Individuals++%28+Updated+Nov.+2026+%29.pdf/c4f3878c-7a44-0a3b-d4a2-4a8cbef3f9ef | 2026-11-14 |

Not yet confirmed: the interest rate the Minister prescribes for late PAYE and Education Tax in 2026 (the 2019 guide shows 16.62681%); whether the 20% NHT and NIS interest is unchanged for 2026; the earlier version's employer annual return IT06 due 14 January (not found on TAJ pages read; TAJ names S02 by 31 March); benefit-in-kind valuation tables other than the employee loan rule; the NIS rules for employees over the deemed retirement age.
