---
name: peru-igv
description: Use this skill whenever asked to prepare, review, or create a Peru IGV (Impuesto General a las Ventas) return for any client. Trigger on phrases like "prepare IGV return", "declaracion de IGV", "Peru VAT", "PDT 621", "Declara Facil", "SUNAT filing", "comprobante de pago", "detracciones", "retenciones", "percepciones", or any request involving Peruvian IGV filing. Also trigger when classifying transactions for IGV purposes from bank statements, invoices, or other source data. This skill contains the complete Peru IGV classification rules, PDT 621 mappings, deductibility rules, the 18% composite rate (16% IGV + 2% IPM), SPOT detracciones system, retenciones and percepciones regimes, and filing deadlines required to produce a correct return. ALWAYS read this skill before touching any IGV-related work for Peru.
---

# Peru IGV Return Preparation Skill

---

## Skill Metadata

| Field | Value |
|-------|-------|
| Jurisdiction | Peru |
| Jurisdiction Code | PE |
| Primary Legislation | TUO de la Ley del IGV e ISC (Decreto Supremo 055-99-EF) |
| Supporting Legislation | Reglamento de la Ley del IGV (DS 029-94-EF); Ley 29215 (credito fiscal); RS 183-2004/SUNAT (SPOT/Detracciones); RS 037-2002/SUNAT (Retenciones); RS 058-2006/SUNAT (Percepciones); Ley 32387 (gradual IGV/IPM restructuring 2026-2029); Ley 32219 (extension of reduced 8% rate for tourism/hospitality MYPES through 2026) |
| Tax Authority | SUNAT -- Superintendencia Nacional de Aduanas y de Administracion Tributaria |
| Filing Portal | https://www.sunat.gob.pe (SOL -- SUNAT Operaciones en Linea / Declara Facil) |
| Contributor | Open Accounting Skills Registry |
| Validated By | Deep research verification, April 2026 |
| Validation Date | April 2026 |
| Skill Version | 1.0 |
| Confidence Coverage | Tier 1: rate classification, PDT 621 mapping, filing periods, SPOT triggers. Tier 2: partial credit (prorrata), sector-specific SPOT rates, complex retenciones/percepciones. Tier 3: transfer pricing, free trade zones (CETICOS/ZOFRATACNA), mining royalties. |

---

## Confidence Tier Definitions

Every rule in this skill is tagged with a confidence tier:

- **[T1] Tier 1 -- Deterministic.** Apply exactly as written. No reviewer judgement required.
- **[T2] Tier 2 -- Reviewer Judgement Required.** Flag the issue and present options. A licensed Contador Publico Colegiado must confirm before filing.
- **[T3] Tier 3 -- Out of Scope / Escalate.** Skill does not cover this. Do not guess. Escalate to licensed Contador Publico Colegiado and document the gap.

---

## Step 0: Client Onboarding Questions

Before classifying ANY transaction, you MUST know these facts about the client. Ask if not already known:

1. **Entity name and RUC (Registro Unico de Contribuyentes)** [T1] -- 11-digit number (10 for empresas, 20 for juridicas, 15/17 for other)
2. **Tax regime** [T1] -- Regimen General, Regimen MYPE Tributario (RMT), Regimen Especial (RER), or NRUS (Nuevo Regimen Unico Simplificado)
3. **Filing period** [T1] -- Monthly (all regimes except NRUS)
4. **Industry/sector** [T2] -- impacts SPOT (detracciones) rates
5. **Does the business make exempt/inafectas supplies?** [T2] -- If yes, proportional credit (prorrata) required
6. **Is the client designated as agente de retencion by SUNAT?** [T1] -- retention agent obligations
7. **Does the client export goods or services?** [T1] -- exporters can recover IGV (saldo a favor del exportador)
8. **Does the client have a Banco de la Nacion account for detracciones?** [T1] -- mandatory for SPOT system
9. **Is the client subject to percepciones on imports or domestic purchases?** [T1]

**If any of items 1-3 are unknown, STOP. Do not classify any transactions until RUC and tax regime are confirmed.**

---

## Step 1: IGV Rate Structure [T1]

### 1a. The 18% Composite Rate [T1]

| Component | Rate (through 2025) | Rate (2026) | Legislation |
|-----------|---------------------|-------------|-------------|
| IGV (Impuesto General a las Ventas) | 16% | 15.5% | TUO IGV, Art. 17; Ley 32387 |
| IPM (Impuesto de Promocion Municipal) | 2% | 2.5% | Decreto Legislativo 776, Art. 76; Ley 32387 |
| **Total effective rate** | **18%** | **18%** | Combined |

**The total 18% rate is unchanged, but the split between IGV and IPM is gradually shifting under Ley 32387 to increase municipal funding. The schedule is: 2026 (15.5% IGV + 2.5% IPM), 2027 (15% + 3%), 2028 (14.5% + 3.5%), 2029 (14% + 4%). For all practical purposes, the combined rate remains 18%. IGV and IPM are declared and paid together.**

