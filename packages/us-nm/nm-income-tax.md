---
name: nm-income-tax
description: "New Mexico PIT-1 resident wages and sole-proprietor income: statutory 2025-onward brackets for the 2026 pack, federal starting point, state adjustments, exemptions, credits and estimates; identifies final 2026 form gaps."
version: "0.2"
jurisdiction: US-NM
category: state-tax
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# New Mexico individual income tax, tax year 2026

> **General reference only.** Built from the official sources identified below. Written by Codex. Not reviewed by an accountant. Obtain qualified professional review before filing, paying or taking a tax position.

> **Circular 230 section 10.37:** Apply this material to the taxpayer's actual facts and the law for the relevant period, evaluate reasonable assumptions and relevant circumstances, and obtain professional review of any federal tax implications. Federal computations belong to the linked federal skills.

**Answer first.** New Mexico taxes resident wage and business income using six statutory bands from 1.5% to 5.9% applicable to tax years beginning on or after 1 January 2025. The three status schedules therefore cover 2026 under the enacted text. Start with federal AGI and apply New Mexico additions, deductions and credits. Social Security is **not unconditionally exempt**: the state exclusion has an AGI ceiling. Sources: [HB252 section 5, NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf); [PIT-ADJ line 25](https://realfile.tax.newmexico.gov/2025pit-adj-ins.pdf).

## Scope

Full-year New Mexico resident individuals, including W-2 wage earners, sole proprietors and disregarded single-member LLC owners. Residents and New Mexico-source nonresidents with a federal filing requirement must test PIT-1 filing. Part-year/nonresident allocations and resident income earned outside the state may require **PIT-B**, not merely a different rate. This skill's form and ancillary rules are the verified **2025-2026 filing cycle**; final 2026 PIT instructions are not asserted to have been read. Use `nm-sales-tax` for separate GRT/compensating tax, `nm-corporate-tax` for corporate returns and `nm-payroll` for employer taxes. Source: [PIT-1 instructions, filing, residence and PIT-B requirements](https://realfile.tax.newmexico.gov/2025pit-1-ins.pdf).

## Ask the client first

1. Residency dates, income sources, federal filing status and any New Mexico community-property allocation.
2. Federal AGI, standard/itemized deduction and underlying federal schedules, including Schedule C and state/local tax deductions.
3. Age, blindness, dependents and whether another taxpayer can claim the person.
4. Social Security, military retirement, U.S./municipal bond interest, losses and state-specific adjustments.
5. Federal EIC, eligible state credits/rebates, approved business credits and supporting certificates.
6. State withholding, prior-year tax, PIT-ES payments and expected remaining balance.

## The method, step by step

### Rates, bands and thresholds

| Single taxable income (USD) | Tax | Official source |
|---|---|---|
| 0 through 5,500 | 1.5% of taxable income | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |
| Over 5,500 through 16,500 | USD 82.50 + 3.2% of excess over USD 5,500 | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |
| Over 16,500 through 33,500 | USD 434.50 + 4.3% of excess over USD 16,500 | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |
| Over 33,500 through 66,500 | USD 1,165.50 + 4.7% of excess over USD 33,500 | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |
| Over 66,500 through 210,000 | USD 2,716.50 + 4.9% of excess over USD 66,500 | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |
| Over 210,000 | USD 9,748.00 + 5.9% of excess over USD 210,000 | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |

| Joint, head of household or qualifying surviving spouse taxable income (USD) | Tax | Official source |
|---|---|---|
| 0 through 8,000 | 1.5% of taxable income | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |
| Over 8,000 through 25,000 | USD 120.00 + 3.2% of excess over USD 8,000 | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |
| Over 25,000 through 50,000 | USD 664.00 + 4.3% of excess over USD 25,000 | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |
| Over 50,000 through 100,000 | USD 1,739.00 + 4.7% of excess over USD 50,000 | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |
| Over 100,000 through 315,000 | USD 4,089.00 + 4.9% of excess over USD 100,000 | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |
| Over 315,000 | USD 14,624.00 + 5.9% of excess over USD 315,000 | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |

| Married separate taxable income (USD) | Tax | Official source |
|---|---|---|
| 0 through 4,000 | 1.5% of taxable income | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |
| Over 4,000 through 12,500 | USD 60.00 + 3.2% of excess over USD 4,000 | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |
| Over 12,500 through 25,000 | USD 332.00 + 4.3% of excess over USD 12,500 | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |
| Over 25,000 through 50,000 | USD 869.50 + 4.7% of excess over USD 25,000 | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |
| Over 50,000 through 157,500 | USD 2,044.50 + 4.9% of excess over USD 50,000 | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |
| Over 157,500 | USD 7,312.00 + 5.9% of excess over USD 157,500 | [HB252 section 5 / NMSA 7-2-7](https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf) |

The following ancillary values are verified for the **2025-2026 filing cycle**, pending final 2026 instructions; do not label a changed annual value confirmed for 2026.

| Item | Verified filing-cycle rule and conditions | Official source |
|---|---|---|
| Federal standard/itemized deduction | Use allowable federal deduction and required state/local-tax add-back; federal dollar amounts have one home in `us-form-1040-individual-return` | [PIT-1 lines 10 and 12](https://realfile.tax.newmexico.gov/2025pit-1-ins.pdf) |
| Low/middle income exemption | Up to USD 2,500 times allowable exemption count; phase-down and AGI eligibility apply | [PIT-1 line 14 worksheet](https://realfile.tax.newmexico.gov/2025pit-1-ins.pdf) |
| Low/middle eligibility ceiling | USD 36,667 single; USD 55,000 joint/HOH/surviving spouse; USD 27,500 separate | [PIT-1 line 14 worksheet](https://realfile.tax.newmexico.gov/2025pit-1-ins.pdf) |
| Low/middle phase-down | USD 2,500 less 15% of AGI over USD 20,000 single; less 10% over USD 30,000 joint/HOH/surviving spouse; less 20% over USD 15,000 separate; apply eligibility ceiling | [PIT-1 line 14 worksheet](https://realfile.tax.newmexico.gov/2025pit-1-ins.pdf) |
| Age 65+/blind exemption | Up to USD 8,000 per eligible person; joint/HOH/surviving spouse AGI ceiling USD 51,000, single USD 28,500, separate USD 25,500; use stepped table, not a flat deduction | [PIT-ADJ line 13 and Table 1](https://realfile.tax.newmexico.gov/2025pit-adj-ins.pdf) |
| Social Security exclusion | Federally included benefits excluded only if AGI no more than USD 100,000 single; USD 75,000 separate; USD 150,000 joint/HOH/surviving spouse | [PIT-ADJ line 25 and Table 2](https://realfile.tax.newmexico.gov/2025pit-adj-ins.pdf) |
| Military retirement | Up to USD 30,000 qualifying armed-forces retirement pay under verified instructions | [PIT-ADJ line 24](https://realfile.tax.newmexico.gov/2025pit-adj-ins.pdf) |
| Working Families Tax Credit | 25% of the qualifying federal EIC amount; eligibility and state instructions apply | [PIT-1 lines 25, 25a and 25b](https://realfile.tax.newmexico.gov/2025pit-1-ins.pdf) |
| Estimated tax | USD 1,000 tax-liability floor; compare prepayment against smaller of 90% current or 100% prior-year liability under instructions | [Estimated Payments and underpayment instructions](https://realfile.tax.newmexico.gov/2025pit-1-ins.pdf) |

1. Prepare federal AGI. Schedule C and deductible self-employment tax feed through it; federal computations and figures are in `us-schedule-c-and-se-computation`. Load federal standard deduction and filing rules from `us-form-1040-individual-return` rather than reprinting federal amounts.
2. Complete **PIT-ADJ** for applicable additions/deductions. The instructions identify state/municipal bond interest, federal NOL add-back and separately computed NM loss, certain 529 refunds/rollovers and conservation-donation adjustments. Subtractions include qualifying U.S. obligation interest, qualifying railroad benefits and military/tribal income under their conditions. Do not assume every federal-exempt bond is exempt in NM. Sources: [PIT-ADJ lines 1 to 13 and military sections](https://realfile.tax.newmexico.gov/2025pit-adj-ins.pdf).
3. Apply the federal deduction and state/local-tax add-back using the PIT-1 worksheet. Evaluate the limited dependent deduction, low/middle-income exemption and age/blindness table from the instructions. For the age/blindness table, the top exemption of USD 8,000 applies at AGI through USD 30,000 joint/HOH/surviving spouse, USD 18,000 single or USD 15,000 separate; subsequent bands reduce it by USD 1,000 each, ending at the ceilings in the table above. Source: [PIT-1 lines 10 to 15](https://realfile.tax.newmexico.gov/2025pit-1-ins.pdf); [Table 1](https://realfile.tax.newmexico.gov/2025pit-adj-ins.pdf).
4. Apply Social Security exclusion only within the AGI ceiling and only for benefits in federal AGI. The old unconditional full exemption was wrong for over-ceiling taxpayers. Do not deduct the same income twice through competing exemptions. Source: [PIT-ADJ line 25](https://realfile.tax.newmexico.gov/2025pit-adj-ins.pdf).
5. The verified PIT-1 mapping is line 9 federal AGI, line 10 state/local-tax deduction add-back, line 11 PIT-ADJ additions, line 12 federal standard/itemized deduction, line 13 certain-dependent deduction, line 14 low/middle exemption, line 15 PIT-ADJ deductions/exemptions, line 17 NM taxable income and line 18 tax. PIT-B filers compute apportioned/allocated tax through that schedule. Final 2026 line numbers require checking. Source: [PIT-1 line instructions](https://realfile.tax.newmexico.gov/2025pit-1-ins.pdf).
6. Apply properly supported credits/rebates: other-state tax credit is considered on line 20, nonrefundable business credits via PIT-CR, and refundable credits/rebates follow their own schedules, including PIT-RC. WFTC is not simply an automatic 25% payment to everyone with self-employment income: establish federal EIC eligibility/adjustments. Subtract withholding from W-2/1099 and PIT-ES payments to determine balance/refund. Source: [PIT-1 lines 20 to 30 and WFTC instructions](https://realfile.tax.newmexico.gov/2025pit-1-ins.pdf).
7. Reconcile GRT paid and passed on with business books. GRT is a separate gross-receipts tax, not an income-tax credit; federal business expense treatment belongs to the Schedule C working paper. Current GRT figures and sourcing have one home in `nm-sales-tax`.

## Boundary and exception table

| Situation | Treatment |
|---|---|
| Social Security above AGI ceiling | Do not take the special exclusion merely because the benefit is Social Security |
| Community property and separate returns | Allocate income and payments under applicable community-property rules; obtain both spouses' records |
| Part-year/nonresident or resident out-of-state income | Determine PIT-B need and allocation; do not apply resident computation without adjustment |
| Technology jobs or angel investment credit | Obtain current eligibility/certification and approval; no credit amount is assumed |
| Income from NM oil, gas or minerals | Separate severance/conservation and royalty rules; refer specialist issues |
| Fiduciary return | FID-1 is outside individual PIT-1 scope |
| Amending | Use current PIT-X procedure; do not just substitute the original return |

## Worked cases

**Case 1: ordinary single resident.** Invented taxpayer has NM taxable income USD 60,000 after verified federal/state adjustments, no credits. Tax under the statutory 2025-onward single schedule is USD 1,165.50 + 4.7% x (60,000 - 33,500) = USD 2,411. With USD 2,500 withholding, refund before other items is USD 89.

```oa-check
name: New Mexico 2026 single taxable income
inputs:
  taxable: 60000
  withheld: 2500
steps:
  - tax: 1165.5 + (taxable - 33500) * 0.047
  - refund: withheld - tax
expected:
  tax: 2411
  refund: 89
```

**Case 2, filing-cycle eligibility decision.** Invented single retiree has federal AGI USD 100,000 including USD 20,000 federally taxable Social Security. Under verified 2025-2026 filing-cycle rules, the AGI ceiling is inclusive, so the USD 20,000 exclusion can apply. Compare a second otherwise identical case with AGI USD 100,001: the specific exclusion is unavailable. Before other deductions, the respective bases are USD 80,000 and USD 100,001, a USD 20,001 difference. This demonstrates the eligibility cliff, not final tax; confirm final 2026 ancillary rules before using for a 2026 filing.

```oa-check
name: New Mexico Social Security exclusion eligibility boundary
inputs:
  agi_eligible: 100000
  agi_over: 100001
  taxable_benefits: 20000
steps:
  - eligible_base: agi_eligible - taxable_benefits
  - over_base: agi_over
  - difference: over_base - eligible_base
expected:
  eligible_base: 80000
  over_base: 100001
  difference: 20001
```

## When to refuse or refer

Refer complex community-property allocation, PIT-B sourcing, credit certification, fiduciaries, amended-return disputes and oil/mineral taxes. Obtain final 2026 instructions before filing with an ancillary value identified here as 2025-2026 filing-cycle evidence. Do not reuse the old federal standard-deduction dollar figures.

## Filing and payment

Use **Taxpayer Access Point (TAP)** at https://tap.state.nm.us: choose personal income/PIT-1 and period, enter identification/status, federal starting amounts and NM adjustments, attach applicable PIT-ADJ/PIT-B/PIT-CR/PIT-RC, reconcile withholding/estimates, submit and retain acceptance. Pay the correct period and save its separate payment confirmation. Verified filing-cycle returns are due 15 April after year end with applicable nonbusiness-day relief; federal extension is recognized for filing, not a general payment extension. Calendar 2026 ordinarily reaches 15 April 2027; confirm final state instructions. Source: [PIT-1 due date, extensions and TAP filing](https://realfile.tax.newmexico.gov/2025pit-1-ins.pdf).

PIT-ES estimated installments use 15 April, 15 June, 15 September and 15 January following the year, with applicable nonbusiness-day adjustments. Use the PIT-ES payment type, retain voucher/payment records and test the USD 1,000 floor and 90%/100% comparison. Late filing/payment can incur 2% per month or part up to 20%, minimum USD 5; interest accrues on unpaid tax at the Department's published variable rate. Do not substitute an assumed 2026 interest rate. Source: [PIT-1 estimates, penalty and interest instructions](https://realfile.tax.newmexico.gov/2025pit-1-ins.pdf).

## Completion checklist

- Resident wages and business income included; residence/status and PIT-B requirement documented.
- Federal figures loaded from federal owner skills; state/local add-back and state adjustments reconciled.
- Social Security, age/blind and low/middle conditions tested, not flattened into unconditional exemptions.
- Final 2026 forms/gaps reviewed, accepted return and payment references retained.

## Sources

| Source and scope actually read | URL | Read on |
|---|---|---|
| Enacted HB252, 2024. Read section 5 / NMSA 7-2-7, pages 16 to 18, all three rate schedules; section 10 corporation rate; sections 42/43 applicability from 2025 onward. Read through official web PDF after direct fetch refused. | https://www.nmlegis.gov/Sessions/24%20Regular/final/HB0252.pdf | 2026-11-13 |
| 2025 PIT-1 instructions. Read filing/residency, PIT-B requirement, estimates, penalties, lines 9 to 30, low/middle worksheet and WFTC. 2025-2026 filing cycle. | https://realfile.tax.newmexico.gov/2025pit-1-ins.pdf | 2026-11-13 |
| 2025 PIT-ADJ instructions. Read additions, loss adjustments, U.S. obligation interest, age/blind Table 1, military retirement and Social Security Table 2. 2025-2026 filing cycle. | https://realfile.tax.newmexico.gov/2025pit-adj-ins.pdf | 2026-11-13 |

Not yet confirmed: final 2026 PIT-1/PIT-ADJ/PIT-B/PIT-CR/PIT-RC and their line numbers; later 2026 conformity changes to deductions/exemptions/credits, including final low/middle, age/blind, WFTC and military-retirement instructions; 2026 variable interest rate; old no-local-income-tax assertion; detailed technology-jobs/angel credit conditions. Old federal standard-deduction dollar figures were unsourced and are replaced by the federal-owner link; old unconditional Social Security exemption and reversed age-exemption AGI thresholds are corrected above. The old local GRT ranges and rates now route to `nm-sales-tax`. EY is not an authoritative source and is replaced by enacted HB252 and TRD publications.
