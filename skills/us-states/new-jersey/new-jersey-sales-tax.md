---
name: new-jersey-sales-tax
description: Use this skill whenever asked about New Jersey sales and use tax, NJ Division of Taxation filings, NJ clothing exemption, NJ Urban Enterprise Zone, NJ exemptions, NJ nexus, or any request involving New Jersey state sales and use tax compliance. Trigger on phrases like "New Jersey sales tax", "NJ sales tax", "NJ Division of Taxation", "ST-50", "ST-51", "NJ clothing exemption", "Urban Enterprise Zone", "UEZ", "NJ resale certificate", or any request involving New Jersey sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any New Jersey sales tax work.
---

# New Jersey Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | New Jersey, United States |
| Jurisdiction Code | US-NJ |
| Tax Type | Sales and Use Tax (state only -- no local taxes) |
| Primary Legislation | New Jersey Sales and Use Tax Act (N.J.S.A. 54:32B-1 et seq.) |
| Key Statutes | N.J.S.A. 54:32B-1 through 54:32B-39 |
| Tax Authority | New Jersey Division of Taxation (within Department of the Treasury) |
| Filing Portal | https://www.nj.gov/treasury/taxation/ |
| Federal Framework Skill | us-sales-tax (read first for Wayfair, nexus overview, and multi-state context) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires New Jersey CPA or EA sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate structure, clothing exemption, UEZ rules, basic taxability, filing mechanics, nexus thresholds. Tier 2: SaaS/digital goods, mixed transactions, UEZ qualification. Tier 3: audit defense, complex bundled transactions, Division rulings. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to a licensed tax professional and document the gap.

---

## Step 0: Client Onboarding Questions

Before proceeding with any New Jersey sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a New Jersey sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in New Jersey? | Drives taxability classification under New Jersey law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in New Jersey? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple New Jersey local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Rate

The New Jersey state sales and use tax rate is **6.625%**. [T1]

**Legislation:** N.J.S.A. 54:32B-3.

### 1.2 No Local Taxes

New Jersey imposes **no local or county sales taxes**. The 6.625% rate is uniform statewide. [T1]

This is a significant simplification compared to most other states. Every transaction in New Jersey uses the same rate (with the exception of UEZ reduced rate -- see below). [T1]

### 1.3 Urban Enterprise Zone (UEZ) Reduced Rate [T1]

Qualified retailers operating within designated **Urban Enterprise Zones** may collect sales tax at a reduced rate of **3.3125%** (exactly 50% of the standard rate). [T1]

- Only applies to **in-person** sales made at a qualified UEZ retail location. [T1]
- Does NOT apply to online or remote sales. [T1]
- The retailer must be certified by the UEZ Authority and have a valid UEZ certificate. [T1]
- UEZ cities include: Newark, Jersey City, Camden, Paterson, Trenton, Elizabeth, and others. [T1]

**Legislation:** N.J.S.A. 52:27H-60 et seq. (Urban Enterprise Zones Act); N.J.A.C. 18:24-31.

### 1.4 Sourcing [T1]

Since there are no local rate variations (except UEZ), sourcing is straightforward:

- All transactions in New Jersey are taxed at **6.625%** (or 3.3125% for qualifying UEZ in-person sales). [T1]
- For remote sellers, destination is New Jersey = 6.625%. [T1]

---

## Step 3: Return Form Structure
### 5.1 Filing Form

The primary returns are:

- **Form ST-50 -- Monthly Remittance Statement** (monthly filers). [T1]
- **Form ST-51 -- Quarterly Return** (all filers, whether monthly or quarterly). [T1]

Monthly filers file ST-50 for the first two months of each quarter and ST-51 for the third month (which also serves as the quarterly reconciliation). [T1]

### 5.2 Filing Frequency [T1]

| Frequency | Criteria | Due Date |
|-----------|----------|----------|
| Monthly | Tax liability > $500/month | 20th of the following month (ST-50 for months 1-2, ST-51 for month 3) |
| Quarterly | Tax liability $500 or less/month | 20th of the month following the quarter (ST-51) |
| Annual | Tax liability less than $500/year | January 20 following the year |

