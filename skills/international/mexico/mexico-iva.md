---
name: mexico-iva
description: Use this skill whenever asked to prepare, review, or create a Mexico IVA (Impuesto al Valor Agregado) return or classify transactions for Mexican VAT purposes. Trigger on phrases like "prepare IVA return", "Mexican VAT", "declaracion de IVA", "CFDI classification", "SAT filing", or any request involving Mexico value-added tax. Also trigger when classifying transactions from CFDI XML files, bank statements, or invoices for Mexican IVA purposes. This skill contains the complete Mexico IVA classification rules, CFDI requirements, rate determination (including border zone), withholding rules, deductibility rules, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any Mexico IVA-related work.
---

# Mexico IVA Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Mexico |
| Jurisdiction Code | MX |
| Primary Legislation | Ley del Impuesto al Valor Agregado (Ley del IVA / LIVA) |
| Supporting Legislation | Codigo Fiscal de la Federacion (CFF); Resolucion Miscelanea Fiscal (RMF 2026); Ley del Impuesto sobre la Renta (LISR); Decreto de Estimulos Fiscales Region Fronteriza; 2026 Tax Reform (DOF Nov 7, 2025) |
| Tax Authority | Servicio de Administracion Tributaria (SAT) |
| Filing Portal | https://www.sat.gob.mx (Portal del SAT) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.1 |
| Confidence Coverage | Tier 1: rate determination, CFDI requirements, box assignment, derived calculations. Tier 2: border zone eligibility, proportional crediting, withholding determinations. Tier 3: maquiladora/IMMEX operations, transfer pricing VAT implications, consolidated group structures. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required. Claude executes, engine computes.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Claude flags the issue and presents options. A licensed Contador Publico must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed Contador Publico and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and RFC (Registro Federal de Contribuyentes)** [T1] -- 12 characters for legal entities (personas morales), 13 for individuals (personas fisicas)
2. **Tax regime (regimen fiscal)** [T1] -- General de Ley (601), RESICO Personas Fisicas (626), Actividades Empresariales y Profesionales (612), Incorporacion Fiscal (621, legacy), or other
3. **Fiscal period** [T1] -- monthly (standard for all IVA filers)
4. **Business activity (actividad economica)** [T2] -- impacts rate determination (agricultural, food production, etc.) and zero-rating eligibility
5. **Is the business located in a border zone (zona fronteriza)?** [T2] -- northern or southern border zone; impacts potential 8% reduced rate eligibility
6. **Does the business perform mixed activities (actos mixtos)?** [T2] -- taxable + zero-rated + exempt; impacts proportional IVA crediting
7. **Does the business make exports?** [T1] -- zero-rated under Article 29 LIVA
8. **Does the business receive services from non-residents?** [T1] -- impacts reverse charge / withholding obligations
9. **IVA favorable balance carried forward (saldo a favor)** [T1] -- from prior period
10. **Does the client issue CFDI correctly?** [T1] -- mandatory for all; verify PAC (Proveedor Autorizado de Certificacion) is active

For RESICO clients (Regimen Simplificado de Confianza) [T1]: confirm annual income is below MXN 3,500,000 for individuals. RESICO personas morales have different rules.

**If items 1-3 are unknown, STOP. Do not classify any transactions until RFC, regime, and period are confirmed.**

---

## Step 1: Transaction Classification Rules

### 1a. Determine Transaction Type [T1]

- Sale/income (IVA trasladado -- output IVA) or Purchase/expense (IVA acreditable -- input IVA)
- Salaries (sueldos y salarios), loan repayments, dividend distributions, income tax payments, PTU (profit sharing), IMSS/INFONAVIT contributions = OUT OF SCOPE (never on IVA return)
- **Legislation:** LIVA Articles 1, 1-A, 1-B (taxable activities definition)

### 1b. Determine Activity Type [T1]

Mexican IVA applies to four categories of activities (Article 1 LIVA):

| Activity | LIVA Article | Description |
|----------|-------------|-------------|
| Enajenacion de bienes | Art. 8 | Sale/transfer of goods |
| Prestacion de servicios | Art. 14 | Provision of services |
| Otorgamiento del uso o goce temporal de bienes | Art. 19 | Temporary use/lease of assets |
| Importacion de bienes o servicios | Art. 24 | Import of goods or services |

### 1c. Determine Counterparty Location [T1]

- Mexico (domestic): supplier/customer is Mexican tax resident or has permanent establishment (establecimiento permanente) in Mexico
- Foreign: supplier/customer outside Mexico
- **Note:** For services, place of supply follows where the service is effectively used/enjoyed (aprovechamiento), not where the supplier is located (Article 16 LIVA).

### 1d. Determine Applicable IVA Rate [T1]

| Rate | Application | LIVA Reference |
|------|------------|----------------|
| 16% | Standard rate -- all taxable activities not otherwise specified | Article 1, second paragraph |
| 8% | Border zone reduced rate (Decreto region fronteriza) -- conditions apply [T2] | Presidential Decree 2018 (extended through 2026) |
| 0% (tasa cero) | Zero-rated supplies -- input IVA IS creditable | Article 2-A |
| Exempt (exento) | Exempt supplies -- input IVA is NOT creditable | Article 9, 15, 20, 25 |

### 1e. Border Zone Rate (8%) Eligibility [T2]

**Legislation:** Decreto de Estimulos Fiscales Region Fronteriza Norte (December 2018, most recently extended through 2026); Decreto Region Fronteriza Sur (January 2021, extended through 2026).

To qualify for the 8% rate, ALL of the following must be met:

1. The taxpayer's domicilio fiscal (tax domicile) is in the northern or southern border zone
2. The supply of goods, services, or temporary use occurs physically in the border zone
3. The taxpayer has been registered in the border zone for at least 18 months (or since inception if newer)
4. The taxpayer has filed a notice (aviso) with SAT to apply the border stimulus
5. The taxpayer is not in the EFOS/EDOS blacklist (Article 69-B CFF)
6. The taxpayer meets minimum payroll requirements in the border zone

