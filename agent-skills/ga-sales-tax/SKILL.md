---
name: ga-sales-tax
description: "Apply Georgia sales and use tax for 2026, for sellers in Georgia, remote sellers, marketplace facilitators and buyers owing use tax. Covers the 4% state rate plus local taxes by delivery jurisdiction code from the quarterly rate chart (6% to 9% from 1 October 2026), remote seller registration (over $100,000 or 200 or more sales), the $100,000 marketplace facilitator test, what is taxed and exempt (groceries at local rate only, electronic software against digital products), Form ST-5 certificates, use tax reason codes, Form ST-3 due on the 20th, the $500 electronic filing trigger, prepaid estimated tax over $60,000, vendor's compensation (3% of the first $3,000, 0.5% above) and penalties. Trigger on \"Georgia sales tax\", \"GA sales tax\", \"Georgia use tax\", \"Form ST-3\", \"Georgia economic nexus\", \"Georgia ST-5\". Load us-sales-tax first for the general method."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ga-sales-tax"
  jurisdiction: "US-GA"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Georgia sales and use tax, 2026

> **Source-cited draft.** Built from the Georgia Department of Revenue's sales and use tax pages, the general rate charts for July to September 2026 and from 1 October 2026, policy bulletins SUT-2019-02, SUT-2020-01 and SUT-2025-02, the Form ST-3 instructions, Form ST-5, the 2020 list of exemptions and DOR's due date and penalty pages, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Georgia's state sales and use tax is **4%**, and local taxes are added by the jurisdiction where the customer takes delivery: on the chart from 1 October 2026 combined rates run from **6% to 9%** (City of Atlanta 8.9%). Rates change quarterly, so always use the chart for the quarter of the sale. A seller outside Georgia must register once its Georgia retail sales of goods exceed **$100,000** or number **200 or more** in the previous or current year, leaving out sales a marketplace facilitator handled. Returns (Form ST-3) are due on the **20th** of the month after the period, even with no sales. A policy bulletin is DOR's position but "does not have the force or effect of law".

## Scope and who this is for

