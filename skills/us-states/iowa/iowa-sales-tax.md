---
name: iowa-sales-tax
description: Use this skill whenever asked about Iowa sales tax, Iowa use tax, Iowa IDR sales tax filing, Iowa local option tax, or Iowa sales tax compliance. Trigger on phrases like "Iowa sales tax", "IA sales tax", "IDR", "Iowa Code §423", "Iowa local option tax", "Iowa SST", or any request involving Iowa state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# Iowa Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Iowa, United States |
| Jurisdiction Code | US-IA |
| Tax Type | Sales and Use Tax (state + local option) |
| State Rate | 6.00% |
| Local Option Tax | 1.00% (where imposed by jurisdiction) |
| Maximum Combined Rate | 7.00% |
| Primary Statute | Iowa Code Chapter 423 |
| Governing Agency | Iowa Department of Revenue (IDR) |
| Portal | https://tax.iowa.gov |
| SST Member | Yes -- Full Member |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics. T2: service taxability, local option determination, exemption specifics. T3: audit defense, complex transactions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Iowa sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have an Iowa sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Iowa? | Drives taxability classification under Iowa law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Iowa? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Iowa local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Sales Tax Rate

Iowa imposes a state sales tax of **6.00%** on the retail sale of tangible personal property and enumerated services. [T1]

**Statute:** Iowa Code §423.2.

### 1.2 Local Option Sales Tax (LOST) [T1]

- Iowa jurisdictions (counties and cities) may impose a **1% local option sales tax** (LOST). [T1]
- LOST requires voter approval. [T1]
- The majority of Iowa's 99 counties have adopted the 1% LOST. [T1]
- Combined rate where LOST is in effect: **7.00%**. [T1]
- LOST is administered and collected by IDR alongside the state tax. [T1]

**Statute:** Iowa Code §423B.

### 1.3 Sourcing [T1]

Iowa uses **destination-based** sourcing. The applicable rate (including LOST) is determined by the delivery address. [T1]

As an SST member, Iowa follows SSUTA sourcing rules. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food -- EXEMPT [T1]

- Unprepared grocery food and food ingredients: **exempt**. Iowa Code §423.3(57). [T1]
- Prepared food: taxable at the full combined rate. [T1]
- Candy: taxable. [T1]
- Soft drinks: taxable. [T1]
- Iowa follows SST definitions for food, prepared food, candy, and soft drinks. [T1]

### 2.2 Clothing [T1]

- Clothing is **fully taxable** at the standard rate. No exemption. [T1]
- Iowa holds a sales tax holiday (see Edge Cases) that temporarily exempts certain clothing items. [T2]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. Iowa Code §423.3(28). [T1]
- Over-the-counter (OTC) drugs: **exempt** (Iowa exempts most OTC drugs). [T1]
- Durable medical equipment: exempt with prescription. [T1]
- Prosthetics, hearing aids, corrective lenses: exempt. [T1]

### 2.4 Services [T2]

Iowa taxes a substantial number of enumerated services:

- **Taxable services include:** Machine/vehicle repair, building cleaning and maintenance, pest control, landscaping, security services, storage, dry cleaning, pet grooming, photography, tanning, dating services, tattoo/body piercing, survey/abstract, electrical/plumbing installation (on existing property). [T2]
- **Exempt services include:** Professional services (legal, accounting, medical, engineering), educational services, financial services, barber/beauty services. [T2]

**Statute:** Iowa Code §423.2(6) (enumerated taxable services).

### 2.5 SaaS and Digital Goods [T2]

- **SaaS:** Iowa currently does **not** tax SaaS. SaaS is not considered TPP or an enumerated taxable service. [T2]
- **Canned software (physical media):** Taxable. [T1]
- **Canned software (electronic delivery):** Taxable. Iowa Code §423.1(52A). [T1]
- **Digital downloads:** Taxable as specified digital products under SST. Iowa Code §423.2(11). [T1]
- **Streaming services:** Taxable. [T2]
- **Custom software:** Exempt when developed for a single customer. [T2]

### 2.6 Manufacturing [T1]

