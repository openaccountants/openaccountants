---
name: ua-social-contributions
description: "Ukrainian unified social contribution (єдиний соціальний внесок, ЄСВ) for tax year 2026 under the Law on the unified social contribution (No. 2464-VI) and the 2026 State Budget Law. Covers who pays: employers, sole proprietors on the general system and the single tax, independent professionals, voluntary payers; the 22% rate and the 8.41% rate for employees with disabilities; the minimum contribution of UAH 1,902.34 a month, due even with no income; the maximum base of 20 minimum wages (UAH 172,940; 15 for service members); exemptions for pensioners, people with disabilities, employed proprietors and mobilised proprietors; the suspended martial-law right not to pay; quarterly payment and annual reporting; fines and penalty interest. Trigger on: ЄСВ Ukraine, єдиний внесок ФОП, unified social contribution, USC Ukraine, social security Ukraine. Out of scope: employer payroll steps (ua-payroll), PIT (ua-income-tax), single tax (ua-single-tax)."
version: 0.1
jurisdiction: UA
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ukraine: unified social contribution, ЄСВ (2026)

The unified social contribution (єдиний соціальний внесок, ЄСВ) is Ukraine's one compulsory social insurance charge. It funds the state pension and the other types of compulsory state social insurance, in proportions set each year (Law No. 2464-VI, art. 8 part 1, art. 11). It is not a tax and sits outside the tax system (art. 8 part 2), but the State Tax Service collects it and the Tax Code governs its administration (art. 8 part 4). The rate is 22% (art. 8 part 5). Every amount ties to the minimum wage, which is UAH 8,647 a month from 1 January 2026 (Law No. 4695-IX on the State Budget for 2026, art. 8). Article numbers below are articles of Law No. 2464-VI of 8 July 2010 ("ЄСВ law") unless another act is named. "TCU" is the Tax Code of Ukraine.

## Who this applies to

- **Employers** pay ЄСВ on the salary of each employee and on fees paid to individuals under civil-law contracts (art. 4 part 1 point 1, art. 7 part 1 point 1). This includes companies, branches, sole proprietors who hire, and individuals who hire staff. The employer pays it on top of gross pay; nothing is deducted from the employee. The payroll steps are in `ua-payroll`.
- **Sole proprietors (ФОП) for themselves,** including those on the single tax, except e-residents (art. 4 part 1 point 4).
- **Independent professionals** for themselves: scientific, literary, artistic, educational, medical and legal practice, including advocates and notaries, and others listed (art. 4 part 1 point 5).
- **Members of a farming household** who are not insured on another ground (art. 4 part 1 point 5-1).
- **Voluntary payers.** People aged 16 or over who are not employed and not otherwise payers, members of a personal peasant household, and domestic workers may join by a voluntary agreement with the tax authority (art. 10 parts 1 and 3). People living or working abroad may pay under such an agreement in foreign currency (art. 9 part 5).
- **Exempt from paying for themselves** (sole proprietors, independent professionals, farming household members): a person who receives an old-age or long-service pension, a person with a disability, or a person who has reached the pension age in art. 26 of the pension insurance law and receives a pension or social assistance (art. 4 part 4). They may join voluntarily.
- **Employed proprietors.** A proprietor or professional is exempt for each month in which an employer, including a Diia City resident, paid ЄСВ for them of at least the minimum contribution (art. 4 part 6). They may pay on a self-chosen base for months where the employer paid less.
- **Mobilised proprietors.** A proprietor, professional or farming household member called up during mobilisation, or serving under contract in the special period, is released from paying for themselves for the whole service; the tax authority takes the dates from the military register (section VIII, point 9-2). The same applies to reservists called up (point 9-18).
- **No general martial-law exemption in 2026.** Point 9-19 gave proprietors the right not to pay ЄСВ for themselves from 1 March 2022 until twelve months after martial law ends. Its effect is suspended for 2025 (Law No. 4059-IX) and for 2026 (Law No. 4695-IX). Everyone not exempt above pays.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| ЄСВ rate | 22% of the base | 2026 | https://zakon.rada.gov.ua/laws/show/2464-17 (art. 8 part 5) |
| Rate on pay of employees with disabilities | 8.41% | 2026 | same, art. 8 part 13 |
| Minimum wage from 1 January 2026 | UAH 8,647 a month | 2026 | https://zakon.rada.gov.ua/laws/show/4695-20 (art. 8) |
| Minimum contribution (22% x minimum wage) | UAH 1,902.34 a month | 2026 | ЄСВ law art. 1 point 5, art. 8 part 5; Budget art. 8 |
| Minimum for a quarter / a year | UAH 5,707.02 / UAH 22,828.08 | 2026 | computed from the line above |
| Maximum monthly base (except service members and police) | 20 minimum wages, UAH 172,940 | 2026 | https://zakon.rada.gov.ua/laws/show/4695-20 (art. 32) |
| Maximum monthly contribution | UAH 38,046.80 (22% x 172,940) | 2026 | computed from the two lines above |
| Maximum monthly base for pay of service members, police and similar ranks | 15 minimum wages, UAH 129,705 | 2026 | Budget art. 32 |
| Maximum base in the ЄСВ law itself | 15 minimum wages; suspended for 2026 by the Budget Law | 2026 | ЄСВ law art. 1 point 4 |
| Payment by proprietors and professionals for themselves | by the 20th of the month after each quarter | 2026 | ЄСВ law art. 9 part 8 |
| Payment by employers | with each salary payment, and for the month by the 20th of the next month | 2026 | ЄСВ law art. 9 part 8 |
| Fine for late or unpaid ЄСВ | 20% of the amount not paid on time | 2026 | ЄСВ law art. 25 part 11 point 2 |
| Fine for under-accrual found later | 10% for each full or part reporting period, at most 50% | 2026 | art. 25 part 11 point 3 |
| Fine for not paying with the salary | 10% | 2026 | art. 25 part 11 point 6 |
| Penalty interest | 0.1% of the unpaid amount a day | 2026 | art. 25 part 10 |

