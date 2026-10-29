---
name: pt-corporate-tax
description: "Portuguese corporate income tax (IRC) for tax year 2026: resident companies in mainland Portugal and permanent establishments. Covers the 19% rate for periods starting in 2026 (20% in 2025, 18% in 2027, 17% from 2028), the 15% SME and 12.5% startup rate on the first EUR 50,000, derrama municipal (up to 1.5%) and derrama estadual (3%, 5%, 9%), autonomous taxation, losses (no time limit, 65% cap, 75% for 2020-2021 losses), the interest limit, participation exemption, CFC, payments on account, the repealed PEC, Modelo 22 by 31 May, IES by 15 July, fines, 7.221% late interest, SIFIDE II and RFAI. Trigger on: IRC Portugal, Modelo 22, derrama, tributação autónoma, pagamentos por conta, prejuízos fiscais. Also states the Madeira and Azores 2026 rates (13.3%, 10.5% on the first EUR 50,000) and the CINM 5% rate. Out of scope: regional surcharges and income allocation between regions; banks, insurers, funds; transfer pricing (pt-transfer-pricing); non-residents and withholding (pt-cross-border);"
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/pt-corporate-tax"
  jurisdiction: "PT"
  tax_year: "2026"
  last_updated: "2026-10-27"
  authored_by: "Michael Cutajar and the OpenAccountants team"
  trust_label: "Built by Michael Cutajar and the OpenAccountants team"
  review_status: "pending_review"
---

# Portugal: corporate income tax (IRC), tax year 2026 v0.2

> Source-cited draft: not reviewed by an accountant.

This skill computes Portuguese corporate income tax (Imposto sobre o Rendimento das Pessoas Coletivas, IRC) for a 2026 tax period. It covers the rates, the two surcharges (derrama municipal and derrama estadual), autonomous taxation, losses, the interest limit, the participation exemption, payments on account, the Modelo 22 and the IES, fines and interest, and the two main investment credits (SIFIDE II and RFAI). Every figure comes from the consolidated Código do IRC (CIRC) and other codes on the Portal das Finanças, read on 24 October 2026, or from the Diário da República.

The IRC rate depends on the year in which the tax period STARTS. Fix that date first.

## Who this applies to

- **In scope.** Companies and other entities with their head office or effective management in Portugal whose main activity is commercial, industrial or agricultural, taxed on worldwide income. For the CIRC, any business activity, including services, counts as commercial, industrial or agricultural (CIRC art. 3(4)). Also non-residents with a permanent establishment in Portugal, for the profit of that establishment.
- **Tax period.** The calendar year, unless the company adopts a different annual period that matches its accounting year (CIRC art. 8). A period that started in 2025 (for example 1 July 2025 to 30 June 2026) uses the 2025 rates in the table below.
- **Madeira and the Azores.** Both regions set their own IRC rates by regional law; the rates for 2026 are in the table below. Madeira fixes its rates in DLR 2/2001/M art. 2 (wording of DLR 8/2025/M, the Madeira 2026 budget, in effect from 1 January 2026). The Azores apply a 30% reduction to the national rates in force each year (DLR 2/99/A art. 5(1)) to companies with their head office, effective management or a permanent establishment there; a company with establishments in more than one region splits its IRC by the share of annual turnover of its Azores establishments (art. 5(2)(b) and (3)). The Madeira International Business Centre (CINM, Zona Franca da Madeira) has its own 5% regime (EBF art. 36-A); derrama municipal for a CINM company is split in its own subtable of Modelo 22 Annex A (EBF art. 36-A(12)). This skill does not compute the regional surcharges (derrama regional), the split of income between regions, or the CINM ceilings: refer.
- **Out of scope here.** Banks, insurers and other supervised financial entities; collective investment funds; entities whose main activity is not commercial, industrial or agricultural (they pay the art. 87(5) rate on global income); the simplified regime; group taxation computations (RETGS, arts. 69 to 71); reorganisations (arts. 73 and following); the global minimum tax (Lei 41/2024); oil, gas and extractive regimes; open inspections, claims, court cases and mutual agreement procedures (refer, and produce no figures that could prejudice the position). Non-residents without a permanent establishment, outbound withholding and treaty relief: `pt-cross-border`. Related-party pricing: `pt-transfer-pricing`. Shareholders' IRS on dividends: `pt-irs-employees-investment`.

