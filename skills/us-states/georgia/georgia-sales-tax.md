---
name: georgia-sales-tax
description: Use this skill whenever asked about Georgia sales tax, Georgia use tax, Georgia sales tax nexus, Georgia sales tax returns, Georgia exemption certificates, taxability of goods or services in Georgia, or any request involving Georgia state-level consumption taxes. Trigger on phrases like "Georgia sales tax", "GA sales tax", "Georgia use tax", "Georgia nexus", "Georgia exemption certificate", "Georgia resale certificate", "O.C.G.A. 48-8", "Georgia DOR sales tax", or any request involving Georgia sales and use tax filing, classification, or compliance. ALWAYS read the parent us-sales-tax skill first for federal context, then layer this Georgia-specific skill on top.
---

# Georgia Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Georgia, United States |
| Jurisdiction Code | US-GA |
| Tax Type | Sales and Use Tax |
| State Tax Rate | 4% |
| Maximum Combined Rate | 8% (4% state + up to 4% local) |
| Primary Legal Framework | Official Code of Georgia Annotated (O.C.G.A.) Title 48, Chapter 8 |
| Governing Body | Georgia Department of Revenue (DOR) |
| Filing Portal | Georgia Tax Center (GTC) -- https://gtc.dor.ga.gov |
| Economic Nexus Effective Date | January 1, 2019 |
| SST Member | No |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate lookups, basic nexus determination, standard taxability. Tier 2: complex exemptions, multi-jurisdiction local rate disputes, digital goods classification. Tier 3: audit defense, penalty abatement, administrative appeals. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Georgia sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Georgia sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Georgia? | Drives taxability classification under Georgia law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Georgia? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Georgia local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Rate

Georgia imposes a **4% state sales and use tax** on the retail sale, lease, or rental of tangible personal property and certain services. This is among the lower state-level rates in the US.

**Statutory authority:** O.C.G.A. Section 48-8-30(a).

### 1.2 Local Rates

Georgia permits counties and certain special districts to levy additional local sales taxes. Local taxes are layered on top of the 4% state rate:

| Local Tax Type | Rate | Authority |
|----------------|------|-----------|
| Local Option Sales Tax (LOST) | 1% | O.C.G.A. Section 48-8-82 |
| Special Purpose Local Option Sales Tax (SPLOST) | 1% | O.C.G.A. Section 48-8-110 |
| Education SPLOST (ESPLOST) | 1% | O.C.G.A. Section 48-8-140 |
| Transportation SPLOST (TSPLOST) | Up to 1% | O.C.G.A. Section 48-8-269 |
| Municipal Option Sales Tax (MOST) | Up to 1% (in select cities) | O.C.G.A. Section 48-8-96 |
| Homestead Option Sales Tax (HOST) | 1% | O.C.G.A. Section 48-8-102 |

**Maximum combined rate:** 4% state + up to 4% local = **8% total**. [T1]

Not all counties levy every available local tax. The actual combined rate depends on the specific county (and in some cases, city) where the transaction is sourced.

### 1.3 Rate Lookup

Georgia publishes a quarterly-updated rate table by county/city. The DOR provides a downloadable spreadsheet of all local rates effective for each quarter.

**Source:** Georgia DOR -- Sales Tax Rate Charts, available at https://dor.georgia.gov/sales-tax-rates

### 1.4 Sourcing Rules [T1]

Georgia is a **destination-based** sourcing state for most transactions:

- **Intrastate sales:** Tax is based on the delivery location (ship-to address). [T1]
- **Interstate sales (remote sellers):** Destination-based. [T1]
- **Over-the-counter (walk-in):** Sourced to the seller's location. [T1]

**Exception:** Motor vehicles are sourced to the county of registration, not the point of sale. Motor vehicles are subject to a separate Title Ad Valorem Tax (TAVT) rather than traditional sales tax (see Section 7 edge cases). [T2]

---

