---
name: wa-sales-tax
description: Washington retail sales and use tax for 2026. Covers the state and local rates, nexus and marketplace receipts, sourcing, goods and food, digital products, ESSB 5814 services and 2026 amendments, resale, use tax, excise returns, deadlines, penalties and historical cases. Trigger on Washington sales tax, WA use tax, remote seller, reseller permit and ESSB 5814. For B&O computation load wa-bo-tax.
version: "2.2"
jurisdiction: US-WA
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - us-tax-workflow-base
category: state
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: situation-rules
---

# Washington retail sales and use tax, tax year 2026

> Built from the law. General reference only; obtain professional review before filing. Sources below were read on 2026-11-27. The 2025 cases remain 2025 cases; the local-rate table covers only October–December 2026.

The state rate is **6.5% plus local tax**. Establish nexus, classify the transaction and any exemption, source it, then use the address and transaction date to obtain the combined rate. Economic nexus requires **more than $100,000**, not exactly that amount; physical presence and Washington domicile are separate tests. [RCW 82.08.020](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.020), [82.04.067](https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.067).

## Scope and who this is for

Sellers of goods, software, digital products and retail services; remote and marketplace sellers and facilitators; businesses and individuals with untaxed Washington purchases. This covers the sales/use portions of the combined excise return. B&O computations belong in `wa-bo-tax`; payroll in `wa-payroll`. The specific holds below are not filing instructions.

## Ask the client first

Obtain the UBI/account number, assigned filing frequency, residence/domicile, staff/property/agents in Washington, current and prior calendar-year Washington receipts from every activity, marketplace reports and evidence of facilitator collection. Obtain itemized contracts, service and payment dates (especially around October 2025 and July 2026), affiliations/public-agency arrangements, purchaser and receipt addresses, exemption documentation and untaxed purchases. For historical cases obtain the original quarter and address; a city name alone cannot validate an old rate.

## The method, step by step

