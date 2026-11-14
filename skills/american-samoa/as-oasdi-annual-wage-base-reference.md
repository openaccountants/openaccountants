---
name: as-oasdi-annual-wage-base-reference
version: "1.0"
description: Bounded American Samoa ordinary private-employee federal OASDI annual wage-base reference for 2026. Uses independently stipulated covered remuneration, separate employee and employer shares and the published annual ceiling. Holds wage classification, exceptions, other programmes, actual withholding, precision, payments and complete outputs. Requires the universal, social-contributions and scope-neutral US Circular 230 disclosure bases; guide presence and component checks do not establish comprehensive acceptance.
category: international
jurisdiction: AS
tax_year: 2026
tax_year_notes: "Calendar-year 2026 published OASDI ceiling and ordinary employee/employer rates only. Selected current US Code text is published through Public Law 119-124, 15 October 2026; this does not establish the absence or effect of later law. Territorial income tax is separate."
last_updated: 2026-11-14
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
depends_on:
  - workflow-base
  - social-contributions-workflow-base
---

# American Samoa: 2026 OASDI annual wage-base reference, v1.0

> **Source-cited draft.** Written by Ryan Duguid; brought to the 2026 standard by Claude. Built from IRC sections 3101, 3111 and 3121, the SSA determination of the 2026 contribution and benefit base (90 FR 49047) and IRS Publication 15 (2026). No accountant has reviewed it.

**Answer first.** For an ordinary private employee in American Samoa, federal social security (OASDI) applies because IRC section 3121(e) includes American Samoa in "State" and "United States". In 2026 the employee and the employer each owe **6.2%** of covered wages up to the **USD 184,500** annual wage base (per employee, per employer, calendar year), so each share is at most **USD 11,439** (derived). Medicare, Additional Medicare Tax and territorial income tax are separate and are not capped by this base.

## Scope

> **General reference only.** This Tier 2 draft illustrates the selected federal Old-Age, Survivors and Disability Insurance (OASDI) annual wage-base profile. It does not establish actual covered wages, complete FICA, territorial income tax, lawful withholding, a remittance or accepted financial outputs. Guide presence and component checks do not establish comprehensive jurisdiction acceptance.

Load all declared bases in full. Preserve the 4 universal outputs and 18 checks, the 5 social-contributions outputs and 12 checks, every mandatory country slot, shared refusals and the exact topical refusals below. This reference leaves the social-contributions country contract incomplete. Actual payroll also requires payroll-workflow-base and a complete American Samoa payroll companion; no output or country acceptance transfers by implication.

Each calculation concerns one fictional ordinary private employee and one employer, with covered employment and all remuneration inclusions/exclusions independently stipulated for the calendar year 2026. Remuneration is paid and received within that same calendar year. There is no predecessor/successor or common-paymaster history, other employer, international agreement, mixed covered/excluded service, excluded employment or disputed wage component. P09 compares 2 separately stipulated employees, each on those conditions. These are explicit fictional premises, never defaults for missing facts. Actual classification, wage inclusion, allocation and the complete applicable law must be established separately before an actual result.

Federal FICA's territorial link is independent of American Samoa's territorial income-tax adoption. IRC section 3121(e)(1) includes American Samoa in 'State' and section 3121(e)(2) includes it geographically in 'United States'. Section 3121(b) includes service within the United States irrespective of either party's citizenship or residence, subject to its exceptions. This does not convert territorial income tax into current federal income-tax tables or establish every worker's coverage.

Government cases are outside the fictional private-employment branch. Do not infer a universal American Samoa government exemption from section 3121(b)(7)'s opening State-service exclusion: paragraph (7)(B) expressly excepts American Samoa government service from that exclusion. Resolve the actual branch, retirement-system facts and complete law separately.

## Ask the client first

1. **Who the legal employer and employee are**, and the actual service, location and status (private, government, household, agricultural or other special service).
2. **Every remuneration component paid and received in calendar 2026**, with inclusions and exclusions.
3. **Other employers, predecessor or successor and common-paymaster history**, and any international agreement.
4. **Corrections, prior wages, actual withholding and remittances so far.**
5. **Whether the reviewer is ready**: identifiers, bank details and signatures stay with the reviewer.

## The method, step by step

### Rates, bands and thresholds

