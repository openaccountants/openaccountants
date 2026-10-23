---
name: be-payroll-withholding
description: "Belgian payroll withholding (bedrijfsvoorheffing / précompte professionnel) on employees' and directors' pay for 2026, computed with the key formula (sleutelformule) of Annex III to the KB/WIB 92. Covers the five steps: pay after employee social security, annualisation, flat-rate professional expenses (30%, capped at EUR 6,070), the withholding scale (which builds in a 7% local surcharge), the tax-free amount, the marital quotient, reductions for children, dependants and single parents, and the work bonus and overtime reductions. Two rule sets apply in 2026: the KB of 11 December 2025 (January to October) and the KB of 27 September 2026 (from 1 November). Also covers holiday pay and bonus rates, the withholding return and payment dates, interest and fines. Trigger on: bedrijfsvoorheffing, précompte professionnel, sleutelformule, formule-clé, Bijlage III, net pay Belgium. Out of scope: belgium-payroll (social security, work bonus amounts), be-employee-income-tax, be-cross-border."
version: 0.1
jurisdiction: BE
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
verified_by: pending
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Belgium: payroll withholding (bedrijfsvoorheffing / précompte professionnel), 2026 key formula

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any person's facts. Do not rely on it to run a payroll, file or pay without review by a qualified professional in Belgium.

This skill computes the monthly withholding an employer takes from pay in 2026. Related skills:

- Employee and employer social security (RSZ / ONSS), the social work bonus amounts, payslips and DmfA: `belgium-payroll`
- The employee's annual return, where withholding is credited against the final tax: `be-employee-income-tax`
- Self-employed people and company directors' own social contributions: `be-social-contributions`
- Frontier workers, non-residents and the inbound regime: `be-cross-border`
- Company side (director pay test, deductibility of pay): `be-corporate-tax`

**2026 has two rule sets.** Pay paid or granted from 1 January to 31 October 2026 uses Annex III as replaced by the KB of 11 December 2025. Pay paid or granted from 1 November 2026 uses the changes of the KB of 27 September 2026, which brings the tax-free amount, the marital quotient and the family reductions into line with the law of 15 July 2026 reforming personal income tax. A third KB, of 24 July 2026, raised the work bonus reduction from 1 August 2026 and the overtime ceiling from 1 January 2026. Pick the rule set by the date the pay is paid or granted, not the month it relates to.

## Who this applies to

