---
name: it-employer-contributions
description: "Italian employer social contributions on employees and the full cost of an employee, tax year 2026. Covers the employer and employee INPS rates for private industry and commerce, component by component (pension IVS 23.81% and 9.19%, NASpI, CUAF, maternity, sickness, Fondo di garanzia TFR, CIGO, CIGS and the FIS by headcount), the extra 1% above EUR 56,224, the 2026 minimum and maximum bases, apprentices in summary, the INAIL premium (voce, tasso, 1% addizionale, autoliquidazione), TFR accrual and the INPS Fondo di Tesoreria with the 2026 headcount rule, UniEmens and F24, sanzioni civili and the 2026 hiring reliefs. Trigger on: contributi INPS datore di lavoro, costo del lavoro, costo azienda dipendente, aliquote contributive industria commercio, FIS, CIGS, INAIL premio, TFR Fondo Tesoreria. Out of scope, see: italy-payroll (IRPEF withholding, payslip, CU), it-irpef-employees (trattamento integrativo, family detrazioni), it-inps-contributions, it-inps-artigiani-commercianti, it-irap, it-cross-border."
jurisdiction: IT
category: international
tax_year: 2026
tier: 2
last_updated: 2026-10-23
version: 0.1
verified_by: pending
---

# Italy: employer INPS and INAIL contributions and the cost of an employee (2026)

This skill works out what a private employer pays on top of gross pay for an employee in Italy in 2026: INPS contributions (employer and employee shares), the INAIL accident premium and the TFR accrual. It gives the rates for the two most common INPS classes, industry and commerce. Income tax withholding, the payslip and the CU are in `italy-payroll`; the trattamento integrativo and family detrazioni are in `it-irpef-employees`.

## Who this applies to

- **Private employers with employees insured in the INPS Fondo pensioni lavoratori dipendenti (FPLD)**, the general scheme with a 33% pension rate (INPS, "Aliquote contributive"). The employer is the only party liable to pay; it withholds the employee share from pay and pays both (same page).
- **The INPS class decides the rates.** INPS classifies each employer by activity (industry, commerce, construction, agriculture, credit and others), size, legal form and the worker's grade (operaio, impiegato, dirigente, apprentice) (same page). This skill gives industry in general and commerce (wholesale and retail).
- **Size thresholds that change the rates:** more than 5 employees (FIS 0.80% instead of 0.50%), more than 15 (CIGS in industry; CIGS for FIS employers since 2022), more than 50 (higher CIGO in industry; CIGS in commerce) (D.Lgs. 148/2015 arts. 13, 20, 29).
- **Out of scope:** construction and stone industry (CIGO 4.70% and 3.30% for operai, art. 13), agriculture (own rates, INPS circolare 43/2026), domestic workers, entertainment and sport workers, dirigenti, public employers, credit and insurance. Refer these.
- **Self-employed** contributions: `it-inps-contributions` (gestione separata) and `it-inps-artigiani-commercianti`.

## Rates, bands and thresholds

