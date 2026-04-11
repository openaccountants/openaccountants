---
name: mongolia-vat
description: Use this skill whenever asked to prepare, review, or create a Mongolia VAT return or any VAT filing for a Mongolian business. Trigger on phrases like "prepare VAT return", "Mongolia VAT", "MTA filing", "НӨАТ", or any request involving Mongolia VAT. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Mongolia VAT classification rules, return form mappings, input credit rules, and filing deadlines. ALWAYS read this skill before touching any Mongolia VAT-related work.
---

# Mongolia VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Mongolia |
| Jurisdiction Code | MN |
| Primary Legislation | Value Added Tax Law of Mongolia (revised 2015, amended) |
| Supporting Legislation | General Taxation Law; Government Resolutions on VAT |
| Tax Authority | Mongolian Tax Authority (MTA) / General Department of Taxation |
| Filing Portal | https://e-tax.mta.mn (E-Barimt system) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending local practitioner validation |
| Validation Date | Pending |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: standard rate classification, input-output mapping, return structure. Tier 2: sector exemptions, mining VAT, special zones. Tier 3: mineral resource agreements, complex multi-entity structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN** [T1] -- Tax Identification Number issued by MTA
2. **VAT registration status** [T1] -- VAT registered (mandatory or voluntary) or below threshold
3. **Filing period** [T1] -- monthly (standard)
4. **Industry/sector** [T2] -- impacts exemptions (mining, agriculture, etc.)
5. **Does the business make exempt supplies?** [T2] -- If yes, input credit apportionment required
6. **Does the business import goods?** [T1] -- customs VAT treatment
7. **Does the business export goods/services?** [T1] -- zero-rating treatment
8. **Is the entity a mining/mineral resources company?** [T3] -- special VAT rules
9. **Does the entity use the E-Barimt system?** [T1] -- mandatory electronic invoicing
10. **Excess credit brought forward** [T1] -- from prior period

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, social insurance, loan repayments, dividends = OUT OF SCOPE
- **Legislation:** VAT Law, Article 4 (definitions)

### 1b. Determine Supply Location [T1]
- Domestic (within Mongolia)
- Import (goods/services from outside Mongolia)
- Export (goods/services to outside Mongolia)
- **Legislation:** VAT Law, Article 8 (place of supply)

### 1c. Determine VAT Rate [T1]
- **Standard rate:** 10%
- **Zero-rated:** Exports of goods and services
- **Exempt:** Listed in Article 13 of VAT Law:
  - Unprocessed agricultural and livestock products
  - Medical and healthcare services
  - Educational services
  - Public transportation
  - Financial and insurance services (interest, premiums)
  - Residential rental
  - Books, newspapers
  - Funeral services
  - Goods and services supplied to diplomats
  - Goods imported for humanitarian/disaster relief
- **Legislation:** VAT Law, Article 11 (rate), Article 13 (exemptions)

### 1d. Determine Expense Category [T1]
- Capital goods: fixed assets > 1 year useful life
- Trading stock: goods for resale
- Raw materials: production inputs
- Services/overheads: rent, utilities, professional fees
- **Legislation:** VAT Law, Article 14 (input tax)

---

## Step 2: VAT Return Form Structure [T1]

**Legislation:** VAT Law; MTA prescribed return form.

### Monthly VAT Return Sections

| Section | Description |
|---------|-------------|
| Part 1 | Taxpayer information (TIN, name, period) |
| Part 2 | Output / Sales |
| 2.1 | Taxable sales at 10% |
| 2.2 | Zero-rated sales (exports) |
| 2.3 | Exempt sales |
| 2.4 | Total sales |
| Part 3 | Output VAT |
| 3.1 | VAT on taxable sales (10%) |
| Part 4 | Purchases / Input |
| 4.1 | Domestic purchases with VAT |
| 4.2 | Imports with VAT paid at customs |
| 4.3 | Non-creditable purchases |
| 4.4 | Total purchases |
| Part 5 | Input VAT credit |
| 5.1 | VAT on domestic purchases |
| 5.2 | VAT on imports |
| 5.3 | Total input VAT credit |
| Part 6 | Net VAT |
| 6.1 | Output VAT minus Input VAT credit |
| 6.2 | Credit brought forward |
| 6.3 | Net payable or credit carried forward |

---

## Step 3: Input Tax Credit Mechanism [T1]

**Legislation:** VAT Law, Article 14-16.

