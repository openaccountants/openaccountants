---
name: om-tax-overview
description: "Tax overview for Oman, tax year 2026: which taxes apply, their headline rates, deadlines and authorities, from the Tax Authority pages and the laws, with links to the skill that owns each tax."
version: 1.2
jurisdiction: OM
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Oman Tax Overview v1.2

> **General reference only.** This Guide is a draft for AI-assisted reference. It has not received independent closeout review or accountant attestation. Do not use it to file, pay or take a position without professional review.

## Who this applies to

Anyone who needs the map of Oman's taxes for 2026: companies, establishments, foreign groups, Omani and foreign employees. Detail sits in the sibling skills, which own their figures: [income tax](om-income-tax.md), [corporate income tax](om-corporate-income-tax.md), [VAT](oman-vat.md), [payroll and social contributions](om-payroll-social.md), [company formation](om-company-formation.md). Currency is the Omani rial (OMR). The authority is the Tax Authority; the portal is at https://tms.taxoman.gov.om/portal/.

## Rates, bands and thresholds

| Item | 2026 position | Tax year | Official URL |
|---|---|---|---|
| Personal income tax | None in 2026. 5% from 1 January 2028 above OMR 42,000 (RD 56/2025, art. IV of the decree, arts 1 and 8) | 2026 | https://tms.taxoman.gov.om/portal/documents/d/taxportal/-56_2025-1?download=true |
| Corporate income tax | 15% of net taxable income (art. 112) | 2026 | https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf |
| Small enterprises | 3% on conditions (art. 159bis 15) | 2026 | https://tms.taxoman.gov.om/portal/tax-rate |
| Petroleum | 55% (art. 114) | 2026 | https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf |
| Withholding on non-residents | Statutory 10% on covered gross payments; dividend/interest suspension and treaty conditions remain held (arts 52, 113) | 2026 | https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf |
| VAT | 5% standard, 0% and exempt lists (RD 121/2020, arts 36, 47, 51) | 2026 | https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Law+.pdf/9cbe8926-066b-d48d-2b7f-14f41b4c19a8?t=1733169733344 |
| Excise | NONOPERATIVE currentness HOLD: the authority’s October 2025 page gives 100% tobacco, energy drinks, electronic smoking devices and liquids; 50% soft drinks. The current 2026 excise instruments were not closed | 2026 | https://tms.taxoman.gov.om/portal/tax-rate |
| Top-up tax | NONOPERATIVE HOLD for current application: RD 70/2024 originally set 15%, EUR 750 million and 2 of 4 preceding years; RD 101/2026 amendment not reconciled. Refer the group for specialist review, do not compute from this headline | 2026 | https://qanoon.om/p/2024/rd2024070/ |
| Top-up tax amendment | RD 101/2026, issued 29 October 2026, renames and amends the law; listed articles apply from tax years starting 1 January 2025 | 2026 | https://decree.om/2026/rd20260101/ |
| Social contributions, Omani worker | Conditional five-branch illustration only: employee 8%, employer 14.5%; see payroll commencement and current-ceiling holds | 2026 | https://www.spf.gov.om/en/faq/what-are-the-contribution-rates-to-be-paid-by-the-worker-and-employer/ |

## The base

Income tax falls on net taxable income of establishments, Omani companies and permanent establishments. VAT falls on supplies and imports. Social contributions fall on monthly wages. Each base is set out in the sibling skill.

## Deadlines and filing

| Obligation | Deadline | Official URL |
|---|---|---|
| Income tax return, 15% taxpayers | Before four months end after the tax year | https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs |
| Income tax return, 3% taxpayers | Before three months end after the tax year (art. 159bis 18) | https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs |
| Withholding remittance | 14 days from the end of the month of payment or crediting (art. 53) | https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf |
| VAT return and payment | 30 days after each calendar quarter (art. 72) | https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Law+.pdf/9cbe8926-066b-d48d-2b7f-14f41b4c19a8?t=1733169733344 |
| Social contributions | First 15 days of the following month (art. 58) | https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf |
| Personal income tax, first year | Return within 6 months of the year end (art. 33), so by 30 June 2029 for 2028 | https://tms.taxoman.gov.om/portal/documents/d/taxportal/-56_2025-1?download=true |

## Penalties and interest

Late income tax and late VAT carry 1% a month on the unpaid tax (https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf, art. 156; https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Law+.pdf/9cbe8926-066b-d48d-2b7f-14f41b4c19a8?t=1733169733344, definition of Additional Tax). Sibling skills give the fines.

## Cross-border points

Double tax agreements are listed at https://tms.taxoman.gov.om/portal/double-tax-agreements. The Tax Authority news list records agreements signed with Austria (29 January 2026) and Angola (21 September 2026); signed is not in force (https://tms.taxoman.gov.om/portal/news). E-invoicing: the Tax Authority launched the Rafid system and issued the first electronic tax invoice at its 2026 conference (https://tms.taxoman.gov.om/portal/web/taxportal/-/tax-conference-2026-highlights-the-latest-developments-and-changes-in-the-tax-system); rollout runs in four phases ending with all VAT-registered entities (https://tms.taxoman.gov.om/portal/e-invoicing).

