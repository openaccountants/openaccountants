---
name: maryland-sales-tax
description: Use this skill whenever asked about Maryland sales tax, Maryland use tax, Maryland sales tax nexus, Maryland sales tax returns, Maryland exemption certificates, taxability of goods or services in Maryland, Maryland digital advertising tax, or any request involving Maryland state-level consumption taxes. Trigger on phrases like "Maryland sales tax", "MD sales tax", "Maryland use tax", "Maryland nexus", "Md. Code Tax-Gen 11", "Maryland Comptroller sales tax", "digital advertising tax", or any request involving Maryland sales and use tax filing, classification, or compliance. ALWAYS read the parent us-sales-tax skill first for federal context, then layer this Maryland-specific skill on top.
---

# Maryland Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Maryland, United States |
| Jurisdiction Code | US-MD |
| Tax Type | Sales and Use Tax |
| State Tax Rate | 6% (flat -- no local sales tax) |
| Maximum Combined Rate | 6% (no local component) |
| Primary Legal Framework | Maryland Code, Tax-General Article, Title 11 (Section 11-101 et seq.) |
| Governing Body | Comptroller of Maryland |
| Filing Portal | Comptroller Online Services -- https://www.marylandtaxes.gov |
| Economic Nexus Effective Date | October 1, 2018 |
| SST Member | No |
| Unique Feature | Digital Advertising Tax (first-in-nation) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate lookups, basic nexus, standard taxability. Tier 2: digital goods/SaaS classification, clothing exemption nuances, digital advertising tax. Tier 3: audit defense, digital ad tax litigation, penalty abatement. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Maryland sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Maryland sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Maryland? | Drives taxability classification under Maryland law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Maryland? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Maryland local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Rate

Maryland imposes a **flat 6% state sales and use tax**. There are **no local sales taxes** in Maryland.

**This makes Maryland straightforward for rate determination.** If the transaction is taxable and delivered to/within Maryland, the rate is always 6%. [T1]

**Statutory authority:** Md. Code Tax-Gen Section 11-104(a).

### 1.2 No Local Taxes

Maryland does **not** permit local jurisdictions to levy sales taxes. The 6% rate is uniform statewide. [T1]

### 1.3 Alcoholic Beverages Rate

Alcoholic beverages are taxed at **9%** rather than the standard 6%. [T1]

**Authority:** Md. Code Tax-Gen Section 11-104(b).

### 1.4 Sourcing Rules [T1]

Maryland is a **destination-based** sourcing state:

- **Shipped/delivered goods:** Destination (ship-to address). [T1]
- **Over-the-counter:** Seller's location. [T1]
- **Digital goods:** Buyer's address. [T1]

---

## Step 2: Transaction Classification Rules
### 2.1 General Rule

Maryland sales tax applies to the retail sale of tangible personal property and certain enumerated services and digital products. Md. Code Tax-Gen Section 11-102.

### 2.2 Taxability Matrix

| Item Category | Taxable? | Rate | Authority | Tier |
|---------------|----------|------|-----------|------|
| General tangible personal property | Yes | 6% | Md. Code Tax-Gen Section 11-102 | [T1] |
| Grocery food (food for home consumption) | **Exempt** | 0% | Md. Code Tax-Gen Section 11-206(a) | [T1] |
| Prepared food (restaurant meals) | Yes | 6% | Md. Code Tax-Gen Section 11-102 | [T1] |
| Clothing and footwear | **Exempt** | 0% | Md. Code Tax-Gen Section 11-211 | [T1] |
| Prescription drugs | Exempt | 0% | Md. Code Tax-Gen Section 11-211 | [T1] |
| Over-the-counter drugs | Exempt | 0% | Md. Code Tax-Gen Section 11-211 | [T1] |
| Durable medical equipment | Exempt | 0% | Md. Code Tax-Gen Section 11-211 | [T1] |
| Motor vehicles | Yes | 6% (excise tax, collected by MVA) | Md. Code Trans. Section 13-809 | [T1] |
| Gasoline and motor fuel | Exempt from sales tax (motor fuel excise tax) | N/A | Md. Code Tax-Gen Section 11-206 | [T1] |
| Utilities (residential) | Exempt | 0% | Md. Code Tax-Gen Section 11-209 | [T1] |
| Utilities (commercial) | Yes | 6% | Md. Code Tax-Gen Section 11-102 | [T1] |
| Manufacturing equipment | Exempt (qualifying manufacturers) | 0% | Md. Code Tax-Gen Section 11-210 | [T2] |
| Agricultural equipment and supplies | Exempt | 0% | Md. Code Tax-Gen Section 11-211(a)(2) | [T1] |
| Software -- canned (tangible medium) | Yes | 6% | Md. Code Tax-Gen Section 11-101(k) | [T1] |
| Software -- canned (electronic delivery) | Yes | 6% | Comptroller guidance | [T2] |
| Software -- custom | Exempt | 0% | Comptroller guidance | [T2] |
| SaaS (Software as a Service) | **Taxable** | 6% | Md. Code Tax-Gen Section 11-101(m-1); effective March 14, 2021 | [T2] |
| Digital goods/products | **Taxable** | 6% | Md. Code Tax-Gen Section 11-101(d-2); effective March 14, 2021 | [T1] |
| Digital codes | Yes | 6% | Md. Code Tax-Gen Section 11-101(d-1) | [T1] |
| Alcoholic beverages | Yes | **9%** | Md. Code Tax-Gen Section 11-104(b) | [T1] |
| Newspapers | Exempt | 0% | Md. Code Tax-Gen Section 11-206(b) | [T1] |

