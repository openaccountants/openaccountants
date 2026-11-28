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
version: 2.3
jurisdiction: AR
tax_year: 2026
last_updated: 2026-11-28
depends_on:
  - income-tax-workflow-base
category: international
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
tier: 2
domain: income-tax
type: situation-rules
---

# Argentina: Monotributo 2026 v2.3

> **General reference only.** This skill is general tax/accounting reference material for AI-assisted workflows. It has not been reviewed for any specific person's facts, documents, elections, deadlines, residency, filing status, or local procedures. Do not rely on it to file, pay, amend, or take a tax position without review by a qualified professional in the relevant jurisdiction.

## Who this applies to

Individuals carrying on eligible sales, leases, services, works and primary activities under the Annex to Ley 24.977 art. 2. The law includes qualifying worker-cooperative members and continuing estates, but not SA/SRL/SAS companies. A continuing estate may remain only until the end of the month in which the first of these occurs: the inheritance declaration, the validating will with the same purpose, or the first anniversary of death. Company direction/administration is outside eligible Monotributo activities. Do not treat a director's separate professional business as automatically the same activity.

**Quick answer:** establish the table period and all relevant trailing-period parameters, choose the category required by the highest applicable parameter, then add only the monthly components actually owed. Both services and goods can reach category K; the old services-only H ceiling is obsolete. Physical/rental parameters do not disappear merely because the person provides services; primary activities and services without fixed premises use the revenue-only exception in Annex art. 9 and decree art. 25. Missing inputs stop the calculation; do not assume zero employees or a convenient activity type.

The existing income-tax workflow base supports a category/payment reconciliation, evidence list and exception flags. Monotributo substitutes the national IVA/Ganancias and the specified contribution obligations for the covered activity; provincial gross-receipts obligations can remain, including unified collection where applicable. Use `argentina-income-tax.md`, `argentina-iva.md` and `ar-social-contributions.md` when the general regime applies.

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
| A | ARS 12,009,410.45 | Hasta 30 m² | Hasta 3330 kWh | ARS 2,792,886.15 | ARS 716,840.77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| B | ARS 17,595,182.74 | Hasta 45 m² | Hasta 5000 kWh | ARS 2,792,886.15 | ARS 716,840.77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| C | ARS 24,670,494.31 | Hasta 60 m² | Hasta 6700 kWh | ARS 3,816,944.41 | ARS 716,840.77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| D | ARS 30,628,651.43 | Hasta 85 m² | Hasta 10000 kWh | ARS 3,816,944.41 | ARS 716,840.77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| E | ARS 36,028,231.33 | Hasta 110 m² | Hasta 13000 kWh | ARS 4,841,002.66 | ARS 716,840.77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| F | ARS 45,151,659.41 | Hasta 150 m² | Hasta 16500 kWh | ARS 4,841,002.66 | ARS 716,840.77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| G | ARS 53,995,798.87 | Hasta 200 m² | Hasta 20000 kWh | ARS 5,771,964.69 | ARS 716,840.77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| H | ARS 81,924,660.37 | Hasta 200 m² | Hasta 20000 kWh | ARS 8,378,658.45 | ARS 716,840.77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| I | ARS 91,699,761.90 | Hasta 200 m² | Hasta 20000 kWh | ARS 8,378,658.45 | ARS 716,840.77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| J | ARS 105,012,519.20 | Hasta 200 m² | Hasta 20000 kWh | ARS 8,378,658.45 | ARS 716,840.77 | https://www.arca.gob.ar/monotributo/categorias.asp |
| K | ARS 126,610,838.75 | Hasta 200 m² | Hasta 20000 kWh | ARS 8,378,658.45 | ARS 716,840.77 | https://www.arca.gob.ar/monotributo/categorias.asp |

### Monthly components, from 1 August 2026

Services and goods have separate integrated-tax columns, not separate revenue ceilings. The full totals below assume ordinary pension and individual health contributions without adherents; test the exceptions before using them.

