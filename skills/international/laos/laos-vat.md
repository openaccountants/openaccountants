---
name: laos-vat
description: Use this skill whenever asked to prepare, review, or create a Laos VAT return or any VAT filing for a Lao business. Trigger on phrases like "prepare VAT return", "Laos VAT", "Tax Department filing", "Lao PDR tax", or any request involving Laos VAT. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Laos VAT classification rules, return form mappings, input credit rules, and filing deadlines. ALWAYS read this skill before touching any Laos VAT-related work.
---

# Laos VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Lao People's Democratic Republic (Laos) |
| Jurisdiction Code | LA |
| Primary Legislation | Tax Law No. 67/NA (amended 2019) |
| Supporting Legislation | Decree on Tax Administration; Ministerial Instructions on VAT |
| Tax Authority | Tax Department, Ministry of Finance |
| Filing Portal | Tax Department offices; limited e-filing via TaxRIS |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending local practitioner validation |
| Validation Date | Pending |
| Last Verified | 2026-04-10 -- web-research cross-check of rates, thresholds, deadlines |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: standard rate classification, input-output mapping, return structure. Tier 2: sector exemptions, concession agreements, foreign-funded projects. Tier 3: mining/energy concessions, complex multi-entity structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN** [T1] -- Tax Identification Number issued by Tax Department
2. **VAT registration status** [T1] -- VAT registered (mandatory or voluntary) or below threshold
3. **Filing period** [T1] -- monthly (standard)
4. **Industry/sector** [T2] -- impacts exemptions and special treatment
5. **Does the business make exempt supplies?** [T2] -- If yes, input credit apportionment required
6. **Does the business import goods?** [T1] -- customs VAT treatment
7. **Does the business export goods/services?** [T1] -- zero-rating treatment
8. **Is the entity operating under a concession agreement?** [T3] -- mining, hydropower, etc.
9. **Is the entity a foreign-invested enterprise?** [T2] -- potential incentives
10. **Excess credit brought forward** [T1] -- from prior period

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, social security contributions, loan repayments, dividends = OUT OF SCOPE
- **Legislation:** Tax Law No. 67/NA, Part 4 (VAT provisions)

### 1b. Determine Supply Location [T1]
- Domestic (within Laos)
- Import (goods/services from outside Laos)
- Export (goods/services to outside Laos)
- **Legislation:** Tax Law No. 67/NA, Article 36 (place of supply)

### 1c. Determine VAT Rate [T1]
- **Standard rate:** 10%
- **Zero-rated:** Exports of goods and services (with proper documentation)
- **Exempt:** Listed in Article 38 of Tax Law:
  - Unprocessed agricultural, forestry, and fishery products
  - Seeds, animal feed, fertilizers, pesticides
  - Educational services
  - Medical and healthcare services
  - Public transportation
  - Banking and financial services (interest, insurance premiums)
  - Residential rent
  - Electricity for domestic consumption (below threshold)
  - Books, newspapers, magazines
  - International transportation
  - Goods imported under diplomatic privilege
- **Legislation:** Tax Law No. 67/NA, Article 35 (rate), Article 38 (exemptions)

### 1d. Determine Expense Category [T1]
- Capital goods: fixed assets with useful life > 1 year
- Trading stock: goods purchased for resale
- Raw materials: production inputs
- Services/overheads: utilities, rent, professional fees
- **Legislation:** Tax Law No. 67/NA, Article 40 (input tax credit)

---

## Step 2: VAT Return Form Structure [T1]

**Legislation:** Tax Law No. 67/NA; Tax Department prescribed return form.

### Monthly VAT Return Sections

| Section | Description |
|---------|-------------|
| Part 1 | Taxpayer information (TIN, name, period, address) |
| Part 2 | Output / Sales |
| 2.1 | Taxable sales at 10% |
| 2.2 | Zero-rated sales (exports) |
| 2.3 | Exempt sales |
| 2.4 | Total sales |
| Part 3 | Output VAT |
| 3.1 | VAT collected on taxable sales |
| Part 4 | Input / Purchases |
| 4.1 | Domestic purchases with VAT |
| 4.2 | Imports with VAT paid at customs |
| 4.3 | Exempt / non-creditable purchases |
| 4.4 | Total purchases |
| Part 5 | Input VAT credit |
| 5.1 | VAT on domestic purchases |
| 5.2 | VAT on imports |
| 5.3 | Total input VAT credit |
| Part 6 | Net VAT |
| 6.1 | Output VAT minus Input VAT credit |
| 6.2 | Credit brought forward from prior period |
| 6.3 | Net payable or credit carried forward |

