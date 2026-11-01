---
name: na-cross-border
description: >
  Namibia cross-border tax, 2026: withholding on dividends, interest, royalties and fees to non-residents, deadlines and rules for non-resident payees. Figures come from Namibian law and official pages opened on 2026-11-01. Items that could not be opened are named as not yet confirmed. Not reviewed by a licensed accountant.
version: 0.1
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

# Namibia Cross-Border Tax v0.1

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. Do not rely on it to file, pay or take a position without review by a qualified professional in Namibia.

## Who this applies to

Namibian payers and non-residents with Namibian-source income. A payment to an address outside Namibia is presumed made to a non-resident (s.35A(5)).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Dividends, company holding 25%+ | 10% | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf (s.45(a)) |
| Dividends, other | 20% | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf (s.45(b)) |
| Interest to non-resident | 10%, final | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf (s.35B) |
| Interest from banks and unit trusts, not to a Namibian company | 10%, final | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf (s.34A) |
| Royalties | 10% | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf (s.35) |
| Management or consultancy fees | 10%, final | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf (s.35A(3)(a)) |
| Directors and entertainment fees | 25%, final | 2026 | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf (s.35A(3)(b)) |

Government stock interest is outside s.34A. Treaties may reduce rates; read the treaty.

## The base

Gross amount paid. "Consultancy" covers administrative, managerial, technical and consultative services.

## Deadlines and filing

Pay and file within 20 days after the month of withholding ([NamRA](https://www.namra.org.na/tax-types/page/withholding-tax-30120/)); foreign interest by the 20th (Act). Interest is deemed paid at the earlier of payment or due date. Dividends: company or agent pays NRST. Freight tax for non-residents: forms on [NamRA](https://www.namra.org.na/tax-types/page/freight-tax/). Payment reference: see the [company skill](na-corporate-income-tax.md).

## Penalties and interest

10% penalty per month or part and 20% interest, limited to the unpaid tax ([NamRA](https://www.namra.org.na/tax-types/page/withholding-tax-30120/)).

## Cross-border points

Imported services VAT: [VAT skill](na-vat-gst.md). Pricing: [transfer pricing skill](na-transfer-pricing.md). Exchange control is not covered.

## Two worked examples that recompute

Example 1. Consultancy fee N$100,000: withhold N$10,000.

```oa-check
name: Fee
inputs:
  a: 100000
steps:
  - wt: a * 0.10
expected:
  wt: 10000.00
```

Example 2. A decision: a holder at 25% or below it. Dividend N$1,000,000 costs N$100,000 at 25%+, N$200,000 below.

```oa-check
name: NRST
inputs:
  d: 1000000
steps:
  - hi: d * 0.20
  - lo: d * 0.10
  - save: hi - lo
expected:
  save: 100000.00
```

## Ask the client first

1. Payee's country and residence?
2. Type of payment?
3. Shareholding percentage?
4. Treaty relied on?
5. Date paid?

## Sources

| Source | URL | Read on |
|---|---|---|
| Income Tax Act 24 of 1981, annotated to Act 4 of 2024 (read: ss.34A, 35, 35A, 45 and 35B) | https://www.lac.org.na/laws/annoSTAT/Income%20Tax%20Act%2024%20of%201981.pdf | 2026-11-01 |
| NamRA withholding page (read: whole page) | https://www.namra.org.na/tax-types/page/withholding-tax-30120/ | 2026-11-01 |

Not yet confirmed: Treaty list and treaty rates (no official list opened); s.35 royalty base beyond the opening words.

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
