---
name: malaysia-sst
description: Use this skill whenever asked to prepare, review, or advise on Malaysia Sales and Service Tax (SST) for any client. Trigger on phrases like "Malaysia SST", "Sales Tax Malaysia", "Service Tax Malaysia", "SST return", "SST-02", "MySST", "RMCD", "SSTax", or any request involving Malaysia SST filing, classification, or compliance. This skill contains the complete Malaysia SST classification rules, return structure, registration thresholds, e-invoicing requirements, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Malaysia SST-related work.
---

# Malaysia Sales and Service Tax (SST) Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Malaysia |
| Jurisdiction Code | MY |
| Primary Legislation | Sales Tax Act 2018 (Act 806); Service Tax Act 2018 (Act 807) |
| Supporting Legislation | Sales Tax Regulations 2018; Service Tax Regulations 2018; Sales Tax (Persons Exempted from Payment of Tax) Order 2018; Service Tax (Digital Service) Regulations 2020; Finance Act 2024 (e-invoicing); Sales Tax (Rate of Tax) Order 2018; Service Tax (Amendment) Regulations 2025 (scope expansion effective 1 July 2025) |
| Tax Authority | Royal Malaysian Customs Department (RMCD / Jabatan Kastam Diraja Malaysia, JKDM) |
| Filing Portal | https://mysst.customs.gov.my (MySST) |
| E-Invoice Portal | https://myinvois.hasil.gov.my (IRBM e-Invoice, from August 2024) |
| Currency | Malaysian Ringgit (MYR / RM) |
| Contributor | [Pending -- must be validated by Malaysian licensed tax agent] |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate application, SST-02 return structure, registration threshold, taxable goods/services classification. Tier 2: mixed supply treatment, group relief, partial exemption, e-invoicing transition. Tier 3: free zone operations, petroleum/crude oil taxation, cross-border digital services from foreign providers. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed Malaysian tax agent must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed tax agent and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and SST registration number** [T1] -- separate registration numbers for Sales Tax and Service Tax
2. **Registration type** [T1] -- Sales Tax registered manufacturer, Service Tax registered service provider, or both
3. **Taxable period** [T1] -- bimonthly (standard for both Sales Tax and Service Tax)
4. **Industry/sector** [T2] -- impacts whether activity attracts Sales Tax, Service Tax, both, or neither
5. **Is the business a manufacturer?** [T1] -- only manufacturers of taxable goods are liable for Sales Tax (not traders/retailers)
6. **Does the business provide prescribed taxable services?** [T1] -- only services listed in the First Schedule of Service Tax Regulations are taxable
7. **Does the business import goods?** [T1] -- Sales Tax at importation is collected by Customs
8. **Is the business in a Free Zone or Licensed Manufacturing Warehouse?** [T3] -- special SST treatment applies; escalate
9. **E-invoicing status** [T2] -- mandatory from August 2024 for turnover > RM 100M; phased rollout through July 2025
10. **Does the business qualify for any Sales Tax exemptions?** [T2] -- Schedule A/B/C exemptions under Sales Tax (Persons Exempted from Payment of Tax) Order 2018

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration type and period are confirmed.**

---

## Step 1: Understanding Malaysia's SST Structure [T1]

**Critical distinction:** Malaysia does NOT have a Value Added Tax (VAT) or Goods and Services Tax (GST). GST was abolished on 1 September 2018 and replaced by the reinstated SST system.

SST consists of TWO separate taxes:

| Tax | Legislation | Scope | Rate |
|-----|-------------|-------|------|
| Sales Tax | Sales Tax Act 2018 (Act 806) | Tax on manufacture and import of taxable goods | 10% (standard), 5% (specific goods), specific rate (e.g., petroleum) |
| Service Tax | Service Tax Act 2018 (Act 807) | Tax on provision of prescribed taxable services | 8% (standard, increased from 6% effective 1 March 2024) |

**Key characteristic:** SST is a single-stage tax. There is NO input tax credit mechanism (unlike VAT/GST). SST paid on inputs is a cost to the business.