| Category | Integrated services | Integrated goods | SIPA | Individual health | Total services | Total goods | Official source |
|---|---|---|---|---|---|---|---|
| A | ARS 5,585.77 | ARS 5,585.77 | ARS 18,246.86 | ARS 25,694.55 | ARS 49,527.18 | ARS 49,527.18 | https://www.arca.gob.ar/monotributo/categorias.asp |
| B | ARS 10,612.98 | ARS 10,612.98 | ARS 20,071.55 | ARS 25,694.55 | ARS 56,379.08 | ARS 56,379.08 | https://www.arca.gob.ar/monotributo/categorias.asp |
| C | ARS 18,246.86 | ARS 16,757.32 | ARS 22,078.71 | ARS 25,694.55 | ARS 66,020.12 | ARS 64,530.58 | https://www.arca.gob.ar/monotributo/categorias.asp |
| D | ARS 29,790.79 | ARS 27,742.67 | ARS 24,286.58 | ARS 30,535.56 | ARS 84,612.93 | ARS 82,564.81 | https://www.arca.gob.ar/monotributo/categorias.asp |
| E | ARS 55,857.73 | ARS 44,313.79 | ARS 26,715.24 | ARS 37,238.48 | ARS 119,811.45 | ARS 108,267.51 | https://www.arca.gob.ar/monotributo/categorias.asp |
| F | ARS 78,573.20 | ARS 57,719.64 | ARS 29,386.76 | ARS 42,824.25 | ARS 150,784.21 | ARS 129,930.65 | https://www.arca.gob.ar/monotributo/categorias.asp |
| G | ARS 142,995.76 | ARS 71,497.87 | ARS 41,141.46 | ARS 46,175.72 | ARS 230,312.94 | ARS 158,815.05 | https://www.arca.gob.ar/monotributo/categorias.asp |
| H | ARS 409,623.31 | ARS 204,811.64 | ARS 57,598.04 | ARS 55,485.33 | ARS 522,706.68 | ARS 317,895.01 | https://www.arca.gob.ar/monotributo/categorias.asp |
| I | ARS 814,591.79 | ARS 325,836.71 | ARS 80,637.26 | ARS 68,518.81 | ARS 963,747.86 | ARS 474,992.78 | https://www.arca.gob.ar/monotributo/categorias.asp |
| J | ARS 977,510.14 | ARS 391,004.07 | ARS 112,892.16 | ARS 76,897.46 | ARS 1,167,299.76 | ARS 580,793.69 | https://www.arca.gob.ar/monotributo/categorias.asp |
| K | ARS 1,368,514.20 | ARS 456,171.40 | ARS 158,049.02 | ARS 87,882.82 | ARS 1,614,446.04 | ARS 702,103.24 | https://www.arca.gob.ar/monotributo/categorias.asp |

Under the source notes, the surface parameter is not considered in towns up to 40,000 inhabitants except ARCA-specified zones/activities. This exception concerns surface, not an automatic exemption from every parameter. An individual health amount covers no adherents; each additional adherent adds that same category health amount. Once elected, the additional payment remains obligatory until lawful removal or departure under decree art. 65. Example: category A with one adherent adds ARS 25,694.55 to the ordinary total, subject to actual health enrolment entitlement.

| Exception | Effect | Official source |
|---|---|---|
| Independent promoted worker, qualifying cooperative member/registered social-economy participant | Integrated-tax relief only as the applicable conditions provide; do not use the ordinary total blindly | Current table note (*); https://www.arca.gob.ar/monotributo/categorias.asp |
| Exclusive landlord of up to two properties, including relevant individual condo interests | Integrated-tax exemption under current table note; decree art. 30 requires exclusive immovable rental, no more than two properties including individual condominium interests, and registered contracts where required; legally noncomputable income does not defeat that exclusivity | Same |
| Exclusive primary tobacco/sugar-cane/yerba-mate/tea activity, receipts within D | Integrated-tax exception in table note; special regime facts required | Same |
| Mandatory coverage by another pension regime, under 18, covered movable/immovable rental activity, qualifying estate | Annex art. 40 exempts under-18s, qualifying provincial-professional pension-fund members and employees with actual national/provincial pension contributions; decree art. 62 requires exclusive movable/immovable rental, not mixed trading/rental; apply estate status under the table note | Same |
| Retired under pre-July-1994 laws | Pension and health exempt for the earlier statutory class; later Ley 24.241 retirees pay art. 39(a) SIPA only | Same |
| Retiree under either applicable pension-law group | No health contribution under note (***); do not infer pension exemption for later retirees | Same |

