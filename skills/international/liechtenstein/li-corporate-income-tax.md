---
name: li-corporate-income-tax
description: >
  Prepare 2026 Liechtenstein corporate profit-tax workpapers for ordinary legal
  entities. Use for residence and source screening, the book-to-tax bridge,
  modified-equity interest deduction, loss use, the minimum-tax exception, tax
  return attachments and provisional/final reconciliation. It replaces the earlier
  approximate secondary-source summary with selected current Tax Act and Tax
  Ordinance provisions. Confirm the entity, period, income, deduction eligibility,
  balances and notices before calculating. This draft does not complete
  participation exemptions, groups, PVS, GloBE, restructuring, foreign relief,
  specialised entities or live return filing. A worked assumption is not an
  approved tax position or named local accountant review.
jurisdiction: LI
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
category: international
version: 0.3
---

# Liechtenstein corporate income tax v0.3

Independent source/editorial review evidence and correction status are in the [dated whole-pack review record](../../../docs/research/2026-10-24-liechtenstein-pack-review.md). Apply its exact revision and scope limits. Named Liechtenstein accountant review remains open.

The 30 October ordinary equity/liquidity and exemption additions are writer drafts awaiting fresh independent whole-pack review. The historical review is not extended to these changes.

## Who this applies to

Use this 2026 source-cited draft for an ordinary legal entity after establishing its classification. SteG article 44 makes seat **or** actual management in Liechtenstein a resident-tax gate; foreign entities have the specified domestic-source categories. Article 46 controls commencement/cessation. Exemption, PVS, special entities and treaty/PE attribution require separate analysis. A foreign registration address does not by itself decide tax residence. [Tax Act, articles 44–46][law]

## Rates, bands and thresholds

| Item | Current rule | Source |
|---|---|---|
| Ordinary profit tax | 12.5% of taxable net income | SteG article 61; [authority summary][authority] |
| Minimum tax where applicable | CHF 1,800, creditable against profit tax, not added to it | SteG article 62(1)–(2) |
| Commercial-business minimum-tax exception | Exclusive qualifying commercial-business purpose and average balance-sheet total over the last three years **not exceeding CHF 500,000** | SteG article 62(3) |
| Ordinary brought-forward loss use | At most 70% of positive taxable net income | SteG article 57(1); exceptions in 57(1a) |
| Equity deduction reference rate | 4% Sollertrag in SteG article 5 for 2026 | SteG articles 5 and 54; [Act 2024/483, commencement II(2)][amendment] |
| Late-payment interest | 4% under current SteV article 45, applied to the correct liability/payment period | SteG article 114; SteV article 45 |

Do not apply a CHF 1,800 minimum to every entity without classification: article 62 distinguishes specified source-tax-finalised cases, its commercial-business exception and assessed versus unassessed payment routes. A short liability period does not itself prorate the statutory minimum. Startups without three completed years and disputed purpose/balance classifications need separate confirmation. [SteG, article 62][law]

## The base

Start from the relevant PGR financial statements. SteG article 47 requires taxable net income, not gross receipts or cash balance; its listed adjustments include non-business expenses, unsupported depreciation/provisions, hidden distributions, tax expense and non-arm's-length related-party financing. Map each line to the actual rule and avoid double-counting tax adjustments already in the accounts. Limited taxpayers need the domestic-income expense link in article 47(5). The accounting-period end determines the tax year under SteV article 4 for noncalendar accounts. [SteG, article 47][law]; [SteV, article 4][ordinance]

Article 48 contains exemptions and anti-abuse conditions; do not treat every participation receipt, disposal, foreign PE result or property item as exempt from a one-line summary. The ordinary screens below now supplement that caution; specialised and disputed application remains open. Likewise, an ordinary 12.5% calculation does not compute a GloBE top-up liability: the latter has its own legislation and scope. The earlier blanket zero-withholding summary is not used as a classifier for every payment; for example article 63a has a distinct 12% source-tax rule for specified nonresident corporate board-function income. Treaty and recipient facts remain necessary. [SteG, articles 1, 44, 48 and 63a][law]

### Equity deduction: establish modified equity first