---

## Step 2: Sales Tax Rules [T1]

### 2a. Who is Liable for Sales Tax [T1]

**Legislation:** Sales Tax Act 2018, Sections 7, 8, 12, 13

| Liable Person | Condition |
|---------------|-----------|
| Registered manufacturer | Manufacturing taxable goods in Malaysia with turnover exceeding RM 500,000 |
| Importer | Importing taxable goods into Malaysia (collected by Customs at border) |
| Person importing on behalf | Customs agent importing goods |

**Key: Retailers and wholesalers do NOT charge Sales Tax. Only manufacturers and importers are liable.**

### 2b. Sales Tax Rates [T1]

**Legislation:** Sales Tax (Rate of Tax) Order 2018, as amended

| Rate | Application |
|------|-------------|
| 10% | Standard rate -- all taxable goods not otherwise specified |
| 5% | Specific goods: fruits, certain food preparations, specific building materials, IT equipment (as listed in Schedule to the Rate of Tax Order) |
| Specific rate | Petroleum products (per litre/kg basis, set by MOF) |
| Exempt | Goods listed in Sales Tax (Goods Exempted from Tax) Order 2018: basic foodstuffs (rice, sugar, flour, cooking oil, salt), live animals, certain agricultural produce, specific medical devices, etc. |
| Exempt at manufacture, taxed at import | Certain goods exempt when manufactured locally but taxed when imported, and vice versa (refer to exemption schedules) |

### 2c. What Constitutes "Manufacturing" [T1]

**Legislation:** Sales Tax Act 2018, Section 2 (definition); Section 5 (deemed manufacture)

"Manufacture" includes:
- Converting or processing raw materials into finished goods
- Assembling component parts into finished goods
- Any operation that substantially transforms a product

Does NOT include:
- Simple packaging, labeling, or sorting (unless specified)
- Repair and maintenance
- Installation of goods on site

[T2] if the activity is borderline manufacturing -- flag for tax agent confirmation.

### 2d. Sales Tax Exemptions [T1]

**Legislation:** Sales Tax (Persons Exempted from Payment of Tax) Order 2018

| Schedule | Exemption |
|----------|-----------|
| Schedule A | Exemption on raw materials, components, packaging used directly in manufacture of taxable goods (for registered manufacturers) |
| Schedule B | Exemption on machinery and equipment used directly in manufacture |
| Schedule C | Exemption for specific persons/situations (government, diplomatic missions, duty-free shops, etc.) |

To claim Schedule A/B exemption, the registered manufacturer must apply via MySST and receive approval from RMCD.

---

## Step 3: Service Tax Rules [T1]

### 3a. Who is Liable for Service Tax [T1]

**Legislation:** Service Tax Act 2018, Sections 7, 8, 12, 13

| Liable Person | Condition |
|---------------|-----------|
| Registered service provider | Providing prescribed taxable services with turnover exceeding RM 500,000 (RM 1,500,000 for restaurants/food & beverage) |
| Imported service recipient | Any person in Malaysia receiving taxable services from a provider outside Malaysia -- self-account mechanism (Section 26) |
| Digital service provider (foreign) | Foreign digital service provider registered under Section 56C |

### 3b. Service Tax Rate [T1]

**Legislation:** Service Tax Act 2018, Section 9; Finance (No. 2) Act 2023

| Rate | Application | Effective Date |
|------|-------------|----------------|
| 8% | Standard rate for all prescribed taxable services | 1 March 2024 onwards |
| 6% | Previous rate / specific services (food & beverage, telecoms, parking, logistics -- retained at 6% per policy) | Ongoing for specified services |
| 6% (retained) | Food & beverage services | Ongoing |
| 6% (retained) | Telecommunications services | Ongoing |
| 6% (retained) | Vehicle parking services | Ongoing |
| 6% (retained) | Logistics services | Ongoing |

### 3c. Prescribed Taxable Services [T1]

**Legislation:** Service Tax Regulations 2018, First Schedule (Groups A through I)

