---
name: germany-payroll
description: Use this skill whenever asked about German payroll processing for employees. Trigger on phrases like "German payroll", "Lohnsteuer", "Gehaltsabrechnung", "Brutto Netto Rechner", "Steuerklasse", "Sozialversicherung", "Arbeitnehmeranteil", "Arbeitgeberanteil", "Beitragsbemessungsgrenze", "payslip Germany", "Lohnabrechnung", "Nettolohn", "Solidaritätszuschlag", "Kirchensteuer", "Rentenversicherung", "Krankenversicherung", "Pflegeversicherung", "Arbeitslosenversicherung", "Minijob", "Midijob", "minimum wage Germany", "Mindestlohn", "Entgeltabrechnung", or any question about computing employee pay, withholding tax, or social contributions in Germany. This skill extends de-payroll.md with full payroll lifecycle coverage including mandatory benefits, payslip requirements, filing obligations, and employer cost analysis. ALWAYS read this skill before processing any German employee payroll.
version: 1.0
jurisdiction: DE
tax_year: 2026
last_updated: 2026-09-27
authored_by: OpenAccountants team
review_status: pending_review
trust_label: Written by the OpenAccountants team
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# German payroll 2026: the full cycle, from wage tax and social insurance to payslip, minimum wage and sick pay

## Scope

For employers, payroll clerks and employees checking a German payslip for pay periods in 2026. This is the full-cycle payroll Guide: besides the rules shared with `de-payroll`, it covers the payslip, the minimum wage duties, tax-free night, Sunday and holiday surcharges, sick pay and the maternity top-up paid through payroll, and the accident insurance annual report. Covered: wage tax (Lohnsteuer) by tax class and ELStAM through the finance ministry's program flow (PAP), solidarity surcharge and church tax, the new exemption for employees past the standard retirement age; the four social insurance branches (RV, KV, PV, AV) with shares and ceilings; Minijobs and the transition band; the wage tax return, contribution and DEÜV deadlines, year-end and late surcharges; and a short section for 2025 pay still being corrected.

The year: the 2026 PAP covers pay periods "die nach dem 31. Dezember 2025, aber vor dem 1. Januar 2027 enden" and one-time payments received in 2026 ([PAP 2026, Anlage 1](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2)). Social insurance values apply from 1 January 2026.

Not covered, see "When to refuse or refer": the self-employed (use `de-freelance-intake`), cross-border and treaty cases, managing directors whose insurance status is open, employer pensions (Versorgungsbezüge), benefits in kind and flat-rate taxes under § 37b and § 40 EStG, the miners' pension scheme, and the exact Midijob formulas. Also out of scope: annual leave entitlements, parental leave and Elterngeld, Krankengeld and Mutterschaftsgeld paid by the health fund, and the employee's own income tax return.