**Quarterly due dates:**

| Quarter | Period | Due Date |
|---------|--------|----------|
| Q1 | January 1 -- March 31 | April 20 |
| Q2 | April 1 -- June 30 | July 20 |
| Q3 | July 1 -- September 30 | October 20 |
| Q4 | October 1 -- December 31 | January 20 |

**Legislation:** N.J.S.A. 54:32B-17.

### 5.3 Electronic Filing [T1]

- Electronic filing is **required** for all monthly and quarterly filers through **NJ Division of Revenue Online Services**. [T1]
- Paper filing is generally no longer accepted for most filers. [T1]

### 5.4 Vendor Discount [T1]

New Jersey does **NOT** offer a vendor discount. Sellers retain no portion of collected tax. [T1]

### 5.5 Penalties and Interest [T1]

| Penalty | Rate | Citation |
|---------|------|----------|
| Late filing | 5% of tax due per month (max 25%) | N.J.S.A. 54:49-4 |
| Late payment | Same | N.J.S.A. 54:49-4 |
| Negligence | 5% of deficiency | N.J.S.A. 54:49-7 |
| Fraud | 50% of deficiency | N.J.S.A. 54:49-8 |
| Interest | Prime rate + percentage (set quarterly) | N.J.S.A. 54:49-3.1 |

---

## Step 4: Deductibility / Exemptions
### 7.1 New Jersey Resale Certificate [T1]

- **Form:** ST-3 (Resale Certificate). [T1]
- Must include the buyer's NJ Certificate of Authority number. [T1]
- Blanket certificates permitted. [T1]
- NJ also accepts the **MTC Uniform Sales Tax Certificate** and the **SST Certificate of Exemption**. [T1]

### 7.2 Exempt Organization Certificate [T1]

- **Form:** ST-5 (Exempt Organization Certificate). [T1]
- Organization must apply and be approved by Division of Taxation. [T1]
- Has an expiration date and must be renewed. [T1]

### 7.3 Other Certificates [T1]

| Certificate | Form | Purpose |
|------------|------|---------|
| Farmer's Exemption | ST-7 | Agricultural purchases |
| Government Entity | ST-13 | Government exempt purchases |
| Diplomatic | ST-15 | Foreign diplomat purchases |
| UEZ Purchase | UZ-5 | Purchases for UEZ business use |

---


### 6.1 When Use Tax Applies

Use tax applies when:

- A New Jersey purchaser acquires TPP or taxable services from a seller who did not collect NJ tax. [T1]
- TPP is purchased tax-free and diverted to taxable use. [T1]
- TPP is brought into New Jersey for use, storage, or consumption. [T1]

**Legislation:** N.J.S.A. 54:32B-6.

### 6.2 Use Tax Rate [T1]

Use tax rate is **6.625%** (same as sales tax -- no local variation). [T1]

### 6.3 Reporting Use Tax [T1]

- **Registered sellers:** Report on ST-51 quarterly return. [T1]
- **Individuals:** Report on NJ-1040 (New Jersey Income Tax Return), Line 51. [T1]
- **Businesses not registered:** File Form ST-18B (Use Tax Return). [T1]

### 6.4 Credit for Tax Paid to Other States [T1]

New Jersey allows a credit for sales/use tax legally paid to another state. N.J.S.A. 54:32B-11(2). [T1]

---

## Step 5: Key Thresholds
### 4.1 Who Must Register

Any seller required to collect NJ sales tax must register with the Division of Taxation and obtain a **New Jersey Certificate of Authority (Form CA-1)** or register online via NJ Business Gateway. N.J.S.A. 54:32B-16. [T1]

### 4.2 Economic Nexus Threshold [T1]

New Jersey's economic nexus threshold:

- **$100,000** in gross revenue from sales into New Jersey, **OR** [T1]
- **200 or more separate transactions** in New Jersey. [T1]
- Measured during the current or preceding calendar year. [T1]
- Effective date: November 1, 2018. [T1]

**Legislation:** N.J.S.A. 54:32B-2(i)(2)(B).

### 4.3 Marketplace Facilitator Rules [T1]

