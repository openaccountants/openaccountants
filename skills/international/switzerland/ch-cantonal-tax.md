---
name: ch-cantonal-tax
description: "Swiss cantonal and communal income and wealth tax on individuals for tax year 2026, from the StHG, the ESTV tables and cantonal sources. Covers how the tax is built (simple tax from the cantonal tariff, times the cantonal, communal and church multipliers), the 2026 multipliers in all 26 cantonal capitals, the Zurich and Zug 2026 tariffs, wealth tax thresholds, deductions that differ by canton (commuting caps, childcare), filing deadlines for Zurich, Zug, Bern, Basel-Stadt, Geneva and Vaud, the 31 December rule when moving between cantons, interest and penalties. Two worked examples: CHF 100,000 taxable income in Zurich city and in Zug city. Trigger on: Kantonssteuer, Gemeindesteuer, Steuerfuss, einfache Steuer, Kirchensteuer, impôt cantonal et communal, centimes additionnels, Vermögenssteuer, moving canton, Swiss income tax by canton. Out of scope: ch-federal-income-tax, ch-payroll (tax at source), ch-cross-border, ch-lump-sum, ch-corporate-income-tax."
version: 2.1
jurisdiction: CH
category: international
tax_year: 2026
last_updated: 2026-10-23
review_status: pending_review
verified_by: pending
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Switzerland: cantonal and communal income and wealth tax (2026)

Every canton must levy an income tax and a wealth tax on individuals (StHG art. 2 para. 1 let. a). Federal law (the StHG) sets what is taxed and how; each canton sets its own tariffs, rates and tax-free amounts (StHG art. 1 para. 3). Most cantons put only a "simple tax" (einfache Steuer) in their tax law. The tax actually owed is the simple tax multiplied by yearly multipliers (Steuerfuss) for the canton, the commune and, for church members, the parish (ESTV, Steuersatz und Steuerfuss, section 3). Federal income tax comes on top and is uniform across Switzerland.

Related skills, linked rather than repeated:

- Federal income tax (direkte Bundessteuer): `ch-federal-income-tax`.
- Tax at source on wages of foreign employees: `ch-payroll`. Arriving, leaving, non-residents, the subsequent ordinary assessment (NOV): `ch-cross-border`.
- Lump-sum taxation (Besteuerung nach dem Aufwand): `ch-lump-sum`.
- Companies: `ch-corporate-income-tax`. Social contributions of the self-employed: `ch-ahv-iv`.

## Who this applies to

- **Unlimited liability in a canton:** a person with tax domicile in the canton, or who stays there at least 30 days while working or 90 days without working (StHG art. 3 para. 1). Domicile means living there with the intention of staying, or a domicile given by federal law (StHG art. 3 para. 2).
- **Couples and children:** the income and wealth of spouses living together are added up, whatever their marital property regime; the same applies to registered partners. A child's income and wealth go to the parent with parental authority, except the child's earned income and real estate gains, which are taxed separately (StHG art. 3 para. 3 to 5).
- **Limited liability in a canton:** a person living elsewhere is taxed in the canton where they run a business or permanent establishment, or own real estate (StHG art. 4 para. 1). People not resident in Switzerland are also taxed on work done in the canton, board fees, mortgage interest, pensions from public or Swiss occupational schemes and similar income (StHG art. 4 para. 2).
- **Moving within Switzerland:** for the whole tax year, the canton where the person lives on 31 December taxes them (StHG art. 4b para. 1). See "Cross-border points".
- **Taxed at source instead:** foreign employees without a settlement permit (C permit) are taxed through payroll (StHG art. 32 and following); see `ch-payroll` and `ch-cross-border`.
- **Out:** companies (`ch-corporate-income-tax`), real estate gains tax (Grundstückgewinnsteuer, a separate cantonal tax, StHG art. 2 para. 1 let. d), inheritance and gift taxes.

## Rates, bands and thresholds

**The method.** Taxable income x cantonal tariff = simple tax. Then:

tax owed = simple tax x (cantonal multiplier + communal multiplier + church multiplier)

Most cantons state the multipliers as a percentage of the simple tax. Some (for example Bern, Lucerne, Obwalden) state them in units, such as 2.975 times the simple tax. In the French-speaking cantons the commune's multiplier is often a share of the cantonal tax (centimes additionnels). Valais applies its tariff directly, without multipliers (ESTV, Steuersatz und Steuerfuss, 3.1 and 3.4).

