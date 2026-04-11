---
name: us-sales-tax
description: Use this skill whenever asked about United States sales tax, use tax, sales tax nexus, multi-state tax compliance, sales tax returns, exemption certificates, taxability of goods or services, economic nexus, or any request involving US state-level consumption taxes. Trigger on phrases like "sales tax", "use tax", "nexus", "Wayfair", "sales tax return", "exemption certificate", "resale certificate", "taxability", "sales tax rate", "marketplace facilitator", "Streamlined Sales Tax", "SST", or any request involving US state sales and use tax filing, classification, or compliance. This skill contains the complete US sales and use tax framework including nexus rules, rate tables, taxability matrices, exemption rules, filing requirements, and major state deep dives. ALWAYS read this skill before touching any US sales tax work.
---

# United States Sales and Use Tax Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | United States of America |
| Jurisdiction Code | US |
| Tax Type | Sales and Use Tax (state-level, no federal equivalent) |
| Primary Legal Framework | No federal sales tax statute; each state has its own sales and use tax act |
| Key Federal Precedent | South Dakota v. Wayfair, Inc., 585 U.S. ___ (2018) |
| Governing Bodies | 45 state revenue departments + DC (no single federal authority) |
| Industry Body | Streamlined Sales Tax Governing Board (SSTGB) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: federal framework, rate lookups for known jurisdictions, basic nexus determination. Tier 2: taxability classification by state, exemption certificate validity, multi-state apportionment. Tier 3: audit defense, complex bundled transactions, state-specific rulings, penalty abatement. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to a licensed tax professional and document the gap.

---

## Section 1: Overview -- The US Has No Federal VAT or Sales Tax [T1]

### 1.1 Fundamental Structure

The United States does **not** impose a federal value-added tax (VAT), goods and services tax (GST), or federal sales tax. This is a critical structural difference from virtually every other developed economy. Consumption taxation in the US is exclusively a **state and local** matter.

**Key facts:**

- **45 states plus the District of Columbia** impose a general sales tax. [T1]
- **5 states impose NO general sales tax:** Alaska (AK), Delaware (DE), Montana (MT), New Hampshire (NH), and Oregon (OR). [T1]
- Even among the "no sales tax" states, Alaska permits **local jurisdictions** to impose sales taxes (some boroughs/cities levy rates up to 7.5%). [T1]
- Montana permits a **resort tax** in certain tourist areas. [T1]
- New Hampshire imposes a **meals and rooms tax** (8.5%) but no general sales tax. [T1]
- Delaware imposes a **gross receipts tax** on sellers rather than a sales tax on buyers. [T1]

**Source:** PwC Tax Summaries -- "Sales and use taxes constitute a major revenue source for the 45 states that impose such taxes and the District of Columbia." State-level rates "generally range from 2.9% to 7.25%."

### 1.2 Sales Tax vs. Use Tax [T1]

- **Sales tax** is collected by the seller at the point of sale on taxable transactions within the state.
- **Use tax** is a complementary tax imposed on the buyer when sales tax was not collected at the point of sale -- typically on out-of-state or online purchases brought into the state for use, storage, or consumption.
- Sales tax and use tax rates are always identical within a jurisdiction. They are two sides of the same coin -- you pay one or the other, never both.
- **Legislation:** Each state's sales and use tax act (e.g., California Revenue & Taxation Code Div. 2, Part 1; Texas Tax Code Ch. 151; New York Tax Law Art. 28).

### 1.3 Tax Base [T1]

- Sales tax generally applies to the **retail sale of tangible personal property (TPP)**.
- Taxation of **services** varies enormously by state -- from states that tax virtually all services (Hawaii, New Mexico, South Dakota) to states that tax almost none (most states only tax specifically enumerated services).
- **Digital goods and SaaS** represent an evolving and inconsistent area of state taxation. [T2]
- **Real property** is generally not subject to sales tax (subject to property tax instead). [T1]

### 1.4 Local Taxes -- The Layering Problem [T1]

Unlike the EU VAT system (one rate per country with limited variation), the US has approximately **13,000 distinct sales tax jurisdictions** when accounting for state, county, city, and special district taxes.

- A single address may be subject to state tax + county tax + city tax + special district tax (transit, stadium, etc.).
- Combined rates can exceed **10%** in some jurisdictions.
- Rate determination requires the **precise delivery address**, not just the state.
- Tools like state tax rate databases, or services such as Avalara, Vertex, and TaxJar, exist specifically to manage this complexity. [T2]

### 1.5 Origin-Based vs. Destination-Based Sourcing [T2]

States follow one of two sourcing methods:

| Method | Description | States |
|--------|-------------|--------|
| **Origin-based** | Tax rate is based on the seller's location | TX, OH, PA, VA, AZ, IL (partial), MO, TN, UT, MS |
| **Destination-based** | Tax rate is based on the buyer's location (delivery address) | CA, NY, FL, WA, NJ, MA, GA, NC, and most other states |

**Note:** For interstate (remote) sales, virtually all states apply **destination-based** sourcing regardless of their intrastate rule. [T1]

---

## Section 2: Nexus Rules -- When Must a Seller Collect Tax? [T1/T2]

### 2.1 Physical Nexus (Pre-Wayfair, Still Applies) [T1]

A seller has **physical nexus** in a state if it has any of the following physical connections:

- Office, store, warehouse, or other place of business in the state
- Employees, agents, or independent contractors performing services in the state
- Inventory stored in the state (including Amazon FBA inventory)
- Delivery vehicles entering the state
- Property (owned or rented) in the state
- Temporary physical presence (trade shows, pop-up shops -- varies by state, some have de minimis thresholds)

**Legislation:** Quill Corp. v. North Dakota, 504 U.S. 298 (1992) established the physical presence standard, which was the sole nexus standard until 2018.

### 2.2 Economic Nexus (Post-Wayfair, 2018) [T1]

On June 21, 2018, the US Supreme Court decided **South Dakota v. Wayfair, Inc., 585 U.S. ___ (2018)**, overruling Quill and holding that a state may require a seller to collect and remit sales tax even without physical presence, provided:

1. The seller exceeds the state's **economic nexus threshold** (typically measured by sales revenue and/or transaction count into the state).
2. The law does not discriminate against interstate commerce.
3. The law does not impose an undue burden on interstate commerce.

**Impact:** All 45 sales tax states (plus DC) have now enacted economic nexus laws. [T1]

### 2.3 Economic Nexus Thresholds by State [T2]

The following table reflects thresholds as of the most recent legislative sessions. **Thresholds change -- always verify current thresholds with the state's revenue department before relying on these figures.**

| State | Revenue Threshold | Transaction Threshold | Effective Date | Notes |
|-------|-------------------|----------------------|----------------|-------|
| Alabama (AL) | $250,000 | N/A | 10/1/2018 | Revenue only |
| Arizona (AZ) | $100,000 | N/A | 10/1/2019 | Dropped transaction test |
| Arkansas (AR) | $100,000 | 200 transactions | 7/1/2019 | |
| California (CA) | $500,000 | N/A | 4/1/2019 | Highest revenue threshold |
| Colorado (CO) | $100,000 | N/A | 6/1/2019 | Revenue only |
| Connecticut (CT) | $100,000 | 200 transactions | 12/1/2018 | |
| District of Columbia (DC) | $100,000 | 200 transactions | 1/1/2019 | |
| Florida (FL) | $100,000 | N/A | 7/1/2021 | Late adopter |
| Georgia (GA) | $100,000 | 200 transactions | 1/1/2019 | |
| Hawaii (HI) | $100,000 | 200 transactions | 7/1/2018 | GET, not traditional sales tax |
| Idaho (ID) | $100,000 | N/A | 6/1/2019 | Revenue only |
| Illinois (IL) | $100,000 | 200 transactions | 10/1/2018 | |
| Indiana (IN) | $100,000 | 200 transactions | 10/1/2018 | |
| Iowa (IA) | $100,000 | N/A | 1/1/2019 | Revenue only |
| Kansas (KS) | $100,000 | N/A | 7/1/2021 | Late adopter |
| Kentucky (KY) | $100,000 | 200 transactions | 10/1/2018 | |
| Louisiana (LA) | $100,000 | 200 transactions | 7/1/2020 | Centralized via Sales Tax Commission |
| Maine (ME) | $100,000 | 200 transactions | 7/1/2018 | |
| Maryland (MD) | $100,000 | 200 transactions | 10/1/2018 | |
| Massachusetts (MA) | $100,000 | N/A | 10/1/2019 | Revenue only |
| Michigan (MI) | $100,000 | 200 transactions | 10/1/2018 | |
| Minnesota (MN) | $100,000 | 200 transactions | 10/1/2018 | |
| Mississippi (MS) | $250,000 | N/A | 9/1/2018 | Higher threshold |
| Missouri (MO) | $100,000 | N/A | 1/1/2023 | Last state to adopt |
| Nebraska (NE) | $100,000 | 200 transactions | 1/1/2019 | |
| Nevada (NV) | $100,000 | 200 transactions | 10/1/2018 | |
| New Jersey (NJ) | $100,000 | 200 transactions | 11/1/2018 | |
| New Mexico (NM) | $100,000 | N/A | 7/1/2019 | Gross receipts tax |
| New York (NY) | $500,000 | 100 transactions | 6/1/2019 | Both thresholds must be met |
| North Carolina (NC) | $100,000 | 200 transactions | 11/1/2018 | |
| North Dakota (ND) | $100,000 | N/A | 10/1/2018 | Revenue only |
| Ohio (OH) | $100,000 | 200 transactions | 8/1/2019 | |
| Oklahoma (OK) | $100,000 | N/A | 7/1/2018 | Revenue only |
| Pennsylvania (PA) | $100,000 | N/A | 7/1/2019 | Revenue only |
| Rhode Island (RI) | $100,000 | 200 transactions | 7/1/2019 | |
| South Carolina (SC) | $100,000 | N/A | 11/1/2018 | Revenue only |
| South Dakota (SD) | $100,000 | 200 transactions | 11/1/2018 | The Wayfair state |
| Tennessee (TN) | $100,000 | N/A | 10/1/2019 | Revenue only |
| Texas (TX) | $500,000 | N/A | 10/1/2019 | High threshold |
| Utah (UT) | $100,000 | 200 transactions | 1/1/2019 | |
| Vermont (VT) | $100,000 | 200 transactions | 7/1/2018 | |
| Virginia (VA) | $100,000 | 200 transactions | 7/1/2019 | |
| Washington (WA) | $100,000 | N/A | 10/1/2018 | Revenue only; B&O tax also applies |
| West Virginia (WV) | $100,000 | 200 transactions | 1/1/2019 | |
| Wisconsin (WI) | $100,000 | N/A | 10/1/2018 | Revenue only |
| Wyoming (WY) | $100,000 | 200 transactions | 2/1/2019 | |

