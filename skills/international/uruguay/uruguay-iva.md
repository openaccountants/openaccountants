---
name: uruguay-iva
description: >
  Use this skill whenever asked to prepare, review, or create a Uruguay IVA (Impuesto al Valor Agregado) return for any client. Trigger on phrases like "prepare IVA return", "do the IVA", "Uruguay VAT", "DGI Uruguay", "tasa basica", "tasa minima", "CFE Uruguay", or any request involving Uruguay value added tax filing. Covers the 22% standard rate (tasa basica), 10% reduced rate (tasa minima), exempt supplies, monthly filing to DGI, input/output IVA computation, CFE electronic invoicing, and withholding/perception rules. ALWAYS read this skill before touching any Uruguay IVA work.
version: 2.0
jurisdiction: UY
tax_year: 2025
category: international
depends_on:
  - vat-workflow-base
---

# Uruguay IVA Return -- Self-Employed Skill v2.0

---

## Section 1 -- Quick Reference

| Field | Value |
|---|---|
| Country | Uruguay (Republica Oriental del Uruguay) |
| Tax | IVA (Impuesto al Valor Agregado) |
| Currency | UYU only |
| Standard rate (tasa basica) | 22% |
| Reduced rate (tasa minima) | 10% |
| Primary legislation | Titulo 10, Texto Ordenado 1996 (IVA); Ley 18.083 (Reforma Tributaria 2007) |
| Supporting legislation | Decreto 220/998 (Reglamento IVA); Resoluciones DGI |
| Tax authority | Direccion General Impositiva (DGI) |
| Filing portal | https://www.dgi.gub.uy (Servicios en Linea DGI) |
| Filing frequency | Monthly |
| Filing deadline | Based on last 2 digits of RUT (16th-27th of following month) |
| Contributor | Open Accountants Community |
| Validated by | Deep research verification, April 2026 |
| Skill version | 2.0 |

### Rate Table

| Rate | Application |
|---|---|
| 22% (tasa basica) | Standard rate on all taxable supplies not otherwise specified |
| 10% (tasa minima) | Basic food, medicines, hotel accommodation, first sale of residential real estate, newspapers, cleaning products, personal hygiene |
| 0% | Exports (full input credit recovery) |
| Exempt (exonerado) | Financial services, education, health, residential rental, public transport, cultural activities |

### Key Thresholds

| Item | Value |
|---|---|
| Mandatory IVA registration | All entities making taxable supplies (no minimum) |
| Monotributo | Small sole proprietors; substitutes IVA + IRAE + social security |
| Literal E | Small enterprise with simplified IVA treatment |
| CFE mandatory | Most taxpayers |

### Conservative Defaults

| Ambiguity | Default |
|---|---|
| Rate unknown on a sale | 22% (tasa basica) |
| Input credit without valid CFE | Not claimable |
| Blocked category (vehicle, entertainment) | No recovery |
| Export of services classification unknown | Taxable at 22% until IRAE source confirmed |

---

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the month in CSV, PDF, or pasted text, plus RUT and IVA taxpayer type.

**Recommended:** Sales and purchase CFEs, prior period return, credit balance brought forward.

**Ideal:** Complete Libro de Compras y Ventas, IRAE return context, free zone status confirmation.

### Refusal Catalogue

**R-UY-1 -- Monotributo taxpayers.** "Monotributo taxpayers pay a single substitute amount and do NOT charge IVA separately. Buyers cannot claim input IVA on Monotributo purchases. This skill does not prepare Monotributo returns."

**R-UY-2 -- Free Trade Zone entities.** "Zona Franca entities have special VAT exemptions that vary by user agreement. Escalate to a qualified contador publico."

**R-UY-3 -- IRAE-IVA interaction on service exports.** "Zero-rating on service exports requires IRAE source determination. Escalate."

**R-UY-4 -- Partial exemption complex.** "If mixed taxable/exempt supplies involve multiple apportionment methods, escalate."

---

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns (Credits)

