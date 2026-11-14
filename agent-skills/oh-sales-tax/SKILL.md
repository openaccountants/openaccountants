---
name: oh-sales-tax
description: "Ohio sales and use tax for 2026. Who must hold a vendor's license or seller's use tax license (physical presence, or over $100,000 or 200 or more sales into Ohio), what is taxable (goods, prewritten software, listed services, business-use computer and information services), which county or transit rate applies (state 5.75%, combined cap 8.75%), exemption certificates, the UST-1 return due on the 23rd, the 0.75% timely-filing discount capped at $750 per license per month from 1 January 2026, use tax, interest at 7% for 2026 and the Voluntary Disclosure Program. Trigger on \"Ohio sales tax\", \"OH sales tax\", \"UST-1\", \"Ohio vendor's license\", \"Ohio use tax\", \"STEC B\", \"Ohio economic nexus\", \"Ohio sales tax holiday\". Not the commercial activity tax (see oh-cat-tax)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/oh-sales-tax"
  jurisdiction: "US-OH"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Ohio sales and use tax, tax year 2026

> **Source-cited draft.** Built from the Ohio Department of Taxation's sales and use tax pages, its Q4 2026 county rate table, the taxability page, information releases ST 1999-04, ST 2005-02, ST 2007-06, ST 2009-03 and ST 2025-02, the 2026 sales tax holiday page, the interest rates page, and Ohio Revised Code sections 5739.02, 5739.12 and 5739.133, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Ohio's state rate is **5.75%**. Counties and regional transit authorities add up to 3%, and the combined rate cannot exceed **8.75%**; the highest rate in the October to December 2026 table is **8.25%** (the Licking County part of Reynoldsburg, in the COTA area). An out-of-state seller must register once its Ohio sales are **over $100,000**, or it makes **200 or more** separate sales to Ohio customers, in the current or previous calendar year. Returns (UST-1) are due on the **23rd** of the month after the period. A return filed and paid on time earns a **0.75%** discount, capped from 1 January 2026 at **$750 per vendor's license for each month** the return covers. Goods an Ohio vendor sells are sourced to where the order is received; services and remote sellers' sales are sourced to where the customer receives them.

## Scope and who this is for

In scope:

- Businesses that sell goods or taxable services in Ohio or to Ohio customers and must decide what to charge, which county or transit rate applies, and how to file the UST-1.
- Out-of-state sellers and marketplace facilitators deciding whether they need an Ohio seller's use tax license.
- Businesses and individuals that owe use tax because no Ohio tax was charged on a purchase.
- Sellers accepting, and buyers giving, exemption certificates (STEC B, STEC U and the rest).

Out of scope, and where it goes:

| Topic | Skill or route |
| --- | --- |
| Ohio commercial activity tax (CAT), a separate tax on the seller's gross receipts | `oh-cat-tax` |
| Ohio individual income tax | `oh-income-tax` |
| Ohio employer withholding and unemployment insurance | `oh-payroll` |
| General US sales tax concepts (nexus after Wayfair, marketplace rules in other states) | `us-sales-tax` |
| Motor vehicles, watercraft and outboard motors titled through the clerk of courts; the resort area gross receipts tax; the Next Generation 9-1-1 access fee; lodging taxes; audit defense | Refer |

## Ask the client first