### 1a-bis. Reduced Rate for Tourism/Hospitality MYPES [T2]

**Legislation:** Ley 31556; Ley 32219 (extension through December 31, 2026).

| Component | Rate (2025) | Rate (2026) | Application |
|-----------|-------------|-------------|-------------|
| IGV (reduced) | 8% | 8% | Micro and small companies in restaurants, hotels, tourist accommodations, catering |
| IPM | 2% | 2.5% | Municipal promotion tax |
| **Total** | **10%** | **10.5%** | Combined reduced rate for qualifying MYPES |

**Flag for reviewer [T2]:** Confirm client qualifies as micro or small enterprise (MYPE) under the applicable SUNAT/MTPE criteria. The reduced rate applies only through December 31, 2026 (rate rises to 12% IGV for 2027). Verify current IPM rate applies correctly.

### 1b. Zero-Rated (Exportaciones) [T1]

| Category | Legislation |
|----------|-------------|
| Export of goods (definitive export) | TUO IGV, Art. 33 |
| Export of services (Appendix V list) | TUO IGV, Art. 33; Appendix V |
| International transport (freight) | TUO IGV, Art. 33 |
| Sub-contracting services for export production | TUO IGV, Art. 33 (conditions apply) |

### 1c. Exempt Supplies (Exoneradas) [T1]

**Legislation:** TUO IGV, Art. 5; Appendix I (goods); Appendix II (services).

| Category | Appendix | Notes |
|----------|----------|-------|
| Basic food (rice, sugar, milk, bread, tubers, vegetables, fruits) | Appendix I | Unprocessed/minimally processed |
| Live animals (cattle, poultry, fish for consumption) | Appendix I | Primary production |
| Fertilizers, pesticides | Appendix I | Agricultural inputs |
| Books, newspapers, periodicals | Appendix I | Cultural goods |
| Gold for Banco Central de Reserva | Appendix I | Monetary gold |
| Education services (formal) | Appendix II | Schools, universities |
| Health/medical services | Appendix II | Hospitals, clinics |
| Public urban transport (passenger) | Appendix II | Buses, metro |
| Financial services (interest on credits) | Appendix II | Banks, financieras |
| Insurance (life, accident) | Appendix II | Certain policies |
| Residential rent | Appendix II | Housing only |
| Transfer of used goods by non-habitual sellers | Appendix II | Personal/occasional sales |
| Shows and cultural events | Appendix II | Certain categories |

### 1d. Not Subject to IGV (Inafectas) [T1]

| Category | Legislation |
|----------|-------------|
| Salaries and wages | Not a sale/service |
| Dividends | Not a sale |
| Transfer of assets in reorganizations (mergers, splits) | TUO IGV, Art. 2 |
| Government fees and contributions | Not commercial activity |
| Lottery and game winnings | Separate tax regime |
| Sale of shares and securities | Not subject to IGV |

---

## Step 2: Transaction Classification Rules

### 2a. Determine Transaction Type [T1]

- Sale (IGV debito fiscal / output IGV) or Purchase (IGV credito fiscal / input IGV)
- Salaries, CTS, gratificaciones, AFP/ONP contributions, tax payments = OUT OF SCOPE
- **Legislation:** TUO IGV, Art. 1 (taxable events: sale of goods, rendering of services, construction contracts, first sale of real estate, imports)

### 2b. Determine Tax Document Type (Comprobante de Pago) [T1]

| Document | Usage | IGV Credit |
|----------|-------|------------|
| Factura | B2B sales; required when buyer needs IGV credit | Yes |
| Boleta de Venta | B2C sales (consumers, NRUS, RER) | No -- buyer cannot claim credito fiscal |
| Nota de Credito | Credit note (reversal/adjustment) | Adjusts credito fiscal |
| Nota de Debito | Debit note (additional charges) | Adjusts credito fiscal |
| Liquidacion de Compra | Buyer-issued invoice for purchases from unregistered/informal suppliers | Yes (conditions) |
| Ticket (maquina registradora) | Small retail transactions | No credito fiscal (unless special format) |
| Recibo por Honorarios | Professional services fee receipt | Not subject to IGV (independent workers under 4ta categoria) |

### 2c. Determine Counterparty Location [T1]

- Peru (domestic): supplier/customer country is PE
- Andean Community (CAN): Bolivia, Colombia, Ecuador -- Decision 599 rules
- International: all other countries

---

## Step 3: PDT 621 / Declara Facil Form Mapping [T1]

**Legislation:** RS SUNAT; PDT 621 -- Declaracion Jurada Mensual IGV-Renta.

### Output IGV (Debito Fiscal)