| Group | Service Category | Notes |
|-------|-----------------|-------|
| A | IT services, digital services | Software development, hosting, cloud, digital content |
| B | Management services | Includes management of real property, clubs, conferences |
| C | Professional services | Legal, accounting, consulting, architecture, engineering, surveying, etc. |
| D | Hire and rental | Vehicles, machinery, equipment hire |
| E | Insurance and takaful | General insurance, life insurance (specific items), reinsurance |
| F | Telecommunication services | Fixed line, mobile, internet services |
| G | Betting and gaming | Casinos, slot machines, lotteries, online gambling |
| H | Credit/charge card services | Annual fees, late payment charges, service charges |
| I | Domestic flights | Air passenger services for domestic segments |

[T2] if a service does not clearly fall within a prescribed group -- flag for tax agent confirmation. Only services explicitly listed are taxable.

### 3e. SST Scope Expansion (Effective 1 July 2025) [T1]

**Legislation:** Service Tax (Amendment) Regulations 2025; MOF press release 25 June 2025

Effective 1 July 2025, the scope of Service Tax was significantly expanded to include the following new service categories:

| New Group / Expansion | Service Category | Rate | Notes |
|----------------------|-----------------|------|-------|
| Rental / leasing services | Rental of equipment, vehicles, machinery (industrial and commercial use) | 8% (reduced to 6% from 1 Jan 2026 for industrial use) | Registration threshold raised to RM 1,000,000 |
| Construction services | All construction activities including residential on mixed development land | 8% | New scope |
| Financial services (Group H expanded) | Banking, insurance, and financial advisory by regulated and unregulated providers | 8% | Registration threshold raised to RM 1,000,000 |
| Private healthcare services | Hospital and allied health professional services to non-Malaysians | 6% | Does NOT apply to services to Malaysians |
| Education services | Private education services | 8% | Specific exemptions for government schools |
| Beauty / wellness services | Spas, wellness centres, beauty treatments | 8% | Under expanded Group C |
| Karaoke / nightclub services | Entertainment establishments | 8% | Under expanded Group C |

**Key compliance note:** For companies that take steps to comply with the prescribed SST legal requirements, no prosecution or penalties will be imposed until 31 December 2025 (grace period).

**MSME threshold increase:** The annual turnover threshold for micro, small, and medium enterprises exempted from paying the Service Tax has been increased from RM 1,000,000 to RM 1,500,000 (for applicable expanded services).

### 3d. Imported Services (Self-Account) [T1]

**Legislation:** Service Tax Act 2018, Section 26

When any person in Malaysia (whether or not SST-registered) receives prescribed taxable services from a provider outside Malaysia:

1. The Malaysian recipient must self-account for Service Tax at 8% (or applicable rate) on the value of the imported service
2. Declare on Form SST-02A
3. Pay within 30 days from the date of payment to the foreign provider OR the date the invoice is received, whichever is earlier
4. **There is NO input credit. The Service Tax paid is a cost.**

---

## Step 4: SST Return Structure [T1]

### SST-02 Return (For Sales Tax and Service Tax) [T1]

**Legislation:** Sales Tax Act 2018, Section 26; Service Tax Act 2018, Section 26; RMCD MySST system

The SST-02 return covers a bimonthly taxable period. It has separate sections for Sales Tax and Service Tax:

### Part A: Sales Tax

| Field | Description | Classification |
|-------|-------------|----------------|
| A1 | Total value of taxable goods sold/disposed at 10% | Standard rate sales |
| A2 | Sales Tax at 10% (A1 * 10%) | Output -- standard |
| A3 | Total value of taxable goods sold/disposed at 5% | Reduced rate sales |
| A4 | Sales Tax at 5% (A3 * 5%) | Output -- reduced |
| A5 | Total value of taxable goods at specific rates | Petroleum/specific |
| A6 | Sales Tax at specific rates | Output -- specific |
| A7 | Value of exempt goods sold/disposed | Exempt sales |
| A8 | Value of goods subject to Schedule A/B/C exemption | Exempt acquisitions |
| A9 | Total Sales Tax payable (A2 + A4 + A6) | Total output |

