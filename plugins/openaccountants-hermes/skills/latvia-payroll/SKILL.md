---
name: latvia-payroll
description: "Latvian payroll for tax year 2026: how an employer computes and withholds wage tax (algas nodoklis) and state social insurance contributions (VSAOI) each month. Covers the flat 25.5% monthly withholding, the EUR 550 monthly non-taxable minimum and EUR 250 dependant relief through the wage tax book, employee 10.5% and employer 23.59% contributions, the EUR 105,300 maximum base and solidarity tax, the EUR 780 minimum wage and the EUR 2,340 quarterly minimum contribution base, the employer's monthly report by the 17th and payment by the 23rd, the 33% band settled in the annual return, and late-payment interest of 0.05% a day. Trigger on: Latvia payroll, gross to net Latvia, darba devēja ziņojums, algas nodokļa grāmatiņa, Latvian wage tax. Out of scope: contribution rules in depth and self-employed contributions (latvia-social-contributions), the annual return (latvia-income-tax), non-residents (lv-cross-border)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/latvia-payroll"
  jurisdiction: "LV"
  tax_year: "2026"
  last_updated: "2026-10-24"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Latvia: payroll (2026) v0.2

> **Source-cited draft.** No accountant has reviewed this skill yet. Every figure comes from the consolidated Law On Personal Income Tax (PIT Law), the law On State Social Insurance (SI Law), the Solidarity Tax Law, the Law On Taxes and Fees (LTF) and the Administrative Liability Law, and from State Revenue Service (VID) pages. See Sources for how they were read.

Related skills in this pack:

- Contribution rates for every category, the minimum contribution base, self-employed contributions and the solidarity tax refund: [latvia-social-contributions](latvia-social-contributions.md).
- The annual income tax return, the 33% band, the 3% surcharge and eligible expenses: [latvia-income-tax](latvia-income-tax.md).
- Non-residents, residence tests and treaties: [lv-cross-border](lv-cross-border.md).
- Microenterprise tax employers: [latvia-tax-optimization](latvia-tax-optimization.md).

## Who this applies to

- Every employer that pays salary to an employee working in Latvia. The employer is the tax agent: it computes, withholds and pays the wage tax (PIT Law s. 17(1), (5)) and computes and pays both its own and the employee's social contributions (SI Law s. 20(1), (2), s. 21(1), (2)).
- Employees who are Latvian tax residents and non-residents working for a Latvian employer. The monthly taxable pay differs for each (PIT Law s. 17(3)).
- A board member of a company who is treated as an employee under SI Law s. 1(2)(m) has a contribution base of at least the minimum monthly wage (SI Law s. 14(12.1)), with exceptions in s. 14(12.2) and (12.3).
- Out of scope here: self-employed people (they report and pay their own contributions each quarter, see latvia-social-contributions), seasonal farm workers (special seasonal workers' tax, PIT Law s. 11.12), and microenterprise tax payers' own contributions.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Monthly wage tax withheld by the employer | 25.5% | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 15(3)) |
| Annual tax on income above the maximum contribution base (settled in the annual return) | 33% | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 15(2)(2)) |
| Monthly non-taxable minimum (only where the wage tax book is filed) | EUR 550 a month (s. 12(1) says EUR 570; transitional provision 197 sets EUR 550 for 2026) | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 12(1); transitional provision 197) |
| Relief for each dependant | EUR 250 a month | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 13(1.2)) |
| Social contributions, employee fully insured | 34.09% total: employer 23.59%, employee 10.50% | 2026 | https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu (s. 18(1)) |
| Social contributions, employee of state pension age | 30.02% total: employer 20.77%, employee 9.25% | 2026 | https://www.vid.gov.lv/lv/valsts-socialas-apdrosinasanas-obligato-iemaksu-likmes |
| Maximum annual contribution base | EUR 105,300 | 2026 | https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu (s. 14(5)) |
| Contributions on pay above the maximum base | Same rate, collected as solidarity tax; the excess over a 25% rate is refunded to the employer | 2026 | https://likumi.lv/ta/id/278636-solidaritates-nodokla-likums (s. 6.1, 6.2) |
| Minimum monthly wage | EUR 780 | 2026 | https://www.vid.gov.lv/lv/pasnodarbinata-socialas-apdrosinasanas-iemaksas |
| Minimum contribution base per quarter (three minimum wages) | EUR 2,340 | 2026 | https://www.vid.gov.lv/lv/valsts-socialas-apdrosinasanas-obligatas-iemaksas ; SI Law s. 20.4(1) |
| Employer's monthly report due | 17th of the following month | 2026 | https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu (s. 23(1)) |
| Contributions due | 23rd of the following month | 2026 | https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu (s. 21(1)) |
| Wage tax due | 23rd of the month the pay is paid out | 2026 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli (s. 17(5)) |
| Late-payment interest | 0.05% a day | 2026 | https://likumi.lv/ta/id/33946-par-nodokliem-un-nodevam (s. 29(2)) |
| Penalty unit for administrative fines | EUR 5 | 2026 | https://likumi.lv/ta/id/303007 (s. 16(2)) |

