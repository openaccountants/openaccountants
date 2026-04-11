---
name: ethiopia-vat
description: Use this skill whenever asked to prepare, review, or create an Ethiopia VAT return for any client. Trigger on phrases like "prepare VAT return", "do the Ethiopia VAT", "MOR return", "fill in VAT return", or any request involving Ethiopia VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Ethiopia VAT classification rules, return form mappings, deductibility rules, turnover tax alternative, reverse charge treatment, registration thresholds, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Ethiopia VAT-related work.
---

# Ethiopia VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Ethiopia (Federal Democratic Republic of Ethiopia) |
| Jurisdiction Code | ET |
| Primary Legislation | Value Added Tax Proclamation No. 1341/2024 (effective 21 August 2024, replacing Proclamation No. 285/2002) |
| Supporting Legislation | Income Tax Amendment Proclamation No. 1395/2025; Tax Administration Proclamation No. 983/2016 |
| Tax Authority | Ministry of Revenues (MOR) / Ethiopian Customs Commission (for imports) |
| Filing Portal | eTax system (https://etax.mor.gov.et) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by a licensed auditor/accountant in Ethiopia |
| Validation Date | Pending |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: rate application, return form mapping, registration threshold, deadlines, blocked categories. Tier 2: partial exemption, mixed supplies, Turnover Tax boundary cases. Tier 3: investment incentives, special economic zones, customs valuation. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN** [T1] -- Ethiopia Taxpayer Identification Number
2. **VAT registration status** [T1] -- VAT-registered or Turnover Tax (TOT) registered
3. **VAT period** [T1] -- monthly filing for VAT-registered; quarterly for TOT
4. **Industry/sector** [T2] -- impacts classification (e.g., construction, agriculture, manufacturing have special provisions)
5. **Does the business make exempt supplies?** [T2] -- if yes, input VAT apportionment required
6. **Does the business import goods?** [T1] -- customs VAT is collected at port of entry
7. **Excess credit brought forward** [T1] -- from prior period
8. **Does the business have any investment incentive certificates?** [T2] -- may affect VAT treatment of capital goods imports

**If items 1-2 are unknown, STOP. Do not classify any transactions until registration status is confirmed.**

---

## Step 1: VAT Rate Structure [T1]

### Rates

| Rate | Description | Legislation |
|------|-------------|-------------|
| 15% | Standard rate on all taxable supplies | VAT Proclamation 1341/2024 |
| 0% | Zero rate (exports, specified supplies) | VAT Proclamation 1341/2024 |
| Exempt | No VAT charged, no input recovery | VAT Proclamation 1341/2024 |

### Zero-Rated Supplies [T1]
**Legislation:** VAT Proclamation 285/2002, Schedule 1.
- Export of goods
- Export of services (services rendered to a person outside Ethiopia, consumed outside Ethiopia)
- International transport services
- Supply of gold to the National Bank of Ethiopia
- Supplies to diplomats and international organizations (with MOR approval)

### Exempt Supplies [T1]
**Legislation:** VAT Proclamation 285/2002, Schedule 2.
- Sale or rental of residential dwellings
- Financial services (interest, commissions on loans, life insurance premiums)
- Supply of goods and services by religious organizations
- Medical and healthcare services (by licensed practitioners and hospitals)
- Educational services (by licensed institutions)
- Postal services provided by the Ethiopian Postal Service
- Supply of electricity, water, and kerosene (for domestic use)
- Bread and milk (basic foodstuffs)
- Import of goods for personal use (below ETB 5,000)
- Goods and services supplied to the Ethiopian military

---

## Step 2: Turnover Tax (TOT) -- ABOLISHED [T1]

**The Turnover Tax regime (Proclamation No. 308/2002) has been repealed under Income Tax Amendment Proclamation No. 1395/2025.** TOT no longer applies.

For businesses below the VAT registration threshold (ETB 2,000,000), Category B taxpayers pay tax based on gross sales at rates ranging from 2% to 9% under the income tax regime. Professionals and VAT-registered businesses are excluded from this category.

**Critical rules:**
- TOT is abolished -- there is no longer a separate turnover tax
- Businesses below ETB 2,000,000 annual turnover are not required to register for VAT
- Voluntary VAT registration is available for businesses with turnover between ETB 1,000,000 and ETB 2,000,000

---

## Step 3: Transaction Classification Rules

### 3a. Determine Transaction Type [T1]
- Sale (output VAT) or Purchase (input VAT)
- Salaries, pension contributions, PAYE, dividends, loan repayments = OUT OF SCOPE
- **Legislation:** VAT Proclamation 285/2002, Art. 3 (definition of taxable transaction)

### 3b. Determine Counterparty Location [T1]
- Domestic (Ethiopia): supplier/customer within Ethiopia
- Foreign: all other countries
- **Note:** Ethiopia is not part of any customs union with common VAT rules. All imports are treated uniformly.

### 3c. Determine Supply Type [T1]
- Goods: tangible movable property and immovable property
- Services: everything that is not goods
- Imports of goods: VAT collected by Ethiopian Customs Commission at port/border
- Imports of services: reverse charge mechanism applies
- **Legislation:** VAT Proclamation 285/2002, Art. 4 (supply of goods), Art. 5 (supply of services)

### 3d. Determine Expense Category [T1]
- Capital goods: assets acquired for use in the business with useful life exceeding one year
- Overhead/services: operating expenses
- Resale goods: goods purchased for direct resale
- **Legislation:** VAT Proclamation 285/2002, Art. 20 (input tax deduction)

---

## Step 4: VAT Return Form Structure [T1]

The Ethiopia VAT return is filed monthly via the MOR eTax system.

### Output Section

| Box | Description | Mapping |
|-----|-------------|---------|
| 1 | Standard-rated supplies (15%) | Net value of taxable sales at 15% |
| 2 | Zero-rated supplies | Net value of export and zero-rated supplies |
| 3 | Exempt supplies | Net value of exempt supplies |
| 4 | Total supplies | Box 1 + Box 2 + Box 3 |
| 5 | Output VAT (15% on Box 1) | VAT charged on standard-rated supplies |
| 6 | Output VAT on imported services (reverse charge) | Self-assessed at 15% |
| 7 | Adjustments to output tax | Credit notes, corrections |
| 8 | Total output tax | Box 5 + Box 6 + Box 7 |

### Input Section

| Box | Description | Mapping |
|-----|-------------|---------|
| 9 | Local taxable purchases | Net value of local purchases with VAT |
| 10 | Imports of goods (customs entries) | Net value from customs documentation |
| 11 | Input VAT on local purchases | 15% VAT on Box 9 |
| 12 | Input VAT on imports of goods | VAT from customs (Box 10) |
| 13 | Input VAT on imported services (reverse charge) | Self-assessed at 15% |
| 14 | Adjustments to input tax | Blocked items, apportionment |
| 15 | Total input VAT claimed | Box 11 + Box 12 + Box 13 - Box 14 |

### Net Calculation

| Box | Description | Formula |
|-----|-------------|---------|
| 16 | Net VAT payable/(refundable) | Box 8 - Box 15 |
| 17 | Credit brought forward | From prior period |
| 18 | Net amount payable/(refundable) | Box 16 - Box 17 |

---

## Step 5: Reverse Charge on Imported Services [T1]

**Legislation:** VAT Proclamation 285/2002, Art. 10 (imported services).

When an Ethiopian VAT-registered person receives services from a non-resident supplier:

1. Self-assess output VAT at 15% on the value of services received (Box 6)
2. Claim input VAT at 15% if the service relates to making taxable supplies (Box 13)
3. Net effect: zero for fully taxable businesses

**Exceptions:**
- Out-of-scope payments (salaries, dividends, loan repayments): NEVER reverse charge
- Services consumed entirely outside Ethiopia: NOT subject to Ethiopian VAT
- Where non-resident has a permanent establishment in Ethiopia and is VAT-registered: normal supply rules apply

---

## Step 6: Deductibility Check

### Blocked Input Tax Categories [T1]
**Legislation:** VAT Proclamation 285/2002, Art. 21 (non-deductible input tax).

The following purchases have ZERO VAT recovery:
- Entertainment and hospitality expenses (Art. 21(1)(a))
- Motor vehicles with fewer than 10 seats, unless used for business of transporting passengers for hire or driving instruction (Art. 21(1)(b))
- Goods and services for personal or non-business use (Art. 21(1)(c))
- Goods and services not used in making taxable supplies (Art. 21(1)(d))
- Purchases from non-VAT-registered suppliers (no valid VAT invoice) (Art. 22)

### Registration-Based Recovery [T1]
- VAT-registered: input VAT recoverable subject to category rules
- TOT-registered: NO input VAT recovery
- Unregistered: NO input VAT recovery

### Partial Exemption [T2]
**Legislation:** VAT Proclamation 285/2002, Art. 20(3) (apportionment).

If business makes both taxable and exempt supplies:
`Recovery % = (Taxable Supplies / Total Supplies) * 100`

**Flag for reviewer: MOR may prescribe alternative apportionment methods. Reviewer must confirm the method used and whether annual adjustment is required.**

---

## Step 7: Invoicing Requirements [T1]

**Legislation:** VAT Proclamation 285/2002, Art. 22; VAT Regulation 79/2002.

A valid VAT invoice (tax invoice) must contain:
- Supplier's name, address, and TIN
- Customer's name, address, and TIN (if VAT-registered)
- Sequential invoice number
- Date of issue
- Description of goods or services
- Quantity and unit price
- VAT amount shown separately
- Total amount including VAT

**Critical rule:** Input VAT is NOT recoverable without a valid VAT invoice from a registered taxpayer. Cash register receipts from registered taxpayers are acceptable for retail purchases up to ETB 500.

---

## Step 8: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory VAT registration | ETB 2,000,000 annual turnover | VAT Proclamation 1341/2024 |
| Voluntary VAT registration | ETB 1,000,000 to ETB 2,000,000 (with MOR approval) | VAT Proclamation 1341/2024 |
| TOT applicability | ABOLISHED (repealed by Proclamation 1395/2025) | -- |
| Cash register receipt limit | ETB 500 (for input VAT without full invoice) | MOR regulations |

---

## Step 9: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|-----------|--------|----------|-------------|
| VAT return filing | Monthly | Last day of following month | VAT Proclamation 1341/2024 |
| VAT payment | Monthly | Same as return deadline | VAT Proclamation 1341/2024 |
| TOT return filing | ABOLISHED | -- | -- |
| TOT payment | ABOLISHED | -- | -- |

### Late Filing Penalties [T1]
**Legislation:** Tax Administration Proclamation 983/2016.
- Late filing penalty: ETB 5,000 for each month or part thereof
- Interest on late payment: 2% per month or part thereof (simple interest)
- Failure to register: 100% of tax that should have been collected, plus penalties
- Understatement of tax: 10% of the understated amount, plus interest

---

## PROHIBITIONS [T1]

- NEVER let AI guess return box assignment -- it is deterministic from transaction facts
- NEVER allow input VAT recovery without a valid VAT invoice from a registered supplier
- NEVER allow TOT taxpayers to charge VAT or recover input VAT
- NEVER confuse zero-rated (input VAT recoverable) with exempt (input VAT NOT recoverable)
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, loans)
- NEVER allow recovery of input VAT on blocked categories (entertainment, motor vehicles, personal use)
- TOT has been ABOLISHED -- do not reference or apply turnover tax rules
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER file a return without checking for credit brought forward from prior period
- NEVER allow VAT recovery on purchases from unregistered suppliers

