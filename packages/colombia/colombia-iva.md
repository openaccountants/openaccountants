---
name: colombia-iva
description: Use this skill whenever asked to prepare, review, or classify transactions for a Colombia IVA (Impuesto sobre las Ventas) return or advise on Colombian VAT registration, filing, and DIAN compliance. Trigger on phrases like "prepare IVA return Colombia", "Colombian VAT", "IVA Colombia", "DIAN", "NIT", or any Colombia IVA request. ALWAYS read this skill before touching any Colombia IVA work.
version: 2.0
jurisdiction: CO
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Colombia IVA (Impuesto sobre las Ventas) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Colombia (República de Colombia) |
| Tax | IVA — Impuesto sobre las Ventas (VAT) |
| Currency | COP (Colombian Peso — $) |
| Standard rate | 19% |
| Reduced rates | 5% (medicines, medical devices, agricultural inputs, passenger air transport, accommodation); 0% (basic foods — pan, arroz, leche, huevos, etc.) |
| Zero rate | 0% (exports of goods, certain services exported to non-residents) |
| Exempt | Financial services, insurance, education, healthcare, public utilities (residential), land transport, books, newspapers |
| Registration threshold | Responsable de IVA: annual income ≥ COP 96,000,000 (UVT × 3,500 for 2025) or other conditions; below = No Responsable de IVA (formerly "Régimen Simplificado") |
| Tax authority | DIAN (Dirección de Impuestos y Aduanas Nacionales) |
| Filing portal | DIAN portal — https://www.dian.gov.co (MUISCA system) |
| Return form | Declaración del Impuesto sobre las Ventas (Formulario 300) |
| Filing frequency | Bimonthly (Jan–Feb, Mar–Apr, May–Jun, Jul–Aug, Sep–Oct, Nov–Dec) for Responsables |
| Deadline | Varies by NIT — typically 10th–23rd of month following period end |
| e-Invoice | Factura Electrónica mandatory (DIAN authorized — habilitación previa) |
| NIT | Número de Identificación Tributaria — Colombian taxpayer ID |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by Colombia-licensed Contador Público |
| Skill version | 2.0 |

### Key Formulario 300 fields

| Field | Meaning |
|---|---|
| Casilla 27 | Total taxable sales 19% |
| Casilla 28 | Total taxable sales 5% |
| Casilla 29 | Total exports |
| Casilla 30 | Total excluded/exempt |
| Casilla 67 | IVA generado (output IVA) |
| Casilla 82 | IVA descontable (input IVA — purchases) |
| Casilla 88 | Retención IVA a favor (IVA withholding received) |
| Casilla 89 | Saldo a pagar (net IVA payable) |
| Casilla 92 | Saldo a favor (excess credit carried forward) |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 19% standard |
| Unknown whether 5% rate applies | 19% until confirmed |
| Unknown whether food is zero-rated basic or not | 0% if unprocessed basic; 19% if processed/restaurant |
| Unknown whether export documentation complete | Treat as domestic 19% |
| Unknown business-use % (vehicle, phone, home) | 0% input credit |
| Unknown whether Factura Electrónica issued | No input credit until confirmed |
| Foreign digital service | 19% — DIAN requires foreign providers to register |
| No Responsable supplier | No IVA credit (they do not charge IVA) |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | COP 50,000,000 |
| HIGH tax delta on single conservative default | COP 9,500,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per return |
| LOW absolute net IVA position | COP 100,000,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

Before starting any Colombia IVA work, obtain:

1. NIT (Número de Identificación Tributaria) and RUT (Registro Único Tributario) certificate
2. Bimonthly bank statements in COP (all business accounts)
3. Facturas Electrónicas issued (XML from DIAN-authorized software with CUFE — Código Único de Factura Electrónica)
4. Facturas Electrónicas received from suppliers (with CUFE)
5. Prior period Formulario 300 (for saldo a favor carried forward)
6. Import customs declarations (Declaración de Importación) from DIAN Customs
7. Retención en la fuente de IVA certificates (if subject to withholding)

### Refusal catalogue

Refuse and escalate to a Contador Público for:
- Prorrata / proporcionalidad (partial exemption for mixed taxable/exempt businesses)
- IVA en construcción (complex rules on real estate and construction)
| IVA retenciones — complex agent cases
- IVA refund for exporters — DIAN process is complex
- Free trade zones (Zonas Francas) — special IVA treatment
- Industria y Comercio (ICA) — separate municipal tax, not IVA
- Impuesto Nacional al Consumo (INC) — separate consumption tax on restaurants, vehicles

---

## Section 3 — Supplier pattern library

