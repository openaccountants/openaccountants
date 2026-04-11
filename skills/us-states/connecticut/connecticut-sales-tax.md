---
name: connecticut-sales-tax
description: Use this skill whenever asked about Connecticut sales tax, Connecticut use tax, Connecticut sales tax nexus, Connecticut sales tax returns, Connecticut exemption certificates, taxability of goods or services in Connecticut, Connecticut luxury tax, or any request involving Connecticut state-level consumption taxes. Trigger on phrases like "Connecticut sales tax", "CT sales tax", "Connecticut use tax", "Connecticut nexus", "C.G.S. 12-407", "Connecticut DRS", "luxury tax Connecticut", or any request involving Connecticut sales and use tax filing, classification, or compliance. NOTE: Connecticut has a luxury surcharge (7.75%) on items over $1,000 (jewelry, clothing, cars). ALWAYS read the parent us-sales-tax skill first for federal context.
---

# Connecticut Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Connecticut, United States |
| Jurisdiction Code | US-CT |
| Tax Type | Sales and Use Tax |
| Standard Rate | 6.35% |
| Luxury Rate | 7.75% (on certain items exceeding $1,000) |
| Maximum Combined Rate | 7.75% (no local taxes) |
| Primary Legal Framework | Connecticut General Statutes (C.G.S.) Chapter 219 (Section 12-407 et seq.) |
| Governing Body | Connecticut Department of Revenue Services (DRS) |
| Filing Portal | DRS myconneCT -- https://portal.ct.gov/DRS |
| Economic Nexus Effective Date | December 1, 2018 |
| SST Member | No |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate lookups, basic nexus, standard taxability, luxury rate application. Tier 2: SaaS classification, service taxability, luxury threshold edge cases. Tier 3: audit defense, penalty abatement, complex bundled transactions. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Connecticut sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Connecticut sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Connecticut? | Drives taxability classification under Connecticut law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Connecticut? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Connecticut local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 Standard Rate

Connecticut imposes a **6.35% state sales tax** with **no local sales taxes**.

**Statutory authority:** C.G.S. Section 12-408(1).

### 1.2 Luxury Rate -- 7.75%

Connecticut imposes an **elevated 7.75% rate** on certain luxury goods:

| Item | Threshold | Rate | Authority |
|------|-----------|------|-----------|
| Motor vehicles (purchase price portion over $50,000) | Over $50,000 | 7.75% on the excess | C.G.S. Section 12-408(1)(H) |
| Jewelry | Over $5,000 per item | 7.75% on entire price | C.G.S. Section 12-408(1)(E) |
| Clothing and footwear | Over $1,000 per item | 7.75% on entire price | C.G.S. Section 12-408(1)(F) |
| Handbags and luggage | Over $1,000 per item | 7.75% on entire price | C.G.S. Section 12-408(1)(F) |

**IMPORTANT:** The luxury rate application varies by item type. For motor vehicles, the standard 6.35% applies to the first $50,000 and 7.75% applies to the amount OVER $50,000. For jewelry, clothing over $1,000, etc., the 7.75% rate applies to the ENTIRE purchase price once the threshold is exceeded. [T1]

### 1.3 No Local Taxes

Connecticut does **not** permit local sales taxes. The rate is uniform statewide (6.35% standard or 7.75% luxury). [T1]

### 1.4 Sourcing Rules [T1]

Connecticut is a **destination-based** sourcing state:

- **Shipped goods:** Destination (ship-to address). [T1]
- **Over-the-counter:** Seller's location. [T1]
- **Digital goods:** Buyer's address. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 General Rule

Connecticut sales tax applies to the retail sale of tangible personal property, specified services, and certain digital products. C.G.S. Section 12-407(a)(2).

### 2.2 Taxability Matrix

