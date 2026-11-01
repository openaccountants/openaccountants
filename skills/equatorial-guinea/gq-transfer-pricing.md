---
name: gq-transfer-pricing
description: >
  Transfer pricing in Equatorial Guinea for tax year 2026 under Ley 1/2024 General Tributaria. Covers related parties, the arm's length comparison, control, dependence and connection tests, privileged tax regimes, the annual related-party statement with its 250,000,000 and 125,000,000 XAF thresholds, country-by-country reporting, and limits on group interest. Use for questions such as does Equatorial Guinea have transfer pricing rules, when must a company file a related-party statement, what is the country-by-country report threshold, how much group interest can be deducted, and what penalty applies. Applies to companies with foreign parents, subsidiaries or linked parties. It covers the rules in the law; no method regulation was found.
jurisdiction: GQ
category: transfer-pricing
tax_year: 2026
tier: 2
last_updated: 2026-11-01
version: 0.2
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Equatorial Guinea Transfer Pricing v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Enterprises that depend on or control others, or are connected to them (art 74). Control is a majority of capital or votes or the power of decision; dependence is power to take part in financial and operating policy; connection is any shareholding, commercial or similar tie (art 74.1).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Related-party statement | Income of 250,000,000 XAF or more, or net assets of 125,000,000 XAF or more (art 30.1) | 2026 | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf |
| Country-by-country report | Group parent with income over 500,000,000 XAF, with art 31.1 conditions (art 31) | 2026 | same |
| Privileged regime | No tax, or tax of half or less of the local charge; the law text as read says "superior a la mitad" (art 74.3) | 2026 | same |
| Group interest rate cap | BEAC rate plus 3 points (art 68.2) | 2026 | same |
| Net interest cap | 30% of gross operating surplus, excess carried 5 years (art 68.4, 68.5) | 2026 | same |

## The base

Profit shifted through prices or otherwise is added back, measured against what would have arisen without the tie (art 74.1). With a privileged regime the tie is presumed, and the company must prove otherwise (art 74.2).

## Deadlines and filing

The statement of gross related-party amounts goes with the DEF, in the form set by the tax administration (art 30.1, 30.2). The DEF is due within 6 months of year end, see [Corporate income tax](gq-corporate-income-tax.md). The country report goes with the consolidated accounts in the same period (art 31.1). A local group member reports if its parent's state has no such duty, or if named by the group, and must notify the administration (art 31.2, 31.3). Foreign-controlled entities must also tell the administration before starting whether accounts are integrated or autonomous (art 30.3).

## Penalties and interest

Added-back profit bears tax at 25%, under-declaration sanctions of 10% to 25% (art 411.A) and interest of 2.5% a month (art 412). False or fraudulent information, or missing notes on country-by-country or transfer pricing transactions, costs a fixed sanction by turnover if not put right within 30 working days of a demand (art 411.E.3, 411.E.5): 250,000 XAF up to 250,000,000; 5,000,000 XAF from 250,000,001 to 1,000,000,000; 25,000,000 XAF above 1,000,000,000.

## Cross-border points

Withholding on the same payments is in [Cross-border](gq-cross-border.md).

## Two worked examples that recompute

**Interest cap.** Gross operating surplus 100,000,000 XAF, net interest 45,000,000. Deductible 30,000,000; 15,000,000 carries for up to 5 years.

```oa-check
name: Net interest cap
inputs:
  ebe: 100000000
  interest: 45000000
steps:
  - allowed: min(interest, ebe * 0.30)
  - carried: interest - allowed
expected:
  allowed: 30000000
  carried: 15000000
```

**Decision: reprice or defend a 50,000,000 XAF excess charge from a parent.** If added back: tax 12,500,000, plus 10% sanction 1,250,000. Repricing before filing costs the same tax with no sanction, so the sanction is the saving.

```oa-check
name: Adjustment cost
inputs:
  excess: 50000000
steps:
  - tax: excess * 0.25
  - sanction: tax * 0.10
  - total: tax + sanction
expected:
  tax: 12500000
  sanction: 1250000
  total: 13750000
```

## Ask the client first

1. Group chart and who controls whom?
2. Income and net assets?
3. Related-party flows by type?
4. Counterparties in low-tax places?
5. Group loans, rate, and is capital fully paid?

## Sources

| Source | URL | Read on |
|---|---|---|
| Ley 1/2024 General Tributaria, Boletin Oficial del Estado scan, read by OCR; arts 30, 31, 68, 74, 411, 412 read | https://boe.gob.gq/files/LEY%20TRIBUTARIA.pdf | 2026-11-01 |

The law is a scan with no text layer: figures were read from machine OCR, and the salary scale from the page image. It applies to tax year 2026; the 2026 Budget Law (Ley 9/2025) changes it only where stated.

Not yet confirmed: a pricing method regulation; documentation content; the form for art 30.2; whether the art 411.A 10% runs on the tax or on the undeclared amount ("la cantidad no declarada"), since the example uses the tax; art 74.3 reads "superior" on the page image, where "inferior" is the expected sense, so confirm whether a correction exists.

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
