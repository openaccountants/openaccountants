---
name: montenegro-payroll
description: "Montenegro employee payroll for tax year 2026. Covers salary income tax withheld on gross pay (0% to EUR 700 a month, 9% to EUR 1,000, 15% above), employee contributions (pension 10%, unemployment 0.5%), employer charges (pension 0% since October 2024, unemployment 0.5%, Labour Fund 0.2%), the municipal surtax (prirez, up to 13% of the tax, 15% in Podgorica and Cetinje) as an employer cost, the 0.27% Chamber of Economy and Chamber of Crafts dues, the disability-employment quota and levy, tax-free payments, the annual pension contribution ceiling and refund, the net minimum wage floors, the monthly IOPPD report by the 15th, payment timing, fines and late-payment interest. Includes twelve worked payroll calculations. Related skills: montenegro-social-contributions, montenegro-income-tax, me-cross-border."
version: 0.3
jurisdiction: ME
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Montenegro payroll, tax year 2026

This skill computes monthly payroll for employees in Montenegro in 2026: salary income tax withheld by the employer, employee and employer contributions, the municipal surtax, the other employer levies, the monthly IOPPD report and the year-end steps. The tax is personal income tax on personal earnings (porez na dohodak fizičkih lica, "PIT Law"). Contributions are under the Law on Compulsory Social Insurance Contributions ("Contributions Law"). The Ministry of Finance employment instruction sets the payroll calculation and payment rules. The Tax Administration (Poreska uprava) collects tax and contributions through the IRMS portal.

## Who this applies to

- **Employers and other payers of personal earnings.** The employer or payer calculates, withholds and pays the tax on every payment of personal earnings (PIT Law art. 46(1)-(2)) and files the monthly IOPPD report (art. 47(3); IOPPD Rulebook art. 4). A non-resident organisation without diplomatic immunity that has a seat or permanent unit in Montenegro has the same duty and pays when it pays the salary (art. 46(5)).
- **Personal earnings.** Salary, salary compensation and other receipts under labour rules; pay of board and body members employed by the payer; vouchers, shares, goods, benefits, debt forgiveness and the payer covering the employee's expenses; temporary and occasional work and supplementary work under labour rules (PIT Law art. 14(1)). The taxable amount is the gross receipt (art. 15).
- **Residents.** A person with domicile or centre of business and life interests in Montenegro, or present more than 183 days in the tax year. A person sent abroad to work for a Montenegrin resident or an international organisation stays resident (PIT Law art. 3).
- **Insured employees.** Employees, temporary and occasional workers and the other groups in Contributions Law arts. 5 and 7 pay pension (PIO) and unemployment contributions; the employer is a co-payer for employees (arts. 5(2), 7(2)).
- **Tax period.** The calendar year; salary tax is withheld monthly as advance payments (PIT Law arts. 7, 46(3)).
- **Exempt persons.** Foreign diplomats and consular staff, UN technical-assistance staff, honorary consuls for pay from the appointing state, and staff of international organisations who are not Montenegrin citizens or residents pay no PIT (PIT Law art. 6).
- **Out of this skill.** Insurance status, minimum contribution bases, entrepreneurs and the PIO refund procedure in detail: see [the social contributions skill](montenegro-social-contributions.md). Self-employment, rent, capital and the annual return: see [the income tax skill](montenegro-income-tax.md). Treaties and withholding on non-residents: see [the cross-border skill](me-cross-border.md). Corporate tax and VAT of the employer: see [the corporate income tax skill](me-corporate-income-tax.md) and [the VAT skill](montenegro-vat.md).

## Rates, bands and thresholds

