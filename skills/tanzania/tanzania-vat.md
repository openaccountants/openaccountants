---
name: tanzania-vat
description: Use this skill whenever asked to prepare, review, or classify transactions for a Tanzania VAT return. Standard rate 18% (16% reduced for non-VAT-registered B2C electronic payments from Sep 2025). EAC customs union but no common VAT. Withholding VAT 3% goods / 6% services from July 2025. ALWAYS read before handling Tanzania VAT work.
version: 2.0
jurisdiction: TZ
tax_year: 2025
last_updated: 2026-07-13
authored_by: Baraka Cassian, CPA, CA, CTA
reviewed_by: Baraka Cassian
review_status: current
trust_label: Checked by Baraka Cassian
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Tanzania VAT

## Tanzania VAT Return Skill v2.0

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Baraka Cassian** on 2026-06-12.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### tanzania-vat

- **Standard VAT rate (Mainland)** — 18%  _(Value Added Tax Act, Cap 148, s.5)_
- **Reduced rate - B2C electronic payments (Mainland)** — 16% on standard-rated supplies to persons NOT VAT-registered where payment is made via bank or electronic payment system approved by the Commissioner General  _(Value Added Tax Act, Cap 148 (as amended by Finance Act 2025 (in force 1 Jul 2025 unless stated)))_
- **Standard VAT rate (Zanzibar)** — 15% (18% for banking, postal, telecommunication, insurance and digital services)  _(Zanzibar VAT Act (administered by ZRA))_
- **Zero rate** — 0% - exports of goods, certain exported services, international transport  _(Value Added Tax Act, Cap 148, Schedule (zero-rated supplies))_
- **VAT registration threshold (Mainland)** — Annual taxable turnover above TZS 200,000,000  _(Value Added Tax Act, Cap 148, s.28 (threshold per Finance Act 2023))_
- **VAT registration threshold (Zanzibar)** — TZS 100,000,000  _(Zanzibar VAT Act)_
- **Mandatory registration regardless of turnover** — Professional service providers (e.g. lawyers, accountants) and government entities/institutions carrying on economic activities  _(Value Added Tax Act, Cap 148, s.28)_
- **Non-resident B2C electronic services** — Simplified VAT registration; NO registration threshold; charge 18% on B2C supplies to Mainland consumers  _(Value Added Tax Act, Cap 148 (non-resident electronic services provisions); VAT (Registration of Non-Resident Electronic Service Suppliers) Regulations)_
- **VAT return frequency and deadline** — Monthly; due on the 20th day of the following month, regardless of whether the 20th falls on a weekend or public holiday  _(Value Added Tax Act, Cap 148, s.66 (deadline rule per Finance Act 2025 (in force 1 Jul 2025 unless stated)))_
- **Withholding VAT - introduction** — Designated agents (MoF, government institutions retaining own-source revenue, CG-appointed VAT-registered persons) must withhold part of the VAT on taxable supplies  _(Value Added Tax Act, Cap 148 (as amended by Finance Act 2025 (in force 1 Jul 2025 unless stated)))_
- **Withholding VAT - rates** — Goods: withhold 3 percentage points of the 18% VAT (supplier receives 15%); Services: withhold 6 percentage points (supplier receives 12%)  _(Value Added Tax Act, Cap 148 (as amended by Finance Act 2025 (in force 1 Jul 2025 unless stated)))_
- **Withholding VAT - remittance and credit** — Agent remits withheld VAT to TRA by the 20th of the following month and issues a VAT Withholding Certificate; supplier claims withheld amount as credit in its VAT return  _(Value Added Tax Act, Cap 148 (as amended by Finance Act 2025 (in force 1 Jul 2025 unless stated)))_
- **Input tax claim time limit** — 6 months, running from the date of the fiscal receipt  _(Value Added Tax Act, Cap 148, s.69)_
- **Pre-registration input tax** — VAT incurred in the 6 months before registration claimable no later than the third VAT return after registration  _(Value Added Tax Act, Cap 148)_
- **Partial exemption thresholds** — Taxable supplies >90% of total: full input credit; <10%: no input credit; 10%-90%: apportion (average method or direct attribution)  _(Value Added Tax Act, Cap 148, s.70 (partial input tax credit))_
- **Reverse charge on imported services** — Registered person accounts for output VAT on imported services only where exempt supplies are 10% or more of total supplies  _(Value Added Tax Act, Cap 148, imported services provisions)_
- **VAT refunds** — Remaining credit claimable 6 months after refund first due (all intervening returns filed); claim must be supported by an auditor's certificate of genuineness; consistent-refund businesses (e.g. exporters) may apply to lodge monthly  _(Value Added Tax Act, Cap 148, s.80-83 (refunds))_
- **VAT deferment on capital goods** — Deferment of VAT on imported capital goods CEASES to apply from 30 June 2026  _(Value Added Tax Act, Cap 148 (sunset per Finance Act 2025 (in force 1 Jul 2025 unless stated)))_
- **Fiscal receipts / EFD** — Fiscal receipt mandatory for every supply; includes receipts from fiscal devices (EFD/EFDMS), Government e-Payment Gateway (GePG) and other CG-approved electronic systems  _(Value Added Tax Act, Cap 148; Tax Administration (Electronic Fiscal Devices) Regulations)_
- **Blocked input tax** — No credit for: entertainment; membership of sporting/social/recreational clubs; spare parts and repair/maintenance of passenger vehicles  _(Value Added Tax Act, Cap 148, s.68 restrictions)_
- **Key exempt supplies (selected)** — Agricultural implements/inputs and basic food; livestock; medicine/pharmaceuticals; health care; education services/materials; financial services; insurance (health, life, aircraft, workers comp, crop, livestock); residential rent; vacant land; un-bottled water; specified petroleum products; gaming supply; solar equipment; passenger transport (excl. taxis, rental cars, boat charters)  _(Value Added Tax Act, Cap 148, Schedule (exempt supplies))_
- **Natural gas for CNG vehicle fuelling** — Exempt from VAT from 1 Jul 2025 to 30 Jun 2028 (supply of natural gas for conversion to CNG for motor vehicles)  _(Value Added Tax Act, Cap 148 (as amended by Finance Act 2025 (in force 1 Jul 2025 unless stated)))_
- **Currency of VAT accounting** — TZS  _(Tax Administration Act, Cap 438)_
- **Filing portal** — TRA online Taxpayer Portal (e-filing)  _(TRA systems)_
- **Default rate where supply classification unknown (agent default)** — 18% standard rate  _(Proposed processing default - not law)_
- **Default input claim where documentation unknown (agent default)** — Not deductible until a valid fiscal receipt is sighted  _(Proposed processing default - not law; consistent with VAT Act fiscal receipt requirement)_

