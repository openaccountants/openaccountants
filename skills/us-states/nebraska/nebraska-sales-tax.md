---
name: nebraska-sales-tax
description: Use this skill whenever asked about Nebraska sales tax, Nebraska use tax, Nebraska DOR sales tax filing, Nebraska local option tax, or Nebraska sales tax compliance. Trigger on phrases like "Nebraska sales tax", "NE sales tax", "R.R.S. Neb. §77-2701", "Nebraska DOR", "Nebraska SST", or any request involving Nebraska state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# Nebraska Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Nebraska, United States |
| Jurisdiction Code | US-NE |
| Tax Type | Sales and Use Tax (state + local) |
| State Rate | 5.50% |
| Maximum Combined Rate | ~7.50% (state 5.5% + local up to 2%) |
| Primary Statute | Revised Statutes of Nebraska (R.R.S. Neb.) §77-2701 et seq. |
| Governing Agency | Nebraska Department of Revenue (DOR) |
| Portal | https://revenue.nebraska.gov |
| SST Member | Yes -- Full Member |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics. T2: local rate determination, service taxability, exemption specifics. T3: audit defense, complex exemptions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Nebraska sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Nebraska sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Nebraska? | Drives taxability classification under Nebraska law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Nebraska? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Nebraska local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Sales Tax Rate

Nebraska imposes a state sales tax of **5.50%** on the retail sale of tangible personal property and enumerated services. [T1]

**Statute:** R.R.S. Neb. §77-2703.

### 1.2 Local Sales Taxes [T1]

- Cities may impose a local option sales tax of **0.50%, 1.00%, 1.50%, or 2.00%**. [T1]
- Most Nebraska cities with a local tax impose 1.5% or 2%. [T1]
- Omaha and Lincoln both impose a local tax. [T1]
- Local taxes are administered and collected by DOR. [T1]
- Combined rates range from 5.5% (state only) to **7.50%** (state + 2% local). [T1]

### 1.3 Sourcing [T1]

Nebraska uses **destination-based** sourcing. [T1]

As an SST member, Nebraska follows SSUTA sourcing rules. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food -- EXEMPT [T1]

- Unprepared grocery food and food ingredients: **exempt**. R.R.S. Neb. §77-2704.24. [T1]
- Prepared food: taxable at the full combined rate. [T1]
- Candy: taxable (excluded from food exemption under SST definitions). [T1]
- Soft drinks: taxable. [T1]
- Nebraska follows SST definitions for food categories. [T1]

### 2.2 Clothing [T1]

- Clothing is **fully taxable**. No exemption. [T1]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. R.R.S. Neb. §77-2704.09. [T1]
- OTC drugs: **exempt**. [T1]
- DME: exempt. [T1]
- Prosthetics, hearing aids: exempt. [T1]

### 2.4 Services [T2]

Nebraska taxes a substantial number of enumerated services:

- **Taxable services include:** Building cleaning/maintenance, pest control, detective/security, motor vehicle repair, lawn care/landscaping, dry cleaning, pet grooming, storage, telecommunications, cable/satellite TV, animal specialty services. [T2]
- **Exempt services include:** Professional services (legal, accounting, medical, engineering), educational services, financial services, barber/beauty services. [T2]

**Statute:** R.R.S. Neb. §77-2701.16 (enumerated taxable services).

### 2.5 SaaS and Digital Goods [T2]

- **SaaS:** Generally **not taxable** in Nebraska. Not considered TPP or an enumerated service. [T2]
- **Canned software (physical):** Taxable. [T1]
- **Canned software (electronic delivery):** Taxable. [T1]
- **Digital downloads:** Taxable as specified digital products under SST. [T1]
- **Custom software:** Exempt. [T2]

### 2.6 Manufacturing [T1]

- Manufacturing machinery and equipment: **exempt**. R.R.S. Neb. §77-2704.22. [T1]
- Includes machinery used directly in processing, refining, or manufacturing. [T1]
- Repair and replacement parts for exempt machinery: exempt. [T1]

