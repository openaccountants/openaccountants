---
name: morocco-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Morocco VAT (TVA) return. Two rates from 2026 -- 20%/10% (7% and 14% phased out). Critical distinction between exempt-with-deduction (Art. 92) and exempt-without-deduction (Art. 91). ALWAYS read before handling Morocco TVA work.
version: 2.0
jurisdiction: MA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Morocco VAT

## Section 1 -- Quick reference

**Quick reference table**

| Field | Value |
| --- | --- |
| Country | Morocco |
| Standard rate | 20% |
| Reduced rate | 10% (hotels/restaurant/tourism, pharmaceuticals, water, electricity, school supplies, banking operations) |
| Phased out | 14% and 7% eliminated by 2026 Loi de Finances reform |
| Exempt with deduction (Art. 92) | 0% effective: exports, international transport, fertilizers, investment goods (36-month window) |
| Exempt without deduction (Art. 91) | Financial, medical, education, bread/flour |
| Filing portal | https://portail.tax.gov.ma (SIMPL) |
| Authority | Direction Generale des Impots (DGI) |
| Currency | MAD |
| Filing frequency | Monthly (>= MAD 1M) or Quarterly |
| Deadline | 20th of following month |
| Registration | MAD 500K goods / 200K services |
| Primary legislation | CGI Art. 87-125; Loi de Finances 2024-2026 |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

## Section 2 -- Required inputs and refusal catalogue

- **Minimum viable input** — Minimum viable -- bank statement. Acceptable from Attijariwafa Bank, BMCE (Bank of Africa), Banque Populaire, CIH, BMCI, Credit du Maroc, or any Moroccan bank.
- **R-MA-1 -- CFC entity** — Trigger: Casablanca Finance City status. Message: "CFC has specific tax regime. Escalate."

## Section 3 -- Supplier pattern library

**Supplier pattern library**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ATTIJARIWAFA, AWB | EXCLUDE | Exempt financial (sans deduction) |
| BMCE, BANK OF AFRICA | EXCLUDE | Same |
| BANQUE POPULAIRE, BP | EXCLUDE | Same |
| CIH, BMCI, CREDIT DU MAROC | EXCLUDE | Same |
| DGI | EXCLUDE | Tax payment |
| DOUANE | Check for import TVA |  |
| CNSS, AMO | EXCLUDE | Social security |
| ONE, ONEE | Domestic 10% or 20% | Electricity/water |
| IAM, MAROC TELECOM, ORANGE MA, INWI | Domestic 20% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Autoliquidation 20% | Non-resident |

## Section 4 -- Worked examples

### Example 1 -- Hotel at 10%

Room MAD 1,500/night. TVA at 10% = MAD 150.

### Example 2 -- Export (exempt with deduction)

Textiles MAD 10M export. Line 5. No output TVA. Input fully recoverable.

### Example 3 -- Financial services (exempt without deduction)

Bank interest MAD 10M. Line 6. No output. Related input NOT recoverable.

## Section 5 -- Classification rules

- **Standard rate** — 20%
- **Reduced rate** — 10% (hotels/restaurants/tourism, pharmaceuticals, water, electricity, school supplies, banking operations, legal/accounting)
- **7% and 14% phased out** — 7% and 14% PHASED OUT by 2026.
- **Art. 92 (exempt WITH deduction)** — Exports, international transport, fertilizers, investment goods (36-month window for new registrations). Functions like zero-rating.  _(Art. 92)_
- **Art. 91 (exempt WITHOUT deduction)** — Financial, medical, education, bread/flour.  _(Art. 91)_

## Section 6 -- TVA return form

Output: Lines 1-14 (20% sales, 10% sales, exempt with deduction, exempt without deduction, total, TVA 20%, TVA 10%, autoliquidation, adjustments, total brute).

Input: Lines 15-20 (operating purchases, capital goods, imports, autoliquidation input, exclusions, total recoverable).

Net: Lines 21-23 (due, credit reporte, payable/credit).

## Section 7 -- Reverse charge and decalage

- **Reverse charge** — Non-resident services. Self-assess at applicable rate (usually 20%). Net zero.  _(CGI Art. 115)_
- **Decalage (one-month delay)** — Progressively abolished. Capital goods: no delay. Operating purchases: check current Loi de Finances. Reviewer flag.

## Section 8 -- Deductibility and blocked input

- **Blocked input** — Vehicles < 9 seats (unless taxi/hire/leasing), fuel for blocked vehicles, personal use, entertainment (above normal level), gifts > MAD 100/item/recipient, invoices without IF/ICE.  _(CGI Art. 106)_
- **Prorata** — Includes exempt-with-deduction in numerator. Annual regularization.  _(Art. 104)_
- **36-month investment window** — New businesses, exempt with deduction on investment goods.  _(Art. 92-I-6)_

## Section 9 -- Filing, deadlines, and penalties

- **Filing frequency and deadline** — Monthly before 20th (>= MAD 1M) or quarterly.
- **Late filing penalty** — 15% + 0.5% first month, 0.5% thereafter.
- **Late payment penalty** — 10% + 5% first month + 0.5% after.

## Section 10 -- Edge cases, test suite, and escalation

Autoliquidation 20%. Net zero.

Not 20%.

Moved from 7%.

Moved from 14%.

Exempt with deduction. Input recoverable.

36-month Art. 92-I-6 window. Reviewer verify.

Exempt without deduction. Input not recoverable.

Escalate.

MAD 100K sale. TVA MAD 20K (20%).

Hotel MAD 500K. TVA MAD 50K (10%).

Pharmacy MAD 200K. TVA MAD 20K (10%).

Freight MAD 300K. TVA MAD 60K (20%).

Export MAD 5M. Zero.

US services MAD 200K. Output 40K, input 40K.

Motor vehicle blocked. MAD 300K + 60K. Input = 0.

Bank interest MAD 10M. Exempt without deduction.

Out of scope: IS 10%/20%/31%, PAYE 0%-38%, CNSS/AMO.

### Prohibitions

- NEVER confuse Art. 92 (with deduction) with Art. 91 (without deduction)
- NEVER apply 7% or 14% -- phased out by 2026
- NEVER ignore decalage without confirming abolition
- NEVER accept invoices without IF/ICE
- NEVER compute numbers -- engine handles arithmetic

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
