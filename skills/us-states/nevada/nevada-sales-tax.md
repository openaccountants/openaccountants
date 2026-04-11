---
name: nevada-sales-tax
description: Use this skill whenever asked about Nevada sales tax, Nevada use tax, Nevada Tax Department sales tax filing, Nevada mining tax, or Nevada sales tax compliance. Trigger on phrases like "Nevada sales tax", "NV sales tax", "NRS 372", "Nevada Tax Dept", "Nevada no income tax", "Nevada mining", or any request involving Nevada state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# Nevada Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Nevada, United States |
| Jurisdiction Code | US-NV |
| Tax Type | Sales and Use Tax (state + local) |
| State Rate | 6.85% |
| Maximum Combined Rate | ~8.375% (state 6.85% + local up to ~1.525%) |
| Primary Statute | Nevada Revised Statutes (NRS) Chapter 372 |
| Governing Agency | Nevada Department of Taxation |
| Portal | https://tax.nv.gov |
| SST Member | Yes -- Full Member |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics. T2: local rate determination, mining industry rules, exemption specifics. T3: audit defense, complex mining transactions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Nevada sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Nevada sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Nevada? | Drives taxability classification under Nevada law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Nevada? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Nevada local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Sales Tax Rate

Nevada imposes a combined state sales tax rate of **6.85%**, which itself is composed of multiple state-level components:

| Component | Rate |
|-----------|------|
| State general fund | 2.00% |
| Local School Support Tax (LSST) | 2.60% |
| State supplemental city/county relief | 0.50% |
| Infrastructure projects | 0.175% |
| Basic city/county relief | 1.75% |
| **Total "state" rate** | **6.85%** |

**Statute:** NRS 372.105 and related statutes.

### 1.2 Local Add-On Taxes [T1]

- Counties and certain cities may impose additional sales taxes (county option tax, city/county relief tax supplemental). [T1]
- Local add-ons range from 0% to approximately **1.525%**. [T1]
- Clark County (Las Vegas): combined rate typically **8.375%**. [T1]
- Washoe County (Reno): combined rate typically **8.265%**. [T1]
- Rural counties may have lower combined rates. [T1]
- Maximum combined rate across all jurisdictions: approximately **8.375%**. [T1]

### 1.3 No State Income Tax [T1]

Nevada has **no state individual or corporate income tax**. Sales tax is a primary revenue source. [T1]

Nevada does impose a **Commerce Tax** on businesses with Nevada gross revenue exceeding $4 million (rate varies by industry, ~0.051% to 0.331%). NRS 363C. [T2]

### 1.4 Sourcing [T1]

Nevada uses **destination-based** sourcing. [T1]

As an SST member, Nevada follows SSUTA sourcing rules. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food -- EXEMPT [T1]

- Unprepared grocery food: **exempt**. NRS 372.284. [T1]
- Prepared food: taxable at the full combined rate. [T1]
- Candy: taxable (excluded from food exemption). [T1]
- Soft drinks: taxable. [T1]
- Nevada follows SST food definitions. [T1]

### 2.2 Clothing [T1]

- Clothing is **fully taxable**. No exemption. [T1]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. NRS 372.283. [T1]
- OTC drugs: **exempt**. [T1]
- DME: exempt. [T1]
- Prosthetics: exempt. [T1]

### 2.4 Services [T2]

Nevada taxes very few services:

- **Taxable services include:** Telecommunications (bundled with TPP), extended warranties/service contracts when separately stated. [T2]
- **Exempt services include:** Most services -- professional, personal care, repair labor, cleaning, landscaping, IT services. Nevada has a narrow sales tax base focused on TPP. [T2]

### 2.5 SaaS and Digital Goods [T2]

- **SaaS:** Generally **not taxable** in Nevada. Not considered TPP or an enumerated taxable item. [T2]
- **Canned software (physical):** Taxable. [T1]
- **Canned software (electronic delivery):** Taxability is unclear; generally not taxable under current practice. [T2]
- **Digital downloads:** Generally not taxable. [T2]
- **Custom software:** Exempt. [T2]

### 2.6 Manufacturing [T2]

- Manufacturing equipment: no specific broad manufacturing exemption exists in Nevada. [T2]
- Certain specialized equipment may qualify for specific incentive programs (e.g., abatements for qualifying businesses). [T2]
- Raw materials incorporated into products for resale: exempt under the resale exemption. [T1]

### 2.7 Mining -- Special Rules [T2]

