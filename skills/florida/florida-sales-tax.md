---
name: florida-sales-tax
description: Use this skill whenever asked about Florida sales and use tax, DOR filings, Florida discretionary surtax, Florida exemptions, Florida nexus, Florida commercial rent tax, or any request involving Florida state sales and use tax compliance. Trigger on phrases like "Florida sales tax", "FL sales tax", "Florida DOR", "DR-15", "Florida surtax", "Florida commercial rent", "Florida resale certificate", or any request involving Florida sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any Florida sales tax work.
version: 2.0
---

# Florida Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Florida, United States |
| Jurisdiction code | US-FL |
| Tax type | Sales and Use Tax + Discretionary Sales Surtax |
| State rate | 6.00% |
| Surtax range | 0% -- 1.5% by county |
| Maximum combined rate | 7.5% |
| Surtax $5,000 cap | Surtax applies only to first $5,000 of any single item |
| Commercial rent tax | 2.0% (unique to Florida) |
| Sourcing | Destination-based (surtax at delivery address) |
| Economic nexus | $100,000 in taxable remote sales (revenue only) |
| Primary legislation | Chapter 212, Florida Statutes |
| Tax authority | Florida Department of Revenue (DOR) |
| Filing portal | https://floridarevenue.com |
| SST member | No |
| Return form | DR-15 (standard); DR-15EZ (short form) |
| Vendor discount | 2.5% of first $1,200 of tax due; max $30/return |
| No state income tax | Yes (corporate income/franchise tax 5.5% is separate) |
| Federal framework skill | us-sales-tax |
| Skill version | 2.0 |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

| # | Question | Why it matters |
|---|----------|----------------|
| 1 | Florida Certificate of Registration number (DR-11)? | Required for filing |
| 2 | Assigned filing frequency? | Monthly, quarterly, semi-annual, annual |
| 3 | Nexus type? | $100,000 threshold for economic nexus |
| 4 | Sell through marketplace facilitators? | Marketplace providers collect on facilitated sales |
| 5 | Lease or sublease commercial real property? | Florida ONLY state that taxes commercial rent (2.0%) |
| 6 | Operate transient rental accommodations? | 6% + surtax + county tourist development tax |
| 7 | Primary county of operation? | Surtax rates vary by county |
| 8 | Sell telecommunications/cable/internet? | Communication Services Tax is separate |

### Refusal catalogue

**R-FL-1 -- Communication Services Tax (CST).** Separate tax with own rates and returns (DR-15CS). Outside scope.

**R-FL-2 -- Tourist development tax.** Reported separately to county, not on DR-15. Outside scope for detailed filing.

**R-FL-3 -- Boat/aircraft tax cap changes.** Cap amounts subject to legislative change. Escalate to reviewer for current caps.

---

## Section 3 -- Transaction pattern library

### 3.1 Tangible personal property

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE | F.S. Section 212.05 |
| Clothing and footwear | TAXABLE | NO clothing exemption (except during holiday) |
| Boats | TAXABLE (capped) | $18,000 max state tax on boats |
| Aircraft | TAXABLE (capped) | Separate cap applies |

### 3.2 Food and beverages

| Pattern | Taxable? | Citation |
|---|---|---|
| Grocery food (unprepared, for home consumption) | EXEMPT | F.S. Section 212.08(1) |
| Prepared food (heated, on-premises) | TAXABLE | F.S. Section 212.08(1)(a) |
| Candy (not at restaurant) | EXEMPT | Treated as food in FL |
| Soft drinks (not at restaurant) | EXEMPT | Treated as food in FL |
| Bakery items (unheated, to go) | EXEMPT | |
| Alcoholic beverages | TAXABLE | |
| Restaurant meals | TAXABLE | |

### 3.3 SaaS and digital goods

| Pattern | Taxable? | Notes |
|---|---|---|
| Canned software (any delivery) | TAXABLE | DOR Rule 12A-1.032 |
| Custom software (electronic delivery) | TAXABLE | Florida taxes custom software too |
| SaaS (cloud-hosted) | TAXABLE | Treated as license of software; evolving area |
| Digital books/music/movies (download) | TAXABLE | TPP |
| Streaming services | Subject to CST | Communication Services Tax, not standard sales tax |

