---
name: italy-payroll
description: Use this skill whenever asked about Italian payroll processing for employees. Trigger on phrases like "Italian payroll", "busta paga", "cedolino", "IRPEF ritenuta", "ritenuta d'acconto dipendenti", "INPS contributi", "contributi previdenziali", "TFR", "trattamento di fine rapporto", "CU certificazione unica", "F24", "tredicesima", "quattordicesima", "stipendio netto Italia", "brutto netto Italia", "Agenzia delle Entrate", "addizionale regionale", "addizionale comunale", "CCNL minimum wage", "ferie maturate", "malattia INPS", "maternità INPS", or any question about computing employee pay, income tax withholding, or social contributions in Italy. This skill covers IRPEF withholding, INPS contributions (employee and employer), TFR, mandatory benefits, busta paga (payslip) requirements, CU/F24 filing, and employer cost analysis. ALWAYS read this skill before processing any Italian employee payroll.
version: 1.0
jurisdiction: IT
tax_year: 2026
last_updated: 2026-09-22
review_status: pending_review
drafted_by: OpenAccountants
approved_by: pending
depends_on:
  - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Italian payroll for employees: IRPEF withholding, INPS, TFR, CU and F24

How an Italian employer runs payroll as sostituto d'imposta: IRPEF withholding with the detrazioni and cuneo fiscale, surcharges, INPS, TFR, leave, the payslip, CU, 770 and F24, and withholding on professionals' fees. Figures are for tax year 2026 (the calendar year). Statutes were read on Normattiva as in force on 30 June 2026: the new TUIR (D.Lgs. 117/2026) applies only from 1 January 2027, yet Normattiva already shows some 2026 rules repealed. Other dates: the employee pension share is from INPS circolare 40/2011 (a standing rate); the INPS rate page was updated September 2024; the Agenzia IRPEF page (13 January 2026) gives the 2026 middle rate only in a note.

## Section 1: Quick Reference

| Field | Value |
| --- | --- |
| Country | Italy (Repubblica Italiana) |
| Standard pay frequency | Monthly; 13 or 14 instalments by CCNL |
| Tax year | Calendar year (1 January to 31 December) |
| Income tax withholding | IRPEF ritenuta alla fonte (D.P.R. 600/1973 art. 23) |
| Local tax surcharges | Addizionale regionale and addizionale comunale IRPEF |
| Social insurance authority | INPS |
| Tax authority | Agenzia delle Entrate |
| Key legislation | TUIR arts. 11 and 13; L. 207/2024; L. 199/2025; Codice Civile art. 2120; D.P.R. 322/1998 art. 4 |
| INPS contribution ceiling | See Section 3 (post-1995 contributors only) |
| Validated by | Pending: requires sign-off by an Italian commercialista or consulente del lavoro |

## Section 2: Income Tax Withholding (IRPEF)

- **IRPEF withholding mechanism.** Each month the employer withholds IRPEF on pay less employee INPS, applying the detrazioni in proportion to the pay period. By 28 February, or on termination, the conguaglio recomputes the year's tax and settles the difference (D.P.R. 600/1973 art. 23(3)): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art23!vig=2026-06-30

### IRPEF Tax Brackets (2026: Legge di Bilancio 2026)

| Taxable income (annual) | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art11!vig= |
| Top of first bracket | EUR 28,000 | "a) fino a 28.000 euro, 23 per cento" |
| Top of second bracket | EUR 50,000 | "b) oltre 28.000 euro e fino a 50.000 euro, ((33 per cento))" |

| Bracket | Rate | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/imposta-sul-reddito-delle-persone-fisiche-irpef-/aliquote-e-calcolo-dell-irpef |
| Up to EUR 28,000 | 23% | "fino a euro 28.000 23% 23% sull’intero importo" |
| Over EUR 28,000 up to EUR 50,000, from 2026 income | 33% | "ha ridotto la seconda aliquota dell’Irpef dal 35 al 33 per cento" |
| Over EUR 50,000 | 43% | "43% sul reddito eccedente i 50.000 euro" |
| Gross tax on the first EUR 50,000 at 2026 rates | EUR 13,700 | "l’imposta dovuta è pari a 13.700 euro (non più 14.140)" |

