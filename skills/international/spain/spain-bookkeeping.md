---
name: spain-bookkeeping
description: Use this skill whenever asked about bookkeeping, chart of accounts, Plan General de Contabilidad (PGC), financial statements, P&L format, balance sheet layout, bank reconciliation, expense classification, asset capitalisation, or day-to-day accounting for a Spanish entity. Trigger on phrases like "PGC", "Plan General de Contabilidad", "cuadro de cuentas", "chart of accounts Spain", "balance", "cuenta de pérdidas y ganancias", "PYMES accounting", "microempresa Spain", "capitalise or expense Spain", "amortización", "depreciation Spain", "bank reconciliation Spain", "autónomo bookkeeping", "bookkeeping Spain", or any question about recording transactions, classifying expenses, or preparing accounts under Spanish law. ALWAYS read this skill before touching any bookkeeping work for Spain.
version: 1.0
jurisdiction: ES
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - bookkeeping-workflow-base
category: bookkeeping
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Spain Bookkeeping

## Spain Bookkeeping Skill v1.0

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | Spain (Reino de España) |
| Currency | EUR |
| Financial year | Calendar year (1 Jan -- 31 Dec) for tax; companies may choose any 12-month period if stated in articles |
| Accounting standards | PGC (Plan General de Contabilidad, RD 1514/2007); PGC-PYMES (RD 1515/2007) for SMEs |
| Governing body | ICAC (Instituto de Contabilidad y Auditoría de Cuentas); Agencia Tributaria |
| Key legislation | Código de Comercio (Art. 25--49); Ley de Sociedades de Capital; LIS (Ley 27/2014 del Impuesto sobre Sociedades); LIRPF (Ley 35/2006); PGC / PGC-PYMES |
| Standard chart of accounts | PGC Cuadro de Cuentas — 7 groups, not mandatory to use exact codes but recommended and universally adopted |
| Record retention | 6 years from last entry (Código de Comercio Art. 30) |

## Section 2 -- Standard Chart of Accounts (PGC / PGC-PYMES — Cuadro de Cuentas)

The PGC defines 7 account groups. Groups 1--5 are balance sheet accounts; Groups 6--7 are income statement accounts. The cuadro de cuentas is technically not mandatory, but it is universally used and the definitions and accounting relationships in Part 5 of the PGC are binding.

### Grupo 1: Financiación Básica (Basic Financing — Equity & Long-Term Liabilities)

**Grupo 1 accounts**

| Code | Account | Notes |
| --- | --- | --- |
| 100 | Capital social | Share capital |
| 102 | Capital | Owner's equity (sole trader) |
| 112 | Reserva legal | Legal reserve (10% of profit until 20% of capital) |
| 113 | Reservas voluntarias | Voluntary reserves |
| 120 | Remanente | Retained earnings |
| 121 | Resultados negativos de ejercicios anteriores | Accumulated losses |
| 129 | Resultado del ejercicio | Current year profit/loss |
| 130 | Subvenciones oficiales de capital | Government capital grants |
| 141 | Provisión para impuestos | Tax provisions |
| 142 | Provisión para otras responsabilidades | Other provisions |
| 170 | Deudas a largo plazo con entidades de crédito | Long-term bank loans |
| 171 | Deudas a largo plazo | Other long-term debts |
| 174 | Acreedores por arrendamiento financiero a l/p | Finance lease liabilities (long-term) |

### Grupo 2: Activo No Corriente (Non-Current Assets)

**Grupo 2 accounts**

