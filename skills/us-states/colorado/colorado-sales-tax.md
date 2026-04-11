---
name: colorado-sales-tax
description: Use this skill whenever asked about Colorado sales tax, Colorado use tax, Colorado sales tax nexus, Colorado sales tax returns, Colorado exemption certificates, taxability of goods or services in Colorado, home-rule cities, retail delivery fee, or any request involving Colorado state-level consumption taxes. Trigger on phrases like "Colorado sales tax", "CO sales tax", "Colorado use tax", "Colorado nexus", "Colorado home rule", "C.R.S. 39-26", "retail delivery fee", "Colorado DOR sales tax", or any request involving Colorado sales and use tax filing, classification, or compliance. ALWAYS read the parent us-sales-tax skill first for federal context, then layer this Colorado-specific skill on top. IMPORTANT: Colorado is one of the MOST COMPLEX sales tax states in the US due to home-rule cities.
---

# Colorado Sales and Use Tax Skill

---

## Skill Metadata
| Field | Value |
|-------|-------|
| Jurisdiction | Colorado, United States |
| Jurisdiction Code | US-CO |
| Tax Type | Sales and Use Tax |
| State Tax Rate | 2.9% |
| Maximum Combined Rate | Approximately 11.2% (varies by locality) |
| Primary Legal Framework | Colorado Revised Statutes (C.R.S.) Title 39, Article 26 |
| Governing Body | Colorado Department of Revenue (CDOR) |
| Filing Portal | Revenue Online -- https://www.colorado.gov/revenueonline |
| Economic Nexus Effective Date | June 1, 2019 (state); varies for home-rule cities |
| SST Member | Yes (associate member) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: state rate lookups, basic nexus. Tier 2: home-rule city rules, local tax administration, retail delivery fee, destination sourcing. Tier 3: audit defense with multiple jurisdictions, home-rule city disputes, complex multi-jurisdiction analysis. |
| Format | Restructured to Q1 execution format, April 2026 |

---

## Confidence Tier Definitions
Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

---

## Step 0: Client Onboarding Questions

Before proceeding with any Colorado sales tax analysis, collect the following from the client: [T1]

| # | Question | Why It Matters |
|---|----------|---------------|
| 1 | Do you have a Colorado sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Colorado? | Drives taxability classification under Colorado law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Colorado? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Colorado local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

---

## Step 1: Tax Rate Structure
### 1.1 State Rate

Colorado's state sales tax rate is **2.9%** -- one of the lowest state rates in the country.

**Statutory authority:** C.R.S. Section 39-26-106.

### 1.2 Local Tax Layers -- The Complexity Problem [T2]

Colorado has one of the **most complex local sales tax structures** in the United States. Multiple layers of local tax can apply to a single transaction:

| Tax Layer | Typical Range | Authority |
|-----------|---------------|-----------|
| State tax | 2.9% | C.R.S. Section 39-26-106 |
| County tax | 0% -- 2.0% | County ordinances |
| City tax | 0% -- 5.0% | City ordinances |
| Special district tax (RTD, FD, etc.) | 0% -- 2.5% | District enabling legislation |
| **Combined total** | **2.9% -- ~11.2%** | |

**Critical distinction -- State-administered vs. Self-collected (Home-Rule) cities:**

Colorado has two types of local jurisdictions:

| Type | Description | Examples | How to file |
|------|-------------|----------|-------------|
| **State-administered** | Local tax collected and remitted through the state return | Most counties, some cities | Filed with CDOR on the state return |
| **Home-rule cities** | City self-administers its own sales tax; separate registration, filing, and rules | Denver, Colorado Springs, Aurora, Boulder, Fort Collins, Lakewood, Pueblo, and ~70 others | Filed directly with the city |

### 1.3 Home-Rule Cities -- Critical Warning [T2]

**Home-rule cities** are the single most important complexity factor in Colorado sales tax:

- **Approximately 70+ cities** in Colorado are self-collecting home-rule jurisdictions. [T2]
- Each home-rule city has its **own tax code**, its **own exemptions**, its **own definitions**, and its **own filing requirements**. [T2]
- A seller may need to register with the state AND separately with each home-rule city where it has nexus. [T2]
- Some home-rule cities have **different exemptions** than the state (e.g., a city may tax items that the state exempts, or vice versa). [T2]
- Home-rule cities may have **different economic nexus thresholds** than the state. [T3]
- The **Sales and Use Tax System (SUTS)** portal allows filing with some (but not all) home-rule cities through a single platform. [T2]

