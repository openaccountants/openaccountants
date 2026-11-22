---
name: us-gaap-asc360-fixed-assets-and-impairment
description: "Publication-held draft US GAAP fixed-asset working paper: register and depreciation recomputation, held-for-sale evidence, disposal presentation and a clearly historical impairment-model comparison. Current initial-cost, depreciation and ASC 360 impairment conclusions await authoritative sources. Load financial-reporting-workflow-base."
jurisdiction: US
category: financial-statements
domain: financial-reporting
type: computation
standard: "ASC 360 Property, Plant, and Equipment (ASU 2014-08 disposal-presentation amendment basis)"
effective_date: 2014-12-15
tier: 2
status: needs_sources
last_updated: 2026-11-22
version: 0.1
depends_on:
  - financial-reporting-workflow-base
---

# US GAAP fixed assets and impairment : ASC 360 v0.1

> **General reference only.** Draft working papers for AI-assisted accounting; no accountant has approved this version. Outputs need a qualified professional's review for the entity's actual facts.

## Scope

**Publication hold.** Current authoritative Codification access is unresolved. This file is held with `status: needs_sources`; do not publish it as a complete current-US-GAAP method. The specifically cited FASB Updates support the amendment-basis research below, not an assertion that every intervening amendment has been incorporated. Unrecovered conclusions are listed individually under Sources and are not usable instructions.

Load `financial-reporting-workflow-base`. Prepare a source-linked working paper, proposed balanced journal entries, disclosure checklist and reviewer brief. Keep assumptions separate from source-confirmed rules. Do not issue financial statements, an audit opinion or a tax return from this file.

Prepare the fixed-asset register, depreciation reconciliation, impairment evidence and disposal worksheet. The date key 2014-12-15 is the first permitted annual-period start in ASU 2014-08's mandatory transition: annual periods beginning on or after 15 December 2014. Its entity/interim and transaction transition conditions must be checked; this is not a claim that all of ASC 360 became effective then. The original cost/depreciation and complete current impairment rules are not cleared by that Update. [ASU 2014-08 transition summary and 205-20-65-1](https://storage.fasb.org/ASU%202014-08.pdf).

## Ask the client first

- Register, opening cost/accumulated depreciation, invoices, construction costs, disposals and ownership evidence.
- Actual in-service dates, asset components, approved useful lives, residual values, depreciation method and capitalization policy.
- Adverse operational/market changes, damage, idle or abandoned assets and management plans.
- Supported asset-group cash flows, independence of those flows, valuations and related liabilities.
- Sale approval, buyer search, marketing price, expected timing and conditions delaying completion.
- Prior impairment, tax basis, held-for-sale/discontinued-operation conclusions and prior entries.

## The method, step by step