**Critical notes:**

- **New York** requires BOTH thresholds be met (AND test). Most other states use an OR test (either threshold triggers nexus). [T1]
- **California and Texas** have the highest revenue-only thresholds at $500,000. [T1]
- Many states have **dropped the transaction count** threshold, retaining only the revenue threshold. This trend is ongoing. [T2]
- Thresholds are measured on a **trailing 12-month** or **current/prior calendar year** basis depending on the state. [T2]
- **Exempt sales generally count** toward the threshold in most states (you may have nexus even if all your sales are exempt). [T2]

### 2.4 Marketplace Facilitator Laws [T1]

As of 2024, **all 45 sales tax states plus DC** have enacted marketplace facilitator laws.

**How they work:**
- A **marketplace facilitator** (e.g., Amazon, eBay, Etsy, Walmart Marketplace) is required to collect and remit sales tax on behalf of third-party sellers on its platform.
- The **marketplace seller** is relieved of the collection obligation for sales made through the marketplace.
- The marketplace seller remains responsible for sales made through their own website or other non-marketplace channels.

**Key marketplace facilitators:** Amazon, eBay, Etsy, Walmart Marketplace, Shopify (when used with certain features), Facebook Marketplace, Google Shopping Actions, Wayfair, Target Plus.

**Legislation:** Each state has its own marketplace facilitator statute. E.g., California Rev. & Tax. Code Section 6040-6045; Texas Tax Code Section 151.0242; New York Tax Law Section 1101(b)(8)(vi).

### 2.5 Remote Seller Obligations [T1]

Once economic nexus is established, a remote seller must:

1. **Register** for a sales tax permit in the state.
2. **Collect** the correct sales tax rate on taxable sales to buyers in that state.
3. **File** sales tax returns on the schedule set by the state (monthly, quarterly, or annually).
4. **Remit** the collected tax by the return due date.

**Failure to comply** can result in penalties, interest, and personal liability for corporate officers in some states. [T1]

### 2.6 Click-Through Nexus and Affiliate Nexus [T2]

Some states have additional nexus types beyond physical and economic:

- **Click-through nexus (affiliate nexus):** If an in-state entity (e.g., a blogger or website) refers customers to an out-of-state seller through a link and the seller pays a commission, nexus may be established. First enacted by New York (the "Amazon tax"). States: NY, CA, IL, AR, CT, GA, KS, ME, MN, MO, NC, NJ, PA, RI, TN, VT, WA.
- **Cookie nexus / Software nexus:** Some states (e.g., MA, OH, CT) assert that placing cookies or software on in-state computers creates nexus.

**These nexus types are less significant post-Wayfair** (since economic nexus is broader), but they remain on the books and may apply in edge cases. [T2]

---

## Section 3: Rate Tables -- State and Local Sales Tax Rates [T1/T2]

### 3.1 State Base Rates [T1]

The following are the **state-level base rates only**. Local taxes (county, city, special district) add to these rates. Combined rates can be significantly higher.

**Source:** Tax Foundation, state revenue department publications. Rates are subject to legislative change.

#### Group A: No General State Sales Tax

| State | State Rate | Notes |
|-------|-----------|-------|
| Alaska (AK) | 0% | Local taxes up to 7.5% may apply |
| Delaware (DE) | 0% | Gross receipts tax on sellers instead |
| Montana (MT) | 0% | Resort tax in certain areas |
| New Hampshire (NH) | 0% | 8.5% meals and rooms tax |
| Oregon (OR) | 0% | No local sales tax either |

#### Group B: Low Rate States (Under 5%)

| State | State Rate | Avg Local Rate | Combined Avg | Max Combined |
|-------|-----------|----------------|-------------|-------------|
| Colorado (CO) | 2.90% | 4.88% | 7.78% | 11.20% |
| Alabama (AL) | 4.00% | 5.28% | 9.28% | 13.50% |
| Georgia (GA) | 4.00% | 3.39% | 7.39% | 9.00% |
| Hawaii (HI) | 4.00% | 0.50% | 4.50% | 4.50% |
| Louisiana (LA) | 4.45% | 5.10% | 9.55% | 11.45% |
| Missouri (MO) | 4.225% | 4.07% | 8.30% | 11.99% |
| New York (NY) | 4.00% | 4.53% | 8.53% | 8.875% |
| North Carolina (NC) | 4.75% | 2.25% | 7.00% | 7.50% |
| South Dakota (SD) | 4.20% | 1.91% | 6.11% | 8.00% |
| Virginia (VA) | 4.30% | 0.47% | 4.77% | 7.00% |
| Wisconsin (WI) | 5.00% | 0.43% | 5.43% | 5.60% |
| Wyoming (WY) | 4.00% | 1.44% | 5.44% | 6.00% |

#### Group C: Medium Rate States (5% to 6.99%)

| State | State Rate | Avg Local Rate | Combined Avg | Max Combined |
|-------|-----------|----------------|-------------|-------------|
| Arizona (AZ) | 5.60% | 2.80% | 8.40% | 11.20% |
| Connecticut (CT) | 6.35% | 0% | 6.35% | 6.35% |
| District of Columbia (DC) | 6.00% | 0% | 6.00% | 6.00% |
| Florida (FL) | 6.00% | 1.01% | 7.01% | 7.50% |
| Idaho (ID) | 6.00% | 0.03% | 6.03% | 8.50% |
| Illinois (IL) | 6.25% | 2.60% | 8.85% | 11.00% |
| Iowa (IA) | 6.00% | 0.94% | 6.94% | 7.00% |
| Kansas (KS) | 6.50% | 2.22% | 8.72% | 11.60% |
| Kentucky (KY) | 6.00% | 0% | 6.00% | 6.00% |
| Maine (ME) | 5.50% | 0% | 5.50% | 5.50% |
| Maryland (MD) | 6.00% | 0% | 6.00% | 6.00% |
| Massachusetts (MA) | 6.25% | 0% | 6.25% | 6.25% |
| Michigan (MI) | 6.00% | 0% | 6.00% | 6.00% |
| Minnesota (MN) | 6.875% | 0.64% | 7.52% | 9.53% |
| Nebraska (NE) | 5.50% | 1.44% | 6.94% | 8.00% |
| Nevada (NV) | 6.85% | 1.38% | 8.23% | 8.38% |
| New Jersey (NJ) | 6.625% | 0% | 6.625% | 6.625% |
| New Mexico (NM) | 5.125% | 2.78% | 7.91% | 9.44% |
| North Dakota (ND) | 5.00% | 2.04% | 7.04% | 8.50% |
| Ohio (OH) | 5.75% | 1.48% | 7.23% | 8.00% |
| Oklahoma (OK) | 4.50% | 4.49% | 8.99% | 11.50% |
| Pennsylvania (PA) | 6.00% | 0.34% | 6.34% | 8.00% |
| Rhode Island (RI) | 7.00% | 0% | 7.00% | 7.00% |
| South Carolina (SC) | 6.00% | 1.44% | 7.44% | 9.00% |
| Utah (UT) | 6.10% | 1.12% | 7.22% | 9.05% |
| Vermont (VT) | 6.00% | 0.38% | 6.38% | 7.00% |
| West Virginia (WV) | 6.00% | 0.56% | 6.56% | 7.00% |

#### Group D: High Rate States (7% and Above)

| State | State Rate | Avg Local Rate | Combined Avg | Max Combined |
|-------|-----------|----------------|-------------|-------------|
| California (CA) | 7.25% | 1.60% | 8.85% | 10.75% |
| Indiana (IN) | 7.00% | 0% | 7.00% | 7.00% |
| Mississippi (MS) | 7.00% | 0.07% | 7.07% | 7.25% |
| Tennessee (TN) | 7.00% | 2.55% | 9.55% | 9.75% |
| Texas (TX) | 6.25% | 1.95% | 8.20% | 8.25% |
| Washington (WA) | 6.50% | 2.76% | 9.26% | 10.60% |
| Arkansas (AR) | 6.50% | 2.97% | 9.47% | 11.63% |

**Notes on this table:**

- Average local rates are approximate and change frequently. [T2]
- "Max Combined" reflects the highest known combined rate in a jurisdiction within the state. Actual rates vary by precise location. [T2]
- States like Connecticut, Kentucky, Maryland, Indiana, Massachusetts, Michigan, and New Jersey have **no local option taxes**, making compliance simpler. [T1]
- Some states cap local taxes (e.g., Virginia caps most local rates at 1%). [T1]

### 3.2 Highest Combined Rates (Top 10 Jurisdictions) [T1]

