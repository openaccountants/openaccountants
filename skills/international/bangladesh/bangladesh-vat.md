---
name: bangladesh-vat
description: Use this skill whenever asked to prepare, review, or create a Bangladesh VAT return (Mushak-9.1 form) or any VAT filing for a Bangladeshi business. Trigger on phrases like "prepare VAT return", "Bangladesh VAT", "fill in Mushak", "BIN registration", "NBR filing", or any request involving Bangladesh VAT. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Bangladesh VAT classification rules, Mushak form mappings, input tax credit rules, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Bangladesh VAT-related work.
---

# Bangladesh VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Bangladesh |
| Jurisdiction Code | BD |
| Primary Legislation | Value Added Tax and Supplementary Duty Act 2012 (VAT & SD Act 2012) |
| Supporting Legislation | VAT & SD Rules 2016; SROs (Statutory Regulatory Orders) issued by NBR |
| Tax Authority | National Board of Revenue (NBR) |
| Filing Portal | https://vat.gov.bd (Mushak Online Portal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending local practitioner validation |
| Validation Date | Pending |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: standard rate classification, input-output mapping, return form fields. Tier 2: turnover tax vs VAT election, sector-specific exemptions. Tier 3: complex multi-establishment structures, bond/export processing zones. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A qualified accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to qualified accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and BIN (Business Identification Number)** [T1] -- 13-digit BIN issued by NBR
2. **Registration type** [T1] -- VAT registered (standard), Turnover Tax (below BDT 3 crore annual turnover), or Exempt
3. **VAT period** [T1] -- monthly (standard for VAT registered entities)
4. **Industry/sector** [T2] -- impacts exemptions and reduced rates (e.g., agriculture, pharmaceuticals)
5. **Does the business make exempt supplies?** [T2] -- If yes, input tax credit apportionment required
6. **Does the business import goods?** [T1] -- impacts customs-stage VAT treatment
7. **Does the business export goods/services?** [T1] -- impacts zero-rating treatment
8. **Excess credit brought forward** [T1] -- from prior period
9. **Is the entity in an Export Processing Zone (EPZ)?** [T2] -- special rules apply
10. **Number of business establishments** [T1] -- each unit may need separate BIN and filing

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration type and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, loan repayments, dividends, bank interest = OUT OF SCOPE (never on VAT return)
- **Legislation:** VAT & SD Act 2012, Section 2 (definitions of supply)

### 1b. Determine Supply Location [T1]
- Domestic (within Bangladesh)
- Import (goods/services from outside Bangladesh)
- Export (goods/services to outside Bangladesh)
- **Legislation:** VAT & SD Act 2012, Section 18 (place of supply)

### 1c. Determine VAT Rate [T1]
- **Standard rate:** 15%
- **Turnover tax rate:** 4% (for businesses with annual turnover BDT 50 lakh to BDT 3 crore, not VAT registered). Businesses with turnover BDT 30 lakh to BDT 50 lakh pay 3% turnover tax.
- **Reduced rates (via SRO):** 5%, 7.5%, 10% on specified goods/services
- **Zero-rated:** Exports, supplies to diplomats, certain deemed exports
- **Exempt:** Listed in First Schedule of VAT & SD Act 2012 (agricultural products, certain food items, education, health services, land transport, etc.)
- **Legislation:** VAT & SD Act 2012, Section 15 (standard rate); Third Schedule (reduced rates)

### 1d. Determine Expense Category [T1]
- Capital goods: machinery, equipment, furniture with useful life > 1 year
- Raw materials: inputs consumed in production
- Services: overhead, professional fees, utilities
- **Legislation:** VAT & SD Act 2012, Section 2(56) (input tax definition)

---

## Step 2: Mushak Form Assignments [T1]

**Legislation:** VAT & SD Rules 2016, Rule 40-47; Mushak form series.

### Key Mushak Forms

| Form | Purpose |
|------|---------|
| Mushak-9.1 | Monthly VAT Return |
| Mushak-6.1 | Purchase Register (local purchases) |
| Mushak-6.2 | Sales Register (local sales) |
| Mushak-6.2.1 | Credit Note Register |
| Mushak-6.3 | Input-Output Coefficient Register |
| Mushak-6.4 | Transfer of Finished Goods |
| Mushak-6.5 | Purchase Register (imports) |
| Mushak-6.6 | Summary Purchase-Sales Statement |
| Mushak-6.10 | Withholding VAT Certificate |
| Mushak-11 | Tax Invoice |
| Mushak-11Ka | Invoice for goods subject to SD |

### Mushak-9.1 Return Structure

