---
name: aw-annual-income-tax-table-reference
description: >
  Conditional Aruba 2026 annual ordinary income tax table reference. Applies the
  published cumulative and marginal table to independently established annual
  tabelinkomen and rounds the resulting table tax down to whole florins. Use for
  Aruba 2026 tax-table arithmetic, table-income bands or whole-florin rounding
  questions. Requires the universal and income tax workflow bases. Fictional
  examples stipulate a full-year individual filing unit and an established ordinary
  progressive table input. Complete current law, residence, household allocation,
  allowance entitlement, deductions, losses, special-rate income, foreign relief,
  payroll conversion, final liability and filing remain held. Guide presence and
  component checks do not establish professional or comprehensive acceptance.
jurisdiction: AW
category: international
tax_year: 2026
tax_year_notes: "2026 annual tax-authority table; hypothetical established table income, no actual liability or withholding accepted"
tier: 2
last_updated: 2026-10-27
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
  - income-tax-workflow-base
---

# Aruba: annual income tax table reference v0.1

> **General reference only.** This source-cited Tier 2 conditional draft illustrates one annual table computation. It does not complete an income tax engagement or a payroll calculation. Source preparation, guide presence and passing component checks do not establish comprehensive jurisdiction acceptance.

## Scope and source conditions

Load workflow-base and income-tax-workflow-base in full. Preserve all 4 universal outputs and 18 checks, all 5 income tax outputs and 12 checks, all mandatory country slots and every shared refusal. Missing applicable law, facts, tools, outputs or qualified review prevents delivery of an actual financial result.

The fictional branch stipulates a full-year individual filing unit for 2026 whose correctly allocated ordinary annual tabelinkomen T has been independently established. Residence, unit, income classification, deductions, loss ordering and applicable tax-free amount have already been determined. These are hypothetical premises, not defaults. A person's address or agreement does not establish legal residence or applicable law.

This reference begins with T, not gross wages, receipts, total income or income before the applicable tax-free amount. It does not establish eligibility for the maximum Afl. 30,000 exemption. Unknown entitlement is not the maximum and is not zero. Do not subtract another allowance from an input already established as tabelinkomen.

The source is the published 2026 table. Do not substitute it for a 2025 or other-year schedule. Before actual work, obtain and reconcile the applicable ordinance, amendments, commencement, classification, residence and procedures for the requested period. A current download does not establish a complete statutory chain. Part-year and non-resident treatment, household allocation, special-rate income, foreign relief, payroll withholding, credits, prepayments and final settlement remain held.

## Primary sources and limits

