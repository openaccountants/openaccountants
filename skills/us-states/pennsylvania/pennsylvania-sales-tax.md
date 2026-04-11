---
name: pennsylvania-sales-tax
description: Use this skill whenever asked about Pennsylvania sales and use tax, PA DOR filings, Pennsylvania clothing exemption, Philadelphia sales tax, Allegheny County tax, Pennsylvania exemptions, Pennsylvania nexus, or any request involving Pennsylvania state sales and use tax compliance. Trigger on phrases like "Pennsylvania sales tax", "PA sales tax", "PA DOR", "PA-3", "Pennsylvania clothing exemption", "Philadelphia tax", "Pennsylvania resale certificate", or any request involving Pennsylvania sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any Pennsylvania sales tax work.
---

# Pennsylvania Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Pennsylvania, United States |
| Jurisdiction Code | US-PA |
| Tax Type | Sales and Use Tax (state + local) |
| Primary Legislation | Tax Reform Code of 1971, Article II (72 P.S. Section 7201 et seq.) |
| Key Statutes | 72 P.S. Sections 7201-7282 |
| Tax Authority | Pennsylvania Department of Revenue (PA DOR) |
| Filing Portal | https://www.revenue.pa.gov |
| Federal Framework Skill | us-sales-tax (read first for Wayfair, nexus overview, and multi-state context) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires Pennsylvania CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate structure, clothing exemption, basic taxability, filing mechanics, nexus thresholds. Tier 2: service taxability, SaaS/software, construction exemptions. Tier 3: audit defense, complex use tax, DOR private letter rulings. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to a licensed tax professional and document the gap.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Pennsylvania sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Pennsylvania sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Pennsylvania? | Drives taxability classification under Pennsylvania law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Pennsylvania? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Pennsylvania local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Rate

The Pennsylvania state sales and use tax rate is **6%**. [T1]

**Legislation:** 72 P.S. Section 7202.

### 1.2 Local Taxes

Only two jurisdictions impose additional local sales tax in Pennsylvania:

| Jurisdiction | Local Rate | Combined Rate |
|-------------|-----------|---------------|
| Philadelphia | 2% | **8%** |
| Allegheny County (Pittsburgh) | 1% | **7%** |
| All other PA jurisdictions | 0% | **6%** |

**This is notably simple compared to other states.** Outside Philadelphia and Allegheny County, the rate is a flat 6% statewide. [T1]

**Legislation:** 72 P.S. Section 7202; Philadelphia Code Section 19-2801; 16 P.S. Section 6120-C.

### 1.3 Sourcing [T1]

Pennsylvania uses **origin-based** sourcing for intrastate sales:

- If both seller and buyer are in Pennsylvania, the rate is based on the **seller's location** (relevant only for Philadelphia and Allegheny County local taxes). [T1]
- For **remote** (out-of-state) sellers, **destination-based** sourcing applies. [T1]

---

## Step 3: Return Form Structure
### 5.1 Filing Form

The primary return is **Form PA-3 (Sales, Use, and Hotel Occupancy Tax Return)**. [T1]

Other forms:
- **PA-3EZ** -- Simplified return (for small retailers)
- **PA-3USB** -- Return for use tax only

### 5.2 Filing Frequency [T1]

| Frequency | Criteria | Due Date |
|-----------|----------|----------|
| Monthly | Average monthly liability > $75 | 20th of the following month |
| Quarterly | Average monthly liability $75 or less | 20th of the month following the quarter |
| Semi-annual | Average monthly liability < $25 (optional) | 20th of the month following the semi-annual period |

**Quarterly due dates:**

| Quarter | Period | Due Date |
|---------|--------|----------|
| Q1 | January 1 -- March 31 | April 20 |
| Q2 | April 1 -- June 30 | July 20 |
| Q3 | July 1 -- September 30 | October 20 |
| Q4 | October 1 -- December 31 | January 20 |

**Legislation:** 72 P.S. Section 7217.

### 5.3 Electronic Filing [T1]

- Electronic filing is available and encouraged through **myPATH**. [T1]
- Required for certain large taxpayers. [T1]

### 5.4 Vendor Discount [T1]

Pennsylvania offers a vendor discount of **1%** of tax collected, up to **$25 per return**. 72 P.S. Section 7227. [T1]

### 5.5 Penalties and Interest [T1]

| Penalty | Rate | Citation |
|---------|------|----------|
| Late filing | 5% of unpaid tax per month (max 25%) | 72 P.S. Section 7259 |
| Late payment | Same as above | 72 P.S. Section 7259 |
| Fraud | 50% of deficiency | 72 P.S. Section 7259 |
| Interest | Rate set by DOR (floating) | 72 P.S. Section 7260 |

---

## Step 4: Deductibility / Exemptions
### 7.1 Pennsylvania Exemption Certificate [T1]

