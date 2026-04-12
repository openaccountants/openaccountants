---
name: texas-sales-tax
description: Use this skill whenever asked about Texas sales and use tax, Comptroller filings, Texas tax permits, Texas exemptions, Texas nexus, or any request involving Texas state sales and use tax compliance. Trigger on phrases like "Texas sales tax", "TX sales tax", "Comptroller", "Texas use tax", "Texas sales tax return", "Texas exemption certificate", or any request involving Texas sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any Texas sales tax work.
version: 2.0
---

# Texas Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Texas, United States |
| Jurisdiction code | US-TX |
| Tax type | Sales and Use Tax (state + local) |
| State rate | 6.25% |
| Local rate cap | 2.00% (city + county + transit + special district) |
| Maximum combined rate | 8.25% |
| Sourcing | Origin-based for intrastate; destination-based for remote sellers |
| Economic nexus | $500,000 in taxable sales (revenue only, no transaction count) |
| Primary legislation | Texas Tax Code, Chapter 151 |
| Tax authority | Texas Comptroller of Public Accounts |
| Filing portal | https://comptroller.texas.gov/taxes/sales/ |
| SST member | Yes (associate member) |
| Return form | 01-114 (standard); 01-117 (short form) |
| Filing frequencies | Monthly, quarterly, annual (assigned by Comptroller) |
| Vendor discount | 0.5% of tax due (max $1,750/month) for timely filing |
| No state income tax | Correct -- but franchise tax applies to businesses (separate) |
| Federal framework skill | us-sales-tax |
| Skill version | 2.0 |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

| # | Question | Why it matters |
|---|----------|----------------|
| 1 | Texas Sales and Use Tax Permit number? | Required for filing |
| 2 | Assigned filing frequency? | Determines due dates |
| 3 | Nexus type (physical, economic, both)? | $500,000 threshold |
| 4 | Sell through marketplace facilitators? | Facilitators collect on facilitated sales |
| 5 | Primary business location in Texas? | Origin-based for intrastate sales |
| 6 | Sell services? Which types? | Texas taxes only enumerated services |
| 7 | Sell SaaS or data processing services? | 20% exemption on data processing services |
| 8 | Franchise tax obligations? | Separate from sales tax -- escalate if needed |

### Refusal catalogue

**R-TX-1 -- Franchise tax.** Texas franchise tax (margin tax) is entirely separate. Outside scope.

**R-TX-2 -- Motor vehicle sales tax.** Administered by TxDMV, not Comptroller. Different return process.

**R-TX-3 -- Oil and gas equipment.** Highly specialized drilling/production equipment taxability. Escalate to reviewer.

---

## Section 3 -- Transaction pattern library

### 3.1 Tangible personal property

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP (electronics, furniture, appliances, equipment) | TAXABLE | Tex. Tax Code Section 151.051 |
| Clothing and footwear | TAXABLE | NO clothing exemption except during Sales Tax Holiday |
| Clothing under $100 during August Sales Tax Holiday | EXEMPT | Tex. Tax Code Section 151.326 |

### 3.2 Food and beverages

| Pattern | Taxable? | Citation |
|---|---|---|
| Grocery food (for home consumption) | EXEMPT | Sec. 151.314 |
| Prepared food (heated, served with utensils) | TAXABLE | Sec. 151.314(c) |
| Soft drinks / candy | TAXABLE | Sec. 151.314(b) |
| Bakery items (unheated, no utensils) | EXEMPT | |
| Dietary supplements | EXEMPT | |
| Bottled water | EXEMPT | |
| Ice | EXEMPT | |
| Alcoholic beverages | TAXABLE | |

### 3.3 SaaS and digital goods

| Pattern | Taxable? | Notes |
|---|---|---|
| Canned software (any delivery) | TAXABLE | Sec. 151.009 |
| Custom software (any delivery) | TAXABLE | Unlike most states, TX taxes custom software |
| SaaS (cloud-hosted) | TAXABLE | As data processing service -- 20% exemption applies |
| Data processing services | TAXABLE (80%) | Only 80% of charge taxable; 20% exempt under Sec. 151.351 |
| Streaming services | TAXABLE | As amusement services |
| Digital books, music, movies (download) | TAXABLE | Treated as TPP |

**CRITICAL: Texas provides a 20% exemption for data processing services. Only 80% of the charge is subject to tax.**

