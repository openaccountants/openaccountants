---
name: indiana-sales-tax
description: Use this skill whenever asked about Indiana sales tax, Indiana use tax, Indiana sales tax nexus, Indiana sales tax returns, Indiana exemption certificates, taxability of goods or services in Indiana, or any request involving Indiana state-level consumption taxes. Trigger on phrases like "Indiana sales tax", "IN sales tax", "Indiana use tax", "Indiana nexus", "IC 6-2.5", "Indiana DOR sales tax", "ST-103", or any request involving Indiana sales and use tax filing, classification, or compliance. Indiana has one of the SIMPLEST sales tax structures in the US: 7% flat with no local sales taxes. ALWAYS read the parent us-sales-tax skill first for federal context.
---

# Indiana Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Indiana, United States |
| Jurisdiction Code | US-IN |
| Tax Type | Sales and Use Tax |
| State Tax Rate | 7% (flat -- no local sales tax) |
| Maximum Combined Rate | 7% (no local component) |
| Primary Legal Framework | Indiana Code (IC) Title 6, Article 2.5 |
| Key Statute | IC 6-2.5-2-1 (Imposition of sales tax) |
| Governing Body | Indiana Department of Revenue (IDOR) |
| Filing Portal | INTIME (Indiana Taxpayer Information Management Engine) -- https://intime.dor.in.gov |
| Economic Nexus Effective Date | October 1, 2018 |
| SST Member | Yes (full member) |
| Primary Return | Form ST-103 |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate lookups, basic nexus, standard taxability. Tier 2: SaaS classification, service taxability, manufacturing exemptions. Tier 3: audit defense, penalty abatement, complex bundled transactions. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Indiana sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have an Indiana sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Indiana? | Drives taxability classification under Indiana law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Indiana? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Indiana local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Rate

Indiana imposes a **flat 7% state sales tax** on the retail sale of tangible personal property and certain services. There are **no local sales taxes** in Indiana.

**This makes Indiana one of the simplest states for sales tax compliance.** The rate is always 7%, regardless of location within the state. [T1]

**Statutory authority:** IC 6-2.5-2-1.

### 1.2 No Local Taxes

Indiana does **not** permit local jurisdictions to levy sales taxes. The 7% rate is uniform statewide. The Indiana Constitution restricts sales tax authority to the state. [T1]

**Note:** Indiana does have local **income taxes** (county option), but no local sales taxes. Do not confuse the two. [T1]

### 1.3 Sourcing Rules [T1]

Indiana follows **Streamlined Sales Tax (SST)** sourcing rules:

- **Shipped/delivered goods:** Destination-based (ship-to address). [T1]
- **Over-the-counter (walk-in):** Seller's location. [T1]
- **Digital goods:** Buyer's address. [T1]
- **Services on TPP:** Location where the benefit is received or where the TPP is delivered after service. [T1]

Since there are no local rate variations in Indiana, the sourcing determination only affects whether the sale is an Indiana sale (7%) or sourced to another state. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 General Rule

Indiana sales tax applies to the retail sale of tangible personal property, certain services, and certain digital products. IC 6-2.5-2-1.

### 2.2 Taxability Matrix