| Code | Account | Notes |
| --- | --- | --- |
| 200 | Investigación | Research costs (expense under PGC-PYMES) |
| 201 | Desarrollo | Development costs |
| 203 | Propiedad industrial | Patents, trademarks |
| 206 | Aplicaciones informáticas | Software |
| 210 | Terrenos y bienes naturales | Land |
| 211 | Construcciones | Buildings |
| 212 | Instalaciones técnicas | Technical installations |
| 213 | Maquinaria | Machinery |
| 214 | Utillaje | Tools |
| 215 | Otras instalaciones | Other installations |
| 216 | Mobiliario | Furniture |
| 217 | Equipos para procesos de información | Computer equipment |
| 218 | Elementos de transporte | Vehicles |
| 219 | Otro inmovilizado material | Other tangible assets |
| 280 | Amortización acumulada del inmovilizado intangible | Accumulated amortisation (intangible) |
| 281 | Amortización acumulada del inmovilizado material | Accumulated depreciation (tangible) |
| 290 | Deterioro de valor del inmovilizado intangible | Impairment (intangible) |
| 291 | Deterioro de valor del inmovilizado material | Impairment (tangible) |

### Grupo 3: Existencias (Inventories)

**Grupo 3 accounts**

| Code | Account | Notes |
| --- | --- | --- |
| 300 | Mercaderías | Merchandise |
| 310 | Materias primas | Raw materials |
| 350 | Productos terminados | Finished goods |
| 390 | Deterioro de valor de las mercaderías | Inventory provisions |

### Grupo 4: Acreedores y Deudores por Operaciones Comerciales (Trade Payables & Receivables)

**Grupo 4 accounts**

| Code | Account | Notes |
| --- | --- | --- |
| 400 | Proveedores | Trade payables |
| 410 | Acreedores por prestaciones de servicios | Creditors for services |
| 430 | Clientes | Trade receivables |
| 440 | Deudores | Sundry debtors |
| 465 | Remuneraciones pendientes de pago | Salaries payable |
| 470 | Hacienda Pública, deudora | Tax receivable (income tax, IVA) |
| 4700 | H.P. deudora por IVA | IVA receivable (input > output) |
| 472 | H.P. IVA soportado | Input IVA |
| 473 | H.P. retenciones y pagos a cuenta | Withholding tax paid |
| 475 | Hacienda Pública, acreedora | Tax payable |
| 4750 | H.P. acreedora por IVA | IVA payable |
| 477 | H.P. IVA repercutido | Output IVA |
| 476 | Organismos de la Seguridad Social, acreedores | Social security payable |
| 480 | Gastos anticipados | Prepaid expenses |
| 485 | Ingresos anticipados | Deferred income |

### Grupo 5: Cuentas Financieras (Financial Accounts)

**Grupo 5 accounts**

| Code | Account | Notes |
| --- | --- | --- |
| 520 | Deudas a corto plazo con entidades de crédito | Short-term bank loans |
| 523 | Proveedores de inmovilizado a corto plazo | Short-term creditors for fixed assets |
| 524 | Acreedores por arrendamiento financiero a c/p | Finance lease liabilities (short-term) |
| 551 | Cuenta corriente con socios y administradores | Directors' current account |
| 570 | Caja, euros | Cash in hand (EUR) |
| 572 | Bancos e instituciones de crédito c/c vista | Bank current accounts |
| 573 | Bancos e instituciones de crédito c/c ahorro | Bank savings accounts |
| 574 | Bancos e inst. crédito, cuentas ahorro, m/e | Foreign currency bank accounts |

### Grupo 6: Compras y Gastos (Purchases & Expenses)

**Grupo 6 accounts**

| Code | Account | Notes |
| --- | --- | --- |
| 600 | Compras de mercaderías | Merchandise purchases |
| 601 | Compras de materias primas | Raw material purchases |
| 602 | Compras de otros aprovisionamientos | Other supplies |
| 606 | Descuentos sobre compras por pronto pago | Purchase discounts |
| 607 | Trabajos realizados por otras empresas | Subcontracting |
| 621 | Arrendamientos y cánones | Rent and royalties |
| 622 | Reparaciones y conservación | Repairs and maintenance |
| 623 | Servicios de profesionales independientes | Professional fees |
| 624 | Transportes | Transport costs |
| 625 | Primas de seguros | Insurance premiums |
| 626 | Servicios bancarios y similares | Bank charges |
| 627 | Publicidad, propaganda y relaciones públicas | Advertising and PR |
| 628 | Suministros | Utilities (electricity, water, gas) |
| 629 | Otros servicios | Telecoms, postage, other services |
| 631 | Otros tributos | Non-income taxes (IAE, IBI) |
| 640 | Sueldos y salarios | Salaries |
| 642 | Seguridad Social a cargo de la empresa | Employer social security |
| 649 | Otros gastos sociales | Other social costs |
| 650 | Pérdidas de créditos comerciales incobrables | Bad debts |
| 662 | Intereses de deudas | Interest on borrowings |
| 669 | Otros gastos financieros | Other financial expenses |
| 678 | Gastos excepcionales | Exceptional charges |
| 680 | Amortización del inmovilizado intangible | Amortisation — intangible |
| 681 | Amortización del inmovilizado material | Depreciation — tangible |
| 694 | Pérdidas por deterioro de créditos | Impairment of receivables |

