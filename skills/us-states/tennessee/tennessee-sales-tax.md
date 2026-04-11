---
name: tennessee-sales-tax
description: Use this skill whenever asked about Tennessee sales tax, Tennessee use tax, Tennessee sales tax nexus, Tennessee sales tax returns, Tennessee exemption certificates, taxability of goods or services in Tennessee, or any request involving Tennessee state-level consumption taxes. Trigger on phrases like "Tennessee sales tax", "TN sales tax", "Tennessee use tax", "Tennessee nexus", "T.C.A. 67-6", "Tennessee DOR sales tax", or any request involving Tennessee sales and use tax filing, classification, or compliance. NOTE: Tennessee has NO state income tax, making sales tax revenue critical. Tennessee has among the HIGHEST combined sales tax rates in the US (up to 9.75%). ALWAYS read the parent us-sales-tax skill first for federal context.
---

# Tennessee Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Tennessee, United States |
| Jurisdiction Code | US-TN |
| Tax Type | Sales and Use Tax |
| State Tax Rate | 7% (standard); 4% on grocery food |
| Maximum Combined Rate | 9.75% (7% state + 2.75% max local) |
| Primary Legal Framework | Tennessee Code Annotated (T.C.A.) Title 67, Chapter 6 |
| Governing Body | Tennessee Department of Revenue (TNDOR) |
| Filing Portal | TNTAP (Tennessee Taxpayer Access Point) -- https://tntap.tn.gov |
| Economic Nexus Effective Date | October 1, 2019 |
| SST Member | Yes (associate member) |
| No State Income Tax | Yes -- Tennessee has NO state income tax (Hall Tax on investment income was repealed effective Jan 1, 2021) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate lookups, basic nexus, standard taxability. Tier 2: single article cap, SaaS taxability, food rate distinctions. Tier 3: audit defense, penalty abatement, complex bundled transactions. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Tennessee sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Tennessee sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Tennessee? | Drives taxability classification under Tennessee law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Tennessee? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Tennessee local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Rate

Tennessee imposes a **7% state sales tax** on the retail sale of tangible personal property and certain services. This is one of the **highest state-level sales tax rates** in the US.

**Statutory authority:** T.C.A. Section 67-6-202.

### 1.2 Reduced Rate on Grocery Food

Tennessee taxes grocery food at a **reduced state rate of 4%** (down from the 5% rate that was in effect previously):

- **Effective January 1, 2024:** The state rate on food and food ingredients (as defined by Tennessee) was reduced to **4%**. [T1]
- Local taxes still apply to food. [T1]

**Authority:** T.C.A. Section 67-6-228.

### 1.3 Local Rates

Counties and cities levy additional local sales taxes:

| Tax Component | Rate Range | Authority |
|---------------|-----------|-----------|
| State tax (general) | 7.0% | T.C.A. Section 67-6-202 |
| State tax (grocery food) | 4.0% | T.C.A. Section 67-6-228 |
| Local option tax (county) | 1.5% -- 2.75% | T.C.A. Section 67-6-702 |
| **Maximum combined (general)** | **9.75%** | |
| **Maximum combined (grocery)** | **6.75%** | |

**Tennessee has among the highest combined sales tax rates in the United States.** Some jurisdictions reach the 9.75% maximum. [T1]

### 1.4 Single Article Cap on Local Tax [T1]

Tennessee caps the local sales tax on a **single article** (single item) at **$1,600**:

- Local tax applies only to the first **$1,600** of the sales price of a single article. [T1]
- The **state** 7% tax applies to the full price (no cap). [T1]
- The cap applies per individual item, not per transaction. [T1]

**Example:** A $50,000 boat -- state tax: $50,000 x 7% = $3,500 (no cap). Local tax: $1,600 x 2.75% (max) = $44 (capped at local tax on $1,600 only).

**Authority:** T.C.A. Section 67-6-702(a).

### 1.5 Sourcing Rules [T1]

Tennessee is generally an **origin-based** sourcing state for intrastate sales:

- **Intrastate over-the-counter:** Seller's location. [T1]
- **Intrastate shipped:** Origin-based (seller's location). [T1]
- **Interstate (remote sellers):** Destination-based. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 General Rule

Tennessee sales tax applies to the retail sale of tangible personal property and certain enumerated services. T.C.A. Section 67-6-201.

### 2.2 Taxability Matrix

| Item Category | Taxable? | Rate | Authority | Tier |
|---------------|----------|------|-----------|------|
| General tangible personal property | Yes | 7% state + local | T.C.A. Section 67-6-202 | [T1] |
| Grocery food (food for home consumption) | Yes (reduced rate) | **4% state + local** | T.C.A. Section 67-6-228 | [T1] |
| Prepared food (restaurant meals) | Yes | 7% state + local | T.C.A. Section 67-6-102(31)(F) | [T1] |
| Clothing and footwear | Yes | Full rate | No exemption | [T1] |
| Prescription drugs | Exempt | 0% | T.C.A. Section 67-6-314(a)(1) | [T1] |
| Over-the-counter drugs | Yes | Full rate | Not exempt | [T1] |
| Durable medical equipment | Exempt (certain items with prescription) | 0% | T.C.A. Section 67-6-314 | [T1] |
| Motor vehicles | Yes | 7% state + local (single article cap on local) | T.C.A. Section 67-6-202 | [T1] |
| Gasoline and motor fuel | Exempt from sales tax (motor fuel tax) | N/A | T.C.A. Section 67-6-329 | [T1] |
| Utilities (residential electricity) | Yes | Full rate | T.C.A. Section 67-6-202 | [T1] |
| Utilities (natural gas, residential) | Yes | Full rate | T.C.A. Section 67-6-202 | [T1] |
| Industrial machinery (direct use in manufacturing) | Exempt | 0% | T.C.A. Section 67-6-206 | [T2] |
| Agricultural equipment and supplies | Exempt | 0% | T.C.A. Section 67-6-207 | [T1] |
| Software -- canned (tangible medium) | Yes | Full rate | T.C.A. Section 67-6-102(44) | [T1] |
| Software -- canned (electronic delivery) | Yes | Full rate | T.C.A. Section 67-6-231 | [T1] |
| Software -- custom | Yes | Full rate | T.C.A. Section 67-6-231 | [T2] |
| SaaS (Software as a Service) | **Taxable** | Full rate | T.C.A. Section 67-6-231; TNDOR guidance | [T2] |
| Digital goods (e-books, music, video) | Yes | Full rate | T.C.A. Section 67-6-231 | [T1] |
| Data processing services | Not taxable | 0% | Not enumerated | [T2] |
| Extended warranties/service contracts | Yes | Full rate | T.C.A. Section 67-6-102(44) | [T1] |

### 2.3 SaaS Taxability -- Tennessee Position [T2]

Tennessee **taxes SaaS** and digital products broadly:

- Tennessee enacted specific legislation (effective July 1, 2015) taxing "specified digital products" and "software access services" (which includes SaaS). [T1]
- **Specified digital products** include digital audio works, digital audiovisual works, digital books, and any other electronically transferred product. [T1]
- **Software access services** (SaaS) are defined as the right to access and use software where the end user does not receive a copy. This is explicitly taxable. [T2]

**Authority:** T.C.A. Section 67-6-231; T.C.A. Section 67-6-102(89).

### 2.4 Services Taxability [T2]

Tennessee taxes several enumerated services:

| Service | Taxable? | Authority |
|---------|----------|-----------|
| Repair and installation of TPP (labor + parts) | Yes | T.C.A. Section 67-6-102(44) |
| Telecommunications | Yes | T.C.A. Section 67-6-102(44)(C) |
| Cable/satellite TV | Yes | T.C.A. Section 67-6-226 |
| Parking (commercial) | Yes | T.C.A. Section 67-6-212 |
| Amusement and recreation | Yes (admissions) | T.C.A. Section 67-6-212 |
| Hotel/lodging | Yes (plus local hotel/motel tax) | T.C.A. Section 67-6-202 |
| Professional services (legal, accounting) | No | Not enumerated |
| Personal services (haircuts, spa) | No | Not enumerated |
| Construction/real property | No (materials taxable at purchase) | DOR guidance |
| Transportation/freight (separately stated) | Not taxable | T.C.A. Section 67-6-102(44) |

---

## Step 3: Return Form Structure
### 3.1 Registration

All sellers with nexus must register through TNTAP for a **sales and use tax certificate of registration**. No fee for registration.

**Authority:** T.C.A. Section 67-6-601.

### 3.2 Filing Frequency

| Monthly Tax Liability | Filing Frequency | Due Date |
|-----------------------|------------------|----------|
| Over $400 per month | Monthly | 20th of the following month |
| Under $400 per month | Quarterly | 20th of month following quarter-end |

**Note:** TNDOR assigns frequency at registration. Annual filing is not generally available for sales tax. [T1]

### 3.3 Returns and Payment

- **Form SLS 450** (Sales and Use Tax Return) is filed through TNTAP. [T1]
- Electronic filing is required for all registrants. [T1]
- Payment is due on the same date as the return. [T1]
- Both state and local taxes are reported on the same return. [T1]

### 3.4 Vendor Discount

Tennessee provides a **vendor discount** for timely filing:

- **2%** of the first $2,500 of tax due per return period. [T1]
- Maximum discount: **$50** per return period. [T1]
- Available only for timely filing and payment. [T1]

**Authority:** T.C.A. Section 67-6-508.

### 3.5 Penalties and Interest

| Violation | Penalty | Authority |
|-----------|---------|-----------|
| Late filing | 5% per month, up to 25% | T.C.A. Section 67-1-804 |
| Late payment | Same as late filing | T.C.A. Section 67-1-804 |
| Failure to file | Estimated assessment + penalties | T.C.A. Section 67-1-1501 |
| Fraud | 50% of deficiency | T.C.A. Section 67-1-804 |
| Interest | Statutory rate (currently ~7.25%) | T.C.A. Section 67-1-801 |

---

## Step 4: Deductibility / Exemptions
### 5.1 Tennessee Exemption Certificates

| Certificate | Use Case | Authority |
|-------------|----------|-----------|
| **Form ST-14** (Certificate of Resale) | Purchases for resale | TNDOR |
| **Form F-13** (Sales Tax Exemption -- Industrial Machinery) | Manufacturing equipment | T.C.A. Section 67-6-206 |
| **Form ST-18** (Agricultural Exemption Certificate) | Farm equipment and supplies | T.C.A. Section 67-6-207 |
| **SSTCE** (Streamlined certificate) | Multi-state purchases | SST Agreement |
| **Government exemption letter** | Government entity purchases | T.C.A. Section 67-6-320 |

### 5.2 Requirements [T1]

Valid certificates must include purchaser information, Tennessee registration number (for resale), reason for exemption, description of goods, signature, and date. [T1]

### 5.3 Good Faith and Retention [T2]

Good faith acceptance protects sellers. Certificates must be retained for **3 years** from the date of the last transaction. [T1]

---


### 6.1 When Use Tax Applies

Tennessee use tax applies when sales tax was not collected on items used, stored, or consumed in Tennessee. [T1]

### 6.2 Use Tax Rate

The use tax rate equals the sales tax rate: 7% state + applicable local. The single article cap applies to local use tax as well. [T1]

### 6.3 Use Tax Reporting

- **Businesses:** Report on Form SLS 450. [T1]
- **Individuals:** Report on Tennessee Consumer Use Tax Return (or via optional reporting on any state filing). [T1]

---

## Step 5: Key Thresholds
### 4.1 Physical Nexus

Standard physical nexus principles apply. [T1]

### 4.2 Economic Nexus [T1]

Tennessee enacted economic nexus effective **October 1, 2019**.

| Threshold | Value | Measurement Period |
|-----------|-------|--------------------|
| Revenue | **$100,000** in sales into Tennessee | Previous 12 months |
| Transactions | N/A (revenue only) | |
| Test | Revenue only | |

**Authority:** T.C.A. Section 67-6-524.

### 4.3 Marketplace Facilitator Rules [T1]

Effective **October 1, 2020**:

- Marketplace facilitators meeting the nexus threshold must collect and remit. [T1]
- Marketplace sellers relieved for facilitated sales. [T1]

**Authority:** T.C.A. Section 67-6-102(24)(C).

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
1. **NEVER** advise that grocery food is exempt in Tennessee (it is taxable at a reduced 4% state rate + local). [T1]
2. **NEVER** advise that SaaS or digital goods are not taxable in Tennessee (both are explicitly taxable). [T1]
3. **NEVER** ignore the single article cap on local tax when calculating tax on items over $1,600. [T1]
4. **NEVER** use a transaction-count threshold for Tennessee economic nexus (revenue only, $100K). [T1]
5. **NEVER** state that Tennessee has a state income tax (it does not, since Jan 1, 2021). [T1]
6. **NEVER** apply the reduced food rate to prepared food or restaurant meals (those are taxed at the full 7% rate). [T1]
7. **NEVER** forget to apply local taxes in Tennessee -- local rates can add up to 2.75% to the state rate. [T1]
8. **NEVER** assume origin-based sourcing applies to remote/interstate sales (destination-based applies for remote sellers). [T1]
9. **NEVER** cap the state tax at $1,600 -- only the LOCAL tax has the single article cap. [T1]
10. **NEVER** advise that Tennessee offers a generous vendor discount -- the maximum is $50 per period. [T1]

---

## Edge Case Registry

### 7.1 Single Article Cap Application [T1]

The single article cap on local tax ($1,600) creates interesting scenarios:

- **High-value items:** A $100,000 piece of equipment pays 7% state tax ($7,000) on the full price, but local tax only on $1,600 (e.g., at 2.75% = $44 local). Total: $7,044. [T1]
- **Multiple items:** Each item in a transaction is evaluated separately. A purchase of 10 items at $500 each: local tax applies to the full $500 per item (since each is under $1,600). [T1]
- **Bundled items:** If items are sold as a unit, the bundle is treated as one article. [T2]

### 7.2 No State Income Tax Impact [T1]

Tennessee has **no state income tax** (the Hall Tax on interest and dividends was fully repealed effective January 1, 2021). This means:

- Sales tax is a critical revenue source for the state. [T1]
- Tennessee has less incentive to reduce sales tax rates. [T1]
- The high combined rate (up to 9.75%) partially compensates for no income tax. [T1]
- Businesses relocating to Tennessee for income tax savings must budget for higher sales tax costs. [T2]

### 7.3 Manufacturing Exemptions [T2]

Tennessee provides a broad manufacturing exemption:

- Machinery used directly and primarily in manufacturing is exempt. [T2]
- Raw materials incorporated into finished products are exempt. [T1]
- The "directly and primarily" test requires that the machinery's primary purpose be manufacturing (51%+ of use). [T2]
- Energy fuel and water used in manufacturing are exempt. [T2]

**Authority:** T.C.A. Section 67-6-206.

### 7.4 Sales Tax Holiday [T1]

Tennessee holds an annual **sales tax holiday** (typically late July/early August):

- Clothing ($100 or less per item): exempt from state and local tax. [T1]
- School supplies ($100 or less per item): exempt. [T1]
- Computers ($1,500 or less): exempt. [T1]
- Specific dates and items vary annually -- verify with TNDOR each year. [T1]

### 7.5 Short-Term Rental Tax [T2]

Short-term rentals (less than 90 consecutive days) are subject to:

- State sales tax (7%). [T1]
- Local sales tax. [T1]
- Additional state and local occupancy taxes. [T2]
- Marketplace facilitators (Airbnb, VRBO) collect and remit. [T1]

### 7.6 Amusement Tax / Admissions [T1]

Admissions to amusement, sports, and entertainment events are taxable:

- State rate of 7% applies. [T1]
- Local rates apply. [T1]
- Nonprofit exempt events may be excluded with proper documentation. [T2]

### 7.7 Waste Collection Services [T2]

Tennessee taxes certain waste collection and disposal services:

- Commercial waste collection: taxable. [T2]
- Residential waste collection: may be exempt in some circumstances. [T2]

---

## Test Suite

### Test 1: Basic Rate Calculation [T1]

**Question:** A retailer in Nashville (2.25% local) sells a $200 pair of shoes. What is the total sales tax?

**Expected Answer:** State: $200 x 7% = $14.00. Local: $200 x 2.25% = $4.50. Total: $18.50.

### Test 2: Grocery Food Rate [T1]

**Question:** A consumer buys $300 in groceries in Memphis (2.25% local). What tax is due?

**Expected Answer:** State: $300 x 4% = $12.00. Local: $300 x 2.25% = $6.75. Total: $18.75.

### Test 3: Single Article Cap [T1]

**Question:** A customer buys a $50,000 boat in a county with 2.75% local tax. What is the total sales tax?

**Expected Answer:** State: $50,000 x 7% = $3,500 (no cap). Local: $1,600 x 2.75% = $44 (capped). Total: $3,544.

### Test 4: SaaS Taxability [T2]

**Question:** A Tennessee business subscribes to a $500/month SaaS CRM tool. Is Tennessee sales tax due?

**Expected Answer:** Yes. Tennessee explicitly taxes SaaS. At Nashville's rate: $500 x 9.25% = $46.25/month.

### Test 5: Economic Nexus [T1]

**Question:** An out-of-state seller made $90,000 in sales and 400 transactions in Tennessee. Does the seller have nexus?

**Expected Answer:** No. Tennessee's economic nexus is revenue-only at $100,000. The seller is below the threshold. Transaction count is not relevant.

### Test 6: No Income Tax Context [T1]

**Question:** A company considering relocating from New York to Tennessee asks about the overall tax burden. What should be highlighted about sales tax?

**Expected Answer:** Tennessee has no state income tax, but it has one of the highest combined sales tax rates (up to 9.75%). The 7% state rate is among the highest in the US. Businesses must factor in higher sales tax costs on purchases to offset income tax savings.

### Test 7: Sales Tax Holiday [T1]

**Question:** During Tennessee's sales tax holiday, a customer buys a $90 shirt and a $120 pair of boots. Which qualify?

**Expected Answer:** The $90 shirt qualifies ($100 or less) and is exempt. The $120 boots do NOT qualify (exceeds $100 threshold) and are fully taxable.

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
