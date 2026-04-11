---
name: new-mexico-sales-tax
description: Use this skill whenever asked about New Mexico Gross Receipts Tax, New Mexico GRT, New Mexico sales tax, New Mexico TRD filing, New Mexico service taxation, or New Mexico healthcare deductions. Trigger on phrases like "New Mexico GRT", "Gross Receipts Tax", "NM sales tax", "NMSA §7-9", "New Mexico TRD", "New Mexico tax on services", or any request involving New Mexico GRT compliance. New Mexico does NOT have a traditional sales tax -- it has a Gross Receipts Tax. ALWAYS load us-sales-tax first for federal context.
---

# New Mexico Gross Receipts Tax (GRT) Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | New Mexico, United States |
| Jurisdiction Code | US-NM |
| Tax Type | Gross Receipts Tax (GRT) -- NOT a traditional sales tax |
| State Rate | 5.125% |
| Maximum Combined Rate | ~9.3125% (state 5.125% + county + city) |
| Primary Statute | New Mexico Statutes Annotated (NMSA) §7-9-1 et seq. |
| Governing Agency | Taxation and Revenue Department (TRD) |
| Portal | https://tap.state.nm.us (Taxpayer Access Point) |
| SST Member | No |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: rates, basic taxability, filing mechanics. T2: service classification, healthcare deductions, construction GRT. T3: audit defense, complex deductions, Native American transactions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any New Mexico sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a New Mexico sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in New Mexico? | Drives taxability classification under New Mexico law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in New Mexico? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple New Mexico local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 Fundamental Structure -- Tax on the Seller [T1]

Like Hawaii's GET, New Mexico's Gross Receipts Tax is fundamentally different from a traditional sales tax:

- **GRT is imposed on the SELLER, not the buyer.** [T1]
- GRT applies to the **gross receipts** of persons engaged in business in New Mexico. [T1]
- GRT applies to virtually **ALL transactions**, including services, making it one of the broadest tax bases in the US. [T1]
- There is no legal requirement to pass GRT to the buyer (though most businesses do). [T1]
- Unlike Hawaii, New Mexico uses a system of **deductions and exemptions** rather than reduced rates. [T2]

**Statute:** NMSA §7-9-4 (imposition of tax).

### 1.2 Rate Structure [T1]

| Component | Rate |
|-----------|------|
| State GRT rate | 5.125% |
| County GRT (varies) | 0% to ~2.1875% |
| Municipal GRT (varies) | 0% to ~2.0% |
| **Combined maximum** | **~9.3125%** |

- Rates vary by location within New Mexico. [T1]
- Each city and county may impose its own GRT increment. [T1]
- Albuquerque combined rate: approximately **7.875%**. [T1]
- Santa Fe combined rate: approximately **8.4375%**. [T1]
- Las Cruces combined rate: approximately **8.3125%**. [T1]

### 1.3 Sourcing -- Destination-Based (2021+) [T1]

- Effective July 1, 2021, New Mexico switched from **origin-based** to **destination-based** sourcing. [T1]
- For sales of tangible property, the rate at the buyer's delivery address applies. [T1]
- For services, the rate at the location where the service is delivered/received applies. [T1]

**Statute:** NMSA §7-1-14 (sourcing rules, as amended by HB 6, 2019).

---

## Step 2: Transaction Classification Rules
### 2.1 Services -- VERY BROADLY TAXABLE [T1]

**New Mexico taxes virtually ALL services under GRT.** [T1]

Taxable services include (non-exhaustive):
- Professional services: legal, accounting, consulting, engineering, architecture. [T1]
- Medical and healthcare services (subject to certain deductions). [T2]
- Personal care: haircuts, spa services. [T1]
- Repair and maintenance. [T1]
- Cleaning and janitorial. [T1]
- IT services, web design, software development. [T1]
- Construction services (major area -- see Edge Cases). [T1]
- Marketing and advertising. [T1]

### 2.2 Grocery Food [T1]

- Unprepared grocery food: **exempt** (deductible from gross receipts). NMSA §7-9-92. [T1]
- This exemption was enacted effective January 1, 2023 (HB 163, 2022). [T1]
- Prior to 2023, food was fully taxable. [T1]
- Prepared food: taxable. [T1]
- Candy: taxable. [T1]
- Soft drinks: taxable. [T1]

### 2.3 Clothing [T1]

- Clothing is taxable at the full combined rate. No exemption. [T1]

### 2.4 Prescription Drugs and Medical [T2]

- Prescription drugs: **deductible** from gross receipts (effectively exempt). NMSA §7-9-73.2. [T1]
- OTC drugs: taxable. [T1]
- Healthcare services: subject to GRT, but many healthcare receipts qualify for **deductions**:
  - Receipts from Medicare/Medicaid: deductible. NMSA §7-9-77.1. [T2]
  - Receipts from managed care organizations: certain deductions available. [T2]
  - Hospital gross receipts: subject to GRT but substantial deductions available. [T2]
