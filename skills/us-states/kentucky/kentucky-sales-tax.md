---
name: kentucky-sales-tax
description: Use this skill whenever asked about Kentucky sales tax, Kentucky use tax, Kentucky DOR sales tax filing, Kentucky services taxation expansion, or Kentucky sales tax compliance. Trigger on phrases like "Kentucky sales tax", "KY sales tax", "KRS §139", "Kentucky DOR", "Kentucky services tax", or any request involving Kentucky state sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
---

# Kentucky Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Kentucky, United States |
| Jurisdiction Code | US-KY |
| Tax Type | Sales and Use Tax (state only -- no local sales tax) |
| State Rate | 6.00% (flat, uniform statewide) |
| Local Rates | None |
| Primary Statute | Kentucky Revised Statutes (KRS) Chapter 139 |
| Governing Agency | Kentucky Department of Revenue (DOR) |
| Portal | https://revenue.ky.gov |
| SST Member | Yes -- Full Member |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | T1: state rate, basic taxability, filing mechanics. T2: newly taxable services (2023), SaaS classification, exemption specifics. T3: audit defense, complex transactions, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Kentucky sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Kentucky sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Kentucky? | Drives taxability classification under Kentucky law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Kentucky? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Kentucky local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Sales Tax Rate

Kentucky imposes a flat, uniform state sales tax of **6.00%** on the retail sale of tangible personal property and enumerated services. [T1]

**Statute:** KRS §139.200.

### 1.2 No Local Sales Taxes [T1]

Kentucky does NOT permit local sales taxes. The 6% rate is the total rate statewide. [T1]

This significantly simplifies compliance compared to states with local add-ons. [T1]

### 1.3 Sourcing [T1]

Kentucky uses **destination-based** sourcing. [T1]

As an SST member, Kentucky follows SSUTA sourcing rules. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 Grocery Food -- EXEMPT [T1]

- Unprepared grocery food and food ingredients: **exempt**. KRS §139.485. [T1]
- Prepared food (restaurant meals, heated food, food sold with utensils): taxable at 6%. [T1]
- Candy: taxable (excluded from the food exemption). [T1]
- Soft drinks: taxable. [T1]
- Kentucky follows SST definitions for food categories. [T1]

### 2.2 Clothing [T1]

- Clothing is **fully taxable** at 6%. No exemption. [T1]

### 2.3 Prescription Drugs and Medical [T1]

- Prescription drugs: **exempt**. KRS §139.472(1). [T1]
- OTC drugs: **exempt**. KRS §139.472(2). [T1]
- DME: exempt with prescription. [T1]
- Prosthetics, hearing aids: exempt. [T1]

### 2.4 Services -- Expanded Taxation (2023) [T2]

**Effective January 1, 2023, Kentucky significantly expanded sales tax to cover numerous services previously exempt.** This was enacted by HB 8 (2022).

**Newly taxable services (2023):**
- Photography and photo finishing [T1]
- Marketing services (advertising-related) [T2]
- Telemarketing [T1]
- Bodywork therapy (massage, etc.) [T1]
- Cosmetic surgery (non-medical) [T2]
- Small animal veterinary services [T1]
- Pet care services (grooming, boarding) [T1]
- Industrial laundry and dry cleaning [T1]
- Limousine services [T1]
- Fitness and recreational sports [T1]
- Golf (green fees, cart rental, range fees) [T1]
- Campground rental [T1]
- Overnight trailer park rental [T1]
- Bowling alley fees [T1]
- Skilled nursing (non-medical, private pay) [T2]
- Executive search/recruitment services [T2]
- Testing laboratory services (non-medical) [T2]

**Still exempt services:**
- Legal services [T1]
- Accounting/CPA services [T1]
- Medical services (physician, dental, hospital) [T1]
- Engineering and architectural services [T1]
- Financial services [T1]
- Educational services [T1]
- Residential cleaning [T2]
- IT and computer services (not specifically enumerated) [T2]

**Statute:** KRS §139.200 as amended by HB 8 (2022).

### 2.5 SaaS and Digital Goods [T2]

- **SaaS:** Generally **not taxable** under current KY law. Not specifically enumerated as a taxable service or TPP. [T2]
- **Canned software (physical):** Taxable. [T1]
- **Canned software (electronic delivery):** Taxable. KRS §139.010(40). [T1]
- **Digital downloads:** Taxable (digital property is taxable in Kentucky). [T1]
- **Streaming services:** Taxable as digital property. [T2]
- **Custom software:** Exempt. [T2]

