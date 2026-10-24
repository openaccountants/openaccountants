---
name: fo-corporate-income-tax
description: >
  Prepare a 2026 Faroese ordinary corporate income tax computation for P/F and
  Sp/F companies. Check the 18% rate conditions, reconcile accounting profit,
  test carried losses, distinguish group and capital-income regimes, and build
  the filing and payment calendar. Special industries, treaty relief and full
  capital-income calculations remain outside this source-cited draft.
jurisdiction: FO
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.4
verified_by: pending
review_status: pending_review
---

# Faroe Islands corporate income tax v0.4

## Who this applies to

This Guide prepares ordinary income-tax working papers for Faroese P/F and Sp/F companies. Faroese registration brings companies with limited-liability participants within Tax Act §1(1)(8); §1(2) also covers relevant foreign-registered entities whose effective management is in the Faroes. Treaty residence requires separate analysis. [Tax Act][tax]

It does not compute capital-income tax, shareholder distributions, petroleum tax, fishing/resource charges, aquaculture surcharges, tonnage taxation, reorganisations or minimum-tax exposure. Identify those activities before using the ordinary calculation. An 18% result here is not necessarily the company's complete tax liability.

**Period:** income year 2026, sources read 23 October 2026. The Tax Act consolidation identifies amendment 53 of 1 June 2026, effective 1 September 2026. Event-specific rules must be matched to the event date.

## Rates, bands and thresholds

| Item | Rule | Source |
|---|---|---|
| Ordinary qualifying company rate | 18% | Assessment Act §5(2) |
| Capital condition in §5(2) | Relevant share/paid-in/guarantee/cooperative capital at least DKK 50,000 for the specified entities | Same |
| Entrepreneur companies | Separately included in §5(2) | Same |
| Residual rate under §5(1) | 49%; do not apply automatically without checking the exceptions in §5(2)–(4) | Same |
| Petroleum-income exception | 27% for the specified Hydrocarbon Tax Act §4 income; excluded here | §5(4) |

[Assessment Act][rate]. The 18% is the combined national and municipal amount; the 70%/30% allocation divides that tax, not additional tax rates. TAKS also describes the 18% treatment for specified funds and insurers, which this ordinary-company Guide does not analyse. [TAKS company-tax guidance][taks]

## The base

Start with a reconciled trial balance and a separate tax-adjustment schedule. Operating expenditure incurred to earn, secure and maintain income is addressed by Tax Act §31. Tax depreciation is governed separately, so an accounting depreciation charge is not its own tax deduction. Check business interest under §33 and related-party restrictions under §37b before allowing it. [Tax Act][tax]

Working-paper sequence:

1. Identify the entity, period and applicable rate provision.
2. Reconcile revenue, costs and accounting profit to signed accounts and ledgers.
3. Separate ordinary income from capital-income items and special regimes; document the legal classification for each material item.
4. Reverse accounting charges that require separate tax treatment; insert only deductions supported by the applicable law and schedules.
5. Establish the allowable loss balance, then apply it against positive ordinary taxable income. Preserve the unused balance by origin year and entity.
6. Multiply the resulting ordinary taxable income by the established rate. Reconcile the assessment and actual payment notices separately.

### Ordinary business equipment depreciation

For machinery, furniture and similar equipment used exclusively in the business, maintain a tax pool separately from accounting carrying values. Classify assets first: buildings, leased-premises installations, ships, mixed/private-use assets and passenger cars subject to §5a cannot simply be placed in this ordinary equipment calculation. Foreign-managed joint ownership also has §1 restrictions. [Depreciation Act §§1–2, 5a][depreciation]

For an ordinary positive pool, start with the opening tax balance, add qualifying acquisitions and deduct disposal proceeds. The maximum annual deduction is **30%** of that adjusted balance. If the balance before depreciation is **DKK 20,000 or less**, the positive remainder can be deducted in full. The ceiling is not a mandatory deduction. [§2(3)–(5)][depreciation]

Separately, an eligible item costing **DKK 20,000 or less** can be deducted immediately in its acquisition year under §3. Choose either full immediate deduction or inclusion of its entire cost in the pool; do not claim both. Subsequent sale proceeds of an immediately deducted item are fully taxable income, not a second pool reduction. [§3(1)–(4)][depreciation]

