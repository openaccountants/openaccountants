---
name: us-federal-return-assembly
description: Assembly order and review controls for a US freelancer's 2026 federal Form 1040 package, with separately dated historical 2025 cases. Routes bookkeeping, Schedule C and SE, retirement, health insurance, premium tax credit, Schedule 1-A, QBI, tax, payments and Form 2210. Preserves holds in dependent Guides and refers unverified current-year form mechanics. Federal only.
version: "1.1"
jurisdiction: US
tax_year: 2026
last_updated: 2026-11-26
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: router
---

# US federal return assembly for a Schedule C freelancer, tax year 2026

Close the books, establish all income, compute Schedule SE, settle retirement before the health insurance limit, resolve any health insurance/PTC interaction, then finish adjustments, deductions, QBI, tax, credits and payments.

## Scope and who this is for

This is an assembly workflow for a sole proprietor or a domestic single-member LLC reporting a business on Schedule C without a corporate election. An LLC's activities may instead require Schedule E or F; entity classification is not decided here. [Schedule C instructions](https://www.irs.gov/instructions/i1040sc).

A route is navigation, not clearance to use a dependent Guide's held facts. Carry every source hold, missing input, referral and year restriction into the reviewer note. Stop the affected computation; do not fill gaps with assumed facts. Obtain professional review before filing. The historical base route `us-tax-workflow-base` supplies intake context; it cannot override any hold here.

**Current-year form hold:** Apart from the bounded Form 7206 reading below, this Guide does not certify 2026 form line numbers, box mechanics or filing software. Its earlier Form 1040, Schedules 1, 1-A, 2 and 3, Schedule D, Forms 8995/8995-A, 8962 and 2210 references used 2025 mechanics. Do not copy those into a 2026 filing. Check this point with one of our partner accountants.

## Intake

Read the existing case record and documents before requesting missing information. Record filing status, birth dates, dependency and identification details; all businesses and entity elections; all W-2s including every box and code; 1099-NEC, 1099-MISC, 1099-K and other receipts; investments, dividends, digital assets, rental/K-1 and foreign items; and state residence. Reconcile income using the books as well as information returns.

