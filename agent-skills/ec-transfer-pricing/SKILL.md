---
name: ec-transfer-pricing
description: "Ecuador transfer pricing (precios de transferencia) for tax year 2026 under the Ley de Régimen Tributario Interno (LRTI), its Reglamento (arts. 4 and 84 to 91) and SRI Resolution NAC-DGERCGC15-00000455 as amended. Covers who is a related party (control, the 25% capital tests, the 50% of sales or purchases presumption, tax havens), the arm's length principle and comparability, the five methods, the interquartile range and adjustment to the median, the Anexo de Operaciones con Partes Relacionadas above USD 3,000,000 and the Informe Integral de Precios de Transferencia above USD 10,000,000, what is left out of the total, the deadline two months after the income tax return is due, the fines by taxpayer size (up to USD 15,000), and advance pricing consultations. Trigger on: precios de transferencia Ecuador, partes relacionadas, anexo de operaciones con partes relacionadas, informe integral de precios de transferencia, plena competencia, rango intercuartil, transfer pricing Ecuador 2026."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ec-transfer-pricing"
  jurisdiction: "EC"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Ecuador: transfer pricing (2026) v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This is the transfer pricing (TP) skill for the Ecuador pack. Company tax, the rate and the April return are in [ec-corporate-income-tax](ec-corporate-income-tax.md); individuals are in [ecuador-income-tax](ecuador-income-tax.md).

**Which text of the law.**
- **LRTI**: the SRI codification with last reform 1 April 2026. That covers the related-party and tax-haven articles after art. 4, the section on transfer pricing after art. 15, and the article on related-party transactions after art. 22.
- **Reglamento (RLRTI)**: the SRI codification with last reform 18 November 2025, arts. 4 and 84 to 91.
- **SRI Resolution NAC-DGERCGC15-00000455** (RO second Supl. 511, 29 May 2015), as amended. The filing thresholds were read in Resolution NAC-DGERCGC25-00000012 (7 June 2025), which restates them; the fines in Resolution NAC-DGERCGC24-00000020.
- **The exemption is gone.** The fifth unnumbered article after LRTI art. 15, which exempted some taxpayers from the TP regime, was repealed by the law in RO Supl. 461 of 20 December 2023. Resolution NAC-DGERCGC24-00000020 removed the matching words from Resolution NAC-DGERCGC15-00000455.

**Quick reference (2026).** Arm's length principle for every related-party transaction. Anexo above USD 3,000,000 of related-party transactions in the year; Informe Integral as well above USD 10,000,000. Both are due within two months of the income tax return due date. Fines up to USD 15,000 per obligation. Out-of-range results are adjusted to the median.

## Who this applies to

- **Every income tax payer that deals with related parties** must set its income, costs and deductible expenses at the prices independent parties would have used in comparable transactions (LRTI, unnumbered article after art. 22). Below the filing thresholds the arm's length rule still applies; only the filings change.
- **Related parties** (LRTI, unnumbered article after art. 4). These are persons or companies, in Ecuador or not, where one takes part directly or indirectly in the management, administration, control or capital of the other, or a third party does so in both. The law's list:
  1. parent and its subsidiaries or permanent establishments;
  2. subsidiaries among themselves;
  3. parties in which the same person takes part;
  4. parties whose boards are mostly the same members;
  5. parties in which the same group of members takes part;
  6. board members, and administrators and auditors (comisarios), where they have relations with the company beyond their role;
  7. a company and the spouses and relatives (to the fourth degree of blood or second by marriage) of its directors, administrators or comisarios;
  8. a person and the trusts in which they have rights;
  9. **any counterparty in a tax haven or lower-tax jurisdiction**.
- **Reglamento tests** (RLRTI art. 4):
  - holding 25% or more of the capital or equity of another company, directly or indirectly;
  - companies in which the same shareholders, their spouses or relatives hold at least 25%, or that trade with each other;
  - holding 25% or more in two or more companies;
  - **50% or more of sales or purchases with one counterparty**. The SRI must notify the taxpayer, who can show there is no link by management, administration, control or capital.

  Taxpayers who meet these tests are in the TP regime without being notified.