The business risk state fee (uzņēmējdarbības riska valsts nodeva) is a further employer cost per employee per month. VID says its amount is set each year by Cabinet regulation and is paid by the 23rd of the next month with the employer's report. The 2026 amount was not read (see Sources).

## The taxable base

**Contributions.** The base for both employer and employee contributions is all pay from employment from which wage tax must be withheld, before the non-taxable minimum, reliefs and eligible expenses (SI Law s. 14(1)). Employer contributions to licensed private pension funds and qualifying life, health and accident insurance premiums are left out, within the PIT Law limits (s. 14(7)).

**Wage tax.** For a resident whose wage tax book (algas nodokļa grāmatiņa) is filed with this employer, the monthly taxable pay is gross pay less (PIT Law s. 17(3)(1), s. 10(2)):

1. the employee's social contributions (10.5%, and the employee share of solidarity tax);
2. the EUR 550 non-taxable minimum (PIT Law transitional provision 197);
3. EUR 250 for each dependant recorded in the book.

Then 25.5% applies (s. 15(3)). Where the book is not filed with this employer, only the employee contributions come off (s. 17(3)(2)). For a non-resident, s. 17(3)(3) applies. A person has only one wage tax book and files it with one payer of their choice (PIT Law s. 6).

**Pay above EUR 8,775 a month.** One twelfth of EUR 105,300 is EUR 8,775. If monthly pay exceeds it, the deductions come off the part up to EUR 8,775 first (PIT Law s. 3(2.4)). Monthly withholding still uses 25.5% for everyone covered by Latvian social insurance (s. 15(3)). The 33% rate for income above EUR 105,300 is settled in the annual return. There the band is tested on income before deductions, and the deductions come off the 25.5% part first (s. 3(2.4), s. 15(15)). The part of the solidarity tax moved to the income tax account counts as tax paid (s. 2(3)), and the deductible contributions are cut by the same amount (s. 10(1.10)). Example 2 shows the result.

**Above the maximum base.** Once a person's pay for the year passes EUR 105,300, the employer keeps withholding and paying contributions at the same rates. The excess is solidarity tax, not pension contributions (SI Law s. 21.2; Solidarity Tax Law s. 6.2(1)). The employer gets back the difference between what was paid and 25% (see latvia-social-contributions). Ten points of the 25% count as the employee's income tax paid (PIT Law s. 2(3); Solidarity Tax Law s. 8.1).

**Minimum contributions.** If an employee's base for a quarter is below EUR 2,340, the State Social Insurance Agency (VSAA) works out the gap and the employer pays contributions on it from its own funds (SI Law s. 20.4(1), (2)). Bases with several employers are added together. Pensioners, people with a disability, full-time students under 24, parents of a child under 3 and other listed groups are exempt (s. 20.4(4)). Unpaid leave, childcare leave and sick leave days on sheet B reduce the minimum pro rata (s. 20.4(5)).

## Deadlines and filing

- **When someone starts work:** register them with VID in the informative declaration on employees. Late filing is fined under LTF s. 142(2).
- **Monthly employer's report (darba devēja ziņojums):** by the 17th of the month after the reporting month, in VID's Electronic Declaration System (EDS) (SI Law s. 23(1)). It reports contributions, wage tax and the business risk fee.
- **Contributions:** paid to the single tax account by the 23rd of the month after the reporting month (SI Law s. 21(1)). If pay is late, contributions are still due as if it had been paid on time (s. 21(9)).
- **Wage tax:** paid to the single tax account by the 23rd of the month in which the pay is paid out. It is due by the 23rd of the following month in five cases: pay for a month calculated and paid in that same month, final pay at termination, holiday pay, sick pay, and court-ordered back pay (PIT Law s. 17(5)).
- **Minimum contributions:** VSAA notifies VID by the 20th of the third month after the quarter. The employer pays by the 23rd of the third month after receiving the notice (SI Law s. 20.4(7) to (9)).
- **Year end:** the employer sends VID a statement of amounts paid to each person by 1 February 2027. For someone who left during the year, it is due by the 15th of the month after the employment ended (PIT Law s. 17(7)). The employee gets a copy within 15 days of asking (s. 17(6)).
- **Corrections:** the employer may correct an employee's pay and contributions within three years of the report deadline, but not downward (SI Law s. 20.1(2)).

## Penalties and interest

