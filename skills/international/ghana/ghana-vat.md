---
name: ghana-vat
description: Use this skill whenever asked to prepare, review, or create a Ghana VAT/NHIL/GETFund/COVID-19 HRL return for any client. Trigger on phrases like "prepare VAT return", "do the Ghana VAT", "fill in VAT return", "GRA return", "NHIL", "GETFund levy", or any request involving Ghana VAT filing. Also trigger when classifying transactions for VAT purposes from bank statements, invoices, or other source data. This skill contains the complete Ghana VAT classification rules, levy structure, return form mappings, deductibility rules, withholding VAT treatment, registration thresholds, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Ghana VAT-related work.
---

# Ghana VAT Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Ghana |
| Jurisdiction Code | GH |
| Primary Legislation | Value Added Tax Act, 2025 (Act 1151), effective 1 January 2026 (repeals Act 870) |
| Supporting Legislation | National Health Insurance Act 2012 (Act 852); GETFund Act 2000 (Act 581) |
| Tax Authority | Ghana Revenue Authority (GRA) |
| Filing Portal | https://taxpayersportal.ghana.gov.gh |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires validation by a licensed Chartered Accountant (ICAG member) in Ghana |
| Validation Date | Pending |
| Skill Version | 2.0 |
| Confidence Coverage | Tier 1: rate application, levy computation, return box assignment, registration threshold, deadlines. Tier 2: partial exemption, mixed supplies, withholding VAT reconciliation. Tier 3: complex group structures, transfer pricing, customs valuation disputes. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed accountant must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed accountant and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and TIN (Taxpayer Identification Number)** [T1] -- format: Pxx-xxxxxxx-x or Cxx-xxxxxxx-x
2. **VAT registration status** [T1] -- registered (mandatory or voluntary) or unregistered
3. **VAT period** [T1] -- monthly filing
4. **Industry/sector** [T2] -- impacts classification (e.g., financial services exempt; mining has special rules)
5. **Does the business make exempt supplies?** [T2] -- if yes, input VAT apportionment required; reviewer must confirm method
6. **Does the business act as a withholding VAT agent?** [T1] -- designated withholding agents must withhold 7% of VAT charged
7. **Excess credit brought forward** [T1] -- from prior period
8. **Does the business import goods?** [T1] -- customs VAT is handled at port of entry

**If items 1-2 are unknown, STOP. Do not classify any transactions until registration status and TIN are confirmed.**

---

## Step 1: VAT and Levy Rate Structure [T1]

### Composite Rate Breakdown

Ghana applies VAT plus two mandatory levies on the same taxable base. Under Act 1151 (effective 1 January 2026), the levies have been re-coupled with VAT:

| Component | Rate | Legislation |
|-----------|------|-------------|
| VAT (standard) | 15% | VAT Act 2025 (Act 1151) |
| NHIL (National Health Insurance Levy) | 2.5% | NHIA Act 2012 (Act 852), s.40 |
| GETFund Levy | 2.5% | GETFund Act 2000 (Act 581), s.3 |
| **Effective total rate** | **20%** | -- |

**Critical change under Act 1151:** The COVID-19 Health Recovery Levy (1%) has been abolished. NHIL and GETFund have been re-coupled with VAT and are now treated as deductible input taxes -- VAT-registered taxpayers CAN claim NHIL and GETFund paid on purchases as input tax credit. This reverses the pre-2026 rule where only the 15% VAT component was recoverable.

### Flat Rate Scheme -- ABOLISHED

**The VAT Flat Rate Scheme (VFRS) has been abolished under Act 1151, effective 1 January 2026.** All previously eligible businesses must now register under the standard 15% VAT regime (if they meet the registration threshold). There is no longer a 3%, 4%, or 5% flat rate option.

### Zero Rate [T1]
- Exports of goods
- Exports of services (where services are consumed outside Ghana)
- Supplies to Free Zones enterprises (with valid permit)
- **Legislation:** VAT Act 2025 (Act 1151)

### Exempt Supplies [T1]
- Financial services (excluding fee-based services)
- Residential rent
- Medical and dental services
- Educational services
- Unprocessed foodstuffs and agricultural inputs
- Petroleum products (subject to separate excise/levies)
- Water and electricity (domestic use)
- **Legislation:** VAT Act 2025 (Act 1151)

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]
- Sale (output VAT/levies) or Purchase (input VAT)
- Salaries, SSNIT contributions, PAYE, dividends, loan repayments = OUT OF SCOPE (never on VAT return)
- **Legislation:** VAT Act 870, s.2 (definitions of taxable supply)

