---
name: wi-sales-tax
description: Use this skill whenever asked about Wisconsin sales tax, Wisconsin use tax, Wisconsin sales tax nexus, Wisconsin sales tax returns, Wisconsin exemption certificates, taxability of goods or services in Wisconsin, or any request involving Wisconsin state-level consumption taxes. Trigger on phrases like "Wisconsin sales tax", "WI sales tax", "Wisconsin use tax", "Wisconsin nexus", "Wis. Stat. 77.51", "Wisconsin DOR sales tax", or any request involving Wisconsin sales and use tax filing, classification, or compliance. ALWAYS read the parent us-sales-tax skill first for federal context.
jurisdiction: US-WI
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# WI Sales Tax

## Skill Metadata

**Skill Metadata**

| Field | Value |
| --- | --- |
| Jurisdiction | Wisconsin, United States |
| Jurisdiction Code | US-WI |
| Tax Type | Sales and Use Tax |
| State Tax Rate | 5% |
| County Tax | 0.5% (all counties authorized; most levy it) |
| Maximum Combined Rate | 5.5% (5% state + 0.5% county) |
| Primary Legal Framework | Wisconsin Statutes (Wis. Stat.) Chapter 77, Subchapter III (Section 77.51 et seq.) |
| Governing Body | Wisconsin Department of Revenue (WDOR) |
| Filing Portal | My Tax Account -- https://tap.revenue.wi.gov |
| Economic Nexus Effective Date | October 1, 2018 |
| SST Member | Yes (full member) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Pending -- requires US CPA or Enrolled Agent sign-off |
| Validation Date | Pending |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate lookups, basic nexus, standard taxability. Tier 2: SaaS classification, service taxability, manufacturing exemptions. Tier 3: audit defense, penalty abatement, complex bundled transactions. |
| Format | Restructured to Q1 execution format, April 2026 |

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed CPA, EA, or tax attorney must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess. Escalate to a licensed tax professional.

## Step 0: Client Onboarding Questions

**Client Onboarding Questions**

| # | Question | Why It Matters |
| --- | --- | --- |
| 1 | Do you have a Wisconsin sales tax registration / tax ID? | Determines whether registration is needed before filing. |
| 2 | What is your current filing frequency (monthly / quarterly / annually)? | Controls which return periods to prepare. |
| 3 | What is your nexus type -- physical presence, economic nexus, or both? | Determines registration obligations and applicable rules. |
| 4 | Are you a marketplace seller (selling through Amazon, Etsy, etc.)? | Marketplace facilitator may already be collecting on your behalf. |
| 5 | What types of products or services do you sell in Wisconsin? | Drives taxability classification under Wisconsin law. |
| 6 | Do you sell to exempt entities (government, nonprofits, resellers)? | Determines whether exemption certificates must be collected and retained. |
| 7 | Do you have locations, employees, or inventory in Wisconsin? | Physical presence creates nexus independent of economic thresholds. |
| 8 | Do you sell into multiple Wisconsin local jurisdictions? | Local tax rates vary; determines compliance complexity. |

**If the client cannot answer questions 1-4, STOP and gather this information before proceeding.** [T1]

## Step 1: Tax Rate Structure

### 1.1 State Rate

- **State sales tax rate** — 5% percent (Moderate rate among US states.)  _(Wis. Stat. Section 77.52(1))_

### 1.2 County Tax

- **County sales tax** — 0.5% percent (All 72 counties authorized; most counties (68 of 72 as of current data) levy it. [T1])
- **No city/special district tax** — There are no city or special district sales taxes in Wisconsin. [T1]
- **Maximum combined rate** — 5.5% percent (5% state + 0.5% county. [T1])
- **Counties without the 0.5% tax** — A small number of counties do not levy the county option tax. Check WDOR's current county tax list. [T2]

### 1.3 Stadium Tax (Expired)

The former 0.1% Miller Park/American Family Field stadium tax in the five-county Milwaukee area expired. However, a new 0.5% local tax for the Brewers stadium was enacted; verify current status for Milwaukee-area counties. [T2]

### 1.4 Sourcing Rules [T1]

- **Sourcing method** — Wisconsin follows SST destination-based sourcing.
- **Shipped/delivered goods sourcing** — Destination (ship-to address). [T1]
- **Over-the-counter sourcing** — Seller's location. [T1]
- **Digital goods sourcing** — Buyer's address. [T1]

