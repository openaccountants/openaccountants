---
name: de-payroll
description: "German payroll for employees for pay periods in 2026: wage tax (Lohnsteuer) by tax class I to VI through the finance ministry's 2026 program flow (PAP) with the EUR 12,348 basic allowance, the Vorsorgepauschale, solidarity surcharge and church tax; the four social insurance branches (pension 18.6%, unemployment 2.6%, health 14.6% plus the fund's additional rate, average 2.9%, care 3.6% with the childless surcharge) and the 2026 ceilings; Minijobs (EUR 603), the Midijob band to EUR 2,000, the Aktivrente; the wage tax return by the 10th, contributions by the third-last bank working day, DEÜV reports, payslips, minimum wage, tax-free surcharges, sick and maternity pay, and penalties. Trigger on: Lohnsteuer, Gehaltsabrechnung, Brutto Netto, Steuerklasse, Arbeitgeberanteil, Beitragsbemessungsgrenze, Minijob, Midijob, Lohnsteuer-Anmeldung, DEÜV. Out of scope: the employee's annual return (de-employee-income-tax), the self-employed (de-social-contributions, de-self-employed-income-tax), non-residents' wider German tax (de-non-resident-tax)."
version: 1.1
jurisdiction: DE
tax_year: 2026
last_updated: 2026-10-24
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# German payroll 2026: wage tax, social insurance, Minijobs and reporting

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any specific employer's or employee's facts. Payroll software that implements the 2026 PAP, and a Steuerberater or payroll accountant (Lohnbuchhalter), should confirm results before a real payroll run.

**The year.** The 2026 PAP applies to pay for periods "die nach dem 31. Dezember 2025, aber vor dem 1. Januar 2027 enden" and to one-time payments received in that window ([PAP 2026, Anlage 1](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2)). Social insurance values apply from 1 January 2026. Pay for 2025 periods still being corrected is covered at the end of "Deadlines and filing".

**Sibling skills.** The employee's own annual return: [de-employee-income-tax](de-employee-income-tax.md). Contributions of the self-employed: [de-social-contributions](de-social-contributions.md); their income tax: [de-self-employed-income-tax](de-self-employed-income-tax.md). German tax of non-residents beyond payroll: [de-non-resident-tax](de-non-resident-tax.md). A foreign company hiring its first German employee: [de-uk-employer-first-hire](de-uk-employer-first-hire.md). Frontier workers to Switzerland: [germany-to-switzerland-cross-border-tax](germany-to-switzerland-cross-border-tax.md). [germany-payroll](germany-payroll.md) overlaps with this skill.

## Who this applies to

