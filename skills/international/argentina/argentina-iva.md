---
name: argentina-iva
description: Use this skill whenever asked to prepare, review, or classify transactions for an Argentina IVA (Impuesto al Valor Agregado) return or advise on Argentine VAT registration, filing, and AFIP compliance. Trigger on phrases like "prepare IVA return", "Argentine VAT", "IVA Argentina", "AFIP", "CUIT", or any Argentina IVA request. ALWAYS read this skill before touching any Argentina IVA work.
version: 2.0
jurisdiction: AR
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Argentina IVA (Impuesto al Valor Agregado) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Argentina (República Argentina) |
| Tax | IVA (Impuesto al Valor Agregado) |
| Currency | ARS (Argentine Peso — $) |
| Standard rate | 21% |
| Reduced rates | 10.5% (medicines, certain food products, passenger transport >100km, medical services, books, agricultural goods); 2.5% (certain agricultural goods for direct consumption) |
| Zero rate | 0% (exports of goods and services) |
| Increased rate | 27% (public utility services: electricity, gas, water, telephone — for non-residential users) |
| Exempt | Financial services, insurance, education, medical services (partial), residential rent, certain books, public passenger transport (<100km) |
| Registration threshold | No turnover threshold for Responsable Inscripto; Monotributo regime for small businesses (ARS thresholds vary by category) |
| Tax authority | AFIP (Administración Federal de Ingresos Públicos) |
| Filing portal | AFIP portal — https://www.afip.gob.ar |
| Return form | Declaración Jurada IVA (DJ IVA) |
| Filing frequency | Monthly |
| Deadline | Varies by CUIT ending digit (between 18th–23rd of following month) |
| e-Invoice | Factura Electrónica mandatory via AFIP RCEL / ARCA portal |
| CUIT | Clave Única de Identificación Tributaria — 11-digit taxpayer ID |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by Argentina-licensed CPN (Contador Público Nacional) |
| Skill version | 2.0 |

### Key DJ IVA fields

