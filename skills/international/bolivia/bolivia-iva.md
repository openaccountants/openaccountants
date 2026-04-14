---
name: bolivia-iva
description: Use this skill whenever asked to prepare, review, or classify transactions for a Bolivia IVA (Impuesto al Valor Agregado) return for any client. Trigger on phrases like "Bolivia IVA", "Bolivia VAT", "SIN filing", "factura", or any request involving Bolivia IVA. MUST be loaded alongside vat-workflow-base v0.1 or later. ALWAYS read this skill before touching any Bolivia IVA work.
version: 2.0
---

# Bolivia IVA Return Skill v2.0

## Section 1 — Quick reference

| Field | Value |
|---|---|
| Country | Bolivia (Estado Plurinacional de Bolivia) |
| Standard rate | 13% (IVA — embedded in price, not added on top) |
| IT rate | 3% (Impuesto a las Transacciones — applies alongside IVA) |
| Zero rate | 0% (exports) |
| Exempt | Basic food basket, education, financial services (limited) |
| Return form | Monthly IVA return (Form 200) via Newton portal |
| Filing portal | https://newton.impuestos.gob.bo (SIAT/Newton) |
| Authority | Servicio de Impuestos Nacionales (SIN) |
| Currency | BOB (Boliviano) |
| Filing frequency | Monthly |
| Deadline | Based on last digit of NIT (staggered: 13th-22nd of following month) |
| Companion skill | vat-workflow-base v0.1 or later — MUST be loaded |
| Validated by | Pending — requires licensed Bolivian tax practitioner |

**CRITICAL: Bolivia IVA is embedded in the price (not added on top).** The 13% is already included in the selling price. Credito fiscal (input tax credit) requires a factura (official invoice) from SIN-authorized billing system.

**Conservative defaults:**

| Ambiguity | Default |
|---|---|
| Unknown rate on a sale | 13% IVA (embedded) |
| Unknown input credit status | Not creditable (no factura assumed) |
| Unknown counterparty location | Domestic Bolivia |

---

## Section 2 — Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — bank statement for the month. Acceptable from: BNB (Banco Nacional de Bolivia), Banco Mercantil Santa Cruz, Banco Union, BancoSol, Banco BISA, Banco FIE, or any other.

### Bolivia-specific refusal catalogue

**R-BO-1 — Regimen simplificado.** Trigger: client on simplified tax regime. Message: "Simplified regime taxpayers have different filing obligations. Please escalate."

**R-BO-2 — Hydrocarbon sector.** Trigger: oil/gas operations. Message: "Hydrocarbon sector has bespoke tax treatment including IDH. Please escalate."

**R-BO-3 — Mining sector.** Trigger: mining operations with IUE/ICM. Message: "Mining has special indirect tax rules. Please escalate."

---

## Section 3 — Supplier pattern library

### 3.1 Bolivian banks (fees — exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| BNB, BANCO NACIONAL DE BOLIVIA | EXCLUDE for bank charges | Financial service |
| BANCO MERCANTIL, BMSC | EXCLUDE | Same |
| BANCO UNION, BANCOSOL | EXCLUDE | Same |
| BANCO BISA, BANCO FIE | EXCLUDE | Same |
| INTEREST, INTERES, PRESTAMO | EXCLUDE | Out of scope |

### 3.2 Government (exclude)

| Pattern | Treatment | Notes |
|---|---|---|
| SIN, IMPUESTOS NACIONALES | EXCLUDE | Tax payment |
| ADUANA, CUSTOMS | EXCLUDE | Duty |
| AFP, PENSION | EXCLUDE | Pension |
| CNS, CAJA NACIONAL DE SALUD | EXCLUDE | Social security |

### 3.3 Utilities

| Pattern | Treatment | Notes |
|---|---|---|
| ENDE, ELECTROPAZ, ELFEC, CRE | Domestic 13% | Electricity |
| EPSAS, SAGUAPAC | Domestic 13% | Water |
| ENTEL, TIGO BO, VIVA BO | Domestic 13% | Telecoms |

### 3.4 SaaS and international services

| Pattern | Treatment | Notes |
|---|---|---|
| GOOGLE, MICROSOFT, META, AWS | Self-assess 13% IVA | Non-resident |
| ZOOM, SLACK, CANVA | Self-assess 13% | Same |

### 3.5 Payroll and exclusions

