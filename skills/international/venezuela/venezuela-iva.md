---
name: venezuela-iva
description: Use this skill whenever asked to prepare, review, or create a Venezuela IVA (Impuesto al Valor Agregado) return for any client. Trigger on phrases like "prepare IVA return", "do the IVA", "Venezuela VAT", "SENIAT IVA", "Forma 30", "debito fiscal", "credito fiscal", "Contribuyente Especial", or any request involving Venezuela value added tax filing. CRITICAL -- Venezuela's economic instability means rates and thresholds change frequently; ALWAYS verify current rates before filing. ALWAYS read this skill before touching any Venezuela IVA work.
version: 2.0
jurisdiction: VE
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Jose Padilla
review_status: current
depends_on: - vat-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Venezuela IVA

## Venezuela IVA Return -- Self-Employed Skill v2.0

## Verified rates & thresholds (accountant-reviewed)

Reviewed against the cited tax authorities by **Jose Padilla** on 2026-06-21.
Items flagged for further clarification are tracked separately and excluded here.
This block is generated from verified `skill_facts` — edit the facts, not the prose.

### venezuela-iva

- **Alícuota general** — 16%  _(Ley del IVA Articles 27, 61, 62)_
- **Alícuota reducida (ciertos alimentos y bienes de primera necesidad)** — 8%  _(Ley del IVA Articles 27, 61, 62)_
- **Alícuota adicional por lujo (sobre la alícuota general)** — Hasta 15%  _(Ley del IVA Articles 27, 61, 62)_
- **Tasa combinada máxima (alícuota general + alícuota adicional por lujo)** — Hasta 31%  _(Ley del IVA)_
- **Alícuota para exportaciones** — 0%  _(Ley del IVA)_
- **Bienes y servicios exentos — Alimentos básicos, medicamentos, insumos agrícolas, libros, combustible, salud, educación, arrendamiento residencial, transporte público** — Exento (0% / sin IVA)  _(Ley del IVA Article 18; Ley del IVA Article 19)_
- **Frecuencia de declaración — Contribuyente Ordinario** — Mensual  _(Ley del IVA)_
- **Base para la fecha límite de declaración** — Calendario publicado por el SENIAT según el último dígito del RIF  _(Providencias SENIAT)_
- **Formulario de declaración** — Forma 30  _(Ley del IVA)_
- **Retención de Contribuyente Especial — fecha límite de declaración del período quincenal del 1 al 15** — Declarado a más tardar el día 20 del mismo mes  _(Providencia SNAT 2005-0056)_
- **Retención de Contribuyente Especial — fecha límite de declaración del período quincenal del 16 al fin de mes** — Declarado a más tardar el día 5 del mes siguiente  _(Providencia SNAT 2005-0056)_
- **Retención de Contribuyente Especial — compras a contribuyente ordinario con domicilio fiscal** — 75% del IVA  _(Providencia SNAT 2005-0056)_
- **Retención de Contribuyente Especial — compras a proveedor sin domicilio fiscal** — 100% del IVA  _(Providencia SNAT 2005-0056)_
- **Retención de Contribuyente Especial — entes gubernamentales** — 75% o 100% del IVA  _(Providencia SNAT 2005-0056)_
- **Vehículos automotores (de pasajeros) — crédito fiscal de IVA soportado** — BLOQUEADO — no credito fiscal  _(Ley del IVA Article 33)_
- **Entretenimiento — crédito fiscal de IVA soportado** — BLOQUEADO — no credito fiscal  _(Ley del IVA Article 33)_
- **Uso personal — crédito fiscal de IVA soportado** — BLOQUEADO — no crédito fiscal  _(Ley del IVA Article 33)_
- **Compras sin factura válida — crédito fiscal de IVA soportado** — BLOQUEADO — no crédito fiscal  _(Ley del IVA Article 33)_
- **Declaración extemporánea** — 5 UT to 50 UT per return  _(Ley del IVA)_
- **Pago extemporáneo** — 1% per month + monetary correction  _(Ley del IVA)_
- **Incumplimiento de la obligación de retener** — 100% to 300% of amount not withheld  _(Ley del IVA)_
- **Incumplimiento de la obligación de llevar Libros (libros de compras y ventas)** — 50 UT to 200 UT  _(Ley del IVA Article 56)_
- **Incumplimiento de la obligación de emitir factura** — Business closure 1–5 days  _(Ley del IVA Article 54)_
- **Fraude fiscal** — 100% to 300% of tax evaded + criminal prosecution  _(Ley del IVA)_
- **Unidad monetaria para umbrales y sanciones** — Unidades Tributarias (UT) — ajustadas periódicamente  _(Ley del IVA)_
- **Denominación monetaria vigente** — Bolívar Digital (introducido en 2021)
- **Tipo de cambio a utilizar en transacciones en moneda extranjera** — Tasa oficial del BCV en la fecha de la transacción
- **Fórmula de recuperación por prorrata** — % de Recuperación = Ventas Gravadas / Ventas Totales  _(Ley del IVA)_
- **Libro de Compras y Ventas — campos obligatorios** — RIF, base imponible, monto del IVA, total — por transacción; los totales resumen se trasladan a la Forma 30  _(Ley del IVA Article 56)_
- **Campos obligatorios de la factura fiscal** — RIF, fecha, descripción, base imponible, monto del IVA, total  _(Ley del IVA Article 54)_
- **Frecuencia de declaración de retenciones del Contribuyente Especial** — Quincenal  _(Providencia SNAT 2005-0056)_
- **Intereses bancarios (Intereses / Int Ganados)** — Exento — no gravable a efectos del IVA  _(Ley del IVA Article 19)_
- **Tasa aplicable al momento del hecho imponible cuando la tasa cambia en el transcurso del período** — La tasa vigente al momento del hecho imponible  _(Ley del IVA)_
- **Retención CE — Providencia rectora** — Providencia SNAT 2005-0056  _(Providencia SNAT 2005-0056)_
- **Artículos de la legislación sobre alícuotas del IVA** — Ley del IVA Articles 27, 61, 62  _(Ley del IVA Articles 27, 61, 62)_
- **Artículo de la legislación sobre bienes exentos** — Ley del IVA Article 18  _(Ley del IVA Article 18)_
- **Artículo de la legislación sobre servicios exentos** — Ley del IVA Article 19  _(Ley del IVA Article 19)_
- **Artículo de la legislación sobre créditos fiscales bloqueados del IVA** — Ley del IVA Article 33  _(Ley del IVA Article 33)_
- **Artículo de la legislación sobre facturas fiscales** — Ley del IVA Article 54  _(Ley del IVA Article 54)_
- **Artículo de la legislación sobre libros contables** — Ley del IVA Article 56  _(Ley del IVA Article 56)_