Percentages are of the employee's taxable pay for contributions (retribuzione imponibile). "Ee" is the employee share.

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Pension (IVS), FPLD total | 33% | 2026 | https://www.inps.it/it/it/inps-comunica/diritti-e-obblighi-in-materia-di-sicurezza-sociale-nell-unione-e/per-le-imprese/aliquote-contributive.html |
| Pension, employee share (so 23.81% employer) | 9.19% | 2026 | https://servizi2.inps.it/servizi/Bussola/visualizzadoc.aspx?svirtualurl=%2Fcircolari%2Fcircolare+numero+40+del+22-02-2011.htm |
| Extra employee pension contribution on pay above the first band | 1% | 2026 | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/01/Circolare_15151/Allegati/16546_Circolare-numero-6-del-30-01-2026.pdf |
| First pension band, yearly (monthly EUR 4,685) | EUR 56,224 | 2026 | same, Circolare 6/2026 para. 5 |
| Massimale, insured from 1996 only | EUR 122,295 | 2026 | same, para. 6 |
| Minimum daily pay for contributions | EUR 58.13 | 2026 | same, para. 2 |
| NASpI (unemployment), employer | 1.31% | 2026 | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2024/04/Circolare_14535/Allegati/15128_Circolare-numero-53-del-03-04-2024.pdf |
| Training levy (L. 845/1978 art. 25), employer | 0.30% | 2026 | same, Circolare 53/2024 |
| NASpI addizionale on fixed-term contracts, employer; plus 0.5 points at each renewal | 1.4% | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2012-06-28;92~art2!vig=2026-10-23 |
| Fondo di garanzia TFR, employer (0.40% for industrial dirigenti) | 0.20% | 2026 | Circolare 53/2024 |
| Maternity, employer: industry | 0.46% | 2026 | Circolare 53/2024 |
| Maternity, employer: commerce and services (terziario) | 0.24% | 2026 | Circolare 53/2024; https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2022/10/Circolare_13970/Allegati/14969_Circolare-numero-117-del-20-10-2022_Allegato-n-1.pdf |
| Sickness, employer: industry, operai only | 2.22% | 2026 | Circolare 53/2024 |
| Sickness, employer: terziario (operai and impiegati in commerce) | 2.44% | 2026 | Circolare 53/2024; INPS 2010 rate tables (commerce rows) https://servizi2.inps.it/CircolariZIP/circolare%20numero%2025%20del%2018-02-2010_Allegato%20n%2014.pdf |
| CUAF (family allowances fund), employer, net of the 1.80-point legal cut (2.48 less 1.80) | 0.68% | 2026 | Circolare 117/2022 Allegato 1; INPS 2010 rate tables (industry and commerce rows) |
| CIGO, industrial firms up to 50 employees, employer | 1.70% | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2015-09-14;148~art13!vig=2026-10-23 |
| CIGO, industrial firms over 50 employees, employer | 2.00% | 2026 | same, art. 13 |
| CIGS, firms in scope, total (0.60% employer, 0.30% Ee) | 0.90% | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2015-09-14;148~art23!vig=2026-10-23 |
| FIS, employers with up to 5 employees (of which 0.17% Ee) | 0.50% | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2015-09-14;148~art29!vig=2026-10-23; split in Circolare 117/2022 Allegato 1 |
| FIS, employers with more than 5 employees (of which 0.27% Ee) | 0.80% | 2026 | same |
| FIS, up to 5 employees with no claim for 24 months: cut in the rate | 40% | 2026 | D.Lgs. 148/2015 art. 29 c. 8-bis |
| Apprentices: employer rate (plus NASpI 1.31% and 0.30%, total 11.61%) | 10% | 2026 | https://www.inps.it/bussola/VisualizzaDoc.aspx?sVirtualURL=/Messaggi/Messaggio+numero+1478+del+10-04-2019.htm |
| Apprentices: employee rate | 5.84% | 2026 | https://www.inps.it/content/dam/inps-site/pdf/inpscomunica/Libretto_INPS_giovani.pdf |
| Apprentices, employers with up to 9 staff: employer rate in year 1 and year 2 | 1.5% and 3% | 2026 | INPS messaggio 1478/2019 (L. 296/2006 art. 1 c. 773) |
| TFR accrual: yearly pay divided by 13.5 | 7.41% | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2120!vig=2026-10-23 |
| Contribution deducted from the TFR accrual (net accrual 6.91%) | 0.50% | 2026 | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1982-05-29;297~art3!vig=2026-10-23 |
| TFR revaluation each 31 December: fixed part plus 75% of the ISTAT price rise | 1.5% | 2026 | Civil Code art. 2120 |
| Fondo di Tesoreria: average headcount that triggers it for 2026 and 2027 pay (firms that grew after their first year) | 60 | 2026 | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/02/Circolare_15160/Allegati/16559_Circolare-numero-12-del-05-02-2026.pdf |
| Fondo di Tesoreria: average headcount in the first year of activity (unchanged rule) | 50 | 2026 | same, Circolare 12/2026 para. 2 |
| Relief when TFR goes to the Fondo di Tesoreria or a pension fund: cut in art. 24 L. 88/1989 contributions | 0.28 points | 2026 | Circolare 12/2026 para. 5 |
| INAIL voce 0722 (office work), tasso medio: Terziario | 4 per mille | 2026 | https://www.inail.it/content/dam/inail-hub-site/documenti/circolari/2025/06/Circolare%20n%2038_24%20giugno%202025.pdf |
| INAIL voce 0722, tasso medio: Industria | 5 per mille | 2026 | same, Circolare INAIL 38/2025 |
| INAIL addizionale ex ANMIL on the premium | 1% | 2026 | https://www.inail.it/content/dam/assicurazione/documenti/2025/12/Guida%20autoliquidazione%202025-2026.pdf |

