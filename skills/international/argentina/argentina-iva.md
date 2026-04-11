---
name: argentina-iva
description: Use this skill whenever asked to prepare, review, or create an Argentina IVA (Impuesto al Valor Agregado) return for any client. Trigger on phrases like "prepare IVA return", "declaracion jurada de IVA", "Argentina VAT", "AFIP filing", "ARCA filing", "monotributo", "factura electronica", or any request involving Argentine IVA filing. Also trigger when classifying transactions for IVA purposes from bank statements, invoices, or other source data. This skill contains the complete Argentina IVA classification rules, form mappings (F.2002), deductibility rules, three-rate structure (21%/10.5%/27%), Monotributo simplified regime, withholding/collection agent (retencion/percepcion) rules, export reimbursement, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any IVA-related work for Argentina.
---

# Argentina IVA Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Argentina |
| Jurisdiction Code | AR |
| Primary Legislation | Ley de IVA (Law 23.349, texto ordenado 1997) and its Decreto Reglamentario (Decree 692/98) |
| Supporting Legislation | Ley 27.430 (2017 Tax Reform); Ley 27.541 (Solidaridad Social); RG AFIP 4.164 (electronic invoicing); RG AFIP 2.854/3.685 (withholding/collection regimes) |
| Tax Authority | ARCA (Agencia de Recaudacion y Control Aduanero) -- formerly AFIP (Administracion Federal de Ingresos Publicos) |
| Filing Portal | https://auth.afip.gob.ar (AFIP/ARCA Online Services) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, form mapping, filing periods, electronic invoicing triggers, Monotributo thresholds. Tier 2: partial exemption, withholding/collection agent calculations, sector-specific regimes. Tier 3: complex international structures, transfer pricing, free trade zone (ZFI) rules. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed Contador Publico must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed Contador Publico and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and CUIT (Clave Unica de Identificacion Tributaria)** [T1] -- format XX-XXXXXXXX-X
2. **IVA registration category** [T1] -- Responsable Inscripto, Monotributista, Exento, or No Alcanzado
3. **Monotributo category (if applicable)** [T1] -- Categories A through K (different thresholds for goods vs services)
4. **Filing period** [T1] -- Monthly (all Responsables Inscriptos)
5. **Industry/sector** [T2] -- impacts rate (e.g., construction, agriculture, media)
6. **Does the business make exempt supplies?** [T2] -- If yes, proportional credit (prorrateo) required
7. **Is the client a withholding/collection agent (agente de retencion/percepcion)?** [T1] -- designated by AFIP/ARCA resolution or provincial tax authority
8. **Does the client export goods or services?** [T1] -- exporters can recover input IVA
9. **Does the client receive income subject to the 27% higher rate?** [T1] -- utilities (gas, electricity, water, telecoms) to Responsable Inscripto

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until registration category is confirmed.**

---

## Step 1: IVA Rate Classification Rules

### 1a. Standard Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 21% | General rate on all taxable goods and services not specifically assigned another rate | Ley IVA, Art. 28 |

### 1b. Reduced Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 10.5% | Capital goods (bienes de capital) -- machinery, equipment, certain fixed assets | Ley IVA, Art. 28, inciso (e) |
| 10.5% | Construction of residential housing | Ley IVA, Art. 28, inciso (b) |
| 10.5% | Certain agricultural inputs (fertilizers, seeds, cattle breeding) | Ley IVA, Art. 28, inciso (a) |
| 10.5% | Passenger land transport (long distance, > 100 km) | Ley IVA, Art. 28, inciso (g) |
| 10.5% | Medical and paramedical services (prepaid health plans) | Ley IVA, Art. 28, inciso (h) |
| 10.5% | Newspapers, magazines, periodicals | Ley IVA, Art. 28, inciso (c) |
| 10.5% | Interest on loans from financial institutions | Ley IVA, Art. 28, inciso (d) |
| 10.5% | Bread, flour, milk | Ley IVA, Art. 28, inciso (a) |

### 1c. Higher Rate [T1]

| Rate | Application | Legislation |
|------|-------------|-------------|
| 27% | Natural gas (supplied via networks) | Ley IVA, Art. 28, ultimo parrafo |
| 27% | Electricity | Ley IVA, Art. 28, ultimo parrafo |
| 27% | Water supply (via networks) | Ley IVA, Art. 28, ultimo parrafo |
| 27% | Telecommunications (landline, mobile, internet) | Ley IVA, Art. 28, ultimo parrafo |

