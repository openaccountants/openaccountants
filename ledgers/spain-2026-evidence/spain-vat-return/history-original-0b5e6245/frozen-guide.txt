---
name: spain-vat-return
description: Reconciles a Spanish ordinary VAT return for 2026 to invoices, bank settlements, customs assessments, registers and accepted prior returns for sole traders and companies in the peninsula and Balearic Islands. Uses es-vat-return for the underlying computation and checks business-use restrictions, general versus special prorrata, investment-good adjustment signs, reverse-charge mapping and credit roll-forward against current Modelo 303 instructions. Separates withheld income tax and platform fees from VAT bases and distinguishes dated energy and housing changes from ordinary rates. Use for revisar IVA, revisar Modelo 303, conciliación IVA, return review, prior credit and investment adjustment. Preserves this existing entry point while recording territorial, special-regime and unresolved computation limits.
version: 2.5
category: international
jurisdiction: ES
tax_year: 2026
last_updated: 2026-10-28
review_status: pending_review
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain: VAT return reconciliation, 2026

**Sourced from the law.** This draft has not had an independent whole-pack review or accountant sign-off. It preserves this existing entry point and reconciles the calculation in [es-vat-return](es-vat-return.md) to invoices, registers and the actual 2026 Modelo 303. Use that Guide's complete ordinary computation, including both prorrata methods; this review route does not supply a competing historical box map.

## Who this applies to

Ordinary IVA taxpayers in the peninsula/Balearic Islands, including businesses with both deduction-entitling and exempt turnover. Establish the taxpayer, period, establishment, regime and competent administration. The Canary Islands, Ceuta and Melilla use separate indirect taxes; foral allocation and special-regime computations remain outside the completed ordinary route ([LIVA art. 3](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a3)).

Read actual invoices, customs documents, registers/SII, prior filed returns, credit/refund decisions and relevant elections. Merchant names, foreign IBANs, round sums or personal-looking counterparties are leads for reconciliation, not legal classifications. A bank-only draft cannot substantiate recoverable input VAT or resolve supply place, exemption, tax point or reverse charge ([LIVA arts. 69–70/84/97](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a97)).

## Rates, bands and thresholds