| Item | Amount | Tax year | Source |
|---|---|---|---|
| Salary PIT, monthly gross personal earnings | 0% to EUR 700.00; 9% on EUR 700.01 to 1,000.00; 15% above EUR 1,000.00 (EUR 27 + 15% of the excess over 1,000) | 2026 (art. 10 as replaced by 160/25 from 1 Jan 2026; salary bands unchanged) | [PIT Law art. 10(1)(1)][pit]; [160/25 art. 3, 21][pit160]; [Instruction art. 3][instr] |
| PIT on self-employment income (annual, not payroll) | 0% to EUR 8,400; 9% to EUR 12,000; 15% above | 2026 | [PIT Law art. 10(1)(2)][pit] |
| PIT on property, capital, capital gains and other income (not payroll) | 15% | 2026 | [PIT Law art. 10(1)(3)][pit] |
| PIO (pension and disability), employee | 10% of gross (15% until 30 Sep 2024) | 2026 | [Contributions Law art. 15(1)][contrib]; [94/24 art. 1, 3][c94]; [Instruction art. 4][instr] |
| PIO, employer | 0% (5.5% until 30 Sep 2024) | 2026 | [Contributions Law art. 15(1)][contrib]; [94/24 art. 1, 3][c94]; [Instruction art. 5][instr] |
| Unemployment insurance | 0.5% employee + 0.5% employer | 2026 | [Contributions Law art. 18(1)][contrib]; [Instruction arts. 4-5][instr] |
| Health insurance contribution | none (the law lists only PIO and unemployment; IOPPD health columns are for periods to December 2021) | 2026 | [Contributions Law art. 2][contrib]; [IOPPD Rulebook, instructions cols. 10, 13][ioppd] |
| Labour Fund (Fond rada), employer | 0.2% of gross | 2026 | [Instruction art. 5][instr] |
| Additional PIO for service counted at an increased rate, employer | 6%, 9%, 12%, 18% or 28% by category (12 months counted as 14, 15, 16, 18 or 24) | 2026 | [Contributions Law art. 16][contrib] |
| Municipal surtax (prirez) | rate set by each municipality, up to 13% of the PIT; up to 15% in Podgorica (Glavni grad) and Cetinje (Prijestonica) | 2026 | [Local Self-Government Financing Law arts. 8-9][local]; [Instruction art. 6][instr] |
| Chamber of Economy membership dues | 0.27% of the gross salaries reported in IOPPD (entrepreneurs: 0.27% of GPP-FL self-employment income) | 2026 | [Chamber decision 151/25 points 1-3, 6][chamber] |
| Chamber of Crafts membership dues (persons in the Register of Craftsmen) | 0.27% on the same bases | 2026 (from 6 Mar 2026) | [Chamber of Crafts decision 30/26 arts. 1-3, 6][crafts] |
| Disability-employment quota | 20 to 50 employees: at least 1 person with disability; over 50: at least 5% of staff (below 0.5 rounds down, 0.5 and above rounds up) | 2026 | [Disability Employment Law art. 21][dis] |
| Special disability contribution | 20% of the prior-year average monthly salary in Montenegro for each quota place not filled; 5% of that average a month for an employer with more than 10 and fewer than 20 employees and no employee with disability | 2026 | [Disability Employment Law art. 22][dis] |
| Contribution-free winter supplies payment (zimnica) | up to 70% of the prior-year average monthly gross salary | 2026 (160/25, from 1 Jan 2026) | [Contributions Law art. 18a(2)][contrib]; [160/25 contributions art. 5, 8][c160] |
| PIO maximum annual base (excess refunded after year end) | EUR 75,453 for 2025; the 2026 amount is set later by Ministry rulebook | 2025 | [Contributions Law arts. 14, 22][contrib]; [Rulebook 134/25 art. 1][cap2025] |
| Net minimum wage floor | not below EUR 600 net (jobs up to qualification level V) or EUR 800 net (level VI and above); part-time pro rata | 2026 (floors from 1 Oct 2024; pro rata rule from 23 Apr 2026) | [Labour Law art. 101(2) as amended by 86/24 art. 2-3][lab86]; [51/26 art. 31][lab51] |
| IOPPD monthly report | by the 15th of the month for the previous month, electronically | 2026 | [PIT Law art. 47(3)][pit]; [IOPPD Rulebook arts. 5, 7][ioppd] |
| Contributions payment | with the salary payment; outer deadline the 15th of the month for the previous month | 2026 | [Instruction art. 7][instr]; [Contributions Law art. 21(1)][contrib] |
| Annual earnings statement to each employee | by 31 January for the previous year | 2026 | [PIT Law art. 47(1)][pit]; [Instruction art. 9][instr] |
| Late-payment interest | 0.03% a day to 17 Jul 2026; 5.4% a year from 18 Jul to 31 Dec 2026 | 2026 | [Tax Administration Law art. 95, before 104/26][tal-old]; [104/26 TAL arts. 20, 26][tal104]; [Tax Administration decision, 24 Jul 2026][kamata] |

The May 2026 amendment (Official Gazette 70/26, in force 21 May 2026) changed only the rate on gambling winnings to 12% (PIT Law art. 10(1)(4)); the salary bands are unchanged ([70/26 arts. 1, 3][pit70]).

## The taxable base

### PIT base and the monthly bands

PIT is charged on gross personal earnings (PIT Law art. 15). Contributions are not deducted before the tax. The monthly withholding base is the gross personal earnings of the calculation period (art. 46(3)), taxed at the art. 10(1)(1) bands (art. 46(4)). For monthly gross G:

`PIT = 0.09 × max(min(G, 1000) − 700, 0) + 0.15 × max(G − 1000, 0)`

The 0% band is part of the scale, not a separate allowance. When the same employee is paid several times in one month, add the payments for the month; do not apply a fresh zero band to each instalment. The employer's payroll record lists each payment and totals them by the 15th day after the month (Instruction art. 10). In IOPPD the tax on personal earnings is reported only through code 097, "personal earnings whose total gross exceeds EUR 700", while the earnings rows (code 001 salary, 006 sick pay up to 60 days and others) carry the contributions ([IOPPD Rulebook, instructions col. 4, 8 and code list][ioppd]). Code 097 repeats the base for the tax; it is not a second payment.

### Non-cash earnings

Benefits in kind are personal earnings (PIT Law art. 14(1)(4)). Their value is the nominal value of vouchers and shares, the market price of goods, the market price of services or benefits, or the cash amount of expenses the employer covers (art. 14(2)). Contributions are not charged on earnings in goods, gifts or benefits unless they replace unpaid salary (Contributions Law art. 18a(3)), so the PIT base and the contribution base can differ. Tax, contributions and surtax on non-cash earnings are paid no later than the last working day of the month in which the earnings arise (Instruction art. 7).

### Tax-free payments (PIT Law art. 5a)

| Payment | Tax-free up to |
|---|---|
| Domestic per diem; use of own car for business | amount set by Government regulation (art. 5a(1)) |
| Foreign per diem | amount set for state budget users (art. 5a(2)(2)) |
| Field allowance where accommodation and food are not provided | EUR 100 a month |
| Allowance for living apart from family | EUR 100 a month |
| Solidarity aid on death of the employee, a close family member or a retired worker | EUR 2,000 (EUR 1,500 until 31 Dec 2025; 160/25 art. 2) |
| Solidarity aid for serious illness, rehabilitation, medicines, treatment | EUR 1,000 |
| Severance on retirement | EUR 1,500 |
| Severance for redundancy | the lowest amount set by labour law |
| Pupil and student scholarships and loans | EUR 300 a month |
| Payment on the birth of an employee's child | EUR 1,000 (social-protection-law payments fully exempt) |
| Employer gifts to women employees for International Women's Day | EUR 100 a year |
| Gifts to employees' children up to age 15 | EUR 50 a year per child |
| Jubilee awards for 10 / 20 / 30 / 40 years of work | EUR 150 / 250 / 350 / 450 |
| Education costs of the employee linked to the employer's business | documented amount |
| One-off court-ordered compensation for a workplace accident; union social aid paid from union dues | full amount |

