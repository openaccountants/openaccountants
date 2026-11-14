---
name: ne-sales-tax
description: "Nebraska 2026 state/local sales-use computation: 5.5% ordinary state rate, actual local and Good Life District treatment, remote/marketplace nexus, software classifications and Form 10. Load us-sales-tax first."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ne-sales-tax"
  jurisdiction: "US-NE"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Nebraska sales and use tax, 2026

> **Built from the law. Not yet approved.** Written by Codex; this version has not been reviewed by an accountant. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

**Answer first:** Nebraska's ordinary state sales/use rate is 5.5%, plus the actual destination's local tax. Do not use a single statewide combined rate or apply the ordinary state rate to every Good Life District transaction. Remote nexus retains a transaction-count test. [DOR rates/sourcing FAQ](https://revenue.nebraska.gov/about/frequently-asked-questions/nebraska-sales-and-use-tax-faqs); [July-December 2026 local schedule](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/salestax/slstax_rates_07-01-2026.pdf); [77-2701.13](https://nebraskalegislature.gov/laws/statutes.php?statute=77-2701.13).

## Scope

Ordinary Nebraska retail sales/use, remote sellers and marketplace facilitators. Load `us-sales-tax` first for the multistate framework. Product definitions, SaaS/hosted contracts, special districts and occupation/industry levies can require separate review. Existing income and new corporate/payroll owners are `ne-income-tax`, `ne-corporate-tax` and `ne-payroll`.

## Ask the client first

1. Physical presence, business/permit details, previous/current-year Nebraska retail receipts and separate transaction counts?
2. Marketplace versus direct sales and proof the facilitator collected/remitted each covered sale?
3. Delivery/service-use street address, sale date, city/county and Good Life District/electing-retailer facts?
4. Product/service/software contract, license/transfer rights, training/support, discounts/freight and exemption certificates?
5. Untaxed own-use purchases/inventory withdrawals, tax paid elsewhere, assigned filing period, prior returns and portal notices?

## The method, step by step

1. **Establish registration.** Physical-presence/other engaged-in-business rules are separate from remote thresholds. A remote retailer has nexus if Nebraska retail sales exceed **$100,000** or reach **200 or more separate retail transactions** in the previous or current calendar year. Marketplace facilitators use sales made or facilitated; seller counts include marketplace activity as applicable. Obtain the permit and reconcile direct-sale obligations even when a platform collects tax. [77-2701.13(1)-(3)](https://nebraskalegislature.gov/laws/statutes.php?statute=77-2701.13); [DOR remote/facilitator FAQ](https://revenue.nebraska.gov/about/frequently-asked-questions/remote-seller-and-marketplace-facilitator-faqs).
2. **Classify the sale.** General tangible property and clothing are taxable absent a specific exemption. Ordinary food/food ingredients are exempt, but prepared food and vending-machine food are exceptions; test definitions. Human prescription drugs require the qualifying prescription; over-the-counter drugs remain taxable even if prescribed, while insulin for human use is exempt with or without a prescription. Manufacturing equipment requires a qualifying manufacturer, eligible machinery/use and proper Form 13 evidence; mixed use must be more than 50% manufacturing, and Option 2/3 contractors have separate tax rules. Resale requires actual resale before use and a valid certificate. Do not turn a manufacturer's name into an exemption. [DOR exemption chart](https://revenue.nebraska.gov/about/information-guides/nebraska-sales-tax-exemptions); [Reg 1-013/1-050/1-087/1-107](https://revenue.nebraska.gov/about/chapter-1-sales-and-use-tax).
3. **Resolve software/digital/services by contract.** Furnishing computer software is taxable regardless of conveyance, including canned/custom software and consultant work transferring code. Generalized advice without software/modifications is exempt. Seller-provided software training and mandatory support are taxable; separately stated optional telephone support is not. The old blanket statement that all SaaS is taxable is not verified for every hosted-access arrangement: stop where the contract does not transfer/license software and obtain the applicable official classification. Digital media likewise needs its specific product/right-of-use rule; do not treat all digital receipts as one taxable class. Professional services can be nontaxable while listed services and taxable components remain taxable. [Reg 1-088](https://revenue.nebraska.gov/about/chapter-1-sales-and-use-tax); [computer consulting FAQ](https://revenue.nebraska.gov/about/frequently-asked-questions/nebraska-sales-and-use-tax-faqs); [services FAQ](https://revenue.nebraska.gov/about/frequently-asked-questions/sales-tax-certain-services-faqs).
4. **Source and select the actual rate.** DOR generally uses delivery location for goods and location of service to the customer for services, with specialized exceptions. Use the date-specific local list and address tool. Local city/county rates can be 0.5%, 1%, 1.5%, 1.75% or 2%. Dakota County's 0.5% applies outside municipalities imposing their own local sales tax; do not stack it on that city's tax. Good Life Avenue One has a special 2.75% state rate only for qualifying transactions physically occurring there by electing retailers, with enumerated vehicle/property exceptions. Other Good Life Districts returned to 5.5% state rate from October 1, 2025. [DOR location/county FAQ](https://revenue.nebraska.gov/about/frequently-asked-questions/nebraska-sales-and-use-tax-faqs); [effective 2026 local/district list](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/salestax/slstax_rates_07-01-2026.pdf); [current Good Life District notice](https://revenue.nebraska.gov/businesses/nebraska-sales-and-use-tax).
5. **Compute and reconcile sales/use tax.** Taxable sales x actual state rate plus taxable sales x applicable local rate, allowing only supported exemptions/adjustments. Retailer-paid freight/delivery is generally taxable when the underlying item is taxable, except the stated direct-mail postage rule. Accrue corresponding use tax on taxable storage/use/consumption without proper sales tax; reconcile any interstate-tax exclusion/credit before finalizing. Licensed retailers report use tax on Form 10; nonretailer business uses Form 2, individuals Form 3 or current 1040N line 59. The generic FAQ's old 1040N line 38 is superseded by the actual 2026 return. [delivery/use-tax FAQ](https://revenue.nebraska.gov/about/frequently-asked-questions/nebraska-sales-and-use-tax-faqs); [2026 Form 1040N line 59](https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n.pdf).

## Rates, bands and thresholds

| 2026 item | Rate/condition | Authority |
| --- | --- | --- |
| Ordinary state sales/use | 5.5% | [current DOR FAQ](https://revenue.nebraska.gov/about/frequently-asked-questions/nebraska-sales-and-use-tax-faqs) |
| Local taxes | Actual address/date; city/county authorized rates 0.5%, 1%, 1.5%, 1.75%, 2% | [rate/location FAQ](https://revenue.nebraska.gov/about/frequently-asked-questions/nebraska-sales-and-use-tax-faqs) |
| Dakota County | 0.5% outside a city with its own local tax; not automatic city+county stacking | [county FAQ](https://revenue.nebraska.gov/about/frequently-asked-questions/nebraska-sales-and-use-tax-faqs) |
| Avenue One electing retailer | 2.75% state on qualifying physical district transactions, plus applicable local; special exclusions | [Good Life District notice](https://revenue.nebraska.gov/businesses/nebraska-sales-and-use-tax) |
| Other Good Life Districts | Ordinary 5.5% state from October 1, 2025 | [Good Life District notice](https://revenue.nebraska.gov/businesses/nebraska-sales-and-use-tax) |
| Remote/facilitator threshold | More than $100,000 retail sales OR 200+transactions, prior/current calendar year | [77-2701.13](https://nebraskalegislature.gov/laws/statutes.php?statute=77-2701.13) |

## Boundary table

| Fact | Treatment or stopping point |
| --- | --- |
| Hosted software / SaaS | Contract/license/control facts unresolved: do not apply the old blanket taxable assertion; no exemption is invented either. |
| Manufacturing / groceries / prescriptions / resale | Eligibility and records determine exemption; use the listed regulation and actual certificate. |
| Special districts, vehicles, lodging or occupation levies | Match actual address/date and transaction-specific tax base; the old approximate 7.5% combined rate is not a universal ceiling or quote. |
| SST membership | DOR supplies a Streamlined registration route; the exact legacy full-member status is not independently confirmed by the permitted state sources read here. |

## Worked cases

### Ordinary taxable delivery with verified 1.5% local tax

For a $1,000 taxable delivery to an ordinary 5.5% state/1.5% local destination confirmed for the sale date, state tax is $55 and local tax $15, total $70. This is an assumed verified address, not a statewide rate.

```oa-check
name: NE ordinary state and local sales tax 2026
inputs:
  sale: 1000
  local_rate: 0.015
steps:
  - state: sale * 0.055
  - local: sale * local_rate
  - tax: state + local
expected:
  state: 55
  local: 15
  tax: 70
```

### Dakota County delivery outside a city imposing local tax

A $2,000 taxable purchase delivered to a Dakota County location where the county 0.5% applies and no city tax applies gives $110 state plus $10 county, total $120. Do not add an unrelated city tax. Confirm address/date and any special district before using the case.

```oa-check
name: NE Dakota County no city stacking 2026
inputs:
  sale: 2000
steps:
  - state: sale * 0.055
  - county: sale * 0.005
  - tax: state + county
expected:
  state: 110
  county: 10
  tax: 120
```

## When to refuse or refer

Refer unclear SaaS/digital rights, bundled services, special-district/vehicle sourcing, disputed nexus, industry exemptions, occupation levies and interstate credits. Do not use a guessed maximum or blanket software exemption/taxability. Compute only after the actual product/address/date is established.

## Filing and payment

File Form 10 through DOR's approved electronic route, including zero returns until the account is properly closed. DOR assigns frequency: generally annual below $900 yearly liability, quarterly from $900 to below $3,000, monthly at least $3,000, with SST/seasonal exceptions. Returns/payment are due the 20th following the reporting period; weekends/approved holidays move to the next business day. [Reg 1-010](https://revenue.nebraska.gov/about/chapter-1-sales-and-use-tax); [returns FAQ](https://revenue.nebraska.gov/about/frequently-asked-questions/nebraska-sales-and-use-tax-faqs).

## Completion checklist

Document nexus and marketplace treatment; validate classification/certificates; resolve SaaS/digital contract gaps; match address/date/local/district rate; reconcile sales, use and tax already paid; file/pay assigned returns and retain confirmations.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| DOR sales/use FAQ; read for rates, delivery/service sourcing, Dakota nonstacking, software/support, use-tax routing and filing; obsolete 1040N line checked against 2026 form. | https://revenue.nebraska.gov/about/frequently-asked-questions/nebraska-sales-and-use-tax-faqs | 2026-11-13 |
| July 1-December 31, 2026 local list; read for current city/county rates and district notes. | https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/salestax/slstax_rates_07-01-2026.pdf | 2026-11-13 |
| DOR sales/use page, current notices; read for Good Life District change and Avenue One exceptions, neighboring superseded notices distinguished. | https://revenue.nebraska.gov/businesses/nebraska-sales-and-use-tax | 2026-11-13 |
| 77-2701.13; read for physical/other business categories and full remote/facilitator threshold clauses. | https://nebraskalegislature.gov/laws/statutes.php?statute=77-2701.13 | 2026-11-13 |
| DOR remote/facilitator FAQ; read for thresholds, marketplace and direct-seller reporting distinctions. | https://revenue.nebraska.gov/about/frequently-asked-questions/remote-seller-and-marketplace-facilitator-faqs | 2026-11-13 |
| DOR sales/use regulations; read for Reg 1-010 filing, 1-013 resale, 1-050 prescription, 1-087 food, 1-088 software and 1-107 MME conditions. | https://revenue.nebraska.gov/about/chapter-1-sales-and-use-tax | 2026-11-13 |
| DOR current exemption chart; read for food/prescription/manufacturing/resale categories and documentation. | https://revenue.nebraska.gov/about/information-guides/nebraska-sales-tax-exemptions | 2026-11-13 |
| DOR services FAQ; read for software training and listed-service distinction. | https://revenue.nebraska.gov/about/frequently-asked-questions/sales-tax-certain-services-faqs | 2026-11-13 |
| Final 2026 Form 1040N; read for current individual use-tax line 59. | https://revenue.nebraska.gov/sites/default/files/doc/tax-forms/2026/f_1040n.pdf | 2026-11-13 |

Not yet confirmed: transaction-specific SaaS/hosted access and digital-media rights classification; special sourcing/interstate credits, exact SST full-member status and non-sales occupation/industry levies. Actual address/date and exemptions must be resolved; no universal 7.5% ceiling is assumed.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ne-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ne-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