---

## Step 3: Input Tax Credit Mechanism [T1]

**Legislation:** Tax Law No. 67/NA, Article 40-44.

### Eligibility for Input Tax Credit

1. The business must be VAT registered [T1]
2. The purchase must relate to making taxable supplies [T1]
3. A valid VAT invoice must be held [T1]
4. The supplier must be VAT registered [T1]
5. The goods/services must have been received [T1]
6. The claim must be within the relevant period [T1]

### Input Tax Credit Rules

- Full credit for purchases used entirely in making taxable supplies
- No credit for purchases used entirely for exempt supplies
- Apportionment for mixed-use purchases [T2]
- Excess input VAT credit carried forward (no automatic refund)

### Input Tax Credit Apportionment [T2]

```
Creditable Input VAT = Total Input VAT x (Taxable Supplies / Total Supplies)
```
**Flag for reviewer: apportionment must be confirmed.**

---

## Step 4: Deductibility Check

### Blocked Input Tax Credit [T1]

**Legislation:** Tax Law No. 67/NA, Article 41.

These have ZERO input tax credit:

- Entertainment expenses (meals, drinks, recreation)
- Motor vehicles for personal transport (unless transport business)
- Personal consumption of owners, directors, employees
- Fuel for non-commercial vehicles
- Gifts and donations
- Purchases without valid VAT invoice
- Purchases from non-VAT-registered suppliers
- Goods/services used for exempt supplies
- Luxury goods for personal use

Blocked categories OVERRIDE any other credit rule. Check blocked FIRST.

### Registration-Based Recovery [T1]
- VAT registered: input tax credit allowed (subject to rules)
- Not registered: NO input tax credit

---

## Step 5: VAT on Imports [T1]

**Legislation:** Tax Law No. 67/NA, Article 39; Customs Law.

### Import VAT
- VAT payable at point of importation
- Calculated on: CIF value + Customs Duty + Excise Tax (if applicable)
- Rate: 10%
- Paid to Customs Department at time of clearing
- Recoverable as input VAT credit if goods used for taxable supplies

### Documentation Required
- Customs Import Declaration
- Commercial invoice
- Bill of Lading / Airway Bill
- Customs payment receipt

---

## Step 6: Excise Tax Interaction [T1]

**Legislation:** Tax Law No. 67/NA, Part 5 (Excise Tax).

Excise tax applies to specified goods:

| Category | Typical Rate |
|----------|-------------|
| Tobacco products | 30% - 90% |
| Alcohol / spirits | 40% - 90% |
| Beer | 40% - 50% |
| Soft drinks | 5% |
| Fuel/petroleum | Specific rates |
| Motor vehicles | 15% - 80% (based on engine size) |
| Perfumes and cosmetics | 15% |

Excise tax is calculated BEFORE VAT. VAT at 10% is applied on (value + excise tax).

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory VAT registration | Annual turnover > LAK 400 million (~USD 20,000) |
| Voluntary registration | Below threshold but may register |
| Small business simplified regime | Below VAT threshold (lump-sum tax) |

---

## Step 8: Filing Deadlines [T1]

| Category | Period | Deadline |
|----------|--------|----------|
| VAT return | Monthly | By the 15th of the following month |
| Payment | Monthly | Same deadline as return |
| Annual tax return | Annual | Within 3 months after fiscal year end |

### Fiscal Year [T1]
Laos fiscal year: 1 January to 31 December (calendar year).

**Note:** The fiscal year was previously reported as October-September in some older sources, but Laos currently uses the calendar year (January-December) for tax purposes. [T2]

### Late Filing Penalties [T1]

| Default | Penalty |
|---------|---------|
| Late filing | 0.3% per day of the tax due |
| Late payment | 0.3% per day of unpaid amount |
| Non-filing | Assessment by Tax Department + penalties |
| Tax evasion | Criminal prosecution, fines, imprisonment |
| Incorrect return | Additional tax + penalty of 30% - 60% of understated amount |

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

## Step 10: Concession Agreements [T3]

**Legislation:** Law on Investment Promotion; individual concession agreements.

