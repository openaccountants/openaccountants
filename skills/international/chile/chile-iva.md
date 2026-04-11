---
name: chile-iva
description: Use this skill whenever asked to prepare, review, or create a Chile IVA (Impuesto al Valor Agregado) return for any client. Trigger on phrases like "prepare IVA return", "declaracion de IVA", "Chile VAT", "Form 29", "F29", "SII filing", "factura electronica", "boleta", or any request involving Chilean IVA filing. Also trigger when classifying transactions for IVA purposes from bank statements, invoices, or other source data. This skill contains the complete Chile IVA classification rules, Form 29 mappings, deductibility rules, export treatment, electronic invoicing requirements, special regimes (Art. 29 DL 825), and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any IVA-related work for Chile.
---

# Chile IVA Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Chile |
| Jurisdiction Code | CL |
| Primary Legislation | Decreto Ley 825 (DL 825) -- Ley sobre Impuesto a las Ventas y Servicios |
| Supporting Legislation | Decreto Supremo 55 (Reglamento del DL 825); Ley 21.210 (Modernizacion Tributaria 2020); Ley 21.420 (2022) |
| Tax Authority | SII -- Servicio de Impuestos Internos |
| Filing Portal | https://www.sii.cl (SII Online / Mi SII) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, Form 29 mapping, filing periods, electronic invoicing triggers. Tier 2: partial credit (credito fiscal proporcional), special regimes, sector-specific rules. Tier 3: complex international structures, transfer pricing, mining/forestry special regimes. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed Contador Auditor must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed Contador Auditor and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and RUT (Rol Unico Tributario)** [T1] -- format XX.XXX.XXX-X (with verification digit)
2. **Taxpayer type** [T1] -- Primera Categoria (business/commercial), Segunda Categoria (professional/independent), or Sociedad
3. **IVA registration status** [T1] -- registered (Inicio de Actividades completed) or not registered
4. **Activity code (codigo de actividad economica)** [T1] -- SII-assigned activity code(s) from Inicio de Actividades
5. **Filing frequency** [T1] -- Monthly (standard for all IVA taxpayers)
6. **Does the business make exempt supplies?** [T2] -- If yes, proportional IVA credit required; reviewer must confirm
7. **Does the client export goods or services?** [T1] -- Exporters have right to IVA refund (Art. 36 DL 825)
8. **Is the client registered for electronic invoicing?** [T1] -- Mandatory for all IVA taxpayers since 2018 (Ley 20.727)
9. **Does the client qualify for simplified regime?** [T2] -- Small taxpayers may qualify for Regimen Pro-Pyme (Ley 21.210)

**If any of items 1-4 are unknown, STOP. Do not classify any transactions until registration status and activity are confirmed.**

---

## Step 1: IVA Rate Classification Rules

### 1a. Standard Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 19% | General rate on all taxable sales of goods and services | DL 825, Art. 14 |

**Legislation:** DL 825, Article 14. The IVA rate is 19% applied on the tax base.

### 1b. Additional Taxes on Specific Products [T1]

| Tax | Rate | Application | Legislation |
|-----|------|-------------|-------------|
| Impuesto Adicional Bebidas Alcoholicas | 31.5% | Liquors, spirits, wine > 40 degrees | DL 825, Art. 42(a) |
| Impuesto Adicional Bebidas Alcoholicas | 20.5% | Wine, champagne, beer | DL 825, Art. 42(b) |
| Impuesto Adicional Bebidas No Alcoholicas (high sugar) | 18% | Non-alcoholic beverages with high sugar content | DL 825, Art. 42(c) |
| Impuesto Adicional Bebidas No Alcoholicas (low sugar) | 10% | Non-alcoholic beverages with low sugar content | DL 825, Art. 42(c) |
| Impuesto a Productos Suntuarios | 15% | Luxury goods (jewelry, furs, yachts, fireworks, etc.) | DL 825, Art. 37 |
| Impuesto Adicional Vehiculos | Additional rates | Diesel vehicles | DL 825, Art. 43 bis |

**These additional taxes are reported on Form 29 in addition to IVA, not instead of IVA.**

### 1c. Zero-Rated (Exento con credito fiscal) [T1]

| Category | Legislation |
|----------|-------------|
| Exports of goods | DL 825, Art. 12(D) |
| Services exported and used exclusively abroad | DL 825, Art. 12(E); DS 55, Art. 36 |
| International transport services | DL 825, Art. 13(3) |

**Key distinction:** Exporters CAN recover input IVA (credito fiscal) on purchases related to export activity via refund mechanism under Art. 36.