| Section | Description |
|---------|-------------|
| Base imponible de ventas gravadas | Net taxable sales |
| Ventas gravadas destinadas a operaciones gravadas | Standard taxable sales |
| Ventas gravadas destinadas a operaciones no gravadas | Mixed sales (for prorrata) |
| Ventas no gravadas | Exempt/inafectas sales (no IGV) |
| Exportaciones | Export sales (zero-rated) |
| IGV de ventas | Output IGV (18% of taxable base) |

### Input IGV (Credito Fiscal)

| Section | Description |
|---------|-------------|
| Compras gravadas destinadas a operaciones gravadas | Purchases for taxable activity |
| Compras gravadas destinadas a operaciones no gravadas | Purchases for exempt/inafecta activity |
| Compras gravadas destinadas a operaciones gravadas y no gravadas | Common purchases (prorrata) |
| Compras no gravadas | Exempt/inafecta purchases |
| IGV de compras | Input IGV |

### SPOT, Retenciones, and Percepciones

| Section | Description |
|---------|-------------|
| Detracciones depositadas | SPOT deposits credited against IGV |
| Retenciones del periodo | IGV retentions suffered |
| Percepciones del periodo | IGV perceptions suffered |
| Percepciones de periodos anteriores | Carried forward perceptions |

### Balance

| Section | Description |
|---------|-------------|
| IGV resultante | Output IGV minus Input IGV |
| Retenciones y percepciones | Credits from SPOT/retenciones/percepciones |
| IGV a pagar | Tax payable after credits |
| Saldo a favor | Credit balance (carried forward) |

---

## Step 4: Credito Fiscal (Input IGV) Rules [T1]

**Legislation:** TUO IGV, Art. 18-19; Ley 29215.

### Substantive Requirements (Art. 18) [T1]

| Requirement | Detail |
|-------------|--------|
| Allowed as cost/expense for income tax | The purchase must be deductible for income tax purposes |
| Used for taxable operations | Direct nexus to IGV-taxable activity |

### Formal Requirements (Art. 19) [T1]

| Requirement | Detail |
|-------------|--------|
| Valid comprobante de pago | Factura or equivalent (not Boleta de Venta) |
| IGV shown separately | IGV must be discriminated on the comprobante |
| Registered in Registro de Compras | Must be recorded in the purchases ledger within the period (or within 12 months per Ley 29215) |
| Supplier RUC active | Verify on SUNAT portal that supplier RUC is "Habido" (active/located) |
| Payment via banked means (bancarizacion) | For transactions > S/ 2,000 (or USD 500), payment must be through bank transfer, check, etc. (Ley 28194) |

### Items Where Credito Fiscal is NOT Allowed [T1]

| Category | Legislation |
|----------|-------------|
| Purchases supported only by Boleta de Venta | TUO IGV, Art. 19 |
| Purchases from suppliers with RUC "No Habido" (inactive/unlocated) | TUO IGV, Art. 19 |
| Purchases not related to taxable activity | TUO IGV, Art. 18 |
| Personal consumption items | TUO IGV, Art. 18 |
| Purchases not paid via banked means (above threshold) | Ley 28194 |
| Purchases without valid comprobante de pago | TUO IGV, Art. 19 |

---

## Step 5: SPOT -- Sistema de Pago de Obligaciones Tributarias (Detracciones) [T1]

**Legislation:** TUO del Decreto Legislativo 940 (DS 155-2004-EF); RS 183-2004/SUNAT.

### Overview [T1]

| Element | Detail |
|---------|--------|
| What is SPOT | System where the buyer deposits a percentage of the sale price into the supplier's Banco de la Nacion account |
| Purpose | Ensure supplier has funds to pay IGV and other tax obligations |
| When it applies | Sale of goods and services listed in Annexes 1, 2, and 3 of RS 183-2004 |
| Deposit timing | Before payment or within 5 business days of payment (varies by annex) |
| Supplier's account | Special account at Banco de la Nacion (cuenta de detracciones) |
| Supplier use of funds | Only to pay SUNAT tax obligations; after 4 consecutive months of no tax debt, can request libre disponibilidad |

### SPOT Rates by Category (Key Rates) [T1]

| Category | Annex | Rate | Examples |
|----------|-------|------|----------|
| Sugar, ethyl alcohol | 1 | 10% | Specific goods |
| Rice | 2 | 3.85% | Arroz pilado |
| Timber | 2 | 4% | Wood products |
| Sand, stone | 2 | 10% | Construction materials |
| Metal waste/scrap | 2 | 15% | Chatarra |
| Gold | 2 | 10% | Gold for industrial use |
| Construction services | 3 | 4% | Contratos de construccion |
| Freight transport | 3 | 4% | Transporte de carga |
| Business intermediation (commissions) | 3 | 10% | Comision mercantil |
| Manufacturing services (maquila) | 3 | 10% | Fabricacion de bienes por encargo |
| Maintenance/repair of goods | 3 | 10% | Mantenimiento y reparacion |
| Other services (general) | 3 | 12% | Catch-all for most business services |
| Legal, accounting, engineering services | 3 | 10% | Professional services |
| Temporary staffing (tercerizacion) | 3 | 12% | Outsourced personnel |