1. **Physical presence in Ohio?** A store, office, warehouse, employees or inventory. If so, it needs a vendor's license whatever its sales volume.
2. **If outside Ohio:** in the current or previous calendar year, were its sales to Ohio customers over $100,000, or did it make 200 or more separate sales to Ohio customers? On what date was either test first met?
3. **Marketplace:** does it sell only through a marketplace (such as Amazon or eBay) that collects Ohio tax? Does it run a marketplace for other sellers?
4. **What exactly does it sell:** goods, prewritten software, digital downloads, data processing or electronic information services, SaaS, or a service on Ohio's list (repair, installation, landscaping, janitorial, personal care, fitness and others)?
5. **Customers:** businesses or individuals? For computer and information services this decides taxability.
6. **Where:** where are orders received, where are goods delivered, and where do customers first use a service? Which Ohio counties does it sell into?
7. **Licenses:** how many fixed selling locations in Ohio, and does each have its own vendor's license? License number(s)?
8. **Filing:** monthly or semi-annual on the account? Was its tax over $75,000 in any calendar year?
9. **Exemptions:** does it hold a complete exemption certificate for every exempt sale? Does it sell to exempt entities? Did it buy taxable items without paying Ohio tax?
10. **History:** has it ever filed or paid late, or failed to register when it should have?

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 value | Condition | Source |
| --- | --- | --- | --- |
| State sales and use tax rate | 5.75% | Retail sales, leases and rentals of tangible personal property and the listed services | [ODT sales and use tax page](https://tax.ohio.gov/business/sales-and-use-tax) |
| County and transit authority tax | Up to 3% in total | Set in multiples of 0.05%; only counties and regional transit authorities levy it | [ODT sales and use tax page](https://tax.ohio.gov/business/sales-and-use-tax) |
| Maximum combined rate | 8.75% | State, local and transit together | [ODT sales and use tax page](https://tax.ohio.gov/business/sales-and-use-tax) |
| Highest rate in the 1 October to 31 December 2026 table | 8.25% | Licking (COTA): the part of Reynoldsburg in Licking County | [Q4 2026 rate table](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/rate-tables/by-county-q4-2026) |
| Cuyahoga (Cleveland) | 8.00% | Q4 2026 | [Q4 2026 rate table](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/rate-tables/by-county-q4-2026) |
| Franklin (Columbus) | 8.00% | Q4 2026 | [Q4 2026 rate table](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/rate-tables/by-county-q4-2026) |
| Hamilton (Cincinnati) | 7.80% | Q4 2026 | [Q4 2026 rate table](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/rate-tables/by-county-q4-2026) |
| Lucas (Toledo) | 7.75% | Q4 2026 | [Q4 2026 rate table](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/rate-tables/by-county-q4-2026) |
| Montgomery (Dayton) | 7.50% | Q4 2026 | [Q4 2026 rate table](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/rate-tables/by-county-q4-2026) |
| Summit (Akron) | 6.75% | Q4 2026 | [Q4 2026 rate table](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/rate-tables/by-county-q4-2026) |
| Stark (Canton) | 6.50% | Q4 2026 | [Q4 2026 rate table](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/rate-tables/by-county-q4-2026) |
| Warren | 7.25% from 1 October 2026 (6.75% before) | Rate change on 1 October 2026 | [Q4 2026 rate table](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/rate-tables/by-county-q4-2026) |
| Remote seller sales test | Over $100,000 of sales to Ohio customers | Current or previous calendar year; exactly $100,000 does not meet it | [ODT sales and use tax page](https://tax.ohio.gov/business/sales-and-use-tax) |
| Remote seller transaction test | 200 or more separate sales to Ohio customers | Current or previous calendar year; in force since 1 August 2019 | [ODT sales and use tax page](https://tax.ohio.gov/business/sales-and-use-tax) |
| Timely-filing discount | 0.75% of the tax shown due | Return filed and tax paid on or before the due date | [R.C. 5739.12(B)(1)](https://codes.ohio.gov/ohio-revised-code/section-5739.12) |
| Discount cap | $750 per vendor's license for each month covered by the return | Returns required to be filed on and after 1 January 2026; not on sales or leases of motor vehicles | [R.C. 5739.12(B)(1)](https://codes.ohio.gov/ohio-revised-code/section-5739.12); [ST 2025-02](https://tax.ohio.gov/wps/portal/gov/tax/business/ohio-business-taxes/sales-and-use/information-releases/st2025-02_vendor_timely_filing_discount_dec_2025) |
| County vendor's license and transient vendor's license fee | $50 | New applications from 9 April 2025 (was $25) | [ODT sales and use tax page](https://tax.ohio.gov/business/sales-and-use-tax) |
| Out-of-state seller's license, direct pay permit, consumer's use tax account | No fee | | [ODT sales and use tax page](https://tax.ohio.gov/business/sales-and-use-tax) |
| Semi-annual filing | May be authorized when tax is less than $1,200 per six-month period | | [ODT sales and use tax page](https://tax.ohio.gov/business/sales-and-use-tax) |
| Quarterly filing (direct pay and consumer's use tax accounts) | Quarterly liability less than $15,000 | | [ODT sales and use tax page](https://tax.ohio.gov/business/sales-and-use-tax) |
| Electronic payment | Annual tax liability over $75,000 | | [ODT sales and use tax page](https://tax.ohio.gov/business/sales-and-use-tax) |
| Accelerated payment | At least 75% of the month's expected tax, by the 23rd of that month; a shortfall charge of up to 5% | Vendors in the electronic payment group | [ST 2007-06](https://tax.ohio.gov/wps/portal/gov/tax/business/ohio-business-taxes/sales-and-use/information-releases/st200706) |
| Landscaping and lawn care service | Taxable once the provider earns $5,000 in a year | Each listed service tested separately | [ODT taxability page](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/taxability) |
| 2026 sales tax holiday | 7 to 9 August 2026: clothing $75 or less; school supplies and instructional materials $20 or less | No expanded $500 holiday in 2026 | [Sales tax holiday page](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/sales-tax-holiday) |
| Interest on late tax, calendar year 2026 | 7.0% a year (0.58% a month) | Simple: tax x rate x days late / days in year; 2025 was 8.0%; 2027 is certified at 7.0% | [ODT interest rates](https://tax.ohio.gov/individual/resources/interest-rates) |
| Assessment penalty | Up to 50% (failure to collect and remit, or collected and not remitted); up to 15% for all other assessments | Never more than 50% of the amount assessed | [R.C. 5739.133(A)](https://codes.ohio.gov/ohio-revised-code/section-5739.133) |
| Voluntary Disclosure Program lookback | Usually 36 months; 10% penalty on tax collected but not remitted; agreement back within 60 days | Only before the Department contacts the business | [ODT use tax, streamlined and VDA page](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/use-streamlined-vda) |

**Look up the rate, do not memorize a table.** Use The Finder on the Department's site (search by address, 9-digit ZIP or latitude and longitude). A 5-digit ZIP can cross county lines. Rates follow county borders except in transit areas such as the Central Ohio Transit Authority (COTA), which reaches into parts of Delaware (8.00% COTA), Fairfield (7.75% COTA) and Licking counties. A county or transit rate can change only at the start of a quarter.

### Step 1: decide whether the seller must be licensed

A business with a fixed location in Ohio needs a county vendor's license for each location before making taxable sales. A transient vendor's license covers temporary locations (shows, flea markets) statewide. An out-of-state seller needs a seller's use tax license once it meets either remote seller test. A seller whose every sale goes through a marketplace that collects and pays the Ohio tax needs no license. The Department's example: a business that reached $100,000 of sales on 15 October 2024 had to register, collect tax and file its first return by 23 November 2024. Source: [ODT sales and use tax page](https://tax.ohio.gov/business/sales-and-use-tax).

A license stays open until it is closed. Every licensed vendor must file a return for every period, including nil returns, until the license is closed through OH|TAX eServices or TeleFile. Ohio has no annual renewal.

### Step 2: classify each sale

Tangible personal property, including prewritten software whether on media or downloaded, is taxable unless an exemption applies. Services are taxable only if Ohio law lists them. Source: [ODT taxability page](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/taxability); [R.C. 5739.02](https://codes.ohio.gov/ohio-revised-code/section-5739.02). See the boundary tables below.

### Step 3: check exemption paperwork

An exempt sale needs a certificate carrying all the required data elements (STEC U, STEC B, the Streamlined Sales Tax certificate, or the MTC certificate for resale only). Source: [ST 2005-02](https://tax.ohio.gov/wps/portal/gov/tax/business/ohio-business-taxes/sales-and-use/information-releases/st2005-02exemptioncertificateforms).

### Step 4: source the sale

| Sale | Sourced to | Condition |
| --- | --- | --- |
| Goods sold by an Ohio vendor to an Ohio customer, in person or remotely (mail, phone, online) | Where the vendor receives the order | Not where the order is processed or shipped from. If the order is received outside Ohio, or the vendor does not capture where it was received, source it as a sale from outside Ohio |
| Goods sold by a transient vendor | Where the sale takes place | |
| Goods sold by an out-of-state seller | Where the customer receives the goods | If not known, the customer's address in the seller's records |
| Services, whoever provides them | Where the customer receives (first uses) the service | For example where a repaired item is handed back, or the club where a member uses the membership |
| Sales facilitated by a marketplace facilitator | Where the customer receives the property or service (R.C. 5741.05) | Except titled motor vehicles, watercraft and outboard motors. A facilitator's own direct sales with the order received in Ohio are sourced to where the order is received |
| Leases | Generally the primary location of the property when tax is due | Variations in the ST 2009-03 sourcing chart |
| Goods an Ohio vendor ships to customers outside Ohio | Not subject to Ohio tax | Check whether the destination state requires collection |

Source: [ST 2009-03](https://tax.ohio.gov/wps/portal/gov/tax/business/ohio-business-taxes/sales-and-use/information-releases/st-2009-03-sourcing). A customer who buys goods and pays Ohio tax at either the order-received rate or the delivery rate owes no more Ohio tax on that purchase. That relief covers goods only: for a service, the customer owes use tax on any difference if the rate where the service is used is higher.

### Step 5: find the rate and charge it on the full price

Take the rate for that location and that quarter from The Finder or the rate table. Charge tax on the full price, including delivery charges on taxable items. Itemize mixed taxable and nontaxable charges; if you do not, the whole charge is taxable. Store and vendor coupons reduce the taxable price; manufacturer's coupons and rebates do not. A trade-in reduces the price only for new motor vehicles, and for watercraft and outboard motors traded through a licensed dealer. Source: [ODT taxability page](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/taxability).

### Step 6: accrue use tax

Use tax is owed by the buyer when tax was due but not collected: out-of-state and online purchases, items bought exempt and then used in a taxable way (including inventory taken out for the business's own use), and goods bought untaxed outside Ohio and brought in. Same rates, at the location of use. Businesses with regular untaxed purchases open a consumer's use tax account and file the UUT-1; infrequent buyers can pay with the Ohio income tax return. Source: [ODT use tax, streamlined and VDA page](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/use-streamlined-vda).

### Step 7: file the UST-1, pay, and take the discount only if on time

Report all sales, including exempt sales, as gross sales on line 1, and exempt sales on line 2. Discount = the smaller of 0.75% of the tax due and $750 x licenses x months covered. Source: [R.C. 5739.12](https://codes.ohio.gov/ohio-revised-code/section-5739.12); [ST 2025-02](https://tax.ohio.gov/wps/portal/gov/tax/business/ohio-business-taxes/sales-and-use/information-releases/st2025-02_vendor_timely_filing_discount_dec_2025).

## Boundary and exception table

### Services ([ODT taxability page](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/taxability))

| Service | Treatment | Condition or exception |
| --- | --- | --- |
| Repair and installation of goods | Taxable | Not taxable if the item repaired or installed is exempt |
| Landscaping and lawn care; snow removal | Taxable once the provider earns $5,000 in a year from that service | Below that, no tax and no license; each service tested separately |
| Building maintenance and janitorial | Taxable once sales of the service reach $5,000 in a calendar year | Once reached, collect on all later sales; the $5,000 does not reset |
| Exterminating and pest control | Taxable | |
| Car washing, waxing, polishing; dry cleaning and laundry | Taxable | Coin-operated services excluded |
| Physical fitness facilities and recreation or sports clubs | Taxable | Gym memberships |
| Personal care services | Taxable | Facials, massages, tattoos, piercings, manicures, tanning. Haircuts, colouring and styling are not taxable; massage prescribed by a physician, chiropractor or listed nurse is not taxable |
| Hotel lodging | Taxable | Stays under 30 days in a facility with five or more sleeping rooms |
| Storage; towing; private investigation and security | Taxable | Storage of goods for resale is not taxable |
| Motor vehicle rental; in-state passenger transport | Taxable | Exceptions for warranty and dealer-paid rentals, public transit and commercial airlines |
| Delivery charges on taxable sales | Taxable | Part of the price |
| Accounting, legal, consulting, financial advice, real estate, insurance agencies | Not taxable | If any tangible item is incidental and not separately charged |
| Employment and job placement services | Not taxable | Repealed as taxable services from 1 October 2021 |
| Internet access | Not taxable | Federal Internet Tax Freedom Act |

**Unsure whether a service is listed?** Do not default either way. Check the taxability page and the matching information release, or ask the Department.

### Computer services, SaaS and digital products ([ST 1999-04](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/sales_and_use/information_releases/ST1999-04_Online_Services_and_Internet_Access-rev9.22.pdf))

| Item | Treatment | Condition |
| --- | --- | --- |
| Automatic data processing, computer services, electronic information services (including SaaS, hosted databases, online subscriptions) | Taxable only when provided for use in business | And only when the true object is the computer service itself, not a personal or professional service to which the computer work is incidental |
| The same service bought for personal use | Not taxable | The provider may rely on the customer's statement of business or personal use unless it is unreasonable on its face: ask at sign-up |
| Prewritten software | Taxable, business or personal, on media or downloaded | A reasonable, separately stated charge for modifying it is not part of the software |
| Digital downloads (e-books, music, movies) and streaming | Taxable | [ODT taxability page](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/taxability) |
| Services between members of an affiliated group | Not sales | One member owns or controls another (for corporations more than 50% of voting stock) |
| Business customer using software at several locations | Multiple Points of Use certificate (STEC MPU) | Apportion among locations |

### Goods ([ODT taxability page](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/taxability))

| Item | Treatment | Condition |
| --- | --- | --- |
| Food for human consumption off the premises | Exempt | Food eaten on the premises is taxable; takeout is exempt, but alcohol, soft drinks, tobacco and dietary supplements are not |
| Candy and chewing gum | Exempt as food | Ohio does not tax candy separately |
| Soft drinks, alcoholic beverages, dietary supplements, tobacco | Taxable | |
| Over-the-counter drugs | Taxable | Prescription drugs are exempt |
| Feminine hygiene products | Exempt | Since 1 April 2020 |
| Pet food and pet supplies | Taxable | Only food for humans is exempt |
| Clothing and footwear | Taxable | Except during the August sales tax holiday |
| Manufacturing equipment and supplies | Exempt | Claimed with an exemption certificate |
| Goods shipped out of Ohio | Not Ohio tax | Delivered out of state |

**2026 sales tax holiday** ([sales tax holiday page](https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/sales-tax-holiday)): from 12:00 a.m. Friday 7 August to 11:59 p.m. Sunday 9 August 2026, each item of clothing priced at $75 or less, and school supplies and school instructional materials priced at $20 or less, are exempt. Items over the limit are fully taxable. Items bought for use in business do not qualify.

### Exemption certificates ([ST 2005-02](https://tax.ohio.gov/wps/portal/gov/tax/business/ohio-business-taxes/sales-and-use/information-releases/st2005-02exemptioncertificateforms))

| Certificate | Use | Who it protects |
| --- | --- | --- |
| STEC U (unit) | One purchase | The vendor, if all data elements are present |
| STEC B (blanket) | A continuing claim on purchases from the same vendor | The vendor, if all data elements are present |
| STEC CC (construction contract) | Materials incorporated into real property under an exempt construction contract; signed by the contractor and the exempt contractee | The contractor too |
| STEC CO (contractor's) | The same purchases, signed by the contractor only | The vendor only |
| STEC MPU (multiple points of use) | Services or software used at several locations at once | The vendor |
| Streamlined Sales Tax certificate | In place of several Ohio STEC forms | The vendor |
| MTC Uniform Sales and Use Tax Certificate | Resale only | The vendor |

Exempt buyers include the United States, Ohio and its political subdivisions, churches and 501(c)(3) organizations. Direct pay permit holders pay tax straight to the Department.

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Whether a good is taxable | Taxable (goods are taxable unless an exemption applies) |
| Whether a service is on Ohio's list | No default: check the taxability page or the Department |
| Whether a computer or information service is bought for business or personal use | Business (taxable) unless the customer has said personal use |
| Where an Ohio vendor received the order | Treat as a sale from outside Ohio: source to the delivery address |
| Exact rate | The Finder for the address and quarter, never a 5-digit ZIP or a remembered table |
| Exemption certificate incomplete | Collect the tax |
| Whether the client also owes CAT | Flag: check `oh-cat-tax` |

### Red flags to raise with the client

| Flag | Why it matters |
| --- | --- |
| Remote seller near $100,000 or 200 Ohio sales | Registration due once met; first return by the 23rd of the next month |
| Monthly discount near or above $750 per license | The 2026 cap applies |
| Tax over $75,000 in a calendar year | Electronic and accelerated payments |
| Service business near $5,000 of landscaping or janitorial sales | Licensing and collection start |
| Unfiled periods on an open license | Nil returns still due; VDA only before the Department makes contact |
| SaaS or data service sold to businesses with no tax charged | Business-use services are taxable |

### Reading bank statements

| Narration | Meaning | Treatment |
| --- | --- | --- |
| OHIO DEPT OF TAXATION / ODT / OH TAX | Sales tax payment | Liability paid, not an expense |
| AMAZON / ETSY / EBAY payout | Marketplace settlement | Check whether the facilitator collected the Ohio tax |
| SQUARE / STRIPE / PAYPAL | Processor payout | Gross up to sales; fees separately |
| OHIO BWC | Workers' compensation premium | Not sales tax |

## Worked cases

**Case 1, a decision: which county rate does an Ohio vendor charge?** A Canton retailer in Stark County (6.50%) takes a phone order at its store for an $800 television and ships it to a customer in Cleveland, Cuyahoga County (8.00%). Goods sold by an Ohio vendor are sourced to where the order is received, so the retailer charges the Stark rate: $800 x 6.50% = $52.00. Charging the delivery rate would cost the customer $64.00, $12.00 more; the customer who paid the Stark rate owes no further use tax. If the item were a repair service delivered in Cleveland instead, the service rule would source it to Cuyahoga. Source: [ST 2009-03](https://tax.ohio.gov/wps/portal/gov/tax/business/ohio-business-taxes/sales-and-use/information-releases/st-2009-03-sourcing).

```oa-check
name: Ohio vendor sourcing, order-received rate against delivery rate (Q4 2026)
inputs:
  price: 800
  stark_rate: 0.065
  cuyahoga_rate: 0.08
steps:
  - tax_order_received: price * stark_rate
  - tax_delivery: price * cuyahoga_rate
  - difference: tax_delivery - tax_order_received
expected:
  tax_order_received: 52.00
  tax_delivery: 64.00
  difference: 12.00
```

**Case 2, the discount cap with three licenses.** A business reports three vendor's licenses on one consolidated monthly return due after 1 January 2026, with $400,000 of tax due, and files and pays on time. The discount at 0.75% would be $3,000, but the cap is $750 x 3 licenses x 1 month = $2,250. It remits $400,000 - $2,250 = $397,750. Source: [ST 2025-02](https://tax.ohio.gov/wps/portal/gov/tax/business/ohio-business-taxes/sales-and-use/information-releases/st2025-02_vendor_timely_filing_discount_dec_2025).

```oa-check
name: Ohio vendor discount cap, three licenses, one month (2026)
inputs:
  tax_due: 400000
  licenses: 3
  months: 1
steps:
  - discount_uncapped: tax_due * 0.0075
  - cap: 750 * licenses * months
  - discount: min(discount_uncapped, cap)
  - remit: tax_due - discount
expected:
  discount_uncapped: 3000.00
  cap: 2250.00
  discount: 2250.00
  remit: 397750.00
```

Further short cases, each from the sources above:

- **Remote seller over the transaction test.** An Oregon seller with no Ohio presence made 210 sales to Ohio customers in 2025 totalling $60,000. The sales test is not met, the transaction test is. It needs a seller's use tax license (no fee) for 2026 and charges the delivery address rate: a $500 order to Cuyahoga carries $500 x 8.00% = $40.00.
- **Semi-annual vendor.** One license, $1,500 of tax for January to June 2026, filed by 23 July 2026: discount $1,500 x 0.75% = $11.25, under the six-month cap of $4,500.
- **Sales tax holiday.** On 8 August 2026 a Columbus shopper (Franklin, 8.00%) buys a $70 jacket and $80 shoes. The jacket is exempt; the shoes are taxable in full: $80 x 8.00% = $6.40.
- **Late payment interest.** $10,000 due 23 April 2026, paid 30 days late: no discount, and interest of $10,000 x 7.0% x 30 / 365 = $57.53.

## When to refuse or refer

| Code | Situation | Action |
| --- | --- | --- |
| R-OH-CAT | Commercial activity tax questions | Use `oh-cat-tax` |
| R-OH-AUDIT | Audits, assessments, petitions for reassessment, appeals | Refer to an Ohio CPA, EA or tax attorney |
| R-OH-VDA | Past non-compliance | Refer for a Voluntary Disclosure application, only if the Department has not yet made contact |
| R-OH-BUNDLE | Complex bundled transactions, leases, and true object disputes over computer and information services (the Ohio Supreme Court's decision in Cincinnati Fed. S. & L. Co. v. McClain (2022) changed how the Department reads the professional services exception, per ST 1999-04) | Refer |
| R-OH-VEHICLE | Motor vehicles, watercraft and outboard motors taxed at titling | Refer |
| R-OH-CONSTRUCT | Construction contracts (the contractor usually pays tax on materials) | Refer, using the STEC CC and STEC CO rules above |
| R-OH-THRESHOLD | A service provider at exactly $5,000 of landscaping or janitorial sales | Confirm with the Department before relying on either reading |

## Filing and payment

| Frequency | Who | Due | Source |
| --- | --- | --- | --- |
| Monthly | The default for vendors, transient vendors and out-of-state sellers | The 23rd of the following month | [ODT sales and use tax page](https://tax.ohio.gov/business/sales-and-use-tax); [R.C. 5739.12(A)(1)](https://codes.ohio.gov/ohio-revised-code/section-5739.12) |
| Semi-annual | Authorized when tax is less than $1,200 per six months | 23 July (January to June) and 23 January (July to December) | [ODT sales and use tax page](https://tax.ohio.gov/business/sales-and-use-tax) |
| Quarterly | Direct pay permit holders and consumer's use tax accounts under $15,000 a quarter | 23 April, 23 July, 23 October, 23 January | [ODT sales and use tax page](https://tax.ohio.gov/business/sales-and-use-tax) |

- A due date on a weekend or holiday moves to the next business day.
- File electronically: OH|TAX eServices (or the Ohio Business Gateway), a Streamlined Sales Tax certified service provider, or TeleFile. Payment is electronic. A vendor whose certified service provider receives a monetary allowance gets no discount ([R.C. 5739.12(B)(2)](https://codes.ohio.gov/ohio-revised-code/section-5739.12)).
- **Electronic and accelerated payments.** Annual tax over $75,000: pay electronically and make accelerated payments of at least 75% of each month's expected tax by the 23rd of that month, with the balance on the return. No shortfall charge if the payment was at least 75% of the tax reported for the same month of the previous year ([ST 2007-06](https://tax.ohio.gov/wps/portal/gov/tax/business/ohio-business-taxes/sales-and-use/information-releases/st200706)).
- **Interest** runs at 7.0% for 2026, simple ([ODT interest rates](https://tax.ohio.gov/individual/resources/interest-rates)). **Assessment penalties** of up to 15%, or up to 50% where tax was not collected and remitted or was collected and kept ([R.C. 5739.133](https://codes.ohio.gov/ohio-revised-code/section-5739.133)). A late return also loses the discount.
- **2025 periods.** Returns required to be filed before 1 January 2026 took the full 0.75% discount with no cap; the December 2025 monthly return and the July to December 2025 semi-annual return were due on 23 January 2026, so they are capped. Interest on tax overdue during 2025 runs at 8.0%. County rates changed during 2025: use that quarter's rate table.

### Working paper

```
OHIO SALES TAX WORKING PAPER (UST-1)
Business: ______  Vendor's license(s): ______  Period: ______  Monthly / Semi-annual

A1 Gross sales, all sales including exempt (line 1)    ______
A2 Exempt sales, certificates on file (line 2)         ______
A3 Taxable sales by county or transit area x rate      ______
B1 Tax due                                             ______
C1 Discount, if on time: min(B1 x 0.75%, $750 x licenses x months)  ______
C2 Net payment (B1 - C1)                               ______
D1 Untaxed purchases subject to use tax                ______
Flags: rate from The Finder for the quarter; certificates complete;
business-use test on computer services; CAT checked separately.
```

## Completion checklist

- [ ] Nexus decided: physical presence, or over $100,000 or 200 or more Ohio sales in the current or previous calendar year; date first met recorded.
- [ ] Right license held: one county vendor's license per fixed location, a transient license, or a seller's use tax license; marketplace-only sellers checked.
- [ ] Every product and service classified; business-use test applied to computer and information services.
- [ ] Each sale sourced (order received, delivery, or where the service is used) and the rate taken for that quarter.
- [ ] Delivery charges included; mixed invoices itemized.
- [ ] Exemption certificates complete; MTC certificates used only for resale.
- [ ] Use tax accrued on untaxed purchases and goods taken out of inventory.
- [ ] UST-1 filed by the 23rd, with exempt sales on line 2.
- [ ] Discount taken only if on time, capped at $750 per license per month.
- [ ] Electronic and accelerated payments made if annual tax is over $75,000.
- [ ] CAT considered separately (`oh-cat-tax`).

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| ODT sales and use tax page. Read for 5.75%, the 3% local cap and 8.75% combined cap, licenses and the $50 fee, the remote seller tests and example, filing frequencies ($1,200, $15,000, $75,000) and the 23rd due dates. | https://tax.ohio.gov/business/sales-and-use-tax | 2026-11-13 |
| ODT sales and use tax rates by county, 1 October to 31 December 2026. Read for the county and COTA rates, 8.25% Licking (COTA) and the Warren change. | https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/rate-tables/by-county-q4-2026 | 2026-11-13 |
| R.C. 5739.12 (effective 30 September 2025, H.B. 96). Read for (A)(1) the 23rd and electronic filing, (B)(1) 0.75% and the $750 per license per month cap, (B)(2) certified service providers. | https://codes.ohio.gov/ohio-revised-code/section-5739.12 | 2026-11-13 |
| R.C. 5739.02. Read for the levy on retail sales. | https://codes.ohio.gov/ohio-revised-code/section-5739.02 | 2026-11-13 |
| R.C. 5739.133. Read for the 50% and 15% assessment penalties. | https://codes.ohio.gov/ohio-revised-code/section-5739.133 | 2026-11-13 |
| ST 2025-02, vendor timely filing discount. Read for the cap from 1 January 2026, the motor vehicle carve-out and the multi-license and semi-annual examples. | https://tax.ohio.gov/wps/portal/gov/tax/business/ohio-business-taxes/sales-and-use/information-releases/st2025-02_vendor_timely_filing_discount_dec_2025 | 2026-11-13 |
| ST 2009-03, sourcing. Read for order-received sourcing for Ohio vendors and marketplace facilitator sourcing under R.C. 5741.05. | https://tax.ohio.gov/wps/portal/gov/tax/business/ohio-business-taxes/sales-and-use/information-releases/st-2009-03-sourcing | 2026-11-13 |
| ODT taxability page. Read for the taxable services, the $5,000 landscaping test, food, soft drinks, pet supplies, feminine hygiene, prewritten software. | https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/taxability | 2026-11-13 |
| ST 1999-04, online services and internet access (PDF). Read for the business-use rule, true object and personal-use reliance. | https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/sales_and_use/information_releases/ST1999-04_Online_Services_and_Internet_Access-rev9.22.pdf | 2026-11-13 |
| ST 2005-02, exemption certificate forms. Read for STEC U, STEC B, STEC CC, STEC CO and the other certificates. | https://tax.ohio.gov/wps/portal/gov/tax/business/ohio-business-taxes/sales-and-use/information-releases/st2005-02exemptioncertificateforms | 2026-11-13 |
| ST 2007-06, electronic funds transfer and accelerated payments. Read for the 75% accelerated payment, the 5% charge and the safe harbour. | https://tax.ohio.gov/wps/portal/gov/tax/business/ohio-business-taxes/sales-and-use/information-releases/st200706 | 2026-11-13 |
| ODT use tax, streamlined and VDA page. Read for use tax, the 36-month lookback, the 10% penalty and the 60 days. | https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/use-streamlined-vda | 2026-11-13 |
| ODT sales tax holiday page. Read for 7 to 9 August 2026, $75 and $20, and no expanded holiday. | https://tax.ohio.gov/wps/portal/gov/tax/business/sales-and-use-tax/sales-tax-holiday | 2026-11-13 |
| ODT interest rates page. Read for 7.0% (2026 and 2027) and 8.0% (2025), and the formula. | https://tax.ohio.gov/individual/resources/interest-rates | 2026-11-13 |

Not yet confirmed: the janitorial $5,000 rule (ST 2002-04) and the employment services repeal date of 1 October 2021 were carried from the earlier version and its information releases, not reopened today; the McClain case reading is the Department's (ST 1999-04), not checked against the decision; the separate late filing penalty amounts for sales tax returns (as distinct from the R.C. 5739.133 assessment penalties) were not read.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `oh-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/oh-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
