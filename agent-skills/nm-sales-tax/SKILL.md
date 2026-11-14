---
name: nm-sales-tax
description: "New Mexico GRT and compensating use tax: seller liability, state and local rate lookup by place and period, economic nexus, deductions and NTTC evidence, gross-up, TRD-41413 and TRD-41412 filing."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/nm-sales-tax"
  jurisdiction: "US-NM"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# New Mexico gross receipts and compensating tax, tax year 2026

> **General reference only.** Built from the official sources identified below. Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply this material to the taxpayer's actual facts and the law for the relevant period, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of any federal tax implications. Federal computations belong to the linked federal skills.

**Answer first.** New Mexico imposes **Gross Receipts Tax (GRT)** on the business, with broad coverage of property, services and licenses. This is the state's sales-tax job, but it is not conventional tax imposed on the customer. The verified state component is 4.875%; local additions and special sourcing require the exact reporting-location code and effective-period rate. Complementary **compensating tax** applies to qualifying use of property, services, licenses or franchises. Sources: [FYI-105, GRT and compensating tax overview](https://realfile.tax.newmexico.gov/FYI-105.pdf); [TRD-41413 instructions](https://realfile.tax.newmexico.gov/trd-41413ins.pdf).

## Scope

New Mexico businesses, remote businesses with state nexus and persons with taxable in-state use. Retains the existing `nm-sales-tax` slug while covering GRT and compensating tax. Net-income taxes belong to `nm-income-tax` and `nm-corporate-tax`; employee taxes to `nm-payroll`. Federal sales-tax concepts route to `us-sales-tax`.

FYI-105 explicitly covers **1 July 2025 to 30 June 2026**, the **2025-2026 filing cycle**. Its deductions and figures are limited to that verified period unless separately confirmed. The final July-December 2026 locality-rate schedule was not fetched; do not reuse a first-half local rate blindly.

## Ask the client first

1. Physical presence, activities and New Mexico-sourced taxable receipts in the preceding calendar year.
2. Customer delivery/performance/use address, seller locations, transaction dates and applicable special-location sourcing.
3. Goods, services, licenses, food, medical or manufacturing transactions and exemption/deduction eligibility.
4. Gross receipts, separately stated GRT, returns, bad debts and valid NTTC or alternative evidence.
5. Out-of-state purchases, import/use date, taxable value, seller's NM tax treatment and other-state tax paid.
6. NMBTIN, assigned filing frequency, tax periods, prior returns/payments and electronic-filing obligations.

## The method, step by step

### Rates, bands and thresholds

