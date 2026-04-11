---
name: virginia-sales-tax
description: Use this skill whenever asked about Virginia sales tax, Virginia use tax, Virginia sales tax nexus, Virginia sales tax returns, Virginia exemption certificates, taxability of goods or services in Virginia, or any request involving Virginia state-level consumption taxes. Trigger on phrases like "Virginia sales tax", "VA sales tax", "Virginia use tax", "Virginia nexus", "Va. Code 58.1-603", "Virginia Tax Department", or any request involving Virginia sales and use tax filing, classification, or compliance. ALWAYS read the parent us-sales-tax skill first for federal context, then layer this Virginia-specific skill on top.
---

# Virginia Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Virginia, United States |
| Jurisdiction Code | US-VA |
| Tax Type | Retail Sales and Use Tax |
| Standard Rate | 5.3% (4.3% state + 1% local mandatory) |
| Regional Rates | 6% in Northern Virginia and Hampton Roads (additional 0.7% regional) |
| Hampton Roads Rate | 7% (additional 1.7% total regional component) |
| Primary Legal Framework | Code of Virginia, Title 58.1, Chapter 6 (Section 58.1-600 et seq.) |
| Key Statute | Va. Code Section 58.1-603 (Imposition of tax) |
| Governing Body | Virginia Department of Taxation (Virginia Tax) |
| Filing Portal | Virginia Tax Online Services -- https://www.tax.virginia.gov |
| Economic Nexus Effective Date | July 1, 2019 |
| SST Member | No |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate lookups, basic nexus, standard taxability. Tier 2: regional rate determinations, grocery food reduced rate, SaaS classification, multi-jurisdiction issues. Tier 3: audit defense, penalty abatement, administrative appeals. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Virginia sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Virginia sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Virginia? | Drives taxability classification under Virginia law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Virginia? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Virginia local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 Standard Rate Composition

Virginia's sales tax has a **mandatory local component** built into the rate structure, unlike most states:

| Component | Rate | Authority |
|-----------|------|-----------|
| State tax | 4.3% | Va. Code Section 58.1-603 |
| Local tax (mandatory statewide) | 1.0% | Va. Code Section 58.1-605 |
| **Standard combined rate** | **5.3%** | |

### 1.2 Regional Rates

Certain regions of Virginia have additional regional taxes:

| Region | Additional Rate | Total Rate | Authority |
|--------|----------------|------------|-----------|
| Northern Virginia (NOVA) | 0.7% (regional transport) | **6.0%** | Va. Code Section 58.1-603.1 |
| Hampton Roads | 0.7% (regional transport) + 1.0% (additional regional) | **7.0%** | Va. Code Section 58.1-603.1; HB 1414 (2020) |
| Central Virginia (Richmond metro) | 0.7% (regional transport) | **6.0%** | Va. Code Section 58.1-603.1 |
| Rest of Virginia | None | **5.3%** | Standard rate |

**Northern Virginia jurisdictions (6.0%):** Arlington, Fairfax, Loudoun, Prince William counties; cities of Alexandria, Fairfax, Falls Church, Manassas, Manassas Park. [T1]

**Hampton Roads jurisdictions (7.0%):** Chesapeake, Hampton, Isle of Wight, James City, Newport News, Norfolk, Poquoson, Portsmouth, Suffolk, Virginia Beach, Williamsburg, York. [T1]

### 1.3 Sourcing Rules [T1]

Virginia is generally an **origin-based** sourcing state for intrastate sales:

- **Intrastate sales:** Sourced to the seller's location for over-the-counter sales. For shipped goods, sourced to the destination. [T1]
- **Interstate sales (remote sellers):** Destination-based. [T1]
- **Delivered sales:** Destination-based (the delivery address determines the rate). [T1]

**Important:** Because Virginia has regional rate differences, the sourcing determination directly affects the rate. A seller in Northern Virginia (6%) shipping to Hampton Roads (7%) charges the 7% rate. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 General Rule

Virginia sales tax applies to the retail sale, lease, or rental of tangible personal property and certain enumerated services. Va. Code Section 58.1-603.

### 2.2 Taxability Matrix