## Rates, bands and thresholds

| Item | Rate or amount | Tax year | Source |
|---|---|---|---|
| General IRC rate, tax periods starting in 2026 (CIRC art. 87(1) and (5); Lei 64/2025 art. 3(2)) | 19% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx |
| General IRC rate, periods starting in 2025 (Lei 45-A/2024 wording) | 20% | 2025 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/ra/Pages/irc87ra_20251107.aspx |
| General IRC rate, periods starting in 2027 (Lei 64/2025 art. 3(3)) | 18% | 2027 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx |
| General IRC rate printed in art. 87(1), periods starting on or after 1 January 2028 | 17% | 2028+ | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx |
| SME and Small Mid Cap rate on the first EUR 50,000 of taxable income (art. 87(2); Lei 64/2025 art. 3(4)) | 15% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx |
| SME rate on the first EUR 50,000, periods starting in 2025 | 16% | 2025 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/ra/Pages/irc87ra_20251107.aspx |
| Startup rate on the same EUR 50,000 (art. 87(8), Lei 21/2023) | 12.5% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx |
| Madeira: general rate; SME and Small Mid Cap rate on the first EUR 50,000 (DLR 2/2001/M art. 2(1) and (5), wording of DLR 8/2025/M art. 19, in effect from 1 January 2026) | 13.3%; 10.5% | 2026 | https://www.madeira.gov.pt//Portals/25/Documentos/Legislacao/Decreto%20Legislativo%20Regional%20n.%C2%BA%208_2025_M%2C%20de%2030%20de%20dezembro.pdf |
| Azores: reduction to the national IRC rates in force each year (DLR 2/99/A art. 5(1)); applied to 19% and 15% | 30% (13.3%; 10.5% on the first EUR 50,000) | 2026 | https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-legislativo-regional/1999-164477580 |
| CINM (Zona Franca da Madeira): rate for entities licensed from 2015 to 31 December 2026, on qualifying income, until 31 December 2033, within the art. 36-A(3) and (4) ceilings (EBF art. 36-A(1), wording of Lei 73-A/2025) | 5% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf-artigo-36-ordm-a.aspx |
| Non-resident without a permanent establishment (art. 87(4)); listed preferential regimes, unidentified accounts, prizes | 25%; 35% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx |
| Derrama municipal, maximum, on taxable profit (Lei 73/2013 art. 18) | up to 1.5% | 2026 | https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irc/Documents/M22ANA.PDF |
| Derrama municipal reduced rate allowed for prior-year turnover not above (art. 18(24)) | EUR 150,000 | 2026 | https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irc/Documents/M22ANA.PDF |
| Derrama estadual on taxable profit above EUR 1,500,000 up to EUR 7,500,000 (CIRC art. 87-A) | 3% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx |
| Derrama estadual above EUR 7,500,000 up to EUR 35,000,000 | 5% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx |
| Derrama estadual above EUR 35,000,000 | 9% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx |
| Autonomous tax, car charges, acquisition cost below EUR 37,500 / EUR 37,500 to below EUR 45,000 / EUR 45,000 or more (art. 88(3)) | 8% / 25% / 32% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx |
| Autonomous tax, qualifying plug-in hybrids and natural gas cars, same bands (art. 88(18)) | 2.5% / 7.5% / 15% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx |
| Autonomous tax, fully electric cars above the art. 34(1)(e) ordinance cost (art. 88(20)) | 10% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx |
| Autonomous tax, undocumented expenses (art. 88(1) and (2)) | 50% (70% for exempt or non-business entities) | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx |
| Autonomous tax, representation expenses (art. 88(7)) | 10% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx |
| Autonomous tax, payments to listed preferential regimes not shown to be real and normal (art. 88(8)) | 35% (55% for art. 88(2) entities) | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx |
| Autonomous tax, per diems and staff own-car payments not invoiced to clients (art. 88(9)) | 5% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx |
| Autonomous tax, profits distributed to exempt entities holding under one year (art. 88(11)) | 23% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx |
| Autonomous tax, manager termination payments; manager bonuses above 25% of annual pay AND above EUR 27,500 unless at least 50% is deferred three years (art. 88(13)) | 35% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx |
| Uplift on every autonomous tax rate in a loss year (art. 88(14)) | +10 percentage points | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx |
| Loss deduction cap, share of the year's taxable profit (art. 52(2)) | 65% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc52.aspx |
| Extra cap for losses of 2020 and 2021 (Lei 27-A/2020 art. 11(2), kept by Lei 24-D/2022 art. 228(1)) | +10 points (75%) | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Lei_27_A_2020.pdf |
| Interest limit: net financing expenses deductible up to the higher of (art. 67(1)) | EUR 1,000,000 or 30% of EBITDA | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc67.aspx |
| Participation exemption: minimum holding; payer's minimum statutory rate as a share of the art. 87(1) rate (art. 51(1)) | 10%; 60% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc51.aspx |
| Payments on account, share of prior-period IRC, prior-period turnover up to EUR 500,000 / above (art. 105) | 80% / 95% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc105.aspx |
| No payments on account if prior-period IRC below; no balance or refund below (art. 104(4) and (7)) | EUR 200; EUR 25 | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc104.aspx |
| Additional payments on account (derrama estadual), prior-period profit slices (art. 105-A) | 2.5% / 4.5% / 8.5% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc105a.aspx |
| Late-payment interest (juros de mora) on debts to the State, from 1 January 2026 (IGCP Aviso 18/2026/2; LGT art. 44) | 7.221% a year | 2026 | https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668 |
| SIFIDE II R&D credit: base rate; incremental rate (cap EUR 1,500,000) (CFI art. 38) | 32.5%; 50% | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cfi/Pages/cfi-38.aspx |
| RFAI investment credit: art. 107(3)(a) regions up to EUR 15m / above; art. 107(3)(c) regions; yearly cap after start-up years (CFI art. 23) | 30% / 10%; 10%; 50% of IRC | 2026 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cfi/Pages/cfi-23.aspx |

