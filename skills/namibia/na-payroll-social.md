---
name: na-payroll-social
description: >
  Namibia payroll, 2026: PAYE, the Social Security ceiling of N$12,500 from 1 March 2026, new benefits from 1 October 2026, VET levy and year-end certificates. Figures come from Namibian law and official pages opened on 2026-11-01. Items that could not be opened are named as not yet confirmed. Not reviewed by a licensed accountant.
version: 0.2
jurisdiction: NA
category: international
tax_year: 2026
tax_year_notes: "Individuals: year of assessment 1 March 2026 to 28 February 2027. Companies: financial year."
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Namibia Payroll and Social Contributions v0.2

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. Do not rely on it to file, pay or take a position without review by a qualified professional in Namibia.

## Who this applies to

Employers in Namibia and their employees. A new employer registers with NamRA within 14 days ([NamRA](https://www.namra.org.na/tax-types/page/employee-tax-30120-30120/)) and with the Social Security Commission on form 1 (https://www.ssc.org.na). A self-employed person registered with the Commission pays both shares (Social Security Act s.21(5)).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| PAYE | Scale in the [income tax skill](na-income-tax.md) | 2026 | https://www.namra.org.na/tax-types/page/employee-tax-30120-30120/ |
| SSC deemed basic wage floor | N$500 a month | 2026 | https://www.lac.org.na/laws/2026/8975.pdf |
| SSC maximum basic wage | N$12,500 from 1 March 2026 | 2026 | https://www.lac.org.na/laws/2026/8975.pdf |
| Same, next steps | N$14,000 from 1 March 2027; N$15,000 from 1 March 2028; N$16,000 from 1 March 2029 | 2027-29 | same |
| SSC contribution rate | unverified: old skill 0.9% each side; the regulation was not opened | 2026 | unverified |
| Maternity benefit from 1 October 2026 | 100% of basic wage, N$20,000 a month maximum, 12 weeks | 2026 | https://www.lac.org.na/laws/2026/9037.pdf |
| Sick leave from 1 October 2026 | 75% up to N$15,000 for 12 months; then 65% up to N$13,000 | 2026 | same |
| Death benefit from 1 October 2026 | N$15,000 lump sum | 2026 | same |
| VET levy | 1% of annual payroll, payroll N$1,000,000 or more | Levy notice 2014, still on NTA page | https://www.nta.com.na/vet-levy/ |

The ceiling table labels N$12,500 as financial year 2025/2026 with effect from 1 March 2026; the notice was gazetted on 15 July 2026 with retroactive effect.

## The base

PAYE: remuneration. SSC: basic wage, between floor and maximum. VET levy: payroll as total remuneration ([NTA](https://www.nta.com.na/vet-levy/)).

## Deadlines and filing

PAYE and employer return: within 20 days after month end (Sch 2 para 2, s.80(2)). PAYE 5 certificates: within 30 days after end of February; within 14 days when an employee leaves; within 7 days if the employer ceases. Annual reconciliation return: within 30 days of 28 February ([NamRA](https://www.namra.org.na/tax-types/page/employee-tax-30120-30120/)). SSC: pay both shares in the prescribed period with a return (Act ss.21(4), 22(3)); records kept 5 years. VET levy: register with the NTA, send the monthly Payroll Return Form, pay by the 20th of the next month. No agreement can waive PAYE deduction.

## Penalties and interest

PAYE: penalty 10% and interest 20% on late payment, limited to the unpaid tax ([NamRA](https://www.namra.org.na/tax-types/page/employee-tax-30120-30120/)). SSC: arrears carry prescribed interest (s.24); non-payment is an offence with a fine up to N$8,000 or imprisonment (s.23).

## Cross-border points

Non-resident directors' fees: 25% final withholding, see the [cross-border skill](na-cross-border.md).

## Two worked examples that recompute

Example 1. Salary N$240,000 a year: N$9,000 + 25% of N$90,000 = N$31,500, or N$2,625 a month.

```oa-check
name: Monthly PAYE
inputs:
  a: 240000
steps:
  - tax: 9000 + (a - 150000) * 0.25
  - m: tax / 12
expected:
  m: 2625.00
```

Example 2. A decision: does the VET levy apply? Payroll N$1,200,000 passes N$1,000,000: N$12,000 a year, N$1,000 a month. A wage of N$20,000 counts as N$12,500 for SSC.

```oa-check
name: VET and SSC wage
inputs:
  p: 1200000
  w: 20000
steps:
  - levy: p * 0.01
  - m: levy / 12
  - ssc: min(w, 12500)
expected:
  m: 1000.00
  ssc: 12500.00
```

## Ask the client first

1. Number of employees and annual payroll?
2. Wages above the SSC maximum?
3. Registered with NamRA, SSC and NTA?
4. Domestic employees (form 2)?
5. Non-resident directors?

## Sources

| Source | URL | Read on |
|---|---|---|
| Government Gazette 8975 GN 236 (read: notice and table) | https://www.lac.org.na/laws/2026/8975.pdf | 2026-11-01 |
| Government Gazette 9037 GN 305 (read: notice) | https://www.lac.org.na/laws/2026/9037.pdf | 2026-11-01 |
| Social Security Act 34 of 1994 (read: ss.20-24) | https://www.lac.org.na/laws/annoSTAT/Social%20Security%20Act%2034%20of%201994.pdf | 2026-11-01 |
| Income Tax Act 24 of 1981, annotated to Act 4 of 2024 (read: s.80, Schedule 2) | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf | 2026-11-01 |
| NamRA employee tax page (read: whole page) | https://www.namra.org.na/tax-types/page/employee-tax-30120-30120/ | 2026-11-01 |
| NTA VET levy page (read: whole page) | https://www.nta.com.na/vet-levy/ | 2026-11-01 |
| SSC site (read: home page and forms 1 to 4) | https://www.ssc.org.na | 2026-11-01 |

Not yet confirmed: SSC contribution rate of 0.9% each side and period of 30 days after the month (old skill; Regulations GN 198 of 1995 not opened); Employees Compensation Fund rates and ceiling (ECF page opened gave no figures; the N$ rates are unverified); PAYE tables for 2026.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
