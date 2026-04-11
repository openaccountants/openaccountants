---
name: rhode-island-sales-tax
description: Use this skill whenever asked about Rhode Island sales tax, RI use tax, Rhode Island Tax Division filing, Rhode Island SaaS tax, or Rhode Island sales tax compliance. Trigger on phrases like "Rhode Island sales tax", "RI sales tax", "R.I.G.L. §44-18", "RI Tax Division", "Rhode Island clothing exemption", "Rhode Island SaaS", or any request involving Rhode Island sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# Rhode Island Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Rhode Island, United States |
| Jurisdiction Code | US-RI |
| Tax Type | Sales and Use Tax (state only -- no local sales tax) |
| State Rate | 7.00% (flat, uniform statewide) |
| Local Rates | None |
| Primary Statute | Rhode Island General Laws (R.I.G.L.) §44-18 et seq. |
| Governing Agency | Rhode Island Division of Taxation |
| Portal | https://www.tax.ri.gov |
| SST Member | Yes -- Full Member |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics. T2: SaaS taxability, clothing exemption threshold, service taxability. T3: audit defense, complex transactions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Rhode Island sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Rhode Island sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Rhode Island? | Drives taxability classification under Rhode Island law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Rhode Island? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Rhode Island local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Sales Tax Rate

Rhode Island imposes a flat, uniform sales tax of **7.00%**. This is one of the higher state rates in the country. [T1]

**Statute:** R.I.G.L. §44-18-18.

### 1.2 No Local Sales Taxes [T1]

Rhode Island does NOT permit local sales taxes. The 7% rate is the total rate statewide. [T1]

### 1.3 Sourcing [T1]

Rhode Island uses **destination-based** sourcing. [T1]

As an SST member, Rhode Island follows SSUTA sourcing rules. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food -- EXEMPT [T1]

- Unprepared grocery food: **exempt**. R.I.G.L. §44-18-30(7). [T1]
- Prepared food (restaurant meals): taxable at 8% (1% meals/beverage tax + 7% sales tax, but the meals tax is structured as a separate 1% additional tax). [T2]
- Candy: taxable. [T1]
- Soft drinks: taxable. [T1]

### 2.2 Clothing -- Exempt Under $250 [T1]

- Clothing and footwear items priced **under $250 per item**: **exempt**. R.I.G.L. §44-18-30(27). [T1]
- Clothing items priced $250 or more: the **entire amount** is taxable (not just the amount over $250). [T1]
- This is an all-or-nothing threshold -- a $249 shirt is exempt; a $250 shirt is fully taxable at 7%. [T1]

**Note:** This is similar to New York's clothing exemption structure (all-or-nothing) but with a higher threshold ($250 vs. $110). [T1]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. R.I.G.L. §44-18-30(8). [T1]
- OTC drugs: **taxable**. [T1]
- DME: exempt. [T1]
- Prosthetics: exempt. [T1]

### 2.4 Services [T2]

Rhode Island taxes a moderate number of services:

- **Taxable services include:** Telecommunications, cable/satellite TV, storage, pet grooming, cleaning (commercial), laundry/dry cleaning, pest control, security/alarm, printing. [T2]
- **Exempt services include:** Professional services (legal, accounting, medical, engineering), personal care (haircuts), education, financial services. [T2]

### 2.5 SaaS and Digital Goods -- TAXABLE [T1/T2]

- **SaaS:** **Taxable** at the full 7% rate. Rhode Island specifically taxes prewritten computer software regardless of the method of delivery or access, including SaaS. R.I.G.L. §44-18-7(8). [T1]
- **Canned software (physical and electronic):** Taxable. [T1]
- **Custom software:** Exempt. [T2]
- **Digital downloads:** Taxable. [T1]
- **Streaming services:** Taxable. [T2]

### 2.6 Manufacturing [T1]

- Machinery and equipment used directly in manufacturing: **exempt**. R.I.G.L. §44-18-30(22). [T1]
- Raw materials for resale: exempt under resale. [T1]

### 2.7 Lodging [T1]

- Hotel rooms and transient accommodations: 7% sales tax + 1% local hotel tax + 5% state hotel tax = **13%** total. [T1]
- Short-term rentals (Airbnb): same combined rate applies. [T1]