| Item Category | Taxable? | Rate | Authority | Tier |
|---------------|----------|------|-----------|------|
| General tangible personal property | Yes | 6.35% | C.G.S. Section 12-408(1) | [T1] |
| Grocery food (food for home consumption) | **Exempt** | 0% | C.G.S. Section 12-412(13) | [T1] |
| Prepared food (restaurant meals) | Yes | 7.35% (meals tax) | C.G.S. Section 12-412(27) | [T1] |
| Clothing and footwear (under $1,000) | Yes | **6.35%** | C.G.S. Section 12-408(1) | [T1] |
| Clothing and footwear (over $1,000) | Yes | **7.75%** (luxury rate on entire price) | C.G.S. Section 12-408(1)(F) | [T1] |
| Prescription drugs | Exempt | 0% | C.G.S. Section 12-412(1) | [T1] |
| Over-the-counter drugs | Yes | 6.35% | Not specifically exempt | [T1] |
| Durable medical equipment | Exempt (certain items) | 0% | C.G.S. Section 12-412(4) | [T1] |
| Motor vehicles (under $50K) | Yes | 6.35% | C.G.S. Section 12-408(1) | [T1] |
| Motor vehicles (over $50K) | Yes | 6.35% on first $50K; 7.75% on excess | C.G.S. Section 12-408(1)(H) | [T1] |
| Gasoline and motor fuel | Exempt from sales tax (motor fuel tax) | N/A | C.G.S. Section 12-412(7) | [T1] |
| Utilities (residential) | Yes | 6.35% | C.G.S. Section 12-408 | [T1] |
| Utilities (commercial) | Yes | 6.35% | C.G.S. Section 12-408 | [T1] |
| Manufacturing machinery | Exempt | 0% | C.G.S. Section 12-412(18) | [T2] |
| Software -- canned | Yes | 6.35% | C.G.S. Section 12-407(a)(2) | [T1] |
| Software -- custom | Exempt | 0% | DRS guidance | [T2] |
| SaaS (Software as a Service) | **Taxable** | 6.35% (1% on certain SaaS with annual charges > $50K) | C.G.S. Section 12-407(a)(37) | [T2] |
| Digital goods | Yes | 6.35% | C.G.S. Section 12-407(a)(2)(CC) | [T1] |
| Data processing services | Taxable | 6.35% | C.G.S. Section 12-407(a)(37)(A) | [T2] |
| Computer and data services | Yes (1% rate on some services) | 1% or 6.35% | C.G.S. Section 12-408(1)(G) | [T2] |

### 2.3 Meals Tax (Prepared Food) [T1]

Connecticut imposes a **7.35% meals tax** (formerly 6.35%, increased effective October 1, 2019) on:

- Restaurant meals. [T1]
- Take-out food. [T1]
- Any food sold by an eating establishment. [T1]
- Catered food. [T1]
- **Groceries are exempt** -- the distinction is whether the food is "prepared" and sold by an "eating establishment." [T1]

### 2.4 SaaS and Computer Services [T2]

Connecticut taxes SaaS and computer services, with a complex rate structure:

- **Standard SaaS:** 6.35% (the standard rate applies to most SaaS products). [T2]
- **Computer and data processing services:** A **reduced 1% rate** applies to certain enumerated computer and data processing services (C.G.S. Section 12-408(1)(G)). [T2]
- Services qualifying for the 1% rate include data processing, computer programming (non-custom), web hosting, and similar services. [T2]
- The distinction between the 6.35% and 1% rate requires careful classification. [T3]

**Authority:** C.G.S. Section 12-407(a)(37); C.G.S. Section 12-408(1)(G).

### 2.5 Services Taxability [T2]

Connecticut taxes a wide range of services:

| Service | Taxable? | Rate | Authority |
|---------|----------|------|-----------|
| Telecommunications | Yes | 6.35% | C.G.S. Section 12-407(a)(2)(I) |
| Cable/satellite TV | Yes | 6.35% | C.G.S. Section 12-407(a)(2)(L) |
| Repair and maintenance of TPP | Yes | 6.35% | C.G.S. Section 12-407(a)(2)(E) |
| Computer services | Yes | 1% or 6.35% | C.G.S. Section 12-407(a)(37) |
| Motor vehicle parking | Yes | 6.35% | C.G.S. Section 12-407(a)(2)(G) |
| Hotel/lodging | Yes | 15% (special rate) | C.G.S. Section 12-407(a)(2)(B) |
| Laundry/dry cleaning | Yes | 6.35% | C.G.S. Section 12-407(a)(2)(D) |
| Interior design | Yes | 6.35% | C.G.S. Section 12-407(a)(37)(J) |
| Professional services (legal, accounting) | No | N/A | Not enumerated |
| Personal services (haircuts, spa) | No | N/A | Not enumerated |
| Construction | No (materials taxable at purchase) | N/A | DRS guidance |

---

## Step 3: Return Form Structure
### 3.1 Registration

All sellers with nexus must register with DRS for a **Sales and Use Tax Permit**. Registration through myconneCT.

**Authority:** C.G.S. Section 12-409.

### 3.2 Filing Frequency

| Monthly Tax Liability | Filing Frequency | Due Date |
|-----------------------|------------------|----------|
| Over $4,000 per month | Monthly | Last day of the following month |
| $1,000 -- $4,000 per month | Quarterly | Last day of month following quarter-end |
| Under $1,000 per month | Annual | January 31 |

