---
name: mexico-iva
description: Use this skill whenever asked to prepare, review, or classify transactions for a Mexico IVA (Impuesto al Valor Agregado) return or classify transactions for Mexican VAT purposes. Trigger on phrases like "prepare IVA return", "Mexican VAT", "declaracion de IVA", "CFDI classification", "SAT filing", or any request involving Mexico value-added tax. Also trigger when classifying transactions from CFDI XML files, bank statements, or invoices for Mexican IVA purposes. This skill contains the complete Mexico IVA classification rules, CFDI 4.0 requirements, rate determination (16%/0%/exempt), border zone treatment, withholding rules, deductibility rules, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Mexico IVA-related work.
version: 2.0
---

# Mexico IVA Return Preparation Skill v2.0

## Section 1 -- Quick reference

**Read this whole section before classifying anything.**

| Field | Value |
|---|---|
| Country | Mexico (Estados Unidos Mexicanos) |
| Standard rate | 16% |
| Border zone rate | 8% (Decreto region fronteriza, conditions apply -- reviewer must confirm eligibility) |
| Zero rate (tasa cero) | 0% (Article 2-A LIVA: basic food, medicine, agricultural, exports) -- input IVA IS creditable |
| Exempt (exento) | No IVA charged, input IVA NOT creditable (Articles 9, 15, 20, 25 LIVA) |
| Return form | Declaracion Mensual de IVA (monthly, filed via Declaraciones y Pagos portal) |
| Filing portal | https://www.sat.gob.mx (Portal del SAT) |
| Authority | Servicio de Administracion Tributaria (SAT) |
| Currency | MXN (Mexican Peso) |
| Filing frequency | Monthly (all IVA filers, no exceptions) |
| Deadline | 17th of the month following the period (individuals under RESICO: same) |
| E-invoice requirement | CFDI 4.0 mandatory for all transactions (Comprobante Fiscal Digital por Internet) |
| Primary legislation | Ley del Impuesto al Valor Agregado (LIVA); Codigo Fiscal de la Federacion (CFF); Resolucion Miscelanea Fiscal (RMF 2026) |
| Contributor | Open Accounting Skills Registry |
| Validated by | Deep research verification, April 2026 |
| Validation date | April 2026 |
| Skill version | 2.0 |

**Key return lines (Declaracion Mensual):**

| Line | Meaning |
|---|---|
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

**CFDI 4.0 requirements (mandatory for all transactions):**

Every sale, purchase, and payment must be documented by a valid CFDI 4.0 containing: RFC of issuer and recipient, regimen fiscal of issuer, uso del CFDI code, forma de pago, metodo de pago (PUE or PPD), lugar de expedicion (ZIP), IVA trasladado and/or retenido shown separately, UUID assigned by PAC, and SAT digital seal. Input IVA is NOT creditable without a valid, non-cancelled CFDI showing the client's correct RFC.

**Cash basis rule:** Mexico IVA operates on a cash basis (flujo de efectivo) for most taxpayers. IVA is owed when payment is received, not when invoiced. IVA is creditable when payment is made, not when the CFDI is received. For PPD invoices, crediting requires the Complemento de Pago (REP) to be issued.

**Conservative defaults -- Mexico-specific:**

| Ambiguity | Default |
|---|---|
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

**Red flag thresholds:**

| Threshold | Value |
|---|---|
| HIGH single-transaction size | MXN 50,000 |
| HIGH tax-delta on a single conservative default | MXN 5,000 |
| MEDIUM counterparty concentration | >40% of output OR input |
| MEDIUM conservative-default count | >4 across the return |
| LOW absolute net IVA position | MXN 100,000 |

---

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- bank statement (estado de cuenta) for the month in CSV, PDF, or pasted text. Must cover the full period. Acceptable from any Mexican bank: BBVA Bancomer, Banorte, Santander Mexico, Citibanamex, HSBC Mexico, Scotiabank Mexico, Banco Azteca, or any other. CFDI XMLs are strongly preferred for input IVA crediting.

**Recommended** -- CFDI XML files for all sales and purchases (or at minimum the monthly CFDI listing from SAT portal), prior month's declaracion showing saldo a favor carried forward, the client's RFC and constancia de situacion fiscal.

**Ideal** -- complete CFDI download from SAT portal (both emitidos and recibidos), estado de cuenta from all business bank accounts, prior month return filed, constancia de situacion fiscal showing regimen and obligations.