**The 27% rate applies ONLY when the recipient is a Responsable Inscripto (registered IVA taxpayer). For consumers (consumidor final), the standard 21% applies to these services.**

### 1d. Zero-Rated (Exento con credito -- Exportaciones) [T1]

| Category | Legislation |
|----------|-------------|
| Exports of goods (definitive export) | Ley IVA, Art. 8(d) |
| Services rendered abroad and effectively used outside Argentina | Ley IVA, Art. 8(d); Decreto Reglamentario Art. 77 |
| International transport (freight/passengers) | Ley IVA, Art. 8(d) |

**Key distinction:** Exporters CAN recover input IVA. Recovery is via refund (reintegro) or offset mechanism.

### 1e. Exempt Supplies (Exento sin credito) [T1]

| Category | Legislation |
|----------|-------------|
| Education services (formal education) | Ley IVA, Art. 7, inciso (h)(1) |
| Health services (public hospitals, social works -- obras sociales) | Ley IVA, Art. 7, inciso (h)(7) |
| Financial services (interest on deposits, certain financial instruments) | Ley IVA, Art. 7, inciso (h)(16) |
| Insurance (life insurance, retirement, work accident -- ART) | Ley IVA, Art. 7, inciso (h)(11) |
| Sale of stamps, bonds, shares | Ley IVA, Art. 7, inciso (a) |
| Residential rent (for housing) | Ley IVA, Art. 7, inciso (h)(22) |
| Books, pamphlets, printed materials (cultural) | Ley IVA, Art. 7, inciso (a) |
| Water supply to residential consumers (first tier) | Ley IVA, Art. 7, inciso (h)(26) |
| Certain basic foods (when sold by specific entities) | Ley IVA, Art. 7 |
| Public urban passenger transport | Ley IVA, Art. 7, inciso (h)(12) |

### 1f. Not Subject to IVA (No Alcanzado) [T1]

| Category | Notes |
|----------|-------|
| Salaries and wages | Employment income |
| Dividends | Not a sale |
| Sale of used personal goods by non-habitual sellers | Occasional transaction |
| Income from dependent employment | Not a commercial activity |
| Certain provincial and municipal taxes | Government impositions |

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]

- Sale (IVA debito fiscal / output IVA) or Purchase (IVA credito fiscal / input IVA)
- Salaries, social security (cargas sociales), tax payments, loan repayments, dividends = OUT OF SCOPE
- **Legislation:** Ley IVA, Art. 1 (taxable events: sale of goods, rendering of services, definitive imports)

### 2b. Determine Counterparty Location [T1]

- Argentina (domestic): supplier/customer country is AR
- MERCOSUR: Brazil, Paraguay, Uruguay -- common external tariff applies to customs; IVA rules per national law
- International: all other countries
- Special: Tierra del Fuego (special customs territory -- reduced IVA/exempt zone)

### 2c. Determine IVA Rate from Invoice [T1]

- Calculate: `rate = iva_amount / net_amount * 100`
- Normalize to nearest standard rate: 0%, 10.5%, 21%, 27%
- If rate does not match, flag for review [T2]

### 2d. Determine Invoice Type [T1]

| Invoice Type | Issued By | Issued To | IVA Shown |
|-------------|-----------|-----------|-----------|
| Factura A | Responsable Inscripto | Responsable Inscripto | Yes -- IVA discriminated |
| Factura B | Responsable Inscripto | Consumidor Final, Exento, Monotributista | No -- IVA embedded in total |
| Factura C | Monotributista or Exento | Any | No IVA (Monotributista does not charge IVA) |
| Factura E | Any exporter | Foreign customer | Export invoice |
| Factura M | Responsable Inscripto (AFIP control) | Responsable Inscripto | IVA shown but subject to withholding |

**Only Factura A and Factura de Importacion generate credito fiscal for the buyer.**

---

## Step 3: IVA Return Form Mapping (F.2002) [T1]

**Legislation:** RG AFIP 715/2000 (and amendments); SIAP/AFIP Portal.

### Output IVA (Debito Fiscal)

