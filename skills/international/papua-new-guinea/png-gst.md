---
name: png-gst
description: Use this skill whenever asked to prepare, review, or create a Papua New Guinea GST return or any GST filing for a PNG business. Trigger on phrases like "prepare GST return", "PNG GST", "IRC filing", "Papua New Guinea tax", or any request involving PNG GST. Also trigger when classifying transactions for GST purposes from bank statements, invoices, or other source data. This skill contains the complete PNG GST classification rules, return form mappings, input credit rules, and filing deadlines. ALWAYS read this skill before touching any PNG GST-related work.
---

# Papua New Guinea GST Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Papua New Guinea |
| Jurisdiction Code | PG |
| Primary Legislation | Goods and Services Tax Act 2003 |
| Supporting Legislation | GST Regulations; Tax Administration Act 2015 |
| Tax Authority | Internal Revenue Commission (IRC) |
| Filing Portal | IRC offices; MyIRC online portal (limited services) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending local practitioner validation |
| Validation Date | Pending |
| Last Verified | 2026-04-10 -- web-research cross-check of rates, thresholds, deadlines |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: standard rate classification, input-output mapping, return structure. Tier 2: resource sector, exempt supplies, partial credit. Tier 3: mining/petroleum agreements, LNG project tax, complex group structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN** [T1] -- Tax Identification Number issued by IRC
2. **GST registration status** [T1] -- Registered or below threshold
3. **Filing period** [T1] -- monthly (turnover > PGK 1.5M) or quarterly (PGK 250K - PGK 1.5M); threshold raised from PGK 1M per 2025 National Budget
4. **Industry/sector** [T2] -- mining, petroleum, LNG, agriculture, services
5. **Does the business make exempt supplies?** [T2] -- apportionment required
6. **Does the business export goods/services?** [T1] -- zero-rating
7. **Is the entity in the resource sector?** [T3] -- mining/petroleum/LNG special rules
8. **Excess credit brought forward** [T1] -- from prior period

**If any of items 1-3 are unknown, STOP.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output GST) or Purchase (input GST)
- Salaries, superannuation, loan repayments, dividends = OUT OF SCOPE
- **Legislation:** GST Act 2003, Section 4

### 1b. Determine Supply Location [T1]
- Domestic (within PNG)
- Import (outside PNG)
- Export (outside PNG)
- **Legislation:** GST Act 2003, Section 11-12

### 1c. Determine GST Rate [T1]
- **Standard rate:** 10%
- **Zero-rated (0%):**
  - Exports of goods and services
  - International transport
  - Supply of fine metal (gold, silver, platinum)
  - Certain medical supplies
- **Exempt:**
  - Financial services (interest, insurance premiums)
  - Residential rental
  - Education (registered institutions)
  - Medical services (hospitals, clinics)
  - Unprocessed food (fresh fruit, vegetables, fish)
  - Water and sewerage (domestic)
  - Public transport
- **Legislation:** GST Act 2003, Section 17 (rate); Schedule 1 (zero-rated); Schedule 2 (exempt)

### 1d. Determine Expense Category [T1]
- Capital goods: assets > 1 year useful life
- Trading stock: goods for resale
- Services/overheads: rent, utilities, professional fees

---

## Step 2: GST Return Form Structure [T1]

**Legislation:** GST Act 2003; IRC prescribed form.

### GST Return Sections

| Section | Description |
|---------|-------------|
| Part A | Entity information (TIN, name, period) |
| Part B | Output / Sales |
| B.1 | Taxable supplies at 10% |
| B.2 | Zero-rated supplies |
| B.3 | Exempt supplies |
| B.4 | Total supplies |
| Part C | Output GST |
| C.1 | GST on taxable supplies |
| Part D | Input / Purchases |
| D.1 | Creditable acquisitions (domestic) |
| D.2 | Imports (GST paid) |
| D.3 | Non-creditable acquisitions |
| Part E | Input GST credit |
| E.1 | GST on domestic purchases |
| E.2 | GST on imports |
| E.3 | Total input credit |
| Part F | Net GST |
| F.1 | Output GST minus input credit |
| F.2 | Credit brought forward |
| F.3 | Net payable or refundable |

