---
name: missouri-sales-tax
description: Use this skill whenever asked about Missouri sales tax, Missouri use tax, Missouri sales tax nexus, Missouri sales tax returns, Missouri exemption certificates, taxability of goods or services in Missouri, or any request involving Missouri state-level consumption taxes. Trigger on phrases like "Missouri sales tax", "MO sales tax", "Missouri use tax", "Missouri nexus", "RSMo 144", "Missouri DOR sales tax", or any request involving Missouri sales and use tax filing, classification, or compliance. NOTE: Missouri was the LAST state to enact economic nexus (effective Jan 1, 2023). ALWAYS read the parent us-sales-tax skill first for federal context.
---

# Missouri Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Missouri, United States |
| Jurisdiction Code | US-MO |
| Tax Type | Sales and Use Tax |
| State Tax Rate | 4.225% |
| Maximum Combined Rate | Approximately 10.85% (varies by locality) |
| Primary Legal Framework | Revised Statutes of Missouri (RSMo) Chapter 144 |
| Governing Body | Missouri Department of Revenue (MODOR) |
| Filing Portal | MyTax Missouri -- https://mytax.mo.gov |
| Economic Nexus Effective Date | January 1, 2023 (last state to enact) |
| SST Member | No |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate lookups, basic nexus, standard taxability. Tier 2: local rate complexity, food rate distinctions, SaaS classification. Tier 3: audit defense, penalty abatement, multi-jurisdiction local tax disputes. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Missouri sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Missouri sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Missouri? | Drives taxability classification under Missouri law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Missouri? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Missouri local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Rate

Missouri imposes a **4.225% state sales tax**. This rate consists of:

- **3.0%** general revenue. [T1]
- **1.0%** education/conservation. [T1]
- **0.125%** parks/soils. [T1]
- **0.10%** transportation. [T1]

**Statutory authority:** RSMo Section 144.020.

### 1.2 Local Rates

Missouri has an extremely complex local sales tax structure:

| Tax Layer | Rate Range | Authority |
|-----------|-----------|-----------|
| State tax | 4.225% | RSMo Section 144.020 |
| County tax | 0.5% -- 2.5% | RSMo Section 67.500 et seq. |
| City tax | 0.5% -- 3.0%+ | RSMo Section 94.500 et seq. |
| Special district (CID, TDD, TIF) | 0.25% -- 1.0%+ | Various |
| **Maximum combined** | **~10.85%** | |

**Jurisdictions with the highest rates:** Certain areas in St. Louis County, Kansas City, and Springfield can exceed 10%. [T1]

Missouri has **over 2,500 local tax jurisdictions** -- one of the highest numbers in the US. [T1]

### 1.3 Food Rate -- Reduced [T1]

Missouri taxes grocery food at a **reduced state rate of 1.225%** (compared to 4.225% for general merchandise):

- The reduction is on the **state portion only** (the 3.0% general revenue portion is removed). [T1]
- Local taxes still apply to food at their full rates. [T1]
- The total rate on food = 1.225% state + applicable local rates. [T1]

**Authority:** RSMo Section 144.014.

### 1.4 Sourcing Rules [T1]

Missouri is an **origin-based** sourcing state for intrastate sales:

- **Intrastate over-the-counter:** Seller's location. [T1]
- **Intrastate shipped:** Origin-based (seller's location). [T1]
- **Interstate (remote sellers):** Destination-based. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 General Rule

Missouri sales tax applies to the retail sale of tangible personal property and certain specifically enumerated services. RSMo Section 144.020.

### 2.2 Taxability Matrix

| Item Category | Taxable? | Rate | Authority | Tier |
|---------------|----------|------|-----------|------|
| General tangible personal property | Yes | Full rate | RSMo Section 144.020 | [T1] |
| Grocery food (food for home consumption) | Yes (reduced state rate) | **1.225% state** + local | RSMo Section 144.014 | [T1] |
| Prepared food (restaurant meals) | Yes | Full rate | RSMo Section 144.020 | [T1] |
| Clothing and footwear | Yes | Full rate | No exemption | [T1] |
| Prescription drugs | Exempt | 0% | RSMo Section 144.030(2)(18) | [T1] |
| Over-the-counter drugs | Yes | Full rate | Not specifically exempt | [T1] |
| Durable medical equipment | Exempt (certain items) | 0% | RSMo Section 144.030(2)(19) | [T1] |
| Motor vehicles | Yes | Full rate | RSMo Section 144.020 | [T1] |
| Gasoline and motor fuel | Exempt from sales tax (motor fuel tax) | N/A | RSMo Section 144.030(2)(3) | [T1] |
| Utilities (residential electricity) | Yes | Full rate | RSMo Section 144.020 | [T1] |
| Utilities (commercial) | Yes | Full rate | RSMo Section 144.020 | [T1] |
| Manufacturing equipment (direct use) | Exempt | 0% | RSMo Section 144.030(2)(5) | [T2] |
| Agricultural supplies and equipment | Exempt | 0% | RSMo Section 144.030(2)(1)-(2) | [T1] |
| Software -- canned (tangible medium) | Yes | Full rate | RSMo Section 144.020 | [T1] |
| Software -- canned (electronic delivery) | Yes | Full rate | MODOR guidance | [T2] |
| Software -- custom | Exempt | 0% | MODOR Letter Ruling | [T2] |
| SaaS (Software as a Service) | **Not taxable** | 0% | MODOR -- not TPP, not enumerated service | [T2] |
| Digital goods (downloads) | Not specifically taxable | 0% | Not defined as TPP in MO statute | [T2] |
| Newspapers | Exempt | 0% | RSMo Section 144.030(2)(9) | [T1] |

### 2.3 Grocery Food -- Reduced but Not Exempt [T1]

Missouri taxes food but at a reduced rate:

- **State portion:** 1.225% (instead of 4.225%). [T1]
- **Local taxes:** Apply at their normal rates. [T1]
- **Prepared food:** Taxed at the full rate (no reduction). [T1]
- **Net effect:** A consumer in a city with 4% local tax pays 1.225% + 4% = 5.225% on groceries vs. 4.225% + 4% = 8.225% on general merchandise. [T1]

### 2.4 SaaS -- Not Taxable [T2]

Missouri does **not** tax SaaS:

- SaaS is not considered tangible personal property under Missouri law. [T2]
- SaaS is not an enumerated taxable service. [T2]
- Digital goods generally are not taxable in Missouri unless they involve the transfer of TPP. [T2]

### 2.5 Services Taxability [T2]

Missouri taxes very few services:

| Service | Taxable? | Authority |
|---------|----------|-----------|
| Telecommunications | Yes | RSMo Section 144.020 |
| Cable/satellite TV | Yes | RSMo Section 144.020 |
| Repair of TPP (parts only) | Parts: Yes; Labor: No (if separately stated) | RSMo Section 144.020 |
| Hotel/lodging | Yes (plus local transient guest taxes) | RSMo Section 144.020 |
| Professional services | No | Not enumerated |
| Personal services | No | Not enumerated |
| Construction | No (materials taxable at purchase) | MODOR guidance |
| Transportation/freight | Exempt (if separately stated) | RSMo Section 144.034 |

---

## Step 3: Return Form Structure
### 3.1 Registration

All sellers with nexus must register with MODOR for a **Sales Tax License**. Registration through MyTax Missouri.

**Fee:** $25 bond may be required. [T1]

**Authority:** RSMo Section 144.083.

### 3.2 Filing Frequency

| Monthly Tax Liability | Filing Frequency | Due Date |
|-----------------------|------------------|----------|
| Over $500 per month | Monthly | Last day of the following month |
| $100 -- $500 per month | Quarterly | Last day of month following quarter-end |
| Under $100 per month | Quarterly | Last day of month following quarter-end |

**Note:** MODOR generally assigns monthly or quarterly filing. Annual filing is not standard. [T1]

### 3.3 Returns and Payment

- **Form 53-1** (Sales/Use Tax Return) is the primary return. [T1]
- Electronic filing through MyTax Missouri is available and encouraged. [T1]
- Payment due on the same date as the return. [T1]
- Both state and state-administered local taxes are reported on the same return. [T1]

### 3.4 Timely Filing Discount

Missouri provides a **timely payment allowance** of **2%** of the tax due, up to **$500 per filing period**. [T1]

**Authority:** RSMo Section 144.140.

### 3.5 Penalties and Interest

| Violation | Penalty | Authority |
|-----------|---------|-----------|
| Late filing | 5% per month, up to 25% | RSMo Section 144.250 |
| Late payment | Same as late filing | RSMo Section 144.250 |
| Failure to file | Estimated assessment + penalties | RSMo Section 144.250 |
| Fraud | 50% of deficiency | RSMo Section 144.250 |
| Interest | Statutory rate (~4%) | RSMo Section 32.065 |

---

## Step 4: Deductibility / Exemptions
### 5.1 Missouri Exemption Certificates

| Certificate | Use Case | Authority |
|-------------|----------|-----------|
| **Form 149** (Sales and Use Tax Exemption Certificate) | General exemption (resale, exempt organizations, manufacturing, agricultural, government) | MODOR |
| **SSTCE** | Multi-state (accepted even though MO is not SST) | MODOR policy |

### 5.2 Requirements [T1]

Valid certificates must include: purchaser information, Missouri tax ID number (for resale), reason for exemption, description of goods, signature, date. [T1]

### 5.3 Good Faith and Retention [T1]

Good faith acceptance protects sellers. Certificates must be retained for **3 years** from the date of the last transaction. [T1]

---


### 6.1 When Use Tax Applies

Missouri use tax applies when sales tax was not collected on items used in Missouri. [T1]

### 6.2 Use Tax Rate

4.225% state + applicable local. [T1]

### 6.3 Use Tax Reporting

- **Businesses:** Report on Form 53-1. [T1]
- **Individuals:** Report on Missouri income tax return (Form MO-1040). [T1]

---

## Step 5: Key Thresholds
### 4.1 Physical Nexus

Standard physical nexus principles apply. [T1]

### 4.2 Economic Nexus [T1]

Missouri was the **last state** to enact economic nexus, effective **January 1, 2023**.

| Threshold | Value | Measurement Period |
|-----------|-------|--------------------|
| Revenue | **$100,000** in gross sales into Missouri | Previous 12 months |
| Transactions | N/A (revenue only) | |
| Test | Revenue only | |

**Authority:** RSMo Section 144.605.1.

### 4.3 Marketplace Facilitator Rules [T1]

Effective **January 1, 2023** (same date as economic nexus):

- Marketplace facilitators meeting the nexus threshold must collect and remit. [T1]
- Marketplace sellers relieved for facilitated sales. [T1]

**Authority:** RSMo Section 144.752.

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
1. **NEVER** advise that grocery food is exempt in Missouri (it is taxed at a reduced state rate of 1.225% + local). [T1]
2. **NEVER** advise that SaaS is taxable in Missouri (it is not). [T1]
3. **NEVER** provide a combined rate without verifying the specific address for local taxes -- Missouri has 2,500+ jurisdictions. [T1]
4. **NEVER** forget that Missouri was the last state to adopt economic nexus (Jan 1, 2023). [T1]
5. **NEVER** use a transaction-count threshold for Missouri economic nexus (revenue only, $100K). [T1]
6. **NEVER** ignore CID/TDD taxes when determining the rate at a specific seller location. [T2]
7. **NEVER** advise that Missouri uses destination-based sourcing for intrastate sales (it uses origin-based). [T1]
8. **NEVER** advise that Missouri is an SST member (it is not). [T1]
9. **NEVER** assume the sales tax holiday includes local tax exemption (local participation is optional). [T2]
10. **NEVER** quote only the 4.225% state rate when asked "what is the sales tax in Missouri" without noting that local taxes typically add 2-6%+ more. [T1]

---

## Edge Case Registry

### 7.1 Local Tax Complexity [T2]

Missouri's 2,500+ local jurisdictions create significant compliance challenges:

- A single street address may be subject to city, county, and multiple special district taxes. [T2]
- Rate changes occur frequently (quarterly in some jurisdictions). [T2]
- MODOR provides a rate lookup tool by address. [T1]
- For intrastate shipped sales, origin-based sourcing adds complexity (the seller's location rate applies, not the buyer's). [T1]

### 7.2 Community Improvement Districts (CIDs) and Transportation Development Districts (TDDs) [T2]

Missouri allows the creation of special taxing districts:

- **CIDs:** An additional sales tax to fund community improvements (sidewalks, lighting, etc.). [T2]
- **TDDs:** An additional tax to fund transportation projects. [T2]
- These taxes are layered on top of state, county, and city taxes. [T2]
- A seller located in a CID/TDD must collect the additional tax on all sales at that location. [T1]

### 7.3 Late Economic Nexus Adoption [T1]

Missouri's January 2023 adoption of economic nexus means:

- Before 2023, remote sellers without physical nexus were NOT required to collect Missouri sales tax. [T1]
- This was a significant compliance change for remote sellers. [T1]
- The marketplace facilitator law also took effect simultaneously. [T1]

### 7.4 Motor Vehicle Sales [T1]

- Motor vehicles taxable at full combined rate. [T1]
- Tax paid at DMV (Department of Revenue license office) when titling. [T1]
- Trade-in credits reduce the taxable base. [T1]

### 7.5 Manufacturing Exemption [T2]

Missouri provides a manufacturing exemption:

- Machinery and equipment used directly in manufacturing, mining, or fabricating. [T2]
- Raw materials incorporated into finished product. [T1]
- Utilities used in manufacturing (reduced rate or exempt). [T2]

**Authority:** RSMo Section 144.030(2)(5).

### 7.6 Agricultural Exemptions [T1]

Missouri provides broad agricultural exemptions:

- Farm machinery and equipment. [T1]
- Feed, seed, and fertilizer. [T1]
- Pesticides and herbicides. [T1]
- Livestock. [T1]

**Authority:** RSMo Section 144.030(2)(1)-(2).

### 7.7 Back-to-School Sales Tax Holiday [T1]

Missouri holds an annual sales tax holiday (typically the first weekend of August):

- Clothing ($100 or less per item): exempt from state tax. [T1]
- School supplies ($50 or less per item): exempt from state tax. [T1]
- Computer software ($350 or less per item): exempt from state tax. [T1]
- Computers ($1,500 or less): exempt from state tax. [T1]
- Local participation is optional. [T2]

---

## Test Suite

### Test 1: Basic Rate Calculation [T1]

**Question:** A retailer in Kansas City (combined local rate ~5.1%) sells a $300 item. What is the approximate total tax?

**Expected Answer:** State 4.225% + local ~5.1% = ~9.325%. Tax = $300 x 9.325% = approximately $27.98.

### Test 2: Grocery Food Rate [T1]

**Question:** A consumer buys $200 of groceries in a city with 3.5% combined local tax. What tax is due?

**Expected Answer:** State: $200 x 1.225% = $2.45. Local: $200 x 3.5% = $7.00. Total: $9.45.

### Test 3: SaaS Taxability [T2]

**Question:** A Missouri business subscribes to a $500/month SaaS platform. Is Missouri sales tax due?

**Expected Answer:** No. SaaS is not taxable in Missouri.

### Test 4: Economic Nexus [T1]

**Question:** An out-of-state seller made $120,000 in sales and 50 transactions in Missouri. Does the seller have nexus?

**Expected Answer:** Yes. Missouri uses a revenue-only threshold of $100,000. Transaction count is irrelevant.

### Test 5: Origin-Based Sourcing [T1]

**Question:** A Missouri seller in Springfield (combined rate ~8.1%) ships a product to a buyer in rural Missouri (combined rate ~6.0%). What rate applies?

**Expected Answer:** For intrastate shipped sales, Missouri uses origin-based sourcing. The Springfield rate (~8.1%) applies.

### Test 6: Late Adopter Context [T1]

**Question:** Did a remote seller without physical presence need to collect Missouri sales tax in 2022?

**Expected Answer:** No. Missouri did not enact economic nexus until January 1, 2023 -- the last state to do so. Before that date, only sellers with physical nexus in Missouri were required to collect.

### Test 7: Vendor Discount [T1]

**Question:** A monthly filer remits $8,000 in Missouri sales tax on time. What discount applies?

**Expected Answer:** 2% of $8,000 = $160. Since this is under the $500 cap, the full $160 discount applies. Remittance: $8,000 - $160 = $7,840.

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