**Totals for an impiegato, 2026, built from the components above:**

| Employer class | Employer INPS | Employee INPS |
|---|---|---|
| Commerce, 6 to 15 employees (FIS 0.80%) | 29.51% (23.81 + 1.31 + 0.30 + 0.20 + 0.68 + 0.24 + 2.44 + 0.53) | 9.46% (9.19 + 0.27) |
| Industry, 16 to 50 employees | 29.06% (23.81 + 1.31 + 0.30 + 0.20 + 0.68 + 0.46 + 1.70 + 0.60) | 9.49% (9.19 + 0.30) |
| Industry, over 50 employees | 29.36% (as above with CIGO 2.00) | 9.49% |

An industrial operaio adds sickness 2.22% to the employer total. These totals are before the Tesoreria relief and before any hiring relief.

**Where the reliefs are 2026 law:**
- **Decontribuzione Sud PMI.** Small and medium employers in Abruzzo, Molise, Campania, Basilicata, Sicilia, Puglia, Calabria and Sardegna: 20% of the employer's pension contributions for 2026, up to EUR 125 a month, for permanent staff hired by 31 December 2025; INAIL excluded; de minimis limits apply (L. 207/2024 art. 1 c. 406 and 408, INPS Circolare 32/2025): https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2025/01/Circolare_14812/Allegati/15880_Circolare-numero-32-del-30-01-2025.pdf
- **2026 hiring bonuses (D.L. 62/2026).** Permanent hires made in 2026 can get a 100% exemption from the employer's pension contributions, INAIL excluded: under-35s out of regular paid work for 24 months (or 6 months if disadvantaged), up to EUR 500 a month (EUR 650 in the ZES Unica), for 12 or 24 months (Circolare 55/2026); disadvantaged women of any age, up to EUR 650 a month (EUR 800 in the ZES), for up to 24 months (Circolare 57/2026); employers with up to 10 staff in the ZES Unica hiring people aged 35 or over out of work for 24 months, up to EUR 650 a month (Circolare 56/2026). Apprentices, domestic work and public employers are excluded (INPS news, 14 May 2026): https://www.inps.it/it/it/inps-comunica/notizie/dettaglio-news-page.news.2026.05.giovani-donne-e-zes-incentivi-per-la-stabilizzazione-professionale.html
- The cuneo fiscale relief for employees in 2026 is a tax measure, not a cut in contributions (L. 207/2024 art. 1 c. 4 to 9); see `italy-payroll`.

## The taxable base

