---
name: vermont-sales-tax
description: Use this skill whenever asked about Vermont sales tax, Vermont use tax, Vermont Tax Dept sales tax filing, Vermont local option tax, Vermont SaaS tax, or Vermont sales tax compliance. Trigger on phrases like "Vermont sales tax", "VT sales tax", "32 V.S.A. §9771", "Vermont Tax Dept", "Vermont local option", "Vermont SaaS", "Vermont SST", or any request involving Vermont state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# Vermont Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Vermont, United States |
| Jurisdiction Code | US-VT |
| Tax Type | Sales and Use Tax (state + local option) |
| State Rate | 6.00% |
| Local Option Tax | Up to 1.00% |
| Maximum Combined Rate | 7.00% |
| Primary Statute | 32 Vermont Statutes Annotated (V.S.A.) §9771 et seq. |
| Governing Agency | Vermont Department of Taxes |
| Portal | https://tax.vermont.gov |
| SST Member | Yes -- Full Member |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics. T2: local option tax, SaaS taxability, exemption specifics. T3: audit defense, complex transactions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Vermont sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Vermont sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Vermont? | Drives taxability classification under Vermont law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Vermont? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Vermont local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Sales Tax Rate

Vermont imposes a state sales tax of **6.00%** on the retail sale of tangible personal property and certain services. [T1]

**Statute:** 32 V.S.A. §9771.

### 1.2 Local Option Tax [T1]

- Municipalities may impose a **1% local option tax** on sales, meals, and/or alcohol. [T1]
- Not all municipalities have adopted the local option tax. [T1]
- Where adopted, the combined rate is **7.00%**. [T1]
- The local option tax is administered by the Vermont Department of Taxes. [T1]
- The local option on meals (9% meals tax + 1% local = 10%) is separate from the general sales tax local option. [T2]

### 1.3 Meals and Alcohol Tax [T1]

- Meals (prepared food served in restaurants): **9.00%** meals tax (not the 6% general rate). [T1]
- Alcoholic beverages served in restaurants/bars: **10.00%**. [T1]
- Alcoholic beverages for off-premises consumption: 6% sales tax. [T1]
- Local option adds 1% where adopted. [T2]

### 1.4 Sourcing [T1]

Vermont uses **destination-based** sourcing. [T1]

As an SST member, Vermont follows SSUTA sourcing rules. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food -- EXEMPT [T1]

- Unprepared grocery food: **exempt**. 32 V.S.A. §9741(13). [T1]
- Prepared food (restaurant meals): taxable at **9%** meals tax (not the 6% general rate). [T1]
- Candy: taxable at the general 6% rate. [T1]
- Soft drinks: taxable at the general 6% rate. [T1]

### 2.2 Clothing -- TAXABLE [T1]

- Clothing is **fully taxable** at the standard 6% rate (+ local option where applicable). [T1]
- Vermont does NOT have a clothing exemption. [T1]
- This distinguishes Vermont from neighboring states like New Hampshire (no sales tax) and Massachusetts (first $175 exempt). [T1]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. 32 V.S.A. §9741(2). [T1]
- OTC drugs: **exempt**. [T1]
- DME: exempt. [T1]
- Prosthetics: exempt. [T1]

### 2.4 Services [T2]

Vermont taxes a limited number of services:

- **Taxable services include:** Telecommunications, amusement/entertainment, fabrication, printing, cleaning (commercial), lodging (9% rooms tax), repair/maintenance when bundled with parts. [T2]
- **Exempt services include:** Professional services (legal, accounting, medical, engineering), personal care, landscaping, cleaning (residential), IT consulting. [T2]

### 2.5 SaaS and Digital Goods -- TAXABLE [T1/T2]

- **SaaS:** **Taxable** in Vermont. Vermont taxes prewritten software regardless of delivery method, including SaaS and cloud-based software. 32 V.S.A. §9701(7). [T1]
- **Canned software (physical and electronic):** Taxable. [T1]
- **Custom software:** Exempt. [T2]
- **Digital downloads:** Taxable as specified digital products. [T1]
- **Streaming services:** Taxable. [T2]

### 2.6 Manufacturing [T1]

