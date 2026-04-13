---
name: uzbekistan-vat
description: >
  Use this skill whenever asked to prepare, review, or create an Uzbekistan VAT return or any VAT filing for an Uzbek business. Trigger on phrases like "prepare VAT return", "Uzbekistan VAT", "STC filing", "soliq.uz", "E-faktura", "factura.uz", or any request involving Uzbekistan VAT. Covers the 12% standard rate, E-faktura mandatory invoicing, input credit rules, turnover tax interaction, import VAT, and monthly filing to the State Tax Committee. ALWAYS read this skill before touching any Uzbekistan VAT work.
version: 2.0
jurisdiction: UZ
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Uzbekistan VAT Return -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Republic of Uzbekistan |
| Tax | VAT (Value Added Tax) at 12% |
| Currency | UZS only |
| Primary legislation | Tax Code of the Republic of Uzbekistan (2020, as amended) |
| Supporting legislation | Presidential Decrees; Cabinet of Ministers Resolutions |
| Tax authority | State Tax Committee (STC) / Davlat soliq qo'mitasi |
| Filing portal | https://my.soliq.uz (Taxpayer Cabinet) |
| Filing frequency | Monthly (standard); quarterly for certain taxpayers |
| Filing deadline | 20th of the month following the reporting period |
| E-faktura system | https://factura.uz (mandatory for all VAT payers) |
| Contributor | Open Accountants Community |
| Validated by | Deep research verification, April 2026 |
| Skill version | 2.0 |

### Rate Table

| Rate | Application |
|---|---|
| 12% | Standard rate on all taxable supplies |
| 0% | Exports of goods and services, international transport |
| Exempt (Article 244) | Financial services, education, medical, public transport, residential rental, agricultural (certain), government services, funeral/cultural/sports |

### Key Thresholds

| Item | Value |
|---|---|
| Mandatory VAT registration | Annual turnover > UZS 1 billion (approx. USD 80,000) |
| Voluntary VAT registration | Below threshold by election |
| Turnover tax (simplified) | 4% for most activities (below VAT threshold or eligible) |
| E-faktura mandatory | All VAT payers |
| E-faktura issuance deadline | Within 10 days of supply |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Tax regime unknown | STOP -- general (VAT) vs simplified (turnover tax) must be confirmed |
| E-faktura status unknown | No input credit until confirmed |
| Expense category unclear | Blocked (no recovery) |
| CIS vs non-CIS import unknown | Standard import VAT at 12% |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the month, TIN (INN, 9 digits), confirmation of VAT registration and tax regime.

**Recommended:** E-faktura records for the period, import customs declarations, prior period return.

**Ideal:** Complete purchase/sales journals, fixed asset register, E-faktura reconciliation.

### Refusal Catalogue

**R-UZ-1 -- Turnover tax payers.** "Entities on simplified (turnover tax) regime do not charge VAT and cannot claim input VAT. This skill does not prepare turnover tax returns."

**R-UZ-2 -- Free Economic Zone entities.** "FEZ entities may have VAT exemptions under specific decrees. Escalate to review the specific FEZ decree."

**R-UZ-3 -- Transfer pricing / subsoil use.** "Transfer pricing and subsoil use taxation are outside this skill scope. Escalate."

**R-UZ-4 -- Complex holding structures.** "Multi-entity and holding structures require specialist review. Escalate."

---

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| PEREVOD OT [client] / TRANSFER FROM | Taxable supply | Output VAT at 12% | Wire transfer from client |
| KARTA POPLNENIYE / CARD CREDIT | Taxable supply | Revenue | Card receipt |
| PAYME SETTLEMENT / PAYME CREDIT | Taxable supply | Revenue | Payme payment gateway |
| CLICK SETTLEMENT / CLICK UZ | Taxable supply | Revenue | Click.uz payment |
| UZCARD SETTLEMENT | Taxable supply | Revenue | UzCard settlement |
| HUMO SETTLEMENT | Taxable supply | Revenue | Humo card settlement |
| PROTSENTY / INTEREST | Exempt | NOT taxable | Bank interest |
| KREDIT / LOAN | EXCLUDE | Not income | Loan proceeds |

### 3.2 Expense Patterns (Debits)

| Pattern | Expense Category | Treatment | Notes |
|---|---|---|---|
| ARENDA OFISA / OFFICE RENT | Rent | Input VAT at 12% | Business premises |
| ELEKTR ENERGIYA / ELECTRICITY | Utilities | Input VAT at 12% | Electricity |
| GAZ / NATURAL GAS | Utilities | Input VAT at 12% | Gas |
| BEELINE / UCELL / UZMOBILE / MOBIUZ | Communications | Business portion claimable | Mixed use: apportion |
| YANDEX TAXI / TAXI | Travel | Input VAT if business | |
| AVTOMOBIL / VEHICLE | Vehicle | BLOCKED | Personal use vehicle |
| PRAZDNIK / BANKET / ENTERTAINMENT | Entertainment | BLOCKED | No input credit |
| NALOG / TAX PAYMENT / STC | EXCLUDE | Tax payment | Not deductible |
| ZARPLATA / SALARY | EXCLUDE | Payroll | Not VAT |
| LICHNIY PEREVOD / PERSONAL | EXCLUDE | Drawings | Not business |