**Refusal policy if minimum is missing -- SOFT WARN.** If no bank statement and no CFDIs are available at all, hard stop. If bank statement only without CFDIs, proceed but record in the reviewer brief: "This IVA return was produced from bank statement alone. The reviewer must verify that all input IVA claims are supported by valid CFDI 4.0 documents and that the cash basis timing rule has been applied correctly."

### Mexico-specific refusal catalogue

**R-MX-1 -- Maquiladora / IMMEX operations.** *Trigger:* client operates under the IMMEX program or has maquiladora status. *Message:* "IMMEX/maquiladora operations have special IVA certification, virtual import/export, and temporary import rules that are outside this skill's scope. Escalate to a Contador Publico with IMMEX experience."

**R-MX-2 -- Consolidated group filing.** *Trigger:* client is part of a grupo empresarial filing consolidated returns. *Message:* "Consolidated group IVA structures are outside this skill's scope. Escalate to a licensed tax practitioner."

**R-MX-3 -- Transfer pricing IVA implications.** *Trigger:* intercompany transactions with related parties where pricing affects IVA base. *Message:* "Transfer pricing adjustments affecting the IVA base require specialist analysis. Escalate."

**R-MX-4 -- EFOS/EDOS blacklist.** *Trigger:* client's RFC or a major supplier's RFC appears on SAT's Article 69-B blacklist (Empresas Facturadoras de Operaciones Simuladas). *Message:* "One or more RFCs involved in these transactions may be on the EFOS/EDOS blacklist. All CFDIs from blacklisted suppliers are presumed false and non-creditable. Escalate to a Contador Publico immediately."

**R-MX-5 -- Income tax return instead of IVA.** *Trigger:* user asks about annual income tax return (declaracion anual ISR), not the monthly IVA. *Message:* "This skill only handles the monthly IVA return. For Mexico income tax (ISR), use the appropriate income tax skill."

**R-MX-6 -- Payroll (nomina) processing.** *Trigger:* user asks about CFDI de nomina, IMSS, INFONAVIT, or payroll obligations. *Message:* "Payroll is outside the scope of the IVA return. Use a payroll-specific skill."

---

## Section 3 -- Supplier pattern library (the lookup table)

This is the deterministic pre-classifier. When a transaction's counterparty matches a pattern in this table, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name as it appears in the bank statement or CFDI. If multiple patterns match, use the most specific.

### 3.1 Mexican banks (fees exempt -- exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BBVA BANCOMER, BBVA MEXICO | EXCLUDE for bank charges/fees/comisiones | Financial service, exempt under Art. 15 Fr. X |
| BANORTE, BANCO MERCANTIL DEL NORTE | EXCLUDE for bank charges/fees | Same |
| SANTANDER MX, SANTANDER MEXICO, BANCO SANTANDER | EXCLUDE for bank charges/fees | Same |
| CITIBANAMEX, BANAMEX | EXCLUDE for bank charges/fees | Same |
| HSBC MEXICO | EXCLUDE for bank charges/fees | Same |
| SCOTIABANK MEXICO | EXCLUDE for bank charges/fees | Same |
| BANCO AZTECA | EXCLUDE for bank charges/fees | Same |
| BANREGIO, BANBAJIO, BANCO DEL BAJIO | EXCLUDE for bank charges/fees | Same |
| INTERESES, INTERES, RDTO | EXCLUDE | Interest income/expense, exempt |
| CREDITO, PRESTAMO, LOAN | EXCLUDE | Loan principal movement, out of scope |
| COMISION BANCARIA, ANUALIDAD TARJETA | EXCLUDE | Bank commission/card annuity, exempt financial service |

### 3.2 Mexican government, regulators, and statutory bodies (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| SAT, SERVICIO DE ADMINISTRACION TRIBUTARIA | EXCLUDE | Tax payment, not a supply |
| DECLARACION, PAGO DE IMPUESTOS | EXCLUDE | Tax payment |
| IMSS, SEGURO SOCIAL | EXCLUDE | Social security contribution, not IVA |
| INFONAVIT | EXCLUDE | Housing fund contribution, not IVA |
| AFORE, PENSIONES | EXCLUDE | Pension fund, out of scope |
| GOBIERNO, SECRETARIA, AYUNTAMIENTO | EXCLUDE | Government fees, sovereign acts |
| MUNICIPIO, PREDIAL, TENENCIA | EXCLUDE | Property/vehicle tax, not a supply |
| TRAMITE, LICENCIA GOBIERNO | EXCLUDE | Government licence, sovereign act |

