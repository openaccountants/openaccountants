---
name: arizona-sales-tax
description: Use this skill whenever asked about Arizona sales tax, Arizona Transaction Privilege Tax (TPT), Arizona use tax, Arizona tax nexus, Arizona tax returns, Arizona exemption certificates, taxability of goods or services in Arizona, or any request involving Arizona state-level consumption taxes. Trigger on phrases like "Arizona sales tax", "AZ sales tax", "TPT", "Transaction Privilege Tax", "Arizona nexus", "A.R.S. Title 42", "Arizona DOR", or any request involving Arizona sales and use tax filing, classification, or compliance. CRITICAL: Arizona does NOT have a traditional "sales tax" -- it has a Transaction Privilege Tax (TPT) levied on the SELLER, not the buyer. ALWAYS read the parent us-sales-tax skill first for federal context, then layer this Arizona-specific skill on top.
---

# Arizona Transaction Privilege Tax (TPT) Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Arizona, United States |
| Jurisdiction Code | US-AZ |
| Tax Type | Transaction Privilege Tax (TPT) -- NOT a traditional sales tax |
| State TPT Rate | 5.6% |
| Maximum Combined Rate | Approximately 11.2% (varies by city/county) |
| Primary Legal Framework | Arizona Revised Statutes (A.R.S.) Title 42, Chapter 5 |
| Governing Body | Arizona Department of Revenue (ADOR) |
| Filing Portal | AZTaxes.gov -- https://www.aztaxes.gov |
| Economic Nexus Effective Date | October 1, 2019 |
| SST Member | No |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate lookups, basic nexus, standard TPT categories. Tier 2: contractor classification, city tax variations, SaaS/digital. Tier 3: audit defense, contractor disputes, complex multi-city analysis. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Arizona sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have an Arizona sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Arizona? | Drives taxability classification under Arizona law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Arizona? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Arizona local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 What Makes Arizona Unique: TPT vs. Sales Tax [T1]

Arizona does **NOT** have a traditional "sales tax." Instead, it imposes a **Transaction Privilege Tax (TPT)** -- a tax on the **seller's privilege of doing business** in Arizona.

**Key distinctions from traditional sales tax:**