| Section | Description | Rate |
|---------|-------------|------|
| Ventas gravadas 21% | Taxable sales at standard rate | 21% |
| Ventas gravadas 10.5% | Taxable sales at reduced rate | 10.5% |
| Ventas gravadas 27% | Taxable sales at higher rate | 27% |
| Ventas exentas | Exempt sales | 0% |
| Exportaciones | Export sales (zero-rated) | 0% |
| Total Debito Fiscal | Sum of all output IVA | calculated |

### Input IVA (Credito Fiscal)

| Section | Description |
|---------|-------------|
| Compras gravadas 21% | Purchases at standard rate |
| Compras gravadas 10.5% | Purchases at reduced rate |
| Compras gravadas 27% | Purchases at higher rate |
| Importaciones | IVA on imports |
| Total Credito Fiscal | Sum of all input IVA |

### Withholdings and Collections (Retenciones y Percepciones)

| Section | Description |
|---------|-------------|
| Retenciones IVA sufridas | IVA withheld by buyers (credit for the seller) |
| Percepciones IVA sufridas | IVA collected by suppliers (additional credit for the buyer) |
| Percepciones aduaneras | IVA perceptions at customs on imports |
| Retenciones practicadas | IVA withheld by client (as agent -- reported but not a credit) |

### Balance

| Line | Description |
|------|-------------|
| Saldo tecnico | Debito Fiscal minus Credito Fiscal |
| Retenciones y percepciones | IVA withheld/collected suffered (reduces tax payable) |
| Saldo a favor AFIP | Tax payable to AFIP |
| Saldo a favor del contribuyente | Credit balance (carried forward or refundable for exporters) |
| Saldo de libre disponibilidad | Freely available credit (from retenciones/percepciones excess) |

---

## Step 4: Monotributo (Simplified Regime) [T1]

**Legislation:** Ley 24.977 (Regimen Simplificado para Pequenos Contribuyentes -- Monotributo), texto ordenado Anexo Ley 26.565.

### Overview [T1]

| Feature | Detail |
|---------|--------|
| What is Monotributo | Unified monthly payment replacing IVA, Income Tax, and Social Security contributions |
| Who qualifies | Individuals and certain partnerships (sociedades de hecho) with income below thresholds |
| IVA impact | Monotributistas do NOT charge IVA and do NOT file IVA returns |
| Invoice type | Issue Factura C (no IVA discriminated) |
| Input IVA | Cannot recover credito fiscal |

### Categories and Thresholds (January 2026, subject to semi-annual update) [T1]

| Category | Annual Income Limit (Services) | Annual Income Limit (Goods) | Monthly Payment (approximate) |
|----------|-------------------------------|----------------------------|-------------------------------|
| A | ARS 10,277,988 | ARS 10,277,988 | Varies by category |
| B | ARS 15,058,448 | ARS 15,058,448 | Varies |
| C | ARS 21,113,697 | ARS 21,113,697 | Varies |
| D | ARS 26,212,684 | ARS 26,212,684 | Varies |
| E | ARS 30,833,423 | ARS 36,424,946 | Varies |
| F | ARS 38,641,459 | ARS 45,537,978 | Varies |
| G | ARS 46,210,165 | ARS 54,502,805 | Varies |
| H | ARS 70,069,823 | ARS 70,069,823 | Varies |
| I | N/A (goods only) | ARS 78,472,882 | Varies |
| J | N/A (goods only) | ARS 89,868,576 | Varies |
| K | N/A (goods only) | ARS 108,357,084 | Varies |

**Note:** These thresholds are updated semi-annually (January and July) due to inflation, based on IPC variation. Always verify current values on the ARCA website (afip.gob.ar/monotributo/categorias.asp). The values above reflect the January 2026 update (14.28% IPC adjustment). A further recategorization applies in April 2026.

### Exclusion Events [T1]

| Event | Consequence |
|-------|-------------|
| Income exceeds category K threshold | Automatic exclusion; must register as Responsable Inscripto |
| More than 3 permitted activities | Exclusion |
| Imports in last 12 months exceed threshold | Exclusion |
| Price per unit exceeds threshold | Exclusion |
| Cost of goods/services exceeds percentage of income | Exclusion |

**If excluded, taxpayer must register as Responsable Inscripto within 10 days and begin filing monthly IVA returns.**

---

## Step 5: Withholding and Collection Regimes (Retenciones y Percepciones) [T2]

**Legislation:** RG AFIP 2.854 (retenciones); RG AFIP 3.685 (percepciones); various RG for specific regimes.

### IVA Withholding (Retencion de IVA) [T2]

