---
name: pl-payroll
description: "Polish payroll for employees (umowa o pracę) for tax year 2026: monthly PIT advances under PIT Act art. 31a-32 and 38 (12% and 32% with the PLN 120,000 threshold per payer, standard costs PLN 250 or 300, the PIT-2 reduction of PLN 300 a month), the PLN 85,528 reliefs for under-26s, returners, parents of four and working seniors, employee and employer ZUS contributions (19.52%, 8%, 2.45%, accident 1.67% for small payers, FP and Solidarity Fund 2.45%, FGŚP 0.10%, FEP 1.5%) with the PLN 282,600 annual cap, 9% health contribution, PPK, the PLN 4,806 minimum wage, ZUS DRA and PIT-4R and PIT-11 deadlines, and penalties. Trigger on: wynagrodzenie netto, zaliczka na PIT pracownika, składki ZUS pracodawcy, PIT-11, PIT-4R, koszt pracodawcy. Out of scope: self-employed ZUS in pl-zus-contributions; annual return and business income in pl-income-tax; company tax in pl-cit-corporate-tax."
jurisdiction: PL
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Poland: payroll for employees (2026)

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any specific employer's or employee's facts. Do not rely on it to run a payroll, file or pay without review by a qualified professional in Poland.

**Which text of the law.** PIT Act (ustawa z dnia 26 lipca 1991 r. o podatku dochodowym od osób fizycznych), consolidated text Dz.U. 2026 poz. 592; the later amendments (poz. 779, 846, 1079) do not touch the payroll articles used here. Social Insurance System Act (ustawa z dnia 13 października 1998 r. o systemie ubezpieczeń społecznych, "ZUS Act"), consolidated text Dz.U. 2026 poz. 199. Health Care Benefits Act (ustawa o świadczeniach opieki zdrowotnej finansowanych ze środków publicznych), consolidated text Dz.U. 2025 poz. 1461. Fund rates for 2026 come from the 2026 Budget Act, Dz.U. 2026 poz. 62.

**Sibling skills.** Residence, the annual PIT return, joint filing and business income: [pl-income-tax](pl-income-tax.md). ZUS for the self-employed (including Mały ZUS Plus): [pl-zus-contributions](pl-zus-contributions.md). Deductibility of salary costs for a company and withholding tax on payments abroad: [pl-cit-corporate-tax](pl-cit-corporate-tax.md). Pricing of staff recharges between related companies: [pl-transfer-pricing](pl-transfer-pricing.md). This skill does not repeat them.

## Who this applies to

**The employer as payer (PIT Act art. 32(1)).** Every employer (individual, company or other unit) that pays salary under an employment relationship (stosunek pracy), a service relationship, outwork or a cooperative employment relationship must compute, withhold and pay monthly PIT advances (zaliczki).

**The employer as ZUS payer (ZUS Act art. 16-17).** The same employer computes the social contributions, deducts the employee's share from pay, adds its own share and pays the total to ZUS. It also deducts and pays the employee's health contribution (Health Act art. 85(1)).

**Covered here:** employees on an employment contract, resident or not, paid by a Polish employer.

