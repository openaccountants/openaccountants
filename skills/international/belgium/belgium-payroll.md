---
name: belgium-payroll
description: "Belgian payroll for 2026: employee and employer social security (RSZ / ONSS), payroll withholding (bedrijfsvoorheffing / précompte professionnel), the social and fiscal work bonus, the structural reduction, the employer exemption above the quarterly pay ceiling, first-hire reductions, payslips, DmfA and withholding returns. Uses the RSZ administrative instructions 2026/3 and the income 2026 Income Tax Code: employee rate 13.07%, private-sector employer basic rate 24.92% (19.88% plus wage moderation for structural-reduction category 1), tax-free amount EUR 11,550. Trigger on: Belgian payroll, RSZ bijdragen, ONSS cotisations, bedrijfsvoorheffing, précompte professionnel, werkbonus, structurele vermindering, employer cost Belgium, DmfA, Belgian payslip, double holiday pay. Out of scope: be-employee-income-tax (the employee's annual return), be-social-contributions (self-employed), be-cross-border (posted and frontier workers)."
version: 1.2
jurisdiction: BE
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belgium Payroll

## Belgium Payroll Skill v1.1 (2026)

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any person's facts. Do not rely on it to run a payroll, file or pay without review by a qualified professional in Belgium.

The employee's annual income tax return, where the year's withholding is credited, is in `be-employee-income-tax`. Self-employed social contributions are in `be-social-contributions`.

The 2026 withholding computation (Annex III key formula, both 2026 rule sets, family reductions, holiday pay and bonus rates) is in `be-payroll-withholding`.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value | Source |
| --- | --- | --- |
| Country | Belgium | |
| Currency | EUR | |
| Tax year | Calendar year; income 2026 is assessment year 2027 | |
| Tax authority | FOD Financiën / SPF Finances | |
| Social security authority | RSZ (Rijksdienst voor Sociale Zekerheid) / ONSS | |
| Employee social security | 13.07% of gross pay (pensions 7.50, health care 3.55, benefits 1.15, unemployment 0.87); blue-collar pay declared at 108% | [RSZ instructions 2026/3, contributions](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html) |
| Employer basic contribution, private sector | 24.92% total rate; 19.88% for workers in category 1 or 3 of the structural reduction, plus wage moderation of at most 5.12% (4.27% + 4.27% of 19.88%), about 25% in all | [RSZ instructions 2026/3, contributions](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html) |
| Blue-collar holiday contribution | 5.57% quarterly with the other contributions, plus 10.27% once a year, on pay at 108% | [RSZ instructions 2026/3, contributions](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html) |
| Employer exemption above the pay ceiling | No basic employer contribution or wage moderation on ordinary pay (pay codes 1 and 61) above EUR 86,700 a quarter (January to June 2026) and EUR 88,434 a quarter (from 1 July 2026) | [RSZ instructions 2026/3, exemption above the pay ceiling](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/otheremployersreductions/partial_exemption_very_high_salaries.html) |
| Withholding | Bedrijfsvoorheffing, computed with the key formula in Annex III of the royal decree implementing the Income Tax Code | |
| Annual scale withholding is built on | 25% to EUR 16,720; 40% to EUR 29,510; 45% to EUR 51,070; 50% above | [Art. 130 WIB 92 (income 2026)](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796a4fc5-340e-4c89-a72a-88caa804ca96) |
| Tax-free amount | EUR 11,550 a year | [Art. 131 WIB 92 (income 2026)](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f3c5d665-cac4-4cbd-b714-bd287f791751) |
| Employee lump-sum expenses | 30% of pay after social security, at most EUR 6,070 a year | [Art. 51 WIB 92 (income 2026)](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e2fb1778-ac33-4e91-8e57-e53c0cac384c) |
| DmfA | Quarterly | |
| Skill version | 1.1 | |

## Section 2 -- Income Tax Withholding (Précompte Professionnel)

### Annual Income Tax Brackets (Income Year 2026, AY 2027)

**Annual Income Tax Brackets**  _(Art. 130 WIB 92, income 2026)_

| Taxable Income (EUR) | Marginal Rate |
| --- | --- |
| 0 -- 16,720 | 25% |
| 16,720 -- 29,510 | 40% |
| 29,510 -- 51,070 | 45% |
| Above 51,070 | 50% |

