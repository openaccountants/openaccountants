---
name: it-inps-contributions
description: "Italian INPS social contributions for the self-employed, tax year 2026, centred on the gestione separata for professionals with a VAT number and no professional fund. Covers who is in it, the 2026 rates (26.07% with no other cover, 24% for pensioners and the otherwise insured, 33.72% and 35.03% for collaborators), the EUR 122,295 massimale, the EUR 18,808 minimale and months credited, the 4% rivalsa, Quadro RR, the 80% acconto rule, F24 causali and deadlines, sanzioni civili and the 2026 definizione agevolata. Gives the 2026 headline figures for artigiani and commercianti (fixed contributions on the minimale, 24% and 24.48%, the 35% cut for forfettari) and points to it-inps-artigiani-commercianti for the detail. Trigger on: gestione separata, INPS freelance, aliquota INPS 2026, rivalsa 4%, Quadro RR, acconto INPS, massimale INPS, contributi artigiani commercianti. Out of scope: employees (italy-payroll, it-employer-contributions), professional funds (it-inps-artigiani-commercianti), income tax (it-income-tax, it-regime-forfettario)."
version: 2.1
jurisdiction: IT
tax_year: 2026
last_updated: 2026-10-24
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
depends_on:
  - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# INPS contributions for the self-employed in Italy (gestione separata, artigiani and commercianti), 2026

A self-employed person in Italy pays pension contributions to INPS unless a professional fund (cassa) covers them. Professionals with a VAT number and no cassa pay a percentage of their income to the gestione separata. Craft and trading businesses pay a fixed amount on a minimum income to the gestione artigiani or commercianti, then a percentage above it. Both are worked out in the income tax return (Quadro RR) and paid by F24.

See also, not repeated here:
- `it-inps-artigiani-commercianti`: full rules for artigiani and commercianti, family helpers, SRL members and the professional funds table.
- `italy-payroll` and `it-employer-contributions`: INPS for employees, paid by the employer.
- `it-income-tax` (regime ordinario) and `it-regime-forfettario`: the income that forms the base, and the deduction of contributions.
- `it-estimated-tax`: the income tax acconti that share the same dates.
- `it-cross-border` and `it-impatriati`: residence and inbound workers.

## Who this applies to