SteG article 54 uses **modified equity**, not simply closing book equity. Its calculation deducts own shares, participations, nonbusiness assets and the stated 6% asset amount; it also addresses opening values and changes. SteV article 32 requires the specified time weighting/quarterly averages and permits a proportional deduction for a period other than twelve months. Article 32a supplies the nonbusiness/excess-liquidity rules. Do not multiply total paid capital by 4% and call that the deduction. [SteG, article 54][law]; [SteV, articles 32–32a][ordinance]

The deduction cannot create or increase a current loss. Negative modified equity gives zero deduction. Article 54(3)–(5) adds connected-loan, financed-participation and anti-abuse adjustments/exceptions. Establish these before using the case-only base below. The 4% reference is now in article 5 itself for 2026; the older instruction to confirm it only from an annual Finance Act is superseded. [SteG, articles 5 and 54][law]; [enacted commencement][amendment]

### Ordinary modified-equity workpaper

1. Reconcile opening equity under SteV articles 18 or 21, including taxed excess/shortfall values. Use only the domestic-income-linked portion for a limited taxpayer. Separate paid capital and reserves from the deductions below. [SteV article 32(1)–(3)][ordinance]
2. Time-weight current capital contributions, reductions, repayments and open distributions. Aggregate each quarter's movements and deem them to arise at its midpoint. Deduction assets use their annual average on the same quarterly basis. A different method where data are unavailable requires an application; the authority can require a more precise average for the specified cases. A non-twelve-month period has the separate proportional route. Do not silently substitute closing equity. [SteV article 32(4)–(7)][ordinance]
3. Deduct own shares, participations and nonbusiness assets, then **6% of the remaining asset pool**, excluding those three categories from that pool. Keep gross assets, each excluded category, the residual asset base and its 6% deduction separately so an asset is not deducted twice. Apply the zero floor and the article 54(3)–(5) connected-loan, financed-participation and anti-abuse rules before the final allowed deduction. [SteG article 54][law]
4. For an ordinary operating enterprise, SteV article 32a(2) presumes excess liquidity to the extent the following balance is positive: short-term receivables, accrual/prepayment assets and liquid funds at 100%, less third-party short-term liabilities/accruals at **160%**, less related-party short-term liabilities at **100%**. Advance payments and turnover deferrals are excluded from the stated liability categories. This is a nonbusiness-asset presumption, not a free-standing profit expense. [SteV article 32a(1)–(2)][ordinance]
5. For operating turnover **below CHF 10 million**, article 32a(3) uses the lower of that positive balance and the amount by which liquid funds exceed **25% of net turnover**. Deduct resolved distributions under article 32a(4). Articles 32a(2)–(4) do not apply to banks, insurers, holding companies or finance companies. Luxury/art assets, land reserves and other assets not predominantly serving the actual business purpose still require the article 32a(1) screen; passing a liquidity test does not make every asset business-essential. [SteV article 32a][ordinance]

Actual asset classification, tax values, averaging and all special adjustments must be documented. The example below assumes an ordinary operating company, no capital movements and already established annual-average asset values. It calculates the base rather than assuming a final modified-equity figure.

### Ordinary exemption workpaper

SteG article 48(1) separately excludes the listed foreign agricultural, PE, rental/property and participation results for an unlimited taxpayer; article 48(2) has its own limited-taxpayer list. Match each receipt or gain to its actual category. An exempt foreign PE's losses have the separate article 57(2) nonduplication/recapture rule. A domestic property gain is excluded from ordinary profit tax only to the stated extent subject to the domestic property-gains tax. [SteG articles 48 and 57][law]

For participation distributions and the specified foundation-like distributions, retain a separate article 48(3)–(7) file:

- At **25% or more of votes or capital**, or for the stated beneficiaries, the hybrid rule in article 48(3)(a) makes the receipt taxable if the payer can claim it as a tax expense. Do not treat every foreign distribution as exempt.
- Independently test the article 48(3)(b) passive/low-tax combination. The foreign payer's total income must persistently consist of **more than 50% passive income**, subject to the actual-economic-activity exception, **and** its net profit must meet the low-tax condition. Exactly 50% does not pass the first numerical test.
- For a holding **below 25%** (or a specified beneficiary), the low-tax test uses a profit-tax rate **less than half** the article 61 domestic rate. With 12.5% domestic tax, half is 6.25%; this arithmetic is not an effective-tax safe harbour. At **25% or more**, compare the actual effective foreign burden with **50% of the comparable domestic-case burden** under the Act. Do not substitute the nominal 6.25% screen for that comparison.
- Article 48(4) defines passive categories, including the specified finance/IP/leasing income and indirect participation income/gains; article 48(5) defines total income before expenses/deductions and net profit with the foreign-tax addback. Article 48(6) extends its stated anti-passive rule to disposal/liquidation gains and unrealised increases. Under article 48(7), the claimant must prove that the disqualifying conditions are absent. Preserve payer accounts, underlying income/activity, ownership, foreign tax and deductibility evidence. [SteG article 48(3)–(7)][law]

This supplies the ordinary statutory screens. It does not establish a particular foreign payer's facts, indirect-chain classification, exemption, group election, restructuring, PVS or GloBE outcome.

### Loss register and sequence

After the relevant current-income adjustments, reconcile the opening assessed loss balance, current loss, amount used and closing balance. Ordinary use is limited to 70% of positive taxable net income; no loss amount is manufactured merely from the percentage. Article 57(1a) removes the cap for its liquidation/all-assets-exit cases. Foreign PE losses have separate nonduplication, recapture and five-year/earlier-cessation rules in article 57(2). Groups under article 58 require a separate method. Do not apply the ordinary example to those cases. [SteG, articles 57–58][law]

### Retained predecessor controls

The [exact original-control annex](../../../ledgers/li-corporate-income-tax-evidence/retained-original-controls.md) preserves all four predecessor executable blocks. Their substantive cases remain here:

- The former book-to-tax case assumes CHF100,000 profit, CHF5,000 addbacks, CHF500,000 already reconciled modified equity and CHF60,000 opening losses. The CHF20,000 equity deduction leaves CHF85,000; the ordinary loss cap allows CHF59,500, leaving CHF25,500 taxable, CHF3,187.50 tax and CHF500 losses carried forward. It does not establish the modified-equity base.
- The minimum-tax case remains executable below: CHF1,250 ordinary tax leads to CHF1,800 total, not CHF3,050, when the minimum applies.
- With CHF10,000 positive profit and CHF500,000 established modified equity, the raw CHF20,000 equity amount is limited to CHF10,000; profit is zero and no current loss is created. The minimum is a later test.
- Three qualifying balance-sheet totals of CHF400,000, CHF500,000 and CHF600,000 average exactly CHF500,000. That passes only the numerical “not exceeding” screen; exclusive commercial purpose and all other conditions still require evidence.

## Deadlines and filing

1. Retain incorporation/management, legal-form/status, accounting-period and ownership records; the PGR accounts and trial balance; the detailed adjustment, equity and loss workpapers; income-category/treaty evidence; and the actual filing/payment notices.
2. SteG article 94 requires a complete, truthful, signed return even without a personal form/notice. SteV article 41 identifies attachments: detailed accounts with comparatives, required auditor/review report, beneficial-owner/related-party loan accounts, provisions/accruals register, profit-allocation resolution and signed completeness confirmation. Its attachment language/currency permissions are not a general waiver of the return's requirements.
3. Check the current allocated filing deadline. The still-linked March 2012 provisional-tax leaflet gives 1 July as the normal following-year filing date, but is historical administrative evidence; this draft has not verified the 2027 calendar for 2026 income. SteV article 42 permits a reasoned written six-month extension under its request deadline and provisional-payment condition, with a further exceptional route. It is not automatic and does not itself postpone tax payment.
4. Under SteG article 127 and SteV article 47, reconcile provisional tax based on the submitted return, estimate or last final assessment with the final assessment. The provisional amount is credited; excess is refunded and a shortfall collected. SteG articles 113–114 distinguish legal due date, ordinary 30-day payment period and exceptions. Preserve actual notice/delivery dates before computing interest; the 2012 leaflet's specific calendar is not proof of the current assigned dates.

## Penalties and interest

