---
name: ng-vat-return
description: Use this skill whenever asked about Nigerian VAT returns for self-employed individuals or small businesses. Trigger on phrases like "Nigeria VAT", "NRS VAT", "FIRS VAT", "7.5% VAT", "VAT return Nigeria", "value added tax Nigeria", or any question about VAT computation or filing for businesses in Nigeria. Covers the 7.5% standard rate, zero-rated and exempt supplies, small-business exemption threshold (gross annual turnover NGN 100M or less and total fixed assets NGN 250M or less, excluding professional services and petroleum operations), monthly filing to NRS, and input/output VAT computation. ALWAYS read this skill before touching any Nigerian VAT work.
version: 2.1
jurisdiction: NG
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - vat-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
---

# NG VAT Return

## Nigeria VAT Return -- Self-Employed Skill v2.1

## Rates and thresholds

Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### ng-vat-return

- **Standard VAT rate** — 7.5%  _(NIGERIAN TAX ACT 2025)_
- **Zero rate: basic food items, medical and pharmaceutical products, medical services and equipment, educational books and tuition, specified agricultural inputs and livestock, GENCO/TCN electricity, exported goods excluding oil and gas, exported services and exported incorporeal property** — 0%  _(Nigeria Tax Act 2025 s. 186)_
- **Exempt supplies: oil and gas exports, crude oil and feed gas, humanitarian donor-funded project goods (pay and claim refund), baby products, locally manufactured sanitary towels/pads/tampons, military hardware, shared passenger road transport, agricultural equipment, EPZ/FTZ approved-activity supplies, diplomatic supplies, educational plays, land or building (including interest in land or building), money/stakes/securities (including interest), government licences and assistive devices** — Exempt (no VAT)  _(Nigeria Tax Act 2025 s. 185(1))_
- **Pre-2020 (superseded) VAT rate — no longer applicable** — 5%  _(Finance Act 2020)_
- **Small-business VAT exemption threshold** — Gross annual turnover of NGN 100,000,000 or less and total fixed assets not more than NGN 250,000,000; businesses providing professional services and companies in petroleum operations are excluded  _(Nigeria Tax Administration Act 2025 ss. 22(4)-(5), (9), 147)_
- **Filing frequency** — Monthly  _(NIGERIAN TAX ACT 2025)_
- **VAT return filing deadline** — 21st of the following month  _(NIGERIAN TAX ACT 2025)_
- **VAT payment deadline** — Same as filing deadline — 21st of the following month  _(NIGERIAN TAX ACT 2025)_
- **Nil returns — required even with no transactions** — Must be filed  _(NIGERIAN TAX ACT 2025)_
- **Tax authority and service entry** — Nigeria Revenue Service (NRS) official service entry (nrs.gov.ng)  _(Nigeria Tax Administration Act 2025 ss. 3, 22)_
- **Penalty — failure to register (first month)** — NGN 50,000  _(NIGERIAN TAX ACT 2025)_
- **Penalty — failure to register (each subsequent month)** — NGN 25,000 per subsequent month  _(NIGERIAN TAX ACT 2025)_
- **Penalty: failure to file returns (or knowingly filing incomplete/inaccurate returns)** — NGN 100,000 for the first month and NGN 50,000 for each subsequent month in which the failure continues  _(Nigeria Tax Administration Act 2025 s. 101)_
- **Penalty: late payment** — 10% of the unpaid tax, plus interest at the prevailing CBN Monetary Policy Rate (MPR) plus a spread determined by the Minister for Naira remittances, or SOFR plus a spread determined by the Minister for foreign currency remittances  _(Nigeria Tax Administration Act 2025 s. 65(1))_
- **Penalty: failure to process a taxable supply through the fiscalisation system** — NGN 200,000 plus 100% of the tax due, plus interest at the prevailing CBN MPR per annum  _(Nigeria Tax Administration Act 2025 s. 104)_
- **Penalty: failure to collect, deduct or withhold VAT** — 40% administrative penalty on the amount not collected, deducted or withheld  _(Nigeria Tax Administration Act 2025 s. 105)_
- **Penalty: failure to remit collected/withheld VAT or failure to self-account** — Unpaid principal tax plus 10% per annum administrative penalty and interest at the prevailing CBN MPR (conviction: up to 3 years imprisonment, or fine of at least principal plus penalty up to 50%, or both)  _(Nigeria Tax Administration Act 2025 s. 107)_
- **VAT invoice retention period (minimum)** — 6 years  _(NIGERIAN TAX ACT 2025)_
- **Output VAT formula** — OUTPUT VAT = TAXABLE SALES × VAT RATE  _(NIGERIAN TAX ACT 2025)_
- **Net VAT formula** — NET VAT = OUTPUT VAT - INPUT VAT  _(NIGERIAN TAX ACT 2025)_
- **Input VAT restriction — exempt supplies** — Under the Nigeria Tax Act (NTA), you cannot recover or offset Input VAT incurred on purchases that directly relate to VAT-exempt supplies. Because you do not charge Output VAT on exempt sales, any Input VAT paid becomes a non-recoverable cost and should be expensed or capitalized.  _(NIGERIAN TAX ACT 2025)_
- **Input VAT claim — invoice requirement** — Not claimable without a valid VAT invoice  _(NIGERIAN TAX ACT 2025)_
- **Input VAT apportionment method — residual (no direct attribution)** — Taxable revenue / Total revenue x Total residual input VAT  _(NIGERIAN TAX ACT 2025)_
- **Default VAT rate when supply classification is unknown** — 7.5% (standard-rated)  _(NIGERIAN TAX ACT 2025)_
- **Default for mixed supply apportionment — disputed portion** — Under the Nigeria Tax Act (NTA), the default for mixed supply apportionment requires separating considerations based on market value or FIRS-approved methods. For disputed mixed supply portions, the taxpayer is advised to apportion using a fair and reasonable method, pending resolution. Taxpayers should pay output VAT on the non-disputed standard-rated portion to avoid penalties and interest  _(NIGERIAN TAX ACT 2025)_
- **VAT self-accounting rate — non-resident digital services not charged by supplier** — 7.5%  _(NIGERIAN TAX ACT 2025)_
- **Currency of assessment and payment for foreign currency invoices** — Tax is assessed in the currency of transaction and tax assessed in a currency other than Naira must be paid in that currency  _(Nigeria Tax Administration Act 2025 s. 39(1)-(2))_
- **Primary legislation reference** — Nigeria Tax Act 2025 (Act No. 7 of 2025, effective 1 January 2026; ss. 143-157, 185-188; repealed VATA Cap. V1 LFN 2004 under s. 195(j)) and Nigeria Tax Administration Act 2025 (Act No. 5 of 2025; ss. 3, 22-23, 31, 39, 56, 65, 100-107, 127, 147)
- **Mandatory VAT invoice fields** — Supplier Tax ID, supplier name and address, sequential invoice number, supplier incorporation or business registration number as applicable, date of supply, name of purchaser or client, gross amount of transaction, and VAT charged and rate  _(Nigeria Tax Act 2025 s. 152(1))_
- **Bank interest classification** — Exempt (money, stakes or securities including interest)  _(Nigeria Tax Act 2025 s. 185(1)(m))_

