---
name: uruguay-iva
description: Use this skill whenever asked to prepare, review, or create a Uruguay IVA (Impuesto al Valor Agregado) return for any client. Trigger on phrases like "prepare IVA return", "do the IVA", "Uruguay VAT", or any request involving Uruguay value added tax filing. ALWAYS read this skill before touching any Uruguay IVA-related work.
---

# Uruguay IVA Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Uruguay |
| Jurisdiction Code | UY |
| Primary Legislation | Titulo 10, Texto Ordenado 1996 (IVA); Ley 18.083 (Reforma Tributaria 2007) |
| Supporting Legislation | Decreto 220/998 (Reglamento IVA); Resoluciones DGI |
| Tax Authority | Direccion General Impositiva (DGI) |
| Filing Portal | https://www.dgi.gub.uy (Servicios en Linea DGI) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, return form, input recovery, calculations. Tier 2: partial exemption, free zone, IRAE interaction. Tier 3: complex structures, rulings. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Step 0: Client Onboarding Questions

1. **Entity name and RUT (Registro Unico Tributario)** [T1] -- 12-digit RUT
2. **IVA taxpayer type** [T1] -- Contribuyente de IRAE (corporate), Unipersonal, Monotributo, Literal E
3. **Filing period** [T1] -- monthly (standard)
4. **Industry/sector** [T2]
5. **Does the business make exempt supplies?** [T2]
6. **Does the business import goods?** [T1]
7. **Is the business in a Free Trade Zone (Zona Franca)?** [T2]
8. **Credit balance brought forward** [T1]

**If items 1-3 are unknown, STOP.**

---

## Step 1: IVA Rate Structure [T1]

**Legislation:** Titulo 10, Texto Ordenado, Articles 18-20.

### Standard Rate

| Rate | Application |
|------|-------------|
| 22% | Standard rate (tasa basica) on all taxable supplies not otherwise specified [T1] |

### Reduced Rate (Tasa Minima)

| Rate | Application |
|------|-------------|
| 10% | Basic food items, medicines, hotel accommodation, first sale of certain goods [T1] |

### Items at Reduced Rate (10%) [T1]

**Legislation:** Titulo 10, Article 19.

- Basic food: bread, pasta, rice, flour, cooking oil, sugar, salt, fresh meats, fresh fish, eggs, milk, fresh fruits and vegetables, yerba mate, tea, coffee
- Medicines and pharmaceutical products
- Hotel and tourist accommodation
- First sale of real estate (residential)
- Newspapers and periodicals (not exempt)
- Cleaning products (basic household)
- Personal hygiene products (basic)

### Exempt Supplies (Exonerado) [T1]

**Legislation:** Titulo 10, Articles 19-20; Decreto 220/998.

**Exempt goods:**
- Agricultural products in their natural state (first sale by producer) [T2]
- Fuel (subject to IMESI -- specific internal tax)
- Precious metals (gold, silver -- certain transactions)

**Exempt services:**
- Financial services (interest on loans, life insurance premiums)
- Educational services (public and authorized private institutions)
- Health services (public health system, mutual health organizations -- mutualistas)
- Residential rental (apartments, houses)
- Public transportation (urban)
- Cultural activities (theater, cinema, concerts -- certain events)

### Exports (0% -- Full Input Credit) [T1]
- Export of goods: zero-rated with full input credit recovery
- Export of services: services consumed outside Uruguay [T2]

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]
- Sale (IVA devengado -- output) or Purchase (IVA deducible -- input)
- Salaries, BPS (social security), IRPF (personal income tax), IRAE (corporate), loans = OUT OF SCOPE

### 2b. Determine Counterparty Location [T1]
- Domestic (Uruguay)
- MERCOSUR: Argentina, Brazil, Paraguay (+ associate members)
- International

### 2c. Determine IVA Rate [T1]
- 0% (export), 10% (reduced), 22% (standard), or exempt

---

## Step 3: IVA Return Form Structure (Formulario 2176/2178) [T1]

**Filed monthly via DGI Servicios en Linea.**

### IVA Devengado (Output)

| Line | Description |
|------|-------------|
| 1 | Ventas gravadas a tasa basica (22%) |
| 2 | IVA devengado a tasa basica |
| 3 | Ventas gravadas a tasa minima (10%) |
| 4 | IVA devengado a tasa minima |
| 5 | Exportaciones (0%) |
| 6 | Ventas exoneradas |
| 7 | Total ventas |
| 8 | Total IVA devengado (Line 2 + Line 4) |

### IVA Deducible (Input)

| Line | Description |
|------|-------------|
| 9 | IVA en compras gravadas a tasa basica |
| 10 | IVA en compras gravadas a tasa minima |
| 11 | IVA en importaciones |
| 12 | Total IVA deducible |
| 13 | Ajustes (blocked/proportional) |
| 14 | IVA deducible neto |

