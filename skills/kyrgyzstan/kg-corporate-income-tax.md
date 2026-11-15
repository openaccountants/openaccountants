---
name: kg-corporate-income-tax
description: "Kyrgyzstan 2026 ordinary profit tax for domestic companies and foreign permanent establishments, deductible expenses, losses, HTP and investment boundaries, withholding and instalments."
jurisdiction: KG
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
tax_year: 2026
last_updated: 2026-11-15
version: 0.1
type: computation
category: international
---

# Kyrgyzstan corporate profit tax (2026)

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

Calculate ordinary profit tax on the statutory profit base, and classify HTP, investment and non-resident payments separately before selecting a rate.

## Who this applies to

Domestic organisations and foreign organisations with a Kyrgyz permanent establishment (PE) under arts207-210. Domestic organisations generally include Kyrgyz and foreign-source income; a foreign PE is taxed on Kyrgyz-source income under arts209,247. Individual entrepreneurs can also be profit-tax taxpayers, but this file's examples concern companies. Foreign organisations without a PE have a gross-income withholding system, not the ordinary net-profit computation.

## Rates, bands and thresholds

| Item | Amount and conditions | Official source |
|---|---|---|
| Ordinary company and foreign PE profit tax | 10% of taxable profit unless an express exemption/special rate applies, arts210,240(1),247 | https://cbd.minjust.gov.kg/112340/edition/latest/ru |
| Loss carry-forward | 5 calendar years following the loss year, oldest first, art232; no losses from exempt periods; reorganisation succession is conditional | https://cbd.minjust.gov.kg/112340/edition/latest/ru |
| HTP qualifying activity | Profit-tax exemption for a properly registered qualifying resident, arts432-435, not an approximate turnover-based corporate tax | https://cbd.minjust.gov.kg/112340/edition/latest/ru |
| Qualifying preferential-area activity | 0% under art240(3) only for the art183(1) listed activity and territorial registration/activity conditions; mining/processing and excisable production exclusions apply | https://cbd.minjust.gov.kg/112340/edition/latest/ru |
| Large-investment manufacturing profit | 0% under art240(4), subject to all art206(6) conditions and exclusions described below; 5 consecutive periods starting after the first new-equipment-profit period | https://cbd.minjust.gov.kg/112340/edition/latest/ru |
| Ordinary non-PE foreign dividends and interest | 10% of gross taxable Kyrgyz-source income, art249(2)(1); securities-income exclusions, art249(2-1) and treaty conditions require separate checking | https://cbd.minjust.gov.kg/112340/edition/latest/ru |
| Ordinary non-PE foreign royalties and Kyrgyz-performed services | 10% of gross taxable Kyrgyz-source income, art249(2)(3)-(4); ordinary consulting/management fees are not a generic 15% category | https://cbd.minjust.gov.kg/112340/edition/latest/ru |
| Specified international transport/telecommunications and insurance | 5% under art249(2)(2)(a),(5); same-country transport points and compulsory insurance are excluded from this category and need the correct art249 classification | https://cbd.minjust.gov.kg/112340/edition/latest/ru |

## The base

Start from annual income, remove non-chargeable/exempt income, then deduct permitted income-producing expenses under arts210,217. Maintain documents and match the correct period; do not deduct the same expense twice. Apply art236 exclusions, including capital costs handled through allowances, fines/interest payable to the budget, tax itself, non-business/private expenses, entertainment and unsupported purchases. Domestic purchases generally need an electronic invoice unless a statutory replacement-document exception applies; specified patent, special-trade-zone and low-rate unified-tax purchases have separate restrictions. A documented receipt alone does not prove deductibility.

Use the calendar year under art211. Apply eligible art232 losses only after reconciling their age, origin and prior utilisation. Do not offset exempt-period losses or assume every successor inherits losses.

The large-investment concession is not a blanket project approval: art206(6) requires own-produced goods using exclusively qualifying new equipment, annual production-sales revenue at least KGS 170000000, PIT paid at least KGS 150000 each month, and paid charter capital at least KGS 10000000. The equipment definition covers qualifying owned/finance-leased imports after, and not used locally before, 1 May 2015 and specified immovable property; excluded modernisation/expansion of the taxpayer's pre-existing complex does not qualify. Import documents are required. Art240(4) excludes trade, excisable production and mineral extraction except its specified processing profits. Each concession year must qualify. Cabinet-listed national/state-significance projects under art183(4)-(5) receive the relief actually granted, not an automatic zero rate.

HTP profit, sales-tax and taxable-supply VAT exemptions attach to qualifying registered activity; other tax obligations remain. Loss of status brings the general rules from that date. Do not replace this with the seed's approximate HTP turnover charge; any directorate contribution is a separate unconfirmed item below. Other art239 exemptions need their own conditions, and exemption does not itself eliminate the annual information return.

## Deadlines and filing

