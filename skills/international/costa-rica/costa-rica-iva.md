---
name: costa-rica-iva
description: Use this skill whenever asked to prepare, review, or classify transactions for a Costa Rica IVA (Impuesto al Valor Agregado) return or advise on Costa Rican VAT registration, filing, and Hacienda compliance. Trigger on phrases like "prepare IVA return Costa Rica", "Costa Rica VAT", "IVA Costa Rica", "Hacienda", "CÉDULA jurídica", or any Costa Rica IVA request. ALWAYS read this skill before touching any Costa Rica IVA work.
version: 2.0
jurisdiction: CR
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Costa Rica IVA (Impuesto al Valor Agregado) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Costa Rica (República de Costa Rica) |
| Tax | IVA — Impuesto al Valor Agregado (effective July 2019, replacing historic sales tax) |
| Currency | CRC (Costa Rican Colón — ₡) |
| Standard rate | 13% |
| Reduced rates | 4% (private medical services and medicines); 2% (private educational services, agricultural inputs); 1% (basic food basket — canasta básica — specified items) |
| Zero rate | 0% (exports of goods and services) |
| Exempt | Public education, public healthcare, financial services, insurance, residential rent (≤ ₡750,000/month), international transport |
| Registration threshold | No threshold — any business making taxable supplies in Costa Rica must register |
| Tax authority | Ministerio de Hacienda (DGT — Dirección General de Tributación) |
| Filing portal | ATV (Administración Tributaria Virtual) — https://www.hacienda.go.cr |
| Return form | Declaración del IVA (Form D-104) |
| Filing frequency | Monthly |
| Deadline | 15th of the following month |
| e-Invoice | Factura Electrónica mandatory (sistema Hacienda XML v4.3) |
| Cédula jurídica | Costa Rican company taxpayer ID (e.g., 3-101-123456) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by Costa Rica-licensed CPA (Contador Público Autorizado) |
| Skill version | 2.0 |

### Key D-104 fields

| Field | Meaning |
|---|---|
| Línea 1 | Taxable sales at 13% (net) |
| Línea 2 | Taxable sales at 4% (net) |
| Línea 3 | Taxable sales at 2% (net) |
| Línea 4 | Taxable sales at 1% (net) |
| Línea 5 | Export sales (0%) |
| Línea 6 | Exempt sales |
| Línea 7 | Total IVA débito fiscal (output) |
| Línea 8 | IVA crédito fiscal on purchases 13% |
| Línea 9 | IVA crédito fiscal on purchases 4%/2%/1% |
| Línea 10 | Net IVA payable (7 − 8 − 9; if positive) |
| Línea 11 | Remanente crédito fiscal (excess credit c/f) |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 13% standard |
| Unknown whether 4% medical rate applies | 13% until confirmed |
| Unknown whether canasta básica 1% applies | 1% only if item is on official DGT list |
| Unknown whether export documentation complete | Treat as domestic 13% |
| Unknown business-use % (vehicle, phone, home) | 0% input credit |
| Unknown whether Factura Electrónica issued | No input credit until confirmed |
| Foreign digital service (B2B) | 13% — buyer self-assesses if provider not registered in CR |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | CRC 50,000,000 |
| HIGH tax delta on single conservative default | CRC 6,500,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per return |
| LOW absolute net IVA position | CRC 100,000,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

Before starting any Costa Rica IVA work, obtain:

1. Cédula jurídica (company) or cédula física (individual) and Hacienda registration
2. Monthly bank statements in CRC and USD (many businesses operate in both)
3. Facturas Electrónicas issued (XML from Hacienda system — key: clave numérica 50 digits)
4. Facturas Electrónicas received (XML or PDF with clave numérica)
5. Prior month D-104 (for remanente crédito fiscal)
6. Import declarations for imported goods
7. Details of exempt activities (residential rent, financial services)

### Refusal catalogue

Refuse and escalate to a CPA for:
- Prorrata (partial exemption for mixed taxable/exempt businesses)
- IVA on real estate sales (complex — only taxable if developer)
- Régimen de Tributación Simplificada — separate simplified regime
- IVA on financial instruments and leasing
- Free trade zone (Zonas Francas) — exempt from IVA
- Non-resident digital service provider registration

---

## Section 3 — Supplier pattern library

