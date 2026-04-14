---
name: new-york-sales-tax
description: Use this skill whenever asked about New York sales and use tax, NYS DTF filings, NYC sales tax, New York exemptions, New York clothing exemption, New York nexus, or any request involving New York state sales and use tax compliance. Trigger on phrases like "New York sales tax", "NY sales tax", "NYC sales tax", "DTF", "ST-100", "New York clothing exemption", "New York resale certificate", or any request involving New York sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any New York sales tax work.
version: 2.0
---

# New York Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | New York, United States |
| Jurisdiction code | US-NY |
| Tax type | Sales and Use Tax (state + local) |
| State rate | 4.00% |
| Local rate range | 3.00% -- 4.875% |
| MCTD surcharge | 0.375% (Metropolitan Commuter Transportation District) |
| Maximum combined rate | 8.875% (New York City) |
| Sourcing | Destination-based |
| Economic nexus | $500,000 revenue AND 100 transactions (AND test -- both must be met) |
| Nexus test type | AND test -- unique among states; most use OR |
| Measurement period | Prior four sales tax quarterly periods (NOT calendar year) |
| Primary legislation | New York Tax Law, Articles 28 and 29 |
| Tax authority | New York State Department of Taxation and Finance (NYS DTF) |
| Filing portal | https://www.tax.ny.gov |
| SST member | No |
| Return form | ST-100 (quarterly); ST-810 (monthly); ST-809 (part-quarterly) |
| Quarterly periods | March-May, June-August, September-November, December-February (NOT calendar quarters) |
| Quarterly deadline | 20th of month following quarter end |
| Vendor discount | Up to 5% of first $1,200,000 collected per quarter; max $200/quarter |
| Federal framework skill | us-sales-tax |
| Skill version | 2.0 |

**CRITICAL: New York sales tax quarters do NOT align with calendar quarters. They start March 1.**

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

| # | Question | Why it matters |
|---|----------|----------------|
| 1 | Certificate of Authority number? | Required for filing; confirms NYS DTF registration |
| 2 | Assigned filing frequency (quarterly, monthly/part-quarterly, annual, PrompTax)? | Determines due dates and payment schedules |
| 3 | Nexus type (physical, economic, both)? | NY requires BOTH $500K AND 100 transactions |
| 4 | Sell through marketplace facilitators? | Marketplace facilitators collect on facilitated sales |
| 5 | Make sales in MCTD (NYC, Rockland, Westchester, Dutchess, Orange, Putnam, Nassau, Suffolk)? | 0.375% MCTD surcharge; separate schedule ST-100.3 |
| 6 | Sell clothing or footwear? | Items under $110/item exempt from state and NYC tax |
| 7 | Annual sales tax liability over $500,000? | PrompTax (accelerated EFT) may be required |
| 8 | Sell software, SaaS, or digital products? | SaaS taxable in NY as pre-written software |

### Refusal catalogue

**R-NY-1 -- Film production credit purchases.** Empire State Film Production tax exemptions require qualifying certificates from Empire State Development. Escalate to reviewer.

**R-NY-2 -- Real property capital improvement vs. repair.** The distinction between exempt capital improvements and taxable repairs requires professional judgment. Escalate to reviewer.

---

## Section 3 -- Transaction pattern library

### 3.1 Tangible personal property

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP (electronics, appliances, furniture, equipment) | TAXABLE | Tax Law Section 1105(a) |

### 3.2 Clothing and footwear -- KEY EXEMPTION

| Pattern | Taxable? | Notes |
|---|---|---|
| Clothing/footwear under $110 per item | EXEMPT | State and NYC local tax exempt; per-ITEM threshold, NOT per transaction |
| Clothing/footwear $110 or more per item | TAXABLE | Full combined rate applies |
| Costume accessories (cuff links, tiara) | TAXABLE | Not qualifying clothing |
| Sport/recreational equipment (ski boots, cleats) | TAXABLE | Not qualifying clothing |
| Protective equipment (hard hats, safety goggles) | TAXABLE | Not qualifying clothing |

