---
name: minnesota-sales-tax
description: Use this skill whenever asked about Minnesota sales tax, Minnesota use tax, Minnesota sales tax nexus, Minnesota sales tax returns, Minnesota exemption certificates, taxability of goods or services in Minnesota, or any request involving Minnesota state-level consumption taxes. Trigger on phrases like "Minnesota sales tax", "MN sales tax", "Minnesota use tax", "Minnesota nexus", "M.S. 297A", "Minnesota DOR sales tax", or any request involving Minnesota sales and use tax filing, classification, or compliance. NOTE: Minnesota EXEMPTS clothing from sales tax. ALWAYS read the parent us-sales-tax skill first for federal context.
---

# Minnesota Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Minnesota, United States |
| Jurisdiction Code | US-MN |
| Tax Type | Sales and Use Tax |
| State Tax Rate | 6.875% |
| Maximum Combined Rate | Approximately 8.875% (6.875% state + up to ~2% local) |
| Primary Legal Framework | Minnesota Statutes (M.S.) Chapter 297A |
| Governing Body | Minnesota Department of Revenue (MNDOR) |
| Filing Portal | e-Services -- https://www.revenue.state.mn.us |
| Economic Nexus Effective Date | October 1, 2018 |
| SST Member | Yes (full member) |
| Notable Exemptions | Clothing exempt; grocery food exempt |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate lookups, basic nexus, standard taxability, clothing/food exemptions. Tier 2: SaaS classification, local tax determination, small seller exemption nuances. Tier 3: audit defense, penalty abatement, complex bundled transactions. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Minnesota sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Minnesota sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Minnesota? | Drives taxability classification under Minnesota law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Minnesota? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Minnesota local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Rate

Minnesota imposes a **6.875% state sales tax** -- one of the higher state-level rates in the US.

**Statutory authority:** M.S. Section 297A.62.

### 1.2 Local Rates

Counties, cities, and special taxing districts may impose additional local sales taxes:

| Tax Component | Rate Range | Authority |
|---------------|-----------|-----------|
| State tax | 6.875% | M.S. Section 297A.62 |
| City/county local | 0% -- ~1.5% | M.S. Section 297A.99 |
| Transit (metro area) | 0.25% -- 0.5% | M.S. Section 297A.992 |
| Special district | 0% -- 0.5% | Various |
| **Maximum combined** | **~8.875%** | |

**Minneapolis:** 6.875% state + 0.5% city + 0.15% entertainment tax + transit = approximately **8.025%** (varies by transaction type). [T1]

**Hennepin County (Minneapolis):** Additional county and transit taxes may apply. [T1]

### 1.3 Sourcing Rules [T1]

Minnesota follows **SST destination-based** sourcing:

- **Shipped/delivered goods:** Destination (ship-to address). [T1]
- **Over-the-counter:** Seller's location. [T1]
- **Digital goods:** Buyer's address. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 General Rule

Minnesota sales tax applies to the retail sale of tangible personal property, certain services, and certain digital products. M.S. Section 297A.61.

### 2.2 Taxability Matrix

| Item Category | Taxable? | Rate | Authority | Tier |
|---------------|----------|------|-----------|------|
| General tangible personal property | Yes | Full rate | M.S. Section 297A.61 | [T1] |
| Grocery food (food for home consumption) | **Exempt** | 0% | M.S. Section 297A.67, Subd. 2 | [T1] |
| Prepared food (restaurant meals) | Yes | Full rate | M.S. Section 297A.61, Subd. 31 | [T1] |
| **Clothing and footwear** | **EXEMPT** | 0% | M.S. Section 297A.67, Subd. 8 | [T1] |
| Prescription drugs | Exempt | 0% | M.S. Section 297A.67, Subd. 7 | [T1] |
| Over-the-counter drugs | Exempt | 0% | M.S. Section 297A.67, Subd. 7 (SST conformity) | [T1] |
| Durable medical equipment | Exempt | 0% | M.S. Section 297A.67, Subd. 7 | [T1] |
| Motor vehicles | Yes | 6.5% (Motor Vehicle Sales Tax, separate from general sales tax) | M.S. Section 297B.02 | [T1] |
| Gasoline and motor fuel | Exempt from sales tax (motor fuel excise tax) | N/A | M.S. Section 297A.67, Subd. 6 | [T1] |
| Utilities (residential) | Exempt | 0% | M.S. Section 297A.67, Subd. 15 | [T1] |
| Utilities (commercial) | Yes | Full rate | M.S. Section 297A.61 | [T1] |
| Manufacturing equipment (capital equipment) | Exempt (refund-based) | 0% (refund) | M.S. Section 297A.68, Subd. 5 | [T2] |
| Agricultural equipment and supplies | Exempt | 0% | M.S. Section 297A.69 | [T1] |
| Software -- canned (tangible medium) | Yes | Full rate | M.S. Section 297A.61 | [T1] |
| Software -- canned (electronic delivery) | Yes | Full rate | MNDOR guidance | [T1] |
| Software -- custom | Exempt | 0% | MNDOR guidance | [T2] |
| SaaS (Software as a Service) | **Taxable** | Full rate | M.S. Section 297A.61, Subd. 3(l); MNDOR Sales Tax Fact Sheet 177 | [T2] |
| Digital goods (e-books, music, video) | Yes | Full rate | M.S. Section 297A.61, Subd. 3 | [T1] |
| Data processing services | Not taxable | 0% | Not enumerated | [T2] |
| Newspapers (print) | Exempt | 0% | M.S. Section 297A.67, Subd. 4 | [T1] |

