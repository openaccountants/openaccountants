---
name: uy-transfer-pricing
description: "Uruguay transfer pricing (precios de transferencia) for IRAE, tax year 2026, under Título 4 Capítulo VIII (arts. 46 to 58) of the Texto Ordenado 2023, Decreto 56/009 and Decreto 353/018. Covers who is in scope (IRAE taxpayers dealing with related non-residents, professionals in IRAE, anyone dealing with low or no-tax jurisdictions or low-tax free zones), the control test of related parties, the irrebuttable presumption for low-tax jurisdictions (effective rate under 12% and no information exchange), the five methods, the interquartile range and the median plus or minus 5% adjustment, quoted commodities and foreign intermediaries (30% test), contract registration, advance pricing agreements up to three years, the annual form 3001 and study above UI 50,000,000 due in the ninth month, country-by-country and master file for groups of EUR 750 million within 12 months, and the penalty of up to 1,000 times the maximum contravention fine. Trigger on: precios de transferencia Uruguay, formulario 3001, estudio de precios de transferencia, informe país por país, Uruguay transfer pricing."
version: 0.1
jurisdiction: UY
tax_year: 2026
last_updated: 2026-11-11
category: transfer-pricing
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: transfer-pricing
type: computation
---

# Uruguay: transfer pricing for IRAE, 2026 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

This skill decides whether a Uruguayan IRAE taxpayer is inside the transfer-pricing regime, how an arm's length price is tested and adjusted, and what must be filed for 2026. The IRAE computation itself, the 25% rate and the proportional deduction for payments to low-taxed recipients are in [uy-corporate-income-tax](uy-corporate-income-tax.md).

**Which text of the law.** Título 4 (IRAE), Capítulo VIII "Precios de transferencia", arts. 46 to 58, of the Texto Ordenado 2023 approved by Decreto 101/024, as consolidated by IMPO. The regulation is Decreto 56/009; country-by-country reporting is regulated by Decreto 353/018. Both decrees still cite the 1996 numbering (Capítulo VII, arts. 38 to 46 ter of Título 4), which is today's Capítulo VIII.

**Quick reference, 2026**

| Item | Figure |
|---|---|
| Who | IRAE taxpayers with transactions with related non-residents or with low-tax jurisdictions (T4 arts. 46 to 48; Decreto 56/009 art. 1) |
| Range | Interquartile range; outside it, adjust to the median minus or plus 5% (Decreto 56/009 art. 8) |
| Annual filing | Form 3001 and the study, if covered transactions exceed UI 50,000,000 or the DGI notifies the taxpayer, in the ninth month after year-end |
| CbC report and master file | Groups with consolidated revenue of EUR 750,000,000 or more, within 12 months after year-end (Decreto 353/018) |
| Penalty for formal breaches | Up to 1,000 times the maximum contravention fine: UYU 13,220,000 in 2026 |

## Who this applies to

- **In scope** (Decreto 56/009 art. 1): businesses taxed under T4 art. 12 that deal with related entities abroad; independent professionals taxed in IRAE by option or compulsorily who deal with related entities abroad; and anyone dealing with entities in low or no-tax countries, jurisdictions or regimes, including entities in customs enclaves (free zones) with a low-tax regime.
- **Related parties** (T4 art. 47): a taxpayer and a non-resident (or a low-tax enclave entity) are related when both are under the direct or indirect direction or control of the same persons, through capital, credit, functional influence or any other contractual or non-contractual means that gives decision power over the taxpayer's activity. Branches, subsidiaries and permanent establishments abroad are included (art. 46).
- **Low or no-tax jurisdictions** (T4 art. 48; Decreto 56/009 art. 3): any transaction with them is presumed, with no proof to the contrary admitted, to be between related parties and not at arm's length, so it must always be adjusted to the methods. A jurisdiction is low-tax if it taxes Uruguayan-source income at an effective rate below 12% and has no information-exchange agreement (or one that is not fully applicable or not honoured). The DGI keeps the list.
- **Low-tax enclaves** (Decreto 56/009 art. 3 bis): free zones, free ports and similar areas whose effective income-tax rate is below 40% of the IRAE rate. Sales from Uruguayan territory to an enclave entity in Uruguay for use only inside the enclave are excluded.
- **Free-zone users** (T4 art. 58) are jointly liable for adjustments on transactions with related IRAE taxpayers; exclusive distribution contracts do not by themselves create the relationship unless they are at least 50% of the taxpayer's income.
- **Out of scope.** Domestic transactions between two Uruguayan IRAE taxpayers (the regime covers non-residents and low-tax enclaves), IRPF taxpayers, and the domestic minimum top-up tax (see the corporate skill).