- **Same base as income tax.** Contributions are due on employment income as defined for IRPEF (TUIR art. 49 and 51, cited as old arts. 46 and 48), gross of any withholding (L. 153/1969 art. 12 c. 1 to 3): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1969-04-30;153~art12!vig=2026-10-23
- **Excluded from the base (closed list, art. 12 c. 4 and 5):** TFR, leaving incentives (but pay in lieu of notice is included), damages, employer contributions to pension funds and to contractual health or welfare funds within the limits set there, and family allowances.
- **Floor.** Contributions are due on at least the CCNL pay and never on less than EUR 58.13 a day in 2026 (Circolare 6/2026 para. 2). Part-time: EUR 8.72 an hour on a 40-hour week.
- **The extra 1%.** The employee pays one more point on pay above EUR 56,224, applied month by month above EUR 4,685 (Circolare 6/2026 para. 5).
- **The massimale.** For workers first insured from 1 January 1996 (and those who opted for the contributory pension), no pension contributions are due on pay above EUR 122,295 in 2026 (Circolare 6/2026 para. 6).
- **TFR is not a contribution but is a cost.** Each year the employer sets aside pay divided by 13.5 (art. 2120 c.c.). From that it deducts the 0.50% contribution it pays to INPS with the other contributions (L. 297/1982 art. 3; Circolare 12/2026 para. 3), so the employee's TFR grows by about 6.91% of pay. Each 31 December the fund is revalued at 1.5% plus 75% of the ISTAT price rise.
- **Where the TFR goes.** It stays with the employer unless the employee chose a pension fund. An employer that had an average of at least 50 staff in its first year, or that has grown to an average of at least 60 in 2025 for 2026 pay (60 also for 2027, 50 for 2028 to 2031, 40 from 2032), pays the TFR of staff not in a pension fund to the INPS Fondo di Tesoreria each month (Circolare 12/2026, premessa and para. 2, L. 296/2006 art. 1 c. 755 and 756 as changed by L. 199/2025 art. 1 c. 203). From 2026 a first-time employee who does not opt out within 60 days has their TFR sent to a pension fund (Circolare 12/2026 para. 1).
- **Relief for TFR paid out of the business.** For the TFR sent to a pension fund or the Tesoreria, the employer stops paying the 0.20% Fondo di garanzia contribution and gets a 0.28-point cut on its art. 24 L. 88/1989 contributions, in the same proportion (Circolare 12/2026 para. 5, citing D.Lgs. 252/2005 art. 10 and D.L. 203/2005 art. 8).
- **INAIL.** Premium = insured pay x tasso applicato / 1,000 for each voce of the INAIL tariff, plus the 1% addizionale (INAIL autoliquidazione guide 2025/2026, Parte 2). The tasso medio of the voce (D.M. 27 February 2019) is adjusted after the first two years by the firm's own accident record and can be cut for prevention work (same guide, "Basi di calcolo").
- **For tax.** How these costs enter the company's taxes: `it-ires-corporate-tax` and `it-irap`.

## Deadlines and filing

- **INPS contributions:** paid on F24 by the 16th of the month after the pay month, with the IRPEF withheld; if the 16th is a Saturday or holiday, the next working day (D.Lgs. 241/1997 art. 18 c. 1): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-07-09;241~art18!vig=2026-10-23
- **TFR to the Fondo di Tesoreria:** monthly, by the same 16th, in the same flow; no relief or exemption applies to it (Circolare 12/2026 para. 4).
- **UniEmens:** the monthly return of pay and contribution data to INPS, filed online by the last day of the month after the pay month (D.L. 269/2003 art. 44 c. 9): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2003-09-30;269~art44!vig=2026-10-23
- **INAIL autoliquidazione:** by 16 February the employer pays the balance for the past year (regolazione) and the advance for the current year (rata) on F24, or the first of four 25% instalments; the others fall due by 18 May, 20 August and 16 November 2026, with interest. The declaration of the past year's pay is due by the end of February, 2 March in 2026 because 28 February was a Saturday (INAIL guide 2025/2026, Parte 1).
- **Annual:** CU by 16 March and the 770 by 31 October, see `italy-payroll`.
- **From 2027** the F24 rules in D.Lgs. 241/1997 arts. 17 to 28 move to D.Lgs. 33/2025 (see `it-inps-artigiani-commercianti`).

## Penalties and interest