Read the statutory contribution exceptions under Annex arts. 39-40 alongside the table, especially employment with pension contributions and professional provincial funds. Mere possession of a health policy does not establish contribution exemption.

## The base

### Eligibility and category computation

Use [Ley 24.977 Annex arts. 2-9, 20-24 and 39-40](https://www.argentina.gob.ar/normativa/nacional/51609/actualizacion), current amended text, and [Decreto 1/2010](https://biblioteca.arca.gob.ar/search/query/dcp/DEC_C_000001_2010_01_04). Do not read an embedded historical H/I/L category table as current.

1. Confirm eligible person/activity and incompatibilities. Retaining IVA-registered status for another activity is incompatible (decree art. 1). Imports for resale disqualify; imported inputs to manufacture goods/provide services, and imported services used internally rather than resold, do not themselves do so (art. 8). Count income sources jointly: first each exploitation unit, then independent activities without units; no more than three in total (arts. 17, 27). Two shops plus two separate no-premises activities can therefore mean four sources. Space-based complementary/related activities and activity vehicles follow art. 17's definitions. Properly registered property contracts, where registration is required, group immovable rentals/condominiums as one unit; otherwise count each affected property/condominium.
2. Reconcile **accrued** gross activity income, not cash collections alone (decree art. 9). Match invoices, unpaid sales, collections of earlier invoices, cash, processors and exports; avoid counting the same sale twice. Annex art. 3 nets cancelled transactions and customary discounts. Ordinary business expenses do not reduce category gross income; reconcile processor net deposits to gross sales and fees. Decree arts. 1, 11-12 exclude public-office/employment earnings, national/provincial pensions, company direction/administration, financial/investment/securities/profit-participation income, and fixed-asset disposal where useful life exceeds two years and the asset was held at least twelve months from commissioning. Their own general-regime taxes can still apply. Non-excluded national taxes form part of receipts, subject to art. 10's tobacco/fuel-tax exceptions.
3. Identify the category required by each applicable parameter and choose the highest. Primary activities and services without fixed premises use gross income alone (Annex art. 9; decree art. 25). Otherwise test physical/rental limits. With multiple activities, aggregate covered accrued income and applicable physical parameters/rents (decree art. 6); the main activity for the integrated-tax column is the one with greatest gross income, not the lowest tax.
4. Measure electricity from bills whose due dates fall within the preceding twelve months and aggregate applicable units (decree art. 18). Sum activity-used surface, excluding unused areas (art. 19). Rent includes in-kind consideration and complements such as qualifying improvements, assumed property taxes and supplied accessories/services, and is aggregated across units (arts. 20-21). In a shared home use activity surface and proportionate rent; a single electricity meter has rebuttable activity-consumption presumptions of 20% for low consumption and 90% for high consumption (Annex art. 9). For simultaneous autonomous subdivided premises, art. 23 uses exclusive area, actual/proportionately assigned electricity and area-proportionate rent. For nonsimultaneous shared use, use full affected surface, electricity divided by number of users and each person's assumed rent obligation. Do not treat every shared site as a home allocation.
5. Apply startup rules separately. Annex art. 12 initially uses affected surface and agreed rent, or reasonable estimation if neither supplies a basis. After six months, annualise receipts, energy and accrued rent; payment effect is the second month after that period ends. Decree arts. 14-15 require a complete calendar semester and align annualisation with the semester recategorisation point; absent coincidence, initial category stays until first recategorisation. Critically, a projection over the maximum keeps the person in K until the next semester recategorisation under current art. 15; projection alone is not actual art. 20 exclusion. For late adhesion within the first twelve months, Annex art. 13 annualises pre-adhesion receipts/energy alongside surface/agreed rent; thereafter use actual preceding twelve months and accrued rent.
6. Determine integrated tax, SIPA and health separately, with proven exceptions/adherents. Exclusive immovable landlords' up-to-two-property integrated-tax exemption differs from exclusive movable/immovable landlords' personal-contribution exemption (decree arts. 30, 62). Condominium adhesion requires every income-attributed co-owner to adhere individually for all leases of that condominium, using their own parameter share (art. 5). Provincial professional-fund members may elect full voluntary contributions under art. 63. Keep provincial/unified charges separate and reconcile federal total to the credential and CCMA.
7. Review semester recategorisation and continuously monitor actual exclusion causes. Exceeding D while fitting E calls for category review; actual receipts above K or another art. 20 cause calls for exclusion, subject to the startup-projection distinction above. Monotributo does not discharge employer general-regime payroll/social-security/ART obligations for staff (Annex art. 38); its personal component table is not an employer payroll package. Route staff to `argentina-payroll.md` and `ar-social-contributions.md`.

### Bank-statement and platform reconciliation

The earlier pattern library is retained as an evidence workflow, not a statutory classifier. **CLIENT PAYMENT, TRANSFERENCIA, FACTURA C, Mercado Pago/Mercado Libre, PedidosYa/Rappi** and other platform deposits need invoice/gross-receipt matching. **TRANSFERENCIA PROPIA/AHORRO** can be excluded from revenue only after tracing both accounts. **DEVOLUCION/REINTEGRO** needs the original invoice/credit note. **SUBSIDIO/PLAN SOCIAL** and **INTERESES/PLAZO FIJO** must be classified under their actual legal nature; their labels alone do not justify inclusion/exclusion.

**PayPal, Wise, Payoneer or Stripe** does not prove foreign-source income or export: inspect customer, service/use, invoice and transaction facts. A qualifying export of services is business revenue and uses Factura E; do not assume every foreign receipt is an export or current exchange permission exists. Currency conversion and BCRA collection rules are referred until the applicable official rule is read.

On debits, match **MONOTRIBUTO/VEP/DEBITO AUTOMATICO** to CCMA period/component. Separate **IIBB/Ingresos Brutos** from the national payment; personal groceries/rent are not profit deductions against the fixed national fee. Expenses still matter for evidence, exclusion screening and other taxes. Bank PDF/CSV column names and export layouts must come from the actual statement, not a generic bank-format promise. Bank-specific formats, unproved subsidy classification and foreign-currency conversion/collection outputs are non-usable here. Check this point with one of our partner accountants.

### Exclusion conditions

[Current ARCA exclusion guidance](https://www.arca.gob.ar/monotributo/ayuda/exclusion.asp), reflecting Annex arts. 20-21, lists these ordinary triggers:

- Trailing twelve-month gross receipts exceed K, or relevant surface/electricity/rent exceeds the K limits.
- Unit goods cash price exceeds the maximum (decree art. 22 tests each offered/sold unit, not the whole invoice); imports of goods/services for subsequent commercialisation; more than three jointly counted sources under decree art. 27; services miscategorised as goods.
- Incompatible personal spending or duly adjusted bank deposits without justification; missing transaction invoices; qualifying REPSAL repeat-offender status.
- Activity purchases plus expenses over the preceding twelve months reach at least 80% of K maximum receipts for goods, or 40% for services/leases/works. This is an exclusion test against K, not a deduction allowance or percentage of the person's actual sales.

Annex art. 21 makes exclusion effective from zero hour of the day the cause occurs, requiring immediate communication and general-regime registrations. Do not wait for an ARCA notice or continue treating Monotributo payments as a cure. Integrated tax paid after the exclusion trigger becomes a general-tax payment on account under art. 21, subject to its implementing procedure. Trace the trigger day and hand off IVA, Ganancias and social security to the relevant Guides. A voluntary renunciation instead takes effect under its own next-month rule (Annex art. 19); keep it distinct from compulsory exclusion.

| Situation | Decision and source |
|---|---|
| Category B receipts now fit C, with all other parameters fitting C | Recategorisation, not automatic exit solely because B was exceeded; Annex art. 9 |
| Goods revenue fits I but affected premises require a higher category | Use the highest required category; no revenue-only shortcut; art. 9 |
| Services receipts fit I/J/K | These categories are available under current art. 8; the old H ceiling is not an exclusion |
| Revenue exceeds K or another art. 20 cause occurs | Exclusion and immediate general-regime handoff; arts. 20-21 |
| Several provincial/employment/retirement obligations | Determine federal component exceptions and separate local liabilities; arts. 39-40, table notes |
| Social/promoted/cooperative status, foreign-currency collection or disputed exclusion | Refer specialist issue and record evidence; do not fill a missing rule from a conservative guess |

## Deadlines and filing

[ARCA recategorisation guidance](https://www.arca.gob.ar/monotributo/ayuda/recategorizacion.asp) specifies the ordinary deadline **5 February and 5 August**, reviewing the preceding twelve months. Those staying in the same category or with under six months of activity take no action under the guidance. The resulting category applies from the second month after semester end under Annex art. 9. This replaces the old Guide's unsourced January/July-20 deadline. Errors/inexact values and recategorisation of office can have retroactive effects under decree art. 13; do not postpone correcting a past error until an ordinary window.

Enter the **Monotributo** portal with CUIT and Clave Fiscal and select **RECATEGORIZARME**. Reconcile the prefilled annual invoicing; the [official tutorial](https://www.arca.gob.ar/guias/paso-a-paso/Recategorizacion-monotributo.pdf) identifies **MIS INGRESOS NO COINCIDEN CON ESTE MONTO** for correcting it, then establishment/local-use information and **CONTINUAR**. Answer the provincial-activity screen where applicable, review the resulting category, use **VOLVER** to correct it or **CONFIRMAR**, and retain the success acknowledgement/new payment credential. Its older January/July availability and “following month” wording does not override the current deadline page and statutory February/August effective periods above. The display assists reconciliation; it does not establish unrecorded receipts or missing parameters. Exact live field numbering and any current use of the historical F.184 form reference are non-usable here. Check this point with one of our partner accountants.

[ARCA payment guidance](https://www.arca.gob.ar/monotributo/ayuda/pagos.asp) sets monthly payment by **the 20th**, rolled to the next business day when needed. Ordinary taxpayers of every category use electronic payment; in-person payment is reserved for the listed social/cooperative/promoted cases. Generate the appropriate VEP or use the available authorised electronic/debit route; reconcile payment in **Cuenta corriente de monotributistas y autónomos (CCMA)** by period, capital and interest. Save the receipt. Do not use the old ordinary Pago Fácil/Rapipago instruction without the specific exception.

[ARCA invoicing guidance](https://www.arca.gob.ar/monotributo/ayuda/facturacion.asp) identifies **C** documents for ordinary domestic transactions and **E** for exports. For domestic operations, [RG 4290 arts. 6-8](https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:4290%7Co:3%7Ca:2018%7Cf:02/08/2018) permits electronic originals or an authorised fiscal controller where the conditions allow, including both together; test the current electronic-only exceptions for the specified MiPyME credit-invoice operations and RG4291 Annex II operations, and the connectivity/contingency conditions. RG5893 extended the ordinary electronic/controller obligation to the social/promoted class from 1 November 2026; do not reuse its former manual-invoice exception as an ordinary method. Do not turn the guidance page's electronic route into a universal ban on permitted controllers. Different methods require their own point of sale. From **1 November 2026**, [RG 5893 arts. 3/5](https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:5893%7Co:9%7Ca:2026%7Cf:27/08/2026) provides that ARCA enables a missing electronic point for **Comprobantes en línea**, associated with **Factura en línea - Monotributo** and the declared fiscal address. To enable other points or modify/add their data, use **Administración de Puntos de Venta y Domicilios**. The general help page’s Registro Único Tributario instruction must be read with that newer operative rule. **Comprobantes en línea** supports invoice/credit/debit documents and later consultation. Retain issuer CUIT, transaction description/amount and authorisation data with the actual issued document; do not separately charge ordinary IVA as if a registered general-regime taxpayer. Exact current mandatory invoice fields beyond this are not asserted here.

For departure, use the portal's corresponding **baja por cese, renuncia or exclusión** path and retain the effective date. [ARCA renunciation guidance](https://www.arca.gob.ar/monotributo/ayuda/renuncia.asp) and exclusion guidance state the ordinary re-entry restriction, read with Annex arts. 19, 21 and decree art. 28: three full calendar years following the event year. For a November 2026 exclusion, or renunciation to obtain IVA-registered status for the same activity, those are 2027-2029, so earliest ordinary re-entry is 1 January 2030, subject to eligibility and the separate benefit-use wait. This is not a three-year bar on a genuine cessation: decree art. 35 allows new adhesion when eligible activity restarts, and art. 36 permits re-entry after administrative non-payment deregistration once the debt is regularised. Decree art. 37 also excepts a renunciation followed by cessation and new adhesion for a different activity, subject to the benefit-use wait. If general-regime transition benefits were used, also test the separate at-least-one-calendar-year wait from the end of the last fiscal period in which the full benefits could have been enjoyed; obtain the benefit-use history before deciding. Historic relief for specified post-1-January-2024 exclusions is a separate statutory exception, not a general 2026 waiver; its current filing route and any claimed individual relief are non-usable here. Check this point with one of our partner accountants.

## Penalties and interest

Check capital/interest in CCMA; no historic daily rate is supplied. Current penalty amounts, interest percentages and payment-plan eligibility are non-usable here. Check this point with one of our partner accountants. ARCA can recategorise or exclude using invoice, spending and bank information; absence of a notice does not keep an ineligible business in the regime.

For a systemic exclusion notice, ARCA's current guidance allows appeal within fifteen days through **Presentaciones Digitales**, **Exclusión de oficio del Monotributo - Apelación en término**. A fiscal inspection has the stated ten-day defence stage and then fifteen-day appeal against the resulting decision; use the actual notice/procedural calendar. Recategorisation of office likewise has a fifteen-day appeal route under its guidance. Do not invent a suspension of tax or payment obligations from an appeal alone. Exact day-count, late-remedy effect or suspension for an actual notice is non-usable here. Check this point with one of our partner accountants.

The old assertion that prolonged non-payment always suspends CUIT/health coverage is not established here. The official cancellation source identifies ten consecutive unpaid periods for administrative deregistration; health reinstatement, CUIT consequences and the original three-missed-month case are non-usable here without their applicable rules. Check this point with one of our partner accountants. **Mis Facilidades** eligibility and terms are not established here; do not treat a plan label as debt cancellation.

## Cross-border points

ARCA defines service exports as services performed in Argentina without employment dependency whose economic use is abroad. Eligible export business receipts enter the activity's gross-income analysis; receipt through a foreign platform does not remove them. C versus E depends on the actual operation. Source, treaty and exchange-control questions are separate; use `argentina-cross-border.md`. Actual source/treaty and BCRA collection/conversion outputs are non-usable here. Check this point with one of our partner accountants. Do not repeat the old assumption that any foreign payer creates foreign-source income or a universally applicable exchange rate.

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

### Original 2025 cases retained with their original inputs

The earlier approximate 2025 table does not establish a lawful category or fee. These five cases retain their original year and inputs; they are not replaced by the 2026 examples. Use the [January 2025 table](https://www.arca.gob.ar/monotributo/documentos/categorias/monotributo-categorias-agosto-2024-enero-2025-1.pdf), [February–July 2025 table](https://www.arca.gob.ar/monotributo/documentos/categorias/monotributo-categorias-febrero-julio-2025.pdf), or [August–December 2025 table](https://www.arca.gob.ar/monotributo/documentos/categorias/monotributo-categorias-agosto-2025-enero-2026.pdf) for the actual month.

1. **2025 consultant, ARS 5,000,000, services only:** revenue alone fits A in all three 2025 periods; the original D conclusion is unsupported. If every other applicable parameter fits A, ordinary contributions with no exception/adherents are 26,600.00 for January, 32,221.31 per month February–July and 37,085.74 per month August–December. If A actually applied throughout, the year’s ordinary federal cost is 405,356.56, before any separately proved benefit or provincial charge. Neither the original approximate 20,434 monthly/245,208 annual nor one current-month fee times twelve is the 2025 answer.
2. **2025 tutor, ARS 1,500,000:** revenue alone also fits A throughout 2025. With the same expressly established A/status conditions, the period-specific amounts and 405,356.56 weighted annual total above apply; the original approximate 13,989/167,868 figures do not.
3. **2025 retailer, ARS 12,000,000, premises80m², unit goods price50,000:** the price is below every 2025 unit maximum. If surface applies, 80m² requires at least D, not automatically I. If all remaining parameters fit D and ordinary individual contributions apply without adherents, the goods totals are 44,343.80 January, 53,714.87 February–July and 61,824.18 August–December. With D throughout, the weighted annual total is 675,753.92. Missing electricity, rent, municipality/exception or contribution facts prevent an actual final category/payment.
4. **2025 services freelancer, trailing receipts13,000,000:** revenue alone fits C in January and February–July, and B in August–December. It does not exceed K in any 2025 period, so the original H-ceiling exclusion is wrong; independently test all other exclusion causes and parameters.
5. **2025 taxpayer currently B, trailing receipts4,000,000:** revenue alone fits A throughout the year, not the original automatic C upgrade. Review the actual semester’s other parameters and effective category date before changing payment.

The earlier **2025 D taxpayer with eleven months’ receipts5,200,000 and one month remaining** still needs the remaining month, all parameters and source period. Those inputs alone neither compel E nor prove exclusion; apply the ordinary review and actual rolling exclusion tests, with the startup-projection exception separately where relevant. A filing amount for any missing-fact historical case is non-usable. Check this point with one of our partner accountants.

```oa-check
name: Original 2025 cases with period-weighted ordinary contributions
inputs:
  january_A: 26600.00
  february_july_A: 32221.31
  august_december_A: 37085.74
  january_goods_D: 44343.80
  february_july_goods_D: 53714.87
  august_december_goods_D: 61824.18
steps:
  - A_2025_if_A_all_year: january_A + 6 * february_july_A + 5 * august_december_A
  - goods_D_2025_if_D_all_year: january_goods_D + 6 * february_july_goods_D + 5 * august_december_goods_D
expected:
  A_2025_if_A_all_year: 405356.56
  goods_D_2025_if_D_all_year: 675753.92
```

## Ask the client first

1. CUIT, registered activity/category, regime history, month being paid and recategorisation/registration dates.
2. All gross covered receipts for the relevant twelve months, invoices/credit notes, cash, processor and bank reconciliation.
3. Goods/services/mixed activity, premises/area, electricity, rent, unit goods prices, units and imports for resale.
4. Other employment/pension/professional-fund coverage, retirement law, health adherents and social/promoted/cooperative status.
5. Foreign transactions, export facts, currency/receipt dates and exchange-control evidence.
6. Employees, employer/payroll registration, CCMA debt/payment history, notices, departure/exclusion facts, transition-benefit use and actual statements/portal credential.

Working paper: retain A gross receipts and parameters; B category per parameter and final category; C each monthly component/exemption/adherent; D period-specific cost and payment reconciliation; plus documented flags. Record who must confirm a disputed point, the evidence, options and unresolved issue. Do not produce a filing-ready figure while an eligibility/category or source-period input is missing.

## Sources

| Source and portions read | Official URL | Read on |
|---|---|---|
| Read for current eligibility, category, exclusions and contribution exceptions: Ley 24.977 Annex arts. 2-13, 19-24, 38-40; quotation: "categoría que corresponda al mayor valor de sus parámetros" | https://www.argentina.gob.ar/normativa/nacional/51609/actualizacion | 2026-11-28 |
| Read for implementation and activity definitions: Decreto 1/2010 current arts. 1, 5-6, 8-12, 14-15, 17-30, 62-65; quotation: "ingresos provenientes de actividades económicas alcanzadas" | https://biblioteca.arca.gob.ar/search/query/dcp/DEC_C_000001_2010_01_04 | 2026-11-28 |
| Read for all August-current table rows and notes (*-****); quotation: "Valores de aplicación desde el 1/08/2026" | https://www.arca.gob.ar/monotributo/categorias.asp | 2026-11-28 |
| Read for January source-period identification and category/component table; quotation: "Vigentes desde el 01/08/2025 al 31/01/2026" | https://www.arca.gob.ar/monotributo/documentos/categorias/monotributo-categorias-agosto-2025-enero-2026.pdf | 2026-11-28 |
| Read for February-July source-period identification and category/component table; quotation: "Vigentes desde el 01/02/2026 al 31/07/2026" | https://www.arca.gob.ar/monotributo/documentos/categorias/monotributo-categorias-febrero-julio-2026.pdf | 2026-11-28 |
| Read for review/payment-period deadlines and portal process: ARCA recategorisation page; quotation: "hasta el día 5 de febrero o de agosto" | https://www.arca.gob.ar/monotributo/ayuda/recategorizacion.asp | 2026-11-28 |
| Read for payment channels, due date and CCMA: ARCA payments page; quotation: "exclusivamente medios electrónicos" | https://www.arca.gob.ar/monotributo/ayuda/pagos.asp | 2026-11-28 |
| Read for invoice types/point of sale: ARCA invoicing page; quotation: "comprobantes electrónicos tipo “C”" | https://www.arca.gob.ar/monotributo/ayuda/facturacion.asp | 2026-11-28 |
| Read for current domestic invoicing modalities, exceptions and connectivity: RG 4290 arts. 6-8, as amended; quotation: "podrán optar por una de las DOS (2) modalidades" | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:4290%7Co:3%7Ca:2018%7Cf:02/08/2018 | 2026-11-28 |
| Read for all exclusion triggers and appeal stages: ARCA exclusion page; quotation: "igual o más del 80%" | https://www.arca.gob.ar/monotributo/ayuda/exclusion.asp | 2026-11-28 |
| Read for renunciation/re-entry: ARCA renuncia page; quotation: "3 años calendario (enero a diciembre)" | https://www.arca.gob.ar/monotributo/ayuda/renuncia.asp | 2026-11-28 |
| Read for cancellation causes/portal steps alongside decree arts35–37; quotation: "falta de pago de 10 períodos consecutivos" | https://www.argentina.gob.ar/servicio/darme-de-baja-en-el-monotributo | 2026-11-28 |

| Read for original 2025 numerical cases, A/B/C/D/K and unit/area limits, ordinary A/D components by source period | https://www.arca.gob.ar/monotributo/documentos/categorias/monotributo-categorias-agosto-2024-enero-2025-1.pdf and https://www.arca.gob.ar/monotributo/documentos/categorias/monotributo-categorias-febrero-julio-2025.pdf | 2026-11-28 |
| Read tutorial steps1–5 for actual portal labels, correction, confirmation and credential; its older timing instructions are not the current legal deadline | https://www.arca.gob.ar/guias/paso-a-paso/Recategorizacion-monotributo.pdf | 2026-11-28 |
| Read RG5893 arts2/3/5 for 1November2026 scope, automatic electronic point and point administration, alongside current RG4290 arts6–8/14 | https://biblioteca.arca.gob.ar/search/query/norma.aspx?p=t:RAG%7Cn:5893%7Co:9%7Ca:2026%7Cf:27/08/2026 | 2026-11-28 |
| Read service-export definition and E invoicing; no inference here about current exchange-control permission or conversion rate | https://www.arca.gob.ar/monotributo/exportacion-servicios/ | 2026-11-28 |

| Read Ley27743 art96 for historical one-off exclusion relief; actual current procedure/individual entitlement held | https://www.argentina.gob.ar/normativa/nacional/norma-401268/texto | 2026-11-28 |

Not yet confirmed: current foreign-currency conversion/BCRA collection rules; further administrative activity-specific parameter-exception lists; bank-specific PDF/CSV export formats; exact live form fields and full mandatory invoice field list; 2026 penalties/interest, payment-plan eligibility and health/CUIT consequences of non-payment; any surviving separate annual information return; detailed general-regime transition benefits and historic re-entry-relief procedure. Special social/promoted/cooperative/unified provincial computations are outside this ordinary Guide. Old unsupported lower services ceilings, employee-count defaults and approximate 2025 tables are not usable law; the original numerical cases and years are retained and corrected above. Special-regime computations, live form fields/F.184 mapping, separate annual information returns and any unproved administrative exception or transition outcome are non-usable here. Check this point with one of our partner accountants.