- **Flag for reviewer:** Healthcare GRT is complex. Multiple overlapping deductions exist. [T3]

### 2.5 SaaS and Digital Goods [T2]

- **SaaS:** **Taxable** under GRT. All services rendered in or delivered to New Mexico are subject to GRT. [T1]
- **Digital downloads:** Taxable. [T1]
- **Streaming services:** Taxable. [T1]
- **Custom software development:** Taxable as a service. [T1]
- **Canned software:** Taxable. [T1]

### 2.6 Construction -- Significant GRT Area [T2]

- Construction services are subject to GRT. The contractor owes GRT on the **entire contract price** (materials + labor). [T1]
- This is different from most states where the contractor pays sales tax on materials and does not collect on the labor component. [T1]
- Construction GRT rates may vary by project location. [T1]
- Nontaxable Transaction Certificates (NTTCs) may apply to certain construction scenarios (e.g., government projects, construction of manufacturing facilities). [T2]
- **Flag for reviewer:** Construction GRT is a major compliance area. Verify deduction eligibility and NTTC applicability for each project. [T3]

### 2.7 Manufacturing [T2]

- Manufacturing equipment: deductible from GRT under the high-wage jobs tax credit or other incentive programs. [T2]
- Raw materials consumed in manufacturing for resale: deductible (sale for resale). NMSA §7-9-47. [T1]
- The standard resale deduction applies to manufacturers selling finished goods. [T1]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | CRS-1 (Combined Reporting System return) |
| Filing Frequencies | Monthly (most common); Semi-annually (small taxpayers) |
| Due Date | 25th of the month following the reporting period |
| Portal | https://tap.state.nm.us |
| E-filing | Required for most filers |

**Note:** New Mexico uses a Combined Reporting System (CRS) where GRT, withholding tax, and compensating tax are reported on a single return. [T1]

### 4.2 Vendor Discount [T1]

New Mexico does NOT offer a vendor discount for timely filing. [T1]

### 4.3 Penalties and Interest [T1]

