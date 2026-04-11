---
name: florida-sales-tax
description: Use this skill whenever asked about Florida sales and use tax, DOR filings, Florida discretionary surtax, Florida exemptions, Florida nexus, Florida commercial rent tax, or any request involving Florida state sales and use tax compliance. Trigger on phrases like "Florida sales tax", "FL sales tax", "Florida DOR", "DR-15", "Florida surtax", "Florida commercial rent", "Florida resale certificate", or any request involving Florida sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any Florida sales tax work.
---

# Florida Sales and Use Tax Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Florida, United States |
| Jurisdiction Code | US-FL |
| Tax Type | Sales and Use Tax + Discretionary Sales Surtax |
| Primary Legislation | Chapter 212, Florida Statutes (Tax on Sales, Use, and Other Transactions) |
| Key Statutes | F.S. Sections 212.01-212.21 |
| Tax Authority | Florida Department of Revenue (DOR) |
| Filing Portal | https://floridarevenue.com/taxes/Pages/default.aspx |
| Federal Framework Skill | us-sales-tax (read first for Wayfair, nexus overview, and multi-state context) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires Florida CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate structure, basic taxability, filing mechanics, nexus thresholds, commercial rent tax. Tier 2: SaaS/communication services, mixed transactions, surtax cap. Tier 3: audit defense, complex bundled transactions, DOR rulings. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to a licensed tax professional and document the gap.

---

## Step 0: Client Onboarding Questions

Before performing any Florida sales tax work, collect the following from the client:

| # | Question | Why It Matters |
|---|----------|----------------|
| 1 | What is your Florida Sales Tax Certificate of Registration number (DR-11)? | Required for filing; confirms registration with FL DOR. [T1] |
| 2 | What is your assigned filing frequency (monthly, quarterly, semi-annual, annual)? | Determines return due dates. [T1] |
| 3 | What type of nexus do you have in Florida (physical, economic, both)? | Economic nexus threshold is $100,000 in taxable remote sales. [T1] |
| 4 | Do you sell through any marketplace facilitators (Amazon, eBay, Etsy, etc.)? | Marketplace providers collect tax on facilitated sales. [T1] |
| 5 | Do you lease or sublease commercial real property? | Florida is the ONLY state that taxes commercial rent (currently 2.0%). [T1] |
| 6 | Do you operate transient rental accommodations (Airbnb, VRBO, hotels)? | Subject to 6% state tax + surtax + county tourist development tax. [T1] |
| 7 | In which county do you primarily operate? | Discretionary surtax rates vary by county (0% -- 1.5%). [T1] |
| 8 | Do you sell telecommunications, cable, or internet services? | Communication Services Tax (CST) is separate from sales tax -- escalate to [T3]. [T3] |

---

## Step 1: Tax Rate Structure [T1]

### 1.1 State Rate

The Florida state sales and use tax rate is **6%**. [T1]

**Legislation:** F.S. Section 212.05(1)(a).

### 1.2 Discretionary Sales Surtax [T1]

| Parameter | Value |
|-----------|-------|
| Surtax rate range | 0% -- 1.5% depending on county [T1] |
| Combined maximum | 7.5% (6% state + 1.5% county maximum) [T1] |
| Surtax $5,000 cap | Most surtaxes apply only to the first $5,000 of any single taxable item (F.S. Section 212.054(2)(b)) [T1] |

### 1.3 Key County Rates [T1]

| County | Surtax Rate | Combined Rate |
|--------|------------|---------------|
| Miami-Dade | 1.00% | 7.00% |
| Broward | 1.00% | 7.00% |
| Orange (Orlando) | 0.50% | 6.50% |
| Hillsborough (Tampa) | 1.50% | 7.50% |
| Duval (Jacksonville) | 1.50% | 7.50% |
| Palm Beach | 1.00% | 7.00% |
| Leon (Tallahassee) | 1.50% | 7.50% |

### 1.4 Sourcing Rules [T1]

| Scenario | Rate Applied |
|----------|-------------|
| Shipped goods | Surtax rate at delivery address (destination-based) [T1] |
| State rate | 6% uniform statewide; only surtax varies [T1] |

---

