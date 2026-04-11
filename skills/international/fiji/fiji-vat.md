---
name: fiji-vat
description: Use this skill whenever asked to prepare, review, or create a Fiji VAT return or any VAT filing for a Fijian business. Trigger on phrases like "prepare VAT return", "Fiji VAT", "FRCS filing", "TIN registration Fiji", or any request involving Fiji VAT. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Fiji VAT classification rules, return form mappings, input credit rules, and filing deadlines. ALWAYS read this skill before touching any Fiji VAT-related work.
---

# Fiji VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Fiji |
| Jurisdiction Code | FJ |
| Primary Legislation | Value Added Tax Act 1991 (as amended) |
| Supporting Legislation | VAT Regulations; Tax Administration Act 2009 |
| Tax Authority | Fiji Revenue and Customs Service (FRCS) |
| Filing Portal | https://www.frcs.org.fj (TPOS -- Taxpayer Online Services) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending local practitioner validation |
| Validation Date | Pending |
| Last Verified | 2026-04-10 -- web-research cross-check of rates, thresholds, deadlines |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: standard rate classification, input-output mapping, return structure. Tier 2: zero-rated food items, tourism incentives, partial exemption. Tier 3: complex group structures, free trade zone, government contracts. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN** [T1] -- Tax Identification Number
2. **VAT registration status** [T1] -- Mandatory, Voluntary, or Not registered
3. **Filing period** [T1] -- monthly (turnover > FJD 300,000/year) or quarterly (FJD 100,000 - FJD 300,000); annual filing removed from 1 January 2025
4. **Industry/sector** [T2] -- impacts zero-rating (e.g., basic food, exports)
5. **Does the business make exempt supplies?** [T2] -- If yes, input credit apportionment
6. **Does the business export goods/services?** [T1] -- zero-rating
7. **Does the business deal in zero-rated basic food items?** [T1] -- specific list
8. **Excess credit brought forward** [T1] -- from prior period

**If any of items 1-3 are unknown, STOP.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, FNPF contributions, loan repayments, dividends = OUT OF SCOPE
- **Legislation:** VAT Act 1991, Section 4

### 1b. Determine Supply Location [T1]
- Domestic (within Fiji)
- Import (outside Fiji)
- Export (outside Fiji)
- **Legislation:** VAT Act 1991, Section 13 (place of supply)

### 1c. Determine VAT Rate [T1]
- **Standard rate:** 12.5% (reduced from 15% effective 1 August 2025; previously 9% before August 2023)
- **Zero-rated (0%):**
  - Exports of goods and services
  - Basic food items (specified list): flour, rice, sugar, cooking oil, canned fish, fresh fruits and vegetables, bread, milk, baby food, etc.
  - Supply of water (domestic)
  - Prescription medicines
  - Kerosene
- **Exempt:**
  - Financial services (interest, insurance premiums)
  - Residential rental
  - Medical services (public hospitals)
  - Educational services (registered institutions)
  - Public transportation (bus services)
  - Charitable activities
- **Legislation:** VAT Act 1991 (as amended), Section 16 (standard rate); First Schedule (zero-rated); Second Schedule (exempt)

### 1d. Determine Expense Category [T1]
- Capital goods: assets > 1 year useful life
- Trading stock: goods for resale
- Services/overheads: rent, utilities, professional fees
- **Legislation:** VAT Act 1991, Section 23 (input tax)

---

## Step 2: VAT Return Form Structure [T1]

**Legislation:** VAT Act 1991; FRCS VAT Return Form.

### VAT Return Sections

| Box | Description |
|-----|-------------|
| Box 1 | Total sales (inclusive of VAT) |
| Box 2 | Zero-rated sales |
| Box 3 | Exempt sales |
| Box 4 | Taxable sales (Box 1 - Box 2 - Box 3) |
| Box 5 | Output VAT (12.5% of taxable sales value) |
| Box 6 | Total purchases (inclusive of VAT) |
| Box 7 | Purchases of capital goods |
| Box 8 | Non-creditable purchases |
| Box 9 | Total input VAT credit |
| Box 10 | Adjustments (credit notes, bad debts, etc.) |
| Box 11 | Net VAT payable (Box 5 - Box 9 +/- Box 10) |
| Box 12 | Credit brought forward |
| Box 13 | Total payable or credit carried forward |

---

## Step 3: Input Tax Credit Mechanism [T1]

**Legislation:** VAT Act 1991, Sections 23-28.

### Eligibility for Input Tax Credit