### Grupo 7: Ventas e Ingresos (Sales & Revenue)

**Grupo 7 accounts**

| Code | Account | Notes |
| --- | --- | --- |
| 700 | Ventas de mercaderías | Merchandise sales |
| 701 | Ventas de productos terminados | Sales of finished goods |
| 705 | Prestaciones de servicios | Service revenue |
| 706 | Descuentos sobre ventas por pronto pago | Sales discounts |
| 708 | Devoluciones de ventas | Sales returns |
| 740 | Subvenciones, donaciones y legados a la explotación | Operating grants |
| 746 | Subvenciones, donaciones y legados de capital transferidos | Capital grants amortised |
| 762 | Ingresos de créditos | Interest income |
| 769 | Otros ingresos financieros | Other financial income |
| 771 | Beneficios procedentes del inmovilizado material | Gains on disposal of fixed assets |
| 778 | Ingresos excepcionales | Exceptional income |

## Section 3 -- Revenue Recognition

**Revenue Recognition scenarios**

| Scenario | Treatment |
| --- | --- |
| **Default (PGC)** | Accruals basis (devengo) — revenue recognised when goods/services delivered |
| **Estimación directa normal** | Full accruals with double-entry bookkeeping |
| **Estimación directa simplificada** | Simplified bookkeeping but still accruals basis; available if prior year revenue < EUR 600,000 |
| **Estimación objetiva (módulos)** | Revenue estimated by objective parameters (for qualifying activities); simplified records |
| **Autónomos (self-employed)** | Must keep libro de ingresos (income book) and libro de gastos (expense book) |
| **IVA on sales** | Revenue recorded net of IVA; IVA goes to 477 (IVA repercutido) |
| **Advance payments** | Credited to 485 (Ingresos anticipados) until service delivered |

### IVA Rates (2025)

**IVA Rates**

| Rate | Application |
| --- | --- |
| 21% (general) | Standard rate — most goods and services |
| 10% (reducido) | Food, transport, hotels, renovation |
| 4% (superreducido) | Bread, milk, fruit, vegetables, books, medicines |
| 0% (exento) | Medical, education, financial services, insurance |

## Section 4 -- Expense Classification

**Expense Classification table**

| Expense Type | PGC Code | Tax Deductibility | Notes |
| --- | --- | --- | --- |
| Rent (commercial premises) | 621 | Fully deductible |  |
| Utilities | 628 | Fully deductible for business premises | Apportion if home office |
| Home office (autónomo) | 628/621 | 30% of proportional area for utilities; rent proportional to m² | Art. 30.2.5c LIRPF |
| Professional fees (asesor fiscal, abogado) | 623 | Fully deductible | Subject to 15% IRPF retention |
| Insurance | 625 | Fully deductible (business) |  |
| Advertising | 627 | Fully deductible |  |
| Travel | 629 | Deductible; per-diem: EUR 26.67/day (Spain), EUR 48.08/day (abroad) |  |
| Entertainment | 627 | Deductible if related to revenue generation and documented | No blanket block; reasonableness test |
| Office supplies | 602 | Fully deductible |  |
| Telecoms | 629 | Fully deductible (business line) | Apportion if mixed |
| Bank charges | 626 | Fully deductible |  |
| Vehicle (autónomo) | Various | 50% IVA deductible; income tax deductible only if exclusively for business (affectación exclusiva) | Very restrictive for autónomos |
| Vehicle fuel | 602 | 50% IVA deductible (rebuttable); income tax % based on use |  |
| Fines and penalties | 678 | NOT deductible |  |
| Depreciation | 680/681 | Deductible per LIS Art. 12 tables | See Section 5 |
| Donations | 678 | Limited deductibility (LIS Art. 20: 10% of tax base) |  |

