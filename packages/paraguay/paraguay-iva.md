---
name: paraguay-iva
description: Use this skill whenever asked to prepare, review, or create a Paraguay IVA (Impuesto al Valor Agregado) return for any client. Trigger on phrases like "prepare IVA return", "do the IVA", "Paraguay VAT", or any request involving Paraguay value added tax filing. ALWAYS read this skill before touching any Paraguay IVA-related work.
---

# Paraguay IVA Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Paraguay |
| Jurisdiction Code | PY |
| Primary Legislation | Ley 125/91 (Ley de Reforma Tributaria), Libro III -- IVA (as amended by Ley 6380/2019) |
| Supporting Legislation | Decreto 1030/2020 (Reglamento IVA); Resoluciones SET |
| Tax Authority | Subsecretaria de Estado de Tributacion (SET) |
| Filing Portal | https://www.set.gov.py (Marangatú System) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, return form, input recovery. Tier 2: partial exemption, maquila, IVA agropecuario. Tier 3: complex structures, rulings. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Step 0: Client Onboarding Questions

1. **Entity name and RUC** [T1]
2. **Tax regime** [T1] -- IRE General, IRE Simple, RESIMPLE, or IRP
3. **Filing period** [T1] -- monthly (standard)
4. **Industry/sector** [T2] -- agriculture (IVA Agropecuario), manufacturing, maquila
5. **Does the business make exempt supplies?** [T2]
6. **Does the business import goods?** [T1]
7. **Is the business under maquila regime?** [T2]
8. **Credit balance brought forward** [T1]

**If items 1-3 are unknown, STOP.**

---

## Step 1: IVA Rate Structure [T1]

**Legislation:** Ley 125/91, Article 91 (as amended by Ley 6380/2019).

### Standard Rate

| Rate | Application |
|------|-------------|
| 10% | Standard rate on most taxable supplies of goods and services [T1] |

### Reduced Rate

| Rate | Application |
|------|-------------|
| 5% | Agricultural products (unprocessed), pharmaceutical products, certain basic goods, residential rental, interest on loans, sale of real estate [T1] |

### Items at Reduced Rate (5%) [T1]

**Legislation:** Ley 125/91, Article 91.

- Unprocessed agricultural and livestock products (first sale)
- Pharmaceutical and medicinal products
- Capital goods (machinery, equipment for production)
- Residential rental income
- Interest and commissions on financial loans
- Sale of real estate (first transfer)
- Public passenger transportation

### Exempt Supplies [T1]

**Legislation:** Ley 125/91, Article 83.

**Exempt goods:**
- Fresh fruits and vegetables (in their natural state, sold by producer)
- Live animals (sold by producer)
- Basic food products: bread, yerba mate, fresh milk, eggs (specific list)
- Fuel and petroleum derivatives (subject to specific tax -- ISC)
- Books, newspapers, educational materials
- Agricultural inputs (certain seeds, fertilizers)

**Exempt services:**
- Educational services (authorized institutions)
- Health/medical services (public institutions, hospitals)
- Financial intermediation (deposits, certain banking services)
- Residential rental (up to certain value -- but NOTE: rental above threshold is at 5%) [T2]
- Public services (water, electricity -- domestic consumption below threshold)

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]
- Sale (IVA debito -- output) or Purchase (IVA credito -- input)
- Salaries, IPS (social security), dividends, loans = OUT OF SCOPE

### 2b. Determine Counterparty Location [T1]
- Domestic (Paraguay)
- MERCOSUR: Argentina, Brazil, Uruguay
- International

### 2c. Determine IVA Rate [T1]
- 0% (export), 5% (reduced), 10% (standard), or exempt

---

## Step 3: IVA Return Form Structure (Formulario 120) [T1]

**Filed monthly via Marangatú system.**

### IVA Debito (Output)

| Line | Description |
|------|-------------|
| 1 | Ventas gravadas al 10% |
| 2 | IVA debito al 10% |
| 3 | Ventas gravadas al 5% |
| 4 | IVA debito al 5% |
| 5 | Exportaciones (0%) |
| 6 | Ventas exentas |
| 7 | Total ventas |
| 8 | Total IVA debito (Line 2 + Line 4) |

### IVA Credito (Input)

| Line | Description |
|------|-------------|
| 9 | IVA en compras al 10% |
| 10 | IVA en compras al 5% |
| 11 | IVA en importaciones |
| 12 | Total IVA credito |
| 13 | Ajustes |
| 14 | IVA credito neto |

### Liquidacion

| Line | Description |
|------|-------------|
| 15 | IVA a pagar (Line 8 - Line 14) |
| 16 | Saldo a favor anterior |
| 17 | Retenciones |
| 18 | Total a pagar / saldo a favor |

