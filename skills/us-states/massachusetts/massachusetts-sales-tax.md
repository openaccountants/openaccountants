---
name: massachusetts-sales-tax
description: Use this skill whenever asked about Massachusetts sales and use tax, MA DOR filings, Massachusetts clothing exemption, Massachusetts meals tax, Massachusetts exemptions, Massachusetts nexus, or any request involving Massachusetts state sales and use tax compliance. Trigger on phrases like "Massachusetts sales tax", "MA sales tax", "MA DOR", "ST-9", "Massachusetts clothing exemption", "Massachusetts meals tax", "Massachusetts resale certificate", or any request involving Massachusetts sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any Massachusetts sales tax work.
---

# Massachusetts Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Massachusetts, United States |
| Jurisdiction Code | US-MA |
| Tax Type | Sales and Use Tax (state only -- limited local option on meals/rooms) |
| Primary Legislation | Massachusetts General Laws (M.G.L.) Chapter 64H (Sales Tax) and Chapter 64I (Use Tax) |
| Key Statutes | M.G.L. c.64H, Sections 1-35; M.G.L. c.64I, Sections 1-9 |
| Tax Authority | Massachusetts Department of Revenue (MA DOR) |
| Filing Portal | https://www.mass.gov/orgs/massachusetts-department-of-revenue |
| Federal Framework Skill | us-sales-tax (read first for Wayfair, nexus overview, and multi-state context) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires Massachusetts CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate structure, clothing exemption ($175), meals tax, basic taxability, filing mechanics, nexus thresholds. Tier 2: SaaS taxability, mixed transactions, local meals option. Tier 3: audit defense, complex bundled transactions, DOR rulings. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to a licensed tax professional and document the gap.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Massachusetts sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Massachusetts sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Massachusetts? | Drives taxability classification under Massachusetts law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Massachusetts? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Massachusetts local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Rate

The Massachusetts state sales and use tax rate is **6.25%**. [T1]

**Legislation:** M.G.L. c.64H, Section 2.

### 1.2 No General Local Taxes

Massachusetts generally imposes **no local sales taxes**. The 6.25% rate is uniform statewide for most transactions. [T1]

**Exception -- Local Option Meals Tax:** Municipalities may impose a **local option meals tax** of up to **0.75%** on top of the state meals tax. Over 100 municipalities have adopted this local option. When adopted, the total meals tax rate is **7.00%** (6.25% state + 0.75% local). M.G.L. c.64L. [T1]

**Exception -- Local Option Room Occupancy Tax:** Municipalities may impose a local option room occupancy excise of up to **6%** in addition to the state 5.7% room occupancy excise. This is separate from sales tax. [T1]

### 1.3 Meals Tax [T1]

Massachusetts imposes a **meals tax** on food and beverages sold by restaurants, snack bars, caterers, and similar establishments:

- State rate: **6.25%** (same as general sales tax). [T1]
- Local option: up to **0.75%** additional. [T1]
- Combined maximum meals tax: **7.00%**. [T1]
- Applies to ALL food sold by restaurants, including items that would be exempt if sold by a grocery store. [T1]

**Legislation:** M.G.L. c.64H, Section 6(h); M.G.L. c.64L.

### 1.4 Sourcing [T1]

Since there is no local sales tax variation (except meals), sourcing is straightforward:

- The 6.25% state rate applies uniformly for sales tax. [T1]
- For meals, determine whether the municipality has adopted the local 0.75% option. [T2]

---

## Step 3: Return Form Structure
### 5.1 Filing Form

The primary return is **Form ST-9 -- Sales and Use Tax Return**. [T1]

Other forms:
- **ST-9A** -- Annual return (for annual filers)
- **ST-MAB** -- Meals tax return (for local option municipalities)

### 5.2 Filing Frequency [T1]

| Frequency | Criteria | Due Date |
|-----------|----------|----------|
| Monthly | Tax liability > $100/month | 20th of the following month |
| Quarterly | Tax liability $100 or less/month | 20th of the month following the quarter |
| Annual | Tax liability less than $100/year | January 31 following the year |

