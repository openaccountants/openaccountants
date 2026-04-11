---
name: texas-sales-tax
description: Use this skill whenever asked about Texas sales and use tax, Comptroller filings, Texas tax permits, Texas exemptions, Texas nexus, or any request involving Texas state sales and use tax compliance. Trigger on phrases like "Texas sales tax", "TX sales tax", "Comptroller", "Texas use tax", "Texas franchise tax", "Texas sales tax return", "Texas exemption certificate", or any request involving Texas sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any Texas sales tax work.
---

# Texas Sales and Use Tax Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Texas, United States |
| Jurisdiction Code | US-TX |
| Tax Type | Sales and Use Tax (state + local) |
| Primary Legislation | Texas Tax Code, Chapter 151 (Limited Sales, Excise, and Use Tax) |
| Key Statutes | Tex. Tax Code Sections 151.001-151.830 |
| Tax Authority | Texas Comptroller of Public Accounts |
| Filing Portal | https://comptroller.texas.gov/taxes/sales/ |
| Federal Framework Skill | us-sales-tax (read first for Wayfair, nexus overview, and multi-state context) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires Texas CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate structure, basic taxability, filing mechanics, nexus thresholds. Tier 2: service taxability, mixed transactions, manufacturing exemptions. Tier 3: audit defense, complex bundled transactions, Comptroller rulings. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to a licensed tax professional and document the gap.

---

## Step 0: Client Onboarding Questions

Before performing any Texas sales tax work, collect the following from the client:

| # | Question | Why It Matters |
|---|----------|----------------|
| 1 | What is your Texas Sales and Use Tax Permit number (taxpayer number)? | Required for filing; confirms registration with Comptroller. [T1] |
| 2 | What is your assigned filing frequency (monthly, quarterly, annual)? | Determines return due dates. [T1] |
| 3 | What type of nexus do you have in Texas (physical, economic, both)? | Economic nexus threshold is $500,000 in taxable sales (revenue only, no transaction count). [T1] |
| 4 | Do you sell through any marketplace facilitators (Amazon, eBay, Etsy, etc.)? | Marketplace facilitators collect tax on facilitated sales; seller must still collect on direct sales. [T1] |
| 5 | What is your primary business location in Texas? | Texas is origin-based for intrastate sales; seller's location rate applies. [T1] |
| 6 | Do you sell services? If so, which types? | Texas taxes only specifically enumerated services. [T1] |
| 7 | Do you sell SaaS or data processing services? | 20% exemption on data processing services (only 80% of charge taxable). [T1] |
| 8 | Do you have franchise tax obligations? | Texas franchise tax is separate from sales tax -- escalate to [T3] if needed. [T3] |

---

## Step 1: Tax Rate Structure [T1]

### 1.1 State Rate

The Texas state sales and use tax rate is **6.25%**. [T1]

**Legislation:** Tex. Tax Code Section 151.051.

### 1.2 Local Tax Rates [T1]

| Jurisdiction Type | Maximum Rate | Authority |
|-------------------|-------------|-----------|
| City | 2.00% | Tex. Tax Code Section 321.101 |
| County | 0.50% | Tex. Tax Code Section 323.101 |
| Transit authority | 1.00% | Tex. Transp. Code Section 451.401 |
| Special purpose district | Varies | Various statutes |
| **Combined maximum** | **8.25%** (state 6.25% + local 2.00% cap) | Tex. Tax Code Section 141.007 |

### 1.3 Sourcing Rules [T1]

| Scenario | Rate Applied |
|----------|-------------|
| Intrastate sales (seller and buyer both in TX) | Rate at seller's location (origin-based) [T1] |
| Remote (out-of-state) sellers | Rate at buyer's ship-to address (destination-based) [T1] |

**Legislation:** Tex. Tax Code Section 321.203.

---

## Step 2: Transaction Classification Rules [T1/T2]

### 2.1 Tangible Personal Property (TPP) [T1]