| Item Category | Taxable? | Rate | Authority | Tier |
|---------------|----------|------|-----------|------|
| General tangible personal property | Yes | Full rate | Va. Code Section 58.1-603 | [T1] |
| Grocery food (food for home consumption) | **Reduced rate: 1%** | 1% (state removed its 1.5% portion effective Jan 1, 2023; local 1% remains in some areas) | Va. Code Section 58.1-611.1 | [T1] |
| Prepared food (restaurant meals) | Yes | Full rate | Va. Code Section 58.1-603 | [T1] |
| Clothing and footwear | Yes | Full rate | No exemption | [T1] |
| Prescription drugs | Exempt | 0% | Va. Code Section 58.1-609.10(9) | [T1] |
| Over-the-counter drugs | Exempt | 0% | Va. Code Section 58.1-609.10(10) | [T1] |
| Durable medical equipment | Exempt (with prescription) | 0% | Va. Code Section 58.1-609.10(11) | [T1] |
| Motor vehicles | Yes | Full rate (but paid at DMV, not seller) | Va. Code Section 58.1-603 | [T1] |
| Gasoline and motor fuel | Exempt from sales tax (separate motor fuel tax) | N/A | Va. Code Section 58.1-609.10(3) | [T1] |
| Utilities (residential) | Exempt | 0% | Va. Code Section 58.1-609.1(4) | [T1] |
| Utilities (commercial) | Yes | Full rate | Va. Code Section 58.1-603 | [T1] |
| Industrial manufacturing materials | Exempt (for use in manufacturing) | 0% | Va. Code Section 58.1-609.3(2) | [T2] |
| Agricultural supplies | Exempt | 0% | Va. Code Section 58.1-609.2 | [T1] |
| Software -- canned (tangible medium) | Yes | Full rate | Va. Code Section 58.1-602 | [T1] |
| Software -- canned (electronic delivery) | Yes | Full rate | Virginia Tax Ruling 12-68 | [T2] |
| Software -- custom | Exempt | 0% | Va. Code Section 58.1-609.5(1) | [T2] |
| SaaS (Software as a Service) | **Taxable** | Full rate | Virginia Tax Ruling 19-45; PD 19-55 | [T2] |
| Digital goods (e-books, music, video) | Yes | Full rate | Virginia Tax Ruling | [T2] |
| Data processing services | Not taxable | 0% | Not enumerated | [T2] |
| Data center equipment | Exempt (qualifying data centers) | 0% | Va. Code Section 58.1-609.3(18) | [T2] |

### 2.3 Grocery Food -- Critical 2023 Change [T1]

Effective **January 1, 2023**, Virginia eliminated the **state** portion of sales tax on grocery food:

- **Before Jan 1, 2023:** Grocery food was taxed at 2.5% (1.5% state + 1% local).
- **After Jan 1, 2023:** Grocery food is taxed at **1%** (0% state + 1% local only).
- In regional tax areas, the regional component is also removed from grocery food. [T1]
- **Prepared food** remains taxable at the full applicable rate. [T1]
- The definition of "food purchased for human consumption" follows Va. Code Section 58.1-611.1 and generally aligns with the federal SNAP definition. [T1]

**Authority:** HB 90 / SB 451 (2022 Session); Va. Code Section 58.1-611.1.

### 2.4 SaaS Taxability -- Virginia's Position [T2]

Virginia **taxes SaaS** as the sale of tangible personal property delivered electronically:

- Virginia has broadly interpreted its definition of tangible personal property to include electronically delivered software. [T2]
- SaaS is treated as a subscription to use software, which Virginia considers a taxable lease of TPP. [T2]
- The tax applies regardless of whether the software is accessed via browser or app. [T2]
- **Infrastructure as a Service (IaaS)** and **Platform as a Service (PaaS)** taxability is less clear and should be evaluated on a case-by-case basis. [T3]

**Source:** Virginia Tax Ruling PD 19-55; Public Document 19-45.

### 2.5 Services Taxability [T2]

Virginia taxes only specifically enumerated services:

| Service | Taxable? | Authority |
|---------|----------|-----------|
| Repair and maintenance of TPP | Yes (labor + parts) | Va. Code Section 58.1-603 |
| Telecommunications services | Yes | Va. Code Section 58.1-602 |
| Hotel/lodging | Yes (plus local transient occupancy taxes) | Va. Code Section 58.1-603 |
| Professional services (legal, accounting) | No | Not enumerated |
| Personal services (haircuts, dry cleaning) | No | Not enumerated |
| Landscape services | No | Not enumerated |
| Construction services | No (materials taxable at purchase) | DOR guidance |
| Transportation/freight (separately stated) | Exempt | Va. Code Section 58.1-609.5(3) |

---

## Step 3: Return Form Structure
### 3.1 Registration

