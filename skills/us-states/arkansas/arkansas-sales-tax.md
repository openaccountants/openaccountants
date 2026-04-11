---
name: arkansas-sales-tax
description: Use this skill whenever asked about Arkansas sales tax, Arkansas use tax, Arkansas DFA sales tax filing, Arkansas grocery tax reduced rate, or Streamlined Sales Tax in Arkansas. Trigger on phrases like "Arkansas sales tax", "AR sales tax", "DFA", "A.C.A. §26-52", "Arkansas grocery tax", "Arkansas SST", or any request involving Arkansas state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# Arkansas Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Arkansas, United States |
| Jurisdiction Code | US-AR |
| Tax Type | Sales and Use Tax (state + local) |
| State Rate | 6.50% |
| Maximum Combined Rate | ~11.625% (state 6.5% + county + city) |
| Primary Statute | Arkansas Code Annotated §26-52 (Gross Receipts Tax); §26-53 (Compensating Use Tax) |
| Governing Agency | Department of Finance and Administration (DFA) |
| Portal | https://www.dfa.arkansas.gov/excise-tax |
| SST Member | Yes -- Full Member |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics. T2: local rate determinations, service taxability, food rate application. T3: audit defense, complex exemption issues, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Arkansas sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have an Arkansas sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Arkansas? | Drives taxability classification under Arkansas law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Arkansas? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Arkansas local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Sales Tax Rate

Arkansas imposes a state gross receipts tax (sales tax) of **6.50%** on the retail sale of tangible personal property and certain services. [T1]

**Statute:** A.C.A. §26-52-301.

**Note:** Arkansas calls its sales tax the "Gross Receipts Tax," but it functions as a traditional sales tax collected from the buyer.

### 1.2 Local Sales Taxes [T1]

- Counties may impose additional sales tax. [T1]
- Cities may impose additional sales tax. [T1]
- Combined state + local rates can exceed **11%** in some jurisdictions. [T1]
- Arkansas has approximately **500+ local taxing jurisdictions**. [T2]

### 1.3 Sourcing [T1]

Arkansas uses **destination-based** sourcing. The tax rate is determined by the delivery address of the buyer. [T1]

As an SST member state, Arkansas follows the SSUTA sourcing rules. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food -- Reduced Rate [T1]

**Arkansas taxes grocery food at a reduced state rate of 0.125% (one-eighth of one percent).** [T1]

- This is effectively near-zero at the state level. [T1]
- Local taxes still apply at the full local rate on grocery food. [T1]
- The combined rate on groceries (state + local) varies by location but is significantly lower than the combined rate on general merchandise. [T1]
- Prepared food is taxable at the full 6.5% state rate + local. [T1]
- Candy and soft drinks are taxable at the full state rate. [T1]

**Statute:** A.C.A. §26-52-317 (food and food ingredients definition); A.C.A. §26-52-301(c) (reduced rate).

### 2.2 Clothing [T1]

- Clothing is **fully taxable** at the standard 6.5% state rate + local. [T1]
- Arkansas holds an annual sales tax holiday (see Edge Cases) that temporarily exempts certain clothing items. [T2]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. A.C.A. §26-52-401(2). [T1]
- Over-the-counter (OTC) drugs: **taxable** at the full rate. [T1]
- Durable medical equipment (DME): exempt with prescription. [T1]
- Prosthetic devices: exempt. [T1]

### 2.4 Services [T2]

Arkansas taxes a moderate number of services:

- **Taxable services include:** Cleaning and janitorial, pest control, security services, telecommunications, cable/satellite TV, landscaping, dry cleaning, pet grooming, parking, storage, body piercing/tattooing, initial installation of TPP. [T2]
- **Exempt services include:** Professional services (legal, accounting, medical), educational services, financial services. [T2]
- **Repair services:** Labor on repair of TPP is generally taxable when combined with taxable parts. [T2]

**Statute:** A.C.A. §26-52-301(3) (taxable services enumerated).

### 2.5 SaaS and Digital Goods [T2]

- **SaaS:** Generally **not taxable** under current Arkansas law and DFA interpretation. SaaS is not considered tangible personal property or a specifically enumerated taxable service. [T2]
- **Canned software (physical media):** Taxable as TPP. [T1]
- **Canned software (electronic delivery):** Taxable. Arkansas follows the SST definition of specified digital products. [T1]
- **Digital downloads (music, e-books):** Taxable as specified digital products under SST definitions. A.C.A. §26-52-304. [T1]
- **Streaming services:** Taxable as specified digital products. [T2]

### 2.6 Manufacturing [T2]

- Machinery and equipment used **directly** in manufacturing: taxable but may qualify for a **sales tax refund** or reduced rate under certain incentive programs. [T2]
- Raw materials incorporated into finished products for resale: exempt under the resale exemption. [T1]
- Utilities used in manufacturing: partial exemption available. A.C.A. §26-52-402. [T2]

### 2.7 Motor Vehicles [T1]

