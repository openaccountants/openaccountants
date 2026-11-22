---
name: us-gaap-asc718-share-based-compensation
description: "Draft issuer working paper for US GAAP stock options, RSUs and other share-based awards: scope, equity and liability gates, service and performance conditions, forfeitures, journal entries and disclosures. Based on named FASB amendments with explicit current-Codification source holds. Load financial-reporting-workflow-base."
jurisdiction: US
category: financial-statements
domain: financial-reporting
type: computation
standard: "ASC 718 Compensation\u2014Stock Compensation (ASU 2018-07 and ASU 2024-01 amendment basis)"
effective_date: 2025-12-16
tier: 2
status: needs_sources
last_updated: 2026-11-22
version: 0.1
depends_on:
  - financial-reporting-workflow-base
---

# US GAAP share-based compensation : ASC 718 v0.1

> **General reference only.** Draft working papers for AI-assisted accounting; no accountant has approved this version. Outputs need a qualified professional's review for the entity's actual facts.

## Scope

**Publication hold.** Current authoritative Codification access is unresolved. This file is held with `status: needs_sources`; do not publish it as a complete current-US-GAAP method. The specifically cited FASB Updates support the amendment-basis research below, not an assertion that every intervening amendment has been incorporated. Unrecovered conclusions are listed individually under Sources and are not usable instructions.

Load `financial-reporting-workflow-base`. Prepare a source-linked working paper, proposed balanced journal entries, disclosure checklist and reviewer brief. Keep assumptions separate from source-confirmed rules. Do not issue financial statements, an audit opinion or a tax return from this file.

This job concerns the issuer's compensation cost, not the employee's tax. The date key 2025-12-16 marks the first possible annual-period start after 15 December 2025 for ASU 2024-01's non-PBE transition; PBEs apply it for annual periods beginning after 15 December 2024, including interim periods. Early adoption and prospective/retrospective choices require the transition conditions. It illustrates profits-interest scope without changing the underlying scope principle. [ASU 2024-01, 718-10-15-3 and -65-17](https://storage.fasb.org/ASU%202024-01.pdf).

## Ask the client first

- Award agreement, grant approval, side letters, modifications, grant date and financial-reporting date.
- Employee, supplier or customer relationship; entity's PBE status and relevant adoption elections.
- Cash or share settlement, repurchase rights, dividends, exercise price and any indexed features.
- Number of awards, service period, graded or cliff vesting, service/performance/market conditions and forfeiture policy.
- Grant-date valuation, current valuation for liabilities, service delivered and previously recognized cost.
- Whether the services construct another asset; tax and payroll consequences for a separate specialist.

## The method, step by step

