---
name: wisconsin-sales-tax
description: Use this skill whenever asked about Wisconsin sales tax, Wisconsin use tax, Wisconsin sales tax nexus, Wisconsin sales tax returns, Wisconsin exemption certificates, taxability of goods or services in Wisconsin, or any request involving Wisconsin state-level consumption taxes. Trigger on phrases like "Wisconsin sales tax", "WI sales tax", "Wisconsin use tax", "Wisconsin nexus", "Wis. Stat. 77.51", "Wisconsin DOR sales tax", or any request involving Wisconsin sales and use tax filing, classification, or compliance. ALWAYS read the parent us-sales-tax skill first for federal context.
jurisdiction: US-WI
tax_year: 2026
last_updated: 2026-10-05
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Wisconsin sales and use tax: rates, taxable sales, permits, remote sellers and returns

Figures are for tax year 2026. This Guide covers Wisconsin state, county and city sales and use tax for sellers and buyers: the rates, what is taxable, the main exemptions, the seller's permit, the remote seller and marketplace rules, filing frequency, due dates, the retailer's discount, use tax and exemption certificates. Every figure comes from a Wisconsin Department of Revenue (DOR) page, retrieved 5 October 2026. Rates can change when a county adopts the tax; check the DOR rate chart before relying on a county rate. This is a working paper for review by an accountant, not a filed return. The twin Guide `wi-sales-tax` covers the same topic. For economic nexus thresholds in other states, see `us-sales-tax-nexus-50-state-matrix`; for the federal and multistate context, see `us-sales-tax`.

## Guide metadata

| Field | Value |
| --- | --- |
| Jurisdiction | Wisconsin, United States (US-WI) |
| Tax type | Sales and use tax (state, county, city of Milwaukee) |
| Law | Chapter 77, Subchapter III, Wisconsin Statutes, and chapter Tax 11, Wisconsin Administrative Code |
| Administered by | Wisconsin Department of Revenue |
| Filing system | My Tax Account (online) or TeleFile (telephone) |
| Rates and thresholds | In the sourced tables below |
| Written by | The OpenAccountants team. No accountant has reviewed this Guide yet. |

## Confidence tier definitions

- **[T1] Deterministic.** Apply as written when the facts match the condition stated.
- **[T2] Judgement.** The answer turns on facts or an interpretation. Present the options and have a CPA, EA or tax attorney confirm before filing.
- **[T3] Out of scope.** Refer to a licensed professional (see "When to refuse or refer").

## The method, step by step

