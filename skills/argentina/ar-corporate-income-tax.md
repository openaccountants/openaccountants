---
name: ar-corporate-income-tax
description: >
  Use this Guide for Argentine corporate income tax in fiscal years beginning
  in 2026: Impuesto a las Ganancias sociedades, Ganancias Personas Juridicas,
  F.713, corporate brackets, ajuste por inflacion, quebrantos and anticipos.
  It covers resident companies and domestic permanent establishments, the
  indexed progressive scale, the tax reconciliation, loss restrictions,
  dividends and branch remittances, ordinary annual filing, the October 2026
  web-service transition and advance payments. It prepares a source-cited
  working paper for a local professional to review. Related-party pricing and
  foreign-beneficiary category computations are routed to the specialist
  Argentina Guides. It does not compute promotion regimes, gaming income,
  reorganisations or provincial turnover tax.
version: 0.1
jurisdiction: AR
tax_year: 2026
tax_year_notes: "Corporate fiscal years beginning during 2026; the return filing year can be 2027."
last_updated: 2026-11-11
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: computation
---

# Argentina: corporate income tax 2026 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Resident capital companies and other entities in LIG art. 73(a), and Argentine permanent establishments under art. 73(b). This includes SA/SAU, SRL and SAS and the other listed entities where no exemption or separate treatment applies. A partnership/unincorporated business is not automatically a capital company: test its classification and any art. 73(a)(8) election. That election requires commercial accounts and remains effective for five fiscal periods.

**Quick answer:** the 2026 scale depends on the fiscal year's opening date, not the year a return is submitted. Reconcile accounts to taxable income, keep domestic/foreign source and restricted losses separate, apply the indexed scale, then eligible credits and actual advance payments. Get entity form, year opening/closing dates, accounts and tax adjustments, loss history and credits first.

This Tier 2 draft has no professional approval. It produces the tax bridge, computation, filing calendar and unresolved-issues list. Resident companies are taxed on worldwide income; foreign tax credit is limited, not a gross-income exclusion (LIG art. 1). Corporate year attribution follows the commercial fiscal period and accrual rules in art. 24. Do not use the individual's calendar-year deduction tables.

Out of scope: gaming's separate art. 73 rate, promotion/RIGI/knowledge-economy regimes, reorganisations and complex trust/fund classification. Foreign source, PE and withholding categories are in [argentina-cross-border](argentina-cross-border.md); TP in [argentina-transfer-pricing](argentina-transfer-pricing.md). Provincial turnover tax is a separate liability, not a credit assumed here.

## Rates, bands and thresholds

### Fiscal years beginning in 2026

| Net taxable income, ARS | Fixed tax, ARS | Marginal rate | Excess over, ARS | Official source |
|---|---|---|---|---|
| 0 to 133,514,185.74 | 0.00 | 25% | 0.00 | ARCA 2026 art. 73 scale; https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/determinacion/documentos/Ganancias-Escala-PJ-2026.pdf |
| Over 133,514,185.74 to 1,335,141,857.38 | 33,378,546.43 | 30% | 133,514,185.74 | same |
| Over 1,335,141,857.38 | 393,866,847.93 | 35% | 1,335,141,857.38 | same |

Apply fixed tax + marginal rate × excess. LIG art. 73 adjusts bands annually by October-on-October IPC for fiscal years beginning after each update. Do not use the unindexed original ARS 5m/50m statute table or the old Guide's 2025 brackets for a year opening in 2026.

| Other rule | Amount or period | Conditions and official source |
|---|---|---|
| Branch profit remittance | Additional 7% | LIG art. 73(b), on remitting PE profits to head office; underlying corporate tax still applies; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Dividends to individuals/foreign beneficiaries | See cross-border Guide's art. 97 computation | Identify recipient and profit period before distributing; corporate resident receipts have separate art. 68 treatment; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Ordinary loss carryforward | Five following years | LIG art. 25, subject to source/type restrictions; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| New loss indexation | Losses from fiscal years beginning from 1 January 2025 | Current art. 25, amended by Ley 27.802 art. 190: IPC between loss-year close and computation-year close; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Tax inflation adjustment trigger | IPC increase above 100% over 36 months before closing | LIG art. 106, transitional first-year rules are separate historic rules; https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 |
| Corporate advances | Nine payments, each 11.11% of adjusted prior-year base | ARCA current anticipos instructions; https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/anticipos.asp |
| Minimum advance amount | ARS 2,500, inclusive | An advance equal to or above this is payable; https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/anticipos.asp |