- Late filing penalty: 2% per month, up to 20%. [T1]
- Late payment penalty: 2% per month, up to 20%. [T1]
- Interest: rate set annually by TRD. [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for New Mexico. Key categories: [T1]

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
| Revenue Threshold | $100,000 in New Mexico gross receipts |
| Transaction Threshold | N/A (revenue only) |
| Measurement Period | Current or prior calendar year |
| Effective Date | July 1, 2019 |

**Statute:** NMSA §7-1-14(D).

### 3.2 Marketplace Facilitator [T1]

New Mexico requires marketplace facilitators to collect and remit GRT. NMSA §7-9-3.5(A)(26). [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER call New Mexico's GRT a "sales tax." It is a Gross Receipts Tax on the seller, not a sales tax on the buyer. [T1]
- NEVER assume services are exempt in New Mexico. GRT applies to virtually ALL services, including professional services. [T1]
- NEVER ignore the destination-based sourcing rules (effective 2021). Rate is based on buyer's location, not seller's. [T1]
- NEVER assume construction labor is exempt. In NM, GRT applies to the ENTIRE contract including labor. [T1]
- NEVER forget healthcare deductions. Medicare/Medicaid receipts are deductible from GRT. [T1]
- NEVER apply GRT to grocery food purchased after 2023. Food is now deductible. [T1]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Services Taxable to Out-of-State Clients [T2]

**Situation:** A New Mexico law firm provides legal services to a client in Texas. Is the revenue subject to GRT?

**Resolution:**
- Under destination-based sourcing (2021+), the GRT rate is based on the location where the service is delivered/received. [T1]
- If the service is delivered to a client outside New Mexico, an interstate commerce deduction may apply. NMSA §7-9-57. [T2]
- The law firm must analyze whether the service was "initially used" in New Mexico or outside the state. [T2]
- **Flag for reviewer:** Service sourcing under the destination-based rules is complex. The "initial use" test determines NM taxability. [T2]

### EC2 -- Construction GRT on Government Projects [T2]

**Situation:** A contractor builds a school for a New Mexico public school district. Does GRT apply?

**Resolution:**
- Construction services are normally subject to GRT. [T1]
- However, governmental entities may issue Nontaxable Transaction Certificates (NTTCs) that provide deductions from GRT. NMSA §7-9-54. [T2]
- The contractor must obtain a valid NTTC (Type 9) from the government entity before claiming the deduction. [T1]
- Without the NTTC, GRT applies at the full combined rate on the entire contract. [T1]
- **Flag for reviewer:** Verify NTTC validity and type. Not all government contracts qualify for the deduction. [T2]

### EC3 -- Healthcare Deductions [T3]

**Situation:** A medical practice receives revenue from Medicare ($200,000), private insurance ($300,000), and self-pay patients ($100,000). How is GRT applied?

**Resolution:**
- Medicare/Medicaid receipts: deductible from GRT. NMSA §7-9-77.1. [T1]
- Private insurance receipts: generally subject to GRT (no broad deduction). [T2]
- Self-pay receipts: subject to GRT. [T1]
- GRT would apply to the $300,000 (insurance) + $100,000 (self-pay) = $400,000. [T1]
- Additional deductions may be available under specific healthcare provisions. [T2]
- **Flag for reviewer:** Healthcare GRT has many nuances and overlapping deductions. Escalate complex medical practice scenarios. [T3]

### EC4 -- Destination-Based Sourcing Transition [T2]

**Situation:** A business previously filed using origin-based sourcing (pre-2021). How did the transition affect compliance?

**Resolution:**
- Before July 1, 2021, GRT was based on the seller's location (origin-based). [T1]
- After July 1, 2021, GRT is based on the buyer's location (destination-based). [T1]
- Sellers must now determine the rate for each customer's delivery address. [T1]
- This increases complexity, especially for sellers shipping to multiple NM locations. [T1]
- **Flag for reviewer:** Verify that the client's systems were updated for destination-based sourcing in 2021. Legacy configurations may cause errors. [T2]

---

### EC5 -- Software Development Services [T2]

**Situation:** A NM-based software development company creates a custom application for a client in Texas.

**Resolution:**
- Software development is a service subject to GRT. [T1]
- Under destination-based sourcing, the GRT rate is based on the client's location. [T1]
- If the service is delivered to a client outside NM, the interstate commerce deduction (NMSA §7-9-57) may apply. [T2]
- The "initial use" test determines where the service is delivered. [T2]
- **Flag for reviewer:** The interstate commerce deduction for services is fact-specific. Analyze where the service output is initially used. [T2]

### EC6 -- Rental of Real Property [T2]

**Situation:** A commercial landlord rents office space in Albuquerque for $5,000/month.

**Resolution:**
- Rental of real property is subject to GRT. NMSA §7-9-3.5(A)(3). [T1]
- GRT applies at the combined rate for the property's location. [T1]
- Residential rental may be subject to GRT at a potentially lower effective rate depending on available deductions. [T2]
- The landlord may pass GRT to tenants (commonly shown as a lease line item). [T2]
- **Flag for reviewer:** Commercial vs. residential rental may have different deduction eligibility. [T2]

---

## Test Suite

### Test 1 -- Basic Sale in Albuquerque

**Input:** Retailer in Albuquerque sells $1,000 of merchandise to a local buyer. Combined rate = 7.875%.
**Expected output:** GRT = $1,000 x 7.875% = $78.75. If passed to buyer, total = $1,078.75.

### Test 2 -- Legal Services Subject to GRT

**Input:** NM attorney bills $5,000 for legal services to a Santa Fe client. Santa Fe combined rate = 8.4375%.
**Expected output:** Legal services ARE subject to GRT. GRT = $5,000 x 8.4375% = $421.88.

### Test 3 -- Grocery Food Exemption (2023+)

**Input:** Customer buys $200 of unprepared groceries in Las Cruces.
**Expected output:** Grocery food is exempt (deductible) from GRT effective 2023. Tax = $0. Total = $200.00.

### Test 4 -- Construction Contract

**Input:** Contractor completes a $500,000 commercial building project in Albuquerque. Combined rate = 7.875%. No NTTC.
**Expected output:** GRT applies to the ENTIRE contract (materials + labor). GRT = $500,000 x 7.875% = $39,375.00.

### Test 5 -- Economic Nexus

**Input:** Remote SaaS company from California earned $120,000 from New Mexico customers.
**Expected output:** $120,000 exceeds $100,000. Nexus IS triggered. SaaS is taxable under GRT. Must register and pay GRT on NM-sourced revenue.

---

### Test 6 -- Software Development for Out-of-State Client

**Input:** NM software company earns $50,000 from a California client. All work performed in NM. Interstate deduction applies.
**Expected output:** If interstate commerce deduction applies, GRT = $0 (deductible). If deduction does NOT apply, GRT = $50,000 x local rate.

### Test 7 -- Real Property Rental

**Input:** Landlord rents commercial space in Santa Fe for $8,000/month. Santa Fe combined rate = 8.4375%.
**Expected output:** GRT = $8,000 x 8.4375% = $675.00 per month.

### Test 8 -- Government Construction Project with NTTC

**Input:** Contractor completes $1 million government building with valid Type 9 NTTC. Albuquerque rate = 7.875%.
**Expected output:** With valid NTTC, GRT is deductible. GRT = $0. Without NTTC, GRT = $1,000,000 x 7.875% = $78,750.

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
