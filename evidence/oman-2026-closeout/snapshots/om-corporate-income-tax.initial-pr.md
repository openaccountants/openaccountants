---
name: om-corporate-income-tax
description: "Corporate income tax for Oman, tax year 2026: 15%, 3% and 55% rates, withholding on non-residents, losses, depreciation, returns, portal services and penalties, from the Income Tax Law and Tax Authority FAQs."
version: 1.1
jurisdiction: OM
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Oman Corporate Income Tax

## Who this applies to

Establishments, Omani companies and permanent establishments of foreign persons (arts 2, 112). A permanent establishment is a fixed place of business in Oman, including a branch, office, factory or dependent agent (art. 2). All commercial register holders must register for income tax, whatever the grade, even with losses (https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs, question 1). The Top-up Tax on large groups is in the [overview](om-tax-overview.md).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Standard rate | 15% of taxable income (art. 112) | 2026 | https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf |
| Small enterprise rate | 3% (art. 159bis 15) | 2026 | same |
| Small enterprise conditions | Registered capital up to 60 thousand, annual gross income up to 150 thousand, up to 25 workers, not an occupational activity | 2026 | https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs |
| Small enterprise exemption | Excluded from the 3% tax if run full time by the owner or a partner, or employing at least two Omanis (art. 159bis 15); a return is still due | 2026 | https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf |
| Petroleum | 55% of income from sale of petroleum (art. 114) | 2026 | same |
| Withholding | 10% of the gross amount (arts 52, 113) | 2026 | same |
| Industrial enterprise | 5 years from production, by decision (art. 118) | 2026 | same |
| Late tax | 1% a month (art. 156) | 2026 | same |
| Late or missing return | OMR 100 to 2,000 (art. 179) | 2026 | same |
| Incorrect return | 1% to 25% of the tax difference (art. 180) | 2026 | same |
| Failure to produce documents | OMR 200 to 5,000 (art. 181) | 2026 | same |

## The base

Accounts follow the accrual basis and international accounting standards (art. 12). Small enterprises use the cash basis unless the Authority approves another (art. 159bis 9 and following). Exempt: dividends from Omani companies and gains on securities listed in Muscat (art. 115). Shipping income of an Omani owner is exempt (art. 116). Losses carry forward for up to five years from the end of the loss year (art. 71); exempt activities cannot carry a loss (art. 72). Depreciation pools: 33 1/3% for machinery, computers, vehicles, fixtures and software; 10% for rigs; 15% for other plant (art. 90). Related-party transactions can be adjusted (art. 125). First accounting period: up to 18 months (art. 50). A register opened from January to June closes that 31 December; from July to December it closes the next 31 December (https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs, question 5).

## Deadlines and filing

| Step | Rule | Official URL |
|---|---|---|
| Tax card | Request when incorporating or registering (art. 11) | https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf |
| Notification | Non-register cases: 60 days from start, 30 days for changes (art. 11) | same |
| Return, 15% | Before four months end after the year | https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs |
| Return, 3% and exempt | Before three months end after the year | https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs |
| Inactive | Zero return with a stamped non-practice letter | https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs |
| Pay | Due on the return date (art. 150), via Claims and Payments on the portal | https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs |
| Withholding | 14 days from the end of the month paid or credited, with the form; copy to the recipient (art. 53) | https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf |
| Objection | 45 days, portal service 12 | https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs |

How to file: sign in to the Tax Authority portal, open income tax services, choose service No. 6 (final returns), complete the return, attach the accounts or the statement of income, submit, then pay through Claims and Payments. Amend registration details with service No. 9. The principal officer gives others access through Representation Rights (https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs, questions 2, 6, 7, 8). The box numbers of the return are not in any page we opened.

## Penalties and interest

Art. 156 additional tax of 1% a month, which the Chairman may relieve. Fines as in the table. Deliberate failure to file by the principal officer: 1 to 6 months in prison and a fine of OMR 500 to 20,000, or either (art. 184). Collection lapses after seven years (art. 157).

## Cross-border points

Withholding covers royalties, research and development, software, and management or service fees paid to a non-resident without a permanent establishment (art. 52; https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs, questions 11, 12, 14). Not subject: conferences and exhibitions, transport, shipping and insurance of goods, training, air tickets and hotels abroad, board meetings, reinsurance, and services tied to activity or property outside Oman (https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs, question 15). Foreign tax credit: apply within two years of the year end (art. 124). Treaties: art. 120 and following. The Tax Authority rate page names interest and the law names dividends in the withholding list, so see the Not yet confirmed line before withholding on either.

## Two worked examples that recompute

**1. Company with taxable income OMR 100,000.** Tax at 15% is OMR 15,000; a late payment of three months adds OMR 450.

```oa-check
name: Standard company with three months late
inputs:
  income: 100000
  months: 3
steps:
  - tax: income * 0.15
  - additional: tax * 0.01 * months
expected:
  tax: 15000
  additional: 450
```

**2. Decision: does a small establishment with profit OMR 40,000 fall at 3%, or 15% once it fails a condition?** Crossing any one condition costs OMR 4,800 a year.

```oa-check
name: Small enterprise against standard rate
inputs:
  profit: 40000
steps:
  - small: profit * 0.03
  - standard: profit * 0.15
  - cost: standard - small
expected:
  small: 1200
  standard: 6000
  cost: 4800
```

## Ask the client first

- Legal form, and is the owner Omani or foreign?
- Registered capital, gross income, worker count, and activity?
- Does the owner run it full time, and how many Omanis work there?
- Year end, and first period dates?
- Payments to non-residents, and their type?
- Any petroleum, industrial or shipping activity?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Law, RD 28/2009, consolidated to RD 118/2020, Tax Authority English text (arts 2, 11, 12, 50, 52, 53, 69 to 73, 90, 112 to 118, 124, 125, 156, 159bis 11 to 19, 179 to 184 read) | https://tms.taxoman.gov.om/portal/documents/20126/1455220/income+tax+law+english.pdf | 2026-11-01 |
| Tax Authority, Income Tax FAQs (all 16 read) | https://tms.taxoman.gov.om/portal/web/taxportal/income-tax-faqs | 2026-11-01 |
| Tax Authority, Tax Rates page (whole page read) | https://tms.taxoman.gov.om/portal/tax-rate | 2026-11-01 |

Not yet confirmed: the current status of withholding on dividends and interest (the law lists dividends, the portal rate page lists interest, FAQ 12 lists neither, and the suspension decisions were not opened); the provisional return in the old skill (no provision found in the consolidated text); the article setting the four-month deadline (art. 134 could not be located in the English PDF, the FAQ states it); the currency of the small enterprise thresholds, which the FAQ gives without saying rials; whether RD 56/2025 art. 3 changes withholding before 2028; amendments to the Income Tax Law after RD 118/2020; statutory audit of tax accounts.

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