**Not covered here:** civil-law contracts (umowa zlecenie, umowa o dzieło), which use art. 41 of the PIT Act and 20% costs (art. 22(9)(4)); board members' fees; the self-employed (see pl-zus-contributions); directors' fees paid to non-residents (see pl-cit-corporate-tax).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| PIT scale, first band | 12% up to PLN 120,000, minus the tax-reducing amount PLN 3,600 | 2026 | PIT Act art. 27(1), https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000592 |
| PIT scale, second band | PLN 10,800 + 32% of the excess over PLN 120,000 | 2026 | PIT Act art. 27(1) |
| Tax-free amount (effect of the PLN 3,600 reduction) | PLN 30,000 a year (3,600 / 12%) | 2026 | PIT Act art. 27(1) |
| Monthly advance rate | 12% until cumulative income from this payer exceeds PLN 120,000; split in the crossing month; 32% after | 2026 | PIT Act art. 32(2) |
| Monthly reduction with PIT-2 statement | 1/12 of PLN 3,600 = PLN 300 (or 1/24 or 1/36 if split across up to three payers) | 2026 | PIT Act art. 31b(1)-(3) |
| Standard employee costs (KUP), one job | PLN 250 a month, max PLN 3,000 a year | 2026 | PIT Act art. 22(2)(1) |
| Standard costs, commuter from another town | PLN 300 a month, max PLN 3,600 a year | 2026 | PIT Act art. 22(2)(3) |
| Standard costs, several jobs | max PLN 4,500 a year (PLN 5,400 for commuters) | 2026 | PIT Act art. 22(2)(2) and (4) |
| Author's costs (creative work) | 50% of revenue after employee social contributions; with exempt revenue, capped at PLN 120,000 a year in total | 2026 | PIT Act art. 22(9)(3), 22(9a), 22(9aa) |
| Reliefs: under 26, relocation to Poland, parents of 4+ children, working seniors | exempt revenue, PLN 85,528 a year in total for all four | 2026 | PIT Act art. 21(1)(148), (152)-(154), 21(44) |
| Pension insurance (emerytalne) | 19.52%: 9.76% employee, 9.76% employer | 2026 | ZUS Act art. 22(1)(1), 16(1), https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000199 |
| Disability insurance (rentowe) | 8%: 1.5% employee, 6.5% employer | 2026 | ZUS Act art. 22(1)(2), 16(1b) |
| Sickness insurance (chorobowe) | 2.45%, all employee | 2026 | ZUS Act art. 22(1)(3), 16(2) |
| Accident insurance (wypadkowe) | 0.40% to 8.12% range in the Act; payers with 9 or fewer insured: 50% of the highest group rate, 1.67%; all employer | 2026 | ZUS Act art. 22(1)(4), 16(3); Accident Insurance Act art. 28(1), https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20250001644; ZUS, https://www.zus.pl/baza-wiedzy/skladki-wskazniki-odsetki/skladki/wysokosc-skladek-na-ubezpieczenia-spoleczne |
| Accident rates by activity group (10 or more insured) | group rates from Annex 2 (0.67% to 3.33%), times the payer's correction factor | 2026 | Regulation on accident rates, Dz.U. 2025 poz. 1874, https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20250001874 |
| Annual cap on pension and disability base (30 x forecast average wage) | PLN 282,600 (average wage PLN 9,420) | 2026 | ZUS Act art. 19(1); M.P. 2025 poz. 1206, https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WMP20250001206 |
| Labour Fund (FP) + Solidarity Fund (FS) | 1.0% + 1.45% = 2.45%, employer; base not capped | 2026 | Budget Act 2026 art. 25-26, https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000062; Labour Market Act art. 259(1), 261-263, https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20250000620; Solidarity Fund Act art. 4(1), https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20240001848 |
| Guaranteed Employee Benefits Fund (FGŚP) | 0.10%, employer that is a business (przedsiębiorca); base not capped | 2026 | Budget Act 2026 art. 27; Employee Claims Act art. 9, 9a-9c, 29(1), https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000186 |
| Bridging Pension Fund (FEP) | 1.5%, employer, only for work in special conditions or of a special nature; base is the pension base under ZUS Act art. 18 and 21, with no reference to the art. 19 cap | 2026 | Bridging Pensions Act art. 35-36, https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20240001696 |
| Health contribution (zdrowotna) | 9% of gross pay less employee social contributions; no annual cap; employee pays; not deductible from PIT | 2026 | Health Act art. 79(1), 81(1), (5) and (6), https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20250001461 |
| PPK basic payments | employee 2% (0.5% to 2% if pay is up to 1.2 x minimum wage), employer 1.5%; extras up to 2% and 2.5% | 2026 | PPK Act art. 26-27, https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000192 |
| Minimum wage | PLN 4,806 a month; PLN 31.40 an hour | 2026 | Dz.U. 2025 poz. 1242, https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20250001242 |
| Late payment interest (tax and ZUS) | 200% of the NBP lombard rate + 2 points, at least 8% a year; 10.50% a year from 5 March 2026 (lombard rate 4.25%) | 2026 | Tax Ordinance art. 56 § 1, https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000622; ZUS Act art. 23(1); M.P. 2026 poz. 269, https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WMP20260000269 |

