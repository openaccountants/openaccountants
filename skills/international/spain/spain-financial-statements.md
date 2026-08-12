---
name: spain-financial-statements
description: Use this skill when preparing, reviewing, or advising on annual financial statements (cuentas anuales) for a Spanish company. Trigger on phrases like "cuentas anuales", "Registro Mercantil", "depósito de cuentas", "Plan General de Contabilidad", "PGC", "PGC PYMES", "balance", "cuenta de pérdidas y ganancias", "memoria", "auditoría España", "ICAC", or any question about preparing and filing statutory accounts under Spanish commercial law. Covers PGC/PGC-PYMES frameworks, size thresholds, required statements, formats, notes, filing deadlines, and audit requirements.
version: 1.0
jurisdiction: ES
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - financial-statements-workflow-base
category: financial-statements
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain Financial Statements

## Spain Financial Statements Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Spain (Reino de España) |
| Currency | EUR |
| Filing authority | Registro Mercantil Provincial |
| Primary legislation | Texto Refundido de la Ley de Sociedades de Capital (TRLSC); Código de Comercio |
| Supporting legislation | Real Decreto 1514/2007 (PGC); Real Decreto 1515/2007 (PGC-PYMES); Ley 22/2015 (Auditoría) |
| Accounting standards | Plan General de Contabilidad (PGC) or PGC-PYMES |
| Financial year | Usually calendar year (January–December) |
| Filing deadline | 1 month after AGM approval of accounts |
| AGM deadline | Within 6 months from year-end |
| Filing fee | Approximately EUR 20–40 (varies by registry) |
| Digital filing | Electronic via registradores.org or paper |

## Section 2 -- Reporting Framework

**Reporting Framework**

| Entity type | Applicable standard |
| --- | --- |
| Large/medium companies | PGC (full Plan General de Contabilidad, RD 1514/2007) |
| Small companies (eligible per Art. 257 TRLSC) | PGC-PYMES (simplified, RD 1515/2007) or full PGC (choice) |
| Micro-entities (Art. 2 RD 1515/2007) | PGC-PYMES with additional micro-entity simplifications |
| Listed groups (consolidated) | IFRS as adopted by the EU (mandatory) |
| Non-listed groups (consolidated) | PGC consolidated rules or IFRS (choice) |

## Section 3 -- Size Thresholds

### Abbreviated accounts (cuentas anuales abreviadas) — Art. 257 TRLSC

- **Eligibility condition** — Companies may prepare abbreviated balance sheet and equity statement if for two consecutive years they meet at least 2 of 3 criteria  _(Art. 257 TRLSC)_

**Abbreviated balance sheet vs P&L thresholds**  _(Art. 257, Art. 258 TRLSC)_

| Criterion | Abbreviated balance sheet (Art. 257) | Abbreviated P&L (Art. 258) |
| --- | --- | --- |
| Total activo (Total assets) | ≤ EUR 4,000,000 | ≤ EUR 11,400,000 |
| Cifra de negocios (Turnover) | ≤ EUR 8,000,000 | ≤ EUR 22,800,000 |
| Empleados (Employees) | ≤ 50 | ≤ 250 |

### PGC-PYMES eligibility

- **PGC-PYMES eligibility thresholds** — Same thresholds as abbreviated balance sheet (Art. 257 TRLSC): assets ≤ EUR 4M, turnover ≤ EUR 8M, employees ≤ 50.  _(Art. 257 TRLSC)_

### Micro-entity criteria (within PGC-PYMES)

**Micro-entity criteria**

| Criterion | Threshold |
| --- | --- |
| Total activo | ≤ EUR 1,000,000 |
| Cifra de negocios | ≤ EUR 2,000,000 |
| Empleados | ≤ 10 |

## Section 4 -- Required Financial Statements

**Required Financial Statements**

| Document | Micro/Small (abbreviated) | Medium/Large (normal) |
| --- | --- | --- |
| Balance (Balance sheet) | Required (abridged) | Required (full) |
| Cuenta de pérdidas y ganancias (P&L) | Required (abridged if Art. 258 met) | Required (full) |
| Estado de cambios en el patrimonio neto (ECPN) | Not required (abbreviated) | Required |
| Estado de flujos de efectivo (EFE / Cash flow) | Not required | Required (if not abbreviated balance) |
| Memoria (Notes) | Required (abbreviated) | Required (full) |
| Informe de gestión (Management report) | Not required (if abbreviated balance) | Required |
| Informe de auditoría (Audit report) | If applicable | Required |

