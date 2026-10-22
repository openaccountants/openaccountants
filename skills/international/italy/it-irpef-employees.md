---
name: it-irpef-employees
description: "Italian personal income tax (IRPEF) for resident employees, pensioners and private investors, tax year 2026. Covers the 2026 bands (23%, 33%, 43%; the middle rate cut from 35% by L. 199/2025), the employment and pension detrazioni of TUIR art. 13, the cuneo fiscale measures of L. 207/2024 (tax-free sum and extra detrazione), family detrazioni, the main oneri deducibili and detraibili with their caps, regional and municipal surcharges, 730 or Redditi PF and the 2027 deadlines, the 26% and 12.5% substitute taxes on investment income, rental income and cedolare secca (21%, 26%, 10%), IVIE and IVAFE on foreign assets, penalties and ravvedimento. Trigger on: IRPEF dipendente, 730, busta paga tax, detrazioni lavoro dipendente, cedolare secca, capital gains Italy, IVAFE, IVIE. Out of scope, see: it-income-tax (self-employed), italy-payroll (withholding), it-estimated-tax, it-impatriati, italy-crypto-tax, it-cross-border."
jurisdiction: IT
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-22
version: 0.1
verified_by: pending
---

# Italy: income tax for employees, pensioners and investment income (2026)

> **General reference only.** This skill is general tax reference material for AI-assisted work. No accountant has reviewed it. Do not rely on it to file, pay or take a tax position without review by a qualified Italian professional (commercialista or CAF).

This skill covers what a resident employee or pensioner owes for 2026 and how they file it, plus the investment and rental income such a person usually has. The tax year is the calendar year. The authority is the Agenzia delle Entrate. Currency is the euro.

It does not repeat what sibling skills already hold:

- self-employed and professional income (regime ordinario), and the forfettario summary: `it-income-tax`;
- how the employer withholds month by month, INPS, TFR and the CU: `italy-payroll`;
- acconti (payments on account) in detail: `it-estimated-tax`;
- inbound workers and the flat tax for new residents: `it-impatriati`;
- crypto-assets: `italy-crypto-tax`;
- residence, non-residents and outbound withholding: `it-cross-border`.

**Which law applies in 2026.** A new income tax code (D.Lgs. 19 June 2026 n. 117) applies only from 1 January 2027. For 2026 income the old TUIR (D.P.R. 917/1986) applies, so this skill cites the old article numbers, read on Normattiva as in force on 30 June 2026. From 2027 the numbers change.

## Who this applies to

