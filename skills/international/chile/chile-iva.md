---
name: chile-iva
description: Use this skill whenever asked to prepare, review, or classify transactions for a Chile IVA (Impuesto al Valor Agregado) return or advise on Chilean VAT registration, filing, and SII compliance. Trigger on phrases like "prepare IVA return Chile", "Chilean VAT", "IVA Chile", "SII", "RUT", or any Chile IVA request. ALWAYS read this skill before touching any Chile IVA work.
version: 2.0
jurisdiction: CL
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Chile IVA (Impuesto al Valor Agregado) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Chile (República de Chile) |
| Tax | IVA (Impuesto al Valor Agregado) |
| Currency | CLP (Chilean Peso — $) |
| Standard rate | 19% |
| Reduced rate | None (Chile has a single standard rate) |
| Zero rate | 0% (exports of goods and services) |
| Exempt | Financial services, insurance, residential rent, healthcare, education, passenger transport (buses, metro, taxis), domestic air transport, certain cultural events |
| Registration threshold | No threshold — any business making taxable supplies must register as contributor (contribuyente) |
| Tax authority | SII (Servicio de Impuestos Internos) |
| Filing portal | SII portal — https://www.sii.cl |
| Return form | Formulario 29 (Declaración Mensual y Pago Simultáneo) |
| Filing frequency | Monthly |
| Deadline | 12th of the following month (electronic); varies by RUT |
| e-Invoice | DTE (Documento Tributario Electrónico) mandatory for all contributors |
| RUT | Rol Único Tributario — Chilean taxpayer ID (e.g., 12.345.678-9) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by Chile-licensed contador auditor |
| Skill version | 2.0 |

### Key Formulario 29 codes

| Code | Meaning |
|---|---|
| Code 502 | Net taxable sales (base 19%) |
| Code 503 | IVA on sales (débito fiscal) |
| Code 505 | Export sales |
| Code 506 | Exempt sales |
| Code 524 | Net taxable purchases |
| Code 525 | IVA on purchases (crédito fiscal) |
| Code 547 | Net IVA payable (503 − 525) |
| Code 77 | Remanente crédito fiscal (excess credit c/f) |
| Code 538 | IVA on imports (paid at customs) |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 19% standard |
| Unknown whether exempt | 19% until confirmed |
| Unknown whether export documentation complete | Treat as domestic 19% |
| Unknown business-use % (vehicle, phone, home) | 0% input credit |
| Unknown whether DTE issued | No input credit until confirmed |
| Foreign digital service (B2B) | 19% — non-resident digital service providers register under SII simplified scheme |
| Transport (local bus/metro) | Exempt |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | CLP 50,000,000 |
| HIGH tax delta on single conservative default | CLP 9,500,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per return |
| LOW absolute net IVA position | CLP 100,000,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

Before starting any Chile IVA work, obtain:

1. RUT (Rol Único Tributario) and SII contributor registration (Inicio de Actividades)
2. Monthly bank statements in CLP (all business accounts)
3. DTE (Documento Tributario Electrónico) files — Facturas Electrónicas issued (XML from SII portal)
4. Facturas Electrónicas received from suppliers (XML or PDF with folio and SII verification)
5. Prior month Formulario 29 (for remanente crédito fiscal carried forward)
6. Import customs declarations (DUS — Declaración de Importación) for imported goods
7. Export documentation (DUS exportación, AWB/BL) for zero-rated exports

### Refusal catalogue

Refuse and escalate to a contador auditor for:
- Proporcionalidad (partial exemption) — businesses with mixed exempt/taxable supplies
- IVA on real estate (complex rules — IVA on first sale of construction)
- IVA retenciones — withholding agents in construction and other sectors
- Export IVA refund (recuperación de IVA exportadores) — complex SII process
- IVA on leasing / leaseback structures
- Zone franca (free trade zone — Iquique/Punta Arenas) special treatment
- Non-resident digital service provider registration compliance

---

## Section 3 — Supplier pattern library

### 3.1 Banking and financial services

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| BancoEstado | Bank fees, transfers | Exempt | No |
| Banco de Chile | Account maintenance, credit | Exempt | No |
| Santander Chile | Commercial banking | Exempt | No |
| BCI (Banco de Crédito e Inversiones) | Business banking | Exempt | No |
| Scotiabank Chile | Corporate banking | Exempt | No |
| Banco Falabella | Consumer/retail banking | Exempt | No |
| Transbank | Card processing (débito/crédito) | 19% (service fee) | Yes |
| GetNet Chile | POS terminal / payment processing | 19% | Yes |
| Kushki | Digital payment gateway | 19% | Yes |
| Mercado Pago Chile | Payment platform | 19% | Yes |

