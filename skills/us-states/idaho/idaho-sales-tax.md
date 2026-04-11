---
name: idaho-sales-tax
description: Use this skill whenever asked about Idaho sales tax, Idaho use tax, Idaho STC sales tax filing, Idaho resort city tax, or Idaho sales tax compliance. Trigger on phrases like "Idaho sales tax", "ID sales tax", "STC", "Idaho Code §63-3619", "Idaho resort city tax", "Idaho SST", or any request involving Idaho state sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# Idaho Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Idaho, United States |
| Jurisdiction Code | US-ID |
| Tax Type | Sales and Use Tax (state + limited local) |
| State Rate | 6.00% |
| Maximum Combined Rate | ~9.00% (state 6% + resort city taxes) |
| Primary Statute | Idaho Code §63-3619 et seq. |
| Governing Agency | Idaho State Tax Commission (STC) |
| Portal | https://tax.idaho.gov |
| SST Member | Yes -- Full Member |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics. T2: resort city taxes, service taxability, exemption certificate management. T3: audit defense, complex exemption issues, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Idaho sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have an Idaho sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Idaho? | Drives taxability classification under Idaho law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Idaho? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Idaho local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Sales Tax Rate

Idaho imposes a state sales tax of **6.00%** on the retail sale of tangible personal property and certain services. [T1]

**Statute:** Idaho Code §63-3619.

### 1.2 Local Sales Taxes -- Limited to Resort Cities [T1/T2]

Idaho does NOT have a general local sales tax system. However:

- **Resort cities** (e.g., Sun Valley, McCall, Ketchum, Sandpoint, Driggs, Victor) may impose a local-option non-property tax, including a sales tax surcharge of up to **3%**. [T1]
- This means combined rates in resort cities can reach approximately **9%**. [T1]
- Outside resort cities, the rate is a uniform **6%** statewide. [T1]

**Statute:** Idaho Code §50-1044 et seq. (resort city local option tax).

### 1.3 Sourcing [T1]

Idaho uses **destination-based** sourcing. Tax rate is based on the delivery address. [T1]

As an SST member, Idaho follows SSUTA sourcing rules. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food [T1]

- Unprepared grocery food: **taxable** at the full 6% state rate. Idaho Code §63-3619. [T1]
- Idaho is one of the minority of states that taxes grocery food at the full rate. [T1]
- A **grocery tax credit** is available on the state income tax return to partially offset the burden ($100 per person for most taxpayers). Idaho Code §63-3024A. [T1]
- Prepared food: taxable at full rate. [T1]

### 2.2 Clothing [T1]

- Clothing is **fully taxable** at the standard 6% rate. No exemption. [T1]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. Idaho Code §63-3622N. [T1]
- Over-the-counter (OTC) drugs: **taxable**. [T1]
- Durable medical equipment (DME): exempt with prescription. [T1]
- Prosthetics: exempt. [T1]

### 2.4 Services [T2]

Idaho taxes relatively few services:

- **Taxable services include:** Hotel/motel accommodations, guided outfitting services, intrastate telecommunications. [T2]
- **Generally exempt services:** Professional services, personal care services, repair and maintenance labor (separately stated), cleaning services. [T2]
- **Repair labor:** If repair labor is separately stated from parts, the labor is exempt. If a lump-sum charge includes both parts and labor, the entire amount is taxable. [T2]

### 2.5 SaaS and Digital Goods [T2]