### Part B: Service Tax

| Field | Description | Classification |
|-------|-------------|----------------|
| B1 | Total value of taxable services provided at 8% | Standard rate services |
| B2 | Service Tax at 8% (B1 * 8%) | Output -- standard |
| B3 | Total value of taxable services at 6% | Retained 6% rate services |
| B4 | Service Tax at 6% (B3 * 6%) | Output -- reduced |
| B5 | Total value of exempt services | Non-taxable services |
| B6 | Total Service Tax payable (B2 + B4) | Total output |

### Part C: Total SST

| Field | Description |
|-------|-------------|
| C1 | Total Sales Tax payable (= A9) |
| C2 | Total Service Tax payable (= B6) |
| C3 | Less: bad debt relief claimed (if applicable) |
| C4 | Less: other adjustments (credit notes, errors) |
| C5 | Net SST payable (C1 + C2 - C3 - C4) |

### Derived Calculations [T1]

```
A9 = A2 + A4 + A6
B6 = B2 + B4
C5 = A9 + B6 - C3 - C4

A2 = A1 * 10%
A4 = A3 * 5%
B2 = B1 * 8%
B4 = B3 * 6%
```

---

## Step 5: Registration Rules [T1]

**Legislation:** Sales Tax Act 2018, Section 12; Service Tax Act 2018, Section 12

### Sales Tax Registration [T1]

| Rule | Detail |
|------|--------|
| Threshold | Manufacturer of taxable goods with total taxable turnover exceeding RM 500,000 in any 12-month period |
| Timing | Must register within 30 days of exceeding threshold |
| Voluntary | Not available (only mandatory registration for manufacturers exceeding threshold) |
| Group registration | Not available under Sales Tax |

### Service Tax Registration [T1]

| Rule | Detail |
|------|--------|
| Threshold (general) | Provider of prescribed taxable services with total taxable turnover exceeding RM 500,000 in any 12-month period |
| Threshold (F&B) | Food and beverage service providers: RM 1,500,000 in any 12-month period |
| Timing | Must register within 30 days of exceeding threshold |
| Voluntary | Available for service providers below threshold who wish to register |
| Group registration | Not available under Service Tax |
| Foreign digital service providers | Must register if providing digital services to consumers in Malaysia with turnover exceeding RM 500,000 (Section 56C) |

### Registration Consequences [T1]

| Status | Tax Obligation |
|--------|---------------|
| Sales Tax registered | Must charge Sales Tax on taxable goods manufactured and sold; can apply for Schedule A/B exemptions on inputs |
| Service Tax registered | Must charge Service Tax on prescribed taxable services provided |
| Not registered (below threshold) | No SST obligation on outputs; SST paid on inputs is a cost |
| Foreign digital service provider (registered) | Must collect and remit Service Tax on digital services to Malaysian consumers |

---

## Step 6: Key Difference -- NO Input Tax Credit [T1]

**THIS IS THE MOST CRITICAL DISTINCTION FROM VAT/GST SYSTEMS.**

**Legislation:** There is NO provision for input tax credit in either the Sales Tax Act 2018 or Service Tax Act 2018.

- SST is a single-stage tax
- Sales Tax paid by a manufacturer on raw materials/components is addressed through the Schedule A/B exemption mechanism (exemption at purchase, NOT credit after payment)
- Service Tax paid on inputs is a **final cost** to the business
- Sales Tax paid on imports of finished goods for resale is a **final cost** to the importer/retailer
- There is NO mechanism to offset SST paid on inputs against SST collected on outputs

### Practical Impact [T1]

| Scenario | Treatment |
|----------|-----------|
| Manufacturer buys raw materials with Sales Tax exemption (Schedule A approved) | No Sales Tax on purchase. Charges Sales Tax on finished goods sold. |
| Manufacturer buys raw materials WITHOUT Schedule A approval | Pays Sales Tax on purchase (cost). Also charges Sales Tax on finished goods sold. Cascading/double tax effect. |
| Service provider pays Service Tax on telecoms/IT inputs | Cost. Cannot offset against Service Tax collected from clients. |
| Retailer imports finished goods, pays Sales Tax at Customs | Cost. No further Sales Tax when resold (single-stage -- manufacturer/import level only). |

