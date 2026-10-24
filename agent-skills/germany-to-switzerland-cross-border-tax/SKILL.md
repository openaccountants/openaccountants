---
name: germany-to-switzerland-cross-border-tax
description: "Use this skill for a German resident who works in Switzerland, or a German who moves there, tax year 2026. Covers the frontier commuter (Grenzgänger) rule in art. 15a of the Germany-Switzerland treaty: Swiss withholding capped at 4.5% of gross pay with a Gre-1 residence certificate, the 60 non-return days test, the new 20% regular-return test and the 2026 protocol, home office days, part-year and part-time limits, and the German credit of the Swiss tax under § 36 EStG. Also covers weekly stayers, Swiss company managers (art. 15(4)), the five-year treaty tail for Germans who move (art. 4(4)), lump-sum taxpayers (art. 4(6)) and the German rules that follow a mover. Trigger on: Grenzgänger Schweiz, Nichtrückkehrtage, Gre-1, Gre-3, Wochenaufenthalter, Quellensteuer 4,5 %, moving to Switzerland. Out of scope: exit tax detail (leaving-germany-exit-tax), the Swiss side (ch-cross-border), German employees' deductions (de-employee-income-tax), dividends paid out of Germany (de-treaty-withholdin"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/germany-to-switzerland-cross-border-tax"
  jurisdiction: "DE"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Michael Cutajar and the OpenAccountants team"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Germany and Switzerland: frontier commuters, weekly stayers and movers, tax year 2026

This skill works out which country taxes the pay of a person who lives on one side of the German-Swiss border and works on the other, and how Germany taxes the result. It also lists the German rules that follow a German who moves to Switzerland. It works from the treaty of 11 August 1971 as amended by the protocol of 21 August 2023. That protocol came into force on 27 November 2025 and applies from 1 January 2026.

See also, and do not repeat here:

- **ch-cross-border** (Switzerland pack): Swiss residence, tax at source, the CHF 120,000 ordinary assessment threshold, lump-sum taxation, Swiss withholding tax refunds.
- **leaving-germany-exit-tax**: the § 6 AStG exit tax on shares and the § 2 AStG extended limited liability, with the full method.
- **de-non-resident-tax**: a person who has left Germany and still has German income.
- **de-partners-and-part-year**: the year of moving out, with the progression clause.
- **de-employee-income-tax**: the 2026 tariff, Werbungskosten and special expenses of an employee.
- **de-treaty-withholding-rates**: German withholding on dividends, interest and royalties paid to Swiss residents.

## Who this applies to

Three groups, with different results. Classify the client first and test again after any change of job, home office pattern, flat or family home.

**1. Frontier commuter (Grenzgänger), art. 15a.** A person resident in one state whose place of work is in the other state and who regularly returns from there to their home. The pay is taxed in the state of residence. The work state may withhold tax, capped at 4.5% of gross pay if the person shows an official residence certificate from their home tax office (art. 15a(1)).

- **Place of work** is normally where the employee is integrated into the employer's business. For drivers and field staff, days away count as business trips when counting non-return days. Where the contract names several sites or none, the place of work is where the work is mostly done (protocol no. 5(a)).
- **Regular return, new from 2026.** There is a regular return only if the employee travels from home to the place of work and back on at least 20% of the agreed working days in the calendar year (protocol no. 5(b)). Agreed working days are those in the contract. Protocol no. 5(d) takes leave and sick days out of the working days for the 60-day test; the protocol does not say whether they also come out of the base for the 20% test, so check both bases (Example 2 passes and fails the same way on either).
- **The 60 non-return days test.** A person who does not return home after every working day keeps commuter status unless, when employed for the whole calendar year, they fail to return home on more than 60 working days because of their work (art. 15a(2)).
- **What counts as a non-return day.** A day on which returning home was not possible or not reasonable for work reasons, and the person in fact did not return. Return is not reasonable when the shortest road distance one way is over 100 km by car, or the fastest public transport one way at usual commuting times takes over 1.5 hours; the means of transport mostly used decides (protocol no. 5(e), which takes over the consultation agreement of 12 October 2018). One-day business trips in either treaty state are not non-return days; one-day trips to a third country always are (protocol no. 5(f)). Weekend and holiday days on a multi-day business trip paid by the employer, and days off worked on the employer's express order, are working days (protocol no. 5(d)). Shift work spread over several days does not break the regular return; breaks under four hours do not end the working day (protocol no. 5(c)).
- **Home office days.** Under the consultation agreement of 15 and 18 July 2022 (BMF letter of 26 July 2022), a working day spent entirely at home in the residence state is not a non-return day. That agreement was made under the treaty as amended in 2010; whether it still applies under the 2026 protocol is not confirmed (see the end of this skill). Either way, a home office day is not a day on which the person travels to the place of work and back, so from 2026 it counts against the 20% regular-return test.
- **Part-year employment.** The allowed non-return days are 5 per full month and 1 per full week of employment in the other state (protocol no. 5(g)).
- **Part-time employment.** Someone who works some hours on every usual working day keeps the 60 days. Someone who works only on some days gets 60 cut in proportion: contractual working days over the usual full-time working days, taken as 240 for a five-day week and 280 for a six-day week if the contract is silent. Leave is not deducted from either figure (protocol no. 5(i)).
- **Several employers in the work state.** Status is judged once for all jobs in the year; non-return days from all jobs are added (protocol no. 5(h)).

