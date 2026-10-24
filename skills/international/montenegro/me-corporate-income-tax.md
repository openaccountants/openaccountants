---
name: me-corporate-income-tax
description: "Prepare 2026 Montenegro ordinary corporate profit-to-tax workpapers. Reconcile accounting profit, payment-timing differences, disallowed/capped expenditure, current depreciation, tax losses and progressive tax; distinguish return/payment, withholding and TP documentation. Includes three executable ordinary-base, asset/pool and upper-band controls. Use for porez na dobit, PD, OA and tax deductions. Current form attachments/portal, capital integration, specialist sectors/groups/incentives, procedures and independent review remain open. Source-cited preparation draft."
version: 0.2
category: international
jurisdiction: ME
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
sources:
  - url: "https://wapi.gov.me/download/8826962a-3806-4619-afa4-0029b0a57afb?version=1.0"
    title: "Corporate-tax consolidation through 88/24"
    as_of: "2026-10-24"
  - url: "https://wapi.gov.me/download/17fea3fc-8c45-434d-b0a2-9a251c3729da?version=1.0"
    title: "Depreciation rule through 124/24"
    as_of: "2026-10-24"
  - url: "https://wapi.gov.me/download/96c3699a-765d-4d19-b15b-e539e9e17691?version=1.0"
    title: "Corporate-return rule through 20/25"
    as_of: "2026-10-24"
---

# Montenegro corporate income-tax preparation v0.2

## Who this applies to

Prepare the ordinary profit-to-tax workpaper for a Montenegro resident company or an established taxable PE, after determining entity, residence, period and sector. Residents and nonresidents have different scope; the [cross-border Guide](me-cross-border.md) owns residence/PE, withholding and foreign-credit routing. The [transfer-pricing Guide](me-transfer-pricing.md) owns controlled-transaction documentation and pricing adjustments. [Articles 2–7, 29–34b, 38–40][law]

This 2026 source-cited draft replaces the retained 2025 summary preserved at Git checkpoint `447d88aa`. The Ministry consolidation through 88/24, depreciation rule through 124/24 and return rule through 20/25 were read. The 104/26 amendment applies from January 2027 with further accession gates; do not import its future anti-profit-shifting chapter into 2026. Full current forms/portal, capital-gain integration, groups/incentives, sector rules, procedure and independent country/professional review remain open. [Law][law]; [depreciation][dep]; [return rule][return]; [104/26 Articles 15–19][amend]

## Rates, bands and thresholds

| Item | Rule | Source |
| --- | --- | --- |
| Ordinary taxable profit | Progressive 9% through EUR 100,000; next band through 1,500,000 at 12%; higher profit at 15%, with statutory fixed amounts 9,000 / 177,000 | Article 28 |
| Tax depreciable assets | Useful life over one year and value over EUR 300; classification and special rules apply | Article 13; depreciation rule Articles 2–4 |
| Groups I / II / III / IV / V | 2.5% / 10% / 15% / 20% / 30%; group I individual straight-line, II–V declining pools | Article 13; depreciation rule Articles 4–6 |
| Qualifying purpose expenditure | Ordinary Article 14 cap 3.5% of total revenue; national sports federations have a separate 5% rule | Article 14 |
| Representation | Up to 1% of total revenue, business purpose/documentation and non-related recipient conditions | Article 15 |
| Association memberships | Ordinary cap 0.1% of total revenue; amounts fixed by law follow the statutory exception | Article 16 |
| Ordinary business losses | Forward against future profit for no more than five years; separate from capital-loss regime | Article 25 |

Sources: [corporate law][law]; [depreciation rule][dep]. The older official-law PDFs still indexed by search show superseded group rates. Use the operative period's law/rule, not a search-result rate table. Article 28 prints bracket boundary amounts with cent expressions; retain the published wording and current authority rounding/form validation. The whole-euro controls below round tax to two decimals and do not adjudicate disputed fraction-of-cent boundaries.

## The base

### Start from accounts and reconcile every adjustment

Article 7 starts from pre-tax profit under the applicable accounting framework, then statutory adjustments. Tie opening accounts and trial balance to the signed statements, reconcile revenue and each adjustment to evidence, and identify income/expense already reflected in profit. Accounting-policy changes under Article 7(4)–(5) have their own five-period treatment; they are not ordinary current cash deductions. [Articles 7–10][law]

