---
name: mi-payroll
description: "Run Michigan employer payroll for tax year 2026, covering state income tax withholding at 4.25% after the $5,900 personal exemption, Form MI-W4, bonuses withheld at 4.25% with no exemption, reciprocal states, the sales, use and withholding (SUW) returns (monthly or quarterly by the 20th, annual by February 28), W-2 and 1099 filing with Treasury (10-form e-file threshold), state unemployment insurance (2.7% new employer rate, 5.0% construction, 0.06% to 12.2% range, $9,500 taxable wage base cut to $9,000 for employers with all reports and payments up to date), the Earned Sick Time Act (72 hours, or 40 for 10 or fewer employees), city income tax withholding and worker classification. Trigger on \"Michigan payroll\", \"MI withholding\", \"MI-W4\", \"Form 5080\", \"Form 5081\", \"Michigan UIA rate\", \"Michigan unemployment tax\", \"Michigan taxable wage base\", \"Earned Sick Time Act\". Load us-form-941-940-payroll for federal payroll."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/mi-payroll"
  jurisdiction: "US-MI"
  tax_year: "2026"
  last_updated: "2026-11-13"
---

# Michigan payroll, tax year 2026

> **Source-cited draft.** Built from Treasury's 2026 Michigan Income Tax Withholding Guide (Form 446), Treasury's SUW filing frequency and due date pages, the Unemployment Insurance Agency (UIA) pages on unemployment insurance taxes, the taxable wage base and the unemployment tax rate, the UIA January 2026 Employer Advisor, Treasury's list of cities with an income tax, and the Department of Labor and Economic Opportunity (LEO) Earned Sick Time Act FAQ, all read on 2026-11-13. No accountant has reviewed it. All outputs must be reviewed by a qualified tax professional before filing.

**Answer first.** For 2026 a Michigan employer withholds **4.25%** of each employee's pay after deducting **$5,900** per exemption claimed on Form MI-W4, spread over the pay periods. Bonuses paid separately are withheld at 4.25% with no exemption. Withholding is reported with sales and use tax on the SUW return, monthly or quarterly by the **20th** of the following month, plus an annual return by **February 28**. Unemployment tax is paid to the UIA: a new employer pays **2.7%** (construction **5.0%**) on the first **$9,500** of each employee's wages, or **$9,000** if all its reports and payments are up to date. All sources: Form 446 (2026), Treasury SUW pages, UIA pages.

## Scope and who this is for

**In scope.** Every employer that must withhold federal income tax from an employee working in Michigan, including out-of-state employers with Michigan workers and tax-exempt organizations (Form 446). Payers of pensions withholding Michigan tax are covered in outline.

| Covered here | Not covered here |
|---|---|
| Michigan income tax withholding, MI-W4, SUW returns | Federal payroll (Forms 941, 940, W-2 federal, FUTA, FICA): `us-form-941-940-payroll` |
| W-2 and 1099 state copies | Multi-state rules for other states: `us-state-payroll-matrix` |
| UIA registration, rates, taxable wage base | Workers' compensation insurance |
| Earned Sick Time Act basics for payroll | Employment law advice on ESTA disputes |
| Which cities have an income tax, and that employers must withhold it | Detroit rates and returns: `mi-detroit-individual-return`; other cities' own rules |
| Worker classification flags | Individual returns: `mi-income-tax`; pension subtraction detail: `mi-pension-retirement-subtraction` |

Michigan has no school district income tax.

## Ask the client first

1. Where does each employee live (state and city) and where do they work (state and city, days in each)?
2. A signed Form MI-W4 for every employee, and the number of exemptions claimed.
3. The Treasury SUW filing frequency on the account (monthly, quarterly, annual, accelerated).
4. The UIA employer account, the year the business became liable, the 2026 rate notice (Form UIA 1771), and whether it is in construction.
5. Headcount in each workweek this year and last (11 or more for 20 workweeks decides the ESTA tier).
6. Anyone paid on a 1099 who works like an employee.

## The method, step by step

### Rates, bands and thresholds