| Feature | Traditional Sales Tax | Arizona TPT |
|---------|----------------------|-------------|
| Who is legally liable? | Buyer | **Seller** |
| Tax on what? | The purchase transaction | The **privilege of conducting business** |
| Can the seller pass it to the buyer? | Yes (required in most states) | Yes (optional -- seller may absorb) |
| Separately stated on invoice? | Required in most states | **Not required** (seller's choice) |
| Legal incidence | On the buyer | **On the seller** |

**Practical effect:** While the economic result is similar to a sales tax (the cost is typically passed to the buyer), the legal difference matters for contracts, exemptions, and audit purposes. [T1]

**Statutory authority:** A.R.S. Section 42-5008.

### 1.2 State Rate

The state TPT rate for the **Retail** classification is **5.6%**.

Arizona has **16 different TPT classifications**, each with its own rate and rules. The most common is the Retail classification.

| TPT Classification | State Rate | Common Applications |
|--------------------|-----------|---------------------|
| Retail | 5.6% | General retail sales of TPP |
| Contracting (prime) | 5.6% | Construction/contracting |
| Mining | 3.125% | Mining operations |
| Utilities | 5.6% | Utility services |
| Telecommunications | 5.6% | Phone, internet services |
| Transient Lodging | 5.5% | Hotels, motels, short-term rentals |
| Restaurant/Bar | 5.6% | Food service establishments |
| Rental of TPP | 5.6% | Equipment rental |
| MRRA (personal property rental) | 5.6% | Short-term rental platforms |
| Amusement | 5.6% | Entertainment, events |
| Publication | 5.6% | Print media |
| Online Lodging Marketplace | 5.5% | Airbnb, VRBO, etc. |

**Statutory authority:** A.R.S. Section 42-5010.

### 1.3 Local Taxes (City and County) [T2]

Cities and counties in Arizona levy their own TPT in addition to the state rate:

- **County TPT:** Generally 0.5% to 1.0%. [T1]
- **City TPT:** Ranges from 0% (unincorporated areas) to approximately 4.0%+. [T2]
- **Combined rates** can reach approximately **11.2%** in some jurisdictions. [T2]

**Important:** As of January 1, 2022, the Arizona Department of Revenue administers and collects **all** city and county TPT (previously, cities self-administered). This is known as the **Municipal Tax Code consolidation**. [T1]

### 1.4 Sourcing Rules [T1]

Arizona is generally an **origin-based** sourcing state:

- **Intrastate sales (in-person):** Tax based on the seller's business location. [T1]
- **Intrastate sales (shipped):** For state TPT, origin-based. For local city/county TPT, destination-based (effective January 2022 with Model City Tax Code changes). [T2]
- **Interstate sales (remote sellers):** Destination-based. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 General Rule

Arizona TPT applies to the gross receipts from conducting business in a taxable classification. The primary retail classification covers the sale of tangible personal property. A.R.S. Section 42-5061.

### 2.2 Taxability Matrix

| Item Category | Taxable? | Rate | Authority | Tier |
|---------------|----------|------|-----------|------|
| General tangible personal property | Yes | Full rate | A.R.S. Section 42-5061 | [T1] |
| Grocery food (food for home consumption) | **Exempt from state TPT** | 0% state (some cities tax food) | A.R.S. Section 42-5061(A)(1) | [T1] |
| Prepared food (restaurant meals) | Yes | Full rate (Restaurant classification) | A.R.S. Section 42-5074 | [T1] |
| Clothing and footwear | Yes | Full rate | No exemption | [T1] |
| Prescription drugs | Exempt | 0% | A.R.S. Section 42-5061(A)(6) | [T1] |
| Over-the-counter drugs | Yes | Full rate | Not specifically exempt | [T1] |
| Durable medical equipment | Exempt (prosthetic, orthotic, etc.) | 0% | A.R.S. Section 42-5061(A)(6) | [T1] |
| Motor vehicles | Yes | Full rate | A.R.S. Section 42-5061 | [T1] |
| Gasoline and motor fuel | Exempt from TPT (motor fuel excise tax applies) | N/A | A.R.S. Section 42-5061(A)(12) | [T1] |
| Residential utilities | Exempt from state TPT | 0% state | A.R.S. Section 42-5063 | [T1] |
| Commercial utilities | Yes | Full rate | A.R.S. Section 42-5063 | [T1] |
| Agricultural equipment and supplies | Exempt | 0% | A.R.S. Section 42-5061(B)(1) | [T1] |
| Machinery (manufacturing, R&D) | Exempt | 0% | A.R.S. Section 42-5061(B)(1) | [T2] |
| Software -- canned | Yes | Full rate | A.R.S. Section 42-5061 | [T1] |
| Software -- custom | Exempt | 0% | ADOR guidance | [T2] |
| SaaS (Software as a Service) | **Generally not taxable** | 0% | ADOR -- not considered TPP | [T2] |
| Digital goods | Not taxable at state level | 0% | Not defined as TPP | [T2] |
| Warranties (extended service contracts) | Yes | Full rate | A.R.S. Section 42-5061 | [T1] |

### 2.3 Grocery Food -- State vs. City [T1]

Arizona exempts grocery food from **state** TPT, but cities can and do tax food:

- **State TPT:** Grocery food exempt (A.R.S. Section 42-5061(A)(1)). [T1]
- **City TPT on food:** Some cities impose their city TPT on grocery food. Examples include some smaller municipalities. As of recent legislation, many major cities have reduced or eliminated food taxation, but verify by city. [T2]
- **Prepared food** is always taxable at both state and city levels. [T1]

### 2.4 Contractor/Construction Rules -- Unique to Arizona [T2]

Arizona has a specific **Contracting** TPT classification that is significantly different from how most states handle construction:

- **Prime contractors** are taxed on 65% of the contract price (a statutory reduction). [T2]
- **Subcontractors** are generally exempt if the prime contractor is paying TPT on the overall contract. [T2]
- **Owner-builders** have different rules. [T3]
- **Speculative builders** (building on their own land for sale) are taxed on the selling price minus land value. [T2]
- **MRRA (maintenance, repair, replacement, alteration):** Contractors performing MRRA work on existing structures are taxed differently from new construction. [T3]

**This is one of the most complex areas of Arizona TPT.** [T3]

**Authority:** A.R.S. Section 42-5075 (contracting classification).

### 2.5 Services Taxability [T2]

Arizona generally does NOT tax services unless they fall within a specific TPT classification:

| Service | Taxable? | Classification | Authority |
|---------|----------|----------------|-----------|
| Restaurant/food service | Yes | Restaurant | A.R.S. Section 42-5074 |
| Telecommunications | Yes | Telecom | A.R.S. Section 42-5064 |
| Rental of TPP | Yes | Personal Property Rental | A.R.S. Section 42-5071 |
| Transient lodging | Yes | Transient Lodging | A.R.S. Section 42-5070 |
| Amusement/entertainment | Yes | Amusements | A.R.S. Section 42-5073 |
| Construction/contracting | Yes | Contracting | A.R.S. Section 42-5075 |
| Professional services | No | N/A | Not a TPT classification |
| Personal services | No | N/A | Not a TPT classification |
| Repair of TPP | Parts: Yes (retail); Labor: Generally No | Retail (parts) | ADOR guidance |

---

## Step 3: Return Form Structure
### 3.1 Registration

All businesses conducting taxable activity in Arizona must obtain a **TPT license** before commencing business.

- Registration through AZTaxes.gov. [T1]
- A single TPT license covers state, county, and city TPT. [T1]
- License fee: None. [T1]

**Authority:** A.R.S. Section 42-5005.

### 3.2 Filing Frequency

| Monthly Tax Liability | Filing Frequency | Due Date |
|-----------------------|------------------|----------|
| Over $500 per month | Monthly | 20th of the following month |
| $50 -- $500 per month | Quarterly | 20th of month following quarter-end |
| Under $50 per month | Annual | 20th of the following month after year-end |

### 3.3 Returns and Payment

- **Form TPT-2** (Transaction Privilege Tax Return) -- filed through AZTaxes.gov. [T1]
- The return covers state, county, and city TPT (all administered by ADOR since Jan 2022). [T1]
- Electronic filing is mandatory for all filers. [T1]
- Payment due on the same date as the return. [T1]

### 3.4 Timely Filing Discount

Arizona does **not** offer a vendor discount for timely filing. [T1]

### 3.5 Penalties and Interest

| Violation | Penalty | Authority |
|-----------|---------|-----------|
| Late filing | 4.5% per month, up to 25% | A.R.S. Section 42-1125 |
| Late payment | 0.5% per month, up to 10% | A.R.S. Section 42-1125 |
| Failure to file | Estimated assessment + penalties | A.R.S. Section 42-1108 |
| Fraud | 50% of deficiency | A.R.S. Section 42-1125 |
| Interest | Published quarterly by ADOR | A.R.S. Section 42-1123 |

---

## Step 4: Deductibility / Exemptions
### 5.1 Arizona Exemption Certificates

| Certificate | Use Case | Authority |
|-------------|----------|-----------|
| **Form 5000** (TPT Exemption Certificate -- General) | Resale, exempt organizations, government | ADOR |
| **Form 5000A** | Contractor's exemption | ADOR |
| **Form 5000M** | Manufacturer's exemption | ADOR |
| **Form 5010** (Exemption Certificate for Other Government) | Government purchases | ADOR |

### 5.2 Requirements [T1]

Valid certificates must include purchaser information, reason for exemption, TPT license number (for resale), description of property, signature, and date. [T1]

### 5.3 Good Faith and Retention [T2]

Good faith acceptance protects sellers. Certificates must be retained for **4 years**. [T1]

---


### 6.1 Arizona Use Tax

Arizona use tax applies to purchases of TPP from out-of-state sellers who did not collect Arizona TPT:

- Rate: Same as applicable TPT rate (5.6% state + local). [T1]
- **Businesses:** Report on Form TPT-2. [T1]
- **Individuals:** Report on Arizona income tax return (Form 140). [T1]

**Authority:** A.R.S. Section 42-5155.

---

## Step 5: Key Thresholds
### 4.1 Physical Nexus

Standard physical nexus principles apply. [T1]

### 4.2 Economic Nexus [T1]

Arizona enacted economic nexus effective **October 1, 2019**.

| Threshold | Value | Measurement Period |
|-----------|-------|--------------------|
| Revenue | **$100,000** in gross receipts from Arizona | Previous or current calendar year |
| Transactions | N/A (revenue only -- Arizona dropped the transaction test) | |
| Test | Revenue only | |

**Authority:** A.R.S. Section 42-5008.

**Note:** Arizona initially included a 200-transaction threshold but subsequently dropped it, retaining only the $100,000 revenue threshold. [T1]

### 4.3 Marketplace Facilitator Rules [T1]

Effective **October 1, 2019**:

- Marketplace facilitators meeting the nexus threshold must collect and remit TPT. [T1]
- Marketplace sellers are relieved for facilitated sales. [T1]

**Authority:** A.R.S. Section 42-5014.

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
1. **NEVER** refer to Arizona's TPT as a "sales tax" without clarifying that it is a Transaction Privilege Tax levied on the seller, not the buyer. [T1]
2. **NEVER** advise that grocery food is taxable at the state level (it is exempt from state TPT). [T1]
3. **NEVER** assume all cities exempt grocery food -- some Arizona cities still tax food. [T2]
4. **NEVER** apply contracting rules without deep analysis -- Arizona contractor TPT is extremely complex. [T3]
5. **NEVER** forget that TPT is legally the seller's tax and may not be separately stated or passed through in all situations. [T1]
6. **NEVER** use a transaction-count threshold for Arizona economic nexus (Arizona uses revenue only). [T1]
7. **NEVER** advise that SaaS is taxable in Arizona under current state guidance. [T2]
8. **NEVER** ignore city-level taxes -- even though ADOR now administers them, city rates and rules vary significantly. [T1]
9. **NEVER** apply TPT to sales on tribal lands without careful analysis of tribal sovereignty issues. [T2]
10. **NEVER** advise that Arizona offers a vendor/timely-filing discount (it does not). [T1]

---

## Edge Case Registry

### 7.1 TPT as Seller's Tax -- Contract Implications [T2]

Because TPT is legally the seller's obligation (not the buyer's):

