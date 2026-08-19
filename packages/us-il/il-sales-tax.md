---
name: il-sales-tax
description: "Illinois Sales Tax return (Form ST-1) for self-employed individuals. Covers all four Illinois occupation and use taxes (ROT, UT, SOT, SUT), state and local rates, origin-based sourcing, vendor discount, and filing frequencies. Primary source: 35 ILCS 120/ (ROT), 35 ILCS 105/ (UT), 35 ILCS 115/ (SOT), 35 ILCS 110/ (SUT)."
version: 1.0
jurisdiction: US-IL
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Amir Pelinkovic
review_status: current
depends_on:
  - us-tax-workflow-base
category: state
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# IL Sales Tax

## Illinois Sales Tax (Form ST-1) v1.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **a licensed accountant** on 2026-06-03.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### IL Sales Tax

- **ROT rate — general merchandise** — 6.25% state (general merchandise)  _(35 ILCS 120/2-10; IDOR PIO-101.)_
- **ROT rate — qualifying food/drugs/medical** — 1.0% state rate for qualifying food/drugs/medical in 2025; the statewide 1% grocery tax is eliminated effective 1/1/2026 (localities may re-impose).  _(35 ILCS 120/2-10; IDOR PIO-115; PA 103-0781.)_
- **SOT rate — general** — 6.25%  _(35 ILCS 110/3-10.)_
- **SOT rate — general** — 6.25%  _(35 ILCS 110/3-10.)_
- **SOT rate — general** — 6.25%  _(35 ILCS 110/3-10.)_
- **SOT tax base** — General SOT base = selling price of TPP transferred (if separately stated) or 50% of the entire bill if not separately stated; never less than cost. 'Cost price' applies only to de minimis servicepersons (cost-of-TPP < 35%, or < 75% pharmacy/graphic arts).  _(86 Ill. Admin. Code 140.106; IDOR Pub-113.)_
- **Chicago — general** — 10.25% combined (state 6.25 + county/RTA/city)  _(IDOR MyTax IL Rate Finder.)_
- **Springfield — general** — Springfield combined rate is ~9.75% (6.25 state + 1.00 county + 2.50 city/home-rule); 8.75% is outdated. Confirm exact rate via MyTax IL Rate Finder.  _(IDOR MyTax IL Tax Rate Finder.)_
- **Champaign — general** — Component math supports 9.00% (6.25 + 1.25 county + 1.50 city); some third-party sources show 9.25% after recent local changes. Confirm via MyTax IL Rate Finder.  _(IDOR MyTax IL Rate Finder.)_
- **Monthly tier** — Monthly filers (avg > $200/mo tax) file ST-1 by the 20th of the following month  _(86 Ill. Admin. Code 130.502; ST-1 instr.)_
- **Quarterly tier** — Quarterly if avg <= $200/mo; due the 20th after quarter end  _(ST-1 instr.)_
- **Annual tier** — Annual if avg < $50/mo; due January 20  _(ST-1 instr.)_
- **Vendor discount rate** — 1.75% of tax timely remitted (min $5/yr); capped at $1,000/month effective 1/1/2025  _(35 ILCS 120/3; PA 103-0592; ST-1 instr.)_
- **Applies to** — The discount is computed on TOTAL ST-1 tax due (Line 9, which includes locally imposed ROT), not the state portion only. ST-1 Step 4 applies 1.75% to Line 9, subject to the $1,000/month cap.  _(ST-1 instr. (R-01/26), Step 4; 35 ILCS 120/3.)_
- **Late filing** — Discount forfeited if the return is filed or tax paid late  _(35 ILCS 120/3; IDOR guidance.)_
- **Sourcing** — IL sourcing is hybrid, not purely origin-based. In-state retailers shipping from IL inventory use origin; remote retailers and marketplace facilitators meeting $100,000/200-transaction nexus source to destination; effective 1/1/2026 IL expands destination-based ROT for in-state sellers shipping from out of state.  _(IDOR Pub-113; FY 2026-12; Leveling the Playing Field Act.)_
- **Qualifying food** — Qualifying food excludes prepared food, candy, soft drinks, and alcohol (general rate)  _(86 Ill. Admin. Code 130.310; IDOR PIO-115.)_
- **E-filing** — IL generally mandates electronic ST-1 filing for most retailers (waiver via Form IL-900-EW). The $200 figure is the monthly-vs-quarterly filing-frequency threshold, not an e-file trigger.  _(ST-1 instr.; 86 Ill. Admin. Code 130.)_