- **Late payment:** 0.05% of the unpaid amount for each day late (LTF s. 29(2); SI Law s. 16(2)). It is charged twice a month, on the 1st and the 15th. None is charged if the payment arrives by the last day of the month in which it was due (LTF s. 29(2.1), (2.2)(1)).
- **Late returns (LTF s. 141), penalty unit EUR 5:**
  - 3 to 10 days late: a warning or EUR 25 to EUR 70. There is no fine for one monthly or quarterly return up to 5 days late in 12 months.
  - 11 to 20 days late: EUR 75 to EUR 150.
  - 21 to 30 days late: EUR 155 to EUR 280.
  - Over 30 days late or not filed: EUR 285 to EUR 700.
- **Late or missing employee registration or year-end statement (LTF s. 142(2)):** a natural person is fined EUR 140 to EUR 500. A legal person is fined EUR 350 to EUR 7,100.
- **Understated tax found in an audit (LTF s. 32):** the tax plus late interest, and a penalty of 20% of the understated tax. The penalty is 30% where the understatement exceeds 15% of the tax due. It is halved for a first offence where filing and payment dates were kept and the taxpayer cooperated (s. 32(7)). Under s. 32(5.1), VID computes contributions and wage tax on pay that was not recorded or reported.

## Cross-border points

- An employee covered by another country's social insurance (an A1 certificate) pays no Latvian contributions. Their wage tax is 33% on the part of monthly pay above EUR 8,775 (PIT Law s. 15(16)).
- A foreign employer with no Latvian registration does not run Latvian payroll. Its employee working in Latvia pays the contributions directly, at 31.83%, from the 184th day of stay (SI Law s. 20(5); VID rate table). They report and pay quarterly, by the 17th and the 23rd of the month after the quarter (SI Law s. 23(2), s. 21(4)).
- Non-resident employees get no non-taxable minimum or dependant relief through payroll (PIT Law s. 17(3)(3)).
- Treaty relief, residence and the 183-day test: see [lv-cross-border](lv-cross-border.md).

## Worked examples

**Example 1: standard monthly payslip.** A resident employee earns EUR 2,000 gross in March 2026. The wage tax book is filed with this employer and records one dependant child. Employee contributions are 10.5%: EUR 210. Taxable pay is EUR 2,000 less EUR 210, EUR 550 and EUR 250, which is EUR 990. Wage tax at 25.5% is EUR 252.45. Net pay is EUR 1,537.55. The employer adds 23.59%, EUR 471.80, so salary and contributions cost EUR 2,471.80, before the business risk fee. The report is due by 17 April 2026. Contributions are due by 23 April 2026. If the March pay is paid out in April, the wage tax is also due by 23 April.

```oa-check
name: Gross EUR 2,000 a month, one dependant, wage tax book filed (2026)
inputs:
  gross: 2000
  dependants: 1
steps:
  - ee_vsaoi: gross * 0.105
  - er_vsaoi: gross * 0.2359
  - taxable: gross - ee_vsaoi - 550 - 250 * dependants
  - wage_tax: taxable * 0.255
  - net: gross - ee_vsaoi - wage_tax
  - employer_cost: gross + er_vsaoi
expected:
  ee_vsaoi: 210
  er_vsaoi: 471.80
  taxable: 990
  wage_tax: 252.45
  net: 1537.55
  employer_cost: 2471.80
```

**Example 2: high earner, annual return.** A resident earns EUR 12,000 a month in 2026, EUR 144,000 for the year. The wage tax book is filed, with no dependants and no other income. Each month the employer withholds 10.5% contributions, EUR 1,260. Wage tax is 25.5% of EUR 12,000 less EUR 1,260 less EUR 550, which is EUR 2,598.45. That is EUR 31,181.40 for the year. The employee keeps paying 10.5% after pay passes EUR 105,300 in September. On the EUR 38,700 above the cap this is solidarity tax. Of the 25% solidarity tax, 10 points (EUR 3,870) go to the personal income tax account and count as income tax paid by the employee (PIT Law s. 2(3); Solidarity Tax Law s. 8.1). In the annual return the deductible contributions are cut by that EUR 3,870 (PIT Law s. 10(1.10)): EUR 15,120 less EUR 3,870 is EUR 11,250. With the EUR 6,600 minimum, deductions are EUR 17,850, and they come off the 25.5% part (s. 3(2.4)). So EUR 87,450 is taxed at 25.5% (EUR 22,299.75) and EUR 38,700 at 33% (EUR 12,771). Tax for the year is EUR 35,070.75. Less the EUR 31,181.40 withheld and the EUR 3,870 credit, the employee pays EUR 19.35. Income is over EUR 105,300, so the return is filed 1 April to 1 July 2027 and paid by 23 July 2027 (latvia-income-tax). Income is under EUR 200,000, so there is no 3% surcharge.