## Step 2: Transaction Classification Rules [T1/T2]

### 2.1 Tangible Personal Property (TPP) [T1]

All sales of TPP are taxable unless specifically exempted. F.S. Section 212.05. Includes: electronics, appliances, furniture, equipment, vehicles, clothing and footwear (**NO clothing exemption**), building materials, jewelry, sporting goods, office supplies. [T1]

### 2.2 Food and Beverages [T1]

| Category | Taxable? | Citation |
|----------|----------|----------|
| Grocery food (unprepared, for home consumption) | **EXEMPT** | F.S. Section 212.08(1) |
| Prepared food (heated, served for on-premises) | **TAXABLE** | F.S. Section 212.08(1)(a) |
| Candy | **EXEMPT** (as food) | F.S. Section 212.08(1) |
| Soft drinks (not served at restaurant) | **EXEMPT** (as food) | F.S. Section 212.08(1) |
| Bakery items (unheated, to go) | **EXEMPT** | F.S. Section 212.08(1) |
| Alcoholic beverages | **TAXABLE** | F.S. Section 212.05 |
| Restaurant meals | **TAXABLE** | F.S. Section 212.08(1)(a) |

### 2.3 Taxable Services [T1/T2]

| Taxable Service | Statute |
|----------------|---------|
| Nonresidential pest control | F.S. Section 212.05(1)(i) |
| Nonresidential cleaning/janitorial | F.S. Section 212.05(1)(i) |
| Burglar protection/security | F.S. Section 212.05(1)(i) |
| Nonresidential detective/investigation | F.S. Section 212.05(1)(i) |
| Commercial rent (unique to FL) | F.S. Section 212.031 |
| Transient accommodations | F.S. Section 212.03 |
| Admissions/amusements | F.S. Section 212.04 |

**Nontaxable services:** Professional services (legal, accounting, medical, engineering, consulting), personal care, advertising, transportation, construction labor. [T1]

### 2.4 Commercial Rent Tax -- UNIQUE TO FLORIDA [T1]

| Parameter | Value |
|-----------|-------|
| Rate | 2.0% on total rent or license fee for commercial real property [T1] |
| Surtax | County discretionary surtax also applies on top of 2% rate [T1] |
| Applies to | Office space, retail space, warehouse space, commercial leases [T1] |
| Does NOT apply to | Residential rent [T1] |
| Responsible party | Landlord collects from tenant and remits to DOR [T1] |
| Subleases | Also subject to commercial rent tax [T1] |
| Authority | F.S. Section 212.031 |

**Rate phase-down history:**

| Effective Date | Rate |
|---------------|------|
| Before Dec 2018 | 5.7% |
| Jan 1, 2019 | 5.5% |
| Dec 1, 2023 | 4.5% |
| June 1, 2024 | 2.0% |

**Note:** The Legislature may continue to reduce or eliminate this tax. Always verify the current rate. [T2]

**Taxable commercial rents include:** Office space leases, retail store leases, warehouse/distribution center leases, parking lots/garages (commercial), storage facilities (commercial), billboard/signage space, cell tower ground leases. [T1]

**Exempt from commercial rent tax:** Residential apartment/house rentals [T1], agricultural land leases (certain qualifying) [T2], government-owned property leased for public purposes [T2].

### 2.5 SaaS and Digital Goods [T2]

| Product | Taxable? | Notes |
|---------|----------|-------|
| Canned software (physical media) | **TAXABLE** | TPP [T1] |
| Canned software (electronic download) | **TAXABLE** | DOR Rule 12A-1.032 [T1] |
| Custom software (electronic delivery) | **TAXABLE** | Florida taxes custom software too [T1] |
| SaaS (cloud-hosted) | **TAXABLE** | Florida treats SaaS as license of software; TAA guidance [T2] |
| Streaming services | **TAXABLE** (as communication services) | CST applies separately -- see below [T3] |
| Digital books/music/movies | **TAXABLE** (if download) | Treated as TPP [T1] |

**Communication Services Tax (CST):** Florida imposes a separate CST on telecommunications, video, and related services. CST has its own rates (state + local, totaling approximately 7-14%). CST compliance is outside the scope of this skill. [T3]

