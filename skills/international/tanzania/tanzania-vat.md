---
name: tanzania-vat
description: Use this skill whenever asked to prepare, review, or create a Tanzania VAT return for any client. Trigger on phrases like "prepare VAT return", "do the Tanzania VAT", "TRA return", "fill in VAT return", or any request involving Tanzania VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Tanzania VAT classification rules, return form mappings, deductibility rules, reverse charge treatment, registration thresholds, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Tanzania VAT-related work.
---

# Tanzania VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Tanzania (United Republic of Tanzania) |
| Jurisdiction Code | TZ |
| Primary Legislation | Value Added Tax Act, 2014 (Act No. 5 of 2014) |
| Supporting Legislation | VAT (General) Regulations 2015; Tax Administration Act 2015 (TAA); East African Community Customs Management Act 2004 |
| Tax Authority | Tanzania Revenue Authority (TRA) |
| Filing Portal | https://ots.tra.go.tz (Online Tax System) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by a licensed CPA (NBAA registered) in Tanzania |
| Validation Date | Pending |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: rate application, return box assignment, registration threshold, deadlines, EAC treatment. Tier 2: partial exemption, mixed supplies, deemed supplies. Tier 3: complex group structures, mining sector, special economic zones. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN** [T1] -- Tanzania Taxpayer Identification Number
2. **VAT registration number (VRN)** [T1] -- assigned upon registration
3. **VAT period** [T1] -- monthly filing
4. **Industry/sector** [T2] -- impacts classification (e.g., mining, agriculture, tourism have special provisions)
5. **Does the business make exempt supplies?** [T2] -- if yes, input VAT apportionment required
6. **Does the business import goods?** [T1] -- customs VAT collected at border by TRA Customs
7. **Excess credit brought forward** [T1] -- from prior period
8. **Is the business located in a Special Economic Zone (SEZ)?** [T2] -- different rules may apply

**If items 1-3 are unknown, STOP. Do not classify any transactions until registration status is confirmed.**

---

## Step 1: VAT Rate Structure [T1]

### Standard Rate

| Rate | Description | Legislation |
|------|-------------|-------------|
| 18% | Standard rate on all taxable supplies | VAT Act 2014, s.7(1) |
| 16% | Reduced standard rate (effective 1 Sep 2025): applies when a standard-rated supply is made to a non-VAT-registered person on mainland Tanzania and payment is via bank or approved electronic payment system | Finance Act 2025 |
| 0% | Zero rate (exports, specified supplies) | VAT Act 2014, First Schedule |
| Exempt | No VAT charged, no input recovery | VAT Act 2014, Second Schedule |

### Zero-Rated Supplies [T1]
**Legislation:** VAT Act 2014, First Schedule.
- Exports of goods
- Exports of services (consumed entirely outside Tanzania)
- International transport services
- Supplies to diplomats (with approved exemption certificate)
- Supplies to SEZ operators (with valid certificate)
- Agricultural inputs (seeds, fertilizers, pesticides as specified)

### Exempt Supplies [T1]
**Legislation:** VAT Act 2014, Second Schedule.
- Unprocessed foodstuffs (rice, maize, wheat, cassava, potatoes, vegetables, fruits, meat, fish, milk, eggs)
- Financial services (excluding fee-based advisory services)
- Medical and healthcare services
- Educational services
- Residential rental
- Life insurance premiums
- Public transportation services
- Agricultural equipment and implements (as specified)
- Water supplied by public utilities
- Petroleum products (subject to separate fuel levy)

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, PAYE, NSSF contributions, SDL, dividends, loan repayments = OUT OF SCOPE
- **Legislation:** VAT Act 2014, s.5 (definition of supply)

### 2b. Determine Counterparty Location [T1]
- Domestic (Tanzania mainland + Zanzibar): within Tanzania
- EAC (East African Community): Kenya, Uganda, Rwanda, Burundi, South Sudan, DRC
- Rest of World: all other countries
- **Note:** Tanzania and Zanzibar have a unified VAT system under the 2014 Act. EAC is a customs union but NOT a common VAT area.

### 2c. Determine Supply Type [T1]
- Goods: tangible movable property
- Services: everything that is not goods
- Imports of goods: VAT collected at customs entry point
- Imports of services: reverse charge applies
- **Legislation:** VAT Act 2014, s.11 (place of supply)

### 2d. Determine Category [T1]
- Capital goods: assets with useful life exceeding one year and value exceeding TZS 1,000,000
- Overhead/services: operating expenses
- Resale goods: goods purchased for direct resale
- **Legislation:** VAT Act 2014, s.2 (definitions)