All sellers with nexus in Virginia must register with Virginia Tax before making taxable sales. Registration is completed through the Virginia Tax Online portal.

**Authority:** Va. Code Section 58.1-613.

### 3.2 Filing Frequency

Virginia uses a **monthly** filing schedule for all active registrants:

| Filing Status | Frequency | Due Date |
|---------------|-----------|----------|
| Standard (all registrants) | Monthly | 20th of the following month |
| Seasonal filers | Monthly during active season | 20th of the following month |

**Note:** Virginia does not offer quarterly or annual filing options for general sales tax filers (unlike many states). All registrants file monthly. [T1]

### 3.3 Returns and Payment

- **Form ST-9** (Retail Sales and Use Tax Return) is the primary return. [T1]
- The return covers both state and local taxes (the local 1% is reported and remitted with the state return). [T1]
- Electronic filing is required for all filers. [T1]
- Payment is due on the same date as the return (20th of the following month). [T1]

### 3.4 Dealer's Discount

Virginia provides a **dealer's discount** for timely filing and payment:

- Dealers may retain the greater of **$0** or an amount computed as follows: [T1]
  - On collections of the first $62,500 of taxable sales: **1.6%** of tax due.
  - The maximum discount is approximately **$53 per month** (for monthly filers with sufficient sales volume). [T1]
- The discount is available only if the return is filed and payment is made on time. [T1]

**Authority:** Va. Code Section 58.1-622.

### 3.5 Penalties and Interest

| Violation | Penalty | Authority |
|-----------|---------|-----------|
| Late filing | 6% of tax due per month, up to 30% | Va. Code Section 58.1-635 |
| Late payment | 6% of tax due per month, up to 30% | Va. Code Section 58.1-635 |
| Failure to file | $10 minimum penalty per return | Va. Code Section 58.1-635 |
| Underpayment (negligence) | Additional 6% | Va. Code Section 58.1-635 |
| Fraud | 100% of tax deficiency | Va. Code Section 58.1-635 |
| Interest | Federal underpayment rate + 2% | Va. Code Section 58.1-15 |

### 3.6 Prepayment Requirement [T1]

Virginia does **not** require sales tax prepayments (unlike some states that require estimated payments mid-month for large filers). [T1]

---

## Step 4: Deductibility / Exemptions
### 5.1 Virginia Exemption Certificates

| Certificate | Use Case | Form |
|-------------|----------|------|
| **ST-10** (Sales and Use Tax Certificate of Exemption) | General exemption certificate (resale, exempt organizations) | Form ST-10 |
| **ST-10A** | Manufacturing exemptions | Form ST-10A |
| **ST-11** | Certificate of exemption for government entities | Form ST-11 |
| **ST-12** | Industrial manufacturing/processing exemption | Form ST-12 |
| **ST-13** | Contractor's exemption certificate | Form ST-13 |
| **ST-13A** | Government contractor exemption | Form ST-13A |
| **Streamlined (SSTCE)** | Multi-state (accepted) | SSTCE form |

### 5.2 Requirements for Valid Certificates [T1]

Valid exemption certificates must contain:

1. Purchaser name and address. [T1]
2. Virginia sales tax registration number (for resale). [T1]
3. Nature of the exemption claimed. [T1]
4. Description of property being purchased. [T1]
5. Purchaser's signature. [T1]
6. Date of certificate. [T1]

### 5.3 Good Faith Acceptance [T2]

Virginia relieves sellers of liability when they accept exemption certificates in good faith. However, the seller must exercise reasonable care:

- The certificate must appear valid on its face. [T1]
- The purchase must be consistent with the claimed exemption. [T2]
- If the seller has knowledge that the exemption is invalid, good faith does not apply. [T2]

**Authority:** Va. Code Section 58.1-623(C).

### 5.4 Retention Period

Exemption certificates must be retained for **3 years** from the date of the last sale made under the certificate. [T1]

---


### 6.1 When Use Tax Applies

Virginia use tax is due when:

- Property is purchased from a seller who did not collect Virginia tax. [T1]
- Property purchased for resale is withdrawn for personal/business use. [T1]
- Property is purchased in another state and brought into Virginia for use. [T1]

### 6.2 Use Tax Rate

The use tax rate equals the applicable sales tax rate (5.3%, 6.0%, or 7.0% depending on region). [T1]

### 6.3 Credit for Taxes Paid to Other States