### 3.3 Mexican utilities

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| CFE, COMISION FEDERAL DE ELECTRICIDAD | Domestic 16% | B1 (input) | Electricity -- deductible overhead, CFDI issued |
| TELMEX, TELEFONOS DE MEXICO | Domestic 16% | B1 (input) | Telecoms -- deductible overhead |
| TELCEL, AT&T MEXICO, MOVISTAR | Domestic 16% | B1 (input) | Mobile telecoms -- confirm business use |
| IZZI, TOTALPLAY, MEGACABLE | Domestic 16% | B1 (input) | Internet/cable -- deductible if business |
| AGUA, SAPAS, SIAPA, SACMEX | EXCLUDE or exempt | | Water -- many municipal water services are exempt |
| GAS NATURAL, NATURGY, GAS LP | Domestic 16% | B1 (input) | Gas supply, standard rated |

### 3.4 Fuel and petroleum (Pemex and others)

| Pattern | Treatment | Notes |
|---|---|---|
| PEMEX, GASOLINERA, ESTACION DE SERVICIO | Domestic 16% | Fuel -- creditable if business vehicle with valid CFDI. Vehicle cap rules apply (MXN 175,000 / MXN 250,000 for electric). Flag if personal vehicle. |
| GASOLINA, DIESEL, COMBUSTIBLE | Domestic 16% | Same treatment as above |
| CASETA, PEAJE, CAPUFE | Domestic 16% | Toll roads -- creditable with CFDI. Some tolls issue simplified CFDI. |

### 3.5 Insurance (exempt -- exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| GNP, GRUPO NACIONAL PROVINCIAL | EXCLUDE | Insurance premium, exempt (Art. 15 Fr. IX/X) |
| AXA SEGUROS, MAPFRE MEXICO | EXCLUDE | Same |
| METLIFE, SEGUROS MONTERREY | EXCLUDE | Same |
| QUALITAS, HDI SEGUROS | EXCLUDE | Same |
| SEGUROS, POLIZA, PRIMA DE SEGURO | EXCLUDE | All insurance premiums exempt |

### 3.6 Major Mexican retailers and e-commerce

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| WALMART MEXICO, WALMEX, BODEGA AURRERA | Domestic 16% | B1 (input) | General merchandise -- creditable if business expense with valid CFDI. Food items may be 0% on CFDI. |
| COSTCO MEXICO | Domestic 16% | B1 (input) | Same. Check CFDI for mixed rates. |
| AMAZON MX, AMAZON MEXICO | Domestic 16% | B1 (input) | Check billing entity -- Amazon Mexico S. de R.L. de C.V. issues Mexican CFDI at 16%. |
| MERCADO LIBRE, MERCADOPAGO | Domestic 16% | B1 (input) | Mexican entity. Transaction fees may be exempt financial service -- check CFDI. |
| OFFICE DEPOT, STAPLES MEXICO | Domestic 16% | B1 (input) | Office supplies, standard rated |
| HOME DEPOT MEXICO | Domestic 16% | B1 (input) | Construction/maintenance supplies |
| LIVERPOOL, PALACIO DE HIERRO | Domestic 16% | B1 (input) | Department store -- confirm business purpose |
| SORIANA, CHEDRAUI, LA COMER | Domestic 16% | B1 (input) | Supermarket -- food items may appear at 0% on CFDI |

### 3.7 Transport and ride-hailing

| Pattern | Treatment | Notes |
|---|---|---|
| UBER MX, UBER MEXICO, UBER TRIP | Domestic 16% with withholding | Uber Mexico issues CFDI. Platform withholds IVA from driver (Art. 1-A). For the rider: input IVA creditable with CFDI. |
| DIDI, DIDI MEXICO | Domestic 16% with withholding | Same as Uber |
| BEAT, CABIFY MEXICO | Domestic 16% | Same treatment |
| VOLARIS, AEROMEXICO, VIVA AEROBUS | Domestic 16% or 0% (international) | Domestic flights at 16%. International flights: check if 0% (export of service). |
| ADO, PRIMERA PLUS, ETN | Domestic 16% | Intercity bus -- standard rated (urban public transport is exempt) |
| METROBUS, METRO, TRANSPORTE PUBLICO | EXCLUDE or exempt | Urban/suburban public transport exempt (Art. 15 Fr. V) |

### 3.8 SaaS and digital services -- foreign suppliers