| Pattern | Tax Line | Treatment | Notes |
|---|---|---|---|
| TRANSFERENCIA [client] / TRF DESDE | Taxable supply | Revenue at applicable rate | Wire transfer from client |
| DEPOSITO EFECTIVO | Taxable supply | Revenue | Cash deposit |
| PAGO ELECTRONICO / PAGOS ONLINE | Taxable supply | Revenue | Electronic payment receipt |
| MERCADOPAGO LIQUIDACION | Taxable supply | Revenue | MercadoPago settlement |
| PREX / MIDES / BPS PAGO | Verify | May be government payment | Check if business income |
| INTERESES / INT GANADOS | Exempt | NOT taxable | Bank interest |
| PRESTAMO / CREDITO BANCARIO | EXCLUDE | Not income | Loan proceeds |

### 3.2 Expense Patterns (Debits)

| Pattern | Expense Category | Treatment | Notes |
|---|---|---|---|
| ALQUILER OFICINA / ARRENDAMIENTO | Rent | Input IVA at 22% | Business premises |
| UTE / ELECTRICIDAD | Utilities | Input IVA at 22% | Electricity |
| OSE / AGUA | Utilities | Input IVA at 22% | Water |
| ANTEL / MOVISTAR / CLARO | Communications | Business portion claimable | Mixed use: apportion |
| UBER / TAXI / CABIFY | Travel | Input IVA if business | Keep receipts |
| AUTOMOVIL / VEHICULO / SEDAN | Vehicle | BLOCKED | No input credit on passenger vehicles |
| RESTAURANT / CENA / ALMUERZO | Entertainment | BLOCKED | No input credit |
| DGI PAGO / IMPUESTOS | EXCLUDE | Tax payment | Not deductible |
| BPS APORTE / SEGURO SOCIAL | EXCLUDE | Social security | Not IVA |
| RETIRO PERSONAL | EXCLUDE | Drawings | Not business |

### 3.3 Reduced Rate (10%) Indicators

| Pattern | Treatment | Notes |
|---|---|---|
| HOTEL / ALOJAMIENTO / HOSPEDAJE | Tasa minima 10% | Hotel accommodation |
| FARMACIA / MEDICAMENTO | Tasa minima 10% | Medicines |
| ARROZ / HARINA / CARNE / YERBA MATE | Tasa minima 10% | Basic food items |
| PERIODICO / DIARIO | Tasa minima 10% | Newspapers |

---

## Section 4 -- Worked Examples

### Example 1 -- Standard Local Purchase at 22%

**Input:** UY supplier, office equipment, gross UYU 12,200, IVA UYU 2,200, net UYU 10,000. Valid CFE (e-Factura).

**Reasoning:** Standard-rated purchase at tasa basica. Valid e-Factura held. Full input credit.

**Classification:** Input IVA UYU 2,200. Full recovery. Report on return Line 9.

### Example 2 -- Export (Zero-Rated)

**Input:** Exporter ships meat to Brazil, net UYU 500,000. Export documentation complete.

**Reasoning:** Export of goods is zero-rated. No output IVA. All input IVA on related purchases fully recoverable.

**Classification:** Report UYU 500,000 on Line 5. No output IVA. Input IVA fully recoverable.

### Example 3 -- Motor Vehicle Purchase (Blocked)

**Input:** Purchase sedan UYU 800,000, IVA UYU 176,000.

**Reasoning:** Passenger vehicles are a blocked category under Titulo 10, Article 21. No input credit regardless of business use.

**Classification:** IVA UYU 176,000 BLOCKED. No input credit.

### Example 4 -- Imported Services (Reverse Charge)

**Input:** US consulting firm, USD 3,000 (approx. UYU 120,000). No IVA charged.

**Reasoning:** Self-assess IVA at 22%: UYU 26,400 output. If for taxable operations, claim UYU 26,400 input. Net = zero.

**Classification:** Output IVA UYU 26,400. Input IVA UYU 26,400. Net zero.

---

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 IVA Return Form Structure (Formulario 2176/2178)

**Filed monthly via DGI Servicios en Linea.**

