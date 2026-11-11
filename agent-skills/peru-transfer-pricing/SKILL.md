---
name: peru-transfer-pricing
description: "Apply Peru's transfer-pricing rules to tax year 2026 transactions of resident businesses and their related parties, including domestic dealings, foreign counterparties and the separate low-tax or preferential-regime scope tests. Build an arm's-length pricing file, test intragroup service deductions, decide whether the local file, master file or country-by-country report is required, and prepare the SUNAT reporting workflow. Covers the 2026 UIT, exact reporting threshold boundaries, benefit evidence, low-value services, comparability, adjustments and ordinary Table I reporting penalties. Use for precios de transferencia Peru, Reporte Local, Reporte Maestro, Reporte Pais por Pais, Formulario 3560, related-party management charges and transfer-pricing records. Does not replace the corporate-tax computation or a transaction-specific valuation, treaty analysis or advance pricing agreement application."
license: "AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)"
metadata:
  source: openaccountants
  openaccountants_url: "https://www.openaccountants.com/skills/peru-transfer-pricing"
  jurisdiction: "PE"
  tax_year: "2026"
  last_updated: "2026-11-11"
---

# Peru transfer pricing, tax year 2026 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Built from the law. Not yet approved.** Prepare a pricing analysis, reporting decision and working papers. Do not submit a return or change a ledger without the responsible person's approval.

**Quick reference.** Pricing scope and reporting scope are different tests. A small transaction can require an arm's-length price even when no informative return is due. For the 2026 reporting year, use the 2026 UIT, not the UIT of the following filing year. The ordinary local-file test combines accrued income **above** its threshold with operations **at or above** the relevant threshold. Establish residence, ownership/control and transaction amounts before choosing a report. See the linked rates table below.

## Who this applies to

