---
name: my-pcb
description: "Use this skill whenever asked about Malaysia PCB (monthly tax deduction, MTD) from wages or CP500 instalment payments for 2026. Trigger on phrases like PCB, Potongan Cukai Bulanan, monthly tax deduction Malaysia, MTD 2026, CP39, TP1, Form EA, CP500, CP502, instalment tax Malaysia, self-employed tax payment Malaysia, e-PCB Plus, LHDN instalments, advance tax Malaysia, or any question about paying income tax during the year in Malaysia. Covers the LHDN 2026 computerised MTD formula and Table 1, rounding, non-resident 30% deduction, employer liability, Form EA, CP500 instalments under section 107B, revision by 30 June and 31 October, and the 10% increases. Year of assessment 2026."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/my-pcb"
  jurisdiction: "MY"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Malaysia PCB (monthly tax deduction) and CP500 instalments, 2026

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Malaysia.

## Scope

Two ways income tax is paid during the year in Malaysia, for year of assessment (YA) 2026:

| System | Applies to | Who pays | Law |
| --- | --- | --- | --- |
| PCB / MTD (Potongan Cukai Bulanan) | Employment income and pensions | Employer deducts from pay and remits | ITA 1967 s. 107; Income Tax (Deduction from Remuneration) Rules 1994; LHDN MTD specification 2026 |
| CP500 instalments | Individuals with business, rental or other non-employment income (not employment income) | The taxpayer, to the schedule on the CP500 notice | ITA 1967 s. 107B |

Out of scope: the final income tax computation and reliefs (`my-income-tax`); EPF, SOCSO and EIS (`my-epf-socso`); company instalments under s. 107C (CP204, see `my-corporate-income-tax`); withholding tax on payments to non-residents (s. 107A and s. 109).

## Ask the client first

1. **Employer or self-employed?** PCB for an employer's staff; CP500 for an individual's own business income.
2. **Residence of each employee** for 2026. Not known to be resident means 30% of remuneration.
3. **Employee category and reliefs.** Single (1), married with non-working spouse (2), or married with working spouse, divorced, widowed or single with adopted child (3); number of qualifying children; any TP1 claims; zakat.
4. **Pay facts.** Monthly salary, bonuses and other additional remuneration, EPF deducted, month of the year.
5. **For CP500.** The notice amount and dates; expected 2026 tax; instalments already paid.

## The method, step by step

### PCB for a resident employee, normal remuneration (LHDN MTD specification 2026)

1. Monthly tax deduction for the current month = [((P - M) x R + B) - (Z + X)] / (n + 1).
2. P is the estimated chargeable income for the year: net remuneration paid to date, plus this month's net pay, plus this month's pay times the remaining months n, less the reliefs D (individual), S (spouse, category 2), DU, SU, Q x C (children) and other TP1 deductions LP. EPF counts only up to the yearly qualifying amount (RM4,000, see `my-income-tax`); K2 is the lower of this month's EPF and the unused balance spread over the remaining months.
3. Find M, R and B in Table 1 below from P. B already nets off the RM400 rebate (RM800 for category 2) in the two lowest bands.
4. Z is zakat paid earlier in the year; X is MTD already deducted this year (including by a previous employer).
5. Truncate to two decimals, then round up to the next 5 sen (0.01 to 0.04 goes to 0.05; 0.06 to 0.09 goes to 0.10).
6. If the MTD before zakat is under RM10, no deduction is required.
7. Net MTD = MTD for the month less zakat for the month.
8. Additional remuneration (bonus, arrears, commission) uses the separate additional-remuneration formula in the same specification; returning experts, knowledge workers in a specified region and C-suite non-citizens in approved companies have their own formulas.

### PCB for a non-resident employee

MTD is 30% of remuneration for an employee not resident or not known to be resident. Exempt allowances and perquisites are left out first. A foreign employee with a contract of 182 days or more is treated under the resident formula.

### Employer duties

- Deduct MTD as the Director General directs (s. 107(1) and (2)); remit with CP39 data, through e-PCB Plus on MyTax or internet banking using the PCB/CP39 account number.
- Give each employee a statement of remuneration (Form EA) for 2026 on or before the last day of February 2027 (s. 83(1A)).
- An employer that fails to deduct is liable for the tax it failed to deduct, as a debt due to the Government (s. 107(4)).

### CP500 for individuals (s. 107B)