## Rates, bands and thresholds

| Item | Rate or amount | Year | Source URL |
|---|---|---|---|
| Arm's length rule and burden: the DGI must prove the price is not at market | Rule | 2026 | https://www.impo.com.uy/bases/todgi-2023/4-2024 (T4 art. 46) |
| Methods: comparable uncontrolled price, resale price, cost plus, profit split, transactional net margin; most appropriate one applies | Five methods | 2026 | same, art. 49; https://www.impo.com.uy/bases/decretos/56-2009 (art. 4) |
| Two or more comparables | Compute the median and interquartile range; a result inside the range is accepted | 2026 | https://www.impo.com.uy/bases/decretos/56-2009 (art. 8) |
| Result below the first quartile | Adjusted to the median reduced by 5% | 2026 | same, art. 8 |
| Result above the third quartile | Adjusted to the median increased by 5% | 2026 | same, art. 8 |
| Narrow range | If the first quartile is above median minus 5%, the latter replaces it; if the third quartile is below median plus 5%, the latter replaces it | 2026 | same, art. 8 |
| Low-tax jurisdiction test | Effective tax on Uruguayan-source income below 12% and no effective information exchange | 2026 | same, art. 3 |
| Low-tax enclave test | Effective income-tax rate below 40% of the IRAE rate (25%) | 2026 | same, art. 3 bis |
| Quoted goods imported from a related party | Highest quotation on a transparent market if the agreed price is higher | 2026 | same, arts. 9 bis, 13; T4 art. 50 |
| Quoted goods exported to a related party | Lowest quotation if the agreed price is lower | 2026 | same, arts. 9 bis, 13 |
| Quoted goods through a foreign intermediary that is not the real buyer | Quotation on the day of loading, whatever price was agreed with the intermediary, unless the intermediary has real substance, mainly active income, and related-party trade of no more than 30% of its operations | 2026 | https://www.impo.com.uy/bases/todgi-2023/4-2024 (T4 art. 51) |
| Optional registration of sale contracts for quoted goods | Registered within 5 working days of the month after signing; the quotation is then taken at the contract date instead of the shipping date | 2026 | https://www.impo.com.uy/bases/decretos/56-2009 (arts. 13, 13 bis) |
| Advance pricing agreement | Signed before the transactions; at most three fiscal years; bilateral possible under tax treaties | 2026 | same, art. 15 bis; T4 art. 53 |
| Supporting documentation on request | At least 8 months from the year-end to provide it | 2026 | same, art. 15 |
| Form 3001 and study: covered transactions above UI 50,000,000 in the fiscal year (free-zone users not taxed by IRAE excepted), or DGI notification | Required | 2026 | https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/precios-transferencia-formulario-3001 |
| Country-by-country report and master file | Groups with consolidated revenue of EUR 750,000,000 or more in the year before the reporting year; filed within 12 months after the reporting year-end | 2026 | https://www.impo.com.uy/bases/decretos/353-2018 (arts. 5, 9) |
| Penalty for breaching transfer-pricing formal duties | Up to 1,000 times the maximum contravention fine, graded by gravity; with the 2026 maximum of UYU 13,220 that is up to UYU 13,220,000 | 2026 | https://www.impo.com.uy/bases/todgi-2023/4-2024 (T4 art. 57); https://www.impo.com.uy/bases/leyes/17930-2005/469; https://www.impo.com.uy/bases/decretos/344-2025 |

## The base

1. **Is the taxpayer in scope?** IRAE taxpayer (or professional in IRAE), and a transaction with a related non-resident or with any party in a low-tax jurisdiction or low-tax enclave.
2. **Choose the method** most appropriate to the transaction (T4 art. 49). Decreto 56/009 art. 9 rules out the comparable uncontrolled price where products, markets, volumes, financial conditions or intangibles are not comparable. For goods with a public quoted price, the quotation rules of arts. 50 and 51 apply first.
3. **Comparability** (Decreto 56/009 arts. 6, 7): characteristics of the transaction (loan amount, term, guarantees and rate; nature of services; physical features of goods; type of intangible), functions, assets and risks, contract terms and economic circumstances. Adjust for payment terms, volume discounts, advertising borne, intermediation costs, packaging, freight and insurance, and timing (IPC and exchange rate). The analysis may test either the Uruguayan party or the foreign one; testing the foreign party needs audited, translated and legalised evidence (art. 5).
4. **Range and adjustment** (art. 8): with two or more comparables, compute quartiles and median; inside the range, no adjustment; outside, move to median minus 5% or plus 5%.
5. **Adjust the IRAE base** by the difference between the arm's length result and the result booked, then apply 25%.
6. **Document and file:** form 3001 with the study if the threshold is met; CbC notification, report and master file if the group is large.