| Item Category | Taxable? | Rate | Authority | Tier |
|---------------|----------|------|-----------|------|
| General tangible personal property | Yes | 7% | IC 6-2.5-2-1 | [T1] |
| Grocery food (food for home consumption) | **Exempt** | 0% | IC 6-2.5-5-20 | [T1] |
| Prepared food (restaurant meals) | Yes | 7% | IC 6-2.5-1-20 | [T1] |
| Clothing and footwear | Yes | 7% | No exemption | [T1] |
| Prescription drugs | Exempt | 0% | IC 6-2.5-5-19 | [T1] |
| Over-the-counter drugs | Exempt | 0% | IC 6-2.5-5-19.5 | [T1] |
| Durable medical equipment | Exempt (with prescription) | 0% | IC 6-2.5-5-18 | [T1] |
| Prosthetic devices | Exempt | 0% | IC 6-2.5-5-18 | [T1] |
| Motor vehicles | Yes | 7% | IC 6-2.5-2-1 | [T1] |
| Gasoline and motor fuel | Exempt from sales tax (motor fuel tax) | N/A | IC 6-2.5-5-22 | [T1] |
| Utilities (residential -- electricity, gas, water) | Exempt | 0% | IC 6-2.5-5-23 | [T1] |
| Utilities (commercial/industrial) | Yes | 7% | IC 6-2.5-2-1 | [T1] |
| Manufacturing equipment (direct production) | Exempt | 0% | IC 6-2.5-5-3 | [T2] |
| Raw materials (incorporated into product for sale) | Exempt | 0% | IC 6-2.5-5-5.1 | [T1] |
| Agricultural supplies and equipment | Exempt | 0% | IC 6-2.5-5-1 to 5-2 | [T1] |
| Software -- canned (tangible medium) | Yes | 7% | IC 6-2.5-1-27 | [T1] |
| Software -- canned (electronic delivery) | Yes | 7% | IC 6-2.5-1-27; Sales Tax Info Bulletin 8 | [T1] |
| Software -- custom | Yes | 7% | IC 6-2.5-1-27 (as prewritten software) | [T2] |
| SaaS (Software as a Service) | **Taxable** | 7% | IDOR Sales Tax Info Bulletin 8; IC 6-2.5-4-16.4 | [T2] |
| Digital goods (e-books, music, video) | Yes | 7% | IC 6-2.5-4-16.4 | [T1] |
| Data processing services | Not taxable | 0% | Not enumerated | [T2] |
| Newspapers (printed) | Exempt | 0% | IC 6-2.5-5-23.5 | [T1] |

### 2.3 Grocery Food Exemption [T1]

Indiana fully exempts **food and food ingredients for human consumption** from sales tax:

- The exemption follows the SST definition of food (Indiana is a full SST member). [T1]
- **Candy** is taxable (excluded from food definition under SST). [T1]
- **Soft drinks** are taxable (excluded from food definition under SST). [T1]
- **Dietary supplements** are taxable. [T1]
- **Prepared food** is taxable. [T1]
- Food sold through vending machines: taxable if heated or prepared. [T2]

**Authority:** IC 6-2.5-5-20.

### 2.4 SaaS Taxability -- Indiana Position [T2]

Indiana **taxes SaaS** as a taxable digital product:

- Effective July 1, 2008, Indiana expanded its sales tax to cover "specified digital products." [T1]
- SaaS is treated as access to prewritten computer software and is taxable. [T2]
- The tax applies whether the software is accessed via a browser, app, or other means. [T2]
- **IaaS** and **PaaS** may also be taxable depending on the specific service. [T3]

**Authority:** IC 6-2.5-4-16.4; IDOR Sales Tax Information Bulletin 8.

### 2.5 Services Taxability [T2]

Indiana taxes certain enumerated services:

