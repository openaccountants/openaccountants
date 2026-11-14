---
name: me-sales-tax
description: "Maine 2026 sales/use computation: 5.5% general, food/lodging/rental special rates, remote/marketplace nexus, conditional software treatment and filing. Load us-sales-tax first."
version: "2.2"
jurisdiction: US-ME
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
category: state-tax
type: computation
---

# Maine sales and use tax, 2026

> **Built from the law. Not yet approved.** Written by Codex; this version has not been reviewed by an accountant. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

**Answer first:** Maine's general retail rate is 5.5%; prepared food is 8%, lodging 9% and qualifying automobile rentals under one year 10%. Software treatment depends on delivery, server location and download rights. [36 M.R.S.1811(1)(D)](https://legislature.maine.gov/statutes/36/title36sec1811.html); [Rule 326(9)](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/125c326-2025-188%20%28NEW%29_accessibility%20update.pdf).

## Scope

Ordinary Maine retail sales and purchases, remote sellers and marketplace facilitators. Load `us-sales-tax` first for the federal/multistate framework. This skill owns Maine state tax; specialized leases, product definitions and unverified local levies remain partial. No SST membership claim is carried forward without a current primary source.

## Ask the client first

1. Seller location, Maine workers/inventory/other presence, registration and prior/current-year gross Maine-delivered sales?
2. Marketplace own/facilitated sales, collection statements, direct sales and exemption certificates?
3. Product/service description, delivery/use location, price, discounts, freight and returns?
4. For software: prewritten/custom terms, download rights, server location, license/user locations and maintenance/update charges?
5. Own-use purchases/inventory withdrawals, tax already paid, filing-period assignment and portal notices?

## The method, step by step