Virginia allows a credit for sales/use tax properly paid to another state, up to the amount of Virginia use tax that would be due. [T1]

**Authority:** Va. Code Section 58.1-611.

### 6.4 Consumer Use Tax Return

- **Businesses:** Report on Form ST-7 (Consumer Use Tax Return) or Form ST-9. [T1]
- **Individuals:** Report on Virginia individual income tax return (Form 760). [T1]

---

## Step 5: Key Thresholds
### 4.1 Physical Nexus

Virginia follows standard physical nexus principles:

- Place of business (office, store, warehouse) in Virginia. [T1]
- Employees or agents operating in Virginia. [T1]
- Inventory stored in Virginia (including FBA). [T1]
- Regular delivery via company vehicles. [T1]
- Affiliate nexus (related entities with physical presence). [T2]

### 4.2 Economic Nexus [T1]

Virginia enacted economic nexus effective **July 1, 2019**.

| Threshold | Value | Measurement Period |
|-----------|-------|--------------------|
| Revenue | **$100,000** in gross revenue from sales into Virginia | Current or prior calendar year |
| Transactions | **200 transactions** delivered into Virginia | Current or prior calendar year |
| Test | **OR** -- either threshold triggers nexus | |

**Authority:** Va. Code Section 58.1-612(C).

### 4.3 Marketplace Facilitator Rules [T1]

Virginia enacted marketplace facilitator legislation effective **July 1, 2019** (concurrent with economic nexus).

- Marketplace facilitators meeting the nexus thresholds must collect and remit. [T1]
- Marketplace sellers are relieved of collection obligation for facilitated sales. [T1]
- A marketplace facilitator is defined as a person who facilitates a retail sale by listing or advertising, collecting payment, and/or transmitting payment to the marketplace seller. [T1]

**Authority:** Va. Code Section 58.1-612(D).

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
1. **NEVER** apply a flat 5.3% rate statewide -- check whether the address is in Northern Virginia (6.0%), Hampton Roads (7.0%), or the rest of Virginia (5.3%). [T1]
2. **NEVER** advise that grocery food is fully exempt from sales tax in Virginia -- it is taxed at a reduced rate of approximately 1% (local component only, after the Jan 2023 change). [T1]
3. **NEVER** advise that SaaS is not taxable in Virginia (it is taxable per DOR rulings). [T1]
4. **NEVER** tell a seller they can file quarterly in Virginia -- Virginia requires monthly filing for all registrants. [T1]
5. **NEVER** confuse Virginia's mandatory 1% local tax with optional local taxes -- every Virginia transaction includes the 1% local component. [T1]
6. **NEVER** apply the grocery food reduced rate to prepared food or restaurant meals. [T1]
7. **NEVER** advise that over-the-counter drugs are taxable in Virginia (they are exempt). [T1]
8. **NEVER** assume motor vehicle tax is collected by the seller -- it is collected by DMV at titling. [T1]
9. **NEVER** ignore the data center exemption for qualifying purchases -- it is a significant incentive. [T2]
10. **NEVER** provide Virginia tax guidance without specifying which regional rate applies to the customer's location. [T1]

---

## Edge Case Registry

### 7.1 Data Center Equipment Exemption [T2]

Virginia offers a significant sales tax exemption for qualifying data centers:

- Qualifying data centers that make a capital investment of at least **$150 million** (or lower thresholds in certain localities) and create a minimum number of jobs are exempt from sales tax on computer equipment and hardware purchased for use in the data center. [T2]
- The exemption also extends to electricity purchased for use in the data center. [T2]
- Application and approval through Virginia Economic Development Partnership (VEDP) required. [T3]

**Authority:** Va. Code Section 58.1-609.3(18).

### 7.2 Mixed Regional Rate Sales [T2]

When a Virginia seller ships within the state, rate determination can be complex:

- A seller located in a 5.3% jurisdiction shipping to Hampton Roads (7.0%) must charge 7.0%. [T1]
- A seller in Hampton Roads shipping to a 5.3% jurisdiction charges 5.3%. [T1]
- For pick-up orders, the seller's location rate applies. [T1]

### 7.3 Motor Vehicle Sales Tax [T1]

- Motor vehicles are subject to the standard sales tax rate, but tax is collected by the **DMV** at the time of titling, not by the dealer. [T1]
- Trade-in allowances reduce the taxable base. [T1]
- The maximum sales tax on motor vehicles was capped historically, but check current law. [T2]

### 7.4 Manufacturing and Industrial Exemptions [T2]

