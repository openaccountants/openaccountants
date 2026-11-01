---
name: tn-transfer-pricing
description: "Tunisia transfer pricing for tax year 2026: control test, arm length add-back under art. 48 septies, privileged-tax jurisdictions, and the annual return for groups with turnover of TND 200 million or more. Use for questions on prix de transfert, related-party pricing or Tunisian TP returns."
version: 0.1
jurisdiction: TN
category: transfer-pricing
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tunisia Transfer Pricing v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Tunisian resident or established companies that depend on or control foreign group companies, and any company dealing with privileged-tax jurisdictions. Art. 48 septies applies to years opened from 1 Jan 2020.

## Rates, bands and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Control test | More than 50% of capital or votes, or de facto decision power | 2026 | Direct or indirect; or common control. Art. 48 septies | https://web.archive.org/web/20250906073044/https://jibaya.tn/wp-content/uploads/2025/07/code-IS-et-IRPP-francais-1.pdf |
| TP return threshold | Turnover excl. tax TND 200 million or more | 2026 | Foreign related parties. Art. 59 II bis | same |

## The base

Profits moved by price changes or any other means are added back, measured against profit without the link (art. 48 septies). No link is needed with privileged-tax jurisdictions.

## Deadlines and filing

Annual TP return, electronic, same date as the IS return (art. 59 II bis, art. 60). It holds group data, policy, assets, transaction summary with methods, loans and non-cash dealings. Country-by-country return: DGI publishes a form and guide; thresholds not confirmed.

## Penalties and interest

Not confirmed.

## Cross-border points

Treaty relief and advance opinion were not read.

## Two worked examples that recompute

Over threshold: turnover 250m. Under: 150m. Only the first files.

```oa-check
name: Margin over the threshold
inputs:
  turnover: 250000000
steps:
  - excess: turnover - 200000000
expected:
  excess: 50000000.00
```

Adjustment: sale at TND 900,000 against arm's length 1,000,000, adding 100,000 of profit at 20%.

```oa-check
name: Adjustment tax
inputs:
  actual: 900000
  arm: 1000000
steps:
  - added: arm - actual
  - tax: added * 0.20
expected:
  tax: 20000.00
```

## Ask the client first

1. Group structure and holdings?
2. Turnover?
3. Dealings with foreign affiliates by type?
4. Any partner in a privileged-tax place?

## Sources

| Source | URL | Read on |
|---|---|---|
| Code IRPP-IS, French text updated to LF 2025, archived copy of the DGI file; articles cited in this skill read. The 2026 edition page exists but its PDF could not be opened | https://web.archive.org/web/20250906073044/https://jibaya.tn/wp-content/uploads/2025/07/code-IS-et-IRPP-francais-1.pdf | 2026-11-01 |

Not yet confirmed: Penalties, documentation arrete of 16 Oct 2019, CbC thresholds, 2026 changes.

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