### 3.1 Banking and financial services

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Banco Nacional de Costa Rica (BNCR) | Bank fees, transfers | Exempt | No |
| Banco de Costa Rica (BCR) | Account fees, corporate banking | Exempt | No |
| BAC Credomatic | Commercial banking | Exempt | No |
| Scotiabank Costa Rica | Business banking | Exempt | No |
| Davivienda CR | Banking services | Exempt | No |
| Promerica | Regional banking | Exempt | No |
| SINPE Móvil (BNCR) | P2P payments | Exempt | No |
| PayRetailers | Payment gateway | 13% | Yes |
| Cuentas Simples / ePagos CR | Digital payments | 13% | Yes |

### 3.2 Electricity, water, and utilities

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| ICE (Instituto Costarricense de Electricidad) | Electricity + telecom | 13% | Yes (business) |
| CNFL (Compañía Nacional de Fuerza y Luz) | Electricity — San José metro | 13% | Yes (business) |
| ESPH (Empresa de Servicios Públicos de Heredia) | Electricity/water — Heredia | 13% | Yes |
| AYA (Instituto Costarricense de Acueductos y Alcantarillados) | Water — national | 13% | Yes (business) |
| JASEC (Junta Administrativa de Servicios Eléctricos) | Electricity — Cartago | 13% | Yes |

### 3.3 Telecommunications

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| ICE / Kölbi | Mobile, broadband (state operator) | 13% | Yes (business use) |
| Claro Costa Rica | Mobile, internet | 13% | Yes (business use) |
| Movistar Costa Rica | Mobile, ADSL | 13% | Yes (business use) |
| Liberty Costa Rica (formerly CableTica) | Cable TV, internet | 13% | Yes (business) |
| Tigo Business CR | Enterprise connectivity | 13% | Yes |

### 3.4 Transport and travel

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| LACSA / Avianca Costa Rica | Domestic / international flights | 0% (international) | No |
| Nature Air / Skyway CR | Domestic feeder flights | 13% | Yes |
| SANSA (domestic) | Domestic air | 13% | Yes |
| INCOFER (train) | San José suburban train | Exempt | No |
| Bus (SACSA, TUAN) | Intercity bus | Exempt | No |
| Uber Costa Rica | Ride-hailing | 13% | Yes (business use) |
| InDriver CR | Ride-hailing | 13% | Yes |

### 3.5 Fuel

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| RECOPE (Refinadora Costarricense de Petróleo) | Fuel at stations — DELTA, PUMA, etc. | 13% | Yes (business vehicles) |
| PUMA Energy CR | Fuel | 13% | Yes |
| Delta (RECOPE distributor) | Fuel stations | 13% | Yes |

### 3.6 Logistics and courier

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Correos de Costa Rica | State postal | 13% | Yes |
| DHL Costa Rica | International courier | 0% (export) / 13% (domestic) | Yes |
| FedEx Costa Rica | International courier | 0% / 13% | Yes |
| Aerocasillas | Miami-San José parcel service | 13% | Yes |
| Jetbox (Ocaso) | International parcel service | 13% | Yes |

### 3.7 Retail and office supplies

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Walmart / Maxi Palí | Supermarket — mixed | 13%/1% mixed | Partial |
| AutoMercado | Premium grocery | 13%/1% mixed | Partial |
| Supermercados BM | Grocery | Mixed | Partial |
| Office Depot CR | Office supplies | 13% | Yes |
| Importaciones Mundiales | Hardware, office | 13% | Yes |
| Farmacia Fischel / Sucre | Pharmacy — medicines (4%) | 4% | Yes |

### 3.8 Software and digital services

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| Soft Expert (Sistemas) | ERP for SMEs | 13% | Yes |
| CONTPAQi CR | Accounting software | 13% | Yes |
| Alegra CR | Cloud invoicing | 13% | Yes |
| FacturaDirecta | e-Invoice SaaS | 13% | Yes |
| Microsoft CR (Azure, M365) | Cloud — B2B | 13% (CR-registered or reverse-charge) | Yes |
| Google CR (Workspace, Ads) | Digital — B2B | 13% | Yes |
| Zoom CR | Video — B2B | 13% | Yes |
| AWS CR (Amazon) | Cloud — B2B | 13% | Yes |

### 3.9 Professional services

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| CPA (Contador Público Autorizado) | Accounting, audit, tax | 13% | Yes |
| Firma de abogados | Legal services | 13% | Yes |
| Agencia de publicidad | Advertising | 13% | Yes |
| Consultora empresarial | Consulting | 13% | Yes |
| Notaría | Notarial services | 13% | Yes |

### 3.10 Medical and insurance

| Supplier | Typical description | IVA rate | Input credit |
|---|---|---|---|
| CCSS (Caja Costarricense de Seguro Social) | Public healthcare | Exempt | No |
| Private clinic / hospital | Private medical | 4% | Yes |
| Pharmacy (medicines) | Prescription and OTC | 4% | Yes |
| INS (Instituto Nacional de Seguros) | Insurance | Exempt | No |
| ASSA CR | Private insurance | Exempt | No |