Entities operating under concession agreements (mining, hydropower, special economic zones) may have unique VAT treatment specified in their agreements. These may include:

- VAT exemption on imports of equipment during construction phase
- VAT holiday for initial operating years
- Special rates
- Exemption from certain obligations

**Do not classify. Escalate to practitioner to review the specific concession agreement.**

---

## PROHIBITIONS [T1]

- NEVER allow unregistered entities to claim input VAT credit
- NEVER classify exempt supplies as zero-rated
- NEVER accept input VAT credit without valid VAT invoice from registered supplier
- NEVER apply input credit on blocked categories
- NEVER ignore excise tax when calculating VAT base
- NEVER assume concession agreement terms without reviewing the actual agreement
- NEVER file return without reconciling purchase/sales registers
- NEVER allow input credit on personal consumption items
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 11: Edge Case Registry

### EC1 -- Reverse charge on imported services [T2]
**Situation:** Lao company pays for technical services from a Thai consultancy.
**Resolution:** Self-assess VAT at 10% on the service value. Report as output VAT. Claim input credit if related to taxable supplies. Flag for reviewer: also confirm WHT obligation.
**Legislation:** Tax Law No. 67/NA, Article 36.

### EC2 -- Foreign-funded project exemptions [T3]
**Situation:** NGO implements a foreign-funded development project.
**Resolution:** Certain foreign-funded projects receive VAT exemption on imports and purchases. Do not classify. Escalate to practitioner to review the project agreement and government approval.

### EC3 -- Hydropower company VAT treatment [T3]
**Situation:** Hydropower company sells electricity to domestic grid and exports to Thailand.
**Resolution:** Complex treatment under concession agreement. Domestic sales may be exempt (electricity). Export sales may be zero-rated. Concession may override general law. Escalate.

### EC4 -- Credit notes for returns [T1]
**Situation:** Customer returns defective goods, credit note issued.
**Resolution:** Supplier reduces output VAT in the period of credit note. Buyer reduces input VAT credit. Both adjust records.

### EC5 -- Barter transactions [T1]
**Situation:** Two businesses exchange goods without monetary consideration.
**Resolution:** VAT applies on the fair market value of goods supplied by each party. Each party accounts for output VAT on the value of goods they supply.
**Legislation:** Tax Law No. 67/NA, Article 37.

### EC6 -- Construction services provided to government [T2]
**Situation:** Construction company builds government infrastructure.
**Resolution:** Standard VAT at 10% applies on contract value. Government may be required to withhold income tax. VAT and income tax are separate. Flag for reviewer: confirm government payment procedures.

### EC7 -- Free zone / SEZ supplies [T3]
**Situation:** Entity in a Special Economic Zone sells goods locally.
**Resolution:** SEZ entities may have preferential tax treatment. When goods leave the SEZ for domestic consumption, import VAT may apply. Escalate to review SEZ regulations and entity agreement.

### EC8 -- Multi-currency invoicing [T1]
**Situation:** Supplier invoices in USD or THB instead of LAK.
**Resolution:** Convert to LAK at the Bank of Lao PDR official exchange rate on the date of supply for VAT purposes. All VAT calculations and reporting must be in LAK.

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
**Input:** Domestic sale of manufactured goods, net LAK 50,000,000, VAT LAK 5,000,000. VAT registered client.
**Expected output:** Part 2.1: LAK 50,000,000. Part 3.1: Output VAT LAK 5,000,000.

### Test 2 -- Local purchase with input credit
**Input:** Purchase of materials from VAT-registered supplier, net LAK 20,000,000, VAT LAK 2,000,000. Valid invoice held.
**Expected output:** Part 5.1: Input VAT LAK 2,000,000. Full credit.

### Test 3 -- Import with customs VAT
**Input:** Import of equipment, CIF LAK 100,000,000. Customs duty LAK 5,000,000. VAT at 10% on LAK 105,000,000 = LAK 10,500,000.
**Expected output:** Part 5.2: Input VAT LAK 10,500,000. Credit allowed.

### Test 4 -- Export (zero-rated)
**Input:** Export of coffee, FOB LAK 80,000,000. All documentation complete.
**Expected output:** Part 2.2: LAK 80,000,000 at 0%. No output VAT. Input credit recoverable.

