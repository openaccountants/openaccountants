---
name: my-pcb
description: Use this skill whenever asked about Malaysia PCB (monthly tax deduction, MTD) from wages or CP500 instalment payments for 2026. Trigger on phrases like PCB, Potongan Cukai Bulanan, monthly tax deduction Malaysia, MTD 2026, CP39, TP1, Form EA, CP500, CP502, instalment tax Malaysia, self-employed tax payment Malaysia, e-PCB Plus, LHDN instalments, advance tax Malaysia, or any question about paying income tax during the year in Malaysia. Covers the LHDN 2026 computerised MTD formula and Table 1, rounding, non-resident 30% deduction, employer liability, Form EA, CP500 instalments under section 107B, revision by 30 June and 31 October, and the 10% increases. Year of assessment 2026.
version: "2.1"
jurisdiction: MY
tax_year: 2026
tax_year_notes: "Calendar 2026 payroll and CP500 instalments for year of assessment 2026."
last_updated: 2026-11-22
depends_on:
  - my-income-tax
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
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
2. P is the estimated annual chargeable income. Add prior normal and additional remuneration, including pay from previous employers this year, current normal remuneration and projected normal remuneration for the remaining months. Deduct qualifying EPF or approved scheme contributions and the reliefs D (individual), S (spouse, category 2), DU, SU, Q x C (children) and prior and current allowable TP1 deductions. The annual EPF relief limit is RM4,000. For each remaining month, K2 is the lower of this month's qualifying EPF (K1) and the unused annual limit divided by the number of remaining months. Omit the projection in December.
3. Find M, R and B in Table 1 below from P. B already nets off the RM400 rebate (RM800 for category 2) in the two lowest bands.
4. Z is zakat paid earlier in the year. X is MTD paid earlier in the year, including by a previous employer. Exclude voluntary extra MTD requested by the employee and tax instalments such as CP38 from X.
5. Truncate calculations to two decimals. Round MTD up to the next multiple of 5 sen if it is between multiples. For example, 0.01 to 0.04 goes to 0.05 and 0.06 to 0.09 goes to 0.10.
6. If the MTD before zakat is under RM10, no deduction is required.
7. Net MTD equals the month's MTD less the month's zakat, with a minimum of zero. If MTD was at least RM10 before deducting zakat, any positive balance remains payable.
8. Use the separate formula for additional remuneration such as bonuses, arrears and commissions outside regular monthly pay. The specification also gives separate formulas for approved returning experts, qualifying knowledge workers in a specified region and resident non-citizen C-suite employees of approved companies.

### PCB for a non-resident employee

MTD is 30% of taxable remuneration for an employee who is non-resident or whose residence is unknown. Exclude exempt allowances, benefits and perquisites. For payroll purposes, the specification applies the resident formula to Visit Pass (Temporary Employment) holders and expatriates with an employment contract of at least 182 days. Determine final tax residence under s. 7 separately.

### Employer duties

- Deduct MTD as the Director General directs (s. 107(1) and (2)). Submit the payroll data and remit by the 15th of the following month under rule 10(1). Use e-PCB Plus on MyTax or pay through a supported bank using the PCB/CP39 account number.
- Give each employee a statement of remuneration (Form EA) for 2026 on or before the last day of February 2027 (s. 83(1A)).
- An employer that fails to deduct is liable for the amount as a debt due to the Government (s. 107(4)). Failing to provide Form EA without reasonable excuse is an offence punishable on conviction by a fine of RM200 to RM20,000, imprisonment for up to 6 months or both (s. 120(1)(b)). Rule 17 covers late MTD remittance offences.

### CP500 for individuals (s. 107B)

1. LHDN sets the instalments by notice and may have regard to preceding assessments (s. 107B(2)). Employment income is excluded (s. 107B(1)).
2. Use the dates on the notice. LHDN's YA 2026 example shows 6 instalments every 2 months from 1 March 2026 through 1 January 2027.
3. File Form CP502 for a first variation by 30 June or 31 October 2026 and a second, if needed, by 31 October 2026. The amended notice (CP503X) allocates the revised total less instalments due before the variation over the remaining instalments.
4. An instalment unpaid 30 days after its due date is increased by 10% of the amount unpaid (s. 107B(3)). LHDN announced a YA 2026 concession against this non-payment penalty for individuals with both employment and non-employment income.
5. If LHDN varied the instalments and the assessed tax exceeds the revised total by more than 30% of that tax, apply a 10% increase to the excess above the 30% margin (s. 107B(4)). For mixed income, first exclude the employment share of assessed tax, calculated as assessed tax multiplied by employment statutory income divided by total income (s. 107B(4A)).
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
| Non-resident employee MTD | 30% of taxable remuneration | same |
| No MTD required below | RM10 a month before current-month zakat | same |
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