The rule works both ways. For a Swiss resident who commutes to a German employer, the German employer withholds at most 4.5% and Switzerland taxes the pay, cutting the gross pay by one fifth when computing its tax base (art. 15a(3)(b)).

**2. Weekly stayer (Wochenaufenthalter) and others who lose commuter status.** A German resident with a weekday room in Switzerland who stays there on more than 60 working days is not a commuter. Art. 15 applies instead: Switzerland may tax pay for work done in Switzerland. Germany exempts that pay but uses it to set the rate on other income (art. 24(1) no. 1(c) and no. 2; § 32b(1) no. 3 EStG). Germany grants the exemption only if the person proves that Switzerland taxed the pay and the tax was paid, or that Switzerland waived its right (§ 50d(8) EStG). Pay for workdays spent outside Switzerland stays taxable in Germany.

A weekday flat does not by itself move the person's residence. If the person is resident in both states under domestic law, art. 4(2) decides: permanent home first, then centre of vital interests (closer personal and economic ties), then habitual abode, then nationality. A family home in Germany usually points to Germany.

**3. Managers of Swiss companies, art. 15(4).** A German resident who is a board member (Vorstandsmitglied), director, managing director (Geschäftsführer) or Prokurist of a Swiss company can be taxed in Switzerland on that pay, unless their duties are limited to work outside Switzerland. Art. 15a takes priority, so a manager who meets the commuter test is a commuter. The German and Swiss authorities agreed on 6 April 2023 to apply art. 15(4) also to people registered with a signature right and no stated function, and to unregistered people with powers at least equal to a Prokura. That agreement now runs to 31 December 2027 (BMF letters of 25 April 2023 and 16 October 2025).

**4. Germans who move to Switzerland.** Moving ends German unlimited liability. Four German rules can follow:

- **Treaty tail, art. 4(4).** A Swiss resident without Swiss nationality who was fully taxable in Germany for at least five years in total remains taxable in Germany on German-source income in the year their German liability ended and the five following years. Germany credits the Swiss tax on that income. This does not apply to someone who moved to take up genuine employment with an employer in which they have no substantial interest. A German employer may not apply the 4.5% cap to such a person while art. 4(4) applies (Gre-1 note 3).
- **Exit tax, § 6 AStG.** Shares of at least 1% held in the last five years, after at least seven years of full German liability in the last twelve: deemed sale on leaving, seven yearly instalments on application. Method in leaving-germany-exit-tax.
- **Extended limited liability, § 2 AStG.** A German citizen who moves to a low-tax country and keeps substantial German economic interests stays taxable on more German income for ten years. Whether the Swiss canton counts as low-tax is a computation; see leaving-germany-exit-tax.
- **Gift and inheritance tax, § 2(1) no. 1(b) ErbStG.** A German national who has lived abroad for no more than five years without a German home still counts as a resident for gift and inheritance tax.