---

## Section 4 — Worked examples

### Example 1 — Standard IVA on consulting

**Scenario:** San José consulting firm issues Factura Electrónica to Costa Rican corporate.

**Bank statement line (Banco Nacional format):**
```
Fecha       : 15/04/2025
Tipo        : Crédito — SINPE / Transferencia
Descripción : TECH SA — FACT ELECT 50401012500310100010100000123456789 HONORARIOS
Monto       : ₡14.700.000,00
```

**Working:**
- Factura Electrónica: net ₡13,000,000 + IVA 13% ₡1,690,000 = ₡14,690,000 (rounding note)
- Return entry: Línea 1 — ₡13,000,000 | Output IVA: ₡1,690,000

*Note: CRC amounts use comma for decimal: ₡14.700.000,00 = CRC 14,700,000.00*

---

### Example 2 — Canasta básica (1% rate)

**Scenario:** Office buys basic food for staff cafetería at Walmart.

**Bank statement line (BCR format):**
```
Fecha       : 10/04/2025
Tipo        : Débito — POS
Descripción : WALMART CR — MAXI PALI HEREDIA
Monto       : -₡850.000,00
```

**Working:**
- Walmart receipt: rice, beans, eggs, oil = ₡600,000 × 1% = ₡5,941 IVA; other items ₡250,000 × 13% = ₡28,761 IVA
- Total IVA: ₡34,702 — partial input credit on business items
- Canasta básica items: only those on DGT official list qualify for 1%

---

### Example 3 — ICE electricity + telecom

**Scenario:** Company pays ICE for office electricity and internet bundle.

**Bank statement line (BAC Credomatic format):**
```
Fecha       : 25/04/2025
Tipo        : Débito Automático
Descripción : ICE — FACTURA CONJUNTA ELECTRICIDAD + INTERNET — ABRIL 2025
Monto       : -₡1.130.000,00
```

**Working:**
- ICE Factura Electrónica: electricity net ₡800,000 + IVA 13% ₡104,000; internet net ₡200,000 + IVA 13% ₡26,000 = Total ₡1,130,000
- 100% business use — full input credit ₡130,000
- Return entry: Línea 8 — ₡1,000,000 net; crédito fiscal: ₡130,000

---

### Example 4 — Export of services (0%)

**Scenario:** Costa Rican IT company exports software services to US client — USD wire.

**Bank statement line (Scotiabank format):**
```
Fecha       : 20/04/2025
Tipo        : Crédito ME — Transferencia Internacional
Descripción : US CLIENT LLC — SOFTWARE DEV SERVICES Q1 2025
Monto       : ₡25.350.000,00 (USD 50.000)
```

**Working:**
- Export of service consumed outside Costa Rica — 0% IVA
- Issue Factura Electrónica de Exportación (tipo 09)
- Return entry: Línea 5 — ₡25,350,000 | IVA: ₡0

---

### Example 5 — Private medical service (4%)

**Scenario:** Company pays for employee health screening at private clinic.

**Bank statement line (BNCR format):**
```
Fecha       : 08/04/2025
Tipo        : Débito — Pago Electrónico
Descripción : CLINICA BIBLICA SA — CHEQUEO MEDICO EMPRESARIAL ABR 2025
Monto       : -₡2.080.000,00
```

**Working:**
- Private clinic Factura Electrónica: net ₡2,000,000 + IVA 4% ₡80,000 = ₡2,080,000
- Input credit: ₡80,000 (business health programme — documented)
- Return entry: Línea 9 (crédito fiscal 4%): ₡80,000

---

### Example 6 — Monthly return summary

**Scenario:** Services company — April 2025.

| Item | Net (CRC) | IVA (CRC) |
|---|---|---|
| Domestic sales 13% | 100,000,000 | 13,000,000 |
| Export sales (0%) | 25,000,000 | 0 |
| Exempt sales | 5,000,000 | 0 |
| Total Output | 130,000,000 | 13,000,000 |
| Input purchases 13% | 50,000,000 | 6,500,000 |
| Input medical 4% | 2,000,000 | 80,000 |
| Total Input | 52,000,000 | 6,580,000 |
| **Net IVA payable** | | **6,420,000** |

---

## Section 5 — Tier 1 rules (compressed)

