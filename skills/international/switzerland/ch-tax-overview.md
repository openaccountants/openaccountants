---
name: ch-tax-overview
description: "Overview of the Swiss tax system for tax year 2026, from the federal laws on fedlex and the Federal Tax Administration (ESTV). Covers the three levels of income tax (federal, cantonal, communal), residence, the 2026 federal income tax top rate, the 8.5% federal profit tax, cantonal wealth tax, VAT rates and threshold, the 35% withholding tax, AHV/IV/EO rates for the self-employed, lump-sum taxation and filing. Each point links to the 2026 skill that computes it: ch-federal-income-tax, ch-cantonal-tax, ch-corporate-income-tax, switzerland-vat, ch-ahv-iv, ch-lump-sum. Trigger on: Swiss tax system, how is Switzerland taxed, Swiss tax overview, Steuersystem Schweiz. Out of scope: any computation (use the linked skills), ch-payroll, ch-cross-border, ch-transfer-pricing."
version: 0.2
jurisdiction: CH
tax_year: 2026
last_updated: 2026-10-30
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Switzerland Tax Overview

## The Swiss tax system at a glance

Switzerland taxes income at three levels: federal (Confederation), cantonal (26 cantons) and communal. The headline burden therefore depends on where a taxpayer lives or a company is based. The figures below are for tax year 2026, read from the federal laws on fedlex and from ESTV and AHV/IV publications. This is a source-cited draft; no accountant has reviewed it. For any computation, use the linked skill.

