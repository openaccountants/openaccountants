---
name: ms-sales-tax
description: "Mississippi 2026 sales/use tax: general7%, SNAP-eligible groceries5%, specified services, remote-seller250000 test, out-of-state-hosted software exemption, local tax and filings."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ms-sales-tax"
  jurisdiction: "US-MS"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Mississippi sales and use tax, 2026

> **Built from the law. Not yet approved.** Written by Codex; this version has not been reviewed by an accountant. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

**Answer first:** Mississippi generally taxes retail goods at 7%; SNAP-eligible grocery food/drink is5%, and specified services have statutory rates. A remote-software exemption depends on out-of-state hosting; local taxes can exceed the old approximate7.25% claim. [DOR rates](https://www.dor.ms.gov/business/sales-use-tax/sales-tax-rates); [Notice72-23-12](https://www.dor.ms.gov/sites/default/files/notices-technical-bulletins/72-23-12%2520Computer%2520Software%2520DPP%2520Notice%2520.pdf); [DOR local-tax FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions).

## Scope

Ordinary Mississippi retail sales, specified services, remote sellers and taxable use. This skill owns the state sales/use job. Actual local special levies, construction/industry classifications and unusual mixed software contracts need the facts below. Load `us-sales-tax` for the general federal-system owner context.

## Ask the client first

1. Business location, Mississippi premises/workers/inventory, registration and first taxable sales?
2. Rolling twelve-month delivered sales, direct/marketplace reports and remote seller collection status?
3. Product/service contracts: goods, SNAP-eligible food versus prepared meals, software, server location and mixed charges?
4. Delivery/use/sale location and date, actual local tax/industry, exemption certificates and manufacturing qualification?
5. Sales/purchases ledger, exempt/resale sales, stock withdrawals, untaxed purchases, assigned filing periods and payments?

## The method, step by step

1. **Determine seller/use liability.** Physical business activity creates its own sales-tax obligations. DOR describes out-of-state seller collection where Mississippi sales **exceed$250,000 in any twelve-month period**; this is not a transaction-count test or a shield for physical-presence sellers. Identify collection through marketplaces separately and keep reports before excluding their tax from the seller's reconciliation. [DOR sales/use FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions).
2. **Classify the tax base.** Ordinary tangible goods/clothing generally7%. Groceries must meet the statutory SNAP-eligible food/drink condition for5%; SNAP-paid food has its own exemption, and ordinary prepared meals do not qualify merely because they are food. Services are taxed when specified; the old claim that virtually all services/professions are taxable was too broad. Use the actual listed activity and gross proceeds/income base. [DOR rate/activity list](https://www.dor.ms.gov/business/sales-use-tax/sales-tax-rates); [HB1§3,27-65-17(1)(n)](https://billstatus.ls.state.ms.us/documents/2025/html/HB/0001-0099/HB0001SG.htm); [DOR food exemptions](https://www.dor.ms.gov/business/sales-use-tax/sales-tax-exemptions).
3. **Apply software boundaries.** Computer software sales/services are generally taxable. Remotely accessed software hosted on servers **outside Mississippi** is exempt under Notice72-23-12. Determine where it is hosted and what is sold; do not exempt every SaaS label. Mixed taxable/non-taxable charges may be reasonably allocated to separately identifiable items with books/records support; a software direct-pay permit changes collection/remittance procedure, not ultimate taxability. [Entire software notice](https://www.dor.ms.gov/sites/default/files/notices-technical-bulletins/72-23-12%2520Computer%2520Software%2520DPP%2520Notice%2520.pdf).
4. **Test other exemptions/reduced rates.** Valid resale inventory may be purchased tax-free but stock withdrawn for use creates use tax. Retail prescription drugs are exempt; manufacturing machinery is listed at 1.5%, subject to actual qualifying facts and any separate certified exemptions. [DOR exemptions](https://www.dor.ms.gov/business/sales-use-tax/sales-tax-exemptions); [DOR manufacturing rate](https://www.dor.ms.gov/business/sales-use-tax/sales-tax-rates); [Resale/use FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions).
5. **Source, compute and reconcile.** Establish actual Mississippi sale/use and local jurisdiction. The old blanket origin label is held pending the applicable transaction sourcing rule; it must not remove remote/use liability. General state tax=taxable base x0.07; qualifying grocery base x0.05; use the specified rate for other classifications. Determine actual local levy and exempt base separately. DOR identifies Tupelo0.25%, Jackson1% on specified sales and numerous special tourism/economic levies; no statewide7.25% ceiling applies. [DOR local-tax and use-tax FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions). Reconcile gross sales, exclusions, marketplace collection, purchases, stock withdrawals, credits and tax already paid before filing.

### Rates, bands and thresholds

| 2026 item | Amount or rule | Authority |
| --- | --- | --- |
| General retail goods | 7% | [DOR retail list](https://www.dor.ms.gov/business/sales-use-tax/sales-tax-rates) |
| Qualifying groceries | 5%, SNAP-eligible food/drink not actually paid with exempt benefits | [DOR groceries](https://www.dor.ms.gov/business/sales-use-tax/sales-tax-rates); [HB1§3](https://billstatus.ls.state.ms.us/documents/2025/html/HB/0001-0099/HB0001SG.htm) |
| Qualifying manufacturing machinery | 1.5%, verify qualification | [DOR machinery row](https://www.dor.ms.gov/business/sales-use-tax/sales-tax-rates) |
| Remote collection test | Sales exceed$250,000 in any twelve-month period | [DOR seller-use FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions) |
| Local levy | Actual location/activity; Tupelo0.25%, Jackson1% specified sales, other special levies | [DOR local-tax FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions) |

## Worked cases

### Groceries and ordinary merchandise

Assume $4,000 qualifying SNAP-eligible groceries purchased with ordinary funds and$6,000 regular taxable merchandise. State tax=$200+$420=$620. Local levies require the actual address/activity; no local rate is assumed in this case.

```oa-check
name: MS grocery and merchandise state tax
inputs:
  groceries: 4000
  merchandise: 6000
steps:
  - grocery_tax: groceries * 0.05
  - merchandise_tax: merchandise * 0.07
  - state_total: grocery_tax + merchandise_tax
expected:
  grocery_tax: 200
  merchandise_tax: 420
  state_total: 620
```

### Hosted software has a factual exemption test

An ordinary$5,000 software licence sale is taxable at 7% absent an exemption, giving$350. A separate$5,000 contract for remotely accessed software documented as hosted outside Mississippi meets the notice's hosting exemption and produces no state tax on that exempt charge. The invoice label alone cannot establish the second result.

```oa-check
name: MS software hosting boundary
inputs:
  charge: 5000
steps:
  - ordinary_tax: charge * 0.07
  - exempt_hosted_tax: charge * 0
expected:
  ordinary_tax: 350
  exempt_hosted_tax: 0
```

## When to refuse or refer

Refer unclear service classification, software hosting/allocation, contractor taxes, direct-pay permits, manufacturing eligibility and local special levies. Stop a combined-rate quote without the actual location/activity. Never state every service taxable, every SaaS exempt or groceries always exempt; use the statutory facts and compute where established.

## Filing and payment

Register the proper sales/seller-use account through DOR's TAP process before taxable activity as required. Returns/payment are due the20th following the assigned period, next business day for weekends/holidays. File required zero returns and reconcile payments to the current account. [DOR registration/filing FAQ](https://www.dor.ms.gov/business/business-tax-frequently-asked-questions). Preserve exemptions, software-hosting evidence and filed returns; correct affected periods through the authorized amendment process.

## Completion checklist

Document liability and period, classification/rate, food/software facts, exemptions, jurisdiction/local tax, use-tax purchases and marketplace reconciliation; then save filing/payment acknowledgments.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| DOR sales tax rates; read for for complete retail/manufacturing/specified-service activity rows and neighbouring special rates. | https://www.dor.ms.gov/business/sales-use-tax/sales-tax-rates | 2026-11-13 |
| DOR business FAQ; read for for sales/use distinction,250000 threshold, local levies, resale/withdrawals, permits and due-date sections. | https://www.dor.ms.gov/business/business-tax-frequently-asked-questions | 2026-11-13 |
| Notice72-23-12; read for for complete software/hosting definition, mixed allocation and direct-pay procedure. | https://www.dor.ms.gov/sites/default/files/notices-technical-bulletins/72-23-12%2520Computer%2520Software%2520DPP%2520Notice%2520.pdf | 2026-11-13 |
| DOR exemptions; read for for prescription medicines, resale/industrial and food/SNAP categories plus adjacent conditions. | https://www.dor.ms.gov/business/sales-use-tax/sales-tax-exemptions | 2026-11-13 |
| HB1§3 final text; read for for grocery definition/rate/effective date and neighbouring municipal provisions. | https://billstatus.ls.state.ms.us/documents/2025/html/HB/0001-0099/HB0001SG.htm | 2026-11-13 |
| DOR 2025 legislation; read for for implemented HB1 grocery reduction. | https://www.dor.ms.gov/forms-resources/laws-regulations/2025-legislation | 2026-11-13 |

Not yet confirmed: transaction-specific origin/destination sourcing and actual special local tax bases/rates, marketplace threshold-count details, new legislative changes after the cited rules, particular manufacturing asset/certificate qualification and mixed-service allocation. The old non-SST membership assertion is not reverified or used. The old0.25% local maximum/7.25% ceiling and blanket service/SaaS claims are superseded or held unresolved, not usable pricing rules.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ms-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ms-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