- **Late or unpaid contributions shown in the UniEmens (omissione):** a yearly sanzione civile at the official reference rate plus 5.5 points, capped at 40% of the contributions; paid within 120 days in one go before any INPS request, the reference rate only (L. 388/2000 art. 116 c. 8): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2000-12-23;388~art116!vig=2026-10-23
- **Evasion (no return or a false one, with intent):** 30% a year, capped at 60%; lower rates if self-reported within 12 months and paid within 30 or 90 days (same article).
- **The rate now.** The reference rate is 2.65% from 16 September 2026, so omissione runs at 8.15% a year (INPS Circolare 98/2026). Full table and the earlier 2026 rates: `it-inps-artigiani-commercianti`, section "Penalties and interest".
- **Employee contributions withheld and not paid:** above EUR 10,000 a year, a crime (up to three years and a fine up to EUR 1,032); up to EUR 10,000, an administrative fine of 1.5 to 4 times the amount. No penalty if paid within three months of the notice (D.L. 463/1983 art. 2 c. 1-bis): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1983-09-12;463~art2!vig=2026-10-23
- **INAIL:** failing to declare the year's pay on time costs EUR 125 to EUR 770 if the premium was not underpaid; otherwise sanzioni civili on the premium due (INAIL guide 2025/2026, Parte 1).

## Cross-border points

- **One country's social security at a time.** Inside the EU, EEA and Switzerland, Regulation (EC) 883/2004 decides which country's contributions apply. An Italian employer posting a worker to another EU country for up to 24 months keeps paying INPS, with an A1 certificate requested before the posting (INPS, "Certificato di distacco del lavoratore in paesi Ue"): https://www.inps.it/it/it/dettaglio-approfondimento.schede-informative.certificato-di-distacco-del-lavoratore-in-paesi-ue.html
- **Foreign employer, worker in Italy.** Under Regulation (EC) 883/2004 a worker who normally works in Italy is insured in Italy unless an A1 from another country covers them. How a foreign employer with no Italian establishment registers and pays was not read for this skill; refer.
- **TFR abroad.** An employer that accrues TFR for staff working abroad, by contract or by law, also pays it to the Tesoreria if it meets the headcount (Circolare 12/2026 para. 1).
- Residence, treaties and the impatriati regime: `it-cross-border`, `it-impatriati`.

## Worked examples

### Example 1: EUR 35,000 at a commercial company with 10 employees

A shop company (INPS commerce class) employs 10 people, so it pays the FIS at 0.80%, of which 0.27% is the employee's. It is below every CIGS threshold. The employee is an impiegato on a permanent contract, gross pay EUR 35,000 for 2026, all of it in the contribution base and in the TFR base, below the EUR 56,224 band. The company is below the Tesoreria headcount and the employee has not joined a pension fund, so the TFR stays in the company. INAIL: office work is voce 0722; we assume the Terziario tasso medio of 4 per mille is the rate applied (a firm older than two years has its own adjusted rate on its INAIL basi di calcolo; use that).

1. Employer INPS rate: 23.81 + 1.31 + 0.30 + 0.20 + 0.68 + 0.24 + 2.44 + 0.53 = 29.51%. Employer INPS: EUR 10,328.50.
2. Employee INPS rate: 9.19 + 0.27 = 9.46%. Withheld: EUR 3,311.00.
3. TFR: 35,000 / 13.5 = EUR 2,592.59, less the 0.50% contribution of EUR 175.00 = EUR 2,417.59 added to the TFR fund.
4. INAIL: 35,000 x 4 / 1,000 = EUR 140.00, plus 1% = EUR 141.40.
5. Cost of the employee for 2026: 35,000 + 10,328.50 + 2,417.59 + 141.40 = EUR 47,887.49, about 1.37 times gross pay. IRPEF on the EUR 31,689 left after employee contributions is in `italy-payroll`.

