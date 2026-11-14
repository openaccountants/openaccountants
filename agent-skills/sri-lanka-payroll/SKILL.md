---
name: sri-lanka-payroll
description: "Use this skill whenever asked to run, check or explain Sri Lanka payroll for the year of assessment 2026/27 (1 April 2026 to 31 March 2027). Trigger on phrases like Sri Lanka payroll, APIT, APIT Table 01, PAYE Sri Lanka, EPF, ETF, 8% 12% 3%, minimum wage Sri Lanka, payslip Sri Lanka, employer contributions Sri Lanka, T-10 certificate. Gives monthly APIT on regular profits from primary employment (Rs. 150,000 monthly relief and the Table 01 formulas), EPF at 8% employee and 12% employer, ETF at 3% employer-only, the EPF earnings base, the Rs. 30,000 monthly and Rs. 1,200 daily national minimum wage from 1 January 2026, remittance and annual statement dates, and the penalties and surcharges."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/sri-lanka-payroll"
  jurisdiction: "LK"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Sri Lanka Payroll, year of assessment 2026/27, v1.0

Built from the law: not yet approved by an accountant. APIT figures come from the IRD's APIT Table 01, which the IRD publishes for the year of assessment that began on 1 April 2025; the individual rates and the relief in the Inland Revenue Act were not changed by the Inland Revenue (Amendment) Act No. 11 of 2026, and no separate 2026/27 tables were on the IRD site on 14 November 2026.

## Scope and who this is for

| Field | Detail |
| --- | --- |
| Country | Democratic Socialist Republic of Sri Lanka |
| Currency | Sri Lankan Rupee (LKR) only |
| Standard pay frequency | Monthly |
| Year of assessment | 1 April to 31 March (2026/27 = 1 April 2026 to 31 March 2027) |
| Income tax withholding | APIT (Advance Personal Income Tax), the PAYE-style monthly withholding under section 83 of the Inland Revenue Act No. 24 of 2017 (IRA) |
| Tax authority | Inland Revenue Department (IRD) |
| Provident fund | Employees' Provident Fund (EPF): EPF Department of the Central Bank of Sri Lanka, with the Department of Labour |
| Trust fund | Employees' Trust Fund Board (ETF Board) |
| Key legislation | IRA No. 24 of 2017 (as amended); Employees' Provident Fund Act No. 15 of 1958; Employees' Trust Fund Act No. 46 of 1980; National Minimum Wage of Workers Act No. 3 of 2016 as amended by Act No. 11 of 2025 |
| Filing channel | IRD e-Services |

- **In:** monthly APIT for resident employees and non-resident employees who are Sri Lankan citizens, on regular profits from primary employment (Table 01); EPF; ETF; the minimum wage floor.
- **Out:** lump-sum, arrears, terminal benefits, secondary employment and mid-year joiners (APIT Tables 02 to 08); annual personal tax (`sri-lanka-income-tax`); payments to non-employees (`sri-lanka-withholding-tax`); corporate tax (`sri-lanka-corporate-tax`).

## Ask the client first

1. Is the employee resident, or a non-resident Sri Lankan citizen, and is this the primary (or only) employment with a primary declaration given?
2. Gross monthly regular profits from employment (salary, allowances, non-cash benefits) for APIT.
3. Total monthly earnings for EPF and ETF (excluding overtime, reimbursable travel, incentive or bonus payments).
4. Any lump-sum, arrears, terminal payment or second employment this month?
5. Employer's EPF and ETF registration numbers; number of employees.

## The method, step by step

### Rates, bands and thresholds