All sales of TPP are taxable unless specifically exempted. Tex. Tax Code Section 151.051. Includes: electronics, furniture, appliances, equipment, vehicles (separate motor vehicle tax), clothing and footwear (**NO clothing exemption** except during Sales Tax Holiday), building materials, jewelry, sporting goods, office supplies. [T1]

### 2.2 Taxable Services [T1]

| Taxable Service | Statute |
|----------------|---------|
| Amusement services | Sec. 151.0028 |
| Cable television services | Sec. 151.0033 |
| Credit reporting services | Sec. 151.0039 |
| Data processing services | Sec. 151.0035 |
| Debt collection services | Sec. 151.0039 |
| Information services | Sec. 151.0038 |
| Insurance services | Sec. 151.0039 |
| Internet access services | **EXEMPT** (federal ITFA) |
| Laundry/cleaning/garment services | Sec. 151.0045 |
| Motor vehicle parking/storage | Sec. 151.0048 |
| Nonresidential real property repair/remodeling | Sec. 151.0048 |
| Pest control services | Sec. 151.0048 |
| Personal property repair services | Sec. 151.0048 |
| Real property services (nonresidential) | Sec. 151.0048 |
| Security services | Sec. 151.0039 |
| Telecommunication services | Sec. 151.0103 |
| Waste/trash removal services | Sec. 151.0048 |

### 2.3 Nontaxable Services [T1]

Professional services (legal, accounting, consulting, medical, engineering, architecture), advertising services, construction labor on new residential real property, educational services, transportation/freight, janitorial/cleaning services (residential), personal care (hair, nails), landscaping (residential). [T1]

### 2.4 Food and Beverages [T1]

| Category | Taxable? | Citation |
|----------|----------|----------|
| Grocery food (for home consumption) | **EXEMPT** | Sec. 151.314 |
| Prepared food (heated, served with utensils) | **TAXABLE** | Sec. 151.314(c) |
| Soft drinks / candy | **TAXABLE** | Sec. 151.314(b) |
| Bakery items (unheated, sold without utensils) | **EXEMPT** | Sec. 151.314 |
| Dietary supplements | **EXEMPT** | Sec. 151.314 |
| Alcoholic beverages | **TAXABLE** | Sec. 151.314(b) |
| Water (bottled) | **EXEMPT** | Sec. 151.314 |
| Ice | **EXEMPT** | Sec. 151.314 |

### 2.5 SaaS and Digital Goods [T2]

| Product | Taxable? | Notes |
|---------|----------|-------|
| Canned software (physical media) | **TAXABLE** | TPP [T1] |
| Canned software (electronic download) | **TAXABLE** | Sec. 151.009 [T1] |
| Custom software | **TAXABLE** (if delivered electronically or on media) | Unlike many states, TX taxes custom software [T1] |
| SaaS (cloud-hosted) | **TAXABLE** (as data processing service) | Comptroller Rule 3.330 -- 20% exemption available [T1] |
| Data processing services | **TAXABLE** (with 20% exemption) | Only 80% of charge is taxable; Sec. 151.351 [T1] |
| Streaming services | **TAXABLE** (as amusement services) | [T1] |
| Digital books, music, movies (download) | **TAXABLE** | Treated as TPP [T1] |

**Important:** Texas uniquely provides a 20% exemption for data processing services -- only 80% of the charge is subject to tax. Tex. Tax Code Section 151.351. [T1]

### 2.6 Clothing [T1]

| Rule | Detail |
|------|--------|
| General rule | Clothing is fully taxable in Texas [T1] |
| Exception | Annual Sales Tax Holiday (typically last full weekend in August) [T1] |
| Holiday threshold | Clothing and footwear under $100/item are exempt during the holiday [T1] |
| Authority | Tex. Tax Code Section 151.326 |

---

## Step 3: Return Form Structure [T1]

### 3.1 Filing Forms

| Form | Name | Use |
|------|------|-----|
| 01-114 | Texas Sales and Use Tax Return | Primary return [T1] |
| 01-117 | Texas Sales and Use Tax Return (Short Form) | Short form [T1] |
| 01-115 | Schedule A (Local Tax) | Local tax detail [T1] |
| 01-148 | Texas Use Tax Return | For purchasers [T1] |