1. Business must be VAT registered [T1]
2. Purchase must relate to making taxable (including zero-rated) supplies [T1]
3. Valid tax invoice held [T1]
4. Supplier must be VAT registered [T1]
5. Claim within the correct period [T1]

### Zero-Rated Supplier's Input Credit [T1]
Businesses making zero-rated supplies (exporters, basic food suppliers) are entitled to full input VAT credit recovery. Zero-rated is NOT the same as exempt -- zero-rated suppliers RECOVER input VAT.

### Input Tax Apportionment [T2]
If making both taxable and exempt supplies:
```
Creditable Input VAT = Total Input VAT x (Taxable + Zero-rated Supplies / Total Supplies)
```
**Flag for reviewer: confirm apportionment.**

---

## Step 4: Deductibility Check

### Blocked Input Tax Credit [T1]

**Legislation:** VAT Act 1991, Section 24.

These have ZERO input tax credit:

- Motor vehicles for private use (unless in transport/rental business)
- Entertainment expenses
- Personal consumption
- Club memberships
- Purchases without valid tax invoice
- Purchases from non-registered suppliers
- Goods/services used for exempt supplies
- Alcohol and tobacco (unless in resale business)

Blocked categories OVERRIDE any other rule. Check blocked FIRST.

---

## Step 5: VAT on Imports [T1]

**Legislation:** VAT Act 1991, Section 14; Customs Act.

### Import VAT
- VAT payable at point of importation
- Calculated on: CIF value + Customs Duty + Fiscal Duty + Excise Duty
- Rate: 12.5%
- Paid to FRCS Customs Division
- Recoverable as input credit if for taxable supplies

---

## Step 6: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory VAT registration | Annual turnover > FJD 100,000 |
| Voluntary registration | Below threshold but may register |
| Monthly filing threshold | Annual turnover > FJD 300,000 |
| Quarterly filing | Annual turnover FJD 100,000 - FJD 300,000 |

---

## Step 7: Filing Deadlines [T1]

| Category | Period | Deadline |
|----------|--------|----------|
| Monthly filers | Monthly | Last day of following month |
| Quarterly filers | Quarterly | Last day of month following quarter end |
| Payment | Same as return | Same deadline |
| Annual reconciliation | Annual | With income tax return |

### Quarterly Periods

| Quarter | Period | Due Date |
|---------|--------|----------|
| Q1 | January - March | 30 April |
| Q2 | April - June | 31 July |
| Q3 | July - September | 31 October |
| Q4 | October - December | 31 January |

### Late Filing Penalties [T1]

| Default | Penalty |
|---------|---------|
| Late filing | FJD 250 per month (minimum) |
| Late payment | 5% immediately + 2% per month compounding |
| Non-filing | Assessment by FRCS + penalties |
| Tax evasion | Criminal prosecution |

---

## Step 8: Derived Calculations [T1]

```
Taxable Sales Value   = Total Sales - Zero-rated - Exempt
Output VAT            = Taxable Sales Value x 12.5/112.5 (VAT-inclusive method)
                     OR Taxable Sales Value x 12.5% (VAT-exclusive method)
Total Input VAT       = VAT on purchases + VAT on imports
Net VAT Payable       = Output VAT - Input VAT - Credit B/F
If Net < 0            = Credit carried forward or refund application
```

---

## Step 9: Environment and Climate Adaptation Levy (ECAL) [T1]

**Legislation:** ECAL Act / Environment and Climate Adaptation Levy.

ECAL is a separate levy imposed on specified services:
- Prescribed services (hotels, restaurants, etc.) at 5%
- ECAL is NOT VAT -- it is a separate environmental levy
- ECAL does not affect VAT calculations
- ECAL is reported on a separate return

**Do not include ECAL in VAT return calculations.**

---

## PROHIBITIONS [T1]

- NEVER allow unregistered entities to claim input VAT credit
- NEVER classify exempt supplies as zero-rated
- NEVER confuse zero-rated basic food with exempt supplies -- zero-rated allows input credit recovery
- NEVER include ECAL in VAT return calculations
- NEVER accept input credit without valid tax invoice
- NEVER apply input credit on blocked categories
- NEVER file return without reconciling records
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 10: Edge Case Registry

### EC1 -- Basic food zero-rating classification [T2]
**Situation:** Supplier sells processed food items (canned vegetables, packaged snacks).
**Resolution:** Only items on the specific zero-rated list qualify. Processed/packaged items may not qualify. Flag for reviewer: check against current FRCS zero-rated food list.
**Legislation:** VAT Act 1991, First Schedule.