## Step 2: Transaction Classification Rules
### 2.1 General Rule

Georgia sales tax applies to the retail sale of **tangible personal property (TPP)** unless specifically exempted. O.C.G.A. Section 48-8-30.

### 2.2 Taxability Matrix

| Item Category | Taxable? | Rate | Authority | Tier |
|---------------|----------|------|-----------|------|
| General tangible personal property | Yes | Full rate | O.C.G.A. Section 48-8-30 | [T1] |
| Grocery food (food for home consumption) | **Exempt** from state 4%; local tax may still apply | 0% state | O.C.G.A. Section 48-8-3(57) | [T1] |
| Prepared food (restaurant meals) | Yes | Full rate | O.C.G.A. Section 48-8-3(57)(B) | [T1] |
| Clothing and footwear | Yes | Full rate | No exemption | [T1] |
| Prescription drugs | Exempt | 0% | O.C.G.A. Section 48-8-3(1) | [T1] |
| Over-the-counter drugs | Yes | Full rate | Not specifically exempt | [T1] |
| Durable medical equipment | Exempt (with prescription) | 0% | O.C.G.A. Section 48-8-3(2) | [T1] |
| Motor vehicles (new/used) | TAVT applies, not sales tax | Varies (currently 6.6% TAVT) | O.C.G.A. Section 48-5C | [T2] |
| Gasoline and motor fuel | Exempt from sales tax (subject to motor fuel excise tax) | N/A | O.C.G.A. Section 48-8-3(12) | [T1] |
| Utilities (electricity, natural gas) | Yes (residential and commercial) | Full rate | O.C.G.A. Section 48-8-30 | [T1] |
| Industrial machinery (direct use) | Exempt | 0% | O.C.G.A. Section 48-8-3(34) | [T2] |
| Agricultural supplies and equipment | Exempt | 0% | O.C.G.A. Section 48-8-3(29)-(31) | [T1] |
| Packaging materials (for resale goods) | Exempt | 0% | O.C.G.A. Section 48-8-3(36) | [T1] |
| Software -- canned (tangible medium) | Yes | Full rate | DOR ruling | [T1] |
| Software -- canned (electronic delivery) | Yes | Full rate | Ga. Comp. R. & Regs. 560-12-2-.111 | [T2] |
| Software -- custom | Exempt | 0% | DOR guidance | [T2] |
| SaaS (Software as a Service) | **Not taxable** | 0% | Georgia DOR Letter Ruling LR SUT-2019-02 | [T2] |
| Digital goods (e-books, music, video) | Yes (electronically delivered) | Full rate | O.C.G.A. Section 48-8-2(31)(A) | [T2] |
| Data processing services | Not taxable | 0% | Not enumerated | [T2] |
| Coins and bullion (gold/silver) | Exempt | 0% | O.C.G.A. Section 48-8-3(62) | [T1] |

### 2.3 Grocery Food -- Important Distinction [T1]

Georgia exempts **food and food ingredients for home consumption** from the **state** 4% sales tax. However:

- **Local sales taxes** (LOST, SPLOST, ESPLOST, etc.) **still apply** to grocery food in most jurisdictions. [T1]
- **Prepared food** remains fully taxable at both state and local rates. [T1]
- Georgia follows the Streamlined Sales Tax definition of "food and food ingredients" for purposes of this exemption, even though Georgia is not an SST member. [T2]
- **Candy** and **soft drinks** are treated as **food** in Georgia (exempt from state tax), unlike in some SST member states. [T1]

**Practical impact:** A consumer in a county with 3% local tax pays 0% state + 3% local = 3% on groceries, but 4% + 3% = 7% on prepared food.

### 2.4 Services Taxability [T2]

Georgia does **not** impose a broad-based tax on services. Only specifically enumerated services are taxable:

| Service | Taxable? | Authority |
|---------|----------|-----------|
| Repair and maintenance of TPP | Yes (labor + parts) | O.C.G.A. Section 48-8-30 |
| Installation services (when part of sale of TPP) | Yes | DOR guidance |
| Telecommunications services | Yes | O.C.G.A. Section 48-8-30 |
| Cable/satellite television | Yes | O.C.G.A. Section 48-8-30 |
| Hotel/motel accommodations | Yes (plus local hotel/motel taxes) | O.C.G.A. Section 48-8-30 |
| Motor vehicle parking (commercial lots) | Yes (in certain jurisdictions) | Local ordinances |
| Professional services (legal, accounting, consulting) | No | Not enumerated |
| Personal services (haircuts, spa, dry cleaning) | No | Not enumerated |
| Construction/real property improvement | No (materials taxable at purchase) | DOR guidance |
| Transportation/shipping charges | Exempt if separately stated | O.C.G.A. Section 48-8-3(41) |
| Janitorial/cleaning services | No | Not enumerated |

---

## Step 3: Return Form Structure
### 3.1 Registration

Every seller making taxable sales in Georgia must register for a **Sales and Use Tax Certificate of Registration** before commencing business. Registration is completed through the Georgia Tax Center (GTC).

**Authority:** O.C.G.A. Section 48-8-59.

### 3.2 Filing Frequency

| Annual Tax Liability | Filing Frequency | Due Date |
|----------------------|------------------|----------|
| $0 -- $800 per year | Quarterly | 20th of the month following the quarter-end |
| $801 -- $24,000 per year | Monthly | 20th of the following month |
| Over $24,000 per year | Monthly | 20th of the following month |

**Note:** The DOR may assign a filing frequency based on expected tax liability at registration. Frequency may be adjusted as actual filing history develops. [T1]

### 3.3 Returns and Payment

- **Form ST-3** (Sales and Use Tax Return) is the primary return. [T1]
- Returns must be filed electronically through the Georgia Tax Center (GTC). [T1]
- Payment is due on the same date as the return (20th of the month). [T1]
- If the 20th falls on a weekend or state holiday, the due date moves to the next business day. [T1]

### 3.4 Vendor Discount (Timely Filing Credit)

Georgia offers a **vendor discount** for timely filing and payment:

- **3% of the first $3,000** of tax due per reporting period, capped at **$90 per period** (monthly filers) or **$270 per period** (quarterly filers). [T1]
- The discount is available only if the return is filed and payment is made by the due date. [T1]
- The discount applies to the **state** portion of tax only (not local taxes). [T1]

**Authority:** O.C.G.A. Section 48-8-50.

### 3.5 Penalties and Interest

| Violation | Penalty | Authority |
|-----------|---------|-----------|
| Late filing | 5% of tax due per month, up to 25% | O.C.G.A. Section 48-2-44(a) |
| Late payment | 5% of tax due per month, up to 25% | O.C.G.A. Section 48-2-44(a) |
| Failure to file | 5% per month, up to 25% + potential criminal penalties | O.C.G.A. Section 48-2-44 |
| Underpayment (negligence) | 5% of underpaid amount | O.C.G.A. Section 48-2-44(b) |
| Fraud | 50% of deficiency | O.C.G.A. Section 48-2-44(c) |
| Interest | Federal short-term rate + 3%, compounded monthly | O.C.G.A. Section 48-2-40 |

### 3.6 Zero Returns

Sellers must file returns even if no tax is due for the period. Failure to file zero returns can result in penalties and may cause the DOR to estimate tax due. [T1]

---

## Step 4: Deductibility / Exemptions
### 5.1 Georgia Exemption Certificates

Georgia accepts the following exemption certificates:

| Certificate | Use Case | Authority |
|-------------|----------|-----------|
| **ST-5** (Sales Tax Certificate of Exemption) | General exemption certificate for exempt organizations | DOR Form ST-5 |
| **ST-5 (Resale)** | Purchases for resale | Resale provision |
| **Streamlined Sales Tax Certificate of Exemption (SSTCE)** | Multi-state exemption (accepted even though GA is not SST member) | DOR policy |
| **Manufacturer's Exemption Certificate** | Direct-use machinery in manufacturing | O.C.G.A. Section 48-8-3(34) |
| **Agricultural Exemption Certificate** | Farm supplies and equipment | O.C.G.A. Section 48-8-3(29) |

