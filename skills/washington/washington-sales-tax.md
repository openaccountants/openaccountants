---
name: washington-sales-tax
description: Use this skill whenever asked about Washington State sales and use tax, WA DOR filings, B&O tax overview, Washington digital goods tax, Washington exemptions, Washington nexus, or any request involving Washington state sales and use tax compliance. Trigger on phrases like "Washington sales tax", "WA sales tax", "Washington DOR", "B&O tax", "Washington use tax", "Washington digital goods", "Washington resale certificate", or any request involving Washington sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any Washington sales tax work.
---

# Washington State Sales and Use Tax Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Washington, United States |
| Jurisdiction Code | US-WA |
| Tax Type | Sales and Use Tax (state + local); Business and Occupation (B&O) Tax (separate) |
| Primary Legislation | Revised Code of Washington (RCW) Chapter 82.08 (Retail Sales Tax); RCW Chapter 82.12 (Use Tax); RCW Chapter 82.04 (B&O Tax) |
| Key Statutes | RCW 82.08.010-82.08.965; RCW 82.12.010-82.12.965 |
| Tax Authority | Washington State Department of Revenue (DOR) |
| Filing Portal | https://dor.wa.gov |
| SST Membership | Yes -- Washington is a full member of the Streamlined Sales Tax (SST) |
| Federal Framework Skill | us-sales-tax (read first for Wayfair, nexus overview, and multi-state context) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires Washington CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate structure, basic taxability, digital goods, filing mechanics, nexus thresholds. Tier 2: B&O tax classification, mixed transactions, local rate lookups. Tier 3: audit defense, complex bundled transactions, DOR rulings. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to a licensed tax professional and document the gap.

---

## Step 0: Client Onboarding Questions

Before performing any Washington sales tax work, collect the following from the client:

| # | Question | Why It Matters |
|---|----------|----------------|
| 1 | What is your Washington UBI (Unified Business Identifier) number? | Required for filing; confirms registration with WA DOR. [T1] |
| 2 | What is your assigned filing frequency (monthly, quarterly, annual)? | Determines return due dates. [T1] |
| 3 | What type of nexus do you have in Washington (physical, economic, both)? | Economic nexus threshold is $100,000 in gross receipts (revenue only). [T1] |
| 4 | Do you sell through any marketplace facilitators (Amazon, eBay, Etsy, etc.)? | Marketplace facilitators collect tax on facilitated sales. [T1] |
| 5 | Do you sell digital products, SaaS, or streaming services? | Washington taxes virtually ALL digital products very broadly. [T1] |
| 6 | Do you sell custom software? | Unlike most states, WA taxes custom software delivered electronically. [T1] |
| 7 | Do you understand your B&O tax obligations? | B&O tax (gross receipts tax) applies IN ADDITION to sales tax on the same transaction. [T1] |
| 8 | What is your primary delivery/sales location? | WA is destination-based for ALL sales; hundreds of local rate jurisdictions exist. [T1] |

---

## Step 1: Tax Rate Structure [T1]

### 1.1 State Rate

The Washington State sales and use tax rate is **6.5%**. [T1]

**Legislation:** RCW 82.08.020.

### 1.2 Local Taxes [T1]

| Component | Range | Notes |
|-----------|-------|-------|
| State rate | 6.5% | Uniform statewide [T1] |
| Local (city + county + transit + special) | 0.5% -- 4.0% | Varies by location [T1] |
| **Combined maximum** | **~10.25%** | In some areas of Seattle and Tacoma [T1] |

### 1.3 Key Combined Rates [T1]

| Jurisdiction | Combined Rate |
|-------------|--------------|
| Seattle | ~10.25% |
| Tacoma | ~10.20% |
| Spokane | ~8.90% |
| Vancouver (Clark County) | ~8.60% |
| Olympia | ~9.00% |
| Unincorporated King County | ~10.10% |

**Legislation:** RCW 82.14 (local taxes).

### 1.4 Sourcing Rules [T1]

| Scenario | Rate Applied |
|----------|-------------|
| Shipped goods | Rate at delivery address (destination-based) [T1] |
| Counter sales | Rate at location of sale [T1] |
| Intrastate sales | Destination-based (WA follows SST sourcing rules) [T1] |
| Interstate sales | Destination-based [T1] |