**The clothing exemption is PERMANENT and year-round. New York does NOT have a temporary sales tax holiday.**

**Non-NYC counties:** Some counties do NOT exempt clothing from local tax. Verify county-specific rules for non-NYC locations.

### 3.3 Food and beverages

| Pattern | Taxable? | Citation |
|---|---|---|
| Grocery food (unprepared, for home consumption) | EXEMPT | Tax Law Section 1115(a)(1) |
| Prepared food (heated, served on-premises) | TAXABLE | Tax Law Section 1105(d) |
| Candy and confections | TAXABLE | Tax Law Section 1115(a)(1) exception |
| Carbonated beverages / soft drinks | TAXABLE | Tax Law Section 1115(a)(1) exception |
| Bottled water (non-carbonated) | EXEMPT | |
| Dietary supplements | EXEMPT | |
| Alcoholic beverages | TAXABLE | |
| ALL food/drink sold by restaurants | TAXABLE | Restaurant context overrides grocery exemption |

**Restaurant rule:** ALL food and drink sold by restaurants becomes TAXABLE, including otherwise exempt items like bottled water. Tax Law Section 1105(d).

### 3.4 SaaS and digital goods

| Pattern | Taxable? | Notes |
|---|---|---|
| Canned software (any delivery method) | TAXABLE | Tax Law Section 1101(b)(6) |
| Custom software (any delivery) | EXEMPT | Not TPP |
| SaaS (cloud-hosted, no download) | TAXABLE | Pre-written software accessed remotely; TSB-A-13(22)S |
| Digital music, movies, books (download) | TAXABLE | TPP equivalents |
| Streaming services | TAXABLE | Information service or entertainment |

**New York clearly taxes SaaS as a sale of pre-written computer software.**

### 3.5 Services

| Pattern | Taxable? | Citation |
|---|---|---|
| Information services | TAXABLE | Tax Law Section 1105(c)(1) |
| Processing and printing | TAXABLE | Tax Law Section 1105(c)(2) |
| Installation, maintenance, repair of TPP | TAXABLE | Tax Law Section 1105(c)(3) |
| Storage | TAXABLE | Tax Law Section 1105(c)(4) |
| Interior decorating/design | TAXABLE | Tax Law Section 1105(c)(5) |
| Protective/detective services | TAXABLE | Tax Law Section 1105(c)(6) |
| Trash removal (commercial) | TAXABLE | Tax Law Section 1105(c)(7) |
| Credit rating/reporting | TAXABLE | Tax Law Section 1105(c)(8) |
| Telephone/telegraph services | TAXABLE | Tax Law Section 1105(b)(1) |
| Professional services (legal, accounting, medical, consulting) | NOT TAXABLE | Not enumerated |
| Advertising | NOT TAXABLE | |
| Education | NOT TAXABLE | |
| Janitorial / personal care | NOT TAXABLE | |

### 3.6 Manufacturing and exemptions

| Pattern | Taxable? | Citation |
|---|---|---|
| Manufacturing equipment (directly and predominantly 50%+ in production) | EXEMPT | Tax Law Section 1115(a)(12) |
| Fuel/utilities for manufacturing | EXEMPT | Tax Law Section 1115(c) |
| Farm equipment | EXEMPT | Tax Law Section 1115(a)(6) |
| Resale (valid ST-120) | EXEMPT | Tax Law Section 1101(b)(4) |
| Interstate commerce (shipped out of state) | EXEMPT | Tax Law Section 1115(a)(8) |
| Federal government sales | EXEMPT | Tax Law Section 1116(a)(1) |
| Prescription drugs | EXEMPT | Tax Law Section 1115(a)(3) |
| OTC drugs | TAXABLE | No OTC exemption in NY |
| Newspapers and periodicals | EXEMPT | Tax Law Section 1115(a)(5) |

---

## Section 4 -- Rate lookup

### 4.1 Key combined rates

