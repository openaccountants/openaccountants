---
name: uganda-vat
description: Use this skill whenever asked to prepare, review, or create a Uganda VAT return for any client. Trigger on phrases like "prepare VAT return", "do the Uganda VAT", "URA return", "fill in VAT return", or any request involving Uganda VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Uganda VAT classification rules, return form mappings, deductibility rules, withholding VAT treatment, reverse charge, registration thresholds, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Uganda VAT-related work.
---

# Uganda VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Uganda (Republic of Uganda) |
| Jurisdiction Code | UG |
| Primary Legislation | Value Added Tax Act, Cap. 349, Laws of Uganda (as amended) |
| Supporting Legislation | VAT Regulations S.I. 340-1; Tax Procedures Code Act 2014; East African Community Customs Management Act 2004 |
| Tax Authority | Uganda Revenue Authority (URA) |
| Filing Portal | https://efiling.ura.go.ug (e-Filing portal) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by a licensed CPA (ICPAU member) in Uganda |
| Validation Date | Pending |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: rate application, return form mapping, registration threshold, deadlines, withholding VAT, blocked categories. Tier 2: partial exemption, mixed supplies, deemed supplies, rental income. Tier 3: petroleum sector, mining, special economic zones. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed accountant.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN** [T1] -- Uganda Taxpayer Identification Number
2. **VAT registration status** [T1] -- registered or unregistered
3. **VAT period** [T1] -- monthly filing
4. **Industry/sector** [T2] -- impacts classification (e.g., agriculture, construction, telecommunications)
5. **Does the business make exempt supplies?** [T2] -- if yes, input VAT apportionment required
6. **Is the business a designated withholding VAT agent?** [T1] -- URA designates certain entities
7. **Does the business import goods?** [T1] -- customs VAT collected at border
8. **Excess credit brought forward** [T1] -- from prior period

**If items 1-2 are unknown, STOP. Do not classify any transactions until registration status is confirmed.**

---

## Step 1: VAT Rate Structure [T1]

| Rate | Description | Legislation |
|------|-------------|-------------|
| 18% | Standard rate on all taxable supplies | VAT Act Cap. 349, s.4(1) |
| 0% | Zero rate (exports, specified supplies) | VAT Act Cap. 349, Second Schedule |
| Exempt | No VAT charged, no input recovery | VAT Act Cap. 349, Third Schedule |

### Zero-Rated Supplies [T1]
**Legislation:** VAT Act Cap. 349, Second Schedule.
- Export of goods (with proof of export)
- Export of services (consumed entirely outside Uganda)
- International transport of goods and passengers
- Supply of drugs and medicines (as specified by the Minister)
- Educational materials (as specified)
- Agricultural inputs (seeds, fertilizers, pesticides, hoes, and specified implements)
- Supply of leased aircraft and aircraft engines for international transport
- Supplies to diplomats (with URA approval)

### Exempt Supplies [T1]
**Legislation:** VAT Act Cap. 349, Third Schedule.
- Unprocessed foodstuffs (maize, millet, sorghum, wheat, rice, groundnuts, beans, cassava, potatoes, fruits, vegetables)
- Financial services (interest, premiums on life insurance, foreign exchange transactions)
- Medical, dental, and nursing services
- Educational services
- Residential rental (unfurnished)
- Social welfare services
- Burial and cremation services
- Postage stamps and postal services
- Insurance services (life insurance)
- Supply of water for domestic use by public utilities

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, PAYE, NSSF, dividends, loan repayments = OUT OF SCOPE
- **Legislation:** VAT Act Cap. 349, s.3 (definition of taxable supply)

### 2b. Determine Counterparty Location [T1]
- Domestic (Uganda): within Uganda
- EAC: Kenya, Tanzania, Rwanda, Burundi, South Sudan, DRC
- Rest of World: all other countries
- **Note:** EAC is a customs union but NOT a common VAT area. Each member charges own VAT on imports.

### 2c. Determine Supply Type [T1]
- Goods: tangible movable property
- Services: everything that is not goods
- Imports of goods: VAT collected at customs
- Imports of services: reverse charge applies
- **Legislation:** VAT Act Cap. 349, s.12 (place of supply of services)

### 2d. Determine Expense Category [T1]
- Capital goods: assets with useful life exceeding one year
- Overhead/services: operating expenses
- Resale goods: goods purchased for direct resale