### 2.6 Clothing [T1]

Clothing is **fully taxable** in Florida. No general clothing exemption. [T1]

**Exception:** Florida holds an annual Back-to-School Sales Tax Holiday (typically July-August). Clothing items under a set threshold (typically $100/item) are exempt, along with school supplies and certain electronics. F.S. Section 212.08(7)(gg) or current year's legislation. [T1]

---

## Step 3: Return Form Structure [T1]

### 3.1 Filing Forms

| Form | Name | Use |
|------|------|-----|
| DR-15 | Sales and Use Tax Return | Primary return [T1] |
| DR-15EZ | Sales and Use Tax Return (Short Form) | Small dealers [T1] |
| DR-15CS | Communication Services Tax Return | Separate from sales tax [T3] |
| DR-15MO | Solid Waste and Surcharge Return | Solid waste [T1] |

### 3.2 Use Tax Reporting [T1]

| Rule | Detail |
|------|--------|
| When use tax applies | TPP/taxable services from seller without FL tax; TPP purchased tax-free and diverted to taxable use; TPP imported into FL for use/storage/consumption [T1] |
| Use tax rate | 6% state + applicable county surtax at location of use [T1] |
| Credit for tax paid to other states | Credit allowed under F.S. Section 212.06(7) [T1] |

---

## Step 4: Deductibility / Exemptions [T1/T2]

### 4.1 Common Exemptions

| Exemption | Statute | Notes | Tier |
|-----------|---------|-------|------|
| Grocery food | F.S. Sec. 212.08(1) | Unprepared food for home consumption | [T1] |
| Prescription drugs | F.S. Sec. 212.08(2) | Prescribed by practitioner | [T1] |
| OTC drugs and medicine | **TAXABLE** | No general OTC exemption | [T1] |
| Prosthetic/orthopedic devices | F.S. Sec. 212.08(2) | Medical devices | [T1] |
| Agricultural supplies/equipment | F.S. Sec. 212.08(3) | Farming use | [T1] |
| Manufacturing machinery | F.S. Sec. 212.08(5)(b) | Industrial machinery/equipment | [T1] |
| Resale | F.S. Sec. 212.18(3) | Goods purchased for resale | [T1] |
| Interstate commerce | F.S. Sec. 212.06(5)(a) | Goods shipped out of state | [T1] |
| Federal/state government | F.S. Sec. 212.08(6) | Government purchases | [T1] |
| Containers/packaging | F.S. Sec. 212.08(7)(c) | Used to package goods for sale | [T1] |
| Aircraft parts/modification | F.S. Sec. 212.08(7)(ff) | Qualifying aviation maintenance | [T1] |

### 4.2 Manufacturing Exemption [T1]

| Parameter | Detail |
|-----------|--------|
| Scope | Broad exemption for industrial machinery and equipment [T1] |
| Qualification | Used at a fixed location in FL for manufacturing, processing, compounding, or producing TPP for sale [T1] |
| Includes | Repair parts and labor for qualifying equipment [T1] |
| Includes | Industrial utility services (electricity, water, natural gas) for qualified manufacturers [T1] |
| Certificate | Annual Resale Certificate for Tax on Purchases (DR-13) [T1] |
| Authority | F.S. Section 212.08(5)(b); F.S. Section 212.08(5)(e) |

### 4.3 Resale Exemption [T1]

| Parameter | Detail |
|-----------|--------|
| Form | DR-13 (Annual Resale Certificate for Sales Tax) [T1] |
| Renewal | Issued annually; valid for the calendar year printed on it [T1] |
| Multi-state accepted | MTC Uniform Sales Tax Certificate accepted [T1] |
| SST Certificate | NOT accepted -- FL is not an SST member [T1] |

### 4.4 Nonprofit Exemptions [T2]

| Parameter | Detail |
|-----------|--------|
| Certificate | Consumer's Certificate of Exemption from FL DOR [T2] |
| Qualifying organizations | 501(c)(3) entities with DOR approval [T2] |
| Scope | Covers purchases by the organization; taxable sales remain taxable [T2] |

### 4.5 Exemption Certificates [T1]