## Two worked examples that recompute

**1. Company profit OMR 200,000 at 15%, tax OMR 30,000.** A company with no small-enterprise relief pays 15% of taxable income.

```oa-check
name: Company profit at the standard rate
inputs:
  profit: 200000
steps:
  - tax: profit * 0.15
expected:
  tax: 30000
```

**2. Decision: which regime for a salaried person earning OMR 60,000 in 2026 and in 2028?** In 2026 tax is nil. In 2028, on the same pay and with no exemptions, OMR 18,000 sits above the threshold and tax is OMR 900.

```oa-check
name: Salary 60000, 2026 against 2028
inputs:
  pay: 60000
steps:
  - tax_2026: 0
  - tax_2028: (pay - 42000) * 0.05
expected:
  tax_2026: 0
  tax_2028: 900
```

## Ask the client first

- Company, establishment, permanent establishment or individual?
- Omani or foreign owner, and does the foreign person have a permanent establishment?
- Annual revenue, staff count and registered capital?
- Omani or non-Omani workers?
- Part of a multinational group with revenue of EUR 750 million or more?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Authority, Tax Rates page (read for the published headline rate table only; later-law completeness not established) | https://tms.taxoman.gov.om/portal/tax-rate | 2026-11-01 |
| Tax Authority, Income Tax FAQs (questions 1 to 16 read for authority guidance, including registration, returns and withholding exclusions) | https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs | 2026-11-01 |
| Income Tax Law, RD 28/2009, authority-hosted English consolidation to RD 118/2020 (selected complete clauses: 1, 2, 11, 12, 40, 42 to 53, 69 to 72, 90, 112 to 116, 118, 124, 125, 150, 156, 157, 159bis and 159bis 4 to 6, 9 to 19, 160, 160bis, 179 to 181, 184; scope is recorded in the closeout ledger, not later-amendment closure) | https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf | 2026-11-01 |
| VAT Law, RD 121/2020, Tax Authority English text (arts 28 to 57, 61, 71, 72, 99 to 101 read) | https://tms.taxoman.gov.om/portal/documents/20126/1414820/VAT+Law+.pdf/9cbe8926-066b-d48d-2b7f-14f41b4c19a8?t=1733169733344 | 2026-11-01 |
| Personal Income Tax Law, RD 56/2025, official Tax Authority-hosted gazette issue 1602 pp. 7 to 31, all 25 PDF pages visually read | https://tms.taxoman.gov.om/portal/documents/d/taxportal/-56_2025-1?download=true | 2026-11-01 |
| Top-up Tax Law, RD 70/2024, Arabic text on Qanoon.om, a private publisher (arts 2, 4, 5 read) | https://qanoon.om/p/2024/rd2024070/ | 2026-11-01 |
| RD 101/2026 amending the Top-up Tax Law, Decree.om translation "subject to further review" (decree only; the amendments are behind a paywall and were not read) | https://decree.om/2026/rd20260101/ | 2026-11-01 |
| Social Protection Fund, contribution-rate FAQ answer checked in cached Fund FAQ HTML; conflicting commencement dates held | https://www.spf.gov.om/en/faq/what-are-the-contribution-rates-to-be-paid-by-the-worker-and-employer/ | 2026-11-01 |
| Social Protection Law, RD 52/2023, Fund-hosted English first edition 2024 (law arts 1, 5, 52, 58, 68, 70, 87, 90, 115, 116, 121, 123, 128, 136, 138, 139 and 155 checked; RD 60/2025 commencement amendment separately read) | https://www.spf.gov.om/wp-content/uploads/2024/11/Social-Protaction-Law.pdf | 2026-11-01 |
| Tax Authority news, Tax Conference 2026, 21 Sep 2026 (read for announced tax-system changes only; news is not the operative instrument) | https://tms.taxoman.gov.om/portal/web/taxportal/-/tax-conference-2026-highlights-the-latest-developments-and-changes-in-the-tax-system | 2026-11-01 |
| Tax Authority, e-invoicing page (read for rollout phases and format/provider statements; effective phase dates not established) | https://tms.taxoman.gov.om/portal/e-invoicing | 2026-11-01 |
| Tax Authority, news list (read for Austria and Angola announcement entries only; treaty instruments not read) | https://tms.taxoman.gov.om/portal/news | 2026-11-01 |

Not yet confirmed: VAT commencement date of 16 April 2021 remains a NONOPERATIVE historical topic until the decisive commencement clause is recovered; the income-tax year is 1 January to 31 December (Income Tax Law art. 1(20)); company accounting periods generally last 12 months, first periods up to 18 months, and year-end changes need Chairman consent (Income Tax Law arts 48 to 51). whether resident companies are taxed on worldwide income (the old skill said so, the articles were not found); the amended text of the Top-up Tax Law; the date of any further Rafid or e-invoicing phase; the rate of the Top-up Tax Law provisions as amended on 29 October 2026; whether the portal rate page, dated 29 October 2025, is complete for 2026.

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