| Pattern | Billing entity | Treatment | Notes |
|---|---|---|---|
| GOOGLE (Ads, Workspace, Cloud) | Google Mexico S. de R.L. de C.V. or Google LLC | If Mexican CFDI: domestic 16%. If no CFDI: imported service, IVA on import applies. | Check CFDI. Google registered in Mexico issues CFDI. |
| MICROSOFT (365, Azure) | Microsoft Mexico or Microsoft Corp | Same -- check billing entity on CFDI | |
| ADOBE | Adobe Systems Mexico or Adobe Inc (US) | Same | |
| META, FACEBOOK ADS | Meta Platforms Mexico or Meta (US/IE) | If Mexican entity with CFDI: 16%. If foreign: imported digital service. | |
| AMAZON WEB SERVICES, AWS | Amazon Web Services Mexico or AWS Inc | Check CFDI entity | |
| ZOOM | Zoom Video Communications | If no Mexican entity: imported service | |
| SLACK, ATLASSIAN, NOTION | Various (US entities) | Imported service -- no CFDI. IVA self-assessed on import. | |
| SPOTIFY, NETFLIX, APPLE | Mexican-registered for B2C digital services | These platforms now collect and remit IVA in Mexico for B2C digital services under Art. 18-B to 18-M LIVA. B2B: check if CFDI issued. | |

### 3.9 Payment processors

| Pattern | Treatment | Notes |
|---|---|---|
| STRIPE (transaction fees) | EXCLUDE (exempt) or imported service | If billed from US entity without CFDI: imported financial service. Transaction fees may be exempt. |
| PAYPAL (transaction fees) | EXCLUDE (exempt) | PayPal Mexico issues CFDI for certain services. Transaction commissions are financial services (exempt). |
| MERCADOPAGO (transaction fees) | EXCLUDE (exempt) | Payment processing commission -- exempt financial service |
| CONEKTA, OPENPAY, SR PAGO | Domestic 16% | Mexican payment processors -- check CFDI for service fees vs. transaction fees |
| CLIP, IZETTLE | Domestic 16% | POS terminal services |

### 3.10 Professional services (Mexico)

| Pattern | Treatment | Line | Notes |
|---|---|---|---|
| NOTARIO, NOTARIA, FE PUBLICA | Domestic 16% | B1 (input) | Notarial services, standard rated |
| CONTADOR, CONTABILIDAD, DESPACHO CONTABLE | Domestic 16% | B1 (input) | Accounting/bookkeeping, always deductible |
| ABOGADO, BUFETE, DESPACHO JURIDICO | Domestic 16% | B1 (input) | Legal services, deductible if business matter |
| CONSULTORIA, ASESORIA | Domestic 16% | B1 (input) | Consulting, standard rated |

### 3.11 Payroll and social security (exclude entirely)

| Pattern | Treatment | Notes |
|---|---|---|
| NOMINA, SUELDO, SALARIO | EXCLUDE | Wages -- outside IVA scope |
| IMSS, SEGURO SOCIAL | EXCLUDE | Social security contribution |
| INFONAVIT | EXCLUDE | Housing fund |
| PTU, REPARTO DE UTILIDADES | EXCLUDE | Profit sharing, out of scope |
| AGUINALDO, VACACIONES | EXCLUDE | Year-end bonus, vacation pay -- out of scope |
| SAR, AFORE | EXCLUDE | Retirement contributions |

### 3.12 Internal transfers and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| TRASPASO, TRANSFERENCIA PROPIA | EXCLUDE | Internal account movement |
| RETIRO, CAJERO, ATM | Ask | Cash withdrawal -- ask what cash was spent on |
| DIVIDENDO | EXCLUDE | Dividend, out of scope |
| PRESTAMO PERSONAL, DISPOSICION | EXCLUDE | Loan drawdown, out of scope |

---

## Section 4 -- Worked examples

These are six fully worked classifications drawn from a hypothetical bank statement of a Mexico-based self-employed software consultant (persona fisica, Actividades Empresariales y Profesionales regime). They illustrate the trickiest cases.

### Example 1 -- Standard domestic sale with CFDI

**Input line:**
`05.04.2026 ; EMPRESA TECH SA DE CV ; CREDIT ; Factura FE-2026-041 Consultoria abril ; MXN 116,000.00`

**Reasoning:**
Client issued CFDI tipo I (ingreso) for MXN 100,000 + IVA MXN 16,000. Payment received in April. Cash basis: IVA causado in April. Line A1 = MXN 100,000. Output IVA = MXN 16,000.

**Output:**

