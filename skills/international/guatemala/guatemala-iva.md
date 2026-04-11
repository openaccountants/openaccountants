---
name: guatemala-iva
description: Use this skill whenever asked to prepare, review, or create a Guatemala IVA (Impuesto al Valor Agregado) return for any client. Trigger on phrases like "prepare IVA return", "do the IVA", "Guatemala VAT", or any request involving Guatemala value added tax filing. Also trigger when classifying transactions for IVA purposes. This skill contains the complete Guatemala IVA classification rules, return form mappings, deductibility rules, and filing deadlines. ALWAYS read this skill before touching any Guatemala IVA-related work.
---

# Guatemala IVA Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Guatemala |
| Jurisdiction Code | GT |
| Primary Legislation | Decreto 27-92, Ley del Impuesto al Valor Agregado (as amended) |
| Supporting Legislation | Acuerdo Gubernativo 5-2013 (Reglamento IVA); Decreto 10-2012 (Ley de Actualizacion Tributaria) |
| Tax Authority | Superintendencia de Administracion Tributaria (SAT) |
| Filing Portal | https://portal.sat.gob.gt (Agencia Virtual SAT) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, return form assignment, input tax recovery, derived calculations. Tier 2: partial exemption, small taxpayer regime, free-zone treatments. Tier 3: complex structures, rulings, transfer pricing. |

---

## Confidence Tier Definitions

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag and present options.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Do not guess.

---

## Step 0: Client Onboarding Questions

1. **Entity name and NIT (Numero de Identificacion Tributaria)** [T1]
2. **Tax regime** [T1] -- Regimen General (general regime with IVA) or Regimen de Pequeno Contribuyente (small taxpayer, 5% flat)
3. **Filing period** [T1] -- monthly (standard)
4. **Industry/sector** [T2] -- agriculture, manufacturing, services, free zone
5. **Does the business make exempt supplies?** [T2]
6. **Does the business import goods?** [T1]
7. **Is the business in a free trade zone (ZOLIC)?** [T2]
8. **Credit balance brought forward** [T1]

**If items 1-3 are unknown, STOP.**

---

## Step 1: IVA Rate Structure [T1]

**Legislation:** Decreto 27-92, Articles 3, 10.

### Standard Rate

| Rate | Application |
|------|-------------|
| 12% | Standard rate on all taxable sales of goods and services [T1] |

### Small Taxpayer Regime (Pequeno Contribuyente) [T1]

| Rate | Application |
|------|-------------|
| 5% | Flat tax on gross income for small taxpayers (replaces IVA and income tax) [T1] |

**Legislation:** Decreto 27-92, Article 45; Decreto 10-2012, Article 48.

Small taxpayers (annual income up to GTQ 150,000):
- Pay 5% on gross income as a simplified tax
- Do NOT charge IVA separately on invoices
- Do NOT claim input IVA credits
- Issue simplified invoices (facturas de pequeno contribuyente)

### Exempt Supplies [T1]

**Legislation:** Decreto 27-92, Article 7.

**Exempt goods:**
- Unprocessed agricultural products sold by producers (first sale)
- Medicines (generic, specified list)
- Agricultural inputs (fertilizers, insecticides, seeds, tools -- artisanal level)
- Books and educational materials
- Live animals (for production, not pets)

**Exempt services:**
- Educational services (approved institutions)
- Health/medical services (public and private clinics, hospitals)
- Financial services (interest, insurance premiums)
- Residential rental (up to certain threshold) [T2]
- Public transportation
- Electricity and water (domestic, first tier)

### Exports (0% -- Full Input Credit) [T1]
- Export of goods: zero-rated with full input credit recovery
- Export of services: services benefiting non-residents may qualify [T2]

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]
- Sale (IVA debito fiscal -- output) or Purchase (IVA credito fiscal -- input)
- Salaries, IGSS (social security), ISR (income tax), loan repayments = OUT OF SCOPE

