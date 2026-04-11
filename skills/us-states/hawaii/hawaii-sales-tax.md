---
name: hawaii-sales-tax
description: Use this skill whenever asked about Hawaii General Excise Tax, Hawaii GET, Hawaii sales tax, Hawaii use tax, Hawaii DoTax filing, or Hawaii tax on services. Trigger on phrases like "Hawaii GET", "General Excise Tax", "HI sales tax", "HRS §237", "Hawaii DoTax", "Hawaii tax on services", or any request involving Hawaii GET compliance. Hawaii does NOT have a traditional sales tax -- it has a General Excise Tax imposed on the SELLER. ALWAYS load us-sales-tax first for federal context.
---

# Hawaii General Excise Tax (GET) Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Hawaii, United States |
| Jurisdiction Code | US-HI |
| Tax Type | General Excise Tax (GET) -- NOT a traditional sales tax |
| General Rate | 4.00% (4.5% on Oahu with county surcharge) |
| Wholesale Rate | 0.50% |
| Insurance Commissions Rate | 0.15% |
| Primary Statute | Hawaii Revised Statutes (HRS) Chapter 237 |
| Governing Agency | Department of Taxation (DoTax) |
| Portal | https://tax.hawaii.gov |
| SST Member | No |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: rates, basic taxability, filing mechanics. T2: service classification, pass-through to buyer, wholesale vs retail. T3: audit defense, complex multi-tier transactions, pyramiding analysis. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Hawaii sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Hawaii sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Hawaii? | Drives taxability classification under Hawaii law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Hawaii? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Hawaii local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 Fundamental Structure -- Tax on the Seller [T1]

Hawaii's General Excise Tax (GET) is fundamentally different from a traditional sales tax:

- **GET is imposed on the SELLER (business), not the buyer.** [T1]
- GET applies to the **gross income** of all business activity in Hawaii -- not just retail sales. [T1]
- GET applies to virtually **ALL transactions**, including services, rentals, commissions, and interest income. [T1]
- There is no legal requirement for sellers to pass GET on to the buyer (though most do). [T1]
- When GET is passed on to the buyer, it becomes part of gross income and is itself subject to GET (tax-on-tax / pyramiding). [T1]

**Statute:** HRS §237-13 (imposition of tax).

**Key difference from sales tax:** In a sales tax state, the seller collects tax from the buyer and remits it to the state. In Hawaii, the seller pays GET on its own gross income. The buyer is NOT legally liable for GET. [T1]

### 1.2 Rate Structure [T1]

| Activity | GET Rate | Effective Rate When Passed to Buyer |
|----------|----------|-------------------------------------|
| Retail sales | 4.00% | ~4.166% (to cover GET on the passed-through amount) |
| Wholesale sales (sale for resale) | 0.50% | ~0.5025% |
| Services | 4.00% | ~4.166% |
| Commissions | 4.00% | ~4.166% |
| Insurance commissions | 0.15% | ~0.15% |
| Manufacturing/producing | 0.50% | ~0.5025% |
| Subletting/subcontracting | 0.50% | ~0.5025% |
| Interest income | 0.50% | N/A |
| Rental income (real property) | 4.00% | ~4.166% |
| Transient accommodations | 4.00% + TAT | ~4.166% + TAT |

### 1.3 County Surcharge (Oahu) [T1]

- **Oahu (City & County of Honolulu):** An additional 0.50% county surcharge applies, bringing the total GET rate on Oahu to **4.50%** for retail activities. [T1]
- **Effective rate passed to buyer on Oahu:** ~4.712%. [T1]
- **Kauai County:** 0.50% surcharge (4.50% total). [T1]
- **Hawaii County (Big Island):** 0.50% surcharge (4.50% total). [T1]
- **Maui County:** 0.50% surcharge (effective dates may vary). [T2]

**Statute:** HRS §248-2.6 (county surcharge).

### 1.4 Pyramiding -- Tax on Tax [T1]

GET pyramids (cascades) at every level of the supply chain:

- A manufacturer pays 0.5% GET on wholesale sales.
- A wholesaler pays 0.5% GET on sales to retailers.
- A retailer pays 4% GET on sales to consumers.
- If the retailer passes the 4% GET to the consumer, the passed-through amount becomes additional gross income, subject to GET again.
- **Result:** The effective tax burden embedded in prices is higher than the nominal 4% rate. [T1]