- **Employers and other payers** in Belgium who pay salaries, wages, benefits in kind and other pay taxable as employment income. They must withhold, file the return and pay it over (art. 412 WIB 92; FOD Financiën, aangifte).
- **Employees** who are Belgian residents, and non-residents who work in Belgium under contracts covering the whole calendar year for at least 75% of normal working time. Both use the full formula with the tax-free amount and family reductions (key formula nr. 11).
- **Other non-residents** use the scale with no tax-free amount and no family reductions (key formula nr. 12). See `be-cross-border`.
- **Company directors (bedrijfsleiders)** under the self-employed social statute use the same formula with their own social deduction table and a 3% flat-rate expense (below).
- **Out of scope here:** pensions and unemployment benefits with company top-up (Part II and III of the key formula), which keep the January 2026 rules all year (KB of 27 September 2026, art. 10).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Employee social security deducted first | 13.07% of gross pay (blue-collar: of gross at 108%), less any social work bonus | 2026 | [RSZ instructions 2026/3](https://www.socialsecurity.be/employer/instructions/dmfa/nl/latest/instructions/socialsecuritycontributions/contributions.html); see `belgium-payroll` |
| Flat-rate professional expenses, employees | 30% of annual gross after social security, capped at EUR 6,070 (cap reached at EUR 20,233.33) | 2026 | [Key formula 2026, nr. 8](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/821b117c-eebc-497a-8297-ed2bb1e99d75) |
| Flat-rate professional expenses, directors | 3%, capped at EUR 3,200 (cap reached at EUR 106,666.67) | 2026 | Key formula 2026, nr. 8 |
| Withholding scale (annex 1) | 26.75% to EUR 16,710; EUR 4,469.93 + 42.80% to EUR 29,500; EUR 9,944.05 + 48.15% to EUR 51,050; EUR 20,320.38 + 53.50% above | 2026, whole year | [Key formula 2026, annex 1](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/821b117c-eebc-497a-8297-ed2bb1e99d75) |
| Tax on the tax-free amount, January to October | EUR 2,987.98 (26.75% of EUR 11,170); EUR 5,975.96 for a one-income couple | 2026 | Key formula 2026, nr. 11 |
| Tax on the tax-free amount, from 1 November | EUR 3,089.63 (26.75% of EUR 11,550); EUR 6,179.26 for a one-income couple | 2026 | [KB 27 September 2026, art. 2 and 4](https://www.ejustice.just.fgov.be/eli/besluit/2026/09/27/2026007167/staatsblad) |
| Marital quotient cap, January to October | 30% of annual net, at most EUR 13,790 | 2026 | Key formula 2026, nr. 11 b |
| Marital quotient cap, from 1 November | 30%, at most EUR 11,780; EUR 12,790 if both spouses are 66 by 1 January 2027 | 2026 | KB 27 September 2026, art. 3 |
| Children reduction (annual), January to October | 1: EUR 624; 2: 1,656; 3: 4,404; 4: 7,620; 5: 11,100; 6: 14,592; 7: 18,120; 8: 21,996; each extra: + 3,864 | 2026 | Key formula 2026, annex 3 |
| Children reduction (annual), from 1 November | 1: EUR 684; 2: 1,644; 3: 4,344; 4: 7,488; 5: 10,884; 6: 14,292; 7: 17,712; 8: 21,492; each extra: + 3,780 | 2026 | KB 27 September 2026, art. 5 |
| Single parent with dependent children | EUR 624 to October; EUR 636 from November | 2026 | Key formula annex 4; KB 27 September 2026, art. 7 |
| Employee is disabled | EUR 624 to October; EUR 648 from November | 2026 | Key formula annex 4 and 5; KB 27 September 2026, art. 6 |
| Other dependants (per person) | EUR 624 to October; EUR 636 from November | 2026 | Same |
| Dependants aged 66 or more needing care (per person) | EUR 1,992 all year | 2026 | Same |
| Spouse disabled (one-income couple) | EUR 624 to October; EUR 636 from November | 2026 | Key formula annex 5; KB 27 September 2026, art. 8 |
| Spouse with own earned income up to EUR 290 net a month | EUR 1,740 | 2026 | Key formula annex 4; KB 27 September 2026, art. 7 |
| Spouse with only pensions up to EUR 579 net a month | EUR 3,474 | 2026 | Same |
| Work bonus reduction (fiscal work bonus in withholding) | 33.14% of part A; part B 52.54% to 31 July, 63% from 1 August | 2026 | Key formula nr. 20; [KB 24 July 2026, art. 4 and 7](https://www.ejustice.just.fgov.be/eli/besluit/2026/07/24/2026005690/staatsblad) |
| Overtime reduction | 57.75% (50% or 100% premium hours) or 66.81% (20% premium hours) of the gross pay base, first 180 hours a year (360 in hotels, 280 in qualifying road and rail works) | 2026 | Key formula nr. 18; KB 24 July 2026, art. 2 and 7 |
| Group insurance and pension contributions withheld | 30% of the employee's contribution | 2026 | Key formula nr. 17 |
| Low-paid statutory public servants | EUR 7.50 a month if taxable pay is EUR 742.26 to 2,722.91 | 2026 | Key formula nr. 19 |
| Holiday pay and other exceptional pay | 0% to 53.50% by annual normal gross pay (table below) | 2026 | [Annex III 2026, nr. 53](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a38f6c59-3ab9-49d3-8844-d39f91387663) |
| Holiday pay paid by a holiday fund (blue-collar) | 17.16% of the whole amount if it is up to EUR 1,740; 23.22% of the whole amount if it is above | 2026 | Annex III 2026, nr. 69 |
| Quarterly payment threshold | Withholding on the previous year's income under EUR 51,480 | Income 2026 | [Art. 412 WIB 92](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/473ac660-d80e-4181-ab8e-e3544b57ffa8) |
| Late payment interest | 4% a year | Current | [FOD Financiën, betaling](https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/betaling); [art. 414](https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/db296af5-75b3-49bc-95e2-a35bb742fed5) |

The scale builds in a 7% increase for local surcharges (key formula nr. 5): 26.75%, 42.80%, 48.15% and 53.50% are 25%, 40%, 45% and 50% times 1.07. Its band limits (EUR 16,710, 29,500, 51,050) are not those of art. 130 WIB 92 for income 2026 (EUR 16,720, 29,510, 51,070), and the KB of 27 September 2026 did not change the scale. The final tax, with the commune's actual surcharge, is settled in the annual return (`be-employee-income-tax`).

Exceptional pay rates (Annex III 2026, nr. 53), by annual normal gross pay:

| Annual normal gross pay | Holiday pay | Other exceptional pay (13th month, bonuses) |
|---|---|---|
| Up to EUR 10,675 | 0% | 0% |
| 10,675.01 to 13,660 | 19.17% | 23.22% |
| 13,660.01 to 17,375 | 21.20% | 25.23% |
| 17,375.01 to 20,840 | 26.25% | 30.28% |
| 20,840.01 to 23,580 | 31.30% | 35.33% |
| 23,580.01 to 26,340 | 34.33% | 38.36% |
| 26,340.01 to 31,830 | 36.34% | 40.38% |
| 31,830.01 to 34,640 | 39.37% | 43.41% |
| 34,640.01 to 45,860 | 42.39% | 46.44% |
| 45,860.01 to 59,900 | 47.44% | 51.48% |
| Above 59,900 | 53.50% | 53.50% |

## The taxable base

The key formula has five steps (key formula nr. 6). Round every amount to the cent at each step (nr. 3).

1. **Annual gross.** Take the month's gross taxable pay, including benefits in kind, and deduct employee social security (13.07%, on gross at 108% for blue-collar workers, after any social work bonus). For directors under the self-employed statute, deduct instead EUR 385 up to EUR 1,465 a month, plus 21.5% of the slice to EUR 6,310, plus 14.5% of the slice to EUR 9,290, at most EUR 1,858.78 (nr. 7). Multiply by 12.
2. **Annual net.** Deduct the flat-rate professional expenses: 30% capped at EUR 6,070 for employees, 3% capped at EUR 3,200 for directors (nr. 8). Actual expenses play no role in withholding.
3. **Annual tax.**
   - Single person, or spouse with own earned income: apply the scale to the annual net, then deduct the tax on the tax-free amount (EUR 2,987.98 to October; EUR 3,089.63 from November) (nr. 11 a).
   - Spouse with no own earned income (or only pensions up to EUR 174 net a month): give the spouse 30% of the annual net, capped (EUR 13,790 to October; EUR 11,780 or 12,790 from November). Tax A is the scale on that slice. Tax B is the scale on the rest. Add them and deduct twice the tax on the tax-free amount (EUR 5,975.96 to October; EUR 6,179.26 from November) (nr. 11 b).
   - Deduct the reductions for children and other family charges (annexes 3 to 5). A disabled child counts as two. Reductions cannot take the tax below zero (nr. 13).
   - Non-residents who do not meet the 75% full-year test: scale only, no tax-free amount, no reductions (nr. 12).
4. **Monthly withholding.** Divide the annual tax by 12 (nr. 16).
5. **Other reductions,** in this order: 30% of group insurance and pension contributions withheld; overtime (not for overtime already exempt under art. 38, § 1, first paragraph, 29°/1 and 30° WIB 92); low-paid public servants; the work bonus (33.14% of part A, 63% of part B from 1 August 2026). The result cannot be negative (nrs. 17 to 21).

**Pay that is not monthly.** Fortnightly pay: after social security, multiply by 2 to get a month, run the five steps, divide the result by 2. Weekly: multiply by 4 and divide by 4. Per working day: multiply by 20 and divide by 20 (nr. 22).

**Holiday pay, 13th month and bonuses.** These are not run through the monthly formula. Apply the percentage from the table to the payment, chosen by the employee's annual normal gross pay (Annex III nr. 53). If the employee has dependent children and annual normal pay up to a limit (EUR 18,858 for one child to October; EUR 19,543 from November, under nr. 54 as amended by the KB of 27 September 2026, art. 9), part of the payment is exempt; up to five children also give a percentage reduction (nr. 55). End-of-year premiums paid in one go for piece or task work take a flat 16.15% (nr. 56). No withholding is due if one twelfth of normal annual pay plus the exceptional pay would not give rise to monthly withholding (nr. 57).

**Arrears** of pay for earlier years use a separate table by reference pay (Annex III nr. 58).

## Deadlines and filing

- **Who files:** every payer of income subject to withholding, online in FinProf ([FOD Financiën, aangifte](https://financien.belgium.be/nl/ondernemingen/personeel_en_loon/bedrijfsvoorheffing/aangifte)).
- **Monthly payers:** return and payment within 15 days after the end of the month in which the pay was paid or granted (art. 412, second paragraph). The FOD calendar shows the 2026 dates: 13 February (January), 13 March, 15 April, 13 May, 15 June, 15 July, 14 August, 15 September, 15 October, 13 November (October), 15 December (November), 15 January 2027 (December) ([FOD kalender](https://financien.belgium.be/nl/ondernemingen/personeel_en_loon/bedrijfsvoorheffing/kalender)).
- **Quarterly payers:** if withholding on the previous year's income was under EUR 51,480, return and payment are due within 15 days after each quarter: 15 April, 15 July, 15 October 2026 and 15 January 2027 (art. 412, third paragraph; FOD kalender).
- **Through a social secretariat:** accredited social secretariats pay the withholding they collect by the second-to-last working day of the month after the month or quarter of payment (FOD kalender).
- The return is a declaration of what was withheld; the payment must reach the account by the due date. The employee's annual statement and the year-end credit run through the annual return (`be-employee-income-tax`).

## Penalties and interest

- **Late payment interest** runs per calendar month at 4% a year on the unpaid amount rounded down to EUR 10, from the first day of the month after the due date. For withholding paid late, a further half month of interest is due for the month the payment fell due. Interest under EUR 5 a month is not charged (art. 414 WIB 92; FOD Financiën, betaling).
- **Administrative fines** of EUR 50 to EUR 1,250 per infringement apply to breaches of the Code and its decrees, such as a late or missing return. The scale is set by royal decree (art. 445, § 1 WIB 92).
- **Tax increases** of 10% to 200% apply where a return wrongly claims an exemption from paying over withholding (art. 444, second paragraph WIB 92).

## Cross-border points

- A non-resident employee working in Belgium for a full year under contracts covering at least 75% of normal working time is withheld like a resident. Other non-residents get no tax-free amount and no family reductions (key formula nr. 11 B and 12).
- Married people are withheld on as single (no marital quotient) if the spouse has earned income exempt under a treaty above a limit or, for non-residents, treaty-exempt or foreign earned income above that limit: EUR 13,790 a year to October (Annex III 2026, nr. 4.2). From 1 November 2026 the limit is EUR 11,550, and a study grant above EUR 11,550 that builds social security rights counts too (KB 27 September 2026, art. 1).
- Frontier workers, treaty exemptions, the inbound regime and which country taxes the pay: `be-cross-border`. Social security coordination (A1 certificates): `belgium-payroll` and `be-cross-border`.

## Worked examples

**Example 1. Single employee, gross EUR 4,000 a month, 2026.**

1. Employee social security: 13.07% x 4,000 = EUR 522.80. Taxable pay EUR 3,477.20. No work bonus at this pay (see `belgium-payroll`).
2. Annual gross: 3,477.20 x 12 = EUR 41,726.40.
3. Flat-rate expenses: 30% is above the cap, so EUR 6,070. Annual net EUR 35,656.40.
4. Scale: 9,944.05 + 48.15% x (35,656.40 - 29,500) = 9,944.05 + 2,964.31 = EUR 12,908.36.
5. January to October: less 2,987.98 gives EUR 9,920.38 a year; withholding 9,920.38 / 12 = **EUR 826.70 a month**.
6. From 1 November: less 3,089.63 gives EUR 9,818.73; withholding **EUR 818.23 a month**.

```oa-check
name: Single employee, EUR 4,000 gross a month, 2026 key formula
inputs:
  gross: 4000
steps:
  - ss: round(gross * 0.1307, 2)
  - annual: (gross - ss) * 12
  - expenses: min(round(annual * 0.30, 2), 6070)
  - net: annual - expenses
  - scale: 9944.05 + round((net - 29500) * 0.4815, 2)
  - monthly_jan_oct: round((scale - 2987.98) / 12, 2)
  - monthly_from_nov: round((scale - 3089.63) / 12, 2)
expected:
  ss: 522.80
  net: 35656.40
  scale: 12908.36
  monthly_jan_oct: 826.70
  monthly_from_nov: 818.23
```

**Example 2. Married, spouse has no income, two dependent children, gross EUR 4,000 a month, 2026.**

1. Steps 1 to 3 as in example 1: annual net EUR 35,656.40.
2. Marital quotient: 30% x 35,656.40 = EUR 10,696.92. This is under both caps (EUR 13,790 to October, EUR 11,780 from November), so it is the same all year.
3. Tax A: 26.75% x 10,696.92 = EUR 2,861.43.
4. Tax B on the rest, 35,656.40 - 10,696.92 = 24,959.48: 4,469.93 + 42.80% x (24,959.48 - 16,710) = 4,469.93 + 3,530.78 = EUR 8,000.71.
5. January to October: 2,861.43 + 8,000.71 - 5,975.96 = 4,886.18; less 1,656 for two children = 3,230.18; withholding **EUR 269.18 a month**.
6. From 1 November: 10,862.14 - 6,179.26 = 4,682.88; less 1,644 for two children = 3,038.88; withholding **EUR 253.24 a month**.

The quotient step below uses the November cap of EUR 11,780; the result is the same with the October cap of EUR 13,790 because 30% of the net is under both.

```oa-check
name: One-income couple, two children, EUR 4,000 gross a month, 2026 key formula
inputs:
  gross: 4000
  children_jan_oct: 1656
  children_from_nov: 1644
steps:
  - ss: round(gross * 0.1307, 2)
  - annual: (gross - ss) * 12
  - expenses: min(round(annual * 0.30, 2), 6070)
  - net: annual - expenses
  - quotient: min(round(net * 0.30, 2), 11780)
  - tax_a: round(quotient * 0.2675, 2)
  - rest: net - quotient
  - tax_b: 4469.93 + round((rest - 16710) * 0.428, 2)
  - monthly_jan_oct: round(max(tax_a + tax_b - 5975.96 - children_jan_oct, 0) / 12, 2)
  - monthly_from_nov: round(max(tax_a + tax_b - 6179.26 - children_from_nov, 0) / 12, 2)
expected:
  quotient: 10696.92
  tax_a: 2861.43
  tax_b: 8000.71
  monthly_jan_oct: 269.18
  monthly_from_nov: 253.24
```

## Ask the client first

1. When is the pay paid or granted? Pay from 1 November 2026 uses the new tax-free amount, quotient cap and family reductions.
2. Family situation on 1 January 2026: married or legal cohabitant, and does the spouse have earned income, pension only (and how much net a month), or none? Are both spouses 66 or older by 1 January 2027?
3. How many dependent children and other dependants, and is anyone disabled? Which spouse claims the children if both earn?
4. Is the person an employee or a company director under the self-employed statute?
5. Resident, or non-resident? If non-resident, does the Belgian work cover the full year at 75% or more of normal working time?
6. Does the person get a social work bonus, overtime with a legal premium, or group insurance contributions withheld from pay?

## Sources

| Source | URL | Read on |
|---|---|---|
| FOD Financiën, sleutelformule vanaf 1 januari 2026 (BEO-DR/2025-0928), FisconetPlus | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/821b117c-eebc-497a-8297-ed2bb1e99d75 | 2026-10-23 |
| Annex III KB/WIB 92, rules from 1 January 2026 (annex to KB 11 December 2025), FisconetPlus | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/a38f6c59-3ab9-49d3-8844-d39f91387663 | 2026-10-23 |
| KB 11 December 2025 amending the KB/WIB 92 on withholding, Belgisch Staatsblad 29 December 2025 (numac 2025009487) | https://www.ejustice.just.fgov.be/eli/besluit/2025/12/11/2025009487/staatsblad | 2026-10-23 |
| KB 24 July 2026 amending the withholding rules, Belgisch Staatsblad 30 July 2026 | https://www.ejustice.just.fgov.be/eli/besluit/2026/07/24/2026005690/staatsblad | 2026-10-23 |
| KB 27 September 2026 amending withholding, Belgisch Staatsblad 2 October 2026 | https://www.ejustice.just.fgov.be/eli/besluit/2026/09/27/2026007167/staatsblad | 2026-10-23 |
| FOD Financiën, bedrijfsvoorheffing berekenen (index of 2026 rules, key formula and simulators) | https://financien.belgium.be/nl/ondernemingen/personeel_en_loon/bedrijfsvoorheffing/berekening | 2026-10-23 |
| FOD Financiën, simulator bedrijfsvoorheffing 2026, version from 1 November 2026 | https://eservices.minfin.fgov.be/myminfin-rest/fisconetPlus/public/document/addenda/SimulatorBV2026novemberverrouille.xlsx | 2026-10-23 |
| FOD Financiën, aangifte bedrijfsvoorheffing | https://financien.belgium.be/nl/ondernemingen/personeel_en_loon/bedrijfsvoorheffing/aangifte | 2026-10-23 |
| FOD Financiën, kalender bedrijfsvoorheffing 2026 | https://financien.belgium.be/nl/ondernemingen/personeel_en_loon/bedrijfsvoorheffing/kalender | 2026-10-23 |
| WIB 92 art. 412 (income 2026), payment dates and quarterly threshold | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/473ac660-d80e-4181-ab8e-e3544b57ffa8 | 2026-10-23 |
| WIB 92 art. 414 (income 2026), late payment interest | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/db296af5-75b3-49bc-95e2-a35bb742fed5 | 2026-10-23 |
| WIB 92 art. 444 (income 2026), tax increases | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/5095859f-8ffb-42f9-b535-3197a7c3dbe0 | 2026-10-23 |
| WIB 92 art. 445 (income 2026), administrative fines | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f9f2e45e-5e3b-4642-a5e3-31ad4ca7f25f | 2026-10-23 |
| WIB 92 art. 130 (income 2026), tax scale | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/796a4fc5-340e-4c89-a72a-88caa804ca96 | 2026-10-23 |
| WIB 92 art. 131 (income 2026), tax-free amount | https://www.minfin.fgov.be/myminfin-web/pages/public/fisconet/document/f3c5d665-cac4-4cbd-b714-bd287f791751 | 2026-10-23 |
| FOD Financiën, vennootschapsbelasting betalen (late payment interest 4%) | https://financien.belgium.be/nl/ondernemingen/vennootschapsbelasting/betaling | 2026-10-23 |

Not yet confirmed: no consolidated key formula for the rules from 1 November 2026 was published at the date read; the November figures come from the KB of 27 September 2026 and the FOD simulator. The FOD aangifte page still gives the quarterly threshold as EUR 50,240 "in 2025"; the EUR 51,480 figure is the income 2026 text of art. 412. The form number of the withholding return (274) and the royal decree scale of fines under art. 445 were not read. The exceptional pay rates of nr. 53, 55 to 57 and 69 are from the January 2026 Annex III; the KB of 27 September 2026 changes only the nr. 54 limits. Annex III does not say in nr. 53 whether the rate is applied to the payment before or after employee social security; nr. 25.1 deducts social security only for monthly pay. The rule that an employer who fails to withhold stays liable was removed because no source was read. The work bonus amounts that feed step 5 are in `belgium-payroll`.