### 2.3 Clothing Exemption -- Minnesota's Distinctive Feature [T1]

Minnesota is one of only a few states that fully **exempts clothing** from sales tax:

- **All clothing and footwear** is exempt, regardless of price. [T1]
- There is **no price cap** (unlike New York's $110 threshold or New Jersey's exemption). [T1]
- **Accessories** are NOT clothing and remain taxable: jewelry, handbags, luggage, cosmetics, watches, sunglasses. [T1]
- **Fur clothing** is taxable (explicitly excluded from the clothing exemption). [T1]
- **Sports or recreational equipment** (helmets, pads, cleats, ski boots) is taxable. [T1]
- **Protective equipment** used in work (hard hats, safety glasses, steel-toe boots) is exempt as clothing. [T1]

**Authority:** M.S. Section 297A.67, Subd. 8.

### 2.4 SaaS Taxability [T2]

Minnesota **taxes SaaS** and digital products:

- SaaS is classified as "specified digital products" or electronically delivered software under Minnesota law. [T2]
- The tax applies to all forms of access to prewritten software, whether downloaded, streamed, or accessed remotely. [T2]
- **Custom software** remains exempt if created specifically for one customer. [T2]

**Authority:** M.S. Section 297A.61, Subd. 3(l); MNDOR Sales Tax Fact Sheet 177.

### 2.5 Services Taxability [T2]

Minnesota taxes a broader range of services than many states:

| Service | Taxable? | Authority |
|---------|----------|-----------|
| Telecommunications | Yes | M.S. Section 297A.61 |
| Cable/satellite TV | Yes | M.S. Section 297A.61 |
| Laundry/dry cleaning | Yes | M.S. Section 297A.61, Subd. 3(d) |
| Repair and maintenance of TPP | Yes (labor + parts) | M.S. Section 297A.61, Subd. 3(f) |
| Parking (commercial) | Yes | M.S. Section 297A.61, Subd. 3(g) |
| Admissions/entertainment | Yes | M.S. Section 297A.61, Subd. 3(b) |
| Hotel/lodging | Yes (plus local lodging taxes) | M.S. Section 297A.61, Subd. 3(c) |
| Building cleaning and maintenance | Yes | M.S. Section 297A.61, Subd. 3(e) |
| Detective/security services | Yes | M.S. Section 297A.61, Subd. 3(h) |
| Professional services (legal, accounting) | No | Not enumerated |
| Personal services (haircuts, spa) | No | Not enumerated |
| Construction/real property | No (materials taxable at purchase) | MNDOR guidance |
| Transportation/freight | Exempt (if separately stated) | M.S. Section 297A.68 |

---

## Step 3: Return Form Structure
### 3.1 Registration

All sellers with nexus must register through MNDOR's e-Services portal. No fee.

**Authority:** M.S. Section 297A.83.

### 3.2 Filing Frequency

| Monthly Tax Liability | Filing Frequency | Due Date |
|-----------------------|------------------|----------|
| Over $500 per month | Monthly | 20th of the following month |
| $100 -- $500 per month | Quarterly | 20th of month following quarter-end |
| Under $100 per month | Annual | February 5 |

### 3.3 Returns and Payment

- Minnesota uses its own electronic return through e-Services (no specific form number for electronic filers). [T1]
- Electronic filing is required for most filers. [T1]
- Payment due on the same date as the return. [T1]
- Accelerated filers (over $250,000/year in tax) must make estimated payments. [T2]

### 3.4 Vendor Discount

Minnesota does **not** offer a vendor discount for timely filing. [T1]

### 3.5 Penalties and Interest