**Note:** Rates are updated periodically by SUNAT resolution. Always verify current rates.

### SPOT and Credito Fiscal [T1]

| Rule | Detail |
|------|--------|
| Condition for credito fiscal | If the purchase is subject to SPOT, the buyer MUST have deposited the detraccion BEFORE the IGV filing deadline to claim credito fiscal |
| Missed deposit | If deposit is made after the deadline, credito fiscal can only be claimed in the period the deposit is actually made |
| Non-compliance | Failure to deposit detracciones = loss of credito fiscal for that period + penalty |

---

## Step 6: Retenciones de IGV (IGV Retention Regime) [T1]

**Legislation:** RS 037-2002/SUNAT.

### Overview [T1]

| Element | Detail |
|---------|--------|
| Who retains | Agentes de Retencion designated by SUNAT (large buyers, government entities) |
| Rate | 3% of total invoice amount (including IGV) |
| When | At the time of payment |
| Minimum | Applies to payments > S/ 700 |
| Certificate | Agent issues "Comprobante de Retencion" to supplier |
| Supplier treatment | Retained amount is credit on supplier's PDT 621 |

### Mechanics [T1]

| Step | Detail |
|------|--------|
| 1 | Buyer (retention agent) pays supplier invoice minus 3% retention |
| 2 | Buyer remits retained amount to SUNAT (PDT 626) |
| 3 | Supplier reports retention as credit on PDT 621 |
| 4 | If retentions exceed IGV payable, supplier can request refund after 3 consecutive months |

### Example [T1]

| Item | Amount |
|------|--------|
| Service fee (base) | S/ 10,000 |
| IGV at 18% | S/ 1,800 |
| Total invoice | S/ 11,800 |
| Retention (3% of S/ 11,800) | S/ 354 |
| Amount paid to supplier | S/ 11,446 |

---

## Step 7: Percepciones de IGV (IGV Perception Regime) [T1]

**Legislation:** RS 058-2006/SUNAT (sales); RS 203-2003/SUNAT (imports).

### Sales Perceptions [T1]

| Element | Detail |
|---------|--------|
| Who collects | Agentes de Percepcion designated by SUNAT (certain sellers of specific goods) |
| Rate | 2% of sale price (standard); 0.5% (fuel) |
| When | At the time of sale/invoicing |
| Document | Perception shown on Comprobante de Percepcion |
| Buyer treatment | Perceived amount is credit on buyer's PDT 621 |

### Import Perceptions [T1]

| Element | Detail |
|---------|--------|
| Who collects | SUNAT Aduanas (Customs) |
| Rate | 10% (importers not in good standing); 5% (specific goods); 3.5% (general) |
| Base | CIF value + customs duty + IGV on import |
| Buyer treatment | Perceived amount is credit on importer's PDT 621 |
| Carry forward | Unused perceptions carry forward; refund request possible after 3 months |

---

## Step 8: IGV on Imports [T1]

**Legislation:** TUO IGV, Art. 1(e); Art. 20.

### Import of Goods [T1]

| Element | Detail |
|---------|--------|
| Taxable event | Definitive import of goods into Peruvian territory |
| Tax base | CIF value + ad valorem duty + other applicable charges |
| Rate | 18% (16% IGV + 2% IPM) |
| Collection | Collected by SUNAT Aduanas at import |
| Additional perception | 3.5%-10% perception on top of IGV |
| Deductibility | IGV on imports deductible as credito fiscal |

### Import of Services (Utilizacion de Servicios) [T1]

**Legislation:** TUO IGV, Art. 1(b); Art. 21.

| Element | Detail |
|---------|--------|
| Taxable event | Services provided by non-domiciled entities and used in Peru |
| Tax base | Total retribution (amount paid) |
| Rate | 18% |
| Mechanism | Buyer self-assesses IGV (reverse charge) |
| Payment | Via Formulario 1662 (guia de pagos varios) within the month of annotation in Registro de Compras |
| Deductibility | Self-assessed IGV is deductible as credito fiscal (net zero for fully taxable businesses) |

---

## Step 9: Export IGV Recovery (Saldo a Favor del Exportador -- SFE) [T1]

**Legislation:** TUO IGV, Art. 34-35; DS 126-94-EF (Reglamento de NCN).

### Mechanism [T1]

| Element | Detail |
|---------|--------|
| Who qualifies | Exporters (zero-rated under Art. 33) |
| What is recoverable | Credito fiscal attributable to exports |
| Limit | 18% of FOB value of exports (Saldo a Favor Materia de Beneficio -- SFMB) |
| Method 1 | Offset against Income Tax (Impuesto a la Renta) payments |
| Method 2 | Compensacion against other SUNAT-administered taxes |
| Method 3 | Refund via Notas de Credito Negociables (NCN) -- tax credit certificates |
| Timeline | SUNAT has 5 business days (with guarantee) or 15 days (without) to issue NCN |