## Section 5 -- Asset vs Expense Thresholds

### Capitalisation Rules

**Capitalisation Rules**  _(LIS Art. 102; LIS Art. 12)_

| Rule | Amount | Treatment |
| --- | --- | --- |
| **Low-value assets (empresas de reducida dimensión)** | ≤ EUR 300 per unit, max EUR 25,000/year aggregate | May be expensed immediately (LIS Art. 102) |
| **General rule** | > EUR 300 or above aggregate limit | Capitalise and depreciate per LIS Art. 12 |
| **Autónomos (estimación directa)** | Same rules apply |  |

### Depreciation Rates (LIS Art. 12.1.a — Tabla de Amortización Lineal)

**Depreciation Rates Table**  _(LIS Art. 12.1.a)_

| Asset Category | Max Linear Rate | Max Period (Years) |
| --- | --- | --- |
| Civil works (general) | 2% | 100 |
| Industrial buildings | 3% | 68 |
| Commercial/administrative buildings | 2% | 100 |
| General installations | 10% | 20 |
| Machinery (maquinaria) | 12% | 18 |
| Tools (utillaje) | 25% | 8 |
| Furniture (mobiliario) | 10% | 20 |
| Electronic equipment (equipos electrónicos) | 20% | 10 |
| Computer equipment (equipos de información) | 25% | 8 |
| Software (sistemas y programas informáticos) | 33% | 6 |
| Vehicles — external transport | 16% | 14 |
| Vehicles — trucks (autocamiones) | 20% | 10 |
| Internal transport elements | 10% | 20 |
| Other fixtures (otros enseres) | 15% | 14 |

### Accelerated Depreciation for Small Businesses (Empresas de Reducida Dimensión)

- **Accelerated depreciation availability** — Available to businesses with prior-year net revenue < EUR 10,000,000: New tangible fixed assets and real estate investments: 2x the maximum linear coefficient; Intangible assets with indefinite useful life: 150% of the deductible amount; Applies for 3 years after exceeding the EUR 10M threshold EUR  _(Empresas de Reducida Dimensión regime)_

### Estimación Directa Simplificada Table

For autónomos using the simplified direct estimation method, a separate simplified depreciation table (Orden de 27 de marzo de 1998) applies with generally similar or slightly higher rates.

## Section 6 -- P&L Format (Cuenta de Pérdidas y Ganancias)

The PGC-PYMES prescribes a vertical format classifying expenses by nature:

```
CUENTA DE PÉRDIDAS Y GANANCIAS
Ejercicio terminado el [date]

 1. Importe neto de la cifra de negocios               xxx
    a) Ventas                                           xxx
    b) Prestaciones de servicios                        xxx
 2. Variación de existencias de productos               xxx
 3. Trabajos realizados por la empresa para su activo   xxx
 4. Aprovisionamientos                                 (xxx)
    a) Consumo de mercaderías                          (xxx)
    b) Consumo de materias primas                      (xxx)
    c) Trabajos realizados por otras empresas           (xxx)
 5. Otros ingresos de explotación                       xxx
 6. Gastos de personal                                 (xxx)
    a) Sueldos, salarios y asimilados                  (xxx)
    b) Cargas sociales                                 (xxx)
 7. Otros gastos de explotación                        (xxx)
    a) Servicios exteriores                            (xxx)
    b) Tributos                                        (xxx)
    c) Pérdidas, deterioro y variación provisiones     (xxx)
    d) Otros gastos de gestión corriente               (xxx)
 8. Amortización del inmovilizado                      (xxx)
 9. Imputación de subvenciones de inmovilizado          xxx
10. Excesos de provisiones                              xxx
11. Deterioro y resultado por enajenaciones             xxx
                                                       -----
A) RESULTADO DE EXPLOTACIÓN                             xxx

12. Ingresos financieros                                xxx
13. Gastos financieros                                 (xxx)
14. Variaciones de valor razonable en inst. financieros xxx
15. Diferencias de cambio                               xxx
16. Deterioro y resultado enajenaciones inst. fin.      xxx
                                                       -----
B) RESULTADO FINANCIERO                                 xxx
                                                       -----
C) RESULTADO ANTES DE IMPUESTOS (A+B)                   xxx

17. Impuestos sobre beneficios                         (xxx)
                                                       -----
D) RESULTADO DEL EJERCICIO                              xxx
```