### Withholding Tax Mechanism

- **How withholding is computed**: Withholding is not the annual scale applied to one month. Annex III of the royal decree implementing the Income Tax Code (KB/WIB 92) sets a key formula that annualises the taxable pay (gross pay less employee social security), takes off a lump sum for expenses, applies the scale, deducts the tax on the tax-free amount and then reductions for family situation (single, married with one income, married with two incomes), dependent children and disability. The annual figures it approximates for income 2026 are the scale above, the tax-free amount of EUR 11,550 (art. 131) and the employee lump sum of 30% capped at EUR 6,070 (art. 51). The final tax is settled in the annual return (`be-employee-income-tax`).
- **Use the official tool or table**: Compute 2026 withholding with the Annex III key formula for 2026, set out with worked examples in `be-payroll-withholding`, or the FPS Finance simulator.

### Key Withholding Rules

**Key Withholding Rules**

| Rule | Detail |
| --- | --- |
| Calculation base | Gross pay minus employee social security (13.07%, less any social work bonus) |
| Social work bonus (werkbonus) | Cuts employee social security for low pay; see Section 3 |
| Fiscal work bonus | A tax credit of 33.14% of part A and 63% of part B of the social work bonus actually granted, at most EUR 2,000 a year (art. 289ter/1 WIB 92); withholding gives it during the year |
| Holiday pay, end-of-year premium, arrears | Taxed with withholding at special rates for exceptional pay, not the monthly key formula |

### Withholding Reductions

The 2026 monthly withholding reductions for dependent children, other dependants and disability are set in Annex III for 2026 and are not reproduced here. Do not use the amounts from earlier versions of this skill.

## Section 3 -- Social Security: Employee Deductions

**Employee Deductions**  _(RSZ instructions 2026/3)_

| Contribution | Rate | Base | Cap |
| --- | --- | --- | --- |
| Personal RSZ / ONSS | 13.07% | Gross pay (blue-collar: at 108%) | No cap |
| Special social security contribution | Withheld with the pay and settled in the annual assessment, scaled to household income | Household taxable income | See "Not yet confirmed" |

### Work Bonus (Werkbonus / Bonus à l'emploi)

The social work bonus cuts the 13.07% employee contribution for low pay. It has two parts, computed on the monthly reference pay S (gross pay at 100%, full-time equivalent), and the final bonus is the sum of both. It can never exceed the employee contribution; a shortfall is cut from part B first, then part A. From 1 July 2026 the total reduction is capped at EUR 3,594.36 per worker per calendar year. Source: [RSZ instructions 2026/3, work bonus](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/workers_reductions/workbonus.html).

| White-collar (bedienden), 2026 | Part A (low pay) | Part B (very low pay) |
| --- | --- | --- |
| Full amount | EUR 127.54 if S is EUR 2,937.93 or less | EUR 171.99 if S is EUR 2,300.62 or less |
| Tapering, July and August 2026 | 127.54 - 0.3196 x (S - 2,937.93), nil above EUR 3,336.98 | 171.99 - 0.2699 x (S - 2,300.62), nil above EUR 2,937.93 |
| Tapering, from 1 September 2026 | 127.54 - 0.2739 x (S - 2,937.93), nil above EUR 3,403.62 | 171.99 - 0.2699 x (S - 2,300.62), nil above EUR 2,937.93 |

Blue-collar workers (arbeiders, declared at 108%) get higher amounts on the same pay bands: part A EUR 137.74, tapering by 0.3452 x (S - 2,937.93) in July and August 2026 and by 0.2958 x (S - 2,937.93) from 1 September 2026; part B EUR 185.75, tapering by 0.2915 x (S - 2,300.62). The amounts for January to June 2026 are not shown on the 2026/3 page; see "Not yet confirmed". Part-time and incomplete months are converted to a full-time reference pay first (S = W / J x D, or W / H x U).

### Key Rules

- **Employee RSZ key rules**: Personal RSZ is deducted before computing taxable pay for withholding; it applies to all pay including bonuses and benefits in kind; there is no ceiling on employee contributions; the work bonus is deducted from the contribution, never paid out beyond it.

