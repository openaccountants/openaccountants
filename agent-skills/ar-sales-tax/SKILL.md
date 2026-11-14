---
name: ar-sales-tax
description: "Arkansas 2026 state and local sales and use tax: general rate, grocery exemption, physical and remote-seller nexus, sourcing, exemptions, registration and ET-1 filing."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ar-sales-tax"
  jurisdiction: "US-AR"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Arkansas sales and use tax, 2026

> **Built from the law. Not yet approved.** Written by Codex; no accountant has reviewed this version. General reference only. Under Circular 230 section 10.37, apply the cited authorities to the actual facts and obtain qualified professional review before filing or acting.

**Answer first:** Arkansas's general state sales/use rate is 6.5%, plus applicable city/county tax. From January 1, 2026, qualifying food and food ingredients are exempt from **state** sales/use tax, while local taxes continue. The old 0.125% state grocery instruction is superseded. [Legislative handbook sections 1.2, 1.7](https://webftp.blr.arkansas.gov/Home/FTPDocument?path=Assembly%2F2027%2FSummary+Budget+Manuals%2F2026+Tax+Handbook.pdf); [Act 1008](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT1008.pdf). Load `us-sales-tax` for the general federal-system context; this skill owns Arkansas-specific figures.

## Scope

Ordinary retail sales delivered or received in Arkansas, remote sellers/marketplace facilitators, and taxable purchases used in Arkansas without full tax collection. Excises on vehicles, lodging, alcohol, fuel and special industries require their own rules. There is no single combined rate for every Arkansas address.

## Ask the client first

1. Physical locations, staff, inventory and other Arkansas presence?
2. Current/prior-calendar-year Arkansas taxable receipts and transaction count, separated from marketplace-facilitated sales?
3. Exact items/services, food preparation and packaging, software delivery method, exempt purchaser/use and supporting certificate?
4. Where did the customer receive each item or first use a service, and on what sale date?
5. Permit/account, assigned filing period, prepayment notices and collection channels?
6. Untaxed business purchases and legally paid tax to another state?

## The method, step by step

### Rates, bands and thresholds

