---
name: myanmar-ct
description: Use this skill whenever asked to prepare, review, or create a Myanmar Commercial Tax return or any CT filing for a Myanmar business. Trigger on phrases like "commercial tax", "Myanmar CT", "IRD filing Myanmar", "CT return", or any request involving Myanmar commercial tax. Also trigger when classifying transactions for CT purposes from bank statements, invoices, or other source data. This skill contains the complete Myanmar Commercial Tax classification rules, return form mappings, input tax credit rules, and filing deadlines. ALWAYS read this skill before touching any Myanmar CT-related work.
---

# Myanmar Commercial Tax Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Myanmar |
| Jurisdiction Code | MM |
| Primary Legislation | Commercial Tax Law (amended 2018) |
| Supporting Legislation | Commercial Tax Rules; Union Tax Law (annual, sets rates); Notifications by IRD |
| Tax Authority | Internal Revenue Department (IRD), Ministry of Planning, Finance and Industry |
| Filing Portal | IRD Myanmar offices (limited online capability; paper-based filing common) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending local practitioner validation |
| Validation Date | Pending |
| Last Verified | 2026-04-10 -- web-research cross-check of rates, thresholds, deadlines |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: standard rate classification, input-output mapping, return structure. Tier 2: sector-specific rates, special goods, mediated sales. Tier 3: oil/gas, mining, complex multi-state structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and Taxpayer Identification Number (TIN)** [T1]
2. **Business type** [T1] -- manufacturer, trader, service provider, importer/exporter
3. **CT registration status** [T1] -- registered or below threshold
4. **Filing period** [T1] -- monthly or quarterly (depending on entity type and turnover)
5. **Industry/sector** [T2] -- critical for rate determination (rates vary by goods/service type)
6. **Does the business import goods?** [T1] -- CT payable at customs
7. **Does the business export goods?** [T1] -- impacts exemptions
8. **Annual turnover** [T1] -- determines whether registration threshold is met
9. **Does the business deal in special goods?** [T2] -- cigarettes, alcohol, teak, jade, petroleum
10. **Excess credit brought forward** [T1] -- from prior period

**If any of items 1-4 are unknown, STOP. Do not classify any transactions until registration type and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale/supply (output CT) or Purchase (input CT)
- Salaries, loan repayments, dividends, donations = OUT OF SCOPE (never on CT return)
- **Legislation:** Commercial Tax Law, Section 3 (definition of taxable goods and services)

### 1b. Determine Supply Location [T1]
- Domestic production/sale
- Import (goods from outside Myanmar)
- Export (goods to outside Myanmar)
- **Legislation:** Commercial Tax Law, Section 5

### 1c. Determine CT Rate [T1]
The standard rate for most goods and services is **5%**. However, rates vary significantly by category:

| Category | CT Rate |
|----------|---------|
| Most goods and services (standard) | 5% |
| Electricity | 8% |
| Cigarettes, cheroots, tobacco | 8% - 120% (tiered) |
| Alcohol / beer / wine | 60% |
| Precious stones (jade, gems) | 10% - 30% |
| Teak and hardwood | 5% - 25% |
| Gold | 1% |
| Petroleum products | 5% - 10% |
| Telecommunications | 5% |
| Hotel/tourism services | 5% |

**Note:** Specific rates are set annually by the Union Tax Law. Rates above are indicative. Always verify against the current year's Union Tax Law. [T2]

### 1d. Determine Exempt Supplies [T1]
The following are exempt from Commercial Tax:
- Agricultural products (unprocessed, domestically consumed)
- Livestock
- Fresh fish and seafood (unprocessed)
- Books and periodicals
- Certain medical supplies and equipment
- Goods for diplomatic missions
- Certain goods specified by notification
- **Legislation:** Commercial Tax Law, Schedule 1 (exempt goods/services)

---

## Step 2: CT Return Form Structure [T1]

**Legislation:** Commercial Tax Law; IRD prescribed forms.

### CT Return Sections

| Section | Description |
|---------|-------------|
| Part A | Taxpayer information (TIN, name, period) |
| Part B | Output CT on domestic sales |
| B.1 | Standard rate (5%) supplies |
| B.2 | Special rate supplies (specify rate and goods type) |
| B.3 | Exempt supplies |
| B.4 | Total domestic output CT |
| Part C | CT on imports (paid at customs) |
| Part D | Export sales (exempt from CT) |
| Part E | Input CT credit |
| E.1 | CT paid on domestic purchases |
| E.2 | CT paid on imports |
| E.3 | Total input CT credit |
| Part F | Net CT payable |
| F.1 | Total output CT - Total input CT credit |
| F.2 | Credit brought forward |
| F.3 | Net payable or credit carried forward |

