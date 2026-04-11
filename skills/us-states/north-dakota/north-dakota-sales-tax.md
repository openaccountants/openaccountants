---
name: north-dakota-sales-tax
description: Use this skill whenever asked about North Dakota sales tax, North Dakota use tax, ND Tax Commissioner sales tax filing, or North Dakota sales tax compliance. Trigger on phrases like "North Dakota sales tax", "ND sales tax", "NDCC §57-39.2", "ND Tax Commissioner", "North Dakota SST", or any request involving North Dakota state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# North Dakota Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | North Dakota, United States |
| Jurisdiction Code | US-ND |
| Tax Type | Sales and Use Tax (state + local) |
| State Rate | 5.00% |
| Maximum Combined Rate | ~8.50% (state 5% + city up to 3.5%) |
| Primary Statute | North Dakota Century Code (NDCC) §57-39.2 |
| Governing Agency | Office of State Tax Commissioner |
| Portal | https://www.tax.nd.gov |
| SST Member | Yes -- Full Member |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics. T2: local rate determination, oil/gas industry, exemption specifics. T3: audit defense, complex energy transactions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any North Dakota sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a North Dakota sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in North Dakota? | Drives taxability classification under North Dakota law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in North Dakota? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple North Dakota local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Sales Tax Rate

North Dakota imposes a state sales tax of **5.00%** on the retail sale of tangible personal property and certain services. [T1]

**Statute:** NDCC §57-39.2-02.1.

### 1.2 Local Sales Taxes [T1]

- Cities may impose a local option city sales tax of up to **3.5%** (voter approved). [T1]
- Most ND cities impose a local tax between 0.5% and 2.5%. [T1]
- Fargo: 2% city tax (combined 7%). Bismarck: 2% city tax (combined 7%). [T1]
- Williston and other oil-producing cities may have higher local rates due to infrastructure needs. [T2]
- Local taxes are administered by the Tax Commissioner's office. [T1]

### 1.3 Sourcing [T1]

North Dakota uses **destination-based** sourcing. [T1]

As an SST member, North Dakota follows SSUTA sourcing rules. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food -- EXEMPT [T1]

- Unprepared grocery food: **exempt**. NDCC §57-39.2-04(57). [T1]
- Prepared food: taxable at full combined rate. [T1]
- Candy: taxable. [T1]
- Soft drinks: taxable. [T1]
- North Dakota follows SST food definitions. [T1]

### 2.2 Clothing [T1]

- Clothing is **fully taxable**. No exemption. [T1]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. NDCC §57-39.2-04(3). [T1]
- OTC drugs: **exempt**. [T1]
- DME: exempt. [T1]
- Prosthetics: exempt. [T1]

### 2.4 Services [T2]

North Dakota taxes a limited number of services:

- **Taxable services include:** Amusement/recreation, repair of TPP, installation, telecommunications, cable/satellite, lodging, car washes, printing. [T2]
- **Exempt services include:** Professional services (legal, accounting, medical, engineering), personal care, cleaning/janitorial, landscaping. [T2]

### 2.5 SaaS and Digital Goods [T2]

- **SaaS:** Generally **not taxable** under current ND law. [T2]
- **Canned software (physical):** Taxable. [T1]
- **Canned software (electronic delivery):** Taxable. [T1]
- **Digital downloads:** Taxable as specified digital products under SST. [T1]
- **Custom software:** Exempt. [T2]

### 2.6 Manufacturing [T1]

- Manufacturing machinery and equipment: **exempt**. NDCC §57-39.2-04(29). [T1]
- Replacement parts for exempt manufacturing equipment: exempt. [T1]
- Plant expansion/modernization: eligible for additional exemptions. [T2]

### 2.7 Oil and Gas Industry [T2]

