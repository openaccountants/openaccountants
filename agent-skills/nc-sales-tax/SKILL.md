---
name: nc-sales-tax
description: "North Carolina sales and use tax for 2026, for sellers and buyers. Covers the 4.75% general state rate (G.S. 105-164.4), county and transit rates giving combined rates of 6.75% to 8.25% from July 1, 2026 (Mecklenburg County rose 1 point to 8.25%), the 2% local-only rate on qualifying food, the boat and aircraft caps, remote seller and marketplace facilitator nexus at more than $100,000 of NC sales in the current or prior calendar year (G.S. 105-164.8(b)(9), (10); there is no transaction count test), registration, Form E-500 filing frequency (quarterly under $100 a month, monthly from $100, prepayment from $20,000) and consumer use tax. Trigger on \"North Carolina sales tax\", \"NC sales tax\", \"NC use tax\", \"Form E-500\", \"NC economic nexus\", \"Mecklenburg sales tax\", \"N.C.G.S. 105-164\". Load us-sales-tax first for the general method."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nc-sales-tax"
  jurisdiction: "US-NC"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# North Carolina sales and use tax, 2026

> **Source-cited draft.** Built from G.S. 105-164.4, 105-164.8, 105-164.13 and 105-164.16, and the NCDOR pages on current sales and use tax rates, food, the Mecklenburg County increase and registration, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** North Carolina's general state sales tax rate is **4.75%**. Every county adds local tax, and some add transit tax, so from **July 1, 2026** the combined general rate is **6.75%, 7%, 7.25% (Wake), 7.5% (Durham, Orange) or 8.25% (Mecklenburg)**. Qualifying food is taxed at a **2% local rate only**. A seller outside NC must register and collect once its NC sales exceed **$100,000** in the current or previous calendar year; there is no 200-transaction test. Returns are on Form E-500: quarterly if the tax is consistently under $100 a month, monthly (due the 20th) from $100.

## Scope and who this is for

In scope: a business selling tangible personal property, certain digital property or taxable services into or within North Carolina in 2026; a remote seller or marketplace facilitator testing nexus; a business or individual owing consumer use tax.

Out of scope, and where it goes:

| Topic | Skill |
| --- | --- |
| General US sales tax method, sourcing and exemption certificates | `us-sales-tax` |
| Nexus thresholds in other states | `us-sales-tax-nexus-50-state-matrix` |
| Use tax entered on the individual return (D-400 line 18) | `nc-income-tax` |
| Prepared meals taxes set by local governments, occupancy taxes, the 7% combined rate on telecommunications, video programming, electricity and piped gas | not covered; refer |

## Ask the client first