**Legislation:** RCW 82.32.730 (SST sourcing).

### 1.5 Rate Lookup [T1]

Due to hundreds of local rate jurisdictions, WA DOR provides a tax rate lookup tool: https://dor.wa.gov/taxes-rates/sales-use-tax-rates. DOR assigns a location code to each address for tax reporting purposes. [T1]

---

## Step 2: Transaction Classification Rules [T1/T2]

### 2.1 Tangible Personal Property (TPP) [T1]

All retail sales of TPP are taxable unless specifically exempted. RCW 82.08.020. Includes: electronics, appliances, furniture, equipment, vehicles (sales tax + separate motor vehicle excise taxes), clothing and footwear (**NO clothing exemption**), building materials, jewelry, sporting goods, office supplies. [T1]

### 2.2 Food and Beverages [T1]

| Category | Taxable? | Citation |
|----------|----------|----------|
| Grocery food (unprepared, for home consumption) | **EXEMPT** | RCW 82.08.0293 |
| Prepared food (heated, served with utensils, 2+ food ingredients mixed for sale) | **TAXABLE** | RCW 82.08.0293(2) |
| Candy | **TAXABLE** | RCW 82.08.0293(2)(d) (SST definition) |
| Soft drinks | **TAXABLE** | RCW 82.08.0293(2)(e) |
| Dietary supplements | **TAXABLE** | RCW 82.08.0293(2)(f) |
| Bottled water | **EXEMPT** | RCW 82.08.0293 |
| Alcoholic beverages | **TAXABLE** (plus separate liquor taxes) | |
| Restaurant meals | **TAXABLE** | |

**Washington follows SST definitions** for food, candy, soft drinks, and dietary supplements. [T1]

### 2.3 Services [T1/T2]

Washington generally does NOT tax services. However, certain specific services are taxable:

| Taxable Service | Citation |
|----------------|----------|
| Construction/repair of real property (labor + materials bundled) | RCW 82.04.050(2)(b) [T1] |
| Digital automated services | RCW 82.04.050(6)(b) [T1] |
| Extended warranties/service contracts | RCW 82.04.050(7) [T1] |
| Physical fitness services | RCW 82.04.050(2)(a) [T1] |
| Amusement/recreation services | RCW 82.04.050(2)(a) [T1] |
| Landscape maintenance | Not taxable (B&O only) [T1] |

**Most professional services are NOT subject to sales tax** (but ARE subject to B&O tax). [T1]

### 2.4 SaaS and Digital Goods -- BROADLY TAXED [T1]

| Product | Taxable? | Notes |
|---------|----------|-------|
| Canned software (physical media) | **TAXABLE** | TPP [T1] |
| Canned software (electronic download) | **TAXABLE** | Digital good; RCW 82.04.050(6)(a) [T1] |
| Custom software (electronic delivery) | **TAXABLE** | Also taxable in WA (unlike most states) [T1] |
| SaaS (cloud-hosted) | **TAXABLE** | Digital automated service; RCW 82.04.050(6)(b) [T1] |
| Digital music/movies/books | **TAXABLE** | Digital goods; RCW 82.04.050(6)(a) [T1] |
| Streaming services | **TAXABLE** | Digital automated service [T1] |
| Digital codes (gift cards for digital products) | **TAXABLE** | RCW 82.04.050(6)(c) [T1] |
| Remote access software | **TAXABLE** | Digital automated service [T1] |

**Critical:** Washington taxes virtually ALL digital products, including SaaS, streaming, downloads, and digital automated services accessed remotely. This is the broadest digital tax regime in the US. [T1]

**Legislation:** RCW 82.04.050(6); RCW 82.04.192; WAC 458-20-15503.

### 2.5 Clothing [T1]

Clothing is **fully taxable** in Washington. No clothing exemption. [T1]

### 2.6 Business and Occupation (B&O) Tax -- Context [T1/T3]