## Section 1 -- Quick Reference

**Quick Reference Table**

| Field | Value |
| --- | --- |
| Country | Venezuela (Republica Bolivariana de Venezuela) |
| Tax | IVA (Impuesto al Valor Agregado) |
| Currency | Bolivares (Bs.) -- current denomination: Bolivar Digital (2021) |
| Standard rate | 16% (VERIFY -- rate has changed multiple times) |
| Reduced rate | 8% (certain food/essential goods, when enacted) |
| Additional luxury rate | Up to 15% on luxury goods (on top of standard) |
| Primary legislation | Ley de Impuesto al Valor Agregado (multiple reforms) |
| Supporting legislation | Reglamento de la Ley del IVA; Providencias SENIAT |
| Tax authority | SENIAT |
| Filing portal | http://www.seniat.gob.ve (Portal Fiscal) |
| Filing frequency | Monthly (Contribuyente Ordinario) |
| Filing deadline | Calendar published by SENIAT based on last digit of RIF |
| Contributor | Open Accountants Community |
| Validated by | Verified by Jose Padilla (CPA) on 2026-06-21 |
| Skill version | 2.0 |

### CRITICAL WARNING

Venezuela's economic and regulatory environment is highly volatile. The IVA rate (currently stated as 16%), currency denomination, exchange rates, and filing systems may change without notice. Flag for reviewer on EVERY filing: confirm current IVA rate, currency denomination, and SENIAT system availability.