### 2b. Determine Counterparty Location [T1]
- Domestic (Guatemala)
- Central American (CAFTA-DR: El Salvador, Honduras, Nicaragua, Costa Rica, Dominican Republic)
- International

### 2c. Determine IVA Rate [T1]
- 0% (export), 12% (standard), or exempt

### 2d. Determine Expense Category [T1]
- Capital goods (activos fijos)
- Inventory (inventario para reventa)
- Operating expenses (gastos)

---

## Step 3: IVA Return Form Structure (SAT-2237) [T1]

**Filed monthly via Agencia Virtual.**

### Debito Fiscal (Output Tax)

| Line | Description |
|------|-------------|
| 1 | Ventas y servicios gravados (Taxable sales and services) |
| 2 | IVA debito fiscal (Line 1 x 12%) |
| 3 | Exportaciones (Exports at 0%) |
| 4 | Ventas exentas (Exempt sales) |
| 5 | Total ventas (Line 1 + Line 3 + Line 4) |
| 6 | IVA en importaciones auto-declarado (Reverse charge on imports) |
| 7 | Total debito fiscal (Line 2 + Line 6) |

### Credito Fiscal (Input Tax)

| Line | Description |
|------|-------------|
| 8 | IVA en compras locales (IVA on local purchases) |
| 9 | IVA en importaciones (IVA paid at customs) |
| 10 | IVA en gastos y servicios (IVA on expenses) |
| 11 | Total credito fiscal (Line 8 + Line 9 + Line 10) |
| 12 | Ajustes (blocked/apportioned) |
| 13 | Credito fiscal neto (Line 11 - Line 12) |

### Liquidacion

| Line | Description |
|------|-------------|
| 14 | IVA a pagar (Line 7 - Line 13) |
| 15 | Credito fiscal del periodo anterior |
| 16 | Retenciones de IVA |
| 17 | Total a pagar / saldo a favor |

---

## Step 4: IVA Retention Regime [T1]

**Legislation:** Decreto 27-92, Article 48; Resoluciones SAT.

Guatemala operates an extensive IVA retention system:

### Designated Retention Agents (Agentes de Retencion)

| Agent Type | Retention Rate |
|------------|---------------|
| Designated by SAT (large taxpayers, exporters, etc.) | Varies: 12%, 15%, 25%, 50%, 65% of IVA invoiced [T2] |
| Exporters purchasing from small suppliers | 65% of IVA [T1] |
| Credit/debit card processors | 15% of IVA [T1] |
| Government entities | 25% of IVA [T1] |

### Treatment on the Return [T1]
- Supplier reports full output IVA
- IVA retained is reported on Line 16 as credit
- Retention certificates (constancias de retencion) must be obtained

### Special: IVA Retention on Non-Resident Services [T1]
- When paying non-residents for services, the payer retains and remits 12% IVA
- Also subject to ISR (income tax) withholding

---

## Step 5: Deductibility Check

### Blocked Input IVA (No Recovery) [T1]

**Legislation:** Decreto 27-92, Articles 16, 18.

- **Entertainment** -- meals, recreation (unless hospitality business) [T1]
- **Motor vehicles** -- passenger vehicles (exception: rental, taxi, transport businesses) [T1]
- **Personal use** [T1]
- **Exempt operations** -- costs attributable to exempt supplies [T1]
- **Purchases without valid factura (DTE)** -- MUST have valid Documento Tributario Electronico [T1]

### DTE (Electronic Tax Document) Requirement [T1]

**Legislation:** Decreto 27-92; SAT electronic invoicing regulations.

- Guatemala has implemented mandatory electronic invoicing (FEL -- Factura Electronica en Linea)
- ALL invoices must be issued through an authorized FEL certifier
- Input IVA is ONLY deductible with valid FEL-certified documents
- Paper invoices are no longer accepted for most taxpayers

### Partial Exemption [T2]
- Direct attribution first
- Common costs: `Recovery % = (Taxable Sales / Total Sales) * 100`
- Flag for reviewer

