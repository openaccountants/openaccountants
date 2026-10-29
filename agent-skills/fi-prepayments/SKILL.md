---
name: fi-prepayments
description: "Calculate and reconcile Finnish income-tax prepayments for individuals, sole traders, partnership partners and corporate entities for 2026. Use a complete annual income-tax forecast, deductions, credits and withholding to establish the outstanding advance requirement, then apply the issued decision and instalment calendar. Covers ennakkovero, ennakkoperintä registration, revised estimates, additional prepayment, residual tax, payment references and the distinction between interest with relief and overdue-payment interest. Includes corporate accounting-period rules, individual seasonal or monthly schedules and the January 2027 weekend trap for 2026 tax. Read with the individual or corporate income-tax computation skill; this payment procedure does not replace those tax-base calculations."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/fi-prepayments"
  jurisdiction: "FI"
  tax_year: "2026"
  last_updated: "2026-10-27"
  authored_by: "Michael Cutajar and the OpenAccountants team"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Finland prepayments v1.3

## Who this applies to

Use for ordinary advance collection of Finnish income tax for individuals, sole traders, partnership partners and corporate entities. Tax on business, rent, gains and other income without sufficient withholding is collected by prepayment under Prepayment Act 1118/1996 §23. A partnership's partners, rather than the partnership itself, prepay their allocated income tax. Registration in the prepayment register governs a customer's withholding on qualifying trade income, not the supplier's own tax liability. Use [individual income tax](fi-income-tax.md), [corporate income tax](fi-corporate-income-tax.md) and the appropriate cross-border skill to establish the annual tax first. [Act §§23–25][law]; [Vero payment instructions][payments].

## Rates, bands and thresholds

| Item | 2026 amount or rule | Official basis |
|---|---|---|
| Ordinary individual advance | Minimum EUR 170; EUR 170–500: 2 instalments in March/September; over 500–1,700: 3 in February/July/November; over 1,700–10,000: 6 in February/April/June/August/October/December; over 10,000: 12 monthly | Act §23 and [Vero instalment table][instalments] |
| Ordinary corporate advance | Minimum EUR 500; EUR 500–2,000: 2 equal instalments in accounting-period months 3 and 9; over 2,000: 12 equal instalments | Act §23 and [Vero instalment table][instalments] |
| Ordinary due day | 23rd, moved to next business day when a weekend or public holiday | Act §23; [Vero payment instructions][payments] |
| Additional prepayment minimum | Individual EUR 170; corporate EUR 500 | Act §24; [Vero additional prepayment][additional] |
| Interest with relief accruing in 2026 | 4.5% annually; starts first day of second month after tax-year end | Act §24; [Vero interest calculation][relief] |
| Ordinary overdue-tax interest accruing in 2026 | 9.5% annually, day after due date through payment | [Vero interest calculation][relief] |
| Relief-interest deduction on back tax | EUR 20, capped at calculated interest; no deduction on additional prepayment | [Vero interest calculation][relief] |
| Back tax collection | Over EUR 170: two instalments; under EUR 10: not collected | [Vero back taxes][backtax] |
| Customer withholding on work paid to a supplier not in the prepayment register | Corporate entity or partnership 13%; self-employed or other individual: rate on the tax card for nonwage pay, or 60% if no card is presented; none on goods or rent | Act §§13,25; [Vero prepayment register][register] |
| Claim for adjustment against a prepayment decision | Within 60 days of receiving the decision; instalments stay payable while it is pending | [Vero claim for adjustment][adjust] |

The ordinary table assumes a full period and no special scheduling election or midyear decision. Individuals can elect equal monthly payments or request seasonal months. A replacement decision controls the actual dates and rounding. Do not mechanically divide a changed advance over months that have already passed. [Vero instalment table][instalments].

## The base

### Compute the tax before computing the payment shortage