| Item | Figure | Conditions | Source |
| --- | --- | --- | --- |
| APIT monthly relief | Rs. 150,000 a month, already built into Table 01 | Annual relief Rs. 1,800,000 | https://www.ird.gov.lk/en/publications/APIT_Tax_Tables/2025-2026/Table%20-%201/02.%20APIT_2526_Table_01_Text.pdf |
| APIT, monthly regular profits up to Rs. 150,000 | Relief from tax | Table 01 | same |
| APIT, over Rs. 150,000 to Rs. 233,333 | 6% of monthly regular profits less Rs. 9,000 | Table 01 | same |
| APIT, over Rs. 233,333 to Rs. 275,000 | 18% of monthly regular profits less Rs. 37,000 | Table 01 | same |
| APIT, over Rs. 275,000 to Rs. 316,667 | 24% of monthly regular profits less Rs. 53,500 | Table 01 | same |
| APIT, over Rs. 316,667 to Rs. 358,333 | 30% of monthly regular profits less Rs. 72,500 | Table 01 | same |
| APIT, over Rs. 358,333 | 36% of monthly regular profits less Rs. 94,000 | Table 01 | same |
| Annual slabs behind the table | 6% on the first Rs. 1,000,000 of taxable income, then 18%, 24%, 30% on Rs. 500,000 each, 36% on the balance | First Schedule paragraph 1(1D), years from 1 April 2025 | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf |
| EPF, employee | 8% of total monthly earnings, deducted from pay | No ceiling stated | https://epf.lk/?page_id=811 |
| EPF, employer | 12% of total monthly earnings | Paid wholly by the employer | same |
| EPF, total | 20% of total monthly earnings | | same |
| ETF, employer only | 3% of total monthly earnings | Must not be deducted from the employee | https://etfb.lk/employers-faq/ |
| National minimum monthly wage | thirty thousand rupees a month | From 1 January 2026; twenty-seven thousand rupees from 1 April 2025 to 31 December 2025 | https://www.parliament.lk/uploads/acts/gbills/english/6388.pdf |
| National minimum daily wage | one thousand two hundred rupees a day | From 1 January 2026; one thousand eighty rupees before | same |
| APIT remittance | Within 15 days after the end of the month | Section 86(1) | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf |
| APIT annual statement | Within 30 days after 31 March | Section 86(2) | same |
| Late payment penalty | 20% of tax due but not paid | Not paid within 14 days of the due date; section 179(1) | same |
| Late payment interest | one and one-half per cent per month or part month | Sections 157, 159(1) | same |
| Late filing penalty | Greater of 5% of tax owing plus 1% a month, or fifty thousand rupees plus ten thousand rupees a month; capped at four hundred thousand rupees | Section 178 | same |
| Statement format non-compliance | Up to two hundred thousand rupees a year, after a warning notice | New sections 86(9) and 178A, Act No. 11 of 2026 | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IR_Act_No_11-2026_E.pdf |
| EPF and ETF payment deadline | Last working day of the following month | | https://epf.lk/?page_id=811 |
| EPF and ETF late surcharge | 5% for up to 10 days; 15% for 11 days to 1 month; 20% for 1 to 3 months; 30% for 3 to 6 months; 40% for 6 to 12 months; 50% over 12 months | Same scale on both FAQ pages | same |
| EPF incomplete details surcharge | 2% of the total payment | Incomplete Form C or text files | same |
| ETF late half-yearly return | 1% surcharge for each delayed month on the face value of the return | Employers remitting on R1 | https://etfb.lk/employers-faq/ |

### Steps