## Section 1 -- Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
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

## Section 2 -- Required inputs and refusal catalogue

**Minimum viable** -- bank statement. Acceptable from CRDB, NMB (National Microfinance Bank), Stanbic TZ, Standard Chartered TZ, NBC, or any Tanzanian bank.

- **R-TZ-1 -- Mining** — Mining has specific provisions under Mining Act 2010. Escalate.  _(Mining Act 2010)_

## Section 3 -- Supplier pattern library

**Supplier pattern library**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CRDB | EXCLUDE | Exempt financial |
| NMB, NATIONAL MICROFINANCE | EXCLUDE | Same |
| STANBIC TZ, NBC | EXCLUDE | Same |
| TRA, TANZANIA REVENUE | EXCLUDE | Tax payment |
| CUSTOMS | Check for import VAT |  |
| NSSF, PPF | EXCLUDE | Social security |
| TANESCO | Domestic 18% | Electricity |
| DAWASA | Domestic 18% | Water |
| VODACOM TZ, AIRTEL TZ, TIGO, HALOTEL | Domestic 18% | Telecoms |
| GOOGLE, MICROSOFT, AWS | Reverse charge 18% | Non-resident |

## Section 4 -- Worked examples

### Example 1 -- Standard sale

TZS 10M net. Output VAT = TZS 1.8M (18%).

### Example 2 -- EAC import

Goods from Kenya TZS 20M. VAT 18% at customs = TZS 3.6M. Recoverable. No intra-community mechanism.

## Section 5 -- Classification rules

- **Classification rules** — 18% standard (16% for B2C electronic payments to unregistered, from Sep 2025). 0% exports, agricultural inputs, diplomatic, SEZ. Exempt: unprocessed foodstuffs, financial, medical, education, residential rental, life insurance, public transport, agricultural equipment, water (public utilities), petroleum (fuel levy).

## Section 6 -- VAT return form (ITX222.01.E)

Output: A1-A7 (18% sales, zero-rated, exempt, total, output VAT, adjustments, total output).

Input: B1-B7 (local purchases, imports, input local, input imports, total input, adjustments, net input).

Net: C1-C3 (net, credit b/f, net payable).

## Section 7 -- Reverse charge, withholding VAT, and imports

- **Reverse charge** — Reverse charge: non-resident services. Self-assess 18%. Net zero.  _(VAT Act s.16)_
- **Withholding VAT (from July 2025)** — Designated agents withhold 3% of VAT on goods, 6% on services. Remit by 20th. Supplier needs certificate to claim credit.
- **EAC imports** — VAT at border, no intra-community mechanism.

## Section 8 -- Deductibility and blocked input

- **Blocked input tax categories** — Blocked (s.64): entertainment, vehicles < 13 seats (unless taxi/hire/driving instruction), clubs, personal use, non-taxable supply purchases.  _(s.64)_
- **De minimis for exempt** — If < 5% of total, full recovery may be allowed. Reviewer confirm.
- **Deemed supplies** — Non-business use, gifts > TZS 100,000, cessation with stock.

## Section 9 -- Filing, deadlines, and penalties

- **Filing and penalties** — Monthly, 20th. Late filing: 1%/month (max 100%), min TZS 150K. Late payment: BoT rate + 5%, daily.

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
