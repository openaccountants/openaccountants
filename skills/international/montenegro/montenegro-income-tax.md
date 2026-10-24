---
name: montenegro-income-tax
description: "Prepare Montenegro 2026 individual income-tax workpapers by income class: principal and supplementary businesses, occasional independent work, property, capital gains, foreign credits, royalties/sport and residual internet/video-game income. Establish residence/source, reconcile business profit and losses, apply category-specific rates/expenses, allocate withholding and advances, and route annual GPP-FL obligations. Includes nine executable controls. Use for porez na dohodak, preduzetnik, capital disposals and GPP-FL. Current form attachments/IRMS, specialist relief, treaties, valuations and procedures remain open. Employment payroll and insurance have separate companion Guides. Source-cited preparation draft awaiting independent and professional review."
version: 0.3
jurisdiction: ME
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
sources:
  - url: "https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0"
    title: "PIT consolidation through 160/25"
    as_of: "2026-10-24"
  - url: "https://wapi.gov.me/download/47bea12c-f250-4cdc-b481-3afc30fba94f?version=1.0"
    title: "Enacted 160/25 PIT amendment applying January 2026"
    as_of: "2026-10-24"
  - url: "https://www.sluzbenilist.me/propisi/394390/download"
    title: "Enacted 70/26 PIT amendment, effective May 2026"
    as_of: "2026-10-24"
  - url: "https://wapi.gov.me/download/afb50b45-7e83-4dac-b69e-2a1e280d3ffc?version=1.0"
    title: "Annual GPP-FL return rule through 103/25, actual attachments omitted"
    as_of: "2026-10-24"
---

# Montenegro individual income-tax preparation v0.3

## Who this applies to

Build a 2026 individual-tax workpaper after establishing residence, source, payer, income category and period. A resident is tested under Article 3's domicile/centre of business and vital interests or more-than-183-days criteria, with its separate posting provision; residence is not determined solely by citizenship, bank location or one immigration document. Residents have worldwide scope; nonresidents have Montenegro-source scope. Actual treaty residence/source/priority needs the relevant treaty and facts. [Articles 2–4, 45][law]

This source-cited draft replaces the retained 2025 secondary-source summary preserved at Git checkpoint `eb255509`. The consolidation through 160/25 is read with the enacted 70/26 amendment, effective 21 May 2026, which changes gambling tax. The September salary proposal specifies January 2027 application and is not applied to 2026. Full current forms/IRMS, treaty/specialist implementation, procedures and independent/named-accountant review remain open. [Law][law]; [160/25 Article 21][amend]; [70/26 Articles 1–3][may]; [Gazette record][mayrecord]; [salary proposal][proposal]

The [payroll Guide](montenegro-payroll.md) owns monthly salary/net/prirez/IOPPD preparation. The [contribution Guide](montenegro-social-contributions.md) owns insurance status, statutory bases, monthly contributions and annual PIO refund. Contributions, local surtax, other levies and VAT are not silently included in the PIT-only examples below. All seven country tax domains remain partial.

## Rates and category boundaries

| Income class | Ordinary PIT treatment | Source |
| --- | --- | --- |
| Employment personal earnings | Monthly marginal 0% through EUR 700, 9% next EUR 300, 15% above EUR 1,000; use payroll Guide | Articles 10(1)(1), 14–15, 46 |
| Principal independent activity | Annual marginal 0% through EUR 8,400, 9% next EUR 3,600, 15% above EUR 12,000 on established taxable profit | Articles 10(1)(2), 16–17 |
| Supplementary entrepreneurship | 15% on established taxable profit; not the principal-business zero band | Articles 10(1)(3), 12(2)(2), 16–17 |
| Occasional independent work | 15% on relevant taxable income; undocumented expenses have statutory 30% standard allowance | Articles 10(1)(3), 16(5), 20(2), 48a |
| Property rental | 15% on qualifying net income; actual documented costs or relevant standard-expense provision | Articles 34–36, 49a |
| Capital income | 15% on gross, no ordinary expense deduction, subject to specific exclusions | Articles 10(1)(3), 37, 50 |
| Capital gains | 15% on established gain after applicable same-period capital losses/exemptions | Articles 37a–37h, 50a |
| Sport, royalties/cultural activity, other receipts, residual internet/video-game income | Ordinary 15% on each category's statutory base; these bases differ | Articles 37i–37r, 50b–50e |
| Gambling covered by 70/26 | 12% under amended Article 10(1)(4) from 21 May 2026; earlier-period law and winning-event base need separate reconciliation | 70/26 Articles 1–3; law Article 37s |

