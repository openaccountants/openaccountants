---
name: california-sales-tax
description: Use this skill whenever asked about California sales and use tax, CDTFA filings, California sales tax returns, district taxes, California exemptions, California nexus, or any request involving California state sales and use tax compliance. Trigger on phrases like "California sales tax", "CA sales tax", "CDTFA", "district tax", "California use tax", "CDTFA-401", "California exemption certificate", "California resale certificate", or any request involving California sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any California sales tax work.
---

# California Sales and Use Tax Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | California, United States |
| Jurisdiction Code | US-CA |
| Tax Type | Sales and Use Tax + District Taxes |
| Primary Legislation | California Revenue and Taxation Code (R&TC), Division 2, Part 1 (Sales and Use Taxes) |
| Key Statutes | R&TC Sections 6001-7176 (Sales Tax); R&TC Sections 6201-6432 (Use Tax); R&TC Sections 7251-7279.6 (Transactions/Use Tax -- District Taxes) |
| Tax Authority | California Department of Tax and Fee Administration (CDTFA) |
| Filing Portal | https://onlineservices.cdtfa.ca.gov |
| Federal Framework Skill | us-sales-tax (read first for Wayfair, nexus overview, and multi-state context) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires California CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate structure, basic taxability, filing mechanics, nexus thresholds. Tier 2: SaaS/digital goods classification, mixed transactions, partial exemptions. Tier 3: audit defense, complex bundled transactions, custom rulings. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to a licensed tax professional and document the gap.

---

## Step 0: Client Onboarding Questions

Before performing any California sales tax work, collect the following from the client:

| # | Question | Why It Matters |
|---|----------|----------------|
| 1 | What is your California Seller's Permit number? | Required for filing; confirms registration with CDTFA. [T1] |
| 2 | What is your assigned filing frequency (monthly, quarterly, annual)? | Determines return due dates and prepayment requirements. [T1] |
| 3 | What type of nexus do you have in California (physical, economic, both)? | Physical nexus (inventory, employees, property) vs. economic nexus ($500K threshold) affects registration obligations. [T1] |
| 4 | Do you sell through any marketplace facilitators (Amazon, eBay, Etsy, etc.)? | Marketplace facilitators collect tax on facilitated sales; seller must still report but not remit on those transactions. [T1] |
| 5 | What is the primary business address / point of sale location? | Needed for district tax rate determination on counter sales. [T1] |
| 6 | Do you ship goods to California customers? If so, from where? | Destination-based sourcing applies; need ship-to addresses for rate lookup. [T1] |
| 7 | Do you sell food, software/SaaS, or manufacturing equipment? | These categories have special exemption or taxability rules requiring additional analysis. [T2] |
| 8 | Are you required to make prepayments (average monthly liability > $17,000)? | Prepayments due 24th of first and second month of each quarter. [T1] |

---

## Step 1: Tax Rate Structure [T1]

### 1.1 State Rate Components

| Component | Rate | Authority |
|-----------|------|-----------|
| State General Fund | 3.9375% | R&TC Section 6051 |
| State Fiscal Recovery Fund | 0.25% | R&TC Section 6051.3 |
| Local Revenue Fund (county) | 1.0625% | R&TC Section 6051.15 |
| Local Public Safety Fund | 0.50% | R&TC Section 6051.2 |
| County Transportation Fund | 0.25% | R&TC Section 6051.8 |
| State Education Protection Account | 0.25% | R&TC Section 6051.9 |
| State General Fund (Prop 30/55) | 1.0% | R&TC Section 6051.7 |
| **Total statewide minimum** | **7.25%** | |

### 1.2 District Taxes (Local Add-Ons) [T1]

| Parameter | Value |
|-----------|-------|
| District tax range | 0.10% -- 3.25% on top of 7.25% base |
| Combined maximum | ~10.25% -- 10.50% (parts of Los Angeles and other high-rate areas) |
| Active district jurisdictions | 300+ as of 2025 |
| Sourcing for district taxes | Destination-based (ship-to address) |
| Authority | R&TC Sections 7251-7279.6; R&TC Section 7261 (county); R&TC Section 7285.5 (city) |

### 1.3 Sourcing Rules [T1]

