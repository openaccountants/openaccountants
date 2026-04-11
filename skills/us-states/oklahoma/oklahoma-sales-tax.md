---
name: oklahoma-sales-tax
description: Use this skill whenever asked about Oklahoma sales tax, Oklahoma use tax, OTC sales tax filing, Oklahoma grocery tax exemption (2024), or Oklahoma sales tax compliance. Trigger on phrases like "Oklahoma sales tax", "OK sales tax", "68 O.S. §1350", "Oklahoma OTC", "Oklahoma grocery tax", "Oklahoma SST", or any request involving Oklahoma state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# Oklahoma Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Oklahoma, United States |
| Jurisdiction Code | US-OK |
| Tax Type | Sales and Use Tax (state + local) |
| State Rate | 4.50% |
| Maximum Combined Rate | ~11.50% (state 4.5% + county + city + special) |
| Primary Statute | 68 Oklahoma Statutes (O.S.) §1350 et seq. |
| Governing Agency | Oklahoma Tax Commission (OTC) |
| Portal | https://oktap.tax.ok.gov |
| SST Member | Yes -- Full Member |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics. T2: local rate lookups, grocery food transition, service taxability. T3: audit defense, complex exemptions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Oklahoma sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have an Oklahoma sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Oklahoma? | Drives taxability classification under Oklahoma law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Oklahoma? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Oklahoma local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Sales Tax Rate

Oklahoma imposes a state sales tax of **4.50%** on the retail sale of tangible personal property and certain services. [T1]

**Statute:** 68 O.S. §1350 et seq.

### 1.2 Grocery Food -- State Exemption (November 2024) [T1]

Oklahoma's treatment of grocery food has changed:

| Period | State Rate on Grocery Food |
|--------|---------------------------|
| Before November 1, 2024 | 4.50% (full state rate) |
| November 1, 2024 onward | **0.00%** (exempt from state tax) |

- **Local taxes continue to apply** to grocery food at the full local rate. [T1]
- Prepared food remains taxable at the full combined rate. [T1]
- Candy and soft drinks remain taxable at the full rate. [T1]

**Statute:** HB 1955 (2024 session).

### 1.3 Local Sales Taxes [T1]

- Counties, cities, and special jurisdictions impose additional sales tax. [T1]
- Local rates can be substantial, with combined rates reaching **11% or more**. [T1]
- Oklahoma has approximately **600+ local taxing jurisdictions**. [T2]
- OTC administers and collects local taxes alongside state tax. [T1]

### 1.4 Sourcing [T1]

Oklahoma uses **destination-based** sourcing for most sales. [T1]

As an SST member, Oklahoma follows SSUTA sourcing rules. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food -- State Exempt (2024+), Local Applies [T1]

- As of November 1, 2024, grocery food is **exempt from state sales tax**. [T1]
- Local taxes continue to apply. Combined local rates on food can be 3-7%. [T1]
- Prepared food: full 4.5% state + local. [T1]
- Candy: full rate. [T1]
- Soft drinks: full rate. [T1]

### 2.2 Clothing [T1]

- Clothing is **fully taxable**. No exemption. [T1]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. 68 O.S. §1357(9). [T1]
- OTC drugs: **taxable**. [T1]
- DME: exempt with prescription. [T1]
- Prosthetics: exempt. [T1]

### 2.4 Services [T2]

Oklahoma taxes a limited number of services:

- **Taxable services include:** Telecommunications, furnishing rooms/lodging, printing, storage/warehousing, computer programming (when bundled with TPP), car washes. [T2]
- **Exempt services include:** Professional services, personal care, repair labor (when separately stated), cleaning, landscaping, IT consulting. [T2]

### 2.5 SaaS and Digital Goods [T2]

- **SaaS:** Generally **not taxable** under current Oklahoma law. [T2]
- **Canned software (physical):** Taxable. [T1]
- **Canned software (electronic delivery):** Taxable. [T1]
- **Digital downloads:** Taxable as specified digital products (SST definitions). [T1]
- **Custom software:** Exempt. [T2]

### 2.6 Manufacturing [T1]