1. Apply the nexus tests below. Do not apply the economic-nexus collection grace period to physical presence.
2. Apply the boundary table, the 2026 amendments and documentation requirements; a business purchaser is not automatically exempt.
3. Apply the sourcing hierarchy, then look up the applicable address/date rate and location code. Separately state sales tax; selling price includes seller-charged shipping/delivery. Sellers owe the correct tax even when under-collected. [DOR remote sellers](https://dor.wa.gov/taxes-rates/retail-sales-tax/marketplace-fairness-leveling-playing-field/remote-sellers).
4. Reconcile gross receipts, deductions, taxable sales by location and buyer use tax; report on the assigned return. Retain the supporting records.

## Rates, bands and thresholds

| Item | Rule | Source |
| --- | --- | --- |
| State sales tax | 6.5% of the taxable selling price | [RCW 82.08.020(1)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.020); [DOR numeric rate](https://dor.wa.gov/taxes-rates/retail-sales-tax) |
| Local rates | Address/date lookup; do not extrapolate one quarter or city rate to another | [DOR rates](https://dor.wa.gov/taxes-rates/sales-use-tax-rates) |
| Seattle / Tacoma | Q4 2026: code 1726, local .0405 + state .0650 = .1055; code 2717, .0400 + .0650 = .1050 | [DOR Q4 flyer](https://dor.wa.gov/sites/default/files/2026-08/Q426_LSU-flyer-by-county.pdf) |
| Olympia / Spokane city | Q4 2026: code 3403, .0350 + .0650 = .1000; code 3210, .0260 + .0650 = .0910 | [DOR Q4 flyer](https://dor.wa.gov/sites/default/files/2026-08/Q426_LSU-flyer-by-county.pdf) |
| Vancouver / Edmonds / Lynnwood | Q4 2026: code 0605, .0240 + .0650 = .0890; codes 3104 and 3110, .0420 + .0650 = .1070 | [DOR Q4 flyer](https://dor.wa.gov/sites/default/files/2026-08/Q426_LSU-flyer-by-county.pdf) |
| Nexus | Current or immediately preceding calendar year: resident/domiciliary individual; entity organized/commercially domiciled in WA; nonresident with more than $100,000 WA cumulative gross receipts or qualifying physical presence | [RCW 82.04.067](https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.067) |

Physical presence includes property/employees and activities through agents or representatives significantly associated with establishing or maintaining a Washington market; the statute requires demonstrably more than a slightest presence and is subject to RCW 82.32.531. Do not use an unqualified “always” test for every incidental contact. [RCW 82.04.067(1)–(3)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.067).

Count all Washington-attributed income, including retail, wholesale and apportionable services, exempt and facilitated sales. A facilitator counts its own receipts plus all sellers' facilitated receipts. There is no current transaction-count alternative. If a remote seller first establishes its collection obligation this year, collection begins the first day of the first month at least 30 days later; physical-presence collection starts immediately. Current/prior-year nexus continues into the following year. [RCW 82.04.067](https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.067), [82.08.052(2),(4)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.052), [DOR remote sellers](https://dor.wa.gov/taxes-rates/retail-sales-tax/marketplace-fairness-leveling-playing-field/remote-sellers).

A facilitator collects on facilitated retail sales; the seller does not collect twice, but its registration/B&O reporting obligations remain. A facilitator is not merely an advertiser: DOR requires the contract to facilitate, communication of offer/acceptance and at least one listed facilitating activity. DOR also requires registration where its marketplace sellers have Washington physical presence. It must provide sellers the prior month's Washington gross-sales report by the 15th of the following month. Use the seller/facilitator reporting distinctions below. [DOR facilitators](https://dor.wa.gov/taxes-rates/retail-sales-tax/marketplace-fairness-leveling-playing-field/marketplace-facilitators).

## Boundary and exception table

Apply these to consumer sales, subject to documented resale/exemptions and the affiliation/public-agency holds below. “Excluded from this category” does not establish an exemption from every other retail category.

| Transaction | Treatment and operative limits | Source |
| --- | --- | --- |
| Goods, including clothing/footwear, electronics, furniture and supplies | Retail sales are taxable unless specifically excluded or exempt | [RCW 82.08.020(1)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.020) |
| Ordinary groceries and packaged chocolate/candy | Exempt food unless a prepared-food or vending rule applies; candy has no separate taxable category in this statute | [RCW 82.08.0293](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.0293) |
| Soft drinks, bottled water, supplements, alcohol | Food exemption does not cover prepared food, soft drinks, bottled water or supplements; alcohol is excluded from food. Soft drinks contain sweetener; exclude milk/milk substitutes and drinks with more than 50% fruit/vegetable juice. Plain/carbonated safety-sealed water can both be bottled water. Prescribed supplements have a separate exemption | [RCW 82.08.0293](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.0293), [82.08.925](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.925) |
| Prepared food | Heated food, seller-provided utensils or seller-mixed ingredients, subject to the statutory exceptions. Mixed-food exclusions cover merely cut/repackaged/pasteurized food and raw animal foods requiring cooking. Without seller-provided utensils, qualifying sector-311 manufacturing (except bakeries), unheated food by weight/volume and bakery items are excluded. Utensil delivery/availability and the more-than-75% prepared-sales test matter; four-or-more-serving packages have a limited exception. Special meal programs also have exceptions. Do not infer tax solely from “restaurant” or from ingredient count | [RCW 82.08.0293(2),(3)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.0293) |
| Vending food | Ordinary food selling price is 57% of gross receipts; for soft drinks, bottled water and hot prepared food (excluding food heated after dispensing), use total receipts divided by (1 + tax rate). Separate-statement/collection requirements are waived for this vending tax | [RCW 82.08.0293(4)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.0293) |
| Human-use prescription/OTC drugs; supplements | Drugs dispensed pursuant to a prescription are exempt; OTC drugs and dietary supplements for human use also have prescription exemptions. Do not apply a blanket “OTC always taxable” rule | [RCW 82.08.0281](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.0281), [82.08.940](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.940), [82.08.925](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.925) |
| Software, SaaS, digital goods and codes | Prewritten software, remote software access and digital products sold to consumers are retail sales; custom software/customization became retail sales on 1 October 2025 regardless of delivery. SaaS may be software access rather than DAS; software is not a digital good. A statutory digital code is not an ordinary stored-value/gift card | [RCW 82.04.050(6),(8)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.050), [82.04.192](https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.192) |
| Digital business purchase / multiple points of use (MPU) | Digital goods and services respecting those goods bought solely for business purposes have relief; this is not a blanket DAS/software exemption and excludes government activity from “business purposes.” Qualifying business/organization purchases concurrently available inside/outside WA can use an MPU certificate and directly pay apportioned state/local use tax. Advertising also has its own MPU provision; it is not restricted to advertising that qualifies as DAS. Personal use does not qualify. Obtain the required certificate/data; apportionment method is a hold below | [RCW 82.08.0208(3),(4),(6),(7)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.0208) |
| IT support, help desk, network support/training, data entry/processing | Retail services from 1 October 2025; web hosting, domain registration, payment processing, website development and separately classified software/DAS are not IT services. Do not infer that all excluded categories are exempt | [RCW 82.04.050(3)(g)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.050), [DOR IT](https://dor.wa.gov/taxes-rates/information-technology-services) |
| Website development; custom software/customization | Website design, development/support and consumer custom software are retail sales from 1 October 2025; hosting/domain registration are not website development. Apply the school/affiliate conditions | [RCW 82.04.050(3)(h),(6)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.050), [DOR new services](https://dor.wa.gov/taxes-rates/retail-sales-tax/services-newly-subject-retail-sales-tax) |
| Advertising | Digital/nondigital creation, preparation, production/dissemination and related marketing are retail services from 1 October 2025. Exclusions include hosting/domain registration, qualifying newspaper/printing/publishing/broadcast activity and out-of-home signage/naming rights; out-of-home does not include direct mail. MPU and affiliate rules can change collection. Standalone graphic design is generally not advertising; design sold as advertising, website development, goods or digital products can be taxable | [RCW 82.04.050(3)(k)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.050), [DOR FAQ](https://dor.wa.gov/frequently-asked-questions-about-essb-5814) |
| Live presentations | Paid interactive lectures, seminars, workshops/courses became retail sales from 1 October 2025. Exclusions include preschool classes and qualifying elementary/secondary/higher-education classes, performances, one-to-one instruction, qualifying religious-facility presentations and youth camps. From 1 July 2026 exclusions also cover on-site/in-person elementary-school before/after care, 501(c) nonprofit presentations, music lessons regardless of participants and instruction incidental to performances. Apply the school-buyer exemption and transition below; uncertain event classification is a hold | [RCW 82.04.050(3)(l)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.050), [DOR July exclusions](https://dor.wa.gov/forms-publications/publications-subject/special-notices/live-presentations-new-exclusions-retail-sales) |
| Investigation, security, monitoring, armored cars | Retail services from 1 October 2025; locksmiths are excluded from this category. Do not treat every HR/forensic/professional investigation as this retail service merely by its name; uncertain classification is a hold | [RCW 82.04.050(3)(i)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.050) |
| Temporary staffing | Retail from 1 October 2025. Hospital staffing under chapters 70.41/71.12 is excluded; qualifying paymaster amounts are excluded. Merely calling a worker an independent contractor does not settle whether the staffing-service definition is met. From 1 July 2026 the hospital exclusion also includes staffing used by hospital-based clinical providers to supplement hospital professional-service contracts AND for limited periods to supplement hospital staffing. Keep the declaration five years | [RCW 82.04.050(3)(j)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.050), [DOR hospital notice](https://dor.wa.gov/forms-publications/publications-subject/special-notices/temporary-staffing-services-modification-exclusion-retail-sales-staff-provided-hospitals) |
| Other retail services / warranties | Construction, goods repair/cleaning, landscaping, parking, towing, specified recreation/fitness, tanning/tattooing, catering and separately charged extended warranties require retail classification. Landscaping excludes qualifying farm horticulture and utility-line tree work; janitorial services are excluded from building-cleaning retail services. Fitness/recreation and warranty definitions have exceptions: do not tax every activity or every service contract by its label | [RCW 82.04.050(2),(3),(7),(15)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.050) |
| Professional work and portals | Email/file exchange alone does not make a professional service DAS. An incidental communications DAS exclusion requires sole use for communications and no consideration for that use; a paid DIY/template product can be different. Do not infer an exemption for IT consulting/advertising from the word “consulting” | [RCW 82.04.192(3)(b)(xiv)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.192), [DOR FAQ](https://dor.wa.gov/frequently-asked-questions-about-essb-5814) |

**Schools/libraries from 1 July 2026:** public libraries, library districts/service centers, K–12 schools, school districts and educational service districts can buy IT, website development, live presentations, investigation/security/armored-car services, temporary staffing and custom software/customization exempt. Advertising is not included. Obtain the prescribed certificate, retain five years; report gross sales under Retailing B&O and sales tax, then take “Sales of Exempt Services to Libraries and Schools” from sales tax. The extended existing-contract grace period for these exempt services and the newly excluded live/hospital services ends 30 June 2026; otherwise pre-July services remain taxable. [DOR school notice](https://dor.wa.gov/forms-publications/publications-subject/special-notices/new-salesuse-tax-exemption-purchases-certain-retail-services-schools-and-libraries).

**Affiliates/public agencies:** the retail definition has specific affiliate exclusions for listed services, custom software, qualifying human-effort DAS and data processing, plus an interlocal public-agency service exclusion. These are not blanket exemptions for all related-party software/staffing sales. Hold their eligibility and any bundled/overlapping classification: Check this point with one of our partner accountants. [RCW 82.04.050(17),(18), 2026 c 250](https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.050).

### Sourcing

For ordinary sales apply RCW 82.32.730(1) in order: (a) receipt at seller's business; (b) known purchaser/donee receipt elsewhere; (c) ordinary business-record purchaser address, absent bad faith; (d) transaction-time purchaser address, absent bad faith; (e) ship-from for goods, first available transmission for electronic software/digital goods, provided-from for warranties/DAS/other retail services, ignoring locations merely transferring the product digitally. “Receipt” means possession of goods, first use of services, or possession/first use of digital goods, whichever comes first; shipping-company possession does not count. [RCW 82.32.730(1),(9)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.730).

Vehicle/aircraft/watercraft, manufactured/modular/mobile homes, florists, direct mail, telecom, towing, advertising without local information and leases have special rules; **hold those sourcing outcomes** rather than applying “destination for ALL sales.” For ordinary equipment recurring leases, first payment follows the ordinary hierarchy and later payments the primary property location, but transport equipment/vehicles have different rules. Check this point with one of our partner accountants. [RCW 82.32.730(2)–(8)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.730).

### Use tax and resale

For untaxed goods first used in Washington, value is generally purchase price including seller-charged freight/delivery; prior extended use elsewhere can change value. State use tax is 6.5% plus local use tax where first used. Businesses report for that first-use period on the excise return; individuals can use My DOR or the Consumer Use Tax Return. Apply exemptions and any other-state tax credit before charging the full amount. [DOR use tax](https://dor.wa.gov/taxes-rates/use-tax).

**Law over older FAQ:** RCW 82.12.020(1)(c)(ii) expressly covers the listed IT, website, investigation/security, staffing and advertising retail services beginning 1 October 2025, as well as remote software services, subject to exclusions. Digital goods/codes/DAS and warranties are separately covered. Own-employee services are excluded. Do not rely on the older FAQ's blanket statement that these new services have no explicit use-tax imposition. Live-presentation/custom-delivery/deferred-sales-tax and credit/MPU computations that do not clearly fit the statute are held: Check this point with one of our partner accountants. [RCW 82.12.020](https://app.leg.wa.gov/RCW/default.aspx?cite=82.12.020).

Use reseller permits for eligible resale/ingredients without intervening use, never routine own-use office supplies or equipment. A permit alone does not make an own-use purchase wholesale. Sellers may use statutory approved certificates/data or annual electronic verification instead of retaining a permit copy; not every buyer requires the same document. DOR allows 120 days to gather wholesale documentation; keep it five years after sale. Permits generally last four years, but two years for contractors, newer businesses and other listed cases. When no valid permit is available, pay tax and consider DOR's tax-paid-at-source deduction/refund process. [RCW 82.04.470](https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.470), [DOR permits](https://dor.wa.gov/taxes-rates/retail-sales-tax/reseller-permits).

Misuse generally adds **50% of the tax due**. RCW 82.32.291 requires waiver for circumstances beyond the taxpayer's control or properly used dual-purpose purchases; do not present the penalty as unconditional. [RCW 82.32.291](https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.291).

### Periods before 1 October 2025 and existing contracts

Do not apply the new service rules or Q4 2026 rates retrospectively. Newly included service categories were previously outside retail sales to the extent they did not already qualify under another retail category; prewritten software, digital products and remote software access already had retail treatment. Check the transaction's actual date/classification. [DOR existing contracts](https://dor.wa.gov/laws-rules/interim-guidance-statement-regarding-contracts-existing-prior-october-1-2025-and-changes-made-essb).

An eligible contract was signed/executed before 1 October 2025, supplies services continuing on/after that date and concerns services newly retail on that date. If fully paid before that date, DOR deems the sale earlier. Otherwise unaltered contracts could retain prior treatment through 31 March 2026; reporting periods beginning 1 April require retail treatment unless otherwise provided by law. Material changes trigger retail treatment when altered; a notice email change alone is not material. Election to retail B&O early also requires sales-tax collection unless exempt. Apply the special June extension above where eligible. [DOR existing contracts](https://dor.wa.gov/laws-rules/interim-guidance-statement-regarding-contracts-existing-prior-october-1-2025-and-changes-made-essb).

## Worked cases

**A: delivery decision, original 5 November 2026 case:** Seattle retailer, $1,000 laptop, Spokane-city delivery versus Seattle collection. Assuming the ordinary goods rule and these exact city codes: $91.00 versus $105.50, a $14.50 difference. Report direct sales at code 3210 or 1726 respectively. [Sourcing statute](https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.730), [Q4 rates](https://dor.wa.gov/sites/default/files/2026-08/Q426_LSU-flyer-by-county.pdf).

```oa-check
name: Seattle sale shipped to Spokane against collected in Seattle (Q4 2026)
inputs:
  price: 1000
  spokane_rate: 0.091
  seattle_rate: 0.1055
steps:
  - tax_shipped: price * spokane_rate
  - tax_collected: price * seattle_rate
  - difference: tax_collected - tax_shipped
expected:
  tax_shipped: 91.00
  tax_collected: 105.50
  difference: 14.50
```

**B: registration decision, original 2026 case:** Oregon seller, no WA presence/domicile, no 2025 nexus; direct $80,000 + facilitated $30,000 = $110,000, first passing $100,000 on 20 August 2026. Collection begins 1 October 2026. Exactly $100,000 would not itself meet the receipts test. These annual totals establish nexus; **do not treat all $80,000 as taxable post-commencement sales**. For each reporting period report its actual gross receipts, deduct facilitated receipts only from sales tax where the facilitator collected, and report direct taxable post-commencement sales by location. B&O treatment is separate. [Nexus/commencement](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.052), [DOR marketplace reporting](https://dor.wa.gov/taxes-rates/retail-sales-tax/marketplace-fairness-leveling-playing-field/marketplace-sellers).

```oa-check
name: Oregon remote seller annual receipts test (not a return allocation)
inputs:
  direct_sales: 80000
  marketplace_sales: 30000
  threshold: 100000
steps:
  - wa_receipts: direct_sales + marketplace_sales
  - must_register: clamp(wa_receipts - threshold, 0, 1)
expected:
  wa_receipts: 110000
  must_register: 1
```

Further original cases, with amounts unchanged:

1. **Tacoma IT, November 2026:** $5,000 help-desk support, unrelated ordinary business customer at code 2717, no exemption: $525 tax. A qualifying Tacoma school district's covered purchase is exempt with the required certificate from July 2026. [IT](https://dor.wa.gov/taxes-rates/information-technology-services), [school notice](https://dor.wa.gov/forms-publications/publications-subject/special-notices/new-salesuse-tax-exemption-purchases-certain-retail-services-schools-and-libraries), [rates](https://dor.wa.gov/sites/default/files/2026-08/Q426_LSU-flyer-by-county.pdf).
2. **15 September 2025 contract:** continuing support billed monthly qualifies for transition only if signed/executed and newly retail; use the existing-contract section, including material alterations, prepaid price, early election and the July school exception. No indefinite grandfathering.
3. **Olympia printer:** original $3,000 Oregon purchase, no tax, first business use at code 3403 in Q4 2026, no exemption/credit: $300 use tax. [DOR use tax](https://dor.wa.gov/taxes-rates/use-tax), [rates](https://dor.wa.gov/sites/default/files/2026-08/Q426_LSU-flyer-by-county.pdf).
4. **Grocery chocolate and spring water:** ordinary packaged bar, not prepared/vending food, is exempt; sealed plain spring water is taxable absent a separate exemption. [RCW 82.08.0293](https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.0293).
5. **Seattle permit misuse:** original $1,000 own-use office supplies, Q4 code 1726, no exemption/credit: tax $105.50. If no statutory waiver applies, penalty $52.75; combined $158.25 before other charges. [RCW 82.32.291](https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.291), [rates](https://dor.wa.gov/sites/default/files/2026-08/Q426_LSU-flyer-by-county.pdf).
6. **Late $2,000 payment:** original due date 25 November 2026, received 10 December: 9% = $180. Not received by 31 December: total 19% = $380; not received by 31 January 2027: total 29% = $580, subject to any legally adjusted deadline/relief. Interest is a separate computation held below, not an invented flat addition. [RCW 82.32.090(1)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.090).

### Original historical cases: inputs retained, unsupported outcomes held

The following are the original 2025 v1 tests and the undated predecessor tests/edge cases. Their percentages are preserved **as original inputs only**, not verified historical rates. Arithmetic shown here does not authorize a filing. Every held row requires: **Check this point with one of our partner accountants.** Do not substitute 2026 rates or silently date the undated cases.

| Original ID | Original inputs and disposition |
| --- | --- |
| 2025 v1 T1 | $500 goods, Seattle pickup, 10.10%; arithmetic $50.50, historical rate application held |
| 2025 v1 T2 | Seattle ships $1,000 to Spokane, 8.90%; arithmetic $89.00, historical rate application held |
| 2025 v1 T3 | $200 SaaS, Bellevue 10.10%; arithmetic $20.20, classification/date/rate application held |
| 2025 v1 T4 | $5,000 Seattle consulting; old automatic $0 result withdrawn; service details/date needed, held |
| 2025 v1 T5 | $2,000 office furniture from Oregon, no tax, Tacoma 10.30%; arithmetic $206.00, historical rate/credit application held |
| Predecessor EC1 | $1,000 Seattle sale, old 10.25% sales rate and .471% B&O; arithmetic $102.50 and $4.71; both rate applications/B&O outcome held |
| Predecessor EC2 | $100/month cloud accounting/HR platform; oldest version uses Seattle 10.25%, arithmetic $10.25; later version gives no location/rate. Keep both variants; tax/classification/date/rate outcome held |
| Predecessor EC3 | Electronic custom software; later variant $20,000, earlier no amount; unknown date and mixed consulting/software, tax outcome held |
| Predecessor EC4 | Seattle ships to Spokane, old 8.90% versus 10.25%, no amount; ordinary sourcing hierarchy retained above, historical rates held |
| Predecessor EC5 | Overall income/B&O/capital-gains structure in oldest version; vendor collection allowance in later version. Both answers held; no no-income-tax or discount assertion supplied |
| Predecessor EC6 | Seattle hotel room $200/night; lodging and total tax outcome held |
| Predecessor EC7 | Out-of-state seller asks about SST/SSTRS registration, UBI/licence; procedure held |
| Predecessor EC8 | Licensed cannabis retailer; old 37% excise/base assertion held, no computation authorized |
| Predecessor EC9 | Plain bottled water versus flavored/carbonated water: withdraw old plain-water exemption; apply the food/water definitions above, not carbonation alone |
| Predecessor EC10 | Optional extended warranty with goods: apply the statutory definition, separate charge and consumer rules above; do not treat every service agreement as a warranty |
| Predecessor T1 | $1,000 Seattle laptop, 10.25%; arithmetic $102.50, total $1,102.50; rate application held |
| Predecessor T2 | $200 bread/milk/produce: $0 sales tax only for ordinary exempt grocery food, not prepared/vending food |
| Predecessor T3 | $300/month Spokane cloud HR, 8.90%; arithmetic $26.70; date/classification/rate application held |
| Predecessor T4 | Oregon online seller, no presence, $120,000 current-year WA sales: receipts exceed threshold; collection commencement needs crossing date/prior year; do not assume immediate retrospective tax |
| Predecessor T5 | Seattle ships $500 to Vancouver, 8.60%; arithmetic $43.00; historical rate application held |
| Predecessor T6 | $5 no-flour chocolate bar, Tacoma 10.20%; old $0.51 taxable-candy result corrected to $0 if ordinary packaged food, not prepared/vending. Flour is not this statute's test |
| Predecessor T7 | $300 Seattle jacket, 10.25%; arithmetic $30.75; historical rate application held |
| Predecessor T8 | $50 optional TV warranty, Seattle 10.25%; arithmetic $5.125 rounds $5.13; historical rate/contract application held |
| Predecessor T9 | Seattle $3,000 Oregon office equipment, no tax, 10.25%; arithmetic $307.50; date/rate/credit application held |
| Predecessor T10 | $20,000 electronic custom software, Seattle, old implicit 10.25%; arithmetic $2,050; date, transition, classification and rate application held |

## Filing and payment

Use My DOR's combined excise return. Report actual-period gross retail sales under Retailing B&O and sales tax; claim only supported deductions. A marketplace **seller** deducts “Gross Sales Collected by Facilitator” from sales tax when the facilitator collected, and excludes those facilitated amounts from its local-sales allocation; no such deduction removes its B&O receipts. A **facilitator** reports facilitated sales for sales tax, while its retailing-B&O deduction for others' sales is “Other” with the required explanation; commission/service income has separate B&O treatment. A certified service provider handling sales tax does not necessarily discharge the seller's B&O return obligation. [DOR sellers](https://dor.wa.gov/taxes-rates/retail-sales-tax/marketplace-fairness-leveling-playing-field/marketplace-sellers), [DOR facilitators](https://dor.wa.gov/taxes-rates/retail-sales-tax/marketplace-fairness-leveling-playing-field/marketplace-facilitators).

| Assigned frequency | Annual tax-liability band / ordinary deadline | Source |
| --- | --- | --- |
| Annual | $1,050 or less; April 15 following the year | [DOR frequencies](https://dor.wa.gov/file-pay-taxes/filing-frequencies-due-dates), [RCW 82.32.045](https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.045) |
| Quarterly | $1,051–$4,800; last day of following month (April 30, July 31, October 31, January 31) | [DOR frequencies](https://dor.wa.gov/file-pay-taxes/filing-frequencies-due-dates), [RCW 82.32.045](https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.045) |
| Monthly | $4,801 or greater; 25th of following month | [DOR frequencies](https://dor.wa.gov/file-pay-taxes/filing-frequencies-due-dates), [RCW 82.32.045](https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.045) |

DOR assigns frequency, initially using estimated income; do not self-select from this table. Weekend/legal-holiday deadlines move to the next business day. Request extensions before the deadline. Active nonreporting requires all conditions: B&O activity under $125,000/year, public-utility income under $24,000/year and no obligation to collect/pay another DOR tax/fee; it is not available merely because sales are below the nexus threshold. [RCW 82.32.045(5)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.045), [DOR frequencies](https://dor.wa.gov/file-pay-taxes/filing-frequencies-due-dates), [late filing](https://dor.wa.gov/file-pay-taxes/late-filing).

Late return-tax payment attracts 9%, total 19% if still unpaid by the end of the following month, total 29% by the end of the second following month; minimum $5. These are not 5%-per-month penalties. Assessment, substantial-underpayment, warrant, unregistered-business, written-instruction/e-filing, avoidance and evasion penalties have separate bases, conditions, disclosure exceptions and stacking limits; their application is held below. [RCW 82.32.090](https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.090).

ESSB 5814 penalty relief is conditional, not automatic: uncollected sales/unpaid use tax caused by the changes, periods 1 October 2025–31 December 2026; application by 30 September 2027 through the Voluntary Disclosure Application and signed agreement returned within 30 days **of application**. For preexisting contracts, relief begins when temporary relief ends or 1 April 2026, whichever is earlier. Tax/interest remain due; evasion, negligence and tax-avoidance penalties are excluded. Follow the assessment/invoice payment deadline. [DOR relief](https://dor.wa.gov/taxes-rates/retail-sales-tax/services-newly-subject-retail-sales-tax/essb-5814-penalty-relief-program).

Keep tax records, including federal/state returns, five years; failure can bar challenging the assessment in court. Ordinary assessment limit is four years **after close of the tax year**, not four years from filing; unregistered taxpayers, fraud/material misrepresentation and written waivers are exceptions. [RCW 82.32.070](https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.070), [82.32.050(4)](https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.050).

## When to refuse or refer

The following outcomes are **non-usable holds**. Preserve the facts and documents; do not apply the old percentage, exemption or procedure. For each: **Check this point with one of our partner accountants.**

- B&O rates, classifications, expense deductions, credits, apportionment and separately stated recovery; capital gains, personal/corporate income-tax answers, payroll and multi-state obligations.
- Special taxes: cannabis (including the old 37%/tax-base claim), liquor/tobacco, lodging (including the $200/night case), motor vehicle/rental, real-estate excise and tribal/Indian-country sales.
- Manufacturing M&E, farm machinery/inputs, prosthetics/medical devices, government/nonprofit purchases, fuel, trade-ins, newspapers, nonresident/interstate exemptions and export-delivery evidence. No blanket agricultural/government exemption or “state-only M&E rate” is authorized.
- MPU/other-state-credit calculations, unclassified hosting/domain/payment or mixed professional/digital packages, affiliated/public-agency eligibility, unusual live/recreation/fitness/investigation/staffing cases, special sourcing and leases identified above.
- Historical rate/date gaps in the retained cases; vendor collection discounts, SST/SSTRS procedures, excess tax collection/refunds, electronic-filing exceptions, No Local Activity deduction, voluntary disclosure, audits, assessments, appeals and penalty stacking/waivers beyond the express rules above. Interest amount and accrual dates require a separate verified computation; no 2026 or 2027 interest rate is supplied here.

## Completion checklist

- [ ] Nexus, measurement year, start date and facilitator role documented
- [ ] Every item/exemption and any transition/affiliation condition resolved or expressly held
- [ ] Receipt address, quarter, location code and rate evidenced
- [ ] Period receipts/deductions reconciled; historic cases not used as current rates
- [ ] Use tax, permits, return deadline and records addressed; held outcomes not used for filing

## Sources

All read 2026-11-27; the old digital-products article/FAQ is not authority over the amended statutes. The Q4 PDF and its official spreadsheet were both read and their city figures agree.

| Source | URL | Read on |
| --- | --- | --- |
| Read for State rate and retail base | https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.020 | 2026-11-27 |
| Read for Nexus, receipts and presence | https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.067 | 2026-11-27 |
| Read for Collection commencement | https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.052 | 2026-11-27 |
| Read for Retail definition; both 2026 amendments, not the 2029 text | https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.050 | 2026-11-27 |
| Read for Digital definitions | https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.192 | 2026-11-27 |
| Read for Digital/advertising exemptions and MPU | https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.0208 | 2026-11-27 |
| Read for Food | https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.0293 | 2026-11-27 |
| Read for Prescription drugs | https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.0281 | 2026-11-27 |
| Read for OTC drugs | https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.940 | 2026-11-27 |
| Read for Prescribed supplements | https://app.leg.wa.gov/RCW/default.aspx?cite=82.08.925 | 2026-11-27 |
| Read for Sourcing and exceptions | https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.730 | 2026-11-27 |
| Read for Use-tax imposition, including 2026 amendments | https://app.leg.wa.gov/RCW/default.aspx?cite=82.12.020 | 2026-11-27 |
| Read for Wholesale evidence | https://app.leg.wa.gov/RCW/default.aspx?cite=82.04.470 | 2026-11-27 |
| Read for Misuse and mandatory waiver | https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.291 | 2026-11-27 |
| Read for Return deadlines/nonreporters | https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.045 | 2026-11-27 |
| Read for Penalties | https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.090 | 2026-11-27 |
| Read for Records | https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.070 | 2026-11-27 |
| Read for Assessment/interest limits | https://app.leg.wa.gov/RCW/default.aspx?cite=82.32.050 | 2026-11-27 |
| Read for Numeric state/local rate and collection | https://dor.wa.gov/taxes-rates/retail-sales-tax | 2026-11-27 |
| Read for Rate lookup | https://dor.wa.gov/taxes-rates/sales-use-tax-rates | 2026-11-27 |
| Read for Q4 2026 PDF | https://dor.wa.gov/sites/default/files/2026-08/Q426_LSU-flyer-by-county.pdf | 2026-11-27 |
| Read for Q4 2026 spreadsheet | https://dor.wa.gov/sites/default/files/2026-08/Q426_Excel_LSU-rates-alpha.xlsx | 2026-11-27 |
| Read for Remote sellers | https://dor.wa.gov/taxes-rates/retail-sales-tax/marketplace-fairness-leveling-playing-field/remote-sellers | 2026-11-27 |
| Read for Marketplace sellers | https://dor.wa.gov/taxes-rates/retail-sales-tax/marketplace-fairness-leveling-playing-field/marketplace-sellers | 2026-11-27 |
| Read for Marketplace facilitators | https://dor.wa.gov/taxes-rates/retail-sales-tax/marketplace-fairness-leveling-playing-field/marketplace-facilitators | 2026-11-27 |
| Read for Filing frequencies | https://dor.wa.gov/file-pay-taxes/filing-frequencies-due-dates | 2026-11-27 |
| Read for Use tax valuation/reporting | https://dor.wa.gov/taxes-rates/use-tax | 2026-11-27 |
| Read for Reseller permits | https://dor.wa.gov/taxes-rates/retail-sales-tax/reseller-permits | 2026-11-27 |
| Read for IT boundaries | https://dor.wa.gov/taxes-rates/information-technology-services | 2026-11-27 |
| Read for Service list and litigation | https://dor.wa.gov/taxes-rates/retail-sales-tax/services-newly-subject-retail-sales-tax | 2026-11-27 |
| Read for FAQ, only where consistent with amended law | https://dor.wa.gov/frequently-asked-questions-about-essb-5814 | 2026-11-27 |
| Read for July school exemption | https://dor.wa.gov/forms-publications/publications-subject/special-notices/new-salesuse-tax-exemption-purchases-certain-retail-services-schools-and-libraries | 2026-11-27 |
| Read for July live-presentation exclusions | https://dor.wa.gov/forms-publications/publications-subject/special-notices/live-presentations-new-exclusions-retail-sales | 2026-11-27 |
| Read for July hospital exclusion | https://dor.wa.gov/forms-publications/publications-subject/special-notices/temporary-staffing-services-modification-exclusion-retail-sales-staff-provided-hospitals | 2026-11-27 |
| Read for Existing contracts | https://dor.wa.gov/laws-rules/interim-guidance-statement-regarding-contracts-existing-prior-october-1-2025-and-changes-made-essb | 2026-11-27 |
| Read for Penalty relief | https://dor.wa.gov/taxes-rates/retail-sales-tax/services-newly-subject-retail-sales-tax/essb-5814-penalty-relief-program | 2026-11-27 |
| Read for Extension requests | https://dor.wa.gov/file-pay-taxes/late-filing | 2026-11-27 |

Not yet confirmed: no unresolved outcome is usable; the explicitly identified holds require partner-accountant resolution. Future rates and litigation outcomes must not be inferred. DOR currently directs affected sellers to report, collect and remit under current guidance despite the proceedings; this Guide does not authorize stopping collection. [DOR litigation notice](https://dor.wa.gov/taxes-rates/retail-sales-tax/services-newly-subject-retail-sales-tax).
