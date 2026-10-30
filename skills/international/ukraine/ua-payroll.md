---
name: ua-payroll
description: "Ukrainian payroll for employers, tax year 2026: companies and sole proprietors (ФОП) who hire staff under employment or civil-law contracts. Covers the hiring notice before work starts; withholding of 18% personal income tax and the 5% military levy; the tax social benefit for low salaries (UAH 1,664, limit UAH 4,660); the employer's 22% ЄСВ on gross pay, with the UAH 1,902.34 floor, the UAH 172,940 cap and 8.41% for employees with disabilities; gross-to-net; paying with each salary and by the 20th; the combined tax calculation (quarterly for sole proprietors, monthly for companies) and its 2026 deadlines; fines under the Tax Code, the ЄСВ law and the Labour Code; contractors versus employees. Trigger on: Ukraine payroll, зарплата податки, ПДФО з зарплати, військовий збір з зарплати, ЄСВ роботодавця, податковий розрахунок, hiring in Ukraine. Out of scope: own ЄСВ (ua-social-contributions), annual declaration (ua-income-tax)."
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

# Ukraine: payroll for employers (2026)

An employer in Ukraine is a tax agent for its staff. From each salary it withholds 18% personal income tax (PIT) and the 5% military levy and pays them to the budget with the salary (Tax Code of Ukraine, "TCU", art. 167.1, 168.1; section XX, subsection 10, point 16-1). On top of gross pay it pays the unified social contribution (ЄСВ) of 22% (Law No. 2464-VI, "ЄСВ law", art. 8 part 5). Everything is reported in one tax calculation. The 2026 minimum wage is UAH 8,647 a month and the subsistence minimum for able-bodied persons is UAH 3,328 a month (Law No. 4695-IX on the State Budget for 2026, arts. 8 and 7). The Labour Code ("KZpP", Law No. 322-VIII) sets hiring and pay rules and the labour fines.

## Who this applies to

- **Every employer** that pays salary under an employment contract or fees to an individual under a civil-law contract: companies and their branches, sole proprietors who hire, independent professionals who hire, and branches of foreign companies (ЄСВ law art. 4 part 1 point 1; TCU art. 171, 177.7). A sole proprietor becomes the tax agent of anyone it pays taxable income to (TCU art. 177.7).
- **Employees and civil-law workers** are the taxpayers; the employer withholds for them (TCU art. 168.1.1). Their own annual position, the tax discount and other income are in `ua-income-tax`.
- **Payments to a registered sole proprietor** for business services are not payroll: the payer withholds nothing once given proof of registration (TCU art. 177.8). That rule does not apply where the relationship under the contract is in fact employment (art. 177.8). See "Contractor or employee" under The taxable base.
- **Out of this skill.** The proprietor's own ЄСВ (`ua-social-contributions`); Diia City gig contracts and Diia City residents' special ЄСВ (`ua-tax-optimization`); pay of service members, police and similar ranks, which follows separate levy and ЄСВ rules; hiring foreign nationals (work permits).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| PIT on salary and civil-law fees | 18%, withheld | 2026 | https://zakon.rada.gov.ua/laws/show/2755-17 (art. 167.1) |
| Military levy on salary | 5%, withheld | 2026 | same (section XX, subs. 10, point 16-1, sub-point 1.3(1)) |
| Employer ЄСВ | 22% of gross pay, on top | 2026 | https://zakon.rada.gov.ua/laws/show/2464-17 (art. 8 part 5) |
| Employer ЄСВ for employees with disabilities | 8.41% | 2026 | same, art. 8 part 13 |
| Minimum wage | UAH 8,647 a month; UAH 52 an hour | 2026 | https://zakon.rada.gov.ua/laws/show/4695-20 (art. 8) |
| ЄСВ floor at the main place of work | UAH 1,902.34 a month (22% x 8,647) | 2026 | ЄСВ law art. 8 part 5; Budget art. 8 |
| ЄСВ maximum base | 20 minimum wages, UAH 172,940 a month | 2026 | https://zakon.rada.gov.ua/laws/show/4695-20 (art. 32) |
| ЄСВ maximum per person | UAH 38,046.80 a month | 2026 | computed: 22% x 172,940 |
| Tax social benefit (ПСП), basic | UAH 1,664 a month (50% of UAH 3,328) | 2026 | TCU art. 169.1.1; Budget art. 7 |
| ПСП for a parent of two or more children | UAH 1,664 per child | 2026 | TCU art. 169.1.2 |
| ПСП, 150% group | UAH 2,496 | 2026 | TCU art. 169.1.3 |
| ПСП, 200% group | UAH 3,328 | 2026 | TCU art. 169.1.4 |
| ПСП salary limit | UAH 4,660 a month (3,328 x 1.4, rounded to UAH 10); times the number of children for child benefits | 2026 | TCU art. 169.4.1 |
| Non-cash pay gross-up | factor 100 / (100 - 18) | 2026 | TCU art. 164.5 |
| Salary paid at least | twice a month, at most 16 days apart, within 7 days after the period | 2026 | https://zakon.rada.gov.ua/laws/show/322-08 (KZpP art. 115) |