## Section 5 -- Year-End Adjustments Checklist

**Year-End Adjustments Checklist**

| # | Adjustment | Spain-specific notes |
| --- | --- | --- |
| 1 | Amortización (Depreciation) | PGC NRV 2ª; systematic method; useful life; fiscal tables (tax alignment common for SMEs) |
| 2 | Provisiones (Provisions) | PGC NRV 15ª; probable obligation, reliable estimate |
| 3 | Periodificación (Accruals/prepayments) | Ajustes por periodificación; strict matching |
| 4 | Deterioro de créditos comerciales (Bad debts) | PGC NRV 9ª; individual + portfolio-based; insolvency at 6 months overdue |
| 5 | Existencias (Inventory) | Lower of cost (PMP/FIFO) and net realisable value |
| 6 | Impuesto diferido (Deferred tax) | PGC NRV 13ª; temporary differences; IS rate 25% (general) |
| 7 | Diferencias de cambio (FX) | PGC NRV 11ª; monetary items at closing rate |
| 8 | Indemnizaciones por despido (Severance) | Provision if restructuring plan exists |
| 9 | Vacaciones devengadas (Holiday accrual) | Provision for untaken leave + social security |
| 10 | Subvenciones de capital (Capital grants) | Recognised in equity, released to P&L over asset life |
| 11 | Arrendamientos financieros (Finance leases) | Capitalised (PGC NRV 8ª) — substance over form |
| 12 | Impuesto sobre Sociedades (IS provision) | Current tax + deferred tax adjustments |

## Section 6 -- Cuenta de Pérdidas y Ganancias Format (P&L)

PGC format — normal model (by nature):

```
A) OPERACIONES CONTINUADAS

1. Importe neto de la cifra de negocios
   a) Ventas
   b) Prestaciones de servicios

2. Variación de existencias de productos terminados y en curso

3. Trabajos realizados por la empresa para su activo

4. Aprovisionamientos
   a) Consumo de mercaderías
   b) Consumo de materias primas
   c) Trabajos realizados por otras empresas

5. Otros ingresos de explotación

6. Gastos de personal
   a) Sueldos, salarios y asimilados
   b) Cargas sociales

7. Otros gastos de explotación

8. Amortización del inmovilizado

9. Imputación de subvenciones de inmovilizado no financiero

10. Excesos de provisiones

11. Deterioro y resultado por enajenaciones del inmovilizado

   A.1) RESULTADO DE EXPLOTACIÓN

12. Ingresos financieros
13. Gastos financieros
14. Variación de valor razonable en instrumentos financieros
15. Diferencias de cambio
16. Deterioro y resultado por enajenaciones de instrumentos financieros

   A.2) RESULTADO FINANCIERO

   A.3) RESULTADO ANTES DE IMPUESTOS

17. Impuestos sobre beneficios

   A.4) RESULTADO DEL EJERCICIO PROCEDENTE DE OPERACIONES CONTINUADAS

B) OPERACIONES INTERRUMPIDAS

   A.5) RESULTADO DEL EJERCICIO
```

## Section 7 -- Balance Format (Balance Sheet)

PGC format — normal model:

```
ACTIVO (Assets)

A) ACTIVO NO CORRIENTE
   I.   Inmovilizado intangible
   II.  Inmovilizado material
   III. Inversiones inmobiliarias
   IV.  Inversiones en empresas del grupo y asociadas a largo plazo
   V.   Inversiones financieras a largo plazo
   VI.  Activos por impuesto diferido

B) ACTIVO CORRIENTE
   I.   Existencias
   II.  Deudores comerciales y otras cuentas a cobrar
   III. Inversiones en empresas del grupo y asociadas a corto plazo
   IV.  Inversiones financieras a corto plazo
   V.   Periodificaciones a corto plazo
   VI.  Efectivo y otros activos líquidos equivalentes

TOTAL ACTIVO

─────────────────────────────────────

PATRIMONIO NETO Y PASIVO

A) PATRIMONIO NETO (Equity)
   A-1) Fondos propios
     I.   Capital
     II.  Prima de emisión
     III. Reservas
     IV.  Acciones y participaciones propias (-)
     V.   Resultados de ejercicios anteriores
     VI.  Otras aportaciones de socios
     VII. Resultado del ejercicio
   A-2) Ajustes por cambios de valor
   A-3) Subvenciones, donaciones y legados

B) PASIVO NO CORRIENTE
   I.   Provisiones a largo plazo
   II.  Deudas a largo plazo
   III. Deudas con empresas del grupo y asociadas a largo plazo
   IV.  Pasivos por impuesto diferido

C) PASIVO CORRIENTE
   I.   Provisiones a corto plazo
   II.  Deudas a corto plazo
   III. Deudas con empresas del grupo y asociadas a corto plazo
   IV.  Acreedores comerciales y otras cuentas a pagar
   V.   Periodificaciones a corto plazo

TOTAL PATRIMONIO NETO Y PASIVO
```