### 5.2 Requirements for Valid Certificates [T1]

A valid exemption certificate must include:

1. Purchaser's name and address. [T1]
2. Seller's name and address. [T1]
3. Description of goods or services being purchased. [T1]
4. Reason for exemption (resale, manufacturing, agricultural, etc.). [T1]
5. Georgia sales tax registration number (for resale certificates). [T1]
6. Signature of purchaser (or authorized agent). [T1]
7. Date. [T1]

### 5.3 Good Faith Acceptance [T2]

Sellers who accept a properly completed exemption certificate in **good faith** are relieved of liability for uncollected tax, even if the certificate is later found to be invalid, provided:

- The certificate was taken at or before the time of sale. [T1]
- The certificate was complete on its face. [T1]
- The seller had no reason to believe the certificate was fraudulent. [T2]

**Authority:** O.C.G.A. Section 48-8-38(a).

### 5.4 Certificate Retention

Exemption certificates must be retained for **3 years** from the date of the last transaction covered by the certificate, or 3 years from the date the certificate was presented, whichever is later. [T1]

---


### 6.1 When Use Tax Applies

Georgia use tax applies when:

- Tangible personal property is purchased from an out-of-state seller who did not collect Georgia sales tax. [T1]
- Property is purchased tax-free for resale but later withdrawn for the purchaser's own use. [T1]
- Property is purchased in another state with a lower tax rate and brought into Georgia for use (Georgia allows a credit for tax paid to another state). [T1]

### 6.2 Use Tax Rate

The use tax rate is identical to the sales tax rate that would have applied had the purchase been made in Georgia: **4% state + applicable local rates**. [T1]

### 6.3 Use Tax Reporting

- **Businesses:** Report use tax on Form ST-3 (same as sales tax return). [T1]
- **Individuals:** Report on Georgia Form 500 (individual income tax return), Line 15. [T1]

**Authority:** O.C.G.A. Section 48-8-30(b).

---

## Step 5: Key Thresholds
### 4.1 Physical Nexus

Georgia follows standard physical nexus principles. A seller has physical nexus in Georgia if it has:

- A place of business in Georgia (office, warehouse, store). [T1]
- Employees, agents, or representatives in Georgia. [T1]
- Inventory stored in Georgia (including FBA). [T1]
- Delivery vehicles making regular trips into Georgia. [T1]
- Property (owned or leased) in Georgia. [T1]

### 4.2 Economic Nexus [T1]

Georgia enacted economic nexus effective **January 1, 2019**.

| Threshold | Value | Measurement Period |
|-----------|-------|--------------------|
| Revenue | **$100,000** in gross revenue from sales into Georgia | Current or prior calendar year |
| Transactions | **200 transactions** delivered into Georgia | Current or prior calendar year |
| Test | **OR** -- either threshold triggers nexus | |

**Authority:** O.C.G.A. Section 48-8-2(8)(M.1).

**Important notes:**

- Exempt sales count toward the threshold. [T2]
- Wholesale (resale) sales count toward the threshold. [T2]
- Marketplace sales facilitated by a marketplace facilitator are generally **excluded** from the seller's threshold calculation (the marketplace bears the obligation). [T1]
- Once nexus is triggered, registration must occur within **30 days**. [T1]

### 4.3 Marketplace Facilitator Rules [T1]

Georgia enacted marketplace facilitator legislation effective **April 1, 2020**.

- Marketplace facilitators meeting the economic nexus threshold must collect and remit sales tax on behalf of marketplace sellers. [T1]
- The marketplace seller is relieved of the collection obligation for marketplace-facilitated sales. [T1]
- The marketplace seller remains responsible for direct-channel sales. [T1]