| Source | Selected proposition and limit |
|---|---|
| [L1: Departamento di Impuesto, Belastingtabel 2026](https://cuatro.sim-cdn.nl/impuesto/uploads/Belastingtabel%202026%20v1.pdf?cb=CI8pIlOQ) | Complete official 1-page table retained and compared with its original. It prints the 2026 bands, cumulative amounts, percentages, a maximum annual tax-free amount of Afl. 30,000 and downward whole-florin rounding of the tax calculated by the table. It does not establish every taxpayer's exemption or the complete upstream and downstream computation. |
| [L2: Departamento di Impuesto, income and wage tax rates](https://www.impuesto.aw/tarief-inkomstenbelasting-en-loonbelasting) | Official provenance page links the exact L1 PDF. It distinguishes income-tax tabelinkomen, taxable income less the applicable tax-free amount, from the payroll input based on zuiver voljaarsloon. A shared table does not authorise an annual-to-monthly withholding conversion. |
| [L3: Departamento di Impuesto, return-computation index](https://www.impuesto.aw/Berekeningen-aangifte-inkomstenbelasting) | The retained index lists separate married-taxpayer, deduction, loss, income-tax, settlement and contribution computations. Those listed branches are not resolved by this table. No historical worked amount or part-year day-count rule is adopted here. |
| [L4: Departamento di Impuesto, return-instruction index](https://www.impuesto.aw/toelichting-aangifte-inkomstenbelasting) | The retained introduction says the instructions apply from tax year 2023 and lists income categories, special rate, foreign relief, losses, joint taxation and prepayments. This reference has not established their complete applicable 2026 rules. |

Only the selected tax-authority table mechanics are illustrated. The complete applicable income-tax ordinance and later amendment chain have not been acquired for this draft. No statutory-currentness, professional or actual-return acceptance follows.

## Intake and component mechanics

Reuse redacted records before grouped questions. Establish the obligation and income year, applicable source chain, filing unit and household allocation, residence and period, ordinary versus special income, taxable-income and loss reconciliation, tax-free entitlement, T, currency, lawful precision, later relief, withholding/prepayments, professional reviewer and required tools. Present the inferred profile and wait for confirmation. Keep tax identifiers, bank details and signatures with the professional. Missing law requires primary evidence, not a taxpayer's guess.

1. **Establish the input.** Accept T only as independently established ordinary annual 2026 tabelinkomen. L2 defines the income-tax stage as taxable income less the applicable tax-free amount. Do not treat the maximum exemption as automatic, repeat its subtraction or infer entitlement from an amount alone.
2. **Validate the fictional input.** These fixtures use a non-negative finite base-10 Afl amount in whole florins or cents. Preserve the exact value. Hold negative, missing, malformed, non-finite, mixed-currency or ambiguous inputs and unsupported precision for reconciliation. The cents restriction is a fixture contract, not an established statutory input-precision rule.
3. **Select one published band.** A row applies when T exceeds its lower column-I amount and does not exceed its column-II amount. Use the zero band for the stipulated non-negative input up to Afl. 34,930. The final row has no upper limit. Equality belongs to the preceding row at each positive cutoff. _(L1, page 1)_
4. **Calculate exact table tax.** Select lower amount L, cumulative tax B and marginal rate r from that row. Set E = T - L and U = B + r x E. Apply r only to the excess E; B is cumulative tax, not an additional allowance or an amount to multiply by r. Preserve all exact decimal digits. _(L1, page 1)_
5. **Round the combined tax once.** Q = floor(U) in whole florins for this non-negative branch. L1 directs downward whole-florin rounding of the tax calculated according to the table. Do not round T, E, B or the marginal tax early; do not use nearest-integer, ceiling or banker's rounding. _(L1, page 1)_
6. **Reconcile and hold settlement.** Verify U = B + r x (T - L), Q <= U < Q + 1 and non-negative Q. Q is the rounded annual table-tax component, not a complete balance due, refund or withholding/payment instruction. Establish every required later adjustment and output separately.

All amounts below are Afl as printed in L1. The first published row has a dash in column I; the zero lower amount below is used only to express the stipulated non-negative fixture branch.

| Annual table income T | Lower L | Cumulative tax B | Marginal rate r |
|---|---|---|---|
| 0 through 34930 | 0 | 0.00 | 0% |
| Over 34930 through 63904 | 34930 | 0.00 | 21% |
| Over 63904 through 135527 | 63904 | 6084.54 | 42% |
| Over 135527 | 135527 | 36166.20 | 52% |

The cumulative amounts reconcile: 21% x (63904 - 34930) = 6084.54; 6084.54 + 42% x (135527 - 63904) = 36166.20. This is an arithmetic cross-check of L1, not an upstream taxable-income determination.

## Fictional 2026 component checks

Each row stipulates the scope and source premises above. T is already table income after the independently established applicable tax-free amount. U preserves 4 decimal places for these exact cents-input examples. Only Q is rounded down to whole florins. No final return or payroll amount is produced.

| Case | T | Selected lower L | Rate | Exact U | Whole-florin Q |
|---|---|---|---|---|---|
| AW01 | 0 | 0 | 0% | 0.0000 | 0 |
| AW02 | 0.01 | 0 | 0% | 0.0000 | 0 |
| AW03 | 34929.99 | 0 | 0% | 0.0000 | 0 |
| AW04 | 34930 | 0 | 0% | 0.0000 | 0 |
| AW05 | 34930.01 | 34930 | 21% | 0.0021 | 0 |
| AW06 | 34934.76 | 34930 | 21% | 0.9996 | 0 |
| AW07 | 34934.77 | 34930 | 21% | 1.0017 | 1 |
| AW08 | 40000 | 34930 | 21% | 1064.7000 | 1064 |
| AW09 | 63903.99 | 34930 | 21% | 6084.5379 | 6084 |
| AW10 | 63904 | 34930 | 21% | 6084.5400 | 6084 |
| AW11 | 63904.01 | 63904 | 42% | 6084.5442 | 6084 |
| AW12 | 63905.09 | 63904 | 42% | 6084.9978 | 6084 |
| AW13 | 63905.10 | 63904 | 42% | 6085.0020 | 6085 |
| AW14 | 100000 | 63904 | 42% | 21244.8600 | 21244 |
| AW15 | 135526.99 | 63904 | 42% | 36166.1958 | 36166 |
| AW16 | 135527 | 63904 | 42% | 36166.2000 | 36166 |
| AW17 | 135527.01 | 135527 | 52% | 36166.2052 | 36166 |
| AW18 | 135528.53 | 135527 | 52% | 36166.9956 | 36166 |
| AW19 | 135528.54 | 135527 | 52% | 36167.0008 | 36167 |
| AW20 | 200000 | 135527 | 52% | 69692.1600 | 69692 |
| AW21 | 1000000 | 135527 | 52% | 485692.1600 | 485692 |

AW06/AW07, AW12/AW13 and AW18/AW19 deliberately straddle a whole-florin tax boundary in each positive-rate band. The cases below, at and above every table cutoff separately test row selection, even where adjacent formulae produce the same tax at equality. No source instruction permits replacing an unknown T with an estimated value merely to run these fixtures.

## Refusal catalogue and held cases

The shared refusals remain mandatory. For actual work, add these scope and evidence stops:

- **R-AW-1:** 'The applicable Aruba law, income year or table conditions are not established. Stop the affected calculation and obtain primary evidence and qualified review.'
- **R-AW-2:** 'Ordinary annual table income is not independently established. Stop and reconcile the filing unit, income classification, deductions, losses and applicable tax-free amount.'
- **R-AW-3:** 'The currency or lawful precision is unresolved. Hold the calculation and obtain the required input and rounding evidence without silently coercing it.'
- **R-AW-4:** 'This component cannot complete an actual tax, withholding, filing or payment result. Hold delivery until every required calculation, output, check and professional sign-off is complete.'

| Held case | Required disposition |
|---|---|
| Missing applicable ordinance, amendments or commencement | R-AW-1; a 2026 PDF is not the complete statutory chain. |
| A 2025 or other-year request | R-AW-1; obtain the applicable period's table and law. |
| Gross wages, receipts or income before the exemption supplied as T | R-AW-2; do not relabel or estimate the table input. |
| Unknown exemption, or requested automatic Afl. 30,000 subtraction | R-AW-2; maximum is not entitlement and an established T is not reduced again. |
| Married or joint allocation, dependant income or another filing-unit issue unresolved | R-AW-2; establish the correct ordinary table input first. |
| Special-rate income, exceptional receipts or unresolved classification | R-AW-2; obtain separate applicable source and computation. |
| Foreign income, residence, part-year or cross-border issue | R-AW-1 and R-AW-2; no day-count or relief rule is inferred. |
| Negative, missing, malformed, ambiguous or non-finite input | R-AW-2 or R-AW-3; no silent zero, absolute-value conversion or coercion. |
| Unsupported input precision or currency conversion | R-AW-3; the fixture format is not a statutory precision rule. |
| Early rounding of T, B, E or marginal tax; nearest-integer tax rounding | R-AW-3; retain exact evidence and reconcile the table's final downward rule. |
| Annual Q divided into a monthly withholding or social contribution | R-AW-4; no conversion or separate charge is established. |
| Q described as final balance due, refund or permission to file/pay | R-AW-4; downstream records, outputs and review remain required. |
| Required output, check, tool or qualified reviewer absent | R-AW-4; fixture success does not complete the workflow. |

These rows document intended behaviour. One-off arithmetic and textual checks do not establish a deployed engine or consuming-LLM enforcement.

## Outputs, checks and country contract

Retain the universal working paper, reviewer brief, action list and practitioner checklist and all 5 income tax outputs: transaction classification register, computation working paper, filing/payment calendar, reviewer brief and taxpayer action list. Preserve identifiable components wherever the universal base permits combination. This static reference replaces none of them.

Add a proposition ledger to eventual reviewer materials: source versions and year, filing-unit/residence evidence, income and deduction/loss allocation, tax-free entitlement and T, selected L/B/r, E/U/Q, exact precision, every later adjustment, withholding/prepayments, procedures, refusals, tools, outputs and reviewer disposition. Mark unresolved fields held.

Run all 18 universal and 12 income tax checks. Add exact band-selection, cumulative-base continuity, no repeated allowance, excess-only marginal rate, exact pre-rounding preservation, final floor inequality, boundary examples and held-delivery checks. A correct annual table calculation does not reconcile the complete tax ladder.

The 13 universal slots are addressed only within this conditional scope: scope, period/source limits, selected figures, primary library, position rules, refusals, no unsupported defaults, material issues, fictional examples, proposition ledger, redacted intake, additional checks and revision metadata. They remain incomplete for actual work; no slot is waived.

| Mandatory income tax slot | Selected reference and remaining hold |
|---|---|
| 1. Year, basis, unit and residence | 2026 annual table and fictional full-year unit; actual basis, unit, residence and complete law held. |
| 2. Income categories | Independently established ordinary table income only; classification and special-rate income held. |
| 3. Rates and effective dates | Published 2026 cumulative/marginal table; complete ordinance and amendment currency held. |
| 4. Allowances, deductions and credits | Input is after established applicable tax-free amount; entitlement, deductions and later credits held. |
| 5. Expenses and capital | No expense, capital, business or investment relief determination; complete rules held. |
| 6. Loss relief | No classification, ordering, offset or carry determination; establish before accepting T. |
| 7. Withholding and prepayments | No withholding conversion, credit, instalment or final settlement accepted. |
| 8. Social contributions | No AOV/AWW, AZV or other contribution, deduction or charge accepted. |
| 9. Filing mechanics | Forms, portal, declaration entries, deadlines, payment, amendment and penalties held. |
| 10. Transaction patterns | One table-input component only; complete receipt, expense and bank-pattern library held. |
| 11. Refusals and defaults | Shared plus 4 topical stops and 13 held cases; no factual default or live runtime qualification. |
| 12. Currency/conversion/rounding | Exact Afl fixtures and published final whole-florin floor; actual upstream precision and conversion held. |
| 13. Full worked ladders | 21 table cases only; complete employee, self-employed and mixed ladders to balance due remain required and unproduced. |

Optional regimes, international matters, local obligations and integrations remain incomplete. No actual income tax, payroll or comprehensive Aruba acceptance follows.

## Revision and disclaimer

27 October 2026, v0.1: conditional 2026 annual table-input component with cumulative and marginal arithmetic, downward whole-florin rounding and upstream/downstream holds. Tier 2, pending_review and verified_by pending remain.

This document is general reference material and does not constitute tax, legal or financial advice. A qualified professional in the relevant jurisdiction must establish applicable law, verify facts and complete and sign off every required output before filing, paying or relying on a result.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained in the
[ryanduguid/openaccountants fork](https://github.com/ryanduguid/openaccountants).
Check its quality tier, recorded review status and cited sources before use.
Choose a practitioner whose credentials and engagement scope you have verified.
The links below are optional upstream services; they do not publish or verify
this fork's changes.

- Upstream connection service: https://www.openaccountants.com/connect
- Upstream accountant network: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
