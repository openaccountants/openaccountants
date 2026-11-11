---
name: co-tax-overview
description: >
  Colombia tax overview and routing for income year 2026, distinguishing the 2026 filing calendar for
  earlier income from future returns. Covers taxpayer, residence/source, annual period, COP and UVT,
  ordinary personal marginal and corporate rates, conditional corporate minimum test and standard IVA.
  Routes individual, corporate, SIMPLE/formalisation, VAT, payroll, independent contributions, transfer
  pricing, cross-border and company-formation work to their owning Guides. Trigger on Colombian tax
  overview, impuestos Colombia, UVT 2026, DIAN, which tax return, tax residence and company versus
  individual tax. Includes one recomputing unit/marginal-band orientation case. Excludes complete return
  preparation, local tax, special-sector and treaty computations and unconfirmed future deadlines.
jurisdiction: CO
category: orchestrator
tax_year: 2026
tax_year_notes: "calendar 2026 income; 2026 filing calendar concerns earlier annual income"
last_updated: 2026-11-11
version: 0.1
type: router
tier: 2
domain: income-tax
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Colombia tax overview and Guide routing, income year 2026 v0.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

**Quick answer.** Identify the taxpayer, residence, income year, activity and actual DIAN responsibilities before selecting a Colombian return. This overview routes ordinary 2026 work to the owning Guides. It is an orientation table and intake workflow, not a complete computation. A return filed during 2026 generally concerns earlier annual income; monthly withholding and IVA periods remain separate. The UVT for 2026 is COP 52,374, not the prior year's unit.

DIAN means Dirección de Impuestos y Aduanas Nacionales. Its national responsibilities do not make it the administrator of every departmental or municipal tax. The monetary unit is the Colombian peso (COP); UVT is an annually adjusted tax-value unit, not another currency or a minimum wage. A general rate, marginal rate, withholding and minimum-tax test answer different questions. Do not add their percentages together or apply a headline rate to gross receipts without the actual legal base.

## Ask the client first

1. Income year, filing year, tax period and actual DIAN notice/return, including a first or final short year.
2. Natural person, domestic company, foreign entity or Colombian permanent establishment; residence and source facts.
3. Employment, services, business, rent, gains, dividends, imports or other activity; ordinary regime or an actual SIMPLE election.
4. RUT/NIT, registered responsibilities, revenue/cost records, prior returns, electronic signature and current notices.
5. Taxable/excluded/exempt IVA transactions, withholding-agent status, staff and independent contributions.
6. Related-party or overseas transactions, ownership, foreign taxes, local registrations and unresolved elections.

## Rates, bands and thresholds