**Conditions for the SME rate (art. 87(2) and (3)).** The company carries on a commercial, industrial or agricultural activity directly and as its main activity, and qualifies as a small or medium enterprise or a Small Mid Cap under the annex to Decreto-Lei 372/2007 (measured with partner and linked enterprises). The reduced rate is EU de minimis aid. It is a band: only the first EUR 50,000 of taxable income gets it. The startup rate needs startup status under Lei 21/2023 and all the conditions of its art. 2(1)(f). A transitional rule (Lei 24-D/2022 art. 229) keeps the SME rate for the two periods after a merger, division, asset contribution or share exchange made from 2023 to 2026 between SMEs, where the receiving company stops qualifying because of the operation.

**Derrama estadual by slices.** Each rate applies only to profit inside its slice: EUR 6,000,000 at 3%, then the next EUR 27,500,000 at 5%, then the excess over EUR 35,000,000 at 9% (art. 87-A(2)). Under RETGS each group company computes it on its own taxable profit (art. 87-A(3)).

**Derrama municipal.** Each municipality sets its rate each year, up to 1.5%, and may set a reduced rate for companies whose prior-year turnover does not exceed EUR 150,000. AT publishes the rates in an Ofício Circulado and under Portal das Finanças, Serviços, IRC, Modelo 22 e Derrama de IRC, Derrama IRC, Consultar taxas. A municipality may instead exempt companies whose prior-year turnover does not exceed EUR 150,000; the rate entered is then zero (Modelo 22 Annex A instructions). Until the municipality's 2026 rate is confirmed, use 1.5%. A company with taxable income above EUR 50,000 AND establishments in more than one municipality files Annex A and splits the derrama by payroll (massa salarial) in each municipality.

## The taxable base