---

## Step 4: IVA Withholding [T1]

**Legislation:** Resoluciones SET.

### Withholding Agents [T1]

| Agent Type | Rate |
|------------|------|
| Government entities | 30% of IVA invoiced [T1] |
| Designated large taxpayers | 30% of IVA [T1] |
| Exporters | 30% of IVA on local purchases [T1] |
| Purchasers from occasional taxpayers | 100% of IVA [T1] |

---

## Step 5: Reverse Charge on Imported Services [T1]

**Legislation:** Ley 125/91, Article 82.

When a Paraguay registered person receives services from a non-resident:

1. Self-assess IVA at applicable rate (10% or 5%) [T1]
2. Report as output IVA [T1]
3. Claim as input if for taxable operations [T1]
4. Net = zero for fully taxable businesses [T1]

---

## Step 6: Deductibility Check

### Blocked Input IVA (No Recovery) [T1]

**Legislation:** Ley 125/91, Article 86.

- **Motor vehicles** -- passenger vehicles (exception: rental, taxi, transport) [T1]
- **Entertainment** -- meals, recreation (unless hospitality) [T1]
- **Personal use** [T1]
- **Exempt operations** -- costs attributable to exempt supplies [T1]
- **Purchases without valid comprobante (factura, boleta, autofactura)** [T1]

### Invoice Requirement [T1]
- Paraguay has implemented SIFEN (Sistema Integrado de Facturacion Electronica)
- Electronic documents (DE -- Documento Electronico) required for most taxpayers
- Valid timbrado (authorization) required for paper invoices (being phased out)
- Input IVA only deductible with valid fiscal document

### Partial Exemption [T2]
- Direct attribution + proportional for common costs
- `Recovery % = (Taxable Sales / Total Sales) * 100`
- Flag for reviewer

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory IVA registration | All IRE taxpayers (companies, sole proprietors above threshold) |
| RESIMPLE | Micro and small enterprises with income up to PYG 80,000,000/year -- simplified regime [T2] |
| Electronic invoicing (SIFEN) | Mandatory phased rollout |

---

## Step 8: Filing Deadlines and Penalties [T1]

**Legislation:** Ley 125/91; Ley 6380/2019; Codigo Tributario.

### Filing Deadlines [T1]

Filing date depends on the last digit of the RUC:

| Last Digit of RUC | Due Date (of following month) |
|-------------------|-------------------------------|
| 0 | 7th |
| 1 | 9th |
| 2 | 11th |
| 3 | 13th |
| 4 | 15th |
| 5 | 17th |
| 6 | 19th |
| 7 | 21st |
| 8 | 23rd |
| 9 | 25th |

### Penalties

| Violation | Penalty |
|-----------|---------|
| Late filing | Multa (fine) per SET resolution [T1] |
| Late payment | Interest at rate set by Central Bank + recargo [T1] |
| Failure to register | Fines + back-assessment [T1] |
| Failure to issue comprobante | Fines + potential closure [T1] |
| Fraud | Criminal penalties [T1] |

---

## Step 9: Classification Matrix [T1]

### Domestic Purchases

| Category | IVA Rate | Input Credit | Notes |
|----------|---------|--------------|-------|
| Office supplies | 10% | Yes | |
| Commercial rent | 10% | Yes | |
| Residential rent | 5% | Yes (if for business) | Tasa reducida |
| Electricity (commercial) | 10% | Yes | |
| Telephone/internet | 10% | Yes | |
| Motor car | 10% | BLOCKED | |
| Entertainment | 10% | BLOCKED | |
| Professional services | 10% | Yes | |
| Agricultural products (first sale) | 5% | Yes | |
| Medicines | 5% | Yes | Tasa reducida |
| Capital goods (machinery) | 5% | Yes | Tasa reducida |
| Insurance (general) | 10% | Yes | |
| Financial interest | 5% | Yes (if for business) | |

### Sales

| Category | IVA | Return Line |
|----------|-----|-------------|
| Domestic sale (standard) | 10% | Line 1, Line 2 |
| Domestic sale (reduced) | 5% | Line 3, Line 4 |
| Export | 0% | Line 5 |
| Exempt | Exempt | Line 6 |

---

## Step 10: Agricultural (IVA Agropecuario) Rules [T2]

**Legislation:** Ley 125/91; Ley 6380/2019.

- Agricultural producers selling unprocessed products: 5% IVA [T1]
- Purchasers from small unregistered producers: issue autofactura and self-assess IVA [T1]
- Agricultural cooperatives: may have special treatments [T2]
- Agricultural inputs: some exempt, some at 5% [T2]
- Flag for reviewer: agricultural sector has numerous special provisions