### 2b. Determine Counterparty Location [T1]
- Domestic (Ghana): supplier/customer is within Ghana
- ECOWAS: Benin, Burkina Faso, Cabo Verde, Gambia, Guinea, Guinea-Bissau, Ivory Coast, Liberia, Mali, Niger, Nigeria, Senegal, Sierra Leone, Togo
- Rest of World: all other countries
- **Note:** ECOWAS membership does not create a common VAT system like the EU. Each country has independent VAT rules.

### 2c. Determine Supply Type [T1]
- Goods: tangible movable property
- Services: everything that is not goods
- Imports of goods: VAT and levies collected by Ghana Customs at the border
- Imports of services: reverse charge mechanism applies (recipient self-accounts)
- **Legislation:** VAT Act 870, s.11 (place of supply); s.16 (imported services)

### 2d. Determine Expense Category [T1]
- Input tax is claimable only on the 15% VAT component
- Capital goods: assets acquired for use in the business over multiple periods
- Overhead/services: operating expenses
- Resale goods: goods purchased for direct resale
- **Legislation:** VAT Act 870, s.41 (input tax deduction)

---

## Step 3: VAT Return Form Structure [T1]

The Ghana VAT return is filed monthly via the GRA Taxpayer Portal. The return captures output tax, input tax, and the three levies separately.

### Output Section

| Box | Description | Mapping |
|-----|-------------|---------|
| 1 | Total taxable supplies (standard rate) | Net value of all 15% standard-rated sales |
| 2 | Zero-rated supplies | Net value of exports and other zero-rated supplies |
| 3 | Exempt supplies | Net value of exempt supplies (no tax) |
| 4 | Total supplies | Box 1 + Box 2 + Box 3 |
| 5 | Output VAT (15% on Box 1) | VAT charged on standard-rated supplies |
| 6 | Output NHIL (2.5% on Box 1) | NHIL on standard-rated supplies |
| 7 | Output GETFund (2.5% on Box 1) | GETFund on standard-rated supplies |
| 8 | Total output tax and levies | Box 5 + Box 6 + Box 7 |

### Input Section

| Box | Description | Mapping |
|-----|-------------|---------|
| 10 | Taxable purchases (local) | Net value of local purchases with VAT |
| 11 | Imports (customs entries) | Net value of imports (from C88/customs docs) |
| 12 | Total input VAT (15% component only) | VAT paid on Box 10 + Box 11 |
| 13 | Input VAT on capital goods | Subset of Box 12 relating to capital assets |
| 14 | Input VAT on overheads | Subset of Box 12 relating to overheads |
| 15 | Input VAT on resale goods | Subset of Box 12 relating to goods for resale |

### Net Calculation

| Box | Description | Formula |
|-----|-------------|---------|
| 16 | Net VAT payable/(refundable) | Box 5 - Box 12 |
| 17 | Net NHIL payable | Box 6 minus NHIL input credit (recoupled under Act 1151) |
| 18 | Net GETFund payable | Box 7 minus GETFund input credit (recoupled under Act 1151) |
| 19 | Credit brought forward | From prior period |
| 20 | Withholding VAT credits | VAT withheld by designated agents |
| 21 | Net amount payable/(refundable) | Box 16 + Box 17 + Box 18 - Box 19 - Box 20 |

---

## Step 4: Reverse Charge on Imported Services [T1]

**Legislation:** VAT Act 2025 (Act 1151).

When a Ghanaian VAT-registered person receives services from a non-resident supplier:

1. Self-assess output VAT at 15% on the value of services received
2. Self-assess NHIL at 2.5%, GETFund at 2.5%
3. Claim input VAT (15% component) and input NHIL/GETFund if the service relates to taxable supplies (levies are now recoupled and recoverable under Act 1151)

**Exceptions to reverse charge:**
- Out-of-scope payments (wages, dividends, loan repayments): NEVER reverse charge
- Services consumed entirely outside Ghana: NOT subject to Ghana VAT
- Supplies by non-residents already registered for VAT in Ghana: normal supply rules apply

---

## Step 5: Withholding VAT [T1]

**Legislation:** VAT Act 870, s.43A (withholding VAT); GRA guidelines on designated agents.

### Mechanism
- Designated withholding VAT agents (government bodies, large companies appointed by GRA) withhold 7% of the VAT amount (not 7% of the invoice total) when paying VAT-registered suppliers
- The supplier receives a withholding VAT certificate
- The supplier claims credit for VAT withheld against output VAT liability
- The agent remits the withheld amount directly to GRA