### 2.3 Clothing Exemption [T1]

Maryland exempts **clothing and footwear** from sales tax:

- The exemption applies to all clothing and footwear regardless of price. [T1]
- There is **no price cap** (unlike some states that exempt clothing only up to a certain amount). [T1]
- **Accessories** (jewelry, handbags, cosmetics) are NOT clothing and remain taxable. [T1]
- **Protective equipment** (safety shoes, hard hats) is exempt as clothing. [T1]
- **Costumes** are taxable (not considered "clothing" for everyday wear). [T2]
- **Fur clothing** is exempt (no luxury surcharge in Maryland). [T1]

**Authority:** Md. Code Tax-Gen Section 11-211(a)(1).

### 2.4 Digital Goods and SaaS -- 2021 Changes [T2]

Effective **March 14, 2021**, Maryland expanded its sales tax to include:

- **Digital products:** Any product obtained electronically, including digital audio, video, books, games, and other digital content. [T1]
- **Digital codes:** Codes that allow a purchaser to obtain a digital product. [T1]
- **SaaS:** Access to software on a remote server, including subscription-based access. [T2]

**Authority:** Md. Code Tax-Gen Section 11-101(d-2), (m-1); HB 932 (2020).

### 2.5 Digital Advertising Tax -- Unique to Maryland [T2]

Maryland enacted the **nation's first digital advertising tax** in 2021 (HB 732):

- Applies to annual gross revenues derived from digital advertising services in Maryland. [T2]
- **Graduated rates** based on the company's global annual gross revenue:
  - $100M -- $1B: **2.5%**
  - $1B -- $5B: **5%**
  - $5B -- $10B: **7.5%**
  - Over $15B: **10%**
- Only applies to companies with **$1 million or more** in digital advertising revenue in Maryland. [T2]
- Applies to display ads, search ads, banner ads, and similar digital advertising. [T2]
- **This tax has faced significant legal challenges** and its enforceability and constitutionality are subject to ongoing litigation. [T3]

**CAUTION:** The digital advertising tax is separate from the sales tax and is reported on a different return. Due to ongoing litigation, always verify the current status before advising. [T3]

**Authority:** Md. Code Tax-Gen Section 7.5-101 et seq.

### 2.6 Services Taxability [T2]

Maryland taxes certain enumerated services:

| Service | Taxable? | Authority |
|---------|----------|-----------|
| Telecommunications | Yes | Md. Code Tax-Gen Section 11-101(k) |
| Cable/satellite TV | Yes | Md. Code Tax-Gen Section 11-101(k) |
| Security monitoring | Yes | Md. Code Tax-Gen Section 11-101(k) |
| Cleaning/janitorial | Yes (commercial only) | Comptroller guidance |
| Fabrication/manufacturing labor | Yes (when creating TPP) | Md. Code Tax-Gen Section 11-101(k) |
| Professional services (legal, accounting) | No | Not enumerated |
| Personal services (haircuts, spa) | No | Not enumerated |
| Construction/real property | No (materials taxable at purchase) | Comptroller guidance |
| Transportation/freight | Exempt (if separately stated) | Md. Code Tax-Gen Section 11-101(k) |

---

## Step 3: Return Form Structure
### 3.1 Registration

All sellers with nexus must register with the Comptroller for a sales and use tax license. Registration is completed online.

**Authority:** Md. Code Tax-Gen Section 11-402.

### 3.2 Filing Frequency

| Monthly Tax Liability | Filing Frequency | Due Date |
|-----------------------|------------------|----------|
| Over $500 per month | Monthly | 20th of the following month |
| $100 -- $500 per month | Quarterly | 20th of month following quarter-end |
| $50 -- $100 per month | Semi-annual | 20th of month after period-end |
| Under $50 per month | Annual | January 20 |

