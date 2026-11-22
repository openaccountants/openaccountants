---
name: us-gaap-asc350-goodwill-and-intangibles
description: "Draft US GAAP goodwill and intangible-asset working paper: separates general impairment from eligible private-company amortization and triggering-event elections, calculates capped goodwill losses and amortization, and holds unrecovered current intangible recognition/measurement rules. Load financial-reporting-workflow-base."
jurisdiction: US
category: financial-statements
domain: financial-reporting
type: computation
standard: "ASC 350 Intangibles\u2014Goodwill and Other (ASU 2017-04 and ASU 2021-03 amendment basis)"
effective_date: 2022-12-16
tier: 2
status: needs_sources
last_updated: 2026-11-22
version: 0.1
depends_on:
  - financial-reporting-workflow-base
---

# US GAAP goodwill and intangibles : ASC 350 v0.1

> **General reference only.** Draft working papers for AI-assisted accounting; no accountant has approved this version. Outputs need a qualified professional's review for the entity's actual facts.

## Scope

**Publication hold.** Current authoritative Codification access is unresolved. This file is held with `status: needs_sources`; do not publish it as a complete current-US-GAAP method. The specifically cited FASB Updates support the amendment-basis research below, not an assertion that every intervening amendment has been incorporated. Unrecovered conclusions are listed individually under Sources and are not usable instructions.

Load `financial-reporting-workflow-base`. Prepare a source-linked working paper, proposed balanced journal entries, disclosure checklist and reviewer brief. Keep assumptions separate from source-confirmed rules. Do not issue financial statements, an audit opinion or a tax return from this file.

This is subsequent-accounting work. `us-gaap-asc805-business-combinations` owns acquisition recognition/allocation; `us-gaap-software-development-costs` owns internal-use/external-use software. Do not treat every intangible asset as goodwill or apply goodwill's model to every intangible.