| Certificate | Form | Purpose |
|------------|------|---------|
| Annual resale | DR-13 | Purchases for resale (renewed annually) [T1] |
| Exempt organization | DR-14 | Qualifying exempt organization purchases (has expiration date) [T1] |

---

## Step 5: Key Thresholds [T1]

### 5.1 Economic Nexus Threshold [T1]

| Parameter | Value |
|-----------|-------|
| Revenue threshold | More than $100,000 in taxable remote sales into FL [T1] |
| Transaction count threshold | **None** -- revenue only [T1] |
| Measurement period | Previous calendar year [T1] |
| Effective date | July 1, 2021 [T1] |
| Sales included | Only taxable sales count [T1] |
| Marketplace exclusion | Marketplace sales facilitated by a marketplace provider do not count toward seller's threshold [T1] |
| Authority | F.S. Section 212.0596 |

**Note:** Florida was one of the last states to enact economic nexus (2021). [T1]

### 5.2 Registration Requirements [T1]

| Requirement | Detail |
|------------|--------|
| Who must register | Any dealer (seller) required to collect FL sales tax (F.S. Section 212.18) [T1] |
| Certificate | Florida Sales Tax Certificate of Registration (DR-11) [T1] |

### 5.3 Marketplace Facilitator Rules [T1]

| Rule | Detail |
|------|--------|
| Effective date | July 1, 2021 [T1] |
| Definition | Person who facilitates retail sale of seller's items through a marketplace (F.S. Section 212.05965) [T1] |
| Obligation | Marketplace providers with FL nexus must collect tax on behalf of sellers [T1] |

### 5.4 No State Income Tax [T1]

Florida has no state personal income tax. Florida does impose a corporate income/franchise tax (currently 5.5% on federal taxable income apportioned to Florida), but this is outside the scope of this skill. [T3]

### 5.5 Surtax $5,000 Cap [T1]

The discretionary sales surtax generally applies only to the first $5,000 of any single item's sales price. F.S. Section 212.054(2)(b). [T1]

**Example:** A $10,000 item in a county with 1% surtax: State tax (6%): $600.00. Surtax (1%): $50.00 (on first $5,000 only). Total tax: $650.00.

---

## Step 6: Filing Deadlines and Penalties [T1]

### 6.1 Filing Frequency

| Frequency | Criteria | Due Date |
|-----------|----------|----------|
| Monthly | Tax due > $1,000/year | 1st-20th of the following month [T1] |
| Quarterly | Tax due $501-$1,000/year | 1st-20th of the month following the quarter [T1] |
| Semi-annual | Tax due $101-$500/year | 1st-20th of the month following the semi-annual period [T1] |
| Annual | Tax due $100 or less/year | 1st-20th of January following the year [T1] |

**Note:** If the 20th falls on a weekend or holiday, the due date extends to the next business day. [T1]

**Legislation:** F.S. Section 212.11.

### 6.2 Collection Allowance (Vendor Discount) [T1]

| Parameter | Value |
|-----------|-------|
| Rate | 2.5% of the first $1,200 of tax due per return [T1] |
| Maximum | $30 per return [T1] |
| Authority | F.S. Section 212.12(1) |

### 6.3 Electronic Filing [T1]

| Rule | Detail |
|------|--------|
| Mandatory e-filing | Dealers who paid $20,000+ in sales tax in prior state fiscal year (July 1 -- June 30) (F.S. Section 213.755) [T1] |
| All others | May file electronically or on paper [T1] |

### 6.4 Penalties and Interest [T1]

| Penalty | Rate | Citation |
|---------|------|----------|
| Late filing (1-30 days) | 10% of tax due (min $50) | F.S. Sec. 212.12(2) [T1] |
| Late filing (> 30 days) | Additional 10% per month (max 50%) | F.S. Sec. 212.12(2) [T1] |
| Fraud | 100% of tax deficiency | F.S. Sec. 212.12(2)(c) [T1] |
| Interest | Floating rate set by DOR | F.S. Sec. 213.235 [T1] |
| Failure to register | Misdemeanor; $250-$5,000 fine | F.S. Sec. 212.18(3)(e) [T1] |

### 6.5 Record Retention [T1]