| Date | Counterparty | Gross | Net | IVA | Rate | Line | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | EMPRESA TECH SA DE CV | +116,000 | +100,000 | +16,000 | 16% | A1/A2 | N | -- |

### Example 2 -- IVA withholding by client (persona moral paying persona fisica)

**Input line:**
`10.04.2026 ; CORPORATIVO DELTA SA DE CV ; CREDIT ; Pago factura consultoria ; MXN 105,333.33`

**Reasoning:**
Client invoiced MXN 100,000 + IVA MXN 16,000 = MXN 116,000. The corporate client (persona moral) withheld 2/3 of IVA (MXN 10,666.67) per Art. 1-A Fr. II(a) LIVA and 10% ISR (MXN 10,000). Net deposit = MXN 116,000 - MXN 10,666.67 = MXN 105,333.33 (ISR withheld is separate). Report full IVA causado MXN 16,000 on A2, and IVA retenido MXN 10,666.67 on C1.

**Output:**

| Date | Counterparty | Gross | Net | IVA causado | IVA retenido | Rate | Lines | Default? | Question? |
|---|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | CORPORATIVO DELTA SA DE CV | +105,333.33 | +100,000 | +16,000 | -10,666.67 | 16% | A1/A2/C1 | N | Verify CFDI shows retencion |

### Example 3 -- Imported digital service (no Mexican CFDI)

**Input line:**
`15.04.2026 ; NOTION LABS INC ; DEBIT ; Monthly subscription ; USD 15.00 ; MXN 270.00`

**Reasoning:**
Notion Labs Inc is a US entity. No Mexican CFDI issued. This is an importation of services under Art. 24 LIVA. The Mexican taxpayer must self-assess IVA at 16% on the value. IVA on import = MXN 270 x 0.16 = MXN 43.20. This import IVA is creditable (B3) if the service is strictly indispensable for the business.

**Output:**

| Date | Counterparty | Gross | Net | IVA import | Rate | Line | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | NOTION LABS INC | -270.00 | -270.00 | 43.20 | 16% | B3 (import) | N | Verify service is business use |

### Example 4 -- Entertainment, non-creditable

**Input line:**
`18.04.2026 ; RESTAURANTE LA HACIENDA ; DEBIT ; Comida con cliente ; MXN 2,500.00`

**Reasoning:**
Restaurant meal. Entertainment expenses (gastos de representacion) are generally non-deductible under LISR Art. 28 Fr. XXI, which cross-references to IVA creditability. IVA on entertainment is not creditable because the expense is not "strictly indispensable." Default: block IVA credit.

**Output:**

| Date | Counterparty | Gross | Net | IVA | Rate | Line | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 18.04.2026 | RESTAURANTE LA HACIENDA | -2,500.00 | -2,155.17 | 0 | -- | -- | Y | "Entertainment: IVA not creditable" |

### Example 5 -- Zero-rated sale (export of services)

**Input line:**
`22.04.2026 ; ACME CORP (US) ; CREDIT ; Invoice MX-2026-012 Software development ; USD 5,000.00 ; MXN 90,000.00`

**Reasoning:**
Software development services exported to US client. Service effectively used/enjoyed abroad. Zero-rated under Art. 2-A Fr. IV / Art. 29 LIVA. Line A5 = MXN 90,000. IVA = 0%. Input IVA on related expenses remains fully creditable (advantage of 0% over exempt).

**Output:**

| Date | Counterparty | Gross | Net | IVA | Rate | Line | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 22.04.2026 | ACME CORP (US) | +90,000 | +90,000 | 0 | 0% | A5 | Y | Verify service used/enjoyed abroad |

### Example 6 -- Vehicle fuel with CFDI, cap consideration

**Input line:**
`28.04.2026 ; GASOLINERA PEMEX EST 1234 ; DEBIT ; Carga gasolina ; MXN 1,200.00`

**Reasoning:**
Fuel purchase at Pemex station. If business vehicle and valid CFDI exists: IVA creditable. IVA = MXN 1,200 / 1.16 x 0.16 = MXN 165.52 (net MXN 1,034.48). However, vehicle cap rules apply: if the vehicle purchase price exceeded MXN 175,000, only proportional IVA on running costs is creditable. Default: block unless vehicle and CFDI confirmed.

**Output:**

| Date | Counterparty | Gross | Net | IVA | Rate | Line | Default? | Question? |
|---|---|---|---|---|---|---|---|---|
| 28.04.2026 | GASOLINERA PEMEX EST 1234 | -1,200.00 | -1,034.48 | 0 | -- | -- | Y | "Vehicle: confirm business use and CFDI" |

