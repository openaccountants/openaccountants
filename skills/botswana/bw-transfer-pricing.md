---
name: bw-transfer-pricing
description: >
  Botswana transfer pricing for 2026-27: the arm's length rule in s 117 of the Income Tax Act, 2026, the nil price rule for assets bought through associates, low tax entities and the interest cap. Use for Botswana related-party pricing.
version: 0.2
jurisdiction: BW
category: international
tax_year: 2026
tax_year_notes: "2026-27 (1 July 2026 to 30 June 2027)"
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Botswana Transfer Pricing v0.2

> **General reference only.** This skill is general tax reference material. It has not been reviewed for any specific person's facts. Check figures against the official sources named here.

Tax year: 2026-27 (1 July 2026 to 30 June 2027). The Income Tax Act, 2026, Tax Administration Act, 2026 and Value Added Tax Act, 2026 commenced on 1 July 2026 and replace the old Cap. 52:01 and Cap. 50:03 regimes.

## Who this applies to

Any person transacting directly or indirectly with an associate, resident or not (ITA s 117(1)).

## Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Standard | Arm's length conditions | 2026-27 | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=954:income-tax-act-amendment-2026 (s 117) |
| Low tax entity | effective rate below 15%, or no tax on foreign income, or secrecy | 2026-27 | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=954:income-tax-act-amendment-2026 (s 119) |
| Attribution trigger | 50% or more | 2026-27 | same |
| Interest cap | 30% of tax EBITDA | 2026-27 | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=954:income-tax-act-amendment-2026 (s 36) |

## The base

BURS may adjust income, deductions, gains, losses and credits (s 117(3)). Method and quantum are as prescribed (s 117(4)); documentation is as prescribed (s 117(5)). A country-by-country report and advance pricing agreements may be prescribed (s 117(7)).

Asset bought from a non-resident associate that bought it from a third party: price is nil unless the taxpayer holds the third party's tax invoice (s 117(6)).

## Deadlines and filing

The Act sets no separate transfer pricing return. Keep records eight years (TAA s 14). Adjustments flow through the [company return](bw-corporate-income-tax.md).

## Penalties and interest

Interest and shortfall penalties follow the [company tax skill](bw-corporate-income-tax.md).

## Cross-border points

Treaty relief: see [Cross-border](bw-cross-border.md). Substance tests for companies: SI 92 regs 36 to 39.

## Two worked examples that recompute

Example 1. Associate fee P1,000,000 against arm's length P700,000: P300,000 added, tax P73,500.

```oa-check
name: Adjustment
inputs:
  paid: 1000000
  arm: 700000
steps:
  - add: paid - arm
  - tax: add * 0.245
expected:
  add: 300000.00
  tax: 73500.00
```

Example 2. A decision: machine P200,000 from a foreign parent. With the supplier's invoice the cost is deductible at 20% a year; without it, cost is nil.

```oa-check
name: Nil price
inputs:
  cost: 200000
steps:
  - yearly: cost * 0.20
  - tax_value: yearly * 0.245
expected:
  yearly: 40000.00
  tax_value: 9800.00
```

## Ask the client first

- Which associates, and where?
- What was bought, sold or charged?
- Any third-party invoices for assets?
- Group revenue, for any country-by-country duty?
- Existing pricing study?

## Sources

| Source | Link | Read |
|---|---|---|
| Income Tax Act, 2026 (No. 13 of 2026), read: ss 7, 8, 17, 28, 34 to 37, 53, 96, 117, 119, 123 to 144, Schedules 1 to 3; Regulations SI 92 and Commencement Order SI 93 in the same file | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=954:income-tax-act-amendment-2026 | 2026-11-01 |
| Tax Administration Act, 2026 (No. 14 of 2026), read: ss 14, 18, 27, 41, 98, 101 to 103; Regulations SI 90 regs 3, 4, 21, 28, 30, 33, 34 in the same file | https://www.burs.org.bw/index.php/tax/tax-laws-2026?download=955:tax-administration-act-2026 | 2026-11-01 |

Not yet confirmed: the Transfer Pricing Regulations made under the old Act (not opened; they continue only if consistent, s 144(i)), including thresholds and documentation content; any CbC rule in force.

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
