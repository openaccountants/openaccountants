---
name: ohio-sales-tax
description: Use this skill whenever asked about Ohio sales and use tax, ODT filings, Ohio CAT, Ohio exemptions, Ohio nexus, or any request involving Ohio state sales and use tax compliance. Trigger on phrases like "Ohio sales tax", "OH sales tax", "ODT", "UST-1", "Ohio exemption certificate", "Ohio resale certificate", "Streamlined Sales Tax Ohio", or any request involving Ohio sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any Ohio sales tax work.
---

# Ohio Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Ohio, United States |
| Jurisdiction Code | US-OH |
| Tax Type | Sales and Use Tax (state + county) |
| Primary Legislation | Ohio Revised Code (ORC), Chapter 5739 (Sales Tax) and Chapter 5741 (Use Tax) |
| Key Statutes | ORC Sections 5739.01-5739.99; ORC Sections 5741.01-5741.99 |
| Tax Authority | Ohio Department of Taxation (ODT) |
| Filing Portal | https://tax.ohio.gov |
| Federal Framework Skill | us-sales-tax (read first for Wayfair, nexus overview, and multi-state context) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires Ohio CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| SST Membership | Yes -- Ohio is a full member of the Streamlined Sales Tax (SST) |
| Confidence Coverage | Tier 1: rate structure, basic taxability, filing mechanics, nexus thresholds, SST compliance. Tier 2: service taxability, SaaS/digital goods, CAT interaction. Tier 3: audit defense, complex bundled transactions, ODT rulings. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to a licensed tax professional and document the gap.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Ohio sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have an Ohio sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Ohio? | Drives taxability classification under Ohio law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Ohio? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Ohio local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Rate

The Ohio state sales and use tax rate is **5.75%**. [T1]

**Legislation:** ORC Section 5739.02(A)(1).

### 1.2 County Taxes

Ohio **counties** (not cities) impose additional sales taxes. There are no city or special district sales taxes -- only county permissive taxes.

- County rates range from **0.75% to 2.25%** on top of the state rate. [T1]
- Combined maximum: approximately **8.00%** (e.g., Cuyahoga County at 5.75% + 2.25% = 8.00%). [T1]

**Key combined rates (examples):**

| County | County Rate | Combined Rate |
|--------|-----------|---------------|
| Cuyahoga (Cleveland) | 2.25% | **8.00%** |
| Franklin (Columbus) | 1.75% | **7.50%** |
| Hamilton (Cincinnati) | 1.80% | **7.55%** (approximate) |
| Summit (Akron) | 1.50% | **7.25%** |
| Montgomery (Dayton) | 1.50% | **7.25%** |
| Lucas (Toledo) | 1.50% | **7.25%** |

**Legislation:** ORC Section 5739.021 et seq.

### 1.3 Sourcing [T1]

Ohio uses **origin-based** sourcing for intrastate sales:

- If both seller and buyer are in Ohio, the rate is based on the **seller's location** (county). [T1]
- For **remote** (out-of-state) sellers, **destination-based** sourcing applies (SST compliant). [T1]
- As an SST member, Ohio follows SST sourcing rules for remote sales. [T1]

**Legislation:** ORC Section 5739.033.

---

## Step 3: Return Form Structure
### 5.1 Filing Form

The primary return is **Form UST-1 (Universal Sales Tax Return)**. [T1]

Other forms:
- **UST-1-X** -- Amended return
- **UUT-1** -- Use Tax Return (for consumers)

### 5.2 Filing Frequency [T1]

| Frequency | Criteria | Due Date |
|-----------|----------|----------|
| Monthly | Tax liability > $600/month | 23rd of the following month |
| Semi-annual | Tax liability $600 or less/month | 23rd of the month following the semi-annual period |

**Semi-annual periods:**

| Period | Coverage | Due Date |
|--------|----------|----------|
| Period 1 | January 1 -- June 30 | July 23 |
| Period 2 | July 1 -- December 31 | January 23 |

