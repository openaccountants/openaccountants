---
name: nepal-vat
description: Use this skill whenever asked to prepare, review, or create a Nepal VAT return or any VAT filing for a Nepalese business. Trigger on phrases like "prepare VAT return", "Nepal VAT", "IRD filing", "PAN registration", or any request involving Nepal VAT. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Nepal VAT classification rules, return form mappings, input tax credit rules, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Nepal VAT-related work.
---

# Nepal VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Nepal |
| Jurisdiction Code | NP |
| Primary Legislation | Value Added Tax Act 2052 (1996) |
| Supporting Legislation | VAT Rules 2053 (1997); Finance Act (annual amendments) |
| Tax Authority | Inland Revenue Department (IRD), Ministry of Finance |
| Filing Portal | https://ird.gov.np (IRD Online Portal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending local practitioner validation |
| Validation Date | Pending |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: standard rate classification, input-output mapping, return fields. Tier 2: partial credit, sector exemptions, reverse charge on imports. Tier 3: complex group structures, SEZ enterprises, bilateral treaty exemptions. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and PAN (Permanent Account Number)** [T1] -- 9-digit PAN issued by IRD
2. **VAT registration status** [T1] -- Mandatory VAT registered, Voluntary, or Small taxpayer (below threshold)
3. **VAT period** [T1] -- monthly (standard)
4. **Industry/sector** [T2] -- impacts exemptions (e.g., agriculture, healthcare, education)
5. **Does the business make exempt supplies?** [T2] -- If yes, input tax credit apportionment required
6. **Does the business import goods?** [T1] -- impacts customs-stage VAT
7. **Does the business export goods/services?** [T1] -- impacts zero-rating
8. **Excess credit brought forward** [T1] -- from prior period
9. **Is the entity in a Special Economic Zone (SEZ)?** [T3] -- special rules apply
10. **Fiscal year** [T1] -- Nepal uses Bikram Sambat calendar; fiscal year is Shrawan to Ashad (mid-July to mid-July)

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration type and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, provident fund, loan repayments, dividends = OUT OF SCOPE (never on VAT return)
- **Legislation:** VAT Act 2052, Section 2 (definitions)

### 1b. Determine Supply Location [T1]
- Domestic (within Nepal)
- Import (goods/services from outside Nepal)
- Export (goods/services to outside Nepal)
- **Legislation:** VAT Act 2052, Section 8 (place of supply)

### 1c. Determine VAT Rate [T1]
- **Standard rate:** 13%
- **Zero-rated:** Exports of goods and services, supplies to diplomats
- **Exempt:** Listed in Schedule 1 of VAT Act 2052:
  - Basic agricultural products (unprocessed)
  - Basic necessities (rice, flour, pulses, fresh vegetables, fresh fruits)
  - Educational services
  - Healthcare / hospital services
  - Public transportation (excluding air and tourist vehicles)
  - Books, newspapers, periodicals
  - Financial and insurance services (interest, premium)
  - Residential rent
  - Electricity (up to certain limit)
  - Precious metals (gold, silver in raw form)
- **Legislation:** VAT Act 2052, Section 5 (rate); Schedule 1 (exemptions); Schedule 2 (zero-rated)

### 1d. Determine Expense Category [T1]
- Capital goods: fixed assets with useful life > 1 year
- Trading stock: goods purchased for resale
- Raw materials: inputs consumed in production
- Services/overheads: rent, utilities, professional fees
- **Legislation:** VAT Act 2052, Section 2 (definitions)

---

## Step 2: VAT Return Form Structure [T1]

**Legislation:** VAT Act 2052; VAT Rules 2053; IRD prescribed return form.

### Nepal VAT Return Sections

| Section | Description |
|---------|-------------|
| Part 1 | Taxpayer information (PAN, name, period) |
| Part 2 | Sales/output details |
| 2.1 | Taxable sales (13%) |
| 2.2 | Tax-exempt sales |
| 2.3 | Zero-rated sales (exports) |
| 2.4 | Total sales |
| Part 3 | Output VAT |
| 3.1 | VAT collected on taxable sales (13%) |
| Part 4 | Purchase/input details |
| 4.1 | Taxable purchases (domestic) |
| 4.2 | Taxable purchases (imports) |
| 4.3 | Non-taxable purchases |
| 4.4 | Total purchases |
| Part 5 | Input VAT |
| 5.1 | VAT on domestic purchases |
| 5.2 | VAT on imports |
| 5.3 | Total input VAT |
| Part 6 | Tax payable / refundable |
| 6.1 | Net tax (Output VAT - Input VAT) |
| 6.2 | Credit brought forward |
| 6.3 | Total payable or credit carried forward |

### Output Tax Classification

