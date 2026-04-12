---
name: illinois-sales-tax
description: Use this skill whenever asked about Illinois sales and use tax, Retailers' Occupation Tax (ROT), Illinois use tax, Service Occupation Tax, IDOR filings, Illinois exemptions, Illinois nexus, or any request involving Illinois state sales and use tax compliance. Trigger on phrases like "Illinois sales tax", "IL sales tax", "ROT", "Retailers Occupation Tax", "IDOR", "ST-1", "Illinois exemption certificate", or any request involving Illinois sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any Illinois sales tax work.
version: 2.0
---

# Illinois Sales and Use Tax Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Illinois, United States |
| Jurisdiction code | US-IL |
| Tax type | Retailers' Occupation Tax (ROT) + Use Tax + Service Occupation Tax (SOT) + Service Use Tax |
| General merchandise state rate | 6.25% |
| Qualifying food/drugs/medical rate | 1.00% (REDUCED, not exempt) |
| Local add-ons | RTA 0.75-1.25%, county/city 0.25-1.75%, home rule up to 3.75%+ |
| Maximum combined rate | 10.25%+ (parts of Chicago/Cook County) |
| Sourcing | Origin-based for intrastate; destination-based for remote sellers |
| Economic nexus | $100,000 OR 200 transactions (OR test) |
| Primary legislation | 35 ILCS 120 (ROT); 35 ILCS 105 (Use Tax); 35 ILCS 110 (SOT); 35 ILCS 115 (Service Use Tax) |
| Tax authority | Illinois Department of Revenue (IDOR) |
| Filing portal | https://mytax.illinois.gov |
| SST member | No |
| Return form | ST-1 (covers all four taxes) |
| Vendor discount | 1.75% of tax due; max $1,000/return |
| Federal framework skill | us-sales-tax |
| Skill version | 2.0 |

**CRITICAL: Illinois has FOUR separate taxes that function together. Illinois taxes grocery food and drugs at a REDUCED 1% rate -- they are NOT exempt.**

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

| # | Question | Why it matters |
|---|----------|----------------|
| 1 | Illinois Certificate of Registration number? | Required for filing |
| 2 | Assigned filing frequency? | Monthly, quarterly, annual |
| 3 | Nexus type? | $100K OR 200 transactions |
| 4 | Sell through marketplace facilitators? | Facilitators collect on facilitated sales |
| 5 | Provide services transferring TPP? | SOT applies to TPP transferred incident to service |
| 6 | Located in a home rule municipality? | Home rule can impose significant additional taxes |
| 7 | Sell food, drugs, or medical appliances? | Reduced 1% state rate |
| 8 | Sell software or SaaS? | Downloaded software taxable; pure SaaS NOT taxable |

### Refusal catalogue

**R-IL-1 -- Home rule municipal taxes.** Each home rule municipality has unique ordinances. Escalate to reviewer for specific compliance.

**R-IL-2 -- Chicago amusement tax on streaming.** 9% separate municipal tax. Outside scope for filing.

---

## Section 3 -- Transaction pattern library

### 3.1 General merchandise (6.25% state rate)

| Pattern | Taxable? | Rate | Notes |
|---|---|---|---|
| General TPP (electronics, furniture, equipment) | TAXABLE | 6.25% + local | 35 ILCS 120/2-10 |
| Clothing and footwear | TAXABLE | 6.25% + local | NO clothing exemption |
| Prepared food (hot, with utensils) | TAXABLE | 6.25% + local | Full rate |
| Candy (no flour, sugar primary ingredient) | TAXABLE | 6.25% + local | NOT qualifying food |
| Soft drinks | TAXABLE | 6.25% + local | NOT qualifying food |
| Alcoholic beverages | TAXABLE | 6.25% + local | |

### 3.2 Reduced rate items (1% state rate)

| Pattern | Rate | Citation |
|---|---|---|
| Grocery food (qualifying, for human consumption, off-premises) | 1% + local | 35 ILCS 120/2-10 |
| Prescription drugs | 1% + local | 35 ILCS 120/2-10 |
| Nonprescription drugs (OTC) | 1% + local | 35 ILCS 120/2-10 |
| Medical appliances (prescribed) | 1% + local | 35 ILCS 120/2-10 |

**CRITICAL: Granola bars with flour = 1% (food). Pure chocolate bar without flour = 6.25% (candy).**

### 3.3 SaaS and digital goods