---

## Step 10: Edge Case Registry

### EC1 -- Import of services from non-resident (cloud software) [T1]
**Situation:** Ethiopian VAT-registered company subscribes to AWS cloud services. Monthly fee USD 500. No VAT on invoice.
**Resolution:** Reverse charge applies. Self-assess output VAT at 15% on ETB equivalent (Box 6). Claim input VAT at 15% (Box 13) if used for taxable supplies. Net effect: zero for fully taxable business.
**Legislation:** VAT Proclamation 285/2002, Art. 10.

### EC2 -- Purchase from unregistered supplier [T1]
**Situation:** VAT-registered company purchases goods from a market trader who is not VAT-registered.
**Resolution:** No VAT invoice issued. Input VAT is NOT recoverable. The purchase is a cost including any implied tax. Report as a cost in the accounts but NOT in the VAT return input section.
**Legislation:** VAT Proclamation 285/2002, Art. 22.

### EC3 -- Export of coffee (zero-rated) [T1]
**Situation:** Ethiopian coffee exporter ships 10 tonnes of green coffee to Italy.
**Resolution:** Zero-rated supply. Report net value in Box 2. No output VAT. Input VAT on related purchases (processing, transport, packaging) is fully recoverable.
**Legislation:** VAT Proclamation 285/2002, Schedule 1.

