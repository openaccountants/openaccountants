---
name: ls-tax-overview
description: "A map of the Lesotho tax system: taxes, rates, deadlines and which skill to open next. Covers Lesotho tax year 2026-27 (1 April 2026 to 31 March 2027), figures read from Revenue Services Lesotho and gazetted law on 1 November 2026. Use when someone asks about lesotho tax overview in Lesotho, what applies, what the rate or threshold is, when to file or pay, what a late filing costs, or how an amount is worked out. Not signed off by an accountant. It states which points could not be read at source so they are not relied on."
jurisdiction: LS
category: international
tax_year: 2026
tax_year_notes: "2026-27"
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
version: 0.2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Lesotho Tax Overview v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Anyone needing a first view of Lesotho tax. Residents are taxed on worldwide income; non-residents on Lesotho-source income. The authority is Revenue Services Lesotho (RSL). The currency is the loti (M, LSL); the 1:1 peg to the South African rand is carried from the older skill and not confirmed at source.

Lesotho's tax year runs 1 April to 31 March. This skill covers 2026-27, from 1 April 2026.

## Rates, bands and thresholds

| Item | Figure | Conditions | Official URL |
|---|---|---|---|
| Personal income tax | 20% and 30% | Band limit M77,760; see ls-income-tax | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Taxation%20of%20Employment%20Income%2026-27.pdf |
| Corporate income tax | 25% | 10% for manufacturing and farming; see ls-corporate-income-tax | https://www.rsl.org.ls/sites/default/files/2024-07/Corporate%20Income%20Tax%20Guide.pdf |
| VAT | 15% | Threshold M2,000,000; see ls-vat-gst | https://www.rsl.org.ls/sites/default/files/2025-01/Guide%20on%20Zero-rated%20Supplies%20of%20Goods.pdf |
| Fringe benefits tax | 40% | See ls-payroll-social | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf |

## The base

Income tax falls under the Income Tax Act 1993 as amended; VAT under the Value Added Tax Act 2001. RSL administers both. Each figure has one home in the skill named on its row.

## Deadlines and filing

- Income tax return: 30 June.
- VAT return and payment: 20th of the next month.
- PAYE: 15th of the next month.
- Provisional tax: 30 September, 31 December, 31 March.

## Penalties and interest

Income tax: 22% per twelve-month period as stated by RSL. VAT: 3% a month or part.

## Cross-border points

Withholding and treaties are in ls-corporate-income-tax.

## Two worked examples that recompute

Example 1: M120,000 resident income is taxed M15,984 (working in ls-income-tax).

```oa-check
name: Resident M120,000
inputs:
  income: 120000
steps:
  - tax: 77760 * 0.20 + (income - 77760) * 0.30 - 12240
expected:
  tax: 15984.00
```

Example 2, a decision: M1,900,000 of taxable turnover need not register for VAT; M2,100,000 must. The excess over the threshold is M100,000.

```oa-check
name: VAT threshold excess
inputs:
  turnover: 2100000
steps:
  - excess: max(turnover - 2000000, 0)
expected:
  excess: 100000.00
```

## Ask the client first

1. Individual, company or branch?
2. Resident?
3. What activity?
4. Taxable turnover?
5. Employees?

## Sources

| Source | URL | Read on |
|---|---|---|
| RSL Guide on Taxation of Employment Income 26-27; read in full | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Taxation%20of%20Employment%20Income%2026-27.pdf | 2026-11-01 |
| RSL Corporate Income Tax Guide; read in full | https://www.rsl.org.ls/sites/default/files/2024-07/Corporate%20Income%20Tax%20Guide.pdf | 2026-11-01 |
| RSL Guide on Zero-rated Supplies of Goods; read in full | https://www.rsl.org.ls/sites/default/files/2025-01/Guide%20on%20Zero-rated%20Supplies%20of%20Goods.pdf | 2026-11-01 |
| RSL Guide on Registration for VAT, VAT 101; read in full | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Registration%20For%20Value%20Added%20Tax%20Purposes%20%20-%20VAT%20101%20%281%29.pdf | 2026-11-01 |
| Income Tax Act 1993, RSL copy updated to 1 April 2012; read the sections cited; later amendments are not in this copy | https://www.rsl.org.ls/sites/default/files/2026-09/Income%20Tax%20Act%201993%20%20Updated%20up%20to%201%20April%202012.pdf | 2026-11-01 |
| RSL Filing of Tax Returns page; read in full | https://www.rsl.org.ls/filing-tax-returns | 2026-11-01 |

Not yet confirmed: loti and rand peg (Common Monetary Area text not read); law changes announced for 2026-27.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network: accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