- Mining is a major Nevada industry. Special tax rules apply:
  - Mining equipment and machinery: generally taxable at the full rate. [T2]
  - The Net Proceeds of Minerals Tax (NRS Chapter 362) is a separate tax on the net proceeds of mining operations. This is NOT a sales tax but is an important compliance consideration for mining companies. [T2]
  - Explosives and chemicals used in mining: taxable unless a specific exemption applies. [T2]
  - **Flag for reviewer:** Mining tax compliance in Nevada involves multiple tax types beyond sales tax. Escalate to a mining tax specialist. [T3]

### 2.8 Motor Vehicles [T1]

- Motor vehicles: subject to a Governmental Services Tax (GST) at registration rather than sales tax. NRS 371.101. [T1]
- The GST is based on the original MSRP and depreciates over time. [T1]
- Out-of-state vehicle purchases: use tax may apply. [T2]

### 2.9 Agricultural [T1]

- Farm machinery and equipment: taxable (no broad agricultural exemption). [T2]
- Feed, seed, fertilizer for commercial agriculture: partially exempt. [T2]
- Livestock: exempt for breeding/dairy purposes. [T2]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | Sales/Use Tax Return (filed via Nevada Tax Center) |
| Filing Frequencies | Monthly (>$10,000/quarter tax); Quarterly (most common) |
| Due Date | Last day of the month following the reporting period |
| Portal | https://nevadatax.nv.gov (Nevada Tax Center) |
| E-filing | Required for most filers |

**Note:** Nevada's due date is the **last day** of the month, not the 20th. [T1]

### 4.2 Vendor Discount [T1]

Nevada does NOT offer a vendor discount for timely filing. [T1]

### 4.3 Penalties and Interest [T1]

