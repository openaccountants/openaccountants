---
name: yt-employer-payroll-relief
description: >
  Mayotte employer relief reference for 2026 employment periods. Routes RGDU and LODEOM by commencement, local minimum wage, employer and employee conditions, contribution limits and noncumulation. Preserves the coefficient illustrations as algebra with explicit assumptions. Identifies the LODEOM schedules without treating their endpoints as eligibility or a complete payroll calculation. DSN codes, a full contribution calculation, special employment adjustments and emergency cyclone measures require separate evidence. Source review of this bounded scope is complete; professional approval remains pending.
version: 0.3
jurisdiction: YT
tax_year: 2026
last_updated: 2026-11-17
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: tax
type: situation-rules
---

# Mayotte: RGDU and LODEOM employer relief

## Scope

This Guide covers the 2026 Mayotte employer-relief framework and a bounded RGDU coefficient illustration. It does not calculate a payslip or establish every contribution base, employee entitlement or declaration field. It remains a source-cited draft without professional approval.

## Ask the client first

- Which employment periods and Mayotte establishment are involved?
- What are the employee's remuneration, hours, absences and contract type?
- What local minimum-wage amounts and eligible employer contribution rates apply to those periods?
- What activity does the employee perform, and what are the employer's sector, workforce and turnover?
- Which reliefs have already been claimed, and are the employer's filing and payment obligations current?
- Are temporary work, paid-leave funds, a repayment plan, a criminal finding or emergency measures relevant?

## The method, step by step

### Employment period and relief

