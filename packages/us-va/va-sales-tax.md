---
name: va-sales-tax
description: Virginia retail sales and use tax for tax year 2026. Rates by locality (5.3% general, 6% in Central Virginia, Hampton Roads and Northern Virginia, 6.3% in eight Southside and Eastern Shore localities, 7% in James City County, Williamsburg and York County), the 1% rate on food for home consumption and essential personal hygiene products, economic nexus at more than $100,000 or 200 transactions, marketplace facilitators, what is taxable (tangible goods, accommodations, few services; electronically delivered software and SaaS are not taxed), Form ST-1 monthly or quarterly returns due the 20th, the dealer discount, penalties, consumer use tax with credit for other states' tax, and the August sales tax holiday. Trigger on "Virginia sales tax", "VA sales tax", "Virginia use tax", "Virginia nexus", "Form ST-1", "Virginia grocery tax". Load us-sales-tax-nexus-50-state-matrix for other states. Not for the US Virgin Islands gross receipts tax (see skills/us-virgin-islands).
version: "2.0"
jurisdiction: US-VA
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# Virginia retail sales and use tax, tax year 2026

> **Source-cited draft.** Built from Va. Code §§ 58.1-603, 58.1-603.1, 58.1-604, 58.1-611, 58.1-615 and 58.1-622, Virginia Tax's Retail Sales and Use Tax, Grocery Tax, Remote Sellers, Sales Tax Exemptions, Consumer's Use Tax and Sales Tax Holiday pages, its locality rate workbook (sheet "January 1, 2026 - Present") and ruling P.D. 25-98, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** The rate depends on where the buyer takes delivery: 5.3% in most of Virginia, 6% in Central Virginia, Hampton Roads and Northern Virginia, 6.3% in Charlotte, Gloucester, Halifax, Henry, Northampton, Patrick and Pittsylvania Counties and Danville, and 7% in James City County, Williamsburg and York County. Food for home consumption and essential personal hygiene products are 1% everywhere. A remote seller must register once it has more than $100,000 of Virginia retail sales or 200 or more transactions in the current or previous calendar year. Returns (Form ST-1) are filed electronically, monthly or quarterly as Virginia Tax assigns, by the 20th of the month after the period, even with no sales. Electronically delivered software and SaaS are not taxable.

## Scope and who this is for

This skill covers the Virginia retail sales and use tax administered by the Virginia Department of Taxation (Virginia Tax): registration, rates, what is taxable, returns and payment, exemption certificates and consumer use tax, for in-state dealers, remote sellers, marketplace sellers and facilitators, and Virginia businesses and individuals who owe use tax.

It does not cover: the motor vehicle sales and use tax (collected by the DMV at titling), aircraft and watercraft taxes, communications sales and use tax, the transient occupancy taxes localities levy on lodging (local ordinances), the disposable plastic bag tax, cigarette and tobacco taxes, or the local BPOL gross receipts tax (see `va-corporate-tax-and-bpol`). Virginia (US-VA) is not the US Virgin Islands: the Virgin Islands gross receipts tax is in `skills/us-virgin-islands`.

## Ask the client first

1. **Where does the buyer take delivery?** The locality sets the rate (5.3%, 6%, 6.3% or 7%), and food and hygiene products are 1% everywhere.
2. **Physical presence in Virginia** (office, store, warehouse, inventory, employees, a fulfillment center)? If yes, register as an in-state dealer (account starts with 10).
3. **For a remote seller: Virginia retail sales and transaction count** in the current and previous calendar year, split between direct sales and sales through a marketplace facilitator.
4. **What is sold?** Tangible goods, food for home consumption or prepared food, software (tangible medium or electronic), SaaS, accommodations, repair or installation labor, separately stated delivery.
5. **Sales to exempt buyers** (resale, government, nonprofits, manufacturers, farmers) and whether certificates are on file.
6. **Filing frequency** Virginia Tax assigned (monthly or quarterly), and whether past returns were filed on time.

## The method, step by step