| Jurisdiction | Combined rate | Breakdown |
|---|---|---|
| New York City (5 boroughs) | 8.875% | 4% state + 4.5% city + 0.375% MCTD |
| Westchester County | 8.375% | 4% + 4% + 0.375% MCTD |
| Nassau County | 8.625% | 4% + 4.25% + 0.375% MCTD |
| Suffolk County | 8.625% | 4% + 4.25% + 0.375% MCTD |
| Albany County | 8.00% | 4% + 4% |
| Erie County (Buffalo) | 8.00% | 4% + 4% |

### 4.2 MCTD counties

NYC, Rockland, Westchester, Dutchess, Orange, Putnam, Nassau, Suffolk -- 0.375% surcharge applies in all.

### 4.3 Sourcing

| Scenario | Rate applied |
|---|---|
| Shipped goods | Delivery address rate |
| Customer pickup | Seller's location rate |
| Remote sellers | Destination-based |

---

## Section 5 -- Classification rules

### 5.1 General rule

New York taxes: (a) retail sales of TPP, (b) enumerated services, (c) restaurant food/drink, (d) hotel occupancy, (e) admissions. Tax Law Section 1105.

### 5.2 Clothing per-item threshold

The $110 exemption is per ITEM, not per transaction. A $109 shirt and a $115 jacket in the same transaction: shirt is exempt, jacket is taxable.

### 5.3 Restaurant override

All food at restaurants is taxable regardless of individual item exemption status. A bottle of water at a grocery store is exempt; the same bottle at a restaurant is taxable.

---

## Section 6 -- Return form and filing

### 6.1 Forms

| Form | Use |
|---|---|
| ST-100 | Quarterly return |
| ST-100.3 | MCTD schedule |
| ST-100.7 | Sub-jurisdiction detail |
| ST-810 | Monthly return (large filers) |
| ST-809 | Part-quarterly monthly payment |
| ST-120 | Resale certificate |
| ST-119/ST-119.1 | Exempt organization certificates |
| ST-124 | Capital improvement certificate |

### 6.2 Filing deadlines (NON-CALENDAR QUARTERS)

| Quarter | Period | Due date |
|---|---|---|
| Q1 | March 1 -- May 31 | June 20 |
| Q2 | June 1 -- August 31 | September 20 |
| Q3 | September 1 -- November 30 | December 20 |
| Q4 | December 1 -- February 28/29 | March 20 |

### 6.3 PrompTax

| Parameter | Value |
|---|---|
| Threshold | Annual liability > $500,000 |
| Method | EFT within 3 business days of each PrompTax period |
| Returns | Still filed quarterly |

---

## Section 7 -- Thresholds, penalties, and deadlines

### 7.1 Economic nexus

| Parameter | Value |
|---|---|
| Revenue threshold | $500,000 gross receipts from TPP delivered in NY |
| Transaction threshold | 100 transactions delivering TPP in NY |
| Test type | AND -- BOTH must be met |
| Measurement period | Prior four sales tax quarterly periods |
| Marketplace exclusion | Marketplace sales do not count |
| Authority | Tax Law Section 1101(b)(8)(iv) |

### 7.2 Marketplace facilitator

| Rule | Detail |
|---|---|
| Effective date | June 1, 2019 |
| Facilitator treated as | Vendor for tax purposes |
| Authority | Tax Law Section 1101(b)(8)(vi) |

### 7.3 Penalties

| Penalty | Rate | Citation |
|---|---|---|
| Late filing | 10% of tax due (max) | Tax Law Section 1145(a)(1) |
| Late payment | 10% of tax due (max) | Tax Law Section 1145(a)(1) |
| Fraud | 50% of deficiency | Tax Law Section 1145(a)(2) |
| Interest | Set quarterly by DTF | Tax Law Section 1142 |

### 7.4 Record retention

| Parameter | Value |
|---|---|
| Period | 3 years from due date or filing date (whichever later) |
| Statute of limitations (standard) | 3 years |
| No return filed | No limitation |
| Fraud | No limitation |
| 25%+ understatement | 6 years |

---