| Parameter | Detail |
|-----------|--------|
| Nature | Separate tax from sales tax; gross receipts tax with NO deductions for COGS, labor, or expenses [T1] |
| Scope | Applies to virtually ALL business activity (not just retail sales) [T1] |
| Interaction | A business may owe BOTH B&O tax AND sales tax on the same transaction [T1] |
| Cannot pass to customer | B&O tax cannot be passed on as a separate line item [T1] |
| Detailed compliance | Outside the scope of this skill -- escalate to [T3] |

**B&O tax rates (for context only):**

| Classification | Rate |
|---------------|------|
| Retailing | 0.471% |
| Wholesaling | 0.484% |
| Manufacturing | 0.484% |
| Service & Other | 1.50% |
| International services | 0.275% |
| Royalties | 1.50% |

**B&O tax is reported on the same Combined Excise Tax Return as sales tax.** [T1]

**Legislation:** RCW Chapter 82.04.

---

## Step 3: Return Form Structure [T1]

### 3.1 Filing Form

| Form | Name | Use |
|------|------|-----|
| Combined Excise Tax Return | Covers sales tax, B&O tax, use tax, and other excise taxes | Single return for all state business taxes [T1] |

Filed through **My DOR** (online portal). [T1]

### 3.2 Use Tax Reporting [T1]

| Filer Type | Reporting Method |
|-----------|-----------------|
| Businesses | Report on Combined Excise Tax Return [T1] |
| Individuals | Excise tax return or DOR's consumer use tax filing [T1] |

### 3.3 Use Tax Rules [T1]

| Rule | Detail |
|------|--------|
| When use tax applies | Goods/digital products from seller without WA tax; TPP purchased tax-free diverted to taxable use; TPP/digital goods/services brought into or used in WA [T1] |
| Use tax rate | Combined state and local rate at location of use [T1] |
| Credit for tax paid to other states | Credit allowed under RCW 82.12.035 [T1] |

---

## Step 4: Deductibility / Exemptions [T1/T2]

### 4.1 Common Exemptions

| Exemption | Statute | Notes | Tier |
|-----------|---------|-------|------|
| Grocery food | RCW 82.08.0293 | Unprepared food for home consumption | [T1] |
| Prescription drugs | RCW 82.08.0281 | Prescribed by practitioner | [T1] |
| OTC drugs | **TAXABLE** | No OTC drug exemption in WA | [T1] |
| Prosthetic devices (prescribed) | RCW 82.08.0283 | Medical devices | [T1] |
| Agricultural machinery/equipment | RCW 82.08.0268 | Used in agricultural production | [T1] |
| Manufacturing machinery | RCW 82.08.02565 | M&E exemption (reduced rate or B&O credit) | [T2] |
| Resale | RCW 82.08.030(1) | Goods for resale | [T1] |
| Interstate commerce | RCW 82.08.0273 | Goods shipped out of state | [T1] |
| Federal/state government | RCW 82.08.0255 | Government purchases | [T1] |
| Trade-ins | RCW 82.08.010(1)(c) | Credit for trade-in value | [T1] |
| Motor fuel (separate tax) | RCW 82.08.0255 | Subject to motor fuel tax | [T1] |
| Newspapers (print) | RCW 82.08.0253 | Qualifying publications | [T1] |

### 4.2 Manufacturing M&E Exemption [T2]

| Parameter | Detail |
|-----------|--------|
| Scope | Machinery and equipment used directly in manufacturing [T1] |
| Rate treatment | Sales tax reduced (not fully exempt) -- buyer pays state rate only (6.5%), local tax exempt [T2] |
| Some categories | Full exemption available [T2] |
| Complexity | Complex eligibility requirements -- flag for reviewer [T2] |
| Authority | RCW 82.08.02565 |

### 4.3 Resale Exemption [T1]

| Parameter | Detail |
|-----------|--------|
| Form | Washington Resale Certificate (DOR form) [T1] |
| Requirement | Must include buyer's WA UBI number [T1] |
| SST Certificate | Accepted -- WA is an SST member [T1] |
| MTC Certificate | Accepted [T1] |
| Blanket certificates | Permitted [T1] |

### 4.4 Nonprofit Exemptions [T2]

