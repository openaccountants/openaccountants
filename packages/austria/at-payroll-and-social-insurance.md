---
name: at-payroll-and-social-insurance
description: "Use this skill for Austrian payroll in tax year 2026: monthly wage tax (Lohnsteuer), the 13th and 14th salaries at 6% within the Jahressechstel, employee and employer social insurance under the ASVG (18.07% and 20.98% outside Vienna), the EUR 6,930 maximum contribution base, the employer's levies (DB 3.7%, DZ, Kommunalsteuer 3%, MV 1.53%), tax-free supplements under EStG § 68 (EUR 400 a month for dirt, hardship, danger, Sunday, holiday and night work, plus 50% overtime supplements for the first 15 hours up to EUR 170 in 2026), and termination pay (old-system Abfertigung at 6%, BV-Kasse payouts, Kündigungsentschädigung and settlements with a tax-free fifth, Urlaubsersatzleistung). Covers monthly and annual deadlines and penalties. Trigger phrases: Lohnverrechnung, Lohnsteuer, Überstundenzuschlag, SEG-Zulage, Abfertigung, Urlaubsersatzleistung, Austrian payroll. Out of scope: the annual tariff and the employee's L 1 or E 1 return (at-income-tax), self-employed SVS (at-svs-contributions), arriving and leaving (at-cross-border), company tax (at-corporate-income-tax)."
version: 0.1
jurisdiction: AT
tax_year: 2026
last_updated: 2026-10-23
authored_by: Ryan Duguid
review_status: pending_review
trust_label: Accountant-authored
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Austria payroll: wage tax and employee and employer social insurance (2026)