The following jurisdictions have among the highest combined sales tax rates in the nation:

| Jurisdiction | State Rate | Local Rate | Combined |
|-------------|-----------|------------|----------|
| Tacoma, WA | 6.50% | 3.80% | 10.30% |
| Chicago, IL | 6.25% | 4.75% | 11.00% |
| Long Beach, CA | 7.25% | 3.25% | 10.50% |
| Baton Rouge, LA | 4.45% | 6.00% | 10.45% |
| Birmingham, AL | 4.00% | 6.00% | 10.00% |
| Little Rock, AR | 6.50% | 4.63% | 11.13% |
| Kansas City, KS | 6.50% | 4.60% | 11.10% |
| Oklahoma City, OK | 4.50% | 4.13% | 8.63% |
| Seattle, WA | 6.50% | 3.75% | 10.25% |
| New York City, NY | 4.00% | 4.875% | 8.875% |

---

## Section 4: Taxability Rules -- What Is Taxable? [T2]

**This entire section is [T2] because taxability varies by state. A practitioner must ALWAYS confirm the specific state's rules. The generalizations below are starting points, not definitive answers.**

### 4.1 Tangible Personal Property (TPP) [T1/T2]

**General rule:** TPP is taxable in ALL 45 sales tax states + DC. [T1]

**Exceptions exist for specific categories of TPP** (see below). [T2]

### 4.2 Food and Groceries [T2]

Food/grocery taxability is one of the most varied areas:

| Treatment | States |
|-----------|--------|
| **Fully taxable** (same rate as other TPP) | AL, HI, ID, KS, MS, OK, SD |
| **Taxable at reduced rate** | AR (0.125%), IL (1%), MO (1.225%), TN (4%), UT (3%), VA (1%) |
| **Exempt** (unprepared food/groceries) | AZ, CA, CO, CT, DC, FL, GA, IA, IN, KY, LA, MA, MD, ME, MI, MN, NC, NE, NJ, NM, NV, NY, ND, OH, PA, RI, SC, TX, VT, WA, WI, WV, WY |

**Key distinctions within food:**
- "Prepared food" (ready to eat, heated, sold with utensils) is **generally taxable** even in states that exempt groceries. [T1]
- Candy and soft drinks are taxable in many states that otherwise exempt groceries. [T2]
- Dietary supplements are treated differently from food in many states. [T2]
- **Legislation examples:** California Rev. & Tax. Code Section 6359 (food exemption); New York Tax Law Section 1115(a)(1) (food exemption with $1.50 candy bar rule repealed).

### 4.3 Clothing and Apparel [T2]

| Treatment | States |
|-----------|--------|
| **Exempt** (general clothing) | PA, NJ, MN, NY (items under $110 per item) |
| **Partially exempt** | MA (items under $175), NY (items under $110), RI (items under $250) |
| **Fully taxable** | All other sales tax states |

**Key details:**
- **Pennsylvania:** All clothing exempt. 6 Pa.C.S. Section 7204(27).
- **New Jersey:** All clothing exempt. N.J.S.A. 54:32B-8.4.
- **New York:** Clothing and footwear items under $110 per item are exempt. N.Y. Tax Law Section 1115(a)(30).
- **Minnesota:** Most clothing exempt. Minn. Stat. Section 297A.67, subd. 8.
- **Massachusetts:** First $175 of each clothing item is exempt. Mass. Gen. Laws ch. 64H, Section 6(k).
- Fur clothing, sports or recreational equipment, and costumes may be treated differently even in exempt states. [T2]

### 4.4 Prescription Drugs and Medical Devices [T1]

**General rule:** Prescription drugs are **exempt in ALL 45 sales tax states + DC.** [T1]

- Over-the-counter (OTC) drugs: **taxable** in most states; exempt in some (e.g., NY, NJ, PA, CT, MD, MN, VA, VT). [T2]
- Durable medical equipment (DME): exempt in most states with a prescription; taxability of non-prescription DME varies. [T2]
- Prosthetics: generally exempt. [T1]

### 4.5 Services -- The Wild West of Sales Tax [T2]

Services taxation is the area of greatest state-by-state variation:

| Approach | States | Notes |
|----------|--------|-------|
| **Tax most/all services** | HI, NM, SD, WV | Broad-based service taxation |
| **Tax many enumerated services** | CT, DC, IA, MS, NE, OH, TX, WA, WI | Tax a substantial list |
| **Tax few services** | CA, CO, FL, GA, IL, IN, MA, MD, MI, MO, NC, NJ, NY, PA, SC, VA | Tax only specifically enumerated services |

**Commonly taxable services across many states:**
- Telecommunications services [T1 -- taxable in virtually all states]
- Cable and satellite TV services [T1]
- Landscaping and lawn care [T2]
- Pest control [T2]
- Security/alarm monitoring [T2]
- Parking services [T2]
- Dry cleaning and laundry [T2]
- Pet grooming [T2]
- Repair and maintenance of TPP [T2]

**Commonly exempt services across many states:**
- Professional services (legal, accounting, medical, engineering) [T2 -- exempt in most states, but taxable in some like NM, HI, SD, WV]
- Personal care (haircuts, manicures) [T2 -- growing number of states taxing these]
- Education and tutoring [T1 -- generally exempt]
- Financial services [T1 -- generally exempt]

**Legislation:** Each state enumerates its taxable services. E.g., Texas Tax Code Section 151.0101 (taxable services list); Connecticut Gen. Stat. Section 12-407(a)(37) (enumerated services).

### 4.6 Software and Digital Goods (SaaS, Cloud, Digital Downloads) [T2]

This is the fastest-evolving area of sales tax. Rules vary significantly:

#### Software Taxability Matrix

| Software Type | Generally Taxable | Generally Exempt | It Depends |
|---------------|-------------------|-----------------|------------|
| Canned software (physical media) | Most states | DE, MT, NH, OR | -- |
| Canned software (electronic delivery) | ~30 states | ~15 states | TX, CA, and others vary by specifics |
| Custom software | ~15 states | ~30 states | Depends on customization degree |
| SaaS (Software as a Service) | ~20 states | ~20 states | ~5 states have partial taxation |
| Digital downloads (music, e-books) | ~30 states | ~15 states | Depends on format and permanence |
| Streaming services | ~30 states | ~15 states | Emerging area |

**States that clearly tax SaaS:** CT, DC, HI, IA, MA, NM, NY, OH, PA, RI, SC, SD, TN, TX, UT, WA, WV.

**States that clearly do NOT tax SaaS:** CA, CO, FL, GA, ID, IL, IN, KS, KY, ME, MD, MI, MN, MO, NC, ND, NE, NJ, NV, OR, VA, VT, WI, WY.

**Caution:** This is a rapidly changing area. Multiple states have pending legislation or administrative rulings that could change classifications. Always check the latest state guidance. [T2]

**Key rulings and guidance:**
- Texas Comptroller Rule 3.330 (data processing services taxable, but SaaS classification debated).
- New York Advisory Opinion TSB-A-13(22)S (SaaS generally taxable as pre-written software).
- California BTLG Annotation 495.0127 (SaaS generally not taxable under current law).

### 4.7 Manufacturing Equipment and Machinery [T2]

Many states provide sales tax exemptions for machinery and equipment used **directly** in manufacturing:

| Exemption Level | States |
|----------------|--------|
| **Full exemption** | CA, CT, FL, GA, IL, IN, KY, MA, MD, MI, MN, MO, NJ, NY, OH, PA, SC, TN, TX, VA, WA, WI |
| **Partial exemption** (reduced rate or specific categories) | AL, AR, AZ, CO, IA, ID, KS, LA, MS, NC, NE, ND, NM, NV, OK, UT, WV |
| **No specific manufacturing exemption** | HI, NM (GET applies broadly), SD, WY |

**Key issues:**
- Definition of "manufacturing" varies by state. [T2]
- "Directly used in" vs. "predominantly used in" -- different standards across states. [T2]
- Research and development equipment may or may not qualify. [T2]
- Packaging materials are often treated differently from production equipment. [T2]

### 4.8 Motor Vehicles [T1]

Motor vehicles are subject to sales tax in all sales tax states, but the mechanism varies:

- Some states impose sales tax at registration (not at point of sale).
- Trade-in credit: most states allow the trade-in value to reduce the taxable amount.
- **Legislation examples:** Florida Stat. Section 212.05(1)(a)1 (motor vehicle sales tax); Texas Tax Code Section 152 (motor vehicle sales and use tax, separate chapter).

### 4.9 Real Property and Construction [T2]

- Real property itself is NOT subject to sales tax. [T1]
- Construction materials: treatment varies:
  - In some states, the contractor pays sales tax on materials and the labor is exempt.
  - In other states, the contract is a lump-sum and materials become exempt as part of a real property improvement.
  - **This is one of the most complex areas of sales tax law.** [T3 for complex projects]

---

## Section 5: Sales Tax Returns -- Filing Requirements [T1/T2]

### 5.1 Filing Frequency [T1]

States assign filing frequency based on the seller's tax liability:

| Frequency | Typical Liability Threshold | States Using This System |
|-----------|---------------------------|-------------------------|
| **Monthly** | > $300-$1,000/month in tax | All 45 states + DC |
| **Quarterly** | $100-$1,000/quarter | Most states |
| **Annually** | < $100-$500/year | Most states |
| **Semi-annually** | Varies | A few states (e.g., ME, WI) |

**Common thresholds for monthly filing:**
- California: $10,000+ in quarterly tax liability
- Texas: $500+ in monthly tax liability
- New York: $3,000+ in quarterly tax liability
- Florida: $1,000+ in monthly tax liability

### 5.2 Due Dates [T1]