### 3.3 Returns and Payment

- **Form 202** (Maryland Sales and Use Tax Return) is the primary return. [T1]
- Electronic filing through the Comptroller's website is available. [T1]
- Payment is due on the same date as the return. [T1]

### 3.4 Vendor Discount

Maryland provides a **vendor discount** for timely filing:

- **1.2%** of tax collected (not to exceed $500 per reporting period). [T1]
- Available only for timely filing and payment. [T1]

**Authority:** Md. Code Tax-Gen Section 11-105.

### 3.5 Penalties and Interest

| Violation | Penalty | Authority |
|-----------|---------|-----------|
| Late filing | 10% of tax due, minimum $1 | Md. Code Tax-Gen Section 13-701 |
| Late payment | Same as late filing | Md. Code Tax-Gen Section 13-701 |
| Failure to file | Estimated assessment + penalties | Md. Code Tax-Gen Section 13-701 |
| Fraud | 25% of deficiency | Md. Code Tax-Gen Section 13-702 |
| Interest | Statutory rate (~10%) | Md. Code Tax-Gen Section 13-601 |

---

## Step 4: Deductibility / Exemptions
### 5.1 Maryland Exemption Certificates

| Certificate | Use Case | Authority |
|-------------|----------|-----------|
| **Form ST-205** (Maryland Resale Certificate) | Purchases for resale | Comptroller |
| **Form ST-206** (Exempt Organizations Certificate) | Nonprofit/government purchases | Comptroller |
| **Form ST-215** (Certificate of Exemption -- Government) | Government entity purchases | Comptroller |
| **SSTCE** (Streamlined certificate) | Multi-state (accepted even though MD is not SST) | Comptroller policy |

### 5.2 Requirements [T1]

Valid certificates must include purchaser information, Maryland registration number (for resale), reason for exemption, description of goods, signature, and date. [T1]

### 5.3 Good Faith and Retention [T2]

Good faith acceptance protects sellers. Certificates must be retained for **4 years** from the date of the last transaction. [T1]

---


### 6.1 When Use Tax Applies

Maryland use tax applies when sales tax was not collected on items used in Maryland. [T1]

### 6.2 Use Tax Rate

6%, identical to the sales tax rate. 9% for alcoholic beverages. [T1]

### 6.3 Use Tax Reporting

- **Businesses:** Report on Form 202. [T1]
- **Individuals:** Report on Maryland income tax return (Form 502), Line 30. [T1]

---

## Step 5: Key Thresholds
### 4.1 Physical Nexus

Standard physical nexus principles apply. [T1]

### 4.2 Economic Nexus [T1]

Maryland enacted economic nexus effective **October 1, 2018**.

| Threshold | Value | Measurement Period |
|-----------|-------|--------------------|
| Revenue | **$100,000** in gross sales into Maryland | Previous or current calendar year |
| Transactions | **200 transactions** into Maryland | Previous or current calendar year |
| Test | **OR** -- either threshold triggers nexus | |

**Authority:** Md. Code Tax-Gen Section 11-101(c-5).

### 4.3 Marketplace Facilitator Rules [T1]

Effective **October 1, 2019**:

- Marketplace facilitators meeting the nexus threshold must collect and remit. [T1]
- Marketplace sellers relieved for facilitated sales. [T1]

**Authority:** Md. Code Tax-Gen Section 11-101(c-6).

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
1. **NEVER** advise that Maryland has local sales taxes (it does not -- 6% flat statewide). [T1]
2. **NEVER** advise that clothing is taxable in Maryland (clothing and footwear are exempt). [T1]
3. **NEVER** advise that grocery food is taxable in Maryland (it is exempt). [T1]
4. **NEVER** advise that SaaS is not taxable in Maryland (it became taxable effective March 14, 2021). [T1]
5. **NEVER** provide definitive guidance on the digital advertising tax without noting ongoing litigation. [T3]
6. **NEVER** apply the 6% rate to alcoholic beverages (the rate is 9%). [T1]
7. **NEVER** confuse the clothing exemption with accessories -- jewelry, handbags, and cosmetics are taxable. [T1]
8. **NEVER** advise that Maryland is an SST member state (it is not). [T1]
9. **NEVER** calculate a rate other than 6% (or 9% for alcohol) for Maryland -- there is no local variation. [T1]
10. **NEVER** ignore the digital advertising tax as a potential obligation for large tech companies operating in Maryland. [T2]

---

## Edge Case Registry

### 7.1 Clothing vs. Accessories Distinction [T2]