## Section 1 -- Quick Reference

**Section 1 Quick Reference**

| Field | Value |
| --- | --- |
| Country | Nigeria (Federal Republic of Nigeria) |
| Tax | Value Added Tax (VAT) at 7.5% |
| Currency | Currency of transaction (NTAA 2025 s. 39) |
| Primary legislation | Nigeria Tax Act 2025 (ss. 143-157, 185-188) and Nigeria Tax Administration Act 2025 (ss. 3, 22-23, 31, 39, 56, 65, 100-107, 127, 147) |
| Supporting legislation | Preserved compatible subsidiary regulations (NTA 2025 s. 198) |
| Tax authority | Nigeria Revenue Service (NRS) |
| Filing portal | NRS official service entry (nrs.gov.ng) |
| Filing frequency | Monthly |
| Filing deadline | 21st of the following month (14th for withheld, collected or self-accounted VAT under NTA s. 154(4)) |
| Contributor | Open Accountants Community |
| Skill version | 2.1 |

### Rate Table

**Rate Table**

| Rate | Application |
| --- | --- |
| 7.5% | Standard rate on all taxable supplies (effective 1 February 2020) |
| 0% | Basic food items, medical and pharmaceutical products, medical services and equipment, educational books and tuition, specified agricultural inputs and livestock, GENCO/TCN electricity, exported goods excluding oil and gas, exported services and exported incorporeal property (NTA 2025 s. 186) |
| Exempt | Oil and gas exports, crude oil and feed gas, humanitarian donor project goods (pay and refund), baby products, locally made sanitary products, military hardware, shared passenger road transport, agricultural equipment, EPZ/FTZ approved supplies, diplomatic supplies, educational plays, land or building (including interest), money/stakes/securities (including interest), government licences and assistive devices (NTA 2025 s. 185(1)) |

