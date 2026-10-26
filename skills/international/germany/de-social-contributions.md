---
name: de-social-contributions
description: "German social insurance contributions for 2026, written for the self-employed and voluntary members. Covers voluntary statutory health insurance (minimum base EUR 1,318.33, ceiling EUR 5,812.50 a month, 14.0% or 14.6% plus the fund's additional rate, average 2.9%), long-term care at 3.6% with the childless surcharge and child reductions, compulsory pension insurance for the self-employed groups in § 2 SGB VI (teachers, carers, midwives, craftspeople, one-client workers) with the 18.6% rate, standard, start-phase and income-based bases, exemptions, voluntary pension contributions, the Künstlersozialkasse and the 4.9% artists' levy, accident and unemployment insurance on application, the status procedure, due dates, late surcharges and the income tax deduction, plus a short employee summary. Trigger on: Krankenkasse freiwillig, Mindestbeitrag, KSK, Künstlersozialabgabe, Rentenversicherungspflicht Selbständige, Pflegeversicherung Kinderlosenzuschlag, Statusfeststellung. Out of scope: the payroll run (de-payroll), benefits in kind and managing directors (de-payroll-benefits), income tax (de-self-employed-income-tax, de-einkommensteuer-freelancer)."
version: 2.1
jurisdiction: DE
tax_year: 2026
last_updated: 2026-10-26
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Social insurance contributions in Germany 2026: the self-employed, voluntary members and a short employee summary

> **General reference only.** This skill is general reference material for AI-assisted work. The health fund's, pension insurer's or KSK's notice sets the amount owed. A Steuerberater or social insurance adviser should confirm a real case.

**Sibling skills.** The monthly payroll run for employees (withholding, reports, Minijob flat rates, the Midijob band, employer levies, due dates): [de-payroll](de-payroll.md). Benefits in kind, employer pensions and managing directors: [de-payroll-benefits](de-payroll-benefits.md). Income tax of the self-employed: [de-self-employed-income-tax](de-self-employed-income-tax.md) and [de-einkommensteuer-freelancer](de-einkommensteuer-freelancer.md).

## Who this applies to

German social insurance for calendar year 2026: health and long-term care (charged on the same base), pension, unemployment, and accident insurance paid by the business. The insurance rules apply to everyone employed or self-employed in Germany, and the rules that do not need work apply to everyone resident here ([§ 3 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__3.html)).

- **The self-employed and voluntary members** are the focus: voluntary or private health cover, compulsory pension insurance for the groups in § 2 SGB VI, the Künstlersozialkasse (KSK), voluntary and on-application insurance, accident insurance, the status procedure and the tax deduction.
- **Employees** get a short summary below. Payroll steps are in `de-payroll`, which uses the same 2026 rates and ceilings.
- **Not covered:** private premiums, professional pension funds (Versorgungswerke), farmers and foresters, civil servants, and the income tax computation.

**The method, step by step.**