Only the excess over each limit is taxable personal earnings. Contributions are also not charged on severance, solidarity and social aid, the winter supplies payment up to the art. 18a(2) limit, the separate-living allowance, the newborn payment and jubilee awards (Contributions Law art. 18a(2)). IOPPD code 102 still describes the contribution-bearing part of zimnica as the amount above the minimum wage; since 1 January 2026 the law sets the limit at 70% of the prior-year average monthly gross salary, and the law prevails ([160/25 contributions art. 5][c160]).

### Contribution base

The contribution base is the employee's gross salary on which PIT is paid, including salary for work done, increased pay, salary compensation and other receipts under law, collective agreement or contract, and pay for work in working bodies (Contributions Law art. 3a). For employees it cannot be lower than the lowest monthly contribution base, which is the gross basic salary for the qualification category under the General Collective Agreement (arts. 4(21), 9(1), 11(1)). That floor and its figures are covered in [the social contributions skill](montenegro-social-contributions.md).

### PIO annual ceiling and refund

The PIO contribution is withheld every month on the full gross. The maximum annual base is set each year by Ministry of Finance rulebook, indexed to average salary growth (Contributions Law art. 14(3)-(4)); for 2025 it is EUR 75,453 ([Rulebook 134/25][cap2025]). An insured person whose PIO was paid on more than the annual maximum may claim a refund of the excess after the year ends, by the end of the following calendar year (art. 22). Employees file Form 1 with the tax office for the employer's seat; the office decides by decision and pays within 30 days of the decision ([Refund Rulebook 107/23 arts. 2-4][refund]). The ceiling covers PIO only: unemployment contributions and the Labour Fund charge have no ceiling.

### Net pay and employer cost

Gross pay (bruto) contains the net pay, the tax and the employee contributions (Instruction art. 2). The surtax is charged on the calculated tax and is an employer charge on the earnings, not a deduction from the employee (Instruction art. 6 and its calculation table; Local Self-Government Financing Law art. 8 places the obligation on legal and natural persons carrying on business in the municipality).

- Employee deductions: PIT + PIO 10% + unemployment 0.5%.
- Net pay: gross − employee deductions.
- Employer charges on top of gross: unemployment 0.5% + Labour Fund 0.2% + surtax (municipal rate × PIT), plus where they apply Chamber dues 0.27%, additional PIO under art. 16 and the special disability contribution.
- Total funding: gross + employer charges.

### Chamber dues

Members of the Chamber of Economy pay 0.27% of the gross salaries reported in IOPPD, with the IOPPD; entrepreneurs pay 0.27% of the self-employment income in their annual GPP-FL return, with that return (decision 151/25 points 1-3). Persons entered in the Register of Craftsmen under the Law on Crafts do not pay the Chamber of Economy dues once the register is established (point 4); they pay the Chamber of Crafts 0.27% on the same bases (decision 30/26 arts. 1-3). A craftsman doing the craft as a supplementary activity pays the Chamber of Crafts dues only for the persons doing the craft (art. 4). The Register of Craftsmen started operating on 1 March 2026 and craftsmen had to register by 1 June 2026 under Law on Crafts art. 20b ([municipal notice][artisan]). The dues are a business cost, never an employee deduction.

### Disability-employment quota and special contribution

An employer with 20 to 50 employees must employ at least one person with disability; above 50, at least 5% of staff, rounded (Disability Employment Law art. 21(1)-(3)). The 5% quota does not bind a newly founded employer for its first 24 months (art. 21(4)). A person with at least 80% disability counts as two (art. 21(5)). For each quota place not filled, the employer pays a special contribution of 20% of the average monthly salary in Montenegro in the year before payment, with each monthly payment of salaries (art. 22(1)-(2)). An employer with more than 10 and fewer than 20 employees and no employee with disability pays 5% of that average each month (art. 22(3)-(4), (6)). The contributions go to the budget account of the Fund for Professional Rehabilitation and Employment of Persons with Disability (art. 22(5)). Organisations and associations of persons with disability are exempt as employers (art. 22a). The Tax Administration checks the calculation and payment (art. 23), and the IOPPD has a separate line for headcount, employees with disability, base, rate and amount ([IOPPD instructions][ioppd]).