### 2.7 Agricultural [T1]

- Farm machinery and equipment used in commercial agriculture: exempt. R.R.S. Neb. §77-2704.36. [T1]
- Feed, seed, fertilizer: exempt. [T1]
- Livestock: exempt when purchased for breeding/production. [T1]
- Agricultural chemicals: exempt. [T1]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | Form 10 (Nebraska and Local Sales and Use Tax Return) |
| Filing Frequencies | Monthly (>$900/quarter); Quarterly ($300-$900); Annually (<$300) |
| Due Date | 20th of the month following the reporting period |
| Portal | https://revenue.nebraska.gov (NebFile) |
| E-filing | Required for most filers |

### 4.2 Vendor Discount [T1]

Nebraska does NOT offer a vendor discount for timely filing. [T1]

### 4.3 Penalties and Interest [T1]

- Late filing/payment penalty: 10% of tax due (maximum). [T1]
- Interest: statutory rate set annually by DOR. [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for Nebraska. Key categories: [T1]

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
| Revenue Threshold | $100,000 in Nebraska sales |
| Transaction Threshold | 200 transactions |
| Test | OR (either threshold triggers nexus) |
| Measurement Period | Current or prior calendar year |
| Effective Date | January 1, 2019 |

**Statute:** R.R.S. Neb. §77-2703(2)(d).

### 3.2 Marketplace Facilitator [T1]

Nebraska requires marketplace facilitators to collect and remit. R.R.S. Neb. §77-2703(2)(e). [T1]

### 3.3 SST Registration [T1]

As an SST member, remote sellers can register through SSTRS and use CSPs. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER tax grocery food in Nebraska. Unprepared food is exempt. [T1]
- NEVER exempt candy and soft drinks as food. They are taxable in Nebraska (SST definitions apply). [T1]
- NEVER assume a uniform rate statewide. Local option taxes vary by city. [T1]
- NEVER tax OTC drugs in Nebraska. They are exempt (unlike most states). [T1]
- NEVER confuse OTC drugs (exempt) with dietary supplements (taxable). [T1]
- NEVER assume SaaS is taxable. Nebraska does not tax SaaS under current law. [T2]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Local Option Tax Determination [T2]

**Situation:** Seller ships to a customer in a small Nebraska town. How to determine the local rate?

**Resolution:**
- Destination-based sourcing applies. The local rate is based on the delivery address. [T1]
- DOR publishes a list of cities with local option taxes and their rates. [T1]
- If the delivery address is outside any city with a local tax, only the 5.5% state rate applies. [T1]
- SST-certified rate tables include local rates. [T1]
- **Flag for reviewer:** Not all Nebraska cities have a local tax. Verify the specific delivery address. [T2]

### EC2 -- OTC Drug Exemption [T1]

**Situation:** A retailer asks whether OTC medications should be taxed in Nebraska.

**Resolution:**
- Nebraska exempts OTC drugs from sales tax. R.R.S. Neb. §77-2704.09. [T1]
- This includes non-prescription medicines, cold remedies, pain relievers, etc. [T1]
- Dietary supplements are NOT considered OTC drugs and are taxable. [T2]
- **Flag for reviewer:** Distinguish between OTC drugs (exempt) and dietary supplements (taxable). [T2]

### EC3 -- Cleaning Services Taxable [T2]

**Situation:** A commercial cleaning company provides janitorial services to an office building in Omaha.

**Resolution:**
- Building cleaning and maintenance is an enumerated taxable service in Nebraska. [T1]
- Tax applies at the combined rate (5.5% state + Omaha local). [T1]
- Both residential and commercial cleaning services are taxable. [T2]
- **Flag for reviewer:** Verify whether the specific cleaning service falls within the statutory enumeration. [T2]

### EC4 -- Agricultural Equipment Exemption vs. General Equipment [T2]

**Situation:** A farmer purchases a pickup truck used both for farm operations and personal use.

**Resolution:**
- Farm machinery and equipment used primarily in commercial agriculture is exempt. [T1]
- A pickup truck used for dual purposes (farm and personal) may not qualify for the full exemption. [T2]
- The exemption generally requires the equipment to be used "directly and primarily" in agricultural operations. [T2]
- **Flag for reviewer:** Mixed-use equipment exemptions require analysis of primary use. Escalate if uncertain. [T2]

---

### EC5 -- Security Services as Enumerated Taxable Service [T2]

**Situation:** A security company provides guard services to a commercial building in Omaha.

**Resolution:**
- Detective and security services are enumerated as taxable in Nebraska. [T1]
- The security company must collect sales tax on its charges. [T1]
- Tax = service charges x combined rate (5.5% state + local). [T1]
- **Flag for reviewer:** Verify the service falls within the statutory definition of detective/security services. [T2]

### EC6 -- Pet Grooming Taxable [T2]

**Situation:** A pet grooming salon charges $80 for grooming in Lincoln.

**Resolution:**
- Animal specialty services (including grooming) are enumerated as taxable. [T1]
- Tax = $80 x combined rate. [T1]
- Veterinary medical services (examination, treatment) are separate and generally exempt. [T2]
- **Flag for reviewer:** Distinguish between taxable pet grooming and exempt veterinary medical services. [T2]

### EC7 -- Repair of TPP with Parts and Labor [T2]

**Situation:** A computer repair shop charges $200 for parts and $150 for labor. Are both taxable?

**Resolution:**
- Motor vehicle repair is specifically enumerated as taxable in Nebraska. [T1]
- Other TPP repair may also be taxable depending on classification. [T2]
- If the repair is an enumerated taxable service, both parts and labor are typically taxable. [T2]
- **Flag for reviewer:** Review the specific service against the enumerated list in R.R.S. Neb. §77-2701.16. [T2]

---

## Test Suite

### Test 1 -- Basic Sale in Omaha

**Input:** Seller in Omaha sells $500 of electronics. Combined rate = 7% (5.5% state + 1.5% local).
**Expected output:** Tax = $500 x 7% = $35.00. Total = $535.00.

### Test 2 -- Grocery Food Exemption

**Input:** Customer buys $200 of unprepared groceries in Lincoln. Combined rate = 7.25%.
**Expected output:** Groceries are EXEMPT. Tax = $0. Total = $200.00.

### Test 3 -- OTC Drug Exemption

**Input:** Customer buys $30 OTC pain reliever and $20 dietary supplement in Omaha. Combined rate = 7%.
**Expected output:** OTC drug: exempt. Dietary supplement: taxable. Tax = $20 x 7% = $1.40. Total = $51.40.

### Test 4 -- Cleaning Service Taxable

**Input:** Janitorial company bills $2,000 for office cleaning in Lincoln. Combined rate = 7.25%.
**Expected output:** Cleaning is taxable. Tax = $2,000 x 7.25% = $145.00. Total = $2,145.00.

### Test 5 -- Economic Nexus

**Input:** Remote seller from Texas sold $80,000 and 250 transactions to Nebraska in the prior year.
**Expected output:** Revenue ($80,000) below $100,000 but transactions (250) exceed 200. Nexus IS triggered (OR test). Must register.

---

### Test 6 -- Security Services Taxable

**Input:** Security company charges $3,000/month for guard services in Omaha. Combined rate = 7%.
**Expected output:** Security services are taxable. Tax = $3,000 x 7% = $210.00. Total = $3,210.00.

### Test 7 -- Pet Grooming Taxable

**Input:** Pet salon charges $65 for dog grooming in Lincoln. Combined rate = 7.25%.
**Expected output:** Pet grooming is taxable. Tax = $65 x 7.25% = $4.71. Total = $69.71.

### Test 8 -- Manufacturing Equipment Exempt

**Input:** Manufacturer buys $75,000 production equipment for Nebraska plant.
**Expected output:** Manufacturing equipment is exempt. Tax = $0. Total = $75,000.

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
