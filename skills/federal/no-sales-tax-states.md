---
name: no-sales-tax-states
description: Use this skill whenever asked about states with no sales tax, Alaska local sales tax, Delaware gross receipts tax, Montana resort tax, New Hampshire meals and rooms tax, Oregon Corporate Activity Tax, or tax obligations in AK, DE, MT, NH, or OR. Trigger on phrases like "no sales tax states", "Alaska sales tax", "Delaware gross receipts", "Montana resort tax", "New Hampshire meals tax", "Oregon CAT", "Oregon no sales tax", or any request involving tax compliance in states that do not impose a general statewide sales tax. ALWAYS load us-sales-tax first for federal context.
version: 2.0
---

# No-Sales-Tax States Skill v2.0 -- AK, DE, MT, NH, OR

## Section 1 -- Quick reference

| State | No general sales tax | But has... |
|---|---|---|
| Alaska (AK) | Correct | Local sales taxes (boroughs/cities up to 7.5%) |
| Delaware (DE) | Correct | Gross Receipts Tax on sellers (0.0945% to 1.9914%) |
| Montana (MT) | Correct | Resort Tax in tourist communities (up to 3%) |
| New Hampshire (NH) | Correct | Meals & Rooms Tax (8.5%) |
| Oregon (OR) | Correct | Corporate Activity Tax (CAT) -- 0.57% on commercial activity over $1M |

**"No sales tax" does NOT mean "no consumption-related taxes." Each state has alternative mechanisms.**

| Field | Value |
|---|---|
| Skill version | 2.0 |
| Federal framework skill | us-sales-tax |

---

## Section 2 -- Required inputs and refusal catalogue

### Refusal catalogue

**R-NOST-1 -- Alaska individual local jurisdiction compliance.** Each of ~100+ local jurisdictions administers its own tax. Detailed compliance for specific jurisdictions requires research beyond this skill.

**R-NOST-2 -- Oregon CAT detailed compliance.** CAT involves subtraction calculations and quarterly estimates. Escalate to CPA.

**R-NOST-3 -- Delaware GRT classification disputes.** GRT rate depends on business type classification. Escalate if disputed.

---

## Section 3 -- Transaction pattern library

### 3.1 Alaska (AK)

| Pattern | Treatment | Notes |
|---|---|---|
| Sale in Anchorage | NO TAX | Anchorage has no local sales tax |
| Sale in Juneau | LOCAL TAX 5% | Juneau City & Borough |
| Sale in Kodiak | LOCAL TAX 7% | One of the highest |
| Sale in Sitka | LOCAL TAX 6% | |
| Sale in Fairbanks | NO TAX | No borough or city tax |
| Sale in Skagway | LOCAL TAX 5% | Tourism-driven |
| Grocery food (varies by locality) | Varies | Some jurisdictions exempt; others tax |
| Prescription drugs | Generally EXEMPT | Most jurisdictions |
| Clothing | TAXABLE where local tax applies | |

### 3.2 Delaware (DE)

| Pattern | Treatment | Notes |
|---|---|---|
| Any retail purchase by buyer | NO TAX to buyer | DE has no sales tax |
| Retailer's gross receipts | GRT 0.7468%/month | Tax on SELLER, not buyer |
| Grocer's gross receipts | GRT 0.0945%/month | Lower rate for grocers |
| Restaurant gross receipts | GRT 0.6758%/month | |
| Wholesaler gross receipts | GRT 0.3985%/month | |
| Manufacturer gross receipts | GRT 0.0945%/month | |
| Professional gross receipts | GRT 0.3944%/month | |

### 3.3 Montana (MT)

| Pattern | Treatment | Notes |
|---|---|---|
| Purchase in resort community (Big Sky, Whitefish, etc.) | RESORT TAX up to 3% | On retail goods and services |
| Purchase outside resort communities | NO TAX | |
| Hotel/lodging (statewide) | 4% LODGING TAX | MCA Section 15-65-111 |
| Rental car | 4% RENTAL TAX | MCA Section 15-68-101 |

### 3.4 New Hampshire (NH)

| Pattern | Treatment | Notes |
|---|---|---|
| Retail goods (clothing, electronics, etc.) | NO TAX | |
| Restaurant meals (prepared food) | 8.5% MEALS TAX | RSA 78-A |
| Hotel/lodging/Airbnb | 8.5% ROOMS TAX | RSA 78-A |
| Motor vehicle rental | 8.5% RENTAL TAX | RSA 78-A |
| SaaS and digital goods | NO TAX | |
| Services | NO TAX | |

### 3.5 Oregon (OR)

| Pattern | Treatment | Notes |
|---|---|---|
| Any retail purchase | NO TAX | Oregon has zero sales tax everywhere |
| Any service | NO TAX | |
| Business with $1M+ OR commercial activity | CAT: $250 + 0.57% | ORS 317A; cannot be separately stated on invoices |
| Hotel/lodging | 1.5% STATE + local | ORS 320.305 |

---

## Section 4 -- Rate lookup

### 4.1 Alaska local rates (selected)

| Jurisdiction | Rate |
|---|---|
| Juneau | 5.00% |
| Kodiak | 7.00% |
| Sitka | 6.00% |
| Skagway | 5.00% |
| Ketchikan | 3.50% |
| Kenai Peninsula Borough | 3.00% |
| Anchorage | 0% |
| Fairbanks | 0% |