| Element | Detail |
|---------|--------|
| Who withholds | Designated withholding agents (grandes contribuyentes, government, specific designees) |
| When | At the time of payment to a Responsable Inscripto supplier |
| Rate | Generally 50% of IVA, but varies (100% for certain cases; reduced rates for specific activities) |
| Minimum | Thresholds per transaction below which no withholding applies |
| Certificate | Agent must issue "Constancia de Retencion" to supplier |
| Supplier treatment | Withheld amount is a credit on the supplier's F.2002 return |

### IVA Collection (Percepcion de IVA) [T2]

| Element | Detail |
|---------|--------|
| Who collects | Designated collection agents (suppliers designated by AFIP) |
| When | At the time of invoicing to a Responsable Inscripto buyer |
| Rate | Generally 3% of net sale, but varies by regime |
| Invoice | Perception must be shown separately on the invoice |
| Buyer treatment | Collected amount is a credit on the buyer's F.2002 return |

### Customs Perceptions [T1]

| Element | Detail |
|---------|--------|
| What | Additional IVA perception charged on imports at customs |
| Rate | 20% of tax base for Responsables Inscriptos; 21% for non-inscriptos |
| Base | CIF value + customs duty + statistics fee + IVA |
| Treatment | Credit on F.2002 (percepciones aduaneras) |
| Legislation | RG AFIP 2.937 |

**Flag for reviewer:** Withholding and collection rates vary by regime, sector, and AFIP designation. Always verify the applicable rate and minimum threshold with the specific RG.

---

## Step 6: Electronic Invoicing (Facturacion Electronica) [T1]

**Legislation:** RG AFIP 4.164 (2017); RG AFIP 4.291 (Factura de Credito Electronica MiPyME).

### Mandatory Requirements [T1]

| Requirement | Detail |
|-------------|--------|
| Who must issue | ALL Responsables Inscriptos and Monotributistas (categories H and above; as of recent RG, all categories) |
| Method | Via AFIP web service (WSFE) or authorized fiscal controller (Controlador Fiscal) |
| CAE | Each invoice receives a CAE (Codigo de Autorizacion Electronico) from AFIP in real time |
| Validity | CAE has a validity period (generally 10 days from issuance) |
| QR Code | Mandatory QR code on printed invoice for verification |
| Storage | Minimum 10 years (Ley 11.683, Art. 48) |

### Document Types [T1]

| Type Code | Document | Issued By |
|-----------|----------|-----------|
| 001 | Factura A | RI to RI |
| 006 | Factura B | RI to CF/Exento/Mono |
| 011 | Factura C | Monotributista/Exento to any |
| 019 | Factura E | Exporter to foreign |
| 051 | Factura M | RI (controlled) to RI |
| 003 | Nota de Credito A | Credit note RI to RI |
| 008 | Nota de Credito B | Credit note RI to CF |
| 013 | Nota de Credito C | Credit note Mono to any |

### Factura de Credito Electronica MiPyME [T2]

**Legislation:** Ley 27.440; RG AFIP 4.291.

| Feature | Detail |
|---------|--------|
| What | Special invoice type for SME suppliers selling to large buyers |
| Purpose | Allows SME to negotiate the receivable (factoring) |
| Who issues | MiPyME registered supplier |
| Who receives | Large company buyer (must accept or reject within 30 days) |
| IVA impact | Standard IVA treatment; additional administrative requirement |

---

## Step 7: IVA on Imports [T1]

**Legislation:** Ley IVA, Art. 1, inciso (c); Art. 25-27.

### Import of Goods [T1]

| Element | Detail |
|---------|--------|
| Taxable event | Definitive import of goods into Argentine customs territory |
| Tax base | CIF value + customs duty (derechos de importacion) + statistics fee (tasa de estadistica) |
| Rate | 21% (standard) or 10.5% (if goods qualify for reduced rate) |
| Collection | IVA collected by Aduana (Customs) at import |
| Additional perceptions | 20% perception (RG 2.937) on top of IVA for RI; 21% for non-RI |
| Deductibility | IVA on imports deductible as credito fiscal on F.2002 |
| Perceptions | Also deductible as credit (percepciones aduaneras section) |

### Import of Services [T1]

**Legislation:** Ley IVA, Art. 1, inciso (d) (added by Ley 27.430).