1. **Start from the accounting result** in the approved accounts and make the tax adjustments to reach taxable profit (lucro tributável).
2. **Participation exemption, dividends (art. 51).** Dividends received are excluded where the company holds at least 10% of the capital or voting rights, for one year without interruption (or keeps it until one year is reached), is not tax transparent, the payer is subject to IRC or a similar tax at a statutory rate of at least 60% of the art. 87(1) rate, and the payer is not in a listed preferential regime. Not for distributions deductible by the payer or under a non-genuine arrangement (art. 51(10), (13)). The minimum-rate test is waived where the conditions of art. 66(7) are met (art. 51(2)). Where the conditions fail, the dividend can still get the foreign tax credit of arts. 91 and 91-A (art. 51(9)). For 2026 the art. 87(1) rate is read through the transitional rule; a payer that passes only against the printed 17% is unsettled, refer.
3. **Participation exemption, share gains (art. 51-C).** Gains and losses on shares held for at least one year are excluded if the art. 51 conditions are met, unless Portuguese real estate (other than business property) is more than 50% of the company's assets. Losses on such shares are not deductible. The same applies to other equity instruments tied to the shares, such as supplementary capital contributions (prestações suplementares) (art. 51-C(2)). Impairment losses on the shares deducted in earlier years are added back in the year of sale (art. 51-C(6)).
4. **Interest limit (art. 67).** Net financing expenses are deductible up to the higher of EUR 1,000,000 and 30% of tax EBITDA. The excess carries forward five periods; unused EBITDA capacity carries forward five periods. The EUR 1,000,000 is pro-rated for a short period. Carry-forwards are lost on a change of more than 50% of the capital or votes, with the art. 52 exceptions. Banks and insurers are excluded.
5. **Controlled foreign companies (art. 66).** Profits of a non-resident entity are attributed to a resident that holds at least 25% of the capital, votes or rights to income, where the entity's profit tax actually paid is below 50% of the IRC that would be due, or the territory is on the ministerial list. Not where passive income is no more than 25% of the entity's income, and not for an EU or EEA entity with valid economic reasons and real activity (art. 66(14)).
6. **Tax losses (art. 52).** Taxable profit less losses brought forward gives taxable income (matéria coletável). Losses carry forward with no time limit. Each year's deduction is capped at 65% of that year's taxable profit; the cap rises by 10 points (to 75%) where the extra deduction comes from losses of 2020 and 2021 (Lei 27-A/2020 art. 11(2)). The part not deducted carries forward. There is no carry-back. Losses from periods before 2023 under the REAID regime keep the old deduction period (Lei 24-D/2022 art. 228(2)). Losses are not deductible in a year assessed by indirect methods, but are not lost (art. 52(3)).
7. **Change of ownership (art. 52(8) and (9)).** Losses are lost if more than 50% of the capital or the majority of votes changes hands since the loss year, unless the operation had no tax-avoidance main purpose. Excluded changes: direct to indirect holding and the reverse, and transfers within a group under common majority control; reorganisations under arts. 73 and following; succession on death; an acquirer that has held more than 20% since the start of the loss year; an acquirer that has been an employee or board member since then.
8. **Rates.** Apply the SME or startup band, then the general rate to the rest, on taxable income.
9. **Surcharges.** Derrama municipal and derrama estadual are charged on TAXABLE PROFIT, before losses, not on taxable income.
10. **Autonomous taxes (art. 88)** are separate charges on the year's expenses listed in the rates table, due even with no taxable income. The car rates cover light passenger cars, the light goods vehicles of art. 7(1)(b) of the Vehicle Tax Code (Código do ISV), and motorcycles, for companies that are not subjectively exempt and whose main activity is commercial, industrial or agricultural (art. 88(3)). Charges include depreciation, rent, insurance, maintenance, fuel and ownership taxes; the band is fixed by the car's acquisition cost. Excluded: vehicles used for public transport or rented out in the business, and cars taxed on the employee under CIRS art. 2(3)(b)(9) (art. 88(6)). A plug-in hybrid gets the reduced rates only with a grid-charged battery, at least 50 km electric range and emissions below 50 gCO2/km (80 gCO2/km if Euro 6e-bis). No deductions are allowed against the total (art. 88(23)). Art. 88 does not apply to the expenses of a permanent establishment outside Portugal relating to its activity there (art. 88(17)). The manager-bonus escape needs at least 50% of the bonus deferred for at least three years AND payment conditional on the company's positive performance over that period; if either condition later fails, the autonomous tax that should have been paid is added to the IRC of the period in which it fails (art. 88(13)(b), (21)).
11. **Loss-year uplift (art. 88(14) and (15)).** Every autonomous tax rate rises by 10 points when the company has a tax loss for the year. Not in the start-up year and the next. **For 2026 only** (Lei 73-A/2025 art. 95(5)) the uplift also does not apply where (a) the company had taxable profit in one of the three previous periods AND filed the Modelo 22 and IES for the two previous periods on time, or (b) 2026 is the start-up year or one of the next two. Under RETGS the group loss is used (art. 88(22)).
12. **Tax credits.** SIFIDE II (CFI arts. 35 to 42) covers R&D expenses of periods from 2014 to 2026: 32.5% base plus 50% of the increase over the average of the two previous years (incremental part capped at EUR 1,500,000), with a 15% uplift to the base rate for micro, small and medium enterprises that have not yet completed two financial years and have not used the incremental rate. The claim needs a certifying declaration from the Agência para a Investigação e Inovação, E. P. E., or proof that it was requested (CFI art. 40(1)); only companies whose profit is not set by indirect methods and that owe no tax or social security may claim (art. 39); no credit for R&D financed directly or indirectly by SIFIDE II investment funds or by other national or international public support (art. 38(10)); applications are due by the end of the fifth month after the year, and applications for years before that are not accepted (CFI art. 40(3)). Unused credit carries forward to the twelfth following period. RFAI (CFI arts. 22 to 26) gives 30% (up to EUR 15m) or 10% (above) of eligible investment in art. 107(3)(a) regions and 10% in art. 107(3)(c) regions, capped at 50% of IRC except in the start-up period and the next two; unused credit carries forward 10 periods; assets and jobs must be kept three years (SMEs) or five years. Eligible investment is new tangible fixed assets used in the business (not land, most buildings, light passenger cars or furniture), some technology-transfer intangibles and the salary cost of new jobs at qualification levels 7 or 8; for a company that is not an SME, intangibles and salary costs are capped at a share of the investment (art. 22(3)), and in art. 107(3)(c) regions only investment in a new economic activity qualifies (art. 22(7)). Total aid must stay within the regional aid ceiling (art. 23(5) and (6)). The region list is the art. 43 CFI map.
13. **Deduct** withholding suffered and the year's payments on account to reach the balance or refund.