### 3.1 Banking and financial services

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Bancolombia | Bank fees, transfers | Exempt | No |
| Davivienda | Account fees, loans | Exempt | No |
| Banco de Bogotá | Commercial banking | Exempt | No |
| Banco Popular | Business banking | Exempt | No |
| BBVA Colombia | Corporate banking | Exempt | No |
| Nequi (Bancolombia) | Digital wallet | Exempt (payment) | No |
| Daviplata (Davivienda) | Mobile money | Exempt | No |
| PayU Colombia | Payment gateway — commission | 19% | Yes |
| ePayco | Digital payments | 19% | Yes |
| Wompi (Bancolombia) | E-commerce payments | 19% | Yes |

### 3.2 Electricity and utilities

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Grupo EPM (EPM Medellín) | Electricity — Medellín/Antioquia | 0% (residential) / 19% (non-residential commercial) | Yes (business) |
| Codensa (Enel Colombia) | Electricity — Bogotá | 19% (non-residential) | Yes (business) |
| Electricaribe / Air-e | Electricity — Caribbean coast | 19% (commercial) | Yes |
| Gas Natural Fenosa Colombia | Natural gas | 0% (residential) / 19% (commercial) | Yes |
| Triple A | Water — Barranquilla | 0% (residential) | No (residential) |
| EAAB (Acueducto Bogotá) | Water — Bogotá | 0% (residential) | No (residential) |

### 3.3 Telecommunications

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Claro Colombia | Mobile, internet, TV | 19% | Yes (business use) |
| Movistar Colombia (Telefónica) | Mobile, broadband | 19% | Yes (business use) |
| Tigo Colombia | Mobile, cable | 19% | Yes (business use) |
| ETB (Empresa de Telecomunicaciones de Bogotá) | Fixed line, fiber | 19% | Yes |
| DirecTV Colombia | Satellite TV | 19% | Yes (business) |
| UNE (EPM Telecomunicaciones) | Fiber, mobile — Medellín | 19% | Yes |

### 3.4 Transport and travel

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Avianca | Domestic flights | 5% (passenger air) | Yes |
| Avianca | International flights | 0% (export) | No |
| LATAM Colombia | Domestic/international | 5% / 0% | Yes (domestic) |
| Viva Air Colombia | Domestic | 5% | Yes |
| Transmilenio (Bogotá BRT) | Bus rapid transit | Exempt | No |
| Metro de Medellín | Metro | Exempt | No |
| Uber Colombia | Ride-hailing | 19% | Yes (business use) |
| InDriver Colombia | Ride-hailing | 19% | Yes |
| Intermunicipal bus | Long-distance bus | Exempt | No |

### 3.5 Logistics and courier

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Servientrega | Domestic courier | 19% | Yes |
| Coordinadora | Domestic courier | 19% | Yes |
| TCC (Transportes Cargo Colombia) | Domestic freight | 19% | Yes |
| DHL Colombia | International courier | 0% (export) / 19% (domestic) | Yes |
| FedEx Colombia | International courier | 0% / 19% | Yes |
| Efecty (Bancolombia) | Cash courier / payment | 19% (service fee) | Yes |

### 3.6 Retail and office supplies

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Éxito (Grupo Éxito) | Supermarket — mixed | 19%/5%/0% mixed | Partial |
| Jumbo Colombia (Cencosud) | Supermarket | Mixed | Partial |
| Rappi Colombia | Delivery platform — commission | 19% | Yes |
| Mercado Libre Colombia | E-commerce | 19% | Yes |
| Office Depot Colombia | Office supplies | 19% | Yes |
| Alkosto / Ktronix | Electronics, home | 19% | Yes |

### 3.7 Software and digital services

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Siigo Colombia | Cloud accounting (SME leader) | 19% | Yes |
| World Office | ERP Colombia | 19% | Yes |
| ContaFácil | Accounting software | 19% | Yes |
| Alegra Colombia | Invoicing, accounting | 19% | Yes |
| Microsoft Colombia (Azure, M365) | Cloud — B2B | 19% (DIAN-registered foreign provider) | Yes |
| Google Colombia (Workspace, Ads) | Digital — B2B | 19% (DIAN-registered) | Yes |
| Zoom Colombia | Video — B2B | 19% | Yes |
| AWS Colombia | Cloud — B2B | 19% | Yes |
| Netflix Colombia | Streaming — B2C | 19% | No (B2C) |

### 3.8 Professional services

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Contador Público | Accounting, audit, tax | 19% | Yes |
| Firma de abogados | Legal services | 19% | Yes |
| Agencia de publicidad | Advertising | 19% | Yes |
| Empresa de consultoría | Management consulting | 19% | Yes |
| Luker (chocolates — example B2B) | FMCG distributor | 19% | Yes |

