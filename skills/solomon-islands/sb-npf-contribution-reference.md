---
name: sb-npf-contribution-reference
description: >
  Conditional Solomon Islands ordinary monthly National Provident Fund
  contribution reference using the authorised Act as at 5 February 2024.
  Illustrates payment-occasion wage precision, complete-dollar contributions,
  half-cent rounding of each employee's monthly total and the separately
  recoverable employee portion. Use for SINPF contribution arithmetic and
  wage-base rounding questions. Requires the universal and social contributions
  workflow bases. Fictional examples stipulate established coverage, period
  allocation and absence of overriding treatment. Actual current law, coverage,
  recovery, remittance, income tax, payroll and other programmes remain held.
  This is a source-cited draft, not comprehensive jurisdiction acceptance.
jurisdiction: SB
category: international
tax_year: 2024
tax_year_notes: "Conditional reference to the Act as at 5 February 2024; fictional February 2024 wages, March contribution month; later law and actual application held"
tier: 2
last_updated: 2026-10-28
version: 0.1
review_status: pending_review
verified_by: pending
depends_on:
  - workflow-base
  - social-contributions-workflow-base
---

# Solomon Islands: ordinary monthly NPF contribution reference v0.1

> **General reference only.** This Tier 2 conditional draft illustrates one contribution component under a dated statutory source. It does not establish actual coverage, a lawful deduction from pay, a complete contribution position or a filing or payment amount. Guide presence, source preparation and passing component checks do not establish comprehensive jurisdiction acceptance.

## Scope and source conditions

Load workflow-base and social-contributions-workflow-base in full. Preserve all 4 universal outputs and 18 checks, all 5 social contributions outputs and 12 checks, every mandatory country slot and all shared refusals. A missing applicable source, fact, tool, output or qualified review prevents delivery of an actual financial result. This component supplies none of the missing slots by assumption.

The fictional branch concerns one established employee of one established employer, ordinary money wages for February 2024 and the associated March 2024 monthly contribution. Each listed payment occasion is a complete positive amount of statutory wages due on a pay day falling within February. The employee is paid more frequently than monthly. There are no arrears, advances, corrections, disputed wages, longer-period allocations, voluntary additions or overriding directions, exemptions or agreements. The examples stipulate that the selected ordinary law applies. These are arithmetic premises, not determinations about a real worker or the complete law for that month.

Monthly and longer pay intervals require the separate section 2 branch for wages due **in respect of** the month. Do not allocate them by simply collecting payment dates, dividing an annual salary or reusing this example branch. Multiple employers, noncash benefits, salary sacrifice, unusual payment arrangements, contractual minimum pay and actual recovery from wages require separate work.

## Primary sources and limits

