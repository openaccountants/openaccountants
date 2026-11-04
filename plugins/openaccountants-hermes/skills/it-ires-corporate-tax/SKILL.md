---
name: it-ires-corporate-tax
description: "Italian corporate income tax (IRES) for tax year 2026: resident companies (S.p.A., S.r.l., cooperatives, commercial entities) and Italian permanent establishments of foreign companies. Covers the 24% rate, the 2025-only reduced 20% rate (IRES premiale) and why it does not apply to 2026, the bank surcharge, the taxable base and main add-backs, the 30% ROL interest limit, the 95% participation exemption and dividend exclusion, the 80% loss carry-forward limit, the domestic tax group (consolidato nazionale), Modello Redditi SC filing, acconti and saldo dates, penalties and ravvedimento operoso, outbound withholding (26%, 1.2%, parent-subsidiary exemption), CFC and exit tax. Trigger on: IRES, imposta sul reddito delle società, Italian corporate tax, Redditi SC, acconto IRES, PEX Italy, consolidato fiscale, perdite pregresse, ROL. Out of scope: IRAP (it-irap), individuals (it-income-tax), transfer pricing (italy-transfer-pricing), VAT (italy-vat-return)."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/it-ires-corporate-tax"
  jurisdiction: "IT"
  tax_year: "2026"
  last_updated: "2026-10-23"
  authored_by: "Ryan Duguid"
  trust_label: "Accountant-authored"
  review_status: "pending_review"
---

# Italian corporate income tax (IRES): tax year 2026

> **General reference only.** This skill is general tax reference material for AI-assisted work. It has not been reviewed for any specific company's facts. Do not rely on it to file, pay or take a position without review by a qualified professional in Italy.