Keep separate schedules for permanent disallowances, payment-timing differences, accounting/tax depreciation, capped expenses, related-party adjustments, business losses, capital transactions, exemptions and credits. Article 9 excludes specified domestic dividend/profit/liquidation receipts where the payer is a taxpayer under this law; do not apply that rule to every foreign dividend. Foreign dividends and credits have separate conditions. [Articles 9, 33–34b][law]

### Expense and payment gates

Article 11 disallows specified nonbusiness/undocumented costs, late tax/contribution interest, fines, political contributions, gifts/free transfers, related-party default interest and other listed items. It also addresses excessive nonresident interest, PE head-office administrative charges and reciprocal-debtor impairment. Classify the actual paragraph and avoid adding the same amount twice under overlapping rules. [Article 11][law]

Article 11a recognises the specified salary, royalty, personal-service/occasional independent-activity and termination-payment costs in the period paid. Track opening unpaid amounts, current accruals and payments by person/type/period. Add back an unpaid current expense already booked; deduct a qualifying prior-period amount on payment only if it was previously added back and is not deducted again through current profit. [Article 11a][law]

Inventory/material cost uses weighted average or FIFO consistently with accounting requirements. A bank payment is not proof that inventory was consumed/sold or that a capital asset is a current expense. [Articles 12–13][law]

### Capped expenditure and receivables

For Article 14 expenditure, retain legal recipient, qualifying purpose, payment/in-kind/service evidence and exclusive use. Apply the ordinary 3.5% rule or the separately applicable national-federation rule; an invoice label alone is insufficient. Donations obtaining the specified innovation-incentive status have an express disallowance in Article 14(5). Do not deduct ordinary gifts under this rule without satisfying its special conditions. [Articles 11, 14][law]

Representation needs business purpose, documentation and a recipient who is not related; cap eligible expenditure at 1% of total revenue. For memberships separate legally fixed dues from ordinary voluntary dues before applying 0.1%. Use the relevant total-revenue denominator and retain its reconciliation; do not silently substitute profit or prior-year turnover. [Articles 15–16][law]

For bad debts/impairment, Article 17 distinguishes write-off, collection-action evidence, age, small-claim litigation-cost exception, impairment and later recoveries. Keep receivable origination, prior income inclusion, due date, accounting treatment, recovery efforts and reciprocal liabilities. The ordinary 365-day write-off conditions and 60-day impairment wording are different gates, not one automatic allowance for every overdue invoice. Sector provisions and full current application remain to be completed. [Articles 11(8), 17–18a][law]

### Depreciation workpaper

Maintain acquisition/available-use evidence, classification, accounting depreciation, statutory tax base, rate, additions/disposals/repairs, tax deduction and closing base. Exclude land/artworks under the rule. Do not assign all intangible or right-of-use assets to a physical-asset pool: Article 13 and rule Article 11 provide specific accounting-amortisation treatment. [Article 13][law]; [rule Articles 2–6, 10–12][dep]

Group I uses each asset's qualifying acquisition/improvement base and 2.5% straight-line rule. Groups II–V start from the prior closing pool, add purchases and subtract disposals, then apply the group's rate. Keep accounting gain/loss and tax-pool consequences separate. Special rules cover exhausted pools, excess sale proceeds and small balances; do not let a negative pool produce negative depreciation. The worked pool below retains assets and stays above the small-balance threshold. [Rule Articles 5–9][dep]

Repairs and improvements need their own Article 10 analysis; do not apply an unsupported current-expense default or add a cost already capitalised twice. Full timing/special disposal/leasing/natural-resource methods remain open. [Rule Articles 10–12][dep]

### Losses and capital transactions

Maintain business-loss origin, original assessed amount, prior use, available balance and expiry; Article 25 limits forward relief to five years and has separate status-change allocation/notification provisions. Do not deduct accounting retained losses as a tax loss without the source return/assessment and utilisation trail. The ordinary example assumes an independently established unexpired balance. [Article 25][law]

Capital transactions require a separate Articles 21–24 schedule. Article 9a removes the accounting capital gain from the ordinary starting base, and Article 18a(3) addresses capital losses; that is not authority to certify every disposal tax-free. Establish market proceeds, sale costs, adjusted acquisition cost, capital-loss offsets and the correct current PD/PG1/PG2 integration before finalising. The current authority attachment/field mapping was not retrieved; the ordinary worked example excludes capital transactions. [Articles 9a, 18a, 21–25][law]; [return rule Article 2][return]