**Northern border municipalities:** Tijuana, Mexicali, Ensenada, Tecate, Playas de Rosarito, San Luis Rio Colorado, Puerto Penasco, Heroica Caborca, Altar, General Plutarco Elias Calles, Santa Cruz, Cananea, Naco, Agua Prieta, Ciudad Juarez, Ascension, Janos, Praxedis G. Guerrero, Guadalupe, Manuel Benavides, Ojinaga, Acuna, Piedras Negras, Guerrero, Hidalgo (Coahuila), Jimenez (Coahuila), Nava, Zaragoza, Anahuac, Nuevo Laredo, Guerrero (Tamaulipas), Mier, Miguel Aleman, Camargo, Gustavo Diaz Ordaz, Reynosa, Rio Bravo, Valle Hermoso, Matamoros, San Fernando.

**Southern border municipalities:** Palenque, Ocosingo, Benemérito de las Americas, Marques de Comillas, Las Margaritas, La Trinitaria, Frontera Comalapa, Amatenango de la Frontera, Motozintla, Mazapa de Madero, Cacahoatan, Union Juarez, Tapachula, Suchiate, Tuxtla Chico, Metapa, Frontera Hidalgo, and others per Decree.

**If client claims border zone rate, flag for reviewer confirmation. Do not apply 8% without verification of all conditions.**

---

## Step 2: Zero-Rated Activities (Tasa 0%) [T1]

**Legislation:** LIVA Article 2-A

Zero-rated activities generate IVA at 0% on output but allow FULL crediting of input IVA. This is more favorable than exempt (which blocks input IVA credit).

### 2a. Zero-Rated Goods (Article 2-A, Fraction I)

| Category | Examples | Notes |
|----------|----------|-------|
| Animals and vegetables (not industrialized) | Live cattle, fresh fruit, fresh vegetables, eggs, milk | Must be in natural state, not processed |
| Medicines (patented) | Prescription drugs, OTC medicines with sanitary registration | Cosmetics and hygiene products are NOT zero-rated |
| Food products (basic) | Tortillas, bread, cereals, meat, fish, dairy | Processed/prepared food for consumption on premises is 16% |
| Water (non-carbonated, non-flavored) | Bottled plain water | Flavored or carbonated water is 16% |
| Tractors and agricultural machinery | Tractors, harvesters, agricultural implements | Must be for agricultural use |
| Fertilizers and pesticides | Agricultural chemicals | Must be for agricultural use |
| Greenhouses and irrigation equipment | Hydroponic systems, drip irrigation | Must be for agricultural use |
| Gold (jewelry grade, minimum 10K) | Gold bars, coins (non-numismatic) | Investment gold only |
| Books, newspapers, magazines | Printed publications by the taxpayer | Digital publications: see specific rules |
| Feminine hygiene products | Sanitary pads, tampons, menstrual cups | Added by 2022 reform |
| Pet food | Dog food, cat food, animal feed | Added by reform |

### 2b. Zero-Rated Services (Article 2-A, Fraction II)

| Category | Examples |
|----------|----------|
| Agricultural services | Plowing, harvesting, veterinary for livestock |
| Grinding of grains | Corn mills (molinos de nixtamal), wheat milling |
| Pasteurization | Milk pasteurization services |
| Agricultural insurance | Crop insurance, livestock insurance |

### 2c. Zero-Rated Temporary Use (Article 2-A, Fraction III)

| Category | Examples |
|----------|----------|
| Agricultural machinery rental | Tractor rental for farming |
| Agricultural land rental | Farmland lease for cultivation |

### 2d. Zero-Rated Exports (Article 2-A, Fraction IV; Article 29)

| Category | Notes |
|----------|-------|
| Export of goods | Physical export with customs documentation (pedimento) |
| Export of services | Service effectively used/enjoyed abroad (strict interpretation) |
| Maquiladora exports | Under IMMEX program -- [T3] escalate for complex structures |

---

## Step 3: Exempt Activities (Exentas) [T1]

**Legislation:** LIVA Articles 9 (goods), 15 (services), 20 (temporary use), 25 (imports)

Exempt activities do NOT charge IVA AND do NOT allow crediting of input IVA. Input IVA on costs related to exempt activities is a non-deductible expense.

### 3a. Exempt Sales of Goods (Article 9)

| Category | LIVA Reference |
|----------|---------------|
| Land (terrenos) | Art. 9, Fr. I |
| Residential construction (casa habitacion) | Art. 9, Fr. II |
| Books, newspapers, magazines (by non-publisher) | Art. 9, Fr. III |
| Shares and credit instruments | Art. 9, Fr. VII |
| Currency (national and foreign) | Art. 9, Fr. VIII |
| Gold ingots (bullion, not jewelry-grade) | Art. 9, Fr. IX |
| Goods between IMMEX-certified companies | Art. 9, Fr. IX (conditions) |

### 3b. Exempt Services (Article 15)

| Category | LIVA Reference |
|----------|---------------|
| Commissions on exempt goods/services | Art. 15, Fr. I |
| Medical services (hospital, dental, veterinary) | Art. 15, Fr. II |
| Education (government-recognized RVOE programs) | Art. 15, Fr. IV |
| Public land transport (urban and suburban) | Art. 15, Fr. V |
| International maritime transport | Art. 15, Fr. VI |
| Insurance on agricultural/fishing activities | Art. 15, Fr. IX |
| Financial interest (consumer credit, mortgage) | Art. 15, Fr. X |
| Financial services (banking, exchange, insurance) | Art. 15, Fr. X |
| Works of art by the artist | Art. 15, Fr. XIII |
| Public entertainment (bullfighting, sports, theater) | Art. 15, Fr. XIV (state/municipal permit required) |

### 3c. Exempt Temporary Use (Article 20)

| Category | LIVA Reference |
|----------|---------------|
| Residential property rental (casa habitacion) | Art. 20, Fr. II |
| Furnished residential rental below threshold | Art. 20, Fr. II |

**Note on residential rental:** Residential property rental is exempt. Commercial property rental is taxable at 16%. Mixed-use properties require allocation [T2].

### 3d. Exempt Imports (Article 25)