---

## Step 3: VAT Return Form Structure [T1]

The Tanzania VAT return is filed monthly via the TRA Online Tax System. The return form (ITX222.01.E) captures output and input tax.

### Output Section

| Box | Description | Mapping |
|-----|-------------|---------|
| A1 | Standard-rated supplies (18%) | Net value of taxable sales at 18% |
| A2 | Zero-rated supplies | Net value of zero-rated sales |
| A3 | Exempt supplies | Net value of exempt sales |
| A4 | Total supplies | A1 + A2 + A3 |
| A5 | Output VAT on standard-rated supplies | 18% of A1 |
| A6 | Adjustments to output tax | Credit notes, corrections |
| A7 | Total output tax | A5 + A6 |

### Input Section

| Box | Description | Mapping |
|-----|-------------|---------|
| B1 | Local taxable purchases | Net value of local purchases with VAT |
| B2 | Imports (customs entries) | Net value from customs documentation |
| B3 | Input VAT on local purchases | VAT on B1 |
| B4 | Input VAT on imports | VAT on B2 (from customs docs) |
| B5 | Total input VAT claimed | B3 + B4 |
| B6 | Input VAT adjustments | Blocked items, apportionment adjustments |
| B7 | Net input VAT | B5 - B6 |

### Net Calculation

| Box | Description | Formula |
|-----|-------------|---------|
| C1 | Net VAT payable/(refundable) | A7 - B7 |
| C2 | Credit brought forward | From prior period |
| C3 | Net amount payable/(refundable) | C1 - C2 |

---

## Step 4: Reverse Charge on Imported Services [T1]

**Legislation:** VAT Act 2014, s.16 (imported services).

When a Tanzania VAT-registered person receives services from a non-resident supplier who is not registered for VAT in Tanzania:

1. Self-assess output VAT at 18% on the value of services received
2. Claim input VAT at 18% if the service relates to taxable supplies
3. Net effect: zero for fully taxable businesses

**Exceptions:**
- Out-of-scope payments (salaries, dividends, loan repayments): NEVER reverse charge
- Services consumed entirely outside Tanzania: NOT subject to Tanzania VAT
- Non-resident suppliers who are VAT-registered in Tanzania: normal supply rules apply

---

## Step 5: Deductibility Check

### Blocked Input Tax Categories [T1]
**Legislation:** VAT Act 2014, s.64 (non-deductible input tax).

The following purchases have ZERO VAT recovery:
- Entertainment expenses (s.64(a))
- Motor vehicles designed for carrying passengers of less than 13 seats, unless used for taxi, car hire, or driving instruction (s.64(b))
- Club subscriptions of a recreational nature (s.64(c))
- Goods and services for personal or non-business use (s.64(d))
- Goods and services not used in making taxable supplies (s.64(e))

### Registration-Based Recovery [T1]
- VAT-registered: input VAT recoverable subject to category rules
- Unregistered: NO input VAT recovery

### Partial Exemption [T2]
**Legislation:** VAT Act 2014, s.62 (apportionment).

If business makes both taxable and exempt supplies:
`Recovery % = (Taxable Supplies / Total Supplies) * 100`

**Flag for reviewer: TRA may approve alternative apportionment methods. De minimis rule: if exempt supplies are less than 5% of total, full input recovery may be allowed. Reviewer must confirm.**

---

## Step 5b: Withholding VAT (effective 1 July 2025) [T1]

**Legislation:** Finance Act 2025 (amending VAT Act 2014).

### Mechanism
- Designated withholding agents (Ministry of Finance, government institutions retaining own-source revenue, VAT-registered persons appointed by the Commissioner General) must withhold part of the VAT on taxable supplies when making payments
- Withholding rate: **3% of the VAT amount for goods** and **6% of the VAT amount for services**
- Withheld VAT must be remitted to TRA by the 20th of the following month
- Supplier must be issued a VAT Withholding Certificate to claim the amount as input tax
- Input VAT is NOT creditable without a valid VAT Withholding Certificate issued on or before the VAT due date

---

## Step 6: Deemed Supplies [T1]

**Legislation:** VAT Act 2014, s.6 (deemed supplies).

A deemed supply arises when:
- Goods are applied for non-business purposes
- Goods are given away free of charge (gifts exceeding TZS 100,000)
- Business assets are used for private purposes
- A VAT-registered person ceases to be registered and holds stock/assets

Output VAT at 18% must be accounted for on the open market value of deemed supplies.

---

