---
name: latvia-social-contributions
description: "Latvian state social insurance contributions (VSAOI) for tax year 2026. Covers the 34.09% rate for employees (employer 23.59%, employee 10.50%) and the reduced rates for pensioners, board members and others, the EUR 105,300 maximum base and the solidarity tax above it with the refund down to 25%, the EUR 780 minimum wage and the EUR 2,340 quarterly minimum contribution base for employees, self-employed contributions (31.07% on at least EUR 780 a month plus 10% for pensions), quarterly reports by the 17th and payment by the 23rd, workers of foreign employers (31.83%), and late interest of 0.05% a day. Trigger on: VSAOI, Latvian social tax, solidaritātes nodoklis, pašnodarbinātā iemaksas, minimālās obligātās iemaksas. Out of scope: monthly gross-to-net and wage tax (latvia-payroll), the annual income tax return (latvia-income-tax), microenterprise tax (latvia-tax-optimization), A1 certificates and residence (lv-cross-border)."
jurisdiction: LV
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-24
version: 0.2
verified_by: pending
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Latvia: state social insurance contributions (2026) v0.2

> **Source-cited draft.** No accountant has reviewed this skill yet. Every figure comes from the consolidated law On State Social Insurance (SI Law), the Solidarity Tax Law, the Law On Personal Income Tax (PIT Law), the Law On Taxes and Fees (LTF) and State Revenue Service (VID) pages. See Sources for how they were read.

Related skills in this pack:

- Monthly payroll, wage tax withholding and the employer's report: [latvia-payroll](latvia-payroll.md).
- The annual income tax return, where contributions are deducted: [latvia-income-tax](latvia-income-tax.md).
- Microenterprise tax, where contributions are part of the tax: [latvia-tax-optimization](latvia-tax-optimization.md).
- Non-residents, posted workers and treaties: [lv-cross-border](lv-cross-border.md).

## Who this applies to

- **Employees** of Latvian employers, including board members who count as employees under SI Law s. 1(2)(m). The employer computes and pays both shares (SI Law s. 20(1), (2), s. 21(1), (2)).
- **Self-employed people** registered for business income under the PIT Law. They report and pay their own contributions each quarter (SI Law s. 14(2), s. 14.1, s. 21(3), s. 23(2)).
- **Workers of foreign employers** not registered in Latvia. They pay their own contributions each quarter (SI Law s. 14(4), s. 20(5), s. 21(4)).
- **Not covered here:** people covered by another country's system under an A1 certificate (no Latvian contributions), microenterprise tax payers (80% of their microenterprise tax goes to their social insurance, per VID), and voluntary insurance (SI Law s. 18(3), s. 21(5)).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Employee insured for all risks | 34.09%: employer 23.59%, employee 10.50% | 2026 | https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu (s. 18(1)) |
| Employee of state pension age | 30.02%: employer 20.77%, employee 9.25% | 2026 | https://www.vid.gov.lv/lv/valsts-socialas-apdrosinasanas-obligato-iemaksu-likmes |
| Employee receiving a service pension or disability special pension | 31.70%: employer 21.94%, employee 9.76% | 2026 | https://www.vid.gov.lv/lv/valsts-socialas-apdrosinasanas-obligato-iemaksu-likmes |
| Board member under SI Law s. 1(2)(m) (24.91% if of pension age) | 27.20% | 2026 | https://www.vid.gov.lv/lv/valsts-socialas-apdrosinasanas-obligato-iemaksu-likmes |
| Self-employed (29.36% if of pension age; 26.59% for real estate managers) | 31.07% | 2026 | https://www.vid.gov.lv/lv/pasnodarbinata-socialas-apdrosinasanas-iemaksas |
| Self-employed pension contribution | 10% | 2026 | https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu (s. 14.1) |
| Foreign worker of a foreign employer | 31.83% | 2026 | https://www.vid.gov.lv/lv/valsts-socialas-apdrosinasanas-obligato-iemaksu-likmes |
| Maximum annual contribution base | EUR 105,300 | 2026 | https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu (s. 14(5)) |
| Solidarity tax on the base above EUR 105,300 | Collected at the person's contribution rate; final rate 25% | 2026 | https://likumi.lv/ta/id/278636-solidaritates-nodokla-likums (s. 6.1, 6.2) |
| Minimum monthly wage | EUR 780 | 2026 | https://www.vid.gov.lv/lv/pasnodarbinata-socialas-apdrosinasanas-iemaksas |
| Employee minimum contribution base per quarter | EUR 2,340 (three minimum wages) | 2026 | https://www.vid.gov.lv/lv/valsts-socialas-apdrosinasanas-obligatas-iemaksas ; SI Law s. 20.4(1) |
| Late-payment interest | 0.05% a day | 2026 | https://likumi.lv/ta/id/33946-par-nodokliem-un-nodevam (s. 29(2)) |