### EC4 -- Business exceeds VAT registration threshold [T1]
**Situation:** A small retailer reaches ETB 2,500,000 cumulative turnover in 9 months.
**Resolution:** Must register for VAT as turnover exceeds ETB 2,000,000 threshold within 12 months. From the date of VAT registration, must charge 15% VAT and file monthly returns. TOT no longer applies (abolished).
**Legislation:** VAT Proclamation 1341/2024.

### EC5 -- Construction services (withholding tax interaction) [T2]
**Situation:** Construction company provides services to a government entity. Government entity withholds 2% income tax from the payment.
**Resolution:** The 2% withholding tax is an income tax obligation, NOT a VAT issue. VAT must still be charged at 15% on the full value of services. The withholding tax reduces the cash received but does not affect the VAT calculation. Flag for reviewer: confirm that the government entity is not confusing withholding tax with VAT.
**Legislation:** VAT Proclamation 285/2002; Income Tax Proclamation 979/2016, Art. 92.

### EC6 -- Investment incentive certificate holder importing capital goods [T2]
**Situation:** A manufacturing company with an Ethiopian Investment Commission certificate imports production machinery.
**Resolution:** Depending on the investment incentive, the import may be exempt from customs duty AND VAT on capital goods. Flag for reviewer: confirm the specific incentive certificate, its validity, and whether it covers VAT exemption or only customs duty exemption. MOR customs division must verify.
**Legislation:** Investment Proclamation No. 1180/2020; VAT Proclamation 285/2002, Schedule 2.

