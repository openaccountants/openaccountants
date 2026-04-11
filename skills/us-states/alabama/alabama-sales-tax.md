---
name: alabama-sales-tax
description: Use this skill whenever asked about Alabama sales tax, Alabama use tax, Alabama sales tax nexus, ADOR sales tax filing, self-administered city taxes in Alabama, or Alabama grocery food taxation. Trigger on phrases like "Alabama sales tax", "AL sales tax", "ADOR", "Code of Ala. §40-23", "Alabama local tax", "Alabama grocery tax", "self-administered cities Alabama", or any request involving Alabama state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# Alabama Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Alabama, United States |
| Jurisdiction Code | US-AL |
| Tax Type | Sales and Use Tax (state + local) |
| State Rate | 4.00% |
| Maximum Combined Rate | ~11.00% (state 4% + county + city) |
| Primary Statute | Code of Alabama §40-23 (Sales Tax); §40-23-60 et seq. (Use Tax) |
| Governing Agency | Alabama Department of Revenue (ADOR) |
| Portal | https://myalabamataxes.alabama.gov |
| Industry Body | N/A (Alabama is NOT an SST member state) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics. T2: self-administered city compliance, local rate lookups, service taxability. T3: audit defense, complex local sourcing, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Alabama sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have an Alabama sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Alabama? | Drives taxability classification under Alabama law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Alabama? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Alabama local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Sales Tax Rate

Alabama imposes a state sales tax rate of **4.00%** on the retail sale of tangible personal property and certain services. [T1]

**Statute:** Code of Ala. §40-23-2.

### 1.2 Local Sales Taxes -- The Layering Problem [T1/T2]

Alabama has one of the most complex local tax structures in the United States:

- **Counties** may levy their own sales tax (rates vary from 0% to 5%). [T1]
- **Cities** may levy additional sales tax (rates vary from 0% to 6%). [T1]
- **Special districts** may add further levies. [T2]
- Combined state + local rates can reach approximately **11%** in some jurisdictions. [T1]
- There are approximately **400+ local taxing jurisdictions** in Alabama. [T2]

### 1.3 Self-Administered Cities -- Alabama's Unique Feature [T2]

Alabama is unique among US states because many cities **self-administer** their local sales taxes rather than relying on ADOR for collection:

- Approximately **200+ cities** self-administer their sales tax. [T2]
- Self-administered cities include Birmingham, Montgomery, Huntsville, Mobile, Tuscaloosa, and many smaller municipalities. [T2]
- Sellers must register **separately** with each self-administered city where they have nexus. [T1]
- Sellers must file **separate returns** with each self-administered city. [T1]
- Each self-administered city may have its own exemptions, definitions, and audit procedures. [T2]
- ADOR administers state tax and the local tax for non-self-administered jurisdictions. [T1]

**Practical impact:** A seller with nexus in Alabama may need to file with ADOR for state tax AND file separately with 10-20+ self-administered cities. This creates significant compliance burden. [T2]

**Source:** ADOR Local Tax Division; Alabama League of Municipalities.

### 1.4 Sourcing [T1]

Alabama is a **destination-based** sourcing state for sales tax purposes. The tax rate applied is based on the delivery address of the buyer. [T1]

For intrastate sales, the rate at the ship-to address controls. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food -- TAXABLE at Full Rate [T1]

**Alabama is one of only a few US states that taxes grocery food at the FULL state rate of 4%.** [T1]

- Unprepared grocery food is taxable at 4% state + applicable local rates. [T1]
- There is no reduced rate for food in Alabama at the state level. [T1]
- Some local jurisdictions may exempt or reduce the rate on food, but this is not uniform. [T2]
- Prepared food is also taxable at the full combined rate. [T1]

**Statute:** Code of Ala. §40-23-2 (no food exemption in the sales tax act).

**Note:** This is a critical distinction from most other states. Alabama, Mississippi, and South Dakota are among the few states that fully tax grocery food at the state level. [T1]

### 2.2 Clothing [T1]

- Clothing is **fully taxable** in Alabama. No exemption exists. [T1]
- Alabama does not hold a clothing-specific sales tax holiday, though it does have a general back-to-school sales tax holiday (see Edge Cases). [T2]

### 2.3 Prescription Drugs and Medical Devices [T1]

- Prescription drugs are **exempt** from Alabama sales tax. Code of Ala. §40-23-4(a)(11). [T1]
- Over-the-counter (OTC) drugs are **taxable**. [T1]
- Durable medical equipment (DME) prescribed by a physician: exempt. [T1]
- Prosthetics and hearing aids: exempt with prescription. [T1]

