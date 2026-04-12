---
name: arizona-sales-tax
description: Use this skill whenever asked about Arizona sales tax, Arizona Transaction Privilege Tax (TPT), Arizona use tax, Arizona tax nexus, or any request involving Arizona state-level consumption taxes. Trigger on phrases like "Arizona sales tax", "AZ sales tax", "TPT", "Transaction Privilege Tax", "Arizona DOR", or any request involving Arizona TPT compliance. CRITICAL -- Arizona has a Transaction Privilege Tax on the SELLER, not a traditional sales tax. ALWAYS load us-sales-tax first.
version: 2.0
---

# Arizona Transaction Privilege Tax (TPT) Skill v2.0

## Section 1 -- Quick reference

| Field | Value |
|---|---|
| Jurisdiction | Arizona, United States |
| Jurisdiction code | US-AZ |
| Tax type | Transaction Privilege Tax (TPT) -- NOT a traditional sales tax; tax is on the SELLER |
| State TPT rate | 5.6% (retail classification) |
| Local add-on range | 0% -- 5.6% (city + county) |
| Maximum combined rate | ~11.2% |
| Sourcing | Origin-based for most TPT classifications |
| Economic nexus | $100,000 in gross proceeds or gross income (revenue only) |
| Primary legislation | A.R.S. Title 42, Chapter 5 |
| Tax authority | Arizona Department of Revenue (ADOR) |
| Filing portal | https://www.aztaxes.gov |
| SST member | No |
| Federal framework skill | us-sales-tax |
| Skill version | 2.0 |

**CRITICAL: Arizona TPT is a tax on the privilege of doing business in Arizona, imposed on the SELLER. It is NOT a sales tax on the buyer, though sellers typically pass it through.**

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

| # | Question | Why it matters |
|---|----------|----------------|
| 1 | Arizona TPT license number? | Required for filing |
| 2 | Filing frequency? | Monthly, quarterly, annual |
| 3 | Nexus type? | $100K threshold |
| 4 | Business classification? | Different TPT rates by classification |
| 5 | Contractor? | Prime contracting has special 65/35 split rules |
| 6 | Sell into multiple cities? | City TPT rates vary significantly |

### Refusal catalogue

**R-AZ-1 -- Prime contracting classification.** 65/35 split between real property and materials is complex. Escalate.

---

## Section 3 -- Transaction pattern library

### 3.1 Retail classification (5.6% state)

| Pattern | Taxable? | Notes |
|---|---|---|
| General TPP | TAXABLE | Retail classification |
| Clothing | TAXABLE | No exemption |
| Grocery food (unprepared) | EXEMPT | A.R.S. §42-5061(A)(1) |
| Prepared food | TAXABLE | |

### 3.2 SaaS and digital goods

| Pattern | Taxable? | Notes |
|---|---|---|
| Canned software (physical or download) | TAXABLE | TPP |
| SaaS (cloud-hosted) | TAXABLE | Arizona treats SaaS as taxable |
| Digital goods | TAXABLE | |

### 3.3 Services

| Pattern | Taxable? | Notes |
|---|---|---|
| Professional services | NOT TAXABLE | |
| Job printing | TAXABLE | Separate classification |
| Restaurants/bars | TAXABLE | Restaurant classification |
| Transient lodging | TAXABLE | Transient lodging classification |
| Personal property rental | TAXABLE | Rental classification |
| Prime contracting | TAXABLE | 65/35 rule applies |

### 3.4 Exemptions

| Pattern | Status |
|---|---|
| Grocery food | EXEMPT |
| Prescription drugs | EXEMPT |
| Manufacturing machinery (directly in manufacturing) | EXEMPT |
| Resale | EXEMPT |
| Interstate commerce | EXEMPT |

---

## Section 4 -- Rate lookup

### 4.1 TPT classifications and state rates

| Classification | State rate |
|---|---|
| Retail | 5.6% |
| Mining | 3.125% |
| Utilities | 5.6% |
| Telecommunications | 5.6% |
| Transient lodging | 5.5% |
| Restaurants/bars | 5.6% |
| Contracting (prime) | 5.6% |
| Rental of TPP | 5.6% |

---

## Section 5 -- Classification rules

### 5.1 TPT is on the seller

TPT is a privilege tax on the seller for conducting business. The buyer is NOT legally liable. Most sellers pass the amount through to buyers.

### 5.2 Model City Tax Code

Arizona cities adopt the Model City Tax Code with local modifications. City rates and exemptions can vary significantly.

---

## Section 6 -- Return form and filing

Filed via AZTaxes.gov. Single return covers state + county + city TPT.

---

## Section 7 -- Thresholds, penalties, and deadlines

### 7.1 Economic nexus

| Parameter | Value |
|---|---|
| Threshold | $100,000 in gross proceeds or gross income |
| Transaction count | None |
| Effective date | October 1, 2019 |

---

## Section 8 -- Edge cases

### EC1 -- Prime contracting

**Situation:** Contractor builds a house.
**Resolution:** Prime contracting classification. 65% of contract price treated as real property improvement (not taxable); 35% treated as materials (taxable at TPT rate). Complex -- escalate.

---

## Section 9 -- Test suite

### Test 1 -- Retail sale in Phoenix

**Input:** $500 item. Combined rate: ~8.6%.
**Expected:** Tax = ~$43.

### Test 2 -- Grocery food exempt

**Input:** $200 groceries.
**Expected:** Tax = $0. Grocery food exempt in AZ.

---

## Section 10 -- Prohibitions

- NEVER call Arizona's tax a "sales tax" without noting it is a Transaction Privilege Tax on the SELLER.
- NEVER forget that city TPT rates and exemptions can differ from the state.
- NEVER apply destination-based sourcing for most TPT classifications -- Arizona is generally origin-based.
- NEVER treat grocery food as taxable -- it is exempt in Arizona.
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude.

---

## Disclaimer

This skill is provided for informational and computational purposes only and does not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.