**Quarterly due dates:**

| Quarter | Period | Due Date |
|---------|--------|----------|
| Q1 | January 1 -- March 31 | April 20 |
| Q2 | April 1 -- June 30 | July 20 |
| Q3 | July 1 -- September 30 | October 20 |
| Q4 | October 1 -- December 31 | January 20 |

**Legislation:** M.G.L. c.62C, Section 16.

### 5.3 Electronic Filing [T1]

- Electronic filing is available and encouraged through **MassTaxConnect**. [T1]
- Required for vendors with liability over certain thresholds. [T1]

### 5.4 Vendor Discount [T1]

Massachusetts does **NOT** offer a vendor discount. Sellers retain no portion of collected tax. [T1]

### 5.5 Penalties and Interest [T1]

| Penalty | Rate | Citation |
|---------|------|----------|
| Late filing | 1% of tax due per month (max 25%) | M.G.L. c.62C, Sec. 33(a) |
| Late payment | Same | M.G.L. c.62C, Sec. 33(a) |
| Negligence/intentional disregard | 25% of underpayment | M.G.L. c.62C, Sec. 35A |
| Fraud | 75% of underpayment | M.G.L. c.62C, Sec. 35A |
| Interest | Rate set by DOR (adjusted annually) | M.G.L. c.62C, Sec. 32 |

---

## Step 4: Deductibility / Exemptions
### 7.1 Massachusetts Resale Certificate [T1]

- **Form:** ST-4 (Sales Tax Resale Certificate). [T1]
- Must include the buyer's MA registration number. [T1]
- Massachusetts also accepts the **MTC Uniform Sales Tax Certificate**. [T1]
- Massachusetts does NOT accept the SST Certificate (MA is not SST member). [T1]
- Blanket certificates permitted. [T1]

### 7.2 Exempt Purchaser Certificate [T1]

- **Form:** ST-2 (Sales Tax Exempt Purchaser Certificate). [T1]
- For qualifying 501(c)(3) organizations. [T1]
- Has expiration date. [T1]

### 7.3 Other Certificates [T1]

| Certificate | Form | Purpose |
|------------|------|---------|
| Farmer | ST-12 | Agricultural exemption |
| Contractor (Exempt Project) | ST-12A | Exempt project purchases |
| Government Entity | Government-issued ID | Government exempt purchases |

---


### 6.1 When Use Tax Applies

Use tax applies when:

- A Massachusetts purchaser acquires TPP from a seller who did not collect MA tax. [T1]
- TPP is purchased tax-free and diverted to taxable use. [T1]
- TPP is brought into Massachusetts for use, storage, or consumption. [T1]

**Legislation:** M.G.L. c.64I.

### 6.2 Use Tax Rate [T1]

Use tax rate is **6.25%** (same as sales tax -- no local variation except for meals). [T1]

### 6.3 Reporting Use Tax [T1]

- **Registered vendors:** Report on Form ST-9. [T1]
- **Individuals:** Report on Form 1 (MA Income Tax Return), Line 34. [T1]

### 6.4 Credit for Tax Paid to Other States [T1]

Massachusetts allows a credit for sales/use tax legally paid to another state. M.G.L. c.64I, Section 7(a). [T1]

---

## Step 5: Key Thresholds
### 4.1 Who Must Register

Any vendor making retail sales in Massachusetts must register with DOR and obtain a **Sales Tax Registration Certificate (Form ST-1)**. M.G.L. c.64H, Section 7. [T1]

### 4.2 Economic Nexus Threshold [T1]

Massachusetts's economic nexus threshold:

- **$100,000** in Massachusetts sales during the preceding calendar year. [T1]
- **No transaction count threshold** -- revenue only. [T1]
- Effective date: October 1, 2019 (for sales tax; MA had an earlier cookie-based nexus standard for internet vendors). [T1]

**Legislation:** 830 CMR 64H.1.7; DOR Directive 17-1.

### 4.3 Marketplace Facilitator Rules [T1]