| Scenario | Rate Applied |
|----------|-------------|
| Shipped goods (intrastate) | Rate at delivery address (destination-based) [T1] |
| Counter sales (customer picks up) | Rate at seller's location [T1] |
| Shipped goods (interstate, into CA) | Rate at CA delivery address [T1] |
| Shipped goods (out of CA) | No CA tax (interstate commerce) [T1] |

**Note:** California uses destination-based sourcing for intrastate sales. This differs from some states that use origin-based sourcing for intrastate sales. [T1]

**CDTFA rate lookup:** https://www.cdtfa.ca.gov/taxes-and-fees/rates.aspx

---

## Step 2: Transaction Classification Rules [T1/T2]

### 2.1 Tangible Personal Property (TPP) [T1]

All sales of TPP are taxable unless specifically exempted. R&TC Section 6051. Taxable items include: electronics, appliances, furniture, equipment, building materials, vehicles, boats, aircraft, clothing and footwear (**NO clothing exemption**), jewelry, watches, accessories, sporting goods, toys, games, household goods, office supplies. [T1]

### 2.2 Food and Beverages [T1]

| Category | Taxable? | Citation |
|----------|----------|----------|
| Grocery food (for home consumption) | **EXEMPT** | R&TC Section 6359 |
| Prepared food (heated, served for on-premises) | **TAXABLE** | R&TC Section 6359(d)(7) |
| Carbonated beverages | **TAXABLE** | R&TC Section 6359(c) |
| Hot prepared food | **TAXABLE** | R&TC Section 6359(d)(2) |
| Cold sandwiches from deli (with utensils/for on-premises) | **TAXABLE** | R&TC Section 6359(d)(7) |
| Cold sandwiches to go (without utensils, no seating) | **EXEMPT** | R&TC Section 6359 |
| Candy | **EXEMPT** (unlike many states) | R&TC Section 6359 |
| Dietary supplements | **EXEMPT** | R&TC Section 6359 |
| Water (non-carbonated, non-flavored) | **EXEMPT** | R&TC Section 6353 |
| Ice | **EXEMPT** (food product) | R&TC Section 6359 |
| Alcoholic beverages | **TAXABLE** | R&TC Section 6359(c) |
| Vending machine food (under $0.25 threshold) | Special rules | R&TC Section 6359.2 |

**80/80 Rule:** When more than 80% of a seller's gross receipts are from the sale of food products AND more than 80% of the food sold is heated or prepared, then ALL sales of food (even cold to-go items) become taxable. R&TC Section 6359(d)(7). [T1]

### 2.3 Services [T1/T2]

| Service Category | Taxable? | Notes |
|-----------------|----------|-------|
| Fabrication labor (creating new TPP) | **TAXABLE** | R&TC Section 6006(b) [T1] |
| Repair labor (restoring TPP) | **EXEMPT** (labor portion) | If separately stated; parts are taxable [T1] |
| Installation labor | **EXEMPT** (if separately stated) | R&TC Section 6012(c)(3) [T1] |
| Professional services (legal, accounting, consulting) | **EXEMPT** | Not enumerated [T1] |
| Janitorial / cleaning services | **EXEMPT** | Not enumerated [T1] |
| Personal care (hair, nails, spa) | **EXEMPT** | Not enumerated [T1] |
| Transportation / shipping | **EXEMPT** (if separately stated) | R&TC Section 6011(c)(7) [T1] |
| Digital / electronic delivery of content | See SaaS/Digital section | Evolving area [T2] |

### 2.4 SaaS and Digital Goods [T2]

| Product | Taxable? | Notes |
|---------|----------|-------|
| Canned software (physical media) | **TAXABLE** | TPP delivered in tangible form [T1] |
| Canned software (electronic download) | **TAXABLE** | Regulation 1502(f)(1)(D) -- treated as TPP [T1] |
| Custom software (any delivery) | **EXEMPT** | Not TPP; treated as a service [T1] |
| SaaS (cloud-hosted, no download) | **NOT TAXABLE** (most cases) | No transfer of TPP; no definitive statute -- case-by-case [T2] |
| Digital music, movies, books (permanent download) | **TAXABLE** | Electronic delivery of TPP equivalent [T1] |
| Streaming services (no download) | **NOT TAXABLE** | No transfer of TPP [T1] |
| Digital photographs (download) | **TAXABLE** | TPP equivalent [T1] |
| Mobile apps (download) | **TAXABLE** | TPP equivalent [T1] |

