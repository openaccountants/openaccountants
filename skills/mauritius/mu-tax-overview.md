---
name: mu-tax-overview
description: >
  Overview of the Mauritius tax system for the 2026/27 income year: who collects tax, the income year, resident basis, headline personal and company rates, VAT, social contributions, and the main return dates, with links to the detailed skills. Use for a first orientation on Mauritius tax, which taxes apply to a person or business, or which skill in the Mauritius pack to open next. Figures that a detailed skill owns are linked rather than repeated beyond the headline.
jurisdiction: MU
category: international
tax_year: 2026
tax_year_notes: "Income year 1 July 2026 to 30 June 2027 (year of assessment 2027/28)"
version: 0.2
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mauritius Tax Overview v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Tax year covered: Income year 1 July 2026 to 30 June 2027 (year of assessment 2027/28).

## Who this applies to

Anyone asking how tax works in Mauritius. The Mauritius Revenue Authority (MRA) collects income tax, VAT, customs and payroll contributions. The currency is the Mauritian rupee (MUR, Rs). The income year runs 1 July to 30 June (Income Tax Act). Use the detailed skills for any computation.

## Rates, bands and thresholds

| Item | Figure | Conditions | Tax year | Source |
|---|---|---|---|---|
| Top personal rate | 35% | Chargeable income above Rs 12 million, from 1 July 2026; next band 20% | 2026/27 | https://www.mra.mu/download/ITAConsolidated.pdf |
| Standard company rate | 15% | Reduced rate 3% on listed activity | 2026/27 | same |
| VAT standard rate | 15% | Registration above Rs 3 million | 2026 | https://www.mra.mu/download/VATAct.pdf |
| Pillar Two domestic top-up | QDMT | Group revenue EUR 750 million or more, from year of assessment starting 1 July 2025 | 2026/27 | https://www.mra.mu/download/ITAConsolidated.pdf |
| Individual return | 15 October | Electronic, tax paid with it | 2026/27 | same |
| Company return | 6 months after the end of the month the accounting period ends | June year end: 2 days before end of December | 2026/27 | same |

## The base

Residents are taxed on income derived from Mauritius and on foreign income; an individual's foreign income counts when received or dealt with in Mauritius (s.5). Companies are taxed on income derived while resident. Dividends from resident companies are exempt. See [Income tax](mu-income-tax.md), [Corporate income tax](mu-corporate-income-tax.md), [VAT](mauritius-vat.md), [Payroll social](mu-payroll-social.md), [Transfer pricing](mu-transfer-pricing.md), [Cross-border](mu-cross-border.md) and [Company formation](mu-company-formation.md).

## Deadlines and filing

Filing is electronic through [MRA e-Services](https://www.mra.mu/index.php/e-services), under File and Pay. Calendar: the [MRA tax calendar](https://www.mra.mu/important-dates). A date on a weekend or public holiday moves to the next working day.

## Penalties and interest

Each detailed skill carries the penalties for its tax. Income tax: Rs 2,000 per month late, capped, 2.5% late payment, 0.25% monthly interest (ss.121, 122, 122D).

## Cross-border points

Mauritius has a treaty network of 45 agreements ([MRA list](https://www.mra.mu/index.php/taxes-duties/international-taxation/double-taxation-agreements)). See [Cross-border](mu-cross-border.md).

## Two worked examples that recompute

**Example 1.** Person with chargeable income Rs 800,000: 10% on Rs 300,000 is Rs 30,000.

```oa-check
name: Chargeable income Rs 800,000
inputs:
  income: 800000
steps:
  - tax: (income - 500000) * 0.10
expected:
  tax: 30000.00
```

**Example 2. Decision: sole trader or company at Rs 2,000,000 profit, all distributed.** Sole trader with no reliefs pays Rs 50,000 plus 20% of Rs 1,000,000: Rs 250,000. A company pays 15%: Rs 300,000, and the dividend is exempt. At this level the sole trader pays Rs 50,000 less, before social contribution and other costs.

```oa-check
name: Sole trader against company, Rs 2m profit
inputs:
  profit: 2000000
steps:
  - sole: 50000 + (profit - 1000000) * 0.20
  - company: profit * 0.15
  - gap: company - sole
expected:
  gap: 50000.00
```

## Ask the client first

1. Individual or company?
2. Resident under s.73?
3. What income, and from where?
4. Turnover?
5. Staff?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act consolidated to Finance Act 2026: ss.5, 44, 73, 112, 116, 121, 122, 122D, First Schedule read | https://www.mra.mu/download/ITAConsolidated.pdf | 2026-11-01 |
| VAT Act consolidated: Fourth and Sixth Schedules read | https://www.mra.mu/download/VATAct.pdf | 2026-11-01 |
| MRA treaty list page, count and country list read | https://www.mra.mu/index.php/taxes-duties/international-taxation/double-taxation-agreements | 2026-11-01 |
| MRA tax calendar, July to December 2026 read | https://www.mra.mu/important-dates | 2026-11-01 |
| MRA e-Services menu read | https://www.mra.mu/index.php/e-services | 2026-11-01 |

Not yet confirmed: the old note calling foreign income taxable on a remittance basis for companies; only individuals have the s.5(3) rule, read in this pass.

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