1. Identify the tax year and taxpayer. For individuals use the calendar-year total, including all accounting periods ending in it. For a corporate taxpayer identify all accounting periods ending in the same calendar year and apply the tax-year-end rule when calculating additional-prepayment interest. [Vero additional prepayment][additional].
2. Build actual year-to-date results plus the remaining forecast. For an individual include the sole-trade/partnership allocation, wages, benefits, pensions, rent, capital gains and foreign receipts, with the correct category, deductions, municipal rate and credits from the income-tax skills. For a company reconcile accounting profit to taxable income, loss use, income tax and other taxes in its assessment. Do not multiply individual business profit by a flat corporate rate. [Act §§1–3,23][law]; [Vero payment instructions][payments].
3. Reconcile the forecast total tax with tax-card withholding, investment withholding, already paid advances and remaining valid instalments. A workpaper shortage is forecast tax less those amounts, floored at zero; do not submit existing advances as if they were income deductions. Reconcile the resulting request to Vero's decision rather than assuming that the workpaper itself changes the assessment. [Act §§3,24][law].
4. Request a higher or lower decision with revised income and deductions. Vero can change or remove an advance on request until the assessment ends. If too much has been paid, follow the replacement decision and final refund allocation. Do not cancel an existing debit unilaterally. [Act §24][law].

### Registration and collection are separate

A qualifying business on the prepayment register receives its work invoice without the customer's advance withholding. The same business still needs its own advance decision. Without registration the customer withholds at the rates in the table above, calculated on the invoice amount excluding VAT; wages always retain their payroll route. Nonresident source-tax rules remain separate. [Act §§13,23,25][law]; [payroll](fi-employer-payroll.md); [corporate cross-border](fi-corporate-cross-border-tax.md).

## Deadlines and filing

Request and revise advances through MyTax using the taxpayer and year concerned. A small-scale business whose income and expenses can be included in the wage tax card changes the tax card instead of requesting a separate prepayment decision. [Vero tax prepayment][prepayment-home]. New businesses supply their own forecast; existing decisions use the latest completed assessment until revised. Preserve the old decision, request, acknowledgement, replacement decision and payment ledger. Continue the old instalments until the replacement arrives. [Act §24][law]; [Vero payment instructions][payments].

Additional prepayment requires a **request before payment**. Individuals can request from December of the tax year until assessment completion; the exact December 2026 opening day is not asserted here. A December request cannot select a December due date: the earliest is the first banking day in January. Corporate requests start only after the tax year ends. Do not confuse an ordinary in-year increase with additional prepayment. Use the new decision's reference and due date; additional prepayments are not paid by e-invoice/web invoice. [Vero additional prepayment][additional].

For 2026 individual tax, a due date **within January 2027** avoids relief interest. Since 31 January 2027 is Sunday, select a due date no later than **Friday 29 January 2027**; a weekend due date moves into February and interest follows the moved due date even if money was sent earlier. Companies have the first month after tax-year end free of relief interest, subject to the same business-day issue. [Act §24][law]; [Vero interest guidance][relief].

Uncovered tax after assessment is back tax. Use the issued decision for final instalments and due dates. An advance request is no substitute for the annual income-tax return; a completed assessment requires the adjustment procedure rather than an advance revision. [Act §24][law].

## Penalties and interest

Distinguish a forecast change, an unpaid decision and a deficient tax return. A good-faith forecast revision is not itself a late tax return. An unpaid advance bears ordinary interest from the day after its due date; follow MyTax for the amount payable and payment-arrangement route. A request to reduce an advance does not suspend its existing due date. A late payment is applied first to the accrued late-payment interest and then to the overdue instalment; tax left unpaid is transferred to enforcement, which adds an enforcement fee. [Vero if you pay late][late]. [Vero payment instructions][payments].

For an additional prepayment due after the interest-free month, calculate relief interest from the first day of the second month after tax-year end **through its due date**, using actual days and the number of days in the relevant calendar year. Split a calculation across calendar years/rate changes. Early payment does not shorten relief interest determined by the chosen due date. After that due date ordinary late interest applies until payment. Back-tax relief interest has the EUR 20 deduction; additional prepayment does not. Vero notes that where the tax is no more than approximately EUR 880 it can cost less to leave it as back tax; compare actual decision dates and interest rather than treating EUR 880 as a fixed cut-off. [Vero additional prepayment][additional]. The **2027 interest rates are not confirmed in this skill**; do not carry 2026's 4.5% or 9.5% into 2027. [Vero interest calculation][relief].

## Cross-border points

A foreign employer that does not withhold Finnish tax can leave taxable wages to advance collection. Include foreign receipts and deductible costs in the annual forecast even where a treaty credit or exemption reduces Finnish tax. Establish the residence period, income source, treaty method and eligible foreign tax using the [individual cross-border skill](fi-individual-cross-border-residence.md) before reducing advances. A foreign assessment is not automatically a Finnish credit. [Act §23][law]; [individual cross-border skill](fi-individual-cross-border-residence.md).