| Category | LIVA Reference |
|----------|---------------|
| Temporary imports (except IMMEX) | Art. 25, Fr. I |
| Return of exported Mexican goods | Art. 25, Fr. II |
| Diplomatic/consular imports | Art. 25, Fr. III |
| Donations to authorized charities | Art. 25, Fr. VI |
| Works of art by the artist (import) | Art. 25, Fr. VII |

---

## Step 4: CFDI (Comprobante Fiscal Digital por Internet) Requirements [T1]

**Legislation:** CFF Articles 29, 29-A; RMF Rules 2.7.x

### 4a. CFDI Mandatory Elements

ALL transactions in Mexico require a CFDI. A valid CFDI must contain:

| Element | Field | Description |
|---------|-------|-------------|
| RFC emisor | Emisor > Rfc | Issuer's 12/13-character RFC |
| RFC receptor | Receptor > Rfc | Recipient's RFC (or XAXX010101000 for general public) |
| Uso del CFDI | Receptor > UsoCFDI | Purpose code (G01=acquisition, G03=expenses, I01-I08=investments, etc.) |
| Forma de pago | FormaPago | Payment method (01=cash, 03=transfer, 04=credit card, 06=e-wallet, 99=other) |
| Metodo de pago | MetodoPago | PUE (one-time payment) or PPD (deferred/installments) |
| Lugar de expedicion | LugarExpedicion | ZIP code where issued |
| Regimen fiscal emisor | Emisor > RegimenFiscal | Issuer's tax regime code |
| Moneda | Moneda | Currency code (MXN, USD, EUR, etc.) |
| Tipo de cambio | TipoCambio | Exchange rate if not MXN |
| Tipo de comprobante | TipoDeComprobante | I=ingreso, E=egreso, T=traslado, P=pago, N=nomina |
| Impuestos trasladados | Impuestos > Traslados | IVA transferred (output) |
| Impuestos retenidos | Impuestos > Retenciones | IVA withheld (if applicable) |
| UUID (folio fiscal) | Complemento > TimbreFiscalDigital > UUID | Unique identifier assigned by PAC |
| Sello digital SAT | Complemento > TimbreFiscalDigital > SelloSAT | SAT digital seal |

### 4b. CFDI Types [T1]

| Type Code | Name | Use |
|-----------|------|-----|
| I | Ingreso | Revenue/sales invoice |
| E | Egreso | Credit note / refund |
| T | Traslado | Transfer of goods (no sale) |
| P | Pago (REP - Recibo Electronico de Pago) | Payment receipt for PPD invoices |
| N | Nomina | Payroll (out of scope for IVA) |

### 4c. CFDI Validation Requirements [T1]

Before crediting input IVA, the CFDI MUST:
1. Have a valid UUID (folio fiscal)
2. Be in "Vigente" (active) status -- NOT "Cancelado"
3. Show the client's correct RFC as receptor
4. Show IVA trasladado separately on the CFDI
5. Have been certified by an authorized PAC
6. Be verifiable on SAT's verification portal

**If CFDI is missing, cancelled, or shows incorrect RFC, input IVA is NOT creditable. No exceptions.**

### 4e. 2026 CFDI Authenticity Requirements [T1]

**Legislation:** CFF Art. 29-A, Fr. IX (added by 2026 reform, effective Jan 1, 2026); CFF Art. 49 Bis

Effective January 1, 2026, CFDIs must reflect real and truthful transactions. Key changes:

1. **Materiality requirement:** A CFDI that does not represent an actual legal act or operation is considered false and loses all tax effects (CFF Art. 29-A, Fr. IX)
2. **SAT verification power:** SAT may request evidence (photos, videos, audio, contracts) to confirm a transaction took place. Taxpayer has 5 business days to respond
3. **Expedited false-CFDI process (Art. 49 Bis):** SAT may suspend digital seals (preventing CFDI issuance) and the taxpayer has 5 business days to prove materiality
4. **Criminal sanctions:** Issuers, recipients, and intermediaries of false CFDIs face criminal liability
5. **Publication:** If a CFDI is determined false, the issuer's RFC is published on SAT's website and in the DOF

### 4d. Complemento de Pago (REP) [T1]

**Legislation:** RMF Rule 2.7.1.32

When MetodoPago = PPD (payment in installments/deferred):
- The original CFDI shows IVA but it is NOT creditable until payment is made
- A Complemento de Pago (REP) must be issued within 5 business days of each payment
- Input IVA becomes creditable ONLY when the REP is issued
- The REP links back to the original CFDI via UUID

**Cash basis (flujo de efectivo):** Mexico's IVA system operates on a cash basis for most taxpayers. IVA is owed/creditable when payment is made/received, not when invoiced. The CFDI + REP system enforces this.

---

## Step 5: IVA Return Structure (Declaracion Mensual) [T1]

**Legislation:** LIVA Article 5-D; CFF Article 31

The monthly IVA return is filed via the SAT portal using the "Declaraciones y Pagos" system. The return calculates:

### 5a. Output IVA (IVA Trasladado / IVA Causado)

| Line | Description | Source |
|------|-------------|--------|
| A1 | Total value of activities at 16% | Sum of 16% rated sales/services/leases |
| A2 | IVA charged at 16% | A1 x 0.16 |
| A3 | Total value of activities at 8% (border zone) | Sum of 8% rated activities |
| A4 | IVA charged at 8% | A3 x 0.08 |
| A5 | Total value of activities at 0% | Sum of zero-rated activities |
| A6 | IVA at 0% | A5 x 0.00 = 0 |
| A7 | Total value of exempt activities | Sum of exempt activities |
| A8 | Total value of activities | A1 + A3 + A5 + A7 |
| A9 | Total IVA charged (IVA causado) | A2 + A4 |

### 5b. Input IVA (IVA Acreditable)

| Line | Description | Source |
|------|-------------|--------|
| B1 | IVA paid on purchases/expenses at 16% | Sum of creditable 16% input IVA |
| B2 | IVA paid on purchases/expenses at 8% | Sum of creditable 8% input IVA |
| B3 | IVA paid on imports | From pedimento (customs entry) |
| B4 | Total IVA paid (IVA acreditable before proportion) | B1 + B2 + B3 |
| B5 | Proportion factor (factor de acreditamiento) | See Step 6 for calculation |
| B6 | Creditable IVA (IVA acreditable) | B4 x B5 (if mixed activities) or B4 (if 100% taxable) |

