---
name: wy-sales-tax
description: "Apply Wyoming 2026 sales and use tax to physical and remote sellers, marketplace transactions and untaxed purchases. Covers the 4% state tax, current nexus law, food and equipment exemptions, digital products, 2026 use-tax consolidation, WYIFS filing and vendor compensation. Load us-sales-tax for the national workflow."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/wy-sales-tax"
  jurisdiction: "US-WY"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Wyoming sales and use tax, tax year 2026

> **Source-cited draft.** Written by Codex. Not reviewed by an accountant. This skill supports a professional working paper; review the taxpayer facts and current forms before filing. Circular 230 section 10.37: this material is not a legal opinion or a substitute for reasonable factual and legal inquiry.

**Answer first.** Wyoming imposes 4% state sales/use tax plus the applicable local taxes. Remote economic nexus uses gross Wyoming revenue **over $100,000** in the current or prior calendar year; the transaction-count test is repealed. Use tax is still due when the seller did not collect.

## Scope and who this is for

Regular vendors, remote sellers, marketplace sellers and consumers with untaxed Wyoming use. This is the state owner; `us-sales-tax` handles the national workflow. From July 1, 2026, SF0079 consolidates use-tax administration into sales-tax provisions; the current Title 39 text reflects that reorganization. Earlier periods need the then-effective use-tax provisions. Mineral severance, property, wind-generation tax and detailed lodging returns remain separate jobs.

## Ask the client first

1. What are the sale dates, products/services, delivery/receipt locations and amounts, including digital and bundled items?
2. What Wyoming premises, employees, inventory and current/prior calendar-year gross receipts establish nexus?
3. Which sales are marketplace-facilitated and supported by facilitator collection statements, versus direct sales?
4. What exemption/resale certificates and actual end-use evidence support each untaxed sale?
5. What untaxed purchases, other-state tax receipts, assigned filing frequency, permit and WYIFS access exist?

## The method, step by step

### Rates, bands and thresholds