This pyramiding effect is a fundamental structural feature of GET and is NOT a bug -- it is by design. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Services -- VERY BROADLY TAXABLE [T1]

**Hawaii taxes virtually ALL services under GET.** This is one of the broadest tax bases in the United States. [T1]

Taxable services include (non-exhaustive):
- Professional services: legal, accounting, consulting, engineering, architecture. [T1]
- Medical and healthcare services (though certain exemptions exist). [T2]
- Personal care: haircuts, spa services, fitness training. [T1]
- Repair and maintenance services. [T1]
- Cleaning and janitorial services. [T1]
- Information technology services, web design, software development. [T1]
- Transportation services. [T1]
- Financial advisory services. [T1]
- Construction services. [T1]
- Advertising and marketing services. [T1]

**Note:** Professionals moving from the mainland to Hawaii are often shocked that their services are subject to GET. This is a common source of non-compliance. [T2]

### 2.2 Grocery Food [T1]

- ALL food, including unprepared grocery food, is subject to GET at the **4% retail rate** (there is no food exemption). [T1]
- Prepared food: 4% GET. [T1]
- Hawaii is one of the few jurisdictions that taxes all food at the full rate. [T1]

### 2.3 Clothing [T1]

- Clothing is subject to GET at the standard 4% retail rate. No exemption. [T1]

### 2.4 Prescription Drugs and Medical [T2]

- Prescription drugs are subject to GET, but at the **reduced wholesale rate of 0.50%** when sold by a licensed pharmacy. HRS §237-24.3(2). [T2]
- Hospital and health care facility gross income may be subject to GET with certain exemptions and deductions. [T2]
- Amounts received by physicians under Medicare/Medicaid: certain exemptions may apply. [T3]

### 2.5 SaaS and Digital Goods [T2]

- **SaaS:** Taxable under GET. All services rendered in Hawaii are subject to GET, and SaaS is treated as a service. [T1]
- **Digital downloads:** Taxable. [T1]
- **Streaming services:** Taxable. [T1]
- **Custom software development:** Taxable as a service. [T1]

### 2.6 Real Property Rental [T1]

- Rental of real property is subject to GET at **4%** (plus county surcharge). [T1]
- Transient accommodations (less than 180 days) are subject to GET **plus** the Transient Accommodations Tax (TAT) of **10.25%** (rate subject to legislative changes). HRS Chapter 237D. [T1]
- Short-term vacation rentals (Airbnb, VRBO) are subject to both GET and TAT. [T1]

### 2.7 Exemptions -- Very Limited [T1]

GET exemptions are narrow compared to sales tax states:

- Federal government sales. HRS §237-25. [T1]
- Certain agricultural cooperative associations. [T2]
- Certain nonprofit organizations (limited). HRS §237-23. [T2]
- Amounts received under contract with the United States. [T1]
- Insurance proceeds. [T2]
- Wages and salaries (employee compensation is not subject to GET). [T1]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | Form G-45 (periodic); Form G-49 (annual reconciliation) |
| Filing Frequencies | Monthly (>$4,000/year liability); Quarterly ($1,000-$4,000); Semi-annually (<$1,000) |
| Due Date | 20th of the month following the reporting period |
| Annual Return (G-49) | Due April 20 of the following year |
| Portal | https://tax.hawaii.gov (Hawaii Tax Online) |
| E-filing | Available and encouraged |

**Important:** ALL GET taxpayers must file the annual Form G-49 reconciliation return, even if they file periodic returns throughout the year. [T1]

### 4.2 Vendor Discount [T1]

Hawaii does NOT offer a vendor discount for timely filing. [T1]

### 4.3 Penalties and Interest [T1]