| Pattern | Taxable? | Notes |
|---|---|---|
| Canned software (physical media) | TAXABLE | TPP at 6.25% |
| Canned software (electronic download) | TAXABLE | 86 Ill. Admin. Code 130.1935 |
| Custom software (any delivery) | NOT TAXABLE | Service, not TPP |
| SaaS (cloud-hosted, no download) | NOT TAXABLE | IDOR Gen. Info. Letter ST 15-0015 |
| Digital music/movies/books (permanent download) | TAXABLE | TPP |
| Streaming (no download/no possession) | NOT TAXABLE | No transfer of TPP |

### 3.4 Services (SOT applies to TPP component only)

| Pattern | SOT on TPP? | Notes |
|---|---|---|
| Auto mechanic (parts + labor) | Yes (parts only) | Parts taxed; labor not taxed |
| Contractor (materials + labor) | Yes (materials only) | Materials taxed |
| Attorney / consultant | No | No TPP transferred |
| Hair salon (sells shampoo) | Yes (shampoo) | TPP sold at retail |

### 3.5 Exemptions

| Pattern | Status | Citation |
|---|---|---|
| Farm equipment and chemicals | EXEMPT | 35 ILCS 120/2-5(2) |
| Manufacturing machinery/equipment (primarily in manufacturing) | EXEMPT | 35 ILCS 120/2-5(14) |
| Resale (CRT-61) | EXEMPT | 35 ILCS 120/2-5(39) |
| Interstate commerce | EXEMPT | 35 ILCS 120/2-5(1) |
| Government purchases | EXEMPT | 35 ILCS 120/2-5(11)(12) |
| Newspapers/magazines | EXEMPT | 35 ILCS 120/2-5(6) |
| Pollution control equipment | EXEMPT | 35 ILCS 120/2-5(16) |
| Gasoline | Separate motor fuel tax | 35 ILCS 120/2-5(5) |

---

## Section 4 -- Rate lookup

### 4.1 Key combined rates

| Jurisdiction | General rate | Food/drug rate |
|---|---|---|
| Chicago (Cook County) | ~10.25% | ~2.00% |
| Springfield | ~9.00% | Varies |
| Suburban Cook County | ~9.00-10.25% | Varies |
| Downstate counties | ~6.25-8.75% | Varies |

### 4.2 Sourcing