### Calculation [T1]

```
SFMB = min(Saldo a Favor del Exportador, 18% * FOB Exports)
```

| Item | Detail |
|------|--------|
| Saldo a Favor del Exportador (SFE) | Total credito fiscal minus total debito fiscal (when negative for taxpayer) |
| SFMB | The portion eligible for refund/offset (capped at 18% of exports) |
| Excess | Carries forward to next period |

---

## Step 10: Proportionality Rule (Prorrata) [T2]

**Legislation:** TUO IGV, Art. 23; Reglamento, Art. 6, numeral 6.

### When It Applies [T2]
When a taxpayer makes both taxable (gravadas) and exempt/inafectas sales, credito fiscal on common purchases must be apportioned.

### Classification of Purchases [T1]

| Category | Treatment |
|----------|-----------|
| Compras destinadas a operaciones gravadas | 100% credito fiscal |
| Compras destinadas a operaciones no gravadas | 0% credito fiscal |
| Compras destinadas a operaciones gravadas y no gravadas (comunes) | Proportional |

### Prorrata Calculation [T2]

```
Proportion % = (Taxable Sales last 12 months / Total Sales last 12 months) * 100
Deductible Credito Fiscal (common) = Common Input IGV * Proportion %
```

**Flag for reviewer: prorrata calculation must be confirmed by Contador Publico Colegiado before applying. The 12-month rolling period must be verified.**

---

## Step 11: Filing Deadlines [T1]

**Legislation:** RS SUNAT (annual cronograma -- filing calendar based on last digit of RUC).

### Standard Filing [T1]

| Period | Filing Deadline | Notes |
|--------|----------------|-------|
| Monthly (Regimen General, RMT, RER) | Between 12th and 22nd of following month | Exact date depends on last digit of RUC |
| NRUS | Monthly payment (no return) | Same calendar |

### RUC-Based Due Dates (Typical) [T1]

| Last Digit of RUC | Approximate Due Date |
|-------------------|---------------------|
| 0 | 12th-14th of following month |
| 1 | 13th-15th |
| 2 | 14th-16th |
| 3 | 15th-17th |
| 4 | 16th-18th |
| 5 | 17th-19th |
| 6 | 18th-20th |
| 7 | 19th-21st |
| 8 | 20th-22nd |
| 9 | 21st-23rd |
| Buenos contribuyentes | Last date in range |

**Exact dates are published annually by SUNAT (Cronograma de Obligaciones Tributarias). Always verify the current year's calendar.**

### Late Filing Penalties [T1]

| Penalty | Calculation | Legislation |
|---------|-------------|-------------|
| Late filing | 1 UIT (Unidad Impositiva Tributaria) maximum, graduated | Codigo Tributario, Art. 176 |
| Late payment interest (TIM) | Tasa de Interes Moratorio: 0.9% monthly (SUNAT) or 0.5% (Aduanas) | Codigo Tributario, Art. 33 |
| Omission | 50% of omitted tax | Codigo Tributario, Art. 178 |
| Fraud | 100% of evaded tax (plus criminal) | Codigo Tributario, Art. 178 |
| Voluntary correction (regimen de gradualidad) | Reduced penalties: 95% reduction if corrected before SUNAT notification | RS 063-2007/SUNAT |

---

## Step 12: Registro de Compras y Ventas (Purchase and Sales Ledgers) [T1]

**Legislation:** TUO IGV, Art. 37; Reglamento, Art. 10; RS 234-2006/SUNAT.

### Requirements [T1]

| Ledger | Content | Notes |
|--------|---------|-------|
| Registro de Ventas e Ingresos | All sales documents issued | Monthly detail |
| Registro de Compras | All purchase documents received | Monthly detail; must show IGV separately |
| Electronic ledgers (PLE/SLE) | Mandatory for certain taxpayers | Submitted to SUNAT electronically |

### Timing for Credito Fiscal [T1]

| Rule | Detail | Legislation |
|------|--------|-------------|
| Standard | Must be registered in the period of the comprobante | TUO IGV, Art. 19 |
| Extended (Ley 29215) | Up to 12 months after issuance, provided registered in the period of annotation | Ley 29215, Art. 2 |
| SPOT condition | If subject to detracciones, deposit must be made before PDT 621 deadline | DS 155-2004-EF |

---

## Step 13: Bancarizacion (Banking Requirement) [T1]

**Legislation:** Ley 28194 (Ley para la Lucha contra la Evasion y para la Formalizacion de la Economia); DS 150-2007-EF.

### Rules [T1]

| Threshold | Requirement | Consequence of Non-Compliance |
|-----------|-------------|-------------------------------|
| > S/ 2,000 or > USD 500 | Payment must be made through the financial system (bank transfer, check, direct debit, etc.) | Loss of credito fiscal; expense not deductible for income tax |
| Cash payments above threshold | NOT allowed for tax purposes | Credito fiscal denied; cost/expense non-deductible |

