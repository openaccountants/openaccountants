---
name: california-sales-tax
description: Use this skill whenever asked about California sales and use tax, CDTFA filings, California district taxes, California exemptions, California nexus, or any request involving California state sales and use tax compliance. Trigger on phrases like "California sales tax", "CA sales tax", "CDTFA", "CDTFA-401", "district tax", "California use tax", "California resale certificate", or any request involving California sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any California sales tax work.
version: 2.0
---

# California Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | California, United States |
| Jurisdiction code | US-CA |
| Tax type | Sales and Use Tax + District Taxes |
| State base rate | 7.25% (minimum statewide) |
| Local add-on range | 0.10% -- 3.25% district taxes |
| Maximum combined rate | ~10.25% -- 10.75% (parts of Los Angeles, Alameda) |
| Sourcing | Destination-based (district taxes by ship-to address) |
| Economic nexus | $500,000 in total sales (revenue only, no transaction count) |
| Nexus test type | Revenue only -- highest threshold tied with Texas |
| Primary legislation | California Revenue and Taxation Code (R&TC), Division 2, Part 1 |
| Tax authority | California Department of Tax and Fee Administration (CDTFA) |
| Filing portal | https://onlineservices.cdtfa.ca.gov |
| SST member | No |
| Return form | CDTFA-401-A (quarterly/monthly); CDTFA-401-EZ (small sellers) |
| Filing frequencies | Monthly, quarterly, annual (assigned by CDTFA) |
| Quarterly deadlines | Last day of month following quarter (Apr 30, Jul 31, Oct 31, Jan 31) |
| Prepayment | Required if average monthly tax liability exceeds $17,000 |
| Vendor discount | None -- California does not offer a vendor collection allowance |
| Federal framework skill | us-sales-tax (read first for Wayfair, nexus overview, multi-state context) |
| Skill version | 2.0 |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

Before performing any California sales tax work, collect the following:

| # | Question | Why it matters |
|---|----------|----------------|
| 1 | California Seller's Permit number? | Required for filing; confirms registration with CDTFA |
| 2 | Assigned filing frequency (monthly, quarterly, annual)? | Determines return due dates and prepayment requirements |
| 3 | Nexus type (physical, economic, both)? | $500,000 threshold for economic nexus |
| 4 | Sell through marketplace facilitators (Amazon, eBay, Etsy)? | Marketplace facilitators collect on facilitated sales |
| 5 | Primary business address / point of sale location? | Needed for district tax rate determination on counter sales |
| 6 | Ship goods to California customers? From where? | Destination-based sourcing for district taxes |
| 7 | Sell food, software/SaaS, or manufacturing equipment? | Special exemption or taxability rules |
| 8 | Average monthly tax liability exceed $17,000? | Prepayments due 24th of first and second month of quarter |

**If the client cannot answer questions 1-3, STOP and gather this information before proceeding.**

### Refusal catalogue

**R-CA-1 -- Cannabis taxation.** Cannabis excise tax and cultivation tax have separate compliance requirements outside this skill. Escalate to a licensed tax professional.

**R-CA-2 -- Fuel and motor vehicle tax.** Fuel excise taxes and motor vehicle fee-for-service are administered separately. Outside scope.

**R-CA-3 -- Timber yield tax.** Separate tax regime. Outside scope.

---

## Section 3 -- Transaction pattern library

This is the deterministic taxability lookup. When a transaction matches a pattern below, apply the listed treatment. Do not second-guess.

### 3.1 Tangible personal property (TPP)

| Pattern | Taxable? | Rate | Notes |
|---|---|---|---|
| General TPP (electronics, furniture, appliances, equipment, jewelry, sporting goods, office supplies) | TAXABLE | 7.25% + district | R&TC Section 6051 |
| Building materials | TAXABLE | 7.25% + district | |
| Vehicles (private party) | TAXABLE | 7.25% + district | Separate use tax filing via DMV |

### 3.2 Food and beverages

| Pattern | Taxable? | Citation |
|---|---|---|
| Grocery food (cold, unheated, for off-premises consumption) | EXEMPT | R&TC Section 6359 |
| Hot prepared food | TAXABLE | R&TC Section 6359(d)(2) |
| Food sold with eating utensils by vendor | TAXABLE | R&TC Section 6359(d)(1) |
| Food sold at restaurants (dine-in or to-go if heated) | TAXABLE | R&TC Section 6359 |
| Carbonated beverages / soft drinks | TAXABLE | R&TC Section 6359(c) |
| Candy | TAXABLE | R&TC Section 6359(c) |
| Bottled water (non-carbonated, non-flavored) | EXEMPT | |
| Alcoholic beverages | TAXABLE | |
| Snack foods (chips, crackers -- cold, unheated) | EXEMPT | Treated as grocery food |
| Dietary supplements | EXEMPT | R&TC Section 6359(c) |
| Ice | EXEMPT | |