---

## Section 5 -- Tier 1 classification rules (compressed)

Each rule states the legal source and the return line mapping. Apply silently if the data is unambiguous.

### 5.1 Standard rate 16% (LIVA Article 1)

Default rate for all taxable activities in Mexico unless zero-rated or exempt. Sales at 16%: Line A1 (net), A2 (IVA). Purchases at 16%: Line B1 (input IVA, if creditable).

### 5.2 Border zone rate 8% (Decreto region fronteriza)

Available ONLY when all conditions are met: tax domicile in qualifying border municipality, supply occurs physically in the zone, 18-month establishment requirement, aviso filed with SAT, not on EFOS blacklist. If ANY condition is unverified, apply 16%. Sales at 8%: Line A3 (net), A4 (IVA). Purchases at 8%: Line B2.

### 5.3 Zero-rated activities 0% (Article 2-A LIVA)

Basic foodstuffs (unprocessed), prescription medicines, agricultural inputs/services, exports of goods (with pedimento), exports of services (used/enjoyed abroad), books/newspapers, feminine hygiene products, pet food. Zero-rate allows FULL crediting of input IVA. Sales: Line A5.

### 5.4 Exempt activities (Articles 9, 15, 20, 25 LIVA)

Residential rental, land sales, financial services (interest, insurance), medical services, accredited education, urban public transport, residential construction. Exempt = no IVA charged AND no input IVA credit on attributable costs.

### 5.5 CFDI requirements for input IVA crediting

Input IVA is creditable ONLY if: (1) valid CFDI 4.0 with UUID exists, (2) CFDI is in "Vigente" status (not cancelled), (3) client's RFC is shown correctly as receptor, (4) IVA is separately stated (trasladado), (5) payment has been made (cash basis), (6) for PPD invoices, REP (Complemento de Pago) has been issued. Missing any element = zero credit.

### 5.6 IVA withholding (retencion, Article 1-A LIVA)

Personas morales paying personas fisicas for professional services: withhold 2/3 of IVA. Personas morales paying for certain subcontracted services: withhold 6% of the payment value as IVA. Digital platform withholding: platforms withhold IVA per Art. 18-J. Withheld IVA is reported on Line C1 (withheld by clients) and is creditable against IVA payable.

### 5.7 Imported services

Services received from non-residents without Mexican CFDI: IVA on import at 16% applies. Self-assessed by the Mexican taxpayer. Reported on Line B3. Creditable if service is strictly indispensable.

### 5.8 Proportional crediting (factor de acreditamiento, Art. 5 Fr. V)

When the taxpayer performs BOTH taxable AND exempt activities: Factor = (value of taxable activities) / (total value of all activities). Apply factor to input IVA on shared/common expenses. Direct attribution first: costs directly for taxable = 100% credit; costs directly for exempt = 0% credit.

### 5.9 Blocked / non-creditable input IVA

Non-deductible expenses under LISR = non-creditable IVA. Entertainment (gastos de representacion). Personal expenses. Expenses without valid CFDI. IVA not separately stated. Expenses related exclusively to exempt activities.

### 5.10 Vehicle rules (LISR Art. 36 Fr. II cross-reference)

Automobiles: IVA creditable only up to the MXN 175,000 purchase price cap (MXN 250,000 for electric/hybrid). IVA on running costs (fuel, maintenance) follows the same proportionality. Cargo vehicles (camiones de carga) used exclusively for freight: no cap. Taxis and passenger transport vehicles used exclusively in transport services: no cap.

### 5.11 Cash basis timing

IVA causado (output): report in the month payment is received. IVA acreditable (input): credit in the month payment is made. For PPD invoices: credit only when REP is issued. For PUE invoices: credit in the month of the CFDI date (payment made at invoice time).

### 5.12 Saldo a favor (favorable balance)

When input IVA exceeds output IVA: the balance can be carried forward (acreditamiento) or refunded (solicitud de devolucion via FED portal). Refund requests trigger SAT review and may require additional documentation.

---

## Section 6 -- Tier 2 catalogue (compressed)

### 6.1 Border zone rate eligibility

*Pattern:* client claims 8% rate. *Why insufficient:* requires verification of all six conditions (domicile, physical supply, 18-month establishment, aviso filed, not on EFOS, payroll requirements). *Default:* 16%. *Question:* "Have you filed the aviso with SAT and do you meet all conditions for the border zone stimulus?"

