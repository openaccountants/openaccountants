---
name: ch-cross-border
description: "Switzerland cross-border tax hub for 2026: when a person or company becomes or stops being taxable in Switzerland. Covers the residence tests for individuals (DBG art. 3: domicile, or a stay of 30 days with work or 90 days without) and companies (seat or effective management), arriving (lump-sum taxation under DBG art. 14, tax at source for foreign employees and the subsequent ordinary assessment from 2021), leaving (no exit tax for individuals; hidden reserves and 35% withholding tax when a company moves abroad), non-residents with Swiss income (employment, board fees, mortgage interest, pensions), the 35% Verrechnungssteuer and treaty refunds, and EU social security coordination. Calendar tax year. Trigger on: moving to Switzerland, leaving Switzerland, non-resident, expat, Quellensteuer, NOV, Pauschalbesteuerung, exit tax, Verrechnungssteuer refund, Grenzgänger. Out of scope: ch-federal-income-tax, ch-cantonal-tax, ch-corporate-income-tax, ch-lump-sum (detail), ch-ahv-iv, germany-to-switzerland-cross-border-tax."
version: 0.2
jurisdiction: CH
tax_year: 2026
last_updated: 2026-11-01
authored_by: Michael Cutajar and the OpenAccountants team
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: cross-border
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Switzerland: crossing the border (residence, arrival, departure, non-residents)

This skill is the cross-border hub for the Switzerland pack. It summarises what changes when a person or company crosses the Swiss border and links to the skills that hold the detail:

- Ordinary federal income tax: `ch-federal-income-tax`. Cantonal and communal tax: `ch-cantonal-tax`. Corporate profit tax: `ch-corporate-income-tax`.
- Lump-sum taxation in depth: `ch-lump-sum`. Note: that skill's federal minimum (CHF 451,200) does not appear in the law; the DBG figure was CHF 421,700 for 2023 to 2025 and is CHF 435,000 from 2026 (table below).
- AHV/IV social contributions: `ch-ahv-iv`. Employee shares and options across borders: `ch-taxation-employee-stock-options-and-employee`.
- The German corridor (Grenzgänger, weekly stayers, German exit tax): `germany-to-switzerland-cross-border-tax` in the Germany pack.

Switzerland taxes at three levels: the Confederation (direkte Bundessteuer, under the DBG), the 26 cantons and the communes. Federal rules are uniform. Cantonal rules differ on rates, on whether lump-sum taxation exists, and on procedure. Where a canton is needed, this skill uses Zurich as the worked example and cites the Zurich tax office. Check the client's own canton before relying on a cantonal point.

## Who this applies to

**Individuals: unlimited tax liability (DBG art. 3).** A person is taxable on worldwide income if they have a Swiss tax domicile or a Swiss tax stay:

- **Domicile:** living in Switzerland with the intention of staying permanently.
- **Stay (Aufenthalt):** being in Switzerland, ignoring temporary interruptions, for at least **30 days while working**, or at least **90 days without working**.
- Students and patients in a clinic who keep a domicile abroad do not become resident by being here for study or care.

There is no split-year concept in the UK sense. Liability starts on the day domicile or stay begins and ends on the day of departure or death (DBG art. 8). For a part year, income of that period is taxed, but the rate on regularly flowing income is set by converting it to 12 months (DBG art. 40 para. 3).

**Individuals: limited liability (DBG art. 4 and 5).** A non-resident is taxed only on Swiss-source items: a Swiss business or permanent establishment, Swiss real estate, work done in Switzerland, board fees from Swiss companies, interest on loans secured on Swiss real estate, Swiss public-sector and occupational pensions, and wages for work in international transport paid by a Swiss employer. Since 1 January 2025, a non-resident employee of a Swiss employer can also be taxable on telework done abroad, where an agreement with the neighbouring state gives Switzerland that right (DBG art. 5 para. 1 let. a-bis).

**Companies (DBG art. 50 to 52).** A company is resident if its **seat or effective management** is in Switzerland, and is then taxed on worldwide profit except foreign permanent establishments and foreign real estate. A foreign company is taxed only on Swiss business participations, permanent establishments, real estate, loans secured on Swiss real estate, and dealing in Swiss real estate (DBG art. 51). A permanent establishment is a fixed place of business; a building or assembly site counts if it lasts at least 12 months.

**Treaty override.** Where a person is resident in Switzerland and in a treaty state under both domestic laws, the treaty tie-breaker decides (see Cross-border points).

## Rates, bands and thresholds