| Pattern | States |
|---------|--------|
| **20th of the following month** | CA, TX, FL, NY, IL, PA, OH, NJ, and most states |
| **Last day of the following month** | Some states |
| **15th of the following month** | A few states |
| **25th of the following month** | WA |

**Note:** If the due date falls on a weekend or holiday, the deadline is generally the next business day. [T1]

### 5.3 Major State Filing Portals [T1]

| State | Portal | Agency |
|-------|--------|--------|
| California | https://www.cdtfa.ca.gov | California Department of Tax and Fee Administration (CDTFA) |
| Texas | https://comptroller.texas.gov | Texas Comptroller of Public Accounts |
| New York | https://www.tax.ny.gov | New York Department of Taxation and Finance (DTF) |
| Florida | https://floridarevenue.com | Florida Department of Revenue (DOR) |
| Illinois | https://mytax.illinois.gov | Illinois Department of Revenue (IDOR) |
| Pennsylvania | https://www.revenue.pa.gov | Pennsylvania Department of Revenue (DOR) |
| Ohio | https://tax.ohio.gov | Ohio Department of Taxation (ODT) |
| New Jersey | https://www.nj.gov/treasury/taxation | New Jersey Division of Taxation |
| Washington | https://dor.wa.gov | Washington Department of Revenue (DOR) |
| Massachusetts | https://www.mass.gov/dor | Massachusetts Department of Revenue (DOR) |

### 5.4 Streamlined Sales Tax (SST) [T2]

The **Streamlined Sales and Use Tax Agreement (SSUTA)** is an interstate compact to simplify sales tax collection and administration across member states.

**Full Member States (24):** AR, GA, IN, IA, KS, KY, MI, MN, NE, NV, NJ, NC, ND, OH, OK, RI, SD, TN, UT, VT, WA, WV, WI, WY.

**Associate Member States (1):** TN (transitioning).

**Benefits of SST membership:**
- Uniform definitions for taxable and exempt items.
- Simplified rate structures.
- Central registration system for sellers (register in all SST states at once).
- Free filing software through Certified Service Providers (CSPs).
- **Legislation:** Streamlined Sales and Use Tax Agreement (adopted 2002, amended periodically).

**Notable non-SST states:** CA, TX, NY, FL, IL, PA, MA, CO -- some of the largest economies are NOT SST members, meaning SST alone does not solve multi-state compliance. [T2]

### 5.5 Multi-State Filing Solutions [T2]

For sellers with nexus in multiple states, manual filing is impractical. Common solutions:

| Solution Type | Examples | Best For |
|--------------|---------|----------|
| **Tax automation platforms** | Avalara, Vertex, TaxJar, Sovos | Mid-to-large sellers |
| **SST Certified Service Providers** | FedTax, TaxCloud | Small sellers in SST states |
| **ERP-integrated solutions** | SAP Tax, Oracle Tax | Enterprise |
| **Marketplace reliance** | Amazon, eBay (they collect/remit) | Marketplace-only sellers |
| **CPA/tax professional filing** | Various | Sellers in few states |

### 5.6 Vendor Discounts (Timely Filing Credits) [T1]

Some states offer a discount for timely filing and remittance:

| State | Discount |
|-------|----------|
| Colorado | 3.33% (up to $200/month) |
| Florida | 2.5% (first $1,200/month) |
| Georgia | 3% (first $3,000/month) |
| Illinois | 1.75% |
| New York | 5% (up to $200/quarter) |
| Ohio | 0.75% |
| Pennsylvania | 1% (first $25/month for timely filing) |
| South Carolina | 3% (up to $3,100/month) |
| Texas | 0.5% (first $2,500/month for timely filers) |

---

## Section 6: Exemption Certificates [T1/T2]

### 6.1 Overview [T1]

Exemption certificates shift the sales tax liability from the seller to the buyer. The buyer provides the certificate to the seller, and the seller is relieved of the obligation to collect tax -- provided the certificate is properly completed and accepted in good faith.

**If a seller does not obtain a valid exemption certificate, the seller is liable for the uncollected tax.** [T1]

### 6.2 Types of Exemptions [T2]

| Exemption Type | Description | Common Form |
|---------------|-------------|-------------|
| **Resale** | Buyer is purchasing for resale, not own consumption | Resale Certificate / MTC Uniform |
| **Manufacturing** | Items used directly in manufacturing process | State-specific forms |
| **Agricultural** | Items used in agricultural production | State-specific forms |
| **Government** | Federal, state, or local government purchases | Government ID or letter |
| **Nonprofit / Religious** | Qualifying 501(c)(3) organizations | State exemption letter |
| **Direct pay permit** | Large buyers authorized to self-assess tax | Direct pay permit number |
| **Industrial** | Machinery/equipment for eligible industries | State-specific forms |
| **Energy/Utility** | Energy used in manufacturing or certain processes | State-specific forms |

### 6.3 Multi-Jurisdiction Exemption Certificate (MTC) [T1]

The **Multistate Tax Commission (MTC) Uniform Sales & Use Tax Exemption/Resale Certificate** (commonly called the "MTC certificate" or "uniform certificate") is accepted in **38+ states**.

**Key features:**
- Single form valid across multiple states.
- Buyer checks the applicable state(s) and reason for exemption.
- Must include buyer's name, address, state tax ID/registration number, description of items, and signature.

**States that do NOT accept the MTC Uniform Certificate** and require their own form:
- **California** -- requires BOE-230 Resale Certificate
- **Florida** -- requires DR-13 Annual Resale Certificate
- **Illinois** -- requires CRT-61 Resale Certificate
- **Massachusetts** -- requires ST-4 Resale Certificate
- **Texas** -- requires Form 01-339 Sales and Use Tax Resale Certificate
- **Washington** -- requires Resale Permit (not a certificate -- must be verified online)

**Always verify current acceptance.** Some states accept the MTC certificate for resale only, but require their own form for other exemption types. [T2]

### 6.4 Resale Certificates [T1]

**Purpose:** The buyer certifies they are purchasing the item for resale (not for their own use/consumption).

**Requirements for a valid resale certificate:**
1. Name and address of the buyer.
2. Buyer's state sales tax registration/permit number.
3. Description of the property being purchased.
4. Statement that the purchase is for resale.
5. Signature (physical or electronic) and date.
6. Some states require the buyer's type of business or SIC/NAICS code.