| Section | Description | Source |
|---------|-------------|--------|
| Part 1 | Entity information (BIN, name, period) | Onboarding data |
| Part 2 | Output tax on local sales | Mushak-6.2 |
| Part 3 | Output tax on exports (zero-rated) | Export documentation |
| Part 4 | Exempt supplies | Mushak-6.2 |
| Part 5 | Total output tax | Calculated |
| Part 6 | Input tax on local purchases | Mushak-6.1 |
| Part 7 | Input tax on imports | Mushak-6.5 / Bill of Entry |
| Part 8 | Total input tax credit | Calculated |
| Part 9 | Net tax payable or credit carried forward | Part 5 minus Part 8 |
| Part 10 | Supplementary Duty (if applicable) | SD calculation |
| Part 11 | Interest / penalty (if late) | Calculated |
| Part 12 | Total payable | Sum of Parts 9-11 |

### Output Tax Classification

| Supply Type | Rate | Return Section |
|-------------|------|----------------|
| Standard domestic supply | 15% | Part 2 |
| Reduced-rate domestic supply | 5% / 7.5% / 10% | Part 2 (separate line) |
| Export (zero-rated) | 0% | Part 3 |
| Exempt supply | N/A | Part 4 |

### Input Tax Classification

| Purchase Type | Source | Return Section |
|---------------|--------|----------------|
| Local purchases (VAT paid) | Mushak-6.1 | Part 6 |
| Imports (VAT paid at customs) | Bill of Entry | Part 7 |
| Capital goods | Mushak-6.1 | Part 6 (included) |

---

## Step 3: Input Tax Credit Mechanism [T1]

**Legislation:** VAT & SD Act 2012, Section 45-52.

### Eligibility for Input Tax Credit

1. The purchase must be used for making taxable supplies [T1]
2. A valid tax invoice (Mushak-11) must be held [T1]
3. The invoice must contain the supplier's BIN [T1]
4. The input tax must have been paid by the supplier to the government [T2]
5. The claim must be made within the return period or within the next 3 (three) return periods [T1]

### Input Tax Credit Apportionment [T2]

If the business makes both taxable and exempt supplies:
```
Creditable Input Tax = Total Input Tax x (Taxable Supplies / Total Supplies)
```
**Flag for reviewer: apportionment calculation must be confirmed by qualified accountant before filing. Annual adjustment required.**

### Input Tax Credit on Capital Goods [T1]

- Full credit in the period of acquisition if used entirely for taxable supplies
- If used for mixed purposes (taxable and exempt), apportionment applies [T2]
- **Legislation:** VAT & SD Act 2012, Section 46

---

## Step 4: Deductibility Check

### Blocked Input Tax Credit [T1]

**Legislation:** VAT & SD Act 2012, Section 49.

These have ZERO input tax credit regardless of anything else:

- Goods or services used for personal consumption
- Passenger vehicles (unless used in transport business)
- Entertainment expenses (unless directly related to business promotion with documentation)
- Goods or services used for making exempt supplies (fully blocked)
- Purchases without valid Mushak-11 tax invoice
- Purchases from unregistered suppliers (no BIN)
- Goods lost, stolen, or destroyed (unless covered by insurance claim)
- Free samples (unless documented as promotional)

Blocked categories OVERRIDE any other credit rule. Check blocked FIRST.

### Registration-Based Recovery [T1]
- VAT registered (standard): full input tax credit (subject to category rules)
- Turnover Tax payer: NO input tax credit (flat 4% on turnover, no deductions)
- Exempt entity: NO input tax credit

---

## Step 5: Withholding VAT (VDS) [T1]

**Legislation:** VAT & SD Act 2012, Section 50; SRO on VDS rates.

Certain entities (government, banks, NGOs, listed companies) must withhold VAT at source (VAT Deducted at Source -- VDS) when making purchases of specified services.

| Service Category | VDS Rate |
|-----------------|----------|
| Audit and accounting | Full VAT (15%) or applicable rate |
| Legal services | Full VAT (15%) or applicable rate |
| Security services | Full VAT (15%) or applicable rate |
| Cleaning services | Full VAT (15%) or applicable rate |
| Engineering/architectural | Full VAT (15%) or applicable rate |
| Other specified services | As per SRO |

**VDS treatment on the return:**
- Withholder: Reports VDS withheld in Mushak-9.1, deposits via Mushak-6.6
- Supplier: Claims VDS deducted as input tax credit (reduces net payable)
- Certificate: Mushak-6.10 must be issued to supplier

---

## Step 6: Supplementary Duty (SD) [T1]

**Legislation:** VAT & SD Act 2012, Part 5; Second Schedule.