| Field | Meaning |
|---|---|
| Ventas gravadas 21% | Taxable sales at 21% (net) |
| Ventas gravadas 10.5% | Taxable sales at 10.5% (net) |
| Ventas gravadas 27% | Utility sales at 27% (net) |
| Exportaciones | Export sales (0%) |
| Ventas exentas | Exempt sales |
| IVA débito fiscal | Total output IVA |
| Compras gravadas | Taxable purchases |
| IVA crédito fiscal | Total input IVA |
| Saldo técnico | Net IVA position (débito − crédito) |
| Saldo a pagar | IVA payable (if débito > crédito) |
| Saldo a favor | Excess credit carried forward |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 21% standard |
| Unknown whether 10.5% rate applies | 21% until confirmed |
| Unknown whether utility service (electricity/gas) 27% applies | Confirm — non-residential = 27%; residential = 21% |
| Unknown whether export documentation complete | Treat as domestic 21% |
| Unknown business-use % (vehicle, phone, home) | 0% input credit |
| Unknown whether Factura Electrónica issued | No input credit until confirmed |
| Foreign digital service (B2B) | 21% reverse-charge — buyer self-assesses |
| Monotributo supplier | No IVA credit available (Monotributistas don't charge IVA) |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | ARS 10,000,000 |
| HIGH tax delta on single conservative default | ARS 2,100,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per return |
| LOW absolute net IVA position | ARS 20,000,000 |

*Note: ARS amounts depreciate rapidly — verify thresholds are still meaningful given inflation.*

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

Before starting any Argentina IVA work, obtain:

1. CUIT (11-digit taxpayer ID) and AFIP inscription as Responsable Inscripto
2. Monthly bank statements in ARS (all business accounts — Banco Nación, Galicia, Santander, etc.)
3. Facturas Electrónicas received (XML from AFIP portal or accounting system)
4. Facturas Electrónicas issued (XML or PDF with CAE — Código de Autorización Electrónico)
5. Prior month DJ IVA (for saldo a favor carried forward)
6. Bank account summaries in USD (if holding dollar-denominated accounts — note FX complexity)
7. Details of exports with AFIP export declaration (e-Declaración de exportación)

### Refusal catalogue

Refuse and escalate to a CPN for:
- Monotributo to Responsable Inscripto transition — complex back-IVA calculations
- IVA on real estate / construction (alícuota reducida especial)
- IVA retenciones y percepciones (withholding agents — AGIP, ARBA, etc.)
- Export refunds (reintegros de IVA exportación) — complex AFIP process
- IVA on financial instruments (complex exemption rules)
- IVA agropecuario (agricultural special schemes)
- Transfer pricing / IVA intercompany Argentina
- IVA in hyperinflationary context — adjustment indexing (revalúo)

---

## Section 3 — Supplier pattern library

### 3.1 Banking and financial services

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Banco de la Nación Argentina (BNA) | Bank fees, wire transfers | Exempt | No |
| Banco Galicia | Account fees, credit lines | Exempt | No |
| Santander Argentina | Commercial banking | Exempt | No |
| BBVA Argentina | Business banking fees | Exempt | No |
| Banco Macro | Regional banking | Exempt | No |
| MercadoPago (MercadoLibre) | Payment gateway — fee | 21% | Yes |
| Prisma (VISA Argentina) | Card processing | 21% | Yes |
| First Data (Fiserv Argentina) | POS terminal fee | 21% | Yes |
| Naranja X | Digital payments | 21% | Yes |
| Ualá | Digital wallet fees | 21% | Yes |

### 3.2 Electricity, gas, and utilities

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Edenor (Empresa Distribuidora Norte) | Electricity — Buenos Aires Norte | 27% (non-residential) / 21% (residential) | Yes (business) |
| Edesur (Empresa Distribuidora Sur) | Electricity — Buenos Aires Sur | 27% (non-residential) | Yes (business) |
| Metrogas | Natural gas — Buenos Aires | 27% (non-residential) | Yes (business) |
| ECOGAS | Gas — Cuyo/NEA regions | 27% (non-residential) | Yes |
| AySA (Agua y Saneamientos Argentinos) | Water — Buenos Aires | 27% (non-residential) | Yes |
| AYSA residential | Water — residential | 21% | Yes |

### 3.3 Telecommunications

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Telecom Argentina (Personal/Fibertel) | Mobile, fiber, fixed line | 21% (service) / 27% if billed as utility | Yes (business use) |
| Claro Argentina | Mobile, broadband | 21% | Yes (business use) |
| Movistar Argentina (Telefónica) | Mobile, ADSL | 21% | Yes (business use) |
| DirecTV Argentina | Satellite TV | 21% | Yes (if business subscription) |
| Arnet | Internet service | 21% | Yes |

### 3.4 Transport and travel

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Aerolíneas Argentinas | Domestic flights | 21% | Yes |
| Aerolíneas Argentinas | International flights | 0% (export) | No input applicable |
| LATAM Argentina | Domestic/international | 21% / 0% | Yes (domestic) |
| Flybondi | Domestic budget | 21% | Yes |
| JetSMART Argentina | Domestic | 21% | Yes |
| Trenes Argentinos | Train tickets | Exempt (<100km) / 10.5% (>100km) | Yes (>100km) |
| Colectivo / subte Buenos Aires | Public bus/metro (<100km) | Exempt | No |
| Uber Argentina | Ride-hailing | 21% | Yes (business) |
| Cabify Argentina | Ride-hailing | 21% | Yes (business) |

### 3.5 Logistics and courier

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| OCA (Organización Coordinadora Argentina) | Domestic courier | 21% | Yes |
| Andreani | Domestic and international courier | 21% | Yes |
| Correo Argentino | State postal service | 21% | Yes |
| DHL Argentina | International courier | 0% (export) / 21% (domestic) | Yes |
| FedEx Argentina | International courier | 0% / 21% | Yes |

### 3.6 Retail and office supplies

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Carrefour Argentina | Supermarket — food/non-food | 21%/10.5% mixed | Partial |
| Disco / Vea (Cencosud) | Supermarket | 21%/10.5% mixed | Partial |
| Rappi Argentina | Delivery platform — commission | 21% | Yes |
| MercadoLibre (marketplace) | E-commerce | 21% | Yes |
| Office supplies store | Stationery | 21% | Yes |
| Farmacity | Pharmacy — medicines | 10.5% (medicines) / 21% (other) | Yes |

### 3.7 Software and digital services

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Tango Gestión (software) | Argentine accounting/ERP | 21% | Yes |
| Bejerman | ERP for SMEs | 21% | Yes |
| Colppy | Cloud accounting | 21% | Yes |
| Nubox Argentina | Accounting software | 21% | Yes |
| Microsoft Argentina (Azure, M365) | Cloud — B2B | 21% (reverse-charge) | Yes |
| Google Argentina (Workspace, Ads) | Digital — B2B | 21% (reverse-charge) | Yes |
| Zoom Argentina | Video — B2B | 21% (reverse-charge) | Yes |
| AWS Argentina | Cloud — B2B | 21% (reverse-charge) | Yes |

### 3.8 Professional services

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| CPN (Contador Público Nacional) | Accounting, audit, tax | 21% | Yes |
| Estudio jurídico (law firm) | Legal services | 21% | Yes |
| Agencia de publicidad | Advertising | 21% | Yes |
| Consultoría | Management consulting | 21% | Yes |
| Escribanía | Notarial services | 21% | Yes |

### 3.9 Insurance

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| San Cristóbal Seguros | Property, vehicle | Exempt | No |
| Galicia Seguros | Business insurance | Exempt | No |
| Experta ART (labor risk) | Workers compensation | Exempt | No |
| Sancor Seguros | All lines | Exempt | No |
| MAPFRE Argentina | Vehicle, property | Exempt | No |

### 3.10 Medical and healthcare

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Obra social (health fund) | Healthcare contributions | Exempt | No |
| Private clinic / sanatorio | Medical treatment | Exempt (up to limit) | No |
| Pharmacy — medicines | Prescription drugs | 10.5% (OTC) / exempt (Rx) | Partial |
| Medical equipment | Devices | 10.5% | Yes |

---

## Section 4 — Worked examples

### Example 1 — Standard IVA on consulting

**Scenario:** Buenos Aires consulting firm issues Factura A to Argentine corporate.

**Bank statement line (Banco Galicia format):**
```
Fecha       : 15/04/2025
Operación   : Acreditación / Transferencia
Descripto   : ACME SA — HONORARIOS CONSULTORÍA — FC A 0001-00004123
Importe     : +$14.520.000,00
```

**Working:**
- Factura A: net $12,000,000 + IVA 21% $2,520,000 = $14,520,000
- Return entry: Ventas gravadas 21% — $12,000,000 | Débito fiscal: $2,520,000

*Note: ARS thousands use period as separator; comma = decimal: $14.520.000,00 = ARS 14,520,000.00*

---

### Example 2 — Utility bill at 27%

**Scenario:** Office electricity from Edenor — non-residential commercial account.

**Bank statement line (Santander Argentina format):**
```
Fecha       : 25/04/2025
Concepto    : Débito — Edenor SA — Factura 0041-2025-04
Importe     : -$6.350.000,00
```

**Working:**
- Edenor Factura: net $5,000,000 + IVA 27% $1,350,000 = $6,350,000
- Input credit: $1,350,000 (business premises — 100% deductible)
- Return entry: Compras gravadas 27% — $5,000,000; Crédito fiscal: $1,350,000

---

### Example 3 — Export of services (0%)

**Scenario:** Argentine tech firm exports SaaS to US client — USD payment.

**Bank statement line (BBVA Argentina format):**
```
Fecha       : 20/04/2025
Operación   : Crédito ME / Liquidación FX
Descripción : TECH INC USA — SAAS SUBSCRIPTION Q1 2025
Importe     : +$62.400.000,00 (USD 60.000)
```

**Working:**
- Export of service to foreign entity — 0% IVA
- Requires: contract, SWIFT payment evidence, AFIP export declaration
- Return entry: Exportaciones — $62,400,000 | IVA: $0

---

### Example 4 — Reverse-charge on foreign digital service

**Scenario:** Company pays for Microsoft Azure (billed from Microsoft Ireland).

**Bank statement line (Banco Nación format):**
```
Fecha       : 05/04/2025
Movimiento  : Pago Exterior — SWIFT
Descripción : MICROSOFT IRELAND — AZURE CLOUD APR 2025
Importe     : -$5.040.000,00
```

**Working:**
- Foreign digital service to Argentine Responsable Inscripto — self-assess IVA
- Self-assess: $5,040,000 × 21/121 = $875,537 IVA (or net $4,164,463 + IVA $875,537)
- Declare as output AND claim as input — net zero for fully taxable business
- Note: AFIP RG 4240 governs digital services imported by Argentine users

---

### Example 5 — Monotributo supplier (no IVA)

**Scenario:** Freelancer under Monotributo issues receipt for design work.

**Bank statement line (Galicia format):**
```
Fecha       : 12/04/2025
Operación   : Transferencia Emitida
Descripción : MARIA GARCIA — DISEÑO GRAFICO — RECIBO C 0001-00000234
Importe     : -$1.200.000,00
```

**Working:**
- Monotributista issues Recibo C (not Factura A) — does NOT charge IVA
- Input credit: $0 — Monotributistas are not IVA-registered
- Record as expense net $1,200,000 with no IVA credit
- Flag: check if supplier should be switching to Responsable Inscripto (if >annual Monotributo limit)

---

### Example 6 — Monthly return summary

**Scenario:** Services company — April 2025.

| Item | Net (ARS) | IVA (ARS) |
|---|---|---|
| Domestic sales 21% | 100,000,000 | 21,000,000 |
| Reduced rate sales 10.5% | 20,000,000 | 2,100,000 |
| Export sales (0%) | 30,000,000 | 0 |
| Total Output | 150,000,000 | 23,100,000 |
| Local purchases 21% | 50,000,000 | 10,500,000 |
| Utility bills 27% | 10,000,000 | 2,700,000 |
| Total Input | 60,000,000 | 13,200,000 |
| **Net IVA payable** | | **9,900,000** |

---

## Section 5 — Tier 1 rules (compressed)

**Rate assignment:**
- 21% standard: most goods and services
- 10.5%: medicines, some food products, books, medical services (private, up to limit), agricultural goods (primary), passenger transport >100km
- 27%: public utility services (electricity, gas, water, telephone) when supplied to non-residential customers; also applies to certain other services per AFIP resolution
- 0%: exports of goods with AFIP export declaration, services exported to non-residents
- Exempt: financial services, insurance, education (public and some private), medical services (public health and obra social), residential rent, public transport <100km, certain books

**Input credit:**
- Credit allowed on all IVA paid on purchases for taxable activities
- No credit from Monotributistas (they issue Recibo C, not Factura A)
- Factura A: B2B — must have buyer's CUIT; allows input credit
- Factura B: B2C — no IVA breakdown; buyer cannot claim input credit
- Factura C: Monotributo — no IVA; no input credit
- Vehicle: partial rules — check AFIP RG for deductible %
- Foreign digital services: AFIP RG 4240 — buyer self-assesses under reverse-charge

**Filing mechanics:**
- File DJ IVA monthly via AFIP portal; deadline varies by CUIT last digit (18th–23rd)
- All sales invoices must have CAE (Código de Autorización Electrónico) from AFIP
- Saldo a favor carries forward indefinitely; export refunds available but slow

---

## Section 6 — Tier 2 catalogue (genuinely data-unknowable items)

| Item | Why unknowable | What to ask |
|---|---|---|
| Utility rate (21% vs 27%) | Depends on whether account is residential or non-residential | "Is the utility account registered as residential (domicilio) or commercial/industrial?" |
| Food product rate | 21% vs 10.5% depends on product type and processing | "What is the exact product? Is it a primary agricultural product or processed?" |
| Transport rate | Exempt (<100km) vs 10.5% (>100km) for passenger | "What is the route distance? Is this passenger or freight transport?" |
| Vehicle purchase | AFIP RG limits input credit on passenger vehicles | "What is the vehicle type? Commercial or passenger? Purchase price?" |
| Home office | Business proportion unknown | "What % of your home is used exclusively for business?" |
| Supplier regime | Responsable Inscripto (IVA credit allowed) vs Monotributista (no credit) | "Confirm supplier's AFIP tax regime — RI or Monotributo?" |
| Export qualification | Whether service truly consumed outside Argentina | "Where is the client? Evidence of offshore consumption?" |

---

## Section 7 — Excel working paper

**Columns:** Date | Supplier/Customer | CUIT | Invoice No. (CAE) | Factura Type (A/B/C) | Net (ARS) | IVA Rate % | IVA (ARS) | In/Out | Export? | Exempt? | Tier 2 flag | Notes

**Tab structure:**
1. `Output_Sales` — ventas (Facturas A/B)
2. `Input_Purchases` — compras (Facturas A only for credit)
3. `ReverseCharge_Digital` — foreign digital services
4. `IVA_Summary` — monthly DJ IVA totals
5. `Tier2_Items` — awaiting client response

---

## Section 8 — Bank statement reading guide

### Banco Galicia format
```
Fecha       : 15/04/2025
Operación   : Acreditación / Transferencia
Descripción : COMPANY NAME — FC A 0001-00004123
Importe     : +$14.520.000,00
Saldo       : $64.520.000,00
```

### Banco Nación format
```
15/04/2025  |  Crédito  |  COMPANY NAME — HONORARIOS  |  +14.520.000,00  |  Saldo: 64.520.000,00
```

### Key patterns:
- **ARS number format:** Period = thousands; comma = decimal ($14.520.000,00 = ARS 14,520,000.00)
- **FC A / Factura A:** B2B invoice — buyer can claim IVA input credit
- **Recibo C:** Monotributo supplier — no IVA credit available
- **Débito — AFIP:** AFIP direct debit — may include IVA payment or other taxes
- **Pago Exterior / SWIFT:** Foreign payment — check reverse-charge or export

---

## Section 9 — Onboarding fallback

When client cannot provide Facturas Electrónicas for all transactions:

1. Use bank statement amounts as IVA-inclusive totals and back-calculate:
   - Net = Total ÷ 1.21 | IVA = Total − Net (for 21% rate)
   - Net = Total ÷ 1.10.5 = Total ÷ 1.105 (for 10.5%)
   - Net = Total ÷ 1.27 (for 27% utilities)
2. Conservative defaults: 21% output; 0% input credit without CAE-validated Factura A
3. Flag all non-A-invoices in Tier2_Items tab
4. Issue data request for missing CAE references
5. Warn client: AFIP can disallow input credit without valid Factura A from Responsable Inscripto supplier

---

## Section 10 — Reference material

| Resource | Reference |
|---|---|
| AFIP portal (filing, Factura Electrónica) | https://www.afip.gob.ar |
| AFIP RCEL (Régimen de Emisión de Comprobantes) | afip.gob.ar — Factura Electrónica section |
| Ley de IVA (Ley 23.349 and amendments) | AFIP legislation library |
| AFIP RG 4240 — digital services | afip.gob.ar — resoluciones generales |
| AFIP RG 4290 — e-invoice expansion | Official Gazette |
| IVA rates (Decreto 280/97 and updates) | AFIP — tablas de alícuotas |


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