- **Gestione separata, professionals.** Anyone who carries on self-employed work (lavoro autonomo) as a habitual profession, even if not their only work, must enrol (L. 335/1995 art. 2(26)). In practice this is a professional with a VAT number taxed under TUIR art. 53(1) who does not pay a cassa.
- **Professionals with a cassa are out.** Those who must pay the contributo soggettivo to an autonomous fund (D.Lgs. 509/1994 and 103/1996) do not enrol and do not fill in Quadro RR section II. So are those insured elsewhere for the activity, such as midwives in the commercianti scheme (Circolare 62/2026, para. 2.2).
- **Members of a professional register who do not pay the cassa are in.** Someone on an Albo who is not required to pay, or pays only part of, the fund's contributo soggettivo, or used a statutory option not to pay, must pay the gestione separata. INPS names engineers in Inarcassa and dottori commercialisti as examples (Circolare 62/2026, para. 2.2).
- **Collaborators and company directors** (co.co.co., amministratori, sindaci) are also in the gestione separata, but the client pays and bears two thirds (Circolare 8/2026, para. 4.1). Rates are in the table; the payroll mechanics are in `italy-payroll`.
- **Occasional self-employed work** (TUIR art. 67(1)(l)) counts only above a EUR 5,000 allowance (Circolare 62/2026, para. 2.2).
- **Amateur sports workers** use Quadro RR section III and have their own base rules (Circolare 62/2026, para. 2.2). Out of scope.
- **Artigiani and commercianti** are owners, family helpers and working partners of craft or trading businesses enrolled with INPS under L. 233/1990. Room letting (affittacamere) and third and fourth group insurance producers have no minimale: they pay the percentage on actual income plus maternity (Circolare 14/2026, para. 7).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Gestione separata, professional with a VAT number, no other compulsory cover, not a pensioner | 26.07% (25% IVS + 0.72% maternity, family, sickness and parental leave + 0.35% ISCRO) | 2026 | Circolare 8/2026, para. 2: https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/02/Circolare_15153/Allegati/16573_Circolare-numero-8-del-03-02-2026.pdf |
| Gestione separata, pensioner or insured with another compulsory scheme | 24% | 2026 | Circolare 8/2026, para. 2 (L. 247/2007 art. 1(79)) |
| Collaborators and directors, no other cover, with DIS-COLL | 35.03% (33% + 0.50% + 0.22% + 1.31%) | 2026 | Circolare 8/2026, para. 1.1 |
| Collaborators without DIS-COLL (e.g. occasional autonomous work, door-to-door sellers) | 33.72% | 2026 | Circolare 8/2026, para. 1.1 |
| Collaborators, pensioner or otherwise insured | 24% | 2026 | Circolare 8/2026, para. 1.1 |
| Split for collaborators | 1/3 worker, 2/3 client; client pays by the 16th of the next month | 2026 | Circolare 8/2026, para. 4.1 |
| Massimale (income cap), gestione separata and anyone first insured from 1996 | EUR 122,295 | 2026 | Circolare 8/2026, para. 6.1 (L. 335/1995 art. 2(18)) |
| Massimale used for the 2025 saldo paid in 2026 | EUR 120,607 | 2025 | Circolare 62/2026, para. 2.2: https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/05/Circolare_15271/Allegati/16793_Circolare-numero-62-del-27-05-2026.pdf |
| Minimale (income that credits the whole year) | EUR 18,808 | 2026 | Circolare 8/2026, para. 6.2 (L. 233/1990 art. 1(3)) |
| Contribution that credits 12 months, professional at 26.07% | EUR 4,903.25 (EUR 4,702.00 for pension) | 2026 | Circolare 8/2026, para. 6.2 |
| Contribution that credits 12 months at 24% | EUR 4,513.92 | 2026 | Circolare 8/2026, para. 6.2 |
| Occasional autonomous work: allowance before contributions | EUR 5,000 | 2026 | Circolare 62/2026, para. 2.2 |
| Rivalsa a professional may charge clients | 4% of gross fees, no cap | permanent | L. 662/1996 art. 1(212); INPS Messaggio 7751/2012 |
| Acconti for 2026: share of 2025 professional income | 80%, in two equal acconti | 2026 | Redditi PF 2026 instructions, Fascicolo 2, Appendice: https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026 |
| Surcharge for paying saldo and first acconto 30 June to 30 July | 0.40% | 2026 | Circolare 62/2026, para. 3 |
| Artigiani: rate up to EUR 56,224 / above | 24% / 25% | 2026 | Circolare 14/2026, para. 1 and 3: https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/02/Circolare_15162/Allegati/16561_Circolare-numero-14-del-09-02-2026.pdf |
| Commercianti: rate up to EUR 56,224 / above (includes 0.48% closure fund) | 24.48% / 25.48% | 2026 | Circolare 14/2026, para. 1 and 3 |
| Artigiani and commercianti minimale | EUR 18,808 | 2026 | Circolare 14/2026, para. 2 |
| Fixed yearly contribution on the minimale, artigiani | EUR 4,521.36 (EUR 4,513.92 IVS + EUR 7.44 maternity) | 2026 | Circolare 14/2026, para. 2 |
| Fixed yearly contribution on the minimale, commercianti | EUR 4,611.64 (EUR 4,604.20 IVS + EUR 7.44 maternity) | 2026 | Circolare 14/2026, para. 2 |
| Monthly fixed contribution for part years | EUR 376.78 artigiani; EUR 384.31 commercianti | 2026 | Circolare 14/2026, para. 2 |
| Artigiani and commercianti massimale, insured before 1996 / first insured from 1996 | EUR 93,707 / EUR 122,295 | 2026 | Circolare 14/2026, para. 4 |
| Artigiani and commercianti in the forfettario INPS regime | contributions cut by 35%; maternity EUR 7.44 still due in full | 2026 | L. 190/2014 art. 1(77); Circolare 14/2026, para. 8; Circolare 35/2016 |
| Over-65s already drawing an INPS pension (artigiani, commercianti) | 50% cut; not available inside the forfettario INPS regime | 2026 | Circolare 14/2026, para. 1 (L. 449/1997 art. 59(15)); L. 190/2014 art. 1(80) |
| Artigiani and commercianti first enrolled in 2025 | 50% cut of the IVS rate for 36 months from the start of activity; maternity (and the commercianti 0.48%) in full; not with the forfettario INPS regime or the over-65 cut; detail in `it-inps-artigiani-commercianti` | 2026 | L. 207/2024 art. 1(186); Circolare 14/2026, para. 1; INPS news page of 28 April 2025 on Circolare 83/2025 |
| ISCRO (income support for gestione separata professionals): income limit for a 2026 claim, on income declared for the prior year | EUR 12,749.18 | 2026 | Circolare 4/2026, para. 10 (L. 213/2023 art. 1(144)(d)): https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/01/Circolare_15147/Allegati/16539_Circolare-numero-4-del-28-01-2026.pdf |
| ISCRO monthly amount, paid for six months | 25% of the average professional income of the two years before the prior year, on a half-year basis; EUR 255.53 minimum, EUR 817.69 maximum | 2026 | Circolare 4/2026, para. 10; L. 213/2023 art. 1(147) and (148), as set out in Circolare 84/2024, para. 4 |
| Reference rate for sanzioni civili (ECB main refinancing rate), from 16 September 2026 | 2.65% | 2026 | Circolare 98/2026, para. 1 and 3 |

