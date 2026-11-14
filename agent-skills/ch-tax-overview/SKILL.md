---
name: ch-tax-overview
description: "Overview of the Swiss tax system for tax year 2026, from the federal laws on fedlex and the Federal Tax Administration (ESTV). Covers the three levels of income tax (federal, cantonal, communal), residence, the 2026 federal income tax top rate, the 8.5% federal profit tax, cantonal wealth tax, VAT rates and threshold, the 35% withholding tax, AHV/IV/EO rates for the self-employed, lump-sum taxation and filing. Each point links to the 2026 skill that computes it: ch-federal-income-tax, ch-cantonal-tax, ch-corporate-income-tax, switzerland-vat, ch-ahv-iv, ch-lump-sum. Trigger on: Swiss tax system, how is Switzerland taxed, Swiss tax overview, Steuersystem Schweiz. Out of scope: any computation (use the linked skills), ch-payroll, ch-cross-border, ch-transfer-pricing."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/ch-tax-overview"
  jurisdiction: "CH"
  tax_year: "2026"
  last_updated: "2026-11-14"
---

# Switzerland Tax Overview v1.0

> **General reference only.** This skill is general tax reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts. Do not rely on it to file, pay or take a tax position without review by a qualified professional in Switzerland.

## Who this applies to

Anyone asking how Switzerland taxes people and companies in tax year 2026: residents, people moving in, and companies based there. Switzerland taxes income at three levels: federal (Confederation), cantonal (26 cantons) and communal, so the headline burden depends on where a taxpayer lives or a company is based. This file explains the system and routes to the skill that computes each tax; it computes nothing on its own beyond the two checks below. No accountant has signed it off yet.

### The system at a glance

Switzerland taxes income at three levels: federal (Confederation), cantonal (26 cantons) and communal. The headline burden therefore depends on where a taxpayer lives or a company is based. The figures below are for tax year 2026, read from the federal laws on fedlex and from ESTV and AHV/IV publications. No accountant has signed it off yet. For any computation, use the linked skill.