- **Key 2026 change.** The middle rate was cut for 2026 (L. 199/2025 art. 1 comma 3); the Agenzia table still shows the 2025 rate, and the note below it gives the 2026 rate.
- **High-income neutralisation.** Above the income in the table below, the detrazioni for certain oneri are cut (TUIR art. 16-ter(5-bis)); not a surcharge on pay.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199 |
| Total income above which the cut applies | EUR 200,000 | "reddito complessivo superiore a 200.000 euro" |
| Cut to the detrazioni for oneri | EUR 440 | "diminuito di un importo pari a 440 euro" |

### Tax-Free Threshold and Detrazioni per Lavoro Dipendente

No statutory tax-free allowance exists. The detrazione is subtracted from gross tax, pro rata to days worked; at low incomes it wipes out the tax. The live Guide's fixed amount for the top band was wrong; the statute's formula is below.

| Total income (reddito complessivo) | Detrazione | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art13!vig=2026-06-30 |
| Up to EUR 15,000 | EUR 1,955 | "a) ((1.955 euro)) , se il reddito complessivo non supera 15.000 euro" |
| Floor for income up to EUR 15,000 | EUR 690 | "690 euro. Per i rapporti di lavoro a tempo determinato" |
| Floor for fixed-term contracts, income up to EUR 15,000 | EUR 1,380 | "inferiore a 1.380 euro" |
| Over EUR 15,000 up to EUR 28,000 | EUR 1,910 plus EUR 1,190 times (EUR 28,000 less income) divided by EUR 13,000 | "1.910 euro, aumentata del prodotto tra 1.190 euro" |
| Over EUR 28,000 up to EUR 50,000 | EUR 1,910 times (EUR 50,000 less income) divided by EUR 22,000 | "l'importo di 50.000 euro, diminuito del reddito complessivo, e l'importo di 22.000 euro" |
| Over EUR 50,000 | none | the formula reaches zero at the limit |
| Extra, income over EUR 25,000 up to EUR 35,000 | EUR 65 | "aumentata di un importo pari a 65 euro" |

- **Not covered here:** trattamento integrativo (D.L. 3/2020 art. 1) and family detrazioni (TUIR art. 12); amounts not read.
- Total income for the detrazione excludes the main home and its pertinenze (art. 13(6-bis)).

### Cuneo fiscale 2026: the tax-free sum and the extra detrazione

Two tax measures, granted automatically in payroll from 2025 (L. 207/2024 art. 1 commi 4 to 9), apply to 2026 pay. Normattiva's current view shows comma 6 repealed from 2027; the table reads the law at 30 June 2026.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207!vig=2026-06-30 |
| Tax-free sum: total income cap | EUR 20,000 | "reddito complessivo non superiore a 20.000 euro è riconosciuta una somma" |
| Tax-free sum, employment income up to EUR 8,500 | 7.1% | "a) 7,1 per cento, se il reddito di lavoro dipendente non è superiore a 8.500 euro" |
| Over EUR 8,500 up to EUR 15,000 | 5.3% | "b) 5,3 per cento, se il reddito di lavoro dipendente è superiore a 8.500 euro" |
| Over EUR 15,000 | 4.8% | "c) 4,8 per cento, se il reddito di lavoro dipendente è superiore a 15.000 euro" |
| Extra detrazione, total income over EUR 20,000 up to EUR 32,000 | EUR 1,000 | "a) a 1.000 euro, se l'ammontare del reddito complessivo è superiore a 20.000 euro" |
| Over EUR 32,000 up to EUR 40,000 | EUR 1,000 times (EUR 40,000 less income) divided by EUR 8,000 | "e 8.000 euro, se l'ammontare del reddito complessivo è superiore a 32.000 euro ma non a 40.000 euro" |
| Recovery in ten instalments if the amount wrongly granted exceeds | EUR 60 | "superiore a 60 euro, il recupero dello stesso è effettuato in dieci rate" |

