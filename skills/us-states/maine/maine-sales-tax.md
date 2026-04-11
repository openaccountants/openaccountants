---
name: maine-sales-tax
description: Use this skill whenever asked about Maine sales tax, Maine use tax, Maine Revenue Services (MRS) sales tax filing, Maine lodging tax, or Maine sales tax compliance. Trigger on phrases like "Maine sales tax", "ME sales tax", "MRS", "36 M.R.S. §1811", "Maine lodging tax", "Maine auto rental tax", or any request involving Maine state sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# Maine Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Maine, United States |
| Jurisdiction Code | US-ME |
| Tax Type | Sales and Use Tax (state only -- no local sales tax) |
| State Rate | 5.50% (general); 8.00% (short-term auto rental); 9.00% (lodging/prepared food) |
| Local Rates | None |
| Primary Statute | 36 Maine Revised Statutes (M.R.S.) §1811 et seq. |
| Governing Agency | Maine Revenue Services (MRS) |
| Portal | https://www.maine.gov/revenue |
| SST Member | No |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics. T2: lodging/auto rental rate application, service taxability, exemption specifics. T3: audit defense, complex transactions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Maine sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Maine sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Maine? | Drives taxability classification under Maine law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Maine? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Maine local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 Rate Structure -- Multiple Rates [T1]

Maine has a tiered rate structure:

| Category | Rate | Statute |
|----------|------|---------|
| General tangible personal property | 5.50% | 36 M.R.S. §1811 |
| Prepared food (restaurant meals, takeout) | 8.00% | 36 M.R.S. §1811 |
| Short-term lodging (hotels, B&Bs, Airbnb) | 9.00% | 36 M.R.S. §1811 |
| Short-term auto/truck rental | 10.00% | 36 M.R.S. §1811 |

**Note:** The lodging and auto rental rates were increased from 9% to current levels. Verify current rates with MRS. [T2]

### 1.2 No Local Sales Taxes [T1]

Maine does NOT allow local sales taxes. The state rate is the only rate. [T1]

This simplifies compliance -- sellers apply a single rate per category statewide. [T1]

### 1.3 Sourcing [T1]

Maine uses **destination-based** sourcing for remote sales. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food -- EXEMPT [T1]

- Unprepared grocery food and food ingredients: **exempt**. 36 M.R.S. §1760(3). [T1]
- Prepared food (restaurant meals, heated food, food with utensils): taxable at **8%**. [T1]
- Candy: exempt (Maine treats candy as food). [T1]
- Soft drinks: exempt (Maine does not exclude soft drinks from the food exemption). [T1]

**Note:** Maine's treatment of candy and soft drinks as exempt food differs from SST-member states that exclude these items from the food exemption. [T1]

### 2.2 Clothing [T1]

- Clothing is **fully taxable** at the general 5.5% rate. No exemption. [T1]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. 36 M.R.S. §1760(5). [T1]
- OTC drugs: **taxable** (no general OTC exemption). [T1]
- DME: exempt with prescription. [T1]
- Prosthetics: exempt. [T1]

### 2.4 Services [T2]

Maine taxes a limited number of services:

- **Taxable services include:** Telecommunications, cable/satellite TV, fabrication services, installation of TPP (when not exempt), extended warranties/service contracts. [T2]
- **Exempt services include:** Professional services (legal, accounting, medical, engineering), personal care, cleaning/janitorial, repair labor, landscaping. [T2]

### 2.5 SaaS and Digital Goods [T2]

- **SaaS:** Generally **not taxable** in Maine. MRS has not specifically enacted taxation of SaaS. [T2]
- **Canned software (physical):** Taxable. [T1]
- **Canned software (electronic delivery):** Taxable. 36 M.R.S. §1752(17-B). [T1]
- **Digital downloads:** Taxability is limited; Maine has not broadly adopted digital goods taxation. [T2]
- **Custom software:** Exempt. [T2]

### 2.6 Lodging and Short-Term Rentals [T1]

- Hotels, motels, B&Bs, vacation rentals (including Airbnb/VRBO): **9.00%**. [T1]
- The 9% rate applies to transient accommodations (stays of less than a specified period). [T1]
- Short-term rental platforms must collect and remit as marketplace facilitators. [T1]

### 2.7 Auto Rentals [T1]