- Late filing/payment penalty: 10% of tax due. [T1]
- Interest: rate set by statute (typically prime rate + specified percentage). [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for Nevada. Key categories: [T1]

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
| Revenue Threshold | $100,000 in Nevada sales |
| Transaction Threshold | 200 transactions |
| Test | OR (either threshold triggers nexus) |
| Measurement Period | Current or prior calendar year |
| Effective Date | October 1, 2018 |

**Statute:** NRS 372.724.

### 3.2 Marketplace Facilitator [T1]

Nevada requires marketplace facilitators to collect and remit. NRS 372.7285. [T1]

### 3.3 SST Registration [T1]

Full SST member. Remote sellers can register via SSTRS and use CSPs. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER apply a single rate across Nevada. Combined rates vary by county and city. [T1]
- NEVER assume Nevada has a simple low tax environment because it has no income tax. Multiple other taxes (Commerce Tax, Modified Business Tax, GST) apply. [T1]
- NEVER apply sales tax to motor vehicle purchases at the point of sale. Nevada uses GST at registration instead. [T1]
- NEVER tax grocery food in Nevada. Unprepared food is exempt. [T1]
- NEVER file Nevada returns by the 20th. The due date is the **last day** of the following month. [T1]
- NEVER assume SaaS or digital goods are taxable in Nevada. Current law does not tax them. [T2]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Clark County (Las Vegas) Combined Rate [T2]

**Situation:** A seller ships to a Las Vegas address. What is the combined rate?

**Resolution:**
- Clark County combined rate is typically **8.375%** (6.85% state + 1.525% local). [T1]
- Verify the exact rate for the specific delivery address, as some areas within Clark County may have different local add-ons. [T2]
- **Flag for reviewer:** Use Nevada Tax Department rate lookup tools for precise address-level rates. [T2]

### EC2 -- Mining Company Tax Obligations [T3]

**Situation:** A gold mining company operates in northern Nevada. What sales tax obligations exist?

**Resolution:**
- Equipment, supplies, and materials purchased for mining operations are subject to sales tax at the applicable combined rate. [T1]
- The Net Proceeds of Minerals Tax is a separate obligation (not sales tax). [T1]
- The Commerce Tax may also apply if Nevada gross revenue exceeds $4 million. [T2]
- Mining companies face multiple Nevada tax obligations beyond sales tax. [T2]
- **Flag for reviewer:** Mining tax compliance requires specialized expertise. Escalate to a mining/natural resources tax specialist. [T3]

### EC3 -- No Income Tax Interaction [T1]

**Situation:** A business considers relocating to Nevada. What consumption tax differences should they consider?

**Resolution:**
- Nevada has no individual or corporate income tax. [T1]
- Sales tax rates are moderate but not low (6.85% state + local). [T1]
- The Commerce Tax applies to businesses with gross revenue exceeding $4 million. [T2]
- Modified Business Tax (payroll tax) applies to employers. [T2]
- **Flag for reviewer:** The total tax burden analysis in a no-income-tax state requires evaluating all tax types, not just sales tax. [T2]

### EC4 -- Motor Vehicle GST vs. Sales Tax [T2]

**Situation:** A customer buys a car in Nevada. Why is sales tax not charged at the dealership?

**Resolution:**
- Nevada imposes a Governmental Services Tax (GST) on vehicles at registration rather than sales tax at the point of sale. [T1]
- GST is calculated based on the MSRP and depreciates annually. [T1]
- This is different from most states that impose sales tax on the purchase price. [T1]
- **Flag for reviewer:** Do not attempt to calculate vehicle GST using the sales tax rate. The GST calculation method is different. [T2]

---

### EC5 -- Hotel Resort Fee Taxation [T2]

**Situation:** A Las Vegas hotel charges $300/night for the room plus a $45 mandatory "resort fee." Is the resort fee taxable?

**Resolution:**
- Mandatory resort fees that are required to complete the room purchase are part of the taxable room charge. [T2]
- Tax applies to the combined $345 ($300 room + $45 resort fee) at the combined rate. [T2]
- Voluntary charges for optional services (spa, golf) may be taxed separately based on their category. [T2]
- **Flag for reviewer:** Mandatory vs. voluntary fee distinction is important. Mandatory fees are generally taxable as part of the room charge. [T2]

### EC6 -- Convention/Trade Show Sales [T2]

**Situation:** A vendor sells merchandise at a Las Vegas trade show. Do they have nexus and must they collect?

**Resolution:**
- Physical presence at a trade show creates nexus in Nevada. [T1]
- The vendor must collect Nevada sales tax at the Clark County combined rate (8.375%). [T1]
- If the vendor only attends for a few days, they may still have nexus for the duration. [T1]
- **Flag for reviewer:** Las Vegas trade show vendors frequently have nexus. Ensure registration and collection at the correct rate. [T2]

### EC7 -- Exempt Sale for Resale with SSUT Certificate [T2]

**Situation:** A wholesaler sells goods to a retailer who provides a valid resale certificate.

**Resolution:**
- The sale is exempt from sales tax. [T1]
- The wholesaler must retain the certificate on file. [T1]
- Nevada accepts the MTC Uniform Exemption Certificate. [T1]
- If the certificate is missing or invalid, the wholesaler is liable for the uncollected tax. [T1]
- **Flag for reviewer:** Verify the resale certificate is properly completed with a valid Nevada tax ID. [T2]

---

## Test Suite

### Test 1 -- Sale in Las Vegas

**Input:** Seller in Las Vegas sells $1,000 of electronics. Clark County combined rate = 8.375%.
**Expected output:** Tax = $1,000 x 8.375% = $83.75. Total = $1,083.75.

### Test 2 -- Grocery Food Exemption

**Input:** Customer buys $200 of unprepared groceries in Reno. Combined rate = 8.265%.
**Expected output:** Groceries are EXEMPT. Tax = $0. Total = $200.00.

### Test 3 -- Sale in Rural County

**Input:** Seller ships $500 item to a customer in Elko County. Combined rate = 7.10%.
**Expected output:** Tax = $500 x 7.10% = $35.50. Total = $535.50.

### Test 4 -- OTC Drug Exemption

**Input:** Customer buys $30 OTC medication in Las Vegas.
**Expected output:** OTC drugs are exempt in Nevada. Tax = $0. Total = $30.00.

### Test 5 -- Economic Nexus

**Input:** Remote seller from California sold $110,000 to Nevada customers in the prior year.
**Expected output:** $110,000 exceeds $100,000 threshold. Nexus IS triggered. Must register and collect.

---

### Test 6 -- Hotel with Resort Fee

**Input:** Hotel in Las Vegas charges $250/night + $40 mandatory resort fee. Combined rate = 8.375%.
**Expected output:** Taxable amount = $290. Tax = $290 x 8.375% = $24.29. Total = $314.29.

### Test 7 -- Trade Show Sale

**Input:** Vendor at a Las Vegas convention sells $2,000 of merchandise. Clark County rate = 8.375%.
**Expected output:** Tax = $2,000 x 8.375% = $167.50. Total = $2,167.50.

### Test 8 -- Prescription Drug Exemption

**Input:** Pharmacy sells $150 prescription drug and $25 OTC cold medicine in Reno.
**Expected output:** Both are exempt in Nevada. Tax = $0. Total = $175.00.

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