Companies use the corresponding [corporate cross-border skill](fi-corporate-cross-border-tax.md) for PE, credit and source-tax classification. A source-tax payment, employer remittance and corporate income-tax advance are distinct liabilities; reconcile each to its own decision and reference.

## Two worked examples that recompute

### 1. Individual forecast and issued six-instalment decision

Assume the income-tax computation has established annual tax of EUR 8,800 and expected wage withholding of EUR 7,000, with no other advances or credits. The advance requirement is EUR 1,800. Assume Vero issues an ordinary unchanged full-year six-instalment decision: each instalment is EUR 300. The example establishes the payment reconciliation, not tax from an arbitrary profit figure.

```oa-check
name: Finland individual forecast to six instalments
inputs:
  computed_annual_tax: 8800
  forecast_withholding: 7000
  instalments: 6
steps:
  requested_advance: max(0, computed_annual_tax - forecast_withholding)
  instalment_amount: requested_advance / instalments
  reconciled_collection: forecast_withholding + instalment_amount * instalments
expected:
  requested_advance: 1800
  instalment_amount: 300
  reconciled_collection: 8800
```

### 2. Corporate shortage and 2026 relief interest

Assume a single corporate tax year ending 31 March 2026, final forecast tax EUR 20,000, paid advances EUR 15,000 and additional-prepayment due date 13 May 2026. The EUR 5,000 shortage bears relief interest for 1–13 May inclusive (13 days): EUR 8.01 at 4.5% / 365. There is no EUR 20 deduction. Payment by 13 May adds no ordinary overdue interest. Eligibility, decision and dates are assumed established.

```oa-check
name: Finland corporate additional prepayment and relief interest
inputs:
  tax_liability: 20000
  paid_advances: 15000
  interest_days: 13
  annual_rate: 0.045
  calendar_days: 365
steps:
  additional_tax: tax_liability - paid_advances
  relief_interest: round(additional_tax * interest_days * annual_rate / calendar_days, 2)
  total_due: additional_tax + relief_interest
expected:
  additional_tax: 5000
  relief_interest: 8.01
  total_due: 5008.01
```

## Ask the client first

- Which taxpayer, tax year, accounting periods and assessment end date apply?
- What are the supported full-year income, deduction and tax-credit calculations?
- Which withholding, advances, references and remaining instalments already exist?
- Has Vero issued a replacement decision, or is a change only requested?
- Is the request in-year, an additional prepayment or an adjustment of completed assessment?
- Are foreign income, seasonal months or payment difficulty involved?

## Sources

| Official source | Provisions read | Read date |
|---|---|---|
| [Prepayment Act 1118/1996][law] | §§1–3,13,23–25: advance collection and revision | 2026-10-26 |
| [Vero instalment table][instalments] | Individual and corporate minimums, bands and scheduling | 2026-10-26 |
| [Vero payment instructions][payments] | Due day, revisions and forecasts | 2026-10-26 |
| [Vero additional prepayment][additional] | Requests, tax year and payment procedure | 2026-10-26 |
| [Vero interest guidance][relief] | 2026 rates, periods and EUR 20 distinction | 2026-10-26 |
| [Vero prepayment register][register]; [if you pay late][late]; [claim for adjustment][adjust]; [back taxes][backtax]; [tax prepayment][prepayment-home] | Withholding rates, payment allocation, 60-day claim, back-tax instalments, wage-card route | 2026-10-27 |

Not yet confirmed: 2027 interest rates and the exact December 2026 opening day for individual 2026 additional-prepayment requests. These are future parameters; they do not change the confirmed 2026 procedures.

[law]: https://www.finlex.fi/fi/lainsaadanto/1996/1118
[instalments]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/tax-prepayment/instructions-for-making-prepayments/how-many-instalments/
[payments]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/tax-prepayment/instructions-for-making-prepayments/
[additional]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/tax-prepayment/additional-prepayment/
[relief]: https://www.vero.fi/en/businesses-and-corporations/taxes-and-charges/tax-prepayment/additional-prepayment/late-payment-interest-with-relief/

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-27. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `fi-prepayments` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/fi-prepayments. If neither is available, confirm every figure against the official source pages cited above before relying on it.