## Step 7: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory VAT registration | TZS 200,000,000 annual turnover | VAT Act 2014, s.28(1) |
| Voluntary VAT registration | Below TZS 200,000,000 (with approval) | VAT Act 2014, s.29 |
| Capital goods threshold | TZS 1,000,000 per item | Practice |
| Gift/deemed supply de minimis | TZS 100,000 per gift | VAT Act 2014, s.6(2) |

---

## Step 8: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|-----------|--------|----------|-------------|
| VAT return filing | Monthly | 20th of following month | VAT Act 2014, s.44 |
| VAT payment | Monthly | 20th of following month (same as return) | VAT Act 2014, s.44 |

### Late Filing Penalties [T1]
**Legislation:** Tax Administration Act 2015, s.78-79.
- Late filing penalty: 1% of tax due per month or part thereof, up to 100%
- Interest on late payment: Bank of Tanzania discount rate + 5%, computed daily
- Minimum penalty: TZS 150,000 per return

---

## Step 9: EAC Customs Union Considerations [T1]

**Legislation:** EAC Customs Management Act 2004; Protocol on the Establishment of the EAC Customs Union.

- Tanzania is part of the EAC Customs Union. Goods moving between EAC states may attract preferential customs duty rates but VAT is charged at the border as an import.
- EAC Rules of Origin certificates are required for preferential treatment on customs duty; VAT is still payable on imports from EAC states.
- There is NO intra-community VAT mechanism like the EU. Each EAC member charges its own VAT on imports.

---

## PROHIBITIONS [T1]

- NEVER let AI guess return box assignment -- it is deterministic from transaction facts
- NEVER allow input VAT recovery on blocked categories (entertainment, motor vehicles, personal use)
- NEVER confuse zero-rated (input VAT recoverable) with exempt (input VAT NOT recoverable)
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, loans)
- NEVER allow unregistered persons to claim input VAT
- NEVER treat EAC transactions as intra-community supplies (no EU-style mechanism)
- NEVER ignore deemed supply rules when goods are used for non-business purposes
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER file a return without checking for credit brought forward from prior period

---

## Step 10: Edge Case Registry

### EC1 -- Import of services from non-resident (SaaS subscription) [T1]
**Situation:** Tanzania company subscribes to Microsoft 365 from a non-resident supplier. Monthly fee USD 100. No VAT on invoice.
**Resolution:** Reverse charge applies. Self-assess output VAT at 18% on TZS equivalent. Claim input VAT at 18% if used for taxable supplies. Net effect: zero for fully taxable business.
**Legislation:** VAT Act 2014, s.16.

### EC2 -- Export of services to Kenya [T1]
**Situation:** Tanzania consulting firm provides advisory services to a Kenyan company. Services consumed in Kenya.
**Resolution:** Zero-rated supply. Report in Box A2. No output VAT. Input VAT on related costs is fully recoverable.
**Legislation:** VAT Act 2014, First Schedule.

### EC3 -- Goods imported from Uganda via EAC [T1]
**Situation:** Tanzania retailer imports consumer goods from Ugandan supplier. Goods clear customs at Namanga border.
**Resolution:** VAT at 18% is charged at customs. Customs documentation (import entry) evidences the VAT paid. The 18% VAT paid at customs is recoverable as input VAT (Box B4) if goods are for taxable supplies. No intra-community mechanism -- treated as a normal import.
**Legislation:** VAT Act 2014, s.15; EAC CMA 2004.

### EC4 -- Mining company purchases [T3]
**Situation:** Mining company purchases heavy equipment and seeks VAT refund.
**Resolution:** Mining sector has special provisions under the Mining Act 2010 and specific VAT relief orders. Escalate to licensed accountant. Do not classify without specialist mining tax advice.
**Legislation:** Mining Act 2010; VAT Act 2014, Third Schedule.

### EC5 -- Deemed supply on cessation of registration [T1]
**Situation:** A business deregisters for VAT while holding TZS 50,000,000 of inventory.
**Resolution:** Output VAT at 18% must be accounted for on the market value of inventory and capital assets held at the date of deregistration. This is a deemed supply. Report in output tax section.
**Legislation:** VAT Act 2014, s.6(1)(c).

### EC6 -- Tourist hotel supplies (tourism sector) [T2]
**Situation:** Hotel charges for accommodation and restaurant services to foreign tourists.
**Resolution:** Hotel accommodation is standard-rated at 18%. Tourism-related services may qualify for zero-rating if the tourist pays in foreign currency and certain conditions are met. Flag for reviewer: confirm whether the specific supply qualifies under the tourism incentive regime and whether the foreign currency condition is met.
**Legislation:** VAT Act 2014; Tourism regulations.