---

## Step 7: E-Invoicing Requirements [T2]

**Legislation:** Finance Act 2024; IRBM (LHDN) e-Invoice Guidelines (Version 4.1)

### Phased Implementation [T1]

| Phase | Effective Date | Threshold |
|-------|---------------|-----------|
| Phase 1 | 1 August 2024 | Annual turnover exceeding RM 100,000,000 |
| Phase 2 | 1 January 2025 | Annual turnover exceeding RM 25,000,000 |
| Phase 3 | 1 July 2025 | All taxpayers (no threshold) |

### E-Invoice Scope [T2]

- E-invoicing is administered by IRBM (Lembaga Hasil Dalam Negeri / Inland Revenue Board), NOT RMCD
- Covers ALL commercial transactions (not limited to SST-taxable transactions)
- Includes: invoices, credit notes, debit notes, refund notes, self-billed invoices
- Must be validated through IRBM's MyInvois system before issuance to buyer

### E-Invoice Mandatory Fields [T1]

1. Supplier name, TIN, BRN/SST registration number
2. Buyer name, TIN, BRN/SST registration number (or MyKad/passport for individuals)
3. Invoice date, unique e-invoice reference number
4. Description of goods/services, quantity, unit price
5. Tax type and amount (Sales Tax, Service Tax, or exempt)
6. Total amount payable
7. Validation by MyInvois (IRBM validation code/QR code)

**Note:** E-invoicing is an IRBM (income tax authority) initiative, separate from RMCD (SST authority). However, e-invoice data feeds into both income tax and SST compliance.

---

## Step 8: Filing Deadlines and Penalties [T1]

**Legislation:** Sales Tax Act 2018, Sections 26, 76-82; Service Tax Act 2018, Sections 26, 62-68

### Filing Deadlines [T1]

| Obligation | Deadline | Notes |
|------------|----------|-------|
| SST-02 return filing | Last day of the month following the taxable period | Bimonthly periods: Jan-Feb, Mar-Apr, May-Jun, Jul-Aug, Sep-Oct, Nov-Dec |
| SST-02 payment | Same as filing deadline | Payment must accompany the return |
| SST-02A (imported services) | Within 30 days of payment or invoice, whichever earlier | Per transaction |
| SST return via MySST | Mandatory electronic filing via mysst.customs.gov.my | Paper filing not accepted |

### Penalties [T1]

| Offence | Penalty | Legislation |
|---------|---------|-------------|
| Late filing of return | Fine: RM 0 -- RM 50,000, or imprisonment up to 3 years, or both | Sales Tax Act s.26(5); Service Tax Act s.26(5) |
| Late payment (RMCD practice) | Penalty: 10% of tax unpaid at first 30 days; additional 15% if unpaid after 60 days; additional 15% after 90 days (total potential 40%) | Sales Tax Act s.26A; Service Tax Act s.26A |
| Failure to register | Fine: RM 0 -- RM 30,000, or imprisonment up to 2 years, or both | Sales Tax Act s.12(5); Service Tax Act s.12(5) |
| Evasion / fraud | Fine: 10-20x tax amount, or imprisonment up to 5 years, or both | Sales Tax Act s.85; Service Tax Act s.71 |
| Failure to issue proper invoice | Fine: RM 0 -- RM 30,000, or imprisonment up to 2 years | Various sections |
| Incorrect return (voluntary correction) | Reduced penalty if disclosed voluntarily before audit | RMCD administrative practice |

### Late Payment Penalty Escalation [T1]

```
Days late 1-30:   10% of unpaid tax
Days late 31-60:  additional 15% of unpaid tax (cumulative 25%)
Days late 61-90:  additional 15% of unpaid tax (cumulative 40%)
Beyond 90 days:   legal proceedings + penalty capped at 40%
```

---