ISCRO is open to a gestione separata professional who is not a pensioner and has no other compulsory cover, does not receive the Assegno di inclusione, whose prior-year professional income fell below 70% of the average of the two years before, is up to date with contributions and has held the VAT number for the activity for at least three years (L. 213/2023 art. 1(144), quoted in Circolare 84/2024, para. 3). The 0.35% in the 26.07% rate funds it (Circolare 8/2026, para. 2). ISCRO months do not credit contributions (Circolare 84/2024, para. 4).

The 35% cut is only for artigiani and commercianti. L. 190/2014 art. 1(76) limits the INPS forfettario regime to people running a business, so a gestione separata professional in the regime forfettario pays the full gestione separata rate.

## The taxable base

**Gestione separata.** The rate applies to income worked out by the IRPEF rules, as shown in the return or a final assessment (L. 335/1995 art. 2(29)). Quadro RR section II, rigo RR5, takes (Circolare 62/2026, para. 2.2.1):
- Quadro RE: rigo RE23, or RE25 where prior losses are in RE24.
- Quadro RH: RH15 or RH17 for an association of professionals; RH18 column 1 for a società semplice earning professional income.
- Quadro LM, forfettari: LM34 column 2 less LM37 column 2.
- Under the concordato preventivo biennale, the agreed income, unless the professional chooses to pay on higher actual income (Circolare 62/2026, para. 1).

The figure goes in RR5 even when it is a loss. Section II must be filled in even when nothing is due (Circolare 62/2026, para. 2.2.1).

Points that change the figure:
- **Before the deduction.** The base is income before the contributions are deducted. Contributions are then deducted from total income as oneri deducibili in the year paid (TUIR art. 10(1)(e)). A forfettario deducts them from the forfettario income first, and any excess from total income (L. 190/2014 art. 1(64)).
- **Rivalsa.** The 4% rivalsa charged to clients is part of the fees, so it is already inside the base. Do not add it again. It is a right, not a duty: the professional alone owes the contribution whether or not the client pays it. Where the fee bears withholding and VAT, so does the rivalsa (Messaggio 7751/2012).
- **One cap for all gestione separata income.** Collaborator pay, occasional work above EUR 5,000 and professional income all count towards the same EUR 122,295 massimale. Once it is reached, no more is due, but Quadro RR is still filed (Circolare 62/2026, para. 2.2).
- **Months credited.** Paying at least the contribution on the minimale credits all 12 months. Below that, months are cut in proportion to the amount paid, counted from 1 January (L. 335/1995 art. 2(29)). There is no minimum payment in the gestione separata: zero income means zero contribution.