## Step 2: Transaction Classification Rules

### 2.1 General Rule

- **General taxability rule** — Wisconsin sales tax applies to the retail sale of tangible personal property, certain services, and certain digital goods.  _(Wis. Stat. Section 77.52)_

### 2.2 Taxability Matrix

**Taxability Matrix**

| Item Category | Taxable? | Rate | Authority | Tier |
| --- | --- | --- | --- | --- |
| General tangible personal property | Yes | Full rate | Wis. Stat. Section 77.52(1) | [T1] |
| Grocery food (food for home consumption) | **Exempt** | 0% | Wis. Stat. Section 77.54(20n) | [T1] |
| Prepared food (restaurant meals) | Yes | Full rate | Wis. Stat. Section 77.51(10m) | [T1] |
| Clothing and footwear | Yes | Full rate | No exemption | [T1] |
| Prescription drugs | Exempt | 0% | Wis. Stat. Section 77.54(14) | [T1] |
| Over-the-counter drugs | Exempt | 0% | Wis. Stat. Section 77.54(14m) | [T1] |
| Durable medical equipment | Exempt (with prescription) | 0% | Wis. Stat. Section 77.54(22) | [T1] |
| Motor vehicles | Yes | Full rate (5% + county 0.5%) | Wis. Stat. Section 77.52 | [T1] |
| Gasoline and motor fuel | Exempt from sales tax (motor fuel tax) | N/A | Wis. Stat. Section 77.54(11) | [T1] |
| Utilities (residential -- electricity, gas) | Exempt | 0% | Wis. Stat. Section 77.54(30) | [T1] |
| Utilities (commercial) | Yes | Full rate | Wis. Stat. Section 77.52 | [T1] |
| Manufacturing equipment (direct use) | Exempt | 0% | Wis. Stat. Section 77.54(6)(am) | [T2] |
| Agricultural supplies and equipment | Exempt | 0% | Wis. Stat. Section 77.54(3) | [T1] |
| Software -- canned (tangible medium) | Yes | Full rate | Wis. Stat. Section 77.52(1) | [T1] |
| Software -- canned (electronic delivery) | Yes | Full rate | WDOR guidance | [T1] |
| Software -- custom | Exempt | 0% | Wis. Stat. Section 77.52(1)(a) | [T2] |
| SaaS (Software as a Service) | **Not taxable** | 0% | WDOR -- not tangible personal property | [T2] |
| Digital goods (downloads) | Yes (specified digital goods) | Full rate | Wis. Stat. Section 77.52(1)(d) | [T1] |
| Data processing services | Not taxable | 0% | Not enumerated | [T2] |
| Newspapers (print) | Exempt | 0% | Wis. Stat. Section 77.54(15) | [T1] |

### 2.3 Grocery Food Exemption [T1]

- **Grocery food exemption scope** — Wisconsin fully exempts food and food ingredients for home consumption. Follows SST definition of food (Wisconsin is an SST member). [T1]  _(Wis. Stat. Section 77.54(20n))_
- **Candy taxable** — Candy is taxable (excluded from food under SST). [T1]  _(Wis. Stat. Section 77.54(20n))_
- **Soft drinks taxable** — Soft drinks are taxable (excluded from food under SST). [T1]  _(Wis. Stat. Section 77.54(20n))_
- **Dietary supplements taxable** — Dietary supplements are taxable. [T1]  _(Wis. Stat. Section 77.54(20n))_
- **Prepared food taxable** — Prepared food is taxable. [T1]  _(Wis. Stat. Section 77.54(20n))_

### 2.4 SaaS -- Not Taxable [T2]

- **SaaS not taxable determination** — WDOR has determined that SaaS is not the sale of tangible personal property or a taxable service. [T2]
- **Access vs. copy distinction** — The customer is accessing software on the vendor's server, not receiving a copy of software. [T2]
- **Canned software vs SaaS** — Canned software delivered electronically IS taxable, but SaaS is distinguished. [T2]
- **SaaS classification test** — The line between 'electronically delivered software' (taxable) and 'SaaS' (not taxable) requires analysis of whether the customer receives a transferable copy. [T2]

### 2.5 Services Taxability [T2]

**Services Taxability Matrix**