### 2.8 Meals and Beverages [T1]

- Meals (prepared food from restaurants): 7% sales tax + 1% local meals/beverage tax = **8%** total. [T1]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | T-204R (Sales and Use Tax Return) |
| Filing Frequencies | Monthly (>$200/month avg liability); Quarterly (most others); Annually (very small) |
| Due Date | 20th of the month following the reporting period |
| Portal | https://www.tax.ri.gov |
| E-filing | Required for most filers |

### 4.2 Vendor Discount [T1]

Rhode Island does NOT offer a vendor discount for timely filing. [T1]

### 4.3 Penalties and Interest [T1]

- Late filing penalty: 10% of tax due or $50, whichever is greater. [T1]
- Interest: 18% per annum (1.5% per month). [T1]
- Fraud penalty: 50% of tax due. [T1]

**Note:** Rhode Island's interest rate of 18% per annum is one of the highest in the nation. [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for Rhode Island. Key categories: [T1]

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
| Revenue Threshold | $100,000 in Rhode Island sales |
| Transaction Threshold | 200 transactions |
| Test | OR (either threshold triggers nexus) |
| Measurement Period | Current or prior calendar year |
| Effective Date | July 1, 2019 |

**Statute:** R.I.G.L. §44-18.2-2.

### 3.2 Marketplace Facilitator [T1]

Rhode Island requires marketplace facilitators to collect and remit. R.I.G.L. §44-18.2-3. [T1]

### 3.3 SST Registration [T1]

Full SST member. SSTRS and CSPs available. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER apply local tax add-ons in Rhode Island. There are NO local sales taxes. 7% is the total rate. [T1]
- NEVER assume SaaS is exempt in Rhode Island. It is explicitly taxable at 7%. [T1]
- NEVER apply the clothing exemption as a deduction. It is all-or-nothing at the $250 threshold. [T1]
- NEVER forget the separate 1% meals/beverage tax on prepared food. Total on meals = 8%. [T1]
- NEVER underestimate the penalty for late payment. RI charges 18% per annum interest. [T1]
- NEVER tax grocery food in Rhode Island. Unprepared food is exempt. [T1]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Clothing Exemption Threshold ($250) [T2]

**Situation:** A retailer sells a jacket for $249 and a pair of boots for $260.

**Resolution:**
- Jacket ($249): EXEMPT (under $250 threshold). Tax = $0. [T1]
- Boots ($260): FULLY TAXABLE (at or above $250). Tax = $260 x 7% = $18.20. [T1]
- This is an all-or-nothing threshold -- the exemption does not apply as a deduction. [T1]
- **Flag for reviewer:** Train retail staff that the $250 threshold is per-item, all-or-nothing. A $251 item is fully taxable. [T2]

### EC2 -- SaaS Taxable in Rhode Island [T2]

**Situation:** A SaaS company from California sells subscriptions to RI businesses. The company assumes SaaS is not taxable based on their experience in CA.

**Resolution:**
- Rhode Island taxes SaaS at the full 7% rate. [T1]
- The SaaS company must register (if economic nexus is met), collect 7%, and remit. [T1]
- R.I.G.L. §44-18-7(8) specifically includes prewritten software accessed remotely. [T1]
- **Flag for reviewer:** SaaS companies with multi-state customers must check RI's position. Rhode Island is one of the states that clearly taxes SaaS. [T2]

### EC3 -- High Interest Rate on Late Payments [T1]

**Situation:** A seller discovers they failed to remit RI sales tax for 12 months.

**Resolution:**
- RI charges 18% per annum (1.5% per month) interest on unpaid tax. [T1]
- Plus a 10% penalty. [T1]
- Combined penalty and interest can be substantial. [T1]
- Consider a Voluntary Disclosure Agreement (VDA) if the seller has multi-year exposure. [T2]
- **Flag for reviewer:** RI's 18% interest rate makes timely compliance critical. VDA should be considered for historical exposure. [T2]

### EC4 -- Meals Tax vs. Sales Tax on Prepared Food [T2]

**Situation:** A restaurant charges $50 for a meal. What is the total tax?

