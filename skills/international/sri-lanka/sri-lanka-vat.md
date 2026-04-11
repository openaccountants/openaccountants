---
name: sri-lanka-vat
description: Use this skill whenever asked to prepare, review, or create a Sri Lanka VAT return or any VAT filing for a Sri Lankan business. Trigger on phrases like "prepare VAT return", "Sri Lanka VAT", "CGIR filing", "IRD return", or any request involving Sri Lanka VAT. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Sri Lanka VAT classification rules, return form mappings, input tax credit rules, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Sri Lanka VAT-related work.
---

# Sri Lanka VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Sri Lanka |
| Jurisdiction Code | LK |
| Primary Legislation | Value Added Tax Act No. 14 of 2002 (as amended) |
| Supporting Legislation | VAT (Amendment) Acts; Inland Revenue Act No. 24 of 2017; Gazette Notifications |
| Tax Authority | Commissioner General of Inland Revenue (CGIR) / Department of Inland Revenue (IRD) |
| Filing Portal | https://www.ird.gov.lk (e-Services Portal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending local practitioner validation |
| Validation Date | Pending |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: standard rate classification, input-output mapping, return fields. Tier 2: partial credit, sector-specific exemptions, risk-based refund mechanism (formerly SVAT). Tier 3: complex group structures, BOI enterprises, free trade zones. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN (Taxpayer Identification Number)** [T1]
2. **VAT registration number** [T1] -- separate from TIN
3. **Registration type** [T1] -- Mandatory VAT registered, Voluntary, or Not registered
4. **VAT period** [T1] -- monthly or quarterly (depending on turnover)
5. **Industry/sector** [T2] -- impacts exemptions (e.g., financial services, healthcare, education)
6. **Does the business make exempt supplies?** [T2] -- If yes, input tax credit apportionment required
7. **Does the business export goods/services?** [T1] -- impacts zero-rating
8. **Is the entity a BOI (Board of Investment) enterprise?** [T3] -- special concessions apply
9. **Is the entity registered under SVAT scheme?** [T2] -- Simplified VAT scheme for exporters
10. **Excess credit brought forward** [T1] -- from prior period

**If any of items 1-4 are unknown, STOP. Do not classify any transactions until registration type and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, EPF/ETF contributions, loan repayments, dividends = OUT OF SCOPE (never on VAT return)
- **Legislation:** VAT Act No. 14 of 2002, Section 2 (definitions of taxable supply)

### 1b. Determine Supply Location [T1]
- Domestic (within Sri Lanka)
- Import (goods/services from outside Sri Lanka)
- Export (goods/services to outside Sri Lanka)
- **Legislation:** VAT Act, Section 3 (place of supply)

### 1c. Determine VAT Rate [T1]
- **Standard rate:** 18%
- **Zero-rated:** Exports, certain essential goods per Gazette
- **Exempt:** Listed in First Schedule of VAT Act (financial services, residential rent, healthcare, education, unprocessed agricultural products, public transport)
- **Legislation:** VAT Act, Section 2 (rates); First Schedule (exemptions)

### 1d. Determine Expense Category [T1]
- Capital goods: assets with useful life > 1 year and value above threshold
- Trading stock: goods purchased for resale
- Services/overheads: rent, utilities, professional fees, etc.
- **Legislation:** VAT Act, Section 22 (input tax definitions)

---

## Step 2: VAT Return Form Structure [T1]

**Legislation:** VAT Act; IRD VAT Return Form.

### VAT Return Sections

| Section | Description |
|---------|-------------|
| Part A | Taxpayer information (TIN, VAT number, period) |
| Part B | Output tax on taxable supplies |
| Part C | Zero-rated supplies |
| Part D | Exempt supplies |
| Part E | Total supplies |
| Part F | Output tax payable |
| Part G | Input tax on local purchases |
| Part H | Input tax on imports |
| Part I | Total input tax credit |
| Part J | Net VAT payable or refundable |
| Part K | Adjustments (credit notes, debit notes) |
| Part L | Total payable after adjustments |

### Output Tax Classification