The date key 2022-12-16 identifies the first possible period start after 15 December 2022 for the amended general impairment test for entities other than SEC-filer PBEs excluding eligible smaller reporting companies. That SEC group uses periods beginning after 15 December 2019, with the SRC status determination as of 15 November 2019. This corrected timing is reproduced in ASU 2021-03; do not rely on the superseded original nonpublic dates in ASU 2017-04. Application is prospective; permitted early measurement dates begin on or after 1 January 2017. [ASU 2021-03, 350-20-65-3](https://storage.fasb.org/ASU%202021-03.pdf).

## Ask the client first

- Acquisition allocation, recognized goodwill and separately identified intangibles; opening balances and prior impairment.
- Entity eligibility and actual goodwill amortization and triggering-event policy elections.
- Reporting units/entity-level test election, allocated carrying amounts and supported fair values.
- Reporting date, acquisition date, amortization start, useful lives and elapsed service period.
- Triggering events, market/operating evidence and results of other asset impairment tests.
- Whether goodwill is tax deductible, relevant deferred taxes and specialist valuation/tax support.

## The method, step by step

1. **Identify the accounting branch.** Under the read general guidance, recognized goodwill is not amortized and is tested at least annually, with interim testing when required. An eligible private company or not-for-profit may instead elect the amortization alternative, and may separately elect the reporting-period-end triggering-event evaluation alternative. These are distinct policies; election of one neither requires nor prevents the other. Document eligibility and the full elected requirements. [ASU 2017-04, 350-20-35-1/-35-30](https://storage.fasb.org/ASU2017-04.pdf); [ASU 2021-03, 350-20-15-4 through -15-6](https://storage.fasb.org/ASU%202021-03.pdf).
2. **Prepare the general impairment assessment.** A permitted qualitative assessment considers whether it is more likely than not that reporting-unit fair value is below carrying amount; the read definition is a likelihood above 50%. The entity may bypass that assessment and perform the quantitative test. For the quantitative calculation, compare reporting-unit carrying amount including goodwill with fair value, limiting the loss to allocated goodwill. The old implied-goodwill second step is removed. [ASU 2017-04, 350-20-35-3A/-35-3B, -35-4/-35-8](https://storage.fasb.org/ASU2017-04.pdf).
3. **Do not ignore tax effects.** If goodwill is tax deductible, an impairment can change deferred taxes and the reporting-unit carrying amount; the read rule requires the associated tax-effect calculation, still subject to the goodwill cap. The simple example below expressly assumes no such tax effect. After recognition, the adjusted goodwill is its new basis and the read rule prohibits subsequent reversal. [ASU 2017-04, 350-20-35-8B, -35-12/-35-13](https://storage.fasb.org/ASU2017-04.pdf).
4. **For an elected amortization alternative, schedule each amortizable unit.** The read rule uses straight-line amortization over 10 years, or a shorter life if demonstrated more appropriate. Apply the actual policy consistently to relevant existing and future goodwill; choose entity-level or reporting-unit impairment testing as required. The optional reporting-period-end trigger assessment is not an election to skip a required triggered impairment. [ASU 2021-03, 350-20-15-5, -35-63/-35-65/-35-66](https://storage.fasb.org/ASU%202021-03.pdf).
5. **Coordinate other assets.** In the read alternative guidance, when other assets/groups and goodwill are tested together, test the other assets first and reflect any loss before testing goodwill. Keep finite-lived and indefinite-lived intangible work separate; their current recognition, useful-life, amortization and impairment rules remain held below. Do not use the goodwill cap or amortization election for an unrelated brand/patent/customer asset. [ASU 2021-03, 350-20-35-79](https://storage.fasb.org/ASU%202021-03.pdf).
6. **Return the rollforward and disclosures list.** Reconcile opening goodwill/intangibles, acquisitions, allocations, amortization, disposals and impairment to closing balances. Identify each valuation assumption, source/current-text hold and required disclosure still to be sourced. No internally created goodwill asset is manufactured from a valuation: the read overview states those development/maintenance/restoration costs are not capitalized. [ASU 2021-03, 350-20-05-4A](https://storage.fasb.org/ASU%202021-03.pdf).

## Worked cases

All balances, lives and policy elections are hypothetical and require separate current-source clearance.

**General-model goodwill cap.** After all required prior tests and with no goodwill-related tax effect, reporting-unit carrying amount is $300,000 including $40,000 goodwill; fair value is $250,000. Excess carrying amount is $50,000, but the goodwill loss is capped at $40,000. Propose Dr goodwill impairment expense / Cr goodwill $40,000; remaining goodwill is zero. The remaining $10,000 reporting-unit deficit is not another goodwill write-down; assess other relevant rules separately.

```oa-check
name: General goodwill test caps loss at allocated goodwill
inputs:
  unit_carrying_amount: 300000
  unit_fair_value: 250000
  allocated_goodwill: 40000
steps:
  - excess: max(0, unit_carrying_amount - unit_fair_value)
  - impairment: min(excess, allocated_goodwill)
  - closing_goodwill: allocated_goodwill - impairment
expected:
  excess: 50000
  impairment: 40000
  closing_goodwill: 0
```

**Eligible private-company alternative.** Assume an eligible entity has properly elected the amortization alternative, has $200,000 newly recognized goodwill and supports the 10-year period, with six months elapsed and no required impairment. Annual amortization is $20,000, half-year cost $10,000 and closing goodwill $190,000. Propose Dr amortization expense / Cr accumulated goodwill amortization $10,000. Under the general nonamortization model the same mere passage of six months would not cause that amortization; the election changes the method.

```oa-check
name: Elected eligible goodwill amortization alternative
inputs:
  goodwill: 200000
  supported_life_years: 10
  months_elapsed: 6
steps:
  - annual_amortization: goodwill / supported_life_years
  - period_amortization: annual_amortization * months_elapsed / 12
  - closing_goodwill: goodwill - period_amortization
expected:
  annual_amortization: 20000
  period_amortization: 10000
  closing_goodwill: 190000
```

## When to refuse or refer

Hold missing allocations, reporting-unit definitions, valuation or election evidence. Refer tax-deductible goodwill calculations, alternative eligibility/transition, private-to-public changes, indefinite-lived intangible impairment, acquisition accounting and valuation. A goodwill impairment worksheet does not clear a business combination's initial accounting.

## Sources

| Official source | Passages actually read | Read date |
|---|---|---|
| [ASU 2017-04](https://storage.fasb.org/ASU2017-04.pdf) | 350-20-35-1 through -35-8B, -35-12/-35-13 and -35-30; general measurement redline visually checked. Original transition later superseded in relevant respects. | 2026-11-21 |
| [ASU 2021-03](https://storage.fasb.org/ASU%202021-03.pdf) | 350-20-05-4A; -15-4 through -15-6; -35-62 through -35-67, -35-79; -65-3/-65-4. Election branches, amortization and corrected general-test dates. | 2026-11-22 |

**Not yet confirmed:** Complete current ASC 350 and all later amendments; reporting-unit identification/allocation and full valuation/disclosure guidance; tax-deductible goodwill computation; finite-/indefinite-lived intangible initial recognition, useful life, amortization and impairment; all alternative transition/eligibility consequences beyond the passages read. These items are non-usable holds. Original ASU 2014-02 and ASU 2012-02 downloads failed and are not represented as read. Official current ASC attempt on 2026-11-21 stopped at CAPTCHA/terms.