- **The tax-free sum** is the percentage applied to the employee's employment income; it is paid in the payslip and is not income; the band uses employment income scaled to a full year (comma 5). The employer recovers it by F24 offset (comma 8). **The extra detrazione** reduces gross tax, pro rata to the period worked.
- **Who is covered.** Employees under TUIR art. 49, not pensioners. Total income includes exempt impatriati income and excludes the main home (comma 9). Entitlement is checked at the conguaglio (comma 7).

### Other 2026 payroll tax measures (L. 199/2025)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199 |
| Substitute tax on 2026 pay rises from contract renewals signed 1 January 2024 to 31 December 2026 | 5% | "regionali e comunali pari al 5 per cento" |
| Only for private-sector employees whose 2025 employment income was not above | EUR 33,000 | "nell'anno 2025, non superiore a 33.000 euro" |
| Substitute tax on night, holiday, rest-day and shift supplements paid in 2026 | 15% | "regionali e comunali pari al 15 per cento le somme corrisposte" |
| Yearly limit of those supplements | EUR 1,500 | "entro il limite annuo di 1.500 euro" |
| Only for private-sector employees, except at the tourism and food-service employers of comma 18, whose 2025 employment income was not above | EUR 40,000 | "nell'anno 2025, a 40.000 euro" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199!vig=2026-06-30 |
| Substitute tax on productivity bonuses and profit shares paid in 2026 and 2027 (L. 208/2015 art. 1 comma 182) | 1% | "con l'aliquota ridotta all'1 per cento" |
| Yearly limit for that rate | EUR 5,000 | "entro il limite di importo complessivo di 5.000 euro" |

- The other conditions of L. 208/2015 art. 1 commi 182 and following apply; they were not read here. Normattiva's current view shows comma 9 repealed by D.Lgs. 117/2026, which applies from 2027. These bonuses do not count towards the EUR 1,500 yearly limit of the supplements above (comma 11).
- Both replace IRPEF and addizionali unless the employee waives them in writing; for the supplements, contributions are unchanged (comma 11); supplements replacing ordinary pay are excluded (commi 7, 10, 11). If another employer issued the 2025 CU, the employee states the 2025 employment income in writing (comma 11).

### Addizionali IRPEF (Regional and Municipal Surcharges)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2011-05-06;68~art6!vig=2026-06-30 |
| Addizionale regionale base rate | 1.23% | "La predetta aliquota di base è pari a 1,23 per cento" |
| Maximum rise a region may add to the base rate, from 2015 | 2.1 points | "c) a 2,1 punti percentuali a decorrere dall'anno 2015" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1998-09-28;360~art1!vig=2026-06-30 |
| Addizionale comunale acconto, share of the prior-year surcharge | 30% | "L'acconto è stabilito nella misura del 30 per cento dell'addizionale" |
| Maximum total variation of the comunale rate | 0.8 points | "eccedere complessivamente 0,8 punti percentuali" |

- **Rates.** A region may raise the base rate by up to 2.1 percentage points (D.Lgs. 68/2011 art. 6); a comune may vary its rate by at most 0.8 percentage points and set an exemption threshold (D.Lgs. 360/1998 art. 1). The live Guide's upper figures were wrong or unproven; use the domicile on 1 January.
- **Addizionali withholding timing.** For the comunale: the acconto is withheld in up to nine monthly instalments from March; the balance, fixed at the conguaglio, in up to eleven from the next pay period, ending by December; on termination at once (D.Lgs. 360/1998 art. 1(5)). The regionale timing (D.Lgs. 446/1997 art. 50) was not re-read.

## Section 3: Social Security, Employee Deductions (2026)