**Critical note:** California's SaaS position is based on administrative guidance and rulings, not a clear statutory provision. The CDTFA's position that SaaS accessed remotely without download is not taxable could change. Always verify current guidance. [T2]

**Legislation:** R&TC Section 6010.9; CDTFA Regulation 1502.

### 2.5 Clothing and Apparel [T1]

**Clothing is FULLY TAXABLE in California.** There is no clothing exemption. This includes all garments, shoes, hats, accessories, and protective clothing. [T1]

---

## Step 3: Return Form Structure [T1]

### 3.1 Primary Return

| Form | Name | Use |
|------|------|-----|
| CDTFA-401 | State, Local, and District Sales and Use Tax Return | Primary return for all filers [T1] |
| CDTFA-401-A | State, Local, and District Sales and Use Tax Return (Short Form) | Annual filers [T1] |
| CDTFA-401-EZ | Short Form | Simple filers [T1] |
| CDTFA-531 | Schedule of Additional District Taxes | Sellers in multiple districts [T1] |

### 3.2 District Tax Reporting [T1]

| Reporting Element | Detail |
|-------------------|--------|
| Return form | District taxes reported on same CDTFA-401 [T1] |
| District schedule | CDTFA-531 may be required for multi-district sellers [T1] |
| District identification | Each district identified by CDTFA-assigned district code [T1] |
| Allocation rule (shipped) | District tax based on delivery address (destination-based) [T1] |
| Allocation rule (counter) | District tax based on seller's location [T1] |

### 3.3 Use Tax Reporting [T1]

| Filer Type | Reporting Method |
|-----------|-----------------|
| Registered sellers | Report on CDTFA-401 return [T1] |
| Individuals | Form 540, Line 91 or separate use tax return [T1] |
| Businesses not registered as sellers | CDTFA-401-A or state income tax return [T1] |

### 3.4 Use Tax Rules [T1]

| Rule | Detail |
|------|--------|
| When use tax applies | TPP purchased from out-of-state seller without CA tax collected; TPP purchased tax-free and diverted to taxable use; TPP brought into CA for use/storage/consumption [T1] |
| Use tax rate | Identical to combined sales tax rate at location of use [T1] |
| Credit for tax paid to other states | Credit allowed under R&TC Section 6406; cannot exceed CA use tax due; no credit for foreign country taxes [T1] |

---

## Step 4: Deductibility / Exemptions [T1/T2]

### 4.1 Common Exemptions

| Exemption | Statute | Notes | Tier |
|-----------|---------|-------|------|
| Food for home consumption | R&TC Section 6359 | Grocery food exempt; prepared food taxable | [T1] |
| Prescription medicine | R&TC Section 6369 | Drugs prescribed by licensed practitioner | [T1] |
| Over-the-counter medicine | **TAXABLE** | No exemption for OTC drugs in CA | [T1] |
| Medical devices (prescribed) | R&TC Section 6369.1 | Must be prescribed | [T1] |
| Agricultural feed and seed | R&TC Section 6358 | Used in farming/agriculture | [T1] |
| Farm equipment and machinery | R&TC Section 6356.5 | Used primarily in producing/harvesting agricultural products | [T1] |
| Manufacturing equipment (partial) | R&TC Section 6377.1 | Partial exemption -- see below | [T1] |
| Resale | R&TC Section 6091 | Goods purchased for resale; requires resale certificate | [T1] |
| Interstate commerce | R&TC Section 6396 | Goods shipped out of state | [T1] |
| US government sales | R&TC Section 6381 | Federal government purchases | [T1] |
| Foreign diplomats | R&TC Section 6381.5 | With proper credentials | [T1] |
| Occasional sales | R&TC Section 6367 | Isolated/occasional sales by non-retailers | [T1] |

### 4.2 Manufacturing and R&D Exemption (Partial) [T1]