**Authority:** O.C.G.A. Section 48-8-2(8)(M.2).

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
1. **NEVER** provide a combined rate for a Georgia address without verifying the current local rate for that specific county/city. Local rates change quarterly. [T1]
2. **NEVER** advise that SaaS is taxable in Georgia under current law (it is not, per DOR guidance). [T1]
3. **NEVER** advise that grocery food is subject to the 4% state tax (it is exempt from the state portion). [T1]
4. **NEVER** apply sales tax to motor vehicles (Georgia uses TAVT, not sales tax on vehicles). [T1]
5. **NEVER** assume a local tax rate without looking it up -- Georgia has 159 counties and rates vary significantly. [T1]
6. **NEVER** file a return without including local taxes (the ST-3 requires reporting of state and all applicable local taxes). [T1]
7. **NEVER** advise that Georgia is an SST member state (it is not). [T1]
8. **NEVER** calculate economic nexus thresholds using marketplace-facilitated sales when the marketplace is collecting. [T1]
9. **NEVER** apply a vendor discount to the local tax portion (the discount applies only to state tax). [T1]
10. **NEVER** provide tax advice for Georgia without recommending verification of current rates and rules with the DOR, as Georgia law changes frequently. [T2]

---

## Edge Case Registry

### 7.1 Title Ad Valorem Tax (TAVT) -- Motor Vehicles [T2]

Georgia replaced its sales tax on motor vehicles with the **Title Ad Valorem Tax (TAVT)** effective March 1, 2013.

- TAVT is a **one-time** tax paid at the time of title transfer. [T1]
- Current rate: **6.6%** of the fair market value. [T1]
- TAVT replaces both the sales tax and the annual ad valorem (property) tax on vehicles. [T1]
- Used vehicles between private parties are also subject to TAVT. [T1]
- Certain transfers (gifts between immediate family members, inheritance) have a reduced TAVT rate of **0.5%**. [T1]

**Authority:** O.C.G.A. Section 48-5C-1.

### 7.2 SaaS and Cloud Computing [T2]

Georgia does **not** tax SaaS or cloud-based software:

- The Georgia DOR has ruled that SaaS is not tangible personal property and does not constitute a taxable service. [T2]
- The key distinction is whether the customer receives a **deliverable** (taxable canned software) or merely **access** to hosted software (not taxable). [T2]
- Infrastructure as a Service (IaaS) and Platform as a Service (PaaS) are also not taxable under current Georgia guidance. [T2]

**Source:** Georgia DOR Letter Ruling LR SUT-2019-02; DOR Policy Bulletin SUT-2010-1006.

**CAUTION:** This area is evolving. Georgia's legislature could change the taxability of digital services at any time. Always verify current guidance. [T3]

### 7.3 Drop Shipments [T2]

A drop shipment occurs when a retailer directs a manufacturer or distributor to ship goods directly to the retailer's customer.

- In Georgia, the retailer is treated as the seller and must collect tax from the end customer. [T1]
- The drop shipper can accept a resale certificate from the retailer. [T2]
- If the retailer does not have Georgia nexus, the drop shipper may be required to collect tax from the end customer. [T2]

### 7.4 Leases and Rentals [T2]

- Leases and rentals of tangible personal property are taxable in Georgia. [T1]
- Tax is due on each lease payment (not the total lease value upfront). [T1]
- If the lessee has the option to purchase the property at the end of the lease, tax is due on the purchase price at that time. [T2]

**Authority:** O.C.G.A. Section 48-8-2(31).

### 7.5 Construction Contractors [T2]

Georgia treats construction contractors as the **consumer** of materials they incorporate into real property improvements:

- Contractors pay sales tax when they **purchase** materials. [T1]
- Contractors do **not** collect sales tax from property owners on the finished improvement. [T1]
- Fabrication labor by the contractor is not subject to sales tax. [T1]
- Separately stated repair labor is taxable (repair vs. improvement distinction matters). [T2]