## Step 9: Credit Notes and Adjustments [T1]

**Legislation:** Sales Tax Act 2018, Section 35; Service Tax Act 2018, Section 35

### Credit Note Treatment [T1]

- If goods are returned or consideration is reduced after Sales Tax/Service Tax has been charged, a credit note may be issued
- The registered person may deduct the excess tax from the next SST-02 return (Part C adjustments)
- Credit note must reference the original invoice number and date
- Must be issued within 6 years of the original taxable event

### Bad Debt Relief [T2]

**Legislation:** Sales Tax Act 2018, Section 36; Service Tax Act 2018, Section 36

- If a customer fails to pay and the debt is written off as bad:
  - Relief available for the SST portion of the debt
  - Debt must be outstanding for at least 6 months
  - Must be written off in the accounts
  - Claim via Part C3 of SST-02
  - If the debt is subsequently recovered, the SST must be repaid
- [T2] flag for tax agent to confirm eligibility before claiming

---

## Step 10: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| Sales Tax registration (manufacturer) | RM 500,000 taxable turnover in 12 months | Sales Tax Act s.12 |
| Service Tax registration (general) | RM 500,000 taxable turnover in 12 months | Service Tax Act s.12 |
| Service Tax registration (F&B) | RM 1,500,000 taxable turnover in 12 months | Service Tax Act s.12 |
| E-invoicing Phase 1 | RM 100,000,000 annual turnover | IRBM directive |
| E-invoicing Phase 2 | RM 25,000,000 annual turnover | IRBM directive |
| E-invoicing Phase 3 | All taxpayers | IRBM directive |
| Foreign digital services registration | RM 500,000 annual value of digital services to Malaysian consumers | Service Tax Act s.56C |

---

## Step 11: Edge Case Registry

### EC1 -- Manufacturer sells goods locally AND exports [T1]

**Situation:** Registered manufacturer sells 60% domestically and exports 40%.
**Resolution:** Domestic sales: charge Sales Tax at 10% (or 5%). Export sales: exempt from Sales Tax under Sales Tax (Goods Exempted from Tax) Order -- exported goods. Report domestic in SST-02 Part A1/A3. Report exports in Part A7 (exempt). All Schedule A/B exemptions on inputs still apply to the full manufacturing operation.
**Legislation:** Sales Tax Act 2018, Section 34; Sales Tax (Goods Exempted from Tax) Order 2018.

### EC2 -- Service provider below RM 500K threshold provides services to foreign client [T1]

**Situation:** Small accounting firm with RM 400K turnover provides advisory to a Singapore company.
**Resolution:** Below threshold -- not registered for Service Tax. No obligation to charge Service Tax. The service is not taxable. If turnover subsequently exceeds RM 500K (including foreign client revenue), must register within 30 days.
**Legislation:** Service Tax Act 2018, Section 12.

### EC3 -- Company receives cloud computing services from US provider (imported services) [T1]

**Situation:** Malaysian company subscribes to AWS/Azure. No SST on invoice.
**Resolution:** Imported taxable service under Group A (IT services). Self-account at 8% (or 6% if classified under retained-rate category) via SST-02A. Pay within 30 days. This is a COST -- no input credit. Applies to all persons in Malaysia, whether or not SST-registered.
**Legislation:** Service Tax Act 2018, Section 26; First Schedule Group A.

### EC4 -- Retailer imports finished goods for resale [T1]

**Situation:** Retailer imports consumer electronics from China. Customs value RM 200,000.
**Resolution:** Sales Tax collected by Customs at import at 10% = RM 20,000. This is a COST to the retailer. When the retailer sells to consumers, NO Sales Tax is charged (retailer is not a manufacturer). The RM 20,000 becomes part of cost of goods.
**Legislation:** Sales Tax Act 2018, Section 13 (tax on import).

### EC5 -- Manufacturer subcontracts part of the manufacturing process [T2]