One percentage point of the contribution rate funds health care (SI Law ch. III.1; VID).

## The taxable base

**Employees.** The base is all employment pay from which wage tax must be withheld. The non-taxable minimum, reliefs and eligible expenses are not taken off (SI Law s. 14(1)). Employer contributions to licensed private pension funds and qualifying insurance premiums are left out, within PIT Law limits (s. 14(7)). Board members are based on at least the minimum monthly wage (s. 14(12.1)). Professional athletes are based on at least EUR 860 a month (s. 14(20)).

**Maximum base and solidarity tax.** The base counts towards the EUR 105,300 cap for the calendar year (SI Law s. 14(5)). Above the cap, the employer keeps withholding and paying at the same rate. That money is solidarity tax, not contributions (SI Law s. 21.2; Solidarity Tax Law s. 3, s. 6.2(1)). The final rate is 25% (s. 6.1). VID refunds the difference to the employer only, by 1 September of the following year, where the rate is split between employer and employee (s. 6.2(2), (3)). VSAA works out the refund by 1 June (s. 7(3)). Of the 25%, 1 point goes to health care, 14 points to the pension budget and 10 points to personal income tax (s. 8.1). The employee's share of the solidarity tax is deductible for income tax (PIT Law s. 10(1)(1.1)).

**Minimum base for employees.** If an employee's base for a quarter is below EUR 2,340, the employer pays contributions on the gap from its own funds (SI Law s. 20.4(1), (2)). Bases with several employers, or as employee and self-employed, are added together, and the gap is shared in proportion. VSAA computes the amount after the quarter (s. 20.4(7)). The minimum does not apply to pension-age people, people with a disability, parents with a child under 3 recorded in their or their spouse's wage tax book, full-time students under 24, prisoners who work, and other listed groups (s. 20.4(4)). Days of unpaid leave, childcare leave or sick leave on sheet B reduce it pro rata (s. 20.4(5)). From 2026 the minimum does not apply to the self-employed, microenterprise tax payers or royalty recipients (s. 20.4(6); transitional provision 105).

**Self-employed.** Monthly income is receipts less expenses for that month. Income received as an employee is not counted (VID self-employed page).

- If monthly income is EUR 780 or more, the person pays 31.07% on a base they choose of at least EUR 780. They also pay 10% for pensions on the part of income above the chosen base (SI Law s. 14(2), s. 14.1(2), s. 14(18)).
- If monthly income is below EUR 780, only 10% of the actual income is paid, for pensions (s. 14.1(1)). This 10% does not build funded pension capital (s. 14.1(6)).
- Self-employed people with farm income or intellectual property income work out the 10% once a year (s. 14.1(3)).

## Deadlines and filing

- **Employers:** report by the 17th of the month after the reporting month (SI Law s. 23(1)). Pay by the 23rd of that month (s. 21(1)). Minimum contributions are paid by the 23rd of the third month after VSAA's notice (s. 20.4(9)).
- **Self-employed and workers of foreign employers:** report each quarter by 17 April, 17 July, 17 October and 17 January (SI Law s. 23(2)). Pay by 23 April, 23 July, 23 October and 23 January (s. 21(3), (4)). A report can be corrected once, within a month of the payment date (s. 20.1(6)).
- **Farm and intellectual property income, annual 10%:** report by 17 January (s. 23(2.2)) and pay by 23 January of the next year (s. 21(3.2)).
- All payments go to the single tax account. Reports are filed in VID's Electronic Declaration System.
- **Overpaid contributions:** VSAA works them out within three months after the year end (SI Law s. 21.1(1)). Amounts under EUR 22.41 are carried forward (s. 21.1(3)).

