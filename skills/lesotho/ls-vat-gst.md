---
name: ls-vat-gst
description: "Value added tax in Lesotho: registration, rates, returns, penalties and e-invoicing. Covers Lesotho tax year 2026-27 (1 April 2026 to 31 March 2027), figures read from Revenue Services Lesotho and gazetted law on 1 November 2026. Use when someone asks about lesotho vat in Lesotho, what applies, what the rate or threshold is, when to file or pay, what a late filing costs, or how an amount is worked out. Not signed off by an accountant. It states which points could not be read at source so they are not relied on."
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

# Lesotho VAT v0.2

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Businesses making taxable supplies in Lesotho. VAT was introduced in July 2003 and replaced General Sales Tax. Registered businesses are vendors.

Lesotho's tax year runs 1 April to 31 March. This skill covers 2026-27, from 1 April 2026.

## Rates, bands and thresholds

| Item | Figure | Conditions | Official URL |
|---|---|---|---|
| Standard rate | 15% |  | https://www.rsl.org.ls/sites/default/files/2025-01/Guide%20on%20Zero-rated%20Supplies%20of%20Goods.pdf |
| Standard rate in regulations | 15% | Reg 6(1)(d) as amended 2020 | https://www.rsl.org.ls/sites/default/files/2026-09/VAT%20REGULATIONS%20NO.18%20OF%202020.pdf |
| 10% rate | 10% | Reg 6(1)(b) as amended 2021. unverified: the supply it covers; the older skill said electricity, and the 2003 Regulations were not read | https://www.rsl.org.ls/sites/default/files/2026-09/VALUE%20ADDED%20TAX%20%28AMENDMENT%29%20REGULATIONS%20LN.30%20OF%202021_0.pdf |
| Telecommunications | unverified | The older skill said standard rate | https://www.rsl.org.ls/sites/default/files/2026-09/VAT%20REGULATIONS%20NO.18%20OF%202020.pdf |
| Zero rate | 0% | Goods in the Fourth Schedule: basic commodities such as listed foods, fertiliser, pesticides and animal feed. Exports: see the Act | https://www.rsl.org.ls/sites/default/files/2025-01/Guide%20on%20Zero-rated%20Supplies%20of%20Goods.pdf |
| Registration threshold | M2,000,000 a year | Taxable turnover of all branches and activities added together; exempt supplies left out | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Registration%20For%20Value%20Added%20Tax%20Purposes%20%20-%20VAT%20101%20%281%29.pdf |
| Late return | 3% a month or part | s.54 | https://www.rsl.org.ls/sites/default/files/2026-09/VAT%20ACT%20-%202001.pdf |
| Late payment | 3% a month or part | s.55 | https://www.rsl.org.ls/sites/default/files/2026-09/VAT%20ACT%20-%202001.pdf |

## The base

Output tax on supplies less allowed input tax for the month (VAT Act tax payable formula). Register if taxable turnover exceeded the threshold in the past 12 months, or will exceed it in the next 12. Voluntary registration is allowed below the threshold on the conditions in the VAT 101 guide, for example a proven contract or arrangements. The threshold rose from M850,000; RSL's 2017 guide still shows the old figure.

## Deadlines and filing

- Registration: apply within 14 days of the end of the 12-month period (s.17).
- Return and payment: monthly, by the 20th of the next month, with a schedule of purchases and sales (RSL filing page).
- Refunds: RSL says an audit takes 21 days and payment follows within 10 working days.
- E-invoicing: LN 25 of 2026 came into operation on 1 April 2026. A vendor must use an accredited Electronic Billing System linked to RSL's system (Lekuka) once the Commissioner General names them by Gazette notice (reg 3). One system per business activity unless authorised (reg 6).

## Penalties and interest

Late return: 3% of the VAT payable a month or part (s.54). Late payment: 3% of unpaid VAT a month or part (s.55). If a notice under the E-Invoicing Regulations applies, see reg 16.

## Cross-border points

RSL has a Lesotho and South Africa VAT agreement on its treaty page. Imported goods carry VAT at import. Imported services: the older skill said the recipient accounts for VAT; this could not be confirmed in the Act, so check before applying.

## Two worked examples that recompute

Example 1: monthly sales M200,000 before VAT, purchases M90,000 before VAT, all standard rated. Output M30,000 less input M13,500 is M16,500, due by the 20th.

```oa-check
name: Monthly VAT
inputs:
  sales: 200000
  purchases: 90000
steps:
  - payable: (sales - purchases) * 0.15
expected:
  payable: 16500.00
```

Example 2, a decision: file two months late or pay on time? Two months late on M16,500 costs 3% twice under each of ss.54 and 55: M990 each, M1,980 in all.

```oa-check
name: Late return and payment, two months
inputs:
  vat: 16500
  months: 2
steps:
  - return_pen: vat * 0.03 * months
  - pay_pen: vat * 0.03 * months
  - total: return_pen + pay_pen
expected:
  total: 1980.00
```

## Ask the client first

1. Taxable turnover, past 12 months and next 12?
2. All branches and activities?
3. Any zero-rated or exempt supplies?
4. Imports, and services from abroad?
5. Has RSL named the business for e-invoicing?

## Sources

| Source | URL | Read on |
|---|---|---|
| RSL Guide on Zero-rated Supplies of Goods; read in full | https://www.rsl.org.ls/sites/default/files/2025-01/Guide%20on%20Zero-rated%20Supplies%20of%20Goods.pdf | 2026-11-01 |
| VAT (Amendment) Regulations 2020, LN 18 of 2020; read in full (scan) | https://www.rsl.org.ls/sites/default/files/2026-09/VAT%20REGULATIONS%20NO.18%20OF%202020.pdf | 2026-11-01 |
| VAT (Amendment) Regulations 2021, LN 30 of 2021; read in full (scan) | https://www.rsl.org.ls/sites/default/files/2026-09/VALUE%20ADDED%20TAX%20%28AMENDMENT%29%20REGULATIONS%20LN.30%20OF%202021_0.pdf | 2026-11-01 |
| RSL Guide on Registration for VAT, VAT 101; read in full | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Registration%20For%20Value%20Added%20Tax%20Purposes%20%20-%20VAT%20101%20%281%29.pdf | 2026-11-01 |
| Value Added Tax Act 2001, RSL copy; read the sections cited | https://www.rsl.org.ls/sites/default/files/2026-09/VAT%20ACT%20-%202001.pdf | 2026-11-01 |
| RSL Filing of Tax Returns page; read in full | https://www.rsl.org.ls/filing-tax-returns | 2026-11-01 |
| VAT (E-Invoicing) Regulations 2026, LN 25 of 2026; read gazette pages 1 to 8 only (regs 1 to 6) | https://www.rsl.org.ls/sites/default/files/2026-09/VAT%20-%20E-Invoicing%20Regulations%20No.25%20of%202026%20%283%29.pdf | 2026-11-01 |
| RSL Guide on Tax Refunds; read in full | https://www.rsl.org.ls/sites/default/files/2026-09/Guide%20on%20Tax%20Refunds.pdf | 2026-11-01 |
| RSL Tax Treaties page; read the list of agreements only, not the treaty texts | https://www.rsl.org.ls/tax-treaties | 2026-11-01 |

Not yet confirmed: which supply takes 10%; telecommunications rate; reverse charge on imported services; the gazette amending the threshold; whether both ss.54 and 55 stack in practice; E-Invoicing Regulations regs 7 to 17 and schedules (not read); Gazette notices naming vendors; the VAT Administration Bill announced for 2026-27.

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
