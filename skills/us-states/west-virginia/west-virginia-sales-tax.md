---
name: west-virginia-sales-tax
description: Use this skill whenever asked about West Virginia sales tax, WV use tax, West Virginia Tax Division filing, West Virginia SaaS tax, West Virginia service taxation, or West Virginia sales tax compliance. Trigger on phrases like "West Virginia sales tax", "WV sales tax", "W.Va. Code §11-15", "WV Tax Division", "West Virginia SaaS", "West Virginia SST", or any request involving West Virginia state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# West Virginia Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | West Virginia, United States |
| Jurisdiction Code | US-WV |
| Tax Type | Sales and Use Tax (state + limited local) |
| State Rate | 6.00% |
| Local Rate | Up to 1.00% (municipal) |
| Maximum Combined Rate | 7.00% |
| Primary Statute | West Virginia Code §11-15-1 et seq. (Consumers Sales and Service Tax) |
| Governing Agency | West Virginia State Tax Division |
| Portal | https://tax.wv.gov |
| SST Member | Yes -- Full Member |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics. T2: broad service taxation, SaaS taxability, local rate determination. T3: audit defense, complex transactions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any West Virginia sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a West Virginia sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in West Virginia? | Drives taxability classification under West Virginia law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in West Virginia? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple West Virginia local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Sales Tax Rate

West Virginia imposes a **Consumers Sales and Service Tax** of **6.00%** on the retail sale of tangible personal property and services. [T1]

**Statute:** W.Va. Code §11-15-3.

**Note:** The name "Consumers Sales and Service Tax" reflects that WV broadly taxes services, unlike states that only tax TPP. [T1]

### 1.2 Local Sales Taxes [T1]

- Municipalities may impose a local sales tax of up to **1.00%**. [T1]
- Not all municipalities have adopted the local option. [T1]
- Where adopted, the combined rate is **7.00%**. [T1]
- Local taxes are administered by the State Tax Division. [T1]

### 1.3 Sourcing [T1]

West Virginia uses **destination-based** sourcing. [T1]

As an SST member, West Virginia follows SSUTA sourcing rules. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food -- EXEMPT [T1]

- Unprepared grocery food: **exempt**. W.Va. Code §11-15-9(a)(8). [T1]
- Prepared food: taxable at the full combined rate. [T1]
- Candy: taxable. [T1]
- Soft drinks: taxable. [T1]
- West Virginia follows SST food definitions. [T1]

### 2.2 Clothing [T1]

- Clothing is **fully taxable**. No exemption. [T1]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. W.Va. Code §11-15-9(a)(6). [T1]
- OTC drugs: **exempt**. [T1]
- DME: exempt. [T1]
- Prosthetics: exempt. [T1]

### 2.4 Services -- BROADLY TAXABLE [T1]

**West Virginia taxes a very broad range of services.** Along with Hawaii, New Mexico, and South Dakota, WV is one of the broadest service-taxing states. [T1]

Taxable services include (non-exhaustive):
- Professional services: legal, accounting, consulting, engineering (many are taxable). [T1]
- Personal care: haircuts, spa, beauty treatments. [T1]
- Repair and maintenance. [T1]
- Cleaning and janitorial. [T1]
- IT services, web design, software development. [T1]
- Construction services. [T1]
- Health and fitness. [T1]
- Telecommunications. [T1]
- Transportation and courier services. [T1]
- Advertising services. [T1]
- Security services. [T1]

**Key exemptions:**
- Medical/healthcare services (physician, dental, hospital). [T1]
- Educational services provided by nonprofit institutions. [T1]
- Financial intermediation services (banking). [T2]

**Statute:** W.Va. Code §11-15-3 (broad definition of taxable services).

### 2.5 SaaS and Digital Goods -- TAXABLE [T1]

- **SaaS:** **Taxable** in West Virginia. WV's broad service tax base includes remotely accessed software. W.Va. Code §11-15-2(b)(19). [T1]
- **Canned software (physical and electronic):** Taxable. [T1]
- **Custom software:** Taxable (WV taxes custom software, unlike many states). [T1]
- **Digital downloads:** Taxable. [T1]
- **Streaming services:** Taxable. [T1]