### Apply tax, relief and payments separately

After supported ordinary adjustments and eligible loss use, compute the progressive tax. Maintain incentives/credits separately from deductions and reconcile the final liability to actual tax paid and account balances. The cross-border method provides a bounded first-band foreign-profit credit example; it does not clear all foreign-dividend or multi-band credit cases. [Articles 28, 31–34b, 40][law]

A low-development-area address alone does not establish the Article 31 incentive: activity, new-business, related-founder/state-aid and application conditions apply. The Article 31a application has a distinct 30-day-from-CRPS-registration requirement. Obtain the authority decision and current supporting implementation before reducing the tax. Group consolidation, agricultural/innovation and other incentive methods remain partial; no assumed relief appears in the calculations below. [Articles 31–31f, 35–37][law]

## Deadlines and filing

The ordinary period is the calendar year, with specific commencement/status-change/liquidation cases. Article 40 requires an electronic return and payment within three months after the period ends, accompanied by balance sheet and income statement. Do not use a generic annual March date for a different statutory short period. [Articles 39–40][law]

The Ministry's linked return-rule reproduction through 20/25 names Form PD with PG1 and PG2 and the competent registered-taxpayer/main-business authority. Its one-page PDF was rendered and visually inspected: it contains rule text and non-working “Obrazac PD” links, not the actual completed form/attachments or instructions. No invented box mapping is supplied. Obtain the current attachments/IRMS schema and validate the reconciliation/authorised signature and acceptance before filing. [Return rule Articles 2–3][return]

Withholding at payment and annual withholding reporting are separate routes under the [cross-border method](me-cross-border.md). The TP transition/documentation timetable is separate from the corporate return/payment deadline. Retain computation, signed statements, loss/asset schedules, decisions/credit/payment evidence and accepted submission. [Articles 29, 38c, 40, 44b][law]

## Penalties and corrections

Article 42a lists legal-person fines of EUR 1,000–20,000 for specified calculation, reporting, documentation and return failures; the responsible-person range is 500–2,000. Exact exposure depends on the actual offence and current procedure. Article 42 refers interest, appeals and collection to tax-procedure law. Current amended-return, interest, assessment and appeal methods are not fully developed here; no invented daily rate or appeal deadline is given. [Articles 42–42a][law]

## Worked examples

Hypothetical EUR workpapers. Every deductibility, relief and asset classification assumption needs independent evidence; arithmetic does not establish eligibility, accepted filing or legal completeness.

### 1. Ordinary profit to progressive tax

Pre-tax profit is 150,000 and total revenue 1,000,000. Costs already booked include accounting depreciation 18,000; tax depreciation is separately established at 14,000. Nonbusiness costs 1,000 and fines 500 are disallowed. Specified current unpaid remuneration 10,000 is added back; a qualifying prior-period amount 4,000, previously added back, is now paid. Ordinary qualifying donations 50,000, eligible representation 15,000 and voluntary dues 3,000 meet their non-cap conditions; there are no sports/mandatory-dues exceptions. A supported TP adjustment is 6,000 and unexpired tax loss 20,000 is available. There are no capital transactions, exemptions or credits. [Articles 7, 11–16, 25, 28, 38a][law]

```oa-check
name: Montenegro ordinary accounts to progressive corporate tax
inputs:
  accounting_profit: 150000
  total_revenue: 1000000
  accounting_depreciation: 18000
  tax_depreciation: 14000
  nonbusiness_costs: 1000
  fines: 500
  current_unpaid_remuneration: 10000
  prior_added_back_remuneration_paid: 4000
  qualifying_donations_booked: 50000
  eligible_representation_booked: 15000
  voluntary_dues_booked: 3000
  transfer_pricing_addback: 6000
  eligible_loss_available: 20000
steps:
  - donation_addback: max(0, qualifying_donations_booked - total_revenue * 0.035)
  - representation_addback: max(0, eligible_representation_booked - total_revenue * 0.01)
  - dues_addback: max(0, voluntary_dues_booked - total_revenue * 0.001)
  - adjusted_profit: accounting_profit + accounting_depreciation - tax_depreciation + nonbusiness_costs + fines + current_unpaid_remuneration - prior_added_back_remuneration_paid + donation_addback + representation_addback + dues_addback + transfer_pricing_addback
  - loss_used: min(max(0, adjusted_profit), eligible_loss_available)
  - taxable_profit: max(0, adjusted_profit - loss_used)
  - first_band_tax: min(taxable_profit, 100000) * 0.09
  - second_band_tax: min(max(0, taxable_profit - 100000), 1400000) * 0.12
  - upper_band_tax: max(0, taxable_profit - 1500000) * 0.15
  - corporate_tax: round(first_band_tax + second_band_tax + upper_band_tax, 2)
expected:
  donation_addback: 15000
  representation_addback: 5000
  dues_addback: 2000
  adjusted_profit: 189500
  loss_used: 20000
  taxable_profit: 169500
  corporate_tax: 17340
```

