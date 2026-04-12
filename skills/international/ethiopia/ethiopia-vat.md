---
name: ethiopia-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Ethiopia VAT return. Standard rate 15%. Turnover Tax abolished under Proclamation 1395/2025. ALWAYS read before handling Ethiopia VAT work.
version: 2.0
---

# Ethiopia VAT Return Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Country | Ethiopia |
| Standard rate | 15% |
| Zero rate | 0% (exports, gold to NBE) |
| Filing portal | https://etax.mor.gov.et |
| Authority | Ministry of Revenues (MOR) |
| Currency | ETB (Ethiopian Birr) |
| Filing frequency | Monthly |
| Deadline | Last day of following month |
| Registration threshold | ETB 2,000,000 (Proclamation 1341/2024) |
| Voluntary registration | ETB 1,000,000-2,000,000 |
| Turnover Tax | ABOLISHED (Proclamation 1395/2025) |
| Primary legislation | VAT Proclamation 1341/2024 (replacing 285/2002) |
| Contributor | Open Accounting Skills Registry |
| Validated by | Pending |
| Last research update | April 2026 |

---

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from CBE (Commercial Bank of Ethiopia), Dashen Bank, Awash Bank, Bank of Abyssinia, Wegagen, or any Ethiopian bank.

**R-ET-1 -- Investment incentive.** Trigger: EIC certificate holder. Message: "Investment incentive may exempt capital goods imports. Verify certificate. Escalate."

---

## Section 3 -- Supplier pattern library

| Pattern | Treatment | Notes |
|---|---|---|
| CBE, COMMERCIAL BANK OF ETHIOPIA | EXCLUDE | Exempt financial |
| DASHEN BANK | EXCLUDE | Same |
| AWASH BANK, BANK OF ABYSSINIA | EXCLUDE | Same |
| WEGAGEN, UNITED BANK | EXCLUDE | Same |
| MOR, MINISTRY OF REVENUES | EXCLUDE | Tax payment |
| CUSTOMS, ECC | Check for import VAT | |
| PENSION, SOCIAL SECURITY | EXCLUDE | |
| EEPCO, EEU | Domestic 15% | Electricity |
| ETHIO TELECOM | Domestic 15% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Reverse charge 15% | Non-resident |

---

## Section 4 -- Worked examples

### Example 1 -- Standard sale

ETB 100,000 net. Output VAT = ETB 15,000 (15%).

### Example 2 -- Purchase from unregistered supplier

Goods ETB 10,000 from market trader. No VAT invoice. Input VAT = 0. Pure cost.

---

## Section 5 -- Classification rules

15% standard. 0% exports, gold to NBE, diplomatic supplies. Exempt: residential rental, financial services, medical, education, religious, postal, electricity/water/kerosene (domestic), bread/milk, military.

TOT abolished. Below-threshold businesses: Category B income tax (2%-9% gross).

---

## Section 6 -- VAT return form

Output: Boxes 1-8 (15% sales, zero-rated, exempt, total, output VAT, reverse charge output, adjustments, total output).

Input: Boxes 9-15 (local purchases, imports, input local, input imports, reverse charge input, adjustments, total input).

Net: Boxes 16-18 (net, credit b/f, net payable).

---

## Section 7 -- Reverse charge

Non-resident services: self-assess 15%. Net zero. Proclamation 285/2002 Art. 10.

Import of goods: VAT at customs. Recoverable if for taxable supplies.

---

## Section 8 -- Deductibility and blocked input

Blocked (Art. 21): entertainment, motor vehicles < 10 seats (unless transport for hire), personal/non-business use, purchases from non-registered suppliers (no valid invoice).

Cash register receipts acceptable for retail up to ETB 500.

Partial exemption: Art. 20(3). Turnover-based apportionment.

---

## Section 9 -- Filing, deadlines, and penalties

Monthly. Last day of following month. Late filing: ETB 5,000/month. Late payment: 2%/month. Failure to register: 100% of tax due. Understatement: 10%.

---

## Section 10 -- Edge cases, test suite, and escalation

**EC1 -- Cloud SaaS.** Reverse charge 15%. Net zero.
**EC2 -- Unregistered supplier.** No input recovery.
**EC3 -- Coffee export.** Zero-rated. Input recoverable.
**EC4 -- Threshold crossed.** Must register for VAT.
**EC5 -- Construction + WHT.** 2% WHT is income tax, not VAT. VAT still 15%.
**EC6 -- Investment incentive.** Capital goods import may be exempt. Escalate.
**EC7 -- Business gifts.** Deemed supply. Output 15% on market value.

**Test 1** -- ETB 100K sale. Output ETB 15K.
**Test 2** -- ETB 50K purchase + ETB 7.5K VAT. Recoverable.
**Test 3** -- UK consulting ETB 200K. Output 30K, input 30K. Net zero.
**Test 4** -- Flower export ETB 5M. Zero-rated.
**Test 5** -- Entertainment ETB 30K + VAT 4.5K. Blocked.
**Test 6** -- Unregistered purchase ETB 10K. No input.
**Test 7** -- Below threshold ETB 1.5M. Not required to register. Category B tax.
**Test 8** -- Sedan ETB 2M + VAT 300K. Blocked.

Out of scope: CIT 30% (mining 25%), PAYE 0%-35%, pension 7%+7%.

### Prohibitions

- NEVER allow input recovery without valid VAT invoice from registered supplier
- NEVER reference Turnover Tax -- it is abolished
- NEVER allow recovery on blocked categories
- NEVER compute numbers -- engine handles arithmetic

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com).