| Line | Description |
|---|---|
| 1 | Ventas gravadas a tasa basica (22%) |
| 2 | IVA devengado a tasa basica |
| 3 | Ventas gravadas a tasa minima (10%) |
| 4 | IVA devengado a tasa minima |
| 5 | Exportaciones (0%) |
| 6 | Ventas exoneradas |
| 7 | Total ventas |
| 8 | Total IVA devengado (Line 2 + Line 4) |
| 9 | IVA en compras gravadas a tasa basica |
| 10 | IVA en compras gravadas a tasa minima |
| 11 | IVA en importaciones |
| 12 | Total IVA deducible |
| 13 | Ajustes (blocked/proportional) |
| 14 | IVA deducible neto |
| 15 | IVA a pagar (Line 8 - Line 14) |
| 16 | Credito del periodo anterior |
| 17 | Retenciones/percepciones |
| 18 | Total a pagar / saldo a favor |

### 5.2 Blocked Input IVA (Titulo 10, Article 21)

No recovery: motor vehicles (passenger), entertainment/recreation, personal use, exempt operations, purchases without valid CFE.

### 5.3 IVA Withholding and Perception

| Agent Type | Rate |
|---|---|
| Government entities (Estado) | 100% of IVA on services, 60% on goods |
| Designated large taxpayers | Varies by DGI resolution |

### 5.4 Reverse Charge on Imported Services (Article 5)

Self-assess IVA at applicable rate. Report as output. Claim as input if for taxable operations.

### 5.5 Filing Deadlines

Based on last 2 digits of RUT: Group 1 (16th-19th), Group 2 (20th-23rd), Group 3 (24th-27th) of following month.

### 5.6 Penalties

| Violation | Penalty |
|---|---|
| Late filing | UYU multa (fine) determined by DGI |
| Late payment | Recargos: 5% first month + 2% per additional month |
| Interest | Rate set by Central Bank |
| Failure to issue CFE | Fines + potential closure |
| Fraud | Criminal penalties |

### 5.7 CFE Electronic Invoicing

| Document | Code | Supports IVA Credit |
|---|---|---|
| e-Factura | 111 | YES |
| e-Ticket | 101 | NO (for buyer) |
| e-Nota de Credito | 112 | YES (reduces IVA) |
| e-Nota de Debito | 113 | YES |
| e-Resguardo | 181 | N/A |
| e-Factura Exportacion | 121 | N/A |

---

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Partial Exemption

Direct attribution + proportional for common costs. Recovery % = Taxable Sales / Total Sales. Flag for reviewer.

### 6.2 Free Trade Zone Rules (Ley 15.921)

Zona Franca entities exempt from all national taxes including IVA. Sales from free zone to domestic market treated as imports. Flag for reviewer.

### 6.3 Agricultural Sector

Agricultural products in natural state (first sale by producer) may be exempt. Multiple overlapping taxes (IMEBA). Flag for reviewer.

### 6.4 Export of Services

Services consumed outside Uruguay may be zero-rated if IRAE treats them as foreign-source. Confirm IRAE source determination before applying zero-rating. Flag for reviewer.

### 6.5 Literal E (Small Enterprise)

Simplified IVA calculation based on sales volume. Confirm current thresholds and obligations. Flag for reviewer.

---

## Section 7 -- Working Paper Template

```
URUGUAY IVA WORKING PAPER
Contribuyente: _______________  RUT: ___________
Periodo: ___________  Mes: ___________

A. IVA DEVENGADO (OUTPUT)
  A1. Ventas tasa basica (22%) neto             ___________
  A2. IVA devengado tasa basica                 ___________
  A3. Ventas tasa minima (10%) neto             ___________
  A4. IVA devengado tasa minima                 ___________
  A5. Exportaciones (0%)                        ___________
  A6. Ventas exoneradas                         ___________
  A7. Total IVA devengado (A2 + A4)             ___________

B. IVA DEDUCIBLE (INPUT)
  B1. IVA compras tasa basica                   ___________
  B2. IVA compras tasa minima                   ___________
  B3. IVA importaciones                         ___________
  B4. Ajustes (blocked)                         ___________
  B5. IVA deducible neto                        ___________

C. LIQUIDACION
  C1. IVA a pagar (A7 - B5)                    ___________
  C2. Credito anterior                          ___________
  C3. Retenciones/percepciones                  ___________
  C4. Total a pagar / saldo a favor             ___________

REVIEWER FLAGS:
  [ ] RUT and taxpayer type confirmed?
  [ ] All input claims supported by valid CFE (e-Factura)?
  [ ] Blocked categories excluded (vehicles, entertainment)?
  [ ] Tasa basica vs tasa minima correctly applied?
  [ ] Export documentation complete for zero-rating?
```