Sources: [PIT law][law]; [May amendment][may]. Do not confuse video-game competition income with gambling or assume every online receipt belongs in the residual internet category. Employment/business/royalty classification takes precedence where applicable under Article 37o. Whole-euro examples use the continuous marginal formula and cents rounding; printed statutory cent boundary expressions and actual electronic rounding remain authority-validation matters.

Article 5 excludes specified receipts and Article 5a exempts specified amounts subject to their conditions; Article 6 addresses specified persons. An inherited asset's initial exclusion does not determine its later disposal gain. Article 10a's separate 80% unexplained-income regime is not an ordinary rate for a classified receipt. Do not treat an unidentified bank credit as an exempt gift or as automatically taxable business revenue. [Articles 5–6, 10a, 37d][law]

## Principal and supplementary business base

Start from accounts profit under Articles 17–20 and reconcile the tax adjustments. Preserve revenue, allowable expense, private/undocumented expenditure, inventory, accounting/tax depreciation, capped expenses, interest, business losses, relief and credit schedules. The business-base exclusion for dividends/profit shares in Article 19 is not a general exemption for an individual's private capital-income receipts under Article 37. [Articles 16–31, 37][law]

Article 21 disallows listed nonbusiness/undocumented costs, late tax/contribution interest, excessive nonresident interest, specified nonresident-head-office payments, distributions, fines/penalties and political contributions. Inventory/materials use weighted average or FIFO as specified. A payment or asset purchase is not automatically a current expense. [Articles 21–22][law]

For PIT depreciable assets the Article 23 value threshold is **over EUR 200**, with life over one year. Do not copy the corporate-tax EUR 300 threshold. Statutory groups I–V carry 2.5/10/15/20/30%; group I individual straight-line, other groups declining-group treatment. Intangible/operating-lease right-of-use accounting amortisation has express provisions. Full current PIT implementing classification, acquisitions/disposals and pool timing remain to be reconciled; the first example assumes an independently established tax-depreciation adjustment. [Article 23][law]

Qualifying purpose expenditure under Article 24 is capped at **3% of total income**, with eligible recipient/exclusive-purpose conditions; do not import the corporate 3.5% cap. Representation is capped at 1%, business-related/documented and non-related recipient; memberships ordinarily 0.1%, with a separate legally fixed amount exception. Bad-debt write-offs require prior income inclusion, book write-off and failed-collection evidence; recoveries return to income. Reserves are disallowed. Related interest has market/actually-paid and foregone-interest adjustment rules. [Articles 24–31][law]

Business losses may be carried against future profit for no more than five years under Article 33. Keep year, origin, prior use and available balance; do not turn a business loss into a deduction from every rental/capital category or carry a capital loss under that rule. The interaction of mixed businesses/status changes with actual forms remains open. [Articles 8, 33, 37h][law]

Principal annual business PIT for nonnegative established base B:

`0.09 × max(min(B, 12000) − 8400, 0) + 0.15 × max(B − 12000, 0)`.

Supplementary business instead follows 15% on its established base. Employment alongside a supplementary business does not create another principal-business allowance. Occasional independent work is a distinct Article 16(5) route; where undocumented costs qualify under Article 20(2), taxable base is 70% of the gross receipt and PIT is 15% of that base. A legal-person/entrepreneur payer withholds at payment under Article 48a; directly received income follows annual filing. Actual registration, substance and payer evidence determine the route. [Articles 10, 12, 16–20, 48a][law]