### 3.2 Electricity, gas, and utilities

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Enel Distribución Chile (formerly Chilectra) | Electricity — Santiago Metropolitan | 19% | Yes (business) |
| CGE (Compañía General de Electricidad) | Electricity — regions | 19% | Yes (business) |
| Engie Chile (formerly GNL Quintero) | Natural gas distribution | 19% | Yes (business) |
| Metrogas (Gas Natural Fenosa) | Piped gas — Santiago | 19% | Yes (business) |
| Aguas Andinas | Water — Santiago | 19% | Yes (business) |
| ESVAL | Water — Valparaíso | 19% | Yes |

### 3.3 Telecommunications

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Entel Chile | Mobile, broadband, enterprise | 19% | Yes (business use) |
| Movistar Chile (Telefónica) | Mobile, fixed, ADSL | 19% | Yes (business use) |
| Claro Chile | Mobile, cable TV | 19% | Yes (business use) |
| WOM | Mobile — budget carrier | 19% | Yes |
| GTD (Grupo Teleductos) | Fiber, enterprise connectivity | 19% | Yes |
| VTR | Cable, internet, phone bundles | 19% | Yes |

### 3.4 Transport and travel

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| LATAM Airlines (domestic) | Domestic flights Chile | Exempt (domestic air) | No |
| LATAM Airlines (international) | International flights | 0% (export) | No |
| Sky Airline (domestic) | Domestic budget | Exempt | No |
| Jet SMART Chile (domestic) | Domestic | Exempt | No |
| EFE (Empresa de Ferrocarriles del Estado) | Train services | Exempt | No |
| Metro de Santiago | Metro tickets | Exempt | No |
| Buses (intercity — Tur-Bus, Pullman Bus) | Long-distance buses | Exempt | No |
| Uber Chile | Ride-hailing | 19% | Yes (business use) |
| Cabify Chile | Ride-hailing | 19% | Yes (business use) |

### 3.5 Fuel

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| COPEC | Fuel (petrol/diesel) | 19% + specific impuesto | Yes (business vehicles) |
| Enex | Fuel stations | 19% + specific impuesto | Yes |
| Petrobras Chile | Fuel | 19% | Yes |
| Shell Chile | Fuel | 19% | Yes |

### 3.6 Logistics and courier

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Chilexpress | Domestic courier | 19% | Yes |
| StarKen | Domestic freight | 19% | Yes |
| DHL Chile | International courier | 0% (export) / 19% (domestic) | Yes |
| FedEx Chile | International courier | 0% / 19% | Yes |
| Correos de Chile | State postal service | 19% | Yes |
| Blue Express | E-commerce delivery | 19% | Yes |

### 3.7 Retail and office supplies

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Falabella (retail) | Department store — mixed goods | 19% | Yes |
| Ripley | Department store | 19% | Yes |
| Jumbo (Cencosud) | Supermarket | 19% | Yes |
| Unimarc | Grocery | 19% | Yes |
| Office Depot Chile | Office supplies | 19% | Yes |
| Sodimac | Hardware, office furniture | 19% | Yes |

### 3.8 Software and digital services

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Nubox | Cloud accounting for SMEs | 19% | Yes |
| Bsale | POS and invoicing software | 19% | Yes |
| Defontana | ERP — Chilean SMEs | 19% | Yes |
| Siigo Chile | Accounting platform | 19% | Yes |
| Microsoft Chile (Azure, M365) | Cloud — B2B | 19% (SII simplified scheme) | Yes |
| Google Chile (Workspace, Ads) | Digital — B2B | 19% (SII scheme) | Yes |
| Zoom Chile | Video — B2B | 19% (SII scheme) | Yes |
| AWS Chile | Cloud — B2B | 19% (SII scheme) | Yes |
| Netflix Chile | Streaming — B2C | 19% | No (B2C) |

### 3.9 Professional services

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Contador auditor / CPA | Accounting, audit, tax | 19% | Yes |
| Estudio de abogados | Legal services | 19% | Yes |
| Agencia de publicidad | Advertising | 19% | Yes |
| Consultoría empresarial | Management consulting | 19% | Yes |
| Notaría | Notarial services | 19% | Yes |