The employee owes the wage tax; the employer must withhold it at every wage payment ([§ 38 EStG](https://www.gesetze-im-internet.de/estg/__38.html)) and is liable for it ([§ 42d(1) EStG](https://www.gesetze-im-internet.de/estg/__42d.html)). The employer pays the total social insurance contribution and recovers the employee's share only by deduction from pay ([§ 28e SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28e.html), [§ 28g SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28g.html)).

## Ask the client first

- **ELStAM:** tax class, child counters, church, allowance or factor; first or further job?
- **Health insurance:** which fund and its own additional rate; or private, or voluntary member?
- **Children and age:** children under 25, proof given, employee 23 or older?
- **State of the place of employment** (church tax rate, Saxony rule).
- **Regular monthly pay and any other jobs or Minijobs.**
- **Standard retirement age** reached before this month?
- **One-time payments** in this run?
- **Hours and surcharges:** hours worked, hourly pay, and any night, Sunday or public holiday work?
- **Absence:** sick days (and since when, same illness before?) or a maternity protection period?
- **Sector** with the immediate-report duty (step 3)?
- **Wage tax paid over for 2025** (sets the filing period).

Defaults when an answer is missing, for an estimate only: unknown class, estimate in class I, but real payroll uses class VI while the employee is at fault for missing data ([§ 39c EStG](https://www.gesetze-im-internet.de/estg/__39c.html)); unknown church, none; unknown children, childless surcharge if 23 or older; unknown Saxony flag, outside Saxony; unknown insurance markers, insured in all branches; unknown additional rate, the average rate (never for a real payslip).

## The method, step by step

**Before the first payday**

1. **Employer number.** Before the first registration, apply electronically to the Federal Employment Agency (its Betriebsnummern-Service) for a Betriebsnummer for each place of employment; separate numbers for different activities or municipalities ([§ 18i SGB IV](https://www.gesetze-im-internet.de/sgb_4/__18i.html)).
2. **Status.** Decide Minijob, short-term job, transition band, normal employment, or pay above the compulsory health insurance threshold. Add up several jobs as [§ 8(2) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__8.html) and [§ 20(2) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__20.html) say.
3. **Immediate report in listed sectors.** Construction, hospitality, passenger transport, haulage and logistics (including platform delivery), fairground work, building cleaning, trade-fair construction, meat industry (not the butchers' trade, "mit Ausnahme des Fleischerhandwerks"), prostitution, security, hairdressing and cosmetics: report the start day to the pension insurers' data office "spätestens bei dessen Aufnahme" ([§ 28a(4) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28a.html)). It does not replace the registration in step 6.
4. **Wage tax data.** Take the tax ID, date of birth, and whether this is the first or a further job; retrieve the ELStAM, enter them in the payroll account, and call up changes "monatlich" ([§ 39e(5) EStG](https://www.gesetze-im-internet.de/estg/__39e.html)). Missing data by the employee's fault: class VI. A technical fault or a reason the employee is not responsible for: the expected class for at most three calendar months ([§ 39c(1) EStG](https://www.gesetze-im-internet.de/estg/__39c.html)).
5. **Payroll account.** One Lohnkonto per employee and year at the place of business, recording pay (tax-free pay included) and tax withheld at every payment; keep it to the end of the sixth calendar year after the last entry ([§ 41(1) EStG](https://www.gesetze-im-internet.de/estg/__41.html)). For social insurance, keep pay records per employee and year in Germany and in German until the end of the calendar year after the last audit; an employer without a seat in Germany appoints an authorised person there ([§ 28f(1), (1b) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28f.html)).
6. **Registration** with the collecting office: the employee's health fund, or the Minijob-Zentrale for a Minijob ([§ 28i SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28i.html)). Deadlines for this and every later report are in "Filing and payment".

**Every pay period**

7. **Wage tax.** Take out tax-free pay first (such as the Aktivrente). Run the 2026 PAP on the rest, then the surcharge and, for church members, church tax on the base BK. One-time payments use the annual method.
8. **Contributions.** Cap pay at each branch's monthly ceiling, apply the shares, deduct the employee's. A missed deduction can be made up only at the next three payments, later only if the employer was not at fault ([§ 28g SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28g.html)).
9. **Employer-only levies.** U1 and U2 at the fund's rates, the insolvency levy, accident insurance.
10. **Minimum wage and absences.** Check pay per hour worked against the minimum wage, keep working-time records where § 17 MiLoG requires them, and pay sick pay, surcharges and the maternity top-up as set out in "Full cycle"; claim U1 or U2 refunds.
11. **Payslip.** Give the employee a pay statement in text form with the § 1 EBV contents ("Full cycle").
12. **Contribution statement and payment** to each collecting office, then the **wage tax return and payment** to the tax office, by the deadlines in "Filing and payment".

**Changes and year-end**

13. **Change reports and the annual report** (DEÜV), and the accident insurance annual report.
14. **Wage tax certificate**: close the payroll account, send it electronically, give the employee a copy.
15. **Annual adjustment** where compulsory and not barred (boundary table).

What breaks when the order is wrong: without wage tax data the tax runs in class VI and is corrected later; a missed employee share is lost after three payments; a late contribution statement lets the fund estimate the pay ([§ 28f(3) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28f.html)).

## Figures for 2026: wage tax

All amounts are yearly unless the row says otherwise. The employer uses them through the PAP, which annualises the period's pay and divides the tax back.

| What | 2026 value | Source |
| --- | --- | --- |
| Basic allowance: no tax on a taxable amount up to | EUR 12,348 | [§ 32a(1) EStG](https://www.gesetze-im-internet.de/estg/__32a.html) |
| First progressive zone | EUR 12,349 to EUR 17,799 | Same |
| Second progressive zone | EUR 17,800 to EUR 69,878 | Same |
| Third zone: factor 0.42 less a fixed amount | EUR 69,879 to EUR 277,825 | Same |
| Top zone: factor 0.45 less a fixed amount | from EUR 277,826 | Same |
| Employee lump sum (ANP), classes I to V | EUR 1,230 | [§ 9a EStG](https://www.gesetze-im-internet.de/estg/__9a.html) |
| Special expenses lump sum (SAP), classes I to V | EUR 36 | [§ 10c EStG](https://www.gesetze-im-internet.de/estg/__10c.html) |
| Single parent relief (EFA), class II, one child | EUR 4,260 | [§ 24b(2) EStG](https://www.gesetze-im-internet.de/estg/__24b.html) |
| Child allowances per counter, classes I to III (only for the surcharge and church tax base) | EUR 9,756 | [PAP 2026](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2) |
| Child allowances per counter, class IV | EUR 4,878 | Same sentence |
| Classes V and VI: minimum tax as a share of the taxable amount | 14% | [§ 39b(2) sentence 7 EStG](https://www.gesetze-im-internet.de/estg/__39b.html) |
| Classes V and VI: at most this share above EUR 14,071; exactly this share above EUR 34,939 | 42% | Same |
| Classes V and VI: share above EUR 222,260 | 45% | Same |
| Solidarity surcharge on the wage tax | 5.5% | [§ 4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html) |
| Surcharge at most this share of the excess over the limit | 11.9% | Same |
| Surcharge exemption limit, classes other than III | EUR 20,350 | [§ 3(3) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html) |
| Surcharge exemption limit, class III | EUR 40,700 | Same |
| Church tax on the church tax base, by state | 8% or 9% | [Finance ministry booklet](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Broschueren_Bestellservice/steuern-von-a-z.pdf?__blob=publicationFile&v=9) |
| Vorsorgepauschale: the unemployment part counts only so far as it and the health and care parts together do not exceed | EUR 1,900 | [§ 39b(2) sentence 5 no. 3(e) EStG](https://www.gesetze-im-internet.de/estg/__39b.html) |
| Reduced health rate used for the Vorsorgepauschale (full rate) | 14.0% | [§ 243 SGB V](https://www.gesetze-im-internet.de/sgb_5/__243.html) |
| Tax-free pay past the standard retirement age (Aktivrente), per year | EUR 24,000 | [§ 3 no. 21 EStG](https://www.gesetze-im-internet.de/estg/__3.html) |
| The same, per month in payroll | EUR 2,000 | [Finance ministry FAQ](https://www.bundesfinanzministerium.de/Content/DE/FAQ/FAQ-zur-Aktivrente.html) |

Which states charge the lower church tax rate is state law and is not printed on an allowed federal page; the common reading is Bavaria and Baden-Württemberg at the lower rate and the other states at the higher one (check with the state's church tax law).

## Wage tax: how the 2026 program works

### Tax classes

| Class | Who ([§ 38b EStG](https://www.gesetze-im-internet.de/estg/__38b.html)) | What the PAP builds in |
| --- | --- | --- |
| I | Single; married, widowed or divorced people who do not meet III or IV; people with limited tax liability | Basic tariff, ANP, SAP, Vorsorgepauschale |
| II | As I, when the single parent relief applies | As I plus EFA for one child |
| III | Married, both resident, not permanently separated, and the spouse is in V on joint application; also the widowed in the year after the death | Splitting: tax on half the amount, doubled |
| IV | Married, both resident, not permanently separated, the default for couples; on application with a factor ([§ 39f EStG](https://www.gesetze-im-internet.de/estg/__39f.html)) | Basic tariff; with the factor the tax is multiplied by it |
| V | The spouse of a class III employee | Special method for V and VI, with ANP, SAP |
| VI | Second and further jobs; missing wage tax data by the employee's fault | Special method, no ANP, no SAP, no child allowance |

Extra child amounts for single parents with more than one child, and other allowances, reach payroll only as an allowance in the ELStAM ([§ 39a EStG](https://www.gesetze-im-internet.de/estg/__39a.html)).

### The order of the calculation

1. **Annualise.** Monthly pay times 12; weekly pay times 360/7; daily pay times 360 ([§ 39b(2) EStG](https://www.gesetze-im-internet.de/estg/__39b.html)).
2. **Taxable amount.** Deduct any pension allowance and old-age relief, deduct or add the ELStAM allowance or added amount, deduct the fixed amounts of the class (ANP, SAP, EFA), deduct the Vorsorgepauschale. Round down to whole euros.
3. **Tariff.** Classes I, II and IV: tariff below. Class III: tariff on half, doubled. Classes V and VI: special method.
4. **Back to the period.** Take 1/12, 7/360 or 1/360 of the yearly tax; drop parts of a cent.
5. **Surcharge and church tax.** Run the calculation again with the child allowances deducted. That second tax (JBMG) is the base for the surcharge and for church tax (BK). The wage tax itself does not fall because of children ([§ 51a(2a) EStG](https://www.gesetze-im-internet.de/estg/__51a.html)).

PAP inputs that change the result most often (2026 PAP, section 3.1):

| Input | Meaning |
| --- | --- |
| KRV | 0 = in the statutory pension scheme (or a professional scheme); 1 = otherwise |
| ALV | New in 2026: 0 = in unemployment insurance; 1 = otherwise |
| PKV | 0 = statutory health insurance; 1 = private only (the value 2 no longer exists) |
| KVZ | Full additional rate of the employee's own fund, two decimals; the PAP halves it |
| PVZ / PVA | PVZ = 1: childless surcharge; PVA = number of reductions (0 to 4) for children two to five |
| PVS | 1 = place of employment in Saxony |

### Tariff formula 2026 (UPTAB26)

~~~
X = taxable amount, rounded down to whole euros (class III: half of it)
X up to 12348:            ST = 0
X up to 17799:            Y = (X - 12348) / 10000;  ST = (914.51 * Y + 1400) * Y
X up to 69878:            Z = (X - 17799) / 10000;  ST = (173.10 * Z + 2397) * Z + 1034.87
X up to 277825:           ST = 0.42 * X - 11135.63
above:                    ST = 0.45 * X - 19470.38
ST is rounded down to whole euros; class III: ST times 2
~~~

Classes V and VI ([§ 39b(2) sentence 7 EStG](https://www.gesetze-im-internet.de/estg/__39b.html); 2026 PAP, W1STKL5 = 14071, W2STKL5 = 34939, W3STKL5 = 222260). Never apply the plain tariff to V or VI.

~~~
UP5-6(Z):  ST = 2 * (tariff(floor(Z * 1.25)) - tariff(floor(Z * 0.75)))
           ST = the higher of ST and floor(Z * 0.14)
MST5-6(X): if X > W2STKL5:
               ST = UP5-6(W2STKL5)
               if X > W3STKL5: ST = ST + floor((W3STKL5 - W2STKL5) * 0.42) + floor((X - W3STKL5) * 0.45)
               else:           ST = ST + floor((X - W2STKL5) * 0.42)
           else:
               ST = UP5-6(X)
               if X > W1STKL5: ST = the lower of ST and UP5-6(W1STKL5) + floor((X - W1STKL5) * 0.42)
~~~

### Vorsorgepauschale (insurance deduction inside the tax)

It stands for the employee's own contributions. The 2026 text has five parts ([§ 39b(2) sentence 5 no. 3 EStG](https://www.gesetze-im-internet.de/estg/__39b.html)):

- **Pension:** pay up to the pension ceiling times the employee pension share, unless the employee is not in the statutory scheme (PAP marker KRV = 1).
- **Health:** pay up to the health ceiling times half the reduced health rate plus half the fund's own additional rate. The PAP writes it as "KVSATZAN = KVZ/2/100 + 0,07". It is not the rate the employee pays, which is built on the general rate.
- **Care:** pay up to the health ceiling times the employee care share from the social insurance table.
- **Private insurance:** instead of health and care, the monthly private premiums from the ELStAM less the tax-free employer subsidy (classes I to V only).
- **Unemployment:** pay up to the pension ceiling times the employee share, only if insured (ALV = 0) and not in class VI, and only so far as it and the health and care parts together do not pass the cap in the table. Once health and care alone exceed the cap, the unemployment part adds nothing; health and care still count in full.

There is no minimum Vorsorgepauschale in 2026. The PAP rounds the Vorsorgepauschale up to whole euros. The additional rate entered is the full rate of the employee's own fund: "Der durchschnittliche Zusatzbeitragssatz ist unmaßgeblich", except for the groups of § 242(3) SGB V, where the average rate counts (the 2026 PAP). Severance within § 24 no. 1 EStG is left out of the insurance parts.

### Solidarity surcharge and church tax

- No surcharge while the yearly base does not exceed the exemption limit. Above it, the surcharge is the lower of the full rate on the base and the mitigation share of the excess, so it phases in ([§ 4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html)).
- The period limit is the matching fraction of the yearly one: 1/12, 7/360 or 1/360 ([§ 3(4) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html)).
- One-time payments: surcharge only if the year's tax with the payment, worked out with child allowances, exceeds the limit; then the full rate, with no mitigation ([§ 3(4a) SolzG](https://www.gesetze-im-internet.de/solzg_1995/__3.html), [§ 4 SolzG](https://www.gesetze-im-internet.de/solzg_1995/__4.html)).
- Church tax only for members of a church that levies it (PAP input R above 0), at the state rate on BK. Caps and mixed-faith couples are state law.

### One-time payments (sonstige Bezüge)

Bonuses, holiday and Christmas pay, back pay for earlier years and severance are taxed by the annual method of [§ 39b(3) EStG](https://www.gesetze-im-internet.de/estg/__39b.html):

1. Yearly tax on the expected annual pay without the payment.
2. Yearly tax on that pay plus the payment.
3. Withhold the difference.

If the employee has not handed in the certificates of earlier employers this year, scale the current pay up for those months, mark the payroll account with the capital letter S, and the employee must then file a return ([§ 46(2) no. 5a EStG](https://www.gesetze-im-internet.de/estg/__46.html)). The one-fifth relief of § 34 EStG for severance is not applied in payroll since 2025; the 2026 PAP covers only "§ 39b Absatz 3 Satz 1 bis 8 EStG". The employee claims it, if due, in the income tax return ([§ 34 EStG](https://www.gesetze-im-internet.de/estg/__34.html)).

### Tax-free pay past the standard retirement age (Aktivrente), new in 2026

- **Who.** Employees in a job under § 19(1) no. 1 EStG, from the month after they reach the standard retirement age of § 35 or § 235 SGB VI, where the employer owes pension contributions for that work ([§ 3 no. 21 EStG](https://www.gesetze-im-internet.de/estg/__3.html)). A pension need not be drawn. Minijobs, self-employment and civil service pay are not covered ([finance ministry FAQ](https://www.bundesfinanzministerium.de/Content/DE/FAQ/FAQ-zur-Aktivrente.html)).
- **How much.** Up to the monthly amount in the table; the yearly amount falls by one twelfth for each month the conditions are not met. Unused room does not move to another month; one-time payments are exempt only within the month's room; severance as a rule is not covered. Pay for periods before the qualifying month is never covered, whenever it is paid. Pay already tax-free under another rule does not use it (§ 3 no. 21 sentence 2).
- **Payroll.** The employer must apply it and leave the exempt pay out of the wage tax. Class VI only with the employee's confirmation that no other job uses it, kept in the payroll account. When a job ends or the employer changes mid-month, the amount is apportioned by days on a 30-day month; a new job started mid-month gets the full amount if the employee confirms in writing that no Aktivrente was used that month. Contributions are unchanged. See Case 5.

## Figures for 2026: social insurance

### Rates

| What | 2026 value | Source |
| --- | --- | --- |
| Pension insurance, full rate | 18.6% | [RVBeitrSBek 2026](https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html) |
| Pension, employee share (employer the same, "je zur Hälfte", [§ 168(1) no. 1 SGB VI](https://www.gesetze-im-internet.de/sgb_6/__168.html)) | 9.3% | [PAP 2026](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2) |
| Unemployment insurance, full rate | 2.6% | [§ 341(2) SGB III](https://www.gesetze-im-internet.de/sgb_3/__341.html) |
| Unemployment, employee share (employer the same, [§ 346(1) SGB III](https://www.gesetze-im-internet.de/sgb_3/__346.html)) | 1.3% | PAP 2026 |
| Health insurance, general rate, without the fund's additional rate | 14.6% | [§ 241 SGB V](https://www.gesetze-im-internet.de/sgb_5/__241.html) |
| Health: the fund's own additional rate on top; employer and employee each bear half of general and additional rate | fund's own rate | [§ 249(1) SGB V](https://www.gesetze-im-internet.de/sgb_5/__249.html) |
| Average additional rate for 2026 (planning value, and the rate that counts for the groups of § 242(3) SGB V) | 2.9% (check) | [Finance ministry monthly report](https://www.bundesfinanzministerium.de/Monatsberichte/Ausgabe/2026/02/Inhalte/Kapitel-2-Analysen/2-3-sollbericht-2026.html) |
| Care insurance, full rate | 3.6% | [§ 1 PBAV 2025](https://www.gesetze-im-internet.de/pbav_2025/__1.html) |
| Care, employee share outside Saxony, with one child (and employer share outside Saxony) | 1.8% | PAP 2026; [§ 58(1) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__58.html) |
| Childless surcharge, employee only, from the month after turning 23 | 0.6 points | [§ 55(3) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__55.html) |
| Reduction per child from the second to the fifth, while under 25, employee share only | 0.25 points | Same |
| Care, employee share in Saxony, with one child | 2.3% | PAP 2026; [§ 58(3) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__58.html): employees bear "1 vom Hundert allein" |

The official notice of the average additional rate is published in the Federal Gazette, which is not an allowed source for this Guide; the figure above is the finance ministry's reading of the estimate. Confirm it before using it for the § 242(3) groups.

**Employee care share by children (derived from the rows above)**

| Children | Outside Saxony: employee | Outside Saxony: employer | Saxony: employee | Saxony: employer |
| --- | --- | --- | --- | --- |
| None, employee 23 or older | 2.4% | 1.8% | 2.9% | 1.3% |
| One child (at any age); or childless and under 23 | 1.8% | 1.8% | 2.3% | 1.3% |
| Two under 25 | 1.55% | 1.8% | 2.05% | 1.3% |
| Three under 25 | 1.3% | 1.8% | 1.8% | 1.3% |
| Four under 25 | 1.05% | 1.8% | 1.55% | 1.3% |
| Five or more under 25 | 0.8% | 1.8% | 1.3% | 1.3% |
| Source | [§ 55(3) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__55.html), [§ 58 SGB XI](https://www.gesetze-im-internet.de/sgb_11/__58.html), PAP 2026 | | | |

- **What counts.** Children who have turned 25 do not count toward the reductions; the reduction for a child ends at the end of the month it turns 25. Parents, at any age of the child, do not pay the surcharge. The surcharge does not apply to people born before 1 January 1940, to people doing military or civilian service, or to recipients of basic income support ([§ 55(3) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__55.html)).
- **Proof.** Parenthood and the number of children under 25 must be proven to the employer unless already known. Proof through the automated procedure, or other proof given within six months of the birth, counts from the month of birth; later proof counts from the month after it is given ([§ 55(3a) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__55.html)).
- **Saxony.** The test is the place of employment, not where the employee lives ([§ 58(3) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__58.html)).
- **Do not read the rate from § 55(1) SGB XI.** The statute page still prints the older rate "3,4 Prozent"; the current rate was set by regulation (PBAV 2025).

### Ceilings and thresholds

| What | 2026 per year | 2026 per month | Source |
| --- | --- | --- | --- |
| Pension and unemployment ceiling (BBG RV/AV) | EUR 101,400 | EUR 8,450 | [SVBezGrV 2026 § 4](https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf?__blob=publicationFile&v=3); AV uses the pension ceiling, [§ 341(4) SGB III](https://www.gesetze-im-internet.de/sgb_3/__341.html) |
| Health and care ceiling (BBG KV/PV), equal to the special threshold of § 6(7) SGB V | EUR 69,750 | EUR 5,812.50 | SVBezGrV 2026 § 2(2); [§ 55(2) SGB XI](https://www.gesetze-im-internet.de/sgb_11/__55.html) ties the care ceiling to it |
| General compulsory health insurance threshold (JAEG) | EUR 77,400 | EUR 6,450 | SVBezGrV 2026 § 2(1) |
| Special threshold, only for people privately insured on 31 December 2002 because of pay above the then threshold | EUR 69,750 | EUR 5,812.50 | SVBezGrV 2026 § 2(2) |

- **Ceilings cap contributions.** Pay above a branch's ceiling carries no contribution in that branch. One value for the whole country.
- **The threshold decides who may leave statutory health insurance.** When pay rises above the JAEG, compulsory insurance ends only at the end of that calendar year, and only if pay also exceeds the threshold for the next year ([§ 6(4) SGB V](https://www.gesetze-im-internet.de/sgb_5/__6.html)).
- **2027 change already enacted.** From 2027 the health ceiling will be the special threshold plus EUR 3,600 ([§ 223(4) SGB V](https://www.gesetze-im-internet.de/sgb_5/__223.html): "entspricht der um 3 600 Euro erhöhten Jahresarbeitsentgeltgrenze nach § 6 Absatz 7 im Jahr 2027"). The 2027 amounts are set by regulation in late 2026 (check).

### Contributions in practice

- **Base.** For each branch: pay for the period, capped at that branch's monthly ceiling. Apply the employee and employer shares from the tables. Round each amount to the cent.
- **Several jobs.** If pay from several insured jobs together passes a ceiling, each pay is first cut to the ceiling and then reduced in proportion so that together they reach the ceiling ([§ 22(2) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__22.html)). The second employer does not stop paying.
- **One-time payments.** They belong to the period in which they are paid and carry contributions only as far as pay so far in the year has not used up the pro-rata yearly ceiling. A payment from 1 January to 31 March that would pass that ceiling goes to the last period of the previous year, if the same employer employed the person then. For those compulsorily insured in health insurance the health ceiling is the test ([§ 23a SGB IV](https://www.gesetze-im-internet.de/sgb_4/__23a.html)).
- **Employees past the standard retirement age.** Drawing a full old-age pension after reaching that age makes the job pension-free, but the employer still pays its half ([§ 172(1) SGB VI](https://www.gesetze-im-internet.de/sgb_6/__172.html)); unemployment insurance works the same way after that age ([§ 346(3) SGB III](https://www.gesetze-im-internet.de/sgb_3/__346.html)). Where no employer pension contribution is due, the Aktivrente does not apply.

### Employer-only levies

| Levy | Rate | Base and rule |
| --- | --- | --- |
| U1 (continued sick pay) | Set by each health fund | Only employers with, as a rule, not more than 30 employees, apprentices not counted; the statute refunds 80% of continued pay ([§ 1(1) AAG](https://www.gesetze-im-internet.de/aufag/__1.html)) |
| U2 (maternity costs) | Set by each health fund | All employers, no size limit ([§ 1(2) AAG](https://www.gesetze-im-internet.de/aufag/__1.html)) |
| Insolvency levy | 0.15% | [§ 360 SGB III](https://www.gesetze-im-internet.de/sgb_3/__360.html); not for private households or public bodies ([§ 358 SGB III](https://www.gesetze-im-internet.de/sgb_3/__358.html)) |
| Accident insurance | Billed by the Berufsgenossenschaft after the year | Total pay, hazard class and the insurer's own factor |

U1, U2 and the insolvency levy are charged on the pay on which pension contributions are worked out ([§ 7(2) AAG](https://www.gesetze-im-internet.de/aufag/__7.html), [§ 358(2) SGB III](https://www.gesetze-im-internet.de/sgb_3/__358.html)).

## Minijobs, short-term jobs and the transition band

| What | 2026 value | Source |
| --- | --- | --- |
| Minimum wage per hour from 1 January 2026 | EUR 13.90 | [MiLoV5](https://www.gesetze-im-internet.de/milov5/__1.html) |
| Minijob limit per month: minimum wage times 130, divided by 3 (EUR 602.33), rounded up to whole euros | EUR 603 | [§ 8(1a) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__8.html); the finance ministry names the band as "603,01 € - 2.000 €" ([FAQ](https://www.bundesfinanzministerium.de/Content/DE/FAQ/FAQ-zur-Aktivrente.html)) |
| Minimum wage from 1 January 2027 | EUR 14.60 | MiLoV5 |
| Employer's flat health contribution, commercial Minijob, if the Minijobber is in statutory health insurance | 13% | [§ 249b SGB V](https://www.gesetze-im-internet.de/sgb_5/__249b.html) |
| Employer's flat pension contribution, commercial Minijob | 15% | [§ 172(3) SGB VI](https://www.gesetze-im-internet.de/sgb_6/__172.html) |
| Minijobber's own pension share (full rate less the employer's flat share) | 3.6% | Derived: 18.6% less 15% |
| Private household Minijob: employer's flat health and pension contributions, each | 5% | § 249b SGB V and § 172(3a) SGB VI |
| Uniform flat tax where flat or Minijob pension contributions are paid (covers wage tax, surcharge and church tax) | 2% | [§ 40a(2) EStG](https://www.gesetze-im-internet.de/estg/__40a.html) |
| Flat tax on a Minijob without those contributions | 20% | § 40a(2a) EStG |
| Flat tax for short-term staff | 25% | § 40a(1) EStG |
| Short-term flat tax: work only occasional, not regularly recurring ("gelegentlich, nicht regelmäßig wiederkehrend"), not longer than 18 consecutive working days, and pay per working day on average not above | EUR 150 | § 40a(1) EStG (or the job is needed at once at an unforeseeable time) |
| No 25% (or farm 5%) flat tax if average pay per hour is above | EUR 19 | § 40a(4) no. 1 EStG; also barred where the same employer pays the person other wages taxed by the ELStAM (§ 40a(4) no. 2) |
| Upper limit of the transition band, regular pay per month (all jobs together) | EUR 2,000 | [§ 20(2) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__20.html) |
| Factor F is this value divided by the total contribution rate | 28% | § 20(2a) SGB IV |
| Total contribution rate 2026: 18.6 + 3.6 + 2.6 + 14.6 + 2.9 | 42.3% (check) | Derived from the rates table; § 20(2a) defines the sum |
| Factor F 2026: 28 / 42.3 | 0.6619 (check) | Derived; the labour ministry publishes it in the Federal Gazette |
| Apprentices: employer bears the whole contribution if monthly pay is not above | EUR 325 | § 20(3) SGB IV |

**Minijob rules**

- **Regular pay.** The limit is on regular monthly pay. An unforeseeable overrun in not more than two calendar months within a twelve-month period, each time by up to the limit itself, does not end the Minijob ([§ 8(1b) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__8.html)).
- **Several jobs.** Several Minijobs are added together. One Minijob beside a main insured job stays separate; every further Minijob is added to the main job ([§ 8(2) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__8.html)).
- **Pension duty is the rule.** A Minijobber is compulsorily insured in pension insurance and pays the own share unless they apply, in writing or electronically, to be released ([§ 6(1b) SGB VI](https://www.gesetze-im-internet.de/sgb_6/__6.html)). If released, the employer still pays its flat share.
- **Flat tax is an option.** The employer may instead tax the pay by the ELStAM. The 2% flat tax is collected by Deutsche Rentenversicherung Knappschaft-Bahn-See, the Minijob-Zentrale ([§ 40a(6) EStG](https://www.gesetze-im-internet.de/estg/__40a.html)); the 20% and 25% flat taxes are declared with the wage tax return.
- **Short-term jobs.** A job limited in advance to three months or 70 working days in a calendar year is contribution-free unless done as a profession with pay above the Minijob limit ([§ 8(1) no. 2 SGB IV](https://www.gesetze-im-internet.de/sgb_4/__8.html)). The social insurance test and the 25% tax test are different tests.
- **No Aktivrente on a Minijob.**

**Transition band (Midijob)**

- Regular monthly pay above EUR 603 and not above EUR 2,000; with several jobs the total counts ([§ 20(2) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__20.html)).
- Normal wage tax by the ELStAM.
- Contributions are worked out on reduced bases by two formulas in § 20(2a) SGB IV: one for the total contribution, one for the employee's share, which is half of the contribution on the second base. The employer bears the rest ([§ 249(3) SGB V](https://www.gesetze-im-internet.de/sgb_5/__249.html), [§ 346(1a) SGB III](https://www.gesetze-im-internet.de/sgb_3/__346.html)). The statute page prints the formulas as images; take them from there or from payroll software, not from memory.
- Not for apprentices.

## Full cycle: payslip, minimum wage, surcharges, sick and maternity pay

### Payslip

- **Duty.** At every payment the employee gets a statement in text form showing at least the pay period and how pay is made up: kind and amount of surcharges, allowances, other pay, deductions, part payments and advances. None is needed if nothing has changed since the last proper one ([§ 108(1), (2) GewO](https://www.gesetze-im-internet.de/gewo/__108.html)).
- **Contents** of the pay certificate for every pay period ([§ 1 EBV](https://www.gesetze-im-internet.de/entgbv/__1.html), [§ 2 EBV](https://www.gesetze-im-internet.de/entgbv/__2.html)): employer name and address; employee name, address, date of birth and pension insurance number; start date (and end date on the last one); pay period with tax days and social insurance days; tax class and factor, child allowances, church tax data, any allowance or added amount, tax ID; contribution group key and collecting office; care code (0 childless, 1 to 5 children counted, a code for proven parenthood); transition band or multiple jobs where so; every item of pay and deduction by name and amount, regular or one-off, and whether it counts for taxable pay, social insurance gross and total gross; taxable pay, social insurance gross, total gross and flat-taxed pay by legal basis; wage tax, church tax and surcharge, and the employee's contributions, split regular and one-off; net pay; employer subsidies to voluntary or private insurance; other deductions such as advances or garnishments; the amount paid out. The employee may black out the church tax data.

### Minimum wage

| What | 2026 | Source |
| --- | --- | --- |
| Minimum wage per hour worked | EUR 13.90 | [MiLoV5](https://www.gesetze-im-internet.de/milov5/__1.html) |
| Paid at the agreed date, and at the latest | last bank working day (Frankfurt am Main) of the month after the work | [§ 2(1) MiLoG](https://www.gesetze-im-internet.de/milog/__2.html) |
| Hours on a written working-time account, per month at most | 50% of contractual hours, balanced within twelve months | § 2(2) MiLoG |
| Working-time records for Minijobs, short-term jobs and § 2a SchwarzArbG sectors | start, end and length by the seventh day after the work; keep at least two years | [§ 17(1) MiLoG](https://www.gesetze-im-internet.de/milog/__17.html) |

Not covered by the minimum wage ([§ 22 MiLoG](https://www.gesetze-im-internet.de/milog/__22.html)): under-18s without completed vocational training; apprentices; volunteers; compulsory internships, and orientation or study-accompanying internships of up to three months; formerly long-term unemployed people in their first six months. Sector minimum wages can be higher.

### Tax-free night, Sunday and holiday surcharges

| Surcharge on basic pay, for work actually done, paid on top of basic pay | Tax-free up to | Source |
| --- | --- | --- |
| Night work, 20:00 to 06:00 | 25% | [§ 3b EStG](https://www.gesetze-im-internet.de/estg/__3b.html) |
| Night work 00:00 to 04:00, if the shift began before midnight | 40% | § 3b(3) EStG |
| Sunday work | 50% | § 3b(1) EStG |
| Public holidays, and 31 December from 14:00 | 125% | § 3b(1) EStG |
| 24 December from 14:00, 25 and 26 December, 1 May | 150% | § 3b(1) EStG |
| Hourly basic pay counted for the tax exemption, at most | EUR 50 | § 3b(2) EStG |
| Contribution-free only where the hourly pay the surcharge is based on is not above | EUR 25 | [§ 1(1) no. 1 SvEV](https://www.gesetze-im-internet.de/svev/__1.html) |

The two caps differ: a surcharge can be tax-free and still carry contributions. Public holidays are those at the place of work.

### Sick pay and the maternity top-up

- **Continued pay in sickness.** Up to six weeks per incapacity, at the pay for regular working time without overtime pay, once the job has lasted four weeks without a break. The same illness again gives a new six weeks only after six months without incapacity from it, or twelve months after the first incapacity from it began ([§ 3 EntgFG](https://www.gesetze-im-internet.de/entgfg/__3.html), [§ 4 EntgFG](https://www.gesetze-im-internet.de/entgfg/__4.html)). Small employers in U1 get part of it back (80% under the statute).
- **Maternity top-up.** For the protection periods before and after the birth and the day of birth, the employer pays the difference between EUR 13 and the average net pay per calendar day of the last three settled months before the protection period ([§ 20(1) MuSchG](https://www.gesetze-im-internet.de/muschg_2018/__20.html)). With several employers, each pays its share. U2 refunds it in full ([§ 1(2) AAG](https://www.gesetze-im-internet.de/aufag/__1.html)).

## Boundaries and exceptions

| Situation | Rule | Source |
| --- | --- | --- |
| Monthly pay exactly EUR 603 | Minijob ("nicht übersteigt"); from EUR 603.01 transition band | § 8(1) no. 1 and § 20(2) SGB IV |
| Monthly pay exactly EUR 2,000 | Still transition band ("nicht übersteigen") | § 20(2) SGB IV |
| Wage tax for the previous year exactly EUR 1,080 | Yearly return; above it quarterly | § 41a(2) EStG |
| Wage tax for the previous year exactly EUR 5,000 | Quarterly return; above it monthly | § 41a(2) EStG |
| Business did not exist all last year | Convert last year's wage tax to a full year; a new business uses the first full month times 12 | § 41a(2) EStG |
| Surcharge base exactly at the limit | No surcharge ("übersteigt") | § 3(3) SolzG |
| Employee turns 23 in the month | Surcharge from the month after | § 55(3) SGB XI |
| Child turns 25 in the month | Reduction until the end of that month | § 55(3) SGB XI |
| Standard retirement age reached in April | Aktivrente from May | § 3 no. 21 EStG |
| Employer with exactly 30 employees | Still in U1 ("nicht mehr als 30") | § 1(1) AAG |
| Employer with ten or more employees on 31 December | Annual adjustment compulsory, unless barred | § 42b(1) EStG |
| Annual adjustment allowed and barred | Only for employees employed by this employer for the whole year. Barred (§ 42b(1) sentence 3 nos. 1 to 6): the employee applies against it; classes V or VI in the year; II, III or IV for only part of the year; an allowance or added amount; the factor method; in the year short-time pay, qualification pay, a maternity pay top-up, compensation under the Infection Protection Act, § 3 no. 21 pay, or § 3 no. 28 or 28a top-ups; at least one capital letter U; Vorsorgepauschale parts only for part of the year, or a change of the additional rate; different care insurance reductions in the year; foreign employment income without German wage tax | [§ 42b(1) EStG](https://www.gesetze-im-internet.de/estg/__42b.html) |
| Late payment of wage tax by up to three days | No late-payment surcharge, except for payment in cash or by cheque (§ 224(2) no. 1 AO) | § 240(3) AO |
| Deadline falls on a Saturday, Sunday or public holiday | Moves to the next working day | [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) |

## Worked cases

Assumed inputs are labelled. Every other number comes from the tables above. Contributions are rounded to the cent.

### Case 1: class I, EUR 5,000 a month, childless, outside Saxony

| Item | Working | Amount |
| --- | --- | --- |
| Assumed inputs | age 30, no church, no children, place of employment in Hesse, fund additional rate 2.9%, EUR 60,000 for the year, no one-time payments | |
| Wage tax for the year | [PAP 2026 test table](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2), class I at EUR 60,000 (built with the same inputs); withhold one twelfth a month | EUR 9,389 |
| Solidarity surcharge | Wage tax below EUR 20,350 | none |
| Base, all branches | Below both monthly ceilings | EUR 5,000 |
| Employee pension | 9.3% | EUR 465.00 |
| Employee unemployment | 1.3% | EUR 65.00 |
| Employee health | (14.6% + 2.9%) / 2 = 8.75% | EUR 437.50 |
| Employee care | Childless, 2.4% | EUR 120.00 |
| Employee total | Sum of the four | EUR 1,087.50 |
| Employer | Pension EUR 465.00, unemployment EUR 65.00, health EUR 437.50, care 1.8% = EUR 90.00, insolvency levy 0.15% | EUR 7.50 levy, plus U1 and U2 at the fund's rates |

### Case 2: class III, EUR 9,000 a month, two children, Bavaria, church member

| Item | Working ([SVBezGrV 2026](https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf?__blob=publicationFile&v=3) ceilings) | Amount |
| --- | --- | --- |
| Assumed inputs | spouse in class V, children aged 8 and 12, place of employment Munich, fund additional rate 2.5%. Pay is above the JAEG of EUR 6,450 a month, so the employee is assumed to be a voluntary member of a statutory fund; the employee owes the whole health contribution to the fund and the employer pays, as a subsidy, what it would bear under compulsory insurance ([§ 257(1) SGB V](https://www.gesetze-im-internet.de/sgb_5/__257.html)); the net shares below are the same | |
| Employee pension | Capped at EUR 8,450; 9.3% | EUR 785.85 |
| Employee unemployment | EUR 8,450 at 1.3% | EUR 109.85 |
| Employee health | Capped at EUR 5,812.50; (14.6% + 2.5%) / 2 = 8.55% | EUR 496.97 |
| Employee care | EUR 5,812.50 at 1.55% (two children under 25) | EUR 90.09 |
| Employer | Pension EUR 785.85, unemployment EUR 109.85, health EUR 496.97; care EUR 5,812.50 at 1.8% | EUR 104.63 care |
| Wage tax | Splitting through the PAP; the two counters (EUR 9,756 each) lower only the surcharge and church tax base; church tax at the Bavarian rate (8%, check) on BK. The test table does not fit: it assumes the childless surcharge | run the PAP |

### Case 3: commercial Minijob at the limit

| Item | Working ([§ 249b SGB V](https://www.gesetze-im-internet.de/sgb_5/__249b.html), [§ 172(3) SGB VI](https://www.gesetze-im-internet.de/sgb_6/__172.html), [§ 40a(2) EStG](https://www.gesetze-im-internet.de/estg/__40a.html)) | Amount |
| --- | --- | --- |
| Assumed inputs | EUR 603 a month, statutory health insurance, no release from pension insurance, 2% flat tax | |
| Employer health | 13% of EUR 603 | EUR 78.39 |
| Employer pension | 15% | EUR 90.45 |
| Employer flat tax | 2% | EUR 12.06 |
| Minijobber's pension share, deducted | 3.6% | EUR 21.71 |
| At EUR 603.01 | Transition band: normal wage tax by the ELStAM, reduced contributions under § 20(2a) SGB IV | n/a |

### Case 4: second job in class VI, and the ministry's test table

| Annual gross pay ([PAP 2026, "Prüftabelle"](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2)) | Class I (= IV) | Class II | Class III | Class V | Class VI |
| --- | --- | --- | --- | --- | --- |
| EUR 20,000 | EUR 380 | EUR 0 | EUR 0 | EUR 2,234 | EUR 2,766 |
| EUR 60,000 | EUR 9,389 | EUR 8,091 | EUR 4,822 | EUR 15,364 | EUR 15,895 |
| EUR 100,000 | EUR 23,248 | EUR 21,634 | EUR 15,012 | EUR 30,157 | EUR 30,689 |

The table is built with ALV, KRV and PKV = 0, KVZ = 2,90 and the childless surcharge (class II without it). Software implementing the [2026 PAP](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026-anlage-1.pdf?__blob=publicationFile&v=2) must reproduce it, and should also pass these checks: the wage tax is the same with and without child counters, while the surcharge and BK never rise with them; the class V tax is never below 14% of the taxable amount and is above class I in every row; pay above both ceilings changes no contribution; a surcharge base just above the limit gives 11.9% of the excess, below 5.5% of the base, and nothing at or below the limit.

Second job (assumed: main job elsewhere, EUR 20,000 a year here): the table row gives the class VI tax against the class I tax at the same pay. Wages from two employers at once oblige the employee to file a return ([§ 46(2) no. 2 EStG](https://www.gesetze-im-internet.de/estg/__46.html)). If both jobs together pass a ceiling, both pays are reduced in proportion ([§ 22(2) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__22.html)).

### Case 5: Aktivrente from May 2026

| Item | Working ([§ 3 no. 21 EStG](https://www.gesetze-im-internet.de/estg/__3.html), [ministry FAQ](https://www.bundesfinanzministerium.de/Content/DE/FAQ/FAQ-zur-Aktivrente.html)) | Amount |
| --- | --- | --- |
| Assumed inputs | standard retirement age reached in April 2026; works on at EUR 2,500 a month; the employer owes pension contributions for the job | |
| January to April | Normal wage tax on EUR 2,500 | taxed |
| May to December, tax-free per month | Up to EUR 2,000 | EUR 2,000 |
| May to December, taxed per month | EUR 2,500 less EUR 2,000 | EUR 500 |
| Yearly room | EUR 24,000 less four twelfths | EUR 16,000 |
| FAQ variant: pay EUR 1,500, December bonus EUR 800 | Tax-free part of the bonus: EUR 2,000 less EUR 1,500 | EUR 500 |
| FAQ variant: taxed part of the bonus | EUR 1,500 + EUR 800 less EUR 2,000 | EUR 300 |
| Contributions | Due in full; the exemption is for tax only | unchanged |

### Case 6: filing period, deadlines and late payment

| Item | Working | Amount or date |
| --- | --- | --- |
| Assumed inputs | wage tax paid over for 2025 was EUR 4,200; EUR 1,275 of third-quarter wage tax paid on 30 October 2026; EUR 3,480 of contributions paid late | |
| Filing period 2026 | More than EUR 1,080, not more than EUR 5,000 ([§ 41a(2) EStG](https://www.gesetze-im-internet.de/estg/__41a.html)) | quarterly |
| Third-quarter deadline | 10 October 2026 is a Saturday ([§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html)) | Monday 12 October 2026 |
| Late-payment surcharge on wage tax | More than three days late, one month started; 1% of EUR 1,250 ([§ 240 AO](https://www.gesetze-im-internet.de/ao_1977/__240.html)) | EUR 12.50 |
| Late-payment surcharge on contributions, per month started | 1% of EUR 3,450 ([§ 24(1) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__24.html)) | EUR 34.50 |

## When to refuse or refer

- **Self-employed and freelancers.** Not payroll; use `de-freelance-intake`, and `de-social-contributions` for their own contributions.
- **Students and working students**, whose insurance rules differ, and **apprentices** paid up to the apprentice limit beyond the rule in the Minijob table.
- **Part-month pay periods** and part-month ceilings.
- **Cross-border work**, postings into or out of Germany, treaty relief (the ministry publishes a separate treaty routine), and foreign social security certificates.
- **Managing directors and shareholder-directors** of a GmbH or UG, and family members, until the insurance status has been decided (status procedure).
- **Employer pensions** (Versorgungsbezüge) and the old-age relief; company pension schemes.
- **Benefits in kind**, company cars, flat-rate wage tax under § 37b and § 40 EStG, tax-free allowances other than the Aktivrente and the § 3b surcharges.
- **Short-time pay, Krankengeld, Mutterschaftsgeld and parental leave**, beyond the employer's own sick pay, maternity top-up and reporting duties.
- **Midijob amounts.** This Guide gives the band and the factor, not the formulas.
- **Miners' pension scheme, civil servants,** and employees exempt from a branch.
- **Exact church tax** (state caps, mixed-faith couples).
- **Private household Minijobs** beyond the rates in the table (the household cheque procedure).
- **Sign-off.** Results are working papers. Payroll software that implements the PAP and a Steuerberater or payroll accountant (Lohnbuchhalter) should confirm them before use.

## Filing and payment

| Duty | Deadline | Source |
| --- | --- | --- |
| Wage tax return and payment, monthly filer (previous year's wage tax above EUR 5,000) | 10th of the next month | [§ 41a EStG](https://www.gesetze-im-internet.de/estg/__41a.html) |
| Quarterly filer (above EUR 1,080 and not above EUR 5,000) | 10 April, 10 July, 10 October, 10 January | § 41a EStG |
| Yearly filer (not above EUR 1,080) | 10 January of the next year | § 41a EStG |
| Deadline on a weekend or public holiday | Next working day | [§ 108(3) AO](https://www.gesetze-im-internet.de/ao_1977/__108.html) |
| Contribution statement | Two working days before the due date | [§ 28f(3) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28f.html) |
| Contributions | Third-last bank working day of the month worked; remainder the third-last bank working day of the next month | [§ 23(1) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__23.html) |
| Immediate report (listed sectors) | At the latest when work starts | [§ 28a(4) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28a.html) |
| Registration / de-registration | Next payroll run, at the latest six weeks after start or end | [§ 6](https://www.gesetze-im-internet.de/de_v/__6.html), [§ 8 DEÜV](https://www.gesetze-im-internet.de/de_v/__8.html) |
| Interruption report, only when pay stops for at least a full calendar month and the employee draws a listed benefit (for example sick pay from the fund), takes parental leave or does military service | Two weeks after the end of the first calendar month | [§ 9 DEÜV](https://www.gesetze-im-internet.de/de_v/__9.html) |
| Change of health fund, contribution group or person group key | De-registration and new registration within six weeks | [§ 12 DEÜV](https://www.gesetze-im-internet.de/de_v/__12.html) |
| Annual report for 2026 | First payroll run of 2027, at the latest 15 February 2027 | [§ 10 DEÜV](https://www.gesetze-im-internet.de/de_v/__10.html) |
| Special annual report to accident insurance for everyone employed and insured in 2026 | 16 February 2027 ("zum 16. Februar des Folgejahres") | [§ 28a(2a) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__28a.html) |
| Minimum wage paid | At the latest the last bank working day of the month after the work | [§ 2 MiLoG](https://www.gesetze-im-internet.de/milog/__2.html) |
| Wage tax certificate for 2026 | Last day of February 2027; 28 February 2027 is a Sunday, so Monday 1 March 2027 under § 108(3) AO (check with the tax office) | [§ 41b(1) EStG](https://www.gesetze-im-internet.de/estg/__41b.html) |

**Surcharges and liability**

- **Late payment of wage tax:** 1% of the amount due, rounded down to a multiple of EUR 50, for each month started; not for a delay of up to three days ([§ 240 AO](https://www.gesetze-im-internet.de/ao_1977/__240.html)).
- **Late filing of the wage tax return:** a late-filing surcharge is at the tax office's discretion; the compulsory amounts of § 152(5) AO do not apply to monthly, quarterly or yearly wage tax returns ([§ 152(8) AO](https://www.gesetze-im-internet.de/ao_1977/__152.html)).
- **Late contributions:** 1% of the arrears, rounded down to EUR 50, for each month started; not charged separately on arrears under EUR 150 ([§ 24(1) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__24.html)).
- **Liability:** the employer is liable for wage tax it should have withheld and paid over ([§ 42d(1) EStG](https://www.gesetze-im-internet.de/estg/__42d.html)).

### 2025 pay still being corrected

Pay for periods ending in 2025 is taxed with the amended 2025 PAP of 22 January 2025, which covers periods "die nach dem 31. Dezember 2024, aber vor dem 1. Januar 2026 enden" ([amended PAP 2025](https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-01-22-geaenderte-PAP-2025-anlage-1.pdf?__blob=publicationFile&v=2)). Do not use 2026 values for 2025 corrections.

| 2025 value | Amount | Source |
| --- | --- | --- |
| Basic allowance | EUR 12,096 | Amended PAP 2025 |
| Surcharge exemption limit (not class III) | EUR 19,950 | Same |
| Pension and unemployment ceiling, per year | EUR 96,600 | Same |
| Health and care ceiling, per year | EUR 66,150 | Same |
| Minimum wage 2025 | EUR 12.82 | [MiLoV4](https://www.gesetze-im-internet.de/milov4/__1.html) |
| Minijob limit 2025: 12.82 x 130 / 3 = EUR 555.53, rounded up | EUR 556 | [§ 8(1a) SGB IV](https://www.gesetze-im-internet.de/sgb_4/__8.html) |

The 2025 annual report was due by 15 February 2026 and the 2025 wage tax certificates by the last day of February 2026 (2 March 2026, as 28 February 2026 was a Saturday). A late or corrected certificate is still sent electronically. Employees with wages from two employers at once in 2025 must file a 2025 return ([§ 46(2) no. 2 EStG](https://www.gesetze-im-internet.de/estg/__46.html)).

## Completion checklist

- [ ] Status of each job decided (Minijob, short-term, transition band, normal, above the JAEG); several jobs added up.
- [ ] Immediate report sent where the sector requires it; registration within six weeks.
- [ ] Pay per hour checked against the minimum wage; working-time records kept where required; § 3b surcharges within both caps.
- [ ] Sick pay and maternity top-up paid and U1/U2 refunds claimed; payslip with the EBV contents issued.
- [ ] Accident insurance annual report by 16 February; social insurance pay records kept in Germany.
- [ ] ELStAM retrieved and changes called up monthly; class VI only where the law requires it.
- [ ] Aktivrente applied for employees from the month after the standard retirement age (not on Minijobs; class VI only with the written confirmation).
- [ ] Wage tax run through software implementing the 2026 PAP; test-table rows reproduced.
- [ ] Surcharge and church tax on the base with child allowances; church rate by the place of employment's state.
- [ ] Each branch capped at its own 2026 ceiling; care share set by children under 25, age and Saxony; proof of children on file.
- [ ] Health share built on the fund's own additional rate, not the average.
- [ ] One-time payments by the annual method; the March rule for contributions checked.
- [ ] Contribution statement two working days before the due date; payment by the third-last bank working day.
- [ ] Wage tax return and payment by the tenth after each period; filing period set from 2025 wage tax.
- [ ] Year-end: annual report by 15 February, certificates by the end of February, annual adjustment where compulsory and not barred.
- [ ] Figures marked "check" confirmed: average additional rate, factor F, the lower church tax states.

## Sources

- Income Tax Act (EStG) §§ 3, 9a, 10c, 24b, 32a, 38, 38b, 39a to 39f, 40a, 41 to 42d, 46, 51a: https://www.gesetze-im-internet.de/estg/
- Solidarity Surcharge Act §§ 3, 4: https://www.gesetze-im-internet.de/solzg_1995/
- Fiscal Code (AO) §§ 108, 152, 240: https://www.gesetze-im-internet.de/ao_1977/
- Social Code IV §§ 8, 20, 22, 23, 23a, 24, 28a, 28e to 28i; DEÜV §§ 6, 8, 9, 10, 12: https://www.gesetze-im-internet.de/sgb_4/ and https://www.gesetze-im-internet.de/de_v/
- Social Code V §§ 6, 223, 241, 243, 249, 249b; VI §§ 6, 168, 172; XI §§ 55, 58; III §§ 341, 346, 358, 360; AAG §§ 1, 7: https://www.gesetze-im-internet.de/
- Pension rate notice 2026 (RVBeitrSBek 2026), care rate regulation (PBAV 2025), minimum wage regulations (MiLoV4, MiLoV5): https://www.gesetze-im-internet.de/rvbeitrsbek_2026/BJNR1230A0025.html and https://www.gesetze-im-internet.de/pbav_2025/__1.html and https://www.gesetze-im-internet.de/milov5/__1.html
- Social insurance values regulation 2026 (SVBezGrV 2026), Federal Law Gazette 2025 I No. 278: https://www.recht.bund.de/bgbl/1/2025/278/regelungstext.pdf?__blob=publicationFile&v=3
- Finance ministry, PAP 2026 overview: https://www.bundesfinanzministerium.de/Content/DE/Downloads/Steuern/Steuerarten/Lohnsteuer/Programmablaufplan/2025-11-12-PAP-2026.html
- Finance ministry, Aktivrente FAQ: https://www.bundesfinanzministerium.de/Content/DE/FAQ/FAQ-zur-Aktivrente.html

This Guide is general information for 2026 and not tax, legal or payroll advice.

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