## Section 7 -- Balance Sheet Format (Balance de Situación)

The PGC-PYMES prescribes a horizontal format:

```
BALANCE DE SITUACIÓN
Al [date]

ACTIVO                                  PATRIMONIO NETO Y PASIVO

A) ACTIVO NO CORRIENTE                 A) PATRIMONIO NETO
   I.   Inmovilizado intangible  xxx      A-1) Fondos propios
   II.  Inmovilizado material    xxx         I.   Capital            xxx
   III. Inversiones inmobiliarias xxx        III.  Reservas           xxx
   IV.  Inversiones financieras  xxx        V.    Resultados ej. ant. xxx
                                -----       VII.  Resultado ejercicio xxx
                                 xxx                                -----
                                                                     xxx
B) ACTIVO CORRIENTE                        A-2) Subvenciones, donaciones xxx
   I.   Existencias              xxx
   II.  Deudores comerciales     xxx   B) PASIVO NO CORRIENTE
   III. Inversiones fin. c/p     xxx      I.   Deudas a largo plazo  xxx
   IV.  Efectivo y equiv.        xxx      II.  Deudas con emp. grupo xxx
                                -----                               -----
                                 xxx                                 xxx

                                       C) PASIVO CORRIENTE
                                          I.   Deudas a corto plazo  xxx
                                          II.  Deudas con emp. grupo xxx
                                          III. Acreedores comerciales xxx
                                                                    -----
                                                                     xxx
                                -----                               -----
TOTAL ACTIVO                     xxx   TOTAL P. NETO Y PASIVO        xxx
```

## Section 8 -- Bank Reconciliation Patterns

### Spanish Bank Statement Formats

**Spanish Bank Statement Formats**

| Bank | Format | Key Fields |
| --- | --- | --- |
| CaixaBank | Norma 43 (CSB) / CSV | Fecha operación, Fecha valor, Concepto, Importe, Saldo |
| Banco Santander | Norma 43 / CSV / OFX | Fecha, Concepto, Importe, Saldo disponible |
| BBVA | Norma 43 / CSV | Fecha, Descripción, Cargo, Abono, Saldo |
| Banco Sabadell | Norma 43 / CSV | Fecha movimiento, Concepto, Importe |
| Bankinter | Norma 43 / CSV | Fecha, Descripción, Importe |
| Revolut / N26 | CSV | Date, Description, Amount, Currency |

- **Norma 43 (Cuaderno 43)** — The Spanish banking standard for electronic statements, widely supported by accounting software (ContaPlus, Sage, Holded, etc.).

### Common Spanish Transaction Descriptions

**Common Spanish Transaction Descriptions**

| Pattern | Likely Classification |
| --- | --- |
| TRANSFERENCIA / TRANSF | Bank transfer — check if income or expense |
| RECIBO / ADEUDO | Direct debit — utility, insurance, social security |
| TARJETA / TPV | Card payment — check merchant |
| NÓMINA | Payroll payment (640) |
| AEAT / AGENCIA TRIBUTARIA | Tax payment (IVA, IRPF, IS) — exclude from P&L |
| SEG. SOCIAL / TGSS | Social security contribution (642) |
| ALQUILER | Rent payment (621) |
| CUOTA PRÉSTAMO | Loan instalment — split capital (170/520) and interest (662) |
| COMISIÓN / GASTOS | Bank charges (626) |
| TRASPASO | Internal transfer — exclude |
| INGRESO EFECTIVO | Cash deposit |
| AUTÓNOMO / RETA | Self-employed social security contribution |