## The base

Use [LIG arts. 23-25, 53, 55-78, 83-93 and 105-109](https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05). The working paper must distinguish book profit, tax adjustments, source-specific results, restricted losses, taxable net income, determined tax and payment credits.

1. Start with the applicable commercial accounts and reconcile to the statutory tax measurement. Taxable business income generally accrues; accounting recognition and inflation restatement are not by themselves the tax result. Separate exempt/non-taxable income and identify direct/shared costs attributable to it.
2. Reconcile sales, inventory and cost of sales under the statutory valuation rules, fixed-asset tax depreciation and disposals, foreign exchange, receivables and provisions. Accounting impairments/reserves are not automatically deductions. Retain asset cost/date and depreciation schedules, inventory and bad-debt evidence.
3. Deduct expenses necessary to earn, maintain or preserve taxable income under art. 83, with documents and any specific limitations. Test art. 92 disallowances separately: distributions, personal costs, non-deductible taxes/penalties, limited royalties and other restricted expenditure do not become deductible by booking them as business expenses.
4. Prepare the tax inflation adjustment where art. 106's trigger applies. This is a distinct statutory balance-sheet computation with prescribed asset/liability exclusions and movements. Do not apply the annual CPI percentage to accounting profit or equate accounting inflation adjustment with tax adjustment. Historic instalment components and special investments require a separate year-by-year schedule.
5. Apply current-year and brought-forward losses by source/type. Under art. 25, securities/digital-asset and non-hedging derivative losses are specific losses; they cannot freely shelter ordinary trading profit. Foreign-source losses remain against foreign-source income under art. 131. Ordinary unabsorbed loss expires after the statutory five-year window. For fiscal years beginning from 2025, update qualifying losses by IPC between year-end months under the current art. 25; do not extend that rule automatically to older losses.
6. Floor the taxable base at zero and apply the fiscal-opening-year scale. Then deduct eligible foreign tax credit and other admitted payment credits, suffered withholdings/perceptions and paid advances, reconciling each certificate and account. A final withholding cannot automatically be used again as a general credit.

**Related-party financial interest:** art. 85(a) limits qualifying financial-debt interest to the greater of the executive-set annual amount and 30% of the specified income measure before those interest charges and depreciation, with statutory exceptions and unused-cap/excess-interest schedules. Trade debts are excluded from that financial-debt definition. Do not apply the ceiling to every interest expense without classification. The executive peso amount and full exception/carryforward computation are not confirmed here; stop that line and obtain the current rule. TP is an additional condition, not a substitute for this limit.

**Exception and transition table**

| Fact | Treatment and source |
|---|---|
| Year begins in 2025 but closes in 2026 | Use the opening-year scale, not this 2026 table, under LIG art. 73 |
| Loss year opened in 2024 | Current art. 25's new 2025-onward indexation does not automatically cover it; keep old loss unconfirmed pending its applicable rules |
| Recipient of dividend is another Argentine capital company | Test LIG art. 68; do not assume the individual/foreign dividend treatment |
| Distribution relates to pre-2018 accumulated profits | Reconcile art. 74 equalisation-tax and transitional provisions before payment; no automatic current-dividend shortcut |
| Gaming, promotion, reorganisation or hybrid entity | Refer the special regime; this ordinary computation does not establish its rate or exemption |

## Deadlines and filing