1. **What is sold** (goods, digital products, software, repair or installation services, food, boats or aircraft)? That decides taxable or not and the rate.
2. **Where it is delivered or received in NC** (county). The county sets the local and transit rate.
3. **NC gross sales in 2025 and so far in 2026**, and whether sales go through a marketplace. That decides the remote seller obligation.
4. **Is the seller already registered** with NCDOR, and on what filing frequency?
5. **Average monthly NC sales and use tax** the business collects: under $100, $100 to $20,000, or over $20,000.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| General state rate | 4.75% | [G.S. 105-164.4(a)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.4.html) |
| Combined general rate, most counties (state plus local) | 6.75% or 7% | [NCDOR current rates, effective July 1, 2026](https://www.ncdor.gov/taxes-forms/sales-and-use-tax/sales-and-use-tax-rates/current-sales-and-use-tax-rates) |
| Combined general rate, Wake County | 7.25% | [NCDOR current rates](https://www.ncdor.gov/taxes-forms/sales-and-use-tax/sales-and-use-tax-rates/current-sales-and-use-tax-rates) |
| Combined general rate, Durham and Orange counties | 7.5% | [NCDOR current rates](https://www.ncdor.gov/taxes-forms/sales-and-use-tax/sales-and-use-tax-rates/current-sales-and-use-tax-rates) |
| Combined general rate, Mecklenburg County, from July 1, 2026 (an extra 1% local tax) | 8.25% | [NCDOR current rates](https://www.ncdor.gov/taxes-forms/sales-and-use-tax/sales-and-use-tax-rates/current-sales-and-use-tax-rates); [NCDOR Mecklenburg notice](https://www.ncdor.gov/taxes-forms/sales-and-use-tax/other-sales-and-use-tax-resources/important-notices-issued-sales-and-use-tax-division/important-notice-mecklenburg-county-sales-and-use-tax-increase) |
| Qualifying food (local rate only; state and transit rates do not apply) | 2% | [NCDOR food page](https://www.ncdor.gov/taxes-forms/sales-and-use-tax/food-non-qualifying-food-and-prepaid-meal-plans) |
| Boats: state rate, maximum per article | 3%, $1,500 | [G.S. 105-164.4(a)(1b)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.4.html) |
| Aircraft: general rate, maximum per article | $2,500 | [G.S. 105-164.4(a)(1a)c](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.4.html) |
| Remote seller nexus: NC gross sales, previous or current calendar year, more than | $100,000 | [G.S. 105-164.8(b)(9)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.8.html) |
| Marketplace facilitator nexus: NC gross sales including facilitated sales, more than | $100,000 | [G.S. 105-164.8(b)(10)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.8.html) |
| Referral (click-through) presumption: receipts from NC customers referred by NC persons for a commission, more than | $10,000 | [G.S. 105-164.8(b)(3)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.8.html) |
| Quarterly filing if consistently liable for less than, a month | $100 | [G.S. 105-164.16(b)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.16.html) |
| Monthly filing if consistently liable for at least $100 and less than, a month | $20,000 | [G.S. 105-164.16(b1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.16.html) |
| Prepayment of next month's tax, at least this share, if liable for $20,000 or more a month | 65% | [G.S. 105-164.16(b2)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.16.html) |

The full county list is on the NCDOR current rates page; check it for each delivery address, since local rates change on July 1 or other quarter starts.

### Step 1: is the sale taxable?

Under [G.S. 105-164.4(a)(1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.4.html) the general rate applies to:

- the sales price of **tangible personal property** not taxed elsewhere in the section;
- **certain digital property** (whether bought outright or used under continuing payments), and digital codes for it;
- **repair, maintenance and installation services** to tangible personal property or certain digital property;
- leases and rentals of tangible personal property (at the rate that applies to a sale), accommodation rentals, laundry and dry cleaning, and items sold at a specialty market or other event.

Services not listed in G.S. 105-164.4 are not taxed. Exemptions are in [G.S. 105-164.13](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.13.html), for example prescription drugs ((13)a), custom computer software ((43)), and software for enterprise servers or datacenters ((43a)).

### Step 2: food or non-qualifying food

Qualifying food is all food except candy, soft drinks, prepared food (other than artisan bakery items sold without utensils), dietary supplements, vending machine food and prepaid meal plans. Qualifying food takes the **2% local rate** only, reported on the "2% Food Rate" line of Form E-500. Non-qualifying food takes the general state rate plus local and transit rates ([NCDOR food page](https://www.ncdor.gov/taxes-forms/sales-and-use-tax/food-non-qualifying-food-and-prepaid-meal-plans)).

### Step 3: which rate

Find the county where the buyer receives the item (sourcing under G.S. 105-164.4B) and take the combined rate from the NCDOR table. A retailer that must collect state tax must also collect local use tax where local sales tax does not apply ([G.S. 105-164.8(c)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.8.html)).

### Step 4: does a remote seller have to register?

A retailer with no NC presence is engaged in business in NC if, among other tests, its gross sales from remote sales sourced to NC exceed **$100,000** in the previous or the current calendar year (including sales as a marketplace seller). A marketplace facilitator counts all facilitated sales. When the seller meets only this test, the obligation starts on **the first day of the first calendar month at least 60 days after** sales exceed the threshold ([G.S. 105-164.8(b)(9), (10)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.8.html)). Other presence tests (offices, employees or agents soliciting in NC, the $10,000 referral presumption) start the obligation at once.

### Step 5: register, file and pay

1. Register with NCDOR online (no fee; NCDOR warns against third-party sites that charge one) ([NCDOR registration](https://www.ncdor.gov/taxes-forms/sales-and-use-tax/sales-and-use-tax-registration)).
2. NCDOR assigns the filing frequency and the taxpayer follows it until told otherwise ([G.S. 105-164.16(b3)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.16.html)). All places of business of the same person are added together.
3. File Form E-500 and pay: quarterly by the last day of the month after the quarter; monthly by the 20th of the next month; prepayment filers also pay at least 65% of the next month's liability (based on the current month, the same month last year, or last year's monthly average) on the monthly due date.
4. The return states gross sales, exempt sales by type, and tax due.

### Consumer use tax

A buyer owes use tax on an item bought for use in NC without paying NC tax. An individual's nonbusiness purchases (other than boats and aircraft) are reported once a year on the income tax return, D-400 line 18; an individual not required to file an income tax return files a use tax return by April 15 ([G.S. 105-164.16(d)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.16.html)). Use tax on food bought without tax goes on Form E-554; boats and aircraft on Form E-555 (NCDOR 2025 D-401).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Grocery food (qualifying food) | Not exempt: the 2% local rate applies; state and transit rates do not |
| Candy, soft drinks, prepared food | Full combined general rate |
| Clothing | Taxable at the general rate; no clothing exemption |
| Digital downloads (certain digital property) | Taxable at the general rate |
| Repair, maintenance or installation of goods | Taxable at the general rate |
| Professional services (legal, accounting, consulting) | Not listed in G.S. 105-164.4, so not taxed |
| Custom software, or the separately stated custom part of modified software | Exempt, G.S. 105-164.13(43) |
| Prescription drugs | Exempt, G.S. 105-164.13(13)a |
| Boat | 3% state rate, capped at $1,500 per boat |
| Aircraft or qualified jet engine | General rate, aircraft capped at $2,500 per article |
| Remote seller under $100,000 in both 2025 and 2026 | No obligation from that test alone; check the other presence tests |
| Remote seller crossing $100,000 during 2026 | Collect from the first day of the first month at least 60 days later |
| Sales made only through a marketplace facilitator over the threshold | The facilitator collects on facilitated sales |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Delivery county | Do not guess a local rate; ask for the address |
| Filing frequency | Monthly until NCDOR's assignment is seen |
| Whether a food item is qualifying | Treat as non-qualifying until the item is checked against the NCDOR list |

## Worked cases

### Case 1: a taxable sale in Mecklenburg County, before and after July 1, 2026

A $1,000 sale of furniture delivered in Charlotte on 15 August 2026 bears 8.25%: $82.50, of which $47.50 is the 4.75% state tax and $35.00 is local and transit tax. The same sale delivered on 15 June 2026 bore 7.25%, $72.50 (the 1% Mecklenburg increase started July 1). A $200 grocery order of qualifying food in August bears only the 2% local rate, $4.00.

```oa-check
name: NC Mecklenburg sale before and after the July 2026 increase
inputs:
  price: 1000
  state_rate: 0.0475
  combined_after: 0.0825
  increase: 0.01
  food: 200
  food_rate: 0.02
steps:
  - tax_after: price * combined_after
  - state_part: price * state_rate
  - local_part: tax_after - state_part
  - tax_before: price * (combined_after - increase)
  - food_tax: food * food_rate
expected:
  tax_after: 82.50
  state_part: 47.50
  local_part: 35.00
  tax_before: 72.50
  food_tax: 4.00
```

### Case 2: must a remote seller register for 2026, and how often will it file?

An online seller with no NC presence sold $95,000 into NC in 2025 and passes $100,000 of NC sales on 10 March 2026. 2025 did not exceed $100,000, but 2026 does, so the seller must collect from **1 May 2026** (the first month starting at least 60 days after 10 March). Its NC sales for the rest of 2026 run at $12,000 a month at an average 7% combined rate: $840 of tax a month, which is between $100 and $20,000, so it files Form E-500 monthly, by the 20th of each following month.

```oa-check
name: NC remote seller threshold and filing frequency
inputs:
  sales_2025: 95000
  sales_2026: 101000
  threshold: 100000
  monthly_sales: 12000
  avg_rate: 0.07
steps:
  - over_2025: min(max(sales_2025 - threshold, 0), 1)
  - over_2026: min(max(sales_2026 - threshold, 0), 1)
  - must_collect: max(over_2025, over_2026)
  - monthly_tax: monthly_sales * avg_rate
  - monthly_filer: min(max(monthly_tax - 99.99, 0), 1) * min(max(20000 - monthly_tax, 0), 1)
expected:
  over_2025: 0
  over_2026: 1
  must_collect: 1
  monthly_tax: 840
  monthly_filer: 1
```

## When to refuse or refer

| Situation | Action |
| --- | --- |
| Software sold for remote access (SaaS) or bundled with services | Refer; this rewrite did not confirm the treatment (v2.0 said "not taxable", unsupported) |
| Manufacturing machinery, the mill machinery privilege tax, or refunds for manufacturers | Refer |
| Telecommunications, video programming, electricity, piped natural gas (7% combined general rate) | Refer |
| Construction contracts, real property contractors | Refer |
| Accommodation rentals and local occupancy taxes | Refer |
| An NCDOR audit or assessment | Refer to a reviewer |

## Filing and payment

| Obligation | When | Source |
| --- | --- | --- |
| Register before making taxable sales (no fee) | Before the first sale; remote sellers by the start date in Step 4 | [NCDOR registration](https://www.ncdor.gov/taxes-forms/sales-and-use-tax/sales-and-use-tax-registration) |
| Form E-500, quarterly filer | Last day of the month after the quarter | [G.S. 105-164.16(b)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.16.html) |
| Form E-500, monthly filer | 20th day of the following month | [G.S. 105-164.16(b1)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.16.html) |
| Prepayment ($20,000 or more a month) | With the monthly return | [G.S. 105-164.16(b2)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.16.html) |
| Late filing / late payment | 5% a month up to 25%; 5% of the tax | [G.S. 105-236(a)(3), (4)](https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-236.html) |

## Completion checklist

- [ ] Each product classified: taxable, qualifying food, exempt, or capped
- [ ] Rate taken from the NCDOR county table for the delivery date (July 1, 2026 change checked)
- [ ] Remote seller test run for 2025 and 2026, start date computed
- [ ] Registration in place; filing frequency matches the NCDOR assignment
- [ ] Use tax on untaxed purchases reported

## Sources

| Source | URL | Read for | Read on |
| --- | --- | --- | --- |
| G.S. 105-164.4 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.4.html | Read for the 4.75% rate, what is taxed, boat and aircraft caps | 2026-11-13 |
| G.S. 105-164.8 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.8.html | Read for remote seller, marketplace and referral nexus | 2026-11-13 |
| G.S. 105-164.13 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.13.html | Read for software and prescription drug exemptions | 2026-11-13 |
| G.S. 105-164.16 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-164.16.html | Read for filing frequency, prepayment and individual use tax | 2026-11-13 |
| G.S. 105-236 | https://www.ncleg.gov/EnactedLegislation/Statutes/HTML/BySection/Chapter_105/GS_105-236.html | Read for penalties | 2026-11-13 |
| NCDOR current sales and use tax rates | https://www.ncdor.gov/taxes-forms/sales-and-use-tax/sales-and-use-tax-rates/current-sales-and-use-tax-rates | Read for county combined rates from July 1, 2026 | 2026-11-13 |
| NCDOR Mecklenburg County notice | https://www.ncdor.gov/taxes-forms/sales-and-use-tax/other-sales-and-use-tax-resources/important-notices-issued-sales-and-use-tax-division/important-notice-mecklenburg-county-sales-and-use-tax-increase | Read for the extra 1% from July 1, 2026 | 2026-11-13 |
| NCDOR food, non-qualifying food and prepaid meal plans | https://www.ncdor.gov/taxes-forms/sales-and-use-tax/food-non-qualifying-food-and-prepaid-meal-plans | Read for the 2% food rate and what is qualifying food | 2026-11-13 |
| NCDOR sales and use tax registration | https://www.ncdor.gov/taxes-forms/sales-and-use-tax/sales-and-use-tax-registration | Read for registration with no fee | 2026-11-13 |
| NCDOR 2025 D-401 instructions | https://www.ncdor.gov/2025-d-401-individual-income-tax-instructions/open | Read for D-400 line 18 and Forms E-554 and E-555 | 2026-11-13 |

Not yet confirmed: the tax treatment of remotely accessed software (SaaS); NC's Streamlined Sales Tax membership status (v2.0 said "full member", not checked); the exemption certificate form for purchases for resale; the manufacturing machinery treatment (v2.0 said "exempt, refund program", not checked); the local rate split by county beyond the combined rates.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nc-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nc-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
