---
name: us-gaap-asc326-receivable-credit-losses
description: "Draft CECL working paper for US GAAP trade receivables and contract assets, including risk pooling, adjusted loss rates, individual exposures, allowance entries and the ASU 2025-05 current-receivable expedient and non-PBE subsequent-collection election. Current consolidated ASC source hold remains. Load financial-reporting-workflow-base."
jurisdiction: US
category: financial-statements
domain: financial-reporting
type: computation
standard: "ASC 326-20 Financial Instruments\u2014Credit Losses\u2014Measured at Amortized Cost (ASU 2016-13 and ASU 2025-05 amendment basis)"
effective_date: 2025-12-16
tier: 2
status: needs_sources
last_updated: 2026-11-22
version: 0.1
depends_on:
  - financial-reporting-workflow-base
---

# US GAAP credit losses on receivables : ASC 326 v0.1

> **General reference only.** Draft working papers for AI-assisted accounting; no accountant has approved this version. Outputs need a qualified professional's review for the entity's actual facts.

## Scope

**Publication hold.** Current authoritative Codification access is unresolved. This file is held with `status: needs_sources`; do not publish it as a complete current-US-GAAP method. The specifically cited FASB Updates support the amendment-basis research below, not an assertion that every intervening amendment has been incorporated. Unrecovered conclusions are listed individually under Sources and are not usable instructions.

Load `financial-reporting-workflow-base`. Prepare a source-linked working paper, proposed balanced journal entries, disclosure checklist and reviewer brief. Keep assumptions separate from source-confirmed rules. Do not issue financial statements, an audit opinion or a tax return from this file.

This job estimates an allowance, rather than deciding that revenue was valid or collecting the debt. Load `us-gaap-asc606-revenue` for revenue recognition and concessions. Exclude loans purchased for investment, available-for-sale debt securities, off-balance-sheet commitments and specialized collateral/PCD methods from this focused receivables worksheet.