### 3.3 Clothing and footwear

| Pattern | Taxable? | Notes |
|---|---|---|
| All clothing and footwear | TAXABLE | California has NO clothing exemption |
| No sales tax holiday | N/A | California does not hold sales tax holidays |

### 3.4 SaaS and digital goods

| Pattern | Taxable? | Notes |
|---|---|---|
| Canned software (physical media) | TAXABLE | TPP -- R&TC Section 6010.9 |
| Canned software (electronic download with permanent right) | TAXABLE | Regulation 1502.1 |
| Custom software (delivered electronically) | EXEMPT | Not TPP per Regulation 1502.1(a)(3) |
| SaaS (cloud-hosted, no download, no transfer of TPP) | NOT TAXABLE | No transfer of TPP; CDTFA has not taxed pure SaaS |
| Streaming services (no download) | NOT TAXABLE | No transfer of TPP |
| Digital music/movies/books (permanent download) | TAXABLE | Transfer of TPP equivalent |
| Digital music/movies/books (streaming only) | NOT TAXABLE | |

### 3.5 Services

| Pattern | Taxable? | Notes |
|---|---|---|
| Professional services (legal, accounting, consulting, medical, engineering) | NOT TAXABLE | Not a sale of TPP |
| Repair labor (separately stated from parts) | NOT TAXABLE | Labor separately stated is exempt |
| Repair parts | TAXABLE | TPP |
| Fabrication labor (producing a new product to customer spec) | TAXABLE | Fabrication labor is taxable; R&TC Section 6006(b) |
| Installation labor (after sale of TPP, separately stated) | NOT TAXABLE | If separately stated |
| Telecommunications | Separate taxes | Subject to utility users tax, not standard sales tax |

### 3.6 Manufacturing and industrial

| Pattern | Taxable? | Notes |
|---|---|---|
| Manufacturing equipment (used directly in manufacturing) | PARTIAL EXEMPTION | R&TC Section 6377.1 -- state rate reduced; district tax may still apply |
| R&D equipment | PARTIAL EXEMPTION | Same partial exemption program |
| Utilities for manufacturing | PARTIAL EXEMPTION | Same program |
| Farm equipment and machinery | PARTIAL EXEMPTION | R&TC Section 6356.5 |
| Raw materials/ingredients for manufactured products | EXEMPT (resale) | Purchased for resale as component of finished product |

### 3.7 Common exemptions

| Pattern | Exempt? | Citation |
|---|---|---|
| Resale (valid resale certificate) | EXEMPT | R&TC Section 6091 |
| Interstate commerce (shipped out of state) | EXEMPT | R&TC Section 6396 |
| US government purchases | EXEMPT | R&TC Section 6381 |
| California state/local government | EXEMPT | R&TC Section 6381.5 |
| Prescription medicine | EXEMPT | R&TC Section 6369 |
| OTC drugs and medicine | TAXABLE | No OTC exemption in California |
| Newspapers and periodicals | EXEMPT | R&TC Section 6362 |
| Containers and packaging (for resale goods) | EXEMPT | R&TC Section 6364 |

---

## Section 4 -- Rate lookup

### 4.1 State rate components

| Component | Rate |
|---|---|
| State General Fund | 3.9375% |
| State Fiscal Recovery Fund | 0.25% |
| Local Revenue Fund (county) | 1.0625% |
| Local Public Safety Fund | 0.50% |
| County Transportation Fund | 0.25% |
| State Education Protection Account | 0.25% |
| Proposition 30/55 Fund | 1.00% |
| **Total statewide minimum** | **7.25%** |

### 4.2 Key combined rates

| Jurisdiction | Combined rate | Breakdown |
|---|---|---|
| Los Angeles (City) | ~10.25% | 7.25% + 2.25% + 0.75% district |
| San Francisco | ~8.625% | 7.25% + 1.375% district |
| San Jose | ~9.375% | 7.25% + 2.125% district |
| San Diego (City) | ~7.75% | 7.25% + 0.50% district |
| Sacramento (City) | ~8.75% | 7.25% + 1.50% district |
| Oakland | ~10.25% | 7.25% + 3.00% district |
| Fresno | ~8.975% | 7.25% + 1.725% district |

### 4.3 District tax sourcing

| Scenario | Rate applied |
|---|---|
| Shipped goods | District tax at delivery address (destination-based) |
| Counter sales / customer pickup | Rate at seller's location |
| Out-of-state seller shipping to CA | District tax at delivery address |

**Always use CDTFA rate lookup tool for exact rate: https://www.cdtfa.ca.gov/taxes-and-fees/rates.aspx**