### Key Thresholds

**Key Thresholds**

| Item | Amount |
| --- | --- |
| Small-business VAT exemption | Gross annual turnover NGN 100,000,000 or less and total fixed assets NGN 250,000,000 or less, excluding professional services and petroleum operations (NTAA 2025 ss. 22(4)-(5), (9), 147) |
| Filing frequency | Monthly for all registered persons |
| Nil returns | Required even with no transactions |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Supply classification unknown | Standard-rated at 7.5% |
| Input VAT claim without invoice | Not claimable |
| Mixed supply apportionment unknown | No input credit on disputed portion |
| Non-resident service VAT | Self-account at 7.5% |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the month in CSV, PDF, or pasted text, plus confirmation of VAT registration status and TIN.

**Recommended:** Sales invoices, purchase invoices with VAT shown, prior period returns.

**Ideal:** Complete invoice register, TIN certificate, WHT-VAT documentation (for government supplies).

### Refusal Catalogue

- **R-NG-1 -- Below threshold** — Qualifying small businesses (gross annual turnover of NGN 100,000,000 or less and total fixed assets not more than NGN 250,000,000, excluding businesses providing professional services and companies in petroleum operations) are exempt from VAT registration, charging and monthly filing unless they opt out in writing (NTAA 2025 ss. 22(4)-(5), (9), 147). Stop.
- **R-NG-2 -- International VAT recovery** — Cross-border VAT recovery and transfer pricing implications are outside this skill scope. Escalate.
- **R-NG-3 -- Corporate tax** — Companies Income Tax (CIT) is a separate obligation outside this skill scope.

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns (Credits)

**3.1 Income Patterns (Credits)**

| Pattern | Tax Line | Treatment | Notes |
| --- | --- | --- | --- |
| TRANSFER FROM [client] / INWARD TRF | Taxable supply | Output VAT at 7.5% | Standard client payment |
| POS SETTLEMENT / POS CREDIT | Taxable supply | Revenue | Point-of-sale terminal settlement |
| PAYSTACK PAYOUT / PAYSTACK SETTLEMENT | Taxable supply | Revenue | Paystack payment gateway |
| FLUTTERWAVE PAYOUT / RAVE SETTLEMENT | Taxable supply | Revenue | Flutterwave (Rave) settlement |
| OPAY SETTLEMENT / OPAY PAYOUT | Taxable supply | Revenue | OPay business payout |
| MONNIFY PAYOUT | Taxable supply | Revenue | Monnify settlement |
| INTERSWITCH / QUICKTELLER | Taxable supply | Revenue | Interswitch settlement |
| FGN / STATE GOVT / LGA PAYMENT | Taxable supply | Revenue with WHT-VAT | Government contract -- check withholding |
| INTEREST EARNED / INT CREDIT | Exempt | NOT taxable supply | Bank interest |
| LOAN DISBURSEMENT | EXCLUDE | Not income | Loan proceeds |

### 3.2 Expense Patterns (Debits)

**3.2 Expense Patterns (Debits)**

| Pattern | Expense Category | Treatment | Notes |
| --- | --- | --- | --- |
| OFFICE RENT / COMMERCIAL LEASE | Rent | Reviewer: confirm before claiming input VAT | NTA 2025 s. 185(1)(l) exempts land or building, including an interest in land or building |
| IKEJA ELECTRIC / EKEDC / AEDC / BEDC | Utilities | Input VAT claimable | Electricity distribution companies |
| MTN / GLO / AIRTEL / 9MOBILE | Communications | Business portion input VAT | Mixed use: apportion |
| UBER / BOLT / TAXI | Travel | Input VAT if business | Keep receipts |
| GOOGLE ADS / META / LINKEDIN | Advertising | Input VAT claimable | Digital advertising |
| NRS / FIRS TAX PAYMENT / VAT | EXCLUDE | Tax payment | Not deductible |
| SALARY / PAYROLL | EXCLUDE | Not subject to VAT | Employment cost |
| PERSONAL WITHDRAWAL / SELF TRANSFER | EXCLUDE | Drawings | Not business |