### Accepted Payment Methods [T1]

| Method | Valid |
|--------|-------|
| Bank transfer (transferencia bancaria) | Yes |
| Certified check (cheque) | Yes (must meet requirements -- "no negociable") |
| Direct debit (cargo en cuenta) | Yes |
| Credit/debit card | Yes |
| Electronic wallet | Yes (regulated) |
| Cash (above threshold) | NO |

---

## Step 14: Key Thresholds [T1]

| Threshold | Value | Notes |
|-----------|-------|-------|
| UIT (Unidad Impositiva Tributaria) 2025 | S/ 5,350 | Updated annually by DS |
| UIT 2026 | Check current MEF decree | Updated annually |
| IGV/IPM split (2026) | 15.5% IGV + 2.5% IPM = 18% | Ley 32387 gradual shift |
| Bancarizacion threshold | S/ 2,000 or USD 500 | Above this: must use banking system |
| Retention threshold (retenciones) | S/ 700 per payment | Below this: no retention |
| SPOT minimum (most categories) | S/ 700 or as specified | Varies by category |
| Perception rate (general imports) | 3.5% | Standard rate |
| TIM (interest rate) | 0.9% monthly (SUNAT) | Late payment |
| Statute of limitations | 4 years (standard); 6 years (non-filers); 10 years (no RUC) | Codigo Tributario |

---

## Step 15: Tax Regimes Summary [T1]

| Regime | Income Limit | IGV Obligation | Income Tax | Ledgers |
|--------|-------------|----------------|------------|---------|
| NRUS (Nuevo RUS) | S/ 96,000 annual | NO IGV return; fixed monthly quota | Fixed quota | None (vouchers only) |
| RER (Regimen Especial) | S/ 525,000 annual | Monthly PDT 621 | 1.5% of net income | Registro de Compras y Ventas |
| RMT (Regimen MYPE) | 1,700 UIT annual | Monthly PDT 621 | Progressive 10%/29.5% | Full or simplified ledgers |
| Regimen General | No limit | Monthly PDT 621 | 29.5% | Full accounting |

### IGV Impact by Regime [T1]

| Regime | Charges IGV | Claims Credito Fiscal | Files PDT 621 |
|--------|-------------|----------------------|----------------|
| NRUS | No | No | No (cuota fija) |
| RER | Yes | Yes | Yes |
| RMT | Yes | Yes | Yes |
| Regimen General | Yes | Yes | Yes |

---

## Step 16: Reviewer Escalation Protocol

When a [T2] situation is identified, output:

```
REVIEWER FLAG
Tier: T2
Transaction: [description]
Issue: [what is ambiguous]
Options: [list the possible treatments]
Recommended: [which treatment is most likely correct and why]
Action Required: Licensed Contador Publico Colegiado must confirm before filing.
```

When a [T3] situation is identified, output:

```
ESCALATION REQUIRED
Tier: T3
Transaction: [description]
Issue: [what is outside skill scope]
Action Required: Do not classify. Refer to licensed Contador Publico Colegiado. Document gap.
```

---

## Step 17: Edge Case Registry

### EC1 -- Purchase with Boleta de Venta (no credito fiscal) [T1]
**Situation:** Employee buys office supplies and receives only a Boleta de Venta.
**Resolution:** No credito fiscal. Boletas de Venta do not give right to credito fiscal. The full amount (including IGV) is the expense. To claim credito fiscal, a Factura must be requested.
**Legislation:** TUO IGV, Art. 19.

### EC2 -- Service subject to detracciones, deposit not yet made [T1]
**Situation:** Client receives a service invoice subject to 12% SPOT. The detraccion deposit has not been made before the PDT 621 filing deadline.
**Resolution:** Credito fiscal CANNOT be claimed in this period. Once the deposit is made, credito fiscal can be claimed in the period of deposit. File PDT 621 without the credito fiscal for this invoice.
**Legislation:** DS 155-2004-EF; TUO IGV, Art. 19.

### EC3 -- Software subscription from US provider (reverse charge) [T1]
**Situation:** Monthly charge from a US company for cloud services.
**Resolution:** Reverse charge applies (utilizacion de servicios). Client self-assesses IGV at 18% on the service value. Pay via Formulario 1662 within the month. Report as output IGV and simultaneously claim as credito fiscal on PDT 621. Net zero for fully taxable businesses.
**Legislation:** TUO IGV, Art. 1(b); Art. 21.

### EC4 -- Supplier with RUC "No Habido" [T1]
**Situation:** Invoice received from a supplier whose RUC status is "No Habido" (unlocated) on SUNAT.
**Resolution:** Credito fiscal is NOT valid. Even if the invoice is otherwise correct, purchases from "No Habido" suppliers do not generate credito fiscal. The IGV becomes part of the expense cost.
**Legislation:** TUO IGV, Art. 19, inciso (a).