---

## Section 5 -- Classification rules

### 5.1 General rule

California imposes sales tax on the retail sale of tangible personal property unless a specific exemption applies. R&TC Section 6051. Services are generally NOT taxable unless they involve fabrication of a new product or transfer of TPP.

### 5.2 Partial exemption for manufacturing (M&E)

| Parameter | Detail |
|---|---|
| Scope | Machinery, equipment, and parts used primarily (50%+) in manufacturing, R&D, or electric power generation |
| Benefit | State portion partially exempted; buyer pays reduced state rate + full district tax |
| Certificate | CDTFA-230-M (Partial Exemption Certificate for Manufacturing) |
| Authority | R&TC Section 6377.1 |

### 5.3 Resale exemption

| Parameter | Detail |
|---|---|
| Certificate | CDTFA-230 (Resale Certificate) |
| Requirement | Buyer must hold California Seller's Permit or be an out-of-state retailer |
| MTC certificate | Accepted |
| SST certificate | California is NOT an SST member |
| Blanket certificates | Permitted for ongoing purchases |

### 5.4 Use tax

| Rule | Detail |
|---|---|
| When applies | TPP purchased from out-of-state seller without CA tax; TPP purchased tax-free and diverted to taxable use |
| Rate | Same as sales tax rate at location of use |
| Credit | Credit for tax paid to other states (R&TC Section 6406) |
| Individual reporting | Schedule G on Form 540 (income tax return) |

---

## Section 6 -- Return form and filing

### 6.1 Filing forms

| Form | Name | Use |
|---|---|---|
| CDTFA-401-A | Sales and Use Tax Return | Standard return |
| CDTFA-401-EZ | Short Form | Small sellers with no adjustments |
| CDTFA-531 | Schedule of District Taxes | District tax detail (auto-populated online) |

### 6.2 Filing frequency

| Frequency | Criteria | Due date |
|---|---|---|
| Quarterly | Most sellers | Last day of month following quarter |
| Monthly | Tax liability > assigned threshold | Last day of following month |
| Annual | Very small sellers | January 31 |

### 6.3 Quarterly due dates

| Quarter | Period | Due date |
|---|---|---|
| Q1 | January 1 -- March 31 | April 30 |
| Q2 | April 1 -- June 30 | July 31 |
| Q3 | July 1 -- September 30 | October 31 |
| Q4 | October 1 -- December 31 | January 31 |

### 6.4 Prepayment requirements

| Parameter | Value |
|---|---|
| Threshold | Average monthly tax liability exceeds $17,000 |
| Due dates | 24th of first and second month of each quarter |
| Amount | At least 90% of actual liability for the month |

---

## Section 7 -- Thresholds, penalties, and deadlines

### 7.1 Economic nexus

| Parameter | Value |
|---|---|
| Revenue threshold | $500,000 in total sales delivered to California |
| Transaction threshold | None -- revenue only |
| Measurement period | Preceding or current calendar year |
| Effective date | April 1, 2019 |
| Sales included | Total sales, including exempt sales |
| Marketplace exclusion | Marketplace sales facilitated by a marketplace provider may count toward threshold |
| Authority | R&TC Section 6203(c)(4) |

### 7.2 Marketplace facilitator rules

| Rule | Detail |
|---|---|
| Effective date | October 1, 2019 |
| Obligation | Marketplace facilitators with $500K in CA sales must collect |
| Seller relief | Sellers relieved for facilitated sales |
| Authority | R&TC Section 6042 |

### 7.3 Penalties and interest

| Penalty | Rate | Citation |
|---|---|---|
| Late filing (1-30 days) | 10% of tax due | R&TC Section 6591 |
| Late payment | 10% of tax due | R&TC Section 6591 |
| Negligence | 10% of deficiency | R&TC Section 6484 |
| Fraud | 25% of deficiency | R&TC Section 6485 |
| Interest | Adjusted quarterly by CDTFA | R&TC Section 6591.5 |

### 7.4 Record retention

| Parameter | Value |
|---|---|
| Period | Minimum 4 years from filing date or due date (whichever is later) |
| Records | Sales invoices, purchase records, exemption certificates, bank statements, POS data, shipping records |

### 7.5 Statute of limitations

| Scenario | Period |
|---|---|
| Standard assessment | 3 years from filing or due date |
| Substantial understatement (25%+) | 8 years |
| No return filed | No limitation |
| Fraud | No limitation |

---

## Section 8 -- Edge cases

### EC1 -- SaaS vs. downloaded software

**Situation:** Business purchases software that is partly cloud-based and partly downloaded.