---

## Step 3: VAT Return Form Structure [T1]

The Uganda VAT return is filed monthly via the URA e-Filing portal.

### Output Section

| Box | Description | Mapping |
|-----|-------------|---------|
| 1a | Standard-rated supplies (18%) | Net value of taxable sales |
| 1b | Zero-rated supplies | Net value of zero-rated sales |
| 1c | Exempt supplies | Net value of exempt sales |
| 1d | Total supplies | 1a + 1b + 1c |
| 2 | Output VAT (18% on 1a) | VAT on standard-rated supplies |
| 3 | Adjustments to output tax | Credit notes, bad debt, corrections |
| 4 | Total output tax | Box 2 + Box 3 |

### Input Section

| Box | Description | Mapping |
|-----|-------------|---------|
| 5a | Local taxable purchases | Net value of local purchases with VAT |
| 5b | Imports of goods | Net value from customs documentation |
| 5c | Imports of services (reverse charge) | Net value of services from non-residents |
| 6 | Input VAT on local purchases | VAT on 5a |
| 7 | Input VAT on imports of goods | VAT from customs (5b) |
| 8 | Input VAT on imported services | Self-assessed 18% on 5c |
| 9 | Total input VAT | Box 6 + Box 7 + Box 8 |
| 10 | Input VAT adjustments | Blocked items, apportionment |
| 11 | Allowable input VAT | Box 9 - Box 10 |

### Net Calculation

| Box | Description | Formula |
|-----|-------------|---------|
| 12 | Net VAT payable/(refundable) | Box 4 - Box 11 |
| 13 | Credit brought forward | From prior period |
| 14 | Withholding VAT credits | VAT withheld by designated agents |
| 15 | Net amount payable/(refundable) | Box 12 - Box 13 - Box 14 |

---

## Step 4: Withholding VAT [T1]

**Legislation:** VAT Act Cap. 349, s.23A (withholding tax agent).

### Mechanism
- URA designates certain entities as withholding VAT agents (government ministries, large companies, NGOs)
- Withholding agent deducts 6% of the taxable value (not 6% of the VAT amount) when paying VAT-registered suppliers
- The supplier receives a withholding VAT credit certificate
- The supplier claims credit against output VAT liability (Box 14)
- The agent remits the withheld amount to URA

### Example [T1]
Invoice: UGX 10,000,000 net + UGX 1,800,000 VAT (18%) = UGX 11,800,000 total.
Withholding: 6% of UGX 10,000,000 = UGX 600,000.
Supplier receives: UGX 11,800,000 - UGX 600,000 = UGX 11,200,000.
Supplier claims UGX 600,000 as withholding VAT credit (Box 14).

---

## Step 5: Reverse Charge on Imported Services [T1]

**Legislation:** VAT Act Cap. 349, s.14 (imported services).

When a Uganda VAT-registered person receives services from a non-resident supplier not registered in Uganda:

1. Self-assess output VAT at 18% on the value of services received
2. Include in output section
3. Claim input VAT at 18% if services relate to taxable supplies (Box 8)
4. Net effect: zero for fully taxable businesses

**Exceptions:**
- Out-of-scope payments: NEVER reverse charge
- Services consumed entirely outside Uganda: NOT subject to Uganda VAT

---

## Step 6: Deductibility Check

### Blocked Input Tax Categories [T1]
**Legislation:** VAT Act Cap. 349, s.21 (non-deductible input tax).

The following have ZERO VAT recovery:
- Entertainment expenses (s.21(1)(a))
- Motor vehicles for personal transport (< 10 seats), unless used for taxi, car hire, or driving instruction (s.21(1)(b))
- Club subscriptions of a recreational nature (s.21(1)(c))
- Goods and services for personal or non-business use (s.21(1)(d))
- Goods and services not used in making taxable supplies (s.21(1)(e))

### Registration-Based Recovery [T1]
- VAT-registered: input VAT recoverable subject to rules
- Unregistered: NO input VAT recovery

### Partial Exemption [T2]
**Legislation:** VAT Act Cap. 349, s.20(3) (apportionment).

If business makes both taxable and exempt supplies:
`Recovery % = (Taxable Supplies / Total Supplies) * 100`

**Flag for reviewer: URA may approve alternative methods. Annual adjustment may be required.**

---