- **Tax year:** the calendar year is the tax period for federal income tax.  _([DBG art. 40 para. 1](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de))_
- **Currency:** Swiss franc (CHF).
- **Federal tax authority:** Federal Tax Administration (ESTV / AFC). The cantons assess and collect the direct federal tax under federal supervision.  _([ESTV](https://www.estv.admin.ch/); [DBG art. 2](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de))_
- **Federal taxes on income:** income tax on individuals, profit tax on legal persons, and tax at source on certain persons.  _([DBG art. 1](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de))_
- **Cantonal and communal taxes:** every canton must levy income and wealth tax on individuals, profit and capital tax on legal persons, tax at source and a real estate gains tax. Federal law (StHG) fixes the framework; each canton sets its own tariffs, rates and tax-free amounts, and communes add their own multipliers. See `ch-cantonal-tax`.  _([StHG art. 1 para. 3, art. 2 para. 1](https://www.fedlex.admin.ch/eli/cc/1991/1256_1256_1256/de))_
- **Residence basis:** an individual is fully liable if they have tax domicile in Switzerland, or stay at least 30 days while working or at least 90 days without working. Full liability does not extend to foreign businesses, permanent establishments and real estate. Non-residents are taxed only on Swiss-source items such as a Swiss business, permanent establishment or real estate. See `ch-federal-income-tax`, `ch-cross-border`.  _([DBG arts. 3, 4, 6](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de))_
- **Top federal personal income tax rate:** single tariff, 11.5% flat on the whole income from CHF 794,000 (CHF 91,310 at that point); married and single-parent tariff, 11.5% flat from CHF 941,400. Below those points the marginal rate reaches 13.2%. Cantonal and communal tax is added on top. See `ch-federal-income-tax`.  _([DBG art. 36 paras. 1, 2](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de), version of 2 September 2026)_
- **Corporate profit tax:** federal 8.5% of net profit. Taxes are deductible business expenses, so this is about 7.83% (8.5/108.5) of profit before tax. Cantonal and communal profit tax comes on top and differs by canton and commune; `ch-corporate-income-tax` builds the combined rate and works through Zurich city. Swiss entities of groups with annual consolidated revenue of EUR 750 million or more are also subject to the Swiss top-up tax (Ergänzungssteuer, Pillar Two); see `ch-corporate-income-tax`.  _([DBG art. 68, art. 59 para. 1 let. a](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de); [MindStV art. 8 para. 1](https://www.fedlex.admin.ch/eli/cc/2023/841/de))_
- **VAT (MWST / TVA / IVA):** standard rate 8.1%, reduced rate 2.6% (food, medicines, books and other listed items), 3.8% for accommodation until 31 December 2027. A business is exempt while its worldwide turnover is under CHF 100,000 a year. See `switzerland-vat`.  _([MWSTG art. 25 paras. 1, 2, 4; art. 10 para. 2 let. a](https://www.fedlex.admin.ch/eli/cc/2009/615/de); [ESTV, MWST-Steuersätze](https://www.estv.admin.ch/de/mwst-steuersaetze-schweiz))_
- **Net wealth tax:** levied only by the cantons and communes, on the whole net wealth of individuals. There is no federal wealth tax. Thresholds and rates are cantonal; see `ch-cantonal-tax`.  _([StHG art. 2 para. 1 let. a, art. 13 para. 1](https://www.fedlex.admin.ch/eli/cc/1991/1256_1256_1256/de); [DBG art. 1](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de))_
- **Withholding tax (Verrechnungssteuer):** 35% on Swiss capital income such as dividends and bank interest, and on certain lottery and gambling gains.  _([VStG art. 13 para. 1 let. a](https://www.fedlex.admin.ch/eli/cc/1966/371_385_384/de))_
- **Social contributions of the self-employed (AHV/IV/EO):** 10.0% in total (AHV 8.1%, IV 1.4%, EO 0.5%) on annual income from CHF 60,500; a lower sliding scale applies below that. See `ch-ahv-iv`; employees: `ch-payroll`.  _([AHV/IV leaflet 2.02, as at 1 January 2026](https://www.ahv-iv.ch/p/2.02.d))_
- **Lump-sum (expenditure-based) taxation:** foreign nationals who become resident for the first time, or after ten years away, and do not work in Switzerland may be taxed on their worldwide living costs instead of income, with a federal minimum base of CHF 435,000. See `ch-lump-sum`.  _([DBG art. 14 paras. 1, 3](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de))_
- **Individual return filing deadline:** one return covers federal, cantonal and communal income tax. The DBG requires a return even without a form but sets no calendar date; the canton does. In Zurich the 2026 return is due **31 March 2027**. Other cantons: `ch-cantonal-tax`.  _([DBG art. 124 paras. 1, 2](https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de); [Kantonales Steueramt Zürich, ZStB 133.1](https://www.zh.ch/de/steuern-finanzen/steuern/treuhaender/steuerbuch/steuerbuch-definition/zstb-133-1.html))_

## Skills in this pack

- `ch-federal-income-tax`: federal income tax on individuals, 2026 tariffs and deductions.
- `ch-cantonal-tax`: cantonal and communal income and wealth tax, multipliers, cantonal deadlines.
- `ch-corporate-income-tax`: federal and cantonal profit tax, capital tax, STAF measures, minimum tax.
- `switzerland-vat` and `ch-vat-return`: VAT registration, rates, methods and the return.
- `ch-ahv-iv`: AHV/IV/EO contributions of the self-employed and non-employed.
- `ch-lump-sum`: expenditure-based taxation.
- `ch-payroll`, `ch-cross-border`, `ch-transfer-pricing`: employees and tax at source, cross-border cases, transfer pricing.

## Sources

| Source | URL | Read on |
| --- | --- | --- |
| Fedlex, Bundesgesetz über die direkte Bundessteuer (DBG), SR 642.11, version of 2 September 2026 (arts. 1 to 4, 6, 14, 36, 40, 59, 68, 124) | https://www.fedlex.admin.ch/eli/cc/1991/1184_1184_1184/de | 2026-10-30 |
| Fedlex, Steuerharmonisierungsgesetz (StHG), SR 642.14, version of 1 January 2025 (arts. 1 to 3, 13) | https://www.fedlex.admin.ch/eli/cc/1991/1256_1256_1256/de | 2026-10-30 |
| Fedlex, Mehrwertsteuergesetz (MWSTG), SR 641.20, version of 31 March 2025 (arts. 10, 25) | https://www.fedlex.admin.ch/eli/cc/2009/615/de | 2026-10-30 |
| Fedlex, Mindestbesteuerungsverordnung (MindStV), SR 642.161, version of 1 January 2026 (art. 8) | https://www.fedlex.admin.ch/eli/cc/2023/841/de | 2026-10-30 |
| Fedlex, Verrechnungssteuergesetz (VStG), SR 642.21, version of 1 January 2025 (art. 13) | https://www.fedlex.admin.ch/eli/cc/1966/371_385_384/de | 2026-10-30 |
| Federal Tax Administration (ESTV) | https://www.estv.admin.ch/ | 2026-10-30 |
| ESTV, MWST-Steuersätze Schweiz | https://www.estv.admin.ch/de/mwst-steuersaetze-schweiz | 2026-10-30 |
| Informationsstelle AHV/IV, Merkblatt 2.02 Beiträge der Selbstständigerwerbenden, Stand 1. Januar 2026 | https://www.ahv-iv.ch/p/2.02.d | 2026-10-30 |
| Kantonales Steueramt Zürich, ZStB 133.1 (filing deadline 2026 return) | https://www.zh.ch/de/steuern-finanzen/steuern/treuhaender/steuerbuch/steuerbuch-definition/zstb-133-1.html | 2026-10-30 |

Not yet confirmed: the range of combined federal, cantonal and communal profit tax rates across the 26 cantons and the national average (the old version gave about 11.85% to 21.6% and about 14.4% from a non-official source; no ESTV table of effective rates by canton was read for 2026); the 2026 filing deadline in every canton other than Zurich (`ch-cantonal-tax` covers Zurich, Zug, Bern, Basel-Stadt, Geneva and Vaud).

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
