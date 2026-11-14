---
name: vt-sales-tax
description: Use this skill whenever asked about Vermont sales tax, Vermont use tax, Vermont Tax Dept sales tax filing, Vermont local option tax, Vermont SaaS tax, or Vermont sales tax compliance. Trigger on phrases like "Vermont sales tax", "VT sales tax", "32 V.S.A. §9771", "Vermont Tax Dept", "Vermont local option", "Vermont SaaS", "Vermont SST", or any request involving Vermont state and local sales and use tax compliance. ALWAYS load us-sales-tax first for federal context.
jurisdiction: US-VT
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
version: "1.2"
type: computation
category: state-tax
---

# Vermont sales and use tax, tax year 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. General reference for AI-assisted working papers. A qualified professional must review the established facts and filing result. Circular 230 section 10.37: consider all relevant facts and circumstances; do not assume missing facts or base advice on audit risk.

**Answer first.** Vermont's ordinary sales/use rate is 6%, with 1% local option where applicable. Ordinary clothing is exempt, including belts; ordinary T-shirts are not taxable brewery merchandise merely because sold by a brewery. Restaurant meals, alcohol and short-term rooms have separate tax categories. Local municipal meals/rooms taxes require their own check.

## Scope

Vermont retail sales, purchaser use tax, remote sellers and marketplace transactions. Load `us-sales-tax` for the common system. This retains the old skill's meals/rooms, software, agricultural, manufacturing and mixed-business examples without expanding into new tax jobs.

## Ask the client first