| Supply Type | Rate | Return Section |
|-------------|------|----------------|
| Standard domestic supply | 18% | Part B |
| Zero-rated supply (exports) | 0% | Part C |
| Exempt supply | N/A | Part D |

### Input Tax Classification

| Purchase Type | Source | Return Section |
|---------------|--------|----------------|
| Local purchases (VAT paid) | Tax invoices | Part G |
| Imports (VAT paid at customs) | Customs declarations (CUSDEC) | Part H |

---

## Step 3: Input Tax Credit Mechanism [T1]

**Legislation:** VAT Act, Sections 22-28.

### Eligibility for Input Tax Credit

1. The purchase must relate to making taxable supplies [T1]
2. A valid tax invoice must be held [T1]
3. The supplier must be VAT registered [T1]
4. The claim must be made within the relevant return period or subsequent adjustment period [T1]
5. The goods/services must have been received [T1]

### Input Tax Credit Apportionment [T2]

If the business makes both taxable and exempt supplies:
```
Creditable Input Tax = Total Input Tax x (Value of Taxable Supplies / Value of Total Supplies)
```
**Flag for reviewer: apportionment calculation must be confirmed. Annual adjustment based on actual ratios required.**

### Input Tax on Capital Goods [T1]

- Full credit in the period of acquisition if used entirely for taxable supplies
- If mixed use, apportionment applies [T2]
- Adjustment required if use changes within 5 years (immovable property) or 3 years (movable property)

---

## Step 4: Deductibility Check

### Blocked Input Tax Credit [T1]

**Legislation:** VAT Act, Section 22(4)-(5).

These have ZERO input tax credit regardless of anything else:

- Motor vehicles for personal transport (unless in transport/rental business)
- Entertainment expenses (meals, hospitality) unless directly related to business with documentation
- Goods and services for personal use of directors/employees
- Club membership fees
- Goods/services used exclusively for making exempt supplies
- Purchases without valid tax invoice
- Purchases from non-VAT-registered suppliers
- Petroleum products for non-commercial vehicles

Blocked categories OVERRIDE any other credit rule. Check blocked FIRST.

### Registration-Based Recovery [T1]
- VAT registered: full input tax credit (subject to category rules and apportionment)
- Not VAT registered: NO input tax credit

---

## Step 5: SVAT Scheme (Simplified VAT) -- ABOLISHED [T2]

**Legislation:** VAT Act, Section 25A (repealed effective 1 October 2025).

**IMPORTANT: The SVAT scheme was abolished effective 1 October 2025.** It has been replaced by a Risk-Based Refund Mechanism for eligible exporters and VAT-registered persons supplying to specified projects. Under the new mechanism, refunds of excess input tax must be processed within 45 days of filing.

### How SVAT Previously Worked (Historical Reference Only)
1. Buyer (SVAT registered) issued an SVAT credit voucher to the supplier
2. Supplier charged 0% VAT on the invoice (instead of 18%)
3. Supplier claimed the SVAT credit voucher against their own output VAT liability
4. Buyer did not pay VAT upfront; no input credit claim needed

### Post-SVAT: Risk-Based Refund Mechanism
- Exporters and specified suppliers now pay standard 18% VAT on purchases
- Excess input tax credits are refunded under the new risk-based refund process
- Refund target: within 45 days of filing
- Legal challenges to the abolishment have been filed by business chambers

**Flag for reviewer: SVAT is no longer available. Exporters must now use the risk-based refund mechanism. Verify current refund processing timelines and eligibility criteria.**

---

## Step 6: Import VAT [T1]

**Legislation:** VAT Act, Section 14; Customs Ordinance.

### VAT on Imports
- VAT is payable at the point of importation
- Calculated on: CIF value + Customs Duty + Ports and Airports Development Levy (PAL) + Cess + other applicable levies
- Rate: 18% (standard rate)
- Paid to Sri Lanka Customs at time of clearing goods
- Recoverable as input tax credit if goods used for taxable supplies

