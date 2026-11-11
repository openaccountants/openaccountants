---
name: ar-monotributo
description: >
  Use this Guide for Argentina Monotributo in 2026: regimen simplificado,
  monotributista, categorias A a K, impuesto integrado, SIPA, obra social,
  recategorizacion, Factura C, Factura E, exclusion and renuncia. It covers
  individual small businesses and qualifying continuing estates, the current
  category parameters and monthly components, contribution exceptions,
  semestral review, invoicing, payment, exclusion and the general-regime
  handoff. It distinguishes January, February-July and August-onward table
  periods. It prepares working papers for professional review, not a filing
  authority. Special social/promoted/cooperative regimes, foreign exchange
  controls and detailed transition-benefit computations require separate
  review. Do not treat a bank credit or foreign payout label as proof of
  taxable revenue or export status.
version: 2.1
jurisdiction: AR
tax_year: 2026
last_updated: 2026-11-11
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Argentina: Monotributo 2026 v2.1

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals carrying on eligible sales, leases, services, works and primary activities under the Annex to Ley 24.977 art. 2. The law includes qualifying worker-cooperative members and continuing estates, but not SA/SRL/SAS companies. A continuing estate may remain only until the earlier of the end of the month of the inheritance declaration/validating will or one year after death. Company direction/administration is outside eligible Monotributo activities. Do not treat a director's separate professional business as automatically the same activity.

**Quick answer:** establish the table period and all relevant trailing-period parameters, choose the category required by the highest applicable parameter, then add only the monthly components actually owed. Both services and goods can reach category K; the old services-only H ceiling is obsolete. Physical/rental parameters do not disappear merely because the person provides services. Missing inputs stop the calculation; do not assume zero employees or a convenient activity type.

This version is a Tier 2 source-cited draft without accountant approval. It loads the existing income-tax workflow base and produces a category/payment reconciliation, evidence list and exception flags. Monotributo substitutes the national IVA/Ganancias and the specified contribution obligations for the covered activity; provincial gross-receipts obligations can remain, including unified collection where applicable. Use [argentina-income-tax](argentina-income-tax.md), [argentina-iva](argentina-iva.md) and [ar-social-contributions](ar-social-contributions.md) when the general regime applies.

Out of scope: detailed Monotributo Social/promoted/cooperative contribution computations, foreign-exchange permissions, provincial unified components, and general-regime transition benefits. The ordinary eligibility and exclusion screening still needs those facts. A general-regime transition or an exclusion cannot be solved by paying a higher Monotributo category.

## Rates, bands and thresholds

### Select the correct table for the 2026 month

| Period | Official table to read | Source |
|---|---|---|
| January 2026 | Values valid from 1 August 2025 to 31 January 2026 | https://www.arca.gob.ar/monotributo/documentos/categorias/monotributo-categorias-agosto-2025-enero-2026.pdf |
| February-July 2026 | Values valid 1 February to 31 July 2026 | https://www.arca.gob.ar/monotributo/documentos/categorias/monotributo-categorias-febrero-julio-2026.pdf |
| From 1 August 2026 | Current official HTML table reproduced below | https://www.arca.gob.ar/monotributo/categorias.asp |

Do not backdate August amounts into January or use an annualised current monthly fee as the actual cost of the full 2026 year. The official historical PDFs carry all category rows and component/physical parameters for their named periods; use the matching row when rebuilding an earlier month.

### Current category parameters, from 1 August 2026

All money values ARS. These are maximum annual gross receipts/rent and maximum unit goods price, not monthly turnover thresholds. Area and electricity are applied subject to the law's activity/town exceptions. Each row is from the same official category table, including its notes.