---

## Step 6: Key Thresholds [T1]

| Threshold | Value |
|-----------|-------|
| Mandatory IVA registration | All persons making taxable sales (no minimum threshold for general regime) |
| Small taxpayer threshold | Annual income up to GTQ 150,000 [T1] |
| FEL electronic invoicing | Mandatory for all taxpayers (phased implementation complete) |

---

## Step 7: Filing Deadlines and Penalties [T1]

**Legislation:** Codigo Tributario, Articles 89, 91, 94.

### Filing Deadlines

| Period | Deadline |
|--------|----------|
| Monthly IVA return | Last business day of the month following the period [T1] |
| Small taxpayer return | Last business day of the month following the period [T1] |

### Penalties

| Violation | Penalty |
|-----------|---------|
| Late filing | GTQ 100 per return (minimum) + interest [T1] |
| Late payment | Interest at rate determined by SAT (currently ~18% annual) [T1] |
| Failure to register | Fines + back-assessment [T1] |
| Failure to issue FEL | Closure of business (temporary) + fines [T1] |
| Fraud | Criminal penalties; fines + imprisonment up to 6 years [T1] |

---

## Step 8: Classification Matrix [T1]

### Domestic Purchases

| Category | IVA Rate | Input Credit | Notes |
|----------|---------|--------------|-------|
| Office supplies | 12% | Yes (with FEL) | |
| Commercial rent | 12% | Yes | |
| Residential rent | Exempt | No | |
| Electricity (commercial) | 12% | Yes | |
| Telephone/internet | 12% | Yes | |
| Motor car | 12% | BLOCKED | |
| Entertainment | 12% | BLOCKED | |
| Professional services | 12% | Yes | |
| Insurance (general) | 12% | Yes | |
| Insurance (life) | Exempt | No | |
| Basic food (first sale) | Exempt | No | |
| Medicines (generic) | Exempt | No | |

### Sales

| Category | IVA | Return Line |
|----------|-----|-------------|
| Domestic sale (standard) | 12% | Line 1, Line 2 |
| Export | 0% | Line 3 |
| Exempt supply | Exempt | Line 4 |

---

## Step 9: Free Trade Zone (ZOLIC) Rules [T2]

**Legislation:** Decreto 65-89 (Ley de Zonas Francas).

- Companies in free trade zones (ZOLIC) may be exempt from IVA on imports for export processing
- Sales to domestic market from ZOLIC: subject to IVA as imports
- Inter-zone transfers: may be exempt
- Flag for reviewer: ZOLIC benefits require valid authorization

---

## Step 9a: FEL Electronic Invoicing System [T1]

**Legislation:** SAT electronic invoicing regulations; Acuerdo de Directorio SAT.

Guatemala has fully implemented mandatory electronic invoicing (FEL -- Factura Electronica en Linea):

### Types of Electronic Documents (DTE)

| Document | Code | Use | Supports IVA Credit |
|----------|------|-----|-------------------|
| Factura | FACT | Standard sales document | YES (with NIT) |
| Factura Cambiaria | FCAM | Installment sales | YES |
| Factura de Pequeno Contribuyente | FPEQ | Small taxpayer sales | NO (no IVA) |
| Nota de Credito | NCRE | Returns, corrections | YES (reduces IVA) |
| Nota de Debito | NDEB | Additional charges | YES |
| Recibo | RECI | Donations, non-sales | NO |
| Factura de Exportacion | FEXP | Export sales | N/A |
| Factura Cambiaria de Exportacion | FCEX | Export installments | N/A |
| Nota de Abono | NABN | Advance payments | NO |
| Factura Especial | FESP | Purchases from unregistered suppliers | YES (buyer self-assesses) |

### FEL Requirements [T1]

1. All taxpayers must issue documents through a FEL certifier (certificador)
2. Documents are authorized in real-time by SAT
3. Each DTE receives a unique UUID authorization number
4. Input IVA ONLY valid with SAT-authorized FEL documents
5. Paper invoices are no longer accepted