| Source | Selected proposition and limit |
|---|---|
| [L1: Attorney-General, authorised National Provident Fund Act v5](https://attorneygenerals.gov.sb/Download/solomon-islands-national-provident-fund-act-cap-109-v5_as-at-050224/) | Complete 41-page PDF retained, expressly as at 5 February 2024. Selected native text was compared with original pages. Physical pages 5-8, printed 1-4, contain the definitions; pages 14-20, printed 10-16, contain complete sections 13-21; pages 22-24 contain complete sections 25-27; pages 35-38 contain complete sections 49-51; page 39 contains both Schedules. This is not proof of all subsequent amendments, instruments or their application to a person. |
| [L2: SINPF, contribution rates](https://www.sinpf.org.sb/employers/contribution-rates/) | Public page accessed 28 October 2026 describes standard total 12.5%, employee 5%, employer 7.5% and the 6-day/$20 monthly conditions. Its broad gross-wage summary does not replace L1's payment-occasion precision, scheduled half-cent rule, recovery conditions or exemptions. Its current EDI description does not establish the complete filing rules for the fictional 2024 period. |
| [L3: Attorney-General, subsidiary legislation index S](https://attorneygenerals.gov.sb/legislation-dashboard/download-info/index-of-subsidiary-legislation-s/) | Complete official workbook retained. Selected sheet S entries identify exemption orders, including the 2020 pandemic order and amendment at rows 524-525. The index is a locator, not the text of those instruments or proof that no other instrument applies. No exemption is inferred or rejected solely from this index. |

The source date controls the primary figures: **2024**. Accessing the sources in 2026 does not prove that the complete 2026 law is unchanged. Obtain and reconcile the applicable amendment and commencement chain, regulations, Board directions, exemptions and agreements before using the mechanics for any actual month.

## Coverage and wage intake

Under L1 section 2, establish the employee and linked employer definitions, rather than relying on a job label or a generic contract-for-services description. Check both Schedules and any section 50(a) order. Section 14 can place liability on a principal in contractor arrangements. The wider definition also contains particular overseas, crew, government and co-operative branches. Those branches are outside this calculation.

Section 25(1) continues contributions after age 50 whilst the person remains an employee, subject to the Act. Turning 50 is not itself an exemption. An existing pension scheme alone gives no exemption under section 26. Section 27 requires a Board certificate and continuing foreign-employer, foreign-scheme and non-residence conditions. Its section 2 residence definition concerns entitlement to enter without an Immigration Act permit; do not substitute the income tax residence test. [L1, sections 2, 14 and 25-27.]

For this branch, establish and record:

1. The precise wage month, following contribution month, employee, employer, actual days worked and applicability of the ordinary section 13(1) branch.
2. Each complete payment occasion and its pay day, with the money wages due before deductions. Aggregate components of the same occasion before applying its precision rule; do not treat payroll line items as separate occasions.
3. The section 2 wage classification. Qualifying reimbursement of sums necessarily spent on the employer's behalf for employment is excluded by that definition. An unexplained allowance, noncash benefit or tax-treatment label does not establish the NPF base.
4. Raw statutory money wages W and precision-adjusted amount B separately. Retain the original cents. Do not use cash net wages, a PAYE base or the adjusted B as an unexplained substitute for earnings evidence.
5. Coverage, ordinary threshold treatment, no overriding direction or exemption, no voluntary addition and the basis for any lawful recovery. Missing evidence means Needs Input.

## Rates, precision and calculation

L1 section 13(1) uses preceding-month wages for the monthly contribution, including the contribution month following termination. Its ordinary proviso removes the contribution where the preceding month earned less than **SBD 20.00** **or** involved fewer than **6 worked days**. A prescribed-employment Board direction can change intervals, calculation, payer and that proviso. Worked days are not the number of payment occasions. Do not turn the $20 condition into a minimum contribution base.

The section 2 definition requires cents on **each payment occasion** to be ignored, except that a payment occasion totalling less than SBD 1 is deemed SBD 1. Preserve this step before aggregating the more-frequent-than-monthly branch. Zero, negative, reversed, corrected, split or incompletely identified occasions are held here; no interpretation for them is supplied.

For the positive, complete occasions in these fixtures, let p_i be the statutory wages for occasion i in whole cents. Compute:

```text
w_i = max(1, floor(p_i / 100))       whole dollars for that occasion
W   = sum(p_i) / 100                raw statutory wages, retain cents
B   = sum(w_i)                      adjusted monthly whole-dollar amount
```

The threshold wording is 'earned', whereas the definition supplies a precision rule. These examples do not decide an uncertain threshold interpretation. If W and B fall on different sides of SBD 20, return Needs Input for the ordinary monetary condition. A qualifying positive case below requires both W >= 20 and B >= 20, with the ordinary rule and at least 6 worked days established. The zero cases below have both values below 20, or fewer than 6 worked days with both values at least 20. Do not infer the outcome of a straddling case by choosing the more convenient value.

Under the **Second Schedule**, calculate the employer's total monthly contribution as **12.5 cents per complete dollar** of B, rounding any half cent on that employee's monthly total up to a complete cent. The employee portion recoverable under section 13(2) is separately **5 cents per complete dollar**. Use exact integer arithmetic:

```text
T_cents = floor((25 * B + 1) / 2)    monthly total, half-cent rounded up
R_cents = 5 * B                     scheduled employee recoverable portion
E_cents = T_cents - R_cents         balance if full lawful recovery is made
```

T is the amount the employer owes to the Fund under this component. R is a **recoverable portion**, not proof that it was or may now be deducted. Section 15 restricts recovery to the wages on which the contribution is calculated, at the time those wages are paid, and not otherwise. Sections 13(3)-(4) separately govern authorised voluntary amounts and over-recovery. An unknown, missed or disputed recovery leaves the actual deduction and employer cost held; it does not reduce T. E is conditional on full lawful recovery and is not automatically the employer's actual cost.

Do not calculate 7.5% of unadjusted decimal gross wages and add a separately rounded 5%. Do not round the contribution on each pay day, average payment amounts, reset the rule per earnings line or round only a pooled total for several employees or months. The Schedule rounds **each employee's monthly total**.

## Fictional 2024 examples

Every row below stipulates the same ordinary branch and established inputs. Amounts are SBD. The small values are artificial boundary cases, not evidence that pay complies with minimum wages or other employment law. 'Balance' means E only if full lawful R recovery is made. All actual delivery remains held.

| Case | Complete wage occasions | Days worked | W | B | T | R | Balance |
|---|---|---:|---:|---:|---:|---:|---:|
| N1 | 20.00 | 6 | 20.00 | 20 | 2.50 | 1.00 | 1.50 |
| N2 | 20.99 | 6 | 20.99 | 20 | 2.50 | 1.00 | 1.50 |
| N3 | 21.00 | 6 | 21.00 | 21 | 2.63 | 1.05 | 1.58 |
| N4 | 21.99 | 6 | 21.99 | 21 | 2.63 | 1.05 | 1.58 |
| N5 | 1000.60 + 1000.60 + 1000.60 + 1000.60 | 20 | 4002.40 | 4000 | 500.00 | 200.00 | 300.00 |
| N6 | 500.99 + 500.01 | 12 | 1001.00 | 1000 | 125.00 | 50.00 | 75.00 |
| N7 | 0.75 + 1000.25 | 12 | 1001.00 | 1001 | 125.13 | 50.05 | 75.08 |
| N8 | 1000.00 + 1001.00 | 12 | 2001.00 | 2001 | 250.13 | 100.05 | 150.08 |
| N9 | 999.99 + 1000.01 | 12 | 2000.00 | 1999 | 249.88 | 99.95 | 149.93 |
| N10 | 2500.75 + 2500.75 | 12 | 5001.50 | 5000 | 625.00 | 250.00 | 375.00 |
| N11 | 19.99 | 6 | 19.99 | 19 | 0.00 | 0.00 | 0.00 |
| N12 | 1000.00 | 5 | 1000.00 | 1000 | 0.00 | 0.00 | 0.00 |
| N13 | 1001.00 + 1001.00 | 12 | 2002.00 | 2002 | 250.25 | 100.10 | 150.15 |

N3 preserves the unrounded 262.5-cent total before rounding to 263 cents. The 105-cent recoverable portion is exact; the conditional balance is 158 cents. N5 discards cents on all 4 occasions, producing B = 4000. Flooring W once would instead produce 4002 and an unsupported T = 500.25. N6 and N7 share W = 1001.00 but have different B because N7 includes a positive sub-dollar occasion. N9 has B = 1999, so the 24987.5-cent total becomes 24988 cents.

N11 is zero because both monetary measures are below 20, with the ordinary threshold applicable. N12 is zero because only 5 days were worked, with no overriding direction. These zeros do not waive another programme or establish actual coverage.

N13 rounds once on B = 2002 for the employee's month. Rounding a separate contribution on each 1001-dollar occasion would incorrectly produce 125.13 + 125.13 = 250.26.

Aggregation checks:

- **A1, separate employees:** 2 otherwise qualifying employees each have B = 21 for February. Each T = 2.63, R = 1.05 and conditional E = 1.58. Their totals are T = 5.26, R = 2.10 and E = 3.16. Rounding once on combined B = 42 would give 5.25 and lose 0.01.
- **A2, separate months:** One otherwise qualifying employee has B = 21 in each of 2 independently established wage months under the same rules. The 2 monthly totals sum to 5.26. Do not recompute a single contribution on B = 42 or infer a carry of half cents between months. This additional fixture stipulates the applicable law for both months; it does not establish it.
- **A3, one occasion with several wage components:** Qualifying money components of 500.99 and 500.01 due and paid together on one complete occasion total 1001.00. That occasion gives B = 1001, T = 125.13, R = 50.05 and conditional E = 75.08. N6 instead has 2 separate occasions and T = 125.00. Payroll line-item count does not identify the payment occasions.

## Held cases and exact stops

Return **Needs Input**, with no dependent financial result, for each unresolved case:

| Case | Trigger and required resolution |
|---|---|
| H1 | No established employee/employer or applicable month-specific law: obtain the complete legal and coverage basis. |
| H2 | Only a monthly gross total is supplied for a worker paid more frequently: obtain all complete occasions and pay days. N6/N7 demonstrate why W alone is insufficient. |
| H3 | Monthly or longer pay frequency, arrears, advances or cross-month allocation: establish the applicable section 2 allocation and precision before computing. |
| H4 | Zero, negative, reversed, corrected or artificially split payment: resolve the complete lawful occasion and its treatment. |
| H5 | Three occasions of 6.80: W = 20.40 but B = 18. Resolve the monetary threshold before any contribution result. |
| H6 | Twenty-two occasions of 0.90: W = 19.80 but B = 22. Resolve the monetary threshold before any contribution result. |
| H7 | Unknown worked days or prescribed-employment direction: establish days and the applicable Board treatment; no default to 6 days or zero. |
| H8 | Possible Schedule, order, certificate, reciprocal agreement, foreign or contractor/principal branch: determine coverage and the correct liable person first. Age or foreign pension participation alone cannot settle it. |
| H9 | Voluntary additional contribution, youSave, religious-organisation branch or cessation of formerly exempt employment: establish the separate rules and evidence. |
| H10 | Unknown or late employee recovery: keep actual deduction and employer cost held; no retrospective recovery or reduction of the Fund total inferred. |
| H11 | Late payment, remission, unmatched or bundled remittance, refund, transfer, interest or withdrawal: obtain the complete applicable rule and allocation. No credit or penalty result supplied. |
| H12 | Actual PAYE, net pay, income tax deduction, other social programme, full filing package or sign-off requested: obtain the missing country rules and complete every required output and review. |

Preserve these topical stops alongside all shared refusals:

- 'Needs Input: establish the applicable NPF law, employee, employer, month, worked days and complete statutory wage occasions before calculating.'
- 'Needs Input: resolve the payment-occasion, allocation or threshold issue before calculating a monthly contribution.'
- 'Needs Input: establish lawful employee recovery separately; the scheduled recoverable portion is not authority for a catch-up deduction.'
- 'Held: this conditional NPF component cannot establish an actual payroll, tax, remittance or complete social contributions result.'

No country-specific factual default is authorised. Resolve a legal gap from primary authority, not an answer guessed by the worker or employer.

## Procedure, outputs and verification

The fictional calculation uses the preceding wage month and following contribution month under section 13(1). Actual registration, declarations, EDI/version rules, submission, due-date treatment and payments require the complete applicable procedures. Do not infer a day-specific deadline from the monthly calculation. Section 16's surcharge, minimum, multiples and Board remission require a separate calculation; none is supplied here. Do not use the Income Tax Act's employer NPF exclusion limit as a contribution rate or deduction determination.

For future actual work, retain a redacted intake and proposition ledger for the exact legal versions and periods, employee/employer and exemption findings, wage classification, payment occasions, W, B, days, threshold decision, T, recoverable R, actual lawful recovery, conditional E and actual employer cost. Keep registration readiness, remittances and allocation, other programmes, income tax treatment, filing calendar, tools, all outputs and qualified reviewer disposition identifiable. Do not collect identifiers, bank details or credentials in this guide's examples.

Run the 18 universal and 12 social contributions checks. Add payment-occasion precision, sub-dollar handling, complete-versus-pooled base, odd/even half-cent, per-employee/per-month aggregation, independent days, threshold-straddle hold, no late recovery, no unsupported remittance credit and held-delivery checks. Passing the component arithmetic does not complete the engagement checks.

All 13 universal country slots remain mandatory. This reference addresses only the selected dated scope, primary sources, NPF mechanics, fictional cases, refusals, intake and checks; it does not complete the actual country contract. For the social contributions contract:

- Slots 1-4: only the selected ordinary NPF rates, base, thresholds and established employee branch are illustrated. Full programmes, effective chain, limits, multiple-employment, contributor and special branches remain required.
- Slots 5-9: registration/identifiers, declaration/payment procedures, penalties, income tax interaction and the payment pattern library remain held. No form, credit, income tax relief or deadline is inferred.
- Slots 10-12: refusals and fictional SBD precision examples are supplied within scope. Currency conversion, complete current-law operation, above-ceiling and self-employed ladders and all actual output packages remain required and unproduced. An absent ceiling in the selected Schedule does not establish the complete limits for every programme or person.

Neither optional regimes nor other payroll, tax, formation, reporting, property, cross-border or compliance topics are completed by this document.

## Revision and disclaimer

28 October 2026, v0.1: conditional ordinary monthly NPF component using the authorised 5 February 2024 Act, with payment-occasion precision, scheduled monthly total, separately recoverable portion and explicit coverage, procedure, current-law and delivery holds. Tier 2, pending_review and verified_by pending remain.

This document is general reference material and does not constitute tax, legal or financial advice. A qualified professional in the relevant jurisdiction must establish the applicable law and facts and complete and sign off all required outputs before filing, paying, deducting or relying on a result.

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