### 3.9 Insurance

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Suramericana (SURA) | All lines | Exempt | No |
| Bolívar Seguros | Property, liability | Exempt | No |
| Colseguros (Allianz) | Business insurance | Exempt | No |
| Liberty Colombia | Motor, property | Exempt | No |

### 3.10 Basic food (0% IVA)

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Unilever Colombia (basic foods) | Aceite, margarina | 0% | No (0-rate) |
| Alpina | Leche, queso, yogur | 0% | No |
| Nutresa (Colanta, etc.) | Basic dairy products | 0% | No |
| Arroz / pan / huevos / sal | Unprocessed staples | 0% | No |

---

## Section 4 — Worked examples

### Example 1 — Standard IVA on consulting

**Scenario:** Bogotá consulting firm issues Factura Electrónica to Colombian corporate.

**Bank statement line (Bancolombia format):**
```
Fecha       : 15/04/2025
Tipo        : Abono — Transferencia Electrónica
Descripción : ACME SA — HONORARIOS CONSULTORÍA — FE CUFE: AB12...
Valor       : +$119.000.000
Saldo       : $619.000.000
```

**Working:**
- Factura Electrónica: net $100,000,000 + IVA 19% $19,000,000 = $119,000,000
- Return entry: Casilla 27 — $100,000,000 | Casilla 67 (IVA generado): $19,000,000

*Note: COP amounts use period as thousands separator: $119.000.000 = COP 119,000,000*

---

### Example 2 — Reduced rate (5%) domestic flight

**Scenario:** Employee flies Bogotá–Medellín on Avianca.

**Bank statement line (Davivienda format):**
```
Fecha       : 10/04/2025
Tipo        : Débito — Pago online
Descripción : AVIANCA SA — TIQUETE BOG-MDE APR 2025
Valor       : -$472.500
```

**Working:**
- Domestic flight ticket: net $450,000 + IVA 5% $22,500 = $472,500
- Input credit: $22,500 (business travel — documented purpose required)
- Return entry: Casilla 28 — $450,000; Input IVA 5%: $22,500

---

### Example 3 — Zero-rated basic food

**Scenario:** Company purchases rice and eggs for cafetería.

**Bank statement line (Banco de Bogotá format):**
```
Fecha       : 08/04/2025
Tipo        : Débito — Pago POS
Descripción : ALMACENES EXITO SA — BOGOTA
Valor       : -$2.500.000
```

**Working:**
- Éxito receipt: rice $800,000 (0%) + eggs $400,000 (0%) + other items $1,300,000 (19%) = $2,500,000
- Input credit on 19% portion: $1,300,000 × 19/119 = $207,563
- Zero-rated items: no IVA credit applicable; not in IVA return

---

### Example 4 — Export of services (0%)

**Scenario:** Colombian IT company exports software development services to US client.

**Bank statement line (Bancolombia format):**
```
Fecha       : 20/04/2025
Tipo        : Abono ME — Reintegro Divisas
Descripción : TECH CORP USA — SOFTWARE DEV SERVICES Q1 2025
Valor       : +$380.000.000 (USD 95.000)
```

**Working:**
- Export of services consumed outside Colombia — 0% IVA
- Issue Factura de Exportación Electrónica; file with DIAN
- Return entry: Casilla 29 — $380,000,000 | IVA: $0

---

### Example 5 — IVA retenida (withholding)

**Scenario:** Company sells services to a gran contribuyente who retains 50% IVA.

**Bank statement line (BBVA format):**
```
Fecha       : 25/04/2025
Tipo        : Abono — Transferencia
Descripción : GRAN EMPRESA SA — FE INV-2025-041 NETO RETENCION IVA
Valor       : +$109.500.000
```

**Working:**
- Invoice: net $100,000,000 + IVA 19% $19,000,000 = $119,000,000
- Gran contribuyente retains 50% IVA = $9,500,000; pays balance: $109,500,000
- Output IVA: $19,000,000; Less retención received: $9,500,000
- Casilla 88 (retención a favor): $9,500,000

---

### Example 6 — Bimonthly return summary (Mar–Apr 2025)

| Item | Net (COP) | IVA (COP) |
|---|---|---|
| Domestic sales 19% | 800,000,000 | 152,000,000 |
| Domestic sales 5% | 50,000,000 | 2,500,000 |
| Export sales (0%) | 100,000,000 | 0 |
| Total Output | 950,000,000 | 154,500,000 |
| Input IVA on purchases | 400,000,000 | 76,000,000 |
| Retención IVA received | — | 15,000,000 |
| Total Input + Retención | | 91,000,000 |
| **Net IVA payable** | | **63,500,000** |