- **Tax haven** (LRTI, unnumbered article after the related-party article). A regime or jurisdiction meeting at least two of three conditions:
  - an effective income tax rate below 60% of Ecuador's, or unknown;
  - activity there need not be substantial to get its benefits;
  - no effective exchange of information.

  This applies even if the jurisdiction is not on the SRI's list.

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Related-party transactions in the tax year above USD 3,000,000 (total) | file the Anexo de Operaciones con Partes Relacionadas | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=1344f03a-3514-48dd-ba5c-c8a37d1e761f&nombre=NAC-DGERCGC25-00000012.pdf (restating Res. NAC-DGERCGC15-00000455 art. 2 as amended) |
| Related-party transactions above USD 10,000,000 (total) | file the Informe Integral de Precios de Transferencia as well as the Anexo | 2026 | same |
| Earlier threshold for the Informe (2015 text, since amended) | USD 15,000,000 | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/50db2d74-4e75-422a-9bc5-b3084d7bb018/NAC-DGERCGC15-00000455+2S.R.O.+511+29-05-2015.pdf (art. 2, original) |
| Fine for not filing, errors, or differences from the income tax return (law cap) | up to USD 15,000 | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI, unnumbered article after art. 22); RLRTI art. 84 |
| Not filing the Informe Integral | large taxpayers (including large estates) USD 15,000; special taxpayers USD 7,500; others USD 3,750 | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=3c8e92c5-f276-46bd-a11e-7014601b270f&nombre=NAC-DGERCGC24-00000020.pdf (new art. 13(a) of Res. 15-455) |
| Not filing the Anexo | large taxpayers USD 10,000; special taxpayers USD 5,000; others USD 2,500 | 2026 | same |
| Incomplete, inaccurate or wrong Informe or Anexo, corrected voluntarily | large USD 11,250; special USD 5,625; others USD 2,812 | 2026 | same (art. 13(b)) |
| Same, found by the SRI | large USD 15,000; special USD 7,500; others USD 3,750 | 2026 | same (art. 13(b)) |
| Arm's length range | first to third quartile of the comparables; a value outside it is adjusted to the median | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 87) |
| Related-party capital test | 25% or more, direct or indirect | 2026 | same (RLRTI art. 4) |
| Related-party trade presumption | 50% or more of sales or purchases with one counterparty | 2026 | same (RLRTI art. 4(4)) |
| Advance pricing consultation (consulta previa de valoración) | binding for the current year, the previous year (if its return is not yet due) and the next 3 years | 2026 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (LRTI, unnumbered article after art. 15); RLRTI art. 88 |

## The base

**What the arm's length principle does** (LRTI, unnumbered articles after art. 15). If related parties set terms that independent parties would not, the profit that one of them would have made without those terms is taxed.

**Comparability factors** (LRTI, unnumbered article after art. 15). Transactions are comparable when no difference significantly affects the price, value or margin, or when reasonable adjustments can remove the difference. The factors are:

- the characteristics of the transaction:
  - services: their nature and the know-how involved;
  - goods: physical features, quality and availability;
  - intangibles: the form of the deal, the type of asset, and its term, protection and expected benefits;
  - shares: equity, net worth, projected cash flows or the last stock-exchange price;
  - loans: amount, term, guarantees, the debtor's solvency, interest rate and substance over form;
- the functions, assets and risks of each party;
- the contract terms as actually performed;
- the economic and market circumstances;
- business strategies.

**Methods** (RLRTI art. 85):
1. comparable uncontrolled price;
2. resale price;
3. cost plus;
4. profit split;
5. transactional net margin.

Use them under the technical rules and order of priority the SRI sets by resolution, and otherwise under the OECD Transfer Pricing Guidelines in force on 1 January of the tax year, as far as they fit Ecuadorian law and treaties (RLRTI art. 89). The SRI may set anti-abuse measures, such as reference prices, sources of price data, quotation periods and the use of intermediaries (RLRTI art. 86), and may use secret comparables (RLRTI art. 90).

**Range and adjustment** (RLRTI art. 87). With two or more comparables, compute the median and the interquartile range (first to third quartile) with conventional statistics. A tested value inside the range is accepted as arm's length. A value outside it is replaced by the median. The difference is an adjustment to the income tax base, taxed at the company's rate (see ec-corporate-income-tax).

**What counts toward the USD 3,000,000 and USD 10,000,000** (Res. NAC-DGERCGC15-00000455 art. 3). Add all related-party transactions of the year, **except**:

- cash capital contributions in US dollars;
- offsets or reclassifications of balance-sheet accounts that do not affect results;
- cash payments in US dollars of dividends or liabilities;
- income under LRTI arts. 27 and 31 and the related assets, liabilities and costs;
- transactions with Ecuadorian public bodies or public companies;
- transactions covered by an approved advance pricing consultation;
- transactions with **local** related parties. This exclusion does not apply if:
  - the local party has art. 27 or 31 income; or
  - the taxpayer declares a negative base, used any tax incentive (including COPCI), took the reinvestment rate reduction, administers or operates a ZEDE, works in non-renewable resources, or has shareholders in a tax haven.

The SRI may still ask any taxpayer with related-party transactions, of any amount, for information.

## Deadlines and filing