The date key 2025-12-16 identifies the first possible annual-period start after 15 December 2025 for ASU 2025-05, including interim periods. Its optional amendments apply prospectively, with early adoption permitted for unissued/not-available interim or annual statements. This is not the original universal CECL adoption date. [ASU 2025-05, Summary and 326-10-65-6](https://storage.fasb.org/ASU%202025-05.pdf).

## Ask the client first

- Reconciled gross receivables/contract assets, invoice terms, reporting date, contractual lives and aging.
- Origin of balances under ASC 606, current/noncurrent classification, operating cycle and PBE status.
- Actual ASU 2025-05 adoption, expedient/policy elections and subsequent-collection cutoff.
- Historical losses/recoveries, pool definitions and changes in customer/credit-policy mix.
- Current customer distress, economic conditions, forecast support and individually assessed exposures.
- Opening allowance, writeoffs/recoveries, collections by invoice and statements' available-to-issue date.

## The method, step by step

1. **Reconcile and scope.** Tie gross amortized-cost balances to the subledger and remove duplicates, settled items and balances outside the assessment. An allowance is separate from a revenue price concession. Under the read amendment, the allowance reduces amortized cost to the amount expected to be collected, with changes in credit-loss expense. [ASU 2016-13, 326-20-30-1 and -35-1](https://storage.fasb.org/ASU%202016-13.pdf).
2. **Pool only comparable risks.** Assess similar-risk balances collectively; assess an exposure individually if it does not share the pool's risks, removing it from the pool. Reassess migration at every reporting date. Do not reserve the same invoice both individually and in an aging bucket. [ASU 2016-13, 326-20-30-2 and -35-2](https://storage.fasb.org/ASU%202016-13.pdf).
3. **Support the estimate.** Aging/loss-rate methods are permitted examples, not mandatory rates. Start with relevant history, adjust for current portfolio/credit differences and reasonable/supportable forecasts, then apply the required historical reversion beyond the supported forecast period. Do not insert a generic industry percentage. The read standard does not permit omitting loss risk merely because it is remote; a supported zero-loss expectation is a different conclusion. [ASU 2016-13, 326-20-30-3, -30-7 through -30-10](https://storage.fasb.org/ASU%202016-13.pdf).
4. **Evaluate the adopted current-receivable expedient.** ASU 2025-05 permits all entities to elect a constant-current-conditions forecast assumption for current ASC 606 receivables/contract assets. Historical loss data still needs current-condition adjustments. Apply consistently to all qualifying balances. Current means the one-year period, unless the operating cycle exceeds 12 months, when the longer cycle applies. Distressed customers do not disappear under the expedient. [ASU 2025-05, 326-20-30-10A through -30-10D](https://storage.fasb.org/ASU%202025-05.pdf).
5. **Apply subsequent collections only with the separate eligible election.** An entity other than a PBE that elects the expedient may also elect to consider collections through the available-to-issue date or an earlier selected date after the balance sheet date. Remove collected amounts from loss exposure; evaluate only remaining balance-sheet-date amounts using delinquency at that cutoff and the expedient. Updating historical loss rates for subsequent collections is permitted, not required. Disclose the elections and, annually, the collection cutoff. This is not a general license for PBEs to use later receipts. [ASU 2025-05, 326-20-30-10E through -30-10H and -50-12A/-50-12B](https://storage.fasb.org/ASU%202025-05.pdf).
6. **Post the movement, not the ending allowance twice.** Roll opening allowance forward for actual writeoffs and recoveries, then compare the pre-adjustment balance to the required estimate. A needed increase is Dr credit-loss expense / Cr allowance; a decrease reverses expense. Under the read writeoff rule, write off uncollectible financial assets against the allowance rather than charging the same loss again. Current recovery refinements beyond the read passages remain held. [ASU 2016-13, 326-20-35-1 and -35-8](https://storage.fasb.org/ASU%202016-13.pdf).

## Worked cases

All balances, losses and rates are hypothetical evidence inputs, not statutory rates.

**Pools plus an individual exposure.** A cleared ordinary-receivable estimate has a $200,000 pool at a supported 1% adjusted loss rate and a separate distressed $20,000 invoice with $8,000 expected collection. Required allowance is $14,000. The invoice is excluded from the pool. If the pre-adjustment allowance is $5,000 after writeoffs/recoveries, propose Dr credit-loss expense / Cr allowance $9,000.

```oa-check
name: No double counting between a receivable pool and individual assessment
inputs:
  pooled_receivables: 200000
  adjusted_loss_rate: 0.01
  distressed_invoice: 20000
  expected_individual_collection: 8000
  pre_adjustment_allowance: 5000
steps:
  - pool_allowance: pooled_receivables * adjusted_loss_rate
  - individual_allowance: distressed_invoice - expected_individual_collection
  - required_allowance: pool_allowance + individual_allowance
  - additional_expense: required_allowance - pre_adjustment_allowance
expected:
  pool_allowance: 2000
  individual_allowance: 12000
  required_allowance: 14000
  additional_expense: 9000
```

**Non-PBE election and cutoff boundary.** Assume adopted ASU 2025-05, both eligible elections, a valid cutoff before statements are available to issue, $100,000 qualifying balance-sheet-date receivables and $60,000 collected by cutoff. A supported 6% loss estimate applies to the remaining $40,000 based on its cutoff delinquency and balance-sheet-date current conditions. Required allowance is $2,400. The $60,000 collected carries no allowance under this election. Do not replace gross balance-sheet receivables with only the uncollected amount; this election affects the allowance estimate, not the historical receivable balance.

```oa-check
name: Eligible subsequent-collections election retains only remaining loss exposure
inputs:
  balance_sheet_receivables: 100000
  qualifying_collections: 60000
  supported_remaining_loss_rate: 0.06
steps:
  - uncollected_exposure: balance_sheet_receivables - qualifying_collections
  - required_allowance: uncollected_exposure * supported_remaining_loss_rate
  - net_balance_sheet_receivables: balance_sheet_receivables - required_allowance
expected:
  uncollected_exposure: 40000
  required_allowance: 2400
  net_balance_sheet_receivables: 97600
```

## When to refuse or refer

Hold if the subledger, risks, forecast, elections or collection cutoff cannot be supported. Refer purchased loans/PCD, collateral-dependent assets, receivable sales, factoring, off-balance-sheet commitments and disputes over whether the amount is revenue. An aging schedule without loss-history/current-condition evidence is not a completed estimate.

## Sources

| Official source | Passages actually read | Read date |
|---|---|---|
| [ASU 2016-13](https://storage.fasb.org/ASU%202016-13.pdf) | 326-20-30-1 through -30-10; -35-1/-35-2 and -35-8. Original amendment-basis allowance, methods and movements, not all subsequent refinements. | 2026-11-21 |
| [ASU 2025-05](https://storage.fasb.org/ASU%202025-05.pdf) | Summary; 326-20-30-7 through -30-10H; -50-12A/-50-12B; illustrative example introduction; transition summary. | 2026-11-21 |

**Not yet confirmed:** Complete current ASC 326 text and intervening amendments; current detailed recovery, contractual-term and scope exceptions; original entity-specific CECL transition; applicability of later purchased-loan amendments to assets outside this job. Full current-ASC signoff remains held. The direct/browser ASC attempt on 2026-11-21 stopped at CAPTCHA/terms. The specifically read optional amendment does not clear unrelated 326 methods.
