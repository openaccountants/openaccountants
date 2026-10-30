---
name: sk-payroll-social
description: "Slovak payroll and social contributions for tax year 2026. Covers employee and employer social insurance (Sociálna poisťovňa, Act 461/2003) and public health insurance (Act 580/2004) at the 2026 rates, including the health rise to 5% employee, 11% employer and 16% self-employed; the EUR 16,764 social ceiling; self-employed (SZČO) contributions from the tax base with the 1.486 coefficient, the EUR 914.40 minimum and the new EUR 396.24 special base; monthly gross-to-net with the EUR 497.23 allowance, the 19/25/30/35% advance bands and the child tax bonus; monthly reports and payment dates; the annual tax and health reconciliations; and penalties. Trigger on 'Slovakia payroll', 'odvody 2026', 'SZČO odvody', 'gross to net Slovakia', 'ročné zúčtovanie', 'Sociálna poisťovňa', 'zdravotné poistenie 2026'. Out of scope: the annual personal return (slovakia-pit), companies (sk-corporate-income-tax), treaties and non-residents in depth (sk-cross-border), set-up (sk-company-formation)."
version: 0.2
jurisdiction: SK
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Slovakia payroll and social contributions, tax year 2026

> **Source-cited draft.** Built by Michael Cutajar and the OpenAccountants team from Act No. 461/2003 Coll. on social insurance, Act No. 580/2004 Coll. on health insurance, Act No. 595/2003 Coll. on income tax and Act No. 563/2009 Coll. (Tax Procedure Code), with Sociálna poisťovňa, VšZP and Financial Directorate pages, read on 2026-10-23. No accountant has reviewed it. Do not run a payroll from it without review by a qualified Slovak professional.

Tax year: the calendar year. Currency: euro. Three bodies collect from a payroll: Sociálna poisťovňa (social insurance), the employee's own health insurer (VšZP, Dôvera or Union, supervised by ÚDZS) and the tax office (Finančná správa) for the wage tax advance. Each has its own registration, report and due date.

See also: `slovakia-pit` (the annual return, other income, flat-rate expenses), `sk-corporate-income-tax`, `sk-cross-border` (treaties, non-residents), `sk-company-formation`.

## Who this applies to

**Employers.** Any person or company that pays an employee is a social insurance payer and deducts the employee's share (Act 461/2003 §§ 128, 141(2)). It is also a health insurance payer and computes and pays health advances for each employee (Act 580/2004 §16(2)(a), (c), (4)). An employer resident in Slovakia, or a foreign one with a Slovak branch, is the tax payer (platiteľ dane) and withholds the monthly tax advance (Act 595/2003 §35(1)).

**Employees.** People in an employment relationship (pracovný pomer) and people on work agreements (dohody). There is no minimum assessment base for an employee's social insurance: the base is the pay actually accounted (Act 461/2003 §138(1); Sociálna poisťovňa, 2026 tables, note 1). The employer must still pay at least the minimum wage under labour law: EUR 915 a month from 1 January 2026 ([Ministry of Labour, minimum wage 2026](https://www.employment.gov.sk/sk/uvodna-stranka/informacie-media/aktuality/historicky-narast-minimalnej-mzdy-je-realitou-roku-2026-je-minimalna-mzda-vo-vyske-915-eur.html)).

**Self-employed (SZČO).** From 1 January 2026 a person aged 18 or over is an SZČO for social insurance if they hold a licence to do business or, by an honest declaration, carry on self-employed work that needs no licence (for example an artist or author). Income no longer decides this status (Sociálna poisťovňa, changes from 1 January 2026, item 22).
- **New entrants** (no licence in the last 60 months) become compulsorily insured from the first day of the sixth calendar month after the month the licence starts.
- **Returning entrants** (a licence ended less than 60 months ago) are insured from the day the licence starts.
- Insurance now lasts until the licence ends. The old income test at 1 July no longer ends it.
- **Transition:** to 30 June 2026 an SZČO who held a licence before 1 January 2026 stays under the old rules. Under those rules insurance started on 1 July 2025 (1 October 2025 with an extended tax deadline) if 2024 income was above EUR 8,580 (Sociálna poisťovňa, 2026 tables, note 3).

Every SZČO pays health insurance advances from the start of the business (Act 580/2004 §16(2)(b), (8)(a)).