**Lump-sum taxpayers, art. 4(6).** A person is not treated as resident in a treaty state if that state does not tax them, at the generally applied taxes, on all their income from the other state that is normally taxable there. A lump-sum (expenditure-based) taxpayer in Switzerland who is not taxed on German-source income at ordinary rates therefore loses treaty protection. The Swiss rules on the lump sum are in ch-cross-border.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Swiss tax on a German-resident commuter's pay | At most 4.5% of gross pay, with a Gre-1 residence certificate; the lower Swiss tariff tax if that is less | 2026 | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Schweiz/2026-07-15-Schweiz-DBA-Bekanntmachung-Neufassung.pdf?__blob=publicationFile&v=2 (art. 15a(1)); Gre-1 note 6 |
| Non-return days allowed, full year, full time | 60 working days | 2026 | Same, art. 15a(2) |
| Non-return days allowed, part year | 5 per full month plus 1 per full week of employment | 2026 | Same, protocol no. 5(g) |
| Non-return days allowed, part time on some days only | 60 × contractual working days / usual full-time days (240 for a five-day week, 280 for a six-day week, if not in the contract) | 2026 | Same, protocol no. 5(i) |
| Regular return | Commute home to work and back on at least 20% of agreed working days | From 2026 | Same, protocol no. 5(b) |
| Return not reasonable | Over 100 km one way by road, or over 1.5 hours one way by public transport at usual times | 2026 | Same, protocol no. 5(e) |
| German credit of the Swiss commuter tax | In full, like German withholding, under § 36 EStG, not under § 34c; also counted when setting prepayments | 2026 | Same, art. 15a(3)(a); https://www.gesetze-im-internet.de/estg/__36.html |
| Swiss resident commuting to Germany | German withholding at most 4.5%; Swiss tax base is gross pay less one fifth | 2026 | Same, art. 15a(1), (3)(b) |
| Treaty tail for Germans who move | Year of departure plus five years | 2026 | Same, art. 4(4) |
| Prior German liability for the treaty tail | At least five years in total | 2026 | Same, art. 4(4) |
| German return required, single, no German wage tax withheld | Total income above EUR 12,348 (EUR 24,696 for a married couple assessed jointly) | 2026 | https://www.gesetze-im-internet.de/estdv_1955/__56.html; https://www.gesetze-im-internet.de/estg/__32a.html |
| 2026 tariff, zone 3 (taxable EUR 17,800 to 69,878) | (173.10 × z + 2,397) × z + 1,034.87, z = (taxable − 17,799) / 10,000, result rounded down | 2026 | https://www.gesetze-im-internet.de/estg/__32a.html |
| Prepayments | 10 March, 10 June, 10 September, 10 December; set only if at least EUR 400 a year and EUR 100 a date | 2026 | https://www.gesetze-im-internet.de/estg/__37.html |
| Art. 15(4) consultation agreement | Applies to 31 December 2027 | 2026 | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Schweiz/2025-10-16-weiterfuehrung-konsultationsvereinb.pdf?__blob=publicationFile&v=3 |
| Swiss mandatory ordinary assessment of source-taxed pay | Gross employment income of at least CHF 120,000 | 2026 | See ch-cross-border (QStV art. 9) |

## The taxable base

### Step 1: is the person a commuter?

1. Residence: where does the person live under domestic law, and if both, where under art. 4(2)?
2. Place of work in the other state (protocol no. 5(a))?
3. Regular return: commuting days ÷ agreed working days, net of leave and sick days, at least 20%?
4. Non-return days: count only days that meet protocol no. 5(e) and (f), and compare with 60 or the reduced limit for part-year or part-time work. Add days from all jobs in the work state.
5. If both tests pass, art. 15a applies to the whole year's pay from that employment. If either fails, go to Step 3.

The employer certifies the non-return days on form Gre-3, stamped by the tax office for the place of work (protocol no. 5(j)). Where the employer finds at the year end, or when the job ends, that commuter status fails because of the non-return days, it sends the Gre-3 to the tax authority that collects the withholding, if possible within three months (Gre-3 note 2). The employee must give the employer the facts needed (protocol no. 5(j)).

### Step 2: the German assessment of a commuter (German resident)

- All the pay, including pay for days worked in Switzerland, is German employment income. Compute it as for any employee (de-employee-income-tax): gross pay less Werbungskosten or the employee lump sum, then special expenses.
- The 2026 tariff applies to taxable income, with the solidarity surcharge at 5.5% above the EUR 20,350 threshold of income tax (see de-employee-income-tax).
- The Swiss tax withheld, up to 4.5% of gross, is credited against German income tax as if it were German withholding (art. 15a(3)(a); § 36(2) no. 2 EStG). It is not capped under § 34c. The employer's certificate of gross pay and Swiss tax is the evidence (protocol no. 6).
- The Swiss employer withholds the lower of 4.5% and the Swiss tariff tax (Gre-1 note 6(b)). The commuter gives the employer the Gre-1 when starting work and when changing employer; the German tax office then renews it each year without a new application (Gre-1 notes 2 and 7).