**Major home-rule cities (partial list):**

| City | City Tax Rate | Administers Own Tax? |
|------|---------------|---------------------|
| Denver | 4.81% | Yes |
| Colorado Springs | 3.07% | Yes |
| Aurora | 3.75% | Yes |
| Fort Collins | 3.85% | Yes |
| Boulder | 3.86% | Yes |
| Lakewood | 3.0% | Yes |
| Pueblo | 4.0% | Yes |
| Thornton | 3.75% | Yes |
| Arvada | 3.46% | Yes |
| Westminster | 3.85% | Yes |

### 1.4 Retail Delivery Fee [T1]

Effective July 1, 2022, Colorado imposes a **Retail Delivery Fee** on all deliveries by motor vehicle to a location in Colorado that include at least one item subject to state sales or use tax:

- Fee amount: **$0.29** per delivery (adjusted for inflation). [T1]
- The fee is charged per delivery, not per item. [T1]
- Must be shown as a separate line item on the receipt/invoice. [T1]
- The seller is responsible for collecting and remitting the fee. [T1]
- Reported on the retailer's sales tax return (DR 0100). [T1]

**Authority:** C.R.S. Section 43-4-218(3)(a).

### 1.5 Sourcing Rules [T1/T2]

Colorado uses **destination-based sourcing** for state tax purposes:

- **Shipped goods:** Destination (ship-to address). [T1]
- **Over-the-counter:** Seller's location. [T1]
- **Home-rule cities:** Each city has its own sourcing rules, but most follow destination-based sourcing. **Verify with each home-rule city.** [T2]

---

## Step 2: Transaction Classification Rules
### 2.1 General Rule

Colorado sales tax applies to the retail sale of tangible personal property and certain services. C.R.S. Section 39-26-104.

### 2.2 Taxability Matrix -- State Level

| Item Category | Taxable? | Rate | Authority | Tier |
|---------------|----------|------|-----------|------|
| General tangible personal property | Yes | Full rate | C.R.S. Section 39-26-104 | [T1] |
| Grocery food (food for home consumption) | **Exempt from state tax** | 0% state (local may still tax) | C.R.S. Section 39-26-707(1)(e) | [T1] |
| Prepared food (restaurant meals) | Yes | Full rate | C.R.S. Section 39-26-104 | [T1] |
| Clothing and footwear | Yes | Full rate | No exemption | [T1] |
| Prescription drugs | Exempt | 0% | C.R.S. Section 39-26-717(1) | [T1] |
| Over-the-counter drugs | Exempt | 0% | C.R.S. Section 39-26-717(2)(c) | [T1] |
| Durable medical equipment | Exempt (prosthetics and certain DME) | 0% | C.R.S. Section 39-26-717(2) | [T1] |
| Motor vehicles | Yes | Full rate | C.R.S. Section 39-26-104 | [T1] |
| Gasoline and motor fuel | Exempt from sales tax (motor fuel excise tax applies) | N/A | C.R.S. Section 39-26-715(1)(a)(III) | [T1] |
| Utilities (residential gas and electricity) | Exempt (residential) | 0% | C.R.S. Section 39-26-715(1)(a)(II) | [T1] |
| Utilities (commercial) | Yes | Full rate | C.R.S. Section 39-26-104 | [T1] |
| Agricultural equipment and supplies | Exempt | 0% | C.R.S. Section 39-26-716(2) | [T1] |
| Software -- canned (tangible medium) | Yes | Full rate | C.R.S. Section 39-26-104 | [T1] |
| Software -- canned (electronic delivery) | Yes | Full rate | CDOR FYI Sales 60 | [T2] |
| Software -- custom | Exempt | 0% | CDOR guidance | [T2] |
| SaaS (Software as a Service) | **Generally not taxable at state level** | 0% state | CDOR guidance; but home-rule cities may differ | [T2] |
| Digital goods | Not taxable at state level | 0% state | Not defined as TPP | [T2] |
| Packaging materials | Exempt (used to package products for sale) | 0% | C.R.S. Section 39-26-706(2) | [T1] |

