---
name: nj-sales-tax
description: New Jersey Sales and Use Tax for sellers and buyers, tax year 2026. Covers the 6.625% State rate with no local sales taxes, the Urban Enterprise Zone and Salem County half rates (3.3125%), what is taxable (tangible goods, specified digital products, listed services) and the main exemptions (most clothing, groceries, drugs, professional services, production machinery, investment bullion), remotely accessed software (SaaS) and information services, registration on NJ-REG, remote sellers (more than 100,000 dollars or 200 transactions) and marketplace facilitators, Form ST-50 quarterly returns and Monthly Vouchers, UZ-50, exemption certificates ST-3, ST-4, ST-5 and ST-SST, Use Tax and ST-18B, rounding and penalties. Trigger on "New Jersey sales tax", "NJ sales tax", "NJ use tax", "ST-50", "UEZ", "Urban Enterprise Zone", "NJ clothing exemption", "NJ remote seller", "NJ SaaS tax", "NJ Division of Taxation".
version: "3.1"
jurisdiction: US-NJ
tax_year: 2026
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
depends_on:
  - us-sales-tax
---

# New Jersey Sales and Use Tax, tax year 2026

> **Source-cited draft.** Built from the Division of Taxation's Sales and Use Tax pages (rate, remote sellers, filing, Urban Enterprise Zones, Use Tax, calculating the tax, penalties, new laws), the New Jersey Sales Tax Guide S&U-4 (Rev. 07/22), S&U-6 and Technical Bulletin TB-72, read on 2026-11-14. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** New Jersey charges one State Sales Tax of **6.625%** on most tangible personal property, specified digital products and listed services; there are no local sales taxes ([Division Sales and Use Tax page](https://www.nj.gov/treasury/taxation/businesses/salestax/index.shtml)). Certified Urban Enterprise Zone sellers charge half, **3.3125%**, on qualifying in-person sales of goods. A remote seller must register when its sales into New Jersey in the current or prior calendar year are **more than USD 100,000** or **200 or more** transactions; marketplace facilitators collect on marketplace sales ([Remote Sellers](https://www.nj.gov/treasury/taxation/remotesellers.shtml)). Every registered seller files a quarterly ST-50 by the 20th after the quarter. Most clothing and footwear, groceries and drugs are exempt. Remotely accessed software (SaaS) is generally not taxed unless it is an information service ([TB-72](https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb72.pdf)). New Jersey is a full Streamlined Sales and Use Tax member.

## Scope and who this is for

In scope: businesses selling into or within New Jersey, and New Jersey residents and businesses buying for use in New Jersey, for 2026: rate, reduced rates, taxability, registration, remote sellers and marketplaces, returns and payments, exemption certificates, Use Tax and penalties. Read `us-sales-tax` first for the multi-state framework.

Out of scope, and where it goes:

| Topic | Where |
| --- | --- |
| Hotel occupancy fee, the Newark USD 3 a day hotel surcharge from 1 January 2026 (P.L. 2025, c.158), motor vehicle, alcohol, cigarette, hemp beverage and cannabis excise taxes | Refer; not in this skill |
| New Jersey income tax on the seller's profit | `nj-income-tax` or `nj-cbt-and-bait` |
| Payroll | `nj-payroll` |

## Ask the client first

1. **Presence:** any office, staff, inventory (including in a marketplace warehouse) or other physical presence in New Jersey?
2. **If remote:** gross sales and number of separate transactions delivered into New Jersey this calendar year and last year?
3. **Channel:** marketplace, direct, or both?
4. **What is sold:** goods, clothing (including fur, sport or protective items), food, digital products, software (downloaded or accessed remotely), information services, other services?
5. **Location rules:** a certified UEZ business (UZ-2 certificate), or located in Salem County, and do the sales meet the in-person and delivery tests?
6. **Size:** how much New Jersey Sales Tax was collected last calendar year (the USD 30,000 monthly-payment test)?

## The method, step by step

### Rates, bands and thresholds

