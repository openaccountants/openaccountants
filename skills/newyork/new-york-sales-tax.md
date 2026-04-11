---
name: new-york-sales-tax
description: Use this skill whenever asked about New York sales and use tax, NYS DTF filings, NYC sales tax, New York exemptions, New York clothing exemption, New York nexus, or any request involving New York state sales and use tax compliance. Trigger on phrases like "New York sales tax", "NY sales tax", "NYC sales tax", "DTF", "ST-100", "New York clothing exemption", "New York resale certificate", or any request involving New York sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any New York sales tax work.
---

# New York Sales and Use Tax Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | New York, United States |
| Jurisdiction Code | US-NY |
| Tax Type | Sales and Use Tax (state + local) |
| Primary Legislation | New York Tax Law, Article 28 (Sales Tax) and Article 29 (Use Tax) |
| Key Statutes | Tax Law Sections 1101-1167 (Article 28); Tax Law Sections 1201-1250 (Article 29) |
| Tax Authority | New York State Department of Taxation and Finance (NYS DTF) |
| Filing Portal | https://www.tax.ny.gov |
| Federal Framework Skill | us-sales-tax (read first for Wayfair, nexus overview, and multi-state context) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires New York CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate structure, clothing exemption, basic taxability, filing mechanics, nexus thresholds. Tier 2: SaaS taxability, mixed transactions, MCTD surcharge. Tier 3: audit defense, complex bundled transactions, advisory opinions. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to a licensed tax professional and document the gap.

---

## Step 0: Client Onboarding Questions

Before performing any New York sales tax work, collect the following from the client:

| # | Question | Why It Matters |
|---|----------|----------------|
| 1 | What is your Certificate of Authority number? | Required for filing; confirms registration with NYS DTF. [T1] |
| 2 | What is your assigned filing frequency (quarterly, monthly/part-quarterly, annual, PrompTax)? | Determines return due dates and payment schedules. [T1] |
| 3 | What type of nexus do you have in New York (physical, economic, both)? | NY requires BOTH $500K revenue AND 100 transactions for economic nexus (AND test). [T1] |
| 4 | Do you sell through any marketplace facilitators (Amazon, eBay, Etsy, etc.)? | Marketplace facilitators collect tax on facilitated sales; seller must still track but not remit on those transactions. [T1] |
| 5 | Do you make sales in the MCTD (NYC, Rockland, Westchester, Dutchess, Orange, Putnam, Nassau, Suffolk)? | 0.375% MCTD surcharge applies; separate schedule (ST-100.3) may be required. [T1] |
| 6 | Do you sell clothing or footwear? | Items under $110/item are exempt from state and NYC tax (per-item threshold). [T1] |
| 7 | Is your annual sales tax liability over $500,000? | PrompTax (accelerated EFT payments) may be required. [T1] |
| 8 | Do you sell software, SaaS, or digital products? | SaaS is taxable in NY as pre-written software. [T1] |

---

## Step 1: Tax Rate Structure [T1]

### 1.1 Rate Components

| Component | Range | Notes |
|-----------|-------|-------|
| State rate | 4.00% | Uniform statewide [T1] |
| County/city rate | 3.00% -- 4.875% | Varies by jurisdiction [T1] |
| MCTD surcharge | 0.375% | Metropolitan Commuter Transportation District only [T1] |

**Legislation:** Tax Law Section 1105.

### 1.2 Key Combined Rates [T1]

| Jurisdiction | Combined Rate | Breakdown |
|-------------|--------------|-----------|
| New York City (all 5 boroughs) | **8.875%** | 4% state + 4.5% city + 0.375% MCTD |
| Westchester County | 8.375% | 4% + 4% county + 0.375% MCTD |
| Nassau County | 8.625% | 4% + 4.25% county + 0.375% MCTD |
| Suffolk County | 8.625% | 4% + 4.25% county + 0.375% MCTD |
| Albany County | 8.00% | 4% + 4% county |
| Erie County (Buffalo) | 8.00% | 4% + 4% county |