## The taxable base

**Base by payer type (art. 7 part 1).**
- **Employers:** the accrued salary of each insured person (basic and additional pay, bonuses, compensation, pay in kind, as defined by the Law "On remuneration") plus fees to individuals under civil-law contracts (point 1). The base is gross: taxes and other deductions do not reduce it (art. 7 part 4). It counts when accrued, whether or not paid (art. 7 part 5). A Cabinet of Ministers list sets payments with no ЄСВ (art. 7 part 7).
- **Sole proprietors on the general system, independent professionals, farming household members:** the income (profit) from their activity that is subject to personal income tax. The contribution cannot be less than the minimum contribution for the month in which income was received. In a month or period with no income, they choose the base themselves, up to the maximum, and still pay at least the minimum (point 2).
- **Sole proprietors on the single tax:** a base they choose themselves, up to the maximum, with the contribution not less than the minimum (point 3). Turnover does not matter.

**The minimum contribution.** It is the minimum wage for the month times the rate, and it is payable every month (art. 1 point 5). If the base does not exceed the minimum wage, the contribution is the minimum wage times 22% (art. 8 part 5). For 2026 that is 8,647 x 22% = UAH 1,902.34. Two exceptions for employers: pay from a job that is not the employee's main place of work, and pay under an employment contract with non-fixed working hours, bear 22% of actual pay with no floor (art. 8 part 5).

**The maximum base.** ЄСВ is charged only up to the maximum base (art. 7 part 3). For 2026 it is 20 minimum wages, UAH 172,940 a month; for pay of service members, police and similar ranks it is 15 minimum wages (Budget Law art. 32). The ЄСВ law's own figure of 15 is suspended for 2026 (art. 1 point 4). So the most a proprietor or an employer pays per person is UAH 38,046.80 a month.

**What this means in practice.**
- A single-tax proprietor in groups 1, 2 or 3 pays at least UAH 1,902.34 every month, with income or without. A higher self-chosen base is allowed, up to UAH 172,940; for example a base of UAH 20,000 gives UAH 4,400 a month.
- A general-system proprietor pays 22% of net taxable income (as computed in `ua-income-tax`), never less than the minimum for any month, never more than 22% of the maximum base. A loss month still costs the minimum.
- An employer pays 22% of each employee's gross pay, at least UAH 1,902.34 for an employee at the main place of work earning below the minimum wage, at most UAH 38,046.80. For an employee with a disability, the rate is 8.41% (art. 8 part 13).
- Own ЄСВ paid by a general-system proprietor is a deductible expense for PIT (TCU art. 177.4.3).

**Currency.** ЄСВ is computed only in hryvnia; amounts in foreign currency are converted at the National Bank rate (art. 9 part 1).

**Priority.** ЄСВ is payable whatever the payer's finances, and ranks ahead of all other obligations except paying wages (art. 9 part 12).

**Diia City residents** pay the minimum contribution on employee salaries and on gig-contract fees if they meet the residency conditions (art. 8 part 14-1). Detail: `ua-tax-optimization`.

## Deadlines and filing