### 3.4 Services

| Pattern | Taxable? | Citation |
|---|---|---|
| Amusement services | TAXABLE | Sec. 151.0028 |
| Cable television | TAXABLE | Sec. 151.0033 |
| Credit reporting / debt collection | TAXABLE | Sec. 151.0039 |
| Data processing | TAXABLE (80%) | Sec. 151.0035; 20% exempt |
| Information services | TAXABLE | Sec. 151.0038 |
| Laundry/cleaning/garment services | TAXABLE | Sec. 151.0045 |
| Motor vehicle parking/storage | TAXABLE | Sec. 151.0048 |
| Nonresidential real property repair/remodeling | TAXABLE | Sec. 151.0048 |
| Pest control | TAXABLE | |
| Security services | TAXABLE | |
| Telecommunication | TAXABLE | Sec. 151.0103 |
| Waste/trash removal | TAXABLE | |
| Professional services (legal, accounting, consulting, medical, engineering) | NOT TAXABLE | Not enumerated |
| Residential construction labor | NOT TAXABLE | |
| Residential real property services (cleaning, landscaping) | NOT TAXABLE | |
| Advertising | NOT TAXABLE | |
| Transportation/freight | NOT TAXABLE | |
| Education | NOT TAXABLE | |

### 3.5 Manufacturing and exemptions

| Pattern | Taxable? | Citation |
|---|---|---|
| Manufacturing equipment (directly in manufacturing) | EXEMPT | Sec. 151.318 |
| Raw materials / ingredients for manufactured product | EXEMPT | Sec. 151.318 |
| Farm/ranch machinery | EXEMPT | Sec. 151.316 |
| Agricultural supplies (feed, seed, fertilizer) | EXEMPT | Sec. 151.316 |
| Resale (Form 01-339) | EXEMPT | Sec. 151.302 |
| Interstate commerce (shipped out of state) | EXEMPT | Sec. 151.307 |
| Federal government | EXEMPT | Sec. 151.309 |
| Prescription drugs | EXEMPT | Sec. 151.313 |
| OTC drugs and medicine | EXEMPT | Sec. 151.313 -- Texas exempts OTC (unlike many states) |
| Containers/packaging for resale goods | EXEMPT | Sec. 151.302(c) |
| Newspapers/periodicals | EXEMPT | Sec. 151.320 |

---

## Section 4 -- Rate lookup

### 4.1 Rate structure

| Component | Maximum rate |
|---|---|
| State | 6.25% |
| City | 2.00% |
| County | 0.50% |
| Transit authority | 1.00% |
| Special district | Varies |
| **Combined cap** | **8.25%** |

### 4.2 Sourcing

| Scenario | Rate applied |
|---|---|
| Intrastate (seller and buyer both in TX) | Rate at seller's location (origin-based) |
| Remote (out-of-state) sellers | Rate at buyer's ship-to address (destination-based) |

---

## Section 5 -- Classification rules

### 5.1 General rule

All sales of TPP taxable unless specifically exempted. Only specifically enumerated services are taxable. Tex. Tax Code Section 151.051.

### 5.2 Data processing 20% exemption

SaaS and data processing services: only 80% of the charge is taxable. The 20% exemption applies automatically. Tex. Tax Code Section 151.351.

### 5.3 Residential vs. nonresidential

Nonresidential real property services are taxable. Residential real property services (cleaning, landscaping, repairs) are NOT taxable. Classification depends on property type, not customer type.

---

## Section 6 -- Return form and filing

### 6.1 Forms

| Form | Use |
|---|---|
| 01-114 | Standard sales and use tax return |
| 01-117 | Short form |
| 01-115 | Schedule A -- local tax detail |
| 01-148 | Use tax return (purchasers) |
| 01-339 | Exemption/resale certificate |

### 6.2 Due dates

| Frequency | Due date |
|---|---|
| Monthly | 20th of following month |
| Quarterly | April 20, July 20, October 20, January 20 |
| Annual | January 20 |

### 6.3 Mandatory e-filing

Taxpayers who paid $50,000+ in state tax in preceding fiscal year must file electronically via WebFile.

---

## Section 7 -- Thresholds, penalties, and deadlines

### 7.1 Economic nexus