### Output CT Classification

| Supply Type | Rate | Return Section |
|-------------|------|----------------|
| Standard domestic supply | 5% | B.1 |
| Special goods (alcohol, tobacco, etc.) | Variable | B.2 |
| Exempt supply | N/A | B.3 |
| Export | 0% (exempt) | Part D |

### Input CT Classification

| Purchase Type | Source | Return Section |
|---------------|--------|----------------|
| Domestic purchases (CT paid) | Tax invoices | E.1 |
| Imports (CT paid at customs) | Customs documents | E.2 |

---

## Step 3: Input Tax Credit Mechanism [T1]

**Legislation:** Commercial Tax Law, Section 12.

### Eligibility for Input CT Credit

1. CT must have been paid on the purchased goods/services [T1]
2. The purchase must relate to making taxable supplies [T1]
3. A valid invoice/receipt must be held [T1]
4. The goods/services must have been actually received [T1]

### Input CT Credit Limitations

- Input CT credit is generally available for goods and services used in the production or supply of taxable goods/services
- CT paid on imports is creditable against domestic CT liability
- No credit for CT on goods used for exempt supplies
- No credit for CT on personal consumption items

### Input CT Apportionment [T2]

If the business makes both taxable and exempt supplies:
```
Creditable Input CT = Total Input CT x (Taxable Supplies / Total Supplies)
```
**Flag for reviewer: apportionment must be confirmed.**

---

## Step 4: Deductibility Check

### Blocked Input CT Credit [T1]

**Legislation:** Commercial Tax Law, Section 12(b).

These have ZERO input CT credit:

- Goods for personal consumption of owners/directors/employees
- Motor vehicles for personal use (unless in transport business)
- Entertainment expenses (meals, hospitality)
- Gifts and donations
- Goods used exclusively for exempt supplies
- Purchases without valid documentation
- Alcohol and tobacco (unless in production/wholesale of same)

Blocked categories OVERRIDE any other credit rule. Check blocked FIRST.

### Registration-Based Recovery [T1]
- CT registered: input CT credit allowed (subject to rules)
- Not registered / below threshold: NO input CT credit

---

## Step 5: CT on Imports [T1]

**Legislation:** Commercial Tax Law, Section 9; Customs Law.

### Import CT
- CT is payable at the point of importation
- Calculated on: CIF value + Customs Duty
- Rate: applicable CT rate for the goods category
- Paid to Myanmar Customs at time of clearing
- Recoverable as input CT credit if goods used for taxable supplies

### Documentation Required
- Import Declaration
- Commercial invoice
- Bill of Lading / Airway Bill
- Customs payment receipt

---

## Step 6: CT on Exports [T1]

**Legislation:** Commercial Tax Law, Section 8.

### Export Exemption
- Exports of goods are generally exempt from CT
- Exception: certain natural resources (teak, gems, jade) may be subject to CT even on export
- Documentation: export license, customs export declaration, bill of lading

**For natural resource exports, confirm the specific CT rate under the Union Tax Law. [T2]**

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| CT registration (goods) | Annual turnover > MMK 50 million |
| CT registration (services) | Annual turnover > MMK 50 million |
| Small taxpayer exemption | Below registration threshold (simplified assessment possible) |

**Note:** Thresholds are set by IRD notifications and may change. Verify current threshold. [T2]

---

## Step 8: Filing Deadlines [T1]

| Category | Period | Deadline |
|----------|--------|----------|
| CT registered (monthly) | Monthly | Within 10 days after end of month |
| CT registered (quarterly) | Quarterly | Within 10 days after end of quarter |
| Annual return | Annual | Within 3 months after fiscal year end (31 March) |
| CT on imports | Per importation | At time of customs clearance |

### Myanmar Fiscal Year [T1]
Myanmar's fiscal year runs from 1 April to 31 March (changed from 1 October - 30 September in 2018/2019).

### Late Filing Penalties [T1]

| Default | Penalty |
|---------|---------|
| Late filing | 10% of tax due |
| Late payment | 10% of unpaid amount + interest at prescribed rate |
| Non-filing | Assessment by IRD + penalties |
| Tax evasion | Criminal prosecution, fines, imprisonment |
| Incorrect return | Up to 100% of understated tax |

---

## Step 9: Derived Calculations [T1]

```
Total Output CT        = Sum of CT on all taxable supplies (by rate category)
Total Input CT         = CT on domestic purchases + CT on imports
Net CT Payable         = Total Output CT - Total Input CT - Credit B/F
If Net < 0             = Credit carried forward
Total Payable          = Net CT Payable + Penalties/Interest (if any)
```

