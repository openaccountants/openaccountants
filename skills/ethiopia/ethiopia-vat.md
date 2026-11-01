---
name: ethiopia-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for an Ethiopia VAT return. Standard rate 15%. Turnover Tax abolished under Proclamation 1395/2025. ALWAYS read before handling Ethiopia VAT work.
version: 2.1
jurisdiction: ET
tax_year: 2026
last_updated: 2026-11-01
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ethiopia VAT

## Who this applies to

Persons with taxable supplies in Ethiopia, importers, and registered persons, government entities and large unregistered persons receiving reverse charged services (Proc. 1341/2024 art. 8). The accounting period is each calendar month, with Nehase and Pagumen treated as one (art. 2).

## Rates, bands and thresholds

| Item | Amount | Tax year | Official URL |
|---|---|---|---|
| Standard rate (art. 8(2)) | 15% | 2026 | https://www.hopr.gov.et/Resources/ViewFiles?path=%2Fadmin%2FFiles%2F2026%5C1%5C21%5C237b0abc-d9d2-4749-96a8-7cf2ae7dbcf91341-2016%20%E1%8B%A8%E1%89%B0%E1%8C%A8%E1%88%9B%E1%88%AA%20%E1%8A%A5%E1%88%B4%E1%89%B5%20%E1%89%B3%E1%8A%AD%E1%88%B5%20%E1%8A%A0%E1%8B%8B%E1%8C%85.pdf |
| Zero rate, Schedule 1 supplies, with proof kept (arts 8(2), 9) | 0% | 2026 | same |
| Compulsory registration, 12 calendar months, actual or expected; related persons may count (art. 12). A Ministry directive may change it | ETB 2,000,000 | 2026 | same |
| Voluntary registration, annual supplies above (art. 13(2)) | ETB 1,000,000 | 2026 | same |
| Government buyer withholds (art. 62) | 50% of the VAT | 2026 | same |
| Input credit in full at B/C of 0.95 or more; none below 0.05 (art. 29(3)) | 0.95 / 0.05 | 2026 | same |

## The base

Output tax runs on the value of the supply. Blocked input: passenger vehicles and their parts and repairs unless dealt in or hired out; entertainment with the listed exceptions; sporting, social and recreational club membership (art. 30). Mixed inputs: A x B / C (art. 29(2)). Capital goods sales and whole-business sales are ignored for the threshold (art. 12(4)). Excess credit carries forward (art. 48). Over 50% zero-rated supplies: refund within one calendar month of filing (art. 49(1)).

## Deadlines and filing