### 3.3 Returns and Payment

- **Form OS-114** (Sales and Use Tax Return) is the primary return. [T1]
- Electronic filing through myconneCT is required. [T1]
- Payment due on the same date as the return. [T1]

### 3.4 Vendor Discount

Connecticut does **not** offer a vendor discount for timely filing. [T1]

### 3.5 Penalties and Interest

| Violation | Penalty | Authority |
|-----------|---------|-----------|
| Late filing | 10% of tax due, minimum $50 | C.G.S. Section 12-419 |
| Late payment | 15% of tax due | C.G.S. Section 12-419 |
| Failure to file | Estimated assessment + penalties | C.G.S. Section 12-415 |
| Fraud | 75% of deficiency | C.G.S. Section 12-419 |
| Interest | 1% per month | C.G.S. Section 12-419 |

---

## Step 4: Deductibility / Exemptions
### 5.1 Connecticut Exemption Certificates

| Certificate | Use Case | Authority |
|-------------|----------|-----------|
| **CERT-100** (Sales and Use Tax Exemption -- General) | Resale exemption | DRS |
| **CERT-101** | Exempt organization purchases | DRS |
| **CERT-102** | Government entity purchases | DRS |
| **CERT-104** | Manufacturing exemption | DRS |
| **CERT-119** | Resale (blanket certificate) | DRS |
| **SSTCE** | Multi-state (accepted) | DRS policy |

### 5.2 Requirements [T1]

Valid certificates must include: purchaser information, CT sales tax registration number (for resale), reason for exemption, description of goods, signature, date. [T1]

### 5.3 Good Faith and Retention [T2]

Good faith acceptance protects sellers. Certificates must be retained for **3 years** from the date of the last transaction. [T1]

---


### 6.1 When Use Tax Applies

Connecticut use tax applies when sales tax was not collected on items used, stored, or consumed in Connecticut. [T1]

### 6.2 Use Tax Rate

6.35% (standard) or 7.75% (luxury items). [T1]

### 6.3 Use Tax Reporting

- **Businesses:** Report on Form OS-114. [T1]
- **Individuals:** Report on Connecticut income tax return (Form CT-1040), Line 67. [T1]

---

## Step 5: Key Thresholds
### 4.1 Physical Nexus

Standard physical nexus principles apply. [T1]

### 4.2 Economic Nexus [T1]

Connecticut enacted economic nexus effective **December 1, 2018**.

| Threshold | Value | Measurement Period |
|-----------|-------|--------------------|
| Revenue | **$100,000** in gross sales into Connecticut | Previous 12 months |
| Transactions | **200 transactions** into Connecticut | Previous 12 months |
| Test | **AND** -- BOTH thresholds must be met | |

**CRITICAL:** Connecticut uses an **AND** test, not an OR test. A seller must meet BOTH the $100,000 revenue threshold AND the 200-transaction threshold to trigger economic nexus. This is more restrictive than most states. [T1]

**Authority:** C.G.S. Section 12-407(a)(12)(N).

### 4.3 Marketplace Facilitator Rules [T1]

Effective **December 1, 2018**:

- Marketplace facilitators meeting the nexus thresholds (AND test) must collect and remit. [T1]
- Marketplace sellers relieved for facilitated sales. [T1]

**Authority:** C.G.S. Section 12-408b.

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
1. **NEVER** advise that Connecticut has local sales taxes (it does not). [T1]
2. **NEVER** apply the standard 6.35% rate to clothing items over $1,000 (the 7.75% luxury rate applies). [T1]
3. **NEVER** apply the 7.75% luxury rate only to the excess over $1,000 for clothing (the rate applies to the ENTIRE price). [T1]
4. **NEVER** treat the motor vehicle luxury rate the same as the clothing luxury rate (vehicles use a split calculation). [T1]
5. **NEVER** advise that grocery food is taxable in Connecticut (it is exempt). [T1]
6. **NEVER** use an OR test for Connecticut economic nexus (Connecticut requires BOTH thresholds -- AND test). [T1]
7. **NEVER** advise that SaaS is not taxable in Connecticut (it is taxable). [T1]
8. **NEVER** apply the standard 6.35% rate to restaurant meals (meals are taxed at 7.35%). [T1]
9. **NEVER** advise that Connecticut offers a vendor discount (it does not). [T1]
10. **NEVER** apply the standard 6.35% rate to lodging (the rate is 15%). [T1]

---

## Edge Case Registry

### 7.1 Luxury Rate Application -- Motor Vehicles [T1]