- **Form:** REV-1220 (Pennsylvania Exemption Certificate). [T1]
- Used for both resale and other exemptions (check appropriate box). [T1]
- Must include the buyer's sales tax license number (for resale). [T1]
- Pennsylvania also accepts the **MTC Uniform Sales Tax Certificate**. [T1]
- Pennsylvania does NOT accept the SST Certificate. [T1]
- Blanket certificates permitted for ongoing purchases. [T1]

---


### 6.1 When Use Tax Applies

Use tax applies when:

- A Pennsylvania purchaser acquires TPP or taxable services from an out-of-state seller who did not collect PA tax. [T1]
- TPP is purchased tax-free and diverted to taxable use. [T1]
- TPP is brought into Pennsylvania for use. [T1]

**Legislation:** 72 P.S. Section 7201(o); 72 P.S. Section 7202(b).

### 6.2 Use Tax Rate [T1]

Use tax rate equals the combined state and local rate at the location of use (6%, 7%, or 8%). [T1]

### 6.3 Credit for Tax Paid to Other States [T1]

Pennsylvania allows a credit against use tax for sales/use tax legally paid to another state. 72 P.S. Section 7210. [T1]

---

## Step 5: Key Thresholds
### 4.1 Who Must Register

Any person maintaining a place of business in Pennsylvania who makes taxable sales must obtain a **Sales Tax License** from PA DOR. 72 P.S. Section 7208. [T1]

### 4.2 Economic Nexus Threshold [T1]

Pennsylvania's economic nexus threshold:

- **$100,000** in gross sales into Pennsylvania in the prior or current calendar year. [T1]
- **No transaction count threshold** -- revenue only. [T1]
- Effective date: July 1, 2019 (for remote sellers not voluntarily collecting). [T1]

**Legislation:** 72 P.S. Section 7213.2; PA DOR Sales Tax Bulletin 2019-04.

### 4.3 Marketplace Facilitator Rules [T1]

Pennsylvania requires marketplace facilitators to collect and remit sales tax:

- Effective April 1, 2018 (one of the earliest). [T1]
- Marketplace facilitators are liable for tax on facilitated sales. [T1]
- Marketplace sellers are relieved of collection on marketplace sales. [T1]

**Legislation:** 72 P.S. Section 7213.2.

### 4.4 Registration Process [T1]

1. Apply online via PA DOR's **myPATH** portal (https://mypath.pa.gov). [T1]
2. Receive a **Sales Tax License** and license number. [T1]
3. Filing frequency assigned by PA DOR. [T1]
4. No fee for the license. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- **NEVER** charge sales tax on exempt everyday clothing in Pennsylvania. [T1]
- **NEVER** forget the fur clothing exception -- fur items over $100 are taxable despite the clothing exemption. [T1]
- **NEVER** assume Philadelphia and Pittsburgh rates are the same -- Philadelphia is 8%, Allegheny County is 7%. [T1]
- **NEVER** treat all software as taxable -- custom software is exempt; only canned software (including SaaS) is taxable. [T1]
- **NEVER** forget that help supply (temporary staffing) services are taxable -- this catches many businesses off guard. [T1]
- **NEVER** apply destination-based sourcing for intrastate PA sales -- PA is origin-based for intrastate. [T1]
- **NEVER** accept the SST Certificate in Pennsylvania -- PA is not an SST member. [T1]
- **NEVER** assume the manufacturing exemption covers office or administrative equipment -- only equipment directly used in production qualifies. [T1]
- **NEVER** overlook that grocery food is exempt but candy and soft drinks are taxable. [T1]
- **NEVER** assume OTC drugs are taxable -- Pennsylvania EXEMPTS OTC drugs. [T1]

---

## Edge Case Registry

### EC1 -- Clothing Accessories vs. Exempt Clothing [T1]

**Situation:** A retailer sells shirts (exempt), handbags (taxable), and jewelry (taxable).

**Resolution:** Shirts are everyday clothing and EXEMPT. Handbags and jewelry are accessories and TAXABLE at 6% (plus local). The classification depends on the item type, not the price. 72 P.S. Section 7204(26); 61 Pa. Code Section 53.1.

### EC2 -- Fur Clothing Exception [T1]

**Situation:** Customer purchases a $200 fur coat.

**Resolution:** Fur clothing priced over $100 is TAXABLE in Pennsylvania (exception to the clothing exemption). 72 P.S. Section 7204(2). A $90 fur item would be exempt under the clothing exemption.

### EC3 -- Philadelphia vs. Pittsburgh Rates [T1]

**Situation:** A PA-based remote seller ships to customers in Philadelphia, Pittsburgh, and State College.

**Resolution:** If the seller is out-of-state, destination-based sourcing applies: Philadelphia orders at 8%, Allegheny County (Pittsburgh) orders at 7%, State College (Centre County) orders at 6%. If the seller is in-state, origin-based sourcing applies -- use the seller's location rate.

### EC4 -- SaaS Taxability [T1]

**Situation:** A business subscribes to a cloud-based project management tool for $500/month.

**Resolution:** TAXABLE in Pennsylvania. PA DOR treats SaaS as a license of canned software. Tax at 6% (plus local). PA DOR Sales Tax Bulletin 2019-01. Tax = $30/month (at 6% state rate).