### 3.3 Exempt Supply Indicators

**3.3 Exempt Supply Indicators**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RICE / BEANS / GARRI / YAMS / VEGETABLES | Zero-rated (0%) | Basic food items (NTA 2025 s. 186(a); input VAT recoverable) |
| PHARMACY / HOSPITAL / CLINIC | Zero-rated (0%) | Medical/pharmaceutical products and medical services (NTA 2025 s. 186(b), (l); input VAT recoverable) |
| SCHOOL FEES / UNIVERSITY / COLLEGE | Zero-rated (0%) | Nursery, primary, secondary or tertiary tuition (NTA 2025 s. 186(m); input VAT recoverable) |
| RESIDENTIAL RENT / HOUSE RENT | Exempt | Land or building including interest in land or building (NTA 2025 s. 185(1)(l)) |

## Section 4 -- Worked Examples

### Example 1 -- Standard Monthly Return

**Input:** Taxable supplies NGN 5,000,000. Input VAT from purchases NGN 150,000.

**Reasoning:**
Output VAT: 5,000,000 x 7.5% = NGN 375,000. Input VAT: NGN 150,000 (with valid VAT invoices). VAT payable: 375,000 - 150,000 = NGN 225,000.

**Classification:** VAT payable NGN 225,000.

### Example 2 -- Exporter in Refund Position

**Input:** Zero-rated exports NGN 10,000,000. Input VAT NGN 300,000.

**Reasoning:**
Output VAT: NGN 0 (zero-rated). Input VAT: NGN 300,000. Excess input: carry forward or claim refund from NRS (request must be made within 12 months of the transaction under NTAA 2025 s. 56(2); NRS refunds or sets off within 30 days under s. 56(3)).

**Classification:** Refund/carry forward NGN 300,000.

### Example 3 -- Mixed Supplies (Taxable and Exempt)

**Input:** Taxable supplies NGN 3,000,000, exempt supplies NGN 2,000,000. Total input VAT NGN 200,000 (none directly attributable).

**Reasoning:**
Taxable ratio: 3,000,000 / 5,000,000 = 60%. Claimable input: 200,000 x 60% = NGN 120,000. Output VAT: 3,000,000 x 7.5% = NGN 225,000. VAT payable: 225,000 - 120,000 = NGN 105,000.

**Classification:** VAT payable NGN 105,000. Flag for reviewer on apportionment.

### Example 4 -- Nil Return

**Input:** No supplies or purchases in the month.

**Reasoning:**
Nil return must still be filed by the 21st. VAT payable = NGN 0.

**Classification:** File nil return.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 VAT Return Computation

**5.1 VAT Return Computation**

| Step | Action |
| --- | --- |
| 1 | Total standard-rated output supplies (exclusive of VAT) |
| 2 | Output VAT = Standard-rated supplies x 7.5% |
| 3 | Total exempt supplies (reported, no VAT) |
| 4 | Total zero-rated supplies (reported, 0% VAT) |
| 5 | Total input VAT on purchases (from valid VAT invoices) |
| 6 | Input VAT restriction: no credit for input on exempt supplies |
| 7 | Net VAT = Output VAT - Allowable input VAT |
| 8 | VAT payable to NRS |

### 5.2 VAT Invoice Requirements (NTA 2025 s. 152(1))

- **VAT invoice requirements** — Must show: supplier Tax ID, supplier name and address, sequential invoice number, supplier incorporation or business registration number as applicable, date of supply, name of purchaser or client, gross amount of transaction, and VAT charged and rate (NTA 2025 s. 152(1)). Retention: 6 years minimum after the relevant year of assessment (NTAA 2025 s. 31(5)).

### 5.3 Filing and Payment

**5.3 Filing and Payment**

| Item | Detail |
| --- | --- |
| Filing frequency | Monthly |
| Filing deadline | 21st of the following month |
| Payment deadline | Same as filing deadline |
| Filing authority | Nigeria Revenue Service (NRS; nrs.gov.ng) |
| Nil returns | Must be filed even if no transactions |

### 5.4 Non-Resident Supplies (NTA 2025 ss. 150, 154)