### EC5 -- Cash payment above S/ 2,000 (bancarizacion violation) [T1]
**Situation:** Client pays a supplier S/ 3,000 in cash for an invoice with IGV S/ 540.
**Resolution:** Credito fiscal DENIED. Payment above S/ 2,000 must be through the banking system. Additionally, the expense is non-deductible for income tax purposes.
**Legislation:** Ley 28194; DS 150-2007-EF.

### EC6 -- Export of services (Appendix V) [T1]
**Situation:** Peruvian company provides software development services to a US client. Service is listed in Appendix V.
**Resolution:** Zero-rated under Art. 33. No IGV charged. Credito fiscal on related costs IS recoverable via Saldo a Favor del Exportador (SFE). Claim NCN or offset against Income Tax.
**Legislation:** TUO IGV, Art. 33; Art. 34-35.

### EC7 -- Credit note reducing a previous sale [T1]
**Situation:** Client issues Nota de Credito for returned goods.
**Resolution:** Reduce debito fiscal by the IGV amount on the Nota de Credito. The NC must reference the original Factura and comply with comprobante de pago requirements. Report on PDT 621 as adjustment to sales.
**Legislation:** TUO IGV, Art. 26.

### EC8 -- Retention suffered by supplier [T1]
**Situation:** Client (supplier) receives payment from an Agente de Retencion. Buyer retained 3% of total invoice.
**Resolution:** Client reports the retained amount as credit on PDT 621 (retenciones sufridas). If retentions exceed IGV payable for 3 consecutive months, client can request refund.
**Legislation:** RS 037-2002/SUNAT.

### EC9 -- Perception on import [T1]
**Situation:** Client imports goods. SUNAT Aduanas charges 3.5% perception on top of IGV.
**Resolution:** Both the IGV and the perception are credits. IGV goes to credito fiscal (imports section). Perception goes to percepciones section. Both reduce IGV payable on PDT 621.
**Legislation:** RS 203-2003/SUNAT.

### EC10 -- Invoice from NRUS supplier [T1]
**Situation:** Client purchases from an NRUS (Nuevo RUS) registered supplier. Receives a Boleta de Venta.
**Resolution:** No credito fiscal. NRUS suppliers do not charge IGV and issue only Boletas. The full amount is the expense cost. No IGV entry on PDT 621.
**Legislation:** DL 937 (NRUS).

---

## Step 18: Penalties and Interest Summary [T1]

**Legislation:** Codigo Tributario, Libro Cuarto.

| Infraction | Penalty | Gradualidad |
|------------|---------|-------------|
| Late filing (Art. 176) | Up to 1 UIT | 90% reduction if voluntary correction |
| Late payment | TIM 0.9% monthly on unpaid amount | N/A |
| Omission of income (Art. 178-1) | 50% of omitted tax | 95% reduction if corrected voluntarily before notification |
| Fraud (Art. 178-1 with dolo) | 100% of evaded tax | No reduction |
| Failure to withhold/perceive/deposit SPOT | 50% of non-deposited amount | Graduated reductions available |
| Not keeping ledgers | Up to 0.6% of net income | Graduated |
| Not issuing comprobante de pago | Closure of establishment (3-10 days) | First offense: 1 day |

---

## Step 19: Test Suite

### Test 1 -- Standard local sale at 18%
**Input:** Peruvian company sells consulting services to local business, base S/ 10,000, IGV S/ 1,800. Factura issued.
**Expected output:** PDT 621, ventas gravadas += S/ 10,000, IGV debito fiscal += S/ 1,800.

### Test 2 -- Purchase with valid Factura, operating expense
**Input:** Company buys office supplies from local supplier, base S/ 1,000, IGV S/ 180. Valid Factura. Supplier RUC is "Habido." Payment via bank transfer.
**Expected output:** PDT 621, compras gravadas += S/ 1,000, IGV credito fiscal += S/ 180.

### Test 3 -- Purchase with Boleta only (no credito fiscal)
**Input:** Employee buys cleaning supplies S/ 500 total. Only Boleta de Venta obtained.
**Expected output:** No credito fiscal. Full S/ 500 is operating expense. No IGV entry on PDT 621.

### Test 4 -- Service subject to detracciones (SPOT)
**Input:** Company receives legal services invoice: base S/ 5,000, IGV S/ 900, total S/ 5,900. Service subject to 10% SPOT. Detraccion deposited = S/ 590 (10% of S/ 5,900).
**Expected output:** PDT 621, compras gravadas += S/ 5,000, IGV credito fiscal += S/ 900 (only if detraccion deposit made before filing deadline). Detracciones depositadas += S/ 590.

### Test 5 -- Export of goods
**Input:** Company exports goods, FOB value USD 10,000. Customs export declaration filed.
**Expected output:** PDT 621, exportaciones += S/ equivalent. No IGV charged. SFE mechanism for credito fiscal recovery.