### Example [T1]
Invoice: GHS 1,000 net + GHS 150 VAT (15%) + GHS 25 NHIL + GHS 25 GETFund = GHS 1,200 total.
Withholding agent withholds: 7% of GHS 150 = GHS 10.50.
Supplier receives: GHS 1,200 - GHS 10.50 = GHS 1,189.50.
Supplier claims GHS 10.50 as withholding VAT credit on their return (Box 20).

---

## Step 6: Deductibility Check

### Blocked Input Tax Categories [T1]
**Legislation:** VAT Act 870, s.42 (non-deductible input tax).

The following purchases have ZERO VAT recovery regardless of business use:
- Entertainment expenses (s.42(1)(a))
- Motor vehicles (unless used exclusively for business of transporting passengers/goods for reward) (s.42(1)(b))
- Club subscriptions and membership fees for recreational purposes (s.42(1)(c))
- Personal use items (s.42(1)(d))
- Goods and services not used in making taxable supplies

**Critical change under Act 1151:** From 1 January 2026, NHIL and GETFund paid on inputs ARE recoverable as input tax credits (recoupled). The COVID-19 HRL has been abolished.

### Registration-Based Recovery [T1]
- VAT-registered (standard scheme): input VAT recoverable subject to category rules
- VAT Flat Rate Scheme: ABOLISHED under Act 1151
- Unregistered persons: NO input VAT recovery

### Partial Exemption (Apportionment) [T2]
**Legislation:** VAT Act 870, s.41(5) (apportionment of input tax).

If business makes both taxable and exempt supplies:
`Recovery % = (Taxable Supplies / (Taxable Supplies + Exempt Supplies)) * 100`

**Flag for reviewer: apportionment method must be approved by GRA. Standard method is turnover-based, but GRA may approve alternative methods. Annual adjustment required.**

---

## Step 7: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Mandatory VAT registration (goods) | GHS 750,000 annual taxable turnover | VAT Act 2025 (Act 1151) |
| Mandatory VAT registration (services) | All suppliers of services, irrespective of turnover | VAT Act 2025 (Act 1151) |
| Voluntary VAT registration | Below GHS 750,000 (goods only) | VAT Act 2025 (Act 1151) |
| Flat Rate Scheme | ABOLISHED under Act 1151 | -- |
| Withholding VAT rate | 7% of VAT charged | GRA Regulations |
| VAT refund threshold | Excess credits for 3 consecutive months | VAT Act 2025 (Act 1151) |

---

## Step 8: Filing Deadlines [T1]

| Obligation | Period | Deadline | Legislation |
|-----------|--------|----------|-------------|
| VAT return (standard) | Monthly | Last working day of following month | VAT Act 2025 (Act 1151) |
| VAT payment | Monthly | Same as return deadline | VAT Act 2025 (Act 1151) |
| Withholding VAT remittance | Monthly | 15th of following month | GRA Regulations |
| VAT Flat Rate return | ABOLISHED | -- | -- |

### Late Filing Penalties [T1]
- Penalty for late filing: GHS 500 per month or part thereof (s.54)
- Interest on late payment: 125% of the Bank of Ghana monetary policy rate, computed monthly (s.55)
- Failure to register: 100% of tax due plus penalties (s.56)

---

## Step 9: Flat Rate Scheme -- ABOLISHED [T1]

**The VAT Flat Rate Scheme has been abolished under Act 1151 effective 1 January 2026.** All businesses that were previously on the flat rate scheme must now register under the standard 15% VAT regime if they meet the registration threshold (GHS 750,000 for goods; all service providers regardless of turnover). There is no transitional flat rate option.

---

## PROHIBITIONS [T1]

- Under Act 1151 (from 1 Jan 2026), NHIL and GETFund ARE now recoverable as input tax (recoupled). COVID HRL has been abolished
- NEVER let AI guess return box assignment -- it is deterministic from transaction facts
- NEVER apply reverse charge to out-of-scope categories (wages, dividends, loans)
- Flat Rate Scheme has been ABOLISHED under Act 1151 -- all taxpayers now use the standard 15% regime
- NEVER confuse zero-rated (input VAT recoverable) with exempt (input VAT NOT recoverable)
- NEVER allow input VAT recovery on blocked categories (entertainment, motor vehicles, personal use)
- NEVER apply withholding VAT to non-VAT-registered suppliers
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude
- NEVER ignore the withholding VAT credit when computing net liability
- NEVER file a return without reconciling withholding VAT certificates against the claim

---

## Step 10: Edge Case Registry