1. LHDN fixes the instalments, usually from the tax assessed for the prior year (s. 107B(2)); employment income is excluded (s. 107B(1)).
2. Pay each instalment by the date on the notice.
3. The taxpayer may apply to vary the amount and number of instalments once by 30 June and once by 31 October of the year of assessment, or both (s. 107B(2) proviso; Form CP502).
4. An instalment unpaid 30 days after its due date is increased by 10% of the amount unpaid (s. 107B(3)).
5. If instalments were varied and the final tax exceeds total instalments by more than 30% of the final tax, the part of the difference above that 30% is increased by 10% (s. 107B(4)).
6. Instalments paid are credited against the final tax on Form B; the balance is due by 30 June 2027 (see `my-income-tax`).

### Rates, bands and thresholds

| Item | Figure | Source |
| --- | --- | --- |
| Table 1, P RM5,001 to 20,000: M / R / B (cat. 1 and 3) / B (cat. 2) | 5,000 / 1% / -400 / -800 | https://www.hasil.gov.my/wp-content/uploads/spesifikasi-kaedah-pengiraan-berkomputer-pcb-2026.pdf |
| Table 1, P RM20,001 to 35,000 | 20,000 / 3% / -250 / -650 | same |
| Table 1, P RM35,001 to 50,000 | 35,000 / 6% / 600 / 600 | same |
| Table 1, P RM50,001 to 70,000 | 50,000 / 11% / 1,500 / 1,500 | same |
| Table 1, P RM70,001 to 100,000 | 70,000 / 19% / 3,700 / 3,700 | same |
| Table 1, P RM100,001 to 400,000 | 100,000 / 25% / 9,400 / 9,400 | same |
| Table 1, P RM400,001 to 600,000 | 400,000 / 26% / 84,400 / 84,400 | same |
| Table 1, P RM600,001 to 2,000,000 | 600,000 / 28% / 136,400 / 136,400 | same |
| Table 1, P above RM2,000,000 | 2,000,000 / 30% / 528,400 / 528,400 | same |
| Non-resident employee MTD | 30% of remuneration | same |
| No MTD required below | RM10 a month | same |
| Rounding | up to the next 5 sen | same |
| Form EA to employees | by last day of February | https://www.hasil.gov.my/wp-content/uploads/Income-Tax-Act-1967-online-version-as-at-1-January-2026.pdf |
| CP500 variation windows | by 30 June and by 31 October | same |
| Late CP500 instalment, after 30 days | 10% of amount unpaid | same |
| Shortfall test after variation | 10% of the difference above 30% of tax payable | same |

## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Employee has only commission, no salary | The commission is the remuneration |
| Pay is daily or hourly | Total monthly pay is the remuneration |
| Employee joined from another employer in 2026 | Include the previous employer's pay, EPF and MTD in Y, K and X |
| Budget 2026 | LHDN states no change to the MTD formula for 2026; TP1 and TP3 forms were updated for new relief items |
| CP500 taxpayer also employed | Employment income stays under PCB; s. 107B(4) removes the employment share of tax from the shortfall test |
| Instalment late but then paid | The Director General may treat it as paid on its due date (s. 107B(3) proviso) |
| First year of business | LHDN may not issue a CP500 until it has an estimate; pay the balance with Form B |
| Paying more than the notice | Allowed; the excess is a credit |

## Worked cases

Case 1, PCB in January 2026. Single resident employee (category 1), salary RM6,000 a month, EPF 11% = RM660, no other reliefs or zakat. K2 = lower of RM660 and (RM4,000 - RM660) / 11 = RM303.64. P = (6,000 - 660) + (6,000 - 303.64) x 11 - 9,000 = RM59,000. Table 1: M = 50,000, R = 11%, B = 1,500. MTD = ((59,000 - 50,000) x 11% + 1,500) / 12 = RM207.50.

```oa-check
name: PCB January 2026, single, RM6,000 salary
inputs:
  salary: 6000
  epf: 660
  epf_cap: 4000
  months_left: 11
  individual_relief: 9000
steps:
  - k2: min((epf_cap - epf) / months_left, epf)
  - p: (salary - epf) + (salary - k2) * months_left - individual_relief
  - mtd: ((p - 50000) * 0.11 + 1500) / (months_left + 1)
expected:
  p: 59000.00
  mtd: 207.50
```