No tax payment is assumed merely because this liability is computed. Reconcile actual payments/credits separately.

### 2. Building and retained IT-equipment pool

A full-year eligible building has qualifying base 400,000, no additions/disposals and group-I rate 2.5%. A separately classified group-V electronic/IT data-processing pool opens at 10,000, adds purchases 3,000 and has disposal proceeds 2,000. Assets remain, there are no repairs/special adjustments and the closing pool exceeds 1,000. Accounting depreciation for both schedules totals 20,000. [Article 13][law]; [rule Articles 4–6, 9][dep]

```oa-check
name: Montenegro building and group V pool depreciation
inputs:
  building_tax_base: 400000
  building_rate: 0.025
  pool_opening: 10000
  pool_purchases: 3000
  pool_disposal_proceeds: 2000
  pool_rate: 0.30
  accounting_depreciation: 20000
steps:
  - building_deduction: building_tax_base * building_rate
  - pool_base: pool_opening + pool_purchases - pool_disposal_proceeds
  - pool_deduction: pool_base * pool_rate
  - pool_closing: pool_base - pool_deduction
  - total_tax_depreciation: building_deduction + pool_deduction
  - net_depreciation_addback: accounting_depreciation - total_tax_depreciation
expected:
  building_deduction: 10000
  pool_base: 11000
  pool_deduction: 3300
  pool_closing: 7700
  total_tax_depreciation: 13300
  net_depreciation_addback: 6700
```

### 3. Adjustment crossing the upper band

Taxable profit before a further supported adjustment is 1,490,000. An additional 30,000 TP adjustment raises it to 1,520,000. No loss, relief or credit applies. Only the part crossing the threshold bears the upper rate; do not charge 15% on the entire adjustment. [Articles 28, 38a][law]

```oa-check
name: Montenegro progressive upper band adjustment
inputs:
  taxable_profit_before: 1490000
  additional_adjustment: 30000
steps:
  - taxable_profit_after: taxable_profit_before + additional_adjustment
  - tax_before: round(min(taxable_profit_before, 100000) * 0.09 + min(max(0, taxable_profit_before - 100000), 1400000) * 0.12 + max(0, taxable_profit_before - 1500000) * 0.15, 2)
  - tax_after: round(min(taxable_profit_after, 100000) * 0.09 + min(max(0, taxable_profit_after - 100000), 1400000) * 0.12 + max(0, taxable_profit_after - 1500000) * 0.15, 2)
  - additional_tax: tax_after - tax_before
expected:
  taxable_profit_after: 1520000
  tax_before: 175800
  tax_after: 180000
  additional_tax: 4200
```

## Review handover

Deliver the accounts/base reconciliation, paid-remuneration register, capped-expense evidence, asset/pool and tax-loss schedules, separate capital/credit/incentive applicability sheets, return/payment evidence and unresolved questions. Complete current PD/PG attachments and portal mapping, capital-gain integration, special disposal/impairment/sector/group/incentive cases, procedure and independent country review. All seven country domains remain partial; no named accountant attestation is claimed.

## Sources

[law]: https://wapi.gov.me/download/8826962a-3806-4619-afa4-0029b0a57afb?version=1.0
[dep]: https://wapi.gov.me/download/17fea3fc-8c45-434d-b0a2-9a251c3729da?version=1.0
[return]: https://wapi.gov.me/download/96c3699a-765d-4d19-b15b-e539e9e17691?version=1.0
[amend]: https://wapi.gov.me/download/8951908b-625c-4219-aefe-0c86501ddaf8?version=1.0

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
