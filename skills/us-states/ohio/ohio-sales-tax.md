---
name: ohio-sales-tax
description: >
  Use this skill whenever asked about Ohio sales and use tax, ODT filings, Ohio CAT, Ohio exemptions, Ohio nexus, or any request involving Ohio state sales and use tax compliance. Trigger on phrases like "Ohio sales tax", "OH sales tax", "ODT", "UST-1", "Ohio exemption certificate", "Streamlined Sales Tax Ohio", or any request involving Ohio sales and use tax classification, filing, or compliance. ALWAYS read this skill before touching any Ohio sales tax work.
version: 2.0
jurisdiction: US-OH
tax_year: 2025
category: us-states
depends_on:
  - us-sales-tax
---

# Ohio Sales and Use Tax Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| State | Ohio |
| Tax | Sales and Use Tax (state + county) |
| State rate | 5.75% |
| Local rates | County only (0.75% to 2.25%) -- no city or district taxes |
| Maximum combined rate | Approx. 8.00% (e.g. Cuyahoga County) |
| Sourcing | Origin-based (intrastate); destination-based (remote/SST) |
| Primary legislation | ORC Chapters 5739 (Sales) and 5741 (Use) |
| Tax authority | Ohio Department of Taxation (ODT) |
| Filing portal | https://tax.ohio.gov / Ohio Business Gateway |
| Return form | UST-1 (Universal Sales Tax Return) |
| SST member | Yes -- full member |
| Economic nexus | $100,000 gross receipts OR 200 transactions (effective Aug 1, 2019) |
| Vendor license | Required; $25/location/year; renew by February 28 |
| Contributor | Open Accountants Community |
| Validated by | Pending -- requires Ohio CPA or EA sign-off |
| Skill version | 2.0 |

### Key Combined Rates

| County | County Rate | Combined Rate |
|---|---|---|
| Cuyahoga (Cleveland) | 2.25% | 8.00% |
| Franklin (Columbus) | 1.75% | 7.50% |
| Hamilton (Cincinnati) | 1.80% | 7.55% |
| Summit (Akron) | 1.50% | 7.25% |
| Montgomery (Dayton) | 1.50% | 7.25% |
| Lucas (Toledo) | 1.50% | 7.25% |

### Taxability Quick Matrix

| Item | Taxable? | Notes |
|---|---|---|
| Tangible personal property | YES | Default taxable |
| SaaS / cloud software | YES | Taxable as automatic data processing (ORC 5739.01(B)(3)(a)) |
| Grocery food | NO | Exempt (but candy without flour, soft drinks, dietary supplements are taxable) |
| Clothing | YES | Fully taxable -- no clothing exemption |
| General services | NO | Most services exempt unless specifically enumerated |
| Employment/staffing services | YES | ORC 5739.01(B)(3)(j) |
| Landscaping/lawn care | YES | ORC 5739.01(B)(3)(h) |
| Physical fitness services | YES | ORC 5739.01(B)(3)(k) |
| Digital products (audio, video, books) | YES | ORC 5739.01(BBB) |
| Manufacturing equipment | NO | Exempt with STEC-B certificate |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Product taxability unknown | Taxable |
| Service taxability unknown | Exempt (unless enumerated) |
| Sourcing location unknown | Seller's county (origin-based intrastate) |
| Candy vs food unclear | Food (exempt) if contains flour |
| CAT obligation | Escalate -- separate tax |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Confirmation of Ohio nexus (physical or economic), vendor license status, filing frequency, and list of products/services sold.

**Recommended:** Sales by county, exemption certificates on file, prior period UST-1.

**Ideal:** Complete transaction log with ship-to addresses, exemption certificate register, CAT filing status.

### Refusal Catalogue

**R-OH-1 -- CAT questions.** "The Commercial Activity Tax (CAT) is a separate tax on gross receipts. CAT compliance is outside this skill scope. Escalate."

**R-OH-2 -- Audit defense.** "Responding to ODT audits or assessments requires specialist representation. Escalate."

**R-OH-3 -- Complex bundled transactions.** "Mixed transactions involving taxable and exempt components require specialist analysis. Escalate."

---

## Section 3 -- Transaction Pattern Library

### 3.1 Taxable Sales