### 5c. IVA Withheld (IVA Retenido)

| Line | Description | Source |
|------|-------------|--------|
| C1 | IVA withheld by clients | Sum of IVA retained by clients on payments received |
| C2 | IVA withheld from suppliers | Sum of IVA retained from supplier payments |

### 5d. Final Calculation

| Line | Description | Calculation |
|------|-------------|-------------|
| D1 | IVA payable before credits | A9 - B6 |
| D2 | Less: IVA withheld by clients | D1 - C1 |
| D3 | Less: Saldo a favor from prior periods | D2 - prior credit balance |
| D4 | Amount payable (cantidad a cargo) | If positive: pay by deadline |
| D5 | Or: Favorable balance (saldo a favor) | If negative: carry forward or request refund |

---

## Step 6: Input IVA Crediting Rules (Acreditamiento) [T1]

**Legislation:** LIVA Article 4, 4-A, 5, 5-A, 5-B, 5-C, 5-D

### 6a. Requirements for Crediting Input IVA [T1]

ALL of the following must be met (Article 5 LIVA):

1. **IVA must be strictly indispensable (estrictamente indispensable)** for the taxpayer's activities -- equivalent to being deductible for income tax purposes under LISR
2. **IVA must be separately stated** on the CFDI
3. **IVA must have been effectively paid** (cash basis) -- for PPD invoices, only when REP is issued
4. **CFDI must be valid** -- not cancelled, correct RFC, certified by PAC
5. **IVA must be withheld and remitted** when withholding applies (Article 1-A)

### 6b. Proportional Crediting (Acreditamiento Proporcional) [T2]

**Legislation:** LIVA Article 5, Fraction V; Article 5-A, 5-B

When a taxpayer performs BOTH taxable (16%/8%/0%) AND exempt activities:

**Proportion factor (factor de acreditamiento):**

```
Factor = (Value of taxable activities at 16% + 8% + 0%) / (Total value of ALL activities including exempt)
```

- Apply factor to input IVA on expenses that cannot be directly attributed to taxable vs exempt activities
- Input IVA directly attributable to taxable activities: 100% creditable (no factor needed)
- Input IVA directly attributable to exempt activities: 0% creditable (no factor needed)
- Input IVA on shared expenses: creditable x factor

**Annual adjustment (ajuste anual):** At year-end, recalculate the factor using full-year figures and adjust. [T2] -- flag for reviewer.

### 6c. Blocked / Non-Creditable Input IVA [T1]

| Category | Legislation | Rule |
|----------|------------|------|
| Non-indispensable expenses | LIVA Art. 5, Fr. I | Not deductible for LISR = not creditable for IVA |
| Entertainment (gastos de representacion) | LISR Art. 28, Fr. XXI cross-ref | Generally non-deductible; IVA not creditable |
| Gifts to employees (beyond exempt threshold) | LISR Art. 28 cross-ref | Non-deductible portion = IVA not creditable |
| Personal expenses of individuals | LIVA Art. 5 | Not indispensable = not creditable |
| Expenses related to exempt activities | LIVA Art. 5, Fr. V | IVA on exempt-related costs is not creditable |
| CFDI cancelled or invalid | CFF Art. 29, 29-A | No valid CFDI = no credit |
| IVA not separately stated | LIVA Art. 5, Fr. II | Must be shown separately on CFDI |

### 6d. Motor Vehicle Rules [T1]

**Legislation:** LISR Article 36, Fraction II; LIVA Article 5 cross-reference

| Vehicle Type | IVA Creditable? | Cap |
|-------------|----------------|-----|
| Automobiles (general business use) | Yes, up to cap | MXN 175,000 purchase price cap for LISR deduction; IVA creditable proportionally |
| Automobiles (indispensable -- delivery, sales force) | Yes, up to cap | Same MXN 175,000 cap unless exception applies |
| Cargo vehicles (camiones de carga) | Yes, fully | No cap for vehicles designed exclusively for cargo |
| Passenger transport vehicles (taxis, buses) | Yes, fully | Used exclusively in transport services |
| Electric/hybrid vehicles | Yes, up to enhanced cap | MXN 250,000 cap (LISR Art. 36, Fr. II) |
| Motorcycles | Yes, up to cap | Same general rules apply |

**IVA on automobile above the cap:** The IVA attributable to the amount exceeding MXN 175,000 (or MXN 250,000 for electric) is NOT creditable. Calculate: `Creditable IVA = IVA x (cap / purchase price)` when purchase price exceeds cap.

---

## Step 7: IVA Withholding (Retencion de IVA) [T1]

**Legislation:** LIVA Article 1-A

### 7a. When to Withhold IVA [T1]

| Scenario | Withholding Rate | LIVA Reference |
|----------|-----------------|----------------|
| Legal entity pays individual for professional services (honorarios) | 2/3 of IVA (i.e., 10.6667% on base) | Art. 1-A, Fr. II(a) |
| Legal entity pays individual for lease of goods | 2/3 of IVA | Art. 1-A, Fr. II(a) |
| Legal entity pays for land transport of goods (autotransporte terrestre) | 4% of payment | Art. 1-A, Fr. II(c) |
| Payments to commission agents (comisionistas) who are individuals | 2/3 of IVA | Art. 1-A, Fr. II(a) |
| Payments to non-residents without PE in Mexico | 100% of IVA | Art. 1-A, Fr. III |
| Digital platform services (intermediaries) | Varies (per RMF) | Art. 1-A Bis, Transitory rules |
| Outsourced personnel services (subcontratacion) | 6% of payment | Art. 1-A, Fr. IV |

### 7b. Withholding Mechanics [T1]

1. The person making the payment (retenedor) withholds the IVA
2. The withheld IVA is remitted to SAT with the monthly IVA return
3. The person receiving payment credits the IVA withheld against their own IVA liability
4. IVA withholding must be reflected on the CFDI