### EC7 -- Credit note for overcharged VAT [T1]
**Situation:** Supplier issues a credit note for TZS 500,000 previously invoiced including VAT.
**Resolution:** Reduce output VAT by the VAT component of the credit note. Report adjustment in Box A6 (output adjustments). The customer must also adjust their input VAT claim.
**Legislation:** VAT Act 2014, s.63.

### EC8 -- Bad debt relief [T2]
**Situation:** Supplier has accounted for output VAT but customer has not paid for 12 months.
**Resolution:** Bad debt relief is available if: (a) debt has been outstanding for at least 12 months; (b) debt has been written off in the accounts; (c) supplier has taken reasonable steps to recover. Flag for reviewer: TRA may require documentation. Claim through output adjustments.
**Legislation:** VAT Act 2014, s.65.

---

## Step 11: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Licensed accountant (NBAA registered CPA) must confirm before filing.
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
**Input:** Tanzania company sells goods for TZS 10,000,000 net. Standard-rated. VAT-registered.
**Expected output:** Box A1 = TZS 10,000,000. Box A5 = TZS 1,800,000 (18%). Total output = TZS 1,800,000.

### Test 2 -- Local purchase, input VAT recovery [T1]
**Input:** VAT-registered company purchases office furniture from local supplier. Invoice: TZS 5,000,000 + TZS 900,000 VAT (18%) = TZS 5,900,000. Not blocked category.
**Expected output:** Box B1 = TZS 5,000,000. Box B3 = TZS 900,000. Input VAT recoverable in full.

### Test 3 -- Reverse charge on imported services [T1]
**Input:** VAT-registered company receives IT services from Indian firm. Invoice USD 2,000 (approx. TZS 5,000,000). No VAT charged.
**Expected output:** Self-assess output VAT = TZS 900,000 (18%). Input VAT claim = TZS 900,000 (if fully taxable). Net effect = zero.

### Test 4 -- Export of goods (zero-rated) [T1]
**Input:** Tanzania exporter ships coffee worth TZS 100,000,000 to Germany.
**Expected output:** Box A2 = TZS 100,000,000. Output VAT = TZS 0. Input VAT on related costs is fully recoverable.

### Test 5 -- Blocked input (entertainment) [T1]
**Input:** VAT-registered company hosts client dinner. Invoice: TZS 2,000,000 + TZS 360,000 VAT = TZS 2,360,000.
**Expected output:** Input VAT = TZS 0 (BLOCKED -- entertainment). Cost = TZS 2,360,000 including irrecoverable VAT.

### Test 6 -- Exempt supply (financial services) [T1]
**Input:** Bank provides loan interest income of TZS 50,000,000.
**Expected output:** Box A3 = TZS 50,000,000 (exempt). No output VAT. Input VAT on expenses related to exempt supplies is NOT recoverable.

### Test 7 -- Import from EAC state [T1]
**Input:** Company imports goods from Kenya valued at TZS 20,000,000. Customs charges VAT at 18%.
**Expected output:** Box B2 = TZS 20,000,000. Box B4 = TZS 3,600,000. Input VAT recoverable if for taxable supplies. No intra-community mechanism.

### Test 8 -- Deemed supply (business gift) [T1]
**Input:** Company gives promotional goods worth TZS 500,000 (market value) to a client.
**Expected output:** Deemed supply. Output VAT = TZS 90,000 (18% of TZS 500,000). Report in output section. Gift exceeds TZS 100,000 de minimis threshold.

---

## Step 13: Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference only. Escalate to licensed accountant.

- **Corporate Income Tax:** 30% standard rate. Mining: 30% + additional profits tax. Agriculture: concessional rates may apply.
- **PAYE:** Separate employer obligation under the Income Tax Act 2004. Progressive rates from 0% to 30%.
- **Skills Development Levy (SDL):** 4% of gross payroll. Separate from VAT.
- **NSSF/PPF:** Social security contributions. Employer 10% + Employee 10%. Separate from VAT.

---

## Contribution Notes

This skill was adapted from the Malta VAT Return Preparation Skill template. Tanzania-specific elements include the 18% rate structure (16% reduced rate for non-VAT-registered B2C electronic payments from Sep 2025), EAC customs union considerations, deemed supply rules, mining sector escalation, and new VAT withholding regime (3% goods / 6% services from July 2025). Updated April 2026.

**A skill may not be published without sign-off from a licensed practitioner (NBAA registered CPA) in Tanzania.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
