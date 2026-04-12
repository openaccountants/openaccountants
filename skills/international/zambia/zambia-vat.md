---
name: zambia-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Zambia VAT return. Standard rate 16%. Unique 100% withholding VAT mechanism. ALWAYS read before handling Zambia VAT work.
version: 2.0
---

# Zambia VAT Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Zambia |
| Standard rate | 16% |
| Zero rate | 0% (exports, agricultural inputs, basic foodstuffs, medical equipment) |
| Filing portal | https://taxonline.zra.org.zm |
| Authority | Zambia Revenue Authority (ZRA) |
| Currency | ZMW (Zambian Kwacha) |
| Filing frequency | Monthly |
| Deadline | 18th of following month |
| Registration threshold | ZMW 800,000 annual turnover |
| Withholding VAT | 100% of VAT amount (unique to Zambia) |
| Primary legislation | VAT Act No. 4 of 1995 (Cap. 331) |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

---

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from Zanaco, Stanbic Bank Zambia, Standard Chartered ZM, FNB Zambia, Absa ZM, or any Zambian bank.

**R-ZM-1 -- Mining sector.** Message: "Mining has specific provisions and development agreements. Escalate."

**R-ZM-2 -- MFEZ.** Message: "Multi-Facility Economic Zone operators require certificate verification. Escalate."

---

## Section 3 -- Supplier pattern library

| Pattern | Treatment | Notes |
|---|---|---|
| ZANACO | EXCLUDE | Exempt financial |
| STANBIC ZM, STANBIC ZAMBIA | EXCLUDE | Same |
| STANDARD CHARTERED ZM | EXCLUDE | Same |
| FNB ZAMBIA, ABSA ZM | EXCLUDE | Same |
| ZRA, ZAMBIA REVENUE | EXCLUDE | Tax payment |
| CUSTOMS | Check for import VAT | |
| NAPSA | EXCLUDE | Social security |
| ZESCO | Domestic 16% | Electricity |
| LWSC, SWSC | Domestic 16% | Water |
| MTN ZM, AIRTEL ZM, ZAMTEL | Domestic 16% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Reverse charge 16% | Non-resident |

---

## Section 4 -- Worked examples

### Example 1 -- Withholding VAT

Government ministry pays supplier. Invoice ZMW 500K + ZMW 80K VAT = ZMW 580K. Ministry withholds ZMW 80K (100% of VAT). Supplier receives ZMW 500K. Claims ZMW 80K credit (Box 19).

### Example 2 -- Reverse charge

SA firm services ZMW 200K. Output Box 6 = ZMW 32K. Input Box 13 = ZMW 32K. Net zero.

---

## Section 5 -- Classification rules

16% standard. 0% exports, agricultural inputs (seeds/fertilizers/pesticides), basic foodstuffs (mealie meal, bread, milk), medical equipment, electricity (first 300 kWh domestic). Exempt: financial, medical, education, residential rental, public transport, postal, water (domestic).

---

## Section 6 -- VAT return form

Output: Boxes 1-8 (standard 16%, zero-rated, exempt, total, output VAT, reverse charge output, adjustments, total output).

Input: Boxes 9-16 (local purchases, imports, input local, input imports, reverse charge input, capital goods, adjustments, allowable input).

Net: Boxes 17-20 (net, credit b/f, withholding VAT credits, net payable).

---

## Section 7 -- Withholding VAT and reverse charge

Withholding VAT: designated agents withhold 100% of VAT amount. Supplier claims credit (Box 19). Unique to Zambia.

Reverse charge: non-resident services. Self-assess 16%. Net zero. VAT Act s.13.

---

## Section 8 -- Deductibility and blocked input

Blocked (s.18): vehicles < 9 seats (unless taxi/hire), entertainment, club subscriptions, personal use, invoices without TPIN.

Partial exemption: s.17. ZRA may approve alternative methods. Refund after 4 months excess credits.

---

## Section 9 -- Filing, deadlines, and penalties

Monthly, 18th of following month. Late filing: 1,000 penalty units or 0.5% of tax, whichever greater. Late payment: 5%/month + BoZ discount rate interest.

---

## Section 10 -- Edge cases, test suite, and escalation

**EC1 -- SaaS.** Reverse charge 16%. Net zero.
**EC2 -- Copper export.** Zero-rated. Input recoverable.
**EC3 -- Withholding VAT.** 100% withheld. Supplier claims credit Box 19.
**EC4 -- Motor vehicle blocked.**
**EC5 -- Mining.** Escalate.
**EC6 -- Agricultural inputs.** Zero-rated.
**EC7 -- Bad debt relief.** 12+ months. Documentation required.

**Test 1** -- ZMW 100K sale. Output ZMW 16K.
**Test 2** -- ZMW 50K purchase + ZMW 8K VAT. Recoverable.
**Test 3** -- SA services ZMW 200K. Output 32K, input 32K. Net zero.
**Test 4** -- Copper export ZMW 5M. Zero-rated.
**Test 5** -- Govt pays supplier ZMW 300K + 48K VAT. Withholding 48K. Credit Box 19.
**Test 6** -- Entertainment. Blocked.

Out of scope: CIT 30%, PAYE 0%-37.5%, NAPSA 5%+5%, Skills Levy 0.5%.

### Prohibitions

- NEVER confuse Zambia withholding VAT (100%) with other countries' rates
- NEVER ignore withholding VAT credits
- NEVER allow recovery on blocked categories
- NEVER accept invoices without TPIN
- NEVER compute numbers -- engine handles arithmetic

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
