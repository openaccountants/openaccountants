---
name: us-gaap-asc740-income-provision
description: "Draft US GAAP income-tax provision working paper for temporary differences, deferred tax balances, valuation-allowance inputs, noncurrent presentation and tax disclosures. Distinguishes accounting from return preparation and preserves current-ASC measurement/source holds. Load financial-reporting-workflow-base."
jurisdiction: US
category: financial-statements
domain: financial-reporting
type: computation
standard: "ASC 740 Income Taxes (ASU 2015-17, ASU 2016-16 and ASU 2023-09 amendment basis)"
effective_date: 2025-12-16
tier: 2
status: needs_sources
last_updated: 2026-11-22
version: 0.1
depends_on:
  - financial-reporting-workflow-base
---

# US GAAP income-tax accounting : ASC 740 v0.1

> **General reference only.** Draft working papers for AI-assisted accounting; no accountant has approved this version. Outputs need a qualified professional's review for the entity's actual facts.

## Scope

**Publication hold.** Current authoritative Codification access is unresolved. This file is held with `status: needs_sources`; do not publish it as a complete current-US-GAAP method. The specifically cited FASB Updates support the amendment-basis research below, not an assertion that every intervening amendment has been incorporated. Unrecovered conclusions are listed individually under Sources and are not usable instructions.

Load `financial-reporting-workflow-base`. Prepare a source-linked working paper, proposed balanced journal entries, disclosure checklist and reviewer brief. Keep assumptions separate from source-confirmed rules. Do not issue financial statements, an audit opinion or a tax return from this file.

This job prepares an accounting provision, not the corporate tax return. The date key 2025-12-16 marks the first possible annual-period start after 15 December 2025 for ASU 2023-09's non-PBE disclosure rules. PBEs use annual periods beginning after 15 December 2024; permitted early adoption applies to unissued/not-available annual statements. Application is prospective, with retrospective application permitted. [ASU 2023-09, 740-10-65-9](https://storage.fasb.org/ASU%202023-09.pdf).

## Ask the client first

- Legal entities, tax-paying components, tax jurisdictions, tax status and reporting period; PBE status.
- Signed-off tax-basis schedules and book balances for every asset/liability; current-return calculation and prior provision.
- Reversal periods, applicable enacted law/rates, carryforwards and expiry/utilization restrictions, all supported separately.
- Positive/negative evidence for realizability and the reviewer's valuation-allowance conclusion.
- Uncertain positions, examinations, interest/penalties, acquisitions, equity/OCI items and intercompany transfers.
- Payments and refunds by jurisdiction, prior deferred balances and actual adoption elections.

## The method, step by step