## Step 7: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory VAT registration | UGX 150,000,000 quarterly turnover (UGX 50M/month). Note: a proposal to raise this to UGX 250,000,000 is under consideration for FY 2026/27 but not yet enacted. | VAT Act Cap. 349, s.7(1) |
| Voluntary VAT registration | Below threshold (with URA approval) | VAT Act Cap. 349, s.7(2) |
| Withholding VAT rate | 6% of taxable value | VAT Act Cap. 349, s.23A |
| VAT refund processing | Within 2 months of claim | Tax Procedures Code Act, s.41 |

---

## Step 8: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|-----------|--------|----------|-------------|
| VAT return filing | Monthly | 15th of following month | VAT Act Cap. 349, s.22 |
| VAT payment | Monthly | 15th of following month | VAT Act Cap. 349, s.22 |
| Withholding VAT remittance | Monthly | 15th of following month | VAT Act Cap. 349, s.23A |

### Late Filing Penalties [T1]
**Legislation:** Tax Procedures Code Act 2014, s.52-53.
- Late filing: UGX 200,000 per month or 2% of tax due per month, whichever is greater
- Interest on late payment: 2% per month or part thereof, compounding monthly
- Failure to register: 100% of tax that should have been collected

---

## Step 9: Deemed Supplies [T1]

**Legislation:** VAT Act Cap. 349, s.5 (deemed supplies).

A deemed supply arises when:
- Goods applied for non-business purposes
- Business gifts exceeding UGX 100,000 per recipient per year
- Business assets used for private purposes
- Cessation of registration while holding stock/assets

Output VAT at 18% on market value of deemed supply.

---

## PROHIBITIONS [T1]

- NEVER let AI guess return box assignment -- it is deterministic from facts
- NEVER allow input VAT recovery on blocked categories
- NEVER confuse zero-rated with exempt
- NEVER apply reverse charge to out-of-scope categories
- NEVER allow unregistered persons to claim input VAT
- NEVER treat EAC transactions as intra-community supplies
- NEVER ignore withholding VAT credits when computing net liability
- NEVER compute any number -- engine handles arithmetic
- NEVER file without checking credit brought forward
- NEVER confuse withholding VAT (6% of taxable value) with withholding income tax

---

## Step 10: Edge Case Registry

### EC1 -- Import of services from non-resident (SaaS) [T1]
**Situation:** Uganda company subscribes to Zoom. Monthly fee USD 20. No VAT.
**Resolution:** Reverse charge. Self-assess output and input VAT at 18% on UGX equivalent. Net effect zero if fully taxable.
**Legislation:** VAT Act Cap. 349, s.14.

### EC2 -- Withholding VAT by government ministry [T1]
**Situation:** Government ministry pays VAT-registered supplier. Invoice: UGX 50,000,000 + UGX 9,000,000 VAT = UGX 59,000,000.
**Resolution:** Ministry withholds 6% of UGX 50,000,000 = UGX 3,000,000. Supplier receives UGX 56,000,000. Supplier claims UGX 3,000,000 in Box 14.
**Legislation:** VAT Act Cap. 349, s.23A.

### EC3 -- Export of goods (zero-rated) [T1]
**Situation:** Uganda exporter ships processed coffee to buyer in UK.
**Resolution:** Zero-rated. Box 1b. No output VAT. Input VAT on related costs fully recoverable. Must have export documentation (customs export entry, bill of lading).
**Legislation:** VAT Act Cap. 349, Second Schedule.

### EC4 -- Furnished residential rental [T2]
**Situation:** Company rents a furnished apartment for expatriate employee.
**Resolution:** Unfurnished residential rental is exempt. Furnished rental may be standard-rated (18%). Flag for reviewer: determination depends on whether furniture is a separate supply or part of the rental. URA practice note may apply.
**Legislation:** VAT Act Cap. 349, Third Schedule; s.9 (mixed/composite supply).

### EC5 -- Import from EAC (Kenya) [T1]
**Situation:** Uganda retailer imports goods from Kenyan supplier. Customs clears at Malaba border.
**Resolution:** VAT at 18% charged at customs. No intra-community mechanism. Customs VAT recoverable as input VAT (Box 7) if for taxable supplies. EAC Rules of Origin may reduce customs duty but NOT VAT.
**Legislation:** VAT Act Cap. 349, s.15; EAC CMA 2004.