## Section 4 -- Social Security: Employer Contributions

**Employer Contributions**  _(RSZ instructions 2026/3)_

| Contribution | Rate | Notes |
| --- | --- | --- |
| Basic employer contribution, private sector | 24.92% | Total rate for all schemes |
| Category 1 or 3 of the structural reduction | 19.88% plus wage moderation 4.27% + 4.27% x 19.88% (5.12%) | About 25.00% in total; most private-sector workers |
| Employer share by branch | Pensions 8.86; health care 3.80; benefits 2.35; unemployment 1.46; occupational diseases 1.00; accidents at work 0.30 | Used to remove schemes that do not apply |
| Asbestos fund | 0.01% | Charged in quarters 1 to 3 of 2026 |
| Accidents at work (special) | 0.02% | |
| 1.60% contribution | 1.60% (1.69% with wage moderation) | Only employers with on average 10 or more workers in the reference period |
| Blue-collar annual holidays | 5.57% quarterly plus 10.27% yearly (15.84% in all, on pay at 108%) | Yearly part due 31 March, paid by 30 April |

Other special contributions (Closure Fund, company car CO2 contribution, extra-legal pension 8.86%) depend on the employer and are not totalled here.

### Employer Contribution Ceiling (from 1 July 2025)

**Exemption above the quarterly pay ceiling**  _(RSZ instructions 2026/3; programme law of 18 July 2025)_

| Parameter | Detail |
| --- | --- |
| Ceiling | EUR 85,000 a quarter to December 2025; EUR 86,700 from 1 January to 30 June 2026; EUR 88,434 from 1 July 2026 |
| What is exempt | The basic employer contribution (after removing non-applicable schemes) and wage moderation on ordinary pay (pay codes 1 and 61) above the ceiling, as reduction code 1360 |
| Still due | Special contributions and employee contributions on all pay; pay codes other than 1 and 61 |
| Part-time and short quarters | Absolute amounts per employer, not prorated by the work fraction; split by employment line if there are several |
| Excluded | From 1 July 2026, paid sportspeople who open the right to their target-group reduction |

### Structural Reduction (Structurele vermindering)

- **Formula**: Ps = R x µ x ßs, per quarter and employment line. For category 1 (general) from the 3rd quarter of 2026: R = 0.14 x (11,687.74 - S) + 0.16 x (9,738.14 - S), each part rounded to the cent and taken as nil if negative. S is the quarterly reference pay: for a full-time worker with a full quarter, S equals the quarter's pay and µ = 1, ßs = 1 (ßs = 1/µ from 80% work). Category 2 (social maribel) and category 3 (sheltered workshops) have their own formulas. Source: [RSZ instructions 2026/3, structural reduction](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/structuralreduction_targetgroupreductions/structuralreduction.html) and [introduction](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/structuralreduction_targetgroupreductions/introduction.html).

### Target Group Reductions

**First hires (eerste aanwervingen)**  _(RSZ instructions 2026/3; programme law of 30 May 2026)_

| Rule | Detail |
| --- | --- |
| First employee | Reduction for an unlimited period, capped at a flat EUR 2,000 a quarter (G21) from 1 July 2026, also for running reductions; it was EUR 3,100 (G20) from 2024 to June 2026 |
| 2nd to 5th employee | From 1 July 2026 again up to the 5th employee (3 from 2024 to June 2026); each for 12 quarters within 20 quarters |
| New employer | No employee subject to the 27 June 1969 law in the 12 months before the hire; technical business unit rules apply |

Source: [RSZ instructions 2026/3, first hires](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/structuralreduction_targetgroupreductions/firstengagments.html). Other target-group reductions (older workers, young workers, long-term unemployed) are regional or have their own conditions and are not covered here.

## Section 5 -- Minimum Wage and Overtime

### Minimum Wage (GGMMI / RMMMG)

The guaranteed average minimum monthly income (GGMMI) is set by collective agreement no. 43 of the National Labour Council and indexed. Read the current amount from the National Labour Council before using it; it is not restated in this update.

- **Minimum wage additional rules**: Set by CAO nr. 43 of the National Labour Council (NAR/CNT); Applies to employment contracts of at least one month; Sectors often have higher minimums via joint committee (CP/PC) agreements; Indexed automatically when pivot index is exceeded; Students under 21 and workers under 18 have separate scales (CAO nr. 50)  _(CAO nr. 43; CAO nr. 50)_