| Item | Figure, 2026 | Source |
|---|---|---|
| OASDI employee rate | 6.2% of covered wages (IRC 3101(a)) | [IRS Publication 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| OASDI employer rate | 6.2% of covered wages (IRC 3111(a)) | same |
| OASDI wage base (contribution and benefit base) | $184,500 for remuneration paid in 2026, per employee and employer, calendar year (IRC 3121(a)(1)) | [SSA determination, 90 FR 49047](https://www.govinfo.gov/content/pkg/FR-2025-11-03/pdf/2025-19763.pdf) |
| Maximum share at the base | USD 11,439 each (derived: 184,500 x 6.2%) | [IRS Publication 15 (2026)](https://www.irs.gov/pub/irs-pdf/p15.pdf) |
| Territorial link | American Samoa is in "State" (3121(e)(1)) and "United States" (3121(e)(2)) | [IRC section 3121](https://uscode.house.gov/us/usc/119-124/t26/s3121/) |

### Primary evidence and reading limits

| Authority | Selected support and limits |
|---|---|
| [IRC section 3101, current published route](https://uscode.house.gov/us/usc/119-124/t26/s3101/) and [section 3111](https://uscode.house.gov/us/usc/119-124/t26/s3111/) | Subsection (a) supplies the ordinary employee and employer OASDI rates of 6.2% each. Their separate hospital-insurance provisions and international-agreement exemptions are not folded into this component. Official text is labelled current through Public Law 119-124, 15 October 2026, not a complete original-amendment audit or a guarantee against later changes. |
| [IRC section 3121](https://uscode.house.gov/us/usc/119-124/t26/s3121/) | Selected complete operative contexts cover remuneration/wages, section 3121(a)(1) calendar-year ceiling and successor rule, employment, mixed service, employee and territorial definitions. Its many exclusions and linked authorities require independent intake. The ceiling links to the contribution and benefit base under Social Security Act section 230. An income-tax exclusion or cash receipt alone does not establish a FICA exclusion. |
| [Published 2026 SSA determination, 90 FR 49047–49053](https://www.govinfo.gov/content/pkg/FR-2025-11-03/pdf/2025-19763.pdf) | Complete final 7-page original retained. Selected OASDI text and original PDF page 4, printed page 49050, compared. It establishes the $184,500 contribution and benefit base for remuneration paid in 2026 and explains the section 230(b) determination. Its other benefit, old-law and household thresholds are different concepts. The unread public-inspection copy is not the authority used here. |
| [IRS Publication 15 (2026)](https://www.irs.gov/publications/p15) | Selected territorial-employer and Social Security sections corroborate 6.2% each and the $184,500 annual base, distinguish territorial income-tax withholding and state Publication 80 is discontinued. This administrative guide does not replace the statutory intake. |
| [SSA contribution and benefit base table](https://www.ssa.gov/OACT/COLA/cbb.html) | The historical row expressly says 2026: $184,500. The page's current 2027 headline is not the 2026 ceiling. No 2027 figure is imported. |

The retained Code responses are complete retrievals; only selected contexts were substantively reviewed. No absence of a later amendment, exclusion, local obligation or filing requirement is inferred from a search, index or administrative summary. Actual application remains held until the full relevant chain and facts are established.

### Intake and conditional mechanics

Reuse relevant redacted evidence before grouped questions. Establish the legal employer and employee, actual service/locations/status, the calendar year in which each amount was paid and received, every remuneration component and exclusion, all employers and predecessor/successor/common-paymaster history, international coverage, corrections, prior wages, actual withholding/remittances and reviewer readiness. Keep identifiers, bank information and signatures with the reviewer. Present and confirm the profile before actual classification; confirmation cannot supply missing law.

1. **Establish the pre-ceiling input.** W is the explicitly stipulated non-negative annual covered remuneration, after all other inclusion/exclusion questions have been resolved independently and before the section 3121(a)(1) OASDI ceiling. W is not territorial taxable income, total accounting expense, net bank pay or an amount inferred from missing records. The fictional W does not resolve actual wage classification.
2. **Apply one employee's annual ceiling on the established employer basis.** For the selected profile, C = min(W, 184500). The ceiling limits the wage base, not the tax amount. Section 3121(a)(1)'s calendar-year/employer and successor rules cannot be replaced with a per-payment, per-component, household-wide or all-employers aggregate ceiling. Exceptional histories remain held.
3. **Keep the shares and programme separate.** E = 0.062 × C and R = 0.062 × C. T = E + R is a combined OASDI reference total only. At the ceiling each share is 11439 and T is 22878. No Medicare, Additional Medicare Tax, unemployment tax, income tax, benefit or other obligation is computed or inferred nil. Do not cap all FICA at this OASDI ceiling.
4. **Aggregate the same fictional employee's components before the annual ceiling.** Do not apply a new annual ceiling to each pay component. Separately stipulated employees each receive their own profile computation; their summed reference totals do not authorise an actual employer declaration or remittance. Actual multiple-employer or successor/common-paymaster treatment is outside this reference.
5. **Preserve exact precision.** Retain W, C, E, R and T exactly for these illustrations. No rounding, truncation to cents, per-pay-period allocation or adjustment is authorised by this reference. Fractional results below are not lawful withholding or filing amounts. Do not turn the annual reference into a per-payment deduction by subtracting an unevidenced prior total.
6. **Keep payment and return completion held.** No reference total establishes actual withholding, recovery, credits, refunds, deposits, filing form, channel, deadline or accepted reconciliation. A payment reference is not evidence of the relevant programme/year split. No remittance is credited without evidence.

## Boundary and exception table

All monetary inputs below are fictional source-scale dollars for 2026. Exact arithmetic remains distinct from actual liability and rounding. A zero stipulated W is an arithmetic case, not a missing-fact default or a determination of a worker's coverage.

| Position | Explicit premises | Reference result or hold |
|---|---|---|
| P01 | W = 0 expressly stipulated. | C = 0, E = 0, R = 0, T = 0; no actual nil-liability conclusion. |
| P02 | W = 0.01. | C = 0.01, E = 0.00062, R = 0.00062, T = 0.00124. |
| P03 | W = 100.01. | C = 100.01, E = 6.20062, R = 6.20062, T = 12.40124. |
| P04 | W = 50000. | C = 50000, E = 3100, R = 3100, T = 6200. |
| P05 | W = 184499.99. | C = 184499.99, E = 11438.99938, R = 11438.99938, T = 22877.99876. |
| P06 | W = 184500. | C = 184500, E = 11439, R = 11439, T = 22878; exact ceiling equality. |
| P07 | W = 184500.01. | C = 184500, E = 11439, R = 11439, T = 22878. |
| P08 | One employee, same employer/year: 150000 plus 50000 independently covered components. | W = 200000, C = 184500, E = 11439, R = 11439, T = 22878. Do not cap each component separately. |
| P09 | Two independently stipulated employees, one employer/year, W = 100000 each. | Each C = 100000, E = 6200, R = 6200, T = 12400. The separate references sum to E = 12400, R = 12400, T = 24800; this is not an accepted employer remittance. |
| P10 | W = 50000; a separate fictional cash deduction of 10000 leaves 40000. | W stays 50000, C = 50000, E = 3100, R = 3100, T = 6200. Actual wage inclusion and deduction treatment remain separate gates. |
| P11 | Negative, absent, malformed or unconfirmed W or profile. | Needs Input. Do not silently clamp corrections to zero or infer nil wages from missing records. |
| P12 | Territorial income-tax adoption or a taxable-income figure is offered as current federal FICA authority/base. | Hold the separate law and covered-wage analysis. No income-tax result or FICA classification follows. |
| P13 | The user asks to cap Medicare or complete FICA at 184500 or use the OASDI total as total employment cost. | Hold the separate programmes, bases, rates and complete inventory; no inferred nil component. |
| P14 | Government, student, household, agricultural, fishing, family, nonresident-alien or other special service is present. | Hold the applicable branch. American Samoa government service is not automatically exempt under the opening words of section 3121(b)(7). |
| P15 | Other employers, predecessor/successor wages, common paymaster or international coverage is present. | Hold the verified aggregation, coverage and ceiling rules; no transferred/exhausted cap or credit is inferred. |
| P16 | Mixed covered/excluded service, noncash remuneration, tips, corrections or uncertain paid/received year. | Hold classification, section 3121(c), valuation and lawful allocation. Do not divide the annual ceiling into invented period limits. |
| P17 | Actual deductions, deposits, credits, refunds, remittance or filing-ready outputs are requested. | Hold complete law/facts, prescribed outputs, verified tools and reviewer acceptance. No static or incomplete substitute. |
| P18 | A fractional illustration is rounded to cents or turned into a per-payment amount without established authority. | Hold the lawful precision and sequence. Exact reference arithmetic supplies no withholding rule. |

### Held-case register

| Hold | Evidence required before the affected actual result |
|---|---|
| H01 | Full applicable federal and territorial current/saved law, amendments, commencement and the relevant period's source reconciliation. |
| H02 | Actual employee/employer status, locations, service, coverage, exclusions and international agreements. |
| H03 | Every remuneration inclusion/exclusion and valuation; no substitution of territorial taxable income, gross accounting pay or net cash. |
| H04 | Calendar year of payment/receipt, mixed-service/pay-period treatment, corrections and retroactive amounts. |
| H05 | Per-employer/person ceiling rules and all predecessor/successor, common-paymaster and multiple-employer history. |
| H06 | Separate Medicare/Additional Medicare, unemployment, income-tax and other programme obligations and complete payroll hand-off. |
| H07 | Actual withholding/recovery, precision, sequence and lawful adjustment or refund authority. |
| H08 | Registration, forms, deposit schedules, filing/payment deadlines, channels, references and administrative acceptance. |
| H09 | Every payment, credit and period/programme split, with complete remittance reconciliation and register. |
| H10 | Complete universal/domain/country outputs and checks, verified runtime calculation/delivery and demonstrated refusal enforcement. |
| H11 | Qualified local reviewer, professional sign-off and disposition of every material discrepancy without a cash/materiality floor. |
| H12 | Evidence reuse, confirmed profile and no more than 10 unresolved grouped factual questions. |

## Worked cases

**Case A: at and just above the ceiling (P06, P07).** One employee, one private employer, covered remuneration W of USD 184,500 and USD 184,500.01 in 2026. C = min(W, 184,500); each share is 6.2% of C.

```oa-check
name: American Samoa OASDI 2026, W at and above the USD 184,500 base
inputs:
  w_at: 184500
  w_above: 184500.01
  base: 184500
  rate: 0.062
steps:
  - c_at: min(w_at, base)
  - c_above: min(w_above, base)
  - employee_at: c_at * rate
  - employee_above: c_above * rate
  - total_above: employee_above * 2
expected:
  c_at: 184500
  c_above: 184500
  employee_at: 11439
  employee_above: 11439
  total_above: 22878
```

**Case B: two components, one cap (P08).** One employee, same employer and year, two covered components of USD 150,000 and USD 50,000. Aggregate first, then cap once; capping each component would wrongly give a base of USD 200,000.

```oa-check
name: American Samoa OASDI 2026, USD 150,000 plus USD 50,000 aggregated before the cap
inputs:
  component_1: 150000
  component_2: 50000
  base: 184500
  rate: 0.062
steps:
  - w: component_1 + component_2
  - c: min(w, base)
  - employee: c * rate
  - employer: c * rate
  - wrong_per_component_base: min(component_1, base) + min(component_2, base)
expected:
  w: 200000
  c: 184500
  employee: 11439
  employer: 11439
  wrong_per_component_base: 200000
```

Result: each share USD 11,439 (derived). These are exact reference figures, not withholding or filing amounts.

## When to refuse or refer

Preserve R-REVIEWER-MISSING and R-CONTENT-MISMATCH with the universal base's exact messages and full scope trace. Apply these additional triggers before actual calculation or assembly and deliver no incomplete financial artifact.

- **R-AS-OASDI-SOURCE.** Trigger: applicable law, coverage, actual wage basis, year or required history remains unresolved. Message: 'I cannot complete this American Samoa OASDI request because the applicable law, covered remuneration or required facts have not been established. Obtain the missing evidence and have a qualified reviewer resolve it before calculation, withholding or filing.'
- **R-AS-OASDI-SCOPE.** Trigger: operative liability, another programme/branch, complete payroll or a filing is requested from this incomplete reference. Message: 'This guide illustrates the selected 2026 ordinary private-employee OASDI annual wage-base profile. Complete contribution and payroll rules, actual withholding, prescribed outputs and professional review are not established. I cannot substitute this reference for an accepted liability, another branch or a filing-ready result.'
- **R-AS-OASDI-RUNTIME.** Trigger: verified recalculation, zero-error checks, complete output generation or delivery is unavailable. Message: 'The required verified contribution calculation and output tools are unavailable. I cannot substitute chat arithmetic, static values or an incomplete file for the required financial outputs.'
- **R-AS-OASDI-AMBIGUITY.** Trigger: more than 10 grouped factual questions remain after evidence reuse. Message: 'More than 10 grouped factual questions remain unresolved. Obtain the missing records with the reviewer before continuing.'

Refer Medicare and Additional Medicare Tax to the pack's Medicare skills, and territorial income tax withholding to the territory's payroll or income tax skill.

## Completion checklist

Preserve the universal working paper, reviewer brief, action list and practitioner checklist and all 5 social-contributions outputs: contribution computation schedule, remittance reconciliation, filing and payment calendar, reviewer brief and contribution register. Every logical output must remain identifiable. No output may be omitted or replaced with static values or mock files. This reference establishes no deployed engine or complete financial artifact.

Run all 18 universal and 12 domain checks. Add independent checks for the territorial bridge, current 2026 ceiling/rates, separate shares, exact ceiling equality and fractional results, component/person aggregation, actual wage/period/coverage holds, no Medicare or benefit-threshold substitution, no unevidenced credits and no financial artifact after refusal. Static cases/document checks do not establish live enforcement. No missing-fact defaults or cash/materiality floor are permitted.

| Mandatory social-contributions country slot | Reference and remaining evidence |
|---|---|
| 1. Programmes and rates | Selected ordinary employee/employer 2026 OASDI only; complete programme/status inventory remains open. |
| 2. Contribution bases | Pre-ceiling covered remuneration is stipulated; actual inclusions, exclusions and other statuses remain held. |
| 3. Floors and ceilings | Selected annual ceiling only; actual aggregation, exceptional histories and other programmes remain held. |
| 4. Contributor categories | Ordinary private employee illustration only; every other category requires separate evidence. |
| 5. Registration and identifiers | Current registration/readiness and required identifiers remain unestablished; reviewer retains sensitive details. |
| 6. Declaration and payment mechanics | Current forms, frequencies, deadlines, portals, schedules and references remain open. |
| 7. Penalties, surcharges and interest | No penalty/interest engine or inferred nil consequence. |
| 8. Interaction with income tax | Federal OASDI and territorial income tax remain separate; deduction/credit treatment is unestablished. |
| 9. Payment pattern library | Salary, income-tax-only and benefit receipts are not OASDI remittances; actual authority/reference patterns and bundled splits remain unverified, so unmatched. |
| 10. Refusals and conservative defaults | Exact topical/shared refusals retained; no factual defaults or accepted live enforcement demonstrated. |
| 11. Currency and rounding | Fictional source-scale dollars and exact rationals only; actual conversion, precision and adjustment rules remain held. |
| 12. Worked examples | Selected within/at/above-ceiling positions only; self-employed, other-status and any applicable floor-based programme examples remain incomplete. |

Optional voluntary, cross-border, sector, benefit and integration slots remain incomplete. No comprehensive country or domain acceptance follows.

2026-10-25, v0.1: selected 2026 ordinary private-employee OASDI annual wage-base reference, 10 numeric positions, 8 held positions and 12 held-case rows. Tier 2, pending_review and verified_by pending remain.

This document is general reference material and does not constitute tax, legal or financial advice. A qualified professional must establish applicable law, verify the facts and complete and sign off every required output before filing, paying or relying on a result.

2026-11-14, v1.0: brought to the 2026 standard (headings, rates rows linked, sources dated, worked cases); figures re-read, unchanged.

## Sources

| Source | URL | Read on |
|---|---|---|
| IRS Publication 15 (2026). Read for social security 6.2% each for employee and employer and the $184,500 wage base limit; Medicare 1.45% each. | https://www.irs.gov/pub/irs-pdf/p15.pdf | 2026-11-14 |
| SSA, 2026 cost-of-living increase and other determinations, 90 FR 49047 to 49053 (3 November 2025). Read for "$184,500 for remuneration paid in 2026". | https://www.govinfo.gov/content/pkg/FR-2025-11-03/pdf/2025-19763.pdf | 2026-11-14 |
| IRC section 3121 (House, through Public Law 119-124). Read for (a)(1), (b), (b)(7), (e)(1) and (e)(2). | https://uscode.house.gov/us/usc/119-124/t26/s3121/ | 2026-11-14 |
| IRC sections 3101 and 3111 (same edition). Read for subsection (a), 6.2% each. | https://uscode.house.gov/us/usc/119-124/t26/s3101/ | 2026-10-25 |
| SSA contribution and benefit base table. Read for the 2026 row, $184,500. | https://www.ssa.gov/OACT/COLA/cbb.html | 2026-10-25 |

Rows dated 2026-10-25 were read by Ryan Duguid on that day; the SSA table refused an automated fetch on 2026-11-14 and the same figure was confirmed in the Federal Register and Publication 15.

Not yet confirmed: later amendments after Public Law 119-124; the complete exclusions in 3121(b) for special service; American Samoa registration, forms, deposit schedules and deadlines for the employer; penalties and interest; rounding and per-period collection rules.
