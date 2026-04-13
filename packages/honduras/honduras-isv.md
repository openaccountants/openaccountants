---
name: honduras-isv
description: Use this skill whenever asked to prepare, review, or classify transactions for a Honduras ISV (Impuesto sobre Ventas) return or advise on Honduran VAT registration, filing, and SAR compliance. Trigger on phrases like "prepare ISV return Honduras", "Honduras sales tax", "ISV Honduras", "SAR Honduras", "RTN", or any Honduras ISV request. ALWAYS read this skill before touching any Honduras ISV work.
version: 2.0
jurisdiction: HN
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Honduras ISV (Impuesto sobre Ventas) Skill v2.0

---

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Honduras (República de Honduras) |
| Tax | ISV — Impuesto sobre Ventas (Sales Tax — functionally a VAT) |
| Currency | HNL (Honduran Lempira — L) |
| Standard rate | 15% |
| Increased rate | 18% (alcoholic beverages, tobacco products, tourist accommodation, food/beverages in hotels and resorts, air tickets to tourism destinations) |
| Zero rate | 0% (exports of goods and services) |
| Exempt | Basic food basket (canasta básica), medicines, medical services, education, financial services, insurance, agricultural inputs, natural gas, water supply (residential), public transport |
| Registration threshold | Annual income ≥ HNL 10,000,000 for mandatory registration; voluntary below |
| Tax authority | SAR (Servicio de Administración de Rentas — formerly DEI) |
| Filing portal | VirtualSAR — https://virtual.sar.gob.hn |
| Return form | Declaración del ISV (Form D-01) |
| Filing frequency | Monthly |
| Deadline | Last business day of the following month |
| e-Invoice | Factura Electrónica (SAR-registered providers — expanding mandate) |
| RTN | Registro Tributario Nacional — Honduran taxpayer ID (14 digits) |
| Contributor | Open Accountants Community |
| Validated by | Pending — requires sign-off by Honduras-licensed CPA or perito mercantil |
| Skill version | 2.0 |

### Key D-01 fields

| Field | Meaning |
|---|---|
| Casilla A | Total taxable sales 15% (net) |
| Casilla B | Total taxable sales 18% (net) |
| Casilla C | Export sales (0%) |
| Casilla D | Exempt sales |
| Casilla E | ISV débito fiscal (output) |
| Casilla F | ISV crédito fiscal (input on purchases) |
| Casilla G | Net ISV payable (E − F) |
| Casilla H | Crédito excedente (excess credit c/f) |

### Conservative defaults

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 15% standard |
| Unknown whether 18% tourism rate applies | Confirm — hotel accommodation and tourist food typically 18% |
| Unknown whether canasta básica exempt | 15% until item confirmed on exempt list |
| Unknown whether export documentation complete | Treat as domestic 15% |
| Unknown business-use % (vehicle, phone, home) | 0% input credit |
| Unknown whether Factura issued | No input credit until confirmed |
| Foreign digital service (B2B) | 15% — buyer self-assesses if foreign provider not registered |

### Red flag thresholds

| Threshold | Value |
|---|---|
| HIGH single transaction | HNL 2,000,000 |
| HIGH tax delta on single conservative default | HNL 300,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per return |
| LOW absolute net ISV position | HNL 5,000,000 |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

Before starting any Honduras ISV work, obtain:

1. RTN (Registro Tributario Nacional — 14 digits) and SAR registration
2. Monthly bank statements in HNL and USD (many Honduran businesses operate in both)
3. Facturas issued (paper or electronic with CAI — Código de Autorización de Impresión)
4. Purchase invoices from registered suppliers (with their RTN and CAI)
5. Prior month D-01 return (for crédito excedente carried forward)
6. Import customs declarations for imported goods
7. Export documentation (for zero-rated exports)

### Refusal catalogue

Refuse and escalate to a CPA / perito mercantil for:
- Proporcionalidad (partial exemption for mixed taxable/exempt businesses)
- ISV on real estate (complex)
- Free trade zone (Zona Libre / ZIP — Choloma) — exempt from ISV
- ISV on tourism — 18% rate rules are detailed
- Maquiladora (export manufacturing) — special ISV treatment
- ISV retenciones as agent
- Non-resident digital service providers

---

## Section 3 — Supplier pattern library

### 3.1 Banking and financial services