### Rate Table (VERIFY BEFORE EACH FILING)

**Rate Table**

| Rate | Application |
| --- | --- |
| 16% | Standard rate (alicuota general) -- VERIFY |
| 8% | Reduced rate on certain essentials (when enacted) |
| Up to 15% additional | Luxury goods (Alicuota Adicional) -- on top of standard |
| 0% | Exports |
| Exempt | Basic food, medicines, agricultural inputs, books, fuel, health, education, residential rent, public transport |

### Key Thresholds

**Key Thresholds Table**

| Item | Value |
| --- | --- |
| Contribuyente Ordinario | All persons making habitual taxable sales above threshold |
| Contribuyente Formal | Small taxpayers -- simplified obligations |
| Contribuyente Especial | Designated by SENIAT -- special withholding agent |
| Thresholds expressed in | Unidades Tributarias (UT) -- adjusted periodically |

### Conservative Defaults

**Conservative Defaults Table**

| Ambiguity | Default |
| --- | --- |
| IVA rate unknown | STOP -- verify current rate before proceeding |
| Currency denomination unknown | STOP -- verify current Bolivar denomination |
| Contribuyente type unknown | Contribuyente Ordinario (monthly filing) |
| Exchange rate for foreign currency | Official BCV rate on date of transaction |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable:** Bank statement for the month, RIF number, confirmation of Contribuyente type, and VERIFIED current IVA rate.

**Recommended:** Sales and purchase Libros (ledgers), fiscal invoices, prior period Forma 30.

**Ideal:** Complete Libro de Compras y Ventas, Contribuyente Especial withholding documentation, BCV exchange rate records.

### Refusal Catalogue

- **R-VE-1 -- Rate not verified.** — The current IVA rate has NOT been verified against the latest Gaceta Oficial. Do not proceed until rate is confirmed.
- **R-VE-2 -- Hyperinflation accounting.** — Hyperinflation adjustments and their interaction with IVA are complex. Escalate to specialist.
- **R-VE-3 -- Currency controls.** — Foreign currency transactions involving IGTF interaction require specialist review. IGTF is separate from IVA.
- **R-VE-4 -- Oil and gas sector.** — Hydrocarbon sector transactions require specialist knowledge. Escalate.

## Section 3 -- Transaction Pattern Library

### 3.1 Income Patterns (Credits)

**Income Patterns Table**

| Pattern | Tax Line | Treatment | Notes |
| --- | --- | --- | --- |
| TRANSFERENCIA [client] / TRF DESDE | Taxable supply | Output IVA at current rate | Wire transfer |
| DEPOSITO EFECTIVO / CASH DEPOSIT | Taxable supply | Revenue | Cash receipt |
| PAGO MOVIL / BIOPAGO | Taxable supply | Revenue | Mobile payment |
| ZELLE / PAYPAL VE | Taxable supply | Revenue | Digital payment -- may trigger IGTF |
| PUNTO DE VENTA / POS | Taxable supply | Revenue | Point of sale |
| MERCADOPAGO VE | Taxable supply | Revenue | MercadoPago settlement |
| INTERESES / INT GANADOS | Exempt | NOT taxable | Bank interest |
| PRESTAMO / CREDITO | EXCLUDE | Not income | Loan proceeds |

### 3.2 Expense Patterns (Debits)

**Expense Patterns Table**

| Pattern | Expense Category | Treatment | Notes |
| --- | --- | --- | --- |
| ALQUILER / ARRENDAMIENTO | Rent | Input IVA at current rate | Business premises |
| CORPOELEC / ELECTRICIDAD | Utilities | Input IVA | Commercial electricity |
| CANTV / MOVILNET / MOVISTAR / DIGITEL | Communications | Business portion | Mixed use: apportion |
| AUTOMOVIL / VEHICULO | Vehicle | BLOCKED | No input credit |
| RESTAURANT / CENA / BANQUETE | Entertainment | BLOCKED | No input credit |
| SENIAT PAGO / IMPUESTO | EXCLUDE | Tax payment | Not deductible |
| IVSS / SEGURO SOCIAL / FAOV / BANAVIH | EXCLUDE | Social security | Not IVA |
| IGTF PAGO | EXCLUDE | Financial transactions tax | Separate from IVA |
| RETIRO PERSONAL | EXCLUDE | Drawings | Not business |