## The taxable base

**Social contributions.** The base for pension, disability, sickness and accident insurance is the employee's gross pay (ZUS Act art. 18(1)). Pension and disability stop once the year's base passes PLN 282,600; the employer stops computing them from that point (art. 19(1), (3) and (5)). Sickness and accident have no cap. FP, FS and FGŚP use the pension base **without** the cap (Labour Market Act art. 259(1); Employee Claims Act art. 29(1)). FS follows the FP rules (Solidarity Fund Act art. 4(1)). FP and FS are due only where the monthly base is at least the minimum wage, and not for women aged 55 or more or men aged 60 or more (Labour Market Act art. 259(1), 261). No FP and FS for 12 months for a hire aged 50 or more who was registered unemployed in the 30 days before, or a referred unemployed hire under 30 (art. 262), and for 36 months after a return from maternity, parental or childcare leave (art. 263). FGŚP has no minimum-wage condition, but the same age, 50-plus, under-30 and return-from-leave exemptions apply (Employee Claims Act art. 9a-9c). Employer PPK payments are not part of the pension and disability base (PPK Act art. 26(5)).

**Health contribution.** 9% of the same base as pension, less the employee's own pension, disability and sickness contributions (Health Act art. 81(1) and (6)). There is no annual cap. Since 2022 it is not deducted from tax (the old art. 27b of the PIT Act is repealed).

**PIT advance, month by month (PIT Act art. 32(4)).**
1. Start with the month's revenue from the employment: cash pay plus benefits in kind and other free benefits (art. 12(1)). Whether and when the employer's PPK payment counts here is on the "Not yet confirmed" line below.
2. Deduct the standard costs (PLN 250, or 300 for a commuter who files the statement in art. 32(7)), or author's costs where the contract says so.
3. Deduct the employee's social contributions withheld that month (9.76% + 1.5% + 2.45% = 13.71% while under the cap).
4. Round the result to whole złoty (Tax Ordinance art. 63 § 1). This is the month's income.
5. Apply 12%, or 32% once cumulative income from this payer is above PLN 120,000 (art. 32(2)). In the crossing month, split the income at the threshold. If the employee filed a statement that they will file jointly with a spouse or as a single parent (art. 6(2) or 6(4d)), all months stay at 12% where the expected incomes meet the conditions in art. 32(3).
6. Subtract PLN 300 if the employee filed a PIT-2 statement with this payer (art. 31b(1)). Round the advance to whole złoty.

**Reliefs.** Revenue exempt under the under-26, relocation, parents of 4+ and working seniors reliefs is left out of steps 1 to 5 up to PLN 85,528 a year in total (art. 21(44)). Social and health contributions are still due on that pay. The payer applies the under-26 relief automatically unless the employee asks it not to (art. 32(6)); the other three need a statement from the employee (art. 31a(8)).

**No advance.** An employee who expects income under PLN 30,000 for the year can ask the payer not to withhold advances at all (art. 31c).

## Deadlines and filing

| What | When | Source |
|---|---|---|
| PIT advances paid to the tax office (mikrorachunek) | by the 20th of the month after withholding | PIT Act art. 38(1) |
| ZUS DRA declaration, RCA monthly reports and payment (social, health, FP, FS, FGŚP, FEP) | by the 15th of the next month for payers with legal personality (e.g. sp. z o.o.); by the 20th for other payers (individuals, partnerships); by the 5th for budget units | ZUS Act art. 47(1) |
| PPK payments | by the 15th of the month after the month the pay was due | PPK Act art. 28 |
| PIT-4R annual payer declaration | by 31 January of the next year | PIT Act art. 38(1a) |
| PIT-11 information per employee | to the tax office by 31 January, to the employee by the end of February | PIT Act art. 39(1), 42g(1) |
| Filing method | PIT-4R and PIT-11 electronically | PIT Act art. 45ba |
| Employer applies a new statement or request from the employee (PIT-2, commuter costs, reliefs, joint filing) | from the month after the month it is received, at the latest | PIT Act art. 31a(5) |

