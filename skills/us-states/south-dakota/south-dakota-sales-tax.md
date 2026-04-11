---
name: south-dakota-sales-tax
description: Use this skill whenever asked about South Dakota sales tax, South Dakota use tax, South Dakota DOR filing, South Dakota Wayfair, South Dakota municipal gross receipts tax, or South Dakota sales tax compliance. Trigger on phrases like "South Dakota sales tax", "SD sales tax", "SDCL §10-45", "South Dakota DOR", "Wayfair", "South Dakota grocery tax", "South Dakota SST", "South Dakota no income tax", or any request involving South Dakota sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# South Dakota Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | South Dakota, United States |
| Jurisdiction Code | US-SD |
| Tax Type | Sales and Use Tax (state + local) |
| State Rate | 4.50% |
| Municipal Tax | Up to 2.00% |
| Municipal Gross Receipts Tax | Additional (varies by municipality) |
| Maximum Combined Rate | ~6.50% + municipal gross receipts |
| Primary Statute | South Dakota Codified Laws (SDCL) §10-45 |
| Governing Agency | South Dakota Department of Revenue (DOR) |
| Portal | https://dor.sd.gov |
| SST Member | Yes -- Full Member |
| No State Income Tax | Yes |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics, Wayfair background. T2: municipal gross receipts, service taxability, exemption specifics. T3: audit defense, complex transactions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any South Dakota sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a South Dakota sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in South Dakota? | Drives taxability classification under South Dakota law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in South Dakota? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple South Dakota local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Sales Tax Rate

South Dakota imposes a state sales tax of **4.50%** on the gross receipts of all retail sales of tangible personal property and services. [T1]

**Statute:** SDCL §10-45-2.

### 1.2 The Wayfair State [T1]

South Dakota is historically significant as the state whose law was upheld in **South Dakota v. Wayfair, Inc., 585 U.S. ___ (2018)**, the landmark US Supreme Court decision that overruled Quill and established that states may impose sales tax collection obligations on remote sellers without physical presence. [T1]

This case revolutionized US sales tax by enabling economic nexus nationwide. [T1]

### 1.3 No State Income Tax [T1]

South Dakota has **no state individual or corporate income tax**. Sales tax is the state's primary revenue source. [T1]

### 1.4 Local Sales Taxes [T1]

- Municipalities may impose a local sales tax of up to **2.00%**. [T1]
- Combined state + municipal rates can reach approximately **6.50%**. [T1]
- **Municipal gross receipts tax:** Some municipalities impose an additional gross receipts tax on specific industries (restaurants, hotels, bars), typically 1-2%. This is IN ADDITION to the sales tax. [T2]

### 1.5 Very Broad Tax Base [T1]

South Dakota has one of the broadest sales tax bases in the country:
- Virtually ALL services are taxable. [T1]
- ALL food (including groceries) is taxable. [T1]
- This broad base allows the state to maintain a relatively low rate. [T1]

### 1.6 Sourcing [T1]

South Dakota uses **destination-based** sourcing. [T1]

As an SST member, South Dakota follows SSUTA sourcing rules. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food -- TAXABLE at Full Rate [T1]

**South Dakota taxes grocery food at the FULL 4.5% state rate + local.** [T1]

- Unprepared food: taxable at 4.5% + local. [T1]
- Prepared food: taxable at the same rate. [T1]
- There is NO reduced rate or exemption for food. [T1]
- South Dakota is one of the few remaining states that fully taxes grocery food. [T1]

### 2.2 Clothing [T1]

- Clothing is **fully taxable**. No exemption. [T1]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. SDCL §10-45-14.5. [T1]
- OTC drugs: **taxable**. [T1]
- DME: exempt with prescription. [T1]
- Prosthetics: exempt. [T1]

### 2.4 Services -- VERY BROADLY TAXABLE [T1]

**South Dakota taxes virtually ALL services.** Along with Hawaii, New Mexico, and West Virginia, South Dakota has one of the broadest service tax bases. [T1]

Taxable services include (non-exhaustive):
- Professional services: legal, accounting, consulting, engineering, architecture. [T1]
- Personal care: haircuts, spa services. [T1]
- Repair and maintenance. [T1]
- Cleaning and janitorial. [T1]
- IT services, web design, software development. [T1]
- Construction services (labor + materials). [T1]
- Marketing and advertising. [T1]
- Financial advisory services. [T2]
- Telecommunications. [T1]

**Very limited exemptions from services:**
- Medical services (physicians, dentists, hospitals). [T1]
- Insurance premiums (subject to premium tax instead). [T1]
- Banking/financial institution services (some). [T2]