**Resolution:** If the software requires a download or local installation, the downloaded component is taxable as TPP. If purely accessed through a browser with no download, it is not taxable. Hybrid products require analysis of the primary function.

### EC2 -- Fabrication labor vs. repair labor

**Situation:** A shop builds a custom metal part for a customer.

**Resolution:** Fabrication labor (creating a new product to customer specifications) is TAXABLE under R&TC Section 6006(b). Repair labor (fixing an existing item) is NOT taxable if separately stated from parts. The distinction is whether a new product is being created.

### EC3 -- Manufacturing partial exemption

**Situation:** Manufacturer purchases a $100,000 machine used 60% for manufacturing, 40% for administration.

**Resolution:** Qualifies for partial exemption because manufacturing use exceeds 50%. The state portion is partially exempted. Full district tax still applies at the delivery location rate.

### EC4 -- Food: grocery vs. prepared

**Situation:** Bakery sells cold sandwiches and hot soup from the same counter.

**Resolution:** Cold sandwiches sold without eating utensils provided by the seller are EXEMPT as grocery food. Hot soup is TAXABLE as prepared food. Each item classified separately. If the seller provides eating utensils, all food becomes taxable.

### EC5 -- Drop shipments

**Situation:** Out-of-state retailer directs a California manufacturer to ship to a California customer.

**Resolution:** The California manufacturer must collect tax unless the retailer provides a valid resale certificate. If the retailer is not registered in California, the manufacturer should collect tax on the retail price. Complex area requiring careful certificate management.

---

## Section 9 -- Test suite

### Test 1 -- Basic taxable sale in Los Angeles

**Input:** Retailer sells a $1,000 TV in Los Angeles. Combined rate: 10.25%.
**Expected:** Tax = $102.50. Total = $1,102.50.

### Test 2 -- Grocery food exempt

**Input:** Customer purchases $200 of cold groceries (produce, dairy, bread) at a supermarket.
**Expected:** Tax = $0. Grocery food is exempt.

### Test 3 -- SaaS not taxable

**Input:** San Francisco business subscribes to cloud-based project management tool. $150/month. No download.
**Expected:** Not taxable. Pure SaaS without download is not TPP in California.

### Test 4 -- Economic nexus

**Input:** Oregon-based online seller has $600,000 in California sales. No physical presence. 50 transactions.
**Expected:** Exceeds $500,000 threshold. Must register with CDTFA and collect California sales tax.

### Test 5 -- Clothing fully taxable

**Input:** Customer buys a $300 jacket in San Francisco. Rate: 8.625%.
**Expected:** Tax = $25.88. No clothing exemption in California.

### Test 6 -- Resale certificate

**Input:** Retailer purchases $15,000 of inventory from a CA wholesaler. Provides valid CDTFA-230.
**Expected:** No tax. Retailer collects tax at point of resale.

### Test 7 -- Use tax on out-of-state purchase

**Input:** Los Angeles business purchases $5,000 of office furniture from an Oregon retailer. No tax collected.
**Expected:** Use tax = $512.50 ($5,000 x 10.25%).

### Test 8 -- Hot prepared food

**Input:** Customer buys a $12 hot meal from a deli counter in Sacramento. Rate: 8.75%.
**Expected:** Tax = $1.05. Hot prepared food is taxable.

### Test 9 -- Manufacturing equipment partial exemption

**Input:** Manufacturer purchases a $200,000 production machine in San Jose. Used 100% in manufacturing.
**Expected:** Partial exemption applies to state portion. District tax still applies. Effective tax rate is reduced compared to full combined rate.

### Test 10 -- Canned software download

**Input:** Business purchases a $500 canned software license via electronic download in San Diego. Rate: 7.75%.
**Expected:** Tax = $38.75. Downloaded canned software is taxable as TPP.

---

## Section 10 -- Prohibitions

- NEVER apply a clothing exemption in California -- clothing is fully taxable at all times.
- NEVER treat pure SaaS (cloud-only, no download) as taxable -- California has not extended sales tax to pure SaaS.
- NEVER confuse fabrication labor (taxable) with repair labor (not taxable if separately stated).
- NEVER forget district taxes -- the 7.25% state rate is only the minimum; most locations have additional district taxes.
- NEVER use origin-based sourcing for district taxes -- California is destination-based for district taxes.
- NEVER assume the manufacturing partial exemption fully eliminates tax -- it reduces the state portion but district taxes still apply.
- NEVER accept SST certificates in California -- CA is not an SST member.
- NEVER forget the prepayment requirement for sellers with average monthly liability over $17,000.
- NEVER treat OTC drugs as exempt -- only prescription medicine is exempt in California.
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude.

---

## Disclaimer

This skill is provided for informational and computational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional (CPA, EA, or tax attorney) before filing.


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
