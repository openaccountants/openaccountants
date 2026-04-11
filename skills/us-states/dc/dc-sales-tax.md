---
name: dc-sales-tax
description: Use this skill whenever asked about District of Columbia sales tax, DC use tax, DC OTR sales tax filing, DC restaurant tax, DC hotel tax, or DC sales tax compliance. Trigger on phrases like "DC sales tax", "District of Columbia sales tax", "OTR", "D.C. Code §47-2001", "DC restaurant tax", "DC hotel tax", or any request involving District of Columbia sales and use tax filing, classification, or compliance. ALWAYS load us-sales-tax first for federal context.
---

# District of Columbia Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | District of Columbia, United States |
| Jurisdiction Code | US-DC |
| Tax Type | Sales and Use Tax |
| General Rate | 6.00% |
| Restaurant/Alcohol Rate | 10.00% |
| Hotel/Transient Accommodations Rate | 10.25% |
| Parking Rate | 18.00% |
| Primary Statute | D.C. Code §47-2001 et seq. |
| Governing Agency | Office of Tax and Revenue (OTR) |
| Portal | https://mytax.dc.gov |
| SST Member | No |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: rates, basic taxability, filing mechanics. T2: special industry rates, service taxability, SaaS. T3: audit defense, complex exemption issues, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any District of Columbia sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a District of Columbia sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in District of Columbia? | Drives taxability classification under District of Columbia law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in District of Columbia? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple District of Columbia local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 Rate Structure -- Multiple Rates by Category [T1]

DC has a tiered rate structure with different rates for different categories:

| Category | Rate | Statute |
|----------|------|---------|
| General tangible personal property | 6.00% | D.C. Code §47-2002 |
| Restaurant meals, prepared food, and takeout | 10.00% | D.C. Code §47-2002(2) |
| Alcoholic beverages (off-premises) | 10.00% | D.C. Code §47-2002(3) |
| Liquor sold for on-premises consumption | 10.00% | D.C. Code §47-2002(2) |
| Transient accommodations (hotels, Airbnb) | 10.25% | D.C. Code §47-2002(1) |
| Parking and vehicle storage | 18.00% | D.C. Code §47-2002(4) |
| Car-sharing services | 10.25% | D.C. Code §47-2002 |
| Soft drinks | 8.00% | D.C. Code §47-2002 |
| Vapor products | 6.00% + excise | D.C. Code §47-2002 |

### 1.2 No Local Add-Ons [T1]

DC is a single jurisdiction -- there are NO county or city add-ons. The rates shown above are the total rates. This simplifies compliance compared to states with thousands of local jurisdictions. [T1]

### 1.3 Sourcing [T1]

DC uses **destination-based** sourcing. All sales delivered to addresses within DC are subject to DC tax. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food [T1]

- Unprepared grocery food and food ingredients: **exempt**. D.C. Code §47-2001(n)(1)(B). [T1]
- Prepared food (restaurant meals, takeout, delivery): taxable at **10%**. [T1]
- Candy: taxable at the general 6% rate. [T1]
- Soft drinks: taxable at **8%**. [T1]
- Bottled water: exempt (food). [T1]

### 2.2 Clothing [T1]

- Clothing is **fully taxable** at the general 6% rate. [T1]
- No clothing exemption exists in DC. [T1]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. D.C. Code §47-2005(14). [T1]
- Over-the-counter (OTC) drugs: **exempt**. [T1]
- Durable medical equipment (DME): exempt with prescription. [T1]
- Prosthetic devices: exempt. [T1]

### 2.4 Services [T2]

DC taxes a broad range of services:

- **Taxable services include:** Data processing, information services, telecommunications, cable/satellite TV, cleaning/janitorial, landscaping, security/alarm, pest control, parking (18%), dry cleaning, bottled water delivery, personal care services (spa, salon), storage, towing. [T2]
- **Exempt services include:** Professional services (legal, accounting, medical, engineering), education, financial services. [T2]
- **Repair services:** Taxable. [T2]

**Statute:** D.C. Code §47-2001(n)(1) (definition of sale).

### 2.5 SaaS and Digital Goods [T2]

- **SaaS:** **Taxable** in DC. DC taxes prewritten software and digital goods regardless of delivery method, including SaaS. D.C. Code §47-2001(n)(1)(A)(ii). [T1]
- **Canned software (physical and electronic):** Taxable. [T1]
- **Custom software:** Exempt if the software is developed specifically for one customer. [T2]
- **Digital downloads (music, e-books, digital video):** Taxable. [T1]
- **Streaming services:** Taxable as digital goods/data processing. [T2]

### 2.6 Lodging and Accommodations [T1]

- Hotel rooms and transient accommodations (including Airbnb, VRBO, and similar short-term rentals): **10.25%**. [T1]
- DC also imposes a separate hotel surcharge that funds the convention center and other initiatives. [T2]
- Short-term rental platforms must collect and remit as marketplace facilitators. [T1]