## Section 9 -- Micro-Entity / Small Business Simplifications

### PGC-PYMES Eligibility (must meet 2 of 3 for two consecutive years)

**PGC-PYMES Eligibility**

| Criterion | PGC-PYMES Threshold | Microempresa Criteria |
| --- | --- | --- |
| Total assets | ≤ EUR 4,000,000 | ≤ EUR 1,000,000 |
| Net revenue | ≤ EUR 8,000,000 | ≤ EUR 2,000,000 |
| Average employees | ≤ 50 | ≤ 10 |

### Simplifications

**Simplifications table**

| Requirement | Microempresa | PGC-PYMES | PGC (full) |
| --- | --- | --- | --- |
| Chart of accounts | PGC-PYMES cuadro | PGC-PYMES cuadro (7 groups) | PGC cuadro (7 groups + subgroups 8/9) |
| Balance sheet | Abbreviated | Abbreviated | Full |
| P&L | Abbreviated | Abbreviated | Full |
| Estado de cambios en el patrimonio neto (ECPN) | NOT required | Required | Required |
| Estado de flujos de efectivo (EFE) | NOT required | NOT required | Required if not abbreviated |
| Memoria (Notes) | Simplified | Simplified | Full |
| Financial instruments | At cost (no fair value) | At cost (simplified) | Fair value options |
| Leases | Expense method allowed (microempresa) | Finance/operating distinction | Full IFRS-style |
| Audit | NOT required (unless exceeding thresholds for 2 years) | Not required if small | Required if exceeding any 2 of: assets > EUR 2.85M, revenue > EUR 5.7M, employees > 50 |
| Filing (Registro Mercantil) | Abbreviated | Abbreviated | Full |

### Autónomo (Self-Employed) Bookkeeping

**Autónomo Bookkeeping Obligations**

| Obligation | Detail |
| --- | --- |
| Libro de ingresos | Record all income with date, invoice number, client, amount, IVA |
| Libro de gastos | Record all expenses with date, invoice number, supplier, amount, IVA |
| Libro registro de bienes de inversión | Fixed asset register (if applicable) |
| Libro registro de IVA | IVA received (repercutido) and IVA paid (soportado) |
| Retention | All books and invoices for 4 years (tax) / 6 years (commercial) |
| SII (Suministro Inmediato de Información) | Mandatory for large companies (revenue > EUR 6M); electronic IVA register reporting |

## Section 10 -- Interaction with Tax Skills

**Interaction with Tax Skills**

| Tax Skill | How Bookkeeping Connects |
| --- | --- |
| **spain-income-tax (IS/IRPF)** | Resultado contable from the cuenta de pérdidas y ganancias is the starting point. Non-deductible items (fines, excess depreciation, non-deductible donations) are adjusted in the Modelo 200 (IS) or Modelo 100 (IRPF). Autónomos declare business income in Modelo 130 (quarterly) and Modelo 100 (annual). |
| **spain-vat-return** | IVA accounts (472 soportado, 477 repercutido, 4700, 4750) feed the Modelo 303 (quarterly IVA return). Annual summary: Modelo 390. Reconcile IVA ledgers quarterly. |
| **es-modelo-111** | IRPF withholdings on professional fees (account 473 for payer; 4751 for payee) declared quarterly on Modelo 111. Annual summary: Modelo 190. |
| **es-rental-income** | Rental income and expenses feed into IRPF rendimientos del capital inmobiliario. Depreciation on rental property at 3% of acquisition cost (excluding land). |
| **spain-social-security** | Autónomo RETA contributions and employer cuotas de Seguridad Social (account 642). Monthly payment to TGSS. Deductible expense for income tax. |

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as an asesor fiscal or auditor de cuentas) before filing or acting upon.

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