### Liquidacion

| Line | Description |
|------|-------------|
| 15 | IVA a pagar (Line 8 - Line 14) |
| 16 | Credito del periodo anterior |
| 17 | Retenciones/percepciones |
| 18 | Total a pagar / saldo a favor |

---

## Step 4: IVA Withholding and Perception [T1]

**Legislation:** Titulo 10; DGI Resoluciones.

### IVA Withholding (Retencion) [T1]

| Agent Type | Rate |
|------------|------|
| Government entities (Estado) | 100% of IVA on services, 60% on goods [T1] |
| Designated large taxpayers | Varies by DGI resolution [T2] |

### IVA Perception (Percepcion) [T1]

| Agent Type | Rate |
|------------|------|
| Importers at customs (Aduana) | IVA paid on CIF + duties at applicable rate [T1] |
| Designated large taxpayers on sales | Varies [T2] |

---

## Step 5: Reverse Charge on Imported Services [T1]

**Legislation:** Titulo 10, Article 5.

When a Uruguay registered person receives services from a non-resident:

1. Self-assess IVA at applicable rate (22% standard, 10% if service qualifies) [T1]
2. Report as output IVA [T1]
3. Claim as input if for taxable operations [T1]
4. Net = zero for fully taxable businesses [T1]

---

## Step 6: Deductibility Check

### Blocked Input IVA (No Recovery) [T1]

**Legislation:** Titulo 10, Article 21.

- **Motor vehicles** -- passenger vehicles (exception: rental, taxi, driving school, transport) [T1]
- **Entertainment/recreation** -- meals, hospitality (unless hospitality trade) [T1]
- **Personal use** [T1]
- **Exempt operations** -- costs attributable to exempt supplies [T1]
- **Purchases without valid comprobante fiscal electronico (CFE)** [T1]

### CFE (Electronic Fiscal Document) [T1]

**Legislation:** DGI Resoluciones; Decreto 36/012.

Uruguay has mandatory electronic invoicing (CFE) for most taxpayers:
- e-Factura, e-Nota de Credito, e-Nota de Debito, e-Resguardo
- All documents must be authorized by DGI
- Input IVA only deductible with valid CFE

### Partial Exemption [T2]
- Direct attribution + proportional for common costs
- `Recovery % = (Taxable Sales / Total Sales) * 100`
- Flag for reviewer

---

## Step 7: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory IVA registration | All entities making taxable supplies must register (no minimum) |
| Monotributo | Small sole proprietors with limited activity (substitute for IVA + IRAE + social security) |
| Literal E (small enterprise) | Annual income up to certain threshold; simplified IVA treatment [T2] |

---

## Step 8: Filing Deadlines and Penalties [T1]

**Legislation:** Codigo Tributario; DGI Resoluciones.

### Filing Deadlines [T1]

Filing date depends on the last digit of the RUT:

| Last 2 Digits of RUT | Due Date Range (of following month) |
|----------------------|--------------------------------------|
| Group 1 | 16th-19th [T1] |
| Group 2 | 20th-23rd [T1] |
| Group 3 | 24th-27th [T1] |

Exact dates published annually by DGI.

### Penalties

| Violation | Penalty |
|-----------|---------|
| Late filing | UYU multa (fine) determined by DGI [T1] |
| Late payment | Recargos (surcharges): 5% first month + 2% per additional month [T1] |
| Interest on late payment | Rate set by Central Bank [T1] |
| Failure to register | Fines + back-assessment [T1] |
| Failure to issue CFE | Fines + potential closure [T1] |
| Fraud | Criminal penalties [T1] |

---

## Step 9: Classification Matrix [T1]

### Domestic Purchases

| Category | IVA Rate | Input Credit | Notes |
|----------|---------|--------------|-------|
| Office supplies | 22% | Yes | |
| Commercial rent | 22% | Yes | |
| Residential rent | Exempt | No | |
| Electricity (commercial) | 22% | Yes | |
| Telephone/internet | 22% | Yes | |
| Motor car | 22% | BLOCKED | |
| Entertainment | 22% | BLOCKED | |
| Professional services | 22% | Yes | |
| Hotel accommodation | 10% | Yes | Tasa minima |
| Basic food items | 10% | Yes (if for resale) | Tasa minima |
| Medicines | 10% | Yes (if for resale) | Tasa minima |
| Insurance (general) | 22% | Yes | |
| Insurance (life) | Exempt | No | |

### Sales

| Category | IVA | Return Line |
|----------|-----|-------------|
| Domestic sale (standard) | 22% | Line 1, Line 2 |
| Domestic sale (reduced) | 10% | Line 3, Line 4 |
| Export | 0% | Line 5 |
| Exempt | Exempt | Line 6 |