- Contracts should specify whether the quoted price includes or excludes TPT. [T2]
- Government contracts often require the seller to absorb TPT (no pass-through). [T2]
- If a contract is silent on TPT, the seller bears the burden. [T2]

### 7.2 Construction Contractor Classification [T3]

Arizona's contracting rules are among the most complex:

- Prime vs. subcontractor treatment. [T3]
- The 65% deduction for prime contractors on new construction. [T2]
- MRRA work has different rules than new construction. [T3]
- Materials vs. labor allocation. [T3]
- Speculative builder rules. [T3]

**Escalate all complex contractor questions to a licensed Arizona tax professional.** [T3]

### 7.3 Short-Term Rental (Airbnb/VRBO) [T2]

- Short-term rentals (less than 30 days) are subject to TPT under the Transient Lodging classification. [T1]
- State rate: 5.5% (slightly lower than the standard 5.6%). [T1]
- City and county lodging taxes also apply. [T1]
- Marketplace facilitators (Airbnb, VRBO) are responsible for collecting and remitting. [T1]

### 7.4 Tribal Lands [T2]

- Sales occurring on tribal (Native American reservation) land are generally NOT subject to Arizona state or local TPT. [T2]
- Tribes may impose their own transaction taxes. [T2]
- The seller's location determines whether TPT applies (if the seller is on tribal land, state TPT may not apply). [T3]

