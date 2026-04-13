---
name: morocco-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Morocco VAT (TVA) return. Two rates from 2026 -- 20%/10% (7% and 14% phased out). Critical distinction between exempt-with-deduction (Art. 92) and exempt-without-deduction (Art. 91). ALWAYS read before handling Morocco TVA work.
version: 2.0
---

# Morocco VAT (TVA) Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
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

---

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from Attijariwafa Bank, BMCE (Bank of Africa), Banque Populaire, CIH, BMCI, Credit du Maroc, or any Moroccan bank.

**R-MA-1 -- CFC entity.** Trigger: Casablanca Finance City status. Message: "CFC has specific tax regime. Escalate."

---

## Section 3 -- Supplier pattern library

| Pattern | Treatment | Notes |
|---|---|---|
| ATTIJARIWAFA, AWB | EXCLUDE | Exempt financial (sans deduction) |
| BMCE, BANK OF AFRICA | EXCLUDE | Same |
| BANQUE POPULAIRE, BP | EXCLUDE | Same |
| CIH, BMCI, CREDIT DU MAROC | EXCLUDE | Same |
| DGI | EXCLUDE | Tax payment |
| DOUANE | Check for import TVA | |
| CNSS, AMO | EXCLUDE | Social security |
| ONE, ONEE | Domestic 10% or 20% | Electricity/water |
| IAM, MAROC TELECOM, ORANGE MA, INWI | Domestic 20% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Autoliquidation 20% | Non-resident |

---

## Section 4 -- Worked examples

### Example 1 -- Hotel at 10%

Room MAD 1,500/night. TVA at 10% = MAD 150.

### Example 2 -- Export (exempt with deduction)

Textiles MAD 10M export. Line 5. No output TVA. Input fully recoverable.

### Example 3 -- Financial services (exempt without deduction)

Bank interest MAD 10M. Line 6. No output. Related input NOT recoverable.

---

## Section 5 -- Classification rules

20% standard. 10% reduced (hotels/restaurants/tourism, pharmaceuticals, water, electricity, school supplies, banking operations, legal/accounting). 7% and 14% PHASED OUT by 2026.

Critical distinction:
- Art. 92 (exempt WITH deduction): exports, international transport, fertilizers, investment goods (36-month window for new registrations). Functions like zero-rating.
- Art. 91 (exempt WITHOUT deduction): financial, medical, education, bread/flour.

---

## Section 6 -- TVA return form

Output: Lines 1-14 (20% sales, 10% sales, exempt with deduction, exempt without deduction, total, TVA 20%, TVA 10%, autoliquidation, adjustments, total brute).

Input: Lines 15-20 (operating purchases, capital goods, imports, autoliquidation input, exclusions, total recoverable).

Net: Lines 21-23 (due, credit reporte, payable/credit).

---

## Section 7 -- Reverse charge and decalage

Reverse charge: non-resident services. Self-assess at applicable rate (usually 20%). Net zero. CGI Art. 115.

Decalage (one-month delay): progressively abolished. Capital goods: no delay. Operating purchases: check current Loi de Finances. Reviewer flag.

---

## Section 8 -- Deductibility and blocked input

Blocked (CGI Art. 106): vehicles < 9 seats (unless taxi/hire/leasing), fuel for blocked vehicles, personal use, entertainment (above normal level), gifts > MAD 100/item/recipient, invoices without IF/ICE.

Prorata (Art. 104): includes exempt-with-deduction in numerator. Annual regularization.

36-month investment window (Art. 92-I-6): new businesses, exempt with deduction on investment goods.

---

## Section 9 -- Filing, deadlines, and penalties

Monthly before 20th (>= MAD 1M) or quarterly. Late filing: 15% + 0.5% first month, 0.5% thereafter. Late payment: 10% + 5% first month + 0.5% after.

---

## Section 10 -- Edge cases, test suite, and escalation

**EC1 -- SaaS.** Autoliquidation 20%. Net zero.
**EC2 -- Hotel 10%.** Not 20%.
**EC3 -- Pharmaceuticals 10%.** Moved from 7%.
**EC4 -- Transport 20%.** Moved from 14%.
**EC5 -- Export (Art. 92).** Exempt with deduction. Input recoverable.
**EC6 -- New business investment.** 36-month Art. 92-I-6 window. Reviewer verify.
**EC7 -- Bank (Art. 91).** Exempt without deduction. Input not recoverable.
**EC8 -- CFC entity.** Escalate.

**Test 1** -- MAD 100K sale. TVA MAD 20K (20%).
**Test 2** -- Hotel MAD 500K. TVA MAD 50K (10%).
**Test 3** -- Pharmacy MAD 200K. TVA MAD 20K (10%).
**Test 4** -- Freight MAD 300K. TVA MAD 60K (20%).
**Test 5** -- Export MAD 5M. Zero.
**Test 6** -- US services MAD 200K. Output 40K, input 40K.
**Test 7** -- Motor vehicle blocked. MAD 300K + 60K. Input = 0.
**Test 8** -- Bank interest MAD 10M. Exempt without deduction.

Out of scope: IS 10%/20%/31%, PAYE 0%-38%, CNSS/AMO.

### Prohibitions

- NEVER confuse Art. 92 (with deduction) with Art. 91 (without deduction)
- NEVER apply 7% or 14% -- phased out by 2026
- NEVER ignore decalage without confirming abolition
- NEVER accept invoices without IF/ICE
- NEVER compute numbers -- engine handles arithmetic

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