| Item | Figure | Tax year | Source |
|---|---|---|---|
| Residence by stay, with gainful activity | 30 days | 2026 | [DBG art. 3](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Residence by stay, without gainful activity | 90 days | 2026 | [DBG art. 3](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Lump-sum taxation: federal minimum tax base | CHF 435,000 (or 7 times annual rent or rental value, if higher) | 2026 (from 1 Jan 2026) | [DBG art. 14 para. 3](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Lump-sum taxation: gap needed after earlier Swiss residence | 10 years | 2026 | [DBG art. 14 para. 1](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Tax at source: mandatory subsequent ordinary assessment (NOV) | Gross employment income of at least CHF 120,000 in a tax year | 2026 | [QStV art. 9](https://www.fedlex.admin.ch/eli/cc/2018/274/de) |
| Zurich: other NOV triggers | Taxable assets of CHF 80,000 (single) or CHF 160,000 (married); other income of CHF 3,000 | 2026 | [Kantonales Steueramt Zürich](https://www.zh.ch/de/steuern-finanzen/steuern/quellensteuer/Quellensteuerpflichtige-Personen.html) |
| Quasi-resident non-resident: NOV on request | At least 90% of worldwide gross income taxed in Switzerland | 2026 | [QStV art. 14](https://www.fedlex.admin.ch/eli/cc/2018/274/de) |
| Federal tax at source on board fees paid to non-residents | 5% of gross | 2026 | [DBG art. 93](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Federal tax at source on mortgage-secured interest paid to non-residents | 3% of gross | 2026 | [DBG art. 94](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Federal tax at source on Swiss pensions (public or occupational) paid abroad | 1% of gross for annuities | 2026 | [DBG art. 95 and 96](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Federal tax at source on blocked employee options, holder now abroad | 11.5% of the benefit | 2026 | [DBG art. 97a](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Non-resident artists, athletes, speakers (federal) | 0.8% to 7% of daily income, by band | 2026 | [DBG art. 92](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Verrechnungssteuer on dividends and on bond and bank interest | 35% | 2026 | [VStG art. 13](https://www.fedlex.admin.ch/eli/cc/1966/371_385_384/de) |
| Verrechnungssteuer on life annuities and pensions; other insurance benefits | 15%; 8% | 2026 | [VStG art. 13](https://www.fedlex.admin.ch/eli/cc/1966/371_385_384/de) |
| Treaty example: Swiss dividend to a German resident (portfolio) | 15% maximum Swiss tax; 0% for a German company holding 10% or more for 365 days | 2026 | [DBA CH-DE art. 10](https://www.fedlex.admin.ch/eli/cc/1972/3075_3128_2910/de) |
| Treaty example: Swiss interest to a German resident | Taxed only in Germany (refund of the 35%) | 2026 | [DBA CH-DE art. 11](https://www.fedlex.admin.ch/eli/cc/1972/3075_3128_2910/de) |
| Royalties and service fees paid abroad | No Swiss withholding tax: not in the VStG list of taxable income | 2026 | [VStG art. 4](https://www.fedlex.admin.ch/eli/cc/1966/371_385_384/de) |
| Exit tax on individuals | None: private capital gains are tax free | 2026 | [DBG art. 16 para. 3](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Company leaving: untaxed hidden reserves | Taxed at the ordinary profit tax rate (federal 8.5% of net profit) | 2026 | [DBG art. 61b, 68, 80](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de) |
| Late payment interest, federal taxes and Verrechnungssteuer | 4.0% | 2026 (unchanged for 2027) | [ESTV 2026](https://www.estv.admin.ch/de/newnsb/58uetWbVftSvrQqxHgivI); [ESTV 2027](https://www.estv.admin.ch/de/newnsb/bCxrY5LSQCuF) |

Cantonal and communal tax at source is added to the federal rates above, using the tariff of the competent canton. The ESTV publishes the cantonal tariffs as files for payroll software; readable tariffs are on each canton's site ([ESTV: Quellensteuer](https://www.estv.admin.ch/estv/de/home/direkte-bundessteuer/dbst-quellensteuer.html)).

## The taxable base

**Residents: worldwide, with exemption for foreign property and business.** A resident is taxed on worldwide income (and, at cantonal level, worldwide wealth). Foreign businesses, permanent establishments and real estate are exempt but count for the rate (exemption with progression, DBG art. 6 and 7). There is no remittance basis.

**Non-residents: Swiss-source only.** A non-resident is taxed only on the items in DBG art. 4 and 5, at the rate that applies to their worldwide income where it can be established (DBG art. 7 para. 1), and at least at the rate for their Swiss income for Swiss business and real estate (para. 2).

**Lump-sum taxation (Besteuerung nach dem Aufwand, DBG art. 14).** Instead of income tax, a person may pay tax on their worldwide living costs if all of these hold:

1. not a Swiss citizen;
2. unlimited Swiss tax liability for the first time, or after at least 10 years away;
3. no gainful activity in Switzerland.

Married spouses living together must both qualify. The base is the higher of actual worldwide living costs and the minimums: CHF 435,000 federal for 2026; 7 times the annual rent or rental value for a person with their own household (3 times the board and lodging price otherwise); and the "control calculation", the gross Swiss-source income plus foreign income on which treaty relief is claimed. The ordinary tariff then applies. The CHF 435,000 is indexed to consumer prices by the Federal Department of Finance (DBG art. 14 para. 6). It was CHF 421,700 for 2023 to 2025 and rose to CHF 435,000 from 1 January 2026 (art. 3 of the EFD ordinance of 10 September 2025 on cold progression, AS 2025 579). Cantons set their own minimums and some have abolished the regime: Zurich abolished it by popular vote in 2009, effective January 2010, and Schaffhausen, Appenzell Ausserrhoden, Basel-Landschaft and Basel-Stadt followed ([EFD](https://www.efd.admin.ch/de/besteuerung-aufwand)). A Zurich resident therefore cannot use lump-sum taxation. Appenzell Innerrhoden keeps the regime (its tax office publishes a lump-sum notice under art. 17 StG AI); the canton that abolished it is Appenzell Ausserrhoden. Detail: `ch-lump-sum`.

**Tax at source for foreign employees (Quellensteuer, DBG art. 83 to 90).** A resident employee without a settlement permit (C permit) or Swiss citizenship has tax deducted from gross salary by the employer. The deduction includes flat allowances for work expenses, insurance premiums and family. Spouses are not taxed at source if either is Swiss or holds a C permit.

Since 1 January 2021 the system has two routes:

- **Mandatory subsequent ordinary assessment (NOV, DBG art. 89).** Applies if gross employment income in a tax year is at least CHF 120,000 (QStV art. 9), or the person has income not taxed at source. Zurich adds triggers for wealth and other income (table above). Once in the NOV, the person stays in it until source taxation ends, even if income later falls. The tax withheld is credited without interest. For a part year, the CHF 120,000 is tested on income converted to 12 months (QStV art. 9 para. 5, pointing to DBG art. 40 para. 3).
- **NOV on request (DBG art. 89a).** Anyone below the triggers can ask for one by 31 March of the following year, or by the date of deregistration if leaving Switzerland. The request cannot be withdrawn (QStV art. 10). Without it, tax at source is final for employment income and no extra deductions are given later (DBG art. 89a para. 4).

Zurich's filing notice (ZStB 133.1) says "more than CHF 120,000", while the federal ordinance and Zurich's own tax-at-source page say "at least". The federal text governs; flag a client at exactly CHF 120,000.

**Non-resident employees (DBG art. 91 and 99a).** Non-residents working for a Swiss employer are taxed at source, and the tax is final (DBG art. 99). They can request an NOV by 31 March of the following year if most of their worldwide income is taxed in Switzerland, their situation is comparable to a resident's, or a treaty deduction needs it. QStV art. 14 fixes the "quasi-resident" test: as a rule at least 90% of worldwide gross income, including the spouse's, taxed in Switzerland. The request is made for each tax year.

**No exit tax for individuals.** Private capital gains are tax free (DBG art. 16 para. 3), and the DBG has no deemed disposal on departure. Leaving ends unlimited liability on the day of departure (DBG art. 8). Gains on Swiss real estate stay taxable by the canton. Pillar 2 and pillar 3a capital paid to someone who has left is taxed at source (DBG art. 95 and 96).

**Companies moving in.** A company that moves its seat or effective management to Switzerland, or transfers assets or functions here, may disclose hidden reserves, including self-created goodwill, tax free. Disclosed reserves are then depreciated; goodwill over 10 years (DBG art. 61a).

**Companies moving out.** Untaxed hidden reserves, including self-created goodwill, are taxed when the seat or effective management moves abroad or assets, businesses or functions are moved to a foreign business or permanent establishment (DBG art. 61b and 80 para. 2). The move of the seat abroad is also treated as a liquidation for Verrechnungssteuer (VStG art. 4 para. 2): the liquidation surplus beyond nominal capital and confirmed capital contribution reserves bears 35%, refundable to the shareholders under a treaty.

## Deadlines and filing

**Arrival.** Register with the commune of residence (Einwohnerkontrolle); cantonal law sets the period. The employer of a source-taxed employee must register them and withhold from the first salary under the tariff of the canton of residence (DBG art. 107 para. 1 let. a). An employee who receives a C permit, or marries a Swiss citizen or C-permit holder, moves to ordinary assessment for the whole year; tax at source stops from the following month (QStV art. 12).

**During residence.** The tax year is the calendar year (DBG art. 40). In Zurich the return for 2026 is due by **31 March 2027**; extension requests must arrive before the deadline ([ZStB 133.1](https://www.zh.ch/de/steuern-finanzen/steuern/treuhaender/steuerbuch/steuerbuch-definition/zstb-133-1.html)). Source-taxed persons in an NOV whose forms arrive after the end of February get 30 days from receipt. A person with other income must ask for the return form by 31 March of the following year (DBG art. 89 para. 4).

**NOV on request.** By 31 March of the following year, or by deregistration if leaving (DBG art. 89a para. 3; QStV art. 10; for non-residents DBG art. 99a and QStV art. 14).

**Departure.** Deregister with the commune. In Zurich, a source-taxed person in the NOV who moves abroad must file a return for the year of departure in all cases, at the earliest one month before leaving, and must appoint a person in Switzerland to receive assessment and collection documents. Other persons who leave file within 30 days of receiving the forms ([ZStB 133.1](https://www.zh.ch/de/steuern-finanzen/steuern/treuhaender/steuerbuch/steuerbuch-definition/zstb-133-1.html)).

**Payment.** Federal tax is payable within 30 days of falling due (DBG art. 163). The cantons publish due dates.

**Verrechnungssteuer refund for a non-resident.** Under the German treaty, the refund is filed online on the ESTV ePortal (form 85) for income due from 1 January 2020, with a stamp sheet certified by the German tax office ([ESTV: Germany](https://www.estv.admin.ch/en/germany)). Each treaty has its own form. Residents of Switzerland claim the refund through their tax return within three years after the end of the calendar year of payment (VStG art. 32).

## Penalties and interest

- **Late payment interest:** 4.0% for 2026, set by the Federal Department of Finance (DBG art. 164; [ESTV](https://www.estv.admin.ch/de/newnsb/58uetWbVftSvrQqxHgivI)). The rate stays 4.0% for 2027.
- **Procedural failures** (no return after a reminder, failing to report): fine up to CHF 1,000, up to CHF 10,000 in serious or repeat cases (DBG art. 174).
- **Tax evasion:** fine normally equal to the tax evaded, reduced to one third for slight fault or increased to three times for serious fault (DBG art. 175). This also covers an employer who fails to deduct tax at source.
- **Misusing tax at source withheld:** imprisonment up to three years or a monetary penalty (DBG art. 187).
- **Losing the Verrechnungssteuer refund:** a resident who does not declare the income or the asset loses the refund (VStG art. 23).
- **Assessment by estimate** if the return is not filed after a reminder (DBG art. 130).

Cantonal penalties follow the cantonal tax law and are broadly parallel.

## Cross-border points

**Treaty tie-breaker.** Switzerland's treaties follow the OECD order: permanent home, centre of vital interests, habitual abode, nationality. Under the German treaty (art. 4 para. 2), a Swiss resident without Swiss nationality who was unlimited taxable in Germany for at least five years in total remains taxable in Germany on German-source income for the year of departure and the five following years, with credit for Swiss tax (art. 4 para. 4). This does not apply to a person who moved to Switzerland to take up genuine employment with an employer in which they have no substantial interest. See `germany-to-switzerland-cross-border-tax`.

**How Switzerland relieves double tax.** Under domestic law, foreign businesses, permanent establishments and real estate of a resident are exempt and count only for the rate (DBG art. 6 and 7). For other foreign income, relief comes from the treaty with the source state; where the source state keeps a limited tax on dividends, interest or royalties, Switzerland gives a credit on request. This skill does not compute that credit.

**Verrechnungssteuer and treaties.** The 35% is withheld by the Swiss paying company or bank. A non-resident gets back the part above the treaty rate. Example rates (German treaty): portfolio dividends 15%, dividends to a German company holding 10% or more for 365 days 0%, interest 0%. Check the treaty for the client's country.

**Cross-border commuters.** Germany, France, Italy and Austria have special frontier worker rules, some with Swiss withholding at a capped rate. They differ by treaty and by canton. See `germany-to-switzerland-cross-border-tax` for the German regime. The Italy agreement excludes quasi-resident NOV for frontier workers under its art. 2 let. b (QStV art. 14 para. 3).

**Social security.** Switzerland is not in the EU, but under Annex II of the Agreement on the Free Movement of Persons (in force 1 June 2002), Regulations (EC) 883/2004 and 987/2009 apply between Switzerland and the EU states; Regulations 1408/71 and 574/72 applied until 31 March 2012. One state is competent for all contributions, normally the state of work. A posted worker stays in the home system with an A1 certificate for up to 24 months; longer needs an exception agreement between the two states ([BSV posting memo](https://www.bsv.admin.ch/dam/de/sd-web/nj5pRW599A3W/entsendungsmerkblatt-ch-eu.pdf)). The same rules apply to Iceland, Liechtenstein and Norway under the EFTA Convention, but only for nationals of those states ([BSV](https://www.bsv.admin.ch/en/social-security-agreements)). Swiss contributions: `ch-ahv-iv`.

**Pointers.** Rates and deductions for residents: `ch-federal-income-tax` and `ch-cantonal-tax`. Corporate profit tax rates and the participation deduction: `ch-corporate-income-tax`.

## Worked examples

### Example 1: German engineer moves to Zurich on 1 April 2026, taxed at source

Facts: German citizen, single, B permit, arrives in Zurich on 1 April 2026 for a job with a Zurich employer. Gross salary CHF 13,000 a month, no 13th salary, no other income, no Swiss wealth. She has no C permit and is not married to a Swiss or C-permit holder, so tax is deducted at source from April (DBG art. 83). She becomes resident from 1 April (domicile, and in any case more than 30 days with work).

Does she fall into the mandatory NOV? Her actual 2026 gross is 9 x 13,000 = CHF 117,000, which is below CHF 120,000. But liability began during the year, so the test uses income converted to 12 months (QStV art. 9 para. 5 and DBG art. 40 para. 3): 117,000 / 9 x 12 = CHF 156,000. That is CHF 36,000 above the threshold, so she must file a 2026 Zurich tax return by 31 March 2027. The tax withheld from April to December is credited, without interest. She stays in the NOV every year until source taxation ends, even if her salary falls.

```oa-check
name: Part-year arrival, NOV threshold test on annualised salary (2026)
inputs:
  monthly_gross: 13000
  months_in_2026: 9
  nov_threshold: 120000
steps:
  - actual_gross: monthly_gross * months_in_2026
  - annualised_gross: actual_gross / months_in_2026 * 12
  - shortfall_on_actual: nov_threshold - actual_gross
  - excess_on_annualised: annualised_gross - nov_threshold
expected:
  actual_gross: 117000.00
  annualised_gross: 156000.00
  shortfall_on_actual: 3000.00
  excess_on_annualised: 36000.00
```

The edge case: testing the actual CHF 117,000 would wrongly conclude that tax at source is final. The tax itself depends on the Zurich and federal tariffs; use `ch-federal-income-tax` and `ch-cantonal-tax`.

### Example 2: German resident with a Swiss board seat and Swiss shares

Facts: a German resident (never Swiss resident) sits on the board of a Zurich AG and receives board fees of CHF 50,000 in 2026. He also owns 2% of the same company and receives a dividend of CHF 20,000.

- **Board fees.** Taxable in Switzerland as a non-resident (DBG art. 5 para. 1 let. b; DBA CH-DE art. 16). Federal tax at source is 5% of gross (DBG art. 93): CHF 2,500. Zurich cantonal and communal tax at source is added under the Zurich tariff for board members (not computed here). Germany taxes the fees too and credits the Swiss tax under its own rules.
- **Dividend.** The company withholds 35% Verrechnungssteuer (VStG art. 13): CHF 7,000. The treaty limits Swiss tax on a portfolio dividend to 15% (DBA CH-DE art. 10 para. 2 let. c): CHF 3,000. He files form 85 on the ESTV ePortal to recover CHF 4,000.

```oa-check
name: Non-resident board fees and dividend, federal tax at source and treaty refund (2026)
inputs:
  board_fees: 50000
  dividend: 20000
steps:
  - federal_qst_board_fees: pct(board_fees, 5)
  - vst_withheld: pct(dividend, 35)
  - treaty_max_swiss_tax: pct(dividend, 15)
  - refund_claim: vst_withheld - treaty_max_swiss_tax
  - swiss_tax_kept_federal_level: federal_qst_board_fees + treaty_max_swiss_tax
expected:
  federal_qst_board_fees: 2500.00
  vst_withheld: 7000.00
  treaty_max_swiss_tax: 3000.00
  refund_claim: 4000.00
  swiss_tax_kept_federal_level: 5500.00
```

If he were a German company holding 10% or more for 365 days, the Swiss tax on the dividend would be 0% (DBA CH-DE art. 10 para. 3) and the full CHF 7,000 would be refundable.

## Ask the client first

1. Which canton and commune do you live in, or will you? Rates, lump-sum availability and procedure depend on it.
2. Nationality, permit (B, C, L, G) and marital status, and your spouse's nationality and permit. These decide whether tax is taken at source.
3. Dates: the exact day you arrived or will leave, and days spent in Switzerland, with and without work.
4. Gross salary for the year, any 13th salary or bonus, wealth, and any income not taxed at source (rent, self-employment, foreign income).
5. Will you work in Switzerland at all? Any gainful activity rules out lump-sum taxation.
6. For a company: where is the board and day-to-day management, what assets and functions move, and what are the hidden reserves and capital contribution reserves?

## Sources

Read on 2026-10-22:

- Bundesgesetz über die direkte Bundessteuer (DBG), SR 642.11, version in force 2 September 2026, art. 3 to 8, 14, 16, 40, 50 to 52, 61a, 61b, 68, 80, 83 to 101, 107, 163, 164, 174, 175, 187: https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de
- DBG, version in force 1 January 2025 (art. 14 para. 3 let. a: CHF 421,700 under the EFD ordinance of 16 September 2022): https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/20250101/de
- Quellensteuerverordnung (QStV), SR 642.118.2, version of 10 January 2025 (still current for 2026), art. 9, 10, 12, 14: https://www.fedlex.admin.ch/eli/cc/2018/274/de
- Bundesgesetz über die Verrechnungssteuer (VStG), SR 642.21, art. 4, 13, 22, 23, 32: https://www.fedlex.admin.ch/eli/cc/1966/371_385_384/de
- Abkommen Schweiz-Deutschland zur Vermeidung der Doppelbesteuerung (DBA CH-DE), SR 0.672.913.62, version of 27 November 2025, art. 4, 10, 11, 16: https://www.fedlex.admin.ch/eli/cc/1972/3075_3128_2910/de
- ESTV, Verzugs- und Vergütungszinssätze ab 2026: https://www.estv.admin.ch/de/newnsb/58uetWbVftSvrQqxHgivI
- ESTV, no change to the interest rates for 2027 (22 September 2026): https://www.estv.admin.ch/de/newnsb/bCxrY5LSQCuF
- ESTV, Schweizerische Quellensteuer: https://www.estv.admin.ch/estv/de/home/direkte-bundessteuer/dbst-quellensteuer.html
- ESTV, Germany (Verrechnungssteuer refund, form 85): https://www.estv.admin.ch/en/germany
- EFD, Besteuerung nach dem Aufwand: https://www.efd.admin.ch/de/besteuerung-aufwand
- BSV, Social security agreements: https://www.bsv.admin.ch/en/social-security-agreements
- Kantonale Steuerverwaltung Appenzell Innerrhoden, Merkblatt Besteuerung nach dem Aufwand (valid from 2024): https://ai.ch/themen/steuern/publikationen/merkblaetter-gueltig-ab-2024/besteuerung-nach-dem-aufwand/download
- BSV, Merkblatt Entsendung Schweiz-EU: https://www.bsv.admin.ch/dam/de/sd-web/nj5pRW599A3W/entsendungsmerkblatt-ch-eu.pdf
- Kantonales Steueramt Zürich, Quellensteuerpflichtige Personen: https://www.zh.ch/de/steuern-finanzen/steuern/quellensteuer/Quellensteuerpflichtige-Personen.html
- Kantonales Steueramt Zürich, Zürcher Steuerbuch Nr. 133.1 (filing notice): https://www.zh.ch/de/steuern-finanzen/steuern/treuhaender/steuerbuch/steuerbuch-definition/zstb-133-1.html

Not yet confirmed: the Zurich cantonal and communal tax-at-source rate for non-resident board members; the deadline for a treaty refund claim of Verrechnungssteuer by a German resident; the period for registering with the commune on arrival (cantonal law); the capped rates in the French, Italian and Austrian frontier-worker arrangements.

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