1. Registration, assigned filing frequency and active locations.
2. Physical presence, employees/inventory and current rolling sales/transaction totals.
3. Marketplace collection and the seller's own uncollected sales.
4. Product/service details, delivery address and date.
5. Buyer exemption/resale documentation and qualifying business use.
6. Meals/rooms/short-term rental activity and applicable local municipal taxes.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Official source |
| --- | --- | --- |
| General sales/use tax | 6% | [9771](https://legislature.vermont.gov/statutes/section/32/233/09771) |
| Local option sales, meals/rooms/alcohol where adopted | Additional 1%; ordinary sales combined 7%; check municipality and separate municipal taxes | [Department local option](https://tax.vermont.gov/business/local-option-tax) |
| Meals/rooms; alcohol for on-premises consumption | 9%; 10% respectively before any applicable local amount | [9241](https://legislature.vermont.gov/statutes/section/32/225/09241) |
| Short-term rental surcharge, qualifying short-term rental | Additional 3% on top of rooms tax; electronic filing required | [Department meals/rooms](https://tax.vermont.gov/business/meals-and-rooms-tax) |
| Remote-seller economic nexus | At least USD 100,000 OR 200 transactions in the preceding 12-month period | [9701(9)(F)](https://legislature.vermont.gov/statutes/section/32/233/09701) |


### State sales tax rate


- **Vermont state sales tax rate** -- 6.00% percent  _(32 V.S.A. §9771)_
- **State sales tax scope** -- Vermont imposes a state sales tax of 6.00% on the retail sale of tangible personal property and certain services.  _(32 V.S.A. §9771)_

### 1.2 Local Option Tax

- **Local option tax rate** -- 1% percent
- **Local option adoption** -- Not all municipalities have adopted the local option tax.
- **Combined rate where adopted** -- 7.00%  _()_
- **Administration** -- The local option tax is administered by the Vermont Department of Taxes.
- **Local option on meals distinct** -- The local option on meals (9% meals tax + 1% local = 10%) is separate from the general sales tax local option.  _(tax.vermont.gov Local Option Tax page)_
- **Motor vehicles** -- Local option tax does not apply to the sale or rental of motor vehicles subject to the motor vehicle purchase and use tax.

### 1.3 Meals and Alcohol Tax

- **Meals tax** -- 9.00% (Prepared food served in restaurants (not the 6% general rate))  _(32 V.S.A. §9241(b))_
- **Alcoholic beverages served in restaurants/bars** -- 10.00%  _(32 V.S.A. §9241(c))_
- **Alcoholic beverages for off-premises consumption** -- 6% (sales tax)  _()_
- **Local option addition** -- Local option adds 1% where adopted.

### 1.4 Sourcing

- **Sourcing method** -- Vermont uses destination-based sourcing.
- **SST sourcing** -- As an SST member, Vermont follows SSUTA sourcing rules.

### 2.1 Grocery Food -- EXEMPT

- **Unprepared grocery food** -- Exempt.  _(32 V.S.A. §9741(13))_
- **Prepared food (restaurant meals)** -- 9% percent
- **Candy** -- 6% percent
- **Soft drinks** -- 6% percent

### 2.2 Clothing -- EXEMPT

- **Clothing taxability** -- Clothing is exempt from Vermont sales tax, with no price cap.  _(32 V.S.A. §9741(45))_
- **What stays taxable** -- The exemption does not cover clothing accessories or equipment, protective equipment, or sport or recreational equipment; these are taxable at 6% (+ local option where applicable).  _(32 V.S.A. §9741(45))_

### 2.3 Prescription Drugs and Medical

- **Prescription drugs** -- Exempt.  _(32 V.S.A. §9741(2))_
- **OTC drugs** -- Exempt.
- **DME** -- Exempt.
- **Prosthetics** -- Exempt.

### 2.4 Services

Classify the actual supply under [9771](https://legislature.vermont.gov/statutes/section/32/233/09771) and the statutory exemptions. The old blanket service classifications were not substantiated and are listed under Not yet confirmed.

### 2.5 SaaS and Digital Goods -- TAXABLE

- **SaaS taxability** -- Taxable in Vermont. Vermont taxes prewritten software regardless of delivery method, including SaaS and cloud-based software.  _(32 V.S.A. §9701(7))_
- **Canned software (physical and electronic)** -- Taxable.
- **Custom software** -- Classification beyond the statutory prewritten-software definition is reserved under Sources.
- **Digital downloads** -- Taxable as specified digital products.
- **Streaming services** -- Determine whether the actual supply is a taxable programming system or specified digital product under 9771; do not apply a service label alone.

### 2.6 Manufacturing

- **Manufacturing machinery and equipment** -- Exempt when used directly in manufacturing.  _(32 V.S.A. §9741(14))_
- **Fuel and electricity used in manufacturing** -- Exempt for manufacturing portion.

### 2.7 Lodging

- **Rooms/lodging (hotels, B&Bs, vacation rentals)** -- 9.00% (rooms tax)  _(32 V.S.A. §9241(a))_
- **Short-term rental surcharge** -- Short-term rentals also pay a 3% surcharge, and a business paying it must file and pay Meals and Rooms Tax electronically.  _(tax.vermont.gov Meals and Rooms Tax page)_
- **Local option addition on lodging** -- Local option adds 1% where adopted (total = 10%).
- **Short-term rental platforms** -- Short-term rental platforms (Airbnb) must collect as marketplace facilitators.

### 2.8 Agricultural

- **Farm machinery and equipment** -- Exempt when used predominately in farm production for sale.  _(32 V.S.A. §9741(25))_
- **Feed, seed, fertilizer** -- Exempt.  _(32 V.S.A. §9741(3))_
- **Livestock** -- Exempt for breeding/dairy.

### 4.1 Filing Details

**Filing Details**

| Field | Detail |
| --- | --- |
| Return Form | Form SUT-451 (Sales and Use Tax Return) |
| Filing Frequencies | Monthly, quarterly or annual, as assigned by the Department of Taxes (the Department does not publish dollar thresholds on its sales tax page) |
| Due Date | 25 th of the month following the reporting period |
| Portal | https://tax.vermont.gov (myVTax) |
| E-filing | Required for taxpayers with sales subject to local option tax; paper SUT-451 only for a single location with no local option sales |

- **Due date note** -- Vermont's due date is the 25 th, not the 20 th; if it falls on a weekend or holiday it moves to the next business day (for example, the quarter ending 3/31/2026 was due 4/27/2026).  _(tax.vermont.gov Sales and Use Tax page)_

### 4.2 Vendor Discount

- **Vendor discount availability** -- Do not deduct an unconfirmed vendor allowance; the old blanket claim is reserved under Sources.

### 4.3 Penalties and Interest

- **Late filing penalty** -- Under 3202(b)(1),5% of unpaid liability per month/part, maximum 25%, subject to reasonable cause; minimum USD 50 after 60 days. Late payment of sales/use tax is generally 5% monthly/part,maximum 25%, under 3202(b)(3).  _(32 V.S.A. §3202(b)(1))_
- **Interest rate** -- Rate set annually (typically federal short-term rate + specified margin).

### Deductibility and exemptions

Exemptions identified in Step 2 above are the primary deductibility rules for Vermont. Key categories:

- **Resale exemption** -- Valid resale certificate required. Retain for the statutory period.
- **Exempt organizations** -- Government entities and qualifying nonprofits -- require exemption certificate on file.
- **Agricultural exemptions** -- Where applicable per Step 2.
- **Manufacturing exemptions** -- Where applicable per Step 2.
- **Exemption certificate retention** -- Retain the certificate and underlying eligibility evidence; exact timing and retention rules are reserved under Sources.

### 3.1 Economic Nexus Threshold

**Economic Nexus Threshold**  _(32 V.S.A. §9701(9)(F))_

| Field | Detail |
| --- | --- |
| Revenue Threshold | $100,000 in Vermont sales |
| Transaction Threshold | 200 transactions |
| Test | OR (either threshold triggers nexus) |
| Measurement Period | The 12-month period preceding the monthly period for which liability is determined |
| Effective Date | July 1, 2018 |

### 3.2 Marketplace Facilitator

- **Marketplace facilitator obligation** -- Vermont requires marketplace facilitators to collect and remit.  _(32 V.S.A. §9713)_

### 3.3 SST Registration

- **SST registration status** -- Full SST member. SSTRS and CSPs available.

### Filing deadlines and penalties

Refer to Step 3 for filing frequencies and due dates.

### Classification checks

- **Clothing taxation** -- NEVER tax ordinary clothing in Vermont. It is exempt; only accessories, protective equipment and sport or recreational equipment are taxable.
- **Meals rate misapplication** -- NEVER apply the 6% sales tax rate to restaurant meals. Meals are taxed at 9% (meals tax), not 6%.
- **SaaS exemption assumption** -- NEVER assume SaaS is exempt in Vermont. It is taxable.
- **Local option universality assumption** -- NEVER assume all municipalities have the local option tax. Not all have adopted it.
- **Wrong due date** -- NEVER file Vermont returns by the 20 th. The due date is the 25 th.
- **Grocery food taxation** -- NEVER tax grocery food in Vermont. Unprepared food is exempt.
- **Computation** -- Compute only after identifying the taxable base, transaction type and actual delivery jurisdiction.



## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Ordinary belts/T-shirts | Clothing exemption, subject to statutory definition; belt buckles and protective/sports equipment differ |
| Mixed brewery/cafe/resort | Keep each revenue category separate; no single rate for all sales |
| Burlington/Rutland meals/rooms | Separate city-administered taxes must be confirmed, not assumed to be the state's 1% option |
| Specific unverified service classification | Stop classification and refer; legacy list is in Sources |

## Worked cases

The original seven scenarios and eight prose tests below are preserved with corrected clothing classifications. Local meals/alcohol examples use hypothetical jurisdictions with the stated option confirmed, rather than asserting Burlington's separate municipal rates.

### EC 1 -- SaaS Taxable in Vermont

**Situation:** A California SaaS company sells subscriptions to Vermont businesses.

**Resolution:**
- Vermont taxes SaaS at 6% (+ 1% local option where applicable).
- The SaaS company must register if economic nexus is met.
- Tax based on customer's Vermont location.
- **Flag for reviewer:** Vermont is on the list of states that clearly tax SaaS. Multi-state SaaS companies must include VT in their compliance matrix.

### EC 2 -- Meals Tax vs. Sales Tax

**Situation:** A cafe sells both grocery items (bags of coffee beans) and prepared food (espresso drinks). Different rates apply.

**Resolution:**
- Bags of coffee beans: exempt (unprepared food).
- Espresso drinks: 9% meals tax (+ 1% local option where applicable).
- If the cafe also sells mugs or equipment: 6% general sales tax.
- **Flag for reviewer:** Mixed-use establishments must classify each revenue stream correctly.

### EC 3 -- Local Option Tax Variance

**Situation:** A retailer ships to customers in Burlington (local option adopted) and a small town without local option tax.

**Resolution:**
- Burlington: 6% state + 1% local = 7%.
- Small town without local option: 6% only.
- Destination-based sourcing applies. Rate depends on delivery address.
- **Flag for reviewer:** Verify whether the specific municipality has adopted the local option.

### EC 4 -- Clothing Exempt, Accessories Taxable

**Situation:** A Vermont outdoor retailer sells jackets, belts and ski helmets.

**Resolution:**
- Jackets are clothing and exempt.
- Ordinary belts are included as clothing under 9701(24)(A)(vi) and exempt; separately sold belt buckles are accessories and taxable.
- Ski helmets are sport or protective equipment and taxable at 6% (+ local).
- **Flag for reviewer:** Classify each item against the SSUTA definitions of clothing, accessories, protective equipment and sport equipment.

### EC 5 -- Brewery/Taproom Mixed Sales

**Situation:** A Vermont brewery sells: pints of beer consumed on-premises, cans/bottles for off-premises consumption, and merchandise (T-shirts, glasses).

**Resolution:**
- Pints on-premises: 10% alcoholic beverage tax.
- Cans/bottles for off-premises: 6% sales tax.
- Glasses: 6% sales tax; ordinary T-shirts are exempt clothing.
- Local option adds 1% to each category where adopted.
- The brewery must segregate sales by category for tax reporting.
- **Flag for reviewer:** Breweries, wineries, and distilleries face complex multi-rate compliance. Verify all revenue streams.

### EC 6 -- SaaS Company Compliance

**Situation:** A SaaS startup from Vermont sells subscriptions to customers in Vermont and other states.

**Resolution:**
- Vermont sales to VT customers: taxable at 6% (+ local option).
- Out-of-state sales: apply destination state rules (SaaS taxability varies by state).
- The startup must determine which other states tax SaaS and whether economic nexus is met in each.
- **Flag for reviewer:** A Vermont SaaS company must evaluate multi-state SaaS taxability. Vermont taxing SaaS does not mean all states do.

### EC 7 -- Ski Resort Season Pass

**Situation:** A Vermont ski resort sells season passes ($1,200) and single-day lift tickets ($120).

**Resolution:**
- Amusement/entertainment admissions are subject to the 6% sales tax.
- Season passes and lift tickets are taxable at 6% (+ local option).
- Lodging at the resort: 9% rooms tax (+ local option).
- Restaurant meals at the resort: 9% meals tax (+ local option).
- The resort must apply different rates to different revenue streams.
- **Flag for reviewer:** Ski resorts face complex multi-rate compliance across admissions, lodging, meals, and retail.

### Test 1 -- Basic Taxable Sale

**Input:** Seller in Burlington sells $500 of electronics. Combined rate = 7% (6% state + 1% local).
**Expected output:** Tax = $500 x 7% = $35.00. Total = $535.00.

### Test 2 -- Grocery Food Exempt

**Input:** Customer buys $150 groceries in Montpelier.
**Expected output:** Groceries are EXEMPT. Tax = $0. Total = $150.00.

### Test 3 -- Restaurant Meal

**Input:** Customer dines in a hypothetical town confirmed to levy the 1% local meals option. Bill = $80. Meals tax = 9% + 1% local = 10%.
**Expected output:** Tax = $80 x 10% = $8.00. Total = $88.00.

### Test 4 -- SaaS Subscription

**Input:** SaaS company charges VT business $600/month. Rate = 6% (no local option at customer's location).
**Expected output:** SaaS IS taxable. Tax = $600 x 6% = $36.00. Total = $636.00.

### Test 5 -- Clothing Exempt

**Input:** Customer buys $200 jacket in Burlington.
**Expected output:** Clothing is EXEMPT in Vermont. Tax = $0. Total = $200.00.

### Test 6 -- Bar Tab (On-Premises Alcohol)

**Input:** Customer's bar tab is $60 for alcoholic beverages in a hypothetical town confirmed to levy the 1% local alcoholic-beverage option. Alcoholic beverage tax = 10% + 1% local = 11%.
**Expected output:** Tax = $60 x 11% = $6.60. Total = $66.60.

### Test 7 -- Off-Premises Alcohol

**Input:** Customer buys $40 of wine at a liquor store in a town with the 1% local sales option. Sales tax = 6% + 1% local = 7%.
**Expected output:** Tax = $40 x 7% = $2.80. Total = $42.80.

### Test 8 -- Ski Lift Ticket

**Input:** Customer buys $130 lift ticket at a resort without local option tax. Rate = 6%.
**Expected output:** Lift tickets are taxable. Tax = $130 x 6% = $7.80. Total = $137.80.





Example A (Test 1): $500 of electronics delivered in Burlington, which has adopted the 1% local option sales tax. Tax = 500 x (6% + 1%) = $35.00.

```oa-check
name: VT sales tax, 6% state plus 1% local option
inputs:
  price: 500
steps:
  - state_tax: pct(price, 6)
  - local_tax: pct(price, 1)
  - total_tax: state_tax + local_tax
  - total_due: price + total_tax
expected:
  state_tax: 30.00
  local_tax: 5.00
  total_tax: 35.00
  total_due: 535.00
```

Example B (Test 3): $80 restaurant bill in a town with the 1% local option meals tax. Tax = 80 x (9% + 1%) = $8.00.

```oa-check
name: VT meals tax, 9% plus 1% local option
inputs:
  bill: 80
steps:
  - meals_tax: pct(bill, 9)
  - local_tax: pct(bill, 1)
  - total_tax: meals_tax + local_tax
expected:
  meals_tax: 7.20
  local_tax: 0.80
  total_tax: 8.00
```



## When to refuse or refer

Refer audit/assessment response, voluntary disclosure or penalty abatement, ambiguous classifications, multistate nexus and distinct city meals/rooms taxes. Preserve original EC 1/EC 6 software multistate routing, EC 2 cafe, EC 3 destination local-option choice, EC 4 clothing, EC 5 brewery and EC 7 resort analyses. Never infer another state's software treatment from Vermont's.

## Filing and payment

Register through myVTax. Prepare SUT-451 for the assigned period with taxable/exempt sales, use-tax purchases and local-option detail; retain exemption certificates and marketplace reconciliation. Submit, save acceptance, arrange payment and confirm it posted to the correct period. Department-assigned monthly/quarterly/annual returns are generally due the 25 th following the period, moved to a business day when required. Electronic filing is required for sales subject to local option, multiple locations, or prior-calendar-year sales/use remittances above USD 100,000; the read Department page permits paper only for the stated eligible single-location/no-local-option situation. Meals/rooms use their own return and any qualifying short-term surcharge must be included.

## Completion checklist

- Nexus and marketplace obligations checked independently.
- Product and exemption conditions supported, including clothing and software definitions.
- Each revenue category and delivery jurisdiction assigned correctly.
- Local option and separate city taxes distinguished.
- Return, payment and certificates reconciled and retained.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| 32 V.S.A. 09771. Read for general rate and taxable categories. | https://legislature.vermont.gov/statutes/section/32/233/09771 | 2026-11-13 |
| 32 V.S.A. 09701. Read for software, clothing/belts/accessories, vendor nexus and rolling thresholds. | https://legislature.vermont.gov/statutes/section/32/233/09701 | 2026-11-13 |
| 32 V.S.A. 09741. Read for food, medical, manufacturing, farm and clothing exemptions. | https://legislature.vermont.gov/statutes/section/32/233/09741 | 2026-11-13 |
| 32 V.S.A. 09713. Read for marketplace facilitator collection. | https://legislature.vermont.gov/statutes/section/32/233/09713 | 2026-11-13 |
| 32 V.S.A. 09241. Read for separate meals/rooms and alcohol categories. | https://legislature.vermont.gov/statutes/section/32/225/09241 | 2026-11-13 |
| 32 V.S.A. 03202. Read for tax-specific penalty framework. | https://legislature.vermont.gov/statutes/section/32/103/03202 | 2026-11-13 |
| Department sales-and-use-tax. Read for SUT-451, electronic requirements, assigned frequency and due dates. | https://tax.vermont.gov/business/sales-and-use-tax | 2026-11-13 |
| Department local-option-tax. Read for local-option adoption and separate Burlington/Rutland municipal administration. | https://tax.vermont.gov/business/local-option-tax | 2026-11-13 |
| Department meals-and-rooms-tax. Read for separate returns and qualifying short-term rental surcharge. | https://tax.vermont.gov/business/meals-and-rooms-tax | 2026-11-13 |

Not yet confirmed: the legacy service list (commercialcleaning, fabrication/printing, repair/maintenance bundles, residentialcleaning, landscaping, ITconsulting and personalcare), blanket vendor-discount claim, exact exemption-certificate timing/retention and application of penalties to a particular delinquency; custom software/streaming classification outside the statutory prewritten/specified-digital definitions; current municipality-specific meals/rooms taxes for Burlington/Rutland. The old belt-taxable and all-brewery-merchandise-taxable assertions were corrected against 9701(24)/9741(45); no unsupported city-rate assumption is usable guidance.
