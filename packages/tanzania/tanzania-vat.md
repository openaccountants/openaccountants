---
name: tanzania-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Tanzania VAT return. Standard rate 18% (16% reduced for non-VAT-registered B2C electronic payments from Sep 2025). EAC customs union but no common VAT. Withholding VAT 3% goods / 6% services from July 2025. ALWAYS read before handling Tanzania VAT work.
version: 2.0
---

# Tanzania VAT Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Tanzania |
| Standard rate | 18% (16% reduced for B2C electronic payments to unregistered persons, from Sep 2025) |
| Zero rate | 0% (exports, agricultural inputs, diplomatic, SEZ) |
| Filing portal | https://ots.tra.go.tz |
| Authority | Tanzania Revenue Authority (TRA) |
| Currency | TZS |
| Filing frequency | Monthly |
| Deadline | 20th of following month |
| Registration | TZS 200,000,000 annual turnover |
| Withholding VAT | 3% goods / 6% services (from July 2025) |
| Primary legislation | VAT Act 2014 (Act No. 5) |
| EAC members | Kenya, Uganda, Rwanda, Burundi, South Sudan, DRC |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

---

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from CRDB, NMB (National Microfinance Bank), Stanbic TZ, Standard Chartered TZ, NBC, or any Tanzanian bank.

**R-TZ-1 -- Mining.** Message: "Mining has specific provisions under Mining Act 2010. Escalate."

---

## Section 3 -- Supplier pattern library

| Pattern | Treatment | Notes |
|---|---|---|
| CRDB | EXCLUDE | Exempt financial |
| NMB, NATIONAL MICROFINANCE | EXCLUDE | Same |
| STANBIC TZ, NBC | EXCLUDE | Same |
| TRA, TANZANIA REVENUE | EXCLUDE | Tax payment |
| CUSTOMS | Check for import VAT | |
| NSSF, PPF | EXCLUDE | Social security |
| TANESCO | Domestic 18% | Electricity |
| DAWASA | Domestic 18% | Water |
| VODACOM TZ, AIRTEL TZ, TIGO, HALOTEL | Domestic 18% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Reverse charge 18% | Non-resident |

---

## Section 4 -- Worked examples

### Example 1 -- Standard sale

TZS 10M net. Output VAT = TZS 1.8M (18%).

### Example 2 -- EAC import

Goods from Kenya TZS 20M. VAT 18% at customs = TZS 3.6M. Recoverable. No intra-community mechanism.

---

## Section 5 -- Classification rules

18% standard (16% for B2C electronic payments to unregistered, from Sep 2025). 0% exports, agricultural inputs, diplomatic, SEZ. Exempt: unprocessed foodstuffs, financial, medical, education, residential rental, life insurance, public transport, agricultural equipment, water (public utilities), petroleum (fuel levy).

---

## Section 6 -- VAT return form (ITX222.01.E)

Output: A1-A7 (18% sales, zero-rated, exempt, total, output VAT, adjustments, total output).

Input: B1-B7 (local purchases, imports, input local, input imports, total input, adjustments, net input).

Net: C1-C3 (net, credit b/f, net payable).

---

## Section 7 -- Reverse charge, withholding VAT, and imports

Reverse charge: non-resident services. Self-assess 18%. Net zero. VAT Act s.16.

Withholding VAT (from July 2025): designated agents withhold 3% of VAT on goods, 6% on services. Remit by 20th. Supplier needs certificate to claim credit.

EAC imports: VAT at border, no intra-community mechanism.

---

## Section 8 -- Deductibility and blocked input

Blocked (s.64): entertainment, vehicles < 13 seats (unless taxi/hire/driving instruction), clubs, personal use, non-taxable supply purchases.

De minimis for exempt: if < 5% of total, full recovery may be allowed. Reviewer confirm.

Deemed supplies: non-business use, gifts > TZS 100,000, cessation with stock.

---

## Section 9 -- Filing, deadlines, and penalties

Monthly, 20th. Late filing: 1%/month (max 100%), min TZS 150K. Late payment: BoT rate + 5%, daily.

---

## Section 10 -- Edge cases, test suite, and escalation

**EC1 -- SaaS.** Reverse charge 18%. Net zero.
**EC2 -- Export to Kenya.** Zero-rated. Input recoverable.
**EC3 -- EAC import (Uganda).** VAT at customs. Recoverable.
**EC4 -- Mining.** Escalate.
**EC5 -- Deemed supply cessation.** 18% on market value.
**EC6 -- Tourism hotel.** May qualify for zero-rating if foreign currency. Reviewer flag.
**EC7 -- Credit note.** Adjust in A6.
**EC8 -- Bad debt.** 12 months + write-off.

**Test 1** -- TZS 10M sale. Output 1.8M.
**Test 2** -- TZS 5M furniture + 900K VAT. Recoverable.
**Test 3** -- Indian IT TZS 5M. Output 900K, input 900K. Net zero.
**Test 4** -- Coffee export TZS 100M. Zero-rated.
**Test 5** -- Entertainment. Blocked.
**Test 6** -- Exempt financial TZS 50M. No output. Input not recoverable.
**Test 7** -- Kenya import TZS 20M. Customs VAT 3.6M. Recoverable.
**Test 8** -- Gift TZS 500K. Deemed supply. Output 90K.

Out of scope: CIT 30%, PAYE 0%-30%, SDL 4%, NSSF/PPF 10%+10%.

### Prohibitions

- NEVER treat EAC as intra-community
- NEVER ignore deemed supply rules
- NEVER allow recovery on blocked categories
- NEVER compute numbers -- engine handles arithmetic

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