**Artigiani and commercianti.** The base is all business income declared for IRPEF for the same year, not only from the activity that triggered enrolment, less prior-year losses (Circolare 14/2026, para. 5; Circolare 62/2026, para. 2.1). A working SRL member includes their share of the company's business income. Dividends from a company where the person does not work are not included (Circolare 62/2026, para. 2.1). Family helpers can be given up to 49% of the income in total (L. 233/1990 art. 1(5)). The minimale and massimale apply to each person, not to the business (Circolare 14/2026, para. 2 and 4).

## Deadlines and filing

| What | When in 2026 | Source |
|---|---|---|
| Gestione separata: saldo 2025 and first acconto 2026 | 30 June 2026, or 30 July 2026 with the 0.40% surcharge | Circolare 62/2026, para. 3 |
| Gestione separata: second acconto 2026 | 30 November 2026 | Circolare 62/2026, para. 3 |
| Artigiani and commercianti: fixed contributions on the minimale, four instalments | 18 May 2026, 20 August 2026, 16 November 2026, 16 February 2027 | Circolare 14/2026, para. 9 |
| Artigiani and commercianti: contributions above the minimale | Saldo 2025 and first acconto 2026 on the income tax dates (30 June, or 30 July with the surcharge), second acconto 30 November | Circolare 14/2026, para. 9; Circolare 62/2026, para. 3 |
| Forfettario INPS regime: application by a business that started in 2025, or renunciation | 28 February 2026 (strict deadline) | L. 190/2014 art. 1(83); Circolare 14/2026, para. 8 |
| Redditi PF with Quadro RR, online | 31 October 2026 for 2025 income | D.P.R. 322/1998 art. 2(1) |

- **Acconti.** For the gestione separata, the two equal acconti for 2026 total the 2026 rate on 80% of the 2025 professional income, within the 2026 massimale (Redditi PF 2026 instructions, Appendice). For artigiani and commercianti, the two equal acconti apply the 2026 rates to the 2025 business income above the 2026 minimale (same Appendice). The acconti paid are subtracted in Quadro RR to give the saldo.
- **First year.** A new professional tells INPS the type of activity from its start date (L. 335/1995 art. 2(27)) and enrols through the Cassetto previdenziale per liberi professionisti (Circolare 62/2026). With no professional income in the prior year, 80% of nil is nil, so no acconto is due and the first year is paid as saldo the next June (Redditi PF 2026 instructions, Appendice).
- **Instalments.** The saldo and the first acconto can be paid in monthly instalments. The first falls on the saldo date, the rest on the 16th of each month, all by 16 December 2026 (D.Lgs. 241/1997 art. 20(1), as replaced by D.Lgs. 33/2025; Circolare 62/2026, para. 4). The second acconto cannot be split. For artigiani and commercianti only the part above the minimale can be split, never the fixed contributions.
- **F24 causali** (Circolare 62/2026, para. 3 and 4): PXX (no other cover) or P10 (pensioner or otherwise insured), with R for instalments (PXXR, P10R). Interest and the 0.40% surcharge go on a separate line: DPPI for the gestione separata, API for artigiani, CPI for commercianti. Artigiani and commercianti use AP/APR and CP/CPR with the INPS codeline shown in the Cassetto previdenziale.
- **Bank statements.** An F24 debit ("DELEGA F24", "AGENZIA DELLE ENTRATE") can mix IRPEF, VAT, local surcharges and INPS on one line. Do not book it as INPS without the F24 receipt. A "RIVALSA" credit from a client is income, not a contribution. A DPPI line is interest, not a contribution.
- **Overpayments.** An acconto paid in excess is set against the next year's payments, or refunded on request by the saldo date of the year it relates to (L. 335/1995 art. 2(30)).