| Category | Annual gross receipts maximum | Surface maximum | Annual electricity maximum | Annual rent maximum | Unit goods price maximum | Official source |
|---|---|---|---|---|---|---|
| A | $12.009.410,45 | Hasta 30 m² | Hasta 3330 kWh | $2.792.886,15 | $716.840,77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| B | $17.595.182,74 | Hasta 45 m² | Hasta 5000 kWh | $2.792.886,15 | $716.840,77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| C | $24.670.494,31 | Hasta 60 m² | Hasta 6700 kWh | $3.816.944,41 | $716.840,77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| D | $30.628.651,43 | Hasta 85 m² | Hasta 10000 kWh | $3.816.944,41 | $716.840,77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| E | $36.028.231,33 | Hasta 110 m² | Hasta 13000 kWh | $4.841.002,66 | $716.840,77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| F | $45.151.659,41 | Hasta 150 m² | Hasta 16500 kWh | $4.841.002,66 | $716.840,77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| G | $53.995.798,87 | Hasta 200 m² | Hasta 20000 kWh | $5.771.964,69 | $716.840,77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| H | $81.924.660,37 | Hasta 200 m² | Hasta 20000 kWh | $8.378.658,45 | $716.840,77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| I | $91.699.761,90 | Hasta 200 m² | Hasta 20000 kWh | $8.378.658,45 | $716.840,77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| J | $105.012.519,20 | Hasta 200 m² | Hasta 20000 kWh | $8.378.658,45 | $716.840,77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| K | $126.610.838,75 | Hasta 200 m² | Hasta 20000 kWh | $8.378.658,45 | $716.840,77 | https://www.arca.gob.ar/monotributo/categorias.asp |

### Monthly components, from 1 August 2026

Services and goods have separate integrated-tax columns, not separate revenue ceilings. The full totals below assume ordinary pension and individual health contributions without adherents; test the exceptions before using them.

| Category | Integrated services | Integrated goods | SIPA | Individual health | Total services | Total goods | Official source |
|---|---|---|---|---|---|---|---|
| A | $5.585,77 | $5.585,77 | $18.246,86 | $25.694,55 | $49.527,18 | $49.527,18 | https://www.arca.gob.ar/monotributo/categorias.asp |
| B | $10.612,98 | $10.612,98 | $20.071,55 | $25.694,55 | $56.379,08 | $56.379,08 | https://www.arca.gob.ar/monotributo/categorias.asp |
| C | $18.246,86 | $16.757,32 | $22.078,71 | $25.694,55 | $66.020,12 | $64.530,58 | https://www.arca.gob.ar/monotributo/categorias.asp |
| D | $29.790,79 | $27.742,67 | $24.286,58 | $30.535,56 | $84.612,93 | $82.564,81 | https://www.arca.gob.ar/monotributo/categorias.asp |
| E | $55.857,73 | $44.313,79 | $26.715,24 | $37.238,48 | $119.811,45 | $108.267,51 | https://www.arca.gob.ar/monotributo/categorias.asp |
| F | $78.573,20 | $57.719,64 | $29.386,76 | $42.824,25 | $150.784,21 | $129.930,65 | https://www.arca.gob.ar/monotributo/categorias.asp |
| G | $142.995,76 | $71.497,87 | $41.141,46 | $46.175,72 | $230.312,94 | $158.815,05 | https://www.arca.gob.ar/monotributo/categorias.asp |
| H | $409.623,31 | $204.811,64 | $57.598,04 | $55.485,33 | $522.706,68 | $317.895,01 | https://www.arca.gob.ar/monotributo/categorias.asp |
| I | $814.591,79 | $325.836,71 | $80.637,26 | $68.518,81 | $963.747,86 | $474.992,78 | https://www.arca.gob.ar/monotributo/categorias.asp |
| J | $977.510,14 | $391.004,07 | $112.892,16 | $76.897,46 | $1.167.299,76 | $580.793,69 | https://www.arca.gob.ar/monotributo/categorias.asp |
| K | $1.368.514,20 | $456.171,40 | $158.049,02 | $87.882,82 | $1.614.446,04 | $702.103,24 | https://www.arca.gob.ar/monotributo/categorias.asp |

Under the source notes, the surface parameter is not considered in towns up to 40,000 inhabitants except ARCA-specified zones/activities. This exception concerns surface, not an automatic exemption from every parameter. An individual health amount covers no adherents; each additional adherent adds that same category health amount. Example: category A with one adherent adds ARS 25,694.55 to the ordinary total, subject to actual health enrolment entitlement.