1. Confirm Table 01 applies (resident or Sri Lankan citizen, primary employment). If not, stop and use the right APIT table.
2. APIT: take gross monthly regular profits (salary, wages, commission, overtime, allowances, non-cash benefits at fair market value, payments of the employee's bills). Do not deduct the relief again; apply the Table 01 formula for the band. Where monthly profits are under Rs. 150,000 but cumulative profits for the year pass Rs. 1,800,000, switch to Table 05 from that month.
3. EPF: total monthly earnings (salary, wages, fees, cost of living and similar allowances, holiday pay, cash value of food, food allowances, commissions, piece-rate and contract pay), excluding overtime, reimbursable travel and incentive or bonus payments. Employee 8%, employer 12%.
4. ETF: 3% of the same total monthly earnings, paid by the employer only.
5. Check pay against the Rs. 30,000 monthly or Rs. 1,200 daily minimum wage.
6. Remit APIT within 15 days after the month end; EPF and ETF by the last working day of the following month.
7. Issue APIT certificates and file the annual statement within 30 days after 31 March.

#### 2.3 No tax-free relief beyond LKR 150,000/month

- **Personal relief limit**: The relief is **LKR 150,000/month** (LKR 1,800,000/year). It is built into the formula; do **not** subtract it a second time. Gross at or below 150,000/month attracts **nil** APIT under Table 01.  _(IRD APIT Table 01 (states "Rs. 150,000.00 per month as personal relief has already been deducted"))_

#### 2.4 Regular profits from employment include

- **Regular profits from employment**: Wages, salary, commission, overtime, travel and other allowances, fees, pension; non-cash benefits (housing, conveyance, electricity, telephone, entertainment, etc., at fair market value); medical bills/insurance (with a limited exemption where dental/medical/health insurance is available to all full-time employees on equal terms); third-party payments made for the employee's benefit. Only Third Schedule exemptions (Inland Revenue Act No. 24 of 2017, as amended) apply.  _(IRD APIT Table 01)_


#### 3.2 EPF "total earnings" base

**EPF total earnings base**  _(EPF Employer FAQ)_

| Treatment | Items |
| --- | --- |
| **Included** | Salary/wages/fees; cost-of-living and special living allowances; holiday payments; cash value of food supplied by the employer; food allowances; commissions; piece-rate / contract payments: *EPF Employer FAQ* |
| **Excluded** | Overtime pay; reimbursable travelling expenses; incentive / bonus payments: *EPF Employer FAQ* |

- **EPF base ≠ APIT base**: APIT (rates table) is computed on full regular profits including overtime and many allowances; the EPF base **excludes** overtime, reimbursed travel and bonuses. Compute the two bases separately; never reuse the gross figure blindly.  _(EPF Employer FAQ)_


### Transaction / Payment Pattern Library

Deterministic mapping of Sri Lankan bank-statement narrations to payroll classifications. Match case-insensitively; longer/more specific patterns win. Statements are commonly in English; banks include Bank of Ceylon (BOC), People's Bank, Commercial Bank (Combank), Hatton National Bank (HNB) and Sampath Bank. Sinhala/Tamil narrations occasionally appear.

#### 8.1 Salary credits (employee side)

**Salary credits (employee side)**

| Narration pattern | Classification |
| --- | --- |
| `SALARY`, `SAL`, `PAY`, `NET SALARY`, `WAGES` | Net salary credit |
| `EMPLOYER [name] TRANSFER`, `STAFF SAL` | Net salary credit |
| `වැටුප` (Sinhala "salary"), `சம்பளம்` (Tamil "salary") | Net salary credit |
| `BONUS`, `INCENTIVE` | Supplement: taxable for APIT, **excluded** from EPF base |
| `OT`, `OVERTIME` | Overtime: taxable for APIT, **excluded** from EPF base |
| `EPF REFUND`, `ETF REFUND` | Fund adjustment: not income |

#### 8.2 Employer debit patterns (remittances)

**Employer debit patterns (remittances)**

| Narration pattern | Classification |
| --- | --- |
| `IRD APIT`, `APIT`, `PAYE`, `IRD PAYMENT` | APIT remittance to IRD |
| `EPF`, `EPF CONTRIBUTION`, `EPF 20%`, `PROVIDENT FUND` | EPF contribution (8% employee + 12% employer) |
| `ETF`, `ETF BOARD`, `TRUST FUND` | ETF contribution (3% employer-only) |
| `NET WAGES`, `PAYROLL`, `SALARY BATCH`, `STAFF SALARIES` | Net salary disbursement to employees |
| `SLIPS`, `PAYMENT VOUCHER IRD` | IRD payment voucher reference: tax remittance |

> **EPF vs ETF note:** an EPF remittance is 20% of the EPF base (8% deducted from staff + 12% employer); an ETF remittance is 3% employer-only. If a single line is labelled "EPF/ETF 23%", split it 20/3 before posting.


### Payslip examples

All examples use **APIT Table 01** (rates table), **EPF 8%/12%** (rates table) and **ETF 3%** (rates table). For simplicity each example assumes the EPF base equals the APIT gross (i.e. no overtime/bonus); where overtime or a bonus exists, the EPF base would be lower: see the note after Example 6. Every figure recomputed end-to-end.

#### Example 1: Minimum-wage earner (gross LKR 30,000/month, from 1 January 2026)

Statement line: `STAFF SAL EMP001 ... 27,600`

- **APIT:** 30,000 ≤ 150,000 → **LKR 0** (relief)
- **EPF employee (8%):** 8% × 30,000 = **LKR 2,400**
- **EPF employer (12%):** 12% × 30,000 = **LKR 3,600**
- **ETF employer (3%):** 3% × 30,000 = **LKR 900**
- **Net pay:** 30,000 − 0 − 2,400 = **LKR 27,600**
- **Total employer cost:** 30,000 + 3,600 + 900 = **LKR 34,500**

*Cross-check vs statement: net 27,600 matches the narration ✓.*

#### Example 2: At the personal relief (gross LKR 150,000/month)

- **APIT:** 150,000 = top of the Nil band → **LKR 0**
- **EPF employee (8%):** 8% × 150,000 = **LKR 12,000**
- **EPF employer (12%):** 12% × 150,000 = **LKR 18,000**
- **ETF employer (3%):** 3% × 150,000 = **LKR 4,500**
- **Net pay:** 150,000 − 0 − 12,000 = **LKR 138,000**
- **Total employer cost:** 150,000 + 18,000 + 4,500 = **LKR 172,500**

#### Example 3: First APIT band, 6% (gross LKR 200,000/month)

- **APIT:** 200,000 in band 150,001–233,333 → 6% × 200,000 − 9,000 = 12,000 − 9,000 = **LKR 3,000**
- **EPF employee (8%):** 8% × 200,000 = **LKR 16,000**
- **EPF employer (12%):** 12% × 200,000 = **LKR 24,000**
- **ETF employer (3%):** 3% × 200,000 = **LKR 6,000**
- **Net pay:** 200,000 − 3,000 − 16,000 = **LKR 181,000**
- **Total employer cost:** 200,000 + 24,000 + 6,000 = **LKR 230,000**

#### Example 4: 24% band (gross LKR 300,000/month)

- **APIT:** 300,000 in band 275,001–316,667 → 24% × 300,000 − 53,500 = 72,000 − 53,500 = **LKR 18,500**
- **EPF employee (8%):** 8% × 300,000 = **LKR 24,000**
- **EPF employer (12%):** 12% × 300,000 = **LKR 36,000**
- **ETF employer (3%):** 3% × 300,000 = **LKR 9,000**
- **Net pay:** 300,000 − 18,500 − 24,000 = **LKR 257,500**
- **Total employer cost:** 300,000 + 36,000 + 9,000 = **LKR 345,000**

#### Example 5: Top APIT band, 36% (gross LKR 500,000/month)

- **APIT:** 500,000 > 358,333 → 36% × 500,000 − 94,000 = 180,000 − 94,000 = **LKR 86,000**
- **EPF employee (8%):** 8% × 500,000 = **LKR 40,000**
- **EPF employer (12%):** 12% × 500,000 = **LKR 60,000**
- **ETF employer (3%):** 3% × 500,000 = **LKR 15,000**
- **Net pay:** 500,000 − 86,000 − 40,000 = **LKR 374,000**
- **Total employer cost:** 500,000 + 60,000 + 15,000 = **LKR 575,000**

#### Example 6: 18% band (gross LKR 250,000/month)

- **APIT:** 250,000 in band 233,334–275,000 → 18% × 250,000 − 37,000 = 45,000 − 37,000 = **LKR 8,000**
- **EPF employee (8%):** 8% × 250,000 = **LKR 20,000**
- **EPF employer (12%):** 12% × 250,000 = **LKR 30,000**
- **ETF employer (3%):** 3% × 250,000 = **LKR 7,500**
- **Net pay:** 250,000 − 8,000 − 20,000 = **LKR 222,000**
- **Total employer cost:** 250,000 + 30,000 + 7,500 = **LKR 287,500**

> **Overtime/bonus illustration.** If Example 4's LKR 300,000 comprised LKR 270,000 regular + LKR 30,000 overtime, APIT still applies to the full 300,000 (overtime is regular profits for APIT) → LKR 18,500, but the **EPF/ETF base** would be **270,000**: EPF employee 8% × 270,000 = 21,600; EPF employer 32,400; ETF 8,100. Always split the two bases.


### Tier 1 Rules (deterministic, always apply)

- **Tier 1 Rules**: 1. APIT is computed on **gross monthly regular profits** using **Table 01** (rates table) for resident / Sri Lankan-citizen-non-resident primary employment. 2. The personal relief is **LKR 150,000/month**, already built into the Table 01 formula: never deduct it twice. 3. EPF = **8% employee + 12% employer = 20%** of **total earnings** (rates table), **no floor, no ceiling**. 4. ETF = **3% employer-only** of total earnings (rates table): **never** deduct ETF from the employee. 5. The **EPF/ETF base excludes** overtime, reimbursed travel and bonuses; the **APIT base includes** them. Compute the two bases separately. 6. Currency is **LKR** only. 7. APIT is remitted by the **15th of the following month**; EPF and ETF by the **last working day of the following month**. 8. The minimum monthly wage is **LKR 27,000** (LKR 30,000 from 1 Jan 2026): flag any gross below it. 9. Every output is labelled **provisional / pending accountant sign-off**.


### Tier 2 Catalogue (reviewer judgement required)

**Tier 2 Catalogue**

| Item | Why it needs judgement |
| --- | --- |
| Selection between APIT Tables 01–08 | Lump-sum (Table 02), terminal (Table 03), mid-year joiner/retiree or sub-threshold-but-annual-over-1.8M (Table 05), Table 08 categories: fact-specific |
| Valuation of non-cash benefits (housing, vehicle, utilities) | Fair-market-value rules under the Inland Revenue Act not fully encoded here |
| Whether a medical/insurance benefit qualifies for the equal-terms exemption | Conditional on all full-time staff being covered on equal terms |
| Third Schedule exemptions | Item-by-item statutory analysis |
| Residence / citizenship for table eligibility | Non-Sri-Lankan-citizen non-residents fall outside Table 01 |
| Whether a specific allowance sits in the EPF base | The named exclusions are overtime, reimbursed travel and bonuses; edge cases need judgement |
| Gross-up where the employer bears the APIT | Iterative; depends on contract terms |
| Double-tax-treaty / expatriate relief | Treaty-by-treaty analysis |
| Mid-month joiners/leavers | Pro-ration and Table 05 interaction not encoded |


## Boundary and exception table

| Situation | Treatment |
| --- | --- |
| Overtime, reimbursed travel, bonus | In the APIT base; out of the EPF and ETF base |
| Monthly profits under Rs. 150,000 but cumulative over Rs. 1,800,000 | Table 05 from that month |
| Employee joins or leaves mid-year | Table 05 |
| Salary arrears | Table 02; tax credit under new section 96A (Act No. 11 of 2026) |
| Lump-sum or terminal payment | Table 02 or 03, not Table 01 |
| Medical or insurance benefit available to all full-time staff on equal terms | Not a regular profit for APIT (Table 01 note) |
| Government departments and local authorities | Not ETF contributors (ETF Board FAQ) |
| Social service organisation training minor offenders, destitute, deaf or blind persons | EPF exemption (EPF FAQ) |

### Conservative Defaults

When a required input is ambiguous and the user cannot supply it, apply the **most conservative** assumption (the one that maximises tax/contribution exposure or that forces a refusal), and label the output as provisional.

**Conservative defaults table**

| Unknown | Conservative default | Rationale |
| --- | --- | --- |
| Which APIT table applies | Use **Table 01** ONLY if primary-employment / single-employer is confirmed; otherwise refuse and ask | Tables 02–08 apply to arrears, terminal payments, secondary employment, mid-year joiners: different formulas |
| Whether a payment is "regular profits" for APIT | **Include** it in the APIT gross | APIT base is broad; over-withholding is recoverable, under-withholding leaves the employer liable to pay the tax anyway (section 86(3)) |
| Whether a payment is in the EPF "total earnings" base | **Include** unless it is overtime, reimbursed travel or a bonus | Those three are the named exclusions; everything else is in |
| Whether ETF applies | Assume **yes** (3% employer) for any covered employee | ETF has no headcount threshold |
| Pay frequency | **Monthly** | Standard Sri Lanka practice |
| Currency | **LKR** | Only legal payroll currency |
| Gross below the minimum wage | **Flag** as below LKR 30,000/month floor (from 1 January 2026; LKR 1,200/day) | A binding floor exists |
| Residence / citizenship for table selection | Refuse and ask | Table 01 covers residents and Sri Lankan-citizen non-residents only |


## Worked cases

### Case 1: employee with overtime, 24% band

Regular salary Rs. 270,000 plus overtime Rs. 30,000. APIT runs on the full Rs. 300,000 (24% band); EPF and ETF run on Rs. 270,000 because overtime is outside total earnings.

```oa-check
name: APIT, EPF and ETF with overtime, one month
inputs:
  salary: 270000
  overtime: 30000
steps:
  - apit_gross: salary + overtime
  - apit: apit_gross * 0.24 - 53500
  - epf_employee: salary * 0.08
  - epf_employer: salary * 0.12
  - etf: salary * 0.03
  - net_pay: apit_gross - apit - epf_employee
  - employer_cost: apit_gross + epf_employer + etf
expected:
  apit: 18500
  epf_employee: 21600
  epf_employer: 32400
  etf: 8100
  net_pay: 259900
  employer_cost: 340500
```

### Case 2: decision, is APIT due at all?

Two employees on Table 01: one at the Rs. 30,000 minimum wage, one at Rs. 250,000. The first is under the Rs. 150,000 relief, so APIT is nil but EPF and ETF still apply; the second is in the 18% band.

```oa-check
name: Minimum-wage employee against Rs. 250,000 employee
inputs:
  low: 30000
  high: 250000
steps:
  - apit_low: min(low, 0)
  - net_low: low - low * 0.08
  - cost_low: low * 1.15
  - apit_high: high * 0.18 - 37000
  - net_high: high - apit_high - high * 0.08
expected:
  apit_low: 0
  net_low: 27600
  cost_low: 34500
  apit_high: 8000
  net_high: 222000
```

### Test Suite

Each test states inputs and the expected output; recompute before trusting any change to this skill. EPF base = APIT gross unless stated; APIT from Section 2.2, EPF/ETF from Sections 3–4.

**Gross 30,000 (minimum wage from 1 January 2026).** Expect APIT = **0**; EPF emp = 2,400; ETF emp = 0; net = **27,600**; employer cost = 34,500. *(See Example 1.)*

**Gross 150,000 (at relief).** Expect APIT = **0**; EPF emp = 12,000; net = **138,000**; employer cost = 172,500. *(See Example 2.)*

**Gross 200,000.** Expect APIT = 6% × 200,000 − 9,000 = **3,000**; EPF emp = 16,000; net = **181,000**. *(See Example 3.)*

**Gross 250,000.** Expect APIT = 18% × 250,000 − 37,000 = **8,000**; EPF emp = 20,000; net = **222,000**. *(See Example 6.)*

**Gross 300,000.** Expect APIT = 24% × 300,000 − 53,500 = **18,500**; EPF emp = 24,000; net = **257,500**. *(See Example 4.)*

**Gross 500,000.** Expect APIT = 36% × 500,000 − 94,000 = **86,000**; EPF emp = 40,000; net = **374,000**. *(See Example 5.)*

**EPF/ETF total check, any base B.** Expect EPF employer 12% + employee 8% = **20% of B**; ETF employer = **3% of B**; total to funds = **23% of B**; no ceiling.

**ETF deducted from employee.** Expect: **refuse / flag**: ETF is employer-only (0% employee); never deduct from pay.

**Gross 300,000 with 30,000 overtime.** Expect APIT on full 300,000 = **18,500**; EPF base = 270,000 → EPF emp = 21,600, EPF er = 32,400, ETF = 8,100. *(See note after Example 6.)*

**Lump-sum / terminal payment.** Expect: **refuse / flag**: use Table 02/03, not the monthly Table 01 formula.

**Gross 26,000 below minimum wage.** Expect: **flag** as below the LKR 30,000/month floor (from 1 January 2026); APIT still 0 (≤150,000).


## When to refuse or refer

#### 7.1 Minimum required inputs

- **Minimum required inputs**: To compute Sri Lanka payroll for one employee for one month, you MUST have: 1. **Gross monthly regular profits** (in LKR) for APIT. 2. **Total monthly earnings** for EPF/ETF (may differ from APIT gross: exclude overtime, reimbursed travel, bonuses). 3. **Employee category** confirming **Table 01** applies (resident or Sri Lankan-citizen non-resident; single/primary employment). 4. **Month of pay** (to set remittance deadlines). 5. Confirmation of whether any allowance/benefit is exempt (Third Schedule) or excluded from the EPF base.

#### 7.2 Refusal Catalogue: REFUSE and ask if any of these hold

**Refusal Catalogue**

| Situation | Why refuse |
| --- | --- |
| APIT table / employment category not stated | Tables 01–08 have different formulas; never assume Table 01 silently |
| Currency given is not LKR | Payroll must be in LKR; silent FX conversion introduces error |
| Lump-sum / arrears / terminal payment present | These use Table 02/03, not the monthly Table 01 formula |
| APIT gross and EPF base conflated as one number | The bases differ (overtime, travel, bonus excluded from EPF) |
| Employee may have a second employment | Secondary employment uses a different table |
| Non-resident who is **not** a Sri Lankan citizen | Table 01 does not apply; different withholding rules |
| Asked to treat the result as final/filed advice | This is a Tier 2 skill pending sign-off |
| Asked to confirm APIT penalties beyond sections 157 to 179 | Only the penalties in the rates table are confirmed |

When refusing, state the missing input plainly and request it. Do not fabricate.


### PROHIBITIONS

- **Table 01 residency/employment condition**: NEVER apply Table 01 without confirming the employee is a resident or Sri Lankan-citizen non-resident on a single/primary employment: other categories use different tables.  _(PROHIBITIONS section)_
- **ETF employee deduction prohibition**: NEVER deduct ETF from the employee: it is a 3% employer-only contribution.  _(PROHIBITIONS section)_
- **Double relief prohibition**: NEVER subtract the LKR 150,000 personal relief a second time: it is already inside the Table 01 formula.  _(PROHIBITIONS section)_
- **APIT gross as EPF base without checks**: NEVER reuse the APIT gross as the EPF base without checking for overtime, reimbursed travel and bonuses (which are excluded from EPF).  _(PROHIBITIONS section)_
- **EPF/ETF ceiling or floor prohibition**: NEVER apply a ceiling or floor to EPF/ETF: the percentages apply to full total earnings.  _(PROHIBITIONS section)_
- **Currency restriction**: NEVER compute payroll in any currency other than LKR.  _(PROHIBITIONS section)_
- **Penalty figures**: use only the penalties in the rates table (sections 157, 159, 178, 179 and 178A of the IRA); anything else is not confirmed.
- **Deadline flagging requirement**: NEVER miss the 15th-of-following-month APIT deadline or the last-working-day EPF/ETF deadline without flagging penalty exposure.  _(PROHIBITIONS section)_
- **Minimum wage ignoring prohibition**: NEVER ignore the LKR 30,000/month (LKR 1,200/day) minimum wage in force from 1 January 2026 when a gross falls below it.  _(PROHIBITIONS section)_
- **Definitive computation prohibition**: NEVER present payroll computations as definitive: always label as estimated and direct to a Sri Lanka-qualified tax practitioner.  _(PROHIBITIONS section)_


## Filing and payment

| Obligation | Channel | Deadline |
| --- | --- | --- |
| APIT monthly remittance | Pay to the Commissioner-General, IRD e-Services or bank | Within 15 days after the end of the month (section 86(1)) |
| APIT annual statement and schedules | IRD e-Services, in the format the Commissioner-General specifies (section 86(9)) | Within 30 days after 31 March: 30 April 2027 for 2026/27 (section 86(2)) |
| Withholding certificate to each employee | Served free of charge (section 87(6)) | With the annual statement cycle; the earlier version said by 30 April or within 30 days of leaving (not confirmed) |
| EPF monthly contribution and Form C or e-Return | EPF Department, Central Bank of Sri Lanka | Last working day of the following month |
| EPF registration of a new employer | Form D to the Labour Office or Commissioner of Labour | Within 14 days of recruiting the first employee |
| EPF membership for a new employee | Include in that month's Form C or e-Return | Within 14 days of recruitment |
| ETF monthly contribution | ETF Board | Last working day of the following month |

### Excel Working Paper Template

Suggested column layout for a monthly Sri Lanka payroll working paper (one row per employee):

**Excel Working Paper Template columns**

| Col | Header | Formula / source |
| --- | --- | --- |
| A | Employee name | input |
| B | TIN | input |
| C | APIT table (confirm 01) | input |
| D | APIT gross / regular profits (LKR) | input |
| E | EPF/ETF base: total earnings (LKR) | input (exclude OT, reimbursed travel, bonus) |
| F | APIT band applied | lookup on D |
| G | APIT (LKR) | Table 01 formula (rates table) |
| H | EPF employee 8% (LKR) | `=ROUND(E*0.08,2)` |
| I | EPF employer 12% (LKR) | `=ROUND(E*0.12,2)` |
| J | ETF employer 3% (LKR) | `=ROUND(E*0.03,2)` |
| K | Net pay (LKR) | `=D-G-H` |
| L | Total employer cost (LKR) | `=D+I+J` |
| M | Remittance month | APIT 15th; EPF/ETF last working day |

- **APIT Table 01 formula (Excel)**: =IF(D<=150000,0, IF(D<=233333,D*0.06-9000, IF(D<=275000,D*0.18-37000, IF(D<=316667,D*0.24-53500, IF(D<=358333,D*0.30-72500, D*0.36-94000)))))  _(rates table)_

Reconcile column G against the worked examples before relying on the sheet. Note: K subtracts APIT and EPF employee only; ETF and EPF employer are employer costs (column L), not employee deductions.


### Bank Statement / Terminology Reading Guide (Sri Lanka)

**Terminology Reading Guide**

| Term / abbreviation | Meaning |
| --- | --- |
| LKR / Rs. | Sri Lankan Rupee |
| IRD | Inland Revenue Department (income tax / APIT) |
| APIT | Advance Personal Income Tax: the PAYE-style monthly withholding |
| PAYE | Older name for the employee-withholding system, often used interchangeably with APIT |
| TIN | Taxpayer Identification Number (employer and each employee) |
| EPF | Employees' Provident Fund (8% employee + 12% employer = 20%) |
| ETF | Employees' Trust Fund (3% employer-only) |
| T-10 / APIT Certificate | Annual earnings/tax certificate the employer must issue to each employee |
| BRA | Budgetary Relief Allowance: consolidated into the 2025 minimum wage |
| BOC / HNB / Combank | Bank of Ceylon / Hatton National Bank / Commercial Bank |
| Y/A | Year of Assessment (1 April – 31 March) |
| වැටුප / சம்பளம் | "Salary" in Sinhala / Tamil |


### Onboarding Fallback

- **Onboarding fallback questions**: If you lack a required input and cannot proceed, ask the user the following, in order, and stop until answered: 1. "Does **APIT Table 01** apply: is the employee a **resident or Sri Lankan-citizen non-resident** on a **single/primary** employment?" 2. "What are the employee's **gross monthly regular profits in LKR** (for APIT)?" 3. "What is the **total-earnings base for EPF/ETF**: does it differ from the APIT gross (overtime, reimbursed travel and bonuses are excluded from EPF)?" 4. "Which **month** is this pay run for (sets the remittance deadlines)?" 5. "Are any allowances or benefits **exempt (Third Schedule)** or excluded from the EPF base?" Do not estimate around a missing APIT table category or gross figure. Do not deduct ETF from the employee under any circumstance.


## Completion checklist

- [ ] Table 01 eligibility confirmed
- [ ] APIT base and EPF base computed separately
- [ ] EPF 8% and 12%, ETF 3% employer-only
- [ ] Pay at or above Rs. 30,000 a month (Rs. 1,200 a day)
- [ ] APIT by the 15th; EPF and ETF by the last working day; annual statement by 30 April

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Read for APIT Table 01 scope, regular profits, the Rs. 150,000 monthly relief, the Table 05 switch and the band formulas | https://www.ird.gov.lk/en/publications/APIT_Tax_Tables/2025-2026/Table%20-%201/02.%20APIT_2526_Table_01_Text.pdf | 2026-11-14 |
| Read for the list of APIT tables published by the IRD (none for a later year) | https://www.ird.gov.lk/en/publications/SitePages/apit_tax_tables.aspx?menuid=1503 | 2026-11-14 |
| Read for First Schedule paragraph 1(1D) and sections 86, 87, 157, 159, 178 and 179 in the IRD consolidated Act | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IRA_Cons_Act_-_2025_Changes.pdf | 2026-11-14 |
| Read for sections 14, 15, 21 and 30 (sections 86(9), 87(6), 96A, 178A) of the Inland Revenue (Amendment) Act No. 11 of 2026 | https://www.ird.gov.lk/en/publications/Acts_Income%20Tax_2017/IR_Act_No_11-2026_E.pdf | 2026-11-14 |
| Read for EPF rates, total earnings inclusions and exclusions, registration within 14 days, payment deadline, surcharges and the 2% incomplete details surcharge, on the EPF Department of the Central Bank of Sri Lanka site | https://epf.lk/?page_id=811 | 2026-11-14 |
| Read for the 3% ETF rate, employer-only rule, earnings base, deadline, surcharge scale and half-yearly return surcharge on the ETF Board employers page | https://etfb.lk/employers-faq/ | 2026-11-14 |
| Read for section 3 of the National Minimum Wage of Workers (Amendment) Act No. 11 of 2025 (Rs. 27,000 and Rs. 1,080 from 1 April 2025; Rs. 30,000 and Rs. 1,200 from 1 January 2026) on the Parliament site | https://www.parliament.lk/uploads/acts/gbills/english/6388.pdf | 2026-11-14 |

Not yet confirmed: an IRD APIT table set for 2026/27 (the 2025-2026 set is the latest; the underlying Act rates are unchanged); the APIT guideline PDF (it would not extract); the T-10 certificate deadline (30 April, or 30 days after leaving) from a secondary source; the employee-certificate form name; budgetary relief allowance treatment inside the minimum wage; gratuity rules; the EPF Act and ETF Act texts themselves (the rates are taken from the two funds' official FAQ pages); whether the cbsl.gov.lk EPF pages say the same (they refused scripted access).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `sri-lanka-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/sri-lanka-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
