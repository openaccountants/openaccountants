---
name: texas-sales-tax
description: >
  Texas sales and use tax for 2026: permits, remote sellers and marketplaces, the 6.25% state rate and 2% local cap, local sourcing, taxable goods and services, resale and exemptions, Form 01-114, filing, discounts, penalties and interest. Includes explicit holds for unresolved boundaries and preserves the original 2025 and 2026 cases. Trigger on Texas sales tax, Texas use tax, Form 01-114, Texas resale certificate and Texas SaaS tax.
version: "2.3"
jurisdiction: US-TX
tax_year: 2026
last_updated: 2026-11-27
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# Texas sales and use tax, 2026

## Scope and who this is for

For sellers of taxable goods or services into Texas and businesses making purchases for use in Texas. The state rate is **6.25%**, with local tax up to **2%**, a combined maximum of **8.25%** ([Comptroller](https://comptroller.texas.gov/taxes/sales/)). Franchise tax and the separate motor vehicle, hotel, mixed beverage, 9-1-1 and oil and gas regimes are outside this Guide.

## Ask the client first

Obtain the seller's Texas locations, formation, staff, representatives and inventory; the preceding twelve calendar months' Texas revenue across every sales channel; marketplace certifications; the actual goods or services; where each order is received, fulfilled and delivered; permits and assigned filing frequency; exemption certificates; untaxed purchases; prior returns, payments and notices. Unknown revenue or missing paperwork is a reason to resolve the facts before deciding, not to invent a taxable amount.

## The method, step by step

### Permit and remote sellers ([Rule 3.286](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=197579))

1. A seller engaged in business in Texas generally needs a permit: this includes Texas premises, representatives and Texas formation; the remote-only and marketplace exceptions require separate examination. Apply through the [Texas registration application or Form AP-201](https://comptroller.texas.gov/taxes/sales/faq/permit.php). A permit is free, but security may be required. Obtain a permit for each active Texas place of business; permits are nontransferable, so a change of legal owner needs a new permit ([§151.201](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.201)).
2. A remote seller's only Texas activity is remote solicitation. The **less-than-$500,000** safe harbor looks at total Texas revenue in the preceding twelve calendar months. It includes taxable, nontaxable and exempt sales, resale sales, associated handling, transportation and installation fees, and marketplace sales; there is no separate transaction-count test ([Rule 3.286(b)(2)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=197579)).
3. When that revenue **exceeds $500,000**, obtain the permit and begin collecting no later than the first day of the fourth month after the crossing month. Exactly $500,000 is a non-usable boundary here: the rule's safe harbor says “less than” but its commencement clause says “exceeds.” Check this point with one of our partner accountants. Do not infer a commencement date from the conflicting summaries ([Rule 3.286(b)(2)(B), (E)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=197579)).
4. After twelve consecutive months in which each trailing twelve-month total is below the safe harbor, termination requires the Comptroller's prescribed form. After termination, resume on the first day of the second month following a twelve-calendar-month period exceeding the safe harbor ([Rule 3.286(b)(2)(F)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=197579)).

### Rates and the taxable price

| Item | Treatment and conditions | Official source |
|---|---|---|
| State sales and use tax | 6.25% on nonexempt taxable items; local tax is additional | [§§151.051, 151.101](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm) |
| Local tax | Up to 2% combined, hence 8.25% maximum state plus local; verify the address, not a ZIP code | [Comptroller rates](https://comptroller.texas.gov/taxes/sales/), [local guide](https://comptroller.texas.gov/taxes/publications/94-105.php) |
| Remote seller's elected single local use tax | 1.75%, replacing destination local tax; Texas-based sellers and marketplace providers cannot use it | [Remote sellers](https://comptroller.texas.gov/taxes/sales/remote-sellers.php) |
| Data processing and information services | 20% of value exempt, leaving 80% taxable (derived), after correct classification; do not apply this reduction to an independently taxable service merely because a computer is used | [§151.351](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.351), [taxable services](https://comptroller.texas.gov/taxes/publications/96-259.php) |

Shipping and delivery connected with a taxable sale are part of its taxable price; delivery connected with an exempt sale is exempt. Separately state Texas tax on the invoice, or satisfy the Comptroller's written tax-included statement and sign requirements ([§151.007](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.007), [collection FAQ](https://comptroller.texas.gov/taxes/sales/faq/collection.php)).

Elect the single local rate on the permit application or notify the Comptroller on Form 01-799 before using it; an existing seller's election starts at a reporting-period boundary. Use it for all qualifying sales until revoked. **Receipt by October 1**, including October 1 itself, makes revocation effective January 1 of the following year; receipt **after October 1** makes it effective January 1 of the year after that. This is the operative rule; the remote-seller summary uses a different cutoff. A purchaser's refund of the single-rate difference requires a separate claim ([Rule 3.334(i)(3)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=219470), [election procedure](https://comptroller.texas.gov/taxes/sales/remote-sellers.php)).

### Which local tax applies ([Rule 3.334](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=219470))

For ordinary goods transactions, establish the seller's qualifying place of business first. It is an established outlet, office or location operated to receive orders from unrelated customers; receipt of three or more orders by sales personnel during the calendar year can establish its purpose. Servers, websites and software alone do not qualify, and forwarding orders to a warehouse does not make it a place of business. Rule 3.334(a)(18), (b) contains the additional facility tests and the single-location small/micro-business presumption. If these distinctions affect the answer, Check this point with one of our partner accountants.

The following matrix excludes marketplace sales and special goods/services sourcing rules. Orders not received by sales personnel are also held: the Comptroller [states that enforcement of that provision is enjoined](https://comptroller.texas.gov/taxes/publications/94-105.php). **AUDIT FLASH POINT**: Check this point with one of our partner accountants.

| Order received | Fulfillment / order facts | Local tax location | Official source |
|---|---|---|---|
| At a Texas place of business | Placed in person, wherever fulfilled | Local sales tax where received | [Rule 3.334(c)(1)(A)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=219470) |
| At a Texas place of business | Not in person; fulfilled at a Texas place of business | Local sales tax where fulfilled | [Rule 3.334(c)(1)(B)(i)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=219470) |
| At a Texas place of business | Not in person; fulfilled anywhere other than a Texas place of business, including outside Texas | Local sales tax where received | [Rule 3.334(c)(1)(B)(ii)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=219470) |
| Not at a Texas place of business | Fulfilled at a Texas place of business | Local sales tax where fulfilled | [Rule 3.334(c)(2)(A)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=219470) |
| Not at a Texas place of business | Fulfilled at a Texas location that is not a place of business | Local sales tax at delivery / possession | [Rule 3.334(c)(2)(B)(i)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=219470) |
| Not at a Texas place of business | Fulfilled outside Texas | Local use tax at first Texas storage, use or consumption; delivery there is presumed use | [Rule 3.334(c)(2)(B)(ii)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=219470) |

For delivery to another jurisdiction, add applicable local use tax only within the **2% total cap**, in this order: **city, county, special purpose district, transit authority**. No use tax of a type is due if sales tax of that type is due. A use tax that cannot fit **in full** is not collected, even in part, and the purchaser does **not** accrue it. The purchaser does owe otherwise applicable tax the seller fails to collect. Multiple overlapping districts, combined areas and special sourcing need individual review ([Rule 3.334(d), (g), (i), (k)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=219470)).

### Marketplaces

A provider engaged in business in Texas assumes seller duties and certifies collection to its sellers. Marketplace local tax follows delivery/possession, and the provider cannot elect the single local use tax rate. A remote provider applies the remote safe harbor to aggregate marketplace sales ([§151.0242](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.0242), [Rule 3.334(k)(5)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=219470), [marketplace FAQ](https://comptroller.texas.gov/taxes/sales/remote-sellers-marketplace-faq.php)).

A remote seller selling only through providers whose certification it accepts in good faith needs no permit, but keeps marketplace records. Temporary inventory at a certifying provider's Texas facility has a specific remote-seller exception below the safe-harbor amount; it does not shelter an above-threshold seller ([Rule 3.286(b)(2)(B)(ii), (b)(3)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=197579)).

**Non-usable reporting/permit holds:** §151.0242(d) and Rule 3.286(b)(3)(C)(i) say to exclude certified marketplace sales from the seller's report, whereas the marketplace FAQ says include them in Item 1 but not Item 2. The FAQ's Texas-only marketplace permit answer also needs reconciliation with Rule 3.286(b)(3)(B)(iii). Do not use this Guide to decide those two points. Check this point with one of our partner accountants. These holds do not remove marketplace sales from the remote-seller revenue test.

## Boundary and exception table

| Sale or purchase | Usable rule or explicit hold | Official source |
|---|---|---|
| Goods and services | Tangible goods are taxable unless exempt; §151.0101 identifies taxable service categories. A professional label does not exempt a separately taxable service. | [§§151.009, 151.0101, 151.051](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm), [services](https://comptroller.texas.gov/taxes/publications/96-259.php) |
| SaaS, web hosting, information services | Classify the actual service. The authority includes SaaS and web hosting as data processing; professional judgment using a computer as a tool is different. Mixed taxable/nontaxable charges, ancillary services and multi-state allocation are held rather than applying the old blanket five-percent summary. Check this point with one of our partner accountants. | [Data processing](https://comptroller.texas.gov/taxes/publications/94-127.php), [services](https://comptroller.texas.gov/taxes/publications/96-259.php) |
| Computer programs, canned or custom | A computer program is tangible personal property. Distinguish a program sale from repair, maintenance, creation or modification of a program not sold by the service provider, excluded by §151.0101(a)(5)(D). Detailed licensing or programming contracts: Check this point with one of our partner accountants. | [§§151.009, 151.0101](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm) |
| Internet access | Separately stated access has not been taxed since July 2020; it was removed from the statutory services list in July 2025. A bundle requires a supportable allocation; otherwise the whole bundle is taxable. | [Comptroller services](https://comptroller.texas.gov/taxes/publications/96-259.php) |
| Resale | Obtain a complete Form 01-339 resale certificate in good faith; a permit number alone is insufficient. A blanket certificate is for exclusively resale purchases. Qualifying resale is in the United States or Mexico; using stock for another purpose requires use-tax review. | [§151.302](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.302), [resale FAQ](https://comptroller.texas.gov/taxes/sales/faq/resale.php) |
| Government buyers | §151.309 covers the United States and specified instrumentalities, Texas and its political subdivisions. It also covers a bordering state/governmental unit to the extent of reciprocity; the old blanket denial for every other state was incorrect. Verify the entity and purchasing records. | [§151.309](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.309) |
| Nonprofits, private schools, colleges, churches, charities; tribal entities | Do not infer exemption from a name or organizational label. Check the specific exemption and purchaser documentation, including Comptroller recognition where required; personal employee/volunteer purchases are not organizational purchases. Tribal-entity/instrumentality status is held. Check this point with one of our partner accountants. | [§151.310](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.310), [exempt organizations](https://comptroller.texas.gov/taxes/publications/96-122.php) |
| Manufacturing | §151.318 exempts qualifying ingredients/components and necessary direct manufacturing property causing a chemical or physical change. It excludes hand tools; it has express exceptions to the intraplant-piping exclusions, so do not treat all conveyors/piping as automatically taxable. Use a supported exemption certificate. Quality control, utilities/predominant-use studies, safety clothing, packaging, pollution equipment, cleanrooms, production companies, short leases, research and support equipment need item-specific review. Check this point with one of our partner accountants. | [§151.318](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.318), [manufacturing](https://comptroller.texas.gov/taxes/publications/94-124.php) |
| Divergent use of qualifying manufacturing property | Before the fourth purchase anniversary, monthly tax is purchase price ÷ 48 × divergent-use fraction × purchase-date tax rate. No tax for a month at 5% or less; none after the fourth anniversary. Measure use by hours or output and keep supporting records. | [§151.3181](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.3181) |
| Occasional sales | The one-or-two-retail-sales test in twelve months requires a person who neither habitually sells nor holds out as doing so; it excludes amusement services and permit holders. It does not cover rentals/leases or marketplace sales. A permitted buyer buying under that exemption must accrue use tax. Entire-operating-assets sales and the other statutory branches are separate tests: Check this point with one of our partner accountants. | [§151.304](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.304) |
| Cleaning | A maid service's cleaning charge is taxable; a household's own employee providing traditional household services is different. Do not extend that exception to pool cleaning or a maid-service subcontractor. | [Cleaning](https://comptroller.texas.gov/taxes/publications/94-111.php) |
| Other previously covered goods/services | Food, prepared/hot food and utensils; soft drinks/milk/juice, candy/gum and ice; human/animal prescription drugs, OTC medicines, supplements and CBD; books/newspapers/magazines; clothing/footwear, holiday exceptions, accessories/rentals and subscription boxes; farm/timber qualifying items and Ag/Timber paperwork; information-media exemptions; homebuilder certificates, residential/separated contracts, nonresidential repairs and scheduled maintenance; amusement, cable, credit reporting, debt collection, insurance, parking/storage, security, telecoms, answering and laundry/cleaning services each need their own operative exceptions. These detailed outcomes are non-usable holds here. Check this point with one of our partner accountants. | [Service categories](https://comptroller.texas.gov/taxes/publications/96-259.php) |
| Interstate sales and foreign exports | Shipping contracts, delivery to a Texas buyer/agent, commercial bills of lading, customs-broker/foreign-import evidence, refunds and return deductions need transaction-specific review. Do not exempt a sale merely because the buyer later takes it out of Texas. Check this point with one of our partner accountants. | [Exports FAQ](https://comptroller.texas.gov/taxes/sales/faq/oos-exports.php) |

## Worked cases

Original inputs are retained. Rates for named cities below are stipulated illustration inputs, not current-address rate lookups. The Navarro County case uses the authority's own sourcing example. Cases marked **held** give no usable tax/filing conclusion.

| Case | Inputs and recomputed outcome | Source / dependency |
|---|---|---|
| 1. Navarro County delivery, 2026 | Store outside Corsicana; in-person table order $1,000 plus $100 delivery. Base $1,100. State 6.25% plus county 0.5%; Ennis city use tax 1.5% fits the cap: $90.75. Waxahachie city use tax 2% does not fit; none is owed for that city tax: $74.25 collected. Difference $16.50. | [Local guide's example](https://comptroller.texas.gov/taxes/publications/94-105.php), [delivery](https://comptroller.texas.gov/taxes/sales/faq/collection.php), [Rule 3.334(d)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=219470) |
| 2. Oregon remote seller, 2026 | No Texas presence; first crossing in June; twelve months to June 30: website $300,000 plus certified marketplaces $300,000 = $600,000. Collection starts no later than October 1. With a valid single-local-rate election, taxable website order $200 × (6.25% + 1.75%) = $16.00. Later marketplace $30,000 plus website $20,000 = $50,000 gross receipts. **Return-line split held** because of the conflict described above; no filing conclusion for those receipts. Check this point with one of our partner accountants. | [Remote FAQ](https://comptroller.texas.gov/taxes/sales/remote-sellers-marketplace-faq.php), [Rule 3.286(b)(2)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=197579), [§151.0242(d)](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.0242) |
| 3. SaaS, 2026 | $2,000 monthly, used wholly at a Texas office; assume a standalone service correctly classified solely as data processing and an applicable 8.25% rate. Base $2,000 × 80% = $1,600; tax $132.00. | [Services](https://comptroller.texas.gov/taxes/publications/96-259.php), [§151.351](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.351) |
| 4. Bookkeeper, 2026, held | $10,000 engagement including $400 unseparated data entry, arithmetically 4%. That percentage alone does not establish the applicable ancillary/mixed-service classification under the operative data-processing rule. The old “no tax” conclusion is non-usable. Check this point with one of our partner accountants. | [Data processing summary](https://comptroller.texas.gov/taxes/publications/94-127.php); operative classification needs resolution |
| 5. Cleaning, 2026 | Maid-service home cleaning $200 at an assumed 8.25% = $16.50. A housekeeper who is the household's own employee is outside that maid-service result. | [Cleaning](https://comptroller.texas.gov/taxes/publications/94-111.php) |
| 6. Timely return, 2026 | $10,000 tax timely reported and paid by a permitted filer: 0.5% discount $50.00; $9,950.00 payable. No discount when late. | [§151.423](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.423), [Rule 3.286(h)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=197579) |
| 7. February prepayment, 2026 | Current liability $2,500, return due March 20; prior February tax $1,700, **owed and paid**. Reasonable estimate: $2,250 (90%) or $1,700 (prior-period amount). February 2026 prepayment due February 17 under the official adjusted chart. | [§151.424](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.424), [prepayment FAQ](https://comptroller.texas.gov/taxes/sales/faq/report-pay.php), [due dates](https://comptroller.texas.gov/taxes/file-pay/due-dates.php) |
| 8. Late September return, 2026 | $2,000 due October 20, filed/paid December 5: 46 days late, assuming no later notice/disaster adjustment. Tax penalty $200 plus report penalty $50 = $250; no discount and no interest yet. | [§151.703](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.703), [penalties](https://comptroller.texas.gov/taxes/file-pay/penalties.php) |
| 9. Manufacturing divergent use, 2026 | Qualifying machine $48,000, purchased at 8.25%, before fourth anniversary; 10% nonmanufacturing use in month. $48,000 ÷ 48 × 10% × 8.25% = $8.25. At 5% or less that month, zero. | [§151.3181](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.3181) |
| 10. Historical data-processing illustration, 2025 | Original invoice $10,000, wholly Texas standalone data processing at assumed 8.25%: base $8,000, tax $660. | [§151.351](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.351) |
| 11. Historical Houston retailer, 2025 | Taxable sales $50,000; assumed state 6.25% and local 2%: $3,125 + $1,000 = $4,125. Timely discount rounds to $20.63; net $4,104.37, subtracting the rounded discount. | [§§151.051, 151.423](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm) |
| 12. Historical Dallas data processing, 2025 | IT consultant's $20,000 correctly classified standalone data processing; assumed 8.25%: base $16,000, tax $1,320, timely discount $6.60, net $1,313.40. | [§§151.351, 151.423](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm) |
| 13. Historical mixed goods/resale, 2025 | $30,000 taxable merchandise plus $5,000 supported resale: total sales $35,000; taxable sales $30,000. Tax needs the actual local sourcing/rate; none invented. | [§151.302](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.302) |
| 14. Historical Austin use tax, 2025 | Office supplies $3,000, no vendor tax, assumed applicable 8.25%, no offsetting tax credit: use tax $247.50. | [Use-tax FAQ](https://comptroller.texas.gov/taxes/sales/faq/use.php) |
| 15. Historical Houston late return, 2025 | Same $4,125 liability as case 11, filed and paid five days late, no notice/disaster adjustment: no discount; 5% = $206.25 plus $50 late report penalty = $256.25. **No interest after only five days**; the former unqualified interest statement was wrong. | [§151.703](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.703), [penalties](https://comptroller.texas.gov/taxes/file-pay/penalties.php) |

```oa-check
name: TX local use tax under the 2% cap, original Navarro inputs (2026)
inputs:
  price: 1100
  state: 0.0625
  county: 0.005
  ennis_city: 0.015
steps:
  - ennis_tax: price * (state + county + ennis_city)
  - waxahachie_tax: price * (state + county)
  - difference: ennis_tax - waxahachie_tax
expected:
  ennis_tax: 90.75
  waxahachie_tax: 74.25
  difference: 16.50
```

**Prepayment decision, 2026.** For the original $2,500 monthly liability and full $2,500 timely qualifying prepayment, ordinary timely filing saves $12.50; prepaying saves an additional $31.25, total $43.75. Choose using the $31.25 benefit and the business's cash timing, after confirming all prepayment conditions ([§§151.423–151.424](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm)).

```oa-check
name: TX prepayment decision, monthly filer (2026)
inputs:
  tax: 2500
  prepayment: 2500
steps:
  - discount_no_prepay: tax * 0.005
  - discount_prepay: tax * 0.005 + prepayment * 0.0125
  - extra_from_prepaying: discount_prepay - discount_no_prepay
expected:
  discount_no_prepay: 12.50
  discount_prepay: 43.75
  extra_from_prepaying: 31.25
```

## When to refuse or refer

The holds in the tables are **not usable filing, exemption or taxability conclusions**. Also hold audits/assessments, hearings, refund limitation periods and single-rate refunds, resale-certificate criminal exposure, special local sourcing/combined districts, detailed software and agricultural/timber exemptions, and missing past permits/returns or penalty waivers. Check this point with one of our partner accountants.

## Filing and payment

- **Frequency:** follow the Comptroller's assignment. Rule 3.286(g) permits quarterly filing below $1,500 state tax per quarter; monthly at $1,500 or more, subject to qualifying quarterly prepayment. Yearly filing requires authorization and less than $1,000 state tax for the calendar year; prior compliance and automatic-revocation conditions also apply. The old quarterly-liability annual bands are not valid ([Rule 3.286(g)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=197579), [§§151.401, 151.405](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm)).
- **Deadline:** returns and payment are due the 20th after the reporting period, next business day on weekends/legal holidays; yearly returns by January 20 following the year. File even a zero return. Retain sales/purchase/exemption records at least four years and longer where required for pending proceedings ([Rule 3.286(e)–(g)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=197579), [§151.025](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.025)).
- **2026 calendar:** monthly due dates January–December: Jan 20, Feb 20, Mar 20, Apr 20, May 20, Jun 22, Jul 20, Aug 20, Sep 21, Oct 20, Nov 20, Dec 21. Quarterly dates in 2026: Jan 20 (Q4 2025), Apr 20, Jul 20, Oct 20. Prepayments: Jan 15, Feb 17, Mar 16, Apr 15, May 15, Jun 15, Jul 15, Aug 17, Sep 15, Oct 15, Nov 16, Dec 15. Q4/yearly 2026 returns fall in January 2027: apply the deadline rule and confirm that year's adjustments ([official 2026 chart](https://comptroller.texas.gov/taxes/file-pay/due-dates.php)).
- **Return:** use [Webfile](https://comptroller.texas.gov/taxes/file-pay/about-webfile.php) or the appropriate prescribed form. Form 01-114 is the long sales/use return; Item 1 is total Texas sales, Item 2 taxable sales, Item 3 taxable purchases for own use without tax paid. Resale/exempt deductions need support; apply the marketplace-reporting hold above. Outlet/list supplements, short-form eligibility, Form 01-148 credits/bad debts and amendments require the current instructions. For nonpermit purchasers use Form 01-156; another-state tax credits need their own eligibility/limit check. Check this point with one of our partner accountants ([use-tax FAQ](https://comptroller.texas.gov/taxes/sales/faq/use.php), [return instructions](https://comptroller.texas.gov/forms/01-922.pdf)).
- **Discount:** a permitted filer reporting and paying timely may deduct 0.5%; there is no stated $500 cap. A monthly/quarterly qualifying prepayment earns 1.25% of the prepayment in addition. Prepay at least 90% of current liability or the corresponding prior-year liability **due and paid**, by the 15th of the month / second month of the quarter, adjusted where applicable; mail filers submit the prepayment report. File the actual return and pay the balance timely; an inadequate estimate loses the whole prepayment discount ([§§151.423–151.424](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm), [Rule 3.286(h)](https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=197579), [FAQ](https://comptroller.texas.gov/taxes/sales/faq/report-pay.php)).
- **Late return/payment:** 5% for failure to report or pay when due; another 5% after 30 days; statutory minimum $1. Add $50 per late return even with no tax due. Notice-stage additional penalties, electronic-payment penalties and collection action are held for account-specific review ([§151.703](https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm#151.703)).
- **Interest:** starts on the 61st day after the due date under the authority's counting convention. For interest accruing in 2026 the annual rate is 7.75%; in 2025 it is 8.50%. Split accrual across years; a 2025 liability does not freeze the 2025 rate. The calculation is tax × annual rate × interest days ÷ days in that year. Original authority example: $1,000 × 7.75% × 150 ÷ 365 = $31.85. Refund interest is a separate calculation ([§111.060](https://tcss.legis.texas.gov/resources/TX/htm/TX.111.htm#111.060), [interest rates](https://comptroller.texas.gov/taxes/file-pay/interest.php)).
- **Payment method:** the existing $10,000/$500,000 payment thresholds, electronic-filing threshold, notices, TEXNET banking cutoffs, mailed-check timing, disaster extensions and amended-return procedures must be checked against the taxpayer's category, instructions and notice before use. They are non-usable procedural holds here. Check this point with one of our partner accountants ([TEXNET FAQ](https://comptroller.texas.gov/taxes/file-pay/texnet-faq.php), [amendments/extensions](https://comptroller.texas.gov/taxes/sales/faq/report-pay.php)).

## Completion checklist

Confirm nexus, permits and revenue first; classify supplies and document exemptions; establish sourcing and rate; accrue untaxed purchases; reconcile the return and supported deductions; check frequency, due date, payment method and discount conditions. Do not treat a held case as an answer. Preserve the original year on historical/amended periods rather than substituting this Guide's current year.

Circular 230 §10.37: apply the law to the actual facts, consider relevant assumptions and limitations, and obtain professional review before relying on written advice for a filing or tax position.

## Sources

| Official source and parts actually read | URL | Read on |
|---|---|---|
| Tax Code Chapter 151: definitions/services, marketplace duties, permits, resale/government/nonprofit exemptions, occasional sales, manufacturing and divergent use, filing/discounts and penalties | https://tcss.legis.texas.gov/resources/TX/htm/TX.151.htm | 2026-11-27 |
| Tax Code §111.060: annual delinquency interest mechanism | https://tcss.legis.texas.gov/resources/TX/htm/TX.111.htm#111.060 | 2026-11-27 |
| Rule 3.286 rendered in the official browser: nexus, remote safe harbor/revenue/start/termination, marketplace exceptions, reporting periods and discounts | https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=197579 | 2026-11-27 |
| Rule 3.334 rendered in the official browser: place of business, six sourcing branches, local cap/order, election and inclusive revocation cutoff, marketplace sourcing | https://texas-sos.appianportalsgov.com/rules-and-meetings?interface=VIEW_TAC_SUMMARY&recordId=219470 | 2026-11-27 |
| Sales tax overview: state/local rates, deadlines and discount conditions | https://comptroller.texas.gov/taxes/sales/ | 2026-11-27 |
| Local collection guide: sourcing matrix, injunction notice, local-tax order and Navarro/Ennis/Waxahachie example | https://comptroller.texas.gov/taxes/publications/94-105.php | 2026-11-27 |
| Remote sellers: current single local rate and election procedure | https://comptroller.texas.gov/taxes/sales/remote-sellers.php | 2026-11-27 |
| Marketplace FAQ: revenue/case inputs; identified reporting and permit conflicts retained as holds | https://comptroller.texas.gov/taxes/sales/remote-sellers-marketplace-faq.php | 2026-11-27 |
| Taxable services: SaaS/web hosting, professional distinction and internet/bundle treatment | https://comptroller.texas.gov/taxes/publications/96-259.php | 2026-11-27 |
| Data processing summary: professional services/mixed charges; not sufficient to resolve operative mixed-service conditions | https://comptroller.texas.gov/taxes/publications/94-127.php | 2026-11-27 |
| Resale FAQ: good faith, complete/blanket certificates and resale geography | https://comptroller.texas.gov/taxes/sales/faq/resale.php | 2026-11-27 |
| Permit FAQ: application, fee/security, locations and changed ownership | https://comptroller.texas.gov/taxes/sales/faq/permit.php | 2026-11-27 |
| Collection/use FAQs: delivery charges, tax-included invoices and taxable-purchase reporting | https://comptroller.texas.gov/taxes/sales/faq/collection.php ; https://comptroller.texas.gov/taxes/sales/faq/use.php | 2026-11-27 |
| Manufacturing guide: qualifying property and divergent-use example; statute controls piping exceptions | https://comptroller.texas.gov/taxes/publications/94-124.php | 2026-11-27 |
| Cleaning: maid-service tax and household-employee exception | https://comptroller.texas.gov/taxes/publications/94-111.php | 2026-11-27 |
| 2026 due-date chart: sales/use and sales-tax prepayment rows | https://comptroller.texas.gov/taxes/file-pay/due-dates.php | 2026-11-27 |
| Prepayment FAQ: estimate/payment conditions and February example | https://comptroller.texas.gov/taxes/sales/faq/report-pay.php | 2026-11-27 |
| Interest page: annual-rate table, accrual and original computation; penalties: late-return/payment treatment | https://comptroller.texas.gov/taxes/file-pay/interest.php ; https://comptroller.texas.gov/taxes/file-pay/penalties.php | 2026-11-27 |

Not yet confirmed: the explicitly non-usable holds above, including exact-threshold commencement, marketplace reporting/permit conflicts, ancillary/mixed-service classification, detailed product/exemption/contract outcomes, exports, credits/refunds and payment procedures. The legacy statute hostname returned a navigation page; the readable legislature resource above replaces it. The official Rule 3.330 direct fetch did not expose the rule text; its mixed-service case remains held. No 2027 chart or current city-address rate lookup is claimed as read.
