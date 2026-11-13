---
name: us-sales-tax-nexus-50-state-matrix
description: The post-Wayfair economic nexus test of every US sales tax state and DC for tax year 2026, each row linked to that state's own source. Gives the sales test, transaction test (if any), measuring period, which sales count and the marketplace facilitator start date, with the five states that have no general sales tax, physical presence through marketplace inventory, and start-collecting rules. Trigger on "economic nexus", "Wayfair threshold", "do I need to register for sales tax in", "remote seller threshold", "marketplace facilitator", "200 transactions". Load us-sales-tax for the framework and the state sales tax skill for rates and returns.
version: "3.0"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: cross-country-method
---

# US sales tax economic nexus: state-by-state thresholds for 2026

> **Source-cited draft.** Each row is linked to that state's own revenue department page, statute or bulletin. Rows for states rewritten on 13 November 2026 (Arkansas, Idaho, Louisiana, Massachusetts, New York, Texas and others) take their figures from those state skills. Other rows were read on 25 September 2026 and their links re-checked on 13 November 2026. No accountant has reviewed it.

Where a row could not be confirmed it says **check**, still links the state's page, and is listed on the "Not yet confirmed:" line under Sources.

## Scope and who this is for

This skill answers one question for a seller with no physical presence in a state: has it crossed that state's economic nexus threshold, so that it must register, collect and file sales tax (or Hawaii general excise tax, or New Mexico gross receipts tax)?

It covers the 45 states with a statewide sales tax and the District of Columbia (threshold, transaction test, "more than" or "at least", period, which sales count, marketplace facilitator start date), the five states with no general sales tax, and how physical presence overrides the thresholds.

It does not cover taxability, rates or sourcing; income or franchise tax nexus (except the P.L. 86-272 point below); Puerto Rico and the territories; local home-rule registrations; or voluntary disclosure and back-tax exposure (see "When to refuse or refer").

The Washington and Pennsylvania rows match the separate Washington and Pennsylvania sales tax Guides.

## Ask the client first

- Which states did you ship goods to, or deliver services or digital products into, in 2025 and so far in 2026?
- For each state: total sales in dollars and number of separate transactions, split by calendar year **and** by month (several states use a rolling 12 months or four quarters, not calendar years).
- How much of that went through a marketplace (Amazon, eBay, Etsy, Walmart and similar) and how much was direct (own website, wholesale, phone)?
- Of the direct sales, how much was exempt, for resale, or wholesale?
- Do you, or any company related to you, have anything in any state: employees, contractors, an office, a warehouse, or inventory in a marketplace's fulfilment centre?
- Are you already registered anywhere? Since when?
- Do related companies also sell into these states? (Arizona and California add their sales.)

## The method, step by step