### 7c. Outsourcing / Subcontracting (Complemento de Pago) [T2]

**Legislation:** LIVA Article 1-A, Fraction IV (added by 2021 reform)

Since the 2021 outsourcing reform:
- Subcontracting of personnel (subcontratacion de personal) is prohibited except for specialized services
- IVA withholding at 6% applies to payments for specialized services/works
- The service provider must be registered in REPSE (Registro de Prestadoras de Servicios Especializados u Obras Especializadas)
- If provider is NOT registered in REPSE, the payment is non-deductible AND IVA is not creditable [T2]

---

## Step 8: Digital Services by Non-Residents [T1]

**Legislation:** LIVA Articles 18-B, 18-C, 18-D, 18-E, 18-F, 18-G, 18-H (added June 2020)

### 8a. Scope

Non-resident digital service providers who provide services to recipients in Mexico must:

1. Register with SAT and obtain an RFC
2. Charge IVA at 16% on digital services to Mexican consumers (B2C)
3. File monthly IVA returns and remit IVA to SAT
4. Issue CFDIs (or equivalent documentation as per SAT rules)

### 8b. Covered Digital Services (Article 18-B)

| Service Type | Examples |
|-------------|----------|
| Downloading/streaming content | Netflix, Spotify, Apple Music, e-books |
| Online intermediation platforms | Uber, Airbnb, Amazon marketplace |
| Online clubs/dating | Match.com, social platforms |
| E-learning | Online courses, webinars |
| Online testing/exercises | Fitness apps with paid content |
| Online news/magazines | Digital newspaper subscriptions |
| Data storage | Dropbox, Google Drive, iCloud |
| Software (SaaS, cloud) | Microsoft 365, Salesforce, Slack |

### 8c. B2B vs B2C Treatment

| Scenario | Treatment |
|----------|-----------|
| Non-resident to Mexican individual (B2C) | Non-resident charges IVA at 16% and remits to SAT |
| Non-resident to Mexican legal entity (B2B) | Mexican entity withholds 100% of IVA (Article 1-A, Fr. III) and remits to SAT; non-resident does not charge IVA |
| Mexican business receiving digital services from non-resident registered with SAT | Withholding still applies per Article 1-A |

### 8e. 2026 Digital Platform Withholding Expansion [T1]

**Legislation:** 2026 Tax Reform (DOF Nov 7, 2025); RMF 2026

Effective January 1, 2026, digital platform intermediaries (marketplaces) must withhold IVA and ISR on payments to sellers transacting through the platform, expanded to include B2B transactions:

| Scenario | IVA Withholding | ISR Withholding |
|----------|----------------|-----------------|
| Seller is Mexican individual with RFC | 50% of IVA | 2.5% of transaction value |
| Seller is Mexican legal entity with RFC | 50% of IVA | 2.5% of transaction value |
| Seller without valid RFC | 100% of IVA | 20% of transaction value |
| Seller is non-resident with goods in Mexico | 100% of IVA | Per applicable rate |
| Payment deposited in foreign bank account (Mexican-sourced income) | 100% of IVA | Per applicable rate |

**Real-time data access:** Platforms must grant SAT online, permanent access to tax information of taxpayers operating through them (effective April 1, 2026). Non-compliance may result in temporary suspension of internet access to the platform.

**CFDI requirement:** Platforms must issue a CFDI de retencion with the "Complemento de Servicios Plataformas Tecnologicas" for each person from whom they withhold.

### 8d. Non-Compliant Non-Residents [T2]

If a non-resident digital service provider fails to register with SAT, the Mexican recipient (if legal entity) must still withhold and remit 100% of the IVA. For individuals receiving from non-compliant providers, SAT may block internet access to the provider's platform (Article 18-H, Fraction III).

---

## Step 9: Import IVA [T1]

**Legislation:** LIVA Articles 24-28

### 9a. Definitive Imports

| Type | Treatment |
|------|-----------|
| Physical goods imported definitively | IVA at 16% collected by Customs (Aduana) at point of entry |
| IVA paid on import | Creditable as input IVA if goods used in taxable activities |
| Documentation | Pedimento de importacion (customs entry) is the supporting document |

### 9b. Temporary Imports

| Type | Treatment |
|------|-----------|
| Temporary import (general) | Exempt from IVA (Article 25, Fr. I) -- must be re-exported within timeframe |
| IMMEX temporary imports | Special regime [T3] -- complex rules on virtual exports, deemed imports |
| Temporary imports converted to definitive | IVA becomes due at time of conversion |

### 9c. IMMEX / Maquiladora [T3]

**Legislation:** IMMEX Decree; LIVA Articles 24-28; Certification rules (IVA/IEPS certification)

IMMEX operations involve complex IVA treatment including:
- Temporary import without IVA (with certification) or with IVA guarantee
- Virtual exports and imports between IMMEX companies
- Transfer pricing implications
- IVA/IEPS Certification (Certificacion de IVA e IEPS) allowing IVA credit on temporary imports

**ESCALATE: All IMMEX/maquiladora IVA matters to licensed Contador Publico with IMMEX experience. Do not attempt to classify these transactions.**

---

## Step 10: Filing Deadlines and Penalties [T1]

**Legislation:** LIVA Article 5-D; CFF Articles 73, 76, 78

### 10a. Filing Deadlines

| Obligation | Deadline | Legislation |
|-----------|----------|-------------|
| Monthly IVA return (declaracion definitiva) | 17th of the month following the reporting period | LIVA Art. 5-D |
| Annual informativa (DIOT - Declaracion Informativa de Operaciones con Terceros) | Last day of the month following the reporting period (per RMF Rule 4.5.1; note: NOT the 17th) | LIVA Art. 32, Fr. VIII; RMF 4.5.1 |
| IVA withholding remittance | Same as monthly return (17th) | LIVA Art. 1-A |
| Saldo a favor refund request | Within 5 years of when saldo a favor arose | CFF Art. 22 |

### 10b. Penalties for Late Filing

