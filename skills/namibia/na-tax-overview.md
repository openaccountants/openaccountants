---
name: na-tax-overview
description: >
  Namibia tax overview for 2026: the taxes, authority, years, top rates and where each is covered. Figures come from Namibian law and official pages opened on 2026-11-01. Items that could not be opened are named as not yet confirmed. Not reviewed by a licensed accountant.
version: 0.2
jurisdiction: NA
category: international
tax_year: 2026
tax_year_notes: "Individuals: year of assessment 1 March 2026 to 28 February 2027. Companies: financial year."
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Namibia Tax Overview v0.2

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. Do not rely on it to file, pay or take a position without review by a qualified professional in Namibia.

## Who this applies to

Anyone asking which Namibian taxes apply. Authority: Namibia Revenue Agency (NamRA, https://www.namra.org.na/). Currency: Namibian dollar (N$). Portal: https://itas.namra.org.na. The annotated Income Tax Act read runs to Income Tax Amendment Act 4 of 2024. The 2025 and 2026 gazette indexes list no Income Tax or VAT amendment act.

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Individual year | 1 March to 28 February | 2026 | https://www.namra.org.na/individual-tax/page/i-earn-a-monthly-salary/ |
| Top individual rate | 37% above N$1,550,000 | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf |
| Tax-free band | N$100,000 | 2026 | same |
| Company rate | 30% | 2026 | same |
| VAT | 15% | 2026 | https://www.lac.org.na/laws/annoSTAT/Value-Added%20Tax%20Act%2010%20of%202000.pdf |

Figures are owned by the [income tax](na-income-tax.md), [company](na-corporate-income-tax.md), [VAT](na-vat-gst.md) and [payroll](na-payroll-social.md) skills.

## The base

Source-based: income from a source within or deemed within Namibia (s.15). Company year: its financial year.

## Deadlines and filing

Salaried 30 June. Business and farming individuals and companies: 7 months after year end (s.56(1A)). VAT 25th after the period. PAYE and withholding within 20 days. Stamp duty and transfer duty are in [NamRA's pages](https://www.namra.org.na/tax-types); transfer duty is payable within 6 months of acquisition.

## Penalties and interest

See each skill. Income tax interest is 20% a year.

## Cross-border points

See [cross-border](na-cross-border.md) and [transfer pricing](na-transfer-pricing.md). A tax residency certificate is applied for on NamRA forms (https://www.namra.org.na/tax-residency-certificate).

## Two worked examples that recompute

Example 1. Individual on N$1,600,000: N$429,000 + 37% of N$50,000 = N$447,500.

```oa-check
name: Top band
inputs:
  t: 1600000
steps:
  - tax: 429000 + (t - 1550000) * 0.37
expected:
  tax: 447500.00
```

Example 2. A decision: at the same N$1,600,000 profit, company tax is N$480,000, more than N$447,500 personally, before dividends and salaries.

```oa-check
name: Company v personal
inputs:
  t: 1600000
steps:
  - co: t * 0.30
  - d: co - 447500
expected:
  d: 32500.00
```

## Ask the client first

1. Individual or company?
2. Source of income?
3. Year end?
4. Turnover?
5. Employees?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act 24 of 1981, annotated to Act 4 of 2024 (read: Schedule 4, s.56) | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf | 2026-11-01 |
| VAT Act (read: s.6) | https://www.lac.org.na/laws/annoSTAT/Value-Added%20Tax%20Act%2010%20of%202000.pdf | 2026-11-01 |
| NamRA salary page (read: whole page) | https://www.namra.org.na/individual-tax/page/i-earn-a-monthly-salary/ | 2026-11-01 |
| NamRA tax types (read: overview) | https://www.namra.org.na/tax-types | 2026-11-01 |

Not yet confirmed: Budget 2026/27 proposals; stamp duty scales.

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