## Penalties and interest

Late or missing gestione separata contributions bear the same sanzioni civili as commercianti (L. 335/1995 art. 2(30)), which are those of L. 388/2000 art. 116(8) (lettera b-bis for the 50% case):

| Case | Sanzione civile, per year | Cap |
|---|---|---|
| Late or missing payment of an amount shown in the return (omissione) | Official reference rate + 5.5 points | 40% of the contributions |
| Same, paid in one go within 120 days, before any INPS request | Official reference rate only (no 5.5 points) | 40% |
| Evasion: return not filed or untrue, with intent not to pay | 30% | 60% |
| Evasion self-reported within 12 months, before any INPS request, paid within 30 days | Official reference rate + 5.5 points | 40% |
| Same, paid within 90 days | Official reference rate + 7.5 points | 40% |
| Debt found by INPS itself or at an inspection, paid in one go within 30 days of the notice | Half the omissione or evasion sanction above | as above |

With the reference rate at 2.65% from 16 September 2026, the omissione sanction is 8.15% a year, 2.65% if paid within 120 days, and the self-reported evasion rates are 8.15% (30 days) and 10.15% (90 days) (Circolare 98/2026, para. 3). The reference rate is the ECB main refinancing rate and moves with it (Circolare 98/2026, note 1). An INPS instalment plan (rateazione) for contribution debts requested from 16 September 2026 bears 4.65% a year (Circolare 98/2026, para. 2).

Once the cap is reached and the debt is still unpaid, interest runs at the late-payment rate of D.P.R. 602/1973 art. 30 (L. 388/2000 art. 116(9)). Where the delay came from genuinely conflicting case law or rulings on whether contributions were due, only legal interest is due if paid by the deadline INPS sets (art. 116(10)). Paying the saldo and first acconto between 30 June and 30 July is not late if the 0.40% surcharge is added (Circolare 62/2026, para. 3).

**Definizione agevolata 2026.** INPS contribution debts handed to the collection agent from 1 January 2000 to 31 December 2023 can be cleared by paying the capital and collection costs only, without sanctions, somme aggiuntive, late interest or the collection fee. Debts from an INPS assessment (accertamento) are excluded. The application was due by 30 April 2026. Payment is in one go by 31 July 2026 or in up to 54 bimonthly instalments, with 3% yearly interest from 1 August 2026 (L. 199/2025 art. 1(82) to (86)).

## Cross-border points

- **EU posting.** A self-employed person who usually works in Italy can work temporarily in another EU country for up to 24 months doing similar work and stay insured with INPS. They ask INPS for form A1 before leaving (INPS, "Certificato di distacco"; Reg. (EC) 883/2004 art. 12).
- **Coming to Italy.** Someone who starts a profession in Italy tells INPS from the start date (L. 335/1995 art. 2(27)). Residence and the impatriati regime are in `it-cross-border` and `it-impatriati`.
- **Contributions before 1996.** The EUR 122,295 cap applies to people with no contributions before 1996. An artigiano or commerciante with contributions at 31 December 1995 uses EUR 93,707 instead (Circolare 14/2026, para. 4).

## Worked examples

### Example 1: consultant in the gestione separata, regime ordinario

A self-employed IT consultant has no other pension cover and is not a pensioner. Rigo RE23 shows 2026 income of EUR 40,000 and 2025 income of EUR 35,000. The 2026 contribution is 26.07% of EUR 40,000, which is EUR 10,428.00, well below the cap. The 2026 acconti are 26.07% of 80% of EUR 35,000, which is EUR 7,299.60, paid as EUR 3,649.80 on 30 June and EUR 3,649.80 on 30 November 2026. The saldo for 2026, paid in June 2027, is EUR 10,428.00 less EUR 7,299.60, so EUR 3,128.40. Income is above the EUR 18,808 minimale, so all 12 months are credited.

