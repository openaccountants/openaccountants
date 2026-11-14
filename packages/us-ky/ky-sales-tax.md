---
name: ky-sales-tax
description: "Kentucky sales and use tax in 2026: uniform state rate, dated economic nexus changes, product and service taxability, purchaser use tax, exemptions and MyTaxes filing."
version: "2.2"
jurisdiction: US-KY
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
category: state-tax
---

# Kentucky sales and use tax, 2026

> **General reference only.** Source-cited draft, not approved by an accountant. For US Treasury Circular 230 §10.37 purposes this is general reference material; a qualified professional must check the facts, current law and forms before filing or taking a position.

**Answer first.** Kentucky sales/use tax is uniform statewide. Determine the transaction date before applying the 2026 remote-seller rule. Load `us-sales-tax` for the federal framework, then this state skill for Kentucky's own rules.

## Who this applies to

Kentucky retailers, remote retailers and marketplace providers with a collection duty, and purchasers using taxable property or services in Kentucky without tax paid. Physical nexus is not protected by the remote-seller threshold. The tax year is 2026; this skill distinguishes changes during that year.

## Rates, bands and thresholds

| Item | Amount and conditions | Official source |
| --- | --- | --- |
| State sales and use tax | 6% of taxable gross receipts/purchase price; no local sales/use tax | [DOR](https://revenue.ky.gov/Business/Sales-Use-Tax/Pages/default.aspx) |
| Remote retailer/marketplace nexus through 31 July 2026 | USD 100,000 or more gross receipts OR 200 or more separate transactions in previous or current calendar year | [DOR 2026 bulletin p.6](https://revenue.ky.gov/News/Publications/Sales%20Tax%20Newsletters/Sales%20Tax%20Facts%20-%20Summer%202026.pdf) |
| Remote retailer/marketplace nexus from 1 August 2026 | USD 100,000 or more gross receipts in previous or current calendar year; transaction-count test removed | [DOR 2026 bulletin p.6](https://revenue.ky.gov/News/Publications/Sales%20Tax%20Newsletters/Sales%20Tax%20Facts%20-%20Summer%202026.pdf) |
| New data-brokering services | 6% from 1 August 2026, subject to governmental seller exemption | [KRS 139.200(2)(ay)](https://apps.legislature.ky.gov/Law/statutes/statute.aspx?id=58186); [bulletin p.3](https://revenue.ky.gov/News/Publications/Sales%20Tax%20Newsletters/Sales%20Tax%20Facts%20-%20Summer%202026.pdf) |
| Ordinary monthly filing/payment | 20th following month; next business day for weekend/holiday; assigned accelerated filers have different timing | [DOR retail packet, filing Q3](https://revenue.ky.gov/Business/Sales-Use-Tax/Documents/Retail%20Packet%20%2811-17%29.pdf) |

## The base

Retail sales, leases and rentals of tangible personal property and digital property are generally taxable. Clothing has no blanket exemption. Prepared food is taxable. Food/food ingredients for human consumption have an exemption with prepared-food/vending limitations. Prescription medical items are exempt only within KRS 139.472; do not apply that rule automatically to animal prescriptions. Manufacturing machinery requires the applicable new/expanded-industry conditions, not an exemption for every item of equipment. Resale requires the proper certificate. [KRS 139.200](https://apps.legislature.ky.gov/Law/statutes/statute.aspx?id=58186); [official tax expenditure report, sales exemptions](https://apps.legislature.ky.gov/AgencyReports/IJC/AR/OSBD/TEA/2025%20to%202027%20Report.pdf); [KRS 139.472](https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=53349).

The enumerated-service statute covers landscaping, janitorial, pet care and small-animal veterinary services, laundry, admissions, fitness instruction, cosmetic surgery and many other listed services. It distinguishes medically necessary massage and lab testing exceptions, and separately stated onsite security guards from security monitoring. Do not replace the list with an assumption that all services are taxed or all professional services are exempt. Ordinary legal/accounting work is not a listed category, but separately sold property or a listed service must be tested. The 2023 expansion remains relevant in 2026. Prewritten software, digital goods and prewritten software access services (including SaaS) fall within the statutory property/service categories. [KRS 139.200(1)-(2)](https://apps.legislature.ky.gov/Law/statutes/statute.aspx?id=58186).

From 1 August, data brokering is included, while qualifying direct religious-function sales by religious institutions become exempt. Earlier religious-function purchase relief continues. The same bulletin explains the end of registration for institutions whose July filing completes taxable sales. Special event, fuel, telecommunications and incentive regimes need separate analysis; the general retail rate is not a substitute. [2026 bulletin pp.3-4](https://revenue.ky.gov/News/Publications/Sales%20Tax%20Newsletters/Sales%20Tax%20Facts%20-%20Summer%202026.pdf).

Kentucky sourcing follows receipt/delivery of property or service under the applicable sourcing rule. Obtain customer delivery/use locations, including employee locations for SaaS, rather than blindly using billing address. When the supplier does not collect, compute purchaser use tax; do not assume out-of-state sales escape tax. [DOR sourcing answers](https://taxanswers.ky.gov/Sales-and-Excise-Taxes/Pages/Sourcing-Guidelines.aspx).

## Deadlines and filing

1. Establish physical/economic nexus and identify taxable products, exemptions, marketplace-collected sales and direct sales separately. The general DOR landing page still prints the old 200-transaction test; the dated summer bulletin and amended KRS 139.340/139.450 govern from August.
2. Register with DOR and keep the sales/use account and assigned frequency. MyTaxes at `mytaxes.ky.gov` requires a user account, business linkage and portal PIN. All monthly, quarterly and annual accounts must electronically file/pay as functionality becomes available, unless a statutory waiver is granted. [DOR mandate](https://revenue.ky.gov/News/Pages/Online-Filing-and-Payment-Mandate-for-Sales-and-Excise-Tax-Returns.aspx).
3. Select the sales/use account and period. Reconcile total receipts, deductions/exemptions and tax collected to invoices and marketplace statements; keep certificates. Enter taxable sales and purchases subject to use tax in their respective fields. The paper retail packet's use-tax line is 23(a); a consumer use-tax return 51A113 uses line 1 for purchases. Do not substitute an assumed current portal line number for the displayed field. [Retail packet](https://revenue.ky.gov/Business/Sales-Use-Tax/Documents/Retail%20Packet%20%2811-17%29.pdf).
4. Submit the return, pay by the due date and retain acknowledgement, payment reference and ledger reconciliation. File at the assigned frequency, even where no tax is due; confirm accelerated or nonmonthly dates on the account. Do not stop reporting until cancellation is accepted. The current bulletin routes updates/cancellation via Form 10A104 or MyTaxes Requests > New Service Request. [Retail packet](https://revenue.ky.gov/Business/Sales-Use-Tax/Documents/Retail%20Packet%20%2811-17%29.pdf); [summer bulletin p.10](https://revenue.ky.gov/News/Publications/Sales%20Tax%20Newsletters/Sales%20Tax%20Facts%20-%20Summer%202026.pdf).

## Penalties and interest

Late filing/payment and interest can apply independently. The current revenue-wide interest notice confirms the unchanged 2026 base rate and statutory deficiency adjustment; annual-return penalty details remain in `ky-income-tax`. Sales-specific failure-to-collect penalties and any timely-filer compensation limits have not been rechecked for 2026 below. Do not claim the old packet's compensation without confirmation.

## Cross-border points

A marketplace's collection does not remove duties for a retailer's own taxable sales. Drop shipments are two transactions; an out-of-state nonregistered retailer can use the certificate procedure in the summer bulletin, while the purchaser may owe use tax if neither seller collects. Do not double-pay tax already properly collected. Local sales tax is absent, but separate occupational or excise taxes can still exist. [DOR](https://revenue.ky.gov/Business/Sales-Use-Tax/Pages/default.aspx); [bulletin p.9](https://revenue.ky.gov/News/Publications/Sales%20Tax%20Newsletters/Sales%20Tax%20Facts%20-%20Summer%202026.pdf).

## Two worked examples that recompute

**Case 1, taxable sales and untaxed purchase.** A registered seller has USD 12,000 taxable merchandise receipts, USD 2,000 valid exempt resale receipts and USD 1,500 taxable business purchases with no tax paid. Output tax USD 720, use tax USD 90, total USD 810 before any confirmed allowance.

```oa-check
name: Kentucky sales and purchaser use tax
inputs:
  taxable_sales: 12000
  resale: 2000
  untaxed: 1500
steps:
  - output_tax: taxable_sales * 0.06
  - use_tax: untaxed * 0.06
  - total: output_tax + use_tax
  - resale_tax: resale * 0
expected:
  output_tax: 720
  use_tax: 90
  total: 810
  resale_tax: 0
```

**Case 2, registration decision across August.** A remote retailer with no physical nexus makes 250 Kentucky transactions totalling USD 90,000. Before August, the transaction count meets nexus; from August the count alone no longer does. At USD 110,000 receipts the remaining test is met in either period. These are separate annual-receipts scenarios, not permission to cancel an existing account without DOR processing. Tax on USD 10,000 taxable post-threshold sales is USD 600 when a collection duty exists, versus zero seller collection in the no-nexus scenario; purchaser use tax remains relevant.

```oa-check
name: Kentucky nexus decision tax consequence
inputs:
  receipts_low: 90000
  receipts_high: 110000
  taxable_sales: 10000
steps:
  - below_gap: 100000 - receipts_low
  - above_gap: receipts_high - 100000
  - collect_if_nexus: taxable_sales * 0.06
  - seller_collect_without_nexus: taxable_sales * 0
expected:
  below_gap: 10000
  above_gap: 10000
  collect_if_nexus: 600
  seller_collect_without_nexus: 0
```

## Ask the client first

1. Transaction dates, prior/current calendar-year Kentucky receipts and pre-August transaction count?
2. Physical locations, inventory, employees and marketplace/direct sales split?
3. Exact goods/services, bundles, SaaS users' locations and delivery/use addresses?
4. Exemption certificates, resale, food/medical/manufacturing eligibility and religious-function facts?
5. Untaxed purchases, other tax paid, account/frequency, filings/payments and cancellation status?

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| DOR sales/use page. Read for state/local rate, property and service base, remote sellers and current filing links. | https://revenue.ky.gov/Business/Sales-Use-Tax/Pages/default.aspx | 2026-11-13 |
| KRS 139.200. Read for full taxable-service list, exclusions and August 2026 effective date. | https://apps.legislature.ky.gov/Law/statutes/statute.aspx?id=58186 | 2026-11-13 |
| DOR Summer 2026 Sales Tax Facts. Read for pp.3-6 tax base and nexus changes; p.9 drop shipments; p.10 account maintenance. | https://revenue.ky.gov/News/Publications/Sales%20Tax%20Newsletters/Sales%20Tax%20Facts%20-%20Summer%202026.pdf | 2026-11-13 |
| DOR retail packet. Read for retailer and filing questions; older paper-field references, not current electronic mandate. | https://revenue.ky.gov/Business/Sales-Use-Tax/Documents/Retail%20Packet%20%2811-17%29.pdf | 2026-11-13 |
| DOR electronic filing mandate. Read for all frequencies and account linkage. | https://revenue.ky.gov/News/Pages/Online-Filing-and-Payment-Mandate-for-Sales-and-Excise-Tax-Returns.aspx | 2026-11-13 |
| DOR sourcing answers. Read for receipt of services and software licences used outside Kentucky. | https://taxanswers.ky.gov/Sales-and-Excise-Taxes/Pages/Sourcing-Guidelines.aspx | 2026-11-13 |
| KRS 139.472. Read for medical item exemption and conditions. | https://apps.legislature.ky.gov/law/statutes/statute.aspx?id=53349 | 2026-11-13 |
| Official Tax Expenditures report 2025-2027. Read for sales food, machinery and prescription exemption descriptions. | https://apps.legislature.ky.gov/AgencyReports/IJC/AR/OSBD/TEA/2025%20to%202027%20Report.pdf | 2026-11-13 |

Not yet confirmed: current 2026 seller-compensation amount/eligibility, sales-specific penalty figures, accelerated/quarterly/annual account-specific due dates and full machinery-exemption eligibility for a particular purchase. No federal or third-party rate table is substituted.