The employee then files the annual return (PIT-37) between 15 February and 30 April (PIT Act art. 45(1)); see [pl-income-tax](pl-income-tax.md).

## Penalties and interest

- **Payer liability.** A payer who did not withhold, or withheld but did not pay, is liable for the tax with all its assets (Tax Ordinance art. 30 § 1 and § 3). Late payment interest runs at the art. 56 § 1 rate: 10.50% a year from 5 March 2026 (M.P. 2026 poz. 269).
- **Fiscal penal code.** Not paying withheld tax on time: fine up to 720 daily rates or up to 3 years' imprisonment, or both (KKS art. 77 § 1). Not withholding or withholding too little: fine up to 720 daily rates or up to 2 years, or both (KKS art. 78 § 1). Amounts under the statutory threshold drop to a fiscal misdemeanour (art. 77 § 3, 78 § 3). Late PIT-11 information: fine up to 120 daily rates (art. 80 § 1). KKS consolidated text Dz.U. 2025 poz. 633.
- **ZUS.** Late contributions carry late payment interest under the Tax Ordinance rules (ZUS Act art. 23(1)); none is charged if it would be under 1% of the minimum wage (art. 23(1a)). ZUS may also impose an additional charge up to 100% of unpaid contributions (art. 24(1a)). Failing to pay, report or file DRA on time is an offence with a fine up to PLN 46,000 (art. 98(1)).

## Cross-border points

- **Work done abroad.** The payer does not withhold advances on pay for work done outside Poland where that pay is or will be taxed abroad, unless the employee asks (PIT Act art. 32(9)). On the annual return, treaty-exempt foreign income uses exemption with progression (art. 27(8)) and other foreign income uses the credit method (art. 27(9)). Residence tests and the return: [pl-income-tax](pl-income-tax.md).
- **Non-resident employees working in Poland.** Advances are computed the same way. The payer sends the PIT-11 to the tax office for foreign persons (art. 39(1), referring to art. 3(2a)).
- **Social security.** Within the EU, EEA and Switzerland, one country's social security applies at a time under Regulation (EC) No 883/2004 (art. 11-13). A posted worker or a person working in two or more states can stay in one system with an A1 certificate. Without an A1, Polish ZUS applies to work done in Poland.
- **Relocation relief.** A person who moves residence to Poland can claim the art. 21(1)(152) relief for four consecutive years, within the PLN 85,528 shared cap.
- **Recharges.** Salaries recharged between related companies are controlled transactions; see [pl-transfer-pricing](pl-transfer-pricing.md).

## Worked examples

### Example 1: PLN 10,000 gross a month, small company employer

An employee of a Polish sp. z o.o. with 9 or fewer insured earns PLN 10,000 gross a month in 2026. One job, lives in the same town, filed PIT-2, aged 35, not in PPK, no benefits in kind. Annual pay is PLN 120,000, so the pension cap (PLN 282,600) is never reached.

**Employee social contributions.** Pension 9.76% = PLN 976.00. Disability 1.5% = PLN 150.00. Sickness 2.45% = PLN 245.00. Total PLN 1,371.00.

**Health.** Base PLN 10,000 − 1,371 = PLN 8,629. At 9%: PLN 776.61.

**PIT advance.** Income = 10,000 − 250 − 1,371 = PLN 8,379. 12% is PLN 1,005.48; less the PIT-2 reduction of PLN 300 gives PLN 705.48, rounded to PLN 705. Cumulative income for the year is 12 x 8,379 = PLN 100,548, under PLN 120,000, so all twelve months stay at 12%.

**Net pay.** 10,000 − 1,371 − 776.61 − 705 = PLN 7,147.39.

**Employer cost.** Pension 9.76% = PLN 976.00, disability 6.5% = PLN 650.00, accident 1.67% = PLN 167.00, FP and FS 2.45% = PLN 245.00, FGŚP 0.10% = PLN 10.00. Total PLN 2,048.00, so the full cost is PLN 12,048.00. The company pays ZUS (both shares plus health) by the 15th and the PIT advance by the 20th of the next month.

