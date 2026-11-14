---
name: ia-sales-tax
description: "Compute Iowa state sales tax, local option sales tax and use tax for 2026. Covers physical and economic nexus, ordinary taxable retail sales, digital and manufacturing exemptions, permit registration and filing frequency. Load us-sales-tax first for the federal-system workflow. Trigger on Iowa sales tax, use tax, SaaS or LOST."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ia-sales-tax"
  jurisdiction: "US-IA"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Iowa sales and use tax, tax year 2026

> **Built from the law. Not yet approved.** Written by Codex. Not reviewed by an accountant. General reference for AI-assisted working papers; a qualified professional must review the facts, computations and filings. Circular 230 section 10.37: apply the law to established facts, consider relevant circumstances and do not rely on audit risk or assume facts that have not been supplied.

**Answer first.** Iowa state sales and use tax is 6%; a location with local option sales tax adds 1% to taxable sales. There is no local option **use** tax. Software and SaaS require an exemption check, including the commercial-enterprise exemption; they are not invariably taxable. [IDR sales and use tax guidance](https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/sales-use-tax-guide).

## Scope

Iowa retailers, remote sellers, marketplace facilitators and purchasers owing use tax. This skill covers ordinary sales/use tax, not specialized lodging, vehicle, rental-car or excise-tax computations. Load `us-sales-tax` for the common workflow; Iowa rates and exceptions stay here.

## Ask the client first

1. Physical presence and gross Iowa sales in this and the preceding calendar year, including marketplace sales.
2. What was sold, delivery/first-use address, sale date and separately stated charges.
3. Buyer type, resale or exemption certificates, commercial use and manufacturing use.
4. Whether a marketplace already collected the tax and which transactions remain the seller's responsibility.
5. Untaxed purchases, other-state tax paid, existing permit and assigned filing frequency.

## The method, step by step

### Rates, bands and thresholds

