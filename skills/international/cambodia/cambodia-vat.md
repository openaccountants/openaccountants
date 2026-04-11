---
name: cambodia-vat
description: Use this skill whenever asked to prepare, review, or create a Cambodia VAT return or any VAT filing for a Cambodian business. Trigger on phrases like "prepare VAT return", "Cambodia VAT", "GDT filing", "tax on value added", or any request involving Cambodia VAT. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Cambodia VAT classification rules, return form mappings, input credit rules, and filing deadlines. ALWAYS read this skill before touching any Cambodia VAT-related work.
---

# Cambodia VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Cambodia |
| Jurisdiction Code | KH |
| Primary Legislation | Law on Taxation (as amended, last major amendment 2023) |
| Supporting Legislation | Prakas (ministerial orders) on VAT; Sub-Decrees on Tax Administration |
| Tax Authority | General Department of Taxation (GDT), Ministry of Economy and Finance |
| Filing Portal | https://www.tax.gov.kh (E-Filing System) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending local practitioner validation |
| Validation Date | Pending |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: standard rate classification, input-output mapping, return structure. Tier 2: special regime (QIP), sector exemptions, non-resident tax. Tier 3: complex group structures, SEZ enterprises, treaty-based exemptions. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN (Tax Identification Number)** [T1] -- 9-digit TIN issued by GDT
2. **VAT registration status** [T1] -- Real Regime (VAT registered) or Estimated Regime (simplified, no VAT)
3. **VAT period** [T1] -- monthly (standard for Real Regime taxpayers)
4. **Industry/sector** [T2] -- impacts potential exemptions
5. **Does the business make exempt supplies?** [T2] -- If yes, input credit apportionment required
6. **Does the business import goods?** [T1] -- impacts customs-stage VAT
7. **Does the business export goods/services?** [T1] -- impacts zero-rating
8. **Is the entity a Qualified Investment Project (QIP)?** [T3] -- special tax incentives
9. **Is the entity in a Special Economic Zone (SEZ)?** [T3] -- special rules
10. **Excess credit brought forward** [T1] -- from prior period

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, NSSF contributions, loan repayments, dividends = OUT OF SCOPE (never on VAT return)
- **Legislation:** Law on Taxation, Chapter 4 (VAT)

### 1b. Determine Supply Location [T1]
- Domestic (within Cambodia)
- Import (goods/services from outside Cambodia)
- Export (goods/services to outside Cambodia)
- **Legislation:** Law on Taxation, Article 56 (place of supply)

### 1c. Determine VAT Rate [T1]
- **Standard rate:** 10%
- **Zero-rated:** Exports of goods and services
- **Exempt:** Listed in Article 57 of Law on Taxation:
  - Public postal services
  - Medical and dental services, medical supplies
  - Public transportation (not including tourist transport)
  - Insurance services (life insurance)
  - Primary financial services (interest income, currency exchange)
  - Import of articles for personal use (under de minimis threshold)
  - Non-profit activities
  - Electricity and water supply (domestic, up to threshold)
  - Unprocessed agricultural products
- **Legislation:** Law on Taxation, Article 55 (rates), Article 57 (exemptions)

### 1d. Determine Expense Category [T1]
- Capital goods: fixed assets with useful life > 1 year
- Trading stock: goods purchased for resale
- Raw materials / inputs
- Services/overheads: rent, utilities, professional fees
- **Legislation:** Law on Taxation, Article 59 (input VAT credit)

---

## Step 2: VAT Return Form Structure [T1]

**Legislation:** Law on Taxation; GDT e-Filing system forms.

### Monthly VAT Return Sections

