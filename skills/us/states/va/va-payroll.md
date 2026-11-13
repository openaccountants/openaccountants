---
name: va-payroll
description: Compute and file Virginia employer payroll taxes for 2026. State income tax withholding by the Virginia formula (annual wages less $8,750, $930 per exemption and $800 per age 65 or blind exemption, then 2% to 5.75%), Form VA-4, the 5.75% flat supplemental option, reciprocity for residents of Kentucky, DC, Maryland, West Virginia and Pennsylvania, filing frequency (quarterly under $100 a month, monthly to $1,000, semi-weekly above) with Forms VA-5, VA-15, VA-16 and VA-6 and W-2s by January 31, household employers (VA-6H), penalties; and Virginia unemployment insurance with the VEC (employer test, $8,000 taxable wage base, base rates 0.1% to 6.2%, new employer 2.5% plus add-ons, FC-20/FC-21 quarterly reports due the last day of the following month, $100 late penalty, 1.5% a month interest), new hire reporting within 20 days, misclassification penalties and the workers' compensation employee count. Trigger on "Virginia payroll", "Virginia withholding", "VA-4", "VA-5", "VA-6", "VEC", "Virginia unemployment tax". Federal payroll is in the federal skills. Not for the US Virgin Islands.
version: "2.0"
jurisdiction: US-VA
tax_year: 2026
last_updated: 2026-11-13
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Virginia payroll: income tax withholding and unemployment insurance, 2026

> **Source-cited draft.** Built from the Virginia Income Tax Withholding Guide for Employers (Rev. 10/26), the Virginia Employer Withholding Tables for wages paid after July 1, 2025, Virginia Tax's Withholding Tax page, the VEC frequently asked questions and FC-20/FC-21 instructions, and Va. Code §§ 58.1-322.03, 58.1-1900, 58.1-1901, 60.2-210, 60.2-229, 60.2-512, 63.2-1946 and 65.2-101, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** Virginia withholding for each pay: annualize the pay, subtract $8,750, $930 for each exemption on Form VA-4 and $800 for each age 65 or blind exemption, apply 2% / 3% / 5% / 5.75% (5.75% above $17,000), and divide by the number of pay periods. Employers with average withholding under $100 a month file quarterly, $100 to under $1,000 monthly (VA-5, due the 25th), and $1,000 or more semi-weekly (VA-15 payments, VA-16 quarterly). Everyone files Form VA-6 with W-2s electronically by January 31. Unemployment insurance (VEC) is paid on the first $8,000 of each employee's wages a year; a new employer's base rate is 2.5% plus add-ons; quarterly reports are due on the last day of the month after the quarter.

## Scope and who this is for

Employers paying wages for services in Virginia, or paying Virginia residents, including household employers. Covers state income tax withholding, returns and annual reconciliation, reciprocity, Virginia unemployment insurance (VEC), new hire reporting, misclassification penalties and when workers' compensation coverage is required.

Not covered: federal withholding, FICA and FUTA (federal skills), the employee's own Form 760 (`va-income-tax`), other states' withholding for reciprocal-state residents, local BPOL (`va-corporate-tax-and-bpol`), wage and hour law, and workers' compensation insurance details beyond the employee count. Virginia (US-VA) is not the US Virgin Islands.

## Ask the client first