### Test 6 -- Import of goods
**Input:** Company imports machinery: CIF S/ 50,000, duty S/ 5,000, IGV = 18% of S/ 55,000 = S/ 9,900. Perception 3.5% = S/ 2,272.
**Expected output:** PDT 621, IGV credito fiscal (imports) += S/ 9,900. Percepciones += S/ 2,272.

### Test 7 -- Import of services (reverse charge)
**Input:** Company pays USD 3,000 (S/ 11,100) for foreign consulting services.
**Expected output:** Self-assess IGV: S/ 11,100 * 18% = S/ 1,998. Report as output IGV AND input IGV. Net zero. Pay via Formulario 1662.

### Test 8 -- Cash payment above bancarizacion threshold
**Input:** Company pays supplier S/ 5,000 cash for services. Invoice shows IGV S/ 900.
**Expected output:** Credito fiscal DENIED (S/ 5,000 > S/ 2,000 threshold, cash payment). IGV of S/ 900 becomes part of expense cost. Expense also non-deductible for income tax.

---

## PROHIBITIONS [T1]

- NEVER allow credito fiscal on Boleta de Venta purchases
- NEVER allow credito fiscal when supplier RUC is "No Habido"
- NEVER allow credito fiscal when bancarizacion requirements are violated (cash > S/ 2,000)
- NEVER allow credito fiscal on SPOT-subject purchases if detraccion deposit was not made before the filing deadline
- NEVER confuse IGV (16%) and IPM (2%) -- always apply the combined 18% rate
- NEVER file IGV returns for NRUS clients (they pay fixed cuota)
- NEVER omit reverse charge on imported services (utilizacion de servicios)
- NEVER ignore the prorrata requirement when client has mixed taxable/exempt income
- NEVER accept invoices without valid comprobante de pago format
- NEVER compute any number -- all arithmetic is handled by the deterministic engine, not the AI

---

## Step 20: Reporting Obligations Summary [T1]

| Form | Description | Frequency | Deadline |
|------|-------------|-----------|----------|
| PDT 621 / Declara Facil 621 | Declaracion Mensual IGV-Renta | Monthly | Per RUC cronograma |
| PDT 626 | Declaracion de Retenciones de IGV (agentes de retencion) | Monthly | Per cronograma |
| PDT 697 | Percepciones a las Ventas Internas | Monthly | Per cronograma |
| PLE / SLE | Libros Electronicos (Registro de Compras y Ventas) | Monthly | Per cronograma |
| Formulario 1662 | Guia de Pagos Varios (IGV por utilizacion de servicios) | Per transaction | Month of annotation |
| DAOT | Declaracion Anual de Operaciones con Terceros | Annual | Per SUNAT resolution |
| Comprobantes de Pago Electronicos | Electronic invoicing (Factura, Boleta, NC, ND) | Continuous | Each transaction |

### Electronic Ledgers (Libros Electronicos) [T1]

| System | Who Must Use | Detail |
|--------|-------------|--------|
| PLE (Programa de Libros Electronicos) | Income > 75 UIT | Upload XML files to SUNAT monthly |
| SLE-Portal (Sistema de Libros Electronicos Portal) | Income < 75 UIT (optional) | Fill directly on SUNAT portal |
| Physical books | Certain small taxpayers | Paper ledgers (legalized by notary) |

### Key Ledgers for IGV [T1]

| Ledger | Content | Impact on IGV |
|--------|---------|---------------|
| Registro de Compras | All purchase documents received | Determines credito fiscal |
| Registro de Ventas e Ingresos | All sales documents issued | Determines debito fiscal |
| Libro Diario | Journal entries | General accounting |
| Libro Mayor | General ledger | General accounting |

---

## Contribution Notes (For Adaptation to Other Jurisdictions)

If you are adapting this skill for another country, you must:

1. Replace all legislation references with the equivalent national legislation.
2. Replace all PDT 621 sections with the equivalent sections on your jurisdiction's VAT/IGV return form.
3. Replace the 18% composite rate with your jurisdiction's rates.
4. Replace the SPOT/detracciones system with your jurisdiction's equivalent anti-evasion mechanisms.
5. Replace the retenciones/percepciones rules with your jurisdiction's equivalent.
6. Replace the bancarizacion thresholds with your jurisdiction's equivalent cash-payment restrictions.
7. Replace the electronic invoicing requirements with your jurisdiction's e-invoicing rules.
8. Have a licensed accountant in your jurisdiction validate every T1 rule before publishing.
9. Add your own edge cases to the Edge Case Registry for known ambiguous situations in your jurisdiction.
10. Run all test suite cases against your jurisdiction's rules and replace expected outputs accordingly.

**A skill may not be published without sign-off from a licensed practitioner in the relevant jurisdiction.**


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

If you would like a licensed accountant to review your return, visit [openaccountants.com](https://openaccountants.com) and log in to request a professional review.