1. **Check physical presence first.** Any physical presence in a state means you register there whatever your sales. Inventory counts: Connecticut says an out-of-state retailer with goods "on the premises of a marketplace facilitator" must register "even if it is under the thresholds" ([Connecticut DRS](https://portal.ct.gov/drs/businesses/new-business-resource-center/registering-with-drs)). If you skip this step, the threshold analysis gives false comfort.
2. **Build the sales data the way each state measures it.** Use the table below to see which sales count (gross or retail or taxable; marketplace sales in or out) and over which period (previous year, current year, rolling 12 months, four quarters, 12 months to 30 September). Do not reuse one national total.
3. **Apply each state's test literally.** Note whether it is "more than" or "at least", and whether a transaction count still exists and whether it is an OR test or an AND test (Connecticut and New York need both).
4. **Find the start date.** Crossing the threshold does not always mean collecting from the next sale. Most states give a lead time (first day of a month at least 30 days later; 90 days in Colorado; the fourth month in Texas; 1 April of the next year in Pennsylvania). Use the start rule in the "Filing and payment" section.
5. **Handle marketplace sales.** A facilitator collects on the sales it facilitates. Some states still require the seller to register if its total, including marketplace sales, crosses the threshold (for example South Dakota, Washington, Nebraska, Maryland). Others let the seller leave facilitated sales out (for example Georgia, Arizona, Oklahoma, and Pennsylvania where the facilitator collects).
6. **Mark every "check" state for follow-up.** Confirm those on the state's site before advising; do not fill the gap from memory or a vendor chart.
7. **Re-test on the state's own cycle.** Monthly for Vermont, quarterly for Illinois, Missouri and New York, and yearly for calendar-year states. A seller under the threshold in January can be over it in June.

## Background

- **Wayfair.** In *South Dakota v. Wayfair* (2018) the Supreme Court overruled the physical-presence rule of *Quill*. It upheld a law covering sellers that "deliver more than $100,000 of goods or services into the State or engage in 200 or more separate transactions" ([Wayfair opinion](https://www.supremecourt.gov/opinions/17pdf/17-494_j4el.pdf)). Every state with a sales tax now has an economic nexus rule, but most have since changed the details. Many have dropped the 200-transaction test.
- **P.L. 86-272 does not protect you from sales tax.** It limits state **income** taxes where your only in-state activity is "the solicitation of orders" for tangible personal property filled from outside the state ([15 U.S.C. 381](https://www.govinfo.gov/content/pkg/USCODE-2024-title15/html/USCODE-2024-title15-chap10B-sec381.htm)). It says nothing about sales tax collection.

## State threshold table for 2026

Read "Sales test" literally: "more than" means exactly the threshold does **not** trigger; "at least" or "or more" means it does. "Prev or current" means the test is met if either the previous calendar year or the current calendar year crosses it. "MPF" is the marketplace facilitator collection start date; "check" means the source reviewed did not give it.

| State | Sales test | Transaction test | Period | Which sales count | MPF start | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Alabama | Over $250,000 | None | Previous calendar year | Retail sales made directly by the seller, taxable and nontaxable; leave out wholesale sales backed by an Alabama resale licence and sales through a marketplace collecting under the Simplified Sellers Use Tax (SSUT) programme | 1 Jan 2019 | [ALDOR FAQ](https://www.revenue.alabama.gov/faqs/are-all-remote-sellers-required-to-register-in-alabama/), [SSUT](https://www.revenue.alabama.gov/sales-use/simplified-sellers-use-tax-ssut/) |
| Arizona (TPT) | More than $100,000 (2021 onward) | None | Prev or current | Gross proceeds from direct business with Arizona customers **not** facilitated by a marketplace facilitator; affiliated persons' sales added | check | [A.R.S. 42-5044](https://www.azleg.gov/ars/42/05044.htm) |
| Arkansas | Exceeding $100,000 | Or exceeding 200 transactions | Previous or current calendar year | Taxable Arkansas sales of goods, taxable services, digital codes and specified digital products | 1 Jul 2019 | [Act 822 of 2019, section 19](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2019R%2FPublic%2FACT822.pdf), [DFA remote sellers](https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/remote-sellers/) |
| California | Exceeds $500,000 | None | Preceding or current calendar year | All sales of tangible goods for delivery in California by the retailer **and all related persons**, including nontaxable sales such as sales for resale, and including sales facilitated through a marketplace | 1 Oct 2019 | [CDTFA Wayfair guide](https://www.cdtfa.ca.gov/industry/wayfair.htm), [Wayfair FAQ](https://www.cdtfa.ca.gov/industry/wayfair/frequently-asked-questions.htm), [Marketplace Facilitator Act guide](https://www.cdtfa.ca.gov/industry/MPFAct.htm) |
| Colorado | Exceeds $100,000 | None | Prev or current | Retail sales of goods, commodities and services into Colorado | check | [CDOR out-of-state businesses](https://tax.colorado.gov/out-of-state-businesses) |
| Connecticut | At least $100,000 **and** | 200 or more retail sales (both needed) | 12 months ending 30 September before the filing period | Gross receipts from sales into Connecticut | 1 Dec 2018 | [DRS registering](https://portal.ct.gov/drs/businesses/new-business-resource-center/registering-with-drs), [OCG-8](https://portal.ct.gov/-/media/DRS/Publications/OCG/OCG-8.pdf?la=en) |
| District of Columbia | More than $100,000 | Or more than 200 separate retail sales | Prev or current | Gross receipts from retail sales delivered into DC | 1 Apr 2019 | [OTR FAQ](https://otr.cfo.dc.gov/page/sales-and-use-tax-faqs) |
| Florida | Taxable remote sales exceeding $100,000 | None | Previous calendar year | **Taxable** remote sales only | 1 Jul 2021 | [FDOR sales tax](https://floridarevenue.com/taxes/taxesfees/Pages/sales_tax.aspx), [FDOR notice 21A01-03](https://floridarevenue.com/taxes/tips/Documents/TIP_21A01-03.pdf) |
| Georgia | Exceeding $100,000 | Or 200 or more separate retail sales | Prev or current | Retail sales of tangible goods delivered into Georgia; a remote seller may leave out facilitated sales | 1 Apr 2020 | [SUT-2019-02](https://dor.georgia.gov/media/35301/download), [SUT-2020-01](https://dor.georgia.gov/media/35306/download) |
| Hawaii (GET) | $100,000 or more | Or 200 or more separate transactions | Current or immediately preceding calendar year | Gross income from goods delivered, services used and intangibles used in Hawaii | 1 Jan 2020 | [Haw. Rev. Stat. 237-2.5](https://files.hawaii.gov/tax/legal/hrs/hrs_237.pdf), [Hawaii release 2019-03](https://files.hawaii.gov/tax/legal/tir/tir19-03_rev2.pdf) |
| Idaho | Exceed $100,000 | None | Current or previous calendar year | Idaho sales; a marketplace facilitator combines its own and third-party sales | check | [Idaho Tax Commission, online sellers](https://tax.idaho.gov/taxes/sales-use/guides-for-certain-groups/online-sellers/online-guide/) |
| Illinois | $100,000 or more | None from 1 Jan 2026 (200 or more before) | 12-month lookback, re-tested each quarter | Cumulative gross receipts from sales of tangible goods to Illinois purchasers | check | [IDOR FY 2026-12](https://tax.illinois.gov/research/publications/bulletins/fy-2026-12.html) |
| Indiana | More than $100,000 | None from 1 Jan 2024 | Current or preceding calendar year | Gross revenue from goods, electronically transferred products and services, taxable or not | 1 Jul 2019 | [DOR FAQ](https://www.in.gov/dor/i-am-a/business-corp/business-faq/remote-seller-faqs/), [facilitators](https://secure.in.gov/dor/business-tax/remote-seller-information/marketplace-facilitators) |
| Iowa | $100,000 or more (the same page also says a seller "exceeds the sales threshold": check exactly $100,000) | None | Prior calendar year, or current year once crossed | All Iowa sales revenue, including exempt, wholesale, resale and facilitator-collected sales | check | [IDR remote sellers](https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/remote-sellers-marketplace-facilitators) |
| Kansas | In excess of $100,000 | None | Current or immediately preceding calendar year | Cumulative gross receipts from sales to Kansas customers | check | [K.S.A. 79-3702](https://www.kslegislature.gov/li/b2025_26/statute/079_000_0000_chapter/079_037_0000_article/079_037_0002_section/079_037_0002_k/) |
| Kentucky | $100,000 or more | Or 200 or more sales | Prev or current | Gross receipts from sales into Kentucky | check | [DOR notice](https://revenue.ky.gov/News/Pages/Kentucky-Sales-and-Use-Tax-Collections-by-Remote-Retailers-U.S.-Supreme-Court-Ruling.aspx) |
| Louisiana | Exceeds $100,000 | None | Previous or current calendar year | Gross revenue from deliveries into Louisiana | check | [La. R.S. 47:301(4)(k)](https://legis.la.gov/Legis/Law.aspx?d=101815&p=y), [La. R.S. 47:340.1](https://www.legis.la.gov/legis/Law.aspx?d=1186690) |
| Maine | Exceed $100,000 | None in Instructional Bulletin 43 (revised 2 Feb 2022) | Prev or current | Total gross sales of tangible goods or taxable services in Maine | check | [IB 43](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/IB43RegistrationofSellers02_2022.pdf) |
| Maryland | Exceeds $100,000 | Or 200 or more separate transactions | Prev or current | Goods or taxable services delivered in Maryland; direct and facilitated sales both counted | 1 Oct 2019 | [Tax Alert 09-19](https://marylandtaxes.gov/forms/Tax_Publications/Tax_Alerts/SUT_Tax_Alert_Sept2019.pdf) |
| Massachusetts | More than $100,000 | None | Calendar year | Remote sales into Massachusetts; for a marketplace, direct plus facilitated sales | check | [Mass. DOR, sales and use tax guide](https://www.mass.gov/guides/sales-and-use-tax) |
| Michigan | Over $100,000 | Or 200 or more separate transactions | Previous calendar year | Gross sales, taxable and non-taxable, to Michigan customers | check | [Michigan Treasury, remote seller FAQ](https://www.michigan.gov/taxes/business-taxes/sales-use-tax/information/remote-seller-faq), [RAB 2021-21](https://www.michigan.gov/taxes/rep-legal/rab/2021-revenue-administrative-bulletins/revenue-administrative-bulletin-2021-21) |
| Minnesota | More than $100,000 | Or 200 or more retail sales | Prior 12-month period | Retail sales made or facilitated from outside Minnesota to Minnesota destinations | check | [Minn. Stat. 297A.66](https://www.revisor.mn.gov/statutes/cite/297a.66) |
| Mississippi | Exceed $250,000 | None | Any twelve-month period | Sales into Mississippi | Act of 2020 (HB 379); exact date check | [DOR FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions), [MPF notice](https://www.dor.ms.gov/news/notice-marketplace-facilitators) |
| Missouri | Exceed $100,000 (DOR FAQ wording) | None | Preceding 12 months, tested at each quarter end | Sales of tangible goods shipped into Missouri, including marketplace sales | check | [DOR FAQ](https://dor.mo.gov/faq/taxation/business/remote-seller-and-marketplace-facilitator.html) |
| Nebraska | More than $100,000 | Or 200 or more transactions | Prior or current calendar year | Retail sales (all except resale), including through a marketplace | 1 Apr 2019 | [DOR FAQ](https://revenue.nebraska.gov/about/frequently-asked-questions/remote-seller-and-marketplace-facilitator-faqs) |
| Nevada | Exceed $100,000 | Or 200 transactions; the page says both "more than 200" and "reach 200": check | Prev or current | All Nevada sales, direct and through marketplaces | 1 Oct 2019 | [Tax FAQ](https://tax.nv.gov/faqs/marketplace-facilitator-seller-faqs/) |
| New Jersey | Exceeds $100,000 | Or 200 or more separate transactions | Current or prior calendar year | Goods, digital products and taxable services delivered into NJ, including nontaxable retail sales | 1 Nov 2018 | [Taxation FAQ](https://www.nj.gov/treasury/taxation/remotesellersfaq.shtml) |
| New Mexico (GRT) | At least $100,000 | None | Previous calendar year | **Taxable** gross receipts sourced to New Mexico | 1 Jul 2019 | [TRD nexus](https://www.tax.newmexico.gov/businesses/determining-nexus/) |
| New York | Exceeded $500,000 **and** | More than 100 sales (both needed) | Immediately preceding four sales tax quarters | Gross receipts from tangible goods delivered into NY | 1 Jun 2019 | [Tax Department, nexus](https://www.tax.ny.gov/pubs_and_bulls/publications/sales/nexus.htm), [TB-ST-175](https://www.tax.ny.gov/pubs_and_bulls/tg_bulletins/st/do_i_need_to_register_for_sales_tax.htm), [TSB-M-19(2.1)S](https://www.tax.ny.gov/pdf/memos/sales/m19-2-1s.pdf) |
| North Carolina | In excess of $100,000 | None from 1 Jul 2024 | Prev or current | Gross remote sales sourced to NC, including sales as a marketplace seller | check | [Directive 24-1](https://www.ncdor.gov/taxes-forms/sales-and-use-tax/other-sales-and-use-tax-resources/sales-and-use-tax-division-directives/sales-and-use-tax-directive-24-1) |
| North Dakota | Exceed $100,000 | None | Current or previous calendar year | **Taxable** sales into ND | check | [Tax Commissioner](https://www.nd.gov/tax/remoteseller) |
| Ohio | Over $100,000 | Or 200 or more separate sales | Current or previous calendar year | Total sales to Ohio customers | 1 Sep 2019 | [Ohio FAQ](https://tax.ohio.gov/help-center/faqs/sales-and-use-tax-substantial-nexus-and-marketplace-facilitator) |
| Oklahoma | Small-seller exception rose to $100,000 on 1 Nov 2019; current wording check | None | Previous 12 months in the June 2020 FAQ; check | **Taxable** sales; sales through a facilitator that collects are left out | check | [OTC FAQ](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/streamlines-sales-tax/WayfairFAQs-06152020.pdf) |
| Pennsylvania | More than $100,000 (one DOR web sentence says "at least": check exactly $100,000) | None | Previous calendar year; collect from 1 April following | All channels, taxable and nontaxable; a marketplace seller leaves out sales on which the facilitator collects | 1 Jul 2019 | [DOR online retailers](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax/online-retailers), [Bulletin 2019-01](https://www.pa.gov/content/dam/copapwp-pagov/en/revenue/documents/taxlawpoliciesbulletinsnotices/taxbulletins/sut/documents/st_bulletin_2019-01.pdf) |
| Rhode Island | check (the Division's page ties the $100,000 or 200-transaction tests to calendar 2018; the current measure is not stated) | check | check | check | check | [RI Division of Taxation, remote sellers](https://tax.ri.gov/tax-sections/sales-excise-taxes/remote-sellers) |
| South Carolina | Exceeds $100,000 | None | Prev or current | Gross revenue from goods, electronic products and services, including exempt and wholesale sales and the seller's own goods sold on a marketplace | check | [SCDOR remote sellers](https://dor.sc.gov/sales-use-tax-index/sales-tax/remote-sellers), [Policy Manual ch. 13](https://dor.sc.gov/sites/dor/files/Documents/Policy%20Manuals/Chapter%2013%20-%20Nexus.pdf) |
| South Dakota | More than $100,000 | None from 1 Jul 2023 | Prev or current | Gross sales into SD, including marketplace sales | 1 Mar 2019 | [2023 updates](https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates/), [MP bulletin](https://dor.sd.gov/media/e0ajtwlg/marketplace-provider-bulletin.pdf) |
| Tennessee | $100,000 or more (out-of-state dealers) | None | Previous 12-month period stated for facilitators; check for dealers | All retail sales including exempt sales; not sales for resale | 1 Oct 2020 at the $100,000 level | [TDOR](https://www.tn.gov/revenue/taxes/sales-and-use-tax/out-of-state-dealers-marketplace-facilitators.html) |
| Texas | Safe harbor below $500,000; "greater than" in another publication: check exactly $500,000 | None | Preceding 12 calendar months | All taxable and nontaxable sales into Texas, including resale, exempt and (from 1 Apr 2020) marketplace sales | check | [Remote sellers](https://comptroller.texas.gov/taxes/sales/remote-sellers.php), [FAQ](https://comptroller.texas.gov/taxes/sales/remote-sellers-marketplace-faq.php), [94-108](https://comptroller.texas.gov/taxes/publications/94-108.php) |
| Utah | More than $100,000 | None from 1 July 2025 (200 transactions before) | Previous or current calendar year | Gross revenue from goods, products transferred electronically and services into Utah | check | [Utah Tax Commission, remote sellers](https://tax.utah.gov/business/sales-tax/other-sales-tax/out-of-state-remote-sellers/), [non-nexus sellers](https://tax.utah.gov/business/sales-tax/other-sales-tax/non-nexus/) |
| Vermont | At least $100,000 | Or at least 200 transactions | 12 months before the monthly period; review at each quarter end | Sales into Vermont, taxable and nontaxable | 1 Jun 2019 | [Wayfair FAQ](https://tax.vermont.gov/business-and-corp/sales-and-use-tax/wayfair/faqs), [marketplace](https://tax.vermont.gov/business-and-corp/sales-and-use-tax/marketplace) |
| Virginia | More than $100,000 | Or 200 or more separate retail transactions | Prev or current | Gross retail sales; a seller also using a marketplace counts only its direct sales | check | [Virginia Tax](https://www.tax.virginia.gov/remote-sellers-marketplace-facilitators-economic-nexus) |
| Washington | More than $100,000, **or** organized or commercially domiciled in Washington (either test) | None | Current or prior calendar year | Combined gross receipts sourced or attributed to WA: retail, wholesale, services, exempt and marketplace sales | check | [DOR remote sellers](https://dor.wa.gov/taxes-rates/retail-sales-tax/marketplace-fairness-leveling-playing-field/remote-sellers) |
| West Virginia | More than $100,000 | Or 200 or more separate transactions | Preceding calendar year, or the current year from the day crossed | Taxable and nontaxable sales delivered into WV | 1 Jul 2019 | [Tax Division](https://tax.wv.gov/Business/SalesAndUseTax/ECommerce/RemoteSellers/Pages/RemoteSellersAndWestVirginiaTax.aspx), [TSD-442](https://tax.wv.gov/Documents/TSD/tsd442.pdf) |
| Wisconsin | Exceed $100,000 | None from 20 Feb 2021 | Prev or current | Gross sales into Wisconsin | check | [DOR remote sellers](https://www.revenue.wi.gov/Pages/TaxPro/2018/Registration-and-Collection-Dates-for-Remote-Sellers.aspx) |
| Wyoming | Exceeds $100,000 | None; repealed by Laws 2024, ch. 67 | Current or immediately preceding calendar year | Gross revenue from goods, admissions or services delivered into WY | check | [Wyo. Stat. 39-15-501](https://wyoleg.gov/statutes/compress/title39.pdf) |

### Notes on individual rows

- **California.** The test adds the sales of "all persons related to the retailer", defined by reference to 26 U.S.C. 267(b) ([CDTFA](https://www.cdtfa.ca.gov/industry/wayfair.htm)). The $500,000 is based on total sales of tangible personal property, "which may include nontaxable sales, such as sales for resale" ([CDTFA Wayfair FAQ](https://www.cdtfa.ca.gov/industry/wayfair/frequently-asked-questions.htm)). A seller must also include sales "facilitated through" a marketplace. It need not register if all of its California sales are facilitated by a registered marketplace facilitator, but must register once it makes any direct sale while over the threshold ([CDTFA Marketplace Facilitator Act guide](https://www.cdtfa.ca.gov/industry/MPFAct.htm)). The test is "exceed", so exactly $500,000 does not trigger it.
- **Colorado.** A retailer is exempt only if its sales are "less than $100,000" in **both** the current and previous years, and must collect once current-year sales "exceed $100,000" ([CDOR](https://tax.colorado.gov/out-of-state-businesses)). Sales of exactly $100,000 fall between the two sentences: check. Colorado home-rule cities run their own sales taxes; this skill does not cover them.
- **Georgia.** The remote seller bulletin is from 2019 and the marketplace bulletin from 2020 ([SUT-2019-02](https://dor.georgia.gov/media/35301/download)). They are still listed on the Department's bulletin page, but check for later law changes before relying on the 200-sale test.
- **Maine.** Instructional Bulletin 43 states the test as sales that "exceed $100,000" with no transaction count. The older Maine remote-sellers web page still quotes a 200-transaction test ([MRS page](https://www.maine.gov/revenue/taxes/sales-use-service-provider-tax/guidance-documents/remote-sellers)). Follow the bulletin, which is the later text, and confirm with Maine Revenue Services if a seller is relying on it.
- **Missouri.** The DOR FAQ uses "exceed $100,000" and, in different answers, both "taxable sales" and "all sales of tangible personal property" ([DOR FAQ](https://dor.mo.gov/faq/taxation/business/remote-seller-and-marketplace-facilitator.html)). Check the statute before advising a seller close to $100,000.
- **Tennessee.** The Department's page says "$100,000 or more" for out-of-state dealers but "more than $100,000" for facilitators ([TDOR](https://www.tn.gov/revenue/taxes/sales-and-use-tax/out-of-state-dealers-marketplace-facilitators.html)). Treat exactly $100,000 as triggering for a dealer.
- **Texas.** The safe harbor applies when Texas revenue is "less than $500,000" in the previous 12 calendar months ([Comptroller FAQ](https://comptroller.texas.gov/taxes/sales/remote-sellers-marketplace-faq.php)); publication 94-108 says "greater than $500,000" ([94-108](https://comptroller.texas.gov/taxes/publications/94-108.php)). Exactly $500,000 is unclear: check.
- **Rows still marked check (Rhode Island, and the marketplace start dates marked check).** Read the state's own page before advising; do not rely on third-party charts. Idaho, Louisiana, Massachusetts, Michigan and Utah were filled on 13 November 2026 from the state skills and the states' own pages.

## States with no general statewide sales tax

| State | Position | Source |
| --- | --- | --- |
| Alaska | No statewide sales tax. Local jurisdictions that are members of the Alaska Remote Seller Sales Tax Commission (ARSSTC) apply a $100,000 statewide gross sales test (current or prior calendar year), with the 200-transaction test removed from 1 January 2025; non-member jurisdictions are handled one by one. See `no-sales-tax-states` and `ak-sales-tax` | [ARSSTC threshold notice](https://arsstc.org/wp-content/uploads/2024/09/Threshold-Change-for-Sellers.pdf) |
| Delaware | Confirm with the Delaware Division of Revenue that no sales tax applies. Its gross receipts tax is levied on the business and should be assessed separately | [Delaware gross receipts tax](https://revenue.delaware.gov/business-tax-forms/gross-receipts-tax/) |
| Montana | No general sales tax. An 8% lodging facility sales and use tax applies statewide, and resort communities may levy a local resort tax. See `no-sales-tax-states` | [Montana DOR, lodging facility tax](https://revenue.mt.gov/taxes/miscellaneous/lodging-facility) |
| New Hampshire | No general sales tax. The 8.5% Meals and Rooms (Rentals) Tax applies to meals, rooms and motor vehicle rentals. See `no-sales-tax-states` | [NH DRA, Meals and Rooms FAQ](https://www.revenue.nh.gov/resource-center/frequently-asked-questions/meals-rooms-rentals-tax) |
| Oregon | No sales tax. The Corporate Activity Tax "is not a transactional tax, such as a retail sales tax" and has its own filing thresholds | [Oregon CAT](https://www.oregon.gov/dor/programs/businesses/pages/corporate-activity-tax.aspx) |

## Boundary and exception table

| Situation | Rule | Source |
| --- | --- | --- |
| Sales of exactly $100,000 in a "more than" or "exceed" state (for example Washington, Indiana, New Jersey, South Carolina) | Not over the threshold; no nexus from the sales test alone | [DOR remote sellers](https://dor.wa.gov/taxes-rates/retail-sales-tax/marketplace-fairness-leveling-playing-field/remote-sellers), [SCDOR](https://dor.sc.gov/sales-use-tax-index/sales-tax/remote-sellers) |
| Sales of exactly $100,000 in an "at least" or "or more" state (Illinois, Kentucky, Hawaii, Vermont, New Mexico, Connecticut) | Threshold met (Iowa uses both wordings: check) | [IDOR FY 2026-12](https://tax.illinois.gov/research/publications/bulletins/fy-2026-12.html), [Vermont FAQ](https://tax.vermont.gov/business-and-corp/sales-and-use-tax/wayfair/faqs) |
| AND tests | Connecticut needs both 200 or more retail sales and at least $100,000; New York needs both more than $500,000 and more than 100 sales. Meeting one prong only is not enough | [Connecticut DRS](https://portal.ct.gov/drs/businesses/new-business-resource-center/registering-with-drs), [TB-ST-175](https://www.tax.ny.gov/pubs_and_bulls/tg_bulletins/st/do_i_need_to_register_for_sales_tax.htm) |
| Transaction tests removed | Indiana from 1 Jan 2024; North Carolina from 1 Jul 2024; Wyoming (Laws 2024, ch. 67); South Dakota from 1 Jul 2023; Wisconsin from 20 Feb 2021; Illinois from 1 Jan 2026 | Row sources in the state table |
| Previous year only | Alabama, Florida, New Mexico, and Pennsylvania (collection from 1 April of the following year). A seller crossing mid-year does not start collecting that year under the sales test | [ALDOR FAQ](https://www.revenue.alabama.gov/faqs/are-all-remote-sellers-required-to-register-in-alabama/), [FDOR notice 21A01-03](https://floridarevenue.com/taxes/tips/Documents/TIP_21A01-03.pdf) |
| Rolling periods | Illinois 12-month lookback re-tested quarterly; Minnesota prior 12 months; Missouri preceding 12 months at each quarter end; Texas preceding 12 calendar months; Vermont 12 months, reviewed each quarter; New York four sales tax quarters; Connecticut 12 months to 30 September; Mississippi any twelve months | Row sources in the state table |
| Taxable sales only | Florida, New Mexico, North Dakota, Oklahoma count taxable sales; a seller of mostly exempt goods can stay under | [FDOR notice 21A01-03](https://floridarevenue.com/taxes/tips/Documents/TIP_21A01-03.pdf), [Tax Commissioner](https://www.nd.gov/tax/remoteseller) |
| Exempt and wholesale sales included | Iowa, South Carolina, Texas, Washington, Indiana, California (nontaxable sales such as sales for resale), New Jersey (nontaxable retail) count them | [IDR](https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/remote-sellers-marketplace-facilitators), [SC Policy Manual](https://dor.sc.gov/sites/dor/files/Documents/Policy%20Manuals/Chapter%2013%20-%20Nexus.pdf), [CDTFA Wayfair FAQ](https://www.cdtfa.ca.gov/industry/wayfair/frequently-asked-questions.htm) |
| Marketplace sales left out of the seller's own test | Arizona (not facilitated), Georgia (may exclude), Oklahoma (if facilitator collects), Pennsylvania (if facilitator collects), Virginia (direct sales only for a seller also using a marketplace), Alabama (SSUT marketplace) | [A.R.S. 42-5044](https://www.azleg.gov/ars/42/05044.htm), [SUT-2020-01](https://dor.georgia.gov/media/35306/download) |
| Marketplace-only seller over the threshold | Must still register: South Dakota (may get non-filing status); New Jersey (may ask for a non-reporting basis); New York (register and file periodic returns even though the provider remits); Washington (B&O filing continues). No registration needed if every sale goes through a facilitator that collects: Ohio, Oklahoma, Tennessee, Missouri, and California (registered facilitator; facilitated sales still count toward the $500,000 test). Other states: check | [CDTFA Marketplace Facilitator Act guide](https://www.cdtfa.ca.gov/industry/MPFAct.htm), [SD 2023 updates](https://dor.sd.gov/businesses/taxes/sales-use-tax/2023-legislative-updates/), [NJ FAQ](https://www.nj.gov/treasury/taxation/remotesellersfaq.shtml), [TB-ST-175](https://www.tax.ny.gov/pubs_and_bulls/tg_bulletins/st/do_i_need_to_register_for_sales_tax.htm), [DOR remote sellers](https://dor.wa.gov/taxes-rates/retail-sales-tax/marketplace-fairness-leveling-playing-field/remote-sellers), [Ohio FAQ](https://tax.ohio.gov/help-center/faqs/sales-and-use-tax-substantial-nexus-and-marketplace-facilitator), [OTC FAQ](https://oklahoma.gov/content/dam/ok/en/tax/documents/resources/publications/streamlines-sales-tax/WayfairFAQs-06152020.pdf), [TDOR](https://www.tn.gov/revenue/taxes/sales-and-use-tax/out-of-state-dealers-marketplace-facilitators.html), [MO FAQ](https://dor.mo.gov/faq/taxation/business/remote-seller-and-marketplace-facilitator.html) |
| Sellers with no taxable retail sales | New Jersey: remote sellers making only sales for resale, or only nontaxable retail sales, need not register. South Carolina: a remote seller making only wholesale sales needs no retail licence | [NJ FAQ](https://www.nj.gov/treasury/taxation/remotesellersfaq.shtml), [SC Policy Manual](https://dor.sc.gov/sites/dor/files/Documents/Policy%20Manuals/Chapter%2013%20-%20Nexus.pdf) |
| Inventory in a marketplace warehouse | Physical presence. Connecticut requires registration "even if it is under the thresholds". Texas: below $500,000 no permit is needed if the provider has certified it will assume the seller's duties; above it, register | [Connecticut DRS](https://portal.ct.gov/drs/businesses/new-business-resource-center/registering-with-drs), [Comptroller FAQ](https://comptroller.texas.gov/taxes/sales/remote-sellers-marketplace-faq.php) |
| Related companies | Arizona aggregates affiliated persons; California adds related persons' sales | [A.R.S. 42-5044](https://www.azleg.gov/ars/42/05044.htm), [CDTFA](https://www.cdtfa.ca.gov/industry/wayfair.htm) |

## Worked cases

These are illustrations with invented numbers. Each assumes no physical presence unless stated.

1. **Illinois after the transaction test ended** ([IDOR FY 2026-12](https://tax.illinois.gov/research/publications/bulletins/fy-2026-12.html)). A seller made 450 sales of goods totalling $80,000 to Illinois buyers in the 12 months to 31 March 2026. Under the old rules, 200 or more transactions would have been enough. From 1 January 2026 the only test is $100,000 or more in the lookback period. $80,000 is below $100,000, so the seller has no Illinois duty from the sales test. It must keep re-testing each quarter.
2. **New York AND test** ([TB-ST-175](https://www.tax.ny.gov/pubs_and_bulls/tg_bulletins/st/do_i_need_to_register_for_sales_tax.htm)). In the four sales tax quarters just ended, a seller of furniture delivered 90 orders into New York worth $520,000. Receipts exceed $500,000, but 90 sales is not more than 100. Both conditions are needed, so no registration is required from the economic test. With a 101st sale in a later four-quarter window, it would be.
3. **Connecticut AND test, and inventory** ([Connecticut DRS](https://portal.ct.gov/drs/businesses/new-business-resource-center/registering-with-drs)). In the 12 months to 30 September 2025, a seller made 150 retail sales into Connecticut worth $150,000. It has at least $100,000 but not 200 or more sales, so the threshold is not met. If any of its stock sits in a marketplace facilitator's Connecticut warehouse, it must register anyway, because that rule applies "even if it is under the thresholds".
4. **Same sales, opposite results: Georgia and South Carolina** ([SUT-2020-01](https://dor.georgia.gov/media/35306/download), [SC Policy Manual](https://dor.sc.gov/sites/dor/files/Documents/Policy%20Manuals/Chapter%2013%20-%20Nexus.pdf)). In 2025 a seller sold $120,000 of its own goods into each state, of which $110,000 went through a facilitator that collects and $10,000 was direct. Georgia lets a remote seller exclude facilitated sales, so its figure is $120,000 minus $110,000, which is $10,000. That is under $100,000, and at 50 direct orders it is under 200 sales too, so there is no Georgia duty. South Carolina counts the seller's own goods sold via a marketplace, so its figure is $120,000. That exceeds $100,000, so the seller needs a South Carolina retail licence and remits on its own direct sales; in the Department's own example the seller remits on its website sales only.
5. **Arizona exactly at the line** ([A.R.S. 42-5044](https://www.azleg.gov/ars/42/05044.htm)). A seller's 2025 direct (non-facilitated) Arizona sales were exactly $100,000. The statute requires "more than" $100,000, so the threshold is not met for 2025. Each calendar year is tested on its own: 2025 sales do not carry into 2026. If its 2026 direct Arizona sales go over $100,000, for example on 20 August 2026, it must get a licence then and start remitting on 1 October 2026 (the first month starting at least thirty days later), for the rest of 2026 and all of 2027.

Cases 2 and 4 recomputed:

```oa-check
name: New York AND test, 520,000 over 90 sales (2026)
inputs:
  receipts: 520000
  sales_count: 90
steps:
  - receipts_over: receipts - 500000
  - sales_over: sales_count - 100
  - both_met: min(receipts_over, sales_over)
expected:
  receipts_over: 20000
  sales_over: -10
  both_met: -10
```

A negative `both_met` means at least one prong fails, so no registration from the economic test.

```oa-check
name: Same sales, Georgia excludes facilitated sales, South Carolina counts them (2025)
inputs:
  own_goods_sales: 120000
  facilitated: 110000
  threshold: 100000
steps:
  - georgia_measure: own_goods_sales - facilitated
  - georgia_margin: georgia_measure - threshold
  - sc_measure: own_goods_sales
  - sc_margin: sc_measure - threshold
expected:
  georgia_measure: 10000
  georgia_margin: -90000
  sc_measure: 120000
  sc_margin: 20000
```

## When to refuse or refer

- The client has, or may have, physical presence (staff, contractors, stock in a fulfilment centre) in states where it has never registered: refer for a back-exposure and voluntary disclosure review. This skill does not cover look-back periods, penalties or disclosure programmes.
- The state is marked **check** and the client needs an answer now: do not fill the gap from a vendor chart. Confirm on the state's own site or with the state.
- Sales sit within a few thousand dollars of a threshold in a state whose wording conflicts (Colorado, Iowa, Missouri, Pennsylvania, Tennessee, Texas, and the transaction counts in Arkansas and Nevada): get written confirmation from the state.
- The question is about taxability, rates, local home-rule registration (Colorado, Alabama, Louisiana, Alaska local jurisdictions) or income tax nexus: refer to the relevant state Guide or a state-tax specialist.
- Sales into Puerto Rico or other territories: out of scope.
- The client has already received a nexus questionnaire or audit letter from a state: refer; voluntary routes may be closed.

## Filing and payment

Start dates after crossing a threshold, where the reviewed source gives them:

| State | When to register and start collecting | Source |
| --- | --- | --- |
| Arizona | Licence once the threshold is met; remit from the first day of the month that starts at least thirty days later, for the rest of that year and the next | [A.R.S. 42-5044](https://www.azleg.gov/ars/42/05044.htm) |
| Colorado | By the first day of the first month starting at least 90 days after current-year sales exceed $100,000; the whole year if the previous year exceeded it | [CDOR](https://tax.colorado.gov/out-of-state-businesses) |
| Iowa | First day of the next month that starts at least 30 days after crossing; through that year and the whole next year | [IDR](https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/remote-sellers-marketplace-facilitators) |
| Maine | On or before the first day of the first month starting at least thirty days after crossing; may cancel after two calendar years under the threshold | [IB 43](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/IB43RegistrationofSellers02_2022.pdf) |
| Missouri | No later than three months after the close of the quarter in which the 12-month total exceeds $100,000 | [DOR FAQ](https://dor.mo.gov/faq/taxation/business/remote-seller-and-marketplace-facilitator.html) |
| North Dakota | From the following calendar year, or 60 days after crossing, whichever is earlier | [Tax Commissioner](https://www.nd.gov/tax/remoteseller) |
| New Jersey | On taxable transactions after the threshold is met (not the one that meets it), with a grace period of up to 30 calendar days to register and begin collecting | [Taxation FAQ](https://www.nj.gov/treasury/taxation/remotesellersfaq.shtml) |
| Pennsylvania | Collection year runs 1 April to 31 March, based on the previous calendar year | [DOR online retailers](https://www.pa.gov/agencies/revenue/resources/tax-types-and-information/sales-use-and-hotel-occupancy-tax/online-retailers) |
| South Carolina | Retail licence and remittance from the first day of the second calendar month after nexus | [SC Policy Manual](https://dor.sc.gov/sites/dor/files/Documents/Policy%20Manuals/Chapter%2013%20-%20Nexus.pdf) |
| South Dakota | By the first day of the month that starts at least thirty days after crossing | [SD MP bulletin](https://dor.sd.gov/media/e0ajtwlg/marketplace-provider-bulletin.pdf) |
| Texas | No later than the first day of the fourth month after the month the $500,000 safe harbor is exceeded | [Remote sellers](https://comptroller.texas.gov/taxes/sales/remote-sellers.php) |
| Washington | First day of the month starting at least 30 days after crossing, if not met the prior year | [DOR remote sellers](https://dor.wa.gov/taxes-rates/retail-sales-tax/marketplace-fairness-leveling-playing-field/remote-sellers) |
| West Virginia | On sales made after the day a threshold is reached in the current year | [Tax Division](https://tax.wv.gov/Business/SalesAndUseTax/ECommerce/RemoteSellers/Pages/RemoteSellersAndWestVirginiaTax.aspx) |

For other states, read the start rule on the row's source. Filing frequencies and due dates are set by each state after registration and are not covered here.

## Periods in 2025 (for returns and reviews of 2025 activity)

- **Illinois:** for lookback periods ending on or before 31 December 2025, the 200-transaction test still applied alongside $100,000. A seller registered only under the 200 test had to review its 12 months ending 31 December 2025 and stop remitting if it was under $100,000 ([IDOR FY 2026-12](https://tax.illinois.gov/research/publications/bulletins/fy-2026-12.html)).
- **Utah:** the 200-transaction test applied before 1 July 2025; from then only the more-than-$100,000 test applies.
- **Alaska (ARSSTC):** the 200-transaction test was removed from 1 January 2025.
- **Louisiana:** the statute gives no transaction count for 2025 or 2026.
- **Other rows:** the reviewed sources show no change taking effect during 2025 or 2026 apart from the Illinois change above. Still confirm the test for the exact period you are reviewing.

## Completion checklist

- [ ] Physical presence checked in every state, including marketplace inventory locations.
- [ ] Sales data built per state: calendar years 2025 and 2026, rolling 12 months, New York quarters, Connecticut 12 months to 30 September.
- [ ] Each state's sales basis applied (gross, retail or taxable; exempt and wholesale in or out; marketplace in or out; related parties added in Arizona and California).
- [ ] "More than" versus "at least" applied; AND tests (Connecticut, New York) applied as AND.
- [ ] Transaction tests applied only where the table shows one still exists.
- [ ] Start date worked out from the state's start rule.
- [ ] Every **check** state confirmed on the state's own site, with the page and date noted in the file.
- [ ] Alaska local jurisdictions and home-rule localities flagged separately.
- [ ] Next re-test date diarised on each state's cycle.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Each state's own page, statute or bulletin, as linked in its row of the state table. Read for the sales test, transaction test, period, which sales count and marketplace start date. | https://www.cdtfa.ca.gov/industry/wayfair.htm | 2026-09-25, links re-checked 2026-11-13 |
| Idaho State Tax Commission, online sellers guide (via `id-sales-tax`). Read for collection once Idaho sales exceed $100,000 in the current or previous year. | https://tax.idaho.gov/taxes/sales-use/guides-for-certain-groups/online-sellers/online-guide/ | 2026-11-13 |
| La. R.S. 47:301(4)(k) and 47:340.1 (via `la-sales-tax`). Read for gross delivered revenue exceeding $100,000, previous or current year, no transaction count. | https://legis.la.gov/Legis/Law.aspx?d=101815&p=y | 2026-11-13 |
| Mass. DOR, sales and use tax guide (via `ma-sales-tax`). Read for more than $100,000 of Massachusetts sales in a calendar year. | https://www.mass.gov/guides/sales-and-use-tax | 2026-11-13 |
| Michigan Treasury, remote seller FAQ. Read for "in the previous calendar year, the remote seller made over $100,000 of gross sales or 200 or more separate transactions". | https://www.michigan.gov/taxes/business-taxes/sales-use-tax/information/remote-seller-faq | 2026-11-13 |
| Utah Tax Commission, out-of-state (remote) sellers. Read for "in either the previous or the current calendar year ... more than $100,000"; non-nexus page for the pre-1 July 2025 transaction test. | https://tax.utah.gov/business/sales-tax/other-sales-tax/out-of-state-remote-sellers/ | 2026-11-13 |
| RI Division of Taxation, remote sellers (via `ri-sales-tax`). Read for the $100,000 or 200 tests tied to calendar 2018. | https://tax.ri.gov/tax-sections/sales-excise-taxes/remote-sellers | 2026-11-13 |
| NY Tax Department, nexus (via `ny-sales-tax`). Read for more than $500,000 and more than 100 sales in the preceding four sales tax quarters. | https://www.tax.ny.gov/pubs_and_bulls/publications/sales/nexus.htm | 2026-11-13 |
| Arkansas Act 822 of 2019, section 19 (via `ar-sales-tax`). Read for exceeding $100,000 or exceeding 200 transactions. | https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2019R%2FPublic%2FACT822.pdf | 2026-11-13 |
| ARSSTC threshold notice (via `ak-sales-tax`). Read for the $100,000 statewide test and the end of the 200-transaction test. | https://arsstc.org/wp-content/uploads/2024/09/Threshold-Change-for-Sellers.pdf | 2026-11-13 |
| South Dakota v. Wayfair, 585 U.S. 162 (2018), slip opinion. Read for the upheld $100,000 or 200 transactions law. | https://www.supremecourt.gov/opinions/17pdf/17-494_j4el.pdf | 2026-11-13 |
| 15 U.S.C. 381 (govinfo). Read for the income tax limit on solicitation of orders. | https://www.govinfo.gov/content/pkg/USCODE-2024-title15/html/USCODE-2024-title15-chap10B-sec381.htm | 2026-11-13 |

Not yet confirmed: Rhode Island's current economic nexus test; the marketplace facilitator start dates marked check (Arizona, Colorado, Idaho, Illinois, Iowa, Kansas, Kentucky, Louisiana, Maine, Massachusetts, Michigan, Missouri, North Carolina, North Dakota, Oklahoma, South Carolina, Texas, Utah, Virginia, Washington, Wisconsin, Wyoming); exactly-at-threshold wording in Colorado, Iowa, Missouri, Pennsylvania, Tennessee and Texas and the transaction count wording in Nevada; Oklahoma's current small-seller wording.

Read on the state's own page on 25 September 2026 and not re-read on 13 November (figures kept, links checked): Alabama, Colorado, Connecticut, DC, Florida, Georgia's 200-sale test, Hawaii, Indiana, Kansas, Kentucky, Maine, Maryland, Minnesota, Mississippi, Missouri, Nebraska, Nevada, New Jersey, North Carolina, North Dakota, Oklahoma, South Carolina, South Dakota, Tennessee, Vermont, Virginia, West Virginia, Wisconsin, Wyoming.