### 3.4 Services

| Pattern | Taxable? | Notes |
|---|---|---|
| Nonresidential pest control | TAXABLE | F.S. Section 212.05(1)(i) |
| Nonresidential cleaning/janitorial | TAXABLE | |
| Burglar protection/security | TAXABLE | |
| Detective/investigation (nonresidential) | TAXABLE | |
| Commercial rent | TAXABLE at 2.0% | F.S. Section 212.031 -- UNIQUE TO FLORIDA |
| Transient accommodations | TAXABLE at 6% + surtax | Plus county tourist development tax |
| Admissions/amusements | TAXABLE | F.S. Section 212.04 |
| Professional services (legal, accounting, medical, consulting) | NOT TAXABLE | |
| Residential services | NOT TAXABLE | |
| Advertising, transportation, construction labor | NOT TAXABLE | |

### 3.5 Commercial rent tax (UNIQUE TO FLORIDA)

| Parameter | Value |
|---|---|
| Rate | 2.0% on total rent for commercial real property |
| Surtax | County surtax also applies on top |
| Applies to | Office, retail, warehouse, commercial leases, subleases |
| Does NOT apply to | Residential rent |
| Responsible party | Landlord collects from tenant, remits to DOR |
| Authority | F.S. Section 212.031 |

### 3.6 Exemptions

| Pattern | Taxable? | Citation |
|---|---|---|
| Grocery food | EXEMPT | F.S. 212.08(1) |
| Prescription drugs | EXEMPT | F.S. 212.08(2) |
| OTC drugs | TAXABLE | No general exemption |
| Manufacturing machinery | EXEMPT | F.S. 212.08(5)(b) |
| Agricultural equipment | EXEMPT | F.S. 212.08(3) |
| Resale (DR-13, renewed annually) | EXEMPT | F.S. 212.18(3) |
| Interstate commerce | EXEMPT | F.S. 212.06(5)(a) |
| Government purchases | EXEMPT | F.S. 212.08(6) |
| Aircraft parts/modification | EXEMPT | F.S. 212.08(7)(ff) |

---

## Section 4 -- Rate lookup

### 4.1 Key county rates

| County | Surtax | Combined rate |
|---|---|---|
| Miami-Dade | 1.00% | 7.00% |
| Broward | 1.00% | 7.00% |
| Orange (Orlando) | 0.50% | 6.50% |
| Hillsborough (Tampa) | 1.50% | 7.50% |
| Duval (Jacksonville) | 1.50% | 7.50% |
| Palm Beach | 1.00% | 7.00% |
| Leon (Tallahassee) | 1.50% | 7.50% |

### 4.2 Surtax $5,000 cap

The discretionary surtax applies only to the first $5,000 of any single item. F.S. Section 212.054(2)(b).

---

## Section 5 -- Classification rules

### 5.1 General rule

All sales of TPP taxable unless specifically exempted. F.S. Section 212.05. Services taxable only if specifically enumerated.

### 5.2 DR-13 resale certificate

Annual certificate. Must be for the correct year. Expired certificates do NOT protect the seller.

### 5.3 Surtax cap calculation

For a $20,000 item in a 1.5% surtax county: State tax = $20,000 x 6% = $1,200. Surtax = $5,000 x 1.5% = $75 (capped). Total = $1,275.

---

## Section 6 -- Return form and filing

### 6.1 Forms

| Form | Use |
|---|---|
| DR-15 | Standard sales and use tax return |
| DR-15EZ | Short form for small dealers |
| DR-13 | Annual resale certificate |
| DR-14 | Exempt organization certificate |

### 6.2 Due dates

| Frequency | Due date |
|---|---|
| Monthly | 1st-20th of following month |
| Quarterly | 1st-20th of month following quarter |
| Semi-annual | 1st-20th of month following period |
| Annual | January 1-20 |

---

## Section 7 -- Thresholds, penalties, and deadlines

### 7.1 Economic nexus

| Parameter | Value |
|---|---|
| Revenue threshold | $100,000 in taxable remote sales |
| Transaction threshold | None |
| Measurement period | Previous calendar year |
| Effective date | July 1, 2021 |
| Authority | F.S. Section 212.0596 |