Virginia provides broad exemptions for manufacturers:

- Raw materials and components that become part of the finished product. [T1]
- Machinery and tools used directly in manufacturing. [T2]
- Fuel used directly in manufacturing (not heating). [T2]
- Pollution control equipment. [T2]

**Authority:** Va. Code Section 58.1-609.3.

### 7.5 Nonprofit and Government Exemptions [T2]

- Virginia exempts purchases by federal and state government entities. [T1]
- Qualifying **501(c)(3)** nonprofit organizations may apply for an exemption certificate. [T2]
- The exemption is not automatic -- nonprofits must apply to Virginia Tax and receive a certificate. [T1]
- Churches are generally exempt without needing to apply. [T2]

**Authority:** Va. Code Section 58.1-609.11.

### 7.6 Occasional or Casual Sales [T1]

Virginia exempts from sales tax the **occasional sale** of tangible personal property by a person not regularly engaged in the business of selling:

- Three or fewer sales in a 12-month period qualify. [T1]
- Motor vehicles, watercraft, and aircraft are **not** eligible for the casual sale exemption. [T1]

**Authority:** Va. Code Section 58.1-602 (definition of "occasional sale").

### 7.7 Digital Advertising Tax [T2]

Unlike Maryland, Virginia does **not** impose a separate digital advertising tax. However, digital goods and SaaS remain subject to the standard sales tax. [T2]

### 7.8 School Supply and Clothing Tax Holiday [T1]

Virginia holds an annual **sales tax holiday** (typically the first weekend in August):

- School supplies ($20 or less per item): exempt. [T1]
- Clothing and footwear ($100 or less per item): exempt. [T1]
- Energy-efficient products (qualifying Energy Star products, $2,500 or less): exempt. [T1]
- Hurricane and emergency preparedness items: exempt. [T1]

**Authority:** Va. Code Section 58.1-611.2.

---

## Test Suite

### Test 1: Standard Rate Calculation [T1]

**Question:** A retailer in Richmond (Central Virginia, 6.0% total) sells a $1,000 laptop. What is the sales tax?

**Expected Answer:** $1,000 x 6.0% = $60.00.

### Test 2: Grocery Food Rate [T1]

**Question:** A consumer buys $300 of groceries in Virginia Beach (Hampton Roads). What tax is due on the groceries?

**Expected Answer:** After Jan 1, 2023, grocery food is taxed at approximately 1% (local portion only). $300 x 1% = $3.00. The state and regional portions do not apply to grocery food.

### Test 3: SaaS Taxability [T2]

**Question:** A Virginia company subscribes to a $500/month CRM SaaS product. Is Virginia sales tax due?

**Expected Answer:** Yes. Virginia taxes SaaS. At the applicable rate for the company's location (e.g., 5.3% in standard Virginia = $26.50/month; 6.0% in NOVA = $30.00/month; 7.0% in Hampton Roads = $35.00/month).

### Test 4: Regional Rate Determination [T1]

**Question:** An online retailer in Roanoke (5.3%) ships a $200 order to a customer in Arlington (NOVA, 6.0%). What rate applies?

**Expected Answer:** 6.0%. For shipped goods, Virginia uses destination-based sourcing, so the buyer's location rate applies. Tax = $200 x 6.0% = $12.00.

### Test 5: Economic Nexus [T1]

**Question:** An out-of-state seller made $50,000 in sales but 210 transactions into Virginia this year. Does the seller have nexus?

**Expected Answer:** Yes. Virginia uses an OR test. The seller exceeded the 200-transaction threshold, so economic nexus is triggered even though revenue is below $100,000.

### Test 6: Sales Tax Holiday [T1]

**Question:** During Virginia's sales tax holiday in August, a customer buys a $90 pair of shoes and a $110 jacket. Which items qualify?

**Expected Answer:** The $90 shoes qualify (under $100 threshold) and are exempt. The $110 jacket does NOT qualify (exceeds $100 per-item limit) and is taxable at the full applicable rate.

### Test 7: Use Tax on Out-of-State Purchase [T1]

**Question:** A Virginia Beach (7.0%) resident buys a $2,000 piece of furniture online from a seller who charges 4% sales tax (from another state). What Virginia use tax is owed?

**Expected Answer:** Virginia use tax at 7.0% = $140. Credit for tax paid to other state: $2,000 x 4% = $80. Net Virginia use tax owed: $140 - $80 = $60.

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