- Machinery and equipment used in manufacturing or processing: **exempt** (for machinery used directly and primarily in manufacturing). Iowa Code §423.3(47). [T1]
- Replacement parts for exempt manufacturing equipment: exempt. [T1]
- Computers used in manufacturing process control: exempt. [T2]

### 2.7 Motor Vehicles [T1]

- Motor vehicles are subject to a 5% fee for new registration (applied at registration, not point of sale). [T1]
- Trade-in credit reduces the taxable amount. [T1]
- The 5% rate for vehicles is different from the general 6% sales tax rate. [T1]

### 2.8 Agricultural [T1]

- Farm machinery and equipment: exempt. Iowa Code §423.3(7). [T1]
- Feed, seed, fertilizer, and agricultural chemicals: exempt. [T1]
- Livestock: exempt. [T1]
- Fuel used in agricultural production: exempt. [T1]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | Sales/Use Tax Return (filed via GovConnectIowa) |
| Filing Frequencies | Monthly (>$1,200/year liability); Quarterly ($120-$1,200); Annually (<$120) |
| Due Date | Last day of the month following the reporting period |
| Portal | https://govconnect.iowa.gov |
| E-filing | Required for most filers |

### 4.2 Vendor Discount [T1]

Iowa does NOT offer a vendor discount for timely filing. [T1]

### 4.3 Penalties and Interest [T1]