| Violation | Penalty | Authority |
|-----------|---------|-----------|
| Late filing | 5% of tax due, minimum $1 | M.S. Section 289A.60 |
| Late payment | 5% of tax due | M.S. Section 289A.60 |
| Extended late payment | Additional 5% if 30+ days late (total 10%) | M.S. Section 289A.60 |
| Failure to file | Estimated assessment + penalties | M.S. Section 289A.35 |
| Fraud | 50% of deficiency | M.S. Section 289A.60 |
| Interest | Adjusted annually (currently ~5%) | M.S. Section 270C.40 |

---

## Step 4: Deductibility / Exemptions
### 5.1 Minnesota Exemption Certificates

| Certificate | Use Case | Authority |
|-------------|----------|-----------|
| **Form ST-3** (Certificate of Exemption) | General exemption (resale, exempt organizations, manufacturing, agricultural) | MNDOR |
| **SSTCE** (Streamlined certificate) | Multi-state purchases (Minnesota is SST member) | SST Agreement |
| **Capital Equipment Refund (Form ST-11)** | Capital equipment exemption (refund-based) | M.S. Section 297A.68, Subd. 5 |

### 5.2 Capital Equipment -- Refund-Based Exemption [T2]

Minnesota's manufacturing/capital equipment exemption is unique:

- Qualifying capital equipment is purchased WITH tax, and then a **refund** is claimed. [T2]
- The refund is filed on Form ST-11. [T2]
- Processing time for refunds can be several weeks to months. [T2]
- This is different from most states where the exemption is claimed at the point of sale. [T2]

**Authority:** M.S. Section 297A.75.

### 5.3 Requirements and Retention [T1]