| Parameter | Value |
|-----------|-------|
| Retention period | Minimum 3 years from the date the return was filed [T1] |
| Authority | F.S. Section 212.13(4) |

### 6.6 Statute of Limitations [T1]

| Scenario | Limitation Period |
|----------|------------------|
| Standard assessment | 3 years from filing or due date [T1] |
| No return filed | No limitation [T1] |
| Fraud | No limitation [T1] |

### 6.7 Audit Considerations [T2]

| Factor | Detail |
|--------|--------|
| Audit types | Desk audits and field audits [T1] |
| High-risk industries | Restaurants, bars, retail (high cash transactions) [T2] |
| DR-13 requirement | Must be for the correct year -- expired certificates do not protect the seller [T1] |
| Landlord audits | Landlords frequently audited for commercial rent tax compliance [T2] |

---

## Step 7: Florida-Specific Rules [T1/T2]

### 7.1 Boat and Aircraft Tax Caps [T2]

| Parameter | Detail |
|-----------|--------|
| Boat tax cap | $18,000 maximum state tax regardless of price (F.S. Section 212.05(1)(a)2.a.) [T2] |
| Aircraft | Separate cap applies [T2] |
| Surtax | Subject to the $5,000 cap [T1] |
| Guidance | Flag for reviewer for exact cap amounts as they are subject to legislative change [T2] |

### 7.2 Detailed Taxability Matrix [T1]

| Category | Taxable? | State Rate | Surtax? | Key Statute |
|----------|----------|-----------|---------|-------------|
| General TPP | Yes | 6% | Yes (up to 1.5%) | F.S. 212.05 |
| Grocery food (unprepared) | No | Exempt | N/A | F.S. 212.08(1) |
| Prepared food / restaurant | Yes | 6% | Yes | F.S. 212.08(1)(a) |
| Candy (not at restaurant) | No | Exempt | N/A | F.S. 212.08(1) |
| Soft drinks (not at restaurant) | No | Exempt | N/A | F.S. 212.08(1) |
| Prescription medicine | No | Exempt | N/A | F.S. 212.08(2) |
| OTC medicine | Yes | 6% | Yes | No general exemption |
| Clothing (all items) | Yes | 6% | Yes | No exemption |
| Canned software (any delivery) | Yes | 6% | Yes | DOR Rule 12A-1.032 |
| Custom software | Yes | 6% | Yes | FL taxes custom too |
| SaaS (cloud) | Yes | 6% | Yes | TAA guidance |
| Manufacturing equipment | No | Exempt | N/A | F.S. 212.08(5)(b) |
| Agricultural equipment | No | Exempt | N/A | F.S. 212.08(3) |
| Resale purchases | No | Exempt | N/A | F.S. 212.18(3) |
| Interstate shipments | No | Exempt | N/A | F.S. 212.06(5)(a) |
| Commercial rent | Yes | 2% | Yes | F.S. 212.031 |
| Residential rent | No | Exempt | N/A | Not subject |
| Transient accommodations | Yes | 6% | Yes + tourist tax | F.S. 212.03 |
| Boats (purchase) | Yes (capped) | 6% ($18K max) | Yes ($5K cap) | F.S. 212.05(1)(a)2 |
| Aircraft | Yes (capped) | 6% (capped) | Yes ($5K cap) | F.S. 212.05(1)(a)2 |
| Telecom/cable/phone | CST | Separate tax | Separate | F.S. Ch. 202 |
| Admissions/amusements | Yes | 6% | Yes | F.S. 212.04 |

---

## PROHIBITIONS [T1]

- **NEVER** apply a clothing exemption in Florida -- clothing is fully taxable (except during sales tax holidays). [T1]
- **NEVER** forget the $5,000 surtax cap on single items -- surtax applies only to the first $5,000 per item. [T1]
- **NEVER** ignore the commercial rent tax -- Florida is the ONLY state that taxes commercial rent. [T1]
- **NEVER** confuse the Communication Services Tax (CST) with general sales tax -- they are separate taxes with separate returns. [T1]
- **NEVER** treat the tourist development tax as part of the DR-15 return -- it is reported separately to the county. [T1]
- **NEVER** assume the DR-13 resale certificate is perpetual -- it must be renewed annually. [T1]
- **NEVER** accept the SST Certificate in Florida -- FL is not an SST member. [T1]
- **NEVER** assume residential rent is taxable -- only COMMERCIAL rent is subject to the rent tax. [T1]
- **NEVER** overlook the boat/aircraft tax cap when computing tax on large vessel or aircraft purchases. [T2]
- **NEVER** fail to claim the collection allowance when filing on time. [T1]