### 3.2 Use Tax Reporting [T1]

| Rule | Detail |
|------|--------|
| When use tax applies | TPP/taxable services from out-of-state seller without TX tax; TPP purchased tax-free and diverted to taxable use; TPP brought into TX for use/storage/consumption [T1] |
| Use tax rate | Combined state and local rate at location of use [T1] |
| Credit for tax paid to other states | Credit allowed under Tex. Tax Code Section 151.303 [T1] |

---

## Step 4: Deductibility / Exemptions [T1/T2]

### 4.1 Common Exemptions

| Exemption | Statute | Notes | Tier |
|-----------|---------|-------|------|
| Grocery food | Sec. 151.314 | Unprepared food for home consumption | [T1] |
| Prescription drugs | Sec. 151.313 | Prescribed by practitioner | [T1] |
| OTC drugs and medicines | Sec. 151.313 | EXEMPT in Texas (unlike many states) | [T1] |
| Medical equipment (prescribed) | Sec. 151.313 | Prosthetics, corrective lenses, hearing aids | [T1] |
| Agricultural supplies | Sec. 151.316 | Feed, seed, fertilizer for agricultural use | [T1] |
| Farm/ranch machinery | Sec. 151.316 | Used exclusively on farm/ranch | [T1] |
| Manufacturing equipment | Sec. 151.318 | Used directly in manufacturing | [T1] |
| Resale | Sec. 151.302 | Goods purchased for resale | [T1] |
| Interstate commerce | Sec. 151.307 | Goods shipped out of state | [T1] |
| Federal government | Sec. 151.309 | Sales to US government | [T1] |
| Containers/packaging | Sec. 151.302(c) | Used to pack goods for sale | [T1] |
| Newspapers/periodicals | Sec. 151.320 | Qualifying publications | [T1] |

### 4.2 Manufacturing Exemption [T1]

| Parameter | Detail |
|-----------|--------|
| Scope | Broad exemption for machinery, equipment, and supplies [T1] |
| Qualification | Used or consumed directly in manufacturing, processing, fabrication, or repair of TPP for sale [T1] |
| Raw materials | Includes ingredients/components of manufactured product [T1] |
| Utilities | Gas/electricity used in manufacturing (only the portion directly consumed in the process) [T2] |
| Excludes | Office equipment, administrative equipment, distribution equipment [T1] |
| Certificate | Form 01-339 (Texas Sales and Use Tax Exemption Certificate) [T1] |
| Authority | Tex. Tax Code Section 151.318 |

### 4.3 Resale Exemption [T1]

| Parameter | Detail |
|-----------|--------|
| Form | 01-339 (Texas Sales and Use Tax Resale Certificate) [T1] |
| Requirements | Buyer's Texas taxpayer number, description of goods, resale statement [T1] |
| Multi-state accepted | Streamlined Sales Tax Certificate and MTC Uniform Sales Tax Certificate accepted [T1] |
| Expiration | Does not expire, but must be updated if buyer's status changes [T1] |

### 4.4 Nonprofit Exemptions [T2]

| Parameter | Detail |
|-----------|--------|
| Qualifying organizations | Religious, educational, and charitable organizations with Comptroller exemption letter [T2] |
| Certificate required | Texas sales tax exemption number issued by Comptroller [T1] |
| Not automatic | Each must apply and receive approval [T2] |
| Authority | Tex. Tax Code Section 151.310 |

### 4.5 Exemption Certificates [T1]

| Certificate | Form | Purpose |
|------------|------|---------|
| General exemption / Resale | 01-339 | Resale and other exemptions (check appropriate box) [T1] |
| Agricultural/Timber | 01-924 + Ag/Timber Number | Farm equipment, feed, seed, timber [T1] |

---

## Step 5: Key Thresholds [T1]

### 5.1 Economic Nexus Threshold [T1]