### Documentation Required
- Customs Declaration (CUSDEC)
- Import invoice
- Bill of Lading / Airway Bill
- Payment receipts from Customs

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory VAT registration | Annual turnover > LKR 60 million (reducing to LKR 36 million from 1 April 2026) |
| Voluntary registration | Below threshold but may register voluntarily |
| Capital goods adjustment period (movable) | 3 years |
| Capital goods adjustment period (immovable) | 5 years |
| SVAT eligibility (export ratio) | ABOLISHED from 1 October 2025; replaced by Risk-Based Refund Mechanism |

---

## Step 8: Filing Deadlines [T1]

| Category | Period | Deadline |
|----------|--------|----------|
| Monthly filers | Monthly | On or before 20th of following month |
| Quarterly filers | Quarterly | On or before 20th of month following quarter end |
| Annual return | Annual | With income tax return deadline |
| Payment | Same as return | Same deadline as return filing |

### Quarterly Periods

| Quarter | Period | Due Date |
|---------|--------|----------|
| Q1 | January - March | 20 April |
| Q2 | April - June | 20 July |
| Q3 | July - September | 20 October |
| Q4 | October - December | 20 January |

### Late Filing Penalties [T1]

| Default | Penalty |
|---------|---------|
| Late filing | LKR 50,000 or 5% of tax, whichever is higher |
| Late payment | 1.5% per month (or part) on unpaid amount |
| Non-filing | Assessment by CGIR + penalties |
| Failure to register | LKR 50,000 + retrospective registration |
| Incorrect return | Up to 100% of understated tax |

---

## Step 9: Derived Calculations [T1]

```
Total Output Tax       = VAT on all standard-rated supplies
Total Input Tax        = VAT on local purchases + VAT on imports
Adjustment             = Credit notes (reduce output) + Debit notes (increase output)
Net VAT Payable        = Total Output Tax - Total Input Tax + Adjustments - Credit B/F
If Net < 0             = Refundable or carried forward
Total Payable          = Net VAT Payable + Penalties/Interest (if any)
```

---

## Step 10: Refund Mechanism [T2]

**Legislation:** VAT Act, Section 29-30.

### Refund Eligibility
- Exporters with excess input tax credits (consistently in credit position)
- SVAT-registered entities with accumulated credits
- Entities ceasing business with remaining credits

### Refund Process
1. Apply via IRD e-Services portal or manual application
2. IRD may audit before processing refund
3. Processing time: typically 30-90 days (may take longer)
4. Refund paid via cheque or bank transfer

**Flag for reviewer: refund applications often trigger audits. Ensure all documentation is complete before applying.**

---

## PROHIBITIONS [T1]

- NEVER allow unregistered entities to claim input tax credit
- NEVER classify exempt supplies as zero-rated
- NEVER accept input tax credit without valid tax invoice from VAT-registered supplier
- NEVER apply input tax credit on blocked categories (motor vehicles, entertainment, personal use)
- NEVER accept SVAT credit vouchers -- the SVAT scheme was abolished from 1 October 2025
- NEVER ignore import VAT as a claimable input (it is recoverable if used for taxable supplies)
- NEVER mix up TIN and VAT registration number -- they are separate identifiers
- NEVER file return without reconciling input/output registers to the return form
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 11: Edge Case Registry

### EC1 -- SVAT credit voucher (legacy / transitional) [T2]
**Situation:** Supplier issues SVAT credit voucher after 1 October 2025.
**Resolution:** SVAT scheme was abolished from 1 October 2025. No SVAT credit vouchers should be issued or accepted. Buyer must pay full 18% VAT. Supplier must issue standard tax invoice. Claim input credit normally. Excess input credits are refunded under the Risk-Based Refund Mechanism.
**Legislation:** VAT Act, Section 25A (repealed); Budget 2026 measures.

### EC2 -- Import of services (reverse charge) [T2]
**Situation:** Client purchases consulting services from a foreign firm with no Sri Lanka presence.
**Resolution:** Client must self-assess VAT at 18% on the service value. Report as deemed supply in the return. May claim input credit if service relates to taxable supplies. Flag for reviewer: confirm service classification.
**Legislation:** VAT Act, Section 14(2).