The clothing exemption requires careful classification:

- **Exempt:** Shirts, pants, dresses, coats, shoes, boots, gloves, hats (everyday wear), underwear, socks. [T1]
- **Taxable:** Jewelry, watches, handbags, wallets, cosmetics, wigs, hair accessories. [T1]
- **Gray area:** Athletic wear (exempt if wearable as everyday clothing), costumes, uniforms. [T2]

### 7.2 Digital Advertising Tax Litigation [T3]

The Maryland digital advertising tax is subject to active litigation:

- Constitutional challenges based on the Internet Tax Freedom Act (ITFA), Commerce Clause, and First Amendment. [T3]
- A Maryland circuit court struck down the tax, but appeals are ongoing. [T3]
- **Do not provide definitive guidance on digital advertising tax obligations without current legal analysis.** [T3]

### 7.3 Vending Machine Sales [T1]

Vending machine sales of food are taxable at 6%. The vendor, not the machine's host location, is responsible for collecting and remitting. [T1]

### 7.4 Trade Shows and Conventions [T2]

Vendors making sales at Maryland trade shows may trigger physical nexus:

- A single trade show can establish nexus in Maryland. [T2]
- Out-of-state vendors at trade shows must collect Maryland sales tax on sales made at the event. [T1]
- Some exemptions may apply for occasional sellers. [T2]

### 7.5 Nonprofit Organizations [T2]

- Qualifying 501(c)(3) nonprofits may apply for an exemption from sales tax on purchases. [T2]
- The exemption is **not automatic** -- organizations must apply to the Comptroller and receive a certificate. [T1]
- Exempt organizations are still required to collect and remit sales tax on their own taxable sales unless specifically exempt from collection. [T2]

### 7.6 Computer Services and Data Processing [T2]

Maryland's taxation of digital goods and SaaS creates questions about related services:

- **Data processing services** are generally not subject to sales tax. [T2]
- **Cloud storage** may be taxable if classified as a digital product. [T2]
- **Web hosting** taxability depends on the specific service provided. [T3]
- The line between SaaS (taxable) and data processing (not taxable) requires careful analysis. [T3]

### 7.7 Short-Term Rentals [T1]

Short-term rentals (Airbnb, VRBO) are subject to:

- 6% state sales tax on the rental charge. [T1]
- Additional local hotel/lodging taxes (collected by the county, not the Comptroller). [T2]
- Marketplace facilitators collect the state portion. [T1]

---

## Test Suite

### Test 1: Basic Rate Calculation [T1]

**Question:** A retailer in Baltimore sells a $500 kitchen appliance. What is the sales tax?

**Expected Answer:** $500 x 6% = $30.00. There are no local sales taxes in Maryland.

### Test 2: Clothing Exemption [T1]

**Question:** A customer buys a $300 winter coat and a $50 handbag in Maryland. What tax is due?

**Expected Answer:** Coat: exempt (clothing). Handbag: taxable (accessory). Tax = $50 x 6% = $3.00.

### Test 3: Grocery Food Exemption [T1]

**Question:** A consumer buys $200 of groceries and a $15 bottle of wine in Maryland. What tax is due?

**Expected Answer:** Groceries: exempt. Wine (alcoholic beverage): $15 x 9% = $1.35. Total tax: $1.35.

### Test 4: SaaS Taxability [T2]

**Question:** A Maryland business subscribes to a $1,000/month cloud-based accounting platform (SaaS). Is Maryland sales tax due?

**Expected Answer:** Yes. SaaS became taxable in Maryland effective March 14, 2021. Tax = $1,000 x 6% = $60/month.

### Test 5: Economic Nexus [T1]

**Question:** An out-of-state seller made $75,000 in sales and 250 transactions in Maryland. Does the seller have nexus?

**Expected Answer:** Yes. The 200-transaction threshold was exceeded (OR test).

### Test 6: Digital Advertising Tax [T3]

**Question:** A tech company with $12 billion in global revenue earns $5 million in digital advertising revenue from Maryland. What is the digital advertising tax?

**Expected Answer:** This question should be escalated to a licensed tax professional due to ongoing litigation challenging the constitutionality of Maryland's digital advertising tax. If enforceable, the rate would be 7.5% (for companies with $5B-$10B global revenue) on the $5M MD-sourced ad revenue = $375,000. But enforceability is uncertain.

### Test 7: Vendor Discount [T1]

**Question:** A monthly filer remits $5,000 in Maryland sales tax on time. What vendor discount applies?

**Expected Answer:** 1.2% of $5,000 = $60. Since this is under the $500 cap, the full $60 discount applies. Remittance: $5,000 - $60 = $4,940.

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
