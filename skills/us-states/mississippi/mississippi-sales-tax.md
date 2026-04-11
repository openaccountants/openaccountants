---
name: mississippi-sales-tax
description: Use this skill whenever asked about Mississippi sales tax, Mississippi use tax, Mississippi DOR sales tax filing, Mississippi grocery tax, Mississippi manufacturing rate, or Mississippi sales tax compliance. Trigger on phrases like "Mississippi sales tax", "MS sales tax", "Miss. Code §27-65", "Mississippi DOR", "Mississippi grocery tax", "Mississippi manufacturing reduced rate", or any request involving Mississippi state sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# Mississippi Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Mississippi, United States |
| Jurisdiction Code | US-MS |
| Tax Type | Sales and Use Tax (state; very limited local) |
| State Rate | 7.00% |
| Maximum Combined Rate | ~7.25% (limited local add-ons in some jurisdictions) |
| Primary Statute | Mississippi Code §27-65-1 et seq. |
| Governing Agency | Mississippi Department of Revenue (DOR) |
| Portal | https://www.dor.ms.gov |
| SST Member | No |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics. T2: reduced rate categories, service taxability, contractor taxation. T3: audit defense, complex manufacturing exemptions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Mississippi sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Mississippi sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Mississippi? | Drives taxability classification under Mississippi law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Mississippi? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Mississippi local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Sales Tax Rate

Mississippi imposes a state sales tax of **7.00%** on the retail sale of tangible personal property and certain services. This is one of the highest standard state rates in the nation. [T1]

**Statute:** Miss. Code §27-65-17.

### 1.2 Reduced Rates [T1]

Mississippi applies reduced rates to certain categories:

| Category | Rate |
|----------|------|
| Manufacturing machinery and equipment | 1.50% |
| Farm implements and parts | 1.50% |
| Motor vehicles | 5.00% (3% for hybrid/electric, subject to change) |
| Aircraft | 3.00% |
| Certain food processing equipment | 1.50% |

### 1.3 Local Sales Taxes [T1]

- Mississippi has very limited local sales tax. Some jurisdictions impose a tourism tax or a special-purpose tax. [T2]
- The Jackson metropolitan area and some resort/tourism areas may have small local add-ons. [T2]
- Local taxes are collected by the state DOR. [T1]

### 1.4 Sourcing [T1]

Mississippi uses **origin-based** sourcing for intrastate sales. For interstate (remote) sales, destination-based sourcing applies. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food -- TAXABLE at Full Rate [T1]

**Mississippi taxes grocery food at the FULL 7% state rate.** [T1]

- Unprepared grocery food: **taxable at 7%**. [T1]
- Prepared food: **taxable at 7%**. [T1]
- There is NO reduced rate or exemption for food in Mississippi. [T1]
- Mississippi is one of only a few states that fully taxes grocery food. [T1]

**Statute:** Miss. Code §27-65-17 (no food exemption).

### 2.2 Clothing [T1]

- Clothing is **fully taxable** at 7%. No exemption. [T1]
- Mississippi holds a sales tax holiday (see Edge Cases). [T2]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. Miss. Code §27-65-111(a). [T1]
- OTC drugs: **taxable** at 7%. [T1]
- DME with prescription: exempt. [T1]
- Prosthetics: exempt. [T1]

### 2.4 Services [T2]

Mississippi taxes a moderate number of services:

- **Taxable services include:** Repair and installation services (for tangible property), cleaning and janitorial, pest control, telecommunications, cable/satellite TV, amusement/recreation, printing, parking/storage. [T2]
- **Exempt services include:** Professional services (legal, accounting, medical, engineering), educational services, financial services, personal care (haircuts, etc.). [T2]

**Important:** Mississippi taxes construction contractors differently -- contractors are generally the end consumers of materials and owe tax on materials purchased. The contractor's labor charge to the customer on real property improvements is generally not subject to sales tax. [T2]

### 2.5 SaaS and Digital Goods [T2]

- **SaaS:** Generally **not taxable** under current Mississippi law. Not considered TPP or an enumerated service. [T2]
- **Canned software (physical):** Taxable. [T1]
- **Canned software (electronic delivery):** Taxability is uncertain. [T2]
- **Digital downloads:** Not specifically taxed. [T2]
- **Custom software:** Exempt. [T2]

### 2.6 Manufacturing -- Reduced Rate [T1]

- Manufacturing machinery, machine parts, and equipment: **1.50%** reduced rate. Miss. Code §27-65-17(1)(d). [T1]
- This is a significant incentive. The 1.5% rate is much lower than the standard 7% rate. [T1]
- The machinery must be used directly in the manufacturing process. [T1]
- Raw materials incorporated into finished products for resale: exempt under resale. [T1]