---

## Section 4 -- Worked Examples

### Example 1 -- Standard Local Sale at 12%

**Input:** Domestic sale, net UZS 100,000,000, VAT UZS 12,000,000. General regime. E-faktura issued.

**Reasoning:** Standard domestic taxable supply. Report in Part 2 (taxable turnover) and Part 6 (output VAT).

**Classification:** Part 2: UZS 100,000,000. Part 6: Output VAT UZS 12,000,000.

### Example 2 -- Import with Customs VAT

**Input:** Import of equipment, customs value UZS 200,000,000. Duty UZS 20,000,000. VAT at 12% on (200M + 20M) = UZS 26,400,000.

**Reasoning:** VAT paid at customs on CIF + duties. Recoverable as input credit if for taxable supplies.

**Classification:** Part 8: Import VAT UZS 26,400,000. Full credit allowed.

### Example 3 -- Reverse Charge on Foreign IT Services

**Input:** Uzbek company pays USD 10,000 (UZS 128,000,000) to Russian IT firm. No VAT charged.

**Reasoning:** Non-resident has no PE in Uzbekistan. Self-assess output VAT at 12%: UZS 15,360,000. Input credit if for taxable supplies. Net = zero.

**Classification:** Output VAT UZS 15,360,000. Input VAT UZS 15,360,000. Net zero.

### Example 4 -- Purchase Without E-Faktura (Blocked)

**Input:** Purchase UZS 30,000,000, VAT UZS 3,600,000. No E-faktura issued by supplier.

**Reasoning:** No E-faktura = no input credit. This is absolute. The VAT is a cost.

**Classification:** Input VAT UZS 0. BLOCKED.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 VAT Return Structure

| Part | Description |
|---|---|
| 1 | Taxpayer information (TIN, name, period) |
| 2 | Taxable turnover at 12% |
| 3 | Zero-rated turnover (exports) |
| 4 | Exempt turnover |
| 5 | Total turnover |
| 6 | Output VAT (12% of Part 2) |
| 7 | Input VAT on domestic purchases |
| 8 | Input VAT on imports (customs) |
| 9 | Total input VAT credit |
| 10 | Net VAT payable |
| 11 | Credit brought forward |
| 12 | Net payable or credit carried forward |
| 13 | Adjustments (credit/debit notes) |

### 5.2 Input Tax Credit Rules (Articles 266-273)

Must be on general regime (VAT payer), purchase for taxable supplies, valid E-faktura held, supplier VAT-registered, goods/services received.

### 5.3 Blocked Input VAT (Article 268)

No credit: motor vehicles (personal), entertainment, personal consumption, no E-faktura, non-VAT-registered suppliers, exempt supply costs, alcohol/tobacco (unless production), gifts/donations, representation expenses beyond limits.

### 5.4 Import VAT (Article 259)

VAT at 12% on customs value + customs duty + excise. Paid at clearing. Recoverable if for taxable supplies.

### 5.5 Excise Interaction (Chapter 40)

Excise calculated BEFORE VAT. VAT at 12% applies on (value + excise).

### 5.6 Penalties

| Offence | Penalty |
|---|---|
| Late filing | 1% per day of tax (max 10%) |
| Late payment | 0.04% per day |
| Failure to issue E-faktura | Administrative fine |
| Under-declaration | Additional tax + 50% penalty |
| Fraudulent declaration | Up to 200% of understated tax |
| Tax evasion | Criminal prosecution |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Input Tax Apportionment

Creditable Input VAT = Total Input VAT x (Taxable Turnover / Total Turnover). Flag for reviewer.

### 6.2 IT Park Regime

IT companies may have incentives under IT Park regime. Software development exports may be zero-rated. Confirm IT Park status. Flag for reviewer.

### 6.3 Agricultural Producer Exemption

Agricultural enterprises selling unprocessed products may qualify for exemption. If voluntarily VAT registered, standard rules apply. Flag for reviewer.

### 6.4 Regime Transition (Turnover Tax to VAT)

When entity crosses VAT threshold, must register within 10 days. Inventory on hand at transition: VAT applies on subsequent sale. No input credit on pre-transition purchases. Flag for reviewer.

### 6.5 Free Economic Zone Entities

FEZ entities may have VAT exemptions on certain operations. Rules vary by FEZ. Escalate.

---

## Section 7 -- Working Paper Template