### Factura Especial [T1]

**Legislation:** Decreto 27-92, Article 52.

When purchasing from an unregistered person/supplier:
- Buyer issues a Factura Especial
- Buyer self-assesses and withholds IVA (12%) and ISR (5%) from the payment
- IVA withheld is deductible as input IVA for the buyer
- ISR withheld must be remitted to SAT

---

## Step 9b: Sector-Specific Rules [T2]

### Agriculture

- First sale of unprocessed agricultural products by the producer: exempt [T2]
- Subsequent sales of processed agricultural products: taxable at 12% [T1]
- Agricultural inputs (artisanal level): exempt [T1]
- Industrial agricultural inputs: taxable at 12% [T1]
- Coffee export: zero-rated [T1]
- Sugar export: zero-rated [T1]
- Flag for reviewer: "first sale" and "artisanal" definitions require interpretation

### Manufacturing

- Manufacturing inputs: taxable at 12% (input credit available) [T1]
- Finished goods sold domestically: taxable at 12% [T1]
- Exports: zero-rated [T1]
- Equipment and machinery for production: taxable at 12% (input credit available) [T1]

### Construction and Real Estate

- Construction services: taxable at 12% [T1]
- Construction materials: taxable at 12% [T1]
- First sale of new real estate: taxable at 12% [T1]
- Subsequent sales: taxable at 12% on improvements/added value [T2]
- Land (bare, without construction): exempt [T2]
- Flag for reviewer: real estate IVA is complex in Guatemala

### Financial Services

- Interest on loans: exempt [T1]
- Banking commissions: taxable at 12% [T1]
- Insurance premiums: exempt [T1]
- Brokerage commissions: taxable at 12% [T1]

### Telecommunications

- All telecom services: taxable at 12% [T1]
- Internet services: taxable at 12% [T1]
- Prepaid cards: IVA included in face value [T1]

### Tourism

- Hotel accommodation: taxable at 12% [T1]
- Restaurant services: taxable at 12% [T1]
- Tour packages: taxable at 12% [T1]
- INGUAT-registered tourism businesses may have specific incentives [T2]

---

## Step 9c: Libro de Compras y Ventas [T1]

**Legislation:** Decreto 27-92, Article 37.

All IVA taxpayers must maintain:

- **Libro de Compras y Servicios Recibidos**: all purchases with FEL details, NIT of supplier, date, base, IVA, total
- **Libro de Ventas y Servicios Prestados**: all sales with FEL details, NIT of customer, date, base, IVA, total
- Books may be physical (authorized by SAT) or electronic
- Chronological order required
- Available for SAT inspection
- Retention: minimum 4 years from end of fiscal year
- Summary totals reconcile to IVA return

---

## Step 9d: IVA on Digital Services [T2]

Guatemala is moving toward taxing digital services provided by non-residents:
- Streaming services, digital advertising, cloud computing from foreign providers
- Current treatment: reverse charge by the buyer (self-assess 12% IVA)
- Registration of non-resident digital service providers: under discussion
- Flag for reviewer: digital taxation rules may evolve

---

## PROHIBITIONS [T1]

- NEVER let AI guess IVA classification -- it is deterministic from facts
- NEVER allow input credit on blocked categories
- NEVER allow input credit without valid FEL document
- NEVER apply reverse charge to out-of-scope categories
- NEVER confuse general regime (12% IVA) with small taxpayer regime (5% flat)
- NEVER allow small taxpayers to claim input IVA credits
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not Claude

---

## Step 10: Edge Case Registry

### EC1 -- Small taxpayer selling to general regime buyer [T1]
**Situation:** Small taxpayer (5% regime) sells goods to a general regime company.
**Resolution:** Small taxpayer issues factura de pequeno contribuyente. The buyer CANNOT claim input IVA credit because no IVA was charged. The 5% is a flat tax, not IVA.