| Supplier | Typical description | ISV rate | Input credit |
|---|---|---|---|
| Banco Atlántida | Bank fees, wire transfers | Exempt | No |
| BAC Honduras | Commercial banking | Exempt | No |
| Ficohsa | Business banking | Exempt | No |
| Banpaís | Regional banking | Exempt | No |
| BANHPROVI | Development banking | Exempt | No |
| Tigo Money (payments) | Mobile money | Exempt | No |
| Tengo (Ficohsa) | Digital wallet | Exempt | No |
| VisaNet Honduras | Card processing | 15% | Yes |
| PayTrust HN | Payment gateway | 15% | Yes |

### 3.2 Electricity and utilities

| Supplier | Typical description | ISV rate | Input credit |
|---|---|---|---|
| ENEE (Empresa Nacional de Energía Eléctrica) | Electricity — national | 15% (commercial) | Yes (business) |
| SERVICIO DE AGUA — SANAA | Water — Tegucigalpa | Exempt (residential) | No |
| Aguas de San Pedro (DIMA) | Water — San Pedro Sula | Exempt (residential) | No |
| Hondugas | Propane/gas | 15% | Yes |
| AMDC (municipalidad) | Waste / municipal services | 15% | Yes |

### 3.3 Telecommunications

| Supplier | Typical description | ISV rate | Input credit |
|---|---|---|---|
| Tigo Honduras (Millicom) | Mobile, broadband | 15% | Yes (business use) |
| Claro Honduras (América Móvil) | Mobile, internet, TV | 15% | Yes (business use) |
| Hondutel | Fixed line, internet | 15% | Yes (business use) |
| Liberty Honduras (formerly Columbus) | Cable TV, fiber | 15% | Yes |

### 3.4 Transport and travel

| Supplier | Typical description | ISV rate | Input credit |
|---|---|---|---|
| CM Airlines / Avianca Honduras | Domestic/regional flights | 18% (tourism air) | Yes |
| Copa Airlines Honduras | International flights | 0% (export) | No |
| American Airlines Honduras | International flights | 0% | No |
| Uber Honduras | Ride-hailing | 15% | Yes (business use) |
| Intercity bus (HEDMAN ALAS) | Long-distance bus | Exempt | No |
| City buses | Urban public transport | Exempt | No |

### 3.5 Fuel

| Supplier | Typical description | ISV rate | Input credit |
|---|---|---|---|
| Petrotela | Fuel stations | 15% | Yes (business) |
| TEXACO Honduras | Fuel | 15% | Yes |
| Uno Honduras (DIPPSA) | Fuel | 15% | Yes |
| Shell Honduras | Fuel, lubricants | 15% | Yes |

### 3.6 Logistics and courier

| Supplier | Typical description | ISV rate | Input credit |
|---|---|---|---|
| Servientrega Honduras | Domestic courier | 15% | Yes |
| DHL Honduras | International courier | 0% (export) / 15% (domestic) | Yes |
| FedEx Honduras | International courier | 0% / 15% | Yes |
| Aerocasillas Honduras | Miami-Tegucigalpa parcels | 15% | Yes |
| Honducor (Correos Honduras) | State postal | 15% | Yes |

### 3.7 Retail and office supplies

| Supplier | Typical description | ISV rate | Input credit |
|---|---|---|---|
| Walmart Honduras (La Colonia) | Supermarket | Mixed (exempt food / 15% non-food) | Partial |
| Supermercados Colonial | Grocery | Mixed | Partial |
| Precio Uno | Discount supermarket | Mixed | Partial |
| Office Depot Honduras | Office supplies | 15% | Yes |
| Librería Navarro | Stationery | 15% | Yes |
| Centro Comercial Malls | General retail | 15% | Yes |

### 3.8 Software and digital services

| Supplier | Typical description | ISV rate | Input credit |
|---|---|---|---|
| Defontana Honduras | ERP for SMEs | 15% | Yes |
| Softland Honduras | Accounting software | 15% | Yes |
| Alegra Honduras | Cloud invoicing | 15% | Yes |
| Microsoft Honduras (Azure, M365) | Cloud — B2B | 15% (reverse-charge if not registered) | Yes |
| Google Honduras (Workspace, Ads) | Digital — B2B | 15% | Yes |
| Zoom | Video — B2B | 15% | Yes |
| AWS | Cloud — B2B | 15% | Yes |

### 3.9 Professional services

| Supplier | Typical description | ISV rate | Input credit |
|---|---|---|---|
| CPA / Auditor | Accounting, audit, tax | 15% | Yes |
| Firma de abogados | Legal | 15% | Yes |
| Agencia de publicidad | Advertising | 15% | Yes |
| Consultora | Consulting | 15% | Yes |
| Notaría | Notarial services | 15% | Yes |