```oa-check
name: Employee PLN 10,000 gross, 2026, PIT-2 filed, small payer
inputs:
  gross: 10000
  kup: 250
  reduction: 300
steps:
  - ee_pension: round(pct(gross, 9.76), 2)
  - ee_disability: round(pct(gross, 1.5), 2)
  - ee_sickness: round(pct(gross, 2.45), 2)
  - ee_social: ee_pension + ee_disability + ee_sickness
  - health: round(pct(gross - ee_social, 9), 2)
  - income: round(gross - kup - ee_social, 0)
  - advance: round(pct(income, 12) - reduction, 0)
  - net: gross - ee_social - health - advance
  - er_pension: round(pct(gross, 9.76), 2)
  - er_disability: round(pct(gross, 6.5), 2)
  - er_accident: round(pct(gross, 1.67), 2)
  - er_fp_fs: round(pct(gross, 2.45), 2)
  - er_fgsp: round(pct(gross, 0.10), 2)
  - er_total: er_pension + er_disability + er_accident + er_fp_fs + er_fgsp
  - employer_cost: gross + er_total
  - annual_income: income * 12
expected:
  ee_social: 1371.00
  health: 776.61
  income: 8379
  advance: 705
  net: 7147.39
  er_total: 2048.00
  employer_cost: 12048.00
  annual_income: 100548
```

### Example 2: The month cumulative income crosses PLN 120,000

Same employer and facts, but pay is PLN 20,000 gross every month. Employee social contributions are 13.71% = PLN 2,742.00 a month. Annual pay is PLN 240,000, still under the PLN 282,600 cap, so contributions do not stop.

**Monthly income.** 20,000 − 250 − 2,742 = PLN 17,008. Cumulative after July: 7 x 17,008 = PLN 119,056. After August: PLN 136,064. So August is the crossing month (PIT Act art. 32(2)(2)).

**July advance (12%).** 17,008 x 12% = 2,040.96, less 300 = PLN 1,740.96, rounded to PLN 1,741.

**August advance (split).** The first 120,000 − 119,056 = PLN 944 at 12% is PLN 113.28. The other 17,008 − 944 = PLN 16,064 at 32% is PLN 5,140.48. Total 5,253.76, less 300 = PLN 4,953.76, rounded to PLN 4,954.

**From September (32%).** 17,008 x 32% = 5,442.56, less 300 = PLN 5,142.56, rounded to PLN 5,143. The PIT-2 reduction still applies in 32% months (art. 31b(1) covers all advances under art. 32).

**August net pay.** Health is (20,000 − 2,742) x 9% = PLN 1,553.22. Net is 20,000 − 2,742 − 1,553.22 − 4,954 = PLN 10,750.78, against PLN 13,963.78 in July. The difference is the higher advance only.

```oa-check
name: PLN 20,000 gross, crossing PLN 120,000 in August 2026
inputs:
  gross: 20000
  kup: 250
  reduction: 300
  threshold: 120000
steps:
  - ee_social: round(pct(gross, 13.71), 2)
  - income: round(gross - kup - ee_social, 0)
  - cum_july: income * 7
  - cum_aug: income * 8
  - at_12: threshold - cum_july
  - at_32: income - at_12
  - adv_july: round(pct(income, 12) - reduction, 0)
  - adv_aug: round(pct(at_12, 12) + pct(at_32, 32) - reduction, 0)
  - adv_sep: round(pct(income, 32) - reduction, 0)
  - health: round(pct(gross - ee_social, 9), 2)
  - net_july: gross - ee_social - health - adv_july
  - net_aug: gross - ee_social - health - adv_aug
expected:
  ee_social: 2742.00
  income: 17008
  cum_july: 119056
  cum_aug: 136064
  at_12: 944
  at_32: 16064
  adv_july: 1741
  adv_aug: 4954
  adv_sep: 5143
  health: 1553.22
  net_july: 13963.78
  net_aug: 10750.78
```

The advances are only prepayments. If the employee has other income or reliefs (joint filing, child relief), the PIT-37 return settles the year; see [pl-income-tax](pl-income-tax.md).