### Step 3: when commuter status fails

- Pay for work days in Switzerland: Swiss tax under art. 15; exempt in Germany with progression (art. 24(1) no. 1(c), no. 2; § 32b EStG), only with proof of Swiss tax paid (§ 50d(8)).
- Pay for days worked in Germany or third countries: taxable in Germany.
- If the employer finds during the year that status will fail, it must collect the full Swiss tax (Gre-1 note 4).

### Step 4: Swiss occupational pensions of former commuters

A former commuter who worked in the Swiss public service and draws a second-pillar pension keeps the Germany-first rule: the Swiss pension fund withholds at most 4.5% on a Gre-4 certificate (Gre-5 for survivors), and Germany credits it in proportion to the taxable share of the pension (BMF letters of 8 February 2018 and 7 December 2023; protocol no. 9).

## Deadlines and filing

| Step | Rule |
|---|---|
| Gre-1 residence certificate | Apply to the German tax office when starting work and when changing employer; valid for one year and renewed without a new application |
| Gre-3 non-return days | Where status fails: employer certifies, the tax office for the place of work stamps; if possible within three months after the year end or the end of the job |
| German return, 2026 | Required when total income exceeds EUR 12,348 (single) and no German wage tax was withheld (§ 56 EStDV). Due 31 July 2027, a Saturday, so Monday 2 August 2027; with a tax adviser 29 February 2028 (§§ 108, 149 AO; see de-non-resident-tax) |
| Prepayments | Quarterly on 10 March, 10 June, 10 September and 10 December; the 4.5% Swiss tax is counted (art. 15a(3)(a); § 37 EStG) |
| Weekly stayer | Swiss tax return or tax at source in Switzerland (see ch-cross-border); German return showing the exempt pay for progression, with proof of Swiss tax |

## Penalties and interest

- **Late filing surcharge (§ 152 AO).** 0.25% per started month of the assessed tax less prepayments and credited withholding, at least EUR 25 per month, at most EUR 25,000. Compulsory if the 2026 return is not filed by 29 February 2028 and tax is due.
- **Interest on assessed tax (§ 233a, § 238 AO).** 0.15% per full month on the balance, from 1 April 2028 for 2026.
- **Late payment (§ 240 AO).** 1% per started month on overdue tax, rounded down to the nearest EUR 50.
- **Lost commuter status found late.** The employer must collect the Swiss tax not withheld (Gre-1 note 4). In Germany the exemption under art. 24 is refused until the Swiss tax is shown paid (§ 50d(8) EStG), so the return is assessed with the pay taxed and changed later.

Figures and sections as in de-non-resident-tax, which read them on 2026-10-23.

## Cross-border points

- **Two treaty layers from 2026.** The protocol of 21 August 2023 rewrote the commuter points into the treaty protocol (nos. 5 to 7) and ended the 1991 negotiation record (protocol no. 7). The 20% regular-return test is the main new condition.
- **Swiss withholding for German residents, dividends, interest.** Switzerland withholds 35% Verrechnungssteuer; under art. 10 a German resident can recover down to 15% (0% for a German company holding at least 10% for 365 days); interest is taxable only in Germany (art. 11). Refund route in ch-cross-border.
- **German withholding on payments to Swiss residents.** See de-treaty-withholding-rates.
- **Social security.** EU-Switzerland coordination decides where contributions are due, separately from tax. Not covered here.
- **Inheritance tax.** A separate Germany-Switzerland inheritance tax treaty of 1978 exists. Not covered here.
- **Currency.** Swiss pay is converted to euro for the German return. The conversion rule is not set out here.

## Worked examples

### Example 1: commuter from Lörrach to Basel, full year 2026

Lena lives in Lörrach and works full time for a Basel employer all of 2026. She commutes every working day except 12 nights away on multi-day business trips in Switzerland and 20 home office days at home. She is single and has no other income. Her gross pay is EUR 80,000 (already converted). After Werbungskosten and special expenses her taxable income is EUR 60,000 (computed as in de-employee-income-tax). She gave her employer a Gre-1. (Invented case.)