### 2.3 Grocery Food -- State vs. Local Divergence [T1]

This is a critical distinction:

- **State level:** Grocery food is **exempt** from the 2.9% state sales tax. [T1]
- **Local level:** Many local jurisdictions (counties, cities, special districts) **still tax grocery food**. [T2]
- Some home-rule cities have adopted their own grocery food exemptions, while others continue to tax food. [T2]
- **Effective January 1, 2023**, many state-administered localities stopped taxing grocery food, but home-rule cities make their own decisions. [T2]

**Practical impact:** A customer may pay 0% state tax on groceries but still owe local taxes totaling several percent depending on location. Always check the specific locality. [T2]

### 2.4 Services Taxability [T2]

Colorado taxes very few services at the state level:

| Service | Taxable? | Authority |
|---------|----------|-----------|
| Telecommunications | Yes | C.R.S. Section 39-26-104 |
| Cable/satellite TV | Yes | C.R.S. Section 39-26-104 |
| Electricity (commercial) | Yes | C.R.S. Section 39-26-104 |
| Professional services | No | Not enumerated |
| Personal services | No | Not enumerated |
| Repair of TPP | Parts: Yes; Labor: No (if separately stated) | CDOR FYI Sales 7 |
| Construction | No (materials taxable at purchase) | CDOR guidance |

**CAUTION:** Home-rule cities may tax services that the state does not. Always check the specific city code. [T3]

---

## Step 3: Return Form Structure
### 3.1 Registration

- **State:** Register with CDOR through Revenue Online. [T1]
- **Home-rule cities:** Register separately with each home-rule city where you have nexus. Some cities participate in the **SUTS (Sales and Use Tax System)** portal for centralized filing. [T2]

**Authority:** C.R.S. Section 39-26-103.

### 3.2 Filing Frequency

| Tax Liability (annual) | Filing Frequency | Due Date |
|------------------------|------------------|----------|
| $0 -- $300 | Annual | January 20 |
| $301 -- $3,600 | Quarterly | 20th of month following quarter-end |
| Over $3,600 | Monthly | 20th of the following month |

**Note:** Home-rule cities have their own filing frequency requirements. [T2]

### 3.3 Returns and Payment

- **Form DR 0100** (Colorado Retail Sales Tax Return) is the primary state return. [T1]
- The return includes state-administered local taxes. [T1]
- Home-rule city taxes are filed separately with each city or through SUTS. [T2]
- Electronic filing is required for most filers. [T1]
- The **Retail Delivery Fee** is reported on the DR 0100. [T1]

### 3.4 Vendor Discount

Colorado allows a **vendor's fee** for timely filing:

- **3.33%** of the state sales tax collected, up to **$1,000** per filing period (for monthly filers). [T1]
- Only available for timely filers. [T1]

**Authority:** C.R.S. Section 39-26-105(1)(a).

### 3.5 Penalties and Interest

| Violation | Penalty | Authority |
|-----------|---------|-----------|
| Late filing | 10% of tax due, plus 0.5% per month (up to 18%) | C.R.S. Section 39-26-118 |
| Late payment | Same as late filing | C.R.S. Section 39-26-118 |
| Failure to file | Estimated assessment + penalties | C.R.S. Section 39-26-118 |
| Fraud | 50% to 100% of deficiency | C.R.S. Section 39-26-118 |
| Interest | Statutory rate (currently ~6%) | C.R.S. Section 39-21-110.5 |

---

## Step 4: Deductibility / Exemptions
### 5.1 Colorado Exemption Certificates

| Certificate | Use Case | Authority |
|-------------|----------|-----------|
| **Form DR 0563** (Sales Tax Exemption Certificate -- Multi-Jurisdiction) | General exemption (resale, exempt organizations) | CDOR |
| **Form DR 0137** (Claim for Refund) | Refund of overpaid tax | CDOR |
| **SSTCE** (Streamlined certificate) | Multi-state purchases | SST Agreement |

### 5.2 Home-Rule City Certificates [T2]

Many home-rule cities have **their own exemption certificate forms**:

