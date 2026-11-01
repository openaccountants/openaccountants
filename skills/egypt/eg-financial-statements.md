---
name: eg-financial-statements
description: Use this skill whenever asked about Egyptian financial statements, financial reporting, or the accounting standards an Egyptian business must follow. Trigger on phrases like "Egypt financial statements", "Egyptian Accounting Standards", "EAS", "القوائم المالية", "المعايير المحاسبية المصرية", "do I file accounts Egypt", "audit Egypt company", "audited financial statements Egypt", "balance sheet Egypt", "IFRS Egypt", "EGX listed company accounts", "FRA filing", or any request to explain who must prepare, audit, or file financial statements in Egypt and and what a self-employed person files instead. ALWAYS read this skill before advising on Egyptian financial reporting or audit.
version: 1.1
jurisdiction: EG
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# EG Financial Statements

## What this file is

Loads on `income-tax-workflow-base`. It says who in Egypt prepares and files financial statements (القوائم المالية), what a self-employed person files instead, and which audit standards apply. It is current for tax year 2026 and the law as read on 1 November 2026. It produces a brief for a reviewer, not an audit opinion. Reply in the user's language.

## Scope statement

Covered: sole proprietors, professionals, LLCs and joint-stock companies. Out of scope: banks, insurers and other FRA or Central Bank regulated entities, and group consolidation. Books are in `eg-bookkeeping`; returns in `eg-income-tax` and `eg-corporate-tax`; Law 6 in `eg-sme-tax`.

Authorities: ETA (tax); the Financial Regulatory Authority, FRA (capital market and accounting and auditor legislation); GAFI and the commercial register (company records); EGX (listed companies).

## Filing requirements

| Taxpayer | What is filed | Deadline | Source |
|---|---|---|---|
| Individual, normal basis | Annual return with its schedules; every table must be complete or the return does not count | Before 1 April | [Law 206 of 2020](https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf) Art. 31 |
| Individual, Law 6 | Form 20 (إقرارات) | Same dates | [Law 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf) Art. 12; [MoF 420 of 2025](https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.420.of_.2025.pdf) Art. 2 |
| Company | Annual return | Before 1 May, or within four months of the financial year end | [Law 206 of 2020](https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf) Art. 31 |

Books for a company follow Law 159 of 1981 as well as Article 38: the amended Article 38 applies "with regard to" that law ([Law No. 150 of 2026](https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf), Article 1). A sole proprietor keeps books, not statutory statements.

## Rates and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Law 6 turnover tax, turnover under EGP 500,000 | 0.4% of turnover | 2026 | Business asked for Law 6; turnover not above EGP 20 million (Art. 10) | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf |
| Law 6, EGP 500,000 to under EGP 2,000,000 | 0.5% | 2026 | same conditions | same |
| Law 6, EGP 2,000,000 to under EGP 3,000,000 | 0.75% | 2026 | same conditions | same |
| Law 6, EGP 3,000,000 to under EGP 10,000,000 | 1% | 2026 | same conditions | same |
| Law 6, EGP 10,000,000 to EGP 20,000,000 | 1.5% | 2026 | same conditions | same |
| Late return, up to 60 days | Fine EGP 3,000 to 50,000, plus the tax | 2026 | Art. 69; on repeat, doubled up to three times the bounds | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf |
| Return not filed for over 60 days | Fine EGP 5,000 to 200,000 | 2026 | Doubles if repeated within three years (Art. 70) | same |
| New Egyptian auditing standards | Apply to statements for financial years starting on or after 1 January 2027 | 2027 | Prime Minister Decree No. 3725 of 2025 | https://fra.gov.eg/%d8%aa%d8%b4%d8%b1%d9%8a%d8%b9%d8%a7%d8%aa-%d9%85%d8%b9%d8%a7%d9%8a%d9%8a%d8%b1-%d8%a7%d9%84%d9%85%d8%ad%d8%a7%d8%b3%d8%a8%d8%a9-%d9%88%d9%85%d8%b1%d8%a7%d9%82%d8%a8%d9%8a-%d8%a7%d9%84%d8%ad%d8%b3-2/ |

## Computation rules

1. Identify the taxpayer: natural person or company.
2. Natural person: prepare revenues, deductible costs, depreciation and net profit behind the return, or the Law 6 turnover figure.
3. Company: prepare the annual statements and file with the return by the Article 31 date.
4. Listed or regulated: add FRA and EGX filings.
5. Year starting on or after 1 January 2027: apply the new auditing standards.

## Edge cases and special rules

