---
name: dk-payroll
description: "Use this skill to run Danish payroll for 2026: registering as an employer on virk.dk, the monthly eIndkomst report and its 2026 deadlines (the 10th of the next month for small and medium employers, the last banking day of the month for large ones), the eSkattekort (hovedkort, bikort, frikort) and the forskudsopgørelse behind it, the withholding order (ATP, then 8% AM-bidrag, then A-skat at the trækprocent after the monthly fradrag), ATP of DKK 99 employee and DKK 198 employer a month, holiday pay under the Holiday Act (ferietillæg 1%, feriegodtgørelse 12.5%, FerieKonto), free car and free phone, payslips and penalties. Trigger phrases: lønkørsel, A-skat, am-bidrag, trækprocent, skattekort, eIndkomst, feriepenge, fri bil, Danish payroll. Out of scope: the employee's own tax computation (dk-income-tax), employer social contributions and Samlet Betaling (dk-social-contributions), self-employed B-tax (dk-income-tax), company tax (dk-corporate-tax)."
version: 0.1
jurisdiction: DK
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Denmark payroll: withholding, eIndkomst and holiday pay (2026)

This skill covers what an employer in Denmark withholds from wages each month, what it reports to eIndkomst, and when it pays. It links to the other Denmark skills and does not repeat them: `dk-income-tax` (the rates behind the trækprocent, the personal allowance, the employee's annual return and the self-employed), `dk-social-contributions` (employer contributions collected through Samlet Betaling, and social security for posted workers), `dk-corporate-tax` and `dk-vat-return`.

All figures are for the 2026 calendar year. Statute text was read on retsinformation.dk on 23 October 2026. Practice figures come from skat.dk, the Danish legal guide (Den juridiske vejledning, info.skat.dk), virk.dk and borger.dk, all read the same day.

## Who this applies to

- **Employers paying A-income.** Anyone who pays A-income (wages and most pay for personal work) must withhold provisional tax at each payment (kildeskatteloven, KSL, § 46(1)). Salary to domestic help in a private household is B-income, so it is not withheld or reported by the household ([skat.dk, Skat af ansattes løn](https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/skat-af-ansattes-loen)).
- **Registration first.** The employer registers as an employer on virk.dk and gets access to eIndkomst before the first pay run ([skat.dk, Hiring your first employee](https://skat.dk/en-us/businesses/employees-and-pay/hiring-your-first-employee)).
- **Foreign employers.** Pay from an employer with no Danish home (hjemting) is not A-income, unless the employer has a Danish permanent establishment (KSL § 44(b)). An employer outside the EU, in a country without a collection agreement with Denmark, pays A-income through a Danish representative (befuldmægtiget), who then does the withholding (KSL § 46(4)). A foreign business with a Danish CVR number for VAT is not a "Danish employer" for this purpose unless it is registered to withhold A-tax ([skat.dk, Skat af ansattes løn](https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/skat-af-ansattes-loen)).
- **Employees in scope.** Employees fully tax liable in Denmark, including those who work abroad for a Danish employer, are withheld on as normal. Pay for work done abroad by an employee who is not fully liable is not withheld on. The Øresund agreement has its own rules ([skat.dk, Skat af ansattes løn](https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/skat-af-ansattes-loen)).
- **Young employees.** From 1 January 2026, AM-bidrag is 0% of the base up to and including 31 December of the income year in which the person turns 17 (arbejdsmarkedsbidragsloven § 1, 2nd sentence, inserted by lov nr. 96 of 4 February 2025, § 1, in force for 2026). So nobody pays AM-bidrag before the year they turn 18, and someone who turns 18 at any point in 2026 pays AM-bidrag for all of 2026. The employer does not report field 16 for them, but still reports the pay in field 13 ([skat.dk, Skat af ansattes løn](https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/skat-af-ansattes-loen)). A business owner's own child who is under 15 when the income year starts does not pay tax on pay for helping in the business, and the business cannot deduct that pay (same page).
- **Not covered here.** Seafarers (DIS), the researcher and key-employee scheme in detail (KSL §§ 48 E and 48 F, see Cross-border points), share-based pay, termination payments, pensions paid out, public-sector pre-paid payroll, and a working spouse in a sole trader's business (see `dk-income-tax`). Refer them.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| AM-bidrag (labour market contribution), employee, on the AM base | 8% | 2026 | https://www.retsinformation.dk/eli/lta/2020/121 |
| AM-bidrag age rule: 0% up to and including the year the employee turns 17 (first paid in the year they turn 18) | from income year 2026 | 2026 | https://www.retsinformation.dk/eli/lta/2025/96 (AMBL § 1, 2nd sentence) |
| Withholding with no tax card retrieved (no fradrag) | 55% of the A-income | 2026 | https://www.retsinformation.dk/eli/lta/2024/460 (KSL § 48(8)) |
| General personal allowance (personfradrag), full-year, fully liable adult | DKK 54,100 (DKK 51,600 in 2025) | 2026 | https://skat.dk/en-us/individuals/tax-card |
| ATP, monthly paid, private employer, at least 117 hours a month: employee / employer / total | DKK 99.00 / 198.00 / 297.00 | 2026 | https://www.borger.dk/pension-og-efterloen/ATP-Livslang-pension-oversigt/atp-bidraget/atp-satser-for-privat-virksomhed |
| ATP, monthly paid, 78 to under 117 hours | DKK 66.00 / 132.00 / 198.00 | 2026 | same |
| ATP, monthly paid, 39 to under 78 hours | DKK 33.00 / 66.00 / 99.00 | 2026 | same |
| ATP, monthly paid, under 39 hours | DKK 0 | 2026 | same |
| ATP, 14-day paid, at least 54 hours | DKK 52.20 / 104.40 / 156.60 | 2026 | same |
| Large employer for deadlines: AM-bidrag over DKK 250,000 or A-tax over DKK 1 million in October 2024 to September 2025; otherwise small and medium (SMV) | as stated | 2026 | https://www.retsinformation.dk/eli/lta/2024/1040 (Opkrævningsloven § 2(6)) |
| Holiday entitlement | 5 weeks a year, earned at 2.08 days per month of employment | holiday year 1 Sep to 31 Aug | https://www.retsinformation.dk/eli/lta/2024/152 (Ferieloven §§ 4, 5) |
| Ferietillæg for employees with paid holiday | 1% of pay | 2026 | same (§ 16(1)) |
| Feriegodtgørelse for other employees | 12.5% of pay | 2026 | same (§ 16(2)) |
| Feriegodtgørelse a salaried employee may elect instead, before the holiday year | 12% | 2026 | same (§ 16(3)) |
| FerieKonto administration fee | DKK 4 per employee a month in which holiday pay is reported | 2026 | https://virk.dk/vejledning/feriepenge/fp-arbejdsgiver/ |
| Free car: share of the car's value (no split at DKK 300,000 from 2025) | 22.5% a year | 2026 | https://www.retsinformation.dk/eli/lta/2025/1500 (Ligningsloven § 16(4)) |
| Free car: minimum value of the car | DKK 160,000 | 2026 | same, and https://skat.dk/erhverv/ansatte-og-loen/personalegoder-naar-du-er-arbejdsgiver/fri-bil-til-dine-medarbejdere-firmabil |
| Free car: environmental supplement (miljøtillæg) | 7 x the annual periodic tax (700%) | 2026 | same |
| Free car: value after 36 months from first registration | 75% of the new-car price, not below DKK 160,000 | 2026 | same |
| Free phone (and data connection without access to the work network) | DKK 3,500 a year (DKK 3,300 in 2025); DKK 291.7 a month | 2026 | https://skat.dk/erhverv/ansatte-og-loen/personalegoder-naar-du-er-arbejdsgiver/fri-telefon-computer-og-internet-til-dine-ansatte |
| Researcher and key-employee scheme (KSL § 48 F) | A-tax 27% of cash pay, plus AM-bidrag, for at most 84 months | 2026 | https://www.retsinformation.dk/eli/lta/2024/460 |
| Researcher and key-employee scheme: minimum monthly pay for key employees (KSL § 48 E(3) no. 3), plus ATP | DKK 65,400 (DKK 78,000 in 2025) | 2026 | https://info.skat.dk/data.aspx?oid=1977289 |
| Fee for each provisional estimate (foreløbig fastsættelse) when a month is not reported | DKK 1,400 | 2026 | https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/saadan-indberetter-du-loen-eindkomst |
| Interest on late A-tax and AM-bidrag (Skattekonto) | 0.95% a month (basis rate 0.1% plus 0.85 points) | 2026 | https://skat.dk/en-us/businesses/payment-and-the-tax-account-skattekontoen/payments-to-your-tax-account and https://info.skat.dk/data.aspx?oid=2459995 |
| Interest on late ATP (Samlet Betaling) | 9.75% a year (1 January to 30 June 2026) | 2026 | https://virk.dk/vejledning/atp/atp-arbejdsgiver/ |
| Interest on late holiday pay to FerieKonto | 1.5% per started month | 2026 | https://www.retsinformation.dk/eli/lta/2024/152 (§ 31(3)) |

The rates behind each employee's trækprocent (bottom-bracket, middle-bracket, municipal and church tax) are in `dk-income-tax`. The employer does not compute them: it applies the rate and monthly deduction on the employee's eSkattekort.

## The taxable base

**The tax card (eSkattekort).** The employer retrieves the card electronically from Skattestyrelsen (KSL § 48(1)). There are three kinds ([skat.dk, The Danish tax card](https://skat.dk/en-us/individuals/tax-card); KSL § 48):

- **Hovedkort (primary card).** Used by one employer only. It shows a withholding rate (trækprocent) and a deduction (fradrag) for a month, 14 days, a week and a day (KSL § 48(3)). The deductions are a share of the allowances the employee is expected to have for the year, including the personal allowance.
- **Bikort (secondary card).** Used by every other payer. It shows a rate and no deduction, so tax is withheld on the whole amount.
- **Frikort (tax-exemption card).** No A-tax until the year's exemption amount is used up; then the payer withholds at the rate on the preliminary assessment. AM-bidrag is still withheld.

The card comes from the employee's preliminary income assessment (forskudsopgørelse) in TastSelv. If income changes, the employee updates it and the employer retrieves the new card. If no card has been retrieved, withhold 55% with no deduction (KSL § 48(8)). An employee may ask for a higher rate than the card shows (§ 48(9)).

**The withholding order each pay run.**

1. Start from gross cash pay for the period, plus the taxable value of benefits (free car, free phone, free board and lodging, health insurance and others listed in KSL § 49 A(2)).
2. Deduct the employee's ATP share and any contributions (employee and employer share) to a deductible employer-administered pension scheme. Field 13 is reported after these are subtracted ([eIndkomst reporting guide 8.2](https://info.skat.dk/data.aspx?oid=2233519); [skat.dk, Labour market contribution](https://skat.dk/en-us/individuals/labour-market-contribution)). ATP is left out of taxable income under PBL § 19(1) ([JV C.A.10.2.1.1.2.4](https://info.skat.dk/data.aspx?oid=2048235)). The pension contributions still carry AM-bidrag (AMBL § 2(1) no. 4; KSL § 49 A(3) no. 1), but the Danish pension fund, insurer or bank computes and withholds it, not the employer (KSL § 49 D(1)). For an approved pension provider elsewhere in the EU or EEA, the employer computes it (KSL § 49 D(4)).
3. AM-bidrag: 8% of that AM base (arbejdsmarkedsbidragsloven § 1). AM-bidrag comes off before A-tax ([skat.dk, start-up guide](https://skat.dk/erhverv/guides-og-webinarer-til-start-ups/start-up-med-skat/for-selskaber/ansatte/del-2-lav-en-loenseddel-og-bogfoer-loennen)).
4. A-income after AM-bidrag, less the period deduction on a hovedkort (none on a bikort).
5. A-tax: the trækprocent times that amount.
6. Net pay: gross cash pay less ATP, any employee pension contribution, AM-bidrag and A-tax. Benefits are not paid in cash, so their tax comes out of cash pay.

A permitted rounding method: round the AM base and the A-tax base down to a multiple of DKK 10, and round the AM-bidrag and A-tax up to whole kroner. If used, show all four figures without øre on the payslip ([JV A.B.4.1.1.2.6](https://info.skat.dk/data.aspx?oid=2292833)). The worked examples below do not round.

**What is in the AM base.** All pay for personal work in employment, in cash or in kind, at the taxable value for benefits, including pay during sickness and maternity leave and termination payments (AMBL § 2(1) no. 1 and § 2(2)). Holiday pay and ferietillæg are AM-liable ([skat.dk, Labour market contribution](https://skat.dk/en-us/individuals/labour-market-contribution)). Employer payments to pension schemes within PBL § 19 are in the AM base under AMBL § 2(1) no. 4, with the AM-bidrag withheld by the pension provider (KSL § 49 D(1)). The employee's and employer's shares of an employer-administered scheme are reported in eIndkomst fields 147 and 148.

**Free car (Ligningsloven § 16(4)).** Annual value: 22.5% of the car's value (minimum DKK 160,000), plus 7 times the annual periodic tax (green owner tax, weight tax or CO2 owner tax). A diesel's equalisation tax (udligningsafgift) and the private-use supplement are left out of the periodic tax. The value is reduced by what the employee pays the employer in the year for the right to use the car. Divide by 12 and add to each month's pay; report it in eIndkomst field 19 and include it in field 13 ([eIndkomst reporting guide 8.4.1](https://info.skat.dk/data.aspx?oid=2395003)). Car value is the new-car price for the first 36 months from first registration, then 75% of it. A used car bought more than 36 months after first registration uses the purchase price. A leasing company states the value for a leased car. Whole months without the car reduce the value. Skattestyrelsen's own example: car DKK 300,000, green tax DKK 660, annual value DKK 72,120, so DKK 6,010 a month ([skat.dk, Fri bil](https://skat.dk/erhverv/ansatte-og-loen/personalegoder-naar-du-er-arbejdsgiver/fri-bil-til-dine-medarbejdere-firmabil)).

**Free phone and internet (Ligningsloven § 16(12)).** DKK 3,500 a year for 2026, once, even with both phone and internet; DKK 291.7 a month for monthly paid staff, reported in field 20 and included in field 13. A work-only phone is not taxed if a sworn statement (tro og love-erklæring) is signed and the employer checks it. An internet connection with access to the work network is not taxed. Private use of a work computer is not taxed. A married couple living together, both taxed on a free phone, each get 25% off if their joint value before the cut is at least DKK 4,600 for 2026 (DKK 3,300 at 2010 level, indexed). The cut is made on the annual tax statement, so the employer reports the full monthly value and does not deduct it ([skat.dk, Fri telefon](https://skat.dk/erhverv/ansatte-og-loen/personalegoder-naar-du-er-arbejdsgiver/fri-telefon-computer-og-internet-til-dine-ansatte); Ligningsloven § 16(12); [eIndkomst reporting guide 8.4.1](https://info.skat.dk/data.aspx?oid=2395003)).

**Holiday pay (Ferieloven, LBK nr. 152 of 20 February 2024).**

- The holiday year runs 1 September to 31 August. The employee earns 2.08 days for each month employed, 25 days a year, and takes them from 1 September of the same holiday year to 31 December after it ends (§§ 4 to 6).
- **Salaried employees with paid holiday** (taken on monthly or longer, with full pay on public holidays and sick days) get normal pay during holiday plus a ferietillæg of 1% of pay (§ 16(1)). The ferietillæg is paid either when the holiday starts, or with May pay for September to May and with August pay for the rest (§ 18). The employer does not report holiday pay for continuing salaried staff to eIndkomst; only on leaving ([skat.dk, Indberet feriepenge](https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/indberet-feriepenge)).
- **Other employees, mainly hourly paid,** get feriegodtgørelse of 12.5% of pay (§ 16(2)). It is calculated on all taxable pay and benefits the employee does not keep during holiday, plus the employee's pension contributions and AM-bidrag (§ 19(1) and (2)). It is not calculated on holiday pay itself (§ 19(4)).
- **FerieKonto.** Feriegodtgørelse is reported to eIndkomst and paid to FerieKonto (§ 31(1) and (2)), unless a collective agreement lets the employer use a holiday fund or a guarantee (§ 3(4)). Holiday pay that FerieKonto or a holiday fund will pay out is taxed when earned: the employer withholds AM-bidrag and A-tax and pays over the net amount. Holiday pay the employer pays out itself is taxed only when paid, so nothing is withheld when it is earned ([eIndkomst reporting guide 8.3.1](https://info.skat.dk/data.aspx?oid=2287085)).
- **A salaried employee who leaves.** Report the untaken days and holiday pay in the leaving month. If FerieKonto pays it out, report the net amount after AM-bidrag and A-tax and tax it in the leaving month. If the employer pays it out, report gross and tax it on payment ([skat.dk, Indberet feriepenge](https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/indberet-feriepenge)).

**Employer contributions.** On top of gross pay, the employer pays its ATP share (DKK 198 a month for a full-time monthly employee) and the other statutory contributions collected through Samlet Betaling. Those are in `dk-social-contributions`.

**Payslip.** Skattestyrelsen's Danish start-up guide says a payslip must be made at each pay run; its English page says the employer should give one each month. The mandatory items the Danish guide lists are the employer's name, address and CVR or SE number; the employee's name, address and CPR number; the pay period; the pay; and the A-tax and AM-bidrag withheld under the tax card ([skat.dk, start-up guide](https://skat.dk/erhverv/guides-og-webinarer-til-start-ups/start-up-med-skat/for-selskaber/ansatte/del-2-lav-en-loenseddel-og-bogfoer-loennen)). Its English page adds hours worked, pension including ATP, net pay, tax card details and rate, holiday pay, benefits such as a free phone, pay date, and A-income and tax for the period and year to date ([skat.dk, Hiring your first employee](https://skat.dk/en-us/businesses/employees-and-pay/hiring-your-first-employee)).

## Deadlines and filing

| What | When | To whom | Source |
|---|---|---|---|
| Register as employer | Before the first pay run | virk.dk | skat.dk, Hiring your first employee |
| Retrieve each employee's eSkattekort | Before the first payment to them | Skattestyrelsen (electronic) | KSL § 48(1) |
| Withhold ATP, AM-bidrag and A-tax | At each payment, including advances and on-account pay | Kept by the employer | KSL § 46(2); skat.dk, Sådan indberetter du løn |
| eIndkomst report and payment, SMV, 2026 periods | The 10th of the following month: 10 Feb, 10 Mar, 10 Apr, 11 May, 10 Jun, 10 Jul, 10 Aug, 10 Sep, 12 Oct, 10 Nov, 10 Dec; December 2026 is due 18 January 2027 | Skattestyrelsen (Skattekonto) | skat.dk, Frister: A-skat og am-bidrag |
| eIndkomst report and payment, large employer ("fremrykket betaling"), 2026 periods | The last banking day of the same month: 30 Jan, 27 Feb, 31 Mar, 30 Apr, 29 May, 30 Jun, 31 Jul, 31 Aug, 30 Sep, 30 Oct, 30 Nov, 30 Dec | Skattestyrelsen | same |
| Size check | Each November, on A-tax and AM-bidrag for October of the previous year to September of the current year; the new status applies from 1 January and is notified through Virk | Skattestyrelsen | Opkrævningsloven § 2(6); skat.dk, Frister |
| Nil return (nulangivelse) | Every month with no pay, including a month the employer registered mid-month | eIndkomst | skat.dk, Sådan indberetter du løn |
| What eIndkomst holds per employee | Pay period and payment date; hours (field 200), AM-liable A-income (13), A-tax (15), AM-bidrag (16), total ATP (46), employer-administered pension (147, 148), holiday pay, benefits; for an employee living abroad, name, address, country, birth date and TIN | eIndkomst | same |
| ATP report | With pay in eIndkomst | eIndkomst | virk.dk, ATP arbejdsgiver |
| ATP payment (billed quarterly by Samlet Betaling) | Q1 by 1 July (report by 31 May), Q2 by 1 October (31 August), Q3 by 1 January (30 November), Q4 by 1 April (28 February) | Samlet Betaling | same |
| Holiday pay for hourly paid staff to FerieKonto | Pay period ending by the 15th: last day of that month; ending later: the 15th of the next month (earlier banking day if on a weekend or holiday) | eIndkomst and FerieKonto | virk.dk, Feriepenge arbejdsgiver |
| Holiday pay for a leaving salaried employee | Last banking day of the leaving month | eIndkomst and FerieKonto | same |
| Holiday pay not drawn by the end of the holiday-taking period, to Arbejdsmarkedets Feriefond (or a private holiday fund) | By 15 November after that period ends | Feriefond | Ferieloven § 34(3) |

Public authorities have their own dates ([skat.dk, Frister](https://skat.dk/erhverv/ansatte-og-loen/frister-ansatte-og-loen)). A payroll bureau or accountant may report for the employer, but the employer stays responsible ([skat.dk, Hiring your first employee](https://skat.dk/en-us/businesses/employees-and-pay/hiring-your-first-employee)). Pay is reported for the right pay period, which is not always a calendar month: many hourly staff run from the 20th to the 19th ([skat.dk, Sådan indberetter du løn](https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/saadan-indberetter-du-loen-eindkomst)).

## Penalties and interest

| What | Amount | Source |
|---|---|---|
| Month not reported (no report and no nil return) | Skattestyrelsen sets a provisional estimate: the average of the last 3 reports, or DKK 7,000 A-tax and DKK 1,000 AM-bidrag for a new employer. Fee DKK 1,400 per estimate, plus interest | skat.dk, Sådan indberetter du løn |
| Four months in a row not reported | Skattestyrelsen may deregister the A-tax registration, and possibly others | same |
| Not reporting at all | No refunds from the Skattekonto (for example VAT) until reported; risk of a criminal case | same |
| A-tax and AM-bidrag paid late, or a correction that adds tax | Interest at 0.95% a month in 2026, calculated daily, from the original deadline. The old 14-day grace for corrections ended on 1 July 2023 | skat.dk, Payments to your tax account; skat.dk, Sådan betaler du A-skat og am-bidrag; JV A.B.4.7.2 |
| Tax not withheld, or withheld too low | The employer is liable for the shortfall unless it shows it was not negligent | KSL § 69(1) |
| Tax withheld but not paid over | The employer is liable for the amount withheld | KSL § 69(2) |
| Failing to withhold A-tax or AM-bidrag, intentionally or through gross negligence | Fine; the statute sets no fixed amount. With intent to evade tax or other aggravating circumstances, up to 1 year 6 months in prison | KSL § 74(1) no. 1 and § 74(2) |
| Reminder fee on an unpaid tax account balance | DKK 65; DKK 160 from 14 September 2026 | skat.dk, Payments to your tax account |
| ATP paid late | Interest at 9.75% a year (1 January to 30 June 2026) | virk.dk, ATP arbejdsgiver |
| Holiday pay paid late to FerieKonto | Interest of 1.5% per started month from the due date | Ferieloven § 31(3) |

## Cross-border points

- **Employees living abroad.** Report name, address, country, gender, birth date and the TIN of the country of residence, even with a Danish CPR number. A report missing these can be rejected ([skat.dk, Sådan indberetter du løn](https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/saadan-indberetter-du-loen-eindkomst)).
- **Foreign employer.** No Danish withholding unless it has a Danish permanent establishment or pays through a Danish representative (KSL §§ 44(b), 46(4) and (5)). When a foreign business hires Danish staff from a Danish employer, the Danish employer withholds ([skat.dk, Skat af ansattes løn](https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/skat-af-ansattes-loen)).
- **Hiring out of labour (arbejdsudleje).** People taxed under KSL § 2(1) no. 3 on pay for being placed at the disposal of a Danish business pay 30% of gross income (KSL § 48 B).
- **Researcher and key-employee scheme.** An employee who has not been tax liable in Denmark in the last 10 years, has had no share in the management or control of the employer in the last 5 years, and meets the pay test or is an approved researcher, can elect A-tax of 27% of cash pay, plus AM-bidrag, for up to 84 months. The pay is then left out of taxable income, and no deductions are allowed (KSL §§ 48 E and 48 F). The pay test for 2026 is an average contractual pay of at least DKK 65,400 a month before AM-bidrag, plus ATP; holiday supplements do not count ([JV C.F.6.1.4](https://info.skat.dk/data.aspx?oid=1977289)). Refer the election.
- **Social security.** Which country's social security applies to a posted or cross-border worker, and A1 certificates: `dk-social-contributions`. ATP is due for employees who work in Denmark or are posted abroad by a Danish employer ([virk.dk, ATP arbejdsgiver](https://virk.dk/vejledning/atp/atp-arbejdsgiver/)).
- **Treaty and residence questions** for the employee: `dk-income-tax`.

## Worked examples

### Example 1: salaried employee, DKK 40,000 a month, hovedkort

A full-time salaried employee of a private company works more than 117 hours a month and earns DKK 40,000 gross a month. There is no pension scheme and no benefit. The employer has retrieved the hovedkort. The card shows a trækprocent of 37% and a monthly deduction of DKK 4,508. These are the card's own numbers for this employee; the employer does not derive them.

1. ATP: DKK 99 from the employee, DKK 198 from the employer.
2. AM base: DKK 40,000 less DKK 99 = DKK 39,901. AM-bidrag at 8% = DKK 3,192.08.
3. A-income after AM-bidrag: DKK 39,901 less DKK 3,192.08 = DKK 36,708.92. Less the monthly deduction of DKK 4,508 = DKK 32,200.92.
4. A-tax at 37% = DKK 11,914.34.
5. Net pay: DKK 40,000 less DKK 99, DKK 3,192.08 and DKK 11,914.34 = DKK 24,794.58.
6. The employer reports field 13 (DKK 39,901), 15 (DKK 11,914.34), 16 (DKK 3,192.08) and 46 (total ATP DKK 297) by 10 February 2026 if it is an SMV, and pays A-tax and AM-bidrag by the same date. ATP goes in the quarterly Samlet Betaling bill.
7. Holiday: the employee earns 2.08 days for the month. The 1% ferietillæg on the year's pay is paid in May and August, or as each holiday starts.

```oa-check
name: Salaried employee, DKK 40,000 a month, hovedkort (2026)
inputs:
  gross: 40000
  atp_employee: 99
  atp_employer: 198
  monthly_deduction: 4508
  rate_pct: 37
steps:
  - am_base: gross - atp_employee
  - am_bidrag: am_base * 0.08
  - after_am: am_base - am_bidrag
  - tax_base: after_am - monthly_deduction
  - a_tax: round(tax_base * rate_pct / 100, 2)
  - net_pay: gross - atp_employee - am_bidrag - a_tax
  - atp_total: atp_employee + atp_employer
  - employer_cost_before_other_contributions: gross + atp_employer
expected:
  am_base: 39901.00
  am_bidrag: 3192.08
  after_am: 36708.92
  tax_base: 32200.92
  a_tax: 11914.34
  net_pay: 24794.58
  atp_total: 297.00
  employer_cost_before_other_contributions: 40198.00
```

### Example 2: free car and free phone on top of DKK 50,000

A full-time salaried employee earns DKK 50,000 a month in cash. The employee has a company car that may be used privately and a free phone. The car cost DKK 300,000 new, is under 36 months old, and has a green owner tax of DKK 660 a year. The hovedkort shows 38% and a monthly deduction of DKK 4,508.

1. Free car: 22.5% of DKK 300,000 = DKK 67,500, plus 7 x DKK 660 = DKK 4,620, so DKK 72,120 a year, DKK 6,010 a month.
2. Free phone: DKK 3,500 / 12 = DKK 291.67 a month.
3. AM base: DKK 50,000 less ATP of DKK 99, plus DKK 6,010 and DKK 291.67 = DKK 56,202.67. AM-bidrag at 8% = DKK 4,496.21.
4. A-income after AM-bidrag: DKK 51,706.46. Less DKK 4,508 = DKK 47,198.46. A-tax at 38% = DKK 17,935.41.
5. The benefits are not paid in cash, so the tax on them comes out of the DKK 50,000. Net cash pay: DKK 50,000 less DKK 99, DKK 4,496.21 and DKK 17,935.41 = DKK 27,469.38.
6. Without the benefits, AM-bidrag would be DKK 3,992.08 and A-tax DKK 15,732.35. So the car and phone cost the employee DKK 2,707.19 a month in withholding.

```oa-check
name: Free car (DKK 300,000) and free phone on DKK 50,000 a month (2026)
inputs:
  cash_pay: 50000
  atp_employee: 99
  car_value: 300000
  periodic_tax: 660
  phone_year: 3500
  monthly_deduction: 4508
  rate_pct: 38
steps:
  - car_year: car_value * 0.225 + periodic_tax * 7
  - car_month: car_year / 12
  - phone_month: phone_year / 12
  - am_base: cash_pay - atp_employee + car_month + phone_month
  - am_bidrag: round(am_base * 0.08, 2)
  - after_am: am_base - am_bidrag
  - a_tax: round((after_am - monthly_deduction) * rate_pct / 100, 2)
  - net_cash: cash_pay - atp_employee - am_bidrag - a_tax
  - am_no_benefits: (cash_pay - atp_employee) * 0.08
  - tax_no_benefits: round((cash_pay - atp_employee - am_no_benefits - monthly_deduction) * rate_pct / 100, 2)
  - benefit_cost: am_bidrag + a_tax - am_no_benefits - tax_no_benefits
expected:
  car_year: 72120.00
  car_month: 6010.00
  phone_month: 291.67
  am_base: 56202.67
  am_bidrag: 4496.21
  a_tax: 17935.41
  net_cash: 27469.38
  tax_no_benefits: 15732.35
  benefit_cost: 2707.19
```

## Ask the client first

1. Is the business registered as an employer, and is it an SMV or a large employer on its registration certificate? (Deadlines: the 10th of the next month or the last banking day of the month.)
2. For each employee: salaried with paid holiday, or hourly paid? Hours a month? (Ferietillæg or 12.5% feriegodtgørelse through FerieKonto; the ATP band.)
3. Has each employee's eSkattekort been retrieved, and is it a hovedkort, bikort or frikort? (Without one, withhold 55%.)
4. Any company car, phone, internet, board and lodging, or health insurance that can be used privately? (These go into the AM base and A-income.)
5. Born in 2009 or later, so turning 17 or younger in 2026? (No AM-bidrag.)
6. Anyone living abroad, posted in or out, or hired from abroad, or anyone who may qualify for the 27% researcher scheme?

## Sources

| Source | URL | Read on |
|---|---|---|
| Kildeskatteloven, LBK nr. 460 of 3 May 2024 (§§ 43 to 49 D, 48 B, 48 E, 48 F, 69, 74) | https://www.retsinformation.dk/eli/lta/2024/460 | 2026-10-23 |
| Arbejdsmarkedsbidragsloven, LBK nr. 121 of 7 February 2020 (§§ 1 to 3) | https://www.retsinformation.dk/eli/lta/2020/121 | 2026-10-23 |
| Lov nr. 96 of 4 February 2025 (young people exempt from AM-bidrag from 2026; AMBL § 1, 2nd sentence) | https://www.retsinformation.dk/eli/lta/2025/96 | 2026-10-23 |
| Opkrævningsloven, LBK nr. 1040 of 13 September 2024 (§ 2(5) and (6): due dates and the large-employer test) | https://www.retsinformation.dk/eli/lta/2024/1040 | 2026-10-23 |
| Ferieloven, LBK nr. 152 of 20 February 2024 (§§ 3, 4 to 6, 16 to 19, 31, 34) | https://www.retsinformation.dk/eli/lta/2024/152 | 2026-10-23 |
| Ligningsloven, LBK nr. 1500 of 24 November 2025 (§ 16(4) free car, § 16(12) free phone) | https://www.retsinformation.dk/eli/lta/2025/1500 | 2026-10-23 |
| Skattestyrelsen, Frister: A-skat og am-bidrag (2026 deadline tables) | https://skat.dk/erhverv/ansatte-og-loen/frister-ansatte-og-loen | 2026-10-23 |
| Skattestyrelsen, Sådan indberetter du løn (eIndkomst fields, nil return, DKK 1,400 fee, SMV test) | https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/saadan-indberetter-du-loen-eindkomst | 2026-10-23 |
| Skattestyrelsen, Skat af ansattes løn (2026 youth AM-bidrag rule, foreign employers) | https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/skat-af-ansattes-loen | 2026-10-23 |
| Skattestyrelsen, Sådan betaler du A-skat og am-bidrag (interest from the original deadline) | https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/saadan-betaler-du-a-skat-og-am-bidrag | 2026-10-23 |
| Skattestyrelsen, Indberet feriepenge | https://skat.dk/erhverv/ansatte-og-loen/indberet-loen-eindkomst/indberet-feriepenge | 2026-10-23 |
| Skattestyrelsen, Fri bil til dine medarbejdere (2026 rates and example) | https://skat.dk/erhverv/ansatte-og-loen/personalegoder-naar-du-er-arbejdsgiver/fri-bil-til-dine-medarbejdere-firmabil | 2026-10-23 |
| Skattestyrelsen, Fri telefon, computer og internet (DKK 3,500 for 2026) | https://skat.dk/erhverv/ansatte-og-loen/personalegoder-naar-du-er-arbejdsgiver/fri-telefon-computer-og-internet-til-dine-ansatte | 2026-10-23 |
| Skattestyrelsen, The Danish tax card (personal allowance DKK 54,100) | https://skat.dk/en-us/individuals/tax-card | 2026-10-23 |
| Skattestyrelsen, Labour market contribution (order of deductions) | https://skat.dk/en-us/individuals/labour-market-contribution | 2026-10-23 |
| Skattestyrelsen, Hiring your first employee (registration, payslip items) | https://skat.dk/en-us/businesses/employees-and-pay/hiring-your-first-employee | 2026-10-23 |
| Skattestyrelsen, Start-up guide: Lav en lønseddel | https://skat.dk/erhverv/guides-og-webinarer-til-start-ups/start-up-med-skat/for-selskaber/ansatte/del-2-lav-en-loenseddel-og-bogfoer-loennen | 2026-10-23 |
| Skattestyrelsen, Payments to your tax account (0.95% a month in 2026; reminder fee DKK 160 from 14 September 2026) | https://skat.dk/en-us/businesses/payment-and-the-tax-account-skattekontoen/payments-to-your-tax-account | 2026-10-23 |
| Den juridiske vejledning A.B.4.7.2 (monthly interest, basis plus 0.85 points) | https://info.skat.dk/data.aspx?oid=2168585 | 2026-10-23 |
| SKM notice: rate under opkrævningsloven § 7(2) for 2026 (0.1%) | https://info.skat.dk/data.aspx?oid=2459995 | 2026-10-23 |
| Den juridiske vejledning A.B.4.1.1.2.6 (rounding) | https://info.skat.dk/data.aspx?oid=2292833 | 2026-10-23 |
| Den juridiske vejledning C.A.10.2.1.1.2.4 (ATP: 1/3 and 2/3, PBL § 19) | https://info.skat.dk/data.aspx?oid=2048235 | 2026-10-23 |
| eIndkomst reporting guide 8.3.1 (holiday pay for hourly staff, taxed when earned) | https://info.skat.dk/data.aspx?oid=2287085 | 2026-10-23 |
| eIndkomst reporting guide 8.2 (field 13 after ATP and employer-administered pension; fields 147 and 148) | https://info.skat.dk/data.aspx?oid=2233519 | 2026-10-23 |
| eIndkomst reporting guide 8.4.1 (field 19 free car, field 20 free phone, couple's threshold DKK 4,600) | https://info.skat.dk/data.aspx?oid=2395003 | 2026-10-23 |
| Den juridiske vejledning C.F.6.1.4 (researcher scheme minimum pay DKK 65,400 for 2026) | https://info.skat.dk/data.aspx?oid=1977289 | 2026-10-23 |
| borger.dk, ATP-satser for 2026 i privat virksomhed | https://www.borger.dk/pension-og-efterloen/ATP-Livslang-pension-oversigt/atp-bidraget/atp-satser-for-privat-virksomhed | 2026-10-23 |
| virk.dk, ATP Livslang Pension: arbejdsgiver (conditions, quarterly deadlines, interest) | https://virk.dk/vejledning/atp/atp-arbejdsgiver/ | 2026-10-23 |
| virk.dk, Feriepenge: arbejdsgiver (FerieKonto deadlines, DKK 4 fee) | https://virk.dk/vejledning/feriepenge/fp-arbejdsgiver/ | 2026-10-23 |

Not yet confirmed: the statutory basis of the monthly payslip duty (Skattestyrelsen's guidance says "must" in Danish and "should" in English, and names no provision).

> Contributed by Ryan Duguid.

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