## Property, capital and disposal schedules

Rental expenses are documented actual costs or, if not documented, the Article 35 standard allowance of 30%. Qualifying tourist accommodation has distinct 50% and 70% standard-expense conditions: paid tourist tax for the former; the specified agency/local-tourism lease and at least 60 occupied days annually for the latter. Establish the exact route/evidence, rather than electing the largest percentage by label. A legal-person/entrepreneur payer withholds on payment under Article 49a; direct receipts follow annual filing. Tourist accommodation licence holders have Article 43(5)'s return duty even without income. VAT, tourist tax and property taxes remain separate. [Articles 34–36, 43(5), 49a][law]

Capital income under Article 37 includes interest, dividends/profit shares, certain owner private use, specified liquidation excess and preferential shares. No ordinary expense deduction is allowed, and there is a specified public-debt-interest exclusion. Keep corporate/private extraction and employment/owner-share treatment separate; do not tax every asset sale as a gross dividend. Payer withholding under Article 50 is a separate payment obligation. [Articles 37, 50][law]

For taxable property disposal, reconcile contract sale price, qualifying documented reconstruction/sale costs, authority market-value adjustment, acquisition/inherited/self-built cost and statutory annual cost indexation. Article 37d's fallback of 80% of sale price applies only where acquisition cost cannot be determined under the preceding routes. It is not an elective cost allowance. No live indexation series or valuation is certified here. [Articles 37a–37d][law]

Company-interest gains use the specific contract/founding-contribution bases and market-value safeguard in Article 37e. Securities use the documented/nominal-value and FIFO rules in Article 37f. Article 37g has specific home exemption requiring the property to have served as the taxpayer’s **only and main residence**, and separate family/partner transfer exemptions; proof is required. Article 37h allows capital losses against capital gains in the same tax period; no five-year capital carryforward is inferred. Article 43(6a) has a books/tax-balance reporting route for recorded gains, so business and private schedules must not report the same disposal twice. [Articles 37e–37h, 43(6a), 50a][law]

## Sport, intellectual property, internet and other receipts

Sport income excludes employment salary. Article 37j permits documented actual expenses, or standard expenses of 30% generally and 90% for the qualifying amateur-sport population. Royalties/cultural receipts have Article 37lj's documented-expense route or standard expenses of 60% for specified fine-art rights, 50% for architecture/planning/landscape rights and 30% for the specified remaining categories. A contract's actual rights and recipient status determine the category. [Articles 37i–37m][law]

Article 37n's other receipts use gross income, with its enumerated populations and exclusions from overlapping categories. Residual internet income has a 15% statutory expense deduction; qualifying video-game competition income has actual documented costs or, if undocumented, 20%. These are expense percentages; the ordinary PIT rate is 15%. Do not subtract both actual and standard expenses or use a residual internet allowance on employment/business income already classified elsewhere. [Articles 37n–37r, 50b–50e][law]

## Foreign income, credits and relief

For an established resident, Article 44 allows a credit for qualifying foreign income tax paid, capped at the Montenegro tax on that foreign income. Retain source/category/year, gross and base, payment proof, treaty entitlement, currency method and credit calculation. Do not credit social contributions, refundable/excess treaty withholding or unproved tax automatically. The actual treaty/protocol/MLI and current certificate procedure require their own reading; no bilateral rate or general unused-credit carryforward is certified here. Avoid claiming the same payment both as a foreign credit and as a domestic advance. [Articles 44–45][law]

The payroll Guide routes foreign salary's five-day self-payment and annual/multiple-employer obligations. Principal/supplementary business, rental and capital income need their own rate/base before computing the foreign cap; a flat 15% cannot be substituted for the progressive principal-business cap. [Articles 10, 43–46][law]