- Businesses selling goods or taxable services in Georgia or to Georgia customers: whether to register, what to charge, which local rate, how to file.
- Out-of-state sellers deciding whether they must register, and marketplace facilitators and their sellers.
- Businesses and individuals owing use tax because no Georgia tax was charged.
- Sellers accepting, and buyers giving, Form ST-5 certificates.
- Georgia is a full member of the Streamlined Sales and Use Tax Agreement from 1 July 2011 ([Streamlined Sales Tax](https://dor.georgia.gov/taxes/tax-rules-and-policies/streamlined-sales-tax)).

Out of scope: Georgia income tax (`ga-income-tax`, `ga-corporate-and-ptet`); motor vehicles (most pay title ad valorem tax, TAVT, instead of sales tax); motor fuel and prepaid local tax; lodging beyond the marketplace rules; alcohol and tobacco excise; the detail of agricultural (GATE) and industry-specific exemptions.

## Ask the client first

1. **Is the business physically in Georgia** (office, store, warehouse, employees, inventory), at Georgia trade shows, or holding a contract with a Georgia state agency?
2. **If outside Georgia:** in 2025 and so far in 2026, its gross revenue from, and number of, its own direct retail sales of goods delivered into Georgia, leaving out marketplace-facilitated sales ([SUT-2019-02](https://dor.georgia.gov/media/35301/download); [SUT-2020-01](https://dor.georgia.gov/media/35306/download)). Does it sell through, or run, a marketplace?
3. **What exactly does it sell:** goods, groceries, prepared food, downloaded software, digital products (e-books, music, video, digital codes), repair or installation labour, lodging, admissions, amusement or other services?
4. **Where do customers take delivery:** which county, and is it inside the City of Atlanta or another city with its own code?
5. **Is it registered, at what filing frequency,** did any return exceed $500, and was last year's state tax over $60,000?
6. **Paperwork and history:** a Form ST-5 for every untaxed sale? Purchases for own use without Georgia tax? Late or unfiled periods, or contact from DOR?

## The method, step by step

### Rates, bands and thresholds

| Item | Amount, 2026 | Source |
| --- | --- | --- |
| State sales and use tax, included in every jurisdiction's chart rate except codes 803 and 805 | 4% | [General rate chart from 1 October 2026](https://dor.georgia.gov/document/document/httpsdorgeorgiagovdocumentdocumentgeneral-rate-chart-effective-october-1-2026/download) |
| Combined state and local rates on the chart from 1 October 2026 | 6% to 9% | same |
| Cobb County (033) and Gwinnett County (067), from 1 October 2026 | 6% | same |
| City of Atlanta, DeKalb part (044A) and Fulton part (060A), from 1 October 2026 | 8.9% | same |
| Fulton County outside Atlanta, Hapeville, College Park and East Point (060), from 1 October 2026 | 7.75% | same |
| Fulton County inside Hapeville, College Park or East Point (800 to 802), from 1 October 2026 | 8.75% | same |
| Clayton County outside College Park (031), from 1 October 2026 | 8% | same |
| Clayton County inside College Park (804), from 1 October 2026 | 9% | same |
| Special Fulton districts Central Yards (803) and South Downtown (805), from 1 October 2026; the 4% state rate is not included | 3.9% shown | same |
| Richmond County (121), 1 July to 30 September 2026 | 8.5% | [General rate chart, July to September 2026](https://dor.georgia.gov/document/document/general-rate-chart-effective-july-1-2026-through-september-30-2026pdf/download) |
| Richmond County (121), from 1 October 2026 | 9% | [General rate chart from 1 October 2026](https://dor.georgia.gov/document/document/httpsdorgeorgiagovdocumentdocumentgeneral-rate-chart-effective-october-1-2026/download) |
| Appling County (001), from 1 October 2026 | 8% | same |
| Remote seller test, gross revenue from retail sales of goods into Georgia, previous or current year | exceeding $100,000 | [SUT-2019-02](https://dor.georgia.gov/media/35301/download) |
| Remote seller test, number of separate retail sales | 200 or more | same |
| Marketplace facilitator test, facilitated plus own Georgia sales, previous or current year | $100,000 or more | [SUT-2020-01](https://dor.georgia.gov/media/35306/download) |
| State agency contract that requires registration | exceeding $100,000 | [DOR out-of-state sellers FAQ](https://dor.georgia.gov/taxes/sales-use-tax/out-state-sellers) |
| Electronic filing and payment required once any return owes more than | $500 | [DOR file and pay FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/file-pay) |
| Prepaid estimated tax: prior-year state tax liability more than | $60,000 | same |
| Prepaid estimated tax, share of estimated tax | 50% | same |
| Vendor's compensation on the first $3,000 of tax on a timely return | 3% | [Form ST-3 instructions](https://dor.georgia.gov/document/document/st-3-sales-and-use-tax-returns-effective-sales-beginning-october-1-2022/download) |
| Vendor's compensation on tax above $3,000 | 0.5% | same |
| Late return or payment penalty, per month or part month (O.C.G.A. § 48-8-66) | greater of 5% or $5, up to the greater of 25% or $25 | [DOR penalty and interest rates](https://dor.georgia.gov/penalty-and-interest-rates) |

The chart's key names each local tax: L (LOST), E (ELOST), S (SPLOST), H (HOST or EHOST), M and m (MARTA), O (other: MOST, second LOST, constitutional, coliseum SPLOST), T, T2, Tf, Ta (the four TSPLOSTs, see [TSPLOSTs](https://dor.georgia.gov/tsplosts)) and P (PTRLOST). The 1% City of Atlanta Municipal Option Sales Tax applies inside city limits ([MOST](https://dor.georgia.gov/1-city-atlanta-municipal-option-sales-tax)). Special Fulton districts 803 and 805 show 3.9% and the chart says the 4% state rate is not included in them; confirm with DOR before charging there. Some local taxes do not apply to some sales (food, energy to manufacturers, jet fuel, some motor vehicles); those sales are reported with an indicator added to the jurisdiction code ([tips for the return](https://dor.georgia.gov/tips-completing-sales-and-use-tax-return)).

### Who must register

1. **Physically located in Georgia:** must register "unless all your sales are made through a marketplace". Every dealer registers "regardless of whether all sales will be online, out of state, wholesale, or exempt from tax". Register on the Georgia Tax Center; the number usually arrives by email in about 15 minutes; display the certificate at the place of business ([registration FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/sales-and-use-tax-registration-faq)).
2. **Remote sellers** (from 1 January 2020, [SUT-2019-02](https://dor.georgia.gov/media/35301/download)): a seller outside Georgia making retail sales of goods delivered electronically or physically into Georgia is a dealer once, in the previous or current calendar year, its gross revenue from those sales is "exceeding $100,000" or it makes "200 or more separate retail sales". It "may exclude" marketplace-facilitated sales when testing. It collects state and local tax at the delivery location's rate. Once met in 2025, it is a dealer for 2026; met during 2026, for the rest of 2026 and, on the previous-year test, 2027. No grace period is given.
   - **Exactly $100,000 or exactly 200 sales: check.** DOR's current [How do I know](https://dor.georgia.gov/taxes/sales-use-tax/how-do-i-know-if-i-need-collect-sales-use-tax) page asks about "over 200 separate sales transactions" or "at least $100,000 in total sales" in "the last calendar year", the reverse of the bulletin at both edges. A seller at either figure should get written confirmation.
3. **Marketplace facilitators** (from 1 April 2020, [SUT-2020-01](https://dor.georgia.gov/media/35306/download); [marketplace facilitators](https://dor.georgia.gov/marketplace-facilitators)): a person that contracts with sellers and both processes payment and lists, markets or takes orders (payment processing alone is not enough) is a dealer if facilitated plus own taxable Georgia sales "equals or exceeds $100,000.00" in the previous or current year; there is no transaction count. A franchisor is not a facilitator for a franchisee, nor a platform for a large seller, only if all three hold: the franchise system's US gross sales (or the large seller's own Georgia-sourced sales) were at least $500 million in the prior year, the seller holds a Georgia certificate, and a contract makes it collect. The facilitator collects state and local tax on the total sales price of facilitated sales, including delivery and service fees, and is liable for the greater of the tax due and the tax collected. It is relieved for errors caused by a non-related seller's wrong information if it made a reasonable effort. The seller does not collect on those sales. Facilitated sales go on a separate marketplace account.
4. **Other rules** ([registration FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/sales-and-use-tax-registration-faq); [out-of-state sellers](https://dor.georgia.gov/taxes/sales-use-tax/out-state-sellers)): a vendor with a contract exceeding $100,000 with a Georgia state agency must register and collect (counties and cities are not state agencies). No registration if trade shows are the only presence, last no more than 5 days in any 12 months and produced no more than $100,000 of net income in Georgia in the prior year, but tax is still collected on sales and orders at the show. Sales tax is a trust fund tax: a person who controls collection and willfully fails to pay is personally liable (O.C.G.A. § 48-2-52).

### Charging and accruing tax

1. **Classify each sale** (table below). A sale is taxable "until the contrary is established".
2. **Find the rate** for the place of delivery, by jurisdiction code on the chart for that quarter (rates "are updated each quarter", [rate FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/tax-rates)), not just the county.
3. **Tax the full sales price**, including delivery charges and mandatory gratuities on a taxable sale; separately stated installation and itemized repair labour are not taxed.
4. **Hold a good-faith certificate for every untaxed sale** (Form ST-5 rules below).
5. **Accrue use tax** on taxable goods and services bought or brought in without Georgia tax, and on stock taken for own use, on Part B of Form ST-3: base is the purchase price if used outside Georgia six months or less, otherwise the lower of price and fair market value; like taxes paid to another state are credited; property brought in on a change of domicile is generally exempt unless for business use. Reason codes: 01 (bought tax-paid in Georgia, used in a higher-rate jurisdiction), 02 (withdrawal from inventory), 03 (import, state tax), 04 (import, local tax).
6. **Keep records** (sales and purchase records, books of account, invoices) for at least three years.

## Boundary and exception table

Sources: [what is subject to tax](https://dor.georgia.gov/taxes/sales-use-tax/what-subject-sales-and-use-tax); [2020 list of exemptions](https://dor.georgia.gov/document/document/2020-list-sales-and-use-tax-exemptions/download).

| Item | Treatment | Condition or exception |
| --- | --- | --- |
| Tangible goods | Taxable, state and local | Unless an exemption in O.C.G.A. § 48-8-3 applies |
| Services | Generally not taxable | Taxed: accommodations, in-state transportation of individuals (taxis, limos), admissions, games and amusement charges |
| Delivery, freight, shipping and handling | Taxable with a taxable item | Not taxable when not tied to a taxable sale |
| Installation charges | Not taxable if separately stated | Otherwise part of the price |
| Repair labour | Not taxable if itemized | Parts taxable |
| Mandatory gratuities | Taxable | Voluntary tips are not |
| Grocery food ("food and food ingredients") | Exempt from the 4% state tax only | Subject to local taxes except the SPLOST levied with an EHOST; only for off-premises consumption by an individual, not for business use. Prepared food, alcohol, dietary supplements, tobacco, drugs, OTC drugs and medical or hygiene items are fully taxed |
| Prescription drugs | Exempt | Prescription-only drugs for people, insulin, prescription eyeglasses and contact lenses |
| Prewritten software delivered electronically or by load and leave | Exempt | From 1 January 2024 not "specified digital products", "other digital goods" or "digital codes", which are taxable |
| Software on a physical medium | Taxable | |
| SaaS | Not addressed on these pages | Refer; seek a letter ruling if material |
| Clothing | Taxable | The listed sales tax holidays were for past dates |
| Newspapers and magazines | Taxable | Subscriptions on the subscription price |
| Casual sales | Not taxable | Only within Rule 560-12-1-.07 |
| Manufacturing machinery and equipment "necessary and integral", with parts, industrial materials, packaging and consumable supplies | Exempt from all sales and use tax | Buyer gives Form ST-5M; mixed-use detail refer |
| Energy necessary and integral to manufacturing at a Georgia plant | Exempt except educational taxes (ELOST and local constitutional educational) | Not for producers of electricity for resale; report with the "E" indicator |
| Governments | Exempt | United States, State of Georgia, Georgia counties and cities, qualifying fire districts, paid directly by warrant on appropriated funds; not other states' governments |
| Nonprofits | Generally no exemption | "Georgia statute grants no sales or use tax exemption to churches, religious, charitable, civic and other nonprofit organizations" except named groups ([nonprofits](https://dor.georgia.gov/taxes/sales-use-tax/tax-exempt-nonprofit-organizations)) |

### Form ST-5 and other certificates

Sources: [Form ST-5](https://dor.georgia.gov/document/form/st-5-sales-tax-certificate-exemption/download); [nontaxable sales FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/nontaxable-sales); [out-of-state sellers](https://dor.georgia.gov/taxes/sales-use-tax/out-state-sellers).
- The seller carries the burden unless it takes a valid certificate in good faith: fully completed (name, address, sales tax number and signature where required), the right form, an exemption that existed on the date and in the jurisdiction, could apply to the item, and reasonable for the buyer's business.
- Resale protects the seller only if the buyer sells goods, holds a valid Georgia number at purchase and lists it, and the seller has no reason to think the item will not be resold. A few named buyers need no number (churches, K-12 private schools, parent-teacher organizations, Scout councils and some others).
- Tax-free treatment does not cover anything the buyer uses, "including items the purchaser will donate".
- One properly completed certificate per buyer; check numbers with the Sales Tax ID Verification Tool. Most certificates do not expire; the GATE certificate expires each year.
- Drop shipments: a Georgia dealer shipping to a Georgia customer of an out-of-state reseller with no Georgia presence need not collect if it holds the Multi-Jurisdictional Certificate of Exemption or the buyer's home-state resale certificate.

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Delivery address | Do not guess the rate; get the address and its jurisdiction code |
| Quarter of the sale | Use the chart for the delivery date's quarter |
| Certificate for an untaxed sale | Treat as taxable until a valid ST-5 is in hand |
| Remote seller's exact count at 200 or revenue at $100,000 | Register, or get DOR's written confirmation |

## Worked cases

Amounts are illustrations; rates are from DOR's charts for the quarter named.

**Case 1, a decision: which quarter's rate?** A Cobb County seller delivers a $1,000 table to a customer in Richmond County. Tax follows the delivery county, not the seller's. Delivered in September 2026, the chart rate is 8.5%: $85.00. Delivered in October 2026, it is 9%: $90.00. A seller deciding whether to ship before or after 1 October changes the customer's tax by $5.00; charging the seller's own Cobb rate of 6% ($60.00) would under-collect.

```oa-check
name: GA 2026 Richmond County delivery, quarter rate change
inputs:
  price: 1000
  rate_q3: 0.085
  rate_q4: 0.09
  cobb_rate: 0.06
steps:
  - tax_september: price * rate_q3
  - tax_october: price * rate_q4
  - difference: tax_october - tax_september
  - under_collected_if_seller_rate: tax_october - price * cobb_rate
expected:
  tax_september: 85.00
  tax_october: 90.00
  difference: 5.00
  under_collected_if_seller_rate: 30.00
```

**Case 2: groceries, use tax and vendor's compensation.** A grocer delivers $200 of food and $50 of cleaning supplies to a household in Appling County (8%). Food carries only the local part, 8% less 4% = 4%: $8.00; the supplies carry 8%: $4.00; total $12.00. A Cobb County business (6%, local part 2%) buys an $800 item online with no tax: state use tax $32.00 (reason 03) and local $16.00 (reason 04). If it buys a $900 item in a state that charged 5%, the 5% exceeds Georgia's 4%, so no state use tax is due, but local use tax is: $18.00. A contractor who buys a $600 item where the rate is 6% and uses it on a job where it is 8% owes 2% more: $12.00 (reason 01). A monthly filer whose state and local tax is $10,000, filed and paid electronically by the 20th, takes vendor's compensation of 3% of $3,000 ($90.00) plus 0.5% of $7,000 ($35.00) = $125.00, and remits $9,875.00. Late or on paper when e-filing is required, compensation is $0.

```oa-check
name: GA 2026 groceries at local rate, use tax and vendor's compensation
inputs:
  food: 200
  supplies: 50
  appling_rate: 0.08
  state_rate: 0.04
  online_item: 800
  cobb_rate: 0.06
  tax_on_return: 10000
steps:
  - grocery_tax: food * (appling_rate - state_rate) + supplies * appling_rate
  - state_use_tax: online_item * state_rate
  - local_use_tax: online_item * (cobb_rate - state_rate)
  - vendor_comp: min(tax_on_return, 3000) * 0.03 + max(tax_on_return - 3000, 0) * 0.005
  - remit: tax_on_return - vendor_comp
expected:
  grocery_tax: 12.00
  state_use_tax: 32.00
  local_use_tax: 16.00
  vendor_comp: 125.00
  remit: 9875.00
```

Other DOR examples kept for reference: a delivery platform's $18.50 order (burger $8, fries $2, drink $2, delivery $4, service fee $2.50) at 8% carries $1.48, collected by the platform ([SUT-2020-01](https://dor.georgia.gov/media/35306/download)); a $20 shirt with $5 delivery is taxed on $25.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-GAST-NEXUS | Remote seller at or near $100,000 or 200 sales | Get DOR's written confirmation; bulletin and web page differ |
| R-GAST-DIGITAL | SaaS, digital products and digital codes where the line matters | Refer or seek a letter ruling |
| R-GAST-LOCAL | Special districts 803 and 805, and sales exempt from some local taxes but not others | Refer |
| R-GAST-CERT | Manufacturing, GATE, data center and other certificate-based exemptions in detail | Refer |
| R-GAST-EXCISE | Motor vehicles, motor fuel, alcohol and tobacco | Refer |
| R-GAST-VDA | Unfiled past periods with no DOR contact | Consider a Voluntary Disclosure Agreement: penalties usually waived, interest due, look-back usually 36 months, longer where tax was collected and not paid ([VDA program](https://dor.georgia.gov/voluntary-disclosure-agreements)) |
| R-GAST-AUDIT | Audits, assessments, appeals and refund claims | Refer to a Georgia CPA, EA or tax attorney |

## Filing and payment

Sources: [file and pay FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/file-pay); [due dates](https://dor.georgia.gov/sales-use-tax-due-dates); [Form ST-3 instructions](https://dor.georgia.gov/document/document/st-3-sales-and-use-tax-returns-effective-sales-beginning-october-1-2022/download); [penalty and interest](https://dor.georgia.gov/penalty-and-interest-rates).

1. **Log in to the Georgia Tax Center** (gtc.dor.ga.gov). Most dealers file monthly; quarterly and annual periods exist, and a dealer may ask in writing to change (Rule 560-12-1-.22). A dealer with four or more locations files under a master account.
2. **Complete Form ST-3** by jurisdiction code: Part A sales, Part B use tax with reason codes, excess tax collected added to the amount due; prepaid estimated tax on lines 11 and 12 for a dealer whose prior-year state tax exceeded $60,000 (50% of its average monthly state tax, adjusted for rate changes, per DOR's annual letter).
3. **File by the 20th** of the month after the period (O.C.G.A. § 48-8-49), even with no sales. Once any return owes more than $500, file and pay electronically for every later period; anyone paying electronically must file electronically.
4. **Take vendor's compensation** only if both return and payment are on time: "Vendor's compensation is only given when both the payment and return are submitted timely."
5. **After filing:** amend with a new ST-3 ticking Amended Return; a mailed return and payment are on time if postmarked by the due date; cash totals may be rounded to a nickel (never more than 4 pennies) with tax on the unrounded price ([SUT-2025-02](https://dor.georgia.gov/document/document/sut-2025-02-federal-government-end-production-penny/download)).

**2026 due dates** ([due dates](https://dor.georgia.gov/sales-use-tax-due-dates)):

| Period | Due |
| --- | --- |
| Monthly: January to December 2026 | 20 Feb, 20 Mar, 20 Apr, 20 May, 22 Jun, 20 Jul, 20 Aug, 21 Sep, 20 Oct, 20 Nov, 21 Dec 2026, 20 Jan 2027 |
| Quarterly: Q1 to Q4 2026 | 20 Apr, 20 Jul, 20 Oct 2026, 20 Jan 2027 |
| Annual 2026 | 20 Jan 2027 |

2025 periods (late, amended or audited returns): use the chart for the 2025 quarter. Monthly 2025 returns fell due 20 Feb, 20 Mar, 21 Apr, 20 May, 20 Jun, 21 Jul, 20 Aug, 22 Sep, 20 Oct, 20 Nov, 22 Dec 2025 and 20 Jan 2026; quarterly 21 Apr, 21 Jul, 20 Oct 2025 and 20 Jan 2026; annual 20 Jan 2026.

| Charge | Rule | Cap |
| --- | --- | --- |
| Late return or payment (O.C.G.A. § 48-8-66) | Greater of 5% of the tax or $5, plus 5% or $5 each further month or part month, "calculated separately for state and local taxes in aggregate" | Greater of 25% or $25 |
| False or fraudulent return | 50% of the tax due | none stated |
| Not filing electronically when required | Greater of $25 or 5% of the tax due | none stated |
| Not paying electronically when required | 10% of the tax due | none stated |
| Interest | Prime rate plus 3% a year, set each January, from the due date | none |

DOR's penalty table lists failure to file and failure to pay as separate rows under the same section, while the ST-3 instructions describe one penalty for each month the return is late; check a bill where both were late. For example, $2,000 due 20 October 2026 and paid 5 December 2026 (second month) costs 10%, $200.00, plus interest and lost vendor's compensation. For a small return the $5 minimum matters: a filer owing $40 ($25 state, $15 local) one month late has 5% of each part below $5; the penalty is $10 if the minimum applies to each part, $5 if once per return. Check the bill. DOR may waive penalties for reasonable cause (O.C.G.A. § 48-2-43), requested on the Georgia Tax Center.

## Completion checklist

- Dealer status decided: physical presence; or remote seller over $100,000 or 200 or more direct sales in 2025 or 2026; or facilitator at $100,000 or more. Edge cases confirmed in writing.
- Registered on the Georgia Tax Center; facilitated sales on their own account.
- Each sale classified; groceries at local rate only and not for business use; electronic software against digital products checked.
- Rate from the chart for the quarter and the delivery jurisdiction code.
- Delivery charges and mandatory gratuities taxed; installation and repair labour separately stated.
- Good-faith ST-5 (or ST-5M, or multi-state certificate) for every untaxed sale.
- Use tax on Part B with the right reason code.
- Return by the 20th, zero returns included; electronic once over $500; prepaid estimated tax if last year's state tax exceeded $60,000.
- Vendor's compensation only on a timely return and payment.
- Records kept at least three years.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR sales tax rates, general. Read for the list of quarterly charts. | https://dor.georgia.gov/sales-tax-rates-general | 2026-11-13 |
| General rate chart effective 1 October 2026. Read for the 4% note, codes 803 and 805, and the Appling, Cobb, Gwinnett, Fulton, Atlanta, Hapeville, College Park, East Point, Clayton and Richmond rates. | https://dor.georgia.gov/document/document/httpsdorgeorgiagovdocumentdocumentgeneral-rate-chart-effective-october-1-2026/download | 2026-11-13 |
| General rate chart, 1 July to 30 September 2026. Read for Richmond County at 8.5%. | https://dor.georgia.gov/document/document/general-rate-chart-effective-july-1-2026-through-september-30-2026pdf/download | 2026-11-13 |
| SUT-2019-02 remote sellers. Read for the over $100,000 and 200 or more tests. | https://dor.georgia.gov/media/35301/download | 2026-11-13 |
| SUT-2020-01 marketplace facilitators. Read for the $100,000 test, carve-outs, liability and the delivery order example. | https://dor.georgia.gov/media/35306/download | 2026-11-13 |
| DOR "How do I know if I need to collect". Read for the "over 200" and "at least $100,000" wording. | https://dor.georgia.gov/taxes/sales-use-tax/how-do-i-know-if-i-need-collect-sales-use-tax | 2026-11-13 |
| DOR marketplace facilitators page. Read for the page as a whole. | https://dor.georgia.gov/marketplace-facilitators | 2026-11-13 |
| DOR registration FAQ. Read for who registers, trade shows and trust fund liability. | https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/sales-and-use-tax-registration-faq | 2026-11-13 |
| DOR out-of-state sellers. Read for drop shipments, trade shows and the over-$100,000 state agency contract registration rule. | https://dor.georgia.gov/taxes/sales-use-tax/out-state-sellers | 2026-11-13 |
| DOR what is subject to sales and use tax. Read for taxed goods and services, delivery, installation, repair labour, gratuities and use tax. | https://dor.georgia.gov/taxes/sales-use-tax/what-subject-sales-and-use-tax | 2026-11-13 |
| DOR 2020 list of sales and use tax exemptions. Read for food, drugs, software, manufacturing and energy. | https://dor.georgia.gov/document/document/2020-list-sales-and-use-tax-exemptions/download | 2026-11-13 |
| DOR nontaxable sales FAQ. Read for the burden of proof and good faith. | https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/nontaxable-sales | 2026-11-13 |
| Form ST-5. Read for resale and exemption certificate conditions. | https://dor.georgia.gov/document/form/st-5-sales-tax-certificate-exemption/download | 2026-11-13 |
| DOR tax-exempt nonprofit organizations. Read for the no-general-exemption rule. | https://dor.georgia.gov/taxes/sales-use-tax/tax-exempt-nonprofit-organizations | 2026-11-13 |
| DOR tax rates FAQ. Read for quarterly updates. | https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/tax-rates | 2026-11-13 |
| DOR 1% City of Atlanta MOST. Read for the page as a whole. | https://dor.georgia.gov/1-city-atlanta-municipal-option-sales-tax | 2026-11-13 |
| DOR TSPLOSTs. Read for the four TSPLOST types. | https://dor.georgia.gov/tsplosts | 2026-11-13 |
| DOR tips for completing the return. Read for the local tax indicators. | https://dor.georgia.gov/tips-completing-sales-and-use-tax-return | 2026-11-13 |
| Form ST-3 instructions (sales from 1 October 2022). Read for Parts A and B, use tax reason codes, vendor's compensation, penalty and interest. | https://dor.georgia.gov/document/document/st-3-sales-and-use-tax-returns-effective-sales-beginning-october-1-2022/download | 2026-11-13 |
| DOR file and pay FAQ. Read for frequency, the $500 electronic trigger, prepaid estimated tax and record keeping. | https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/file-pay | 2026-11-13 |
| DOR sales and use tax due dates. Read for the 2025 and 2026 dates. | https://dor.georgia.gov/sales-use-tax-due-dates | 2026-11-13 |
| SUT-2025-02, end of penny production. Read for cash rounding. | https://dor.georgia.gov/document/document/sut-2025-02-federal-government-end-production-penny/download | 2026-11-13 |
| DOR penalty and interest rates. Read for the sales and use tax and mandatory electronic filing penalties. | https://dor.georgia.gov/penalty-and-interest-rates | 2026-11-13 |
| DOR voluntary disclosure agreements. Read for penalty waiver and look-back. | https://dor.georgia.gov/voluntary-disclosure-agreements | 2026-11-13 |
| DOR Streamlined Sales Tax. Read for full membership from 1 July 2011. | https://dor.georgia.gov/taxes/tax-rules-and-policies/streamlined-sales-tax | 2026-11-13 |

Not yet confirmed: the rate chart for January to March 2027 was not yet published; whether the $5 minimum penalty applies to each of the state and local parts or once per return; SaaS treatment; whether a remote seller at exactly $100,000 or exactly 200 sales is in or out (bulletin and web page differ).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ga-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ga-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