- Manufacturing machinery and equipment: **exempt** (for machinery used directly and predominantly in manufacturing). 68 O.S. §1359.2. [T1]
- Raw materials for resale: exempt under resale. [T1]
- Repair parts for exempt machinery: exempt. [T1]

### 2.7 Agricultural [T1]

- Farm tractors, implements, and equipment: exempt. 68 O.S. §1358.1. [T1]
- Feed, seed, fertilizer: exempt. [T1]
- Livestock: exempt for breeding/production. [T1]

### 2.8 Oil and Gas [T2]

- Equipment used in oil and gas drilling: subject to sales tax (no broad exemption). [T2]
- Gross production tax on oil and gas production is separate from sales tax. [T2]
- Certain downhole equipment may qualify for exemptions. [T2]
- **Flag for reviewer:** Oil and gas equipment taxability is nuanced. Review specific items against OTC guidance. [T2]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | STS 20002 (Sales Tax Return) |
| Filing Frequencies | Monthly (most common); Semi-annually (small taxpayers) |
| Due Date | 20th of the month following the reporting period |
| Portal | https://oktap.tax.ok.gov (Oklahoma Taxpayer Access Point) |
| E-filing | Required for most filers |

### 4.2 Vendor Discount [T1]

Oklahoma offers a vendor discount of **1%** of tax collected (maximum varies) for timely filing. [T1]

### 4.3 Penalties and Interest [T1]