For health insurance, obtain monthly coverage, payer and premiums, Form 1095-A/APTC, and eligibility for subsidized employer plans through the taxpayer, spouse, dependents or children under 27. Form 7206 excludes premiums for months of such eligibility, even if coverage was declined. [Form 7206](https://www.irs.gov/pub/irs-pdf/f7206.pdf), line 1; [26 USC 162(l)(2)(B)](https://uscode.house.gov/us/usc/t26/s162/).

Obtain retirement plan type (including SEP, solo 401(k), SIMPLE or IRA), establishment date, contribution amounts and dates; 2026 estimated payment dates/amounts, 2025 overpayment applied, and 2025 tax/AGI. Match payments to account records and flag discrepancies.

## The method, step by step

| Order | Work and route | Required assembly control |
| --- | --- | --- |
| 1 | `us-sole-prop-bookkeeping`, `us-1099-k-and-payment-processors` | Reconcile books, banks and information returns; document transfers, loans and personal transactions individually. |
| 2 | `us-schedule-c-and-se-computation`, `us-section-179-and-bonus-depreciation` | Finish Schedule C, home office (Form 8829) and depreciation (Form 4562); carry all upstream limitations. |
| 3 | `us-capital-gains`, `us-form-1040-individual-return` | Establish wages, gains, qualified dividends and all other income before finalizing total income, AGI or QBI inputs. |
| 4 | `us-schedule-c-and-se-computation` | Complete Schedule SE and screen Form 8959; keep each spouse's information distinct. |
| 5 | `us-self-employed-retirement` | Resolve the plan-specific deductible contribution, not simply the cash paid. |
| 6 | `us-self-employed-health-insurance` | Apply the same-business limit and monthly eligibility; obtain all missing facts. |
| 7 | `us-premium-tax-credit-8962` | Coordinate Form 8962 with health insurance; current-year credit eligibility and repayment remain held here. |
| 8 | `us-form-1040-individual-return` | Finish other Schedule 1 adjustments, including HSA, IRA and student loan interest, then AGI; revisit linked calculations when an input changes. |
| 9 | `us-form-1040-individual-return` | Resolve standard/itemized deduction, SALT and other limitations, charitable relief, and Schedule 1-A tips/overtime/car-loan/senior items under the correct year's rules. |
| 10 | `us-qbi-deduction` | Resolve QBI and Form 8995/8995-A using the correct year's law; full QBI computation is held here. |
| 11 | `us-form-1040-individual-return`, `us-capital-gains` | Select the applicable tax calculation; reconcile Schedule 2 Parts I/II, Form 8959 and Form 8960 where relevant. |
| 12 | `us-child-tax-credit-and-eitc`, `us-education-credits-8863`, `us-foreign-tax-credit-1116` | Screen credits, Schedule 3 and refundable amounts; foreign-tax matters leave the basic assembly scope. |
| 13 | `us-quarterly-estimated-tax` | Reconcile withholding, estimated payments, prior-year credit and refunds/balance; separately determine Form 2210 duties and next year's 2027 estimates. |
| 14 | This Guide | Resolve tie-outs and prepare the reviewer package; unresolved dependencies prevent a filing-ready result. |

The historical `us-federal-income-tax-return-1040` route is not authority to bypass the year limits or holds in `us-form-1040-individual-return`.

**Retirement before health insurance.** Publication 560's self-employed worksheet starts with net profit less the deductible part of SE tax, then applies the plan computation. SEP contributions and the earnings used to limit them depend on each other; use its reduced contribution rate method. Do not treat net profit less half of SE tax as the final retirement deduction. This worksheet does not subtract health insurance. Its 2025 dollar limits are not 2026 limits. [Publication 560](https://www.irs.gov/publications/p560), Deduction Limit for Self-Employed Individuals and chapter 5 worksheet.

For Form 7206 (2026), line 9 subtracts deductible SEP/SIMPLE/qualified-plan contributions attributable to the business under which the insurance plan is established. Lines 4–8 allocate the deductible SE-tax portion; multiple businesses require that allocation rather than subtracting the entire deduction from each business. The simple subtraction in the case below applies only to its single-business situation. Line 14 uses the smaller of eligible premiums and the remaining income limit; do not confuse the limit with a deduction. [Form 7206](https://www.irs.gov/pub/irs-pdf/f7206.pdf), lines 4–14.

**Marketplace interaction.** Publication 974 (2025) explains that health insurance deductions and PTC can affect each other, and identifies additional interactions with IRA/student-loan deductions and other exclusions. The earlier claim that this was the return's only loop is withdrawn. Its 2025 eligibility, repayment caps, worksheets and convergence methods are not certified for 2026 here. For 2026 Marketplace entitlement, excess APTC and linked calculations: Check this point with one of our partner accountants. [Publication 974](https://www.irs.gov/publications/p974), Self-Employed Health Insurance Deduction and PTC.

## Tie-out checks before sign-off

These are review tasks, not a certified 2026 line map. The preparer must identify each actual year's form and field before using a tie-out.

- Reconcile Schedule C profit/loss to Schedule SE, accounting for every business, permitted adjustment and limitation; an unexplained difference stops assembly.
- Reconcile SE tax to Schedule 2 and its deductible portion to Schedule 1; reconcile retirement and Form 7206/worksheet results to Schedule 1 without duplication.
- Reconcile every Schedule 1 income and adjustment entry to its supporting document and totals; include gains and qualified dividends before computing AGI.
- Reconcile standard/itemized deductions, Schedule 1-A and Form 8995/8995-A to taxable income, with all applicable limitations. The old QBI shortcut is held.
- Reconcile tax, credits and Schedule 2/3 totals to Form 1040; separately reconcile Form 8962 credit/repayment and Form 2210 treatment.
- Reconcile withholding, current-year estimates and prior-year credit to total payments and account records. Trace each information return to the correct income category or a documented exclusion, not automatically to Schedule C.
- Compare total payments with total tax: equality can produce zero overpayment and zero balance due. Explain any differing amount rather than demanding one positive figure.

## Worked cases

**2026 order-error case (original inputs).** Single developer, net profit USD 120,000, no wages, SEP contribution USD 15,000. The following is conditional working arithmetic for one ordinary Schedule C business, no other SE income/loss, no optional method, with the SEP amount established as deductible and attributable to this business. Those additional facts are not supplied by the original case: if unresolved, stop. Regular SE arithmetic is USD 120,000 × 92.35% × 15.3% = USD 16,955.46; half USD 8,477.73. The correct income limit is USD 96,522.27 versus USD 111,522.27 if retirement is omitted, a USD 15,000 overstatement of the limit. This does not establish eligible premiums, Marketplace treatment or an actual deduction. Sources: [Schedule SE](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf), [SE instructions](https://www.irs.gov/pub/irs-pdf/i1040sse.pdf), [Form 7206](https://www.irs.gov/pub/irs-pdf/f7206.pdf). Figures are cents-based diagnostics, not completed rounded filing fields.

```oa-check
name: Retirement before the health insurance limit (2026)
inputs:
  net_profit: 120000
  sep: 15000
steps:
  - half_se: net_profit * 0.9235 * 0.153 / 2
  - limit_right_order: net_profit - half_se - sep
  - limit_wrong_order: net_profit - half_se
  - overstatement: limit_wrong_order - limit_right_order
expected:
  half_se: 8477.73
  limit_right_order: 96522.27
  limit_wrong_order: 111522.27
  overstatement: 15000
```

**Historical Case A, 2025, and Case D order error.** Preserve the earlier single developer aged 40, USD 120,000 profit, no wages/other income/capital gains/Schedule 1-A items, USD 9,600 private non-Marketplace premiums, no employer plan available, and USD 15,000 SEP contribution. Given the original worksheet parameters, its arithmetic is net earnings USD 110,820; Social Security USD 13,741.68 plus Medicare USD 3,213.78 = USD 16,955.46; half USD 8,477.73; proposed SEP ceiling USD 22,304.45; health income limit USD 96,522.27; after subtracting premiums, USD 86,922.27. Subtracting the original USD 15,750 deduction gives USD 71,172.27; its 20% is USD 14,234.45 versus USD 17,384.45 on USD 86,922.27, leaving USD 56,937.82. The old threshold comparison was USD 197,300. These are historical unrounded arithmetic benchmarks, not findings of deduction eligibility or a completed return. Plan terms/timing, insurance qualification, standard deduction eligibility, QBI and whole-dollar return/Tax Table computation still require resolution. Case D's omitted-SEP limit is USD 111,522.27; with USD 9,600 premiums the income limit alone does not restrict that amount. Check this point with one of our partner accountants.

```oa-check
name: Historical Case A and D arithmetic only (2025)
inputs:
  profit: 120000
  sep: 15000
  premiums: 9600
  original_deduction: 15750
steps:
  - earnings: profit * 0.9235
  - ss: earnings * 0.124
  - medicare: earnings * 0.029
  - se: ss + medicare
  - half: se / 2
  - proposed_sep_ceiling: (profit - half) * 0.20
  - health_limit: profit - half - sep
  - after_adjustments: health_limit - premiums
  - before_qbi: after_adjustments - original_deduction
  - tentative_qbi: after_adjustments * 0.20
  - proposed_income_cap: before_qbi * 0.20
  - residual: before_qbi - proposed_income_cap
  - omitted_sep_limit: profit - half
expected:
  earnings: 110820
  ss: 13741.68
  medicare: 3213.78
  se: 16955.46
  half: 8477.73
  proposed_sep_ceiling: 22304.45
  health_limit: 96522.27
  after_adjustments: 86922.27
  before_qbi: 71172.27
  tentative_qbi: 17384.45
  proposed_income_cap: 14234.45
  residual: 56937.82
  omitted_sep_limit: 111522.27
```

**Historical Case B, 2025.** Single filer born in 1959, valid SSN, MAGI USD 95,000. If otherwise eligible for the senior deduction, USD 6,000 − 6% × (USD 95,000 − USD 75,000) = USD 4,800. This is separate from the additional standard deduction for age; no eligibility or amount for that separate deduction is inferred. [Public Law 119-21, section 70103](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm).

```oa-check
name: Historical senior deduction arithmetic (2025)
inputs:
  magi: 95000
steps:
  - senior: 6000 - (magi - 75000) * 0.06
expected:
  senior: 4800
```

**Historical Case C, 2026 QBI.** Original facts: freelancer actively runs a business, QBI USD 1,500; alternative USD 999. The original 20% arithmetic is USD 300 or USD 199.80. The old proposed USD 400 minimum and USD 1,000 eligibility test do not establish the full QBI entitlement, material-participation finding or ordinary income limitation. No deduction is approved from these sparse facts. Check this point with one of our partner accountants.

```oa-check
name: Historical QBI arithmetic only (2026)
inputs:
  original_qbi: 1500
  alternative_qbi: 999
steps:
  - ordinary_product: original_qbi * 0.20
  - alternative_product: alternative_qbi * 0.20
expected:
  ordinary_product: 300
  alternative_product: 199.80
```

## When to refuse or refer

Stop the affected work and retain the route and missing facts in the reviewer note:

- Corporations, partnerships/multi-member LLCs, rental/Schedule E, K-1s, losses with at-risk/passive/excess-business-loss issues: Check this point with one of our partner accountants.
- Material gains, digital assets or other specialist transactions: `us-capital-gains`. Check this point with one of our partner accountants.
- Foreign income/credit, Form 2555, FBAR/Form 8938, nonresident or dual-status: `us-foreign-tax-credit-1116`, `us-fbar-and-fatca-8938`, `us-form-1040-nr-nonresident-return`. Check this point with one of our partner accountants.
- QBI thresholds, minimum, SSTBs, aggregation, cooperative patrons, wage/property limits and Forms 8995/8995-A: Check this point with one of our partner accountants.
- Schedule 1-A occupation, FLSA overtime, reporting, SSN/joint-return, car-loan and senior eligibility questions: Check this point with one of our partner accountants.
- Marketplace eligibility, repayment, nonconvergence or other interacting deductions: Check this point with one of our partner accountants.
- Amended returns, unfiled years, IRS notices or collection: `us-amended-return-form-1040-including-capital`. Check this point with one of our partner accountants.
- Missing source documents, unresolved tie-outs, unsupported figures, failed upstream checks or an unverified current-year filing mechanism: Check this point with one of our partner accountants.

## Filing and payment

For an ordinary domestic calendar-year 2026 individual return, the general filing date is **15 April 2027**. A timely Form 4868 generally extends filing six months to **15 October 2027**, not the ordinary payment deadline. Overseas/military/disaster relief and other exceptions, late interest/penalties, payment routes and Form 2210 filing exceptions: Check this point with one of our partner accountants. [26 USC 6072(a)](https://uscode.house.gov/us/usc/t26/s6072/), [IRS extension guidance](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return).

For the historical educator, reservist/performing-artist/fee-basis-official, military moving, alimony, savings-withdrawal penalty, Archer MSA, Saver’s Credit and child/dependent-care topics, obtain the actual facts and use the year-specific Form 1040 Guide; occupation alone is no exclusion. Check this point with one of our partner accountants.

## Reviewer package and completion

Include the dated form package; source documents and classifications; a working paper that recomputes the schedules and distinguishes cents from filed rounding; every hold/judgment and tie-out; payment evidence; and separately dated next-year estimates/vouchers where applicable. Identify the reviewer and record actual form/PDF, structured-data and e-file status; no rendering or submission is promised. Do not label incomplete forms or flat values as an executable return model. Record actual spreadsheet anchors before writing cross-sheet formulas, recalculate with a spreadsheet engine, and compare key outputs to the independent arithmetic; inspecting formula text alone is insufficient.

For California, route to `ca-540-individual-return` with federal AGI, taxable income, QBI, depreciation, health insurance, retirement and payment detail. For any state, also supply HSA, Schedule C profit and Schedule SE detail where relevant. State conformity/add-backs, state subsidies and claims that no state handoff is needed are not decided here. Check this point with one of our partner accountants.

## Sources

Bounded official-source reads on 2026-11-26: [Form 7206 (2026), lines 1 and 4–14](https://www.irs.gov/pub/irs-pdf/f7206.pdf); [26 USC 162(l)](https://uscode.house.gov/us/usc/t26/s162/); [Publication 560 (2025), self-employed deduction worksheet](https://www.irs.gov/publications/p560); [Publication 974 (2025), interaction discussion](https://www.irs.gov/publications/p974). Reused completed operative-source reads dated 2026-11-22/26: [Schedule C instructions](https://www.irs.gov/instructions/i1040sc), [Schedule SE](https://www.irs.gov/pub/irs-pdf/f1040sse.pdf), [Schedule SE instructions](https://www.irs.gov/pub/irs-pdf/i1040sse.pdf), [senior-deduction law](https://www.govinfo.gov/content/pkg/PLAW-119publ21/html/PLAW-119publ21.htm), [filing-date statute](https://uscode.house.gov/us/usc/t26/s6072/) and [extension guidance](https://www.irs.gov/filing/get-an-extension-to-file-your-tax-return). These are bounded claim reads, not a claim that whole publications or 2026 form sets were read.

Not yet confirmed: 2026 form mechanics beyond the bounded Form 7206 fields, full QBI and Marketplace calculations, and referred specialist outcomes are non-usable holds. Check this point with one of our partner accountants.
