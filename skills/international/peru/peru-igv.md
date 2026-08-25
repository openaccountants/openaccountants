---
name: peru-igv
description: Use this skill whenever asked to prepare, review, or classify transactions for a Peru IGV (Impuesto General a las Ventas) return or advise on Peruvian VAT registration, filing, and SUNAT compliance. Trigger on phrases like "prepare IGV return Peru", "Peruvian VAT", "IGV Peru", "SUNAT", "RUC", or any Peru IGV request. ALWAYS read this skill before touching any Peru IGV work.
version: 2.0
jurisdiction: PE
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Maria Clemencia Valverde Rios
review_status: current
depends_on:
  - vat-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Peru Igv

## Peru IGV (Impuesto General a las Ventas) Skill v2.0

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Maria Clemencia Valverde Rios** on 2026-06-29.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### peru-igv

- **Standard rate** — 18% (16% IGV + 2% IPM)
- **IGV component of standard rate** — 16%  _(TUO de la Ley del IGV — Decreto Supremo 055-99-EF)_
- **IPM (Impuesto de Promoción Municipal) component** — 2%  _(TUO de la Ley del IGV — Decreto Supremo 055-99-EF)_
- **Reduced rate** — For the 2026 fiscal year, MYPEs within the restaurant and hotel sector (revenues ≤ 1,700 UIT and core business ≥ 70%) qualify for a consolidated reduced rate of 10.5% (8% VAT + 2.5% IPM)  _(Ley N.° 32219)_
- **Zero rate** — 0% (exports of goods and services)
- **Exempt supplies** — Financial services, insurance, medical services, education, residential rent (some), basic foodstuffs (Apéndice I), agricultural goods, international transport  _(Apéndice I — LIGV)_
- **Registration threshold** — No general threshold — any business making taxable supplies must register; however Nuevo RUS and RER for small businesses have simplified obligations
- **Currency** — PEN (Peruvian Sol — S/)
- **Return form** — PDT 621 — Declaración Mensual de IGV — Renta 3ra Categoría
- **Filing frequency** — Monthly
- **Filing deadline** — Varies by RUC last digit (first twelve business days of the following month per SUNAT calendar)  _(Art. 29 DS Nº 135-99-EF)_
- **RUC (taxpayer ID) format** — Registro Único de Contribuyentes — 11-digit Peruvian taxpayer ID
- **Foreign digital service (B2B) default treatment** — the Peruvian entity must self-assess 18% VAT for inbound services and withhold 30% Income Tax on the gross foreign invoice.  _(TUO LIR Art 56°, j))_
- **LOW absolute net IGV position** — monthly tax payable is determined by deducting the Input Tax (Credit) from the Output Tax (Gross IGV).  _(TUO Ley IGV Art. 11)_
- **Casilla 189 — IGV payable formula** — 105 − 125 − 140; if positive  _(RS N° 076 -2020 SUNAT)_
- **SPOT detracción rate — construction services** — 4%  _(Art. 13 RS N° 183-2004 SUNAT)_
- **International flights IGV rate** — 0% (export)
- **IGV retenciones (withholding) rate** — If the transaction exceeds S/. 700, a 3% withholding by designated agents applies, which offsets the tax liability.  _(art 3 RS N°037-2002 SUNAT)_
- **IGV percepciones (advance) rate** — 3.5%,5 or 10% on imports (depending on the importer's risk profile and asset condition) and 1% on fuel — credit against payable  _(Art 19 Ley N.° 29173)_
- **Boleta de Venta input credit cap** — taxpayers under the MYPE or GENERAL income tax regimens may deduct as a cost or expense those boletas de venta issued exclusively by taxpayers under the simplified regimen NUEVO RUS, up to a limit of 6% of the total value of purchases supported by invoices recorded in the purchase ledger (Registro de compras), provided that such deduction does not exceed 200 UIT per fiscal year.  _(TUO LIR Art. 37)_
- **IGV-inclusive back-calculation** — Net = Total ÷ 1.18 | IGV = Total − Net
- **Legal basis — TUO de la Ley del IGV** — Decreto Supremo 055-99-EF (as amended)  _(Decreto Supremo 055-99-EF)_
- **Input credit on Nuevo RUS / Boleta de Venta** — No credit on Boleta de Venta (B2C receipt) or Nuevo RUS suppliers

## Section 1 — Quick reference

**Quick reference**

| Field | Value |
| --- | --- |
| Country | Peru (República del Perú) |
| Tax | IGV — Impuesto General a las Ventas (18% = 16% IGV + 2% IPM — Impuesto de Promoción Municipal) |
| Currency | PEN (Peruvian Sol — S/) |
| Standard rate | 18% (16% IGV + 2% IPM) |
| Reduced rate | None (single 18% rate in general) |
| Zero rate | 0% (exports of goods and services) |
| Exempt | Financial services, insurance, medical services, education, residential rent (some), basic foodstuffs (Apéndice I), agricultural goods, international transport |
| Registration threshold | No general threshold — any business making taxable supplies must register; however Nuevo RUS and RER for small businesses have simplified obligations |
| Tax authority | SUNAT (Superintendencia Nacional de Aduanas y de Administración Tributaria) |
| Filing portal | SUNAT Operaciones en Línea (SOL) — https://www.sunat.gob.pe |
| Return form | PDT 621 — Declaración Mensual de IGV — Renta 3ra Categoría |
| Filing frequency | Monthly |
| Deadline | Varies by RUC last digit (8th–22nd of following month per SUNAT calendar) |
| e-Invoice | CPE (Comprobante de Pago Electrónico) mandatory for most businesses (factura electrónica, boleta electrónica) |
| RUC | Registro Único de Contribuyentes — 11-digit Peruvian taxpayer ID |
| Contributor | Open Accountants Community |
| Validated by | Verified by Maria Clemencia Valverde Rios (CPA) on 2026-06-29 |
| Skill version | 2.0 |

### Key PDT 621 fields

**Key PDT 621 fields**

| Field | Meaning |
| --- | --- |
| Casilla 100 | Net taxable sales (base imponible ventas) |
| Casilla 105 | IGV on sales (débito fiscal) |
| Casilla 107 | Export sales (0%) |
| Casilla 109 | Exempt sales |
| Casilla 120 | Net taxable purchases |
| Casilla 125 | IGV on purchases (crédito fiscal) |
| Casilla 140 | Retenciones y percepciones a favor |
| Casilla 189 | IGV payable (105 − 125 − 140; if positive) |
| Casilla 190 | Saldo a favor (excess credit c/f) |

### Conservative defaults

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown rate on a sale | 18% standard |
| Unknown whether Apéndice I exempt | 18% until confirmed in exempt list |
| Unknown whether export documentation complete | Treat as domestic 18% |
| Unknown business-use % (vehicle, phone, home) | 0% input credit |
| Unknown whether CPE (e-invoice) issued | No input credit until confirmed |
| Foreign digital service (B2B) | 18% — foreign provider registers under SUNAT simplified scheme (from 2024) |
| Nuevo RUS supplier | No IGV credit (they do not charge IGV) |

### Red flag thresholds

**Red flag thresholds**

| Threshold | Value |
| --- | --- |
| HIGH single transaction | S/ 100,000 |
| HIGH tax delta on single conservative default | S/ 18,000 |
| MEDIUM counterparty concentration | >40% of output or input |
| MEDIUM conservative default count | >4 per return |
| LOW absolute net IGV position | S/ 200,000 |

## Section 2 — Required inputs and refusal catalogue

### Required inputs

Before starting any Peru IGV work, obtain:

1. RUC (11-digit) and SUNAT inscription certificate
2. Monthly bank statements in PEN (all business accounts)
3. CPE (Comprobante de Pago Electrónico) — Facturas Electrónicas issued (XML from OSE/SOL)
4. CPE received from suppliers (XML or PDF with hash and SUNAT validation)
5. Prior month PDT 621 (for saldo a favor and retenciones carried forward)
6. Import customs declarations (DAM — Declaración Aduanera de Mercancías) for imports
7. Retenciones y percepciones certificates

### Refusal catalogue

- **Refuse and escalate to a CPC** — Prorrata del crédito fiscal (partial exemption for mixed businesses); IGV on real estate / first sale of construction; Sistema de Pago de Obligaciones Tributarias (SPOT / detracciones) — complex for certain sectors; IGV retenciones as an agent (retención agent obligations); IGV percepciones (advance IGV collection — fuel, imports); Export IGV refund (drawback / recuperación anticipada); Free trade zones (Zonas Francas de Tacna, etc.); Non-resident digital service compliance (newer 2024 rules — complex)

## Section 3 — Supplier pattern library

### 3.1 Banking and financial services

**Banking and financial services suppliers**

| Supplier | Typical description | IGV rate | Input credit |
| --- | --- | --- | --- |
| BCP (Banco de Crédito del Perú) | Bank fees, wire transfers | Exempt | No |
| BBVA Perú | Account maintenance, loans | Exempt | No |
| Interbank | Commercial banking fees | Exempt | No |
| Scotiabank Perú | Business banking | Exempt | No |
| BanBif | Corporate banking | Exempt | No |
| Yape (BCP) | Mobile payments | Exempt (payment service) | No |
| Plin (Interbank/BBVA/Scotiabank) | P2P payments | Exempt | No |
| VisaNet Perú | Card processing | 18% | Yes |
| Niubiz (VisaNet renamed) | POS terminal | 18% | Yes |
| Culqi | Digital payment gateway | 18% | Yes |

### 3.2 Electricity and utilities

**Electricity and utilities suppliers**

| Supplier | Typical description | IGV rate | Input credit |
| --- | --- | --- | --- |
| Luz del Sur (Enel) | Electricidad — Lima Sur | 18% | Yes (business) |
| Enel Distribución Perú (formerly Edelnor) | Electricity — Lima Norte | 18% | Yes (business) |
| Hidrandina | Electricity — La Libertad/Ancash | 18% | Yes (business) |
| Electrosur | Electricity — Tacna/Moquegua | 18% | Yes |
| SEDAPAL | Water — Lima | 18% | Yes (business) |
| Gas Natural Fenosa (Cálidda) | Natural gas — Lima | 18% | Yes |

### 3.3 Telecommunications

**Telecommunications suppliers**

| Supplier | Typical description | IGV rate | Input credit |
| --- | --- | --- | --- |
| Entel Perú | Mobile, broadband | 18% | Yes (business use) |
| Movistar Perú (Telefónica) | Mobile, fixed, ADSL | 18% | Yes (business use) |
| Claro Perú | Mobile, internet, TV | 18% | Yes (business use) |
| Bitel | Mobile — budget carrier | 18% | Yes |
| Win (Winncompany) | Fiber internet — Lima | 18% | Yes |

### 3.4 Transport and travel

**Transport and travel suppliers**

| Supplier | Typical description | IGV rate | Input credit |
| --- | --- | --- | --- |
| LATAM Perú | Domestic flights | 18% | Yes |
| LATAM Perú | International flights | 0% (export) | No |
| Sky Airline Perú | Domestic | 18% | Yes |
| Star Perú | Domestic regional | 18% | Yes |
| Metropolitano (Lima BRT) | Bus rapid transit | Exempt | No |
| Metro de Lima (líneas 1, 2) | Metro | Exempt | No |
| Uber Perú | Ride-hailing | 18% | Yes (business use) |
| InDriver Perú | Ride-hailing | 18% | Yes |
| Cruz del Sur (intercity bus) | Long-distance bus | Exempt | No |

### 3.5 Logistics and courier

**Logistics and courier suppliers**

| Supplier | Typical description | IGV rate | Input credit |
| --- | --- | --- | --- |
| Olva Courier | Domestic courier | 18% | Yes |
| Urbano Express | Domestic courier | 18% | Yes |
| DHL Perú | International courier | 0% (export) / 18% (domestic) | Yes |
| FedEx Perú | International courier | 0% / 18% | Yes |
| MiBanco (business loan) | Financial service | Exempt | No |
| Serpost | State postal | 18% | Yes |

### 3.6 Fuel

**Fuel suppliers**

| Supplier | Typical description | IGV rate | Input credit |
| --- | --- | --- | --- |
| Primax | Fuel stations | 18% (+ ISC impuesto selectivo) | Yes (business vehicles) |
| Pecsa (Petroperú) | Fuel | 18% | Yes |
| Repsol Perú | Fuel, lubricants | 18% | Yes |

### 3.7 Retail and office supplies

**Retail and office supplies suppliers**

| Supplier | Typical description | IGV rate | Input credit |
| --- | --- | --- | --- |
| Wong / Metro (Cencosud) | Supermarket — mixed | 18% / exempt food mix | Partial |
| Plaza Vea (InRetail) | Supermarket | 18% / exempt mix | Partial |
| Tottus (Falabella) | Supermarket | 18% / exempt mix | Partial |
| Sodimac Perú | Hardware, home | 18% | Yes |
| Office Depot Perú | Office supplies | 18% | Yes |
| Falabella Perú (retail) | Department store | 18% | Yes |

### 3.8 Software and digital services

**Software and digital services suppliers**

| Supplier | Typical description | IGV rate | Input credit |
| --- | --- | --- | --- |
| Contasimple Perú | Cloud accounting | 18% | Yes |
| Alegra Perú | Invoicing, accounting | 18% | Yes |
| Facturador SUNAT | Free SUNAT e-invoice tool | Free — no IGV | N/A |
| Efact (OSE provider) | CPE electronic issuance | 18% | Yes |
| Microsoft Perú (Azure, M365) | Cloud — B2B | 18% (SUNAT-registered foreign) | Yes |
| Google Perú (Workspace, Ads) | Digital — B2B | 18% (SUNAT-registered) | Yes |
| Zoom Perú | Video — B2B | 18% | Yes |
| AWS Perú | Cloud — B2B | 18% | Yes |

### 3.9 Professional services

**Professional services suppliers**

| Supplier | Typical description | IGV rate | Input credit |
| --- | --- | --- | --- |
| CPC (Contador Público Colegiado) | Accounting, audit, tax | 18% | Yes |
| Estudio de abogados | Legal | 18% | Yes |
| Agencia de publicidad | Advertising | 18% | Yes |
| Consultora empresarial | Management consulting | 18% | Yes |
| Notaría | Notarial services | 18% | Yes |

### 3.10 Insurance

**Insurance suppliers**

| Supplier | Typical description | IGV rate | Input credit |
| --- | --- | --- | --- |
| Rimac Seguros | All lines | Exempt | No |
| Pacífico Seguros | Business, health | Exempt | No |
| La Positiva | Property, motor | Exempt | No |
| Mapfre Perú | All lines | Exempt | No |

## Section 4 — Worked examples

### Example 1 — Standard IGV on consulting

**Scenario:** Lima IT firm issues Factura Electrónica to Peruvian corporate.

**Bank statement line (BCP format):**
```
Fecha       : 15/04/2025
Operación   : Abono — Transferencia Interbancaria
Descripción : EMPRESA TECH SAC — FACT ELEC B001-00004123 HONORARIOS TI
Importe     : +S/ 590.000,00
Saldo       : S/ 2.590.000,00
```

**Working:**
- Factura Electrónica: net S/ 500,000 + IGV 18% S/ 90,000 = S/ 590,000
- Return entry: Casilla 100 — S/ 500,000 | Casilla 105 (débito fiscal): S/ 90,000

### Example 2 — Export of services (0%)

**Scenario:** Peruvian software firm exports SaaS to US client — USD wire.

**Bank statement line (BBVA Perú format):**
```
Fecha       : 20/04/2025
Tipo        : Abono — Transferencia Internacional
Descripción : TECH CORP USA — SOFTWARE LICENSE Q1 2025
Importe     : +S/ 1.850.000,00 (USD 500.000)
```

**Working:**
- Export of service to foreign entity — 0% IGV
- Issue Factura de Exportación Electrónica (tipo 09)
- Return entry: Casilla 107 — S/ 1,850,000 | IGV: S/ 0

### Example 3 — Electricity bill (business)

**Scenario:** Lima office — Luz del Sur bill for April 2025.

**Bank statement line (Interbank format):**
```
Fecha       : 25/04/2025
Tipo        : Débito — Pago de Servicios
Descripción : LUZ DEL SUR SAA — SUMINISTRO 1234567 ABR 2025
Importe     : -S/ 47.200,00
```

**Working:**
- CPE: net S/ 40,000 + IGV 18% S/ 7,200 = S/ 47,200
- 100% business — full input credit
- Return entry: Casilla 120 — S/ 40,000; Casilla 125: S/ 7,200

### Example 4 — Detracción (SPOT) on construction services

**Scenario:** Company contracts construction services — subject to SPOT detracción.

**Bank statement line (Scotiabank format):**
```
Fecha       : 05/04/2025
Tipo        : Cargo — Depósito Detracción
Descripción : DETRACCION CONST SERV — BANCO NACION CTA DETR 00-12345
Importe     : -S/ 60.000,00
```

**Working:**
- Construction services subject to 4% SPOT detracción
- Total contract S/ 1,500,000 inc IGV × 4% = S/ 60,000 deposited to supplier's Banco de la Nación SPOT account
- Supplier can only access IGV credit after SUNAT verification
- Escalate to CPC — SPOT is complex; this example shows the detracción payment

### Example 5 — Nuevo RUS supplier (no IGV)

**Scenario:** Small supplier (Nuevo RUS) provides printing services.

**Bank statement line (BCP format):**
```
Fecha       : 12/04/2025
Tipo        : Débito — Transferencia
Descripción : IMPRENTA RAPIDEZ — BOLETA VENTA 001-00001234
Importe     : -S/ 3.500,00
```

**Working:**
- Nuevo RUS supplier issues Boleta de Venta (not Factura) — does not charge IGV
- Input credit: S/ 0 — Nuevo RUS businesses are not IGV-registered
- Record as expense S/ 3,500; no IGV credit

### Example 6 — Monthly return summary

**Monthly return summary table**

| Item | Net (PEN) | IGV (PEN) |
| --- | --- | --- |
| Domestic taxable sales | 2,000,000 | 360,000 |
| Export sales (0%) | 500,000 | 0 |
| Exempt sales (Apéndice I) | 200,000 | 0 |
| Total Output | 2,700,000 | 360,000 |
| Input IGV on purchases | 1,200,000 | 216,000 |
| Retenciones received | — | 25,000 |
| Total Input |  | 241,000 |
| **Net IGV payable** |  | **119,000** |

## Section 5 — Tier 1 rules (compressed)

**Rate assignment:**
- 18% (16% + 2% IPM): all goods and services not specifically exempt
- 0%: exports of goods (DAM exportación), services exported to non-residents consumed outside Peru
- Exempt (Apéndice I — LIGV): basic unprocessed foods, agricultural goods, fishing, certain medical supplies, educational materials, international transport services

**Input credit:**
- Credit allowed on 18% purchases for taxable activities with valid CPE (Factura Electrónica)
- No credit on Boleta de Venta (B2C receipt) or Nuevo RUS suppliers
- Prorrata: if mixed taxable/exempt business — proportional calculation required (escalate)
- Retenciones: 3% withheld by designated retención agents from certain suppliers; offsets payable
- Percepciones: 2%/1% advance IGV on imports and fuel — credit against payable
- SPOT (Detracciones): complex sector-specific system — escalate

**Filing mechanics:**
- File PDT 621 monthly via SUNAT SOL; deadline varies by RUC last digit
- CPE mandatory — factura electrónica for B2B (with RUC); boleta electrónica for B2C
- Saldo a favor carries forward; export refund via SUNAT after filing

## Section 6 — Tier 2 catalogue (genuinely data-unknowable items)

**Tier 2 catalogue**

| Item | Why unknowable | What to ask |
| --- | --- | --- |
| Apéndice I exemption | List is specific — product must be exactly named | "What is the product HS code/description? Need to match against Apéndice I list." |
| Fuel — business vs personal | IGV credit only for business vehicles | "Is vehicle in company's name? What % business use?" |
| SPOT detracción obligation | Complex — depends on sector, amount, and type | "What is the service/goods type and contract amount? Escalate to CPC." |
| Supplier regime | Nuevo RUS (no credit) vs Régimen MYPE Tributario (credit OK) | "Confirm supplier's SUNAT regime from SOL portal." |
| Export qualification | Service must be consumed outside Peru | "Client location and evidence of offshore consumption?" |
| Mixed residential/commercial | Residential rent exempt; commercial 18% | "Is the property lease for residential or commercial use?" |

## Section 7 — Excel working paper

**Columns:** Date | Supplier/Customer | RUC | CPE Series/No. | CPE Type | Net (PEN) | IGV 18% (PEN) | In/Out | Export? | Exempt? | Detracción? | Tier 2 flag | Notes

**Tab structure:**
1. `Output_Sales` — CPE issued (facturas electrónicas)
2. `Input_Purchases` — CPE received
3. `Retenciones_Percepciones` — withholding credits
4. `PDT621_Summary` — monthly return totals
5. `Tier2_Items` — awaiting client response

## Section 8 — Bank statement reading guide

### BCP format

```
Fecha       : 15/04/2025
Operación   : Abono — Transferencia Interbancaria
Descripción : COMPANY NAME — FACT B001-00004123
Importe     : +S/ 590.000,00
Saldo       : S/ 2.590.000,00
```

### BBVA Perú format

```
15/04/2025  |  TRANSFER CREDIT  |  COMPANY NAME  |  +590,000.00  |  BAL: 2,590,000.00
```

### Key patterns:

- **PEN number format:** Period = thousands; comma = decimal: S/ 590.000,00 = S/ 590,000.00
- **Abono:** Credit (money in) — match to issued Factura Electrónica
- **Débito:** Debit (money out) — match to received CPE for input credit
- **Detracción / Banco Nación:** SPOT detracción payment — escalate to CPC
- **Transferencia Internacional:** Foreign payment — export zero-rate or reverse-charge

## Section 9 — Onboarding fallback

When client cannot provide CPEs for all transactions:

1. Use bank statement amounts as IGV-inclusive and back-calculate:
   - Net = Total ÷ 1.18 | IGV = Total − Net
2. Conservative defaults: 18% output; 0% input credit without valid CPE
3. Flag all items without CPE in Tier2_Items
4. Issue data request for missing CPE series/numbers
5. Warn client: SUNAT can disallow input credit without valid CPE from RUC-registered supplier; Boletas only credit up to 6% of net credit from facturas

## Section 10 — Reference material

**Reference material**

| Resource | Reference |
| --- | --- |
| SUNAT SOL (filing, CPE) | https://www.sunat.gob.pe |
| SUNAT — Apéndice I (exempt goods) | sunat.gob.pe — Texto Único Ordenado LIGV |
| PDT 621 instructions | SUNAT website — formularios virtuales |
| SPOT (Detracciones) guidance | SUNAT — Spot normativa |
| TUO de la Ley del IGV | Decreto Supremo 055-99-EF (as amended) |
| CPE technical specifications | SUNAT — comprobantes de pago electrónicos |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

<!-- openaccountants-cta-block -->

---

## Talk to a verified accountant

This guide is maintained by the OpenAccountants network — accountants who put
their name behind the tax answers AI gives people. The live, always-current
version (and the professional behind it) is at
[openaccountants.com](https://www.openaccountants.com).

- Use it in your AI: https://www.openaccountants.com/connect
- Meet the accountants: https://www.openaccountants.com/network

> **General reference only.** This document does not constitute tax, legal, or
> financial advice. Verify figures against the cited primary sources or with a
> licensed professional before relying on them.