| Service | Taxable? | Authority |
| --- | --- | --- |
| Telecommunications | Yes | Wis. Stat. Section 77.52(2)(a)5 |
| Cable/satellite TV | Yes | Wis. Stat. Section 77.52(2)(a)5 |
| Repair and maintenance of TPP | Parts: Yes; Labor: Not separately taxable if repair is not itemized | Wis. Stat. Section 77.52(2)(a)10 |
| Hotel/lodging | Yes (plus local room taxes) | Wis. Stat. Section 77.52(2)(a)1 |
| Laundry/dry cleaning | Yes | Wis. Stat. Section 77.52(2)(a)3 |
| Parking (commercial) | Yes | Wis. Stat. Section 77.52(2)(a)4 |
| Admissions/entertainment | Yes | Wis. Stat. Section 77.52(2)(a)2 |
| Photography | Yes | Wis. Stat. Section 77.52(2)(a)7 |
| Landscaping/lawn care | Yes | Wis. Stat. Section 77.52(2)(a)10 |
| Professional services (legal, accounting) | No | Not enumerated |
| Personal services (haircuts, spa) | No | Not enumerated |
| Construction/real property | No (materials taxable at purchase) | WDOR guidance |
| Transportation/freight | Exempt (if separately stated) | Wis. Stat. Section 77.52(18) |

## Step 3: Return Form Structure

### 3.1 Registration

- **Seller's Permit registration** — All sellers with nexus must register with WDOR for a Seller's Permit. Registration through My Tax Account portal.  _(Wis. Stat. Section 77.52(7))_
- **Registration fee** — $20 USD (One-time fee. [T1])  _(Wis. Stat. Section 77.52(7))_

### 3.2 Filing Frequency

**Filing Frequency**

| Annual Tax Liability | Filing Frequency | Due Date |
| --- | --- | --- |
| Over $3,600 per year | Monthly | Last day of the following month |
| $1,200 -- $3,600 per year | Quarterly | Last day of month following quarter-end |
| Under $1,200 per year | Annual | January 31 |

### 3.3 Returns and Payment

- **Form ST-12** — Form ST-12 (Wisconsin Sales and Use Tax Return) is the primary return. [T1]
- **Electronic filing requirement** — Electronic filing through My Tax Account is required. [T1]
- **Payment due date** — Payment due on the same date as the return. [T1]
- **County tax reporting** — County taxes are reported on the same return. [T1]

### 3.4 Vendor Discount

- **Retailer's discount rate** — 0.5% of the tax due (both state and county), up to a maximum of $1,000 per reporting period. [T1] percent  _(Wis. Stat. Section 77.61(4)(a))_
- **Discount availability condition** — Available only for timely filing and payment. [T1]  _(Wis. Stat. Section 77.61(4)(a))_

### 3.5 Penalties and Interest

**Penalties and Interest**

| Violation | Penalty | Authority |
| --- | --- | --- |
| Late filing | $20 or 5% of tax due, whichever is greater (per month, up to 25%) | Wis. Stat. Section 77.60(1) |
| Late payment | 1% per month, up to 24% | Wis. Stat. Section 77.60(2) |
| Failure to file | Estimated assessment + penalties | Wis. Stat. Section 77.59(2) |
| Fraud | 100% of deficiency | Wis. Stat. Section 77.60(9) |
| Interest | 12% per year (adjusted) | Wis. Stat. Section 77.60(1) |

## Step 4: Deductibility / Exemptions

### 5.1 Wisconsin Exemption Certificates

**Wisconsin Exemption Certificates**

| Certificate | Use Case | Authority |
| --- | --- | --- |
| **Form S-211** (Wisconsin Sales and Use Tax Exemption Certificate) | General exemption (resale, manufacturing, agricultural, government, nonprofit) | WDOR |
| **Form S-211E** (Electronic version) | Same as S-211, electronic format | WDOR |
| **SSTCE** (Streamlined certificate) | Multi-state purchases (Wisconsin is SST member) | SST Agreement |

### 5.2 Requirements [T1]

- **Valid certificate requirements** — Valid certificates must include: purchaser information, seller's permit number (for resale), reason for exemption, description of goods, signature, date. [T1]

### 5.3 Good Faith and Retention [T1]

- **Certificate retention period** — Good faith acceptance protects sellers. Certificates must be retained for 4 years from the date of the last transaction. [T1] years

### 6.1 When Use Tax Applies

- **Use tax applicability** — Wisconsin use tax applies when sales tax was not collected on items used, stored, or consumed in Wisconsin. [T1]

### 6.2 Use Tax Rate

