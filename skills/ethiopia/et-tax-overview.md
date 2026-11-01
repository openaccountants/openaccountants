---
name: et-tax-overview
description: "Source-cited draft: tax overview for Ethiopia (tax year 2026) - rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
version: 0.2
jurisdiction: ET
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---


# Ethiopia Tax Overview

## Ethiopia tax system at a glance

Ethiopia operates a federal direct- and indirect-tax system administered by the Ministry of Revenues. The framework was substantially reformed in 2024-2025 by a new VAT Proclamation and an Income Tax Amendment Proclamation; the figures below reflect the post-reform position. This is an unverified draft for review by a licensed Ethiopia accountant.

- **Tax (budget) year** - 8 July to 7 July (Ethiopian fiscal year, Hamle 1 to Sene 30)  _(Income Tax Proclamation No. 979/2016)_
- **Currency** - Ethiopian Birr (ETB)  _(National Bank of Ethiopia Establishment Proclamation)_
- **Tax authority** - Ministry of Revenues (federal); Ethiopian Customs Commission for customs  _(Ministry of Revenues Establishment Regulation)_
- **Residence basis of taxation** - Residents taxed on worldwide income; non-residents taxed only on Ethiopian-source income  _(Income Tax Proclamation No. 979/2016 (as amended by No. 1395/2025))_
- **Top personal income tax rate** - 35%  _(Income Tax (Amendment) Proclamation No. 1395/2025)_
- **Standard corporate income tax rate** - 30%  _(Income Tax Proclamation No. 979/2016)_
- **Does VAT exist** - Yes - Value Added Tax at a standard rate of 15%  _(Value Added Tax Proclamation No. 1341/2024)_
- **Annual income tax return deadline (companies / Category A)** - Within 4 months of the end of the tax year (i.e. by 7 November for an 8 July–7 July year) _(Proc. 979/2016 art. 83(4))_
- **VAT return frequency and deadline** - Monthly, by the last day of the following calendar month (Proc. 1341/2024 art. 58) _(Value Added Tax Proclamation No. 1341/2024)_

## Two worked examples that recompute

Simple case: VAT at the standard 15% on a sale of ETB 100,000.

```oa-check
name: Standard VAT
inputs:
  v: 100000
steps:
  - vat: v * 0.15
expected:
  vat: 15000.00
```

Edge case: monthly employment income of ETB 30,000, in the top band of Proc. 1395/2025 art. 11.

```oa-check
name: Top band employment tax
inputs:
  s: 30000
steps:
  - lower: 300 + 600 + 750 + 1200
  - top: (s - 14000) * 0.35
  - tax: lower + top
expected:
  lower: 2850.00
  top: 5600.00
  tax: 8450.00
```

## Sources

| Source | URL | Read on | What was read |
|---|---|---|---|
| Income Tax (Amendment) Proclamation 1395/2025, Federal Negarit Gazette 31st Year No. 64 | https://www.hopr.gov.et/admin/Files/2026/4/8/5fc57d68-d0f6-4bf1-91b4-5b23abd0df72%E1%8C%88%E1%89%A2%20%E1%8C%8D%E1%89%A5%E1%88%AD%20%201395.pdf | 2026-11-01 | Whole text read (English column) |
| Federal Income Tax Proclamation 979/2016, Amharic consolidated print | https://www.lawethiopia.com/images/federal_proclamation/proclamations_by_number/979.pdf | 2026-11-01 | Declaration, payment, withholding and exemption articles read in Amharic; article numbers are those before the 1395/2025 renumbering |
| Value Added Tax Proclamation 1341/2024, Federal Negarit Gazette, 21 August 2024 | https://www.hopr.gov.et/Resources/ViewFiles?path=%2Fadmin%2FFiles%2F2026%5C1%5C21%5C237b0abc-d9d2-4749-96a8-7cf2ae7dbcf91341-2016%20%E1%8B%A8%E1%89%B0%E1%8C%A8%E1%88%9B%E1%88%AA%20%E1%8A%A5%E1%88%B4%E1%89%B5%20%E1%89%B3%E1%8A%AD%E1%88%B5%20%E1%8A%A0%E1%8B%8B%E1%8C%85.pdf | 2026-11-01 | Arts 2, 6, 8 to 13, 29, 30, 47 to 49, 58, 59, 62, 64 to 66, 71 to 75 read; the copy has no Schedules |
| Tax Administration (Amendment) Proclamation 1434/2026, Federal Negarit Gazette 32nd Year No. 48, 30 July 2026, listed by the Ministry of Revenues | https://www.mor.gov.et/domestic-law-proclamation | 2026-11-01 | Whole text read; adds 17 to the penalty article numbers of 983/2016 |

Not yet confirmed: the 30% company rate, covered in the corporate skill as unverified.

> **General reference only.** This document does not constitute tax, legal, or financial advice. Verify figures against the cited primary sources or with a licensed professional before relying on them.