### 1d. Exempt Supplies (Exento sin credito fiscal) [T1]

| Category | Legislation |
|----------|-------------|
| Residential property rental (unfurnished) | DL 825, Art. 12(E)(11) -- but furnished/commercial rent IS taxable |
| Education services (schools, universities) | DL 825, Art. 13(4) |
| Health services (hospitals, clinics -- public) | DL 825, Art. 13(7) |
| Public urban transport (buses, metro) | DL 825, Art. 13(3) |
| Financial interest on loans and credits | DL 825, Art. 12(E)(10) |
| Insurance premiums (certain types) | DL 825, Art. 12(E)(4) |
| Entry to shows, sporting events (certain) | DL 825, Art. 12(E)(1) |
| Sales of newsprint and periodicals (cultural) | DL 825, Art. 12(E)(14) |
| Raw materials sold by small miners | DL 825, Art. 12(E)(16) |

**Key distinction:** Exempt suppliers CANNOT recover input IVA (credito fiscal). IVA paid on purchases becomes part of the cost.

### 1e. Not Subject to IVA (No Afecto) [T1]

| Category | Notes |
|----------|-------|
| Salaries and wages | Employment income -- not a taxable supply |
| Dividends | Capital distribution -- not a sale |
| Loan repayments (principal) | Financial transaction -- not a sale |
| Sale of shares and financial instruments | Generally not subject to IVA (but transfer of business assets may be) |
| Donations (certain) | Subject to conditions |

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]

- Sale (IVA debito fiscal / output IVA) or Purchase (IVA credito fiscal / input IVA)
- Salaries, pension contributions, tax payments, loan repayments, dividends = OUT OF SCOPE (never on IVA return)
- **Legislation:** DL 825, Art. 2 (definitions); Art. 8 (taxable events: sales of goods, services)

### 2b. Determine Counterparty Location [T1]

- Chile (domestic): supplier/customer country is CL
- International: all other countries
- Special: Free Trade Agreements (TLC) may affect customs duties but NOT IVA rate

### 2c. Determine IVA Rate from Invoice [T1]

- Standard: 19%
- Additional taxes: added on top of 19% for specific products
- Exempt: 0% with no credit
- Export: 0% with credit

### 2d. Determine Document Type [T1]

| Document | Code (SII) | Usage | IVA Credit |
|----------|------------|-------|------------|
| Factura Electronica | 33 | B2B sales | Yes -- buyer can claim credito fiscal |
| Factura Exenta Electronica | 34 | Exempt sales | No IVA |
| Boleta Electronica | 39 | B2C sales (consumers) | No -- buyer cannot claim credito fiscal |
| Nota de Credito Electronica | 61 | Credit note (reversal/adjustment) | Adjusts credito fiscal |
| Nota de Debito Electronica | 56 | Debit note (additional charges) | Adjusts credito fiscal |
| Factura de Compra Electronica | 46 | Buyer-issued invoice (cambio de sujeto) | Special treatment |
| Guia de Despacho Electronica | 52 | Delivery document | No direct IVA impact |
| Liquidacion Factura Electronica | 43 | Commission agent liquidation | Special treatment |

---

## Step 3: Form 29 Mapping (Formulario 29) [T1]

**Legislation:** DL 825; SII Circular Letters; Form 29 instructions.

### IVA Debito Fiscal (Output IVA)

| Line | Description | Notes |
|------|-------------|-------|
| Line 20 | Taxable sales with Factura (net amount) | Sales documented by Factura |
| Line 142 | IVA Debito Fiscal on Factura sales | 19% of Line 20 |
| Line 22 | Taxable sales with Boleta (net amount) | Sales documented by Boleta |
| Line 151 | IVA Debito Fiscal on Boleta sales | 19% of Line 22 |
| Line 24 | Exempt and non-taxable sales | Exports + exempt supplies |
| Line 111 | Sales with retention (cambio de sujeto) | Where buyer retains IVA |
| Line 39 | Total IVA Debito Fiscal | Sum of all output IVA lines |

### IVA Credito Fiscal (Input IVA)

