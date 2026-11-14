---
name: mexico-iva
description: Use this skill whenever asked to prepare, review, or classify transactions for a Mexico IVA (Impuesto al Valor Agregado) return or classify transactions for Mexican VAT purposes. Trigger on phrases like "prepare IVA return", "Mexican VAT", "declaracion de IVA", "CFDI classification", "SAT filing", or any request involving Mexico value-added tax. Also trigger when classifying transactions from CFDI XML files, bank statements, or invoices for Mexican IVA purposes. This skill contains the complete Mexico IVA classification rules, CFDI 4.0 requirements, rate determination (16%/0%/exempt), border zone treatment, withholding rules, deductibility rules, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Mexico IVA-related work.
version: 2.2
jurisdiction: MX
tax_year: 2026
last_updated: 2026-11-14
type: situation-rules
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Mexico IVA

## Who this applies to

Self-employed personas fisicas and personas morales filing the monthly Mexican IVA declaration through the SAT Declaraciones y Pagos portal. Covers classifying bank-statement and CFDI transactions at 16%, the 0% rate or exempt, plus IVA withholding and crediting rules. IMMEX/maquiladora operations, consolidated groups and payroll sit outside this skill (see the refusal catalogue).


## Rates, bands and thresholds

Country: Mexico (Estados Unidos Mexicanos). Authority: Servicio de Administración Tributaria (SAT). Currency: MXN. Return: the monthly IVA declaration, filed in the Declaraciones y Pagos service on the SAT portal (https://www.sat.gob.mx). E-invoicing: CFDI 4.0 for every transaction. Primary legislation: Ley del Impuesto al Valor Agregado (LIVA), its Reglamento (RLIVA), Código Fiscal de la Federación (CFF) and Resolución Miscelánea Fiscal 2026 (RMF 2026). Tax year 2026.

| Item | Figure (2026) | Conditions | Source |
| --- | --- | --- | --- |
| Standard rate | 16% | All taxable acts and activities unless zero-rated or exempt (LIVA Art. 1: "la tasa del 16%") | [LIVA Art. 1 (SAT)](https://wwwmatnp.sat.gob.mx/articulo/19848/articulo-1) |
| Zero rate (tasa 0%) | 0% | Activities listed in LIVA Art. 2-A (unprocessed basic food, patent medicines, agricultural inputs, listed exports); input IVA is creditable; food prepared for consumption on the premises is taxed at 16%; processed pet food is outside the 0% list (Art. 2-A fr. I b) numeral 6) | [LIVA Art. 2-A (SAT)](https://wwwmatnp.sat.gob.mx/articulo/06071/articulo-2-a) |
| Exempt (exento) | No IVA, no credit | LIVA Arts. 9, 15, 20 and 25 (see 5.4) | same |
| Northern border region stimulus | Credit of 50% of the IVA, an effective 8% | Only taxpayers with the aviso filed and all decree conditions met; CFDI shows "IVA Crédito aplicado del 50%" (RMF 2026 rule 11.9.3); decree extended to 31 December 2026 | [DOF 31-12-2025 extension decree](https://dof.gob.mx/nota_detalle.php?codigo=5777697&fecha=31/12/2025); [RMF 2026 rule 11.9.3](https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf) |
| Retention by personas morales on fees and rent from personas físicas | Two thirds of the IVA transferred and effectively paid | RLIVA Art. 3 fr. I | [RLIVA Art. 3 fr. I, DOF 04-12-2006](https://dof.gob.mx/nota_detalle.php?codigo=4939297&fecha=04/12/2006) |
| Monthly payment deadline | Day 17 of the following month | Monthly declaration (LIVA Art. 5-D) | [LIVA Art. 5-D (SAT)](https://wwwmatnp.sat.gob.mx/articulo/73134/articulo-5-d) |
| Automobile investment cap carried into IVA credit | MXN 175,000 | LISR Art. 36 fr. II; LIVA Art. 5 fr. I ties credit to ISR deductibility | [LISR Art. 36 fr. II, DOF 18-11-2015](https://dof.gob.mx/nota_detalle.php?codigo=5415878&fecha=18/11/2015) |

**Read this whole section before classifying anything.**

- **CFDI 4.0 requirements** -- Every sale, purchase, and payment must be documented by a valid CFDI 4.0 containing: RFC of issuer and recipient, regimen fiscal of issuer, uso del CFDI code, forma de pago, metodo de pago (PUE or PPD), lugar de expedicion (ZIP), IVA trasladado and/or retenido shown separately, UUID assigned by PAC, and SAT digital seal. Input IVA is NOT creditable without a valid, non-cancelled CFDI showing the client's correct RFC.
- **Cash basis rule** -- Mexico IVA operates on a cash basis (flujo de efectivo) for most taxpayers. IVA is owed when payment is received, not when invoiced. IVA is creditable when payment is made, not when the CFDI is received. For PPD invoices, crediting requires the Complemento de Pago (REP) to be issued.

## The taxable base

**Return concepts (generic descriptions)**

The A/B/C/D codes below are internal worksheet labels used by this skill, not official SAT casillas. The official Declaraciones y Pagos form uses named fields; map by concept.

| Line | Meaning |
| --- | --- |
| A1 | Total value of activities at 16% |
| A2 | IVA charged at 16% (A1 x 0.16) |
| A3 | Total value of activities at 8% (border zone) |
| A4 | IVA charged at 8% (A3 x 0.08) |
| A5 | Total value of zero-rated activities |
| A6 | IVA at 0% (always zero) |
| A7 | Total value of exempt activities |
| A8 | Total value of all activities (A1+A3+A5+A7) |
| A9 | Total IVA causado (output IVA: A2+A4) |
| B1 | Input IVA at 16% (IVA acreditable) |
| B2 | Input IVA at 8% (border zone) |
| B3 | IVA on imports (from pedimento) |
| B4 | Total input IVA before proportion |
| B5 | Proportion factor (factor de acreditamiento) |
| B6 | Creditable IVA (B4 x B5, or B4 if 100% taxable) |
| C1 | IVA withheld by clients (IVA retenido por clientes) |
| C2 | IVA withheld from suppliers |
| D1 | IVA payable before credits (A9 - B6) |
| D2 | Less IVA withheld by clients (D1 - C1) |
| D3 | Less saldo a favor from prior periods |
| D4 | Amount payable (cantidad a cargo) or D5: saldo a favor |

**Conservative defaults -- Mexico-specific** (practice guidance set by this skill, not statutory rules)

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 16% |
| Unknown IVA status of a purchase | Not creditable |
| Unknown counterparty location | Domestic Mexico |
| Unknown B2B vs B2C status | B2C (no withholding) |
| Unknown business-use proportion (vehicle, phone, home office) | 0% recovery |
| Unknown whether CFDI exists | Not creditable (no CFDI = no credit) |
| Unknown border zone eligibility | Standard 16% (do not apply 8% without verification) |
| Unknown whether transaction is in scope | In scope at 16% |
| Unknown whether expense is strictly indispensable | Not creditable |
| Unknown IVA withholding obligation | No withholding (flag for reviewer) |

**Red flag thresholds** (practice guidance set by this skill, not statutory thresholds)

| Threshold | Value |
| --- | --- |
| HIGH single-transaction size | MXN 50,000 |
| HIGH tax-delta on a single conservative default | MXN 5,000 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net IVA position | MXN 100,000 |


Each rule states the legal source and the return line mapping. Apply silently if the data is unambiguous.

### 5.1 Standard rate 16% (LIVA Article 1)

- **Standard rate rule** -- Default rate for all taxable activities in Mexico unless zero-rated or exempt. Sales at 16%: Line A1 (net), A2 (IVA). Purchases at 16%: Line B1 (input IVA, if creditable).  _(LIVA Article 1)_

### 5.2 Border zone rate 8% (Decreto region fronteriza)

- **Border zone rate rule** -- Available ONLY when all conditions are met: tax domicile in qualifying border municipality, supply occurs physically in the zone, 18-month establishment requirement, aviso filed with SAT, not on EFOS blacklist. If ANY condition is unverified, apply 16%. The decree grants a credit of 50% of the IVA (CFDI value "IVA Crédito aplicado del 50%", RMF 2026 rule 11.9.3), an effective 8%. Sales at 8%: internal lines A3 (net), A4 (IVA). Purchases at 8%: internal line B2.  _(Decreto de Estimulos Fiscales Region Fronteriza Norte, DOF 31-12-2018, extended to 31 December 2026 by the decree of DOF 31-12-2025)_

### 5.3 Zero-rated activities 0% (Article 2-A LIVA)

- **Zero-rated activities rule** -- Basic foodstuffs (unprocessed), prescription medicines, agricultural inputs/services, exports of goods (with pedimento), exports of services (used/enjoyed abroad), books/newspapers, feminine hygiene products. Zero-rate allows FULL crediting of input IVA. Pet food is NOT zero-rated: processed food for dogs, cats and small pets is excluded from the 0% rate and pays 16% (LIVA Art. 2-A Fr. I b) numeral 6). Sales at 0%: internal line A5.  _(Article 2-A LIVA)_

### 5.4 Exempt activities (Articles 9, 15, 20, 25 LIVA)

- **Exempt activities rule** -- Sale of land (Art. 9 Fr. I) and of constructions destined or used for housing (Art. 9 Fr. II); used movable goods except those sold by businesses (Art. 9 Fr. IV); residential rental (Art. 20 Fr. II); and the services listed in Art. 15, including accredited education (Fr. IV), urban/suburban public land transport (Fr. V), agro-weather, housing-credit, financial-guarantee and life insurance plus agent commissions on those (Fr. IX), and services deriving from interest in authorized financing operations (Fr. X). Import exemptions sit in Art. 25. Professional medical services that require a medical degree and are provided by individuals (personas físicas), alone or through civil societies, are exempt (Art. 15 Fr. XIV); medical, hospital, radiology and laboratory services of public decentralised bodies are exempt under Fr. XV. Exempt = no IVA charged AND no input IVA credit on attributable costs.  _(Articles 9, 15, 20, 25 LIVA)_

### 5.5 CFDI requirements for input IVA crediting

- **CFDI requirements for crediting** -- Input IVA is creditable ONLY if: (1) valid CFDI 4.0 with UUID exists, (2) CFDI is in "Vigente" status (not cancelled), (3) client's RFC is shown correctly as receptor, (4) IVA is separately stated (trasladado), (5) payment has been made (cash basis), (6) for PPD invoices, REP (Complemento de Pago) has been issued. Missing any element = zero credit.

### 5.6 IVA withholding (retencion, Article 1-A LIVA)

- **IVA withholding rule** -- Personas morales that receive independent personal services or commission services from, or temporarily use goods of, personas fisicas must retain the IVA trasladado (LIVA Art. 1o.-A Fr. II a)); the retention is two thirds of the IVA effectively paid (RLIVA Art. 3 Fr. I). The former 6% subcontracting retention is repealed (LIVA Art. 1o.-A Fr. IV, derogada DOF 23-04-2021) -- do not apply it. Digital platforms operating as intermediaries retain 50% of the IVA charged to personas fisicas (LIVA Art. 18-J Fr. II a)); Mexican-resident digital intermediation platforms carry the same duties (Art. 1o.-A BIS). Withheld IVA is reported on the withheld-by-clients line and is creditable against IVA payable.  _(LIVA Art. 1o.-A; RLIVA Art. 3 Fr. I; LIVA Art. 18-J)_

### 5.7 Imported services

- **Imported services rule** -- Services received from non-residents without Mexican CFDI: IVA on import at 16% applies. Self-assessed by the Mexican taxpayer. Reported on Line B3. Creditable if service is strictly indispensable.

### 5.8 Proportional crediting (factor de acreditamiento, Art. 5 Fr. V)

- **Factor de acreditamiento formula** -- When the taxpayer performs BOTH taxable AND exempt activities: Factor = (value of taxable activities) / (total value of all activities). Apply factor to input IVA on shared/common expenses. Direct attribution first: costs directly for taxable = 100% credit; costs directly for exempt = 0% credit.  _(Art. 5 Fr. V)_

### 5.9 Blocked / non-creditable input IVA

- **Blocked / non-creditable input IVA rule** -- LIVA Art. 5 Fr. I limits credit to gastos estrictamente indispensables, defined as expenses deductible for ISR, so non-deductible expenses carry non-creditable IVA. Entertainment (gastos de representacion, non-deductible under LISR Art. 28 Fr. IV). Personal expenses. Expenses without valid CFDI. IVA not separately stated on the CFDI (LIVA Art. 5 Fr. II). Expenses related exclusively to exempt activities.

### 5.10 Vehicle rules (LISR Art. 36 Fr. II cross-reference)

- **Vehicle cap rules** -- Automobile investments are deductible only up to MXN 175,000 (LISR Art. 36 Fr. II, DOF 18-11-2015); a higher cap applies to automobiles propelled by rechargeable electric batteries and to hybrids (amount on the Not yet confirmed line). Because LIVA Art. 5 Fr. I ties IVA credit to ISR deductibility, input IVA on the vehicle follows the same cap. The cap does not apply to taxpayers whose activity is granting temporary use of automobiles, provided the vehicles are used exclusively for that activity.  _(LISR Art. 36 Fr. II; LIVA Art. 5 Fr. I)_

### 5.11 Cash basis timing

- **Cash basis timing rule** -- IVA causado (output): report in the month payment is received. IVA acreditable (input): credit in the month payment is made. For PPD invoices: credit only when REP is issued. For PUE invoices: credit in the month of the CFDI date (payment made at invoice time).

### 5.12 Saldo a favor (favorable balance)

- **Saldo a favor rule** -- When input IVA exceeds output IVA: the balance can be carried forward (acreditamiento) or refunded (solicitud de devolucion via FED portal). Refund requests trigger SAT review and may require additional documentation.

## Deadlines and filing

- IVA is declared monthly through Declaraciones y Pagos; for personas morales under the general regime the monthly declaration and payment are due on the 17th day of the month following the taxed month (SAT obligations page, Read on 2026-10-28).
- Timing is cash basis (LIVA Art. 4o. and 5o.): output IVA arises when consideration is effectively received; input IVA is creditable when consideration is effectively paid. CFDI "P" (paid) requires a "P" in the payment complement (REP); "PPD" requires the REP.
- IVA retained by clients is reported on the withheld-by-clients line of the taxpayer's monthly declaration; the retenedor pays it over with its own declaration (LIVA Art. 1o.-A, final paragraphs).
- Monthly saldo a favor carries forward, or a devolucion may be requested (LIVA Art. 6o.).

## Penalties and interest

Late or incorrect declarations attract CFF accesorios (updates and surcharges) on unpaid amounts, and fines for filing failures; errors are corrected by filing a complementary declaration. Specific CFF amounts are not reproduced here because the archived CFF text was not profiled for this skill.

## Cross-border points

- Imports of goods or services by Mexican businesses: IVA at 16% is paid at import or self-assessed; credit follows LIVA Art. 5o. (pedimento or D-1 in the importer's name).
- Foreign digital intermediation platforms: registration and 50% IVA retention duties under LIVA Arts. 18-B through 18-M, retention per Art. 18-J; Mexican-resident digital platforms carry the same duties (Art. 1o.-A BIS).
- Exports of goods and services are taxed at the 0% rate in the terms of LIVA Art. 2o.-A and Art. 29; keep the pedimento (goods) or proof the service is effectively used or enjoyed abroad (services).
- Temporary imports and IMMEX are out of scope (refusal R-MX-1).

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement (estado de cuenta) for the month in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Mexican bank: BBVA Bancomer, Banorte, Santander Mexico, Citibanamex, HSBC Mexico, Scotiabank Mexico, Banco Azteca, or any other. CFDI XMLs are strongly preferred for input IVA crediting.

**Recommended** -- CFDI XML files for all sales and purchases (or at minimum the monthly CFDI listing from SAT portal), prior month's declaracion showing saldo a favor carried forward, the client's RFC and constancia de situacion fiscal.

**Ideal** -- complete CFDI download from SAT portal (both emitidos and recibidos), estado de cuenta from all business bank accounts, prior month return filed, constancia de situacion fiscal showing regimen and obligations.

**Refusal policy if minimum is missing -- SOFT WARN.** If no bank statement and no CFDIs are available at all, hard stop. If bank statement only without CFDIs, proceed but record in the reviewer brief: "This IVA return was produced from bank statement alone. The reviewer must verify that all input IVA claims are supported by valid CFDI 4.0 documents and that the cash basis timing rule has been applied correctly."

### Mexico-specific refusal catalogue

- **R-MX-1 -- Maquiladora / IMMEX operations** -- Trigger: client operates under the IMMEX program or has maquiladora status. Message: "IMMEX/maquiladora operations have special IVA certification, virtual import/export, and temporary import rules that are outside this skill's scope. Escalate to a Contador Publico with IMMEX experience."
- **R-MX-2 -- Consolidated group filing** -- Trigger: client is part of a grupo empresarial filing consolidated returns. Message: "Consolidated group IVA structures are outside this skill's scope. Escalate to a licensed tax practitioner."
- **R-MX-3 -- Transfer pricing IVA implications** -- Trigger: intercompany transactions with related parties where pricing affects IVA base. Message: "Transfer pricing adjustments affecting the IVA base require specialist analysis. Escalate."
- **R-MX-4 -- EFOS/EDOS blacklist** -- Trigger: client's RFC or a major supplier's RFC appears on SAT's Article 69-B blacklist (Empresas Facturadoras de Operaciones Simuladas). Message: "One or more RFCs involved in these transactions may be on the EFOS/EDOS blacklist. All CFDIs from blacklisted suppliers are presumed false and non-creditable. Escalate to a Contador Publico immediately."
- **R-MX-5 -- Income tax return instead of IVA** -- Trigger: user asks about annual income tax return (declaracion anual ISR), not the monthly IVA. Message: "This skill only handles the monthly IVA return. For Mexico income tax (ISR), use the appropriate income tax skill."
- **R-MX-6 -- Payroll (nomina) processing** -- Trigger: user asks about CFDI de nomina, IMSS, INFONAVIT, or payroll obligations. Message: "Payroll is outside the scope of the IVA return. Use a payroll-specific skill."

## Section 3 -- Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement or CFDI. If multiple patterns match, use the most specific.

### 3.1 Mexican banks (fees exempt -- exclude)

**Mexican banks table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| BBVA BANCOMER, BBVA MEXICO | EXCLUDE for bank charges/fees/comisiones (flag general account fees) | Art. 15 Fr. X exempts services deriving from interest, including commissions of credit institutions in authorized financing operations; general account fees are not squarely covered -- verify CFDI treatment |
| BANORTE, BANCO MERCANTIL DEL NORTE | EXCLUDE for bank charges/fees | Same |
| SANTANDER MX, SANTANDER MEXICO, BANCO SANTANDER | EXCLUDE for bank charges/fees | Same |
| CITIBANAMEX, BANAMEX | EXCLUDE for bank charges/fees | Same |
| HSBC MEXICO | EXCLUDE for bank charges/fees | Same |
| SCOTIABANK MEXICO | EXCLUDE for bank charges/fees | Same |
| BANCO AZTECA | EXCLUDE for bank charges/fees | Same |
| BANREGIO, BANBAJIO, BANCO DEL BAJIO | EXCLUDE for bank charges/fees | Same |
| INTERESES, INTERES, RDTO | EXCLUDE | Interest income/expense, exempt |
| CREDITO, PRESTAMO, LOAN | EXCLUDE | Loan principal movement, out of scope |
| COMISION BANCARIA, ANUALIDAD TARJETA | EXCLUDE for commissions tied to interest-bearing financing; flag the rest | Art. 15 Fr. X covers commissions of credit institutions in financing operations; card annuities -- verify CFDI treatment |

### 3.2 Mexican government, regulators, and statutory bodies (exclude entirely)

**Government bodies table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SAT, SERVICIO DE ADMINISTRACION TRIBUTARIA | EXCLUDE | Tax payment, not a supply |
| DECLARACION, PAGO DE IMPUESTOS | EXCLUDE | Tax payment |
| IMSS, SEGURO SOCIAL | EXCLUDE | Social security contribution, not IVA |
| INFONAVIT | EXCLUDE | Housing fund contribution, not IVA |
| AFORE, PENSIONES | EXCLUDE | Pension fund, out of scope |
| GOBIERNO, SECRETARIA, AYUNTAMIENTO | EXCLUDE | Government fees, sovereign acts |
| MUNICIPIO, PREDIAL, TENENCIA | EXCLUDE | Property/vehicle tax, not a supply |
| TRAMITE, LICENCIA GOBIERNO | EXCLUDE | Government licence, sovereign act |

### 3.3 Mexican utilities

**Utilities table**

| Pattern | Treatment | Line | Notes |
| --- | --- | --- | --- |
| CFE, COMISION FEDERAL DE ELECTRICIDAD | Domestic 16% | B1 (input) | Electricity -- deductible overhead, CFDI issued |
| TELMEX, TELEFONOS DE MEXICO | Domestic 16% | B1 (input) | Telecoms -- deductible overhead |
| TELCEL, AT&T MEXICO, MOVISTAR | Domestic 16% | B1 (input) | Mobile telecoms -- confirm business use |
| IZZI, TOTALPLAY, MEGACABLE | Domestic 16% | B1 (input) | Internet/cable -- deductible if business |
| AGUA, SAPAS, SIAPA, SACMEX | EXCLUDE or exempt |  | Water -- many municipal water services are exempt |
| GAS NATURAL, NATURGY, GAS LP | Domestic 16% | B1 (input) | Gas supply, standard rated |

### 3.4 Fuel and petroleum (Pemex and others)

**Fuel and petroleum table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PEMEX, GASOLINERA, ESTACION DE SERVICIO | Domestic 16% | Fuel -- creditable if business vehicle with valid CFDI. Vehicle cap rules apply (MXN 175,000 / MXN 250,000 for electric). Flag if personal vehicle. |
| GASOLINA, DIESEL, COMBUSTIBLE | Domestic 16% | Same treatment as above |
| CASETA, PEAJE, CAPUFE | Domestic 16% | Toll roads -- creditable with CFDI. Some tolls issue simplified CFDI. |

### 3.5 Insurance (exempt -- exclude)

**Insurance table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GNP, GRUPO NACIONAL PROVINCIAL | EXCLUDE for qualifying policies (flag others) | Art. 15 Fr. IX exempts only agro-weather insurance, housing-credit insurance, financial-guarantee insurance, life insurance, and agent commissions on those; other premiums need review |
| AXA SEGUROS, MAPFRE MEXICO | EXCLUDE | Same |
| METLIFE, SEGUROS MONTERREY | EXCLUDE | Same |
| QUALITAS, HDI SEGUROS | EXCLUDE | Same |
| SEGUROS, POLIZA, PRIMA DE SEGURO | EXCLUDE for Art. 15 Fr. IX categories; flag the rest | Only agro-weather, housing-credit, financial-guarantee and life insurance are exempt |

### 3.6 Major Mexican retailers and e-commerce

**Retailers table**

| Pattern | Treatment | Line | Notes |
| --- | --- | --- | --- |
| WALMART MEXICO, WALMEX, BODEGA AURRERA | Domestic 16% | B1 (input) | General merchandise -- creditable if business expense with valid CFDI. Food items may be 0% on CFDI. |
| COSTCO MEXICO | Domestic 16% | B1 (input) | Same. Check CFDI for mixed rates. |
| AMAZON MX, AMAZON MEXICO | Domestic 16% | B1 (input) | Check billing entity -- Amazon Mexico S. de R.L. de C.V. issues Mexican CFDI at 16%. |
| MERCADO LIBRE, MERCADOPAGO | Domestic 16% | B1 (input) | Mexican entity. Transaction fees may be exempt financial service -- check CFDI. |
| OFFICE DEPOT, STAPLES MEXICO | Domestic 16% | B1 (input) | Office supplies, standard rated |
| HOME DEPOT MEXICO | Domestic 16% | B1 (input) | Construction/maintenance supplies |
| LIVERPOOL, PALACIO DE HIERRO | Domestic 16% | B1 (input) | Department store -- confirm business purpose |
| SORIANA, CHEDRAUI, LA COMER | Domestic 16% | B1 (input) | Supermarket -- food items may appear at 0% on CFDI |

### 3.7 Transport and ride-hailing

**Transport table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| UBER MX, UBER MEXICO, UBER TRIP | Domestic 16% with withholding | Uber Mexico issues CFDI. The platform withholds 50% of the IVA charged to persona fisica drivers (LIVA Art. 18-J Fr. II a); Mexican-resident digital intermediation platforms carry the same duties (Art. 1o.-A BIS). For the rider: input IVA creditable with CFDI. |
| DIDI, DIDI MEXICO | Domestic 16% with withholding | Same as Uber |
| BEAT, CABIFY MEXICO | Domestic 16% | Same treatment |
| VOLARIS, AEROMEXICO, VIVA AEROBUS | Domestic 16% or 0% (international) | Domestic flights at 16%. International flights: check if 0% (export of service). |
| ADO, PRIMERA PLUS, ETN | Domestic 16% | Intercity bus -- standard rated (urban public transport is exempt) |
| METROBUS, METRO, TRANSPORTE PUBLICO | EXCLUDE or exempt | Urban/suburban public transport exempt (Art. 15 Fr. V) |

### 3.8 SaaS and digital services -- foreign suppliers

**SaaS table**

| Pattern | Billing entity | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE (Ads, Workspace, Cloud) | Google Mexico S. de R.L. de C.V. or Google LLC | If Mexican CFDI: domestic 16%. If no CFDI: imported service, IVA on import applies. | Check CFDI. Google registered in Mexico issues CFDI. |
| MICROSOFT (365, Azure) | Microsoft Mexico or Microsoft Corp | Same -- check billing entity on CFDI |  |
| ADOBE | Adobe Systems Mexico or Adobe Inc (US) | Same |  |
| META, FACEBOOK ADS | Meta Platforms Mexico or Meta (US/IE) | If Mexican entity with CFDI: 16%. If foreign: imported digital service. |  |
| AMAZON WEB SERVICES, AWS | Amazon Web Services Mexico or AWS Inc | Check CFDI entity |  |
| ZOOM | Zoom Video Communications | If no Mexican entity: imported service |  |
| SLACK, ATLASSIAN, NOTION | Various (US entities) | Imported service -- no CFDI. IVA self-assessed on import. |  |
| SPOTIFY, NETFLIX, APPLE | Mexican-registered for B2C digital services | These platforms now collect and remit IVA in Mexico for B2C digital services under Art. 18-B to 18-M LIVA. B2B: check if CFDI issued. |  |

### 3.9 Payment processors

**Payment processors table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| STRIPE (transaction fees) | EXCLUDE (exempt) or imported service | If billed from US entity without CFDI: imported financial service. Transaction fees may be exempt. |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | PayPal Mexico issues CFDI for certain services. Transaction commissions are financial services (exempt). |
| MERCADOPAGO (transaction fees) | EXCLUDE (exempt) | Payment processing commission -- exempt financial service |
| CONEKTA, OPENPAY, SR PAGO | Domestic 16% | Mexican payment processors -- check CFDI for service fees vs. transaction fees |
| CLIP, IZETTLE | Domestic 16% | POS terminal services |

### 3.10 Professional services (Mexico)

**Professional services table**

| Pattern | Treatment | Line | Notes |
| --- | --- | --- | --- |
| NOTARIO, NOTARIA, FE PUBLICA | Domestic 16% | B1 (input) | Notarial services, standard rated |
| CONTADOR, CONTABILIDAD, DESPACHO CONTABLE | Domestic 16% | B1 (input) | Accounting/bookkeeping, always deductible |
| ABOGADO, BUFETE, DESPACHO JURIDICO | Domestic 16% | B1 (input) | Legal services, deductible if business matter |
| CONSULTORIA, ASESORIA | Domestic 16% | B1 (input) | Consulting, standard rated |

### 3.11 Payroll and social security (exclude entirely)

**Payroll table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| NOMINA, SUELDO, SALARIO | EXCLUDE | Wages -- outside IVA scope |
| IMSS, SEGURO SOCIAL | EXCLUDE | Social security contribution |
| INFONAVIT | EXCLUDE | Housing fund |
| PTU, REPARTO DE UTILIDADES | EXCLUDE | Profit sharing, out of scope |
| AGUINALDO, VACACIONES | EXCLUDE | Year-end bonus, vacation pay -- out of scope |
| SAR, AFORE | EXCLUDE | Retirement contributions |

### 3.12 Internal transfers and exclusions

**Internal transfers table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRASPASO, TRANSFERENCIA PROPIA | EXCLUDE | Internal account movement |
| RETIRO, CAJERO, ATM | Ask | Cash withdrawal -- ask what cash was spent on |
| DIVIDENDO | EXCLUDE | Dividend, out of scope |
| PRESTAMO PERSONAL, DISPOSICION | EXCLUDE | Loan drawdown, out of scope |

## Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of a Mexico-based self-employed software consultant (persona fisica, Actividades Empresariales y Profesionales regime). They illustrate the trickiest cases.

### Worked example 1: Standard domestic sale with CFDI

**Input line:**
`05.04.2026 ; EMPRESA TECH SA DE CV ; CREDIT ; Factura FE-2026-041 Consultoria abril ; MXN 116,000.00`

**Reasoning:**
Client issued CFDI tipo I (ingreso) for MXN 100,000 + IVA MXN 16,000. Payment received in April. Cash basis: IVA causado in April. Activities at 16% = MXN 100,000. Output IVA = MXN 16,000.

```oa-check
name: Standard 16% sale (Example 1)
inputs:
  net: 100000
steps:
  - iva: net * 0.16
  - gross: net + iva
expected:
  iva: 16000.00
  gross: 116000.00
```

**Example 1 output table**  _(--)_

| Date | Counterparty | Gross | Net | IVA | Rate | Line | Default? | Question? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 05.04.2026 | EMPRESA TECH SA DE CV | +116,000 | +100,000 | +16,000 | 16% | A1/A2 | N | -- |

### Worked example 2: IVA withholding by client (persona moral paying persona fisica)

**Input line:**
`10.04.2026 ; CORPORATIVO DELTA SA DE CV ; CREDIT ; Pago factura consultoria ; MXN 105,333.33`

**Reasoning:**
Client invoiced MXN 100,000 + IVA MXN 16,000 = MXN 116,000. The corporate client (persona moral) withheld 2/3 of the IVA (MXN 10,666.67): LIVA Art. 1o.-A Fr. II a) obliges the retention on independent personal services from personas fisicas, and RLIVA Art. 3 Fr. I sets it at dos terceras partes. It also withheld 10% ISR (MXN 10,000, LISR Art. 106). Net deposit = MXN 116,000 - MXN 10,666.67 = MXN 105,333.33 (ISR withheld is separate). Report full IVA causado MXN 16,000 on the 16% output line and IVA retenido MXN 10,666.67 on the withheld-by-clients line.

```oa-check
name: Persona moral withholds 2/3 IVA (Example 2)
inputs:
  fee: 100000
steps:
  - iva: fee * 0.16
  - retenido: round(iva * 2 / 3, 2)
  - isr: round(fee * 0.10, 2)
  - net: fee + iva - retenido
expected:
  iva: 16000.00
  retenido: 10666.67
  isr: 10000.00
  net: 105333.33
```

**Example 2 output table**  _(Verify CFDI shows retencion)_

| Date | Counterparty | Gross | Net | IVA causado | IVA retenido | Rate | Lines | Default? | Question? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 10.04.2026 | CORPORATIVO DELTA SA DE CV | +105,333.33 | +100,000 | +16,000 | -10,666.67 | 16% | A1/A2/C1 | N | Verify CFDI shows retencion |

### Worked example 3: Imported digital service (no Mexican CFDI)

**Input line:**
`15.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 15.00 ; MXN 270.00`

**Reasoning:**
Notion Labs Inc is a US entity. No Mexican CFDI issued. This is an importation of services under Art. 24 LIVA. The Mexican taxpayer must self-assess IVA at 16% on the value. IVA on import = MXN 270 x 0.16 = MXN 43.20. This import IVA is creditable on the imports line if the service is strictly indispensable for the business.

```oa-check
name: Self-assessed IVA on imported service (Example 3)
inputs:
  mxn_value: 270
steps:
  - iva_import: mxn_value * 0.16
expected:
  iva_import: 43.20
```

**Example 3 output table**  _(Verify service is business use)_

| Date | Counterparty | Gross | Net | IVA import | Rate | Line | Default? | Question? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 15.04.2026 | NOTION LABS INC | -270.00 | -270.00 | 43.20 | 16% | B3 (import) | N | Verify service is business use |

### Worked example 4: Entertainment, non-creditable

**Input line:**
`18.04.2026 ; RESTAURANTE LA HACIENDA ; DEBIT ; Comida con cliente ; MXN 2,500.00`

**Reasoning:**
Restaurant meal with a client. Gastos de representacion are non-deductible for ISR under LISR Art. 28 Fr. IV. LIVA Art. 5 Fr. I makes input IVA creditable only for gastos estrictamente indispensables, defined as expenses deductible for ISR, so IVA on non-deductible entertainment is not creditable. Default: block IVA credit.

**Example 4 output table**  _("Entertainment: IVA not creditable")_

| Date | Counterparty | Gross | Net | IVA | Rate | Line | Default? | Question? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 18.04.2026 | RESTAURANTE LA HACIENDA | -2,500.00 | -2,155.17 | 0 | -- | -- | Y | "Entertainment: IVA not creditable" |

### Worked example 5: Zero-rated sale (export of services)

**Input line:**
`22.04.2026 ; ACME CORP (US) ; CREDIT ; Invoice MX-2026-012 Software development ; USD 5,000.00 ; MXN 90,000.00`

**Reasoning:**
Software development services exported to US client. Service effectively used/enjoyed abroad. Zero-rated under Art. 2-A Fr. IV / Art. 29 LIVA. Line A5 = MXN 90,000. IVA = 0%. Input IVA on related expenses remains fully creditable (advantage of 0% over exempt).

**Example 5 output table**  _(Verify service used/enjoyed abroad)_

| Date | Counterparty | Gross | Net | IVA | Rate | Line | Default? | Question? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 22.04.2026 | ACME CORP (US) | +90,000 | +90,000 | 0 | 0% | A5 | Y | Verify service used/enjoyed abroad |

### Worked example 6: Vehicle fuel with CFDI, cap consideration

**Input line:**
`28.04.2026 ; GASOLINERA PEMEX EST 1234 ; DEBIT ; Carga gasolina ; MXN 1,200.00`

**Reasoning:**
Fuel purchase at Pemex station. If business vehicle and valid CFDI exists: IVA creditable. IVA = MXN 1,200 / 1.16 x 0.16 = MXN 165.52 (net MXN 1,034.48). However, vehicle cap rules apply: if the vehicle purchase price exceeded MXN 175,000, only proportional IVA on running costs is creditable. Default: block unless vehicle and CFDI confirmed.

```oa-check
name: IVA inside MXN 1,200 gross fuel purchase (Example 6)
inputs:
  gross: 1200
steps:
  - iva: round(gross / 1.16 * 0.16, 2)
  - net: round(gross - gross / 1.16 * 0.16, 2)
expected:
  iva: 165.52
  net: 1034.48
```

**Example 6 output table**  _("Vehicle: confirm business use and CFDI")_

| Date | Counterparty | Gross | Net | IVA | Rate | Line | Default? | Question? |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 28.04.2026 | GASOLINERA PEMEX EST 1234 | -1,200.00 | -1,034.48 | 0 | -- | -- | Y | "Vehicle: confirm business use and CFDI" |


## Section 6 -- Tier 2 catalogue (compressed)

### 6.1 Border zone rate eligibility

- **Border zone rate eligibility** -- Pattern: client claims 8% rate. Why insufficient: requires verification of all six conditions (domicile, physical supply, 18-month establishment, aviso filed, not on EFOS, payroll requirements). Default: 16%. Question: "Have you filed the aviso with SAT and do you meet all conditions for the border zone stimulus?"

### 6.2 Restaurants and entertainment

- **Restaurants and entertainment** -- Pattern: restaurant, bar, entertainment venue. Why insufficient: gastos de representacion are non-deductible under LISR Art. 28 Fr. IV, and LIVA Art. 5 Fr. I makes only ISR-deductible expenses creditable, so the IVA is generally non-creditable. Default: block IVA credit. Question: "Was this a business meal or entertainment? (Note: entertainment IVA is generally not creditable.)"

### 6.3 Mixed activities -- proportional crediting

- **Mixed activities proportional crediting** -- Pattern: client has both taxable and exempt revenue. Why insufficient: requires annual factor calculation and direct attribution analysis. Default: apply factor based on available period data; flag for year-end adjustment. Question: "What proportion of your revenue is from taxable vs exempt activities?"

### 6.4 Vehicle business use

- **Vehicle business use** -- Pattern: fuel, car maintenance, vehicle lease. Why insufficient: business vs personal use and vehicle value unknown. Default: 0% recovery (practice default set by this skill, not a statutory rule). Question: "Is this a business vehicle? What was the purchase price? Is there a valid CFDI?"

### 6.5 IVA withholding classification

- **IVA withholding classification** -- Pattern: payment to persona fisica for services. Why insufficient: need to confirm the counterparty is persona fisica and the service type. Default: no withholding (flag for reviewer). Question: "Is the service provider a persona fisica or persona moral? What service is being provided?"

### 6.6 Export of services -- place of enjoyment

- **Export of services place of enjoyment** -- Pattern: service income from foreign client. Why insufficient: zero-rating requires that the service is "effectively used or enjoyed abroad" (Art. 29 Fr. IV LIVA) -- strict interpretation by SAT. Default: 16% (conservative). Question: "Where is this service effectively used or enjoyed? Can you document that the benefit occurs outside Mexico?"  _(Art. 29 Fr. IV LIVA)_

### 6.7 Round-number incoming transfers

- **Round-number incoming transfers** -- Pattern: large round credit from owner-named or personal counterparty. Default: exclude as owner injection. Question: "Is this a customer payment, your own money, or a loan?"

### 6.8 Ambiguous SaaS billing entity

- **Ambiguous SaaS billing entity** -- Pattern: Google, Microsoft, Adobe, Meta where the billing entity is unclear. Default: assume no CFDI exists, treat as imported service with IVA self-assessment at 16%. Question: "Does the provider issue a Mexican CFDI? What entity name and RFC appear on the invoice?"

### 6.9 Cash withdrawals

- **Cash withdrawals** -- Pattern: ATM, retiro efectivo, cajero. Default: exclude as personal drawing. Question: "What was the cash used for?"

### 6.10 PPD invoices without REP

- **PPD invoices without REP** -- Pattern: purchase where CFDI shows MetodoPago = PPD but no REP has been received. Default: IVA NOT creditable until REP is issued. Question: "Has the supplier issued a Complemento de Pago (REP) for this payment?"

## Section 7 -- Excel working paper template (Mexico-specific)

### Sheet "Transactions"

Columns: A (Date), B (Counterparty/RFC), C (CFDI UUID), D (Gross MXN), E (Net MXN), F (IVA trasladado), G (IVA retenido), H (Rate), I (Line code), J (Default Y/N), K (Question), L (Notes).

Column C (UUID) is critical in Mexico -- it links every transaction to its CFDI. If UUID is blank, input IVA is not creditable.

### Sheet "Return Summary"

A/B/C/D codes below are internal worksheet labels, not official SAT casillas.

**Return Summary template**

```
Output IVA:
| A1 | Activities at 16% (net) | =SUMIFS(Transactions!E:E, Transactions!I:I, "A1") |
| A2 | IVA at 16% | =A1*0.16 |
| A3 | Activities at 8% (net) | =SUMIFS(Transactions!E:E, Transactions!I:I, "A3") |
| A4 | IVA at 8% | =A3*0.08 |
| A5 | Zero-rated activities | =SUMIFS(Transactions!E:E, Transactions!I:I, "A5") |
| A7 | Exempt activities | =SUMIFS(Transactions!E:E, Transactions!I:I, "A7") |
| A8 | Total activities | =A1+A3+A5+A7 |
| A9 | Total IVA causado | =A2+A4 |

Input IVA:
| B1 | Input IVA 16% | =SUMIFS(Transactions!F:F, Transactions!I:I, "B1") |
| B2 | Input IVA 8% | =SUMIFS(Transactions!F:F, Transactions!I:I, "B2") |
| B3 | IVA on imports | =SUMIFS(Transactions!F:F, Transactions!I:I, "B3") |
| B4 | Total input IVA | =B1+B2+B3 |
| B6 | Creditable IVA | =B4*B5 or =B4 |

Withholdings:
| C1 | IVA withheld by clients | =SUMIFS(Transactions!G:G, Transactions!I:I, "C1") |

Final:
| D1 | IVA payable before credits | =A9-B6 |
| D2 | Less IVA withheld | =D1-C1 |
| D3 | Less saldo a favor prior | [manual entry] |
| D4 | Amount payable | =MAX(D2-D3, 0) |
| D5 | Saldo a favor | =MAX(-(D2-D3), 0) |
```

### Color and formatting conventions

Blue for hardcoded values from bank statement/CFDI data. Black for formulas. Green for cross-sheet references. Yellow background for any row where Default = "Y". Red background for any row where UUID is blank and IVA credit was attempted.

## Section 8 -- Mexican bank statement reading guide (estado de cuenta)

**Estado de cuenta format conventions.** Mexican banks (BBVA Bancomer, Banorte, Santander, Citibanamex) typically export statements in PDF with DD/MM/YYYY or DD-MMM-YYYY date formats. CSV exports use comma or pipe delimiters. Common columns: Fecha, Descripcion/Concepto, Cargo (debit), Abono (credit), Saldo. Some banks include Referencia (reference number) and Movimiento (transaction type: SPEI, transferencia, cargo automatico, domiciliacion).

**SPEI transfers.** Most business payments in Mexico use SPEI (Sistema de Pagos Electronicos Interbancarios). The description often includes the beneficiary name, CLABE (18-digit interbank account number), and a reference. Match the beneficiary name against Section 3.

**Domiciliaciones.** Recurring direct debits (domiciliaciones) appear with the service provider name: CFE, TELMEX, insurance companies. These are pre-authorized charges.

**Card charges.** Credit/debit card charges appear with merchant names, often abbreviated. AMZN = Amazon, UBER = Uber, GGLE = Google, MSFT = Microsoft, FCBK = Facebook/Meta. Map abbreviations to full names before matching Section 3.

**Internal transfers and exclusions.** Transfers between the client's own accounts (BBVA to BBVA, or to another bank). Labelled "traspaso", "transferencia propia", "movimiento entre cuentas". Always exclude.

**Owner draws (retiros personales).** Self-employed individuals (persona fisica) withdrawing cash or transferring to personal accounts. Labelled "retiro", "disposicion", "transferencia a cuenta personal". Exclude as personal drawings.

**IVA withholding entries.** When a persona moral client pays the freelancer, the bank statement shows the net amount after IVA and ISR withholdings. The gross invoice amount, IVA causado, and IVA retenido must be reconstructed from the CFDI, not the bank statement amount. This is a critical reconciliation step.

**Foreign currency transactions.** Convert to MXN at the exchange rate published by Banco de Mexico (tipo de cambio FIX) for the transaction date. The CFDI must show the exchange rate used (TipoCambio field).

**Cryptic descriptions.** SPEI transfers with only a CLABE or reference number. Ask the client. Do not classify unidentified transactions.

**Refunds and credit notes.** Identified by "devolucion", "nota de credito", "bonificacion", "cancelacion". Book as a negative in the same line as the original transaction. The supplier must issue a CFDI tipo E (egreso) for the credit note.

## Ask the client first

For each question, the inference rule comes first. Only ask if inference fails.

### 9.1 RFC and regimen fiscal

- **RFC and regimen fiscal** -- Inference rule: RFC sometimes appears in SPEI transfer descriptions. 12 characters = persona moral, 13 = persona fisica. Fallback question: "What is your RFC and regimen fiscal (e.g. 601, 612, 626)?"

### 9.2 Tax regime type

- **Tax regime type** -- Inference rule: RESICO clients (626) have annual revenue below MXN 3,500,000 for personas fisicas. Fallback question: "Are you under Regimen General (601), Actividades Empresariales y Profesionales (612), or RESICO (626)?"

### 9.3 Filing period

- **Filing period** -- Inference rule: first and last transaction dates on the bank statement. Monthly filing is universal. Fallback question: "Which month does this cover?"

### 9.4 Industry and sector

- **Industry and sector** -- Inference rule: counterparty mix, CFDI descripciones, actividad economica. Fallback question: "In one sentence, what does the business do?"

### 9.5 Border zone status

- **Border zone status** -- Inference rule: ZIP codes (codigo postal) in the 21000-22900 range suggest Baja California; 32000-32700 suggest Ciudad Juarez; 88000-88999 suggest Nuevo Laredo/Tamaulipas border. Fallback question: "Is your tax domicile in the northern or southern border zone? Have you filed the aviso for the 8% rate?"

### 9.6 Exempt activities

- **Exempt activities inference** -- Inference rule: presence of residential rental income, medical service income, educational income. Fallback question: "Do you perform any exempt activities (residential rental, medical, education, insurance)?"

### 9.7 Export activities

- **Export activities** -- Inference rule: foreign currency credits, foreign-named counterparties on income side. Fallback question: "Do you export goods or services? To which countries?"

### 9.8 Saldo a favor carried forward

- **Saldo a favor carried forward** -- Inference rule: not inferable from a single period statement. Always ask. Question: "Do you have a saldo a favor from the prior month?"

### 9.9 IVA withholding status

- **IVA withholding status** -- Inference rule: if client is persona fisica receiving payments from personas morales, withholding is likely. Fallback question: "Do your clients withhold IVA from your payments?"

### 9.10 CFDI availability

- **CFDI availability** -- Inference rule: if client provides CFDI XMLs, this is answered. Fallback question: "Can you provide your CFDI XMLs (emitidos and recibidos) from the SAT portal for this month?"

## Sources


| Source | URL | Read on |
| --- | --- | --- |
| SAT article portal, LIVA Art. 1, read for the 16% rate | https://wwwmatnp.sat.gob.mx/articulo/19848/articulo-1 | 2026-11-14 |
| SAT article portal, LIVA Art. 2-A, read for the 0% list, the 16% on food prepared on the premises and the effects of the 0% rate | https://wwwmatnp.sat.gob.mx/articulo/06071/articulo-2-a | 2026-11-14 |
| SAT article portal, LIVA Art. 15, read for the exempt services list including Fr. IV (education) and Fr. XIV (medical services by individuals) | https://wwwmatnp.sat.gob.mx/articulo/67548/articulo-15 | 2026-11-14 |
| SAT article portal, LIVA Art. 5-D, read for monthly payment by day 17 | https://wwwmatnp.sat.gob.mx/articulo/73134/articulo-5-d | 2026-11-14 |
| DOF 31-12-2025, decree extending the northern and southern border stimulus decrees, read for the new validity to 31 December 2026 | https://dof.gob.mx/nota_detalle.php?codigo=5777697&fecha=31/12/2025 | 2026-11-14 |
| SAT, RMF 2026 (DOF 28-12-2025), read for chapter 11.9 and rule 11.9.3 (CFDI "IVA Crédito aplicado del 50%") | https://sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/rmf/RMF_2026-DOF-28122025.pdf | 2026-11-14 |
| DOF 04-12-2006, Reglamento de la Ley del IVA, read for Art. 3 fr. I (two thirds retention) | https://dof.gob.mx/nota_detalle.php?codigo=4939297&fecha=04/12/2006 | 2026-11-14 |
| DOF 18-11-2015, LISR reform decree, read for Art. 36 fr. II (MXN 175,000 automobile cap) | https://dof.gob.mx/nota_detalle.php?codigo=5415878&fecha=18/11/2015 | 2026-11-14 |
| Ley del Impuesto al Valor Agregado, texto vigente (ultima reforma DOF 12-11-2021), Arts. 1o., 1o.-A, 1o.-A BIS, 2o.-A, 4o., 5o., 9o., 15, 18-B, 18-J, 20, 25 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf | 2026-11-02 |
| Reglamento de la Ley del IVA (ultima reforma DOF 25-09-2014), Art. 3 | https://www.diputados.gob.mx/LeyesBiblio/regley/Reg_LIVA_250914.pdf | 2026-11-01 |
| Ley del Impuesto sobre la Renta, texto vigente (ultima reforma DOF 01-04-2024), Arts. 28 Fr. IV, 36 Fr. II, 106 | https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf | 2026-10-28 |
| SAT, Estímulo Fiscal Region Fronteriza Norte 8% IVA (guide to the Decreto DOF 31-12-2018) | https://www.sat.gob.mx/cs/Satellite?blobcol=urldata&blobkey=id&blobtable=MungoBlobs&blobwhere=1461173770379&ssbinary=true | 2026-10-28 |
| SAT, personas morales regimen general: declaraciones o pagos mensuales (dia 17) | http://omawww.sat.gob.mx/informacion_fiscal/obligaciones_fiscales/personas_morales/regimen_general/Paginas/declaraciones_mensuales.aspx | 2026-10-28 |

Also referenced without full archival: CFF Arts. 29, 29-A, 32, 69-B (CFDI and EFOS/EDOS blacklist); CFDI 4.0 technical catalogues; Declaraciones y Pagos system instructions.

### Known gaps

1. The supplier pattern library covers the most common Mexican and international counterparties but does not cover every regional business.
2. ICMS-ST equivalent mechanisms (retencion to specific industries) require more granular treatment.
3. The worked examples are drawn from a hypothetical software consultant. Sector-specific examples (manufacturing, retail, agricultural) should be added in v2.1.
4. Border zone municipality lists may be updated by decree -- verify annually.
5. The MXN 175,000 vehicle cap (DOF 18-11-2015) applies in 2026; the electric and hybrid cap is on the Not yet confirmed line.
6. Digital platform withholding rules (Art. 18-B to 18-M) are evolving and may change.

Not yet confirmed: the higher LISR Art. 36 fr. II automobile cap for electric and hybrid vehicles (the old MXN 250,000, not read in a 2026 text today); the 50% IVA retention by digital intermediation platforms under LIVA Art. 18-J (not read today); no-cap treatment of cargo and taxi vehicles under LISR Art. 36 Fr. II (not present in the archived texto vigente); official SAT Declaraciones y Pagos field names for the IVA return (the A/B/C/D codes in this skill are internal worksheet labels).


## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained in the OpenAccountants skills registry.

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network -- accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