```oa-check
name: Gestione separata professional, 2026 income EUR 40,000, 2025 income EUR 35,000
inputs:
  income_2026: 40000
  income_2025: 35000
  rate: 0.2607
  acconto_share: 0.80
  massimale: 122295
steps:
  - contribution_2026: round(min(income_2026, massimale) * rate, 2)
  - acconti_total: round(min(income_2025 * acconto_share, massimale) * rate, 2)
  - each_acconto: round(acconti_total / 2, 2)
  - saldo_june_2027: contribution_2026 - acconti_total
expected:
  contribution_2026: 10428.00
  acconti_total: 7299.60
  each_acconto: 3649.80
  saldo_june_2027: 3128.40
```

### Example 2: professional who is also a company director, above the cap

A designer with a VAT number and no other cover earns professional income of EUR 110,000 in 2026. She is also a director of a client company, which has charged EUR 30,000 of her director's fees to the gestione separata. Both incomes share the EUR 122,295 massimale. Only EUR 92,295 of her professional income is still under the cap, so her own contribution is 26.07% of EUR 92,295, which is EUR 24,061.31. Without the director's fees she would have paid 26.07% of EUR 110,000, which is EUR 28,677.00. Quadro RR section II is still filed with the full income.

```oa-check
name: Professional plus director's fees in the gestione separata, 2026 cap
inputs:
  professional_income: 110000
  director_fees: 30000
  massimale: 122295
  rate: 0.2607
steps:
  - room_under_cap: max(massimale - director_fees, 0)
  - professional_base: min(professional_income, room_under_cap)
  - contribution: round(professional_base * rate, 2)
  - contribution_without_fees: round(min(professional_income, massimale) * rate, 2)
  - saved_by_cap: contribution_without_fees - contribution
expected:
  room_under_cap: 92295
  professional_base: 92295
  contribution: 24061.31
  contribution_without_fees: 28677.00
  saved_by_cap: 4615.69
```

## Ask the client first