- Manufacturing machinery and equipment: **exempt** when used directly in manufacturing. 32 V.S.A. §9741(25). [T1]
- Fuel and electricity used in manufacturing: exempt for manufacturing portion. [T2]

### 2.7 Lodging [T1]

- Rooms/lodging (hotels, B&Bs, vacation rentals): **9.00%** rooms tax. [T1]
- Local option adds 1% where adopted (total = 10%). [T2]
- Short-term rental platforms (Airbnb) must collect as marketplace facilitators. [T1]

### 2.8 Agricultural [T1]

- Farm machinery and equipment: exempt. 32 V.S.A. §9741(3). [T1]
- Feed, seed, fertilizer: exempt. [T1]
- Livestock: exempt for breeding/dairy. [T1]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | Form SU-452 (Sales and Use Tax Return) |
| Filing Frequencies | Monthly (>$500/month avg); Quarterly ($100-$500); Annually (<$100) |
| Due Date | 25th of the month following the reporting period |
| Portal | https://tax.vermont.gov (myVTax) |
| E-filing | Required for most filers |

**Note:** Vermont's due date is the **25th**, not the 20th. [T1]

### 4.2 Vendor Discount [T1]

Vermont does NOT offer a vendor discount for timely filing. [T1]

### 4.3 Penalties and Interest [T1]