```
UZBEKISTAN VAT WORKING PAPER
Taxpayer: _______________  TIN (INN): ___________
Period: ___________  Regime: General / Simplified

A. OUTPUT
  A1. Taxable turnover at 12%                   ___________
  A2. Output VAT (A1 x 12%)                     ___________
  A3. Zero-rated turnover (exports)              ___________
  A4. Exempt turnover                            ___________

B. INPUT
  B1. Input VAT domestic purchases               ___________
  B2. Input VAT imports (customs)                ___________
  B3. Blocked input (vehicles, entertainment)    ___________
  B4. Total allowable input VAT                  ___________

C. NET VAT
  C1. Net payable (A2 - B4)                     ___________
  C2. Credit brought forward                     ___________
  C3. Adjustments                                ___________
  C4. Total payable / credit                     ___________

REVIEWER FLAGS:
  [ ] Tax regime confirmed (general VAT, not turnover tax)?
  [ ] All input claims supported by valid E-faktura?
  [ ] Blocked categories excluded?
  [ ] Import VAT reconciled with customs declarations?
  [ ] E-faktura issued within 10 days of supply?
```

---

## Section 8 -- Bank Statement Reading Guide

### Uzbek Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| NBU (National Bank) | PDF | Data, Opisaniye, Debet, Kredit, Ostatok |
| Kapitalbank | CSV / PDF | Sana, Tavsif, Chiqim, Kirim, Qoldiq |
| Ipoteka Bank | CSV | Date, Description, Debit, Credit, Balance |
| Hamkorbank | PDF | Sana, Bayonnoma, Chiqim, Kirim, Qoldiq |
| Uzpromstroybank | CSV | Date, Narration, Debit, Credit, Balance |
| InfinBank | CSV | Date, Details, Withdrawal, Deposit, Balance |

### Key Uzbek Banking Narrations

| Narration | Meaning | Classification Hint |
|---|---|---|
| PEREVOD / TRANSFER | Wire transfer | Income or expense |
| OPLATA / PAYMENT | Payment | Expense |
| POSTUPLENIE / RECEIPT | Incoming receipt | Income |
| NALOG / TAX | Tax payment | Exclude |
| ZARPLATA / SALARY | Payroll | Exclude |
| PROTSENTY / INTEREST | Interest | Exempt |
| KREDIT / LOAN | Loan | Exclude |

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Confirm tax regime FIRST -- if turnover tax, this skill does not apply
2. Classify all business credits as potential taxable supplies at 12%
3. Only claim input VAT where E-faktura is confirmed
4. Flag all imports for customs VAT verification

Present these questions:

```
ONBOARDING QUESTIONS -- UZBEKISTAN VAT
1. What is your TIN (INN)?
2. Are you on the general tax regime (VAT) or simplified regime (turnover tax)?
3. What types of goods or services do you sell?
4. Do you make any exempt supplies?
5. Do you export goods or services?
6. Are you in a Free Economic Zone (FEZ)?
7. Do you trade with CIS countries?
8. Do you have E-faktura records for all purchases?
9. Any excess credit brought forward from prior period?
10. Are you registered with IT Park (if IT company)?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| VAT imposition | Tax Code Chapter 35-39 |
| Rates | Tax Code Article 258 |
| Exemptions | Tax Code Article 244 |
| Place of supply | Tax Code Articles 241-245 |
| Input credit | Tax Code Articles 266-273 |
| Blocked input | Tax Code Article 268 |
| Import VAT | Tax Code Article 259 |
| Reverse charge | Tax Code Article 243 |
| Excise tax | Tax Code Chapter 40 |
| E-faktura | STC Regulations |

### Known Gaps / Out of Scope

- Turnover tax returns
- Free Economic Zone complex arrangements
- Transfer pricing
- Subsoil use taxation
- Complex holding structures

### Changelog

| Version | Date | Change |
|---|---|---|
| 2.0 | April 2026 | Full rewrite to v2.0 structure; Uzbek bank formats; local payment patterns (Payme, Click, UzCard, Humo); worked examples; E-faktura integration |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Tax regime confirmed (general VAT, not turnover tax)?
- [ ] All input claims supported by valid E-faktura?
- [ ] Blocked categories excluded?
- [ ] Import VAT reconciled?
- [ ] Excise calculated before VAT where applicable?
- [ ] Filing by 20th of following month?

---

## PROHIBITIONS

- NEVER allow turnover tax payers to claim input VAT credit or charge VAT
- NEVER classify exempt supplies as zero-rated
- NEVER accept input credit without valid E-faktura
- NEVER apply input credit on blocked categories
- NEVER confuse general regime (VAT) with simplified regime (turnover tax)
- NEVER file return without reconciling E-faktura records
- NEVER ignore excise when calculating VAT base
- NEVER present calculations as definitive -- always label as estimated and direct client to a qualified Uzbek accountant

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed auditor or tax consultant practicing in Uzbekistan) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
