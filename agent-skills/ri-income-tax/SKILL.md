---
name: ri-income-tax
description: "Rhode Island resident wages and sole-proprietor income: 2026 brackets, standard deductions, exemptions, phase-out, RI-1040 adjustments, credits and estimated tax; final 2026 filing gaps identified."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ri-income-tax"
  jurisdiction: "US-RI"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Rhode Island resident individual income tax, tax year 2026

> **General reference only.** Written by Codex. Not reviewed by an accountant. Apply the official sources to the taxpayer's facts and obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Consider relevant facts, reasonable assumptions and applicable law. Evaluate federal tax implications using the federal owner skills and obtain professional review where needed.

**Answer first.** Full-year residents compute tax from federal AGI with Rhode Island modifications, a state standard deduction and exemptions, then apply three bands from 3.75% to 5.99%. Rhode Island does **not** allow the federal itemized deduction. The 2026 inflation advisory supplies current annual amounts; final 2026 return instructions remain a gap. Sources: [2026 inflation adjustments](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-11/ADV_2025_22_Inflation_Adjustments.pdf); [2025 RI-1040 instructions, lines 1 to 8](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-12/2025%201040R%20Instructions%20122025.pdf).

## Scope

Ordinary full-year resident W-2 wages and sole-proprietor/disregarded LLC income. A person domiciled in RI, or maintaining a permanent abode and spending **more than 183 days** here, tests resident status. Part-year/nonresidents use RI-1040NR and need allocation outside this ordinary computation. Federal Schedule C/SE figures belong to `us-schedule-c-and-se-computation`; federal AGI and federal filing rules to `us-form-1040-individual-return`. Separate sales/use is in `ri-sales-tax`, employer taxes in `ri-payroll`, and entity minimum/corporate tax in `ri-corporate-tax`. Source: [Who must file and residence definitions](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-12/2025%201040R%20Instructions%20122025.pdf).

## Ask the client first

1. Domicile, abode, days in RI and any move or out-of-state wages.
2. Filing status, federal AGI and schedules, including business income and deduction adjustments.
3. Allowable exemption count, dependents and whether anyone can claim the taxpayer.
4. Bond interest, state tax refunds, retirement income and business adjustments, including HR1 items.
5. Federal EIC, other-state tax, property tax relief and certified state credits.
6. W-2/1099 withholding, estimates, prior-year tax and extension/payment records.

## The method, step by step

### Rates, bands and thresholds