| Section | Description |
|---------|-------------|
| Part 1 | Taxpayer information (TIN, name, period) |
| Part 2 | Sales / Output |
| 2.1 | Taxable sales at 10% |
| 2.2 | Zero-rated sales (exports) |
| 2.3 | Exempt sales |
| 2.4 | Total sales |
| Part 3 | Output VAT |
| 3.1 | VAT on taxable sales (10%) |
| Part 4 | Purchases / Input |
| 4.1 | Domestic taxable purchases |
| 4.2 | Imports (VAT paid at customs) |
| 4.3 | Non-creditable purchases |
| 4.4 | Total purchases |
| Part 5 | Input VAT credit |
| 5.1 | VAT on domestic purchases |
| 5.2 | VAT on imports |
| 5.3 | Total input VAT credit |
| Part 6 | Net VAT |
| 6.1 | Net tax (output - input) |
| 6.2 | Credit brought forward |
| 6.3 | Total payable or credit carried forward |

---

## Step 3: Input Tax Credit Mechanism [T1]

**Legislation:** Law on Taxation, Article 59-63.

### Eligibility for Input Tax Credit

1. The business must be registered under the Real Regime [T1]
2. The purchase must relate to making taxable supplies [T1]
3. A valid VAT invoice must be held [T1]
4. The supplier must be VAT registered [T1]
5. The claim must be made in the correct return period [T1]

### Input Tax Credit Rules

- Input VAT credit is available for goods and services used in making taxable (including zero-rated) supplies
- If used for both taxable and exempt supplies, apportionment required [T2]
- Credit cannot exceed output VAT unless consistently in credit (export-oriented businesses)
- Excess credit is carried forward (no automatic refund)

### Input Tax Credit Apportionment [T2]

```
Creditable Input VAT = Total Input VAT x (Taxable Turnover / Total Turnover)
```
**Flag for reviewer: apportionment calculation must be confirmed.**

---

## Step 4: Deductibility Check

### Blocked Input Tax Credit [T1]

**Legislation:** Law on Taxation, Article 60.

These have ZERO input tax credit:

- Entertainment expenses (meals, hospitality, recreation)
- Motor vehicles for personal use (private cars, motorcycles)
- Goods and services for personal consumption of owners/directors/employees
- Purchases without valid VAT invoice
- Purchases from Estimated Regime (non-VAT-registered) taxpayers
- Alcohol and tobacco (unless in production/distribution business)
- Gifts and donations
- Goods used exclusively for exempt supplies

Blocked categories OVERRIDE any other credit rule. Check blocked FIRST.

### Registration-Based Recovery [T1]
- Real Regime (VAT registered): input tax credit allowed
- Estimated Regime: NO input tax credit (flat turnover tax instead)

---

## Step 5: Withholding Tax Interaction [T1]

**Legislation:** Law on Taxation, Articles 24-33.

While withholding tax (WHT) is not VAT, it is commonly confused. Key distinctions:

| Tax | Nature | Applies To |
|-----|--------|-----------|
| VAT (10%) | Indirect, on consumption | Goods and services |
| WHT on services (15%) | Direct, on income | Payments to non-residents for services |
| WHT on rent (10%) | Direct, on income | Rental payments |
| WHT on interest (15%) | Direct, on income | Interest payments |

**WHT and VAT are separate obligations. Both may apply to the same transaction. VAT goes on the VAT return; WHT goes on the WHT return.**

---

## Step 6: VAT on Imports [T1]

**Legislation:** Law on Taxation, Article 58; Customs Law.

### Import VAT
- VAT is payable at the point of importation
- Calculated on: CIF value + Customs Duty + Excise Tax (if applicable)
- Rate: 10%
- Paid to General Department of Customs and Excise (GDCE) at time of clearing
- Recoverable as input VAT credit if goods used for taxable supplies

### Documentation Required
- Customs Declaration (SAD)
- Commercial invoice
- Bill of Lading / Airway Bill
- Customs payment receipt

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Real Regime mandatory (turnover) | Quarterly turnover > KHR 125 million (~USD 31,250) for goods; KHR 60 million (~USD 15,000) for services; or annual turnover > KHR 250 million (goods) / KHR 125 million (services). Importers, exporters, investment companies, and government contractors with total taxable turnover > KHR 30 million must also register. |
| Estimated Regime | Below Real Regime thresholds (simplified turnover tax) |
| Estimated Regime tax rate | 2% of turnover (goods) or 2% of turnover (services) |