| Supply Type | Rate | Return Section |
|-------------|------|----------------|
| Standard domestic supply | 13% | Part 2.1 |
| Tax-exempt supply | N/A | Part 2.2 |
| Export (zero-rated) | 0% | Part 2.3 |

### Input Tax Classification

| Purchase Type | Source | Return Section |
|---------------|--------|----------------|
| Domestic purchases (VAT paid) | Tax invoices | Part 4.1 / 5.1 |
| Imports (VAT paid at customs) | Customs declarations | Part 4.2 / 5.2 |
| Non-taxable purchases | -- | Part 4.3 (no credit) |

---

## Step 3: Input Tax Credit Mechanism [T1]

**Legislation:** VAT Act 2052, Section 17-18.

### Eligibility for Input Tax Credit

1. The purchase must relate to making taxable (including zero-rated) supplies [T1]
2. A valid tax invoice must be held [T1]
3. The supplier must be VAT registered (PAN with VAT registration) [T1]
4. The claim must be made within the relevant return period [T1]
5. The goods/services must have been actually received [T1]

### Input Tax Credit Apportionment [T2]

If the business makes both taxable and exempt supplies:
```
Creditable Input Tax = Total Input Tax x (Taxable Supplies / Total Supplies)
```
**Flag for reviewer: apportionment must be confirmed. Adjustment at year-end based on actual ratios.**

### Input Tax Credit on Capital Goods [T1]

- Full credit in the period of acquisition if used entirely for taxable supplies
- If mixed use, apportionment applies [T2]
- Capital goods adjustment: if use changes within adjustment period, clawback required

---

## Step 4: Deductibility Check

### Blocked Input Tax Credit [T1]

**Legislation:** VAT Act 2052, Section 17(3).

These have ZERO input tax credit:

- Alcoholic beverages and tobacco products
- Petroleum products for non-commercial vehicles
- Entertainment and hospitality expenses (unless directly in hospitality business)
- Motor vehicles for personal use (unless transport/rental business)
- Personal consumption of directors/partners/proprietors
- Goods and services used exclusively for exempt supplies
- Purchases without valid tax invoice
- Purchases from non-registered vendors
- Gifts and donations (unless documented promotional samples)

Blocked categories OVERRIDE any other credit rule. Check blocked FIRST.

### Registration-Based Recovery [T1]
- VAT registered: full input tax credit (subject to category rules)
- Small taxpayer (below threshold): NO input tax credit (simplified regime)
- Not registered: NO input tax credit

---

## Step 5: Reverse Charge on Imported Services [T2]

**Legislation:** VAT Act 2052, Section 8(3); Section 12.

### When Reverse Charge Applies
- Services received from a non-resident provider who has no business establishment in Nepal
- The recipient (Nepalese business) must self-assess VAT at 13%

### Treatment on Return
1. Include the value of imported service in Part 2.1 (output / taxable supplies)
2. Self-assess VAT at 13% in Part 3.1
3. If service relates to taxable supplies, claim input credit in Part 5
4. Net effect: zero for fully taxable businesses

**Flag for reviewer: confirm service type and whether it qualifies for input credit.**

---

## Step 6: Excise Duty Interaction [T1]

**Legislation:** Excise Act 2058 (2002).

- Excise duty applies to specified goods (alcohol, tobacco, cement, iron rods, vehicles, etc.)
- Excise duty is calculated BEFORE VAT
- VAT is applied on (value + excise duty)
- Excise duty is NOT recoverable as input tax credit (it is a separate levy)

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory VAT registration | Annual turnover > NPR 5 million (goods only) or NPR 3 million (services only, or mixed goods and services) -- revised from earlier NPR 2 million for services |
| Voluntary registration | Below threshold but may register voluntarily |
| Small taxpayer limit | Below registration threshold |
| Input tax credit time limit | Within the return period (monthly) |

---

## Step 8: Filing Deadlines [T1]

| Category | Period | Deadline |
|----------|--------|----------|
| VAT registered | Monthly | Within 25 days after end of Nepali month |
| Payment | Monthly | Same deadline as return filing |
| Annual reconciliation | Annual | Within 3 months of fiscal year end |

### Nepal Calendar Note [T1]
Nepal uses the Bikram Sambat (BS) calendar. The fiscal year runs from 1 Shrawan to 31 Ashad (approximately mid-July to mid-July in the Gregorian calendar). VAT periods follow BS months. The 25-day deadline is measured from the end of each BS month.

### Late Filing Penalties [T1]

| Default | Penalty |
|---------|---------|
| Late filing | NPR 1,000 per day of delay (up to maximum) |
| Late payment | 15% per annum interest on unpaid amount |
| Non-filing | Assessment by IRD + penalties |
| Failure to register | Retrospective registration + penalties |
| Incorrect return | Up to 100% of understated tax + interest |
| Tax evasion | Criminal prosecution possible |

---

## Step 9: Derived Calculations [T1]