| Pattern | Treatment | Notes |
|---|---|---|
| Electronics / hardware sale | Taxable at combined rate | TPP |
| SaaS subscription / cloud CRM | Taxable | Automatic data processing |
| Staffing / temp agency | Taxable | Employment services |
| Landscaping invoice | Taxable | ORC 5739.01(B)(3)(h) |
| Gym membership | Taxable | Physical fitness service |
| Digital download (movie, music, ebook) | Taxable | Specified digital products |
| Furniture / office equipment | Taxable | TPP |

### 3.2 Exempt Sales

| Pattern | Treatment | Notes |
|---|---|---|
| Grocery food (bread, milk, produce) | Exempt | Not candy, soft drinks, supplements |
| Manufacturing equipment with STEC-B | Exempt | Must have valid certificate |
| Sale to government entity | Exempt | With proper documentation |
| Resale with valid certificate | Exempt | STEC-B or SST Certificate |
| Medical equipment (certain) | Exempt | Check specific exemption |

### 3.3 Candy/Food Classification (SST Standard)

| Item | Classification | Rationale |
|---|---|---|
| Chocolate bar (no flour) | Candy -- TAXABLE | No flour ingredient |
| Chocolate-covered pretzels | Food -- EXEMPT | Contains flour |
| Soft drinks | TAXABLE | Specifically enumerated |
| Dietary supplements | TAXABLE | Specifically enumerated |
| Fresh produce | EXEMPT | Grocery food |

---

## Section 4 -- Worked Examples

### Example 1 -- Basic Taxable Sale in Columbus

**Input:** Retailer in Columbus (Franklin County) sells electronics for $800. Combined rate: 7.50%.

**Reasoning:** Electronics are TPP, taxable. Columbus is Franklin County: 5.75% state + 1.75% county = 7.50%.

**Classification:** Sales tax = $60.00. Total = $860.00.

### Example 2 -- SaaS Subscription in Cuyahoga County

**Input:** Ohio business subscribes to cloud-based CRM. $300/month. Business in Cuyahoga County (8.00%).

**Reasoning:** SaaS is taxable as automatic data processing service in Ohio.

**Classification:** Sales tax = $24.00/month.

### Example 3 -- Vendor Discount

**Input:** Vendor timely files and pays $20,000 in Ohio sales tax.

**Reasoning:** Ohio offers 0.75% vendor discount for timely filing and payment. No cap.

**Classification:** Discount = $150.00. Net remittance = $19,850.00.

### Example 4 -- Origin-Based Intrastate Sourcing

**Input:** Columbus-based seller ships goods to customer in Cleveland (Cuyahoga County).

**Reasoning:** Intrastate Ohio sales use origin-based sourcing. Seller charges Franklin County rate (7.50%), not Cuyahoga (8.00%).