### EC2 -- Tourism operator input credit [T1]
**Situation:** Tour operator purchases fuel, vehicles, and meals for tourists.
**Resolution:** Input credit on fuel and vehicles used in the business is allowed (business use). Meals provided to tourists as part of a package are business inputs (not entertainment). Full input credit if VAT registered.

### EC3 -- Imported services (reverse charge) [T2]
**Situation:** Fijian company pays for cloud software from a US provider.
**Resolution:** Self-assess VAT at 12.5% on service value. Report as output VAT. Claim input credit if used for taxable supplies. Flag for reviewer: confirm current reverse charge rules.

### EC4 -- Bad debt relief [T2]
**Situation:** Customer does not pay, debt written off after 12 months.
**Resolution:** VAT bad debt relief may be available. Reduce output VAT by the VAT component of the bad debt. Flag for reviewer: confirm eligibility criteria and time limits.
**Legislation:** VAT Act 1991, Section 33.

### EC5 -- Second-hand goods [T1]
**Situation:** Business purchases second-hand equipment from a non-registered person.
**Resolution:** No input VAT credit. No VAT was charged. Full cost as expense.

### EC6 -- Mixed supply: taxable and zero-rated [T1]
**Situation:** Supermarket sells both standard-rated and zero-rated food items.
**Resolution:** Classify each item individually. Zero-rated items at 0%. Standard items at 12.5%. Input credit on overhead proportioned to both (full credit since both are taxable/zero-rated, not exempt).

### EC7 -- Cross-border digital services [T2]
**Situation:** Fijian consumer purchases digital content from overseas.
**Resolution:** Non-resident digital service providers may be required to register for VAT. If B2B, reverse charge by Fijian business. If B2C, provider responsible. Flag for reviewer.

### EC8 -- Government grants and subsidies [T1]
**Situation:** Business receives government grant for capital investment.
**Resolution:** Grants are not consideration for a supply. No output VAT on grant receipt. Input credit on purchases funded by grant still allowed if for taxable business activities.

---

## Step 11: Reviewer Escalation Protocol

When a [T2] situation is identified:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
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

## Step 12: Test Suite

### Test 1 -- Standard local sale at 12.5%
**Input:** Domestic sale of furniture, net FJD 10,000, VAT FJD 1,250. VAT registered.
**Expected output:** Box 4: FJD 10,000. Box 5: Output VAT FJD 1,250.

### Test 2 -- Local purchase with input credit
**Input:** Purchase from registered supplier, net FJD 5,000, VAT FJD 625. Valid invoice.
**Expected output:** Box 9: Input VAT FJD 625. Full credit.

### Test 3 -- Export (zero-rated)
**Input:** Export of sugar, FOB FJD 100,000. Documentation complete.
**Expected output:** Box 2: FJD 100,000 at 0%. No output VAT. Full input credit recovery.

### Test 4 -- Zero-rated basic food
**Input:** Sale of rice (10kg bags), FJD 50,000 total.
**Expected output:** Box 2: FJD 50,000 at 0%. No output VAT. Seller's input credit on related costs fully recoverable.

### Test 5 -- Blocked input: entertainment
**Input:** Client dinner, FJD 500, VAT FJD 62.50.
**Expected output:** Input VAT FJD 0 (BLOCKED).

### Test 6 -- Import with customs VAT
**Input:** Import goods, CIF FJD 20,000. Duty FJD 3,000. Fiscal duty FJD 1,000. VAT at 12.5% on FJD 24,000 = FJD 3,000.
**Expected output:** Box 9: Input VAT FJD 3,000. Credit allowed.

### Test 7 -- Mixed taxable and exempt
**Input:** Financial institution: 70% exempt (lending), 30% taxable (advisory). Total input VAT FJD 10,000.
**Expected output:** Creditable input VAT = FJD 10,000 x 30% = FJD 3,000.

### Test 8 -- Late payment penalty
**Input:** VAT payable FJD 5,000. Paid 3 months late.
**Expected output:** Immediate penalty: 5% x FJD 5,000 = FJD 250. Monthly: 2% compounding for 3 months. Total additional calculated by engine.

---

## Step 13: Invoice Requirements [T1]

**Legislation:** VAT Act 1991, Section 18.

### Mandatory Contents of Tax Invoice
1. Supplier's name, address, and TIN
2. Buyer's name and TIN (if registered)
3. Date of issue
4. Sequential invoice number
5. Description of goods/services
6. Quantity and unit price
7. VAT rate (12.5%) and VAT amount
8. Total amount including VAT
9. Words "Tax Invoice" must appear on the document