1. **Settle the status.** Work under instructions and inside the client's organisation points to employment ([§ 7(1) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__7.html)). If unclear, use the status procedure below.
2. **Employees:** insured by law in all four branches. Test the JAEG (health and care only) and the Minijob limit, then hand the payroll to `de-payroll`.
3. **Self-employed health:** a main-occupation self-employed person is not compulsorily insured as an employee (§ 5(5) SGB V) and must hold statutory voluntary or private cover ([§ 193(3) VVG](https://www.gesetze-im-internet.de/vvg_2008/__193.html)). Give the fund the latest tax notice, or at the start the expected income.
4. **Health amount:** all income, lifted to the minimum base and cut at the ceiling, times the reduced rate (general rate if sick pay was elected) plus the fund's own additional rate. Care on the same base at the rate for the member's children and age.
5. **Pension:** test the § 2 SGB VI list. If a group applies and the work is more than marginal, register within three months and choose the contribution; check the exemptions. Otherwise decide on voluntary contributions or insurance on application.
6. **Artists and publicists:** test the KSVG conditions, register with the KSK, report next year's expected income by 1 December.
7. **Accident and unemployment:** notify the accident insurer within one week of starting; decide on unemployment insurance on application within three months.
8. **Artists' levy:** if the business pays self-employed artists or publicists, test the levy duty and report the fees by 31 March of the next year.
9. **Pay and check.** The fund's or insurer's notice is the amount. Never rebuild a year's total from rates: add up the debits and check them against the notices.
10. **Income tax:** deduct the contributions within the caps of [§ 10 EStG](https://www.gesetze-im-internet.de/estg/__10.html). They are private, not business expenses.

The three-month windows (pension registration and exemptions, unemployment insurance) and the one-month window of the status procedure all run from the first day of the work.

### Employees: a short summary

Employees working for pay are insured by law in health ([§ 5(1) no. 1 SGB V](https://www.gesetze-im-internet.de/sgb_5/__5.html)), care ([§ 20(1) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__20.html)), pension ([§ 1 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__1.html)) and unemployment ([§ 25(1) SGB III](https://www.gesetze-im-internet.de/sgb_3/__25.html)). They are also covered by accident insurance, which the employer pays alone ([§ 150(1) SGB VII](https://www.gesetze-im-internet.de/sgb_7/__150.html)). The employer pays the total to the employee's health fund ([§ 28h SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28h.html)).

| Branch | Employee | Employer | Rule |
| --- | --- | --- | --- |
| Pension | 9.3% | 9.3% | Half each ([§ 168(1) SGB VI](https://www.gesetze-im-internet.de/sgb_6/__168.html)) |
| Unemployment | 1.3% | 1.3% | Half each ([§ 346(1) SGB III](https://www.gesetze-im-internet.de/sgb_3/__346.html)) |
| Health | 7.3% + half the fund's rate | 7.3% + half the fund's rate | Half each ([§ 249(1) SGB V](https://www.gesetze-im-internet.de/sgb_5/__249.html)) |
| Care, parent | 1.8%, less 0.25 points per child from the second to the fifth under 25 | 1.8% | Half each ([§ 58(1) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__58.html)); for how the reductions split, see `de-payroll` |
| Care, childless, 23 or older | 2.4% | 1.8% | The employee bears the surcharge alone ([§ 58(1) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__58.html)) |

- **Saxony:** the employee bears one more point of care alone ([§ 58(3) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__58.html)); use the shares in `de-payroll`.
- **Ceilings:** pension and unemployment stop at EUR 8,450 a month; health and care at EUR 5,812.50.
- **The JAEG (health and care only):** an employee whose regular yearly pay exceeds EUR 77,400 is free of compulsory health insurance ([§ 6(1) no. 1 SGB V](https://www.gesetze-im-internet.de/sgb_5/__6.html)). For someone already insured, cover ends at the end of the year the limit is exceeded, but only if the pay also exceeds next year's limit (§ 6(4)). The special JAEG of EUR 69,750 applies only to those privately insured on 31 December 2002 for that reason. Such an employee may stay voluntarily or go private; either way the employer pays a subsidy ([§ 257 SGB V](https://www.gesetze-im-internet.de/sgb_5/__257.html)).
- **Minijob and transition band:** pay up to EUR 603 a month is a Minijob ([§ 8(1) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__8.html)). Above that, up to EUR 2,000 a month, the employee's share is reduced ([§ 20(2) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__20.html)). Both are in `de-payroll`.
- **Job plus business:** if self-employment is the main occupation, the job does not bring compulsory health insurance (§ 5(5) SGB V), but pension and unemployment insurance of the job continue. If the job is the main occupation, the employee is insured through it and the freelance income carries no health or care contribution: the contribution is on pay. The exception is an employee who also draws a statutory pension or a pension-like payment (Versorgungsbezüge): then the freelance income counts too, if it and any pension-like payments together exceed 1/20 of the monthly reference amount (EUR 197.75 in 2026) ([§ 226(1) no. 4 and (2) SGB V](https://www.gesetze-im-internet.de/sgb_5/__226.html)). Employing someone above the Minijob level raises the presumption that self-employment is the main occupation; the fund decides case by case.

**Case: employee above the JAEG.** Hired 1 January 2026 at EUR 7,000 a month (EUR 84,000 a year), childless, age 40. Pay exceeds EUR 77,400, so the employee is free of compulsory health insurance and may stay as a voluntary member or go private, with the employer's subsidy. Pension and unemployment continue at 9.3% and 1.3% on the full EUR 7,000: EUR 651.00 and EUR 91.00 from the employee. Payroll steps: `de-payroll`.

### Status determination (Statusfeststellung)

- **Who decides.** The parties to a contract can ask the Deutsche Rentenversicherung Bund, in writing or electronically, whether it is employment or self-employment. This is not possible once a health fund or another insurer has already started its own procedure on the same contract ([§ 7a(1) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__7a.html)). The fund must apply where the employer's report shows that the worker is the employer's spouse, partner or descendant, or a managing shareholder of a GmbH. The decision rests on an overall assessment of all circumstances. Other insurers are bound by it.
- **The test.** Signs of employment are work under instructions and being part of the client's organisation ([§ 7(1) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__7.html)). Working for one client only is not by itself employment, but it can trigger compulsory pension insurance as a one-client self-employed person (group 9 above). Keep the two risks apart.
- **Before the work starts.** On application the decision can be made before the work begins (§ 7a(4a)). Changes in the first month must be reported at once. A client can also ask for an opinion that covers other contracts of the same kind (§ 7a(4b)). These options, the third-party rule of § 7a(2) sentences 2 and 3, and the right to a joint hearing expire at the end of 30 June 2027 (§ 7a(7)). Check the law for any contract running past that date.
- **The one-month window.** If the application is made within one month of the work starting and employment is found, insurance starts only on the day the decision is announced. Two conditions apply: the worker consents, and for the time in between the worker had cover against illness and for old age comparable to the statutory schemes. The total contribution then falls due only when the decision can no longer be challenged (§ 7a(5)).
- **Appeals.** An objection or court action against the decision has suspensive effect (§ 7a(6)).
- **If employment is found later**, without the one-month protection, the client owes contributions back to the start of the work, and late-payment surcharges of 1% a month on the rounded-down arrears can follow ([§ 24(1) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__24.html)). The exposure is large. Refer before the client signs or at once when it comes up.

## Rates, bands and thresholds

All figures are for 2026 unless the row says otherwise. Amounts marked "check" use the average additional health rate; each fund sets its own rate and the fund's notice decides. The 2.9% average for 2026 is announced by the Federal Health Ministry ([Beiträge](https://www.bundesgesundheitsministerium.de/beitraege)), which also lists EUR 1,017.19 as the top monthly health contribution of a voluntary member with sick pay.

**Rates**

| What | 2026 | Source |
| --- | --- | --- |
| Health, general rate (members with a sick pay claim) | 14.6% | [§ 241 SGB V](https://www.gesetze-im-internet.de/sgb_5/__241.html) |
| Health, reduced rate (no sick pay claim: the normal self-employed case) | 14.0% | [§ 243 SGB V](https://www.gesetze-im-internet.de/sgb_5/__243.html) |
| Health, fund's additional rate | set by each fund | [§ 242(1) SGB V](https://www.gesetze-im-internet.de/sgb_5/__242.html) |
| Health, average additional rate (planning value only) | 2.9% (check) | [Federal Health Ministry, Beiträge](https://www.bundesgesundheitsministerium.de/beitraege) |
| Care, base rate | 3.6% | [§ 1 PBAV 2025](https://www.gesetze-im-internet.de/pbav_2025/__1.html) |
| Care, childless surcharge from the month after turning 23; reduction per child from the second to the fifth, while under 25 | 0.6 points; 0.25 points | [§ 55(3) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__55.html) |
| Pension, general scheme; miners' scheme (tax cap only) | 18.6%; 24.7% | [RVBeitrSBek 2026](https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html) |
| Unemployment | 2.6% | [§ 341(2) SGB III](https://www.gesetze-im-internet.de/sgb_3/__341.html) |
| Artists' levy on fees paid in 2026 | 4.9% | [§ 1 KSAbg2026V](https://www.gesetze-im-internet.de/ksabg2026v/BJNR0DC0A0025.html) |

**Full care rate of a member who pays alone, by children** (derived from [PBAV 2025](https://www.gesetze-im-internet.de/pbav_2025/__1.html) and [§ 55(3) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__55.html)): no children, 23 or older 4.2%; one child (any age) or all children 25 or older 3.6%; two under 25 3.35%; three 3.1%; four 2.85%; five or more 2.6%. A parent never pays the surcharge, even when the children are grown. Members born before 1 January 1940 are also exempt from it. Proof of children goes to the care fund, and until it is given the fund charges the childless rate. Proof given within six months of the birth counts from the month of birth; later proof counts from the month after it is given ([§ 55(3a) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__55.html)).

**Reference values and ceilings** ([SVBezGrV 2026](https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf?__blob=publicationFile&v=3))

| What | Per year | Per month |
| --- | --- | --- |
| Reference amount (Bezugsgröße), [§ 1 SVBezGrV 2026](https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf?__blob=publicationFile&v=3) | EUR 47,460 | EUR 3,955 |
| General JAEG (employees only) | EUR 77,400 | EUR 6,450 |
| Special JAEG (privately insured on 31 December 2002), also the health and care ceiling | EUR 69,750 | EUR 5,812.50 |
| Pension and unemployment ceiling | EUR 101,400 | EUR 8,450 |
| Pension ceiling, miners' scheme | EUR 124,800 | EUR 10,400 |

**Worked-out amounts**

| What | 2026 | Working |
| --- | --- | --- |
| Minijob limit, per month | EUR 603 | EUR 13.90 minimum wage x 130 / 3 = EUR 602.33, rounded up ([§ 8(1a) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__8.html), [MiLoV5](https://www.gesetze-im-internet.de/milov5/__1.html)) |
| Voluntary member's minimum base, per month | EUR 1,318.33 | 1/90 of EUR 3,955 per day x 30 = EUR 3,955 / 3 ([§ 240(4) SGB V](https://www.gesetze-im-internet.de/sgb_5/__240.html)) |
| KSK member's minimum health base, per month | EUR 659.17 | 1/180 per day x 30 = EUR 3,955 / 6 ([§ 234(1) SGB V](https://www.gesetze-im-internet.de/sgb_5/__234.html)) |
| Health, lowest and highest, 14.0% + 2.9% = 16.9% | EUR 222.80 and EUR 982.31 (check) | EUR 1,318.33 and EUR 5,812.50 x 16.9% |
| Health with sick pay, 14.6% + 2.9% = 17.5% | EUR 230.71 and EUR 1,017.19 (check) | Same bases x 17.5% |
| Care at 3.6%, lowest and highest (a notice can differ by a cent) | EUR 47.46 and EUR 209.25 | Same bases x 3.6% ([§ 57(4) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__57.html)) |
| Pension, lowest and highest monthly contribution | EUR 112.16 and EUR 1,571.70 | EUR 603 and EUR 8,450 x 18.6% ([§ 165](https://www.gesetze-im-internet.de/sgb_6/__165.html), [§ 167 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__167.html)) |
| Pension, standard and half standard (self-employed) | EUR 735.63 and EUR 367.82 | EUR 3,955 and EUR 3,955 / 2 x 18.6% |
| Unemployment on application, full and start phase | EUR 102.83 and EUR 51.42 | EUR 3,955 and EUR 3,955 / 2 x 2.6% ([§ 345b SGB III](https://www.gesetze-im-internet.de/sgb_3/__345b.html)) |
| Tax cap for pension contributions, single (doubled for spouses assessed jointly) | EUR 30,826 | EUR 124,800 x 24.7% = EUR 30,825.60, rounded up to a full euro ([§ 10(3) EStG](https://www.gesetze-im-internet.de/estg/__10.html)) |

**KSK thresholds**

| Rule | Value | Source |
| --- | --- | --- |
| Not insured if expected yearly income from the work does not exceed | EUR 3,900 | [§ 3(1) KSVG](https://www.gesetze-im-internet.de/ksvg/__3.html) |
| Pension base: expected yearly income, at least | EUR 3,900 | [§ 165(1) no. 3 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__165.html) |
| Health and care base: 1/360 of expected yearly income per day, at least 1/180 of the monthly reference amount; minimum per month | EUR 659.17 | [§ 234(1) SGB V](https://www.gesetze-im-internet.de/sgb_5/__234.html) |

**Previous year (2025) figures still in use**

Used now for the final health assessment of 2025 when the 2025 tax notice arrives, and for the artists' levy report on fees paid in 2025 (due 31 March 2026).

| What | 2025 value | Source |
| --- | --- | --- |
| Reference amount, per month | EUR 3,745 | [§ 1 SVBezGrV 2025](https://www.gesetze-im-internet.de/svbezgrv_2025/__1.html) |
| Health and care minimum base of a voluntary member, per month (EUR 3,745 / 3) | EUR 1,248.33 | [§ 240(4) SGB V](https://www.gesetze-im-internet.de/sgb_5/__240.html) |
| General JAEG, per year | EUR 73,800 | [§ 2 SVBezGrV 2025](https://www.gesetze-im-internet.de/svbezgrv_2025/__2.html) |
| Health and care ceiling, per year and per month | EUR 66,150 and EUR 5,512.50 | [§ 2(2) SVBezGrV 2025](https://www.gesetze-im-internet.de/svbezgrv_2025/__2.html) |
| Pension ceiling, general scheme, per year and per month | EUR 96,600 and EUR 8,050 | [§ 4 SVBezGrV 2025](https://www.gesetze-im-internet.de/svbezgrv_2025/__4.html) |
| Average additional health rate for 2025 (2.9% less the 0.4-point rise) | 2.5% | [Finance ministry monthly report](https://www.bundesfinanzministerium.de/Monatsberichte/Ausgabe/2026/02/Inhalte/Kapitel-2-Analysen/2-3-sollbericht-2026.html) |

- The care base rate of 3.6% applied throughout 2025 as well ([§ 1 PBAV 2025](https://www.gesetze-im-internet.de/pbav_2025/__1.html)).
- The levy rate for 2025 fees: the Künstlersozialabgabe-Verordnung 2024 (BGBl. 2023 I Nr. 240) sets the rate only "im Jahr 2024" (5.0%), and it expired at the end of 2025 ([§ 2 KSAbg2026V](https://www.gesetze-im-internet.de/ksabg2026v/BJNR0DC0A0025.html)). The ordinance that sets the 2025 rate was not found on an official page for this skill: take the 2025 rate from the KSK's notice.

**Already enacted for 2027.** The health and care ceiling will be the special JAEG plus EUR 3,600 ([§ 223(4) SGB V](https://www.gesetze-im-internet.de/sgb_5/__223.html)). The 2027 amounts come in the next ordinance, expected in late 2026 (check).

## The taxable base

### Voluntary and private health and care cover

**Who is in which system.**

- A main-occupation self-employed person is not compulsorily insured as an employee ([§ 5(5) SGB V](https://www.gesetze-im-internet.de/sgb_5/__5.html)); KSK members are the exception.
- When compulsory or family insurance ends, cover continues as voluntary membership from the next day, unless the member leaves within two weeks of the fund's notice and proves other cover ([§ 188(4) SGB V](https://www.gesetze-im-internet.de/sgb_5/__188.html)).
- A person outside the statutory system can join only in the cases in [§ 9 SGB V](https://www.gesetze-im-internet.de/sgb_5/__9.html). The main case is after leaving compulsory insurance with 24 months of cover in the last five years, or 12 months without a break just before, notified to the fund within three months.
- A person who becomes compulsorily insured after turning 55 stays insurance-free if there was no statutory cover in the five years before and at least half of that time was insurance-free, exempt or main-occupation self-employed ([§ 6(3a) SGB V](https://www.gesetze-im-internet.de/sgb_5/__6.html)).
- Everyone resident must hold cover: without statutory cover, a private policy covering at least outpatient and inpatient treatment ([§ 193(3) VVG](https://www.gesetze-im-internet.de/vvg_2008/__193.html)). A voluntary statutory member is compulsorily insured in social care insurance ([§ 20(3) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__20.html)).

**What a voluntary member pays** ([§ 240 SGB V](https://www.gesetze-im-internet.de/sgb_5/__240.html)).

- **Base:** the member's whole economic capacity, not only profit: capital and letting income count too. The base is at least EUR 1,318.33 a month and at most the ceiling of EUR 5,812.50 ([§ 223(3) SGB V](https://www.gesetze-im-internet.de/sgb_5/__223.html)). If the spouse is not in a statutory fund, the spouse's income can count, less set amounts for children (§ 240(5)).
- **Rate:** 14.0% plus the fund's additional rate. It is 14.6% plus that rate only if the member has declared to the fund that the membership shall include sick pay ([§ 44(2) SGB V](https://www.gesetze-im-internet.de/sgb_5/__44.html)).
- **Who pays:** the member pays all of the health contribution ([§ 250(2) SGB V](https://www.gesetze-im-internet.de/sgb_5/__250.html)). The member also pays all of the care contribution, on the same base ([§ 57(4)](https://www.gesetze-im-internet.de/sgb_11/__57.html), [§ 59(4) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__59.html)).

**Provisional and final assessment** (§ 240(1) and (4a) SGB V).

- **Provisional:** set from the latest income tax notice, from the month after it was issued. At the start of self-employment, set from the proven expected income.
- **Final:** set from the year's actual income once that year's tax notice is presented. Overpayments are refunded; shortfalls are charged.
- **No proof within three years:** if actual income is not proven within three years after the year ends, when the fund asks, the year is set finally on the ceiling. This is held off for twelve months where the member shows that no tax notice has been issued yet. Within twelve months of an assessment on the ceiling, the member can have it redone by presenting the tax notice.
- **Proof requested and not given:** the fund charges on the ceiling for as long as proof is missing. A new assessment can be applied for within twelve months. Where there are sufficient signs that income does not exceed the minimum base, the fund must reassess on its own initiative.
- **Letting income and time limits:** letting income is handled the same way. The time limit on the fund's claim does not run until the tax notice is presented.

**Case: high income, sick pay, two children.** Profit EUR 90,000, sick pay elected, two children under 25, the fund's additional rate assumed 2.5%. The base is capped at EUR 5,812.50. Health EUR 5,812.50 x 17.1% = EUR 993.94; care EUR 5,812.50 x 3.35% = EUR 194.72 a month.

### Pension insurance of the self-employed

**Who must be insured** ([§ 2 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__2.html)). Most self-employed people are not. These are:

1. Teachers and educators who regularly employ no employee subject to insurance in the work.
2. Carers in sick, maternity, infant or child care, on the same condition.
3. Midwives.
4. Sea pilots.
5. Artists and publicists under the KSVG (through the KSK).
6. Home-based traders.
7. Coastal skippers and fishers who are part of the crew (or fish without a vessel) and regularly employ no more than four employees subject to insurance.
8. Craftspeople in the Handwerksrolle who themselves meet the conditions for entry.
9. People who regularly employ no employee subject to insurance and work permanently and essentially for one client. For partners, the partnership's clients count, and the partnership's employees count as their employees.

For groups 1, 2, 7 and 9, apprentices count as employees and Minijobbers do not.

- **Marginal work is free.** Self-employed work whose income is regularly not above the Minijob limit is insurance-free in that work ([§ 5(2) no. 2 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__5.html), [§ 8(3) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__8.html)). The limit in force on 1 January (EUR 603 a month in 2026) holds all year. So a teacher with no insured staff is insured once teaching income is more than EUR 603 a month. The same test applies to every group, not only teachers.
- **Register** within three months of starting: groups 1, 2, 3 and 9. Craftspeople report within three months unless the Handwerksrolle already shows it ([§ 190a SGB VI](https://www.gesetze-im-internet.de/sgb_6/__190a.html)).
- **Who pays:** the self-employed person alone. Home-based traders share half and half with the traders they work for. For KSK members the KSK pays and collects half from the member ([§ 169 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__169.html)).
- **When due:** at the latest on the third-last bank working day of the month the work is done ([§ 23(1) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__23.html)).

**Contribution base** ([§ 165 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__165.html)).

- **Default:** the reference amount, which gives the standard contribution of EUR 735.63 a month.
- **Proven income:** if lower or higher income is proven, that income is used, but at least twelve times the Minijob limit a year. That gives the lowest contribution of EUR 112.16 a month; the pension ceiling is the top. The proof is the profit from the insured work in the latest tax notice. It is uprated by the change in average pay and grossed up to a full year if earned in part of the year.
- **New tax notice:** it must reach the insurer within two calendar months of issue. It applies from the month after it is presented, and at the latest from the third month after issue.
- **Current income:** on application, current income is used if it is expected to be at least 30% below the tax-notice income ([§ 165(1a) SGB VI](https://www.gesetze-im-internet.de/sgb_6/__165.html)).
- **Start phase:** until the end of the third calendar year after the year of starting, the statute sets the base at half the reference amount (EUR 367.82 a month), or the full amount on application. Ask the insurer whether a lower proven income can be used in this phase (check).

**Exemptions on application** ([§ 6 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__6.html)).

- **Craftspeople:** after at least 18 years of compulsory contributions.
- **Group 9 (one client):** for three years after first taking up such work, and again for a second such activity. Also a person first liable under group 9 after turning 58, following earlier self-employment. Renaming a business, or keeping its purpose, is not a new start.
- **Chamber professions:** members of a professional pension fund with compulsory chamber membership, applying through the fund.
- **Timing:** an exemption applied for within three months works from the day its conditions are met; later applications work from the day the application arrives.

**No duty: voluntary or on application.**

- **Voluntary contributions:** anyone not compulsorily insured, from age 16, may pay any amount from EUR 112.16 to EUR 1,571.70 a month ([§ 7](https://www.gesetze-im-internet.de/sgb_6/__7.html), [§ 161(2) SGB VI](https://www.gesetze-im-internet.de/sgb_6/__161.html)). Payments for a year count only if made by 31 March of the next year ([§ 197(2)](https://www.gesetze-im-internet.de/sgb_6/__197.html)). Not allowed once a full old-age pension has been granted and the month of reaching the standard retirement age has passed.
- **Compulsory insurance on application:** a self-employed person may apply within five years of starting, or of the end of compulsory insurance from that work ([§ 4(2) SGB VI](https://www.gesetze-im-internet.de/sgb_6/__4.html)). Cover starts when the conditions are first met if applied for within three months, otherwise the day after the application arrives. It ends only when its conditions end; the law names no right to cancel it. Tell the client before applying.

### Artists and publicists: the Künstlersozialkasse

**Who is insured** ([§ 1 KSVG](https://www.gesetze-im-internet.de/ksvg/__1.html)). A self-employed artist or publicist is insured in pension, health and care when both conditions are met:

- the work is done for a living and not just for a short time;
- the person employs no more than one employee in that work (apprentices and Minijobbers do not count).

The KSK decides whether work is artistic or publicist.

(The income thresholds are in the rates table above.)

- **When the income limit bites:** it is lowered pro rata for part-year work and does not apply in the first three years after the work was first taken up. Cover also stays in place so long as income falls to the limit or below no more than twice in six calendar years.

**Member's shares.** The member pays half of each contribution to the KSK.

- **Pension:** half ([§ 15 KSVG](https://www.gesetze-im-internet.de/ksvg/__15.html)).
- **Health:** half at the general rate plus half the fund's additional rate. Without a sick pay claim the reduced rate is used ([§ 16(1) KSVG](https://www.gesetze-im-internet.de/ksvg/__16.html)).
- **Care:** half, adjusted by the § 55(3) SGB XI amounts, so a childless member pays the whole surcharge on top ([§ 16a KSVG](https://www.gesetze-im-internet.de/ksvg/__16a.html)).
- **Due date:** each month's shares are due on the 5th of the next month.
- **Arrears:** after two months' arrears the KSK sends a reminder. If more than one month's share is still unpaid two weeks later, health benefits are suspended until the arrears are paid.
- **Registration and reports:** register on the KSK's forms ([§ 11 KSVG](https://www.gesetze-im-internet.de/ksvg/__11.html)). Report next year's expected income by 1 December, up to the pension ceiling ([§ 12 KSVG](https://www.gesetze-im-internet.de/ksvg/__12.html)). A change of circumstances can be applied for with effect from the next month. Without a report, the KSK estimates.

**The artists' levy (Künstlersozialabgabe)** ([§ 24 KSVG](https://www.gesetze-im-internet.de/ksvg/__24.html)).

- **Typical users** always owe it: publishers, theatres, orchestras, broadcasters, galleries, advertising or PR for third parties, training schools for artistic work and similar.
- **Other businesses** owe it when they commission self-employed artists or publicists for their own advertising or PR, or to use their work in the business to earn income. This applies only if the fees for orders placed in the calendar year exceed EUR 1,000 in total. Once the limit is passed, the whole amount is levied.
- **Exceptions (use-in-business case only):** fees at events when no more than three such events are held in a year, and music clubs for their regular choir leaders or conductors.
- **Base and rate:** all fees paid in the year to self-employed artists or publicists, insured or not, net of VAT shown separately. Payments to collecting societies and tax-free expense allowances are left out ([§ 25 KSVG](https://www.gesetze-im-internet.de/ksvg/__25.html)). The rate is 4.9% for 2026. The levy is a cost of the business, never deducted from the artist.
- **Report:** the year's total goes to the KSK by 31 March of the next year; otherwise the KSK estimates ([§ 27 KSVG](https://www.gesetze-im-internet.de/ksvg/__27.html)).
- **Prepayments:** due within ten days after each month. Each is the current rate on one twelfth of last year's fees; until 1 March, the December amount. None is due if the amount would not exceed EUR 40 ([§ 27(3) KSVG](https://www.gesetze-im-internet.de/ksvg/__27.html)). The KSK can reduce prepayments on application if this year's fees will be much lower.

**Case: KSK member.** Graphic designer, expected 2026 income reported as EUR 30,000 (EUR 2,500 a month), childless, age 28, sick pay claim, additional rate assumed 2.9%. Pension share EUR 2,500 x 18.6% / 2 = EUR 232.50; health share EUR 2,500 x 17.5% / 2 = EUR 218.75; care share EUR 2,500 x 3.6% / 2 plus the whole surcharge EUR 2,500 x 0.6% = EUR 60.00. Total EUR 511.25 to the KSK, due on the 5th of the next month.

**Case: the artists' levy.** An advertising agency (a typical user under § 24(1) KSVG) paid EUR 20,000 net of VAT in 2026 to freelance designers: levy EUR 980.00, reported by 31 March 2027. A bakery that paid EUR 800 in 2026 for a logo for its own advertising, and nothing else, owes no levy for 2026.

### Accident and unemployment insurance

**Accident insurance.**

- **Notify:** tell the competent accident insurer within one week of starting; a trade registration within that week counts. Changes to the type of business are reported within four weeks ([§ 192 SGB VII](https://www.gesetze-im-internet.de/sgb_7/__192.html)).
- **Owner's cover:** most owners are not insured by law but can apply in writing or electronically. Cover starts the day after the application arrives and lapses if a contribution is unpaid two months after it falls due ([§ 6 SGB VII](https://www.gesetze-im-internet.de/sgb_7/__6.html)). Insured by law, with no application: among others self-employed people in the health service or welfare work (for example midwives, physiotherapists, carers) and home-based traders ([§ 2(1) no. 6 and 9 SGB VII](https://www.gesetze-im-internet.de/sgb_7/__2.html)). They owe the contribution themselves (§ 150(1)). Some insurers also cover entrepreneurs through their own statute ([§ 3 SGB VII](https://www.gesetze-im-internet.de/sgb_7/__3.html)): ask the insurer for the trade.
- **Payment:** the entrepreneur pays for staff and, if insured, for the owner ([§ 150(1)](https://www.gesetze-im-internet.de/sgb_7/__150.html)). Contributions are assessed after the year ends ([§ 152 SGB VII](https://www.gesetze-im-internet.de/sgb_7/__152.html)) and are due on the 15th of the month after the notice ([§ 23(3) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__23.html)). During the year the insurer may charge advance payments up to the expected yearly requirement ([§ 164(1) SGB VII](https://www.gesetze-im-internet.de/sgb_7/__164.html)). Each insurer sets its own rates; this skill gives none.

**Unemployment insurance on application** ([§ 28a SGB III](https://www.gesetze-im-internet.de/sgb_3/__28a.html)).

- **Who:** a person starting self-employed work of at least 15 hours a week who either:
  - had 12 months of compulsory unemployment insurance in the 30 months before starting, or
  - had a claim to a wage replacement benefit under SGB III just before starting.
- **Barred:** a person already insured this way who interrupted that work twice and claimed unemployment benefit in the breaks.
- **Deadline:** within three months of starting. If another insurance duty blocked the application, within three months after that ends.
- **Base:** the monthly reference amount, halved until the end of the calendar year after the year of starting ([§ 345b SGB III](https://www.gesetze-im-internet.de/sgb_3/__345b.html)). At 2.6% that is EUR 102.83, or EUR 51.42 a month.
- **Payment:** the insured pays alone, to the employment agency; due date as in the agency's notice (check). The § 24 SGB IV late surcharge does not apply ([§ 349a SGB III](https://www.gesetze-im-internet.de/sgb_3/__349a.html)).
- **End of cover:** after more than three months' arrears (at the end of the last day paid for); by notice, first possible after five years, three months to the end of a month; or when the conditions end.

### Boundaries and exceptions

| Situation | Rule | Source |
| --- | --- | --- |
| Employed with a side business | Health follows the job unless self-employment is the main occupation. If the job is the main occupation, the freelance income carries no health or care contribution, unless the employee also draws a statutory pension or a pension-like payment; then it counts too, if it and any pension-like payments together exceed 1/20 of the monthly reference amount (EUR 197.75 in 2026) ([§ 226(1) no. 4 and (2) SGB V](https://www.gesetze-im-internet.de/sgb_5/__226.html)). Employing someone above the Minijob level raises that presumption | [§ 5(5) SGB V](https://www.gesetze-im-internet.de/sgb_5/__5.html) |
| Teacher or carer with one employee above the Minijob level | Not compulsorily insured under § 2 no. 1 or 2 (a Minijobber does not count; an apprentice does) | [§ 2 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__2.html) |
| Self-employed income at or below the Minijob limit | Pension insurance-free in that work | [§ 5(2) SGB VI](https://www.gesetze-im-internet.de/sgb_6/__5.html) |
| Artist employing two employees above the Minijob level | Not insured under the KSVG | [§ 1 KSVG](https://www.gesetze-im-internet.de/ksvg/__1.html) |
| Business with own-advertising fees of EUR 1,000 or less in the year | No levy; the limit does not help a typical user under § 24(1) | [§ 24(2) KSVG](https://www.gesetze-im-internet.de/ksvg/__24.html) |
| Late statutory contributions | 1% for each month started, on arrears rounded down to EUR 50; not charged separately under EUR 150. Not for unemployment insurance on application | [§ 24(1) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__24.html), [§ 349a SGB III](https://www.gesetze-im-internet.de/sgb_3/__349a.html) |

## Deadlines and filing

Registration windows: pension registration and exemptions, and unemployment insurance on application, within three months of starting; the accident insurer within one week; the status procedure within one month for its protection; the KSK income estimate by 1 December; the artists' levy report by 31 March of the next year.

**Due dates.**

| Contribution | Due | Source |
| --- | --- | --- |
| Voluntary health and care member | Under the fund's statute and the funds' association's rules; ordinarily by the 15th of the month after the contribution month (check the notice) | [§ 23(1) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__23.html) |
| Compulsory pension, self-employed | Third-last bank working day of the month the work is done | [§ 23(1) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__23.html) |
| Voluntary pension | Counts for a year only if paid by 31 March of the next year | [§ 197(2) SGB VI](https://www.gesetze-im-internet.de/sgb_6/__197.html) |
| KSK member's shares | 5th of the next month | [§ 15 KSVG](https://www.gesetze-im-internet.de/ksvg/__15.html) |
| Accident insurance | 15th of the month after the notice | [§ 23(3) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__23.html) |
| Artists' levy | Prepayments within ten days after each month; report by 31 March | [§ 27 KSVG](https://www.gesetze-im-internet.de/ksvg/__27.html) |

**Income tax deduction** ([§ 10 EStG](https://www.gesetze-im-internet.de/estg/__10.html)). The owner's own contributions are private, not business expenses. They are claimed in the income tax return (filed through ELSTER).

| Contribution | Treatment | Value |
| --- | --- | --- |
| Pension (statutory, KSK share, voluntary, professional funds, certain annuities) | Up to the yearly cap ([§ 10(3) EStG](https://www.gesetze-im-internet.de/estg/__10.html)) | EUR 30,826 single, doubled for spouses assessed jointly |
| Basic health cover and statutory care | No cap; a statutory contribution that can give sick pay is first cut by | 4% |
| Other insurance (unemployment, accident, supplementary health) | Within one yearly cap shared with health and care, so nothing if basic health and care already exceed it | EUR 2,800 |
| The same cap where health costs are partly paid without own expense, or tax-free payments under § 3 no. 9, 14, 57 or 62 EStG are made (no. 57 is the KSK's share, so KSK members) | | EUR 1,900 |

Whether the owner's own accident contribution can be a business expense instead is not settled by the statute pages read here: flag it for review.

**Bank debits.**

| Debit from | Treatment |
| --- | --- |
| Statutory health fund | Owner's health and care: private, § 10 EStG. In a business with staff it may be the employees' total contribution: payroll |
| Private insurer | Private premium; only basic cover is deductible without a cap |
| Künstlersozialkasse | Member's shares (private) or the business's levy prepayment (business cost): ask which |
| Deutsche Rentenversicherung | Private; pension deduction |
| Accident insurer (Berufsgenossenschaft) | Staff part: business cost. Owner's part: flag for review |
| Bundesagentur für Arbeit | Unemployment insurance on application: private, other insurance cap |
| Finanzamt | Tax, not social insurance |

## Penalties and interest

- **Late statutory contributions:** a late-payment surcharge of 1% for each month or part month started, on the arrears rounded down to the nearest EUR 50; not charged separately if under EUR 150 ([§ 24(1) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__24.html)). It does not apply to unemployment insurance on application ([§ 349a SGB III](https://www.gesetze-im-internet.de/sgb_3/__349a.html)).
- **Missing income proof (voluntary health member):** the fund charges on the ceiling (EUR 5,812.50 a month) for as long as proof is missing, and finally on the ceiling if actual income is not proven within three years ([§ 240(1) and (4a) SGB V](https://www.gesetze-im-internet.de/sgb_5/__240.html)).
- **KSK arrears:** after two months' arrears a reminder; if more than one month's share is unpaid two weeks later, health benefits are suspended ([§ 16(2) KSVG](https://www.gesetze-im-internet.de/ksvg/__16.html)).
- **Owner's accident cover** lapses if a contribution is unpaid two months after it falls due ([§ 6 SGB VII](https://www.gesetze-im-internet.de/sgb_7/__6.html)). Unemployment insurance on application ends after more than three months' arrears ([§ 28a SGB III](https://www.gesetze-im-internet.de/sgb_3/__28a.html)).
- **Employment found later** without the one-month protection: contributions back to the start of the work plus the surcharges above ([§ 7a SGB IV](https://www.gesetze-im-internet.de/sgb_4/__7a.html)).

## Cross-border points

- **Territory:** German insurance duty follows work in Germany, and the rules that need no work follow residence ([§ 3 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__3.html)).
- **Posting out and in:** a self-employed person who goes abroad for a period limited in advance stays in German insurance (Ausstrahlung); one coming in for such a period from abroad does not enter it (Einstrahlung) ([§ 4(2)](https://www.gesetze-im-internet.de/sgb_4/__4.html), [§ 5(2) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__5.html)).
- **Treaties and EU law come first:** intergovernmental and supranational rules override these provisions ([§ 6 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__6.html)). For work in more than one EU or EEA state, or a stay with an A1 certificate from another state, refer: this skill does not carry those rules.
- **People insured abroad** and cross-border commuters: refer.

## Worked examples

Each example uses 2026 figures from the rates table. The fund's additional rate is assumed at the 2.9% average; a real case uses the fund's own rate and its notice.

**Example 1: self-employed consultant, middle income.** Profit EUR 48,000 in the latest tax notice (EUR 4,000 a month), voluntary member, no sick pay, childless, age 35, no single client. The base of EUR 4,000 lies between the minimum base and the ceiling. Health EUR 4,000 x (14.0% + 2.9%) = EUR 676.00. Care EUR 4,000 x 4.2% (childless) = EUR 168.00. Total EUR 844.00 a month. Not on the § 2 SGB VI list, so no pension duty; voluntary contributions are possible.

```oa-check
name: DE 2026 voluntary member, profit 48,000, childless, no sick pay
inputs:
  profit_year: 48000
  reference_month: 3955
  ceiling_month: 5812.50
  extra_rate: 2.9
steps:
  - min_base: reference_month / 3
  - base: clamp(profit_year / 12, min_base, ceiling_month)
  - health: round(base * (14.0 + extra_rate) / 100, 2)
  - care: round(base * 4.2 / 100, 2)
  - total: health + care
expected:
  base: 4000
  health: 676.00
  care: 168.00
  total: 844.00
```

**Example 2: yoga teacher in the first year, low income, one child.** Starts teaching on 1 March 2026, profit about EUR 1,000 a month, no insured staff, one child aged 10, voluntary health member without sick pay. Health: the base is lifted to the minimum of EUR 1,318.33, so health EUR 222.80 (check) and care at 3.6% EUR 47.46. Pension: a teacher with no insured staff is on the § 2 SGB VI list and EUR 1,000 is above the EUR 603 Minijob limit, so the work is not marginal. Register by the end of May 2026. In the start phase (to the end of 2029) the base is half the reference amount: EUR 1,977.50 x 18.6% = EUR 367.82 a month, or EUR 735.63 on application. Total EUR 638.08 a month on EUR 1,000 of profit, which is why the minimum bases matter.

```oa-check
name: DE 2026 yoga teacher start phase, profit 1,000 a month, one child
inputs:
  profit_month: 1000
  reference_month: 3955
  ceiling_month: 5812.50
  minijob: 603
  extra_rate: 2.9
steps:
  - min_base: reference_month / 3
  - base: clamp(profit_month, min_base, ceiling_month)
  - health: round(base * (14.0 + extra_rate) / 100, 2)
  - care: round(base * 3.6 / 100, 2)
  - above_marginal: max(0, profit_month - minijob)
  - pension: round(reference_month / 2 * 18.6 / 100, 2)
  - total: health + care + pension
expected:
  base: 1318.33
  health: 222.80
  care: 47.46
  above_marginal: 397
  pension: 367.82
  total: 638.08
```

## Ask the client first

- Employed, self-employed, or both? If both, which is the main occupation, and do you employ anyone above the Minijob level?
- If employed: regular yearly pay, and were you privately insured on 31 December 2002 because your pay was over that year's threshold?
- Health cover today: statutory fund (which, compulsory or voluntary, sick pay elected?) or private insurer? Since when?
- What exactly is your work: teaching, nursing or child care, midwifery, a craft in the Handwerksrolle, art or writing, home-based work, or work mostly for one client? When did it start? Is it your first self-employed activity?
- Children: how many under 25? Your age?
- Latest income tax notice, and expected income this year from all sources (business, job, capital, letting)?
- Just before starting, were you in compulsory unemployment insurance or drawing unemployment benefit? Hours a week in the business?
- Does the business pay fees to self-employed artists, designers, photographers, writers or other publicists?
- Has anyone already asked the pension insurer to decide whether a contract is employment?

**When to refuse or refer**

- Private health and care premiums, and any advice to move between private and statutory cover: the law makes the way back narrow (§ 6(3a), § 9 SGB V). Refer.
- Whether a contract is employment (status procedure) or whether the client works "essentially for one client": refer at once; the exposure is contributions back to the start of the work.
- Whether self-employment is the main occupation: the health fund decides case by case.
- Whether work is artistic or publicist: the KSK decides.
- A given fund's additional rate: take it from the fund. This skill carries only the average, marked "check".
- Accident insurance amounts: each insurer sets its own rates.
- Professional pension funds (Versorgungswerke) and their exemption procedure.
- Cross-border work, A1 certificates, and people insured abroad.
- Farmers and foresters (their own social insurance), civil servants.
- Pensioners, students, and people on benefits who are also self-employed: other base rules apply.
- Payroll (withholding, reports, Minijob flat rates, transition band, employer levies): `de-payroll`.
- The income tax computation: `de-einkommensteuer-freelancer`.

**Completion checklist**

- [ ] Status settled: employee, self-employed, or both; status procedure considered for one-client or client-integrated work.
- [ ] Health system known (statutory compulsory, statutory voluntary, private); sick pay election known.
- [ ] Base for a voluntary member from the latest tax notice, between EUR 1,318.33 and EUR 5,812.50 a month; the fund's own additional rate used, not the average.
- [ ] Care rate set by age and children under 25; proof of children given to the care fund.
- [ ] § 2 SGB VI list tested; three-month registration and exemption windows checked; start phase applied.
- [ ] KSK: conditions, income limit, 1 December estimate, half shares; levy duty for businesses that pay artists.
- [ ] Accident insurer notified within one week; owner's cover decided.
- [ ] Unemployment insurance on application decided within three months of starting.
- [ ] Each amount checked against the fund's or insurer's notice; no year total rebuilt from rates.
- [ ] Tax deduction entered with the § 10 EStG caps; figures marked "check" confirmed.

## Sources

| Source | URL | Read on |
|---|---|---|
| SGB IV (§§ 3-8, 7a, 20, 23, 24, 28h) | https://www.gesetze-im-internet.de/sgb_4/ | 2026-10-26 |
| SGB V (§§ 5, 6, 9, 44, 188, 223, 226, 234, 240-243, 249, 250, 257) | https://www.gesetze-im-internet.de/sgb_5/ | 2026-10-26 |
| SGB VI (§§ 1, 2, 4-7, 161, 165, 167-169, 190a, 197) | https://www.gesetze-im-internet.de/sgb_6/ | 2026-10-26 |
| SGB VII (§§ 2, 3, 6, 150, 152, 164, 192) | https://www.gesetze-im-internet.de/sgb_7/ | 2026-10-24 |
| SGB XI (§§ 20, 55, 57-59) | https://www.gesetze-im-internet.de/sgb_11/ | 2026-10-24 |
| SGB III (§§ 25, 28a, 341, 345b, 346, 349a) | https://www.gesetze-im-internet.de/sgb_3/ | 2026-10-24 |
| Künstlersozialversicherungsgesetz (§§ 1, 3, 11, 12, 15, 16, 16a, 24, 25, 27) | https://www.gesetze-im-internet.de/ksvg/ | 2026-10-26 |
| Künstlersozialabgabe-Verordnung 2024 (BGBl. 2023 I Nr. 240) | https://www.recht.bund.de/bgbl/1/2023/240/regelungstext.pdf | 2026-10-26 |
| Künstlersozialabgabe-Verordnung 2026 | https://www.gesetze-im-internet.de/ksabg2026v/BJNR0DC0A0025.html | 2026-10-26 |
| Sozialversicherungs-Rechengrößenverordnung 2026 | https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf?__blob=publicationFile&v=3 | 2026-10-24 |
| Beitragssatzbekanntmachung Rentenversicherung 2026 | https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html | 2026-10-24 |
| Pflegeversicherungs-Beitragssatzanpassungsverordnung 2025 | https://www.gesetze-im-internet.de/pbav_2025/__1.html | 2026-10-24 |
| Federal Health Ministry, Beiträge (2026 average additional rate 2.9%) | https://www.bundesgesundheitsministerium.de/beitraege | 2026-10-24 |
| Mindestlohnverordnung (MiLoV5) | https://www.gesetze-im-internet.de/milov5/__1.html | 2026-10-24 |
| VVG § 193; EStG § 10 | https://www.gesetze-im-internet.de/vvg_2008/__193.html | 2026-10-24 |

Not yet confirmed: the 2025 artists' levy rate (the ordinance setting it was not found; take it from the KSK notice); the due date of a voluntary health member's contribution (fund statute; ordinarily the 15th of the next month); the due date of unemployment insurance on application (agency notice); whether a lower proven income can be used in the pension start phase; whether the owner's own accident contribution is a business expense; the 2027 ceilings (next ordinance, expected late 2026); accident insurance rates (set by each insurer); each fund's own additional rate.