- Non-return days: 12, below 60. Home office days do not count.
- Regular return: she commutes on almost every working day, far above 20%.
- She is a commuter. Swiss tax at source: 4.5% × 80,000 = EUR 3,600.
- German tax on EUR 60,000: z = (60,000 − 17,799) / 10,000 = 4.2201; tax = (173.10 × 4.2201 + 2,397) × 4.2201 + 1,034.87 = 14,233.23, rounded down EUR 14,233. Below EUR 20,350, so no solidarity surcharge.
- Credit of the Swiss tax: EUR 3,600 in full (§ 36). German tax still to pay: EUR 10,633.
- Total tax on the pay: EUR 3,600 in Switzerland plus EUR 10,633 in Germany, EUR 14,233.

```oa-check
name: DE-CH commuter 2026, 4.5% Swiss tax credited under § 36
inputs:
  gross_pay: 80000
  taxable_income: 60000
  swiss_cap_rate: 0.045
steps:
  - swiss_tax: gross_pay * swiss_cap_rate
  - z: (taxable_income - 17799) / 10000
  - german_tax: floor((173.10 * z + 2397) * z + 1034.87)
  - german_balance: german_tax - swiss_tax
  - total: swiss_tax + german_balance
expected:
  swiss_tax: 3600
  german_tax: 14233
  german_balance: 10633
  total: 14233
```

### Example 2: part-time commuter with home office and overnight trips

Jonas lives in Konstanz and works three days a week for a Zurich employer all of 2026. His contract does not state the usual full-time days, so a five-day week gives 240. His contractual days are 3/5 of 240 = 144. He takes 12 days of leave, so he has 132 working days. He works 30 of them at home in Konstanz and stays overnight in Switzerland on 30 days because of evening client work more than 100 km from home. (Invented case.)

- Non-return limit: 60 × 144 / 240 = 36 days (leave is not deducted for this ratio). His 30 days are within it.
- Regular return: commuting days = 132 − 30 − 30 = 72. 20% of 132 = 26.4. 72 is above, so he passes. On the contract days without deducting leave (144) the threshold is 28.8; he still passes.
- He is a commuter: Switzerland withholds at most 4.5% and Germany taxes the pay and credits it, as in Example 1.
- Edge case: if he had worked 80 days at home, his commuting days would be 132 − 80 − 30 = 22, below 26.4 (and below 28.8). He would then fail the regular-return test from 2026 even though the home office days are not non-return days. Art. 15 would then apply: Switzerland taxes pay for his Swiss work days and Germany exempts it with progression, on proof of Swiss tax.

```oa-check
name: DE-CH part-time commuter 2026, non-return limit and 20% return test
inputs:
  usual_days: 240
  days_per_week: 3
  leave_days: 12
  home_office_days: 30
  nonreturn_days: 30
  home_office_alt: 80
steps:
  - contract_days: usual_days * days_per_week / 5
  - nonreturn_limit: 60 * contract_days / usual_days
  - working_days: contract_days - leave_days
  - commute_days: working_days - home_office_days - nonreturn_days
  - min_commute: working_days * 0.20
  - margin_nonreturn: nonreturn_limit - nonreturn_days
  - margin_return: commute_days - min_commute
  - commute_alt: working_days - home_office_alt - nonreturn_days
  - margin_alt: commute_alt - min_commute
expected:
  contract_days: 144
  nonreturn_limit: 36
  working_days: 132
  commute_days: 72
  min_commute: 26.4
  margin_nonreturn: 6
  margin_return: 45.6
  commute_alt: 22
  margin_alt: -4.4
```

## Ask the client first

1. Where is your home, where does your family live, and do you keep a room or flat in the other country?
2. Your contract: employer, place of work, working days per week, and any second job in the same country.
3. For 2026: days worked at home, days you stayed overnight for work (with distance or travel time), days on trips to third countries, leave and sick days.
4. Are you a board member, managing director or Prokurist of the Swiss company, or registered with a signature right?
5. Did you live in Germany before moving, for how many years, and do you hold 1% or more of any company?
6. Do you have the Gre-1 for 2026, and will your employer issue the Gre-3 and a certificate of pay and Swiss tax?

## Sources