- A state exemption certificate may NOT be accepted by a home-rule city. [T2]
- Sellers must obtain the city-specific certificate for home-rule city exemptions. [T2]
- Some cities participate in SUTS and accept the SUTS exemption certificate. [T2]

### 5.3 Requirements and Retention [T1]

Standard requirements apply: name, address, registration number, reason for exemption, signature, date. Certificates must be retained for **3 years**. [T1]

---


### 6.1 When Use Tax Applies

Colorado use tax applies when sales tax was not collected on property used, stored, or consumed in Colorado. [T1]

### 6.2 Use Tax Rate

State use tax rate: 2.9%. Local use tax may also apply. [T1]

### 6.3 Use Tax Reporting

- **Businesses:** Report on the DR 0100 or separately on Form DR 0252. [T1]
- **Individuals:** Report on Colorado income tax return (Form DR 0104). [T1]

---

## Step 5: Key Thresholds
### 4.1 Physical Nexus

Standard physical nexus principles apply at the state level. [T1]

### 4.2 Economic Nexus [T1]

Colorado enacted economic nexus effective **June 1, 2019**.

| Threshold | Value | Measurement Period |
|-----------|-------|--------------------|
| Revenue | **$100,000** in gross sales into Colorado | Previous or current calendar year |
| Transactions | N/A (revenue only) | |
| Test | Revenue only -- no transaction count test | |

**Authority:** C.R.S. Section 39-26-102(3).

### 4.3 Home-Rule City Economic Nexus [T2]

Each home-rule city can set its own economic nexus threshold:

- Many home-rule cities have adopted **$100,000** in city-specific sales as their threshold. [T2]
- Some cities have adopted **$500** or other low thresholds. [T3]
- **Always check the specific home-rule city's threshold.** [T2]
- HB 19-1240 established that remote sellers meeting the state threshold must also collect for state-administered localities, but home-rule cities retain control over their own nexus rules. [T2]

### 4.4 Marketplace Facilitator Rules [T1]

Colorado enacted marketplace facilitator rules effective **October 1, 2019**:

- Marketplace facilitators must collect and remit state sales tax. [T1]
- For state-administered localities, marketplace facilitators also collect local tax. [T1]
- Home-rule cities may have their own marketplace facilitator rules. [T2]

**Authority:** C.R.S. Section 39-26-102(3.5).

---

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

---

## PROHIBITIONS
1. **NEVER** provide a combined rate for a Colorado address without identifying ALL applicable jurisdictions (state, county, city, special district). [T1]
2. **NEVER** assume a home-rule city follows the state's exemptions or definitions (each has its own rules). [T2]
3. **NEVER** tell a seller they only need to register with the state -- if they sell into home-rule cities, they likely need separate city registrations. [T2]
4. **NEVER** advise that grocery food is fully exempt in Colorado without specifying this applies to state tax only; local taxes may still apply. [T1]
5. **NEVER** forget the Retail Delivery Fee ($0.29) on qualifying deliveries. [T1]
6. **NEVER** assume SaaS is taxable in Colorado at the state level (it generally is not). [T2]
7. **NEVER** assume SaaS is NOT taxable in a Colorado home-rule city without verifying that city's specific rules. [T3]
8. **NEVER** use a transaction-count threshold for Colorado state economic nexus (Colorado uses revenue only, $100,000). [T1]
9. **NEVER** file a single return and assume all Colorado obligations are met -- home-rule cities require separate filings. [T2]
10. **NEVER** underestimate the complexity of Colorado sales tax -- it is widely considered the most complex sales tax state in the US. [T1]

---

## Edge Case Registry

### 7.1 Multi-Jurisdiction Delivery [T2]

A single delivery in Colorado may involve:

- State tax (2.9%)
- County tax
- City tax (state-administered or home-rule)
- Special district tax (RTD, Scientific & Cultural Facilities District, etc.)

The seller must determine ALL applicable jurisdictions based on the delivery address. Rate lookup tools are essential. [T2]

### 7.2 Home-Rule City Audit Risk [T3]

Home-rule cities can (and do) audit sellers independently of the state:

- A seller may face audit by the state AND by multiple home-rule cities simultaneously. [T3]
- Each home-rule city has its own audit process, protest procedures, and penalties. [T3]
- Denver, Colorado Springs, and Aurora are among the most active auditors. [T3]