New Jersey requires marketplace facilitators to collect and remit sales tax:

- Effective November 1, 2018. [T1]
- Marketplace facilitators are treated as retailers. [T1]
- Marketplace sellers relieved for facilitated sales. [T1]

**Legislation:** N.J.S.A. 54:32B-2(mm); N.J.S.A. 54:32B-3.6.

### 4.4 Registration Process [T1]

1. Register online via **NJ Business Gateway** (https://www.njportal.com/DOR/BusinessRegistration). [T1]
2. Receive a **Certificate of Authority** with NJ Tax ID. [T1]
3. Filing frequency assigned by Division of Taxation. [T1]
4. No fee for registration. [T1]

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
- **NEVER** charge sales tax on clothing in New Jersey -- clothing is exempt regardless of price. [T1]
- **NEVER** apply the UEZ reduced rate to online, phone, or mail-order sales -- UEZ rate is for in-person sales only. [T1]
- **NEVER** treat candy and soft drinks as taxable in NJ -- they are exempt as food items (when not sold as prepared food). [T1]
- **NEVER** apply local or county tax rates -- NJ has NO local sales taxes. The rate is uniform at 6.625%. [T1]
- **NEVER** assume a shore tourism surcharge exists -- there is no special rate for tourist/shore areas. [T1]
- **NEVER** treat SaaS as nontaxable in NJ -- SaaS is taxable as prewritten software. [T1]
- **NEVER** assume residential energy is taxable -- residential gas and electric are exempt. [T1]
- **NEVER** forget that paper products (towels, tissues, toilet paper) are exempt in NJ. [T1]
- **NEVER** assume OTC drugs are taxable -- New Jersey EXEMPTS OTC drugs and medicine. [T1]
- **NEVER** assume the vendor retains a discount -- NJ has NO vendor discount for timely filing. [T1]

---

## Edge Case Registry

### EC1 -- Urban Enterprise Zone Sales [T1]

**Situation:** A certified UEZ retailer in Newark makes an in-person sale of a $1,000 appliance.

**Resolution:** The UEZ retailer collects the reduced rate of **3.3125%** (50% of 6.625%). Tax = $33.13. The retailer must be UEZ-certified and the sale must be made in person at the qualifying UEZ location. N.J.S.A. 52:27H-60 et seq.

### EC2 -- UEZ Online Sales Not Qualifying [T1]

**Situation:** The same Newark UEZ retailer sells the same appliance to a NJ customer through their website (shipped to customer's home).

**Resolution:** The UEZ reduced rate does NOT apply to online/remote sales. The retailer must collect the full **6.625%** rate on the online sale. Tax = $66.25. The UEZ rate only applies to in-person retail transactions at the qualified physical location.

### EC3 -- Clothing Exemption -- No Price Cap [T1]

**Situation:** A customer purchases a $2,000 designer suit in a NJ store.

**Resolution:** EXEMPT. New Jersey's clothing exemption has NO price cap. Unlike New York (which caps at $110), NJ exempts all clothing regardless of price. Sales tax = $0. N.J.S.A. 54:32B-8.4.

### EC4 -- Paper Products Exemption [T1]

**Situation:** A customer purchases paper towels, toilet paper, and disposable diapers.

**Resolution:** Disposable paper products (paper towels, toilet paper, facial tissues, napkins) are EXEMPT in New Jersey. Disposable diapers are also EXEMPT. N.J.S.A. 54:32B-8.21. This is unusual -- most states tax these items.

### EC5 -- SaaS Taxability [T1]

**Situation:** A NJ business subscribes to cloud-based HR software for $500/month.

**Resolution:** TAXABLE at 6.625%. Tax = $33.13/month. NJ treats SaaS as a sale/license of prewritten computer software. TB-72(R).

### EC6 -- Shore Tourism Sales [T1]

**Situation:** A retailer at the Jersey Shore asks about special seasonal tax rates.

**Resolution:** There is NO special tourism or shore district sales tax rate in New Jersey. The statewide 6.625% rate applies uniformly. Unlike some states with tourism surcharges, NJ has no additional tax for shore/tourist areas. Hotel occupancy taxes are separate (not part of sales tax).

### EC7 -- Motor Vehicle Sales [T1]

**Situation:** A NJ resident purchases a car from a NJ dealer for $30,000.

**Resolution:** Motor vehicle sales are subject to 6.625% sales tax, but the tax is collected by the **Motor Vehicle Commission (MVC)** at the time of title registration, not by the dealer. Tax = $1,987.50. N.J.S.A. 54:32B-3(a).

### EC8 -- Energy -- Residential vs. Commercial [T1]

**Situation:** A property owner receives a gas and electric bill.

**Resolution:** Residential gas and electric utility services are **EXEMPT** from sales tax. N.J.S.A. 54:32B-8.7a. Commercial/industrial gas and electric are **TAXABLE** at 6.625%. The property use classification determines taxability.

### EC9 -- Candy and Soft Drink Exemption [T1]

**Situation:** A convenience store sells candy bars and soft drinks.

**Resolution:** Both candy and soft drinks are EXEMPT in New Jersey when sold as grocery items (not as prepared food at a restaurant). N.J.S.A. 54:32B-8.2. This is different from many states (and SST states) that tax candy and soft drinks. NJ is notably consumer-friendly here.

### EC10 -- Digital Products Uniformity [T1]

**Situation:** A customer downloads a digital movie from an online retailer.

**Resolution:** TAXABLE at 6.625%. Digital products (music, movies, books, software) delivered electronically are taxable in NJ. N.J.S.A. 54:32B-2(oo). The same rate applies regardless of the customer's specific location in NJ (no local variation).

---

## Test Suite

### Test 1 -- Basic Taxable Sale [T1]

**Input:** Retailer sells a $500 TV in a NJ store.
**Expected output:** Sales tax = $33.13 ($500 x 6.625%). Total = $533.13.

### Test 2 -- Clothing Exemption [T1]

**Input:** Customer purchases a $300 winter coat in NJ.
**Expected output:** Sales tax = $0. Clothing is exempt in NJ regardless of price.

### Test 3 -- UEZ Sale (In-Person) [T1]

**Input:** UEZ-certified retailer in Camden sells a $1,000 refrigerator to a walk-in customer.
**Expected output:** Sales tax = $33.13 ($1,000 x 3.3125%). UEZ 50% reduced rate applies for in-person sales.

### Test 4 -- UEZ Online Sale (Not Qualifying) [T1]

**Input:** Same Camden UEZ retailer ships a $1,000 refrigerator to a NJ customer who ordered online.
**Expected output:** Sales tax = $66.25 ($1,000 x 6.625%). Full rate applies -- UEZ rate does not apply to remote sales.

### Test 5 -- Economic Nexus [T1]

**Input:** Out-of-state seller has $80,000 in NJ sales and 250 transactions in the current year.
**Expected output:** Seller HAS economic nexus (250 transactions exceeds 200 threshold -- OR test). Must register and collect NJ tax.

### Test 6 -- Grocery Food Including Candy [T1]

**Input:** Customer buys $100 of groceries: $70 general food, $15 candy bars, $15 soda. From a grocery store (not restaurant).
**Expected output:** Sales tax = $0. All items (including candy and soft drinks) are exempt in NJ when sold as grocery items.

### Test 7 -- SaaS Subscription [T1]

**Input:** NJ business subscribes to cloud-based project management tool. $200/month.
**Expected output:** Sales tax = $13.25/month ($200 x 6.625%). SaaS is taxable in NJ.

### Test 8 -- Paper Products [T1]

**Input:** Customer buys $50 of paper towels, toilet paper, and tissues.
**Expected output:** Sales tax = $0. Disposable paper products are exempt.

### Test 9 -- Resale Certificate [T1]

**Input:** Retailer purchases $20,000 inventory from NJ wholesaler. Provides valid ST-3 resale certificate.
**Expected output:** No sales tax charged. Retailer collects tax at resale.

### Test 10 -- Use Tax [T1]

**Input:** NJ business purchases $5,000 of taxable equipment from a Delaware retailer. No tax collected.
**Expected output:** Use tax = $331.25 ($5,000 x 6.625%). Report on ST-51 or NJ-1040.

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