Article 135's procedural fine requires its intentional/negligent noncompliance after reminder; ordinary maximum CHF 1,000 and serious/repeat maximum CHF 10,000 are ceilings, not automatic charges. Evasion, false accounts, collection, appeals and other sanctions require their own analysis. [SteG, articles 94, 113–114, 127 and 135][law]; [SteV, articles 41–42, 45 and 47][ordinance]; [historical provisional leaflet][provisional]

Late-payment interest is 4% under SteV article45 for the applicable period. Retain actual due, receipt and payment facts and distinguish a filing extension from an approved payment arrangement. The exact interest day-count and full sanctions/appeal application remain unresolved. [SteG articles113–114][law]; [SteV article45][ordinance]

## Cross-border points

Separate unlimited liability, domestic-source limited liability and treaty/PE allocation before computing. The article 63a source-tax example in The base is a payment-specific rule; it is not a universal withholding result. Use the [cross-border Guide](li-cross-border.md) for the distinct foreign-credit, claim and exit workpapers, and the [TP Guide](li-transfer-pricing.md) for article63/124a corresponding adjustments. Each retains its actual treaty, domestic-tax mapping, foreign-finality and procedure limits. Ordinary participation exemption screens above do not complete those processes. [SteG articles44,48,51,63–63a][law]

## Two worked examples that recompute

All case facts are assumptions. Arithmetic does not establish an allowed classification, exemption, deduction or final assessment.

### Build the ordinary liquidity, equity and loss base

Assume a full-year ordinary operating company, CHF1.2 million net turnover, no capital movements, no resolved distribution and no special equity adjustment. Assume these liquidity amounts give the same deduction at each relevant valuation point. The documented liquidity inputs are CHF800,000 short-term receivables/accrual assets/liquid funds, CHF300,000 qualifying third-party short-term liabilities, CHF100,000 qualifying related-party liabilities and CHF400,000 liquid funds. The weighted balance is CHF220,000; the under-CHF10m cash/turnover route gives CHF100,000, so CHF100,000 is the presumed excess-liquidity amount.

Assume CHF800,000 opening tax-adjusted paid equity/reserves and documented annual-average deductions of CHF20,000 own shares, CHF100,000 participations and CHF100,000 excess liquidity, with no other nonbusiness asset. The residual asset pool after those categories is CHF1 million; its 6% deduction is CHF60,000. Modified equity is CHF520,000 and the 4% equity amount CHF20,800. Assume CHF100,000 book profit before tax plus CHF5,000 established addbacks and CHF60,000 assessed opening losses. Profit after equity is CHF84,200; loss use is limited to CHF58,940. Taxable profit is CHF25,260, ordinary tax CHF3,157.50 and closing losses CHF1,060. The applicable CHF1,800 minimum does not increase that tax. [SteG articles 54,57,61–62][law]; [SteV articles 32–32a][ordinance]

```oa-check
name: Liechtenstein assumed operating liquidity modified equity and loss bridge
inputs:
  short_term_asset_pool: 800000
  qualifying_third_party_short_liabilities: 300000
  third_party_weight: 1.60
  qualifying_related_party_short_liabilities: 100000
  liquid_funds: 400000
  net_turnover: 1200000
  turnover_fraction: 0.25
  opening_adjusted_equity_no_movements: 800000
  average_own_shares: 20000
  average_participations: 100000
  average_remaining_asset_pool: 1000000
  remaining_asset_deduction_rate: 0.06
  profit_before_tax: 100000
  established_addbacks: 5000
  equity_reference_rate: 0.04
  assessed_opening_losses: 60000
  ordinary_loss_fraction: 0.70
  tax_rate: 0.125
  applicable_minimum: 1800
steps:
  liquidity_balance: max(0, short_term_asset_pool - qualifying_third_party_short_liabilities * third_party_weight - qualifying_related_party_short_liabilities)
  turnover_cash_excess: max(0, liquid_funds - net_turnover * turnover_fraction)
  presumed_excess_liquidity: min(liquidity_balance, turnover_cash_excess)
  residual_asset_deduction: average_remaining_asset_pool * remaining_asset_deduction_rate
  modified_equity: opening_adjusted_equity_no_movements - average_own_shares - average_participations - presumed_excess_liquidity - residual_asset_deduction
  profit_before_equity: profit_before_tax + established_addbacks
  allowed_equity_deduction: min(max(0, profit_before_equity), max(0, modified_equity) * equity_reference_rate)
  profit_before_losses: profit_before_equity - allowed_equity_deduction
  losses_used: min(assessed_opening_losses, max(0, profit_before_losses) * ordinary_loss_fraction)
  taxable_profit: profit_before_losses - losses_used
  ordinary_tax: taxable_profit * tax_rate
  resulting_income_tax: max(ordinary_tax, applicable_minimum)
  closing_loss_balance: assessed_opening_losses - losses_used
expected:
  liquidity_balance: 220000
  turnover_cash_excess: 100000
  presumed_excess_liquidity: 100000
  residual_asset_deduction: 60000
  modified_equity: 520000
  profit_before_equity: 105000
  allowed_equity_deduction: 20800
  profit_before_losses: 84200
  losses_used: 58940
  taxable_profit: 25260
  ordinary_tax: 3157.50
  resulting_income_tax: 3157.50
  closing_loss_balance: 1060
```

