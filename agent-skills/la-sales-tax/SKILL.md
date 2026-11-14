---
name: la-sales-tax
description: "Louisiana 2026 sales/use tax: 5% state rate, local sourcing, remote seller nexus, taxable software access, exemptions, registration, filing and computation. Load us-sales-tax first."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/la-sales-tax"
  jurisdiction: "US-LA"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Louisiana sales and use tax, 2026

> **Built from the law. Not yet approved.** Written by Codex; this version has not been reviewed by an accountant. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

**Answer first:** Louisiana's general state rate is 5%, with local tax determined for the actual address and date. Prewritten software access, including subscriptions commonly called SaaS, is taxable unless a specific exception applies. The old 4.45% and blanket SaaS exemption are superseded. [LDR sales/use page](https://revenue.louisiana.gov/businesses/general-sales-and-use-taxes/general-sales-use-tax); [R.S.47:301.3(9)](https://www.legis.la.gov/Legis/Law.aspx?d=1392324).

## Scope

Ordinary Louisiana retail sales and taxable purchases, physical-presence dealers, remote sellers and marketplace transactions. This skill owns the state sales/use job and identifies local sourcing/filing gates; it does not publish every parish rate or special excise/vehicle/hotel regime. Load `us-sales-tax` for the federal owner context, then apply Louisiana law here.

## Ask the client first

1. Selling entity, Louisiana premises/workers/agents/inventory and first business date; existing LDR, local and remote-commission accounts?
2. Prior/current calendar-year Louisiana delivered sales, retail versus resale and direct versus marketplace-facilitated sales?
3. Contracts/invoices for goods, digital products, software access, information or other services; exemptions and valid purchaser certificates?
4. Where did the buyer receive/use the product, and where are software users located; transaction dates, returns and discounts?
5. Assigned reporting frequency, local collector/rates for each address, tax already collected, taxable purchases without tax and payment history?

## The method, step by step