**Legislation:** ORC Section 5739.12.

### 5.3 Vendor Discount [T1]

Ohio offers a **vendor discount** of **0.75%** of tax collected for timely filing and payment. ORC Section 5739.12(B). [T1]

- No cap on the discount amount. [T1]
- Only available if the return is filed AND payment is made on time. [T1]

### 5.4 Electronic Filing [T1]

- Electronic filing is available through the **Ohio Business Gateway** (https://gateway.ohio.gov). [T1]
- Required for certain large filers. [T1]

### 5.5 Penalties and Interest [T1]

| Penalty | Rate | Citation |
|---------|------|----------|
| Late filing | Greater of 10% of tax due or $50 | ORC Section 5739.13 |
| Late payment | Same | ORC Section 5739.13 |
| Fraud | 50% of deficiency | ORC Section 5739.13(C) |
| Interest | Federal short-term rate + 5% | ORC Section 5703.47 |

---

## Step 4: Deductibility / Exemptions
### 7.1 Ohio Exemption Certificates [T1]

- **Form STEC-B** -- Blanket Exemption Certificate (for ongoing purchases). [T1]
- **Form STEC-U** -- Unit Exemption Certificate (single transaction). [T1]
- Ohio accepts the **SST Certificate of Exemption** (Ohio is an SST member). [T1]
- Ohio accepts the **MTC Uniform Sales Tax Certificate**. [T1]
- Certificates must include the buyer's vendor license number and reason for exemption. [T1]

### 7.2 Construction Contract Exemption Certificate [T1]

- **Form STEC-CO** -- for contractors on exempt construction projects. [T1]

---


### 6.1 When Use Tax Applies

Use tax applies when:

- An Ohio purchaser acquires TPP, taxable services, or digital goods from a seller who did not collect Ohio tax. [T1]
- TPP is purchased tax-free and diverted to taxable use. [T1]
- TPP is brought into Ohio for use, storage, or consumption. [T1]

**Legislation:** ORC Chapter 5741.

### 6.2 Use Tax Rate [T1]

Use tax rate equals the combined state and county rate at the location of use. [T1]

### 6.3 Reporting Use Tax [T1]

- **Registered vendors:** Report on UST-1. [T1]
- **Individuals:** Report on Ohio IT-1040 (Schedule of Adjustments). [T1]
- **Businesses not registered:** File Form UUT-1. [T1]

### 6.4 Credit for Tax Paid to Other States [T1]

Ohio allows a credit for sales/use tax legally paid to another state. ORC Section 5741.02(C)(3). [T1]

---

## Step 5: Key Thresholds
### 4.1 Who Must Register

Any vendor making taxable sales in Ohio must obtain a **Vendor's License**. ORC Section 5739.17. [T1]

- The license must be renewed annually (by February 28). [T1]
- Fee: **$25** per location per year. [T1]

### 4.2 Economic Nexus Threshold [T1]

Ohio's economic nexus threshold:

- **$100,000** in gross receipts from sales into Ohio during the current or preceding calendar year, **OR** [T1]
- **200 or more transactions** in Ohio during the same period. [T1]
- Effective date: August 1, 2019. [T1]

**Legislation:** ORC Section 5741.01(I)(2).

### 4.3 Marketplace Facilitator Rules [T1]

Ohio requires marketplace facilitators to collect and remit sales tax:

- Effective January 1, 2020. [T1]
- Marketplace facilitators are treated as vendors. [T1]
- Marketplace sellers are relieved for facilitated sales. [T1]

**Legislation:** ORC Section 5739.01(Q); ORC Section 5741.01(R).

### 4.4 Commercial Activity Tax (CAT) [T2]

Ohio imposes a **Commercial Activity Tax (CAT)** on gross receipts:

- This is a **separate tax** from sales tax. [T1]
- Applies to all businesses with Ohio gross receipts over $150,000/year. [T1]
- Rate: 0.26% of gross receipts (over $1 million). [T1]
- The CAT replaced Ohio's corporate franchise tax and tangible personal property tax. [T1]
- CAT compliance is outside the scope of this skill -- escalate to [T3]. [T1]

**Legislation:** ORC Chapter 5751.

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- **NEVER** apply a clothing exemption in Ohio -- clothing is fully taxable. [T1]
- **NEVER** forget that Ohio's vendor license must be renewed annually ($25/location/year). [T1]
- **NEVER** treat grocery food as taxable -- grocery food is exempt (but candy, soft drinks, and dietary supplements are taxable). [T1]
- **NEVER** confuse the CAT with sales tax -- they are separate taxes with separate obligations. [T1]
- **NEVER** use destination-based sourcing for intrastate Ohio sales -- Ohio is origin-based for intrastate. [T1]
- **NEVER** forget the 0.75% vendor discount for timely filing -- it has no cap and applies to all timely returns. [T1]
- **NEVER** treat SaaS as nontaxable in Ohio -- SaaS is taxable as automatic data processing. [T1]
- **NEVER** refuse the SST Certificate in Ohio -- Ohio is an SST member and must accept SST certificates. [T1]
- **NEVER** assume landscaping and physical fitness services are exempt -- both are taxable in Ohio. [T1]
- **NEVER** apply the flour-based candy exception incorrectly -- items WITH flour are food (exempt), items WITHOUT flour (meeting other candy criteria) are candy (taxable). [T1]

---

## Edge Case Registry

### EC1 -- SST Compliance and Multi-State Registration [T1]

**Situation:** An out-of-state seller wants to register in Ohio and other SST member states simultaneously.

**Resolution:** Because Ohio is an SST member, the seller can register through the **SST Registration System** (SSTRS) at https://www.sstregister.org. This allows registration in all SST member states through a single application. Ohio will issue a vendor's license upon registration.

### EC2 -- Vendor License Renewal [T1]

**Situation:** A vendor forgets to renew the annual vendor's license by February 28.

**Resolution:** The vendor must renew immediately. Operating without a valid vendor's license is a violation of ORC Section 5739.17. Penalties may apply. The renewal fee is $25 per location per year.

### EC3 -- Candy Definition (SST Standard) [T1]

**Situation:** A store sells chocolate-covered pretzels and asks if they are "candy."

**Resolution:** Under SST definitions adopted by Ohio, "candy" means a preparation of sugar, honey, or other sweetener combined with chocolate, fruits, nuts, or other ingredients, that does NOT contain flour as an ingredient. Chocolate-covered pretzels contain flour (in the pretzel), so they are classified as FOOD (exempt), not candy (taxable). ORC Section 5739.01(AAAA).

### EC4 -- Data Processing Services vs. SaaS [T2]

**Situation:** A business purchases cloud-based data analytics services.

**Resolution:** Ohio taxes "automatic data processing and computer services" under ORC Section 5739.01(B)(3)(a). Cloud analytics likely falls under this category and is taxable. However, certain consulting and professional services that happen to use computers may not qualify as "automatic data processing." Flag for reviewer if the service is primarily analytical/consulting in nature with technology as incidental.

### EC5 -- Temporary Staffing [T1]

**Situation:** A company uses a temporary staffing agency for $8,000/month.

**Resolution:** Employment services and employment placement services are TAXABLE in Ohio. ORC Section 5739.01(B)(3)(j). Tax = $8,000 x combined rate (e.g., 7.50% in Columbus = $600/month).

### EC6 -- CAT vs. Sales Tax [T1]

**Situation:** Business owner asks about the total Ohio tax burden on a transaction.

**Resolution:** Ohio imposes BOTH sales tax (collected from the customer) AND the Commercial Activity Tax (CAT, imposed on the seller's gross receipts). They are separate taxes. A sale may be subject to both. The CAT is NOT in lieu of sales tax. Escalate CAT questions to [T3].

### EC7 -- Origin-Based Intrastate Anomaly [T1]

**Situation:** A Columbus-based seller ships goods to a customer in Cleveland (different county, different combined rate).

**Resolution:** For intrastate Ohio sales, origin-based sourcing applies. The Columbus seller charges the Franklin County rate (7.50%) even though Cleveland (Cuyahoga County) has a rate of 8.00%. The customer's county rate is irrelevant for intrastate sales from an Ohio-based seller.

### EC8 -- Physical Fitness Services [T1]

**Situation:** A gym charges monthly membership fees of $50.

**Resolution:** Physical fitness facility services are TAXABLE in Ohio. ORC Section 5739.01(B)(3)(k). Tax applies to the $50 monthly fee at the applicable combined rate.

### EC9 -- Digital Products [T1]

**Situation:** Consumer purchases a digital movie download for $14.99 from an Ohio retailer.

**Resolution:** Specified digital products (digital audio, video, and books) are TAXABLE in Ohio under ORC Section 5739.01(BBB). Tax applies at the combined rate at the buyer's location (destination-based for remote sellers).

### EC10 -- Landscaping and Lawn Care [T1]

**Situation:** A commercial property owner hires a landscaping company for $2,000/month.

**Resolution:** Landscaping and lawn care services are TAXABLE in Ohio. ORC Section 5739.01(B)(3)(h). Both commercial and residential landscaping are taxable. Tax = $2,000 x combined rate.

---

## Test Suite

### Test 1 -- Basic Taxable Sale in Columbus [T1]

**Input:** Retailer in Columbus (Franklin County) sells electronics for $800. Combined rate: 7.50%.
**Expected output:** Sales tax = $60.00. Total = $860.00.

### Test 2 -- Grocery Food Exempt [T1]

**Input:** Customer buys $150 of groceries (bread, milk, produce) at a Cleveland supermarket.
**Expected output:** Sales tax = $0. Grocery food exempt.

### Test 3 -- Candy Taxable [T1]

**Input:** Customer buys a $5 chocolate bar (no flour) at a Columbus store. Rate: 7.50%.
**Expected output:** Sales tax = $0.38 ($5 x 7.50%). Candy (no flour) is taxable.

### Test 4 -- Chocolate-Covered Pretzels (Food, Not Candy) [T1]

**Input:** Customer buys $5 bag of chocolate-covered pretzels (contains flour) at a Columbus store.
**Expected output:** Sales tax = $0. Item contains flour, classified as food (exempt), not candy.

### Test 5 -- SaaS Taxable [T1]

**Input:** Ohio business subscribes to a cloud-based CRM. $300/month. Business in Cuyahoga County (8.00%).
**Expected output:** Sales tax = $24.00/month. SaaS is taxable as automatic data processing service.

### Test 6 -- Economic Nexus -- Revenue [T1]

**Input:** Out-of-state seller has $120,000 in Ohio sales and 50 transactions in the past year.
**Expected output:** Seller HAS economic nexus (revenue exceeds $100,000 -- OR test).

### Test 7 -- Vendor Discount [T1]

**Input:** Vendor timely files and pays $20,000 in Ohio sales tax.
**Expected output:** Vendor discount = 0.75% of $20,000 = $150.00. Net remittance = $19,850.00.

### Test 8 -- Temporary Staffing [T1]

**Input:** Company pays $6,000/month for temporary staffing in Hamilton County (7.55%).
**Expected output:** Sales tax = $453.00 ($6,000 x 7.55%). Employment services are taxable.

### Test 9 -- Manufacturing Equipment Exempt [T1]

**Input:** Manufacturer purchases $75,000 production line equipment. Used primarily in manufacturing. Provides STEC-B.
**Expected output:** Sales tax = $0. Manufacturing equipment exempt.

### Test 10 -- Use Tax [T1]

**Input:** Cleveland business purchases $4,000 office furniture from a New Hampshire retailer. No tax collected. Cuyahoga County rate: 8.00%.
**Expected output:** Use tax = $320.00 ($4,000 x 8.00%). Report on UST-1 or IT-1040.

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