---

## Step 3: Input Tax Credit Mechanism [T1]

**Legislation:** GST Act 2003, Sections 29-35.

### Eligibility

1. Business must be GST registered [T1]
2. Purchase must relate to making taxable supplies [T1]
3. Valid tax invoice held [T1]
4. Supplier must be registered [T1]
5. Goods/services received [T1]

### Input Credit Apportionment [T2]

```
Creditable Input GST = Total Input GST x (Taxable + Zero-rated Supplies / Total Supplies)
```
**Flag for reviewer: confirm apportionment.**

---

## Step 4: Deductibility Check

### Blocked Input GST Credit [T1]

**Legislation:** GST Act 2003, Section 31.

These have ZERO input GST credit:

- Motor vehicles (private use)
- Entertainment
- Personal consumption
- Club memberships
- Purchases without valid tax invoice
- Purchases from non-registered suppliers
- Goods/services for exempt supplies
- Alcohol and tobacco (unless resale)

Blocked categories OVERRIDE any other rule. Check blocked FIRST.

---

## Step 5: GST on Imports [T1]

**Legislation:** GST Act 2003, Section 24; Customs Act.

### Import GST
- GST payable at importation
- Calculated on: Customs Value + Customs Duty + Excise
- Rate: 10%
- Paid to PNG Customs
- Recoverable if for taxable supplies

---

## Step 6: Resource Sector GST [T3]

**Legislation:** GST Act 2003, Part 5; Mining Act; Oil and Gas Act.

Resource sector entities (mining, petroleum, LNG) may have:
- Specific GST provisions under their fiscal stability agreements
- Different input credit rules
- Special treatment for imported equipment during development phase
- Zero-rating on certain supplies within the project

**Do not classify resource sector transactions without reviewing the specific agreement. Escalate.**

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory GST registration | Annual turnover > PGK 250,000 |
| Voluntary registration | Below threshold |
| Monthly filing | Annual turnover > PGK 1,500,000 |
| Quarterly filing | PGK 250,000 - PGK 1,500,000 (threshold raised from PGK 1,000,000 per 2025 National Budget) |

---

## Step 8: Filing Deadlines [T1]

| Category | Period | Deadline |
|----------|--------|----------|
| Monthly filers | Monthly | 21st of following month |
| Quarterly filers | Quarterly | 21st of month following quarter end |
| Payment | Same as return | Same deadline |

### Late Filing Penalties [T1]

| Default | Penalty |
|---------|---------|
| Late filing | PGK 500 per day (max PGK 10,000) |
| Late payment | 20% of unpaid amount |
| Non-filing | Assessment by IRC + penalties |
| Tax evasion | Criminal prosecution |

---

## Step 9: Derived Calculations [T1]

```
Total Output GST       = GST on all taxable supplies (10%)
Total Input GST        = GST on domestic purchases + GST on imports
Net GST Payable        = Total Output GST - Total Input GST - Credit B/F
If Net < 0             = Refundable or carried forward
Total Payable          = Net GST + Penalties (if any)
```

---

## Step 10: Refund Mechanism [T2]

**Legislation:** GST Act 2003, Section 40-42.

### Refund Eligibility
- Excess credits for 3+ consecutive months
- Exporters with persistent credit positions
- Resource sector (per agreement terms)

### Process
1. Apply to IRC
2. Audit may be conducted
3. Processing: 30-60 days

---

## PROHIBITIONS [T1]

- NEVER allow unregistered entities to claim input GST credit
- NEVER classify exempt supplies as zero-rated
- NEVER accept input credit without valid tax invoice
- NEVER apply input credit on blocked categories
- NEVER classify resource sector transactions without reviewing the specific agreement
- NEVER file return without reconciling records
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 11: Edge Case Registry