---

## Step 11: Maquila Regime [T2]

**Legislation:** Ley 1064/97 (Ley de Maquila).

- Maquila companies: special IVA treatment on imports and exports
- Inputs imported for maquila processing: may be exempt from IVA
- Finished goods exported: zero-rated
- Flag for reviewer: maquila benefits require CNIME authorization

---

## Step 11a: SIFEN Electronic Invoicing [T1]

**Legislation:** Decreto 3585/2020; SET Resoluciones.

Paraguay is implementing SIFEN (Sistema Integrado de Facturacion Electronica):

### Types of Electronic Documents (DE)

| Document | Code | Use | Supports IVA Credit |
|----------|------|-----|-------------------|
| Factura Electronica | FE | Standard sales | YES [T1] |
| Autofactura Electronica | AFE | Purchase from informal sector | YES [T1] |
| Nota de Credito Electronica | NCE | Returns, corrections | YES (reduces IVA) [T1] |
| Nota de Debito Electronica | NDE | Additional charges | YES [T1] |
| Nota de Remision Electronica | NRE | Transport documents | NO [T1] |

### SIFEN Requirements [T1]

1. Phased mandatory rollout based on taxpayer size
2. Documents authorized electronically by SET
3. Each DE has a unique CDC (Codigo de Control Digital)
4. XML format with digital signature
5. Paper timbrado still valid for non-SIFEN taxpayers (transitional)

### Timbrado (Paper Authorization) [T1]

For taxpayers not yet on SIFEN:
- All invoices must have valid timbrado (authorization number from SET)
- Timbrado has a validity period (fecha de inicio / fecha de vencimiento)
- Expired timbrado = invalid factura = NO credito fiscal [T1]
- Verify timbrado validity on SET website

---

## Step 11b: Sector-Specific Rules [T2]

### Agriculture and Livestock

- Paraguay is a major agricultural exporter (soybeans, beef, grains)
- First sale of unprocessed agricultural products: IVA at 5% [T1]
- Processed agricultural products: IVA at 10% [T1]
- Exports of agricultural products: zero-rated [T1]
- Autofactura: used when purchasing from small unregistered producers [T1]
- Agricultural cooperatives: IVA applies normally, but cooperative structure may affect income tax [T2]

### Real Estate

- First sale of new real estate: IVA at 5% [T1]
- Subsequent sales: IVA at 5% [T2]
- Commercial rental: IVA at 10% [T1]
- Residential rental: IVA at 5% [T1]
- Construction services: IVA at 10% [T1]
- Land (bare): exempt [T2]

### Financial Services

- Interest on loans: IVA at 5% [T1]
- Banking commissions and fees: IVA at 10% [T1]
- Insurance premiums (life): exempt [T1]
- Insurance premiums (general): IVA at 10% [T1]
- Leasing (arrendamiento financiero): IVA at 5% [T1]

### Telecommunications

- All telecom services: IVA at 10% [T1]
- Internet services: IVA at 10% [T1]
- Prepaid cards: IVA included [T1]

### Digital Services [T2]

- Digital services from non-residents: subject to IVA at 10% via reverse charge
- Streaming, cloud computing, digital advertising: buyer self-assesses
- Flag for reviewer: digital taxation rules are evolving

---

## Step 11c: RESIMPLE Regime [T2]

**Legislation:** Ley 6380/2019.

- Micro and small enterprises with annual income up to PYG 80,000,000
- Simplified regime substituting IVA, IRACIS, and other obligations
- RESIMPLE taxpayers do NOT charge IVA separately
- Buyers CANNOT claim IVA credit on RESIMPLE purchases
- Fixed periodic payments based on income bracket

---

## Step 11d: Libro de Compras y Ventas [T1]

All IVA taxpayers must maintain:

- **Libro de Compras**: purchases with factura/DE details, RUC of supplier, date, base (by rate 5%/10%), IVA, total
- **Libro de Ventas**: sales with factura/DE details, RUC of customer, date, base (by rate), IVA, total
- Electronic submission via Marangatú system (HECHAUKA)
- Summary totals reconcile to Formulario 120
- Retention: minimum 5 years

---

## PROHIBITIONS [T1]

- NEVER let AI guess IVA classification
- NEVER allow input credit on blocked categories
- NEVER allow input credit without valid fiscal document (timbrado or SIFEN)
- NEVER confuse 10% standard with 5% reduced rate
- NEVER apply reverse charge to out-of-scope categories
- NEVER confuse zero-rated exports with exempt supplies
- NEVER compute any number -- all arithmetic is handled by the deterministic engine