## The taxable base

**PIT and levy base.** Accrued salary, including bonuses and compensation, and fees under civil-law contracts (TCU art. 164.2.1, 164.2.2). The PIT base is salary less the ПСП where it applies (art. 164.6). The levy is charged on the income itself, not reduced by the ПСП (point 16-1, sub-point 1.2(1)). Neither has a floor or a cap. Pay in kind is grossed up at 100 / 82 for PIT (art. 164.5). Fringe benefits such as free housing, goods or services, and compensation of the employee's own costs, are taxable income (art. 164.2.17).

**Tax social benefit (ПСП).** Applied only at the one employer the employee names in a written application (art. 169.2.1, 169.2.2), only to salary, and only in a month when salary does not exceed UAH 4,660 (art. 169.2.3, 169.4.1). Since the 2026 minimum wage is UAH 8,647, it reaches only part-time and other low monthly salaries. The employer recalculates salary and the benefit at year end, with the last month's pay (art. 169.4.2).

**ЄСВ base.** Accrued salary of each insured person, plus civil-law fees, gross of taxes and deductions, counted when accrued whether or not paid (ЄСВ law art. 7 part 1 point 1, parts 4 and 5). Payments on the Cabinet of Ministers' list bear no ЄСВ (art. 7 part 7).
- **Floor.** Where the base does not exceed the minimum wage, the employer pays 22% of the minimum wage, UAH 1,902.34 (art. 8 part 5). The floor does not apply to pay from a job that is not the employee's main place of work, or under a contract with non-fixed working hours: 22% of actual pay (art. 8 part 5).
- **Cap.** No ЄСВ on pay above UAH 172,940 a month (art. 7 part 3; Budget Law art. 32).
- **Disability rate.** 8.41% for employees with disabilities (art. 8 part 13). Keep the disability document on file.

**Gross to net.** For each employee each month:
1. PIT = 18% x (gross - ПСП, if any).
2. Levy = 5% x gross.
3. Net pay = gross - PIT - levy.
4. ЄСВ = 22% x the base, after the floor and the cap (8.41% for disability).
5. Employer cost = gross + ЄСВ.

**Other common cases, 2026.**
- Minimum-wage employee, UAH 8,647: PIT 1,556.46, levy 432.35, net 6,658.19; ЄСВ 1,902.34; cost 10,549.34.
- Employee with a disability on UAH 30,000: PIT 5,400, levy 1,500, net 23,100; ЄСВ at 8.41% is 2,523; cost 32,523, which is UAH 4,077 less than at 22%.
- High earner on UAH 200,000: PIT 36,000 and levy 10,000 on the full amount, net 154,000; ЄСВ only on UAH 172,940, so 38,046.80; cost 238,046.80.

**Civil-law contracts with individuals.** The payer withholds PIT and levy and pays ЄСВ on the fee, like salary (TCU art. 164.2.2, 168.1.1; ЄСВ law art. 7 part 1 point 1). The ПСП does not apply (art. 169.2.3). For work lasting more than a calendar month, the ЄСВ base is spread over the months of the work (ЄСВ law art. 7 part 2).