### 2.6 Manufacturing [T1]

- Machinery and equipment used in manufacturing: **exempt**. KRS §139.480(10). [T1]
- Raw materials incorporated into finished products for resale: exempt. [T1]
- Industrial supplies consumed in manufacturing: exempt. [T1]
- Energy used in manufacturing: reduced rate on portion used in production. [T2]

### 2.7 Agricultural [T1]

- Farm machinery and equipment: exempt. KRS §139.480(6). [T1]
- Feed, seed, fertilizer: exempt. [T1]
- Livestock for breeding: exempt. [T1]

---

## Step 3: Return Form Structure
### 4.1 Filing Details [T1]

| Field | Detail |
|-------|--------|
| Return Form | Form 51A102 (Sales and Use Tax Return) |
| Filing Frequencies | Monthly (>$400/month average liability); Quarterly; Annually (small sellers) |
| Due Date | 20th of the month following the reporting period |
| Portal | https://revenue.ky.gov (Kentucky Taxpayer Online) |
| E-filing | Required for most filers |

### 4.2 Vendor Discount [T1]

Kentucky offers a vendor compensation (timely filing discount) of **1.75%** of the first $1,000 of tax due per reporting period (maximum $17.50/period). [T1]

**Statute:** KRS §139.570.

### 4.3 Penalties and Interest [T1]

- Late filing penalty: 2% of tax due per month (first month), 10% per month thereafter, up to 20% total. [T1]
- Late payment penalty: included in the above. [T1]
- Interest: 12% per annum on underpayments. [T1]

---

## Step 4: Deductibility / Exemptions
Exemptions identified in Step 2 above are the primary deductibility rules for Kentucky. Key categories: [T1]

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
| Revenue Threshold | $100,000 in Kentucky sales |
| Transaction Threshold | 200 transactions |
| Test | OR (either threshold triggers nexus) |
| Measurement Period | Current or prior calendar year |
| Effective Date | October 1, 2018 |

**Statute:** KRS §139.340(2).

### 3.2 Physical Nexus [T1]

Standard physical nexus rules apply. [T1]

### 3.3 Marketplace Facilitator [T1]