```
Total Output VAT       = VAT on all standard-rated supplies (13%)
Total Input VAT        = VAT on domestic purchases + VAT on imports
Net VAT Payable        = Total Output VAT - Total Input VAT - Credit B/F
If Net < 0             = Credit carried forward to next period
Total Payable          = Net VAT Payable + Interest/Penalty (if any)
```

---

## Step 10: Refund Mechanism [T2]

**Legislation:** VAT Act 2052, Section 24-25.

### Refund Eligibility
- Exporters with accumulated input tax credits for 6+ consecutive months
- Diplomatic missions and international organizations
- Entities ceasing business

### Refund Process
1. Apply to IRD office with all supporting documentation
2. IRD may conduct desk audit or field audit
3. Processing time: typically 30-90 days
4. Refund capped at input tax relating to zero-rated supplies

**Flag for reviewer: refund applications trigger audits. Documentation must be meticulous.**

---

## Step 11: Invoice Requirements [T1]

**Legislation:** VAT Act 2052, Section 14; VAT Rules 2053.

### Mandatory Contents of VAT Invoice
1. Seller's name, address, PAN, and VAT registration number
2. Buyer's name and PAN (if registered)
3. Date of issue
4. Sequential invoice number
5. Description of goods/services
6. Quantity and unit price
7. Total amount before VAT
8. VAT amount (13%)
9. Total amount including VAT

### Invoice Types
- Tax Invoice: for VAT-registered buyers (enables input credit)
- Abbreviated Invoice: for retail sales below NPR 5,000 (less detail required)

---

## PROHIBITIONS [T1]

- NEVER allow unregistered entities to claim input tax credit
- NEVER classify exempt supplies as zero-rated
- NEVER accept input tax credit without valid tax invoice from registered supplier
- NEVER apply input tax credit on blocked categories
- NEVER ignore the Bikram Sambat calendar when determining filing deadlines
- NEVER treat excise duty as input VAT -- excise is a separate non-creditable levy
- NEVER allow input credit on purchases for personal consumption
- NEVER file return without reconciling purchase/sales registers
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 12: Edge Case Registry

### EC1 -- Reverse charge on imported digital services [T2]
**Situation:** Nepalese company subscribes to cloud software from a US provider.
**Resolution:** Reverse charge applies. Self-assess VAT at 13% on the subscription value. Claim input credit if service relates to taxable supplies. Flag for reviewer: confirm classification.
**Legislation:** VAT Act 2052, Section 8(3).

### EC2 -- Mixed supply: taxable and exempt [T2]
**Situation:** A hospital provides both taxable (cosmetic surgery) and exempt (general healthcare) services.
**Resolution:** Input tax credit must be apportioned. Only the portion relating to taxable supplies is creditable. Flag for reviewer: confirm apportionment ratio.

### EC3 -- Capital goods sold within adjustment period [T2]
**Situation:** Client sells office equipment purchased 1 year ago with full input credit claimed.
**Resolution:** Adjustment may be required to reverse proportional input credit for remaining useful life. Flag for reviewer: calculate adjustment.

### EC4 -- Credit notes for returned goods [T1]
**Situation:** Customer returns goods and credit note issued.
**Resolution:** Seller reduces output VAT in the period of credit note. Buyer reverses input tax credit. Both update purchase/sales registers.

### EC5 -- Goods purchased for employee welfare [T1]
**Situation:** Company purchases tea, snacks, and supplies for employee consumption.
**Resolution:** Input tax credit is BLOCKED -- personal consumption/welfare. No credit regardless of business justification.
**Legislation:** VAT Act 2052, Section 17(3).

### EC6 -- Construction of own building [T2]
**Situation:** Company constructs its own office building, purchasing materials with VAT.
**Resolution:** If building will be used for taxable business activities, input tax credit is allowed on construction materials and services. If building will be rented (exempt supply), input credit is blocked. If mixed use, apportioned. Flag for reviewer.

### EC7 -- Advance payments [T1]
**Situation:** Client receives advance payment for future supply of goods.
**Resolution:** VAT is chargeable at the earlier of: receipt of payment or delivery of goods. Advance payment triggers VAT obligation. Include in output tax for the period received.
**Legislation:** VAT Act 2052, Section 6 (time of supply).

### EC8 -- Import of goods with multiple duties [T1]
**Situation:** Import of goods subject to customs duty, excise duty, and VAT.
**Resolution:** Customs duty and excise duty are added to the customs value. VAT at 13% is computed on (customs value + customs duty + excise duty + other levies). Only the VAT component is claimable as input credit. Customs duty and excise are NOT recoverable.

---

## Step 13: Reviewer Escalation Protocol

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

## Step 14: Test Suite

### Test 1 -- Standard local sale at 13%
**Input:** Domestic sale of furniture, net NPR 200,000, VAT NPR 26,000. VAT registered client.
**Expected output:** Part 2.1: NPR 200,000. Part 3.1: Output VAT NPR 26,000.