| Parameter | Value |
|-----------|-------|
| Revenue threshold | More than $500,000 in total revenue from taxable items in TX [T1] |
| Transaction count threshold | **None** -- revenue only [T1] |
| Measurement period | Preceding twelve calendar months [T1] |
| Effective date | October 1, 2019 [T1] |
| Sales included | Only taxable items; exempt sales do NOT count toward threshold [T1] |
| Authority | Tex. Tax Code Section 151.107; Comptroller Rule 3.286 |

**Note:** The $500,000 threshold is the highest among US states (tied with California). [T1]

### 5.2 Registration Requirements [T1]

| Requirement | Detail |
|------------|--------|
| Who must register | Any person engaged in business in TX as a seller of taxable TPP or services (Sec. 151.203) [T1] |
| Registration type | Texas Sales and Use Tax Permit [T1] |

### 5.3 Marketplace Facilitator Rules [T1]

| Rule | Detail |
|------|--------|
| Effective date | October 1, 2019 [T1] |
| Obligation | Marketplace facilitators with TX nexus must collect on behalf of marketplace sellers [T1] |
| Seller relief | Sellers relieved of collection obligation for marketplace sales [T1] |
| Direct sales | Marketplace sellers must still collect on direct (non-marketplace) sales [T1] |
| Authority | Tex. Tax Code Section 151.0242; Comptroller Rule 3.286 |

### 5.4 No State Income Tax [T1]

Texas has no state personal income tax and no state corporate income tax. Texas does impose a franchise tax (margin tax) on business entities, but this is separate from sales tax and outside the scope of this skill. [T3]

---

## Step 6: Filing Deadlines and Penalties [T1]

### 6.1 Filing Frequency

| Frequency | Criteria | Due Date |
|-----------|----------|----------|
| Monthly | State and local tax due > $1,500/quarter or > $500/month | 20th of the following month [T1] |
| Quarterly | State and local tax due $500-$1,500/quarter | 20th of the month following the quarter [T1] |
| Annual | State and local tax due < $1,000/year | January 20 of the following year [T1] |

### 6.2 Quarterly Due Dates [T1]

| Quarter | Period | Due Date |
|---------|--------|----------|
| Q1 | January 1 -- March 31 | April 20 |
| Q2 | April 1 -- June 30 | July 20 |
| Q3 | July 1 -- September 30 | October 20 |
| Q4 | October 1 -- December 31 | January 20 |

**Legislation:** Tex. Tax Code Section 151.401.

### 6.3 Electronic Filing [T1]

| Rule | Detail |
|------|--------|
| Mandatory e-filing | Taxpayers who paid $50,000+ in state tax in preceding fiscal year (Sec. 151.401) [T1] |
| All others | May file electronically or on paper [T1] |
| Platform | Comptroller's WebFile system [T1] |

### 6.4 Timely Filing Discount (Vendor Discount) [T1]

| Parameter | Value |
|-----------|-------|
| Rate | 0.5% of tax due (for amounts up to $1.25 million/month) [T1] |
| Maximum | $1,750/month for timely filers [T1] |
| Authority | Tex. Tax Code Section 151.423 |

### 6.5 Penalties and Interest [T1]

| Penalty | Rate | Citation |
|---------|------|----------|
| Late filing (1-30 days) | 5% of tax due | Sec. 151.703 [T1] |
| Late filing (> 30 days) | 10% of tax due | Sec. 151.703 [T1] |
| Interest on underpayment | Prime rate + additional percentage | Sec. 111.060 [T1] |
| Fraud | 50% of deficiency | Sec. 151.703(d) [T1] |

### 6.6 Record Retention [T1]

| Parameter | Value |
|-----------|-------|
| Retention period | Minimum 4 years from the date the return was filed or due, whichever is later [T1] |
| Authority | Tex. Tax Code Section 111.0041 |
| Records required | Sales invoices/receipts, purchase invoices, exemption certificates (Form 01-339), bank statements, inventory records, shipping/delivery records, electronic records (POS, e-commerce) [T1] |

### 6.7 Statute of Limitations [T1]