- Short-term auto and truck rentals: **10.00%**. [T1]
- This is the highest category-specific rate in Maine. [T1]

### 2.8 Manufacturing [T1]

- Machinery and equipment used directly in manufacturing: **exempt**. 36 M.R.S. §1760(31). [T1]
- Fuel and electricity used in manufacturing: exempt for the portion used in production. [T2]

### 2.9 Agricultural [T1]

- Farm machinery and equipment: exempt. 36 M.R.S. §1760(7-B). [T1]
- Feed, seed, fertilizer: exempt. [T1]
- Livestock: exempt. [T1]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | Form ST-7 (Sales/Use Tax Return) |
| Filing Frequencies | Monthly ($400+/month avg liability); Quarterly ($100-$400); Semi-annually or annually (small) |
| Due Date | 15th of the month following the reporting period |
| Portal | https://portal.maine.gov/tax |
| E-filing | Required for most filers |

**Note:** Maine's due date is the **15th**, not the 20th. This is earlier than most states. [T1]

### 4.2 Vendor Discount [T1]

Maine does NOT offer a vendor discount for timely filing. [T1]

### 4.3 Penalties and Interest [T1]

- Late filing penalty: 1% per month, up to 25%. [T1]
- Late payment penalty: 1% per month, up to 25%. [T1]
- Interest: rate set annually by MRS. [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for Maine. Key categories: [T1]

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
| Revenue Threshold | $100,000 in Maine sales |
| Transaction Threshold | 200 transactions |
| Test | OR (either threshold triggers nexus) |
| Measurement Period | Current or prior calendar year |
| Effective Date | July 1, 2018 |

**Statute:** 36 M.R.S. §1951-B.

### 3.2 Physical Nexus [T1]

Standard physical nexus rules apply. Maine's tourism industry means seasonal businesses and temporary presences are common. [T2]

### 3.3 Marketplace Facilitator [T1]

Maine requires marketplace facilitators to collect and remit sales tax. 36 M.R.S. §1951-C. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER apply local tax add-ons in Maine. There are NO local sales taxes. [T1]
- NEVER apply the general 5.5% rate to prepared food (8%), lodging (9%), or auto rentals (10%). Each has its own rate. [T1]
- NEVER tax candy or soft drinks in Maine. They are exempt as food, unlike in SST member states. [T1]
- NEVER file Maine returns by the 20th assuming it matches other states. Maine's due date is the **15th**. [T1]
- NEVER assume SaaS is taxable in Maine. Current law does not tax SaaS. [T2]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Lodging Tax on Seasonal Vacation Rentals [T2]

**Situation:** A property owner rents a lakeside cabin in Maine during summer for $300/night through a direct website.

**Resolution:**
- Short-term lodging is taxable at 9%. [T1]
- Tax = $300 x 9% = $27.00 per night. [T1]
- If booked through a marketplace facilitator (Airbnb, VRBO), the platform collects the tax. [T1]
- If booked directly, the property owner must register with MRS, collect 9%, and file returns. [T1]
- The owner must also comply with any local registration or safety requirements. [T2]
- **Flag for reviewer:** Seasonal vacation rental owners often fail to register. Verify compliance. [T2]

### EC2 -- Candy and Soft Drinks Exempt (Unlike SST States) [T2]

**Situation:** A retailer moving from an SST state to Maine asks whether candy and soft drinks are taxable.

**Resolution:**
- Maine is NOT an SST member and does NOT use SST definitions. [T1]
- In Maine, candy and soft drinks are treated as food and are **exempt** from sales tax. [T1]
- This is the opposite treatment from SST states where candy and soft drinks are excluded from the food exemption. [T1]
- **Flag for reviewer:** Ensure POS systems classify candy and soft drinks as exempt in Maine. [T2]

### EC3 -- Earlier Due Date (15th vs. 20th) [T1]

**Situation:** A multi-state seller files returns on the 20th in most states. Maine's return is due on the 15th.

**Resolution:**
- Maine returns are due on the **15th** of the month following the reporting period. [T1]
- Filing by the 20th (as with most states) would be LATE in Maine, resulting in penalties and interest. [T1]
- **Flag for reviewer:** Calendar Maine's earlier due date separately from other states. [T1]

### EC4 -- Auto Rental vs. Long-Term Vehicle Lease [T2]

**Situation:** A company leases a vehicle for 24 months in Maine. Is the 10% auto rental rate applicable?

**Resolution:**
- The 10% rate applies to short-term auto rentals (typically 30 days or fewer). [T1]
- Long-term leases (more than 30 days) are subject to the general 5.5% sales tax rate. [T2]
- The distinction between short-term rental and long-term lease affects the applicable rate. [T2]
- **Flag for reviewer:** Verify the lease term and whether it qualifies as a short-term rental or long-term lease. [T2]

---

### EC5 -- Vacation Rental Marketplace Facilitator [T2]

**Situation:** A property owner lists a Maine cottage on both Airbnb and their own website. Airbnb collects and remits the 9% lodging tax on its bookings.

**Resolution:**
- Airbnb bookings: Airbnb collects and remits as marketplace facilitator. Owner should NOT also collect. [T1]
- Direct website bookings: Owner must register with MRS, collect 9%, and file returns. [T1]
- The owner must segregate marketplace sales from direct sales on their return. [T1]
- **Flag for reviewer:** Verify that the marketplace is collecting the correct rate (9%) and that the owner is handling direct bookings properly. [T2]

### EC6 -- Bakery Mixed Sales [T2]

**Situation:** A bakery sells both unpackaged pastries (eaten in-store) and packaged baked goods (taken home). Different rates may apply.

**Resolution:**
- Unpackaged pastries consumed on premises (with plates/utensils): prepared food at 8%. [T1]
- Packaged baked goods sold for off-premises consumption: food (exempt in Maine). [T1]
- Items sold without utensils and not heated, for off-premises consumption: food (exempt). [T1]
- **Flag for reviewer:** The prepared food determination depends on eating utensils, heating, and on-premises consumption. [T2]

### EC7 -- Extended Warranty/Service Contract [T2]

**Situation:** A retailer sells a $200 product and a $50 extended warranty/service contract.

**Resolution:**
- Product: taxable at 5.5%. [T1]
- Extended warranty/service contract: taxable at 5.5% (service contracts on TPP are taxable in Maine). [T1]
- Total taxable = $250. Tax = $250 x 5.5% = $13.75. [T1]
- **Flag for reviewer:** Service contracts are a commonly overlooked taxable category. [T2]

---

## Test Suite

### Test 1 -- General Merchandise Sale

**Input:** Seller in Portland sells $800 of clothing. ME rate = 5.5%.
**Expected output:** Clothing is taxable. Tax = $800 x 5.5% = $44.00. Total = $844.00.

### Test 2 -- Restaurant Meal

**Input:** Customer dines at a Bangor restaurant. Bill = $75. Prepared food rate = 8%.
**Expected output:** Tax = $75 x 8% = $6.00. Total = $81.00.

### Test 3 -- Lodging

**Input:** Guest stays 2 nights at a hotel in Bar Harbor at $200/night. Lodging rate = 9%.
**Expected output:** Room = $400. Tax = $400 x 9% = $36.00. Total = $436.00.

### Test 4 -- Grocery and Candy (Both Exempt)

**Input:** Customer buys $100 groceries and $5 candy at a Portland supermarket.
**Expected output:** Both groceries and candy are exempt in Maine. Tax = $0. Total = $105.00.

### Test 5 -- Auto Rental

**Input:** Customer rents a car for 3 days at $60/day in Augusta. Auto rental rate = 10%.
**Expected output:** Rental = $180. Tax = $180 x 10% = $18.00. Total = $198.00.

---

### Test 6 -- Candy Exempt in Maine

**Input:** Customer buys $10 candy at a Portland store.
**Expected output:** Candy is EXEMPT in Maine (treated as food). Tax = $0. Total = $10.00.

### Test 7 -- Vacation Rental (Direct Booking)

**Input:** Guest books directly with a cabin owner for 5 nights at $150/night in Bar Harbor. Lodging rate = 9%.
**Expected output:** Rental = $750. Tax = $750 x 9% = $67.50. Total = $817.50. Owner must collect and remit.

### Test 8 -- Extended Warranty Taxable

**Input:** Retailer sells $500 laptop and $75 extended warranty in Augusta. General rate = 5.5%.
**Expected output:** Both taxable. Tax = ($500 + $75) x 5.5% = $31.63. Total = $606.63.

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