---

## Step 8: Filing Deadlines [T1]

| Category | Period | Deadline |
|----------|--------|----------|
| VAT return (Real Regime) | Monthly | By the 20th of the following month |
| Payment | Monthly | Same deadline as return |
| Annual return / Tax on Profit | Annual | Within 3 months after fiscal year end |

### Late Filing Penalties [T1]

| Default | Penalty |
|---------|---------|
| Late filing | KHR 500,000 per month (minimum) or 2% of tax per month |
| Late payment | 2% per month on unpaid amount |
| Non-filing | Assessment by GDT + penalties |
| Failure to register | Retrospective registration + penalties |
| Tax evasion | Criminal prosecution, fines up to 400% of tax evaded |

---

## Step 9: Derived Calculations [T1]

```
Total Output VAT       = VAT on all standard-rated supplies (10%)
Total Input VAT        = VAT on domestic purchases + VAT on imports
Net VAT Payable        = Total Output VAT - Total Input VAT - Credit B/F
If Net < 0             = Credit carried forward
Total Payable          = Net VAT Payable + Penalties/Interest (if any)
```

---

## Step 10: Specific Tax on Certain Merchandise and Services (STCMS) [T1]

**Legislation:** Law on Taxation, Chapter 8.

STCMS (similar to excise duty) applies to specific goods:

| Category | Rate |
|----------|------|
| Cigarettes | 20% - 25% |
| Beer | 25% - 30% |
| Wine and spirits | 25% - 35% |
| Vehicles | 10% - 45% (depending on engine size) |
| Petroleum products | Specific rates per liter |
| Telecommunications | 3% |
| Air tickets (domestic) | 10% |

STCMS is calculated BEFORE VAT. VAT at 10% is applied on (value + STCMS).

---

## PROHIBITIONS [T1]

- NEVER allow Estimated Regime taxpayers to claim input VAT credit
- NEVER classify exempt supplies as zero-rated
- NEVER accept input VAT credit without valid VAT invoice from Real Regime supplier
- NEVER apply input credit on blocked categories
- NEVER confuse WHT with VAT -- they are separate obligations
- NEVER ignore STCMS when calculating VAT base for applicable goods
- NEVER allow input credit older than the current return period without adjustment
- NEVER file return without reconciling purchase/sales journals
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 11: Edge Case Registry

### EC1 -- Reverse charge on imported services [T2]
**Situation:** Cambodian company pays for consulting services from a foreign firm with no Cambodia presence.
**Resolution:** Client must self-assess VAT at 10% on the service value. Report as output VAT. May claim input credit if related to taxable supplies. Also assess WHT at 14% (separate obligation).
**Legislation:** Law on Taxation, Article 56.

### EC2 -- QIP enterprise VAT treatment [T3]
**Situation:** Client holds a QIP certificate from the Council for Development of Cambodia (CDC).
**Resolution:** QIP enterprises may be exempt from VAT on certain imports or supplies under their investment certificate. Do not classify. Escalate to practitioner to review QIP certificate terms.
**Legislation:** Law on Investment; CDC QIP certificate.

### EC3 -- Mixed supply: taxable and exempt [T2]
**Situation:** Bank provides both lending (exempt) and advisory (taxable) services.
**Resolution:** Input VAT credit must be apportioned. Only the portion relating to taxable supplies is creditable. Flag for reviewer: confirm apportionment ratio.

### EC4 -- Credit notes for price adjustments [T1]
**Situation:** Supplier issues credit note for defective goods returned.
**Resolution:** Supplier reduces output VAT in the period of credit note. Buyer reduces input VAT credit. Both adjust records accordingly.

### EC5 -- Prepaid Accommodation Tax interaction [T2]
**Situation:** Hotel collects both VAT and Accommodation Tax from guests.
**Resolution:** Accommodation Tax (2%) is a separate levy from VAT (10%). Both apply. VAT is on the room rate. Accommodation Tax is on the room rate excluding VAT. They are reported on separate returns. Do not net them.