| Source | URL | Read on |
|---|---|---|
| BMF, consolidated Germany-Switzerland treaty as in force from 27 November 2025 (arts. 4, 15, 15a, 24; protocol nos. 5 to 7, 9) | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Schweiz/2026-07-15-Schweiz-DBA-Bekanntmachung-Neufassung.pdf?__blob=publicationFile&v=2 | 2026-10-23 |
| BMF, entry into force of the protocol of 21 August 2023 (27 November 2025) | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Schweiz/2025-12-23-Schweiz-DBA-Bekanntmachung-Protokoll.pdf?__blob=publicationFile&v=3 | 2026-10-23 |
| Fedlex, treaty SR 0.672.913.62, version of 27 November 2025 (application from 2026, art. 23(2) of the protocol) | https://www.fedlex.admin.ch/eli/cc/1972/3075_3128_2910/de | 2026-10-23 |
| BMF letter of 26 July 2022, home office days of commuters | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Schweiz/2022-07-26-konsultationsvereinbarung-betreffend-der-grenzgaengerregelung-artikel-15a-des-deutsch-schweizerischen-DBS.pdf?__blob=publicationFile&v=2 | 2026-10-23 |
| BMF letter of 25 October 2018, non-return for work reasons (100 km, 1.5 hours) | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Schweiz/2018-10-25-nichtrueckkehr-eines-grenzgaengers-aufgrund-der-arbeitsausuebung-nach-artikel-15a-asbsatz-2-DBA-Schweiz.pdf?__blob=publicationFile&v=1 | 2026-10-23 |
| BMF letter of 7 December 2023, forms Gre-1, Gre-3, Gre-4, Gre-5 with notes | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Schweiz/2023-12-07-ansaessigkeitsbescheinigungen-und-arbeitgeberbescheinigung-ueber-die-nichtrueckkehr.pdf?__blob=publicationFile&v=3 | 2026-10-23 |
| BMF letter of 8 February 2018, credit of Swiss tax on second-pillar pensions | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Schweiz/2018-02-08-DBA-Schweiz-Abzugsteuer-Grenzgaenger.pdf?__blob=publicationFile&v=1 | 2026-10-23 |
| BMF letter of 25 April 2023, art. 15(4) managers | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Schweiz/2023-04-25-konsultationsvereinbarung-zu-artikel-15-absatz-4-des-deutsch-schweizerischen-DBA.pdf?__blob=publicationFile&v=1 | 2026-10-23 |
| BMF letter of 16 October 2025, art. 15(4) agreement continued to 2027 | https://www.bundesfinanzministerium.de/Content/DE/Standardartikel/Themen/Steuern/Internationales_Steuerrecht/Staatenbezogene_Informationen/Laender_A_Z/Schweiz/2025-10-16-weiterfuehrung-konsultationsvereinb.pdf?__blob=publicationFile&v=3 | 2026-10-23 |
| EStG § 32a (2026 tariff) | https://www.gesetze-im-internet.de/estg/__32a.html | 2026-10-23 |
| EStG § 32b (progression) | https://www.gesetze-im-internet.de/estg/__32b.html | 2026-10-23 |
| EStG § 36 (credit of withholding) | https://www.gesetze-im-internet.de/estg/__36.html | 2026-10-23 |
| EStG § 37 (prepayments) | https://www.gesetze-im-internet.de/estg/__37.html | 2026-10-23 |
| EStG § 50d (proof for exempt employment income) | https://www.gesetze-im-internet.de/estg/__50d.html | 2026-10-23 |
| EStDV § 56 (duty to file) | https://www.gesetze-im-internet.de/estdv_1955/__56.html | 2026-10-23 |
| ErbStG § 2 (five-year rule for German nationals) | https://www.gesetze-im-internet.de/erbstg_1974/__2.html | 2026-10-23 |
| AO §§ 152, 233a, 238, 240 | https://www.gesetze-im-internet.de/ao_1977/__152.html | 2026-10-23 |

Not yet confirmed: whether the home office consultation agreement of July 2022 still applies under the 2026 protocol text (it was made under the treaty as amended in 2010, and the new protocol no. 5 does not mention home office days; the 2023 Gre-1 notes still cite it); whether the BMF has issued an introductory letter on the 2026 commuter rules (none found in a search of bundesfinanzministerium.de on 2026-10-23); whether leave and sick days come out of the base for the 20% test; how the German implementing ordinance KonsVerCHEV (https://www.gesetze-im-internet.de/konsverchev/), which still uses 250 and 300 usual working days for part-time workers (§ 9) and a one day a week or five days a month return test (§ 7), sits beside protocol no. 5 from 2026; the euro conversion rule for Swiss pay; how the German tax office treats a year in which the 20% test fails only because of home office days.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `germany-to-switzerland-cross-border-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/germany-to-switzerland-cross-border-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