A proved disposal loss has special treatment: compare proceeds with that asset's cost less prior tax depreciation. Deduct the loss in the disposal year and remove the asset's remaining tax value from the pool. Do not both remove that tax value and deduct the proceeds again from the pool. Keep asset-level records even though ordinary annual depreciation uses a pool. [§4(1)][depreciation]

If proceeds create a negative pool, stop the positive-pool calculation. Section 5 allows inclusion in taxable income in the current year and requires settlement by the following income year unless offset through qualifying acquisitions or a permitted extension. Record the negative balance and its deadline; it is not a negative depreciation deduction. The full reinvestment/extension procedure remains outside this Guide. [§5][depreciation]

### Passenger cars used exclusively for business

Depreciation Act §5a applies to passenger cars used exclusively for business but registered for private passenger transport when acquisition cost **exceeds DKK 150,000**. Registration class and actual use are separate tests. Do not assume a company-owned car qualifies for ordinary pooling merely because its use is entirely business-related. Exactly DKK 150,000 does not trigger this particular above-threshold exclusion; other classification conditions still apply. [§5a(1)][depreciation]

For an affected car, keep a separate DKK 150,000 depreciable balance. Record the excess purchase cost and improvement expenditure as a separate non-depreciable asset item in the accounts accompanying the return. Apply the compatible Chapter 1 rules to the depreciable portion, including the 30% annual ceiling, without adding this car to the ordinary equipment pool. No depreciation is allowed in its disposal year. [§5a(2)–(4), (6)][depreciation]

On disposal, compare proceeds with full acquisition cost plus improvements less prior depreciation. A positive gain is taxable. A loss is deductible only to the extent it exceeds the amount that §5a(2) excluded from depreciation. This differs from deducting the full accounting loss. Preserve original cost, improvements, prior tax deductions and the excluded balance separately. [§5a(4)][depreciation]

Private or mixed use requires a separate analysis under Chapter 2 and the change-of-use provisions; employee benefits and payroll valuation are also separate. This section does not determine them. [§§5a(5), 7–10, 31][depreciation]

### Business buildings

Classify each building under Depreciation Act §17 before selecting a rate. Category (a) covers exclusive craft/industrial use, including necessary offices/storage; (b) covers exclusive hotel use or rental buildings with at least ten apartments, including necessary offices/storage. Category (c), including other office/storage buildings, requires at least **75%** business floor area. Residential use is excluded except within the express §17(1) exceptions. [§17][depreciation]

| Classification | Acquisition year and next nine income years | Later income years |
|---|---:|---:|
| §17(1)(a) or (b) | Up to 7% of eligible acquisition cost annually | Up to 2% |
| §17(1)(c) | Up to 4% of eligible acquisition cost annually | Up to 1% |

These are cost-based rates, not the equipment pool method. The acquisition-year definition in §20(1) includes acquisition/completion and use for a qualifying purpose. Keep that date and accumulated deductions in the schedule; do not start a new ten-year period merely because this year's return is the first one being prepared. [§20][depreciation]

Exclude land acquisition, site preparation and surrounding-area costs from the depreciable building basis. Where only part qualifies, allocate cost by qualifying floor area under §18; where business uses span the rate classes, apply §20(4)'s area allocation. Test eligibility before allocation: a 74% business-use office building does not meet the 75% test merely by reducing its deduction to 74%. Keep separate schedules for each building and its reconstruction/improvement expenditure. [§§18–22, 27][depreciation]

No annual depreciation is allowed in the disposal or demolition year. Section 24 provides a separate demolition deduction for unrelieved amounts less material-sale proceeds only where ownership and qualifying use lasted at least five years before demolition. Disposal gains, indexation, reinvestment and insurance relief under §§25–26 need separate computations; an accounting disposal loss is not automatically deductible. [§§21, 24–26][depreciation]

### Losses

Section 33a allows forward deduction, using available earlier profits before carrying losses to a later year. Company losses are forfeited under its ownership-continuity rule if at least 50% of capital or voting value is not in the same hands at the beginning of the utilisation year as at the end of the loss year. The statute preserves an exception where the company carried on significant business activity involving economic risk when ownership changed. Do not treat every share sale as automatic forfeiture. [§33a(1)–(2)][tax]

