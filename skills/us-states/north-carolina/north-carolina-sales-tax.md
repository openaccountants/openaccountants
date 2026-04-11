---
name: north-carolina-sales-tax
description: Use this skill whenever asked about North Carolina sales tax, North Carolina use tax, NC sales tax nexus, NC sales tax returns, NC exemption certificates, taxability of goods or services in North Carolina, or any request involving North Carolina state-level consumption taxes. Trigger on phrases like "North Carolina sales tax", "NC sales tax", "NC use tax", "NC nexus", "N.C.G.S. 105-164", "NC DOR sales tax", or any request involving North Carolina sales and use tax filing, classification, or compliance. ALWAYS read the parent us-sales-tax skill first for federal context, then layer this North Carolina-specific skill on top.
---

# North Carolina Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | North Carolina, United States |
| Jurisdiction Code | US-NC |
| Tax Type | Sales and Use Tax |
| State Tax Rate | 4.75% |
| Maximum Combined Rate | 7.5% (4.75% state + up to 2.75% local) |
| Primary Legal Framework | North Carolina General Statutes (N.C.G.S.) Chapter 105, Article 5 (Section 105-164 et seq.) |
| Governing Body | North Carolina Department of Revenue (NCDOR) |
| Filing Portal | NCDOR Online Filing -- https://www.ncdor.gov |
| Economic Nexus Effective Date | November 1, 2018 |
| SST Member | Yes (full member) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate lookups, basic nexus, standard taxability. Tier 2: digital property classification, service taxability, repair/installation. Tier 3: audit defense, penalty abatement, complex bundled transactions. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any North Carolina sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a North Carolina sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in North Carolina? | Drives taxability classification under North Carolina law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in North Carolina? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple North Carolina local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Rate

North Carolina imposes a **4.75% state sales and use tax** on the retail sale, lease, or rental of tangible personal property, certain digital property, and certain services.

**Statutory authority:** N.C.G.S. Section 105-164.4(a).

### 1.2 Local Rates

Counties in North Carolina levy additional local sales taxes. All 100 counties levy at least a 2% local rate, with some authorized for up to 2.75%:

| Tax Component | Rate | Authority |
|---------------|------|-----------|
| State sales tax | 4.75% | N.C.G.S. Section 105-164.4 |
| County Article 39 (all counties) | 1% | N.C.G.S. Section 105-468 |
| County Article 40 (all counties) | 0.5% | N.C.G.S. Section 105-469 |
| County Article 42 (most counties) | 0.5% | N.C.G.S. Section 105-535 |
| County Article 43 (some counties) | 0.25% | N.C.G.S. Section 105-537 |
| County transit tax (select counties) | 0.5% | N.C.G.S. Section 105-504 |

**Most common combined rate:** 4.75% state + 2.0% local = **6.75%**. [T1]
**Maximum combined rate:** 4.75% state + 2.75% local = **7.5%** (in counties with all authorized levies). [T1]

**Counties with the highest combined rates (7.5%):** Mecklenburg (Charlotte), Durham, Orange, and others with the transit tax. [T1]

### 1.3 Food Rate -- Special Reduced Rate [T1]

North Carolina imposes a **reduced rate** on certain food items:

- **2% state rate** (reduced from the standard 4.75%) applies to qualifying food that is NOT prepared food. [T1]
- **Local taxes** still apply to food, so the total rate on food = 2% + local (typically 2.0-2.75%) = **4.0-4.75%**. [T1]

**Authority:** N.C.G.S. Section 105-164.13B.

### 1.4 Sourcing Rules [T1]

North Carolina is a **destination-based** sourcing state, consistent with SST:

- **Shipped/delivered goods:** Destination (ship-to address). [T1]
- **Over-the-counter (walk-in):** Seller's location. [T1]
- **Digital goods:** Buyer's address. [T1]
- **Services:** Where the benefit is received. [T2]

---

## Step 2: Transaction Classification Rules
### 2.1 General Rule

North Carolina taxes the retail sale of tangible personal property, certain digital property, and certain services. N.C.G.S. Section 105-164.4.

### 2.2 Taxability Matrix