### 2.7 Motor Vehicles [T1]

- Motor vehicles: **5.00%** (reduced from the 7% general rate). Miss. Code §27-65-17(1)(c). [T1]
- Trade-in credit reduces the taxable amount. [T1]
- Some hybrid/electric vehicle rates may differ. [T2]

### 2.8 Agricultural [T1]

- Farm implements, machinery, and parts: **1.50%** reduced rate. Miss. Code §27-65-17(1)(e). [T1]
- Feed, seed, fertilizer: exempt. [T1]
- Livestock: exempt. [T1]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | Form 72-100 (Sales Tax Return) |
| Filing Frequencies | Monthly (most taxpayers); Quarterly (small taxpayers) |
| Due Date | 20th of the month following the reporting period |
| Portal | https://tap.dor.ms.gov (Taxpayer Access Point) |
| E-filing | Required for most filers |

### 4.2 Vendor Discount [T1]

Mississippi offers a vendor discount of **2%** of the first $2,500 of tax due (maximum $50/month) for timely filing. [T1]

**Statute:** Miss. Code §27-65-33(3).

### 4.3 Penalties and Interest [T1]

- Late filing penalty: 10% of tax due or $25, whichever is greater. [T1]
- Interest: 1% per month (12% per annum). [T1]
- Fraud penalty: 50% of tax due. [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for Mississippi. Key categories: [T1]

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
| Revenue Threshold | $250,000 in Mississippi sales |
| Transaction Threshold | N/A (revenue only) |
| Measurement Period | 12-month period ending on the last day of the month preceding the most recent calendar quarter |
| Effective Date | September 1, 2018 |

**Statute:** Miss. Code §27-67-3(h).

**Note:** Mississippi's $250,000 threshold is higher than the standard $100,000 used by most states. [T1]

### 3.2 Physical Nexus [T1]

Standard physical nexus rules apply. [T1]

### 3.3 Marketplace Facilitator [T1]

Mississippi requires marketplace facilitators to collect and remit sales tax. Miss. Code §27-67-3(i). [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER assume grocery food is exempt in Mississippi. It is taxable at the FULL 7% state rate. [T1]
- NEVER apply the general 7% rate to manufacturing machinery (1.5%), motor vehicles (5%), or farm implements (1.5%). Reduced rates exist for specific categories. [T1]
- NEVER ignore Mississippi's higher economic nexus threshold ($250,000 vs. $100,000). [T1]
- NEVER assume contractors collect sales tax from property owners on real property improvements. Contractors are the end consumers of materials in Mississippi. [T1]
- NEVER assume SaaS is taxable. Mississippi has not specifically addressed SaaS taxation. [T2]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Grocery Food Fully Taxable at 7% [T2]

**Situation:** A multi-state retailer configures POS for Mississippi, assuming food is exempt like most states.

**Resolution:**
- Mississippi taxes ALL food, including unprepared grocery food, at the full 7% rate. [T1]
- POS must be configured to collect 7% on grocery food. [T1]
- There is NO reduced rate or exemption for food at the state level. [T1]
- **Flag for reviewer:** Mississippi, Alabama, and South Dakota are the remaining states that tax food at the full rate. Verify POS configuration. [T2]

### EC2 -- Manufacturing Reduced Rate Application [T2]

**Situation:** A manufacturer purchases a $500,000 CNC machine for its Mississippi plant. Does the 1.5% rate apply?

**Resolution:**
- Manufacturing machinery used directly in the manufacturing process qualifies for the 1.5% rate. [T1]
- Tax = $500,000 x 1.5% = $7,500 (vs. $35,000 at the standard 7% rate). [T1]
- The manufacturer must demonstrate the machine is used directly in manufacturing. [T1]
- Office equipment, vehicles, and general-purpose computers do NOT qualify for the reduced rate. [T1]
- **Flag for reviewer:** Verify that the equipment qualifies under the statutory definition of manufacturing machinery. [T2]

### EC3 -- Contractor Taxation in Mississippi [T2]

**Situation:** A general contractor builds a commercial building. How is sales tax handled?

**Resolution:**
- In Mississippi, the contractor is generally the end consumer of building materials. [T1]
- The contractor pays 7% sales tax on materials at the time of purchase. [T1]
- The contractor does NOT collect sales tax from the property owner on labor or the completed project (real property improvement). [T1]
- Subcontractors purchasing materials also pay tax on their material purchases. [T1]
- **Exception:** Certain government and nonprofit construction projects may qualify for exemptions. [T2]
- **Flag for reviewer:** Construction taxation is complex. Review the specific project type and contractual structure. [T3]

### EC4 -- Sales Tax Holiday [T2]

**Situation:** Mississippi's annual sales tax holiday (typically the last full weekend in July) exempts certain items.

**Resolution:**
- Clothing and footwear under $100 per item: exempt during the holiday. [T1]
- School supplies: exempt during the holiday (verify item list and thresholds). [T2]
- The holiday is set by legislation; dates and items may change annually. [T2]
- **Statute:** Miss. Code §27-65-111(p).
- **Flag for reviewer:** Verify current year's holiday dates, items, and thresholds with DOR. [T2]

---

### EC5 -- Multiple Reduced Rate Categories in One Transaction [T2]

**Situation:** A farm equipment dealer sells both farm implements (1.5% reduced rate) and general accessories (7% standard rate) in a single transaction.

**Resolution:**
- Farm implements: 1.5% rate. [T1]
- General accessories (clothing, tools not qualifying as farm implements): 7% rate. [T1]
- Each item must be classified and taxed at the correct rate. [T1]
- The invoice should separately identify items qualifying for the reduced rate. [T2]
- **Flag for reviewer:** Verify that each item qualifies for the reduced rate. Not all items sold by a farm dealer are "farm implements." [T2]

### EC6 -- Construction Contract in Mississippi [T2]

**Situation:** A contractor builds a warehouse in Jackson for $2 million.

**Resolution:**
- The contractor is the end consumer of building materials. [T1]
- The contractor pays 7% sales tax on all materials purchased. [T1]
- The contractor does NOT collect sales tax from the property owner on the construction contract. [T1]
- Labor charges for real property improvements are not subject to sales tax. [T1]
- Manufacturing equipment installed as part of the building may qualify for the 1.5% reduced rate. [T2]
- **Flag for reviewer:** Complex construction projects may have multiple rate categories. Review material classifications. [T3]

### EC7 -- Aircraft Reduced Rate [T2]

**Situation:** A business purchases a $5 million aircraft based in Mississippi.

**Resolution:**
- Aircraft are subject to a reduced rate of **3%** (not the standard 7%). Miss. Code §27-65-17(1)(f). [T1]
- This applies to fixed-wing aircraft and rotorcraft. [T1]
- The reduced rate is a significant incentive for aviation businesses. [T1]
- **Flag for reviewer:** Verify that the aircraft qualifies for the reduced rate and is based in Mississippi. [T2]

---

## Test Suite

### Test 1 -- Basic Taxable Sale

**Input:** Seller in Jackson sells $1,000 of furniture. State rate = 7%.
**Expected output:** Tax = $1,000 x 7% = $70.00. Total = $1,070.00.

### Test 2 -- Grocery Food at Full Rate

**Input:** Customer buys $200 of unprepared groceries in Biloxi. Rate = 7%.
**Expected output:** Food IS taxable at full rate. Tax = $200 x 7% = $14.00. Total = $214.00.

### Test 3 -- Manufacturing Equipment Reduced Rate

**Input:** Manufacturer buys $100,000 CNC lathe for factory use. Manufacturing rate = 1.5%.
**Expected output:** Tax = $100,000 x 1.5% = $1,500.00. Total = $101,500.00.

### Test 4 -- Motor Vehicle Reduced Rate

**Input:** Customer buys a $25,000 car in Hattiesburg. Vehicle rate = 5%.
**Expected output:** Tax = $25,000 x 5% = $1,250.00. Total = $26,250.00.

### Test 5 -- Economic Nexus Threshold

**Input:** Remote seller from Oregon sold $200,000 to Mississippi customers in the trailing 12 months.
**Expected output:** $200,000 < $250,000 threshold. No economic nexus. No collection obligation based on these facts.

---

### Test 6 -- Farm Implement at Reduced Rate

**Input:** Farmer buys a $30,000 tractor (farm implement) in Tupelo. Farm implement rate = 1.5%.
**Expected output:** Tax = $30,000 x 1.5% = $450.00. Total = $30,450.00.

### Test 7 -- Aircraft Reduced Rate

**Input:** Business purchases $500,000 aircraft based in Jackson. Aircraft rate = 3%.
**Expected output:** Tax = $500,000 x 3% = $15,000.00. Total = $515,000.00.

### Test 8 -- Use Tax on Out-of-State Purchase

**Input:** Mississippi business purchases $10,000 of equipment from Tennessee vendor (no MS tax collected). Rate = 7%.
**Expected output:** Use tax due = $10,000 x 7% = $700.00.

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