- Late filing penalty: 5% of tax due per month, up to 25%. [T1]
- Late payment penalty: 20% of unpaid tax. [T1]
- Interest: statutory rate set annually by DoTax. [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for Hawaii. Key categories: [T1]

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
| Revenue Threshold | $100,000 in Hawaii gross income |
| Transaction Threshold | 200 transactions |
| Test | OR (either threshold triggers nexus) |
| Measurement Period | Current or prior calendar year |
| Effective Date | July 1, 2018 |

**Statute:** Act 41 (2018); HRS §237-2.

### 3.2 Physical Nexus [T1]

Standard physical nexus rules apply. Note that Hawaii's tourism-dependent economy means many mainland businesses may have physical nexus through trade shows, temporary employees, or equipment stationed in Hawaii. [T2]

### 3.3 Marketplace Facilitator [T1]

Hawaii requires marketplace facilitators to collect and remit GET on marketplace sales. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER refer to Hawaii's GET as a "sales tax." It is a General Excise Tax on the seller's gross income, not a sales tax on the buyer. [T1]
- NEVER assume services are exempt in Hawaii. GET applies to virtually ALL services, including professional services. [T1]
- NEVER assume grocery food is exempt in Hawaii. GET applies to all food at the full retail rate. [T1]
- NEVER assume a flat 4% rate across Hawaii. County surcharges (0.5%) apply on Oahu, Kauai, Hawaii County, and Maui. [T1]
- NEVER forget the pyramiding effect. When GET is passed to the buyer, the pass-through amount is itself subject to GET. The effective rate to make the seller whole is higher than the nominal rate. [T1]
- NEVER confuse GET rates: retail (4%), wholesale (0.5%), insurance commissions (0.15%). Misclassification causes under- or over-payment. [T1]
- NEVER forget the annual G-49 reconciliation return. It is required for ALL GET taxpayers, even those filing periodic returns. [T1]
- NEVER ignore TAT obligations for short-term rental income. GET and TAT are separate taxes that both apply. [T1]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Passing GET to the Customer (Visibly or Invisibly) [T2]

**Situation:** A retailer on Oahu charges $100 for an item. Can they add GET to the invoice?

**Resolution:**
- Legally, GET is a tax on the seller. There is NO requirement for the seller to pass it to the buyer. [T1]
- Most sellers DO pass GET to the buyer, either as a separate line item or built into the price. [T1]
- If the seller adds 4.5% (Oahu rate) as a visible surcharge, the surcharge itself becomes gross income subject to GET. [T1]
- The effective pass-through rate to make the seller whole is ~4.712% on Oahu (4.5% / (1 - 0.045)). [T1]
- Some sellers simply build GET into their prices and do not show a separate line item. [T2]
- **Flag for reviewer:** If the client is pricing products, ensure they understand that a simple 4.5% surcharge will NOT fully cover their GET liability due to pyramiding. [T2]

### EC2 -- Mainland Service Provider Performing Work in Hawaii [T2]

**Situation:** A California consulting firm sends consultants to work in Hawaii for 3 weeks. The engagement generates $50,000 in revenue.

**Resolution:**
- Services performed in Hawaii are subject to Hawaii GET at 4%. [T1]
- The consulting firm has physical nexus in Hawaii due to employee presence. [T1]
- The firm must register for GET, file returns, and pay GET on the $50,000 (or the portion attributable to Hawaii work). [T1]
- The firm may also owe Hawaii income tax on the income earned in Hawaii. [T2]
- **Flag for reviewer:** Many mainland service providers are unaware that Hawaii taxes ALL services. This is a common compliance gap. [T2]

### EC3 -- Wholesale vs. Retail Classification [T2]

**Situation:** A manufacturer sells products to both retailers (for resale) and directly to consumers. Different GET rates apply.

**Resolution:**
- Sales to retailers for resale: 0.5% wholesale rate. The retailer must provide a resale certificate (Form G-17). [T1]
- Direct sales to consumers: 4% retail rate. [T1]
- The manufacturer must segregate wholesale and retail income on Form G-45/G-49. [T1]
- Misclassifying retail sales as wholesale results in underpayment and penalties. [T1]
- **Flag for reviewer:** Verify that sales claimed at the 0.5% wholesale rate are supported by valid resale certificates. [T2]

### EC4 -- GET on Rental Income vs. TAT [T2]

**Situation:** A property owner rents a Waikiki condo for short-term vacation stays at $300/night.

**Resolution:**
- GET at 4.5% (Oahu) applies to the rental income. [T1]
- Transient Accommodations Tax (TAT) at 10.25% also applies (short-term rentals under 180 days). [T1]
- Oahu county TAT surcharge of 3% also applies (verify current surcharge rate). [T2]
- Total tax burden can exceed 17% on short-term rental income. [T1]
- The property owner must register for both GET and TAT, file separate returns, and remit both taxes. [T1]
- **Flag for reviewer:** The combined GET + TAT + county surcharge burden on short-term rentals is among the highest in the nation. Ensure the property owner is aware of all obligations. [T2]

---

### EC5 -- Subcontracting Rate [T2]

**Situation:** A general contractor hires a subcontractor for $100,000 of electrical work on a project.

**Resolution:**
- The subcontractor pays GET at the **0.5% subletting rate** on the amount received from the general contractor. [T1]
- The general contractor pays GET at the **4% retail rate** on the total contract price received from the property owner. [T1]
- Without the subletting deduction, double taxation would occur (full 4% at both levels). [T1]
- The subcontractor must provide documentation establishing the subletting relationship. [T2]
- **Flag for reviewer:** The subletting rate only applies when there is a documented contractor/subcontractor relationship. Independent vendor relationships do not qualify. [T2]

### EC6 -- Out-of-State Vendor Selling to Hawaii Customers [T2]

**Situation:** A mainland company ships $200,000 of goods to Hawaii customers annually. Does GET apply?

**Resolution:**
- If the company meets the $100,000 OR 200 transaction economic nexus threshold, it must register for GET. [T1]
- GET applies at the 4% retail rate on sales to Hawaii end consumers. [T1]
- The company should consider whether to absorb GET or pass it to customers. [T2]
- If passing GET, the effective rate to make the company whole is ~4.166% (4.5% with Oahu surcharge = ~4.712%). [T1]
- **Flag for reviewer:** Out-of-state vendors often fail to register for GET. This is a growing enforcement area. [T2]

---

## Test Suite

### Test 1 -- Basic Retail Sale on Oahu

**Input:** Retailer on Oahu sells a $1,000 item to a consumer. GET rate = 4.5% (4% state + 0.5% county). Retailer passes GET to buyer.
**Expected output:** Visible GET passed to buyer at effective rate ~4.712% = $47.12. Total charged to buyer = $1,047.12. GET due to state on gross income of $1,047.12 = $1,047.12 x 4.5% = $47.12.

### Test 2 -- Service Income Subject to GET

**Input:** Accounting firm on Maui provides $5,000 in consulting services to a Hawaii client. Maui GET rate = 4.5%.
**Expected output:** GET due = $5,000 x 4.5% = $225.00 (if firm absorbs the tax). If firm passes GET to client, gross income increases and GET is calculated on the higher amount.

### Test 3 -- Wholesale Sale

**Input:** Manufacturer sells $10,000 of goods to a retailer in Honolulu. Retailer provides valid Form G-17 resale certificate.
**Expected output:** Wholesale GET rate = 0.5% + 0.5% county surcharge = 1.0% (verify county surcharge applicability to wholesale). GET due = $10,000 x 0.5% = $50.00 (state) + county surcharge if applicable.

### Test 4 -- Grocery Food (No Exemption)

**Input:** Customer buys $150 of groceries at a supermarket on Oahu. GET rate = 4.5%.
**Expected output:** ALL grocery food is subject to GET. Tax passed to buyer at ~4.712% effective rate = $7.07. Total = $157.07.

### Test 5 -- Economic Nexus Determination

**Input:** Mainland SaaS company earned $120,000 in revenue from Hawaii customers and had 150 transactions in the prior year.
**Expected output:** Revenue ($120,000) exceeds $100,000 threshold. Nexus IS triggered. Company must register for GET and pay GET on Hawaii-sourced income.

---

### Test 6 -- Subcontracting Rate

**Input:** General contractor receives $500,000 from property owner. Pays $200,000 to subcontractor. Both on Oahu (4.5% retail, 0.5% subletting).
**Expected output:** Subcontractor GET on $200,000 at 0.5% = $1,000. General contractor GET on $500,000 at 4.5% = $22,500.

### Test 7 -- Professional Services to Mainland Client

**Input:** Hawaii accounting firm provides $10,000 in tax preparation services to a California client. Work performed in Hawaii. GET rate = 4%.
**Expected output:** Services performed in Hawaii are subject to GET regardless of client location. GET = $10,000 x 4% = $400.

### Test 8 -- Rental Income (Long-Term Residential)

**Input:** Landlord rents residential apartment on Oahu for $2,500/month (long-term, not transient). GET rate = 4.5%.
**Expected output:** Long-term rental income is subject to GET (no TAT since not transient). GET = $2,500 x 4.5% = $112.50.

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