Debt cancellation/reduction also reduces losses; debt-to-equity conversion uses the difference between face and market value, with adjustment for debt-release income taxed. Review the transaction before using the old loss balance. [§33a(3)][tax]

TAKS describes ordinary-income losses as deductible in the capital-income return but not the reverse. Do not combine the two bases into a single net-profit figure. The exact capital-income ordering and computation remain outside this Guide. [TAKS][taks]

### Group taxation

Regulation 148/2015 requires eligible Faroese-registered entities, matching financial years and full subsidiary ownership throughout the subsidiary's income year. Application is written, ordinarily by 1 July following the first relevant year, with returns/accounts submitted before consideration. Companies in liquidation cannot obtain permission; liquidation ends their participation from that income year. Section 4(4) prohibits renewed permission after departure. Treat approval as evidence, not an assumption. [Regulation §§1–5][group]

Each company computes its own result. Pre-group losses first offset its own profit; the regulation prescribes further ordering involving its own capital income and group-period losses before group allocation. Do not transfer an acquired company's pre-group loss directly to its parent. The parent reports the joint result; §9 requires intercompany tax/loss compensation to be paid or booked by 1 October following the income year. [§§6–9][group]

This is a screening summary, not a complete group-loss calculator. Capital-income grouping requires its own authority and review.

## Deadlines and filing

Company returns are ordinarily due **1 July following the income year** under §100(3). For a calendar-year 2026 company, that means 1 July 2027. A permitted extension cannot exceed **15 August** under §105. [Tax Act][tax]

TAKS requires company accounts with the return, including exempt companies; accounts must be submitted on Borgaragluggin. Retrieve the current return and accounting template and retain submission receipts. [TAKS returns][returns]

Ordinary company tax falls due in three payments on **1 October, 1 November and 1 December**, with payment permitted through the **20th** of each month. Use the assessed year and issued amounts; do not substitute the return deadline for the payment calendar. [Tax Act §81][tax]; [TAKS][taks]

New-company first periods and cessation have separate §21 rules. This Guide does not supply an incorporation/closure calendar; resolve it before applying the ordinary-year example.

## Penalties and interest

Section 104 provides estimated assessment for a missing timely complete return, a DKK **1,000–5,000** fine, and income-tax increases of **2%** when less than seven days late or **5%** when seven or more days late. Relief requires a supported application under subsection 3. [Tax Act][tax]

Section 81(2) states ordinary late-payment interest of **0.7% per commenced month**, subject to §146(1). That latter provision addresses specified offence penalties and underpaid tax, with **12% annual interest** for the specified companies. Do not stack or substitute these mechanically. TAKS's short guidance describes the ordinary calculation from the timely-payment date, whereas §81 says the due date; obtain the assessment's calculation if the start-date distinction affects the charge. [Tax Act][tax]; [TAKS][taks]

## Cross-border points

Foreign incorporation does not settle residence where effective management is Faroese. Foreign businesses require a separate domestic-source/PE and treaty analysis under §§1–2. Controlled transactions and thin capitalisation require their own schedules; see the transfer-pricing Guide. Foreign tax credits, participation relief, withholding and treaty procedures are unresolved here. [Tax Act §§1–2, 37a–37b][tax]

## Worked examples that recompute

### 1. Ordinary profit bridge

Assume a qualifying 18% company, no special regime or capital-income items, accounting profit DKK 600,000, accounting depreciation DKK 80,000 and independently verified tax depreciation DKK 100,000. The ordinary base is DKK 580,000 and tax DKK 104,400. The depreciation input is a case assumption, not a rate established by this Guide.

```oa-check
name: Faroese ordinary company profit bridge
inputs:
  profit: 600000
  accounting_depreciation: 80000
  verified_tax_depreciation: 100000
  rate: 0.18
steps:
  taxable: profit + accounting_depreciation - verified_tax_depreciation
  tax: taxable * rate
expected:
  taxable: 580000
  tax: 104400
```

### 2. Loss use and a failed continuity condition