## Deadlines and filing

| What | When | Source |
|---|---|---|
| Payments on account (3) | July, September and 15 December of the year itself; non-calendar period: 7th month, 9th month, 15th of the 12th month (art. 104(1)(a)) | CIRC art. 104 |
| Additional payments on account for derrama estadual | Same dates, if derrama estadual was due for the prior period (art. 104-A, 105-A) | CIRC art. 104-A |
| Modelo 22 (annual self-assessment) | Last day of May of the following year, working day or not: 31 May 2027 for 2026. Other period: last day of the 5th month after the period ends. Cessation: last day of the 3rd month after (art. 120) | CIRC art. 120 |
| IRC and derrama estadual balance | By the Modelo 22 deadline (art. 104(1)(b), 104-A(1)(b)) | CIRC art. 104 |
| Refund | By the end of the 3rd month after a timely, error-free return (art. 104(3)); late refunds earn interest (art. 104(6)) | CIRC art. 104 |
| IES (accounting and tax information, including related-party transactions, art. 63(7)) | 15 July of the following year, working day or not: 15 July 2027 for 2026 (art. 121(2)). Other period: 15th day of the 7th month after the period ends (art. 121(3)) | CIRC art. 121 |
| IRC withheld by the company | By the 20th of the month after deduction (art. 94(6)) | CIRC art. 94 |

**Payments on account (art. 105).** The base is the prior period's IRC net of withholding. The share is 80% if prior-period turnover was up to EUR 500,000, 95% above. Each payment is a third, rounded up to the euro (art. 105(2) and (3)). No payments when the prior-period IRC was below EUR 200. A company may skip or reduce the third payment if the payments made already cover the year's tax; if that leaves unpaid more than 20% of a normal third payment, compensatory interest runs (art. 107).

**Special payment on account (PEC).** Repealed by Lei 12/2022 for tax periods starting on or after 1 January 2022 (art. 106). No company pays a PEC for 2026.

**Group filing.** Under RETGS the parent files the group return and every group company also files its own (art. 120(6)).