---

## Edge Case Registry [T1/T2]

### EC1 -- Commercial Rent Tax Calculation [T1]

**Situation:** Business leases office space in Miami-Dade County for $5,000/month.

**Resolution:** Commercial rent tax at 2.0% + Miami-Dade surtax (1.0%) = 3.0% total on rent. Monthly tax = $5,000 x 3.0% = $150.00. Landlord collects and remits. F.S. Section 212.031.

### EC2 -- Surtax $5,000 Cap [T1]

**Situation:** A customer purchases a $20,000 piece of equipment in Hillsborough County (1.5% surtax).

**Resolution:** State tax (6%): $20,000 x 6% = $1,200.00. Surtax: $5,000 x 1.5% = $75.00 (capped at first $5,000 per item). Total tax: $1,275.00. Without the cap, surtax would be $300.

### EC3 -- Transient Rental Accommodations (Airbnb/VRBO) [T1]

**Situation:** Property owner rents a vacation home for $200/night through Airbnb.

**Resolution:** Transient rentals (6 months or less) are subject to: (a) 6% state sales tax, (b) county surtax, and (c) county tourist development tax (varies by county, typically 2-6%). The state sales tax and surtax are reported on DR-15. The tourist development tax is reported separately to the county. Airbnb collects state tax in Florida but may not collect all local taxes. F.S. Sections 212.03, 125.0104.

### EC4 -- Aircraft and Boat Purchases [T2]

**Situation:** Florida resident purchases a boat for $500,000.

**Resolution:** Boats and aircraft are subject to Florida sales tax. A $18,000 cap applies to sales tax on boats (F.S. Section 212.05(1)(a)2.a.), meaning the maximum state tax on a boat is $18,000 regardless of the price. Aircraft have a separate cap. County surtax is subject to the $5,000 cap. Flag for reviewer for exact cap amounts as they are subject to legislative change.

### EC5 -- Bundled Cable/Internet/Phone [T2]

**Situation:** Customer subscribes to a bundled service that includes cable TV, internet, and phone.

**Resolution:** These services are subject to the Communication Services Tax (CST), which is a separate tax from the general sales tax. CST has its own rates and filing requirements (Form DR-15CS). This is outside the scope of this skill -- escalate to [T3].

### EC6 -- Sales Tax Holiday (Back-to-School) [T1]

**Situation:** Customer purchases school supplies during the annual back-to-school holiday.

**Resolution:** Florida typically declares an annual back-to-school sales tax holiday (usually July-August). During this period, qualifying items are exempt: clothing under a set threshold, school supplies under a set threshold, and certain computers/accessories. Specific thresholds vary by year and are set by the Legislature. Verify current year's legislation.

### EC7 -- Voluntary Disclosure Program [T2]

**Situation:** An out-of-state business realizes it has had nexus in Florida for several years without collecting tax.

**Resolution:** Florida DOR offers an informal voluntary disclosure program. Benefits typically include waiver of penalties and a limited lookback period (usually 3 years). Must be initiated before DOR contacts the business. Flag for reviewer.

### EC8 -- Amusement Machine Receipts [T1]

**Situation:** Business operates coin-operated amusement machines.

**Resolution:** Receipts from amusement machines are subject to sales tax. F.S. Section 212.05(1)(h). The operator reports the gross receipts on the DR-15 return.

### EC9 -- Condo Association Assessments [T2]

**Situation:** Condominium association charges monthly maintenance assessments to unit owners.

**Resolution:** General maintenance assessments by residential condo associations are NOT subject to sales tax. However, specific charges for taxable services (e.g., pest control, security) may be taxable if charged separately. Flag for reviewer if the assessment bundles taxable and nontaxable items.