From 1 December 2026 the amendment in Official Gazette 122/25 applies. It applies from the start of unified disability assessment ([122/25 art. 10][dis122]), which Unified Disability Assessment Law art. 60 sets at 1 December 2026 ([unified assessment law art. 60][unified]; [92/26 art. 1][deferral]). From that date art. 21(5) is repealed (122/25 art. 9, new art. 48e) and an employee with a disability status and fourth-degree support need counts as two (122/25 art. 5). Employers keep rights obtained under the old rules until those rights end (new art. 48d). Persons whose status was set under the old law must apply for unified assessment within three years (unified assessment law art. 61).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Calculate, withhold and pay PIT | at every payment of personal earnings, under the rules in force on the payment date | [PIT Law art. 46(2)][pit] |
| Pay contributions and surtax | with the salary payment (Instruction art. 7); contributions no later than the 15th of the month for the previous month | [Instruction art. 7][instr]; [Contributions Law art. 21(1)][contrib] |
| Tax, contributions and surtax on non-cash earnings | by the last working day of the month the earnings arise | [Instruction art. 7][instr] |
| Monthly IOPPD report (all payers of personal earnings, also residents receiving salary from abroad) | by the 15th of the month for the previous month, through the Tax Administration's electronic service | [PIT Law art. 47(3)][pit]; [IOPPD Rulebook arts. 4, 5, 7][ioppd] |
| Amended IOPPD | must contain complete data for every person in that period's calculation, not only the changed rows | [IOPPD Rulebook art. 6][ioppd] |
| Chamber of Economy / Chamber of Crafts dues | when the IOPPD (or the entrepreneur's GPP-FL) is filed | [151/25 point 3][chamber]; [30/26 art. 3][crafts] |
| Special disability contribution | with each monthly payment of salaries | [Disability Employment Law art. 22][dis] |
| Annual statement of earnings and tax to each employee (Form OPD-2) | by 31 January for the previous year | [PIT Law art. 47(1)][pit]; [Instruction art. 9][instr] |
| Employee's annual PIT return, where required | by the end of April for the previous year | [PIT Law art. 43(2), (4)][pit] |
| PIO refund claim on the annual ceiling | after year end, by the end of the following year (2025 claims by 31 Dec 2026) | [Contributions Law art. 22][contrib]; [Refund Rulebook art. 3][refund] |

**Portal.** Since 12 January 2026 the Tax Administration takes reports through the IRMS portal (https://irms.tax.gov.me/). The old CRPS and TAXIS portals closed on 31 December 2025. The December 2025 IOPPD counted as on time if filed by 30 January 2026; that extension did not move any payment deadline ([Tax Administration notice, 30 Dec 2025][irms]).

**Annual return.** An employee with salary from one employer does not file. A resident must file by the end of April if, among other cases, they had personal earnings from two or more employers or payers whose combined monthly gross exceeded EUR 700, or income from abroad (PIT Law art. 43(4)(4)-(5)). For the multiple-employer case the tax office assesses the tax by decision within 30 days of the return (art. 43a).

**Records.** The employer keeps a payroll record per employee in date order: time of payment, earnings by type, tax and contributions calculated, withheld and paid, and surtax. It closes the record at year end or when the employee leaves (Instruction art. 10).

**Earlier-period pay.** Salary for earlier periods paid after a court decision or labour-dispute settlement is taxed and charged at the rates in force on the date it should have been paid (PIT Law art. 60k; Contributions Law art. 29b). Pay for periods before the IOPPD Rulebook applied, not paid by then, is reported on Form OPD-1 (IOPPD Rulebook art. 8).

## Penalties and interest

| Offence | Fine | Source |
|---|---|---|
| Legal person as payer fails to calculate, withhold or pay PIT at each payment; fails to give the employee or the tax office the earnings and tax data; files the IOPPD late | EUR 2,000 to 20,000; responsible person EUR 500 to 1,000 | [PIT Law art. 53a(1)-(2)][pit] |
| Legal person as payer fails to calculate, withhold or pay contributions by the 15th | EUR 2,000 to 20,000; responsible person EUR 500 to 1,000; entrepreneur EUR 1,000 to 6,000 | [Contributions Law art. 26][contrib] |
| Individual who must pay own contributions (citizen employed abroad, employee of an immune employer, farmer) pays late | EUR 250 to 2,000 | [Contributions Law art. 27][contrib] |
| Individual fails to file the annual PIT return by end April, or a resident paid from abroad or by an immune employer fails to calculate and pay the tax on time | EUR 500 to 2,000 | [PIT Law art. 53v][pit] |

**Interest.** Interest on unpaid or underpaid tax and contributions runs daily from the day after the due date, with no interest on interest (Tax Administration Law art. 95, applied by PIT Law art. 53 and Contributions Law art. 25). The rate was 0.03% a day until 17 July 2026. From 18 July 2026 (104/26) it is the ECB main refinancing rate on the first day of the half-year plus 3 points, set each half-year by the Tax Administration: 5.4% a year for 18 July to 31 December 2026 ([decision of 24 July 2026][kamata]).

## Cross-border points

- **Salary paid from abroad.** A resident who receives personal earnings directly from another state calculates the tax at the art. 10 bands and pays it within five days of receipt (PIT Law art. 46(7); Instruction art. 7), files the IOPPD (IOPPD Rulebook art. 4 point 7) and files the annual return (PIT Law art. 43(4)(4)).
- **Immune employers.** A resident employed by a foreign embassy or consulate, an international organisation or an office with diplomatic immunity calculates and pays the tax within five days of receipt (PIT Law art. 46(6)) and pays the contributions within five days if the payer does not (Contributions Law art. 21(7)).
- **Foreign tax credit and treaties.** A resident taxed abroad on foreign income gets a credit for the foreign tax, capped at the Montenegrin tax on that income (PIT Law art. 44). A double tax treaty takes precedence over the PIT Law (art. 45). Treaty relief from tax does not settle social insurance, which follows the Contributions Law and any social security agreement.
- **Contributions.** Montenegrin citizens employed in Montenegro by foreign or international employers or foreign missions, and foreigners employed in Montenegro by foreign employers, pay contributions unless a treaty provides otherwise (foreigners also not if insured under another state's rules). Foreigners working for international organisations or foreign missions pay only where a treaty provides (Contributions Law arts. 5(1)(6), (8), (9); 7(1)(4), (6), (7)). Employees posted abroad by a Montenegrin employer stay insured unless insured abroad or a treaty provides otherwise, and pay on the salary they would earn in Montenegro for the same work, not below the minimum base (arts. 5(1)(5), 9(3)).
- **Digital nomads.** A person with digital nomad status under the law on foreigners, paid by an employer not registered in Montenegro, is exempt from PIT and from contributions (PIT Law art. 32d; Contributions Law art. 18d as replaced by 160/25 art. 6). A foreign payer alone does not give the exemption; the status must be granted.
- **Expired relief.** The new-employee relief in PIT Law art. 32c (90%, 60% and 30% of the tax in 2021 to 2023) and IOPPD code 095 do not apply in 2026.

## Worked examples

All twelve examples are full months in 2026 (example 11 is the 2025 refund claimed in 2026), cash salary unless stated, ordinary employee status, no art. 16 additional PIO and no Chamber dues or disability contribution unless stated. The surtax rate is an input: the relevant municipality's decision sets it within the art. 8 caps. Each component is rounded to the cent.

### Example 1: ordinary salary EUR 2,000, surtax rate 15%

Gross 2,000 with a municipality using the 15% maximum (Podgorica or Cetinje). PIT = 27 + 15% × 1,000 = 177. Employee PIO 200 and unemployment 10. Net = 2,000 − 177 − 200 − 10 = 1,613. Employer unemployment 10, Labour Fund 4, surtax 15% × 177 = 26.55. Total funding 2,040.55. The surtax is in the employer's funding and is not deducted from net. Payments to the state (427.55) plus net equal total funding.

```oa-check
name: Montenegro ordinary cash payroll and payer reconciliation
inputs:
  gross: 2000
  local_rate: 0.15
steps:
  - pit: round(27 + (gross - 1000) * 0.15, 2)
  - employee_pio: round(gross * 0.10, 2)
  - employee_unemployment: round(gross * 0.005, 2)
  - net: gross - pit - employee_pio - employee_unemployment
  - employer_unemployment: round(gross * 0.005, 2)
  - labour_fund: round(gross * 0.002, 2)
  - prirez: round(pit * local_rate, 2)
  - specified_funding: gross + employer_unemployment + labour_fund + prirez
  - remittances: pit + employee_pio + employee_unemployment + employer_unemployment + labour_fund + prirez
  - cash_reconciliation: specified_funding - net - remittances
expected:
  pit: 177
  employee_pio: 200
  employee_unemployment: 10
  net: 1613
  employer_unemployment: 10
  labour_fund: 4
  prirez: 26.55
  specified_funding: 2040.55
  remittances: 427.55
  cash_reconciliation: 0
```

### Example 2: salary at the top of the 9% band, EUR 1,000, surtax rate 13%

PIT = 9% × 300 = 27. Net = 1,000 − 27 − 100 − 5 = 868. Surtax 13% × 27 = 3.51. Total funding = 1,000 + 5 + 2 + 3.51 = 1,010.51. Do not apply 9% to the whole 1,000 and do not deduct contributions before the tax.

```oa-check
name: Montenegro salary band ceiling
inputs:
  gross: 1000
  local_rate: 0.13
steps:
  - pit: round(max(min(gross, 1000) - 700, 0) * 0.09 + max(gross - 1000, 0) * 0.15, 2)
  - net: gross - pit - round(gross * 0.10, 2) - round(gross * 0.005, 2)
  - prirez: round(pit * local_rate, 2)
  - specified_funding: gross + round(gross * 0.005, 2) + round(gross * 0.002, 2) + prirez
expected:
  pit: 27
  net: 868
  prirez: 3.51
  specified_funding: 1010.51
```

### Example 3: lower band, EUR 800, surtax rate 13%

PIT = 9% × 100 = 9. Employee PIO 80, unemployment 4, net 707. Employer unemployment 4, Labour Fund 1.60, surtax 13% × 9 = 1.17. Total funding 806.77. At EUR 700 or less the tax and the surtax are nil, but contributions still apply.

```oa-check
name: Montenegro lower band salary
inputs:
  gross: 800
  local_rate: 0.13
steps:
  - pit: round(max(min(gross, 1000) - 700, 0) * 0.09 + max(gross - 1000, 0) * 0.15, 2)
  - employee_pio: round(gross * 0.10, 2)
  - employee_unemployment: round(gross * 0.005, 2)
  - net: gross - pit - employee_pio - employee_unemployment
  - employer_unemployment: round(gross * 0.005, 2)
  - labour_fund: round(gross * 0.002, 2)
  - prirez: round(pit * local_rate, 2)
  - specified_funding: gross + employer_unemployment + labour_fund + prirez
expected:
  pit: 9
  employee_pio: 80
  employee_unemployment: 4
  net: 707
  employer_unemployment: 4
  labour_fund: 1.60
  prirez: 1.17
  specified_funding: 806.77
```

### Example 4: net-to-gross in the 15% band, target net EUR 1,500

Above EUR 1,000, net = G − (27 + 0.15 × (G − 1,000)) − 0.105 × G = 0.745 × G + 123. Gross = (1,500 − 123) / 0.745 = 1,848.32. Recompute each component at the cent: PIT 154.25, PIO 184.83, unemployment 9.24, net 1,500.00. The factor holds only in this band, for cash salary at ordinary rates.

```oa-check
name: Montenegro upper band net to gross
inputs:
  target_net: 1500
steps:
  - gross: round((target_net - 123) / 0.745, 2)
  - pit: round(27 + (gross - 1000) * 0.15, 2)
  - employee_pio: round(gross * 0.10, 2)
  - employee_unemployment: round(gross * 0.005, 2)
  - actual_net: gross - pit - employee_pio - employee_unemployment
expected:
  gross: 1848.32
  pit: 154.25
  employee_pio: 184.83
  employee_unemployment: 9.24
  actual_net: 1500
```

### Example 5: benefit in kind, EUR 2,000 salary plus EUR 200 benefit

Cash salary 2,000 plus a benefit valued at market price 200 under art. 14(2), not replacing unpaid salary. PIT base 2,200, PIT 207. Contribution base 2,000 because art. 18a(3) excludes the benefit, so employee contributions 210. Cash net = 2,000 − 207 − 210 = 1,583, and the employee also receives the benefit.

```oa-check
name: Montenegro noncash benefit separate payroll bases
inputs:
  cash_gross: 2000
  taxable_benefit: 200
steps:
  - pit_base: cash_gross + taxable_benefit
  - contribution_base: cash_gross
  - pit: round(27 + (pit_base - 1000) * 0.15, 2)
  - employee_contributions: round(contribution_base * 0.10, 2) + round(contribution_base * 0.005, 2)
  - net_cash: cash_gross - pit - employee_contributions
expected:
  pit_base: 2200
  contribution_base: 2000
  pit: 207
  employee_contributions: 210
  net_cash: 1583
```

### Example 6: two employers in the same month

Employer A pays 1,200 (PIT 57) and employer B pays 800 (PIT 9). Combined monthly gross 2,000 is over EUR 700, so the employee files an annual return (art. 43(4)(5)) and the tax office assesses the tax (art. 43a). On the combined gross the monthly scale gives 177, so the difference for that month is 111. Each employer withholds only on its own payment.

```oa-check
name: Montenegro concurrent employers indicative tax difference
inputs:
  gross_a: 1200
  gross_b: 800
steps:
  - withheld_a: 27 + (gross_a - 1000) * 0.15
  - withheld_b: (gross_b - 700) * 0.09
  - total_gross: gross_a + gross_b
  - aggregate_pit: 27 + (total_gross - 1000) * 0.15
  - indicative_difference: aggregate_pit - withheld_a - withheld_b
expected:
  withheld_a: 57
  withheld_b: 9
  total_gross: 2000
  aggregate_pit: 177
  indicative_difference: 111
```

### Example 7: salary and sick pay rows, one tax row

Salary 1,500 (code 001) and employer-paid sick pay 500 (code 006) in the same month. Contributions are reported on each row: PIO 150 and 50. The tax is reported once, through code 097 on the combined 2,000: 177. The IOPPD column 7 bases add up to 4,000 because code 097 repeats the base, but the economic gross is 2,000 and net is 1,613. Each row does not get its own zero band.

```oa-check
name: Montenegro IOPPD salary and sick pay aggregate tax control
inputs:
  salary_base: 1500
  sick_base: 500
steps:
  - economic_gross: salary_base + sick_base
  - salary_pio: salary_base * 0.10
  - sick_pio: sick_base * 0.10
  - total_pio: salary_pio + sick_pio
  - employee_unemployment: economic_gross * 0.005
  - code_097_pit: 27 + (economic_gross - 1000) * 0.15
  - repeated_report_bases: salary_base + sick_base + economic_gross
  - net_cash: economic_gross - total_pio - employee_unemployment - code_097_pit
expected:
  economic_gross: 2000
  salary_pio: 150
  sick_pio: 50
  total_pio: 200
  employee_unemployment: 10
  code_097_pit: 177
  repeated_report_bases: 4000
  net_cash: 1613
```

### Example 8: Chamber of Economy dues on example 1

A Chamber member, not in the Register of Craftsmen, with the example 1 employee. Dues 0.27% × 2,000 = 5.40, paid with the IOPPD. Total funding rises from 2,040.55 to 2,045.95; net stays 1,613.

```oa-check
name: Montenegro Chamber contribution incremental payroll funding
inputs:
  salary_gross: 2000
  funding_before_chamber: 2040.55
  employee_net: 1613
steps:
  - chamber_due: round(salary_gross * 0.0027, 2)
  - expanded_specified_funding: funding_before_chamber + chamber_due
  - employee_net_after_employer_charge: employee_net
expected:
  chamber_due: 5.40
  expanded_specified_funding: 2045.95
  employee_net_after_employer_charge: 1613
```

### Example 9: entrepreneur's own Chamber dues

An entrepreneur member reports self-employment income of 15,000 in the GPP-FL. Dues 0.27% × 15,000 = 40.50, paid with that return. The base is the income in the return, not turnover and not the payroll.

```oa-check
name: Montenegro entrepreneur Chamber contribution
inputs:
  established_return_income: 15000
steps:
  - annual_chamber_contribution: round(established_return_income * 0.0027, 2)
expected:
  annual_chamber_contribution: 40.50
```

### Example 10: 15 employees and no employee with disability

October 2026, employer not exempt under art. 22a. The levy is 5% of the prior-year average monthly salary, once a month for the employer, not per employee. With an average-salary input of 1,000 (replace it with the published figure), the monthly charge is 50.

```oa-check
name: Montenegro smaller employer disability levy method
inputs:
  hypothetical_established_reference_base: 1000
steps:
  - monthly_employer_levy: hypothetical_established_reference_base * 0.05
expected:
  monthly_employer_levy: 50
```

### Example 11: PIO ceiling refund for 2025

An employee earned 7,000 gross every month of 2025 from one employer: 84,000 for the year, PIO withheld 8,400. The 2025 maximum annual base is 75,453, so PIO due on the capped base is 7,545.30 and the refund is 854.70. The employee claims it on Form 1 at the tax office for the employer's seat by 31 December 2026. The monthly payroll itself is not capped.

```oa-check
name: Montenegro 2025 PIO annual ceiling refund
inputs:
  monthly_gross: 7000
  months: 12
  annual_maximum_base_2025: 75453
steps:
  - annual_gross: monthly_gross * months
  - pio_withheld: round(annual_gross * 0.10, 2)
  - pio_on_maximum: round(min(annual_gross, annual_maximum_base_2025) * 0.10, 2)
  - refund: pio_withheld - pio_on_maximum
expected:
  annual_gross: 84000
  pio_withheld: 8400
  pio_on_maximum: 7545.30
  refund: 854.70
```

### Example 12: 80 employees, quota shortfall

October 2026, 80 employees, quota 5% = 4. Two employees with disability count once each (no 80% disability, not a new employer). Shortfall 2. With an average-salary input of 1,000, the monthly contribution is 2 × 20% × 1,000 = 400. From 1 December 2026 the double-count rule changes to the fourth-degree support test.

```oa-check
name: Montenegro disability quota shortfall employer levy
inputs:
  employee_count: 80
  established_qualifying_count: 2
  hypothetical_established_reference_base: 1000
steps:
  - required_count: employee_count * 0.05
  - shortfall: max(required_count - established_qualifying_count, 0)
  - monthly_employer_levy: shortfall * hypothetical_established_reference_base * 0.20
expected:
  required_count: 4
  shortfall: 2
  monthly_employer_levy: 400
```

## Ask the client first

1. In which municipality (or municipalities) does the employer carry on business, and what surtax rate does that municipality's decision set?
2. What does each employee receive in the month: cash salary, sick pay, benefits in kind, allowances or one-off payments (severance, jubilee, solidarity aid, newborn, zimnica)? Is any of it paid by another employer or from abroad?
3. Is the employer a member of the Chamber of Economy, or entered in the Register of Craftsmen?
4. How many employees does it have each month, how many have a recognised disability status (and at what percentage or support degree), and when was the employer founded?
5. Does any employee have digital nomad status, a foreign employer, a posting abroad or a job with service counted at an increased rate?
6. What qualification level does each job require (for the EUR 600 or EUR 800 net minimum)?

[pit]: https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0
[pit160]: https://wapi.gov.me/download/47bea12c-f250-4cdc-b481-3afc30fba94f?version=1.0
[pit70]: https://www.sluzbenilist.me/propisi/394390/download
[contrib]: https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0
[c160]: https://wapi.gov.me/download/9c7ab8f6-6971-48cb-9ac0-4d6f87ac48bb?version=1.0
[c94]: https://www.sluzbenilist.me/propisi/373700/download
[instr]: https://wapi.gov.me/download/f73befc2-975e-42d9-af00-4d5de0a3172d?version=1.0
[ioppd]: https://wapi.gov.me/download/28aa7760-8d39-440d-8874-1ffcc5773095?version=1.0
[local]: https://wapi.gov.me/download/98dd2203-4c4e-4751-bbb9-9ad1e13564bd?version=1.0
[chamber]: https://www.sluzbenilist.me/propisi/389055/download
[crafts]: https://www.sluzbenilist.me/propisi/391034/download
[artisan]: https://www.ul-gov.me/me/aktuelnosti/prijava-u-registar-zanatlija
[dis]: https://www.zzzcg.me/wp-content/uploads/2018/01/Zakon-o-profesionalnoj-rehabilitaciji-i.pdf
[dis122]: https://www.sluzbenilist.me/propisi/385768/download
[unified]: https://www.sluzbenilist.me/propisi/385760/download
[deferral]: https://www.sluzbenilist.me/propisi/395547/download
[cap2025]: https://www.sluzbenilist.me/propisi/387933/download
[refund]: https://www.sluzbenilist.me/propisi/362476/download
[lab86]: https://www.sluzbenilist.me/propisi/387096/download
[lab51]: https://www.sluzbenilist.me/propisi/393230/download
[tal-old]: https://wapi.gov.me/download/2dd530ac-eec4-4d0c-9d8f-0c9e7ebc5b86?version=1.0
[tal104]: https://wapi.gov.me/download/c22f3c59-7e52-4213-bbe4-3cd9d8d3a373?version=1.0
[kamata]: https://wapi.gov.me/download/6d6ec964-3dd6-4588-b81a-a5affc153f6e?version=1.0
[irms]: https://www.gov.me/clanak/vazno-obavjestenje-u-vezi-sa-pocetkom-primjene-novog-integrisanog-it-sistema-poreske-uprave-irms

## Sources

| Source | URL | Read on |
|---|---|---|
| PIT Law (Zakon o porezu na dohodak fizičkih lica), Ministry consolidation through 160/25: arts. 3, 5a, 6, 10, 14, 15, 32c, 32d, 43, 43a, 44-47, 53, 53a, 53v, 60k | https://wapi.gov.me/download/b8465a42-2073-4894-9be0-3b965c2f7195?version=1.0 | 2026-10-30 |
| PIT Law amendment, Official Gazette 160/25: arts. 2, 3, 21 (application from 1 Jan 2026) | https://wapi.gov.me/download/47bea12c-f250-4cdc-b481-3afc30fba94f?version=1.0 | 2026-10-30 |
| PIT Law amendment, Official Gazette 70/26: arts. 1-3 (gambling rate, in force 21 May 2026) | https://www.sluzbenilist.me/propisi/394390/download | 2026-10-30 |
| Contributions Law (Zakon o doprinosima za obavezno socijalno osiguranje), Ministry consolidation through 160/25: arts. 2, 3a, 4(21), 5, 7, 9, 11, 14-16, 18, 18a, 18d, 21, 22, 25-27, 29b | https://wapi.gov.me/download/97253561-f373-4456-a024-b15f6596a0f2?version=1.0 | 2026-10-30 |
| Contributions Law amendment, Official Gazette 160/25: arts. 5, 6, 8 | https://wapi.gov.me/download/9c7ab8f6-6971-48cb-9ac0-4d6f87ac48bb?version=1.0 | 2026-10-30 |
| Contributions Law amendment, Official Gazette 94/24: arts. 1, 3 (PIO 0% / 10% from 1 Oct 2024) | https://www.sluzbenilist.me/propisi/373700/download | 2026-10-30 |
| Ministry of Finance instruction on calculating and paying tax and contributions on employment earnings, through 103/24: arts. 2-10 | https://wapi.gov.me/download/f73befc2-975e-42d9-af00-4d5de0a3172d?version=1.0 | 2026-10-30 |
| Instruction amendment, Official Gazette 103/24: arts. 1-3 | https://www.sluzbenilist.me/propisi/374308/download | 2026-10-30 |
| IOPPD Rulebook with instructions and code list, through 124/24: arts. 4-8, columns 4-15, codes 001, 006, 095, 097, 102 | https://wapi.gov.me/download/28aa7760-8d39-440d-8874-1ffcc5773095?version=1.0 | 2026-10-30 |
| Local Self-Government Financing Law, consolidation through 149/25: arts. 4, 8, 9 (amendment 119/26 changes only art. 13) | https://wapi.gov.me/download/98dd2203-4c4e-4751-bbb9-9ad1e13564bd?version=1.0 | 2026-10-30 |
| Local Self-Government Financing Law amendment, Official Gazette 119/26: arts. 1-2 | https://www.sluzbenilist.me/propisi/397075/download | 2026-10-30 |
| Chamber of Economy decision on 2026 membership dues, Official Gazette 151/25: points 1-6 | https://www.sluzbenilist.me/propisi/389055/download | 2026-10-30 |
| Chamber of Crafts decision on 2026 membership dues, Official Gazette 30/26: arts. 1-6 | https://www.sluzbenilist.me/propisi/391034/download | 2026-10-30 |
| Municipality of Ulcinj notice on the Register of Craftsmen, 17 Apr 2026 | https://www.ul-gov.me/me/aktuelnosti/prijava-u-registar-zanatlija | 2026-10-30 |
| Law on Professional Rehabilitation and Employment of Persons with Disability (Disability Employment Law), through 55/16 (Employment Agency text): arts. 21, 22, 22a, 23 | https://www.zzzcg.me/wp-content/uploads/2018/01/Zakon-o-profesionalnoj-rehabilitaciji-i.pdf | 2026-10-30 |
| Amendment to that law, Official Gazette 122/25: arts. 5, 9, 10 | https://www.sluzbenilist.me/propisi/385768/download | 2026-10-30 |
| Unified Disability Assessment Law, Official Gazette 122/25: arts. 60, 61 | https://www.sluzbenilist.me/propisi/385760/download | 2026-10-30 |
| Amendment to the Unified Disability Assessment Law, Official Gazette 92/26: arts. 1-2 (start 1 Dec 2026) | https://www.sluzbenilist.me/propisi/395547/download | 2026-10-30 |
| Rulebook on the 2025 maximum annual contribution base, Official Gazette 134/25: art. 1 | https://www.sluzbenilist.me/propisi/387933/download | 2026-10-30 |
| Rulebook on PIO contribution refunds, Official Gazette 107/23: arts. 2-4 and Form 1 | https://www.sluzbenilist.me/propisi/362476/download | 2026-10-30 |
| Labour Law amendment, Official Gazette 86/24: arts. 2, 3 (art. 101(2) minimum wage floors from 1 Oct 2024) | https://www.sluzbenilist.me/propisi/387096/download | 2026-10-30 |
| Labour Law amendment, Official Gazette 51/26: art. 31 (art. 101(3), (4), (6)), art. 66 | https://www.sluzbenilist.me/propisi/393230/download | 2026-10-30 |
| Tax Administration Law, Ministry consolidation before 104/26: art. 95 | https://wapi.gov.me/download/2dd530ac-eec4-4d0c-9d8f-0c9e7ebc5b86?version=1.0 | 2026-10-30 |
| Tax Administration Law amendment, Official Gazette 104/26: arts. 20, 21, 26 | https://wapi.gov.me/download/c22f3c59-7e52-4213-bbe4-3cd9d8d3a373?version=1.0 | 2026-10-30 |
| Tax Administration decision on the default interest rate, 18 Jul to 31 Dec 2026 | https://wapi.gov.me/download/6d6ec964-3dd6-4588-b81a-a5affc153f6e?version=1.0 | 2026-10-30 |
| Tax Administration notice on the IRMS portal, 30 Dec 2025 | https://www.gov.me/clanak/vazno-obavjestenje-u-vezi-sa-pocetkom-primjene-novog-integrisanog-it-sistema-poreske-uprave-irms | 2026-10-30 |
| Official Gazette 2026 issue lists, issues 1 to 159, scanned for amendments to the PIT, contributions, labour, local-finance and disability laws | https://www.sluzbenilist.me/registri?type=0&year=2026 | 2026-10-30 |

Not yet confirmed: each municipality's current surtax decision and rate (the Bar 13% decision was read only on a municipal investment portal, investin.bar.me, not in the Gazette); whether the surtax follows the employer's seat, the place of work or the employee's residence when they differ, and whether any municipality requires a separate local return; the 2026 PIO maximum annual base (Ministry rulebook not yet published); the 2025 average monthly salary used for the disability contribution and whether it is the gross or net series; the Government's current minimum wage amounts under Labour Law art. 101(3); the Government regulation amounts for tax-free domestic per diem and own-car use; which employers are Chamber of Economy members (Law on the Chamber of Economy, 1/18, not read); statutory overtime, night and holiday premiums under the Labour Law; whether the Government's September 2026 proposal to change the salary bands from 1 January 2027 has been enacted.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