**RETGS conditions (art. 69).** The parent holds, directly or indirectly, at least 75% of each subsidiary's capital, giving more than half of the votes (art. 69(2)). The option also needs (art. 69(3)): all group companies have their head office and effective management in Portugal and all their income is taxed under the general regime at the highest normal rate; the parent has held each holding for more than one year when the regime starts (not required for a subsidiary the group set up less than a year before, if the holding has existed since incorporation, art. 69(13)); the parent is not itself controlled by another resident company that could be a parent; and the parent has not renounced the regime in the previous three years. Among others, companies that are inactive for more than a year or dissolved, in insolvency or recovery proceedings, that had tax losses in the three years before the regime starts (unless the parent has held them for more than two years), that pay a lower IRC rate without renouncing it, that use a different tax period, or that are not an Lda, SA or SCA, cannot join (art. 69(4)). The parent must prove the conditions (art. 69(12)). Group computations stay out of scope.

## Penalties and interest

| Item | Figure | Source |
|---|---|---|
| Late-payment interest (juros de mora), tax not paid by the deadline, from 1 January 2026 | 7.221% a year | IGCP Aviso 18/2026/2; LGT art. 44 |
| Compensatory interest (juros compensatórios): late return, late payment on account, under-assessment | Rate of legal interest under Civil Code art. 559(1); late payments on account start it at once (CIRC art. 104(5)) | LGT art. 35 |
| Non-payment of tax, payments on account included (negligence) | Fine of 15% to half of the tax missing | RGIT art. 114(2), (5)(f) |
| Non-payment (intentional, not a crime) | Fine of the tax missing to double it | RGIT art. 114(1) |
| Late or missing Modelo 22 | Fine of EUR 150 to EUR 3,750 | RGIT art. 116(1) |
| Companies | Minimum and maximum of each fine doubled; overall caps EUR 45,000 (negligence) and EUR 165,000 (intent) | RGIT art. 26(1), (4) |
| Waiver | No fine where, in the last five years, there was no conviction or prior waiver, the breach caused no actual loss of revenue and it is put right; non-payment always counts as a loss. The waiver is requested within the defence period | RGIT art. 29 |

## Cross-border points

- **Non-residents.** A non-resident with no permanent establishment pays 25% (35% in the listed cases), mostly by final withholding at source (art. 87(4), 94). Permanent establishments are taxed like residents on their profit and pay both derramas. See `pt-cross-border`.
- **Withholding by the company.** IRC withholding at 25% on the income in art. 94(1), 21.5% on board members' fees; final for non-residents without a permanent establishment. IRS withholding on dividends and interest to individuals is a final 28% (35% for listed regimes and unidentified accounts) (CIRS art. 71). Treaty relief at source needs proof given to the payer by the payment deadline (art. 98).
- **Outbound dividends (art. 14(3)).** Exempt where an EU, EEA or treaty-state parent holds at least 10% for one year, is subject to tax (a treaty-state parent at a statutory rate of at least 60% of the art. 87(1) rate), and proves it before payment; not for non-genuine arrangements. Detail: `pt-cross-border`.
- **Foreign tax credit and treaties.** Arts. 91 and 91-A CIRC; for individuals see `pt-foreign-source-treaties`.
- **Transfer pricing.** Related-party dealings at arm's length (art. 63); documentation in the tax file and disclosure in the IES. Thresholds, methods and the country-by-country report: `pt-transfer-pricing`.
- **CFC.** See the taxable base, point 5.
- **Global minimum tax.** Lei 41/2024 (RIMG) transposes Directive (EU) 2022/2523; AT runs the Modelo 62 and Modelo 63 returns. Refer large groups.

## Worked examples

### Example 1: SME, one municipality

A Lda qualifies as an SME, has a calendar 2026 tax period, one establishment, no losses and taxable profit of EUR 130,000. The municipality's 2026 rate is not yet confirmed, so 1.5% is used. IRC: EUR 50,000 at 15% = EUR 7,500, plus EUR 80,000 at 19% = EUR 15,200, total EUR 22,700. No derrama estadual (profit is not above EUR 1,500,000). Derrama municipal: 1.5% of EUR 130,000 = EUR 1,950. Total EUR 24,650, before autonomous taxes, credits and payments on account. Payments on account in 2027: turnover decides 80% or 95% of the 2026 IRC.