### 2.7 Motor Vehicles [T1]

- Motor vehicle purchases are subject to DC excise tax (separate from sales tax), typically **6%** based on vehicle weight. D.C. Code §50-2201.03. [T1]
- Trade-in credit reduces the taxable amount. [T1]

### 2.8 Alcohol and Tobacco [T1]

- Alcoholic beverages for off-premises consumption: **10%** sales tax. [T1]
- Alcoholic beverages for on-premises consumption: **10%** (included in restaurant meals rate). [T1]
- Tobacco products: subject to excise tax in addition to sales tax. [T1]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | FR-800A (monthly); FR-800Q (quarterly); FR-800 (annual) |
| Filing Frequencies | Monthly (>$1,200/year liability); Quarterly ($200-$1,200/year); Annually (<$200/year) |
| Due Date | 20th of the month following the reporting period |
| Portal | https://mytax.dc.gov |
| E-filing | Required for most filers |

### 4.2 Vendor Discount [T1]

DC does NOT offer a vendor discount for timely filing. [T1]

### 4.3 Penalties and Interest [T1]

- Late filing penalty: 5% of tax due per month, up to 25%. [T1]
- Late payment penalty: 5% per month, up to 25%. [T1]
- Interest: federal underpayment rate + 2%. [T1]
- Fraud penalty: 75% of tax due. [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for District of Columbia. Key categories: [T1]

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
| Revenue Threshold | $100,000 in DC sales |
| Transaction Threshold | 200 transactions |
| Test | OR (either threshold triggers nexus) |
| Measurement Period | Current or prior calendar year |
| Effective Date | January 1, 2019 |

**Statute:** D.C. Code §47-2001(r-1).

### 3.2 Physical Nexus [T1]

Standard physical nexus rules apply: office, warehouse, employees, inventory, or agents in DC create nexus. [T1]

Many businesses have physical nexus in DC due to federal government presence, lobbying offices, and trade association headquarters. [T2]

### 3.3 Marketplace Facilitator [T1]

DC requires marketplace facilitators to collect and remit sales tax on third-party sales made through their platforms. D.C. Code §47-2002.01a. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER apply a single rate to all DC transactions. DC has multiple rates depending on the category (6%, 8%, 10%, 10.25%, 18%). [T1]
- NEVER assume grocery food is taxable in DC. Unprepared food is exempt; prepared food is 10%; soft drinks are 8%. [T1]
- NEVER forget the 18% parking tax rate. It is one of the highest category-specific rates in the country. [T1]
- NEVER apply local add-on rates. DC has no local jurisdictions -- the stated rates are the total rates. [T1]
- NEVER assume SaaS is exempt in DC. DC taxes SaaS and digital goods. [T1]
- NEVER ignore the distinction between prepared and unprepared food. A 4-percentage-point difference (6% vs 10%) applies. [T1]
- NEVER advise that federal government employees are personally exempt from DC sales tax. Only the government entity itself (or qualifying diplomats with proper cards) is exempt. [T2]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Restaurant vs. Grocery Classification [T2]

**Situation:** A grocery store has a deli section selling prepared sandwiches and a bakery selling unpackaged pastries. The store also sells bottled drinks and packaged snacks.

**Resolution:**
- Prepared sandwiches from the deli: 10% (prepared food). [T1]
- Unpackaged pastries sold with eating utensils or heated: 10% (prepared food). [T1]
- Unpackaged pastries sold without utensils and not heated: 6% (general TPP) or potentially exempt if they qualify as food ingredients. [T2]
- Bottled soft drinks: 8%. [T1]
- Bottled water: exempt (food). [T1]
- Packaged snacks (chips, crackers): exempt (food ingredient). [T1]
- **Flag for reviewer:** The prepared food determination depends on whether items are heated, sold with utensils, or mixed for immediate consumption. Review each item category. [T2]

### EC2 -- SaaS Company Selling to DC Government [T2]

**Situation:** A SaaS company sells subscriptions to DC government agencies. Is the sale exempt?

**Resolution:**
- Sales to the DC government are **exempt** from DC sales tax. D.C. Code §47-2005(1). [T1]
- The DC government entity must provide a valid exemption certificate or purchase order. [T1]
- Sales to federal government agencies are also exempt. [T1]
- Sales to foreign embassies and international organizations with proper diplomatic exemption cards may also be exempt. [T2]
- **Flag for reviewer:** Verify the purchaser is a bona fide government entity and the exemption documentation is properly completed. [T2]

### EC3 -- Hotel Tax on Short-Term Rentals (Airbnb) [T2]

**Situation:** An individual rents out their DC apartment on Airbnb for $200/night.

**Resolution:**
- Short-term transient accommodations are taxable at **10.25%**. [T1]
- If booked through Airbnb (marketplace facilitator), Airbnb collects and remits the tax. [T1]
- If booked directly (not through a platform), the host must register with OTR, collect the 10.25% tax, and file returns. [T1]
- Additional DC requirements may apply, including a Clean Rivers Fee and regulatory permits. [T2]
- **Flag for reviewer:** Verify whether the platform is collecting tax as a marketplace facilitator. If so, the host should not also collect. [T2]

### EC4 -- Parking Tax at 18% [T2]

**Situation:** A parking garage in DC charges $30/day. A business rents monthly parking for employees at $300/month.

**Resolution:**
- Daily parking: $30 x 18% = $5.40 tax. [T1]
- Monthly parking: $300 x 18% = $54.00 tax. [T1]
- The 18% rate applies to all commercial parking and vehicle storage. [T1]
- Residential parking included in a lease may be exempt if it is part of the residential rental (not separately stated). [T2]
- **Flag for reviewer:** Distinguish between commercial/transient parking (18%) and residential parking bundled with a lease. [T2]

### EC5 -- Federal Government Employees and Diplomatic Exemptions [T2]

**Situation:** A foreign diplomat presents a diplomatic tax exemption card at a DC retailer.

**Resolution:**
- Certain diplomatic personnel are exempt from DC sales tax based on the level of their diplomatic card (issued by the US Department of State). [T1]
- The card color and markings indicate the scope of exemption (personal purchases, official purchases, or both). [T2]
- The retailer must record the diplomat's card number and retain documentation. [T2]
- Not all diplomatic personnel receive full exemption. [T2]
- **Flag for reviewer:** Verify the specific card type and associated exemption level with the State Department's Office of Foreign Missions. [T2]

---

### EC6 -- Catering Services in DC [T2]

**Situation:** A catering company provides food and services for a DC office event. The invoice includes $2,000 for food and $500 for staff/service charges.

**Resolution:**
- Food provided by a caterer is considered prepared food: 10% rate applies. [T1]
- Service charges that are mandatory (not voluntary tips) are generally included in the taxable amount. [T2]
- Voluntary gratuities/tips left by customers are NOT taxable. [T1]
- Tax base = $2,000 + $500 = $2,500 (if service charge is mandatory). Tax = $2,500 x 10% = $250. [T1]
- **Flag for reviewer:** Distinguish between mandatory service charges (taxable) and voluntary tips (not taxable). [T2]

### EC7 -- Software Plus Consulting Bundle [T2]

**Situation:** A technology firm sells a package including $5,000 SaaS subscription (taxable) and $3,000 exempt consulting services to a DC client.

**Resolution:**
- SaaS is taxable at 6%. Consulting is exempt. [T1]
- If separately stated on the invoice: SaaS tax = $5,000 x 6% = $300. Consulting = $0 tax. [T1]
- If bundled at a single price ($8,000): bundled transaction rules may apply, potentially making the entire amount taxable. [T2]
- **Flag for reviewer:** Always separately state taxable and exempt components. [T2]

---

## Test Suite

### Test 1 -- General Taxable Sale

**Input:** Seller in DC sells $500 of office furniture to a DC buyer. DC general rate = 6%.
**Expected output:** Sales tax = $500 x 6% = $30.00. Total = $530.00.

### Test 2 -- Restaurant Meal

**Input:** Customer dines at a DC restaurant. Bill = $100 (food and drink). DC restaurant rate = 10%.
**Expected output:** Sales tax = $100 x 10% = $10.00. Total = $110.00. (Tip is not taxable.)

### Test 3 -- Hotel Stay

**Input:** Guest stays at a DC hotel for 3 nights at $250/night. Hotel rate = 10.25%.
**Expected output:** Room charges = $750. Tax = $750 x 10.25% = $76.88. Total = $826.88.

### Test 4 -- Grocery Purchase (Mixed Items)

**Input:** Customer buys rice ($5, exempt food), soda ($3, soft drink at 8%), and candy bar ($2, general TPP at 6%).
**Expected output:** Rice: exempt. Soda tax = $3 x 8% = $0.24. Candy tax = $2 x 6% = $0.12. Total tax = $0.36. Total = $10.36.

### Test 5 -- Parking Tax

**Input:** Customer parks in a DC commercial garage for one day at $25. Parking rate = 18%.
**Expected output:** Tax = $25 x 18% = $4.50. Total = $29.50.

### Test 6 -- SaaS Subscription

**Input:** SaaS company charges a DC business $1,000/month for cloud software. DC taxes SaaS at 6%.
**Expected output:** Tax = $1,000 x 6% = $60.00. Total = $1,060.00.

---

### Test 7 -- Catering with Service Charge

**Input:** Caterer bills $3,000 for food + $600 mandatory service charge to DC office. Prepared food rate = 10%.
**Expected output:** Tax = ($3,000 + $600) x 10% = $360.00. Total = $3,960.00.

### Test 8 -- Diplomatic Exemption

**Input:** Foreign diplomat with full exemption card purchases $500 electronics at a DC store.
**Expected output:** Exempt (valid diplomatic card with full exemption). Tax = $0. Total = $500.00.

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