| What | Deadline | Source |
|---|---|---|
| Proprietor, professional, farming household: ЄСВ for Q1 2026 | 20 April 2026 | art. 9 part 8 |
| Same, Q2 2026 | 20 July 2026 | art. 9 part 8 |
| Same, Q3 2026 | 20 October 2026 | art. 9 part 8 |
| Same, Q4 2026 | 20 January 2027 | art. 9 part 8 |
| Employer: ЄСВ on each salary payment | at the same time as the pay | art. 9 part 8 |
| Employer: ЄСВ for the month | by the 20th of the next month (28th for mining companies) | art. 9 part 8 |
| Reporting period, employers | the calendar month | art. 9 part 8 |
| Reporting period, proprietors and professionals for themselves | the calendar year; the last period ends on the date of deregistration | art. 9 part 8 |

**How it is reported.** There is no separate ЄСВ report. Payers report ЄСВ inside their personal income tax or single-tax reporting, on the form and by the deadlines set in the Tax Code (art. 6 part 2 point 4). For a general-system proprietor that is the annual PIT declaration, due 1 May (so 3 May 2027 for 2026) (TCU art. 49.18.4, 49.20); for single-tax payers it is the single-tax declaration (`ua-single-tax`); for employers it is the tax calculation of income and ЄСВ, quarterly for proprietors and monthly for others (TCU art. 176.2 "б"; see `ua-payroll`). Employers report hires and changes in insured persons' details in the same reporting (art. 6 part 2 points 8 and 10).

**Paying.** By bank transfer from the payer's account to the tax authority's accounts or the single account, in hryvnia (art. 9 parts 5 and 7). The day of payment is the day the bank debits the payer's account (art. 9 part 10).

**Mobilised employers.** A proprietor who hands payroll to an authorised person while serving pays the ЄСВ accrued by that person within 180 days after demobilisation, and reports it within 150 days, without fines (section VIII, point 9-2).

## Penalties and interest

| Breach | Penalty | Source |
|---|---|---|
| ЄСВ not paid or paid late | fine of 20% of the amount not paid on time | art. 25 part 11 point 2 |
| ЄСВ not accrued on time, found by the tax authority or the payer | 10% of the amount for each full or part reporting period, at most 50% | art. 25 part 11 point 3 |
| Employer does not pay ЄСВ with the salary | 10% of the amount | art. 25 part 11 point 6 |
| Improper keeping of the records ЄСВ is based on | 8 to 15 tax-free minimum incomes of citizens | art. 25 part 11 point 5 |
| Penalty interest on arrears | 0.1% of the unpaid amount for each day late | art. 25 part 10 |

**Martial law.** The 2022 to 2023 reliefs from fines and penalty interest ended on 1 August 2023 (section VIII, points 9-21 and 9-22). A mobilised proprietor's fines and penalty interest for the service period are cancelled (point 9-2).

## Cross-border points

- **Voluntary payment from abroad.** A person living or working abroad who is not otherwise insured may sign a voluntary agreement and pay in foreign currency to the tax authority's account; it is converted to hryvnia (art. 9 part 5, art. 10).
- **e-residents.** Sole proprietors who are e-residents are outside art. 4 part 1 point 4 and do not pay ЄСВ for themselves.
- **Foreign employers.** Branches and representative offices of foreign companies in Ukraine, and diplomatic missions, are employers that pay ЄСВ on staff they employ (art. 4 part 1 point 1).
- **Social security agreements.** Ukraine's bilateral agreements can change which country's contributions apply to a posted worker; their texts were not read for this skill. See `ua-cross-border` for residence and treaty points.

## Worked examples

**Example 1. Single-tax proprietor, a full year at the minimum.** A group 3 single-tax proprietor works all of 2026 and is not exempt. Her income does not matter: she pays the minimum, UAH 1,902.34 a month. Each quarter she pays UAH 5,707.02, by 20 April, 20 July and 20 October 2026 and 20 January 2027. The year costs UAH 22,828.08. If she chose a base of UAH 20,000 instead, she would pay UAH 4,400 a month, still below the maximum of UAH 38,046.80.

```oa-check
name: Single-tax proprietor, minimum ЄСВ, 2026
inputs:
  minimum_wage: 8647
  rate: 0.22
  chosen_base: 20000
  maximum_base_multiple: 20
steps:
  - monthly_minimum: minimum_wage * rate
  - quarterly_minimum: monthly_minimum * 3
  - annual_minimum: monthly_minimum * 12
  - maximum_base: minimum_wage * maximum_base_multiple
  - maximum_monthly: maximum_base * rate
  - chosen_monthly: min(chosen_base, maximum_base) * rate
expected:
  monthly_minimum: 1902.34
  quarterly_minimum: 5707.02
  annual_minimum: 22828.08
  maximum_base: 172940
  maximum_monthly: 38046.80
  chosen_monthly: 4400
```

