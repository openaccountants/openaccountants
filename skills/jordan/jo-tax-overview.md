---
name: jo-tax-overview
description: "Conditional overview of Jordan tax sources for a 2026 refresh. Routes individual income tax, company tax, General Sales Tax and social security questions to the existing detailed Jordan Guides. Gives source-text headline rates and calendar illustrations with the conditions in those Guides. All source-currentness and filing-procedure holds carry through to this overview. Includes two executable arithmetic examples for a standard company and an ordinary full-coverage employee. Use for Jordan tax overview research, taxes in Jordan, ISTD, social security and the Jordan tax calendar. Do not treat the target tax year as clearance of a current filing position."
version: 1.1
jurisdiction: JO
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Jordan Tax Overview

## Who this applies to

**Source currentness hold.** This is a source-cited research draft for the 2026 refresh, not a cleared filing instruction. The clause extracts below are conditional reference material. Before using them for a 2026 position, close the amendment and procedure gaps named in Sources. A read date records the stated read scope, not verification of every later amendment.

Income arising in Jordan is taxed wherever it is paid; a resident's foreign income is taxed only where it arises from funds or deposits from Jordan (art. 3). ISTD runs income tax and sales tax; the Social Security Corporation runs contributions. Currency is the Jordanian dinar (JOD).

## Rates, bands and thresholds

| Tax | Headline | Skill | Source |
|---|---|---|---|
| Personal income tax | 5% to 30% | [jo-income-tax](jo-income-tax.md) | https://www.istd.gov.jo/EBV4.0/Root_Storage/AR/EB_Tenders/%D9%82%D8%A7%D9%86%D9%88%D9%86_%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9_%D8%A7%D9%84%D8%AF%D8%AE%D9%84_34_%D9%84%D8%B3%D9%86%D8%A9_2014_%D9%88%D8%AA%D8%B9%D8%AF%D9%8A%D9%84%D8%A7%D8%AA%D9%87.docx |
| Company tax | 20%, 24%, 35% | [jo-corporate-income-tax](jo-corporate-income-tax.md) | same |
| National contribution | 1% to 7% for companies; 1% above JOD 200,000 for individuals | [jo-corporate-income-tax](jo-corporate-income-tax.md) | same |
| General Sales Tax | 16% standard | [jordan-gst](jordan-gst.md) | https://istd.gov.jo/EBV4.0/Root_Storage/AR/QRCODE/sales2.pdf |
| Social security | Employer 14.25%, employee 7.5% | [jo-payroll-social](jo-payroll-social.md) | https://www.ssc.gov.jo/wp-content/uploads/2025/02/law-26.1.2025-compressed.pdf |
| Income tax return | End of April for a calendar year | [jo-income-tax](jo-income-tax.md) | https://www.istd.gov.jo/EBV4.0/Root_Storage/AR/EB_Tenders/%D9%82%D8%A7%D9%86%D9%88%D9%86_%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9_%D8%A7%D9%84%D8%AF%D8%AE%D9%84_34_%D9%84%D8%B3%D9%86%D8%A9_2014_%D9%88%D8%AA%D8%B9%D8%AF%D9%8A%D9%84%D8%A7%D8%AA%D9%87.docx |

## The base

Each tax has its own base; see the linked skill.

## Deadlines and filing

Income tax returns are due by the end of the fourth month after the period. GST and contribution dates are in the linked skills.

## Penalties and interest

Late income tax and GST payment costs 0.4% per week or part of a week. Contributions carry 1% a month.

## Cross-border points

For non-exempt income due or paid to a non-resident, the art. 12(b) extract requires withholding at the earlier date; treaty relief is outside this draft. See [jo-corporate-income-tax](jo-corporate-income-tax.md).

## Two worked examples that recompute

Simple: a standard company with taxable income of JOD 50,000 pays 20% plus the 1% contribution.

```oa-check
name: Company, JOD 50,000
inputs:
  taxable: 50000
steps:
  - total: taxable * 0.21
expected:
  total: 10500.00
```

Edge: ordinary full-coverage worker subject to the ordinary ceiling, wage JOD 5,000, with no protected legacy wage, hazardous addition or approved reduction. The conditional employer-cost calculation uses JOD 3,733; see the coverage and currentness holds in [payroll](jo-payroll-social.md).

```oa-check
name: Employer cost above the ceiling
inputs:
  wage: 5000
steps:
  - employer: min(wage, 3733) * 0.1425
  - cost: wage + employer
expected:
  cost: 5531.95
```

## Ask the client first

- Individual or company.
- Resident or not.
- Sector and activity.
- Employees or none.
- Annual sales.

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Law No. 34 of 2014 as amended, ISTD consolidated text: inherited original-author reading of arts. 2, 3, 4 (part), 9 to 12, 17 to 19, 36; closeout reread cached clause output; normal refetch blocked | https://www.istd.gov.jo/EBV4.0/Root_Storage/AR/EB_Tenders/%D9%82%D8%A7%D9%86%D9%88%D9%86_%D8%B6%D8%B1%D9%8A%D8%A8%D8%A9_%D8%A7%D9%84%D8%AF%D8%AE%D9%84_34_%D9%84%D8%B3%D9%86%D8%A9_2014_%D9%88%D8%AA%D8%B9%D8%AF%D9%8A%D9%84%D8%A7%D8%AA%D9%87.docx | 2026-11-01 |
| General Sales Tax Law No. 6 of 1994 as amended, ISTD scan: inherited original-author OCR reading of rate, registration, return, deduction, refund and penalty clauses; closeout reread cached output, fresh scan unavailable | https://istd.gov.jo/EBV4.0/Root_Storage/AR/QRCODE/sales2.pdf | 2026-11-01 |
| Social Security Law No. 1 of 2014, SSC official translation through 16 Apr 2023: arts. 3-7, 19-24, 42-49, 59, 64 read; original Arabic source/pages recorded in closeout ledger | https://www.ssc.gov.jo/wp-content/uploads/2025/02/law-26.1.2025-compressed.pdf | 2026-11-01 |

Not yet confirmed: calendar tax year as the rule for all taxpayers; the dinar peg to the US dollar (no Central Bank of Jordan page read); amendments after the texts above. This overview inherits JO-IT-CURRENT, JO-GST-CURRENT and JO-SSC-CURRENT from the detailed Guides; its headline figures and examples are non-operative until the relevant hold closes.

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