### INPS Contributions (Employee Share)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.inps.it/it/it/inps-comunica/diritti-e-obblighi-in-materia-di-sicurezza-sociale-nell-unione-e/per-le-imprese/aliquote-contributive.html |
| Pension (IVS) rate, fondo pensioni lavoratori dipendenti, employer and employee together | 33% | "cosiddetta AGO) è pari al 33%" |

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://servizi2.inps.it/servizi/Bussola/visualizzadoc.aspx?svirtualurl=%2Fcircolari%2Fcircolare+numero+40+del+22-02-2011.htm |
| Employee share of the pension (IVS) rate | 9.19% | "Totale a carico del lavoratore 33,00% 9,19%" |

- **Rate variation.** This is the fondo pensioni lavoratori dipendenti general rate; the employer withholds it each pay period and pays both shares. Other contributions vary by sector, size and category and are mostly employer-only; the live Guide's sector variants were unproven and removed.
- **Extra employee contribution.** One extra point on pay above the first pension band, month by month (table below).

### INPS Ceiling (Massimale, 2026)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/01/Circolare_15151/Allegati/16546_Circolare-numero-6-del-30-01-2026.pdf |
| Daily minimum pay for contributions (minimale giornaliero) | EUR 58.13 | "Minimale di retribuzione giornaliera (9,5%) 58,13" |
| Hourly minimum, part-time, 40-hour week | EUR 8.72 | "58,13 euro x 6/40 = 8,72 euro" |
| Extra employee contribution | 1% | "l'aliquota aggiuntiva dell’1% deve essere applicata" |
| First pension band (extra contribution above it), yearly | EUR 56,224 | "Prima fascia di retribuzione pensionabile annua 56.224,00" |
| Same band, monthly | EUR 4,685 | "Importo mensilizzato 4.685,00" |
| Massimale annuo (post-1995 contributors) | EUR 122,295 | "Massimale annuo della base contributiva 122.295,00" |

- **Massimale applicability.** Only workers first insured after 31 December 1995, and those opting for the contributory pension; no pension contributions, employee or employer, above it.
- **Minimum.** Contributions are due on at least the CCNL pay and the daily minimum; the live Guide's "minimale annuo" belonged to traders and craftsmen and is removed.

## Section 4: Social Security, Employer Contributions (2026)

### INPS Contributions (Employer Share)

- **Total employer INPS rate range.** The employer pays the rest of the pension rate (Section 3) plus, by sector and size: malattia, maternità, NASpI, CIG/CIGS/fondi di solidarietà, Fondo di garanzia TFR, CUAF; and INAIL (risk-based, separate). No allowed page prints these rates; the live Guide's percentages are removed.

### Typical Total Employer Rates

Not printed on any allowed page. Use the company's INPS classification (inquadramento) and the CCNL. For IRAP on staff costs see `it-irap`.

## Section 5: Minimum Wage and Overtime

### Minimum Wage

- **No statutory national minimum wage.** Minimum pay is set by the applicable CCNL, which sets paga base, contingenza and EDR and changes at each renewal. The live Guide's CCNL amounts were not proven and are removed; read the current CCNL tables.

### Working Hours and Overtime

| Rule | Detail |
| --- | --- |
| Legal normal week | 40 hours (D.Lgs. 66/2003 art. 3) |
| Maximum including overtime | 48 hours, averaged over 4 months (CCNL may extend) |
| Annual overtime cap | 250 hours unless the CCNL says otherwise |
| Overtime and night supplements | Set by the CCNL (live Guide percentages removed) |

Kept from the live Guide; D.Lgs. 66/2003 was not re-read.

## Section 6: Mandatory Benefits

### Tredicesima (13th Month Salary)

| Entitlement | Detail |
| --- | --- |
| Amount | One extra month's pay |
| Accrual | One twelfth per month worked |
| Payment | December |
| Source | Paid under the CCNL; the live Guide's claim that a statute requires it for all employees was not proven |
| Subject to IRPEF and INPS | Yes; IRPEF is withheld on it on its own, using the yearly brackets scaled to one month (D.P.R. 600/1973 art. 23(2)(b)); it then enters the conguaglio |

### Quattordicesima (14th Month Salary)