### Types
- **Full Tax Invoice:** For B2B transactions, enables input credit
- **Simplified Tax Invoice:** For retail sales under FJD 1,000
- **Credit Note:** For returns and price adjustments

---

## Step 14: Record Keeping [T1]

**Legislation:** Tax Administration Act 2009, Section 46.

### Mandatory Records (retain for 7 years)
1. All purchase and sales invoices
2. VAT account / control account
3. Import documentation (customs entries)
4. Export documentation
5. Bank statements and payment receipts
6. General ledger, journals, trial balance
7. Stock records
8. Fixed asset register
9. Credit and debit notes
10. Payroll records (separate obligation)

---

## Step 15: Specific Sector Rules

### Tourism and Hospitality [T1]
- Hotel accommodation: VAT at 12.5%
- Restaurant services: VAT at 12.5%
- Tour operator services: VAT at 12.5%
- ECAL at 5% on prescribed services (separate from VAT)
- Input credit on hotel supplies fully recoverable
- Duty-free shops: may have special customs treatment but VAT still applies on domestic sales

### Sugar Industry [T1]
- Raw sugar: zero-rated (basic food item)
- Processed/refined sugar products: may be zero-rated per list
- Molasses and by-products: VAT at 12.5%
- Input credit on mill equipment and supplies allowed

### Financial Services [T2]
- Interest on loans: exempt
- Insurance premiums: exempt
- Fee-based advisory services: VAT at 12.5%
- Banks must apportion input credit between taxable and exempt
- **Flag for reviewer: bank apportionment is complex**

### Construction [T1]
- Construction services: VAT at 12.5%
- Sale of new residential property: VAT at 12.5%
- Residential rental: exempt
- Commercial rental: VAT at 12.5%
- Input credit on materials allowed

---

## Step 16: Penalties Detailed Summary [T1]

| Offence | Penalty |
|---------|---------|
| Failure to register | FJD 500 + retrospective registration |
| Late filing | FJD 250 per month |
| Late payment | 5% immediately + 2% per month compounding |
| Non-issuance of invoice | FJD 500 per instance |
| Fraudulent return | Up to 300% of tax evaded + criminal prosecution |
| Failure to maintain records | FJD 500 |
| Under-declaration | Additional tax + penalty up to 75% |
| Tax evasion | Criminal prosecution, imprisonment up to 10 years |

---

## Step 17: Audit and Appeals [T2]

### Audit Process
1. FRCS may audit within **4 years** of filing (7 years for fraud)
2. Desk audits and field audits
3. Risk-based selection

### Appeals
1. File objection with FRCS within **60 days** of assessment
2. Appeal to Tax Tribunal
3. Further appeal to High Court

**Escalate any audit situation to qualified practitioner.**

---

## Step 18: Currency and Reporting [T1]

- All returns filed in FJD (Fiji Dollar)
- Foreign currency transactions: Reserve Bank of Fiji rate on date of supply
- Import transactions: customs exchange rate at date of declaration

---

## Step 19: Refund Mechanism [T2]

**Legislation:** VAT Act 1991, Section 35.

### Refund Eligibility
- Excess input credits for 3+ consecutive periods
- Exporters and zero-rated suppliers with persistent credits
- Entities ceasing business

### Process
1. Apply to FRCS
2. Audit may be conducted
3. Processing: 30-90 days
4. Refund via cheque or bank transfer

**Flag for reviewer: refund applications may trigger audits. Ensure documentation is complete.**

---

## Step 20: Specific VAT Treatment of Digital Services [T2]

**Legislation:** VAT Act amendments; FRCS rulings.

- Non-resident providers of digital services to Fiji consumers may need to register
- Fijian businesses purchasing digital services from overseas: reverse charge at 12.5%
- Evolving area -- flag for reviewer if significant digital service purchases

---

## Step 21: Transitional and Historical Rate Information [T1]

The VAT rate in Fiji has changed over time:
- Original rate (1992): 10%
- Reduced to 12.5% then to various rates at different points
- 2016: reduced to 9%
- 1 August 2023: increased from 9% to 15%
- 1 August 2025: reduced from 15% to **12.5%** (2025-2026 National Budget)
- Zero-rated food items introduced to reduce cost of living impact

**Always apply the CURRENT rate (12.5%) to current-period transactions. Historical rates only relevant for amended returns for prior periods.**

---

## Contribution Notes

This skill must be validated by a qualified Chartered Accountant or tax practitioner in Fiji before use in production.

**A skill may not be published without sign-off from a qualified practitioner in Fiji.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