| Parameter | Detail |
|-----------|--------|
| Scope | Limited sales tax exemptions for certain nonprofits [T2] |
| Blanket exemption? | NO -- specific qualifying criteria apply [T2] |
| Some organizations | Exempt for specific purchases only (e.g., fundraising items for qualifying charities) [T2] |

### 4.5 Exemption Certificates [T1]

| Certificate | Form | Purpose |
|------------|------|---------|
| Resale | WA Resale Certificate | Purchases for resale [T1] |
| Buyer's exemption | Buyers' Retail Sales Tax Exemption Certificate (various forms by type) | Various exemptions [T1] |

---

## Step 5: Key Thresholds [T1]

### 5.1 Economic Nexus Threshold [T1]

| Parameter | Value |
|-----------|-------|
| Revenue threshold | $100,000 in cumulative gross receipts from WA-sourced sales [T1] |
| Transaction count threshold | **None** -- revenue only [T1] |
| Measurement period | Current or preceding calendar year [T1] |
| Effective date | October 1, 2018 (one of the first post-Wayfair states) [T1] |
| Sales included | Gross receipts, including exempt sales [T1] |
| B&O nexus thresholds | Separate [T2] |
| Authority | RCW 82.08.020; RCW 82.04.067 |

### 5.2 Registration Requirements [T1]

| Requirement | Detail |
|------------|--------|
| Who must register | Any person making retail sales in WA (RCW 82.32.030) [T1] |
| Registration type | Washington Business License (includes sales tax registration) [T1] |
| SST registration | Can register through SSTRS at https://www.sstregister.org (covers WA + all other SST states) [T1] |

### 5.3 Marketplace Facilitator Rules [T1]

| Rule | Detail |
|------|--------|
| Effective date | January 1, 2018 (pre-Wayfair, one of the earliest) [T1] |
| Facilitator treated as | Sellers [T1] |
| Seller relief | Sellers relieved for facilitated sales [T1] |
| Authority | RCW 82.08.0531 |

### 5.4 No State Income Tax [T1]

Washington has no state personal income tax and no state corporate income tax. The B&O tax (gross receipts tax) is the primary business tax. Washington also imposes a capital gains tax on sale of certain capital assets (enacted 2021, upheld by WA Supreme Court 2023), but this is outside the scope of this skill. [T3]

---

## Step 6: Filing Deadlines and Penalties [T1]

### 6.1 Filing Frequency

| Frequency | Criteria | Due Date |
|-----------|----------|----------|
| Monthly | Tax liability > set threshold | 25th of the following month [T1] |
| Quarterly | Tax liability between thresholds | 25th of the month following the quarter [T1] |
| Annual | Tax liability below threshold | April 15 following the year [T1] |

### 6.2 Quarterly Due Dates [T1]

| Quarter | Period | Due Date |
|---------|--------|----------|
| Q1 | January 1 -- March 31 | April 25 |
| Q2 | April 1 -- June 30 | July 25 |
| Q3 | July 1 -- September 30 | October 25 |
| Q4 | October 1 -- December 31 | January 25 |

**Legislation:** RCW 82.32.045.

### 6.3 Electronic Filing [T1]

| Rule | Detail |
|------|--------|
| Mandatory e-filing | Most businesses through My DOR (RCW 82.32.080) [T1] |
| Paper filing | Available only for very small businesses by special arrangement [T1] |

### 6.4 Vendor Discount [T1]

Washington does **NOT** offer a vendor discount. Sellers retain no portion of collected tax. [T1]

### 6.5 Penalties and Interest [T1]

| Penalty | Rate | Citation |
|---------|------|----------|
| Late filing | 5% of tax due per month (max 25%) | RCW 82.32.090(1) [T1] |
| Substantial underpayment | 5% of deficiency | RCW 82.32.090(2) [T1] |
| Evasion/fraud | 50% of deficiency | RCW 82.32.090(7) [T1] |
| Interest | Rate set by DOR (adjusted periodically) | RCW 82.32.050 [T1] |

### 6.6 Record Retention [T1]

| Parameter | Value |
|-----------|-------|
| Retention period | Minimum 5 years from the date the return was filed or due, whichever is later [T1] |
| Authority | RCW 82.32.070 |

### 6.7 Statute of Limitations [T1]