1. **Route before measuring.** Collect the complete contract and document whether it falls within ASC 718. Legal labels such as RSU, profits interest or phantom stock do not decide the answer. The read ASU 2024-01 adds scope illustrations; it does not make every profits interest an equity award. Determine current equity/liability classification and grant date before calculating cost. Those full conclusions remain held below. [ASU 2024-01, 718-10-15-3 and -55-138 onward](https://storage.fasb.org/ASU%202024-01.pdf).
2. **Identify the measurement input.** Under the read amendment, equity compensation generally uses grant-date fair value, net of consideration the grantee pays for the instrument. An option's exercise price is not its fair value. Use an appropriately supported valuation; this Guide does not perform an option valuation or turn a tax valuation into an accounting valuation. [ASU 2018-07, 718-10-30-2 through -30-6](https://storage.fasb.org/ASU%202018-07.pdf).
3. **Build the service schedule.** For an employee award already concluded to be equity, recognize compensation cost over its requisite service period with a credit to equity. The debit is expense or an eligible asset cost, depending on the services received. For a simple cliff award, allocate the supported compensation amount over the service period; use the actual period elapsed and subtract cost already recognized to obtain the current entry. Do not apply that simple schedule automatically to graded awards. [ASU 2018-07, 718-10-25-2A, -35-2 and -35-8](https://storage.fasb.org/ASU%202018-07.pdf).
4. **Keep vesting conditions separate.** The read performance-condition guidance makes accrual depend on the probable outcome; a change in the estimate produces a cumulative catch-up. Service/performance vesting conditions are not incorporated into grant-date fair value in the same way as market conditions. A market-condition failure alone is not treated as a forfeiture. Recover the precise current award provisions before applying these distinctions. [ASU 2018-07, 718-10-25-20, -30-27 through -30-28](https://storage.fasb.org/ASU%202018-07.pdf).
5. **Apply the actual forfeiture election.** For employee awards the read amendment permits an entity-wide policy of estimating service forfeitures or accounting for them when they occur. Under the latter, reverse previously recognized cost if the requisite service is not provided. Do not reverse cost merely because a vested option expires unexercised. Nonemployee elections and recognition are separately addressed. [ASU 2018-07, 718-10-35-1D through -35-1F and -35-3](https://storage.fasb.org/ASU%202018-07.pdf).
6. **Return the reviewer package.** Reconcile opening awards, grants, forfeitures, exercises/settlements and closing awards; separately reconcile recognized and unrecognized cost. Identify capitalization, valuation, liability remeasurement, modification and tax questions as separate workstreams. Do not infer that no cash payment means no compensation cost.

### Later amendment boundary

ASU 2025-04 addresses share-based consideration payable to a customer. Its new customer-related performance-condition definition cannot be applied by analogy to employee or supplier compensation. It retains separate employee/nonemployee service-forfeiture elections. It is effective for annual reporting periods beginning after 15 December 2026, including interim periods, with permitted early adoption subject to its transition provisions. Do not silently apply its customer rules to the employee cases below. [ASU 2025-04, Summary and 606-10-65-2](https://storage.fasb.org/ASU%202025-04.pdf).

## Worked cases

All amounts, periods and rates are hypothetical input facts; neither case supplies a valuation or clears the current-source gate.

**Simple service-only cliff award.** Assume an employee's 12,000 options are equity, grant-date fair value is $4 per option, no payment is made for the grant, requisite service is 48 months, service is rendered evenly, and the entity accounts for forfeitures when they occur. With no forfeiture and 12 months completed, cumulative cost is $12,000. With no opening cost, propose Dr compensation expense / Cr additional paid-in capital $12,000, assuming the services do not qualify for capitalization.

```oa-check
name: Equity cliff award service schedule with supplied valuation
inputs:
  awards: 12000
  fair_value_per_award: 4
  total_months: 48
  elapsed_months: 12
  previously_recognized: 0
steps:
  - total_cost: awards * fair_value_per_award
  - cumulative_cost: total_cost * elapsed_months / total_months
  - current_cost: cumulative_cost - previously_recognized
expected:
  total_cost: 48000
  cumulative_cost: 12000
  current_cost: 12000
```

**Forfeiture boundary.** Assume 3,000 of those awards are forfeited after the first service year, before any further service cost is booked. Under the stated as-occurs policy, reverse the $3,000 previously recognized for them: Dr additional paid-in capital / Cr compensation expense $3,000. Remaining cumulative cost is $9,000. If the employee had instead completed the requisite service and merely let vested options lapse, the read rule would not permit that reversal.

```oa-check
name: As-occurs forfeiture before service is completed
inputs:
  forfeited_awards: 3000
  fair_value_per_award: 4
  elapsed_months: 12
  total_months: 48
  opening_cumulative_cost: 12000
steps:
  - reversal: forfeited_awards * fair_value_per_award * elapsed_months / total_months
  - remaining_cumulative_cost: opening_cumulative_cost - reversal
expected:
  reversal: 3000
  remaining_cumulative_cost: 9000
```

## When to refuse or refer

Hold booking conclusions where the grant date, classification, valuation, service conditions or current operative text is unresolved. Refer cash-settled awards, complex modifications, market conditions, repurchase features, graded attribution, private-company valuation expedients and tax/payroll effects. Do not treat employee income-tax treatment as ASC 718 expense recognition. The existing `us-gaap-debt-vs-equity` handles financing-instrument classification; this job handles compensation only.

## Sources

| Official source | Passages actually read | Read date |
|---|---|---|
| [ASU 2018-07](https://storage.fasb.org/ASU%202018-07.pdf) | 718-10-25-2 through -25-3, -25-20; -30-2 through -30-8, -30-27/-28; -35-1A through -35-3, -35-5/-35-8. Amendment-basis recognition, measurement and attribution. | 2026-11-21 |
| [ASU 2024-01](https://storage.fasb.org/ASU%202024-01.pdf) | Summary; 718-10-15-3 scope clarification; transition summary. No blanket profits-interest conclusion. | 2026-11-21 |
| [ASU 2025-04](https://storage.fasb.org/ASU%202025-04.pdf) | Summary distinguishing customer consideration from employee/supplier awards and effective/transition summary. | 2026-11-21 |

**Not yet confirmed:** Current ASC 718 complete scope and definitions; grant-date prerequisites; complete equity/liability classification; current liability measurement and private-company expedients; modification/cancellation rules; all disclosure requirements; tax/payroll treatment; applicability of intervening amendments beyond the passages read. These are non-usable holds, not presumed conclusions. Official ASC access was attempted on 2026-11-21 and stopped at its CAPTCHA/terms screen, not read as authoritative text.
