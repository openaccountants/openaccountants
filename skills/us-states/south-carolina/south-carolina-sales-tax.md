---
name: south-carolina-sales-tax
description: Use this skill whenever asked about South Carolina sales tax, South Carolina use tax, SC sales tax nexus, SC sales tax returns, SC exemption certificates, taxability of goods or services in South Carolina, or any request involving South Carolina state-level consumption taxes. Trigger on phrases like "South Carolina sales tax", "SC sales tax", "SC use tax", "SC nexus", "S.C. Code 12-36", "SC DOR sales tax", or any request involving South Carolina sales and use tax filing, classification, or compliance. NOTE: SC has a max tax cap of $500 on certain items (vehicles, boats, aircraft). ALWAYS read the parent us-sales-tax skill first for federal context.
---

# South Carolina Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | South Carolina, United States |
| Jurisdiction Code | US-SC |
| Tax Type | Sales and Use Tax |
| State Tax Rate | 6% |
| Maximum Combined Rate | 9% (6% state + up to 3% local) |
| Primary Legal Framework | South Carolina Code of Laws, Title 12, Chapter 36 (Section 12-36-10 et seq.) |
| Governing Body | South Carolina Department of Revenue (SCDOR) |
| Filing Portal | MyDORWAY -- https://mydorway.dor.sc.gov |
| Economic Nexus Effective Date | November 1, 2018 |
| SST Member | No |
| Notable Feature | $500 max tax cap on motor vehicles, boats, aircraft, manufactured homes |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate lookups, basic nexus, standard taxability, max tax cap. Tier 2: SaaS classification, local penny tax, service taxability. Tier 3: audit defense, penalty abatement, complex multi-jurisdiction analysis. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any South Carolina sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a South Carolina sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in South Carolina? | Drives taxability classification under South Carolina law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in South Carolina? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple South Carolina local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Rate

South Carolina imposes a **6% state sales and use tax** on the retail sale of tangible personal property and certain services.

**Statutory authority:** S.C. Code Section 12-36-910.

### 1.2 Local Rates

Counties in South Carolina may levy additional local sales taxes (commonly called "penny taxes"):

| Tax Component | Rate Range | Authority |
|---------------|-----------|-----------|
| State tax | 6% | S.C. Code Section 12-36-910 |
| Local option (county) | 1% -- 3% | S.C. Code Section 4-10 (various articles) |
| **Maximum combined** | **9%** | |

Common local tax types:

- **Capital Projects Sales Tax** (1%): For specific capital improvement projects, approved by referendum. [T1]
- **Transportation Penny Tax** (1%): For transportation infrastructure. [T1]
- **Local Option Tax** (1%): General county use, with property tax rollback. [T1]

Not all counties levy local taxes. Many counties have one or two local levies; some have none. [T1]

### 1.3 Max Tax Cap -- Critical Feature [T1]

South Carolina caps the **state** sales tax at **$500** on certain items:

| Item | Max State Tax | Authority |
|------|---------------|-----------|
| Motor vehicles | $500 | S.C. Code Section 12-36-2110(A) |
| Boats and watercraft | $500 | S.C. Code Section 12-36-2110(A) |
| Aircraft | $500 | S.C. Code Section 12-36-2110(A) |
| Manufactured homes | $500 | S.C. Code Section 12-36-2110(A) |
| Motorcycles | $500 | S.C. Code Section 12-36-2110(A) |
| Recreational vehicles | $500 | S.C. Code Section 12-36-2110(A) |

**How the cap works:**

- The maximum **state** sales tax on these items is $500, regardless of the purchase price. [T1]
- $500 / 6% = $8,333. So for items priced at $8,333 or less, the full 6% applies. For items over $8,333, the state tax is capped at $500. [T1]
- **Local taxes** are NOT subject to the cap and apply to the full purchase price. [T1]

**Example:** A $50,000 vehicle in a county with 2% local tax: State tax = $500 (capped). Local tax = $50,000 x 2% = $1,000. Total tax = $1,500. [T1]

### 1.4 Sourcing Rules [T1]

South Carolina is a **destination-based** sourcing state:

- **Shipped goods:** Destination (ship-to address). [T1]
- **Over-the-counter:** Seller's location. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 General Rule

South Carolina sales tax applies to the retail sale of tangible personal property and certain services. S.C. Code Section 12-36-910.

### 2.2 Taxability Matrix