### 4.2 Alaska Remote Seller Sales Tax Commission (ARSSTC)

Remote sellers can register through ARSSTC (https://arsstc.org) for centralized filing in participating jurisdictions. Not all jurisdictions participate.

---

## Section 5 -- Classification rules

### 5.1 Key distinctions

| Concept | Rule |
|---|---|
| Alaska: no state agency for local tax | Each jurisdiction administers its own tax separately |
| Delaware: GRT is on SELLER | Cannot be passed to buyer as "sales tax" line item |
| Montana: resort tax is local | Only in designated resort communities |
| New Hampshire: meals & rooms only | Retail goods completely untaxed |
| Oregon: CAT cannot be itemized | Oregon law prohibits businesses from adding CAT as line item |

### 5.2 Use tax obligations

Buyers who purchase in no-sales-tax states may owe USE TAX in their home state on items brought back.

---

## Section 6 -- Return form and filing

| State | Return | Frequency | Due date | Portal |
|---|---|---|---|---|
| AK (local) | Varies by jurisdiction | Varies | Varies | ARSSTC or individual jurisdiction |
| DE | Monthly GRT Return | Monthly | 20th of following month | https://revenue.delaware.gov |
| MT (resort) | Local resort tax return | Varies | Varies by community | https://mtrevenue.gov |
| MT (lodging) | Lodging tax return | Varies | Varies | https://mtrevenue.gov |
| NH | Form MR (Meals & Rooms) | Monthly | 15th of following month | https://www.revenue.nh.gov |
| OR | CAT Annual Return | Annual | April 15 | https://revenueonline.dor.oregon.gov |

---

## Section 7 -- Thresholds, penalties, and deadlines

### 7.1 Economic nexus

| State | Threshold | Notes |
|---|---|---|
| AK | Local jurisdiction determines | ARSSTC may set uniform remote seller thresholds |
| DE | N/A | GRT applies to businesses operating IN Delaware |
| MT | N/A | Resort tax based on physical presence in resort community |
| NH | N/A | Meals & rooms tax on businesses operating in NH |
| OR | $1M commercial activity | CAT threshold |

---

## Section 8 -- Edge cases

### EC1 -- Alaska remote seller compliance

**Situation:** Texas e-commerce seller ships to customers throughout Alaska.
**Resolution:** Must determine which delivery addresses fall in taxing jurisdictions. ARSSTC for participating jurisdictions. Non-participating handled individually. Anchorage = no tax. Juneau = 5%.

### EC2 -- Delaware "tax-free shopping" marketing

**Situation:** Delaware retailer advertises "tax-free."
**Resolution:** Accurate from buyer's perspective. Retailer pays GRT built into prices. Out-of-state shoppers may owe use tax in home state.

### EC3 -- Oregon seller with multi-state customers

**Situation:** Oregon e-commerce company sells nationwide. Exceeds nexus in 15 states.
**Resolution:** No Oregon sales tax. Must collect in each state where nexus met. Oregon's lack of sales tax does not exempt from other states' laws.

### EC4 -- NH border shopping

**Situation:** MA residents purchase goods in NH.
**Resolution:** Items brought to MA subject to MA use tax (6.25%). Self-assessed on MA income tax return. Business purchases auditable.

### EC5 -- Montana resort tax for online seller

**Situation:** Online seller ships to Big Sky.
**Resolution:** Resort tax applicability to remote sellers unclear. Verify with specific resort community.

---

## Section 9 -- Test suite

### Test 1 -- Alaska: Juneau

**Input:** $500 item shipped to Juneau. Rate: 5%.
**Expected:** Tax = $25.

### Test 2 -- Alaska: Anchorage

**Input:** $500 item shipped to Anchorage.
**Expected:** Tax = $0.

### Test 3 -- Delaware: no buyer tax

**Input:** $1,000 electronics at Delaware store.
**Expected:** No tax to buyer. Retailer pays GRT.

### Test 4 -- NH: restaurant meal

**Input:** $80 dinner at NH restaurant. Rate: 8.5%.
**Expected:** Tax = $6.80.

### Test 5 -- NH: retail purchase

**Input:** $500 laptop at NH store.
**Expected:** Tax = $0.

### Test 6 -- Oregon: no tax

**Input:** $2,000 merchandise in Oregon.
**Expected:** Tax = $0.

### Test 7 -- Montana: resort community

**Input:** $200 item in Big Sky. Resort tax: 3%.
**Expected:** Tax = $6.

---

## Section 10 -- Prohibitions

- NEVER state Alaska has no sales tax without qualifying that local jurisdictions may impose up to 7.5%.
- NEVER state Delaware is "completely tax-free" -- GRT applies to sellers.
- NEVER assume Oregon seller has no multi-state obligations.
- NEVER apply any sales tax rate in Oregon.
- NEVER forget NH's 8.5% Meals & Rooms Tax.
- NEVER assume Montana is completely tax-free -- resort tax and lodging tax apply.
- NEVER advise buyers that no-sales-tax state purchases are free of all tax -- use tax may apply in home state.
- NEVER add Oregon's CAT as a separate line item on invoices.
- NEVER confuse Delaware's GRT (tax on seller) with a sales tax (tax on buyer).
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude.

---

## Disclaimer

This skill is provided for informational and computational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional (CPA, EA, or tax attorney) before filing.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