| Exception | Effect | Official source |
|---|---|---|
| Independent promoted worker, qualifying cooperative member/registered social-economy participant | Integrated-tax relief only as the applicable conditions provide; do not use the ordinary total blindly | Current table note (*); https://www.arca.gob.ar/monotributo/categorias.asp |
| Exclusive landlord of up to two properties, including relevant individual condo interests | Integrated-tax exemption under current table note; statutory rental conditions need checking | Same |
| Exclusive primary tobacco/sugar-cane/yerba-mate/tea activity, receipts within D | Integrated-tax exception in table note; special regime facts required | Same |
| Mandatory coverage by another pension regime, under 18, covered movable/immovable rental activity, qualifying estate | Contribution exceptions in note (***); verify precise legal status | Same |
| Retired under pre-July-1994 laws | Pension and health contribution exception as stated; later retirement has different pension treatment | Same |
| Retiree under either applicable pension-law group | No health contribution under note (***); do not infer pension exemption for later retirees | Same |

Read the statutory contribution exceptions under Annex arts. 39-40 alongside the table, especially employment with pension contributions and professional provincial funds. Mere possession of a health policy does not establish contribution exemption.

## The base

### Eligibility and category computation

Use [Ley 24.977 Annex arts. 2-9, 20-24 and 39-40](https://biblioteca.arca.gob.ar/search/query/dcp/LEY_C_024977_1998_06_03), current amended text, and [Decreto 1/2010](https://biblioteca.arca.gob.ar/search/query/dcp/DEC_C_000001_2010_01_04). Do not read an embedded historical H/I/L category table as current.

1. Confirm eligible person/activity, prior twelve-month receipts, units/activities, imports for resale, goods unit price, affected premises, electricity and rent. General entry conditions require no more than three simultaneous activities or three units. Properly registered property-rental contracts have the statutory single-unit rule regardless of property count; exclusive rental of up to two properties has the stated exemption. Refer mixed/special cases before applying the ordinary total.
2. Reconcile gross receipts for the applicable activity across invoices, credit notes, cash, bank, payment processors and exports. Category receipts are gross activity receipts; the regime does not deduct ordinary business expenses to set a profit base. A merchant processor's net deposit must be reconciled to gross sale and fees, not taken as gross revenue automatically.
3. Identify each parameter's required category and choose the category where none of the relevant limits is exceeded. Do not categorise services using revenue alone. In mixed activities, aggregate covered receipts and determine the main activity for the applicable integrated-tax column; the source's legal activity rules govern, not whichever column gives the smaller fee.
4. For activity at home/shared premises, use the legally affected area, electricity and rent proportion under art. 9, with evidence. Do not simply charge the full family home's measures or ignore them. Startup/less-than-full-year annualisation and activity-specific exceptions require the implementing rules; stop rather than inventing twelve months of turnover.
5. Determine integrated tax, SIPA and health components separately. Apply only proven exemptions and add adherents. Keep provincial/unified charges distinct from the federal table. Reconcile the total to the portal credential and CCMA.
6. Review recategorisation at each semester end and continuously monitor automatic-exclusion triggers. A category update is different from an exclusion: exceeding category D while fitting E means category review; exceeding K or another exclusion condition ends eligibility.

### Bank-statement and platform reconciliation

The earlier pattern library is retained as an evidence workflow, not a statutory classifier. **CLIENT PAYMENT, TRANSFERENCIA, FACTURA C, Mercado Pago/Mercado Libre, PedidosYa/Rappi** and other platform deposits need invoice/gross-receipt matching. **TRANSFERENCIA PROPIA/AHORRO** can be excluded from revenue only after tracing both accounts. **DEVOLUCION/REINTEGRO** needs the original invoice/credit note. **SUBSIDIO/PLAN SOCIAL** and **INTERESES/PLAZO FIJO** must be classified under their actual legal nature; their labels alone do not justify inclusion/exclusion.

**PayPal, Wise, Payoneer or Stripe** does not prove foreign-source income or export: inspect customer, service/use, invoice and transaction facts. A qualifying export of services is business revenue and uses Factura E; do not assume every foreign receipt is an export or current exchange permission exists. Currency conversion and BCRA collection rules are referred until the applicable official rule is read.

On debits, match **MONOTRIBUTO/VEP/DEBITO AUTOMATICO** to CCMA period/component. Separate **IIBB/Ingresos Brutos** from the national payment; personal groceries/rent are not profit deductions against the fixed national fee. Expenses still matter for evidence, exclusion screening and other taxes. Bank PDF/CSV column names and export layouts must come from the actual statement, not a generic bank-format promise.

### Exclusion conditions

[Current ARCA exclusion guidance](https://www.arca.gob.ar/monotributo/ayuda/exclusion.asp), reflecting Annex arts. 20-21, lists these ordinary triggers:

- Trailing twelve-month gross receipts exceed K, or relevant surface/electricity/rent exceeds the K limits.
- Unit goods price exceeds the maximum; imports of goods/services for subsequent commercialisation; more than three activities/units; services miscategorised as goods.
- Incompatible personal spending or duly adjusted bank deposits without justification; missing transaction invoices; qualifying REPSAL repeat-offender status.
- Activity purchases plus expenses over the preceding twelve months reach at least 80% of K maximum receipts for goods, or 40% for services/leases/works. This is an exclusion test against K, not a deduction allowance or percentage of the person's actual sales.

Annex art. 21 makes exclusion effective from zero hour of the day the cause occurs, requiring immediate communication and general-regime registrations. Do not wait for an ARCA notice or continue treating Monotributo payments as a cure. Trace the trigger day and hand off IVA, Ganancias and social security to the relevant Guides. A voluntary renunciation instead takes effect under its own next-month rule (Annex art. 19); keep it distinct from compulsory exclusion.

| Situation | Decision and source |
|---|---|
| Category B receipts now fit C, with all other parameters fitting C | Recategorisation, not automatic exit solely because B was exceeded; Annex art. 9 |
| Goods revenue fits I but affected premises require a higher category | Use the highest required category; no revenue-only shortcut; art. 9 |
| Services receipts fit I/J/K | These categories are available under current art. 8; the old H ceiling is not an exclusion |
| Revenue exceeds K or another art. 20 cause occurs | Exclusion and immediate general-regime handoff; arts. 20-21 |
| Several provincial/employment/retirement obligations | Determine federal component exceptions and separate local liabilities; arts. 39-40, table notes |
| Social/promoted/cooperative status, foreign-currency collection or disputed exclusion | Refer specialist issue and record evidence; do not fill a missing rule from a conservative guess |

## Deadlines and filing

[ARCA recategorisation guidance](https://www.arca.gob.ar/monotributo/ayuda/recategorizacion.asp) specifies the ordinary deadline **5 February and 5 August**, reviewing the preceding twelve months. Those staying in the same category or with under six months of activity take no action under the guidance. The resulting category applies from the second month after semester end under Annex art. 9. This replaces the old Guide's unsourced January/July-20 deadline.

Enter the **Monotributo** portal with Clave Fiscal, select **Recategorización**, review the prefilled annual invoice total and correct/reconcile it using actual records. Supply receipts, affected surface/electricity/rent and other requested facts; confirm the resulting category, submit and save the updated credential and acknowledgement. The simplified display is assistance, not a substitute for cash/processor receipts or parameter checks. Exact 2026 live field numbering has not been independently confirmed.

[ARCA payment guidance](https://www.arca.gob.ar/monotributo/ayuda/pagos.asp) sets monthly payment by **the 20th**, rolled to the next business day when needed. Ordinary taxpayers of every category use electronic payment; in-person payment is reserved for the listed social/cooperative/promoted cases. Generate the appropriate VEP or use the available authorised electronic/debit route; reconcile payment in **Cuenta corriente de monotributistas y autónomos (CCMA)** by period, capital and interest. Save the receipt. Do not use the old ordinary Pago Fácil/Rapipago instruction without the specific exception.

[ARCA invoicing guidance](https://www.arca.gob.ar/monotributo/ayuda/facturacion.asp) requires **C** electronic invoices for ordinary domestic transactions and **E** for exports. Enable a point of sale in **Registro Único Tributario**, selecting the invoicing system; different methods require their own point of sale. **Comprobantes en línea** supports invoice/credit/debit documents and later consultation. Retain issuer CUIT, transaction description/amount and authorisation data with the actual issued document; do not separately charge ordinary IVA as if a registered general-regime taxpayer. Exact current mandatory invoice fields beyond this are not asserted here.

For departure, use the portal's corresponding **baja por cese, renuncia or exclusión** path and retain the effective date. [ARCA renunciation guidance](https://www.arca.gob.ar/monotributo/ayuda/renuncia.asp) and exclusion guidance state the ordinary three-calendar-year re-entry restriction. Historic relief for specified post-1-January-2024 exclusions is a separate statutory exception, not a general 2026 waiver; have a professional confirm its current route before relying on it.

## Penalties and interest

Check capital/interest in CCMA; no historic daily rate is supplied. Current penalty amounts, interest percentages and payment-plan eligibility were not confirmed. ARCA can recategorise or exclude using invoice, spending and bank information; absence of a notice does not keep an ineligible business in the regime.

For a systemic exclusion notice, ARCA's current guidance allows appeal within fifteen days through **Presentaciones Digitales**, **Exclusión de oficio del Monotributo - Apelación en término**. A fiscal inspection has the stated ten-day defence stage and then fifteen-day appeal against the resulting decision; use the actual notice/procedural calendar. Recategorisation of office likewise has a fifteen-day appeal route under its guidance. Do not invent a suspension of tax or payment obligations from an appeal alone. Detailed day-count/procedural effect requires review.

The old assertion that prolonged non-payment always suspends CUIT/health coverage is not established here. The official cancellation source identifies ten consecutive unpaid periods for administrative deregistration; health reinstatement and individual consequences require their own official check. **Mis Facilidades** is a potential payment-plan route, not automatic debt cancellation.

## Cross-border points

Eligible export business receipts enter the activity's gross-income analysis; receipt through a foreign platform does not remove them. C versus E depends on the actual operation. Source, treaty and exchange-control questions are separate; use [argentina-cross-border](argentina-cross-border.md) and refer BCRA collection/conversion issues. Do not repeat the old assumption that any foreign payer creates foreign-source income or a universally applicable exchange rate.

## Two worked examples that recompute

### 1. Services consultant in D, current monthly fee

Assume eligible full-year individual services activity, twelve-month receipts ARS 28,000,000, every other applicable parameter fits D, no component exemption or adherents, and the month is November 2026. D's 30,628,651.43 receipts limit is met. Monthly fee = 29,790.79 integrated tax + 24,286.58 SIPA + 30,535.56 health = 84,612.93. Multiplying by twelve gives 1,015,355.16 **at this unchanged monthly rate**, not actual full-year 2026 cost because earlier table periods differ.

```oa-check
name: Current category D services monthly components
inputs:
  integrated_tax: 29790.79
  sipa: 24286.58
  health: 30535.56
steps:
  - monthly_total: integrated_tax + sipa + health
  - unchanged_rate_twelve_months: monthly_total * 12
expected:
  monthly_total: 84612.93
  unchanged_rate_twelve_months: 1015355.16
```

### 2. Category A with health adherent or employment contribution exception?

Assume receipts ARS 5,000,000, all other parameters fit A, ordinary November table. An ordinary contributor with one adherent pays 5,585.77 + 18,246.86 + twice 25,694.55 = 75,221.73. If instead the individual proves concurrent employment and mandatory pension coverage satisfying Annex art. 40, federal payment for the covered self-employed activity can be integrated tax alone, 5,585.77, with health/contribution entitlement handled under the applicable other regime. The difference is 69,635.96; this is a factual status decision, not a free choice to omit contributions.

```oa-check
name: Category A component-status decision
inputs:
  integrated_tax: 5585.77
  sipa: 18246.86
  health: 25694.55
steps:
  - ordinary_one_adherent: integrated_tax + sipa + health * 2
  - proven_employment_exception: integrated_tax
  - difference: ordinary_one_adherent - proven_employment_exception
expected:
  ordinary_one_adherent: 75221.73
  proven_employment_exception: 5585.77
  difference: 69635.96
```

The earlier goods-I, exclusion and recategorisation examples remain as current decision cases: goods receipts ARS 85m with every parameter fitting I select I; services receipts ARS 130m exceed current K and trigger exit; a B taxpayer with receipts ARS 20m and all parameters fitting C reviews C at the next ordinary window. Those are assumed fact patterns, not claims that revenue overrides other parameters. Apply the source-period row and exclusion day in each case.

## Ask the client first

1. CUIT, registered activity/category, regime history, month being paid and recategorisation/registration dates.
2. All gross covered receipts for the relevant twelve months, invoices/credit notes, cash, processor and bank reconciliation.
3. Goods/services/mixed activity, premises/area, electricity, rent, unit goods prices, units and imports for resale.
4. Other employment/pension/professional-fund coverage, retirement law, health adherents and social/promoted/cooperative status.
5. Foreign transactions, export facts, currency/receipt dates and exchange-control evidence.
6. CCMA debt/payment history, notices, departure/exclusion facts and the actual statements/portal credential.

Working paper: retain A gross receipts and parameters; B category per parameter and final category; C each monthly component/exemption/adherent; D period-specific cost and payment reconciliation; plus documented flags. Record who must confirm a disputed point, the evidence, options and unresolved issue. Do not produce a filing-ready figure while an eligibility/category or source-period input is missing.

## Sources

| Source and portions read | Official URL | Read on |
|---|---|---|
| Read for current eligibility, category, exclusions and contribution exceptions: Ley 24.977 Annex arts. 2-9, 19-24, 39-40; quotation: "categoría que corresponda al mayor valor de sus parámetros" | https://biblioteca.arca.gob.ar/search/query/dcp/LEY_C_024977_1998_06_03 | 2026-11-11 |
| Read for implementation and activity definitions: Decreto 1/2010 related eligibility/category provisions; quotation: "ingresos provenientes de actividades económicas alcanzadas" | https://biblioteca.arca.gob.ar/search/query/dcp/DEC_C_000001_2010_01_04 | 2026-11-11 |
| Read for all August-current table rows and notes (*-****); quotation: "Valores de aplicación desde el 1/08/2026" | https://www.arca.gob.ar/monotributo/categorias.asp | 2026-11-11 |
| Read for January source-period identification and category/component table; quotation: "Vigentes desde el 01/08/2025 al 31/01/2026" | https://www.arca.gob.ar/monotributo/documentos/categorias/monotributo-categorias-agosto-2025-enero-2026.pdf | 2026-11-11 |
| Read for February-July source-period identification and category/component table; quotation: "Vigentes desde el 01/02/2026 al 31/07/2026" | https://www.arca.gob.ar/monotributo/documentos/categorias/monotributo-categorias-febrero-julio-2026.pdf | 2026-11-11 |
| Read for review/payment-period deadlines and portal process: ARCA recategorisation page; quotation: "hasta el día 5 de febrero o de agosto" | https://www.arca.gob.ar/monotributo/ayuda/recategorizacion.asp | 2026-11-11 |
| Read for payment channels, due date and CCMA: ARCA payments page; quotation: "exclusivamente medios electrónicos" | https://www.arca.gob.ar/monotributo/ayuda/pagos.asp | 2026-11-11 |
| Read for invoice types/point of sale: ARCA invoicing page; quotation: "comprobantes electrónicos tipo “C”" | https://www.arca.gob.ar/monotributo/ayuda/facturacion.asp | 2026-11-11 |
| Read for all exclusion triggers and appeal stages: ARCA exclusion page; quotation: "igual o más del 80%" | https://www.arca.gob.ar/monotributo/ayuda/exclusion.asp | 2026-11-11 |
| Read for renunciation/re-entry: ARCA renuncia page; quotation: "3 años calendario (enero a diciembre)" | https://www.arca.gob.ar/monotributo/ayuda/renuncia.asp | 2026-11-11 |
| Read for cancellation causes: official Monotributo cancellation procedure; quotation: "falta de pago de 10 períodos consecutivos" | https://www.argentina.gob.ar/servicio/darme-de-baja-en-el-monotributo | 2026-11-11 |

Not yet confirmed: current foreign-currency conversion/BCRA collection rules; detailed startup annualisation and activity-specific surface exceptions; bank-specific PDF/CSV export formats; exact live form fields and full mandatory invoice field list; 2026 penalties/interest, payment-plan eligibility and health/CUIT consequences of non-payment; any surviving separate annual information return; detailed general-regime transition benefits and historic re-entry-relief procedure. Special social/promoted/cooperative/unified provincial computations are outside this ordinary Guide. Old unsupported lower services ceiling, employee-count assumptions and approximate 2025 figures are replaced by the current verified rules above.