**Contractor or employee.** A business may engage a registered sole proprietor and withhold nothing (TCU art. 177.8). If the relationship is in fact employment, art. 177.8 stops applying and the payer owes PIT, levy and ЄСВ as an employer (art. 177.8, read with art. 14.1.195 and 14.1.222). Letting someone work without an employment contract, or registering them part-time while they work full-time, with no ЄСВ and taxes paid, is fined at 10 minimum wages per worker (KZpP art. 265). Signs that point to employment: fixed hours and workplace, one client, a fixed monthly sum, the business's tools, no right to substitute, and being managed like staff. Advise an employment contract when these are present.

**Hiring.** A worker may not start before the employment contract, the employer's order and the notice to the tax authority, which administers ЄСВ, about the hire (KZpP art. 24). Hires are also reported in the ЄСВ reporting (ЄСВ law art. 6 part 2 point 8).

**Sole proprietor employers.** Wages and the employer's ЄСВ are deductible for a general-system proprietor (TCU art. 177.4.2, 177.4.3). Single-tax group limits on staff are in `ua-single-tax`.

## Deadlines and filing

| What | Deadline | Source |
|---|---|---|
| Hiring notice to the tax authority | before the employee starts work | KZpP art. 24 |
| Salary payment | at least twice a month, at most 16 days apart; if the pay day is a day off, the day before | KZpP art. 115 |
| PIT and levy on salary paid | with the salary, in one payment document | TCU art. 168.1.2; point 16-1 sub-point 1.4 |
| PIT on pay in kind or cash from the till | within 3 operational days after payment | TCU art. 168.1.4 |
| PIT on salary accrued but not paid | within the monthly period deadline: 20 days to file plus 10 days to pay, so 30 days after the month | TCU art. 168.1.5, 49.18.1, 57.1 |
| ЄСВ on each salary payment | at the same time as the pay | ЄСВ law art. 9 part 8 |
| ЄСВ for the month | by the 20th of the next month (28th for mining companies) | ЄСВ law art. 9 part 8 |
| Tax calculation, employers other than sole proprietors and professionals | monthly, within 20 days after the month | TCU art. 176.2 "б", 49.18.1 |
| Tax calculation, sole proprietors and professionals | quarterly with a monthly breakdown, within 40 days after the quarter | TCU art. 176.2 "б", 49.18.2 |
| Same, Q1 2026 | 11 May 2026 (10 May is a Sunday) | art. 49.18.2, 49.20 |
| Same, Q2 2026 | 10 August 2026 (9 August is a Sunday) | art. 49.18.2, 49.20 |
| Same, Q3 2026 | 9 November 2026 | art. 49.18.2 |
| Same, Q4 2026 | 9 February 2027 | art. 49.18.2 |
| Example monthly deadline: October 2026 calculation | 20 November 2026 | art. 49.18.1 |

**The tax calculation.** One form covers income paid to each individual, PIT and levy withheld, and ЄСВ accrued: "податковий розрахунок сум доходу, нарахованого (сплаченого) на користь платників податків - фізичних осіб, і сум утриманого з них податку, а також сум нарахованого єдиного внеску" (TCU art. 176.2 "б"). It is filed only for periods in which such income was accrued (art. 176.2 "б"). There is no separate levy return; the levy follows the PIT procedure (point 16-1, sub-points 1.4 to 1.6). There is no separate ЄСВ report (ЄСВ law art. 6 part 2 point 4). It is filed through the Electronic Cabinet.

**On request.** The employer gives the employee a statement of income paid, the ПСП applied and tax withheld (art. 176.2 "в").

## Penalties and interest