| Violation | Penalty Range |
|-----------|--------------|
| Late payment of IVA | Surcharges (recargos) at rate set by CFF (~1.47%/month approx.) |
| Late filing | CFF Art. 82: MXN 1,810 to MXN 22,400 per return (updated annually) |
| Failure to issue CFDI | CFF Art. 83, Fr. VII: MXN 17,020 to MXN 97,330 per CFDI |
| Failure to withhold IVA | 100% of unwithheld amount plus recargos |
| Incorrect IVA claimed | 55-75% of incorrectly credited IVA (CFF Art. 76) |

---

## Step 11: Key Thresholds [T1]

| Threshold | Value | Legislation |
|-----------|-------|-------------|
| RESICO individuals income limit | MXN 3,500,000 annual | LISR Art. 113-E |
| Automobile deduction cap (general) | MXN 175,000 | LISR Art. 36, Fr. II |
| Automobile deduction cap (electric/hybrid) | MXN 250,000 | LISR Art. 36, Fr. II |
| Small taxpayer DIOT exemption | None -- all taxpayers must file DIOT | LIVA Art. 32 |
| Border zone rate eligibility | 18 months of domicile | Decree |
| Digital services provider registration | Any amount of services to Mexican recipients | LIVA Art. 18-D |
| CFDI cancellation window | Up to the month in which the annual ISR return for the fiscal year of issuance must be filed (March for legal entities, April for individuals); recipient acceptance required | CFF Art. 29-A (2026 reform); RMF 2.7.1.47 |

---

## Step 12: DIOT (Declaracion Informativa de Operaciones con Terceros) [T1]

**Legislation:** LIVA Article 32, Fractions V and VIII

### 12a. What is DIOT?

The DIOT is an informational return filed monthly (by the last day of the following month, per RMF 4.5.1). It reports all transactions with third parties (suppliers) where IVA was involved.

**2025/2026 Platform Change:** As of August 1, 2025, the DIOT must be submitted exclusively through SAT's new digital platform (Comunicado 042-2025). The previous desktop application is no longer accepted, even for late filings of prior periods. The new form has expanded from 24 to 54 fields and supports automatic batch loading (carga batch) via .txt format for over 40,000 records.

### 12b. DIOT Data Requirements

| Field | Description |
|-------|-------------|
| RFC of supplier | Supplier's RFC |
| Type of third party | Nacional (domestic), Extranjero (foreign), Global (public at large) |
| Type of operation | Services, goods, lease, others |
| Taxable value at 16% | Base amount subject to 16% |
| IVA paid at 16% | IVA amount |
| Taxable value at 15% (legacy) | Historical rate |
| Taxable value at 8% | Border zone base |
| IVA paid at 8% | Border zone IVA |
| Zero-rated value | Base amount at 0% |
| Exempt value | Base amount exempt |
| IVA withheld | Amount withheld |

### 12c. DIOT Exceptions

- RESICO individuals are exempt from DIOT filing
- Taxpayers using "Mi Contabilidad" simplified tool may be exempt per RMF

---

## PROHIBITIONS [T1]

- NEVER credit input IVA without a valid, non-cancelled CFDI with IVA separately stated
- NEVER apply the 8% border zone rate without verified eligibility for ALL conditions
- NEVER credit IVA on PPD invoices until the corresponding REP (Complemento de Pago) has been issued
- NEVER credit IVA on expenses that are non-deductible for income tax purposes (LISR)
- NEVER classify salary/payroll (nomina), loan repayments, dividends, or income tax payments as IVA-relevant
- NEVER apply zero-rate to processed/prepared food consumed on premises (restaurants charge 16%)
- NEVER forget IVA withholding when a legal entity pays an individual for professional services
- NEVER treat exempt supplies as zero-rated -- they have opposite input IVA treatment
- NEVER credit IVA on automobile purchases above the MXN 175,000 cap (proportional calculation required)
- NEVER file IVA on an accrual basis -- Mexico IVA is cash-basis (flujo de efectivo) for almost all taxpayers
- NEVER allow IMMEX/maquiladora IVA classification without specialist review [T3]
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Step 13: Comparison with EU VAT System

| Feature | Mexico IVA | EU VAT (e.g., Malta) |
|---------|-----------|---------------------|
| Standard rate | 16% | Varies (18% Malta, 21% Germany, etc.) |
| Reduced rates | 0% (zero-rated), 8% (border zone) | Multiple reduced rates per country |
| Invoicing | CFDI mandatory electronic (XML + PAC seal) | Paper or e-invoicing (varies by country) |
| Tax basis | Cash basis (flujo de efectivo) | Accrual basis (generally) |
| Filing frequency | Monthly | Varies (monthly, quarterly, annual) |
| Intra-community acquisitions | N/A -- no trade bloc equivalent | Yes (reverse charge on IC acquisitions) |
| Reverse charge on imports | No -- IVA collected by Customs on goods; withholding on services | Yes (self-assessment in many cases) |
| Withholding mechanism | Extensive (individuals, outsourcing, non-residents) | Generally not used for domestic supplies |
| Digital services (B2C foreign) | Non-resident must register and charge 16% | OSS/IOSS one-stop shop within EU |
| Place of supply (services) | Where effectively used/enjoyed (aprovechamiento) | Generally where recipient is established (B2B) |
| Proportional credit | Factor de acreditamiento (annual adjustment) | Pro-rata recovery with annual adjustment |
| Capital goods scheme | Standard depreciation rules (LISR) | Adjustment period (e.g., 5-10 years in Malta) |

---

## Step 14: Edge Case Registry

### EC1 -- Restaurant meals (comidas de negocios) [T1]
**Situation:** Business pays for a client lunch at a restaurant. CFDI issued at 16% IVA.
**Resolution:** Restaurant meals are taxable at 16% (NOT zero-rated even though food). IVA is generally NOT creditable because entertainment/business meals are non-deductible under LISR Article 28, Fraction XXI. Exception: meals may be partially deductible (up to 91.5% if paid electronically and CFDI obtained) but this is an income tax rule. For IVA, the deductible portion of the expense allows crediting the corresponding IVA portion. [T2] -- flag for reviewer to confirm deductibility percentage.
**Legislation:** LIVA Art. 5, Fr. I; LISR Art. 28, Fr. XX and XXI.