- **Employers in Germany.** Wage tax is collected by deduction from pay where the employer is a "domestic employer": it has a residence, seat, management, permanent establishment or permanent representative in Germany, or it is a foreign agency hiring out workers to work in Germany ([§ 38(1) EStG](https://www.gesetze-im-internet.de/estg/__38.html)). The employee owes the tax; the employer must withhold it at every payment ([§ 38(3) EStG](https://www.gesetze-im-internet.de/estg/__38.html)) and is liable for it ([§ 42d(1) EStG](https://www.gesetze-im-internet.de/estg/__42d.html)).
- **Social insurance.** The employer pays the whole contribution (Gesamtsozialversicherungsbeitrag) to the collecting office and gets the employee's share back only by deducting it from pay ([§ 28e SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28e.html), [§ 28g SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28g.html)). The collecting office is the employee's health fund; for Minijobs it is the Minijob-Zentrale ([§ 28i SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28i.html)).
- **Who is in.** Employees in normal jobs, Minijobs, short-term jobs and the transition band (Midijob), and employees past the standard retirement age.
- **Who is out, and refer.** The self-employed; managing directors and shareholder-directors of a GmbH or UG and family members until their insurance status has been decided; civil servants; the miners' pension scheme; employer pensions (Versorgungsbezüge) and the old-age relief; benefits in kind, company cars and flat-rate taxes under § 37b and § 40 EStG; students and working students; short-time pay and parental leave beyond the reporting duty; part-month pay periods; exact church tax (state caps, mixed-faith couples); private-household Minijobs beyond the rates below.

## Rates, bands and thresholds

All wage tax amounts are yearly. The PAP annualises the period's pay, computes the year's tax and divides it back.

**Wage tax and surcharges**

| Item | Rate or amount | Year | Source |
| --- | --- | --- | --- |
| Basic allowance (Grundfreibetrag): no tax up to | EUR 12,348 | 2026 | [§ 32a(1) EStG](https://www.gesetze-im-internet.de/estg/__32a.html) |
| First progressive zone: (914.51 y + 1,400) y | EUR 12,349 to 17,799 | 2026 | § 32a(1) EStG |
| Second progressive zone: (173.10 z + 2,397) z + 1,034.87 | EUR 17,800 to 69,878 | 2026 | § 32a(1) EStG |
| Third zone: 0.42 x less 11,135.63 | EUR 69,879 to 277,825 | 2026 | § 32a(1) EStG |
| Top zone: 0.45 x less 19,470.38 | from EUR 277,826 | 2026 | § 32a(1) EStG |
| Employee lump sum (ANP), classes I to V | EUR 1,230 | 2026 | [§ 9a EStG](https://www.gesetze-im-internet.de/estg/__9a.html) |
| Special expenses lump sum (SAP), classes I to V | EUR 36 | 2026 | [§ 10c EStG](https://www.gesetze-im-internet.de/estg/__10c.html) |
| Single parent relief (EFA), class II, first child; each further child adds EUR 240 (only through an ELStAM allowance) | EUR 4,260 | 2026 | [§ 24b(2) EStG](https://www.gesetze-im-internet.de/estg/__24b.html) |
| Child allowances per counter, classes I to III (surcharge and church tax base only) | EUR 9,756 | 2026 | [PAP 2026](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2) |
| Child allowances per counter, class IV | EUR 4,878 | 2026 | PAP 2026 |
| Classes V and VI: minimum tax as share of the taxable amount | 14% | 2026 | [§ 39b(2) sentence 7 EStG](https://www.gesetze-im-internet.de/estg/__39b.html) |
| Classes V and VI: at most 42% above EUR 14,071; exactly 42% above EUR 34,939; 45% above EUR 222,260 | thresholds as stated | 2026 | § 39b(2) sentence 7 EStG; PAP 2026 (W1STKL5, W2STKL5, W3STKL5) |
| Vorsorgepauschale: the unemployment part counts only so far as it and the health and care parts together stay within | EUR 1,900 | 2026 | [§ 39b(2) sentence 5 no. 3(e) EStG](https://www.gesetze-im-internet.de/estg/__39b.html); PAP 2026 (VSPHB) |
| Reduced health rate used in the Vorsorgepauschale (PAP: KVSATZAN = KVZ/2/100 + 0.07) | 14.0% | 2026 | [§ 243 SGB V](https://www.gesetze-im-internet.de/sgb_5/__243.html); PAP 2026 |
| Solidarity surcharge on the wage tax | 5.5% | 2026 | [§ 4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html) |
| Surcharge capped at this share of the excess over the exemption limit (phase-in) | 11.9% | 2026 | § 4 SolzG |
| Surcharge exemption limit, all classes except III | EUR 20,350 | 2026 | [§ 3(3) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html) |
| Surcharge exemption limit, class III | EUR 40,700 | 2026 | § 3(3) SolzG |
| Church tax on the church tax base, by state | 8% or 9% | 2026 | [Finance ministry, Steuern von A bis Z](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9) |
| Tax-free pay past the standard retirement age (Aktivrente), per year | EUR 24,000 | 2026 | [§ 3 no. 21 EStG](https://www.gesetze-im-internet.de/estg/__3.html) |
| The same, per month in payroll | EUR 2,000 | 2026 | [Finance ministry Aktivrente FAQ](https://www.bundesfinanzministerium.de/Content/DE/FAQ/FAQ-zur-Aktivrente.html) |

**Social insurance**

| Item | Rate or amount | Year | Source |
| --- | --- | --- | --- |
| Pension insurance, full rate (employer and employee 9.3% each) | 18.6% | 2026 | [RVBeitrSBek 2026](https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html); [§ 168(1) no. 1 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__168.html) |
| Unemployment insurance, full rate (1.3% each) | 2.6% | 2026 | [§ 341(2) SGB III](https://www.gesetze-im-internet.de/sgb_3/__341.html); [§ 346(1) SGB III](https://www.gesetze-im-internet.de/sgb_3/__346.html) |
| Health insurance, general rate (half each) | 14.6% | 2026 | [§ 241 SGB V](https://www.gesetze-im-internet.de/sgb_5/__241.html); [§ 249(1) SGB V](https://www.gesetze-im-internet.de/sgb_5/__249.html) |
| Health: the fund's own additional rate, half each | fund's rate | 2026 | § 249(1) SGB V |
| Average additional rate (planning value; binding for the groups of § 242(3) SGB V) | 2.9% | 2026 | [Federal Health Ministry, Beiträge](https://www.bundesgesundheitsministerium.de/beitraege) |
| Care insurance, full rate | 3.6% | 2026 | [§ 1 PBAV 2025](https://www.gesetze-im-internet.de/pbav_2025/__1.html) |
| Care, employer share outside Saxony (employee the same with one child) | 1.8% | 2026 | [§ 58(1) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__58.html); PAP 2026 |
| Care, Saxony: employee bears 1 point more (employee 2.3%, employer 1.3%, with one child) | 1 point | 2026 | [§ 58(3) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__58.html); PAP 2026 |
| Childless surcharge, employee only, from the month after turning 23 | 0.6 points | 2026 | [§ 55(3) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__55.html) |
| Reduction per child from the second to the fifth, while under 25, employee only | 0.25 points | 2026 | § 55(3) SGB XI |
| Pension and unemployment ceiling (BBG RV/AV) | EUR 101,400 a year; EUR 8,450 a month | 2026 | [SVBezGrV 2026 § 4](https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf?__blob=publicationFile&v=3); [§ 341(4) SGB III](https://www.gesetze-im-internet.de/sgb_3/__341.html) |
| Health and care ceiling (BBG KV/PV) | EUR 69,750 a year; EUR 5,812.50 a month | 2026 | SVBezGrV 2026 § 2(2) (special JAEG of § 6(7) SGB V); [§ 55(2) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__55.html) |
| Compulsory health insurance threshold (JAEG) | EUR 77,400 a year; EUR 6,450 a month | 2026 | SVBezGrV 2026 § 2(1) |
| Special JAEG, only for people privately insured on 31 December 2002 | EUR 69,750 a year | 2026 | SVBezGrV 2026 § 2(2) |
| Insolvency levy, employer only | 0.15% | 2026 | [§ 360 SGB III](https://www.gesetze-im-internet.de/sgb_3/__360.html) |
| U1 (sick pay) and U2 (maternity) levies, employer only | each fund's rate | 2026 | [§ 1 AAG](https://www.gesetze-im-internet.de/aufag/__1.html), [§ 7 AAG](https://www.gesetze-im-internet.de/aufag/__7.html) |

**Employee care share by children**, derived from the rows above:

| Children | Outside Saxony: employee | Outside Saxony: employer | Saxony: employee | Saxony: employer |
| --- | --- | --- | --- | --- |
| None, employee 23 or older | 2.4% | 1.8% | 2.9% | 1.3% |
| One child (any age); or childless and under 23 | 1.8% | 1.8% | 2.3% | 1.3% |
| Two under 25 | 1.55% | 1.8% | 2.05% | 1.3% |
| Three under 25 | 1.3% | 1.8% | 1.8% | 1.3% |
| Four under 25 | 1.05% | 1.8% | 1.55% | 1.3% |
| Five or more under 25 | 0.8% | 1.8% | 1.3% | 1.3% |

Do not read the care rate from § 55(1) SGB XI: the statute still prints "3,4 Prozent"; the current 3.6% was set by regulation (PBAV 2025).

**Minijobs, short-term jobs and the transition band**

| Item | Rate or amount | Year | Source |
| --- | --- | --- | --- |
| Minimum wage per hour | EUR 13.90 (EUR 14.60 from 1 January 2027) | 2026 | [MiLoV5 § 1](https://www.gesetze-im-internet.de/milov5/__1.html) |
| Minijob limit per month: minimum wage x 130 / 3 (EUR 602.33), rounded up to whole euros | EUR 603 | 2026 | [§ 8(1a) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__8.html); [Minijob-Zentrale](https://www.minijob-zentrale.de/DE/die-minijobs/minijob-mit-verdienstgrenze) |
| Commercial Minijob: employer's flat health contribution (if statutorily insured) | 13% | 2026 | [§ 249b SGB V](https://www.gesetze-im-internet.de/sgb_5/__249b.html) |
| Commercial Minijob: employer's flat pension contribution | 15% | 2026 | [§ 172(3) SGB VI](https://www.gesetze-im-internet.de/sgb_6/__172.html) |
| Minijobber's own pension share (18.6% less 15%), unless released | 3.6% | 2026 | Derived; [Minijob-Zentrale](https://www.minijob-zentrale.de/DE/die-minijobs/minijob-mit-verdienstgrenze) states 3.6% |
| Private-household Minijob: employer's flat health and pension contributions, each | 5% | 2026 | § 249b SGB V; § 172(3a) SGB VI |
| Uniform flat tax where flat or Minijob pension contributions are paid (covers wage tax, surcharge, church tax) | 2% | 2026 | [§ 40a(2) EStG](https://www.gesetze-im-internet.de/estg/__40a.html) |
| Flat tax on a Minijob without those contributions | 20% | 2026 | § 40a(2a) EStG |
| Flat tax for short-term staff (occasional, at most 18 consecutive working days, average pay per working day not above EUR 150, or needed at once at an unforeseeable time) | 25% | 2026 | § 40a(1) EStG |
| No 25% (or farm 5%) flat tax if average pay per hour exceeds | EUR 19 | 2026 | § 40a(4) no. 1 EStG |
| Short-term job, contribution-free: limited to (not if pursued as an occupation and paid above EUR 603) | 3 months or 70 working days a calendar year; on a farm 15 weeks or 90 working days | 2026 | [§ 8(1) no. 2 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__8.html) |
| Transition band (Midijob), regular monthly pay, all jobs together | EUR 603.01 to EUR 2,000 | 2026 | [§ 20(2) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__20.html); [Minijob-Zentrale, Midijob](https://www.minijob-zentrale.de/DE/die-minijobs/midijob) |
| Factor F = 28% divided by the total contribution rate (18.6 + 3.6 + 2.6 + 14.6 + 2.9 = 42.3), as published by the labour ministry (notice of 25 November 2025, Federal Gazette 18 December 2025) | 0.6619 | 2026 | § 20(2a) SGB IV; [Berlin Senate finance circular on 2026 social insurance values](https://www.berlin.de/politik-und-verwaltung/rundschreiben/download.php/4330060) |
| Apprentices: employer bears the whole contribution if monthly pay is not above | EUR 325 | 2026 | § 20(3) SGB IV |

## The taxable base

**Wage tax, in the PAP's order** ([§ 39b(2) EStG](https://www.gesetze-im-internet.de/estg/__39b.html)):

1. **Annualise.** Monthly pay x 12; weekly x 360/7; daily x 360.
2. **Take out tax-free pay first**, such as the Aktivrente and tax-free surcharges (below).
3. **Deduct** the ELStAM allowance (or add the added amount), the class amounts (ANP and SAP in classes I to V, EFA in class II) and the Vorsorgepauschale. The result is the taxable amount (ZVE).
4. **Tariff.** Classes I, II and IV: § 32a(1) on the ZVE rounded down to whole euros. Class III: tax on half, doubled (§ 32a(5)). Classes V and VI: twice the difference between the tariff on 1.25 times and 0.75 times the ZVE, at least 14%, with the 42% and 45% caps in the table. Never apply the plain tariff to V or VI. Class IV with a factor ([§ 39f EStG](https://www.gesetze-im-internet.de/estg/__39f.html)): the class IV tax times the factor.
5. **Back to the period.** 1/12, 7/360 or 1/360 of the year's tax; parts of a cent are dropped.
6. **Surcharge and church tax base.** Run the same calculation again with the child allowances deducted (two allowances per counter in classes I to III, per [§ 3(2a) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html) and [§ 51a(2a) EStG](https://www.gesetze-im-internet.de/estg/__51a.html)). That tax (JBMG) is the base for the surcharge and church tax. The wage tax itself does not fall because of children.

**Tax classes** ([§ 38b EStG](https://www.gesetze-im-internet.de/estg/__38b.html)): I single, or married not meeting III or IV, or with limited tax liability; II as I with the single parent relief; III married, both resident, not permanently separated, with the spouse in V on joint application, and the widowed in the year after the death; IV the default for married couples; V the spouse of a class III employee; VI second and further jobs. Missing wage tax data through the employee's fault: class VI; a technical fault: the expected class for at most three months ([§ 39c(1) EStG](https://www.gesetze-im-internet.de/estg/__39c.html)).

**Vorsorgepauschale** (the employee's insurance, inside the tax; [§ 39b(2) sentence 5 no. 3 EStG](https://www.gesetze-im-internet.de/estg/__39b.html), PAP 2026):

- Pension: pay up to EUR 101,400 x 9.3%, unless not in the statutory scheme (PAP marker KRV = 1).
- Health and care: pay up to EUR 69,750 x (half the fund's additional rate + 7.0% + the employee care rate). The PAP uses the full additional rate of the employee's own fund: "Der durchschnittliche Zusatzbeitragssatz ist unmaßgeblich", except for the § 242(3) SGB V groups. The statutory health and care parts apply in classes I to VI ([§ 39b(2) sentence 5 no. 3(b), (c) EStG](https://www.gesetze-im-internet.de/estg/__39b.html)); the ministry's class VI test figures include them. Privately insured (PKV = 1): the private premiums from the ELStAM less the tax-free employer subsidy, classes I to V only; in class VI a privately insured employee gets no health or care part.
- Unemployment (new in 2026, ALV = 0 if insured, not in class VI): the PAP compares pension + health + care with pension + the lower of EUR 1,900 and (unemployment + health + care), and takes the higher. Once health and care alone pass EUR 1,900, unemployment adds nothing.
- The total is rounded up to whole euros (PAP 2026, MVSPKVPV and MVSPHB). There is no minimum Vorsorgepauschale in 2026. Severance under § 24 no. 1 EStG is left out of the insurance parts.

**Other PAP inputs that change the result:** ALV (0 insured / 1 not), KRV, PKV (0 statutory, 1 private), KVZ (the fund's full additional rate), PVZ (1 = childless surcharge), PVA (number of reductions, 0 to 4), PVS (1 = place of employment in Saxony).

**Solidarity surcharge and church tax.** No surcharge while the yearly base does not exceed the exemption limit; above it, the lower of 5.5% of the base and 11.9% of the excess ([§ 4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html)). The period limit is the matching fraction of the yearly limit ([§ 3(4) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html)). Church tax applies only to members of a church that levies it, at the state's rate on the base.

**One-time payments** (bonuses, holiday and Christmas pay, back pay, severance) use the annual method of [§ 39b(3) EStG](https://www.gesetze-im-internet.de/estg/__39b.html): tax on the expected annual pay with the payment, less tax without it. If certificates from earlier employers this year are missing, the employer scales up current pay, marks the payroll account "S", and the employee must then file a return ([§ 46(2) no. 5a EStG](https://www.gesetze-im-internet.de/estg/__46.html)). Surcharge on a one-time payment: only if the year's tax with child allowances exceeds the limit ([§ 3(4a) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html)), and then the full 5.5% with no phase-in (§ 4 sentence 4 SolzG). The one-fifth relief of § 34 EStG for severance is not given in payroll; the 2026 PAP covers only "§ 39b Absatz 3 Satz 1 bis 8 EStG". The employee claims it in the return.

**Aktivrente, new in 2026** ([§ 3 no. 21 EStG](https://www.gesetze-im-internet.de/estg/__3.html), [finance ministry FAQ](https://www.bundesfinanzministerium.de/Content/DE/FAQ/FAQ-zur-Aktivrente.html)): pay from an employment under § 19(1) no. 1 EStG for work from the month after the standard retirement age (§ 35 sentence 2 or § 235 SGB VI) is tax-free up to EUR 2,000 a month, where the employer owes pension contributions under § 168(1) no. 1 or no. 1d or § 168(3), § 172(1) or § 172a SGB VI. The yearly EUR 24,000 falls by one twelfth for each month the conditions are not met. Not for Minijobs, self-employment or civil service. Pay already tax-free under another rule does not use it. Class VI only with the employee's confirmation that no other job uses it, kept with the payroll account. Unused room does not move to another month; a one-time payment is exempt only within the month's room. When a job ends mid-month the amount is apportioned by days; a new job started mid-month gets the full amount if the employee confirms in writing that none was used that month. Contributions are unchanged.

**Tax-free night, Sunday and holiday surcharges** ([§ 3b EStG](https://www.gesetze-im-internet.de/estg/__3b.html)), paid on top of basic pay for work actually done: night (20:00 to 06:00) 25%, rising to 40% for 00:00 to 04:00 if the shift began before midnight; Sunday 50%; public holidays and 31 December from 14:00 125%; 24 December from 14:00, 25 and 26 December and 1 May 150%; hourly basic pay counted at most EUR 50. They are free of contributions only where the hourly pay they are based on is not above EUR 25 ([§ 1(1) no. 1 SvEV](https://www.gesetze-im-internet.de/svev/__1.html)). So a surcharge can be tax-free and still carry contributions.

**Contribution base.**

- Each branch: pay for the period, capped at that branch's monthly ceiling, times the shares; round each amount to the cent.
- Several insured jobs together above a ceiling: each pay is reduced in proportion so that together they reach the ceiling ([§ 22(2) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__22.html)).
- One-time payments carry contributions only up to the unused pro-rata yearly ceiling. One paid from 1 January to 31 March that passes that ceiling goes to the last period of the previous year, if the same employer employed the person then ([§ 23a SGB IV](https://www.gesetze-im-internet.de/sgb_4/__23a.html)).
- Care children: proof of parenthood and children under 25 must be given; proof through the automated procedure, or other proof within six months of the birth, counts from the month of birth; the reduction ends with the month the child turns 25. No surcharge for people born before 1940, those in military or civilian service, or recipients of basic income support ([§ 55(3), (3a) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__55.html)). Saxony is tested by place of employment ([§ 58(3) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__58.html)).
- Pay above the JAEG: compulsory health insurance ends at the end of the year in which the threshold is passed, and only if pay also exceeds the next year's threshold ([§ 6(4) SGB V](https://www.gesetze-im-internet.de/sgb_5/__6.html)). A voluntary member then pays the fund directly and the employer pays a subsidy of what it would bear under compulsory insurance ([§ 257(1) SGB V](https://www.gesetze-im-internet.de/sgb_5/__257.html)).
- Past the standard retirement age: drawing a full old-age pension, or reaching that age, frees the employee from pension and unemployment contributions, but the employer still pays its half ([§ 172(1) SGB VI](https://www.gesetze-im-internet.de/sgb_6/__172.html), [§ 346(3) SGB III](https://www.gesetze-im-internet.de/sgb_3/__346.html)).
- A missed employee deduction can be made up only at the next three payments, later only if the employer was not at fault ([§ 28g SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28g.html)).
- U1 applies to employers with, as a rule, not more than 30 employees (apprentices not counted) and refunds 80% of continued sick pay; U2 applies to all employers. U1, U2 and the insolvency levy are charged on pension-contribution pay ([§ 1 AAG](https://www.gesetze-im-internet.de/aufag/__1.html), [§ 7(2) AAG](https://www.gesetze-im-internet.de/aufag/__7.html), [§ 358(2) SGB III](https://www.gesetze-im-internet.de/sgb_3/__358.html)). Accident insurance is billed by the Berufsgenossenschaft after the year.
- 2027 already enacted: the health ceiling will be the special JAEG plus EUR 3,600 ([§ 223(4) SGB V](https://www.gesetze-im-internet.de/sgb_5/__223.html)).

**Minijob rules.** The limit is on regular monthly pay; an unforeseeable overrun in not more than two calendar months within the twelve months ending with the pay period, each by up to the limit itself, does not end the Minijob ([§ 8(1b) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__8.html)). Several Minijobs are added together; one Minijob beside a main insured job stays separate, every further one is added to the main job ([§ 8(2) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__8.html)). A Minijobber is in pension insurance unless they apply in writing or electronically to be released ([§ 6(1b) SGB VI](https://www.gesetze-im-internet.de/sgb_6/__6.html)); the employer's 15% stays. The flat tax is an option: the employer may tax by the ELStAM instead. The 2% flat tax is collected by the Minijob-Zentrale (Deutsche Rentenversicherung Knappschaft-Bahn-See, [§ 40a(6) EStG](https://www.gesetze-im-internet.de/estg/__40a.html)); 20% and 25% go on the wage tax return. Exactly EUR 603 is a Minijob ("nicht übersteigt"); EUR 603.01 is in the transition band.

**Transition band.** Normal wage tax by the ELStAM. Contributions are worked out on reduced bases by two formulas in [§ 20(2a) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__20.html), with AE the monthly pay, G = EUR 603 and F = 0.6619. Base for the total contribution: BE = F x G + (2,000 / (2,000 - G) - G / (2,000 - G) x F) x (AE - G). Base for the employee's share: BE = 2,000 / (2,000 - G) x (AE - G). The employee pays the employee rates on the second base; the employer pays the total contribution on the first base less the employee's share. At AE EUR 1,000 the bases are EUR 854.06 and EUR 568.36. Not for apprentices. Exactly EUR 2,000 is still in the band ("nicht übersteigen").

**Minimum wage.** EUR 13.90 per hour worked, paid at the agreed date and at the latest on the last bank working day (Frankfurt am Main) of the month after the work ([§ 2(1) MiLoG](https://www.gesetze-im-internet.de/milog/__2.html)). Hours on a written working-time account may not exceed 50% of contractual hours a month and must be balanced within twelve months (§ 2(2) MiLoG). Not covered ([§ 22 MiLoG](https://www.gesetze-im-internet.de/milog/__22.html)): under-18s without completed vocational training, apprentices, volunteers, compulsory internships and orientation or study-accompanying internships of up to three months, and the formerly long-term unemployed in their first six months.

**Sick pay and the maternity top-up.** Continued pay for up to six weeks per incapacity, once the job has lasted four weeks without a break; the same illness again gives a new six weeks only after six months free of it, or twelve months after the first incapacity from it began ([§ 3 EntgFG](https://www.gesetze-im-internet.de/entgfg/__3.html)), at the pay for regular working time ([§ 4 EntgFG](https://www.gesetze-im-internet.de/entgfg/__4.html)). During the protection periods and the day of birth the employer pays the difference between EUR 13 and the average net pay per calendar day ([§ 20(1) MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__20.html)); U2 refunds it ([§ 1(2) AAG](https://www.gesetze-im-internet.de/aufag/__1.html)).

## Deadlines and filing

**Before the first payday**

- **Employer number** (Betriebsnummer) from the Federal Employment Agency for each place of employment.
- **Immediate report** in listed sectors, "spätestens bei dessen Aufnahme", to the pension insurers' data office: construction, hospitality, passenger transport, haulage and logistics including platform delivery, fairground work, building cleaning, trade-fair construction, the meat industry (not the butchers' trade), prostitution, security, hairdressing and cosmetics ([§ 28a(4) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28a.html)). It does not replace the registration.
- **Wage tax data.** Take the tax ID and date of birth, retrieve the ELStAM and call up changes monthly ([§ 39e(5) EStG](https://www.gesetze-im-internet.de/estg/__39e.html)).
- **Payroll account** (Lohnkonto) per employee and year, kept to the end of the sixth calendar year after the last entry ([§ 41(1) EStG](https://www.gesetze-im-internet.de/estg/__41.html)).

**Filing and payment**

| Duty | Deadline | Source |
| --- | --- | --- |
| Wage tax return (Lohnsteuer-Anmeldung), electronic, and payment to the Betriebsstättenfinanzamt | 10th day after each filing period | [§ 41a(1) EStG](https://www.gesetze-im-internet.de/estg/__41a.html) |
| Filing period: monthly | previous year's wage tax above EUR 5,000 | [§ 41a(2) EStG](https://www.gesetze-im-internet.de/estg/__41a.html) |
| Filing period: quarterly (10 April, 10 July, 10 October, 10 January) | above EUR 1,080 and not above EUR 5,000 | § 41a(2) EStG |
| Filing period: yearly (10 January) | not above EUR 1,080 | § 41a(2) EStG |
| New business last year: convert last year's wage tax to a full year; new this year: first full month x 12 | as stated | § 41a(2) EStG |
| Deadline on a Saturday, Sunday or public holiday | next working day | [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) |
| Contributions (estimated amount) | third-last bank working day of the month worked; remainder the third-last bank working day of the next month | [§ 23(1) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__23.html) |
| Contribution statement (Beitragsnachweis) | two working days before the due date | [§ 28f(3) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28f.html) |
| DEÜV registration | first payroll run after the start, at the latest six weeks after it | [§ 6 DEÜV](https://www.gesetze-im-internet.de/de_v/__6.html) |
| DEÜV de-registration | next payroll run after the end, at the latest six weeks after it | [§ 8 DEÜV](https://www.gesetze-im-internet.de/de_v/__8.html) |
| Interruption report (pay stops for at least a calendar month, for example sick pay from the fund) | within two weeks after the end of the first calendar month of the interruption | [§ 9 DEÜV](https://www.gesetze-im-internet.de/de_v/__9.html) |
| Change of health fund, contribution group or person group key: de-registration and new registration | first payroll run after the change, at the latest six weeks after it | [§ 12(1), (4) DEÜV](https://www.gesetze-im-internet.de/de_v/__12.html) |
| Annual report for 2026 | first payroll run of 2027, at the latest 15 February 2027 | [§ 10 DEÜV](https://www.gesetze-im-internet.de/de_v/__10.html) |
| Electronic wage tax certificate for 2026 | last day of February 2027 | [§ 41b(1) EStG](https://www.gesetze-im-internet.de/estg/__41b.html); [§ 93c(1) AO](https://www.gesetze-im-internet.de/ao_1977/__93c.html) |
| Annual wage tax adjustment (compulsory with at least 10 employees on 31 December, unless barred) | at the earliest with the last 2026 pay run, at the latest with the last run ending in February 2027 | [§ 42b(1), (3) EStG](https://www.gesetze-im-internet.de/estg/__42b.html) |

The annual adjustment is barred (§ 42b(1) sentence 3) where the employee applies against it; was in class V or VI, or in II, III or IV for only part of the year; had an allowance or added amount, or the factor method; drew short-time pay, qualification pay, a maternity top-up, Infection Protection Act compensation, tax-free Aktivrente pay (§ 3 no. 21) or certain tax-free top-ups; has at least one capital letter U; had Vorsorgepauschale parts only for part of the year, a change of the additional rate, or different care reductions; or had foreign employment income without German wage tax.

**Payslip.** At every payment the employee gets a statement in text form showing at least the pay period and how pay is made up; none is needed if nothing changed ([§ 108(1), (2) GewO](https://www.gesetze-im-internet.de/gewo/__108.html)). The required contents are listed in [§ 1 EBV](https://www.gesetze-im-internet.de/entgbv/__1.html): employer and employee details, pension insurance number, pay period, tax class, child allowances, church tax data, tax ID, contribution group key and collecting office, every item of pay and deduction, taxable pay, social insurance gross, wage tax, surcharge, church tax, employee contributions, net pay and the amount paid. The employee may black out the church tax data ([§ 2(2) EBV](https://www.gesetze-im-internet.de/entgbv/__2.html)).

**Minimum wage records.** For Minijobs, short-term jobs and the § 2a SchwarzArbG sectors, record start, end and length of daily working time by the seventh day after the work and keep the records at least two years ([§ 17(1) MiLoG](https://www.gesetze-im-internet.de/milog/__17.html)).

**2025 pay still being corrected.** Use the amended 2025 PAP of 22 January 2025, for periods "die nach dem 31. Dezember 2024, aber vor dem 1. Januar 2026 enden" ([amended PAP 2025](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-01-22-geaenderte-PAP-2025-anlage-1.pdf?__blob=publicationFile&v=2)): basic allowance EUR 12,096, surcharge limit EUR 19,950 (not class III), pension ceiling EUR 96,600, health ceiling EUR 66,150; minimum wage EUR 12.82 ([MiLoV4](https://www.gesetze-im-internet.de/milov4/__1.html)) and Minijob limit EUR 556. Never use 2026 values for 2025 corrections. Employees with wages from two employers at once in 2025 must file a 2025 return ([§ 46(2) no. 2 EStG](https://www.gesetze-im-internet.de/estg/__46.html)).

## Penalties and interest

- **Late payment of wage tax:** 1% of the amount due, rounded down to a multiple of EUR 50, for each month started. Not charged for a delay of up to three days, except for payment by cheque or in cash under § 224(2) no. 1 AO ([§ 240(1), (3) AO](https://www.gesetze-im-internet.de/ao_1977/__240.html)).
- **Late filing of the wage tax return:** a late-filing surcharge is at the tax office's discretion ([§ 152(1) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html)); the compulsory surcharge of § 152(2) and the fixed amounts of § 152(5) do not apply to monthly, quarterly or yearly wage tax returns (§ 152(3) no. 4 and § 152(8) AO).
- **Late contributions:** 1% of the arrears, rounded down to a multiple of EUR 50, for each month started; not charged separately on arrears under EUR 150 ([§ 24(1) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__24.html)).
- **Late contribution statement:** the collecting office may estimate the pay the contributions are based on ([§ 28f(3) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28f.html)).
- **Lost employee share:** a missed employee deduction is lost after the next three payments unless the employer was not at fault ([§ 28g SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28g.html)); the employer still owes the whole contribution.
- **Liability:** the employer is liable for wage tax it should have withheld and paid over, and for tax it wrongly refunded in the annual adjustment ([§ 42d(1) EStG](https://www.gesetze-im-internet.de/estg/__42d.html)).

## Cross-border points

- **Who must withhold.** A foreign company with no German establishment is not a domestic employer, but a German company receiving a seconded employee is the domestic employer when it bears the pay economically, or would have to at arm's length, even if it does not pay it out ([§ 38(1) sentence 2 EStG](https://www.gesetze-im-internet.de/estg/__38.html)). A foreign agency hiring workers out in Germany must withhold too (§ 38(1) no. 2).
- **Non-resident employees.** They go into class I ([§ 38b(1) EStG](https://www.gesetze-im-internet.de/estg/__38b.html)). The Betriebsstättenfinanzamt, not a residence office, issues their tax ID and wage tax data ([§ 39(2), (3) EStG](https://www.gesetze-im-internet.de/estg/__39.html)).
- **Short assignments.** For short activities in Germany of employees with limited tax liability who belong to a foreign establishment of the same employer, the employer may apply a 30% flat tax, if the work in Germany does not exceed 18 consecutive working days ([§ 40a(7) EStG](https://www.gesetze-im-internet.de/estg/__40a.html)).
- **Social insurance postings.** An employee sent abroad within a German employment, limited in advance, stays in German insurance (Ausstrahlung, [§ 4 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__4.html)); one sent to Germany within a foreign employment, limited in advance, is not insured here (Einstrahlung, [§ 5 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__5.html)). EU rules and social security agreements take priority ([§ 6 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__6.html)): get the A1 or treaty certificate before applying either rule.
- **Treaty relief** from wage tax needs an exemption certificate from the Betriebsstättenfinanzamt; this skill does not cover the treaty tests. See [de-non-resident-tax](de-non-resident-tax.md) and, for Swiss frontier workers, [germany-to-switzerland-cross-border-tax](germany-to-switzerland-cross-border-tax.md).
- **Foreign employment income without German wage tax** bars the employer's annual adjustment ([§ 42b(1) sentence 3 no. 6 EStG](https://www.gesetze-im-internet.de/estg/__42b.html)).

## Worked examples

Every number comes from the tables above. Both examples recompute the 2026 PAP from the law and reproduce the finance ministry's own test table (class I EUR 9,389 at EUR 60,000; class III at EUR 100,000 gives EUR 15,012 with the same method).

### Example 1: class I, EUR 5,000 a month, childless, outside Saxony

An employee aged 30, no church, no children, place of employment in Hesse, statutory health fund with a 2.9% additional rate, EUR 5,000 a month, no one-time payments. Annual pay is EUR 60,000. The Vorsorgepauschale is pension EUR 5,580 (60,000 x 9.3%) plus health and care EUR 6,510 (60,000 x (1.45% + 7.0% + 2.4%)). Health and care alone pass EUR 1,900, so unemployment adds nothing: EUR 12,090. The taxable amount is 60,000 less 1,230 less 36 less 12,090 = EUR 46,644, in the second progressive zone. The tariff gives EUR 9,389 a year, the ministry's test-table figure, so EUR 782.41 a month. No surcharge: EUR 9,389 is under EUR 20,350. Employee contributions are pension EUR 465.00, unemployment EUR 65.00, health EUR 437.50 (half of 17.5%) and care EUR 120.00 (2.4%). Net pay is EUR 3,130.09. The employer adds its own EUR 465.00, 65.00, 437.50 and EUR 90.00 care, plus the 0.15% insolvency levy and U1 and U2.

```oa-check
name: DE 2026 class I, EUR 5,000 a month, childless, fund rate 2.9%
inputs:
  monthly_pay: 5000
  fund_rate: 2.9
steps:
  - annual: monthly_pay * 12
  - vsp_pension: min(annual, 101400) * 0.093
  - vsp_health_care: min(annual, 69750) * (fund_rate / 2 / 100 + 0.07 + 0.024)
  - vsp_unemp_cap: min(1900, min(annual, 101400) * 0.013 + vsp_health_care)
  - vsp: ceil(max(vsp_pension + vsp_health_care, vsp_pension + vsp_unemp_cap))
  - zve: floor(annual - 1230 - 36 - vsp)
  - z: (zve - 17799) / 10000
  - annual_tax: floor((173.10 * z + 2397) * z + 1034.87)
  - monthly_tax: floor(annual_tax / 12 * 100) / 100
  - soli: min(annual_tax * 0.055, max(0, annual_tax - 20350) * 0.119)
  - ee_pension: round(monthly_pay * 0.093, 2)
  - ee_unemp: round(monthly_pay * 0.013, 2)
  - ee_health: round(monthly_pay * (14.6 + fund_rate) / 2 / 100, 2)
  - ee_care: round(monthly_pay * 0.024, 2)
  - ee_total: ee_pension + ee_unemp + ee_health + ee_care
  - net: monthly_pay - monthly_tax - ee_total
expected:
  vsp: 12090
  zve: 46644
  annual_tax: 9389
  monthly_tax: 782.41
  soli: 0
  ee_total: 1087.50
  net: 3130.09
```

### Example 2: class III, EUR 9,000 a month, two children, church member, above the ceilings

A married employee in class III (spouse in class V), two children aged 8 and 12 (two child counters), church member in a state with the 8% rate, place of employment outside Saxony, fund additional rate 2.5%, EUR 9,000 a month (EUR 108,000 a year). Pay is above the EUR 6,450 JAEG; assume the employee stays in the statutory fund as a voluntary member, so the employer's subsidy matches the compulsory employer share (§ 257(1) SGB V) and the net shares are the same.

Edge points: pension and unemployment are capped at EUR 8,450 a month, health and care at EUR 5,812.50; the second child gives one 0.25-point care reduction (employee 1.55%). Vorsorgepauschale: pension 101,400 x 9.3% = EUR 9,430.20; health and care 69,750 x (1.25% + 7.0% + 1.55%) = EUR 6,835.50; total EUR 16,265.70, rounded up to EUR 16,266. Taxable amount 108,000 less 1,266 less 16,266 = EUR 90,468. Splitting: tariff on EUR 45,234 is EUR 8,913, doubled EUR 17,826 a year, EUR 1,485.50 a month. The child counters cut only the surcharge and church base: (90,468 less 2 x 9,756) / 2 = EUR 35,478, tariff EUR 5,813, doubled EUR 11,626. No surcharge (below EUR 40,700). Church tax EUR 930.08 a year. Employee contributions: EUR 785.85 + 109.85 + 496.97 + 90.09 = EUR 1,482.76 a month. The employer's care share is EUR 104.63 (1.8% of EUR 5,812.50).

```oa-check
name: DE 2026 class III, EUR 9,000 a month, two children, church 8%, capped
inputs:
  monthly_pay: 9000
  fund_rate: 2.5
  child_counters: 2
  church_rate: 8
steps:
  - annual: monthly_pay * 12
  - care_ee_rate: 0.018 - (child_counters - 1) * 0.0025
  - vsp_pension: min(annual, 101400) * 0.093
  - vsp_health_care: min(annual, 69750) * (fund_rate / 2 / 100 + 0.07 + care_ee_rate)
  - vsp_unemp_cap: min(1900, min(annual, 101400) * 0.013 + vsp_health_care)
  - vsp: ceil(max(vsp_pension + vsp_health_care, vsp_pension + vsp_unemp_cap))
  - zve: floor(annual - 1230 - 36 - vsp)
  - x: floor(zve / 2)
  - z: (x - 17799) / 10000
  - annual_tax: floor((173.10 * z + 2397) * z + 1034.87) * 2
  - monthly_tax: floor(annual_tax / 12 * 100) / 100
  - x_child: floor((zve - child_counters * 9756) / 2)
  - z_child: (x_child - 17799) / 10000
  - jbmg: floor((173.10 * z_child + 2397) * z_child + 1034.87) * 2
  - soli: min(jbmg * 0.055, max(0, jbmg - 40700) * 0.119)
  - church_tax_year: jbmg * church_rate / 100
  - ee_pension: round(min(monthly_pay, 8450) * 0.093, 2)
  - ee_unemp: round(min(monthly_pay, 8450) * 0.013, 2)
  - ee_health: round(min(monthly_pay, 5812.50) * (14.6 + fund_rate) / 2 / 100, 2)
  - ee_care: round(min(monthly_pay, 5812.50) * care_ee_rate, 2)
  - ee_total: ee_pension + ee_unemp + ee_health + ee_care
  - er_care: round(min(monthly_pay, 5812.50) * 0.018, 2)
expected:
  vsp: 16266
  zve: 90468
  annual_tax: 17826
  monthly_tax: 1485.50
  jbmg: 11626
  soli: 0
  church_tax_year: 930.08
  ee_total: 1482.76
  er_care: 104.63
```

Other cases, in short. A commercial Minijob at EUR 603: employer health 13% EUR 78.39, pension 15% EUR 90.45, flat tax 2% EUR 12.06; the Minijobber's 3.6% is EUR 21.71. Aktivrente from May 2026 at EUR 2,500 a month: EUR 2,000 tax-free and EUR 500 taxed in each of May to December, yearly room EUR 16,000. Late payment: EUR 1,275 of wage tax paid one month late costs 1% of EUR 1,250 = EUR 12.50; EUR 3,480 of contributions costs 1% of EUR 3,450 = EUR 34.50 per month started. A quarterly filer's third-quarter deadline fell on Saturday 10 October 2026 and moved to Monday 12 October 2026. A second job in class VI at EUR 20,000 a year bears EUR 2,766 of wage tax against EUR 380 in class I, and EUR 2,234 in class V (ministry test table, built with ALV, KRV and PKV = 0, KVZ 2.90 and the childless surcharge except in class II); wages from two employers at once oblige the employee to file a return ([§ 46(2) no. 2 EStG](https://www.gesetze-im-internet.de/estg/__46.html)). Payroll software implementing the 2026 PAP must reproduce that table; quick self-checks: wage tax is the same with and without child counters while the surcharge and church base never rise with them; class V tax is never below 14% of the taxable amount; pay above a ceiling changes no contribution in that branch.

## Ask the client first

- **ELStAM:** tax class, child counters, church, any allowance or factor; first or further job? Unknown data by the employee's fault means class VI.
- **Health insurance:** which statutory fund and its own additional rate, or private (premiums), or a voluntary member?
- **Children and age:** children under 25 with proof given; is the employee 23 or older; standard retirement age reached?
- **Place of employment:** the state (church tax rate; Saxony care split).
- **Status of each job:** regular monthly pay, other jobs or Minijobs, short-term limits, sector with the immediate-report duty.
- **Last year's wage tax paid over** (sets the filing period) and any one-time payments in this run.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| EStG §§ 3, 3b, 9a, 10c, 24b, 32a, 38, 38b, 39, 39b, 39c, 39e, 39f, 40a, 41, 41a, 41b, 42b, 42d, 46, 51a | https://www.gesetze-im-internet.de/estg/ | 2026-10-24 |
| Solidaritätszuschlaggesetz §§ 3, 4 | https://www.gesetze-im-internet.de/solzg_1995/ | 2026-10-24 |
| Abgabenordnung §§ 93c, 108, 152, 240 | https://www.gesetze-im-internet.de/ao_1977/ | 2026-10-24 |
| SGB IV §§ 4, 5, 6, 8, 20, 22, 23, 23a, 24, 28a, 28e, 28f, 28g, 28i | https://www.gesetze-im-internet.de/sgb_4/ | 2026-10-24 |
| DEÜV §§ 6, 8, 9, 10, 12 | https://www.gesetze-im-internet.de/de_v/ | 2026-10-24 |
| SGB V §§ 6, 223, 241, 243, 249, 249b, 257 | https://www.gesetze-im-internet.de/sgb_5/ | 2026-10-24 |
| SGB VI §§ 6, 168, 172 | https://www.gesetze-im-internet.de/sgb_6/ | 2026-10-24 |
| SGB XI §§ 55, 58 | https://www.gesetze-im-internet.de/sgb_11/ | 2026-10-24 |
| SGB III §§ 341, 346, 358, 360 | https://www.gesetze-im-internet.de/sgb_3/ | 2026-10-24 |
| Aufwendungsausgleichsgesetz §§ 1, 7 | https://www.gesetze-im-internet.de/aufag/ | 2026-10-24 |
| Pension rate notice 2026 (RVBeitrSBek 2026) | https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html | 2026-10-24 |
| Care rate regulation (PBAV 2025) § 1 | https://www.gesetze-im-internet.de/pbav_2025/__1.html | 2026-10-24 |
| Social insurance values regulation 2026 (SVBezGrV 2026), BGBl. 2025 I No. 278 | https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf?__blob=publicationFile&v=3 | 2026-10-24 |
| Finance ministry, Programmablaufplan 2026, Anlage 1 (final, 12 November 2025), incl. test table | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2 | 2026-10-24 |
| Finance ministry, Aktivrente FAQ | https://www.bundesfinanzministerium.de/Content/DE/FAQ/FAQ-zur-Aktivrente.html | 2026-10-24 |
| Finance ministry, Steuern von A bis Z (church tax 8% or 9%) | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9 | 2026-10-24 |
| Federal Health Ministry, contributions page (average additional rate 2.9%, ceilings) | https://www.bundesgesundheitsministerium.de/beitraege | 2026-10-24 |
| Minimum wage regulation MiLoV5 § 1 | https://www.gesetze-im-internet.de/milov5/__1.html | 2026-10-24 |
| Minijob-Zentrale, Minijob with earnings limit (EUR 603, 3.6%) | https://www.minijob-zentrale.de/DE/die-minijobs/minijob-mit-verdienstgrenze | 2026-10-24 |
| Minijob-Zentrale, Midijob (EUR 603.01 to EUR 2,000) | https://www.minijob-zentrale.de/DE/die-minijobs/midijob | 2026-10-24 |
| § 20 SGB IV formula images (BGBl. 2022 I) | https://www.gesetze-im-internet.de/normengrafiken/bgbl1_2022/j1988_0010.jpg and j1988_0020.jpg | 2026-10-24 |
| Berlin Senate finance circular on 2026 social insurance values (factor F 0.6619; average additional rate 2.9% in the Federal Gazette of 10 November 2025) | https://www.berlin.de/politik-und-verwaltung/rundschreiben/download.php/4330060 | 2026-10-24 |
| MiLoG §§ 2, 17, 22; GewO § 108; EBV §§ 1, 2; SvEV § 1; EntgFG §§ 3, 4; MuSchG § 20 | https://www.gesetze-im-internet.de/ | 2026-10-24 |
| Amended PAP 2025 (22 January 2025), for 2025 corrections | https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-01-22-geaenderte-PAP-2025-anlage-1.pdf?__blob=publicationFile&v=2 | 2026-10-24 |
| Minimum wage regulation MiLoV4 § 1 (2025) | https://www.gesetze-im-internet.de/milov4/__1.html | 2026-10-24 |

Not yet confirmed: the Federal Gazette text of the labour ministry's 2026 factor F notice itself (0.6619 is taken from an official state circular that cites it, and equals 28 / 42.3); which states levy 8% and which 9% church tax (secondary sources name Bavaria and Baden-Württemberg at 8%), and state church tax caps; U1 and U2 rates (set by each fund) and accident insurance; the 2027 health ceiling amount; whether the 2026 wage tax certificate deadline moves from Sunday 28 February 2027 to Monday 1 March 2027 under § 108(3) AO.

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
