---
name: italy-payroll
description: "Italian payroll for employees, tax year 2026: how the employer, as sostituto d'imposta, withholds IRPEF each month and settles it at the conguaglio. Covers the 2026 bands (23%, 33%, 43%), the employment detrazione, the cuneo fiscale (tax-free sum up to EUR 20,000, extra detrazione to EUR 40,000), the 2026 substitute taxes on pay rises, shift pay and productivity bonuses, regional and municipal surcharges, employee INPS (9.19% plus 1% above EUR 56,224, massimale EUR 122,295), TFR accrual and revaluation, tredicesima and quattordicesima, fringe benefits (EUR 1,000 or 2,000 with children; meal vouchers), F24 by the 16th, UniEmens, CU, 770, penalties and leave pay. Trigger on: busta paga, cedolino, ritenute IRPEF dipendenti, conguaglio, CU, 770, F24 1001, TFR, tredicesima, fringe benefit. Out of scope, see: it-employer-contributions, it-irpef-employees, it-income-tax, it-inps-contributions, it-impatriati, it-cross-border."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/italy-payroll"
  jurisdiction: "IT"
  tax_year: "2026"
  last_updated: "2026-10-24"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Italian payroll for employees: IRPEF withholding, INPS, TFR, CU and F24 (2026)

> **General reference only.** This skill is general tax reference material for AI-assisted work. No accountant has reviewed it. Do not run a payroll, file or pay on it without review by a qualified Italian professional (consulente del lavoro or commercialista).

How an Italian employer runs payroll for its employees in tax year 2026 (the calendar year). The employer is the sostituto d'imposta: it withholds IRPEF, the regional and municipal surcharges and the employee's INPS share from each pay, pays them by F24, and reports them on the CU and the 770 in 2027. The authority for tax is the Agenzia delle Entrate; for contributions, INPS. For 2026 pay the old TUIR (D.P.R. 917/1986) applies; the new TUIR (D.Lgs. 117/2026) applies from 1 January 2027. Every statute here was read as in force on 24 October 2026.

This skill does not repeat its siblings:

- employer INPS rates by sector and size, INAIL, the Fondo di Tesoreria, hiring reliefs, cost of an employee: `it-employer-contributions`;
- the employee's own return, family detrazioni, the trattamento integrativo in full, the 19% detrazioni: `it-irpef-employees`;
- self-employed IRPEF and the 20% withholding on fees in depth: `it-income-tax`; gestione separata: `it-inps-contributions`;
- inbound workers: `it-impatriati`; residence and treaties: `it-cross-border`.

## Who this applies to

