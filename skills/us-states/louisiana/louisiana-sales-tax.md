---
name: louisiana-sales-tax
description: Use this skill whenever asked about Louisiana sales tax, Louisiana use tax, Louisiana sales tax nexus, Louisiana sales tax returns, Louisiana exemption certificates, taxability of goods or services in Louisiana, Louisiana Sales Tax Commission, parish tax administration, or any request involving Louisiana state-level consumption taxes. Trigger on phrases like "Louisiana sales tax", "LA sales tax", "Louisiana use tax", "Louisiana nexus", "R.S. 47:301", "Louisiana DOR sales tax", "parish sales tax", "Sales Tax Commission", or any request involving Louisiana sales and use tax filing, classification, or compliance. CRITICAL: Louisiana has one of the MOST COMPLEX local sales tax structures in the US -- parishes self-administer local taxes with their own collectors. Combined rates can be the HIGHEST in the US (up to ~11.45%). ALWAYS read the parent us-sales-tax skill first for federal context.
---

# Louisiana Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Louisiana, United States |
| Jurisdiction Code | US-LA |
| Tax Type | Sales and Use Tax |
| State Tax Rate | 4.45% |
| Maximum Combined Rate | Approximately 11.45% (among highest in US) |
| Primary Legal Framework | Louisiana Revised Statutes (R.S.) 47:301 et seq. |
| State Governing Body | Louisiana Department of Revenue (LDR) |
| Local Tax Administration | Parish and municipal tax collectors (NOT administered by the state) |
| Remote Seller Commission | Louisiana Sales and Use Tax Commission for Remote Sellers |
| Filing Portal (state) | Louisiana File Online -- https://revenue.louisiana.gov |
| Filing Portal (remote sellers) | Louisiana Sales Tax Commission -- https://www.lstc.la.gov |
| Economic Nexus Effective Date | July 1, 2020 |
| SST Member | No |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: state rate lookups, basic nexus, standard taxability. Tier 2: parish-level tax variations, food taxation at local level, dual-administration complexity. Tier 3: audit defense by multiple authorities, penalty abatement, parish-specific rulings. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Louisiana sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Louisiana sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Louisiana? | Drives taxability classification under Louisiana law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Louisiana? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Louisiana local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Rate

Louisiana imposes a **4.45% state sales tax** (reduced from 5% effective July 1, 2018).

**Statutory authority:** R.S. 47:302, 47:321, 47:321.1, 47:331.

**Note:** The 4.45% state rate is composed of multiple levies:

- 2% general fund (R.S. 47:302). [T1]
- 1% education (R.S. 47:321). [T1]
- 0.45% transportation (R.S. 47:321.1). [T1]
- 1% SAVE (R.S. 47:331) -- temporary but repeatedly extended. [T1]

### 1.2 Local Rates -- Parish and Municipal

This is where Louisiana becomes one of the **most complex** sales tax states:

| Tax Layer | Rate Range | Authority |
|-----------|-----------|-----------|
| State tax | 4.45% | R.S. 47:302 et seq. |
| Parish (county equivalent) tax | 1% -- 5%+ | Parish ordinances |
| Municipal (city) tax | 0% -- 3%+ | City ordinances |
| Special district tax | 0% -- 1%+ | District legislation |
| **Maximum combined** | **~11.45%** | |

**Louisiana can have the highest combined sales tax rates in the entire United States.** [T1]

### 1.3 Dual Administration -- The Core Complexity [T2]

Louisiana is **unique** in that local sales taxes are NOT administered by the state:

| Tax Level | Administrator | Where to File |
|-----------|---------------|---------------|
| **State** (4.45%) | Louisiana Department of Revenue (LDR) | Louisiana File Online |
| **Local** (parish/city) | Individual parish/city tax collectors (there are 64 parishes, many with their own collector) | Filed with each local collector |
| **Remote sellers** (state + local) | Louisiana Sales and Use Tax Commission for Remote Sellers | LSTC portal (single filing for remote sellers) |

**Critical implications:**