Massachusetts requires marketplace facilitators to collect and remit sales tax:

- Effective October 1, 2019. [T1]
- Marketplace facilitators are treated as retailers. [T1]
- Marketplace sellers relieved for facilitated sales. [T1]

**Legislation:** M.G.L. c.64H, Section 1.

### 4.4 Registration Process [T1]

1. Register online via **MassTaxConnect** (https://mtc.dor.state.ma.us). [T1]
2. Receive a **Sales Tax Registration Certificate**. [T1]
3. Filing frequency assigned by DOR. [T1]
4. No fee. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- **NEVER** charge full tax on a clothing item over $175 -- only tax the amount ABOVE $175 (sliding scale). [T1]
- **NEVER** confuse MA's $175 clothing threshold with NY's $110 threshold or NJ's unlimited exemption. [T1]
- **NEVER** charge sales tax on off-premises alcohol -- MA voters repealed this tax in 2010. [T1]
- **NEVER** forget the local option meals tax -- check whether the municipality has adopted the 0.75% add-on. [T2]
- **NEVER** treat SaaS as nontaxable in Massachusetts -- SaaS is taxable under DOR Directive 13-3. [T1]
- **NEVER** apply local sales tax rates for general merchandise -- MA has no local sales tax (only local meals and room taxes). [T1]
- **NEVER** accept the SST Certificate in Massachusetts -- MA is not an SST member. [T1]
- **NEVER** assume OTC drugs are taxable -- Massachusetts exempts OTC drugs and medicine. [T1]
- **NEVER** assume all digital goods are taxable -- MA specifically targets software (including SaaS); other digital products may not be enumerated. [T2]
- **NEVER** assume the vendor retains a discount -- MA has NO vendor discount. [T1]

---

## Edge Case Registry

### EC1 -- Clothing Sliding Scale: $200 Item [T1]

**Situation:** Customer buys a $200 pair of shoes.

**Resolution:** First $175 is EXEMPT. Only $25 ($200 - $175) is taxable. Tax = $25 x 6.25% = $1.56. This is different from New York's approach (which would tax the ENTIRE item if it's $110 or more).

### EC2 -- Multiple Clothing Items at Different Prices [T1]

**Situation:** Customer buys a $100 shirt, a $175 jacket, and a $300 coat.

**Resolution:** Shirt: $0 tax (under $175). Jacket: $0 tax (exactly $175). Coat: ($300 - $175) x 6.25% = $7.81 tax. Total tax = $7.81. Each item assessed individually.

### EC3 -- Meals Tax with Local Option [T1]

**Situation:** A restaurant in Boston serves a $50 meal. Boston has adopted the 0.75% local option meals tax.

**Resolution:** State meals tax: $50 x 6.25% = $3.13. Local meals tax: $50 x 0.75% = $0.38. Total meals tax: $3.51 (7.00% effective rate). The restaurant reports the local option separately on Form ST-MAB.

### EC4 -- Alcoholic Beverages -- Off-Premises vs. Restaurant [T1]

**Situation:** A liquor store sells a $20 bottle of wine. A restaurant sells a $20 glass of wine.

**Resolution:** Liquor store (off-premises): $0 tax. MA voters repealed the sales tax on off-premises alcohol in 2010. Restaurant (on-premises): $20 is subject to the meals tax at 6.25% (+ local option if applicable). Tax = $1.25 minimum.

### EC5 -- Sales Tax Holiday [T1]

**Situation:** Customer asks about the annual sales tax holiday.

**Resolution:** Massachusetts typically declares an annual **Sales Tax Holiday** (usually one weekend in August). During this period, qualifying items priced at $2,500 or less per item are exempt from sales tax. Clothing already exempt under $175 is unaffected. Items over $2,500 remain taxable. The exact dates and dollar threshold are set by annual legislation. M.G.L. c.64H, Section 6A.

### EC6 -- SaaS Taxability [T1]

**Situation:** A MA business subscribes to a cloud-based CRM (SaaS) for $150/month.