### 2.4 Services [T2]

Alabama taxes relatively few services:

- **Taxable services:** Rental of tangible personal property, lodging (4% state + local), amusement/entertainment, storage, automotive repair labor (taxable when combined with parts). [T2]
- **Generally exempt services:** Professional services (legal, accounting, medical, engineering), personal care services, information services. [T2]
- **Utility services:** Electricity and gas sold for domestic use are taxable at a reduced rate. Industrial use of electricity may be exempt under certain conditions. Code of Ala. §40-23-4(a)(10). [T2]

### 2.5 SaaS and Digital Goods [T2]

- **SaaS:** Alabama has not issued comprehensive guidance on SaaS taxability. Under current interpretation, SaaS is generally **not taxable** because it is not considered tangible personal property. [T2]
- **Canned software (physical media):** Taxable as TPP. [T1]
- **Canned software (electronic delivery):** Taxability is unclear; ADOR has not issued definitive guidance. [T2]
- **Digital downloads (music, e-books):** Generally not taxable under current law, but this is an evolving area. [T2]

### 2.6 Manufacturing [T2]

- Machinery used in manufacturing is subject to a **reduced state rate** of 1.5% (instead of 4%). Code of Ala. §40-23-2(3). [T1]
- Raw materials consumed in manufacturing are generally exempt when incorporated into the finished product for resale. [T1]
- Pollution control equipment used in manufacturing is exempt. [T2]

### 2.7 Motor Vehicles [T1]

- Motor vehicles are subject to sales tax at the time of purchase/registration. [T1]
- Trade-in value reduces the taxable amount. [T1]
- Private-party sales are subject to use tax at the same rates. [T1]

### 2.8 Agricultural Products [T1]

- Farm machinery and equipment: exempt from state sales tax. Code of Ala. §40-23-4(a)(7). [T1]
- Feed, seed, fertilizer, and insecticides used in agriculture: exempt. [T1]
- Livestock: exempt when purchased for breeding or dairy purposes. [T1]

---

## Step 3: Return Form Structure
### 4.1 State Filing [T1]

| Field | Detail |
|-------|--------|
| Return Form | Form 2100 (monthly/quarterly); SSUT filers use Form SSUT-1 |
| Filing Frequencies | Monthly (>$2,400/year liability); Quarterly ($200-$2,400/year); Annually (<$200/year) |
| Due Date | 20th of the month following the reporting period |
| Portal | https://myalabamataxes.alabama.gov |
| E-filing | Required for most filers |

### 4.2 Local Filing (Self-Administered Cities) [T2]

- Each self-administered city has its own return form, due date, and portal. [T2]
- Many self-administered cities use third-party platforms (e.g., My Alabama Taxes municipal portal, ONE SPOT). [T2]
- **ONE SPOT:** Alabama's One Spot system allows filing state and some local returns through a single portal. Not all self-administered cities participate. [T2]
- Filing frequency for local returns may differ from state filing frequency. [T2]

### 4.3 Vendor Discount [T1]

Alabama offers a vendor discount (timely filing discount) of **5%** of the first $100 of tax due, plus 2% of any additional tax due, capped at specific amounts based on filing frequency. [T1]

**Statute:** Code of Ala. §40-23-36.

### 4.4 Penalties and Interest [T1]