1. **Decide whether the seller must register.** An in-state dealer registers before making taxable sales. A remote seller registers when its own (non-marketplace) Virginia retail sales are more than $100,000, or it has 200 or more separate retail transactions, in the previous or current calendar year. Sales made only through a marketplace facilitator do not count toward the seller's own duty; the facilitator collects. Register online; Virginia Tax issues a 15-digit account number and the Certificate of Registration (Form ST-4), which must be displayed at the registered location.
2. **Classify each sale.** Taxable: retail sale, lease or rental of tangible personal property, accommodations furnished to transients, and services the chapter names as taxable (Va. Code § 58.1-603). Then check the exemptions (step 4).
3. **Find the rate for the delivery locality** from the rates table below or Virginia Tax's locality workbook. Apply 1% to qualifying food for home consumption and essential personal hygiene products.
4. **Apply exemptions and exclusions.** Resale (with certificate), prescription and nonprescription drugs, durable medical equipment, separately stated delivery charges, separately stated installation and repair labor, custom software, electronically delivered software and SaaS, and the others in the table of what is taxable.
5. **Compute the tax** on the gross sales price of each taxable item and total it by locality.
6. **File Form ST-1** electronically (Online Services account, eForms or Web Upload) by the 20th of the month after the period, reporting sales and tax by locality, and pay electronically. File a return for every period, even with no sales.
7. **Take the dealer discount** if the payment is not delinquent (see the rates table).
8. **Use tax.** A Virginia business that bought taxable goods without paying Virginia tax reports the cost on its regular sales tax return, less a credit for sales tax paid to another state, capped at the Virginia tax.

### Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
| --- | --- | --- | --- |
| General rate, most localities | 5.3% | "Everywhere else" on Virginia Tax's table | [Virginia Tax: Retail Sales and Use Tax](https://www.tax.virginia.gov/retail-sales-and-use-tax) |
| Central Virginia | 6% | Charles City, Chesterfield, Goochland, Hanover, Henrico, New Kent, Powhatan and Richmond City | [Virginia Tax: Retail Sales and Use Tax](https://www.tax.virginia.gov/retail-sales-and-use-tax) |
| Hampton Roads | 6% | Chesapeake, Franklin City, Hampton, Isle of Wight, Newport News, Norfolk, Poquoson, Portsmouth, Southampton, Suffolk and Virginia Beach | [Virginia Tax: Retail Sales and Use Tax](https://www.tax.virginia.gov/retail-sales-and-use-tax) |
| Northern Virginia | 6% | Alexandria, Arlington, Fairfax City, Fairfax County, Falls Church, Loudoun, Manassas, Manassas Park and Prince William; includes the 0.70% regional tax | [Virginia Tax: Retail Sales and Use Tax](https://www.tax.virginia.gov/retail-sales-and-use-tax); [Va. Code § 58.1-603.1](https://law.lis.virginia.gov/vacode/title58.1/chapter6/section58.1-603.1/) |
| Southside and Eastern Shore localities | 6.3% | Charlotte, Gloucester, Halifax, Henry, Northampton and Patrick Counties, Pittsylvania County and Danville | [Virginia Tax: Retail Sales and Use Tax](https://www.tax.virginia.gov/retail-sales-and-use-tax); [locality rate workbook](https://www.tax.virginia.gov/sites/default/files/inline-files/sales-and-use-tax-rates-by-locality-by-date.xlsx) |
| Historic Triangle | 7% | James City County, Williamsburg and York County | [Virginia Tax: Retail Sales and Use Tax](https://www.tax.virginia.gov/retail-sales-and-use-tax) |
| Food for home consumption and essential personal hygiene products | 1% | Statewide; not alcohol, tobacco, prepared hot food for immediate consumption, sales by caterers, vending machines, food trucks and other vendors presumed to sell for immediate consumption, or sales by a store whose immediate-consumption food sales are 80% or more of total sales | [Virginia Tax: Grocery Tax](https://www.tax.virginia.gov/grocery-tax) |
| Use tax rate | Same as the sales tax rate where the goods are used | Credit for sales tax paid to another state, not more than the Virginia tax | [Virginia Tax: Consumer's Use Tax](https://www.tax.virginia.gov/consumers-use-tax); [Va. Code § 58.1-611](https://law.lis.virginia.gov/vacode/title58.1/chapter6/section58.1-611/) |
| Economic nexus, remote sellers and marketplace facilitators | More than $100,000 of annual gross retail sales, or 200 or more transactions, to Virginia customers | Previous or current calendar year; a facilitator counts direct plus facilitated sales | [Virginia Tax: Remote Sellers, Marketplace Facilitators, and Economic Nexus](https://www.tax.virginia.gov/remote-sellers-marketplace-facilitators-economic-nexus) |
| Dealer discount | 4%, 3% or 2% of the first three percent of the state tax | By monthly taxable sales: $0 to $62,500 at 4%; $62,501 to $208,000 at 3%; $208,001 and above at 2%; only if the amount due is not delinquent | [Va. Code § 58.1-622](https://law.lis.virginia.gov/vacode/title58.1/chapter6/section58.1-622/) |
| Late filing or late payment penalty | 6% of the tax a month, up to 30%; minimum $10 | The $10 minimum applies to a late return even with no tax due | [Virginia Tax: Retail Sales and Use Tax](https://www.tax.virginia.gov/retail-sales-and-use-tax) |
| Interest | Federal underpayment rate plus 2% | Accrues until paid | [Virginia Tax: Retail Sales and Use Tax](https://www.tax.virginia.gov/retail-sales-and-use-tax) |
| Individuals' out-of-state catalog purchases | $100 or less in a calendar year need not be reported | Above $100, report the whole cost | [Virginia Tax: Consumer's Use Tax](https://www.tax.virginia.gov/consumers-use-tax) |
| Sales tax holiday 2026 | August 7 to 9, 2026 | School supplies $20 or less an item; clothing and footwear $100 or less; portable generators $1,000 or less; gas chainsaws $350 or less; chainsaw accessories and other hurricane items $60 or less; Energy Star and WaterSense products for home use $2,500 or less | [Virginia Tax: Virginia Sales Tax Holiday](https://www.tax.virginia.gov/virginia-sales-tax-holiday) |

### What is taxable and what is not

| Item | Treatment | Source |
| --- | --- | --- |
| Tangible personal property sold, leased or rented at retail | Taxable at the locality rate | [Va. Code § 58.1-603](https://law.lis.virginia.gov/vacode/title58.1/chapter6/section58.1-603/) |
| Accommodations furnished to transients | Taxable (the "accommodations" wording applies from September 1, 2021); stays of more than 90 days are not taxable | [Va. Code § 58.1-603](https://law.lis.virginia.gov/vacode/title58.1/chapter6/section58.1-603/); [Virginia Tax: Sales Tax Exemptions](https://www.tax.virginia.gov/sales-tax-exemptions) |
| Prepared food and restaurant meals | Taxable at the full rate (any local meals tax is not covered here) | [Virginia Tax: Grocery Tax](https://www.tax.virginia.gov/grocery-tax) |
| Clothing and footwear | Taxable, except during the August holiday within the price limits | [Virginia Tax: Virginia Sales Tax Holiday](https://www.tax.virginia.gov/virginia-sales-tax-holiday) |
| Prescription drugs, eyeglasses, hearing aids; nonprescription drugs and proprietary medicines for human use; durable medical equipment for the buyer's own use | Exempt | [Virginia Tax: Sales Tax Exemptions](https://www.tax.virginia.gov/sales-tax-exemptions) (Va. Code § 58.1-609.10) |
| Prewritten software delivered electronically, and SaaS or other software, data and content delivered over the Internet | Not taxable: the Department treats electronic delivery as a nontaxable service; software provided with the sale of tangible goods stays taxable | Va. Code § 58.1-609.5(1); [P.D. 25-98](https://www.tax.virginia.gov/laws-rules-decisions/rulings-tax-commissioner/25-98) |
| Software on a tangible medium | Taxable | [P.D. 25-98](https://www.tax.virginia.gov/laws-rules-decisions/rulings-tax-commissioner/25-98) |
| Custom software; separately stated charges to modify prewritten software | Not taxable | [Virginia Tax: Sales Tax Exemptions](https://www.tax.virginia.gov/sales-tax-exemptions) |
| Maintenance contracts covering both parts and labor | Taxable on one-half of the charge | [P.D. 25-98](https://www.tax.virginia.gov/laws-rules-decisions/rulings-tax-commissioner/25-98) (Va. Code § 58.1-609.5(10)) |
| Separately stated installation, repair and clothing-alteration labor; separately stated transportation charges; auto diagnostic labor (from July 1, 2023) | Not taxable; parts sold are taxable | [Virginia Tax: Sales Tax Exemptions](https://www.tax.virginia.gov/sales-tax-exemptions) |
| Professional, insurance and personal services with only inconsequential items and no separate charge; Internet access | Not taxable | [Virginia Tax: Sales Tax Exemptions](https://www.tax.virginia.gov/sales-tax-exemptions) |
| Data center computer hardware and software | Exempt where the data center meets the $150 million investment, job and VEDP memorandum conditions; certificate ST-11A | [Virginia Tax: Sales Tax Exemptions](https://www.tax.virginia.gov/sales-tax-exemptions) |
| Agricultural production for market (feed, seed, farm machinery and similar) | Exempt by use, not by type; certificate ST-18 | [Virginia Tax: Sales Tax Exemptions](https://www.tax.virginia.gov/sales-tax-exemptions) |
| Motor vehicles, aircraft, watercraft | Taxed under separate rates and rules; the motor vehicle tax is handled by the DMV | [Virginia Tax: Retail Sales and Use Tax](https://www.tax.virginia.gov/retail-sales-and-use-tax) |

## Boundary and exception table

| Situation | Rule |
| --- | --- |
| Seller in a 5.3% locality ships to a buyer in Williamsburg | Charge 7%: the rate of the place the merchandise is received |
| Buyer picks up at the store | The store's locality rate |
| Grocery item sold by a food truck, caterer, vending machine or theater | Full rate, not 1%: these vendors are presumed to sell for immediate consumption |
| Store whose food-for-immediate-consumption sales are 80% or more of total sales (motor fuel counted) | May not charge 1% |
| Remote seller with exactly $100,000 of sales and 150 transactions | Not yet required: the test is more than $100,000, or 200 or more transactions |
| Remote seller selling only through a marketplace facilitator | No registration needed; the facilitator collects |
| Seller using a facilitator and its own website | Test only the direct sales against the thresholds |
| Facilitator whose sellers are all registered | May apply to Virginia Tax for a waiver |
| No sales in the period | File the return anyway; a late zero return still costs the $10 minimum penalty |
| SaaS subscription billed to a Virginia customer | Not taxable; the Department may still ask for documents showing no tangible goods came with it |
| Computer sold with software and updates installed, with a maintenance contract covering both | Taxable in full; the software is part of the taxable equipment sale (P.D. 25-98) |
| Item bought in another state with 4% tax paid, used in a 6% locality | Owe 2% Virginia use tax |
| Individual's catalog purchases total $100 for the year | Nothing to report; at $101, report all $101 |
| Holiday: a $110 jacket and $90 shoes | Shoes exempt; jacket fully taxable (the limit is per item) |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| Delivery locality not known | Do not guess the rate; ask, or look up the ship-to locality in the workbook |
| Whether software was delivered electronically | Ask how it was delivered and whether any tangible item came with it |
| Whether a buyer is exempt | Treat the sale as taxable until a valid certificate is on file |
| Filing frequency | Use the frequency in the seller's Virginia Tax account; do not assume monthly |

## Worked cases

**Case 1, mixed basket in Henrico County (6%).** A Henrico grocery store sells USD 1,000 of general merchandise and USD 300 of food for home consumption in one sale. Merchandise: 6% x USD 1,000 = USD 60. Food: 1% x USD 300 = USD 3. Tax USD 63.

```oa-check
name: VA 2026 Henrico sale, general merchandise plus food for home consumption
inputs:
  general_goods: 1000
  grocery_food: 300
  locality_rate: 0.06
  food_rate: 0.01
steps:
  - tax_general: general_goods * locality_rate
  - tax_food: grocery_food * food_rate
  - total_tax: tax_general + tax_food
expected:
  tax_general: 60.00
  tax_food: 3.00
  total_tax: 63.00
```

**Case 2, a decision: must a remote seller register?** An out-of-state online seller had 2026 Virginia retail sales of USD 90,000 in 210 orders, all from its own website. Sales are under the USD 100,000 line, but 210 transactions meets the "200 or more" test, so it must register as an out-of-state dealer and collect. With 199 orders, neither test would be met and it would not register; had the 210 orders all gone through a marketplace facilitator, the facilitator would collect and the seller would not register.

```oa-check
name: VA 2026 remote seller economic nexus test
inputs:
  sales: 90000
  transactions: 210
steps:
  - over_sales_line: max(sales - 100000, 0)
  - transaction_test_met: min(floor(transactions / 200), 1)
  - must_register: max(min(over_sales_line, 1), transaction_test_met)
expected:
  over_sales_line: 0
  transaction_test_met: 1
  must_register: 1
```

**Case 3, use tax with credit.** A Virginia Beach (6%) business buys USD 2,000 of furniture from another state's seller who charged 4%. Virginia use tax is 6% x USD 2,000 = USD 120, less the USD 80 already paid, so USD 40 is reported on the business's sales tax return.

## When to refuse or refer

- Audit notices, assessments, appeals and penalty waivers.
- Voluntary disclosure for a seller that should have registered in past years.
- Manufacturing, processing, research, semiconductor and data center exemption claims beyond the headline rule (fact-specific; the data center exemption needs a VEDP memorandum).
- Nonprofit exemption applications and government contractor questions.
- Motor vehicle, aircraft, watercraft and communications taxes; local meals and lodging taxes.
- Bundles of software, hardware and services where the true object test decides the outcome.
- Direct payment permit applications (Va. Code § 58.1-624).
- Any question about the US Virgin Islands: different place, see `skills/us-virgin-islands`.

## Filing and payment

| Step | What to do | Source |
| --- | --- | --- |
| Register | Online as an in-state dealer (account starts 10), out-of-state dealer (starts 12) or marketplace facilitator; receive the 15-digit account number and Form ST-4 | [Virginia Tax: Retail Sales and Use Tax](https://www.tax.virginia.gov/retail-sales-and-use-tax) |
| Frequency | Monthly or quarterly, assigned by Virginia Tax on the dealer's liability | [Va. Code § 58.1-615](https://law.lis.virginia.gov/vacode/title58.1/chapter6/section58.1-615/) |
| Monthly due date | 20th of the next month (the April return is due May 20) | [Virginia Tax: Retail Sales and Use Tax](https://www.tax.virginia.gov/retail-sales-and-use-tax) |
| Quarterly due dates | April 20, July 20, October 20, January 20 | [Virginia Tax: Retail Sales and Use Tax](https://www.tax.virginia.gov/retail-sales-and-use-tax) |
| Return | Form ST-1, electronically: Online Services account, eForms (also for amendments) or Web Upload; paper only with an electronic filing waiver | [Virginia Tax: Retail Sales and Use Tax](https://www.tax.virginia.gov/retail-sales-and-use-tax) |
| Payment | Electronically with the return, or ACH credit | [Virginia Tax: Retail Sales and Use Tax](https://www.tax.virginia.gov/retail-sales-and-use-tax) |
| Individuals' consumer use tax | On the individual income tax return (line 35 on paper), or Form CU-7; due May 1 for calendar-year filers | [Virginia Tax: Consumer's Use Tax](https://www.tax.virginia.gov/consumers-use-tax) |

## Completion checklist

- [ ] Registration duty decided (in-state, remote seller test, marketplace).
- [ ] Each sale sourced to the delivery locality and the 2026 rate applied.
- [ ] Food and hygiene items at 1%, but not food sold for immediate consumption.
- [ ] SaaS and electronically delivered software left untaxed; software sold with hardware taxed.
- [ ] Separately stated delivery, installation and repair labor excluded.
- [ ] Exemption certificates on file for every exempt sale.
- [ ] Use tax reported on untaxed purchases, with credit for other states' tax.
- [ ] Form ST-1 filed and paid by the 20th, including zero returns; dealer discount only when not delinquent.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Virginia Tax, Retail Sales and Use Tax. Read for the rate table by locality, registration, Form ST-1, monthly and quarterly due dates, electronic filing, penalties ($10 minimum, 6% a month to 30%) and interest. | https://www.tax.virginia.gov/retail-sales-and-use-tax | 2026-11-13 |
| Virginia Tax, sales and use tax rates by locality workbook. Read for sheet "January 1, 2026 - Present": 94 localities at 5.3%, 28 at 6%, 8 at 6.3%, 3 at 7%, food 1% in all 133. | https://www.tax.virginia.gov/sites/default/files/inline-files/sales-and-use-tax-rates-by-locality-by-date.xlsx | 2026-11-13 |
| Virginia Tax, Grocery Tax. Read for the 1% rate and the items and vendors that do not qualify. | https://www.tax.virginia.gov/grocery-tax | 2026-11-13 |
| Virginia Tax, Remote Sellers, Marketplace Facilitators, and Economic Nexus. Read for the $100,000 / 200 transaction thresholds and facilitator rules. | https://www.tax.virginia.gov/remote-sellers-marketplace-facilitators-economic-nexus | 2026-11-13 |
| Virginia Tax, Sales Tax Exemptions. Read for medical, service, software, data center and agricultural exemptions. | https://www.tax.virginia.gov/sales-tax-exemptions | 2026-11-13 |
| Virginia Tax, Consumer's Use Tax. Read for the use tax rate, the $100 catalog rule and Form CU-7. | https://www.tax.virginia.gov/consumers-use-tax | 2026-11-13 |
| Virginia Tax, Virginia Sales Tax Holiday. Read for the August 7 to 9, 2026 dates and item limits. | https://www.tax.virginia.gov/virginia-sales-tax-holiday | 2026-11-13 |
| Virginia Tax, Ruling P.D. 25-98. Read for electronically delivered software as a nontaxable service and maintenance contracts. | https://www.tax.virginia.gov/laws-rules-decisions/rulings-tax-commissioner/25-98 | 2026-11-13 |
| Va. Code § 58.1-603. Read for the imposition of the sales tax and what it covers. | https://law.lis.virginia.gov/vacode/title58.1/chapter6/section58.1-603/ | 2026-11-13 |
| Va. Code § 58.1-603.1. Read for the 0.70% regional tax. | https://law.lis.virginia.gov/vacode/title58.1/chapter6/section58.1-603.1/ | 2026-11-13 |
| Va. Code § 58.1-611. Read for the credit for tax paid in another state. | https://law.lis.virginia.gov/vacode/title58.1/chapter6/section58.1-611/ | 2026-11-13 |
| Va. Code § 58.1-615. Read for monthly returns, less frequent periods and returns with no tax. | https://law.lis.virginia.gov/vacode/title58.1/chapter6/section58.1-615/ | 2026-11-13 |
| Va. Code § 58.1-622. Read for the dealer discount table. | https://law.lis.virginia.gov/vacode/title58.1/chapter6/section58.1-622/ | 2026-11-13 |

Not yet confirmed: the liability level at which Virginia Tax assigns quarterly rather than monthly filing (not stated on the page read); whether an Appropriation Act limits the § 58.1-622 dealer discount in 2026 (not checked); what the "(Contingent effective date)" note now shown on §§ 58.1-603 and 58.1-604 refers to (the contingent text was not read); the exemption certificate retention period; the full list of exemption certificate forms beyond those named on the exemptions page.