## Section 8 -- Memoria (Notes to Accounts)

**Memoria (Notes to Accounts)**

| # | Disclosure | Abbreviated | Normal |
| --- | --- | --- | --- |
| 1 | Actividad de la empresa (Company activity) | Required | Required |
| 2 | Bases de presentación (Basis of preparation) | Required | Required |
| 3 | Normas de valoración (Accounting policies) | Required (simplified) | Required (full) |
| 4 | Inmovilizado material e intangible | Required (summary) | Required (movements) |
| 5 | Instrumentos financieros | Simplified | Required (full IFRS 7 equivalent) |
| 6 | Existencias (Inventory) | Required | Required |
| 7 | Fondos propios (Equity) | Required | Required |
| 8 | Situación fiscal (Tax position) | Simplified | Required (reconciliation) |
| 9 | Ingresos y gastos (Revenue/expenses) | Not required | Required |
| 10 | Partes vinculadas (Related parties) | Required | Required (detailed) |
| 11 | Otra información (Other) | Headcount, auditor fees | Full |
| 12 | Hechos posteriores (Subsequent events) | Required | Required |

## Section 9 -- Filing Requirements

**Filing Requirements**

| Item | Detail |
| --- | --- |
| Filing authority | Registro Mercantil of the province where registered office is located |
| Filing method | Electronic (registradores.org) or paper at registry |
| Formulation deadline | Directors must formulate accounts within 3 months of year-end |
| AGM approval deadline | Within 6 months from year-end |
| Filing deadline | Within 1 month after AGM approval |
| Latest possible filing | End of July (for calendar-year companies) |
| Format | Standardised models approved annually by DGRN/DGSJFP resolution |
| Language | Spanish (or co-official language of the autonomous community) |
| Penalty for non-filing | Registry closure (no new entries); fine EUR 1,200–60,000 |
| XBRL | Not mandatory for individual accounts (consolidated listed: ESEF/XBRL) |

### Consequences of non-filing

- **Registry closure**: if accounts not filed for one year, the Registro Mercantil closes the company's sheet — no new registrations (appointments, capital changes) until filed
- **Fine**: ICAC can impose fines from EUR 1,200 to EUR 60,000 (based on turnover)

## Section 10 -- Audit Requirements

### Mandatory audit (Art. 263 TRLSC)

- **Mandatory audit trigger condition** — A company must undergo audit if, for two consecutive financial years, it exceeds at least 2 of 3 thresholds.  _(Art. 263 TRLSC)_

**Mandatory audit thresholds**  _(Art. 263 TRLSC)_

| Criterion | Threshold |
| --- | --- |
| Total activo (Total assets) | > EUR 2,850,000 |
| Cifra neta de negocios (Net turnover) | > EUR 5,700,000 |
| Número medio de empleados (Employees) | > 50 |

- **Cessation of audit obligation** — The audit obligation ceases when the company no longer exceeds two thresholds for two consecutive years.  _(Art. 263 TRLSC)_

### Always subject to audit (regardless of size)

- Companies issuing securities on regulated markets
- Companies receiving public subsidies or contracting with public sector above certain thresholds
- Companies forming part of a group required to consolidate
- Insurance and financial entities

### Auditor qualification

- **Auditor qualification requirement** — Auditor inscrito en el Registro Oficial de Auditores de Cuentas (ROAC), regulated by the Instituto de Contabilidad y Auditoría de Cuentas (ICAC).  _(ROAC / ICAC)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional before filing or acting upon.

## Talk to a verified accountant

This skill is a tool, not an engagement. Every taxpayer's situation is
different, and the rules in the skill may not match your specific facts.

To speak with one of the licensed accountants who verifies skills for your
jurisdiction — **no liability on either side until you and the accountant sign
a formal engagement letter** — book a free 30-minute call:

**→ [Book a call](https://calendly.com/openaccountants-info/30min)**

We'll route you to the named verifier covering your country or state. You can
also see the full list of verified accountants at
[openaccountants.com/network](https://openaccountants.com/network).

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