Kentucky requires marketplace facilitators to collect and remit sales tax. KRS §139.340(4). [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- NEVER apply local tax add-ons in Kentucky. There are NO local sales taxes. The rate is 6% statewide. [T1]
- NEVER assume all services are exempt in Kentucky. HB 8 (2022) significantly expanded taxable services effective 2023. [T1]
- NEVER tax large animal (livestock) veterinary services. Only small animal (pet) vet services are taxable. [T2]
- NEVER assume SaaS is taxable in Kentucky. Current law does not specifically enumerate SaaS. [T2]
- NEVER forget that OTC drugs are exempt in Kentucky, unlike most states. [T1]
- NEVER ignore the 2023 service expansion when advising service businesses in Kentucky. Many businesses that never collected tax before must now do so. [T1]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude. [T1]

---

## Edge Case Registry

### EC1 -- Newly Taxable Services (2023 Expansion) [T2]

**Situation:** A fitness center that previously did not collect sales tax now must collect 6% on memberships and class fees.

**Resolution:**
- Effective January 1, 2023, fitness and recreational sports services became taxable. [T1]
- The fitness center must register (if not already) and collect 6% on membership fees, class fees, personal training, and related charges. [T1]
- Fees for purely educational classes (e.g., nutrition classes without fitness component) may remain exempt. [T2]
- **Flag for reviewer:** Review all revenue streams to determine which are newly taxable under HB 8. Some services have nuanced classification. [T2]

### EC2 -- Veterinary Services Classification [T2]

**Situation:** A veterinarian provides medical treatment for a dog ($200 surgery) and grooming services ($50). Are both taxable?

**Resolution:**
- Small animal veterinary services became taxable in 2023. KRS §139.200 as amended. [T1]
- Both the veterinary medical services and grooming are taxable at 6%. [T1]
- Large animal (livestock) veterinary services remain exempt (agricultural exemption). [T2]
- **Flag for reviewer:** Distinguish between small animal (pet) and large animal (livestock) veterinary services. [T2]

### EC3 -- Marketing vs. Advertising Services [T2]

**Situation:** A marketing agency provides strategic marketing consulting and produces advertising materials for a Kentucky client.

**Resolution:**
- "Marketing services" as defined under HB 8 are taxable when related to advertising, promotion, or communications. [T2]
- Pure strategic consulting (market research, brand strategy) may or may not fall within the statutory definition. [T2]
- Production of advertising materials (tangible output) is taxable. [T1]
- **Flag for reviewer:** The boundary between taxable "marketing services" and exempt professional consulting is not well-defined. Review specific service descriptions against KY DOR guidance. [T2]

### EC4 -- Uniform Statewide Rate Advantage [T1]

**Situation:** A multi-state seller asks whether Kentucky requires rate lookups by address.

**Resolution:**
- Kentucky has NO local sales taxes. The rate is a flat 6% statewide. [T1]
- Sellers do NOT need address-level rate lookups for Kentucky. [T1]
- This makes Kentucky one of the simplest states for rate determination. [T1]
- Tax = sales price x 6%, regardless of location within Kentucky. [T1]

---

### EC5 -- Massage Therapy vs. Medical Services [T2]

**Situation:** A massage therapist provides both therapeutic massage (medical referral) and relaxation massage. Are both taxable?

**Resolution:**
- Bodywork therapy (including massage) became taxable in 2023 under HB 8. [T1]
- Medical services provided by licensed healthcare professionals under a medical referral may be exempt. [T2]
- Relaxation massage without medical referral: taxable. [T1]
- The distinction between medical and non-medical massage is fact-specific. [T2]
- **Flag for reviewer:** Review whether the massage is provided under a medical referral and by a licensed healthcare professional. The exemption boundary is not well-defined. [T2]

### EC6 -- Pet Boarding During Travel vs. Veterinary Boarding [T2]

**Situation:** A pet owner boards their dog at a veterinary clinic during vacation. Is the boarding taxable?

**Resolution:**
- Pet care services (grooming, boarding) became taxable in 2023. [T1]
- Boarding at a veterinary clinic for medical observation after surgery: may be part of an exempt medical service. [T2]
- Boarding at a veterinary clinic for convenience (owner traveling): taxable as pet care. [T1]
- **Flag for reviewer:** The purpose of boarding determines taxability. Medical necessity vs. convenience. [T2]

---

## Test Suite

### Test 1 -- Basic Taxable Sale

**Input:** Seller in Louisville sells $1,000 of electronics to a local buyer. KY rate = 6%.
**Expected output:** Tax = $1,000 x 6% = $60.00. Total = $1,060.00.

### Test 2 -- Grocery Food Exemption

**Input:** Customer buys $150 of unprepared groceries in Lexington. KY rate = 6%.
**Expected output:** Groceries are EXEMPT. Tax = $0. Total = $150.00.

### Test 3 -- Newly Taxable Fitness Service

**Input:** Gym charges $50/month membership to a Bowling Green member. KY rate = 6%.
**Expected output:** Fitness services are taxable (effective 2023). Tax = $50 x 6% = $3.00. Total = $53.00.

### Test 4 -- Veterinary Services

**Input:** Vet charges $300 for dog surgery in Frankfort. KY rate = 6%.
**Expected output:** Small animal vet services are taxable. Tax = $300 x 6% = $18.00. Total = $318.00.

### Test 5 -- Prescription and OTC Drug Exemption

**Input:** Pharmacy sells $100 prescription drug and $25 OTC medicine. KY rate = 6%.
**Expected output:** Both are exempt in Kentucky. Tax = $0. Total = $125.00.

---

### Test 6 -- Pet Grooming (Newly Taxable)

**Input:** Pet grooming salon charges $60 for dog grooming in Covington. KY rate = 6%.
**Expected output:** Pet grooming is taxable (2023+). Tax = $60 x 6% = $3.60. Total = $63.60.

### Test 7 -- Golf Green Fees (Newly Taxable)

**Input:** Golfer pays $75 for 18 holes at a Lexington course. KY rate = 6%.
**Expected output:** Golf fees are taxable (2023+). Tax = $75 x 6% = $4.50. Total = $79.50.

### Test 8 -- Legal Services (Still Exempt)

**Input:** Attorney bills $5,000 for legal services in Louisville. KY rate = 6%.
**Expected output:** Legal services remain EXEMPT. Tax = $0. Total = $5,000.

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