[RG 4626 art. 6](https://biblioteca.arca.gob.ar/dcp/REAG01004626_2019_11_05) ordinarily places return and balance payment in the fifth month after commercial closing, subject to the official CUIT calendar. Financial statements and the required accompanying documents are due by the last day of the sixth month. Do not repeat the old Guide's unsourced general June extension: an extension needs its own applicable resolution.

### 2026 transition for F.713

[RG 5908 arts. 1-4](https://biblioteca.arca.gob.ar/dcp/REAG01005908_2026_10_01) introduces **GANANCIAS PERSONAS JURÍDICAS**, Clave Fiscal level 2 or above, for commercial closings from June 2026 inclusive. From 19 October 2026 to 28 February 2027, choose the web service or the existing application; from 1 March 2027 the web service is mandatory. Earlier closings, original or amended, remain in the application. An amendment follows the medium used for its original return.

ARCA's [presentation page](https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/presentacion.asp) identifies the return as **F.713**. Reconcile its determination to the working paper: domestic/foreign-source result, admissible losses, determined tax and payment credits/saldo. Exact current web field/box numbering has not been confirmed; do not invent it from older SIAP screenshots. Validate and submit, retain the return and acknowledgement, and separately reconcile payment in Sistema Cuentas Tributarias.

Under RG 4626 art. 4, submit **Memoria, Estados Contables e Informe del Auditor**, professionally certified and signature authenticated, through **Presentación Única de Balances (PUB)**, Clave Fiscal level 2 or above. NIIF reporters have the prescribed local-accounting reconciliation/documents; qualifying MiPyME reporters may use the specified note alternative and retain its working papers. Use individual accounts where consolidated accounts exist. Save PUB's acknowledgement; F.713 does not replace PUB.

### Advances and reduction

The [ARCA anticipos page](https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/anticipos.asp) requires nine advances, starting the month after the ordinary annual return/balance deadline. Prior-year determined tax is reduced by the specified promotion relief, non-final withholding/perception credits, substitute-withholding payments, qualifying diesel fuel-tax credits and analogous foreign-tax credit. Current-period amounts are not subtracted from the prior-year base. Apply 11.11% to that adjusted base for each advance, reconcile ARCA's **Sistema Cuentas Tributarias** figures and pay when the minimum is met. VEP advance codes: tax **010**, concept **191**, subconcept **191**. The published [2026 advance calendar](https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/documentos/Anticipos-Vencimientos-PJ.pdf) is period/CUIT-specific; calendar-year 2026 profit can create 2027 payment dates, so obtain that year's schedule when published.

Do not reduce advances informally. Ordinary reduction is from the fifth advance; from the third if total exceeds estimated tax by more than 25%, or first if more than 40%. Requirements include active unrestricted CUIT, electronic fiscal domicile, no same-tax/year reduction request in the prior 90 days, and no missing relevant income-tax returns from January of the previous year. Request in **Sistema Cuentas Tributarias**, **Reducción de Anticipos**, with tax/year/projected base; retain **F.2254** and check the fiscal-domicile decision. Pay the resulting estimate on time. Underpayment carries interest under the stated comparison of real tax and original advances.

The special procedure applies if the determined advance-base parameter exceeds ARS 250m for segment 11 or ARS 200m for others **and** the estimated base is more than 10% lower. Use **Presentaciones Digitales**, **Solicitud de Reducción de Anticipos Impuesto a las Ganancias - Trámite Especial**, with supporting projection, at least 60 calendar days before the last advance. ARCA's decision period is 60 calendar days. Do not mistake the request acknowledgement for approval. Source: same current ARCA advance page; its 2027 IPC update applies from March, not a retroactive 2026 threshold change.

## Penalties and interest

Annual return, balance payment, advances and PUB are separate obligations. A filing acknowledgement does not prove payment, and a reduction request does not excuse an unapproved shortfall. Current 2026 penalty amounts and interest rates have not been confirmed here; compute neither from historic nominal figures. The advance-reduction source above expressly warns of interest where reduced amounts fall short, rejection and appeal procedures. Refer a disputed loss indexation, historic inflation component, deduction cap or late-payment assessment before finalising the liability.

## Cross-border points

Residents include foreign income with the limited foreign-tax credit. PE profits use the ordinary scale and the separate remittance charge; dividends and pre-2018 equalisation require recipient/profit-period analysis. The prior Guide's interest/royalty/treaty topics are retained through [argentina-cross-border](argentina-cross-border.md), which owns the category-specific gross withholding and treaty documentation. There is no general software-royalty rate inferred from an invoice label, and no unverified count of treaties. TP, service benefit evidence and financial-interest deduction limits must be checked independently.

## Two worked examples that recompute

### 1. Ordinary 2026 company in the second band

Assume an ordinary resident company's reconciled net taxable income is ARS 200,000,000 for a year opening in 2026, with no special regime, loss or foreign credit. Tax is 33,378,546.43 + (200,000,000 - 133,514,185.74) × 30% = 53,324,290.71. With paid advances of 40,000,000 and valid non-final withholding credits of 5,000,000, balance is 8,324,290.71. The inputs are assumed; scale is ARCA's original 2026 PDF.

```oa-check
name: Corporate second-band tax and balance
inputs:
  taxable_income: 200000000
  first_limit: 133514185.74
  fixed_tax: 33378546.43
  paid_advances: 40000000
  withholding_credit: 5000000
steps:
  - determined_tax: round(fixed_tax + (taxable_income - first_limit) * 0.30, 2)
  - balance: determined_tax - paid_advances - withholding_credit
expected:
  determined_tax: 53324290.71
  balance: 8324290.71
```

### 2. Ordinary loss or restricted securities loss?

Assume ARS 120,000,000 ordinary trading income and a documented ARS 20,000,000 loss, with no indexation difference, previous credits or special regime. If the loss is an eligible ordinary trading loss within its window, taxable income is 100,000,000 and tax 25,000,000. If it is instead a restricted securities loss with no same-source/type gain, it cannot shelter the ordinary income: taxable income remains 120,000,000 and tax 30,000,000. Classification changes current tax by 5,000,000. Both bases remain within the first 2026 band; source LIG art. 25. Do not elect a convenient loss classification.

```oa-check
name: Loss classification decision
inputs:
  ordinary_income: 120000000
  loss: 20000000
steps:
  - ordinary_loss_base: max(0, ordinary_income - loss)
  - ordinary_loss_tax: ordinary_loss_base * 0.25
  - restricted_loss_base: ordinary_income
  - restricted_loss_tax: restricted_loss_base * 0.25
  - tax_difference: restricted_loss_tax - ordinary_loss_tax
expected:
  ordinary_loss_base: 100000000
  ordinary_loss_tax: 25000000
  restricted_loss_base: 120000000
  restricted_loss_tax: 30000000
  tax_difference: 5000000
```

## Ask the client first

1. Legal form, tax classification/elections, fiscal-year opening/closing dates, CUIT and special-regime certificates.
2. Individual accounts, tax bridge, inventories, asset/depreciation and inflation-adjustment schedules, supporting invoices.
3. Loss origin/type/source/year, utilisation and IPC schedules; prior returns and disputed positions.
4. Foreign income/taxes, related-party dealings, financing terms and restrictions.
5. Withholding/perception certificates, actual advances paid and tax-account reconciliations.
6. Distribution/profit-year history, original filing medium, F.713/PUB acknowledgements and any advance-reduction decision.

## Sources

| Source and portions read | Official URL | Read on |
|---|---|---|
| Read for corporate scope, accrual, losses/rates and deductions: LIG arts. 1, 23-25, 53, 68, 73-74, 83, 85, 92-93, 105-109; quotations: "se inicien a partir del 1° de enero de 2025", "TREINTA Y SEIS (36) meses" | https://biblioteca.arca.gob.ar/dcp/LEY_C_020628_2019_12_05 | 2026-11-11 |
| Read for every indexed band/rate/fixed amount: ARCA corporate scale 2026, whole one-page table; quotation: "133.514.185,74" | https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/determinacion/documentos/Ganancias-Escala-PJ-2026.pdf | 2026-11-11 |
| Read for F.713/PUB and deadlines: RG 4626 current arts. 1-7; quotation: "quinto mes siguiente al de cierre" | https://biblioteca.arca.gob.ar/dcp/REAG01004626_2019_11_05 | 2026-11-11 |
| Read for new filing service and stages: RG 5908 arts. 1-4; quotation: "desde el 19 de octubre de 2026 hasta el 28 de febrero de 2027" | https://biblioteca.arca.gob.ar/dcp/REAG01005908_2026_10_01 | 2026-11-11 |
| Read for current form and amendment route: ARCA Presentación page; quotation: "El formulario de declaración jurada es el F. 713" | https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/presentacion.asp | 2026-11-11 |
| Read for advance base/payment/reduction conditions and codes: ARCA Anticipos page, general and special procedures; quotations: "9 anticipos", "11,11%", "F.2254" | https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/anticipos.asp | 2026-11-11 |
| Read for advance-calendar identification: ARCA 2026 PDF, title and CUIT/month tables; quotation: "Vencimientos 2026" | https://www.arca.gob.ar/gananciasYBienes/ganancias/personas-juridicas/declaracion-jurada/documentos/Anticipos-Vencimientos-PJ.pdf | 2026-11-11 |

Not yet confirmed: precise 2027 CUIT return/payment dates and live F.713 web box numbering; current penalty amounts and interest; executive financial-interest peso ceiling and full exception/carryforward computation; detailed historic inflation instalments and special investments; pre-2018 equalisation/transitional profit computation. Old approximate royalty rates, treaty count and general June extension are replaced by verified specialist routing or this explicit unresolved list, not repeated as facts.