| Element | Detail |
|---------|--------|
| Taxable event | Services provided from abroad and effectively used in Argentina |
| Tax base | Total amount paid for the service |
| Rate | 21% |
| Mechanism | Buyer self-assesses IVA (reverse charge -- "IVA por prestaciones del exterior") |
| Filing | Declared on F.2002; buyer pays via VEP (Volante Electronico de Pago) |
| Deductibility | Self-assessed IVA is simultaneously deductible as credito fiscal (net zero for fully taxable businesses) |
| Digital services | Foreign providers of digital services to Argentine consumers must register and charge IVA (RG 4.240) |

---

## Step 8: Export IVA Recovery (Reintegro de IVA a Exportadores) [T1]

**Legislation:** Ley IVA, Art. 43; RG AFIP 2.000 (Solicitud de Reintegro).

### Mechanism [T1]

| Element | Detail |
|---------|--------|
| Who qualifies | Exporters (IVA exempt on exports with right to credit) |
| What is recoverable | Credito fiscal (input IVA) attributable to export activity |
| Method | Refund request to AFIP via "Solicitud de Acreditacion, Devolucion o Transferencia" |
| Calculation | Credito fiscal * (Export sales / Total sales) |
| Limit | Cannot exceed statutory export reimbursement rate (alicuota del bien) |
| Timeline | AFIP has 60 business days to process (often longer in practice) |

### Export Reimbursement vs IVA Refund [T2]

| Concept | Detail |
|---------|--------|
| Reintegros de exportacion | Customs-based reimbursement (derechos de exportacion negativos) -- separate from IVA |
| Devolucion de IVA | Recovery of input IVA on export-related purchases -- this is the IVA refund |
| Draw-back | Refund of import duties on inputs used for exported goods -- separate from IVA |

**Flag for reviewer:** Export IVA recovery is a complex area frequently audited by AFIP. Ensure all documentation (customs declarations, purchase invoices with CAE, shipping documents) is complete and cross-referenced. The credito fiscal must be directly attributable to export activity.

---

## Step 9: Proportionality Rule (Prorrateo) [T2]

**Legislation:** Ley IVA, Art. 13.

### When It Applies [T2]
When a taxpayer makes both taxable (gravadas) and exempt (exentas) sales, credito fiscal on common expenses must be apportioned.

### Calculation [T2]

```
Proportion % = (Taxable Sales / Total Sales) * 100
Deductible Credito Fiscal = Common Input IVA * Proportion %
```

| Expense Type | Treatment |
|-------------|-----------|
| Exclusively for taxable sales | 100% credito fiscal |
| Exclusively for exempt sales | 0% credito fiscal |
| Common/shared expenses | Proportional (prorrateo) |

**Flag for reviewer: prorrateo must be confirmed by Contador Publico before applying. Annual adjustment required at fiscal year-end.**

---

## Step 10: Non-Deductible Input IVA [T1]

**Legislation:** Ley IVA, Art. 12; Decreto Reglamentario Art. 52.

### Categories Where Credito Fiscal is NOT Allowed [T1]

| Category | Legislation | Notes |
|----------|-------------|-------|
| Purchases not related to taxable activity | Ley IVA, Art. 12 | Must have direct/indirect nexus |
| Automobiles (above depreciation threshold) | Ley Ganancias, Art. 88 cross-reference | Limited by income tax deduction caps |
| Personal consumption items | Ley IVA, Art. 12 | Not business-related |
| Purchases from Monotributistas | Invoice C | No IVA discriminated on Factura C; no credito fiscal |
| Purchases documented on Factura B | Invoice B | IVA embedded, not discriminated; no credito fiscal |
| Entertainment (esparcimiento) | General principle | Unless directly related to taxable sales |

### Credito Fiscal Requirement [T1]

- Only IVA shown (discriminado) on Factura A or Factura de Importacion generates credito fiscal
- IVA embedded in Factura B or Factura C is NOT recoverable
- The invoice must have a valid CAE from AFIP

---

## Step 11: Filing Deadlines [T1]

**Legislation:** RG AFIP (annual resolution setting due dates based on CUIT termination).

### Standard Filing [T1]

| Period | Filing Deadline | Notes |
|--------|----------------|-------|
| Monthly (all Responsables Inscriptos) | Between 18th and 22nd of following month | Exact date depends on last digit of CUIT |
| Monotributistas | Monthly payment (no IVA return) | Between 20th and 24th |

### CUIT-Based Due Dates (Typical) [T1]