### 3.10 Tourism and hospitality (18% rate)

| Supplier | Typical description | ISV rate | Input credit |
|---|---|---|---|
| Hotel Princess (Tegucigalpa) | Hotel accommodation | 18% | Yes (business travel) |
| Intercontinental Honduras | Hotel | 18% | Yes |
| Restaurant in hotel | Food/beverage in hotel | 18% | Yes (business meals, documented) |
| Roatán resort | Tourism accommodation | 18% | Yes |
| Tourist air ticket (domestic) | Air to Roatán, La Ceiba | 18% | Yes |

---

## Section 4 — Worked examples

### Example 1 — Standard ISV on consulting

**Scenario:** Tegucigalpa consulting firm issues factura to Honduran corporate.

**Bank statement line (Banco Atlántida format):**
```
Fecha       : 15/04/2025
Tipo        : Crédito — Transferencia Electrónica
Descripción : TECH SA DE CV — FACTURA 001-001-000001234 HONORARIOS
Monto       : +L. 1.150.000,00
Saldo       : L. 5.150.000,00
```

**Working:**
- Factura: net L 1,000,000 + ISV 15% L 150,000 = L 1,150,000
- Return entry: Casilla A — L 1,000,000 | Casilla E: L 150,000

*Note: HNL amounts use period for thousands; comma for decimal: L. 1.150.000,00 = HNL 1,150,000.00*

---

### Example 2 — Hotel accommodation (18%)

**Scenario:** Employee stays at Hotel Princess for business meeting.

**Bank statement line (BAC Honduras format):**
```
Fecha       : 10/04/2025
Tipo        : Débito — Cargo Tarjeta
Descripción : HOTEL PRINCESS TEGUCIGALPA — 3 NIGHTS
Monto       : -L. 10.620,00
```

**Working:**
- Hotel Factura: net L 9,000 + ISV 18% L 1,620 = L 10,620
- Input credit: L 1,620 (business travel — room only, documented)
- Return entry: Crédito fiscal 18%: L 1,620

---

### Example 3 — ENEE electricity (business)

**Scenario:** Office electricity bill — Tegucigalpa.

**Bank statement line (Ficohsa format):**
```
Fecha       : 25/04/2025
Tipo        : Débito — Pago Servicio
Descripción : ENEE — FACTURA ENERGIA ELECTRICA ABR 2025 — CLIENTE 1234567
Monto       : -L. 115.000,00
```

**Working:**
- ENEE Factura: net L 100,000 + ISV 15% L 15,000 = L 115,000
- 100% business use — full input credit
- Return entry: Casilla F: L 15,000

---

### Example 4 — Export of services (0%)

**Scenario:** Honduran IT firm exports software to US client — USD wire.

**Bank statement line (Banco Atlántida format):**
```
Fecha       : 20/04/2025
Tipo        : Crédito ME — Transferencia Internacional
Descripción : TECH CORP USA — SOFTWARE LICENSE Q1 2025
Monto       : +L. 2.500.000,00 (USD 100.000)
```

**Working:**
- Export of service consumed outside Honduras — 0% ISV
- Factura de Exportación with SAR endorsement
- Return entry: Casilla C — L 2,500,000 | ISV: L 0

---

### Example 5 — Canasta básica (exempt)

**Scenario:** Office purchases basic groceries at La Colonia for cafetería.

**Bank statement line (Banpaís format):**
```
Fecha       : 08/04/2025
Tipo        : Débito — POS
Descripción : SUPERMERCADOS LA COLONIA TEGUCIGALPA
Monto       : -L. 45.000,00
```

**Working:**
- La Colonia receipt: rice, beans, tortillas, eggs (exempt) L 30,000; cleaning supplies 15% L 15,000 × 15% = L 1,957 ISV
- Input credit: L 1,957 on non-exempt items only
- Exempt canasta básica: no ISV; not in return

---

### Example 6 — Monthly return summary

**Scenario:** Services company — April 2025.

| Item | Net (HNL) | ISV (HNL) |
|---|---|---|
| Domestic sales 15% | 8,000,000 | 1,200,000 |
| Tourism services 18% | 500,000 | 90,000 |
| Export sales (0%) | 2,000,000 | 0 |
| Exempt sales | 1,000,000 | 0 |
| Total Output | 11,500,000 | 1,290,000 |
| Input ISV on purchases | 4,000,000 | 600,000 |
| **Net ISV payable** | | **690,000** |

---