---

## Step 10: Free Trade Zone (Zona Franca) Rules [T2]

**Legislation:** Ley 15.921 (Ley de Zonas Francas).

- Free zone companies (usuarios de zona franca): exempt from ALL national taxes including IVA
- Sales from free zone to domestic market: treated as imports, subject to IVA at applicable rate
- Services from free zone to domestic clients: subject to IVA [T2]
- Purchases by free zone companies: IVA exempt (supplier zero-rates the sale)
- Flag for reviewer: free zone rules are complex; confirm specific user agreement

---

## Step 10a: CFE Electronic Invoicing System [T1]

**Legislation:** DGI Resoluciones; Decreto 36/012.

Uruguay has implemented mandatory electronic invoicing (CFE -- Comprobantes Fiscales Electronicos):

### Types of CFE

| Document | Code | Use | Supports IVA Credit |
|----------|------|-----|-------------------|
| e-Factura | 111 | B2B standard sales | YES [T1] |
| e-Ticket | 101 | B2C sales | NO (for buyer) [T1] |
| e-Nota de Credito | 112 | Returns, corrections | YES (reduces IVA) [T1] |
| e-Nota de Debito | 113 | Additional charges | YES [T1] |
| e-Resguardo | 181 | Withholding certificate | N/A [T1] |
| e-Factura Exportacion | 121 | Export sales | N/A [T1] |
| e-Remito | 131 | Goods transport | NO [T1] |

### CFE Requirements [T1]

1. Most taxpayers must issue CFEs (phased mandate by DGI)
2. CFEs are signed with digital certificate and authorized by DGI
3. Each CFE has a unique CAE (Codigo de Autorizacion de Emision)
4. Contingency procedures exist for system downtime
5. Input IVA only deductible with valid e-Factura (not e-Ticket)

---

## Step 10b: Sector-Specific Rules [T2]

### Agriculture and Livestock

- Agricultural products in natural state (first sale by producer): may be exempt [T2]
- Meat processing and exports: significant sector. Exports zero-rated. Input IVA fully recoverable.
- Agricultural inputs: IVA at applicable rate (some at tasa minima 10%)
- IMEBA (Impuesto a la Enajenacion de Bienes Agropecuarios): separate tax on agricultural sales, not IVA [T2]
- Flag for reviewer: agricultural taxation has multiple overlapping taxes

### Tourism and Hospitality

- Hotel accommodation: tasa minima 10% [T1]
- Restaurant services: tasa basica 22% [T1]
- Tourism packages for incoming tourists: may qualify for IVA reimbursement [T2]
- Tax-free shopping for tourists: IVAS refund scheme at departure [T2]
- Flag for reviewer: confirm tourism incentive applicability

### Financial Services

- Interest on loans between financial institutions: exempt [T1]
- Banking commissions and fees: taxable at 22% [T1]
- Insurance premiums (life): exempt [T1]
- Insurance premiums (property/general): taxable at 22% [T1]
- Credit card processing fees: taxable at 22% [T1]

### Real Estate

- First sale of new residential real estate: tasa minima 10% [T1]
- Sale of used real estate: exempt [T2]
- Construction services: tasa basica 22% [T1]
- Commercial rental: tasa basica 22% [T1]
- Residential rental: exempt [T1]

### Software and Technology

- Software licenses: taxable at 22% [T1]
- IT consulting services: taxable at 22% [T1]
- Software development for export: zero-rated [T2]
- Flag for reviewer: software export classification requires review

---

## Step 10c: IRAE-IVA Interaction [T2]

**Legislation:** Titulo 4, Texto Ordenado (IRAE).

- IVA is independent of IRAE (corporate income tax)
- However, IVA treatment follows IRAE source rules for certain cross-border transactions
- Services exported to non-residents: zero-rated for IVA if IRAE treats them as foreign-source
- Flag for reviewer: confirm IRAE source determination before applying IVA zero-rating on service exports

---

## Step 10d: Monotributo and Literal E [T2]

### Monotributo [T1]
- Very small sole proprietors with limited activities
- Pay a single monthly amount that substitutes IVA, IRAE, and social security
- Do NOT charge IVA separately
- Buyers CANNOT claim input IVA credit on purchases from Monotributo taxpayers

### Literal E (Small Enterprise) [T2]
- Small enterprises below certain income threshold
- Simplified IVA calculation based on sales volume
- May not be required to issue CFE (simplified receipts)
- Flag for reviewer: confirm current Literal E thresholds and obligations

---

## Step 10e: Libro de Compras y Ventas [T1]

All IVA taxpayers must maintain:

- **Libro de Ventas**: all sales with CFE details, RUT of customer (B2B), date, base (by rate), IVA, total
- **Libro de Compras**: all purchases with CFE details, RUT of supplier, date, base (by rate), IVA, total
- Electronic format via DGI system
- Summary totals reconcile to IVA return
- Retention: minimum 5 years

---

## PROHIBITIONS [T1]

- NEVER let AI guess IVA classification
- NEVER allow input credit on blocked categories
- NEVER allow input credit without valid CFE
- NEVER confuse tasa basica (22%) with tasa minima (10%)
- NEVER apply reverse charge to out-of-scope categories
- NEVER confuse zero-rated exports with exempt supplies
- NEVER compute any number -- all arithmetic is handled by the deterministic engine

---

## Step 11: Edge Case Registry

### EC1 -- Hotel accommodation at reduced rate [T1]
**Situation:** Business travel, hotel in Montevideo charges 10% IVA.
**Resolution:** Hotel accommodation is at tasa minima (10%). Input IVA recoverable if for business purposes. Report on Line 10.

### EC2 -- Imported software [T1]
**Situation:** Uruguay company subscribes to US cloud service. No IVA.
**Resolution:** Self-assess IVA at 22%. Output and input. Net = zero.

### EC3 -- Sale of basic food at 10% [T1]
**Situation:** Supermarket sells rice, flour, and meat.
**Resolution:** Basic food items are at tasa minima (10%). Report on Line 3 (sales) and Line 4 (IVA at 10%).

### EC4 -- Credit notes [T1]
**Situation:** Client issues e-Nota de Credito.
**Resolution:** Reduce output IVA. Must be valid CFE. Report net.

### EC5 -- Free zone company selling to domestic market [T2]
**Situation:** Zona Franca company sells manufactured goods to Montevideo retailer.
**Resolution:** Treated as import. IVA at applicable rate paid by buyer at customs/upon entry. Flag for reviewer.

### EC6 -- MERCOSUR trade [T1]
**Situation:** Uruguay company imports goods from Argentina.
**Resolution:** IVA paid at customs on CIF + duties. Input credit available. No special MERCOSUR IVA rules -- each country applies its own IVA independently.

### EC7 -- Yerba mate sale (reduced rate) [T1]
**Situation:** Wholesale company sells yerba mate.
**Resolution:** Yerba mate is a tasa minima (10%) product. Report at 10%.

### EC8 -- Mixed-rate business [T2]
**Situation:** Grocery store sells both basic food (10%) and general merchandise (22%).
**Resolution:** Separate reporting by rate. Output IVA split between Line 2 (22%) and Line 4 (10%). Input IVA fully recoverable (both rates support input credit).

---

## Step 12: Test Suite

### Test 1 -- Standard local purchase, 22%
**Input:** UY supplier, office equipment, gross UYU 12,200, IVA UYU 2,200, net UYU 10,000. Valid CFE.
**Expected output:** Line 9 = UYU 2,200 input IVA. Full recovery.

### Test 2 -- Export, zero-rated
**Input:** Exporter ships meat to Brazil, net UYU 500,000.
**Expected output:** Line 5 = UYU 500,000. No output IVA. Input IVA fully recoverable.

### Test 3 -- Motor vehicle, blocked
**Input:** Purchase sedan UYU 800,000, IVA UYU 176,000.
**Expected output:** IVA UYU 176,000 BLOCKED. No input credit.

### Test 4 -- Hotel accommodation at 10%
**Input:** Business hotel UYU 11,000 (UYU 10,000 + UYU 1,000 IVA at 10%).
**Expected output:** Line 10 = UYU 1,000 input IVA at tasa minima. Full recovery.

### Test 5 -- Sale of basic food at 10%
**Input:** Supermarket sells rice for UYU 55,000 (UYU 50,000 + UYU 5,000 IVA at 10%).
**Expected output:** Line 3 = UYU 50,000. Line 4 = UYU 5,000.

### Test 6 -- Imported services, reverse charge
**Input:** US consulting firm, USD 3,000 (~ UYU 120,000). No IVA.
**Expected output:** Self-assess output IVA = UYU 26,400 (22%). Input = UYU 26,400. Net = zero.

### Test 7 -- Exempt supply (residential rental)
**Input:** Landlord earns UYU 30,000/month from residential rental.
**Expected output:** Line 6 = UYU 30,000. No output IVA. Input IVA on property expenses NOT recoverable.

### Test 8 -- Entertainment, blocked
**Input:** Client dinner UYU 6,100 inclusive of IVA UYU 1,100.
**Expected output:** IVA UYU 1,100 BLOCKED. No input credit.

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
Action Required: Licensed Contador Publico must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed Contador Publico. Document gap.
```


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