### EC1 -- Mining company equipment imports [T3]
**Situation:** Mining company imports heavy machinery during development.
**Resolution:** May have special GST treatment under fiscal stability agreement. Escalate.

### EC2 -- Reverse charge on imported services [T2]
**Situation:** PNG company pays for consulting from Australian firm.
**Resolution:** Self-assess GST at 10%. Claim input credit if for taxable supplies. Flag for reviewer.

### EC3 -- Supply of gold (fine metal) [T1]
**Situation:** Gold mining company sells refined gold.
**Resolution:** Zero-rated supply. No output GST. Full input credit on related costs.
**Legislation:** GST Act 2003, Schedule 1.

### EC4 -- Unprocessed food exemption [T1]
**Situation:** Farmer sells fresh vegetables at market.
**Resolution:** Exempt supply. No GST. Seller cannot claim input credit on farming inputs.

### EC5 -- Credit notes [T1]
**Situation:** Customer returns goods, credit note issued.
**Resolution:** Seller reduces output GST. Buyer reverses input credit.

### EC6 -- Second-hand goods from unregistered seller [T1]
**Situation:** Business buys used vehicle from individual.
**Resolution:** No input credit. No GST charged. Full cost as expense.

### EC7 -- Construction in remote area [T2]
**Situation:** Construction company works in remote location, purchases from unregistered village suppliers.
**Resolution:** No input credit on purchases from unregistered suppliers. Flag for reviewer if amounts are material.

### EC8 -- International shipping services [T1]
**Situation:** Shipping company provides international freight services.
**Resolution:** Zero-rated. No output GST. Full input credit on vessel costs, fuel, port charges.

---

## Step 12: Reviewer Escalation Protocol