- Late filing penalty: 25% of tax due. [T1]
- Interest: 1.25% per month (15% per annum). [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for Oklahoma. Key categories: [T1]

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
| Revenue Threshold | $100,000 in Oklahoma sales |
| Transaction Threshold | N/A (revenue only) |
| Measurement Period | Current or prior calendar year |
| Effective Date | July 1, 2018 |

**Statute:** 68 O.S. §1392.

### 3.2 Marketplace Facilitator [T1]

Oklahoma requires marketplace facilitators to collect and remit. 68 O.S. §1401.3. [T1]

### 3.3 SST Registration [T1]

Full SST member. SSTRS and CSPs available. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER apply state sales tax to grocery food after November 1, 2024. It is state-exempt. [T1]
- NEVER forget that local taxes still apply to grocery food. [T1]
- NEVER treat candy or soft drinks as exempt food. They are taxed at the full combined rate. [T1]
- NEVER assume a uniform rate across Oklahoma. Combined rates vary widely by location. [T1]
- NEVER assume SaaS is taxable in Oklahoma. Current law does not tax SaaS. [T2]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Grocery Food Transition (2024) [T2]

**Situation:** A grocery retailer needs to update POS systems for the November 2024 state food exemption.

**Resolution:**
- As of November 1, 2024, state tax on grocery food = 0%. [T1]
- Local taxes still apply at full rates. [T1]
- POS must classify items as food (0% state + local) or non-food (4.5% state + local). [T1]
- Candy and soft drinks are NOT food -- full rate applies. [T1]
- **Flag for reviewer:** Verify current effective date and POS configuration. [T2]

### EC2 -- High Combined Local Rates [T2]

**Situation:** Buyer in Oklahoma City complains about a 9%+ combined rate on a purchase.

**Resolution:**
- Oklahoma allows stacking of state + county + city + special district taxes. [T1]
- Combined rates can exceed 10% in some areas. [T1]
- The seller must apply the correct combined rate for the delivery address. [T1]
- **Flag for reviewer:** Use OTC rate lookup tools for precise rates. [T2]

### EC3 -- Oil and Gas Equipment Taxability [T2]

**Situation:** An oil company purchases $1 million in drilling equipment for use in Oklahoma.

**Resolution:**
- Most drilling equipment is subject to sales tax at the full combined rate. [T2]
- Some specific downhole equipment categories may qualify for exemptions. [T2]
- The gross production tax on oil/gas is a separate obligation. [T1]
- **Flag for reviewer:** Oil and gas equipment exemptions are narrow and fact-specific. Review each item against OTC guidance. [T2]

### EC4 -- Sales Tax Holiday [T2]

**Situation:** Oklahoma's sales tax holiday (typically first full weekend in August) exempts certain items.

**Resolution:**
- Clothing under $100 per item: exempt from state tax during the holiday. [T1]
- Some local jurisdictions may or may not participate. [T2]
- Verify current year's dates, items, and thresholds with OTC. [T2]

---

### EC5 -- Tribal Sales within Indian Country [T3]

**Situation:** A sale occurs within tribal land (Indian Country) in Oklahoma. Is Oklahoma sales tax due?

**Resolution:**
- Sales by tribal businesses to tribal members within Indian Country may be exempt from Oklahoma sales tax. [T2]
- Sales to non-tribal members within Indian Country are generally subject to Oklahoma sales tax. [T2]
- Tribal compact agreements govern the tax treatment. [T3]
- Oklahoma has compacts with various tribes that address tobacco, motor fuel, and sales tax. [T3]
- **Flag for reviewer:** Tribal taxation in Oklahoma is governed by compact agreements and is highly complex. Escalate to a specialist. [T3]

### EC6 -- Lodging and Tourism [T2]

**Situation:** A hotel in Oklahoma City charges $120/night. What taxes apply?

**Resolution:**
- State sales tax: 4.5%. [T1]
- Local sales tax: varies by city (OKC may have 4%+ local). [T1]
- Additional local lodging/tourism tax may apply. [T2]
- Combined effective tax on hotel rooms can exceed 12%. [T2]
- **Flag for reviewer:** Hotel taxation includes both general sales tax and potentially separate lodging taxes. Verify all applicable taxes. [T2]

### EC7 -- Use Tax on Vehicles Purchased Out of State [T2]

**Situation:** An Oklahoma resident purchases a vehicle in Texas and brings it to Oklahoma.

**Resolution:**
- Oklahoma use tax applies at the time of registration/title transfer. [T1]
- Credit is given for sales tax paid to the other state. [T1]
- If Texas tax paid < Oklahoma combined rate, the difference is due as use tax. [T1]
- If Texas tax paid >= Oklahoma rate, no additional use tax is due. [T1]
- **Flag for reviewer:** Vehicle use tax credit calculations require verification of the exact tax paid to the other state. [T2]

---

## Test Suite

### Test 1 -- Basic Taxable Sale

**Input:** Seller in Oklahoma City sells $800 of furniture. Combined rate = 8.625% (4.5% state + 4.125% local).
**Expected output:** Tax = $800 x 8.625% = $69.00. Total = $869.00.

### Test 2 -- Grocery Food (2024+ Exemption)

**Input:** Customer buys $200 of unprepared groceries in Tulsa. State food rate = 0%. Local rate = 4.5%.
**Expected output:** State tax = $0. Local tax = $200 x 4.5% = $9.00. Total = $209.00.

### Test 3 -- Candy at Full Rate

**Input:** Customer buys $10 candy in OKC. Combined rate = 8.625%.
**Expected output:** Candy is NOT food. Tax = $10 x 8.625% = $0.86. Total = $10.86.

### Test 4 -- Economic Nexus

**Input:** Remote seller sold $110,000 to Oklahoma in the prior year.
**Expected output:** $110,000 exceeds $100,000. Nexus IS triggered. Must register.

### Test 5 -- Manufacturing Exemption

**Input:** Manufacturer buys $50,000 of production machinery for Oklahoma plant.
**Expected output:** Manufacturing machinery is exempt. Tax = $0.

---

### Test 6 -- Oil Field Equipment Taxable

**Input:** Oil company purchases $100,000 drilling equipment for Oklahoma well. Combined rate = 8.5%.
**Expected output:** Drilling equipment is generally taxable. Tax = $100,000 x 8.5% = $8,500. Total = $108,500.

### Test 7 -- Hotel Room with Multiple Taxes

**Input:** Guest stays at OKC hotel. Room = $100/night. Combined sales tax = 8.5%. Additional local lodging tax = 3.5%. Total = 12%.
**Expected output:** Tax = $100 x 12% = $12.00. Total = $112.00/night.

### Test 8 -- Vehicle Use Tax Credit

**Input:** Oklahoma resident bought car in Texas for $20,000, paid $1,650 TX sales tax (8.25%). Oklahoma combined rate for their location = 8.5%.
**Expected output:** OK use tax = $20,000 x 8.5% = $1,700. Credit for TX tax paid = $1,650. Additional OK use tax due = $50.

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

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