| Item Category | Taxable? | Rate | Authority | Tier |
|---------------|----------|------|-----------|------|
| General tangible personal property | Yes | Full rate | S.C. Code Section 12-36-910 | [T1] |
| Grocery food (food for home consumption) | **Exempt** | 0% | S.C. Code Section 12-36-2120(75) | [T1] |
| Prepared food (restaurant meals) | Yes | Full rate | S.C. Code Section 12-36-910 | [T1] |
| Clothing and footwear | Yes | Full rate | No exemption | [T1] |
| Prescription drugs | Exempt | 0% | S.C. Code Section 12-36-2120(28) | [T1] |
| Over-the-counter drugs | Exempt | 0% | S.C. Code Section 12-36-2120(28)(c) | [T1] |
| Durable medical equipment | Exempt (with prescription) | 0% | S.C. Code Section 12-36-2120(28) | [T1] |
| Motor vehicles | Yes (subject to $500 cap on state tax) | 6% capped at $500 state | S.C. Code Section 12-36-2110(A) | [T1] |
| Gasoline and motor fuel | Exempt from sales tax (motor fuel excise) | N/A | S.C. Code Section 12-36-2120(16) | [T1] |
| Utilities (residential electricity) | Yes | Full rate | S.C. Code Section 12-36-910 | [T1] |
| Utilities (commercial) | Yes | Full rate | S.C. Code Section 12-36-910 | [T1] |
| Manufacturing equipment (direct use) | Exempt | 0% | S.C. Code Section 12-36-2120(17) | [T2] |
| Agricultural supplies and equipment | Exempt | 0% | S.C. Code Section 12-36-2120(14)-(15) | [T1] |
| Software -- canned (tangible medium) | Yes | Full rate | S.C. Code Section 12-36-910 | [T1] |
| Software -- canned (electronic delivery) | Yes | Full rate | SCDOR Revenue Ruling 16-2 | [T2] |
| Software -- custom | Exempt | 0% | SCDOR guidance | [T2] |
| SaaS (Software as a Service) | **Not taxable** | 0% | SCDOR -- not TPP; Revenue Ruling 19-1 | [T2] |
| Digital goods (electronically delivered) | Not specifically taxable | 0% | Not defined as TPP | [T2] |
| Newspapers (printed) | Exempt | 0% | S.C. Code Section 12-36-2120(4) | [T1] |

### 2.3 Grocery Food Exemption [T1]

South Carolina fully exempts **unprepared food** (food for home consumption) from sales tax:

- The exemption applies to food eligible for purchase with SNAP/EBT. [T1]
- **Prepared food** remains fully taxable. [T1]
- **Candy** and **soft drinks** are treated as food (exempt). [T1]
- Local taxes may still apply to food in some jurisdictions. [T2]

**Authority:** S.C. Code Section 12-36-2120(75).

### 2.4 SaaS -- Not Taxable [T2]

South Carolina does **not** tax SaaS:

- SaaS is not considered tangible personal property under SC law. [T2]
- Revenue Ruling 19-1 confirmed that remotely accessed software does not constitute a taxable sale. [T2]
- Canned software delivered electronically IS taxable, but SaaS (where the software resides on the vendor's server) is distinguished. [T2]

### 2.5 Services Taxability [T2]

South Carolina taxes certain enumerated services:

| Service | Taxable? | Authority |
|---------|----------|-----------|
| Telecommunications | Yes | S.C. Code Section 12-36-910 |
| Cable/satellite TV | Yes | S.C. Code Section 12-36-910 |
| Repair and maintenance of TPP | Parts: Yes; Labor: Yes (total charge taxable) | S.C. Code Section 12-36-910(B) |
| Hotel/lodging | Yes (plus local accommodations tax) | S.C. Code Section 12-36-920 |
| Laundry/dry cleaning | Yes | S.C. Code Section 12-36-910(B)(3) |
| Electricity/gas utility service | Yes | S.C. Code Section 12-36-910 |
| Professional services (legal, accounting) | No | Not enumerated |
| Personal services (haircuts, spa) | No | Not enumerated |
| Construction/real property | No (materials taxable at purchase) | SCDOR guidance |
| Transportation/freight | Exempt (if separately stated) | S.C. Code Section 12-36-2120(66) |

---

## Step 3: Return Form Structure
### 3.1 Registration

All sellers with nexus must register with SCDOR for a **Retail License**. Registration through MyDORWAY.

**Fee:** $50 per retail location. [T1]

**Authority:** S.C. Code Section 12-36-510.

### 3.2 Filing Frequency

South Carolina assigns **monthly** filing for all active registrants:

| Filing Status | Frequency | Due Date |
|---------------|-----------|----------|
| All registrants | Monthly | 20th of the following month |

**Note:** South Carolina does NOT offer quarterly or annual filing for general sales tax. All filers file monthly. [T1]

### 3.3 Returns and Payment

- **Form ST-3** (State Sales, Use and Accommodations Tax Return) is the primary return. [T1]
- Electronic filing through MyDORWAY is required. [T1]
- Payment due by the 20th of the following month. [T1]
- Both state and state-administered local taxes are reported on the same return. [T1]

### 3.4 Timely Filing Discount

South Carolina provides a **timely payment discount** of **3%** of the first $100 of tax due per return period (maximum $3 per period). The discount is minimal. [T1]

**Authority:** S.C. Code Section 12-36-2610.

### 3.5 Penalties and Interest

| Violation | Penalty | Authority |
|-----------|---------|-----------|
| Late filing | 5% per month, up to 25% | S.C. Code Section 12-54-43 |
| Late payment | 0.5% per month, up to 25% | S.C. Code Section 12-54-43 |
| Failure to file | Estimated assessment + penalties | S.C. Code Section 12-54-44 |
| Fraud | 75% of deficiency | S.C. Code Section 12-54-43 |
| Interest | Federal underpayment rate | S.C. Code Section 12-54-25 |

---

## Step 4: Deductibility / Exemptions
### 5.1 South Carolina Exemption Certificates

| Certificate | Use Case | Authority |
|-------------|----------|-----------|
| **Form ST-8A** (Resale Certificate) | Purchases for resale | SCDOR |
| **Form ST-8F** (Exempt Organization Certificate) | Nonprofit/government purchases | SCDOR |
| **Form ST-8B** (Manufacturing Exemption) | Manufacturing equipment | SCDOR |
| **SSTCE** | Multi-state (accepted) | SCDOR policy |

### 5.2 Requirements [T1]

Valid certificates must include: purchaser information, SC retail license number (for resale), reason for exemption, description of goods, signature, date. [T1]

### 5.3 Good Faith and Retention [T1]

Good faith acceptance protects sellers. Certificates must be retained for **3 years** from the date of the last transaction. [T1]

---


### 6.1 When Use Tax Applies

SC use tax applies when sales tax was not collected on items used, stored, or consumed in South Carolina. [T1]

### 6.2 Use Tax Rate

6% state + applicable local. The $500 cap applies to qualifying items for use tax as well. [T1]

### 6.3 Use Tax Reporting

- **Businesses:** Report on Form ST-3. [T1]
- **Individuals:** Report on SC income tax return (Form SC1040), Line 19. [T1]

---

## Step 5: Key Thresholds
### 4.1 Physical Nexus

Standard physical nexus principles apply. [T1]

### 4.2 Economic Nexus [T1]

South Carolina enacted economic nexus effective **November 1, 2018**.

| Threshold | Value | Measurement Period |
|-----------|-------|--------------------|
| Revenue | **$100,000** in gross sales into South Carolina | Previous or current calendar year |
| Transactions | N/A (revenue only) | |
| Test | Revenue only | |

**Authority:** S.C. Code Section 12-36-71.

### 4.3 Marketplace Facilitator Rules [T1]

Effective **April 26, 2019**:

- Marketplace facilitators meeting the nexus threshold must collect and remit. [T1]
- Marketplace sellers relieved for facilitated sales. [T1]

**Authority:** S.C. Code Section 12-36-71(H).

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
1. **NEVER** apply full 6% state tax to motor vehicles, boats, or aircraft over $8,333 (the $500 cap applies). [T1]
2. **NEVER** advise that grocery food is taxable in SC (it is exempt). [T1]
3. **NEVER** advise that SaaS is taxable in SC (it is not). [T1]
4. **NEVER** tell a seller they can file quarterly in SC -- all filers file monthly. [T1]
5. **NEVER** apply the $500 cap to local taxes (only the state tax is capped). [T1]
6. **NEVER** use a transaction-count threshold for SC economic nexus (revenue only, $100K). [T1]
7. **NEVER** ignore local "penny taxes" -- they can add up to 3% on top of the 6% state rate. [T1]
8. **NEVER** advise that repair labor is exempt in SC (the total charge for repair, including labor, is taxable). [T1]
9. **NEVER** exempt casual sales of motor vehicles (they are always subject to tax). [T1]
10. **NEVER** forget the $50 per-location retail license fee when advising on registration. [T1]

---

## Edge Case Registry

### 7.1 Max Tax Cap Calculations [T1]

The $500 cap creates significant tax savings on high-value items:

| Purchase Price | Uncapped State Tax (6%) | Capped State Tax | Savings |
|---------------|------------------------|-------------------|---------|
| $10,000 | $600 | $500 | $100 |
| $25,000 | $1,500 | $500 | $1,000 |
| $50,000 | $3,000 | $500 | $2,500 |
| $100,000 | $6,000 | $500 | $5,500 |
| $500,000 | $30,000 | $500 | $29,500 |

**Local taxes still apply to the full purchase price.** [T1]

### 7.2 Accommodations Tax [T1]

South Carolina imposes a separate **accommodations tax** on short-term rentals:

- **State:** 7% (2% more than the general 5% sales tax base -- effectively 7% state rate on lodging). [T1]
- Actually, accommodations are taxed at the 6% state sales tax PLUS a 2% state accommodations tax = 8% total state. [T2]
- Local accommodations taxes also apply (vary by county). [T2]
- Marketplace facilitators collect on short-term rental platforms. [T1]

### 7.3 Manufacturing Exemptions [T2]

South Carolina provides manufacturing exemptions:

- Machines used in manufacturing, processing, fabrication. [T2]
- Raw materials incorporated into finished products. [T1]
- Electricity used in manufacturing (reduced rate). [T2]
- Pollution control equipment. [T2]

**Authority:** S.C. Code Section 12-36-2120(17).

### 7.4 Casual/Occasional Sales [T1]

South Carolina exempts casual or occasional sales by persons not regularly engaged in business:

- The exemption does NOT apply to motor vehicles, boats, aircraft, or manufactured homes (always subject to tax, even between private parties). [T1]
- Private party vehicle sales: $500 max tax cap still applies. [T1]

### 7.5 Construction Contractors [T2]

- Contractors pay tax on materials at purchase. [T1]
- Contractors do NOT collect sales tax on real property improvements. [T1]
- Prefabricated components may have different treatment. [T2]

### 7.6 Repair Services -- Total Charge [T1]

Unlike many states that only tax parts, South Carolina taxes the **total charge** for repair and maintenance of TPP:

- Both labor and parts are taxable. [T1]
- The tax applies to the total invoice amount. [T1]
- This is important for auto repair shops, appliance repair, and similar businesses. [T1]

### 7.7 Sales Tax Holiday [T1]

South Carolina holds an annual sales tax holiday (typically the first weekend of August):

- Clothing (any price): exempt from state and local tax. [T1]
- School supplies: exempt. [T1]
- Computers ($1,000 or less): exempt. [T1]
- Bed and bath items: exempt. [T1]
- SC's holiday is broader than most states (no price cap on clothing). [T1]

---

## Test Suite

### Test 1: Basic Rate Calculation [T1]

**Question:** A retailer in Charleston County (2% local) sells a $800 television. What is the total sales tax?

**Expected Answer:** State: $800 x 6% = $48. Local: $800 x 2% = $16. Total: $64.

### Test 2: Max Tax Cap on Vehicle [T1]

**Question:** A customer buys a $45,000 car in a county with 1% local tax. What is the total sales tax?

**Expected Answer:** State: $500 (capped). Local: $45,000 x 1% = $450 (no cap on local). Total: $950.

### Test 3: Grocery Food Exemption [T1]

**Question:** A consumer buys $200 of groceries in Greenville County. What tax is due?

**Expected Answer:** $0. Grocery food is exempt from both state and local sales tax in SC.

### Test 4: SaaS Taxability [T2]

**Question:** A SC business subscribes to a $400/month SaaS accounting platform. Is SC sales tax due?

**Expected Answer:** No. SaaS is not taxable in South Carolina per Revenue Ruling 19-1.

### Test 5: Economic Nexus [T1]

**Question:** An out-of-state seller made $110,000 in SC sales and 50 transactions. Does the seller have nexus?

**Expected Answer:** Yes. SC uses a revenue-only threshold of $100,000. Transaction count is irrelevant.

### Test 6: Repair Services [T1]

**Question:** An auto repair shop charges $300 for labor and $400 for parts to fix a transmission in SC. What tax is due?

**Expected Answer:** The entire $700 (labor + parts) is taxable. Tax = $700 x 8% (example with 2% local) = $56.

### Test 7: Boat Purchase Cap [T1]

**Question:** A customer buys a $200,000 boat in a county with 2% local tax. What is the total tax?

**Expected Answer:** State: $500 (capped). Local: $200,000 x 2% = $4,000. Total: $4,500. Without the cap, state tax alone would have been $12,000.

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