| Item | Rate, amount and conditions | Official source |
|---|---|---|
| State GRT component | 4.875%, plus applicable locality rate; FYI-105 period 1 July 2025 to 30 June 2026 | [FYI-105, rate and period](https://realfile.tax.newmexico.gov/FYI-105.pdf) |
| Combined GRT/compensating tax | Use reporting location's official rate for the actual period; state component alone is not generally the final rate | [Location Code and Tax Rate](https://realfile.tax.newmexico.gov/trd-41413ins.pdf) |
| Remote economic nexus | At least USD 100,000 taxable gross receipts sourced to New Mexico in preceding calendar year; physical presence is separate | [Who Must File](https://realfile.tax.newmexico.gov/trd-41413ins.pdf) |
| Return/payment due date | Twenty-fifth day of month following assigned reporting period, adjusted for applicable nonbusiness days | [General instructions and filing periods](https://realfile.tax.newmexico.gov/trd-41413ins.pdf) |
| Compensating tax | Location/use-based rate under the official rate schedule, not a single statewide use-tax rate | [Gross Receipts and Compensating Tax Rate Table](https://realfile.tax.newmexico.gov/trd-41412ins.pdf) |
| Late return/payment penalty | 2% per month or part, maximum 20%, minimum USD 5 under the applicable instructions | [Interest and Penalties](https://realfile.tax.newmexico.gov/trd-41413ins.pdf) |

1. Establish nexus and register through **Taxpayer Access Point (TAP)**, https://tap.state.nm.us. Retain the **New Mexico Business Tax Identification Number (NMBTIN)**. A remote seller/marketplace provider meets the statutory business test at USD 100,000 preceding-year taxable NM receipts; do not substitute current-year revenue or count only goods. Physical activities can create nexus independently. Source: [Who Must File and NMBTIN](https://realfile.tax.newmexico.gov/trd-41413ins.pdf).
2. Identify gross receipts by business activity and reporting location before deducting anything. The base generally includes money/value from selling property, licensing/leasing property, franchises and taxable services. GRT is paid by the business; invoice tax treatment does not change nexus. Effective from 2019, billing must separately state GRT or state that the charge includes tax under FYI-105. Source: [Gross Receipts Tax and billing rules](https://realfile.tax.newmexico.gov/FYI-105.pdf).
3. Distinguish **exempt** receipts from **deductible** receipts. Exemption generally excludes the receipt from reporting; a deduction generally requires gross reporting and a supported deduction/code. Keep a valid **Nontaxable Transaction Certificate (NTTC)** or other permitted evidence for the particular statute. A customer's resale purpose does not automatically exempt every service. Sources: [Exemptions, Deductions and NTTCs](https://realfile.tax.newmexico.gov/FYI-105.pdf); [deduction code and column instructions](https://realfile.tax.newmexico.gov/trd-41413ins.pdf).
4. Classify recurring patterns using the boundary table below. Ordinary goods, clothing, prepared food and professional services remain taxable unless a specific exemption/deduction applies. SaaS/digital transactions may involve a license, service or property: identify the rights and sourcing rather than assuming a blanket exclusion. Source: [Gross Receipts Tax scope and deductions](https://realfile.tax.newmexico.gov/FYI-105.pdf).
5. Source each taxable receipt. TRD-41413 instructions distinguish real-property situs, receipt at seller premises, delivery instructions, ordinary business customer address and other fallbacks for property, with separate rules for services. Do not flatten all transactions to destination sourcing. Obtain the actual location code and rate from the [official GRT location/rate map](https://www.tax.newmexico.gov/governments/gross-receipts-location-code-and-tax-rate-map/) for the actual period. Save the lookup evidence with the return. Source: [Location Code and Tax Rate, NMSA 7-1-14](https://realfile.tax.newmexico.gov/trd-41413ins.pdf).
6. Compute taxable receipts after supported deductions and apply the verified full location rate. When a fixed total charge includes separately identifiable GRT, the net receipt is `total / (1 + rate)` and tax is total less net; do not multiply tax-inclusive receipts by the rate a second time. Where price excludes tax, add `net price * rate`. Reconcile invoice treatment and the instructions' definition of gross receipts. Source: [GRT base, excluded GRT and billing rules](https://realfile.tax.newmexico.gov/FYI-105.pdf).
7. Independently test purchases used in NM from an out-of-state person whose transaction would have borne GRT if the seller had nexus, and a manufacturer's own-use withdrawals. Compensating tax reaches tangible property, services, licenses and franchises under the conditions in NMSA 7-9-7. Apply the location/use rule and supported exemptions; mere interstate origin does not establish exemption. Source: [General information and use definitions](https://realfile.tax.newmexico.gov/trd-41412ins.pdf).

## Boundary and exception table

| Pattern | Verified 2025-2026 filing-cycle treatment and evidence |
|---|---|
| General tangible goods or clothing | Taxable unless a specific provision applies; no generic clothing exemption |
| Grocery food | Qualifying food sold by a qualifying retail food store has NMSA 7-9-92 deduction; alcohol, tobacco and prepared hot food for immediate consumption do not qualify; special reporting required |
| Prepared food | Do not apply grocery deduction automatically; prepared hot food for immediate consumption is excluded |
| Ordinary professional services | Broad GRT coverage, subject to actual statutory deductions and sourcing |
| Resale property/licenses | NMSA 7-9-47/73 and required evidence, not an unconditional exemption |
| Services for resale | NMSA 7-9-48 conditions and NTTC/evidence; not all business-to-business services qualify |
| Prescription drugs | Specific deduction under NMSA 7-9-73.2; classify as deduction, not blanket exemption |
| Healthcare | Practitioner, payer and service-specific deductions, including Medicare provisions; not every healthcare receipt is deductible |
| Manufacturing | Separate materials/property/service provisions and evidence; old blanket manufacturing-equipment deduction needs confirmation |
| SaaS/digital goods | Identify property/license/service, use and applicable resale or other deduction; old blanket classification not a substitute for the transaction analysis |
| Marketplace sale | Seller deduction depends on marketplace provider collecting/remitting the associated tax; retain documentation |

Sources for the table: [FYI-105, deductions including food, healthcare, prescription drugs, resale and marketplace receipts](https://realfile.tax.newmexico.gov/FYI-105.pdf).

## Worked cases

**Case 1: tax-exclusive versus tax-inclusive price.** Invented transaction dated in the verified first half of 2026. This example computes the **state component only**, 4.875%, to show the arithmetic; the final return must use the full actual local rate. A USD 10,000 tax-exclusive base gives USD 487.50 state component and USD 10,487.50 total. If that total already includes the component, divide by 1.04875 to recover USD 10,000, not USD 10,487.50 taxable net receipt.

```oa-check
name: New Mexico GRT state component tax exclusive versus inclusive
inputs:
  net: 10000
  state_rate: 0.04875
steps:
  - state_tax: net * state_rate
  - total: net + state_tax
  - net_from_total: total / (1 + state_rate)
  - tax_from_total: total - net_from_total
expected:
  state_tax: 487.5
  total: 10487.5
  net_from_total: 10000
  tax_from_total: 487.5
```

**Case 2: deduction decision.** Invented qualifying retail food store in the verified first half of 2026 has USD 20,000 receipts: USD 15,000 substantiated qualifying grocery food and USD 5,000 prepared hot food for immediate consumption. The grocery deduction leaves USD 5,000 taxable. State component is USD 243.75, versus USD 975 if all receipts were taxed, or zero if the entire food category were incorrectly deducted. Final tax must include the correct local component and reporting code.

```oa-check
name: New Mexico qualifying food deduction versus hot prepared food
inputs:
  receipts: 20000
  qualifying_food: 15000
steps:
  - taxable: receipts - qualifying_food
  - state_component: taxable * 0.04875
  - no_deduction_component: receipts * 0.04875
  - deduction_effect: no_deduction_component - state_component
expected:
  taxable: 5000
  state_component: 243.75
  no_deduction_component: 975
  deduction_effect: 731.25
```

## When to refuse or refer

Refer unsupported NTTCs, mixed healthcare reimbursement, manufacturing equipment, software characterization, tribal transactions, construction/location disputes and compensating-tax credits. Oil/gas, cannabis and insurance premium taxes are separate jobs, as is county property tax. Do not compute final tax without verified full location and period rate, including the July 2026 rate period.

## Filing and payment

In TAP select gross receipts, tax period and **TRD-41413**. Enter location code, gross receipts, supported deductions and special deduction code, taxable receipts and the rate/tax for each reporting location; reconcile totals and credits, submit, save acceptance and pay the correct account/period. Source: [TRD-41413 column and line instructions](https://realfile.tax.newmexico.gov/trd-41413ins.pdf).

Compensating tax uses the separate **TRD-41412** account/return: identify use location, taxable value and deductions, use the location's compensating rate, apply supported credits and reconcile payment. Both returns are due the twenty-fifth of the next month after the assigned period, with applicable weekend/state/federal holiday relief. Filing frequency is assigned by TRD; retain the registration notice and file required zero returns until properly closed. Source: [TRD-41412 filing and line instructions](https://realfile.tax.newmexico.gov/trd-41412ins.pdf); [filing period and due-date instructions](https://realfile.tax.newmexico.gov/trd-41413ins.pdf).

Penalty is generally 2% per month or part, maximum 20%, minimum USD 5. Interest accrues daily at the applicable published variable rate; no assumed annual 2026 rate is supplied. Retain payment confirmation separately from return acceptance. Source: [Interest and Penalties](https://realfile.tax.newmexico.gov/trd-41413ins.pdf); [Interest and Penalties](https://realfile.tax.newmexico.gov/trd-41412ins.pdf).

## Completion checklist

- Physical/economic nexus, legal activity and NMBTIN documented.
- Every exemption/deduction supported and reported with correct code; no deduction described as a blanket exemption.
- Location, period and complete rate evidence retained; midyear rates not rolled forward blindly.
- Compensating purchases checked separately; return and payment acknowledgements reconciled.

## Sources

| Source and scope actually read | URL | Read on |
|---|---|---|
| FYI-105 revised August 11, 2025, expressly July 2025-June 2026. Read GRT base/billing/rates/sourcing, exemptions, NTTCs, food/resale/healthcare/drug/manufacturing deductions and compensating-tax overview. 2025-2026 filing cycle. | https://realfile.tax.newmexico.gov/FYI-105.pdf | 2026-11-13 |
| TRD-41413 instructions. Read who must file, preceding-year USD 100,000 nexus, location/sourcing, form columns, deductions, filing frequency, due dates and penalties. | https://realfile.tax.newmexico.gov/trd-41413ins.pdf | 2026-11-13 |
| TRD-41412 instructions revised August 11, 2025. Read use scope, rate/location table, forms, filing and payment, line instructions, interest and penalties. 2025-2026 filing cycle. | https://realfile.tax.newmexico.gov/trd-41412ins.pdf | 2026-11-13 |

Not yet confirmed: exact July-December 2026 GRT/locality and compensating rate schedule and revised FYI-105 for that period; current transaction-specific manufacturing-equipment and SaaS/digital exceptions; compensating credit conditions for another jurisdiction's tax; old SST membership claim; unsupported old local add-on/maximum ranges of approximately 4.1875%/9.3125% and the income skill's approximately 5.0%-9.4375% range. The old 5.125% state rate is replaced with verified 4.875% for the stated period. The old no-computation prohibition conflicts with required worked examples and is superseded.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `nm-sales-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/nm-sales-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