| Item | Deadline | Source URL |
|---|---|---|
| Anexo and Informe Integral for tax year 2026 | within two months after the income tax return was due. For a company with ninth RUC digit 1 (return due 10 April 2027), by 10 June 2027 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf (RLRTI art. 84; return dates in RLRTI art. 72) |
| One-off extension for tax year 2024 | until September 2025, on the monthly return dates of each taxpayer | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=1344f03a-3514-48dd-ba5c-c8a37d1e761f&nombre=NAC-DGERCGC25-00000012.pdf |
| How | the Anexo is sent online through the SRI site under its technical sheet; the Informe Integral is filed as a digital PDF-text file | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/50db2d74-4e75-422a-9bc5-b3084d7bb018/NAC-DGERCGC15-00000455+2S.R.O.+511+29-05-2015.pdf (arts. 4 to 6) |
| SRI information request | at least 2 months to answer | same |

**Step by step.**

1. Map every related party under the law's list and the Reglamento's 25% and 50% tests. Include every counterparty in a tax haven.
2. Add up the year's related-party transactions, less the exclusions above. Decide whether the Anexo (over USD 3,000,000) and the Informe (over USD 10,000,000) are due.
3. For each type of transaction, do the comparability analysis and choose the method. Compute the interquartile range and the median.
4. If a tested result is outside the range, adjust to the median in the income tax return (tax reconciliation) by its April due date.
5. File the Anexo, and the Informe if due, within two months after the return's due date. The figures must match the income tax return, because differences are themselves fined.
6. Keep the analysis. The information is confidential and used only for tax (LRTI, unnumbered article after art. 22; RLRTI art. 91).

## Penalties and interest

| Item | Rule | Source URL |
|---|---|---|
| Filing failures, errors, differences from the income tax return | fine up to USD 15,000 per obligation, graded by taxpayer type as in the rates table | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=3c8e92c5-f276-46bd-a11e-7014601b270f&nombre=NAC-DGERCGC24-00000020.pdf |
| Tax on an SRI adjustment | income tax at the company rate, plus a 20% surcharge on tax assessed by the SRI and interest at 1.3 times the Banco Central 90-day active reference rate | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/00682c30-727a-4268-b095-f485d226ce49/Codigo_Tributario_10082023.pdf (CT arts. 21, 90) |
| Taxpayer type for the fine | large taxpayers and special taxpayers as at 1 January of the year in which the filing falls due | Res. NAC-DGERCGC24-00000020 (new art. 12) |

## Cross-border points

- **Tax havens** are always related parties. Payments to them also carry 37% withholding, and dividends 14% in the cases in ec-corporate-income-tax.
- **Treaties**: tax administrations may agree values jointly (RLRTI art. 88). Treaty corresponding adjustments and mutual agreement procedures are not covered here.
- **Share sales** between related parties: comparability looks at equity, projected cash flows or the last stock-exchange price. Losses on such sales are not deductible (LRTI art. 11; see ec-corporate-income-tax).

## Two worked examples that recompute

### Example 1: which filings are due? (a decision worked both ways)

Quito Distribuciones S.A. is an Ecuadorian company with ninth RUC digit 3. In 2026 it:
- buys goods from its foreign parent for USD 8,200,000;
- pays the parent USD 1,500,000 of management fees;
- receives a USD 2,000,000 cash capital contribution in dollars;
- buys USD 900,000 from a local sister company. The company used no tax incentive, has no tax-haven shareholders and its base is positive, so the local exclusion applies.

- **Counting total**: 8,200,000 + 1,500,000 = **USD 9,700,000**. The capital contribution and the local purchases are left out.
- **Result**: above USD 3,000,000, so the **Anexo is due**. Not above USD 10,000,000, so **no Informe Integral**. Both are due by 14 June 2027 (two months after its 14 April 2027 return date).
- **The other way**: if the company had taken the reinvestment rate reduction, the local exclusion would not apply. The total would be 9,700,000 + 900,000 = **USD 10,600,000**, and the **Informe Integral would also be due**.
- **The figure that decides** is whether the USD 900,000 counts. The USD 10,000,000 line sits between USD 9,700,000 and USD 10,600,000.

```oa-check
name: EC TP 2026, filing thresholds with and without the local exclusion
inputs:
  goods_from_parent: 8200000
  fees_to_parent: 1500000
  local_purchases: 900000
  anexo_threshold: 3000000
  informe_threshold: 10000000
steps:
  - counted_excluding_local: goods_from_parent + fees_to_parent
  - counted_including_local: counted_excluding_local + local_purchases
  - excess_over_anexo: counted_excluding_local - anexo_threshold
  - headroom_under_informe_a: informe_threshold - counted_excluding_local
  - excess_over_informe_b: counted_including_local - informe_threshold
expected:
  counted_excluding_local: 9700000
  counted_including_local: 10600000
  excess_over_anexo: 6700000
  headroom_under_informe_a: 300000
  excess_over_informe_b: 600000
```