### Eligibility for Input Tax Credit

1. Business must be VAT registered [T1]
2. Purchase must relate to taxable supplies [T1]
3. Valid E-Barimt receipt or VAT invoice held [T1]
4. Supplier must be VAT registered [T1]
5. Goods/services must have been received [T1]

### E-Barimt System [T1]

Mongolia uses the E-Barimt electronic receipt system. All VAT-registered taxpayers must issue E-Barimt receipts for all sales. Input tax credit is only valid with an E-Barimt receipt number.

- Every sale generates an E-Barimt receipt with a QR code
- Receipts are automatically transmitted to MTA
- Input credit claims are verified against E-Barimt database
- No E-Barimt = No input credit

### Input Tax Apportionment [T2]

If the business makes both taxable and exempt supplies:
```
Creditable Input VAT = Total Input VAT x (Taxable Supplies / Total Supplies)
```
**Flag for reviewer: apportionment must be confirmed.**

---

## Step 4: Deductibility Check

### Blocked Input Tax Credit [T1]

**Legislation:** VAT Law, Article 15.

These have ZERO input tax credit:

- Passenger vehicles (unless transport/rental business)
- Entertainment and hospitality expenses
- Personal consumption of owners/directors/employees
- Alcohol and tobacco products (unless in production/wholesale)
- Gifts and donations
- Purchases without valid E-Barimt receipt
- Purchases from non-VAT-registered suppliers
- Goods/services used for exempt supplies
- Fuel for non-commercial vehicles

Blocked categories OVERRIDE any other credit rule. Check blocked FIRST.

### Registration-Based Recovery [T1]
- VAT registered: input tax credit allowed
- Not registered: NO input tax credit

---

## Step 5: VAT on Imports [T1]

**Legislation:** VAT Law, Article 9; Customs Law.

### Import VAT
- VAT payable at point of importation
- Calculated on: Customs Value + Customs Duty + Excise Tax (if applicable)
- Rate: 10%
- Paid to Mongolian Customs at time of clearing
- Recoverable as input VAT credit

### Documentation
- Customs Declaration
- Commercial invoice
- Transport documents
- Customs payment receipt

---

## Step 6: Excise Tax Interaction [T1]

**Legislation:** Excise Tax Law.

| Category | Typical Rate |
|----------|-------------|
| Tobacco | MNT per unit (specific) |
| Alcohol / spirits | MNT per liter (specific) + ad valorem |
| Beer | MNT per liter |
| Vehicles (imported) | 5% - 20% |
| Petroleum products | MNT per liter (specific) |

Excise is calculated BEFORE VAT. VAT at 10% applies on (value + excise).

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory VAT registration | Annual turnover > MNT 50 million |
| Voluntary registration | Below threshold but may register |
| E-Barimt mandatory | All VAT-registered taxpayers |

---

## Step 8: Filing Deadlines [T1]

| Category | Period | Deadline |
|----------|--------|----------|
| VAT return | Monthly | By the 10th of the following month |
| Payment | Monthly | Same deadline as return |
| Annual reconciliation | Annual | With annual tax return (Feb 10 following year) |

### Fiscal Year [T1]
Mongolia fiscal year: 1 January to 31 December (calendar year).

### Late Filing Penalties [T1]

| Default | Penalty |
|---------|---------|
| Late filing | 0.3% per day of tax due (max 30% of tax) |
| Late payment | 0.3% per day of unpaid amount |
| Non-filing | Assessment by MTA + penalties |
| Failure to issue E-Barimt | Fine per transaction |
| Tax evasion | Criminal prosecution, fines |
| Incorrect return | Additional tax + 30% penalty |

---

## Step 9: Derived Calculations [T1]

```
Total Output VAT       = VAT on all taxable supplies (10%)
Total Input VAT        = VAT on domestic purchases + VAT on imports
Net VAT Payable        = Total Output VAT - Total Input VAT - Credit B/F
If Net < 0             = Credit carried forward (refund after 3 months)
Total Payable          = Net VAT Payable + Penalties/Interest (if any)
```

---

## Step 10: VAT Refund [T2]

**Legislation:** VAT Law, Article 17.

### Refund Eligibility
- Excess input VAT credit accumulated for 3+ consecutive months
- Exporters with consistent credit positions
- Entities ceasing business

