---
name: zimbabwe-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Zimbabwe VAT return. Standard rate 15%. Mandatory fiscalised electronic devices. Multi-currency regime (ZiG/USD). ALWAYS read before handling Zimbabwe VAT work.
version: 2.0
jurisdiction: ZW
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Zimbabwe VAT

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Zimbabwe |
| Standard rate | 15% |
| Zero rate | 0% (exports, basic foodstuffs, farming inputs, medical, fuel) |
| Filing portal | https://efiling.zimra.co.zw |
| Authority | ZIMRA |
| Currency | ZiG (Zimbabwe Gold) / USD (multi-currency) |
| Filing frequency | Bi-monthly; Monthly (large taxpayers) |
| Deadline | 25th of following month |
| Registration | USD 25,000 taxable supplies in 12 months |
| Fiscalised device | MANDATORY for all VAT-registered operators |
| Primary legislation | VAT Act [Chapter 23:12] |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

- **Standard rate** — 15%
- **Zero rate** — 0% (exports, basic foodstuffs, farming inputs, medical, fuel)
- **Filing portal** — https://efiling.zimra.co.zw
- **Authority** — ZIMRA
- **Currency** — ZiG (Zimbabwe Gold) / USD (multi-currency)
- **Filing frequency** — Bi-monthly; Monthly (large taxpayers)
- **Deadline** — 25th of following month
- **Registration** — USD 25,000 taxable supplies in 12 months
- **Fiscalised device** — MANDATORY for all VAT-registered operators
- **Primary legislation** — VAT Act [Chapter 23:12]
- **Contributor** — Open Accounting Skills Registry
- **Validated by** — Pending
- **Last research update** — April 2026

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from CBZ, FBC Bank, Stanbic ZW, NMB ZW, ZB Bank, or any Zimbabwean bank.

## Section 3 -- Supplier pattern library

**Supplier pattern library**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CBZ, CBZ BANK | EXCLUDE | Exempt financial |
| FBC, FBC BANK | EXCLUDE | Same |
| STANBIC ZW, NMB, ZB BANK | EXCLUDE | Same |
| ZIMRA | EXCLUDE | Tax payment |
| CUSTOMS | Check for import VAT |  |
| NSSA | EXCLUDE | Social security |
| ZESA, ZETDC | Domestic 15% | Electricity |
| ZINWA | Domestic 15% | Water |
| ECONET, NETONE, TELECEL | Domestic 15% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Reverse charge 15% | Non-resident |

## Section 4 -- Worked examples

### Example 1 -- Non-fiscalised invoice

VAT-registered supplier issues handwritten invoice (no fiscal device). Input VAT NOT recoverable even if supplier is registered.

### Example 2 -- Deemed supply on gift

Company gives client gifts USD 200. Exceeds USD 25 threshold. Deemed supply. Output VAT = USD 30 (15%).

## Section 5 -- Classification rules

- **Standard rate classification** — 15% standard.
- **Zero-rated items** — 0% exports, basic foodstuffs (maize meal, bread, milk, sugar, cooking oil, salt, fruits/vegetables), farming inputs, medical supplies, fuel (separate levy), domestic electricity.
- **Exempt supplies** — Exempt: financial, medical services, education, residential rental, public transport, postal, water.
- **Fiscalised device requirement** — Fiscalised device: mandatory. Non-fiscalised invoices cannot support input claims.

## Section 6 -- VAT return form

- **VAT return form boxes** — Output: Boxes 1-8. Input: Boxes 9-16 (must have fiscal invoice). Net: Boxes 17-19.

## Section 7 -- Reverse charge and fiscalisation

- **Reverse charge non-resident services** — Non-resident services: self-assess 15%. Net zero.  _(VAT Act s.13)_
- **Fiscalisation requirement** — All sales must go through fiscalised device connected to ZIMRA. Criminal offence for non-compliance.

## Section 8 -- Deductibility and blocked input

- **Blocked input categories** — Blocked (s.16): vehicles < 9 seats, entertainment, club subscriptions, personal use, non-fiscalised invoices.  _(s.16)_
- **Multi-currency conversion** — Multi-currency: convert USD to ZiG at interbank rate on date of supply if filing in ZiG. Reviewer must confirm current policy.
- **Deemed supplies** — Deemed supplies: goods for non-business use, gifts > USD 25, cessation with stock.

## Section 9 -- Filing, deadlines, and penalties

- **Bi-monthly periods** — Bi-monthly periods: Jan-Feb, Mar-Apr, etc.
- **Deadline** — 25th of following month
- **Late filing penalty** — USD 30/day
- **Late payment penalty** — 10% + prescribed interest
- **Non-fiscalisation penalty** — Criminal

## Section 10 -- Edge cases, test suite, and escalation

Reverse charge 15%. Net zero.

Input NOT recoverable.

Zero-rated. Input recoverable.

Reviewer flag.

Zero-rated.

15% on market value.

Escalate.

USD 10K sale. Output USD 1,500.

Fiscal invoice USD 5K + USD 750. Recoverable.

Handwritten receipt USD 2K + USD 300. Input = 0.

SA consulting USD 20K. Output 3K, input 3K. Net zero.

Export USD 500K. Zero-rated.

Gift USD 200. Deemed supply. Output USD 30.

Out of scope: CIT 24.72% (24% + AIDS levy), PAYE 0%-40%, NSSA 4.5%+4.5%, IMTT 2%.

### Prohibitions

- **Prohibition 1** — NEVER allow input recovery without fiscalised invoice
- **Prohibition 2** — NEVER ignore exchange rate conversion requirements
- **Prohibition 3** — NEVER allow recovery on blocked categories
- **Prohibition 4** — NEVER compute numbers -- engine handles arithmetic

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).

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