## Penalties and interest

- **Late payment:** 0.05% of the unpaid amount for each day late, under the LTF (SI Law s. 16(2); LTF s. 29(2)). It is charged on the 1st and 15th of each month. None is charged if the payment arrives by the last day of the month in which it was due (LTF s. 29(2.1), (2.2)(1)). Late interest is payable from the employer's or self-employed person's own funds (SI Law s. 16(3)).
- **Late reports (LTF s. 141; penalty unit EUR 5):**
  - 3 to 10 days late: a warning or EUR 25 to EUR 70. There is no fine for one monthly or quarterly report up to 5 days late in 12 months.
  - 11 to 20 days late: EUR 75 to EUR 150.
  - 21 to 30 days late: EUR 155 to EUR 280.
  - Over 30 days late or not filed: EUR 285 to EUR 700.
- **Understatement found in an audit (LTF s. 32):** the tax plus interest, and a penalty of 20% of the understated tax. The penalty is 30% where the understatement exceeds 15% of the tax due. For undeclared pay, VID computes the contributions itself (s. 32(5.1), (5.2)).

## Cross-border points

- EU Regulation 883/2004 decides which single country's system applies. A person with an A1 certificate from another state pays no Latvian contributions for that period. If an A1 is issued late, VSAA transfers the contributions paid to the other state, except minimum contributions (SI Law s. 21.4). The Latvian employer's report entries are then cancelled.
- Contributions paid in another member state for a period later ruled Latvian are transferred in, without late interest (SI Law s. 21.3(3)).
- A foreign employer's local employee and a foreign worker of a foreign employer pay contributions themselves. The foreign worker pays 31.83%, without the work-accident and unemployment parts, from the 184th day of stay. For a posting of up to 12 months that runs over, it starts from the 367th day (SI Law s. 20(5)).
- Wage tax for people insured abroad: see [latvia-payroll](latvia-payroll.md). Residence and treaties: see [lv-cross-border](lv-cross-border.md).

## Worked examples

**Example 1: self-employed person, one quarter.** A self-employed designer has monthly income (receipts less expenses) of EUR 1,200 in April, EUR 600 in May and EUR 2,000 in June 2026. They choose the minimum base. April and June reach EUR 780, so each of those months carries 31.07% on EUR 780 (EUR 242.346), plus 10% on the excess: EUR 42 for April and EUR 122 for June. May is below EUR 780, so only 10% of EUR 600 (EUR 60) is due. Contributions for the quarter are EUR 484.69 at 31.07% and EUR 224 for pensions, EUR 708.69 in total. The report is due 17 July 2026 and payment is due 23 July 2026.

```oa-check
name: Self-employed quarter, months EUR 1,200 / 600 / 2,000 (2026)
inputs:
  m1: 1200
  m2: 600
  m3: 2000
  min_wage: 780
steps:
  - full_rate: round(min_wage * 0.3107 * 2, 2)
  - pension: (m1 - min_wage) * 0.10 + m2 * 0.10 + (m3 - min_wage) * 0.10
  - total: full_rate + pension
expected:
  full_rate: 484.69
  pension: 224
  total: 708.69
```

**Example 2: employee above the maximum base, solidarity tax refund.** An employee under pension age earns EUR 144,000 in 2026. Contributions on the first EUR 105,300 are normal contributions. On the EUR 38,700 above the cap, the employer keeps paying 23.59% (EUR 9,129.33) and withholding 10.5% (EUR 4,063.50), EUR 13,192.83 in all. This is solidarity tax. The final rate is 25%, EUR 9,675. VID refunds the EUR 3,517.83 difference to the employer, by 1 September 2027. The employee's share is not refunded.

```oa-check
name: Salary EUR 144,000, solidarity tax and employer refund (2026)
inputs:
  salary: 144000
  cap: 105300
steps:
  - excess: max(salary - cap, 0)
  - employer_part: excess * 0.2359
  - employee_part: excess * 0.105
  - paid: employer_part + employee_part
  - final_tax: excess * 0.25
  - refund_to_employer: paid - final_tax
expected:
  excess: 38700
  employer_part: 9129.33
  employee_part: 4063.50
  paid: 13192.83
  final_tax: 9675
  refund_to_employer: 3517.83
```