| Entitlement | Detail |
| --- | --- |
| Amount | One extra month's pay |
| Required | Only where the CCNL provides it (for example Commercio, Turismo) |
| Payment | Usually June or July |

### TFR (Trattamento di Fine Rapporto)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2120!vig= |
| Revaluation each 31 December, fixed part | 1.5% | "un tasso costituito dall'1,5 per cento in misura fissa e dal 75 per cento" |
| Revaluation, share of the consumer price index rise | 75% | "dal 75 per cento dell'aumento dell'indice dei prezzi al consumo" |

- **Accrual formula.** Each year's TFR equals that year's pay divided by 13.5 (art. 2120), after the Fondo di garanzia deduction the law allows.
- **Destination.** Kept by the employer or paid to a pension fund of the employee's choice; larger employers pay retained TFR to the INPS Fondo di Tesoreria. The 2026 headcount threshold was not read on an allowed page.
- **Tax treatment.** Tassazione separata at the employee's average rate (TUIR art. 19), F24 code 1012; the revaluation's substitute tax rate was not proven here.

### Ferie (Annual Leave)

| Entitlement | Detail |
| --- | --- |
| Statutory minimum | 4 weeks a year (D.Lgs. 66/2003 art. 10) |
| Typical CCNL | More, by seniority |
| Non-substitutable | At least 2 weeks taken in the year; the 4-week minimum cannot be paid out except on termination |
| Festività | National public holidays are paid |

Kept from the live Guide; not re-read for this refresh.

### Sick Leave (Malattia)

| Entitlement | Detail |
| --- | --- |
| INPS indennità | Paid by INPS from day 4 up to 180 days a year, at a share of average daily pay set by law; the live Guide's percentages were unproven and removed |
| Employer top-up | Per CCNL |
| Waiting period | First 3 days (carenza) paid by the employer under most CCNLs |
| Medical certificate | Sent online by the doctor to INPS; the employer is notified |

### Maternity Leave (Congedo di Maternità)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2001-03-26;151~art22!vig=2026-06-30 |
| Maternity allowance for the whole leave | 80% | "un'indennità giornaliera pari all'80 per cento della retribuzione" |

- **Duration.** Five months, usually two before and three after birth (D.Lgs. 151/2001 art. 16); counts for tredicesima and ferie (art. 22(3)).

**Parental leave (congedo parentale, D.Lgs. 151/2001 art. 34)**

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2001-03-26;151~art34!vig=2026-06-30 |
| Allowance, three months per parent (not transferable), until the child is 14 | 30% | "un'indennità pari al 30 per cento della retribuzione, elevata" |
| Raised allowance, up to three months in total between the parents, until the child is 6 | 80% | "alla misura dell'80 per cento della retribuzione e, per la durata massima" |

- A further three months, shared, is paid at the lower rate; a single parent gets up to nine months at it.

### Paternity Leave (Congedo di Paternità)

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2001-03-26;151~art29!vig=2026-06-30 |
| Allowance for the compulsory paternity leave | 100% | "un'indennità giornaliera pari al 100 per cento della retribuzione" |

- **Duration and timing.** Ten working days (twenty for multiple births), from two months before to five months after the birth (art. 27-bis).

## Section 7: Payslip Requirements

- **Payslip governing law.** The busta paga (cedolino) is governed by L. 4/1953 and later rules.

### Mandatory Payslip Fields

| Field | Required |
| --- | --- |
| Employer and employee details (codice fiscale, INPS position, qualifica, livello, CCNL) | Yes |
| Pay period, hours, overtime, CCNL pay elements, gross pay | Yes |
| INPS contributions, IRPEF, addizionali withheld; detrazioni and cuneo fiscale sum | Yes |
| TFR accrual for the period | Yes (or annual statement) |
| Net pay (netto in busta) | Yes |
| Ferie and ROL/permessi accrued, used, remaining | Yes |

### Delivery

- Paper or electronic (with consent); the CU is the annual summary.

