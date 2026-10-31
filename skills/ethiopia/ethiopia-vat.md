---
name: ethiopia-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Ethiopia VAT return. Standard rate 15%. Turnover Tax abolished under Proclamation 1395/2025. ALWAYS read before handling Ethiopia VAT work.
version: 2.0
jurisdiction: ET
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ethiopia VAT

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
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

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from CBE (Commercial Bank of Ethiopia), Dashen Bank, Awash Bank, Bank of Abyssinia, Wegagen, or any Ethiopian bank.

- **R-ET-1 -- Investment incentive** — Investment incentive may exempt capital goods imports. Verify certificate. Escalate. (Trigger: EIC certificate holder)

## Section 3 -- Supplier pattern library

**Supplier pattern library**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CBE, COMMERCIAL BANK OF ETHIOPIA | EXCLUDE | Exempt financial |
| DASHEN BANK | EXCLUDE | Same |
| AWASH BANK, BANK OF ABYSSINIA | EXCLUDE | Same |
| WEGAGEN, UNITED BANK | EXCLUDE | Same |
| MOR, MINISTRY OF REVENUES | EXCLUDE | Tax payment |
| CUSTOMS, ECC | Check for import VAT |  |
| PENSION, SOCIAL SECURITY | EXCLUDE |  |
| EEPCO, EEU | Domestic 15% | Electricity |
| ETHIO TELECOM | Domestic 15% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Reverse charge 15% | Non-resident |

## Section 4 -- Worked examples

### Example 1 -- Standard sale

ETB 100,000 net. Output VAT = ETB 15,000 (15%).

### Example 2 -- Purchase from unregistered supplier

Goods ETB 10,000 from market trader. No VAT invoice. Input VAT = 0. Pure cost.

## Section 5 -- Classification rules

- **Standard rate classification** — 15% standard. 0% exports, gold to NBE, diplomatic supplies. Exempt: residential rental, financial services, medical, education, religious, postal, electricity/water/kerosene (domestic), bread/milk, military.
- **TOT abolished; below-threshold treatment** — TOT abolished. Below-threshold businesses: Category B income tax (2%-9% gross).

## Section 6 -- VAT return form

Output: Boxes 1-8 (15% sales, zero-rated, exempt, total, output VAT, reverse charge output, adjustments, total output).

Input: Boxes 9-15 (local purchases, imports, input local, input imports, reverse charge input, adjustments, total input).

Net: Boxes 16-18 (net, credit b/f, net payable).

## Section 7 -- Reverse charge

- **Non-resident services reverse charge** — Non-resident services: self-assess 15%. Net zero. Proclamation 285/2002 Art. 10.  _(Proclamation 285/2002 Art. 10)_
- **Import of goods VAT** — Import of goods: VAT at customs. Recoverable if for taxable supplies.

## Section 8 -- Deductibility and blocked input

- **Blocked input categories** — Blocked (Art. 21): entertainment, motor vehicles < 10 seats (unless transport for hire), personal/non-business use, purchases from non-registered suppliers (no valid invoice).  _(Art. 21)_
- **Cash register receipt threshold for retail** — ETB 500 ETB (Cash register receipts acceptable for retail up to this amount)
- **Partial exemption apportionment** — Partial exemption: Art. 20(3). Turnover-based apportionment.  _(Art. 20(3))_

## Section 9 -- Filing, deadlines, and penalties

- **Filing frequency and deadline** — Monthly. Last day of following month.
- **Late filing penalty** — ETB 5,000/month ETB per month
- **Late payment penalty** — 2%/month % per month
- **Failure to register penalty** — 100% of tax due %
- **Understatement penalty** — 10% %

## Section 10 -- Edge cases, test suite, and escalation

EC1 -- Cloud SaaS. Reverse charge 15%. Net zero.

EC2 -- Unregistered supplier. No input recovery.

EC3 -- Coffee export. Zero-rated. Input recoverable.

EC4 -- Threshold crossed. Must register for VAT.

EC5 -- Construction + WHT. 2% WHT is income tax, not VAT. VAT still 15%.

EC6 -- Investment incentive. Capital goods import may be exempt. Escalate.

EC7 -- Business gifts. Deemed supply. Output 15% on market value.

Test 1 -- ETB 100K sale. Output ETB 15K.

Test 2 -- ETB 50K purchase + ETB 7.5K VAT. Recoverable.

Test 3 -- UK consulting ETB 200K. Output 30K, input 30K. Net zero.

Test 4 -- Flower export ETB 5M. Zero-rated.

Test 5 -- Entertainment ETB 30K + VAT 4.5K. Blocked.

Test 6 -- Unregistered purchase ETB 10K. No input.

Test 7 -- Below threshold ETB 1.5M. Not required to register. Category B tax.

Test 8 -- Sedan ETB 2M + VAT 300K. Blocked.

Out of scope: CIT 30% (mining 25%), PAYE 0%-35%, pension 7%+7%.

### Prohibitions

- NEVER allow input recovery without valid VAT invoice from registered supplier
- NEVER reference Turnover Tax -- it is abolished
- NEVER allow recovery on blocked categories
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
