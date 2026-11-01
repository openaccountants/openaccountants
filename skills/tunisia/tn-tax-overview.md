---
name: tn-tax-overview
description: "Tunisia tax overview for tax year 2026: a short map of income tax, company tax, VAT, wealth tax, authority, currency and residence basis, linking to the skill that owns each figure. Use first for general questions on how tax works in Tunisia, which taxes apply, or which authority to deal with."
version: 1.1
jurisdiction: TN
category: international
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tunisia Tax Overview v1.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone needing a map of Tunisian tax for 2026. Calendar tax year; currency TND; authority Direction Generale des Impots (DGI).

## Rates, bands and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Top income tax rate | Owned by income tax skill | 2026 | See [income tax](tn-income-tax.md) | https://web.archive.org/web/20250906073044/https://jibaya.tn/wp-content/uploads/2025/07/code-IS-et-IRPP-francais-1.pdf |
| Standard company rate | Owned by company skill | 2026 | See [corporate income tax](tn-corporate-income-tax.md) | same |
| VAT | Owned by VAT skill | 2026 | See [VAT](tunisia-vat.md); returns monthly | https://web.archive.org/web/20250906073223/https://jibaya.tn/wp-content/uploads/2024/02/Code-de-la-taxe-sur-la-valeur-ajoutee-2023_compressed.pdf |
| Wealth tax on individuals | 0.5% from TND 3m to 5m; 1% above TND 5m | 2026 | Due 1 January on net wealth, including minor children's. Residents worldwide, others on Tunisian assets. Main home, business assets, cars up to 12 fiscal horsepower and bank deposits are out. Return by end of June. LF 2026 art. 88 | https://web.archive.org/web/20261005010006/https://jibaya.tn/wp-content/uploads/2025/12/Loi2025_17-1.pdf |

## The base

Residents: tax on all income (art. 2). Non-residents: Tunisian source only (art. 3). Companies: profits of Tunisian establishments (art. 47).

## Deadlines and filing

Companies: 25 March (art. 60). Individuals: by income type. See each skill.

## Penalties and interest

See each skill.

## Cross-border points

See [cross-border](tn-cross-border.md).

## Two worked examples that recompute

```oa-check
name: Band check
inputs:
  income: 10000
steps:
  - tax: (income - 5000) * 0.15
expected:
  tax: 750.00
```

Income TND 10,000 pays 750 before deductions.

```oa-check
name: Minimum tax floor
inputs:
  turnover: 100000
steps:
  - minimum: max(turnover * 0.002, 500)
expected:
  minimum: 500.00
```

Company at TND 100,000 turnover: floor applies, TND 500.

## Ask the client first

1. Individual or company?
2. Resident or not?
3. What activity?

## Sources

| Source | URL | Read on |
|---|---|---|
| Code IRPP-IS, French text updated to LF 2025, archived copy of the DGI file; articles cited in this skill read. The 2026 edition page exists but its PDF could not be opened | https://web.archive.org/web/20250906073044/https://jibaya.tn/wp-content/uploads/2025/07/code-IS-et-IRPP-francais-1.pdf | 2026-11-01 |
| Loi n° 2025-17 du 12 decembre 2025, loi de finances 2026, JORT n° 148, archived copy of the DGI file; art. 88 read | https://web.archive.org/web/20261005010006/https://jibaya.tn/wp-content/uploads/2025/12/Loi2025_17-1.pdf | 2026-11-01 |
| Code de la TVA, 2023 French edition, archived copy of the DGI file; arts. 2, 7, 10, 15, 18, 19, 19 bis and Tables A and B read. The 2026 edition PDF could not be opened | https://web.archive.org/web/20250906073223/https://jibaya.tn/wp-content/uploads/2024/02/Code-de-la-taxe-sur-la-valeur-ajoutee-2023_compressed.pdf | 2026-11-01 |

Not yet confirmed: Social Solidarity Contribution rate.

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