| Line | Description | Notes |
|------|-------------|-------|
| Line 25 | Purchases with Factura (net amount) | Documented by valid Factura |
| Line 520 | IVA Credito Fiscal on purchases | 19% of Line 25 |
| Line 28 | Imports (CIF + duties) | Goods imported |
| Line 532 | IVA Credito Fiscal on imports | 19% of Line 28 |
| Line 31 | Fixed asset purchases (activo fijo) | Capital goods with Factura |
| Line 535 | IVA Credito Fiscal on fixed assets | 19% of Line 31 |
| Line 521 | Credito Fiscal from internal use of inventory | Taxable deemed supply |
| Line 536 | Credito Fiscal from Notas de Credito received | Reduces credito fiscal |
| Line 537 | Total IVA Credito Fiscal | Sum of all input IVA lines |

### Balance and Payment

| Line | Description |
|------|-------------|
| Line 89 | IVA Determinado (Debito Fiscal minus Credito Fiscal) |
| Line 77 | Remanente credito fiscal from prior period (carried forward) |
| Line 91 | IVA to pay (if debito > credito) |
| Line 77 (next period) | Remanente credito fiscal carried to next period (if credito > debito) |

---

## Step 4: Credito Fiscal (Input IVA) Rules [T1]

**Legislation:** DL 825, Art. 23.

### Requirements for Valid Credito Fiscal [T1]

| Requirement | Detail | Legislation |
|-------------|--------|-------------|
| Valid tax document | Must be Factura Electronica (code 33) or equivalent | DL 825, Art. 23(1) |
| Related to taxable activity | Expense must have direct nexus to IVA-generating activity | DL 825, Art. 23(1) |
| Timely registration | Must be recorded in Libro de Compras within 2 months of issuance | DL 825, Art. 24(1) |
| Not a boleta | Boletas do NOT give right to credito fiscal | DL 825, Art. 23 |
| Correct RUT | Supplier RUT on invoice must be valid and active | SII verification |

### Items Where Credito Fiscal is NOT Allowed [T1]

| Category | Legislation | Notes |
|----------|-------------|-------|
| Purchases supported only by Boleta | DL 825, Art. 23 | Boletas are for B2C; no credito fiscal |
| Purchases not related to taxable activity | DL 825, Art. 23(2) | Personal use, non-business |
| Automobiles (station wagons, sedans) and related expenses | DL 825, Art. 23(4) | Exception: vehicles essential to business (taxis, freight, car rental) |
| Entertainment and hospitality | DL 825, Art. 23(4) | Representation expenses -- blocked |
| Goods used for exempt supplies exclusively | DL 825, Art. 23(2) | No credit on exempt-only inputs |
| Invoices older than 2 months not recorded | DL 825, Art. 24(1) | Time-barred |

### Automobile Exception [T2]

**Legislation:** DL 825, Art. 23(4).

Vehicles that are NOT blocked (credito fiscal IS allowed):
- Trucks and freight vehicles (camiones)
- Taxis and ride-hire vehicles
- Vehicles used in car rental business
- Ambulances, hearses
- Vehicles essential to business operations (e.g., delivery vans)

**Flag for reviewer:** If client claims credito fiscal on a vehicle, confirm the vehicle type and business necessity before allowing.

---

## Step 5: Proportional Credito Fiscal [T2]

**Legislation:** DL 825, Art. 23(3); DS 55, Art. 43.

### When It Applies [T2]
When a taxpayer makes both taxable (afectas) and exempt (exentas) sales, the credito fiscal on common expenses must be apportioned.

### Calculation Method [T2]

```
Proportion % = (Taxable Sales in last 12 months / Total Sales in last 12 months) * 100
Deductible Credito Fiscal = Common Input IVA * Proportion %
```

| Expense Type | Treatment |
|-------------|-----------|
| Exclusively attributable to taxable sales | 100% credito fiscal |
| Exclusively attributable to exempt sales | 0% credito fiscal |
| Common/shared expenses | Proportional credito fiscal |

**Flag for reviewer: proportional calculation must be confirmed by Contador Auditor before applying. The 12-month rolling basis must be verified.**

---

## Step 6: Electronic Invoicing (Facturacion Electronica) [T1]

**Legislation:** Ley 20.727 (2014); Resolucion SII Exenta 11 de 2003; DL 825, Art. 54.

### Mandatory Requirements [T1]

| Requirement | Detail |
|-------------|--------|
| Who must issue | ALL IVA taxpayers (mandatory since 2018 under Ley 20.727) |
| Format | XML format per SII technical specifications |
| Validation | SII assigns folio ranges; taxpayer generates documents within authorized range |
| Timbre Electronico | Digital stamp (timbre) on each document for authenticity |
| Delivery | Must be sent to buyer electronically; buyer has 8 days to accept or reject (acuse de recibo) |
| Storage | Minimum 6 years (Codigo Tributario, Art. 200) |
| Contingency | SII may authorize contingency manual invoicing; must be reported within days |