1. **Reconcile the register.** Opening cost plus supported additions less disposed cost must equal closing cost. Separately reconcile accumulated depreciation, impairment and net book value. Recompute the entity's approved depreciation schedule from actual in-service dates and supported assumptions. This arithmetic does not establish that the cost, life, residual value or method complies with current ASC; obtain the sources listed below before approving those policies.
2. **Separate use, sale and abandonment evidence.** The read disposal guidance treats abandonment and other nonsale disposals as held and used until disposal, rather than automatically held for sale. Do not infer depreciation cessation from idling or an intention to sell; obtain the held current depreciation and held-for-sale rules before deciding. The current depreciation/impairment consequences require their separately held rules. [ASU 2014-08, 360-10-45-15](https://storage.fasb.org/ASU%202014-08.pdf).
3. **Check every held-for-sale condition.** Under the reproduced 360-10-45-9, require authorized commitment to a plan, immediate availability subject only to usual/customary terms, an active buyer/completion program, probable completed sale within one year subject to the specified exceptions, reasonable active marketing price, and actions making significant plan change/withdrawal unlikely. A listing alone is insufficient. The one-year exceptions require the actual 360-10-45-11 conditions, not a generic extension whenever convenient. [ASU 2014-08, 360-10-45-9/-45-11](https://storage.fasb.org/ASU%202014-08.pdf).
4. **Prepare the impairment evidence without clearing a current rule.** Retain carrying amounts, proposed grouping, expected cash-flow support, trigger evidence and valuation. For comparison only, historical FAS 144 paragraphs 7–10 used an undiscounted recoverability gate followed by a fair-value loss measurement and addressed cash-flow grouping. That pre-Codification document is superseded as a source of current authoritative GAAP; do not turn the historical comparison or case below into a current ASC 360 booking instruction. Current recognition, cash-flow construction, allocation and reversal conclusions remain non-usable holds. [Historical FAS 144, paragraphs 7–10](https://storage.fasb.org/fas144.pdf).
5. **Keep presentation separate from measurement.** The read 360-10-45-5 places an ordinary long-lived-asset sale gain/loss that is not a discontinued operation in continuing operations before income taxes, included in operating income if that subtotal is shown. The read held-for-sale presentation keeps assets/liabilities of a disposal group separate, without netting. Discontinued-operations eligibility is a separate ASC 205-20 question. [ASU 2014-08, 360-10-45-5 and -45-14](https://storage.fasb.org/ASU%202014-08.pdf).
6. **Return the review package.** Give a rollforward, conditional depreciation/impairment worksheets, proposed entry only where the underlying measurement has been independently cleared, and the unresolved policy/source list. Link the impairment work to `us-gaap-asc350-goodwill-and-intangibles`; do not use the goodwill test for tangible assets.

### Later amendment boundary

ASU 2025-12 removes obsolete 360-10-40-2; it is not a new general disposal-method authorization. Its relevant amendments apply to annual periods beginning after 15 December 2026, including interims, with early adoption and transition options in 105-10-65-10. Recover the operative nonfinancial-asset derecognition requirements rather than relying on the obsolete paragraph. [ASU 2025-12, issue 8 and 105-10-65-10](https://storage.fasb.org/ASU%202025-12.pdf).

## Worked cases

All inputs are hypothetical. These are arithmetic checks on explicit assumptions, not current-ASC clearance.

**Approved-policy depreciation recomputation.** Assume a separately supported straight-line policy, $60,000 eligible cost, $6,000 residual, five-year life and six months in service, with no impairment. Annual depreciation is $10,800 and six-month cost is $5,400, leaving $54,600. Only after the cost/life/method conclusions are cleared, propose Dr depreciation expense / Cr accumulated depreciation $5,400. Tax deductions are a separate calculation.

```oa-check
name: Conditional straight-line fixed-asset schedule
inputs:
  supported_cost: 60000
  supported_residual: 6000
  supplied_life_years: 5
  months_in_service: 6
steps:
  - depreciable_amount: supported_cost - supported_residual
  - annual_depreciation: depreciable_amount / supplied_life_years
  - period_depreciation: annual_depreciation * months_in_service / 12
  - closing_book_value: supported_cost - period_depreciation
expected:
  depreciable_amount: 54000
  annual_depreciation: 10800
  period_depreciation: 5400
  closing_book_value: 54600
```

**Historical impairment-model boundary.** To illustrate the historical model only, assume carrying amount $100,000, undiscounted cash flows $110,000 and fair value $80,000. The historical recoverability headroom is $10,000; the mere $20,000 fair-value shortfall would not itself pass that model's recognition gate. If a separate scenario instead has $90,000 undiscounted cash flows and the same fair value, its historical arithmetic gives a $20,000 loss, not the $10,000 cash-flow shortfall. No current journal is authorized; current scope, grouping, inputs and recognition remain held.

```oa-check
name: Historical comparison separates recoverability from loss measurement
inputs:
  carrying_amount: 100000
  first_scenario_undiscounted: 110000
  second_scenario_undiscounted: 90000
  fair_value: 80000
steps:
  - first_headroom: first_scenario_undiscounted - carrying_amount
  - second_recoverability_shortfall: carrying_amount - second_scenario_undiscounted
  - conditional_historical_loss: carrying_amount - fair_value
expected:
  first_headroom: 10000
  second_recoverability_shortfall: 10000
  conditional_historical_loss: 20000
```

## When to refuse or refer

Refuse a current impairment or policy conclusion using only the historical comparison. Refer new cost policies, capitalization thresholds, major components, borrowing costs, leases, asset retirement obligations, goodwill, specialized assets and discontinued operations. An unsupported fair-value report or optimistic cash-flow spreadsheet does not clear the source/input gates.

## Sources

| Official source | Passages actually read | Read date |
|---|---|---|
| [ASU 2014-08](https://storage.fasb.org/ASU%202014-08.pdf) | 360-10-45-5, -45-9/-45-11, -45-14/-45-15; transition summary. Disposal classification/presentation only. | 2026-11-21 |
| [FAS 144, August 2001](https://storage.fasb.org/fas144.pdf) | Historical paragraphs 7–10, PDF pages 9–10. Superseded pre-Codification source, read only for the expressly historical model comparison. | 2026-11-22 |
| [ASU 2025-12](https://storage.fasb.org/ASU%202025-12.pdf) | Issue 8 removal description; 105-10-65-10 effective and transition text. | 2026-11-21 |

**Not yet confirmed:** Current ASC 360 initial cost, depreciation, useful-life/residual revisions, complete held-and-used impairment model and grouping/cash-flow rules, loss allocation/reversals, held-for-sale measurement/depreciation, disposal recognition and complete disclosures; current ASC 205-20 eligibility. Historical FAS 144 is not current authority. Official current ASC access attempted 2026-11-21 stopped at CAPTCHA/terms. All current conclusions listed here are non-usable holds.