1. Decide whether the seller must hold a Wisconsin seller's permit. Every person making taxable retail sales, licenses, leases or rentals of taxable products or taxable services in Wisconsin needs one. A seller with a physical presence in Wisconsin registers whatever its sales volume. A remote seller (no physical presence) registers only when it does not qualify for the small seller exception in the remote seller table below. A marketplace seller whose Wisconsin taxable sales are all facilitated by a marketplace provider does not register. See [DOR sales and use tax common questions](https://www.revenue.wi.gov/Pages/FAQS/pcs-sales.aspx) and [DOR remote sellers](https://www.revenue.wi.gov/Pages/Businesses/remote-sellers.aspx). [T1]
2. Classify each sale: tangible personal property, certain coins and stamps, certain leased property affixed to realty, certain digital goods, or a listed taxable service. If it is none of these, or an exemption applies, no tax is due. See [DOR What is taxable](https://www.revenue.wi.gov/Pages/FAQS/ise-taxable.aspx) and the taxability section below. [T1 for listed items, T2 for software and bundles]
3. Source the sale to a place. County tax applies to sales sourced to a county that adopted the county tax; city tax applies to sales to a location in the city of Milwaukee. Motor vehicles, boats, recreational vehicles and aircraft follow the county and city where they are customarily kept. See [DOR tax rates](https://www.revenue.wi.gov/Pages/FAQS/pcs-taxrates.aspx). [T1]
4. Apply the state rate plus any county and city rate from the rate tables below. Use the DOR rate lookup or rate chart for the exact address. Do not combine rates by hand for a location the chart does not cover. [T1]
5. For an exempt sale that needs a certificate, obtain a fully completed exemption certificate (Form S-211, Form S-211E or Form S-211-SST) before treating the sale as exempt. If the certificate is not fully completed, charge tax. See [Form S-211](https://www.revenue.wi.gov/DORForms/s-211f.pdf). [T1]
6. File Form ST-12 with Schedule CT for each reporting period through My Tax Account, even if no tax is due. Take the retailer's discount only if the tax is paid on time. See [Form ST-12 instructions (S-114)](https://www.revenue.wi.gov/DORForms/S-114.pdf). [T1]
7. For purchases on which no Wisconsin tax was charged and no exemption applies, report use tax: businesses on the sales and use tax return or Form UT-5; individuals on Form 1 or Form 1NPR or on Form UT-5. See [DOR use tax](https://www.revenue.wi.gov/Pages/FAQS/ise-usetax.aspx). [T1]

## Ask the client first

- Do you have any physical presence in Wisconsin (an office, staff, inventory, or sales at Wisconsin events), or do you only ship into Wisconsin? The small seller exception never applies to a seller with a physical presence.
- What were your gross sales into Wisconsin, taxable and exempt together, in the previous calendar year and so far in the current calendar year?
- Do you sell through a marketplace such as an online platform that lists your products and processes the payment? Are any of your Wisconsin sales made outside that marketplace?
- What exactly do you sell: goods, prewritten software (downloaded or remotely accessed), digital goods, or services? For remotely accessed software, who controls the servers and the software?
- Where do your Wisconsin customers take delivery: which county, and is it inside the city of Milwaukee?
- Do any customers claim an exemption (resale, manufacturing, farming, government, 501(c)(3) organization), and do you hold their completed certificates?

## Step 1: Rates

### 1.1 State, county and city rates

Wisconsin has a state sales tax and a state use tax at the same rate. Seventy counties have adopted a county tax. Milwaukee County's rate rose on January 1, 2024. The city of Milwaukee is the only municipality with a city sales and use tax, from January 1, 2024. The rate chart notes that the city of Milwaukee is located in multiple counties; it lists the city tax under Milwaukee, Washington and Waukesha counties, so use the rate lookup for a city address. The DOR rate chart shows no county rate for Waukesha County and Winnebago County. The rate chart lists Racine County's county tax from April 2025 (4/25). [T1]

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.wi.gov/Pages/FAQS/pcs-taxrates.aspx |
| State sales tax rate | 5% | "The Wisconsin sales tax is a 5% tax imposed on the sales price of retailers" |
| State use tax rate | 5% | "The Wisconsin use tax is a 5% tax imposed on the purchase price" |
| County tax rate (70 counties) | 0.5% | "Seventy Wisconsin counties have adopted a 0.5% county tax." |
| Milwaukee County rate from January 1, 2024 | 0.9% | "Milwaukee County sales and use tax increases from 0.5% to 0.9%, effective January 1, 2024." |
| City of Milwaukee rate from January 1, 2024 | 2% | "The 2% city of Milwaukee sales and use tax is effective January 1, 2024." |

Retailers that hold or must hold a Wisconsin seller's permit collect county tax and city tax on sales sourced to a county or city that adopted the tax, wherever the retailer is located. [T1]

### 1.2 Other local taxes a seller may meet

The county page lists the possible rates, including taxes outside the county and city sales tax. The premier resort area tax applies only in a premier resort area and only to sellers in certain Standard Industrial Classification codes. The same page lists local exposition taxes (basic room tax, additional room tax in the city of Milwaukee only, food and beverage tax, rental car tax). These are separate from the county and city tax and are not covered further in this Guide. [T2]

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.wi.gov/Pages/FAQS/pcs-county.aspx |
| County tax: the two county rates | 0.5% or 0.9% | "County sales and use tax (0.5% or 0.9%)" |
| City of Milwaukee | 2% | "City of Milwaukee sales and use tax (2%)" |
| Premier resort area tax (two possible rates) | 0.5% or 1.25% | "Premier resort area tax (0.5% or 1.25%)" |

The county page also lists the start dates: "Beginning April 1, 2025, Racine County imposes a 0.5% county sales and use tax. Beginning January 1, 2025, Manitowoc County imposes a 0.5% county sales and use tax."

### 1.3 Published bracket rates

DOR publishes Form 213 bracket tables for four rates. These are the rate totals DOR prints for retailers; this Guide does not compute any other total. [T1]

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.wi.gov/DORforms/s-203.pdf |
| Bracket rate | 5.5% | "brackets are available for the 5%, 5.5%, 5.9%, and 7.9% rates" |
| Bracket rate | 5.9% | "brackets are available for the 5%, 5.5%, 5.9%, and 7.9% rates" |
| Bracket rate | 7.9% | "brackets are available for the 5%, 5.5%, 5.9%, and 7.9% rates" |
| Maximum security deposit DOR may require | USD 15,000 | "deposit security, not in excess of $15,000, before a permit is issued or any time thereafter" |

### 1.4 Sourcing

- Sales are sourced to where they take place. County tax is due on taxable sales "sourced to (i.e., take place in) a county that adopted the county tax". [T1]
- Motor vehicles, boats, recreational vehicles and aircraft are taxed for county and city purposes by the county and city where the item is customarily kept. Snowmobiles, trailers, semitrailers, ATVs, UTVs and off-highway motorcycles are taxed where the buyer receives possession. See [DOR use tax](https://www.revenue.wi.gov/Pages/FAQS/ise-usetax.aspx). [T1]
- Prewritten software delivered electronically is sourced to where the purchaser receives it, under sec. 77.522, Wis. Stats. A buyer that uses the software in Wisconsin owes Wisconsin use tax even when the sale was sourced elsewhere, with credit for tax properly paid to the other state. See [DOR computer hardware, software and services](https://www.revenue.wi.gov/Pages/FAQS/pcs-computerc.aspx). [T2]

## Step 2: What is taxable

### 2.1 General rule

Sales tax applies to retail sales, licenses, leases and rentals in Wisconsin of tangible personal property, certain coins and stamps, certain leased property affixed to real property, and certain digital goods, and to listed services, unless an exemption applies. Tangible personal property includes clothing, computers, electricity, gas, steam, water, and prewritten computer software regardless of how it is delivered. See [DOR What is taxable](https://www.revenue.wi.gov/Pages/FAQS/ise-taxable.aspx). [T1]

Clothing has no general exemption in Wisconsin: DOR lists clothing as tangible personal property and as an example of an item subject to use tax. [T1]

### 2.2 Taxable services (DOR list)

| Service | Taxable? |
| --- | --- |
| Admissions and access to amusement, athletic, entertainment or recreational places or events | Yes |
| Access or use of amusement devices | Yes |
| Boat docking and storage | Yes |
| Cable television services | Yes |
| Contracts for future performance of services | Yes |
| Fabricating, processing and printing | Yes |
| Landscaping and lawn maintenance services | Yes |
| Laundry and dry cleaning services | Yes |
| Parking for motor vehicles and aircraft | Yes |
| Photographic services | Yes |
| Repair and service of tangible personal property, items, property or goods | Yes |
| Rooms or lodging for less than one month | Yes |
| Telecommunications message services and telecommunications services, including prepaid calling and ancillary services | Yes |
| Towing and hauling of motor vehicles by a tow truck | Yes |
| Services not on this list (for example legal, accounting or medical services) | No, unless another rule applies |

Source: [DOR What is taxable](https://www.revenue.wi.gov/Pages/FAQS/ise-taxable.aspx). DOR's ST-12 instructions list "charges for certain professional services such as legal, accounting, or medical services" among exempt sales ([S-114](https://www.revenue.wi.gov/DORForms/S-114.pdf)). [T1]

Delivery charges: when the product or service sold is taxable, the retailer's total charge including delivery is taxable, whoever makes the delivery. Exceptions: separately stated delivery charges for direct mail, and delivery charges the Wisconsin buyer pays to a carrier independent of the seller. [T1]

### 2.3 Software, SaaS and digital goods

- **Prewritten software** is tangible personal property, whether delivered on physical media or by download, and its sale, license, lease or rental sourced to Wisconsin is taxable unless an exemption applies. [T1]
- **Remotely accessed software ("cloud computing" or SaaS)** is a nontaxable data processing service only when all three conditions on the DOR page are met: (1) the customer's people are not on the premises where the equipment and software are and do not operate or control it, AND (2) any software downloaded to the customer is incidental (used only to reach the provider's hardware and software), AND (3) the provider is not also providing a taxable product or service in the transaction. If the customer controls the hardware and software (for example loads its own software, has unlimited server access and runs its own security), DOR treats it as a taxable lease or license of software. See [DOR computer hardware, software and services](https://www.revenue.wi.gov/Pages/FAQS/pcs-computerc.aspx). [T2]
- **Internet access services** are not taxable beginning July 1, 2020. Website design is not a taxable service unless it is primarily a photographic service. [T1]
- **Digital goods** are taxable when they are specified digital goods (digital audio works, digital audiovisual works and digital books) or additional digital goods transferred electronically (greeting cards, finished artwork, periodicals, video or electronic games, and newspapers or other news or information products). A digital code is treated the same as the goods it relates to. See [DOR Publication 240](https://www.revenue.wi.gov/DOR%20Publications/pb240.pdf). [T1]

## Step 3: Main exemptions

| Exemption | Condition | Source |
| --- | --- | --- |
| Food and food ingredients for human consumption | Does not include alcoholic beverages, tobacco products, candy, soft drinks, dietary supplements and prepared foods | [S-114](https://www.revenue.wi.gov/DORForms/S-114.pdf) |
| Prescription drugs, newspapers, corrective eyeglasses, caskets, crutches, wheelchairs, hearing aids, artificial teeth | Listed as exempt sales on line 3 of Form ST-12 | [S-114](https://www.revenue.wi.gov/DORForms/S-114.pdf) |
| Motor fuel (gas and clear diesel), alternate fuel, general aviation fuel | Only when subject to the Wisconsin motor vehicle fuel tax | [S-114](https://www.revenue.wi.gov/DORForms/S-114.pdf) |
| Electricity and natural gas for residential use | From October 1, 2025, exempt regardless of the month sold (before that, only November to April). Residential use means use in a person's permanent residence, not transient accommodations, motor homes, travel trailers or other recreational vehicles. Electricity or natural gas is considered sold at the time of billing. Other use is taxable unless another exemption applies; for example, Form S-211 lists fuel and electricity consumed in manufacturing. | [Wisconsin Tax Bulletin 230](https://www.revenue.wi.gov/WisconsinTaxBulletin/230-07-31-WTB.pdf) |
| Manufacturing | Machines and specific processing equipment used exclusively and directly by a manufacturer in manufacturing tangible personal property, and property that becomes an ingredient or component of, or is consumed in making, an article destined for sale. Tools used to repair exempt machines are not exempt. Claimed on Form S-211. | [S-211](https://www.revenue.wi.gov/DORForms/s-211f.pdf) |
| Farming | Items used exclusively and directly in the business of farming (tractors other than lawn and garden tractors, farm machines, feed, seed, fertilizer, livestock and others on the form). Claimed on Form S-211. | [S-211](https://www.revenue.wi.gov/DORForms/s-211f.pdf) |
| Governments and exempt organizations | The United States and its unincorporated agencies, federally recognized tribes in Wisconsin, Wisconsin governmental units, and 501(c)(3) organizations (Wisconsin organizations enter a CES number). Claimed on Form S-211. | [S-211](https://www.revenue.wi.gov/DORForms/s-211f.pdf) |
| Resale | The buyer enters its seller's permit or use tax certificate number on Form S-211 | [S-211](https://www.revenue.wi.gov/DORForms/s-211f.pdf) |

If a sale is exempt from the state tax, it is also exempt from the county and city tax ([S-114](https://www.revenue.wi.gov/DORForms/S-114.pdf)). [T1]

## Step 4: Seller's permit, remote sellers and marketplaces

### 4.1 Seller's permit and registration fee

Every person making taxable retail sales, licenses, leases or rentals of taxable products or taxable services in Wisconsin must have a seller's permit. Register online through DOR's business tax registration (BTR). A separate permit is issued for each business location ([S-203](https://www.revenue.wi.gov/DORforms/s-203.pdf)). [T1]

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.wi.gov/Pages/FAQS/pcs-btr.aspx |
| Initial business tax registration fee (covers two years) | USD 20 | "The initial BTR fee of $20 covers a period of two years." |
| Renewal fee for each following two-year period | USD 10 | "a $10 BTR renewal fee applies for the next two-year period" |

### 4.2 Remote sellers (economic nexus)

Since October 1, 2018, Wisconsin requires remote sellers to collect and remit tax. From February 20, 2021 (2021 Wis. Act 1) there is no transaction-count test: the 200-transaction threshold was eliminated, and the test uses calendar years. A remote seller must register and collect only if its gross sales into Wisconsin exceed the amount in the table in the previous OR the current calendar year. Gross sales include sales for resale, taxable and exempt sales. A remote seller that does not qualify for the small seller exception but only makes nontaxable sales in Wisconsin is not required to register, for example a wholesaler that only sells for resale. If it makes taxable sales to end users, it must register and collect unless an exemption applies ([DOR remote sellers common questions](https://www.revenue.wi.gov/Pages/FAQS/ise-remote-sellers.aspx)). The exception does not apply to sellers with a physical presence in Wisconsin, or to holders of a wine direct shipper's permit. [T1]

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.wi.gov/Pages/Businesses/remote-sellers.aspx |
| Small seller exception: gross sales into Wisconsin, previous or current calendar year | USD 100,000 | "required to collect and remit sales or use tax if its gross sales into Wisconsin exceed $100,000 in the previous or current calendar year" |

The direction matters: a remote seller with gross sales of exactly the threshold amount or less in BOTH years qualifies for the exception; the duty starts only when sales exceed it in either year ([DOR remote sellers common questions](https://www.revenue.wi.gov/Pages/FAQS/ise-remote-sellers.aspx)). The gross sales count also includes sales into Wisconsin made by the remote seller on behalf of other sellers and sales made by another seller on its behalf. Remote sellers may register directly with Wisconsin or through the Streamlined Sales Tax Registration System. Registered remote sellers collect the county and city tax too. [T1]

### 4.3 Marketplace providers and marketplace sellers

- From January 1, 2020, a marketplace provider must collect and remit Wisconsin sales or use tax on all taxable sales it facilitates for marketplace sellers, unless DOR has granted it a waiver under sec. 77.52(3m)(b) or (c), Wis. Stats. ([DOR sales and use tax common questions](https://www.revenue.wi.gov/Pages/FAQS/pcs-sales.aspx)). A marketplace provider with no physical presence in Wisconsin must register and collect unless it qualifies for the small seller exception in sec. 77.51(13gm), Wis. Stats. ([DOR marketplace provider common questions](https://www.revenue.wi.gov/Pages/FAQS/ise-marketplace-providers.aspx)). [T1]
- A marketplace provider is a person who facilitates a retail sale for another seller by listing or advertising the seller's taxable products or services AND, directly or indirectly, processes the payment, whether or not it is paid for doing so. [T1]
- Tax is due on the entire amount charged to the buyer, including any fee the marketplace provider charges for facilitating the sale, and including lodging sales. The provider also collects county and city tax (city from January 1, 2024), and keeps fully completed exemption certificates for exempt facilitated sales. See [DOR marketplace provider common questions](https://www.revenue.wi.gov/Pages/FAQS/ise-marketplace-providers.aspx). [T1]
- A marketplace seller does not register if all its Wisconsin taxable sales are facilitated by a marketplace provider. It must register and collect on any Wisconsin taxable sales made outside the marketplace. See [DOR marketplace seller common questions](https://www.revenue.wi.gov/Pages/FAQS/ise-marketplace-sellers.aspx). [T1]

## Step 5: Returns, due dates and the retailer's discount

### 5.1 Filing frequency

DOR sets each filer's frequency: early monthly, monthly, quarterly or annual. The annual review is based on remittances for the 12 months ending October 31; affected filers get a letter by the end of November, and the change first applies to periods beginning January 1. A filer may ask to keep a more frequent status ("Keep Filing Frequency" in My Tax Account, available until December 31). Requests to file less often are generally not allowed. Remote sellers get a frequency based on their registration information. [T1]

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.wi.gov/Pages/Businesses/Filing-Frequency-Changes.aspx |
| Early monthly: remittances per quarter | USD 3,601 or more | "$3,601 or more/quarter Monthly $1,201 - $3,600/quarter" |
| Monthly: remittances per quarter | USD 1,201 to USD 3,600 | "$1,201 - $3,600/quarter Quarterly $601 - $1,200/quarter" |
| Quarterly: remittances per quarter | USD 601 to USD 1,200 | "$601 - $1,200/quarter Annual $600/year or less" |
| Annual: remittances per year | USD 600 or less | "$600/year or less" |

### 5.2 Due dates and how to file

- Returns are due by the last day of the month after the end of the reporting period. Early monthly filers file by the 20th of the month after the period (a February return is due March 20). When the due date falls on a weekend or legal holiday, it moves to the next business day. [T1]
- File through My Tax Account or TeleFile; electronic filing is mandated for all sales and use tax registrants ([S-203](https://www.revenue.wi.gov/DORforms/s-203.pdf)). Electronic returns and ACH debit payments must be received by 4:00 p.m. (CST) on the due date. [T1]
- A return is due for every period, even with no tax to report. Report all locations on one consolidated Form ST-12; report county and city tax on Schedule CT. Keep a copy of each return for at least four years ([S-114](https://www.revenue.wi.gov/DORForms/S-114.pdf)). [T1]
- Extension: DOR may grant one additional month from the original due date. Tax unpaid by the original due date carries interest during the extension and a higher rate after it (table below). [T1]

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.wi.gov/Pages/FAQS/pcs-sales.aspx |
| Interest during an extension period | 1% per month | "subject to 1% interest per month during the extension period and 1.5% interest per month thereafter" |
| Interest after the extension period | 1.5% per month | "1.5% interest per month thereafter" |

A return not filed by the due date carries interest on the tax due from the due date of the return to the date the tax is paid. A return filed after the due date also carries a late filing fee and a negligence penalty for each month or fraction of a month it is late, up to the maximum in the table below. DOR may waive the fee and penalty on the death of the person required to file, or where a reasonable explanation exists for the late filing. Other penalties are not printed on the pages read for this Guide; see "When to refuse or refer". [T1]

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.wi.gov/DORForms/S-114.pdf |
| Interest on a return not filed by the due date, per month | 1.5% | "at the rate of 1.5% per month from the due" |
| Late filing fee | USD 20 | "Late filing fee ($20) and negligence penalty: Returns" |
| Negligence penalty, per month or fraction of a month late, on the tax due on line 22 | 5% | "negligence penalty equal to 5% of the amount on line 22 (total" |
| Maximum negligence penalty | 25% | "the return is late, up to a maximum penalty of 25%." |

### 5.3 County and city lines on Form ST-12

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.wi.gov/DORForms/S-114.pdf |
| County rate, other than Milwaukee County | 0.5% | "0.5% county (not including Milwaukee County)" |
| Milwaukee County only | 0.9% | "0.9% Milwaukee County only" |
| City of Milwaukee only | 2.0% | "2.0% city of Milwaukee only" |

### 5.4 Retailer's discount (taxes payable on or after October 1, 2023)

The discount is computed on the total sales tax on line 14 of Form ST-12. It is allowed only on timely reported tax paid by the due date, or before the end of an extension period if one was granted. It is not a flat percentage for every filer; use the bands in the table. [T1]

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.wi.gov/DORForms/S-114.pdf |
| Tax from USD 0 to USD 10 | Discount equals the tax on line 14 | "If line 14 is $0 to $10, the discount is the amount on line 14." |
| Tax from USD 10 to USD 1,333: discount | USD 10 | "If the amount on line 14 is $10 to $1,333, the discount is $10." |
| Tax greater than USD 1,333: discount is the tax times .0075, capped | USD 8,000 | "the amount on line 14 times .0075, but not exceeding $8,000." |

## Step 6: Use tax

- Use tax is due when Wisconsin sales tax (state, county or city) was not charged and no exemption applies, for example on purchases from sellers that do not collect Wisconsin tax or on items brought into Wisconsin. It applies to the same goods and services as sales tax. [T1]
- Wisconsin gives credit for sales tax properly paid to another state. Foreign taxes and customs duties do not qualify for the credit. [T1]
- County and city use tax: an item bought in a county or city without the tax and later used in a taxable county or city is generally not subject to county or city use tax. Exceptions include construction materials used to improve real property in a taxable county or city, and titled items (taxed where customarily kept). [T2]
- How to pay: individuals on Form 1 or Form 1NPR (the line for sales and use tax due on internet, mail-order, or other out-of-state purchases) or quarterly on Form UT-5; businesses on the sales and use tax return or quarterly on Form UT-5. A person who regularly owes use tax should apply for a consumer's use tax certificate ([DOR sales and use tax common questions](https://www.revenue.wi.gov/Pages/FAQS/pcs-sales.aspx)). [T1]

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.wi.gov/Pages/FAQS/ise-usetax.aspx |
| State use tax rate | 5.0% | "State 5.0% County 0.5% - 0.9% City of Milwaukee 2.0%" |
| County use tax range | 0.5% - 0.9% | "County 0.5% - 0.9% City of Milwaukee 2.0%" |
| DOR's example: camera shipped to a home in Dane County | 5.5% | "The use tax rate is 5.5% (5% state tax plus 0.5% Dane County tax)." |

## Step 7: Exemption certificates (Form S-211)

- The buyer completes Form S-211 (or S-211E, the electronic version, or S-211-SST, the Streamlined form) and gives it to the seller; it is not sent to DOR. It can cover a single purchase or be continuous. [T1]
- The seller must charge tax if the certificate is not fully completed, and keeps the certificate with its records. [T1]
- A registered seller buys goods for resale without tax by giving the supplier a completed certificate showing its tax account number. Goods not resold cannot be bought tax-free unless another exemption applies ([S-203](https://www.revenue.wi.gov/DORforms/s-203.pdf)). [T1]
- If the buyer later uses the item in a non-exempt way, the buyer owes use tax at the time of first taxable use. [T1]
- A seller who accepts a certificate after the sale can deduct the sale on the return for the period in which it receives the certificate, if it refunded the tax to the buyer and the conditions on Form ST-12 line 2 are met ([S-114](https://www.revenue.wi.gov/DORForms/S-114.pdf)). [T2]

| Item | Value | Note (verbatim from the page) |
| --- | --- | --- |
| Source | all figures below | https://www.revenue.wi.gov/DORForms/s-211f.pdf |
| Fine for using the certificate to avoid sales tax, per transaction | USD 250 | "may result in a fine of $250 for each transaction for which the certificate is used" |

## Prohibitions

1. Never say Wisconsin has no city sales tax. The city of Milwaukee has one from January 1, 2024. [T1]
2. Never apply one county rate to every county. Milwaukee County's rate differs and some counties have no county tax. [T1]
3. Never apply a transaction-count test to Wisconsin economic nexus for periods from February 20, 2021. [T1]
4. Never use the small seller exception for a seller with a physical presence in Wisconsin. [T1]
5. Never call SaaS automatically nontaxable. It is nontaxable only when all three DOR conditions are met. [T2]
6. Never treat clothing as exempt. [T1]
7. Never apply the pre-October 2023 retailer's discount bands to tax payable from October 1, 2023. [T1]
8. Never treat residential electricity or natural gas sold from October 1, 2025 as taxable because of the month. [T1]
9. Never compute a combined rate that DOR does not print. Use the rate chart or rate lookup. [T1]

## Edge case registry

### Manufacturing [T2]
The S-211 manufacturing exemption requires use "exclusively and directly" by a manufacturer in manufacturing. Equipment with a non-manufacturing use may fail that test. Tools used to repair exempt machines are not exempt.

### Landscaping and lawn care [T1]
Landscaping and lawn maintenance services are on DOR's list of taxable services.

### Construction materials [T2]
Construction materials bought in a county or city without the tax and used to improve real property in a taxable county or city are subject to county or city use tax unless an exemption applies.

### Trade-ins [T1]
Form ST-12 line 4 lets the seller subtract trade-in allowances and cash discounts on taxable sales.

### Motor vehicles, boats and aircraft [T1]
County and city tax follows where the item is customarily kept. Sales of motor vehicles, aircraft and truck bodies to nonresidents who only remove them from Wisconsin are exempt; for boats, recreational vehicles, snowmobiles, trailers, ATVs, UTVs and off-highway motorcycles sold to nonresidents, DOR says they "are subject to Wisconsin state sales and use tax, if possession transfers in Wisconsin, county and/or city taxes may apply." The punctuation leaves open whether the possession condition governs the state tax or only the county and city tax; confirm before advising. [T2]

### Marketplace bad debts [T2]
When a marketplace provider collects for a marketplace seller, the provider may claim the bad debt deduction if either party qualifies under section 166 of the Internal Revenue Code; the marketplace seller cannot claim it for the same sale.

## Test suite

### Test 1: Rate in Dane County [T1]
**Question:** A camera is shipped to a home in Dane County and no Wisconsin tax is charged. What use tax rate applies?
**Expected answer:** The rate DOR prints for its own Dane County example in the use tax table above.

### Test 2: Remote seller below the threshold [T1]
**Question:** An out-of-state seller with no physical presence made many small sales into Wisconsin, with gross sales below the small seller amount in both years. Must it register?
**Expected answer:** No. There is no transaction-count test after February 20, 2021.

### Test 3: SaaS [T2]
**Question:** A Wisconsin business subscribes to hosted HR software. The vendor controls the servers and the software; nothing is downloaded except a browser login. Is it taxable?
**Expected answer:** Not taxable as a data processing service if all three DOR conditions are met. If the customer controls the hardware and software, it is a taxable software lease.

### Test 4: Clothing [T1]
**Question:** Is a jacket sold in Milwaukee taxable?
**Expected answer:** Yes. State tax applies, plus the county tax of the county where the jacket is delivered and, if delivered inside the city of Milwaukee, city tax. Part of the city lies outside Milwaukee County, so check the address on the rate lookup.

### Test 5: Retailer's discount [T1]
**Question:** A filer's total tax on line 14 for a period after October 1, 2023 is in the middle band. What discount applies if paid on time?
**Expected answer:** The flat amount in the retailer's discount table; nothing if paid late.

## When to refuse or refer

- Refer audits, assessments, penalties, penalty abatement and voluntary disclosure to a licensed professional. This Guide states only the late filing fee, negligence penalty and interest printed in the Form ST-12 instructions. [T3]
- Refer premier resort area tax, local exposition taxes and the state rental vehicle fee questions. [T3]
- Refer questions on sales before the dates in this Guide (for example remote sales before February 20, 2021, or Milwaukee sales before January 1, 2024) for a period-specific review. [T2]
- Refer mixed software and service bundles, and remotely accessed software where control is unclear. [T2]
- Refer multistate sourcing disputes involving three or more states. [T3]

## Reviewer escalation protocol

| Trigger | Action |
| --- | --- |
| Any [T3] item | Stop. Refer to a licensed CPA, EA or tax attorney. |
| Audit notice or assessment | Refer at once. |
| Ambiguous taxability of a product or service | Present both readings with the DOR page that supports each. |
| Rate for an address the chart does not settle | Use the DOR rate lookup and record the result. |

## Contribution notes

- To update this Guide, cite the DOR page or statute section and the date the change takes effect.
- An accountant who adopts this Guide should settle the open questions in the change notes before signing.

## Sources

- [DOR Tax Rates](https://www.revenue.wi.gov/Pages/FAQS/pcs-taxrates.aspx)
- [DOR County and City Sales and Use Taxes](https://www.revenue.wi.gov/Pages/FAQS/pcs-county.aspx)
- [DOR Sales and Use Tax Common Questions](https://www.revenue.wi.gov/Pages/FAQS/pcs-sales.aspx)
- [DOR What Is Taxable](https://www.revenue.wi.gov/Pages/FAQS/ise-taxable.aspx)
- [DOR Use Tax](https://www.revenue.wi.gov/Pages/FAQS/ise-usetax.aspx)
- [DOR Remote Sellers](https://www.revenue.wi.gov/Pages/Businesses/remote-sellers.aspx)
- [DOR Remote Sellers Common Questions](https://www.revenue.wi.gov/Pages/FAQS/ise-remote-sellers.aspx)
- [DOR Marketplace Provider Common Questions](https://www.revenue.wi.gov/Pages/FAQS/ise-marketplace-providers.aspx)
- [DOR Marketplace Seller Common Questions](https://www.revenue.wi.gov/Pages/FAQS/ise-marketplace-sellers.aspx)
- [DOR Annual Filing Frequency Scan](https://www.revenue.wi.gov/Pages/Businesses/Filing-Frequency-Changes.aspx)
- [DOR Business Tax Registration](https://www.revenue.wi.gov/Pages/FAQS/pcs-btr.aspx)
- [DOR Computer Hardware, Software, Services](https://www.revenue.wi.gov/Pages/FAQS/pcs-computerc.aspx)
- [Form S-203, Your Privileges and Obligations as a Seller](https://www.revenue.wi.gov/DORforms/s-203.pdf)
- [Form S-114, ST-12 instructions](https://www.revenue.wi.gov/DORForms/S-114.pdf)
- [Form S-211, exemption certificate](https://www.revenue.wi.gov/DORForms/s-211f.pdf)
- [Publication 240, Digital Goods](https://www.revenue.wi.gov/DOR%20Publications/pb240.pdf)
- [Wisconsin Tax Bulletin 230, July 2025](https://www.revenue.wi.gov/WisconsinTaxBulletin/230-07-31-WTB.pdf)

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date version of this Guide is maintained on the OpenAccountants website. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