This skill covers what an employer in Austria withholds and pays on wages each month, and what it costs on top of gross pay. It links to the other Austria skills and does not repeat them: `at-income-tax` (the tariff, the credits, Werbungskosten, the Pendlerpauschale amounts and the employee's own return), `at-svs-contributions` (social insurance of the self-employed), `at-cross-border` (residence, non-residents, the A1 certificate) and `at-corporate-income-tax`.

All figures are for the 2026 calendar year. Statute text was read on RIS (the federal legal information system) on 23 October 2026. Social insurance figures come from the ÖGK information sheet for employers (as at 1 January 2026), the Dachverband table of 2026 contribution values (version of 19 May 2026) and the ÖGK Arbeitsbehelf 2026.

## Who this applies to

- **Employers with an Austrian permanent establishment.** Where the employer has a Betriebsstätte in Austria, income tax on wages is collected by withholding: wage tax, Lohnsteuer (EStG § 47(1)). The employer is liable for withholding and paying it over (EStG § 82).
- **Foreign employers with no Austrian establishment.** They may run Austrian payroll voluntarily, and then carry all the employer's duties (EStG § 47(1) lit. b). If they do not, they must send the Finanzamt a wage certificate (Lohnbescheinigung, EStG § 84a) for employees with unlimited tax liability whose centre of activity is in Austria for more than six months of the year (EStG § 47(1) lit. c). The employee then declares the wages in their own return.
- **Employees (Dienstnehmer) under the ASVG.** Anyone in an employment relationship, plus free service contractors (freie Dienstnehmer), is insured with the ÖGK (Österreichische Gesundheitskasse). Pay above EUR 551.10 a month means full insurance. At or below it, the person is marginally employed (geringfügig) and only accident insurance is paid by the employer.
- **Registration.** The employer registers each employee with the ÖGK before work starts, and deregisters them within seven days after insurance ends (ASVG § 33(1)).
- **Not covered here.** Civil servants (B-KUVG), miners (knappschaftliche Pensionsversicherung), apprentices' reduced rates, construction workers' BUAK contributions and their special rules under EStG § 67(5), widow's pension settlements under § 67(4), pension buy-outs under § 67(8)(e), back pay for earlier calendar years under § 67(8)(c), and back pay in insolvency under § 67(8)(g). Refer them. Supplements under EStG § 68 and termination payments under § 67(3), (6) and (8)(a), (b), (d) and (f) are covered below.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Wage tax: tariff applied to annualised pay, bands 0% to EUR 13,539, 20% to 21,992, 30% to 36,458, 40% to 70,365, 48% to 104,859, 50% to 1,000,000, 55% above | as listed | 2026 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=33 |
| Verkehrsabsetzbetrag (every employee), applied in payroll | EUR 496 a year | 2026 | same |
| Verkehrsabsetzbetrag with a Pendlerpauschale, income up to EUR 15,069 | EUR 853 a year | 2026 | same |
| Pendlereuro (with a Pendlerpauschale) | EUR 6 a year per km one way | 2026 | same |
| Werbungskostenpauschale deducted in payroll | EUR 132 a year | 2026 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=16 |
| 13th and 14th salary (sonstige Bezüge within the Jahressechstel): first EUR 620 | 0% | 2026 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=67 |
| Next EUR 24,380 / next EUR 25,000 / next EUR 33,333 | 6% / 27% / 35.75% | 2026 | same |
| Freigrenze: fixed rates not used if the Jahressechstel is at most | EUR 2,615 (EUR 2,675 for 2027) | 2026 | same |
| Social insurance, employee share, salaried and wage-earning staff outside Vienna | 18.07% (health 3.87, pension 10.25, unemployment 2.95, AK levy 0.50, WBF 0.50) | 2026 | https://www.sozialversicherung.at/cdscontent/load?contentid=10008.806858 |
| Social insurance, employer share, outside Vienna | 20.98% (health 3.78, accident 1.10, pension 12.55, unemployment 2.95, IESG 0.10, WBF 0.50) | 2026 | same |
| Wohnbauförderungsbeitrag (WBF) in Vienna | 1.5% (0.75% each side), so 18.32% employee and 21.23% employer | from 1 January 2026 | same |
| Employee share on special payments (no AK levy, no WBF) | 17.07% | 2026 | https://www.gesundheitskasse.at/cdscontent/load?contentid=10008.802672&version=1775628844 |
| Employer share on special payments (no WBF) | 20.48% | 2026 | same |
| Employee unemployment share for low pay: base up to EUR 2,225 / to 2,427 / to 2,630 / above | 0% / 1% / 2% / 2.95% | 2026 | https://www.sozialversicherung.at/cdscontent/load?contentid=10008.806858 |
| Höchstbeitragsgrundlage (maximum contribution base), current pay | EUR 6,930 a month (EUR 231 a day) | 2026 | https://www.gesundheitskasse.at/cdscontent/load?contentid=10008.784766&version=1752580359 |
| Höchstbeitragsgrundlage, special payments | EUR 13,860 a year | 2026 | same |
| Geringfügigkeitsgrenze (marginal-employment limit) | EUR 551.10 a month (not indexed for 2026) | 2026 | same |
| Employer accident insurance for marginal employees | 1.1% | 2026 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008147&Paragraf=53a |
| Dienstgeberabgabe (federal) on marginal employees, if their pay in the month totals more than EUR 826.65 | 19.4% | 2026 | https://www.sozialversicherung.at/cdscontent/load?contentid=10008.806858 (rate) and https://www.gesundheitskasse.at/cdscontent/load?contentid=10008.784766&version=1752580359 (EUR 826.65) |
| Mitarbeitervorsorge (MV, also BV), employer, no cap and no floor | 1.53% of pay including special payments | 2026 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20002088&Paragraf=6 |
| Dienstgeberbeitrag (DB) to the family fund | 3.7% (2.7% from 2028) | 2025 to 2027 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008220&Paragraf=41 |
| Zuschlag zum DB (DZ), WKO members only: Burgenland 0.40, Kärnten 0.37, Niederösterreich 0.33, Oberösterreich 0.31, Salzburg 0.35, Steiermark 0.34, Tirol 0.39, Vorarlberg 0.33, Wien 0.36 | % of the DB base | 2026 | https://www.wko.at/lohnverrechnung/zuschlag-dienstgeberbeitrag |
| Kommunalsteuer to the municipality | 3% | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004841 |
| DB, DZ and Kommunalsteuer small-payroll relief: if the month's total pay is at most EUR 1,460, deduct | EUR 1,095 from the base | 2026 | same, and FLAG § 41(4) |
| Late-payment interest on social insurance (Verzugszinsen) | 5.53% | from 1 January 2026 | https://www.gesundheitskasse.at/cdscontent/load?contentid=10008.802672&version=1775628844 |
| Vienna Dienstgeberabgabe (U-Bahn levy), per employee working in Vienna, for each started week; employees over 55 exempt | EUR 2 | 2026 | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=LrW&Gesetzesnummer=20000133 |
| Tax-free total of dirt, hardship and danger allowances (SEG-Zulagen), Sunday, holiday and night supplements, overtime supplements linked to that work, and holiday-work pay under ARG § 9(5) | EUR 400 a month (EUR 600 if normal hours fall mostly between 19:00 and 07:00) | 2026 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=68 |
| Tax-free overtime supplements on top of that (EStG § 68(2) as modified for 2026) | first 15 overtime hours a month, at most 50% of the basic hourly pay, at most EUR 170 a month | pay periods in 2026 (the permanent rule is 10 hours and EUR 120) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=124b (Z 440 lit. c) |
| Same overtime relief, for comparison | first 18 hours, EUR 200 a month | pay periods 2024 and 2025 only | same (Z 440 lit. b) |
| Statutory or collective-agreement severance (Abfertigung alt) | 6%, or the tariff tax on one month's current pay times the number of months if that is lower | 2026 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=67 |
| Capital paid out by a BV-Kasse (Abfertigung neu) | 6%; nil if moved to a pension insurer, a pension fund or a Pensionskasse | 2026 | same |
| Voluntary severance and other payments on leaving (§ 67(6)): slice at 6% | one quarter of the last 12 months' current pay, at most 9 times EUR 6,930 (EUR 62,370) | 2026 | same |
| Kündigungsentschädigung, and court or out-of-court settlements (§ 67(8)(a) and (b)): tax-free part | one fifth after social insurance, at most one fifth of EUR 62,370 (EUR 12,474) | 2026 | same |
| Settlement on leaving for periods covered by a BV-Kasse | up to EUR 7,500 at 6% | 2026 | same |
| Social-plan payments on leaving (§ 67(8)(f)) | up to EUR 22,000 at half the rate that results when the payment is spread evenly over the months of the year | 2026 | same |

The BMF deadlines page gives the same DB rate (3.7%) and DZ range (0.31% to 0.4%) ([BMF, Fristen und Fälligkeiten](https://www.bmf.gv.at/themen/steuern/fristen-verfahren/fristen-faelligkeiten.html)).

## The taxable base

**Monthly wage tax on current pay (EStG §§ 62 and 66).**

1. Start from gross current pay for the month.
2. Deduct the employee's social insurance on that pay, including the AK levy and WBF (§ 62 Z 3 to 5), and any Pendlerpauschale or allowance the employee has claimed with the employer (§ 62).
3. Multiply by the annualisation factor. For a monthly payroll it is 12 (§ 66(3)).
4. Deduct the yearly amounts, mainly the Werbungskostenpauschale of EUR 132 (§ 66(2), § 62 Z 1, § 16(3)). Do not deduct a Sonderausgaben lump sum: the EUR 60 in § 18(2) still stands in § 62 Z 2, but it applied for the last time to pay periods ending before 1 January 2021 (§ 124b Z 285 and 286; LStR 2002 Rz 596 and 813a).
5. Apply the § 33 tariff to that annual figure.
6. Deduct the credits payroll may give: the Verkehrsabsetzbetrag and Pendlereuro, the Familienbonus Plus and the sole-earner or single-parent credit if the employee has claimed them with the employer (§ 66(1)). The Zuschlag zum Verkehrsabsetzbetrag is given only on assessment. Amounts and conditions: `at-income-tax`.
7. Divide by 12 and round to the cent. That is the month's wage tax.

**13th and 14th salaries (sonstige Bezüge, EStG § 67).** The holiday bonus (Urlaubszuschuss) and Christmas bonus (Weihnachtsremuneration) come from the collective agreement or the contract, which sets their amount and timing.

- They are taxed apart from current pay, at fixed rates, as long as they stay within the Jahressechstel: one sixth of the current pay already received in the year, converted to a full year, counting the current pay paid with the bonus (§ 67(2)). With 14 equal payments, both bonuses together fill the sixth exactly.
- First deduct the employee's social insurance on the bonus (§ 67(12)). Then the first EUR 620 of the year's bonuses is tax-free, the next EUR 24,380 is taxed at 6%, and the higher slices at 27% and 35.75% (§ 67(1)). The EUR 620 is used once a year, normally on the first bonus.
- Bonuses above the sixth, or above EUR 83,333 after social insurance, are taxed with the current pay of the month at the tariff (§ 67(2) and (10)).
- If the Jahressechstel is EUR 2,615 or less, the fixed rates do not apply (§ 67(1)). On the employee's assessment, the tax on bonuses within the sixth is recalculated under § 67(1) and (2) if those bonuses exceed EUR 2,615 (§ 41(4)).

**Social insurance base (ASVG §§ 44, 45, 49, 54).** Contributions are due on all pay (Entgelt) up to the maximum base: EUR 6,930 a month for current pay and EUR 13,860 a year for special payments. Special payments carry no AK levy and no WBF. The low-pay reduction of the employee's unemployment share is tested separately on the month's current pay and on the special payment, never on the two added together (Arbeitsbehelf 2026, 3.5.2). The MV contribution of 1.53% has no cap and no floor.

**Base for DB, DZ and Kommunalsteuer.** All wages paid in the month, current and special payments alike, with no maximum base (FLAG § 41(3); KommStG § 5). Pensions, the termination payments named in § 67(3) and (6), wages of disabled employees protected by law, and wages of employees from the month after they turn 60 are left out of the DB base (FLAG § 41(4)). Kommunalsteuer is owed to the municipality where the establishment is (KommStG § 5(1)). DZ is owed only by members of the Wirtschaftskammer (WKO).

**Supplements for overtime, night, Sunday and holiday work, and SEG-Zulagen (EStG § 68).**

1. Split each overtime hour into its basic pay (Grundlohn) and the supplement (Zuschlag). The basic pay is always taxed at the tariff with current pay. Only the supplement can be tax-free (§ 68(1) to (3)).
2. Find the basic hourly pay. The BMF divides monthly pay by 173 for a 40-hour week, unless the collective agreement or works agreement sets another divisor (LStR 2002 Rz 1148).
3. An overtime hour is an hour beyond the normal working time set by law, collective agreement or works agreement, and only time beyond 40 hours a week, or beyond the daily hours that a 40-hour week spread over the working days gives, counts (§ 68(4)). The BMF also treats supplements for Mehrarbeit between a shorter collective-agreement week and 40 hours as overtime supplements. Part-time extra hours paid with the 25% Mehrarbeit supplement under AZG § 19d(3a) are not overtime and stay taxable (LStR 2002 Rz 1146).
4. Pot 1, EUR 400 a month (§ 68(1)): SEG-Zulagen, Sunday, holiday and night supplements, overtime supplements for overtime worked on Sundays, holidays or at night, and holiday-work pay under ARG § 9(5). Night work means at least 3 hours in a row between 19:00 and 07:00 that the business requires (§ 68(6)). If the employee's normal hours in the pay period fall mostly in that window, the pot is EUR 600. SEG-Zulagen qualify only if a law, collective agreement, works agreement or an in-house rule for all staff or a group of staff grants them (§ 68(5)).
5. Pot 2, the weekday overtime pot (§ 68(2) with § 124b Z 440 lit. c): for pay periods in 2026, supplements for the first 15 overtime hours in the month, at most 50% of the basic hourly pay per hour, at most EUR 170 in total. A supplement above 50% is tax-free only up to 50%. If the supplement is below 50%, only that lower amount is tax-free, and still for 15 hours at most (LStR 2002 Rz 1148, which gives the same rule for the old 10 hours). Overtime supplements that do not fit in pot 1 because pot 1 is full can use pot 2 if its hours are not used up (Rz 1147).
6. Everything above the two pots is taxed at the tariff with current pay (§ 68(3)).
7. Social insurance: overtime pay, the supplements, the hardship and danger allowances and the Sunday, holiday and night supplements are all Entgelt and bear full contributions. Only a dirt allowance (Schmutzzulage) is exempt, and only as far as it is tax-free under § 68 (ASVG § 49(3) Z 2). DB, DZ, Kommunalsteuer and MV are due on all of it: § 68 pay is not on the exempt lists (FLAG § 41(4); KommStG § 5(2); BMSVG § 6(5) with ASVG § 49). The employee's social insurance on tax-free supplements is deducted in full from current pay before the tariff (EStG § 62 Z 4, which excludes only contributions on pay taxed at a fixed rate under § 67; LStR 2002 Rz 1121).
8. Each employer gives both pots in full, even where the employee changes job in the month or has two jobs (Rz 1147).

§ 68(1) was amended twice in 2026, both times for pay periods ending after 31 December 2025. BGBl I 4/2026 (in force 19 February 2026) added holiday-work pay under ARG § 9(5) to the EUR 400 pot; BGBl I 43/2026 (in force 1 July 2026) added pay under comparable statutory rules. An employer that had not applied them had to correct (aufrollen) earlier 2026 payrolls where technically possible: by 31 May 2026 for the first (§ 124b Z 492) and by 30 September 2026 for the second (§ 124b Z 494). The same 31 May 2026 deadline applied to the 15-hour and EUR 170 rule (§ 124b Z 440 lit. c).

**Termination payments (EStG § 67(3) to (8)).** Run them in the final payroll in this order.

1. **Statutory or collective-agreement severance, old system (Abfertigung alt, § 67(3)).** It applies to employment that began before 1 January 2003 (BMSVG § 46(1)), or to the frozen old entitlement of an employee who moved to the new system for later years (BMSVG § 47(2)). The labour-law amount is a number of monthly pays. Tax is the lower of 6% of the payment, or the tariff wage tax on one month's current pay multiplied by that number of months (the Vervielfachungsmethode). No social insurance (ASVG § 49(3) Z 7), no MV, and no DB, DZ or Kommunalsteuer (FLAG § 41(4) lit. b; KommStG § 5(2) lit. b). Extra severance paid for years covered by a BV-Kasse is taxed at the tariff under § 67(10).
2. **New-system severance (Abfertigung neu, BMSVG).** The employer does not pay it: the employee claims it from the BV-Kasse (BMSVG § 14(1)). The employee cannot take it out yet, and it stays in the BV-Kasse, if they resigned, were dismissed for cause, left early without good reason, or have fewer than 36 contribution months (§ 14(2)). A cash payout is taxed at 6%. If the employee moves the money to a pension insurer, a pension investment fund, a Pensionskasse or (from 17 October 2026) a supplementary pension scheme under ASVG § 479, no wage tax arises (EStG § 67(3); BMSVG § 17(1)).
3. **Voluntary severance and other payments on leaving (§ 67(6)).** 6% applies to one quarter of the current pay of the last 12 months, capped at 9 times the monthly maximum contribution base (EUR 62,370 for 2026). For service years with no BV-Kasse claim, a further slice of 2/12 to 12/12 of the last 12 months' current pay is also taxed at 6%, depending on proven years of service (3 to 25 years), capped at 3 times EUR 6,930 per month counted; any statutory severance already paid or due reduces that further slice (§ 67(6) Z 2, 3 and 7). Anything above is taxed at the tariff as current pay of the month (§ 67(6) Z 6). Payments for waiving work in future pay periods are excluded from § 67(6). § 67(6) applies only to periods with no BV-Kasse claim (Z 7). The BMF reads this as: no § 67(6) relief at all for an employment that has been in the new system since it began after 2002, so a voluntary severance there is taxed at the tariff; where the old claim was frozen at a transfer date, both slices apply, but only service up to that date counts (LStR 2002 Rz 1087a and 1087c). Payments named in § 67(6) are left out of the DB, DZ and Kommunalsteuer base (FLAG § 41(4) lit. b; KommStG § 5(2) lit. b).
4. **Kündigungsentschädigung (damages for the pay the employee would have earned up to the end of the proper notice period, § 67(8)(b)).** Deduct the employee's social insurance on it. One fifth of the rest is tax-free, at most EUR 12,474 (one fifth of EUR 62,370). The remainder is taxed with the current pay of the month of payment at the tariff (§ 67(10)). It is Entgelt for social insurance and MV, and insurance runs on for the notice period it covers (ASVG § 11(2); BMSVG § 14(2)).
5. **Settlements (Vergleichssummen, § 67(8)(a)).** Same one-fifth rule and cap, unless part of the sum is severance under § 67(3) or (6), which keeps its 6%. A settlement paid on or after leaving for periods covered by a BV-Kasse is taxed at 6% up to EUR 7,500. Insurance runs on for the period the settlement covers, after leaving out amounts that are not Entgelt (ASVG § 11(2)).
6. **Pay for untaken holiday (Urlaubsersatzleistung, § 67(8)(d)).** Split it. The part that replaces current pay is taxed as current pay of the month of payment. The part that replaces the 13th and 14th salary is a special payment and is taxed under § 67(1) and (2). Social insurance and MV are due, and insurance runs on for the holiday period it covers, after any Kündigungsentschädigung period (ASVG § 11(2)).
7. **Social-plan payments (§ 67(8)(f)).** Paid on leaving under a social plan for a restructuring under ArbVG § 109(1) Z 1 to 6, and not already taxed at 6% under § 67(6): up to EUR 22,000 at half the rate that results when the payment is spread evenly over the months of the year.
8. **Everything else** paid on leaving, such as a bonus or commission earned during employment, follows the normal rules for current pay or special payments.

## Deadlines and filing

| What | When | To whom | Source |
|---|---|---|---|
| Register the employee | Before work starts | ÖGK, via ELDA | ASVG § 33(1) |
| Payroll account (Lohnkonto) | From the 15th of the month after employment starts | Kept by the employer | EStG § 76(1) |
| Wage tax for the month | By the 15th of the following month | Finanzamt | EStG § 79(1) |
| DB and DZ for the month | By the 15th of the following month | Finanzamt | FLAG § 43(1) |
| Kommunalsteuer for the month | By the 15th of the following month | Municipality | KommStG § 11(2) |
| Monthly contribution report (mBGM), self-accounting employers | By the 15th of the following month (if employment starts after the 15th, by the 15th of the month after next) | ÖGK, via ELDA | Arbeitsbehelf 2026, 5.2.3 |
| Social insurance contributions | Due on the last day of the month; on time if credited within 15 days, so by the 15th of the following month, with three days' grace | ÖGK | Arbeitsbehelf 2026, 3.14 and 3.15 |
| Annual wage slip (Lohnzettel, form L 16) for each employee | By end of February of the following year, electronically via ELDA (on paper by end of January only if electronic filing is not possible) | Finanzamt or ÖGK | EStG § 84(1) |
| Annual Kommunalsteuer return | By end of March of the following year, via FinanzOnline | Municipality | KommStG § 11(4) |
| Vienna Dienstgeberabgabe | By the 15th of the following month; annual return by 31 March | City of Vienna (Magistrat) | Wiener Dienstgeberabgabegesetz § 6 |
| Employee's own assessment (Arbeitnehmerveranlagung, form L 1) | Within five years after the year ends, so for 2026 by 31 December 2031 | Finanzamt | EStG § 41(2) |

Wages for one month that are paid by the 15th of the next month count for the earlier month (EStG § 79(1), FLAG § 43(1), KommStG § 11(1)). Wages for the prior year paid between 16 January and 15 February are paid over by 15 February as the prior year's tax (EStG § 79(2)).

An employee who had two or more employers at the same time during the year, each withholding separately, must file an assessment (EStG § 41(1) Z 2). Other filing duties: `at-income-tax`.

Termination payments have no deadlines of their own. The wage tax on them is paid over by the 15th of the following month like other wages, and the leaver's Lohnzettel goes in with all the others by end of February (EStG §§ 79(1) and 84(1)).

## Penalties and interest

| What | Amount | Source |
|---|---|---|
| Wage tax, DB or DZ paid late: first late-payment surcharge (Säumniszuschlag) | 2% of the unpaid amount | BAO § 217(2) |
| Second and third surcharges, if still unpaid three months after enforceability, and three months after that | 1% each | BAO § 217(3) |
| Wage tax not withheld or not paid over | Employer is liable; the Finanzamt may estimate the arrears and hold the employer liable | EStG §§ 79(3), 82 |
| mBGM filed late (self-accounting), up to 5 days / 6 to 10 days / 11 days to month end | EUR 5 / EUR 12 / EUR 18 | Arbeitsbehelf 2026, 6.13.2 |
| Any other reporting breach, including a late registration or deregistration | EUR 70 each (2026) | same |
| Employee found working without prior registration (Beitragszuschlag) | EUR 400 per person plus EUR 600 for the inspection; administrative fine of EUR 730 to 2,180 (repeat: EUR 2,180 to 5,000) | Arbeitsbehelf 2026, 6.13.1 |
| Social insurance paid late | Interest at 5.53% a year from the 16th day | Arbeitsbehelf 2026, 3.15 |
| Kommunalsteuer return intentionally not filed on time | Fine up to EUR 500 | KommStG § 15(3) |

## Cross-border points

- **Postings and the A1 certificate.** Under Regulation (EC) No 883/2004 a worker is insured in one state at a time. Postings from Austria for up to 24 months stay under Austrian insurance with an A1 certificate. The conditions are in `at-cross-border`. An employee posted abroad still counts as employed in Austria for DB (FLAG § 41(1)) and DZ.
- **Non-resident employees.** Wages for work done in Austria are Austrian income of a non-resident (EStG § 98(1) no. 4) and go through Austrian payroll if the employer has an Austrian establishment. In payroll they get the Verkehrsabsetzbetrag and Pendlereuro but not the Familienbonus Plus or the sole-earner or single-parent credit (EStG § 70(2) Z 1). The non-resident add-on of EUR 11,077 applies on assessment, not in payroll (EStG § 102(3)): `at-cross-border`.
- **Foreign employer, no Austrian establishment.** No duty to withhold. Either run voluntary payroll (§ 47(1) lit. b), or send the § 84a wage certificate for employees with their centre of activity in Austria for more than six months (§ 47(1) lit. c). Social insurance follows Regulation 883/2004, not the tax rules: refer the registration of a foreign employer.
- **Treaty cases.** Where a treaty gives the taxing right on part of the wages to another state (for example work days abroad), refer the split payroll. The same applies to a severance or settlement that pays for years partly worked abroad: refer the split before applying the 6% or the one-fifth rule.

## Worked examples

### Example 1: salaried employee on EUR 4,000 a month in Graz (14 payments)

A salaried employee (Angestellte) in Graz, Styria, earns EUR 4,000 gross a month, paid 14 times. No Pendlerpauschale, no Familienbonus Plus, no sole-earner credit. The employer is a GmbH holding a trade licence, so it is a WKO member and pays DZ at the Styrian rate of 0.34%. The figures are for a normal month, not a bonus month.

1. Employee social insurance: 18.07% of EUR 4,000 = EUR 722.80. Pay is above EUR 2,630, so the full unemployment share applies, and below the EUR 6,930 cap.
2. Monthly tax base: EUR 4,000 less EUR 722.80 = EUR 3,277.20.
3. Annualised: EUR 3,277.20 x 12 = EUR 39,326.40, less the Werbungskostenpauschale of EUR 132 = EUR 39,194.40.
4. Tariff: EUR 1,690.60 (20% band) plus EUR 4,339.80 (30% band) plus 40% of EUR 2,736.40 (EUR 1,094.56) = EUR 7,124.96.
5. Less the Verkehrsabsetzbetrag of EUR 496 = EUR 6,628.96. Divided by 12 = EUR 552.41 wage tax for the month.
6. Net pay: EUR 4,000 less EUR 722.80 less EUR 552.41 = EUR 2,724.79.
7. Employer cost: social insurance 20.98% (EUR 839.20), MV 1.53% (EUR 61.20), DB 3.7% (EUR 148.00), DZ 0.34% (EUR 13.60), Kommunalsteuer 3% (EUR 120.00). Total on top of gross: EUR 1,182.00. Total cost: EUR 5,182.00.

In Vienna the WBF is 0.75% for each side, so the employee pays EUR 10 more social insurance and the employer EUR 10 more; DZ is 0.36%, and the employer also pays the Dienstgeberabgabe of EUR 2 for each started week.

```oa-check
name: Salaried employee, Graz, EUR 4,000 a month, normal month (2026)
inputs:
  gross: 4000
steps:
  - ee_sv: gross * 0.1807
  - tax_base_month: gross - ee_sv
  - annual_base: tax_base_month * 12 - 132
  - b20: (21992 - 13539) * 0.20
  - b30: (36458 - 21992) * 0.30
  - b40: (annual_base - 36458) * 0.40
  - annual_tax: b20 + b30 + b40 - 496
  - wage_tax: round(annual_tax / 12, 2)
  - net: gross - ee_sv - wage_tax
  - er_sv: gross * 0.2098
  - mv: gross * 0.0153
  - db: gross * 0.037
  - dz: gross * 0.0034
  - kommst: gross * 0.03
  - employer_cost: gross + er_sv + mv + db + dz + kommst
expected:
  ee_sv: 722.80
  tax_base_month: 3277.20
  annual_base: 39194.40
  annual_tax: 6628.96
  wage_tax: 552.41
  net: 2724.79
  er_sv: 839.20
  employer_cost: 5182.00
```

### Example 2: the first bonus of the year, EUR 4,000, paid with June pay

The same employee receives the holiday bonus of EUR 4,000 with the June salary. It is the first special payment of the year, so the EUR 620 allowance is still unused.

1. Jahressechstel: current pay received January to June is EUR 24,000. Converted to a year: EUR 48,000. One sixth: EUR 8,000. The bonus of EUR 4,000 is inside it, and the sixth is above EUR 2,615, so the fixed rates apply.
2. Employee social insurance on the bonus: 17.07% (no AK levy, no WBF) of EUR 4,000 = EUR 682.80. The special-payment cap of EUR 13,860 a year is not reached.
3. Tax base: EUR 4,000 less EUR 682.80 = EUR 3,317.20. Less the EUR 620 allowance = EUR 2,697.20, all inside the 6% slice. Tax: EUR 161.83.
4. Net bonus: EUR 4,000 less EUR 682.80 less EUR 161.83 = EUR 3,155.37.
5. Employer cost on the bonus: social insurance 20.48% (no WBF) EUR 819.20, MV EUR 61.20, DB EUR 148.00, DZ EUR 13.60, Kommunalsteuer EUR 120.00. Total EUR 5,162.00.
6. The Christmas bonus in November gets no second EUR 620: its tax is 6% of EUR 3,317.20 = EUR 199.03. By November the sixth is still EUR 8,000 (EUR 44,000 of current pay over 11 months, annualised to EUR 48,000), and EUR 4,000 of it is used, so the second bonus also fits.

```oa-check
name: First bonus of the year, EUR 4,000, salaried, Graz (2026)
inputs:
  bonus: 4000
  pay_to_june: 24000
  months_paid: 6
steps:
  - sixth: pay_to_june / months_paid * 12 / 6
  - ee_sv: bonus * 0.1707
  - tax_base: bonus - ee_sv
  - tax: round((tax_base - 620) * 0.06, 2)
  - net_bonus: bonus - ee_sv - tax
  - second_bonus_tax: round(tax_base * 0.06, 2)
  - er_sv: bonus * 0.2048
  - employer_cost: bonus + er_sv + bonus * 0.0153 + bonus * 0.037 + bonus * 0.0034 + bonus * 0.03
expected:
  sixth: 8000.00
  ee_sv: 682.80
  tax_base: 3317.20
  tax: 161.83
  net_bonus: 3155.37
  second_bonus_tax: 199.03
  er_sv: 819.20
  employer_cost: 5162.00
```

### Example 3: ten weekday overtime hours at a basic hourly pay of EUR 30

A wage-earning employee in Linz has a 40-hour week and monthly pay of EUR 5,190. The collective agreement uses the divisor 173, so the basic hourly pay is EUR 30. In March 2026 they work 10 overtime hours on weekdays, in daytime, each paid at the basic hourly pay plus a 50% supplement. There is no Sunday, holiday or night work and no SEG-Zulage, so the EUR 400 pot is not touched.

1. Basic pay for the overtime: 10 x EUR 30 = EUR 300. Always taxable.
2. Supplements: 10 x EUR 15 = EUR 150.
3. Weekday overtime pot for 2026: supplements for up to 15 hours, at most 50% of EUR 30 per hour (EUR 15), at most EUR 170. All 10 hours fit and EUR 150 is under EUR 170, so the whole EUR 150 is tax-free.
4. Social insurance: the full EUR 450 is Entgelt. Employee share 18.07% = EUR 81.32 (monthly total EUR 5,640, under the EUR 6,930 cap). The employer also pays its 20.98%, MV, DB, DZ and Kommunalsteuer on EUR 450.
5. Edge case: with 18 overtime hours instead, the supplements are EUR 270. Only the first 15 hours count (EUR 225), and the cap cuts that to EUR 170. So EUR 100 of supplement is taxable, plus EUR 540 of basic pay. Under the 2024 and 2025 rule (18 hours, EUR 200) EUR 200 would have been tax-free; under the permanent rule (10 hours, EUR 120) only EUR 120.

```oa-check
name: Weekday overtime supplements, EUR 30 basic hourly pay (2026)
inputs:
  monthly_pay: 5190
  divisor: 173
  hours: 10
  hours_b: 18
  rate: 0.5
steps:
  - hourly: monthly_pay / divisor
  - basic_ot: hours * hourly
  - supplement: hours * hourly * rate
  - tax_free: min(min(hours, 15) * hourly * min(rate, 0.5), 170)
  - taxable_supplement: supplement - tax_free
  - ee_sv_ot: round((basic_ot + supplement) * 0.1807, 2)
  - supplement_b: hours_b * hourly * rate
  - tax_free_b: min(min(hours_b, 15) * hourly * min(rate, 0.5), 170)
  - taxable_b: supplement_b - tax_free_b + hours_b * hourly
expected:
  hourly: 30.00
  basic_ot: 300.00
  supplement: 150.00
  tax_free: 150.00
  taxable_supplement: 0.00
  ee_sv_ot: 81.32
  supplement_b: 270.00
  tax_free_b: 170.00
  taxable_b: 640.00
```

### Example 4: old-system severance of three months' pay

The employee from Example 1 (EUR 4,000 a month in Graz, 14 payments) joined in 1999. On 1 January 2005 they moved to the new severance system by written agreement and kept their old claim frozen (BMSVG § 47(2)). The employer ends the employment on 30 September 2026. The frozen claim is three monthly pays, computed on the last month's pay of EUR 4,000, so EUR 12,000. Whether the monthly base should also include a share of the 13th and 14th salary is a labour-law point: confirm it before paying.

1. Vervielfachungsmethode: the tariff wage tax on one month's current pay is EUR 552.41 (Example 1, step 5). Times 3 = EUR 1,657.23.
2. Fixed rate: 6% of EUR 12,000 = EUR 720.00.
3. The lower figure applies: wage tax EUR 720.00. Net severance EUR 11,280.00.
4. No employee or employer social insurance (ASVG § 49(3) Z 7), no MV, and no DB, DZ or Kommunalsteuer (FLAG § 41(4) lit. b, KommStG § 5(2) lit. b). Employer cost is the EUR 12,000 itself.
5. For years from 2005 the employee's claim is against the BV-Kasse, not the employer. Suppose the employer also paid a voluntary EUR 12,000. Only service up to the transfer date of 1 January 2005 counts for § 67(6) (Z 7; LStR 2002 Rz 1087c), which is at least 5 years. Z 1: 6% on up to one quarter of the last 12 months' current pay (12 x EUR 4,000 / 4 = EUR 12,000). Z 2: 3/12 of EUR 48,000 = EUR 12,000 for 5 years, but the EUR 12,000 statutory severance cuts it to nil (Z 3). So the whole voluntary EUR 12,000 falls in the Z 1 slice and is taxed at 6% (EUR 720).

```oa-check
name: Old-system severance, three monthly pays of EUR 4,000 (2026)
inputs:
  monthly_pay: 4000
  months: 3
  monthly_wage_tax: 552.41
  voluntary: 12000
steps:
  - severance: monthly_pay * months
  - tax_multiple: monthly_wage_tax * months
  - tax_fixed: severance * 0.06
  - wage_tax: min(tax_multiple, tax_fixed)
  - net: severance - wage_tax
  - quarter_cap: min(monthly_pay * 12 / 4, 9 * 6930)
  - voluntary_tax: min(voluntary, quarter_cap) * 0.06
  - z2_slice: max(min(monthly_pay * 12 * 3 / 12, 3 * 6930 * 3) - severance, 0)
expected:
  severance: 12000.00
  tax_multiple: 1657.23
  tax_fixed: 720.00
  wage_tax: 720.00
  net: 11280.00
  quarter_cap: 12000.00
  voluntary_tax: 720.00
  z2_slice: 0.00
```

## Ask the client first

1. Where is each establishment, which municipality, and which Land? (Kommunalsteuer goes to the municipality; DZ, the Vienna WBF and the Vienna Dienstgeberabgabe depend on the Land.)
2. Is the employer a member of the Wirtschaftskammer, and does it have a permanent establishment in Austria? (DZ; whether wage tax must be withheld at all.)
3. Which collective agreement applies, and how many special payments does it give, and when? (13th and 14th salary, the Jahressechstel.)
4. For each employee: salaried or wage-earning, apprentice, marginal, or free service contractor; age (60 or over drops out of the DB base); start date (MV is free in the first month).
5. Has the employee claimed a Pendlerpauschale (form L 34 EDV), the Familienbonus Plus or a sole-earner credit with you?
6. Does anyone work abroad or come from abroad, and is there an A1 certificate?
7. For overtime: which divisor and which overtime and night rules does the collective agreement set, and are overtime hours recorded hour by hour? (The basic hourly pay, which hours fall in the EUR 400 pot and which in the EUR 170 pot.)
8. For a leaver: when did the employment start, was there a move to the new severance system and on what date, who ended it and how, and what does the termination agreement or settlement pay? (Old or new severance, § 67(3) or (6), the one-fifth rule, Urlaubsersatzleistung.)

## Sources

| Source | URL | Read on |
|---|---|---|
| EStG 1988 § 16 (Werbungskostenpauschale EUR 132) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=16 | 2026-10-23 |
| EStG § 33 (2026 tariff, Verkehrsabsetzbetrag, Pendlereuro) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=33 | 2026-10-23 |
| EStG § 41 (employee assessment, five years, recalculation of bonus tax) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=41 | 2026-10-23 |
| EStG § 47 (employer, foreign employer without establishment) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=47 | 2026-10-23 |
| EStG § 62 (deductions before the wage-tax tariff; Z 4 on contributions) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=62 | 2026-10-23 |
| EStG § 66 (wage-tax tariff, annualisation) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=66 | 2026-10-23 |
| EStG § 67 (special payments, EUR 620, 6%, Jahressechstel, EUR 2,615; termination payments in (3), (6), (8) and (10), as in force from 17 October 2026 and compared with the text in force on 1 March 2026) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=67 | 2026-10-23 |
| EStG § 76 (payroll account) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=76 | 2026-10-23 |
| EStG § 79 (paying over wage tax by the 15th) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=79 | 2026-10-23 |
| EStG § 82 (employer liability) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=82 | 2026-10-23 |
| EStG § 84 (Lohnzettel by end of February) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=84 | 2026-10-23 |
| FLAG 1967 § 41 (DB 3.7%, base, § 67(3) and (6) payments left out, EUR 1,460 relief, 2.7% from 2028) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008220&Paragraf=41 | 2026-10-23 |
| FLAG § 43 (DB due by the 15th) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008220&Paragraf=43 | 2026-10-23 |
| Kommunalsteuergesetz 1993 (§§ 5, 9, 11) | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004841 | 2026-10-23 |
| ASVG § 33 (registration before work starts) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008147&Paragraf=33 | 2026-10-23 |
| ASVG § 53a (marginal employment) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008147&Paragraf=53a | 2026-10-23 |
| ASVG § 54 (contributions on special payments) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008147&Paragraf=54 | 2026-10-23 |
| BMSVG § 6 (MV 1.53%) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20002088&Paragraf=6 | 2026-10-23 |
| BAO § 217 (late-payment surcharges) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10003940&Paragraf=217 | 2026-10-23 |
| ÖGK, Sozialversicherungswerte für 2026 (employer information sheet) | https://www.gesundheitskasse.at/cdscontent/load?contentid=10008.784766&version=1752580359 | 2026-10-23 |
| Dachverband, Beitragsrechtliche Werte in der Sozialversicherung 2026 | https://www.sozialversicherung.at/cdscontent/load?contentid=10008.806858 | 2026-10-23 |
| ÖGK, Arbeitsbehelf 2026 für Dienstgeberinnen und Dienstgeber | https://www.gesundheitskasse.at/cdscontent/load?contentid=10008.802672&version=1775628844 | 2026-10-23 |
| WKO, Zuschlag zum Dienstgeberbeitrag, DZ rates by Land 2026 | https://www.wko.at/lohnverrechnung/zuschlag-dienstgeberbeitrag | 2026-10-23 |
| EStG § 70 (wage tax of non-residents) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=70 | 2026-10-23 |
| EStG § 102 (non-resident add-on EUR 11,077) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=102 | 2026-10-23 |
| EStG § 18 and § 124b Z 285 and 286 (Sonderausgaben lump sum last applied for 2020) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=124b | 2026-10-23 |
| BMF, Lohnsteuerrichtlinien 2002 Rz 596 and 813a (no Sonderausgaben lump sum from 2021; order of the wage-tax computation) | https://findok.bmf.gv.at/findok/iwg/19/19974/19974.21.pdf | 2026-10-23 |
| Wiener Dienstgeberabgabegesetz §§ 3, 5, 6 (EUR 2 a week, over-55 exemption, deadlines) | https://www.ris.bka.gv.at/GeltendeFassung.wxe?Abfrage=LrW&Gesetzesnummer=20000133 | 2026-10-23 |
| BMF, Fristen und Fälligkeiten (15th of the month, L 16, DB 3.7%) | https://www.bmf.gv.at/themen/steuern/fristen-verfahren/fristen-faelligkeiten.html | 2026-10-23 |
| EStG § 68 (supplements: EUR 400, EUR 600 for night workers, 10 hours and EUR 120, overtime and night definitions), in force from 1 July 2026, and the versions in force on 1 January and 1 March 2026 | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=68 | 2026-10-23 |
| EStG § 124b Z 440 lit. b and c (overtime relief: 18 hours and EUR 200 for 2024 and 2025; 15 hours and EUR 170 for 2026), Z 492 and Z 494 (§ 68(1) roll-back deadlines) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004570&Paragraf=124b | 2026-10-23 |
| ASVG § 11(2) (insurance runs on for Kündigungsentschädigung, Urlaubsersatzleistung and settlements) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008147&Paragraf=11 | 2026-10-23 |
| ASVG § 49(3) Z 2 and Z 7 (dirt allowances and termination payments are not Entgelt) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10008147&Paragraf=49 | 2026-10-23 |
| BMSVG § 6(5) (MV base follows ASVG § 49) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20002088&Paragraf=6 | 2026-10-23 |
| BMSVG § 14 (claim against the BV-Kasse, exclusions, 36 contribution months) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20002088&Paragraf=14 | 2026-10-23 |
| BMSVG § 17 (payout and transfer options) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20002088&Paragraf=17 | 2026-10-23 |
| BMSVG § 46 (new system for employment beginning after 31 December 2002) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20002088&Paragraf=46 | 2026-10-23 |
| BMSVG § 47 (move to the new system, frozen old claim on the last month's pay) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=20002088&Paragraf=47 | 2026-10-23 |
| Kommunalsteuergesetz § 5 (base, § 67(3) and (6) payments excluded) | https://www.ris.bka.gv.at/NormDokument.wxe?Abfrage=Bundesnormen&Gesetzesnummer=10004841&Paragraf=5 | 2026-10-23 |
| BMF, Lohnsteuerrichtlinien 2002 as amended 18 December 2025, Rz 1087a and 1087c (§ 67(6) and the BV-Kasse), Rz 1121 (social insurance on tax-free supplements), Rz 1145 to 1148 (overtime: divisor 173, supplements under 50%, part-time Mehrarbeit, both pots per employer) | https://findok.bmf.gv.at/findok/iwg/19/19974/19974.26.pdf | 2026-10-23 |

Not yet confirmed: the fine range for late or missing wage-tax payments under the Finanzstrafgesetz, which was not read. The Lohnsteuerrichtlinien edition of 18 December 2025 is the latest on findok; it predates the 2026 overtime rule (15 hours, EUR 170), so only its method points are used and the figures come from § 124b Z 440 lit. c. Whether the DB, DZ and Kommunalsteuer exclusion reaches the part of a voluntary severance above the § 67(6) limits, or a voluntary severance paid to a new-system employee, was not read. The labour-law size of a severance (AngG § 23 months, and whether the monthly base includes a share of the 13th and 14th salary) was not read.

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
