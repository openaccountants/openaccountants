---
name: michigan-sales-tax
description: Use this skill whenever asked about Michigan sales tax, Michigan use tax, Michigan sales tax nexus, Michigan sales tax returns, Michigan exemption certificates, taxability of goods or services in Michigan, or any request involving Michigan state-level consumption taxes. Trigger on phrases like "Michigan sales tax", "MI sales tax", "Michigan use tax", "Michigan nexus", "MCL 205.51", "Michigan Treasury sales tax", or any request involving Michigan sales and use tax filing, classification, or compliance. ALWAYS read the parent us-sales-tax skill first for federal context, then layer this Michigan-specific skill on top.
---

# Michigan Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Michigan, United States |
| Jurisdiction Code | US-MI |
| Tax Type | General Sales Tax and Use Tax |
| State Tax Rate | 6% (flat -- no local sales tax) |
| Maximum Combined Rate | 6% (no local component) |
| Primary Legal Framework | Michigan Compiled Laws (MCL) 205.51 et seq. (General Sales Tax Act); MCL 205.91 et seq. (Use Tax Act) |
| Governing Body | Michigan Department of Treasury |
| Filing Portal | Michigan Treasury Online (MTO) -- https://mto.treasury.michigan.gov |
| Economic Nexus Effective Date | October 1, 2018 |
| SST Member | Yes (full member) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate lookups, basic nexus, standard taxability. Tier 2: SaaS/digital classification, industrial processing exemption, service taxability. Tier 3: audit defense, penalty abatement, administrative appeals. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Michigan sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Michigan sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Michigan? | Drives taxability classification under Michigan law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Michigan? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Michigan local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Rate

Michigan imposes a **flat 6% state sales tax** on the retail sale of tangible personal property and certain services. There are **no local sales taxes** in Michigan.

**This makes Michigan one of the simplest states for rate determination.** Once you confirm the transaction is taxable and delivered to/within Michigan, the rate is always 6%. [T1]

**Statutory authority:** MCL 205.52(1).

### 1.2 No Local Taxes

Michigan is one of a small number of states that **prohibits local sales taxes entirely**. There are no county, city, or special district sales taxes. The Michigan Constitution (Article IX, Section 8) restricts sales tax authority to the state level. [T1]

### 1.3 Sourcing Rules [T1]

Michigan follows **Streamlined Sales Tax (SST)** sourcing rules:

- **Shipped/delivered goods:** Destination-based (ship-to address). [T1]
- **Over-the-counter (walk-in):** Seller's location. [T1]
- **Digital goods (electronically delivered):** Buyer's address. [T1]
- **Services on TPP:** Location where TPP is delivered after service. [T1]

Since there are no local rate variations, the sourcing determination affects only whether the sale is a Michigan sale (6%) or sourced to another state. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 General Rule

Michigan sales tax applies to the retail sale of **tangible personal property (TPP)** and certain specifically enumerated services. MCL 205.51a.

### 2.2 Taxability Matrix