### 3.3 Exempt Supply Indicators

**Exempt Supply Indicators Table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ARROZ / HARINA / PAN / CARNE / LECHE | Exempt | Basic food |
| FARMACIA / MEDICINA | Exempt | Pharmaceutical |
| COLEGIO / UNIVERSIDAD | Exempt | Education |
| CONSULTA MEDICA / HOSPITAL | Exempt | Health services |
| GASOLINA / DIESEL | Exempt | Fuel (regulated) |

## Section 4 -- Worked Examples

### Example 1 -- Standard Local Purchase at 16%

**Input:** VE supplier, office supplies, gross Bs. 11,600, IVA Bs. 1,600, net Bs. 10,000. Valid factura.

**Reasoning:** Standard-rated purchase. Valid fiscal invoice. Full credito fiscal.

**Classification:** Line 8 = Bs. 1,600 credito fiscal. Full recovery. (Verify rate at time of transaction.)

### Example 2 -- Contribuyente Especial Withholding

**Input:** Contribuyente Especial purchases services from ordinary taxpayer. Invoice: Bs. 10,000 + IVA Bs. 1,600. Withhold 75%.

**Reasoning:** Withhold 75% of IVA = Bs. 1,200. Pay supplier Bs. 10,400 (10,000 + 400 remaining IVA). File bi-weekly withholding return. Issue comprobante de retencion. Supplier claims Bs. 1,200 on Line 16.

**Classification:** Withholding Bs. 1,200. Supplier claims on Line 16.

### Example 3 -- Imported Services (Reverse Charge)

**Input:** US consulting, USD 1,000 at BCV rate 36.60 = Bs. 36,600. No IVA charged.

**Reasoning:** Self-assess debito fiscal at current rate: Bs. 5,856 (16%). Credito fiscal: Bs. 5,856. Net = zero.

**Classification:** Output IVA Bs. 5,856. Input IVA Bs. 5,856. Net zero.

### Example 4 -- Motor Vehicle (Blocked)

**Input:** Purchase sedan Bs. 200,000, IVA Bs. 32,000.

**Reasoning:** Passenger vehicles are blocked under Article 33. No credito fiscal.

**Classification:** IVA Bs. 32,000 BLOCKED.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Forma 30 Return Structure

**Forma 30 Return Structure Table**

| Line | Description |
| --- | --- |
| 1 | Ventas internas gravadas (domestic taxable sales) |
| 2 | Debito fiscal en ventas internas |
| 3 | Ventas de exportacion (exports, 0%) |
| 4 | Ventas internas no gravadas / exentas |
| 5 | Total ventas |
| 6 | Total debito fiscal |
| 7 | Compras internas gravadas |
| 8 | Credito fiscal en compras internas |
| 9 | Importaciones gravadas |
| 10 | Credito fiscal en importaciones |
| 11 | Total credito fiscal |
| 12 | Ajustes (blocked/proportional) |
| 13 | Credito fiscal neto |
| 14 | Diferencia (Line 6 - Line 13) |
| 15 | Excedente credito fiscal anterior |
| 16 | Retenciones de IVA (Contribuyentes Especiales) |
| 17 | Total a pagar / excedente |

### 5.2 Blocked Input IVA (Article 33)

- **Blocked input categories** — No credit: motor vehicles (passenger), entertainment, personal use, exempt operations, purchases without valid factura.  _(Ley del IVA Article 33)_

### 5.3 Contribuyente Especial Withholding (Providencia 2005-0056)

**CE Withholding Table**

| Scenario | Rate |
| --- | --- |
| Purchasing from ordinary taxpayer with fiscal domicile | 75% of IVA |
| Purchasing from supplier without fiscal domicile address | 100% of IVA |
| Government entities | 75% or 100% of IVA |