**Resolution:** TAXABLE at 6.25%. Tax = $9.38/month. MA DOR Directive 13-3 treats SaaS as a sale/license of prewritten computer software, taxable regardless of delivery method.

### EC7 -- Custom Software Exempt [T1]

**Situation:** A MA business hires a developer to create custom software. Cost: $50,000.

**Resolution:** EXEMPT. Custom software is not prewritten software and is treated as a professional service. No sales tax. This contrasts with Washington State (which taxes custom software).

### EC8 -- Motor Vehicle Use Tax [T1]

**Situation:** A MA resident purchases a car from a private party in New Hampshire (no sales tax state) for $25,000.

**Resolution:** MA use tax of 6.25% is due: $25,000 x 6.25% = $1,562.50. Paid at the time of registration with the Registry of Motor Vehicles (RMV). If the car was purchased in a state with sales tax, a credit applies for tax paid to that state.

### EC9 -- Telecom Services Taxable [T1]

**Situation:** A MA business pays $500/month for telephone and internet services.

**Resolution:** Telecommunications services are TAXABLE at 6.25%. Tax = $31.25/month. M.G.L. c.64H, Section 1(13)(b). Note: Internet access is generally exempt under the federal Internet Tax Freedom Act (ITFA), but bundled telecom/internet packages may require allocation. [T2]

### EC10 -- Vendor Purchases for Own Use [T1]

**Situation:** A retailer withdraws $500 of merchandise from inventory for personal use.

**Resolution:** The retailer must self-assess and pay use tax of 6.25% on the cost of goods withdrawn. Tax = $31.25. Report on Form ST-9.

---

## Test Suite

### Test 1 -- Clothing Under $175 [T1]

**Input:** Customer buys a $150 dress at a MA store.
**Expected output:** Sales tax = $0. Clothing under $175 is exempt.

### Test 2 -- Clothing Over $175 (Sliding Scale) [T1]

**Input:** Customer buys a $250 pair of boots.
**Expected output:** Taxable portion = $250 - $175 = $75. Tax = $75 x 6.25% = $4.69.

### Test 3 -- Grocery Food Exempt [T1]

**Input:** Customer buys $200 of groceries (bread, milk, produce).
**Expected output:** Sales tax = $0. Grocery food exempt.

### Test 4 -- Restaurant Meal with Local Option [T1]

**Input:** Customer eats a $75 dinner at a restaurant in Cambridge (local meals tax adopted). Combined rate: 7.00%.
**Expected output:** Meals tax = $5.25 ($75 x 7.00%).

### Test 5 -- SaaS Subscription [T1]

**Input:** MA business subscribes to cloud-based accounting software. $100/month.
**Expected output:** Sales tax = $6.25/month. SaaS taxable under Directive 13-3.

### Test 6 -- Economic Nexus [T1]

**Input:** Out-of-state seller has $120,000 in MA sales in the preceding year. No physical presence.
**Expected output:** Exceeds $100,000 threshold. Must register with MA DOR and collect MA sales tax.

### Test 7 -- Off-Premises Alcohol Exempt [T1]

**Input:** Customer buys a $30 bottle of whiskey at a liquor store.
**Expected output:** Sales tax = $0. Off-premises alcohol exempt (2010 voter repeal).

### Test 8 -- Resale Certificate [T1]

**Input:** Retailer purchases $12,000 inventory from a MA wholesaler. Provides valid ST-4 resale certificate.
**Expected output:** No sales tax charged. Retailer collects tax at resale.

### Test 9 -- Use Tax on Out-of-State Purchase [T1]

**Input:** MA business purchases $4,000 of taxable office equipment from a New Hampshire retailer. No tax collected.
**Expected output:** Use tax = $250.00 ($4,000 x 6.25%). Report on ST-9 or Form 1.

### Test 10 -- Telecom Service Taxable [T1]

**Input:** MA business pays $800/month for telephone services.
**Expected output:** Sales tax = $50.00 ($800 x 6.25%). Telecommunications services are taxable.

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