- **Resident individuals** (TUIR art. 2; the residence tests are in `it-cross-border`). They pay IRPEF on worldwide income.
- **Employment income** (TUIR art. 49) and income treated like it (art. 50: for example scholarships, co.co.co. fees, some directors' fees). These people get the art. 13 comma 1 detrazione.
- **Pensioners** (art. 49 comma 2 lett. a). They get the separate pension detrazione of art. 13 comma 3, not the employee one, and none of the cuneo fiscale measures.
- **Investors**: interest, dividends and capital gains (TUIR arts. 44 and 67) are mostly taxed outside IRPEF by a substitute tax.
- **Landlords** letting residential property outside a business, who may choose cedolare secca.

Out of scope here: anyone with business or self-employment income (see `it-income-tax`), non-residents (taxed on Italian income only, art. 24; see `it-cross-border`), and people under the impatriati or EUR 300,000 flat tax regimes (see `it-impatriati`).

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| IRPEF, taxable income up to EUR 28,000 | 23% | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art11!vig=2026-06-30 |
| IRPEF, over EUR 28,000 up to EUR 50,000 | 33% (35% in 2024 and 2025; cut by L. 199/2025 art. 1 comma 3) | 2026 | same; https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199~art1!vig=2026-06-30 |
| IRPEF, over EUR 50,000 | 43%; tax on the first EUR 50,000 is EUR 13,700 | 2026 | TUIR art. 11; https://www.agenziaentrate.gov.it/portale/imposta-sul-reddito-delle-persone-fisiche-irpef-/aliquote-e-calcolo-dell-irpef |
| Band edges | Unchanged at EUR 28,000 and EUR 50,000 (L. 199/2025 changed only the rate) | 2026 | L. 199/2025 art. 1 comma 3 |
| No IRPEF if the only income is a full-year pension up to EUR 7,500, land up to EUR 185.92 and the main home | nil | 2026 | TUIR art. 11 comma 2 |
| Employee detrazione, total income up to EUR 15,000 | EUR 1,955 (minimum EUR 690; EUR 1,380 on fixed-term contracts) | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art13!vig=2026-06-30 |
| Employee detrazione, over EUR 15,000 up to 28,000 | EUR 1,910 + EUR 1,190 x (28,000 - income) / 13,000 | 2026 | TUIR art. 13 comma 1 lett. b |
| Employee detrazione, over EUR 28,000 up to 50,000 | EUR 1,910 x (50,000 - income) / 22,000; nil above 50,000 | 2026 | TUIR art. 13 comma 1 lett. c |
| Employee extra, income over EUR 25,000 up to 35,000 | + EUR 65 | 2026 | TUIR art. 13 comma 1.1 |
| Pension detrazione, income up to EUR 8,500 | EUR 1,955 (minimum EUR 713) | 2026 | TUIR art. 13 comma 3 lett. a |
| Pension detrazione, over EUR 8,500 up to 28,000 | EUR 700 + EUR 1,255 x (28,000 - income) / 19,500 | 2026 | TUIR art. 13 comma 3 lett. b |
| Pension detrazione, over EUR 28,000 up to 50,000 | EUR 700 x (50,000 - income) / 22,000; nil above 50,000 | 2026 | TUIR art. 13 comma 3 lett. c |
| Pension extra, income over EUR 25,000 up to 29,000 | + EUR 50 | 2026 | TUIR art. 13 comma 3-bis |
| Cuneo fiscale: tax-free sum for employees with total income up to EUR 20,000 | 7.1% of employment income up to EUR 8,500; 5.3% over 8,500 up to 15,000; 4.8% over 15,000 | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-06-30 (commi 4 and 5) |
| Cuneo fiscale: extra detrazione, total income over EUR 20,000 up to 32,000 | EUR 1,000 | 2026 | L. 207/2024 art. 1 comma 6 |
| Cuneo fiscale: extra detrazione, over EUR 32,000 up to 40,000 | EUR 1,000 x (40,000 - income) / 8,000; nil above 40,000 | 2026 | L. 207/2024 art. 1 comma 6 |
| Trattamento integrativo (cash supplement), total income up to EUR 15,000 | EUR 1,200 a year, if gross tax on employment income exceeds the art. 13 detrazione less EUR 75 | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2020-02-05;3~art1!vig=2026-06-30 |
| Dependent spouse | EUR 800 - 110 x income / 15,000 up to 15,000; EUR 690 from 15,000 to 40,000; EUR 690 x (80,000 - income) / 40,000 from 40,000 to 80,000; small extras between EUR 29,000 and 35,200 | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art12!vig=2026-06-30 |
| Dependent child aged 21 to 29 (or 30+ with disability) | EUR 950 x (95,000 - income) / 95,000; EUR 95,000 rises by 15,000 per child after the first; split 50/50 between parents unless agreed | 2026 | TUIR art. 12 comma 1 lett. c |
| Other dependant: ascendant living with the taxpayer | EUR 750 x (80,000 - income) / 80,000 | 2026 | TUIR art. 12 comma 1 lett. d |
| Dependant's own income limit | EUR 2,840.51; EUR 4,000 for children up to age 24 | 2026 | TUIR art. 12 comma 2 |
| Oneri detraibili: credit rate | 19% (art. 15 still prints 22%; art. 16-ter comma 5-bis refers to items "detraibili nella misura del 19 per cento") | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art16ter!vig=2026-06-30 |
| Medical expenses | 19% of the part above EUR 129.11 (art. 15 prints 250,000 lire) | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art15!vig=2026-06-30 |
| Mortgage interest on the main home | 19% of up to EUR 4,000 a year | 2026 | TUIR art. 15 comma 1 lett. b |
| School fees (infant to upper secondary) | 19% of up to EUR 1,000 per pupil | 2026 | TUIR art. 15 comma 1 lett. e-bis |
| Funeral costs | 19% of up to EUR 1,550 per death | 2026 | TUIR art. 15 comma 1 lett. d |
| Phase-out of 19% credits | full up to total income EUR 120,000; then x (240,000 - income) / 120,000; mortgage interest is kept in full | 2026 | TUIR art. 15 commi 3-bis and 3-quater |
| Overall cap on detraibili oneri, total income over EUR 75,000 | base EUR 14,000 (over 100,000: EUR 8,000) x 0.50 / 0.70 / 0.85 / 1 by number of dependent children; medical costs outside the cap | 2026 | TUIR art. 16-ter |
| Cut for total income over EUR 200,000 | 19% credits reduced by EUR 440 (medical costs excluded) | 2026 | TUIR art. 16-ter comma 5-bis (L. 199/2025 art. 1 comma 4) |
| Supplementary pension contributions (deductible) | up to EUR 5,300 from tax year 2026 (EUR 5,164.57 before) | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-12-05;252~art8!vig=2026-06-30 |
| Contributions to registered supplementary health funds (deductible) | up to EUR 3,615.20 | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art10!vig=2026-06-30 |
| Regional surcharge (addizionale regionale) | base 1.23%; each region may raise it by up to 2.1 points or lower it | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2011-05-06;68~art6!vig=2026-06-30 |
| Municipal surcharge (addizionale comunale) | set by each comune, variation up to 0.8 points in total; the comune may set an exemption threshold | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1998-09-28;360~art1!vig=2026-06-30 |
| Interest, dividends and gains (substitute tax or final withholding) | 26% | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2014-04-24;66~art3!vig=2026-06-30 |
| Italian government bonds and bonds of white-list states | 12.5% on interest; gains counted at 48.08% of the amount, so 26% x 48.08% = 12.5% | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1996-04-01;239~art2!vig=2026-06-30 ; D.L. 66/2014 art. 3 commi 2 and 5 |
| Cedolare secca, long-term residential lets | 21% of the yearly rent | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2011-03-14;23~art3!vig=2026-06-30 |
| Cedolare secca, agreed-rent contracts (canone concordato) in high-demand comuni | 10% | 2026 | D.Lgs. 23/2011 art. 3 comma 2 |
| Cedolare secca, short lets (up to 30 days) | 26%; 21% for one unit the taxpayer picks in the return | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2017-04-24;50~art4!vig=2026-06-30 |
| Rent taxed under IRPEF | rent less a flat 5% (if higher than the cadastral income) | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art37!vig=2026-06-30 (comma 4-bis) |
| IVIE (foreign real estate) | 1.06% of value; not due if EUR 200 or less | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-12-06;201~art19!vig=2026-06-30 (comma 15) |
| IVAFE (foreign financial assets) | 0.2% of value; 0.4% for assets in listed tax havens (from 2024); bank accounts a flat EUR 34.20 | 2026 | D.L. 201/2011 art. 19 comma 20, same URL |

## The taxable base

**Step by step** (TUIR arts. 8 to 13).

1. Add up the income of each category: employment or pension income, buildings (fondiari), and any other income that is not taxed separately. This is the **reddito complessivo**. The main home and its pertinenze are in it, but are deducted again, so in practice they are untaxed.
2. Take off the **oneri deducibili** (art. 10): compulsory social contributions not already taken off in the payslip, supplementary pension contributions up to EUR 5,300, registered health-fund contributions up to EUR 3,615.20, periodic maintenance paid to a former spouse under a court order (not child support). The result is taxable income.
3. Apply the bands (art. 11) to get **gross tax** (imposta lorda).
4. Subtract the **detrazioni** (art. 11 comma 3), never below zero: employment or pension (art. 13), the cuneo extra detrazione, family (art. 12), and the 19% oneri (art. 15). Unused detrazioni are lost, not refunded.
5. Subtract withholdings and payments on account. The difference is the balance or refund.

**Employment income** is gross pay less the employee's compulsory social contributions, with some benefits exempt (art. 51). The employer's payslip and the CU carry the figure. Contract-renewal pay rises (5%), night and holiday supplements (15%) and productivity bonuses (1%) can be taxed by a substitute tax in 2026 instead: see `italy-payroll`.

**Which "income" the formulas use.** Every detrazione formula uses total income net of the main home (art. 13 comma 6-bis, art. 12 comma 4-bis). Rent taxed under cedolare secca still counts for these tests (D.Lgs. 23/2011 art. 3 comma 7), so choosing cedolare can still cost a detrazione. The ratios in the formulas are taken to four decimal places (art. 13 comma 6).

**Cuneo fiscale (L. 207/2024 art. 1 commi 4 to 9).** Employees only, not pensioners. With total income up to EUR 20,000 the employee gets a tax-free cash sum, a percentage of employment income (the band uses income scaled to a full year). From EUR 20,000 to 40,000 they get an extra detrazione instead: EUR 1,000 up to 32,000, falling to nil at 40,000. The employer gives both automatically and checks them at the year-end conguaglio. Exempt impatriati income counts in total income for these tests (comma 9).

**Family detrazioni.** For children under 21 there is no tax detrazione; families receive the INPS single allowance (assegno unico) instead, which is outside this skill. Detrazioni are monthly: they start and stop with the month the conditions are met (art. 12 comma 3). A non-EU, non-EEA citizen gets no family detrazioni for relatives living abroad (art. 12 comma 2-bis).

**Investment income (outside IRPEF).**

- **Interest and dividends** from Italian payers are taxed at source at 26% (12.5% on government bonds) and need no return. Foreign interest and dividends received without Italian withholding go in the return and bear the same 26% substitute tax.
- **Capital gains** on shares, funds and bonds are "redditi diversi" (art. 67), taxed at 26% under one of three regimes (D.Lgs. 461/1997):
  - **dichiarativo** (art. 5): the taxpayer reports gains and losses in the Redditi PF return and pays;
  - **amministrato** (art. 6): by option, the Italian bank or broker taxes each gain and carries losses within the account;
  - **gestito** (art. 7): by option, for a discretionary portfolio mandate, tax on the yearly managed result.
- **Losses** (minusvalenze) offset gains of the same year and the next four (D.Lgs. 461/1997 art. 6 comma 5).
- Crypto-assets have their own rules: `italy-crypto-tax`.

**Rental income.** A residential let outside a business is taxed either:

- under IRPEF: the higher of the cadastral income and rent less 5% joins total income and bears bands and surcharges; or
- by **cedolare secca**: a flat 21% (10% for agreed-rent contracts in listed comuni) on the full rent, which replaces IRPEF, the surcharges, registration tax and stamp duty on the lease. The option is made on registration of the lease and the tax is paid with IRPEF. It is not available for lets made in a business (D.Lgs. 23/2011 art. 3 comma 6).

## Deadlines and filing

| What | When (2026 income) | Source |
|---|---|---|
| CU (employer's income statement) to the employee | Each spring; see `italy-payroll` | D.P.R. 322/1998 art. 4 |
| Modello 730 (employees and pensioners, through the employer, a CAF, a professional or the Agenzia's precompiled service) | By 30 September 2027 | D.M. 164/1999 art. 13 comma 1, https://www.normattiva.it/uri-res/N2Ls?urn:nir:ministero.finanze:decreto:1999-05-31;164~art13!vig=2026-06-30 ; Agenzia, 730/2026 page (30 September 2026 for 2025 income), https://www.agenziaentrate.gov.it/portale/quando-e-come-presentare-il-730-2026 |
| Modello Redditi PF, online | 15 April to 31 October 2027; 31 October 2027 is a Sunday and 1 November a holiday, so the deadline moves to 2 November 2027 | D.P.R. 322/1998 art. 2 comma 1, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig=2026-06-30 ; D.L. 70/2011 art. 7 comma 2 lett. l, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-05-13;70~art7!vig=2026-06-30 |
| Balance for 2026 and first acconto for 2027 (Redditi PF, or 730 without an employer to settle it) | 30 June 2027, or by 30 July 2027 with 0.40% extra | https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef |
| Second or single acconto for 2027 | 30 November 2027 | same |
| 730 with an employer or pension body | No separate payment: the refund or balance goes through pay from July | same |

**730 or Redditi PF.** The 730 is for people with employment, pension and similar income (D.Lgs. 241/1997 art. 34 comma 4, referred to by D.M. 164/1999 art. 13). It is simpler, and refunds come through pay within months. Use Redditi PF when the person has business or self-employment income. Payments go by F24.

**Do I have to file at all?** Filing lets an employee claim oneri the employer did not apply (medical costs, mortgage interest). A person with rent, foreign income not taxed at source, or foreign assets to report in RW files a return.

**Acconti.** Due if the tax declared, after detrazioni and withholdings, is above EUR 51.65: 40% by 30 June and 60% by 30 November (one payment by 30 November if under EUR 257.52). Detail: `it-estimated-tax`.

**Surcharges.** The comunale acconto is 30% of the prior-year surcharge (D.Lgs. 360/1998 art. 1 comma 4). For employees the employer withholds the surcharges through pay (for the comunale, art. 1 comma 5; see `italy-payroll`). The rates are those of the region and comune of tax domicile; look them up in the region's law and the comune's resolution for 2026.

**Foreign assets.** A resident who holds foreign accounts, investments, property or crypto reports them in the RW section of the return and pays IVIE and IVAFE (D.L. 167/1990 art. 4; D.L. 201/2011 art. 19). A wealth tax paid abroad on the same financial assets is credited against IVAFE (art. 19 comma 21).

## Penalties and interest

| Failure | Penalty | Source |
|---|---|---|
| No return filed | 120% of the tax due, minimum EUR 250; EUR 250 to 1,000 if no tax is due | D.Lgs. 471/1997 art. 1 comma 1, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-06-30 |
| Return filed more than 90 days late, before any audit | The late-payment penalty, tripled | art. 1 comma 1-bis, same URL |
| Return filed up to 90 days late | Penalty reduced to one tenth of the minimum by ravvedimento | D.Lgs. 472/1997 art. 13 comma 1 lett. c, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-06-30 |
| Understated income or tax, or a wrong detrazione | 70% of the extra tax, minimum EUR 150 | D.Lgs. 471/1997 art. 1 comma 2 |
| Late or missing payment | 25%; halved if paid within 90 days; one fifteenth of that per day for delays up to 15 days | D.Lgs. 471/1997 art. 13 comma 1, https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-06-30 |
| Foreign assets not reported in RW | 3% to 15% of the amount not declared (6% to 30% for tax havens) | D.L. 167/1990 art. 5 comma 2 (see `it-cross-border`) |

**Ravvedimento operoso** (D.Lgs. 472/1997 art. 13). If the taxpayer corrects the error and pays the tax, interest and reduced penalty before the Agenzia starts a check, the penalty falls to:

- one tenth of the minimum for a payment made within 30 days;
- one ninth within 90 days of the error, or of the return deadline for a return error;
- one eighth by the return deadline for the year of the error;
- one seventh after that.

Interest on the late tax is paid as well. The new consolidated penalty and payment codes apply from 1 January 2027; this table is the 2026 law.

## Cross-border points

- **Foreign income of a resident** is taxed in Italy with a credit for final foreign tax, limited to the Italian tax on that income (TUIR art. 165). No credit if the return is not filed or the income is left out (art. 165 comma 8). Detail: `it-cross-border`.
- **Foreign employment income** of a resident who works abroad: see the treaty and `it-cross-border`; frontier-worker rules are not covered here.
- **Non-residents** are taxed on Italian income only, with no family detrazioni unless at least 75% of their income is Italian (art. 24 comma 3-bis): `it-cross-border`.
- **Inbound workers**: under the impatriati regime only 50% (or 40%) of qualifying pay is taxed, but the full amount still counts for the cuneo tests: `it-impatriati`.
- **Foreign assets**: RW, IVIE and IVAFE above. People under the art. 24-bis flat tax have their own rules: `it-impatriati`.

## Worked examples

### Example 1: employee on EUR 45,000 gross, no dependants

Facts. Giulia, a private-sector employee resident in Bologna, earns EUR 45,000 gross in 2026 on a permanent contract. She lives in her own home, has no other income, no dependants and no deductible or 19% expenses.

1. **Employment income.** Her employee INPS share is 9.19% (INPS circolare 40/2011): EUR 4,135.50. Employment income: EUR 40,864.50. This is also her total income.
2. **Gross tax.** EUR 28,000 at 23% = EUR 6,440.00; EUR 12,864.50 at 33% = EUR 4,245.29. Gross IRPEF: EUR 10,685.29.
3. **Employee detrazione** (art. 13 comma 1 lett. c). (50,000 - 40,864.50) / 22,000 = 0.4152 (four decimals). EUR 1,910 x 0.4152 = EUR 793.03. No EUR 65 extra: her income is above EUR 35,000.
4. **Cuneo fiscale.** Her total income is above EUR 40,000, so the extra detrazione is nil. Had she earned a little less, so that total income were EUR 36,000, she would get EUR 1,000 x 4,000 / 8,000 = EUR 500.
5. **Net IRPEF**: EUR 9,892.26, before the regional and municipal surcharges, which depend on Emilia-Romagna's and Bologna's 2026 rates and are not computed here. Her employer has withheld this through the year; she owes nothing more unless she has other income.

```oa-check
name: Employee EUR 45,000 gross, IRPEF 2026 before surcharges
inputs:
  gross_pay: 45000
  inps_rate: 0.0919
steps:
  - inps: round(gross_pay * inps_rate, 2)
  - income: gross_pay - inps
  - band_23: min(income, 28000) * 0.23
  - band_33: (min(income, 50000) - 28000) * 0.33
  - gross_tax: round(band_23 + band_33, 2)
  - ratio: floor((50000 - income) / 22000 * 10000) / 10000
  - detrazione: round(1910 * ratio, 2)
  - cuneo_extra: 1000 * clamp((40000 - income) / 8000, 0, 1)
  - net_irpef: gross_tax - detrazione - cuneo_extra
expected:
  inps: 4135.50
  income: 40864.50
  gross_tax: 10685.29
  ratio: 0.4152
  detrazione: 793.03
  cuneo_extra: 0
  net_irpef: 9892.26
```

### Example 2: the same employee lets a flat: IRPEF or cedolare secca

Facts. Giulia also owns a second flat, let on a free-market four-year residential lease (canone libero) for EUR 12,000 a year. Rent less 5% is higher than the flat's cadastral income.

**Under IRPEF.** Rental income is EUR 12,000 less 5% = EUR 11,400. Total income: EUR 40,864.50 + 11,400 = EUR 52,264.50. Gross tax: EUR 13,700 + 43% of 2,264.50 = EUR 14,673.74. Total income is above EUR 50,000, so the employee detrazione is lost. Net IRPEF: EUR 14,673.74, plus the regional and municipal surcharges on the whole EUR 52,264.50, plus registration tax on the lease.

**Under cedolare secca.** 21% of EUR 12,000 = EUR 2,520. IRPEF on her salary stays at gross tax EUR 10,685.29. But the rent still counts for the detrazione test (D.Lgs. 23/2011 art. 3 comma 7). Whether the test uses the full rent or rent less 5%, her income for the test is over EUR 50,000, so the EUR 793.03 detrazione is lost here too. Total: EUR 10,685.29 + 2,520 = EUR 13,205.29.

**Result.** Cedolare saves EUR 1,468.45 of tax before surcharges, and also takes the EUR 11,400 out of the surcharge base and removes registration tax and stamp duty on the lease. Her employer withheld tax as if she had no rent, so she must file (730 or Redditi PF) and pay the cedolare, with acconti for 2027.

The edge: someone near a detrazione threshold does not escape it by choosing cedolare. Her withholding of EUR 9,892.26 in Example 1 no longer covers her IRPEF: the EUR 793.03 detrazione the employer gave is clawed back in the return.

```oa-check
name: Employee plus rented flat, IRPEF vs cedolare secca 21% (2026)
inputs:
  employment_income: 40864.50
  rent: 12000
  ced_rate: 0.21
steps:
  - rental_income: rent * 0.95
  - total_irpef_route: employment_income + rental_income
  - gross_irpef_route: round(13700 + (total_irpef_route - 50000) * 0.43, 2)
  - test_income_ced: employment_income + rental_income
  - det_ced: 1910 * clamp((50000 - test_income_ced) / 22000, 0, 1)
  - gross_salary_only: round(28000 * 0.23 + (employment_income - 28000) * 0.33, 2)
  - cedolare: rent * ced_rate
  - total_ced_route: gross_salary_only - det_ced + cedolare
  - saving: gross_irpef_route - total_ced_route
expected:
  rental_income: 11400.00
  total_irpef_route: 52264.50
  gross_irpef_route: 14673.74
  det_ced: 0
  cedolare: 2520.00
  total_ced_route: 13205.29
  saving: 1468.45
```

## Ask the client first

1. Are you employed, retired, or both, and do you have any self-employment or VAT-registered activity? (Self-employment means `it-income-tax` and Redditi PF.)
2. What is your total income from all sources, including rent you tax under cedolare? Every detrazione and the cuneo measures turn on this figure.
3. Who in your family lives with you and what does each earn? Ages of the children (under 21 means assegno unico, not a tax detrazione).
4. Do you let property? Which contract type (free market, canone concordato, short lets), in which comune, and did you opt for cedolare secca at registration?
5. Do you hold investments or accounts abroad, or with an Italian broker under the regime amministrato? Foreign holdings mean RW, IVIE, IVAFE and possibly the dichiarativo regime.
6. Did you pay medical costs, mortgage interest on your main home, school fees, or supplementary pension contributions in 2026?

## Sources

| Source | URL | Read on |
|---|---|---|
| TUIR art. 10 (oneri deducibili) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art10!vig=2026-06-30 | 2026-10-22 |
| TUIR art. 11 (bands, 33% from 2026) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art11!vig=2026-06-30 | 2026-10-22 |
| TUIR art. 12 (family detrazioni) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art12!vig=2026-06-30 | 2026-10-22 |
| TUIR art. 13 (employment and pension detrazioni) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art13!vig=2026-06-30 | 2026-10-22 |
| TUIR art. 15 (oneri detraibili) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art15!vig=2026-06-30 | 2026-10-22 |
| TUIR art. 16-ter (cap on detrazioni; EUR 440 cut over EUR 200,000) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art16ter!vig=2026-06-30 | 2026-10-22 |
| TUIR art. 37 (rent less 5%) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art37!vig=2026-06-30 | 2026-10-22 |
| L. 199/2025 (Budget law 2026) art. 1 commi 3 and 4 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199~art1!vig=2026-06-30 | 2026-10-22 |
| L. 207/2024 (Budget law 2025) art. 1 commi 4 to 9 (cuneo fiscale) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1!vig=2026-06-30 | 2026-10-22 |
| D.L. 3/2020 art. 1 (trattamento integrativo) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2020-02-05;3~art1!vig=2026-06-30 | 2026-10-22 |
| D.Lgs. 252/2005 art. 8 (supplementary pension cap) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2005-12-05;252~art8!vig=2026-06-30 | 2026-10-22 |
| D.Lgs. 68/2011 art. 6 (regional surcharge) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2011-05-06;68~art6!vig=2026-06-30 | 2026-10-22 |
| D.Lgs. 360/1998 art. 1 (municipal surcharge) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1998-09-28;360~art1!vig=2026-06-30 | 2026-10-22 |
| D.L. 66/2014 art. 3 (26% on financial income) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2014-04-24;66~art3!vig=2026-06-30 | 2026-10-22 |
| D.Lgs. 239/1996 art. 2 (12.5% on government bonds) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1996-04-01;239~art2!vig=2026-06-30 | 2026-10-22 |
| D.Lgs. 461/1997 arts. 5, 6, 7 (dichiarativo, amministrato, gestito) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-11-21;461~art6!vig=2026-06-30 | 2026-10-22 |
| D.Lgs. 23/2011 art. 3 (cedolare secca) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2011-03-14;23~art3!vig=2026-06-30 | 2026-10-22 |
| D.L. 50/2017 art. 4 (short lets) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2017-04-24;50~art4!vig=2026-06-30 | 2026-10-22 |
| D.L. 201/2011 art. 19 (IVIE, IVAFE) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-12-06;201~art19!vig=2026-06-30 | 2026-10-22 |
| D.M. 164/1999 art. 13 (730 deadline) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:ministero.finanze:decreto:1999-05-31;164~art13!vig=2026-06-30 | 2026-10-22 |
| D.P.R. 322/1998 art. 2 (Redditi PF deadline) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig=2026-06-30 | 2026-10-22 |
| D.L. 70/2011 art. 7 comma 2 lett. l (weekend and holiday deadlines) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2011-05-13;70~art7!vig=2026-06-30 | 2026-10-22 |
| D.Lgs. 471/1997 arts. 1 and 13 (penalties) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-06-30 | 2026-10-22 |
| D.Lgs. 472/1997 art. 13 (ravvedimento) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-06-30 | 2026-10-22 |
| INPS circolare 40/2011 (employee pension share 9.19%) | https://servizi2.inps.it/servizi/Bussola/visualizzadoc.aspx?svirtualurl=%2Fcircolari%2Fcircolare+numero+40+del+22-02-2011.htm | 2026-10-22 |
| Agenzia delle Entrate, IRPEF rates (updated 13 January 2026; notes the 33% rate) | https://www.agenziaentrate.gov.it/portale/imposta-sul-reddito-delle-persone-fisiche-irpef-/aliquote-e-calcolo-dell-irpef | 2026-10-22 |
| Agenzia delle Entrate, how IRPEF is paid (12 March 2026) | https://www.agenziaentrate.gov.it/portale/come-si-paga-l-irpef | 2026-10-22 |
| Agenzia delle Entrate, when to file the 730/2026 | https://www.agenziaentrate.gov.it/portale/quando-e-come-presentare-il-730-2026 | 2026-10-22 |

Not yet confirmed:

- **Supplementary pension cap timing.** D.Lgs. 252/2005 art. 8 comma 4 says EUR 5,300 "from tax year 2026", but Normattiva's note on the change (L. 199/2025 art. 1 commi 202 and 205) says the amended provisions apply from 1 July 2026. Confirm in the 2027 return instructions whether the full EUR 5,300 applies to 2026.
- **School fee cap.** The text in force on 30 June 2026 shows EUR 1,000 per pupil in double brackets (a recent amendment); we did not read the amending act or its start date.
- **Gains on qualifying holdings** (over 2% voting rights or 5% capital in listed companies): this skill assumes the same 26% as other gains; we did not read the act that aligned them.
- **Short-let business presumption**: how many units make short lets a business in 2026 (L. 178/2020 art. 1 comma 595, possibly changed by L. 199/2025) was not read.
- **Payment traceability** for 19% credits (L. 160/2019) and the IVAFE exemption for small bank balances: not read.
- **Legal interest rate for 2026** used in ravvedimento: not read.
- Whether the 730/2027 has the sections for capital gains (RT), foreign income and RW: check the 730/2027 instructions when published.
