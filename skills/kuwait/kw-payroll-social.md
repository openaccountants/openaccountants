---
name: kw-payroll-social
description: "Payroll and social contributions in Kuwait for tax year 2026. Covers the absence of tax on individual income from work, Public Institution for Social Security contributions for Kuwaiti nationals, Gulf nationals, expatriates and end-of-service pay. Use for questions on Kuwait payroll, PIFSS, employer cost, salary tax, gratuity or indemnity. The contribution figures are marked unverified because the PIFSS rate pages could not be opened in this review, and the reader must confirm them with PIFSS before payroll runs. Not signed off by an accountant."
version: 0.2
jurisdiction: KW
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Kuwait Payroll and Social Contributions

Tax year 2026. Contribution figures below could not be read at source and are marked unverified. Confirm them with PIFSS before running payroll.

## Who this applies to

Employers in Kuwait. Social insurance applies to Kuwaiti nationals through PIFSS; Gulf nationals and expatriates are treated as shown.

## Rates, bands and thresholds

| Item | Figure and conditions | Tax year | Official URL |
|---|---|---|---|
| Tax on salaries | None: the income tax falls on corporate bodies and individuals are exempt (reg. arts. 1 and 8) | 2026 | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf |
| Employer contribution, Kuwaiti | unverified: 11.5% of monthly salary | 2026 | unverified |
| Employee basic contribution, Kuwaiti | unverified: 8% of monthly salary | 2026 | unverified |
| Additional employee contribution | unverified: 2.5%, making 10.5% in total | 2026 | unverified |
| Monthly salary ceiling | unverified: KWD 2,750 | 2026 | unverified |
| Expatriates (non-GCC) | unverified: outside PIFSS; employer owes end-of-service indemnity | 2026 | unverified |
| GCC nationals | unverified: home-state scheme through the GCC insurance extension | 2026 | unverified |
| Remittance deadline | unverified: by the 15th of the following month | 2026 | unverified |
| End-of-service indemnity | unverified: 15 days a year for the first 5 years, then one month a year, private sector | 2026 | unverified |

## The base

Unverified: contributions fall on monthly salary up to the ceiling above.

## Deadlines and filing

PIFSS runs employer forms and services under the employer tab at https://www.pifss.gov.kw. Steps for the monthly remittance could not be read and are not given here.

## Penalties and interest

Not confirmed; see Sources.

## Cross-border points

Foreign employees pay no Kuwaiti tax on salary. Their home state's tax is a separate question.

## Two worked examples that recompute

Both use the unverified figures above and must be rerun if PIFSS shows otherwise.

**Example 1.** Kuwaiti employee on KWD 2,000: employer KWD 230, employee KWD 210.

```oa-check
name: Kuwaiti employee KWD 2,000, unverified rates
inputs:
  salary: 2000
steps:
  - base: min(salary, 2750)
  - employer: base * 0.115
  - employee: base * 0.105
expected:
  employer: 230.00
  employee: 210.00
```

**Example 2 (decision).** Hire a Kuwaiti on KWD 3,000 or a non-GCC expatriate on the same pay. The Kuwaiti costs KWD 316.25 a month in employer contributions at the ceiling; the expatriate costs none but accrues indemnity, 15 days a year in the first five years.

```oa-check
name: Employer contribution above the ceiling, unverified rates
inputs:
  salary: 3000
steps:
  - base: min(salary, 2750)
  - employer: base * 0.115
expected:
  base: 2750.00
  employer: 316.25
```

## Ask the client first

- Nationality of each employee: Kuwaiti, GCC or other?
- Monthly salary and allowances?
- Private or public sector?
- Length of service for indemnity?

## Sources

| Source | URL | Read on |
|---|---|---|
| Executive Regulations of Law 2 of 2008, Ministerial Resolution 29 of 2008, arts. 1 to 3, 8 to 14, 19, 20, 24 to 28, 34, 37 to 39, 41, 42, 46; all 23 pages read in Arabic by OCR, art. 9 by page image | https://www.mof.gov.kw/Desicions/Decree/PDF/la2-2008.pdf | 2026-11-01 |

Not yet confirmed: All PIFSS figures: only the PIFSS home page opened on 2026-11-01 and it carries no rates; Social Security Law 61 of 1976 not read. Labour Law 6 of 2010 indemnity and its caps not read; manpower.gov.kw did not open. Secondary payroll sites disagree on the employee rate, and were not used. Any 2026 change to the ceiling and any employer unemployment contribution. PIFSS late-payment penalties.

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