---

## Step 12: Edge Case Registry

### EC1 -- Agricultural first sale at 5% [T1]
**Situation:** Farmer sells soybeans to processor.
**Resolution:** First sale of unprocessed agricultural product at 5%. Processor claims input IVA credit at 5%.

### EC2 -- Imported software [T1]
**Situation:** Paraguay company subscribes to US cloud service. No IVA.
**Resolution:** Self-assess IVA at 10%. Output and input. Net = zero.

### EC3 -- Capital goods purchase at 5% [T1]
**Situation:** Company purchases industrial machinery.
**Resolution:** Capital goods (machinery, equipment for production) are at reduced rate of 5%. Input IVA at 5% is fully recoverable.

### EC4 -- Credit notes [T1]
**Situation:** Client issues nota de credito.
**Resolution:** Reduce output IVA. Must be valid fiscal document. Report net.

### EC5 -- Residential rental at 5% [T1]
**Situation:** Company rents apartment for employee housing.
**Resolution:** Residential rental is at 5% IVA. Input credit available if for business purposes. If personal use, BLOCKED.

### EC6 -- Financial interest received [T1]
**Situation:** Company earns interest on a loan made to another company.
**Resolution:** Interest on loans is taxable at 5%. Report on Line 3/Line 4.

### EC7 -- Autofactura for informal purchases [T1]
**Situation:** Business purchases agricultural products from unregistered farmer.
**Resolution:** Issue autofactura. Self-assess IVA at 5%. Input credit available. Withhold and remit IVA on behalf of seller.

### EC8 -- MERCOSUR import [T1]
**Situation:** Company imports goods from Brazil.
**Resolution:** IVA paid at customs on CIF + duties at 10%. Input credit available. No special MERCOSUR IVA treatment -- each country applies own IVA.

---

## Step 13: Test Suite

### Test 1 -- Standard local purchase, 10%
**Input:** PY supplier, office supplies, gross PYG 11,000,000, IVA PYG 1,000,000, net PYG 10,000,000. Valid SIFEN document.
**Expected output:** Line 9 = PYG 1,000,000 input IVA. Full recovery.

### Test 2 -- Export, zero-rated
**Input:** Exporter ships soybeans to Argentina, net PYG 500,000,000.
**Expected output:** Line 5 = PYG 500,000,000. No output IVA. Input IVA fully recoverable.

### Test 3 -- Motor vehicle, blocked
**Input:** Purchase sedan PYG 150,000,000, IVA PYG 15,000,000.
**Expected output:** IVA PYG 15,000,000 BLOCKED. No input credit.

### Test 4 -- Agricultural sale at 5%
**Input:** Farmer sells cattle PYG 50,000,000 (PYG 47,619,048 + IVA PYG 2,380,952 at 5%).
**Expected output:** Line 3 = PYG 47,619,048. Line 4 = PYG 2,380,952.

### Test 5 -- Capital goods at 5%
**Input:** Industrial machinery PYG 100,000,000 + IVA PYG 5,000,000 (5%).
**Expected output:** Line 10 = PYG 5,000,000 input IVA at reduced rate. Full recovery.

### Test 6 -- Imported services, reverse charge
**Input:** US consulting, USD 5,000 (~ PYG 37,000,000). No IVA.
**Expected output:** Self-assess output IVA = PYG 3,700,000 (10%). Input = PYG 3,700,000. Net = zero.

### Test 7 -- Exempt supply (education)
**Input:** School earns PYG 20,000,000 from tuition.
**Expected output:** Line 6 = PYG 20,000,000. No output IVA. Input IVA NOT recoverable.

### Test 8 -- Entertainment, blocked
**Input:** Client dinner PYG 1,100,000 inclusive of IVA PYG 100,000.
**Expected output:** IVA PYG 100,000 BLOCKED. No input credit.

---

## Contribution Notes

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**

---

## Appendix A: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Licensed CPA must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed CPA. Document gap.
```

---

## Appendix B: Additional Rules [T1]

### Self-Supply (Autoconsumo) [T1]

- Withdrawal of goods for personal use: taxable event at applicable rate (10% or 5%) [T1]
- Report as output IVA [T1]

### Installment Sales [T1]

- IVA due at time of delivery, not at payment [T1]
- Full IVA reported in the delivery period [T1]

### ISC (Impuesto Selectivo al Consumo) Interaction [T1]

- ISC applies to specific goods (fuel, alcohol, tobacco, vehicles, soft drinks)
- ISC is separate from IVA
- IVA base INCLUDES ISC amount [T1]


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
