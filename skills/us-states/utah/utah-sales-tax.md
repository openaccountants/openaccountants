---
name: utah-sales-tax
description: Use this skill whenever asked about Utah sales tax, Utah use tax, USTC sales tax filing, Utah grocery tax reduced rate, Utah SaaS tax, or Utah sales tax compliance. Trigger on phrases like "Utah sales tax", "UT sales tax", "Utah Code §59-12", "USTC", "Utah grocery tax", "Utah SaaS", "Utah SST", or any request involving Utah state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# Utah Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Utah, United States |
| Jurisdiction Code | US-UT |
| Tax Type | Sales and Use Tax (state + local) |
| State Rate | 4.85% |
| Grocery Food Rate | 3.00% (combined state + local -- see details) |
| Maximum Combined Rate | ~7.50% (state 4.85% + local up to ~2.65%) |
| Primary Statute | Utah Code §59-12 |
| Governing Agency | Utah State Tax Commission (USTC) |
| Portal | https://tax.utah.gov |
| SST Member | Yes -- Full Member |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, food rate, basic taxability, filing mechanics. T2: local rate lookups, SaaS taxability, service classification. T3: audit defense, complex exemptions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Utah sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have an Utah sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Utah? | Drives taxability classification under Utah law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Utah? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Utah local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Sales Tax Rate

Utah imposes a state sales tax of **4.85%** on the retail sale of tangible personal property and certain services. [T1]

**Statute:** Utah Code §59-12-103.

**Note:** The 4.85% consists of a base state rate (currently 4.85%, subject to legislative changes). Some sources may break this into components. [T2]

### 1.2 Local Sales Taxes [T1]

- Counties, cities, and special districts impose additional sales tax. [T1]
- Local add-ons range from approximately **1.15% to 2.65%**. [T1]
- Combined rates range from approximately **6.10% to 7.50%**. [T1]
- Salt Lake City combined rate: approximately **7.75%** (verify current rate). [T2]
- Local taxes are administered by USTC. [T1]

### 1.3 Sourcing [T1]

Utah uses a hybrid sourcing approach:
- **Origin-based** for intrastate sales from locations within Utah. [T1]
- **Destination-based** for interstate (remote) sales. [T1]

As an SST member, Utah follows SSUTA sourcing rules for remote sales. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food -- Reduced Rate [T1]

Utah taxes grocery food at a **reduced combined rate of 3.00%** (combining state and local components):

| Component | Rate on Food |
|-----------|-------------|
| State rate on food | 1.75% |
| Local uniform rate on food | 1.25% |
| **Total combined food rate** | **3.00%** |

- This rate applies uniformly statewide to qualifying food items. [T1]
- Prepared food: taxable at the FULL combined rate (not the reduced food rate). [T1]
- Candy: taxable at the full rate. [T1]
- Soft drinks: taxable at the full rate. [T1]

**Statute:** Utah Code §59-12-103(2).

### 2.2 Clothing [T1]

- Clothing is **fully taxable** at the standard combined rate. No exemption. [T1]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. Utah Code §59-12-104(8). [T1]
- OTC drugs: **taxable**. [T1]
- DME: exempt with prescription. [T1]
- Prosthetics: exempt. [T1]

### 2.4 Services [T2]

Utah taxes a moderate number of services:

- **Taxable services include:** Repair/renovation of TPP, cleaning/washing of TPP, laundry, telecommunications, lodging, admissions/amusements, parking, personal property rental, certain IT services. [T2]
- **Exempt services include:** Professional services (legal, accounting, medical), education, financial services, most personal care services. [T2]

### 2.5 SaaS and Digital Goods -- TAXABLE [T1/T2]

- **SaaS:** **Taxable** in Utah. Utah taxes prewritten computer software regardless of delivery method, including remotely accessed software (SaaS). Utah Code §59-12-103(1)(q). [T1]
- **Canned software (physical and electronic):** Taxable. [T1]
- **Custom software:** Exempt when specifically designed for a single customer. [T2]
- **Digital downloads:** Taxable. [T1]
- **Streaming services:** Taxable. [T2]

### 2.6 Manufacturing [T1]

- Manufacturing equipment: **exempt** when used in manufacturing or processing operations. Utah Code §59-12-104(14). [T1]
- Includes machinery, equipment, and supplies used directly in manufacturing. [T1]

### 2.7 Agricultural [T1]

- Farm machinery and equipment: exempt. Utah Code §59-12-104(58). [T1]
- Feed, seed, fertilizer: exempt. [T1]
- Livestock: exempt for breeding/production. [T1]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | TC-62S (Sales and Use Tax Return) |
| Filing Frequencies | Monthly (>$1,000/quarter avg tax); Quarterly ($250-$1,000); Annually (<$250) |
| Due Date | Last day of the month following the reporting period |
| Portal | https://tap.tax.utah.gov (Taxpayer Access Point) |
| E-filing | Required for most filers |