- **In-state sellers** must file **two separate returns**: one with LDR (state) and one with the local parish/city tax collector. [T2]
- Each of the **64 parishes** may have its own tax collector, its own forms, its own due dates, and its own audit process. [T2]
- **Remote sellers** can use the **Louisiana Sales Tax Commission (LSTC)** as a single point of filing for both state and local taxes. This was established to simplify compliance for out-of-state sellers. [T1]
- The LSTC applies a **single blended local rate** by parish for remote seller purposes, which may differ slightly from the actual rate charged by local collectors. [T2]

### 1.4 Sourcing Rules [T1]

Louisiana uses **destination-based** sourcing:

- **Shipped goods:** Destination (ship-to address). [T1]
- **Over-the-counter:** Seller's location. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 General Rule

Louisiana sales tax applies to the retail sale of tangible personal property and the sale of certain services. R.S. 47:301(10), 47:302.

### 2.2 Taxability Matrix

| Item Category | Taxable? | Rate | Authority | Tier |
|---------------|----------|------|-----------|------|
| General tangible personal property | Yes | Full rate | R.S. 47:302 | [T1] |
| Grocery food (food for home consumption) | **Exempt from state tax** | 0% state; local varies | R.S. 47:305(D)(1)(n-r) | [T1] |
| Prepared food (restaurant meals) | Yes | Full rate | R.S. 47:302 | [T1] |
| Clothing and footwear | Yes | Full rate | No exemption | [T1] |
| Prescription drugs | Exempt | 0% | R.S. 47:305(D)(1)(c) | [T1] |
| Over-the-counter drugs | Yes | Full rate | Not specifically exempt | [T1] |
| Durable medical equipment | Exempt (certain items) | 0% | R.S. 47:305(D)(1)(d) | [T1] |
| Motor vehicles | Yes | Full rate | R.S. 47:302 | [T1] |
| Gasoline and motor fuel | Exempt from sales tax (motor fuel excise) | N/A | R.S. 47:305(D)(1)(g) | [T1] |
| Utilities (residential -- first $15/month natural gas, first 1,000 kWh electricity) | Exempt (state only) | 0% state | R.S. 47:305.28 | [T1] |
| Utilities (commercial) | Yes | Full rate | R.S. 47:302 | [T1] |
| Manufacturing equipment (direct use) | Exempt (state only; local may still tax) | 0% state | R.S. 47:301(3)(i) | [T2] |
| Agricultural supplies and equipment | Exempt | 0% | R.S. 47:305(A) | [T1] |
| Software -- canned (tangible medium) | Yes | Full rate | R.S. 47:301(16) | [T1] |
| Software -- canned (electronic delivery) | Yes | Full rate | LDR Revenue Ruling 09-001 | [T2] |
| Software -- custom | Exempt | 0% | LDR guidance | [T2] |
| SaaS (Software as a Service) | **Taxability unclear** | Depends on facts | LDR has issued conflicting guidance | [T3] |
| Digital goods (downloads) | Yes (taxable as TPP) | Full rate | LDR Revenue Ruling 09-001 | [T2] |
| Newspapers (print) | Exempt | 0% | R.S. 47:305(D)(1)(a) | [T1] |

### 2.3 Grocery Food -- State vs. Local Divergence [T1]

Louisiana exempts grocery food from the **state** 4.45% sales tax, but local treatment varies:

- **State tax:** Exempt on food for home consumption. [T1]
- **Local taxes:** Many parishes STILL tax grocery food at their full local rate. [T2]
- Some parishes have voluntarily exempted food from their local taxes. [T2]
- **Net effect:** A consumer may pay 0% state tax on groceries but 3-5%+ in local taxes depending on the parish. [T2]

**Authority:** R.S. 47:305(D)(1)(n-r).

### 2.4 SaaS Taxability -- Uncertain [T3]

Louisiana's position on SaaS is unclear and potentially conflicting:

- LDR has issued guidance suggesting that electronically delivered software is taxable. [T2]
- However, the application to true SaaS (remote access, no download) is less clear. [T3]
- Individual parish tax collectors may take their own positions on SaaS. [T3]
- **Escalate all SaaS taxability questions in Louisiana to a licensed tax professional.** [T3]