**Example 2. Employed until June, then a late payment.** A proprietor on the single tax worked as an employee from January to June 2026, and his employer paid ЄСВ for him above the minimum. He is exempt for those six months (art. 4 part 6) and owes nothing for Q1 and Q2. From July he owes the minimum: UAH 5,707.02 for Q3, due 20 October 2026, and the same for Q4, due 20 January 2027, so UAH 11,414.04 for the year. He pays Q3 30 days late. The fine is 20% of the late amount, UAH 1,141.40, and penalty interest is 0.1% a day for 30 days, UAH 171.21 (art. 25 part 10, part 11 point 2).

```oa-check
name: Employed half-year exemption, then late Q3 ЄСВ, 2026
inputs:
  minimum_wage: 8647
  months_owed: 6
  days_late: 30
steps:
  - monthly_minimum: minimum_wage * 0.22
  - quarter_due: monthly_minimum * 3
  - year_due: monthly_minimum * months_owed
  - late_fine: round(quarter_due * 0.20, 2)
  - penalty_interest: round(quarter_due * 0.001 * days_late, 2)
expected:
  monthly_minimum: 1902.34
  quarter_due: 5707.02
  year_due: 11414.04
  late_fine: 1141.40
  penalty_interest: 171.21
```

## Ask the client first

1. Are you a sole proprietor (general system or single tax, which group), an independent professional, an employer, or a voluntary payer?
2. Do you receive an old-age or long-service pension, have a disability, or have you reached pension age with a pension or social assistance?
3. Were you employed in any month of 2026, and did the employer pay ЄСВ for you of at least UAH 1,902.34 for each such month?
4. Were you mobilised or did you serve under contract in 2026? From and to what dates?
5. For a general-system proprietor: your net taxable income by month or for the year.
6. Which quarters have you paid, and on what dates?

## Sources

| Source | URL | Read on |
|---|---|---|
| Law of Ukraine "On the collection and accounting of the unified contribution to compulsory state social insurance", No. 2464-VI of 8 Jul 2010, text in force from 1 Jan 2026 (amended by Laws 4280-IX, 4681-IX, 4695-IX): arts. 1, 4, 6, 7, 8, 9, 10, 25; section VIII points 9-2, 9-18 to 9-22 | https://zakon.rada.gov.ua/laws/show/2464-17 | 2026-10-30 (zakon.rada.gov.ua timed out from our network; read via web.archive.org capture of 9 Jan 2026, https://web.archive.org/web/20260109165053/https://zakon.rada.gov.ua/laws/show/2464-17; the 18 Oct 2026 capture shows the current text is the edition of 26 Jan 2026 under Law 4697-IX, which only adds a rule on court-ordered pay for forced absence) |
| Law No. 4697-IX of 3 Dec 2025, amending the ЄСВ law on forced absence | https://zakon.rada.gov.ua/laws/show/4697-20 | 2026-10-30 (via web.archive.org capture of 8 Aug 2026) |
| Law "On the State Budget of Ukraine for 2026", No. 4695-IX of 3 Dec 2025, arts. 8 and 32, and the suspensions of ЄСВ law art. 1 point 4 and section VIII point 9-19 | https://zakon.rada.gov.ua/laws/show/4695-20 | 2026-10-30 (via web.archive.org capture of 4 Jan 2026) |
| Tax Code of Ukraine, Law No. 2755-VI, arts. 49.18.4, 49.20, 176.2, 177.4.3 | https://zakon.rada.gov.ua/laws/show/2755-17 | 2026-10-30 (via web.archive.org capture of 12 Oct 2026) |
| State Tax Service of Ukraine | https://tax.gov.ua | 2026-10-30 (refused automated access with HTTP 403; not read) |

Not yet confirmed: how a proprietor who registers or deregisters mid-month counts that month; how a general-system proprietor spreads annual net income across months for the minimum and the cap (the Ministry of Finance instruction was not read); whether a payment date on a weekend moves (none of the 2026 quarterly dates falls on one); the proportional floor for employees hired or leaving mid-month; the amount of the tax-free minimum income of citizens for the records fine; how insurance length of service (страховий стаж) is counted (pension insurance law not read); the Cabinet of Ministers list of payments free of ЄСВ; social security agreements with other countries; any amendment after the 18 October 2026 archive capture.

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