- Late filing penalty: 10% of tax due. [T1]
- Late payment penalty: 5% of tax due. [T1]
- Interest: rate set annually by IDR. [T1]
- Fraud penalty: 75% of tax due. [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for Iowa. Key categories: [T1]

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
| Revenue Threshold | $100,000 in Iowa sales |
| Transaction Threshold | N/A (revenue only) |
| Measurement Period | Current or prior calendar year |
| Effective Date | January 1, 2019 |

**Statute:** Iowa Code §423.14A.

### 3.2 Physical Nexus [T1]

Standard physical nexus rules apply. [T1]

### 3.3 Marketplace Facilitator [T1]

Iowa requires marketplace facilitators to collect and remit sales tax on marketplace sales. Iowa Code §423.14A(3). [T1]

### 3.4 SST Registration [T1]

As a full SST member, Iowa allows registration through the SSTRS and use of CSPs. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER assume a uniform 7% rate across Iowa. LOST applies in most but not all jurisdictions. Verify delivery address. [T1]
- NEVER tax grocery food in Iowa. Unprepared food and food ingredients are exempt. [T1]
- NEVER exempt candy and soft drinks in Iowa. They are excluded from the food exemption and are fully taxable. [T1]
- NEVER ignore Iowa's broad OTC drug exemption. Iowa exempts OTC drugs, unlike most states. [T1]
- NEVER assume all services are exempt. Iowa taxes a substantial enumerated list of services. [T2]
- NEVER apply the general 6% rate to motor vehicles. Vehicles are subject to a 5% new registration fee. [T1]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Local Option Sales Tax Determination [T2]

**Situation:** An e-commerce seller ships products to two Iowa addresses: one in a county with LOST (7% combined) and one without LOST (6% state only).

**Resolution:**
- Destination-based sourcing applies. Seller must determine whether the delivery address is in a LOST jurisdiction. [T1]
- IDR publishes a list of jurisdictions with LOST. [T1]
- Sellers using SST-certified rate tables will automatically receive the correct rate. [T1]
- **Flag for reviewer:** Most Iowa counties have adopted LOST, but not all. Verify the specific delivery jurisdiction. [T2]

### EC2 -- Sales Tax Holiday (Back-to-School) [T2]

**Situation:** Iowa's annual sales tax holiday (typically first Friday-Saturday in August) exempts certain items. What qualifies?

**Resolution:**
- Clothing items under $100 per item: exempt from state and local tax during the holiday. [T1]
- Specified items only; verify current year's list with IDR. [T2]
- Online purchases placed during the holiday qualify. [T1]
- **Statute:** Iowa Code §423.3(68).
- **Flag for reviewer:** Verify current year's thresholds and item categories before applying. [T2]

### EC3 -- Enumerated Services vs. Non-Enumerated [T2]

**Situation:** A company provides "consulting services" which include technology consulting and equipment installation. Is the service taxable?

**Resolution:**
- Professional consulting is NOT an enumerated taxable service in Iowa. [T2]
- However, installation of TPP may be taxable if it falls under an enumerated service category. [T2]
- If the invoice bundles consulting and installation, the taxable treatment may depend on the "true object" of the transaction. [T2]
- Best practice: separately state taxable and non-taxable service components. [T2]
- **Flag for reviewer:** Review the enumerated services list in Iowa Code §423.2(6) to determine whether any component is taxable. [T2]

### EC4 -- Motor Vehicle Rate Difference [T2]

**Situation:** A customer purchases a car for $30,000 and separately purchases accessories ($500) installed at the dealership.

**Resolution:**
- The vehicle purchase is subject to the 5% new registration fee (not the 6% sales tax). [T1]
- The accessories (if sold as TPP at the dealership) are subject to the general 6% sales tax + LOST. [T1]
- The vehicle and accessories have DIFFERENT tax rates. [T1]
- **Flag for reviewer:** Ensure POS systems at auto dealerships apply the correct rate to vehicle vs. non-vehicle items. [T2]

---

### EC5 -- Machine Repair as Taxable Service [T2]

**Situation:** A repair company charges $1,500 for parts and $1,000 for labor to repair a piece of industrial equipment.

**Resolution:**
- Machine/vehicle repair is an enumerated taxable service in Iowa. [T1]
- Both parts AND labor are taxable when provided as part of a repair service. [T1]
- Tax applies to the total $2,500 at the combined rate. [T1]
- **Flag for reviewer:** Unlike some states that exempt separately stated labor, Iowa taxes the entire repair transaction. [T2]

### EC6 -- LOST Refund for Overpayment [T2]

**Situation:** A seller inadvertently collected 1% LOST on a sale delivered to a jurisdiction without LOST.

**Resolution:**
- The seller overcollected from the buyer. [T1]
- The seller should refund the overpayment to the buyer. [T1]
- The seller can claim a credit on a subsequent return or file an amended return. [T2]
- **Flag for reviewer:** LOST errors are common. Implement address verification to prevent them. [T2]

---

## Test Suite

### Test 1 -- Basic Taxable Sale with LOST

**Input:** Seller in Des Moines sells $800 of furniture to a local buyer. Polk County has LOST. Combined rate = 7%.
**Expected output:** Sales tax = $800 x 7% = $56.00. Total = $856.00.

### Test 2 -- Grocery Food Exemption

**Input:** Customer buys $150 of unprepared groceries in Iowa City. Combined rate = 7%.
**Expected output:** Unprepared food is EXEMPT. Tax = $0. Total = $150.00.

### Test 3 -- Candy and Soft Drinks Taxable

**Input:** Customer buys $10 candy and $5 soft drink at a Cedar Rapids store. Combined rate = 7%.
**Expected output:** Both candy and soft drinks are taxable. Tax = $15 x 7% = $1.05. Total = $16.05.

### Test 4 -- Prescription and OTC Drugs

**Input:** Pharmacy sells $80 prescription drug and $20 OTC cold medicine in Davenport. Combined rate = 7%.
**Expected output:** Both prescription and OTC drugs are exempt in Iowa. Tax = $0. Total = $100.00.

### Test 5 -- Economic Nexus

**Input:** Online seller from Oregon sold $110,000 to Iowa buyers in the prior calendar year.
**Expected output:** Revenue ($110,000) exceeds $100,000 threshold. Nexus IS triggered. Seller must register and collect Iowa sales tax.

---

### Test 6 -- Machine Repair Taxable

**Input:** Repair shop charges $800 parts + $600 labor for machine repair in Des Moines. Combined rate = 7%.
**Expected output:** Both parts and labor are taxable (enumerated service). Tax = $1,400 x 7% = $98.00. Total = $1,498.00.

### Test 7 -- Sale Without LOST

**Input:** Seller ships $500 item to a buyer in a rural Iowa county WITHOUT LOST. State rate = 6% only.
**Expected output:** Tax = $500 x 6% = $30.00. Total = $530.00.

### Test 8 -- Digital Download Taxable

**Input:** Customer downloads $20 music album. Buyer in Iowa City. Combined rate = 7%.
**Expected output:** Digital downloads are taxable. Tax = $20 x 7% = $1.40. Total = $21.40.

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
