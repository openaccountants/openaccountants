---
name: tn-cross-border
description: "Tunisia cross-border tax for tax year 2026: withholding on non-residents, dividends, interest, property and share gains, privileged-tax jurisdictions and gross-up. Use for questions on paying a foreign supplier from Tunisia, retenue a la source for non-residents, or Tunisian-source income."
version: 0.1
jurisdiction: TN
category: cross-border
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tunisia Cross-Border Withholding v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Payers in Tunisia paying non-residents, and non-residents with Tunisian income. Tax treaties prevail (art. 2).

## Rates, bands and thresholds

| Item | Amount | Tax year | Conditions | Official URL |
|---|---|---|---|---|
| Non-resident fees and income | 15% | 2026 | Not through a Tunisian establishment. Art. 52 I(b) | https://web.archive.org/web/20250906073044/https://jibaya.tn/wp-content/uploads/2025/07/code-IS-et-IRPP-francais-1.pdf |
| Capital income | 20% | 2026 | Art. 52 I(c) | same |
| Dividends | 10% | 2026 | Art. 52 I(c bis) | same |
| Bank loan interest | 10% | 2026 | Foreign banks. Art. 52 I(e) | same |
| Property sale by non-established seller | 15% of price | 2026 | Sales from 1 Jan 2025. Art. 52 I(b bis) | same |
| Share gain, non-resident company | 20%, cap 5% of price | 2026 | Art. 52 I(e bis) | same |
| Share gain, non-resident individual | 10%, cap 2.5% of price | 2026 | same | same |
| Privileged-tax jurisdictions | 25% | 2026 | Lines b third dash, c, c bis, e | same |
| Established non-residents without declaration | 15%, or 25% if privileged | 2026 | Final. Art. 52 | same |

## The base

Gross amount. Where the payer bears the tax, gross up with the formula in art. 52. Exempt: foreign-currency deposit interest, international ship and aircraft charter (art. 3).

## Deadlines and filing

Remit with the monthly return. See [VAT](tunisia-vat.md) for dates. VAT on foreign suppliers is also there.

## Penalties and interest

Not confirmed.

## Cross-border points

Apply a treaty only with the residence certificate the treaty route requires.

## Two worked examples that recompute

Fee TND 10,000 to a non-resident: withhold 1,500.

```oa-check
name: Non-resident fee
inputs:
  fee: 10000
steps:
  - tax: fee * 0.15
expected:
  tax: 1500.00
```

Share gain 400,000 on price 1,000,000: 20% is 80,000, cap 50,000, pay 50,000.

```oa-check
name: Capped share gain
inputs:
  gain: 400000
  price: 1000000
steps:
  - tax: min(gain * 0.20, price * 0.05)
expected:
  tax: 50000.00
```

## Ask the client first

1. Payee residence and treaty certificate?
2. Income type?
3. Tunisian establishment?
4. Who bears the tax?

## Sources

| Source | URL | Read on |
|---|---|---|
| Code IRPP-IS, French text updated to LF 2025, archived copy of the DGI file; articles cited in this skill read. The 2026 edition page exists but its PDF could not be opened | https://web.archive.org/web/20250906073044/https://jibaya.tn/wp-content/uploads/2025/07/code-IS-et-IRPP-francais-1.pdf | 2026-11-01 |

Not yet confirmed: Treaty rates and list. Privileged-jurisdiction list. Certificate rules. 2026 consolidated code.

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