| Breach | Penalty | Source |
|---|---|---|
| Tax calculation not filed, late, incomplete or with errors | UAH 1,020; UAH 2,040 if fined for the same breach in the past year | TCU art. 119.1 |
| PIT or levy not withheld or not paid | 10% of the tax; 25% if intentional; 50% repeated within 1,095 days; 75% the third time; the agent also owes the tax | TCU art. 125-1 |
| Agreed tax paid late | 5% up to 30 days; 10% after 30 days | TCU art. 124.1 |
| Penalty interest on tax | 120% a year of the National Bank of Ukraine discount rate, per day | TCU art. 129.4 |
| ЄСВ not paid or paid late | 20% of the late amount | ЄСВ law art. 25 part 11 point 2 |
| ЄСВ not paid with the salary | 10% | ЄСВ law art. 25 part 11 point 6 |
| ЄСВ under-accrued, found later | 10% per period, at most 50% | ЄСВ law art. 25 part 11 point 3 |
| Penalty interest on ЄСВ | 0.1% a day | ЄСВ law art. 25 part 10 |
| Worker admitted without a contract, or part-time on paper while working full-time, without ЄСВ and taxes | 10 minimum wages per worker (UAH 86,470 at 2026 rates); 30 (UAH 259,410) if repeated within two years | KZpP art. 265 |
| Wages paid more than a month late, or not in full | 3 minimum wages (UAH 25,941) | KZpP art. 265 |
| Minimum state pay guarantees not met | 2 minimum wages per worker (UAH 17,294) | KZpP art. 265 |
| Other labour law breaches | 1 minimum wage per breach (UAH 8,647); 2 if repeated within a year | KZpP art. 265 |

The labour fines use the minimum wage in force when the breach is found. Paying 50% of a labour fine within 10 banking days settles it (KZpP art. 265). Under martial law, an employer that cannot file or pay on time because of martial law is released from Tax Code liability but must comply within six months after martial law ends (TCU section XX, subsection 10, point 69.1).

## Cross-border points

- **Non-resident employees.** Pay for work in Ukraine is Ukrainian-source income, taxed at the resident rates (TCU art. 170.10.1). The Ukrainian employer withholds as tax agent (art. 170.10.3).
- **Foreign employers.** Branches and representative offices of foreign companies, and diplomatic missions, are ЄСВ payers for staff they employ in Ukraine (ЄСВ law art. 4 part 1 point 1).
- **Paying a foreign company.** Withholding on Ukrainian-source payments to non-resident companies is 15% unless a treaty gives less (TCU art. 141.4.2): see `ua-cross-border`.
- **Residence and treaties** for staff who move in or out of Ukraine: `ua-cross-border`.

## Worked examples

**Example 1. Standard full-time employee.** A company pays an employee UAH 30,000 gross in October 2026. It withholds PIT of UAH 5,400 and levy of UAH 1,500 and pays them with the salary. The employee receives UAH 23,100. The company also pays ЄСВ of UAH 6,600 with the salary, and in any case by 20 November 2026. The employee costs UAH 36,600, of which UAH 13,500 goes to the budget. The October tax calculation is due by 20 November 2026.

```oa-check
name: Gross to net, UAH 30,000 salary, 2026
inputs:
  gross: 30000
  minimum_wage: 8647
  maximum_base: 172940
steps:
  - pit: gross * 0.18
  - levy: gross * 0.05
  - net: gross - pit - levy
  - esv_base: min(max(gross, minimum_wage), maximum_base)
  - esv: esv_base * 0.22
  - employer_cost: gross + esv
  - to_budget: pit + levy + esv
expected:
  pit: 5400
  levy: 1500
  net: 23100
  esv_base: 30000
  esv: 6600
  employer_cost: 36600
  to_budget: 13500
```

**Example 2. Part-time salary below the minimum wage, with the tax social benefit.** A sole proprietor employs a part-time assistant at her main place of work for UAH 4,600 a month. The assistant has applied for the basic ПСП at this employer. UAH 4,600 is not above the UAH 4,660 limit, so the PIT base is 4,600 - 1,664 = UAH 2,936 and PIT is UAH 528.48. The levy is 5% of the full UAH 4,600, UAH 230. Net pay is UAH 3,841.52. ЄСВ cannot be less than the minimum at the main place of work, so the employer pays UAH 1,902.34, not 22% of 4,600. The month costs UAH 6,502.34. As a sole proprietor, she reports the quarter in one calculation, for Q4 2026 by 9 February 2027.