### 2.5 Services Taxability [T2]

Louisiana taxes certain enumerated services:

| Service | Taxable? | Authority |
|---------|----------|-----------|
| Telecommunications | Yes | R.S. 47:301(14) |
| Cable/satellite TV | Yes | R.S. 47:301(14) |
| Repair and maintenance of TPP | Parts: Yes; Labor: Generally No (if separately stated) | R.S. 47:301(3) |
| Hotel/lodging | Yes (plus state and local occupancy taxes) | R.S. 47:301(6) |
| Laundry/dry cleaning | Yes | R.S. 47:301(14)(g) |
| Printing services | Yes | R.S. 47:301(14)(e) |
| Cold storage/warehousing | Yes | R.S. 47:301(14)(k) |
| Professional services (legal, accounting) | No | Not enumerated |
| Personal services (haircuts, spa) | No | Not enumerated |
| Construction/real property | No (materials taxable at purchase) | LDR guidance |
| Transportation/freight | Exempt (if separately stated) | R.S. 47:301(3) |

---

## Step 3: Return Form Structure
### 3.1 Registration

- **State:** Register with LDR for a state sales tax license. [T1]
- **Local:** Register separately with each parish/city tax collector where you have nexus (in-state sellers). [T2]
- **Remote sellers:** Register with the Louisiana Sales and Use Tax Commission (LSTC). [T1]

**Authority:** R.S. 47:306.

### 3.2 Filing Frequency

**State returns (with LDR):**

| Monthly Tax Liability | Filing Frequency | Due Date |
|-----------------------|------------------|----------|
| Over $500 per month | Monthly | 20th of the following month |
| Under $500 per month | Quarterly | 20th of month following quarter-end |

**Local returns:** Each parish/city collector sets its own filing frequency and due dates. Many require monthly filing by the 20th of the following month, but **this varies by collector.** [T2]

**Remote sellers (through LSTC):** Monthly or quarterly, filed with the Commission. [T1]

### 3.3 Returns and Payment

- **State:** Filed electronically through Louisiana File Online. [T1]
- **Local (in-state sellers):** Filed with each parish/city collector, often through Parish E-File or paper returns. [T2]
- **Remote sellers:** Filed through the LSTC portal. [T1]

### 3.4 Vendor Discount

Louisiana provides a **vendor's compensation** of **1.1%** of the tax collected (state portion only) for timely filing. No stated cap. [T1]

**Authority:** R.S. 47:306(A)(3)(a).

### 3.5 Penalties and Interest

| Violation | Penalty | Authority |
|-----------|---------|-----------|
| Late filing | 5% per month, up to 25% | R.S. 47:1602 |
| Late payment | 5% per month, up to 25% | R.S. 47:1602 |
| Negligence | 5% of tax due | R.S. 47:1604 |
| Fraud | 50% of deficiency | R.S. 47:1604 |
| Interest | Rate set annually by LDR (approximately 6%) | R.S. 47:1601 |

**Note:** Local collectors may impose their own separate penalties and interest. [T2]

---

## Step 4: Deductibility / Exemptions
### 5.1 Louisiana Exemption Certificates

| Certificate | Use Case | Authority |
|-------------|----------|-----------|
| **Form R-1048** (Certificate of Exemption/Exclusion) | Resale, exempt organizations, manufacturing | LDR |
| **Form R-1059** (Resale Certificate -- Specific) | Single-purchase resale certificate | LDR |
| **SSTCE** | Multi-state (may be accepted -- verify with collector) | LDR/local policy |

### 5.2 Dual Certificate Requirements [T2]

Because state and local taxes are separately administered:

- A state exemption certificate (accepted by LDR) may NOT be accepted by a local parish collector. [T2]
- Some local collectors have their own exemption certificate forms. [T2]
- **Best practice:** Obtain both a state and local exemption certificate, or use a certificate that both authorities accept. [T2]

### 5.3 Requirements and Retention [T1]

Standard requirements: name, address, registration number (for resale), reason for exemption, description of goods, signature, date. Certificates must be retained for **3 years** from the date of the last transaction. [T1]