Case 1, PCB in January 2026. A single resident employee in category 1 earns RM6,000 a month and contributes RM660 in EPF under Part A of the Third Schedule. Assume only individual and EPF relief and no zakat. K2 is the lower of RM660 and (RM4,000 − RM660) ÷ 11, truncated to RM303.63. P = (6,000 − 660) + (6,000 − 303.63) × 11 − 9,000 = RM59,000.07. Table 1 gives M = 50,000, R = 11% and B = 1,500. MTD = ((59,000.07 − 50,000) × 11% + 1,500) ÷ 12, truncated to RM207.50. It is already a multiple of 5 sen.

```oa-check
name: PCB January 2026, single, RM6,000 salary
inputs:
  salary: 6000
  epf: 660
  epf_cap: 4000
  months_left: 11
  individual_relief: 9000
steps:
  - k2: floor(min((epf_cap - epf) / months_left, epf) * 100) / 100
  - p: (salary - epf) + (salary - k2) * months_left - individual_relief
  - mtd_cents: floor(((p - 50000) * 0.11 + 1500) / (months_left + 1) * 100)
  - mtd: ceil(mtd_cents / 5) * 5 / 100
expected:
  k2: 303.63
  p: 59000.07
  mtd: 207.50
```

Case 2, varying CP500. A consultant with only business income receives a YA 2026 notice for 6 instalments of RM1,400 from March 2026 to January 2027. LHDN approves a reduction from RM8,400 to RM4,500 after the consultant pays the March and May instalments. The remaining RM1,700 is payable in 4 instalments of RM425. Final tax of RM7,000 exceeds the revised total by RM2,500. The 30% margin is RM2,100. The increase is 10% of RM400, or RM40. The reduction retains RM2,925 in cash through December and a further RM975 in January. The unvaried payments would have exceeded the assessed tax by RM1,400, subject to any offsets. The highest final tax to the sen with no increase is RM6,428.57.

```oa-check
name: CP500 varied to RM4,500, final tax RM7,000
inputs:
  original: 8400
  varied: 4500
  final_tax: 7000
  instalments: 6
  paid_before_variation: 2
  instalments_in_2026: 5
steps:
  - original_payment: original / instalments
  - revised_payment: (varied - original_payment * paid_before_variation) / (instalments - paid_before_variation)
  - difference: final_tax - varied
  - margin: final_tax * 0.30
  - increase: max(difference - margin, 0) * 0.10
  - cash_freed_in_2026: (original_payment - revised_payment) * (instalments_in_2026 - paid_before_variation)
  - cash_freed_in_january: original_payment - revised_payment
  - safe_final_tax: varied / 0.70
expected:
  revised_payment: 425.00
  difference: 2500
  margin: 2100.00
  increase: 40.00
  cash_freed_in_2026: 2925
  cash_freed_in_january: 975
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
| MTD remittance with CP39 data | By the 15th of the following month | e-PCB Plus on MyTax, or a supported bank with the PCB/CP39 account number |
| Form EA to employees, 2026 | By 28 February 2027 | Employer |
| Employer return Form E, 2026 remuneration | Statutory deadline 31 March 2027 | e-E on MyTax with C.P.8D or the required prefill data |
| CP500 instalments | Dates on the notice | ByrHASiL, FPX or bank |
| CP502 variation | First by 30 June or 31 October 2026. Second by 31 October 2026 | Deliver to a HASiL office in person or by post, or submit through the Customer Feedback Form |

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
| Employer guide to rules 10 and 17 | https://www.hasil.gov.my/media/gvfnqbqh/majikan-2026.pdf | 2026-11-24 |
| Form CP502 and submission instructions | https://www.hasil.gov.my/wp-content/uploads/borang-cp502.pdf | 2026-11-24 |
| CP502 explanatory notes and YA 2026 schedule example | https://www.hasil.gov.my/wp-content/uploads/nota-penerangan-cp502.pdf | 2026-11-24 |
| YA 2026 CP500 non-payment penalty concession | https://www.hasil.gov.my/wp-content/uploads/20260105-kenyataan-media-hasil-konsesi-pengenaan-penalti-cp500-bg-individu-yg-menerima-pendapatan-penggajian.pdf | 2026-11-24 |
| Third Schedule to the EPF Act 1991, Part A wage band in Case 1 | https://www.kwsp.gov.my/documents/d/guest/bm-third_schedule_from_october2025 | 2026-11-24 |

Not yet confirmed: any 2027 e-filing or payment grace period, an automatic 10% increase for late employer MTD remittance, or a standard 5% to 10% uplift of prior-year tax for CP500.