1. **Establish liability before using a threshold.** Physical presence/business activity is a separate dealer route; the remote-seller dollar test is no safe harbor for a local dealer. Current R.S.47:301(4)(k) uses gross revenue **exceeding $100,000** from delivered goods, digital products or services during the previous/current calendar year. It no longer has a 200-transaction test. Determine the statutory count from actual sales and document uncertain exclusions. [R.S.47:301(4)](https://legis.la.gov/Legis/Law.aspx?d=101815&p=y). Marketplace facilitators have their separate retail-sales threshold, collection and record duties in [R.S.47:340.1](https://www.legis.la.gov/legis/Law.aspx?d=1186690); retain their collection reports and reconcile direct sales separately.
2. **Classify each sale.** General tangible goods/clothing, digital products and listed services are taxable unless excluded or exempt. Prewritten downloaded software and access to seller-hosted prewritten software require software classification; hosting possession does not itself exempt access. Information services also have an express category, with exceptions including qualifying proprietary single-client information and data processing. A professional-service label alone does not settle a mixed contract. [R.S.47:301.3](https://www.legis.la.gov/Legis/Law.aspx?d=1392324); [R.S.47:301 definitions](https://legis.la.gov/Legis/Law.aspx?d=101815&p=y).
3. **Test exemptions against documents.** Food for home preparation/consumption is generally state-exempt; prepared meals generally taxable; local food tax may remain. Prescription drugs and qualifying manufacturing machinery/equipment have specific exemptions, not blanket exemptions for every medical or factory purchase. Valid resale transactions are excluded, subject to certificate rules. [LDR food FAQ](https://www.revenue.la.gov/tax-education-and-faqs/faqs/fairs-festivals-and-other-special-events/is-there-sales-tax-on-food/); [R-1002 current-period exemption table](https://dam.ldr.la.gov/publications/1002-8-25.pdf); [R.S.47:301(10)](https://legis.la.gov/Legis/Law.aspx?d=101815&p=y). For software/digital products, R.S.47:305.12(A) requires all three: exclusive commercial use, direct production of goods/services sold to customers, and taxable sales/use or insurance-premium outputs. Ordinary administrative software does not qualify merely because a business buys it. Separate self-created, financial and health-provider exemptions have their own facts. [R.S.47:305.12](https://www.legis.la.gov/legis/Law.aspx?d=101877).
4. **Source and determine both tax bases.** Follow the statutory hierarchy: receipt at seller premises, otherwise known delivery/receipt location, then prescribed address fallbacks. Specific services and multi-location software use have special sourcing rules; preserve location/user records. Do not assign all tax to a head-office parish merely because it pays the invoice. [R.S.47:301.4](https://www.legis.la.gov/legis/Law.aspx?d=1392328). Get the actual applicable local collector, base and rate; the historical 0%-7% local range and approximate 11.45% maximum are unconfirmed and must not price a sale.
5. **Compute and reconcile.** State tax = state-taxable sales price x 0.05; local tax uses its separately verified base and rate. Add use tax on taxable Louisiana use/purchases without proper tax collection, with any legally allowed prior-tax credit verified. Match invoices, exempt sales, marketplace collection, purchases, returns, deposits and return totals. Use-tax liability can exist without seller collection. [LDR general sales/use page](https://revenue.louisiana.gov/businesses/general-sales-and-use-taxes/general-sales-use-tax); [R.S.47:301(18)-(19)](https://legis.la.gov/Legis/Law.aspx?d=101815&p=y).

### Rates, bands and thresholds

| 2026 rule | Value | Authority |
| --- | --- | --- |
| General state sales/use rate | 5% | [LDR sales/use page](https://revenue.louisiana.gov/businesses/general-sales-and-use-taxes/general-sales-use-tax) |
| Remote-seller dealer threshold, no physical presence | Gross delivered revenue exceeds $100,000 in previous/current calendar year; no transaction-count alternative | [R.S.47:301(4)(k)](https://legis.la.gov/Legis/Law.aspx?d=101815&p=y) |
| Marketplace facilitator threshold | Louisiana remote retail-sale revenue exceeds $100,000 in previous/current calendar year | [R.S.47:340.1(C)](https://www.legis.la.gov/legis/Law.aspx?d=1186690) |
| State food for home consumption | Generally exempt; local tax may apply | [LDR food FAQ](https://www.revenue.la.gov/tax-education-and-faqs/faqs/fairs-festivals-and-other-special-events/is-there-sales-tax-on-food/) |
| Local rates | Address/date-specific, not a statewide fixed maximum in this skill | [R.S.47:301.4](https://www.legis.la.gov/legis/Law.aspx?d=1392328); [R.S.47:340.1(E)](https://www.legis.la.gov/legis/Law.aspx?d=1186690) |

## Worked cases

### Office software access compared with documented production use

A customer pays $5,000 for prewritten hosted office-management software used in administration. Assume Louisiana sourcing and no other exemption. State tax is $250; local tax still needs the location rate. If a different $5,000 licence meets every production exemption condition in R.S.47:305.12(A), document those facts and its exempt result. Business status alone does not produce the second result.

```oa-check
name: LA software access exemption boundary
inputs:
  price: 5000
steps:
  - office_state_tax: price * 0.05
  - qualified_production_tax: price * 0
expected:
  office_state_tax: 250
  qualified_production_tax: 0
```

### Groceries and prepared meals use different state bases

An ordinary retailer has $4,000 documented groceries for home consumption and $6,000 taxable prepared meals, with no other exemptions. Gross sales are $10,000; state-taxable sales $6,000 and state tax $300. Do not exclude grocery sales from a parish base without its applicable exemption. Return deductions and local collection still require reconciliation.

```oa-check
name: LA grocery and prepared food split
inputs:
  groceries: 4000
  meals: 6000
steps:
  - gross: groceries + meals
  - state_taxable: gross - groceries
  - state_tax: state_taxable * 0.05
expected:
  gross: 10000
  state_taxable: 6000
  state_tax: 300
```

## When to refuse or refer

Stop a combined-rate quote without the actual local location/date and taxable base. Refer mixed software/information/professional contracts, disputed exemptions, construction, direct-pay arrangements and local assessments. Never infer SaaS exemption, ignore parish obligations or use old maximum-rate marketing claims. Arithmetic is required when the base/rate is established; the legacy prohibition on every computation has no tax-law basis.

## Filing and payment

Register the applicable LDR and local accounts before taxable dealer activity; a qualifying no-physical-presence remote seller/facilitator uses the Louisiana Sales and Use Tax Commission for Remote Sellers channel, which administers state/local remote collections. Physical-presence dealer registrations and local collector returns require separate attention. [LDR sales/use page](https://revenue.louisiana.gov/businesses/general-sales-and-use-taxes/general-sales-use-tax); [R.S.47:340.1](https://www.legis.la.gov/legis/Law.aspx?d=1186690).

LDR states sales returns and payment are due by the twentieth following the assigned month or quarter. Use the assigned account's LaTAP return and current R-1029 instructions, retain acknowledgments, and reconcile local returns separately. Marketplace-facilitator tax is monthly, due by the twentieth following the collection month. [LDR filing rule](https://revenue.louisiana.gov/businesses/general-sales-and-use-taxes/general-sales-use-tax); [R-1029 instructions revised June 2026](https://dam.ldr.la.gov/taxforms/1029i-1-25-revised-06-01-26.pdf); [R.S.47:340.1(E)(3)](https://www.legis.la.gov/legis/Law.aspx?d=1186690). Do not net a prior-period error into current sales without the authorized amendment procedure.

## Completion checklist

Confirm dealer route, classify each transaction, retain exemption evidence and source-location records, verify each local rate/base, reconcile marketplace reports and untaxed purchases, then save the state/local filing and payment acknowledgments.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| LDR general sales/use page; read for taxable categories, rate, dealer and return/payment sections. | https://revenue.louisiana.gov/businesses/general-sales-and-use-taxes/general-sales-use-tax | 2026-11-13 |
| R.S.47:301; read for dealer, retail sale/resale, professional work product, digital sale/use, sales-price and use-tax exemption neighbours. | https://legis.la.gov/Legis/Law.aspx?d=101815&p=y | 2026-11-13 |
| R.S.47:301.3; read for complete service categories and information-service exceptions. | https://www.legis.la.gov/Legis/Law.aspx?d=1392324 | 2026-11-13 |
| R.S.47:301.4; read for complete sourcing hierarchy, special services and local software-user allocation. | https://www.legis.la.gov/legis/Law.aspx?d=1392328 | 2026-11-13 |
| R.S.47:305.12; read for all exemption conditions and separate business/financial/health subsections. | https://www.legis.la.gov/legis/Law.aspx?d=101877 | 2026-11-13 |
| R.S.47:340.1; read for facilitator definitions, retail threshold, application/collection, records and monthly filing. | https://www.legis.la.gov/legis/Law.aspx?d=1186690 | 2026-11-13 |
| LDR food FAQ; read for entire prepared/home-consumption and local caveat. | https://www.revenue.la.gov/tax-education-and-faqs/faqs/fairs-festivals-and-other-special-events/is-there-sales-tax-on-food/ | 2026-11-13 |
| R-1002 August2025; read for 2025-2029 current-period columns for prescription drugs, food and qualifying manufacturing equipment, including repealed neighbouring items. | https://dam.ldr.la.gov/publications/1002-8-25.pdf | 2026-11-13 |
| R-1029 instructions revised June 2026; read for general filing, gross sales/purchases, exemption deductions, remittances and amendments. | https://dam.ldr.la.gov/taxforms/1029i-1-25-revised-06-01-26.pdf | 2026-11-13 |

Not yet confirmed: each actual parish/city/district rate and exemption base; portal-specific remote registration start date and current no-physical-presence threshold counting exclusions; mixed-contract treatment and asset-specific manufacturing exemptions; prior-tax use-credit limitations. The legacy assertion that Louisiana is not an SST member is not reverified here and is not used to establish liability. The old local range/max rate and blanket professional-service/software exemptions are not usable rules.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `la-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/la-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