| Parameter | Value |
|---|---|
| Revenue threshold | $500,000 in taxable items in TX |
| Transaction threshold | None |
| Measurement period | Preceding 12 calendar months |
| Sales included | Only taxable items; exempt sales do NOT count |
| Authority | Sec. 151.107; Comptroller Rule 3.286 |

### 7.2 Penalties

| Penalty | Rate |
|---|---|
| Late filing (1-30 days) | 5% of tax due |
| Late filing (>30 days) | 10% of tax due |
| Fraud | 50% of deficiency |

### 7.3 Vendor discount

| Parameter | Value |
|---|---|
| Rate | 0.5% of tax due |
| Maximum | $1,750/month for timely filers |

### 7.4 Record retention

4 years from filing or due date.

### 7.5 Statute of limitations

| Scenario | Period |
|---|---|
| Standard | 4 years |
| No return | Unlimited |
| Fraud | Unlimited |
| 25%+ understatement | 6 years |

---

## Section 8 -- Edge cases

### EC1 -- Data processing 20% exemption

**Situation:** Business purchases $1,000/month SaaS.
**Resolution:** Taxable amount = $800 (80%). At 8.25%: tax = $66.00, not $82.50.

### EC2 -- Residential vs. nonresidential cleaning

**Situation:** Cleaning company serves both commercial offices and homes.
**Resolution:** Commercial (nonresidential) = TAXABLE. Residential = NOT TAXABLE. Classify by property type.

### EC3 -- Sales Tax Holiday

**Situation:** Customer buys $75 jeans during August holiday weekend.
**Resolution:** EXEMPT. Clothing under $100/item during holiday. Sec. 151.326.

### EC4 -- Motor vehicle

**Situation:** Dealer sells a vehicle.
**Resolution:** Motor vehicle sales tax (6.25%) administered by TxDMV, not Comptroller. Separate process.

### EC5 -- Custom software

**Situation:** Business purchases custom-developed software.
**Resolution:** TAXABLE in Texas (unlike most states). Sec. 151.009.

---

## Section 9 -- Test suite

### Test 1 -- Basic sale in Houston

**Input:** $800 TV. Rate: 8.25%.
**Expected:** Tax = $66.00.

### Test 2 -- Grocery exempt

**Input:** $150 of bread, eggs, meat.
**Expected:** Tax = $0.

### Test 3 -- Data processing 20% exemption

**Input:** $2,000/month SaaS. Rate: 8.25%.
**Expected:** Taxable = $1,600. Tax = $132.00.

### Test 4 -- Economic nexus

**Input:** NY seller, $550K Texas sales, 12 months, no physical presence.
**Expected:** Exceeds $500K. Must register.

### Test 5 -- OTC medicine exempt

**Input:** $30 OTC cold medicine.
**Expected:** Tax = $0. OTC exempt in Texas.

### Test 6 -- Nonresidential cleaning

**Input:** $500 commercial janitorial. Rate: 8.25%.
**Expected:** Tax = $41.25.

### Test 7 -- Residential cleaning

**Input:** $200 home cleaning.
**Expected:** Tax = $0. Residential exempt.

### Test 8 -- Manufacturing equipment

**Input:** $50,000 production machine. Form 01-339.
**Expected:** Tax = $0.

### Test 9 -- Vendor discount

**Input:** Timely pays $10,000 in tax.
**Expected:** Discount = $50. Net = $9,950.

### Test 10 -- Clothing during holiday

**Input:** $75 jeans during August Sales Tax Holiday.
**Expected:** Tax = $0.

---

## Section 10 -- Prohibitions

- NEVER apply a general clothing exemption -- clothing is taxable except during the Sales Tax Holiday.
- NEVER assume all services are taxable -- Texas taxes only enumerated services.
- NEVER forget the 20% data processing exemption on SaaS.
- NEVER confuse motor vehicle sales tax (TxDMV) with general sales tax (Comptroller).
- NEVER apply destination-based sourcing for intrastate Texas sales -- Texas is origin-based for intrastate.
- NEVER assume nonprofits are automatically exempt -- must have Comptroller-issued exemption number.
- NEVER include exempt sales in the economic nexus threshold -- Texas counts only taxable sales.
- NEVER file without claiming the timely filing discount if eligible.
- NEVER treat residential and nonresidential real property services the same.
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude.

---

## Disclaimer

This skill is provided for informational and computational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional (CPA, EA, or tax attorney) before filing.