**Maximum combined rate: 8.875%** (New York City). [T1]

### 1.3 MCTD Surcharge [T1]

| Parameter | Value |
|-----------|-------|
| MCTD counties | New York City, Rockland, Westchester, Dutchess, Orange, Putnam, Nassau, Suffolk [T1] |
| Surcharge rate | 0.375% [T1] |
| Authority | Tax Law Section 1109 |

### 1.4 Sourcing Rules [T1]

| Scenario | Rate Applied |
|----------|-------------|
| Shipped goods | Rate at delivery address (destination-based) [T1] |
| Customer pickup | Rate at seller's location [T1] |
| Remote (out-of-state) sellers | Destination-based [T1] |

---

## Step 2: Transaction Classification Rules [T1/T2]

### 2.1 General Rule [T1]

New York imposes sales tax on: (a) retail sales of TPP, (b) certain enumerated services, (c) food and drink sold by restaurants, (d) hotel occupancy, and (e) admissions and entertainment. Tax Law Section 1105. [T1]

### 2.2 Tangible Personal Property (TPP) [T1]

All retail sales of TPP are taxable unless specifically exempted: electronics, appliances, furniture, equipment, vehicles, jewelry, watches, accessories, sporting goods, toys, games, building materials, office supplies. [T1]

### 2.3 Clothing and Footwear -- KEY EXEMPTION [T1]

| Item Price | State Tax (4%) | NYC Local Tax (4.5%) | Total in NYC |
|-----------|---------------|---------------------|-------------|
| Under $110 | **EXEMPT** | **EXEMPT** (NYC exempts local too) | **$0** [T1] |
| $110 or more | **TAXABLE** (4%) | **TAXABLE** | 8.875% [T1] |

**Critical details:**

| Rule | Detail |
|------|--------|
| Per-item threshold | Exemption applies per ITEM, not per transaction [T1] |
| NYC coverage | NYC exempts qualifying clothing from BOTH state and local tax [T1] |
| Non-NYC counties | Some counties do NOT exempt clothing from local tax -- check county-specific rules [T2] |
| Non-qualifying items | Costume/formal wear accessories (cuff links, tiara), sport/recreational equipment (ski boots, cleats), protective equipment (hard hats, safety goggles) [T1] |
| Sales tax holiday | New York does NOT have a temporary sales tax holiday -- the clothing exemption is permanent and year-round [T1] |

**Legislation:** Tax Law Section 1115(a)(30); Tax Bulletin ST-530.

### 2.4 Food and Beverages [T1]

| Category | Taxable? | Citation |
|----------|----------|----------|
| Grocery food (unprepared, for home consumption) | **EXEMPT** | Tax Law Section 1115(a)(1) |
| Prepared food (heated, served for on-premises) | **TAXABLE** | Tax Law Section 1105(d) |
| Candy and confections | **TAXABLE** | Tax Law Section 1115(a)(1) exception |
| Carbonated beverages / soft drinks | **TAXABLE** | Tax Law Section 1115(a)(1) exception |
| Bottled water (non-carbonated) | **EXEMPT** | |
| Dietary supplements | **EXEMPT** | Tax Law Section 1115(a)(1) |
| Alcoholic beverages | **TAXABLE** | |
| Restaurant meals | **TAXABLE** | Tax Law Section 1105(d) |

**Restaurant rule:** ALL food and drink sold by restaurants (including otherwise exempt items like bottled water) becomes TAXABLE. Tax Law Section 1105(d). The restaurant context overrides the grocery food exemption. [T1]

### 2.5 Taxable Services [T1/T2]

