---
name: ga-sales-tax
description: Use this skill whenever asked about Georgia sales and use tax. Trigger on phrases like "Georgia sales tax", "GA sales tax", "O.C.G.A. 48-8", "Georgia DOR". ALWAYS load us-sales-tax first.
version: 2.0
jurisdiction: US-GA
tax_year: 2026
last_updated: 2026-09-25
authored_by: OpenAccountants team
review_status: pending_review
trust_label: By OpenAccountants
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Georgia sales and use tax: 2026 rates, nexus, marketplaces, exemptions and filing

Figures are for tax year 2026, as they stand on 25 September 2026. They come from the Georgia Department of Revenue at dor.georgia.gov: its pages, forms, rate charts and policy bulletins. A policy bulletin is the Department's position, but it "does not have the force or effect of law". A short section near the end covers 2025 periods.

## Scope and who this is for ([DOR sales and use tax](https://dor.georgia.gov/taxes/sales-use-tax))

- Businesses that sell goods or taxable services in Georgia or to Georgia customers, and must decide whether to register, what to charge, which local rate applies and how to file.
- Out-of-state sellers deciding whether they must register (remote sellers), and marketplace facilitators and the sellers who use them.
- Businesses and individuals who owe use tax because no Georgia tax was charged on a purchase.
- Sellers accepting, and buyers giving, Form ST-5 resale and exemption certificates.
- Georgia is a full member of the Streamlined Sales and Use Tax Agreement, from 1 July 2011 ([Streamlined Sales Tax](https://dor.georgia.gov/taxes/tax-rules-and-policies/streamlined-sales-tax)).
- **Out of scope:** Georgia income tax. For individuals see the Guide `ga-income-tax`; for corporations, partnerships and the pass-through entity tax election see `ga-corporate-and-ptet`. Also out of scope: motor vehicles (most pay title ad valorem tax, TAVT, instead of sales tax), motor fuel and prepaid local tax, lodging charges beyond the marketplace rules, alcohol and tobacco excise, and the detail of agricultural (GATE) and industry-specific exemptions.

## Ask the client first

- Is the business physically located in Georgia (office, store, warehouse, employees, inventory)? Does it attend trade shows here, or hold a contract with a Georgia state agency?
- If it is outside Georgia: in 2025 and so far in 2026, what were its gross revenue and its number of separate retail sales of tangible goods delivered into Georgia, counting only its own direct sales and leaving out sales made through a marketplace facilitator ([SUT-2019-02](https://dor.georgia.gov/media/35301/download); [SUT-2020-01](https://dor.georgia.gov/media/35306/download))?
- Does it sell through a marketplace, or run one? If it runs one, what were its total facilitated Georgia sales plus its own?
- What exactly does it sell: goods, groceries, prepared food, downloaded software, digital products (e-books, music, video, digital codes), repair or installation labor, lodging, admissions, amusement, or other services?
- Where do customers take delivery (which county, and is it inside the City of Atlanta)?
- Is it registered, and what filing frequency has the Department assigned? Did it owe more than $500 on any return ([file and pay FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/file-pay))? Was its state tax liability last year more than $60,000?
- Does it hold a properly completed Form ST-5 (or other certificate) for every sale it did not tax? Has it bought taxable items for its own use without paying Georgia tax?
- Were any returns or payments late, or periods not filed at all? Has the Department contacted it?

## The method, step by step

1. **Decide whether the seller is a dealer that must register.** A business physically located in Georgia must register unless all its sales are made through a marketplace. A remote seller must register once, in the previous or current calendar year, its Georgia retail sales of tangible goods are more than $100,000 or number 200 or more ([SUT-2019-02](https://dor.georgia.gov/media/35301/download)). A marketplace facilitator must register once its facilitated plus own Georgia sales are $100,000 or more ([SUT-2020-01](https://dor.georgia.gov/media/35306/download)).
2. **Classify each sale.** Tangible goods are taxable unless an exemption applies. Services are generally not taxable; the taxed ones are accommodations, in-state transportation of individuals, admissions and amusement charges ([what is subject to tax](https://dor.georgia.gov/taxes/sales-use-tax/what-subject-sales-and-use-tax)). Check the exemption list ([list of exemptions](https://dor.georgia.gov/document/document/2020-list-sales-and-use-tax-exemptions/download)).
3. **Check the paperwork for every untaxed sale.** A sale is taxable "until the contrary is established". Hold a properly completed Form ST-5 or other certificate taken in good faith ([nontaxable sales FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/nontaxable-sales)).
4. **Find the rate where the customer takes delivery.** The state rate is 4%. Add the local taxes of the place where the customer takes delivery, using that place's jurisdiction code on the rate chart and Form ST-3, not just the county. Some cities have their own codes and rates: the City of Atlanta (044A, 060A), Fulton County inside Hapeville, College Park or East Point (800 to 802) and Clayton County inside College Park (804). Use the chart for the quarter of the sale; rates change quarterly ([rate FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/tax-rates); [general rate charts](https://dor.georgia.gov/sales-tax-rates-general)).
5. **Charge tax on the full sales price**, including delivery charges and mandatory gratuities on a taxable sale. Separately stated installation charges and itemized repair labor are not taxed ([what is subject to tax](https://dor.georgia.gov/taxes/sales-use-tax/what-subject-sales-and-use-tax)).
6. **Accrue use tax** on taxable goods and services bought or brought into Georgia without Georgia tax, and on items taken from resale stock for your own use ([ST-3 instructions](https://dor.georgia.gov/document/document/st-3-sales-and-use-tax-returns-effective-sales-beginning-october-1-2022/download)).
7. **File Form ST-3 through the Georgia Tax Center by the 20th** of the month after the period, even with no sales. File and pay electronically once you owe more than $500 on any return. Take vendor's compensation only if both the return and the payment are on time ([file and pay FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/file-pay); [due dates](https://dor.georgia.gov/sales-use-tax-due-dates)).
8. **Keep records for at least three years**: sales and purchase records, books of account, and invoices ([file and pay FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/file-pay)).

## Rates for 2026 ([general rate charts](https://dor.georgia.gov/sales-tax-rates-general); [chart from 1 October 2026](https://dor.georgia.gov/document/document/httpsdorgeorgiagovdocumentdocumentgeneral-rate-chart-effective-october-1-2026/download))

| Item | 2026 position | Condition |
| --- | --- | --- |
| State sales and use tax | 4% | Included in every jurisdiction's chart rate except two special Fulton County districts (codes 803 and 805) |
| Combined state and local rates | 6% to 9% on the chart from 1 October 2026 | For example Cobb and Gwinnett 6%, many counties 9%. Never guess: read the chart for the quarter and the delivery county |
| City of Atlanta (DeKalb or Fulton part) | 8.9% on the same chart | Codes 044A and 060A; the 1% Municipal Option Sales Tax (MOST) applies inside city limits ([MOST](https://dor.georgia.gov/1-city-atlanta-municipal-option-sales-tax)) |
| Fulton County inside Hapeville, College Park or East Point; Clayton County inside College Park | 8.75% (codes 800 to 802) and 9% (code 804) on the same chart | Separate codes from the county: Fulton outside these cities and Atlanta (060) is 7.75% and Clayton (031) is 8%. Report on the city code ([ST-3 instructions](https://dor.georgia.gov/document/document/st-3-sales-and-use-tax-returns-effective-sales-beginning-october-1-2022/download)) |
| Special Fulton districts 803 and 805 | 3.9% shown | The chart says the 4% state rate is not included in these two codes. Confirm with the Department before charging there |
| Use tax | Same state and local rates | Local use tax at the rate where the item is first used or received |

Rates change on the first day of a quarter. Richmond County, for example, was 8.5% on the chart for July to September 2026 ([chart from 1 July 2026](https://dor.georgia.gov/document/document/general-rate-chart-effective-july-1-2026-through-september-30-2026pdf/download)) and is 9% from 1 October 2026. The Department's rate charts "are updated each quarter" ([rate FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/tax-rates)).

**Which local taxes make up the rate.** The chart's key names each local tax a county levies. This Guide does not list local rates; read the chart.

| Chart code | Local tax |
| --- | --- |
| L | LOST (local option sales tax) |
| E | Educational (ELOST) |
| S | SPLOST (special purpose local option sales tax) |
| H | HOST or EHOST (homestead taxes) |
| M, m | MARTA; local MARTA in Atlanta |
| O | Other: MOST, second LOST, constitutional, coliseum SPLOST |
| T, T2, Tf, Ta | The four TSPLOSTs (regional, single-county, Fulton, Atlanta) ([TSPLOSTs](https://dor.georgia.gov/tsplosts)) |
| P | PTRLOST |

Some local taxes do not apply to some sales (for example food, energy sold to manufacturers, jet fuel and some motor vehicles). Those sales are reported with an indicator added to the jurisdiction code ([tips for the return](https://dor.georgia.gov/tips-completing-sales-and-use-tax-return)).

## Nexus, registration and marketplaces ([SUT-2019-02](https://dor.georgia.gov/media/35301/download); [SUT-2020-01](https://dor.georgia.gov/media/35306/download); [How do I know if I need to collect](https://dor.georgia.gov/taxes/sales-use-tax/how-do-i-know-if-i-need-collect-sales-use-tax))

### Remote sellers ([SUT-2019-02](https://dor.georgia.gov/media/35301/download); [How do I know if I need to collect](https://dor.georgia.gov/taxes/sales-use-tax/how-do-i-know-if-i-need-collect-sales-use-tax))

| Rule | Position from 1 January 2020 |
| --- | --- |
| Who | A seller outside Georgia making retail sales of tangible goods delivered electronically or physically into Georgia |
| Revenue test | Gross revenue "exceeding $100,000" from those sales |
| Transaction test | "200 or more separate retail sales" |
| Period | The previous or current calendar year. Once either test is met in 2025, the seller is a dealer for 2026; meeting it during 2026 makes it a dealer for the rest of 2026 and, on the previous-year test, for 2027. The bulletin gives no grace period |
| Marketplace sales | A remote seller "may exclude" sales facilitated by a marketplace facilitator when testing its duty |
| What to collect | State tax and local tax, with the local rate based on the delivery location |

**Exactly $100,000 or exactly 200 sales: check.** The Department's pages do not agree. The bulletin says revenue "exceeding $100,000" and "200 or more" sales. The Department's current "How do I know" page asks whether the seller had "over 200 separate sales transactions" or "at least $100,000 in total sales" in "the last calendar year". On the bulletin, $100,000 exactly is not over the line and 200 sales exactly is. On the web page it is the other way round. A seller at either figure should get written confirmation from the Department. The 200-sale test is not only in the 2019 bulletin: the current web page still asks about it. Check for later law changes before relying on it.

### Sellers with a Georgia presence, and other registration rules ([registration FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/sales-and-use-tax-registration-faq); [out-of-state sellers](https://dor.georgia.gov/taxes/sales-use-tax/out-state-sellers))

- **Physically located in Georgia.** Must register "unless all your sales are made through a marketplace".
- **Every dealer registers**, "regardless of whether all sales will be online, out of state, wholesale, or exempt from tax".
- **How.** Online through the Georgia Tax Center; the account number usually arrives by email within about 15 minutes. The certificate must be displayed at the place of business.
- **Officers.** Sales tax is a trust fund tax. A person who controls collecting and paying it and willfully fails to do so is personally liable (O.C.G.A. § 48-2-52).
- **State agency contracts.** A vendor with a contract exceeding $100,000 with a Georgia state agency must register and collect, even with no presence. Counties and cities are not state agencies for this rule.
- **Trade shows.** No registration if trade shows are the only presence, last no more than 5 days in any 12 months, and produced no more than $100,000 of net income in Georgia in the prior calendar year. Tax must still be collected on sales made at the show and on orders taken there.

### Marketplace facilitators ([marketplace facilitators](https://dor.georgia.gov/marketplace-facilitators); [SUT-2020-01](https://dor.georgia.gov/media/35306/download))

- **Who.** A person that contracts with sellers to facilitate taxable retail sales by both processing the payment and providing a service such as listing, marketing or taking orders. Merely processing payments does not make a facilitator.
- **Threshold.** From 1 April 2020 a facilitator is a dealer if its taxable Georgia retail sales, combined across all its marketplace sellers and itself, "equals or exceeds $100,000.00" in the previous or current calendar year. There is no transaction count.
- **Carve-outs.** A franchisor is not a facilitator for a franchisee, and a platform is not one for a large seller, only if all three conditions are met: the franchisor and all its franchisees combined had gross sales in the United States of at least $500 million in the prior calendar year (for a large seller: its own gross sales sourced to Georgia of at least $500 million); the franchisee or seller holds a Georgia sales tax certificate; and a contract makes it collect the tax.
- **What it collects.** State and local tax on the total sales price of facilitated sales sourced to Georgia, including delivery charges and service fees. It is liable for the greater of the full tax due and the tax it collected.
- **Relief.** It is not liable for tax missed because of wrong or incomplete seller information only if it shows the error came from the seller's information, it made a reasonable effort to get correct information, and the two are not related members. The seller is then solely liable.
- **The seller.** A marketplace seller does not collect or remit on sales its facilitator must collect on.
- **Reporting.** Facilitated sales go on a separate marketplace facilitator account. The facilitator's own direct sales go on a different account, or both on a master account.

## Boundary and exception table ([what is subject to tax](https://dor.georgia.gov/taxes/sales-use-tax/what-subject-sales-and-use-tax); [list of exemptions](https://dor.georgia.gov/document/document/2020-list-sales-and-use-tax-exemptions/download))

### What is taxed ([what is subject to tax](https://dor.georgia.gov/taxes/sales-use-tax/what-subject-sales-and-use-tax); [list of exemptions](https://dor.georgia.gov/document/document/2020-list-sales-and-use-tax-exemptions/download))

| Item | Treatment | Condition or exception |
| --- | --- | --- |
| Tangible goods | Taxable, state and local | Unless an exemption in O.C.G.A. § 48-8-3 applies |
| Services | Generally not taxable | Taxed: accommodations, in-state transportation of individuals (taxis, limos), admissions, and charges for games and amusement activities. |
| Delivery, freight, shipping and handling | Taxable when the item is taxable | Not taxable when not tied to a taxable sale |
| Installation charges | Not taxable if separately stated | Otherwise part of the taxable sales price |
| Repair labor | Not taxable if itemized | Parts are taxable |
| Mandatory gratuities | Taxable | Voluntary tips are not |
| Grocery food ("food and food ingredients") | Exempt from the 4% state tax only | Subject to all local taxes except the SPLOST levied with an EHOST. Only for off-premises consumption by an individual; not when bought for any use in a business. Prepared food, alcoholic beverages, dietary supplements, tobacco, drugs, OTC drugs and items for medical or hygiene purposes (cough drops, breath strips) are taxed at the full state and local rate |
| Prescription drugs | Exempt | Drugs dispensable only by prescription for people, insulin, and prescription eyeglasses and contact lenses; keep the prescription record |
| Prewritten software delivered electronically or by load and leave | Exempt | From 1 January 2024 the exemption excludes "specified digital products", "other digital goods" and "digital codes", which are taxable |
| Software on a physical medium | Taxable | Outside the electronic-delivery exemption |
| SaaS | Not addressed on the pages cited here | Refer; ask the Department for a letter ruling if the amount matters |
| Clothing | Taxable | The sales tax holidays on the exemption list were for past dates only |
| Newspapers and magazines | Taxable | Subscriptions are taxed on the subscription price |
| Casual (occasional) sales | Not taxable | Only if the sale meets the casual sale definition in Rule 560-12-1-.07 |

### Manufacturing ([list of exemptions](https://dor.georgia.gov/document/document/2020-list-sales-and-use-tax-exemptions/download))

- **Machinery and equipment** "necessary and integral to the manufacture of tangible personal property", with components and repair or replacement parts, and industrial materials, packaging supplies and consumable supplies, are exempt from all sales and use tax. The buyer gives Form ST-5M.
- **Energy** necessary and integral to manufacturing at a Georgia plant is exempt, except from the educational sales taxes (ELOST and local constitutional educational taxes). It does not cover energy bought by a manufacturer primarily engaged in producing electricity for resale. Report it with the "E" indicator.
- Detailed eligibility (what is "necessary and integral", mixed-use equipment) is not covered here; refer.

### Who can buy tax free ([nonprofits](https://dor.georgia.gov/taxes/sales-use-tax/tax-exempt-nonprofit-organizations); [Form ST-5](https://dor.georgia.gov/document/form/st-5-sales-tax-certificate-exemption/download))

- **Governments.** The United States, the State of Georgia, Georgia counties and cities, qualifying fire districts, and their departments, but only when paid directly to the seller by warrant on appropriated government funds. The list does not include other states' governments.
- **Nonprofits.** "In general, Georgia statute grants no sales or use tax exemption to churches, religious, charitable, civic and other nonprofit organizations." Only named groups qualify (for example licensed nonprofit hospitals and nursing homes, nonprofit private schools, food banks, health centers and volunteer clinics), each with its own paperwork. Nonprofits that sell goods must collect tax, apart from limited fundraising exemptions.

### Resale and exemption certificates: Form ST-5 ([Form ST-5](https://dor.georgia.gov/document/form/st-5-sales-tax-certificate-exemption/download); [nontaxable sales FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/nontaxable-sales))

- **Burden on the seller.** "All sales are subject to sales tax until the contrary is established." The seller carries the burden of proof unless it takes a valid certificate in good faith.
- **Good faith.** The certificate must be fully completed (name, address, sales tax number and signature where required), in the right form for the exemption, claim an exemption that existed on the date and in the jurisdiction of the sale, could apply to the item, and is reasonable for the buyer's type of business.
- **Resale.** The certificate protects the seller only if the buyer is in the business of selling tangible goods, has a valid Georgia sales tax number at the time of purchase and lists it, and the seller has no reason to believe the item will not be resold. A number is not needed for a few named buyers (churches, K-12 private schools, parent-teacher organizations, Scout councils and some others).
- **Own use.** Tax-free treatment does not extend to anything the buyer uses, "including items the purchaser will donate". A retailer who takes stock for its own use owes tax.
- **One certificate per buyer.** The supplier must get and keep one properly completed certificate from each buyer. Check numbers with the Sales Tax ID Verification Tool.
- **Expiry.** Most certificates do not expire; the Georgia Agricultural Tax Exemption (GATE) certificate expires each year.
- **Out-of-state buyers (drop shipments).** When a buyer with no Georgia presence or number buys for resale and has the Georgia dealer ship to its customer in Georgia, the dealer need not collect if it holds the Multi-Jurisdictional Certificate of Exemption or the buyer's home-state resale certificate ([out-of-state sellers](https://dor.georgia.gov/taxes/sales-use-tax/out-state-sellers)).

### Use tax ([what is subject to tax](https://dor.georgia.gov/taxes/sales-use-tax/what-subject-sales-and-use-tax); [ST-3 instructions](https://dor.georgia.gov/document/document/st-3-sales-and-use-tax-returns-effective-sales-beginning-october-1-2022/download))

- **When.** On the first use, storage or consumption in Georgia of taxable goods bought without Georgia tax, and on taxable goods or services bought in Georgia without tax.
- **Base.** The purchase price if the item was used outside Georgia for six months or less; the lower of purchase price and fair market value if used there longer.
- **Credit.** Like taxes paid to another state reduce the Georgia use tax.
- **Moving in.** Property brought in on a change of domicile is generally exempt, unless brought in for use in a trade, business or profession.
- **Reporting.** On Part B of Form ST-3, by jurisdiction and reason code: 01 (bought tax-paid in Georgia, used in a higher-rate jurisdiction), 02 (withdrawal from inventory), 03 (import, state tax), 04 (import, local tax).

## Worked cases ([rate FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/tax-rates); [SUT-2020-01](https://dor.georgia.gov/media/35306/download); [ST-3 instructions](https://dor.georgia.gov/document/document/st-3-sales-and-use-tax-returns-effective-sales-beginning-october-1-2022/download))

Amounts are illustrations. Rates are from the Department's charts for the quarter named; cases 3 and 7 are the Department's own examples.

1. **Quarterly rate change.** A seller in Cobb County delivers a $1,000 table to a customer in Richmond County. Tax follows the delivery county, not the seller's. Delivered in September 2026, the chart rate is 8.5%: $1,000 × 8.5% = $85.00. Delivered in October 2026, the rate is 9%: $1,000 × 9% = $90.00 ([chart from 1 July 2026](https://dor.georgia.gov/document/document/general-rate-chart-effective-july-1-2026-through-september-30-2026pdf/download); [chart from 1 October 2026](https://dor.georgia.gov/document/document/httpsdorgeorgiagovdocumentdocumentgeneral-rate-chart-effective-october-1-2026/download)).
2. **Remote seller using a marketplace.** An online store with no Georgia presence made 300 retail sales into Georgia totalling $120,000. A facilitator handled 280 of them ($110,000); the store made 20 directly ($10,000). It counts only its 20 direct sales and $10,000, so it has no duty to register ([SUT-2020-01](https://dor.georgia.gov/media/35306/download)). If instead it had made 200 or more direct sales in the year, even of small value, it would meet the bulletin's transaction test; at exactly 200, confirm with the Department.
3. **Marketplace delivery order.** A delivery platform that is a dealer processes a food order: burger $8.00, fries $2.00, drink $2.00, delivery $4.00 and service fee $2.50, a sales price of $18.50. Delivery and service fees are part of the price. At 8%, tax is $18.50 × 8% = $1.48, and the total is $19.98. The platform collects and remits; the restaurant is not liable for that tax ([SUT-2020-01](https://dor.georgia.gov/media/35306/download)).
4. **Groceries at the local rate only.** A grocer delivers $200 of food and $50 of cleaning supplies to a household in Appling County, where the chart rate is 8%. Food is exempt from the 4% state tax but not from local tax, so it carries 8% − 4% = 4%: $200 × 4% = $8.00. The cleaning supplies carry 8%: $50 × 8% = $4.00. Total tax $12.00. If an office bought the same $200 of food as snacks for its staff, the grocery exemption would not apply, because the food is for use in a business: $200 × 8% = $16.00. A restaurant buying ingredients to resell as meals is different: it buys for resale on Form ST-5 and pays no tax ([list of exemptions](https://dor.georgia.gov/document/document/2020-list-sales-and-use-tax-exemptions/download); [chart from 1 October 2026](https://dor.georgia.gov/document/document/httpsdorgeorgiagovdocumentdocumentgeneral-rate-chart-effective-october-1-2026/download)).
5. **Vendor's compensation.** A monthly filer's state and local tax (excluding motor fuel) is $10,000, filed and paid electronically by the 20th. Compensation is 3% of the first $3,000 ($90.00) plus 0.5% of the $7,000 above it ($35.00): $125.00, so it remits $9,875.00. If the return or the payment is late, or it files on paper when it must file electronically, compensation is $0 ([ST-3 instructions](https://dor.georgia.gov/document/document/st-3-sales-and-use-tax-returns-effective-sales-beginning-october-1-2022/download)).
6. **Late return.** A monthly filer owes $2,000 for September 2026, due 20 October 2026. It files and pays on 5 December 2026, in the second month after the due date. The penalty is 5% for each month or fraction of a month: 10%, or $200.00. It also owes interest from 20 October 2026 and loses vendor's compensation. For a small return the $5 minimum matters, and the penalty is "calculated separately for state and local taxes in aggregate". A filer owing $40 ($25 state and $15 local) and one month late has 5% of each part below $5 (5% of the whole $40 is only $2.00). If the minimum applies to each part, the penalty is $5 + $5 = $10; if once to the return, $5. Check the bill ([penalty and interest](https://dor.georgia.gov/penalty-and-interest-rates); [ST-3 instructions](https://dor.georgia.gov/document/document/st-3-sales-and-use-tax-returns-effective-sales-beginning-october-1-2022/download)).
7. **Delivery charge.** A seller charges $20 for a shirt and $5 to deliver it. Tax is due on $25 ([what is subject to tax](https://dor.georgia.gov/taxes/sales-use-tax/what-subject-sales-and-use-tax)).
8. **Use tax.** A Cobb County business (6%, of which 4% state and 6% − 4% = 2% local) buys an $800 item online and is charged no tax: state use tax $800 × 4% = $32.00 (reason 03) and local use tax $800 × 2% = $16.00 (reason 04). It buys a $900 item in a state that charged 5%: the 5% exceeds Georgia's 4%, so no state use tax is due, but local use tax is: $900 × 2% = $18.00. A contractor who buys a $600 item where the rate is 6% and uses it on a job where it is 8% owes 8% − 6% = 2% more: $12.00 (reason 01) ([ST-3 instructions](https://dor.georgia.gov/document/document/st-3-sales-and-use-tax-returns-effective-sales-beginning-october-1-2022/download)).

## When to refuse or refer

- **Georgia income tax.** Individuals: `ga-income-tax`. Corporations, partnerships, S corporations and the pass-through entity tax: `ga-corporate-and-ptet`.
- **The nexus boundary.** A remote seller at or near $100,000 or 200 sales; the Department's bulletin and web page point different ways. Get written confirmation ([How do I know](https://dor.georgia.gov/taxes/sales-use-tax/how-do-i-know-if-i-need-collect-sales-use-tax)).
- **SaaS, digital products and digital codes.** Where the line between exempt prewritten software and taxable digital products matters, refer or ask the Department for a letter ruling.
- **Special districts** (Fulton codes 803 and 805) and sales that are exempt from some local taxes but not others (energy to manufacturers, jet fuel, TSPLOST-exempt fuels, motor vehicles).
- **Manufacturing, agricultural (GATE), data center and other certificate-based exemptions** in detail.
- **Motor vehicles, motor fuel, alcohol and tobacco.**
- **Unfiled past periods.** A business that should have registered and has not been contacted may qualify for a Voluntary Disclosure Agreement: penalties are usually waived, interest is still due, and the look-back for sales tax is usually thirty-six months, longer where tax was collected but not paid ([VDA program](https://dor.georgia.gov/voluntary-disclosure-agreements)).
- **Audits, assessments, appeals and refund claims.** Refer to a Georgia CPA, EA or tax attorney.

## Filing and payment ([file and pay FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/file-pay); [due dates](https://dor.georgia.gov/sales-use-tax-due-dates); [ST-3 instructions](https://dor.georgia.gov/document/document/st-3-sales-and-use-tax-returns-effective-sales-beginning-october-1-2022/download))

### Frequency, returns and electronic filing ([file and pay FAQ](https://dor.georgia.gov/taxes/business-taxes/sales-use-tax/file-pay); [ST-3 instructions](https://dor.georgia.gov/document/document/st-3-sales-and-use-tax-returns-effective-sales-beginning-october-1-2022/download))

- **Frequency.** Returns are due monthly for most dealers. Quarterly and annual periods exist; a dealer may ask in writing to change its frequency (Rule 560-12-1-.22).
- **Due date.** The 20th of the month after the period (O.C.G.A. § 48-8-49). A return is due even with no sales or no tax.
- **Form ST-3.** Excess tax collected is added to the amount due. A dealer with four or more locations files on the Georgia Tax Center under a master account.
- **Electronic filing and payment.** Required once you owe more than $500 on any return, and it continues even if later payments fall below $500. Anyone paying electronically must also file electronically. Paper filers use Form ST-3.
- **Prepaid estimated tax.** A dealer whose state tax liability (excluding local taxes) in the previous calendar year was more than $60,000 must prepay 50% of its estimated tax. Estimated tax is its average monthly state tax payment for last year, adjusted for any rate change. The prepayment appears on lines 11 and 12 of Form ST-3; follow the Department's annual prepaid estimated tax letter.
- **Amended returns.** File a new ST-3 with the Amended Return box ticked, showing changed and unchanged figures.
- **Cash rounding.** If pennies are short, a dealer may round a cash total to a nickel, but tax is due on the unrounded price, and rounding may never be more than 4 pennies ([SUT-2025-02](https://dor.georgia.gov/document/document/sut-2025-02-federal-government-end-production-penny/download)).

### 2026 due dates ([due dates](https://dor.georgia.gov/sales-use-tax-due-dates))

| Period | Due |
| --- | --- |
| Monthly: January to December 2026 | 20 Feb, 20 Mar, 20 Apr, 20 May, 22 Jun, 20 Jul, 20 Aug, 21 Sep, 20 Oct, 20 Nov, 21 Dec 2026, 20 Jan 2027 |
| Quarterly: Q1 to Q4 2026 | 20 Apr 2026, 20 Jul 2026, 20 Oct 2026, 20 Jan 2027 |
| Annual 2026 | 20 Jan 2027 |

### Vendor's compensation ([ST-3 instructions](https://dor.georgia.gov/document/document/st-3-sales-and-use-tax-returns-effective-sales-beginning-october-1-2022/download))

| Tax base (state and local, excluding motor fuel) | Rate | Condition |
| --- | --- | --- |
| First $3,000 of tax on the return | 3% | Both the return and the payment are on time |
| Tax above $3,000 | 0.5% | Same |
| Prepaid local tax on on-road motor fuel; off-road motor fuel | 3% | Motor fuel is out of scope here |

"Vendor's compensation is only given when both the payment and return are submitted timely." A dealer required to file electronically gets none if it files or pays on paper.

### Penalties and interest ([penalty and interest](https://dor.georgia.gov/penalty-and-interest-rates))

| Charge | Rule | Cap |
| --- | --- | --- |
| Late return or late payment (O.C.G.A. § 48-8-66) | Greater of 5% of the tax or $5, plus 5% or $5 for each further month or fraction of a month | Greater of 25% of the tax or $25 |
| False or fraudulent return | 50% of the tax due | None stated |
| Not filing electronically when required | Greater of $25 or 5% of the tax due | None stated |
| Not paying electronically when required | 10% of the tax due | None stated |
| Interest | Federal Reserve prime rate plus 3% a year, set each January, from the due date until paid | None |

- **One penalty or two?** The Department's table lists failure to file and failure to pay as separate rows under the same section. The ST-3 instructions describe one penalty billed "for each month, or fraction of a month, for which the return is delinquent", calculated separately for state and local taxes in aggregate. If both are late, check the bill against the section.
- **Timeliness.** A mailed return and payment are on time if postmarked by the due date. The return must be completed and signed to count as filed.
- **Waiver.** The Department may waive penalties in whole or part for reasonable cause (O.C.G.A. § 48-2-43); request it through the Georgia Tax Center. Voluntary disclosure also waives penalties but not interest.
- **Officers.** Unpaid trust fund tax can be collected from responsible officers personally.

## 2025 periods (for late, amended or audited 2025 returns) ([due dates](https://dor.georgia.gov/sales-use-tax-due-dates); [general rate charts](https://dor.georgia.gov/sales-tax-rates-general))

- **Rates.** Use the chart for the quarter of the 2025 sale; the Department keeps each 2025 quarterly chart.
- **Due dates.** Monthly 2025 returns fell due on 20 Feb, 20 Mar, 21 Apr, 20 May, 20 Jun, 21 Jul, 20 Aug, 22 Sep, 20 Oct, 20 Nov and 22 Dec 2025, and 20 Jan 2026. Quarterly: 21 Apr, 21 Jul and 20 Oct 2025, and 20 Jan 2026. The 2025 annual return was due 20 Jan 2026.
- **Nexus.** A remote seller's 2025 sales count toward the "previous calendar year" test for 2026.
- **Unchanged rules.** The Department's current pages describe the state rate, the vendor's compensation rates, the $500 electronic filing trigger and the penalty rates as standing rules, with no 2026 change.

## Completion checklist ([DOR sales and use tax](https://dor.georgia.gov/taxes/sales-use-tax))

- [ ] Dealer status decided: physical presence; or remote seller over $100,000 or 200 or more direct retail sales in 2025 or 2026 (facilitated sales left out); or facilitator at $100,000 or more. Exactly $100,000 or 200 sales confirmed with the Department.
- [ ] Registered through the Georgia Tax Center; marketplace facilitator sales on their own account.
- [ ] Each sale classified: goods, taxed services, food at local rate only (not for business use), exempt electronic software versus taxable digital products.
- [ ] Rate taken from the chart for the quarter, using the jurisdiction code for the place of delivery (county, or city code such as Atlanta, Hapeville, College Park or East Point).
- [ ] Delivery charges and mandatory gratuities taxed with the item; installation and repair labor separately stated.
- [ ] A good-faith Form ST-5 (or ST-5M, or multi-state certificate) on file for every untaxed sale.
- [ ] Use tax accrued on Part B with the right reason code.
- [ ] Return filed by the 20th, including zero returns; filed and paid electronically if any return was over $500; prepaid estimated tax paid if last year's state tax was over $60,000.
- [ ] Vendor's compensation (3% of the first $3,000, 0.5% above) taken only on a timely return and payment.
- [ ] Any late period costed: 5% or $5 a month up to 25% or $25, plus interest at prime plus 3%.
- [ ] Records kept for at least three years.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