### Refund Process
1. Apply through E-Tax system
2. MTA may conduct audit
3. Processing: 30-45 days (may take longer)
4. Refund via bank transfer

**Flag for reviewer: refund applications trigger audits. All E-Barimt records must be verified.**

---

## PROHIBITIONS [T1]

- NEVER allow unregistered entities to claim input VAT credit
- NEVER classify exempt supplies as zero-rated
- NEVER accept input credit without valid E-Barimt receipt
- NEVER apply input credit on blocked categories
- NEVER ignore excise tax when calculating VAT base
- NEVER allow input credit from non-registered suppliers
- NEVER file return without reconciling E-Barimt records
- NEVER assume mining entities follow standard VAT rules
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 11: Edge Case Registry

### EC1 -- Mining company VAT treatment [T3]
**Situation:** Mining company imports heavy equipment and exports minerals.
**Resolution:** Mining companies may operate under Stability Agreements with special VAT provisions. Do not classify. Escalate to review the specific agreement.
**Legislation:** Minerals Law; Stability Agreement terms.

### EC2 -- Reverse charge on imported services [T2]
**Situation:** Mongolian company pays for consulting from a foreign firm.
**Resolution:** Self-assess VAT at 10%. Report output VAT. Claim input credit if related to taxable supplies. Flag for reviewer.
**Legislation:** VAT Law, Article 8.

### EC3 -- E-Barimt receipt missing [T1]
**Situation:** Purchase made but E-Barimt receipt not issued by supplier.
**Resolution:** Input VAT credit DENIED. Full cost as expense. Report supplier to MTA for non-compliance. No exception.

### EC4 -- Cashmere and wool exports [T1]
**Situation:** Company exports raw cashmere.
**Resolution:** Export is zero-rated. Full input credit recovery on related purchases. Documentation: export customs declaration, bill of lading, bank receipt.

### EC5 -- Construction services [T1]
**Situation:** Construction company provides building services.
**Resolution:** VAT at 10% on contract value. Input credit on materials and subcontractor services allowed with valid E-Barimt. Progress billing: VAT on each payment milestone.

### EC6 -- Nomadic herder purchases [T2]
**Situation:** Food processing company purchases raw milk/meat from nomadic herders (not VAT registered).
**Resolution:** No VAT on purchase (unprocessed agricultural products are exempt). No input credit. The raw product exemption applies at first sale. Flag for reviewer if processed.

### EC7 -- Government contract payments [T1]
**Situation:** Company provides services to government under contract.
**Resolution:** Standard VAT at 10% applies. Government is the buyer. Issue E-Barimt receipt. Government may withhold income tax separately.

### EC8 -- Multi-currency transactions [T1]
**Situation:** Invoice issued in USD.
**Resolution:** Convert to MNT at Bank of Mongolia official rate on date of supply. All VAT calculations and reporting in MNT.

---

## Step 12: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

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
**Input:** Domestic sale of goods, net MNT 5,000,000, VAT MNT 500,000. VAT registered.
**Expected output:** Part 2.1: MNT 5,000,000. Part 3.1: Output VAT MNT 500,000.

### Test 2 -- Local purchase with input credit
**Input:** Purchase from VAT-registered supplier, net MNT 2,000,000, VAT MNT 200,000. Valid E-Barimt held.
**Expected output:** Part 5.1: Input VAT MNT 200,000. Full credit.

### Test 3 -- Import with customs VAT
**Input:** Import equipment, customs value MNT 30,000,000. Duty MNT 1,500,000. VAT at 10% on MNT 31,500,000 = MNT 3,150,000.
**Expected output:** Part 5.2: Input VAT MNT 3,150,000. Credit allowed.

### Test 4 -- Export (zero-rated)
**Input:** Export cashmere, FOB MNT 20,000,000. Documentation complete.
**Expected output:** Part 2.2: MNT 20,000,000 at 0%. Input credit recoverable.

### Test 5 -- Blocked input: personal vehicle
**Input:** Company purchases SUV for director, MNT 80,000,000, VAT MNT 8,000,000.
**Expected output:** Input VAT MNT 0 (BLOCKED).

### Test 6 -- No E-Barimt, no credit
**Input:** Purchase MNT 1,000,000 from supplier who did not issue E-Barimt.
**Expected output:** Input VAT MNT 0. No credit without E-Barimt receipt.