Supplementary Duty applies to specified luxury/sin goods and services at varying rates:

| Category | Typical SD Rate |
|----------|----------------|
| Cigarettes/tobacco | 65% - 150% |
| Alcohol/beer | 250% - 350% |
| Carbonated beverages | 25% |
| SIM cards | 15% |
| Mobile phone services | 15% |
| Motor vehicles (imported) | 20% - 500% |
| Air-conditioned hotels/restaurants | 7.5% |
| Club/casino services | 35% |

SD is calculated BEFORE VAT. VAT is applied on (value + SD).

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| VAT registration mandatory | Annual turnover > BDT 3 crore (BDT 30 million) |
| Turnover Tax band (4%) | Annual turnover BDT 50 lakh to BDT 3 crore |
| Turnover Tax band (3%) | Annual turnover BDT 30 lakh to BDT 50 lakh |
| Cottage industry exemption | Annual turnover < BDT 30 lakh (no VAT/TT obligation) |
| Input tax credit time limit | Within 3 return periods from invoice date |
| Withholding VAT applicability | Specified withholding agents per SRO |

---

## Step 8: Filing Deadlines [T1]

| Registration Type | Period | Deadline |
|-------------------|--------|----------|
| VAT registered | Monthly | Within 15 days after end of month |
| Turnover Tax | Quarterly | Within 15 days after end of quarter |
| Supplementary Duty | Monthly | Within 15 days after end of month |
| Amended return | -- | Within 3 months of original due date (with interest) |

### Late Filing Penalties [T1]

| Default | Penalty |
|---------|---------|
| Late filing | BDT 10,000 per month of delay |
| Late payment | 2% per month simple interest on unpaid amount |
| Non-filing | BDT 10,000 + interest on assessed liability |
| Failure to issue Mushak-11 | BDT 10,000 per instance |
| Incorrect return | 100% of evaded tax + BDT 10,000 |

---

## Step 9: Mushak-9.1 Derived Calculations [T1]

```
Total Output Tax     = Sum of VAT on all taxable supplies (standard + reduced rates)
Total Input Tax      = Sum of VAT on local purchases + VAT on imports
Net Tax Payable      = Total Output Tax - Total Input Tax - Credit B/F
If Net < 0           = Credit carried forward to next period
SD Payable           = Sum of SD on all dutiable supplies
Total Payable        = Net VAT Payable + SD Payable + Interest (if any)
```

---

## Step 10: Zero-Rating and Export Rules [T1]

**Legislation:** VAT & SD Act 2012, Section 24-25.

### Zero-Rated Supplies
- Direct exports of goods (with customs documentation)
- Deemed exports (supplies to export processing zones)
- Supplies to diplomats/diplomatic missions
- International transport services

### Export Documentation Required
1. Export LC or contract
2. Bill of Lading / Airway Bill
3. Customs export declaration (Bill of Export)
4. Bank realization certificate (within 6 months)

**If documentation is incomplete, zero-rating may be denied and standard 15% applies retroactively. [T2]**

---

## PROHIBITIONS [T1]

- NEVER allow turnover tax payers to claim input tax credit
- NEVER classify exempt supplies as zero-rated (zero-rated allows credit; exempt does not)
- NEVER accept input tax credit without valid Mushak-11 invoice bearing supplier BIN
- NEVER apply input tax credit on personal consumption or blocked categories
- NEVER file a return without reconciling Mushak-6.1 and Mushak-6.2 to Mushak-9.1
- NEVER compute SD after VAT -- SD is always computed first, then VAT on (value + SD)
- NEVER allow input tax credit older than 3 return periods
- NEVER ignore VDS obligations when client is a designated withholding agent
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 11: Edge Case Registry

### EC1 -- Withholding VAT (VDS) on imported services [T2]
**Situation:** Client receives consulting services from a foreign firm, no local BIN.
**Resolution:** Reverse charge mechanism applies under Section 18. Client must self-assess VAT at 15% and deposit via Mushak-9.1. No input tax credit for the foreign firm. Client may claim input credit if used for taxable supplies.
**Legislation:** VAT & SD Act 2012, Section 18(3).

### EC2 -- Mixed supply: taxable and exempt components [T2]
**Situation:** A single invoice contains both taxable goods and exempt services.
**Resolution:** Split by line item. Taxable portion attracts VAT at applicable rate. Exempt portion excluded from output tax. Input tax credit only allowed for the taxable portion. If line items not separable, flag for reviewer.