| Last Digit of CUIT | Approximate Due Date |
|--------------------|---------------------|
| 0-1 | 18th of following month |
| 2-3 | 19th of following month |
| 4-5 | 20th of following month |
| 6-7 | 21st of following month |
| 8-9 | 22nd of following month |

**Exact dates are set annually by AFIP resolution. Always verify the current fiscal calendar.**

### Late Filing Penalties [T1]

| Penalty | Calculation | Legislation |
|---------|-------------|-------------|
| Late filing (presentacion extemporanea) | Formal penalty (multa) under Art. 38 Ley 11.683 | Up to ARS amount set annually |
| Late payment interest (intereses resarcitorios) | Daily rate set by AFIP (approximately 4-6% monthly) | Ley 11.683, Art. 37 |
| Tax evasion | 2-10 times the evaded tax (criminal penalties possible) | Ley Penal Tributaria 27.430 |
| Omission penalty | 50-100% of omitted tax | Ley 11.683, Art. 45 |

---

## Step 12: Key Thresholds [T1]

| Threshold | Value | Notes |
|-----------|-------|-------|
| Responsable Inscripto | No minimum | All commercial activity not in Monotributo |
| Monotributo max (services) | Category H annual limit | Verify current AFIP values |
| Monotributo max (goods) | Category K annual limit | Verify current AFIP values |
| Withholding minimum (general) | Varies by RG | Check specific RG for threshold |
| Perception rate (customs) | 20% (RI) / 21% (non-RI) | On imports |
| Automobile deduction cap | Income tax limitation | Cross-reference with Ley Ganancias |
| Statute of limitations | 5 years (standard); 10 years (non-registered) | Ley 11.683, Art. 56-57 |

---

## Step 13: Saldo a Favor (Credit Balances) [T1]

**Legislation:** Ley IVA, Art. 24; Ley 11.683.

### Types of Credit Balances [T1]

| Type | Name | Origin | Usage |
|------|------|--------|-------|
| Saldo Tecnico a Favor | Technical balance | Credito fiscal exceeds debito fiscal | Carry forward only; NOT refundable (except exporters) |
| Saldo de Libre Disponibilidad | Freely available balance | Excess retenciones/percepciones after absorbing tax payable | Can offset other national taxes or request refund |

### Rules [T1]

| Rule | Detail |
|------|--------|
| Saldo tecnico | Carries forward indefinitely to next period; can only offset future debito fiscal |
| Saldo libre disponibilidad | Can offset IVA, Income Tax (Ganancias), or other national taxes; can request cash refund |
| Exporter saldo tecnico | Exporters CAN request refund of saldo tecnico attributable to exports (Art. 43) |
| Indexation | No inflation adjustment on carried-forward balances (significant in high-inflation environment) |

---

## Step 14: Tierra del Fuego and Special Zones [T2]

**Legislation:** Ley 19.640 (Tierra del Fuego Promotion Regime).

### Tierra del Fuego (TdF) [T2]

| Rule | Detail |
|------|--------|
| Sales within TdF | Exempt from IVA |
| Sales from mainland Argentina to TdF | Treated as export (zero-rated) |
| Sales from TdF to mainland | Treated as import (IVA applies at import) |
| Companies based in TdF | Exempt from IVA on local activity; special regime applies |

**Flag for reviewer:** Tierra del Fuego rules are complex and interact with customs and income tax regimes. Escalate to specialist.

### Free Trade Zones (Zonas Francas) [T2]

| Rule | Detail |
|------|--------|
| Goods entering ZF from abroad | No IVA (no import) |
| Goods from ZF to mainland Argentina | IVA at import |
| Services within ZF | Special treatment -- review applicable rules |

---

## Step 15: Reviewer Escalation Protocol

When a [T2] situation is identified, output the following structured flag:

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

## Step 16: Edge Case Registry

### EC1 -- Utility bill at 27% (electricity, gas) [T1]
**Situation:** Client (Responsable Inscripto) receives electricity bill with 27% IVA.
**Resolution:** The 27% rate is correct for utilities supplied to Responsables Inscriptos. Credito fiscal at 27% is fully deductible (assuming related to taxable activity). Report on F.2002 in the 27% section.
**Legislation:** Ley IVA, Art. 28, ultimo parrafo.

