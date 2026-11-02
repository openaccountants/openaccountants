---
name: ad-corporate-income-tax
description: "Source-cited draft: corporate income tax for Andorra (tax year 2025) — rates, thresholds and rules with primary-source citations. Unverified; pending local-accountant review."
jurisdiction: AD
tax_year: 2025
last_updated: 2026-10-23
version: 0.6
category: international
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Andorra Corporate Income Tax

## Corporate income tax (Impost sobre Societats)

- **Standard corporate income tax rate** — 10% under [Law 95/2010, Article 41(1)](https://www.portaljuridicandorra.ad/L2010095).
- **Legacy new-business incentive** — Do not apply the former 5%-on-EUR-50,000 claim as a current new-company rate. The former second additional provision was repealed by Law 17/2017; the current second additional provision addresses speculative property gains. The first additional provision concerns the first year of application of the tax itself, not each company’s first year. [Current law and amendment annotations](https://www.portaljuridicandorra.ad/L2010095). Historical-period eligibility requires separate review.
- **Holding-company regime** — Article 38 exempts qualifying dividend and disposal income under an authorised special regime, subject to the conditions below. This is an income exemption, not a blanket zero-rate company. [Law 95/2010, Article 38](https://www.portaljuridicandorra.ad/L2010095).
- **Eligible intangible income** — Article 23 provides an 80% base reduction multiplied by the qualifying expenditure ratio, subject to asset, activity, record and authorisation conditions. It is not a general 2% rate on all intellectual-property revenue. See the workpaper below. [Law 95/2010, Article 23](https://www.portaljuridicandorra.ad/L2010095).
- **Tax base** — Correct the accounting result prepared under the accounting law and general accounting plan for the adjustments in Chapter IV. See the reconciliation below. [Law 95/2010, Article 9](https://www.portaljuridicandorra.ad/L2010095).
- **Corporate residence** — A company is resident if incorporated under Andorran law, has its registered office in Andorra, or has its effective management in Andorra  _(Llei 95/2010 IS)_
- **Withholding tax on dividends to non-residents** — 0% — no withholding tax on dividends paid by Andorran companies to non-residents %  _(Llei 94/2010 IRNR)_
- **Withholding tax on interest to non-residents** — 0% — no withholding tax on interest paid to non-residents %  _(Llei 94/2010 IRNR)_
- **Withholding tax on royalties to non-residents** — 5% (may be reduced under an applicable double tax treaty) % (approx — confirm treaty rates)  _(Llei 94/2010 IRNR)_
- **IS filing window** — The month following the six months after the tax period ends. For a 31 December 2025 year-end, the ordinary window is July 2026. Earlier filing during the first six months is permitted without changing payment/refund deadlines. Confirm the current approved form; no form number is certified here. [Corporate-tax regulation, Article 45](https://www.portaljuridicandorra.ad/R20231229C).
- **Advance payment** — During the ninth month after the period begins, pay 50% of the immediately preceding period's settlement liability. For a calendar-year business this is September. If the previous period was shorter than twelve months, include proportionate liability from preceding periods to complete twelve months. The regulation excludes the first activity year from this advance. [Law 95/2010, Article 45](https://www.portaljuridicandorra.ad/L2010095); [regulation, Article 37](https://www.portaljuridicandorra.ad/R20231229C).

## Filing and payment workpapers

**Scope of this update:** filing, ordinary advance-payment, general-rate, ordinary expense-reconciliation, loss-relief, holding-company and Article 23 intangible rules were checked on 23 October 2026 against the current legal-portal consolidations. The other legacy 2025 bullets above, including residence, base and withholding summaries, have not been reverified by this update and must not be used as confirmed current advice. The portal labels its consolidations as without official legal status. This remains a partial source-cited draft, not comprehensive corporate-tax coverage.

Reconcile the settlement liability before advances to the payments actually made. Under Article 46, payments under Articles 45 and 45 bis are credited to determine the balance; an excess is refundable. Property-transfer advances have their own rules, including timing of credit where income is recognised over deferred receipts, and are not computed in the examples below. [Law, Article 46](https://www.portaljuridicandorra.ad/L2010095).

### Example 1: ordinary advance and balance

Assume a full prior year, prior settlement liability EUR 18,000, current settlement liability EUR 22,000 and no property advance or other adjustment. The September advance is EUR 9,000. After it is paid, the annual balance is EUR 13,000. The settlement liabilities are assumed independently verified; the example does not compute incentives or taxable profit.

```oa-check
name: Andorra ordinary advance and annual balance
inputs:
  prior_liability: 18000
  advance_rate: 0.50
  current_liability: 22000
steps:
  advance: prior_liability * advance_rate
  final_balance: current_liability - advance
expected:
  advance: 9000
  final_balance: 13000
```

### Example 2: excess advance

Assume a full prior year with settlement liability EUR 20,000, a EUR 10,000 advance actually paid, current settlement liability EUR 6,000 and no other adjustments. The balance is negative EUR 4,000, producing a EUR 4,000 excess for refund under Article 46. This arithmetic does not establish when the refund will be received.

```oa-check
name: Andorra advance excess reconciliation
inputs:
  prior_liability: 20000
  advance_rate: 0.50
  current_liability: 6000
steps:
  paid_advance: prior_liability * advance_rate
  final_balance: current_liability - paid_advance
  excess: paid_advance - current_liability
expected:
  paid_advance: 10000
  final_balance: -4000
  excess: 4000
```

Ask for the declared accounting period, activity start date, prior-period lengths and settlement liabilities, payment receipts, and any property-transfer advances before applying this timetable. Current electronic forms, general penalties, special regimes, the full tax-base calculation and professional review remain outstanding.

## Eligible intangible income workpaper

Article 23 covers positive income from the specified patents, utility models and copyright-protected computer programs. Compute the reduction separately for each asset. For licensing, the eligible income is receipts less the directly related deductible expenses, not gross royalty revenue. [Article 23(1), (3)](https://www.portaljuridicandorra.ad/L2010095).

The numerator includes qualifying own creation costs and the specified subcontracting costs. Related-party subcontracting qualifies in the numerator only where the related party is Andorran-resident and performs the activity in Andorra. For unrelated-party work abroad, apply the statutory 25% numerator limitation before the uplift. Uplift the qualifying numerator by 30%, capped at the denominator. The denominator includes total relevant creation costs, the specified nonqualifying subcontracting costs and intangible acquisition costs. General expenses, including interest and property depreciation, are excluded from both sides when not directly related to creation. Do not classify costs by accounting treatment alone. [Article 23(1)](https://www.portaljuridicandorra.ad/L2010095).

The taxpayer must exploit the asset in its own name in its economic activity. The licensee must use the rights in an economic activity, and that use must not produce goods/services generating deductible expenses for the licensor. Separate asset-level accounts must identify income, direct costs and relief. Prior negative income must be recovered before later positive income receives relief; later negative income following relieved profits has its own corresponding reduction rule. [Article 23(2)–(4)](https://www.portaljuridicandorra.ad/L2010095).

Apply for authorisation with the activity, asset types, means and evidence of conditions. The statutory decision period is six months from receipt or required correction; silence can be treated as rejection. Do not import the deemed-acceptance rule for advance-pricing agreements into this regime. The authorised regime takes effect in the application period; substantive changes require the statutory notification/authorisation process. Required exploitation, management or promotion activities also need evidence. [Article 23(5)–(6)](https://www.portaljuridicandorra.ad/L2010095).

### Example 3: partial qualifying expenditure

Assume an authorised eligible asset, EUR 100,000 positive net income, no prior-loss restriction, a correctly classified EUR 60,000 numerator before uplift and EUR 100,000 denominator. All foreign-subcontracting limits have already been tested. The uplifted ratio is 78%, so the reduction is EUR 62,400. EUR 37,600 remains taxable and produces EUR 3,760 at the general 10% rate before other adjustments. This is not a 2% result.

```oa-check
name: Andorra eligible intangible partial expenditure ratio
inputs:
  net_income: 100000
  qualifying_costs: 60000
  total_costs: 100000
  uplift: 1.30
  reduction_rate: 0.80
  general_rate: 0.10
steps:
  adjusted_numerator: min(qualifying_costs * uplift, total_costs)
  ratio: adjusted_numerator / total_costs
  reduction: net_income * reduction_rate * ratio
  remaining_base: net_income - reduction
  tax_before_other_adjustments: remaining_base * general_rate
expected:
  adjusted_numerator: 78000
  ratio: 0.78
  reduction: 62400
  remaining_base: 37600
  tax_before_other_adjustments: 3760
```

## Holding-company and participation exemptions

### Special holding-company regime

An Andorran SA or SL whose exclusive object is managing and holding participations in resident or non-resident companies can request the Article 38 regime. Its own capital securities/interests must be nominative. Apply through the census declaration; the regime applies to the tax period ending after ministry authorisation and later periods until renunciation is communicated. A description in the articles of association alone is not evidence that approval was granted. [Law, Article 38(1)–(2)](https://www.portaljuridicandorra.ad/L2010095); [regulation, Article 32](https://www.portaljuridicandorra.ad/R20231229C).

For foreign subsidiaries, the regime requires exposure, without exemption, to a substantially similar income tax at a nominal rate at least 40% of Andorra's general rate: 4% when the general rate is 10%. The statute treats this condition as met where an applicable Andorran double-tax treaty covers the subsidiary's country. It also provides a specified route for income traced through an untaxed direct subsidiary from a qualifying second-tier subsidiary. For Andorran subsidiaries, the condition is liability without exemption at the general rate. Do not substitute an effective-tax-rate calculation for the stated nominal-rate test. [Article 38(3)](https://www.portaljuridicandorra.ad/L2010095).

Article 38 imports Article 20(2)'s limitations. These include the exclusion for gains on interests in entities with at least 50% of assets directly or indirectly in Andorran real property/relevant rights; dividends generating a deduction for the payer; non-deductibility of expenses linked to exempt participation income; and participation-loss restrictions, including special extinction exceptions and reductions. Test each applicable limitation before exempting income or claiming a loss. [Articles 20(2), 38(3)](https://www.portaljuridicandorra.ad/L2010095).

Maintain the annual-accounts note showing participations held during the year, portfolio value and dividends/reserves received. Report the exemption in the tax return. The holding company must file even if no tax is payable. [Article 38(3), (5)](https://www.portaljuridicandorra.ad/L2010095); [regulation, Article 32](https://www.portaljuridicandorra.ad/R20231229C).

### Do not conflate this with the ordinary participation exemption

Article 20(1)'s ordinary exemption has its own tests, including at least 5% participation and the one-year holding condition, and for foreign subsidiaries a nominal-tax threshold of 50% of the general rate, rather than Article 38's 40%. Dividend holdings can complete the year after entitlement; a disposal requires the holding period to be met by disposal. The law specifies indirect-holding, related-holder continuity, underlying-income and tax-period tests that must also be checked. These ordinary-regime conditions are not a replacement for the special regime's approval and exclusive-object requirements. [Article 20(1)](https://www.portaljuridicandorra.ad/L2010095).

The transitional rules of Law 6/2018 can preserve historic treatment for part of a later gain on pre-1 July 2017 participations held under the qualifying old authorised regime. Obtain the original authorisation, acquisition date and pre-2021 gain allocation evidence before using that transition; this draft does not calculate its application. [Law 6/2018, third transitional provision reproduced with the corporate law](https://www.portaljuridicandorra.ad/L2010095).

## Carried losses and the settlement floor

Article 22 permits negative tax bases to offset positive tax bases of periods ending within the following **17 years**, subject to Article 43(2). Amounts not used because of that limit retain the window measured from generation; the limit does not restart the loss's expiry clock. Maintain the generation period, original amount, prior use, expiry and current eligible balance separately for each loss. This draft does not determine transitional treatment of historic losses. [Articles 22(1), 43(2)](https://www.portaljuridicandorra.ad/L2010095).

The settlement liability cannot fall below **30% of the gross tax on the positive base before prior-year losses**. Where that floor binds, reduce the losses and the deductions referred to in Article 43 accordingly. It is a combined constraint, not a general permission to use 70% losses and then deduct all credits as well. For a simple company at the general rate with no deductions, the arithmetic limits loss use to 70% of the positive pre-loss base; other deductions require a combined calculation. [Article 43(1)–(3)](https://www.portaljuridicandorra.ad/L2010095).

Article 22(2)'s loss restriction combines acquisition of majority capital/voting rights after the loss period, the acquiring person/entity or related group having held less than 25% at the end of that loss period, and the specified inactivity or changed/additional-activity condition. Do not describe a majority acquisition by itself as automatic loss forfeiture. Inactivity means no economic activity during the six months before acquisition. The alternative changed/additional-activity test requires both a different Andorran economic-activity classification group and the statutory turnover comparison: average annual turnover of those activities during the two post-acquisition years exceeds 50% of the entity's average annual turnover in the two preceding years. Record the ownership and activity evidence, not only the acquisition date. [Article 22(2)](https://www.portaljuridicandorra.ad/L2010095).

### Example 4: available losses do not eliminate the annual liability

Assume EUR 100,000 positive base before losses, EUR 90,000 eligible unexpired losses, the general 10% rate, no tax deductions and no special adjustments. Gross pre-loss tax is EUR 10,000 and the floor is EUR 3,000. Use EUR 70,000 losses, leave EUR 30,000 taxable and retain EUR 20,000 losses within their original expiry window. This example assumes ownership/activity restrictions have already been tested.

```oa-check
name: Andorra loss relief settlement floor without credits
inputs:
  pre_loss_base: 100000
  available_losses: 90000
  tax_rate: 0.10
  floor_fraction: 0.30
steps:
  pre_loss_tax: pre_loss_base * tax_rate
  liability_floor: pre_loss_tax * floor_fraction
  maximum_loss_use: pre_loss_base * (1 - floor_fraction)
  losses_used: min(available_losses, maximum_loss_use)
  taxable_base: pre_loss_base - losses_used
  settlement_liability: taxable_base * tax_rate
  losses_remaining: available_losses - losses_used
expected:
  pre_loss_tax: 10000
  liability_floor: 3000
  maximum_loss_use: 70000
  losses_used: 70000
  taxable_base: 30000
  settlement_liability: 3000
  losses_remaining: 20000
```

## Accounting-profit reconciliation

Under direct determination, start with the accounting result and reconcile the statutory adjustments. Distinguish permanent disallowances from timing differences; a cash payment does not establish deductibility. Keep an adjustment schedule linking each ledger item to its rule and evidence. [Article 9](https://www.portaljuridicandorra.ad/L2010095).

Article 13 excludes equity remuneration, the booked corporate tax charge, the specified communal rental-income and business-location tax liabilities, criminal/administrative fines, the specified late-filing/enforcement surcharges, gambling losses and costs of unlawful acts. Corporate-tax accounting income is likewise not taxable income. Do not generalise the listed disallowed surcharges to every type of interest without checking its provision. [Article 13(1)(a)–(e), (h)](https://www.portaljuridicandorra.ad/L2010095).

Donations and gratuitous expenditure have their own limits and exceptions under Article 13(1)(f). The provision describes client/supplier relations, customary staff expenditure, promotion and income-related costs and caps the deductible expenditure it covers at 1% of the average positive tax base for the current and two preceding years, before that limitation. Recognised nonprofit donations have a separate maximum of 10% of accounting result. Determine the classification and relevant base; neither is a general percentage of turnover. Interaction with separate donation credits and cases with short or loss-making histories need further review before calculation. [Article 13(1)(f)](https://www.portaljuridicandorra.ad/L2010095).

For related-entity payments, Article 13(1)(g) separately restricts deductions where the recipient's income is exempt, outside a similar income tax or subject to a nominal rate below 50% of the general rate, including specified mismatched classifications. The article contains an applicable-treaty presumption that must be tested. Arm's-length pricing alone does not displace this restriction. Director remuneration specifically for the office is deductible only if provided for in the company's articles; that condition does not by itself prove all other deduction requirements. [Article 13(1)(g), (2)](https://www.portaljuridicandorra.ad/L2010095).

Depreciation, impairment, provisions, finance-cost limits and timing require their separate Chapter IV tests. This ordinary-expense section does not supply complete schedules for those items.

### Example 5: permanent adjustments already charged in the accounts

Assume accounting profit EUR 80,000 after a EUR 7,000 corporate-tax expense, EUR 2,000 administrative fine and EUR 1,000 of the specified communal business-location tax. Assume no other adjustments, exemptions, losses, credits or special regimes. Add back those EUR 10,000 expenses to obtain EUR 90,000 taxable base and EUR 9,000 tax at 10%. Do not add an expense again if the starting profit already excludes it.

```oa-check
name: Andorra ordinary permanent expense adjustments
inputs:
  accounting_profit: 80000
  booked_corporate_tax: 7000
  administrative_fine: 2000
  specified_communal_tax: 1000
  tax_rate: 0.10
steps:
  permanent_addbacks: booked_corporate_tax + administrative_fine + specified_communal_tax
  taxable_base: accounting_profit + permanent_addbacks
  tax: taxable_base * tax_rate
expected:
  permanent_addbacks: 10000
  taxable_base: 90000
  tax: 9000
```

## Sources

Filing/payment and selected incentive provisions read 23 October 2026:

- [Law 95/2010, Articles 9, 13, 20, 22–23, 38, 41, 43, 45–46 and additional-provision annotations](https://www.portaljuridicandorra.ad/L2010095).
- [Corporate-tax regulation, Articles 32, 37 and 45](https://www.portaljuridicandorra.ad/R20231229C).

These citations substantiate the updated filing/payment and selected incentive sections, not every legacy incentive claim above.

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