### EC2 -- Uber/ride-hailing services received [T1]
**Situation:** Business uses Uber for employee transport. Uber issues CFDI.
**Resolution:** Uber is a digital intermediation platform. IVA at 16% applies. If Uber issues a valid CFDI to the business, IVA is creditable as a transport expense (if indispensable for business). Verify CFDI is in the business's RFC.
**Legislation:** LIVA Art. 18-B; Art. 5.

### EC3 -- Payment to foreign freelancer (programmer, designer) [T1]
**Situation:** Mexican company pays a US-based freelancer for software development. No CFDI issued by freelancer.
**Resolution:** This is an import of services. Mexican company must withhold 100% of IVA (16% on the fee) under Article 1-A, Fraction III. The company must self-issue a CFDI or use the SAT foreign supplier module. The withheld IVA is remitted to SAT. The company can credit the IVA paid as input IVA if the service is for taxable activities.
**Legislation:** LIVA Art. 1-A, Fr. III; Art. 24, Fr. V.

### EC4 -- CFDI issued with incorrect RFC [T1]
**Situation:** Supplier issues CFDI with a typo in the client's RFC.
**Resolution:** IVA is NOT creditable until corrected. Request a replacement CFDI (cancellation of incorrect + reissuance with correct RFC). The original incorrect CFDI provides zero IVA credit.
**Legislation:** CFF Art. 29-A; LIVA Art. 5, Fr. II.

### EC5 -- Credit note (nota de credito) [T1]
**Situation:** Client receives a credit note (CFDI tipo E - Egreso) from a supplier.
**Resolution:** The credit note reduces the original IVA charged. The client must reduce their input IVA credit by the IVA amount on the credit note. If already credited, adjust in the month the credit note is received.
**Legislation:** LIVA Art. 7; CFF Art. 29, complemento CFDI tipo E.

### EC6 -- Gasoline/fuel purchases [T1]
**Situation:** Business purchases gasoline for company vehicles. CFDI obtained.
**Resolution:** IVA on fuel is creditable IF: (a) valid CFDI with IVA separated, (b) paid with electronic means (credit/debit card, transfer -- NOT cash for amounts over MXN 2,000), (c) vehicle is used for business purposes. If vehicle is subject to the MXN 175,000 cap, fuel IVA is still fully creditable (the cap applies to the vehicle purchase, not operating expenses).
**Legislation:** LIVA Art. 5; LISR Art. 27, Fr. III (electronic payment requirement).

### EC7 -- Advance payments (anticipos) [T1]
**Situation:** Client pays an advance on a construction project. Supplier issues CFDI for the advance.
**Resolution:** IVA is owed on the advance at the time of receipt (cash basis). Supplier must issue CFDI tipo I (ingreso) for the advance. Input IVA is creditable by the payer when the CFDI is received and payment is made. When final CFDI is issued, the advance is deducted from the total, and IVA is adjusted accordingly.
**Legislation:** LIVA Art. 1-B; RMF Rule 2.7.1.35.

### EC8 -- Mixed-use property rental [T2]
**Situation:** Client rents a property that is partially residential and partially commercial (e.g., ground floor shop, upper floor apartment).
**Resolution:** The commercial portion is subject to IVA at 16%. The residential portion is exempt. A reasonable allocation must be made (typically by square meters). Input IVA on shared expenses follows proportional crediting. [T2] -- flag for reviewer to confirm allocation method.
**Legislation:** LIVA Art. 15, Fr. II (residential exemption); Art. 20, Fr. II; Art. 5, Fr. V (proportional crediting).

### EC9 -- Salary vs. professional services (honorarios) [T2]
**Situation:** Company pays an individual who might be an employee or independent contractor.
**Resolution:** If the individual is truly independent (not subordinated), payment is for professional services (honorarios) -- subject to IVA at 16% and the company must withhold 2/3 of IVA. If the relationship is actually employment (subordinated), it is salary -- OUT OF SCOPE for IVA. Misclassification is a significant risk. [T2] -- flag for reviewer. Consider LISR subordination indicators.
**Legislation:** LIVA Art. 1-A, Fr. II(a); LISR Art. 94 (employment definition); LFT (Federal Labor Law) subordination test.

### EC10 -- IVA on real estate purchase [T2]
**Situation:** Company buys commercial real estate.
**Resolution:** Land is EXEMPT from IVA (Article 9, Fr. I). Construction/building is subject to IVA at 16%. The purchase price must be split between land and construction. The notario (notary public) typically handles this split on the escritura (deed). Only the IVA on the construction portion is creditable. [T2] -- verify split with notarial deed.
**Legislation:** LIVA Art. 9, Fr. I (land exempt); Art. 1 (construction taxable).

### EC11 -- Cryptocurrency / digital assets [T3]
**Situation:** Client receives payment in cryptocurrency or trades digital assets.
**Resolution:** SAT has not issued definitive IVA guidance on cryptocurrency transactions. The treatment depends on whether the crypto is classified as a good, service, or financial instrument. ESCALATE to specialist. Do not classify.
**Legislation:** No specific LIVA provision. CFF general principles. SAT Prodecon criteria pending.

### EC12 -- Donations to authorized charities (donatarias autorizadas) [T1]
**Situation:** Company makes a donation to an authorized charity.
**Resolution:** Donations are NOT subject to IVA (not a taxable activity -- no enajenacion, prestacion de servicios, or uso/goce). No IVA is charged or credited. The donation may be deductible for income tax (LISR Art. 27, Fr. I) up to limits, but this is outside IVA scope.
**Legislation:** LIVA Art. 8 (enajenacion does not include donations to donatarias autorizadas).

### EC13 -- Intercompany services within Mexico [T1]
**Situation:** Parent company provides management services to subsidiary. Both are Mexican entities.
**Resolution:** Intercompany services are subject to IVA at 16% like any other domestic service. CFDI must be issued. Transfer pricing rules (LISR Art. 76 and 179-184) require arm's length pricing but this is an income tax matter. For IVA: charge 16%, issue CFDI, subsidiary credits input IVA normally.
**Legislation:** LIVA Art. 14 (services); Art. 1 (taxable activities between related parties).