| Item Category | Taxable? | Rate | Authority | Tier |
|---------------|----------|------|-----------|------|
| General tangible personal property | Yes | Full rate | N.C.G.S. Section 105-164.4 | [T1] |
| Grocery food (food for home consumption) | **Reduced 2% state** (+ local) | 2% + local | N.C.G.S. Section 105-164.13B | [T1] |
| Prepared food (restaurant meals) | Yes | Full rate | N.C.G.S. Section 105-164.4 | [T1] |
| Clothing and footwear | Yes | Full rate | No exemption | [T1] |
| Prescription drugs | Exempt | 0% | N.C.G.S. Section 105-164.13(12) | [T1] |
| Over-the-counter drugs | Exempt | 0% | N.C.G.S. Section 105-164.13(12a) | [T1] |
| Durable medical equipment | Exempt (with prescription) | 0% | N.C.G.S. Section 105-164.13(12) | [T1] |
| Motor vehicles | Yes (but tax collected by DMV at registration) | 3% (capped at $2,000 per article) | N.C.G.S. Section 105-164.4(a)(4a) | [T1] |
| Gasoline and motor fuel | Exempt from sales tax (separate motor fuel tax) | N/A | N.C.G.S. Section 105-164.13(11) | [T1] |
| Utilities (electricity, piped natural gas) | Yes | Full rate | N.C.G.S. Section 105-164.4 | [T1] |
| Industrial machinery and equipment | Exempt (qualifying manufacturers) | 0% | N.C.G.S. Section 105-164.13(5e) | [T2] |
| Agricultural supplies | Exempt | 0% | N.C.G.S. Section 105-164.13(4a) | [T1] |
| Software -- canned (tangible medium) | Yes | Full rate | N.C.G.S. Section 105-164.4 | [T1] |
| Software -- canned (electronic delivery) | Yes | Full rate | Treated as digital property | [T1] |
| Software -- custom | Yes | Full rate | N.C.G.S. Section 105-164.4(a)(6b) | [T2] |
| SaaS (Software as a Service) | **Taxable** | Full rate | N.C.G.S. Section 105-164.4(a)(6b) | [T2] |
| Digital property (e-books, music, video) | **Taxable** | Full rate | N.C.G.S. Section 105-164.4(a)(6b) | [T1] |
| Data processing services | Not taxable | 0% | Not enumerated as taxable | [T2] |
| Newspapers (print, general circulation) | Exempt | 0% | N.C.G.S. Section 105-164.13(30) | [T1] |

### 2.3 Digital Property -- North Carolina's Broad Approach [T2]

North Carolina taxes **digital property** broadly, which is significant:

- "Digital property" is defined as digital audio works, digital audiovisual works, digital books, and other digital property delivered or accessed electronically. [T1]
- This includes downloaded or streamed music, movies, e-books, and digital images. [T1]
- **SaaS** falls under the "other digital property" category and is taxable. [T2]
- **Custom software** is also taxable in NC, unlike many states. [T2]
- Digital property is sourced to the buyer's location (destination-based). [T1]

**Authority:** N.C.G.S. Section 105-164.3(8c); Section 105-164.4(a)(6b).

### 2.4 Services Taxability [T2]

North Carolina taxes certain specifically enumerated services:

| Service | Taxable? | Authority |
|---------|----------|-----------|
| Repair, maintenance, and installation (TPP) | Yes | N.C.G.S. Section 105-164.4(a)(16) |
| Telecommunications services | Yes | N.C.G.S. Section 105-164.4(a)(4c) |
| Video programming (cable, satellite, streaming) | Yes | N.C.G.S. Section 105-164.4(a)(4c) |
| Hotel/lodging | Yes (plus local occupancy tax) | N.C.G.S. Section 105-164.4(a)(3) |
| Laundry and dry cleaning | Yes | N.C.G.S. Section 105-164.4(a)(15) |
| Electricity service | Yes | N.C.G.S. Section 105-164.4(a)(4b) |
| Professional services (legal, accounting) | No | Not enumerated |
| Personal services (haircuts, spa) | No | Not enumerated |
| Construction (real property improvement) | No (materials taxable at purchase) | DOR guidance |
| Transportation/freight (separately stated) | Exempt | N.C.G.S. Section 105-164.13(49) |

---

## Step 3: Return Form Structure
### 3.1 Registration

All sellers with nexus must register for a **Certificate of Registration** with NCDOR. Registration is completed online.

**Authority:** N.C.G.S. Section 105-164.29.

### 3.2 Filing Frequency

| Monthly Tax Liability | Filing Frequency | Due Date |
|-----------------------|------------------|----------|
| Over $100 per month | Monthly | 20th of the following month |
| $10 -- $100 per month | Quarterly | Last day of month following quarter-end |
| Under $10 per month | Annual | January 15 |

**Note:** NCDOR assigns filing frequency at registration. [T1]

### 3.3 Returns and Payment

- **Form E-500** (Sales and Use Tax Return) is the primary return. [T1]
- Electronic filing is mandatory for all filers. [T1]
- Payment is due on the same date as the return. [T1]
- Prepayment may be required for large filers (over $10,000/month in tax). [T2]

### 3.4 Discount for Timely Filing

North Carolina allows a **discount** for timely filing:

- **On state tax:** Filers may retain the greater of (a) $25 or (b) the following: for monthly filers, **1.5%** of the first $3,000 of state tax collected. [T1]
- **On local tax:** The county may provide a separate discount. [T2]
- Maximum state discount is generally capped. [T1]