1. **Establish registration.** Physical-presence sellers and other section 1754-B categories must register as applicable. For remote sellers, gross sales of tangible property, electronically transferred products or taxable services delivered into Maine exceeding **$100,000 in the previous or current calendar year** trigger registration. The facilitator test counts its own plus facilitated sales. No transaction-count test remains. Retain marketplace proof and separate direct-sale obligations. [1754-B(1-B)(B),(K)](https://legislature.maine.gov/statutes/36/title36sec1754-B.html).
2. **Classify before selecting a rate.** Separate grocery staples from prepared food, lodging from other rentals, and an automobile rental under one year from other leases. General tangible property, including clothing, is taxable unless an identified exemption applies. Grocery staples and human medicines on a doctor's prescription are exempt, with the cannabis exception. Production machinery requires direct-and-primary qualifying use, not merely purchase by a manufacturer. Resale treatment needs a valid certificate and supporting purpose. [1811](https://legislature.maine.gov/statutes/36/title36sec1811.html); [1760(3),(5),(31)](https://legislature.maine.gov/statutes/36/title36sec1760.html); [MRS resale/registration FAQ](https://www.maine.gov/revenue/faq/sales-use-service-provider-tax).
3. **Resolve software and services.** Electronically downloaded prewritten software is taxable. Remote access to software on an **out-of-state server with no download rights** is not a taxable retail sale under Rule 326; access to software hosted in Maine is taxable. Upgrades and maintenance that supply updates can be taxable; segregate service-only charges and document use/location. The old blanket SaaS exemption was wrong. Professional services are not automatically taxable merely because they are services, but taxable telecommunications, fabrication, digital audio/video and other listed services must be identified; do not exempt a mixed contract by its professional label. [Rule 326(9),(10)](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/125c326-2025-188%20%28NEW%29_accessibility%20update.pdf); [MRS taxable-service list](https://www.maine.gov/revenue/faq/sales-use-service-provider-tax).
4. **Source and compute.** Use actual Maine delivery/use evidence. Out-of-state delivery and software use require records and the applicable sourcing rule; a customer's billing address alone does not settle every transaction. Tax = taxable sale price x applicable state rate; separate each class and reconcile marketplace tax, exemptions and returns. Do not add a guessed local rate. A current primary-source blanket statement of no local sales tax was not confirmed. [1811](https://legislature.maine.gov/statutes/36/title36sec1811.html); [Rule 326(10)](https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/125c326-2025-188%20%28NEW%29_accessibility%20update.pdf).
5. **Accrue use tax and file.** Maine use tax applies at the corresponding sales rate when taxable property/services are used or consumed in Maine without proper tax payment, including inventory withdrawn for own use. Reconcile purchase tax and any legally available credit before determining a net amount; interstate-credit detail requires review. File/pay through the Maine Tax Portal and retain confirmation. [1861](https://legislature.maine.gov/statutes/36/title36sec1861.html); [use-tax and filing FAQ](https://www.maine.gov/revenue/faq/sales-use-service-provider-tax).

## Rates, bands and thresholds

| 2026 transaction | State rate or rule | Authority |
| --- | --- | --- |
| General taxable retail property/services | 5.5% | [1811(1)(D)](https://legislature.maine.gov/statutes/36/title36sec1811.html) |
| Prepared food / qualifying on-premises liquor | 8% | [1811(1)(D)(1),(2)](https://legislature.maine.gov/statutes/36/title36sec1811.html) |
| Hotel/rooming-house/tourist or trailer-camp living quarters | 9% | [1811(1)(D)(3)](https://legislature.maine.gov/statutes/36/title36sec1811.html) |
| Automobile / qualifying non-warranty loaner rental for less than one year | 10% | [1811(1)(D)(4)](https://legislature.maine.gov/statutes/36/title36sec1811.html) |
| Covered adult-use/nonpatient cannabis from January 1, 2026 | **14%**, replacing 10% | [1811(1)(D)(5)](https://legislature.maine.gov/statutes/36/title36sec1811.html) |
| Remote seller / facilitator nexus | More than $100,000 previous/current-year qualifying Maine deliveries | [1754-B](https://legislature.maine.gov/statutes/36/title36sec1754-B.html) |

The special rates and neighboring cannabis effective date were read in [current 1811](https://legislature.maine.gov/statutes/36/title36sec1811.html); nexus conditions in [1754-B](https://legislature.maine.gov/statutes/36/title36sec1754-B.html). The rental rule is not a general 10% rate for every vehicle or every lease term.

## Worked cases

### Prepared food at 8%

A $100 taxable prepared-food sale produces $8 state tax. Keep it out of the 5.5% general bucket.

```oa-check
name: Prepared food at 8%
inputs:
  sale: 100
steps:
  - tax: sale * 0.08
expected:
  tax: 8
```

### Short-term auto rental at 10%

A $300 qualifying automobile rental for less than one year produces $30 state tax. The vehicle and rental term must satisfy section 1811; the rate is not inferred from the word rental alone.

```oa-check
name: Short-term auto rental at 10%
inputs:
  rental: 300
steps:
  - tax: rental * 0.10
expected:
  tax: 30
```

## When to refuse or refer

Refer uncertain prepared-food/lodging definitions, mixed digital contracts, leases outside the stated automobile rule, cross-border credits, special industry exemptions, disputed nexus and unverified municipal assessments. Do not apply blanket SaaS, manufacturing or professional-service exemptions. Confirm every material classification before issuing an amount.

## Filing and payment

MRS assigns frequency. Its current FAQ generally specifies monthly for average liability at least $600/month, quarterly for $100 to below $600/month, semiannual below $100/month but over $50/year, and annual below $50/year. The FAQ does not resolve the exact $50/year boundary; use the actual assignment and Rule 304 rather than inventing one. Returns are due the 15th after the period, moving to the next nonweekend/non-State-holiday day. Electronic filing is the ordinary route; paper requires waiver. [filing FAQ](https://www.maine.gov/revenue/faq/sales-use-service-provider-tax).

## Completion checklist

Document nexus and marketplace collections; classify each sale and exemption; retain software/server evidence; compute special rates separately; reconcile own-use purchases and assigned filing period; file/pay and retain confirmations. Flag unknown local/sourcing facts explicitly.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| 36 M.R.S.1811; read for all current rates, rental boundary and 2026 cannabis change, neighboring historical periods. | https://legislature.maine.gov/statutes/36/title36sec1811.html | 2026-11-13 |
| 36 M.R.S.1754-B; read for seller/facilitator registration conditions and gross-sales threshold. | https://legislature.maine.gov/statutes/36/title36sec1754-B.html | 2026-11-13 |
| MRS Rule 326, effective October 6, 2025; read for software delivery/server/download distinction, maintenance and sourcing. | https://www.maine.gov/revenue/sites/maine.gov.revenue/files/inline-files/125c326-2025-188%20%28NEW%29_accessibility%20update.pdf | 2026-11-13 |
| 36 M.R.S.1760; read for grocery, prescription/cannabis exception and direct-primary machinery conditions. | https://legislature.maine.gov/statutes/36/title36sec1760.html | 2026-11-13 |
| 36 M.R.S.1861; read for corresponding-rate use tax and inventory withdrawal. | https://legislature.maine.gov/statutes/36/title36sec1861.html | 2026-11-13 |
| MRS sales/use FAQ; read for current taxable-service list, resale certification, filing assignment and due date. | https://www.maine.gov/revenue/faq/sales-use-service-provider-tax | 2026-11-13 |

Not yet confirmed: blanket absence of local sales levies and SST membership; transaction-specific sourcing/interstate-credit detail; special leases/product definitions; exact $50/year filing-frequency boundary. Rule 326 is a current rule effective in 2025, not an extrapolated 2026 SaaS assumption.