- **Law 6.** Exempt from Article 38 books, with the MoF 420 set instead; form 20 replaces profit accounts. Examination happens only after five years ([Law 6 of 2025](https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf), Art. 12).
- **Incomplete return.** A return without all tables does not count for the deadline.
- **Auditing reform.** Decree 3725 of 2025 is on the FRA list "as last amended". The FRA list also holds Prime Minister Decree 2115 of 2023, amended by Decree 712 of 2026, on the Permanent Committee for Egyptian Accounting Standards and auditing standards.
- **Only a registered Egyptian auditor signs an audit.** Never imply assurance.
- **EAS is not IFRS.** Never treat them as identical.

Example 1: freelance developer, turnover EGP 1,200,000 in Law 6. No statutory statements. Tax 0.5%: EGP 6,000 on form 20 before 1 April 2027.

```oa-check
name: Developer, Law 6 tax
inputs:
  turnover: 1200000
  rate: 0.005
steps:
  - tax: turnover * rate
expected:
  tax: 6000.00
```

Example 2: decision, stay a sole proprietor or incorporate. The same developer weighs an LLC. Tax under Law 6 is the same EGP 6,000 if the LLC qualifies. The added yearly cost is accounts and audit at an illustrative EGP 40,000 plus EGP 10,000 for filings. A contract worth more than EGP 50,000 a year in margin, available only to a company, pays for it. Below that, stay a sole proprietor.

```oa-check
name: Decision, incorporate if company-only margin exceeds added cost
inputs:
  audit_cost: 40000
  filing_cost: 10000
  extra_margin: 80000
steps:
  - added_cost: audit_cost + filing_cost
  - net_gain: extra_margin - added_cost
expected:
  added_cost: 50000.00
  net_gain: 30000.00
```

Example 3: EGX-listed joint-stock company. Files with the ETA, FRA and EGX. New auditing standards from the financial year starting on or after 1 January 2027.

## Self-checks

- Inputs trace to source documents.
- Taxpayer type matches the filing row.
- Deadline matches Article 31.
- Law 6 status confirmed before using form 20.
- No statement that EAS equals IFRS, and no audit opinion given.
- Refer when a company needs statements or an audit, when the entity is regulated, where EAS and IFRS differ, across the 2027 changeover, or for group work.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law No. 150 of 2026 (Arts 1 to 3), gazette, rendered pages read | https://eta.gov.eg/sites/default/files/2026-08/law.no_.150.of_.2026.pdf | 2026-11-01 |
| Correction notice for Laws 149, 150, 151 of 2026 | https://eta.gov.eg/sites/default/files/2026-08/law.no_.149.150.151.of_.2026.retractation.pdf | 2026-11-01 |
| Unified Tax Procedures Law No. 206 of 2020, Arts 31, 38, 69 to 71, gazette text | https://eta.gov.eg/sites/default/files/2024-03/law_no.206-2020.pdf | 2026-11-01 |
| Law No. 6 of 2025, Arts 7 to 10, 12, 13 | https://eta.gov.eg/sites/default/files/2025-02/law_no.6.of_.2025.pdf | 2026-11-01 |
| MoF Decision No. 420 of 2025, Arts 1 to 4 | https://eta.gov.eg/sites/default/files/2025-12/mof.decision.no_.420.of_.2025.pdf | 2026-11-01 |
| FRA, legislation on accounting standards and auditors, list page only | https://fra.gov.eg/%d8%aa%d8%b4%d8%b1%d9%8a%d8%b9%d8%a7%d8%aa-%d9%85%d8%b9%d8%a7%d9%8a%d9%8a%d8%b1-%d8%a7%d9%84%d9%85%d8%ad%d8%a7%d8%b3%d8%a8%d8%a9-%d9%88%d9%85%d8%b1%d8%a7%d9%82%d8%a8%d9%8a-%d8%a7%d9%84%d8%ad%d8%b3-2/ | 2026-11-01 |

Not yet confirmed: the audit duty for all companies except partnerships (Companies Law 159 of 1981 and Capital Market Law text not opened); the statement list under EAS (financial position, comprehensive income, cash flows, changes in equity, notes); EAS history (2015 set; 2019 and 2023 amendments; IFRS 9, 15, 16 and 17 equivalents and the 1 July 2024 date); who applies EAS or full IFRS, including public-interest entities and EGX issuers; SME standards; Ministry of Investment Decision 166 of 2008; ISQM 1 and 2 from 2025; the claim that Decree 3725 cancels existing standards (the FRA list gives only the application date); FRA interim reporting cadence; bank-required audits of partnerships.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon. The most up-to-date version of this skill is maintained at [openaccountants.com](https://www.openaccountants.com).

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
