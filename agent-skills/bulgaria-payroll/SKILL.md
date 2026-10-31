---
name: bulgaria-payroll
description: "Bulgarian payroll for employees for tax year 2026, in euro. Covers the monthly gross-to-net: employee and employer social contributions on the insurable income (floor and ceiling), health insurance, the 10% wage tax withheld on gross pay less the employee's own contributions, the annual recalculation by 31 January, and filing of Declarations 1 and 6 and payment by the 25th of the next month. Uses the 2026 minimum wage (EUR 620.20) and the two ceilings for 2026 (EUR 2,111.64 to 31 July, EUR 2,300 from 1 August). Lev amounts are shown in euro at BGN 1.95583. Trigger phrases: Bulgaria payroll, gross to net Bulgaria, заплата, данък по чл. 42 ЗДДФЛ, Декларация образец 1, Декларация образец 6, осигуровки работодател. Out of scope: self-employed contributions and fund-by-fund detail (bulgaria-social-contributions), the annual income tax return (bulgaria-income-tax), posted workers and treaties (bg-cross-border)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/bulgaria-payroll"
  jurisdiction: "BG"
  tax_year: "2026"
  last_updated: "2026-10-24"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Bulgaria payroll (2026)

> **Source-cited draft.** Drafted from the Social Insurance Code (KSO), the Health Insurance Act (ZZO), the Personal Income Taxes Act (ZDDFL), the State Social Insurance Budget Act for 2026, the National Health Insurance Fund Budget Act for 2026, Council of Ministers Decree 243/2025 on the minimum wage, Ordinance N-13 on Declarations 1 and 6 and the Euro Introduction Act, read on lex.bg, dv.parliament.bg and nssi.bg on 2026-10-24. No accountant has reviewed it. Do not run a payroll from it without review by a qualified Bulgarian professional.

Tax year: the calendar year. Authorities: the National Revenue Agency (NRA, НАП) collects contributions and tax; the National Social Security Institute (NSSI, НОИ) runs the funds. Currency: the euro from 1 January 2026. Amounts still printed in leva in a law are read as euro at BGN 1.95583, rounded to the cent (Euro Introduction Act arts. 11(2), 12, 13). The 2026 budget acts were adopted late (ДВ бр. 68 of 28 July 2026), so two sets of insurable income limits apply in 2026: one to 31 July and one from 1 August. For the self-employed and the fund-by-fund rules, see `bulgaria-social-contributions`. For the annual return and reliefs, see `bulgaria-income-tax`.

## Who this applies to