### EC2 -- Purchase from Monotributista supplier [T1]
**Situation:** Client purchases goods from a Monotributista supplier. Factura C received.
**Resolution:** No credito fiscal. Factura C does not discriminate IVA. The full invoice amount is the expense cost. No IVA entry on F.2002 for this purchase.
**Legislation:** Ley 24.977 (Monotributo).

### EC3 -- Software subscription from US provider (e.g., Google, AWS) [T1]
**Situation:** Monthly charge from a US company for digital services.
**Resolution:** Reverse charge applies. Client self-assesses IVA at 21% ("IVA por prestaciones del exterior"). Report as debito fiscal and simultaneously claim as credito fiscal on F.2002. Net zero for fully taxable businesses. Payment via VEP.
**Legislation:** Ley IVA, Art. 1(d); Ley 27.430.

### EC4 -- Credit note received from supplier [T1]
**Situation:** Supplier issues Nota de Credito A for returned goods.
**Resolution:** Reduce credito fiscal by the IVA amount on the Nota de Credito. The NC must have a valid CAE and reference the original Factura.
**Legislation:** Ley IVA, Art. 12; RG AFIP 1.415.

### EC5 -- Retencion de IVA suffered by client [T1]
**Situation:** Client (supplier) receives payment from a Grande Contribuyente buyer who withheld IVA.
**Resolution:** Client reports the withheld amount in "Retenciones IVA sufridas" section of F.2002. This reduces tax payable. If retenciones exceed tax payable, the excess becomes saldo de libre disponibilidad.
**Legislation:** RG AFIP 2.854.

### EC6 -- Export of services [T1]
**Situation:** Argentine company provides consulting services to a foreign client. Service used exclusively abroad.
**Resolution:** Zero-rated under Art. 8(d). Issue Factura E. No IVA charged. Credito fiscal on related costs IS recoverable via refund mechanism (Art. 43).
**Legislation:** Ley IVA, Art. 8(d); Art. 43.

### EC7 -- Sale of used fixed asset [T2]
**Situation:** Client sells a computer previously used as a fixed asset.
**Resolution:** Sale of movable goods that were fixed assets used in the business is subject to IVA at the applicable rate. The tax base is the sale price. If the original credito fiscal was taken, IVA must be charged on the sale. Flag for reviewer if original treatment of input IVA is unclear.
**Legislation:** Ley IVA, Art. 2.

### EC8 -- Mixed invoice: taxable + exempt items [T1]
**Situation:** Single invoice includes both taxable (21%) and exempt items.
**Resolution:** Credito fiscal is only deductible on the IVA attributed to taxable items. Split the invoice by line item. If line items are not segregated, flag for reviewer [T2].
**Legislation:** Ley IVA, Art. 12.

### EC9 -- Monotributo exclusion mid-year [T2]
**Situation:** Monotributista exceeds income threshold mid-year and is excluded.
**Resolution:** Must register as Responsable Inscripto within 10 business days. Begin filing monthly F.2002 from the exclusion date. Cannot recover input IVA on pre-exclusion purchases. Must begin issuing Factura A/B (not C). Flag for reviewer: transition requires careful handling of opening balances and retroactive liability assessment.
**Legislation:** Ley 24.977, Art. 21.

### EC10 -- Provincial gross income tax (Ingresos Brutos) confusion [T1]
**Situation:** Client confuses IVA (national) with Ingresos Brutos (provincial turnover tax).
**Resolution:** These are entirely separate taxes. IVA is national (AFIP/ARCA). Ingresos Brutos is provincial (ARBA for Buenos Aires, AGIP for CABA, etc.). Ingresos Brutos is NOT deductible against IVA. They appear on separate returns. This skill covers IVA only.
**Legislation:** Ley IVA (national); provincial fiscal codes (Ingresos Brutos).

---

## Step 17: Inflation and IVA Considerations [T1]

### Impact on Credit Balances [T1]

| Issue | Detail |
|-------|--------|
| Nominal balances | Saldo tecnico and saldo de libre disponibilidad are carried at nominal value |
| No inflation adjustment | Argentine law does not provide for inflation adjustment of IVA credit balances |
| Real value erosion | In high-inflation environments, credit balances lose real value over time |
| Strategic implication | Businesses should manage the timing of input vs output IVA to minimize persistent credit balances |

### Impact on Thresholds [T1]