### Acuse de Recibo (Receipt Acknowledgment) [T1]

**Legislation:** DL 825, Art. 23, numeral 7; Ley 19.983.

| Requirement | Detail |
|-------------|--------|
| Buyer acknowledgment | Buyer must electronically acknowledge receipt of goods/services within 8 days |
| Effect on credito fiscal | Credito fiscal is only valid once the buyer has acknowledged receipt |
| Merchandise receipt (Recepcion de Mercaderias) | Separate from document acceptance; confirms physical receipt |

---

## Step 7: IVA on Imports [T1]

**Legislation:** DL 825, Art. 8(c); Art. 11; Art. 12(D).

### Import of Goods [T1]

| Element | Detail |
|---------|--------|
| Taxable event | Import of goods into Chilean territory |
| Tax base | CIF value + customs duties (arancel aduanero) + other import charges |
| Rate | 19% |
| Collection | IVA collected by Servicio Nacional de Aduanas at import |
| Document | Declaracion de Importacion (DIN) |
| Deductibility | IVA on imports is deductible as credito fiscal (Line 532 of Form 29) |

### IMPORTANT: Ley de Cumplimiento Tributario Changes (October 2025) [T1]

**Legislation:** Ley de Cumplimiento Tributario (Ley 21.713).

As of October 25, 2025, the VAT exemption for low-value imports (previously under USD 41) has been **eliminated**. All physical goods imported into Chile are now subject to 19% IVA regardless of value. For purchases up to USD 500, foreign digital platforms (e.g., AliExpress, Shein, Amazon) are responsible for collecting and remitting the IVA at the point of sale. New marketplace reporting requirements became effective October 1, 2025, with periodic verification mandatory from January 1, 2026.

### Import of Services [T1]

**Legislation:** DL 825, Art. 8(h) (added by Ley 21.420 of 2022).

| Element | Detail |
|---------|--------|
| Taxable event | Services provided from abroad and used in Chile |
| Tax base | Total amount paid for the service |
| Rate | 19% |
| Mechanism | Service recipient self-assesses IVA (reverse charge) |
| Filing | Buyer declares and pays IVA on Form 29 |
| Deductibility | Self-assessed IVA is simultaneously deductible as credito fiscal (net zero for fully taxable businesses) |
| Digital services | Foreign providers of digital services to Chilean consumers must register with SII and charge IVA (Ley 21.210, 2020) |

---

## Step 8: Export IVA Recovery (Art. 36 DL 825) [T1]

**Legislation:** DL 825, Art. 36; DS 348.

### Mechanism [T1]

| Element | Detail |
|---------|--------|
| Who qualifies | Exporters of goods and services |
| What is recoverable | Credito fiscal (input IVA) related to export activity |
| How | Refund request to SII; or imputation against other tax obligations |
| Period | Within the month following the export period |
| Document | Declaracion Jurada and supporting documentation |

### Eligible Exports [T1]

| Type | Treatment |
|------|-----------|
| Physical goods exported | Zero-rated; credito fiscal recoverable |
| Services exported (used abroad) | Zero-rated; credito fiscal recoverable (Art. 12(E)(16)) |
| International transport | Zero-rated; credito fiscal recoverable |

### Recovery Process [T2]

| Step | Detail |
|------|--------|
| 1 | Accumulate credito fiscal as remanente (carried forward) |
| 2 | File Form 29 showing remanente |
| 3 | Submit refund request (solicitud de devolucion) to SII or Tesoreria General |
| 4 | SII reviews and may audit before approving |
| 5 | Refund issued within 30 days (standard) or faster for certified exporters |

**Flag for reviewer:** Export IVA recovery claims are subject to SII audit. Ensure all supporting documentation (customs declarations, bills of lading, service contracts) is complete.

---

## Step 9: Cambio de Sujeto (Change of Taxpayer) [T2]

**Legislation:** DL 825, Art. 3; SII Resolutions.

### Concept [T2]
In certain sectors, SII designates the BUYER as the person responsible for withholding and remitting IVA, instead of the seller. This is called "cambio de sujeto."

### Common Sectors [T2]

| Sector | Resolution | Detail |
|--------|------------|--------|
| Agricultural products (trigo, arroz, legumbres) | SII Res. Ex. 3722/2000 | Buyer withholds IVA |
| Scrap metal (chatarra) | SII Res. Ex. 142/2005 | Buyer withholds IVA |
| Berries and fruits | SII Res. Ex. 1496/1976 | Buyer withholds IVA |
| Timber/lumber | SII Res. Ex. Various | Buyer withholds IVA |
| Cattle/livestock | SII Res. Ex. Various | Buyer withholds IVA |