---

## Section 8 -- Bank Statement Reading Guide

### Uruguayan Bank Statement Formats

| Bank | Format | Key Fields |
|---|---|---|
| BROU (Banco Republica) | CSV / PDF | Fecha, Concepto, Debito, Credito, Saldo |
| Santander Uruguay | CSV | Fecha, Descripcion, Debito, Credito, Saldo |
| Itau Uruguay | CSV | Fecha, Detalle, Debe, Haber, Saldo |
| BBVA Uruguay | CSV | Fecha, Concepto, Cargo, Abono, Saldo |
| Scotiabank Uruguay | CSV | Fecha, Descripcion, Retiro, Deposito, Saldo |
| Heritage (OCA) | CSV | Fecha, Descripcion, Monto, Saldo |

### Key Uruguayan Banking Narrations

| Narration | Meaning | Classification Hint |
|---|---|---|
| TRANSFERENCIA / TRF | Wire transfer | Potential income or expense |
| DEPOSITO | Cash deposit | Income |
| DEBITO AUTOMATICO | Direct debit | Regular expense |
| CHEQUE | Cheque payment | Income or expense |
| BPS | Social security | Exclude from IVA |
| DGI | Tax payment | Exclude |
| INTERESES | Interest | Exempt |

---

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all business-name credits as potential taxable supplies at 22%
2. Apply blocked category rules to vehicles and entertainment
3. Only claim input IVA where CFE documentation is confirmed
4. Flag all reduced-rate items for verification

Present these questions:

```
ONBOARDING QUESTIONS -- URUGUAY IVA
1. What is your RUT (Registro Unico Tributario)?
2. What is your IVA taxpayer type (Contribuyente IRAE, Unipersonal, Monotributo, Literal E)?
3. What types of goods or services do you sell?
4. Do you make any exempt supplies?
5. Do you export goods or services?
6. Are you in a Free Trade Zone (Zona Franca)?
7. Do you have valid CFEs (e-Facturas) for all purchase claims?
8. Any credit balance brought forward from prior period?
```

---

## Section 10 -- Reference Material

### Key Legislation

| Topic | Reference |
|---|---|
| IVA imposition | Titulo 10, Texto Ordenado 1996 |
| Rates | Titulo 10, Articles 18-20 |
| Exempt supplies | Titulo 10, Articles 19-20; Decreto 220/998 |
| Blocked input | Titulo 10, Article 21 |
| Reverse charge | Titulo 10, Article 5 |
| CFE system | DGI Resoluciones; Decreto 36/012 |
| Free Trade Zones | Ley 15.921 |
| Reforma Tributaria | Ley 18.083 (2007) |

### Known Gaps / Out of Scope

- Monotributo returns
- Free Trade Zone complex arrangements
- IRAE-IVA interaction on service exports
- IMEBA (agricultural tax)
- Complex partial exemption

### Changelog

| Version | Date | Change |
|---|---|---|
| 2.0 | April 2026 | Full rewrite to v2.0 structure; Uruguayan bank formats; local payment patterns; worked examples; CFE integration |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] RUT and taxpayer type confirmed?
- [ ] Tasa basica (22%) vs tasa minima (10%) correctly applied?
- [ ] All input claims supported by valid CFE (e-Factura, not e-Ticket)?
- [ ] Blocked categories excluded?
- [ ] Export documentation complete?
- [ ] Filing deadline based on RUT last digits?

---

## PROHIBITIONS

- NEVER allow input credit on blocked categories (vehicles, entertainment, personal use)
- NEVER allow input credit without valid CFE (e-Factura)
- NEVER confuse tasa basica (22%) with tasa minima (10%)
- NEVER confuse zero-rated exports with exempt supplies
- NEVER apply reverse charge to out-of-scope categories
- NEVER prepare returns for Monotributo taxpayers using this skill
- NEVER zero-rate service exports without IRAE source confirmation
- NEVER present calculations as definitive -- always label as estimated and direct client to a qualified Uruguayan contador publico

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador publico or equivalent licensed practitioner in Uruguay) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