- **Use tax rate** — 5.5% (5% state + 0.5% county (if applicable), maximum [T1])

### 6.3 Use Tax Reporting

- **Business reporting** — Businesses: Report on Form ST-12. [T1]
- **Individual reporting** — Individuals: Report on Wisconsin income tax return (Form 1), Line 14. [T1]

## Step 5: Key Thresholds

### 4.1 Physical Nexus

- **Physical nexus standard** — Standard physical nexus principles apply. [T1]

### 4.2 Economic Nexus [T1]

- **Economic nexus enactment date** — October 1, 2018

**Economic Nexus Thresholds**  _(Wis. Stat. Section 77.53(9m))_

| Threshold | Value | Measurement Period |
| --- | --- | --- |
| Revenue | **$100,000** in gross sales into Wisconsin | Current or prior calendar year |
| Transactions | N/A (revenue only) |  |
| Test | Revenue only -- no transaction count test |  |

- **No transaction count alternative** — Wisconsin uses a revenue-only threshold. There is no transaction-count alternative. [T1]  _(Wis. Stat. Section 77.53(9m))_

### 4.3 Marketplace Facilitator Rules [T1]

- **Marketplace facilitator effective date** — Effective January 1, 2020.  _(Wis. Stat. Section 77.52(1m))_
- **Facilitator collection obligation** — Marketplace facilitators meeting the nexus threshold must collect and remit. [T1]  _(Wis. Stat. Section 77.52(1m))_
- **Marketplace seller relief** — Marketplace sellers relieved for facilitated sales. [T1]  _(Wis. Stat. Section 77.52(1m))_

## Step 6: Filing Deadlines and Penalties

Refer to Step 3 for filing frequencies and due dates. [T1]

## PROHIBITIONS

- **1** — NEVER advise that Wisconsin has city or special district sales taxes (only state and county). [T1]
- **2** — NEVER advise that SaaS is taxable in Wisconsin (it is not). [T1]
- **3** — NEVER advise that grocery food is taxable in Wisconsin (it is exempt). [T1]
- **4** — NEVER advise that clothing is exempt in Wisconsin (it is taxable -- no clothing exemption). [T1]
- **5** — NEVER calculate a combined rate exceeding 5.5% (5% state + 0.5% county max). [T1]
- **6** — NEVER use a transaction-count threshold for Wisconsin economic nexus (revenue only, $100K). [T1]
- **7** — NEVER forget that landscaping services are taxable in Wisconsin. [T1]
- **8** — NEVER advise that Wisconsin is not an SST member (it is a full member). [T1]
- **9** — NEVER assume all counties levy the 0.5% tax without verifying. [T2]
- **10** — NEVER ignore the $20 seller's permit fee when advising on registration. [T1]

## Edge Case Registry

### 7.1 Manufacturing Exemption [T2]

- **Manufacturing exemption standard** — Machinery and equipment used exclusively and directly in manufacturing are exempt. [T2]  _(Wis. Stat. Section 77.54(6)(am))_
- **Manufacturing definition** — "Manufacturing" includes processing, fabricating, and assembling. [T1]  _(Wis. Stat. Section 77.54(6)(am))_
- **Exclusively and directly standard** — The "exclusively and directly" standard is stricter than some states' "predominantly" test. [T2]  _(Wis. Stat. Section 77.54(6)(am))_
- **Dual-use equipment** — Dual-use equipment (manufacturing + non-manufacturing) may not qualify. [T2]  _(Wis. Stat. Section 77.54(6)(am))_

### 7.2 Landscaping and Lawn Care [T1]

- **Landscaping taxable services** — Lawn mowing, snow removal, tree trimming: taxable. [T1]
- **Landscape design not taxable** — Landscape design (intellectual services): generally not taxable. [T2]
- **Landscaping materials taxable** — Materials incorporated into landscaping: taxable. [T1]

### 7.3 Construction Contractors [T2]

- **Contractor materials tax** — Contractors pay tax on materials at purchase. [T1]
- **No sales tax collection on real property** — Contractors do NOT collect sales tax on real property improvements. [T1]
- **Time and materials vs lump sum** — Time and materials vs. lump sum contracts may be treated differently for certain items. [T2]

### 7.4 Trade-In Credits [T1]