### EC1 -- Import of services from non-resident (e.g., cloud software from US) [T1]
**Situation:** Ghana VAT-registered company subscribes to US-based SaaS platform, USD 500/month. No VAT on invoice.
**Resolution:** Reverse charge applies. Self-assess output VAT at 15% on GHS equivalent. Also self-assess NHIL 2.5%, GETFund 2.5%. Under Act 1151, claim input VAT, NHIL, and GETFund if used for taxable supplies.
**Legislation:** VAT Act 2025 (Act 1151).

### EC2 -- Former flat rate scheme business transitioning to standard [T1]
**Situation:** A retailer previously on the flat rate scheme (abolished under Act 1151) must now register under the standard 15% regime.
**Resolution:** From 1 January 2026, the business charges 15% VAT + 2.5% NHIL + 2.5% GETFund on sales. Input VAT, NHIL, and GETFund on purchases are recoverable. No transitional flat rate applies.
**Legislation:** VAT Act 2025 (Act 1151).

### EC3 -- Withholding VAT agent pays supplier [T1]
**Situation:** A government ministry (designated withholding agent) pays a VAT-registered supplier. Invoice: GHS 5,000 + VAT GHS 750 + NHIL GHS 125 + GETFund GHS 125 = GHS 6,000.
**Resolution:** Agent withholds 7% of GHS 750 = GHS 52.50. Remits GHS 52.50 to GRA by 15th of following month. Supplier receives GHS 5,947.50. Supplier claims GHS 52.50 as withholding VAT credit on return (Box 20). Agent only withholds on the VAT portion, NOT on NHIL/GETFund.
**Legislation:** VAT Act 2025 (Act 1151).

### EC4 -- Export of goods (zero-rated) [T1]
**Situation:** Ghanaian manufacturer exports cocoa products to Switzerland.
**Resolution:** Output VAT at 0%. No NHIL, GETFund, or COVID HRL on exports. Report net value in zero-rated supplies (Box 2). Input VAT on purchases related to export production is FULLY recoverable. If excess credits arise, claim refund after 3 consecutive months.
**Legislation:** VAT Act 870, First Schedule Part A; s.45 (refunds).

### EC5 -- Mixed supply (taxable and exempt) [T2]
**Situation:** A company provides both financial advisory services (exempt) and IT consulting (taxable).
**Resolution:** Input VAT must be apportioned. Direct costs: allocate to the respective supply. Common costs: apportion using the turnover ratio. Flag for reviewer: GRA must approve the apportionment method. Annual adjustment may be required.
**Legislation:** VAT Act 870, s.41(5).

### EC6 -- Bad debt relief [T2]
**Situation:** Supplier has issued a VAT invoice and accounted for output VAT, but the customer has not paid for 12 months.
**Resolution:** The supplier may claim a deduction for the VAT accounted for on the bad debt, provided: (a) the debt has been outstanding for at least 12 months; (b) the supplier has taken reasonable steps to recover; (c) the debt has been written off in the books. Flag for reviewer: documentation must be adequate. GRA may request proof.
**Legislation:** VAT Act 870, s.44.

### EC7 -- Free Zones enterprise supply [T1]
**Situation:** Ghanaian company supplies raw materials to an enterprise operating in a designated Free Zone.
**Resolution:** Supply is zero-rated. The Free Zones enterprise must provide a valid Free Zones Board permit. Supplier reports in Box 2 (zero-rated). If the Free Zones enterprise sells more than 30% of production locally, special rules apply -- [T2] flag for reviewer.
**Legislation:** VAT Act 870, First Schedule; Free Zones Act 1995 (Act 504).

### EC8 -- Motor vehicle purchase [T1]
**Situation:** Company purchases a pickup truck for business use.
**Resolution:** Input VAT is BLOCKED unless the vehicle is used exclusively for transporting passengers or goods for reward (e.g., taxi, logistics company). If the company is a logistics firm, input VAT may be recoverable -- [T2] flag for reviewer to confirm exclusive business transport use.
**Legislation:** VAT Act 870, s.42(1)(b).

---

## Step 11: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Licensed accountant (ICAG member) must confirm before filing.
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

### Test 1 -- Standard local sale, all levies [T1]
**Input:** Ghanaian company sells goods for GHS 10,000 net. Standard-rated. VAT-registered.
**Expected output:** Box 1 = GHS 10,000. Box 5 = GHS 1,500 (15%). Box 6 = GHS 250 (2.5% NHIL). Box 7 = GHS 250 (2.5% GETFund). Total output = GHS 2,000 (20% effective).