### EC6 -- Supply of used goods [T1]
**Situation:** Company sells used office equipment.
**Resolution:** VAT at 10% on the selling price. Full output VAT applies regardless of whether input credit was claimed on original purchase. No reduced-rate or margin scheme in Cambodia.

### EC7 -- Non-resident digital services [T2]
**Situation:** Cambodian business subscribes to international SaaS platform.
**Resolution:** Reverse charge applies. Self-assess VAT at 10%. Also assess WHT at 14% if applicable. Flag for reviewer: confirm whether non-resident has registered for VAT in Cambodia (new rules may apply).

### EC8 -- Goods in transit through Cambodia [T1]
**Situation:** Goods pass through Cambodia in transit to a third country.
**Resolution:** No VAT applies to goods in transit if they remain under customs control and are not released for domestic consumption. Documentation must show transit status.

---

## Step 12: Reviewer Escalation Protocol

When a [T2] situation is identified, output the following structured flag:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Qualified accountant must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to qualified accountant. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard local sale at 10%
**Input:** Domestic sale of electronics, net KHR 10,000,000, VAT KHR 1,000,000. Real Regime client.
**Expected output:** Part 2.1: KHR 10,000,000. Part 3.1: Output VAT KHR 1,000,000.

### Test 2 -- Local purchase with input credit
**Input:** Purchase of office supplies from Real Regime supplier, net KHR 2,000,000, VAT KHR 200,000. Valid invoice held.
**Expected output:** Part 5.1: Input VAT KHR 200,000. Full credit.

### Test 3 -- Import with customs VAT
**Input:** Import of raw materials, CIF USD 10,000 (KHR 40,000,000). Customs duty KHR 2,000,000. VAT at 10% on KHR 42,000,000 = KHR 4,200,000.
**Expected output:** Part 5.2: Input VAT KHR 4,200,000. Credit allowed.

### Test 4 -- Export (zero-rated)
**Input:** Export of garments, FOB USD 50,000. All documentation complete.
**Expected output:** Part 2.2: KHR equivalent at 0%. No output VAT. Input credit recoverable.

### Test 5 -- Blocked input: entertainment
**Input:** Company pays for client dinner, KHR 1,500,000, VAT KHR 150,000.
**Expected output:** Input VAT KHR 0 (BLOCKED -- entertainment).

### Test 6 -- Estimated Regime, no input credit
**Input:** Small shop (Estimated Regime), monthly sales KHR 8,000,000.
**Expected output:** Turnover tax = 2% x KHR 8,000,000 = KHR 160,000. No VAT return filed. No input credit.

### Test 7 -- Reverse charge on imported services
**Input:** Cambodian company pays USD 5,000 to Singapore consulting firm. No local VAT invoice.
**Expected output:** Self-assess output VAT: KHR 2,000,000 (10% of KHR 20,000,000). Input credit: KHR 2,000,000 (if taxable business). Net effect: zero. Also: WHT at 14% = KHR 2,800,000 (separate return).

### Test 8 -- STCMS interaction with VAT
**Input:** Import of beer, CIF KHR 5,000,000. Customs duty KHR 500,000. STCMS at 30% on KHR 5,500,000 = KHR 1,650,000. VAT at 10% on KHR 7,150,000 = KHR 715,000.
**Expected output:** Import VAT: KHR 715,000. Input credit: KHR 715,000 (if in resale business). STCMS KHR 1,650,000 is NOT creditable as input VAT.

---

## Step 14: Invoice Requirements [T1]

**Legislation:** Law on Taxation; Prakas on Tax Invoices.

### Mandatory Contents of VAT Invoice
1. Supplier's name, address, and TIN
2. Buyer's name, address, and TIN (if Real Regime)
3. Date of issue
4. Sequential invoice number
5. Description of goods/services
6. Quantity and unit price
7. VAT rate (10%) and VAT amount
8. Total amount including VAT
9. "Tax Invoice" must be printed on the document