| Rule | Conditions for 2026 | Official source |
|---|---|---|
| RGDU begins with January employment | Use the employment period, not the later payment date | [Decree 2026-82, art. 3 I](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053465499) |
| LODEOM begins with 1 July employment | CSSM identifies the first declaration at the August due date; this is not a complete DSN calendar | [Art. 3 II](https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053465499), [CSSM, June update](https://www.cssm.fr/actualite/deux-dispositifs-majeurs-dexonerations-sociales-sont-desormais-applicables-a-mayotte) |
| RGDU and LODEOM cannot be combined | Do not add both reductions for the same employment | [CSSM](https://www.cssm.fr/actualite/deux-dispositifs-majeurs-dexonerations-sociales-sont-desormais-applicables-a-mayotte), [CSS L.752-3-2 VI](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053285063) |

CSSM contrasts the new RGDU endpoint with the former local relief ending at **1.4 times** minimum wage. That former endpoint is historical and must not be used for the new reduction. [CSSM's earlier explanation](https://www.cssm.fr/actualite/reduction-generale-degressive-unique-rgdu-et-exoneration-lodeom).

### RGDU parameters specific to Mayotte

| Parameter | 2026 value and condition | Official source |
|---|---|---|
| Maximum remuneration multiplier `A` | `round(3 × 53.33%, 2) = 1.60`; local RGDU becomes zero at that remuneration-to-SMIC ratio | [CSS D.241-7-1 1° and 2°](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053467212/) |
| `Tmin` and `P` | `Tmin = 0`, `P = 1` for 2026; do not import mainland parameters | [D.241-7-1 2°](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053467212/) |
| `Tdelta` | Maximum coefficient is the sum of eligible local employer contribution rates; reduce `Tdelta` if the actual eligible rate total is lower | [D.241-7-1 2°](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053467212/) |
| Annual minimum wage `S` | Mayotte's applicable minimum wage; combine the periods before and after a parameter change and apply the relevant working-time adjustments | [D.241-7-1 2° and 3°](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053467212/), [D.241-7 IV and V](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006172138/2026-11-11/) |

The Mayotte formula is:

`coefficient = Tmin + Tdelta × [(1 / (A − 1)) × (A × S / R − 1)]^P`

The June amendments apply to calculation of the reduction for **2026**, under their express application provision. [Decree 2026-509, art. 2](https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000054250620).

`R` is annual remuneration under the governing statutory definition. Do not freeze `S` at January's local wage when a relevant parameter changes, and do not use an assumed rate total for an actual employer. The statutory result is rounded to four decimals and capped; actual entitlement also requires annual regularisation, eligible contribution limits and any special contract adjustments. This Guide supplies the raw algebra, not those complete payroll computations. [D.241-7-1](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053467212/); [D.241-7 II, IV and V, D.241-8 to D.241-11](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006172138/2026-11-11/).

The November consolidated D.241-7 displays a new branch-minimum mechanism. Its express commencement note applies the amendment to employment periods from **1 January 2027**. Do not use the display's November commencement badge alone to replace the 2026 Mayotte formula. No 2027 calculation is supplied here. [D.241-7, commencement note citing Decree 2026-1037 art. 3 II](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006172138/2026-11-11/).

### Route LODEOM to the correct schedule

LODEOM extends to Mayotte through L.752-3-2 VIII and D.752-7-1, using local minimum wage and applicable local contributions/rates. Public employers within the statutory exclusion and household employers do not qualify. Eligibility includes the small-employer route, specified sectors irrespective of workforce, and specified transport routes and personnel; a Guyana-only professional-services route does not become a Mayotte entitlement. Match the exact statutory category and each employee's activity before choosing a schedule. [L.752-3-2 I, II, V and VIII](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053285063); [D.752-7-1](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000021630175/?anchor=LEGIARTI000053469915).

| Schedule | Eligibility gate and remuneration endpoint | Official source |
|---|---|---|
| Ordinary, III A | Eligible II categories outside B and C; exemption decreases after `1.3 × S` and ends at `2.2 × S`. The small-employer route starts below 11 employees, with the statutory preservation rule on crossing that threshold | [L.752-3-2 II and III A](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053285063), [D.752-7 II A](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000052196887) |
| Reinforced, III B | Fewer than 250 employees **and** annual turnover below EUR 50 million **and** a qualifying statutory activity/route; the listed-sector route excludes building/public works. Decrease after `2 × S`, zero at `2.7 × S` | [L.752-3-2 III B](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053285063), [D.752-7 II B](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000052196887) |
| Innovative ICT, III C | Same workforce/turnover limits, with the employee essentially engaged in a qualifying innovative ICT project. Full eligible contributions below `1.7 × S`; between that and `2.5 × S`, relief is limited to the portion corresponding to `1.7 × S`; then decreases to zero at `3.5 × S`. Administrative, finance, logistics and HR functions are excluded by the implementing conditions | [L.752-3-2 III C](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053285063), [D.752-7 II C](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000052196887) |

The ICT project must meet the cumulative project, innovation and listed technical-domain conditions in D.752-7 II C. The endpoints are a routing aid, not permission to use the most generous schedule. LODEOM is annual, by employee and contract, with time-related minimum-wage adjustments. Its contribution perimeter refers to L.241-13 I **in the version before the 2025 financing law**, so do not substitute the current mainland RGDU rate total. [L.752-3-2 I, III and IV](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053285063); [D.752-7](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000052196887).

## Boundary and exception table

| Situation | Consequence | Source |
|---|---|---|
| LODEOM filing/payment obligations overdue | Relief requires compliance; payment condition can be met by a respected arrears plan together with timely current contributions | [L.752-3-2 VI](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053285063) |
| Another employer contribution exemption | General noncumulation, subject to the expressly listed overtime deductions and statutory rate-reduction exceptions; this does not permit RGDU plus LODEOM | [L.752-3-2 VI](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053285063) |
| Final criminal conviction for the listed tax-fraud or illegal-labour offences, or notified control report | Statutory exclusion or suspension during the judicial procedure; check the actual provision and facts | [L.752-3-2 VII](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053285063) |
| Part-year, part-time, temporary work, special paid-leave arrangements or changing parameters | Apply the applicable adjustments before an actual claim; the simple coefficient examples do not establish entitlement | [D.241-7 IV/V and D.241-10-1](https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006172138/2026-11-11/), [L.752-3-2 IV](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053285063) |

## Worked cases

These preserve the original assumptions. `S` is already independently established, the worker is assumed eligible and `Tdelta = 0.24` is an **assumed eligible rate total**, not a published universal rate. The outputs are the unrounded expression only. [Formula: D.241-7-1](https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053467212/).

At `R = 1.2 × S`, `0.24 × [(1 / 0.6) × (1.6 / 1.2 − 1)] = 0.133333…`. Expressing remuneration as a ratio to `S` avoids inventing a Mayotte wage amount.

```oa-check
name: Assumed eligible RGDU coefficient at 1.2 times local annual SMIC
inputs:
  remuneration_ratio: 1.2
  assumed_tdelta: 0.24
  a: 1.6
steps:
  - raw_coefficient: assumed_tdelta * (1 / (a - 1)) * (a / remuneration_ratio - 1)
expected:
  raw_coefficient: 0.133333333333
tolerance: 0.000000001
```

At `R = 1.6 × S`, the same raw expression is zero. At `R = S`, it reaches the assumed maximum of `0.24`. These are endpoint checks, not a payslip, rounding instruction or annual regularisation.

```oa-check
name: Original RGDU zero and maximum endpoints
inputs:
  upper_ratio: 1.6
  lower_ratio: 1
  assumed_tdelta: 0.24
  a: 1.6
steps:
  - upper_raw: assumed_tdelta * (1 / (a - 1)) * (a / upper_ratio - 1)
  - lower_raw: assumed_tdelta * (1 / (a - 1)) * (a / lower_ratio - 1)
expected:
  upper_raw: 0
  lower_raw: 0.24
tolerance: 0.000000001
```

## When to refuse or refer

Do not produce an executable payroll claim from a schedule endpoint, an assumed contribution rate or these algebraic examples. Hold the calculation where employee/employer eligibility, local `S`, contribution perimeter, special-contract adjustments or previous relief use is missing. Detailed LODEOM activity classification and payroll computation need the complete transaction-specific statutory test.

## Filing and payment

CSSM points to an updated Urssaf declaration guide and payroll-software changes. The linked declaration guide was not successfully read, so no DSN code, CTP, form field, payment calendar or software instruction is supplied. The July commencement and August first declaration above do not close that execution gap. [CSSM](https://www.cssm.fr/actualite/deux-dispositifs-majeurs-dexonerations-sociales-sont-desormais-applicables-a-mayotte).

## Completion checklist

Record employment periods, establishment, employee activity/eligibility, contract and hours, remuneration, period-specific local minimum wage, eligible rates and contribution total, statutory schedule, other reliefs and compliance evidence. Keep the calculation on hold until its inputs and execution route are supported.

## Sources

| Source and actual scope read | URL | Read on |
|---|---|---|
| CSSM June update: commencement, local rates/SMIC, choice and declaration-guide link | https://www.cssm.fr/actualite/deux-dispositifs-majeurs-dexonerations-sociales-sont-desormais-applicables-a-mayotte | 2026-11-17 |
| CSSM earlier explanation: operative former/new endpoints, commencement and noncumulation; opened and read again for this draft | https://www.cssm.fr/actualite/reduction-generale-degressive-unique-rgdu-et-exoneration-lodeom | 2026-11-17 |
| Decree 2026-82: art. 1 local adaptations and art. 3 employment-period commencement | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053465499 | 2026-11-17 |
| CSS art. D.241-7-1: operative local formula, convergence and period changes; read in full, version since June 2026 | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053467212/ | 2026-11-17 |
| Decree 2026-509 art. 2: complete operative commencement and application to the 2026 reduction calculation | https://www.legifrance.gouv.fr/loda/article_lc/LEGIARTI000054250620 | 2026-11-17 |
| CSS common section: art. D.241-7 II, IV to VI and express 2027 commencement note; local D.241-7-1 and special-contract/limit neighbours | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000006172138/2026-11-11/ | 2026-11-17 |
| CSS art. L.752-3-2: I to VIII read in full, including exclusions, schedules, compliance, noncumulation and Mayotte adaptation | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000053285063 | 2026-11-17 |
| CSS art. D.752-7: II to V schedule formulas, innovative-project conditions, definitions and adjustments read in full | https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000052196887 | 2026-11-17 |
| CSS art. D.752-7-1: operative Mayotte local-wage/contribution adaptations read in full; neighbouring Saint-Martin schedules excluded | https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006073189/LEGISCTA000021630175/?anchor=LEGIARTI000053469915 | 2026-11-17 |

Not yet confirmed: complete transaction-specific RGDU/LODEOM eligibility and contribution computation, precise statutory remuneration/base dependencies, all special-contract and regularisation mechanics, individual contribution bases and other payroll charges, DSN/CTP codes and operational filing/payment instructions, emergency cyclone measures, and a 2027 calculation. These are non-usable holds, not permissions to estimate. Independent source review of this bounded scope is complete; professional approval is pending.