## What this file is

**Obligation category:** CT (Consumption Tax)
**Functional role:** Return preparation
**Status:** Complete

This is a Tier 2 content skill for preparing the Illinois Form ST-1 (Sales and Use Tax and E911 Surcharge Return). Illinois has a unique four-tax structure for sales/use taxes, and this skill covers all four taxes as they appear on the combined ST-1 return.

## Section 1 -- Scope statement

**In scope:**

- Form ST-1 (Sales and Use Tax and E911 Surcharge Return)
- All four Illinois occupation/use taxes:
  - Retailers' Occupation Tax (ROT) -- on sellers of tangible personal property
  - Use Tax (UT) -- on out-of-state purchases by Illinois consumers
  - Service Occupation Tax (SOT) -- on servicepersons transferring tangible personal property incident to a service
  - Service Use Tax (SUT) -- on consumers of property transferred incident to a service
- State and local rate components
- Vendor discount (1.75%)
- Filing frequency determination

**Out of scope (refused):**

- Automobile Renting Occupation and Use Tax
- Hotel Operators' Occupation Tax
- Telecommunications taxes
- Cannabis taxes
- Chicago Home Rule Municipal Soft Drink Tax and other Chicago-specific levies
- Marketplace facilitator obligations
- Multi-state nexus determinations

## Section 2 -- Filing requirements

### Who must register

- **Registration requirement** — Any person engaged in the business of selling tangible personal property at retail in Illinois must register with the Illinois Department of Revenue (IDOR) and collect and remit ROT. Servicepersons who transfer tangible personal property incident to a service must also register.  _(35 ILCS 120/2.)_

### Filing frequency

**Filing frequency**  _(86 Ill. Admin. Code 130.601)_

| Monthly tax liability | Filing frequency | Source |
| --- | --- | --- |
| $200 or more/month (average) | Monthly (due 20th of following month) | 86 Ill. Admin. Code 130.601 |
| Less than $200/month (average) | Quarterly (due 20th after quarter end) | 86 Ill. Admin. Code 130.601 |
| Less than $50/month (average) | Annual (due January 20) | 86 Ill. Admin. Code 130.601 |

- **Electronic filing** — Required for all taxpayers whose average monthly liability is $200 or more.  _(35 ILCS 120/3.)_

## Section 3 -- Rates and thresholds

### The four-tax structure

**The four-tax structure**  _(35 ILCS 120/2; 35 ILCS 105/3; 35 ILCS 115/3; 35 ILCS 110/3)_

| Tax | Who pays | Rate (general merchandise) | Rate (qualifying food/drugs/medical) | Source |
| --- | --- | --- | --- | --- |
| Retailers' Occupation Tax (ROT) | Seller | 6.25% state | 1.0% state | 35 ILCS 120/2 |
| Use Tax (UT) | Buyer (out-of-state) | 6.25% state | 1.0% state | 35 ILCS 105/3 |
| Service Occupation Tax (SOT) | Serviceperson | 6.25% state | 1.0% state | 35 ILCS 115/3 |
| Service Use Tax (SUT) | Consumer of service | 6.25% state | 1.0% state | 35 ILCS 110/3 |

**Note:** In practice, sellers collect all four taxes as a combined "sales tax" and remit on Form ST-1. The buyer sees a single tax rate.

### State rate components

**State rate components**  _(35 ILCS 120/2; 35 ILCS 120/2-10)_