- **SaaS:** Generally **not taxable** in Idaho. SaaS is not considered tangible personal property or a specifically enumerated taxable service. [T2]
- **Canned software (physical media):** Taxable as TPP. [T1]
- **Canned software (electronic delivery):** Taxability is evolving; generally taxable if transferred with a permanent license. [T2]
- **Digital downloads (music, e-books):** Generally not taxable under current law (Idaho has not adopted SST's specified digital products provisions in full). [T2]
- **Custom software:** Exempt. [T2]

### 2.6 Manufacturing [T1]

- Production equipment used in manufacturing, fabrication, or processing: **exempt**. Idaho Code §63-3622GG. [T1]
- This includes machinery, equipment, and supplies used directly in manufacturing. [T1]
- Repair parts for exempt production equipment are also exempt. [T1]

### 2.7 Motor Vehicles [T1]

- Motor vehicles are subject to sales/use tax at the 6% rate at the time of title transfer. [T1]
- Trade-in credit reduces the taxable amount. [T1]

### 2.8 Agricultural [T1]

- Farm machinery and equipment: taxable (no broad exemption, but some specific items may qualify). [T2]
- Seed, feed, and fertilizer used in commercial agriculture: exempt. Idaho Code §63-3622P. [T1]
- Livestock: exempt when purchased for breeding or dairy. [T1]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | Form 850 (Sales/Use Tax Return) |
| Filing Frequencies | Monthly (>$1,666/month average tax); Quarterly ($300-$1,666/month); Annually (<$300/month) |
| Due Date | 20th of the month following the reporting period |
| Portal | https://tax.idaho.gov (TAP - Taxpayer Access Point) |
| E-filing | Required for most filers |

### 4.2 Vendor Discount [T1]

Idaho does NOT offer a vendor discount for timely filing. [T1]

### 4.3 Penalties and Interest [T1]

- Late filing/payment penalty: 5% of tax due per month, up to 25%. [T1]
- Minimum penalty: $10. [T1]
- Interest: rate set annually by Idaho STC (typically based on federal rate + 2%). [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for Idaho. Key categories: [T1]

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
| Revenue Threshold | $100,000 in Idaho sales |
| Transaction Threshold | N/A (revenue only) |
| Measurement Period | Current or prior calendar year |
| Effective Date | June 1, 2019 |

**Statute:** Idaho Code §63-3611(b).

### 3.2 Physical Nexus [T1]

Standard physical nexus rules apply. [T1]

### 3.3 Marketplace Facilitator [T1]

Idaho requires marketplace facilitators to collect and remit sales tax on marketplace sales. Effective June 1, 2019. Idaho Code §63-3611A. [T1]

### 3.4 SST Registration [T1]

As a full SST member, Idaho allows registration through the SSTRS and use of Certified Service Providers. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER assume grocery food is exempt in Idaho. It is taxable at the full 6% state rate. [T1]
- NEVER assume a uniform rate across Idaho. Resort cities add up to 3% local tax. [T1]
- NEVER tax separately stated repair labor. It is exempt when separately stated from parts. [T1]
- NEVER assume SaaS is taxable in Idaho. Current interpretation treats SaaS as non-taxable. [T2]
- NEVER forget the grocery tax credit exists as an income tax offset. Do not confuse it with a sales tax exemption. [T1]
- NEVER ignore the SST framework for Idaho compliance. SST registration and CSP options simplify compliance for remote sellers. [T2]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Resort City Tax Application [T2]

**Situation:** An e-commerce seller ships a product to a customer in Sun Valley (resort city with a 3% local tax). The combined rate is 9%.

**Resolution:**
- Destination-based sourcing applies. The 3% resort city tax applies in addition to the 6% state tax. [T1]
- The seller must determine the delivery address and apply the correct combined rate. [T1]
- Resort city taxes are remitted to the STC (the STC administers them). [T1]
- **Flag for reviewer:** Not all addresses in resort areas fall within the resort city boundaries. Verify the precise delivery address. [T2]

### EC2 -- Repair Labor Separately Stated [T2]

**Situation:** An auto repair shop charges $500 for parts and $300 for labor. If labor is separately stated, is the labor exempt?

**Resolution:**
- Idaho exempts separately stated repair labor. If the invoice shows $500 parts and $300 labor as separate line items, tax applies only to the $500 in parts. [T1]
- If the shop charges a lump sum of $800 for "repair service," the ENTIRE $800 is taxable. [T1]
- **Flag for reviewer:** Advise clients in repair industries to always separately state parts and labor on invoices. [T2]

### EC3 -- Grocery Tax Credit Interaction [T2]

**Situation:** A low-income Idaho resident asks whether there is relief from the grocery food tax.

**Resolution:**
- Idaho does not exempt grocery food from sales tax. [T1]
- However, Idaho provides a grocery tax credit on the state income tax return of $100 per person ($120 for persons 65+). Idaho Code §63-3024A. [T1]
- The credit is available to all Idaho residents, regardless of income. [T1]
- The credit is intended to partially offset the regressive effect of taxing groceries. [T1]
- **Flag for reviewer:** The grocery tax credit is claimed on the income tax return, not at the point of sale. Sales tax must still be collected on groceries. [T1]

### EC4 -- SaaS vs. Canned Software Distinction [T2]

**Situation:** A software company sells both downloadable software licenses ($500 one-time) and a SaaS subscription ($50/month) to Idaho customers.

**Resolution:**
- Downloadable canned software with a permanent license: likely taxable as TPP. [T2]
- SaaS subscription: generally not taxable under current Idaho law. [T2]
- The company should separately invoice these products and apply tax only to the taxable component. [T2]
- **Flag for reviewer:** Idaho's treatment of electronically delivered software is evolving. Verify current STC guidance before advising. [T2]

---

### EC5 -- Tourism Season and Resort City Boundaries [T2]

**Situation:** A customer places an online order for delivery to a vacation cabin. The cabin's address is near Sun Valley but may or may not be within the resort city boundary.

**Resolution:**
- Resort city tax only applies within the legal boundaries of the resort city. [T1]
- Addresses just outside the city limits are subject to state tax only (6%). [T1]
- Address verification against resort city boundary maps is required. [T2]
- SST-certified rate databases include resort city boundary data. [T1]
- **Flag for reviewer:** Resort city boundaries do not always align with intuitive geographic areas. Verify with STC mapping tools. [T2]

### EC6 -- Fabrication vs. Repair Classification [T2]

**Situation:** A machine shop creates custom parts for a customer (fabrication). Is the labor taxable?

**Resolution:**
- Fabrication (creating new items) is treated differently from repair. [T2]
- The sale of custom-fabricated items is a sale of TPP -- the full invoice (materials + fabrication labor) is taxable. [T1]
- Repair of existing items with separately stated labor: labor is exempt, parts are taxable. [T1]
- The distinction between fabrication and repair matters for tax purposes. [T2]
- **Flag for reviewer:** Classify the transaction as fabrication (fully taxable) or repair (labor separable). [T2]

---

## Test Suite

### Test 1 -- Basic Taxable Sale

**Input:** Seller in Boise sells $1,000 of office equipment to a local buyer. State rate = 6% (no resort city tax in Boise).
**Expected output:** Sales tax = $1,000 x 6% = $60.00. Total = $1,060.00.

### Test 2 -- Resort City Sale

**Input:** Seller ships a $500 item to a buyer in Sun Valley. State rate = 6%, resort city tax = 3%. Combined = 9%.
**Expected output:** Sales tax = $500 x 9% = $45.00. Total = $545.00.

### Test 3 -- Grocery Food Taxable

**Input:** Customer buys $200 of unprepared groceries at a Boise supermarket. Rate = 6%.
**Expected output:** Groceries ARE taxable in Idaho. Tax = $200 x 6% = $12.00. Total = $212.00.

### Test 4 -- Repair with Separately Stated Labor

**Input:** Auto repair shop charges $400 parts + $250 labor (separately stated) in Pocatello. Rate = 6%.
**Expected output:** Tax on parts only. Tax = $400 x 6% = $24.00. Labor ($250) is exempt (separately stated). Total = $674.00.

### Test 5 -- Economic Nexus Threshold

**Input:** Online retailer sold $90,000 into Idaho in the prior calendar year with 300 transactions.
**Expected output:** Revenue ($90,000) is below $100,000 threshold. Idaho uses revenue only (no transaction test). No economic nexus based on these facts.

---

### Test 6 -- Use Tax Self-Assessment

**Input:** Idaho business in Boise purchases $3,000 of supplies from an Oregon vendor (no tax collected). Boise combined rate = 6%.
**Expected output:** Use tax due = $3,000 x 6% = $180.00. Reported on Form 850.

### Test 7 -- Fabrication vs. Repair

**Input:** Machine shop fabricates custom brackets for $800 ($300 materials, $500 labor) for a Boise customer. Rate = 6%.
**Expected output:** Fabrication = sale of TPP. Full $800 is taxable. Tax = $800 x 6% = $48.00. Total = $848.00.

### Test 8 -- Manufacturing Equipment Exemption

**Input:** Manufacturer purchases $50,000 CNC machine for direct use in production at Idaho plant.
**Expected output:** Manufacturing equipment used directly in production is exempt. Tax = $0. Total = $50,000.

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