| Parameter | Detail |
|-----------|--------|
| Scope | State portion (3.9375%) exempt; district taxes still apply in full [T1] |
| Qualifying property | TPP used in manufacturing, processing, refining, fabricating, or recycling [T1] |
| R&D coverage | Qualified equipment in biotechnology, physical/engineering/life sciences [T1] |
| Certificate required | CDTFA-230-M (partial exemption certificate) [T1] |
| Sunset | Extended multiple times; verify current expiration date [T2] |
| Authority | R&TC Section 6377.1; CDTFA Regulation 1525.4 |

### 4.3 Resale Exemption [T1]

| Parameter | Detail |
|-----------|--------|
| Form | CDTFA-230 (Resale Certificate) [T1] |
| Expiration | Does not expire; seller should periodically verify buyer's permit is active [T1] |
| Multi-state certificates accepted? | **NO** -- CA does NOT accept MTC Uniform Certificate or SST Certificate [T1] |
| Misuse penalty | Misdemeanor; fine and/or imprisonment (R&TC Section 6094.5) [T1] |

### 4.4 Nonprofit Exemptions [T2]

| Rule | Detail |
|------|--------|
| Blanket exemption? | **NO** -- California does NOT provide a blanket sales tax exemption for nonprofits [T1] |
| General rule | Nonprofits must pay sales tax on purchases and collect on taxable sales [T1] |
| Limited exceptions | Certain thrift stores (R&TC Section 6375); some fundraising sales may qualify for occasional sale exemption [T2] |

### 4.5 Exemption Certificates [T1]

| Certificate | Form | Purpose |
|------------|------|---------|
| Resale | CDTFA-230 | Purchases for resale [T1] |
| Manufacturing/R&D (partial) | CDTFA-230-M | Manufacturing/R&D equipment [T1] |
| Government entity | CDTFA-230-G | Government purchases [T1] |
| Foreign diplomat | CDTFA-230-FD | Diplomatic exemption [T1] |
| Farm equipment | CDTFA-230-F | Agricultural equipment [T1] |
| Teleproduction | CDTFA-230-TP | Motion picture/TV production [T1] |

**Burden of proof:** The seller bears the burden of proving a sale was exempt. Failure to obtain and retain a valid exemption certificate means the seller is liable for uncollected tax. R&TC Section 6091-6094. [T1]

---

## Step 5: Key Thresholds [T1]

### 5.1 Economic Nexus Threshold [T1]

| Parameter | Value |
|-----------|-------|
| Revenue threshold | More than $500,000 in total combined sales of TPP delivered into CA [T1] |
| Transaction count threshold | **None** -- revenue only [T1] |
| Measurement period | Preceding or current calendar year [T1] |
| Effective date | April 1, 2019 [T1] |
| Exempt sales included? | Yes -- exempt sales count toward the threshold [T1] |
| Marketplace sales excluded? | Yes -- marketplace-facilitated sales excluded from seller's threshold [T1] |
| Authority | R&TC Section 6203(c)(4) |

**Note:** The $500,000 threshold is the highest among US states (tied with Texas). [T1]

### 5.2 Registration Requirements [T1]

| Requirement | Detail |
|------------|--------|
| Who must register | Any person engaged in business in CA as a seller of TPP (R&TC Section 6066) [T1] |
| Registration type | California Seller's Permit (no fee) [T1] |
| Security deposit | CDTFA may require based on estimated tax liability [T1] |
| Display requirement | Display permit at each place of business (R&TC Section 6067) [T1] |

### 5.3 Marketplace Facilitator Rules [T1]

| Rule | Detail |
|------|--------|
| Effective date | Enacted; marketplace facilitators must collect and remit [T1] |
| Facilitator treated as | The retailer for purposes of the transaction (R&TC Sections 6040-6045) [T1] |
| Seller relief | Sellers relieved of collection obligation for marketplace sales [T1] |
| Seller filing obligation | Sellers must still file returns reporting marketplace sales (as non-taxable) [T1] |
| Facilitator liability | Limited if good-faith reliance on seller-provided information (R&TC Section 6045) [T1] |

### 5.4 Prepayment Threshold [T1]