| Item and conditions | Amount / treatment | Official source |
| --- | --- | --- |
| State sales/use rate | 4% (3% plus continuing 1%) | [39-15-104(a)-(b)](https://www.wyoleg.gov/statutes/compress/title39.pdf) |
| Local rate | Use current location/date-specific DOR rate; no universal combined ceiling is assumed | [official text](https://excise-tax-div.wyo.gov/salesuselodging-tax/tax-rates) |
| Remote seller economic nexus | Gross Wyoming revenue > $100,000, current or prior calendar year; no transaction-count test | [39-15-501(a)](https://www.wyoleg.gov/statutes/compress/title39.pdf) |
| Regular vendor initial license | $60, subject to statutory remote/Streamlined exceptions; separate place licenses | [39-15-106](https://www.wyoleg.gov/statutes/compress/title39.pdf) |
| Reduced-frequency reporting | DOR may authorize quarterly/annual if tax in a month is < $150; do not self-switch | [39-15-107(a)(i)](https://www.wyoleg.gov/statutes/compress/title39.pdf) |
| Vendor compensation | 1.95%, maximum $500 in a month, payment by the 15th of the due month | [39-15-107(b)(xi)](https://www.wyoleg.gov/statutes/compress/title39.pdf) |
| Additional statewide lodging assessment | 5%, in addition to ordinary sales tax; check other local lodging taxes | [39-15-104(h)](https://www.wyoleg.gov/statutes/compress/title39.pdf) |

### Nexus, sourcing and marketplace split

Physical presence is independent of the economic threshold. A remote seller crosses the gross-revenue test at **more than** $100,000; the old 200-transaction route was repealed in 2024. Marketplace facilitators are vendors for facilitated sales and collect on their own and facilitated sales under W.S.39-15-502; reconcile their statements so the seller does not collect twice. Sources: [39-15-501 and 502](https://www.wyoleg.gov/statutes/compress/title39.pdf).

Sourcing is a hierarchy: customer receipt at the seller's business location first, then the known receipt/delivery location; statutory fallback addresses apply if those facts are unavailable. Leases, vehicles, telecommunications and direct mail have special rules. Use the DOR rate for the actual jurisdiction/date, not an assumed statewide 6%. Source: [39-15-104(f)](https://www.wyoleg.gov/statutes/compress/title39.pdf), [official text](https://excise-tax-div.wyo.gov/salesuselodging-tax/tax-rates).

### Base and preserved category rules

| Category | 2026 treatment and conditions | Official source |
| --- | --- | --- |
| Tangible goods, clothing and equipment rentals | Generally taxable retail sales or rentals unless a specific exemption applies | [39-15-103(a)(i)(A)-(B)](https://www.wyoleg.gov/statutes/compress/title39.pdf) |
| Food for domestic home consumption | Exempt; statutory definition excludes alcohol, tobacco and prepared food, not candy/soft drinks merely by name. Old blanket candy/soft-drink taxation is not the rule. | [39-15-101(a)(xli), 105(a)(vi)(E)](https://www.wyoleg.gov/statutes/compress/title39.pdf) |
| Prepared food and restaurant meals | Taxable subject to statutory definitions and exceptions | [39-15-101(a)(xlvi), 103(a)(i)(F)](https://www.wyoleg.gov/statutes/compress/title39.pdf) |
| Prescription human medical goods | Listed prescription drugs (excluding OTC), insulin/administration supplies, prosthetics, hearing aids, glasses, mobility/DME and assistive devices qualify under the listed prescription conditions | [39-15-105(a)(vi)(B)-(C)](https://www.wyoleg.gov/statutes/compress/title39.pdf) |
| Services | Intrastate telecom, passenger transport, utilities, lodging, admissions and repair/alteration/improvement of tangible property are enumerated taxable services; no blanket repair-labor exemption | [39-15-103(a)(i)(C)-(K)](https://www.wyoleg.gov/statutes/compress/title39.pdf) |
| Digital audio/video/books | Specified digital products with permanent purchaser use are taxable; commercial redistribution and listed trade-association benefits have exceptions | [39-15-101(a)(xliii),103(a)(i)(P)](https://www.wyoleg.gov/statutes/compress/title39.pdf) |
| Hardware/system software and physical software media | Taxable as specified; do not infer the treatment of hosted SaaS, electronically delivered software or custom-development contracts from the media rule | [39-15-103(a)(i)(O)](https://www.wyoleg.gov/statutes/compress/title39.pdf) |
| Manufacturing | Ingredients/components, qualifying consumed chemicals/catalysts and containers can be exempt; machinery used directly and predominantly in manufacturing has an exemption through December 31,2042. The old assertion that no manufacturing machinery exemption exists is incorrect. | [39-15-105(a)(iii)(A),(viii)(O)](https://www.wyoleg.gov/statutes/compress/title39.pdf) |
| Farm/ranch | Livestock, production feed, seed and fertilizer qualify under production conditions. Farm implements must be designed/adapted and used **exclusively** for agriculture; titled vehicles, snowmobiles, lawn tractors, ATVs and repair/replacement parts are excluded from that implement exemption. | [39-15-105(a)(iii)(B),(viii)(H)](https://www.wyoleg.gov/statutes/compress/title39.pdf) |
| Resale/government/charity | Wholesale resale and specific government/religious/charitable categories qualify; a nonprofit label alone does not prove exemption. Keep the signed resale/exemption evidence. | [39-15-105(a)(iii)(F),(iv),(vi)(F)](https://www.wyoleg.gov/statutes/compress/title39.pdf) |
| Mining/oil/gas/wind | Review actual equipment and service stage. Post-production-casing oil/gas well-site services are specifically taxable; special industry incentives must be independently established. | [39-15-103(a)(i)(K),105](https://www.wyoleg.gov/statutes/compress/title39.pdf) |

Use tax applies to taxable purchases first used/stored/consumed in Wyoming when the seller did not collect. Credit legally imposed and paid sales tax to another state only up to the Wyoming use-tax liability, with documentary proof. Sources: [39-15-103(c)(ii),109(d)(v)](https://www.wyoleg.gov/statutes/compress/title39.pdf).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Exactly $100,000 remote receipts, no physical presence | Revenue test alone not met; > $100,000 is required. |
| Qualifying groceries versus prepared meal | Classify separately; exemption is not every food sale. |
| Farm tractor used partly personally | Do not apply exclusive-agriculture exemption. |
| Claimed professional/personal care/cleaning/landscaping/IT service exemption | Classify the actual service and any taxable goods/repair bundle; old blanket assertions are listed unconfirmed below. |
| Jackson/Teton hotel | Sales tax plus statewide 5% lodging assessment and applicable local lodging taxes; the old no-state-lodging claim is false. |
| Furniture bought outside Wyoming with no tax | Accrue Wyoming use tax at the use location's rate; no credit without tax legally paid. |
| Incorporating in Wyoming | No general income tax does not eliminate sales, property, mineral, payroll or annual license duties; no separate Commerce Tax is identified here. |

Sources: [39-15-103 to 105,109,501](https://www.wyoleg.gov/statutes/compress/title39.pdf).

## Worked cases

**Case 1.** A hypothetical jurisdiction/date has a documented 6% combined general sales rate. An $800 equipment sale produces $48 tax and $848 invoice; $200 qualifying home-consumption groceries produce no tax. A $300 jacket produces $18 tax and $318 invoice. These retain the old goods examples without asserting that today's Cheyenne/Jackson rates are universally 6%.

```oa-check
name: WY taxable goods and groceries
inputs:
  equipment: 800
  groceries: 200
  jacket: 300
  documented_rate: 0.06
steps:
- equipment_tax: equipment * documented_rate
- equipment_total: equipment + equipment_tax
- grocery_tax: groceries * 0
- jacket_tax: jacket * documented_rate
- jacket_total: jacket + jacket_tax
expected:
  equipment_tax: 48
  equipment_total: 848
  grocery_tax: 0
  jacket_tax: 18
  jacket_total: 318
```

**Case 2, payment-date decision.** $10,000 tax eligible for compensation, paid by the 15th, gives min($10,000 x 1.95%,$500) = **$195** credit and $9,805 payment. Payment on the statutory last-day due date can still be timely for the return but misses the compensation cutoff: **$10,000** is payable. At $40,000 eligible tax the computed $780 credit is capped at $500.

```oa-check
name: WY vendor timely payment decision
inputs:
  tax: 10000
  large_tax: 40000
steps:
- early_credit: min(tax * 0.0195, 500)
- early_payment: tax - early_credit
- last_day_payment: tax
- large_credit: min(large_tax * 0.0195, 500)
expected:
  early_credit: 195
  early_payment: 9805
  last_day_payment: 10000
  large_credit: 500
```

Preserved corrected old cases: qualifying $40,000 and $60,000 exclusive-use farm tractors are exempt ($0 tax); $105,000 remote receipts cross the revenue threshold. At an assumed documented 6% general rate, $2,000 untaxed furniture produces $120 use tax. $2 million drilling equipment and $5 million wind turbines require an actual exemption determination; no incentive is presumed. A three-night $350 room charge totals $1,050: at assumed general 6% plus statewide lodging 5%, tax is $115.50 and invoice $1,165.50 **before any additional local lodging tax**, replacing the old incomplete $63 tax. The old $400/night hotel question follows the same combined-tax analysis. Hosted SaaS remains unconfirmed below rather than being treated as categorically exempt.


## When to refuse or refer

Refer ambiguous products/bundles, hosted software and digital licensing, mineral/energy incentives, lodging local levies, vehicle/county-treasurer tax, audits, voluntary disclosure and abatement. An unresolved certificate or taxability question blocks the exemption, not the obligation to investigate it.

## Filing and payment

Register a regular vendor through [DOR registration](https://excise-tax-div.wyo.gov/salesuselodging-tax/salesuselodging-registration) and establish access in [WYIFS](https://excise-wyifs.wy.gov). DOR labels monthly/quarterly filings **Return 41**, annual **Return 42**, occasional vendors **Return 43**, and unlicensed consumers **Return 44**. Choose the actual account/period; reconcile gross receipts, exempt amounts, jurisdictional taxable sales, use purchases and credits to supporting schedules. Use the current DOR return instructions for field placement; do not substitute an example-only paper form. Submit the return and payment and retain both records. Sources: [official text](https://excise-tax-div.wyo.gov/salesuselodging-tax/salesuselodging-returns), [official text](https://excise-tax-div.wyo.gov/wyifs).

The normal return/payment deadline is the **last day of the following month**. Reduced-frequency filing needs DOR authorization; the old $100/$300 frequency tiers are replaced by the statutory < $150 monthly-tax condition. Compensation requires payment **by the 15th**, earlier than the normal due date. Keep books/invoices at least three years, and longer through an open audit; final return/payment is due within 30 days after discontinuance/sale. Source: [39-15-107(a),(b)(xi),108(a)](https://www.wyoleg.gov/statutes/compress/title39.pdf).

The statutory deficiency penalty for negligence/intentional disregard without fraud is 10%; fraud is 25%. Interest on post-June1994 sales is annual prime-plus-four, adjusted as prescribed, maximum18%, rather than a general 1%-monthly assumption. The current numeric 2026 rate and any additional routine late-return charge are not confirmed here. Source: [39-15-108(b)-(c)](https://www.wyoleg.gov/statutes/compress/title39.pdf).

## Completion checklist

- Reconcile channel totals and facilitator collection.
- Confirm product classification, actual sourcing, date-specific rates and exemption proof.
- Accrue use tax and document allowable credits.
- Preserve the submitted return, early-payment compensation support and receipts.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Wyoming Statutes Title39. Read for 39-15-101,103-109, local-option provisions and501-502: definitions, base, sourcing, exemptions, nexus, records, penalties and credit. | https://www.wyoleg.gov/statutes/compress/title39.pdf | 2026-11-13 |
| SF0079 enrolled act,2026. Read for section1 and final applicability/effective provisions: July1,2026 administration consolidation; section2 deferred to2027. | https://www.wyoleg.gov/2026/Enroll/SF0079.pdf | 2026-11-13 |
| DOR WYIFS instructions. Read for official portal and license/return module links. | https://excise-tax-div.wyo.gov/wyifs | 2026-11-13 |
| DOR registration. Read for regular vendor registration route. | https://excise-tax-div.wyo.gov/salesuselodging-tax/salesuselodging-registration | 2026-11-13 |
| DOR returns. Read for Return41/42/43/44 and supplements; field instructions not read. | https://excise-tax-div.wyo.gov/salesuselodging-tax/salesuselodging-returns | 2026-11-13 |
| DOR rate page. Read for current sales/use/lodging rate resources and annual-interest publication links. | https://excise-tax-div.wyo.gov/salesuselodging-tax/tax-rates | 2026-11-13 |

Not yet confirmed: Hosted SaaS, electronically delivered prewritten software, custom software, personal-care/cleaning/landscaping/IT services and special wind/mineral incentive eligibility from the old version are not confirmed as blanket exemptions. Current local general/lodging rates and the numeric2026 delinquency-interest rate require the dated DOR schedule. Exact2026 authenticated WYIFS field mapping and universal e-file mandate are not confirmed. The old generic minimum$25 late-filing penalty was not established. Streamlined full-member status, SSTRS/CSP service availability and a universal certificate-at-time-of-sale rule from the old version were not independently confirmed; the statutory Streamlined licensing exception and record requirements above remain. No blanket exemption is inferred from these gaps.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `wy-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/wy-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