**Note:** West Virginia is notable for taxing CUSTOM software, which most states exempt. [T1]

### 2.6 Manufacturing [T1]

- Manufacturing machinery and equipment used directly in manufacturing: **exempt**. W.Va. Code §11-15-9(b)(3). [T1]
- Raw materials for resale: exempt under resale. [T1]
- Utilities used in manufacturing: reduced rate or exemption for qualifying manufacturers. [T2]

### 2.7 Agricultural [T1]

- Farm machinery and equipment: exempt. W.Va. Code §11-15-9(a)(3). [T1]
- Feed, seed, fertilizer: exempt. [T1]
- Livestock for breeding/production: exempt. [T1]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | CST-200 (Consumers Sales and Service Tax Return) |
| Filing Frequencies | Monthly (>$600/quarter avg); Quarterly ($150-$600); Annually (<$150) |
| Due Date | 20th of the month following the reporting period |
| Portal | https://tax.wv.gov (MyTaxes) |
| E-filing | Required for most filers |

### 4.2 Vendor Discount [T1]

West Virginia does NOT offer a vendor discount for timely filing. [T1]

### 4.3 Penalties and Interest [T1]

- Late filing penalty: 5% of tax due per month, up to 25%. [T1]
- Late payment penalty: 0.5% per month, up to 25%. [T1]
- Interest: rate set by statute, based on federal underpayment rate. [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for West Virginia. Key categories: [T1]

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
| Revenue Threshold | $100,000 in West Virginia sales |
| Transaction Threshold | 200 transactions |
| Test | OR (either threshold triggers nexus) |
| Measurement Period | Current or prior calendar year |
| Effective Date | January 1, 2019 |

**Statute:** W.Va. Code §11-15A-6b.

### 3.2 Marketplace Facilitator [T1]

West Virginia requires marketplace facilitators to collect and remit. W.Va. Code §11-15A-6c. [T1]

### 3.3 SST Registration [T1]

Full SST member. SSTRS and CSPs available. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER assume services are exempt in West Virginia. WV taxes virtually ALL services, including professional services. [T1]
- NEVER assume custom software is exempt in WV. Unlike most states, WV taxes custom software. [T1]
- NEVER assume SaaS is exempt. WV taxes SaaS. [T1]
- NEVER tax grocery food in WV. Unprepared food is exempt. [T1]
- NEVER forget the OTC drug exemption. OTC drugs are exempt in WV. [T1]
- NEVER assume a uniform rate. Municipal add-ons of up to 1% may apply. [T1]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Professional Services Taxable [T2]

**Situation:** An out-of-state accounting firm provides tax preparation services to WV clients. Is the fee taxable?

**Resolution:**
- Accounting services ARE taxable in West Virginia. [T1]
- If the firm meets economic nexus, it must collect WV sales tax on fees. [T1]
- Many out-of-state service providers are unaware of WV's broad service taxation. [T2]
- **Flag for reviewer:** WV is one of the few states taxing professional services. Verify that all service revenue streams are evaluated. [T2]

### EC2 -- Custom Software Taxable [T2]

**Situation:** A software development company creates a custom application for a WV client. Is the development fee taxable?

**Resolution:**
- West Virginia taxes CUSTOM software, unlike most states that only tax canned software. [T1]
- The development fee is subject to the 6% state rate + local. [T1]
- This is unusual nationally -- most states exempt custom software. [T1]
- **Flag for reviewer:** Developers accustomed to custom software exemptions in other states must adjust for WV. [T2]

### EC3 -- Broad Service Base Impact on Compliance [T2]

**Situation:** A multi-state service company needs to determine which of its services are taxable in WV vs. other states.

**Resolution:**
- WV taxes virtually all services. The starting assumption should be that a service is taxable, then check for specific exemptions. [T1]
- This is the opposite approach from most states, where services are assumed exempt unless specifically enumerated. [T1]
- The company should review its entire revenue mix against WV law. [T2]
- **Flag for reviewer:** In WV, the question is "is there an exemption?" rather than "is the service specifically taxable?" [T2]

### EC4 -- OTC Drug Exemption [T1]

**Situation:** A retailer asks whether OTC medications are taxable in WV.

**Resolution:**
- OTC drugs are exempt in West Virginia. [T1]
- Dietary supplements are NOT OTC drugs and are taxable. [T2]
- **Flag for reviewer:** Ensure POS systems distinguish between OTC drugs and dietary supplements. [T2]

---

### EC5 -- IT Consulting and Software Bundle [T2]

**Situation:** An IT company provides consulting ($5,000), custom software development ($10,000), and canned software licenses ($3,000) to a WV client.

**Resolution:**
- IT consulting: taxable (service). [T1]
- Custom software development: taxable (WV taxes custom software). [T1]
- Canned software licenses: taxable. [T1]
- ALL three components are taxable at the combined rate. [T1]
- Total taxable = $18,000. [T1]
- **Flag for reviewer:** In most other states, custom software and IT consulting would be exempt. WV is unusual. [T2]

### EC6 -- Construction Services [T2]

**Situation:** A contractor performs a $200,000 renovation on a commercial building in Charleston.

**Resolution:**
- Construction services are subject to the consumers sales and service tax. [T1]
- The contractor should collect tax on the contract price. [T1]
- The contractor does NOT separately pay tax on materials (the tax is on the service, not the materials). [T2]
- Different from states where the contractor pays tax on materials and does not charge the customer. [T1]
- **Flag for reviewer:** WV's construction tax treatment may differ from the contractor's experience in other states. Verify application. [T2]

### EC7 -- Advertising and Marketing Services [T2]

**Situation:** A marketing agency provides advertising campaign services to a WV business.

**Resolution:**
- Advertising services are taxable in West Virginia. [T1]
- The agency must collect WV sales tax on its fees if it has nexus. [T1]
- Digital advertising, print advertising, and media buying are all subject to tax. [T2]
- **Flag for reviewer:** Most states exempt advertising services. WV's broad base captures them. [T2]

---

## Test Suite

### Test 1 -- Basic Taxable Sale

**Input:** Seller in Charleston sells $1,000 of furniture. Combined rate = 7% (6% state + 1% local).
**Expected output:** Tax = $1,000 x 7% = $70.00. Total = $1,070.00.

### Test 2 -- Grocery Food Exempt

**Input:** Customer buys $200 of unprepared groceries in Huntington.
**Expected output:** Groceries are EXEMPT. Tax = $0. Total = $200.00.

### Test 3 -- Legal Services Taxable

**Input:** Attorney in Morgantown bills $2,000 for legal services. Combined rate = 7%.
**Expected output:** Legal services ARE taxable. Tax = $2,000 x 7% = $140.00. Total = $2,140.00.

### Test 4 -- SaaS and Custom Software Taxable

**Input:** Software company charges $5,000 for custom development + $500/month SaaS to a WV client. Combined rate = 6% (no local).
**Expected output:** BOTH are taxable. Custom dev tax = $5,000 x 6% = $300.00. SaaS tax = $500 x 6% = $30.00/month.

### Test 5 -- Economic Nexus

**Input:** Remote consulting firm from Virginia earned $120,000 from WV clients in the prior year.
**Expected output:** $120,000 exceeds $100,000. Nexus IS triggered. Must register and collect on WV-delivered services.

---

### Test 6 -- IT Consulting Taxable

**Input:** IT consultant charges $8,000 for consulting services in Morgantown. Combined rate = 7%.
**Expected output:** IT consulting IS taxable. Tax = $8,000 x 7% = $560.00. Total = $8,560.00.

### Test 7 -- Custom Software Taxable

**Input:** Developer charges $15,000 for custom application built for WV client. Rate = 6% (no local).
**Expected output:** Custom software IS taxable in WV. Tax = $15,000 x 6% = $900.00. Total = $15,900.00.

### Test 8 -- OTC Drug Exemption

**Input:** Customer buys $25 OTC pain reliever and $20 dietary supplement. Combined rate = 6%.
**Expected output:** OTC drug: exempt. Supplement: taxable. Tax = $20 x 6% = $1.20. Total = $46.20.

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