## Section 8: Filing Obligations

### Monthly

| Obligation | Deadline | Method |
| --- | --- | --- |
| F24: IRPEF, addizionali, INPS | 16th of the month after payment (next working day if a Saturday or holiday) | F24 telematico |
| UniEmens (INPS monthly return) | End of the following month | Kept from the live Guide |

- 16th rule for sostituti d'imposta (Agenzia): https://www.agenziaentrate.gov.it/portale/schede/pagamenti/versamento-modello-f24-ritenute-su-reddito-di-lavoro-autonomo-f24_rit_red_lav_aut/come-e-quando-si-versa-f24_rit_red_lav_aut

**F24 codici tributo for withholding (Agenzia list for the 770 of 2026)**: https://www.agenziaentrate.gov.it/portale/documents/20143/9741427/allegato+1+-+codici+tributo+F24_770-2026.pdf/d9d83f8b-d8e0-3045-4469-e7bd3301026a?t=1771600455976

| Code | What |
| --- | --- |
| 1001 | IRPEF withheld on pay, pensions, trasferte, extra months and the conguaglio |
| 1002 | IRPEF withheld on arrears (emolumenti arretrati) |
| 1012 | IRPEF withheld on TFR and other termination payments (tassazione separata) |
| 1040 | Withholding on fees for arts and professions |
| 3802 | Addizionale regionale withheld by the sostituto d'imposta |
| 3847 | Addizionale comunale withheld, acconto |
| 3848 | Addizionale comunale withheld, saldo |
| 1704 | Employer's credit for the tax-free sum paid to employees (L. 207/2024 art. 1 comma 4), used in offset |

INPS contributions go in the INPS section of the same F24 (causali not re-read).

### Annual

| Obligation | Deadline | Notes |
| --- | --- | --- |
| Conguaglio | 28 February, or on termination | D.P.R. 600/1973 art. 23(3) |
| CU to the employee | 16 March of the following year (12 days after a request if the job ends) | art. 4(6-quater) |
| CU to the Agenzia delle Entrate | 16 March of the following year | art. 4(6-quinquies) |
| CU with only self-employment fees or agents' commissions | 30 April of the following year, from 2026 | art. 4(6-quinquies) |
| Modello 770 (withholding agent return) | 31 October of the following year | art. 4(3-bis) |
| Autoliquidazione INAIL | 16 February (payment) and 28 February (declaration) | Kept from the live Guide; not an allowed host |

D.P.R. 322/1998 art. 4: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art4!vig=2026-06-30

### Employee Obligations

| Item | Detail |
| --- | --- |
| Modello 730 | The 2026 return (2025 income) was due by 30 September 2026; the sostituto d'imposta applies the refund or debit in payroll |
| Modello Redditi PF | Alternative to the 730; online by 31 October of the following year (D.P.R. 322/1998 art. 2). The live Guide's 30 November was wrong |

Sources: https://www.agenziaentrate.gov.it/portale/quando-e-come-presentare-il-730-2026 and https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig=2026-06-30

### Withholding on fees to self-employed professionals

When a business pays a resident professional's fee, it withholds on account and pays by F24 with code 1040.

| Item | Value | Note |
| --- | --- | --- |
| Source | all figures below | https://www.agenziaentrate.gov.it/portale/schede/pagamenti/versamento-modello-f24-ritenute-su-reddito-di-lavoro-autonomo-f24_rit_red_lav_aut/aliquote-f24_rit_red_lav_aut |
| Resident professional, withholding on account | 20% | "la ritenuta, effettuata a titolo d’acconto, è pari al 20%" |
| Non-resident, services performed in Italy, final withholding | 30% | "si applica una ritenuta a titolo di imposta in misura del 30%" |

- Normattiva's text of D.P.R. 600/1973 art. 25 still prints the 1973 rate; later laws, in its notes, raised it. Use the table; forfettari are exempt. See `it-income-tax`.

## Section 9: Common Payroll Patterns

### Typical Bank Statement Descriptions (Salary Credits)