- **Tax year:** the calendar year is the tax period for federal income tax.  _([DBG art. 40 para. 1](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html.html))_
- **Currency:** Swiss franc (CHF).
- **Federal tax authority:** Federal Tax Administration (ESTV / AFC). The cantons assess and collect the direct federal tax under federal supervision.  _([ESTV](https://www.estv.admin.ch/); [DBG art. 2](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html.html))_
- **Federal taxes on income:** income tax on individuals, profit tax on legal persons, and tax at source on certain persons.  _([DBG art. 1](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html.html))_
- **Cantonal and communal taxes:** every canton must levy income and wealth tax on individuals, profit and capital tax on legal persons, tax at source and a real estate gains tax. Federal law (StHG) fixes the framework; each canton sets its own tariffs, rates and tax-free amounts, and communes add their own multipliers. See `ch-cantonal-tax`.  _([StHG art. 1 para. 3, art. 2 para. 1](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1256_1256_1256/20250101/de/html/fedlex-data-admin-ch-eli-cc-1991-1256_1256_1256-20250101-de-html.html))_
- **Residence basis:** an individual is fully liable if they have tax domicile in Switzerland, or stay at least 30 days while working or at least 90 days without working. Full liability does not extend to foreign businesses, permanent establishments and real estate. Non-residents are taxed only on Swiss-source items such as a Swiss business, permanent establishment or real estate. See `ch-federal-income-tax`, `ch-cross-border`.  _([DBG arts. 3, 4, 6](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html.html))_
- **Top federal personal income tax rate:** single tariff, 11.5% flat on the whole income from CHF 794,000 (CHF 91,310 at that point); married and single-parent tariff, 11.5% flat from CHF 941,400. Below those points the marginal rate reaches 13.2% on the single tariff and 13.0% on the married tariff. Cantonal and communal tax is added on top. See `ch-federal-income-tax`.  _([DBG art. 36 paras. 1, 2](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html.html), version of 2 September 2026)_
- **Corporate profit tax:** federal 8.5% of net profit. Taxes are deductible business expenses, so this is about 7.83% (8.5/108.5) of profit before tax. Cantonal and communal profit tax comes on top and differs by canton and commune; `ch-corporate-income-tax` builds the combined rate and works through Zurich city. Swiss entities of groups with annual consolidated revenue of EUR 750 million or more are also subject to the Swiss top-up tax (Ergänzungssteuer, Pillar Two); see `ch-corporate-income-tax`.  _([DBG art. 68, art. 59 para. 1 let. a](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html.html); [MindStV art. 8 para. 1](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2023/841/20260101/de/html/fedlex-data-admin-ch-eli-cc-2023-841-20260101-de-html.html))_
- **VAT (MWST / TVA / IVA):** standard rate 8.1%, reduced rate 2.6% (food, medicines, books and other listed items), 3.8% for accommodation until 31 December 2027. A business is exempt while its worldwide turnover is under CHF 100,000 a year. See `switzerland-vat`.  _([MWSTG art. 25 paras. 1, 2, 4; art. 10 para. 2 let. a](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2009/615/20250101/de/html/fedlex-data-admin-ch-eli-cc-2009-615-20250101-de-html.html); [ESTV, MWST-Steuersätze](https://www.estv.admin.ch/de/mwst-steuersaetze-schweiz))_
- **Net wealth tax:** levied only by the cantons and communes, on the whole net wealth of individuals. There is no federal wealth tax. Thresholds and rates are cantonal; see `ch-cantonal-tax`.  _([StHG art. 2 para. 1 let. a, art. 13 para. 1](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1256_1256_1256/20250101/de/html/fedlex-data-admin-ch-eli-cc-1991-1256_1256_1256-20250101-de-html.html); [DBG art. 1](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html.html))_
- **Withholding tax (Verrechnungssteuer):** 35% on Swiss capital income such as dividends and bank interest, and on certain lottery and gambling gains.  _([VStG art. 13 para. 1 let. a](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1966/371_385_384/20250101/de/html/fedlex-data-admin-ch-eli-cc-1966-371_385_384-20250101-de-html.html))_
- **Social contributions of the self-employed (AHV/IV/EO):** 10.0% in total (AHV 8.1%, IV 1.4%, EO 0.5%) on annual income from CHF 60,500; a lower sliding scale applies below that. See `ch-ahv-iv`; employees: `ch-payroll`.  _([AHV/IV leaflet 2.02, as at 1 January 2026](https://www.ahv-iv.ch/p/2.02.d))_
- **Lump-sum (expenditure-based) taxation:** foreign nationals who become resident for the first time, or after ten years away, and do not work in Switzerland may be taxed on their worldwide living costs instead of income, with a federal minimum base of the highest of CHF 435,000, seven times the annual rent or rental value of their home, and the other amounts listed in DBG art. 14 para. 3. See `ch-lump-sum`.  _([DBG art. 14 paras. 1, 3](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html.html))_
- **Individual return filing deadline:** one return covers federal, cantonal and communal income tax. The DBG requires a return even without a form but sets no calendar date; the canton does. In Zurich the 2026 return is due **31 March 2027**; an extension must be requested before that date, and requests made after it are not considered. Other cantons: `ch-cantonal-tax`.  _([DBG art. 124 paras. 1, 2](https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html.html); [Kantonales Steueramt Zürich, ZStB 133.1](https://www.zh.ch/de/steuern-finanzen/steuern/treuhaender/steuerbuch/steuerbuch-definition/zstb-133-1.html))_

### Skills in this pack

- `ch-federal-income-tax`: federal income tax on individuals, 2026 tariffs and deductions.
- `ch-cantonal-tax`: cantonal and communal income and wealth tax, multipliers, cantonal deadlines.
- `ch-corporate-income-tax`: federal and cantonal profit tax, capital tax, STAF measures, minimum tax.
- `switzerland-vat` and `ch-vat-return`: VAT registration, rates, methods and the return.
- `ch-ahv-iv`: AHV/IV/EO contributions of the self-employed and non-employed.
- `ch-lump-sum`: expenditure-based taxation.
- `ch-payroll`, `ch-cross-border`, `ch-transfer-pricing`: employees and tax at source, cross-border cases, transfer pricing.

## Rates, bands and thresholds

Federal figures for tax year 2026. Cantonal and communal rates come on top and are in `ch-cantonal-tax`.

| Item | Figure | Condition | Source |
|---|---|---|---|
| Full tax liability by stay | 30 days with gainful activity; 90 days without | DBG art 3 | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html.html |
| Federal income tax, top rate, single tariff | 11.5% flat on the whole income from CHF 794,000 (CHF 91,310 at that point); marginal rate below it up to 13.2% | DBG art 36 para 1 | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html.html |
| Federal income tax, top rate, married and single-parent tariff | 11.5% flat from CHF 941,400 (CHF 108,261 at that point); marginal rate below it up to 13.0% | DBG art 36 para 2 | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html.html |
| Federal profit tax | 8.5% of net profit | DBG art 68; taxes are deductible, so about 7.83% of profit before tax (computed) | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html.html |
| Swiss top-up tax (Pillar Two) | Groups with consolidated revenue of EUR 750 million or more | MindStV art 8 para 1 | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2023/841/20260101/de/html/fedlex-data-admin-ch-eli-cc-2023-841-20260101-de-html.html |
| VAT standard rate | 8.1% | MWSTG art 25 para 1 | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2009/615/20250101/de/html/fedlex-data-admin-ch-eli-cc-2009-615-20250101-de-html.html |
| VAT reduced rate | 2.6% | MWSTG art 25 para 2: food, medicines, books and the other listed items | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2009/615/20250101/de/html/fedlex-data-admin-ch-eli-cc-2009-615-20250101-de-html.html |
| VAT accommodation rate | 3.8% | MWSTG art 25 para 4, until 31 December 2027 at the latest | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2009/615/20250101/de/html/fedlex-data-admin-ch-eli-cc-2009-615-20250101-de-html.html |
| VAT registration exemption | Worldwide turnover under CHF 100,000 a year | MWSTG art 10 para 2 let a | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2009/615/20250101/de/html/fedlex-data-admin-ch-eli-cc-2009-615-20250101-de-html.html |
| Withholding tax (Verrechnungssteuer) | 35% | VStG art 13 para 1 let a: dividends, bank interest, certain lottery gains | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1966/371_385_384/20250101/de/html/fedlex-data-admin-ch-eli-cc-1966-371_385_384-20250101-de-html.html |
| AHV/IV/EO, self-employed | 10.0% (AHV 8.1%, IV 1.4%, EO 0.5%) from CHF 60,500 of annual income; sliding scale below | AHV/IV leaflet 2.02, as at 1 January 2026 | https://www.ahv-iv.ch/p/2.02.d |
| Lump-sum taxation, federal minimum base | CHF 435,000, or seven times the annual rent or rental value if higher | DBG art 14 para 3; first arrival or after ten years away, no Swiss work | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html.html |
| Fine for a procedural breach (federal tax) | Up to CHF 1,000; up to CHF 10,000 in serious cases or on repetition | DBG art 174 para 2, after a reminder | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html.html |
| Late payment interest, federal taxes | 4.0% | ESTV rate from 2026, unchanged for 2027 | https://www.estv.admin.ch/de/newnsb/58uetWbVftSvrQqxHgivI |

## The base

- **Individuals:** federal income tax on worldwide income of residents, less foreign businesses, permanent establishments and real estate (DBG arts 3 to 6); cantons add income and wealth tax under the StHG framework. There is no federal wealth tax.
- **Companies:** federal profit tax on net profit (DBG arts 57 to 68), cantonal profit and capital tax on top; `ch-corporate-income-tax` builds the combined rate.
- **Expenditure-based taxation:** worldwide living costs instead of income, with the minimum above; `ch-lump-sum`.
- **VAT:** turnover from taxable supplies in Switzerland; `switzerland-vat`.

## Deadlines and filing

- The tax year is the calendar year (DBG art 40 para 1).
- One return covers federal, cantonal and communal income tax. The DBG requires a return even without a form (art 124) but sets no date; the canton does. In Zurich the 2026 return is due **31 March 2027** ([ZStB 133.1](https://www.zh.ch/de/steuern-finanzen/steuern/treuhaender/steuerbuch/steuerbuch-definition/zstb-133-1.html)); an extension must be requested before that date. Other cantons: `ch-cantonal-tax`.

## Penalties and interest

- A taxpayer who fails a procedural duty after a reminder (no return, no attachments, no information) is fined up to CHF 1,000, or up to CHF 10,000 in serious cases or on repetition (DBG art 174).
- Late payment interest on federal taxes is 4.0% from 2026 and unchanged for 2027 (ESTV).
- Evasion (DBG art 175) is fined as a multiple of the tax evaded; see `ch-federal-income-tax`.

## Cross-border points

- Residence starts with domicile or a stay of 30 days with work or 90 days without (DBG art 3). Arrivals, departures and non-residents: `ch-cross-border`.
- The 35% Verrechnungssteuer is refundable to residents who declare the income and, under a treaty, partly to non-residents.
- Foreign employees without a C permit are taxed at source; `ch-payroll` and `ch-cross-border`.

## Two worked examples that recompute

### Example 1: federal income tax at the top of the single tariff

A single resident has taxable federal income of CHF 1,000,000 in 2026. At or above CHF 794,000 the single tariff taxes the whole income at 11.5% (DBG art 36 para 1): CHF 115,000. Cantonal and communal tax comes on top.

```oa-check
name: Switzerland 2026 federal income tax top single tariff
inputs:
  income: 1000000
  rate: 0.115
steps:
  - federal_tax: income * rate
expected:
  federal_tax: 115000
```

### Example 2: register for VAT or not? (a decision)

A consultant expects CHF 95,000 of worldwide turnover in 2026; a second year is projected at CHF 105,000. Below CHF 100,000 the business is exempt from VAT liability (MWSTG art 10 para 2 let a); at CHF 105,000 it is liable and charges 8.1%, CHF 8,505 of output VAT on that turnover if all of it is standard-rated. The figure that decides is the CHF 100,000 line, measured on worldwide turnover, not only Swiss.

```oa-check
name: Switzerland 2026 VAT registration threshold decision
inputs:
  turnover_year1: 95000
  turnover_year2: 105000
  threshold: 100000
  rate: 0.081
steps:
  - headroom_year1: threshold - turnover_year1
  - excess_year2: turnover_year2 - threshold
  - output_vat_year2: turnover_year2 * rate
expected:
  headroom_year1: 5000
  excess_year2: 5000
  output_vat_year2: 8505
```

## Ask the client first

- Where do you live (canton and commune), or where is the company based? Every cantonal figure depends on it.
- Are you resident, arriving, leaving or non-resident in 2026?
- Are you employed (with or without a C permit), self-employed, or a company?
- What is your worldwide turnover, if you sell goods or services? It decides VAT liability.
- Are you a foreign national with no Swiss work who might use lump-sum taxation?

## Sources

| Source | What was read | URL | Read on |
|---|---|---|---|
| Fedlex, DBG, SR 642.11, consolidated version of 2 September 2026 | Read for arts 1 to 6, 14 (CHF 435,000), 36 (CHF 794,000, CHF 941,400, 11.5%), 40, 59, 68 (8.5%), 124, 174 (CHF 1,000 and 10,000) | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1184_1184_1184/20260902/de/html/fedlex-data-admin-ch-eli-cc-1991-1184_1184_1184-20260902-de-html.html | 2026-11-14 |
| Fedlex, StHG, SR 642.14, version of 1 January 2025 | Read for arts 1 to 3 and 13 (cantonal taxes, wealth tax) | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1991/1256_1256_1256/20250101/de/html/fedlex-data-admin-ch-eli-cc-1991-1256_1256_1256-20250101-de-html.html | 2026-11-14 |
| Fedlex, MWSTG, SR 641.20, version of 1 January 2025 | Read for arts 10 para 2 (CHF 100,000) and 25 (8.1%, 2.6%, 3.8%) | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2009/615/20250101/de/html/fedlex-data-admin-ch-eli-cc-2009-615-20250101-de-html.html | 2026-11-14 |
| Fedlex, MindStV, SR 642.161, version of 1 January 2026 | Read for art 8 para 1 (EUR 750 million) | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/2023/841/20260101/de/html/fedlex-data-admin-ch-eli-cc-2023-841-20260101-de-html.html | 2026-11-14 |
| Fedlex, VStG, SR 642.21, version of 1 January 2025 | Read for art 13 (35%) | https://www.fedlex.admin.ch/filestore/fedlex.data.admin.ch/eli/cc/1966/371_385_384/20250101/de/html/fedlex-data-admin-ch-eli-cc-1966-371_385_384-20250101-de-html.html | 2026-11-14 |
| ESTV, MWST-Steuersätze Schweiz | Read for the current VAT rates page | https://www.estv.admin.ch/de/mwst-steuersaetze-schweiz | 2026-11-14 |
| ESTV, Verzugs- und Vergütungszinssätze ab 2026 | Read for the 4.0% late payment rate | https://www.estv.admin.ch/de/newnsb/58uetWbVftSvrQqxHgivI | 2026-11-14 |
| Informationsstelle AHV/IV, Merkblatt 2.02, Stand 1. Januar 2026 | Read for the 10.0% total (8.1%, 1.4%, 0.5%) and the CHF 60,500 line | https://www.ahv-iv.ch/p/2.02.d | 2026-11-14 |
| Kantonales Steueramt Zürich, ZStB 133.1 | Read for the 31 March 2027 filing date for the 2026 return | https://www.zh.ch/de/steuern-finanzen/steuern/treuhaender/steuerbuch/steuerbuch-definition/zstb-133-1.html | 2026-11-14 |

Not yet confirmed: the range of combined federal, cantonal and communal profit tax rates across the 26 cantons and the national average (the old version gave about 11.85% to 21.6% and about 14.4% from a non-official source; no ESTV table of effective rates by canton was read for 2026); the 2026 filing deadline in every canton other than Zurich (`ch-cantonal-tax` covers Zurich, Zug, Bern, Basel-Stadt, Geneva and Vaud).

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-14. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `ch-tax-overview` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/ch-tax-overview. If neither is available, confirm every figure against the official source pages cited above before relying on it.