---


### 6.1 When Use Tax Applies

Louisiana use tax applies when sales tax was not collected on items used in Louisiana. [T1]

### 6.2 Use Tax Rate

4.45% state + applicable local rates. [T1]

### 6.3 Use Tax Reporting

- **Businesses (state):** Report on state return with LDR. [T1]
- **Businesses (local):** Report on local returns with parish collectors. [T2]
- **Individuals:** Report on Louisiana income tax return. [T1]

---

## Step 5: Key Thresholds
### 4.1 Physical Nexus

Standard physical nexus principles apply. [T1]

### 4.2 Economic Nexus [T1]

Louisiana enacted economic nexus effective **July 1, 2020**.

| Threshold | Value | Measurement Period |
|-----------|-------|--------------------|
| Revenue | **$100,000** in gross sales into Louisiana | Previous or current calendar year |
| Transactions | **200 transactions** into Louisiana | Previous or current calendar year |
| Test | **OR** -- either threshold triggers nexus | |

**Authority:** R.S. 47:301(4)(m).

### 4.3 Remote Seller Filing Simplification [T1]

Remote sellers who trigger economic nexus can file through the **Louisiana Sales and Use Tax Commission (LSTC)** rather than filing separately with LDR and each local collector:

- The LSTC serves as a single point of filing for both state and local taxes. [T1]
- The Commission applies a unified local rate by parish for remote sellers. [T1]
- This was a critical simplification -- without it, remote sellers would need to potentially register with 64 parish collectors. [T1]

**Authority:** R.S. 47:339.

### 4.4 Marketplace Facilitator Rules [T1]

Effective **July 1, 2020**:

- Marketplace facilitators meeting the nexus threshold must collect and remit. [T1]
- Marketplace sellers relieved for facilitated sales. [T1]
- Marketplace facilitators file through the LSTC. [T1]

**Authority:** R.S. 47:301(4)(m)(ii).

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
1. **NEVER** advise that grocery food is fully exempt in Louisiana without specifying this applies to STATE tax only -- local parishes may still tax food. [T1]
2. **NEVER** tell an in-state seller they only need to file one return (they must file state AND local separately). [T2]
3. **NEVER** provide a combined rate without verifying the specific parish and municipality -- Louisiana has extreme rate variation. [T1]
4. **NEVER** advise that SaaS is definitively taxable or not taxable in Louisiana (the position is unclear -- escalate). [T3]
5. **NEVER** assume a state exemption certificate is accepted by local collectors (it may not be). [T2]
6. **NEVER** forget that Louisiana can have the HIGHEST combined sales tax rates in the US (up to ~11.45%). [T1]
7. **NEVER** tell a remote seller they need to file with 64 parish collectors (the LSTC provides single-point filing for remote sellers). [T1]
8. **NEVER** apply manufacturing exemptions to local taxes without verifying the specific parish's rules. [T2]
9. **NEVER** advise that Louisiana is an SST member (it is not). [T1]
10. **NEVER** underestimate the compliance complexity of Louisiana -- it has one of the most complex sales tax systems in the entire US. [T1]

---

## Edge Case Registry

### 7.1 Dual-Filing Burden for In-State Sellers [T2]

In-state Louisiana sellers face a unique compliance burden:

- File state return with LDR. [T1]
- File local return(s) with parish/city tax collector(s). [T2]
- If a seller has locations or delivers in multiple parishes, it may need to file with MULTIPLE local collectors. [T2]
- Each collector may have different forms, rules, and audit schedules. [T2]
- This is one of the most burdensome compliance environments for in-state sellers in the entire US. [T1]

### 7.2 State vs. Local Exemption Conflicts [T2]

Louisiana's dual-administration system creates situations where an item is:

- **Exempt from state tax but taxable at the local level** (e.g., manufacturing equipment, grocery food in many parishes). [T2]
- **Taxable at the state level but exempt at the local level** (less common). [T2]
- Sellers must track these differences and apply the correct exemptions to the state and local portions separately. [T2]