- **Bi-weekly filing deadlines** — Bi-weekly filing: 1st-15th filed by 20th; 16th-end filed by 5th of following month.  _(Providencia SNAT 2005-0056)_

### 5.4 Libro de Compras y Ventas (Article 56)

- **Libro de Compras y Ventas requirement** — All IVA taxpayers must maintain purchase and sales ledgers with RIF, base, IVA, total. Summary totals flow to Forma 30.  _(Ley del IVA Article 56)_

### 5.5 Fiscal Invoice Requirements (Article 54)

- **Fiscal invoice requirements** — Must include RIF, date, description, base imponible, IVA amount, total. Fiscal machines required for certain taxpayers.  _(Ley del IVA Article 54)_

### 5.6 Penalties

**Penalties Table**

| Violation | Penalty |
| --- | --- |
| Late filing | 5 UT to 50 UT per return |
| Late payment | 1% per month + monetary correction |
| Failure to withhold | 100% to 300% of amount not withheld |
| Failure to keep Libros | 50 UT to 200 UT |
| Failure to issue factura | Business closure (1-5 days) |
| Fraud | 100% to 300% of tax evaded + criminal prosecution |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Rate Change Mid-Period

- **Rate change mid-period** — If IVA rate changes during a filing period, apply the rate in effect at the time of the taxable event. A single period may have transactions at different rates. Flag for reviewer.

### 6.2 Luxury Goods Additional Rate

- **Luxury goods additional rate** — May be subject to standard rate + additional luxury rate (up to 31% total). Verify current gazette for product list. Flag for reviewer.

### 6.3 USD/Foreign Currency Transactions

- **USD/Foreign currency transactions** — Convert to Bolivares at BCV official rate on date of transaction. IGTF may also apply on foreign currency portion. IGTF is separate from IVA. Flag for reviewer.

### 6.4 Partial Exemption

- **Partial exemption recovery formula** — Direct attribution + proportional (prorrata). Recovery % = Taxable Sales / Total Sales. Flag for reviewer.

### 6.5 SENIAT Portal Downtime

- **SENIAT portal downtime** — Document system unavailability. File as soon as available. Penalties may be contested on force majeure. Flag for reviewer.

## Section 7 -- Working Paper Template

```
VENEZUELA IVA WORKING PAPER (FORMA 30)
Contribuyente: _______________  RIF: ___________
Periodo: ___________  Mes: ___________
IVA RATE VERIFIED: ____% (Date verified: _________)
Currency: Bs. (denomination: _________)

A. DEBITO FISCAL (OUTPUT)
  A1. Ventas internas gravadas (excl. IVA)       ___________
  A2. Debito fiscal                              ___________
  A3. Exportaciones (0%)                         ___________
  A4. Ventas exentas                             ___________

B. CREDITO FISCAL (INPUT)
  B1. Credito fiscal compras internas            ___________
  B2. Credito fiscal importaciones               ___________
  B3. Blocked (vehicles, entertainment)          ___________
  B4. Credito fiscal neto                        ___________

C. LIQUIDACION
  C1. Diferencia (A2 - B4)                      ___________
  C2. Excedente anterior                         ___________
  C3. Retenciones IVA                            ___________
  C4. Total a pagar / excedente                  ___________

REVIEWER FLAGS:
  [ ] Current IVA rate verified against Gaceta Oficial?
  [ ] Currency denomination confirmed?
  [ ] Contribuyente type confirmed?
  [ ] All fiscal invoices compliant?
  [ ] CE withholding documented?
  [ ] IGTF separated from IVA?
```

## Section 8 -- Bank Statement Reading Guide

### Venezuelan Bank Statement Formats

**Venezuelan Bank Statement Formats Table**