### 3.10 Insurance and healthcare

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Banco Estado Seguros | Business insurance | Exempt | No |
| Metlife Chile | Life, health insurance | Exempt | No |
| Clínica privada / hospital | Private medical | Exempt | No |
| Isapre (health fund) | Healthcare contributions | Exempt | No |
| Farmacia Cruz Verde / Salcobrand | Medicines | Exempt (medicines) | No |

---

## Section 4 — Worked examples

### Example 1 — Standard IVA on consulting

**Scenario:** Santiago consulting firm issues Factura Electrónica to Chilean corporate.

**Bank statement line (Banco de Chile format):**
```
Fecha       : 15/04/2025
Tipo        : Abono / Transferencia Electrónica
Descripción : ACME LTDA — HONORARIOS CONSULTORÍA — FCTE N°123456
Monto       : +$23.800.000
```

**Working:**
- Factura Electrónica: net $20,000,000 + IVA 19% $3,800,000 = $23,800,000
- Return entry: Code 502 — $20,000,000 | Code 503 (débito fiscal): $3,800,000

*Note: CLP amounts use period as thousands separator; no decimal places commonly shown*

---

### Example 2 — Export of services (0%)

**Scenario:** Chilean software firm exports SaaS to US client — USD wire.

**Bank statement line (BancoEstado format):**
```
Fecha       : 20/04/2025
Tipo        : Abono ME — Transferencia Internacional
Descripción : TECH INC USA — SAAS SUSCRIPCION Q1 2025
Monto       : +$47.600.000 (USD 50.000)
```

**Working:**
- Export of service to foreign entity — 0% IVA
- Issue Factura de Exportación Electrónica (DTE tipo 110)
- Return entry: Code 505 — $47,600,000 | IVA: $0

---

### Example 3 — IVA on fuel (business vehicle)

**Scenario:** Company fills up business vehicle at COPEC.

**Bank statement line (Santander Chile format):**
```
Fecha       : 10/04/2025
Tipo        : Cargo / Pago con Tarjeta
Descripción : COPEC SA — ESTACION SERVICIO PROVIDENCIA
Monto       : -$119.000
```

**Working:**
- COPEC DTE: net $100,000 + IVA 19% $19,000 = $119,000
- Input credit: $19,000 if vehicle registered in company's name for business
- Return entry: Code 524 — $100,000; Code 525 (crédito fiscal): $19,000

---

### Example 4 — Non-resident digital service (SII simplified scheme)

**Scenario:** Company pays for Google Workspace (Google Chile registered under SII simplified scheme for non-residents).

**Bank statement line (BCI format):**
```
Fecha       : 05/04/2025
Tipo        : Cargo — Débito Automático
Descripción : GOOGLE CHILE LTDA — WORKSPACE BUSINESS APR 2025
Monto       : -$892.500
```