| Obligation | Due and condition | Official source |
|---|---|---|
| Organisation's unified annual declaration | Before 1 April following the calendar tax year, art106(6)(1), subject to the express art106 exemptions; replaces the seed's March date | https://cbd.minjust.gov.kg/112340/edition/latest/ru |
| Final profit tax | By the unified annual declaration deadline, less preliminary tax and eligible foreign-tax credit, arts242,246 | https://cbd.minjust.gov.kg/112340/edition/latest/ru |
| Preliminary profit return and payment | From the second quarter: not later than 20 of the second month after the reporting period; Q1, half-year and first 9 months, art243; ordinary dates 20 May,20 August,20 November are derived | https://cbd.minjust.gov.kg/112340/edition/latest/ru |
| Non-PE foreign-income WHT | Report and remit not later than 20 of the month following payment, art250 | https://cbd.minjust.gov.kg/112340/edition/latest/ru |

Preliminary tax is 10% of cumulative accounting profit, excluding art243(3-1) income, less the previously calculated preliminary amount and the prescribed carried-loss adjustment; only a positive amount is paid. Zero-rate and exempt taxpayers are outside this preliminary obligation. Foreign-branch results of a domestic company enter at year end, not these preliminary periods.

Reconcile the tax computation, losses, preliminary payments and foreign-income schedules before entering the prescribed electronic annual declaration under art100. Keep TIN, addresses, period, tax obligation, filed return/submission evidence and payment evidence. The current live form/box mapping is unconfirmed; do not present these calculations as a filed return. Art18 governs non-working due dates; art102 can extend filing without extending payment.

## Penalties and interest

Art82 ordinary late-payment interest is 0.09% per calendar day from the day after the deadline, capped at 100% of the arrears, with specified exceptions including qualifying deferral, force majeure, bankruptcy and reliance on official explanations. Art243(6) also applies interest to late preliminary tax. Art163 separately addresses non-filing and understatement sanctions; classify the offence rather than applying one universal penalty.

## Cross-border points

Test PE under art28, including its preparatory/auxiliary and independent-agent exclusions, and check treaty priority under art3. For a non-PE recipient, arts248-249 charge the taxable gross payment without expense deductions; gross up if the contract shifts the tax to the payer. A registered PE recipient with the required registration card and tax certificate is treated differently under art248. Do not withhold on every foreign invoice merely because the payee is abroad: first test Kyrgyz source, income class, statutory exemption and the actual treaty. Treaty rates, securities exemptions and foreign credits are not determined by the examples.

## Two worked examples that recompute

Illustrative KGS inputs for an ordinary taxable company, with no exemption, special rate, foreign credit or disputed expense. The deduction and loss inputs are assumed to have passed arts217,232,236. Annual taxable income KGS 12000000 less allowed expenses KGS 8000000 and eligible prior loss KGS 1000000 produces KGS 300000 tax; preliminary payments matching assessed preliminary tax of KGS 200000 leave KGS 100000 payable.

```oa-check
name: Annual ordinary profit and balance after preliminary payments
inputs:
  taxable_income: 12000000
  allowed_expenses: 8000000
  eligible_loss: 1000000
  preliminary_paid: 200000
steps:
  - current_profit: taxable_income - allowed_expenses
  - loss_used: min(current_profit, eligible_loss)
  - taxable_profit: current_profit - loss_used
  - annual_tax: taxable_profit * 0.10
  - balance: max(0, annual_tax - preliminary_paid)
expected:
  taxable_profit: 3000000
  annual_tax: 300000
  balance: 100000
```

At the half-year preliminary calculation, assume art243 accounting profit after exclusions is KGS 3000000, prior calculated preliminary tax is KGS 100000, and unused eligible carried loss for this adjustment is KGS 500000. The positive difference, reduced by 10% of that loss, is KGS 150000. Reconcile loss use across periods to prevent a double claim.

```oa-check
name: Half-year preliminary payment with carried-loss adjustment
inputs:
  cumulative_accounting_profit: 3000000
  previous_preliminary: 100000
  carried_loss_for_adjustment: 500000
steps:
  - cumulative_tax: cumulative_accounting_profit * 0.10
  - period_difference: max(0, cumulative_tax - previous_preliminary)
  - loss_adjustment: carried_loss_for_adjustment * 0.10
  - payable: max(0, period_difference - loss_adjustment)
expected:
  cumulative_tax: 300000
  loss_adjustment: 50000
  payable: 150000
```

## Ask the client first

- Domestic company, foreign PE or foreign recipient without a PE, and relevant treaty.
- Tax year, accounting profit, source of income and excluded/exempt activities.
- Expense invoices/documents, capital expenditure and related-party payments.
- Loss-year schedules, utilisation and any reorganisation.
- HTP or investment status, qualifying activity, dates and supporting decision/equipment evidence.
- Preliminary/WHT payments, foreign tax paid and prior declarations.

## Sources

| Source and scope actually read | URL | Read on |
|---|---|---|
| Tax Code No3, consolidated 6 August 2026. Read for arts3,18,28,53,82,100-102,106,183,206-211,217,232,236,239-243,247-250,432-435: ordinary profit, losses, concessions, withholding and filings | https://cbd.minjust.gov.kg/112340/edition/latest/ru | 2026-11-15 |

Not yet confirmed: current electronic declaration fields and payment references; any HTP directorate turnover contribution (the old approximate corporate-tax figure is withdrawn); project-specific Cabinet relief, treaty/securities relief and foreign-credit eligibility for an actual case; complete specialist mining/excise/investment computations. Art246 is referenced by art242, but its full foreign-credit procedure is not supplied here.