| Scenario | Limitation Period |
|----------|------------------|
| Standard assessment | 4 years from filing date or due date [T1] |
| No return filed | No limitation (unlimited) [T1] |
| Fraud | No limitation (unlimited) [T1] |
| 25% or more understatement | 6 years [T1] |

### 6.8 Audit Considerations [T2]

| Factor | Detail |
|--------|--------|
| Lookback period | Typically 4 years [T1] |
| Sampling methods | May be used for large-volume retailers [T2] |
| Appeals | Administrative process through Comptroller, then district court [T2] |
| Most common adjustment | Missing exemption certificates [T1] |

---

## Step 7: Texas-Specific Rules [T1/T2]

### 7.1 Industry-Specific Rules

#### Construction Industry [T2]

| Rule | Detail |
|------|--------|
| Lump-sum contractors | Consumers of materials; pay sales tax on material purchases [T1] |
| Separated contract contractors | May pass through materials tax to property owner [T2] |
| Residential construction labor | Generally exempt [T1] |
| Nonresidential construction labor | Taxable as real property service [T1] |

#### Oil and Gas Industry [T2]

| Rule | Detail |
|------|--------|
| Drilling equipment | May qualify for manufacturing exemption (Sec. 151.318) [T2] |
| Chemicals/materials | May qualify for exemption if consumed in production [T2] |
| Well servicing/fracturing | May be taxable [T2] |
| Guidance | Highly specialized -- flag for reviewer [T2] |

#### Technology Companies [T1]

| Product/Service | Taxable? | Tier |
|----------------|----------|------|
| Hardware sales | Fully taxable as TPP | [T1] |
| Custom software | Taxable (unusual for TX) | [T1] |
| SaaS/data processing | 80% of charge taxable (20% exempt) | [T1] |
| IT consulting/professional services | NOT taxable | [T1] |
| Web hosting | May be taxable as data processing | [T2] |
| Internet access | Exempt (federal ITFA) | [T1] |

### 7.2 Detailed Taxability Matrix [T1]

| Category | Taxable? | Rate | Key Statute |
|----------|----------|------|-------------|
| General TPP | Yes | 6.25% + local | Sec. 151.051 |
| Grocery food (unprepared) | No | Exempt | Sec. 151.314 |
| Prepared food (hot, dine-in) | Yes | 6.25% + local | Sec. 151.314(c) |
| Candy and soft drinks | Yes | 6.25% + local | Sec. 151.314(b) |
| Prescription medicine | No | Exempt | Sec. 151.313 |
| OTC medicine | No | Exempt | Sec. 151.313 |
| Clothing (general) | Yes | 6.25% + local | No exemption |
| Clothing (during holiday) | No | Exempt (under $100) | Sec. 151.326 |
| Canned software (any delivery) | Yes | 6.25% + local | Sec. 151.009 |
| Custom software | Yes | 6.25% + local | Unlike most states |
| SaaS / Data processing | Yes (80% taxable) | 6.25% + local on 80% | Sec. 151.351 |
| Manufacturing equipment | No | Exempt | Sec. 151.318 |
| Farm/ranch equipment | No | Exempt | Sec. 151.316 |
| Resale purchases | No | Exempt | Sec. 151.302 |
| Interstate shipments | No | Exempt | Sec. 151.307 |
| Telecom services | Yes | 6.25% + local | Sec. 151.0103 |
| Data processing services | Yes (80%) | 20% exempt | Sec. 151.351 |
| Amusement services | Yes | 6.25% + local | Sec. 151.0028 |
| Real property repair (nonresidential) | Yes | 6.25% + local | Sec. 151.0048 |
| Real property repair (residential) | No | Exempt | Sec. 151.0048 |
| Professional services | No | Exempt | Not enumerated |
| Motor vehicles | Yes (separate admin) | 6.25% | Sec. 152.021 (TxDMV) |

---

## PROHIBITIONS [T1]