| Taxable Service | Statute |
|----------------|---------|
| Information services | Tax Law Section 1105(c)(1) |
| Processing and printing services | Tax Law Section 1105(c)(2) |
| Installation, maintenance, and repair of TPP | Tax Law Section 1105(c)(3) |
| Storage | Tax Law Section 1105(c)(4) |
| Interior decorating/design | Tax Law Section 1105(c)(5) |
| Protective/detective services | Tax Law Section 1105(c)(6) |
| Trash removal (commercial) | Tax Law Section 1105(c)(7) |
| Credit rating/reporting | Tax Law Section 1105(c)(8) |
| Telephone/telegraph services | Tax Law Section 1105(b)(1) |
| Utility services (gas, electric, steam) | Tax Law Section 1105(b)(2) |

**Nontaxable services:** Legal, accounting, medical, consulting, advertising, education, janitorial, personal care, construction labor. [T1]

### 2.6 SaaS and Digital Goods [T1/T2]

| Product | Taxable? | Notes |
|---------|----------|-------|
| Canned software (physical media) | **TAXABLE** | TPP [T1] |
| Canned software (electronic download) | **TAXABLE** | Tax Law Section 1101(b)(6) -- pre-written software is TPP [T1] |
| Custom software (any delivery) | **EXEMPT** | Not TPP [T1] |
| SaaS (cloud-hosted) | **TAXABLE** | NYS treats SaaS as a sale of pre-written software; TSB-A-13(22)S [T1] |
| Digital music, movies, books (download) | **TAXABLE** | TPP equivalents [T1] |
| Streaming services (no download) | **TAXABLE** (as information service or entertainment) | Tax Law Section 1105(c)(1) [T1] |

**Important:** New York is one of the states that clearly taxes SaaS as a sale of pre-written computer software accessed remotely. [T1]

**Legislation:** Tax Law Section 1101(b)(6); TSB-A-13(22)S; TSB-A-18(27)S.

---

## Step 3: Return Form Structure [T1]

### 3.1 Filing Forms

| Form | Name | Use |
|------|------|-----|
| ST-100 | New York State and Local Quarterly Sales and Use Tax Return | Primary return [T1] |
| ST-100.3 | Quarterly Schedule N | Filers with nexus in the MCTD [T1] |
| ST-100.7 | Quarterly Schedule H | Sub-jurisdiction detail [T1] |
| ST-101 | Annual Schedule (Summary) | Annual summary [T1] |
| ST-810 | Monthly return | Large filers [T1] |
| ST-809 | Monthly return | NYC/MCTD quarterly filers with monthly part-quarterly payments [T1] |

### 3.2 Use Tax Reporting [T1]