| Scenario | Limitation Period |
|----------|------------------|
| Standard assessment | 4 years from filing or due date [T1] |
| No return filed | No limitation [T1] |
| Fraud | No limitation [T1] |

### 6.8 Audit Considerations [T2]

| Factor | Detail |
|--------|--------|
| Key focus | Use tax compliance (self-assessment on out-of-state purchases) [T1] |
| Increasing focus | Digital product taxability [T2] |
| Location codes | Incorrect codes result in misallocated local taxes [T1] |
| Common finding | B&O tax classification errors (e.g., retail vs. wholesale) [T2] |

---

## Step 7: Washington-Specific Rules [T1/T2]

### 7.1 B&O Tax Interaction with Sales Tax [T1]

| Rule | Detail |
|------|--------|
| Dual obligation | A retail business owes BOTH sales tax (collected from customer) AND B&O tax (on gross receipts) [T1] |
| Not duplicative | One is a consumer tax, the other a business tax [T1] |
| Cannot pass B&O to customer | B&O tax cannot be passed on as a separate line item [T1] |
| Combined burden | Sales tax + B&O can be significant for low-margin businesses [T1] |
| B&O reported on | Same Combined Excise Tax Return as sales tax [T1] |

### 7.2 Cannabis Taxation [T1]

| Parameter | Detail |
|-----------|--------|
| Cannabis excise tax | 37% (RCW 69.50.535) [T1] |
| Sales tax | State and local rates also apply [T1] |
| Excise tax treatment | Included in selling price before sales tax is calculated [T1] |
| Complexity | Escalate detailed questions to [T3] |

### 7.3 Detailed Taxability Matrix [T1]

| Category | Taxable? | State Rate | Local Add? | Key Statute |
|----------|----------|-----------|-----------|-------------|
| General TPP | Yes | 6.5% | Yes (up to ~4%) | RCW 82.08.020 |
| Grocery food (unprepared) | No | Exempt | N/A | RCW 82.08.0293 |
| Prepared food / restaurant | Yes | 6.5% | Yes | RCW 82.08.0293(2) |
| Candy (SST: no flour) | Yes | 6.5% | Yes | RCW 82.08.0293(2)(d) |
| Soft drinks | Yes | 6.5% | Yes | RCW 82.08.0293(2)(e) |
| Dietary supplements | Yes | 6.5% | Yes | RCW 82.08.0293(2)(f) |
| Prescription drugs | No | Exempt | N/A | RCW 82.08.0281 |
| OTC drugs | Yes | 6.5% | Yes | No exemption |
| Clothing (all items) | Yes | 6.5% | Yes | No exemption |
| Canned software (any delivery) | Yes | 6.5% | Yes | RCW 82.04.050(6)(a) |
| Custom software (electronic) | Yes | 6.5% | Yes | RCW 82.04.050(6)(a) |
| SaaS / digital automated service | Yes | 6.5% | Yes | RCW 82.04.050(6)(b) |
| Digital music/movies/books | Yes | 6.5% | Yes | RCW 82.04.050(6)(a) |
| Streaming services | Yes | 6.5% | Yes | Digital automated service |
| Digital codes | Yes | 6.5% | Yes | RCW 82.04.050(6)(c) |
| Manufacturing M&E | Partial | Reduced | Varies | RCW 82.08.02565 |
| Farm equipment | No | Exempt | N/A | RCW 82.08.0268 |
| Resale purchases | No | Exempt | N/A | RCW 82.08.030(1) |
| Interstate shipments | No | Exempt | N/A | RCW 82.08.0273 |
| Extended warranties | Yes | 6.5% | Yes | RCW 82.04.050(7) |
| Physical fitness services | Yes | 6.5% | Yes | RCW 82.04.050(2)(a) |
| Professional services | No (sales tax) | B&O only | N/A | Not retail |
| Telecom services | Yes | 6.5% | Yes | Various |
| Motor vehicles | Yes | 6.5% + excise | Yes + MVET | RCW 82.08.020 |
| Cannabis products | Yes | 6.5% + 37% excise | Yes | RCW 69.50.535 |

---

## PROHIBITIONS [T1]