**Not covered here.** Voluntary insurance (dobrovoľne poistená osoba), the special scheme for municipal police, and health insurance on dividends. See `slovakia-pit` for an SZČO's annual return.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Employee social insurance: sickness 1.4%, old age 4%, disability 3%, unemployment 1% | 9.4% of gross pay | 2026 | [Sociálna poisťovňa, 2026 tables](https://www.socpoist.sk/socialne-poistenie/platenie-poistneho/tabulky-platenia-poistneho/tabulky-platenia-poistneho-od-1-6?ref=2435); Act 461/2003 §§ 130 to 136 |
| Employer social insurance: sickness 1.4%, old age 14%, disability 3%, unemployment 0.5%, short-time support 0.5%, guarantee 0.25%, solidarity reserve 4.75% | 24.4% of gross pay, capped | 2026 | Sociálna poisťovňa, 2026 tables; Act 461/2003 §§ 130 to 137 |
| Employer accident insurance | 0.8%, no cap | 2026 | Act 461/2003 § 133, §138(10) |
| Employer unemployment rate where it pays no short-time support contribution (work agreements) | 1% instead of 0.5% + 0.5% | 2026 | Act 461/2003 §128(1)(g), §136(b) |
| Second pillar (II. pilier) saver | 4% of the employer's 14% old-age rate goes to the saver's pension fund; the total rate is unchanged | 2026 | Act 461/2003 §131(2); Sociálna poisťovňa, changes from 1 January 2026, item 13 |
| Maximum monthly social assessment base (11 x EUR 1,524 average monthly wage for 2024) | EUR 16,764 | 2026 | Sociálna poisťovňa, 2026 tables, note 2; Act 461/2003 §138(9), (10) |
| Maximum monthly social insurance | Employee EUR 1,575.81; employer EUR 4,090.41 plus 0.8% accident on the full pay | 2026 | Sociálna poisťovňa, 2026 tables |
| Health insurance, employee | 5% (2.5% for a person with a disability), no cap | 2026 | [Act 580/2004](https://static.slov-lex.sk/static/SK/ZZ/2004/580/20260701.html) §12(1)(a); [VšZP, changes from 1 January 2026](https://www.vszp.sk/platitelia/platenie-poistneho/oznamenia-zmeny/zmeny-od-01-01.2026/) |
| Health insurance, employer | 11% (5.5% for an employee with a disability), no cap, for 2026 and 2027 | 2026 | Act 580/2004 §38ezk(c) |
| Health insurance, SZČO | 16% (8% with a disability), for 2026 and 2027 | 2026 | Act 580/2004 §38ezk(b); VšZP, changes from 1 January 2026 |
| Minimum monthly health advance, SZČO (16% of 50% of EUR 1,524) | EUR 121.92 (EUR 60.96 with a disability); set by the Act, so the same at every insurer | 2026 | VšZP, changes from 1 January 2026; Act 580/2004 §13(10), §16(8)(a) |
| Minimum monthly health advance per employee (5% + 11% of the subsistence minimum of EUR 284.13, each rounded down) | EUR 45.45 (employee EUR 14.20 + employer EUR 31.25); set by the Act, so the same at every insurer | 2026 | VšZP, changes from 1 January 2026; Act 580/2004 §16a, §16(1) |
| Health deductible amount for a low-paid employee who claims it | Up to EUR 380 a month, zero from EUR 570 of pay; up to EUR 4,560 a year in the reconciliation | 2026 | Act 580/2004 §16(16) to (18), §13a; [VšZP, odpočítateľná položka](https://www.vszp.sk/platitelia/platenie-poistneho/odpocitatelna-polozka/) |
| SZČO social insurance: sickness 4.4%, old age 18%, disability 6%, solidarity reserve 4.75% | 33.15% of the assessment base | 2026 | Sociálna poisťovňa, 2026 tables; Act 461/2003 §§ 130 to 132, 137 |
| SZČO minimum social base (60% of EUR 1,524) and payment | EUR 914.40; EUR 303.11 a month | 2026 | Sociálna poisťovňa, 2026 tables, note 1; Act 461/2003 §138(8) |
| SZČO special base (26% of EUR 1,524) and payment, for new entrants and SZČO with prior-year income up to EUR 9,144 | EUR 396.24; EUR 131.34 a month | 2026 | [Sociálna poisťovňa, changes from 1 January 2026, item 22](https://www.socpoist.sk/socialne-poistenie/zmeny-v-socialnom-poisteni/najdolezitejsie-zmeny-v-socialnom-poisteni-od-1-1?ref=2441); Act 461/2003 §138(2)(b) |
| SZČO maximum social payment | EUR 5,557.26 a month | 2026 | Sociálna poisťovňa, 2026 tables |
| SZČO income test for the 1.486 base | Income (not profit) above EUR 9,144 (50% of the 2024 general assessment base) | 2026 | Sociálna poisťovňa, changes from 1 January 2026, item 22; Act 461/2003 §138(2)(a) |
| Work agreement deduction (dohoda) for a student or pensioner who claims it | EUR 200 a month off the social base | 2026 | Act 461/2003 §138a |
| Personal allowance (NČZD), annual and monthly | EUR 5,966.73 and EUR 497.23 (21 x EUR 284.13); tapers above an annual tax base of EUR 26,083.13 | 2026 | [Financial Directorate, 31/DZPaU/2025/I](https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Dane/Novinky_leg/Priame_dane_uct/2025/2025.10.17_031_DZPaU_2025_I.pdf); [Act 595/2003](https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html) §11(2), §35(1)(b) |
| Annual tax bands on employment income | 19% to EUR 43,983.32; 25% to EUR 60,349.21; 30% to EUR 75,010.32; 35% above | 2026 | Financial Directorate, 31/DZPaU/2025/I; Act 595/2003 §15(a)(1) |
| Monthly advance bands | 19% to EUR 3,665.28; 25% to EUR 5,029.10; 30% to EUR 6,250.86; 35% above | 2026 | Financial Directorate, 31/DZPaU/2025/I; Act 595/2003 §35(2) |
| Child tax bonus | EUR 100 a month per child under 15; EUR 50 from 15 to 18 | 2026 | Financial Directorate, 31/DZPaU/2025/I; Act 595/2003 §33(1) |
| Tax bonus cap as a share of the employment tax base | 29% (1 child), 36% (2), 43% (3), 50% (4), 57% (5), 64% (6 or more) | 2026 | Act 595/2003 §33(6) |
| Tax bonus taper | Each child's bonus falls by 1/10 of the tax base above EUR 27,432 a year (1.5 x 12 x EUR 1,524, the 2024 average wage). In payroll the employer applies it to the month's base above EUR 2,286 (1/12) | 2026 | Act 595/2003 §33(11), §35(5); [Financial Directorate, tax bonus in 2026, question 5](https://podpora.financnasprava.sk/549090-Da%C5%88ov%C3%BD-bonus-na-vy%C5%BEivovan%C3%A9-die%C5%A5a-v-roku-2026) |

**Rounding.** Social insurance: each assessment base and each separate contribution is rounded down to the cent (Act 461/2003 §138(14); 2026 tables, closing note). Health: bases and advances are rounded down to the cent (Act 580/2004 §13(17), §16(1)). Income tax: amounts are rounded half up to two decimals (Act 595/2003 §47).

## The taxable base

**Employee social base.** Pay from the work, except income that is not taxable or is exempt from income tax, and except employer contributions to supplementary pension saving (Act 461/2003 §138(1)). A profit share paid to an employee who holds no capital is included. The base is capped at EUR 16,764 a month; employer accident insurance runs on the full pay (§138(10)). From 2026 the employee and employer pay social insurance on any pay accounted during sickness, maternity or care leave. The old exclusion periods are gone for employees (Sociálna poisťovňa, changes from 1 January 2026, item 26). Where someone has several jobs, social contributions run from the highest base down (§138(12)).

**Employee health base.** The same employment income, with no ceiling (Act 580/2004 §13(1); VšZP, employer page). The employer's 11% runs on the gross before any deductible amount (§13(4), §16(2)(c)). The total employee and employer health advance must be at least EUR 45.45 for a full month; any shortfall is added to the employee's share (§16a).

**Wage tax advance.** Taxable wage = gross taxable pay less the employee's social and health contributions, less EUR 497.23 if the employee has signed the declaration (vyhlásenie) with this employer (Act 595/2003 §35(1), (4), §36(6)). Only one employer may hold that declaration. The spouse allowance and pension savings deductions wait for the annual reconciliation (§35(1)(b)). Apply the monthly bands to the taxable wage, then reduce the advance by the child tax bonus (§35(2), (5)).

**Child tax bonus in payroll.** Granted only by the employer holding the declaration. It is capped at the §33(6) share of the month's employment tax base (gross less employee contributions), and the §33(11) taper applies to that monthly base (§35(5)). If the bonus exceeds the advance, the employer pays the difference from the tax it withheld for all staff. If that is not enough, it pays from its own money and claims the balance from the tax office after the quarter (§35(7)).

**Net pay** = gross − employee social − employee health − tax advance after bonus. **Employer cost** = gross + employer social (with accident) + employer health.

**SZČO social base** (Act 461/2003 §138(2)):
1. If last year's income from business (not profit) was above EUR 9,144: take the business tax base from the tax return, before deducting the social and health contributions paid. Divide it by 12, then by 1.486, and round down to the cent. The result is at least EUR 914.40 and at most EUR 16,764. It applies from 1 July of the year after the income year to 30 June of the next year, or from 1 October to 30 September with an extended tax deadline.
2. Otherwise, and for a new entrant, the special base of EUR 396.24 applies.

Each component (4.4%, 18%, 6%, 4.75%) is rounded down separately.

**SZČO health advance.** 16% of the business tax base from two years earlier (2024 for 2026), taken before contributions paid, divided by the months of business in that year and by 1.486. The advance is at least EUR 121.92 (Act 580/2004 §16(2)(b), (3), (8)(a)). The insurer states the amount in the annual reconciliation. An SZČO who is also an employee pays their own SZČO advance, with no minimum (§16(6), (8)(e)).

## Deadlines and filing

| Obligation | When | Source |
|---|---|---|
| Employer registers with Sociálna poisťovňa | At the latest the day before it starts employing the first employee | Act 461/2003 §231(1)(a) |
| Register each employee for social insurance | Before the employee starts work; deregister within 8 days | Act 461/2003 §231(1)(b) |
| Employer registers as a health insurance payer; reports each employee start and end | Within 8 working days | [VšZP, employer page](https://www.vszp.sk/platitelia/platenie-poistneho/zamestnavatel/) |
| Employer social insurance payment and monthly report (výkaz poistného) | On the payday set for the month's pay; if none is set, the last day of the next month; a weekend or holiday moves it to the next working day | Act 461/2003 §143(2), §231(1)(g) |
| Employer health advances | On the payday for the month's pay; if none is set, the last day of the next month | Act 580/2004 §17(1) |
| Employer health monthly report (dávka 514), electronic | Within 3 days of the advance due date | Act 580/2004 §20(1), (6); Ministry of Health Decree 159/2018 §2(2); VšZP, employer page |
| Wage tax advance remitted | Within 5 days after the payday | Act 595/2003 §35(6) |
| Monthly tax summary (Prehľad) | By the end of the next month | Act 595/2003 §39(9)(a), §49(2) |
| SZČO social insurance | By the 8th of the next month (January 2026 was due 9 February 2026) | Act 461/2003 §143(1); Sociálna poisťovňa, changes from 1 January 2026, item 23 |
| SZČO health advance | By the 8th day after the month ends | Act 580/2004 §17(2) |
| Employee asks the employer for the tax reconciliation (ročné zúčtovanie) and hands in documents | By 15 February 2027 for 2026 | Act 595/2003 §38(1), (5) |
| Employer completes the tax reconciliation | By 31 March 2027; any refund paid at the latest with April 2027 pay; an underpayment above EUR 5 is deducted from pay by the end of 2027 | Act 595/2003 §38(6), (7) |
| Annual tax report (Hlásenie) | By 30 April 2027 | Act 595/2003 §39(9)(b), §49(2) |
| Health insurance annual reconciliation (ročné zúčtovanie poistného) for 2026 | The insurer completes it by 30 September 2027 (31 October with an extended tax deadline); an underpayment is paid within 45 days of the statement becoming final | Act 580/2004 §19(2), (15); §38ezl(3) |

Social insurance has no annual reconciliation for employees: each month is final when paid. An employee with other taxable income, or one who does not ask for the reconciliation, files the annual return instead. See `slovakia-pit`.

## Penalties and interest

| Failure | Consequence | Source |
|---|---|---|
| Social insurance paid late or short | Penalty (penále) of 0.05% of the unpaid amount per day from the due date. It cannot exceed the unpaid amount for the checked period, and is not charged if EUR 5 or less | Act 461/2003 §240 |
| Social insurance reporting duties (registrations, monthly report, notices) | Fine up to EUR 16,596.96; none if the duty is met within 7 days of the deadline | Act 461/2003 §239 |
| Health advance paid late | Interest of 4 x the ECB main rate on the due date, at least 15% a year, per day | Act 580/2004 §18(1) |
| Health payer duties under §24 not met | ÚDZS fine up to EUR 3,319 per breach, doubled for a repeat within two years | Act 580/2004 §26(1)(c), (3) |
| Wage tax advance paid late | Interest of 4 x the ECB main rate, at least 15% a year, per day, for at most four years | Act 563/2009 §156(1)(d), (2) |
| Monthly Prehľad not filed within 5 days after its deadline, in a month with advances to pay or a bonus claimed | The tax office applies the Tax Procedure Code fines and late-payment interest | Act 595/2003 §39(11); Act 563/2009 §§ 155, 156 |
| Employer does not do a tax reconciliation that an employee validly asked for | Fine of at least EUR 15 per employee, at most EUR 30,000 in total for the year | Act 595/2003 §38(9) |
| Hlásenie filed late (it counts as a tax return) | Fine EUR 100 to 30,000; a range fine is not imposed on a first breach | Act 595/2003 §39(11); Act 563/2009 §154(1)(a), §155(1)(a), (4) |
| Tax understated in a return or Hlásenie, found by the tax office | 3 x the ECB main rate a year, at least 10%, on the extra tax | Act 563/2009 §155(1)(f), (5) |

## Cross-border points

- **EU coordination.** Within the EU, EEA and Switzerland a person is subject to one country's social security law at a time (Regulation 883/2004 Art. 11(1)). A worker posted from Slovakia for work expected to last up to 24 months stays under Slovak law (Art. 12(1)) and carries an A1 form issued by Sociálna poisťovňa. A worker posted to Slovakia with a foreign A1 pays no Slovak social insurance.
- **Foreign employer.** A foreign employer with no Slovak branch is not the tax payer. A resident employee pays the tax advances themselves by the end of the next month (Act 595/2003 §35(10)). A non-resident does the same under §35(11), from the start of the stay if the contract shows more than 183 days.
- **Pay taxed abroad.** The employer withholds no advance on pay that is taxed abroad (Act 595/2003 §35(8)). The tax bonus needs at least 90% of total income from Slovak sources (§33(9)). Treaty conditions and documents are in `sk-cross-border`.

## Worked examples

### Example 1: employee, EUR 2,500 a month, one child aged 10

Jana works full time under an employment contract. Her gross pay is EUR 2,500 a month. She signed the declaration with this employer, has one child aged 10, no disability, and earns nothing else.

Her pay is below EUR 16,764, so the social base is EUR 2,500. Employee social is 9.4% = EUR 235.00. Employee health is 5% = EUR 125.00. The taxable wage is 2,500 − 360 − 497.23 = EUR 1,642.77. That is below EUR 3,665.28, so the advance is 19% = EUR 312.13. The child bonus of EUR 100 is below the cap of 29% of EUR 2,140 (EUR 620.60). Her monthly base is below the EUR 2,286 taper point (EUR 27,432 / 12), so the bonus is not reduced. The advance falls to EUR 212.13. Net pay is EUR 1,927.87.

The employer pays 24.4% social (EUR 610.00), 0.8% accident (EUR 20.00) and 11% health (EUR 275.00). Employer cost is EUR 3,405.00. Sociálna poisťovňa receives EUR 865.00 on payday, the health insurer EUR 400.00, and the tax office EUR 212.13 within 5 days.

```oa-check
name: Jana, EUR 2,500 gross, one child under 15, declaration signed (2026)
inputs:
  gross: 2500
  social_cap: 16764
  allowance_month: 497.23
  band_19_month: 3665.28
  bonus_child: 100
  taper_month: 2286
steps:
  - base: min(gross, social_cap)
  - ee_social: floor(base * 1.4) / 100 + floor(base * 4) / 100 + floor(base * 3) / 100 + floor(base * 1) / 100
  - ee_health: floor(gross * 5) / 100
  - tax_base_month: gross - ee_social - ee_health
  - taxable_wage: tax_base_month - allowance_month
  - advance: round(min(taxable_wage, band_19_month) * 0.19 + max(taxable_wage - band_19_month, 0) * 0.25, 2)
  - bonus_cap: round(tax_base_month * 0.29, 2)
  - bonus: min(max(bonus_child - max(tax_base_month - taper_month, 0) / 10, 0), bonus_cap)
  - advance_after_bonus: advance - bonus
  - net_pay: gross - ee_social - ee_health - advance_after_bonus
  - er_social: floor(base * 1.4) / 100 + floor(base * 14) / 100 + floor(base * 3) / 100 + floor(base * 0.5) / 100 + floor(base * 0.5) / 100 + floor(base * 0.25) / 100 + floor(base * 4.75) / 100
  - er_accident: floor(gross * 0.8) / 100
  - er_health: floor(gross * 11) / 100
  - employer_cost: gross + er_social + er_accident + er_health
  - to_social_insurer: ee_social + er_social + er_accident
expected:
  ee_social: 235.00
  ee_health: 125.00
  advance: 312.13
  advance_after_bonus: 212.13
  net_pay: 1927.87
  er_social: 610.00
  employer_cost: 3405.00
  to_social_insurer: 865.00
```

### Example 2: self-employed (SZČO) contributions from July 2026

Peter has been self-employed for years. His 2025 return shows business income of EUR 48,000 and a tax base of EUR 21,000, after deducting EUR 7,500 of social and health contributions he paid in 2025. His 2024 return showed a tax base of EUR 24,000 before contributions, for 12 months of business. He has no extended filing deadline and no disability.

His 2025 income is above EUR 9,144, so the 1.486 method applies. The tax base before contributions is 21,000 + 7,500 = EUR 28,500. That gives 28,500 / 12 = EUR 2,375, and 2,375 / 1.486 = EUR 1,598.25 (rounded down). This is between EUR 914.40 and EUR 16,764. From July 2026 to June 2027 he pays EUR 70.32 sickness, EUR 287.68 old age, EUR 95.89 disability and EUR 75.91 reserve fund: EUR 529.80 a month, each due by the 8th of the next month.

His 2026 health advance uses 2024: 24,000 / 12 / 1.486 = EUR 1,345.89, and 16% gives EUR 215.34 a month. That is above the EUR 121.92 minimum.

The edge case: if his 2025 income had been EUR 9,144 or less, he would pay on the EUR 396.24 special base, EUR 131.34 a month, not on the EUR 914.40 minimum.

```oa-check
name: Peter, SZCO, 2025 tax base 21,000 plus 7,500 contributions, social from July 2026
inputs:
  income_2025: 48000
  tax_base_2025: 21000
  contributions_deducted_2025: 7500
  tax_base_2024_before_contributions: 24000
  months_2024: 12
  min_base: 914.40
  max_base: 16764
  special_base: 396.24
steps:
  - base_raw: floor((tax_base_2025 + contributions_deducted_2025) / 12 / 1.486 * 100) / 100
  - social_base: clamp(base_raw, min_base, max_base)
  - sickness: floor(social_base * 4.4) / 100
  - old_age: floor(social_base * 18) / 100
  - disability: floor(social_base * 6) / 100
  - reserve: floor(social_base * 4.75) / 100
  - social_month: sickness + old_age + disability + reserve
  - health_base: floor(tax_base_2024_before_contributions / months_2024 / 1.486 * 100) / 100
  - health_advance: max(floor(health_base * 16) / 100, 121.92)
  - special_month: floor(special_base * 4.4) / 100 + floor(special_base * 18) / 100 + floor(special_base * 6) / 100 + floor(special_base * 4.75) / 100
expected:
  social_base: 1598.25
  social_month: 529.80
  health_base: 1345.89
  health_advance: 215.34
  special_month: 131.34
```

## Ask the client first

1. **Contract type for each worker.** Employment contract, work agreement (dohoda) or self-employed. This changes the unemployment and support rates, the EUR 200 deduction and the health deductible amount.
2. **Has the employee signed the tax declaration with you, and which children (with ages) are claimed?** Only one employer gives the EUR 497.23 allowance and the tax bonus.
3. **Disability, pension or second-pillar status.** Disability halves the health rates; a pensioner pays no disability or unemployment insurance; a saver's 4% goes to the pension fund.
4. **Your payday.** Social and health payments fall due on it; the tax advance 5 days later.
5. **For an SZČO: the date the licence started, any licence that ended in the last 60 months, the last two returns (income, tax base, contributions deducted) and any extended filing deadline.** These set the start date and both bases.
6. **Any work abroad, A1 form or foreign employer.** This changes who collects.

## Sources

| Source | URL | Read on |
|---|---|---|
| Act No. 461/2003 Coll. on social insurance, version from 1 September 2026, §§ 128 to 143, 231, 239, 240 | https://static.slov-lex.sk/static/SK/ZZ/2003/461/20260901.html | 2026-10-23 |
| Act No. 580/2004 Coll. on health insurance, version from 1 July 2026, §§ 12, 13, 13a, 16 to 20, 26, 38ezk, 38ezl | https://static.slov-lex.sk/static/SK/ZZ/2004/580/20260701.html | 2026-10-23 |
| Act No. 595/2003 Coll. on income tax, version from 1 January 2026, §§ 11, 15, 33, 35, 38, 39, 47, 49 | https://static.slov-lex.sk/static/SK/ZZ/2003/595/20260101.html | 2026-10-23 |
| Act No. 563/2009 Coll., Tax Procedure Code, version from 1 September 2026, §§ 154 to 156 | https://static.slov-lex.sk/static/SK/ZZ/2009/563/20260901.html | 2026-10-23 |
| Sociálna poisťovňa, contribution tables from 1 January 2026 | https://www.socpoist.sk/socialne-poistenie/platenie-poistneho/tabulky-platenia-poistneho/tabulky-platenia-poistneho-od-1-6?ref=2435 | 2026-10-23 |
| Sociálna poisťovňa, main changes in social insurance from 1 January 2026 (items 9, 13, 22 to 26) | https://www.socpoist.sk/socialne-poistenie/zmeny-v-socialnom-poisteni/najdolezitejsie-zmeny-v-socialnom-poisteni-od-1-1?ref=2441 | 2026-10-23 |
| VšZP, changes from 1 January 2026 (rates, minimum advances) | https://www.vszp.sk/platitelia/platenie-poistneho/oznamenia-zmeny/zmeny-od-01-01.2026/ | 2026-10-23 |
| VšZP, employer obligations | https://www.vszp.sk/platitelia/platenie-poistneho/zamestnavatel/ | 2026-10-23 |
| VšZP, self-employed obligations | https://www.vszp.sk/platitelia/platenie-poistneho/samostatne-zarobkovo-cinna-osoba/ | 2026-10-23 |
| VšZP, deductible amount (odpočítateľná položka) | https://www.vszp.sk/platitelia/platenie-poistneho/odpocitatelna-polozka/ | 2026-10-23 |
| Financial Directorate, tax bonus on a dependent child in 2026 (podpora page; live site returned 503, read through the Wayback Machine copy of 15 October 2026) | https://podpora.financnasprava.sk/549090-Da%C5%88ov%C3%BD-bonus-na-vy%C5%BEivovan%C3%A9-die%C5%A5a-v-roku-2026 | 2026-10-24 |
| Ministry of Health Decree No. 159/2018 Coll. on reporting health insurance advances, version from 1 July 2025, §2(2) | https://static.slov-lex.sk/static/SK/ZZ/2018/159/20250701.html | 2026-10-24 |
| Ministry of Labour, minimum wage for 2026 | https://www.employment.gov.sk/sk/uvodna-stranka/informacie-media/aktuality/historicky-narast-minimalnej-mzdy-je-realitou-roku-2026-je-minimalna-mzda-vo-vyske-915-eur.html | 2026-10-24 |
| Regulation (EC) No 883/2004, consolidated 31 July 2019, Art. 11 and 12 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:02004R0883-20190731 | 2026-10-24 |
| Financial Directorate, 31/DZPaU/2025/I, amounts for individuals' tax for 2026 | https://www.financnasprava.sk/_img/pfsedit/Dokumenty_PFS/Zverejnovanie_dok/Dane/Novinky_leg/Priame_dane_uct/2025/2025.10.17_031_DZPaU_2025_I.pdf | 2026-10-23 |

Not yet confirmed: which fine band in Act 563/2009 §155 the tax office uses for a late monthly Prehľad (Act 595/2003 §39(11) points to §§ 155 and 156 without naming a band); the rule that Sociálna poisťovňa issues the A1 form rests on Regulation 987/2009 Art. 19(2), which was not read.

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