Case 2, decision: vary the CP500 down or keep paying? A consultant's CP500 for YA 2026 is 6 x RM1,400 = RM8,400, based on YA 2025. She expects 2026 tax of about RM4,500 and varies the instalments to RM4,500 by 30 June. Her final tax turns out to be RM7,000. Difference RM2,500; 30% of RM7,000 is RM2,100; the excess RM400 is increased by 10%, so the increase is RM40. If she had not varied, she would have paid RM8,400 during the year and waited for a RM1,400 refund. Varying freed RM3,900 of cash during 2026 at a cost of RM40. The figure that decides it is how far the final tax can exceed the varied total before the 30% margin is used up: here up to RM6,428.57 of final tax carries no increase.

```oa-check
name: CP500 varied to RM4,500, final tax RM7,000
inputs:
  original: 8400
  varied: 4500
  final_tax: 7000
steps:
  - difference: final_tax - varied
  - margin: final_tax * 0.30
  - increase: max(difference - margin, 0) * 0.10
  - cash_freed: original - varied
  - safe_final_tax: varied / 0.70
expected:
  difference: 2500
  margin: 2100.00
  increase: 40.00
  cash_freed: 3900
  safe_final_tax: 6428.57
```

## When to refuse or refer

| Code | Trigger | Message |
| --- | --- | --- |
| R-PCB-1 | Employee residence unknown | "I will apply 30% until residence is confirmed, as LHDN's specification requires." |
| R-PCB-2 | Returning expert, knowledge worker or C-suite formula | "These use separate LHDN formulas and approvals. Confirm the approval letter before computing." |
| R-PCB-3 | Company instalments (CP204) | "Companies pay under s. 107C. Use the corporate skill." |
| R-PCB-4 | Employer wants to stop deducting or to settle tax for the employee | "The employer is liable for tax it fails to deduct. Refer to a tax agent." |

Never: treat CP500 payments as a business expense (they are credits); advise skipping instalments; vary CP500 well below expected tax without showing the s. 107B(4) increase; apply a variation after 31 October; present results as final.

## Filing and payment

| Item | When | How |
| --- | --- | --- |
| MTD remittance with CP39 data | Monthly | e-PCB Plus on MyTax, or internet banking with the PCB/CP39 account number |
| Form EA to employees, 2026 | By 28 February 2027 | Employer |
| Employer return Form E, 2025 | By 31 March 2026 (e-Filing grace 1 month) | e-E on MyTax |
| CP500 instalments | Dates on the notice | ByrHASiL, FPX or bank |
| CP502 variation | By 30 June and/or by 31 October 2026 | MyTax |

## Completion checklist

- Category, children and residence recorded for each employee.
- EPF qualifying cap applied through K, K1, K2.
- MTD truncated, rounded up to 5 sen, and the RM10 floor tested.
- Previous employer figures included where relevant.
- CP500 amounts tied to the notice; variation dates diarised; s. 107B(4) margin computed.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for the 2026 MTD formula, definitions of P, M, R, B, Z, X, Table 1, categories, non-resident 30%, rounding and the RM10 floor, and the Budget 2026 note that the formula is unchanged: LHDN specification for MTD computerised calculation 2026 | https://www.hasil.gov.my/wp-content/uploads/spesifikasi-kaedah-pengiraan-berkomputer-pcb-2026.pdf | 2026-11-14 |
| Read for s. 83(1A) Form EA, s. 107 employer deduction and liability, s. 107B instalments, variation dates and increases: Income Tax Act 1967 as at 1 January 2026 | https://www.hasil.gov.my/wp-content/uploads/Income-Tax-Act-1967-online-version-as-at-1-January-2026.pdf | 2026-11-14 |
| Read for PCB payment channels and the PCB/CP39 account number | https://www.hasil.gov.my/en/majikan/pembayaran-pcb/ | 2026-11-14 |
| Read for the Form E due date in the 2026 filing programme | https://www.hasil.gov.my/wp-content/uploads/rf-filing-programme-for-2026.pdf | 2026-11-14 |
| Read for the late CP500 instalment and shortfall penalties | https://www.hasil.gov.my/en/perundangan/kesalahan-denda-dan-penalti/ | 2026-11-14 |

Not yet confirmed: the monthly MTD remittance deadline (old file: by the 15th of the following month; set by the Income Tax (Deduction from Remuneration) Rules 1994, not opened); the 10% increase for late MTD remittance and the fine for not furnishing Form EA (old file: up to RM20,000 or 6 months), not checked; the usual CP500 instalment months (old file: six bi-monthly instalments, 15 March to 15 January); LHDN's practice of uplifting the prior-year figure (old file: 5% to 10%).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `my-pcb` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/my-pcb. If neither is available, confirm every figure against the official source pages cited above before relying on it.