### EC3 -- Mixed supply: taxable and exempt components [T2]
**Situation:** Financial institution provides both taxable and VAT-exempt services.
**Resolution:** Input tax credit must be apportioned. Only the portion relating to taxable supplies is creditable. Annual adjustment required. Flag for reviewer.

### EC4 -- Credit notes for price adjustments [T1]
**Situation:** Supplier issues credit note reducing the price of previously supplied goods.
**Resolution:** Supplier reduces output tax in the period of credit note. Buyer reduces input tax credit in the same period. Both parties adjust their records.

### EC5 -- BOI enterprise supplies [T3]
**Situation:** Client supplies goods to a BOI-approved enterprise under a special agreement.
**Resolution:** BOI enterprises may have VAT exemptions or concessionary rates under their agreements. Do not classify. Escalate to practitioner to review the specific BOI agreement.
**Legislation:** BOI Act; specific BOI agreement terms.

### EC6 -- VAT on digital services from non-resident providers [T2]
**Situation:** Client subscribes to cloud services from a US-based company.
**Resolution:** Non-resident digital service providers may be required to register for VAT in Sri Lanka. If not registered, the recipient may need to account for VAT under reverse charge. Flag for reviewer: confirm current rules on digital services as they are evolving.

### EC7 -- Tourism sector supplies [T1]
**Situation:** Hotel provides accommodation and food to tourists.
**Resolution:** All supplies at standard 18% rate. No reduced rate for tourism. Input tax credit on hotel supplies (food, amenities, maintenance) fully recoverable if hotel is VAT registered.

### EC8 -- Disposal of capital goods within adjustment period [T2]
**Situation:** Client sells machinery after 2 years (within 3-year adjustment period).
**Resolution:** Adjustment required. Proportional claw-back of input tax credit for remaining adjustment period. Flag for reviewer: calculate adjustment amount.
**Legislation:** VAT Act, Section 27.

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

### Test 1 -- Standard local sale at 18%
**Input:** Domestic sale of electronic goods, net LKR 500,000, VAT LKR 90,000. VAT registered client.
**Expected output:** Part B: Net LKR 500,000, Output VAT LKR 90,000.

### Test 2 -- Local purchase with input tax credit
**Input:** Purchase of office supplies from VAT-registered supplier, net LKR 100,000, VAT LKR 18,000 (18%). Valid tax invoice held.
**Expected output:** Part G: Input VAT LKR 18,000. Full credit allowed.

### Test 3 -- Import with customs VAT
**Input:** Import of raw materials, CIF value LKR 2,000,000. Customs duty LKR 200,000. PAL LKR 100,000. VAT at 18% on LKR 2,300,000 = LKR 414,000.
**Expected output:** Part H: Input VAT LKR 414,000. Credit allowed if used for taxable supplies.

### Test 4 -- Export (zero-rated)
**Input:** Export of tea, FOB value LKR 5,000,000. All export documentation complete.
**Expected output:** Part C: LKR 5,000,000 at 0%. No output VAT. Input tax credit on related purchases fully recoverable.

### Test 5 -- Blocked input: director's car
**Input:** VAT registered company purchases a car for managing director, LKR 8,000,000, VAT LKR 1,440,000.
**Expected output:** Input VAT LKR 0 (BLOCKED -- personal transport vehicle). Full cost capitalized without VAT recovery.

### Test 6 -- Post-SVAT exporter purchase (Risk-Based Refund)
**Input:** Exporter purchases fabric from VAT-registered supplier, LKR 1,000,000. VAT LKR 180,000 (18%). SVAT no longer available.
**Expected output:** VAT charged at 18%. Exporter claims input tax credit of LKR 180,000. Excess input credits refunded under Risk-Based Refund Mechanism (target: within 45 days of filing).

### Test 7 -- Apportionment for mixed supplies
**Input:** Financial institution with 60% taxable and 40% exempt supplies. Total input VAT for period LKR 300,000.
**Expected output:** Creditable input VAT = LKR 300,000 x 60% = LKR 180,000. Blocked portion = LKR 120,000.