### 7.3 Manufacturing Exemption -- State Only [T2]

Louisiana's manufacturing exemption is generally limited to the **state** tax:

- Manufacturing machinery is exempt from the 4.45% state tax. [T2]
- Local parishes may or may NOT exempt manufacturing equipment. [T2]
- This means a manufacturer may still owe 3-5%+ in local taxes on exempt equipment. [T2]

### 7.4 Tourism and Hospitality [T2]

Louisiana (and particularly New Orleans) has high combined lodging and sales taxes:

- State sales tax: 4.45%. [T1]
- State occupancy tax: 4%. [T1]
- New Orleans city/parish occupancy and sales taxes: can add 6-8%+. [T2]
- Total effective tax on hotel rooms in New Orleans can exceed 15%. [T2]

### 7.5 Private Right of Action by Local Collectors [T3]

Louisiana local collectors have an unusual power: they can pursue legal action independently of LDR to collect unpaid local taxes. This means:

- A seller could face audit and legal action from LDR AND from local collectors simultaneously. [T3]
- Local collectors are often aggressive in audit and collection efforts. [T3]

### 7.6 Oil and Gas Industry [T2]

Louisiana has specific sales tax rules for the oil and gas industry:

- Certain oilfield equipment and services have unique exemptions. [T2]
- The "boiler and machinery" exemption affects industrial equipment. [T2]
- Severance taxes interact with sales tax on production equipment. [T3]

### 7.7 Mardi Gras and Festival Sales [T2]

Vendors at festivals and events must collect Louisiana sales tax:

- Temporary vendors at events like Mardi Gras, Jazz Fest, etc., must register and collect. [T1]
- Both state and local taxes apply. [T1]
- Short-term permits may be available from local collectors. [T2]

---

## Test Suite

### Test 1: Basic Rate Calculation [T1]

**Question:** A retailer in Baton Rouge (approximately 5% local) sells a $500 television. What is the approximate total sales tax?

**Expected Answer:** State 4.45% + local ~5% = ~9.45%. Tax = $500 x 9.45% = approximately $47.25.

### Test 2: Grocery Food [T1]

**Question:** A consumer buys $200 of groceries in a New Orleans parish that taxes food locally at 5%. What tax is due?

**Expected Answer:** State: $0 (food exempt from state tax). Local: $200 x 5% = $10.00. Total: $10.00. (Note: verify current New Orleans parish food tax rate.)

### Test 3: Remote Seller Filing [T1]

**Question:** An out-of-state retailer exceeds the $100K threshold for Louisiana sales. How many returns must it file?

**Expected Answer:** One. Remote sellers file through the Louisiana Sales and Use Tax Commission (LSTC), which serves as a single point of filing for both state and local taxes.

### Test 4: In-State Seller Filing [T2]

**Question:** An in-state Louisiana seller with locations in Baton Rouge and New Orleans -- how many returns must it file?

**Expected Answer:** At minimum 3: one state return with LDR, one local return with the East Baton Rouge Parish collector, and one local return with the Orleans Parish collector. Additional returns may be needed depending on delivery locations.

### Test 5: Economic Nexus [T1]

**Question:** An out-of-state seller made $80,000 in sales and 250 transactions in Louisiana. Does the seller have nexus?

**Expected Answer:** Yes. Louisiana uses an OR test. The 200-transaction threshold was exceeded.

### Test 6: Manufacturing Exemption [T2]

**Question:** A manufacturer buys a $100,000 machine in a parish with 4% local tax. What tax is due?

**Expected Answer:** State: $0 (manufacturing exemption from 4.45% state tax). Local: depends on whether the parish exempts manufacturing equipment. If the parish does NOT exempt it: $100,000 x 4% = $4,000 in local tax. This illustrates the state vs. local exemption disconnect.

### Test 7: Highest Combined Rate [T1]

**Question:** What is the approximate maximum combined sales tax rate in Louisiana, and why is it notable?

**Expected Answer:** Approximately 11.45%. This is notable because Louisiana can have the highest combined sales tax rate in the entire United States, primarily due to the layering of state + parish + city + special district taxes.

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