- **Non-resident supplies** — A non-resident person making taxable supplies to Nigeria must register for tax and include VAT on its invoice (NTA 2025 s. 150(1)). Where a non-resident supplies from outside Nigeria to a taxable person in Nigeria, the Nigerian taxable recipient must withhold and remit the VAT to NRS unless an NRS-appointed collector collects it (s. 150(2)-(4)). Withheld, collected or self-accounted VAT is due on or before the 14th day of the following month (NTA 2025 s. 154(4)).

### 5.5 Penalties (NTAA 2025 ss. 65, 100, 101, 104, 105, 107, 127)

**5.5 Penalties (NTAA 2025)**

| Offence | Penalty |
| --- | --- |
| Failure to register (s. 100(1)) | NGN 50,000 first month + NGN 25,000 per subsequent month |
| Failure to file / incomplete or inaccurate return (s. 101) | NGN 100,000 first month + NGN 50,000 per subsequent month |
| Late payment (s. 65(1)) | 10% of unpaid tax + interest at CBN MPR plus Ministerial spread (Naira) or SOFR plus Ministerial spread (foreign currency) |
| Failure to process supply through fiscalisation system (s. 104) | NGN 200,000 + 100% of tax due + interest at CBN MPR per annum |
| Failure to collect, deduct or withhold VAT (s. 105) | 40% administrative penalty on the amount not collected, deducted or withheld |
| Failure to remit collected/withheld VAT or to self-account (s. 107) | Unpaid principal + 10% per annum administrative penalty + CBN MPR interest (plus criminal sanctions on conviction) |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Mixed Taxable and Exempt Supplies

- **Mixed taxable and exempt supplies** — When a business makes both taxable and exempt supplies, input VAT must be apportioned. Directly attributable input follows its supply; residual input is apportioned by revenue ratio. Flag for reviewer.

### 6.2 Non-Resident Services

- **Non-resident services** — Where a non-resident makes taxable supplies from outside Nigeria to a taxable person in Nigeria, the Nigerian recipient must withhold and remit VAT by the 14th day of the following month unless an NRS-appointed collector collects it (NTA 2025 ss. 150(2)-(4), 154(4)). Flag for reviewer when client purchases services from non-residents.

### 6.3 Foreign Currency Invoicing

- **Foreign currency invoicing** — Under NTAA 2025 s. 39(1)-(2), tax is assessed in the currency of transaction and tax assessed in a currency other than Naira must be paid in that currency. Flag foreign-currency invoices for reviewer.

### 6.4 WHT-VAT on Government Contracts

- **WHT-VAT on government contracts** — Government entities may withhold VAT at source. Verify withholding documentation.

## Section 7 -- Working Paper Template

```
NIGERIA VAT WORKING PAPER
Taxpayer: _______________  TIN: ___________
Period: ___________  Month: ___________

A. OUTPUT (SALES)
  A1. Standard-rated supplies (excl. VAT)        ___________
  A2. Output VAT (A1 x 7.5%)                    ___________
  A3. Zero-rated supplies                        ___________
  A4. Exempt supplies                            ___________
  A5. Total supplies                             ___________

B. INPUT (PURCHASES)
  B1. Input VAT on taxable purchases             ___________
  B2. Less: input on exempt supplies             ___________
  B3. Net allowable input VAT                    ___________

C. NET VAT
  C1. VAT payable (A2 - B3)                     ___________
  C2. Or excess credit                           ___________

REVIEWER FLAGS:
  [ ] VAT registration confirmed?
  [ ] All input claims supported by valid VAT invoices?
  [ ] Mixed supply apportionment applied?
  [ ] Nil return filed if no activity?
  [ ] WHT-VAT from government contracts accounted for?
```

## Section 8 -- Bank Statement Reading Guide

### Nigerian Bank Statement Formats

**Nigerian Bank Statement Formats**

| Bank | Format | Key Fields |
| --- | --- | --- |
| GTBank | CSV / PDF | Date, Description, Debit, Credit, Balance |
| First Bank | CSV | Transaction Date, Narration, Debit, Credit, Balance |
| Access Bank | CSV | Date, Description, Debit Amount, Credit Amount, Balance |
| UBA | CSV | Date, Narration, Debit, Credit, Balance |
| Zenith Bank | CSV | Date, Description, Debit, Credit, Balance |
| Fidelity Bank | CSV | Trans Date, Narration, Debit, Credit, Balance |