```oa-check
name: Commerce, 10 staff, impiegato, gross EUR 35,000 (2026)
inputs:
  gross: 35000
  ivs_employer: 23.81
  naspi: 1.31
  training: 0.30
  tfr_guarantee: 0.20
  cuaf: 0.68
  maternity: 0.24
  sickness: 2.44
  fis_total: 0.80
  fis_employee: 0.27
  ivs_employee: 9.19
  tfr_divisor: 13.5
  tfr_contribution: 0.50
  inail_per_mille: 4
  inail_addizionale: 1
steps:
  - employer_rate: ivs_employer + naspi + training + tfr_guarantee + cuaf + maternity + sickness + (fis_total - fis_employee)
  - employer_inps: round(pct(gross, employer_rate), 2)
  - employee_rate: ivs_employee + fis_employee
  - employee_inps: round(pct(gross, employee_rate), 2)
  - tfr_gross: round(gross / tfr_divisor, 2)
  - tfr_net: tfr_gross - round(pct(gross, tfr_contribution), 2)
  - inail_base: gross * inail_per_mille / 1000
  - inail: round(inail_base + pct(inail_base, inail_addizionale), 2)
  - cost: gross + employer_inps + tfr_net + inail
expected:
  employer_rate: 29.51
  employer_inps: 10328.50
  employee_rate: 9.46
  employee_inps: 3311.00
  tfr_gross: 2592.59
  tfr_net: 2417.59
  inail: 141.40
  cost: 47887.49
```

### Example 2: the same salary at an industrial company with 120 employees

A manufacturer (INPS industry class) has had more than 50 staff since its first year, so it pays CIGO at 2.00% and CIGS at 0.90% (0.30% from the employee) and must pay TFR to the INPS Fondo di Tesoreria. The employee is an impiegato (no sickness contribution; an operaio would add 2.22%), gross EUR 35,000, not in a pension fund. Because all of the TFR goes to the Tesoreria, the employer does not pay the 0.20% Fondo di garanzia and takes the 0.28-point cut. INAIL: voce 0722, Industria tasso medio 5 per mille, on the same assumption as Example 1.

1. Employer INPS rate before relief: 23.81 + 1.31 + 0.30 + 0.20 + 0.68 + 0.46 + 2.00 + 0.60 = 29.36%.
2. Less 0.20 (Fondo di garanzia) and 0.28 (Tesoreria relief) = 28.88%. Employer INPS: EUR 10,108.00.
3. Employee INPS: 9.19 + 0.30 = 9.49%, EUR 3,321.50.
4. TFR: EUR 2,417.59 as in Example 1, but paid out each month to the Tesoreria by the 16th rather than kept in the business. It is still the employer's cost.
5. INAIL: 35,000 x 5 / 1,000 = EUR 175.00, plus 1% = EUR 176.75.
6. Cost for 2026: 35,000 + 10,108.00 + 2,417.59 + 176.75 = EUR 47,702.34. It is EUR 185.15 lower than Example 1: the Tesoreria relief and the absence of a sickness contribution for impiegati in industry more than offset the CIG contributions.

```oa-check
name: Industry, 120 staff, impiegato, TFR to the Tesoreria, gross EUR 35,000 (2026)
inputs:
  gross: 35000
  ivs_employer: 23.81
  naspi: 1.31
  training: 0.30
  tfr_guarantee: 0.20
  cuaf: 0.68
  maternity: 0.46
  cigo: 2.00
  cigs_total: 0.90
  cigs_employee: 0.30
  tesoreria_relief: 0.28
  ivs_employee: 9.19
  tfr_divisor: 13.5
  tfr_contribution: 0.50
  inail_per_mille: 5
  inail_addizionale: 1
  cost_example_1: 47887.49
steps:
  - rate_before_relief: ivs_employer + naspi + training + tfr_guarantee + cuaf + maternity + cigo + (cigs_total - cigs_employee)
  - employer_rate: rate_before_relief - tfr_guarantee - tesoreria_relief
  - employer_inps: round(pct(gross, employer_rate), 2)
  - employee_rate: ivs_employee + cigs_employee
  - employee_inps: round(pct(gross, employee_rate), 2)
  - tfr_to_tesoreria: round(gross / tfr_divisor, 2) - round(pct(gross, tfr_contribution), 2)
  - inail_base: gross * inail_per_mille / 1000
  - inail: round(inail_base + pct(inail_base, inail_addizionale), 2)
  - cost: gross + employer_inps + tfr_to_tesoreria + inail
  - saving_vs_example_1: cost_example_1 - cost
expected:
  rate_before_relief: 29.36
  employer_rate: 28.88
  employer_inps: 10108.00
  employee_rate: 9.49
  employee_inps: 3321.50
  tfr_to_tesoreria: 2417.59
  inail: 176.75
  cost: 47702.34
  saving_vs_example_1: 185.15
```