### EC7 -- Deemed supply on business gifts [T1]
**Situation:** Company distributes branded merchandise worth ETB 200,000 to clients at a trade fair.
**Resolution:** Business gifts of goods are deemed supplies. Output VAT at 15% must be accounted for on the market value. No de minimis threshold for business gifts under Ethiopian VAT law.
**Legislation:** VAT Proclamation 285/2002, Art. 6 (deemed supply).

### EC8 -- Mixed supply (exempt and taxable) [T2]
**Situation:** A private hospital provides both exempt medical services and taxable cafeteria/restaurant services.
**Resolution:** Input VAT must be apportioned. Direct costs allocated to each supply type. Common costs apportioned by turnover ratio. Flag for reviewer: confirm apportionment method with MOR.
**Legislation:** VAT Proclamation 285/2002, Art. 20(3).

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
Action Required: Licensed accountant must confirm before filing.
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
**Input:** Ethiopian company sells goods for ETB 100,000 net. Standard-rated. VAT-registered.
**Expected output:** Box 1 = ETB 100,000. Box 5 = ETB 15,000 (15%). Total output = ETB 15,000.

### Test 2 -- Local purchase, input VAT recovery [T1]
**Input:** VAT-registered company purchases raw materials from VAT-registered supplier. Invoice: ETB 50,000 + ETB 7,500 VAT = ETB 57,500.
**Expected output:** Box 9 = ETB 50,000. Box 11 = ETB 7,500. Input VAT recoverable in full.

### Test 3 -- Reverse charge on imported services [T1]
**Input:** VAT-registered company receives consulting from UK firm. Invoice ETB 200,000. No VAT.
**Expected output:** Box 6 = ETB 30,000 (output, 15%). Box 13 = ETB 30,000 (input). Net effect = zero.

### Test 4 -- Export (zero-rated) [T1]
**Input:** Exporter ships flowers worth ETB 5,000,000 to Netherlands.
**Expected output:** Box 2 = ETB 5,000,000. Output VAT = ETB 0. Input VAT on related costs is fully recoverable.

### Test 5 -- Blocked input (entertainment) [T1]
**Input:** VAT-registered company hosts event for clients. Invoice: ETB 30,000 + ETB 4,500 VAT = ETB 34,500.
**Expected output:** Input VAT = ETB 0 (BLOCKED -- entertainment). Cost = ETB 34,500 including irrecoverable VAT.

### Test 6 -- Purchase from unregistered supplier [T1]
**Input:** Company buys supplies from unregistered trader for ETB 10,000. No VAT invoice.
**Expected output:** No entry in VAT return input section. ETB 10,000 is a cost. No input VAT recovery.

### Test 7 -- Below-threshold business (no VAT) [T1]
**Input:** Small retailer with annual turnover ETB 1,500,000 (below ETB 2,000,000 threshold) sells goods.
**Expected output:** Not required to register for VAT. No VAT charged. Subject to Category B income tax on gross sales (2%-9%). May voluntarily register for VAT if turnover exceeds ETB 1,000,000.

### Test 8 -- Motor vehicle (blocked) [T1]
**Input:** Company purchases a sedan for ETB 2,000,000 + VAT ETB 300,000.
**Expected output:** Input VAT = ETB 0 (BLOCKED -- passenger motor vehicle < 10 seats). Total cost = ETB 2,300,000.

---

## Step 13: Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. Reference only. Escalate to licensed accountant.

- **Corporate Income Tax:** 30% standard rate. Mining: 25%. Agriculture: concessional rates may apply.
- **PAYE:** Progressive rates from 0% to 35%. Employer obligation.
- **Pension:** 7% employer + 7% employee (private sector). Separate from VAT.
- **Withholding Tax:** Various rates depending on payment type (2%-15%). Income tax obligation.

---

## Contribution Notes

This skill was adapted from the Malta VAT Return Preparation Skill template. Ethiopia-specific elements include the single 15% rate, purchase-from-unregistered-supplier rules, and investment incentive interactions. Updated April 2026 to reflect VAT Proclamation 1341/2024 (replacing 285/2002): registration threshold raised to ETB 2,000,000, Turnover Tax abolished under Proclamation 1395/2025, digital services VAT framework added.

**A skill may not be published without sign-off from a licensed practitioner in Ethiopia.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