| Tax year 2026 item | Amount or computation | Official source |
|---|---|---|
| Taxable income through USD 82,050 | 3.75% | [2026 tax computation](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-11/ADV_2025_22_Inflation_Adjustments.pdf) |
| Over USD 82,050 through USD 186,450 | USD 3,076.88 + 4.75% of excess over USD 82,050 | [2026 tax computation](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-11/ADV_2025_22_Inflation_Adjustments.pdf) |
| Over USD 186,450 | USD 8,035.88 + 5.99% of excess over USD 186,450 | [2026 tax computation](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-11/ADV_2025_22_Inflation_Adjustments.pdf) |
| Standard deduction: single or married separate | USD 11,200 before phase-out | [2026 standard deductions](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-11/ADV_2025_22_Inflation_Adjustments.pdf) |
| Joint or qualifying surviving spouse | USD 22,400 before phase-out | [2026 standard deductions](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-11/ADV_2025_22_Inflation_Adjustments.pdf) |
| Head of household | USD 16,800 before phase-out | [2026 standard deductions](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-11/ADV_2025_22_Inflation_Adjustments.pdf) |
| Personal/dependent exemption | USD 5,250 each before phase-out | [2026 exemptions](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-11/ADV_2025_22_Inflation_Adjustments.pdf) |
| Modified-AGI phase-out | Starts over USD 261,000; USD 7,450 increments; no deduction/exemption above USD 290,800 | [2026 phase-out thresholds](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-11/ADV_2025_22_Inflation_Adjustments.pdf); [final 2026 ES phase-out worksheet](https://tax.ri.gov/sites/g/files/xkgbur541/files/2026-01/2026%20RI-1040ES_w.pdf) |

The final 2026 RI-1040ES linked from the current personal-income forms page corroborates the advisory's annual thresholds and supplies the stepped worksheet. Deduction/exemption factors are 100% through USD 261,000; 80% for the first USD 7,450 excess; 60% for the second; 40% for the third; 20% for the fourth; zero when excess is **more than USD 29,800**. Round a fractional increment upward, not by linear interpolation. Source: [phase-out worksheet](https://tax.ri.gov/sites/g/files/xkgbur541/files/2026-01/2026%20RI-1040ES_w.pdf).

1. Establish federal AGI. Wages and net sole-proprietor profit feed through federal AGI; do not compute a second RI Schedule C. Do not repeat federal standard-deduction, Social Security wage-base or SE tax figures here.
2. Prepare **RI Schedule M** for supported additions/subtractions. Include qualifying other-state/municipal bond interest in additions and qualifying U.S. obligation interest in subtractions. The old blanket addition for state income-tax refunds is not supported by the passages read. The correct treatment of a particular refund, including federal inclusion and any state modification, is **Not yet confirmed**; do not make an automatic addition or subtraction. Source: [Schedule M instructions](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-12/2025%201040R%20Instructions%20122025.pdf).
3. The verified **2025-2026 filing cycle** form path is RI-1040 line 1 federal AGI, line 2 RI Schedule M net modifications, line 3 modified AGI, line 4 RI standard deduction, line 5 income after deduction, line 6 exemptions, line 7 taxable income and line 8 tax. Recheck final 2026 mapping. The state standard deduction replaces the old claim that federal itemized deductions could be selected. Source: [RI-1040 lines 1 to 8](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-12/2025%201040R%20Instructions%20122025.pdf).
4. For business HR1, use the actual qualifying federal deduction and the applicable state difference, not a blanket add-back of every expenditure. Verified 2025 Schedule HR1 covers additional business interest under section 163(j), domestic research under section 174A, increased section 179(b) expensing and section 181 production costs. Total line 1f flows to Schedule M **line 2k**. Final 2026 conformity and schedule values are Not yet confirmed. Source: [2025 Schedule HR1, individual](https://tax.ri.gov/sites/g/files/xkgbur541/files/2026-01/2025%20RI%20Schedule%20HR1%20-%20Individual_w_0.pdf).
5. Subtract the permitted 2026 deduction and exemptions after the phase-out. Use the correct taxpayer/dependent count; do not assume every household member qualifies. The uniform table above is status independent after deriving taxable income. The verified filing-cycle instructions require a tax-table lookup for taxable income below USD 100,000; final 2026 table is not yet read. Examples below use taxable income above that point.
6. Apply supported other-state tax credit via RI Schedule II/RI-1040MU; refundable property-tax relief via RI-1040H; RI EIC via Schedule EIC; and certified business or lead-paint credits where eligible. The verified **2025-2026 filing cycle** EIC equals **16% of qualifying federal EIC** and is reported with payments/refundable credits; the old assertion that only 15% was refundable is not supported. The old USD 500-per-child-under-six state credit has not been confirmed and must not be claimed from this skill. Source: [lines 9, 14c, 14d and Schedule EIC](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-12/2025%201040R%20Instructions%20122025.pdf).
7. Reconcile RI withholding through Schedule W and supporting W-2/1099, estimates and eligible PTE credits. Tax after credits less payments gives balance or refund. PTE credits and related state add-back require entity statements and current rules, not an assumed full-dollar credit. Source: [Schedule W and PTE instructions](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-12/2025%201040R%20Instructions%20122025.pdf).

### Retirement and other old topics retained with limits

The inflation advisory's retirement section gives **2025-2026 filing cycle** thresholds, not a verified 2026 retirement table: eligible federally taxable Social Security requires full retirement age and federal AGI below USD 107,000 single/HOH/separate or USD 133,750 joint/surviving spouse. Its pension/annuity modification reaches USD 50,000 subject to qualifying income, full-retirement-age and AGI conditions. Do not carry these annual thresholds into a 2026 return as confirmed. Source: [2025 retirement modifications](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-11/ADV_2025_22_Inflation_Adjustments.pdf).

Property tax circuit-breaker eligibility/amounts, age-related relief, other-state tax calculations and full Social Security/pension definitions remain separate eligibility work. The old mention of property-tax relief is retained, without inventing a 2026 credit amount. Final 2026 rules and any child credit are **Not yet confirmed**.

## Boundary and exception table

| Situation | Action |
|---|---|
| More than 183 days plus permanent abode | Test resident definition; 183 days alone does not meet this limb |
| Nonresident/part-year or multistate work | Use RI-1040NR allocation and reciprocity/sourcing research; refer complex allocation |
| Modified AGI crosses a phase-out increment | Recompute both deduction and exemptions using the stepped worksheet |
| Retirement income | Confirm age, income type, federal inclusion and correct-year ceiling |
| HR1 or PTE adjustments | Obtain the federal/entity workpaper and final state schedule |
| Property-tax or business credits | Obtain eligibility/certification; no unsupported automatic credit |

## Worked cases

**Case 1, ordinary wage earner.** Invented single resident has 2026 modified AGI USD 150,000, one exemption and no credits. Deduction USD 11,200 and exemption USD 5,250 give taxable income USD 133,550. Tax is USD 3,076.88 + (133,550 - 82,050) x 4.75% = **USD 5,523.13**. With USD 6,000 RI withholding, refund is USD 476.87 before other items.

```oa-check
name: Rhode Island 2026 ordinary resident wage calculation
inputs:
  modified_agi: 150000
  withholding: 6000
steps:
  - taxable: modified_agi - 11200 - 5250
  - tax: 3076.88 + (taxable - 82050) * 0.0475
  - refund: withholding - tax
expected:
  taxable: 133550
  tax: 5523.13
  refund: 476.87
```

**Case 2, phase-out decision.** Invented single taxpayer with one exemption compares modified AGI USD 268,450 with USD 268,451. The first is exactly one increment above USD 261,000: 80% deduction/exemption. One dollar more enters the second increment: 60%. Taxable incomes become USD 255,290 and USD 258,581; taxes are USD 12,159.396 and USD 12,356.5269 before return rounding. The USD 197.1309 change demonstrates the stepped phase-out, rather than tax at a single marginal rate. The annual amounts come from the final advisory; worksheet mechanics are from the final 2026 ES form; final annual-return instructions remain to be checked.

```oa-check
name: Rhode Island stepped deduction and exemption boundary
inputs:
  agi_at: 268450
  agi_over: 268451
steps:
  - taxable_at: agi_at - 11200 * 0.8 - 5250 * 0.8
  - taxable_over: agi_over - 11200 * 0.6 - 5250 * 0.6
  - tax_at: 8035.88 + (taxable_at - 186450) * 0.0599
  - tax_over: 8035.88 + (taxable_over - 186450) * 0.0599
  - change: tax_over - tax_at
expected:
  taxable_at: 255290
  taxable_over: 258581
  tax_at: 12159.396
  tax_over: 12356.5269
  change: 197.1309
```

## When to refuse or refer

Refer RI-1040NR, domicile disputes, complex other-state credits, HR1 differences, special retirement cases, certified incentives and undocumented exemptions. Do not compute a 2026 filing with an unconfirmed final form or credit. This is a state supplement, not a substitute for the federal return.

## Filing and payment

File RI-1040 through authorized e-file/software or the permitted paper route, with RI Schedule M, EIC, W, HR1 and credit schedules as applicable; save acceptance and reconcile separate payment confirmation. The verified filing-cycle due date is 15 April following the tax year, subject to calendar relief. RI-4868 grants six months to file, with payment due by the original deadline; where no RI payment is due and a federal extension exists, follow the instructions' federal-extension attachment route. Final 2026 deadlines and return paths require confirmation. Source: [filing and extension instructions](https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-12/2025%201040R%20Instructions%20122025.pdf).

The final 2026 ES form requires estimates when tax over credits is **USD 250 or more**, with installments 15 April, 15 June and 15 September 2026 and 15 January 2027; exceptions and prior-year basis appear in the form. The stated underpayment comparison is 80% of installment liability, with RI-2210 exceptions. The January payment exception requires filing and paying in full by 15 February 2027 under that form. Use the final ES worksheet and any applicable RI-2210 exception. Source: [final estimated-tax instructions](https://tax.ri.gov/sites/g/files/xkgbur541/files/2026-01/2026%20RI-1040ES_w.pdf).

## Completion checklist

- Residence/status and federal starting amounts reconciled; no federal deduction figures copied.
- 2026 brackets, deduction, exemption and phase-out used for the correct tax year.
- State adjustments and credits supported; withholding and estimates matched to records.
- Final 2026 forms/retirement/credit gaps resolved before filing; acceptance/payment retained.

## Sources

| Official source and scope actually read | URL | Read on |
|---|---|---|
| Read for ADV 2025-22: 2026 brackets, deductions, exemptions and phase-out; neighboring 2025 retirement paragraphs read and kept separate. | https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-11/ADV_2025_22_Inflation_Adjustments.pdf | 2026-11-13 |
| Read for Final 2026 RI-1040ES: pages 1 to 2, estimate trigger, dates, rate and phase-out worksheets; final current forms-page publication supersedes research draft. | https://tax.ri.gov/sites/g/files/xkgbur541/files/2026-01/2026%20RI-1040ES_w.pdf | 2026-11-13 |
| Read for 2025 resident instructions: residency, filing, extensions, RI-1040 lines 1 to 15, Schedule EIC, W and M, retirement and HR1 sections. 2025-2026 filing cycle. | https://tax.ri.gov/sites/g/files/xkgbur541/files/2025-12/2025%201040R%20Instructions%20122025.pdf | 2026-11-13 |
| Read for 2025 individual Schedule HR1: four adjustment categories, K-1 references and line 1f destination Schedule M 2k. | https://tax.ri.gov/sites/g/files/xkgbur541/files/2026-01/2025%20RI%20Schedule%20HR1%20-%20Individual_w_0.pdf | 2026-11-13 |

Not yet confirmed: final 2026 RI-1040/RI-1040NR, Schedule M/HR1/EIC/W and tax-table line mapping; 2026 retirement thresholds, credit/circuit-breaker amounts and detailed eligibility; alleged USD 500 child credit; final 2026 federal conformity; local income-tax assertion. The old 2025 standard deduction/exemption figures are superseded by the fetched 2026 advisory, and federal deduction figures route to the federal owner skill.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ri-income-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ri-income-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