```oa-check
name: PT SME 2026, taxable profit EUR 130,000, municipal rate 1.5%
inputs:
  taxable_profit: 130000
  sme_band: 50000
steps:
  - irc_sme: min(taxable_profit, sme_band) * 0.15
  - irc_general: max(taxable_profit - sme_band, 0) * 0.19
  - irc: irc_sme + irc_general
  - derrama_estadual: max(taxable_profit - 1500000, 0) * 0.03
  - derrama_municipal: taxable_profit * 0.015
  - total: irc + derrama_estadual + derrama_municipal
expected:
  irc_sme: 7500.00
  irc_general: 15200.00
  irc: 22700.00
  derrama_estadual: 0.00
  derrama_municipal: 1950.00
  total: 24650.00
```

### Example 2: large company, loss cap with 2021 losses and derrama estadual

A company that is not an SME has a calendar 2026 period and taxable profit of EUR 10,000,000. It brings forward losses of EUR 9,000,000, all from 2020 (EUR 4,000,000) and 2021 (EUR 5,000,000). No ownership change. Municipal rate assumed at 1.5%.

The basic cap is 65% of EUR 10,000,000 = EUR 6,500,000. The cap rises by 10 points (EUR 1,000,000) because the extra deduction comes from 2020 and 2021 losses, so the deduction is EUR 7,500,000. Had only part of the losses come from 2020 and 2021, the extra 10 points would cover only deductions of those years' losses; art. 52 sets no order of use, so confirm the allocation in the Modelo 22 loss table. Taxable income is EUR 2,500,000; IRC at 19% is EUR 475,000. EUR 1,500,000 of losses carry forward. The surcharges use taxable profit before losses: derrama estadual EUR 6,000,000 at 3% = EUR 180,000 plus EUR 2,500,000 at 5% = EUR 125,000, total EUR 305,000; derrama municipal EUR 150,000. Total EUR 930,000. Because derrama estadual was due, the company also makes additional payments on account in 2027.

```oa-check
name: PT 2026, profit EUR 10m, losses EUR 9m all from 2020 and 2021
inputs:
  taxable_profit: 10000000
  losses_bf: 9000000
  losses_2020_2021: 9000000
steps:
  - cap_basic: taxable_profit * 0.65
  - cap_extra: min(taxable_profit * 0.10, losses_2020_2021)
  - loss_used: min(losses_bf, cap_basic + cap_extra)
  - taxable_income: taxable_profit - loss_used
  - irc: taxable_income * 0.19
  - losses_cf: losses_bf - loss_used
  - de_slice1: (min(taxable_profit, 7500000) - 1500000) * 0.03
  - de_slice2: (min(taxable_profit, 35000000) - 7500000) * 0.05
  - derrama_estadual: de_slice1 + de_slice2
  - derrama_municipal: taxable_profit * 0.015
  - total: irc + derrama_estadual + derrama_municipal
expected:
  loss_used: 7500000.00
  taxable_income: 2500000.00
  irc: 475000.00
  losses_cf: 1500000.00
  derrama_estadual: 305000.00
  derrama_municipal: 150000.00
  total: 930000.00
```

## Ask the client first

1. When did the tax period start, and is it the calendar year? (Decides 19% or 20%.)
2. Is the company an SME or Small Mid Cap under Decreto-Lei 372/2007, counting partner and linked enterprises, or a certified startup? Has it used its de minimis allowance?
3. Where are the head office and establishments, including Madeira or the Azores, and what was last year's turnover? (Derrama municipal, Annex A, regional rates.)
4. What losses are brought forward, by year (especially 2020 and 2021), and has more than 50% of the capital or votes changed hands since?
5. Was there a tax loss this year, taxable profit in any of the last three years, and were the last two Modelo 22 and IES filed on time? (Autonomous tax uplift.)
6. Is the company in a group (RETGS, global minimum tax), and does it have foreign subsidiaries or related-party dealings?

## Sources