**Authority:** Ga. Comp. R. & Regs. 560-12-2-.21.

### 7.6 Bundled Transactions [T2]

When taxable and non-taxable items are sold together as a single package:

- If the transaction is predominantly taxable (more than 50% of the value), the entire transaction is taxable. [T2]
- If the transaction is predominantly non-taxable, only the taxable portion is taxable, if separately stated. [T2]
- **True object test:** The DOR may apply a "true object" test to determine the primary purpose of the transaction. [T3]

### 7.7 Trade-In Credits [T1]

Georgia allows a deduction for trade-in value on the purchase of tangible personal property of the **same kind**:

- The sales tax base is reduced by the fair market value of the traded-in property. [T1]
- This applies most commonly to motor vehicles (TAVT context) and heavy equipment. [T1]

**Authority:** O.C.G.A. Section 48-8-30(c).

### 7.8 Film Industry Tax Incentives [T2]

Georgia's film tax credit (O.C.G.A. Section 48-7-40.26) interacts with sales tax:

- Qualifying production companies are **exempt** from sales tax on purchases or rentals of tangible personal property used directly in production activities. [T2]
- An exemption certificate specific to film production must be presented. [T2]
- This exemption has been a significant driver of Georgia's film industry. [T2]

---

## Test Suite

These questions should be used to verify correct application of this skill.

### Test 1: Basic Rate Calculation [T1]

**Question:** A retailer in Fulton County, Georgia sells a $500 television to a walk-in customer. Fulton County has a 3% combined local rate. What is the total sales tax?

**Expected Answer:** $500 x (4% state + 3% local) = $500 x 7% = $35.00 total tax.

### Test 2: Grocery Food Exemption [T1]

**Question:** A grocery store in DeKalb County (3% local rate) sells $200 of unprepared food items. What sales tax is due?

**Expected Answer:** $200 x 0% state + $200 x 3% local = $0 + $6.00 = **$6.00**. The state 4% is exempt on grocery food; local taxes still apply.

### Test 3: SaaS Taxability [T2]

**Question:** A Georgia business subscribes to a $1,000/month project management SaaS tool from a vendor with no Georgia presence. Is Georgia sales/use tax due?

**Expected Answer:** No. SaaS is not taxable in Georgia per DOR Letter Ruling LR SUT-2019-02. No sales tax or use tax is due on the subscription.

### Test 4: Economic Nexus [T1]

**Question:** An out-of-state seller made $80,000 in sales and 250 transactions into Georgia in the current year. Does the seller have economic nexus?

**Expected Answer:** Yes. Although the $100,000 revenue threshold was not met, the 200-transaction threshold was exceeded. Georgia uses an OR test, so exceeding either threshold triggers nexus.

### Test 5: TAVT on Vehicle [T2]

**Question:** A customer purchases a new vehicle in Georgia for $40,000. What tax applies?

**Expected Answer:** TAVT of 6.6% applies, not sales tax. TAVT = $40,000 x 6.6% = $2,640 (one-time, at title transfer). No annual ad valorem tax will apply.

### Test 6: Vendor Discount [T1]

**Question:** A monthly filer owes $5,000 in state sales tax and files/pays on time. What vendor discount applies?

**Expected Answer:** 3% of the first $3,000 = $90. The discount is capped at $90 per monthly period. Total remittance: $5,000 - $90 = $4,910 (state portion only).

### Test 7: Drop Shipment [T2]

**Question:** A California retailer (no GA nexus) directs a Georgia manufacturer to ship goods directly to a Georgia customer. Who collects the tax?

**Expected Answer:** The Georgia manufacturer (drop shipper) must collect Georgia sales tax from the end customer because the California retailer lacks nexus. The manufacturer cannot accept a resale certificate from a retailer without Georgia nexus for a Georgia delivery.

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