```oa-check
name: EUR 12,000 a month, monthly 25.5% withholding and annual 33% band with the solidarity tax credit (2026)
inputs:
  monthly: 12000
  months: 12
  cap: 105300
steps:
  - ee_vsaoi_month: monthly * 0.105
  - wage_tax_month: (monthly - ee_vsaoi_month - 550) * 0.255
  - withheld_year: wage_tax_month * months
  - income: monthly * months
  - high_band: max(income - cap, 0)
  - solidarity_pit_credit: high_band * 0.10
  - deductions: income * 0.105 - solidarity_pit_credit + 550 * months
  - low_band: max(min(income, cap) - deductions, 0)
  - annual_tax: low_band * 0.255 + high_band * 0.33
  - balance_due: annual_tax - withheld_year - solidarity_pit_credit
expected:
  ee_vsaoi_month: 1260
  wage_tax_month: 2598.45
  withheld_year: 31181.40
  high_band: 38700
  solidarity_pit_credit: 3870
  deductions: 17850
  low_band: 87450
  annual_tax: 35070.75
  balance_due: 19.35
```

## Ask the client first

1. Is the employee's wage tax book filed with you, and which dependants does it record? Without it, no minimum or relief is given.
2. Has the employee reached state pension age, or do they receive a service or disability special pension? A different contribution rate applies.
3. Is the employee covered by another country's social insurance (A1 certificate), or a non-resident?
4. Will pay for the year pass EUR 105,300? If so, expect solidarity tax, a refund to you, and a 33% band settled in the employee's annual return.
5. Is the person a board member without an employment contract, part-time, or in an exempt group for the minimum contribution base?
6. On what date is each month's pay paid out? This fixes the wage tax deadline.

## Sources

| Source | URL | Read on |
|---|---|---|
| Law On Personal Income Tax (Par iedzīvotāju ienākuma nodokli), consolidated, in force 1 January 2026: ss. 2(3), 3(2), 3(2.4), 6, 10(1), 10(1.10), 10(2), 12(1), 13(1.2), 15(2), 15(3), 15(15), 15(16), 17; transitional provision 197 | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli | 2026-10-24 |
| Law On State Social Insurance (Par valsts sociālo apdrošināšanu), consolidated with amendments to 16 April 2026: ss. 14, 16, 18, 20, 20.1, 20.4, 21, 21.2, 23 | https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu | 2026-10-24 |
| Solidarity Tax Law (Solidaritātes nodokļa likums), version in force from 1 January 2021: ss. 3, 6.1, 6.2, 8.1 | https://likumi.lv/ta/id/278636-solidaritates-nodokla-likums | 2026-10-24 |
| Law On Taxes and Fees (Par nodokļiem un nodevām): ss. 29, 32, 141, 142 | https://likumi.lv/ta/id/33946-par-nodokliem-un-nodevam | 2026-10-24 |
| Administrative Liability Law: s. 16(2) | https://likumi.lv/ta/id/303007 | 2026-10-24 |
| VID, state social insurance contributions (2026 minimum quarterly base EUR 2,340; maximum EUR 105,300) | https://www.vid.gov.lv/lv/valsts-socialas-apdrosinasanas-obligatas-iemaksas | 2026-10-24 |
| VID, contribution rate table | https://www.vid.gov.lv/lv/valsts-socialas-apdrosinasanas-obligato-iemaksu-likmes | 2026-10-24 |
| VID, self-employed contributions (minimum wage EUR 780; updated 14 May 2026) | https://www.vid.gov.lv/lv/pasnodarbinata-socialas-apdrosinasanas-iemaksas | 2026-10-24 |
| VID, business risk state fee | https://www.vid.gov.lv/lv/uznemejdarbibas-riska-valsts-nodeva | 2026-10-24 |

likumi.lv and vid.gov.lv refused connections from our network on 23 and 24 October 2026. All texts were read from Internet Archive (web.archive.org) copies made in 2026: the PIT Law captured 1 September 2026, the SI Law 3 October 2026, the Solidarity Tax Law 18 February 2026 (m.likumi.lv), the LTF 18 September 2026, the Administrative Liability Law 10 August 2026, the VID contributions page 13 September 2026, the VID rate table 10 August 2026, the VID self-employed page 19 May 2026 and the VID business risk fee page 16 March 2026.

Not yet confirmed: the 2026 amount of the business risk state fee (the Cabinet regulation for 2026 was not read); Cabinet Regulation No. 656 on the minimum wage itself (EUR 780 is taken from VID pages); the Cabinet regulation that splits the reduced rates for pensioners and other groups between employer and employee (taken from the VID table, not the regulation); Cabinet Regulation No. 827 on the employer's report and the exact deadline for registering a new employee; whether the s. 17(5) wage tax deadline moves to the following month when pay is paid out after the 23rd; whether VID treats the employer's report as a tax return under LTF s. 141 or an informative declaration under s. 142; SI Law and PIT Law amendments adopted after the capture dates.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `latvia-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/latvia-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