- Do you pay the contributo soggettivo to a professional fund (cassa), in full, in part, or not at all?
- Are you already a pensioner, or insured with another compulsory scheme, for example as an employee?
- Are you a professional, an artigiano or a commerciante, and are you in the regime forfettario? If you run a business, did you join the INPS forfettario regime?
- Did you have other gestione separata income in the year (director's fees, co.co.co., occasional work above EUR 5,000)?
- Did you charge the 4% rivalsa, and is it inside the fees you declared?
- When did you start, and are you enrolled with INPS? Do you have Italian contributions from before 1996?

## Sources

| Source | URL | Read on |
|---|---|---|
| INPS Circolare n. 8 of 3 February 2026, gestione separata rates, massimale and minimale 2026 | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/02/Circolare_15153/Allegati/16573_Circolare-numero-8-del-03-02-2026.pdf | 2026-10-24 |
| INPS Circolare n. 14 of 9 February 2026, artigiani and commercianti 2026 | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/02/Circolare_15162/Allegati/16561_Circolare-numero-14-del-09-02-2026.pdf | 2026-10-24 |
| INPS Circolare n. 62 of 27 May 2026, Quadro RR, saldo 2025 and acconti 2026 | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/05/Circolare_15271/Allegati/16793_Circolare-numero-62-del-27-05-2026.pdf | 2026-10-24 |
| INPS Messaggio n. 7751 of 7 May 2012, rivalsa | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2012/05/Circolare_10983/Allegati/7928_Messaggio-numero-7751-del-07-05-2012.pdf | 2026-10-24 |
| INPS Circolare n. 35 of 19 February 2016, forfettari INPS regime (35% cut, maternity) | https://www.inps.it/bussola/VisualizzaDoc.aspx?sVirtualURL=%2FCircolari%2FCircolare+numero+35+del+19-02-2016.htm | 2026-10-24 |
| INPS, "Certificato di distacco del lavoratore in paesi Ue" | https://www.inps.it/it/it/dettaglio-approfondimento.schede-informative.certificato-di-distacco-del-lavoratore-in-paesi-ue.html | 2026-10-24 |
| L. 335/1995 art. 2 (c. 18 massimale, c. 26 to 30 gestione separata) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1995-08-08;335~art2!vig=2026-10-24 | 2026-10-24 |
| L. 233/1990 art. 1 (artigiani and commercianti: minimale, massimale, 49%) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1990-08-02;233~art1!vig=2026-10-24 | 2026-10-24 |
| L. 190/2014 art. 1 (c. 64 deduction, c. 76 to 84 forfettari INPS regime) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2014-12-23;190~art1 | 2026-10-24 |
| L. 662/1996 art. 1 c. 212 (rivalsa 4%) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:1996-12-23;662~art1!vig=2026-10-24 | 2026-10-24 |
| INPS Circolare n. 98 of 11 September 2026, reference rate, sanzioni civili and rateazione interest from 16 September 2026 | https://www.inps.it/it/it/inps-comunica/atti/circolari-messaggi-e-normativa/dettaglio.circolari-e-messaggi.2026.09.circolare-numero-98-del-11-09-2026_15369.html | 2026-10-24 |
| INPS Circolare n. 4 of 28 January 2026, ISCRO income limit and amounts 2026 | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2026/01/Circolare_15147/Allegati/16539_Circolare-numero-4-del-28-01-2026.pdf | 2026-10-24 |
| INPS Circolare n. 84 of 23 July 2024, ISCRO conditions and calculation (L. 213/2023 art. 1 c. 142 to 155) | https://www.inps.it/content/dam/inps-site/it/scorporati/circolari-e-messaggi/2024/07/Circolare_14640/Allegati/15257_Circolare-numero-84-del-23-07-2024.pdf | 2026-10-24 |
| INPS news page, 28 April 2025, 50% cut for artigiani and commercianti first enrolled in 2025 (Circolare 83/2025) | https://www.inps.it/it/it/inps-comunica/notizie/dettaglio-news-page.news.2025.04.artigiani-e-commercianti-riduzione-contributiva-ai-nuovi-iscritti.html | 2026-10-24 |
| L. 388/2000 art. 116 c. 8 to 10 (sanzioni civili) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2000-12-23;388~art116!vig=2026-10-24 | 2026-10-24 |
| L. 199/2025 art. 1 c. 82 to 86 (definizione agevolata 2026) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199 | 2026-10-24 |
| TUIR art. 10 (deduction of compulsory contributions) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art10 | 2026-10-24 |
| D.P.R. 322/1998 art. 2 (return deadline) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1998-07-22;322~art2 | 2026-10-24 |
| Agenzia delle Entrate, Redditi PF 2026 instructions, Fascicolo 2 (Quadro RR, INPS acconti) | https://www.agenziaentrate.gov.it/portale/documents/d/guest/pf2_istruzioni_2026_agg-13-05-2026 | 2026-10-24 |

Not yet confirmed: how INPS splits a sanzione civile across the 2026 periods before 16 September 2026, when the reference rate was lower (the ECB rate was 2.15% to 16 June and 2.40% from 17 June 2026); the text of L. 207/2024 art. 1(186) and L. 213/2023 art. 1(142) to (155) on Normattiva (both read through INPS documents only, as the article page did not load past its first commi); whether any provision of L. 199/2025 after comma 100 changes self-employed INPS contributions (the February 2026 INPS circulars report none); the rules for amateur sports workers (Quadro RR section III); Reg. (EC) 883/2004 arts. 11 and 13 on which country insures a person working in several states (EUR-Lex blocked scripts); the historic F24 code DPP from the earlier version; the professional fund rates (see `it-inps-artigiani-commercianti`); refunds of excess contributions beyond L. 335/1995 art. 2(30); suspension of contributions for illness or injury; the Quadro RP line number for the deduction in the 2027 form.

> Contributed by OpenAccountants.

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