| Pattern | Classification |
| --- | --- |
| STIPENDIO, EMOLUMENTI, BUSTA PAGA | Net salary payment |
| TREDICESIMA, 13A MENSILITA | 13th month salary |
| QUATTORDICESIMA, 14A MENSILITA | 14th month salary (if applicable) |
| TFR, LIQUIDAZIONE | TFR paid on termination |
| INDENNITA MALATTIA INPS | Sickness allowance (from INPS, may pass through the employer) |
| INDENNITA MATERNITA | Maternity allowance |
| RIMBORSO 730 | Modello 730 refund through payroll |

### Typical Employer Debit Patterns

| Pattern | Classification |
| --- | --- |
| F24 INPS, CONTRIBUTI INPS | INPS contribution payment |
| F24 IRPEF, RITENUTE | IRPEF and addizionali payment |
| INAIL PREMIO | Accident insurance premium |
| FONDO TESORERIA INPS | TFR transfer to the INPS fund |
| FONDO PENSIONE (name) | Supplementary pension fund contribution |

## Section 10: Interaction with Other Guides

| Scenario | Guide to use |
| --- | --- |
| Employee payroll (IRPEF and INPS) | This Guide (`italy-payroll`) |
| Self-employed income tax | `it-income-tax` |
| Self-employed INPS (gestione separata, artigiani, commercianti) | `it-inps-contributions` |
| IRAP | `it-irap` |
| Italian VAT (IVA) | `italy-vat-return` |
| E-invoicing (FatturaPA / SDI) | `italy-einvoice` |

### Key Handoff Points

- **Payroll to Bookkeeping.** Gross pay, employer INPS, INAIL and TFR accrual are costs. Amounts withheld are debts (debiti verso erario, verso INPS) until paid by F24; TFR sits in the fondo TFR until paid or transferred.
- **Payroll to Income Tax.** CU data feed the 730 or Redditi PF; 730 results are settled in payroll.
- **Payroll to INPS.** UniEmens reconciles with F24 and with CU totals.

## The method, step by step

1. **Gross pay and INPS.** Apply the CCNL pay, overtime and extra months; check the daily minimum; withhold the employee share, the extra point above the first band, and stop at the massimale for post-1995 contributors (INPS circolare 6/2026): https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/01/Circolare_15151/Allegati/16546_Circolare-numero-6-del-30-01-2026.pdf
2. **Gross IRPEF.** Taxable pay is gross less employee contributions and exempt items; apply TUIR art. 11 with the 2026 middle rate; keep amounts under the 2026 substitute taxes apart: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art11!vig=
3. **Detrazioni and cuneo fiscale.** Subtract the art. 13 detrazione and, where due, the extra detrazione; add the tax-free sum to net pay (L. 207/2024 art. 1 commi 4 to 9): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207!vig=2026-06-30
4. **Addizionali and TFR.** Withhold the surcharge instalments (D.Lgs. 360/1998 art. 1(5)); accrue TFR at pay divided by 13.5: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1998-09-28;360~art1!vig=2026-06-30
5. **Pay and report.** F24 by the 16th with the Section 8 codes; conguaglio by 28 February; CU by 16 March; 770 by 31 October (D.P.R. 322/1998 art. 4): https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art4!vig=2026-06-30

## Ask the client first

- Which CCNL applies, and what level and contract type (permanent, fixed-term, part-time, apprentice) does the employee have?
- When was the employee first insured with INPS: before 1996, or from 1996 (massimale)?
- What was the employee's 2025 income, and any other 2026 income? (Detrazione, cuneo fiscale, substitute taxes.)
- Where was the employee's tax domicile on 1 January (addizionali)?
- Has the employee chosen a pension fund for the TFR, and how many employees does the company have (Fondo di Tesoreria)?
- Did the employee work for another employer earlier in the year, and do they want that pay included in the conguaglio?

## When to refuse or refer