| Item | 2026 figure | Source |
|---|---|---|
| Withholding rate | 4.25% of compensation after the personal and dependency exemption allowance | [Form 446 (2026)](https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf) |
| Personal exemption, per exemption | $5,900 a year | same |
| Bonuses and other payments made separately from regular pay | 4.25%, no adjustment for exemptions | same |
| Pension withholding with no MI-W4P | 4.25% of all taxable distributions | same |
| Pension and retirement subtraction limit (born after 1945, general rule) | $67,610 single or married filing separately; $135,220 joint | same |
| Reciprocal states (no Michigan withholding on their residents) | Illinois, Indiana, Kentucky, Minnesota, Ohio, Wisconsin | same |
| MI-W4 copies to Treasury | Employee claims 10 or more exemptions, or claims exemption from withholding | same |
| W-2 and 1099 electronic filing | Required at 10 or more forms a year (all W-2s and 1099s issued, not only Michigan ones) | same |
| Records | Keep at least 6 years after the tax is due or paid, whichever is later | same |
| SUW monthly or quarterly return | On or before the 20th of the month after the month or quarter | [Treasury, Filing and Payment Due Dates](https://www.michigan.gov/taxes/business-taxes/payroll-service-providers/filing-and-payment-due-dates) |
| SUW annual return | February 28 | same |
| Accelerated withholding payers | Pay state withholding on the day the federal deposit is due, by EFT | same |
| UIA new employer rate (first two years) | 2.7% | [UIA, Unemployment Insurance Taxes, 2026 summary](https://www.michigan.gov/leo/bureaus-agencies/uia/employers/about-taxes-and-ui/unemployment-insurance-taxes) |
| UIA construction new employer rate | 5.0% | same |
| UIA lowest and highest rate | 0.06% and 12.2% (15.2% with penalty) | same |
| UIA component maximums | CBC 8.2%, ABC 3%, NBC 1% | same |
| UIA taxable wage base | $9,500 default; $9,000 for a qualified employer (all quarterly reports filed, no unpaid balance of $25 or more) | [UIA, Taxable Wage Base](https://www.michigan.gov/leo/bureaus-agencies/uia/employers/forms/accordion/taxable-wage-base); [UIA Employer Advisor, January 2026](https://www.michigan.gov/leo/bureaus-agencies/uia/employers/michigan-employer-advisor/2026/01/21/michigan-employer-advisor-january-2026) |
| ESTA use cap | 72 hours a year; 40 hours for a small business (10 or fewer employees), unless the employer allows more | [LEO, Earned Sick Time Act FAQ](https://www.michigan.gov/leo/bureaus-agencies/ber/wage-and-hour/paid-medical-leave-act/frequently-asked-questions--faqs) |
| ESTA accrual | At least 1 hour per 30 hours worked | same |

### Step 1: register

1. Get an FEIN from the IRS, then register for withholding with Treasury on Michigan Treasury Online (mto.treasury.michigan.gov). The Treasury account number is usually the FEIN. A buyer of a business needs its own FEIN and registration (Form 446).
2. Register with the UIA for an employer account (MiWAM). The UIA was moving to its new MiUI system, scheduled for February 23, 2026 (Employer Advisor, January 2026).
3. Register with each city income tax that applies (step 6).
4. Report new hires (mi-newhire.com, Form 3281).

### Step 2: collect Form MI-W4

1. Every employee completes an MI-W4; the federal W-4 does not replace it (Form 446).
2. An altered MI-W4 is invalid. Tell the employee and withhold on zero exemptions until a valid one arrives (or keep using the prior valid certificate).
3. An employee may not claim more exemptions than on their Michigan return.
4. Send Treasury a copy (Tax Technical Section, P.O. Box 30477, Lansing, MI 48909) if the employee claims 10 or more exemptions or claims to be exempt. Do not send copies for part-time or student workers under their exemption, reciprocal-state residents, short-period exemptions, or ordinary new hires.
5. A resident of a reciprocal state gives a signed statement of their address (Treasury issues no nonresidency certificate); keep it on file.

### Step 3: compute withholding each pay period

1. Start from wages taxable for federal income tax withholding (Michigan follows IRS Pub. 15 for compensation and fringe benefits, Form 446). Pre-tax 401(k) and cafeteria plan amounts follow the federal treatment.
2. Exemption allowance per period = exemptions x $5,900 / pay periods in the year.
3. Withholding = (wages - allowance) x 4.25%, not below zero. Add any extra amount the employee asked for on the MI-W4.
4. A bonus or commission paid separately: 4.25% of the whole payment, no exemption.
5. Michigan residents working temporarily in another state: withhold Michigan tax on that pay too (Form 446).
6. Nonresidents working in Michigan: withhold, unless they live in a reciprocal state.

Per period allowance for one exemption in 2026: weekly $113.46, biweekly $226.92, semimonthly $245.83, monthly $491.67.

### Step 4: file and pay SUW returns

1. Treasury sets the filing frequency from the estimated liability on registration and reviews it yearly; sales, use and withholding share one frequency. File on that frequency, even with nothing due (Treasury Filing Frequency page).
2. Monthly or quarterly return (Form 5080, or through MTO or software) by the 20th of the next month: quarters due April 20, July 20, October 20 and January 20.
3. Accelerated payers pay withholding by EFT on the federal deposit day.
4. Annual return (Form 5081) by February 28 for every filer. It reconciles the year; it does not replace missed monthly or quarterly returns.
5. Amend with Form 5092 (monthly or quarterly) or Form 5082 (annual).
6. Closing the business: Form 163 as soon as possible; W-2s to Treasury within 30 days of ceasing; W-2s to employees within 30 days of the last pay; Form 5081 by February 28 of the next year.

### Step 5: unemployment insurance

1. **Rate.** First two years of liability: 2.7% (construction: the average construction rate, 5.0% for 2026). After that the rate phases in to experience: for accounts set up in 2013 or later, from the third year the rate is the sum of the Chargeable Benefits Component (CBC), Account Building Component (ABC) and Nonchargeable Benefits Component (NBC) (UIA, Unemployment Insurance Taxes). The UIA mails the rate each year on Form UIA 1771; it can be protested within 30 days.
2. **Wage base.** Tax applies to the first $9,500 of each employee's wages in the calendar year, or $9,000 for a qualified employer. For 2026 the UIA issued Form 6354 (notice of the $9,500 base) on February 2, 2026; employers had until February 13, 2026 to file missing reports and pay balances to qualify for $9,000 (Employer Advisor, January 2026).
3. **Contribution** = taxable wages (capped per employee) x the employer's rate. Report wages each quarter, including wages above the base.

### Step 6: city income taxes

Twenty-four Michigan cities levy income taxes, including withholding tax on employers (Treasury, Which cities impose an income tax?): Albion, Battle Creek, Benton Harbor, Big Rapids, Detroit, East Lansing, Flint, Grand Rapids, Grayling, Hamtramck, Highland Park, Hudson, Ionia, Jackson, Lansing, Lapeer, Muskegon, Muskegon Heights, Pontiac, Port Huron, Portland, Saginaw, Springfield and Walker.

- Treasury administers only the City of Detroit's income taxes. The other 23 cities run their own forms, filing, payment and support (same page).
- An employer with employees who live in, or work in, one of these cities registers with that city and withholds its tax (resident rate for residents, nonresident rate for work done in the city). Detroit rates and rules: `mi-detroit-individual-return`. Other cities: use the city's own site from the Treasury list.
- MI-W4 does not cover city tax; each city has its own employee certificate.

### Step 7: Earned Sick Time Act

1. **Who is a small business.** 10 or fewer employees, counting full-time, part-time, temporary and agency workers. Once an employer has 11 or more for 20 or more workweeks in the current or prior calendar year, it is not a small business for the rest of that year and the next (LEO FAQ).
2. **Start.** Small businesses: accrual from October 1, 2025 (or hire, if later). Others: February 21, 2025. A small business that had no employee by February 21, 2022 need not comply until 3 years after it first employs someone.
3. **Accrual.** At least 1 hour per 30 hours worked. Exempt salaried staff are assumed to work 40 hours a week (or their normal shorter week).
4. **Use cap.** 72 hours a year, 40 for a small business, unless the employer allows more.
5. **Carryover** under the accrual method: up to 72 hours (40 for a small business). Frontloading is allowed instead; hours must be available at once.
6. Payroll systems must track hours worked, accrued, used and carried, with dates.

### Step 8: W-2 and 1099 state copies

1. Send Treasury a W-2 for a Michigan resident, for work in Michigan, or where Michigan tax was withheld (Form 446).
2. Send Treasury a 1099 issued to a Michigan resident, wherever the payer is.
3. Due dates follow the federal ones: most by January 31; 1099-MISC, 1099-K, 1099-R and 1099-DA by February 28 on paper or March 31 electronically.
4. W-2s go to the SSA federally, not the IRS, so they are not shared under the Combined Federal/State Filing program: always file W-2 state copies directly with Treasury. 1099-NEC with a Michigan impact must also be filed directly.
5. 10 or more forms in total: upload through MTO in magnetic media format. Fewer: MTO upload in any accepted format, or paper to Michigan Department of Treasury, Lansing, MI 48930. Do not mail W-2s with the annual return.
6. Correcting W-2s: under-withholding, issue a corrected W-2 and copy Treasury; over-withholding, repay the employee in the same year and adjust, or leave the employee to claim it on the MI-1040 (Mich Admin Code R 206.21, R 206.22, as summarized in Form 446).

## Boundary and exception table

| Situation | Treatment | Source |
|---|---|---|
| Ohio resident working at a Michigan site | No Michigan withholding (reciprocity); keep the address statement | Form 446 |
| Michigan resident sent to work in Indiana for a month by a Michigan employer | Keep withholding Michigan tax | Form 446 |
| Employee claims exempt on MI-W4 | Honour if valid, send a copy to Treasury | Form 446 |
| Employee hands in an altered MI-W4 | Invalid; withhold on zero exemptions (or the prior valid certificate) | Form 446 |
| $5,000 bonus in a separate payment | $212.50 withheld, no exemption | Form 446 |
| Employer missed a quarterly report and has a $40 balance in January 2026 | Not qualified: wage base $9,500 unless cured by the UIA deadline | UIA Taxable Wage Base; Employer Advisor January 2026 |
| New construction contractor | 5.0% for 2026, not 2.7% | UIA 2026 summary |
| Employer with 12 staff for 20 summer weeks in 2025, 8 since | Not a small business for the rest of 2025 and all of 2026: 72-hour cap | LEO ESTA FAQ |
| 9 W-2s and 2 1099s issued | 11 forms: electronic filing required | Form 446 |
| Payroll in Pontiac, Hamtramck or Highland Park | City-administered, not Treasury: register with the city | Treasury city list |

### Defaults when a fact is missing

| Missing fact | Default |
|---|---|
| No MI-W4 | Zero exemptions |
| Unknown city of residence | Ask; until known, withhold for any work city on the list |
| Unknown UIA qualification | Use $9,500 |
| Headcount history | Treat as 11 or more (72-hour cap) |
| 1099 worker who works like staff | Treat as an employee and flag |

### Red flags to raise with the client

- Payroll software still set to the $5,800 2025 exemption, or a wage base of $9,000 when the employer did not qualify.
- An out-of-Detroit employer with employees who live in or travel to a listed city and no city registration.
- 1099 workers on fixed hours, the client's equipment and the client's core product: Michigan unemployment law tests economic reality; issuing a 1099 does not make someone a contractor.
- Moving staff into a new entity to get a fresh 2.7% rate: unemployment rate transfer rules apply; refer.

## Worked cases

**Case 1, biweekly withholding and unemployment tax.** A single employee paid USD 104,000 a year biweekly (USD 4,000 a period) claims 1 exemption. The employer is in its first year (2.7%) and qualified for the USD 9,000 base.

Allowance per period: USD 5,900 / 26 = USD 226.92. Withholding per period: (USD 4,000 - USD 226.92) x 4.25% = USD 160.36. Annual tax on the annual figures: (USD 104,000 - USD 5,900) x 4.25% = USD 4,169.25. Unemployment tax for the year: USD 9,000 x 2.7% = USD 243, all paid in the first quarter because the base is reached in the third pay period.

```oa-check
name: Michigan biweekly withholding and UIA (2026)
inputs:
  annual_wages: 104000
  periods: 26
  exemptions: 1
  exemption_amount: 5900
  rate: 0.0425
  wage_base: 9000
  uia_rate: 0.027
steps:
  - gross_per_period: annual_wages / periods
  - allowance: round(exemptions * exemption_amount / periods, 2)
  - withholding_per_period: round((gross_per_period - allowance) * rate, 2)
  - annual_tax: (annual_wages - exemptions * exemption_amount) * rate
  - uia: min(annual_wages, wage_base) * uia_rate
expected:
  gross_per_period: 4000.00
  allowance: 226.92
  withholding_per_period: 160.36
  annual_tax: 4169.25
  uia: 243.00
```

**Case 2, a decision: clear the UIA balance to get the lower wage base?** A new employer (2.7%) with 10 employees, each earning well over USD 9,500, has one quarterly report missing in January 2026. If it files and pays by the UIA deadline it qualifies for the USD 9,000 base; if not, USD 9,500. Unemployment tax: 10 x USD 9,500 x 2.7% = USD 2,565 against 10 x USD 9,000 x 2.7% = USD 2,430. Filing on time saves USD 135, and stops penalty and interest on the missing report. Decision: file and pay before the deadline.

```oa-check
name: Michigan UIA wage base decision (2026)
inputs:
  employees: 10
  default_base: 9500
  qualified_base: 9000
  uia_rate: 0.027
steps:
  - tax_default: employees * default_base * uia_rate
  - tax_qualified: employees * qualified_base * uia_rate
  - saving: tax_default - tax_qualified
expected:
  tax_default: 2565.00
  tax_qualified: 2430.00
  saving: 135.00
```

## When to refuse or refer

| Situation | Action |
|---|---|
| Protesting a UIA rate notice or benefit charges | Refer: protest Form UIA 1771 within 30 days; not a payroll task |
| ESTA claims or lawsuits | Refer to Michigan employment counsel |
| Workers' compensation premiums | Refer to a licensed insurance professional |
| Renaissance Zone or other special wage exemptions | Refer; confirm with Treasury |
| Pension plan administration (MI-W4P elections) | Refer to the plan administrator |
| Moving payroll between related entities to change the UIA rate | Refuse; refer |
| Corporate or unitary tax questions | `mi-corporate-income-tax` |
| Withholding for another state | `us-state-payroll-matrix` |

## Filing and payment

| What | When | How |
|---|---|---|
| SUW monthly return | 20th of the next month | MTO, software or Form 5080 |
| SUW quarterly return | April 20, July 20, October 20, January 20 | same |
| Accelerated withholding | Federal deposit day | EFT |
| SUW annual return (Form 5081) | February 28, 2027 for 2026 | MTO, software or paper |
| W-2s and most 1099s to Treasury | January 31, 2027 | MTO upload (10 or more forms: magnetic media format) |
| UIA quarterly wage and tax report | Each quarter on the UIA system | MiWAM, moving to MiUI |
| City withholding | Each city's own schedule | City systems; Detroit through Treasury |

Weekends and state holidays move SUW due dates to the next business day (Treasury due dates page).

## Completion checklist

- [ ] Treasury, UIA and city registrations in place; new hires reported.
- [ ] A valid MI-W4 for every employee; copies sent for 10 or more exemptions or exempt claims.
- [ ] Payroll software set to 4.25% and $5,900 for 2026; bonuses at 4.25% flat.
- [ ] Reciprocal-state residents documented.
- [ ] SUW returns on Treasury's frequency by the 20th; annual return by February 28.
- [ ] UIA rate from Form UIA 1771; wage base $9,000 only if qualified.
- [ ] City withholding for every listed city where staff live or work.
- [ ] ESTA tier set from the 20-workweek count; accrual and carryover tracked.
- [ ] W-2 and 1099 state copies filed directly with Treasury, electronically at 10 or more forms.
- [ ] 1099 workers reviewed for employee status.

## Sources

| Source | URL | Read on |
|---|---|---|
| 2026 Michigan Income Tax Withholding Guide, Form 446 (Treasury). Read for the 4.25% rate, $5,900 exemption, bonuses, pensions and the $67,610 and $135,220 limits, registration, MI-W4, reciprocity, discontinuance, records, W-2 and 1099 filing and the 10-form threshold. | https://www.michigan.gov/taxes/-/media/Project/Websites/taxes/Forms/SUW/TY2026/446_Withholding-Guide_2026.pdf | 2026-11-13 |
| Filing and Payment Due Dates (Treasury). Read for the monthly, quarterly and annual SUW due dates and accelerated payments. | https://www.michigan.gov/taxes/business-taxes/payroll-service-providers/filing-and-payment-due-dates | 2026-11-13 |
| Filing Frequency (Treasury). Read for how Treasury assigns and reviews the SUW frequency. | https://www.michigan.gov/taxes/business-taxes/payroll-service-providers/filing-frequency | 2026-11-13 |
| Sales and Use Taxes (Treasury). Read for the quarterly due dates April 20, July 20, October 20, January 20. | https://www.michigan.gov/taxes/business-taxes/sales-use-tax | 2026-11-13 |
| Filing Requirements FAQ (Treasury). Read for nil returns, the annual return not replacing missed returns, and amended Forms 5092 and 5082. | https://www.michigan.gov/taxes/business-taxes/sales-use-tax/information/filing-requirements-faq | 2026-11-13 |
| Unemployment Insurance Taxes (UIA). Read for the Tax Rate Summary for 2026 (2.7%, 5.0%, 0.06%, 12.2%, 15.2%, CBC 8.2%, ABC 3%, NBC 1%) and the three components. | https://www.michigan.gov/leo/bureaus-agencies/uia/employers/about-taxes-and-ui/unemployment-insurance-taxes | 2026-11-13 |
| Taxable Wage Base (UIA). Read for the $9,500 default, the $9,000 qualified base and the qualification test. | https://www.michigan.gov/leo/bureaus-agencies/uia/employers/forms/accordion/taxable-wage-base | 2026-11-13 |
| Unemployment Tax Rate (UIA). Read for the new employer phase-in (years 1 to 5), the NBC reductions and the 30-day protest. | https://www.michigan.gov/leo/bureaus-agencies/uia/assets/unemployment-tax-rate | 2026-11-13 |
| Michigan Employer Advisor, January 2026 (UIA). Read for the 2026 taxable wage base notice (Form 6354, February 2), the February 13 deadline for the $9,000 base and the MiUI launch date. | https://www.michigan.gov/leo/bureaus-agencies/uia/employers/michigan-employer-advisor/2026/01/21/michigan-employer-advisor-january-2026 | 2026-11-13 |
| Which cities impose an income tax? (Treasury). Read for the 24 cities and that Treasury administers only Detroit. | https://www.michigan.gov/taxes/questions/iit/accordion/general/what-cities-impose-an-income-tax | 2026-11-13 |
| Earned Sick Time Act FAQ (LEO). Read for small business, start dates, accrual, use caps, carryover and frontloading. | https://www.michigan.gov/leo/bureaus-agencies/ber/wage-and-hour/paid-medical-leave-act/frequently-asked-questions--faqs | 2026-11-13 |

Not yet confirmed: the dollar thresholds Treasury uses to assign SUW filing frequency and the accelerated payer threshold; the SUW late penalty and interest rates (MCL 205.23 and 205.24, not opened); the UIA quarterly report due dates and late report penalty on the new MiUI system; UIA registration thresholds; city income tax rates and exemptions outside Detroit; the ESTA civil fine amounts; the MI-W4 line numbers.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-13. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `mi-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/mi-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