1. **Build the scope and differences register.** The read recognition rule calls for current taxes payable/refundable and deferred tax effects of temporary differences/carryforwards, subject to the specified exceptions. Keep each exception as a separate question; do not infer universal recognition. Book-versus-tax timing differences for accelerated tax depreciation and later-deductible expenses are illustrated in the read amendment. [ASU 2016-16, 740-10-25-2/-25-3 and -25-20 through -25-24](https://storage.fasb.org/ASU%202016-16.pdf).
2. **Classify the reversal, not just the sign.** For each item describe how book recovery/settlement produces future taxable or deductible amounts. An asset's carrying amount above its tax basis may produce future taxable amounts; an accrued expense deductible only upon payment may produce future deductions. Separate permanent items from future reversals. Use the actual law and tax basis, not a generic account-name mapping. [ASU 2016-16, 740-10-25-20/-25-23](https://storage.fasb.org/ASU%202016-16.pdf).
3. **Prepare conditional measurement.** The read implementation guidance requires enacted tax law for recognition/measurement. Obtain current ASC 740-10-30 and the jurisdiction's enacted reversal-period law before setting the rate, measuring carryforwards or deciding a valuation allowance. Once those inputs and conclusions are separately cleared, multiply each supported temporary difference by its applicable rate and reconcile the deferred balance movement. The worked cases demonstrate that arithmetic only. [ASU 2015-17, 740-10-55-1 and -55-15](https://storage.fasb.org/ASU%202015-17.pdf).
4. **Keep presentation boundaries.** In a classified balance sheet, present deferred tax balances as noncurrent. Offset deferred assets, liabilities and related valuation allowance within the same tax-paying component and jurisdiction; do not offset across different components or jurisdictions. This presentation does not determine whether a DTA is realizable. [ASU 2015-17, 740-10-45-4/-45-6](https://storage.fasb.org/ASU%202015-17.pdf).
5. **Prepare the disclosure inputs.** For adopted ASU 2023-09, all entities disclose annual income taxes paid, net of refunds, by federal/national, state and foreign categories; individually disclose jurisdictions at or above 5% of total net taxes paid. Trace numerator and denominator to actual payments/refunds, not provision expense. A non-PBE qualitatively describes significant reconciling categories/jurisdictions; PBEs have a different quantitative reconciliation. The illustration below has a positive denominator; zero or negative totals require a separate supported analysis. [ASU 2023-09, 740-10-50-13 and -50-22/-50-23](https://storage.fasb.org/ASU%202023-09.pdf).
6. **Return the provision bridge.** Show current tax, deferred movement, valuation allowance, tax recorded outside continuing operations, effective-rate reconciliation and cash paid as separate schedules. Do not assume every deferred balance movement belongs in profit or loss. Reconcile each balance to the ledger and the prior provision; identify unresolved items without inserting zero.

### Adoption and exception boundary

The read ASU 2016-16 distinguishes intercompany inventory transfers from other asset transfers; do not eliminate all intercompany tax effects as one rule. ASU 2025-12 corrects intraperiod-allocation implementation guidance in 740-10-55-38(b)(1), effective for annual periods beginning after 15 December 2026, including interims, with permitted early adoption and specified transition choices. That correction does not clear the full intraperiod allocation method here. [ASU 2016-16, 740-10-25-3(e), -25-20(i)](https://storage.fasb.org/ASU%202016-16.pdf); [ASU 2025-12, issue 12 and 105-10-65-10](https://storage.fasb.org/ASU%202025-12.pdf).

## Worked cases

All monetary values, rates and review conclusions below are hypothetical; 25% is a supplied example rate, not a claim about US statutory tax.

**Conditional deferred balance.** A separately reviewed schedule supports a $40,000 taxable temporary difference on equipment, a $12,000 deductible difference on accrued expenses and an applicable 25% enacted reversal rate. Assume no exception, no valuation allowance, one component/jurisdiction and no opening deferred balance. DTL $10,000, DTA $3,000, net noncurrent DTL $7,000. If the reviewer separately confirms the movements belong in continuing operations, propose Dr tax expense $10,000 / Cr DTL $10,000 and Dr DTA $3,000 / Cr tax benefit $3,000.

```oa-check
name: Conditional temporary-difference arithmetic with supplied enacted rate
inputs:
  taxable_difference: 40000
  deductible_difference: 12000
  supplied_rate: 0.25
steps:
  - gross_dtl: taxable_difference * supplied_rate
  - gross_dta: deductible_difference * supplied_rate
  - net_dtl: gross_dtl - gross_dta
expected:
  gross_dtl: 10000
  gross_dta: 3000
  net_dtl: 7000
```

**Offsetting boundary.** The same entity also has a separately measured $4,000 DTA in another jurisdiction. Retain the first jurisdiction's $7,000 DTL and present the second jurisdiction's $4,000 DTA separately; a $3,000 global net liability would hide the required separation. For a separate disclosure illustration, annual net taxes paid are $200,000 and one jurisdiction accounts for $10,000: it meets the inclusive 5% threshold. Do not treat that disclosure threshold as a DTA recognition test.

```oa-check
name: Separate-jurisdiction presentation and inclusive paid-tax threshold
inputs:
  jurisdiction_a_dtl: 10000
  jurisdiction_a_dta: 3000
  jurisdiction_b_dta: 4000
  total_net_paid: 200000
  individual_net_paid: 10000
steps:
  - jurisdiction_a_net_liability: jurisdiction_a_dtl - jurisdiction_a_dta
  - separate_asset: jurisdiction_b_dta
  - threshold_amount: total_net_paid * 0.05
  - individual_percentage: individual_net_paid / total_net_paid * 100
expected:
  jurisdiction_a_net_liability: 7000
  separate_asset: 4000
  threshold_amount: 10000
  individual_percentage: 5
```

## When to refuse or refer

Hold recognition/measurement conclusions until current authoritative rules and actual enacted law are available. Refer uncertain tax positions, valuation allowances, loss/credit limitations, outside-basis differences, acquisitions, intraperiod allocation and international minimum taxes. A mathematically correct deferred balance is not evidence that its tax basis or rate is valid. No filing position is taken; any US federal tax advice requires the fact-specific analysis required by Circular 230 §10.37, separately from this accounting worksheet.

## Sources

| Official source | Passages actually read | Read date |
|---|---|---|
| [ASU 2016-16](https://storage.fasb.org/ASU%202016-16.pdf) | 740-10-25-2/-25-3; -25-20 through -25-24. Recognition, exception boundary and temporary-difference illustrations. | 2026-11-21 |
| [ASU 2015-17](https://storage.fasb.org/ASU%202015-17.pdf) | 740-10-45-4/-45-6; -55-1/-55-15. Noncurrent classification, offsetting and enacted-law/scheduling boundary. Redline visually checked. | 2026-11-21 |
| [ASU 2023-09](https://storage.fasb.org/ASU%202023-09.pdf) | 740-10-50-13, -50-22/-50-23 and -65-9. Read disclosure and transition passages only. | 2026-11-21 |
| [ASU 2025-12](https://storage.fasb.org/ASU%202025-12.pdf) | Issue 12 description; 105-10-65-10 effective/early-adoption and transition text. | 2026-11-21 |

**Not yet confirmed:** Current ASC 740 full scope/exceptions; complete enacted-rate and reversal measurement requirements; valuation-allowance probability/evidence test; uncertain-tax-position recognition/measurement; carryforward restrictions; intraperiod allocation; full PBE reconciliation; actual jurisdiction tax law/rates and complete intervening-amendment applicability. None is cleared by the conditional examples. Official ASC access attempted 2026-11-21 stopped at CAPTCHA/terms. The Circular 230 reference is a referral boundary, not a tax-advice method.