### EC3 -- Capital goods purchased for mixed use [T2]
**Situation:** Client purchases machinery used partly for taxable and partly for exempt production.
**Resolution:** Input tax credit must be apportioned based on ratio of taxable to total supplies. Annual adjustment required. Flag for reviewer: confirm the apportionment ratio.
**Legislation:** VAT & SD Act 2012, Section 46.

### EC4 -- Goods destroyed in natural disaster [T1]
**Situation:** Inventory destroyed by flood; input tax credit already claimed.
**Resolution:** If goods were insured, no reversal required (insurance proceeds subject to VAT if paid for supply). If uninsured, input tax credit must be reversed in the period of loss. Report reversal in Mushak-9.1 as reduction of input tax.
**Legislation:** VAT & SD Act 2012, Section 49(1)(g).

### EC5 -- Transfer of goods between own establishments [T1]
**Situation:** Client transfers finished goods from factory (one BIN) to retail shop (different BIN).
**Resolution:** Inter-establishment transfer is a deemed supply. Issue Mushak-6.4 (transfer challan). Output VAT applies at factory. Input credit at receiving unit. Each BIN files separate Mushak-9.1.
**Legislation:** VAT & SD Act 2012, Section 5(3).

### EC6 -- Free samples distributed for promotion [T2]
**Situation:** Client distributes samples to potential customers without charge.
**Resolution:** Free samples treated as supply; output VAT due on fair market value. Input tax credit on raw materials used for samples is allowed if properly documented. If quantity is excessive relative to business size, flag for reviewer -- NBR may disallow.
**Legislation:** VAT & SD Act 2012, Section 5(4).

### EC7 -- Advance payments received before supply [T1]
**Situation:** Client receives advance payment for future delivery of goods.
**Resolution:** VAT becomes chargeable at the time of receiving advance payment, not at the time of supply. Issue Mushak-11 at the time of advance receipt. Include in output tax for the period.
**Legislation:** VAT & SD Act 2012, Section 14 (time of supply).

### EC8 -- Credit notes for returned goods [T1]
**Situation:** Customer returns goods and a credit note is issued.
**Resolution:** Supplier reduces output tax in the period of credit note issuance. Buyer must reverse input tax credit previously claimed. Both must update Mushak-6.1/6.2. Credit note registered in Mushak-6.2.1.
**Legislation:** VAT & SD Act 2012, Section 57.

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

### Test 1 -- Standard local sale at 15%
**Input:** Domestic sale of office furniture, net BDT 100,000, VAT BDT 15,000. VAT registered client.
**Expected output:** Mushak-9.1 Part 2: Net BDT 100,000, Output VAT BDT 15,000.

### Test 2 -- Local purchase with input tax credit
**Input:** Purchase of raw materials from local VAT-registered supplier, net BDT 50,000, VAT BDT 7,500 (15%). Valid Mushak-11 held.
**Expected output:** Mushak-9.1 Part 6: Input VAT BDT 7,500. Full credit allowed.

### Test 3 -- Import with customs VAT
**Input:** Import of machinery, assessable value BDT 500,000. Customs duty BDT 25,000. VAT at 15% on (BDT 500,000 + BDT 25,000) = BDT 78,750.
**Expected output:** Mushak-9.1 Part 7: Input VAT BDT 78,750. Credit allowed if used for taxable supplies.

### Test 4 -- Export (zero-rated)
**Input:** Export of garments, FOB value BDT 1,000,000. All export documentation complete.
**Expected output:** Mushak-9.1 Part 3: BDT 1,000,000 at 0%. No output VAT. Input tax credit on related purchases fully recoverable.

### Test 5 -- Turnover tax payer, no input credit
**Input:** Small trader, annual turnover BDT 1.5 crore, registered for turnover tax. Quarterly sales BDT 40 lakh.
**Expected output:** Turnover Tax = 4% x BDT 40,00,000 = BDT 1,60,000. No input tax credit allowed.

### Test 6 -- Blocked input: passenger vehicle
**Input:** VAT registered company purchases a sedan for director, BDT 3,000,000, VAT BDT 450,000.
**Expected output:** Input VAT BDT 0 (BLOCKED -- passenger vehicle). Full cost capitalized without VAT recovery.

### Test 7 -- VDS withholding on audit services
**Input:** Listed company pays audit fee BDT 200,000 to VAT-registered CA firm. VDS at 15%.
**Expected output:** Withholder deducts BDT 30,000 VDS, issues Mushak-6.10. Pays BDT 170,000 to CA firm. Deposits BDT 30,000 to treasury. CA firm claims BDT 30,000 as credit in Mushak-9.1.