| Check | Required rule | Period | Official source |
|---|---|---|---|
| Ordinary rates | **21% / 10% / 4%** under the exact categories; **0%** only where the specific statutory conditions hold | 2026 | [LIVA arts. 90–91](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a91) |
| Dated energy supplies | Apply the spring temporary rates and later conditional product/CPI rules in the computation Guide; do not assume all-year 21% or all-year 10% | 2026 | [RDL 7/2026 art. 42](https://www.boe.es/buscar/act.php?id=BOE-A-2026-6544#a4-4); [RDL 18/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-14112); [RDL 25/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20265) |
| Housing period split | New furnished-short-letting, renovation and permanently protected-home wording applies from **1 December 2026**, not January | 2026 cutover | [RDL 29/2026 art. 7](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823#a7) |
| Prorrata percentage | Round annual eligible-turnover fraction **up to whole percent** | 2026 | [LIVA art. 104](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a104) |
| Mandatory special method | General recovery exceeds special recovery by **10% or more**; this is not a ten-percentage-point test | 2026 | [Art. 103](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a103) |
| Passenger vehicle | **50%** business-use presumption after establishing business allocation, or the statutory supported/100% category | 2026 | [Art. 95](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a95) |
| Investment-good adjustment | Percentage change **strictly over ten points**, divisor **5**, land/buildings **10** | Statutory adjustment window | [Arts. 107–109](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a109) |
| Deduction and return-credit clocks | Separate **four-year** clocks from entitlement arising and original credit-return filing, respectively | 2026 | [Art. 99](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a99) |

**Energy CPI closure.** The canonical VAT Guide now gives the official INE indices and annual comparisons: electricity 6.0%/8.4%/11.4%, gas 0.8%/4.1%/4.3% for June/July/September 2026. The more-than 15% trigger therefore fails for August/September/November; the corresponding conditional 10% VAT relief is not activated and 21% applies. The gas trigger also covers the listed biomass/firewood. December still awaits October indices. Follow the dated table and primary references in [es-vat-return](es-vat-return.md#energy-conditions-resolved-from-the-official-indices). Source read 2026-10-27.

## The base

### Reconcile the source ledger

Use one row per actual transaction/invoice with issuer/recipient NIF, legal counterparty and establishment, description, supply/movement evidence, invoice/receipt/devengo dates, base, actual rate/quota, business-use fraction, blocked amount, sector/use allocation, prorrata method/percentage, deductible quota, return box and source reference. Keep amendments, prior-period claims, returned payments and unpaid invoices separately. Reconcile opening bank balances plus all movements to closing balances without treating each movement as a sale or purchase.

Reconstruct the invoice settlement as **base + VAT − documented withholding − other settled credits = money received**. If the platform deducts fees, record the gross underlying sales and actual separately invoiced platform service. Do not infer a universal VAT or withholding rate from the amount received. Loans, own-account transfers, owner capital/draws, payroll and statutory payments receive their actual treatment, not an invented VAT extraction ([LIVA arts. 4/7/75/78](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a78)).

Check invoice support before deduction: issuer/recipient details, separate VAT quota and statutory content, including extra details on a simplified invoice. Missing/incorrect documents require correction or an unresolved item, not a fabricated invoice. The investment-good definition is a VAT test separate from book capitalisation. Foreign VAT is not Spanish deductible quota ([LIVA arts. 97–100/108](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a97); [RD 1619/2012 arts. 6–7](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696#a7)).


For the ordinary sector/startup methods, use [es-vat-return: The base](es-vat-return.md#the-base). Reconcile the CNAE/50-point/15% sector tests, exclusive versus cross-sector shared input, the before-1-July startup counting rule and aggregate four-year correction separately from ordinary annual prorrata. An interrupted full year uses the last three operating calendar years' global percentage. For mixed-use investment input, business use is applied before prorrata:2,100×50%×60%=630; fixed50% use with provisional50% and definitive60% prorrata produces105 additional annual deduction. These supplied methods replace a bare handoff. A fact-specific common-regime authorisation still requires its own evidence; the investment-good method below supplies the finite both-gates simultaneous-change branch and preserves the exact one-gate reservation.

### Check retained special-regime gateways

Use [the computation Guide's retained gateways](es-vat-return.md#retained-special-regime-and-small-transaction-gateways) for the retailer surcharge **5.2/1.4/0.5/1.75%**, agriculture/forestry compensation **12%** versus livestock/fishing **10.5%**, advertising objects' same-recipient annual **200** boundary, the distinct acquisition and distance/TBE **10,000** tests, and cash-scheme **2m/100,000** entry/exclusion tests. Those are conditional rules, not general ordinary-return allowances. The computation Guide now supplies the **published 2026 AEAT 250,000/125,000/250,000 entry route**, its post-repeal explanation, equality controls and dated renunciation routes. Preserve the 150,000/75,000/150,000 ordinary statutory baseline and repeal history; the linked IRPF B2B subset is not a stand-alone IVA turnover limb. Check all the activity, entity, aggregation and election conditions before assigning a regime ([LIVA arts. 7/14/73/122/130/161/163 decies](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740)).

For cash-scheme information, reconcile **62/63** sales base/quota and **74/75** affected purchase base/quota on ordinary art. 75 timing, separately from the actual collection/payment-driven output/deduction. The purchase information also affects a non-elected recipient of a cash-scheme invoice. A descriptive row does not accelerate recovery or add its quota twice ([AEAT 2026 instructions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html)).

### Recompute recovery before mapping boxes

Apply business/private allocation and art. 96 restrictions first. The passenger-car presumption is not an automatic deduction on an unrelated personal vehicle. A property partly used by the business can support proportionate utility recovery under the binding TEAC criterion; it does not establish the same proportion for every private mobile service ([LIVA arts. 95–96](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a95); [TEAC 19 July 2023 RG 00/06654/2022](https://serviciostelematicosext.hacienda.gob.es/TEAC/DYCTEA/criterio.aspx?id=00%2F06654%2F2022%2F00%2F0%2F1)).

Rebuild the annual art. 104 included-turnover fraction and retain each exclusion. Exempt turnover is not subject to a generic de-minimis refusal. Under general prorrata, apply the rounded percentage to the eligible business pool; under special, allocate exclusively entitling/exempt/shared costs separately. Recompute both methods for the mandatory comparison. The final correction is **definitive annual recovery − all provisional recovery**, including whatever provisional amount has already been entered for the last period. Do not multiply private-use deductions twice, allow exempt-only costs in special recovery, or use the special method voluntarily without its required election/holding rules ([LIVA arts. 101–106](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a106); [RIVA art. 28](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925#a28)).

For investment goods, retain acquisition and first-use dates, original and applicable reference U/P/deduction, the actual correction route and remaining years. The [canonical investment-good method](es-vat-return.md#investment-goods-and-credit-ledger) now separates the 420 annual delayed-use prorrata example from a whole pre-use changed-destination correction under 99/114 and the separate 111–113 startup reconciliation. It also supplies a finite simultaneous-change computation when both independent U/P gates are crossed. The canonical Guide also supplies the labelled literal DGT later-reference ledger: the420annual addition takes8,400to8,820; first-useP60%and actual post-adjustment deduction8,820give693at later75%, without a4,200reset. The contrary acquisition-reference schedule and exact authority reconciliation remain explicit. The source reconciliation, cases where only one of two changing variables crosses its gate, and a decisive irrecoverable-VAT acquisition-value component remain specifically unresolved. A repayment reduces recovery in box 43; an additional investment deduction has the opposite sign. Ordinary current-year definitive-prorrata correction belongs in 44 and is not duplicated in 43. ([LIVA 95/107–114](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a107); [DGT V0835-25](https://petete.tributos.hacienda.gob.es/consultas/?num_consulta=V0835-25); [V0386-24](https://petete.tributos.hacienda.gob.es/consultas/?num_consulta=V0386-24).)

### Reconcile the 2026 form and credit roll-forward

Use the relevant January/1T or later-period AEAT instructions. Domestic output 4/10/21% uses **01–03/04–06/07–09**. Intra-EU goods/services received use output **10/11** and ordinary input **36/37**; other reverse charge output **12/13**, with the domestic input-row interpretation disclosed in the computation Guide. Imports use **32/33**, and the corresponding investment-input pairs are **30/31 domestic, 34/35 import, 38/39 intra-EU**. Thus an EU service does not use the old sibling's 17/18 mapping, nor does non-EU service output use 19/20 ([AEAT 2026 instructions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html)).

Tie output to **27**, input/adjustments to **45**, and net to **46 = 27 − 45**. In a simple state-only original return with no special adjustments, 64/66 follow the ordinary result, **69 = 66 − 78**, and **71 = 69**. Verify prior credit **110**, actual applied credit **78**, and remaining **87 = 110 − 78**. Newly generated negative current-period VAT is not put into 87: it is a separate current-period amount added to the next ledger. No already requested refund remains available for compensation. Carry the original filing date for each unused balance, not a restarted four-year clock at every return ([LIVA art. 99](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a99); [AEAT later-period credit instructions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026/instrucciones-02-12-2t-4t-2026.html)).

Use a formula-driven working paper with transaction totals, box summary, adjustments and separate prior/current credit schedules. Reconcile invoices to VAT registers/SII, then returns to payment/refund confirmations. Keep the tax computation and payment status distinct: a draft, saved form or bank transfer by itself is not the accepted filing receipt. Detailed fuel, foral, correction and special-regime result fields require their own rule rather than a balancing entry.

## Deadlines and filing

Ordinary 303 quarters file in the first **20 calendar days of April/July/October**; the final quarter in the first **30 days of January**. Monthly filers generally have the first **30 days** of the next month, with January's period due by the last day of February. Confirm holidays and direct-debit windows for the actual period. Monthly status depends on the statutory categories, including prior-year turnover **over 6,010,121.04** and REDEME; monthly filing alone does not establish monthly-refund entitlement ([RIVA art. 71](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925#a71)).

Check 390 filing or the exact exoneration/last-303 annual data requirements; its ordinary annual deadline is the first **30 January days**. Reconcile 349 using the supplied-goods/services **50,000** quarterly test and the preceding four quarters, rather than applying a threshold to all purchases indiscriminately. SII has its separate four/eight-day and before-16th deadlines ([390 order art. 8](https://www.boe.es/buscar/act.php?id=BOE-A-2009-18472#a8); [RIVA arts. 69 bis/81](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925#a81); [AEAT 2026 exemptions](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html)).

For non-EU general-rule B2B services, recoverable-VAT investment-value assembly and ordinary corrective returns, use [the canonical303 mapping and correction route](es-vat-return.md#current-ordinary-303-mapping). It supplies the12/13-to28/29 input/output distinction and the separate rectificativa/request exceptions. The unprorated input base and deductible quota remain separate, so mixed-business reverse charge does not become automatically neutral.

## Penalties and interest

Classify voluntary late filing, underpayment, late collection and record/invoice infringements separately. LGT art. 27 provides **1% plus 1% per complete late month** through twelve months, then **15% plus the prescribed interest**; offence and collection amounts depend on their own conditions. A rectificative label does not remove a surcharge or establish a harmless error. Use the full sourced penalty table in [the computation Guide](es-vat-return.md#penalties-and-interest), with the conduct, notice, date, unpaid amount and payment evidence recorded ([LGT arts. 26–28/188/191/198](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186#a27)).

## Cross-border points

Confirm the actual supplier/customer establishment, business status and goods movement. General B2B services, property/other exceptions, intra-EU acquisition, export and import are different legal routes. Reverse-charge output is reported in full; the input side remains restricted by business use, blocking and prorrata. Check a supplier's incorrect foreign VAT separately from the Spanish recipient tax obligation. Reconcile relevant 349, customs and VAT-register entries without assuming that every foreign payment is a reverse charge or every foreign receipt an export ([LIVA arts. 13/21/25/69–70/84/94](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a84)).

## Two worked examples that recompute

### Invoice settlement and prior credit are separate from the VAT base

The source invoice states **1,000 base + 210 VAT − 150 withholding = 1,060 received**. These are assumed documented facts, not a rule assigning every payment that withholding rate. Eligible input VAT is **80**. The VAT base stays 1,000 and current net VAT is **130**. Of **200** prior credit, apply 130 and carry **70** in box 87; the original return result is zero. Do not extract VAT from the 1,060 bank receipt or deduct the withholding from output VAT.

```oa-check
name: Spain 2026 invoice withholding settlement and prior VAT credit
inputs:
  invoice_base: 1000
  invoice_vat: 210
  documented_withholding: 150
  eligible_input: 80
  prior_credit: 200
steps:
  bank_receipt: invoice_base + invoice_vat - documented_withholding
  current_net: invoice_vat - eligible_input
  prior_used: min(prior_credit, max(current_net, 0))
  prior_remaining: prior_credit - prior_used
  return_result: current_net - prior_used
expected:
  bank_receipt: 1060
  current_net: 130
  prior_used: 130
  prior_remaining: 70
  return_result: 0
```

### Investment adjustment sign and ordinary result

Assume acquisition and first use occurred in the same initial year,with no later reference reset. A machine within its adjustment window originally bore **1,260 VAT**, with an **80%** deduction. Current definitive deduction is **60%**, a **20-point** change, so adjustment is required. Original recovery **1,008** minus current-percentage recovery **756**, divided by five, is **50.40 repayable**. Enter **−50.40** in box 43. Assuming **500** other fully reconciled final-period input after its own current-year percentage correction and **1,000** output, total input including box 43 is **449.60**, and the original state-only result without prior credit is **550.40 payable**. No second copy of this same adjustment goes into box 44.

```oa-check
name: Spain 2026 investment-good adjustment reduces input recovery
inputs:
  original_vat: 1260
  original_percentage: 80
  current_percentage: 60
  divisor: 5
  other_final_input: 500
  output: 1000
steps:
  points_change: abs(original_percentage - current_percentage)
  original_deduction: original_vat * original_percentage / 100
  current_equivalent: original_vat * current_percentage / 100
  repayment: (original_deduction - current_equivalent) / divisor
  box43: 0 - repayment
  total_input: other_final_input + box43
  payable: output - total_input
expected:
  points_change: 20
  original_deduction: 1008
  current_equivalent: 756
  repayment: 50.40
  box43: -50.40
  total_input: 449.60
  payable: 550.40
```

## Ask the client first

1. Which legal taxpayer, VAT territory, filing period, regimes/elections and previous accepted returns apply?
2. Which invoices, customs assessments, credit notes and payment/withholding records explain every material register-to-bank difference?
3. What proves business/private and taxable/exempt use, sector allocation, annual turnover and any special-prorrata election?
4. What original investment-good deductions, first-use years and changes/disposals require adjustment?
5. What prior credit/refund ledger and filing receipts establish the opening balance, actual use and unexpired closing balances?
6. Which energy/housing tax points or cross-border facts need the dated or territorial rule before approval?

## Sources

| Official source | Scope read | Read on |
|---|---|---|
|[INE national subclass indices, table 76128](https://www.ine.es/jaxiT3/Tabla.htm?t=76128&L=0),[official CSV](https://www.ine.es/jaxiT3/files/t/es/csv_bdsc/76128.csv)|2026 June/July/September and same 2025 indices; annual variations; six independent product/month comparisons and VAT activation results|2026-10-27|
| [LIVA, Ley 37/1992](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740) | Tax point/base, invoice-supported deduction, use/blocking, prorrata and investment adjustments, credit and refund clocks | 2026-10-26 |
| [RIVA, RD 1624/1992](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28925), [invoice regulation](https://www.boe.es/buscar/act.php?id=BOE-A-2012-14696), [390 order](https://www.boe.es/buscar/act.php?id=BOE-A-2009-18472) | Elections, records, invoice details, return/SII/349 and annual-summary periods | 2026-10-26 |
| [AEAT January/1T 2026](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026.html), [later periods](https://sede.agenciatributaria.gob.es/Sede/todas-gestiones/impuestos-tasas/iva/modelo-303-iva-autoliquidacion_/instrucciones-2026/instrucciones-02-12-2t-4t-2026.html), [approved 303](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-1761) | Current ordinary output/input/credit mapping and signed adjustments, replacing stale sibling box references | 2026-10-26 |
| [TEAC RG 00/06654/2022](https://serviciostelematicosext.hacienda.gob.es/TEAC/DYCTEA/criterio.aspx?id=00%2F06654%2F2022%2F00%2F0%2F1) | Business/private property utility recovery, not a general mobile-phone percentage | 2026-10-26 |
| [RDL 7/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-6544), [RDL 18/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-14112), [RDL 25/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20265), [RDL 29/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-20823) | Dated/conditional energy rules and December housing provisions, with unresolved timing/index points inherited from the computation Guide | 2026-10-26 |
| [LGT, Ley 58/2003](https://www.boe.es/buscar/act.php?id=BOE-A-2003-23186) | Conduct-based surcharge, penalty and collection classification | 2026-10-26 |
|[DGT V0386-24 section6](https://petete.tributos.hacienda.gob.es/consultas/?num_consulta=V0386-24),[canonicalcalculation](es-vat-return.md#investment-goods-and-credit-ledger) |Delayed-first-use reference qualification;original worked example expressly assumes same-year acquisition/use |2026-10-27 |
| [DGT V0835-25, section 4](https://petete.tributos.hacienda.gob.es/consultas/?num_consulta=V0835-25), [LIVA arts. 95/99/104/107–114](https://www.boe.es/buscar/act.php?id=BOE-A-1992-28740#a95) | Actual binding pre-use changed-destination correction, distinct annual delayed-use and pre-activity routes; canonical finite method and later-reference conflict | 2026-10-27 |
| [AEAT live Calculadora de prorrata](https://www2.agenciatributaria.gob.es/wlpl/AVAC-CALC/CalculadoraProrrata), [canonical calculation](es-vat-return.md#investment-goods-and-credit-ledger) | Actual annual first-use 420 and both-gates joint-change control; one-gate and later-reference source limitations retained | 2026-10-27 |
| [AEAT1April2026 post-repeal effects note](https://sede.agenciatributaria.gob.es/Sede/todas-noticias/2026/abril/1/nota-sobre-efectos-ambito-tributario-febrero.html), [IVA eligibility](https://sede.agenciatributaria.gob.es/Sede/iva/regimenes-tributacion-iva/regimen-simplificado/quien-se-aplica-regimen-simplificado.html), [IRPF eligibility](https://sede.agenciatributaria.gob.es/Sede/empresarios-individuales-profesionales/contribuyentes-modulos/quien-se-aplica/irpf.html) | Published2026 higher limits and preserved submission routes, distinguished from the ordinary consolidated statutory text and the remaining legal-reconciliation boundary | 2026-10-27 |
| [RDL16/2025](https://www.boe.es/buscar/act.php?id=BOE-A-2025-26458), [27January repeal](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-2024), [RDL2/2026](https://www.boe.es/buscar/act.php?id=BOE-A-2026-2547), [26February repeal](https://www.boe.es/diario_boe/txt.php?id=BOE-A-2026-4667) | Actual extending provisions and non-convalidation history; neither decree presented as currently in force | 2026-10-27 |


**Published route supplied:** The ordinary AEAT exactly-10-kW route and its literal-source reconciliation are supplied in the linked computation Guide. Its source-derived initial acquisition-value, either-separate-gate annual U/P and literal DGT delayed-first-use ledger methods are also supplied, with independent recovery rights, the combined-text interpretation and the actual calculator discrepancy kept explicit. **Not yet confirmed:** December's unpublished October-index condition, fact-specific common-regime-authorisation, the precise authority reconciliation between the supplied DGT post-adjustment reference interpretation and the acquisition-reference wording/calculator, and specialised fuel-result points recorded in [es-vat-return Sources](es-vat-return.md#sources); specific foral allocation exceptions beyond [the ordinary allocation method](es-vat-return.md#the-base); use [IGIC](es-canary-islands-igic.md) or [IPSI](es-ceuta-melilla-ipsi.md) for their territories. This review route does not close an unresolved computation by agreeing with a duplicate draft. Independent whole-pack review remains outstanding.

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