1. Register within 7 days of becoming liable, on the approved form (art. 12(6)); the form is on the [Ministry page](https://www.mor.gov.et/forms).
2. File by the last day of the following calendar month, even with nothing due (art. 58(1), (2)).
3. Pay by the same date (art. 59(1)).
4. Large unregistered persons and unregistered government entities declare reverse charge monthly by the same date (art. 58(3)).
5. The Ministry publishes a VAT declaration form, a VAT and reverse charge form and a VAT withholding declaration.

## Penalties and interest

ETB 100,000 for each listed failure, such as not displaying the certificate or not issuing a credit note (art. 66(1)). ETB 50,000 for each wrong tax invoice or note (art. 66(2)). ETB 50,000 for failing the reverse charge notice (arts 65, 66(3)). General penalties: see [payroll](ethiopia-payroll.md#penalties-and-interest). The old 100% failure-to-register figure and the ETB 5,000 late-filing figure were not found in the law read and are withdrawn.

## Cross-border points

Services from a person outside Ethiopia with no fixed place of business are reverse charged on registered persons, government entities and large unregistered persons (art. 6). Foreign suppliers issue an electronic invoice (Regulation 570/2025). The Tax Authority may require security and then a VAT representative (art. 64). A registered person with no fixed place of business gets no input credit (art. 30(3)).

## Two worked examples that recompute

Simple case: a sale of ETB 100,000.

```oa-check
name: Standard sale
inputs:
  v: 100000
steps:
  - vat: v * 0.15
expected:
  vat: 15000.00
```

Edge case: mixed inputs of ETB 30,000 with taxable supplies of 800,000 out of 1,000,000.

```oa-check
name: Mixed input credit
inputs:
  a: 30000
  b: 800000
  c: 1000000
steps:
  - credit: a * b / c
expected:
  credit: 24000.00
```

## Ask the client first

- Taxable supplies in the last 12 months, and expected?
- Related persons?
- Exports or other zero-rated supplies?
- Any exempt supplies?
- Any government customers or foreign suppliers?

## Sources

| Source | URL | Read on | What was read |
|---|---|---|---|
| Value Added Tax Proclamation 1341/2024, Federal Negarit Gazette, 21 August 2024 | https://www.hopr.gov.et/Resources/ViewFiles?path=%2Fadmin%2FFiles%2F2026%5C1%5C21%5C237b0abc-d9d2-4749-96a8-7cf2ae7dbcf91341-2016%20%E1%8B%A8%E1%89%B0%E1%8C%A8%E1%88%9B%E1%88%AA%20%E1%8A%A5%E1%88%B4%E1%89%B5%20%E1%89%B3%E1%8A%AD%E1%88%B5%20%E1%8A%A0%E1%8B%8B%E1%8C%85.pdf | 2026-11-01 | Arts 2, 6, 8 to 13, 29, 30, 47 to 49, 58, 59, 62, 64 to 66, 71 to 75 read; the copy has no Schedules |
| Federal Tax Administration Proclamation 983/2016, Amharic consolidated print | https://www.lawethiopia.com/images/federal_proclamation/proclamations_by_number/983.pdf | 2026-11-01 | Penalty articles and art. 37 read in Amharic |
| Ministry of Revenues forms list | https://www.mor.gov.et/forms | 2026-11-01 | Titles of the published forms read; the form boxes were not read |

Not yet confirmed: Schedules 1, 2 and 3 are absent from the copy read, so the zero-rated and exempt lists in the retained notes are not confirmed; Directive 1104/2025 on registration was not read, and any change to the ETB 2,000,000 threshold must be checked there; the definition of a large unregistered person; box numbers; articles carried in the notes from the repealed Proc. 285/2002; the ETB 500 receipt limit; the 2% a month, 10% figures in the notes are replaced by the general penalty table.

### Retained working notes from the earlier version (not re-read against the law)

### Section 1 -- Quick reference

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

### Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from CBE (Commercial Bank of Ethiopia), Dashen Bank, Awash Bank, Bank of Abyssinia, Wegagen, or any Ethiopian bank.

- **R-ET-1 -- Investment incentive**, Investment incentive may exempt capital goods imports. Verify certificate. Escalate. (Trigger: EIC certificate holder)

### Section 3 -- Supplier pattern library

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

### Section 4 -- Worked examples

#### Example 1 -- Standard sale

ETB 100,000 net. Output VAT = ETB 15,000 (15%).

#### Example 2 -- Purchase from unregistered supplier

Goods ETB 10,000 from market trader. No VAT invoice. Input VAT = 0. Pure cost.

### Section 5 -- Classification rules

- **Standard rate classification**, 15% standard. 0% exports, gold to NBE, diplomatic supplies. Exempt: residential rental, financial services, medical, education, religious, postal, electricity/water/kerosene (domestic), bread/milk, military.
- **TOT abolished; below-threshold treatment**, TOT abolished. Below-threshold businesses: Category B income tax (2%-9% gross).

### Section 6 -- VAT return form

Output: Boxes 1-8 (15% sales, zero-rated, exempt, total, output VAT, reverse charge output, adjustments, total output).

Input: Boxes 9-15 (local purchases, imports, input local, input imports, reverse charge input, adjustments, total input).

Net: Boxes 16-18 (net, credit b/f, net payable).

### Section 7 -- Reverse charge

- **Non-resident services reverse charge**, Non-resident services: self-assess 15%. Net zero. Proclamation 285/2002 Art. 10.  _(Proclamation 285/2002 Art. 10)_
- **Import of goods VAT**, Import of goods: VAT at customs. Recoverable if for taxable supplies.

### Section 8 -- Deductibility and blocked input

- **Blocked input categories**, Blocked (Art. 21): entertainment, motor vehicles < 10 seats (unless transport for hire), personal/non-business use, purchases from non-registered suppliers (no valid invoice).  _(Art. 21)_
- **Cash register receipt threshold for retail**, ETB 500 ETB (Cash register receipts acceptable for retail up to this amount)
- **Partial exemption apportionment**, Partial exemption: Art. 20(3). Turnover-based apportionment.  _(Art. 20(3))_

### Section 9 -- Filing, deadlines, and penalties

- **Filing frequency and deadline**, Monthly. Last day of following month.

### Section 10 -- Edge cases, test suite, and escalation

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

#### Prohibitions

- NEVER allow input recovery without valid VAT invoice from registered supplier
- NEVER reference Turnover Tax -- it is abolished
- NEVER allow recovery on blocked categories
- NEVER compute numbers -- engine handles arithmetic

> **General reference only.** This document does not constitute tax, legal, or financial advice. Verify figures against the cited primary sources or with a licensed professional before relying on them.
