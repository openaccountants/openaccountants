---
name: tn-payroll-social
description: "Tunisia payroll and social contributions for tax year 2026: job-loss fund, State relief on employer contributions for graduates hired from 2026, salary tax base and CNSS filing route. Use for questions on CNSS, retenue a la source on pay, or employer cost in Tunisia. The main CNSS percentages could not be checked at an official source and are marked unverified, so confirm them before use."
version: 1.1
jurisdiction: TN
category: payroll
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tunisia Payroll and Social Contributions v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Private-sector employers and employees in the CNSS general scheme. Tax year 2026. This skill has unverified contribution rates: CNSS pages hold no rate table that could be read.

## Rates, bands and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Employer contribution | unverified: 17.07% in the old file, 16.57% for industrial full exporters | 2026 | Includes the job-loss share | unverified |
| Employee contribution | unverified: 9.68% in the old file | 2026 | Includes the job-loss share | unverified |
| Work accident | unverified: 0.4% to 4%, employer | 2026 | By sector | unverified |
| Job-loss fund | 0.5% employer, 0.5% employee | 2026 | On payroll declared to CNSS. LF 2025 fund article | https://web.archive.org/web/20251205000847/https://jibaya.tn/wp-content/uploads/2024/12/Loi2024_48.pdf |
| State relief on employer share | 100%, 80%, 60%, 40%, 20% over years 1 to 5 | 2026 | Higher-education graduates hired by private firms from 1 Jan 2026. LF 2026 art. 13 | https://web.archive.org/web/20261005010006/https://jibaya.tn/wp-content/uploads/2025/12/Loi2025_17-1.pdf |
| Employee flat expenses | 10%, cap TND 2,000 | 2026 | Art. 26 I | https://web.archive.org/web/20250906073044/https://jibaya.tn/wp-content/uploads/2025/07/code-IS-et-IRPP-francais-1.pdf |
| Withholding exempt pay | Net annual pay up to TND 5,000 | 2026 | Art. 53; check art. text in the income skill | same |

LF 2026 art. 15 raises public and private pay for 2026 to 2028 by decree; the decree was not read.

## The base

Contribution base: unverified: old file says gross pay with most cash and in-kind benefits, no general ceiling. Taxable pay: gross less compulsory contributions, less flat expenses, then family deductions. Work transport for workers is outside tax from 2026 (LF 2026 art. 22).

## Deadlines and filing

Salary tax is withheld under art. 53 and paid with the monthly return: dates in the [VAT skill](tunisia-vat.md). The annual employer statement is form DEC-EMPL. CNSS: unverified quarterly declaration from the old file; online via the CNSS teleservice with ID-TRUST or DIGIGO certificate, or file upload without one (https://www.cnss.tn/dspc/Cotisants.html).

## Penalties and interest

Not confirmed.

## Cross-border points

Non-resident employees: see the income skill. Social security conventions: CNSS lists covered countries.

## Two worked examples that recompute

Simple: job-loss fund on payroll TND 10,000: 50 from each side.

```oa-check
name: Job-loss fund
inputs:
  payroll: 10000
steps:
  - each: payroll * 0.005
  - total: each * 2
expected:
  total: 100.00
```

Decision: hire a graduate at employer contribution of TND 3,000 a year (client's own figure). The State covers all in year 1 and 80% in year 2.

```oa-check
name: Graduate relief over two years
inputs:
  annual: 3000
steps:
  - y1: annual * 1.0
  - y2: annual * 0.8
  - saved: y1 + y2
expected:
  saved: 5400.00
```

## Ask the client first

1. Sector and full-exporter status?
2. Gross pay and benefits?
3. Hired after 1 January 2026, and a graduate?
4. Family status of the employee?

## Sources

| Source | URL | Read on |
|---|---|---|
| Loi n° 2025-17 du 12 decembre 2025, loi de finances 2026, JORT n° 148, archived copy of the DGI file; tax articles read | https://web.archive.org/web/20261005010006/https://jibaya.tn/wp-content/uploads/2025/12/Loi2025_17-1.pdf | 2026-11-01 |
| Loi n° 2024-48 du 9 decembre 2024, loi de finances 2025, archived copy of the DGI file; arts. 31, 64 and the job-loss fund article read | https://web.archive.org/web/20251205000847/https://jibaya.tn/wp-content/uploads/2024/12/Loi2024_48.pdf | 2026-11-01 |
| Code IRPP-IS, French text updated to LF 2025, archived copy of the DGI file; articles cited in this skill read. The 2026 edition page exists but its PDF could not be opened | https://web.archive.org/web/20250906073044/https://jibaya.tn/wp-content/uploads/2025/07/code-IS-et-IRPP-francais-1.pdf | 2026-11-01 |

Not yet confirmed: All CNSS rates above marked unverified, base, ceiling, remittance frequency, penalties. The law setting contribution rates was not found on an openable official page.

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