**Situation:** Registered manufacturer sends semi-finished goods to subcontractor for processing, then receives finished goods back.
**Resolution:** The subcontractor's processing service may or may not be "manufacturing" under Section 2. If the subcontractor is deemed a manufacturer, they must register and charge Sales Tax on the processed goods. If merely providing a service, Service Tax may apply instead. Flag for tax agent: determine whether the subcontractor's activity constitutes manufacturing or a service.
**Legislation:** Sales Tax Act 2018, Section 2 (definition of manufacture); Section 5 (deemed manufacture).

### EC6 -- Mixed supply: goods + services in one transaction [T2]

**Situation:** Company sells IT equipment (goods) with installation and maintenance (services) in a bundled contract.
**Resolution:** If the goods and services can be separated, apply Sales Tax to the goods component and Service Tax to the services component. If they cannot be separated (composite supply), determine the principal supply: if predominantly goods, treat as Sales Tax; if predominantly services, treat as Service Tax. Flag for tax agent: confirm whether the supply is severable and which is the principal component.
**Legislation:** RMCD Industry Guides; administrative practice.

### EC7 -- Transitional credit from old GST period [T1]

**Situation:** Company had GST input credits when GST was abolished on 1 September 2018.
**Resolution:** GST transitional period has ended. Unclaimed GST input credits from the GST era must have been claimed via the transitional provisions (GST (Repeal) Act 2014). As of 2024, no new claims from the GST era can be made unless under special RMCD approval. Treat as expired.
**Legislation:** Goods and Services Tax (Repeal) Act 2014.

### EC8 -- Digital services by foreign provider directly to Malaysian consumer [T1]

**Situation:** Netflix/Spotify provides streaming to Malaysian consumers, charges RM 49.90/month.
**Resolution:** Foreign digital service provider should be registered under Section 56C of Service Tax Act if turnover exceeds RM 500K. If registered, the provider collects and remits 8% Service Tax. If NOT registered but should be, RMCD enforcement applies. Malaysian consumers cannot self-account (self-accounting is for B2B only under Section 26).
**Legislation:** Service Tax Act 2018, Section 56C; Service Tax (Digital Service) Regulations 2020.

### EC9 -- Sale of exempt goods by a registered manufacturer [T1]

**Situation:** Registered manufacturer also produces exempt goods (e.g., basic foodstuffs like rice processing).
**Resolution:** No Sales Tax on exempt goods. Only taxable goods attract Sales Tax. Report exempt goods value in SST-02 Part A7. Schedule A/B exemptions apply only to inputs for taxable goods production. If inputs are shared between taxable and exempt production, [T2] flag for tax agent to confirm allocation.
**Legislation:** Sales Tax Act 2018, Section 8; Sales Tax (Goods Exempted from Tax) Order 2018.

### EC10 -- Professional services firm provides both taxable and non-taxable services [T2]

**Situation:** Law firm provides legal advisory (taxable under Group C) and also acts as nominee shareholder (potentially non-prescribed service).
**Resolution:** Service Tax applies only to prescribed taxable services listed in the First Schedule. Non-prescribed services are not subject to Service Tax. Must separate turnover: only prescribed service turnover counts toward the RM 500K registration threshold. Flag for tax agent: confirm which specific services are prescribed under the current First Schedule.
**Legislation:** Service Tax Act 2018, Section 12; First Schedule.

---