- **NEVER** apply a clothing exemption in Washington -- clothing is fully taxable. [T1]
- **NEVER** treat SaaS or digital automated services as nontaxable -- Washington taxes digital products very broadly. [T1]
- **NEVER** assume custom software is exempt -- Washington taxes custom software delivered electronically (unlike most states). [T1]
- **NEVER** forget that B&O tax applies IN ADDITION to sales tax -- they are separate taxes. [T1]
- **NEVER** use origin-based sourcing for Washington -- WA is destination-based for ALL sales. [T1]
- **NEVER** confuse the absence of income tax with the absence of business tax -- B&O tax is a significant gross receipts tax. [T1]
- **NEVER** forget that candy and soft drinks are taxable (SST definitions apply). [T1]
- **NEVER** assume the vendor retains a discount -- WA has NO vendor discount. [T1]
- **NEVER** refuse the SST Certificate in Washington -- WA is an SST member and must accept it. [T1]
- **NEVER** treat OTC drugs as exempt in Washington -- only prescription drugs are exempt. [T1]

---

## Edge Case Registry [T1/T2]

### EC1 -- B&O Tax in Addition to Sales Tax [T1]

**Situation:** A retailer makes a $1,000 sale in Seattle. They ask about total tax impact.

**Resolution:** The retailer must: (a) collect sales tax from the customer (approximately $102.50 at Seattle's ~10.25% rate), AND (b) pay B&O tax on the gross receipts ($1,000 x 0.471% retailing rate = $4.71). The B&O is the retailer's own tax obligation, not collected from the customer. Total tax burden includes both.

### EC2 -- Digital Automated Services (SaaS) [T1]

**Situation:** A Washington business subscribes to a cloud-based accounting platform for $100/month.

**Resolution:** TAXABLE. Digital automated services (including SaaS) are taxable in Washington at the combined rate. Tax = $100 x ~10.25% (Seattle) = $10.25/month. RCW 82.04.050(6)(b). Washington's definition of digital automated services is very broad.

### EC3 -- Custom Software Also Taxable [T1]

**Situation:** A business hires a developer to create custom software, delivered electronically.

**Resolution:** Unlike most states, Washington taxes custom software when delivered electronically. RCW 82.04.050(6)(a) defines "digital goods" to include custom digital products. The development service may also be subject to B&O tax under the service classification. Flag for reviewer if the custom software includes significant consulting/professional service components. [T2]

### EC4 -- Destination-Based Rate Complexity [T1]

**Situation:** A Seattle retailer ships goods to a customer in Spokane.

**Resolution:** Destination-based sourcing applies. The retailer charges the Spokane rate (~8.90%), NOT the Seattle rate (~10.25%). The retailer must determine the correct rate using the DOR's rate lookup tool for the specific delivery address.

### EC5 -- No Income Tax, But B&O and Capital Gains [T1]

**Situation:** A business owner asks about Washington's overall tax structure.

**Resolution:** Washington has NO personal income tax and NO corporate income tax. However: (a) B&O tax applies to gross receipts (no deductions), (b) sales tax applies to retail sales, (c) a capital gains tax applies to certain capital asset sales (high-income individuals). The B&O tax is unique to Washington. Escalate B&O details to [T3].

### EC6 -- Lodging Tax [T1]

**Situation:** A hotel charges $200/night for a room in Seattle.

**Resolution:** Hotels are subject to: (a) retail sales tax at the combined rate, AND (b) a separate lodging tax (varies by jurisdiction). The lodging taxes are separate from and in addition to sales tax. Specific lodging tax rates are outside this skill's scope -- escalate to [T2].

### EC7 -- SST Registration [T1]

**Situation:** An out-of-state online seller wants to register in Washington.

**Resolution:** Because Washington is an SST member, the seller can register through the SST Registration System (SSTRS) at https://www.sstregister.org, covering Washington and all other SST states simultaneously. Washington will issue a UBI number and business license upon registration.

### EC8 -- Marijuana/Cannabis [T1]

**Situation:** A licensed cannabis retailer sells products in Washington.

**Resolution:** Cannabis products are subject to: (a) a 37% cannabis excise tax (RCW 69.50.535), AND (b) state and local sales tax at the combined rate. Both taxes apply. The excise tax is included in the selling price before sales tax is calculated. Cannabis taxation is complex -- escalate detailed questions to [T3].

### EC9 -- Bottled Water vs. Soft Drinks [T1]

**Situation:** A convenience store sells bottled water and flavored sparkling water.

**Resolution:** Plain bottled water (non-carbonated, no flavoring) is EXEMPT as a food product. Flavored water and carbonated water are classified as soft drinks and are TAXABLE. RCW 82.08.0293.

### EC10 -- Extended Warranties/Service Contracts [T1]

**Situation:** A retailer sells an optional extended warranty with a product.

**Resolution:** Extended warranties and service contracts sold at the time of sale of TPP are TAXABLE in Washington. RCW 82.04.050(7). The warranty price is subject to sales tax at the combined rate, same as the underlying product.

---

## Test Suite

### Test 1 -- Basic Taxable Sale in Seattle [T1]

**Input:** Retailer sells a $1,000 laptop in Seattle. Combined rate: 10.25%.
**Expected output:** Sales tax = $102.50. Total = $1,102.50.

### Test 2 -- Grocery Food Exempt [T1]

**Input:** Customer buys $200 of groceries (bread, milk, produce) at a Seattle supermarket.
**Expected output:** Sales tax = $0. Grocery food exempt.

### Test 3 -- SaaS (Digital Automated Service) Taxable [T1]

**Input:** Spokane business subscribes to cloud-based HR tool. $300/month. Spokane rate: 8.90%.
**Expected output:** Sales tax = $26.70/month. Digital automated services (SaaS) are taxable in WA.

### Test 4 -- Economic Nexus [T1]

**Input:** Oregon-based online seller has $120,000 in WA sales in the current year. No physical presence.
**Expected output:** Exceeds $100,000 threshold. Must register with WA DOR and collect WA sales tax.

### Test 5 -- Destination-Based Sourcing [T1]

**Input:** Seattle retailer ships a $500 item to a customer in Vancouver, WA. Vancouver rate: 8.60%.
**Expected output:** Sales tax = $43.00 ($500 x 8.60%). Destination-based -- Vancouver rate, not Seattle rate.

### Test 6 -- Candy Taxable (SST Definition) [T1]

**Input:** Customer buys a $5 chocolate bar (no flour) at a store in Tacoma. Rate: 10.20%.
**Expected output:** Sales tax = $0.51. Candy is taxable under SST definitions.

### Test 7 -- Clothing Fully Taxable [T1]

**Input:** Customer buys a $300 jacket in Seattle. Rate: 10.25%.
**Expected output:** Sales tax = $30.75. No clothing exemption in Washington.

### Test 8 -- Extended Warranty Taxable [T1]

**Input:** Customer purchases a $50 extended warranty with a new TV. Seattle rate: 10.25%.
**Expected output:** Sales tax on warranty = $5.13. Extended warranties are taxable in WA.

### Test 9 -- Use Tax [T1]

**Input:** Seattle business purchases $3,000 of office equipment from an Oregon retailer (no sales tax). No WA tax collected. Rate: 10.25%.
**Expected output:** Use tax = $307.50 ($3,000 x 10.25%). Report on Combined Excise Tax Return.

### Test 10 -- Custom Software Taxable [T1]

**Input:** WA business pays $20,000 for custom software development, delivered electronically. Business in Seattle.
**Expected output:** Sales tax = $2,050.00 ($20,000 x 10.25%). Custom software delivered electronically is taxable in WA (unlike most states).

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
| WA DOR Main | https://dor.wa.gov |
| My DOR (Online Filing) | https://secure.dor.wa.gov/home/ |
| Rate Lookup | https://dor.wa.gov/taxes-rates/sales-use-tax-rates |
| Phone | 360-705-6705 |
| Business License Application | https://bls.dor.wa.gov |
| SST Registration | https://www.sstregister.org |
| Tax Topics | https://dor.wa.gov/taxes-rates/retail-sales-tax |
| B&O Tax Information | https://dor.wa.gov/taxes-rates/business-occupation-tax |
| WAC 458-20 (Admin Rules) | https://apps.leg.wa.gov/wac/default.aspx?cite=458-20 |

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