---

## Section 5 — Tier 1 rules (compressed)

**Rate assignment:**
- 19% standard: most goods and services not listed below
- 5%: domestic passenger air transport, accommodation/lodging, agricultural inputs, some medicines and medical devices
- 0% (excluido/zero-rated): basic unprocessed foods (arroz, maíz, papa, sal, panela, leche, huevos, carne/pescado sin procesar), books, water supply (residential), agricultural animals
- Exempt: financial services, insurance, education, healthcare (licensed practitioners), public utilities (residential electricity/gas), land transport, newspapers, public passenger transport

**Input credit:**
- Credit allowed on 19% and 5% purchases for taxable activities
- Must have Factura Electrónica with CUFE from Responsable de IVA supplier
- No credit from No Responsable suppliers (they do not charge IVA)
- No credit on excluido (0%) purchases or exempt purchases
- IVA retenida: gran contribuyentes and retención agents withhold 15% or 50% of IVA — offset against payable

**Filing mechanics:**
- File Formulario 300 bimonthly via DIAN MUISCA; deadline varies by NIT last digit
- All B2B sales require Factura Electrónica with CUFE (DIAN-authorized software)
- Saldo a favor carries forward; exporters can request refund after filing

---

## Section 6 — Tier 2 catalogue (genuinely data-unknowable items)

| Item | Why unknowable | What to ask |
|---|---|---|
| Utility rate | Residential (0%) vs commercial/industrial (19%) depends on usage classification | "Is the utility account registered for residential or commercial use? Provide contract." |
| Food product (0% vs 19%) | Processed vs unprocessed distinction; restaurant meals (19%) vs basic food (0%) | "Is this a basic unprocessed food? Or restaurant service / processed packaged product?" |
| Air transport (5% vs 0%) | Domestic (5%) vs international (0%) | "What is the route? Domestic Colombia or international?" |
| Supplier regime | Responsable (IVA charged, credit allowed) vs No Responsable | "Confirm supplier's RUT — Responsable de IVA or No Responsable?" |
| Business-use vehicle | DIAN limits on passenger vehicle IVA | "Vehicle type and business use %" |
| Export documentation | Zero-rate requires DIAN export declaration | "Provide export invoice and DIAN export authorization." |

---

## Section 7 — Excel working paper

**Columns:** Date | Supplier/Customer | NIT | CUFE | Net (COP) | IVA Rate % | IVA (COP) | In/Out | Zero-rated? | Exempt? | Retención IVA? | Tier 2 flag | Notes

**Tab structure:**
1. `Output_Sales` — Facturas Electrónicas issued
2. `Input_Purchases` — Facturas Electrónicas received
3. `F300_Summary` — bimonthly return totals
4. `Tier2_Items` — awaiting client response

---

## Section 8 — Bank statement reading guide

### Bancolombia format
```
Fecha       : 15/04/2025
Tipo        : Abono — Transferencia Electrónica
Descripción : COMPANY NAME — FE INV-2025-041
Valor       : +$119.000.000
Saldo       : $619.000.000
```

### Davivienda format
```
15/04/2025  |  Crédito  |  COMPANY NAME  |  +119.000.000  |  Saldo: 619.000.000
```

### Key patterns:
- **COP number format:** Period = thousands; no decimal (whole pesos): $119.000.000 = COP 119,000,000
- **Abono:** Credit (money in) — match to issued Factura Electrónica
- **Débito:** Debit (money out) — match to received Factura for input credit
- **Reintegro Divisas:** Foreign currency conversion — export or foreign service

---

## Section 9 — Onboarding fallback

When client cannot provide Facturas Electrónicas for all transactions:

1. Use bank statement amounts as IVA-inclusive and back-calculate:
   - Net = Total ÷ 1.19 | IVA = Total − Net
   - Net = Total ÷ 1.05 (5% rate)
2. Conservative defaults: 19% output; 0% input credit without CUFE-valid Factura Electrónica
3. Flag all items without CUFE in Tier2_Items
4. Issue data request for missing invoice references
5. Warn client: DIAN can disallow input credit without Factura Electrónica with valid CUFE

---

## Section 10 — Reference material

| Resource | Reference |
|---|---|
| DIAN portal (MUISCA system) | https://www.dian.gov.co |
| Estatuto Tributario (IVA — Artículos 420–512) | DIAN — legislación |
| Resolución DIAN 000042/2020 — Factura Electrónica | DIAN — resoluciones |
| IVA rate schedule | DIAN — tarifas IVA |
| Retención en fuente IVA | DIAN — retención IVA guidance |
| UVT (Unidad de Valor Tributario) — annual update | DIAN resolution each December |


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