## Deadlines and filing

| Step | What and where | Source |
|---|---|---|
| Form 3001 | Generated with the DGI Sigma application (version 2.0); filed online through Servicios en Línea with a web contract: a .txt file from Sigma plus the study as a PDF named 3001_aaaamm_rut.pdf, under 1 MB | [DGI, form 3001](https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/precios-transferencia-formulario-3001) |
| Due date | Ninth month after the fiscal year-end, on the date of the general deadline table for the group and last RUT digit; for a calendar 2026 year, September 2027 | same |
| Paper fallback | Magnetic media at DGI offices only if web filing fails, with a signed summary sheet bearing the professional stamp | same |
| CbC: identify the reporting entity | The local entity tells the DGI which group entity reports and where | [T4 art. 56](https://www.impo.com.uy/bases/todgi-2023/4-2024) |
| CbC report and master file | Special sworn returns within 12 months after the reporting year-end, unless the report is filed abroad and exchanged with Uruguay | [Decreto 353/018 art. 9](https://www.impo.com.uy/bases/decretos/353-2018) |
| IRAE adjustment | Included in the IRAE return (form 1050) for the year | [uy-corporate-income-tax](uy-corporate-income-tax.md) |

## Penalties and interest

- **Formal breaches** of the regime (no form, no study, incomplete information): graded fine up to 1,000 times the maximum contravention fine under Ley 17.930 art. 469 (T4 art. 57), so up to UYU 13,220,000 in 2026 using Decreto 344/025.
- **Tax shortfall** from an adjustment: the IRAE difference, with the mora fine (5%, 10% or 20%) and the monthly surcharge under Código Tributario art. 94.
- **CbC data alone** cannot ground an adjustment (Decreto 353/018 art. 8).

## Cross-border points

- **Treaty APAs**: bilateral advance pricing agreements are possible with treaty partners (T4 art. 53; Decreto 56/009 art. 15 bis).
- **Deduction limits** still apply alongside transfer pricing: payments to recipients taxed below 25% are deducted only in proportion (T4 art. 31; see the corporate skill).
- **Permanent establishments**: dealings between a Uruguayan PE and its head office are treated as between independent parties if on market terms (Decreto 150/007 art. 63 bis).

## Two worked examples that recompute

### Example 1: distributor below the range

Sur Distribuciones SA buys products from its Spanish parent and resells them in Uruguay. For 2026 its sales are UYU 50,000,000 and its operating profit UYU 2,500,000, a 5% operating margin. The study uses the transactional net margin method; the comparable distributors' operating margins give a first quartile of 8%, a median of 10% and a third quartile of 12%.

The 5% margin is below the first quartile, so it is adjusted to the median reduced by 5%: 10% x 0.95 = 9.5%. (The first quartile, 8%, is not above 9.5%, so the range is not narrowed.) The arm's length operating profit is 9.5% of UYU 50,000,000 = UYU 4,750,000. The IRAE base rises by UYU 2,250,000 and the extra IRAE is UYU 562,500. If its covered transactions with the parent exceed UI 50,000,000 for the year, form 3001 and the study are due in September 2027.

```oa-check
name: UY TP 2026, TNMM margin below first quartile
inputs:
  sales: 50000000
  operating_profit: 2500000
  q1: 0.08
  median: 0.10
  q3: 0.12
steps:
  - margin: operating_profit / sales
  - adjusted_margin: median * 0.95
  - lower_bound: max(q1, median * 0.95)
  - arm_length_profit: sales * adjusted_margin
  - adjustment: arm_length_profit - operating_profit
  - extra_irae: adjustment * 0.25
expected:
  margin: 0.05
  adjusted_margin: 0.095
  lower_bound: 0.095
  arm_length_profit: 4750000
  adjustment: 2250000
  extra_irae: 562500
```

Note on the range: because median minus 5% (9.5%) is above the first quartile (8%), art. 8 makes 9.5% the effective lower bound; a margin of 9% would also have been adjusted to 9.5%.

### Example 2: should an exporter register its soybean contract?

Agro Este SA sells 10,000 tonnes of soybeans to a related buyer abroad at USD 370 a tonne. On the contract date the lowest quotation on the reference market is USD 400; on the bill-of-lading date it will be either USD 380 (prices fall) or USD 420 (prices rise). For exports to a related party below the quotation, the lowest quotation applies (Decreto 56/009 arts. 9 bis, 13): at the contract date if the contract was registered within 5 working days of the next month, otherwise at the bill-of-lading date.

If prices fall: registered, the price is lifted to USD 400, an adjustment of USD 300,000 (USD 75,000 of IRAE); unregistered, it is lifted to USD 380, an adjustment of USD 100,000 (USD 25,000 of IRAE). If prices rise: registered, the adjustment stays USD 300,000; unregistered, it becomes USD 500,000 (USD 125,000 of IRAE).

The decision: registration fixes the quotation at the contract date. It costs USD 50,000 of IRAE if prices fall and saves USD 50,000 if they rise. It removes the timing risk rather than lowering the expected tax; the cleaner fix is to price the related-party sale at the quotation in the first place.

```oa-check
name: UY TP 2026, registering a quoted-commodity export contract
inputs:
  tonnes: 10000
  agreed: 370
  quote_contract: 400
  quote_bl_fall: 380
  quote_bl_rise: 420
steps:
  - adj_registered: (max(agreed, quote_contract) - agreed) * tonnes
  - adj_unreg_fall: (max(agreed, quote_bl_fall) - agreed) * tonnes
  - adj_unreg_rise: (max(agreed, quote_bl_rise) - agreed) * tonnes
  - irae_registered: adj_registered * 0.25
  - irae_unreg_fall: adj_unreg_fall * 0.25
  - irae_unreg_rise: adj_unreg_rise * 0.25
  - cost_of_registering_if_fall: irae_registered - irae_unreg_fall
  - saving_of_registering_if_rise: irae_unreg_rise - irae_registered
expected:
  adj_registered: 300000
  adj_unreg_fall: 100000
  adj_unreg_rise: 500000
  irae_registered: 75000
  irae_unreg_fall: 25000
  irae_unreg_rise: 125000
  cost_of_registering_if_fall: 50000
  saving_of_registering_if_rise: 50000
```

## Ask the client first

1. Is the client an IRAE taxpayer, and which foreign counterparties are related by capital, credit, functional influence or contract?
2. Does any counterparty sit in a low or no-tax jurisdiction on the DGI list, or in a free zone or other enclave with a low-tax regime?
3. Total value of covered transactions in the fiscal year, in pesos and in UI (the UI 50,000,000 test), and whether the DGI has sent a notification.
4. The transactions by type (goods, quoted commodities, services, royalties, loans), the method used last year and the comparables.
5. Group consolidated revenue in the previous year (EUR 750 million test), the ultimate parent and who files the CbC report.
6. Any advance pricing agreement, registered commodity contracts or foreign intermediaries.

## Sources

| Source | URL | Read on |
|---|---|---|
| Texto Ordenado 2023, Título 4, Capítulo VIII, arts. 46 to 58 read in full | https://www.impo.com.uy/bases/todgi-2023/4-2024 | 2026-11-11 |
| Decreto 56/009 (transfer-pricing regulation), arts. 1 to 16 read | https://www.impo.com.uy/bases/decretos/56-2009 | 2026-11-11 |
| Decreto 353/018 (country-by-country and master file), arts. 3 to 10 read | https://www.impo.com.uy/bases/decretos/353-2018 | 2026-11-11 |
| DGI, Precios de transferencia formulario 3001 (guide of 13 October 2023), read for who files, the UI 50,000,000 test and the ninth-month deadline | https://www.gub.uy/direccion-general-impositiva/comunicacion/publicaciones/precios-transferencia-formulario-3001 | 2026-11-11 |
| Ley 17.930, art. 469 (fine up to 1,000 times the maximum contravention fine) | https://www.impo.com.uy/bases/leyes/17930-2005/469 | 2026-11-11 |
| Decreto 344/025, arts. 1 and 2: contravención maximum UYU 13,220 for 2026 | https://www.impo.com.uy/bases/decretos/344-2025 | 2026-11-11 |
| Código Tributario, art. 94 (mora) | https://www.impo.com.uy/bases/codigo-tributario/14306-1974/94 | 2026-11-11 |

Not yet confirmed: the text of Resolución DGI 2084/009 numeral 10 and its amendments (Res. 2098/009, 745/011), which IMPO did not serve; the DGI guide is cited for the UI 50,000,000 test instead; the current DGI list of low or no-tax jurisdictions; the additional filing and payment periods of Resolución DGI 1881/010; the exact September 2027 day in the deadline table; the UI quotation that converts the UI 50,000,000 test; the CbC notification deadline set by the DGI; the presumed-profit regimes the Executive may set under T4 art. 52.

> Contributed by Michael Cutajar.
