---
name: malta-payroll
description: Use for Malta payroll paid in 2026, including FSS withholding, FS4, FS5, FS3, FS7, Class 1 social security, the Maternity Leave Fund, minimum wages, COLA and statutory bonuses. Covers cumulative payroll examples and refers unresolved mid-year starter, personal-status, leave and specialist questions.
version: "2.2"
jurisdiction: MT
tax_year: 2026
last_updated: 2026-11-26
depends_on:
  - payroll-workflow-base
category: payroll
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: payroll
type: computation
---

# Malta payroll 2026: FSS, Class 1, wages and FS forms

## Scope

Use for emoluments paid in calendar 2026 (year of assessment 2027). The article 56 income tax tables apply through FSS; personal tax status and reliefs need the relevant conditions in [malta-income-tax](malta-income-tax.md). See [Act III of 2026, article 13(2)(b)](https://legislation.mt/eli/act/2026/3/eng/pdf).

## Ask the client first

Collect the payer's registration and first accrual date; each payee's FS4, main/part-time/other source, previous payers' FS3s and start date; age and date of birth; basic weekly pay; overtime hours, rate, managerial role and Jobsplus registration; any opt-out or Commissioner direction. Ask about earlier self-employment, rent or investment income for separate tax-return advice. These are information requests, not findings about eligibility.

## The method, step by step

Apply the [FSS Rules, S.L. 372.14](https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3):

1. **Register** within fifteen days from the first emoluments starting to accrue; the duty also applies to a buyer of a going concern with payees (rule 4).
2. **FS4:** the payee completes the website form in triplicate within seven days of a new source or a change to its Parts B, C or D. The payer completes its parts, files the original by the last working day of the month after receipt, keeps its copy and gives the remaining copy to the payee (rule 3).
3. **Missing FS4:** deduct the article 56 maximum, 35%, while the default continues; the payer still completes and files the form to the best of its knowledge. An FS4 unacceptable because of a payee default, not corrected in time to be resubmitted within fourteen days also triggers the maximum rate until the Commissioner directs otherwise (rule 3(2)–(7)).
4. **Main:** ordinarily the one employment source declared as main, excluding qualifying part-time pay. For a payee receiving local pensions, no further emoluments qualify for Main; pension aggregation under rule 7(3): Check this point with one of our partner accountants.
5. **Formula or Tables:** unless the Commissioner directs otherwise, use the cumulative formula. Fewer than ten full-time payees may use the Commissioner's Tables; do not mix the two in the year. Here a full-time payee means an individual whose emoluments are subject to Main deductions, rather than a test of contracted hours (rule 7(4)–(5), Schedule B).
6. **Other Emoluments:** where rules 7 and 8 do not apply, or the Commissioner directs, deduct 20%, subject to the missing-FS4 rule. The payee may direct a higher rate on the prescribed form; pensioners and full-time students (including qualifying apprentices) may direct nil or lower. Other payees need the Commissioner's written approval for a lower rate (rule 9).
7. **Qualifying part-time pay:** rule 8 applies only where article 90A and the Part-time Work Rules qualify the work. Eligibility, rates, caps and any no-deduction direction: Check this point with one of our partner accountants.
8. **Rounding:** discard a euro fraction of 50 cents or less; round a fraction over 50 cents up to one euro (rule 6(3)).
9. **50% limit:** deductions under rules 7, 8 or 9 are limited to 50% of cash emoluments unless the payee consents, article 71 ITA applies or article 46 ITMA has been applied. Rule 11(2) reduces a rule 10 arrears deduction if the aggregate exceeds 50%. Termination payments under rule 34 are outside rule 11.

### Main cumulative formula

Under Schedule B Part I, E is total Main emoluments for the calendar year through the current pay period, C the Current Pay Period Number, N the Number of Pay Periods in the Year, and X tax deducted through the preceding period:

- A = (E / C) x N: projected annual emoluments.
- P: apply the article 56(1)(a) or (b) rates to A for the FS4 status.
- D = (P / N) x C: tax due to date.
- L = D - X: current deduction; if negative, deduct nothing for that period.

The examples below use single income between EUR 16,000 and EUR 60,000 at 25% less EUR 3,400, and married joint income between EUR 23,000 and EUR 60,000 at 25% less EUR 4,550 ([Income Tax Act, article 56](https://legislation.mt/getpdf/69d8a9187da37f0580d5140c)). Other statuses, the qualifying-child conditions and the parent-one-child high-band source conflict: Check this point with one of our partner accountants.

### Mid-year starters and income outside FSS

FSS applies to emoluments as defined in rule 2: employment income/fringe benefits, relevant local pensions and other remuneration for services subject to that definition's exceptions. Its third limb excludes services paid in the course of a trade, business, profession or vocation, services requiring VAT registration and domestic/private services to an individual. Self-employed trading profits, rent and investment income must not simply be added to payroll Main emoluments. Their separate tax treatment and the payee's total annual liability: Check this point with one of our partner accountants.

Collect previous payers' FS3s. Under Schedule B Part II, a Tables year-end adjustment normally occurs in the final pay period and needs complete information, including those FS3s where the payee received Main emoluments from previous payers. It applies annual tax to the year's total Main emoluments, less prior deductions. A negative adjustment means no deduction in that last period; the note does not instruct an automatic payroll refund. Credits/refunds are subject to rules 26–27, including the overtime exception.

**Mid-year starter after self-employment (invented).** Single FS4; starts 1 November on EUR 3,000 a month after self-employment from January to October. Schedule B calls C the Current Pay Period Number but does not expressly explain this starter situation in the text read. Do not choose C = 1 or C = 11, or prescribe a withholding figure, from a conservative guess. Check this point with one of our partner accountants.

**Practice recommendation:** warn the payee in writing that low or nil payroll tax does not settle tax on other income. This recommendation is not a statutory payslip requirement.

## Qualifying overtime

Use [S.L. 123.200, rules 2–3](https://legislation.mt/getpdf/62026ae5c9c73a144cfb58eb) and FSS rule 7A. The employment must be full-time and registered as such with Jobsplus; basic weekly wage must not exceed EUR 375 and the post must not be managerial (director, partner or officer with managerial functions). Overtime means paid hours beyond normally scheduled working hours. Qualifying income is capped at the lower of EUR 10,000 and actual qualifying hours x maxrate; maxrate is the paid overtime hourly rate capped at twice basic weekly wage / 40.

Deduct 15 cents per euro of qualifying overtime, separately from Main. Ordinarily this tax is final and the income excluded from chargeable income, with no credit or refund. A written notice on the approved form can opt out or revoke an opt-out from delivery; rule 7A(6) permits ordinary-rate treatment on the return with a credit, and rule 7A(7) deems that election for article 12A individuals where the Commissioner finds it beneficial. Overtime failing the qualifying conditions stays under the applicable ordinary method.

## Class 1 and the employer's Maternity Leave Fund

Use [Cap. 318, articles 2, 7–9](https://legislation.mt/eli/cap/318/eng/pdf) and the [MTCA 2026 table](https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026). Basic weekly wage (or weekly equivalent of basic monthly salary) excludes overtime, bonuses, extra allowances, remuneration in kind and commissions. Percentage weekly rates are rounded to the nearest cent. Maternity contributions below are payable by the employer.

| Category | Basic weekly wage / condition | Employee EUR | Employer EUR | Employer maternity EUR  Source |
|---|---|---|---|---|---|
| A, under 18 | 0.10–229.44 | 6.62 | 6.62 | 0.20 | https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026 |
| B, 18+ | 0.10–229.44 | 22.94, subject to election below | 22.94 | 0.69 | https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026 |
| C, born by 31 December 1961 | 229.45–490.38 | 10% | 10% | 0.3% | https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026 |
| D, born by 31 December 1961 | 490.39 and over | 49.04 | 49.04 | 1.47 | https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026 |
| C, born from 1 January 1962 | 229.45–559.30 | 10% | 10% | 0.3% | https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026 |
| D, born from 1 January 1962 | 559.31 and over | 55.93 | 55.93 | 1.68 | https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026 |
| E, qualifying students under 18 | Scheme definition below | 10%, max 4.38 | 10%, max 4.38 | 0.3%, max 0.13 | https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026 |
| F, qualifying students 18+ | Scheme definition below | 10%, max 7.94 | 10%, max 7.94 | 0.3%, max 0.24 | https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026 |

E/F means students following full-time studies under the Student-Worker Scheme or similar schemes (including Extended Skills Training, excluding Worker-Student Schemes), with distinct paid work and study periods.

**Category B election:** an eligible part-time employee whose basic weekly earnings do not exceed the National Minimum Wage may elect 10% of actual basic weekly wage instead of the employee Category B amount. It gives pro-rata contributory benefits. The employer still pays EUR 22.94 plus EUR 0.69 maternity. At EUR 100 basic weekly pay, the election therefore gives EUR 10.00 employee, EUR 22.94 employer and EUR 0.69 maternity.

The employer initially pays both Class 1 shares. For ordinary wage deductions it recovers the employee share only from remuneration paid wholly or partly for that contribution week; recovering its own share from the employee is an offence (article 8). Multiple jobs, the election for several part-time jobs without full-time employment, and a change of employer mid-week: Check this point with one of our partner accountants.

## Minimum wage, cost of living and bonuses

From 1 January 2026, weekly national minimum wages are EUR 229.44 at 18+, EUR 222.66 at 17 and EUR 219.82 below 17. Part-time minimum pay uses the comparable whole-time hourly rate under the relevant Wage Regulation Order; without an applicable Order the floor is the national weekly minimum / 40 (EUR 5.736 for an adult). See [L.N. 289 of 2025](https://legislation.mt/getpdf/696e2f8c52ff32215ce13d7b). Sector wage carry-forward rules: Check this point with one of our partner accountants.

The whole-time weekly wage increase is EUR 4.66 from 1 January 2026. Part-time hourly increases follow the comparable whole-time employee, or applicable Order; without either, use 1/40 of the weekly increase ([L.N. 290 of 2025](https://legislation.mt/getpdf/696e3268cc8c701d50c97020)). This is a wage increase, included in basic wages, rather than a separate bonus.

For whole-time employees, statutory bonuses are paid between 15–30 June and 15–23 December; each is at least half the Government's announced annual bonus. Under a year's service, the bonus is proportionate to annual hours worked; reduced-hours whole-time employees receive a proportional entitlement ([Cap. 452, articles 23–24](https://legislation.mt/getpdf/69faf83e2eb86e24207539ec)). [DIER's amounts](https://dier.gov.mt/en/services/employment-conditions/wages/bonus-and-weekly-allowances/) are EUR 135.10 at end-June and 15–23 December; its partial bonus rate is EUR 0.74 per calendar day, including weekends. Income supplements are separate: EUR 121.16 at end-March and end-September; partial weekly allowance EUR 4.66 per working week or proportion.

Bonuses and supplements are excluded from the Class 1 basic-pay base. Any specific FSS exemption, part-time bonus entitlement, service increments, sector pay and overtime premiums: Check this point with one of our partner accountants.

Annual leave and public holidays, average working time and opt-outs, maternity leave/pay and benefit rates: Check this point with one of our partner accountants.

## Filing, payment and records

Apply the FSS Rules cited above:

- **FS5 and payment:** by the last working day of the following month remit tax deducted or required to be deducted, with the monthly advice, including nil advice. Show payee counts, gross pay split into qualifying part-time, qualifying overtime and other pay, fringe benefits separately, tax by category and directed arrears (rules 15, 20).
- **FS3:** two copies to the payee by 31 January of the following year; where the contract ends before 31 December, within seven days of termination, subject to rule 28. Report qualifying overtime income and hours separately (rule 21).
- **FS7 with original FS3s:** to the Commissioner by 15 February of the following year. If the payer ceases, by the last working day of the month after its last emoluments payment, subject to rule 28 (rule 22).
- **Class 1:** unless the Director approves other arrangements, monthly in arrears, within the time and form/manner the Director determines (Cap. 318, article 9).
- **Pay statement each payment:** gross for each category, fringe benefits distinguished, tax deducted and any Commissioner-directed arrears (rule 19).
- **Records:** maintain payee identity/address and ID or tax number, payment dates, gross/fringe pay and deductions including arrears, with monthly and cumulative totals as applicable; retain under ITMA article 23(12) (rule 18).

Schedule C FSS additional tax, subject to EUR 1,000 maximum per default:

| Default | Amount | Source |
|---|---|---|
| FS4 not submitted as required | EUR 2 per form, or EUR 23 where defaults in one month do not exceed ten | https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3 |
| Failure to register/re-register | EUR 115 | https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3 |
| Monthly advice (including nil) late or wrong manner | EUR 15 | https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3 |
| FS7 with original FS3s not submitted | EUR 200 | https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3 |

Under rule 3(6), a payer acting **without reasonable excuse** who submits incorrect/incomplete FS4 information or fails to submit is also liable for consequent under-deductions unless otherwise recovered by the Commissioner by 31 December of that year.

Default notices, contestation, continuing-default increases, late FSS/Class 1 interest, and over-deduction recovery: Check this point with one of our partner accountants.

## Worked cases

All employees are invented; assume the relevant conditions above and full contribution weeks for Class 1.

**Case 1 - cumulative single, two months.** Starts in January, basic salary EUR 2,500 monthly, single FS4, twelve periods. A = EUR 30,000; P = 30,000 x 25% - 3,400 = EUR 4,100. January D = EUR 341.666… and deduction EUR 342. February D = EUR 683.333…; subtract the actual EUR 342 already deducted: L = EUR 341.333…, deduction EUR 341. With an eligible married joint FS4, P = EUR 2,950 and January deduction EUR 246: annual difference EUR 1,150.

```oa-check
name: Single FSS cumulative formula, EUR 2,500 a month, two months with euro rounding (2026)
inputs:
  salary: 2500
steps:
  - annual_tax: salary * 12 * 0.25 - 3400
  - month_one: ceil(annual_tax / 12)
  - month_two: floor(annual_tax / 12 * 2 - month_one)
  - married_annual: salary * 12 * 0.25 - 4550
  - status_saving: annual_tax - married_annual
expected:
  annual_tax: 4100
  month_one: 342
  month_two: 341
  married_annual: 2950
  status_saving: 1150
```

**Case 2 - Class 1 cap.** Weekly basic EUR 700, born 1985: Category D, EUR 55.93 employee and EUR 55.93 employer; maternity EUR 1.68 (uncapped 0.3% would be EUR 2.10). Employer cost above wages EUR 57.61. At EUR 400 basic, Category C gives EUR 40.00 employee, EUR 40.00 employer and EUR 1.20 maternity.

```oa-check
name: Class 1 2026, born from 1962, weekly basic EUR 700 above the cap
inputs:
  weekly_basic: 700
steps:
  - employee: min(weekly_basic * 0.10, 55.93)
  - employer: min(weekly_basic * 0.10, 55.93)
  - maternity: min(weekly_basic * 0.003, 1.68)
  - employer_extra: employer + maternity
expected:
  employee: 55.93
  employer: 55.93
  maternity: 1.68
  employer_extra: 57.61
```

- **No FS4:** EUR 2,500 monthly x 35% = EUR 875. Half the cash pay is EUR 1,250; that arithmetic does not extend rule 11's scope to missing-FS4 deductions.
- **Qualifying overtime:** basic EUR 360 weekly, non-managerial, Jobsplus-registered full-time; 40 qualifying hours at EUR 13.50 = EUR 540, assuming a valid FS4, no earlier qualifying overtime that year and no opt-out. Basic hourly EUR 9; twice that EUR 18. The income is within the limits; 15% deduction EUR 81, separately reported on FS5/FS3 and excluded from Main. Return elections remain as described above.
- **Second job:** EUR 1,000 monthly classified as Other Emoluments, with FS4: 20% = EUR 200, subject to the permitted higher/lower directions above.

## When to refuse or refer

Personal returns and reliefs, Class 2 self-employment, disputed family/child status, expatriate regimes, cross-border/posted workers and A1 certificates, directors' fees, net-pay/gross-up arrangements, agreements about deductions, payments after death or contract end: Check this point with one of our partner accountants.

The actual 2026 Main Tax Deduction Tables, January–February transition instructions, monthly-to-weekly Class 1 conversion, FS5 layout/Class 1 presentation, employment-law itemised payslips and electronic FS3 filing threshold: Check this point with one of our partner accountants.

## Sources

The unchanged operative reads from 22 November 2026 are reused; recovered exact passages from those saved official texts were read on 26 November. This is not accountant approval.

| Source | URL | Read date |
|---|---|---|
| FSS rules and Schedule B/C | https://legislation.mt/getpdf/6a6c4d3b52fe3f25d8b039d3 | 2026-11-22; relevant passages 2026-11-26 |
| Income Tax Act article 56 | https://legislation.mt/getpdf/69d8a9187da37f0580d5140c | 2026-11-22; example bands 2026-11-26 |
| Act III of 2026, article 13 | https://legislation.mt/eli/act/2026/3/eng/pdf | 2026-11-22 |
| Social Security Act | https://legislation.mt/eli/cap/318/eng/pdf | 2026-11-22; articles 2, 7–9 passages 2026-11-26 |
| MTCA Class 1 2026 table and notes | https://mtca.gov.mt/personal-tax/fss/social-security-contribution-rates/class-1---social-security-contribution-rates/2026 | 2026-11-22 |
| Minimum wage and wage increase orders | https://legislation.mt/getpdf/696e2f8c52ff32215ce13d7b ; https://legislation.mt/getpdf/696e3268cc8c701d50c97020 | 2026-11-22; relevant passages 2026-11-26 |
| Bonus/supplement law and DIER amounts | https://legislation.mt/getpdf/69faf83e2eb86e24207539ec ; https://dier.gov.mt/en/services/employment-conditions/wages/bonus-and-weekly-allowances/ | 2026-11-22 |
| Qualifying overtime | https://legislation.mt/getpdf/62026ae5c9c73a144cfb58eb | 2026-11-22; relevant passages 2026-11-26 |

Not yet confirmed: the specialist and form questions above are referred with the partner-accountant line; they are not usable payroll instructions.