### Mechanics [T2]

| Step | Detail |
|------|--------|
| 1 | Buyer issues Factura de Compra (code 46) instead of seller issuing Factura |
| 2 | Buyer withholds the IVA amount |
| 3 | Buyer reports withheld IVA as debito fiscal on their Form 29 |
| 4 | Buyer simultaneously claims credito fiscal (if related to taxable activity) |
| 5 | Seller does not report this IVA on their own return |

**Flag for reviewer:** Cambio de sujeto rules are sector-specific. Confirm the applicable SII resolution and withholding percentage with Contador Auditor.

---

## Step 10: Filing Deadlines [T1]

**Legislation:** DL 825, Art. 64; Codigo Tributario, Art. 36.

### Standard Filing [T1]

| Period | Filing Deadline | Notes |
|--------|----------------|-------|
| Monthly (all IVA taxpayers) | 12th of the following month | Standard deadline |
| Monthly (electronic filers) | 20th of the following month | Extended deadline for electronic filing via SII portal |
| Monthly (with no sales -- sin movimiento) | Still must file | File a zero return (declaracion sin movimiento) |

### Payment Methods [T1]

| Method | Detail |
|--------|--------|
| Online (SII portal) | Formulario 29 filed and paid electronically |
| Bank payment (convenio bancario) | Payment at authorized banks with Form 29 |
| Tesoreria General | Government treasury payment |

### Late Filing Penalties [T1]

| Penalty | Calculation | Legislation |
|---------|-------------|-------------|
| Late filing surcharge | 10% of tax, plus 2% per month (up to 30% total) | Codigo Tributario, Art. 97(2) |
| Late payment interest | 1.5% per month or fraction | Codigo Tributario, Art. 53 |
| Failure to file | Up to 300% of tax evaded (criminal for fraud) | Codigo Tributario, Art. 97(4) |

---

## Step 11: Small Business Regimes [T2]

### Regimen Pro-Pyme (Ley 21.210) [T2]

**Legislation:** Ley de Impuesto a la Renta, Art. 14(D); Ley 21.210 (Modernizacion Tributaria).

| Feature | Detail |
|---------|--------|
| Who qualifies | Micro, small, and medium enterprises (average income < 75,000 UF over last 3 years) |
| IVA impact | Pro-Pyme affects income tax, NOT IVA. IVA obligations remain standard |
| Credito fiscal | Standard rules apply |
| Simplified accounting | Simplified cash-basis accounting permitted (but IVA still accrual-based) |

### Art. 29 DL 825 -- Small Taxpayer Regime [T2]

**Legislation:** DL 825, Art. 29; DS 55, Art. 32.

| Feature | Detail |
|---------|--------|
| Who qualifies | Small businesses meeting SII criteria (low turnover, simplified activities) |
| Simplified IVA | May use simplified calculation methodology |
| Filing | Still monthly on Form 29 |
| Credito fiscal | May be limited or calculated differently |

**Flag for reviewer:** Qualification for simplified regimes must be verified by Contador Auditor. Criteria change and are subject to SII interpretation.

---

## Step 12: Key Thresholds [T1]

| Threshold | Value | Notes |
|-----------|-------|-------|
| UF (Unidad de Fomento) | Daily indexed value (~CLP 38,800 as of 2025) | Used for various thresholds |
| UTM (Unidad Tributaria Mensual) | Monthly indexed value (~CLP 66,000 as of 2025) | Used for penalty calculations |
| Pro-Pyme income threshold | 75,000 UF average (3 years) | For simplified income tax regime |
| Credito fiscal time limit | 2 months from invoice date | DL 825, Art. 24(1) |
| Boleta minimum amount | No minimum | All B2C sales need Boleta |
| Statute of limitations | 3 years (standard); 6 years (fraud) | Codigo Tributario, Art. 200 |

---

## Step 13: Remanente de Credito Fiscal (Carried Forward IVA Credit) [T1]

**Legislation:** DL 825, Art. 26.

### Rules [T1]

| Rule | Detail |
|------|--------|
| Carryforward | If credito fiscal exceeds debito fiscal, the excess (remanente) carries forward to the next period |
| Indexation | Remanente is adjusted for inflation (UTM variation) before applying to next period |
| Expiry | Remanente does NOT expire -- carries forward indefinitely |
| Refund | Generally no refund (exception: exporters under Art. 36; fixed asset purchasers under Art. 27 bis) |