### Example 2: margin outside the range, adjusted to the median

The same company is a distributor. It is tested with the transactional net margin method on operating margin. Its 2026 sales are USD 12,000,000 and its operating margin is 1.5%. The comparables give a first quartile of 2.8%, a median of 4.0% and a third quartile of 5.6%. It pays the 25% company rate.

- 1.5% is below the first quartile (2.8%), so it is outside the range. Adjust to the **median, 4.0%** (RLRTI art. 87).
- Adjustment: (4.0% − 1.5%) × 12,000,000 = **USD 300,000** added to the base.
- Extra income tax: 300,000 × 25% = **USD 75,000**, if the company makes the adjustment in its own return.
- If the SRI makes it in an audit instead, the 20% surcharge adds USD 15,000 (CT art. 90), plus interest.
- **Had the margin been 2.8% or more**, it would have been inside the range, with no adjustment.

```oa-check
name: EC TP 2026, TNMM adjustment to the median
inputs:
  sales: 12000000
  tested_margin: 0.015
  q1: 0.028
  median: 0.040
  rate: 0.25
steps:
  - gap_below_q1: round(q1 - tested_margin, 4)
  - adjustment: round((median - tested_margin) * sales, 2)
  - extra_tax: adjustment * rate
  - surcharge_if_assessed: extra_tax * 0.20
expected:
  gap_below_q1: 0.013
  adjustment: 300000
  extra_tax: 75000
  surcharge_if_assessed: 15000
```

## Ask the client first

1. Who owns the company, at every level, and with what percentages? Who sits on its board and in management, and who are their close relatives?
2. Which counterparties are in a tax haven, lower-tax jurisdiction or preferential regime? Does any one counterparty account for 50% or more of sales or purchases?
3. The year's related-party transactions by type (goods, services, royalties, loans, guarantees, share sales), counterparty and amount, foreign and local.
4. Did the company use any tax incentive, the reinvestment reduction, a ZEDE, or non-renewable resources, or declare a negative base? Each of these brings local transactions into the count.
5. Is it a large taxpayer or a special taxpayer on 1 January of the filing year? This sets the fine.
6. Does it have an approved advance pricing consultation, and does it have comparables and a benchmark for each transaction?

## Sources

| Source | URL | Read on |
|---|---|---|
| LRTI, SRI codification, last reform 2026-04-01: unnumbered articles after art. 4 (related parties, tax havens), after art. 15 (transfer pricing section) and after art. 22 (related-party transactions, fine) read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/12c884d5-c8d9-4171-becc-1513b990b87a/LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf | 2026-11-11 |
| RLRTI, SRI codification, last reform 2025-11-18: arts. 4, 72, 84-91 read | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/ee775a90-0ba9-48fe-85cb-9a52673c4c61/REGLAMENTO_PARA_APLICACION_LEY_DE_REGIMEN_TRIBUTARIO_INTERNO_LRTI.pdf | 2026-11-11 |
| SRI Resolution NAC-DGERCGC15-00000455 (RO second Supl. 511, 29 May 2015), original text: arts. 2-6 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/50db2d74-4e75-422a-9bc5-b3084d7bb018/NAC-DGERCGC15-00000455+2S.R.O.+511+29-05-2015.pdf | 2026-11-11 |
| SRI Resolution NAC-DGERCGC25-00000012 (7 Jun 2025): restates the USD 3,000,000 and USD 10,000,000 thresholds; extension for tax year 2024 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=1344f03a-3514-48dd-ba5c-c8a37d1e761f&nombre=NAC-DGERCGC25-00000012.pdf | 2026-11-11 |
| SRI Resolution NAC-DGERCGC24-00000020: amends Res. 15-455 art. 2, adds arts. 12-13 (taxpayer types and fines) | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=3c8e92c5-f276-46bd-a11e-7014601b270f&nombre=NAC-DGERCGC24-00000020.pdf | 2026-11-11 |
| Código Tributario, SRI codification, last modification RO 372 of 10 Aug 2023: arts. 21 and 90 | https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar/00682c30-727a-4268-b095-f485d226ce49/Codigo_Tributario_10082023.pdf | 2026-11-11 |

Not yet confirmed:
- the text of Resolution NAC-DGERCGC23-00000025, which moved the Informe threshold from USD 15,000,000 to USD 10,000,000 (read only as restated in Res. 25-00000012);
- the technical rules and method priority in Resolution NAC-DGERCGC16-00000532;
- the Anexo's due day by ninth digit for 2026 (two months after the return due date is assumed to give the same day two months later);
- the SRI's current tax-haven list;
- any country-by-country or master-file requirement;
- the rules for corresponding adjustments under treaties.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ec-transfer-pricing` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ec-transfer-pricing. If neither is available, confirm every figure against the official source pages cited above before relying on it.