| Item | Rate or amount, 2026 | Condition | Source |
| --- | --- | --- | --- |
| State Sales Tax rate | 6.625% | Most tangible personal property, specified digital products and listed services, unless exempt | [Division Sales and Use Tax page](https://www.nj.gov/treasury/taxation/businesses/salestax/index.shtml) |
| Use Tax rate | 6.625% | Same as Sales Tax; for purchases made in 2018 and after | [Use Tax FAQ](https://www.nj.gov/treasury/taxation/su_10.shtml) |
| Urban Enterprise Zone reduced rate | 3.3125% | Certified sellers only, qualifying in-person sales of tangible personal property in the zone | [UEZ page](https://www.nj.gov/treasury/taxation/businesses/salestax/uez-over.shtml) |
| Salem County reduced rate | Half the regular rate (3.3125%, derived: half of 6.625%) | Qualifying in-person retail sales of goods from a Salem County place of business; confirm the programme is current | [S&U-4](https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf) |
| Remote seller revenue threshold | More than USD 100,000 | Sales delivered into New Jersey, current or prior calendar year | [Remote Sellers](https://www.nj.gov/treasury/taxation/remotesellers.shtml) |
| Remote seller transaction threshold | 200 or more transactions | Same period; either test is enough | same |
| Marketplace facilitator delay | Up to 180 days | On written request | same |
| Monthly payment test, prior-year collections | More than USD 30,000 | Both monthly tests must be met | [Filing and remitting](https://www.nj.gov/treasury/taxation/su_12.shtml) |
| Monthly payment test, month 1 or 2 of the quarter | More than USD 500 | Both monthly tests must be met | same |
| ST-18B business Use Tax ceiling | Average annual Use Tax under USD 2,000 over the last three years | And no taxable sales or leases, and Use Tax owed this year | [Use Tax FAQ](https://www.nj.gov/treasury/taxation/su_10.shtml) |
| Government purchase where an ST-4 may replace a purchase order | USD 150 or less | Paid by agency check, voucher or a qualifying GSA SmartPay card | [S&U-4](https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf) |
| Zero emission vehicles | 6.625% | Full rate from 1 July 2025 (3.3125% from 1 October 2024 to 30 June 2025) | [Division new laws page](https://www.nj.gov/treasury/taxation/newlegislation.shtml) |

### Step 1: must the seller collect?

- Any person engaged in business in New Jersey registers on Form NJ-REG at least 15 business days before starting business or opening another place of business; seasonal or occasional sellers at flea markets or craft shows must register too ([S&U-4](https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf); [Filing and remitting](https://www.nj.gov/treasury/taxation/su_12.shtml)).
- A **remote seller** (no physical presence) must register, collect and remit for sales on and after 1 November 2018 if, in the current or prior calendar year, its gross revenue from goods, specified digital products or taxable services delivered into New Jersey **exceeds** USD 100,000 (equal is not enough), **or** it made **200 or more** separate such transactions. A seller meeting neither test need not register ([Remote Sellers](https://www.nj.gov/treasury/taxation/remotesellers.shtml), last updated 04/24/25).
- Remote sellers register through the Division of Revenue and Enterprise Services ("Register as Remote Seller Only") or the Streamlined Sales Tax Registration System, because New Jersey is a full member of the Streamlined Sales and Use Tax Governing Board.

### Step 2: take marketplace sales out

The marketplace facilitator collects and remits on all marketplace transactions, "regardless of whether the marketplace seller is above or below either of the economic thresholds". A remote seller over the threshold that sells only through marketplaces must still register, but may ask to be placed on a non-reporting basis by mailing Form C-6205-ST to the Division of Revenue and Enterprise Services. Guidance: Technical Bulletin TB-83 ([Remote Sellers](https://www.nj.gov/treasury/taxation/remotesellers.shtml)).

### Step 3: classify each item ([S&U-4](https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf); [S&U-6](https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su6.pdf); [TB-72](https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb72.pdf))

The Sales and Use Tax Act taxes receipts from every retail sale of tangible personal property, specified digital products and certain services unless the Act exempts them. Tangible personal property includes prewritten software delivered electronically. Most services performed on tangible personal property and specified digital products are taxable unless exempt.

| Pattern | Treatment | Condition or limit |
| --- | --- | --- |
| General tangible personal property | Taxable | Unless a specific exemption applies |
| Clothing and footwear for human use | Exempt | Not "fur clothing; accessories or equipment; sport or recreational equipment, or protective equipment (unless the protective equipment is necessary for the daily work of the user)". Those are taxable; work-required protective equipment stays exempt |
| Grocery food | Exempt | "most food sold as grocery items" |
| Prepared food (heated, combined by the seller, or sold with utensils), including beverages; candy and soft drinks | Taxable | |
| Prescription drugs; over-the-counter drugs for human use | Exempt | OTC only with a label identifying the product as a drug, such as a "Drug Facts" panel or a statement of active ingredients |
| Disposable paper products for household use | Exempt | |
| Specified digital products (digital audio-visual works, audio works, books) transferred electronically | Taxable | When billed to a New Jersey address; products streamed or accessed but not delivered are not taxable |
| Prewritten software delivered electronically | Taxable when sold to individuals | Exempt under S&U-6 when "used directly and exclusively in the conduct of the purchaser's business, trade, or occupation", but not for "load and leave" delivery or software-related services |
| Software accessed remotely (SaaS, PaaS, IaaS) | Generally not taxable | TB-72: use of a software application is not a listed service, so most SaaS charges are not taxed; SaaS used to provide information (an information service, such as legal research databases) is taxable |
| Information services | Taxable | N.J.S.A. 54:32B-3(b)(12), as quoted in TB-72 |
| Data hosting | Not taxable | TB-72 |
| Purchases for resale | Exempt | With Form ST-3 |
| Professional services (doctor, lawyer, accountant) | Exempt | S&U-4 services list |
| Production machinery and equipment, and parts with a useful life over one year | Exempt | Used directly and primarily in production; not simple hand tools; claim on Form ST-4 (S&U-6) |
| Investment metal bullion and investment coins (fair market value at least USD 1,000 for coins) | Exempt | Retail sales on or after 1 January 2025 (P.L. 2024, c.64, [new laws page](https://www.nj.gov/treasury/taxation/newlegislation.shtml)) |
| Recreational cannabis sold in a UEZ | Full rate | Not eligible for the UEZ rate ([new laws page](https://www.nj.gov/treasury/taxation/newlegislation.shtml)) |
| Annual back-to-school sales tax holiday | Repealed | P.L. 2024, c.19 ([new laws page](https://www.nj.gov/treasury/taxation/newlegislation.shtml)) |

### Step 4: check for a valid exemption certificate ([S&U-4](https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf); [S&U-6](https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su6.pdf))

- The common certificates are the Resale Certificate (ST-3), the Exempt Use Certificate (ST-4) and the Exempt Organization Certificate (ST-5); the Streamlined certificate ST-SST is accepted too.
- The seller must be registered with New Jersey and should accept only a fully completed certificate. Once it is taken in good faith, the seller is relieved of collecting even if the buyer later proves ineligible.
- One certificate covers later purchases of the same general type. Keep it at least four years from the last purchase it covers.
- Government purchases of USD 150 or less may be made on a fully completed ST-4 instead of a purchase order, paid by the agency's check or voucher or a GSA SmartPay 2 card with 0, 6, 7, 8 or 9 as the sixth digit.

### Step 5: pick the rate

- **State rate** 6.625% by default.
- **Urban Enterprise Zone, 3.3125%** ([UEZ page](https://www.nj.gov/treasury/taxation/businesses/salestax/uez-over.shtml), last updated 11/13/26; [S&U-4](https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf)): only a business the UEZ Authority has certified (UZ-2 certificate); only tangible personal property, not services; the buyer places the order in person at the seller's zone location **and** either accepts delivery there **or** the seller delivers from its zone location, "not from another location". Certification is online through the UEZ Business Certification System; an annual report is due and recertification every three years. Qualified UEZ businesses may also buy most items (not motor vehicles or energy) and most services (not telecommunications or utilities) exempt, within the purchase limitations in the UEZ notices.
- **Salem County, half rate** ([S&U-4](https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf), Rev. 07/22): retail sales of goods made in person from a place of business regularly operated for retail sales, with delivery at or from the Salem County location. Not eligible include motor vehicles, alcoholic beverages, cigarettes, mail-order, catalog and internet sales, services, and prepared food, meals and beverages. No current Division web page on Salem County was found, so confirm the programme before applying it.

### Step 6: compute the tax ([Calculating the Tax](https://www.nj.gov/treasury/taxation/ratechange/su-calculatingthetax.shtml))

Use the Form ST-75 bracket, or multiply taxable receipts by the rate, carry to the third decimal, and round up at half a cent (USD 0.005) or more, down below it. Example on the page: USD 20 x 0.06625 = USD 1.325, collected as USD 1.33.

### Step 7: Use Tax on purchases ([Use Tax FAQ](https://www.nj.gov/treasury/taxation/su_10.shtml), last updated 03/18/26)

A New Jersey resident or business owes Use Tax on a taxable item or service bought outside New Jersey for use here if no sales tax of any kind was paid, or sales tax was paid elsewhere at a lower rate; in the second case only the difference is due. No credit is allowed for sales tax paid to a foreign country (S&U-4). Individuals report it on Form NJ-1040 (or Form ST-18); the FAQ's estimated Use Tax chart may be used when receipts are missing. Businesses use Form ST-18B only if all three ST-18B tests in the rates table hold; otherwise they register for quarterly or monthly Sales Tax filing.

## Boundary and exception table

| Situation | Treatment | Source |
| --- | --- | --- |
| Remote seller with exactly USD 100,000 of New Jersey sales and 150 transactions | No obligation: revenue must exceed USD 100,000, transactions must reach 200 | [Remote Sellers](https://www.nj.gov/treasury/taxation/remotesellers.shtml) |
| Remote seller with 200 small orders totalling USD 8,000 (derived: example input) | Must register: either test is enough | same |
| Sells only through a marketplace, over the threshold | Register, then ask for non-reporting status on C-6205-ST | same |
| Fur coat, ski boots, bicycle helmet (not for work) | Taxable: outside the clothing exemption | [S&U-4](https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf) |
| Steel-toe boots needed for daily work | Exempt clothing | same |
| SaaS project-management subscription | Generally not taxable | [TB-72](https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb72.pdf) |
| Online legal research database subscription | Taxable information service | same |
| Downloaded software bought by a business for exclusive business use | Exempt (S&U-6 business use), not if "load and leave" | [S&U-6](https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su6.pdf) |
| Certified UEZ seller ships an online order from its warehouse outside the zone | Full 6.625%: fails the in-person and delivery tests | [S&U-4](https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf) |
| UEZ seller's repair service | Full rate: the reduced rate covers goods only | same |
| Prior-year collections exactly USD 30,000 | No Monthly Vouchers in any month: the test is "more than" | [Filing and remitting](https://www.nj.gov/treasury/taxation/su_12.shtml) |
| Monthly payer collects exactly USD 500 in a month | No voucher for that month | same |
| Error on a Monthly Voucher found after the quarter's ST-50 is filed | File an amended ST-50 | [S&U-4](https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf) |
| Desk bought in Maine with 5.5% tax, brought to New Jersey | Use Tax on the 1.125% difference (derived: 6.625% less 5.5%) | [Use Tax FAQ](https://www.nj.gov/treasury/taxation/su_10.shtml) |
| Goods bought abroad with foreign VAT | Full Use Tax: no credit for foreign sales tax | [S&U-4](https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf) |

### Defaults when a fact is missing

| Missing fact | Default, and flag it |
| --- | --- |
| Whether a SaaS product delivers information | Treat as not taxable only if it is plainly a software tool; otherwise refer |
| UEZ certificate | Full rate until a UZ-2 is seen |
| Prior-year collections | Assume quarterly only; ask before the first quarter's second month |
| Whether a buyer certificate is complete | Charge tax |

## Worked cases

**Case 1, a decision: must a remote seller register?** An online seller with no New Jersey presence shipped USD 95,000 of goods in 180 orders into New Jersey in 2025. By 30 June 2026 it has shipped USD 102,000 in 160 orders. 2025 meets neither test, so no obligation then. In 2026 revenue now exceeds USD 100,000, so it must register, collect and remit (on the transaction test alone it would not yet have to). Its third-quarter 2026 taxable New Jersey sales of USD 30,000 carry USD 1,987.50 of tax, due on the ST-50 by 20 October 2026.

```oa-check
name: NJ remote seller 2026, threshold test and quarter tax
inputs:
  revenue_2025: 95000
  orders_2025: 180
  revenue_2026: 102000
  orders_2026: 160
  q3_taxable_sales: 30000
steps:
  - over_revenue_2025: min(max(revenue_2025 - 100000, 0), 1)
  - over_orders_2025: min(max(orders_2025 - 199, 0), 1)
  - must_register_2025: max(over_revenue_2025, over_orders_2025)
  - over_revenue_2026: min(max(revenue_2026 - 100000, 0), 1)
  - over_orders_2026: min(max(orders_2026 - 199, 0), 1)
  - must_register_2026: max(over_revenue_2026, over_orders_2026)
  - q3_tax: q3_taxable_sales * 0.06625
expected:
  must_register_2025: 0
  must_register_2026: 1
  q3_tax: 1987.50
```

**Case 2: UEZ sale, monthly payments and Use Tax.** A certified UEZ furniture store sells a USD 240 lamp to a customer in person at its zone store: tax at 3.3125% is USD 7.95 (USD 15.90 at the State rate). It collected USD 34,000 of tax in 2025 (more than USD 30,000), and in January 2026 USD 620 and in February USD 450: a Monthly Voucher is due for January by 20 February; none for February, which goes on the ST-50 by 20 April. (As a UEZ business it also files UZ-50 monthly by the 20th.) The owner also brought a USD 4,000 desk from Maine, paying 5.5% Maine tax: New Jersey Use Tax is USD 265.00 less USD 220.00 = USD 45.00.

```oa-check
name: NJ 2026 UEZ rate, monthly voucher test and Use Tax difference
inputs:
  lamp_price: 240
  prior_year_collected: 34000
  january_collected: 620
  february_collected: 450
  desk_price: 4000
  maine_rate: 0.055
steps:
  - uez_tax: lamp_price * 0.033125
  - state_tax: lamp_price * 0.06625
  - big_seller: min(max(prior_year_collected - 30000, 0), 1)
  - january_voucher: big_seller * min(max(january_collected - 500, 0), 1)
  - february_voucher: big_seller * min(max(february_collected - 500, 0), 1)
  - nj_tax_on_desk: desk_price * 0.06625
  - maine_tax: desk_price * maine_rate
  - use_tax: max(nj_tax_on_desk - maine_tax, 0)
expected:
  uez_tax: 7.95
  state_tax: 15.90
  january_voucher: 1
  february_voucher: 0
  use_tax: 45.00
```

## When to refuse or refer

- SaaS or remote software that may be an information service, bundled digital offerings, or mixed software and service contracts: refer, since TB-72 (issued 2013) turns on facts.
- Salem County reduced rate claims: refer until a current Division page confirms the programme.
- UEZ certification, recertification, purchase limitations, cannabis in a UEZ, or energy exemptions for UEZ manufacturers: refer to the Department of Community Affairs and the UEZ notices.
- Audits, assessments, voluntary disclosure or penalty abatement: refer to a New Jersey practitioner.
- Hotel occupancy, the Newark hotel surcharge, motor vehicle, alcohol, cigarette and hemp beverage taxes: outside this skill.
- Never treat all clothing as exempt, never apply the UEZ rate without a UZ-2 certificate or to services, and never compute tax except by the published rate and rounding rule.

## Filing and payment

Sources: [Filing and remitting](https://www.nj.gov/treasury/taxation/su_12.shtml); [S&U-4](https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf); [penalties page](https://www.nj.gov/treasury/taxation/njit19.shtml).

1. Log in to the **New Jersey Tax Portal** (nj.gov/taxation) with the New Jersey registration.
2. **Monthly Voucher** (Form Type: Monthly Voucher) for month 1 and month 2 of a quarter, only if both monthly tests are met; due the 20th of the next month. It is a payment only and cannot be filed for zero. A seller that collected USD 30,000 or less last year makes no monthly payments, "no matter how much tax is due for that particular month".
3. **Form ST-50**, quarterly, for every registered seller even with no sales: report gross receipts, deductions and taxable receipts and the tax, then subtract the Monthly Vouchers already paid. Due 20 April, 20 July, 20 October and 20 January; a weekend or legal holiday moves it to the next business day. For 2026: 20 April, 20 July, 20 October 2026 and 20 January 2027.
4. **UZ-50** monthly by the 20th for UEZ businesses.
5. **Pay** by e-check, electronic funds transfer, or credit card (fees apply). Keep the confirmation.
6. **Corrections:** a Monthly Voucher error may be corrected on the ST-50 only within the same quarter; after that, amend the ST-50.

**Penalties and interest** (the Division's penalties page, last updated 05/18/26):

| Item | Rate or amount | Source |
| --- | --- | --- |
| Late filing penalty | 5% of the tax due per month or part month, up to 25% | [Penalties page](https://www.nj.gov/treasury/taxation/njit19.shtml) |
| Additional late filing charge | USD 100 per month late | same |
| Late payment penalty | 5% of the tax due | same |
| Interest | Prime rate plus 3%, compounded annually (TB-21(R)) | same |
| Referral cost recovery fee (collection agency) | 9.85% from 15 June 2026 (11% before) | same |

Penalties may be abated for reasonable cause.

## Completion checklist

- [ ] Physical presence tested; remote seller revenue (more than USD 100,000) and transaction (200 or more) tests run for the current and prior year.
- [ ] Marketplace sales excluded; non-reporting request filed if all sales are on marketplaces.
- [ ] Each item classified: clothing carve-outs, digital products, software delivered or accessed remotely, information services, bullion.
- [ ] Exemption certificates complete and kept four years.
- [ ] Rate checked: UEZ only with a UZ-2 and the in-person and delivery tests; Salem County only once confirmed.
- [ ] Tax rounded at the third decimal or by ST-75.
- [ ] Monthly Vouchers only when both tests are met; ST-50 filed every quarter by the 20th; UZ-50 monthly for UEZ sellers.
- [ ] Use Tax assessed on untaxed or under-taxed purchases; ST-18B only if all three tests hold.

## Sources

| Source | URL | Read on |
|---|---|---|
| Division Sales and Use Tax page (last updated 11/13/26); read for the 6.625% rate and recent topics | https://www.nj.gov/treasury/taxation/businesses/salestax/index.shtml | 2026-11-14 |
| Division Remote Sellers page (last updated 04/24/25); read for the USD 100,000 and 200 transaction tests, marketplaces, C-6205-ST, SST membership and the 180-day delay | https://www.nj.gov/treasury/taxation/remotesellers.shtml | 2026-11-14 |
| Division Filing and Remitting page; read for the ST-50 and Monthly Voucher chart and the USD 30,000 and USD 500 tests | https://www.nj.gov/treasury/taxation/su_12.shtml | 2026-11-14 |
| Division Urban Enterprise Zone page (last updated 11/13/26); read for the 3.3125% rate, certification and UZ-50 | https://www.nj.gov/treasury/taxation/businesses/salestax/uez-over.shtml | 2026-11-14 |
| Division Use Tax FAQ (last updated 03/18/26); read for Use Tax, the examples, ST-18B and ST-18 | https://www.nj.gov/treasury/taxation/su_10.shtml | 2026-11-14 |
| Division Calculating the Tax page; read for the rounding rule and ST-75 | https://www.nj.gov/treasury/taxation/ratechange/su-calculatingthetax.shtml | 2026-11-14 |
| Division penalties, interest and collection fees page; read for penalties, interest and the collection fee | https://www.nj.gov/treasury/taxation/njit19.shtml | 2026-11-14 |
| Division new laws page; read for P.L. 2024, c.19 (zero emission vehicles, holiday repeal), P.L. 2024, c.64 (bullion), P.L. 2025, c.158 (Newark hotel surcharge) and the UEZ cannabis rule | https://www.nj.gov/treasury/taxation/newlegislation.shtml | 2026-11-14 |
| S&U-4 New Jersey Sales Tax Guide (Rev. 07/22); read for the taxable base, clothing, drugs, digital products, Salem County, UEZ tests, NJ-REG, certificates, the USD 150 rule and corrections | https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su4.pdf | 2026-11-14 |
| S&U-6 Sales Tax Exemption Administration; read for the software business use and production machinery exemptions | https://www.nj.gov/treasury/taxation/pdf/pubs/sales/su6.pdf | 2026-11-14 |
| TB-72 Cloud Computing (issued 3 July 2013); read for SaaS, PaaS, IaaS, information services and data hosting | https://www.nj.gov/treasury/taxation/pdf/pubs/tb/tb72.pdf | 2026-11-14 |

Not yet confirmed: whether the Salem County reduced rate programme is still running in 2026 (S&U-4 dated 07/22 describes it; no current Division page found); whether a revised TB-72 exists (the address tb72r.pdf returned no document, so the 2013 bulletin is used); whether the penalties page, published under individual income tax, applies unchanged to Sales Tax returns; the 2026 prime rate for interest; the Form ST-50 line numbers for 2026.