| Component | Rate | Source |
| --- | --- | --- |
| State (general merchandise) | 6.25% | 35 ILCS 120/2 |
| State (qualifying food, drugs, medical appliances) | 1.00% | 35 ILCS 120/2-10 |

### Local rate add-ons (examples, 2025)

Illinois is origin-based for most transactions. The rate is determined by the seller's location.

**Local rate add-ons (examples, 2025)**  _(IDOR tax rate finder)_

| Location | Combined rate (general) | Combined rate (food/drugs) | Source |
| --- | --- | --- | --- |
| Chicago | 10.25% | 2.25% | IDOR tax rate finder |
| Cook County (outside Chicago) | ~9.00-10.25% | varies | IDOR tax rate finder |
| Springfield (Sangamon Co.) | 8.75% | 2.00% | IDOR tax rate finder |
| Champaign | 9.00% | 2.00% | IDOR tax rate finder |

**Important:** Local rates vary by municipality and county. Always verify the exact combined rate for the seller's business location using the IDOR tax rate database (tax.illinois.gov).

### Vendor discount

**Vendor discount**  _(35 ILCS 120/3)_

| Item | Amount | Source |
| --- | --- | --- |
| Vendor discount | 1.75% of state tax collected and timely remitted | 35 ILCS 120/3 |

The vendor discount compensates the retailer for collecting and remitting tax. It applies only to the state portion of the tax and only if the return is filed and paid on time.

## Section 4 -- Computation rules (Step format)

### Step 1: Determine the applicable tax

0. **Step 1** — Selling tangible personal property at retail? --> ROT Providing a service that involves transferring tangible personal property? --> SOT Purchasing from out-of-state for own use in Illinois? --> UT/SUT Most small retailers will report primarily under ROT.

### Step 2: Classify all sales

0. **Step 2** — For each sale, determine: 1. **Taxable or exempt?** (See Section 5 for exemptions.) 2. **General merchandise or qualifying food/drugs/medical?** (Determines rate.) 3. **Location of seller.** (Illinois is origin-based; the rate depends on WHERE YOU SELL FROM.)

### Step 3: Compute gross receipts (ST-1 Line 1)

0. **Step 3** — Sum all receipts from taxable and exempt sales.

### Step 4: Subtract exempt receipts (ST-1 Lines 2-4)

0. **Step 4** — Deduct sales for resale, sales to exempt organizations, and other exempt transactions.

### Step 5: Compute taxable receipts by rate category

0. **Step 5** — General merchandise taxable receipts x applicable combined rate (state + local). Qualifying food/drug/medical taxable receipts x applicable combined rate (state + local at reduced rate).

### Step 6: Compute total tax (ST-1 Line 12)

0. **Step 6** — Sum of all tax amounts by rate category.

### Step 7: Apply vendor discount (ST-1 Line 14)

0. **Step 7** — If filing on time: - State tax portion x 1.75% = vendor discount. - The discount applies only to the state component, not local taxes.

### Step 8: Add use tax if applicable (ST-1 Line 18)

0. **Step 8** — For items purchased from out-of-state vendors without IL tax collected, report use tax at the applicable rate.

### Step 9: Compute net tax due (ST-1 Line 20)

0. **Step 9** — Total tax - vendor discount + use tax = net tax due.

## Section 5 -- Edge cases and special rules

### E-1: Origin-based sourcing

- **Origin-based sourcing** — Illinois is an origin-based state for most sales. The tax rate is determined by the location of the seller, not the buyer. Exception: sales by Illinois retailers to out-of-state buyers may be exempt (see E-3).  _(86 Ill. Admin. Code 130.410.)_

### E-2: Qualifying food, drugs, and medical appliances

- **Qualifying food, drugs, medical appliances** — These items are taxed at the reduced 1% state rate (plus reduced local rates). Qualifying food includes most grocery items but NOT prepared food, soft drinks, candy, or alcoholic beverages.  _(35 ILCS 120/2-10.)_

### E-3: Interstate sales