- **NEVER** apply a general clothing exemption outside of the Sales Tax Holiday period -- clothing is normally fully taxable in Texas. [T1]
- **NEVER** assume all services are taxable -- Texas taxes only specifically enumerated services. [T1]
- **NEVER** forget the 20% data processing services exemption when computing tax on SaaS/data processing. [T1]
- **NEVER** confuse motor vehicle sales tax (TxDMV) with general sales tax (Comptroller). [T1]
- **NEVER** apply destination-based sourcing for intrastate Texas sales -- Texas is origin-based for intrastate. [T1]
- **NEVER** assume nonprofits are automatically exempt -- they must have a Comptroller-issued exemption number. [T1]
- **NEVER** include exempt sales in the economic nexus threshold calculation (Texas counts only taxable sales). [T1]
- **NEVER** ignore the franchise tax when advising on overall Texas tax obligations -- flag as [T3] and escalate. [T1]
- **NEVER** treat residential and nonresidential real property services the same -- different taxability rules apply. [T1]
- **NEVER** file without claiming the timely filing discount if the return and payment are on time. [T1]

---

## Edge Case Registry [T1/T2]

### EC1 -- Motor Vehicle Sales Tax [T1]

**Situation:** A dealer sells a motor vehicle in Texas.

**Resolution:** Motor vehicles are subject to motor vehicle sales tax, NOT the standard sales tax. The motor vehicle rate is 6.25% (same rate as standard sales tax), but it is administered by the Texas Department of Motor Vehicles (TxDMV), not the Comptroller. Reported separately. Tex. Tax Code Section 152.021.

### EC2 -- Data Processing Services -- 20% Exemption [T1]

**Situation:** A business purchases data processing services (including SaaS) for $1,000/month.

**Resolution:** Under Tex. Tax Code Section 151.351, data processing services receive a 20% exemption. Only 80% of the charge ($800) is subject to tax. At 8.25% combined rate: tax = $66.00 (not $82.50). This exemption applies automatically.

### EC3 -- Residential vs. Nonresidential Real Property Services [T1]

**Situation:** A cleaning company provides janitorial services.

**Resolution:** Janitorial services for nonresidential (commercial) real property are TAXABLE. Janitorial services for residential real property are EXEMPT. The classification depends on the property type, not the customer type. Tex. Tax Code Section 151.0048.

### EC4 -- No Income Tax but Franchise Tax [T1]

**Situation:** A business asks about overall Texas tax obligations.

**Resolution:** Texas has no personal income tax or corporate income tax. However, most business entities are subject to the Texas franchise tax (a gross margin tax). The franchise tax is entirely separate from sales tax and is outside the scope of this skill. Escalate franchise tax questions to [T3].

### EC5 -- Sales Tax Holiday [T1]

**Situation:** A retailer asks about the annual sales tax holiday.

**Resolution:** Texas holds an annual sales tax holiday (typically last full weekend in August). During this period, qualifying items are exempt: clothing and footwear under $100/item, school supplies under $100/item, and most backpacks under $100. Energy Star products and emergency preparation supplies also have separate holidays. Tex. Tax Code Section 151.326.

### EC6 -- Oil and Gas Equipment [T2]

**Situation:** An oil company purchases drilling equipment.

**Resolution:** Equipment used directly in oil and gas exploration and production may qualify for the manufacturing exemption under Tex. Tax Code Section 151.318. However, the application to oil field equipment is complex and depends on the specific use. Flag for reviewer.

### EC7 -- Voluntary Disclosure Agreements [T2]

**Situation:** An out-of-state seller discovers it should have been collecting Texas sales tax for the past three years.

**Resolution:** Texas offers a Voluntary Disclosure Agreement (VDA) program through the Comptroller. Benefits typically include waiver of penalties and limitation of the lookback period (typically 4 years). Flag for reviewer -- specific terms are negotiated case by case.

### EC8 -- Drop Shipments [T2]

**Situation:** An out-of-state retailer directs a Texas manufacturer to ship goods directly to a Texas customer.

**Resolution:** The Texas manufacturer is making a sale in Texas and must collect tax unless the out-of-state retailer provides a valid resale certificate. If the retailer is not registered in Texas, the manufacturer should collect tax on the retail price or obtain an exemption certificate from the retailer. Complex area -- flag for reviewer.