The motor vehicle luxury rate has a unique split calculation:

- **First $50,000:** Taxed at 6.35%.
- **Excess over $50,000:** Taxed at 7.75%.
- **Example:** A $70,000 car: ($50,000 x 6.35%) + ($20,000 x 7.75%) = $3,175 + $1,550 = **$4,725**. [T1]

This is different from jewelry/clothing luxury, where the ENTIRE price is taxed at 7.75% once the threshold is exceeded. [T1]

### 7.2 Clothing Luxury Threshold [T1]

For clothing items over $1,000:

- The ENTIRE purchase price is taxed at 7.75%, not just the excess. [T1]
- A $999 jacket: 6.35%. A $1,001 jacket: 7.75% on the ENTIRE $1,001. [T1]
- This creates a "cliff effect" at the $1,000 threshold. [T1]

### 7.3 Lodging Tax [T1]

Connecticut imposes a **15% tax** on lodging (hotels, motels, B&Bs, short-term rentals):

- This is significantly higher than the standard 6.35% rate. [T1]
- Applies to stays of less than 30 consecutive days. [T1]
- Marketplace facilitators (Airbnb, VRBO) are responsible for collection. [T1]

### 7.4 Computer Services 1% Rate [T2]

The reduced 1% rate on certain computer services is complex:

- Qualifying services include: automatic data processing, computer programming, data hosting, web hosting, data storage, computer time rental. [T2]
- **Not all SaaS qualifies for 1%** -- many SaaS products are taxed at 6.35%. [T2]
- The classification requires careful analysis of the specific service provided. [T3]

### 7.5 Construction Contractors [T2]

- Contractors pay tax on materials at purchase. [T1]
- Construction services are not subject to sales tax. [T1]
- Fabrication labor may create taxable TPP. [T2]

### 7.6 Nonprofit Organizations [T2]

- Qualifying 501(c)(3) nonprofits may obtain a **CERT-119** exemption certificate for purchases. [T2]
- The exemption must be applied for and approved by DRS. [T1]
- Government entities use CERT-102. [T1]

### 7.7 AND Test Economic Nexus Implications [T1]

Connecticut's AND test creates unique planning considerations:

- A seller with $500,000 in revenue but only 100 transactions does NOT have nexus (fails the 200-transaction prong). [T1]
- A seller with 500 transactions but only $50,000 in revenue does NOT have nexus (fails the $100,000 revenue prong). [T1]
- This makes Connecticut harder to trigger than most states for economic nexus. [T1]

---

## Test Suite

### Test 1: Basic Rate Calculation [T1]

**Question:** A retailer sells a $400 kitchen appliance in Connecticut. What is the sales tax?

**Expected Answer:** $400 x 6.35% = $25.40.

### Test 2: Clothing Luxury Rate [T1]

**Question:** A customer buys a $1,200 designer jacket in Connecticut. What tax is due?

**Expected Answer:** Since the item exceeds $1,000, the luxury rate of 7.75% applies to the ENTIRE price: $1,200 x 7.75% = $93.00.

### Test 3: Motor Vehicle Luxury Rate [T1]

**Question:** A customer buys a $80,000 car in Connecticut. What sales tax is due?

**Expected Answer:** First $50,000 at 6.35% = $3,175. Excess $30,000 at 7.75% = $2,325. Total: $5,500.

### Test 4: AND Test Economic Nexus [T1]

**Question:** An out-of-state seller made $200,000 in sales but only 150 transactions in Connecticut. Does the seller have nexus?

**Expected Answer:** No. Connecticut uses an AND test. Although the $100,000 revenue threshold is met, the 200-transaction threshold is NOT met. Both must be satisfied.

### Test 5: SaaS Taxability [T2]

**Question:** A Connecticut business subscribes to a $300/month CRM SaaS tool. Is Connecticut sales tax due?

**Expected Answer:** Yes. SaaS is taxable in Connecticut at 6.35% (or potentially 1% if the service qualifies as a computer/data processing service). Tax at standard rate: $300 x 6.35% = $19.05/month.

### Test 6: Grocery Food vs. Meals [T1]

**Question:** A customer buys $100 in groceries and a $25 prepared sandwich from the deli counter. What tax is due?

**Expected Answer:** Groceries: exempt ($0). Prepared sandwich (meals tax): $25 x 7.35% = $1.84. Total: $1.84.

### Test 7: Lodging Tax [T1]

**Question:** A guest stays at a Connecticut hotel for 3 nights at $200/night. What tax is due?

**Expected Answer:** $600 x 15% = $90.00.

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