- **Interstate sales** — Sales shipped to buyers outside Illinois are generally exempt from Illinois ROT if the seller ships the goods via common carrier or U.S. mail. The seller must retain proof of out-of-state delivery.  _(35 ILCS 120/1.)_

### E-4: Service vs. sale distinction

- **Service vs. sale distinction** — If a serviceperson transfers tangible personal property incident to a service, SOT applies to the cost price of the property transferred (not the full service charge). For example, a plumber who installs a faucet pays SOT on the faucet's cost price, not the labor charge.  _(35 ILCS 115/3.)_

### E-5: Exempt organizations

- **Exempt organizations** — Sales to organizations holding a valid Illinois exemption identification number (E-number) are exempt. The seller must retain a copy of the exemption certificate.  _(35 ILCS 120/2-5(11).)_

### E-6: Zero returns

- **Zero returns** — Retailers with no activity must still file a return showing zero tax. Failure to file results in penalties and potential revocation of the certificate of registration.

### E-7: Prepaid phone cards and calling arrangements

- **Prepaid calling arrangements** — Prepaid calling arrangements are taxable as general merchandise at the point of sale.  _(35 ILCS 120/2-25.)_

## Section 6 -- Test suite

### Test 1: Standard retailer, general merchandise

**Input:** Chicago seller. Gross sales: $20,000, all general merchandise, all in-store. No exempt sales.
**Expected:** Combined rate: 10.25%. Tax: $20,000 x 10.25% = $2,050. State portion: $20,000 x 6.25% = $1,250. Vendor discount: $1,250 x 1.75% = $21.88. Net tax: $2,050 - $21.88 = $2,028.12.

### Test 2: Mixed rate sales (food and general)

**Input:** Springfield seller. General merchandise: $10,000. Qualifying food: $5,000.
**Expected:** General: $10,000 x 8.75% = $875. Food: $5,000 x 2.00% = $100. Total: $975. State portion: ($10,000 x 6.25%) + ($5,000 x 1%) = $625 + $50 = $675. Vendor discount: $675 x 1.75% = $11.81. Net: $963.19.

### Test 3: Service with property transfer

**Input:** HVAC contractor in Champaign. Service charges: $3,000. Parts (cost price): $800.
**Expected:** SOT applies to $800 (cost price of parts). Tax: $800 x 9.00% = $72.

### Test 4: Use tax on out-of-state purchase

**Input:** Chicago business purchases $5,000 of equipment from out-of-state vendor, no tax collected.
**Expected:** Use tax: $5,000 x 10.25% = $512.50.

### Test 5: Late filing (no vendor discount)

**Input:** Same as Test 1 but filed 10 days late.
**Expected:** No vendor discount. Net tax: $2,050 plus penalties and interest.

## Section 7 -- Prohibitions

- **P-1:** Do NOT apply destination-based sourcing. Illinois is origin-based for most transactions.
- **P-2:** Do NOT charge the general merchandise rate on qualifying food, drugs, or medical appliances.
- **P-3:** Do NOT apply the vendor discount to local tax amounts -- only the state portion qualifies.
- **P-4:** Do NOT apply SOT to the full service charge -- only the cost price of transferred property.
- **P-5:** Do NOT claim vendor discount on a late-filed return.
- **P-6:** Do NOT assume all food is taxed at the reduced rate. Prepared food, candy, and soft drinks are taxed at the general rate.

## Section 8 -- Self-checks

Before delivering output, verify:

- [ ] Correct combined rate used for seller's location (verified via IDOR tax rate database)
- [ ] Sales properly categorized as general merchandise vs. qualifying food/drugs/medical
- [ ] Origin-based sourcing applied (seller's location determines rate)
- [ ] Vendor discount applied only to state portion and only for timely returns
- [ ] SOT applied to cost price (not retail or service price) for service transactions
- [ ] Use tax reported for out-of-state purchases
- [ ] Zero return filed if no activity
- [ ] Interstate sales properly excluded with documentation

## Section 9 -- Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