- Employer contribution rates, INAIL premiums, CIG/fondi di solidarietà: not printed here; refer to a consulente del lavoro.
- Dirigenti, apprentices, agricultural, domestic, entertainment and public-sector workers (special schemes).
- Non-resident, cross-border, impatriati or seconded employees. Refer.
- Termination packages, TFR advances and settlements, and taxation of arrears. Refer.
- Periods before 2026, or from 2027 under the new TUIR.
- Any payslip that will actually be paid: a qualified professional must sign it off.

## Sources

- TUIR art. 11: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art11!vig=
- TUIR art. 13: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1986-12-22;917~art13!vig=2026-06-30
- Agenzia, IRPEF rates: https://www.agenziaentrate.gov.it/portale/imposta-sul-reddito-delle-persone-fisiche-irpef-/aliquote-e-calcolo-dell-irpef
- L. 199/2025: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199
- L. 207/2024: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207!vig=2026-06-30
- D.Lgs. 68/2011 art. 6: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2011-05-06;68~art6!vig=2026-06-30
- D.Lgs. 360/1998 art. 1: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1998-09-28;360~art1!vig=2026-06-30
- D.P.R. 600/1973 art. 23: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1973-09-29;600~art23!vig=2026-06-30
- D.P.R. 322/1998 art. 4: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art4!vig=2026-06-30
- INPS circolare 6/2026: https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/01/Circolare_15151/Allegati/16546_Circolare-numero-6-del-30-01-2026.pdf
- INPS, contribution rates: https://www.inps.it/it/it/inps-comunica/diritti-e-obblighi-in-materia-di-sicurezza-sociale-nell-unione-e/per-le-imprese/aliquote-contributive.html
- INPS circolare 40/2011: https://servizi2.inps.it/servizi/Bussola/visualizzadoc.aspx?svirtualurl=%2Fcircolari%2Fcircolare+numero+40+del+22-02-2011.htm
- Civil Code art. 2120: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:regio.decreto:1942-03-16;262:2~art2120!vig=
- D.Lgs. 151/2001 arts. 22, 29, 34: https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2001-03-26;151~art22!vig=2026-06-30
- Agenzia, F24 codes for the 770: https://www.agenziaentrate.gov.it/portale/documents/20143/9741427/allegato+1+-+codici+tributo+F24_770-2026.pdf/d9d83f8b-d8e0-3045-4469-e7bd3301026a?t=1771600455976
- Agenzia, withholding on fees: https://www.agenziaentrate.gov.it/portale/schede/pagamenti/versamento-modello-f24-ritenute-su-reddito-di-lavoro-autonomo-f24_rit_red_lav_aut/aliquote-f24_rit_red_lav_aut
- https://www.agenziaentrate.gov.it/portale/quando-e-come-presentare-il-730-2026
- https://www.agenziaentrate.gov.it/portale/schede/pagamenti/versamento-modello-f24-ritenute-su-reddito-di-lavoro-autonomo-f24_rit_red_lav_aut/come-e-quando-si-versa-f24_rit_red_lav_aut
- https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.del.presidente.della.repubblica:1998-07-22;322~art2!vig=2026-06-30
- https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2001-03-26;151~art29!vig=2026-06-30
- https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2001-03-26;151~art34!vig=2026-06-30
- https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199!vig=2026-06-30

## PROHIBITIONS

- NEVER apply a flat rate or the 2025 middle IRPEF rate to 2026 pay
- NEVER forget the addizionali: they depend on the employee's domicile
- NEVER treat the INPS massimale as a general salary cap: it only affects post-1995 contributors
- NEVER compute TFR without the art. 2120 formula
- NEVER use the rate in the body text of D.P.R. 600/1973 art. 25 as the fee withholding rate
- NEVER assume a national minimum wage: use the CCNL
- NEVER present payroll computations as definitive: a commercialista or consulente del lavoro signs off

## Disclaimer

This Guide and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this Guide. All outputs must be reviewed and signed off by a qualified professional (such as a commercialista or consulente del lavoro in Italy) before implementation.

> Contributed by OpenAccountants.

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