Articles 32–32b contain underdeveloped-area business/employment incentives with registration, sector, application, aid and employment/recapture gates; Article 32c has the historical 2021–2023 scheme. Article 32d addresses research/innovation and acquired digital-nomad status under their separate laws. Do not claim relief from low turnover, remote work or a code appearing on an old form. Full current implementing eligibility/aid/status work is not completed and no incentive is applied in the examples. [Articles 32–32d][law]

## Worked examples

Hypothetical 2026 EUR workpapers, established category/residence and evidence as stated, no local surtax/social contributions/VAT/incentive unless specifically included. These are category calculations, not completed GPP-FL boxes or accepted filings.

### 1. Principal business accounts-to-tax and annual settlement

Total revenue 80,000; accounting profit 25,000 already includes all stated expenses. Add private expenditure 1,200 and established accounting-over-tax depreciation 800. Qualifying-purpose spend 3,000 exceeds the 3% cap by 600; representation 1,000 exceeds 1% by 200; ordinary memberships 120 exceed 0.1% by 40. Established unexpired unused business loss is 3,000; paid PIT advances 1,800. No capital/foreign income or other adjustments. [Articles 17–33, 42, 48][law]

```oa-check
name: Montenegro principal business annual profit and settlement
inputs:
  revenue: 80000
  accounting_profit: 25000
  private_expense: 1200
  depreciation_adjustment: 800
  qualifying_spend: 3000
  representation: 1000
  memberships: 120
  available_loss: 3000
  paid_advances: 1800
steps:
  - purpose_excess: max(qualifying_spend - revenue * 0.03, 0)
  - representation_excess: max(representation - revenue * 0.01, 0)
  - membership_excess: max(memberships - revenue * 0.001, 0)
  - adjusted_profit: accounting_profit + private_expense + depreciation_adjustment + purpose_excess + representation_excess + membership_excess
  - loss_used: min(available_loss, max(adjusted_profit, 0))
  - taxable_business: max(adjusted_profit - loss_used, 0)
  - annual_pit: max(min(taxable_business, 12000) - 8400, 0) * 0.09 + max(taxable_business - 12000, 0) * 0.15
  - settlement_due: annual_pit - paid_advances
expected:
  purpose_excess: 600
  representation_excess: 200
  membership_excess: 40
  adjusted_profit: 27840
  loss_used: 3000
  taxable_business: 24840
  annual_pit: 2250
  settlement_due: 450
```

### 2. Principal versus supplementary business status

Identical independently established taxable profit 10,000, with no credit/relief. Principal business PIT 144; supplementary business PIT 1,500. These are alternative legal classifications, not a taxpayer's free election between rates. [Articles 10, 12, 16–17][law]

```oa-check
name: Montenegro principal versus supplementary income rates
inputs:
  taxable_profit: 10000
steps:
  - principal_pit: max(min(taxable_profit, 12000) - 8400, 0) * 0.09 + max(taxable_profit - 12000, 0) * 0.15
  - supplementary_pit: taxable_profit * 0.15
expected:
  principal_pit: 144
  supplementary_pit: 1500
```

### 3. Occasional independent receipt with withholding

Qualifying occasional independent service gross 2,000, no documented expenses, corporate payer. Standard expenses 600, taxable base 1,400, PIT withheld 210. Gross less PIT 1,790 is **before** any separately applicable PIO or other deduction, not a certified net payment. [Articles 16(5), 20(2), 48a][law]

```oa-check
name: Montenegro occasional independent work withholding
inputs:
  gross_receipt: 2000
steps:
  - standard_expenses: gross_receipt * 0.30
  - taxable_base: gross_receipt - standard_expenses
  - pit_withheld: taxable_base * 0.15
  - receipt_after_pit_only: gross_receipt - pit_withheld
expected:
  standard_expenses: 600
  taxable_base: 1400
  pit_withheld: 210
  receipt_after_pit_only: 1790
```

### 4. Rental standard-expense scenarios