**Authority:** N.C.G.S. Section 105-164.7.

### 3.5 Penalties and Interest

| Violation | Penalty | Authority |
|-----------|---------|-----------|
| Late filing | 5% per month, up to 25% | N.C.G.S. Section 105-236 |
| Late payment | 10% of tax due | N.C.G.S. Section 105-236 |
| Failure to file | $50 penalty per return + late penalties | N.C.G.S. Section 105-236 |
| Fraud | 50% of deficiency | N.C.G.S. Section 105-236 |
| Interest | Statutory rate (set semi-annually) | N.C.G.S. Section 105-241.21 |

---

## Step 4: Deductibility / Exemptions
### 5.1 North Carolina Exemption Certificates

| Certificate | Use Case | Authority |
|-------------|----------|-----------|
| **Form E-595E** (Streamlined Sales and Use Tax Certificate of Exemption) | Primary exemption certificate for all purposes (resale, exempt organizations, government) | N.C.G.S. Section 105-164.28A |
| **SSTCE** (Streamlined multi-state) | Multi-state purchases | SST Agreement |

**Note:** North Carolina uses the SST-compliant Form E-595E as its primary certificate, which consolidates multiple exemption types into one form. [T1]

### 5.2 Requirements for Valid Certificates [T1]

1. Purchaser's name and address. [T1]
2. Reason for exemption (resale, manufacturing, government, etc.). [T1]
3. NC sales tax registration number (for resale claims). [T1]
4. Description of property. [T1]
5. Purchaser's signature. [T1]
6. Date. [T1]

### 5.3 Good Faith Acceptance [T2]

Sellers accepting properly completed certificates in good faith are protected from liability. Blanket certificates are accepted for ongoing relationships. [T2]

### 5.4 Retention Period

Certificates must be retained for **3 years** from the date of the last transaction. [T1]

---


### 6.1 When Use Tax Applies

NC use tax applies when sales tax was not collected at the point of sale on property subsequently used, stored, or consumed in North Carolina. [T1]

### 6.2 Use Tax Rate

The use tax rate equals the applicable sales tax rate (4.75% state + applicable local). [T1]

### 6.3 Credit for Taxes Paid

Credit is allowed for sales/use tax paid to another state, up to the NC rate. [T1]

### 6.4 Use Tax Reporting

- **Businesses:** Report on Form E-500. [T1]
- **Individuals:** Report on NC individual income tax return (Form D-400), Line 18. [T1]

---

## Step 5: Key Thresholds
### 4.1 Physical Nexus

Standard physical nexus principles apply:

- Place of business in North Carolina. [T1]
- Employees or agents in the state. [T1]
- Inventory in the state (including FBA). [T1]
- Regular deliveries by company vehicles. [T1]
- Affiliate nexus (related entities with NC presence). [T2]

### 4.2 Economic Nexus [T1]

North Carolina enacted economic nexus effective **November 1, 2018** -- one of the earliest states post-Wayfair.

| Threshold | Value | Measurement Period |
|-----------|-------|--------------------|
| Revenue | **$100,000** in gross sales into North Carolina | Previous or current calendar year |
| Transactions | **200 transactions** into North Carolina | Previous or current calendar year |
| Test | **OR** -- either threshold triggers nexus | |

**Authority:** N.C.G.S. Section 105-164.8(b).

### 4.3 Marketplace Facilitator Rules [T1]

Effective **February 1, 2020**, marketplace facilitators must collect and remit:

- Marketplace facilitators meeting the nexus thresholds must collect on behalf of marketplace sellers. [T1]
- Marketplace sellers relieved of collection obligation for facilitated sales. [T1]

**Authority:** N.C.G.S. Section 105-164.4J.

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
1. **NEVER** advise that grocery food is fully exempt in North Carolina (it is taxed at a reduced 2% state rate + local taxes). [T1]
2. **NEVER** advise that SaaS or digital property is not taxable in NC (both are broadly taxable). [T1]
3. **NEVER** advise that custom software is exempt in NC (it is taxable, unlike in many states). [T1]
4. **NEVER** apply the standard 4.75% rate to motor vehicles (they have a 3% rate with a $2,000 cap). [T1]
5. **NEVER** provide a combined rate without verifying the specific county's local rate. [T1]
6. **NEVER** ignore the RMI (repair, maintenance, installation) taxability -- both labor and parts are taxable on TPP services. [T1]
7. **NEVER** advise that NC is not an SST member (it is a full member). [T1]
8. **NEVER** apply origin-based sourcing for shipped goods in NC (it uses destination-based per SST). [T1]
9. **NEVER** ignore the local tax component when quoting the food rate (2% state + local). [T1]
10. **NEVER** assume all digital transactions are taxable -- distinguish between digital property (taxable) and non-taxable services. [T2]

---

## Edge Case Registry