### Test 7 -- Reverse charge on imported services
**Input:** Mongolian company pays USD 3,000 (MNT 10,200,000) to Korean IT firm.
**Expected output:** Self-assess output VAT: MNT 1,020,000. Input credit: MNT 1,020,000 (if taxable). Net: zero.

### Test 8 -- Exempt agricultural product
**Input:** Herder sells raw unprocessed wool MNT 500,000 to processor.
**Expected output:** No VAT. Exempt supply. Buyer: no input credit on this purchase.

---

## Step 14: Invoice and E-Barimt Requirements [T1]

**Legislation:** VAT Law; E-Barimt Law.

### E-Barimt System Details
1. Every sale by a VAT-registered entity must generate an E-Barimt receipt
2. Receipts contain a unique QR code linked to MTA database
3. Consumer can verify receipt via E-Barimt mobile app
4. System provides lottery incentive for consumers who register receipts
5. E-Barimt is both a fiscal receipt and a tax invoice

### Mandatory Contents
1. Seller's name and TIN
2. Buyer's TIN (for B2B transactions)
3. Date and time of sale
4. Description of goods/services
5. Quantity and unit price
6. VAT amount (10%)
7. Total amount
8. E-Barimt receipt number and QR code

### Record Keeping (minimum 5 years)
1. All E-Barimt records (digital)
2. Purchase and sales journals
3. Import/export documentation
4. Bank statements
5. General ledger
6. Stock records
7. Fixed asset register

---

## Step 15: Specific Sector Rules

### Mining and Natural Resources [T3]
- Mining companies under Stability Agreements may have preferential VAT
- Mineral exports may have special documentation requirements
- Gold and precious metals: separate treatment under VAT Law
- **Always escalate mining sector VAT questions**

### Cashmere and Textile [T1]
- Raw cashmere purchase from herders: no VAT (exempt agricultural product)
- Processing: VAT at 10% on processed goods
- Export of cashmere products: zero-rated
- Input credit on processing equipment and chemicals allowed

### Construction [T1]
- Construction services: VAT at 10%
- Progress billing: VAT on each milestone
- Input credit on materials per E-Barimt

### Agriculture and Livestock [T1]
- Unprocessed agricultural products: exempt
- Raw livestock products (milk, wool, meat at first sale): exempt
- Processed food: VAT at 10%
- Agricultural equipment: VAT at 10% (input credit allowed if registered)

---

## Step 16: Penalties Detailed Summary [T1]

| Offence | Penalty |
|---------|---------|
| Failure to register | MNT 1,000,000 + retrospective registration |
| Late filing | 0.3% per day (max 30% of tax) |
| Late payment | 0.3% per day of unpaid amount |
| Failure to issue E-Barimt | MNT 200,000 per instance |
| Fraudulent declaration | Additional tax + 30% penalty + criminal prosecution |
| Failure to maintain records | MNT 500,000 |
| Tax evasion | Criminal prosecution, fines up to 300% of evaded tax |
| Obstruction of tax officer | MNT 300,000 |

---

## Step 17: Audit and Assessment [T2]

### Audit Process
1. MTA may audit within **4 years** of filing
2. Extended for suspected fraud
3. Risk-based selection using E-Barimt data analytics
4. E-Barimt mismatches may trigger automatic audit flag

### Appeals
1. File objection with MTA within **30 days** of assessment
2. Appeal to Tax Dispute Resolution Council
3. Further appeal to court

**Escalate any audit situation to qualified practitioner.**

---

## Step 18: Currency and Reporting Rules [T1]

**Legislation:** VAT Law; Bank of Mongolia Regulations.

- All VAT returns filed in MNT (Mongolian Tugrik)
- Foreign currency transactions: Bank of Mongolia official rate on date of supply
- E-Barimt system records all transactions in MNT
- Multi-currency contracts must be converted per transaction date
- For imports, customs exchange rate at date of declaration applies

---

## Step 19: Special Economic Zones [T3]

**Legislation:** Law on Free Trade Zones.

- Free trade zone entities may have preferential VAT treatment
- Goods entering domestic market from free zone treated as imports (VAT applies)
- Inter-zone transactions may be exempt
- Do not classify. Escalate to review specific zone regulations.

---

## Contribution Notes

This skill must be validated by a qualified Certified Professional Accountant (CPA) practicing in Mongolia before use in production. All T1 rules must be verified against the latest amendments to the VAT Law and MTA resolutions.

**A skill may not be published without sign-off from a qualified practitioner in Mongolia.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