Gross rent 20,000, no documented actual costs. Ordinary 30% route and separately qualifying tourist 50%/70% routes shown as alternative established facts. The 70% case assumes the required agency/local-tourism agreement and at least 60 occupied days; the 50% case assumes tourist tax paid. All other licence/local/VAT and filing obligations are separate. [Articles 35–36, 49a][law]

```oa-check
name: Montenegro rental standard expense alternatives
inputs:
  gross_rent: 20000
steps:
  - ordinary_base: gross_rent * (1 - 0.30)
  - ordinary_pit: ordinary_base * 0.15
  - qualifying_50_base: gross_rent * (1 - 0.50)
  - qualifying_50_pit: qualifying_50_base * 0.15
  - qualifying_70_base: gross_rent * (1 - 0.70)
  - qualifying_70_pit: qualifying_70_base * 0.15
expected:
  ordinary_base: 14000
  ordinary_pit: 2100
  qualifying_50_base: 10000
  qualifying_50_pit: 1500
  qualifying_70_base: 6000
  qualifying_70_pit: 900
```

### 5. Taxable property gain and same-period capital loss

Nonexempt property sale 150,000, permitted documented reconstruction 7,000 and sale costs 3,000, no authority market-price adjustment. Acquisition cost after independently established statutory indexation is 110,000. A separate allowable same-period capital loss of 5,000 is available. No business-book double reporting or exempt main-home/family transfer. Indexation/valuation and actual expense eligibility remain assumptions. [Articles 37a–37d, 37g–37h, 50a][law]

```oa-check
name: Montenegro property gain and current capital loss
inputs:
  sale_price: 150000
  reconstruction: 7000
  sale_costs: 3000
  established_indexed_cost: 110000
  current_capital_loss: 5000
steps:
  - adjusted_sale: sale_price - reconstruction - sale_costs
  - gain: adjusted_sale - established_indexed_cost
  - taxable_capital_gain: max(gain - current_capital_loss, 0)
  - pit: taxable_capital_gain * 0.15
expected:
  adjusted_sale: 140000
  gain: 30000
  taxable_capital_gain: 25000
  pit: 3750
```

### 6. Securities FIFO acquisition lots

Same issuer: buy 100 units at 10, then 100 at 15; sell 150 at 20. Documented prices, no other cost, exemption, market adjustment or losses. FIFO basis 1,750, gain 1,250, PIT 187.50. Remaining lot is 50 at 15. [Articles 37a, 37f, 50a][law]

```oa-check
name: Montenegro securities FIFO gain
inputs:
  first_units: 100
  first_price: 10
  second_units: 100
  second_price: 15
  units_sold: 150
  sale_price_each: 20
steps:
  - first_used: min(first_units, units_sold)
  - second_used: units_sold - first_used
  - proceeds: units_sold * sale_price_each
  - fifo_cost: first_used * first_price + second_used * second_price
  - gain: proceeds - fifo_cost
  - pit: gain * 0.15
  - remaining_second_units: second_units - second_used
expected:
  first_used: 100
  second_used: 50
  proceeds: 3000
  fifo_cost: 1750
  gain: 1250
  pit: 187.50
  remaining_second_units: 50
```

### 7. Residual internet income versus video-game competition

Separate qualifying receipts 10,000 each, neither salary nor already taxed under another category. Internet expense allowance 15%; video-game costs undocumented, standard 20%. These are different actual classifications. [Articles 37o–37r, 50e][law]

```oa-check
name: Montenegro residual internet and video game bases
inputs:
  internet_receipts: 10000
  game_receipts: 10000
steps:
  - internet_base: internet_receipts * (1 - 0.15)
  - internet_pit: internet_base * 0.15
  - game_base: game_receipts * (1 - 0.20)
  - game_pit: game_base * 0.15
expected:
  internet_base: 8500
  internet_pit: 1275
  game_base: 8000
  game_pit: 1200
```

### 8. Capped foreign tax on private dividend income