### Types of Invoices
- **Tax Invoice:** For Real Regime taxpayers (enables input credit)
- **Commercial Invoice:** For Estimated Regime taxpayers (does NOT enable input credit for buyer)
- **Credit Note:** For price adjustments and returns

---

## Step 15: Record Keeping [T1]

**Legislation:** Law on Taxation, Article 73; Sub-Decree on Tax Administration.

### Mandatory Records (retain for 10 years)
1. All purchase and sales invoices
2. VAT account / control account
3. Import documentation (SAD, commercial invoices)
4. Export documentation (customs declarations)
5. Bank statements and payment receipts
6. General ledger, journals, and trial balance
7. Payroll records (separate from VAT but required)
8. Fixed asset register
9. Stock/inventory records
10. Credit and debit notes

### Language and Currency
- Records must be in Khmer or bilingual (Khmer + English)
- All amounts in KHR (Cambodian Riel)
- USD transactions converted at NBC (National Bank of Cambodia) rate

---

## Step 16: Specific Sector Rules

### Construction [T1]
- Construction services: VAT at 10% on contract value
- Progress billing: VAT on each stage payment
- Input credit on materials and subcontractor invoices allowed
- Government contracts: standard VAT applies

### Garment Manufacturing (Export) [T1]
- Export of garments: zero-rated
- Input credit on raw materials (fabric, thread, accessories) fully recoverable
- QIP garment factories may have additional incentives [T3]

### Real Estate [T2]
- Sale of land: exempt from VAT (but subject to transfer tax)
- Sale of buildings: VAT at 10% on new buildings
- Residential rental: exempt
- Commercial rental: VAT at 10%
- **Flag for reviewer: mixed-use property requires careful classification**

### Telecommunications [T1]
- Telecom services: VAT at 10%
- STCMS at 3% on telecom (separate from VAT)
- Input credit on infrastructure allowed

---

## Step 17: Penalties Detailed Summary [T1]

| Offence | Penalty |
|---------|---------|
| Failure to register | KHR 1,000,000 + retrospective registration |
| Late filing | 2% of tax per month (min KHR 500,000) |
| Late payment | 2% per month on unpaid amount |
| Non-issuance of invoice | KHR 500,000 per instance |
| Fraudulent invoice | Up to 400% of evaded tax + criminal prosecution |
| Failure to maintain records | KHR 1,000,000 |
| Under-declaration | Additional tax + penalty of 40% |
| Tax evasion | Criminal prosecution, imprisonment 1-5 years |
| Failure to withhold WHT | Amount of WHT + 2% per month interest |

---

## Step 18: Audit and Appeals [T2]

### Audit Process
1. GDT may audit within **3 years** of filing (10 years for fraud)
2. Types: desk audit, field audit, comprehensive audit
3. Taxpayer must provide records within 15 days of notice

### Appeals
1. File objection with GDT within **30 days** of reassessment
2. Appeal to Tax Dispute Resolution Commission within **30 days**
3. Further appeal to courts

**Escalate any audit situation to qualified practitioner.**

---

## Step 19: Currency and Exchange Rate Rules [T1]

**Legislation:** Law on Taxation; NBC Regulations.

- All tax returns must be filed in KHR (Cambodian Riel)
- Cambodia widely uses USD in commerce; all USD amounts must be converted
- Exchange rate: National Bank of Cambodia (NBC) official rate on date of supply
- For imports, the customs exchange rate at date of declaration
- Dual-currency invoices (USD and KHR) are common and acceptable
- VAT amount must always be calculated and reported in KHR

---

## Contribution Notes

This skill must be validated by a qualified accountant or tax advisor practicing in Cambodia before use in production. All T1 rules must be verified against the latest Prakas and amendments to the Law on Taxation.

**A skill may not be published without sign-off from a qualified practitioner in Cambodia.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