| Filer Type | Reporting Method |
|-----------|-----------------|
| Registered vendors | Report on Form ST-100 [T1] |
| Individuals | Form IT-201 (NY resident income tax return), Line 59 [T1] |
| Businesses not registered | Form ST-140 (Individual Purchaser's Annual Report of Sales and Use Tax) [T1] |

### 3.3 Use Tax Rules [T1]

| Rule | Detail |
|------|--------|
| When use tax applies | TPP/taxable services from out-of-state seller without NY tax; TPP purchased tax-free and diverted to taxable use; TPP brought into NY for use/storage/consumption [T1] |
| Use tax rate | Combined state and local rate at location of use [T1] |
| Credit for tax paid to other states | Credit allowed under Tax Law Section 1118(7) [T1] |

---

## Step 4: Deductibility / Exemptions [T1/T2]

### 4.1 Common Exemptions

| Exemption | Statute | Notes | Tier |
|-----------|---------|-------|------|
| Clothing/footwear (under $110/item) | Sec. 1115(a)(30) | State and NYC local tax | [T1] |
| Grocery food | Sec. 1115(a)(1) | Unprepared food for home consumption | [T1] |
| Prescription drugs | Sec. 1115(a)(3) | Prescribed by practitioner | [T1] |
| OTC drugs and medicine | **TAXABLE** | No OTC exemption in NY | [T1] |
| Prosthetic devices, hearing aids | Sec. 1115(a)(4) | Medical devices | [T1] |
| Newspapers and periodicals | Sec. 1115(a)(5) | Qualifying publications | [T1] |
| Resale | Sec. 1101(b)(4) | Goods purchased for resale | [T1] |
| Manufacturing equipment | Sec. 1115(a)(12) | Machinery/equipment used directly in production | [T1] |
| Fuel/utilities for manufacturing | Sec. 1115(c) | Gas, electric used in production | [T1] |
| Farm equipment | Sec. 1115(a)(6) | Agricultural use | [T1] |
| Interstate commerce | Sec. 1115(a)(8) | Goods shipped out of state | [T1] |
| Federal government | Sec. 1116(a)(1) | Sales to US government | [T1] |
| NY state/local government | Sec. 1116(a)(1) | Sales to NY government entities | [T1] |

### 4.2 Manufacturing Exemption [T1]

| Parameter | Detail |
|-----------|--------|
| Scope | Full exemption for machinery, equipment, and parts [T1] |
| Qualification | Used directly and predominantly (more than 50%) in production of TPP for sale [T1] |
| Includes | Production machinery, conveyors, related equipment [T1] |
| Includes | Fuel and utilities consumed in production (Tax Law Section 1115(c)) [T1] |
| Excludes | Administrative, distribution, or office equipment [T1] |
| Authority | Tax Law Section 1115(a)(12) |

### 4.3 Resale Exemption [T1]

| Parameter | Detail |
|-----------|--------|
| Form | ST-120 (Resale Certificate) [T1] |
| Requirement | Must include buyer's Certificate of Authority number [T1] |
| Multi-state accepted | MTC Uniform Sales Tax Certificate accepted [T1] |
| SST Certificate | NOT accepted -- NY is not an SST member [T1] |
| Blanket certificates | Permitted for ongoing purchases [T1] |

### 4.4 Nonprofit Exemptions [T2]

| Parameter | Detail |
|-----------|--------|
| Certificate | Form ST-119 (Exempt Organization Certificate) from NYS DTF [T2] |
| Purchase certificate | Form ST-119.1 (Exempt Organization Exempt Purchase Certificate) [T2] |
| Qualifying organizations | IRC 501(c)(3) entities with NYS DTF approval [T2] |
| Scope | Covers purchases by the organization, not sales by the organization [T2] |

### 4.5 Exemption Certificates [T1]

| Certificate | Form | Purpose |
|------------|------|---------|
| Resale | ST-120 | Purchases for resale [T1] |
| Exempt organization purchase | ST-119.1 | Exempt organization purchases [T1] |
| Capital improvement | ST-124 | Exempt capital improvements to real property [T1] |
| Contractor exempt purchase | ST-120.1 | Contractor purchasing for exempt project [T1] |
| Farmer/commercial horse boarding | FT-1004 | Agricultural exemption [T1] |
| IDA agent | ST-123 | Industrial Development Agency projects [T1] |

---

## Step 5: Key Thresholds [T1]

### 5.1 Economic Nexus Threshold [T1]

| Parameter | Value |
|-----------|-------|
| Revenue threshold | More than $500,000 in gross receipts from sales of TPP delivered in NY [T1] |
| Transaction threshold | More than 100 transactions delivering TPP in NY [T1] |
| Test type | **AND test** -- BOTH thresholds must be met (unique among states; most use OR) [T1] |
| Measurement period | Prior four sales tax quarterly periods (NOT calendar year) [T1] |
| Marketplace exclusion | Marketplace sales where the marketplace collects tax do not count [T1] |
| Authority | Tax Law Section 1101(b)(8)(iv) |

### 5.2 Registration Requirements [T1]

| Requirement | Detail |
|------------|--------|
| Who must register | Any person required to collect sales tax (Tax Law Section 1134) [T1] |
| Registration form | Form DTF-17 or online through NY Business Express [T1] |
| Timing | Must register at least 20 days before beginning to collect tax [T1] |
| Fee | No fee [T1] |
| Filing frequency | Assigned by NYS DTF [T1] |

### 5.3 Marketplace Facilitator Rules [T1]

| Rule | Detail |
|------|--------|
| Effective date | June 1, 2019 [T1] |
| Facilitator treated as | The vendor for tax purposes (Tax Law Section 1101(b)(8)(vi)) [T1] |
| Seller relief | Sellers relieved of collection obligation for marketplace-facilitated sales [T1] |
| Direct sales | Marketplace sellers must still collect on direct (non-marketplace) sales [T1] |

### 5.4 PrompTax Threshold [T1]

| Parameter | Value |
|-----------|-------|
| Threshold | Annual sales tax liability exceeding $500,000 [T1] |
| Payment method | Electronic funds transfer (EFT) on accelerated schedule [T1] |
| Payment timing | Within 3 business days of end of each PrompTax period [T1] |
| Returns | Still filed quarterly [T1] |

---

## Step 6: Filing Deadlines and Penalties [T1]

### 6.1 Filing Frequency

| Frequency | Criteria | Due Date |
|-----------|----------|----------|
| Quarterly | Most vendors | 20th of the month following the quarter [T1] |
| Monthly (Part-Quarterly) | Tax liability > $300,000/year | Monthly payments due + quarterly return [T1] |
| Annual | Annual filers with minimal liability | March 20 following the year [T1] |
| PrompTax | Very large filers (> $500,000/year) | Accelerated electronic schedule [T1] |

### 6.2 Quarterly Due Dates (Sales Tax Quarters) [T1]

**IMPORTANT:** New York's sales tax quarters do NOT align with calendar quarters. They start March 1. [T1]

| Quarter | Period | Due Date |
|---------|--------|----------|
| March-May | March 1 -- May 31 | June 20 |
| June-August | June 1 -- August 31 | September 20 |
| September-November | September 1 -- November 30 | December 20 |
| December-February | December 1 -- February 28/29 | March 20 |

**Legislation:** Tax Law Section 1136.

### 6.3 Part-Quarterly (Monthly) Payment Schedule [T1]

| Month in Quarter | Due Date | Form |
|-----------------|----------|------|
| 1st month | 20th of the 2nd month | ST-809 |
| 2nd month | 20th of the 3rd month | ST-809 |
| 3rd month | 20th of the month after quarter end | ST-100 (full quarterly return) |

### 6.4 Penalties and Interest [T1]

| Penalty | Rate | Citation |
|---------|------|----------|
| Late filing | 10% of tax due (max) | Tax Law Section 1145(a)(1) [T1] |
| Late payment | 10% of tax due (max) | Tax Law Section 1145(a)(1) [T1] |
| Fraud | 50% of deficiency | Tax Law Section 1145(a)(2) [T1] |
| Interest on underpayment | Rate set quarterly by DTF | Tax Law Section 1142 [T1] |

### 6.5 Vendor Credit (Collection Allowance) [T1]

| Parameter | Value |
|-----------|-------|
| Rate | Up to 5% of the first $1,200,000 in tax collected per quarter [T1] |
| Maximum | $200 per quarter [T1] |
| Authority | Tax Law Section 1137(f) |

### 6.6 Record Retention [T1]

| Parameter | Value |
|-----------|-------|
| Retention period | Minimum 3 years from the due date of the return or the date filed, whichever is later [T1] |
| Authority | Tax Law Section 1135 |
| Records required | Sales invoices/receipts, purchase invoices, resale certificates (ST-120), exemption certificates, bank statements, inventory records, cash register tapes/POS data, delivery/shipping records [T1] |

### 6.7 Statute of Limitations [T1]

| Scenario | Limitation Period |
|----------|------------------|
| Standard assessment | 3 years from filing date [T1] |
| No return filed | No limitation (unlimited) [T1] |
| Fraud or willful evasion | No limitation (unlimited) [T1] |
| Substantial understatement (25%+) | 6 years [T1] |

### 6.8 Audit Considerations [T2]

| Factor | Detail |
|--------|--------|
| Audit types | Desk audits and field audits [T1] |
| High-risk industries | Restaurants, gas stations, auto dealers, construction [T2] |
| Estimation methods | Markup method, bank deposit method (if records inadequate) [T2] |
| Most common adjustment | Missing exemption certificates [T1] |

---

## Step 7: New York-Specific Rules [T1/T2]

### 7.1 MCTD Surcharge Detail [T1]

The Metropolitan Commuter Transportation District (MCTD) includes New York City, Rockland, Westchester, Dutchess, Orange, Putnam, Nassau, and Suffolk counties. An additional 0.375% sales tax surcharge applies in the MCTD. Tax Law Section 1109. [T1]

### 7.2 Detailed Taxability Matrix [T1]

| Category | Taxable? | State Rate | NYC Rate | Key Statute |
|----------|----------|-----------|----------|-------------|
| General TPP | Yes | 4% + local | 8.875% | Sec. 1105(a) |
| Grocery food (unprepared) | No | Exempt | Exempt | Sec. 1115(a)(1) |
| Prepared food / restaurant | Yes | 4% + local | 8.875% | Sec. 1105(d) |
| Candy and confections | Yes | 4% + local | 8.875% | Sec. 1115(a)(1) exc. |
| Prescription medicine | No | Exempt | Exempt | Sec. 1115(a)(3) |
| OTC medicine | Yes | 4% + local | 8.875% | No exemption |
| Clothing under $110/item | No | Exempt | Exempt (NYC) | Sec. 1115(a)(30) |
| Clothing $110 or more/item | Yes | 4% + local | 8.875% | Full rate applies |
| Canned software (any delivery) | Yes | 4% + local | 8.875% | Sec. 1101(b)(6) |
| Custom software | No | Exempt | Exempt | Not TPP |
| SaaS (cloud) | Yes | 4% + local | 8.875% | TSB-A-13(22)S |
| Manufacturing equipment | No | Exempt | Exempt | Sec. 1115(a)(12) |
| Farm equipment | No | Exempt | Exempt | Sec. 1115(a)(6) |
| Resale purchases | No | Exempt | Exempt | Sec. 1101(b)(4) |
| Interstate shipments | No | Exempt | Exempt | Sec. 1115(a)(8) |
| Telecom services | Yes | 4% + local | 8.875% | Sec. 1105(b)(1) |
| Information services | Yes | 4% + local | 8.875% | Sec. 1105(c)(1) |
| Repair/maintenance TPP | Yes | 4% + local | 8.875% | Sec. 1105(c)(3) |
| Professional services | No | Exempt | Exempt | Not enumerated |
| Hotel occupancy | Yes | Special rates | Special | Sec. 1105(e) |

---

## PROHIBITIONS [T1]

- **NEVER** apply the $110 clothing exemption per transaction -- it is per ITEM. [T1]
- **NEVER** use calendar quarters for New York sales tax -- NY quarters start March 1, not January 1. [T1]
- **NEVER** accept the SST Certificate of Exemption in New York -- NY is not an SST member. [T1]
- **NEVER** assume economic nexus with only the revenue threshold -- New York requires BOTH $500K revenue AND 100 transactions. [T1]
- **NEVER** treat SaaS as nontaxable in New York -- SaaS is taxable as pre-written software. [T1]
- **NEVER** treat restaurant food as exempt -- all food/drink at restaurants is taxable regardless of the individual item's grocery exemption status. [T1]
- **NEVER** assume the clothing exemption applies to local tax in all counties -- verify county-specific rules. [T2]
- **NEVER** confuse capital improvements (exempt) with repairs (taxable) without proper analysis. [T2]
- **NEVER** assume OTC medicine is exempt in New York -- only prescription drugs are exempt. [T1]
- **NEVER** file returns using calendar quarters -- use NY's March 1 quarterly start dates. [T1]

---

## Edge Case Registry [T1/T2]

### EC1 -- Clothing Threshold: $110 Boundary [T1]

**Situation:** A customer buys a shirt for $109 and a jacket for $115.

**Resolution:** The shirt ($109) is EXEMPT from state and NYC tax (under $110). The jacket ($115) is TAXABLE at the full combined rate. Tax is calculated on each item individually, not on the total transaction.

### EC2 -- Clothing Alterations [T1]

**Situation:** A tailor charges $30 for hemming pants that cost $90.

**Resolution:** The alteration service is taxable as a repair/maintenance service under Tax Law Section 1105(c)(3). The pants themselves are exempt (under $110). The $30 alteration charge is subject to sales tax.

### EC3 -- Capital Improvements vs. Repairs [T2]

**Situation:** A contractor performs work on a building.

**Resolution:** Capital improvements to real property are EXEMPT from sales tax (the contractor provides Form ST-124). Repairs, maintenance, and installations that do not qualify as capital improvements are TAXABLE services under Tax Law Section 1105(c)(3). The distinction requires professional judgment -- a capital improvement adds to the value or substantially prolongs the life of the property. Flag for reviewer.

**Legislation:** Tax Law Section 1105(c)(3); Tax Law Section 1101(b)(9); Tax Bulletin TB-ST-104.

### EC4 -- New York City vs. Upstate Clothing Rules [T2]

**Situation:** Vendor operates in Saratoga County and asks about the clothing exemption.

**Resolution:** While the STATE clothing exemption (under $110) applies statewide, individual counties may choose whether to also exempt clothing from their local tax. Most counties follow the state exemption, but some may not. Check the specific county's local law. NYC exempts clothing from both state and local tax. Flag for reviewer for non-NYC counties.

### EC5 -- SaaS Taxability [T1]

**Situation:** A business subscribes to a cloud-based CRM (SaaS). No software is downloaded.

**Resolution:** TAXABLE in New York. NYS treats SaaS as a sale of pre-written computer software regardless of delivery method. Tax Law Section 1101(b)(6); TSB-A-13(22)S. Collect sales tax at the rate applicable to the customer's location.

### EC6 -- Empire State Film Production Credit Purchases [T2]

**Situation:** A film production company claims sales tax exemption on purchases used in production.

**Resolution:** Qualifying film, television, and commercial productions may be exempt from sales tax on certain production-related purchases. Requires a qualifying certificate from Empire State Development. Complex area -- flag for reviewer.

### EC7 -- Clothing During Back-to-School Period [T1]

**Situation:** Retailer asks if New York has a sales tax holiday for clothing.

**Resolution:** New York does NOT have a temporary sales tax holiday. The clothing exemption (under $110/item) is permanent and year-round. This differs from states like Texas that have temporary holiday periods.

### EC8 -- Restaurant Receipts: Food vs. Drink [T1]

**Situation:** Restaurant receipt shows food and beverages.

**Resolution:** ALL food and drink sold by restaurants (including nontaxable grocery items like bottled water) becomes TAXABLE when sold as part of a restaurant meal. Tax Law Section 1105(d). The restaurant context overrides the grocery food exemption.

### EC9 -- Vendor Purchases for Own Use [T1]

**Situation:** A retailer withdraws merchandise from inventory for personal use or business use (e.g., office supplies).

**Resolution:** The withdrawal is a taxable event. The retailer must report and pay use tax on the cost of the items. Tax Law Section 1105(a) and Section 1110.

### EC10 -- Digital Advertising and Information Services [T2]

**Situation:** A business purchases an online information service (e.g., Bloomberg Terminal, legal research database).

**Resolution:** Information services are TAXABLE in New York under Tax Law Section 1105(c)(1). However, certain information services are exempt if they meet specific criteria (e.g., personal or individual information not substantially incorporated in reports to others). The line between taxable information services and exempt professional services requires analysis. Flag for reviewer.

---

## Test Suite

### Test 1 -- Clothing Under $110 in NYC [T1]

**Input:** Customer buys a $95 pair of shoes in Manhattan. NYC combined rate: 8.875%.
**Expected output:** Sales tax = $0. Clothing under $110 exempt from both state and NYC local tax.

### Test 2 -- Clothing Over $110 in NYC [T1]

**Input:** Customer buys a $200 jacket in Manhattan. NYC combined rate: 8.875%.
**Expected output:** Sales tax = $17.75 ($200 x 8.875%). Full tax applies since item is $110 or more.

### Test 3 -- Grocery Food Exemption [T1]

**Input:** Customer purchases $100 of groceries (bread, milk, produce) from a supermarket.
**Expected output:** Sales tax = $0. Grocery food exempt.

### Test 4 -- SaaS Subscription [T1]

**Input:** NYC business subscribes to a project management SaaS tool for $100/month. No download.
**Expected output:** Sales tax = $8.88 ($100 x 8.875%). SaaS is taxable in New York.

### Test 5 -- Economic Nexus Analysis [T1]

**Input:** Out-of-state seller had $600,000 in NY gross receipts and 80 transactions in the prior four quarterly periods.
**Expected output:** Seller does NOT have economic nexus. Although revenue exceeds $500,000, the transaction count (80) does not exceed 100. New York requires BOTH thresholds to be met.

### Test 6 -- Economic Nexus -- Both Met [T1]

**Input:** Out-of-state seller had $600,000 in NY gross receipts and 150 transactions in the prior four quarterly periods.
**Expected output:** Seller HAS economic nexus. Both $500,000 revenue AND 100 transaction thresholds exceeded. Must register for Certificate of Authority.

### Test 7 -- Resale Certificate [T1]

**Input:** Retailer purchases $10,000 of inventory from a NY wholesaler. Provides valid ST-120 resale certificate.
**Expected output:** No sales tax charged. Retailer collects tax at point of resale.

### Test 8 -- Restaurant Meal [T1]

**Input:** Customer orders a $50 dinner at a NYC restaurant (including bottled water that would be exempt at a grocery store).
**Expected output:** Sales tax = $4.44 ($50 x 8.875%). ALL items in a restaurant meal are taxable, including otherwise exempt items.

### Test 9 -- Manufacturing Equipment [T1]

**Input:** Manufacturer purchases a $200,000 machine used directly and predominantly in production at a Buffalo factory. Erie County rate: 8%.
**Expected output:** Sales tax = $0. Manufacturing equipment used directly and predominantly in production is exempt under Section 1115(a)(12).

### Test 10 -- Use Tax on Out-of-State Purchase [T1]

**Input:** NYC business purchases $5,000 of office furniture from a New Hampshire retailer (no sales tax state). No tax collected.
**Expected output:** Use tax = $443.75 ($5,000 x 8.875%). Report on ST-100 or IT-201.

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
| NYS DTF Main | https://www.tax.ny.gov |
| Online Filing | https://www.tax.ny.gov/online/ |
| Rate Lookup | https://www.tax.ny.gov/bus/st/stidx.htm |
| Phone | 518-485-2889 |
| Certificate of Authority Application | Online via NY Business Express |
| Tax Bulletins | https://www.tax.ny.gov/pubs_and_bulls/tg_bulletins/st/sales_tax_background.htm |
| Advisory Opinions | https://www.tax.ny.gov/pubs_and_bulls/advisory_opinions/sales.htm |
| Audit Information | https://www.tax.ny.gov/bus/aud/aud.htm |

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