### EC10 -- Motor Vehicle Private Sale [T1]

**Situation:** Individual sells a used car to another individual in Florida.

**Resolution:** Sales tax of 6% (plus surtax) is due. The buyer pays the tax to the county tax collector at the time of title transfer and registration. F.S. Section 212.05(1)(a)1.b.

---

## Test Suite

### Test 1 -- Basic Taxable Sale in Miami [T1]

**Input:** Retailer sells a laptop for $1,200 in Miami-Dade County (7.00% combined). Single item.
**Expected output:** State tax = $72.00 ($1,200 x 6%). Surtax = $12.00 ($1,200 x 1% -- under $5,000 cap). Total tax = $84.00. Total charged = $1,284.00.

### Test 2 -- Grocery Food Exemption [T1]

**Input:** Customer buys $200 of groceries (bread, milk, produce) at a Florida supermarket.
**Expected output:** Sales tax = $0. Grocery food is exempt. F.S. Section 212.08(1).

### Test 3 -- Commercial Rent [T1]

**Input:** Business pays $10,000/month for office space in Orange County (0.5% surtax). Commercial rent tax rate: 2.0%.
**Expected output:** State rent tax = $200.00 ($10,000 x 2.0%). Surtax on rent = $50.00 ($10,000 x 0.5%). Total monthly tax on rent = $250.00.

### Test 4 -- Surtax Cap on Large Purchase [T1]

**Input:** Business purchases $50,000 machine in Duval County (1.5% surtax). Single item.
**Expected output:** State tax = $3,000.00 ($50,000 x 6%). Surtax = $75.00 ($5,000 x 1.5% -- capped). Total = $3,075.00.

### Test 5 -- Out-of-State Seller Nexus [T1]

**Input:** California-based e-commerce seller had $120,000 in taxable Florida sales last calendar year.
**Expected output:** Exceeds $100,000 economic nexus threshold. Must register with FL DOR and collect tax.

### Test 6 -- Clothing Sale [T1]

**Input:** Customer buys a $150 dress in Broward County (7.00% combined).
**Expected output:** Sales tax = $10.50 ($150 x 7%). Clothing is fully taxable. No clothing exemption.

### Test 7 -- Transient Rental [T1]

**Input:** Vacation rental in Osceola County for 7 nights at $250/night. State rate 6%, surtax 0.5%, tourist development tax 6%.
**Expected output:** Gross rental = $1,750. State sales tax = $105.00. Surtax = $8.75. Tourist development tax = $105.00 (reported separately to county). Total state + surtax on DR-15 = $113.75.

### Test 8 -- Resale Certificate [T1]

**Input:** Retailer purchases $8,000 of inventory from a Florida wholesaler. Provides valid DR-13 for current year.
**Expected output:** No sales tax charged. Retailer collects tax at resale.

### Test 9 -- SaaS Subscription [T2]

**Input:** Florida business subscribes to a cloud-based HR platform (SaaS). $200/month. No download. Miami-Dade (7%).
**Expected output:** Generally TAXABLE in Florida as a license to use software. Tax = $14.00/month. However, the exact treatment of cloud-only SaaS is evolving -- flag for reviewer if the product is purely cloud-hosted with no download component.

### Test 10 -- Vendor Discount [T1]

**Input:** Dealer files DR-15 on time with $800 in tax due.
**Expected output:** Collection allowance = 2.5% of $800 = $20.00. Net remittance = $780.00. (Within the $30 max.)

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
| FL DOR Main | https://floridarevenue.com |
| Online Filing | https://floridarevenue.com/taxes/eservices/Pages/default.aspx |
| Rate Lookup | https://floridarevenue.com/taxes/taxesfees/Pages/discretionary.aspx |
| Phone | 850-488-6800 |
| Registration | Online via FL DOR website |
| Tax Information Publications | https://floridarevenue.com/taxes/tips/Pages/default.aspx |
| Commercial Rent Tax Info | https://floridarevenue.com/taxes/taxesfees/Pages/commercial_rental.aspx |
| Surtax Rates by County | https://floridarevenue.com/taxes/taxesfees/Pages/discretionary.aspx |

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
