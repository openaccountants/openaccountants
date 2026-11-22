---
name: us-gaap-software-development-costs
description: "Draft US GAAP software-cost working paper distinguishing internal-use software, external marketing and cloud implementation. Separates pre-adoption and early-adopted ASU 2025-06 capitalization gates, eligible cost records and exclusions; external-use measurement and current-ASC conclusions remain source-held. Load financial-reporting-workflow-base."
jurisdiction: US
category: financial-statements
domain: financial-reporting
type: computation
standard: "ASC 350-40 Internal-Use Software and ASC 985-20 (ASU 2025-06 amendment basis)"
effective_date: 2027-12-16
tier: 2
status: needs_sources
last_updated: 2026-11-22
version: 0.1
depends_on:
  - financial-reporting-workflow-base
---

# US GAAP software and development costs : ASC 350-40 and 985-20 v0.1

> **General reference only.** Draft working papers for AI-assisted accounting; no accountant has approved this version. Outputs need a qualified professional's review for the entity's actual facts.

## Scope

**Publication hold.** Current authoritative Codification access is unresolved. This file is held with `status: needs_sources`; do not publish it as a complete current-US-GAAP method. The specifically cited FASB Updates support the amendment-basis research below, not an assertion that every intervening amendment has been incorporated. Unrecovered conclusions are listed individually under Sources and are not usable instructions.

Load `financial-reporting-workflow-base`. Prepare a source-linked working paper, proposed balanced journal entries, disclosure checklist and reviewer brief. Keep assumptions separate from source-confirmed rules. Do not issue financial statements, an audit opinion or a tax return from this file.