## Ask the client first

1. Is the person an employee, a board member, self-employed, a microenterprise tax payer, or working for a foreign employer?
2. Have they reached state pension age, or do they receive a service or disability special pension?
3. Do they hold an A1 certificate from another country?
4. For an employee: is quarterly pay below EUR 2,340, and does the person fall in an exempt group?
5. For the self-employed: monthly income for each month of the quarter, and do they want a base above EUR 780?
6. Will employment pay for the year pass EUR 105,300?

## Sources

| Source | URL | Read on |
|---|---|---|
| Law On State Social Insurance (Par valsts sociālo apdrošināšanu), consolidated with amendments to 16 April 2026: ss. 14, 14.1, 16, 18, 20, 20.1, 20.4, 21, 21.1, 21.2, 21.3, 21.4, 23; transitional provisions 102 to 105 | https://likumi.lv/ta/id/45466-par-valsts-socialo-apdrosinasanu | 2026-10-24 |
| Solidarity Tax Law (Solidaritātes nodokļa likums), version in force from 1 January 2021: ss. 3, 5, 6.1, 6.2, 7, 8.1 | https://likumi.lv/ta/id/278636-solidaritates-nodokla-likums | 2026-10-24 |
| Law On Personal Income Tax (Par iedzīvotāju ienākuma nodokli): s. 10(1)(1.1) | https://likumi.lv/ta/id/56880-par-iedzivotaju-ienakuma-nodokli | 2026-10-24 |
| Law On Taxes and Fees (Par nodokļiem un nodevām): ss. 29, 32, 141 | https://likumi.lv/ta/id/33946-par-nodokliem-un-nodevam | 2026-10-24 |
| Administrative Liability Law: s. 16(2) | https://likumi.lv/ta/id/303007 | 2026-10-24 |
| VID, state social insurance contributions (2026 minimum quarterly base EUR 2,340; maximum EUR 105,300) | https://www.vid.gov.lv/lv/valsts-socialas-apdrosinasanas-obligatas-iemaksas | 2026-10-24 |
| VID, contribution rate table | https://www.vid.gov.lv/lv/valsts-socialas-apdrosinasanas-obligato-iemaksu-likmes | 2026-10-24 |
| VID, self-employed contributions (EUR 780, 31.07%, 10%; updated 14 May 2026) | https://www.vid.gov.lv/lv/pasnodarbinata-socialas-apdrosinasanas-iemaksas | 2026-10-24 |
| VID, solidarity tax rates (updated 11 July 2026) | https://www.vid.gov.lv/lv/solidaritates-nodokla-likmes | 2026-10-24 |

likumi.lv and vid.gov.lv refused connections from our network on 23 and 24 October 2026. All texts were read from Internet Archive (web.archive.org) copies made in 2026: the SI Law captured 3 October 2026, the Solidarity Tax Law 18 February 2026 (m.likumi.lv), the PIT Law 1 September 2026, the LTF 18 September 2026, the Administrative Liability Law 10 August 2026, the VID contributions page 13 September 2026, the VID rate table 10 August 2026, the VID self-employed page 19 May 2026 and the VID solidarity tax page 26 September 2026.

Not yet confirmed: the Cabinet regulation that splits the reduced rates (pensioners, board members, self-employed, foreign workers) by insurance type (rates taken from the VID table, which says it was published 28 September 2022); Cabinet Regulation No. 656 on the 2026 minimum wage (EUR 780 is from VID pages); whether the employer's minimum contributions on the quarterly gap are at the full 34.09% for a fully insured employee (s. 20.4 says the employer pays from its own funds but the rate split was not confirmed); the Cabinet regulation on the self-employed minimum base under SI Law s. 14(2); how contributions on royalties to a person not registered for business are collected in 2026 (SI Law s. 14(19)); the Cabinet regulation on the solidarity tax refund method; SI Law amendments adopted after 3 October 2026.