### 4.2 Vendor Discount [T1]

Utah offers a vendor discount of **1.31%** of the tax collected for timely filing (subject to caps). [T1]

### 4.3 Penalties and Interest [T1]

- Late filing penalty: 10% of tax due or $20, whichever is greater. [T1]
- Interest: rate set quarterly based on federal short-term rate + specified margin. [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for Utah. Key categories: [T1]

- **Resale exemption:** Valid resale certificate required. Retain for the statutory period. [T1]
- **Exempt organizations:** Government entities and qualifying nonprofits -- require exemption certificate on file. [T1]
- **Agricultural exemptions:** Where applicable per Step 2. [T1]
- **Manufacturing exemptions:** Where applicable per Step 2. [T2]

All exemption certificates must be collected at or before the time of sale and retained per the state's statute of limitations. [T1]


---

## Step 5: Key Thresholds
### 3.1 Economic Nexus Threshold [T1]

| Field | Detail |
|-------|--------|
| Revenue Threshold | $100,000 in Utah sales |
| Transaction Threshold | 200 transactions |
| Test | OR (either threshold triggers nexus) |
| Measurement Period | Current or prior calendar year |
| Effective Date | January 1, 2019 |

**Statute:** Utah Code §59-12-107(2)(d).

### 3.2 Marketplace Facilitator [T1]

Utah requires marketplace facilitators to collect and remit. Utah Code §59-12-107.1. [T1]

### 3.3 SST Registration [T1]

Full SST member. SSTRS and CSPs available. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER apply the full combined rate to grocery food. The reduced 3% rate applies statewide. [T1]
- NEVER apply the reduced food rate to candy, soft drinks, or prepared food. These are at the full rate. [T1]
- NEVER assume SaaS is exempt in Utah. It is taxable at the full combined rate. [T1]
- NEVER assume destination-based sourcing for all Utah sales. Intrastate sales use origin-based sourcing. [T1]
- NEVER assume a uniform combined rate across Utah. Local rates vary. However, the food rate IS uniform at 3%. [T1]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Food Rate vs. Full Rate Classification [T2]

**Situation:** A grocery store sells prepared deli items, packaged snacks, and fresh produce. Different rates apply.

**Resolution:**
- Fresh produce: 3% food rate. [T1]
- Packaged snacks (chips, crackers, not candy): 3% food rate. [T1]
- Candy: full combined rate (not food rate). [T1]
- Prepared deli items (heated, with utensils): full combined rate. [T1]
- Soft drinks: full combined rate. [T1]
- **Flag for reviewer:** Item classification against SST food definitions determines the applicable rate. [T2]

### EC2 -- SaaS Taxability [T2]

**Situation:** A SaaS company from Oregon provides cloud software to Utah businesses. Is it taxable?

**Resolution:**
- Utah taxes SaaS at the full combined rate. [T1]
- The SaaS company must register if it meets the $100K or 200 transaction economic nexus threshold. [T1]
- Tax is based on the customer's location (destination-based for remote sales). [T1]
- **Flag for reviewer:** Utah is one of the states that clearly taxes SaaS. Verify current USTC guidance. [T2]

### EC3 -- Origin-Based vs. Destination-Based Sourcing [T2]

**Situation:** A Utah retailer with a store in Salt Lake City ships an order to a customer in Park City. Different combined rates may apply.

**Resolution:**
- For intrastate sales, Utah uses origin-based sourcing. The rate at the seller's location (SLC) applies. [T1]
- For interstate sales (out-of-state buyer), destination-based sourcing applies. [T1]
- **Flag for reviewer:** Utah's hybrid sourcing creates different rate applications depending on whether the sale is intrastate or interstate. Verify the buyer's location. [T2]

### EC4 -- Food Rate Uniformity [T1]

**Situation:** A retailer asks whether the 3% food rate varies by location in Utah.

**Resolution:**
- The 3% food rate is **uniform statewide** regardless of the local combined rate on general merchandise. [T1]
- A store in a city with a 7.50% general rate and a store in a city with a 6.10% general rate both charge 3% on food. [T1]
- This simplifies POS configuration for food items. [T1]

---

### EC5 -- SaaS Company with Multi-State Customers [T2]

**Situation:** A SaaS company from Idaho (where SaaS is not taxable) sells subscriptions to Utah businesses.

**Resolution:**
- Utah taxes SaaS at the full combined rate. [T1]
- The company must register if economic nexus is met ($100K or 200 transactions). [T1]
- Destination-based sourcing applies for interstate sales. [T1]
- Tax based on the customer's Utah location. [T1]
- **Flag for reviewer:** SaaS companies should include Utah in their compliance matrix. Utah is one of the states that clearly taxes SaaS. [T2]

### EC6 -- Prepared Food at a Grocery Store [T2]

**Situation:** A grocery store has a deli that sells hot sandwiches, cold pre-made salads without utensils, and uncut birthday cakes.

**Resolution:**
- Hot sandwiches: prepared food (full rate). [T1]
- Cold pre-made salads without utensils and not heated: food (3% rate). [T1]
- Uncut birthday cakes (not heated, no utensils): food (3% rate). [T1]
- If the deli provides utensils with the salads, they become prepared food (full rate). [T2]
- **Flag for reviewer:** The prepared food determination depends on heating, utensils, and whether items are mixed for immediate consumption. [T2]

### EC7 -- Manufacturing Equipment Exemption [T1]

**Situation:** A manufacturer purchases a $500,000 production line for a Utah facility.

**Resolution:**
- Manufacturing equipment used in manufacturing/processing is exempt. Utah Code §59-12-104(14). [T1]
- The manufacturer must provide an exemption certificate to the seller. [T1]
- Office equipment, vehicles, and non-production items do NOT qualify. [T1]
- **Flag for reviewer:** Maintain documentation of equipment use in manufacturing. [T2]

---

## Test Suite

### Test 1 -- General Merchandise Sale

**Input:** Seller in Salt Lake City sells $1,000 electronics. Combined rate = 7.75%.
**Expected output:** Tax = $1,000 x 7.75% = $77.50. Total = $1,077.50.

### Test 2 -- Grocery Food at Reduced Rate

**Input:** Customer buys $200 of groceries anywhere in Utah. Food rate = 3%.
**Expected output:** Tax = $200 x 3% = $6.00. Total = $206.00.

### Test 3 -- Candy at Full Rate

**Input:** Customer buys $10 candy in SLC. Combined rate = 7.75%.
**Expected output:** Candy is NOT food rate. Tax = $10 x 7.75% = $0.78. Total = $10.78.

### Test 4 -- SaaS Subscription

**Input:** SaaS company charges Utah business $800/month. Combined rate = 7.25%.
**Expected output:** SaaS IS taxable. Tax = $800 x 7.25% = $58.00. Total = $858.00.

### Test 5 -- Economic Nexus

**Input:** Remote seller from Nevada sold $105,000 to Utah customers in the prior year.
**Expected output:** $105,000 exceeds $100,000 threshold. Nexus IS triggered. Must register and collect.

---

### Test 6 -- Prepared Food at Grocery Deli

**Input:** Customer at a Provo grocery store buys a $8 hot sandwich (prepared) and $5 cold salad (no utensils, not heated). Combined non-food rate = 7.25%. Food rate = 3%.
**Expected output:** Hot sandwich: $8 x 7.25% = $0.58. Cold salad (food): $5 x 3% = $0.15. Total tax = $0.73. Total = $13.73.

### Test 7 -- Origin-Based Intrastate Sale

**Input:** Seller in Salt Lake City (combined rate 7.75%) ships to buyer in Provo (combined rate 7.25%). Both in Utah.
**Expected output:** Intrastate sale uses origin-based sourcing. Rate = 7.75% (seller's SLC rate). Tax = sale price x 7.75%.

### Test 8 -- Manufacturing Equipment Exempt

**Input:** Manufacturer buys $100,000 production equipment for Utah plant.
**Expected output:** Manufacturing equipment exempt. Tax = $0. Total = $100,000.

---

## Reviewer Escalation Protocol

| Trigger | Action |
|---------|--------|
| Any [T3] tagged item encountered | STOP. Do not guess. Escalate to licensed CPA, EA, or tax attorney. |
| Client has audit notice or assessment | Escalate immediately. Do not advise on audit response. |
| Multi-state nexus question involving 3+ states | Flag for senior reviewer with multi-state experience. |
| Penalty abatement or voluntary disclosure | Escalate to licensed professional with state-specific experience. |
| Ambiguous taxability of a product/service | Present both interpretations to reviewer with supporting authority. |

---

## Contribution Notes

- This skill follows the Q1 execution format (Step 0 through Step 7).
- All rules are tagged [T1], [T2], or [T3] per the Confidence Tier Definitions.
- Rate tables are deterministic lookup tables -- no narrative explanation of rates.
- To update this skill, submit a pull request with the specific section, supporting statutory authority, and effective date of the change.
- All changes require validation by a US CPA or EA before merging.

---

## Disclaimer
This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