**Seller obligations:**
- Accept in good faith (seller has no duty to investigate the buyer's claim, provided the certificate is properly completed and the claim is not obviously fraudulent). [T1]
- Retain on file for the statute of limitations period (typically 3-4 years, but varies). [T1]
- A missing or incomplete certificate shifts liability to the seller. [T1]

**Blanket certificates vs. single-purchase certificates:**
- A blanket certificate covers all future purchases of the described type from the seller.
- A single-purchase certificate covers one specific transaction.
- Most states allow blanket certificates. [T1]

### 6.5 Nonprofit Exemptions [T2]

- Federal 501(c)(3) status does NOT automatically provide sales tax exemption in most states.
- Each state has its own exemption application process.
- Some states exempt only purchases; others also exempt the nonprofit's sales.
- The scope of exemption varies (some states exempt only religious organizations, others include charitable, educational, etc.).
- **Key states with NO general nonprofit sales tax exemption on purchases:** IL (some limited exemptions), CO (must apply per transaction in many cases).

### 6.6 Exemption Certificate Management Best Practices [T2]

- Maintain a centralized certificate repository (physical or digital).
- Set expiration reminders (some states require periodic renewal; e.g., Florida's DR-13 is annual).
- Validate buyer registration numbers against state databases where possible.
- Flag certificates that are missing required fields before accepting.
- Implement a system for audit retrieval -- certificates are the first thing auditors request. [T2]

---

## Section 7: Use Tax [T1/T2]

### 7.1 What Is Use Tax? [T1]

Use tax is a **complementary tax** to sales tax. It applies when:

1. A taxable item is purchased **without sales tax being collected** (e.g., from an out-of-state seller who has no nexus).
2. The item is used, stored, or consumed in a state that imposes sales/use tax.
3. No valid exemption applies.

**The rate of use tax is always the same as the sales tax rate.** [T1]

**Legislation:** Every sales tax state has a corresponding use tax statute. E.g., California Rev. & Tax. Code Section 6201-6246; New York Tax Law Section 1110.

### 7.2 Consumer Use Tax vs. Seller Use Tax [T1]

| Type | Who Reports/Pays | When |
|------|-----------------|------|
| **Consumer use tax** | The buyer (end consumer or business) | When purchasing from a seller who did not collect tax |
| **Seller use tax** | The seller (registered in the buyer's state) | When the seller has nexus and must collect "use tax" on remote sales |

**For businesses:** Consumer use tax is self-assessed on purchases where sales tax was not collected. This is reported on the business's sales tax return (most states have a "use tax" line) or on a separate use tax return. [T1]

**For individuals:** Most states include a use tax line on the individual income tax return. Compliance by individuals is historically very low but has increased with marketplace facilitator laws. [T2]

### 7.3 Common Use Tax Scenarios [T1]

1. **Online purchase from a small out-of-state seller** that has no nexus and no marketplace facilitator obligation. Buyer owes use tax.
2. **Business purchases supplies** from an out-of-state vendor who does not collect the state's tax. Business must self-assess use tax.
3. **Withdrawal from inventory:** A business takes an item from its resale inventory for its own use. Use tax is due on the item's cost.
4. **Items purchased tax-free with a resale certificate** that are later used by the business instead of resold. Use tax is due.
5. **Interstate transfers of equipment:** A business moves equipment from a no-tax state to a tax state. Use tax may be due.

### 7.4 Credit for Tax Paid to Another State [T1]

Most states allow a credit for sales or use tax legally paid to another state on the same transaction:

- If you paid 5% sales tax in State A and your home State B has a 7% rate, you owe 2% use tax to State B.
- If you paid 7% in State A and State B's rate is 5%, no use tax is due to State B (and no refund of the excess).
- The credit applies to **legally imposed and paid** tax only, not voluntary overpayments.

---

## Section 8: Major State Deep Dives [T1/T2]

### 8.1 California [T1/T2]

| Field | Detail |
|-------|--------|
| **State rate** | 7.25% (highest state base rate in the US) |
| **Local add-ons** | County and city rates; combined rates range from 7.25% to 10.75% |
| **Governing agency** | California Department of Tax and Fee Administration (CDTFA) |
| **Portal** | https://www.cdtfa.ca.gov |
| **Economic nexus** | $500,000 in sales (no transaction test) |
| **Filing frequency** | Monthly, quarterly, or annual depending on liability |
| **Due date** | Last day of the month following the reporting period |
| **Key statute** | California Revenue & Taxation Code, Division 2, Part 1 |

**California-specific rules:**
- **District taxes:** California has numerous special taxing districts (transit, library, public safety). Each has its own rate and boundaries. Rate lookup requires precise address. [T2]
- **Food:** Unprepared food is exempt; prepared food is taxable. Cal. Rev. & Tax. Code Section 6359. [T1]
- **SaaS:** Generally NOT taxable under current CDTFA guidance. Technology transfer agreements (TTAs) for custom software are also not taxable. But pre-written software delivered on tangible media IS taxable. [T2]
- **Manufacturing exemption:** Partial exemption (3.9375% rate reduction) for manufacturing equipment. Cal. Rev. & Tax. Code Section 6377.1. [T1]
- **Clothing:** Fully taxable (no exemption). [T1]
- **Prepayment requirement:** Large sellers (> $17,000/month tax) must prepay estimated tax by the 15th of the month. [T1]

### 8.2 Texas [T1/T2]

| Field | Detail |
|-------|--------|
| **State rate** | 6.25% |
| **Local add-ons** | Up to 2% (cities, counties, transit, SPDs); combined max 8.25% |
| **Governing agency** | Texas Comptroller of Public Accounts |
| **Portal** | https://comptroller.texas.gov |
| **Economic nexus** | $500,000 in sales (no transaction test) |
| **Filing frequency** | Monthly, quarterly, or annual |
| **Due date** | 20th of the month following the reporting period |
| **Key statute** | Texas Tax Code, Chapter 151 |

**Texas-specific rules:**
- **No state income tax** -- sales tax is the state's primary revenue source. [T1]
- **Services:** Texas taxes 17 enumerated services, including data processing, real property repair, amusement services, and cable TV. Tex. Tax Code Section 151.0101. [T2]
- **SaaS / Data processing:** Taxable as "data processing services" at a reduced rate (80% of the taxable amount is exempt, effective rate = 20% x 8.25% = 1.65% max). Tex. Tax Code Section 151.0035. [T2]
- **Food:** Unprepared groceries are exempt. Tex. Tax Code Section 151.314. [T1]
- **Manufacturing:** Equipment and machinery used in manufacturing are exempt. Tex. Tax Code Section 151.318. [T1]
- **Clothing:** Fully taxable (no exemption, except during sales tax holidays). [T1]
- **Origin-based sourcing:** For intrastate sales, tax rate is based on seller's location. [T1]

### 8.3 New York [T1/T2]

| Field | Detail |
|-------|--------|
| **State rate** | 4.00% |
| **Local add-ons** | Up to 4.875% (county/city/MCTD); NYC combined = 8.875% |
| **Governing agency** | New York Department of Taxation and Finance (DTF) |
| **Portal** | https://www.tax.ny.gov |
| **Economic nexus** | $500,000 in sales AND 100+ transactions (both required) |
| **Filing frequency** | Quarterly (with monthly PrompTax for large vendors) |
| **Due date** | 20th of the month following the quarter |
| **Key statute** | New York Tax Law, Article 28 |

**New York-specific rules:**
- **MCTD surcharge:** The Metropolitan Commuter Transportation District imposes an additional 0.375% on sales within its boundaries (NYC and surrounding counties). [T1]
- **Clothing:** Items under $110 per item are exempt from state AND NYC tax. N.Y. Tax Law Section 1115(a)(30). [T1]
- **Food:** Unprepared food exempt; prepared food, candy, and soft drinks are taxable. [T1]
- **SaaS:** Taxable as pre-written software. NYS Advisory Opinion TSB-A-13(22)S. [T2]
- **Services:** Limited enumeration; information services, maintenance/repair, and protective/detective services are among those taxed. [T2]
- **Economic nexus note:** New York is unique in requiring BOTH thresholds (revenue AND transactions). A seller with $1M in sales but only 50 transactions does NOT have economic nexus. [T1]

### 8.4 Florida [T1/T2]

| Field | Detail |
|-------|--------|
| **State rate** | 6.00% |
| **Local add-ons** | County surtax up to 1.5%; combined max ~7.50% |
| **Governing agency** | Florida Department of Revenue (DOR) |
| **Portal** | https://floridarevenue.com |
| **Economic nexus** | $100,000 in sales (no transaction test) |
| **Filing frequency** | Monthly, quarterly, semi-annual, or annual |
| **Due date** | 1st through 20th of the month following the reporting period |
| **Key statute** | Florida Statutes Chapter 212 |

**Florida-specific rules:**
- **No state income tax** -- similar to Texas, heavy reliance on sales tax revenue. [T1]
- **Late adopter:** Florida's economic nexus law took effect July 1, 2021 -- one of the last states. [T1]
- **Commercial rent:** Florida is one of the few states that taxes commercial real property rentals (rate is 2.0% as of 2024, reduced from 5.5% over several years). Fla. Stat. Section 212.031. [T1]
- **Food:** Unprepared groceries exempt. Fla. Stat. Section 212.08(1). [T1]
- **SaaS:** Generally NOT taxable (no specific statute, but DOR has ruled SaaS is not tangible personal property). [T2]
- **Manufacturing:** Equipment used in manufacturing is exempt. Fla. Stat. Section 212.08(5)(b). [T1]
- **Discretionary surtax:** Counties impose their own surtax (0.5% to 1.5%), but it typically applies only to the first $5,000 of a single transaction. [T1]

### 8.5 Illinois [T1/T2]

| Field | Detail |
|-------|--------|
| **State rate** | 6.25% (general merchandise); 1% (qualifying food, drugs, medical appliances) |
| **Local add-ons** | Home rule municipalities, county, transit; combined can exceed 10% |
| **Governing agency** | Illinois Department of Revenue (IDOR) |
| **Portal** | https://mytax.illinois.gov |
| **Economic nexus** | $100,000 in sales or 200 transactions |
| **Filing frequency** | Monthly, quarterly, or annual |
| **Due date** | 20th of the month following the reporting period |
| **Key statute** | Illinois Retailers' Occupation Tax Act (35 ILCS 120); Use Tax Act (35 ILCS 105) |

**Illinois-specific rules:**
- **Not technically a sales tax:** Illinois imposes a Retailers' Occupation Tax (ROT) on the seller's gross receipts, not a tax on the buyer. The economic effect is the same, but the legal distinction matters for sourcing and nexus. [T1]
- **Dual rate structure:** General merchandise at 6.25%; qualifying food, drugs, and medical appliances at 1%. [T1]
- **Home rule:** Home rule municipalities (e.g., Chicago) can impose additional taxes without state authorization. Chicago's combined rate can reach 10.25% or higher. [T1]
- **SaaS:** Not taxable (not considered tangible personal property). [T2]
- **Origin-based sourcing:** For intrastate sales by Illinois retailers. [T1]

### 8.6 Pennsylvania [T1/T2]

| Field | Detail |
|-------|--------|
| **State rate** | 6.00% |
| **Local add-ons** | Philadelphia: 2% (total 8%); Allegheny County: 1% (total 7%) |
| **Governing agency** | Pennsylvania Department of Revenue (DOR) |
| **Portal** | https://www.revenue.pa.gov |
| **Economic nexus** | $100,000 in sales (no transaction test) |
| **Filing frequency** | Monthly, quarterly, or semi-annual |
| **Due date** | 20th of the month following the reporting period |
| **Key statute** | Pennsylvania Tax Reform Code, Article II (72 P.S. Section 7201 et seq.) |

**Pennsylvania-specific rules:**
- **Clothing:** ALL clothing and footwear are exempt (one of the broadest clothing exemptions). 72 P.S. Section 7204(27). [T1]
- **Food:** Unprepared food exempt. [T1]
- **SaaS:** Taxable. Pennsylvania taxes canned software regardless of delivery method, and has ruled SaaS is taxable. [T2]
- **Philadelphia:** The 2% local tax applies to most taxable items; Philadelphia also has its own separate beverage tax on sugar-sweetened and diet beverages. [T1]
- **Manufacturing:** Machinery and equipment used directly in manufacturing are exempt. 72 P.S. Section 7201(k)(8). [T1]
- **Vendor discount:** 1% of tax collected (max $25/month) for timely filing. [T1]

### 8.7 Ohio [T1/T2]

| Field | Detail |
|-------|--------|
| **State rate** | 5.75% |
| **Local add-ons** | County rates; combined rates range from 6.50% to 8.00% |
| **Governing agency** | Ohio Department of Taxation (ODT) |
| **Portal** | https://tax.ohio.gov |
| **Economic nexus** | $100,000 in sales or 200 transactions |
| **Filing frequency** | Monthly or semi-annual |
| **Due date** | 23rd of the month following the reporting period |
| **Key statute** | Ohio Revised Code Chapter 5739 (Sales Tax); Chapter 5741 (Use Tax) |

**Ohio-specific rules:**
- **CAT vs. sales tax:** Ohio also imposes a Commercial Activity Tax (CAT) on gross receipts, which is separate from and in addition to sales tax. [T1]
- **Food:** Unprepared food is exempt. Ohio Rev. Code Section 5739.02(B)(2). [T1]
- **SaaS:** Taxable as an "automatic data processing" service. Ohio Rev. Code Section 5739.01(B)(3)(e). [T2]
- **Manufacturing:** Equipment used in manufacturing is exempt. Ohio Rev. Code Section 5739.011. [T1]
- **SST member:** Ohio is a full member of the Streamlined Sales Tax Agreement. [T1]
- **Origin-based sourcing** for intrastate sales. [T1]

### 8.8 New Jersey [T1/T2]

| Field | Detail |
|-------|--------|
| **State rate** | 6.625% |
| **Local add-ons** | None (uniform statewide rate); Urban Enterprise Zones (UEZ) have reduced rate of 3.3125% |
| **Governing agency** | New Jersey Division of Taxation |
| **Portal** | https://www.nj.gov/treasury/taxation |
| **Economic nexus** | $100,000 in sales or 200 transactions |
| **Filing frequency** | Monthly or quarterly |
| **Due date** | 20th of the month following the reporting period |
| **Key statute** | New Jersey Sales and Use Tax Act (N.J.S.A. 54:32B-1 et seq.) |

**New Jersey-specific rules:**
- **No local taxes:** NJ has a uniform statewide rate -- no county or city add-ons (except UEZ reductions). This makes compliance simpler than many states. [T1]
- **Clothing:** ALL clothing and footwear are exempt. N.J.S.A. 54:32B-8.4. [T1]
- **Food:** Unprepared groceries, most food, and beverages are exempt. [T1]
- **OTC drugs:** Exempt. [T1]
- **SaaS:** Not specifically addressed; generally treated as not taxable under current interpretation (pre-written software delivered electronically is not taxable). [T2]
- **Urban Enterprise Zones:** Qualified businesses in UEZs collect tax at 50% of the standard rate (3.3125%). [T1]
- **SST member:** Yes, full member. [T1]

### 8.9 Washington [T1/T2]

| Field | Detail |
|-------|--------|
| **State rate** | 6.50% |
| **Local add-ons** | City/county/transit rates; combined up to 10.60% |
| **Governing agency** | Washington Department of Revenue (DOR) |
| **Portal** | https://dor.wa.gov |
| **Economic nexus** | $100,000 in sales (no transaction test) |
| **Filing frequency** | Monthly, quarterly, or annual |
| **Due date** | 25th of the month following the reporting period |
| **Key statute** | Washington Revised Code Chapter 82.08 (Retail Sales Tax); Chapter 82.12 (Use Tax) |

**Washington-specific rules:**
- **No state income tax** -- heavy reliance on sales tax and B&O tax. [T1]
- **B&O tax:** Washington also imposes a Business & Occupation (B&O) tax on gross receipts -- this is separate from and IN ADDITION TO sales tax. B&O is a tax on the seller; sales tax is on the buyer. [T1]
- **SaaS:** Taxable. Digital automated services (including SaaS) are taxable. RCW 82.04.192. [T1]
- **Digital goods:** Taxable. Washington was one of the first states to comprehensively tax digital goods. [T1]
- **Food:** Unprepared groceries exempt; prepared food taxable. [T1]
- **Resale permits:** Washington uses a permit system (not certificates). Sellers must verify the buyer's resale permit online -- they cannot simply accept a paper certificate. [T1]
- **Destination-based sourcing.** [T1]
- **SST member:** Full member. [T1]

### 8.10 Massachusetts [T1/T2]

| Field | Detail |
|-------|--------|
| **State rate** | 6.25% |
| **Local add-ons** | None (uniform statewide rate) |
| **Governing agency** | Massachusetts Department of Revenue (DOR) |
| **Portal** | https://www.mass.gov/dor |
| **Economic nexus** | $100,000 in sales (no transaction test) |
| **Filing frequency** | Monthly or quarterly |
| **Due date** | 20th of the month following the reporting period |
| **Key statute** | Massachusetts General Laws Chapter 64H (Sales Tax); Chapter 64I (Use Tax) |

**Massachusetts-specific rules:**
- **No local taxes:** Uniform statewide rate of 6.25%. [T1]
- **Clothing:** First $175 of each clothing item is exempt. Amount above $175 is taxable. Mass. Gen. Laws ch. 64H, Section 6(k). Example: a $200 jacket incurs tax on $25 only. [T1]
- **Food:** Unprepared groceries exempt; meals served at restaurants/cafeterias are taxable (meals tax, which can include a local option of 0.75%). [T1]
- **SaaS:** Taxable. Massachusetts taxes pre-written software regardless of delivery method, including SaaS. Mass. Gen. Laws ch. 64H, Section 1 (definition of tangible personal property includes pre-written software). [T2]
- **Telecom:** Taxable. [T1]
- **Manufacturing:** Machinery used directly and exclusively in manufacturing is exempt. Mass. Gen. Laws ch. 64H, Section 6(s). [T1]
- **Cookie nexus:** Massachusetts asserted nexus through cookies/software placed on in-state devices (Directive 17-1), though this is largely superseded by economic nexus. [T2]

---

## Section 9: Edge Cases [T2/T3]

### EC1 -- Drop Shipping [T2]

**Situation:** Seller A in State X takes an order from Buyer in State Y. Seller A directs Manufacturer B in State Z to ship directly to Buyer in State Y. Three states, three parties.

**Resolution:**
- **Seller A** must collect tax from Buyer if Seller A has nexus in State Y (the buyer's state).
- **Manufacturer B** may be required to collect tax from Seller A unless Seller A provides a resale certificate valid in State Z (the ship-from state) OR State Y (the ship-to state, depending on the state's rules).
- Some states require the resale certificate to be issued in the drop-ship state; others accept out-of-state certificates. [T2]
- **Key issue:** If Seller A does NOT have nexus in State Y and Manufacturer B DOES have nexus in State Y, Manufacturer B may be obligated to collect tax from the end buyer -- but Manufacturer B's customer is Seller A, not Buyer. This creates a compliance gap.
- **SSUTA Section 310.1** provides model rules for drop shipping in SST states.
- **Flag for reviewer:** Drop shipping scenarios require analysis of nexus in all involved states and the validity of exemption certificates across jurisdictions. [T2]

### EC2 -- Marketplace Facilitator Double Taxation Risk [T2]

**Situation:** A seller has nexus in a state and files returns. They also sell through Amazon, which collects and remits tax as a marketplace facilitator. The seller's return may include marketplace sales in gross receipts.

**Resolution:**
- The seller must **exclude** marketplace sales (where the marketplace collected tax) from their own return to avoid double remittance.
- Most state returns have a specific line for "marketplace sales" deductions.
- If the seller fails to exclude these sales and the marketplace also remits, the state may receive double tax. The seller would need to request a refund.
- **Flag for reviewer:** Ensure the seller's accounting system properly segregates marketplace vs. direct sales. [T2]

### EC3 -- Digital Goods Sold Across State Lines [T2]

**Situation:** A company in Oregon (no sales tax) sells digital downloads to customers in 30 different states.

**Resolution:**
- The company must analyze economic nexus in each destination state.
- Where nexus exists, the company must determine if digital goods are taxable in that state (varies -- see Section 4.6).
- The company must register, collect, file, and remit in each state where it has nexus and the product is taxable.
- Oregon's lack of sales tax is irrelevant -- nexus and taxability are determined by the destination state for digital goods.
- **Flag for reviewer:** Digital goods classification (purchase vs. subscription vs. streaming) may affect taxability differently in different states. [T2]

### EC4 -- SaaS Taxability Conflicts [T2]

**Situation:** A SaaS company based in California (SaaS not taxable) sells subscriptions to customers in Texas (SaaS taxable as data processing at reduced rate), Pennsylvania (SaaS taxable at full rate), and Washington (SaaS taxable as digital automated service).

**Resolution:**
- Taxability is determined by the **customer's state**, not the seller's state. [T1]
- The SaaS company must collect and remit at the applicable rate in each customer's state where (a) it has nexus and (b) SaaS is taxable.
- TX: collect at 80% exemption rate (effective ~1.65% combined).
- PA: collect at full 6% state + local.
- WA: collect at full combined rate (6.5% + local).
- **Flag for reviewer:** Confirm current SaaS taxability status in each state, as this area is rapidly evolving. [T2]

### EC5 -- Economic Nexus Threshold Monitoring [T2]

**Situation:** A growing e-commerce company approaches the $100,000 threshold in several states simultaneously.

**Resolution:**
- Must track trailing 12-month (or current/prior calendar year, depending on state) sales into each state.
- Some states measure by gross sales; others by taxable sales only. [T2]
- Some states count only sales of TPP; others include services and exempt sales. [T2]
- Once the threshold is crossed, registration is typically required within 30-60 days (varies by state).
- **Retroactive exposure:** Some states assert that nexus applies to sales made BEFORE the threshold was crossed (in the measuring period). This is contested but some states take this position. [T3]
- **Flag for reviewer:** Implement automated threshold monitoring. Manual tracking across 45+ states is error-prone. [T2]

### EC6 -- Exempt Organization Purchases [T2]

**Situation:** A 501(c)(3) nonprofit purchases office supplies from a retailer. The nonprofit has state sales tax exemption letters in some states but not others.

**Resolution:**
- The nonprofit must present a valid exemption certificate or letter for the state where the purchase occurs.
- Federal 501(c)(3) status alone is NOT sufficient for state sales tax exemption in most states. [T1]
- Some states require the nonprofit to apply for and receive a state-issued exemption number.
- The seller must retain the exemption documentation.
- If the nonprofit makes purchases in a state where it does not have an exemption, sales tax applies.
- **Flag for reviewer:** Verify the nonprofit's exemption status is current in the specific state. Exemptions may have expiration dates or activity requirements. [T2]

### EC7 -- Construction Contracts and Lump-Sum vs. Time-and-Materials [T2/T3]

**Situation:** A contractor builds an addition to a commercial building. The contract is $500,000 including labor and materials.

**Resolution:**
- In most states, the contractor is the **end consumer** of the materials incorporated into real property (the building). The contractor pays sales tax on materials at the time of purchase.
- The customer is NOT charged sales tax on the lump-sum contract price (it is a real property improvement, not a sale of TPP).
- **Exception:** In some states (e.g., AZ, HI, NM, MS), the contractor may be required to collect tax on the entire contract (including labor).
- **Time-and-materials contracts:** Some states treat separately stated materials as sales of TPP (taxable) and labor as a service (possibly exempt).
- **This is one of the most complex areas of sales tax law.** [T3]
- **Flag for reviewer:** Construction contract taxability requires detailed state-specific analysis. Do not apply general rules without confirmation. [T3]

### EC8 -- Bundled Transactions (Mixed Taxable and Exempt Items) [T2]

**Situation:** A seller offers a package deal: a computer ($800, taxable) bundled with installation services ($200, exempt in the state) for a flat price of $900.

**Resolution:**
- **SST definition (SSUTA Section 330):** If the transaction includes both taxable and exempt items and the taxable portion exceeds 10% of the total, the ENTIRE transaction is taxable (unless items are separately stated).
- **Non-SST states:** Rules vary. Some states apply the "true object" test (what is the primary purpose of the transaction?). Others prorate.
- **Best practice:** Always separately state taxable and exempt items on the invoice to avoid bundling issues.
- **Flag for reviewer:** Determine whether the state follows SST bundling rules, true object test, or another method. [T2]

### EC9 -- Sales Tax Holidays [T1]

**Situation:** Customer purchases school supplies and clothing during a state-designated "sales tax holiday" weekend.

**Resolution:**
- Approximately **18 states** hold annual sales tax holidays, typically in July/August (back-to-school) or during severe weather season.
- Common categories exempt during holidays: clothing (under a threshold, e.g., $100/item), school supplies, computers (some states), Energy Star appliances.
- Each state defines its own items, thresholds, and dates.
- **States with regular sales tax holidays include:** AL, AR, CT, FL, IA, MA, MD, MO, MS, NM, OH, OK, SC, TN, TX, VA, WV.
- Online purchases qualify if the order is placed during the holiday period (regardless of delivery date in most states).
- **Legislation example:** Texas Tax Code Section 151.326 (clothing and footwear holiday).

### EC10 -- Leases and Rentals of Tangible Personal Property [T2]

**Situation:** A company leases office equipment (copiers, printers) under a 36-month lease.

**Resolution:**
- Most states tax leases/rentals of TPP.
- Some states tax the **full purchase price upfront** (at lease inception).
- Other states tax **each lease payment** as it is made.
- Some states distinguish between "true leases" and "financing arrangements" (the latter may be treated as a sale).
- **Flag for reviewer:** Determine the specific state's treatment of lease/rental transactions, especially regarding upfront vs. periodic tax, and lease vs. financing classification. [T2]

### EC11 -- Interstate Employee Travel and Supplies [T2]

**Situation:** A company based in New Jersey purchases supplies in New Jersey (6.625% tax paid) and then ships them to its Pennsylvania office (6% tax + possible local).

**Resolution:**
- New Jersey sales tax was paid at purchase. When the items enter Pennsylvania for use, PA use tax may theoretically be due.
- Credit applies: PA would grant credit for the NJ tax paid (6.625%), which exceeds PA's rate (6%). Therefore, no PA use tax is due.
- If the reverse were true (purchased in PA at 6%, moved to NJ at 6.625%), NJ use tax of 0.625% would be due.
- **Practical note:** States rarely audit individual supply transfers between offices, but the obligation technically exists. [T2]

### EC12 -- Voluntary Disclosure Agreements (VDAs) [T2]

**Situation:** A company discovers it has had economic nexus in five states for three years but never registered, collected, or remitted sales tax.

**Resolution:**
- Most states offer a **Voluntary Disclosure Agreement (VDA)** program that allows the company to come into compliance with reduced penalties and a limited look-back period (typically 3-4 years, sometimes shorter).
- The Multistate Tax Commission (MTC) offers a centralized VDA program (National Nexus Program) for sellers who need to register in multiple states simultaneously.
- **Benefits of VDA:** Reduced or waived penalties; limited look-back period; negotiated payment terms.
- **Risks of NOT doing VDA:** Full look-back (statute of limitations, typically 3-7 years); full penalties (5-25% of tax due); interest from the original due date.
- **Flag for reviewer:** VDAs should be handled by a tax attorney or CPA with multi-state experience. The company should NOT register or file past-due returns without first negotiating the VDA. [T3]

### EC13 -- Resale Certificate Abuse / Misuse [T2]

**Situation:** An individual provides a resale certificate to a furniture store to purchase furniture for personal use, claiming it is for resale.

**Resolution:**
- The buyer is committing fraud. The buyer is liable for the uncollected tax plus penalties.
- The seller is protected IF the certificate was accepted in good faith (properly completed, not obviously fraudulent).
- **Good faith indicators:** The buyer has a valid sales tax registration number, the business type is consistent with the purchase, and the seller had no reason to know the purchase was for personal use.
- Some states impose penalties on buyers who misuse resale certificates (e.g., penalty equal to the tax evaded plus additional fines).
- **Flag for reviewer:** Sellers should implement procedures to identify suspicious resale claims (e.g., a hair salon buying industrial machinery on a resale certificate). [T2]

### EC14 -- Subscription Boxes and Mixed Deliveries [T2]

**Situation:** A subscription box company ships monthly boxes containing a mix of taxable tangible goods and non-taxable items (e.g., a book + candle + digital download code) to customers in multiple states.

**Resolution:**
- The company must determine taxability of each item in each destination state.
- Books are exempt in some states (NJ, NY, PA, CT) but taxable in others.
- If items are bundled at a single price, bundling rules apply (see EC8).
- Shipping and handling charges may or may not be taxable depending on the state (see below).
- The company should separately state taxable and exempt items where possible.
- **Shipping charges:** Taxable in some states (TX, NY, OH); exempt in others (CA on shipping separately stated; NJ); partially taxable in others (if shipping includes handling, the handling may be taxable). [T2]

---

## Section 10: Test Suite [T1]

### Test 1 -- Basic Taxable Sale in California

**Input:** Seller located in Los Angeles, CA sells office furniture for $1,000 to a buyer in Los Angeles. No exemption certificate. Combined rate in buyer's location is 9.50%.
**Expected output:** Sales tax = $95.00. Total charged to buyer = $1,095.00. Seller reports and remits $95.00 to CDTFA (apportioned between state and district taxes).

### Test 2 -- Economic Nexus Determination

**Input:** Online seller based in Oregon (no sales tax) made $120,000 in sales to Texas customers and $80,000 in sales to Florida customers in the trailing 12 months.
**Expected output:**
- Texas: $120,000 < $500,000 threshold. No economic nexus in TX. No collection obligation. [T1]
- Florida: $80,000 < $100,000 threshold. No economic nexus in FL. No collection obligation. [T1]
- Seller has no sales tax obligations in either state based on these facts alone.

### Test 3 -- Clothing Exemption in New York

**Input:** Retailer in NYC sells a jacket priced at $150 to a walk-in customer. NYC combined rate = 8.875%.
**Expected output:** Jacket is under $110 threshold -- WAIT. $150 > $110. The full $150 is taxable (the exemption applies to items UNDER $110, not the first $110 of each item). Sales tax = $150 x 8.875% = $13.31.
**Note:** This is a common error. In NY, the exemption applies to items with a price under $110, not a per-item deduction. A $109 shirt is exempt; a $111 shirt is fully taxable.

### Test 4 -- Clothing Exemption in Massachusetts

**Input:** Retailer in Boston sells a jacket priced at $200. MA rate = 6.25%.
**Expected output:** First $175 is exempt. Tax applies to ($200 - $175) = $25. Sales tax = $25 x 6.25% = $1.56. Total charged = $201.56.
**Note:** Massachusetts applies the exemption as a per-item deduction (first $175 exempt), unlike New York's all-or-nothing approach.

### Test 5 -- Use Tax Self-Assessment

**Input:** A business in Illinois purchases $5,000 of office supplies from an out-of-state vendor who did not collect Illinois tax. Business is located in a jurisdiction with a combined rate of 8.75%.
**Expected output:** Business must self-assess use tax of $5,000 x 8.75% = $437.50, reported on the business's use tax return or sales tax return (use tax line).

### Test 6 -- Marketplace Facilitator Sale

**Input:** Third-party seller on Amazon ships a $50 taxable product to a buyer in Tennessee. Amazon is the marketplace facilitator. Combined TN rate at buyer's location = 9.75%.
**Expected output:** Amazon collects and remits $4.88 in sales tax. The third-party seller does NOT collect or remit tax on this sale. The seller should exclude this sale from their own TN sales tax return (deduction for marketplace sales).

### Test 7 -- Resale Certificate (Valid)

**Input:** Wholesale distributor in Texas sells $10,000 of inventory to a retail store. The retail store presents a properly completed Texas Form 01-339 with a valid TX sales tax permit number.
**Expected output:** No sales tax collected. The sale is exempt as a sale for resale. Distributor retains the certificate on file. The retail store will collect sales tax when it resells the inventory to end consumers.

### Test 8 -- SaaS Multi-State Taxability

**Input:** SaaS company based in California sells a $500/month subscription to customers in CA, TX, WA, and FL.
**Expected output:**
- CA: Not taxable. No tax collected. [T2]
- TX: Taxable as data processing at 80% exemption. Tax = $500 x 20% x 8.25% (max combined) = $8.25. [T2]
- WA: Taxable as digital automated service. Tax = $500 x 10.25% (Seattle rate example) = $51.25. [T2]
- FL: Not taxable under current interpretation. No tax collected. [T2]

### Test 9 -- Credit for Tax Paid to Another State

**Input:** A consumer purchases a $2,000 laptop in New Hampshire (0% sales tax) and brings it home to Massachusetts (6.25% sales tax).
**Expected output:** Consumer owes MA use tax of $2,000 x 6.25% = $125.00. No credit applies (no tax was paid to NH). Consumer should report on MA individual income tax return or file a use tax return.

### Test 10 -- Drop Ship Scenario

**Input:** Online seller in NY takes an order from a buyer in Ohio. Seller directs a manufacturer in California to ship directly to the Ohio buyer. The seller has nexus in Ohio. Ohio combined rate at buyer's location = 7.50%.
**Expected output:**
- NY seller collects OH sales tax from the buyer: $price x 7.50%.
- CA manufacturer does not collect tax IF the NY seller provides a valid resale certificate (MTC or CA-specific) to the CA manufacturer.
- If the NY seller does NOT provide a certificate, the CA manufacturer may need to collect CA tax from the NY seller (but the shipment is out-of-state, so CA tax may not apply on a shipment to OH). [T2]
- **Flag for reviewer:** Confirm certificate validity and nexus in all three states.

### Test 11 -- Grocery Exemption vs. Prepared Food

**Input:** Customer purchases the following at a Texas grocery store: bag of rice ($3.00), rotisserie chicken ($7.99), bottle of water ($1.50), deli sandwich heated at customer request ($5.99). Combined TX rate = 8.25%.
**Expected output:**
- Bag of rice: Exempt (unprepared food). [T1]
- Rotisserie chicken: Taxable (prepared food -- sold ready to eat, heated). Tax = $7.99 x 8.25% = $0.66. [T1]
- Bottle of water: Exempt (unprepared food/beverage, not carbonated). [T1]
- Deli sandwich (heated): Taxable (prepared food). Tax = $5.99 x 8.25% = $0.49. [T1]
- Total tax = $1.15.

### Test 12 -- Sales Tax Holiday

**Input:** Customer purchases a $75 pair of jeans and a $200 laptop during Texas's sales tax holiday weekend (clothing under $100 and school supplies under $100 are exempt). Combined TX rate = 8.25%.
**Expected output:**
- Jeans ($75): Exempt during holiday (clothing under $100 threshold). [T1]
- Laptop ($200): NOT exempt (laptops are not school supplies; Texas does exempt certain computer/technology items during the holiday but with a threshold -- check current year's list). [T2]
- **Flag for reviewer:** Verify current year's sales tax holiday items and thresholds, as they change annually. [T2]

---

## Section 11: Comparison with EU VAT [T1]

Understanding the structural differences between US Sales Tax and EU VAT is critical for businesses operating in both jurisdictions.

### 11.1 Structural Comparison Table [T1]

| Feature | US Sales Tax | EU VAT |
|---------|-------------|--------|
| **Federal/national tax?** | NO -- state and local only | YES -- each EU member state imposes VAT under a harmonized EU directive (Council Directive 2006/112/EC) |
| **Number of taxing jurisdictions** | ~13,000 (state + county + city + district) | 27 member states, each with one rate schedule |
| **Tax type** | Single-stage retail tax (tax collected once, at final sale) | Multi-stage value-added tax (tax collected at each stage of production/distribution) |
| **Input tax credit / deduction** | NO -- no mechanism for businesses to recover sales tax paid on inputs (tax cascading occurs) | YES -- businesses deduct input VAT from output VAT; only net VAT is remitted |
| **Tax cascading** | YES -- if a manufacturer pays sales tax on raw materials and the retailer pays sales tax on the finished good, tax-on-tax occurs | NO -- input credit system prevents cascading |
| **Invoice requirements** | No standardized tax invoice requirement (receipts show tax, but no formal invoice system) | Formal VAT invoice required with specific fields (supplier/customer VAT numbers, line-item tax, etc.) |
| **Registration threshold** | Varies by state ($100K-$500K economic nexus) | Varies by member state (e.g., EUR 35,000 in Malta, EUR 85,000 in UK pre-Brexit) |
| **Cross-border treatment** | Destination state's rules apply; no formal "reverse charge" between states | Intra-EU: reverse charge on B2B services; zero-rate on intra-EU goods with B2B proof |
| **Exemption certificates** | Yes -- buyer provides certificate to avoid tax at point of sale | Yes -- but structured differently (exempt activities, not buyer certificates) |
| **Rate uniformity** | NO -- rates vary by precise location within a state | YES -- each country has uniform rates nationwide (standard, reduced, zero) |
| **Filing** | Separate return filed in each state where nexus exists | Single return per country (with EC Sales List for intra-EU) |
| **Audit** | Each state audits independently | Each member state's tax authority audits |
| **Real-time reporting** | Not required (standard periodic filing) | Emerging in EU (e.g., Italy's SDI e-invoicing, Spain's SII) |

### 11.2 Key Implications for Businesses Operating in Both Systems [T2]

1. **No input credit in the US:** A business that pays sales tax on a US purchase cannot recover that tax (unlike EU input VAT). This means sales tax is a real cost to businesses on non-resale purchases. [T1]

2. **Tax cascading:** Because there is no input credit mechanism, US sales tax can "cascade" -- tax is embedded in the price at each level of the supply chain. Exemptions for manufacturing and resale mitigate this, but do not eliminate it entirely. [T1]

3. **Compliance burden:** A business selling across the EU files up to 27 VAT returns (one per country), each with uniform national rules. A business selling across the US may need to file in 45+ states, each with unique rules and potentially thousands of local rate variations. [T1]

4. **No harmonization body:** The EU has the European Commission and ECJ to harmonize VAT law. The US has no equivalent federal body for sales tax harmonization. The SST Agreement is voluntary and covers only 24 states. [T1]

5. **Digital goods:** The EU comprehensively taxes digital services under MOSS/OSS. The US has no federal equivalent -- each state decides independently whether and how to tax digital goods/SaaS. [T2]

### 11.3 Why the US Does Not Have a VAT [T1]

- **Constitutional structure:** The US Constitution grants taxing power to both federal and state governments. States have historically relied on sales tax as a primary revenue source and resist federal encroachment.
- **Political opposition:** Proposals for a federal VAT/national sales tax have been made (e.g., the FairTax proposal) but have never gained sufficient congressional support.
- **Federalism:** Each state views its taxing power as a matter of sovereignty. A federal VAT would directly compete with state sales taxes.
- **Revenue replacement:** A federal VAT would need to coexist with or replace the federal income tax -- politically difficult.

---

## Section 12: PROHIBITIONS [T1]

- NEVER assume a transaction is exempt without verifying the specific state's rules. Taxability varies by state for almost every category except prescription drugs. [T1]
- NEVER assume a single "US sales tax rate" exists. Always determine the specific state AND local rate for the buyer's precise delivery address. [T1]
- NEVER apply EU VAT concepts (input credits, reverse charge, zero-rating with credit) to US sales tax. The systems are structurally different. [T1]
- NEVER advise a seller that they have no nexus in a state without analyzing BOTH physical nexus AND economic nexus. [T1]
- NEVER ignore local taxes. State rate alone is insufficient. Combined rates can be 2-5 percentage points higher than the state base rate. [T1]
- NEVER accept an exemption certificate without verifying it is properly completed (name, address, tax ID, reason, signature). [T1]
- NEVER file a sales tax return in a state without first confirming the seller is registered in that state. Filing without registration can create unintended nexus in some states. [T2]
- NEVER advise a client to register in a state without considering the implications (once registered, filing obligations are ongoing even if sales drop below the nexus threshold). [T2]
- NEVER ignore use tax obligations. If sales tax was not collected on a taxable purchase, use tax is due. [T1]
- NEVER assume marketplace sales should be included on the seller's own return. Marketplace facilitator sales must be excluded to avoid double remittance. [T1]
- NEVER treat SaaS/digital goods taxability as uniform across states. Always check the specific state's current position. [T2]
- NEVER confuse origin-based and destination-based sourcing. The wrong rate applied to the wrong location is a common audit finding. [T1]
- NEVER advise on construction contract taxability without state-specific analysis. This area is too complex for general rules. [T3]
- NEVER register or file past-due returns in multiple states without first considering a Voluntary Disclosure Agreement (VDA). Premature registration can waive VDA benefits. [T2]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous or state-dependent]
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

If you are adapting this skill for a specific US state deep dive:

1. Replace the general state references with the specific state's statutes and administrative rules.
2. Include the state's complete rate schedule (including all local jurisdictions or a link to the official rate database).
3. Enumerate all taxable and exempt categories per the state's law.
4. Include state-specific exemption certificate forms and acceptance rules.
5. Include state-specific filing frequencies, due dates, and portal URLs.
6. Add state-specific edge cases (e.g., Texas data processing services, California district taxes, New York clothing threshold).
7. Have a licensed CPA or EA in the relevant state validate every T1 rule before publishing.
8. Run all test suite cases against the state's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