| Pattern | Treatment | Notes |
|---|---|---|
| SALARIO, SUELDO, WAGES | EXCLUDE | Outside IVA scope |
| TRANSFERENCIA PROPIA, INTERNAL | EXCLUDE | Internal |
| RETIRO, ATM | TIER 2 — ask | Default exclude |

---

## Section 4 — Worked examples

### Example 1 — Standard domestic sale (13% embedded)

**Input line:** `05.04.2026 ; EMPRESA ABC SRL ; CREDIT ; Factura 1041 servicios ; BOB 11,300`

**Reasoning:** IVA is embedded. Gross = BOB 11,300 = net. IVA component = 11,300 * 13/113 = BOB 1,300. Debito fiscal.

| Date | Counterparty | Gross | Net | IVA | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 05.04.2026 | EMPRESA ABC SRL | +11,300 | +10,000 | 1,300 | 13% | Debito fiscal | N | — |

### Example 2 — Purchase with factura (credito fiscal)

**Input line:** `10.04.2026 ; PROVEEDOR XYZ ; DEBIT ; Factura 5678 insumos ; BOB -5,650`

**Reasoning:** Purchase with SIN-authorized factura. Credito fiscal = 5,650 * 13/113 = BOB 650.

| Date | Counterparty | Gross | Net | IVA | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 10.04.2026 | PROVEEDOR XYZ | -5,650 | -5,000 | 650 | 13% | Credito fiscal | N | — |

### Example 3 — Export, zero-rated

**Input line:** `15.04.2026 ; BRAZILIAN BUYER SA ; CREDIT ; Exported quinoa ; BOB 100,000`

| Date | Counterparty | Gross | Net | IVA | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 15.04.2026 | BRAZILIAN BUYER SA | +100,000 | +100,000 | 0 | 0% | Zero-rated | N | — |

### Example 4 — Bank charges

**Input line:** `30.04.2026 ; BNB ; DEBIT ; Comision mensual ; BOB -30`

| Date | Counterparty | Gross | Net | IVA | Rate | Field | Default? | Excluded? |
|---|---|---|---|---|---|---|---|---|
| 30.04.2026 | BNB | -30 | — | — | — | — | N | "Financial service" |

---

## Section 5 — Tier 1 classification rules (compressed)

### 5.1 Standard rate 13% (embedded) — IVA is included in the total price. Extract: total * 13/113.
### 5.2 Zero rate — Exports with customs documentation.
### 5.3 Exempt — Basic food basket, education, limited financial services.
### 5.4 Credito fiscal — Valid SIN-authorized factura required. Must be dosificada (authorized). Without factura, no credit.
### 5.5 Blocked input — Personal consumption, entertainment without factura.
### 5.6 Imports — IVA at 13% on CIF plus duty. Paid at customs. Creditable with póliza de importación.
### 5.7 IT (Impuesto a las Transacciones) — 3% on gross revenue. Separate from IVA. Offsettable against IUE.
### 5.8 Electronic invoicing — SIN requires electronic invoicing (facturación electrónica) via SIAT system.

---

## Section 6 — Tier 2 catalogue (compressed)

### 6.1 Factura validity — Default: no credit without factura. Question: "Do you have a SIN-authorized factura?"
### 6.2 IT offset against IUE — Default: flag for accountant.
### 6.3 SaaS entities — Default: self-assess 13%.
### 6.4 Cash withdrawals — Default: exclude.

---

## Section 7 — Excel working paper template

Per vat-workflow-base Section 3: Debito fiscal (output), Credito fiscal (input), Zero-rated, Exempt, Net IVA.

---

## Section 8 — Bank statement reading guide

BNB and Banco Mercantil exports CSV/PDF. BOB primary. Spanish descriptions. Internal transfers: exclude.

---

## Section 9 — Onboarding fallback

### 9.1 NIT — "What is your NIT (Numero de Identificación Tributaria)?"
### 9.2 Filing deadline — Based on last digit of NIT.
### 9.3 Industry — "What does the business do?"
### 9.4 Exports — "Do you export?"
### 9.5 Credit brought forward — Always ask.

---

## Section 10 — Reference material

### Sources
1. Ley 843 (Tax Reform Law, IVA provisions). 2. SIN regulations. 3. Newton/SIAT portal.

### Change log
- v2.0 (April 2026): Full rewrite to Malta v2.0 ten-section structure.

---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. All outputs must be reviewed by a qualified professional before filing.

The most up-to-date version is maintained at [openaccountants.com](https://openaccountants.com).


---

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at [openaccountants.com](https://openaccountants.com). Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.