**Legislation:** Comptroller Rule 3.286; Tex. Tax Code Section 151.302.

### EC9 -- Mixed Transactions (Bundled TPP + Service) [T2]

**Situation:** A vendor sells a bundled package that includes both taxable TPP and nontaxable services for a single price.

**Resolution:** If the charges are separately stated, each component is taxed according to its own rules. If bundled as a single price, the entire transaction may be treated as a sale of TPP (taxable) unless the nontaxable service component is the "real object" of the transaction. Flag for reviewer -- requires analysis of the true object test.

---

## Test Suite

### Test 1 -- Basic Taxable Sale in Houston [T1]

**Input:** Retailer in Houston sells a TV for $800. Combined rate: 8.25%.
**Expected output:** Sales tax = $66.00. Total = $866.00.

### Test 2 -- Grocery Food Exemption [T1]

**Input:** Grocery store sells $150 of unprepared food (bread, eggs, meat) to a consumer.
**Expected output:** Sales tax = $0. Grocery food exempt under Sec. 151.314.

### Test 3 -- Data Processing Service with 20% Exemption [T1]

**Input:** Business purchases $2,000/month of SaaS data processing services. Combined rate: 8.25%.
**Expected output:** Taxable amount = $1,600 (80% of $2,000). Tax = $132.00. 20% exemption saves $33.00.

### Test 4 -- Out-of-State Seller Nexus [T1]

**Input:** A New York-based e-commerce seller has $550,000 in Texas sales in the past 12 months. No physical presence in TX.
**Expected output:** Exceeds $500,000 economic nexus threshold. Must register with Comptroller, collect TX sales tax, and file returns.

### Test 5 -- OTC Medicine Exemption [T1]

**Input:** Customer purchases $30 of over-the-counter cold medicine from a Texas pharmacy.
**Expected output:** Sales tax = $0. OTC medicine is exempt in Texas under Sec. 151.313.

### Test 6 -- Nonresidential Cleaning Service [T1]

**Input:** Cleaning company charges $500 for monthly janitorial service at a commercial office building. Rate: 8.25%.
**Expected output:** Sales tax = $41.25. Nonresidential real property services are taxable.

### Test 7 -- Residential Cleaning Service [T1]

**Input:** Same cleaning company charges $200 for cleaning a private residence.
**Expected output:** Sales tax = $0. Residential real property cleaning services are exempt.

### Test 8 -- Manufacturing Exemption [T1]

**Input:** Manufacturer purchases a $50,000 production machine used directly in manufacturing. Provides Form 01-339 with manufacturing exemption checked.
**Expected output:** Sales tax = $0. Manufacturing equipment directly used in production is exempt under Sec. 151.318.

### Test 9 -- Vendor Discount [T1]

**Input:** Retailer timely files and pays $10,000 in sales tax for the month.
**Expected output:** Vendor discount = $50.00 (0.5% of $10,000). Net remittance = $9,950.00.

### Test 10 -- Sales Tax Holiday [T1]

**Input:** Customer purchases a $75 pair of jeans during the August Sales Tax Holiday weekend.
**Expected output:** Sales tax = $0. Clothing under $100/item is exempt during the holiday. Tex. Tax Code Section 151.326.

---

## Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Licensed CPA, EA, or tax attorney must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed tax professional. Document gap.
```

---

## Contribution Notes

| Resource | URL / Contact |
|----------|---------------|
| Comptroller Main | https://comptroller.texas.gov |
| WebFile (Online Filing) | https://comptroller.texas.gov/taxes/file-pay/ |
| Rate Lookup | https://mycpa.cpa.state.tx.us/atj/atj.jsp |
| Phone | 1-800-252-5555 |
| Permit Application | Online via Comptroller website |
| Tax Publications | https://comptroller.texas.gov/taxes/publications/ |
| Comptroller Rules (TAC Title 34) | https://comptroller.texas.gov/about/policies-rules.php |
| Audit Procedures | https://comptroller.texas.gov/taxes/audit/ |

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