- Late filing penalty: 10% of tax due or $50, whichever is greater. [T1]
- Interest: 1% per month (12% per annum) on unpaid tax. [T1]
- Fraud penalty: 50% of tax due. [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for Alabama. Key categories: [T1]

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
| Revenue Threshold | $250,000 in Alabama sales |
| Transaction Threshold | N/A (revenue only) |
| Measurement Period | Prior calendar year |
| Effective Date | October 1, 2018 |

**Statute:** Code of Ala. §40-23-190 et seq. (Simplified Sellers Use Tax Remittance Act).

**Note:** Alabama's threshold of $250,000 is higher than the standard $100,000 used by most states. [T1]

### 3.2 Physical Nexus [T1]

Standard physical nexus rules apply: office, warehouse, employees, inventory, or agents in Alabama create collection obligations. [T1]

### 3.3 Simplified Sellers Use Tax (SSUT) [T1]

Alabama offers the **Simplified Sellers Use Tax (SSUT)** program for remote sellers:

- Remote sellers may elect to collect a flat **8% simplified sellers use tax** on all Alabama sales. [T1]
- This flat rate replaces the need to determine and collect the precise combined rate for each delivery address. [T1]
- SSUT filers file a **single return** with ADOR (no separate city filings required). [T1]
- ADOR distributes the collected tax to the appropriate local jurisdictions. [T1]
- This is a **voluntary** election for qualifying remote sellers; not all sellers qualify. [T2]
- Sellers with physical presence in Alabama may not qualify for SSUT. [T2]

**Source:** ADOR SSUT Program; Code of Ala. §40-23-191.

### 3.4 Marketplace Facilitator [T1]

Alabama requires marketplace facilitators to collect and remit sales tax (including SSUT) on sales made through their platforms on behalf of third-party sellers. Effective January 1, 2019. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER assume grocery food is exempt in Alabama. It is taxable at the full state and local rate. [T1]
- NEVER file only with ADOR if the seller has physical nexus in self-administered cities. Separate local filings are required unless the seller qualifies for SSUT. [T1]
- NEVER assume state exemptions automatically apply to self-administered city taxes. Local rules may differ. [T2]
- NEVER advise a remote seller to register with individual Alabama cities without first evaluating the SSUT program. SSUT dramatically simplifies compliance. [T2]
- NEVER apply a single combined rate across all Alabama locations. Rates vary by precise delivery address. [T1]
- NEVER confuse the SSUT flat 8% rate with the actual combined rate. They are different and serve different purposes. [T1]
- NEVER ignore Alabama's higher economic nexus threshold ($250,000 vs. $100,000 in most states). [T1]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Self-Administered City Registration for Remote Sellers [T2]

**Situation:** An e-commerce seller exceeds Alabama's $250,000 economic nexus threshold. Must they register with each self-administered city?

**Resolution:**
- If the seller elects SSUT, they file ONLY with ADOR at the flat 8% rate. No separate city registrations are required. [T1]
- If the seller does NOT elect SSUT, they must determine the correct combined rate for each delivery address and may need to register with each self-administered city where they make deliveries. [T2]
- **Recommendation:** Remote sellers should strongly consider the SSUT program to avoid the burden of multiple local registrations and filings. [T2]
- **Flag for reviewer:** Verify the seller's eligibility for SSUT before advising. Physical presence sellers may not qualify. [T2]

### EC2 -- Grocery Food Taxed at Full Rate -- Client Surprise [T2]

**Situation:** A multi-state retailer assumes grocery food is exempt in Alabama based on their experience in other states.

**Resolution:**
- Alabama taxes grocery food at the full state rate of 4% plus applicable local rates. [T1]
- The retailer must configure their POS system to charge tax on grocery food items for Alabama locations. [T1]
- Failure to collect tax on groceries results in the seller being liable for the uncollected amount. [T1]
- **Flag for reviewer:** Remind clients that Alabama, Mississippi, and South Dakota are among the few states taxing groceries at the full rate. Verify POS configuration. [T2]

### EC3 -- Different Local Exemptions by Self-Administered City [T2]

**Situation:** A seller operates in Birmingham and Huntsville. Birmingham exempts a specific category of goods from its local tax; Huntsville does not.

**Resolution:**
- Each self-administered city can establish its own exemptions independent of the state. [T2]
- The seller must track and apply different exemption rules for each city. [T2]
- This creates compliance complexity that does not exist in states with centralized local tax administration. [T2]
- **Flag for reviewer:** When a client operates in multiple Alabama cities, review local ordinances for each city. Do not assume state exemptions apply locally. [T2]

### EC4 -- Sales Tax Holiday in Alabama [T2]

**Situation:** During Alabama's back-to-school sales tax holiday (typically the third full weekend in July), a retailer asks which items qualify.

**Resolution:**
- Alabama's sales tax holiday exempts: clothing ($100 or less per item), computers/tablets ($750 or less per item), school supplies ($50 or less per item), books ($30 or less per item). [T1]
- The exemption applies to state tax; some self-administered cities may or may not participate. [T2]
- Verify the current year's items, thresholds, and participating localities before applying. [T2]
- **Statute:** Code of Ala. §40-23-211.

### EC5 -- SSUT Rate vs. Actual Combined Rate [T2]

**Situation:** A remote seller collects the flat 8% SSUT rate. The actual combined rate in the buyer's city is 10%. The buyer complains they were undercharged, or a competitor at a physical location charges a higher rate.

**Resolution:**
- The SSUT flat rate of 8% is the legally authorized rate for qualifying remote sellers. [T1]
- The buyer does NOT owe additional use tax on the difference. [T1]
- Local jurisdictions may receive less revenue from SSUT sales than from in-state sales, but this is by design. [T1]
- The seller is in full compliance by collecting the 8% SSUT rate. [T1]
- **Flag for reviewer:** The SSUT rate is a simplification; it is not the same as the actual combined rate. This is lawful and intentional. [T1]

---

### EC6 -- Vending Machine Sales [T2]

**Situation:** A vending machine operator places machines in multiple Alabama cities.

**Resolution:**
- Vending machine sales of food and beverages are subject to sales tax. [T1]
- The operator must determine the local rate for each machine location. [T1]
- If machines are in self-administered cities, the operator may need to register with each city. [T2]
- Food sold through vending machines remains taxable (no food exemption). [T1]
- **Flag for reviewer:** Vending machine operators face the same multi-jurisdiction burden as other sellers. Consider SSUT eligibility. [T2]

### EC7 -- Contractor Purchasing Materials in Alabama [T2]

**Situation:** An out-of-state contractor purchases building materials at an Alabama hardware store for a construction project in Alabama.

**Resolution:**
- Alabama generally treats contractors as the end consumers of building materials. [T1]
- The contractor pays sales tax on materials at the time of purchase. [T1]
- If the materials are for a project in a different city/county than the purchase location, the sourcing rules determine which rate applies. [T2]
- The contractor does NOT collect sales tax from the property owner on real property improvements (labor + installed materials). [T1]
- **Flag for reviewer:** Construction contract taxation in Alabama varies by contract type. Review specific project details. [T3]

---

## Test Suite

### Test 1 -- Basic Taxable Sale in Alabama

**Input:** Seller in Tuscaloosa sells $500 of office supplies to a local buyer. Combined Tuscaloosa rate = 9% (4% state + 5% local).
**Expected output:** Sales tax = $500 x 9% = $45.00. Total = $545.00. Seller remits state portion to ADOR and local portion to Tuscaloosa (self-administered city).

### Test 2 -- Grocery Food Taxation

**Input:** Buyer purchases $100 of unprepared grocery food at a store in Birmingham. Combined Birmingham rate = 10% (4% state + 6% local).
**Expected output:** Grocery food is TAXABLE at the full combined rate. Sales tax = $100 x 10% = $10.00. Total = $110.00.

### Test 3 -- SSUT Remote Seller

**Input:** E-commerce seller based in Oregon has $300,000 in Alabama sales. Elects SSUT. Sells a $200 item to a buyer in a city with a 9.5% actual combined rate.
**Expected output:** Seller collects SSUT flat rate of 8%. Tax = $200 x 8% = $16.00. Total = $216.00. Single return filed with ADOR.

### Test 4 -- Prescription Drug Exemption

**Input:** Pharmacy sells $50 prescription medication and $20 OTC pain reliever in Huntsville. Combined rate = 9%.
**Expected output:** Prescription drug: exempt, $0 tax. OTC pain reliever: taxable. Tax = $20 x 9% = $1.80. Total charged = $71.80.

### Test 5 -- Manufacturing Equipment Reduced Rate

**Input:** Manufacturer purchases $100,000 of machinery for use directly in manufacturing at an Alabama plant. Combined local rate = 5%.
**Expected output:** State rate reduced to 1.5% for manufacturing machinery. Local rate applies at full local rate (5%). Combined = 6.5%. Tax = $100,000 x 6.5% = $6,500.00.

### Test 6 -- Economic Nexus Threshold

**Input:** Online retailer based in Texas sold $200,000 into Alabama in the prior calendar year.
**Expected output:** $200,000 < $250,000 Alabama threshold. No economic nexus. No Alabama sales tax collection obligation based on these facts alone.

---

### Test 7 -- Sales Tax Holiday (State Participating, City Not)

**Input:** During the sales tax holiday, a customer buys a $90 pair of shoes in a self-administered city that has NOT opted into the holiday. State rate = 4%, local rate = 5%. Holiday exempts state tax on qualifying clothing under $100.
**Expected output:** State tax = $0 (holiday exemption). Local tax = $90 x 5% = $4.50 (city did not participate). Total tax = $4.50. Total = $94.50.

### Test 8 -- Vending Machine Sale

**Input:** Vending machine sells a $2.00 snack in Montgomery. Combined rate = 10% (4% state + 6% local).
**Expected output:** Food is taxable in Alabama (including vending). Tax = $2.00 x 10% = $0.20. Total = $2.20.

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