| Orientation item | Figure and condition | Period | Official source |
|---|---|---|---|
| Ordinary income-tax year | 1 January to 31 December, with specified shorter periods for newly formed entities and other statutory cases | Income year 2026 | [DUR 1625 art. 1.6.1.5.7](https://normograma.dian.gov.co/dian/compilacion/docs/decreto_1625_2016.htm#1.6.1.5.7) |
| Monetary unit | Colombian peso; UVT is the ET's separate tax-value unit | 2026 | [Ley 31/1992 art. 6, quoted by Banco de la República](https://www.banrep.gov.co/es/banco/junta-directiva/conceptos/jds-16276); [ET art. 868, quoted in current DIAN Res. 238](https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0238_2025.htm) |
| UVT | COP 52,374 per UVT for calendar 2026; do not use this unit for a different year's statutory measurement | 2026 | [DIAN Res. 000238/2025 art. 1](https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0238_2025.htm): “($52.374)” |
| Natural-person source rule | Residents: national and foreign-source income/gains; non-residents without a Colombian PE: Colombian-source income/gains; PE attribution is tested separately. Residence is established under all relevant art. 10 tests, not nationality alone | 2026 | [ET arts. 9-10](https://normativa.colpensiones.gov.co/compilacion/docs/estatuto_tributario.htm) |
| Resident ordinary art. 241 top marginal band | 39% on the part above 31,000 UVT; the table formula is (base UVT − 31,000) × 39% + 10,352 UVT. This is not the rate on every receipt or every separate income category | 2026 law; dated official table corroborates statutory rate | [ET art. 241](https://normativa.colpensiones.gov.co/compilacion/docs/estatuto_tributario.htm); [DIAN table, rate row](https://micrositios.dian.gov.co/renta-personas-naturales-ag-2024/preparese-para-la-declaracion-de-renta/) |
| General company income-tax rate | 35% on the applicable income-tax base for the taxpayers within art. 240. Special rates, surcharges, free zones and SIMPLE are separate tests | 2026 | [ET art. 240](https://normativa.colpensiones.gov.co/compilacion/docs/estatuto_tributario.htm): “treinta y cinco por ciento (35%)” |
| Corporate minimum test | 15% Tasa de Tributación Depurada (TTD), calculated using Impuesto Depurado / Utilidad Depurada under art. 240 paragraph 6, with scope, exclusions and consolidation rules. Not a universal 15% tax on revenue | 2026 | [ET art. 240 paragraph 6](https://normativa.colpensiones.gov.co/compilacion/docs/estatuto_tributario.htm) |
| General IVA | 19%, except the title's specific exceptions; liability, zero-rated/exempt/excluded treatment and credits require the transaction analysis | 2026 | [ET art. 468](https://normativa.colpensiones.gov.co/compilacion/docs/estatuto_tributario.htm): “diecinueve por ciento (19%) salvo las excepciones” |
| Historical filing-calendar orientation only | The published 2026 annual calendar concerns 2025 income: ordinary legal-person declarations 12–26 May 2026; large taxpayers 13–24 April; resident individuals 12 August–26 October. This is the ordinary baseline, not every current deadline: Decreto 1226/2026 extends specified August-due individuals/successions in affected DIAN districts. Different classes/payment instalments use their actual NIT rules; individual schedule uses the last two digits | Filing year 2026, not income year 2026 | [DIAN 2026 calendar announcement](https://www.dian.gov.co/Prensa/Paginas/NG-Comunicado-de-Prensa-128-2025.aspx) |

The old overview's 2025 UVT has been replaced, not rolled forward. A 2026 auditor test based on prior-year accounts can still use a prior-year minimum wage; load the formation Guide for that distinct rule. Do not use the 2026 UVT or the current wage simply because today's date is in 2026.

The TTD row does not state that every resident corporation always pays exactly 15% or that it replaces the ordinary 35% rate. Paragraph 6 excludes foreign legal persons without Colombian residence in its opening scope and specifies further ZESE/ZOMAC and paragraph 5/7 cases subject to conditions, paragraph 1 entities, relevant nonpositive adjusted-profit cases and art. 32 cases. It has a separate consolidated-group calculation. Load the corporate Guide to determine scope and adjusted figures; accounting profit, taxable income, revenue and Utilidad Depurada are not interchangeable.

## The method, step by step

1. **Fix the job and period.** Separate 2026 economic income from an annual return submitted in 2026, an IVA period and a withholding month. Under DUR 1625 art. 1.6.1.5.7, the general annual period is the calendar year, with specified shorter periods. Return the actual year, taxpayer class, fiscal domicile and applicable ordinary or special calendar entry alongside every deadline. Decreto 1226/2026 transitory art. 1.6.1.13.2.15 grants 27 October–13 November 2026 dates to specified August-due natural persons/successions with NIT endings 01–26 and fiscal domicile on 10 August 2026 in the named affected seccionales; Grandes Contribuyentes are excluded. Include the decree’s first-time RUT/domicile exceptions and the evidence rule for qualifying post-event RUT changes. Test all conditions and the actual band, not this summary alone. Do not carry the historical calendar row into the still-unconfirmed 2027 filing calendar.
2. **Establish the correct taxpayer and source rule.** Load [colombia-cross-border](colombia-cross-border.md) for residence, migration, overseas income/payees, permanent establishments, treaties, withholding and foreign credits. Natural-person ET art. 9 is not a complete company rule. Domestic companies have their own ET arts. 12/12-1 test; foreign PE/branch attribution can include foreign-source income attributable to it under DUR 1625 art. 1.2.1.1.5. A person outside Colombia or a foreign customer does not alone resolve source or residence.
3. **Route individual income.** Load [colombia-income-tax](colombia-income-tax.md) for the return obligation, cedulas, taxable base, exemptions/deductions, gains and tax/credit calculation. Apply the correct year's UVT and the correct income-category table. The 39% row is the top marginal ordinary art. 241 band; it is not a flat effective rate. Withholding and payments credited against annual liability need their own reconciliation.
4. **Route company and small-business work.** Use [co-corporate-income-tax](co-corporate-income-tax.md) for ordinary company income tax, losses, rates/surcharges, TTD, credits and filing/payment. Use [formalizing-small-informal-businesses-in-colombia](formalizing-small-informal-businesses-in-colombia.md) for SIMPLE eligibility, registration and formalisation choices. An SAS legal form is not a SIMPLE election and a small turnover is not evidence that every eligibility condition is met.
5. **Route IVA, documents and withholding.** Load [co-vat-return](co-vat-return.md) for transaction scope, responsibility, taxable/exempt/excluded supplies, base, input tax, periodicity, invoicing and the actual filing route. Use that current owner instead of the duplicate `colombia-iva.md`. ET art. 600 sets IVA periods by class; art. 605 concerns withholding-agent declarations. Formation alone does not mean every entity files both from day one. Current responsibilities and underlying transactions control.
6. **Route people and contributions.** Use [colombia-payroll](colombia-payroll.md) for employed workers, payroll withholding, employer charges and actual employee records. Use [co-social-contributions](co-social-contributions.md) for independent IBC, costs, PILA, health/pension/ARL and the applicable current rules. Do not infer employment status from an invoice. A pension reform's enacted text and its commencement date are separate questions; use the contribution owner's current effective-law analysis.
7. **Route structure and related parties.** Load [co-company-formation](co-company-formation.md) for legal form, Chamber/RUT/NIT, capital, registry tax, renewal, auditor and beneficial-owner reporting. Load [colombia-transfer-pricing](colombia-transfer-pricing.md) for controlled transactions, documentation and disclosure. Keep incorporation, tax registration, electronic invoicing readiness and actual ongoing compliance as distinct completed records.
8. **Prepare the handoff and verify the filing.** Return the chosen Guide(s), legal period, documents, taxpayer class, source provisions, unresolved elections and exact current calendar entry. Electronic services and signature readiness are part of the current DIAN workflow, but a draft, saved form or payment instruction is not a filing receipt. Preserve the actual submitted return, acknowledgement and separate payment evidence. This router does not certify that any return has been filed.

## Worked orientation example

Assume the ordinary art. 241 table applies after the owning Guide has determined a resident individual's annual taxable base. With 2026 UVT COP 52,374, 31,000 UVT equals COP 1,623,594,000. An illustrative base of 31,001 UVT is one UVT into the top band. The table expression gives 10,352 + 0.39 = 10,352.39 UVT, or COP 542,196,073.86 before the return's statutory rounding, credits and payments. This checks the marginal-band distinction and unit conversion only; it is not a completed return or a result for gross income of that amount.

```oa-check
name: CO 2026 ordinary top-band orientation with annual UVT
inputs:
  uvt_2026: 52374
  top_band_uvt: 31000
  assumed_taxable_uvt: 31001
  fixed_tax_uvt: 10352
steps:
  - top_band_pesos: uvt_2026 * top_band_uvt
  - marginal_slice_uvt: assumed_taxable_uvt - top_band_uvt
  - table_tax_uvt: fixed_tax_uvt + marginal_slice_uvt * 0.39
  - table_tax_pesos: table_tax_uvt * uvt_2026
expected:
  top_band_pesos: 1623594000
  marginal_slice_uvt: 1
  table_tax_uvt: 10352.39
  table_tax_pesos: 542196073.86
```

## When to refuse or refer

Refer unresolved residence/source, an unproved SIMPLE election, an unavailable current source, an adjusted-tax/consolidation dispute, treaty entitlement, a regulated or special sector and missing filing documents to the owning specialist workflow. Do not substitute the general table for a complete tax base or a current-year calendar. Municipal ICA and other local taxes require the actual territory's law; the national orientation is not their computation. Special regimes, wealth tax, consumption taxes, customs and treaty-rate tables are outside this overview's computation scope.

A dated DIAN personal-tax page is used solely to corroborate the unchanged art. 241 rate/formula, not its historical filing thresholds, UVT or deadlines. The current law and 2026 unit are separately sourced. Likewise, the old approximate “mid-year / last digit” annual statement is replaced with class-specific historical calendar context and a current-calendar handoff; no 2027 due date is guessed.

## Sources

| Source and portions read | Official URL | Read on |
|---|---|---|
| ET current consolidated arts. 9-12/12-1,20-20-2,240 including paragraph 6,241,468,555-2,600,605 | https://normativa.colpensiones.gov.co/compilacion/docs/estatuto_tributario.htm | 2026-11-11 |
| Current DUR 1625, arts. 1.6.1.5.7 annual period/short years and 1.2.1.1.5 foreign PE/branch attribution | https://normograma.dian.gov.co/dian/compilacion/docs/decreto_1625_2016.htm | 2026-11-11 |
| DIAN Res. 000238/2025 art. 1, 2026 UVT | https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0238_2025.htm | 2026-11-11 |
| DIAN published art. 241 table, >31,000 /39% /10,352 formula, rate only; page concerns income year 2024 | https://micrositios.dian.gov.co/renta-personas-naturales-ag-2024/preparese-para-la-declaracion-de-renta/ | 2026-11-11 |
| DIAN announcement of the 2026 filing calendar for 2025 income, taxpayer classes, dates and NIT rules | https://www.dian.gov.co/Prensa/Paginas/NG-Comunicado-de-Prensa-128-2025.aspx | 2026-11-11 |
| Decreto 1226/2026, transitory individual/succession deadline extension with NIT, domicile, district and class conditions | https://normograma.dian.gov.co/dian/compilacion/docs/decreto_1226_2026.htm | 2026-11-11 |
| DIAN release105/2026, operational explanation of that special extension | https://www.dian.gov.co/Prensa/Paginas/NG-Comunicado-de-Prensa-105-2026.aspx | 2026-11-11 |
| Banco de la República official legal concept quoting Ley 31/1992 art. 6, peso monetary/account unit | https://www.banrep.gov.co/es/banco/junta-directiva/conceptos/jds-16276 | 2026-11-11 |
| DIAN Res. 227/2025, current RUT and electronic registration workflow identified for formation handoff | https://normograma.dian.gov.co/dian/compilacion/docs/resolucion_dian_0227_2025.htm | 2026-11-11 |

Not yet confirmed: the complete 2027 filing/payment calendar for 2026 income, the actual taxpayer's electronic filing/rounding fields, local ICA and special-sector calculations, and case-specific residence/treaty/SIMPLE/TTD elections or classifications not proved here. They must be resolved through the linked owner and current original; none is inferred from a historical deadline, general rate or prior year's unit.
