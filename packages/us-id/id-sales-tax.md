---
name: id-sales-tax
description: Idaho sales and use tax for retailers and buyers in 2026, including remote sellers, groceries, software delivery, exemptions, taxable price and Form 850 filing. Load us-sales-tax for the federal-system workflow, then apply these Idaho rules.
version: 2.1
jurisdiction: US-ID
category: state-tax
type: situation-rules
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
---

# Idaho sales and use tax v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick reference:** 2026 state sales/use rate 6%; resort-city taxes require a separate location check. Remote-seller threshold and grocery/software exceptions appear below. Built from the law; Not yet approved.

## Who this applies to

Idaho retailers, remote sellers with an Idaho collection obligation, and buyers using taxable goods in Idaho without the correct sales tax. Physical presence can require collection independently of the remote-sales threshold. A marketplace facilitator's own and facilitated sales use separate permits. See the [Commission's online-seller requirements](https://tax.idaho.gov/taxes/sales-use/guides-for-certain-groups/online-sellers/online-guide/).

## Rates, bands and thresholds

| Item | Amount and condition | Official source |
|---|---|---|
| State sales/use tax | 6% on the taxable base, unless exempt | [Commission basics; Code 63-3619 and 63-3621](https://tax.idaho.gov/taxes/sales-use/online-guide/) |
| Remote retailer without physical presence | Collection when Idaho sales exceed $100,000 in the current or previous year | [Online sellers](https://tax.idaho.gov/taxes/sales-use/guides-for-certain-groups/online-sellers/online-guide/) |
| Remote marketplace facilitator | Same $100,000 test, combining own and third-party Idaho sales | [Online sellers](https://tax.idaho.gov/taxes/sales-use/guides-for-certain-groups/online-sellers/online-guide/) |
| Local taxes | Resort cities choose their own taxable categories; no universal combined maximum supplied here | [Commission city-tax page](https://tax.idaho.gov/taxes/sales-use/sales-tax/local-sales-tax/city-sales-tax/) |
| Regular monthly return | Form 850 and payment by the 20th of the following month; next business day if weekend/holiday | [Sales tax filing](https://tax.idaho.gov/taxes/sales-use/stfiling/) |
| Quarterly filing | Tax below $750 per quarter; due 20 days after quarter-end, subject to the account's assigned cycle | [Sales tax filing](https://tax.idaho.gov/taxes/sales-use/stfiling/) |

## The base

Apply the [Commission's transaction classifications](https://tax.idaho.gov/taxes/sales-use/guides-for-certain-groups/retailers/collecting/): tangible goods, including ordinary clothing, meals and prepared food are taxable. Fabrication labor is taxable too. Downloaded software and load-and-leave software without retained media are nontaxable; permanent-use digital books, music, video and games are a distinct taxable category. The page exempts **some** remotely accessed software: inspect the contract and delivery rather than assuming every SaaS bundle is exempt.

| Exception | Condition | Official source |
|---|---|---|
| Grocery food | Ordinary retail food is taxable. Food-stamp/EBT and WIC purchases have an exception | [Grocers: taxable and nontaxable sales](https://tax.idaho.gov/taxes/sales-use/guides-for-certain-groups/food/grocers/sales/) |
| Prescription drugs | Prescription sales and refills are exempt | [Grocers](https://tax.idaho.gov/taxes/sales-use/guides-for-certain-groups/food/grocers/sales/) |
| Resale | Obtain and retain a completed, signed and dated ST-101 for qualifying resale | [Collecting tax](https://tax.idaho.gov/taxes/sales-use/guides-for-certain-groups/retailers/collecting/) |
| Production equipment | Directly used and necessary equipment used more than 50% in producing tangible goods for sale; obtain the applicable exemption certificate | [Collecting tax](https://tax.idaho.gov/taxes/sales-use/guides-for-certain-groups/retailers/collecting/) |

Compute state tax on taxable consideration. Separately stated outbound delivery and installation/repair labor are excluded; parts and fabrication charges remain taxable. Trade-in allowances require the correct transaction treatment. Use tax addresses untaxed or undertaxed goods used or stored in Idaho, including business purchases. These are [Commission basics](https://tax.idaho.gov/taxes/sales-use/online-guide/), not permission to exempt all service bundles.

## Deadlines and filing

Register for the correct seller's permit before collecting. In [TAP](https://tap.tax.idaho.gov/), select the sales/use account and correct return period, complete Form 850's sales and taxable-purchase fields, reconcile tax, submit and pay, and retain confirmation and payment records. Use the [Commission's filing instructions](https://tax.idaho.gov/taxes/sales-use/stfiling/): report on the accrual sale period, file zero returns while registered, and omit sales already reported by a registered marketplace facilitator. Keep those sales separately reconciled. Approved semiannual/annual cycles have their own assigned periods; do not choose one unilaterally.

## Penalties and interest

A filing or payment failure can create additional charges. Numeric penalty schedules and the applicable annual interest rate were not established in this pass; obtain the Commission's current computation before calculating arrears.

## Cross-border points

Identify physical presence, shipment destination, facilitator reporting and any tax paid elsewhere separately. Do not substitute an SST membership label for Idaho's own nexus and transaction rules. Resort-city taxes, including McCall and Sun Valley, depend on location and taxable category; the [state's directory](https://tax.idaho.gov/taxes/sales-use/sales-tax/local-sales-tax/city-sales-tax/) confirms that cities administer different bases.

## Two worked examples that recompute

**Ordinary grocery sale.** Invented taxable cash grocery sale of $100, with no benefits exception and no local tax: state tax is $6. This corrects the old blanket grocery exemption; the [grocer page](https://tax.idaho.gov/taxes/sales-use/guides-for-certain-groups/food/grocers/sales/) controls.

```oa-check
name: Idaho ordinary grocery sale in 2026
inputs:
  taxable_food: 100
steps:
  state_tax: taxable_food * 0.06
expected:
  state_tax: 6
```

**Delivery charge boundary.** Invented taxable goods of $1,000 with $50 separately stated outbound delivery. Tax is $60 when excluded correctly, compared with $63 if the delivery is incorrectly included. The invoice distinction, rather than a seller's preference, decides the base under the [Commission basics](https://tax.idaho.gov/taxes/sales-use/online-guide/).

```oa-check
name: Idaho separately stated outbound delivery
inputs:
  goods: 1000
  delivery: 50
steps:
  correct_tax: goods * 0.06
  incorrect_tax: (goods + delivery) * 0.06
  overcharge: incorrect_tax - correct_tax
expected:
  correct_tax: 60
  incorrect_tax: 63
  overcharge: 3
```

## Ask the client first

- What goods, services, software rights and delivery methods are on the invoice?
- Where are the seller, buyer, inventory, staff and delivery location?
- What are current/prior-year Idaho direct and marketplace sales?
- Which exemptions, benefit payments and signed certificates support untaxed sales?
- What permit, assigned filing cycle, unpaid periods and prior tax payments exist?

## Sources

| Source | URL | Read for | Read on |
|---|---|---|---|
| Commission sales/use basics; Code 63-3619/63-3621 | https://tax.idaho.gov/taxes/sales-use/online-guide/ | Read for state rate, taxable price, delivery, fabrication, digital products and use tax | 2026-11-13 |
| Commission online sellers | https://tax.idaho.gov/taxes/sales-use/guides-for-certain-groups/online-sellers/online-guide/ | Read for physical-presence boundary, remote thresholds, facilitator aggregation and separate permits | 2026-11-13 |
| Commission collecting tax; Sales Tax Rule 027 classification | https://tax.idaho.gov/taxes/sales-use/guides-for-certain-groups/retailers/collecting/ | Read for goods, software delivery, production-use condition and ST-101 | 2026-11-13 |
| Commission grocers | https://tax.idaho.gov/taxes/sales-use/guides-for-certain-groups/food/grocers/sales/ | Read for food, benefit purchases, prescription drugs and resale exceptions | 2026-11-13 |
| Commission filing | https://tax.idaho.gov/taxes/sales-use/stfiling/ | Read for regular due dates, accrual reporting, zero returns and facilitator exclusions | 2026-11-13 |
| Commission city taxes | https://tax.idaho.gov/taxes/sales-use/sales-tax/local-sales-tax/city-sales-tax/ | Read for local administration, differing taxable bases and city directory | 2026-11-13 |

Not yet confirmed: current city-specific rates and combined maximum (the old up-to-3%/~9% assertions are withdrawn); general service-bundle and SaaS-contract classification beyond the stated software-delivery distinction; the old SST membership and blanket destination-sourcing assertions; current penalty and interest schedules. The current administrative-rule PDF timed out; no unread rule text is treated as confirmed.