## Section 8 -- Edge cases

### EC1 -- Clothing at $110 boundary

**Situation:** Customer buys $109 shirt and $115 jacket.
**Resolution:** Shirt ($109) is EXEMPT. Jacket ($115) is TAXABLE at full rate. Per-item, not per-transaction.

### EC2 -- SaaS taxability

**Situation:** Business subscribes to cloud-based CRM (no download).
**Resolution:** TAXABLE. NY treats SaaS as pre-written software. TSB-A-13(22)S.

### EC3 -- Restaurant bottled water

**Situation:** Customer orders bottled water at a restaurant.
**Resolution:** TAXABLE. Restaurant context overrides the grocery food exemption.

### EC4 -- Economic nexus AND test

**Situation:** Out-of-state seller: $600K revenue, 80 transactions.
**Resolution:** No nexus. Revenue exceeds $500K but transactions (80) do not exceed 100. NY requires BOTH.

### EC5 -- Non-NYC county clothing

**Situation:** Vendor in Saratoga County asks about clothing exemption on local tax.
**Resolution:** State exemption (under $110) applies statewide. Some counties may not exempt local tax. Verify county-specific rules.

### EC6 -- Capital improvement vs. repair

**Situation:** Contractor performs work on a building.
**Resolution:** Capital improvements (Form ST-124) are EXEMPT. Repairs are TAXABLE under Section 1105(c)(3). Requires professional judgment.

---

## Section 9 -- Test suite

### Test 1 -- Clothing under $110 in NYC

**Input:** $95 shoes in Manhattan. NYC rate: 8.875%.
**Expected:** Tax = $0. Clothing under $110 exempt.

### Test 2 -- Clothing over $110 in NYC

**Input:** $200 jacket in Manhattan.
**Expected:** Tax = $17.75. Full rate applies.

### Test 3 -- Grocery food exempt

**Input:** $100 groceries (bread, milk, produce) from a supermarket.
**Expected:** Tax = $0.

### Test 4 -- SaaS subscription in NYC

**Input:** $100/month SaaS tool. NYC rate 8.875%.
**Expected:** Tax = $8.88. SaaS is taxable.

### Test 5 -- Economic nexus AND test (not met)

**Input:** $600K revenue, 80 transactions.
**Expected:** NO nexus. Both thresholds not met.

### Test 6 -- Economic nexus AND test (met)

**Input:** $600K revenue, 150 transactions.
**Expected:** HAS nexus. Both exceeded.

### Test 7 -- Restaurant meal in NYC

**Input:** $50 dinner at NYC restaurant.
**Expected:** Tax = $4.44. All restaurant food taxable.

### Test 8 -- Manufacturing equipment in Buffalo

**Input:** $200K machine for production. Erie County rate: 8%.
**Expected:** Tax = $0. Manufacturing exemption.

### Test 9 -- Use tax on out-of-state purchase

**Input:** NYC business buys $5,000 furniture from NH retailer. No tax collected.
**Expected:** Use tax = $443.75.

### Test 10 -- Resale certificate

**Input:** Retailer purchases $10K inventory. Valid ST-120 provided.
**Expected:** No tax. Retailer collects at resale.

---

## Section 10 -- Prohibitions

- NEVER apply the $110 clothing exemption per transaction -- it is per ITEM.
- NEVER use calendar quarters for New York sales tax -- NY quarters start March 1.
- NEVER accept SST certificates in New York -- NY is not an SST member.
- NEVER assume economic nexus with only the revenue threshold -- NY requires BOTH $500K AND 100 transactions.
- NEVER treat SaaS as nontaxable in New York.
- NEVER treat restaurant food as exempt -- all food/drink at restaurants is taxable.
- NEVER assume the clothing exemption applies to local tax in all counties.
- NEVER confuse capital improvements (exempt) with repairs (taxable).
- NEVER assume OTC medicine is exempt in New York.
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude.

---

## Disclaimer

This skill is provided for informational and computational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional (CPA, EA, or tax attorney) before filing.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