| Bank | Format | Key Fields |
| --- | --- | --- |
| Banco de Venezuela | PDF | Fecha, Descripcion, Debito, Credito, Saldo |
| Banesco | CSV / PDF | Fecha, Referencia, Descripcion, Monto, Saldo |
| Banco Mercantil | CSV | Fecha, Descripcion, Cargo, Abono, Saldo |
| Provincial (BBVA) | CSV | Fecha, Concepto, Debito, Credito, Saldo |
| Banco Nacional de Credito | PDF | Fecha, Detalle, Debito, Credito, Disponible |
| Banco del Tesoro | PDF | Fecha, Descripcion, Debe, Haber, Saldo |

### Key Venezuelan Banking Narrations

**Key Venezuelan Banking Narrations Table**

| Narration | Meaning | Classification Hint |
| --- | --- | --- |
| TRANSFERENCIA / TRF | Wire transfer | Income or expense |
| PAGO MOVIL | Mobile payment | Income or expense |
| PUNTO DE VENTA / POS | Card terminal | Income or expense |
| IGTF | Financial transactions tax | Exclude from IVA |
| SENIAT | Tax payment | Exclude |
| IVSS / BANAVIH / FAOV | Social security | Exclude |
| INTERESES | Interest | Exempt |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. STOP if current IVA rate is not verified
2. Classify all business credits as potential taxable supplies
3. Apply blocked rules to vehicles and entertainment
4. Separate IGTF from IVA
5. Flag all foreign currency transactions for BCV rate verification

Present these questions:

```
ONBOARDING QUESTIONS -- VENEZUELA IVA
1. What is your RIF?
2. Are you Contribuyente Ordinario, Formal, or Especial?
3. What is the CURRENT IVA rate in the latest Gaceta Oficial?
4. What types of goods or services do you sell?
5. Do you make any exempt supplies?
6. Are you a designated Contribuyente Especial (withholding agent)?
7. Do you have transactions in foreign currency (USD)?
8. Any excedente credito fiscal from prior period?
9. Do you sell any luxury goods subject to additional rate?
```

## Section 10 -- Reference Material

### Key Legislation

**Key Legislation Table**

| Topic | Reference |
| --- | --- |
| IVA imposition | Ley del IVA |
| Rates | Ley del IVA Articles 27, 61, 62 |
| Exempt goods | Ley del IVA Article 18 |
| Exempt services | Ley del IVA Article 19 |
| Blocked input | Ley del IVA Article 33 |
| Fiscal invoices | Ley del IVA Article 54 |
| Libros | Ley del IVA Article 56 |
| CE withholding | Providencia SNAT 2005-0056 |
| IGTF | Ley de IGTF (separate tax) |

### Known Gaps / Out of Scope

- Hyperinflation accounting interaction
- IGTF computation and returns
- Oil and gas sector
- Currency control mechanisms
- Rate changes (verify each filing)

### Changelog

**Changelog Table**

| Version | Date | Change |
| --- | --- | --- |
| 2.0 | April 2026 | Full rewrite to v2.0 structure; Venezuelan bank formats; local payment patterns; critical volatility warnings; CE withholding detail |
| 1.1 | April 2026 | Rates and thresholds re-verified |
| 1.0 | 2025 | Initial version |

### Self-Check

- [ ] Current IVA rate verified against latest Gaceta Oficial?
- [ ] Currency denomination confirmed (Bolivar Digital)?
- [ ] Contribuyente type confirmed?
- [ ] CE withholding documented and reconciled?
- [ ] IGTF clearly separated from IVA?
- [ ] All fiscal invoices compliant?
- [ ] BCV exchange rate used for foreign currency?

## PROHIBITIONS

- NEVER assume IVA rate without verification -- rates change frequently in Venezuela
- NEVER allow input credit on blocked categories (vehicles, entertainment, personal)
- NEVER allow input credit without valid factura
- NEVER confuse IVA with IGTF (they are separate taxes)
- NEVER use outdated currency denominations
- NEVER ignore Contribuyente Especial withholding obligations
- NEVER apply reverse charge to out-of-scope categories
- NEVER present calculations as definitive -- always label as estimated and direct client to a licensed Venezuelan Contador Publico Colegiado

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed Contador Publico Colegiado or equivalent practitioner in Venezuela) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