### Minimum tax is not added to ordinary tax

Assume CHF 10,000 final taxable profit and no minimum-tax exemption. Ordinary tax CHF 1,250 is below the applicable CHF 1,800 minimum: the resulting income tax is CHF 1,800, not CHF 3,050. This excludes other levies or GloBE.

```oa-check
name: Liechtenstein assumed applicable minimum tax comparison
inputs:
  established_taxable_profit: 10000
  tax_rate: 0.125
  applicable_minimum: 1800
steps:
  ordinary_tax: established_taxable_profit * tax_rate
  resulting_income_tax: max(ordinary_tax, applicable_minimum)
  increase_due_to_minimum: resulting_income_tax - ordinary_tax
expected:
  ordinary_tax: 1250
  resulting_income_tax: 1800
  increase_due_to_minimum: 550
```

## Ask the client first

Obtain actual management, legal form/exemption/PVS status, full period and income source; all accounts/equity movements and related-party balances; assessed loss history; three-year minimum-tax data and purpose; current forms, notices and elections. Refer participation/exemption anti-abuse, NID special cases, groups, foreign PE loss/credit, exit/restructuring, PVS, GloBE, source tax and live filing. Corporate/XB coverage, full legal/amendment chain and named accountant review remain open.

## Sources

Historical selected reads on 24 October 2026:

- [Tax Act, consolidated 1 July 2026][law], selected articles 5, 44–47, 49, 54, 57, 61–63a, 94, 113–114, 127 and 135. Article 48/group/special provisions are not fully reconciled by this Guide.
- [Tax Ordinance, consolidated 1 July 2026][ordinance], articles 4, 32–32a, 41–42, 45 and 47.
- [Act 2024/483][amendment], article 5 and commencement II(2): 1 January 2026/first 2026 assessments for the statutory Sollertrag rule.
- [Current corporate-tax authority summary][authority], 12.5%/CHF 1,800 headline only; statutory exceptions control.
- [March 2012 provisional collection leaflet][provisional], retained as historical explanation, not renewed confirmation of every present deadline.

The current Tax Act and Ordinance were refetched on 30 October 2026 and matched the saved consolidations. Selected passages used by the ledger include corporate articles5,44,46–49,54,57–58,61–63a,94,113–114,127,135 and SteV4,18,21,32–32a,41–42,45,47, read that day. The ordinary methods above use those passages. Administrative summary/2012 leaflet dates are not renewed, and this is not a complete special-regime/amendment audit.

[law]: https://www.gesetze.li/konso/pdf/2010340000
[ordinance]: https://www.gesetze.li/konso/pdf/2010437000
[amendment]: https://www.gesetze.li/chrono/pdf/2024483000
[authority]: https://www.llv.li/de/landesverwaltung/steuerverwaltung/steuern-juristische-personen/ertragssteuer
[provisional]: https://www.llv.li/servicekonto/steuerverwaltung/provisorischer-bezug-der-ertragssteuer-merkblatt.pdf

<!-- openaccountants-cta-block -->

---

## Talk to an accountant

Find the current Guide and professional-review status at [OpenAccountants](https://www.openaccountants.com).