| Source | URL | Read on |
|---|---|---|
| CIRC art. 87 (rates) with Lei 64/2025 art. 3 transitional rule | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87.aspx | 2026-10-24 |
| CIRC art. 87, version in force until November 2025 (2025 rates, Lei 45-A/2024) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/ra/Pages/irc87ra_20251107.aspx | 2026-10-24 |
| CIRC art. 87-A (derrama estadual) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc87a.aspx | 2026-10-24 |
| CIRC art. 88 (autonomous taxation) with Lei 73-A/2025 (OE 2026) art. 95(5) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc88.aspx | 2026-10-24 |
| CIRC art. 52 (losses) with Lei 24-D/2022 art. 228 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc52.aspx | 2026-10-24 |
| Lei 27-A/2020 art. 11(2) (AT copy) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/legislacao/diplomas_legislativos/Documents/Lei_27_A_2020.pdf | 2026-10-24 |
| CIRC art. 3, 8, 14, 51, 51-C, 63, 66, 67, 69, 94, 104, 104-A, 105, 105-A, 106, 107, 117, 120, 121 | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc104.aspx (same path, irc + article number) | 2026-10-24 |
| AT, Modelo 22 Annex A instructions (derrama municipal, Lei 73/2013 art. 18) | https://info.portaldasfinancas.gov.pt/pt/apoio_contribuinte/modelos_formularios/irc/Documents/M22ANA.PDF | 2026-10-24 |
| IGCP Aviso 18/2026/2 (juros de mora 7.221% from 1 January 2026) | https://diariodarepublica.pt/dr/detalhe/aviso/18-2026-993315668 | 2026-10-24 |
| LGT art. 35 and 44 (interest) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/lgt/Pages/lgt35.aspx | 2026-10-24 |
| RGIT art. 26, 29, 114, 116 (fines) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/rgit/Pages/rgit114.aspx | 2026-10-24 |
| Madeira: DLR 8/2025/M (2026 regional budget), art. 19 amending DLR 2/2001/M art. 2 | https://www.madeira.gov.pt//Portals/25/Documentos/Legislacao/Decreto%20Legislativo%20Regional%20n.%C2%BA%208_2025_M%2C%20de%2030%20de%20dezembro.pdf | 2026-10-24 |
| Azores: DLR 2/99/A art. 5, consolidated version (Diário da República) | https://diariodarepublica.pt/dr/legislacao-consolidada/decreto-legislativo-regional/1999-164477580 | 2026-10-24 |
| EBF art. 36-A (CINM) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/bf_rep/Pages/ebf-artigo-36-ordm-a.aspx | 2026-10-24 |
| CIRS art. 71 (final IRS withholding) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cirs_rep/Pages/irs71.aspx | 2026-10-24 |
| CIRC art. 69 (RETGS conditions), 88(3), (17), (21), 51(2), (9), 51-C(2), 105(2) and (3) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/CIRC_2R/Pages/irc69.aspx (same path, irc + article number) | 2026-10-24 |
| CFI art. 22, 23 (RFAI) and 35, 38, 39, 40 (SIFIDE II) | https://info.portaldasfinancas.gov.pt/pt/informacao_fiscal/codigos_tributarios/cfi/Pages/cfi-38.aspx | 2026-10-24 |

Not yet confirmed: the Madeira and Azores derrama regional rates and the Madeira rules for allocating income to the region (DLR 2/2001/M art. 2(2) to (4) not read); whether Madeira's 2026 rates follow the start of the tax period, as the national rates do, for a non-calendar period; the Madeira startup rate; the fine for a late or missing IES (RGIT art. 116(1) or art. 117 not settled); that AT applies the municipality's normal derrama rate when the IES was not filed (AT's older field 364 help sheet says so; not re-read for 2026); the derrama municipal rates of each municipality for 2026 (AT's Ofício Circulado for 2026 profits is not yet out); the legal interest rate that sets compensatory interest (Civil Code art. 559 ordinance not read); the SME size thresholds in the annex to Decreto-Lei 372/2007; the fully electric car cost limit in the art. 34(1)(e) ordinance; the minimum tax scope, rate and deadlines under Lei 41/2024; group taxation computations under RETGS (conditions only: 75% holding, art. 69); whether "turnover not above EUR 150,000" in a municipality's reduced rate includes exactly EUR 150,000 (the Annex A instructions say "não ultrapasse", the AT field 364 help sheet says "inferior a"; Lei 73/2013 art. 18 not read).

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

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-10-27. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `pt-corporate-tax` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/pt-corporate-tax. If neither is available, confirm every figure against the official source pages cited above before relying on it.