1. **Where each employee lives and works**, and for residents of Kentucky, DC, Maryland, West Virginia or Pennsylvania, whether they commute daily or meet the 183-day and wages-only conditions.
2. **Each employee's Form VA-4** (exemptions, age 65 or blind, extra withholding, exempt claim).
3. **Pay frequency and pay amounts**, and any bonuses or commissions paid separately.
4. **Average monthly Virginia withholding** (or the filing frequency Virginia Tax assigned).
5. **VEC account and the tax rate on the VEC rate notice**; first year of employing in Virginia; quarterly wages per employee.
6. **Number of employees regularly in service** (workers' compensation) and any workers paid as contractors.

## The method, step by step

1. **Register** for a withholding account with Virginia Tax and an unemployment account with the VEC before the first payroll.
2. **Collect Form VA-4** at hire (Form VA-4P for pension payees). With no VA-4, withhold as if no exemptions were claimed. An employee claiming exempt files a new certificate each year.
3. **Reciprocity check** before withholding for a nonresident:
   - Kentucky and DC residents who commute daily to work in Virginia: no Virginia withholding.
   - Maryland, West Virginia and Pennsylvania residents: no Virginia withholding if domiciled in the other state, living in Virginia less than 183 days (or not at all), with only wage income from Virginia, taxed by their home state.
   - The employee shows the exemption on Form VA-4. Residents of other states (including North Carolina and Tennessee) are withheld on like residents.
4. **Compute withholding** with the formula in the rates table (or the published wage-bracket tables, which are approximate).
5. **Supplemental wages** paid with regular wages: add them and use the formula. Paid separately: either add to the regular wages of the period and withhold the difference, or, if tax was withheld from regular wages, withhold a flat 5.75%.
6. **Deposit and file** by frequency (filing and payment table). All returns and payments are electronic. File even when no tax was withheld.
7. **Year end**: Form VA-6 (or VA-6H) and all W-2s and 1099s showing Virginia tax, electronically, by January 31 (or within 30 days of the final wage payment).
8. **Unemployment insurance**: if the employer test is met, report each quarter's wages on FC-21 and taxable wages on FC-20; taxable wages are each employee's wages up to $8,000 for the year (counting wages reported to other states); tax = taxable wages x the assigned rate.
9. **New hires and new contractors**: report to the Virginia New Hire Reporting Center within 20 days.

### Rates, bands and thresholds

| Item | 2026 figure | Conditions | Source |
| --- | --- | --- | --- |
| Withholding formula | T = (pay x periods) less [$8,750 + $930 x exemptions + $800 x age 65 or blind exemptions]; W = tax on T; withhold W / periods | Effective for wages paid after July 1, 2025, for 2025 and later; $8,750 used for every filing status in the formula | [Employer Withholding Tables (July 2025 and later)](https://www.tax.virginia.gov/sites/default/files/taxforms/withholding/any/employer-withholding-tables-july-2025-and-later-any.pdf) |
| Tax on T | 2% up to $3,000; $60 + 3% of excess over $3,000 to $5,000; $120 + 5% of excess over $5,000 to $17,000; $720 + 5.75% of excess over $17,000 | All filing statuses | [Employer Withholding Tables (July 2025 and later)](https://www.tax.virginia.gov/sites/default/files/taxforms/withholding/any/employer-withholding-tables-july-2025-and-later-any.pdf) |
| Pay periods (P) | Annual 1, semiannual 2, quarterly 4, monthly 12, semi-monthly 24, bi-weekly 26, weekly 52, daily 300 | | [Employer Withholding Tables (July 2025 and later)](https://www.tax.virginia.gov/sites/default/files/taxforms/withholding/any/employer-withholding-tables-july-2025-and-later-any.pdf) |
| Supplemental wages paid separately | Flat 5.75% allowed | Only if tax was withheld from regular wages; no exemptions | [Withholding Guide for Employers (Rev. 10/26)](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/employer-withholding-instructions.pdf) |
| Quarterly filing | Average liability under $100 a month | VA-5 quarterly, due April 30, July 31, October 31, January 31 | [Virginia Tax: Withholding Tax](https://www.tax.virginia.gov/withholding-tax) |
| Monthly filing | $100 to under $1,000 a month | VA-5 due the 25th of the next month | [Virginia Tax: Withholding Tax](https://www.tax.virginia.gov/withholding-tax) |
| Semi-weekly filing | $1,000 or more a month | VA-15 payment within 3 banking days when withholding exceeds $500 on a federal cutoff date; VA-16 quarterly by the end of the month after the quarter; waiver possible for 5 or fewer employees | [Virginia Tax: Withholding Tax](https://www.tax.virginia.gov/withholding-tax) |
| Annual summary | Form VA-6 (VA-6H for household employers) and W-2s / 1099s with Virginia tax, by January 31 | Or within 30 days of the final wage payment; electronic | [Virginia Tax: Withholding Tax](https://www.tax.virginia.gov/withholding-tax) |
| Late filing and late payment penalty | 6% of the tax a month, up to 30% combined; minimum $10 | The minimum applies even with no tax due | [Withholding Guide for Employers (Rev. 10/26)](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/employer-withholding-instructions.pdf) |
| Semi-weekly underpayment penalty | 6% | If 90% of the quarter's liability is not paid within 3 banking days after the period covering the quarter end | [Withholding Guide for Employers (Rev. 10/26)](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/employer-withholding-instructions.pdf) |
| Interest | IRC § 6621 underpayment rate plus 2% | From the due date, even with an extension | [Withholding Guide for Employers (Rev. 10/26)](https://www.tax.virginia.gov/sites/default/files/vatax-pdf/employer-withholding-instructions.pdf) |
| Unemployment employer test | $1,500 of wages in any calendar quarter, or at least one worker on some part of a day in 20 different weeks, in the current or preceding year | | [Va. Code § 60.2-210](https://law.lis.virginia.gov/vacode/title60.2/chapter2/section60.2-210/) |
| Unemployment taxable wage base | $8,000 per employee per calendar year | Wages paid in any state count toward it | [Va. Code § 60.2-229](https://law.lis.virginia.gov/vacode/title60.2/chapter2/section60.2-229/); [VEC FC-20/FC-21 instructions](https://www.vec.virginia.gov/sites/default/files/documents/eFORMFC20_21INST.pdf) |
| Base tax rates | 0.1% to 6.2% | Assigned by calendar year | [VEC: How are tax rates assigned?](https://www.vec.virginia.gov/FAQs/employers/how-are-tax-rates-assigned) |
| New employer base rate | 2.5% plus add-ons | Until eligible for a calculated rate | [VEC: How are tax rates assigned?](https://www.vec.virginia.gov/FAQs/employers/how-are-tax-rates-assigned) |
| Add-ons | Pool cost charge (varies); fund building charge of 0.2% | Fund building applies when the trust fund balance is 50% or less | [VEC frequently asked questions](https://vec.virginia.gov/frequently-asked-questions) |
| VEC quarterly reports (FC-20 / FC-21) | Due the last day of the month after the quarter: April 30, July 31, October 31, January 31 | Required even with no wages | [VEC frequently asked questions](https://vec.virginia.gov/frequently-asked-questions) |
| VEC late report penalty | $100 per report | Not charged for quarters with no wages | [VEC FC-20/FC-21 instructions](https://www.vec.virginia.gov/sites/default/files/documents/eFORMFC20_21INST.pdf) |
| VEC late payment interest | 1.5% a month (18% a year); part month counts as a month | | [VEC FC-20/FC-21 instructions](https://www.vec.virginia.gov/sites/default/files/documents/eFORMFC20_21INST.pdf) |
| New hire and new contractor report | Within 20 days of hire or contract start | Virginia New Hire Reporting Center | [Va. Code § 63.2-1946](https://law.lis.virginia.gov/vacode/title63.2/chapter19/section63.2-1946/) |
| Misclassification civil penalty | Up to $1,000 per worker (first), $2,500 (second), $5,000 (third and later) | Presumption of employee status; IRS guidelines decide | [Va. Code § 58.1-1900](https://law.lis.virginia.gov/vacode/title58.1/chapter19/section58.1-1900/); [§ 58.1-1901](https://law.lis.virginia.gov/vacode/title58.1/chapter19/section58.1-1901/) |
| Workers' compensation | Required once three or more employees are regularly in service in the same business in Virginia | Domestic servants and casual employees are excluded; farm laborers unless more than three full-time | [Va. Code § 65.2-101](https://law.lis.virginia.gov/vacode/title65.2/chapter1/section65.2-101/) |

## Boundary and exception table

| Situation | Rule |
| --- | --- |
| Employee gave no VA-4 | Withhold as if no exemptions |
| Maryland resident working in Virginia, wages only, lives in Maryland | No Virginia withholding (exemption shown on VA-4); Maryland withholding is a Maryland question |
| DC resident who commutes daily to Virginia | No Virginia withholding |
| North Carolina or Tennessee resident working in Virginia | Withhold Virginia tax: no reciprocity |
| Pennsylvania resident who lives in Virginia 200 days | Not exempt: fails the under-183-days condition |
| Average liability exactly $1,000 a month | Semi-weekly |
| Average liability exactly $100 a month | Monthly (quarterly is "less than $100") |
| Separate bonus to an employee with no tax withheld from regular pay | Flat 5.75% not allowed; use the aggregate method |
| Employee paid $11,200 in 2026, $2,800 a quarter | VEC taxable $2,800 in Q1 and Q2, $2,400 in Q3 ($400 excess), $0 in Q4 |
| Business bought mid-year and the employee kept on | The seller's wages to that employee count toward the buyer's $8,000 (Va. Code § 60.2-229) |
| Household employer, domestic service only | May register to file withholding annually (VA-6H by January 31) and VEC reports annually |
| No wages in a quarter | VEC report still due, no late penalty for that quarter |
| Two employees regularly in service | Workers' compensation not required by the Act (may elect) |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| Filing frequency | Use the frequency on the Virginia Tax account; do not assume |
| VEC rate | Use the rate on the VEC notice; for a new employer 2.5% plus add-ons, and say add-ons are not included |
| Reciprocal-state employee's conditions | Withhold Virginia tax until the VA-4 shows the exemption |

## Worked cases

**Case 1, regular withholding.** Single employee paid USD 4,000 semi-monthly, one exemption. Annual USD 96,000 less USD 8,750 less USD 930 = USD 86,320. Tax: USD 720 + 5.75% x USD 69,320 = USD 4,705.90. Per pay: USD 4,705.90 / 24 = USD 196.08.

```oa-check
name: VA 2026 withholding, 4,000 semi-monthly, one exemption
inputs:
  pay: 4000
  periods: 24
  exemptions: 1
steps:
  - t: pay * periods - (8750 + 930 * exemptions)
  - w: 0.02 * min(t, 3000) + 0.03 * clamp(t - 3000, 0, 2000) + 0.05 * clamp(t - 5000, 0, 12000) + 0.0575 * max(t - 17000, 0)
  - per_pay: w / periods
expected:
  t: 86320
  w: 4705.90
  per_pay: 196.08
```

**Case 2, a decision: flat 5.75% or the aggregate method for a separate bonus?** A part-time employee is paid USD 500 semi-monthly (one exemption), from which USD 1.93 is withheld, and receives a separate USD 1,000 bonus. Flat method: 5.75% x USD 1,000 = USD 57.50. Aggregate method: tax on USD 1,500 for the period (USD 52.33) less tax on USD 500 (USD 1.93) = USD 50.40. The aggregate method withholds USD 7.10 less and is closer to the employee's real rate; for an employee already in the 5.75% band both methods give the same answer, so the flat method is simpler there.

```oa-check
name: VA 2026 separate bonus, flat 5.75% against aggregate method
inputs:
  regular: 500
  bonus: 1000
  periods: 24
steps:
  - t_reg: regular * periods - 9680
  - w_reg: (0.02 * min(t_reg, 3000) + 0.03 * clamp(t_reg - 3000, 0, 2000) + 0.05 * clamp(t_reg - 5000, 0, 12000) + 0.0575 * max(t_reg - 17000, 0)) / periods
  - t_all: (regular + bonus) * periods - 9680
  - w_all: (0.02 * min(t_all, 3000) + 0.03 * clamp(t_all - 3000, 0, 2000) + 0.05 * clamp(t_all - 5000, 0, 12000) + 0.0575 * max(t_all - 17000, 0)) / periods
  - aggregate: w_all - w_reg
  - flat: bonus * 0.0575
  - difference: flat - aggregate
expected:
  w_reg: 1.93
  aggregate: 50.40
  flat: 57.50
  difference: 7.10
```

**Case 3, unemployment tax for a new employer.** Three employees earn USD 11,200, USD 30,000 and USD 6,000 in 2026. Taxable wages: USD 8,000 + USD 8,000 + USD 6,000 = USD 22,000. At the 2.5% new employer base rate: USD 550, before the pool cost and any fund building charge shown on the VEC rate notice.

```oa-check
name: VA 2026 VEC tax, new employer base rate, three employees
inputs:
  wages_a: 11200
  wages_b: 30000
  wages_c: 6000
  rate: 0.025
steps:
  - taxable: min(wages_a, 8000) + min(wages_b, 8000) + min(wages_c, 8000)
  - tax: taxable * rate
expected:
  taxable: 22000
  tax: 550.00
```

## When to refuse or refer

- Multistate employees whose unemployment coverage depends on the localization, base of operations or direction and control tests.
- The other state's withholding for reciprocal-state residents (Maryland county taxes, Pennsylvania local taxes, Kentucky local taxes).
- VEC experience rating disputes, successor (SUTA dumping) transfers and voluntary contributions.
- Misclassification audits, worker classification rulings and workers' compensation coverage disputes.
- Semi-weekly waiver requests and electronic filing waivers.
- Wage and hour, final pay and paid leave questions (labor law, not tax).

## Filing and payment

| Item | Due | How | Source |
| --- | --- | --- | --- |
| VA-5 quarterly | April 30, July 31, October 31, January 31 | eForms, Online Services account or Web Upload | [Virginia Tax: Withholding Tax](https://www.tax.virginia.gov/withholding-tax) |
| VA-5 monthly | 25th of the next month | Same | [Virginia Tax: Withholding Tax](https://www.tax.virginia.gov/withholding-tax) |
| VA-15 semi-weekly | Payday Wednesday to Friday: the following Wednesday; Saturday to Tuesday: the following Friday | Electronic payment | [Virginia Tax: Withholding Tax](https://www.tax.virginia.gov/withholding-tax) |
| VA-16 (semi-weekly filers) | Last day of the month after the quarter | Electronic | [Virginia Tax: Withholding Tax](https://www.tax.virginia.gov/withholding-tax) |
| VA-6 / VA-6H with W-2s and 1099s | January 31, 2027 for 2026 | Electronic | [Virginia Tax: Withholding Tax](https://www.tax.virginia.gov/withholding-tax) |
| 1099-K (third-party settlement organizations, Virginia payees of $600 or more) | March 31 (paper with IRS) or April 30 (electronic, or not filed with IRS) | Web Upload | [Virginia Tax: Withholding Tax](https://www.tax.virginia.gov/withholding-tax) |
| VEC FC-20 / FC-21 | April 30, July 31, October 31, January 31 | VEC eForms, Web Upload or Employer Self-Service | [VEC frequently asked questions](https://vec.virginia.gov/frequently-asked-questions) |
| Household employer VEC (domestic service only) | Annually, by January 31 | VEC | [Va. Code § 60.2-512](https://law.lis.virginia.gov/vacode/title60.2/chapter2/section60.2-512/) |
| New hire report | Within 20 days | Virginia New Hire Reporting Center | [Va. Code § 63.2-1946](https://law.lis.virginia.gov/vacode/title63.2/chapter19/section63.2-1946/) |

## Completion checklist

- [ ] Withholding and VEC accounts registered.
- [ ] VA-4 on file for every employee; reciprocal exemptions documented.
- [ ] Withholding computed with $8,750, $930 and $800 and the 2026 rate schedule.
- [ ] Separate bonuses: flat 5.75% only where regular pay had tax withheld.
- [ ] Returns filed at the assigned frequency, including zero returns.
- [ ] VA-6 and W-2s filed electronically by January 31.
- [ ] VEC taxable wages capped at $8,000 per employee; rate from the VEC notice; FC-20/FC-21 filed quarterly.
- [ ] New hires reported within 20 days.
- [ ] Contractors tested against IRS guidelines; workers' compensation in place at three regular employees.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Virginia Employer Withholding Tables, wages paid after July 1, 2025. Read for the formula ($8,750, $930, $800), the rate schedule, the worked example and the pay period table. | https://www.tax.virginia.gov/sites/default/files/taxforms/withholding/any/employer-withholding-tables-july-2025-and-later-any.pdf | 2026-11-13 |
| Virginia Income Tax Withholding Guide for Employers (Rev. 10/26). Read for reciprocity conditions, VA-4, supplemental wages (5.75%), semi-weekly rules, penalties and interest. | https://www.tax.virginia.gov/sites/default/files/vatax-pdf/employer-withholding-instructions.pdf | 2026-11-13 |
| Virginia Tax, Withholding Tax. Read for filing frequencies ($100 / $1,000), due dates, VA-6, W-2 and 1099 filing, 1099-K and household employers. | https://www.tax.virginia.gov/withholding-tax | 2026-11-13 |
| Va. Code § 58.1-322.03. Read for the $8,750 standard deduction for 2025 and 2026 used in the formula. | https://law.lis.virginia.gov/vacode/title58.1/chapter3/section58.1-322.03/ | 2026-11-13 |
| VEC, How are tax rates assigned? Read for base rates 0.1% to 6.2% and the 2.5% new employer rate plus add-ons. | https://www.vec.virginia.gov/FAQs/employers/how-are-tax-rates-assigned | 2026-11-13 |
| VEC frequently asked questions. Read for the pool cost and fund building charges, quarterly report due dates and the $8,000 excess wage method. | https://vec.virginia.gov/frequently-asked-questions | 2026-11-13 |
| VEC FC-20/FC-21 eForm instructions. Read for the $8,000 excess wages, the $100 late penalty and 1.5% monthly interest. | https://www.vec.virginia.gov/sites/default/files/documents/eFORMFC20_21INST.pdf | 2026-11-13 |
| Va. Code § 60.2-210. Read for the employer test. | https://law.lis.virginia.gov/vacode/title60.2/chapter2/section60.2-210/ | 2026-11-13 |
| Va. Code § 60.2-229. Read for the $8,000 wage limit. | https://law.lis.virginia.gov/vacode/title60.2/chapter2/section60.2-229/ | 2026-11-13 |
| Va. Code § 60.2-512. Read for reporting periods and the annual option for household employers. | https://law.lis.virginia.gov/vacode/title60.2/chapter2/section60.2-512/ | 2026-11-13 |
| Va. Code § 63.2-1946. Read for the 20-day new hire and new contractor report. | https://law.lis.virginia.gov/vacode/title63.2/chapter19/section63.2-1946/ | 2026-11-13 |
| Va. Code §§ 58.1-1900 and 58.1-1901. Read for the classification presumption and civil penalties. | https://law.lis.virginia.gov/vacode/title58.1/chapter19/section58.1-1901/ | 2026-11-13 |
| Va. Code § 65.2-101. Read for the employee exclusions, including fewer than three employees regularly in service. | https://law.lis.virginia.gov/vacode/title65.2/chapter1/section65.2-101/ | 2026-11-13 |

Not yet confirmed: the 2026 pool cost charge and whether the fund building charge applies for 2026 (the 2026 VEC rate notice was not read); the VEC page blocks scripts, so the FAQ text was read through a scraper; whether Virginia Tax will issue new tables for 2027 if the standard deduction rises to $9,200 (Va. Code § 58.1-322.03).