### Key Nigerian Banking Narrations

**Key Nigerian Banking Narrations**

| Narration | Meaning | Classification Hint |
| --- | --- | --- |
| NIP / NIBSS / INWARD TRF | Interbank transfer in | Potential income |
| POS / SETTLEMENT | POS terminal | Income or expense |
| USSD / MOBILE BANKING | Mobile transfer | Income or expense |
| FGN / MDAs | Government payment | Income with WHT-VAT |
| STAMP DUTY | Stamp duty charge | Exclude |
| VAT / FIRS | Tax payment | Exclude |
| SMS ALERT | Bank charge | Input VAT if business (a bank fee is not money or securities under NTA 2025 s. 185(1)(m)) |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all NIP/NIBSS credits from non-personal sources as potential taxable supplies
2. Apply 7.5% output VAT to all unclassified business income
3. Only claim input VAT where description clearly indicates business purchase
4. Flag all government payments for WHT-VAT review
5. Generate working paper with PENDING flags

Present these questions:

```
ONBOARDING QUESTIONS -- NIGERIA VAT
1. Are you registered for VAT with NRS? What is your Tax ID?
2. What is your gross annual turnover and total fixed assets (small-business exemption: NGN 100 million or less turnover and NGN 250 million or less fixed assets, excluding professional services and petroleum operations)?
3. What types of goods or services do you sell?
4. Do you make any zero-rated supplies (basic food, medical, tuition, non-oil exports) or exempt supplies (land/building, shared passenger road transport, financial instruments)?
5. Do you sell to government entities?
6. Do you import goods or services?
7. Do you have valid VAT invoices for all purchase claims?
8. Any excess credit carried forward from prior period?
```

## Section 10 -- Reference Material

### Key Legislation

**Key Legislation**

| Topic | Reference |
| --- | --- |
| VAT imposition and rate | NTA 2025 ss. 144, 147 |
| Small-business VAT exemption | NTAA 2025 ss. 22(4)-(9), 147 |
| Exempt and zero-rated supplies | NTA 2025 ss. 185, 186 |
| VAT invoice and fiscalisation | NTA 2025 ss. 152, 157; NTAA 2025 s. 23 |
| Non-resident supplies and withholding | NTA 2025 ss. 150, 154 |
| Filing, payment and input VAT | NTAA 2025 ss. 22, 39, 56; NTA 2025 s. 155 |
| Penalties | NTAA 2025 ss. 65, 100, 101, 104, 105, 107, 127 |

### Known Gaps / Out of Scope

- International VAT recovery
- Transfer pricing implications
- Companies Income Tax (CIT)
- Withholding tax on contracts (separate from VAT)

### Changelog

**Changelog**

| Version | Date | Change |
| --- | --- | --- |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; Nigerian bank formats; local payment patterns (Paystack, Flutterwave, OPay); worked examples |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Registration and TIN confirmed?
- [ ] Outside small-business exemption (turnover above NGN 100M, fixed assets above NGN 250M, professional services, petroleum operations or written opt-out)?
- [ ] All input claims supported by valid VAT invoices?
- [ ] Exempt supplies identified and excluded from output VAT?
- [ ] Nil return filed if no activity?
- [ ] Filing by 21st of following month?

## PROHIBITIONS

- NEVER charge 7.5% VAT on zero-rated supplies (basic food items, medical products/services, educational tuition/books) or exempt supplies (land or building, residential rent)
- NEVER claim input VAT without a valid VAT invoice
- NEVER require VAT registration for qualifying small businesses (gross annual turnover NGN 100,000,000 or less and total fixed assets NGN 250,000,000 or less, excluding professional services and petroleum operations) unless they opt out in writing
- NEVER apply a VAT rate other than 7.5% (the pre-2020 rate of 5% is no longer applicable)
- NEVER miss the 21st monthly filing deadline -- nil returns are still required
- NEVER claim input VAT on purchases used for exempt supplies
- NEVER ignore self-accounting obligations on imported services from non-residents
- NEVER present calculations as definitive -- always label as estimated and direct client to ICAN/ANAN member

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a chartered accountant (FCA/ACA) or accredited tax practitioner in Nigeria) before filing or acting upon.