**Tax year.** IRES is charged per tax period (periodo d'imposta), which is the company's financial year. Most companies use the calendar year, so "2026" here means the period 1 January to 31 December 2026. The return for that period is filed in 2027.

**The law is moving in 2027.** The rules below are in the Testo unico delle imposte sui redditi, D.P.R. 917/1986 (TUIR). On Normattiva, TUIR arts. 1 to 191 are shown as in force until 31 December 2026. A new consolidated income tax code, D.Lgs. 19 June 2026 n. 117, came into force on 4 July 2026, and its art. 377 says its provisions apply from 1 January 2027 ([D.Lgs. 117/2026](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-06-19;117)). The same is true of the payment and withholding code (D.Lgs. 33/2025, art. 243: from 1 January 2027) and the penalty code (D.Lgs. 173/2024, which repeals D.Lgs. 471/1997 from 1 January 2027). This skill cites the TUIR article numbers that govern the 2026 tax period. Expect new article numbers in the 2027 software and instructions; whether the new code changes anything of substance for the 2026 return has not been checked here.

**Sibling skills.** IRAP, the regional tax on productive activity, is a second tax on the same company and is covered in [it-irap](it-irap.md). Transfer pricing documentation is in [italy-transfer-pricing](italy-transfer-pricing.md). Statutory accounts, which are the starting point for IRES, are in [italy-financial-statements](italy-financial-statements.md). Entity choice is in [italy-formation](italy-formation.md).

## Who this applies to

**Taxpayers (TUIR art. 73(1)).** IRES is charged on:
- (a) resident S.p.A., S.a.p.a., S.r.l. (including S.r.l.s.), cooperatives, mutual insurers, European companies and European cooperatives;
- (b) resident public and private entities, and trusts, whose sole or main object is a commercial activity;
- (c) resident entities and trusts with no main commercial object, and resident investment funds (OICR);
- (d) non-resident companies and entities of any kind, on their Italian-source income.

**Residence of a company (art. 73(3)).** A company is resident if, for the greater part of the tax period, it has in Italy its legal seat, its place of effective management (sede di direzione effettiva: the continuous and coordinated taking of strategic decisions for the company as a whole) or its ordinary management (gestione ordinaria: the continuous and coordinated carrying out of day-to-day management acts). This wording applies from the 2024 tax period (D.Lgs. 209/2023, art. 7(2), printed as note 227 to art. 73). Art. 73(5-bis) adds a rebuttable presumption of residence for foreign holding companies controlled from Italy; read it if the client has one.

**Permanent establishments of non-residents (arts. 151 and 152).** A foreign company is taxed only on income produced in Italy. Business income of an Italian permanent establishment (stabile organizzazione) is computed under the same rules as a resident company, on a separate profit and loss account and balance sheet for the PE, which is treated as a separate and independent entity.

**Out of scope here.**
- Partnerships (s.n.c., s.a.s., società semplici): transparent, taxed on the partners (TUIR art. 5; return Modello Redditi SP).
- Individuals and sole traders: IRPEF, see [it-income-tax](it-income-tax.md).
- Non-commercial entities filing Modello Redditi ENC, banks' and insurers' special base rules, REITs (SIIQ), tonnage tax, and companies under the biennial arrangement (concordato preventivo biennale). Refer these.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| IRES standard rate | 24% of total net income | 2026 | [TUIR art. 77](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art77!vig=2026-10-22) |
| IRES premiale (reduced rate) | 24% cut by 4 points to 20%, on conditions | 2025 only (the period after the one in progress at 31 Dec 2024). Not available for 2026 | [L. 207/2024, art. 1(436)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1-com436!vig=2026-10-22); [Redditi SC 2026 instructions](https://www.agenziaentrate.gov.it/portale/documents/20143/9962362/SC_istr_2026.pdf/7c2fd2b6-6264-88eb-5c92-9d9ecf81e2c4?t=1779895444801) |
| IRES surcharge, financial intermediaries (fund management companies and SIMs excluded) and Banca d'Italia | +3.5 percentage points on the art. 77 rate | 2026 | L. 208/2015, art. 1(65), printed as notes 181 and 192 to [TUIR art. 77](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art77!vig=2026-10-22) |
| IRAP standard rate (separate regional tax, regions may vary it) | 3.9% of net value of production | 2026 (rate printed in the 2026 IRAP instructions) | [it-irap](it-irap.md); [IRAP 2026 instructions](https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414) |
| Participation exemption on gains (PEX) | 95% of the gain exempt | 2026 | [TUIR art. 87](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art87!vig=2026-10-22) |
| Dividends received from resident companies | 95% excluded, 5% taxed | 2026 | [TUIR art. 89(2)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art89!vig=2026-10-22) |
| Loss carry-forward cap | 80% of each later year's taxable income; no time limit | 2026 | [TUIR art. 84(1)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art84!vig=2026-10-22) |
| Losses of the first three tax periods | Usable in full against later income, if they relate to a new productive activity | 2026 | [TUIR art. 84(2)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art84!vig=2026-10-22) |
| Net interest expense deduction limit | 30% of tax ROL (gross operating result); unused ROL carried forward 5 periods | 2026 | [TUIR art. 96(2), (4), (7)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art96!vig=2026-10-22) |
| Company cars not used exclusively in the business | 20% of costs deductible | 2026 | [TUIR art. 164(1)(b)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art164!vig=2026-10-22) |
| Telephone and electronic communication devices | 80% of costs deductible | 2026 | [TUIR art. 102(9)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art102!vig=2026-10-22) |
| Assets costing up to EUR 516.46 each | Deductible in full in the year of purchase | 2026 | [TUIR art. 102(5)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art102!vig=2026-10-22) |
| Entertainment (spese di rappresentanza) cap | 1.5% of revenue to EUR 10m; 0.6% from EUR 10m to 50m; 0.4% above EUR 50m | 2026 | [TUIR art. 108(2)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art108!vig=2026-10-22) |
| Acconto (advance) on IRES | 100% of prior-year tax, 40% first instalment and 60% second (50% and 50% for businesses in an activity with approved ISA indices whose revenue is not above the limit set in that ISA's approval decree, D.L. 124/2019 art. 58(1)) | 2026 | [Redditi 2026 general instructions, 4.2](https://www.agenziaentrate.gov.it/portale/documents/20143/9771542/Parte_Generale_istr_2026.pdf/2ad66f68-6f28-a982-8570-c130cdcdddfa?t=1772195389363) |
| Acconto not due if prior-year tax is not above | EUR 20.66 | 2026 | Same, 4.2 |
| Single acconto instalment if the first instalment would not exceed | EUR 103 | 2026 | Same, 4.2 (DPR 435/2001 art. 17(3)) |
| Interest for paying within 30 days after the deadline | 0.40% | 2026 | Same, 4.1 (DPR 435/2001 art. 17(2)) |
| Pillar Two | 15% minimum tax (IIR, UTPR, domestic minimum tax) for groups with consolidated revenue of EUR 750m or more in at least two of the four previous years | in force since 2024 under D.Lgs. 209/2023 | [D.Lgs. 117/2026, TU arts. 310 and 334](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-06-19;117), which carry over D.Lgs. 209/2023 arts. 10 and 34 |

**The reduced 20% rate in detail, and why it matters in 2026.** For the 2025 tax period only, L. 207/2024 art. 1(436)-(444) let a company apply 20% instead of 24% if it (a) set aside at least 80% of its 2024 profit in a reserve, (b) invested at least 30% of that reserve, and at least 24% of the 2023 profit, in new 4.0 / 5.0 capital goods located in Italy, at least EUR 20,000, between 1 January 2025 and the 2025 return deadline, (c) did not reduce headcount against the previous three-year average and hired permanent staff equal to at least 1% of the 2024 average (minimum one person), and (d) used no wage-subsidy scheme (cassa integrazione) in 2024 or 2025, with a narrow exception. Two things carry into 2026:
- **Clawback.** The benefit is lost if the reserve is distributed by the end of the second financial year after 2024, that is during 2026 for a calendar-year company, or if the assets are disposed of or moved abroad within five tax periods after the investment (art. 1(438)).
- **Acconti for 2026.** The 2026 acconti are computed on the 2025 tax as if the reduced rate had not been used (art. 1(443); general instructions 4.2).

The 2026 budget law (L. 199/2025) did not renew the reduced rate. A read of all its commi on 2026-10-22 found no IRES rate change for 2026. It did change the base: from the 2026 tax period, gains on business assets other than PEX shareholdings are taxed in full in the year realised, and spreading over up to five years survives only for the sale of a business or business unit held for at least three years (TUIR [art. 86(4)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art86!vig=2026-10-22) as replaced by L. 199/2025 art. 1(42) and (43)). The super-depreciation of L. 199/2025 art. 1(427)-(436) is outside this skill.

**Recomputing the 2025 tax for the 2026 acconti.** On top of the IRES premiale adjustment above, the 2025 tax used for the 2026 acconti is recomputed as if the new art. 86(4) had applied in 2025 (so a 2025 gain spread over five years counts in full), and without the super-depreciation of L. 199/2025 art. 1(427)-(436) (L. 199/2025 art. 1(43) and (434); general instructions 4.2). The instructions also list commi 51, 56 and 57: comma 51 was repealed by D.L. 38/2026, and commi 56 and 57 concern banks' credit write-downs.

**What the 2026 budget law tried, and what is now in force.** L. 199/2025 art. 1(51)-(55) narrowed the 95% dividend exclusion and the PEX to holdings meeting new minimum requirements, from 1 January 2026. D.L. 38/2026 art. 11 repealed those commi and restored the previous regime, with effect from 1 January 2026 ([D.L. 38/2026 art. 11](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2026-03-27;38~art11!vig=2026-10-22)). For 2026 the 95% rules apply as they did in 2025.

## The taxable base

**Start from the accounts (TUIR art. 83).** Taxable income is the profit or loss in the income statement, adjusted by the TUIR rules. Companies reporting under IFRS, and companies reporting under the civil code other than micro-companies (art. 2435-ter civil code), take the accounting qualification, timing and classification of items as given ("derivazione rafforzata"), even where later TUIR articles say otherwise, subject to specific exceptions. The working paper is quadro RF of Modello Redditi SC: profit, plus increases (variazioni in aumento), less decreases (variazioni in diminuzione).

**Main add-backs (variazioni in aumento).**
- IRES itself and other income taxes are not deductible (art. 99(1)). Other taxes are deductible in the year paid.
- Company cars: 80% of costs added back where the car is not used exclusively in the business (art. 164(1)(b)). Sales agents' cars and cars assigned to employees follow other percentages in art. 164.
- Telephones: 20% of costs added back (art. 102(9)).
- Entertainment above the art. 108(2) cap.
- Directors' fees not paid in the year: deductible only when paid (art. 95(5)).
- Depreciation above the ministerial coefficients, which are halved in the first year (art. 102(2)).
- Net interest expense above the art. 96 limit (below).
- IRAP: not deductible except for the partial deductions covered in [it-irap](it-irap.md).

**Main deductions (variazioni in diminuzione).**
- 95% of dividends from resident companies (art. 89(2)). Dividends from companies in privileged tax regimes are taxed in full or at 50%, depending on what the taxpayer can show (art. 89(3)).
- 95% of qualifying gains on shareholdings (PEX, art. 87). All four conditions must hold: (a) held without interruption from the first day of the twelfth month before the sale; (b) classified as a financial fixed asset in the first balance sheet of the holding period; (c) the subsidiary is not resident in a privileged tax regime, or the taxpayer proves the condition in art. 47-bis(2)(b); (d) the subsidiary runs a commercial business. Condition (c) must hold from the start of the holding (for holdings of more than five periods sold outside the group, the five periods before the sale are enough); condition (d) must hold from the start of the third tax period before the sale (art. 87(2)).
- Tax losses brought forward (below).
- Acconti and tax credits are not deductions; they reduce the tax.

**Interest limitation (art. 96).** Net interest expense (interest expense less interest income) is deductible up to 30% of the tax ROL of the year, plus 30% of ROL carried forward from earlier years. ROL is value of production less costs of production (art. 2425 civil code, lines A and B), excluding depreciation (B10a and B10b) and finance-lease payments, measured under the tax rules. Disallowed interest carries forward without time limit; unused 30% ROL carries forward for five tax periods (art. 96(5) and (7)). Excess interest income also carries forward (art. 96(6)).

**Losses (art. 84).**
- An ordinary loss carries forward without time limit, but in each later year it can absorb only 80% of that year's taxable income (art. 84(1)).
- Losses of the first three tax periods from incorporation can absorb 100% of later income, if they relate to a new productive activity (art. 84(2)).
- There is no carry-back.
- Change of control: losses are lost if the majority of voting rights is transferred and the main activity actually carried on changes, in the period of transfer or the two before or after (art. 84(3)). D.Lgs. 148/2026 art. 7(1) says a transfer of a controlling parent counts as a transfer (note 250 to art. 84). The vitality test in art. 84(3-bis) and the equity cap in art. 84(3-ter) can save the losses. The same rule applies to carried-forward interest under art. 96 (art. 84(3-quater)).

**Domestic tax group, consolidato nazionale (arts. 117 to 129).** A resident parent and its resident S.p.A., S.a.p.a. and S.r.l. subsidiaries in which it holds more than 50% of capital and profits, directly or through the chain (art. 120), can opt jointly for group taxation. IRES is then computed by the parent on the algebraic sum of the members' incomes and losses. The option runs for three financial years, is irrevocable and is tacitly renewed every three years unless revoked (art. 117(3)). A foreign parent can be the head of the group through an Italian PE (art. 117(2)), and an EU/EEA parent can designate an Italian subsidiary to head it (art. 117(2-bis)). In a group only the parent pays the acconti (general instructions 4.2).

## Deadlines and filing

| Step | Deadline, calendar-year company | Rule |
|---|---|---|
| First acconto for 2026 (40% of 2025 tax, or 50% for ISA taxpayers) | 30 June 2026 | Last day of the sixth month after the end of the previous tax period, same day as the 2025 balance (DPR 435/2001 art. 17(1); general instructions 4.1, 4.2) |
| Late option for the first acconto and the balance | Up to 30 days later, adding 0.40% | DPR 435/2001 art. 17(2) |
| Second acconto for 2026 (60%, or 50% for ISA taxpayers) | 30 November 2026 | Last day of the eleventh month of the tax period (general instructions 4.2(b)) |
| Balance (saldo) for 2026, and first acconto for 2027 | 30 June 2027 | DPR 435/2001 art. 17(1) |
| Return for 2025 (Modello Redditi SC 2026) | 2 November 2026 | Last day of the tenth month after year end; 31 October 2026 is a Saturday (general instructions 3.1; DPR 322/1998 art. 2(2)) |
| Return for 2026 (Modello Redditi SC 2027) | Last day of the tenth month: 31 October 2027 is a Sunday and 1 November a public holiday, so expect 2 November 2027 | DPR 322/1998 art. 2(2). Not yet confirmed by the 2027 instructions |

- **Non-calendar years.** For a period 1 July 2025 to 30 June 2026 the return is due 30 April 2027 (general instructions 3.1).
- **Late approval of accounts.** Companies that by law approve their accounts more than four months after year end pay by the last day of the month after approval (general instructions 4.1).
- **Weekend rule.** A payment deadline falling on a Saturday or public holiday moves to the next working day (general instructions 4.1).
- **Form and channel.** Modello Redditi SC, filed electronically, usually through an authorised intermediary. Payment by F24, which VAT-registered businesses must make online (general instructions 4.1). The return can be filed from 15 April after a calendar year ends (general instructions 3.1).
- **90-day grace.** A return filed within 90 days after the deadline is valid but penalised. After 90 days it counts as not filed, although the tax shown on it can still be collected (general instructions 3.1).
- **Amounts of EUR 12 or less** for each tax are not paid (general instructions 4.1).

## Penalties and interest

These are the rules of D.Lgs. 471/1997 and D.Lgs. 472/1997 as revised by D.Lgs. 87/2024, which apply to violations committed from 1 September 2024 (note 40 to D.Lgs. 471/1997 art. 1).

| Violation | Penalty | Source |
|---|---|---|
| Return not filed | 120% of the tax due, minimum EUR 250; EUR 250 to 1,000 if no tax is due (may be doubled for companies that keep accounts) | [D.Lgs. 471/1997 art. 1(1)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-10-22) |
| Return filed more than 90 days late but before any audit starts | The late-payment penalty of art. 13(1) (25%) tripled, on the tax due | art. 1(1-bis) |
| Understated income or tax (dichiarazione infedele) | 70% of the extra tax, minimum EUR 150 | art. 1(2) |
| Late or missing payment of acconti or balance | 25% of the unpaid amount; 12.5% if paid within 90 days; within 15 days, 1/15 of the 12.5% per day late | [D.Lgs. 471/1997 art. 13(1)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-10-22) |

**Ravvedimento operoso (voluntary correction, D.Lgs. 472/1997 art. 13).** For taxes administered by the Agenzia delle Entrate, such as IRES, the correction stays open until an assessment or a liquidation notice (DPR 600/1973 arts. 36-bis and 36-ter) is served, even if an audit has started (art. 13(1-ter)); later fractions (1/6, 1/5, 1/4) apply once a verbale or a draft assessment (schema di atto) has been issued. Otherwise the penalty is cut to a fraction of the minimum: 1/10 if a missed payment is made within 30 days; 1/9 within 90 days; 1/8 by the return deadline for the year of the violation; 1/7 after that; 1/10 of the minimum for a return filed up to 90 days late. The tax, the reduced penalty and interest at the legal rate, accruing day by day, are paid together ([D.Lgs. 472/1997 art. 13(2)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-10-22)). The legal rate (civil code art. 1284) is 1.60% a year from 1 January 2026, down from 2% in 2025, so days in 2025 accrue at 2% and days in 2026 at 1.60% ([MEF decree 10 December 2025, GU n. 289 of 13 December 2025](https://www.gazzettaufficiale.it/eli/id/2025/12/13/25A06705/sg)).

The interest rate on tax assessed after an audit was not fetched for this skill; see "Not yet confirmed".

## Cross-border points

**Withholding on outbound payments, domestic law (DPR 600/1973).** Treaty rates can be lower; apply the treaty only with the documents the treaty requires.

| Payment to a non-resident without an Italian PE | Withholding | Source |
|---|---|---|
| Dividends, general rate | 26%, final | [DPR 600/1973 art. 27(3)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1973-09-29;600~art27!vig=2026-10-22), with the rate set at 26% by [D.L. 66/2014 art. 3(1)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2014-04-24;66~art3!vig=2026-10-22) |
| Dividends to companies subject to corporate tax in, and resident in, an EU or listed EEA state | 1.2%, final | DPR 600/1973 art. 27(3-ter), as replaced by D.L. 38/2026 art. 11(2) |
| Dividends under the Parent-Subsidiary Directive | Exempt on request (or refund) if the EU parent holds directly at least 10% for at least one year, has a form listed in the directive and is subject to one of its taxes | [DPR 600/1973 art. 27-bis](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1973-09-29;600~art27bis!vig=2026-10-22); the 10% comes from D.Lgs. 49/2007 art. 2(2), printed as note 97 |
| Interest | 26%, final (art. 26(5) charges 12.5%, raised to 26% by D.L. 66/2014 art. 3(1)); many exemptions, for example medium and long-term loans from EU banks (art. 26(5-bis)) | [DPR 600/1973 art. 26](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1973-09-29;600~art26!vig=2026-10-22) |
| Royalties | 30% on the taxable part, final | [DPR 600/1973 art. 25(4)](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1973-09-29;600~art25!vig=2026-10-22) |
| Interest and royalties under the Interest and Royalties Directive | Exempt where a 25% direct voting link exists between associated EU companies and the other conditions are met | [DPR 600/1973 art. 26-quater](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1973-09-29;600~art26quater!vig=2026-10-22) |

**CFC rules (TUIR art. 167).** An Italian company that controls a foreign company or PE includes the foreign entity's income in its own, in proportion to its holding, if both: (a) the foreign entity's effective tax rate is below 15% (on audited accounts; otherwise, or if below 15%, the test is whether it is taxed at less than half the Italian rate it would pay as a resident), and (b) more than one third of its income is passive (interest, royalties, dividends and gains on shares, financial leasing, insurance, banking and other financial income, and intra-group sales or services with little or no added value). The rules do not apply if the company shows the foreign entity carries on a real economic activity with staff, equipment, assets and premises (art. 167(5)). See [TUIR art. 167](https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art167!vig=2026-10-22).

**Exit tax (TUIR art. 166).** A company that moves its tax residence abroad, transfers assets to an exempt foreign PE, moves an Italian PE or its assets abroad, or is merged into or split in favour of a non-resident company is taxed on the market value of the assets less their tax value. If the move is to an EU or listed EEA state, the tax can be paid in five equal annual instalments, with guarantees where required (art. 166(9)).

**Pillar Two.** See the rates table. Refer in-scope groups.

**Transfer pricing.** Related-party prices must be arm's length (TUIR art. 110(7)); documentation and penalty protection are in [italy-transfer-pricing](italy-transfer-pricing.md).

## Worked examples

### Example 1: a trading S.r.l., calendar year 2026

Facts (invented): Alfa S.r.l. is an Italian trading company, not an ISA taxpayer, not in a tax group, no losses brought forward. Its 2026 accounts show profit before tax of EUR 300,000. Within that: car costs of EUR 10,000 for cars not used exclusively in the business; telephone costs of EUR 5,000; a dividend of EUR 40,000 from an Italian subsidiary. Its IRES for 2025 was EUR 60,000, computed at 24% (it did not claim the reduced rate). Net interest is within the 30% ROL limit.

Walk-through:
1. Add back 80% of the car costs: 10,000 x 80% = 8,000 (art. 164).
2. Add back 20% of the telephone costs: 5,000 x 20% = 1,000 (art. 102(9)).
3. Deduct 95% of the dividend: 40,000 x 95% = 38,000 (art. 89(2)).
4. Taxable income: 300,000 + 8,000 + 1,000 - 38,000 = 271,000.
5. IRES at 24%: 65,040.
6. Acconti paid during 2026, on the 2025 tax of 60,000: 24,000 by 30 June 2026 and 36,000 by 30 November 2026.
7. Balance due 30 June 2027: 65,040 - 60,000 = 5,040. On the same day the first acconto for 2027 falls due: 40% of 65,040 = 26,016. The second acconto for 2027, 39,024, is due 30 November 2027.

IRAP is computed separately on the value of production (see [it-irap](it-irap.md)); this example leaves out IRAP and its partial deductions from IRES.

```oa-check
name: Alfa S.r.l., trading company, IRES 2026 at 24% with acconti
inputs:
  profit_before_tax: 300000
  car_costs: 10000
  phone_costs: 5000
  dividend_received: 40000
  ires_2025: 60000
steps:
  - car_addback: car_costs * 0.80
  - phone_addback: phone_costs * 0.20
  - dividend_exclusion: dividend_received * 0.95
  - taxable_income: profit_before_tax + car_addback + phone_addback - dividend_exclusion
  - ires_2026: taxable_income * 0.24
  - acconto_1_2026: ires_2025 * 0.40
  - acconto_2_2026: ires_2025 - acconto_1_2026
  - saldo_2026: ires_2026 - acconto_1_2026 - acconto_2_2026
  - acconto_1_2027: ires_2026 * 0.40
  - acconto_2_2027: ires_2026 - acconto_1_2027
expected:
  taxable_income: 271000
  ires_2026: 65040
  acconto_1_2026: 24000
  acconto_2_2026: 36000
  saldo_2026: 5040
  acconto_1_2027: 26016
  acconto_2_2027: 39024
```

### Example 2: losses brought forward and the interest limit

Facts (invented): Beta S.p.A. was incorporated in 2015. It has EUR 250,000 of ordinary tax losses from 2023 (not first-three-year losses) and no change of control. In 2026 its profit before tax is EUR 170,000, after net interest expense of EUR 150,000. Its tax ROL for 2026 is EUR 400,000 and it has no ROL or interest carried forward. There are no other adjustments.

Walk-through:
1. Interest limit: 30% x 400,000 = 120,000. Net interest of 150,000 exceeds it by 30,000, which is added back and carried forward (art. 96(2) and (5)).
2. Income before losses: 170,000 + 30,000 = 200,000.
3. Loss cap: 80% x 200,000 = 160,000. The 2023 losses are larger, so 160,000 is used (art. 84(1)).
4. Taxable income: 200,000 - 160,000 = 40,000. IRES at 24%: 9,600.
5. Carried forward to 2027: losses of 250,000 - 160,000 = 90,000, and disallowed interest of 30,000.

If the losses had arisen in Beta's first three tax periods from a new productive activity, the 80% cap would not apply (art. 84(2)): taxable income would be nil and 50,000 of losses would remain.

```oa-check
name: Beta S.p.A., 2026, 30% ROL interest limit and 80% loss cap
inputs:
  profit_before_tax: 170000
  net_interest_expense: 150000
  tax_rol: 400000
  losses_bf: 250000
steps:
  - interest_capacity: tax_rol * 0.30
  - interest_disallowed: max(net_interest_expense - interest_capacity, 0)
  - income_before_losses: profit_before_tax + interest_disallowed
  - loss_cap: income_before_losses * 0.80
  - losses_used: min(losses_bf, loss_cap)
  - taxable_income: income_before_losses - losses_used
  - ires_2026: taxable_income * 0.24
  - losses_cf: losses_bf - losses_used
expected:
  interest_disallowed: 30000
  income_before_losses: 200000
  losses_used: 160000
  taxable_income: 40000
  ires_2026: 9600
  losses_cf: 90000
```

## Ask the client first

1. **Tax period and status.** Calendar year or not; ISA taxpayer or not (it decides 40/60 or 50/50 acconti); in a tax group (consolidato) or transparency option; any biennial arrangement (concordato preventivo biennale).
2. **2025 return.** The 2025 IRES actually due, and whether the 20% IRES premiale was claimed. If it was, check the reserve has not been distributed during 2026 and the assets are still held, and recompute the 2026 acconti at 24%. Ask also whether any 2025 gain on business assets was spread over five years, because the 2026 acconti treat it as taxed in full.
3. **Losses.** The loss schedule by year, which losses arose in the first three tax periods, and any transfer of control or change of main activity, including at parent level.
4. **Financing.** Net interest expense, tax ROL, and ROL and interest carried forward.
5. **Shareholdings.** Dividends received and shares sold in 2026, with holding dates, balance sheet classification and the subsidiaries' countries and activity, to test the 95% rules and the CFC rules.
6. **Cross-border payments.** Dividends, interest or royalties paid to non-residents, and the recipients' documents (residence certificates, beneficial ownership), before deciding the withholding rate.

## Sources

| Source | URL | Read on |
|---|---|---|
| TUIR (D.P.R. 917/1986) art. 73, residence and taxpayers | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art73!vig=2026-10-22 | 2026-10-22 |
| TUIR art. 77, IRES rate, with notes on the 3.5-point surcharge | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art77!vig=2026-10-22 | 2026-10-22 |
| TUIR art. 77 in the version from 1 January 2027 (repealed by D.Lgs. 117/2026) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art77!vig=2027-01-02 | 2026-10-22 |
| TUIR art. 83, from accounts to taxable income | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art83!vig=2026-10-22 | 2026-10-22 |
| TUIR art. 84, losses | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art84!vig=2026-10-22 | 2026-10-22 |
| TUIR art. 86(4), gains on business assets, as replaced by L. 199/2025 art. 1(42) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art86!vig=2026-10-22 | 2026-10-22 |
| TUIR art. 87, participation exemption | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art87!vig=2026-10-22 | 2026-10-22 |
| TUIR art. 89, dividends (and its January to March 2026 version) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art89!vig=2026-10-22 | 2026-10-22 |
| TUIR art. 95, directors' fees | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art95!vig=2026-10-22 | 2026-10-22 |
| TUIR art. 96, interest limitation | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art96!vig=2026-10-22 | 2026-10-22 |
| TUIR art. 99, taxes not deductible | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art99!vig=2026-10-22 | 2026-10-22 |
| TUIR art. 102, depreciation, small assets, telephones | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art102!vig=2026-10-22 | 2026-10-22 |
| TUIR art. 108, entertainment | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art108!vig=2026-10-22 | 2026-10-22 |
| TUIR arts. 117 and 120, consolidato nazionale | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art117!vig=2026-10-22 and https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art120!vig=2026-10-22 | 2026-10-22 |
| TUIR arts. 151 and 152, non-resident companies and PEs | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art152!vig=2026-10-22 | 2026-10-22 |
| TUIR art. 164, vehicles | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art164!vig=2026-10-22 | 2026-10-22 |
| TUIR art. 166, exit tax | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art166!vig=2026-10-22 | 2026-10-22 |
| TUIR art. 167, CFC | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1986-12-22;917~art167!vig=2026-10-22 | 2026-10-22 |
| L. 207/2024 art. 1(436)-(444), IRES premiale | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2024-12-30;207~art1-com436!vig=2026-10-22 | 2026-10-22 |
| L. 199/2025 (2026 budget law), art. 1, all commi | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:legge:2025-12-30;199 | 2026-10-22 |
| D.L. 38/2026 art. 11, dividend and PEX regime restored, 1.2% rate | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2026-03-27;38~art11!vig=2026-10-22 | 2026-10-22 |
| D.Lgs. 117/2026, new income tax code (arts. 310, 334, 376, 377) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2026-06-19;117 | 2026-10-22 |
| D.Lgs. 33/2025, payments code, art. 243 (applies from 1 January 2027) | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:2025-03-24;33 | 2026-10-22 |
| D.Lgs. 471/1997 arts. 1 and 13, penalties | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art1!vig=2026-10-22 and https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;471~art13!vig=2026-10-22 | 2026-10-22 |
| MEF decree 10 December 2025, legal interest rate 1.60% from 1 January 2026 (GU n. 289, 13 December 2025) | https://www.gazzettaufficiale.it/eli/id/2025/12/13/25A06705/sg | 2026-10-22 |
| D.Lgs. 472/1997 art. 13, ravvedimento operoso | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legislativo:1997-12-18;472~art13!vig=2026-10-22 | 2026-10-22 |
| DPR 600/1973 arts. 25, 26, 26-quater, 27, 27-bis, withholding | https://www.normattiva.it/uri-res/N2Ls?urn:nir:presidente.repubblica:decreto:1973-09-29;600~art27!vig=2026-10-22 (and ~art25, ~art26, ~art26quater, ~art27bis) | 2026-10-22 |
| D.L. 66/2014 art. 3(1), 26% rate | https://www.normattiva.it/uri-res/N2Ls?urn:nir:stato:decreto.legge:2014-04-24;66~art3!vig=2026-10-22 | 2026-10-22 |
| Agenzia delle Entrate, Redditi 2026 general instructions (filing terms 3.1, payments 4.1, acconti 4.2) | https://www.agenziaentrate.gov.it/portale/documents/20143/9771542/Parte_Generale_istr_2026.pdf/2ad66f68-6f28-a982-8570-c130cdcdddfa?t=1772195389363 | 2026-10-22 |
| Agenzia delle Entrate, Redditi SC 2026 instructions (IRES premiale, quadro RN) | https://www.agenziaentrate.gov.it/portale/documents/20143/9962362/SC_istr_2026.pdf/7c2fd2b6-6264-88eb-5c92-9d9ecf81e2c4?t=1779895444801 | 2026-10-22 |
| Agenzia delle Entrate, IRAP 2026 instructions (3.9% rate) | https://www.agenziaentrate.gov.it/portale/documents/20143/9765340/IRAP_2026_istruzioni.pdf/6cd3bc0e-e7bd-f449-c86b-03cc142c1b74?t=1772192055414 | 2026-10-22 |

Not yet confirmed: the exact filing date for the 2026 return (Modello Redditi SC 2027 and its instructions are not yet published; 2 November 2027 is inferred from the weekend and holiday rule); how D.Lgs. 117/2026, D.Lgs. 33/2025 and D.Lgs. 173/2024 (all applying from 1 January 2027) affect the 2026 return, payments and penalties made in 2027; the interest rate on assessed tax; the euro figure of the ISA revenue limit that decides 50/50 acconti (the general instructions 4.2 say only that each ISA approval decree sets it); the "taxable part" of royalties under DPR 600/1973 art. 25(4); treaty withholding rates; the super-depreciation measure in L. 199/2025 art. 1(427)-(436).

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

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-23. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `it-ires-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/it-ires-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