```oa-check
name: Part-time salary with ПСП and ЄСВ floor, 2026
inputs:
  gross: 4600
  subsistence_minimum: 3328
  minimum_wage: 8647
steps:
  - psp_limit: round(subsistence_minimum * 1.4 / 10, 0) * 10
  - psp: subsistence_minimum * 0.5
  - pit_base: gross - psp
  - pit: pit_base * 0.18
  - levy: gross * 0.05
  - net: gross - pit - levy
  - esv: max(gross, minimum_wage) * 0.22
  - employer_cost: gross + esv
expected:
  psp_limit: 4660
  psp: 1664
  pit_base: 2936
  pit: 528.48
  levy: 230
  net: 3841.52
  esv: 1902.34
  employer_cost: 6502.34
```

## Ask the client first

1. Is the employer a company or a sole proprietor (general system or which single-tax group)?
2. For each person: employment contract or civil-law contract, main place of work or second job, fixed or non-fixed hours, monthly gross pay.
3. Does any employee have a disability document, or has anyone applied for the ПСП here?
4. Was the hiring notice filed before each person started?
5. Is anyone working as a registered sole proprietor who works like staff (fixed hours, one client, your tools)?
6. Any non-resident staff, pay in kind, or benefits such as housing or a company car?

## Sources

| Source | URL | Read on |
|---|---|---|
| Tax Code of Ukraine, Law No. 2755-VI, consolidated with amendments to Law No. 4967-IX of 3 Sep 2026: arts. 49.18.1, 49.18.2, 49.20, 57.1, 119.1, 124.1, 125-1, 129.4, 141.4.2, 164, 167.1, 168, 169, 170.10, 171, 176.2, 177.4, 177.7, 177.8; section XX subsection 10 points 16-1 and 69.1 | https://zakon.rada.gov.ua/laws/show/2755-17 | 2026-10-30 (zakon.rada.gov.ua timed out from our network; read via web.archive.org capture of 12 Oct 2026, https://web.archive.org/web/20261012050950/https://zakon.rada.gov.ua/laws/show/2755-17/print) |
| Law No. 2464-VI on the unified social contribution, edition of 1 Jan 2026: arts. 4, 6, 7, 8, 9, 25 | https://zakon.rada.gov.ua/laws/show/2464-17 | 2026-10-30 (via web.archive.org capture of 9 Jan 2026; the 18 Oct 2026 capture shows only the 26 Jan 2026 forced-absence amendment by Law 4697-IX since) |
| Law "On the State Budget of Ukraine for 2026", No. 4695-IX of 3 Dec 2025, arts. 7, 8 and 32 | https://zakon.rada.gov.ua/laws/show/4695-20 | 2026-10-30 (via web.archive.org capture of 4 Jan 2026) |
| Labour Code of Ukraine (Кодекс законів про працю), Law No. 322-VIII, edition of 31 Jul 2026: arts. 24, 115, 265 | https://zakon.rada.gov.ua/laws/show/322-08 | 2026-10-30 (via web.archive.org capture of 1 Oct 2026, https://web.archive.org/web/20261001113537/https://zakon.rada.gov.ua/laws/show/322-08/print) |
| State Tax Service of Ukraine | https://tax.gov.ua | 2026-10-30 (refused automated access with HTTP 403; not read) |

Not yet confirmed: the Cabinet of Ministers procedure and form for the hiring notice; the tax calculation form and its annexes (Ministry of Finance order not read); ЄСВ and the floor for an employee hired or leaving mid-month, on unpaid leave or on sick leave (Ministry of Finance instruction not read); how sick pay and holiday pay are split between employer and social fund; the Law "On remuneration of labour" rule that full-time pay may not be below the minimum wage; the employment test in the draft new Labour Code; ЄСВ for foreign nationals and social security agreements; Diia City gig contracts; the National Bank discount rate for penalty interest; any amendment after the archive captures named above.

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