Standard requirements: name, address, registration number (for resale), reason, description, signature, date. Certificates retained for **3.5 years** from the date of the last transaction (Minnesota's statute of limitations is 3.5 years). [T1]

---


### 6.1 When Use Tax Applies

Minnesota use tax applies when sales tax was not collected on items used, stored, or consumed in Minnesota. [T1]

### 6.2 Use Tax Rate

6.875% state + applicable local. [T1]

### 6.3 Use Tax Reporting

- **Businesses:** Report on the sales tax return through e-Services. [T1]
- **Individuals:** Report on Minnesota income tax return (Form M1), Line 20a. [T1]

---

## Step 5: Key Thresholds
### 4.1 Physical Nexus

Standard physical nexus principles apply. [T1]

### 4.2 Economic Nexus [T1]

Minnesota enacted economic nexus effective **October 1, 2018**.

| Threshold | Value | Measurement Period |
|-----------|-------|--------------------|
| Revenue | **$100,000** in gross sales into Minnesota | Previous 12 months |
| Transactions | **200 transactions** into Minnesota (requires **10 or more retail sales** for small seller threshold) | Previous 12 months |
| Test | **OR** -- either threshold triggers nexus | |

**Special note on small seller provision:** Minnesota has an additional nuance -- a remote seller is not required to collect if it makes fewer than **10 retail sales** totaling less than **$100** in the preceding 12 months. This is a de minimis exemption, separate from the main economic nexus thresholds. [T2]

**Authority:** M.S. Section 297A.66.

### 4.3 Marketplace Facilitator Rules [T1]

Effective **October 1, 2019**:

- Marketplace facilitators meeting the nexus threshold must collect and remit. [T1]
- Marketplace sellers relieved for facilitated sales. [T1]

**Authority:** M.S. Section 297A.665.

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
1. **NEVER** advise that clothing is taxable in Minnesota (it is exempt). [T1]
2. **NEVER** advise that grocery food is taxable in Minnesota (it is exempt). [T1]
3. **NEVER** advise that SaaS is not taxable in Minnesota (it is taxable). [T1]
4. **NEVER** ignore local taxes when quoting a rate -- Minnesota has city, county, and transit taxes. [T1]
5. **NEVER** advise that Minnesota offers a vendor discount for timely filing (it does not). [T1]
6. **NEVER** confuse the Motor Vehicle Sales Tax rate (6.5%) with the general sales tax rate (6.875%). [T1]
7. **NEVER** advise that capital equipment is exempt at the point of sale -- it uses a refund-based mechanism. [T2]
8. **NEVER** classify fur clothing as exempt (it is specifically excluded from the clothing exemption). [T1]
9. **NEVER** forget that building cleaning services are taxable in Minnesota. [T1]
10. **NEVER** advise that Minnesota is not an SST member (it is a full member). [T1]

---

## Edge Case Registry

### 7.1 Motor Vehicle Sales Tax (MVST) [T1]

Minnesota imposes a separate Motor Vehicle Sales Tax:

- Rate: **6.5%** (lower than the general 6.875% rate). [T1]
- Collected by the Driver and Vehicle Services (DVS) division at registration. [T1]
- Trade-in values reduce the taxable base. [T1]
- MVST is constitutionally dedicated to transportation funding. [T1]

**Authority:** M.S. Section 297B.02.

### 7.2 Clothing vs. Accessories Line Drawing [T2]

The clothing exemption requires careful classification:

- **Exempt:** Shirts, pants, coats, shoes (non-sport), dresses, underwear, socks, hats (non-sport), gloves, scarves. [T1]
- **Taxable:** Jewelry, watches, handbags, wallets, umbrellas, cosmetics, hair accessories, sport-specific footwear (cleats, ski boots), fur coats/accessories, sewing equipment. [T1]
- **Costumes:** Taxable. [T1]
- **Formal wear rental:** Taxable (rental, not sale of clothing). [T2]

### 7.3 Building Cleaning and Maintenance Services [T1]

Minnesota is notable for taxing building cleaning services:

- Janitorial services, window cleaning, carpet cleaning (for buildings) are taxable. [T1]
- Residential cleaning is taxable (unlike some states). [T1]
- Lawn care and landscaping: NOT taxable (real property services). [T2]

### 7.4 Capital Equipment Refund Timing [T2]

The refund-based capital equipment exemption creates cash flow considerations:

- Businesses must pay tax upfront and then wait for the refund. [T2]
- Refund claims must be filed within 3.5 years. [T1]
- Interest is paid on late refunds. [T1]
- Some businesses negotiate direct purchase exemptions with MNDOR for very large purchases. [T3]

### 7.5 Local Tax Complexity [T2]

While Minnesota has fewer local jurisdictions than some states, the local tax layer adds complexity:

- Minneapolis and St. Paul have city sales taxes. [T1]
- Hennepin and Ramsey counties have additional taxes. [T1]
- The Metropolitan Council area has transit taxes. [T1]
- Food and clothing exemptions generally apply at the local level too. [T1]

### 7.6 Farm Equipment and Agricultural Exemptions [T1]

Minnesota provides broad agricultural exemptions:

- Farm machinery: exempt. [T1]
- Seeds, feed, fertilizer: exempt. [T1]
- Farm chemicals and pesticides: exempt. [T1]
- Livestock: exempt. [T1]
- The farmer must provide a certificate of exemption. [T1]

### 7.7 Short-Term Rentals [T2]

- Subject to state sales tax. [T1]
- Subject to local lodging taxes. [T1]
- Minneapolis and St. Paul have additional lodging taxes. [T1]
- Marketplace facilitators collect state tax. [T1]

---

## Test Suite

### Test 1: Basic Rate Calculation [T1]

**Question:** A retailer in a rural Minnesota county (no local tax) sells a $400 kitchen appliance. What sales tax is due?

**Expected Answer:** $400 x 6.875% = $27.50.

### Test 2: Clothing Exemption [T1]

**Question:** A customer buys a $500 winter coat and a $200 watch in Minnesota. What tax is due?

**Expected Answer:** Coat: exempt (clothing). Watch: taxable (accessory). Tax = $200 x 6.875% = $13.75.

### Test 3: Grocery Food Exemption [T1]

**Question:** A consumer buys $250 in groceries and $30 in prepared deli food in Minneapolis. What tax is due?

**Expected Answer:** Groceries: exempt ($0). Prepared food: $30 x (6.875% + Minneapolis local) = approximately $30 x 8.025% = $2.41. Total: approximately $2.41.

### Test 4: SaaS Taxability [T2]

**Question:** A Minnesota company subscribes to a $600/month SaaS project management tool. Is Minnesota sales tax due?

**Expected Answer:** Yes. Minnesota taxes SaaS. Tax = $600 x (6.875% + applicable local rate).

### Test 5: Economic Nexus [T1]

**Question:** An out-of-state seller made $110,000 in Minnesota sales last year. Does the seller have nexus?

**Expected Answer:** Yes. The $100,000 revenue threshold was exceeded.

### Test 6: Capital Equipment Refund [T2]

**Question:** A manufacturer buys $500,000 of qualifying capital equipment in Minnesota. How is the tax handled?

**Expected Answer:** The manufacturer pays 6.875% tax upfront ($34,375), then files Form ST-11 to claim a refund. The refund is processed by MNDOR, typically within several weeks to months.

### Test 7: Motor Vehicle Tax [T1]

**Question:** A customer buys a $30,000 car with a $5,000 trade-in in Minnesota. What motor vehicle sales tax is due?

**Expected Answer:** Taxable base: $30,000 - $5,000 = $25,000. MVST: $25,000 x 6.5% = $1,625 (not 6.875% -- MVST has its own rate).

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