- Late filing penalty: 5% of tax due per month, up to 25%. [T1]
- Interest: rate set annually (typically federal short-term rate + specified margin). [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for Vermont. Key categories: [T1]

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
| Revenue Threshold | $100,000 in Vermont sales |
| Transaction Threshold | 200 transactions |
| Test | OR (either threshold triggers nexus) |
| Measurement Period | Current or preceding 12-month period |
| Effective Date | July 1, 2018 |

**Statute:** 32 V.S.A. §9701(9).

### 3.2 Marketplace Facilitator [T1]

Vermont requires marketplace facilitators to collect and remit. 32 V.S.A. §9713. [T1]

### 3.3 SST Registration [T1]

Full SST member. SSTRS and CSPs available. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER assume clothing is exempt in Vermont. It is fully taxable. [T1]
- NEVER apply the 6% sales tax rate to restaurant meals. Meals are taxed at 9% (meals tax), not 6%. [T1]
- NEVER assume SaaS is exempt in Vermont. It is taxable. [T1]
- NEVER assume all municipalities have the local option tax. Not all have adopted it. [T2]
- NEVER file Vermont returns by the 20th. The due date is the **25th**. [T1]
- NEVER tax grocery food in Vermont. Unprepared food is exempt. [T1]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- SaaS Taxable in Vermont [T2]

**Situation:** A California SaaS company sells subscriptions to Vermont businesses.

**Resolution:**
- Vermont taxes SaaS at 6% (+ 1% local option where applicable). [T1]
- The SaaS company must register if economic nexus is met. [T1]
- Tax based on customer's Vermont location. [T1]
- **Flag for reviewer:** Vermont is on the list of states that clearly tax SaaS. Multi-state SaaS companies must include VT in their compliance matrix. [T2]

### EC2 -- Meals Tax vs. Sales Tax [T2]

**Situation:** A cafe sells both grocery items (bags of coffee beans) and prepared food (espresso drinks). Different rates apply.

**Resolution:**
- Bags of coffee beans: exempt (unprepared food). [T1]
- Espresso drinks: 9% meals tax (+ 1% local option where applicable). [T1]
- If the cafe also sells mugs or equipment: 6% general sales tax. [T1]
- **Flag for reviewer:** Mixed-use establishments must classify each revenue stream correctly. [T2]

### EC3 -- Local Option Tax Variance [T2]

**Situation:** A retailer ships to customers in Burlington (local option adopted) and a small town without local option tax.

**Resolution:**
- Burlington: 6% state + 1% local = 7%. [T1]
- Small town without local option: 6% only. [T1]
- Destination-based sourcing applies. Rate depends on delivery address. [T1]
- **Flag for reviewer:** Verify whether the specific municipality has adopted the local option. [T2]

### EC4 -- Clothing Taxable (Unlike Neighboring States) [T1]

**Situation:** A Vermont retailer near the New Hampshire border faces competitive pressure because NH has no sales tax.

**Resolution:**
- Vermont taxes clothing at the full 6% (+ local). [T1]
- New Hampshire has no sales tax. [T1]
- This price differential is a known cross-border shopping issue. [T1]
- Vermont retailers cannot unilaterally choose to not collect tax to compete. [T1]
- **Flag for reviewer:** Cross-border shopping is an economic reality but does not affect the legal obligation to collect tax. [T1]

---

### EC5 -- Brewery/Taproom Mixed Sales [T2]

**Situation:** A Vermont brewery sells: pints of beer consumed on-premises, cans/bottles for off-premises consumption, and merchandise (T-shirts, glasses).

**Resolution:**
- Pints on-premises: 10% alcoholic beverage tax. [T1]
- Cans/bottles for off-premises: 6% sales tax. [T1]
- Merchandise: 6% sales tax. [T1]
- Local option adds 1% to each category where adopted. [T2]
- The brewery must segregate sales by category for tax reporting. [T1]
- **Flag for reviewer:** Breweries, wineries, and distilleries face complex multi-rate compliance. Verify all revenue streams. [T2]

### EC6 -- SaaS Company Compliance [T2]

**Situation:** A SaaS startup from Vermont sells subscriptions to customers in Vermont and other states.

**Resolution:**
- Vermont sales to VT customers: taxable at 6% (+ local option). [T1]
- Out-of-state sales: apply destination state rules (SaaS taxability varies by state). [T2]
- The startup must determine which other states tax SaaS and whether economic nexus is met in each. [T2]
- **Flag for reviewer:** A Vermont SaaS company must evaluate multi-state SaaS taxability. Vermont taxing SaaS does not mean all states do. [T2]

### EC7 -- Ski Resort Season Pass [T2]

**Situation:** A Vermont ski resort sells season passes ($1,200) and single-day lift tickets ($120).

**Resolution:**
- Amusement/entertainment admissions are subject to the 6% sales tax. [T1]
- Season passes and lift tickets are taxable at 6% (+ local option). [T1]
- Lodging at the resort: 9% rooms tax (+ local option). [T1]
- Restaurant meals at the resort: 9% meals tax (+ local option). [T1]
- The resort must apply different rates to different revenue streams. [T1]
- **Flag for reviewer:** Ski resorts face complex multi-rate compliance across admissions, lodging, meals, and retail. [T2]

---

## Test Suite

### Test 1 -- Basic Taxable Sale

**Input:** Seller in Burlington sells $500 of electronics. Combined rate = 7% (6% state + 1% local).
**Expected output:** Tax = $500 x 7% = $35.00. Total = $535.00.

### Test 2 -- Grocery Food Exempt

**Input:** Customer buys $150 groceries in Montpelier.
**Expected output:** Groceries are EXEMPT. Tax = $0. Total = $150.00.

### Test 3 -- Restaurant Meal

**Input:** Customer dines in Burlington. Bill = $80. Meals tax = 9% + 1% local = 10%.
**Expected output:** Tax = $80 x 10% = $8.00. Total = $88.00.

### Test 4 -- SaaS Subscription

**Input:** SaaS company charges VT business $600/month. Rate = 6% (no local option at customer's location).
**Expected output:** SaaS IS taxable. Tax = $600 x 6% = $36.00. Total = $636.00.

### Test 5 -- Clothing Taxable

**Input:** Customer buys $200 jacket in Burlington. Combined rate = 7%.
**Expected output:** Clothing IS taxable in Vermont. Tax = $200 x 7% = $14.00. Total = $214.00.

---

### Test 6 -- Bar Tab (On-Premises Alcohol)

**Input:** Customer's bar tab is $60 for alcoholic beverages in Burlington. Alcoholic beverage tax = 10% + 1% local = 11%.
**Expected output:** Tax = $60 x 11% = $6.60. Total = $66.60.

### Test 7 -- Off-Premises Alcohol

**Input:** Customer buys $40 of wine at a Burlington liquor store. Sales tax = 6% + 1% local = 7%.
**Expected output:** Tax = $40 x 7% = $2.80. Total = $42.80.

### Test 8 -- Ski Lift Ticket

**Input:** Customer buys $130 lift ticket at a resort without local option tax. Rate = 6%.
**Expected output:** Lift tickets are taxable. Tax = $130 x 6% = $7.80. Total = $137.80.

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