Established resident, foreign gross dividend 10,000; qualifying foreign income tax actually paid 2,000, with treaty/refund/credit eligibility independently cleared. Montenegro tax 1,500, credit capped at 1,500, residual PIT zero. The excess 500 is not claimed as an automatic carryforward, refund or offset against another category. No local prirez, domestic advance or other credit is included. [Articles 37, 44–45][law]

```oa-check
name: Montenegro private foreign dividend credit cap
inputs:
  foreign_gross_dividend: 10000
  qualifying_foreign_tax: 2000
steps:
  - domestic_tax_on_foreign: foreign_gross_dividend * 0.15
  - allowed_credit: min(qualifying_foreign_tax, domestic_tax_on_foreign)
  - residual_domestic_pit: domestic_tax_on_foreign - allowed_credit
  - excess_not_claimed: qualifying_foreign_tax - allowed_credit
expected:
  domestic_tax_on_foreign: 1500
  allowed_credit: 1500
  residual_domestic_pit: 0
  excess_not_claimed: 500
```

### 9. Fine-art royalty and qualifying amateur-sport expenses

Separate qualifying receipts: fine-art rights 5,000 with no documented expenses and amateur-sport nonemployment receipt 5,000 with no documented expenses. Standard deductions 60% and 90%, PIT 300 and 75. Neither receipt is employment or another intellectual-property/sport category. Contributions and payer/annual withholding credits remain separate. [Articles 37i–37m, 50b–50c][law]

```oa-check
name: Montenegro fine art royalty and amateur sport
inputs:
  fine_art_rights: 5000
  qualifying_amateur_sport: 5000
steps:
  - royalty_base: fine_art_rights * (1 - 0.60)
  - royalty_pit: royalty_base * 0.15
  - sport_base: qualifying_amateur_sport * (1 - 0.90)
  - sport_pit: sport_base * 0.15
expected:
  royalty_base: 2000
  royalty_pit: 300
  sport_base: 500
  sport_pit: 75
```

## Annual return, advances and withholding workflow

Establish liability category by category before assembling GPP-FL. Keep separate taxable bases, losses, exemptions, gross tax, qualifying foreign credits, paid domestic advances/withholding and settlement. Do not put all gross receipts into the principal-business scale, apply one 15% rate to principal-business profit, or subtract a paid tax twice. Article 42 addresses annual calculation, payment with filing and excess advances by request/refund or next-period credit. Exact current form integration for mixed categories remains open. [Articles 10, 12, 42–45][law]

The ordinary annual deadline is the end of April for the previous year. Principal actual-income and supplementary business, occasional independent income not withheld, qualifying direct property income, capital gains, foreign income and other Article 43 categories must be assessed against the current legal filing population. Do not copy the older rule's broader rental wording over the law's current legal-person/entrepreneur payer exception. A licensed tourist accommodation provider files even without income. Nonresidents file Montenegro income for which withholding is not prescribed; recorded business-book capital gains have the specified tax-balance route. [Article 43][law]

Cessation of independent activity has a separate period and return within 30 days of deregistration. Multiple-employer salary above the statutory monthly threshold follows taxpayer filing and Article 43a authority assessment; the payroll Guide contains the indicative reconciliation. An employer's statement is not the individual's annual return. [Articles 42(1a), 43(2a), 43a, 47][law]

Principal/supplementary business advances are monthly, generally 1/12 of prior-year business tax, payable by the end of the current month for the preceding month. New activity uses an informative estimated-income declaration within 15 days of registration. Keep actual prior liability, start/stop periods, paid amounts and changes; no universal reduction for low current receipts is assumed. [Article 48][law]

Lump-sum principal-business taxation needs an application/decision, permitted activity and turnover conditions; Article 49's stated threshold below EUR 30,000.01 is not a VAT threshold or automatic exemption. Listed professional/sector activities and VAT-registered taxpayers are excluded, with specific kiosk/mobile/own-production exceptions. Applications ordinarily by end January or within five days of a new registration; seasonal payment has its separate rule. Full current scale/application/decision is not reconstructed here, and no lump-sum election is assumed. [Article 49][law]