A qualifying company's ordinary profit before loss relief is DKK 300,000, with DKK 500,000 verified carried losses. If the losses survive §33a and no other adjustment applies, DKK 300,000 is used, ordinary tax is zero and DKK 200,000 remains. If ownership continuity fails and the significant-business exception does not apply, assume the whole DKK 500,000 is forfeited: tax is DKK 54,000 and no such loss remains. This is a conditional comparison, not a factual finding about a share transfer.

```oa-check
name: Faroese loss eligibility changes the result
inputs:
  profit: 300000
  eligible_loss: 500000
  rate: 0.18
steps:
  used: min(profit, eligible_loss)
  taxable: max(0, profit - used)
  tax: taxable * rate
  remaining: eligible_loss - used
  tax_if_forfeited: profit * rate
expected:
  used: 300000
  taxable: 0
  tax: 0
  remaining: 200000
  tax_if_forfeited: 54000
```

### 3. Equipment pool and immediate deduction

Assume all assets qualify for ordinary exclusive-business treatment. An opening pool of DKK 200,000 plus DKK 100,000 of eligible acquisitions gives DKK 300,000. Electing the maximum deduction gives DKK 90,000 and a closing pool of DKK 210,000. A separate eligible item costing exactly DKK 20,000 is immediately deducted and excluded from that pool. There are no disposals or other adjustments.

```oa-check
name: Faroese equipment pool and separate small item
inputs:
  opening_pool: 200000
  pooled_additions: 100000
  small_item: 20000
  rate: 0.30
steps:
  pool_before: opening_pool + pooled_additions
  pool_deduction: pool_before * rate
  closing_pool: pool_before - pool_deduction
  total_deduction: pool_deduction + small_item
expected:
  pool_before: 300000
  pool_deduction: 90000
  closing_pool: 210000
  total_deduction: 110000
```

### 4. Proved disposal loss

Assume a DKK 200,000 opening pool includes an asset with DKK 60,000 remaining tax value, sold for DKK 40,000. Its proved loss is DKK 20,000. Remove DKK 60,000 from the pool, leaving DKK 140,000 before depreciation. At the elected 30% maximum, depreciation is DKK 42,000 and the closing pool DKK 98,000. Total deduction is DKK 62,000. Do not deduct the sale proceeds from the pool again.

```oa-check
name: Faroese equipment disposal loss without double reduction
inputs:
  opening_pool: 200000
  asset_tax_value: 60000
  proceeds: 40000
  rate: 0.30
steps:
  disposal_loss: asset_tax_value - proceeds
  pool_before: opening_pool - asset_tax_value
  depreciation: pool_before * rate
  closing_pool: pool_before - depreciation
  total_deduction: disposal_loss + depreciation
expected:
  disposal_loss: 20000
  pool_before: 140000
  depreciation: 42000
  closing_pool: 98000
  total_deduction: 62000
```

### 5. Building eligibility at the floor-area boundary

Assume a §17(1)(c) office building in its first ten-year period, DKK 4 million eligible building cost after excluding land/site costs, and 1,000 square metres total floor area. At 750 square metres of qualifying business use, the 75% eligibility test is met, allocated basis is DKK 3 million and the maximum annual deduction is DKK 120,000. At 740 square metres, category (c) fails. Assume no other qualifying category, relief or exceptional facts.

```oa-check
name: Faroese building floor-area boundary
inputs:
  building_cost: 4000000
  total_area: 1000
  eligible_area: 750
  below_area: 740
  threshold: 0.75
  rate: 0.04
steps:
  eligible_share: eligible_area / total_area
  boundary_margin: eligible_share - threshold
  basis: building_cost * eligible_share
  deduction: basis * rate
  below_margin: below_area / total_area - threshold
expected:
  eligible_share: 0.75
  boundary_margin: 0
  basis: 3000000
  deduction: 120000
  below_margin: -0.01
```

### 6. Demolition deduction is separate from annual depreciation

Assume a qualifying building is demolished after six years of continuous ownership and qualifying use. Verified unrelieved cost is DKK 600,000 and material-sale proceeds DKK 40,000. The separate §24 deduction is DKK 560,000; no ordinary annual depreciation is added in the demolition year. With only four years of ownership/use, the five-year condition would fail.

