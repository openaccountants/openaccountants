---
name: oh-payroll
description: "Run Ohio employer payroll taxes for 2026, state income tax withholding and state unemployment insurance. Covers the Ohio withholding tables effective 1 October 2025 and the new tables effective 1 August 2026 (1.600%, 2.990% and 3.400% bands, $650 per exemption a year), the 2.75% supplemental rate, Form IT 4, IT 501 and IT 941 filing frequency (quarterly, monthly, partial-weekly), school district withholding, penalties, and Ohio unemployment insurance for 2026 (taxable wage base $9,000, new employer rate 2.85% or 5.85% for construction, experience rates 0.4% to 10.1%, quarterly reports due the last day of the month after the quarter). Trigger on \"Ohio payroll\", \"Ohio withholding\", \"IT 501\", \"IT 941\", \"IT 4\", \"Ohio SUI\", \"ODJFS unemployment rate\", \"Ohio new employer rate\". Points to municipal income tax withholding without computing it."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/oh-payroll"
  jurisdiction: "US-OH"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Ohio payroll: state withholding and unemployment insurance, 2026

> **Source-cited draft.** Built from the Ohio Department of Taxation employer withholding page, the Ohio withholding tables effective 1 October 2025 and 1 August 2026 (percentage method and optional computer formula), the Ohio Department of Job and Family Services (ODJFS) contribution rates page and 2026 Rate Details, the ODJFS quarterly reports page and Ohio Adm. Code 4141-11-01, read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified payroll or tax professional before payroll is run.

**Answer first.** Ohio employers withhold state income tax from wages using the Department's tables: the tables in force from **1 October 2025 to 31 July 2026** use bands of 1.775%, 2.990% and 3.640%; the tables from **1 August 2026** use **1.600%, 2.990% and 3.400%**, with $650 a year off taxable wages per exemption claimed on Form IT 4. Bonuses and other supplemental pay: **2.75%**. Unemployment insurance for 2026 is due on the first **$9,000** of each employee's wages; a new employer pays **2.85%** (construction **5.85%**), and experience rates run from **0.4% to 10.1%** before the 0.15% technology and customer service fee. Quarterly UI reports are due by the last day of the month after the quarter.

## Scope and who this is for

In scope: an employer with employees working in Ohio, for calendar year 2026. Ohio state income tax withholding (IT 4, IT 501, IT 941, W-2 upload), school district withholding at the level of "when it applies", and Ohio unemployment insurance (registration, rates, wage base, quarterly reports).

Out of scope, and where it goes:

| Topic | Where |
| --- | --- |
| Federal withholding, FICA and FUTA | the federal payroll skills (for example `us-form-941-940-payroll`) |
| The employee's own Ohio return | `oh-income-tax` |
| Municipal (city and village) income tax withholding: workplace and resident cities, the 20-day rule, RITA, CCA and direct-file cities | not computed here: a cross-state local income tax skill covers it. Pointer only, see "When to refuse or refer" |
| School district rate lookup and the SD 101 / SD 141 detail | the Department's 2026 school district rate list; see "When to refuse or refer" |
| Workers' compensation (Ohio Bureau of Workers' Compensation) | refer: not a tax, and its premium rules are not covered here |
| Household employees | federal Schedule H skill |

## Ask the client first