- **Employers that pay employment income.** Companies, partnerships, sole traders, professionals and condominiums that pay employment income must withhold IRPEF on account when they pay (D.P.R. 600/1973 art. 23(1)).
- **Employees.** Employment income comes from work done for and under the direction of another, at any grade, including home workers treated as employees (TUIR art. 49(1)). Pay is everything received in the year in connection with the job, including pay for the year paid by 12 January of the next year (TUIR art. 51(1)).
- **The cuneo fiscale** goes to employees under TUIR art. 49, not to pensioners (L. 207/2024 art. 1 commi 4 and 6).
- **Out of scope:** dirigenti, apprentices in detail, agricultural, domestic, entertainment, construction and public-sector workers (special INPS schemes, see `it-employer-contributions`); termination packages, TFR advances and settlements; any payslip that will actually be paid without professional sign-off.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| IRPEF band 1, taxable income up to EUR 28,000 | 23% | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=2026-10-24 |
| IRPEF band 2, EUR 28,000 to 50,000 (35% in 2024 and 2025) | 33% | 2026 | L. 199/2025 art. 1 comma 3, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199~art1!vig=2026-10-24 |
| IRPEF band 3, above EUR 50,000 | 43% | 2026 | TUIR art. 11, link above |
| Gross tax on the first EUR 50,000 (was 14,140) | EUR 13,700 | 2026 | https://www.agenziaentrate.gov.it/portale/imposta-sul-reddito-delle-persone-fisiche-irpef-/aliquote-e-calcolo-dell-irpef |
| Employment detrazione, total income up to EUR 15,000 (at least 690; 1,380 for fixed-term contracts) | EUR 1,955 | 2026 | TUIR art. 13(1)(a), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig=2026-10-24 |
| Employment detrazione, EUR 15,000 to 28,000 | EUR 1,910 + 1,190 x (28,000 - total income) / 13,000 | 2026 | TUIR art. 13(1)(b), link above |
| Employment detrazione, EUR 28,000 to 50,000; nil above 50,000 | EUR 1,910 x (50,000 - total income) / 22,000 | 2026 | TUIR art. 13(1)(c), link above |
| Extra employment detrazione, total income above EUR 25,000 and not above 35,000 | EUR 65 | 2026 | TUIR art. 13(1.1), link above |
| Cuneo fiscale tax-free sum, total income up to EUR 20,000: share of employment income up to 8,500 / up to 15,000 / above 15,000 | 7.1% / 5.3% / 4.8% | 2026 | L. 207/2024 art. 1 commi 4-5, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-24 |
| Cuneo fiscale extra detrazione, total income above EUR 20,000 and up to 32,000 | EUR 1,000 | 2026 | L. 207/2024 art. 1 comma 6(a), link above |
| Same, total income above EUR 32,000 and up to 40,000; nil above 40,000 | EUR 1,000 x (40,000 - total income) / 8,000 | 2026 | L. 207/2024 art. 1 comma 6(b), link above |
| Cuneo wrongly granted: recovered in ten equal instalments if above | EUR 60 | 2026 | L. 207/2024 art. 1 comma 7, link above |
| Trattamento integrativo, total income up to EUR 15,000 (up to 28,000 under conditions) | EUR 1,200 | 2026 | D.L. 3/2020 art. 1(1), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2020-02-05;3~art1!vig=2026-10-24 |
| Substitute tax on 2026 pay rises from contract renewals signed 1 January 2024 to 31 December 2026; private sector; 2025 employment income up to EUR 33,000 | 5% | 2026 | L. 199/2025 art. 1 comma 7, link above |
| Substitute tax on night, holiday, rest-day and shift supplements up to EUR 1,500 a year; private sector; 2025 employment income up to EUR 40,000 | 15% | 2026 | L. 199/2025 art. 1 commi 10-11, link above |
| Substitute tax on productivity bonuses and profit shares paid in 2026 and 2027, up to EUR 5,000 | 1% | 2026 | L. 199/2025 art. 1 comma 9, link above |
| Trattamento integrativo speciale, tourism and food-service staff, 1 January to 30 September 2026, 2025 employment income up to EUR 40,000: share of gross pay for night work and holiday overtime | 15% | 2026 | L. 199/2025 art. 1 commi 18-21, link above |
| Addizionale regionale, base rate (regions may add up to 2.1 points) | 1.23% | 2026 | D.Lgs. 68/2011 art. 6, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2011-05-06;68~art6!vig=2026-10-24 |
| Addizionale comunale: maximum total variation of the rate; acconto as share of the prior-year surcharge | 0.8 points; 30% | 2026 | D.Lgs. 360/1998 art. 1, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1998-09-28;360~art1!vig=2026-10-24 |
| Employee INPS pension share, Fondo pensioni lavoratori dipendenti (total IVS 33%, so 23.81% employer) | 9.19% | 2026 | https://servizi2.inps.it/servizi/Bussola/visualizzadoc.aspx?svirtualurl=%2Fcircolari%2Fcircolare+numero+40+del+22-02-2011.htm |
| Extra employee contribution on pay above the first pension band of EUR 56,224 a year (EUR 4,685 a month) | 1% | 2026 | INPS Circolare 6/2026 para. 5, https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/01/Circolare_15151/Allegati/16546_Circolare-numero-6-del-30-01-2026.pdf |
| Massimale, workers first insured from 1 January 1996 | EUR 122,295 | 2026 | INPS Circolare 6/2026 para. 6, link above |
| Minimum daily pay for contributions (part-time on a 40-hour week: EUR 8.72 an hour) | EUR 58.13 | 2026 | INPS Circolare 6/2026 para. 2, link above |
| TFR accrual: yearly pay divided by 13.5 | 7.41% | 2026 | Civil Code art. 2120, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2120!vig=2026-10-24 |
| Contribution deducted from the TFR accrual (0.30 + 0.20; net accrual about 6.91%) | 0.50% | 2026 | L. 297/1982 art. 3, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1982-05-29;297~art3!vig=2026-10-24 |
| TFR revaluation each 31 December: fixed part, plus 75% of the ISTAT price rise since December | 1.5% | 2026 | Civil Code art. 2120, link above |
| Substitute tax on the TFR revaluation (acconto: 90% of the prior year's revaluation) | 17% | 2026 | D.Lgs. 47/2000 art. 11(3)-(4), https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2000-02-18;47~art11!vig=2026-10-24 |
| Fringe benefits (goods, services, home utilities, rent or mortgage interest on the main home) exempt up to | EUR 1,000; EUR 2,000 with dependent children | 2025-2027 | L. 207/2024 art. 1 commi 390-391, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-24 |
| Standing fringe-benefit limit in the TUIR, replaced for 2025 to 2027 | EUR 258.23 | 2026 | TUIR art. 51(3), https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art51!vig=2026-10-24 |
| Meal vouchers exempt per day: paper / electronic (electronic was EUR 8) | EUR 4 / EUR 10 | 2026 | TUIR art. 51(2)(c) as amended by L. 199/2025 art. 1 comma 14 |
| Company car for mixed use: taxable share of the ACI cost for 15,000 km (10% battery electric, 20% plug-in hybrid) | 50% | 2026 | TUIR art. 51(4)(a), link above |
| Fee withholding on resident professionals (on account) / non-residents for work done in Italy (final) | 20% / 30% | 2026 | https://www.agenziaentrate.gov.it/portale/schede/pagamenti/versamento-modello-f24-ritenute-su-reddito-di-lavoro-autonomo-f24_rit_red_lav_aut/aliquote-f24_rit_red_lav_aut |
| Legal interest rate for ravvedimento | 1.60% | 2026 | D.M. 10 December 2025, GU n. 289 of 13 December 2025 |

## The taxable base

**Monthly withholding (D.P.R. 600/1973 art. 23(2)).**
- Each pay period the employer applies the IRPEF bands scaled to the pay period, less the art. 12 and 13 detrazioni scaled to the same period. Family detrazioni (art. 12) apply only if the employee declares the right and gives the codici fiscali.
- **Tredicesima and other extra months** are taxed on their own, with the yearly bands scaled to one month (art. 23(2)(b)). They then enter the conguaglio.
- **Arrears from earlier years** are taxed separately, using as total income the employment pay from this employer in the two prior years (art. 23(2)(c)); F24 code 1002.
- **TFR** is taxed separately at the employee's own average rate (TUIR art. 19; art. 23(2)(d)); F24 code 1012.

**What is taxed.**
- Taxable pay is gross pay less the employee's compulsory social contributions (TUIR art. 51(2)(a)) and less exempt items.
- **Tredicesima.** One extra month's pay, usually in December, set by the CCNL, not by statute. **Quattordicesima.** Only where the CCNL gives it, usually June or July. Both carry IRPEF and INPS.
- **Fringe benefits for 2026.** These are goods and services given to employees, plus sums paid or refunded for home water, electricity and gas, rent of the main home or interest on its mortgage. They are not income up to EUR 1,000. The limit is EUR 2,000 for an employee with dependent children who declares it and gives the children's codici fiscali (L. 207/2024 commi 390-391). The employer must first inform the unions.
- The fringe limit replaces only the EUR 258.23 figure in TUIR art. 51(3). The rest of art. 51(3) still applies: if the total goes above the limit, the whole value is taxed, not only the excess.
- **The same base for INPS.** The contribution base is pay as defined in TUIR art. 51 (L. 153/1969 art. 12(2), as replaced by D.Lgs. 314/1997 art. 6). Fringe benefits within the limit are out of the INPS base too; above the limit, the whole value carries employee and employer INPS.
- **Meal vouchers** are exempt up to EUR 4 a day on paper and EUR 10 electronic (art. 51(2)(c)).
- **Company cars** for mixed use: the taxable value is 50% of the ACI cost for 15,000 km (10% battery electric, 20% plug-in hybrid), less what the employee pays. Values rise by 50% after 31 December of the fifth year after first registration (art. 51(4)(a)).
- **Also outside pay:** contractual health fund contributions up to EUR 3,615.20 (art. 51(2)(a)), and welfare and education services for all staff or categories of staff (art. 51(2)(f), (f-bis)).

**The cuneo fiscale (L. 207/2024 art. 1 commi 4 to 9).**
- **Total income up to EUR 20,000:** a tax-free sum, a share of employment income (7.1%, 5.3% or 4.8%). It is not income. The band uses employment income scaled to a full year (comma 5). The employer pays it in the payslip and recovers it by F24 offset, code 1704 (comma 8).
- **Total income above EUR 20,000 and up to 40,000:** an extra detrazione from gross tax, pro rata to the period worked.
- The employer grants both automatically and checks them at the conguaglio. If a sum turns out not due, it recovers it; above EUR 60, in ten equal instalments (comma 7).
- Total income includes exempt impatriati income and excludes the main home (comma 9).

**Other 2026 measures (L. 199/2025 art. 1).**
- The 5%, 15% and 1% substitute taxes replace IRPEF and both surcharges unless the employee waives them in writing (commi 7, 9, 10).
- Supplements that replace ordinary pay are not covered (comma 11). Productivity bonuses do not count towards the EUR 1,500 limit (comma 11).
- If another employer issued the 2025 CU, the employee states the 2025 employment income in writing (comma 11).
- The 5% rate on productivity bonuses (L. 207/2024 comma 385) now covers 2025 only (L. 199/2025 comma 8).
- The trattamento integrativo speciale (15%) is paid on request and recovered by F24 offset (commi 20-21).

**Trattamento integrativo (D.L. 3/2020 art. 1).** EUR 1,200 a year, not income, when total income is up to EUR 15,000 and gross tax on employment income is above the employment detrazione less EUR 75 (scaled to the period worked). Between EUR 15,000 and 28,000 it is paid only if certain detrazioni exceed gross tax. Full rules: `it-irpef-employees`.

**Surcharges.**
- **Regional.** Fixed at the conguaglio. Withheld in up to eleven instalments from the next pay period, ending no later than the pay whose withholding is paid in December. On leaving, all at once (D.Lgs. 446/1997 art. 50(4)).
- **Municipal.** The acconto (30% of the prior year's surcharge) is withheld in up to nine monthly instalments from March. The balance is fixed at the conguaglio and withheld like the regional one (D.Lgs. 360/1998 art. 1(5)).
- Rates follow the employee's domicile. Each region and comune sets its own.

**The conguaglio (art. 23(3)-(4)).** By 28 February of the next year, or when the job ends, the employer recomputes the year's tax on all pay and settles the difference. It also counts the detrazioni for oneri it withheld for. The employee can ask it to include pay from earlier jobs in the year by handing over that CU by 12 January.

**Employee INPS.**
- The employer withholds the employee share each pay period and pays both shares.
- The general rate is 9.19% (FPLD). Employers in the FIS or CIGS add a small employee share (for example 0.27% or 0.30%; see `it-employer-contributions`).
- One more point is due on pay above EUR 4,685 in the month (INPS Circolare 6/2026 para. 5).
- Contributions are due on at least the CCNL pay and EUR 58.13 a day.
- For workers first insured from 1996, no pension contributions are due above EUR 122,295.

**TFR (Civil Code art. 2120; L. 297/1982 art. 3).**
- Each year the employer sets aside pay divided by 13.5. It deducts from that accrual the 0.50% contribution it pays to INPS, so the employee's TFR grows by about 6.91% of pay.
- On 31 December the fund is revalued at 1.5% plus 75% of the ISTAT price rise. The employer pays a 17% substitute tax on the revaluation and charges it to the fund, with an acconto of 90% of the prior year's revaluation (D.Lgs. 47/2000 art. 11).
- Where the TFR goes (employer, pension fund, or the INPS Fondo di Tesoreria) and the 2026 headcount rule are in `it-employer-contributions`.

**Leave pay and working time, as set by law.**
- Annual leave is at least four weeks; at least two are taken in the year. The minimum cannot be paid out except on termination (D.Lgs. 66/2003 art. 10).
- Maternity leave runs two months before and three after the birth (D.Lgs. 151/2001 art. 16), paid at 80% of pay (art. 22).
- Paternity leave is ten working days (twenty for multiple births), from two months before to five months after the birth (art. 27-bis), paid at 100% (art. 29).
- Parental leave is paid at 30% until the child is 14. Up to three months in total between the parents are paid at 80% until the child is 6 (art. 34).
- The normal week is 40 hours (D.Lgs. 66/2003 art. 3). The average including overtime is at most 48 hours over four months, extendable by CCNL (art. 4). Without a CCNL rule, overtime needs the employee's agreement and is capped at 250 hours a year (art. 5).
- There is no statutory national minimum wage: pay, overtime and night rates come from the CCNL.

## Deadlines and filing

| Obligation | Deadline for 2026 pay | Law |
|---|---|---|
| F24: IRPEF, surcharges, substitute taxes and INPS withheld | 16th of the month after payment; next working day if a Saturday or holiday | D.Lgs. 241/1997 art. 18(1) |
| UniEmens (monthly pay and contribution data to INPS) | Last day of the month after the pay month | D.L. 269/2003 art. 44(9) |
| Conguaglio | By 28 February 2027, or when the job ends | D.P.R. 600/1973 art. 23(3) |
| CU to the employee | 16 March 2027; within 12 days of a request if the job ends | D.P.R. 322/1998 art. 4(6-quater) |
| CU to the Agenzia delle Entrate | 16 March 2027 | art. 4(6-quinquies) |
| CU with only professional fees or agents' commissions | 30 April 2027 | art. 4(6-quinquies) |
| Modello 770 | 31 October 2027 is a Sunday and 1 November a holiday, so 2 November 2027 | art. 4(3-bis); D.L. 70/2011 art. 7(2)(l) |
| Employee's 730 (2025 income) | 30 September 2026; the employer applies the refund or debit in payroll | Agenzia, 730/2026 page |

**F24 codici tributo** (Agenzia list for the 770/2026):

| Code | What |
|---|---|
| 1001 | IRPEF withheld on pay, extra months and the conguaglio |
| 1002 | IRPEF withheld on arrears |
| 1012 | IRPEF withheld on TFR and other termination payments |
| 1040 | Withholding on fees for arts and professions |
| 3802 | Addizionale regionale withheld |
| 3847 / 3848 | Addizionale comunale withheld, acconto / saldo |
| 1704 | Employer's credit for the cuneo tax-free sum, used in offset |

INPS contributions go in the INPS section of the same F24. INAIL's autoliquidazione (16 February) is in `it-employer-contributions`.

**The payslip (busta paga).** It shows the employer and employee details, CCNL, grade and pay period. It also shows hours, overtime, each pay element and gross pay; INPS, IRPEF and surcharges withheld; detrazioni and the cuneo sum; TFR accrued; leave and permits accrued, used and left; and net pay. It can be on paper or electronic.

**How payroll shows on bank statements.** Credits: STIPENDIO, EMOLUMENTI, BUSTA PAGA (net pay); TREDICESIMA or 13A MENSILITA; QUATTORDICESIMA; TFR or LIQUIDAZIONE; INDENNITA MALATTIA or MATERNITA INPS; RIMBORSO 730. Employer debits: F24 IRPEF or RITENUTE; F24 INPS; INAIL PREMIO; FONDO TESORERIA INPS; FONDO PENSIONE.

**Bookkeeping.** Gross pay, employer INPS, INAIL and the TFR accrual are costs. Amounts withheld are debts to the Erario and to INPS until paid by F24. TFR sits in the TFR fund until paid or transferred. CU data feed the employee's 730 or Redditi PF; UniEmens totals reconcile with the F24 and the CU.

## Penalties and interest

- **Withholding not paid on time:** 25% of the amount. Paid within 90 days, half (12.5%). Paid within 15 days, 1/15 of the halved rate for each day late (D.Lgs. 471/1997 art. 13(1)).
- **Withholding not made:** 20% of the amount not withheld (art. 14(1)).
- **770 not filed:** 120% of the withholding not paid, at least EUR 250. If all withholding was paid, EUR 250 to 2,000. Plus EUR 50 for each payee left out (art. 2(1) and (4)).
- **770 filed more than 90 days late,** before any audit: the art. 13 penalty tripled on the withholding not paid (art. 2(1-bis)).
- **Pay understated in the 770:** 70% of the withholding not paid, at least EUR 250 (art. 2(2)).
- **CU missing, late or wrong:** EUR 100 per certificate, up to EUR 50,000 per employer. No penalty if a wrong CU is corrected within five days. Cut to a third (up to EUR 20,000) if sent correctly within 60 days (D.P.R. 322/1998 art. 4(6-quinquies)).
- **Ravvedimento** (before any audit): the penalty falls to 1/10 of the minimum if paid within 30 days, to 1/9 within 90 days, and to 1/8 by the return deadline for the year of the breach. Interest at the legal rate (1.60% for 2026) runs day by day (D.Lgs. 472/1997 art. 13(1)).
- **Employee INPS withheld and not paid:** see `it-employer-contributions`.

## Cross-border points

- **Non-resident employees.** Employment income for work done in Italy is Italian-source (TUIR art. 23(1)(c)). An Italian employer withholds on it as for residents. Treaties can remove the Italian tax; see `it-cross-border`.
- **Residents working abroad.** An employee may work abroad continuously and only there, staying more than 183 days in 12 months. The taxable base is then the yearly retribuzioni convenzionali set by ministerial decree, not actual pay (TUIR art. 51(8-bis)). The employer still withholds on it (D.P.R. 600/1973 art. 23(1-bis)).
- **Impatriati.** The exempt part of an impatriato's pay still counts in total income for the cuneo fiscale (L. 207/2024 comma 9). Regime rules: `it-impatriati`.
- **Social security.** Which country's contributions apply, A1 certificates and postings: `it-employer-contributions`.
- **Fees to non-resident professionals** for work done in Italy: 30% final withholding, F24 code 1040, subject to treaty relief.

## Worked examples

### Example 1: Office employee, gross EUR 32,000, small industrial firm (2026)

An impiegato at an industrial firm with 10 staff works the whole of 2026 for gross pay of EUR 32,000. The firm has no CIGS or FIS employee share, so employee INPS is 9.19%. No other income, no family detrazioni.

Employee INPS: 9.19% of 32,000 = EUR 2,940.80. Taxable pay and total income: EUR 29,059.20. Gross tax: 23% of 28,000 = 6,440, plus 33% of 1,059.20 = 349.54, total EUR 6,789.54. Employment detrazione: (50,000 - 29,059.20) / 22,000 = 0.951854, kept to four decimals as 0.9518, times 1,910 = EUR 1,817.94. Total income is between 25,000 and 35,000, so add EUR 65. Total income is between 20,000 and 32,000, so the cuneo extra detrazione is EUR 1,000. Net IRPEF at the conguaglio: 6,789.54 - 1,817.94 - 65 - 1,000 = EUR 3,906.60, before the surcharges. TFR set aside: 32,000 / 13.5 = 2,370.37, less 0.50% of 32,000 = 160, so EUR 2,210.37.

```oa-check
name: Employee EUR 32,000 gross, industrial firm up to 15 staff, IRPEF and TFR (2026)
inputs:
  gross: 32000
steps:
  - inps_ee: round(gross * 0.0919, 2)
  - taxable: gross - inps_ee
  - band_23: min(taxable, 28000) * 0.23
  - band_33: (min(taxable, 50000) - 28000) * 0.33
  - gross_tax: round(band_23 + band_33, 2)
  - ratio: floor((50000 - taxable) / 22000 * 10000) / 10000
  - detrazione: round(1910 * ratio, 2)
  - extra_65: 65
  - cuneo_detrazione: 1000
  - net_irpef: gross_tax - detrazione - extra_65 - cuneo_detrazione
  - tfr_gross: round(gross / 13.5, 2)
  - tfr_net: tfr_gross - gross * 0.005
expected:
  inps_ee: 2940.80
  taxable: 29059.20
  gross_tax: 6789.54
  ratio: 0.9518
  detrazione: 1817.94
  net_irpef: 3906.60
  tfr_gross: 2370.37
  tfr_net: 2210.37
```

### Example 2: Low earner with a child, cuneo tax-free sum and the fringe-benefit cliff (2026)

Same kind of firm. An employee earns gross pay of EUR 17,000 for the whole year and has one dependent child. The employer refunds EUR 1,800 of home electricity and gas bills. The employee has declared the child's codice fiscale, so the limit is EUR 2,000 and the refund is not income.

Employee INPS: 9.19% of 17,000 = EUR 1,562.30. Taxable pay and total income: EUR 15,437.70. Total income is up to EUR 20,000, so the cuneo is the tax-free sum. Employment income is above 15,000, so the share is 4.8%: EUR 741.01, paid in the payslip and not taxed. Gross tax: 23% = EUR 3,550.67. Employment detrazione: (28,000 - 15,437.70) / 13,000 = 0.966331, kept as 0.9663, times 1,190 = 1,149.90, plus 1,910 = EUR 3,059.90. Net IRPEF: EUR 490.77. Income is above 15,000 and the detrazione is below gross tax, so there is no trattamento integrativo. Net cash for the year: 17,000 - 1,562.30 - 490.77 + 741.01 = EUR 15,687.94, plus the EUR 1,800 refund.

The edge case: had the refunds been EUR 2,100, the limit is passed and all EUR 2,100 is taxed, not just the EUR 100 excess (TUIR art. 51(3)). It also enters the INPS base (L. 153/1969 art. 12(2)): employee INPS becomes 9.19% of 19,100 = EUR 1,755.29. Taxable income becomes 19,100 - 1,755.29 = EUR 17,344.71. The tax-free sum rises to 4.8% of it, EUR 832.55. Gross tax becomes EUR 3,989.28. The detrazione ratio is (28,000 - 17,344.71) / 13,000 = 0.819637, kept as 0.8196, so the detrazione falls to 1,910 + 975.32 = EUR 2,885.32, and net IRPEF rises to EUR 1,103.96.

```oa-check
name: Employee EUR 17,000 gross, cuneo tax-free sum, fringe benefit within and over EUR 2,000 (2026)
inputs:
  gross: 17000
  fringe_over: 2100
steps:
  - inps_ee: round(gross * 0.0919, 2)
  - taxable: gross - inps_ee
  - cuneo_sum: round(taxable * 0.048, 2)
  - gross_tax: round(taxable * 0.23, 2)
  - ratio: floor((28000 - taxable) / 13000 * 10000) / 10000
  - detrazione: 1910 + round(1190 * ratio, 2)
  - net_irpef: gross_tax - detrazione
  - net_cash: gross - inps_ee - net_irpef + cuneo_sum
  - inps_ee_over: round((gross + fringe_over) * 0.0919, 2)
  - taxable_over: gross + fringe_over - inps_ee_over
  - cuneo_sum_over: round(taxable_over * 0.048, 2)
  - gross_tax_over: round(taxable_over * 0.23, 2)
  - ratio_over: floor((28000 - taxable_over) / 13000 * 10000) / 10000
  - detrazione_over: 1910 + round(1190 * ratio_over, 2)
  - net_irpef_over: gross_tax_over - detrazione_over
expected:
  inps_ee: 1562.30
  taxable: 15437.70
  cuneo_sum: 741.01
  gross_tax: 3550.67
  ratio: 0.9663
  detrazione: 3059.90
  net_irpef: 490.77
  net_cash: 15687.94
  inps_ee_over: 1755.29
  taxable_over: 17344.71
  cuneo_sum_over: 832.55
  gross_tax_over: 3989.28
  ratio_over: 0.8196
  detrazione_over: 2885.32
  net_irpef_over: 1103.96
```

## Ask the client first

- Which CCNL applies, and what grade and contract does the employee have (permanent, fixed-term, part-time, apprentice)? This sets pay, extra months, the detrazione floor and the INPS class.
- How many staff does the firm have, and in which sector? This sets the employee's extra INPS share and where the TFR goes.
- When was the employee first insured with INPS: before 1996, or from 1996 (massimale)?
- What was the employee's 2025 employment income, and any other 2026 income? This decides the cuneo fiscale and the 5%, 15% and 1% substitute taxes.
- Where is the employee's tax domicile, and do they have dependent children (surcharges, fringe-benefit limit)?
- Did the employee work for another employer earlier in 2026, and do they want that pay in the conguaglio?

## Sources

| Source | URL | Read on |
|---|---|---|
| TUIR, D.P.R. 917/1986, art. 11 (bands) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art11!vig=2026-10-24 | 2026-10-24 |
| TUIR art. 13 (employment detrazione, four decimals) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art13!vig=2026-10-24 | 2026-10-24 |
| TUIR art. 19 (TFR taxation) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art19!vig=2026-10-24 | 2026-10-24 |
| TUIR art. 23 (non-residents, Italian-source income) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art23!vig=2026-10-24 | 2026-10-24 |
| TUIR art. 49 (employment income) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art49!vig=2026-10-24 | 2026-10-24 |
| TUIR art. 51 (taxable pay, meal vouchers, fringe benefits, cars, work abroad) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art51!vig=2026-10-24 | 2026-10-24 |
| L. 199/2025 (Legge di Bilancio 2026), art. 1 commi 3, 7-21 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199~art1!vig=2026-10-24 | 2026-10-24 |
| L. 207/2024 (Legge di Bilancio 2025), art. 1 commi 3-9 (cuneo fiscale), 385, 390-391 (fringe benefits) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-10-24 | 2026-10-24 |
| D.L. 3/2020 art. 1 (trattamento integrativo) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2020-02-05;3~art1!vig=2026-10-24 | 2026-10-24 |
| D.P.R. 600/1973 art. 23 (withholding, conguaglio) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1973-09-29;600~art23!vig=2026-10-24 | 2026-10-24 |
| D.P.R. 322/1998 art. 4 (CU, 770, CU penalty) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-07-22;322~art4!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 68/2011 art. 6 (addizionale regionale) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2011-05-06;68~art6!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 446/1997 art. 50 (regional surcharge withholding) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-15;446~art50!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 360/1998 art. 1 (addizionale comunale) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1998-09-28;360~art1!vig=2026-10-24 | 2026-10-24 |
| L. 153/1969 art. 12, as replaced by D.Lgs. 314/1997 art. 6 (INPS base follows TUIR art. 51) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-09-02;314~art6!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 241/1997 art. 18 (F24 by the 16th) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-07-09;241~art18!vig=2026-10-24 | 2026-10-24 |
| D.L. 269/2003 art. 44 (UniEmens) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2003-09-30;269~art44!vig=2026-10-24 | 2026-10-24 |
| D.L. 70/2011 art. 7(2)(l) (deadlines on a Saturday or holiday) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-05-13;70~art7!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 471/1997 arts. 2, 13, 14 (penalties) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art2!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 472/1997 art. 13 (ravvedimento) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-10-24 | 2026-10-24 |
| D.M. 10 December 2025, legal interest rate for 2026 (GU n. 289, 13 December 2025) | https://www.gazzettaufficiale.it/atto/vediMenuHTML?atto.dataPubblicazioneGazzetta=2025-12-13&atto.codiceRedazionale=25A06705&tipoSerie=serie_generale&tipoVigenza=originario | 2026-10-24 |
| Civil Code art. 2120 (TFR) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2120!vig=2026-10-24 | 2026-10-24 |
| L. 297/1982 art. 3 (0.50% deducted from TFR) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1982-05-29;297~art3!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 47/2000 art. 11 (17% on TFR revaluation) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2000-02-18;47~art11!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 66/2003 arts. 3, 4, 5, 10 (hours, overtime, leave) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2003-04-08;66~art10!vig=2026-10-24 | 2026-10-24 |
| D.Lgs. 151/2001 arts. 16, 22, 27-bis, 29, 34 (maternity, paternity, parental leave) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2001-03-26;151~art34!vig=2026-10-24 | 2026-10-24 |
| INPS Circolare 6 of 30 January 2026 (minimum pay, extra 1%, massimale) | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/01/Circolare_15151/Allegati/16546_Circolare-numero-6-del-30-01-2026.pdf | 2026-10-24 |
| INPS Circolare 40/2011 (employee pension share 9.19%) | https://servizi2.inps.it/servizi/Bussola/visualizzadoc.aspx?svirtualurl=%2Fcircolari%2Fcircolare+numero+40+del+22-02-2011.htm | 2026-10-24 |
| Agenzia delle Entrate, IRPEF rates (33% from 2026) | https://www.agenziaentrate.gov.it/portale/imposta-sul-reddito-delle-persone-fisiche-irpef-/aliquote-e-calcolo-dell-irpef | 2026-10-24 |
| Agenzia delle Entrate, F24 codes for the 770/2026 | https://www.agenziaentrate.gov.it/portale/documents/20143/9741427/allegato+1+-+codici+tributo+F24_770-2026.pdf/d9d83f8b-d8e0-3045-4469-e7bd3301026a?t=1771600455976 | 2026-10-24 |
| Agenzia delle Entrate, withholding rates on self-employed income | https://www.agenziaentrate.gov.it/portale/schede/pagamenti/versamento-modello-f24-ritenute-su-reddito-di-lavoro-autonomo-f24_rit_red_lav_aut/aliquote-f24_rit_red_lav_aut | 2026-10-24 |
| Agenzia delle Entrate, when to file the 730/2026 | https://www.agenziaentrate.gov.it/portale/quando-e-come-presentare-il-730-2026 | 2026-10-24 |

Not yet confirmed:

- **Consolidated codes from 2027.** The conguaglio, CU, 770 and F24 payments for 2026 pay fall in 2027, when D.Lgs. 33/2025 (payments) and D.Lgs. 173/2024 (penalties) apply with new article numbers. We did not read whether they change any date or figure above.
- **Sick pay (malattia).** INPS pays from day 4 for up to 180 days a year at a share of pay set by law; the first three days are usually paid by the employer under the CCNL. Neither the percentages nor the statute were read.
- **Payslip law.** The payslip contents above follow L. 4/1953, which was not re-read.
- **Regional and municipal rates for 2026** and the 2027 acconto: each region and comune sets its own; none read.
- **Criminal thresholds** for unpaid withholding (D.Lgs. 74/2000) were not read.
- **Moved, not dropped:** employer INPS rates by sector, the Fondo di Tesoreria and its 2026 headcount rule, INAIL autoliquidazione and the 2026 hiring reliefs are in `it-employer-contributions`. Family detrazioni and the 19% detrazioni (including the EUR 440 cut above EUR 200,000) are in `it-irpef-employees` and `it-income-tax`. The Modello Redditi PF deadline is in `it-income-tax`.

> Contributed by OpenAccountants.

> Contributed by Ryan Duguid.

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-24. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `italy-payroll` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/italy-payroll. If neither is available, confirm every figure against the official source pages cited above before relying on it.