```oa-check
name: Faroese separate demolition deduction
inputs:
  unrelieved_cost: 600000
  material_proceeds: 40000
  years: 6
  minimum_years: 5
  short_ownership: 4
steps:
  deduction: unrelieved_cost - material_proceeds
  qualifying_margin: years - minimum_years
  failing_margin: short_ownership - minimum_years
expected:
  deduction: 560000
  qualifying_margin: 1
  failing_margin: -1
```

### 7. Passenger-car cost cap

Assume an exclusively business-used passenger car registered for private passenger transport, purchased for DKK 250,000, with no improvements or disposal in the year. The separately depreciable portion is DKK 150,000 and the excluded cost DKK 100,000. Electing the 30% maximum gives DKK 45,000 depreciation and a DKK 105,000 closing depreciable balance. Depreciating the full purchase price would overstate the deduction by DKK 30,000.

```oa-check
name: Faroese passenger-car separate cost cap
inputs:
  cost: 250000
  cap: 150000
  rate: 0.30
steps:
  excluded_cost: cost - cap
  depreciation: cap * rate
  closing_balance: cap - depreciation
  overstatement: cost * rate - depreciation
expected:
  excluded_cost: 100000
  depreciation: 45000
  closing_balance: 105000
  overstatement: 30000
```

### 8. Passenger-car disposal loss restriction

Assume that same car is sold in the following year for DKK 80,000, with DKK 45,000 prior tax depreciation and no improvements. Full cost less prior depreciation is DKK 205,000, giving a DKK 125,000 loss before the restriction. Subtract the DKK 100,000 non-depreciable amount: only DKK 25,000 is deductible. No annual depreciation is added in the disposal year.

```oa-check
name: Faroese passenger-car restricted disposal loss
inputs:
  full_cost: 250000
  prior_depreciation: 45000
  excluded_cost: 100000
  proceeds: 80000
steps:
  adjusted_full_cost: full_cost - prior_depreciation
  loss_before_restriction: adjusted_full_cost - proceeds
  deductible_loss: max(0, loss_before_restriction - excluded_cost)
expected:
  adjusted_full_cost: 205000
  loss_before_restriction: 125000
  deductible_loss: 25000
```

## Ask the client first

- What are the legal form, relevant capital, registration and actual management location?
- What are the financial year and incorporation/closure dates?
- Which items involve capital income, special industries or foreign operations?
- What are the loss-year balances, ownership histories and debt restructurings?
- Is group taxation approved, and were all ownership and period conditions met?
- What returns, assessments, extension decisions and payment notices have been received?

## Review limits

Source-cited draft, not professional attestation. Building disposal/indexation and special reliefs, ship and mixed-use depreciation, vehicle change-of-use and benefit treatment, capital-income computation/grouping, shareholder distributions, special industries, minimum-tax applicability and treaty relief remain open. Neither the examples nor this file establish comprehensive corporate or country coverage.

## Sources

All read 23 October 2026.

| Source | Locator |
|---|---|
| Consolidated Tax Act | [§§1–2, 21, 31, 33a, 37a–b, 81, 100, 104–105, 146][tax] |
| Assessment Act | [§5][rate] |
| TAKS company tax | [Rates, losses and payment guidance][taks] |
| Group taxation regulation 148/2015 | [§§1–9][group] |
| Current Depreciation Act | [§§1–5a, 7–10, 17–27 and 31, equipment and building computations][depreciation] |
| TAKS returns | [Company filing procedure][returns] |

[tax]: https://www.logir.fo/Logtingslogarkunngerd/109-fra-19-09-2023-um-landsskatt-og-kommunuskatt
[rate]: https://logir.fo/Logtingslog/87-fra-01-09-1983-um-aseting-av-skatti-sum-seinast-broytt-vid-logtingslog-nr-170
[taks]: https://www.taks.fo/fo/vinna/skattur/partafelagsskattur
[group]: https://logir.fo/Kunngerd/148-fra-18-12-2015-um-samskatting-av-felogum
[returns]: https://www.taks.fo/en/individuals/tax/tax-return

[depreciation]: https://logir.fo/Logtingslog/52-fra-29-12-1971-um-skattligar-avskrivingar-vm-sum-seinast-broytt-vid-logtingslog-nr-174