| Item Category | Taxable? | Rate | Authority | Tier |
|---------------|----------|------|-----------|------|
| General tangible personal property | Yes | 6% | MCL 205.52 | [T1] |
| Grocery food (food for home consumption) | **Exempt** | 0% | MCL 205.54g | [T1] |
| Prepared food (restaurant meals) | Yes | 6% | MCL 205.54g(4) | [T1] |
| Clothing and footwear | Yes | 6% | No exemption | [T1] |
| Prescription drugs | Exempt | 0% | MCL 205.54g(1)(a) | [T1] |
| Over-the-counter drugs | Exempt | 0% | MCL 205.54g(1)(b) (SST conformity) | [T1] |
| Durable medical equipment | Exempt (with prescription) | 0% | MCL 205.54g(1)(c) | [T1] |
| Prosthetic devices | Exempt | 0% | MCL 205.54g(1)(d) | [T1] |
| Motor vehicles | Yes | 6% | MCL 205.52 | [T1] |
| Gasoline and motor fuel | Exempt from sales tax (motor fuel tax applies) | N/A | MCL 205.54g(1)(k) | [T1] |
| Utilities (residential -- electricity, gas) | Exempt | 0% | MCL 205.54d | [T1] |
| Utilities (commercial/industrial) | Yes | 6% | MCL 205.52 | [T1] |
| Industrial processing equipment | Exempt (direct use) | 0% | MCL 205.54t | [T2] |
| Agricultural supplies and equipment | Exempt | 0% | MCL 205.54a | [T1] |
| Software -- canned (tangible medium) | Yes | 6% | MCL 205.51a | [T1] |
| Software -- canned (electronic delivery) | Yes | 6% | Revenue Administrative Bulletin (RAB) 1999-5 | [T2] |
| Software -- custom | Exempt | 0% | RAB 1999-5 | [T2] |
| SaaS (Software as a Service) | **Not taxable** | 0% | Michigan Treasury -- SaaS is not tangible personal property | [T2] |
| Digital goods (prewritten, delivered electronically) | Yes (per SST conformity) | 6% | MCL 205.51a(r) | [T2] |
| Data processing services | Not taxable | 0% | Not enumerated | [T2] |
| Newspapers and periodicals | Exempt | 0% | MCL 205.54g(1)(j) | [T1] |

### 2.3 Grocery Food Exemption [T1]

Michigan fully exempts **food for human consumption** (grocery food) from sales tax:

- The exemption applies to food and food ingredients as defined by SST (Michigan is an SST member). [T1]
- **Prepared food**, **soft drinks**, and **dietary supplements** are NOT considered "food for human consumption" and remain taxable. [T1]
- **Candy** is taxable (it is excluded from the "food" definition under SST). [T1]
- Food purchased with SNAP/EBT benefits is exempt regardless of type. [T1]

**Authority:** MCL 205.54g.

### 2.4 SaaS -- Not Taxable [T2]

Michigan does **not** tax SaaS because it is not considered tangible personal property:

- The Michigan Department of Treasury has consistently held that SaaS is a service, not the sale of TPP. [T2]
- The key factor is that no transfer of possession or ownership of the software occurs -- the customer merely accesses the vendor's server. [T2]
- **Canned software** delivered electronically IS taxable (RAB 1999-5), but SaaS (where the software resides on the vendor's servers and is accessed via browser) is distinguished from electronic delivery of software. [T2]
- IaaS and PaaS follow similar logic -- generally not taxable. [T2]

**CAUTION:** The distinction between "electronically delivered canned software" (taxable) and "SaaS" (not taxable) can be fact-specific. If a product allows download and offline use, it may be treated as canned software. [T3]

### 2.5 Services Taxability [T2]

Michigan does **not** impose a broad-based tax on services. Only specifically enumerated services are taxable:

| Service | Taxable? | Authority |
|---------|----------|-----------|
| Telecommunications services | Yes | MCL 205.51a(o) |
| Installation of TPP (when incidental to sale) | Yes | MCL 205.51a |
| Repair and maintenance of TPP | Labor: No (if separately stated); Parts: Yes | RAB 2015-22 |
| Hotel/motel accommodations | Yes (plus separate use tax on accommodations) | MCL 205.93a |
| Laundry and dry cleaning | Yes | MCL 205.51a |
| Professional services (legal, accounting) | No | Not enumerated |
| Personal services (haircuts, spa) | No | Not enumerated |
| Construction (real property) | No (materials taxable at purchase) | DOR guidance |
| Transportation/shipping (separately stated) | Exempt | MCL 205.54g |

---

## Step 3: Return Form Structure
### 3.1 Registration

All sellers with nexus must register for a Michigan sales tax license. Registration is completed through Michigan Treasury Online (MTO).

**Cost:** There is **no fee** for a Michigan sales tax license. [T1]

**Authority:** MCL 205.53.

### 3.2 Filing Frequency

| Monthly Tax Liability | Filing Frequency | Due Date |
|-----------------------|------------------|----------|
| $0 -- $62 per month ($750/year) | Annual | February 28 |
| $63 -- $300 per month ($750 -- $3,600/year) | Quarterly | 20th of month following quarter-end |
| Over $300 per month (over $3,600/year) | Monthly | 20th of the following month |

**Note:** The Treasury may assign filing frequency at registration. Newly registered sellers are typically assigned monthly filing and may be moved to a less frequent schedule after a filing history is established. [T1]

### 3.3 Returns and Payment

- **Form 5080** (Sales, Use, and Withholding Taxes Monthly/Quarterly Return) is the primary return. [T1]
- **Form 5081** (Sales, Use, and Withholding Taxes Annual Return) for annual filers. [T1]
- Electronic filing through Michigan Treasury Online (MTO) is required. [T1]
- Payment is due on the same date as the return. [T1]

### 3.4 Discount for Timely Filing

Michigan provides a **discount** for timely filing and remittance:

- **0.75%** of the tax collected, up to **$20 per month** for monthly filers. [T1]
- The discount is available only when the return is filed and payment is made by the due date. [T1]

**Authority:** MCL 205.54.

### 3.5 Penalties and Interest

| Violation | Penalty | Authority |
|-----------|---------|-----------|
| Late filing | 5% of tax due per month, up to 25% | MCL 205.24(2) |
| Late payment | 5% of tax due per month, up to 25% | MCL 205.24(2) |
| Failure to file | Estimated assessment + penalties | MCL 205.21 |
| Negligence | 10% of deficiency | MCL 205.23(2) |
| Fraud | 100% of deficiency | MCL 205.23(3) |
| Interest | 1% above the adjusted prime rate, per year | MCL 205.23(2) |

### 3.6 Zero Returns

Returns must be filed even if no tax is due. Failure to file zero returns may result in automatic assessment by the Department of Treasury. [T1]

---

## Step 4: Deductibility / Exemptions
### 5.1 Michigan Exemption Certificates

Michigan accepts the following:

| Certificate | Use Case | Authority |
|-------------|----------|-----------|
| **Form 3372** (Michigan Sales and Use Tax Certificate of Exemption) | General exemption (resale, industrial processing, agricultural, etc.) | MCL 205.54a |
| **Streamlined Sales Tax Certificate of Exemption (SSTCE)** | Multi-state exemption (Michigan is SST member) | SST Agreement |
| **Form 3520** (Michigan Industrial Processing Exemption) | Specific to industrial processing claims | MCL 205.54t |

### 5.2 Requirements for Valid Certificates [T1]

A valid Michigan exemption certificate must include:

1. Purchaser's name, address, and signature. [T1]
2. Type of exemption claimed (resale, industrial processing, agricultural, etc.). [T1]
3. Michigan sales tax registration number (for resale). [T1]
4. Description of property being purchased. [T1]
5. Date of certificate. [T1]

### 5.3 Good Faith Acceptance [T2]

Sellers accepting certificates in good faith are relieved of tax liability:

- Certificate must be complete and appear valid. [T1]
- Purchase must be consistent with the claimed exemption. [T2]
- Blanket certificates are accepted for ongoing relationships. [T1]

**Authority:** MCL 205.54a(3).

### 5.4 Retention Period

Michigan requires exemption certificates to be retained for **4 years** from the date of the last transaction under the certificate. [T1]

---


### 6.1 When Use Tax Applies

Michigan use tax is complementary to the sales tax and applies when:

- Property purchased from a seller that did not collect Michigan sales tax is used, stored, or consumed in Michigan. [T1]
- Property purchased for resale is withdrawn for personal/business use. [T1]
- Property brought into Michigan from another state where tax was not paid. [T1]

### 6.2 Use Tax Rate

The Michigan use tax rate is **6%**, identical to the sales tax rate. [T1]

**Authority:** MCL 205.93.

### 6.3 Credit for Taxes Paid

Michigan allows a credit for sales/use tax paid to another state, up to 6%. [T1]

### 6.4 Use Tax Reporting

- **Businesses:** Report on Form 5080/5081 (same return as sales tax). [T1]
- **Individuals:** Report on Michigan individual income tax return (Form MI-1040), Line 23. [T1]
- Michigan is more aggressive than many states in pursuing individual use tax compliance. [T2]

---

## Step 5: Key Thresholds
### 4.1 Physical Nexus

Michigan follows standard physical nexus principles:

- Place of business in Michigan. [T1]
- Employees or agents in Michigan. [T1]
- Inventory stored in Michigan (including FBA warehouses). [T1]
- Regular deliveries by company vehicles. [T1]

### 4.2 Economic Nexus [T1]

Michigan enacted economic nexus effective **October 1, 2018**.

| Threshold | Value | Measurement Period |
|-----------|-------|--------------------|
| Revenue | **$100,000** in gross sales into Michigan | Previous calendar year |
| Transactions | **200 transactions** into Michigan | Previous calendar year |
| Test | **OR** -- either threshold triggers nexus | |

**Authority:** MCL 205.52b.

**Important notes:**

- Michigan was among the earliest states to enact post-Wayfair economic nexus (effective just months after the decision). [T1]
- The threshold is measured on the **previous calendar year** (not trailing 12 months). [T1]
- Exempt sales count toward the threshold. [T2]

### 4.3 Marketplace Facilitator Rules [T1]

Michigan enacted marketplace facilitator rules effective **January 1, 2020**.

- Marketplace facilitators meeting the nexus thresholds must collect and remit. [T1]
- Marketplace sellers are relieved for facilitated sales. [T1]
- A marketplace facilitator is broadly defined to include any person who lists products for sale and collects payment on behalf of a third-party seller. [T1]

**Authority:** MCL 205.52a.

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
1. **NEVER** advise that Michigan has local sales taxes (it does not -- the rate is always 6% statewide). [T1]
2. **NEVER** advise that SaaS is taxable in Michigan (it is not, as it is not tangible personal property). [T1]
3. **NEVER** advise that grocery food is taxable in Michigan (it is exempt). [T1]
4. **NEVER** confuse the Michigan sales tax (General Sales Tax Act, MCL 205.51 et seq.) with the Michigan use tax (Use Tax Act, MCL 205.91 et seq.) -- they are separate statutes with the same rate. [T1]
5. **NEVER** advise that all nonprofits are exempt from Michigan sales tax (most are not). [T1]
6. **NEVER** apply the industrial processing exemption broadly to all manufacturing-related purchases (it is limited to "direct use" in the transformation process). [T2]
7. **NEVER** calculate a rate other than 6% for Michigan sales tax. There is no reduced rate, no local add-on, no regional variation. [T1]
8. **NEVER** tell sellers they can file annually without first verifying their tax liability qualifies ($750/year or less). [T1]
9. **NEVER** advise that Michigan uses origin-based sourcing for shipped goods (it uses destination-based per SST). [T1]
10. **NEVER** ignore the candy/soft drink distinction when applying the grocery food exemption -- candy and soft drinks are taxable. [T1]

---

## Edge Case Registry

### 7.1 Industrial Processing Exemption [T2]

Michigan provides a significant exemption for property used in **industrial processing**:

- Equipment, machinery, and tools used in the **actual transformation** of materials into a finished product are exempt. [T2]
- "Industrial processing" begins when raw materials are moved from storage to the production line and ends when the finished product is first placed in finished goods storage. [T2]
- Ancillary activities (administration, distribution, shipping, R&D) do NOT qualify. [T2]
- A **35% industrial processing** exemption may apply to items used partially in industrial processing and partially in other activities. [T3]

**Authority:** MCL 205.54t; Revenue Administrative Bulletin (RAB) 2002-15.

### 7.2 Technology and Hosting [T2]

- **Web hosting services:** Generally not taxable (service, not TPP). [T2]
- **Cloud storage:** Not taxable (service). [T2]
- **Downloaded music, movies, e-books:** Taxable as digital goods. [T1]
- **Streaming services (Netflix, Spotify):** Taxable as the sale of digital goods. [T2]
- **SaaS:** Not taxable (see Section 2.4). [T2]

### 7.3 Drop Shipments [T2]

Michigan follows SST protocols for drop shipments:

- The retailer is the seller and must collect tax from the customer. [T1]
- The drop shipper can accept a resale certificate from the retailer. [T2]
- If the retailer lacks Michigan nexus, the drop shipper may need to collect tax. [T2]

### 7.4 Motor Vehicle Sales [T1]

- Motor vehicles are taxable at 6%. [T1]
- Tax is paid at the Secretary of State's office when the vehicle is titled, not at the dealership. [T1]
- Trade-in values reduce the taxable base. [T1]
- Gifts between immediate family members (parent, child, spouse, sibling) are exempt. [T1]

**Authority:** MCL 205.52(1); MCL 205.54g.

### 7.5 Construction Contractors [T2]

Michigan treats construction contractors as consumers of materials:

- Contractors pay sales tax when purchasing materials. [T1]
- Contractors do NOT charge sales tax on the finished real property improvement. [T1]
- Prefabricated items that could be TPP may complicate this analysis. [T2]
- Repair vs. real property improvement distinction applies. [T2]

### 7.6 Nonprofit Organizations [T2]

- Michigan provides a **very limited** sales tax exemption for nonprofits. [T2]
- Most nonprofits are NOT automatically exempt from paying sales tax on their purchases. [T1]
- Nonprofits may be exempt from collecting sales tax on occasional fundraising sales. [T2]
- Government entities and qualifying educational institutions have broader exemptions. [T2]

**Authority:** MCL 205.54a(1)(e).

### 7.7 Bad Debt Deductions [T1]

Sellers may take a deduction on their return for sales tax previously remitted on accounts that become uncollectible (bad debts):

- The deduction is available on the return for the period in which the debt is written off for federal income tax purposes. [T1]
- Michigan follows SST guidelines for bad debt deductions. [T1]

**Authority:** MCL 205.54i.

---

## Test Suite

### Test 1: Basic Rate Calculation [T1]

**Question:** A retailer in Detroit sells a $800 television. What is the sales tax?

**Expected Answer:** $800 x 6% = $48.00. There is no local tax in Michigan.

### Test 2: Grocery Food Exemption [T1]

**Question:** A grocery store sells $150 in bread, milk, and fresh vegetables, plus $20 in candy bars. What tax is due?

**Expected Answer:** Groceries ($150): exempt, $0 tax. Candy ($20): taxable at 6% = $1.20. Total tax: $1.20.

### Test 3: SaaS Taxability [T2]

**Question:** A Michigan company subscribes to a $2,000/month cloud-based accounting SaaS platform. Is Michigan sales/use tax due?

**Expected Answer:** No. SaaS is not taxable in Michigan because it is not tangible personal property and no transfer of possession occurs.

### Test 4: Economic Nexus [T1]

**Question:** An out-of-state seller had $120,000 in Michigan sales but only 50 transactions last year. Does the seller have nexus?

**Expected Answer:** Yes. The $100,000 revenue threshold was exceeded. Michigan uses an OR test.

### Test 5: Industrial Processing [T2]

**Question:** A manufacturer buys a $50,000 milling machine used exclusively on the production line. Is it exempt?

**Expected Answer:** Yes, if the machine is used directly in the industrial processing (transformation) of materials into a finished product. The manufacturer must provide a completed Form 3372 claiming the industrial processing exemption.

### Test 6: Use Tax on Out-of-State Purchase [T1]

**Question:** A Michigan resident buys a $3,000 laptop from an Oregon retailer (Oregon has no sales tax). What Michigan use tax is owed?

**Expected Answer:** $3,000 x 6% = $180.00. No credit for tax paid to another state (Oregon has no sales tax). The resident should report this on their MI-1040.

### Test 7: Repair vs. Parts [T2]

**Question:** A Michigan auto repair shop charges $200 for labor and $300 for parts to fix a transmission. How is each component taxed?

**Expected Answer:** Parts ($300): taxable at 6% = $18.00. Labor ($200): exempt if separately stated from parts. Total tax: $18.00.

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