### Working Hours and Overtime

**Working Hours and Overtime**

| Parameter | Standard |
| --- | --- |
| Standard working week | 38 hours |
| Maximum daily hours | 9 hours (extendable to 11 in certain sectors) |
| Overtime premium (first 2 hours) | 50% supplement |
| Overtime on Sundays/holidays | 100% supplement |
| Voluntary overtime (no reason) | Up to 120 hours/year (extendable to 360) |
| Internal overtime limit | 143 hours above normal before mandatory rest |

## Section 6 -- Mandatory Benefits

**Mandatory Benefits**

| Benefit | Detail |
| --- | --- |
| Annual holiday | 20 days (based on prior year's work) |
| Single holiday pay | Normal salary during vacation |
| Double holiday pay | 92% of gross monthly salary (paid in May/June) |
| 13th month / end-of-year premium | Sector-dependent (most CPs mandate it) |
| Guaranteed salary (illness) | 30 days at full pay (white-collar); 7/7/14 days (blue-collar) |
| Meal vouchers | Electronic vouchers granted from 1 January 2026: employer share at most EUR 8.91 per voucher, employee share at least EUR 1.09, one voucher per day actually worked ([art. 38/1, §2 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796974b3-6cc3-458b-bd22-a129b359909b)) |
| Eco-cheques | At most EUR 250 per worker per year, EUR 10 per cheque ([art. 38/1, §4 WIB 92](https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796974b3-6cc3-458b-bd22-a129b359909b)) |
| Commuting allowance | Mandatory (amount depends on transport mode and CP) |
| Group insurance (2nd pillar pension) | Common via sector or company plan |
| Hospitalisation insurance | Widespread (not strictly mandatory but often via CP) |

### Statutory Holidays (2026)

Belgium has 10 legal public holidays. If a holiday falls on a weekend or rest day, it must be replaced by another paid day off.

## Section 7 -- Payslip Requirements

Belgian employers MUST issue a payslip (fiche de paie / loonfiche) for each salary payment. Required elements:

**Payslip Required Elements**

| Element | Mandatory |
| --- | --- |
| Employer identification (name, address, ONSS number) | Yes |
| Employee identification (name, NISS/INSZ number) | Yes |
| Pay period | Yes |
| Gross salary | Yes |
| All salary components (base, premiums, overtime, BIK) | Yes |
| ONSS employee deduction (13.07%) | Yes |
| Work bonus (if applicable) | Yes |
| Taxable base (after ONSS) | Yes |
| Précompte professionnel withheld | Yes |
| Special social security contribution | Yes |
| Net salary | Yes |
| Employer contributions (information) | Recommended |
| Meal vouchers / eco-cheques (if applicable) | Yes |
| Holiday pay details (when paid) | Yes |
| Cumulative year-to-date figures | Recommended |

### Annual Tax Documents

**Annual Tax Documents**

| Document | Deadline |
| --- | --- |
| Fiche 281.10 (employment income) | 28 February of following year |
| Fiche 281.20 (directors' income) | 28 February of following year |

## Section 8 -- Filing Obligations

**Filing Obligations**

| Filing | Frequency | Deadline | Authority |
| --- | --- | --- | --- |
| DmfA (quarterly social security declaration) | Quarterly | Last day of month after quarter end | ONSS/RSZ |
| Précompte professionnel (withholding tax) | Monthly | 15th of following month | SPF Finances |
| Dimona (employment start/end declaration) | Per event | Day of start/end of employment | ONSS/RSZ |
| Fiche 281.10/20 | Annual | 28 February | SPF Finances |
| Work accident declaration | Per event | Within 8 calendar days | Fedris |

### DmfA Details

**DmfA Details**

| Parameter | Detail |
| --- | --- |
| Content | Worker data, salary, working days, contributions per employee |
| Submission | Electronic via ONSS portal or batch file |
| Penalties | Flat-rate penalty + interest for late/incorrect filing |
| Payment | Same deadline as filing (end of month after quarter) |
| Correction | Modification DmfA possible within limitation period |

### Key Annual Calendar

**Key Annual Calendar**

| Month | Obligation |
| --- | --- |
| January | DmfA Q4 prior year; monthly PP |
| February | Fiches 281.10/20 deadline |
| April | DmfA Q1 |
| May/June | Double holiday pay processing |
| July | DmfA Q2 |
| October | DmfA Q3 |
| December | 13th month / end-of-year premium processing |

## Section 9 -- Worked Examples

### Example 1: white-collar employee, EUR 3,500 a month, third quarter of 2026

Facts: a full-time white-collar employee in the private sector, category 1 of the structural reduction, gross pay EUR 3,500 a month for July, August and September 2026, no other pay elements.

1. Employee social security: 13.07% x 3,500 = EUR 457.45 a month. No work bonus: the reference pay of EUR 3,500 is above EUR 3,336.98 (July and August) and EUR 3,403.62 (September).
2. Taxable pay for withholding: 3,500 - 457.45 = EUR 3,042.55 a month. Withholding itself comes from the 2026 Annex III formula; compute it with `be-payroll-withholding`.
3. Employer basic contribution at 19.88% + 5.12% = 25.00%: EUR 875.00 a month, EUR 2,625.00 for the quarter.
4. Structural reduction, quarter: S = 10,500. R = 0.14 x (11,687.74 - 10,500) = 166.28; the very-low-pay part is negative, so nil. Ps = EUR 166.28.
5. Net basic employer contributions for the quarter: 2,625.00 - 166.28 = EUR 2,458.72. Special contributions come on top.

```oa-check
name: White-collar EUR 3,500 a month, Q3 2026, employee RSZ and structural reduction
inputs:
  monthly_gross: 3500
  employee_rate: 0.1307
  employer_rate: 0.25
steps:
  - employee_ss: round(monthly_gross * employee_rate, 2)
  - taxable_pay: monthly_gross - employee_ss
  - quarter_pay: monthly_gross * 3
  - employer_quarter: quarter_pay * employer_rate
  - low_pay_part: max(round(0.14 * (11687.74 - quarter_pay), 2), 0)
  - very_low_pay_part: max(round(0.16 * (9738.14 - quarter_pay), 2), 0)
  - structural_reduction: low_pay_part + very_low_pay_part
  - employer_net: employer_quarter - structural_reduction
expected:
  employee_ss: 457.45
  taxable_pay: 3042.55
  employer_quarter: 2625.00
  structural_reduction: 166.28
  employer_net: 2458.72
```

### Example 2: low-paid white-collar employee, EUR 2,500 a month, September 2026

Facts: a full-time white-collar employee, category 1, gross pay EUR 2,500 a month in each month of the third quarter of 2026. The work bonus is shown for September 2026.

1. Work bonus part A: the reference pay of EUR 2,500 is under EUR 2,937.93, so the full EUR 127.54.
2. Work bonus part B: 171.99 - 0.2699 x (2,500 - 2,300.62) = EUR 118.18.
3. Social work bonus: 127.54 + 118.18 = EUR 245.72.
4. Employee social security: 13.07% x 2,500 = 326.75, less the bonus: EUR 81.03 withheld.
5. Fiscal work bonus earned by this month's social bonus (art. 289ter/1): 33.14% x 127.54 + 63% x 118.18 = 42.27 + 74.45 = EUR 116.72.
6. Employer, quarter: 25% x 7,500 = 1,875.00. Structural reduction: 0.14 x (11,687.74 - 7,500) = 586.28 plus 0.16 x (9,738.14 - 7,500) = 358.10, total EUR 944.38. Net basic employer contributions EUR 930.62.

```oa-check
name: White-collar EUR 2,500 a month, September 2026, work bonus and structural reduction
inputs:
  monthly_gross: 2500
  employee_rate: 0.1307
  employer_rate: 0.25
steps:
  - part_a: 127.54
  - part_b: round(max(min(171.99 - 0.2699 * (monthly_gross - 2300.62), 171.99), 0), 2)
  - work_bonus: part_a + part_b
  - employee_ss_gross: round(monthly_gross * employee_rate, 2)
  - employee_ss_net: employee_ss_gross - work_bonus
  - fiscal_bonus: round(part_a * 0.3314, 2) + round(part_b * 0.63, 2)
  - quarter_pay: monthly_gross * 3
  - employer_quarter: quarter_pay * employer_rate
  - structural_reduction: max(round(0.14 * (11687.74 - quarter_pay), 2), 0) + max(round(0.16 * (9738.14 - quarter_pay), 2), 0)
  - employer_net: employer_quarter - structural_reduction
expected:
  part_b: 118.18
  work_bonus: 245.72
  employee_ss_net: 81.03
  fiscal_bonus: 116.72
  structural_reduction: 944.38
  employer_net: 930.62
```

### Holiday Pay and Company Cars

- **Holiday pay**: Blue-collar workers receive holiday pay through the holiday fund, financed by the 15.84% contribution on pay at 108%. White-collar workers receive single and double holiday pay from the employer; the double holiday pay carries employee social security and is subject to withholding at the rate for exceptional pay.
- **Company car**: The benefit in kind (CO2-based) is added to taxable pay for withholding, and the employer owes the monthly CO2 solidarity contribution ([RSZ instructions 2026/3, company cars](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/special_contributions/companycar.html)). The 2026 amounts are not reproduced here.

## Section 10 -- Interaction with Other Skills

**Interaction with Other Skills**

| Skill | Interaction |
| --- | --- |
| be-employee-income-tax | The employee's annual return; withholding and the fiscal work bonus are credited there |
| belgium-bookkeeping | Payroll journal entries, accruals for holiday pay and the 13th month |
| be-cross-border | Posted workers, frontier workers, A1 certificates |
| payroll-workflow-base | General payroll workflow; Belgium-specific overrides in this skill |

### Belgium-Specific Payroll Considerations

- **Indexation**: Belgian pay is indexed automatically under sector agreements when the index moves; the timing depends on the joint committee.
- **Joint Committees (PC / CP)**: Over 100 joint committees set sector minimum pay, premiums and benefits. Always identify the joint committee before running a payroll.

## Sources

| Source | URL | Read on |
|---|---|---|
| RSZ, administrative instructions 2026/3, social security contributions | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html | 2026-10-23 |
| RSZ, administrative instructions 2026/3, work bonus | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/workers_reductions/workbonus.html | 2026-10-23 |
| RSZ, administrative instructions 2026/3, structural reduction | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/structuralreduction_targetgroupreductions/structuralreduction.html | 2026-10-23 |
| RSZ, administrative instructions 2026/3, reductions introduction (S, µ, ß) | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/structuralreduction_targetgroupreductions/introduction.html | 2026-10-23 |
| RSZ, administrative instructions 2026/3, exemption above the pay ceiling | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/otheremployersreductions/partial_exemption_very_high_salaries.html | 2026-10-23 |
| RSZ, administrative instructions 2026/3, first hires | https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/deductions/structuralreduction_targetgroupreductions/firstengagments.html | 2026-10-23 |
| Fisconetplus, art. 51 WIB 92 (income 2026), lump-sum expenses | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/e2fb1778-ac33-4e91-8e57-e53c0cac384c | 2026-10-23 |
| Fisconetplus, art. 130 WIB 92 (income 2026), tax scale | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796a4fc5-340e-4c89-a72a-88caa804ca96 | 2026-10-23 |
| Fisconetplus, art. 131 WIB 92 (income 2026), tax-free amount | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f3c5d665-cac4-4cbd-b714-bd287f791751 | 2026-10-23 |
| Fisconetplus, art. 38/1 WIB 92, meal vouchers and eco-cheques (version for vouchers granted from 1 January 2026) | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796974b3-6cc3-458b-bd22-a129b359909b | 2026-10-23 |
| Fisconetplus, art. 289ter/1 WIB 92 (income 2026), fiscal work bonus | https://eservices.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5403364d-120e-4c43-8945-ac770f1228f6 | 2026-10-23 |

Not yet confirmed: the special social security contribution scale for 2026; the work bonus amounts for January to June 2026; the 2026 minimum wage (GGMMI) under collective agreement no. 43, which is not restated here; the company car CO2 contribution for 2026. Sections 5 to 8 (minimum wage, working time, benefits, payslips and filing deadlines) were not re-read against 2026 sources in this update, except the meal voucher and eco-cheque limits.