| Parameter | Value |
|-----------|-------|
| Threshold | Average monthly tax liability exceeding $17,000 [T1] |
| Prepayment schedule | Two prepayments per quarter (quarterly filers) [T1] |
| Due dates | 24th of the first and second month of each quarter [T1] |
| Reconciliation | Prepayments reconciled on the quarterly return [T1] |
| Authority | R&TC Sections 6471, 6479 |

---

## Step 6: Filing Deadlines and Penalties [T1]

### 6.1 Filing Frequency

| Frequency | Criteria | Due Date |
|-----------|----------|----------|
| Monthly | Tax liability > ~$10,000/month | Last day of the month following the reporting period [T1] |
| Quarterly | Most retailers | Last day of the month following the quarter [T1] |
| Annual | Low-volume sellers (< $23,000/year in tax) | January 31 following the calendar year [T1] |

### 6.2 Quarterly Due Dates [T1]

| Quarter | Period | Due Date |
|---------|--------|----------|
| Q1 | January 1 -- March 31 | April 30 |
| Q2 | April 1 -- June 30 | July 31 |
| Q3 | July 1 -- September 30 | October 31 |
| Q4 | October 1 -- December 31 | January 31 |

**Legislation:** R&TC Section 6451 (quarterly); R&TC Section 6455 (monthly prepayments); R&TC Section 6479.3 (annual).

### 6.3 Electronic Filing [T1]

| Rule | Detail |
|------|--------|
| Mandatory e-filing | Taxpayers with estimated tax liability averaging $10,000+/month, or making 2+ monthly prepayments (R&TC Section 6479.3) [T1] |
| Portal | CDTFA Online Services [T1] |

### 6.4 Penalties and Interest [T1]

| Penalty | Rate | Citation |
|---------|------|----------|
| Late filing | 10% of tax due | R&TC Section 6591 [T1] |
| Late payment | 10% of tax due | R&TC Section 6591 [T1] |
| Negligence | 10% of deficiency | R&TC Section 6484 [T1] |
| Fraud | 25% of deficiency | R&TC Section 6485 [T1] |
| Interest on underpayment | Adjusted quarterly (linked to federal rate) | R&TC Section 6591.5 [T1] |

### 6.5 Vendor Discount [T1]

California does **not** offer a vendor discount (timely filing discount). Sellers do not retain a percentage of collected tax as compensation. [T1]

### 6.6 Record Retention [T1]

| Parameter | Value |
|-----------|-------|
| Retention period | Minimum 4 years from the later of: due date of return or date return was filed [T1] |
| Authority | R&TC Section 7053; CDTFA Regulation 1698 |
| Records required | Invoices, receipts, exemption/resale certificates, bank statements, purchase orders, contracts, inventory records, shipping records [T1] |

### 6.7 Statute of Limitations [T1]

| Scenario | Limitation Period |
|----------|------------------|
| Standard assessment | 3 years from filing date or due date [T1] |
| No return filed | No limitation (unlimited) [T1] |
| Fraud | No limitation (unlimited) [T1] |
| 25% or more understatement | 8 years [T1] |

**Legislation:** R&TC Section 6487.

---

## Step 7: California-Specific Rules [T1/T2]

### 7.1 District Tax Administration [T1]

| Rule | Detail |
|------|--------|
| Reporting | District taxes reported on same CDTFA-401 return [T1] |
| Multi-district sellers | CDTFA-531 (Schedule of Additional District Taxes) may be required [T1] |
| District identification | Each district identified by CDTFA-assigned district code [T1] |
| Sales tracking | Sellers must track sales by district for proper allocation [T1] |
| Common audit finding | Allocation errors -- maintain detailed records of delivery addresses [T1] |

### 7.2 District Tax Allocation Scenarios [T1]