### EC14 -- Return/refund of goods previously sold [T1]
**Situation:** Customer returns goods that were sold with IVA.
**Resolution:** Issue CFDI tipo E (Egreso / credit note). Reduce output IVA by the IVA on the credit note in the month of return. If the customer had credited the input IVA, they must reduce their credit accordingly. The CFDI E must reference the original CFDI I via UUID.
**Legislation:** LIVA Art. 7; CFF Art. 29.

---

## Step 15: Reviewer Escalation Protocol

When Claude identifies a [T2] situation, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment Claude considers most likely correct and why]
Action Required: Licensed Contador Publico must confirm before filing.
```

When Claude identifies a [T3] situation, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed Contador Publico with relevant specialty. Document gap.
```

---

## Step 16: Test Suite

These reference transactions have known correct outputs. Use to validate skill execution.

### Test 1 -- Standard domestic sale at 16%
**Input:** Mexican company sells consulting services to domestic client for MXN 100,000 net. CFDI tipo I issued at 16% IVA.
**Expected output:** A1 = MXN 100,000, A2 = MXN 16,000. Output IVA of MXN 16,000 included in IVA causado.

### Test 2 -- Standard domestic purchase at 16%, overhead
**Input:** Mexican company purchases office supplies from domestic supplier for MXN 5,000 net + MXN 800 IVA. Valid CFDI received. Paid via bank transfer.
**Expected output:** B1 += MXN 800 (input IVA creditable). DIOT entry for supplier required.

### Test 3 -- Zero-rated sale (food products)
**Input:** Agricultural company sells fresh vegetables (unprocessed) to distributor for MXN 200,000 net. CFDI at tasa 0%.
**Expected output:** A5 = MXN 200,000, A6 = MXN 0. Input IVA on related purchases remains fully creditable.

### Test 4 -- Exempt sale (residential rent)
**Input:** Individual rents residential property for MXN 12,000/month. No IVA charged.
**Expected output:** A7 += MXN 12,000. No output IVA. Input IVA on related expenses is NOT creditable.

### Test 5 -- Professional services with IVA withholding
**Input:** Legal entity pays individual accountant MXN 50,000 for professional services. Accountant's CFDI shows IVA of MXN 8,000 (16%).
**Expected output:** Legal entity withholds 2/3 of IVA = MXN 5,333.33. Legal entity credits input IVA of MXN 8,000 (B1). Legal entity remits withheld MXN 5,333.33 to SAT. Accountant receives MXN 50,000 + MXN 2,666.67 (1/3 IVA not withheld).

### Test 6 -- Import of physical goods
**Input:** Company imports computer equipment from China. Customs value MXN 300,000. Pedimento shows IVA of MXN 48,000 (16%) paid at Aduana.
**Expected output:** B3 += MXN 48,000 (input IVA from import, creditable). Supporting document is pedimento, not CFDI.

### Test 7 -- Border zone sale at 8%
**Input:** Company in Tijuana (northern border zone, verified eligible) sells goods to local customer for MXN 80,000 net. CFDI at 8%.
**Expected output:** A3 = MXN 80,000, A4 = MXN 6,400. [T2] flag: border zone eligibility must be confirmed by reviewer.

### Test 8 -- Automobile purchase exceeding cap
**Input:** Company purchases sedan for general business use at MXN 350,000 + IVA MXN 56,000 (16%). Valid CFDI.
**Expected output:** Creditable IVA = MXN 56,000 x (175,000 / 350,000) = MXN 28,000. Remaining MXN 28,000 IVA is NOT creditable (non-deductible for LISR above cap).

### Test 9 -- Digital services from non-resident (B2B)
**Input:** Mexican company pays Netflix MXN 15,000/month for corporate subscription. Netflix is SAT-registered non-resident.
**Expected output:** Mexican company withholds 100% of IVA = MXN 2,400 (16%). Company remits MXN 2,400 to SAT. Company credits MXN 2,400 as input IVA if used for taxable activities.

### Test 10 -- PPD invoice, payment not yet made
**Input:** Supplier issues CFDI with MetodoPago=PPD for MXN 100,000 + MXN 16,000 IVA. No payment has been made yet and no REP issued.
**Expected output:** IVA of MXN 16,000 is NOT creditable in this period. Will become creditable only when payment is made AND REP (Complemento de Pago) is issued.

### Test 11 -- Credit note received
**Input:** Supplier issues CFDI tipo E (credit note) for MXN 10,000 + MXN 1,600 IVA, referencing original invoice UUID.
**Expected output:** Reduce input IVA by MXN 1,600. B1 -= MXN 1,600 in the month the credit note is received.

### Test 12 -- Mixed activities (taxable + exempt), proportional crediting
**Input:** Company has monthly taxable sales of MXN 800,000 and exempt sales of MXN 200,000. Total input IVA on shared expenses = MXN 32,000.
**Expected output:** Factor = 800,000 / 1,000,000 = 0.80. Creditable IVA on shared expenses = MXN 32,000 x 0.80 = MXN 25,600. Remaining MXN 6,400 is non-creditable expense. [T2] -- annual adjustment required.

---

## Contribution Notes

If you are adapting this skill for another Latin American country, you must:

1. Replace all legislation references (LIVA, CFF, LISR) with the equivalent national legislation.
2. Replace CFDI requirements with your jurisdiction's invoicing system (e.g., factura electronica in Colombia, boleta in Chile).
3. Replace IVA rates with your jurisdiction's rates.
4. Replace withholding rules with your jurisdiction's equivalent.
5. Replace SAT references with your jurisdiction's tax authority.
6. Replace border zone rules if not applicable.
7. Replace the automobile deduction cap with your jurisdiction's equivalent.
8. Have a licensed accountant/tax professional in your jurisdiction validate every T1 rule before publishing.
9. Add your own edge cases for known ambiguous situations.
10. Run all test suite cases against your jurisdiction's rules.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