### 7.1 Motor Vehicle Tax Cap [T1]

North Carolina caps sales tax on motor vehicles:

- **Highway vehicles:** 3% tax rate, capped at **$2,000** per vehicle. [T1]
- **Boats/aircraft:** Tax capped at $1,500. [T1]
- Tax is collected by the DMV at registration, not by the dealer. [T1]
- Trade-in values reduce the taxable base. [T1]

**Authority:** N.C.G.S. Section 105-164.4(a)(4a).

### 7.2 SaaS and Digital Property Classification [T2]

North Carolina broadly taxes digital property:

- SaaS is taxable as digital property accessed electronically. [T2]
- The key question is whether the digital product provides "utility" to the customer -- if accessed via the internet and provides a useful function, it is likely taxable. [T2]
- **Information services** (database access, research services) may be treated differently from SaaS. [T3]
- **Digital advertising** is generally not taxable (service, not digital property). [T2]

### 7.3 Repair, Maintenance, and Installation Services [T2]

NC taxes RMI services on TPP broadly:

- Both labor and parts are taxable. [T1]
- The tax applies to the total charge for the service, including labor, parts, and materials. [T1]
- This is broader than many states that only tax parts, not labor. [T1]
- Real property repair is NOT subject to sales tax (contractor rules apply). [T2]

**Authority:** N.C.G.S. Section 105-164.4(a)(16).

### 7.4 Manufacturing Exemptions [T2]

North Carolina provides exemptions for qualifying manufacturers:

- Machinery and equipment used in manufacturing (direct use). [T2]
- Raw materials and components. [T1]
- Electricity and fuel used in manufacturing (reduced rate or exempt). [T2]
- Annual certification may be required. [T2]

**Authority:** N.C.G.S. Section 105-164.13(5e).

### 7.5 Food Establishment and Mixed Sales [T2]

The distinction between grocery food (2% state rate) and prepared food (full rate) can be complex:

- A grocery store deli selling hot prepared food: prepared food rate. [T1]
- A bakery selling unsliced bread: grocery food rate. [T1]
- A bakery selling sandwiches: prepared food rate. [T1]
- Food sold with utensils provided: prepared food. [T1]
- **Key test:** Was the food sold in a heated state, or with utensils, or as two or more food ingredients mixed by the seller for sale as a single item? [T2]

### 7.6 Construction Contractors [T2]

North Carolina treats contractors as consumers of materials:

- Contractors pay tax on materials at purchase. [T1]
- Contractors do NOT collect sales tax on real property improvements. [T1]
- Modular/manufactured homes have specific rules. [T2]

### 7.7 Film Industry Incentives [T2]

North Carolina previously had a film tax credit that interacted with sales tax exemptions. The credit has been modified/replaced -- verify current status. [T3]

---

## Test Suite

### Test 1: Basic Rate Calculation [T1]

**Question:** A retailer in Wake County (2.0% local) sells a $600 appliance. What is the total sales tax?

**Expected Answer:** $600 x (4.75% state + 2.0% local) = $600 x 6.75% = $40.50.

### Test 2: Grocery Food Rate [T1]

**Question:** A consumer buys $100 of groceries in Mecklenburg County (2.5% local). What tax is due?

**Expected Answer:** State: $100 x 2% = $2.00. Local: $100 x 2.5% = $2.50. Total: $4.50.

### Test 3: SaaS Taxability [T2]

**Question:** A Raleigh business subscribes to a $400/month project management SaaS tool. Is NC sales tax due?

**Expected Answer:** Yes. NC taxes SaaS as digital property. Tax = $400 x 6.75% (Wake County rate) = $27.00 per month.

### Test 4: Motor Vehicle Cap [T1]

**Question:** A customer purchases a $70,000 vehicle in North Carolina. What sales tax applies?

**Expected Answer:** Highway vehicles are taxed at 3%, capped at $2,000. Tax = min($70,000 x 3%, $2,000) = min($2,100, $2,000) = $2,000.

### Test 5: Economic Nexus [T1]

**Question:** An out-of-state seller made $95,000 in sales and 210 transactions in NC last year. Does the seller have nexus?

**Expected Answer:** Yes. NC uses an OR test. The 200-transaction threshold was exceeded.

### Test 6: RMI Services [T1]

**Question:** A repair shop charges $150 labor and $200 parts to fix a washing machine in NC. What is taxable?

**Expected Answer:** The entire $350 (labor + parts) is taxable. NC taxes the total charge for RMI services on TPP. At 6.75% (example): $350 x 6.75% = $23.63.

### Test 7: Custom Software [T2]

**Question:** A software development firm creates a $50,000 custom application for a North Carolina business. Is it taxable?

**Expected Answer:** Yes. Unlike many states, NC taxes custom software at the full sales tax rate. Tax = $50,000 x applicable combined rate.

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