**Working:**
- Google Chile registered under SII's simplified foreign provider scheme — charges IVA directly
- DTE issued by Google: net $750,000 + IVA 19% $142,500 = $892,500
- Input credit: $142,500 if B2B (need DTE with buyer's RUT)
- Return entry: Code 524 — $750,000; Code 525: $142,500

---

### Example 5 — Domestic air transport (exempt)

**Scenario:** Employee flies Santiago–Puerto Montt on LATAM domestic.

**Bank statement line (Scotiabank format):**
```
Fecha       : 08/04/2025
Tipo        : Cargo — Pago Web
Descripción : LATAM AIRLINES — BOLETO DOMESTICO SCL-PMC
Monto       : -$185.000
```

**Working:**
- Domestic air transport in Chile — exempt from IVA
- No IVA on the ticket
- Record as exempt expenditure; no input credit
- Return entry: Not entered in IVA return — expense record only

---

### Example 6 — Monthly return summary

**Scenario:** Services company — April 2025.

| Item | Net (CLP) | IVA (CLP) |
|---|---|---|
| Domestic sales 19% | 200,000,000 | 38,000,000 |
| Export sales (0%) | 50,000,000 | 0 |
| Exempt sales | 10,000,000 | 0 |
| Total Output | 260,000,000 | 38,000,000 |
| Local purchases | 100,000,000 | 19,000,000 |
| Import VAT (customs) | 30,000,000 | 5,700,000 |
| Total Input | 130,000,000 | 24,700,000 |
| **Net IVA payable** | | **13,300,000** |

---

## Section 5 — Tier 1 rules (compressed)

**Rate assignment:**
- 19% standard: almost all goods and services
- 0%: exports of goods (DUS exportación), services exported to non-residents
- Exempt: financial services, insurance, residential rent, healthcare and medical (licensed practitioners), education, passenger transport (metro, bus, taxi, domestic air), cultural events (some), funeral services

**Input credit:**
- Credit allowed on all IVA paid on DTE purchases for taxable activities
- Must have valid DTE (Factura Electrónica) with buyer's RUT to claim credit
- Boleta (B2C receipt) does not give IVA credit breakdown — not usable for crédito fiscal
- Partial exemption (proporcionalidad): if business has both taxable and exempt sales, must apportion — escalate
- Domestic air transport is exempt — no IVA, no credit issue

**Filing mechanics:**
- File Formulario 29 monthly via SII portal by 12th of following month
- All sales require DTE (Factura Electrónica tipo 33 for B2B; Boleta Electrónica tipo 39 for B2C)
- Remanente crédito fiscal carries forward indefinitely; export refund available via SII

---

## Section 6 — Tier 2 catalogue (genuinely data-unknowable items)

| Item | Why unknowable | What to ask |
|---|---|---|
| Transport exemption | Depends on mode and route — bus/metro exempt, ride-hailing taxable, domestic air exempt | "What transport mode? Uber/Cabify (taxable) or bus/metro/domestic flight (exempt)?" |
| Fuel — business vs personal | Only business vehicle use qualifies for input credit | "Is the vehicle registered in the company's name? What % business use?" |
| Construction services | May include IVA on materials but exempt on labour — complex split | "Break down contract into materials vs labour components." |
| Real estate (first sale) | First sale of new construction subject to IVA on construction cost portion | "Is this a first sale from developer? Or resale? Get deed details." |
| Non-resident digital service | Whether provider registered under SII simplified scheme affects how IVA flows | "Did the foreign provider issue a DTE with your RUT? Or is this reverse-charge?" |
| Mixed-use property | Business portion of home office — IVA credit only on business % | "What % of property is exclusively for business?" |

---

## Section 7 — Excel working paper

**Columns:** Date | Supplier/Customer | RUT | DTE Folio | DTE Type | Net (CLP) | IVA 19% (CLP) | In/Out | Export? | Exempt? | Tier 2 flag | Notes

**Tab structure:**
1. `Output_Sales` — Facturas Electrónicas issued (débito fiscal)
2. `Input_Purchases` — Facturas Electrónicas received (crédito fiscal)
3. `Import_Customs` — IVA paid at customs (DUS)
4. `F29_Summary` — monthly Formulario 29 totals
5. `Tier2_Items` — awaiting client response

---

## Section 8 — Bank statement reading guide

### Banco de Chile format
```
Fecha       : 15/04/2025
Tipo        : Abono / Transferencia Electrónica
Descripción : COMPANY NAME — FC ELECTRONICA N°123456
Monto       : +$23.800.000
Saldo       : $123.800.000
```

### BancoEstado format
```
15/04/2025  |  Transferencia recibida  |  COMPANY NAME  |  +23.800.000  |  Saldo: 123.800.000
```

### Key patterns:
- **CLP number format:** Period = thousands separator; no decimal places for CLP (whole pesos) — $23.800.000 = CLP 23,800,000
- **Abono:** Credit (money in) — match to issued Factura Electrónica for débito fiscal
- **Cargo:** Debit (money out) — match to received Factura Electrónica for crédito fiscal
- **Abono ME:** Foreign currency credit — check for export or non-resident service
- **Débito Automático:** Direct debit — utilities, subscriptions; request DTE

---

## Section 9 — Onboarding fallback

When client cannot provide DTEs for all transactions:

1. Use bank statement amounts as IVA-inclusive totals and back-calculate:
   - Net = Total ÷ 1.19 | IVA = Total − Net
2. Apply conservative defaults: 19% output; 0% input credit without valid DTE with buyer's RUT
3. Flag all non-DTE items in Tier2_Items tab
4. Issue data request for missing folio numbers
5. Warn client: SII can disallow crédito fiscal without valid Factura Electrónica from registered contributor

---

## Section 10 — Reference material

| Resource | Reference |
|---|---|
| SII portal (Declaración F29, DTE) | https://www.sii.cl |
| DTE verification portal | https://maullin.sii.cl/cgi_dte/UF_srv_bouncer |
| Ley de IVA (DL 825/1974 and amendments) | SII — legislación |
| SII Resolución 45/2003 — DTE | SII — resoluciones |
| Non-resident digital services — SII | SII Circular 42/2020 |
| IVA exportadores — refund guide | SII — guías de usuario |


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