### 7.2 Penalties

| Penalty | Rate |
|---|---|
| Late filing (1-30 days) | 10% of tax due (min $50) |
| Late filing (>30 days) | Additional 10%/month (max 50%) |
| Fraud | 100% of deficiency |
| Failure to register | Misdemeanor; $250-$5,000 fine |

### 7.3 Record retention

3 years from filing date.

### 7.4 Statute of limitations

| Scenario | Period |
|---|---|
| Standard | 3 years |
| No return | Unlimited |
| Fraud | Unlimited |

---

## Section 8 -- Edge cases

### EC1 -- Commercial rent tax

**Situation:** Business leases office in Miami-Dade for $5,000/month.
**Resolution:** 2.0% + 1.0% surtax = 3.0%. Tax = $150/month.

### EC2 -- Surtax $5,000 cap

**Situation:** $20,000 equipment in Hillsborough County (1.5% surtax).
**Resolution:** State: $1,200. Surtax: $75 (on first $5,000 only). Total: $1,275.

### EC3 -- Transient rental

**Situation:** Vacation rental $200/night x 7 nights in Osceola County.
**Resolution:** Gross = $1,750. State + surtax on DR-15. Tourist development tax reported separately to county.

### EC4 -- Boat purchase cap

**Situation:** $500,000 boat purchase.
**Resolution:** Max state tax = $18,000 regardless of price. Plus surtax on first $5,000.

### EC5 -- DR-13 expired

**Situation:** Seller accepts prior-year DR-13 for a resale purchase.
**Resolution:** Invalid. Seller is liable for uncollected tax. Must be current year.

---

## Section 9 -- Test suite

### Test 1 -- Basic sale in Miami

**Input:** $1,200 laptop in Miami-Dade (7%). Single item.
**Expected:** State = $72. Surtax = $12. Total = $84.

### Test 2 -- Grocery exempt

**Input:** $200 groceries.
**Expected:** Tax = $0.

### Test 3 -- Commercial rent

**Input:** $10,000/month office in Orange County (0.5% surtax).
**Expected:** Rent tax = $200. Surtax = $50. Total = $250.

### Test 4 -- Surtax cap

**Input:** $50,000 machine in Duval (1.5% surtax).
**Expected:** State = $3,000. Surtax = $75 (capped). Total = $3,075.

### Test 5 -- Economic nexus

**Input:** CA seller, $120K Florida sales last year.
**Expected:** Exceeds $100K. Must register.

### Test 6 -- Clothing taxable

**Input:** $150 dress in Broward (7%).
**Expected:** Tax = $10.50. Clothing fully taxable.

### Test 7 -- Vendor discount

**Input:** $800 tax due, filed on time.
**Expected:** Discount = $20 (2.5% of $800). Net = $780.

### Test 8 -- Candy exempt

**Input:** $10 bag of candy at grocery store.
**Expected:** Tax = $0. Candy treated as food in FL (not at restaurant).

### Test 9 -- Resale certificate

**Input:** $8,000 inventory. Valid current-year DR-13.
**Expected:** No tax.

### Test 10 -- SaaS

**Input:** $200/month SaaS in Miami-Dade (7%).
**Expected:** Tax = $14. SaaS generally taxable in FL.

---

## Section 10 -- Prohibitions

- NEVER apply a clothing exemption in Florida -- clothing is fully taxable (except during holidays).
- NEVER forget the $5,000 surtax cap on single items.
- NEVER ignore the commercial rent tax -- Florida is the ONLY state that taxes commercial rent.
- NEVER confuse CST with general sales tax -- separate taxes, separate returns.
- NEVER treat tourist development tax as part of DR-15 -- reported separately to county.
- NEVER assume DR-13 resale certificates are perpetual -- renewed annually.
- NEVER accept SST certificates -- FL is not an SST member.
- NEVER assume residential rent is taxable -- only COMMERCIAL rent.
- NEVER overlook the boat/aircraft tax cap on large purchases.
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude.

---

## Disclaimer

This skill is provided for informational and computational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional (CPA, EA, or tax attorney) before filing.