1. **Where each employee works and lives** (street address), and whether any work from home or travel to other cities. This drives state, school district and municipal withholding.
2. **Form IT 4** for each employee: exemptions claimed and school district of residence. Without one, withhold as if zero exemptions were claimed.
3. **Residents of Indiana, Kentucky, Michigan, Pennsylvania or West Virginia** working in Ohio: no Ohio withholding is required on their Ohio wages.
4. **Pay frequency** (weekly, biweekly, semi-monthly, monthly, daily) and the pay dates, which pick the table and the partial-weekly period.
5. **Combined Ohio and school district withholding** in the 12 months to 30 June 2025, which sets the 2026 filing frequency.
6. **ODJFS account:** whether the employer is registered, its 2026 contribution rate notice (mailed by 1 December 2025), and whether it is in the construction industry.
7. **Each employee's year-to-date wages** with this employer, for the $9,000 UI base.
8. **Bonuses, commissions or other supplemental pay** paid separately from regular wages.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure | Source |
| --- | --- | --- |
| Withholding exemption allowance | $650 a year per exemption ($12.50 weekly, $25.00 biweekly, $27.08 semi-monthly, $54.17 monthly, $2.50 daily) | [Percentage method, 1 August 2026](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/employer_withholding/2026%20Withholding%20Tables/WHT_PercentageMethod_2026.pdf); [1 October 2025](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/employer_withholding/2025%20Withholding%20Tables/WHT_PercentageMethod_2025.pdf) |
| Annual taxable wage bands | $26,050 or less; more than $26,050 to $100,000; more than $100,000 | [Optional computer formula, 1 August 2026](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/employer_withholding/2026%20Withholding%20Tables/WHT_OptionalComputerFormula_2026.pdf) |
| Band rates, 1 October 2025 to 31 July 2026 | 1.775%, 2.990%, 3.640% | [Percentage method effective 1 October 2025](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/employer_withholding/2025%20Withholding%20Tables/WHT_PercentageMethod_2025.pdf) |
| Band rates, from 1 August 2026 | 1.600%, 2.990%, 3.400% | [Percentage method effective 1 August 2026](https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/employer_withholding/2026%20Withholding%20Tables/WHT_PercentageMethod_2026.pdf) |
| Supplemental compensation (bonuses) | 2.75% | [Employer withholding page](https://tax.ohio.gov/business/employer-withholding) |
| Quarterly filer | combined state and school district withholding $2,000 or less in the look-back year | [Employer withholding page](https://tax.ohio.gov/business/employer-withholding) |
| Monthly filer | more than $2,000 but less than $84,000 | same |
| Partial-weekly filer (EFT) | $84,000 or more | same |
| Next-banking-day rule | combined withholding in a pay period of $100,000 or more | same |
| UI taxable wage base | $9,000 per employee per year | [ODJFS contribution rates](https://jfs.ohio.gov/page/CAJM.hl56rs7cilxWeGzd); [2026 Rate Details](https://dam.assets.ohio.gov/image/upload/jfs.ohio.gov/ouio/uctax/2026RateDetails.pdf) |
| UI new employer rate | 2.85% (2.7% plus 0.15% fee) | same |
| UI new employer rate, construction | 5.85% (5.7% plus 0.15% fee) | same |
| UI experience rates | lowest 0.4%, highest 10.1% (plus 0.15% fee, so 0.55% to 10.25% effective) | same |
| UI mutualized rate | 0% | [ODJFS contribution rates](https://jfs.ohio.gov/page/CAJM.hl56rs7cilxWeGzd) |
| UI delinquency rate | 12.75% | same |
| Interest on late withholding | 7% (calendar year 2026) | [Department interest rate page](https://tax.ohio.gov/individual/resources/interest-rates) |

### Ohio income tax withholding, per pay period

1. **Confirm withholding is required.** Every employer with an office or doing business in Ohio withholds from compensation paid to residents and nonresidents (R.C. 5747.06), except, among others: agricultural labor; domestic service in a private home; residents of Michigan, Indiana, Kentucky, West Virginia or Pennsylvania for services in Ohio; and a nonresident civilian spouse of a servicemember stationed in Ohio.
2. **Register** with the Department within 15 days of the liability beginning, through OH|TAX eServices (FEIN, legal name, email). The same account number covers school district withholding.
3. **Pick the table by pay date:** the 1 October 2025 tables for wages paid through 31 July 2026; the 1 August 2026 tables from then on.
4. **Taxable wage** = gross wage for the period minus the per-period allowance times the exemptions on the IT 4. In the computer formula: TW = (pay per period x pay periods) minus ($650 x exemptions).
5. **Apply the band.** August 2026 biweekly table: up to $1,001.92, 1.600%; $1,001.92 to $3,846.15, $16.03 plus 2.990% of the excess over $1,001.92; above $3,846.15, $101.07 plus 3.400% of the excess. The other periods are in the same table (weekly $500.96 and $1,923.08; semi-monthly $1,085.42 and $4,166.67; monthly $2,170.83 and $8,333.33; daily $100.19 and $384.62). The October 2025 biweekly bases were $17.78 and $102.82.
6. **Supplemental pay** paid separately: 2.75%.
7. **School district:** if the IT 4 names a taxing school district, also withhold its tax. Traditional base districts use the same wage base and exemptions as state withholding; earned income base districts withhold a flat rate with no exemption reduction. Rates are on the Department's 2026 school district list.
8. **Municipal tax:** handled separately (see "When to refuse or refer").

### Filing and paying withholding

- **Frequency** is set each calendar year from combined state and school district withholding in the 12 months ending 30 June of the previous year: quarterly ($2,000 or less, IT 501 and payment due the last day of the month after the quarter), monthly (more than $2,000 but less than $84,000, due within 15 days after the month), or partial-weekly ($84,000 or more, by EFT through the Ohio Treasurer of State within three banking days after each Saturday to Tuesday or Wednesday to Friday period in which payroll was issued). A pay period with $100,000 or more of combined withholding makes the Ohio portion due the next banking day.
- **IT 501** reports and pays each period (not needed for a period with no liability). **SD 101** does the same for school district tax.
- **IT 941** annual reconciliation by **31 January** of the following year (or 15 days after the business stops); total withheld must equal the W-2s and 1099s. **SD 141** for school district tax, same date.
- **W-2 and 1099** information must be uploaded electronically through OH|TAX eServices.
- **Electronic filing and payment** are required (Ohio Adm. Code 5703-7-19).
- **Records:** keep pay, withholding, IT 4s, W-2s, 1099s and IT 3 for at least four years from the due date.
- **Closing or changing entity:** final IT 941 within 15 days of the business stopping; a new FEIN needs a new withholding account.

### Ohio unemployment insurance

1. **Register** with ODJFS once covered and keep the account number; reports go through the ODJFS online system ("The SOURCE").
2. **Rate.** A new employer pays 2.85% (construction 5.85%) until its account has been chargeable with benefits for four consecutive calendar quarters ending 30 June; it then gets an experience rate from the next calendar year. Rate notices for a year are mailed on or before 1 December before it. The 2026 experience rates include a minimum-safe-level increase.
3. **Taxable wages:** each employee's first $9,000 of wages from this employer in 2026.
4. **Contribution** = rate times taxable wages paid in the quarter.
5. **Quarterly contribution and wage report:** electronic, due by the **last day of the month after the quarter** (30 April, 31 July, 31 October, 31 January, moved to the next business day on a weekend or holiday). A report is due even for a quarter with no wages (Ohio Adm. Code 4141-11-01; ODJFS).
6. **Voluntary contributions** to lower a 2026 rate were due by 31 December 2025.

## Boundary and exception table

| Situation | Rule |
| --- | --- |
| Pay date 31 July 2026 | 1 October 2025 tables. Pay date 1 August 2026 or later: 1 August 2026 tables. |
| Employee filed no IT 4 | Withhold as if zero exemptions were claimed. |
| Indiana resident working in Ohio | No Ohio withholding required on the Ohio wages. |
| Bonus paid with regular wages in one payment | Use the tables on the combined amount; the 2.75% rate is for supplemental pay. |
| Look-back withholding exactly $2,000 | Quarterly filer. |
| Look-back withholding exactly $84,000 | Partial-weekly filer by EFT. |
| Employee's year-to-date wages pass $9,000 mid-quarter | UI only on the part up to $9,000. |
| Employee moved from another employer mid-year | The $9,000 base restarts with each employer. |
| Employer has not yet had four chargeable quarters ending 30 June | New employer rate, 2.85% or 5.85%. |
| No wages in a quarter | The UI quarterly report is still due. |

### Defaults when a fact is missing

| Missing fact | Default |
| --- | --- |
| IT 4 | Zero exemptions |
| Prior-year withholding history (new employer) | The frequency set at registration |
| ODJFS rate notice | New employer rate 2.85% (5.85% construction) until the notice arrives |
| Industry for UI | Ask; do not use 2.85% for a builder |

### Red flags to raise with the client

- A payroll provider still on the 1 October 2025 tables for pay dates from 1 August 2026.
- Withheld tax not paid over: a 50% penalty plus double interest.
- Employees working from home in a different city, or travelling to client sites: municipal withholding needs a separate review.
- Payments to workers treated as contractors in construction or delivery: classification affects withholding and UI.
- Missing school district numbers on IT 4s.

## Worked cases

Employer facts are invented; rates and tables are real.

**Case 1: biweekly withholding, before and after 1 August 2026.** An employee paid $2,000 biweekly claims two exemptions. Taxable wage: $2,000 minus 2 x $25.00 = $1,950. Under the 1 August 2026 table: $16.03 plus 2.990% of ($1,950 minus $1,001.92) = $16.03 + $28.35 = $44.38. Under the October 2025 table the same pay gave $17.78 plus the same $28.35 = $46.13. Withholding falls by $1.75 a pay period.

```oa-check
name: Ohio biweekly withholding, August 2026 against October 2025 tables
inputs:
  gross: 2000
  exemptions: 2
steps:
  - taxable: gross - exemptions * 25
  - wh_aug_2026: 16.03 + 0.0299 * (taxable - 1001.92)
  - wh_oct_2025: 17.78 + 0.0299 * (taxable - 1001.92)
  - change: wh_oct_2025 - wh_aug_2026
expected:
  taxable: 1950
  wh_aug_2026: 44.38
  wh_oct_2025: 46.13
  change: 1.75
```

**Case 2: first-year UI cost, builder or not (decision).** A new employer in 2026 pays three employees $30,000, $12,000 and $6,000 in the year. Taxable wages: $9,000 + $9,000 + $6,000 = $24,000. If it is not in the construction industry: 2.85% = $684. If it is: 5.85% = $1,404. Decision: the industry code drives a $720 difference; record the employer's activity at registration correctly, since a builder registered as a non-construction employer is under-paying and will be reassessed.

```oa-check
name: Ohio 2026 new employer UI, construction against other
inputs:
  w1: 30000
  w2: 12000
  w3: 6000
  base: 9000
steps:
  - taxable: min(w1, base) + min(w2, base) + min(w3, base)
  - ui_standard: taxable * 0.0285
  - ui_construction: taxable * 0.0585
  - difference: ui_construction - ui_standard
expected:
  taxable: 24000
  ui_standard: 684
  ui_construction: 1404
  difference: 720
```

## When to refuse or refer

- **Municipal income tax withholding.** Ohio cities and villages levy their own income taxes under R.C. Chapter 718, with workplace and resident-city withholding, a 20-day rule for occasional work in another city, and collection by the Regional Income Tax Agency (RITA), the Central Collection Agency (CCA) or the city itself. This skill does not compute it: use the cross-state local income tax skill, and confirm each city's rate, credit and administrator with the city.
- **School district rates and SD 101 / SD 141 detail:** take the rate from the Department's 2026 school district list for the district number on the IT 4; do not guess.
- **Workers' compensation:** Ohio coverage is through the Ohio Bureau of Workers' Compensation; refer premium questions there.
- **Worker classification disputes**, successor-employer rate transfers, SUTA dumping, reimbursing (non-profit) employers, joint accounts, and assessments or appeals.
- **Gaming and sports betting withholding** (2.75% for proprietors): refer.

## Filing and payment

| Obligation | Form | Due |
| --- | --- | --- |
| Register for withholding | OH\|TAX eServices | within 15 days of the liability beginning |
| Withholding, quarterly filer | IT 501 (and SD 101) | last day of the month after the quarter |
| Withholding, monthly filer | IT 501 (and SD 101) | within 15 days after the month |
| Withholding, partial-weekly filer | EFT through the Ohio Treasurer of State | within three banking days after the partial-weekly period |
| Annual reconciliation | IT 941 (and SD 141), W-2 and 1099 upload | 31 January of the following year |
| UI quarterly contribution and wage report | ODJFS online system | 30 April, 31 July, 31 October 2026 and 1 February 2027 (31 January 2027 is a Sunday) |

**Penalties on withholding** (employer withholding page): failure to file, the greater of $50 a month up to $500 or 5% a month up to 50% of the tax; failure to pay, 10% of the late payment plus double interest; withheld but not remitted, 50% plus double interest; bad check, $50. Interest runs from the due date at 7% for 2026. The officer or employee responsible for filing and paying is personally liable (R.C. 5747.07). Late UI reports bring penalties and interest from ODJFS, which can be waived on application.

## Completion checklist

- [ ] Each employee's work and home locations recorded; reciprocity states identified.
- [ ] IT 4 on file for each employee (or zero exemptions used), with school district number.
- [ ] Correct table by pay date (1 October 2025 tables to 31 July 2026; 1 August 2026 tables after).
- [ ] Supplemental pay at 2.75% where paid separately.
- [ ] Filing frequency checked against the look-back year ending 30 June 2025.
- [ ] IT 501 / SD 101 filed and paid on time; IT 941 / SD 141 and W-2 upload by 31 January of the following year.
- [ ] ODJFS registration, 2026 rate notice, construction status checked.
- [ ] UI computed on the first $9,000 per employee; quarterly reports filed, including nil quarters.
- [ ] Municipal withholding handed to the local tax skill.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Ohio Department of Taxation, employer withholding. Read for who must withhold and exceptions, registration within 15 days, the table editions (1 October 2025 to 31 July 2026; from 1 August 2026), the 2.75% supplemental rate, school district bases, IT 4, IT 501, IT 941, SD 101, SD 141, filing frequency thresholds ($2,000, $84,000, $100,000), penalties and record keeping. | https://tax.ohio.gov/business/employer-withholding | 2026-11-13 |
| Withholding tables, percentage method, effective 1 August 2026. Read for 1.600%, 2.990%, 3.400%, the band limits and base amounts, and the per-period exemption allowances. | https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/employer_withholding/2026%20Withholding%20Tables/WHT_PercentageMethod_2026.pdf | 2026-11-13 |
| Withholding tables, optional computer formula, effective 1 August 2026. Read for TW = (pay per period x PP) minus ($650 x exemptions) and the $26,050 and $100,000 bands. | https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/employer_withholding/2026%20Withholding%20Tables/WHT_OptionalComputerFormula_2026.pdf | 2026-11-13 |
| Withholding tables, percentage method, effective 1 October 2025. Read for 1.775%, 2.990%, 3.640% and the biweekly bases $17.78 and $102.82. | https://dam.assets.ohio.gov/image/upload/tax.ohio.gov/employer_withholding/2025%20Withholding%20Tables/WHT_PercentageMethod_2025.pdf | 2026-11-13 |
| ODJFS, contribution rates 2023 to 2026. Read for the 2026 lowest (0.4%) and highest (10.1%) experience rates, mutualized rate 0%, new employer rate 2.85%, construction 5.85%, delinquency 12.75%, wage base $9,000, the four-quarter experience rule and the minimum-safe-level increase. | https://jfs.ohio.gov/page/CAJM.hl56rs7cilxWeGzd | 2026-11-13 |
| ODJFS, 2026 Rate Details. Read for the 0.15% technology and customer service fee, new employer 2.7% and construction 5.7% before the fee, taxable wage base $9,000 and the 31 December 2025 voluntary contribution date. | https://dam.assets.ohio.gov/image/upload/jfs.ohio.gov/ouio/uctax/2026RateDetails.pdf | 2026-11-13 |
| ODJFS, filing quarterly reports. Read for electronic filing, the due date (last day of the first month after the quarter, next business day on weekends and holidays) and nil reports. | https://jfs.ohio.gov/page/fK0GvyJhY73VW83jHK35t | 2026-11-13 |
| Ohio Adm. Code 4141-11-01, quarterly reports and due date. Read for (A) the due date and electronic filing. | https://codes.ohio.gov/ohio-administrative-code/rule-4141-11-01 | 2026-11-13 |
| Ohio Department of Taxation, interest rates. Read for 7.0% for 2026. | https://tax.ohio.gov/individual/resources/interest-rates | 2026-11-13 |

Not yet confirmed: the UI coverage thresholds (wages in a quarter and weeks of employment under R.C. 4141.01) and the ODJFS registration deadline were not reopened today and are left out. The 1 February 2027 UI date assumes no Ohio holiday that day. Workers' compensation figures are not given.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `oh-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/oh-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