Payer withholding and annual settlement are different: occasional independent work Article 48a, rent Article 49a, capital Article 50, sport/royalties Articles 50b–50c and other receipts Article 50d have their own payer/event rules. Capital gains and residual internet/video-game income follow annual payment under Articles 50a/50e. Domestic gambling uses the amended regime and specific winning/payment events, including its transition; no full gambling method is claimed. Foreign salary has the separate Article 46 five-day payment route and annual reporting. [Articles 46–50f][law]; [70/26][may]

## Actual form evidence and limits

The Ministry's April 2026 annual-return rule reproduces amendments through 103/25. Article 3 names GPP-FL plus A, PPG, A1, B, B1, C, D, D1, E, E1, F, G and H, with instructions. Articles 4–5 cover filing location/method and signature. The actual two-page download **does not include those form attachments**; it ends with a form label/link. It therefore does not establish current boxes or an accepted 2026 submission. [Annual rule Articles 1–5][return]

A different actual government GPP-FL attachment inspected here contains an obsolete flat 9% main calculation and fewer schedules. It is **not used** as current form mapping or current tax law. An online proposed 2025 replacement is likewise not substituted for the promulgated actual form. Supplementary-business schedule updates, full current instructions/attachments and IRMS field validation remain outstanding. No fictional numbered-box mapping is supplied. [Annual rule][return]; [obsolete attachment, comparison only][oldform]

Retain identity/residence/source, all income records, accounts/loss registers, asset/valuation/indexation evidence, status/relief documents, foreign taxes/treaties, payer statements, paid advances, applicable schedules, signed final return/acknowledgement and payment/assessment ledgers. For corrections retain original, changes and accepted authority outcome; exact current correction, interest, appeal/stay and enforcement procedure still needs the applicable tax-procedure law under Article 53. [Articles 42–53][law]

## Sanctions and remaining review

Article 53a contains offence-specific payer/entrepreneur failures and ranges; Article 53v specifies individual return/payment/foreign-salary offences with EUR 500–2,000 range. Do not turn an arithmetic difference into an automatic penalty. Procedure, original due dates, assessments and remedy periods require current evidence. [Articles 53–53v][law]

Remaining: actual current GPP-FL attachments, supplementary-business/new-activity forms and IRMS; full PIT depreciation and status/loss integration; specialist expense/receivable/incentive/lump-sum applications; current valuations/indexation and property/family exclusions; full gambling transition; treaties/residence certificates/credit allocation; local surtax, contribution and other levy interfaces; exact procedure/corrections/refunds; independent full-country review and named accountant attestation. All seven domains remain partial. Nine computations and file presence do not establish comprehensive coverage.

## Sources

Read on **24 October 2026**. Actual law reading covers Articles 2–8, 10–37s, 42–50f, 53–53v and targeted historical provisions, with current 160/25/70/26 gates. The annual-rule PDF was retrieved/read and page 1 visually inspected; missing attachments and obsolete alternative form are recorded. No actual taxpayer facts, accepted filing, bilateral treaty clearance or accountant attestation obtained.

[law]: https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0
[amend]: https://wapi.gov.me/download/47bea12c-f250-4cdc-b481-3afc30fba94f?version=1.0
[may]: https://www.sluzbenilist.me/propisi/394390/download
[mayrecord]: https://www.sluzbenilist.me/propisi/394390
[return]: https://wapi.gov.me/download/afb50b45-7e83-4dac-b69e-2a1e280d3ffc?version=1.0
[oldform]: https://wapi.gov.me/download/6f6af511-ccf7-4fc1-bd5d-82243d9a91cd?version=1.0
[proposal]: https://wapi.gov.me/download/58f7f48c-33de-4ec0-a1f4-28fd16fc7fb6?version=1.0

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