### EC5 -- Computer Services vs. Taxable Services [T2]

**Situation:** A company purchases computer programming services.

**Resolution:** Computer programming and web development services are generally NOT taxable in PA (professional services). However, if the deliverable is canned software, the software itself may be taxable. The distinction between custom programming (exempt) and canned software license (taxable) requires analysis. Flag for reviewer.

### EC6 -- Construction -- Real Estate Improvements [T2]

**Situation:** A contractor installs fixtures in a commercial building.

**Resolution:** In Pennsylvania, contractors are generally the consumers of materials they install into real property. The contractor pays sales tax on materials purchased. The contractor does NOT collect sales tax from the property owner on the installed price (it is a real estate improvement, not a sale of TPP). However, if the contractor retains ownership of the items (e.g., leased equipment), different rules apply. Flag for reviewer.

### EC7 -- Wrapping Supplies and Packaging [T1]

**Situation:** Retailer purchases wrapping paper, bags, and boxes used to package goods for sale to customers.

**Resolution:** Wrapping supplies, containers, and packaging used to deliver goods to customers are EXEMPT. 72 P.S. Section 7204(23). Supplies used for the retailer's own internal packaging or storage are TAXABLE.

### EC8 -- Farm Equipment Exemption [T1]

**Situation:** Farmer purchases a new tractor for use on the farm.

**Resolution:** Farm equipment used directly in farming operations is EXEMPT. 72 P.S. Section 7204(1). Includes tractors, harvesters, plows, and other agricultural machinery. Does NOT include vehicles used for personal transportation (even if used partly on the farm).

### EC9 -- Help Supply Services (Temporary Staffing) [T1]

**Situation:** A company hires temporary workers through a staffing agency. The agency charges $5,000/month.

**Resolution:** Help supply services (temporary staffing) are TAXABLE in Pennsylvania. 72 P.S. Section 7201(k)(17). Tax = $300/month at 6%. This is unusual -- most states do not tax temporary staffing services.

### EC10 -- Vendor Located in Philadelphia Selling Statewide [T1]

**Situation:** A retailer located in Philadelphia sells goods in-store and ships to customers across Pennsylvania.

**Resolution:** In-store sales are taxed at 8% (Philadelphia rate, origin-based). For shipped orders within PA, origin-based sourcing applies, so the Philadelphia 8% rate applies to all intrastate shipments from the Philadelphia location. For out-of-state customers, no PA tax (interstate commerce exemption).

---

## Test Suite

### Test 1 -- Exempt Clothing Sale [T1]

**Input:** Customer buys a $75 shirt at a retailer in State College, PA.
**Expected output:** Sales tax = $0. Clothing is exempt in Pennsylvania.

### Test 2 -- Taxable Fur Clothing [T1]

**Input:** Customer buys a $500 fur coat at a Philadelphia store.
**Expected output:** Sales tax = $40.00 ($500 x 8%). Fur clothing over $100 is taxable. Philadelphia rate applies.

### Test 3 -- Grocery Food Exempt [T1]

**Input:** Customer buys $200 of groceries (bread, meat, produce) in Pittsburgh (Allegheny County).
**Expected output:** Sales tax = $0. Grocery food is exempt.

### Test 4 -- SaaS Subscription [T1]

**Input:** PA business subscribes to cloud-based accounting software. $100/month. Business in Lancaster (6% rate).
**Expected output:** Sales tax = $6.00/month. SaaS is taxable in PA as canned software.

### Test 5 -- Economic Nexus [T1]

**Input:** Out-of-state seller has $120,000 in gross PA sales this calendar year. No physical presence.
**Expected output:** Exceeds $100,000 threshold. Must register and collect PA sales tax.

### Test 6 -- Temporary Staffing Service [T1]

**Input:** Company pays $10,000/month for temporary staffing services. Located outside Philadelphia/Allegheny.
**Expected output:** Sales tax = $600.00/month ($10,000 x 6%). Help supply services are taxable.

### Test 7 -- Manufacturing Equipment [T1]

**Input:** Manufacturer purchases $50,000 production machine used directly in manufacturing. Provides REV-1220 with manufacturing exemption.
**Expected output:** Sales tax = $0. Manufacturing equipment exempt under 72 P.S. Section 7201(k)(8).

### Test 8 -- Resale Certificate [T1]

**Input:** Retailer purchases $15,000 inventory from a PA wholesaler. Provides valid REV-1220 marked for resale.
**Expected output:** No sales tax charged. Retailer collects tax at resale.

### Test 9 -- Use Tax [T1]

**Input:** Philadelphia business purchases $3,000 of taxable office equipment from a Delaware retailer (no sales tax). No tax collected.
**Expected output:** Use tax = $240.00 ($3,000 x 8%). Report on PA-3.

### Test 10 -- Vendor Discount [T1]

**Input:** Retailer files PA-3 on time with $2,500 in tax collected.
**Expected output:** Vendor discount = 1% of $2,500 = $25.00 (at cap). Net remittance = $2,475.00.

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