**Classification:** Rate = 7.50% (seller's county).

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Rate Structure

State rate: 5.75%. County permissive taxes: 0.75% to 2.25%. No city or special district taxes.

### 5.2 Sourcing (ORC 5739.033)

Origin-based for intrastate (both seller and buyer in Ohio). Destination-based for remote sellers (SST compliant).

### 5.3 Filing (ORC 5739.12)

| Frequency | Criteria | Due Date |
|---|---|---|
| Monthly | Tax liability > $600/month | 23rd of following month |
| Semi-annual | Tax liability $600 or less/month | July 23 / January 23 |

### 5.4 Vendor Discount

0.75% of tax collected for timely filing and payment. No cap. ORC 5739.12(B).

### 5.5 Economic Nexus (ORC 5741.01(I)(2))

$100,000 gross receipts OR 200 transactions in current or preceding calendar year. Effective August 1, 2019.

### 5.6 Marketplace Facilitator (ORC 5739.01(Q))

Required to collect and remit. Effective January 1, 2020. Marketplace sellers relieved for facilitated sales.

### 5.7 Exemption Certificates

STEC-B (blanket), STEC-U (unit), STEC-CO (construction). Ohio accepts SST Certificate and MTC Uniform Certificate.

### 5.8 Use Tax

Applies when Ohio purchaser acquires TPP/services without Ohio tax collected. Rate = combined state + county at location of use. Report on UST-1 (vendors) or IT-1040 (individuals).

### 5.9 Penalties (ORC 5739.13)

| Penalty | Rate |
|---|---|
| Late filing/payment | Greater of 10% of tax due or $50 |
| Fraud | 50% of deficiency |
| Interest | Federal short-term rate + 5% |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Data Processing vs Consulting

Cloud analytics may be taxable as automatic data processing. However, consulting services using technology incidentally may not qualify. Flag for reviewer.

### 6.2 CAT Interaction

Ohio imposes BOTH sales tax (customer-collected) and CAT (seller's gross receipts). They are separate. Escalate CAT questions.

### 6.3 Complex Bundled Transactions

When taxable and exempt items are sold together, bundling rules determine treatment. Flag for reviewer.

---

## Section 7 -- Working Paper Template

```
OHIO SALES TAX WORKING PAPER (UST-1)
Business: _______________  Vendor License: ___________
Period: ___________  Filing Frequency: Monthly / Semi-Annual

A. GROSS SALES
  A1. Total gross sales                          ___________
  A2. Exempt sales (with certificates)           ___________
  A3. Taxable sales (A1 - A2)                   ___________

B. TAX COMPUTATION
  B1. State tax (A3 x 5.75%)                    ___________
  B2. County tax (A3 x county rate ___%)         ___________
  B3. Total tax collected                        ___________

C. VENDOR DISCOUNT
  C1. Discount (B3 x 0.75% if timely)           ___________
  C2. Net remittance (B3 - C1)                  ___________

D. USE TAX
  D1. Purchases without Ohio tax                 ___________
  D2. Use tax due                                ___________

REVIEWER FLAGS:
  [ ] Vendor license current (renewed by Feb 28)?
  [ ] Origin-based sourcing applied for intrastate?
  [ ] SST/MTC certificates accepted?
  [ ] Candy/food classification verified?
  [ ] CAT obligation flagged separately?
```

---

## Section 8 -- Bank Statement Reading Guide

### Common Ohio Business Narrations

| Narration | Meaning | Classification Hint |
|---|---|---|
| ODT / OHIO DEPT OF TAXATION | Tax payment | Exclude |
| AMAZON / ETSY / SHOPIFY | Marketplace settlement | Check if facilitator collected |
| SQUARE / STRIPE / PAYPAL | Payment processor | Business income |
| OHIO BWC | Workers comp | Exclude |

---

## Section 9 -- Onboarding Fallback

Present these questions:

```
ONBOARDING QUESTIONS -- OHIO SALES TAX
1. Do you have an Ohio vendor license? License number?
2. What is your filing frequency (monthly / semi-annual)?
3. What is your nexus type (physical, economic, or both)?
4. Are you a marketplace seller?
5. What types of products or services do you sell in Ohio?
6. Do you sell to exempt entities?
7. Do you have locations, employees, or inventory in Ohio?
8. Which Ohio counties do you sell into?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| Sales tax imposition | ORC 5739.02 |
| Use tax | ORC Chapter 5741 |
| Sourcing | ORC 5739.033 |
| Vendor license | ORC 5739.17 |
| Economic nexus | ORC 5741.01(I)(2) |
| Marketplace facilitator | ORC 5739.01(Q) |
| Vendor discount | ORC 5739.12(B) |
| Penalties | ORC 5739.13 |
| CAT (separate) | ORC Chapter 5751 |

### Known Gaps / Out of Scope

- Commercial Activity Tax (CAT)
- Audit defense
- Complex bundled transactions
- ODT private letter rulings

### Changelog

| Version | Date | Change |
|---|---|---|
| 2.0 | April 2026 | Full rewrite to v2.0 10-section structure; taxability matrix; worked examples; origin-based sourcing detail |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Vendor license current?
- [ ] Correct sourcing applied (origin intrastate, destination remote)?
- [ ] Candy/food distinction applied correctly?
- [ ] SaaS classified as taxable?
- [ ] Vendor discount applied if timely?
- [ ] CAT flagged as separate obligation?

---

## PROHIBITIONS

- NEVER apply a clothing exemption in Ohio -- clothing is fully taxable
- NEVER forget that Ohio's vendor license must be renewed annually ($25/location/year)
- NEVER treat grocery food as taxable -- grocery food is exempt (but candy, soft drinks, dietary supplements are taxable)
- NEVER confuse the CAT with sales tax -- they are separate taxes
- NEVER use destination-based sourcing for intrastate Ohio sales -- Ohio is origin-based for intrastate
- NEVER forget the 0.75% vendor discount for timely filing -- no cap
- NEVER treat SaaS as nontaxable -- SaaS is taxable as automatic data processing
- NEVER refuse SST Certificate -- Ohio is an SST member
- NEVER present calculations as definitive -- always label as estimated and direct client to a qualified Ohio CPA or EA

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, or tax attorney) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