### EC6 -- Motor vehicle purchase (blocked) [T1]
**Situation:** Company purchases Toyota Corolla sedan for director.
**Resolution:** Input VAT BLOCKED -- passenger vehicle < 10 seats not used for hire. Total cost includes irrecoverable VAT.
**Legislation:** VAT Act Cap. 349, s.21(1)(b).

### EC7 -- Agricultural inputs (zero-rated) [T1]
**Situation:** Farm purchases fertilizer and seeds from local supplier.
**Resolution:** Agricultural inputs (seeds, fertilizers, pesticides, and specified implements) are zero-rated. Supplier should charge 0%. If supplier incorrectly charges 18%, buyer should request a corrected invoice.
**Legislation:** VAT Act Cap. 349, Second Schedule.

### EC8 -- Bad debt relief [T2]
**Situation:** Supplier has issued VAT invoice and accounted for output VAT. Customer has not paid for 6+ months.
**Resolution:** Bad debt relief available if: (a) debt outstanding for at least 3 years; (b) written off in accounts; (c) reasonable steps taken to recover. Flag for reviewer: the 3-year period is long; confirm with current URA practice.
**Legislation:** VAT Act Cap. 349, s.22A.

---

## Step 11: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list possible treatments]
Recommended: [which treatment and why]
Action Required: Licensed accountant (ICPAU member) must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed accountant. Document gap.
```

---

## Step 12: Test Suite

### Test 1 -- Standard local sale [T1]
**Input:** Uganda company sells goods for UGX 20,000,000 net. Standard-rated.
**Expected output:** Box 1a = UGX 20,000,000. Box 2 = UGX 3,600,000 (18%).

### Test 2 -- Local purchase, input VAT recovery [T1]
**Input:** VAT-registered company buys office equipment. Invoice: UGX 5,000,000 + UGX 900,000 VAT = UGX 5,900,000.
**Expected output:** Box 5a = UGX 5,000,000. Box 6 = UGX 900,000. Recoverable.

### Test 3 -- Reverse charge on imported services [T1]
**Input:** Company receives legal services from South African firm. Invoice UGX 10,000,000. No VAT.
**Expected output:** Output VAT = UGX 1,800,000. Input VAT = UGX 1,800,000. Net = zero.

### Test 4 -- Export (zero-rated) [T1]
**Input:** Exporter ships fish worth UGX 100,000,000 to DRC.
**Expected output:** Box 1b = UGX 100,000,000. Output VAT = UGX 0. Input VAT fully recoverable.

### Test 5 -- Withholding VAT [T1]
**Input:** Government ministry pays supplier. Invoice: UGX 30,000,000 + UGX 5,400,000 VAT = UGX 35,400,000.
**Expected output:** Withholding = 6% of UGX 30,000,000 = UGX 1,800,000. Supplier claims UGX 1,800,000 (Box 14).

### Test 6 -- Blocked input (entertainment) [T1]
**Input:** Company hosts client dinner. Invoice: UGX 3,000,000 + UGX 540,000 VAT = UGX 3,540,000.
**Expected output:** Input VAT = UGX 0 (BLOCKED). Cost = UGX 3,540,000.

### Test 7 -- Exempt supply (financial services) [T1]
**Input:** Bank earns interest income of UGX 500,000,000.
**Expected output:** Box 1c = UGX 500,000,000 (exempt). No output VAT. Related input VAT NOT recoverable.

### Test 8 -- Deemed supply (gift) [T1]
**Input:** Company gives client gifts worth UGX 500,000 (market value).
**Expected output:** Deemed supply. Output VAT = UGX 90,000 (18%). Exceeds UGX 100,000 threshold.

---

## Step 13: Out of Scope -- Direct Tax (Reference Only) [T3]

- **Corporate Income Tax:** 30% standard. Small business: concessional rates.
- **PAYE:** Progressive rates 0% to 40%. Employer obligation.
- **NSSF:** 5% employer + 5% employee. Separate from VAT.
- **Local Service Tax (LST):** Employment-based levy. Separate from VAT.

---

## Contribution Notes

This skill was adapted from the Malta VAT Return Preparation Skill template. Uganda-specific elements include withholding VAT (6% of taxable value), EAC customs union treatment, agricultural zero-rating, and deemed supply rules.

**A skill may not be published without sign-off from a licensed practitioner (ICPAU member) in Uganda.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