When a [T2] situation is identified:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list possible treatments]
Recommended: [most likely correct treatment]
Action Required: Qualified accountant must confirm before filing.
```

When a [T3] situation is identified:

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
**Input:** Domestic sale of hardware supplies, net PGK 50,000, GST PGK 5,000. Registered.
**Expected output:** B.1: PGK 50,000. C.1: Output GST PGK 5,000.

### Test 2 -- Purchase with input credit
**Input:** Purchase from registered supplier, net PGK 20,000, GST PGK 2,000. Valid invoice.
**Expected output:** E.1: Input GST PGK 2,000. Full credit.

### Test 3 -- Export (zero-rated)
**Input:** Export of coffee, FOB PGK 200,000. Documentation complete.
**Expected output:** B.2: PGK 200,000 at 0%. Full input credit recovery.

### Test 4 -- Blocked input: entertainment
**Input:** Client entertainment, PGK 3,000, GST PGK 300.
**Expected output:** Input GST PGK 0 (BLOCKED).

### Test 5 -- Import with customs GST
**Input:** Import equipment, CIF PGK 100,000. Duty PGK 10,000. GST at 10% on PGK 110,000 = PGK 11,000.
**Expected output:** E.2: Input GST PGK 11,000. Credit allowed.

### Test 6 -- Gold sale (zero-rated)
**Input:** Sale of refined gold PGK 5,000,000.
**Expected output:** B.2: PGK 5,000,000 at 0%. No output GST.

### Test 7 -- Mixed taxable and exempt
**Input:** Entity: 80% taxable, 20% exempt. Total input GST PGK 50,000.
**Expected output:** Creditable: PGK 50,000 x 80% = PGK 40,000.

### Test 8 -- Late payment
**Input:** GST payable PGK 10,000. Filed on time but paid 10 days late.
**Expected output:** Late payment penalty: 20% x PGK 10,000 = PGK 2,000.

---

## Step 14: Invoice Requirements [T1]

**Legislation:** GST Act 2003, Section 35.

### Mandatory Contents of Tax Invoice
1. Supplier's name, address, and TIN
2. Buyer's name and TIN (if registered)
3. Date of issue
4. Sequential invoice number
5. Description of goods/services
6. Quantity and unit price
7. GST rate (10%) and GST amount
8. Total amount including GST
9. Words "Tax Invoice" on the document

### Types
- **Full Tax Invoice:** For B2B, enables input credit
- **Abbreviated Invoice:** For retail under PGK 500
- **Credit/Debit Note:** For adjustments

---

## Step 15: Record Keeping [T1]

**Legislation:** Tax Administration Act 2015, Section 48.

### Mandatory Records (retain for 7 years)
1. All purchase and sales invoices
2. GST account / control account
3. Import documentation (customs entries, bills of entry)
4. Export documentation (export entries, bills of lading)
5. Bank statements and payment receipts
6. General ledger, journals, trial balance
7. Stock/inventory records
8. Fixed asset register
9. Credit and debit notes
10. Employment records (separate from GST but required)

---

## Step 16: Specific Sector Rules

### Mining [T3]
- Mining operations under fiscal stability agreements may have different GST rules
- Equipment imports may qualify for concessional treatment
- Gold refining and export: zero-rated
- **Always escalate mining GST questions**

### Petroleum and LNG [T3]
- LNG project entities may have GST exemptions under their Tax Credit Agreement
- Subcontractors to LNG projects: complex treatment
- **Always escalate petroleum/LNG questions**

### Agriculture [T1]
- Unprocessed food (fresh fruit, vegetables, fish): exempt
- Processed food: GST at 10%
- Agricultural inputs (seeds, fertilizer, tools): GST at 10%, credit allowed
- Coffee, cocoa, copra exports: zero-rated

### Fisheries [T1]
- Fresh fish (unprocessed): exempt
- Canned/processed fish: GST at 10%
- Export of fresh fish: zero-rated
- Input credit on fishing equipment allowed if registered

### Construction [T1]
- Construction services: GST at 10%
- Progress billing: GST on each stage
- Input credit on materials and subcontractors allowed
- Government contracts: standard GST applies

---

## Step 17: Penalties Detailed Summary [T1]

| Offence | Penalty |
|---------|---------|
| Failure to register | PGK 1,000 + retrospective registration |
| Late filing | PGK 500 per day (max PGK 10,000) |
| Late payment | 20% of unpaid amount |
| Non-issuance of invoice | PGK 500 per instance |
| Fraudulent return | Up to 200% of understated tax + criminal prosecution |
| Failure to maintain records | PGK 1,000 |
| Under-declaration | Additional tax + penalty |
| Tax evasion | Criminal prosecution, imprisonment |

---

## Step 18: Audit and Appeals [T2]

### Audit Process
1. IRC may audit within **6 years** of filing
2. Types: desk review, field audit, comprehensive audit
3. Resource sector entities: priority audit targets
4. Risk-based selection using data analytics

### Appeals
1. File objection with IRC within **60 days** of assessment
2. Appeal to Tax Review Tribunal within **60 days**
3. Further appeal to National Court

**Escalate any audit situation to qualified practitioner.**

---

## Step 19: Currency and Reporting [T1]

- All GST returns filed in PGK (Papua New Guinea Kina)
- Foreign currency transactions: Bank of Papua New Guinea rate on date of supply
- Import transactions: customs exchange rate at date of declaration
- Resource sector entities may have USD-denominated contracts; convert per transaction

---

## Step 20: Provincial and Local Government Supplies [T1]

**Legislation:** GST Act 2003.

- Supplies by government agencies: generally exempt
- Supplies TO government: standard GST at 10%
- Government contracts: GST applies on contract value
- Government may withhold income tax on payments (separate from GST)

---

## Step 21: Informal Sector Considerations [T2]

**Legislation:** GST Act 2003; IRC rulings.

- PNG has a significant informal economy
- Purchases from unregistered / informal sellers: no input credit
- Market vendors below threshold: not required to register
- Businesses buying from informal sector: full cost as expense, no GST recovery
- **Flag for reviewer: material purchases from informal sector may attract IRC attention**

---

## Contribution Notes

This skill must be validated by a qualified CPA practicing in PNG before use in production.

**A skill may not be published without sign-off from a qualified practitioner in PNG.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