### Test 2 -- Local purchase with input tax credit
**Input:** Purchase of raw materials from VAT-registered supplier, net NPR 100,000, VAT NPR 13,000. Valid tax invoice held.
**Expected output:** Part 4.1: NPR 100,000. Part 5.1: Input VAT NPR 13,000. Full credit.

### Test 3 -- Import with customs VAT
**Input:** Import of equipment, CIF NPR 1,000,000. Customs duty NPR 50,000. Excise NPR 30,000. VAT at 13% on NPR 1,080,000 = NPR 140,400.
**Expected output:** Part 4.2 / 5.2: Input VAT NPR 140,400. Credit allowed. Customs duty and excise NOT creditable.

### Test 4 -- Export (zero-rated)
**Input:** Export of handicrafts, FOB NPR 500,000. All documentation complete.
**Expected output:** Part 2.3: NPR 500,000 at 0%. No output VAT. Input credit fully recoverable.

### Test 5 -- Blocked input: alcohol for office party
**Input:** VAT registered company purchases alcohol NPR 50,000, VAT NPR 6,500.
**Expected output:** Input VAT NPR 0 (BLOCKED -- alcohol).

### Test 6 -- Reverse charge on imported services
**Input:** Nepalese company pays NPR 300,000 to Indian consulting firm for advisory services.
**Expected output:** Self-assess output VAT: NPR 39,000 (13%). Claim input credit: NPR 39,000 (if used for taxable supplies). Net effect: zero.

### Test 7 -- Credit note adjustment
**Input:** Client issued credit note for NPR 50,000 (net) + NPR 6,500 (VAT) for returned goods.
**Expected output:** Reduce Part 2.1 by NPR 50,000. Reduce Part 3.1 by NPR 6,500. Buyer reverses NPR 6,500 input credit.

### Test 8 -- Exempt supply: educational services
**Input:** School receives tuition fees NPR 1,000,000 for the month.
**Expected output:** Part 2.2: NPR 1,000,000. No output VAT. No input tax credit on related purchases.

---

## Step 15: Record Keeping Requirements [T1]

**Legislation:** VAT Act 2052, Section 16; VAT Rules 2053.

### Mandatory Records (retain for 6 years minimum)
1. Purchase register (with VAT details)
2. Sales register (with VAT details)
3. All tax invoices (issued and received)
4. Import/export documentation (customs declarations, transport docs)
5. Bank statements and payment records
6. Stock/inventory records
7. Credit and debit notes
8. Asset register (for capital goods)
9. General ledger and journals

---

## Step 16: Specific Sector Rules

### Tourism and Hospitality [T1]
- Hotel accommodation: taxable at 13%
- Restaurant services: taxable at 13%
- Trekking and mountaineering services: taxable at 13%
- Input credit on hotel supplies and equipment allowed
- Tourism Development Fee is SEPARATE from VAT

### Construction [T2]
- Construction services: taxable at 13%
- Government construction contracts: VAT at 13%, may have withholding
- Input credit on construction materials allowed
- **Flag for reviewer: confirm contract terms for government projects**

### Financial Services [T1]
- Banking services (interest): exempt
- Insurance premiums: exempt
- Fee-based services (commissions, advisory): taxable at 13%
- Money exchange: exempt

---

## Step 17: Penalties Detailed Summary [T1]

**Legislation:** VAT Act 2052, Section 29; Revenue Administration Act.

| Offence | Penalty |
|---------|---------|
| Failure to register | NPR 10,000 + retrospective registration |
| Late filing | NPR 1,000 per day of delay |
| Late payment | 15% per annum interest |
| Non-issuance of invoice | NPR 5,000 per instance |
| Fraudulent invoice | 200% of VAT + criminal prosecution |
| Failure to maintain records | NPR 10,000 |
| Under-declaration | 100% of understated tax + interest |
| Tax evasion | Criminal prosecution, imprisonment up to 3 years |
| Obstruction of tax officer | NPR 25,000 |
| Non-cooperation with audit | NPR 10,000 per instance |

---

## Step 18: Audit and Appeals [T2]

### Audit Process
1. IRD may audit within **4 years** of filing (6 years for fraud)
2. Desk audits and field audits
3. Taxpayer must provide records within 15 days of request

### Appeals
1. File objection with IRD within **30 days** of assessment
2. Appeal to Revenue Tribunal within **35 days**
3. Further appeal to Appellate Court

---

## Contribution Notes

This skill must be validated by a qualified Chartered Accountant (CA) registered with the Institute of Chartered Accountants of Nepal (ICAN) before use in production. All T1 rules must be verified against the latest Finance Act amendments.

**A skill may not be published without sign-off from a qualified practitioner in Nepal.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