**Rate assignment:**
- 13%: standard for most goods and services
- 4%: private medical and dental services, medicines (prescription and OTC)
- 2%: private educational services (tuition), agricultural inputs
- 1%: canasta básica — specific list of basic food items (DGT Resolución MH-DGT-RES-0024-2019)
- 0%: exports of goods and services
- Exempt: public education, public health (CCSS), financial services, insurance, residential rent ≤ ₡750,000/month, public transport, international transport

**Input credit:**
- Credit at the rate paid on each purchase, for purchases used in taxable activities
- Must have Factura Electrónica with clave numérica (50 digits)
- Prorrata if mixed taxable/exempt business — escalate to CPA
- Residential rent: provider must monitor rent threshold; above ₡750,000/month = taxable at 13%

**Filing mechanics:**
- File Form D-104 monthly via ATV portal by 15th of following month
- All B2B sales require Factura Electrónica (XML v4.3, transmitted to Hacienda in real time)
- Remanente crédito fiscal carries forward indefinitely; refund rare in practice

---

## Section 6 — Tier 2 catalogue (genuinely data-unknowable items)

| Item | Why unknowable | What to ask |
|---|---|---|
| Canasta básica (1%) | Only specific items on DGT list qualify — must check item-by-item | "What is the exact food product? Check against DGT Resolución 0024-2019 list." |
| Residential rent rate | Exempt if ≤ ₡750,000/month; 13% if above | "What is the monthly rent amount? Provide lease agreement." |
| Medical rate (4%) | Only licensed medical services qualify | "Is this a licensed health professional service? Or wellness/cosmetic?" |
| Agriculture rate (2%) | Only agricultural inputs on approved list | "What is the input? Is it for direct agricultural production?" |
| Vehicle — business vs personal | Input credit only for business use | "Is vehicle in company name? % business use?" |
| Foreign digital service | Provider may be Hacienda-registered (charges 13%) or not (buyer must self-assess) | "Has the foreign provider registered with Hacienda? Do they issue a CR Factura?" |

---

## Section 7 — Excel working paper

**Columns:** Date | Supplier/Customer | Cédula | Clave numérica | Net (CRC) | IVA Rate % | IVA (CRC) | In/Out | Export? | Exempt? | Tier 2 flag | Notes

**Tab structure:**
1. `Output_Sales` — Facturas Electrónicas issued
2. `Input_Purchases` — Facturas Electrónicas received
3. `D104_Summary` — monthly return totals
4. `Tier2_Items` — awaiting client response

---

## Section 8 — Bank statement reading guide

### Banco Nacional (BNCR) format
```
Fecha       : 15/04/2025
Tipo        : Crédito — SINPE / Transferencia
Descripción : COMPANY NAME — FACTURA ELECT — HONORARIOS
Monto       : ₡14.700.000,00
Saldo       : ₡64.700.000,00
```

### BAC Credomatic format
```
15/04/2025  |  Crédito  |  COMPANY NAME  |  +14.700.000,00  |  Saldo: 64.700.000,00
```

### Key patterns:
- **CRC number format:** Period = thousands; comma = decimal: ₡14.700.000,00 = CRC 14,700,000.00
- **SINPE / Transferencia:** Domestic wire — match to Factura Electrónica
- **Débito Automático:** Direct debit — utilities; request Factura Electrónica from supplier
- **Crédito ME:** Foreign currency credit — export or foreign service
- **Clave numérica 50 digits:** Unique Factura Electrónica identifier — required for input credit

---

## Section 9 — Onboarding fallback

When client cannot provide Facturas Electrónicas:

1. Use bank statement amounts as IVA-inclusive and back-calculate:
   - Net = Total ÷ 1.13 | IVA = Total − Net (13% rate)
   - Net = Total ÷ 1.04 (4%); Net = Total ÷ 1.02 (2%); Net = Total ÷ 1.01 (1%)
2. Conservative defaults: 13% output; 0% input credit without clave numérica
3. Flag all items without e-invoice in Tier2_Items
4. Issue data request for missing clave numérica references
5. Warn client: Hacienda can disallow input without valid Factura Electrónica

---

## Section 10 — Reference material

| Resource | Reference |
|---|---|
| ATV — Administración Tributaria Virtual | https://www.hacienda.go.cr |
| DGT — Dirección General de Tributación | hacienda.go.cr — legislación |
| Ley del IVA (Ley 9635, Ley de Fortalecimiento) | Asamblea Legislativa — SINALEVI |
| Canasta básica list | DGT Resolución MH-DGT-RES-0024-2019 |
| Factura Electrónica technical spec | Hacienda XML v4.3 |
| Reduced rate decree | Decreto Ejecutivo 41820-H |