### Art. 27 bis -- Fixed Asset Refund [T2]

**Legislation:** DL 825, Art. 27 bis.

| Feature | Detail |
|---------|--------|
| Who qualifies | Taxpayers who acquire fixed assets generating persistent remanente for 6+ consecutive months |
| What is refundable | Credito fiscal attributable to fixed asset acquisitions |
| Process | Request to SII after 6 months of accumulated remanente |
| Condition | If fixed assets sold within specified period, refund must be returned |

**Flag for reviewer:** Art. 27 bis refund requires careful analysis of fixed asset purchases and holding period. Confirm with Contador Auditor.

---

## Step 14: Libro de Compras y Ventas (Purchase and Sales Ledgers) [T1]

**Legislation:** DL 825, Art. 59; DS 55, Art. 74-76.

### Requirements [T1]

| Ledger | Content | Notes |
|--------|---------|-------|
| Libro de Ventas | All sales documents issued (Facturas, Boletas, Notas de Credito/Debito) | Reported to SII electronically |
| Libro de Compras | All purchase documents received (Facturas, Declaraciones de Importacion) | Reported to SII electronically |
| Registro de Compras y Ventas (RCV) | Electronic register maintained by SII from electronic documents | Taxpayer must verify and confirm monthly |

### Propuesta de F29 (SII Pre-filled Return) [T1]

| Feature | Detail |
|---------|--------|
| What it is | SII pre-fills Form 29 based on electronic documents in RCV |
| Taxpayer obligation | Must review, adjust (if necessary), and confirm the proposal |
| Adjustments | Taxpayer may add non-electronic documents (e.g., imports, adjustments) |
| Deadline | Same as Form 29 filing deadline |

---

## Step 15: Reviewer Escalation Protocol