## Ask the client first

1. What is the company's INPS class (codice statistico contributivo) and its average headcount over the last six months and last year? (Industry or commerce, FIS rate, CIGO and CIGS, Tesoreria.)
2. What is each worker's grade (operaio, impiegato, quadro, apprentice) and contract (permanent, fixed-term, part-time)? (Sickness 2.22%, apprentice rates, NASpI addizionale.)
3. Which INAIL voci and which tasso applicato appear on the company's INAIL basi di calcolo? (Premium.)
4. Has each employee chosen a pension fund for the TFR, and when did the company start trading? (TFR destination, Fondo di garanzia and 0.28 relief.)
5. Where is each workplace, and was each employee hired in 2026 out of long unemployment, under 35, or a disadvantaged woman? (Decontribuzione Sud and the 2026 bonuses.)
6. Was the employee first insured with INPS before 1996, and is pay above EUR 56,224? (Massimale and the extra 1%.)

## Sources

| Source | URL | Read on |
|---|---|---|
| INPS, "Aliquote contributive" (IVS 33%, who pays, what drives the rates) | https://www.inps.it/it/it/inps-comunica/diritti-e-obblighi-in-materia-di-sicurezza-sociale-nell-unione-e/per-le-imprese/aliquote-contributive.html | 2026-10-23 |
| INPS Circolare 40/2011 (employee share 9.19%) | https://servizi2.inps.it/servizi/Bussola/visualizzadoc.aspx?svirtualurl=%2Fcircolari%2Fcircolare+numero+40+del+22-02-2011.htm | 2026-10-23 |
| INPS Circolare 6 of 30 January 2026 (minimum pay, first band, extra 1%, massimale) | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/01/Circolare_15151/Allegati/16546_Circolare-numero-6-del-30-01-2026.pdf | 2026-10-23 |
| INPS Circolare 53 of 3 April 2024 (NASpI, training levy, Fondo di garanzia, maternity and sickness by sector, FIS, CIGS) | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2024/04/Circolare_14535/Allegati/15128_Circolare-numero-53-del-03-04-2024.pdf | 2026-10-23 |
| INPS Circolare 117 of 20 October 2022, Allegato 1 (terziario rate table, CUAF 0.68%, FIS employee shares) | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2022/10/Circolare_13970/Allegati/14969_Circolare-numero-117-del-20-10-2022_Allegato-n-1.pdf | 2026-10-23 |
| INPS, "Aliquote contributive in vigore dal 1 gennaio 2010" (Circolare 25/2010, Allegato 14: industry and commerce rows by grade) | https://servizi2.inps.it/CircolariZIP/circolare%20numero%2025%20del%2018-02-2010_Allegato%20n%2014.pdf | 2026-10-23 |
| D.Lgs. 148/2015 arts. 10, 13, 20, 23, 29, 33 (CIGO, CIGS, FIS) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2015-09-14;148~art13!vig=2026-10-23 | 2026-10-23 |
| L. 92/2012 art. 2 (NASpI financing, addizionale 1.4% on fixed-term) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2012-06-28;92~art2!vig=2026-10-23 | 2026-10-23 |
| L. 153/1969 art. 12 (contribution base) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1969-04-30;153~art12!vig=2026-10-23 | 2026-10-23 |
| Civil Code art. 2120 (TFR) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2120!vig=2026-10-23 | 2026-10-23 |
| L. 297/1982 arts. 2 and 3 (Fondo di garanzia; 0.50% deducted from TFR) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1982-05-29;297~art3!vig=2026-10-23 | 2026-10-23 |
| INPS Circolare 12 of 5 February 2026 (Fondo di Tesoreria after L. 199/2025; 7.41% less 0.50%; reliefs; deadline) | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/02/Circolare_15160/Allegati/16559_Circolare-numero-12-del-05-02-2026.pdf | 2026-10-23 |
| INPS, "TFR a carico del Fondo di Tesoreria" (60, 50 and 40 thresholds) | https://www.inps.it/it/it/dettaglio-scheda.it.schede-servizio-strumento.schede-servizi.50018.tfr-a-carico-del-fondo-di-tesoreria.html | 2026-10-23 |
| INPS messaggio 1478/2019 (apprentices: 10%, 1.31%, 0.30%; cuts for up to 9 staff) | https://www.inps.it/bussola/VisualizzaDoc.aspx?sVirtualURL=/Messaggi/Messaggio+numero+1478+del+10-04-2019.htm | 2026-10-23 |
| INPS, "Insieme per il tuo futuro" booklet (apprentice 10% and 5.84%) | https://www.inps.it/content/dam/inps-site/pdf/inpscomunica/Libretto_INPS_giovani.pdf | 2026-10-23 |
| INPS Circolare 32 of 30 January 2025 (Decontribuzione Sud PMI, 2026 at 20%, EUR 125) | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2025/01/Circolare_14812/Allegati/15880_Circolare-numero-32-del-30-01-2025.pdf | 2026-10-23 |
| INPS news, 14 May 2026 (Circolari 55, 56 and 57/2026: 2026 hiring bonuses) | https://www.inps.it/it/it/inps-comunica/notizie/dettaglio-news-page.news.2026.05.giovani-donne-e-zes-incentivi-per-la-stabilizzazione-professionale.html | 2026-10-23 |
| INAIL Circolare 38 of 24 June 2025 (voce 0722 tassi medi) | https://www.inail.it/content/dam/inail-hub-site/documenti/circolari/2025/06/Circolare%20n%2038_24%20giugno%202025.pdf | 2026-10-23 |
| INAIL, Guida autoliquidazione 2025/2026 (dates, premium formula, 1% addizionale, penalties) | https://www.inail.it/content/dam/assicurazione/documenti/2025/12/Guida%20autoliquidazione%202025-2026.pdf | 2026-10-23 |
| D.Lgs. 241/1997 art. 18 (payment by the 16th) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-07-09;241~art18!vig=2026-10-23 | 2026-10-23 |
| D.L. 269/2003 art. 44 c. 9 (UniEmens monthly) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2003-09-30;269~art44!vig=2026-10-23 | 2026-10-23 |
| L. 388/2000 art. 116 c. 8 (sanzioni civili) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2000-12-23;388~art116!vig=2026-10-23 | 2026-10-23 |
| INPS Circolare 98 of 11 September 2026 (reference rate 2.65%) | https://www.inps.it/it/it/inps-comunica/atti/circolari-messaggi-e-normativa/dettaglio.circolari-e-messaggi.2026.09.circolare-numero-98-del-11-09-2026_15369.html | 2026-10-23 |
| D.L. 463/1983 art. 2 c. 1-bis (withheld contributions not paid) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:1983-09-12;463~art2!vig=2026-10-23 | 2026-10-23 |
| INPS, "Certificato di distacco del lavoratore in paesi Ue" | https://www.inps.it/it/it/dettaglio-approfondimento.schede-informative.certificato-di-distacco-del-lavoratore-in-paesi-ue.html | 2026-10-23 |

Not yet confirmed: no INPS publication for 2026 prints the full rate set for industry and commerce, so the totals are built from the 2022 and 2024 INPS circulars, the INPS 2010 rate tables (CUAF 0.68% for industry and commerce, sickness 2.44% for commerce impiegati) and the statutes; L. 199/2025 was not read line by line for changes to these smaller contributions. INPS rate tables show no separate line for the 0.50% of L. 297/1982, which we read as sitting inside the employer's 23.81%. The INAIL rate a given firm pays (its tasso applicato after oscillation and prevention cuts) and any general INAIL premium cut for 2026 were not read; the examples use the voce 0722 tasso medio. The 2026/2027 INAIL autoliquidazione dates, the full conditions of the D.L. 62/2026 bonuses (read only from the INPS news item) and the 2026 rules for foreign employers registering with INPS were not read.