- **Trade-in credit reduces base** — Trade-in of like-kind property reduces the taxable base. [T1]  _(Wis. Stat. Section 77.51(15b)(a))_
- **Trade-in applicability** — Applies to motor vehicles, boats, aircraft, and other TPP. [T1]  _(Wis. Stat. Section 77.51(15b)(a))_

### 7.5 Coin-Operated Amusement and Vending [T1]

- **Vending machine food sales** — Coin-operated vending machine sales of food are taxable. [T1]
- **Coin-operated amusement devices** — Coin-operated amusement devices: the operator pays use tax on the purchase; individual transactions by customers are not separately taxed. [T2]

### 7.6 Motor Vehicles and Boats [T1]

- **Motor vehicle tax and rate** — Motor vehicles: taxable at 5% + county 0.5%. Tax paid at DMV registration. [T1]
- **Boats and watercraft tax** — Boats and personal watercraft: same rate, paid at registration with DNR. [T1]
- **Trade-in credits for vehicles** — Trade-in credits reduce the taxable base. [T1]
- **Casual sales between individuals** — Casual sales between individuals: use tax applies. [T1]

### 7.7 Temporary Events and Craft Fairs [T1]

- **Temporary event seller's permit requirement** — Sellers at temporary events (craft fairs, festivals) must have a seller's permit. [T1]
- **Out-of-state sellers at events** — Out-of-state sellers making sales at Wisconsin events establish physical nexus. [T1]
- **Temporary seller's permit availability** — A temporary seller's permit is available for sellers at single events. [T1]

## Test Suite

### Test 1: Basic Rate Calculation [T1]

**Question:** A retailer in Dane County (0.5% county tax) sells a $500 computer. What is the total sales tax?

**Expected Answer:** $500 x (5% + 0.5%) = $500 x 5.5% = $27.50.

### Test 2: Grocery Food Exemption [T1]

**Question:** A grocery store sells $200 in produce and dairy, $10 in candy, and $8 in soft drinks. What tax is due?

**Expected Answer:** Produce/dairy: exempt ($0). Candy: $10 x 5.5% = $0.55. Soft drinks: $8 x 5.5% = $0.44. Total: $0.99.

### Test 3: SaaS Taxability [T2]

**Question:** A Wisconsin business subscribes to a $1,500/month SaaS HR platform. Is Wisconsin sales tax due?

**Expected Answer:** No. SaaS is not taxable in Wisconsin as it is not tangible personal property.

### Test 4: Clothing [T1]

**Question:** A customer buys a $300 jacket in Milwaukee. Is it taxable?

**Expected Answer:** Yes. Wisconsin does NOT exempt clothing. Tax = $300 x 5.5% = $16.50.

### Test 5: Economic Nexus [T1]

**Question:** An out-of-state seller made $80,000 in sales and 500 transactions in Wisconsin. Does the seller have nexus?

**Expected Answer:** No. Wisconsin uses a revenue-only threshold of $100,000. Transaction count is irrelevant.

### Test 6: Manufacturing Exemption [T2]

**Question:** A factory buys a $100,000 milling machine used exclusively in production. Is it exempt?

**Expected Answer:** Yes, if used exclusively and directly in manufacturing. Must provide Form S-211 claiming the manufacturing exemption.

### Test 7: Landscaping Services [T1]

**Question:** A homeowner pays a landscaping company $500 for lawn mowing and $200 for tree trimming in Wisconsin. What tax is due?

**Expected Answer:** Both services are taxable. Total: $700 x 5.5% = $38.50.

## Reviewer Escalation Protocol

**Reviewer Escalation Protocol**

| Trigger | Action |
| --- | --- |
| Any [T3] tagged item encountered | STOP. Do not guess. Escalate to licensed CPA, EA, or tax attorney. |
| Client has audit notice or assessment | Escalate immediately. Do not advise on audit response. |
| Multi-state nexus question involving 3+ states | Flag for senior reviewer with multi-state experience. |
| Penalty abatement or voluntary disclosure | Escalate to licensed professional with state-specific experience. |
| Ambiguous taxability of a product/service | Present both interpretations to reviewer with supporting authority. |

## Contribution Notes

- This skill follows the Q1 execution format (Step 0 through Step 7).
- All rules are tagged [T1], [T2], or [T3] per the Confidence Tier Definitions.
- Rate tables are deterministic lookup tables -- no narrative explanation of rates.
- To update this skill, submit a pull request with the specific section, supporting statutory authority, and effective date of the change.
- All changes require validation by a US CPA or EA before merging.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