| Item and condition | Amount, 2026 | Official source |
| --- | --- | --- |
| State sales and use tax, ordinary taxable base | 6% | [IDR sales/use guidance](https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/sales-use-tax-guide) |
| Local option sales tax (LOST) where adopted | Additional 1%; ordinary combined rate 7% in such a jurisdiction; no local option use tax | [IDR sales/use guidance](https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/sales-use-tax-guide) |
| Remote seller economic nexus | At least USD 100,000 gross Iowa sales in current or immediately preceding calendar year; physical presence is a separate trigger | [IDR permit/nexus guidance](https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/permits-filing-requirements-local-option-sales-tax-lost) |
| Marketplace facilitator nexus | At least USD 100,000 sales made or facilitated into Iowa | [IDR permit/nexus guidance](https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/permits-filing-requirements-local-option-sales-tax-lost) |
| Regular use-tax purchaser permit screen | USD 1,200 or more annual use tax; smaller/nonregular purchasers may use the non-permit return | [IDR use-tax guidance](https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/sales-use-tax-guide) |
| Annual sales/use filer | Less than USD 1,200 annual sales/use tax; due January 31 following the year | [IDR filing frequencies](https://revenue.iowa.gov/taxes/file-my-taxes/business-taxes/filing-frequency-return-due-dates) |
| Monthly sales/use filer | USD 1,200 or more annual tax; return and payment due last day of following month | [IDR filing frequencies](https://revenue.iowa.gov/taxes/file-my-taxes/business-taxes/filing-frequency-return-due-dates) |
| Seasonal filer | At least USD 1,200 tax in four or fewer months per year; approved seasonal registration, monthly due date | [IDR filing frequencies](https://revenue.iowa.gov/taxes/file-my-taxes/business-taxes/filing-frequency-return-due-dates) |

### Apply the right base and exception

1. Establish physical or economic nexus before applying the remote-sales threshold. Register the sales/use permit through GovConnectIowa. Physical sellers cannot use the remote-sales threshold as an exemption. Check marketplace collection and avoid collecting twice.
2. Source tangible goods and specified digital products to Iowa delivery and taxable services to Iowa first use under [IDR guidance](https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/sales-use-tax-guide); identify the actual local jurisdiction instead of assuming the entire county adopts LOST.
3. Under [423.2 and 423.3](https://www.legis.iowa.gov/docs/code/2026/423.3.pdf), ordinary tangible personal property and clothing are generally taxable; qualifying food/food ingredients are exempt, while prepared food is taxable. Prescription drugs require the statutory dispensing/prescription conditions. Resale needs a valid exemption certificate and actual resale use.
4. Prewritten software, custom software, specified digital products and SaaS can be taxable; a qualifying commercial enterprise's exclusive business-use purchases of specified digital products, prewritten software and enumerated related services can be exempt under 423.3(104). More than de minimis noncommercial use defeats that exception. Other nonprofits do not automatically qualify as commercial enterprises; insurance companies and financial institutions have special inclusion. [IDR digital-product guidance](https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/taxation-specified-digital-products-software-and-related-services).
5. A professional-service label alone does not establish exemption: check whether the actual service is enumerated as taxable. For manufacturing equipment, establish manufacturer status and directly/primarily qualifying processing or another listed statutory use; merely calling equipment industrial is insufficient. See [IDR manufacturing guidance](https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/iowa-sales-and-use-tax-manufacturing-and-processing).
6. Compute state tax on the taxable sales price, then LOST only where due. Review refunds, taxable delivery/bundling and exemption documentation before reporting. If sales tax was not collected on a taxable Iowa-use purchase, accrue state use tax; valid tax paid to another state may reduce the Iowa state-tax balance, supported by delivery/payment evidence. No local option use tax is added.

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Local jurisdiction has no LOST | State tax only; location must be checked |
| Vendor did not collect Iowa tax | Buyer examines use tax; lack of seller nexus does not exempt the buyer |
| Exempt SaaS/digital business use | Retain qualifying commercial-enterprise and exclusive-use evidence |
| Groceries versus prepared food | Determine product classification; do not apply a blanket grocery exemption |
| Manufacturing/resale | Retain completed exemption certificate and qualifying-use evidence |

## Worked cases

**Case 1.** An invented retailer makes USD 10,000 taxable clothing sales delivered to a jurisdiction confirmed to levy LOST. State tax is USD 600, local tax USD 100 and total USD 700. If delivery is instead to a jurisdiction without LOST, total is USD 600. The location determines the difference.

```oa-check
name: Iowa sales tax with and without local option
inputs:
  taxable_sales: 10000
steps:
  - state: taxable_sales * 0.06
  - local: taxable_sales * 0.01
  - with_local: state + local
  - without_local: state
expected:
  state: 600
  local: 100
  with_local: 700
  without_local: 600
```

**Case 2, decision.** An invented Iowa purchaser buys USD 5,000 taxable office furniture for Iowa use from a seller with no collection duty. No tax was charged: buyer use tax is USD 300. If instead a valid USD 200 other-state sales tax was paid and the credit conditions are established, Iowa state use tax falls to USD 100. Do not add LOST to either use-tax computation. A vendor invoice with no tax therefore triggers a purchaser accrual review, not a zero-tax conclusion.

```oa-check
name: Iowa purchaser use-tax and other-state credit decision
inputs:
  purchase: 5000
  eligible_other_state_tax: 200
steps:
  - no_prior_tax: purchase * 0.06
  - credit: min(eligible_other_state_tax, no_prior_tax)
  - residual: max(no_prior_tax - credit, 0)
expected:
  no_prior_tax: 300
  credit: 200
  residual: 100
```

## When to refuse or refer

Refer unusual software bundles, mixed-use digital products, uncertain manufacturing exemptions, refund limitation periods and special excise regimes. Do not repeat the old prohibition on computation: compute only after classifying the sale and confirming source jurisdiction and exemption evidence.

## Filing and payment

Use GovConnectIowa, select the permit/period, report total sales, exempt sales, taxable sales and taxable purchases, and complete the local-option schedule when taxable amounts are nonzero, even if no LOST is due. Reconcile state and local amounts to the sales ledger and marketplace reports, submit the return, save confirmation and arrange payment separately by its due date. Monthly and seasonal filers file/pay electronically; follow the assigned frequency until an approved change. Weekend/holiday dates move under Iowa Code 421.9A.

[421.27](https://www.legis.iowa.gov/docs/code/2026/421.27.pdf) can impose separate 5% late-filing and 5% late-payment penalties if less than 90% was paid by the due date, subject to waiver conditions, plus applicable interest. Required electronic sales/use filing and payment can each attract a separate 5% penalty if the required method is not used. Apply the interest rate for the delinquency period from the official notice, not a guessed rate for a tax year.

## Completion checklist

- Nexus, marketplace responsibility and permit established.
- Product, exemption and actual delivery/first-use jurisdiction supported.
- State, LOST and purchaser use tax kept distinct.
- Return frequency, local schedule, payment and confirmation reconciled.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| IDR Sales & Use Tax Guide. Read for 6% state rate, 1% local option, no local use tax, sourcing, purchaser use tax and reporting steps. | https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/sales-use-tax-guide | 2026-11-13 |
| IDR permit and LOST guidance. Read for physical presence, remote seller and marketplace permit obligations. | https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/permits-filing-requirements-local-option-sales-tax-lost | 2026-11-13 |
| Iowa Code 423.2. Read for taxed sales and services, remote-seller trigger and ordinary tax base. | https://www.legis.iowa.gov/docs/code/2026/423.2.pdf | 2026-11-13 |
| Iowa Code 423.3. Read for food, prescription, resale, manufacturing and commercial-enterprise exemptions and conditions. | https://www.legis.iowa.gov/docs/code/2026/423.3.pdf | 2026-11-13 |
| IDR digital products/software guidance. Read for taxability and commercial-enterprise exclusive-use exception. | https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/taxation-specified-digital-products-software-and-related-services | 2026-11-13 |
| IDR manufacturing guidance. Read for manufacturer definition and directly/primarily qualifying equipment use. | https://revenue.iowa.gov/taxes/tax-guidance/sales-use-excise-tax/iowa-sales-and-use-tax-manufacturing-and-processing | 2026-11-13 |
| IDR filing frequencies. Read for annual, monthly and seasonal thresholds and payment dates. | https://revenue.iowa.gov/taxes/file-my-taxes/business-taxes/filing-frequency-return-due-dates | 2026-11-13 |
| Iowa Code 421.27. Read for late filing/payment and required electronic-method penalties. | https://www.legis.iowa.gov/docs/code/2026/421.27.pdf | 2026-11-13 |

Not yet confirmed: each transaction address's applicable LOST adoption/date must be checked at filing; specific professional-service classifications and specialized excise taxes require separate official-source review. No general exemption is asserted for every professional service or every manufacturing purchase.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ia-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ia-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