### Test 2 -- Local purchase, input VAT recovery [T1]
**Input:** VAT-registered company (standard scheme) purchases office supplies from local supplier. Invoice: GHS 2,000 + GHS 300 VAT + GHS 50 NHIL + GHS 50 GETFund + GHS 20 COVID HRL = GHS 2,420.
**Expected output:** Box 10 = GHS 2,000. Box 12 = GHS 300 (input VAT). Box 14 = GHS 300 (overhead). Under Act 1151, NHIL (GHS 50) and GETFund (GHS 50) are also recoverable as input tax.

### Test 3 -- Reverse charge on imported services [T1]
**Input:** VAT-registered company receives legal services from UK firm. Invoice GHS 5,000 (no VAT charged by UK firm). Used entirely for taxable supplies.
**Expected output:** Self-assess output VAT = GHS 750 (15%). Self-assess NHIL = GHS 125 (2.5%). Self-assess GETFund = GHS 125 (2.5%). Claim input VAT = GHS 750. Claim input NHIL = GHS 125. Claim input GETFund = GHS 125. Net effect = zero (all components recoverable under Act 1151).

### Test 4 -- Export, zero-rated [T1]
**Input:** Ghanaian exporter ships goods worth GHS 50,000 to buyer in Germany.
**Expected output:** Box 2 = GHS 50,000. Box 5 = GHS 0. No NHIL/GETFund/COVID HRL. Input VAT on related purchases is fully recoverable.

### Test 5 -- Former flat rate scheme business (now standard) [T1]
**Input:** Retailer (formerly on flat rate scheme, now standard scheme under Act 1151) sells goods for GHS 8,000 net.
**Expected output:** Box 1 = GHS 8,000. Output VAT = GHS 1,200 (15%). NHIL = GHS 200 (2.5%). GETFund = GHS 200 (2.5%). Total = GHS 1,600 (20%). Input VAT, NHIL, and GETFund on purchases are recoverable.

### Test 6 -- Withholding VAT [T1]
**Input:** Government ministry pays VAT-registered supplier. Invoice: GHS 20,000 + GHS 3,000 VAT + GHS 500 NHIL + GHS 500 GETFund = GHS 24,000. Ministry is a designated withholding agent.
**Expected output:** Withholding = 7% of GHS 3,000 = GHS 210. Supplier receives GHS 23,790. Supplier claims GHS 210 as withholding VAT credit (Box 20). Ministry remits GHS 210 to GRA by 15th of following month.

### Test 7 -- Blocked input (entertainment) [T1]
**Input:** VAT-registered company hosts client entertainment event. Invoice: GHS 3,000 + GHS 450 VAT + GHS 75 NHIL + GHS 75 GETFund = GHS 3,600.
**Expected output:** Input VAT = GHS 0 (BLOCKED -- entertainment). Total cost = GHS 3,600 including all irrecoverable VAT and levies.

### Test 8 -- Exempt supply (financial services) [T1]
**Input:** Bank provides loan arrangement services for GHS 100,000 fee.
**Expected output:** Box 3 = GHS 100,000 (exempt). No output VAT. No NHIL/GETFund/COVID HRL. Input VAT on expenses related to exempt supplies is NOT recoverable.

---

## Step 13: Out of Scope -- Direct Tax (Reference Only) [T3]

This skill does not compute income tax. The following is reference information only. Do not execute any of these rules. Escalate to licensed accountant.

- **Corporate Income Tax:** Standard rate 25%. Small companies (turnover < GHS 200 million) may qualify for reduced rate. Branch profits subject to 8% branch profits tax.
- **PAYE/Withholding Tax:** Separate employer obligations under the Income Tax Act 2015 (Act 896). Out of scope.
- **SSNIT:** Social Security and National Insurance Trust contributions at 13.5% (employer) + 5.5% (employee). Entirely separate from VAT.
- **Communication Service Tax (CST):** 9% on electronic communication charges. Separate from VAT.

---

## Contribution Notes

This skill was adapted from the Malta VAT Return Preparation Skill template. Ghana-specific elements include the multi-levy structure (NHIL, GETFund -- now recoupled as input-deductible under Act 1151), the withholding VAT mechanism, and Free Zones treatment. Updated April 2026 to reflect VAT Act 2025 (Act 1151) effective 1 January 2026: COVID HRL abolished, flat rate scheme abolished, NHIL/GETFund recoupled, registration threshold raised to GHS 750,000 for goods (all service providers regardless of turnover).

**A skill may not be published without sign-off from a licensed practitioner (ICAG member) in Ghana.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
