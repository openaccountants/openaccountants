---
name: pg-payroll-social
description: >
  Prepare 2026 PNG fortnightly salary and wages tax and standard superannuation contributions. Apply declarations and resident bands, reconcile gross and net pay, remit withholding and identify coverage, pay-component and remittance-clock issues. Hold unsupported wage, levy, special benefit and exemption claims rather than guessing.
jurisdiction: PG
category: payroll
tax_year: 2026
last_updated: 2026-11-16
version: 1.0
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Papua New Guinea payroll and superannuation v1.0

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Scope

Prepare 2026 PNG salary and wages tax (SWT), employer remittance records and the standard mandatory superannuation-contribution reconciliation. Use statutory fortnightly employment-income bands, not annual income tax divided by pay periods. This skill does not establish payroll software, employment-law compliance or every employee benefit value.

### Quick reference

| Obligation | Rate, threshold or timing with conditions | Official source |
|---|---|---|
| Resident SWT | 0% through 42%, using the fortnightly marginal bands below | [Income Tax Act s. 13 and Sch. 1 Part I clause (3)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Non-resident SWT | 22% through 42%, without the resident first-band exemption | [Sch. 1 Part I clause (4)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| No employment declaration | Highest SWT rate, 42%, applied to the fortnight's employment income, subject to specific special-payment rules | [Sch. 6 clause 2(4)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| SWT return and remittance | By 7th of the following month | [s. 158(1)(a)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Annual withholding statement | Within 3 months after fiscal-year end | [s. 159](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Mandatory employer size | At least 15 employees under the current regulator notice; smaller employers may elect to participate | [BPNG employer and employee contribution notice](https://www.bankpng.gov.pg/publications/public-notices/employer-and-employee-superannuation-contributions) |
| Covered employment duration | Continuous employment for 3 months or more, not an assumed citizenship-only or permanent-staff rule | [BPNG contribution notice](https://www.bankpng.gov.pg/publications/public-notices/employer-and-employee-superannuation-contributions) |
| Employee contribution | 6% of base salary | [BPNG contribution notice](https://www.bankpng.gov.pg/publications/public-notices/employer-and-employee-superannuation-contributions) |
| Employer contribution | 8.4% of base salary | [BPNG contribution notice](https://www.bankpng.gov.pg/publications/public-notices/employer-and-employee-superannuation-contributions) |
| Standard contributions combined | Derived: 14.4% of the same verified base | [BPNG contribution notice](https://www.bankpng.gov.pg/publications/public-notices/employer-and-employee-superannuation-contributions) |

## Ask the client first

Obtain the employer identity and TIN, payroll periods, gross pay components, cash and non-cash benefits, residence and employment declarations, dependants and supporting income facts, secondary employment, leave, redundancy and superannuation payouts, actual withholding, IRC remittances and account balance. For superannuation obtain headcount across branches, continuous employment, fund approval/membership, base-pay components, any exemption, deduction dates and remittance records. Obtain the employment contract and current wage determination for a minimum-pay check.

## The method, step by step

### Establish employment, source and the base

Employment is determined by the Act, not whether the bank description says salary or a contract says consultant. The anti-conversion rule examines control, commercial risk, ability to substitute labour, rectification risk, remuneration structure, client concentration and the person's own assets. A salary deposit is usually net pay and cannot substitute for gross payroll and withholding records. [Income Tax Act ss. 19-20, 132 and 149](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

Reconcile salary, wages, allowances, overtime, bonuses, commissions and taxable benefits to employment income. SWT and superannuation have different bases. Do not omit a commission from taxable employment income merely because a contribution-base question is unresolved. Value non-cash benefits under the applicable statutory schedule and regulations, check exemptions and salary packaging, and refer unresolved valuation or expatriate packages. [ss. 19-21, Sch. 2 and Sch. 3](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

### Apply the fortnightly schedule

| Part of fortnightly employment income, PGK | Resident marginal rate | Non-resident marginal rate | Official source |
|---|---|---|---|
| Up to 770 | 0% | 22% | [Income Tax Act Sch. 1 Part I clauses (3), (4)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Above 770 up to 1,270 | 30% | 30% | [Sch. 1 Part I clauses (3), (4)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Above 1,270 up to 2,693 | 35% | 35% | [Sch. 1 Part I clauses (3), (4)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Above 2,693 up to 9,615 | 40% | 40% | [Sch. 1 Part I clauses (3), (4)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |
| Above 9,615 | 42% | 42% | [Sch. 1 Part I clauses (3), (4)](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf) |


Each rate applies only to the portion of pay in that band. Aggregate separate payments in the same fortnight. For a valid declaration, deduct the allowed annual dependant tax credit divided by 26, the statutory pay-period divisor; do not grant an unsupported credit. Without the declaration, use the maximum-rate rule rather than assuming resident zero-band eligibility. Special redundancy and long-service leave payments have separate conditions and rates and cannot be treated as ordinary salary automatically. [Schedule 6 clauses 2-4](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf). The annual dependant-credit eligibility and computation are in `pg-income-tax`.

For a pay frequency other than the fortnight, do not divide annual tax by the number of pays or invent a conversion. Apply the current authorised IRC payroll-table method or obtain the applicable statutory conversion before finalisation. The source read verifies fortnightly tables, not every software implementation.

### Remit and reconcile

Prepare the prescribed employer withholding return and pay by the statutory date. Keep the gross employment-income record, employee withholding certificate, return acknowledgement and payment reference. Match the annual statement to payroll and monthly remittances. The annual statement is distinct from a salary-only employee's possible annual income-tax-return exemption. [ss. 156-160](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

### Determine superannuation coverage

The current BPNG notice covers employers meeting its headcount and employees meeting continuous-employment conditions. Do not narrow it to permanent employees, count each branch as a separate employer, or treat every non-citizen as exempt. The older Act permits a Central Bank exemption in specified overseas-fund circumstances; obtain the actual current exemption and membership facts before applying it. [BPNG notice](https://www.bankpng.gov.pg/publications/public-notices/employer-and-employee-superannuation-contributions); [Superannuation Act ss. 10, 76-83](https://www.bankpng.gov.pg/sites/default/files/2024-09/Superannution-General-Provision-Act-2000.pdf).

Use the same verified base salary for the ordinary employee and employer percentages. Employee deductions are not an extra employer contribution. Employer contributions are additional employer cost and not a deduction from the employee's gross taxable pay. For the employer's income-tax deduction, approved-fund contributions actually borne by the employer are subject to the statutory limit; do not deduct contributions to a non-approved fund. [Income Tax Act s. 117](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

The pre-amendment Superannuation Act's definition of pay includes salary, wages and commissions and excludes specified overtime, allowances and bonuses. That conflicts with the old skill's blanket commission exclusion. Later amending texts on the regulator's site could not be read through the access challenge. Therefore do not assume a general commission exclusion, a ceiling, or a universal no-ceiling rule. Use uncontested base salary for an illustrative calculation and hold disputed components pending the actual current law and fund record. [Superannuation Act s. 3, older text](https://www.bankpng.gov.pg/sites/default/files/2024-09/Superannution-General-Provision-Act-2000.pdf).

### Remittance-clock conflict

BPNG's current notice directs payment within 14 days of month-end. The older available Act distinguishes employer payment after month-end from employee deductions due within 14 days of deduction. The later amending scans could not be opened sufficiently to resolve that clock. Record both deduction and month-end dates, flag the conflict and obtain the applicable current statutory text before declaring any disputed remittance timely. Do not use the notice to extend an earlier statutory employee-deduction date. [BPNG notice](https://www.bankpng.gov.pg/publications/public-notices/employer-and-employee-superannuation-contributions); [older Act s. 78](https://www.bankpng.gov.pg/sites/default/files/2024-09/Superannution-General-Provision-Act-2000.pdf).

### Payouts, levy and minimum wage

Approved-fund payouts must separate already-taxed contributions from the taxable component. The enacted amendment changes the long-contribution ordinary payout rate, but does not make every early, disability or death payout tax-free. Use `pg-income-tax` and the fund's component certificate rather than treating the whole bank credit as taxable wages. [Income Tax Act s. 119](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf); [2026 budget amendment s. 4](https://pdis.parliament.gov.pg/uploads/e755f62f-9e85-40b1-bb96-d8a162d32050).

The former training-levy paragraph had no confirmed current threshold or rate. Keep training expenditure and any levy notice as separate open items; no levy calculation is authorised here. Likewise the old minimum-wage figures came from non-official summaries. A dated official minimum-wage determination, its phased dates and exemptions must be read before certifying hourly-pay compliance. Neither issue is silently treated as zero.

### Income-tax administration

The Income Tax Act's administration clause incorporates the Tax Administration Act 2017, with the cross-reference corrections in the enacted budget amendment. Keep a penalty separate from interest and from the underlying tax. A penalty requires an IRC assessment and notice; remission may be requested. Do not turn these statutory exposures into an automatic debit in a working paper. [Income Tax Act s. 133 and amendment s. 3](https://pdis.parliament.gov.pg/uploads/e755f62f-9e85-40b1-bb96-d8a162d32050); [TAA ss. 39, 93-101](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d).

| Default | Statutory amount and conditions | Official source |
|---|---|---|
| Late filing | Higher of 20% of tax due, or PGK 200 per month or part month for a company and PGK 100 for another person | [TAA s. 93](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |
| Late payment penalty | 20% of unpaid tax, in addition to interest; tax for this purpose excludes penalty and interest | [TAA s. 94](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |
| Late payment interest | Central Bank rediscount rate at the start of the relevant period plus 5 percentage points; simple interest calculated daily, not a fixed annual penalty rate | [TAA s. 39](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |
| Tax shortfall | 100% for deliberate or reckless statements; otherwise 25%, subject to repeat-default increases, timely-disclosure reductions and statutory defences | [TAA s. 95](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |
| Retention | 7 years after the tax period, extended for unexpired amendment periods, unused losses, audits and proceedings | [TAA s. 11](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |
| Objection and review | Objection within 60 days of service; Tribunal review normally within 28 days of service of the reviewable decision; National Court appeal on law within 28 days of notification, with extension powers | [TAA ss. 24-27, 79](https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d) |

Preserve the notice, service date, grounds, return, undisputed-tax payment and disputed-tax payment arrangements. An objection does not itself suspend collection. Obtain current legislation and the actual IRC decision before advising on a dispute, transition or enforcement case. The current rediscount rate and day-count denominator are not supplied here, so no numerical interest estimate is authorised.


## Worked cases

### Fortnightly SWT with a valid declaration

A resident employee has taxable fortnightly pay of PGK 2,450, a valid declaration, no dependant credit and no special payout. SWT is PGK 563. Superannuation must use the verified base salary separately. [Sch. 1 Part I clause (3), Sch. 6](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

```oa-check
name: PNG resident fortnightly SWT no dependant credit
inputs:
  fortnight_pay: 2450
steps:
  - band_two: max(min(fortnight_pay,1270)-770,0) * 0.30
  - band_three: max(min(fortnight_pay,2693)-1270,0) * 0.35
  - band_four: max(min(fortnight_pay,9615)-2693,0) * 0.40
  - band_five: max(fortnight_pay-9615,0) * 0.42
  - swt: band_two + band_three + band_four + band_five
expected:
  swt: 563
```


### Standard uncontested base salary

An employee is confirmed covered and has base salary of PGK 2,450 for the pay period, with no disputed pay component, exemption or ceiling. Employee contribution is PGK 147, employer contribution PGK 205.80, combined PGK 352.80. If taxable pay also equals that salary and the first case applies, net pay after SWT and the employee contribution is PGK 1,740; employer payroll cost is PGK 2,655.80. [BPNG contribution notice](https://www.bankpng.gov.pg/publications/public-notices/employer-and-employee-superannuation-contributions); [Income Tax Act Schedule 6](https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf).

```oa-check
name: PNG standard super contributions and payroll reconciliation
inputs:
  base_salary: 2450
  swt: 563
steps:
  - employee: round(base_salary * 0.06,2)
  - employer: round(base_salary * 0.084,2)
  - combined: employee + employer
  - net_pay: base_salary - swt - employee
  - employer_cost: base_salary + employer
expected:
  employee: 147
  employer: 205.8
  combined: 352.8
  net_pay: 1740
  employer_cost: 2655.8
```


## When to refuse or refer

Do not finalise payroll with unknown residency, a missing declaration treated as present, unsupported benefit values, unknown gross pay or disputed fund coverage. Refer salary packaging, non-fortnight conversions not documented by IRC, expatriate exemptions, termination payouts, contribution-base disputes and overdue remittances. Hold training-levy and wage-compliance conclusions until the applicable official rule is read.

## Sources

Read on 16 November 2026. A scoped read does not certify every provision in a long Act.

| Official source and scope read | URL | Read on |
|---|---|---|
| Read for Income Tax Act 2025: ss. 13, 19-21, 56, 117-119, 132, 149, 156-160, Sch. 1 and Sch. 6; benefit scope, not every valuation certified | https://www.treasury.gov.pg/wp-content/uploads/2025/10/Certified-Income-Tax-Act-2025.pdf | 2026-11-16 |
| Read for Certified Income Tax 2026 Budget amendment, s. 4 payout-rate change and s. 3 administration | https://pdis.parliament.gov.pg/uploads/e755f62f-9e85-40b1-bb96-d8a162d32050 | 2026-11-16 |
| Read for BPNG current employer and employee contribution notice: coverage, standard rates and stated remittance timing, read through official web text | https://www.bankpng.gov.pg/publications/public-notices/employer-and-employee-superannuation-contributions | 2026-11-16 |
| Read for Superannuation General Provisions Act 2000, older official text: ss. 3, 10, 76-83; later amendments not read | https://www.bankpng.gov.pg/sites/default/files/2024-09/Superannution-General-Provision-Act-2000.pdf | 2026-11-16 |
| Read for Superannuation Regulation 2002: contribution-rate provisions, older official text | https://www.bankpng.gov.pg/sites/default/files/2024-09/SuperannuationRegulation2002.pdf | 2026-11-16 |
| Read for Tax Administration Act 2017: income-tax record, penalty, interest and dispute provisions | https://pdis.parliament.gov.pg/uploads/4b825861-6fb1-41a1-b3a6-01ce3dd7fb5d | 2026-11-16 |

Not yet confirmed: Current amended superannuation pay-component definition and contribution ceiling, resolution of employee-deduction remittance timing, later superannuation amendments blocked by the regulator access challenge, current wage determination, training-levy status, non-fortnight conversion instructions, live return fields, special benefit valuations and current interest input. These are held, not assumed absent.