### Test 8 -- Late payment penalty
**Input:** VAT payable LKR 500,000. Filed and paid 45 days late (2 months overdue including part month).
**Expected output:** Penalty: LKR 50,000 or 5% of LKR 500,000 = LKR 25,000 -- whichever is higher = LKR 50,000. Interest: 1.5% x 2 months x LKR 500,000 = LKR 15,000. Total additional: LKR 65,000.

---

## Step 14: Invoice Requirements [T1]

**Legislation:** VAT Act, Section 20.

### Mandatory Contents of VAT Invoice
1. Supplier's name, address, TIN, and VAT registration number
2. Buyer's name, address, and VAT number (if registered)
3. Date of issue
4. Sequential invoice number
5. Description of goods/services
6. Quantity and unit price
7. Total value before VAT
8. VAT rate and VAT amount
9. Total value including VAT

### Types of Invoices
- **Full Tax Invoice:** For supplies to VAT-registered buyers (enables input credit)
- **Simplified Invoice:** For retail sales under LKR 5,000
- **SVAT Credit Voucher:** Issued by SVAT-registered buyers to suppliers

---

## Step 15: Record Keeping [T1]

**Legislation:** VAT Act, Section 31.

### Mandatory Records (retain for 5 years minimum)
1. All purchase and sales invoices
2. VAT account / control account
3. Import and export documentation (CUSDEC, Bills of Lading)
4. Bank statements and payment receipts
5. General ledger and journals
6. Stock records (for trading businesses)
7. SVAT credit vouchers (historical records prior to 1 October 2025 abolishment)
8. Credit and debit notes

---

## Step 16: Specific Sector Rules

### Financial Services [T2]
**Legislation:** VAT Act, First Schedule.

- Most financial services are exempt (interest on loans, insurance premiums, currency exchange)
- However, fee-based services (advisory, custodian, brokerage commissions) are taxable at 18%
- Financial institutions must carefully segregate exempt and taxable activities
- Input credit apportionment mandatory for banks and insurance companies
- **Flag for reviewer: financial sector classification is complex. Confirm with practitioner.**

### Telecommunications [T1]
- All telecom services subject to VAT at 18%
- Telecom Levy is a SEPARATE obligation (not part of VAT)
- Input credit on network equipment and infrastructure allowed
- SIM card sales: taxable at 18%

### Construction and Real Estate [T2]
- Construction services: taxable at 18%
- Sale of completed buildings: taxable at 18%
- Residential rental: exempt
- Commercial rental: taxable at 18%
- Input credit on construction materials allowed if for taxable supplies
- **Flag for reviewer: mixed-use buildings require apportionment.**

---

## Step 17: Penalties Detailed Summary [T1]

| Offence | Penalty |
|---------|---------|
| Failure to register | LKR 50,000 + retrospective registration |
| Late filing | LKR 50,000 or 5% of tax (whichever higher) |
| Late payment | 1.5% per month on unpaid amount |
| Non-issuance of invoice | LKR 25,000 per instance |
| Fraudulent invoice | 200% of VAT + criminal prosecution |
| Failure to maintain records | LKR 25,000 |
| Under-declaration | Up to 100% of understated tax |
| Tax evasion | Criminal prosecution, imprisonment up to 5 years |
| Obstruction of officers | LKR 50,000 |
| Failure to furnish information | LKR 25,000 per instance |

---

## Step 18: Audit and Appeals [T2]

**Legislation:** Inland Revenue Act No. 24 of 2017; Tax Appeals Commission Act.

### Audit Process
1. CGIR may audit any return within **4 years** (6 years for fraud)
2. Desk audits and field audits
3. Taxpayer must provide records within 30 days of request
4. Assessment issued after audit

### Appeals
1. File objection with CGIR within **30 days** of assessment
2. Appeal to Tax Appeals Commission within **30 days** of objection determination
3. Further appeal to Court of Appeal on points of law

**Any audit or assessment situation requires immediate escalation to qualified practitioner.**

---

## Contribution Notes

This skill must be validated by a qualified chartered accountant practicing in Sri Lanka before use in production. All T1 rules must be verified against the latest Gazette Notifications and amendments to the VAT Act.

**A skill may not be published without sign-off from a qualified practitioner in Sri Lanka.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
