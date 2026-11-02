---
name: mozambique-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Mozambique VAT (IVA) return. Standard rate 16%, reduced 5%. ISPC simplified regime for small taxpayers. Portuguese-language terminology. ALWAYS read before handling Mozambique IVA work.
version: 2.0
jurisdiction: MZ
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mozambique VAT

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Mozambique |
| Standard rate | 16% |
| Reduced rate | 5% (private health, education, vocational training) |
| Zero rate | 0% (exports) |
| ISPC (simplified) | 3% of turnover (below MZN 2,500,000) |
| Filing portal | https://efatura.at.gov.mz |
| Authority | Autoridade Tributaria de Mocambique (AT) |
| Currency | MZN (Metical) |
| Filing frequency | Monthly (large) or Quarterly (standard) |
| Deadline | Last working day of following month/quarter |
| Registration threshold | MZN 2,500,000 |
| Primary legislation | CIVA, Law 32/2007 as amended |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from BCI (Banco Comercial e de Investimentos), Millennium bim, Standard Bank MZ, BCI Fomento, Absa MZ, or any Mozambican bank.

- **R-MZ-1 -- Megaproject** — Trigger: LNG, Sasol, mining concessions. Message: "Megaproject fiscal regimes are negotiated individually. Escalate."

## Section 3 -- Supplier pattern library

**Supplier pattern library**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BCI, BANCO COMERCIAL | EXCLUDE | Exempt financial |
| MILLENNIUM BIM | EXCLUDE | Same |
| STANDARD BANK MZ | EXCLUDE | Same |
| AT, AUTORIDADE TRIBUTARIA | EXCLUDE | Tax payment |
| ALFANDEGAS, CUSTOMS | Check for import IVA |  |
| INSS | EXCLUDE | Social security |
| EDM, ELECTRICIDADE | Domestic 16% | Electricity |
| FIPAG | Domestic 16% | Water |
| VODACOM MZ, TMCEL, MOVITEL | Domestic 16% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Autoliquidacao 16% | Non-resident |

## Section 4 -- Worked examples

### Example 1 -- Standard sale

MZN 1,000,000 net. IVA = MZN 160,000 (16%).

### Example 2 -- ISPC taxpayer

Small retailer under ISPC. Quarterly sales MZN 400,000. ISPC = 3% = MZN 12,000. No input recovery.

## Section 5 -- Classification rules

- **Standard rate classification** — 16% standard. 5% reduced (private health/education). 0% exports. Exempt: basic foodstuffs, financial, medical (public), education (public), residential rental, public transport, agricultural inputs.
- **ISPC classification** — ISPC: 3% of gross turnover for businesses below MZN 2,500,000. No IVA charged, no input recovery.

## Section 6 -- IVA return form

Output: Lines 1-8 (16% sales, exempt, exports, total, IVA liquidado, autoliquidacao, adjustments, total).

Input: Lines 9-14 (local, imports, autoliquidacao input, capital goods, exclusions, total deductible).

Net: Lines 15-17 (net, credit transitado, payable/credit).

## Section 7 -- Reverse charge (autoliquidacao)

- **Non-resident services reverse charge** — Non-resident services: self-assess 16%. Net zero.  _(CIVA Art. 23)_

## Section 8 -- Deductibility and blocked input

- **Blocked input VAT** — Blocked: vehicles < 9 seats, entertainment, personal use, fuel for blocked vehicles, invoices without NUIT.  _(CIVA Art. 20-22)_
- **Prorata deduction** — Prorata deduction rule applies.  _(CIVA Art. 19)_

## Section 9 -- Filing, deadlines, and penalties

- **Filing frequency and deadline** — Monthly or quarterly. Last working day of following month.
- **Late filing penalty** — MZN 5K-50K
- **Late payment penalty** — 2%/month

## Section 10 -- Edge cases, test suite, and escalation

Autoliquidacao 16%. Net zero.

Zero-rated. Input recoverable.

Exceeds MZN 2.5M: must register for IVA.

Escalate.

Rice/bread exempt. No output, no input recovery.

MZN 1M sale. IVA MZN 160K.

MZN 500K purchase + IVA 80K. Recoverable.

SA services MZN 3M. Output 480K, input 480K. Net zero.

Export MZN 50M. Zero-rated.

Entertainment. Blocked.

ISPC quarterly MZN 400K. ISPC = MZN 12K.

Out of scope: IRPC 32%, IRPS progressive 10%-32%, INSS employer 4% + employee 3%.

### Prohibitions

- **Prohibitions list** — - NEVER confuse IVA with ISPC - NEVER allow ISPC taxpayers to charge IVA - NEVER apply standard rules to megaprojects without verification - NEVER accept invoices without NUIT - NEVER compute numbers -- engine handles arithmetic

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