## Section 5 — Tier 1 rules (compressed)

**Rate assignment:**
- 15% standard: most goods and services not exempt or 18%
- 18%: alcoholic beverages, tobacco, hotel/resort accommodation, food/beverages in hotels and resorts, air tickets to tourism destinations (domestic)
- 0%: exports of goods and services
- Exempt: canasta básica (basic food basket — SAR list), medicines, medical and dental services, education (public and private), financial services, insurance, water (residential), public transport (bus/city), agricultural inputs

**Input credit:**
- Credit allowed on 15% and 18% purchases for taxable activities
- Must have valid Factura with RTN and CAI number
- No credit on exempt purchases or purchases for non-business use
- Tourism 18%: input credit allowed for businesses operating in taxable activities

**Filing mechanics:**
- File D-01 monthly via VirtualSAR by last business day of following month
- Facturas must have CAI (Código de Autorización de Impresión) issued by SAR
- e-Invoice mandate expanding — confirm with SAR which companies required
- Crédito excedente carries forward; export refund available but slow

---

## Section 6 — Tier 2 catalogue (genuinely data-unknowable items)

| Item | Why unknowable | What to ask |
|---|---|---|
| Tourism rate (18%) | Applies to hotel accommodation, food in hotels, tourist air — must confirm venue/service type | "Is this hotel accommodation, food served in a hotel, or tourist air ticket?" |
| Canasta básica exemption | Only SAR-listed items exempt — product description needed | "What is the exact product? Check against SAR canasta básica list." |
| Export qualification | Service must be consumed outside Honduras | "Where is the client? Evidence of offshore consumption?" |
| Fuel — business vs personal | Input credit only for business vehicles | "Is vehicle registered in company's name? % business use?" |
| Foreign digital service | Whether provider SAR-registered (charges ISV) or buyer must self-assess | "Does the foreign provider issue a Honduran Factura with RTN?" |
| Maquiladora supplier | Maquiladoras may be in free zone — no ISV | "Is this supplier a Zona Libre / ZIP operation?" |

---

## Section 7 — Excel working paper

**Columns:** Date | Supplier/Customer | RTN | Factura No. | CAI | Net (HNL) | ISV Rate % | ISV (HNL) | In/Out | Export? | Exempt? | Tier 2 flag | Notes

**Tab structure:**
1. `Output_Sales` — Facturas issued
2. `Input_Purchases` — Facturas received
3. `D01_Summary` — monthly return totals
4. `Tier2_Items` — awaiting client response

---

## Section 8 — Bank statement reading guide

### Banco Atlántida format
```
Fecha       : 15/04/2025
Tipo        : Crédito — Transferencia Electrónica
Descripción : COMPANY NAME — FACTURA 001-001-000001234
Monto       : +L. 1.150.000,00
Saldo       : L. 5.150.000,00
```

### BAC Honduras format
```
15/04/2025  |  Crédito  |  COMPANY NAME  |  +1,150,000.00 HNL  |  Saldo: 5,150,000.00
```

### Key patterns:
- **HNL number format:** Period = thousands; comma = decimal: L. 1.150.000,00 = HNL 1,150,000.00
- **Crédito — Transferencia:** Money in — match to issued Factura for output ISV
- **Débito — Pago Servicio:** Utility/service payment — request Factura for input credit
- **Crédito ME:** Foreign currency — export zero-rate or reverse-charge
- **CAI on Factura:** Required for valid ISV document — always verify present

---

## Section 9 — Onboarding fallback

When client cannot provide Facturas for all transactions:

1. Use bank statement amounts as ISV-inclusive and back-calculate:
   - Net = Total ÷ 1.15 | ISV = Total − Net (15%)
   - Net = Total ÷ 1.18 (18% tourism)
2. Conservative defaults: 15% output; 0% input credit without valid Factura/CAI
3. Flag all items without CAI in Tier2_Items
4. Issue data request for missing Factura references
5. Warn client: SAR can disallow input credit without valid Factura with CAI from RTN-registered supplier

---

## Section 10 — Reference material

| Resource | Reference |
|---|---|
| SAR (Servicio de Administración de Rentas) | https://www.sar.gob.hn |
| VirtualSAR (filing portal) | https://virtual.sar.gob.hn |
| Ley del ISV (Decreto 24-98 and amendments) | SAR — legislación |
| Canasta básica exempt list | SAR — bienes exentos |
| Tourism 18% rate — Decreto 51-2003 | Congreso Nacional Honduras |
| CAI authorization guide | SAR — facturas y talonarios |