| Service | Taxable? | Authority |
|---------|----------|-----------|
| Telecommunications | Yes | IC 6-2.5-4-6 |
| Cable/satellite TV | Yes | IC 6-2.5-4-6 |
| Repair and maintenance of TPP | Parts: Yes; Labor: No (if separately stated) | IC 6-2.5-4-1 |
| Hotel/lodging | Yes (plus county innkeeper's tax) | IC 6-2.5-4-4 |
| Laundry/dry cleaning | Yes | IC 6-2.5-4-2 |
| Professional services (legal, accounting) | No | Not enumerated |
| Personal services (haircuts, spa) | No | Not enumerated |
| Construction/real property | No (materials taxable at purchase) | IDOR guidance |
| Transportation/freight | Exempt (if separately stated) | IC 6-2.5-5-10 |

---

## Step 3: Return Form Structure
### 3.1 Registration

All sellers with nexus must register with IDOR through INTIME. No fee for registration. The registration number is called a **Registered Retail Merchant Certificate (RRMC)** number.

**Authority:** IC 6-2.5-8-1.

### 3.2 Filing Frequency

| Monthly Tax Liability | Filing Frequency | Due Date |
|-----------------------|------------------|----------|
| Over $1,000 per month | Monthly | 20th of the following month (or 30th for e-filers) |
| $75 -- $1,000 per month | Monthly | 20th of the following month |
| Under $75 per month | Annual | January 31 |
| New registrants | Monthly (default) | 20th of the following month |

**Note:** Quarterly filing may be available for certain filers. IDOR assigns frequency. [T1]

### 3.3 Returns and Payment

- **Form ST-103** (Indiana Sales Tax Return) is the primary return. [T1]
- Electronic filing through INTIME is required for all filers. [T1]
- Payment is due on the same date as the return. [T1]

### 3.4 Vendor Collection Allowance

Indiana provides a **collection allowance** for timely filing:

- **0.73%** of the state sales tax collected. [T1]
- No maximum cap per period. [T1]
- Available only for timely filing and payment. [T1]

**Authority:** IC 6-2.5-6-10.

### 3.5 Penalties and Interest

| Violation | Penalty | Authority |
|-----------|---------|-----------|
| Late filing | 10% of tax due or $5, whichever is greater | IC 6-8.1-10-2.1 |
| Late payment | 10% of tax due or $5, whichever is greater | IC 6-8.1-10-2.1 |
| Failure to file | Estimated assessment + penalties | IC 6-8.1-5-1 |
| Negligence | 10% of deficiency | IC 6-8.1-10-2.1(b) |
| Fraud | 100% of deficiency | IC 6-8.1-10-4 |
| Interest | Statutory rate (adjusted annually, typically ~6-8%) | IC 6-8.1-10-1 |

---

## Step 4: Deductibility / Exemptions
### 5.1 Indiana Exemption Certificates

| Certificate | Use Case | Authority |
|-------------|----------|-----------|
| **Form ST-105** (General Sales Tax Exemption Certificate) | Resale, exempt organizations, manufacturing, agricultural | IC 6-2.5-8-8 |
| **Form ST-105GP** | Government entity purchases | IDOR |
| **SSTCE** (Streamlined certificate) | Multi-state purchases (Indiana is SST member) | SST Agreement |

### 5.2 Requirements [T1]

Valid certificates must include:

1. Purchaser's name, address, and signature. [T1]
2. Indiana RRMC number (for resale). [T1]
3. Reason for exemption. [T1]
4. Description of property. [T1]
5. Date. [T1]

### 5.3 Good Faith and Retention [T2]

Good faith acceptance protects sellers. Blanket certificates accepted for ongoing relationships. Certificates must be retained for **3 years** from the date of the last transaction. [T1]

---


### 6.1 When Use Tax Applies

Indiana use tax applies when sales tax was not collected on items used, stored, or consumed in Indiana. [T1]

### 6.2 Use Tax Rate

7%, identical to the sales tax rate. [T1]

### 6.3 Use Tax Reporting

- **Businesses:** Report on Form ST-103. [T1]
- **Individuals:** Report on Indiana income tax return (Form IT-40), Schedule 5. [T1]

---

## Step 5: Key Thresholds
### 4.1 Physical Nexus

Standard physical nexus principles apply. [T1]

### 4.2 Economic Nexus [T1]

Indiana enacted economic nexus effective **October 1, 2018**.

| Threshold | Value | Measurement Period |
|-----------|-------|--------------------|
| Revenue | **$100,000** in gross sales into Indiana | Previous or current calendar year |
| Transactions | **200 transactions** into Indiana | Previous or current calendar year |
| Test | **OR** -- either threshold triggers nexus | |

**Authority:** IC 6-2.5-2-1(c).

### 4.3 Marketplace Facilitator Rules [T1]

Effective **July 1, 2019**:

- Marketplace facilitators meeting the nexus threshold must collect and remit. [T1]
- Marketplace sellers relieved for facilitated sales. [T1]

**Authority:** IC 6-2.5-4-18.

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
1. **NEVER** advise that Indiana has local sales taxes (it does not -- 7% flat statewide). [T1]
2. **NEVER** advise that grocery food is taxable in Indiana (it is exempt). [T1]
3. **NEVER** advise that SaaS is not taxable in Indiana (it is taxable). [T1]
4. **NEVER** calculate a rate other than 7% for Indiana sales tax. [T1]
5. **NEVER** confuse Indiana's local income taxes (county option) with local sales taxes (which do not exist). [T1]
6. **NEVER** ignore the SST membership when advising on multi-state compliance (Indiana is a full SST member). [T1]
7. **NEVER** apply origin-based sourcing for shipped goods in Indiana (SST requires destination-based). [T1]
8. **NEVER** advise that custom software is exempt in Indiana (it is generally taxable as prewritten software). [T2]
9. **NEVER** forget the candy/soft drink taxability when advising on grocery food exemptions. [T1]
10. **NEVER** direct a filer to use paper returns -- Indiana requires electronic filing through INTIME. [T1]

---

## Edge Case Registry

### 7.1 Indiana's Simplicity Advantage [T1]

Indiana's 7% flat rate with no local taxes makes it one of the simplest states for compliance:

- No need for rate lookup tools or address-based rate determination within Indiana. [T1]
- One return covers all Indiana obligations (no local filings). [T1]
- SST membership further simplifies multi-state compliance. [T1]

### 7.2 Manufacturing Exemptions [T2]

Indiana provides a broad manufacturing exemption:

- **Direct production:** Equipment and materials used directly in the manufacturing process are exempt. [T2]
- The exemption does not extend to equipment used in pre-production (R&D, testing) or post-production (storage, shipping) unless specifically provided. [T2]
- **30% threshold rule:** If equipment is used at least 50% in production, the entire purchase may be exempt. [T2]

**Authority:** IC 6-2.5-5-3.

### 7.3 Construction and Real Property [T2]

- Contractors pay tax on materials at purchase. [T1]
- Contractors do NOT collect sales tax on real property improvements. [T1]
- Temporary materials (scaffolding, forms) are taxable. [T2]
- The distinction between real property improvement and TPP installation can be fact-specific. [T3]

### 7.4 Trade-In Allowances [T1]

Indiana allows trade-in credits to reduce the taxable base:

- The fair market value of the trade-in reduces the sales price subject to tax. [T1]
- Applies most commonly to motor vehicles. [T1]
- The trade-in must be of "like kind" (same general type of property). [T1]

**Authority:** IC 6-2.5-1-5.

### 7.5 Food Prepared by Grocers [T2]

The distinction between exempt grocery food and taxable prepared food can be nuanced:

- Food heated by the seller: taxable. [T1]
- Two or more food ingredients mixed by the seller for sale as a single item: taxable (with exceptions for bakery items, deli salads, etc.). [T2]
- Food sold with utensils provided: taxable. [T1]
- Whole rotisserie chicken from the deli: taxable (heated). [T1]
- Unheated deli sandwiches: taxable (two or more ingredients combined). [T2]

### 7.6 Leases and Rentals [T1]

- Leases of TPP are taxable at 7%. [T1]
- Tax is due on each lease payment. [T1]
- An option to purchase at end of lease: purchase price is taxable. [T1]

### 7.7 Motor Vehicle Sales [T1]

- Motor vehicles are taxable at 7%. [T1]
- Tax is paid at the BMV (Bureau of Motor Vehicles) at registration, not at the dealer. [T1]
- Trade-in values reduce the taxable base. [T1]
- Gifts between immediate family members: not taxable. [T1]

---

## Test Suite

### Test 1: Basic Rate Calculation [T1]

**Question:** A retailer in Indianapolis sells a $1,200 television. What is the sales tax?

**Expected Answer:** $1,200 x 7% = $84.00. No local tax applies.

### Test 2: Grocery Food Exemption [T1]

**Question:** A grocery store sells $100 in bread and produce, $15 in candy, and $10 in soft drinks. What tax is due?

**Expected Answer:** Bread/produce: exempt ($0). Candy: $15 x 7% = $1.05. Soft drinks: $10 x 7% = $0.70. Total tax: $1.75.

### Test 3: SaaS Taxability [T2]

**Question:** An Indiana company subscribes to a $800/month SaaS accounting platform. What Indiana sales tax is due?

**Expected Answer:** $800 x 7% = $56.00 per month. SaaS is taxable in Indiana.

### Test 4: Economic Nexus [T1]

**Question:** An out-of-state seller made $60,000 in sales and 210 transactions in Indiana. Does the seller have nexus?

**Expected Answer:** Yes. The 200-transaction threshold was exceeded (OR test).

### Test 5: Simplicity [T1]

**Question:** How many different sales tax rates exist within Indiana?

**Expected Answer:** One: 7%. Indiana has a flat statewide rate with no local sales taxes.

### Test 6: Manufacturing Exemption [T2]

**Question:** A manufacturer buys a $200,000 CNC machine used 80% in direct production and 20% in prototype testing. Is it exempt?

**Expected Answer:** Likely exempt, as the machine is used more than 50% in direct production. However, this requires careful analysis of Indiana's manufacturing exemption standards. A licensed professional should confirm the exemption eligibility.

### Test 7: Motor Vehicle [T1]

**Question:** A customer trades in a car worth $8,000 toward a new $35,000 vehicle in Indiana. What sales tax is due?

**Expected Answer:** Taxable base: $35,000 - $8,000 (trade-in) = $27,000. Tax: $27,000 x 7% = $1,890. Tax is paid at the BMV.

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