---

## Step 10: Specific Goods Tax (SGT) [T2]

**Legislation:** Union Tax Law (annual); Commercial Tax Law, Schedule 2.

Certain goods attract significantly higher CT rates (Specific Goods Tax):

| Goods | Rate Range |
|-------|-----------|
| Virginia cigarettes | 80% - 120% |
| Cheroots | 8% - 20% |
| Alcohol (domestic) | 60% |
| Beer | 60% |
| Wine | 50% |
| Jade (uncut) | 15% - 30% |
| Rubies and sapphires | 10% - 20% |
| Teak logs | 25% |

**These rates change annually. Always verify against the current Union Tax Law.**

---

## PROHIBITIONS [T1]

- NEVER apply a flat 5% rate without checking if the goods/services fall under special rate categories
- NEVER allow input CT credit on personal consumption items
- NEVER classify exempt goods as zero-rated -- Myanmar does not have a zero-rating concept; exports are exempt
- NEVER ignore Special Goods Tax rates for alcohol, tobacco, gems, teak
- NEVER accept input CT credit without valid documentation
- NEVER assume online filing is available -- verify with local IRD office
- NEVER file return without confirming the current Union Tax Law rates
- NEVER allow CT credit on blocked categories
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 11: Edge Case Registry

### EC1 -- Mixed goods with different CT rates [T2]
**Situation:** A single invoice contains goods subject to 5% and goods subject to special rates.
**Resolution:** Split by line item. Each goods category attracts its own rate. If line items are not separable, flag for reviewer.

### EC2 -- Imported goods subsequently exported [T2]
**Situation:** Client imports raw materials (CT paid at customs), processes them, and exports finished goods.
**Resolution:** CT paid on imports is creditable as input CT. Exports are exempt from output CT. Net effect: CT refund position. Flag for reviewer: confirm export documentation is complete.

### EC3 -- Sale of jade/gems by non-mining entity [T2]
**Situation:** Trading company sells jade purchased from a licensed miner.
**Resolution:** CT applies at the applicable rate for jade/gems. Input CT credit allowed on the purchase if CT was charged. Verify rate against Union Tax Law. Flag for reviewer: confirm licensing status.
**Legislation:** Commercial Tax Law; Union Tax Law.

### EC4 -- Foreign currency transactions [T1]
**Situation:** Client invoices in USD for exported goods.
**Resolution:** Convert to MMK at the Central Bank of Myanmar reference rate on the date of supply for CT purposes. Export exemption applies if documentation is complete. No CT on exports (except specified resources).

### EC5 -- Barter/exchange transactions [T1]
**Situation:** Client exchanges goods with another party without monetary consideration.
**Resolution:** CT applies on the fair market value of the goods supplied. Output CT must be self-assessed on market value. Issue appropriate documentation.
**Legislation:** Commercial Tax Law, Section 6.

### EC6 -- Construction services [T1]
**Situation:** Construction company provides building services.
**Resolution:** CT at 5% on the contract value. Input CT credit on materials purchased with valid documentation. If contract is a turnkey/lump-sum, CT on full contract value.

### EC7 -- Goods lost or destroyed [T1]
**Situation:** Inventory destroyed by fire; input CT was previously claimed.
**Resolution:** If goods are insured, no immediate reversal (insurance payout may attract CT). If uninsured, input CT credit must be reversed in the period of loss.

### EC8 -- Telecommunications services [T1]
**Situation:** Mobile operator provides voice, data, and value-added services.
**Resolution:** CT at 5% on all telecom services. Input CT credit on infrastructure and equipment purchases allowed. Premium-rate services (ringtones, games) also at 5%.

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

### Test 1 -- Standard domestic sale at 5%
**Input:** Sale of manufactured goods, net MMK 10,000,000, CT MMK 500,000 (5%). CT registered client.
**Expected output:** Part B.1: Net MMK 10,000,000, Output CT MMK 500,000.

### Test 2 -- Local purchase with input CT credit
**Input:** Purchase of raw materials from CT-registered supplier, net MMK 5,000,000, CT MMK 250,000. Valid invoice held.
**Expected output:** Part E.1: Input CT MMK 250,000. Full credit allowed.

### Test 3 -- Import with customs CT
**Input:** Import of machinery, CIF MMK 20,000,000. Customs duty MMK 1,000,000. CT at 5% on MMK 21,000,000 = MMK 1,050,000.
**Expected output:** Part E.2: Input CT MMK 1,050,000. Credit allowed.