When a [T2] situation is identified, output the following structured flag before proceeding:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Licensed Contador Auditor must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed Contador Auditor. Document gap.
```

---

## Step 16: Edge Case Registry

These are known ambiguous situations and their confirmed resolutions.

### EC1 -- Vehicle purchase (sedan/station wagon) [T1]
**Situation:** Client purchases a sedan for business use. Invoice shows IVA CLP 3,800,000.
**Resolution:** Credito fiscal BLOCKED under DL 825, Art. 23(4). Sedans and station wagons are not eligible for credito fiscal regardless of business use. IVA becomes part of the asset cost.
**Legislation:** DL 825, Art. 23(4).

### EC2 -- Purchase documented with Boleta instead of Factura [T1]
**Situation:** Employee purchases office supplies and obtains only a Boleta (consumer receipt).
**Resolution:** No credito fiscal. Boletas do not give right to credito fiscal. The full amount (including IVA) is the expense. To claim credito fiscal, a Factura must be requested.
**Legislation:** DL 825, Art. 23(1).

### EC3 -- Software subscription from US provider (e.g., AWS, Slack) [T1]
**Situation:** Monthly charge from a US company for cloud services.
**Resolution:** Since 2020 (Ley 21.210), foreign digital service providers must register with SII and charge 19% IVA to Chilean consumers. If the provider charges IVA, it appears as IVA recargado on the invoice. For B2B, if provider does not charge IVA, buyer must self-assess (reverse charge) under Art. 8(h) (Ley 21.420). Report as debito fiscal and simultaneously claim as credito fiscal. Net zero for fully taxable businesses.
**Legislation:** DL 825, Art. 8(h); Ley 21.210; Ley 21.420.

### EC4 -- Credit note received from supplier [T1]
**Situation:** Supplier issues Nota de Credito Electronica (code 61) for returned goods.
**Resolution:** Reduce credito fiscal by the IVA amount on the credit note. Report on Line 536 of Form 29. The credit note must reference the original Factura number.
**Legislation:** DL 825, Art. 21; DS 55, Art. 37.

### EC5 -- Export of professional services [T1]
**Situation:** Chilean consulting firm provides services to a foreign client. Service is used exclusively abroad.
**Resolution:** Zero-rated under Art. 12(E)(16). No IVA charged. Report as exempt/export on Line 24 of Form 29. Credito fiscal on related costs IS recoverable via Art. 36 refund mechanism.
**Legislation:** DL 825, Art. 12(E)(16); Art. 36.

### EC6 -- Construction services (IVA on real estate) [T2]
**Situation:** Client sells a new residential property.
**Resolution:** Sale of new real estate by a habitual seller is subject to IVA (DL 825, Art. 8(f)). However, there is a credito especial (special credit) for construction companies (Art. 21 DL 910) that reduces the effective IVA burden on affordable housing. Flag for reviewer: confirm whether credito especial applies based on property value and construction company status.
**Legislation:** DL 825, Art. 8(f); DL 910, Art. 21.

### EC7 -- Deemed sale (retiro de bienes) [T1]
**Situation:** Client withdraws inventory for personal use or gifts to employees.
**Resolution:** Deemed taxable sale. Must issue internal Factura and charge IVA debito fiscal. Report on Form 29 as a sale.
**Legislation:** DL 825, Art. 8(d).

### EC8 -- Mixed business: taxable + exempt income [T2]
**Situation:** Client earns both taxable consulting income and exempt rental income.
**Resolution:** Credito fiscal on expenses exclusively for taxable activity: 100% deductible. Credito fiscal on expenses exclusively for exempt activity: 0%. Shared expenses: proportional under Art. 23(3). Flag for reviewer.
**Legislation:** DL 825, Art. 23(3).

### EC9 -- Invoice received more than 2 months ago [T1]
**Situation:** Client finds a Factura from 3 months ago not yet recorded.
**Resolution:** Credito fiscal is time-barred. DL 825, Art. 24(1) requires registration within 2 months of issuance. The IVA becomes part of the expense cost and cannot be claimed.
**Legislation:** DL 825, Art. 24(1).

### EC10 -- Payments to foreign freelancers (servicios prestados desde el exterior) [T2]
**Situation:** Chilean company hires a foreign freelancer for design work.
**Resolution:** Under Ley 21.420 (2022), services provided from abroad and used in Chile are subject to IVA. Buyer must self-assess IVA (reverse charge). If the freelancer is in a country with a tax treaty, withholding tax (impuesto adicional) considerations also apply. Flag for reviewer: confirm treaty applicability and withholding obligations.
**Legislation:** DL 825, Art. 8(h); Ley 21.420; DL 824, Art. 59.

---

## Step 17: Test Suite

These reference transactions have known correct outputs. Use to validate skill execution.

### Test 1 -- Standard local sale with Factura
**Input:** Chilean company sells consulting services, net CLP 10,000,000, IVA CLP 1,900,000. Factura Electronica issued.
**Expected output:** Form 29, Line 20 += CLP 10,000,000, Line 142 += CLP 1,900,000.

### Test 2 -- Purchase with valid Factura, operating expense
**Input:** Chilean company buys office supplies from local supplier, net CLP 500,000, IVA CLP 95,000. Valid Factura Electronica received and acknowledged.
**Expected output:** Form 29, Line 25 += CLP 500,000, Line 520 += CLP 95,000. Credito fiscal valid.

### Test 3 -- B2C sale with Boleta
**Input:** Retail client sells goods to consumer, total CLP 119,000 (net CLP 100,000, IVA CLP 19,000). Boleta Electronica issued.
**Expected output:** Form 29, Line 22 += CLP 100,000, Line 151 += CLP 19,000.

### Test 4 -- Export of goods
**Input:** Chilean manufacturer exports goods, FOB value USD 10,000. Customs export declaration filed.
**Expected output:** Form 29, Line 24 += CLP equivalent. No IVA charged. Credito fiscal on inputs recoverable under Art. 36.

### Test 5 -- Import of goods
**Input:** Company imports machinery, CIF value CLP 20,000,000, customs duty CLP 1,200,000. IVA on import = (20,000,000 + 1,200,000) * 19% = CLP 4,028,000.
**Expected output:** Form 29, Line 28 += CLP 21,200,000, Line 532 += CLP 4,028,000. Credito fiscal valid.

### Test 6 -- Vehicle purchase (sedan, blocked)
**Input:** Company purchases sedan, net CLP 15,000,000, IVA CLP 2,850,000.
**Expected output:** NO credito fiscal. IVA blocked under Art. 23(4). Vehicle cost = CLP 17,850,000. Form 29 -- no entry for credito fiscal on this purchase.

### Test 7 -- Purchase with Boleta only (no credito fiscal)
**Input:** Employee buys cleaning supplies CLP 23,800 (gross, including IVA). Only Boleta obtained.
**Expected output:** No credito fiscal. Full CLP 23,800 is operating expense. No Form 29 entry for input IVA.

### Test 8 -- Reverse charge on imported services
**Input:** Chilean company pays US$2,000 (CLP 1,800,000) for foreign cloud service. No IVA on invoice.
**Expected output:** Self-assess IVA: CLP 1,800,000 * 19% = CLP 342,000. Report as debito fiscal AND credito fiscal on Form 29. Net IVA effect = zero for fully taxable business.

---

## PROHIBITIONS [T1]

- NEVER allow credito fiscal on purchases documented only with Boleta
- NEVER allow credito fiscal on sedan/station wagon purchases (unless confirmed exception by reviewer)
- NEVER allow credito fiscal on invoices older than 2 months not yet registered
- NEVER omit IVA on deemed sales (retiros de bienes)
- NEVER confuse IVA (19%) with additional taxes on alcohol/beverages (which are ON TOP of IVA)
- NEVER file an IVA return without reviewing the SII pre-filled proposal (Propuesta de F29)
- NEVER ignore cambio de sujeto rules for applicable sectors
- NEVER allow credito fiscal without valid Factura Electronica and acuse de recibo
- NEVER confuse remanente de credito fiscal (carried forward) with a refund right (refund only for exporters and Art. 27 bis)
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 18: Additional Taxes Reported on Form 29 [T1]

**Legislation:** DL 825, Art. 37-43 bis.

### Impuesto Adicional (Additional Taxes on Specific Goods) [T1]

These additional taxes are reported and paid alongside IVA on the same Form 29:

| Tax | Rate | Base | Legislation |
|-----|------|------|-------------|
| Alcoholic beverages (spirits > 40 degrees) | 31.5% | Net sale price | DL 825, Art. 42(a) |
| Alcoholic beverages (wine, beer, champagne) | 20.5% | Net sale price | DL 825, Art. 42(b) |
| Non-alcoholic beverages (high sugar) | 18% | Net sale price | DL 825, Art. 42(c) |
| Non-alcoholic beverages (low sugar) | 10% | Net sale price | DL 825, Art. 42(c) |
| Luxury goods (jewelry, furs, yachts) | 15% | Net sale price | DL 825, Art. 37 |

### Relationship to IVA [T1]

| Rule | Detail |
|------|--------|
| Calculation base | Additional tax is calculated on the SAME base as IVA (net sale price) |
| Concurrence | IVA (19%) is charged IN ADDITION to the additional tax |
| Example: Wine sale | Base CLP 10,000 + IVA 19% (CLP 1,900) + Impuesto Adicional 20.5% (CLP 2,050) = CLP 13,950 |
| Credito fiscal | Additional tax paid on purchases generates its own credit, separate from IVA credito fiscal |

---

## Step 19: Reporting Obligations Summary [T1]

| Form | Description | Frequency | Deadline |
|------|-------------|-----------|----------|
| Form 29 (F29) | Declaracion Mensual y Pago Simultaneo | Monthly | 12th (paper) / 20th (electronic) |
| Form 50 (F50) | Declaracion Mensual de Impuestos (certain additional taxes) | Monthly | Same as F29 |
| DDJJ Renta (F22) | Annual income tax return | Annual | April |
| Registro de Compras y Ventas | Electronic purchase/sales ledger | Monthly | Verified via SII RCV |
| Facturacion Electronica | Electronic invoicing | Continuous | Each transaction |

### SII Online Obligations [T1]

| Obligation | Detail |
|------------|--------|
| RCV verification | Taxpayer must verify the Registro de Compras y Ventas monthly on SII portal |
| Propuesta F29 | SII pre-fills Form 29; taxpayer must review and confirm or adjust |
| Declaraciones Juradas | Various annual information returns (DJ) required depending on activity |
| Inicio de Actividades | Must be filed within 2 months of starting commercial activity |
| Termino de Giro | Must be filed when ceasing commercial activity; final IVA return required |

---

## Contribution Notes (For Adaptation to Other Jurisdictions)

If you are adapting this skill for another country, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all Form 29 line numbers with the equivalent lines on your jurisdiction's IVA/VAT return form.
3. Replace IVA rates with your jurisdiction's standard, reduced, and zero rates.
4. Replace the UF/UTM values and thresholds with your jurisdiction's equivalent indexed units.
5. Replace the document types (Factura, Boleta, etc.) with your jurisdiction's equivalent.
6. Replace the electronic invoicing requirements with your jurisdiction's e-invoicing rules.
7. Replace the cambio de sujeto rules with your jurisdiction's equivalent withholding/reverse charge rules.
8. Have a licensed accountant in your jurisdiction validate every T1 rule before publishing.
9. Add your own edge cases to the Edge Case Registry for known ambiguous situations in your jurisdiction.
10. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
