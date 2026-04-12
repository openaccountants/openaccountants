---
name: uganda-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Uganda VAT return. Standard rate 18%. Withholding VAT 6% of taxable value. EAC customs union but no common VAT. ALWAYS read before handling Uganda VAT work.
version: 2.0
---

# Uganda VAT Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Uganda |
| Standard rate | 18% |
| Zero rate | 0% (exports, drugs/medicines, educational materials, agricultural inputs) |
| Filing portal | https://efiling.ura.go.ug |
| Authority | Uganda Revenue Authority (URA) |
| Currency | UGX |
| Filing frequency | Monthly |
| Deadline | 15th of following month |
| Registration | UGX 150,000,000 quarterly turnover |
| Withholding VAT | 6% of taxable value (not 6% of VAT) |
| Primary legislation | VAT Act Cap. 349 |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

---

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from Stanbic Uganda, dfcu Bank, Standard Chartered UG, Centenary Bank, Bank of Baroda UG, or any Ugandan bank.

---

## Section 3 -- Supplier pattern library

| Pattern | Treatment | Notes |
|---|---|---|
| STANBIC UG, STANBIC UGANDA | EXCLUDE | Exempt financial |
| DFCU, DFCU BANK | EXCLUDE | Same |
| STANDARD CHARTERED UG | EXCLUDE | Same |
| CENTENARY BANK | EXCLUDE | Same |
| URA, UGANDA REVENUE | EXCLUDE | Tax payment |
| CUSTOMS | Check for import VAT | |
| NSSF UGANDA | EXCLUDE | Social security |
| UMEME | Domestic 18% | Electricity |
| NWSC | Domestic 18% | Water |
| MTN UG, AIRTEL UG | Domestic 18% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Reverse charge 18% | Non-resident |

---

## Section 4 -- Worked examples

### Example 1 -- Withholding VAT

Government pays supplier. Invoice UGX 50M + UGX 9M VAT = UGX 59M. Withholding = 6% of UGX 50M = UGX 3M. Supplier receives UGX 56M. Claims UGX 3M credit (Box 14).

### Example 2 -- Agricultural inputs zero-rated

Farm purchases fertilizer. Supplier charges 0%. Zero-rated supply.

---

## Section 5 -- Classification rules

18% standard. 0% exports, drugs/medicines, educational materials, agricultural inputs (seeds/fertilizers/pesticides/hoes), aircraft for international transport, diplomatic. Exempt: unprocessed foodstuffs, financial (interest/forex/life insurance), medical/dental, education, residential rental (unfurnished), social welfare, burial, postal, water (domestic public).

---

## Section 6 -- VAT return form

Output: 1a-1d, 2-4 (standard, zero-rated, exempt, total, output VAT, adjustments, total output).

Input: 5a-5c, 6-11 (local purchases, imports, imported services, input local, input imports, input imported services, total input, adjustments, allowable input).

Net: 12-15 (net, credit b/f, withholding VAT credits, net payable).

---

## Section 7 -- Withholding VAT and reverse charge

Withholding VAT: designated agents deduct 6% of TAXABLE VALUE (not 6% of VAT). Supplier claims Box 14.

Reverse charge: non-resident services. Self-assess 18%. Net zero. VAT Act s.14.

EAC: no intra-community mechanism.

---

## Section 8 -- Deductibility and blocked input

Blocked (s.21): entertainment, vehicles < 10 seats (unless taxi/hire/driving instruction), clubs, personal use, non-taxable supply purchases.

Deemed supplies: non-business use, gifts > UGX 100,000, cessation with stock.

Bad debt: 3 years (long period).

---

## Section 9 -- Filing, deadlines, and penalties

Monthly, 15th. Late filing: UGX 200K/month or 2%/month, whichever greater. Late payment: 2%/month compounding.

---

## Section 10 -- Edge cases, test suite, and escalation

**EC1 -- SaaS.** Reverse charge 18%. Net zero.
**EC2 -- Withholding VAT.** 6% of taxable value. Supplier claims credit.
**EC3 -- Coffee export.** Zero-rated. Input recoverable.
**EC4 -- Furnished rental.** May be 18%. Reviewer flag.
**EC5 -- EAC import (Kenya).** VAT at customs. Recoverable.
**EC6 -- Motor vehicle blocked.**
**EC7 -- Agricultural inputs.** Zero-rated.
**EC8 -- Bad debt.** 3-year period.

**Test 1** -- UGX 20M sale. Output 3.6M.
**Test 2** -- UGX 5M equipment + 900K VAT. Recoverable.
**Test 3** -- SA services UGX 10M. Output 1.8M, input 1.8M.
**Test 4** -- Fish export UGX 100M. Zero-rated.
**Test 5** -- Govt pays UGX 30M + 5.4M VAT. Withholding 6% of 30M = 1.8M.
**Test 6** -- Entertainment. Blocked.
**Test 7** -- Exempt financial UGX 500M. No output. Input not recoverable.
**Test 8** -- Gift UGX 500K. Deemed supply. Output 90K.

Out of scope: CIT 30%, PAYE 0%-40%, NSSF 5%+5%, LST.

### Prohibitions

- NEVER confuse withholding VAT (6% of taxable value) with withholding income tax
- NEVER treat EAC as intra-community
- NEVER ignore withholding VAT credits
- NEVER compute numbers -- engine handles arithmetic

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