- **Employers** (осигурители) of anyone working under an employment contract in Bulgaria: companies, sole traders, branches of foreign companies and individuals who employ staff (KSO arts. 4(1)(1), 5(1)).
- **Employees** under an employment contract, whatever their nationality, for work done in Bulgaria (KSO art. 4(1)(1); ZDDFL arts. 8(2), 24).
- **Managers and similar office holders** paid under a management contract are insured like employees (KSO art. 4(1)(7)); the same rates and limits apply.
- **Civil servants, judges and prosecutors** (KSO art. 4(1)(2), (3), (10)) have a separate split from 1 August 2026 (KSO art. 6(5a)). This skill does not cover them.
- **Out of scope here:** the self-employed and freelancers (they insure themselves), civil-contract workers paid without an employment contract, seafarers (1% tax and own-account contributions) and workers posted abroad. See `bulgaria-social-contributions` and `bg-cross-border`.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Minimum monthly wage | EUR 620.20 (BGN 1,213); hourly EUR 3.74 | 2026 | Decree 243/2025, ДВ 98/2025, [dv.parliament.bg](https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=238961) |
| Maximum monthly insurable income, 1 Jan to 31 Jul | EUR 2,111.64 (BGN 4,130) | 2026 | State Social Insurance Budget Act 2026 (ZBDOO) art. 9(1)(c), [dv.parliament.bg](https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=244982) |
| Maximum monthly insurable income, 1 Aug to 31 Dec | EUR 2,300 | 2026 | ZBDOO 2026 art. 9(2)(c) |
| Minimum insurable income by activity and job group, 1 Jan to 31 Jul | EUR 550.66 to EUR 901.41 (Appendix 1) | 2026 | ZBDOO 2026 art. 9(1)(a), Appendix 1 |
| Minimum insurable income by activity and job group, 1 Aug to 31 Dec | EUR 620.20 to EUR 1,532.00 (Appendix 1A) | 2026 | ZBDOO 2026 art. 9(2)(a), Appendix 1A |
| Pension fund, born after 31 Dec 1959 | 14.8%: employer 8.22%, employee 6.58% | 2026 | KSO art. 6(1)(2)(a), (1)(4), (3)(9), [lex.bg](https://lex.bg/laws/ldoc/1597824512) |
| Pension fund, born before 1 Jan 1960 | 19.8%: employer 11.02%, employee 8.78% | 2026 | KSO art. 6(1)(1)(a), (1)(4), (3)(8) |
| Universal pension fund (second pillar), born after 31 Dec 1959 | 5%: employer 2.8%, employee 2.2% | 2026 | KSO art. 157(1)(1)(c), (3) |
| General illness and maternity | 3.5%: employer 2.1%, employee 1.4% (60:40) | 2026 | KSO art. 6(1)(5), (3)(7) |
| Unemployment | 1%: employer 0.6%, employee 0.4% (60:40) | 2026 | KSO art. 6(1)(6), (3)(7) |
| Work accident and occupational disease | 0.4% to 1.1% by economic activity, employer only (e.g. IT and accounting 0.4%, retail 0.5%, building construction 1.1%) | 2026 | KSO art. 6(1)(7), (6); ZBDOO 2026 art. 14, Appendices 2 and 2A |
| Guaranteed receivables fund | Not paid for 2026 | 2026 | ZBDOO 2026 art. 15(1) |
| Health insurance | 8%: employer 4.8%, employee 3.2% (60:40) | 2026 | NHIF Budget Act 2026 art. 2, [dv.parliament.bg](https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=244981); ZZO art. 40(1)(1), [lex.bg](https://lex.bg/laws/ldoc/2134412800) |
| Total, standard employee | Employee 13.78%; employer 18.52% plus the work accident rate | 2026 | Sum of the rows above |
| Wage tax | 10% of gross pay less the employee's own mandatory contributions | 2026 | ZDDFL arts. 42(2), (4), 48(1), [lex.bg](https://lex.bg/laws/ldoc/2135538631) |
| Teachers' pension fund (teachers only) | 4.3%, employer only | 2026 | KSO art. 6(7) |
| Professional pension fund (category I or II labour only) | 12% (cat. I) or 7% (cat. II), employer only | 2026 | KSO art. 157(1)(2), (4) |

Totals for a standard employee born after 1959: employee 6.58 + 2.2 + 1.4 + 0.4 + 3.2 = 13.78%; employer 8.22 + 2.8 + 2.1 + 0.6 + 4.8 = 18.52%, plus 0.4% to 1.1% work accident. For an employee born before 1960 there is no second-pillar contribution, and the higher pension rate gives the same totals.

## The taxable base

**Insurable income.** Contributions are due on all pay for work, including pay accrued but not yet paid (KSO art. 6(2), (3)). The base for each month is gross pay, but:
- not less than the minimum insurable income for the employer's main activity and the employee's job group (Appendix 1 to 31 July, Appendix 1A from 1 August), or the minimum wage where no minimum is set (KSO art. 6(3)). Part-time staff use a pro rata minimum (ZBDOO 2026, notes to Appendices 1 and 1A);
- not more than the monthly maximum: EUR 2,111.64 for January to July 2026 and EUR 2,300 for August to December 2026 (ZBDOO 2026 art. 9). Where hours are averaged over several months, the maximum is the sum of the monthly maxima (KSO art. 6(16));
- for an employee with several jobs, on the total, up to one maximum, in the order the KSO sets (KSO art. 6(11)).

Pay for past work is spread over the days on which the work was done (KSO art. 6(2)), so the ceiling of the month of work applies.

**Health insurance** uses the same base as the social contributions (ZZO art. 40(1)(1)).

**Employer and employee shares.** The employer's share is a cost of the employer. It cannot be deducted from the employee's pay, and pay cannot be cut to fund it (KSO art. 6(13)).

**Wage tax.** The employer works out an advance tax each month (ZDDFL art. 42):
1. Monthly tax base = taxable employment income accrued for the month (art. 24) less the employee's own mandatory social and health contributions withheld (art. 42(2)).
2. Less any monthly reliefs the employer applies (disability relief, voluntary insurance withheld by the employer; art. 42(3)).
3. Tax = base x 10% (art. 42(4)). It is withheld when the month's pay is finally paid (art. 42(5)) and paid over by the 25th of the month after the month it was withheld (art. 65(11)). There is no tax-free allowance.

**Annual recalculation.** If the employer holds the employee's main contract on 31 December, it recalculates the year's tax by 31 January of the next year, using the reliefs the employee documents between 30 November and 31 December (ZDDFL art. 49(1), (3), (4)). Any shortfall is withheld, and any overpayment refunded, by 31 January (art. 49(5), (6)). Tax withheld on the recalculation is paid by 25 February (art. 65(11)).

## Deadlines and filing

| What | Deadline | Source |
|---|---|---|
| Social and health contributions for the month | 25th of the next month | KSO art. 7(1); ZZO art. 40(1)(1)(c) |
| Contributions on extra pay for a past month, accrued or paid late | 25th of the month after it is accrued or paid | KSO art. 7(2) |
| Declaration 1 (data per insured person) | 25th of the month after the month the data relate to; if pay for that month is accrued or paid after that date, by the end of the month in which it is accrued or paid | Ordinance N-13 art. 4(1)(1)(a), consolidated to ДВ бр. 90/2026 |
| Declaration 6 (contributions due) | With Declaration 1 | Ordinance N-13 art. 4(3)(1) |
| Wage tax withheld | 25th of the month after the month in which it was withheld | ZDDFL art. 65(11) |
| Declaration 6 for the wage tax | 1st to 25th of the month after the month the tax was withheld | Ordinance N-13 art. 4(3)(5)(a) |
| Annual recalculation of the employee's tax | 31 January of the next year | ZDDFL art. 49(1), (5), (6) |
| Payment of tax withheld on the annual recalculation | 25 February of the next year | ZDDFL art. 65(11) |
| Declaration 6 for tax from the annual recalculation | 25 February of the next year | Ordinance N-13 art. 4(3)(5)(b) |
| Corrections to Declarations 1 and 6 by the employer | Up to 30 April of the next year; later only with NRA or NSSI approval | Ordinance N-13 art. 9(5) |

All filings go to the NRA, usually online with a qualified electronic signature or a personal code (Ordinance N-13 art. 8). Payments go to the NRA account using the employer's unified identification code (KSO art. 7(7)).

## Penalties and interest

| Breach | Penalty | Source |
|---|---|---|
| Breach of the KSO insurance rules (part one) | Fine EUR 51.13 to EUR 1,022.58 on the person at fault; plus a sanction of EUR 255.65 to EUR 1,022.58 on a company or sole trader employer, per case | KSO art. 349(1), amended by ДВ 68/2026 |
| Declaration 1 not filed, or filed late | EUR 25.56 to EUR 255.65 for an individual who is not a trader; EUR 255.65 to EUR 2,556.46 for a company or sole trader | KSO art. 355(1) |
| False Declaration 1 data to avoid contributions | EUR 25.56 to EUR 127.82 per case | KSO art. 355(2) |
| Repeat breach of art. 355(1) | Fine EUR 255.65 to EUR 1,022.58, or sanction of EUR 511.29 per case, capped at EUR 5,112.92 | KSO art. 355(4) |
| Tax not withheld or not paid on time | Up to BGN 1,000 (EUR 511.29) | ZDDFL art. 81(1) |
| Late payment of contributions or tax | Statutory interest (законна лихва) | Law on Interest on Taxes, Fees and Other Similar State Receivables, art. 1 |

The KSO amounts are now printed in euro (2026 amendments). The ZDDFL amount is still printed in leva and is converted here at BGN 1.95583.

## Cross-border points

- **Source rule.** Pay for work done in Bulgaria is Bulgarian-source income (ZDDFL art. 8(2)). A Bulgarian employer withholds the 10% tax for non-resident staff in the same way.
- **Foreign contributions.** Mandatory contributions paid abroad for the employee reduce the monthly tax base like Bulgarian ones (ZDDFL art. 42(2)).
- **Which country's insurance applies** inside the EU, the EEA and Switzerland is decided by Regulation 883/2004. Staff posted from Bulgaria stay insured in Bulgaria on the higher of their pay and the host-country minimum (KSO art. 6a). See `bg-cross-border` for A1 certificates, treaties and tax residence.

## Worked examples

### Example 1: standard employee, October 2026

An IT company (work accident rate 0.4%) pays an employee born in 1990 a gross salary of EUR 2,000 for October 2026. This is above the minimum insurable income for any activity (the highest in Appendix 1A is EUR 1,532.00) and below the EUR 2,300 ceiling, so the base is EUR 2,000.

Employee contributions at 13.78%: EUR 275.60 (pension 131.60, second pillar 44.00, illness and maternity 28.00, unemployment 8.00, health 64.00). Tax base: 2,000 - 275.60 = EUR 1,724.40. Tax at 10%: EUR 172.44. Net pay: EUR 1,551.96. Employer contributions at 18.52% + 0.4% = 18.92%: EUR 378.40. Total cost to the employer: EUR 2,378.40. Contributions and Declarations 1 and 6 are due by 25 November 2026. If the October pay is also paid (and the tax withheld) in October, the tax is due by 25 November 2026 too; if the pay is paid in November, the tax is due by 25 December 2026 (ZDDFL art. 65(11)).

```oa-check
name: Bulgaria employee born 1990, EUR 2,000 gross, October 2026, IT activity
inputs:
  gross: 2000
  ceiling: 2300
steps:
  - base: min(gross, ceiling)
  - ee_pension: round(base * 0.0658, 2)
  - ee_upf: round(base * 0.022, 2)
  - ee_illness: round(base * 0.014, 2)
  - ee_unemployment: round(base * 0.004, 2)
  - ee_health: round(base * 0.032, 2)
  - ee_total: ee_pension + ee_upf + ee_illness + ee_unemployment + ee_health
  - tax: round((gross - ee_total) * 0.10, 2)
  - net: gross - ee_total - tax
  - er_total: round(base * (0.0822 + 0.028 + 0.021 + 0.006 + 0.004 + 0.048), 2)
  - employer_cost: gross + er_total
expected:
  ee_total: 275.60
  tax: 172.44
  net: 1551.96
  er_total: 378.40
  employer_cost: 2378.40
```

### Example 2: high earner born in 1958, the ceiling changes on 1 August

A construction company (work accident rate 1.1%) pays an employee born in 1958 EUR 3,000 a month. Because he was born before 1960 he has no second-pillar contribution and pays the higher pension rate; the totals are still 13.78% (employee) and 18.52% + 1.1% = 19.62% (employer).

July 2026: the base is capped at EUR 2,111.64. Employee contributions: EUR 290.98. Tax: (3,000 - 290.98) x 10% = EUR 270.90. Net: EUR 2,438.12. Employer contributions: EUR 414.30.

August 2026: the cap rises to EUR 2,300. Employee contributions: EUR 316.94. Tax: (3,000 - 316.94) x 10% = EUR 268.31. Net: EUR 2,414.75, which is EUR 23.37 less than in July. Employer contributions: EUR 451.26. July pay keeps the July ceiling even if it is paid in August.

```oa-check
name: Bulgaria employee born 1958, EUR 3,000 gross, July and August 2026, construction
inputs:
  gross: 3000
  ceiling_july: 2111.64
  ceiling_august: 2300
steps:
  - ee_rate: 0.0878 + 0.014 + 0.004 + 0.032
  - er_rate: 0.1102 + 0.021 + 0.006 + 0.048 + 0.011
  - ee_july: round(min(gross, ceiling_july) * ee_rate, 2)
  - tax_july: round((gross - ee_july) * 0.10, 2)
  - net_july: gross - ee_july - tax_july
  - er_july: round(min(gross, ceiling_july) * er_rate, 2)
  - ee_august: round(min(gross, ceiling_august) * ee_rate, 2)
  - tax_august: round((gross - ee_august) * 0.10, 2)
  - net_august: gross - ee_august - tax_august
  - er_august: round(min(gross, ceiling_august) * er_rate, 2)
  - net_change: net_august - net_july
expected:
  ee_july: 290.98
  tax_july: 270.90
  net_july: 2438.12
  er_july: 414.30
  ee_august: 316.94
  tax_august: 268.31
  net_august: 2414.75
  er_august: 451.26
  net_change: -23.37
```

## Ask the client first

1. The employee's year of birth (before 1960 changes the pension split and removes the second pillar) and whether they moved from the universal fund into the state pension fund.
2. The employer's main economic activity code and the employee's job group (they set the work accident rate and the minimum insurable income).
3. The month each payment relates to, not just the month it is paid (the July and August ceilings differ).
4. Whether the employee has another job or is also self-insured (one ceiling for all income).
5. Whether this employer holds the main contract on 31 December, and what reliefs the employee will document (annual recalculation).
6. Whether the work is category I or II labour, or the employee is a teacher (extra employer-only pension contributions).

## Sources

| Source | URL | Read on |
|---|---|---|
| Social Insurance Code (KSO), consolidated to ДВ бр. 68/2026: arts. 4, 5, 6, 6a, 7, 157, 349, 355 | https://lex.bg/laws/ldoc/1597824512 | 2026-10-24 |
| State Social Insurance Budget Act for 2026, ДВ бр. 68/2026: arts. 9, 14, 15, Appendices 1, 1A, 2, 2A, § 6 | https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=244982 | 2026-10-24 |
| National Health Insurance Fund Budget Act for 2026, ДВ бр. 68/2026: art. 2 | https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=244981 | 2026-10-24 |
| Health Insurance Act (ZZO), consolidated to ДВ бр. 68/2026: arts. 29(3), 40 | https://lex.bg/laws/ldoc/2134412800 | 2026-10-24 |
| Personal Income Taxes Act (ZDDFL): arts. 8, 24, 25, 42, 48, 49, 65, 81 | https://lex.bg/laws/ldoc/2135538631 | 2026-10-24 |
| Council of Ministers Decree 243 of 13 November 2025 on the minimum wage, ДВ бр. 98/2025 | https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=238961 | 2026-10-24 |
| Ordinance N-13 of 17 December 2019 (Declarations 1 and 6), original text ДВ бр. 1/2020: arts. 2, 4, 8, 9 | https://dv.parliament.bg/DVWeb/showMaterialDV.jsp?idMat=144073 | 2026-10-24 |
| Ordinance N-13, consolidated text to ДВ бр. 90/2026 (amendments ДВ бр. 10/2021, 15/2024, 17/2026, 90/2026; secondary consolidation by KiK-Info, checked article by article against the original): arts. 4, 6, 8, 9 | https://kik-info.com/normativna-baza/naredbi/h-13/ | 2026-10-24 |
| NSSI, new insurable income limits from 1 August 2026 | https://nssi.bg/dohod01082026/ | 2026-10-24 |
| Euro Introduction Act: arts. 11, 12, 13 | https://lex.bg/bg/laws/ldoc/2137244903 | 2026-10-24 |
| Law on Interest on Taxes, Fees and Other Similar State Receivables, art. 1 | https://lex.bg/bg/laws/ldoc/2123675140 | 2026-10-24 |

Not yet confirmed: the amending ДВ issues of Ordinance N-13 were not read on dv.parliament.bg (the consolidated text used is a secondary consolidation; arts. 4(1)(1)(a), 4(3)(1), 4(3)(5) and 9(5) read the same in the original 2020 text); the NRA's own 2026 payroll guidance (nra.bg served a human check, so it was not read); the statutory late-payment interest rate after the euro changeover; the minimum wage for 2027 (no decree had been published when this was read).

> Contributed by Michael Cutajar.

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `bulgaria-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/bulgaria-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