| Issue | Detail |
|-------|--------|
| Monotributo thresholds | Updated periodically (often quarterly) to reflect inflation |
| Withholding minimums | Updated by AFIP resolution |
| UVT equivalent | Argentina does not use a UVT; thresholds are set in ARS and updated by resolution |

---

## Step 18: Test Suite

### Test 1 -- Standard local sale at 21%
**Input:** Argentine company sells consulting services to local Responsable Inscripto, net ARS 1,000,000, IVA ARS 210,000. Factura A issued.
**Expected output:** F.2002, Ventas gravadas 21% += ARS 1,000,000, Debito Fiscal += ARS 210,000.

### Test 2 -- Purchase at 21% with Factura A
**Input:** Company purchases office supplies from RI supplier, net ARS 50,000, IVA ARS 10,500. Valid Factura A with CAE.
**Expected output:** F.2002, Compras gravadas 21% += ARS 50,000, Credito Fiscal += ARS 10,500.

### Test 3 -- Electricity bill at 27%
**Input:** RI client receives electricity bill: net ARS 100,000, IVA ARS 27,000 (27%).
**Expected output:** F.2002, Compras gravadas 27% += ARS 100,000, Credito Fiscal += ARS 27,000.

### Test 4 -- Purchase from Monotributista (no credito fiscal)
**Input:** Company buys supplies from Monotributista, total ARS 50,000. Factura C received.
**Expected output:** No credito fiscal. No IVA entry on F.2002. Full ARS 50,000 is expense.

### Test 5 -- Export of goods
**Input:** Company exports goods, FOB value USD 10,000. Factura E issued. Customs export declaration filed.
**Expected output:** F.2002, Exportaciones += ARS equivalent. No debito fiscal. Credito fiscal on inputs recoverable via Art. 43 refund.

### Test 6 -- Import of services (reverse charge)
**Input:** Company pays USD 5,000 (ARS 4,500,000) for foreign consulting services.
**Expected output:** Self-assess IVA: ARS 4,500,000 * 21% = ARS 945,000. Report as debito fiscal AND credito fiscal. Net zero. Pay self-assessed IVA via VEP.

### Test 7 -- Retencion de IVA suffered
**Input:** Client (supplier) receives payment of ARS 1,000,000 + IVA ARS 210,000 from a Grande Contribuyente. Buyer withheld 50% of IVA = ARS 105,000.
**Expected output:** F.2002, Debito Fiscal += ARS 210,000 (full IVA on sale). Retenciones sufridas += ARS 105,000 (credit). Net tax payable reduced by ARS 105,000.

### Test 8 -- Capital goods purchase at 10.5%
**Input:** Company purchases industrial machinery, net ARS 5,000,000, IVA ARS 525,000 (10.5%). Factura A.
**Expected output:** F.2002, Compras gravadas 10.5% += ARS 5,000,000, Credito Fiscal += ARS 525,000.

---

## PROHIBITIONS [T1]

- NEVER allow credito fiscal on Factura B or Factura C (IVA not discriminated)
- NEVER file an IVA return for a Monotributista client (they pay fixed monthly amount, no IVA return)
- NEVER apply the 27% rate to utility sales to consumidores finales (21% applies to CF)
- NEVER ignore the distinction between saldo tecnico (carry forward only) and saldo de libre disponibilidad (freely usable)
- NEVER allow credito fiscal without valid CAE on the invoice
- NEVER omit reverse charge on services imported from abroad
- NEVER confuse IVA (national, AFIP) with Ingresos Brutos (provincial)
- NEVER ignore inflation impact on nominal credit balances
- NEVER accept a Monotributo exclusion without triggering RI registration obligation
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Contribution Notes (For Adaptation to Other Jurisdictions)

If you are adapting this skill for another country, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all form numbers (F.2002) and section names with your jurisdiction's equivalent.
3. Replace IVA rates (21%/10.5%/27%) with your jurisdiction's standard, reduced, and higher rates.
4. Replace the Monotributo thresholds with your jurisdiction's simplified regime equivalent.
5. Replace the withholding/collection agent rules with your jurisdiction's equivalent.
6. Replace the electronic invoicing requirements (CAE, WSFE) with your jurisdiction's e-invoicing rules.
7. Replace the inflation considerations with your jurisdiction's relevant economic context.
8. Have a licensed accountant in your jurisdiction validate every T1 rule before publishing.
9. Add your own edge cases to the Edge Case Registry for known ambiguous situations in your jurisdiction.
10. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
