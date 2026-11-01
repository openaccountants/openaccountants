---
name: et-company-formation
description: "Source-cited draft: company formation & entity choice for Ethiopia (tax year 2026) - rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
version: 0.2
jurisdiction: ET
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---


# Ethiopia Company Formation & Entity Choice

## Entity types, capital and incorporation

- **Incorporation overview** - The most common vehicle is the Private Limited Company (PLC) under the 2021 Commercial Code, including a one-member PLC. Incorporation runs through name reservation, notarised constitutive documents, TIN registration, commercial registration and a business licence.
- **Common entity types** - Private Limited Company (PLC), One-Member PLC, Share Company (S.C.), branch of a foreign company, sole proprietorship, partnership  _(Commercial Code of Ethiopia Proclamation No. 1243/2021 (unverified))_
- **PLC membership limits** - Minimum 1 (one-member PLC) or 2 members; maximum 50 members  _(Commercial Code of Ethiopia Proclamation No. 1243/2021 (unverified))_
- **PLC minimum capital** - ETB 15,000, fully subscribed and paid up at incorporation  _(Commercial Code of Ethiopia Proclamation No. 1243/2021 (unverified))_
- **Share Company minimum capital** - ETB 50,000 with a minimum of 5 shareholders (unverified) _(Commercial Code of Ethiopia Proclamation No. 1243/2021 (unverified))_
- **Minimum capital for foreign investors** - Generally USD 200,000 per investment project (USD 150,000 for joint ventures); lower thresholds for certain sectors (unverified) _(Investment Proclamation No. 1180/2020 and Investment Regulation (unverified))_
- **Step 1 - Name reservation** - Reserve a company name (submit several options); approval reserves the name for ~30 days  _(Commercial Registration and Business Licensing Proclamation (unverified))_
- **Step 2 - Constitutive documents** - Prepare and notarise the Memorandum of Association (MOA) and Articles of Association (AOA), in Amharic or English  _(Commercial Code of Ethiopia Proclamation No. 1243/2021 (unverified))_
- **Step 3 - Tax Identification Number** - Obtain a Taxpayer Identification Number (TIN) from the Ministry of Revenues  _(Tax Administration Proclamation No. 983/2016 (unverified))_
- **Step 4 - Commercial registration and licence** - File for commercial registration and obtain a business licence specifying authorised activities (Ministry of Trade and Regional Integration or Ethiopian Investment Commission for foreign investors)  _(Commercial Registration and Business Licensing Proclamation (unverified))_
- **Typical incorporation timeline** - Roughly 2–4 weeks for a domestic PLC once documents are ready (unverified) _(Commercial Registration and Business Licensing Proclamation (unverified))_
- **Core annual compliance** - Annual business-licence renewal, annual income tax return within 4 months of year-end, monthly VAT and payroll filings, and statutory bookkeeping  _(Commercial Registration and Business Licensing Proclamation; Tax Administration Proclamation No. 983/2016 (unverified))_

## Two worked examples that recompute

Simple case: a new company with sales of ETB 180,000 a month passes the ETB 2,000,000 VAT registration threshold over 12 months (Proc. 1341/2024 art. 12).

```oa-check
name: VAT registration test
inputs:
  m: 180000
steps:
  - annual: m * 12
  - over: annual - 2000000
expected:
  annual: 2160000.00
  over: 160000.00
```

Edge case: the first employee at a salary of ETB 10,000 a month, employer pension 11% (Proc. 1268/2022 art. 10).

```oa-check
name: First employee cost
inputs:
  s: 10000
steps:
  - pension: s * 0.11
  - cost: s + pension
expected:
  pension: 1100.00
  cost: 11100.00
```

## Sources

| Source | URL | Read on | What was read |
|---|---|---|---|
| Federal Income Tax Proclamation 979/2016, Amharic consolidated print | https://www.lawethiopia.com/images/federal_proclamation/proclamations_by_number/979.pdf | 2026-11-01 | Declaration, payment, withholding and exemption articles read in Amharic; article numbers are those before the 1395/2025 renumbering |
| Federal Tax Administration Proclamation 983/2016, Amharic consolidated print | https://www.lawethiopia.com/images/federal_proclamation/proclamations_by_number/983.pdf | 2026-11-01 | Penalty articles and art. 37 read in Amharic |
| Value Added Tax Proclamation 1341/2024, Federal Negarit Gazette, 21 August 2024 | https://www.hopr.gov.et/Resources/ViewFiles?path=%2Fadmin%2FFiles%2F2026%5C1%5C21%5C237b0abc-d9d2-4749-96a8-7cf2ae7dbcf91341-2016%20%E1%8B%A8%E1%89%B0%E1%8C%A8%E1%88%9B%E1%88%AA%20%E1%8A%A5%E1%88%B4%E1%89%B5%20%E1%89%B3%E1%8A%AD%E1%88%B5%20%E1%8A%A0%E1%8B%8B%E1%8C%85.pdf | 2026-11-01 | Arts 2, 6, 8 to 13, 29, 30, 47 to 49, 58, 59, 62, 64 to 66, 71 to 75 read; the copy has no Schedules |
| Private Organization Employees Pension Proclamation 1268/2022 | https://www.hopr.gov.et/Resources/ViewFiles?path=%2Fadmin%2FFiles%2F2026%2F2%2F25%2Ffc53f560-b228-4314-b372-da2b26ef4b53_Upploads_04012023090127_%E1%8B%A8%E1%8C%8D%E1%88%8D%20%E1%8B%B5%E1%88%AD%E1%8C%85%E1%89%B5%20%E1%88%A0%E1%88%AB%E1%89%B0%E1%8A%9E%E1%89%BD%20%E1%8C%A1%E1%88%A8%E1%89%B3%20%E1%8A%A0%E1%8B%8B%E1%8C%85%20%E1%89%81%E1%8C%A5%E1%88%AD%201268%20(1).pdf | 2026-11-01 | Arts 2, 10 to 12 read |

Not yet confirmed: every company law figure and step above: the Commercial Code 1243/2021 and the registration and investment rules were not opened, so each stays unverified.

> **General reference only.** This document does not constitute tax, legal, or financial advice. Verify figures against the cited primary sources or with a licensed professional before relying on them.