| Rule and conditions | Amount | Official source |
| --- | --- | --- |
| General state sales tax on ordinary taxable retail goods/services | 6.5% | [Legislative handbook section 1.7](https://webftp.blr.arkansas.gov/Home/FTPDocument?path=Assembly%2F2027%2FSummary+Budget+Manuals%2F2026+Tax+Handbook.pdf) |
| General state compensating use tax | 6.5% | [Legislative handbook section 1.2](https://webftp.blr.arkansas.gov/Home/FTPDocument?path=Assembly%2F2027%2FSummary+Budget+Manuals%2F2026+Tax+Handbook.pdf) |
| Food and food ingredients, January 1 2026 onward | 0% state; full applicable local taxes remain | [Act 1008 sections 9, 11, 17; DFA announcement](https://www.dfa.arkansas.gov/wp-content/uploads/Whatsnew2025_1.pdf) |
| Prepared food, alcohol, dietary supplements and tobacco | Outside qualifying-food exemption; apply ordinary rate unless another specific rule applies | [Act 1008 food definitions/exclusions](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT1008.pdf) |
| Remote seller/facilitator taxable Arkansas sales, current or previous calendar year | **Exceeding $100,000 or exceeding 200 transactions** | [Act 822 section 19, section 26-52-111(a)](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2019R%2FPublic%2FACT822.pdf); [DFA current guidance](https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/remote-sellers/) |
| New sales-tax permit | $50, paid electronically with application | [DFA registration](https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/register-for-a-tax-account/) |
| City/county taxes | Address- and date-specific; add to state tax where applicable | [DFA FAQ, local sourcing/lookup](https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/sales-and-use-tax-faqs/) |

1. **Test collection responsibility.** Arkansas physical business activity and taxable sales require analysis independently of the remote-seller threshold. For a remote seller/facilitator without presence, test taxable Arkansas receipts and transaction counts in either current or previous calendar year. Under section 26-52-111(b), facilitated sales belong to the facilitator for this threshold and not the marketplace seller; retain the facilitator's collection records. Do not infer no use tax merely because a remote seller is below threshold. [Act 822 section 19](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2019R%2FPublic%2FACT822.pdf).
2. **Classify the sale.** Ordinary tangible goods, including clothing outside a valid holiday, are taxable. Qualifying food/ingredients changed to state-exempt from January 1, 2026, not local-exempt. Prescription drugs/oxygen, sales for resale and qualifying manufacturing equipment have exemptions; establish the statutory purchaser/use conditions before applying them. Prepared food and the other exclusions do not become grocery-exempt. Blanket SaaS/downloaded-software/professional-service conclusions from the old skill are not usable without confirming their specific provisions. [Handbook section 1.7](https://webftp.blr.arkansas.gov/Home/FTPDocument?path=Assembly%2F2027%2FSummary+Budget+Manuals%2F2026+Tax+Handbook.pdf); [Act 1008](https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT1008.pdf).
3. **Source and look up local tax.** Merchandise taken at the seller's store uses that store location. If the seller delivers/ships it, use the customer's receipt/delivery address. Taxable services performed at the customer location generally follow that location; repaired goods delivered back by the seller follow delivery. Use the state's date/address lookup and record the jurisdiction codes and rates. Do not substitute a remembered maximum combined rate. [DFA FAQ, sourcing](https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/sales-and-use-tax-faqs/).
4. **Register through [ATAP](https://atap.arkansas.gov).** Select registration for sales/use tax, provide actual business location (not a post-office box), start date, signed lease if rented and acquisition bill of sale if applicable, and pay the $50 electronically. Other outstanding tax liabilities must be cleared; DFA asks that applicants allow up to two weeks. Retain the permit and account ID. [DFA registration](https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/register-for-a-tax-account/).
5. **Compute tax and use tax.** Multiply the state-taxable base by the applicable state rate and each local base by that jurisdiction's rate. Qualifying groceries have zero state base tax but remain in the relevant local taxable base. For untaxed out-of-state purchases used/stored/consumed in Arkansas, compute use tax; legally paid other-state sales tax may reduce Arkansas liability, with motor-vehicle exceptions. Registered businesses report use tax in Column B of the periodic reporting form. [DFA FAQ, use tax](https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/sales-and-use-tax-faqs/).
6. **File ET-1/ATAP and pay.** Open the sales/use account for the assigned period, reconcile gross sales to taxable sales and documented exemptions, enter use-tax purchases and city/county detail, review any eligible credits, submit and retain acceptance and payment references. DFA's forms page directs taxpayers to ATAP for online returns; paper ET-1 forms are supplied on request. Final screen/box detail remains a gap below. [DFA forms](https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/sales-and-use-tax-forms/).

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Qualifying grocery vs prepared food | State exemption requires Act 1008 definitions; keep item/category records. Local tax remains. |
| Marketplace plus own website | Separate facilitator-collected sales from the seller's own channel for the threshold and avoid double collection. |
| Resale | Obtain supporting exemption documentation; DFA publishes the SST Certificate of Exemption on its forms page. [DFA forms](https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/sales-and-use-tax-forms/). |
| Manufacturing equipment | Exemption is conditional on qualifying manufacturing/processing use; ordinary office equipment does not qualify merely because the buyer manufactures. Refer unclear replacement/expansion facts. |
| Taxable delivery charges | Seller's freight/shipping is in gross receipts when the goods are taxable; direct common-carrier billing is treated separately. [DFA FAQ](https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/sales-and-use-tax-faqs/). |
| Local-tax cap | Ordinary merchandise is taxed on the full invoice; special vehicles/watercraft and eligible business rebates have distinct rules. Do not cap an ordinary retail invoice. [DFA FAQ](https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/sales-and-use-tax-faqs/). |
| Goods shipped out of Arkansas | Check the destination state's collection rules separately; Arkansas's rate does not establish another state's liability. |

## Worked cases

**Case 1: grocery classification decision.** An invented shop sells $200 qualifying unprepared groceries and $100 ordinary taxable household goods in 2026. Assume a documented local rate of 2% solely as an input, not an actual city's rate. Correct state tax is $6.50 on the household goods, plus local tax $6 on all $300, total $12.50. Treating the groceries as ordinary taxable goods would collect $13 too much state tax.

```oa-check
name: AR 2026 grocery state exemption with local tax
inputs:
  groceries: 200
  household: 100
  local_rate: 0.02
steps:
  - state_tax: household * 0.065
  - local_tax: (groceries + household) * local_rate
  - total: state_tax + local_tax
  - wrong_state: (groceries + household) * 0.065
  - overcollection: wrong_state - state_tax
expected:
  state_tax: 6.50
  local_tax: 6
  total: 12.50
  overcollection: 13
```

**Case 2: a low-value remote seller can meet the transaction test.** An invented seller with no physical presence has $90,000 of direct taxable Arkansas sales in 201 transactions in the current calendar year. Receipts do not exceed $100,000, but transactions exceed 200, so collection is required under the statutory alternative. At exactly 200 transactions and $90,000, neither statutory numeric threshold is exceeded; physical presence and purchaser use-tax obligations still need their own tests.

```oa-check
name: AR remote transaction decision
inputs:
  receipts: 90000
  transactions: 201
steps:
  - receipts_excess: max(receipts - 100000, 0)
  - transaction_excess: max(transactions - 200, 0)
expected:
  receipts_excess: 0
  transaction_excess: 1
```

## When to refuse or refer

Refer uncertain software/SaaS/bundled transactions, exemption qualifications, special industries, disputed physical nexus, marketplace liability and local cap/rebate facts. The prior prohibition on computation is retired: sourced arithmetic is part of this skill. Never label grocery food entirely tax-free, since local tax continues.

## Filing and payment

DFA's 2026 calendar has monthly sales/use reports for the previous month on the 20th, moving to June 22, September 21 and December 21 where its calendar specifies. Prepayment obligations have separate dates; use the assigned notice and current calendar. Do not elect a less frequent return without the state's classification. [DFA 2026 calendar](https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/due-dates/). Penalty/interest rates and prepayment qualification were not confirmed from the permitted current sources and are not supplied here.

## Completion checklist

- Taxable/exempt sales and marketplace transactions reconcile to receipts.
- Correct 2026 grocery treatment, delivery address and dated local rate saved.
- Use-tax purchases included; certificates retained.
- Assigned period filed and payment confirmation saved.

## Sources

| Source and reading scope | URL | Read on |
| --- | --- | --- |
| Act 1008 of 2025. Read for entire grocery exemption act, definitions, local-tax preservation and January 1 2026 effective date. | https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2025R%2FPublic%2FACT1008.pdf | 2026-11-13 |
| DFA 2025 sales-tax changes. Read for both pages, especially Act 1008 effective January 1 2026. | https://www.dfa.arkansas.gov/wp-content/uploads/Whatsnew2025_1.pdf | 2026-11-13 |
| Legislative Tax Handbook 2026. Read for sections 1.2 and 1.7 general rate/base and listed exemptions, with neighbouring services/exemptions. | https://webftp.blr.arkansas.gov/Home/FTPDocument?path=Assembly%2F2027%2FSummary+Budget+Manuals%2F2026+Tax+Handbook.pdf | 2026-11-13 |
| Act 822 of 2019. Read for section 19 and adjacent marketplace definitions, threshold alternatives and facilitator allocation. | https://www.arkleg.state.ar.us/Home/FTPDocument?path=%2FACTS%2F2019R%2FPublic%2FACT822.pdf | 2026-11-13 |
| DFA remote sellers page, ordinary browser after direct fetch failed. Read for description, current/prior-year taxable thresholds, registration and SST references. | https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/remote-sellers/ | 2026-11-13 |
| DFA sales/use FAQ, ordinary browser. Read for complete FAQ on local sourcing, rate lookup, cap/rebates, freight and use-tax reporting. | https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/sales-and-use-tax-faqs/ | 2026-11-13 |
| DFA register for tax account, ordinary browser. Read for complete application requirements, permit fee, processing and ATAP functions. | https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/register-for-a-tax-account/ | 2026-11-13 |
| DFA 2026 due dates, ordinary browser. Read for all monthly report rows and distinction from prepayments. | https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/due-dates/ | 2026-11-13 |
| DFA sales/use forms, ordinary browser. Read for ET-1/ATAP direction and published SST exemption certificate. | https://www.dfa.arkansas.gov/office/taxes/excise-tax-administration/sales-use-tax/sales-and-use-tax-forms/ | 2026-11-13 |

Not yet confirmed: current detailed ET-1 box/screen instructions, prepayment qualification/calculation and penalty/interest provisions; current software downloaded electronically, SaaS and blanket professional-service treatment; exact manufacturing-equipment exemption conditions for a specific asset. Legacy maximum combined rate about 11.625% is not confirmed and must not be used for an address. Old 0.125% grocery state rate is superseded, not an unresolved rule. No new ancillary exemption/regime is claimed covered.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ar-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ar-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