**2026 multipliers in the cantonal capitals (individuals, income and wealth).** Source: [ESTV, Steuersatz und Steuerfuss, January 2026, table 3.4.1](https://www.estv2.admin.ch/stp/ds/e-steuersatz-steuerfuss-de.pdf). Other communes in the same canton have other multipliers.

| Canton | Capital | Canton | Commune | Church, reformed | Church, Roman Catholic | Note |
|---|---|---|---|---|---|---|
| ZH | Zurich | 95% | 119% | 10% | 10% | Christian Catholic 14% ([Stadt Zürich](https://www.stadt-zuerich.ch/de/lebenslagen/steuern/natuerliche-personen/steuerberechnung.html)) |
| BE | Bern | 2.975 | 1.54 | 0.184 | 0.190 | in units of the simple tax |
| LU | Lucerne | 1.45 | 1.45 | 0.25 | 0.25 | units |
| UR | Altdorf | 100% | 95% | 115% | 82% | |
| SZ | Schwyz | 110% | 175% | 25% | 26% | commune includes the district |
| OW | Sarnen | 3.25 | 3.86 | 0.54 | 0.54 | units |
| NW | Stans | 2.66 | 2.35 | 0.26 | 0.40 | units |
| GL | Glarus | 58% | 61% | 7.5% | 8% | plus a 1.7% building surcharge on the simple tax |
| ZG | Zug | 78% | 52% | 6% | 5.95% | ESTV prints the 2025 commune and church figures (52.11%, 7.5%, 7%); 2026 from the [Zug tax office](https://zg.ch/dam/jcr:24fb8832-3383-4718-9a48-9461bc7501fc/Steuerf%C3%BCsse%202026_effektiv%2021.1.26.pdf) |
| FR | Fribourg | 96% (wealth 100%) | 80% | 9% (wealth 10%) | 7% (wealth 20%) | |
| SO | Solothurn | 104% | 107% | 16% | 21% | ESTV shows the 2025 figures |
| BS | Basel | 100% | none | 8% of the cantonal income tax | 8% of the cantonal income tax | the city levies no communal tax; the canton's tax includes it |
| BL | Liestal | 100% | 65% | 0.55% of taxable income; on wealth ESTV prints 0.05 (footnote: per cent or per mille) | 6.75% of the cantonal tax | |
| SH | Schaffhausen | 76% | 83% | 13% | 13% | |
| AR | Herisau | 3.3 | 4.1 | 0.60 | 0.47 | units |
| AI | Appenzell | 96% | 56% | 10% | 10% | ESTV shows the 2025 figures |
| SG | St. Gallen | 105% | 138% | 25% | 26% | |
| GR | Chur | 92% | 88% of the simple cantonal tax | 14.5% | 9% | |
| AG | Aarau | 103% | 96% | 15% | 18% | |
| TG | Frauenfeld | 109% | 142% | 16% | 16% | |
| TI | Bellinzona | 100% | 93% | none | none | |
| VD | Lausanne | 155% | 78.5% | none | none | |
| VS | Sion | no multiplier: tariff applies directly | 1.10 | 3% of the communal tax | 3% of the communal tax | |
| NE | Neuchâtel | 124% | 65% | none | none | |
| GE | Geneva | 48.5% | 45.49% | none | none | ESTV footnote: a deduction of 12% of the cantonal tax at 147.5% |
| JU | Delémont | 2.85 | 1.90 | 8.1% | 6.4% | units |

**Other figures.**

| Item | Rate or amount | Year | Source |
|---|---|---|---|
| Zurich: income tariff for single people (Grundtarif), simple tax | 0% on the first CHF 7,000, then 2%, 3%, 4%, 5%, 6%, 7%, 8%, 9%, 10%, 11%, 12% on bands of 5,000, 4,800, 8,000, 9,700, 11,200, 13,100, 17,600, 34,000, 33,700, 53,300, 69,300; 13% above CHF 266,700 | 2026 | [ESTV Kantonsblatt Zürich, § 35 para. 1 StG](https://www.estv2.admin.ch/stp/kb/zh-de.pdf) |
| Zurich: married tariff | 0% on the first CHF 14,100; 13% above CHF 370,600 | 2026 | [ESTV Kantonsblatt Zürich, § 35 para. 2 StG](https://www.estv2.admin.ch/stp/kb/zh-de.pdf) |
| Zurich: wealth tariff, single | 0 per mille on the first CHF 81,000, rising to 3 per mille above CHF 3,304,000; married: 0 on the first CHF 161,000 | 2026 | [ESTV Kantonsblatt Zürich, § 47 StG](https://www.estv2.admin.ch/stp/kb/zh-de.pdf) |
| Zurich: cantonal multiplier | 95% for 2026. The Kantonsrat sets it for two calendar years at a time, and the 2026 indexation marks the start of a period, so 95% runs for 2026 and 2027 | 2026 | [ESTV table 3.4.1](https://www.estv2.admin.ch/stp/ds/e-steuersatz-steuerfuss-de.pdf); [§ 2 para. 2 and § 48 StG in the Kantonsblatt](https://www.estv2.admin.ch/stp/kb/zh-de.pdf) |
| Zug: income tariff for single people (Grundtarif), simple tax (bands unchanged from 2025: index June 2025 at 110.2, as in June 2024) | 0.5% on the first CHF 1,100, then 1%, 2%, 3%, 3.25%, 3.5%, 4%, 4.5%, 5.5%, 5.5%, 6.5%, 8%, 10%, 9% on bands of 2,200, 2,800, 4,000, 5,200, 5,800, 5,800, 8,000, 11,500, 13,300, 15,000, 20,100, 25,300, 29,800; 8% above CHF 149,900 | 2026 | [Steuerverwaltung Zug, Grundtarif gültig Steuerperiode 2026](https://zg.ch/dam/jcr:96c7eef4-eb2f-4f8a-a4c4-dad209249598/Grundtarif%202001%20bis%202026.pdf) |
| Zug: personal deduction | CHF 12,000 single; CHF 24,000 married or single with children (amounts in force from 2025) | 2026 | [ESTV Kantonsblatt Zug, § 33 StG](https://www.estv2.admin.ch/stp/kb/zg-de.pdf) |
| Zug: wealth tariff | 0.425 per mille on the first CHF 254,000, up to 1.7 per mille above CHF 762,000 | 2026 | [Steuerverwaltung Zug, Grundtarif 2026](https://zg.ch/dam/jcr:96c7eef4-eb2f-4f8a-a4c4-dad209249598/Grundtarif%202001%20bis%202026.pdf) |
| Zug: cantonal multiplier | 78% for 2026 to 2029 (statutory 82%, cut by the vote of 30 November 2025) | 2026 | [Zug tax office, Steuerfüsse 2023 to 2026](https://zg.ch/dam/jcr:24fb8832-3383-4718-9a48-9461bc7501fc/Steuerf%C3%BCsse%202026_effektiv%2021.1.26.pdf); [vote explanation](https://cdn.zg.ch/dam/jcr:09c43d5c-61d7-4ca1-b825-62f5cba55fba/20251130_Erl%C3%A4uterung%20KA2_%C3%84nderung_Steuergesetz-9_UA.pdf) |
| Wealth tax-free amount, Zug | CHF 204,000 single; CHF 408,000 married; CHF 102,000 per minor child (amounts in force from 2025) | 2026 | [ESTV Kantonsblatt Zug, § 44 StG](https://www.estv2.admin.ch/stp/kb/zg-de.pdf) |
| Wealth tax-free amount, Basel-Stadt | CHF 75,000 single; CHF 150,000 married or single parent; CHF 15,000 per minor child | 2026 | [ESTV Kantonsblatt Basel-Stadt, § 49 StG](https://www.estv2.admin.ch/stp/kb/bs-de.pdf) |
| Wealth tax, Bern | Not levied if the rate-determining wealth is below CHF 100,000 | 2026 | [ESTV Kantonsblatt Bern, art. 65 para. 3 StG](https://www.estv2.admin.ch/stp/kb/be-de.pdf) |
| Wealth deduction, Geneva | CHF 87,872 single; CHF 175,743 married or single parent; CHF 43,936 per dependant | 2026 | [ESTV Feuille cantonale Genève, art. 58 LIPP, art. 16 RCEPF](https://www.estv2.admin.ch/stp/kb/ge-fr.pdf) |
| Wealth tax, Vaud | Net wealth below CHF 60,000 not taxed; doubled for married couples | 2026 | [ESTV Feuille cantonale Vaud, LI](https://www.estv2.admin.ch/stp/kb/vd-fr.pdf) |
| Pillar 3a, maximum deduction (federal and cantonal) | CHF 7,258 with a pension fund; up to CHF 36,288 without | 2026 | [BSV, Masszahlen berufliche Vorsorge 2025/2026, no. 9](https://www.bsv.admin.ch/dam/de/sd-web/GZplHByBJoFc/Internet_Masszahlenarticles_25_26_d.pdf) |

**Deductions that differ by canton (2026).** The StHG lets each canton cap commuting costs and set the childcare maximum (StHG art. 9 para. 1 and para. 2 let. m). Pension fund contributions and buy-ins (StHG art. 9 para. 2 let. d) and pillar 3a (let. e, same maximum as federal) are deductible everywhere.

| Canton | Commuting cap, employees | Childcare per child under 14 | Source |
|---|---|---|---|
| Zurich | CHF 5,200 | CHF 25,300 | [Kantonsblatt ZH, § 26 and 31 StG](https://www.estv2.admin.ch/stp/kb/zh-de.pdf) |
| Zug | CHF 6,000 | CHF 25,400 | [Kantonsblatt ZG, § 25 and 30 StG](https://www.estv2.admin.ch/stp/kb/zg-de.pdf) |
| Bern | CHF 7,000 | CHF 16,000 | [Kantonsblatt BE, art. 31 and 38 StG](https://www.estv2.admin.ch/stp/kb/be-de.pdf) |
| Basel-Stadt | CHF 3,200 | CHF 26,000 | [Kantonsblatt BS, § 27 and 32 StG](https://www.estv2.admin.ch/stp/kb/bs-de.pdf) |
| Geneva | CHF 536 | CHF 26,392 | [Feuille cantonale GE, art. 29 and 35 LIPP, RCEPF 2026](https://www.estv2.admin.ch/stp/kb/ge-fr.pdf) |
| Vaud | flat rates by means of transport; no overall cap read | CHF 15,200 | [Feuille cantonale VD, art. 30 and 37 LI](https://www.estv2.admin.ch/stp/kb/vd-fr.pdf) |

The Basel-Stadt and Zug amounts are those in force from 2025 as shown in the February 2026 Kantonsblatt; the Zurich, Geneva and Vaud amounts are stated for 2026.

## The taxable base

**Income.** The StHG sets the base the cantons must use: all income, including employment, self-employment, investment income, pensions and imputed rent on an owner-occupied home (StHG art. 7). The cantons follow it closely, so the base is largely the same as for federal tax (`ch-federal-income-tax`). Differences sit mainly in the amounts of deductions (tables above) and in a few cantonal rules, for example:

- Zurich taxes dividends from holdings of at least 10% at 50% (§ 20 para. 2 StG); gains on private movable assets are tax-free everywhere, subject to the real estate gains tax (§ 16 para. 3 StG for Zurich).
- Zurich has no general personal deduction: its tariff starts with a 0% band of CHF 7,000 (single) or CHF 14,100 (married). Zug gives a personal deduction of CHF 12,000 or CHF 24,000 and a rent deduction of 30% of rent, at most CHF 10,800 (§ 33 StG Zug).
- Zurich gives CHF 9,400 per child (§ 34 StG, 2026); Zug CHF 12,600 per child (§ 33 StG, from 2025).

**Order of the computation.** Gross income, less work costs and general deductions, gives net income; less social deductions, gives taxable income (Zurich and Zug Kantonsblätter, "Ermittlung des steuerbaren Einkommens"). Apply the tariff for the household type (single, or married and single parents) to get the simple tax, then the multipliers.

**Self-employed.** Profit from the business year that ends in the tax year counts (StHG art. 16). The signed accounts, or for simplified bookkeeping a statement of income, expenses, assets and private drawings, go with the return (StHG art. 42 para. 3).

**Wealth.** All net wealth is taxed: assets at market value less debts; household goods and personal effects are exempt (StHG art. 13 and 14). Business assets are valued at their income tax value (StHG art. 14 para. 3). Wealth is measured at 31 December or at the end of tax liability (StHG art. 17). The canton then subtracts its tax-free amounts and applies its wealth tariff, multiplied by the same multipliers as income in most cantons.

**Lump sums from pensions.** Pension capital (2nd pillar, pillar 3a) is taxed separately from other income, at a reduced rate, in the canton of residence at the time of payment (StHG art. 4b para. 1 and art. 11 para. 3). Zurich computes it at the rate for one twentieth of the lump sum, with a minimum simple rate of 2% (§ 37 StG); Zug charges 30% (40% above CHF 230,400) of the normal tariff (§ 37 StG Zug).

**Caps on the total burden.** In Geneva and Ticino, cantonal and communal income and wealth tax together may not exceed 60% of net taxable income; any cut is taken from the wealth tax. Bern, Lucerne, Basel-Stadt, Aargau, Vaud and Valais have caps of their own, each worked differently (ESTV, Steuersatz und Steuerfuss, 3.3.1).

## Deadlines and filing

- **Tax period:** the calendar year (StHG art. 15 para. 1). One return covers cantonal, communal, church and federal tax.
- **Who must file in Zurich for 2026:** everyone living in Zurich on 31 December 2026 who is not taxed at source, source-taxed people in the subsequent ordinary assessment, and people living elsewhere who own Zurich real estate or a business there on 31 December 2026 ([ZStB 133.1, Aufforderung 2027](https://www.zh.ch/content/dam/zhweb/bilder-dokumente/themen/steuern-finanzen/steuern/vertreter/steuerbuch/zstb-nr-133-1/ZStB-Nr-133-1_Aufforderung-2027.pdf), A.I.1).

| Canton | Filing deadline (individuals) | Source |
|---|---|---|
| Zurich | 31 March 2027 for the 2026 return; forms sent in January 2027 | [ZStB 133.1, Aufforderung 2027, A.I.3 and 4](https://www.zh.ch/content/dam/zhweb/bilder-dokumente/themen/steuern-finanzen/steuern/vertreter/steuerbuch/zstb-nr-133-1/ZStB-Nr-133-1_Aufforderung-2027.pdf) |
| Zug | 30 April of the following year (30 April 2026 for the 2025 return); extensions online | [Kanton Zug, eTax.zug 2025](https://zg.ch/news/news~_2026_2_etax-zug-2025-neue-deklarationsloesung-fuer-natuerliche-personen-ist-online~.html) |
| Bern | 15 March for employees; 15 May for the self-employed. For the 2025 returns, free online extension to 15 July 2026, at most to 15 November 2026 | [Steuerverwaltung Bern, TaxInfo](https://www.taxinfo.sv.fin.be.ch/taxinfo/1cce120a-05da-45e8-8968-b66ae236fee5); [Kanton Bern media release](https://www.be.ch/de/start/dienstleistungen/medien/medienmitteilungen.html?newsID=68239ab2-4062-4a28-a910-4a9b7bd0dbf4) |
| Basel-Stadt | 31 March of the following year (31 March 2026 for the 2025 return); free extension to 30 September 2026 for the 2025 return, CHF 40 for a longer one; reminder fee CHF 40 | [bs.ch, Steuererklärung als natürliche Person einreichen](https://www.bs.ch/themen/arbeit-und-steuern/steuererklaerung/steuererklaerung-als-natuerliche-person-einreichen) |
| Geneva | Before 31 March of each year, even if no tax is due | [ge.ch, Remplir ma déclaration d'impôt](https://www.ge.ch/remplir-ma-declaration-impot-tant-que-particulier) |
| Vaud | Legal deadline 15 March, tolerance to 30 June; free extension requests by 30 June | [vd.ch, Demander un délai](https://www.vd.ch/etat-droit-finances/impots/impots-pour-les-individus/demander-un-delai-pour-deposer-ma-declaration-dimpot) |

Other cantons were not read for this skill; use the date on the canton's own notice.

- **Leaving Switzerland or death (Zurich):** a return for the part year is due within 30 days after the forms are sent, 60 days on death (ZStB 133.1, A.II.3).
- **Payment in Zurich:** payments made in 2026 before 1 October 2026 earn interest in the taxpayer's favour; from 1 October 2026 interest runs against the taxpayer on the final tax. The rate both ways for 2026 is 0.75% ([Wegleitung ZH 2026](https://www.zh.ch/content/dam/zhweb/bilder-dokumente/themen/steuern-finanzen/steuern/natuerlichepersonen/2026/est-wegleitungen-uj/305%20Wegleitung%20ZH%202026%20UJ%20bf.pdf), Anmerkungen zur Steuerzahlung). Other cantons set their own due dates and instalment plans.

## Penalties and interest

- **Late payment, Zurich:** 4.5% default interest on a final invoice not paid within 30 days (Wegleitung ZH 2026). Federal tax has its own rate (`ch-federal-income-tax`).
- **Procedural failures** (not filing after a reminder, not giving information): fine up to CHF 1,000, up to CHF 10,000 in serious or repeat cases (StHG art. 55 para. 1). A person who does not file after a reminder is assessed by estimate.
- **Tax evasion:** fine from one third to three times the evaded tax, normally equal to it, plus the evaded tax (StHG art. 56 para. 1).
- **Voluntary disclosure:** a first self-report is penalty-free if no tax authority knew, the person cooperates fully and tries seriously to pay the back tax (StHG art. 56 para. 1bis). For each later self-report the fine is one fifth of the evaded tax (StHG art. 56 para. 1ter). Zurich requires an express statement that undeclared income or wealth is now declared (Wegleitung ZH 2026).
- **Spouses** are fined only for evasion of their own tax factors (StHG art. 57 para. 4).

## Cross-border points

- **Moving between cantons:** the canton of residence on 31 December taxes the whole year's income and wealth (StHG art. 4b para. 1). Someone moving from Zug to Zurich on 1 December 2026 files one 2026 return, in Zurich, at Zurich rates. Exception: a pension lump sum is taxed in the canton of residence on the day it falls due (StHG art. 4b para. 1).
- **Property or business in another canton:** that canton taxes the property or business for the whole year, even if it was bought or sold during the year; income and wealth are split between the cantons under the federal ban on intercantonal double taxation (StHG art. 4b para. 2). The rate in each canton is set on total income and wealth.
- **Arriving from or leaving for abroad:** liability covers only part of the year; regular income is converted to 12 months for the rate (StHG art. 15 para. 3). See `ch-cross-border`.
- **Tax at source:** foreign employees without a C permit pay cantonal, communal and federal tax through payroll at the tariff of their canton of residence. Those with gross pay of more than CHF 120,000, and in Zurich those with taxable wealth of at least CHF 80,000 (single; CHF 160,000 jointly taxed) or other income of at least CHF 3,000 not taxed at source, are moved into an ordinary assessment ([ZStB 133.1, A.III](https://www.zh.ch/content/dam/zhweb/bilder-dokumente/themen/steuern-finanzen/steuern/vertreter/steuerbuch/zstb-nr-133-1/ZStB-Nr-133-1_Aufforderung-2027.pdf)). Details: `ch-payroll`, `ch-cross-border`.
- **Non-residents** with Swiss real estate or a Swiss business file in the canton where it is (StHG art. 4 para. 1; ZStB 133.1, A.I.1 let. d).

## Worked examples

### Example 1: single person in Zurich city, taxable income CHF 100,000 (2026)

Facts: Anna is single, has no children, lives in the city of Zurich all year and belongs to the reformed church. Her taxable income for cantonal tax, after all deductions, is CHF 100,000. Wealth tax is left out.

- Simple tax from the Zurich Grundtarif (§ 35 para. 1 StG, 2026): 0% on 7,000; 2% on 5,000 = 100; 3% on 4,800 = 144; 4% on 8,000 = 320; 5% on 9,700 = 485; 6% on 11,200 = 672; 7% on 13,100 = 917; 8% on 17,600 = 1,408. That reaches CHF 76,400. The remaining CHF 23,600 falls in the 9% band: 2,124. Simple tax CHF 6,170.
- Cantonal tax: 95% x 6,170 = CHF 5,861.50.
- Communal tax, city of Zurich: 119% x 6,170 = CHF 7,342.30.
- Church tax, reformed: 10% x 6,170 = CHF 617.00.
- Total cantonal, communal and church tax: CHF 13,820.80, or 13.82% of taxable income. Without church membership: CHF 13,203.80.

Federal income tax comes on top (`ch-federal-income-tax`).

```oa-check
name: Zurich city, single, taxable income CHF 100,000, reformed church (2026)
inputs:
  income: 100000
  canton_pct: 95
  city_pct: 119
  church_pct: 10
steps:
  - b2: max(0, min(income, 12000) - 7000) * 0.02
  - b3: max(0, min(income, 16800) - 12000) * 0.03
  - b4: max(0, min(income, 24800) - 16800) * 0.04
  - b5: max(0, min(income, 34500) - 24800) * 0.05
  - b6: max(0, min(income, 45700) - 34500) * 0.06
  - b7: max(0, min(income, 58800) - 45700) * 0.07
  - b8: max(0, min(income, 76400) - 58800) * 0.08
  - b9: max(0, min(income, 110400) - 76400) * 0.09
  - b10: max(0, min(income, 144100) - 110400) * 0.10
  - simple_tax: b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10
  - cantonal_tax: round(pct(simple_tax, canton_pct), 2)
  - communal_tax: round(pct(simple_tax, city_pct), 2)
  - church_tax: round(pct(simple_tax, church_pct), 2)
  - total: cantonal_tax + communal_tax + church_tax
  - total_without_church: cantonal_tax + communal_tax
  - effective_pct: round(total / income * 100, 2)
expected:
  simple_tax: 6170.00
  cantonal_tax: 5861.50
  communal_tax: 7342.30
  church_tax: 617.00
  total: 13820.80
  total_without_church: 13203.80
  effective_pct: 13.82
```

The edge case: the church multiplier depends on the parish, not only the commune. A Christian Catholic in Zurich city pays 14%, not 10%. Leaving the church during the year changes the church tax; the Zurich rule for the cut-off date was not read for this skill.

### Example 2: the same income in Zug city (2026)

Facts: as example 1, but Anna lives in the city of Zug all year and is Roman Catholic. Taxable income for Zug cantonal tax is CHF 100,000. (In practice Zug's taxable income would differ from Zurich's for the same gross pay, because Zug's deductions differ, for example its personal deduction of CHF 12,000. The example holds taxable income equal to compare tariffs and multipliers.)

- Simple tax from the Zug Grundtarif 2026: the bands up to CHF 94,800 give CHF 5,114.50 (Zug tax office table). The next CHF 5,200 is in the 10% band: 520. Simple tax CHF 5,634.50.
- Cantonal tax: 78% x 5,634.50 = CHF 4,394.91.
- Communal tax, city of Zug: 52% x 5,634.50 = CHF 2,929.94.
- Church tax, Roman Catholic parish of Zug: 5.95% x 5,634.50 = CHF 335.25.
- Total: CHF 7,660.10, or 7.66% of taxable income.

Against Zurich city (example 1) that is CHF 6,160.70 less on the same taxable income. Two things drive it: the Zug simple tax is lower (CHF 5,634.50 against CHF 6,170), and the multipliers add up to 135.95% in Zug against 224% in Zurich.

```oa-check
name: Zug city, single, taxable income CHF 100,000, Roman Catholic (2026)
inputs:
  income: 100000
  canton_pct: 78
  city_pct: 52
  church_pct: 5.95
  zurich_total: 13820.80
steps:
  - b1: min(income, 1100) * 0.005
  - b2: max(0, min(income, 3300) - 1100) * 0.01
  - b3: max(0, min(income, 6100) - 3300) * 0.02
  - b4: max(0, min(income, 10100) - 6100) * 0.03
  - b5: max(0, min(income, 15300) - 10100) * 0.0325
  - b6: max(0, min(income, 21100) - 15300) * 0.035
  - b7: max(0, min(income, 26900) - 21100) * 0.04
  - b8: max(0, min(income, 34900) - 26900) * 0.045
  - b9: max(0, min(income, 46400) - 34900) * 0.055
  - b10: max(0, min(income, 59700) - 46400) * 0.055
  - b11: max(0, min(income, 74700) - 59700) * 0.065
  - b12: max(0, min(income, 94800) - 74700) * 0.08
  - b13: max(0, min(income, 120100) - 94800) * 0.10
  - simple_tax: b1 + b2 + b3 + b4 + b5 + b6 + b7 + b8 + b9 + b10 + b11 + b12 + b13
  - cantonal_tax: round(pct(simple_tax, canton_pct), 2)
  - communal_tax: round(pct(simple_tax, city_pct), 2)
  - church_tax: round(pct(simple_tax, church_pct), 2)
  - total: cantonal_tax + communal_tax + church_tax
  - effective_pct: round(total / income * 100, 2)
  - total_multiplier_pct: canton_pct + city_pct + church_pct
  - saving_vs_zurich: zurich_total - total
expected:
  simple_tax: 5634.50
  cantonal_tax: 4394.91
  communal_tax: 2929.94
  church_tax: 335.25
  total: 7660.10
  effective_pct: 7.66
  total_multiplier_pct: 135.95
  saving_vs_zurich: 6160.70
```

The edge case: Zug's city multiplier was 52.11% in 2025 (54% less a 3.5% rebate) and is 52% for 2026; the ESTV capital-city table still prints the 2025 figure. Always take the multiplier for the right year from the canton's own list.

## Ask the client first

1. Where did the client live on 31 December 2026: canton, commune, and parish? Any move during the year?
2. Single, married or registered partners, or a single parent living with children? The tariff and deductions depend on it.
3. Church membership of each spouse (reformed, Roman Catholic, Christian Catholic, none), and any exit during the year.
4. Real estate or a business in another canton or abroad.
5. Permit and tax at source status: C permit or Swiss, or taxed at source with pay of more than CHF 120,000?
6. Net wealth at 31 December 2026, and any pension lump sum paid in 2026.

## Sources

| Source | URL | Read on |
|---|---|---|
| StHG, SR 642.14, version of 1 January 2025 (latest consolidated version on Fedlex), art. 1 to 4b, 7, 9, 11, 13 to 17, 42, 55 to 57 | https://www.fedlex.admin.ch/eli/cc/1991/1256_1256_1256/de | 2026-10-23 |
| ESTV, Steuersatz und Steuerfuss (law as at 1 January 2026), sections 3.1, 3.3.1 and table 3.4.1 (multipliers in the cantonal capitals 2026) | https://www.estv2.admin.ch/stp/ds/e-steuersatz-steuerfuss-de.pdf | 2026-10-23 |
| ESTV, Kantonsblatt Zürich (February 2026), § 2, 16, 20, 26, 31, 34, 35, 37, 47 StG | https://www.estv2.admin.ch/stp/kb/zh-de.pdf | 2026-10-23 |
| ESTV, Kantonsblatt Zug (February 2026), § 2, 25, 30, 33, 35, 37, 44 StG | https://www.estv2.admin.ch/stp/kb/zg-de.pdf | 2026-10-23 |
| ESTV, Kantonsblatt Bern (February 2026), art. 31, 38, 65 StG | https://www.estv2.admin.ch/stp/kb/be-de.pdf | 2026-10-23 |
| ESTV, Kantonsblatt Basel-Stadt (February 2026), § 27, 32, 36a, 49 StG | https://www.estv2.admin.ch/stp/kb/bs-de.pdf | 2026-10-23 |
| ESTV, Feuille cantonale Genève (February 2026), art. 29, 35, 58 LIPP; RCEPF 2026 | https://www.estv2.admin.ch/stp/kb/ge-fr.pdf | 2026-10-23 |
| ESTV, Feuille cantonale Vaud (February 2026), art. 30, 37 LI; wealth threshold | https://www.estv2.admin.ch/stp/kb/vd-fr.pdf | 2026-10-23 |
| Stadt Zürich, Steuerberechnung und Steuerfuss (2026 multipliers) | https://www.stadt-zuerich.ch/de/lebenslagen/steuern/natuerliche-personen/steuerberechnung.html | 2026-10-23 |
| Kantonales Steueramt Zürich, ZStB 133.1, Aufforderung 2027 (2026 returns) | https://www.zh.ch/content/dam/zhweb/bilder-dokumente/themen/steuern-finanzen/steuern/vertreter/steuerbuch/zstb-nr-133-1/ZStB-Nr-133-1_Aufforderung-2027.pdf | 2026-10-23 |
| Kantonales Steueramt Zürich, Wegleitung zur Steuererklärung 2026 (part-year), payment, interest and penalties | https://www.zh.ch/content/dam/zhweb/bilder-dokumente/themen/steuern-finanzen/steuern/natuerlichepersonen/2026/est-wegleitungen-uj/305%20Wegleitung%20ZH%202026%20UJ%20bf.pdf | 2026-10-23 |
| Steuerverwaltung Zug, Steuerfüsse der Gemeinden 2023 to 2026 (21 January 2026) | https://zg.ch/dam/jcr:24fb8832-3383-4718-9a48-9461bc7501fc/Steuerf%C3%BCsse%202026_effektiv%2021.1.26.pdf | 2026-10-23 |
| Steuerverwaltung Zug, Kantonssteuer Grundtarif gültig Steuerperiode 2026 | https://zg.ch/dam/jcr:96c7eef4-eb2f-4f8a-a4c4-dad209249598/Grundtarif%202001%20bis%202026.pdf | 2026-10-23 |
| Kanton Zug, vote explanation, Steuergesetz change of 30 November 2025 (multiplier 78% for 2026 to 2029) | https://cdn.zg.ch/dam/jcr:09c43d5c-61d7-4ca1-b825-62f5cba55fba/20251130_Erl%C3%A4uterung%20KA2_%C3%84nderung_Steuergesetz-9_UA.pdf | 2026-10-23 |
| Kanton Zug, eTax.zug 2025 (filing deadline 30 April 2026) | https://zg.ch/news/news~_2026_2_etax-zug-2025-neue-deklarationsloesung-fuer-natuerliche-personen-ist-online~.html | 2026-10-23 |
| Steuerverwaltung Bern, TaxInfo, Abgabefrist | https://www.taxinfo.sv.fin.be.ch/taxinfo/1cce120a-05da-45e8-8968-b66ae236fee5 | 2026-10-23 |
| Kanton Bern, media release on the 2025 returns | https://www.be.ch/de/start/dienstleistungen/medien/medienmitteilungen.html?newsID=68239ab2-4062-4a28-a910-4a9b7bd0dbf4 | 2026-10-23 |
| Kanton Basel-Stadt, Steuererklärung als natürliche Person einreichen | https://www.bs.ch/themen/arbeit-und-steuern/steuererklaerung/steuererklaerung-als-natuerliche-person-einreichen | 2026-10-23 |
| République et canton de Genève, Remplir ma déclaration d'impôt | https://www.ge.ch/remplir-ma-declaration-impot-tant-que-particulier | 2026-10-23 |
| Canton de Vaud, Demander un délai pour déposer ma déclaration d'impôt | https://www.vd.ch/etat-droit-finances/impots/impots-pour-les-individus/demander-un-delai-pour-deposer-ma-declaration-dimpot | 2026-10-23 |
| BSV, Wichtige Masszahlen berufliche Vorsorge 2025/2026, no. 9 (pillar 3a) | https://www.bsv.admin.ch/dam/de/sd-web/GZplHByBJoFc/Internet_Masszahlenarticles_25_26_d.pdf | 2026-10-23 |

Not yet confirmed: the 2026 filing dates for Zug, Basel-Stadt and Bern (only the 2025-return dates were published; the rules suggest 30 April, 31 March and 15 March / 15 May 2027); filing dates for the other 20 cantons; the 2026 multipliers of Solothurn, Appenzell Innerrhoden and other communes not in the tables; whether Basel-Stadt and Bern indexed any deduction for 2026 beyond the amounts shown in the February 2026 Kantonsblätter; the Geneva, Vaud, Bern and Basel-Stadt 2026 income tariffs (not worked here); the Vaud commuting rules beyond the flat rates; due dates, instalments and interest rates outside Zurich; the Zurich rule for church tax when someone leaves the church during the year; ESTV footnote detail for Basel-Landschaft church tax and the Geneva 12% deduction.