### Test 4 -- Export (exempt)
**Input:** Export of garments, FOB MMK 30,000,000. All documentation complete.
**Expected output:** Part D: MMK 30,000,000. No output CT. Input CT on related purchases fully recoverable.

### Test 5 -- Blocked input: director's personal vehicle
**Input:** Company purchases sedan for director, MMK 40,000,000, CT MMK 2,000,000.
**Expected output:** Input CT MMK 0 (BLOCKED -- personal use vehicle).

### Test 6 -- Special goods: alcohol sale
**Input:** Distillery sells locally produced spirits, net MMK 5,000,000. CT rate: 60%.
**Expected output:** Part B.2: Net MMK 5,000,000, CT MMK 3,000,000 at 60%.

### Test 7 -- Mixed supplies at different rates
**Input:** Supplier sells general goods (MMK 3,000,000, 5%) and cigarettes (MMK 2,000,000, 80%) on one invoice.
**Expected output:** Part B.1: MMK 3,000,000, CT MMK 150,000. Part B.2: MMK 2,000,000, CT MMK 1,600,000. Total output CT: MMK 1,750,000.

### Test 8 -- Import and re-export
**Input:** Import materials MMK 10,000,000 (CT paid MMK 500,000). Process and export finished goods MMK 15,000,000.
**Expected output:** Input CT credit: MMK 500,000. Output CT on export: MMK 0 (exempt). Net refund position: MMK 500,000.

---

## Step 14: Invoice and Documentation Requirements [T1]

**Legislation:** Commercial Tax Law; IRD instructions.

### Mandatory Contents of CT Invoice
1. Seller's name, address, and TIN
2. Buyer's name and TIN (if registered)
3. Date of issue
4. Invoice number
5. Description of goods/services
6. Quantity and unit price
7. Commercial Tax rate and amount
8. Total amount including CT

### Record Keeping (minimum 5 years)
1. All purchase and sales invoices
2. CT account ledger
3. Import/export documentation
4. Bank statements
5. Stock/inventory records
6. General ledger and journals
7. Customs payment receipts

---

## Step 15: Specific Sector Rules

### Manufacturing [T1]
- CT at 5% on manufactured goods (standard)
- Input CT credit on raw materials allowed
- Must maintain production records and input-output coefficients

### Hotel and Tourism [T1]
- Hotel services: CT at 5%
- Restaurant services: CT at 5%
- Input credit on supplies and equipment allowed
- Tourism license required from Ministry of Hotels and Tourism

### Real Estate and Construction [T2]
- Construction services: CT at 5% on contract value
- Sale of property: CT at 5% on selling price
- Input credit on construction materials allowed
- **Flag for reviewer: confirm contract classification and applicable rate**

### Telecommunications [T1]
- CT at 5% on all telecom services
- Input credit on network equipment allowed
- International call services: CT at 5%

---

## Step 16: Penalties Detailed Summary [T1]

| Offence | Penalty |
|---------|---------|
| Failure to register | Assessment + 10% surcharge |
| Late filing | 10% of tax due |
| Late payment | 10% of unpaid amount + interest |
| Non-issuance of invoice | Fine per IRD notification |
| Fraudulent under-declaration | Up to 100% of understated CT + criminal prosecution |
| Failure to maintain records | Fine per IRD notification |
| Tax evasion | Criminal prosecution, imprisonment, and fines |
| Obstruction of tax officer | Fine and possible imprisonment |

---

## Step 17: Audit and Assessment [T2]

### Audit Process
1. IRD may audit within **3 years** of filing
2. Extended to **6 years** for suspected fraud
3. Desk audits and field audits
4. Assessment issued post-audit

### Appeals
1. File objection with IRD within **30 days**
2. Appeal to Revenue Appellate Tribunal
3. Further appeal to High Court

**Escalate any audit situation to qualified practitioner immediately.**

---

## Step 18: Currency and Exchange Rate Rules [T1]

**Legislation:** Central Bank of Myanmar Regulations; Commercial Tax Law.

- All CT returns must be filed in Myanmar Kyat (MMK)
- Foreign currency transactions converted at Central Bank of Myanmar reference rate
- Rate applied on the date of supply (not date of payment)
- For imports, the customs exchange rate at date of declaration applies
- For exports, the exchange rate at date of export declaration applies
- Multi-currency accounts must be reconciled to MMK for each transaction

---

## Contribution Notes

This skill must be validated by a qualified Certified Public Accountant (CPA) practicing in Myanmar before use in production. All T1 rules must be verified against the latest Union Tax Law and IRD notifications.

**A skill may not be published without sign-off from a qualified practitioner in Myanmar.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