The date key 2027-12-16 identifies the first possible annual-period start after 15 December 2027 for mandatory ASU 2025-06 application, including interim periods. Early adoption is allowed as of an annual-period beginning. Thus a calendar-2026 entity has not adopted this amendment merely because it has been issued. Record its actual election and prospective, modified or retrospective transition choice. [ASU 2025-06, 350-40-65-4](https://storage.fasb.org/ASU%202025-06.pdf).

## Ask the client first

- Product, intended customers/use, distribution rights, hosting arrangement, contractual right to take possession and relevant modules.
- Reporting period, adoption of ASU 2025-06 and transition election; any costs capitalized before adoption.
- Authorization/funding date, feasibility/completion evidence, unresolved novel functionality and significant performance requirements.
- Dated time records, vendor invoices and allocation between coding, testing, training, data conversion and maintenance.
- Substantial completion/ready-for-use date, useful life, amortization policy and abandonment/impairment indicators.
- Whether a customer receives a software license, or access to a hosted service; external marketing plans.

## The method, step by step

1. **Document scope before costs.** Internal-use software and software to be sold, leased or marketed externally have different guidance. Evaluate the actual contract and business plan; a SaaS label alone decides neither the customer's license accounting nor the developer's cost scope. The read Update states that it does not amend ASC 985-20. Recover the current scope text before issuing the final conclusion. [ASU 2025-06, Summary and 350-40-15-2](https://storage.fasb.org/ASU%202025-06.pdf).
2. **Use the correct version.** Before adopting ASU 2025-06, the reproduced prior text uses preliminary-project, application-development and postimplementation stages, with the preliminary stage complete and management authorization/funding plus probable completion/use required for capitalization. Under adopted ASU 2025-06, the revised 350-40-25-12/-25-12A instead requires authorization/committed funding and probable completion/intended use, including resolution of significant development uncertainty. Do not combine the old stage gate with the new recognition gate as if both are one rule. [ASU 2025-06, 350-40-25-1 through -25-14, redline and transition](https://storage.fasb.org/ASU%202025-06.pdf).
3. **Track uncertainty explicitly in the adopted branch.** Assess novel/unproven functions and whether significant performance requirements have been identified or remain subject to substantial revision. If significant development uncertainty prevents the probable-to-complete threshold, expense the affected pre-threshold costs; do not backfill capitalization just because the project later succeeds. If the capitalization requirements later cease to be met, stop capitalizing further costs and assess existing balances under the impairment guidance; readiness is the latest cessation point, not the only one. Capitalization ceases no later than substantial completion and readiness for intended use. [ASU 2025-06, 350-40-25-12/-25-12A, -25-13/-25-14](https://storage.fasb.org/ASU%202025-06.pdf).
4. **Classify each cost.** The read cost list includes direct external materials/services and directly associated employee payroll/benefits to the extent of project time. Interest has its separate ASC 835-20 conditions. General administration/overhead is excluded. Expense training and data conversion itself; distinguish software built to enable data access/conversion. Maintenance is not an enhancement; inability to separate internal maintenance from minor upgrades cost-effectively leads to expense under the stated rule. Each cost needs the applicable recognition gate as well as an eligible nature. [ASU 2025-06, 350-40-25-4/-25-5, -25-17A through -25-17E, -30-1 through -30-3](https://storage.fasb.org/ASU%202025-06.pdf).
5. **Handle hosting separately.** For a hosting arrangement already concluded to be a service contract, ASU 2018-15 applies internal-use recognition guidance to implementation costs. Capitalized implementation costs are amortized over the hosting term as specified, with expense presented in the same line as hosting fees, the asset in the same balance-sheet line as prepayments for hosting, and cash flows classified consistently with hosting fees. Amortize straight-line unless another systematic and rational pattern is more representative. Determine the term from the noncancellable period plus the specified reasonably-certain customer options and vendor-controlled extensions, and reassess it periodically. Begin by module or component when ready for intended use after substantial testing; wait for dependent modules if functionality is entirely dependent on them. That is not a software-license asset conclusion. [ASU 2018-15, 350-40-25-18, -35-11 through -35-17, -45-1 through -45-3](https://storage.fasb.org/ASU%202018-15.pdf).
6. **Build the capitalization rollforward.** Show opening cost, eligible additions by module/date, expense exclusions, ready-for-use transfers, amortization and writeoffs separately. Attach the supported life/method and separate impairment assessment. Recover the full external-use technological-feasibility, amortization and recoverability method before computing an ASC 985-20 asset; do not import the internal-use threshold.

## Worked cases

All costs and dates are illustrative. Both cases assume scope, current text and transition have been separately cleared for an early adopter using the amended internal-use gate, with no capitalization of interest.

**Eligible costs after the gate.** After satisfying both recognition conditions and before readiness for use, a project incurs $40,000 direct vendor coding and $30,000 directly supported employee project payroll. Training is $6,000, data cleansing is $4,000 and administration is $5,000. Proposed additions are $70,000; expense exclusions total $15,000. Dr software-in-development $70,000 and relevant expenses $15,000 / Cr payables/payroll clearing/cash $85,000, according to actual settlement.

```oa-check
name: Eligible internal-use costs versus excluded activities
inputs:
  direct_vendor: 40000
  direct_payroll: 30000
  training: 6000
  data_cleansing: 4000
  administration: 5000
steps:
  - capitalized: direct_vendor + direct_payroll
  - expensed: training + data_cleansing + administration
  - total_cost: capitalized + expensed
expected:
  capitalized: 70000
  expensed: 15000
  total_cost: 85000
```

**Gate changes the result.** Of $70,000 otherwise direct project costs, $20,000 is incurred while significant development uncertainty still prevents the recognition threshold. The remaining $50,000 follows its resolution, after authorized funding and probable completion, before ready-for-use. Capitalize $50,000 and expense $20,000. If the threshold had never been met, all $70,000 would be expensed. This is a conditional comparison, not permission to move expenditure dates or revive earlier expense.

```oa-check
name: Unresolved development uncertainty prevents earlier capitalization
inputs:
  total_direct_cost: 70000
  pre_threshold_cost: 20000
steps:
  - after_threshold_capitalized: total_direct_cost - pre_threshold_cost
  - expensed_before_threshold: pre_threshold_cost
  - no_threshold_expense: total_direct_cost
expected:
  after_threshold_capitalized: 50000
  expensed_before_threshold: 20000
  no_threshold_expense: 70000
```

## When to refuse or refer

Hold where scope, adoption, completion evidence or reliable time/cost allocation is missing. Refer multiple-purpose software, externally marketed products, complex CCAs, acquired technology, capitalization of interest and impairment. Do not infer R&D tax deductions from GAAP capitalization. A tax specialist must assess tax treatment separately.

## Sources

| Official source | Passages actually read | Read date |
|---|---|---|
| [ASU 2025-06](https://storage.fasb.org/ASU%202025-06.pdf) | Summary; 350-40-15-2, -25-1 through -25-17E, -30-1 through -30-3 and -65-4. Read both redline versions and transition; selected recognition redline rendered visually. | 2026-11-21 |
| [ASU 2018-15](https://storage.fasb.org/ASU%202018-15.pdf) | 350-40-25-18, -35-11 through -35-17 and -45-1 through -45-3; hosting implementation cost treatment. | 2026-11-21 |

**Not yet confirmed:** Current complete ASC 350-40 and 985-20 scope/definitions; external-use technological-feasibility evidence, cost/amortization and recoverability rules; all current internal-use amortization/impairment/disclosure requirements; license-versus-service classification; complete intervening-amendment applicability. ASU 2025-06's exclusion of ASC 985-20 is not evidence of a completed ASC 985-20 source read. Official ASC attempt 2026-11-21 stopped at CAPTCHA/terms. These held items are not usable guidance.
