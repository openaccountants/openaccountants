---
name: hi-sales-tax
description: "Compute Hawaii GET on business gross receipts and complementary use tax on imports, including all county surcharges, pass-on gross-up, wholesale classification, economic nexus and G-45/G-49 filing."
version: "2.1"
jurisdiction: US-HI
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: vat-gst
type: computation
---

# Hawaii General Excise Tax and use tax, tax year 2026

> **General reference only.** Built from the official sources identified below. Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply this material to the taxpayer's actual facts and the law for the relevant period, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of any federal tax implications. Federal computations belong to the linked federal Guides.

**Answer first.** Hawaii's business tax is GET, imposed on the seller's gross receipts; it is not a conventional customer sales tax. The general state rate is 4% plus the applicable 0.5% county surcharge. All four counties currently impose that surcharge, including Maui from 2024. Wholesaling generally uses 0.5% and insurance commissions 0.15%, without county surcharge. Use tax tests purchases from unlicensed out-of-state sellers separately. Sources: [DOTAX GET information](https://tax.hawaii.gov/get/); [county surcharge](https://tax.hawaii.gov/geninfo/countysurcharge/).

## Scope

Hawaii businesses with taxable gross receipts, including sole proprietors, corporations, retailers, service providers, landlords, contractors, manufacturers and wholesalers, and persons importing goods, services, intangibles or contracting for use in Hawaii. GET and use tax are separate from net income tax in `hi-income-tax` and `hi-corporate-tax`. The old `hi-sales-tax` slug is retained for existing links. Federal sales-tax concepts are in `us-sales-tax`; federal income computations are in `us-schedule-c-and-se-computation`.

The official 2025 brochures were read for the **2025-2026 filing cycle**; the live DOTAX GET and county pages were also read. No unannounced 2026 change is assumed.

## Ask the client first

1. Each activity, goods or service, exemption claimed and evidence supporting wholesale rather than retail treatment.
2. County of business and delivery/performance, including establishments and customers in multiple counties.
3. Gross receipts before expenses, separately stated GET passed on, refunds and exemption/deduction documentation.
4. Physical presence and Hawaii receipts and transaction counts in both the current and preceding calendar years.
5. Imports, landed costs, intended use, vendor GET licensing and specific sales/use tax paid to another state.
6. GET license, expected annual tax, filing frequency, prior G-45 payments and electronic-filing requirements.

## The method, step by step

### Rates, bands and thresholds

| Item | Amount and conditions | Official source |
|---|---|---|
| General GET | 4% state rate for retail goods, services, rents and other general business receipts before applicable exemption | [GET brochure, rates](https://files.hawaii.gov/tax/legal/brochures/GE_brochure-25.pdf) |
| County surcharge on general-rate activity | 0.5% Honolulu, Kauai, Hawaii and Maui; does not apply to 0.5% or 0.15% activities | [county surcharge](https://tax.hawaii.gov/geninfo/countysurcharge/) |
| General combined rate | 4.5% where county surcharge applies | [GET rates](https://tax.hawaii.gov/get/) |
| Wholesaling and qualifying wholesale services/production | 0.5%; resale is not a blanket zero-rate exemption | [GET rates and activity types](https://tax.hawaii.gov/get/) |
| Insurance commissions | 0.15% | [GET rates](https://tax.hawaii.gov/get/) |
| Maximum visibly passed-on general GET plus surcharge | 4.7120% of pretax price; passed-on amount itself is taxable gross receipts | [Maximum Pass-On Rates](https://tax.hawaii.gov/geninfo/countysurcharge/) |
| Economic nexus for remote business | At least USD 100,000 receipts or at least 200 transactions in current or preceding calendar year | [Economic Nexus Threshold](https://tax.hawaii.gov/get/) |
| GET license application | One-time USD 20, Form BB-1 | [How to Register](https://tax.hawaii.gov/get/) |
| Use tax, imports for retail resale/lease | 0.5% landed value where qualifying goods remain perceptible or services are identifiable elements, not overhead | [Use tax brochure, questions 11 to 16](https://files.hawaii.gov/tax/legal/brochures/Use_brochure-25.pdf) |
| Use tax, qualifying wholesale resale | 0%; keep classification evidence and comply with reporting/deduction method | [Use tax brochure, question 11 and Appendix II](https://files.hawaii.gov/tax/legal/brochures/Use_brochure-25.pdf) |
| Use tax, personal/business consumption or overhead | 4% plus applicable 0.5% surcharge, generally 4.5% | [Use tax brochure, questions 11 and 16](https://files.hawaii.gov/tax/legal/brochures/Use_brochure-25.pdf) |
| Periodic filing exception | Total annual liability no more than USD 100: no G-45 required; G-49 remains required | [GET brochure, question 35](https://files.hawaii.gov/tax/legal/brochures/GE_brochure-25.pdf) |
| Semiannual periodic return | Annual GET including surcharge no more than USD 2,000, subject to USD 100 exception | [GET brochure, question 35](https://files.hawaii.gov/tax/legal/brochures/GE_brochure-25.pdf) |
| Quarterly periodic return | Annual GET including surcharge over USD 2,000 and no more than USD 4,000 | [GET brochure, question 35](https://files.hawaii.gov/tax/legal/brochures/GE_brochure-25.pdf) |
| Monthly periodic return | Annual GET including surcharge over USD 4,000; e-file unless waiver | [GET brochure, question 35](https://files.hawaii.gov/tax/legal/brochures/GE_brochure-25.pdf) |

1. Test nexus. Local business, employees, inventory, representatives or in-state services may establish physical nexus independently of the remote thresholds. Count both receipts and transactions for economic nexus; the old Guide omitted the transaction limb. Apply for a GET account through **Hawaii Tax Online**, https://hitax.hawaii.gov/, using BB-1, and save the license/account number. Display the license; use G-50 for additional branches. Source: [registration and nexus](https://tax.hawaii.gov/get/).
2. Classify gross receipts by actual business activity. Start before business expenses; separate wholesale/manufacturing, retail/service/rent, insurance and use-tax imports. GET cascades: qualifying manufacturer/wholesaler receipts can bear the lower rate and the retail sale bears general GET. It is not a conventional resale-certificate exemption. Obtain the appropriate resale evidence. Source: [GET brochure, rates and business activities](https://files.hawaii.gov/tax/legal/brochures/GE_brochure-25.pdf).
3. Include any passed-on GET in taxable receipts. If a business wants to recover its general 4.5% liability in full, the exact gross-up is `pretax price / (1 - 0.045) - pretax price`; the visibly passed-on rate must stay within DOTAX's published maximum. With no surcharge, the analogous 4% gross-up is approximately 4.1667%; that is not the current four-county general pass-on rate. Source: [Maximum Pass-On Rates](https://tax.hawaii.gov/geninfo/countysurcharge/).
4. Apply sourced exemptions/deductions with supporting documentation. General retail clothing, groceries and prepared food do not gain an exemption simply because they are necessities. Professional services, SaaS/digital licensing, equipment and other business activities require the applicable exemption test rather than a blanket exempt label. The old assertion that all medical services are invariably taxed must not override specific healthcare exemptions. Source: [What is Taxed and Exemptions](https://tax.hawaii.gov/get/). Unconfirmed product-specific exemptions are listed below.
5. Allocate general-rate income under the county sourcing rules. Multiple counties require G-75 attached to G-45/G-49; do not universally label all transactions destination-sourced. The county page distinguishes income taxed under different chapter 237 provisions. Source: [Sourcing Rules and G-75](https://tax.hawaii.gov/geninfo/countysurcharge/).
6. For imports from unlicensed out-of-state sellers, calculate landed value including freight, handling, insurance and customs costs, excluding another state's sales tax. Test wholesale resale, retail resale/lease or consumption/overhead. The purchase from a licensed seller subject to GET is not also subject to use tax on the same transaction; an importing reseller can nevertheless owe use tax on its import and GET on its later sale. Foreign-country imports are within this test. Source: [Use tax brochure, questions 1 to 16](https://files.hawaii.gov/tax/legal/brochures/Use_brochure-25.pdf).
7. Another-state sales/use tax credit is item-specific, capped by the applicable Hawaii use tax on that item. Do not net credits across unrelated imports. The brochure Appendix III computes the base state-tax credit through the deduction column and separately applies county surcharge to full landed value in its worked example; do not wipe out surcharge without checking the governing credit rules. Source: [Use tax brochure, Appendix III](https://files.hawaii.gov/tax/legal/brochures/Use_brochure-25.pdf).

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Wholesale sale | Qualify the customer/use and evidence; lower GET may apply, not a generic exemption |
| Consumer/nonbusiness occasional import | G-26 instead of GET-business G-45/G-49; due twentieth day of next month |
| Grocery food, clothing or prepared food | Ordinary general-rate receipt absent a specific substantiated exemption |
| Prescription drugs or healthcare services | Verify statutory exemption, seller and reimbursement conditions; old blanket prescription-drug exemption is not approved guidance here |
| SaaS, digital goods and intangible licenses | Identify rights, seller licensing, Hawaii use and any exemption; imported online-use licenses are expressly discussed in use-tax brochure questions 18 to 20 |
| Manufacturing equipment | No automatic exemption from the old label; examine actual use and statutory exemption |
| Multi-county business | Separate county sourcing and G-75; all four county rates are currently 0.5% |
| No income during an otherwise required filing period | File zero return; the annual USD 100 periodic exception must be tested separately |
| Out-of-state imports with mixed wholesale/retail use | Use supported actual-cost or approved deduction method; preserve records under use-tax brochure Appendix II |

## Worked cases

**Case 1, a pricing decision.** Invented Oahu consultant has a USD 10,000 pretax fee with no exemptions. Absorbing GET means USD 450 tax and USD 9,550 retained. Passing on the published 4.7120% maximum adds USD 471.20: gross receipts USD 10,471.20 and GET USD 471.204, or USD 471.20 rounded. Retained revenue is approximately USD 10,000. The pass-on is optional and included in the base.

```oa-check
name: Hawaii GET absorb or pass on decision
inputs:
  price: 10000
steps:
  - absorbed_tax: price * 0.045
  - retained_absorbed: price - absorbed_tax
  - passed_on: price * 0.047120
  - gross: price + passed_on
  - passed_tax: gross * 0.045
  - retained_passed: gross - passed_tax
expected:
  absorbed_tax: 450
  retained_absorbed: 9550
  passed_on: 471.2
  gross: 10471.2
  passed_tax: 471.204
  retained_passed: 9999.996
```

**Case 2: import classification.** Invented Maui retailer imports USD 20,000 landed-value goods from an unlicensed seller: USD 15,000 for documented retail resale and USD 5,000 of office equipment for own use. The resale import bears 0.5%, USD 75; equipment bears 4.5%, USD 225; total use tax USD 300. Taxing the entire import as retail resale would understate tax by USD 200. The later retail sale has its own GET liability.

```oa-check
name: Hawaii use tax retail inventory and business consumption
inputs:
  resale: 15000
  own_use: 5000
steps:
  - inventory_tax: resale * 0.005
  - equipment_tax: own_use * 0.045
  - use_tax: inventory_tax + equipment_tax
  - incorrect_tax: (resale + own_use) * 0.005
  - understatement: use_tax - incorrect_tax
expected:
  inventory_tax: 75
  equipment_tax: 225
  use_tax: 300
  understatement: 200
```

## When to refuse or refer

Refer unsupported wholesale status, healthcare/drug exemptions, exported services, marketplace facilitator allocation, construction deductions, mixed-county sourcing and disputed import credits. Lodging may also trigger separate transient accommodations tax; this Guide does not compute it. Do not treat GET as income tax or assume the seller must collect it from the buyer.

## Filing and payment

In Hawaii Tax Online select the GET/use account, period and **G-45**. Enter gross income/landed value by activity, qualifying exemptions/deductions with Schedule GE codes, taxable balance, rate and county surcharge. Attach **G-75** for multi-county activity. Reconcile gross receipts including passed-on tax, submit, retain the acceptance and pay using the correct account/period. Reconcile annual gross income, exemptions and periodic payments on **G-49**, rather than assuming the periodic returns replace it. Sources: [Filing Requirements](https://tax.hawaii.gov/get/); [GET brochure, questions 33 to 44](https://files.hawaii.gov/tax/legal/brochures/GE_brochure-25.pdf).

G-45 is due the twentieth day of the month after the assigned period; G-49 is due the twentieth day of the fourth month after year end, 20 April 2027 for calendar 2026. Applicable weekend/holiday dates move to the next business day. A nonbusiness importer uses G-26 by the twentieth day of the month after import, without annual or quarterly filing. Filing an annual extension request does not extend tax payment; periodic returns have no filing extension. Sources: [GET brochure, questions 35 to 38](https://files.hawaii.gov/tax/legal/brochures/GE_brochure-25.pdf); [Use tax brochure, question 39](https://files.hawaii.gov/tax/legal/brochures/Use_brochure-25.pdf).

Late filing penalty is 5% per month or part up to 25%. A 20% late-payment penalty may apply to timely-filed return tax unpaid after 60 days. Interest is two-thirds of 1% per month on unpaid tax and penalties. Required e-file/e-pay failures can incur 2%, and incorrect Part V completion can incur 10%. Source: [Penalties and Interest Rates](https://tax.hawaii.gov/get/).

## Completion checklist

- Classifications, exempt deductions and county sourcing supported; transaction-count nexus limb checked.
- Passed-on tax included in receipts and reconciled to invoices.
- Imports reviewed separately from sales, with landed value and correct end use.
- G-45 frequency and USD 100 exception checked, G-49 completed, payments and acknowledgements retained.

## Sources

| Source and scope actually read | URL | Read on |
|---|---|---|
| DOTAX GET information. Read taxable activities, rates, nexus, registration, periodic/annual return and penalties sections. | https://tax.hawaii.gov/get/ | 2026-11-13 |
| DOTAX county surcharge page. Read all four effective dates, lower-rate exclusions, pass-on maximums and sourcing rules. | https://tax.hawaii.gov/geninfo/countysurcharge/ | 2026-11-13 |
| An Introduction to the General Excise Tax, revised May 2025. Read rates, gross income, registration, questions 33 to 44 on returns, frequency, due dates and extensions. 2025-2026 filing cycle. | https://files.hawaii.gov/tax/legal/brochures/GE_brochure-25.pdf | 2026-11-13 |
| An Introduction to the Use Tax, revised April 2025. Read questions 1 to 20 and 39, Appendix II resale methods and Appendix III credit conditions and example. 2025-2026 filing cycle. | https://files.hawaii.gov/tax/legal/brochures/Use_brochure-25.pdf | 2026-11-13 |

Not yet confirmed: 2026-specific revised GET/use brochures and final 2026 form fields; exact current prescription-drug and healthcare exemption conditions, replacing the old unconditional prescription-drug exemption and all-medical-services-taxable assertions; item-specific SaaS/digital-goods exceptions and manufacturing equipment exemptions beyond the general business/import rules. Old unsourced SST-membership claim is not used for filing guidance. The old no-computation instruction conflicted with the required worked-case standard and is superseded by the two recomputing cases here.