### 6.2 Restaurants and entertainment

*Pattern:* restaurant, bar, entertainment venue. *Why insufficient:* entertainment is generally non-deductible under LISR, making IVA non-creditable. *Default:* block IVA credit. *Question:* "Was this a business meal or entertainment? (Note: entertainment IVA is generally not creditable.)"

### 6.3 Mixed activities -- proportional crediting

*Pattern:* client has both taxable and exempt revenue. *Why insufficient:* requires annual factor calculation and direct attribution analysis. *Default:* apply factor based on available period data; flag for year-end adjustment. *Question:* "What proportion of your revenue is from taxable vs exempt activities?"

### 6.4 Vehicle business use

*Pattern:* fuel, car maintenance, vehicle lease. *Why insufficient:* business vs personal use and vehicle value unknown. *Default:* 0% recovery. *Question:* "Is this a business vehicle? What was the purchase price? Is there a valid CFDI?"

### 6.5 IVA withholding classification

*Pattern:* payment to persona fisica for services. *Why insufficient:* need to confirm the counterparty is persona fisica and the service type. *Default:* no withholding (flag for reviewer). *Question:* "Is the service provider a persona fisica or persona moral? What service is being provided?"

### 6.6 Export of services -- place of enjoyment

*Pattern:* service income from foreign client. *Why insufficient:* zero-rating requires that the service is "effectively used or enjoyed abroad" (Art. 29 Fr. IV LIVA) -- strict interpretation by SAT. *Default:* 16% (conservative). *Question:* "Where is this service effectively used or enjoyed? Can you document that the benefit occurs outside Mexico?"

### 6.7 Round-number incoming transfers

*Pattern:* large round credit from owner-named or personal counterparty. *Default:* exclude as owner injection. *Question:* "Is this a customer payment, your own money, or a loan?"

### 6.8 Ambiguous SaaS billing entity

*Pattern:* Google, Microsoft, Adobe, Meta where the billing entity is unclear. *Default:* assume no CFDI exists, treat as imported service with IVA self-assessment at 16%. *Question:* "Does the provider issue a Mexican CFDI? What entity name and RFC appear on the invoice?"

### 6.9 Cash withdrawals

*Pattern:* ATM, retiro efectivo, cajero. *Default:* exclude as personal drawing. *Question:* "What was the cash used for?"

### 6.10 PPD invoices without REP

*Pattern:* purchase where CFDI shows MetodoPago = PPD but no REP has been received. *Default:* IVA NOT creditable until REP is issued. *Question:* "Has the supplier issued a Complemento de Pago (REP) for this payment?"

---

## Section 7 -- Excel working paper template (Mexico-specific)

### Sheet "Transactions"

Columns: A (Date), B (Counterparty/RFC), C (CFDI UUID), D (Gross MXN), E (Net MXN), F (IVA trasladado), G (IVA retenido), H (Rate), I (Line code), J (Default Y/N), K (Question), L (Notes).

Column C (UUID) is critical in Mexico -- it links every transaction to its CFDI. If UUID is blank, input IVA is not creditable.

### Sheet "Return Summary"

One row per return line. Column A is the line code, column B is the description, column C is the value. Structure:

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

---

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

---

## Section 9 -- Onboarding fallback (only when inference fails)

For each question, the inference rule comes first. Only ask if inference fails.

### 9.1 RFC and regimen fiscal
*Inference rule:* RFC sometimes appears in SPEI transfer descriptions. 12 characters = persona moral, 13 = persona fisica. *Fallback question:* "What is your RFC and regimen fiscal (e.g. 601, 612, 626)?"

### 9.2 Tax regime type
*Inference rule:* RESICO clients (626) have annual revenue below MXN 3,500,000 for personas fisicas. *Fallback question:* "Are you under Regimen General (601), Actividades Empresariales y Profesionales (612), or RESICO (626)?"

### 9.3 Filing period
*Inference rule:* first and last transaction dates on the bank statement. Monthly filing is universal. *Fallback question:* "Which month does this cover?"

### 9.4 Industry and sector
*Inference rule:* counterparty mix, CFDI descripciones, actividad economica. *Fallback question:* "In one sentence, what does the business do?"

### 9.5 Border zone status
*Inference rule:* ZIP codes (codigo postal) in the 21000-22900 range suggest Baja California; 32000-32700 suggest Ciudad Juarez; 88000-88999 suggest Nuevo Laredo/Tamaulipas border. *Fallback question:* "Is your tax domicile in the northern or southern border zone? Have you filed the aviso for the 8% rate?"