| Scenario | Tax Rate Applied |
|----------|-----------------|
| Seller in LA, ships to San Francisco | SF combined rate (destination) [T1] |
| Seller in LA, customer picks up at LA store | LA combined rate (seller's location) [T1] |
| Seller in Oregon, ships to Sacramento | Sacramento combined rate (destination) [T1] |
| Seller in LA, ships to Oregon | No CA tax (interstate commerce) [T1] |

### 7.3 Amazon FBA Inventory Nexus [T1]

Inventory stored in an Amazon FBA warehouse in California creates **physical nexus**. The seller must register for a California seller's permit and collect California sales tax on all taxable sales to California customers (not just sales fulfilled from CA warehouses). Sales through Amazon's marketplace are collected by Amazon as the marketplace facilitator. [T1]

**Legislation:** R&TC Section 6203(c); R&TC Sections 6040-6045.

### 7.4 Cannabis Products [T1]

Cannabis products are subject to California sales tax at the standard rate. Additionally, cannabis is subject to a separate cannabis excise tax (currently 15%) and, for cultivators, a cultivation tax (suspended effective July 1, 2022). The sales tax and cannabis excise tax are separate obligations. [T1]

**Legislation:** R&TC Section 34011 (cannabis excise tax); R&TC Section 6051.

### 7.5 Detailed Taxability Matrix [T1]

| Category | State Rate (7.25%) | District Tax | Exemption Certificate | Key Statute |
|----------|-------------------|-------------|----------------------|-------------|
| General TPP | Taxable | Yes (varies) | N/A | R&TC Sec. 6051 |
| Grocery food (cold, unprepared) | Exempt | Exempt | N/A | R&TC Sec. 6359 |
| Prepared food (hot, dine-in) | Taxable | Yes | N/A | R&TC Sec. 6359(d) |
| Carbonated beverages | Taxable | Yes | N/A | R&TC Sec. 6359(c) |
| Candy | Exempt | Exempt | N/A | R&TC Sec. 6359 |
| Prescription medicine | Exempt | Exempt | N/A | R&TC Sec. 6369 |
| OTC medicine | Taxable | Yes | N/A | No exemption |
| Clothing (all items) | Taxable | Yes | N/A | No exemption |
| Canned software (download) | Taxable | Yes | N/A | Reg. 1502 |
| SaaS (cloud, no download) | Not taxable (generally) | Not taxable (generally) | N/A | Admin. guidance |
| Custom software | Exempt | Exempt | N/A | Service, not TPP |
| Manufacturing equipment | Partial (reduced state) | Yes (full district) | CDTFA-230-M | R&TC Sec. 6377.1 |
| Farm equipment | Exempt | Exempt | CDTFA-230-F | R&TC Sec. 6356.5 |
| Resale purchases | Exempt | Exempt | CDTFA-230 | R&TC Sec. 6091 |
| Interstate shipments | Exempt | Exempt | N/A | R&TC Sec. 6396 |
| Government purchases (federal) | Exempt | Exempt | N/A | R&TC Sec. 6381 |
| Fuel/petroleum | Separate excise | Separate excise | N/A | R&TC Sec. 7301+ |
| Newspapers/periodicals | Exempt | Exempt | N/A | R&TC Sec. 6362 |
| Motor vehicles | Taxable | Yes (registration) | N/A | R&TC Sec. 6051 |

---

## PROHIBITIONS [T1]

- **NEVER** apply a clothing exemption in California -- clothing is fully taxable. [T1]
- **NEVER** assume SaaS is definitively taxable or nontaxable without reviewing the specific facts of the transaction (download vs. cloud-only access). [T2]
- **NEVER** accept a multi-state exemption certificate (MTC Uniform or SST) in lieu of the California CDTFA-230 form. [T1]
- **NEVER** use origin-based sourcing for California transactions -- California is destination-based. [T1]
- **NEVER** assume nonprofits are exempt from California sales tax without verifying the specific statutory exemption. [T1]
- **NEVER** ignore district taxes -- the 7.25% state rate is the minimum, not the total rate. [T1]
- **NEVER** treat OTC medicine as exempt -- only prescription medicine is exempt in California. [T1]
- **NEVER** file a return without reconciling prepayments if the seller is required to make prepayments. [T1]
- **NEVER** assume marketplace sellers have no filing obligation -- they must still file returns even if the marketplace collects tax. [T1]
- **NEVER** forget that Amazon FBA inventory in California creates physical nexus independent of economic nexus. [T1]

---

## Edge Case Registry [T1/T2]

### EC1 -- Drop Shipments [T2]

**Situation:** An out-of-state retailer sells goods to a California customer and has a California supplier drop-ship directly to the customer.

**Resolution:** The drop shipper (CA supplier) may owe California sales tax on the retail selling price unless the out-of-state retailer provides a valid resale certificate. If the retailer is not registered in California, the drop shipper should collect tax from the retailer or on the retail value. This is a complex area -- flag for reviewer.

**Legislation:** R&TC Section 6007; CDTFA Regulation 1706.

### EC2 -- Leases and Rentals [T1]

**Situation:** A California business leases equipment to customers.

**Resolution:** Leases and rentals of TPP are generally taxable in California. Tax applies to the lease payments as they become due. R&TC Section 6006(g). If the lessor paid sales tax on the purchase price, they may elect to pay tax on the purchase price rather than on each lease payment.

**Legislation:** R&TC Section 6006(g); CDTFA Regulation 1660.

### EC3 -- Bundled Transactions (Mixed TPP and Services) [T2]

**Situation:** A seller provides a bundled transaction that includes both taxable TPP and nontaxable services.

**Resolution:** If the true object of the transaction is the service, and the TPP is incidental (less than 10% of the total price), the entire transaction may be exempt. If the TPP component is more than incidental, the entire transaction is taxable unless the seller separately states the charges. Flag for reviewer -- the "true object" test requires judgment.

**Legislation:** R&TC Section 6012(c)(3); CDTFA Regulation 1501.

### EC4 -- Construction Contractors [T2]

**Situation:** A contractor installs materials into real property.

**Resolution:** Contractors are generally the consumers of materials they install into real property and must pay sales tax on their purchase of those materials. They do not collect sales tax from the property owner on the installed price. However, if the contractor sells materials separately without installation, sales tax applies.

**Legislation:** R&TC Section 6006; CDTFA Regulation 1521.

### EC5 -- Trade-Ins [T1]

**Situation:** A customer trades in used equipment as partial payment for new equipment.

**Resolution:** California allows a trade-in credit -- sales tax is calculated on the net price (selling price minus trade-in value) rather than the gross selling price, provided the trade-in is of "like kind." R&TC Section 6011(c)(8).

**Legislation:** R&TC Section 6011(c)(8); CDTFA Regulation 1655.

### EC6 -- Digital Advertising [T1]

**Situation:** A company purchases digital advertising services (Google Ads, social media ads).

**Resolution:** Digital advertising services are not taxable in California. They are services, not sales of TPP. No sales tax applies. [T1]

### EC7 -- Shipping and Handling Charges [T1]

**Situation:** A seller charges shipping and handling separately on an invoice.

**Resolution:** Delivery charges are not taxable when: (a) separately stated on the invoice, (b) the shipment includes only exempt items or the delivery is by common carrier or USPS. However, handling charges that are not true delivery costs may be taxable. If shipping and handling are combined as one line item, the entire charge is taxable.

**Legislation:** R&TC Section 6011(c)(7); R&TC Section 6012(c)(7); CDTFA Regulation 1628.

### EC8 -- Amazon FBA Inventory Nexus [T1]

**Situation:** An out-of-state seller stores inventory in an Amazon FBA warehouse in California.

**Resolution:** The presence of inventory in California creates physical nexus. The seller must register for a California seller's permit and collect California sales tax on all taxable sales to California customers. Sales made through Amazon's marketplace are collected by Amazon as the marketplace facilitator.

**Legislation:** R&TC Section 6203(c); R&TC Sections 6040-6045.

### EC9 -- Cannabis Products [T1]

**Situation:** A licensed cannabis retailer sells cannabis products.

**Resolution:** Cannabis products are subject to California sales tax at the standard rate plus a separate cannabis excise tax (currently 15%). The cultivation tax was suspended effective July 1, 2022. Sales tax and cannabis excise tax are separate obligations.

**Legislation:** R&TC Section 34011; R&TC Section 6051.

### EC10 -- Marketplace Seller Also Sells Direct [T1]

**Situation:** A seller sells products both on Amazon and through their own website.

**Resolution:** Amazon collects tax on marketplace sales. The seller must collect and remit tax on direct website sales to California customers independently. Track marketplace vs. direct sales separately and report accordingly on the CDTFA-401.

**Legislation:** R&TC Sections 6040-6045.

---

## Test Suite

### Test 1 -- Basic Taxable Sale in Los Angeles [T1]

**Input:** Retailer in Los Angeles sells a laptop for $1,000 to a walk-in customer. Combined LA rate is 9.50%.
**Expected output:** Sales tax = $95.00. Total charged = $1,095.00. Report on CDTFA-401 with district tax breakout.

### Test 2 -- Grocery Food Exemption [T1]

**Input:** Grocery store sells $200 of unprepared food items (bread, milk, produce) to a consumer.
**Expected output:** Sales tax = $0. Grocery food is exempt under R&TC Section 6359. No tax collected.

### Test 3 -- Prepared Food -- Taxable [T1]

**Input:** Restaurant sells a $25 hot meal for dine-in consumption. Location rate: 8.75%.
**Expected output:** Sales tax = $2.19 (rounded). Prepared food is taxable.

### Test 4 -- Out-of-State Seller Exceeding Economic Nexus [T1]

**Input:** An Oregon-based online retailer has $600,000 in sales to California customers in the current calendar year. No physical presence in CA.
**Expected output:** Seller exceeds the $500,000 economic nexus threshold. Must register with CDTFA, collect CA sales tax on all future taxable sales to CA customers, and file returns.

### Test 5 -- Resale Certificate [T1]

**Input:** A California retailer purchases $5,000 of inventory from a California wholesaler for resale. Retailer provides a valid CDTFA-230 resale certificate.
**Expected output:** No sales tax charged on the purchase. The retailer collects sales tax when the goods are sold to the end consumer.

### Test 6 -- SaaS Subscription [T2]

**Input:** A California business subscribes to a cloud-based accounting software (SaaS). Monthly fee: $50. No software is downloaded; access is purely via web browser.
**Expected output:** Generally NOT TAXABLE under current CDTFA guidance (no transfer of TPP). However, flag for reviewer -- this area lacks definitive statutory authority. If the subscription includes downloadable components, analysis may change.

### Test 7 -- Manufacturing Equipment Partial Exemption [T1]

**Input:** A manufacturer purchases a $100,000 CNC machine for use in manufacturing. Location has a combined rate of 9.25% (7.25% state + 2.00% district).
**Expected output:** Partial exemption applies (CDTFA-230-M provided). State portion reduced by 3.9375%. Effective state rate: 3.3125%. District tax of 2.00% still applies. Total rate: 5.3125%. Tax = $5,312.50 (instead of $9,250 without exemption). Savings = $3,937.50.

### Test 8 -- Use Tax on Out-of-State Purchase [T1]

**Input:** A California business purchases office furniture for $3,000 from an Oregon retailer. Oregon has no sales tax. No tax is collected at purchase. Furniture is used in the business's San Francisco office (combined rate 8.625%).
**Expected output:** California use tax of $258.75 is due ($3,000 x 8.625%). Report on CDTFA-401 or income tax return.

### Test 9 -- Clothing Sale [T1]

**Input:** A clothing retailer sells a $500 jacket to a customer. Store located in San Jose (rate 9.375%).
**Expected output:** Sales tax = $46.88. Clothing is fully taxable in California. No clothing exemption exists.

### Test 10 -- Marketplace Facilitator [T1]

**Input:** A third-party seller lists products on Amazon. Amazon fulfills and ships a $200 item to a California customer. Rate at customer's address: 8.25%.
**Expected output:** Amazon (marketplace facilitator) collects and remits $16.50 in sales tax. The seller does not collect tax on this transaction but must report it as marketplace-facilitated on their own return.

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
| CDTFA Main | https://www.cdtfa.ca.gov |
| Online Filing | https://onlineservices.cdtfa.ca.gov |
| Rate Lookup | https://www.cdtfa.ca.gov/taxes-and-fees/rates.aspx |
| Phone | 1-800-400-7115 |
| Seller's Permit Application | Online via CDTFA |
| Regulation Text | https://www.cdtfa.ca.gov/lawguides/vol1/sutr/sales-and-use-tax-regulations.html |
| District Tax Rates | https://www.cdtfa.ca.gov/taxes-and-fees/sales-use-tax-rates.htm |
| Audit Manual | https://www.cdtfa.ca.gov/taxes-and-fees/audit-manual.htm |
| Publications/Pamphlets | https://www.cdtfa.ca.gov/formspubs/ |

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
