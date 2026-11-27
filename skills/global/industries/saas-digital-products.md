---
name: saas-digital-products
description: "For 2026 SaaS and digital-product businesses: reconcile contracts, hosted-service revenue, licences, implementation, acquisition costs and platform settlements; map EU OSS and country VAT, sales-tax, withholding and presence questions without applying unsupported global rates."
version: 1.1
jurisdiction: GLOBAL
tax_year: 2026
last_updated: 2026-11-27
depends_on:
  - corporate-income-tax-workflow-base
category: vertical
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
type: cross-country-method
domain: tax
---

# SaaS and digital products v1.1

## Scope

A cross-country method for subscription software, hosted applications, app developers and digital marketplaces in 2026. It produces a contract revenue schedule, settlement reconciliation and country tax questions. It does not calculate a customer's tax from a global standard-rate table. Load `corporate-income-tax-workflow-base` and the country VAT and income tax jobs before a return computation.

Financial reporting and tax are separate. The accounting method below uses the IFRS revenue model, for for-profit customer contracts, using Australian adopted text for the cited paragraphs. Match the compilation to the annual reporting period’s start: the linked original AASB 15/AASB 138 compilations cover starts before 1 July 2026; the [later AASB 15](https://standards.aasb.gov.au/aasb-15-dec-2022-0) and [later AASB 138](https://standards.aasb.gov.au/aasb-138-dec-2022-0) compilations cover starts from 1 July 2026 to before 1 January 2027. This does not turn Australian adoption or its disclosure tiers into universal IFRS compliance. Confirm the reporting framework and local adoption; do not silently apply it as US GAAP or cash-basis tax accounting. This is not software engineering, SOC 2, ISO 27001 or app-store pricing advice.

## Quick reference

| Question | First instruction | Source |
| --- | --- | --- |
| When is subscription revenue earned? | Identify the promise and how control transfers; a hosted service is not a delivered software licence merely because it was billed | [AASB 15, paragraphs 22-38](https://standards.aasb.gov.au/aasb-15-dec-2022) |
| Is cash collected revenue? | Reconcile earned revenue, unconditional receivables, contract assets and contract liabilities separately | [AASB 15, paragraphs 105-109](https://standards.aasb.gov.au/aasb-15-dec-2022) |
| Does a marketplace payout equal sales? | Assess principal or agent for each specified service before gross or net reporting | [AASB 15, paragraphs B34-B38](https://standards.aasb.gov.au/aasb-15-dec-2022) |
| Which EU scheme covers software services? | Consider Union or non-Union OSS. Import OSS concerns goods, not an electronically supplied service | [European Commission, OSS scope](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en) |

## Ask the client first

- Which entity earns the income, where is it tax resident, and which reporting framework, accounting basis and reporting dates apply?
- What does each contract promise: hosted access, a licence, implementation, support, updates or a physical product?
- Where are the customers, are they businesses or consumers, and what location/status evidence is held?
- Who controls the service before supply, and is the intermediary an agent, reseller or merchant of record?
- What are the billings, receipts, refunds, variable fees, renewal rights, costs and outstanding obligations by contract?
- Where are staff, agents, servers and decision makers, and are there existing local registrations or elections?

## The method, step by step

1. Confirm a customer contract within the revenue standard’s scope; leases, insurance and financial instruments require their applicable standards. Apply paragraph 9 only when approval/commitment, identifiable rights, identifiable payment terms, commercial substance and probable collection are all present. Enforceability is a legal assessment. Do not treat a customer deposit as earned income simply because it is non-refundable. For a combination or modification whose paragraph 17–21 outcome is unresolved, do not compute a revenue adjustment. Check this point with one of our partner accountants.
2. Identify distinct goods and services. Both the ability to benefit from a service and its separation within the contract matter. Setup administration alone is not a separate performance obligation. Installation that significantly integrates or modifies the software may form a combined promise.
3. Determine consideration, including discounts, usage charges, refund rights and non-cash amounts. Estimate variable consideration using the expected value or most likely amount, whichever better predicts entitlement, consistently; include it only to the extent it is highly probable a significant cumulative revenue reversal will not occur on resolution, and reassess each reporting period. The special royalty rule applies where the royalty relates only to an intellectual-property licence or that licence is the predominant item: recognise at the later of sale/use and satisfaction (or partial satisfaction) of the allocated obligation. Otherwise use the ordinary variable-consideration rules.
4. Allocate consideration using relative stand-alone selling prices. Allocate a discount specifically only with observable evidence from regular stand-alone sales and comparable discounted bundles identifying that obligation; allocate a variable amount specifically only when its terms relate specifically to that obligation/service and doing so meets the allocation objective considering the whole contract. A price ramp does not by itself prove a changing service pattern.
5. Establish over-time or point-in-time recognition. Over-time recognition requires simultaneous customer receipt/consumption, customer control of an asset being created/enhanced, or both no alternative use and an enforceable right to payment for performance to date. Otherwise recognise when control transfers at a point in time. For a constant hosted stand-ready service satisfying the over-time test, a time measure may faithfully depict performance; reassess progress at each reporting date. A licence requires a separate right-to-access or right-to-use assessment, when the customer can use it, and any combined obligations. A distinct licence gives access over time only when expected activities significantly affect the intellectual property, expose the customer to their effects and do not themselves transfer a separate service; otherwise test the right to use at a point in time, never before the customer can use and benefit from it. Downloadability alone is not the test.
6. Record contract balances and reconcile earned revenue to billings and cash. An amount earned before it becomes an unconditional right to payment is a contract asset, not deferred revenue. Refund liabilities, credit losses and price concessions are different items.
7. Assess acquisition and fulfilment costs, then perform the separate country tax, VAT, withholding and permanent establishment work below. Costs incurred regardless of obtaining the contract are expensed unless explicitly chargeable regardless of success. For fulfilment costs, first apply any other applicable standard; otherwise capitalise only if directly related to an identified contract/anticipated contract, creating or enhancing resources for future performance, and expected to be recovered. Expense general administration unless explicitly chargeable, waste, past-performance costs and costs indistinguishable between past and future performance. Do not infer deductibility from accounting expense recognition.

Authority for steps 1-6: [AASB 15, paragraphs 9-45, 47-90, 105-109 and B48-B63B](https://standards.aasb.gov.au/aasb-15-dec-2022). Step 7 uses paragraphs 91-104. Read the matching [July–December 2026 AASB 15 compilation](https://standards.aasb.gov.au/aasb-15-dec-2022-0) for periods beginning in that window. Other frameworks, early adoption and not-for-profit/public-sector arrangements need a separate applicability conclusion.

## Revenue and cost decisions

| Topic | Apply to the actual contract | Source |
| --- | --- | --- |
| Subscription, support and updates | Identify the series of services and a faithful progress measure, including promised upgrades | [AASB 15, paragraphs 22-40](https://standards.aasb.gov.au/aasb-15-dec-2022) |
| Implementation | Test both limbs of distinctness; a customer using another provider is evidence, not the entire test | [AASB 15, paragraphs 27-30](https://standards.aasb.gov.au/aasb-15-dec-2022) |
| Activation fee | If no separate service transfers, allocate to the future services; extend beyond the initial term only where the renewal option creates a material right | [AASB 15, paragraphs B48-B51](https://standards.aasb.gov.au/aasb-15-dec-2022) |
| Usage fees and performance bonuses | Apply estimation, constraint and allocation requirements; recognise a qualifying intellectual-property royalty no earlier than the applicable sale/use and satisfied obligation | [AASB 15, paragraphs 50-59, 84-86 and B63-B63B](https://standards.aasb.gov.au/aasb-15-dec-2022) |
| Sales commissions | Capitalise incremental, recoverable acquisition costs. Amortise consistently with the related goods/services, including supported anticipated contracts; update for changed expected transfer timing. Impair when carrying amount exceeds remaining expected consideration less directly related unexpensed fulfilment costs, adjusting consideration for customer credit risk without applying the variable-consideration constraint to that impairment estimate; apply other-standard impairment first. Test the resulting asset with its cash-generating unit; a later reversal cannot exceed the no-impairment carrying amount | [AASB 15, paragraphs 91-104](https://standards.aasb.gov.au/aasb-15-dec-2022) |
| Acquisition-cost practical expedient | Expense is an election where the otherwise recognised asset's amortisation period would be one year or less, including exactly one year | [AASB 15, paragraph 94](https://standards.aasb.gov.au/aasb-15-dec-2022) |
| Customer's cloud setup costs | First test identifiability, control and future economic benefits, then probable benefits and reliable cost measurement. A hosted service does not automatically make every implementation cost an immediate expense; where no asset is identified, the timing of services received or prepaid still needs assessment. Do not use this preliminary asset test as a completed cloud-cost conclusion. Check this point with one of our partner accountants. | [IAS 38 recognition principles in AASB 138, paragraphs 8-23](https://standards.aasb.gov.au/aasb-138-dec-2022) |

US ASC 606, ASC 340-40, ASC 985-20 and cloud implementation under ASC 350-40 remain separate framework review topics. Do not use the IFRS case as an ASC conclusion. Check this point with one of our partner accountants. This file does not claim that their detailed rules or effective amendments were read for this edition; see the held items in Sources.

## Worked case: a ramp creates an asset, not deferred revenue

Fabricated currency units, excluding VAT, financing, credit losses and contract changes. One enforceable hosted-service obligation is provided evenly over three years. Fixed consideration is 100,000 in the first year and 150,000 in each following year. Assume the assessed performance pattern supports equal annual revenue, all billed amounts are collected, and future billing remains conditional on further performance.

The total contract price is 400,000. Annual revenue is 133,333.33 before rounding adjustments. At the first year end, earned revenue exceeds the 100,000 billed by 33,333.33: a contract asset. At the second year end, cumulative revenue is 266,666.67 and cumulative billings are 250,000: the remaining contract asset is 16,666.67. Allocate the rounding remainder so cumulative recognised revenue finishes at the contract price. If the right to the extra amount were already unconditional, that balance would instead be a receivable.

```oa-check
name: Constant SaaS service with billing ramp
inputs:
  bill_year_one: 100000
  bill_year_two: 150000
  bill_year_three: 150000
  years: 3
steps:
  contract_price: bill_year_one + bill_year_two + bill_year_three
  annual_revenue: contract_price / years
  first_asset: annual_revenue - bill_year_one
  second_asset: annual_revenue * 2 - bill_year_one - bill_year_two
expected:
  contract_price: 400000
  annual_revenue: 133333.33
  first_asset: 33333.33
  second_asset: 16666.67
```

Boundary case: preserve the original two alternatives—implementation specific to the SaaS, versus implementation available from another vendor. Neither fact alone decides distinctness. If either limb of distinctness fails, combine promises and assess the combined performance pattern; if implementation is distinct, allocate consideration using stand-alone selling prices and recognise that obligation as it transfers. Do not spread it automatically over the subscription or recognise it automatically on invoice. [AASB 15, paragraphs 27-30, 35-38 and 73-86](https://standards.aasb.gov.au/aasb-15-dec-2022).

## European Union

Distinguish business customers from consumers, establish the place of supply and retain customer-location evidence. For a supplier using OSS, first establish which scheme and supplies it covers. Union and non-Union OSS returns supplement domestic VAT obligations; they do not replace them. Choosing a scheme means including all supplies within that scheme's scope, not selecting only convenient countries. The Commission distinguishes electronic services from imported goods in its [OSS scheme overview](https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en).

Do not apply Import OSS to a SaaS subscription. For mixed hardware/software, separate the goods import analysis from the service analysis. Route destination rates, customer-status evidence, the small-supplier place-of-supply derogation and reverse-charge conditions to the applicable country VAT job; no universal exemption threshold is set here. For the legacy Article 44/58, customer-evidence, small-supplier derogation and reverse-charge questions, this Guide gives no completed tax conclusion. Check this point with one of our partner accountants.

## United Kingdom

This section is a non-usable country-tax handoff, not a registration, rate or taxability conclusion. Check this point with one of our partner accountants.

Use the UK digital-services VAT rules and supplier establishment analysis, rather than an EU OSS registration as proof of UK compliance. Check whether the supplier has a UK establishment, whether the customer is a business, who supplies through the platform and the correct registration route. The legacy label "VOES" and an assumed standard rate do not establish registration eligibility. UK rates, non-established supplier registration and Making Tax Digital are held for the country job; this file does not instruct a return filing.

## Australia and Canada

This section is a non-usable country-tax handoff, not a registration, rate or taxability conclusion. Check this point with one of our partner accountants.

For Australia, test imported digital services separately from low-value physical goods; identify consumer status, relevant turnover, the party responsible for GST and any reverse-charge issue. For Canada, distinguish ordinary from simplified GST/HST registration, the relevant rolling sales test, customer registration evidence, platform responsibility and provincial PST/RST/QST. Do not apply a consumer simplified regime indiscriminately to registered business customers. The old headline thresholds and rates are held pending the relevant current country source, not inherited from a dated global list.

## India and other countries

This section is a non-usable country-tax handoff, not a registration, rate or taxability conclusion. Check this point with one of our partner accountants.

For India, keep OIDAR, recipient status, supplier registration, GST and equalisation levy as separate questions. Do not use an old levy statement without checking its repeal and transaction dates. For New Zealand, Singapore, Japan, South Korea, Mexico, Chile and Argentina, retain a country workpaper for digital-service registration, rates, platform collection and withholding as applicable. Each country's job must supply its own current values and conditions. No prior rate list is a 2026 rates card.

## United States and cross-border presence

This section is a non-usable country-tax handoff, not a registration, rate or taxability conclusion. Check this point with one of our partner accountants.

US state sales-tax nexus, SaaS taxability and marketplace-facilitator responsibilities remain separate state-law checks. Wayfair is not a single nationwide registration threshold or a uniform definition of taxable SaaS. Preserve the original state questions for California, New York, Texas, Florida, Washington, Illinois, Pennsylvania, Massachusetts, Ohio, Virginia, Tennessee, Georgia and North Carolina. This edition supplies no state rate, exemption percentage or transaction-count safe harbour; load the relevant state job and read its current law.

Separately map staff, dependent agents, local sales/support offices and servers for income-tax permanent establishment and withholding. Do not conclude "no PE" from a purely hosted delivery model or from a server being outside the customer country. Obtain an applicable treaty/domestic-law analysis of the actual functions before taking a PE or withholding position. Check this point with one of our partner accountants. Load `digital-services-tax-matrix` for the DST question, but confirm the covered tax and date before quoting it. Do not use a Pillar One/Amount A proposal or the old DST country count as an operative tax rule. Check this point with one of our partner accountants.

## Management measures and reconciliations

Maintain MRR, ARR, bookings, remaining performance obligations, churn, net revenue retention, customer acquisition cost and lifetime value as explicitly defined management measures. They are not interchangeable with recognised revenue or financial-statement assets. Reconcile the subscription ledger to the general ledger, exclude tax collected for third parties, identify credits/refunds and explain contract assets/liabilities separately from receivables. Under AASB 15 paragraphs 120–122, RPO disclosure covers allocated transaction price for unsatisfied/partly satisfied obligations and expected revenue timing; the paragraph 121 expedient covers contracts originally one year or less or revenue recognised under paragraph B16, with qualitative explanation under paragraph 122. Check any local simplified-disclosure framework separately; a marketing backlog number is not automatically that disclosure. See [AASB 15, paragraphs 47, 105-122](https://standards.aasb.gov.au/aasb-15-dec-2022).

## When to refuse or refer

- Missing contracts, disputed enforceability, unresolved gross/net status or an unmeasurable service pattern: give a missing-evidence schedule, not a completed revenue conclusion.
- Unconfirmed country rate, registration test, repeal, digital levy, withholding or PE: stop that computation and hand over the exact country question.
- A requested ASC result without the applicable current codification or an accounting/tax basis mismatch: retain a framework reconciliation for professional review.
- Never turn ARR, a billing schedule, a payment-processor payout or a platform tax collection feature into proof that all obligations are met.

## Completion checklist

- Contract and obligations supported; distinctness, licence and progress conclusions recorded.
- Discounts, ramps, refunds, variable consideration, commission assets and impairment assessed.
- Contract balances reconcile to billing, cash and the ledger.
- Customer location/status, platform role and every country registration question tracked.
- US state, DST, PE, withholding and local staff questions handed to their current country jobs.
- All held figures below remain absent from any usable calculation.

## Sources

| Source | URL | Read on | Read for |
| --- | --- | --- | --- |
| AASB 15, December 2022 compilation, incorporating IFRS 15 | https://standards.aasb.gov.au/aasb-15-dec-2022 | 2026-11-27 | Read for Sections on recognition, measurement, contract costs and presentation; paragraphs 9-45, 47-109, 120-122, B34-B63B; compilation period and IFRS comparison |
| AASB 138, December 2022 compilation, incorporating IAS 38 | https://standards.aasb.gov.au/aasb-138-dec-2022 | 2026-11-27 | Read for Definitions, control and recognition paragraphs 8-23; preliminary asset test only, unresolved cloud-cost timing referred |
| AASB 15, compilation for annual periods starting July–December 2026 | https://standards.aasb.gov.au/aasb-15-dec-2022-0 | 2026-11-27 | Read for Operative-period boundary and corresponding for-profit customer-contract principles |
| AASB 138, compilation for annual periods starting July–December 2026 | https://standards.aasb.gov.au/aasb-138-dec-2022-0 | 2026-11-27 | Read for Operative-period boundary and paragraphs 8–23 asset/control/recognition tests |
| AASB current standards index | https://standards.aasb.gov.au/accounting-standards | 2026-11-27 | Read for Calendar-year 2026 and subsequent amendments, distinguishing public-sector insurance amendments from the cited for-profit revenue principles |
| European Commission, One Stop Shop | https://vat-one-stop-shop.ec.europa.eu/one-stop-shop_en | 2026-11-27 | Read for Background and scope sections, the three schemes and domestic-return boundary |

Not yet confirmed: current US ASC 606/340-40/985-20/350-40 detail and implementation amendments; each named US state's SaaS taxability, nexus and marketplace law, including the old Texas exclusion and Tennessee/North Carolina descriptions; EU Article 44/58 text and customer evidence/derogation conditions; UK digital registration route and rates; Australian imported-service/goods turnover tests and reverse-charge scope; Canadian simplified registration, rolling threshold and provincial regimes; Indian OIDAR scope/rate and equalisation-levy repeal dates; New Zealand, Singapore, Japan, South Korea, Mexico, Chile and Argentina digital taxes/withholdings; treaty/server PE conclusions; Pillar One commencement and DST country count. These are preserved research questions, not usable figures.