### 9.6 Exempt activities
*Inference rule:* presence of residential rental income, medical service income, educational income. *Fallback question:* "Do you perform any exempt activities (residential rental, medical, education, insurance)?"

### 9.7 Export activities
*Inference rule:* foreign currency credits, foreign-named counterparties on income side. *Fallback question:* "Do you export goods or services? To which countries?"

### 9.8 Saldo a favor carried forward
*Inference rule:* not inferable from a single period statement. Always ask. *Question:* "Do you have a saldo a favor from the prior month?"

### 9.9 IVA withholding status
*Inference rule:* if client is persona fisica receiving payments from personas morales, withholding is likely. *Fallback question:* "Do your clients withhold IVA from your payments?"

### 9.10 CFDI availability
*Inference rule:* if client provides CFDI XMLs, this is answered. *Fallback question:* "Can you provide your CFDI XMLs (emitidos and recibidos) from the SAT portal for this month?"

---

## Section 10 -- Reference material

### Sources

**Primary legislation:**
1. Ley del Impuesto al Valor Agregado (LIVA) -- Articles 1, 1-A, 1-B, 2-A, 4, 5, 5-D, 8, 9, 14, 15, 16, 19, 20, 24, 25, 29
2. Codigo Fiscal de la Federacion (CFF) -- Articles 29, 29-A, 32, 69-B
3. Ley del Impuesto sobre la Renta (LISR) -- Articles 28, 36 (cross-reference for deductibility)
4. Resolucion Miscelanea Fiscal 2026 (RMF) -- Rules 2.7.x (CFDI requirements)
5. Decreto de Estimulos Fiscales Region Fronteriza Norte (2018, extended through 2026)
6. Decreto Region Fronteriza Sur (2021, extended through 2026)

**SAT guidance:**
7. Portal del SAT -- https://www.sat.gob.mx
8. CFDI 4.0 technical specifications and catalogues
9. Declaraciones y Pagos system instructions

### Known gaps

1. The supplier pattern library covers the most common Mexican and international counterparties but does not cover every regional business.
2. ICMS-ST equivalent mechanisms (retencion to specific industries) require more granular treatment.
3. The worked examples are drawn from a hypothetical software consultant. Sector-specific examples (manufacturing, retail, agricultural) should be added in v2.1.
4. Border zone municipality lists may be updated by decree -- verify annually.
5. The MXN 175,000 / MXN 250,000 vehicle cap values are as of 2026. Verify annually.
6. Digital platform withholding rules (Art. 18-B to 18-M) are evolving and may change.

### Change log

- **v2.0 (April 2026):** Full rewrite to Malta v2.0 structure. Quick reference at top (Section 1) with CFDI 4.0 requirements and conservative defaults. Supplier pattern library restructured as literal lookup tables (Section 3) with Mexican vendors. Six worked examples added (Section 4). Tier 1 rules compressed (Section 5). Tier 2 catalogue added (Section 6). Excel template specification added (Section 7). Mexican bank statement reading guide added (Section 8). Onboarding fallback with inference rules (Section 9).
- **v1.1 (April 2026):** Previous version with full monolithic structure.

### Self-check (v2.0)

1. Quick reference at top with return lines and conservative defaults: yes (Section 1).
2. CFDI 4.0 requirements prominently stated: yes (Section 1).
3. Supplier library as literal lookup tables with Mexican vendors: yes (Section 3, 12 sub-tables).
4. Worked examples from hypothetical consultant: yes (Section 4, 6 examples).
5. Tier 1 rules compressed: yes (Section 5, 12 rules).
6. Tier 2 catalogue compressed with inference rules: yes (Section 6, 10 items).
7. Excel template specification: yes (Section 7).
8. Mexican bank statement reading guide (estado de cuenta): yes (Section 8).
9. Onboarding as fallback with inference rules: yes (Section 9, 10 items).
10. Cash basis rule explicitly stated: yes (Section 1, Section 5.11).
11. IVA withholding rules explicit: yes (Section 5.6, Example 2).
12. Entertainment block explicit: yes (Section 5.9, Example 4).
13. Vehicle cap rules explicit: yes (Section 5.10, Example 6).
14. Export zero-rating and place-of-enjoyment test explicit: yes (Section 5.3, Example 5).
15. Refusal catalogue present: yes (Section 2, R-MX-1 through R-MX-6).

## End of Mexico IVA Return Skill v2.0


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