## Ask the client first

1. Is the employer a company or other legal person (ZUS due by the 15th) or an individual or partnership (by the 20th)? How many people did it insure for accident on average last year (9 or fewer means 1.67%)?
2. Has the employee filed PIT-2 with this employer, or with up to two others (1/24 or 1/36 split)?
3. Does the employee live outside the town of the workplace (PLN 300 costs), or is part of the pay for creative work under a contract that provides author's costs?
4. Does the employee qualify for a relief: under 26, moved residence to Poland, four or more children, or past retirement age (60 women, 65 men) without drawing a pension?
5. Is the employee in PPK, and at what rates?
6. Does any of the work happen abroad, or is the employee covered by another country's social security with an A1?

## Sources

| Source | URL | Read on |
|---|---|---|
| PIT Act, consolidated text Dz.U. 2026 poz. 592 (art. 21, 22, 27, 31a-32, 38, 39, 42g, 45ba) | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000592 | 2026-10-23 |
| PIT Act amendments after consolidation: Dz.U. 2026 poz. 779 and 846 (checked, no payroll changes) | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000846 | 2026-10-23 |
| ZUS Act, consolidated text Dz.U. 2026 poz. 199 (art. 16-19, 22-24, 47, 98) | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000199 | 2026-10-23 |
| Cap on pension and disability base for 2026, M.P. 2025 poz. 1206 | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WMP20250001206 | 2026-10-23 |
| Accident Insurance Act, Dz.U. 2025 poz. 1644 (art. 28) | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20250001644 | 2026-10-23 |
| Regulation on accident insurance rates, Dz.U. 2025 poz. 1874 (annexes) | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20250001874 | 2026-10-23 |
| ZUS, contribution rates for 2026 (accident 1.67%) | https://www.zus.pl/baza-wiedzy/skladki-wskazniki-odsetki/skladki/wysokosc-skladek-na-ubezpieczenia-spoleczne | 2026-10-23 |
| Health Care Benefits Act, Dz.U. 2025 poz. 1461 (art. 79, 81, 85) | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20250001461 | 2026-10-23 |
| Budget Act 2026, Dz.U. 2026 poz. 62 (art. 24-27) | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000062 | 2026-10-23 |
| Labour Market Act, Dz.U. 2025 poz. 620 (art. 259-263) | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20250000620 | 2026-10-23 |
| Employee Claims Act (FGŚP), Dz.U. 2026 poz. 186 (art. 9-9c, 29) | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000186 | 2026-10-23 |
| Bridging Pensions Act, Dz.U. 2024 poz. 1696 (art. 35-36) | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20240001696 | 2026-10-23 |
| PPK Act, Dz.U. 2026 poz. 192 (art. 26-28) | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000192 | 2026-10-23 |
| Minimum wage 2026, Dz.U. 2025 poz. 1242 | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20250001242 | 2026-10-23 |
| Tax Ordinance, Dz.U. 2026 poz. 622 (art. 30, 56, 63) | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20260000622 | 2026-10-23 |
| Minister of Finance notice on late payment interest rates from 5 March 2026, M.P. 2026 poz. 269 | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WMP20260000269 | 2026-10-23 |
| NBP base rates (lombard 4.25% from 5 March 2026) | https://static.nbp.pl/dane/stopy/stopy_procentowe.xml | 2026-10-23 |
| Solidarity Fund Act, Dz.U. 2024 poz. 1848 (art. 4) | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20240001848 | 2026-10-23 |
| Fiscal Penal Code, Dz.U. 2025 poz. 633 (art. 77-78) | https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20250000633 | 2026-10-23 |
| Regulation (EC) No 883/2004 on social security coordination | https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32004R0883 | 2026-10-23 |

Not yet confirmed: whether the employer's PPK payment is employment revenue of the employee under PIT Act art. 12(1), and in which month it arises (the PIT Act and PPK Act do not say so expressly; only secondary sources were found); the 2027 minimum wage (Dz.U. 2026 poz. 1213) is out of scope for this 2026 skill.