Peru income-tax taxpayers must test transactions with related parties and the separate non-cooperative, low/no-tax territory and preferential-regime categories. The full scope is in LIR art. 32(4), read with art. 32-A(a), and Regulation art. 108. Do not read the older wording reproduced under `TEXTO ANTERIOR` in a consolidation as current law. Unrelated-party status alone does not clear the low-tax or preferential-regime tests. Sources: [LIR arts. 32 and 32-A](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [Regulation art. 108](https://www.sunat.gob.pe/legislacion/renta/regla/cap19.pdf).

**Related parties.** Read every route in Regulation art. 24, rather than using a single shareholding test:

- Direct or indirect capital ownership **above 30%**, common ownership above that level, the specified spouse/family ownership cases, or common partners above that level.
- Common directors, managers or administrators with decision power; consolidated financial statements; dominant influence over management decisions.
- Business collaboration arrangements, association-in-participation contracts and the statutory decision-power or participation tests.
- A foreign enterprise and its Peru permanent establishments, and a Peru enterprise and its foreign permanent establishments.
- The domestic economic-dependence test: at least **80%** of sales/services/other operations with the specified domestic counterparty or linked counterparties, also representing at least **30%** of the other party's purchases. Test the immediately preceding tax year; for businesses operating for more than three tax years, use the average percentages for the three immediately preceding tax years. Test at year-end and apply the resulting relationship throughout the following tax year. The provision excludes the specified state-business transactions where state capital participation is above **50%**.

For dominant influence, art. 24(12) contains the absolute-voting-majority route and the special General Companies Law art. 126 meeting route, requiring the greatest number of voting shares in that vote and at least **10%** of subscribed voting shares. Do not label an exactly 30% shareholder related through the ownership test alone. Other routes can still apply. Record when the relationship starts and ends: art. 24(a)-(c) treats the ownership/control routes, dominant influence and the domestic turnover test differently. Source: [Regulation art. 24](https://www.sunat.gob.pe/legislacion/renta/regla/cap6.pdf).

**Who files.** The reporting resolutions define their taxpayers as Peru-domiciled persons within TP scope. RS 014-2018 art. 3 excludes individuals, undivided estates and electing marital communities without third-category business income, and the specified state enterprises, from the local-file declaration. That exemption is not an exemption from income-tax valuation rules. Master-file reporting also requires group membership. Sources: [RS 014-2018 arts. 1-3](https://www.sunat.gob.pe/legislacion/superin/2018/014-2018.pdf), [RS 163-2018 art. 2](https://www.sunat.gob.pe/legislacion/superin/2018/163-2018.pdf).

For reporting, a **group** is an ownership/control-linked collection required to prepare consolidated financial statements under the applicable generally accepted accounting principles, or that would be required to consolidate if its equity were traded on a centralised market. A related-party relationship alone does not establish this reporting definition. Constituents include entities excluded from consolidation solely for size or materiality, and the qualifying foreign-jurisdiction PEs for which separate statements are prepared for financial, regulatory, tax or internal-management purposes. Apply the distinct multinational-group definition for CbC. [Regulation art. 116(a)(1), (2) and (4)](https://www.sunat.gob.pe/legislacion/renta/regla/cap19.pdf).

## Rates, bands and thresholds

Amounts below are for **2026 transactions**, unless a row explicitly uses a prior-year group figure. PEN means Peruvian soles. The short original-language extracts identify the operative boundary; read the conditions in the same row.

| Item and conditions | Amount or rule | Official text and short extract |
|---|---|---|
| UIT used for 2026 local/master reporting | PEN 5,500; use the reporting year's UIT under Regulation art. 116(a)(7) | [SUNAT UIT table, DS 301-2025-EF](https://www.sunat.gob.pe/indicestasas/uit.html): `2026 ... 5,500`; [Regulation art. 116](https://www.sunat.gob.pe/legislacion/renta/regla/cap19.pdf) |
| Direct/indirect ownership route to related-party status | More than 30%; separate control/family/other tests remain | [Regulation art. 24(1)-(4)](https://www.sunat.gob.pe/legislacion/renta/regla/cap6.pdf): `más del treinta por ciento` |
| Local-file accrued-income gate | Above 2,300 UIT, or above PEN 12,650,000 | [RS 014-2018 art. 2](https://www.sunat.gob.pe/legislacion/superin/2018/014-2018.pdf): `hayan superado ... (2 300)` |
| Local-file limited information | Income gate met; covered operations at least 100 UIT and below 400 UIT: PEN 550,000 to below PEN 2,200,000 | [RS 014-2018 arts. 2.1 and 4.1](https://www.sunat.gob.pe/legislacion/superin/2018/014-2018.pdf): `igual o mayor a cien ... y menor a cuatrocientas` |
| Local-file fuller information and attachments | Income gate met; covered operations at least 400 UIT, or PEN 2,200,000 | [RS 014-2018 arts. 2.2 and 4.2](https://www.sunat.gob.pe/legislacion/superin/2018/014-2018.pdf): `igual o mayor a cuatrocientas (400)` |
| Goods sold with market value below tax cost | Income gate met; fuller local-file information irrespective of operation amount, even below 100 UIT | [RS 014-2018 art. 2.3](https://www.sunat.gob.pe/legislacion/superin/2018/014-2018.pdf): `incluso si este fuera menor a cien` |
| Small-transaction analysis exception within art. 2.2 reporting | Below 2.5 UIT, or below PEN 13,750, per individually tested transaction or tested group; art. 4.3 limits the analysis information, not the taxpayer's entire reporting duty | [RS 014-2018 art. 4.3](https://www.sunat.gob.pe/legislacion/superin/2018/014-2018.pdf): `transacciones inferiores a dos y media (2,5)` |
| Master file | Group member; own accrued income above 20,000 UIT, or PEN 110,000,000, and covered operations at least 400 UIT | [RS 163-2018 art. 2](https://www.sunat.gob.pe/legislacion/superin/2018/163-2018.pdf): `integrantes de un grupo ... hayan superado ... veinte mil` |
| CbC report group gate | Prior tax year's consolidated accrued income at least PEN 2,700,000,000; apply the filing-person and exchange exceptions below | [RS 163-2018 art. 10.1](https://www.sunat.gob.pe/legislacion/superin/2018/163-2018.pdf): `mayores o iguales a ... (S/ 2 700 000 000,00)` |
| Low-value-adding related-party services | Deduction comprises supported allocated costs/expenses plus a profit margin not exceeding 5% of those costs/expenses; benefit and other deduction tests still apply | [LIR art. 32-A(i)](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf): `no puede exceder el cinco por ciento` |
| TP report supporting records | Keep for five years or the limitation period, whichever is longer, with Spanish translation where required | [LIR art. 32-A(g)](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf): `cinco (5) años o durante el plazo de prescripción` |
| Ordinary Table I late or inaccurate TP informative declaration, before reductions | 0.6% of statutory IN; floor 10% of UIT and ceiling 25 UIT. This is the TP-report rule, not the beneficial-owner floor/ceiling | [Tax Code arts. 176(2), 176(4), Table I notes 10 and 14](https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf): `0.6% de los IN`; `10% de la UIT ... 25 UIT` |

Do not use these reporting thresholds as safe harbours for the price. Do not translate the CbC group gate into UIT: it is a statutory PEN amount.

## The base

### Build the transaction and method file

1. Reconcile the transaction population to accounts, contracts and counterparties. RS 014-2018 art. 1(4) defines operations as a sum without offsetting positive and negative signs: relevant taxable accrued income, deductible purchases/costs and other specified transactions. Gratuitous property transfers use tax cost. Check the excluded remuneration amount identified by Regulation art. 108. [RS 014-2018 art. 1](https://www.sunat.gob.pe/legislacion/superin/2018/014-2018.pdf).
2. Record functions, assets, risks, contract terms, market circumstances and business strategies. Use independent comparables; document reliable adjustments for material differences. Foreign comparables require adjustments for relevant market differences where local information is unavailable. [LIR art. 32-A(d)](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf).
3. Choose and justify the most appropriate method: comparable uncontrolled price, resale price, cost plus, profit split, residual profit split or transactional net margin. Do not select a margin merely because the group uses it elsewhere. [LIR art. 32-A(e)(1)-(6)](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [Regulation arts. 110-113](https://www.sunat.gob.pe/legislacion/renta/regla/cap19.pdf).
4. For methods (1)-(6), if multiple comparables produce a range, use Regulation arts. 114-115. Within the appropriate range, the agreed value is market value. Outside it, where it lowers Peru income tax for the period, the adjustment uses the median. The special highly comparable CUP route permits a full minimum/maximum range only when the coefficient of variation is no more than **3%**. Do not apply a software package's default percentile convention: art. 115 defines the positions and interpolation. [Regulation arts. 114-115](https://www.sunat.gob.pe/legislacion/renta/regla/cap19.pdf).
5. Other valuation methods under LIR art. 32-A(e)(7), amended by DL 1663, are available when the six methods cannot reliably apply and the statutory conditions hold. They require a technical report and the appropriate regulatory method. Unlisted-share discounted cash flow has specific exclusions, including a seller holding below **5%** or prior-year issuer net accrued income not above **1,700 UIT**. Do not apply the interquartile rule automatically to these other methods. The regulation was amended by DS 302-2025-EF, effective 18 December 2025; SUNAT's 2026 report limits its retrospective use for already-valued 2025 transactions. Sources: [LIR art. 32-A(e)(7)](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [Regulation arts. 113-115](https://www.sunat.gob.pe/legislacion/renta/regla/cap19.pdf), [Informe 000042-2026, conclusion](https://www.sunat.gob.pe/legislacion/oficios/2026/informe-oficios/i000042-2026-7T0000.pdf).

Commodity transactions require the statutory quotation and communication analysis rather than an ordinary management-fee benchmark. LIR art. 32-A(e) requires the communication by the start of shipment/unloading and provides a restricted export-correction window. Preserve the contract, quotation dates, incoterm, quantities, market and adjustments; obtain a transaction-specific analysis of the commodity rules before relying on a different method. [LIR art. 32-A(e)](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf).

### Service deductions

For related-party services, identify the actual recipient benefit: would an independent business pay for the service or perform it itself? Retain evidence of delivery, commercial need, provider costs and the reasonable allocation key. A parent's activity solely for its own benefit fails the recipient-benefit test. A contract or invoice alone is not delivery evidence. [LIR art. 32-A(i)](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [Regulation art. 118-A(a)-(d)](https://www.sunat.gob.pe/legislacion/renta/regla/cap19.pdf).

Low-value-adding services must be auxiliary/supportive, outside the group's core activity, not use/create unique valuable intangibles and not assume/control significant risk. The cap in the rates table is a deduction ceiling, not proof that the service qualifies or that its cost allocation is arm's length. Regulation art. 118-A(e) identifies activities that do not qualify unless they meet the statutory characteristics, including R&D, production, sales/distribution, financial transactions, extraction, insurance and senior management. Record the allocation justification and any change of allocation key. [LIR art. 32-A(i)](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [Regulation art. 118-A](https://www.sunat.gob.pe/legislacion/renta/regla/cap19.pdf).

### Adjustments

Test whether the agreed valuation reduces Peru tax, including deferred income or increased tax losses; SUNAT also has the connected-transaction power in art. 32-A(c). Determine the proper recognition period and each party's effect. A TP adjustment does not itself change the monthly income-tax advance base. Do not manufacture a dividend: Regulation art. 109(d) has a specific secondary-adjustment rule and exception. Route the resulting annual taxable-income adjustment to [pe-corporate-income-tax](pe-corporate-income-tax.md), whose tax-year status must be checked before applying a rate. [LIR art. 32-A(c)](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [Regulation art. 109](https://www.sunat.gob.pe/legislacion/renta/regla/cap19.pdf).

## Deadlines and filing

**Reporting period.** For 2026 transactions, the local file follows the **May 2027 monthly-tax schedule**, generally filing in the following month, not a made-up universal calendar day. The master file and CbC report follow the **September 2027 monthly-tax schedule**. Use the actual RUC category/digit and any applicable extension. Specific 2027 RUC dates were not confirmed at the read date. Sources: [RS 014-2018 art. 9](https://www.sunat.gob.pe/legislacion/superin/2018/014-2018.pdf), [RS 163-2018 arts. 8 and 17](https://www.sunat.gob.pe/legislacion/superin/2018/163-2018.pdf).

**Local file, Formulario Virtual 3560.** Under RS 014-2018 arts. 4-10:

1. Confirm the art. 3 exclusions and art. 2 threshold route. For the limited tier prepare Annex I data. For the fuller tier prepare Annex II data, Annex III narrative/PDF and Annex IV calculation/Excel information. Check SUNAT's current annex version before building the upload.
2. Log into **SUNAT Operaciones en Linea** using the taxpayer's SOL credentials. Choose `Presento mis declaraciones informativas / Informativas / Presentacion de declaraciones informativas`.
3. Choose `Formulario Virtual` and `Precios de Transferencia - Reporte Local`, enter the reporting exercise, complete the relevant annex data and import/attach the required files in the prescribed formats. Use the form's named fields; no unverified numbered box is supplied here.
4. Run the system validations and obtain authorised human submission. Structural or consistency rejection means the declaration was **not filed**.
5. Save the `constancia de presentacion` with the exercise, RUC, filed data and attachments. The informative declaration itself does not create a tax-payment reference. Any annual income-tax adjustment follows the separate return/payment process.
6. For replacement/correction, re-enter all required information, including unchanged items: the new declaration supersedes the previous one.

Source for the complete sequence: [RS 014-2018 arts. 4-10](https://www.sunat.gob.pe/legislacion/superin/2018/014-2018.pdf).

**Master file, Formulario Virtual 3561.** Confirm both thresholds and group membership; use the same SOL menu, select `Precios de Transferencia - Reporte Maestro`, and import the Annex I PDF/group information. Rejection is non-filing; save the accepted receipt. A correction replaces the whole earlier declaration. [RS 163-2018 arts. 2-9](https://www.sunat.gob.pe/legislacion/superin/2018/163-2018.pdf).

**CbC, Formulario Virtual 3562.** Test prior-year consolidated income and filing-person status first. For a Peru ultimate parent the report is local; for a Peru entity in a foreign-parented group apply Regulation art. 116(b): no parent reporting duty, the specified missing exchange agreement, notified systemic failure, or a designated Peru surrogate. The foreign parent's EUR **750 million** or local-equivalent exclusion and the qualifying foreign-surrogate exception must also be tested. An ordinary foreign group membership does not alone make every Peru subsidiary a CbC filer. Check actual exchange status and notices for that group/year. [Regulation art. 116(b)](https://www.sunat.gob.pe/legislacion/renta/regla/cap19.pdf).

Where RS 163-2018 art. 10.1.2 applies, communicate the Peru designated filer using Annex II by the last business day of the month before the reporting month, under art. 10.2; failure can make all Peru constituents responsible under art. 10.3. A qualifying foreign surrogate requires the separate art. 11 communication and supporting copy by the reporting deadline. Then select `Precios de Transferencia - Reporte Pais por Pais` in SOL and import the prescribed XML for Annexes III/IV. Save acceptance and the receipt; structural rejection is non-filing. [RS 163-2018 arts. 10-18](https://www.sunat.gob.pe/legislacion/superin/2018/163-2018.pdf).

## Penalties and interest

Classify the failure before calculating a sanction. For an ordinary Table I business, missing/late TP informative declarations and incomplete/untrue declarations fall under Tax Code arts. 176(2) and 176(4), with the TP-specific annual-IN formula in the rates table. Failure to produce supporting documents/Spanish translations on request is a distinct art. 177(27) offence; Table I uses **0.6% of IN**, subject to notes 10 and 20 and the applicable art. 180 alternative bases. Do not apply a beneficial-owner penalty range to a TP report. [Tax Code arts. 176-180 and Table I](https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf).

IN is the statutory net-sales/services/other-income base defined in art. 180(b), not the related-party transaction amount. For General Regime and MYPE businesses, normally use the annual return for the year before commission or detection of the offence, as applicable. If commission or detection occurs before presentation or expiry of the annual-return deadline, art. 180(b) instead requires the annual return for the year preceding that prior year (`ejercicio precedente al anterior`). Establish the offence/detection date and the actual filing and due dates before selecting the income year. If the income/return facts needed by art. 180 are missing, do not substitute an invented IN. Assess the correct taxpayer table, UIT at the legally relevant time, notice date, correction/payment and any applicable graduality/discretion before giving a payable fine. Interest on unpaid tax is a separate calculation under art. 33; use the published SUNAT rate for the actual overdue days. Current relief percentages and a numeric interest rate are not asserted here. [Tax Code arts. 33, 166 and 180](https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf).

## Cross-border points

TP pricing, non-resident withholding, customs valuation and indirect tax are separate analyses. An arm's-length price does not establish treaty entitlement or eliminate withholding. The withholding agent can have a liability for an adjustment involving a non-resident under LIR art. 32-A(c). [LIR art. 32-A(c)](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf).

Corresponding adjustments follow the applicable treaty and require the foreign adjustment and Peru acceptance described in LIR art. 32-A(c) and Regulation art. 109(c). Do not automatically mirror a foreign audit into a Peru refund. An APA can settle the specified pricing methodology prospectively; bilateral/multilateral agreements and rollback require the treaty/competent-authority conditions of art. 32-A(f), including unchanged material facts, an open limitation period and the assessment exclusion. Refer the application rather than promise approval. [LIR art. 32-A(f)](https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf), [Regulation arts. 109 and 118](https://www.sunat.gob.pe/legislacion/renta/regla/cap19.pdf).

## Two worked examples that recompute

### 1. Choose the reporting tier at the exact boundary

A Peru-domiciled ordinary company has 2026 accrued income PEN 13,000,000 and TP operations PEN 2,200,000. It has no art. 3 exclusion and no below-cost goods sale. The 2026 UIT is PEN 5,500. Income exceeds 2,300 UIT by PEN 350,000. Operations equal 400 UIT, so it needs the fuller local-file information, not Annex I alone. If operations had instead been PEN 2,199,999 with all other facts unchanged, they would be above 100 UIT but below 400 UIT, selecting the limited tier. These are filing decisions, not price safe harbours. Sources: RS 014-2018 arts. 2 and 4 and the UIT source in the rates table.

```oa-check
name: 2026 local file, exact 400 UIT versus one sol below
inputs:
  uit: 5500
  income: 13000000
  operations: 2200000
  alternative_operations: 2199999
steps:
  - income_gate: 2300 * uit
  - limited_start: 100 * uit
  - full_start: 400 * uit
  - income_excess: income - income_gate
  - exact_boundary_difference: operations - full_start
  - alternative_below_full: full_start - alternative_operations
expected:
  income_gate: 12650000
  limited_start: 550000
  full_start: 2200000
  income_excess: 350000
  exact_boundary_difference: 0
  alternative_below_full: 1
```

### 2. A qualifying support-service charge and a failed benefit test

An independent source analysis establishes that an actual related-party support service meets all low-value characteristics and that PEN 100,000 of provider cost is reasonably allocated to the Peru recipient. Its invoice is PEN 108,000. The supported deduction ceiling before other income-tax limits is PEN 105,000, leaving a PEN 3,000 excess. For the alternative decision, if the same charge is a parent-only shareholder activity with no recipient benefit, the maximum under this service-benefit test is zero, not cost plus the capped markup. This example does not assume all management services are low-value. The invoice, allocated cost and benefit facts are hypothetical; the legal deduction and benefit rules are LIR art. 32-A(i) and Regulation art. 118-A.

```oa-check
name: Low-value support service, qualifying versus parent-only activity
inputs:
  supported_cost: 100000
  invoice: 108000
  markup_cap: 0.05
  benefit_failed_deduction: 0
steps:
  - capped_markup: supported_cost * markup_cap
  - ceiling: supported_cost + capped_markup
  - qualifying_deduction: min(invoice, ceiling)
  - qualifying_excess: invoice - qualifying_deduction
  - parent_only_addback: invoice - benefit_failed_deduction
expected:
  capped_markup: 5000
  ceiling: 105000
  qualifying_deduction: 105000
  qualifying_excess: 3000
  parent_only_addback: 108000
```

## Ask the client first

1. The reporting exercise, Peru domicile/tax regime, RUC and whether the business falls within a reporting exemption.
2. The full ownership/control/family/PE chart, when relationships existed and counterparty countries or preferential regimes.
3. Accrued income and the non-netted transaction schedule, including gratuitous transfers, below-cost goods and any commodity exports/imports.
4. Contracts, delivery/benefit evidence, provider costs and allocations, tested-party selection and actual comparable data.
5. Group membership, ultimate parent, prior-year consolidated income, CbC filing jurisdiction, surrogate designation and exchange/failure notices.
6. Existing reports, receipts, tax returns, APAs/MAPs, audits, notices and dates needed to assess corrections, relief and interest.

## Sources

| Source and portions actually read | URL | Read on |
|---|---|---|
| LIR, DS 179-2004-EF consolidated Chapter V; read arts. 32(4), 32-A(a)-(i), amendment notes and adjacent exceptions, not every historical text | https://www.sunat.gob.pe/legislacion/renta/ley/capv.pdf | 2026-11-11 |
| Regulation, DS 122-94-EF consolidated Chapter VI; read art. 24 relationship routes and timing | https://www.sunat.gob.pe/legislacion/renta/regla/cap6.pdf | 2026-11-11 |
| Regulation Chapter XIX; read arts. 108-109, 114-116, 118 and 118-A; reviewed method headings and DS 302-2025-EF amendment notes, not a full technical valuation implementation | https://www.sunat.gob.pe/legislacion/renta/regla/cap19.pdf | 2026-11-11 |
| RS 014-2018/SUNAT; read arts. 1-10, local reporting population, thresholds, exclusions, uploads and receipt rules | https://www.sunat.gob.pe/legislacion/superin/2018/014-2018.pdf | 2026-11-11 |
| RS 163-2018/SUNAT; read arts. 1-18, master/CbC population, notifications, uploads and filing periods | https://www.sunat.gob.pe/legislacion/superin/2018/163-2018.pdf | 2026-11-11 |
| SUNAT UIT table; read 2026 row and legal instrument DS 301-2025-EF | https://www.sunat.gob.pe/indicestasas/uit.html | 2026-11-11 |
| SUNAT Informe 000042-2026; read issue, legal framework and conclusion on other-methods timing | https://www.sunat.gob.pe/legislacion/oficios/2026/informe-oficios/i000042-2026-7T0000.pdf | 2026-11-11 |
| Tax Code, DS 133-2013-EF consolidated through 26 June 2026; read arts. 176-180 and Table I rows/notes 10, 14 and 20; consulted art. 33 for interest framework | https://www.sunat.gob.pe/legislacion/codigo/textoCompleto-TUO-CT.pdf | 2026-11-11 |

Not yet confirmed: exact 2027 RUC-specific filing dates for 2026 reports; current annex upload schemas and post-2018 annex changes; group-specific CbC exchange status and notifications; current penalty graduality/discretion percentages and the numeric interest rate for any late-payment period. No unconfirmed date, technical upload limit, relief percentage or interest figure is supplied. Commodity-specific alternative-method applications and full technical valuation/APA procedures are outside this skill's ordinary reporting and pricing-file scope.

## Today's figures and who stands behind this skill

This file is an AI skill (tax rules your AI follows) from OpenAccountants, copied on 2026-11-11. Rates, thresholds and deadlines change. For the current version of this skill, its official sources and the named accountant (if any) who stands behind it, call `get_skill` with slug `peru-transfer-pricing` on the OpenAccountants connector (https://www.openaccountants.com/connect), or read https://www.openaccountants.com/skills/peru-transfer-pricing. If neither is available, confirm every figure against the official source pages cited above before relying on it.