- Motor vehicles are subject to sales tax at the state rate of 6.5% (some local taxes may apply). [T1]
- Trade-in credit reduces the taxable amount. [T1]
- Private-party sales are subject to use tax. [T1]

### 2.8 Agricultural [T1]

- Farm machinery and equipment: exempt. A.C.A. §26-52-403. [T1]
- Feed, seed, fertilizer: exempt when used in commercial agriculture. [T1]
- Livestock: exempt when purchased for breeding or production. [T1]

---

## Step 3: Return Form Structure
### 4.1 State Filing [T1]

| Field | Detail |
|-------|--------|
| Return Form | ET-1 (Sales and Use Tax Return) |
| Filing Frequencies | Monthly (>$100/month liability); Quarterly ($25-$100/month); Annually (<$25/month) |
| Due Date | 20th of the month following the reporting period |
| Portal | https://atap.arkansas.gov (Arkansas Taxpayer Access Point) |
| E-filing | Required for most filers |

### 4.2 Vendor Discount [T1]

Arkansas offers a timely filing discount of **2%** of the first $1,000 of tax due per reporting period. Maximum discount = $20/month. [T1]

**Statute:** A.C.A. §26-52-503.

### 4.3 Penalties and Interest [T1]

- Late filing penalty: 5% of tax due per month, up to 35%. [T1]
- Minimum penalty: $5. [T1]
- Interest: rate set annually by DFA, typically around 10% per annum. [T1]
- Fraud penalty: 50% of tax due. [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for Arkansas. Key categories: [T1]

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
| Revenue Threshold | $100,000 in Arkansas sales |
| Transaction Threshold | 200 transactions |
| Test | OR (either threshold triggers nexus) |
| Measurement Period | Current or prior calendar year |
| Effective Date | July 1, 2019 |

**Statute:** A.C.A. §26-52-111.

### 3.2 Physical Nexus [T1]

Standard physical nexus rules apply: office, warehouse, employees, inventory, or agents in Arkansas create nexus. [T1]

### 3.3 Marketplace Facilitator [T1]

Arkansas requires marketplace facilitators to collect and remit sales tax on sales made through their platforms. Effective July 1, 2019. A.C.A. §26-52-117. [T1]

### 3.4 SST Registration [T1]

As a full SST member, Arkansas allows remote sellers to register through the Streamlined Sales Tax Registration System (SSTRS) and use Certified Service Providers (CSPs) for free tax computation and filing. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER assume grocery food is exempt in Arkansas. It is taxable at a reduced state rate of 0.125% plus full local rates. [T1]
- NEVER apply the reduced food rate to candy, soft drinks, dietary supplements, or prepared food. These are taxed at the full state rate. [T1]
- NEVER ignore the SST framework when advising Arkansas sellers. SST registration and CSP options simplify compliance. [T2]
- NEVER assume SaaS is taxable in Arkansas. Current interpretation treats SaaS as non-taxable. Verify before collecting. [T2]
- NEVER apply a single combined rate across all Arkansas locations. Rates vary by delivery address. [T1]
- NEVER forget that digital downloads (specified digital products) ARE taxable in Arkansas under SST definitions. [T1]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Grocery Food Rate Application [T2]

**Situation:** A grocery store sells a mix of food items and non-food items. How should the reduced food rate (0.125%) be applied?

**Resolution:**
- Each item must be classified as "food and food ingredients" (reduced rate) or non-food (full rate). [T1]
- Candy and soft drinks are specifically excluded from the reduced rate and are taxed at the full 6.5% state rate. [T1]
- Dietary supplements are excluded from the food definition and taxed at full rate. [T1]
- Prepared food (heated, has eating utensils, or is two or more food ingredients mixed for immediate consumption) is taxed at the full rate. [T1]
- **Flag for reviewer:** The SST definitions of food, candy, soft drinks, and prepared food apply. Review item classifications carefully. [T2]

### EC2 -- SST Certified Service Provider Filing [T2]

**Situation:** A remote seller uses a CSP through the SST system. The CSP miscalculates tax due to a rate change.

**Resolution:**
- Under SST rules, if a CSP miscalculates tax using the SST-certified rate and taxability tables, the seller is held harmless. [T1]
- The state must look to the CSP for any error, not the seller. [T1]
- This protection applies ONLY to errors in the SST-provided data, not to errors in the seller's classification of its own products. [T2]
- **Flag for reviewer:** Verify that the CSP is currently certified and that the error stems from rate/taxability data, not product classification. [T2]

### EC3 -- Sales Tax Holiday [T2]

**Situation:** During Arkansas's back-to-school sales tax holiday (typically the first Saturday-Sunday in August), which items qualify?

**Resolution:**
- Clothing items $100 or less per item: exempt from state tax (local tax may still apply). [T1]
- School supplies, instructional materials, and art supplies $50 or less per item: exempt from state tax. [T1]
- Electronics: generally NOT included in the holiday. [T1]
- Verify current year's items, thresholds, and dates with DFA before applying. [T2]
- **Statute:** A.C.A. §26-52-444.

### EC4 -- Digital Products and Bundled Transactions [T2]

**Situation:** A seller offers a subscription that includes both SaaS access (not taxable) and digital downloads (taxable). The subscription is sold at a single price.

**Resolution:**
- Under SST bundled transaction rules, if the taxable portion exceeds a specified threshold of the total price, the entire transaction may be taxable. [T2]
- Arkansas follows SSUTA Section 330 on bundled transactions. [T2]
- Best practice: separately state the taxable and non-taxable components on the invoice. [T2]
- **Flag for reviewer:** Analyze the bundled transaction under Arkansas's adopted SST bundling rules. [T2]

### EC5 -- Out-of-State Contractor Performing Services in Arkansas [T2]

**Situation:** An out-of-state construction company performs a project in Arkansas for 6 months.

**Resolution:**
- The contractor has physical nexus in Arkansas during the project period. [T1]
- Materials purchased for the project are subject to Arkansas sales or use tax. [T1]
- The contractor may need to register for Arkansas sales tax and potentially withhold Arkansas income tax for employees working in the state. [T2]
- **Flag for reviewer:** Construction contract taxability in Arkansas requires state-specific analysis. Escalate complex construction scenarios. [T3]

---

### EC6 -- Mixed Food and Non-Food Purchase [T2]

**Situation:** A customer buys groceries ($80), candy ($5), soft drinks ($10), and paper towels ($8) at one transaction.

**Resolution:**
- Groceries ($80): state rate 0.125% + full local. [T1]
- Candy ($5): full 6.5% state + local. [T1]
- Soft drinks ($10): full 6.5% state + local. [T1]
- Paper towels ($8): full 6.5% state + local (non-food TPP). [T1]
- POS must classify each item correctly at the register. [T1]
- **Flag for reviewer:** The three different rate categories in a single grocery transaction are a common source of error. [T2]

### EC7 -- Lodging and Tourism Services [T2]

**Situation:** A hotel in Hot Springs charges $150/night. What taxes apply?

**Resolution:**
- Hotel room rental is subject to the full 6.5% state sales tax + local. [T1]
- An additional state tourism tax of **2%** applies to hotels. A.C.A. §26-63-301. [T1]
- Local lodging taxes may also apply. [T2]
- The combined tax on a hotel room in Hot Springs can exceed 12%. [T2]
- **Flag for reviewer:** Hotel taxation includes both the general sales tax and the separate tourism tax. Both must be collected. [T2]

---

## Test Suite

### Test 1 -- Basic Taxable Sale

**Input:** Seller in Little Rock sells $1,000 of furniture to a local buyer. Combined Little Rock rate = 9.625% (6.5% state + 3.125% local).
**Expected output:** Sales tax = $1,000 x 9.625% = $96.25. Total = $1,096.25.

### Test 2 -- Grocery Food Reduced Rate

**Input:** Customer buys $200 of unprepared grocery food in Fayetteville. State rate on food = 0.125%. Local rate = 2.75%.
**Expected output:** State tax = $200 x 0.125% = $0.25. Local tax = $200 x 2.75% = $5.50. Total tax = $5.75. Total = $205.75.

### Test 3 -- Candy at Full Rate

**Input:** Customer buys a $5 candy bar at a Little Rock grocery store. Combined rate = 9.625%.
**Expected output:** Candy is excluded from the reduced food rate. Tax = $5 x 9.625% = $0.48. Total = $5.48.

### Test 4 -- Economic Nexus Determination

**Input:** Online seller from California sold $80,000 and 250 transactions to Arkansas buyers in the prior calendar year.
**Expected output:** Revenue ($80,000) is below $100,000 but transactions (250) exceed 200. Nexus IS triggered (OR test). Seller must register and collect Arkansas sales tax.

### Test 5 -- Prescription Drug Exemption

**Input:** Pharmacy sells $100 prescription medication and $30 OTC cold medicine in Bentonville. Combined rate = 9.75%.
**Expected output:** Prescription: exempt, $0 tax. OTC: taxable. Tax = $30 x 9.75% = $2.93. Total = $132.93.

---

### Test 6 -- Digital Download Taxable

**Input:** Customer downloads a $15 e-book in Fayetteville. Combined rate = 9.625%.
**Expected output:** Digital downloads are taxable as specified digital products. Tax = $15 x 9.625% = $1.44. Total = $16.44.

### Test 7 -- Hotel Room with Tourism Tax

**Input:** Guest stays at a Little Rock hotel. Room = $120/night. State sales tax rate = 6.5%. Local = 3%. Tourism tax = 2%. Total = 11.5%.
**Expected output:** Total tax = $120 x 11.5% = $13.80. Total = $133.80.

### Test 8 -- Use Tax Self-Assessment

**Input:** Arkansas business purchases $5,000 of office equipment from an out-of-state vendor that did not collect tax. Business location combined rate = 9%.
**Expected output:** Use tax due = $5,000 x 9% = $450.00. Reported on ET-1 return.

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