### Test 5 -- Blocked input: entertainment
**Input:** Company dinner for clients, LAK 3,000,000, VAT LAK 300,000.
**Expected output:** Input VAT LAK 0 (BLOCKED -- entertainment).

### Test 6 -- Reverse charge on imported services
**Input:** Lao company pays USD 2,000 (LAK 40,000,000) to Vietnamese IT firm.
**Expected output:** Self-assess output VAT: LAK 4,000,000 (10%). Input credit: LAK 4,000,000 (if taxable business). Net: zero.

### Test 7 -- Excise + VAT on beer import
**Input:** Import beer, CIF LAK 10,000,000. Customs duty LAK 1,000,000. Excise at 50% on LAK 11,000,000 = LAK 5,500,000. VAT at 10% on LAK 16,500,000 = LAK 1,650,000.
**Expected output:** Import VAT: LAK 1,650,000. Credit allowed if in resale business. Excise NOT creditable.

### Test 8 -- Unregistered supplier purchase
**Input:** Purchase from small farmer (not VAT registered), LAK 5,000,000. No VAT invoice.
**Expected output:** No input VAT credit. Full cost as expense. No VAT recovery.

---

## Step 14: Invoice Requirements [T1]

**Legislation:** Tax Law No. 67/NA; Ministerial Instructions.

### Mandatory Contents of VAT Invoice
1. Supplier's name, address, and TIN
2. Buyer's name and TIN (if registered)
3. Date of issue
4. Invoice number (sequential)
5. Description of goods/services
6. Quantity and unit price
7. VAT rate (10%) and VAT amount
8. Total amount including VAT
9. Authorized signature and stamp

### Invoice Issuance
- Must be issued at time of supply
- Pre-printed invoice books obtained from Tax Department (controlled forms)
- Electronic invoicing being phased in

---

## Step 15: Record Keeping [T1]

**Legislation:** Tax Law No. 67/NA, Article 60.

### Mandatory Records (retain for 10 years)
1. All purchase and sales invoices
2. VAT account ledger
3. Import/export documentation
4. Bank statements and payment receipts
5. General ledger and journals
6. Stock/inventory records
7. Fixed asset register
8. Payroll records (separate obligation)
9. Credit and debit notes

### Language and Currency
- Records in Lao language
- All amounts in LAK (Lao Kip)
- Foreign currency transactions converted at Bank of Lao PDR rate

---

## Step 16: Specific Sector Rules

### Mining and Natural Resources [T3]
- Mining companies under concession agreements may have different VAT treatment
- Timber and wood products: VAT at 10% on processed; unprocessed may be exempt
- Escalate all mining/resource sector questions

### Tourism and Hospitality [T1]
- Hotel accommodation: VAT at 10%
- Restaurant services: VAT at 10%
- Tour operator services: VAT at 10%
- Input credit on supplies allowed

### Construction [T1]
- Construction services: VAT at 10% on contract value
- Input credit on materials allowed
- Government infrastructure projects: standard VAT rules apply

### Agriculture [T1]
- Unprocessed agricultural products: exempt
- Processed food products: VAT at 10%
- Agricultural inputs (seeds, fertilizer): exempt
- Transition from exempt to taxable occurs at processing stage

---

## Step 17: Penalties Detailed Summary [T1]

| Offence | Penalty |
|---------|---------|
| Failure to register | Fine + retrospective registration |
| Late filing | 0.3% per day of tax due |
| Late payment | 0.3% per day of unpaid amount |
| Non-issuance of invoice | Fine per Tax Department regulation |
| Fraudulent declaration | 30%-60% of understated amount + criminal prosecution |
| Failure to maintain records | Fine per regulation |
| Tax evasion | Criminal prosecution, imprisonment |
| Obstruction of tax officer | Fine and possible imprisonment |

---

## Step 18: Audit and Assessment [T2]

### Audit Process
1. Tax Department may audit within **3 years** of filing
2. Extended for suspected fraud
3. Types: desk audit, field audit, special investigation

### Appeals
1. File objection with Tax Department within **30 days**
2. Appeal to court within **60 days** of objection decision

**Escalate any audit situation to qualified practitioner.**

---

## Contribution Notes

This skill must be validated by a qualified accountant or tax advisor practicing in Laos before use in production. All T1 rules must be verified against the latest Tax Law amendments and ministerial instructions.

**A skill may not be published without sign-off from a qualified practitioner in Laos.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