### 7.3 Construction and Building Materials [T2]

Colorado construction tax rules are complex:

- Contractors generally pay sales tax on materials at purchase. [T1]
- Some jurisdictions allow contractors to purchase materials tax-free and remit use tax based on the delivery location. [T2]
- Denver has its own construction use tax rate (4% for contractor use). [T2]
- The "use tax on building materials" rule varies by home-rule city. [T3]

### 7.4 Marijuana/Cannabis [T2]

Colorado imposes additional taxes on recreational marijuana/cannabis:

- **State excise tax:** 15% on wholesale. [T1]
- **State retail marijuana sales tax:** 15% (in addition to standard 2.9% sales tax). [T1]
- **Local taxes** also apply (many cities impose additional marijuana sales taxes). [T2]
- Medical marijuana is subject to standard sales tax but exempt from the special retail marijuana tax. [T2]

**Authority:** C.R.S. Section 39-28.8-302.

### 7.5 Retail Delivery Fee Complexities [T1]

- The fee applies to ALL deliveries that include at least one taxable item, even if most items are exempt. [T1]
- Only one fee per delivery, regardless of the number of taxable items. [T1]
- The fee applies even to deliveries made by third-party carriers (FedEx, UPS, USPS). [T1]
- Small retailers with less than $500,000 in annual sales were temporarily exempt but this exemption has expired. [T2]

### 7.6 SaaS at the Local Level [T3]

While the state does not tax SaaS, some home-rule cities may tax it under their own definitions:

- Denver has been known to take expansive positions on the taxability of digital products. [T3]
- Boulder and Fort Collins have their own guidance on digital/SaaS taxability. [T3]
- This is a rapidly evolving area and requires city-by-city analysis. [T3]

### 7.7 Vendor-Issued Credits and Returns [T1]

- Refunds on returned merchandise: seller may claim a credit on the next return. [T1]
- The refund must be properly documented with the original transaction details. [T1]
- Home-rule city refund procedures may differ. [T2]

---

## Test Suite

### Test 1: Basic State Rate [T1]

**Question:** What is the Colorado state sales tax rate on a $500 purchase of clothing?

**Expected Answer:** $500 x 2.9% = $14.50 in state tax. Additional local taxes would apply depending on the delivery location.

### Test 2: Grocery Food [T1]

**Question:** A customer buys $200 in groceries in Denver. What state sales tax applies?

**Expected Answer:** $0 state sales tax. Grocery food is exempt from the 2.9% state tax. However, Denver city tax and other local taxes may still apply to groceries (check Denver's current rules).

### Test 3: Home-Rule City [T2]

**Question:** A remote seller has $150,000 in sales into Colorado, including $60,000 specifically to Denver customers. What registrations are needed?

**Expected Answer:** The seller must register with CDOR (state economic nexus at $100K is met). The seller must ALSO check whether Denver's home-rule city nexus threshold is met (Denver has its own threshold) and if so, register separately with Denver.

### Test 4: Retail Delivery Fee [T1]

**Question:** An online retailer ships 3 separate orders to Colorado customers in a day. Each order contains taxable items. How much in Retail Delivery Fees is owed?

**Expected Answer:** 3 x $0.29 = $0.87. The fee is per delivery, not per item.

### Test 5: Economic Nexus [T1]

**Question:** A seller made $90,000 in sales and 500 transactions in Colorado. Does the seller have state economic nexus?

**Expected Answer:** No. Colorado's state economic nexus threshold is $100,000 in revenue only. There is no transaction-count test at the state level.

### Test 6: Multi-Jurisdiction Rate [T2]

**Question:** A retailer in Denver sells a $1,000 laptop with delivery in Denver. What is the approximate total tax?

**Expected Answer:** State 2.9% + Denver city 4.81% + other applicable local = approximately 8.81% or higher depending on special district overlays. Approximately $88.10+ in tax. The exact rate requires a precise address lookup.

### Test 7: SaaS [T2]

**Question:** A Colorado business subscribes to a $300/month SaaS CRM platform. Is state sales tax due?

**Expected Answer:** No state sales tax is due on SaaS in Colorado. However, if the business is located in a home-rule city (e.g., Denver, Boulder), the city may independently tax SaaS -- check the specific city's rules.

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