| Scenario | Rate applied |
|---|---|
| Intrastate sales | Generally origin-based (seller's location) |
| Remote sellers | Destination-based (buyer's location) |
| Home rule taxes | May have different sourcing |

---

## Section 5 -- Classification rules

### 5.1 Four-tax system

| Tax | Statute | Imposed on | Collected from |
|---|---|---|---|
| Retailers' Occupation Tax (ROT) | 35 ILCS 120 | Retailers on gross receipts | Passed to customers |
| Use Tax | 35 ILCS 105 | Purchasers on out-of-state TPP | Purchasers or retailer collects |
| Service Occupation Tax (SOT) | 35 ILCS 110 | Service providers transferring TPP | Passed to customers |
| Service Use Tax | 35 ILCS 115 | Purchasers of services with TPP | Purchasers |

### 5.2 SOT calculation methods

| Method | Calculation |
|---|---|
| Cost price | Tax on cost of materials/parts transferred |
| 50% election | Tax on 50% of entire bill |
| Separately stated | Tax on materials/parts amount only |

### 5.3 Candy vs. food (flour test)

Items containing flour = FOOD (1%). Items without flour but with sugar/sweetener as primary = CANDY (6.25%).

---

## Section 6 -- Return form and filing

### 6.1 Forms

| Form | Use |
|---|---|
| ST-1 | Primary return (covers all four taxes) |
| ST-2 | Multiple site form |
| CRT-61 | Certificate of resale |
| ST-587 | Exemption certificates (manufacturing, agriculture, etc.) |

### 6.2 Due dates

| Frequency | Due date |
|---|---|
| Monthly | 20th of following month |
| Quarterly | Apr 30, Jul 31, Oct 31, Jan 31 |
| Annual | January 31 |

---

## Section 7 -- Thresholds, penalties, and deadlines

### 7.1 Economic nexus

| Parameter | Value |
|---|---|
| Revenue threshold | $100,000 in gross receipts |
| Transaction threshold | 200 transactions |
| Test type | OR -- either triggers nexus |
| Measurement period | Preceding 12 months |
| Effective date | October 1, 2018 |
| Authority | 35 ILCS 105/2 |

### 7.2 Marketplace facilitator

| Rule | Detail |
|---|---|
| Effective date | January 1, 2020 |
| Facilitators treated as | Retailers for ROT/Use Tax |

### 7.3 Penalties

| Penalty | Rate |
|---|---|
| Late filing/payment | 2%/month (max 25%) |
| Negligence | 20% of deficiency |
| Fraud | 50% of deficiency |

### 7.4 Record retention

4 years from filing or due date.

### 7.5 Statute of limitations

| Scenario | Period |
|---|---|
| Standard | 3.5 years |
| No return | Unlimited |
| Fraud | Unlimited |

---

## Section 8 -- Edge cases

### EC1 -- Grocery food reduced rate

**Situation:** Grocery store sells both hot prepared food and cold items.
**Resolution:** Cold grocery items at 1%. Hot prepared food at 6.25%. Each classified separately.

### EC2 -- Auto repair SOT

**Situation:** Mechanic charges $500 labor + $300 parts.
**Resolution:** SOT on parts ($300) at 6.25% + local. Labor ($500) NOT taxable if separately stated.

### EC3 -- Candy flour test

**Situation:** Chocolate bar (no flour) $3 vs. granola bar (with flour) $3.
**Resolution:** Chocolate = 6.25% (candy). Granola bar = 1% (food).

### EC4 -- SaaS vs. downloaded software

**Situation:** Software partly cloud, partly downloaded.
**Resolution:** Downloaded component taxable. Pure cloud access not taxable. Hybrid requires analysis.

### EC5 -- Chicago streaming tax

**Situation:** Chicago resident subscribes to Netflix.
**Resolution:** 9% Chicago amusement tax applies. Separate municipal tax, not state ROT.

---

## Section 9 -- Test suite

### Test 1 -- General merchandise in Chicago

**Input:** $500 laptop. Chicago rate: 10.25%.
**Expected:** Tax = $51.25.

### Test 2 -- Grocery food reduced rate

**Input:** $100 groceries. Chicago food rate: ~2%.
**Expected:** Tax = ~$2.00. Food taxed at reduced rate, NOT exempt.

### Test 3 -- Prepared food full rate

**Input:** $15 hot sandwich in Springfield. Rate: ~9%.
**Expected:** Tax = $1.35.

### Test 4 -- SaaS not taxable

**Input:** $200/month cloud CRM. No download.
**Expected:** Not taxable.

### Test 5 -- Economic nexus (revenue)

**Input:** $110K IL sales, 50 transactions.
**Expected:** Has nexus. Revenue exceeds $100K (OR test).

### Test 6 -- Economic nexus (transactions)

**Input:** $50K IL sales, 250 transactions.
**Expected:** Has nexus. Transactions exceed 200 (OR test).

### Test 7 -- Auto repair SOT

**Input:** $400 labor + $200 parts. Rate: 8.25%.
**Expected:** Tax on parts = $16.50. Tax on labor = $0.

### Test 8 -- Candy vs. food

**Input:** Chocolate bar $3, granola bar $3. Chicago rates.
**Expected:** Chocolate at ~10.25%. Granola at ~2%.

### Test 9 -- Vendor discount

**Input:** $5,000 ROT due, filed on time.
**Expected:** Discount = $87.50. Net = $4,912.50.

### Test 10 -- Use tax

**Input:** $2,000 supplies from Oregon. Springfield rate: ~9%.
**Expected:** Use tax = $180.

---

## Section 10 -- Prohibitions

- NEVER say Illinois exempts grocery food -- it taxes food at a REDUCED 1% rate.
- NEVER forget Illinois has FOUR separate taxes (ROT, Use Tax, SOT, Service Use Tax).
- NEVER apply a clothing exemption -- clothing is fully taxable at 6.25%.
- NEVER assume all services are taxable -- SOT applies only to the TPP component.
- NEVER treat SaaS as taxable if purely cloud-based with no download.
- NEVER confuse candy (no flour = 6.25%) with food (flour = 1%).
- NEVER ignore home rule taxes -- significant additional rates possible.
- NEVER use destination-based sourcing for intrastate Illinois sales.
- NEVER accept SST certificates -- IL is not an SST member.
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude.

---

## Disclaimer

This skill is provided for informational and computational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional (CPA, EA, or tax attorney) before filing.