### 7.5 Jet Fuel and Aviation [T2]

- Jet fuel is exempt from TPT but subject to a separate use fuel tax. [T1]
- Aircraft sales are subject to TPT but certain exemptions exist for aircraft used in interstate commerce. [T2]

### 7.6 Data Center Equipment [T2]

Arizona provides TPT exemptions for qualifying data centers:

- Computer equipment purchased for qualifying data centers is exempt. [T2]
- Qualification requires a minimum investment threshold. [T2]

**Authority:** A.R.S. Section 42-5061(B)(17).

---

## Test Suite

### Test 1: Basic TPT Calculation [T1]

**Question:** A retailer in Phoenix (city rate ~2.3%, county ~0.7%) sells a $1,000 appliance. What is the approximate total TPT?

**Expected Answer:** State 5.6% + county ~0.7% + city ~2.3% = ~8.6%. Tax = $1,000 x 8.6% = approximately $86.00.

### Test 2: Grocery Food [T1]

**Question:** A grocery store in Tucson sells $500 of unprepared food. What state TPT is due?

**Expected Answer:** $0 state TPT. Grocery food is exempt from the 5.6% state TPT. City and county taxes may still apply depending on Tucson's current rules.

### Test 3: TPT Legal Incidence [T2]

**Question:** A contractor's bid of $100,000 to a government agency is silent on TPT. Who bears the TPT cost?

**Expected Answer:** The contractor. TPT is the seller's tax, and if the contract is silent, the contractor must absorb the TPT from the $100,000 contract price.

### Test 4: Economic Nexus [T1]

**Question:** An out-of-state seller made $80,000 in sales and 300 transactions in Arizona. Does the seller have economic nexus?

**Expected Answer:** No. Arizona's economic nexus threshold is $100,000 in revenue only. There is no transaction-count test. The seller does not have nexus.

### Test 5: Contractor TPT [T2]

**Question:** A prime contractor has a $500,000 contract for new commercial construction in Arizona. What is the TPT base?

**Expected Answer:** Under the contracting classification, the tax base is 65% of the contract price: $500,000 x 65% = $325,000. TPT at 5.6% state rate = $18,200 (plus county/city TPT on the same base).

### Test 6: SaaS [T2]

**Question:** An Arizona business subscribes to a $200/month cloud-based HR platform (SaaS). Is Arizona TPT due?

**Expected Answer:** No. SaaS is generally not subject to Arizona TPT as it is not considered tangible personal property.

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