**Resolution:**
- Sales tax: 7%. [T1]
- Meals/beverage tax: additional 1%. [T1]
- Total tax rate on prepared food: **8%** ($4.00 on a $50 meal). [T1]
- The 1% meals/beverage tax is reported separately on the return. [T2]
- **Flag for reviewer:** Ensure restaurants are collecting and reporting both the 7% sales tax and the 1% meals tax. [T2]

---

### EC5 -- Multiple Clothing Items at Different Price Points [T2]

**Situation:** Customer buys: shirt ($50), pants ($100), jacket ($260), shoes ($249).

**Resolution:**
- Shirt ($50): EXEMPT (under $250). [T1]
- Pants ($100): EXEMPT (under $250). [T1]
- Jacket ($260): FULLY TAXABLE at 7% ($18.20 tax). [T1]
- Shoes ($249): EXEMPT (under $250). [T1]
- Total tax = $18.20. [T1]
- **Flag for reviewer:** Each item is evaluated independently. A $260 item is fully taxable even if other items in the same transaction are exempt. [T1]

### EC6 -- Digital Subscription Bundle [T2]

**Situation:** A company sells a bundle including SaaS access ($200), digital music streaming ($50), and a physical product ($100) to an RI customer. Single invoice.

**Resolution:**
- SaaS: taxable at 7%. [T1]
- Digital music streaming: taxable at 7%. [T1]
- Physical product: taxable at 7%. [T1]
- All three components are taxable, so bundling does not create a mixed-taxability issue. [T1]
- Total taxable = $350. Tax = $350 x 7% = $24.50. [T1]
- **Flag for reviewer:** If any component were exempt, bundled transaction rules would apply. [T2]

### EC7 -- Voluntary Disclosure Agreement (High Interest) [T2]

**Situation:** A company discovers 3 years of uncollected RI sales tax. The potential interest at 18% per annum is substantial.

**Resolution:**
- RI's 18% interest rate creates urgency for voluntary disclosure. [T1]
- The company should consider a VDA through the MTC National Nexus Program or directly with RI. [T2]
- A VDA may limit the look-back period and reduce or waive penalties. [T2]
- Interest is generally NOT waivable even under a VDA. [T2]
- **Flag for reviewer:** Given RI's high interest rate, speed is essential. Every month of delay adds 1.5% interest. [T2]

---

## Test Suite

### Test 1 -- Basic Taxable Sale

**Input:** Seller in Providence sells $1,000 of electronics. RI rate = 7%.
**Expected output:** Tax = $1,000 x 7% = $70.00. Total = $1,070.00.

### Test 2 -- Clothing Under $250 (Exempt)

**Input:** Customer buys a $200 jacket in Warwick. RI rate = 7%.
**Expected output:** Clothing under $250 is EXEMPT. Tax = $0. Total = $200.00.

### Test 3 -- Clothing At/Over $250 (Taxable)

**Input:** Customer buys $300 boots in Newport. RI rate = 7%.
**Expected output:** Clothing $250+ is FULLY taxable. Tax = $300 x 7% = $21.00. Total = $321.00.

### Test 4 -- SaaS Subscription

**Input:** SaaS company charges RI business $500/month. RI rate = 7%.
**Expected output:** SaaS IS taxable in RI. Tax = $500 x 7% = $35.00. Total = $535.00.

### Test 5 -- Restaurant Meal

**Input:** Customer has $80 dinner in Providence. Sales tax = 7%, meals tax = 1%. Total = 8%.
**Expected output:** Tax = $80 x 8% = $6.40. Total = $86.40.

---

### Test 6 -- Hotel Stay

**Input:** Guest stays 3 nights at a Providence hotel at $200/night. Total lodging rate = 13%.
**Expected output:** Room = $600. Tax = $600 x 13% = $78.00. Total = $678.00.

### Test 7 -- Mixed Clothing Purchase

**Input:** Customer buys a $240 coat (exempt) and a $260 dress (taxable). RI rate = 7%.
**Expected output:** Coat ($240 < $250): exempt. Dress ($260 >= $250): fully taxable. Tax = $260 x 7% = $18.20. Total = $518.20.

### Test 8 -- Digital Download

**Input:** Customer downloads $25 e-book. RI rate = 7%.
**Expected output:** Digital downloads are taxable. Tax = $25 x 7% = $1.75. Total = $26.75.

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