### EC2 -- Import of services from US company [T1]
**Situation:** Guatemala company subscribes to US cloud software. No IVA on invoice.
**Resolution:** Self-assess IVA at 12%. Report as output (Line 6). Claim input (Line 10) if for taxable operations. Net = zero.

### EC3 -- Agricultural first sale exemption [T2]
**Situation:** Farmer sells coffee beans directly to processor.
**Resolution:** First sale of unprocessed agricultural products by the producer is exempt. However, subsequent sales (processor to roaster) are taxable at 12%. Flag for reviewer: confirm this is a qualifying first sale.

### EC4 -- Credit notes [T1]
**Situation:** Client issues credit note (nota de credito FEL).
**Resolution:** Reduce output IVA. Report net. Credit note must be issued through FEL system.

### EC5 -- IVA retention by large taxpayer [T1]
**Situation:** Large taxpayer client purchases goods and retains IVA from supplier.
**Resolution:** Client reports input IVA in full. Retained portion is remitted to SAT via retention return. Supplier claims retention credit on their return (Line 16).

### EC6 -- Real estate sale [T2]
**Situation:** Company sells a commercial building.
**Resolution:** First sale of newly constructed commercial real estate is subject to IVA at 12%. Subsequent sales of used properties may be exempt. Land is generally exempt. Flag for reviewer.

### EC7 -- Cross-border services within Central America [T2]
**Situation:** Guatemala company provides services to El Salvador company.
**Resolution:** May qualify as export of services (zero-rated) if consumed outside Guatemala. Flag for reviewer: confirm place of consumption.

### EC8 -- Vehicle purchase for transport business [T2]
**Situation:** Transport company purchases a bus.
**Resolution:** Vehicles for passenger or goods transport businesses may qualify for input IVA credit. Passenger vehicles for personal use are blocked. Flag for reviewer: confirm vehicle is exclusively for business transport.

---

## Step 11: Test Suite

### Test 1 -- Standard local purchase, 12%
**Input:** Guatemala supplier, office supplies, gross GTQ 11,200, IVA GTQ 1,200, net GTQ 10,000. Valid FEL.
**Expected output:** Line 8 = GTQ 1,200 input IVA. Full recovery.

### Test 2 -- Export, zero-rated
**Input:** Exporter ships coffee to US, net GTQ 200,000.
**Expected output:** Line 3 = GTQ 200,000. No output IVA. Input IVA fully recoverable.

### Test 3 -- Motor vehicle, blocked
**Input:** Purchase sedan GTQ 150,000, IVA GTQ 18,000.
**Expected output:** IVA GTQ 18,000 BLOCKED. No input credit.

### Test 4 -- Small taxpayer sale
**Input:** Small taxpayer sells goods GTQ 5,000. Pays 5% flat = GTQ 250.
**Expected output:** No IVA return filed. 5% flat tax return. Buyer gets no input IVA credit.

### Test 5 -- Imported services, reverse charge
**Input:** US consulting firm, USD 2,000 (~ GTQ 15,400). No IVA.
**Expected output:** Self-assess output IVA = GTQ 1,848 (12%). Input = GTQ 1,848. Net = zero.

### Test 6 -- Exempt supply (medical services)
**Input:** Medical clinic earns GTQ 50,000 from patient fees.
**Expected output:** Line 4 = GTQ 50,000. No output IVA. Input IVA on clinic expenses NOT recoverable.

### Test 7 -- Mixed operations apportionment
**Input:** 60% taxable, 40% exempt. Common IVA = GTQ 5,000.
**Expected output:** Flag T2. Input = GTQ 3,000 (60%). Blocked = GTQ 2,000 (40%).

### Test 8 -- Purchase without FEL
**Input:** Supplier provides handwritten receipt, no FEL. IVA GTQ 600.
**Expected output:** IVA GTQ 600 NOT deductible. No valid FEL = no credit.

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

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