### Test 8 -- Inter-establishment transfer
**Input:** Factory (BIN-A) transfers goods worth BDT 80,000 to retail unit (BIN-B).
**Expected output:** Factory issues Mushak-6.4. Factory Mushak-9.1: output VAT BDT 12,000 (15%). Retail unit Mushak-9.1: input VAT BDT 12,000.

---

## Step 14: Invoice Requirements [T1]

**Legislation:** VAT & SD Act 2012, Section 53; VAT & SD Rules 2016, Rule 40.

### Mandatory Contents of Mushak-11 Tax Invoice

1. Supplier's name, address, and BIN
2. Buyer's name and BIN (if registered)
3. Date of issue
4. Sequential invoice number
5. Description of goods/services with HS Code or service code
6. Quantity and unit price
7. Total value before VAT
8. VAT rate and VAT amount
9. Supplementary Duty amount (if applicable)
10. Total amount including VAT and SD
11. Signature of authorized person

### Invoice Types
- **Mushak-11:** Standard tax invoice for VAT-registered buyers
- **Mushak-11Ka:** Invoice for goods subject to Supplementary Duty
- **Mushak-11Kha:** Invoice for goods at reduced rates (per SRO)
- **Simplified invoice:** For retail sales below BDT 500 (less detail)

### Invoice Issuance Deadlines [T1]
- Must be issued at the time of supply or within the same day
- For continuous supplies (rent, utilities), at the time of each payment or billing
- For advance payments, at the time of receiving the advance

---

## Step 15: Record Keeping Requirements [T1]

**Legislation:** VAT & SD Act 2012, Section 107.

### Mandatory Records
All VAT-registered entities must maintain the following records for a minimum of **6 years**:

1. **Mushak-6.1** -- Purchase register (local purchases with VAT details)
2. **Mushak-6.2** -- Sales register (local sales with VAT details)
3. **Mushak-6.2.1** -- Credit note register
4. **Mushak-6.3** -- Input-output coefficient register (for manufacturers)
5. **Mushak-6.4** -- Transfer of finished goods register
6. **Mushak-6.5** -- Import purchase register
7. **Mushak-6.6** -- Summary purchase-sales statement
8. **Mushak-6.10** -- Withholding VAT (VDS) certificates
9. All original invoices (purchase and sales)
10. Bank statements and payment records
11. Import documents (Bills of Entry, LCs, Bills of Lading)
12. Export documents (Bills of Export, realization certificates)

### Electronic Record Keeping
- NBR encourages electronic maintenance of all registers
- The Mushak Online Portal allows digital submission
- Physical records must also be maintained as backup
- Records must be available for inspection by NBR officers

---

## Step 16: Audit and Assessment [T2]

**Legislation:** VAT & SD Act 2012, Sections 82-95.

### Types of Audit
1. **Desk Audit:** Review of return and records at NBR office
2. **Field Audit:** On-site inspection at taxpayer's premises
3. **Special Audit:** Triggered by discrepancies, intelligence, or random selection

### Audit Triggers
- Consistent refund claims
- Significant variance between declared and expected turnover
- Mismatch between purchase and sales registers
- Complaints from other taxpayers
- Random selection by NBR risk management system

### Assessment Powers
- NBR may issue assessment within **4 years** from the end of the tax period
- Extended to **6 years** in cases of suspected fraud or wilful default
- Taxpayer has **30 days** to file an objection against assessment
- Appeal to VAT Appellate Tribunal within **60 days** of objection decision

**Flag for reviewer: any audit or assessment situation requires immediate escalation to qualified practitioner.**

---

## Step 17: Penalties and Offences Summary [T1]

**Legislation:** VAT & SD Act 2012, Sections 109-130.

| Offence | Penalty |
|---------|---------|
| Failure to register | BDT 10,000 + retrospective registration |
| Late filing of return | BDT 10,000 per month |
| Late payment of VAT | 2% per month simple interest |
| Non-issuance of Mushak-11 | BDT 10,000 per instance |
| Issuance of fake invoice | 200% of VAT shown + criminal prosecution |
| Failure to maintain records | BDT 10,000 per offence |
| Obstruction of audit | BDT 25,000 |
| Tax evasion | 150% of evaded amount + criminal prosecution |
| Failure to deduct VDS | Amount of VDS + 2% per month interest |
| Under-declaration of output | 100% of underdeclared amount + interest |

---

## Contribution Notes

This skill must be validated by a qualified chartered accountant or cost and management accountant practicing in Bangladesh before use in production. All T1 rules must be verified against the latest SROs issued by NBR, as rates and thresholds are updated frequently via SRO.

**A skill may not be published without sign-off from a qualified practitioner in Bangladesh.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