## Step 12: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Licensed Malaysian tax agent must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed Malaysian tax agent. Document gap.
```

---

## Step 13: Test Suite

### Test 1 -- Standard manufacturer domestic sale at 10%

**Input:** Registered manufacturer sells furniture to Malaysian retailer. Selling price RM 80,000.
**Expected output:** SST-02 Part A1 = RM 80,000. Part A2 (Sales Tax) = RM 8,000. Invoice shows RM 88,000 total.

### Test 2 -- Manufacturer export sale, exempt

**Input:** Registered manufacturer exports textiles to Australia. FOB value RM 500,000.
**Expected output:** SST-02 Part A7 = RM 500,000 (exempt). Part A2 = RM 0. No Sales Tax on export.

### Test 3 -- Professional service at 8%

**Input:** Registered accounting firm provides audit services. Fee RM 30,000.
**Expected output:** SST-02 Part B1 = RM 30,000. Part B2 (Service Tax) = RM 2,400. Invoice shows RM 32,400 total. (Group C prescribed service.)

### Test 4 -- Restaurant service at retained 6%

**Input:** Registered restaurant (turnover > RM 1.5M). Food and beverage sale RM 500.
**Expected output:** SST-02 Part B3 = RM 500. Part B4 (Service Tax at 6%) = RM 30. Invoice shows RM 530 total.

### Test 5 -- Imported cloud service (self-account)

**Input:** Malaysian company subscribes to Salesforce CRM. Monthly fee USD 500 (~RM 2,350). No SST on invoice.
**Expected output:** File SST-02A. Service Tax at 8% = RM 188. Pay within 30 days. No input credit -- RM 188 is a cost to the company.

### Test 6 -- Importer of finished goods (retail)

**Input:** Retailer imports electronics from China. Customs value RM 100,000. Sales Tax at import = 10%.
**Expected output:** Sales Tax paid at Customs = RM 10,000 (cost). When retailer sells to consumers, NO Sales Tax charged. Total cost of goods = RM 110,000 (including tax).

### Test 7 -- Manufacturer with Schedule A exemption on raw materials

**Input:** Registered furniture manufacturer purchases timber (raw material) RM 200,000 from local supplier. Schedule A exemption approved.
**Expected output:** No Sales Tax on timber purchase (exempt under Schedule A). Manufacturer charges Sales Tax on finished furniture sold. SST-02 Part A8 = RM 200,000.

### Test 8 -- Below-threshold service provider

**Input:** Freelance graphic designer, annual turnover RM 300,000. Provides design services.
**Expected output:** Below RM 500,000 threshold. Not required to register for Service Tax. No SST charged on invoices. No SST-02 filing obligation.

### Test 9 -- Credit note on returned goods

**Input:** Manufacturer issues credit note for RM 5,000 returned goods (original Sales Tax RM 500).
**Expected output:** Deduct RM 500 from Part C4 (adjustments) of next SST-02. Net SST payable reduced by RM 500.

### Test 10 -- Mixed goods and services supply

**Input:** IT company sells RM 50,000 hardware (goods) and RM 20,000 installation service (services) to a client. Separately invoiced.
**Expected output:** Sales Tax on hardware: RM 50,000 * 10% = RM 5,000 (Part A1/A2 if manufacturer). Service Tax on installation: RM 20,000 * 8% = RM 1,600 (Part B1/B2). Total SST = RM 6,600. [T2] if not separately invoiced -- flag for tax agent.

---

## PROHIBITIONS [T1]

- NEVER let AI guess SST classification -- Sales Tax vs. Service Tax vs. exempt is deterministic from facts
- NEVER apply input tax credit under SST -- there is NO input credit mechanism (this is NOT a VAT system)
- NEVER confuse SST with the abolished GST (GST was replaced by SST on 1 September 2018)
- NEVER charge Sales Tax at the retail/wholesale level -- Sales Tax applies only at the manufacturer/import stage
- NEVER apply Service Tax to services not listed in the First Schedule of Service Tax Regulations -- only prescribed taxable services are subject
- NEVER apply the 8% Service Tax rate to services that retain the 6% rate (F&B, telecoms, parking, logistics)
- NEVER omit the self-account obligation for imported services -- it applies to ALL persons in Malaysia, not just SST-registered persons
- NEVER assume e-invoicing exemption -- check the client's turnover against the phased implementation thresholds
- NEVER treat Sales Tax paid on imports as creditable -- it is a cost to the importer
- NEVER combine Sales Tax and Service Tax registration thresholds -- they are separate registrations with separate thresholds
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Contribution Notes

This skill requires validation by a licensed Malaysian tax agent (Ejen Cukai Berlesen) before production use. All T1 rules are based on the Sales Tax Act 2018, Service Tax Act 2018, and RMCD guidance current as of early 2026, including the major SST scope expansion effective 1 July 2025.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