### 2.5 SaaS and Digital Goods [T1]

- **SaaS:** **Taxable**. South Dakota taxes all electronically transferred products and services, including SaaS. SDCL §10-45-4.2. [T1]
- **Digital downloads:** Taxable. [T1]
- **Streaming services:** Taxable. [T1]
- **Canned and custom software:** Taxable. [T1]

### 2.6 Manufacturing [T2]

- Manufacturing equipment: no specific broad manufacturing exemption in South Dakota. [T2]
- Raw materials incorporated into finished products for resale: exempt under resale. [T1]
- South Dakota's broad base means most equipment purchases are taxable. [T1]

### 2.7 Agricultural [T1]

- Farm machinery and equipment: **exempt**. SDCL §10-45-14. [T1]
- Feed, seed, fertilizer: exempt. [T1]
- Livestock: exempt for breeding/production. [T1]
- Agricultural chemicals: exempt. [T1]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | South Dakota Sales Tax Return (filed via DOR portal) |
| Filing Frequencies | Monthly (>$250/month avg); Quarterly ($50-$250); Annually (<$50) |
| Due Date | 20th of the month following the reporting period |
| Portal | https://dor.sd.gov |
| E-filing | Required for most filers |

### 4.2 Vendor Discount [T1]

South Dakota does NOT offer a vendor discount for timely filing. [T1]

### 4.3 Penalties and Interest [T1]