- Oil and gas well equipment and supplies: generally taxable. [T2]
- Specific exemptions may apply to new well drilling equipment under certain incentive programs. [T2]
- Oil extraction tax and gross production tax are separate from sales tax. [T2]
- **Flag for reviewer:** Oil and gas tax compliance in North Dakota involves multiple tax types. Escalate complex scenarios. [T3]

### 2.8 Agricultural [T1]

- Farm machinery and equipment: exempt. NDCC §57-39.2-04(26). [T1]
- Feed, seed, fertilizer: exempt. [T1]
- Livestock: exempt. [T1]
- Irrigation equipment: exempt. [T1]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | Form ST (Sales Tax Return) |
| Filing Frequencies | Monthly (>$500/quarter avg); Quarterly ($83-$500); Annually (<$83) |
| Due Date | Last day of the month following the reporting period |
| Portal | https://www.tax.nd.gov (Taxpayer Access Point) |
| E-filing | Required for most filers |

### 4.2 Vendor Discount [T1]

North Dakota does NOT offer a vendor discount for timely filing. [T1]

### 4.3 Penalties and Interest [T1]

- Late filing/payment penalty: 5% of tax due. [T1]
- Interest: 12% per annum. [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for North Dakota. Key categories: [T1]

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
| Revenue Threshold | $100,000 in North Dakota sales |
| Transaction Threshold | N/A (revenue only -- removed transaction test) |
| Measurement Period | Current or prior calendar year |
| Effective Date | October 1, 2018 |

**Statute:** NDCC §57-39.2-02.2.

### 3.2 Marketplace Facilitator [T1]

North Dakota requires marketplace facilitators to collect and remit. NDCC §57-39.2-02.3. [T1]

### 3.3 SST Registration [T1]

Full SST member. Register via SSTRS. CSPs available. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER tax grocery food in North Dakota. Unprepared food is exempt. [T1]
- NEVER assume a uniform rate across ND. City tax rates vary. [T1]
- NEVER tax OTC drugs in North Dakota. They are exempt. [T1]
- NEVER assume SaaS is taxable. ND does not tax SaaS under current law. [T2]
- NEVER confuse digital downloads (taxable) with SaaS subscriptions (not taxable). [T2]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Oil-Producing City Tax Rates [T2]

**Situation:** A supplier sells equipment to a company in Williston, ND. What combined rate applies?

**Resolution:**
- Williston has a city sales tax that, combined with the 5% state rate, creates a combined rate that may be higher than Fargo or Bismarck. [T2]
- Verify the current city rate for Williston and any special district taxes. [T2]
- **Flag for reviewer:** Oil-boom cities may change rates more frequently than other jurisdictions. Verify current rates. [T2]

### EC2 -- Agricultural Equipment vs. General Equipment [T2]

**Situation:** A rancher buys a utility vehicle (UTV) used both on the farm and for personal recreation.

**Resolution:**
- Farm machinery used primarily in agricultural production is exempt. [T1]
- A UTV used for dual purposes may not qualify if personal use exceeds agricultural use. [T2]
- The exemption requires the equipment to be used "exclusively or primarily" in farming/ranching. [T2]
- **Flag for reviewer:** Mixed-use equipment requires analysis of primary use. [T2]

### EC3 -- Digital Products Under SST [T1]

**Situation:** An online seller sells e-books and digital music to North Dakota customers.

**Resolution:**
- Digital downloads are taxable as specified digital products under SST definitions. [T1]
- The seller must collect tax at the combined rate for the buyer's delivery address. [T1]
- SaaS is NOT taxable, but digital downloads (transferred electronically) ARE. [T2]
- **Flag for reviewer:** Distinguish between SaaS access (not taxable) and digital product downloads (taxable). [T2]

### EC4 -- OTC Drug Exemption [T1]

**Situation:** A retailer asks whether OTC medications are taxable in North Dakota.

**Resolution:**
- OTC drugs are exempt in North Dakota. NDCC §57-39.2-04(3). [T1]
- Dietary supplements are NOT OTC drugs and remain taxable. [T2]
- **Flag for reviewer:** Ensure POS distinguishes between OTC drugs (exempt) and dietary supplements (taxable). [T2]

---

### EC5 -- Lodging Tax [T2]

**Situation:** A hotel in Fargo charges $150/night. What taxes apply?

**Resolution:**
- State sales tax: 5% + Fargo city tax: 2% = 7% combined sales tax. [T1]
- North Dakota also imposes a **state lodging tax of 1%** in addition to sales tax. NDCC §57-40.1. [T1]
- Plus local lodging taxes may also apply. [T2]
- Total effective tax on lodging can exceed 8%. [T2]
- **Flag for reviewer:** Hotel taxation includes both general sales tax and separate lodging taxes. [T2]

### EC6 -- Agricultural Cooperative Sales [T2]

**Situation:** A farm cooperative sells fuel and supplies to member farmers.

**Resolution:**
- Farm machinery and equipment: exempt. [T1]
- Feed, seed, fertilizer: exempt. [T1]
- Fuel used in agricultural production: exempt or reduced rate. [T2]
- General merchandise sold by the cooperative (clothing, food): taxable at standard rates. [T1]
- **Flag for reviewer:** Cooperative sales must be classified item-by-item. Not everything sold by a farm cooperative is exempt. [T2]

### EC7 -- Seasonal Tourism Businesses [T2]

**Situation:** A seasonal retail business operates only during the summer in a tourist area near Theodore Roosevelt National Park.

**Resolution:**
- The business must register for ND sales tax before opening. [T1]
- Filing frequency may be adjusted for seasonal operation. [T2]
- The business must collect the correct city rate for its location. [T1]
- During the off-season, the business should continue to file $0 returns or request inactive status. [T2]
- **Flag for reviewer:** Seasonal businesses should not simply stop filing during the off-season without notifying the Tax Commissioner. [T2]

---

## Test Suite

### Test 1 -- Basic Sale in Fargo

**Input:** Seller in Fargo sells $500 of electronics. Combined rate = 7% (5% state + 2% city).
**Expected output:** Tax = $500 x 7% = $35.00. Total = $535.00.

### Test 2 -- Grocery Food Exemption

**Input:** Customer buys $150 of unprepared groceries in Bismarck.
**Expected output:** Groceries are EXEMPT. Tax = $0. Total = $150.00.

### Test 3 -- OTC Drug Exemption

**Input:** Customer buys $25 OTC allergy medicine in Minot.
**Expected output:** OTC drugs are exempt. Tax = $0. Total = $25.00.

### Test 4 -- Digital Download Taxable

**Input:** Customer downloads $10 e-book. Buyer in Grand Forks. Combined rate = 7.5%.
**Expected output:** Digital downloads are taxable. Tax = $10 x 7.5% = $0.75. Total = $10.75.

### Test 5 -- Economic Nexus

**Input:** Remote seller from Oregon sold $95,000 to ND in the prior year.
**Expected output:** $95,000 < $100,000 threshold. No economic nexus. No collection obligation.

---

### Test 6 -- Lodging with Additional Tax

**Input:** Guest stays 2 nights at a Bismarck hotel at $120/night. Combined sales tax = 7%. State lodging tax = 1%.
**Expected output:** Sales tax = $240 x 7% = $16.80. Lodging tax = $240 x 1% = $2.40. Total tax = $19.20. Total = $259.20.

### Test 7 -- Farm Equipment Exempt

**Input:** Farmer buys a $45,000 combine for agricultural use.
**Expected output:** Farm machinery is exempt. Tax = $0. Total = $45,000.

### Test 8 -- Dietary Supplement Taxable vs. OTC Drug Exempt

**Input:** Customer buys $30 OTC allergy medicine and $25 dietary supplement (vitamins) in Fargo. Combined rate = 7%.
**Expected output:** OTC medicine: exempt. Dietary supplement: taxable. Tax = $25 x 7% = $1.75. Total = $56.75.

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