- Late filing penalty: 10% of tax due or $10, whichever is greater. [T1]
- Interest: 1% per month (12% per annum). [T1]
- Fraud penalty: 100% of tax due. [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for South Dakota. Key categories: [T1]

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
| Revenue Threshold | $100,000 in South Dakota sales |
| Transaction Threshold | 200 transactions |
| Test | OR (either threshold triggers nexus) |
| Measurement Period | Current or prior calendar year |
| Effective Date | November 1, 2018 (post-Wayfair) |

**Statute:** SDCL §10-64-2.

### 3.2 Marketplace Facilitator [T1]

South Dakota requires marketplace facilitators to collect and remit. SDCL §10-45-98. [T1]

### 3.3 SST Registration [T1]

Full SST member. SSTRS and CSPs available. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER assume grocery food is exempt in South Dakota. It is taxable at the FULL rate. [T1]
- NEVER assume services are exempt in South Dakota. Virtually ALL services are taxable, including professional services. [T1]
- NEVER assume SaaS is exempt. South Dakota taxes SaaS and all digital products. [T1]
- NEVER confuse sales tax with the separate municipal gross receipts tax. They are different obligations. [T2]
- NEVER forget South Dakota's role as the Wayfair state when advising on economic nexus. [T1]
- NEVER assume a uniform rate. Municipal taxes vary by city. [T1]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Grocery Food Fully Taxable [T2]

**Situation:** A multi-state retailer assumes food is exempt in South Dakota based on other states.

**Resolution:**
- South Dakota taxes ALL grocery food at the full 4.5% state rate + local. [T1]
- POS systems must be configured to charge sales tax on food. [T1]
- South Dakota, Alabama, and Mississippi remain among the few states taxing food at the full rate. [T1]
- **Flag for reviewer:** Verify POS food classification. Common error is configuring food as exempt. [T2]

### EC2 -- Professional Services Taxable [T2]

**Situation:** A mainland law firm provides services to a South Dakota client. Is the legal fee subject to SD sales tax?

**Resolution:**
- Legal services ARE taxable in South Dakota. [T1]
- If the law firm has economic nexus in SD ($100K+ or 200+ transactions), it must collect SD sales tax on fees for services delivered to SD clients. [T1]
- Most mainland professionals are unaware that SD taxes professional services. [T2]
- **Flag for reviewer:** Service providers from states that exempt professional services often fail to collect SD tax. Verify compliance. [T2]

### EC3 -- Municipal Gross Receipts Tax [T2]

**Situation:** A restaurant in Sioux Falls owes both sales tax and municipal gross receipts tax. How do they interact?

**Resolution:**
- The restaurant collects and remits 4.5% state + 2% city = 6.5% sales tax. [T1]
- The municipal gross receipts tax is an ADDITIONAL tax imposed on the restaurant's gross receipts (typically 1-2%). [T2]
- This tax is on the BUSINESS, not passed to the customer (though businesses often build it into prices). [T2]
- The two taxes are separate returns/obligations. [T2]
- **Flag for reviewer:** Municipal gross receipts taxes are filed separately from sales tax. Verify all applicable municipal taxes. [T2]

### EC4 -- Wayfair Compliance for Remote Sellers [T1]

**Situation:** A remote seller wants to understand their SD obligation given the Wayfair decision.

**Resolution:**
- South Dakota's law (upheld in Wayfair) requires remote sellers meeting the $100K OR 200 transaction threshold to collect SD sales tax. [T1]
- The law was found constitutional because it: (a) has a safe harbor for small sellers, (b) does not apply retroactively, (c) South Dakota is an SST member (simplifying compliance). [T1]
- Remote sellers should register through SSTRS for free compliance tools. [T1]
- **Flag for reviewer:** Wayfair is the foundation of all US economic nexus laws. South Dakota's law is the model. [T1]

---

### EC5 -- Consulting Firm from Non-Service-Tax State [T2]

**Situation:** A management consulting firm from Colorado (where consulting is exempt from sales tax) provides strategic consulting to an SD client. The firm has economic nexus in SD.

**Resolution:**
- Consulting services ARE taxable in South Dakota. [T1]
- The firm must register for SD sales tax and collect on fees for services delivered to SD clients. [T1]
- The firm's home state treatment (exempt in CO) is irrelevant. Destination state rules apply. [T1]
- **Flag for reviewer:** Service firms from states that exempt professional services are high-risk for SD non-compliance. [T2]

### EC6 -- Construction Services [T2]

**Situation:** A contractor builds a commercial building in Rapid City. The total contract is $1 million (materials + labor).

**Resolution:**
- In South Dakota, construction services are subject to sales tax on the ENTIRE contract (materials + labor). [T1]
- This is different from most states where the contractor pays tax on materials only. [T1]
- Tax = $1,000,000 x combined rate (4.5% state + 2% city = 6.5%). [T1]
- The contractor collects tax from the property owner. [T1]
- **Flag for reviewer:** Contractors from other states may be unfamiliar with SD's treatment of construction as a fully taxable service. [T2]

### EC7 -- Use Tax on Personal Purchases [T1]

**Situation:** An SD resident purchases a $2,000 laptop online from a seller that did not collect SD tax.

**Resolution:**
- Use tax is due at the same rate as sales tax. [T1]
- The resident should self-assess use tax on their SD income tax return (SD has no income tax, so use tax must be reported separately). [T1]
- SD use tax return (SDCL §10-46) is available. [T1]
- **Flag for reviewer:** In a no-income-tax state, there is no income tax return to add use tax to. Separate use tax reporting is required. [T2]

---

## Test Suite

### Test 1 -- Basic Taxable Sale

**Input:** Seller in Sioux Falls sells $500 of office supplies. Combined rate = 6.5% (4.5% state + 2% city).
**Expected output:** Tax = $500 x 6.5% = $32.50. Total = $532.50.

### Test 2 -- Grocery Food at Full Rate

**Input:** Customer buys $200 of unprepared groceries in Rapid City. Combined rate = 6.5%.
**Expected output:** Food IS taxable. Tax = $200 x 6.5% = $13.00. Total = $213.00.

### Test 3 -- Legal Services Taxable

**Input:** Attorney in Pierre bills $3,000 for legal services. State rate = 4.5% (no city tax in this example).
**Expected output:** Legal services ARE taxable. Tax = $3,000 x 4.5% = $135.00. Total = $3,135.00.

### Test 4 -- SaaS Taxable

**Input:** SaaS company charges SD business $500/month. Combined rate = 6.5%.
**Expected output:** SaaS IS taxable. Tax = $500 x 6.5% = $32.50. Total = $532.50.

### Test 5 -- Economic Nexus (Wayfair Threshold)

**Input:** Remote seller from Delaware sold $110,000 to SD in the prior year, with 150 transactions.
**Expected output:** Revenue ($110,000) exceeds $100,000 threshold. Nexus IS triggered (OR test -- revenue alone sufficient). Must register and collect.

---

### Test 6 -- Consulting Services Taxable

**Input:** Consulting firm charges $10,000 for services to an SD business in Sioux Falls. Combined rate = 6.5%.
**Expected output:** Consulting IS taxable. Tax = $10,000 x 6.5% = $650.00. Total = $10,650.00.

### Test 7 -- Construction Contract

**Input:** Contractor charges $500,000 for building project in Rapid City. Combined rate = 6.5%.
**Expected output:** Entire contract is taxable. Tax = $500,000 x 6.5% = $32,500.00. Total = $532,500.00.

### Test 8 -- Farm Equipment Exempt

**Input:** Farmer buys $80,000 tractor for agricultural use.
**Expected output:** Farm machinery is exempt. Tax = $0. Total = $80,000.

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
