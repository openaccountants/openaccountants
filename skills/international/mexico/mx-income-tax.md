---
name: mx-income-tax
description: Use this skill whenever asked about Mexican individual income tax (ISR) for self-employed individuals (personas físicas con actividades empresariales y profesionales). Trigger on phrases like "how much tax do I pay in Mexico", "ISR", "Declaración Anual", "pagos provisionales", "actividades profesionales", "honorarios", "RESICO", "deducciones personales", "deducciones autorizadas", "retenciones", "RFC", "income tax return Mexico", "SAT", "CFDI honorarios", "comprobante fiscal", or any question about filing or computing income tax for a self-employed or freelance client in Mexico. This skill covers the Declaración Anual PF (Personas Físicas), pagos provisionales (monthly estimated payments), progressive ISR brackets, deducciones autorizadas and personales, retenciones on professional CFDI, and the RESICO regime. ALWAYS read this skill before touching any Mexican income tax work.
version: "2.3"
jurisdiction: MX
tax_year: 2026
last_updated: 2026-10-29
review_status: pending_review
trust_label: Built by Michael Cutajar and the OpenAccountants team
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# MX Income Tax

> **Tax year 2026, with the 2025 tariff kept for 2025 returns filed in April 2026.** Both annual tariffs are from SAT's Resolución Miscelánea Fiscal 2026, Anexo 8 (DOF 28-12-2025), section C, read on 2026-10-29 (sat.gob.mx timed out; read from the Internet Archive copy). The RESICO table is LISR Art. 113-F. No accountant has reviewed it.

Tax year: the calendar year. Currency: Mexican peso (MXN). The Servicio de Administración Tributaria (SAT) administers ISR and IVA.

## Who this applies to

Self-employed individuals (personas físicas con actividades empresariales y profesionales) resident in Mexico: freelancers and professionals paid by honorarios, taxed either under the Régimen de Actividades Empresariales y Profesionales (Régimen General) or, if eligible, under RESICO. Employment income, rental income (Capítulo III) and companies are handled elsewhere or flagged (see the refusal and Tier 2 catalogues below).

### Key Legislation

- **Key Legislation**: LISR (Ley del Impuesto Sobre la Renta): Mexican income tax law; Capítulo II (actividades empresariales y profesionales), Capítulo IX (RESICO). LISR Art. 28, non-deductible expenses (meals cap, fuel rules, etc.). LISR Art. 105, deductible expenses for professionals. Resolución Miscelánea Fiscal 2025, annual SAT administrative rules.  _(LISR; LISR Art. 28; LISR Art. 105; Resolución Miscelánea Fiscal 2025)_

## Rates, bands and thresholds

### ISR Annual Brackets 2026 (Personas Físicas: Régimen General)

**ISR Annual Brackets 2026**  _(RMF 2026 Anexo 8, C.II, tarifa Arts. 97 and 152 LISR, DOF 28-12-2025)_

| Lower Limit (MXN) | Upper Limit (MXN) | Fixed Fee | Rate on Excess |
| --- | --- | --- | --- |
| 0.01 | 10,135.11 | 0 | 1.92% |
| 10,135.12 | 86,022.11 | 194.59 | 6.40% |
| 86,022.12 | 151,176.19 | 5,051.37 | 10.88% |
| 151,176.20 | 175,735.66 | 12,140.13 | 16.00% |
| 175,735.67 | 210,403.69 | 16,069.64 | 17.92% |
| 210,403.70 | 424,353.97 | 22,282.14 | 21.36% |
| 424,353.98 | 668,840.14 | 67,981.92 | 23.52% |
| 668,840.15 | 1,276,925.98 | 125,485.07 | 30.00% |
| 1,276,925.99 | 1,702,567.97 | 307,910.81 | 32.00% |
| 1,702,567.98 | 5,107,703.92 | 444,116.23 | 34.00% |
| 5,107,703.93 | and over | 1,601,862.46 | 35.00% |

### ISR Annual Brackets 2025 (Personas Físicas: Régimen General)

**ISR Annual Brackets 2025, for 2025 returns filed in April 2026**  _(RMF 2025 Anexo 8; reproduced in RMF 2026 Anexo 8, C.I, which this review checked row by row)_

| Lower Limit (MXN) | Upper Limit (MXN) | Fixed Fee | Rate on Excess |
| --- | --- | --- | --- |
| 0.01 | 8,952.49 | 0 | 1.92% |
| 8,952.50 | 75,984.55 | 171.88 | 6.40% |
| 75,984.56 | 133,536.07 | 4,461.94 | 10.88% |
| 133,536.08 | 155,229.80 | 10,723.55 | 16.00% |
| 155,229.81 | 185,852.57 | 14,194.54 | 17.92% |
| 185,852.58 | 374,837.88 | 19,682.13 | 21.36% |
| 374,837.89 | 590,795.99 | 60,049.40 | 23.52% |
| 590,796.00 | 1,127,926.84 | 110,842.74 | 30.00% |
| 1,127,926.85 | 1,503,902.46 | 271,981.99 | 32.00% |
| 1,503,902.47 | 4,511,707.37 | 392,294.17 | 34.00% |
| 4,511,707.38 | and over | 1,414,947.85 | 35.00% |

- **ISR calculation formula**: ISR = Fixed Fee + (taxable income after deductions − Lower Limit) × Rate

SAT publishes the tariffs in Anexo 8 of each year's Resolución Miscelánea Fiscal; LISR Art. 152 updates them when cumulative inflation passes 10%, which happened for 2026. Monthly pagos provisionales use the monthly table in the same Anexo.

RESICO eligibility and the annual table: LISR Arts. 113-E and 113-F. Client withholding of 10% ISR (Régimen General): LISR Art. 106. Client withholding of 1.25% (RESICO): LISR Art. 113-J. IVA at 16%: Ley del IVA.

### RESICO (Régimen Simplificado de Confianza): Alternative

**RESICO rate schedule**

| Annual Income (MXN) | RESICO Rate |
| --- | --- |
| Up to 300,000 | 1.00% |
| 300,001 – 600,000 | 1.10% |
| 600,001 – 1,000,000 | 1.50% |
| 1,000,001 – 2,500,000 | 2.00% |
| 2,500,001 – 3,500,000 | 2.50% |

- **RESICO eligibility**: individuals with only business, professional or leasing income whose income from those activities in the **prior year** did not exceed MXN 3,500,000 may opt in (new starters on an estimate). If income passes MXN 3,500,000 at any time in the year, RESICO stops applying from the following month (LISR Art. 113-E).
- **Monthly payments** use the Art. 113-E monthly table (1.00% up to MXN 25,000 a month; 1.10% to 50,000; 1.50% to 83,333.33; 2.00% to 208,333.33; 2.50% above), due by the 17th of the following month.
- **Withholding by companies:** a persona moral paying a RESICO taxpayer withholds **1.25%** of the payment excluding IVA (LISR Art. 113-J), not the 10% of Art. 106. Both the monthly payments and the 1.25% withheld are credited in the annual return (Art. 113-F).

Rate applied to gross income (no expense deductions)
Monthly provisional = monthly gross × rate
- Annual Declaración Anual due in April of the following year, at the Art. 113-F annual table, with monthly ISR already paid credited
Cannot combine RESICO with Régimen General in same year for same activity

### Retenciones (Withholding by Clients)

**Retenciones (Withholding by Clients)**

| Client Type | Withholding on Honorarios CFDI |
| --- | --- |
| Moral (corporation), payee in Régimen General | 10% ISR (LISR Art. 106) + 2/3 of applicable IVA (10.667% of invoice amount; IVA part not yet confirmed) |
| Moral (corporation), payee in RESICO | 1.25% ISR on the payment excluding IVA (LISR Art. 113-J) |
| Física (individual) with business activity | Same obligations as Moral |
| Persona Física consumer | No withholding obligation |

Retenciones are credited against the annual ISR balance.

- **ISR retenido**: Client withholds 10% on the pre-IVA amount (honorarios brutos). The 10% is an advance payment, not the final rate.

### IVA on Professional Services

- **Standard IVA rate**: 16%
- **IVA treatment for ISR**: Not included in ISR computation: IVA is collected and remitted separately. Strip IVA from all income and expense figures for ISR purposes.

## The taxable base

### Income Patterns

**Income Patterns**

| # | Narration Pattern | Tax Line | Notes |
| --- | --- | --- | --- |
| I-01 | `TRANSFERENCIA DE [client]` / `SPEI DE [client]` | Gross income (ex-IVA) | SPEI (Mexican interbank transfer) from client |
| I-02 | `CoDi COBRO [client]` / `CODI PAGO RECIBIDO` | Gross income (ex-IVA) | CoDi (Cobro Digital) QR/NFC payment from client |
| I-03 | `MERCADO PAGO RETIRO` / `MERCADOPAGO DEPOSITO` | Gross income, gross-up | Mercado Pago payout; fee deductible with CFDI |
| I-04 | `STRIPE PAYMENTS MEXICO` / `STRIPE PAYOUT MXN` | Gross income, gross-up | Stripe Mexico payout; require CFDI Stripe Mexico |
| I-05 | `PAYPAL RETIRO` / `PAYPAL TRANSFER` | Gross income, foreign-source or domestic | PayPal payout; classify by payer country; IVA implications |
| I-06 | `DEPOSITO [client]` / `ABONO [client]` | Gross income (ex-IVA) | Generic bank deposit from client |
| I-07 | `RETENCION ISR 10%` (annotation on CFDI) | Tax credit, not income reduction | Withholding by PJ client; gross up received amount |
| I-08 | `DEVOLUCION SAT` / `SALDO A FAVOR ISR` | NOT income: ISR refund | SAT devolution is not income |
| I-09 | `DEPOSITO IVA RETENIDO` (from client) | IVA retention: NOT ISR income | IVA 2/3 retained by PJ is separate from ISR computation |
| I-10 | `ARRENDAMIENTO RECIBIDO` | Rental income: Capítulo III | Separate from Capítulo II professional income |

### Expense Patterns (Deducciones Autorizadas, require CFDI)

**Expense Patterns (Deducciones Autorizadas, require CFDI)**

| # | Narration Pattern | Tax Line | Notes |
| --- | --- | --- | --- |
| E-01 | `RENTA OFICINA` / `ARRENDAMIENTO OFICINA` | Rent, deductible (professional use) | Require CFDI arrendamiento from landlord |
| E-02 | `CFE ENERGIA ELECTRICA` / `CFE PAGO` | Utilities, deductible (professional proportion) | CFE = Comisión Federal de Electricidad; require CFDI |
| E-03 | `TELMEX` / `IZZI` / `TOTALPLAY` / `MEGACABLE` | Internet/phone, deductible (professional %) | Require CFDI; document business percentage |
| E-04 | `TELCEL` / `AT&T MEXICO` / `MOVISTAR MEXICO` | Mobile, deductible (professional %) | Require CFDI factura |
| E-05 | `ADOBE` / `MICROSOFT 365` / `GOOGLE WORKSPACE` | Software, deductible | Require CFDI or foreign CFDI equivalent |
| E-06 | `CONTADOR` / `DESPACHO CONTABLE` / `CPA` | Accounting fees, deductible | Require CFDI servicios profesionales |
| E-07 | `AEROMEXICO` / `VOLARIS` / `VIVAAEROBUS` | Air travel, deductible (business) | Require CFDI or factura; business purpose needed |
| E-08 | `HOTEL` / `RESERVACION HOTEL` / `AIRBNB` | Accommodation, deductible (business travel) | Require CFDI; meals follow E-09 |
| E-09 | `RESTAURANTE` / `ALIMENTOS` | Meals: 8.5% deductible (Art. 28 fr. XX LISR) | 91.5% of restaurant consumption is non-deductible; the 8.5% is deductible only if paid by credit, debit or service card or SAT-authorised e-wallet |
| E-10 | `COMBUSTIBLE` / `GASOLINA` / `PEMEX` / `OXXO GAS` | Fuel, deductible (vehicle proportion) | Require CFDI; electronic payment only (cash fuel NOT deductible) |
| E-11 | `SEGURO VEHICULO EMPRESARIAL` | Vehicle insurance, deductible (proportion) | Business use proportion |
| E-12 | `PAGO PROVISIONAL ISR SAT` / `LINEA DE CAPTURA` | Pago provisional: NOT deductible | ISR advance payment; not an expense |
| E-13 | `PAGO IVA SAT` | IVA payment: NOT deductible | Separate tax |
| E-14 | `IMSS VOLUNTARIO` | Voluntary IMSS, deducción personal (not autorizada) | Goes in Declaración Anual deducc. personales, not Cap. II |
| E-15 | `CAPACITACION` / `CURSOS` / `DIPLOMADO` | Training, deductible | Require CFDI; professional development |
| E-16 | `PAPELERIA` / `MATERIAL OFICINA` | Office supplies, deductible | Require CFDI; small amounts deductible with CFDI |
| E-17 | `COMISION BANCARIA` / `CUOTA ANUAL TARJETA` | Bank commissions, deductible | Require bank CFDI; professional account fees |

### Deducciones Personales (in Declaración Anual, not Cap. II expenses)

**Deducciones Personales (in Declaración Anual, not Cap. II expenses)**

| # | Type | Cap |
| --- | --- | --- |
| DP-01 | Gastos médicos, dentales, hospitalarios | No cap (require CFDI) |
| DP-02 | Primas de seguros de gastos médicos | No cap (require CFDI) |
| DP-03 | Gastos funerarios | Up to the annual general minimum salary of the taxpayer's geographic area (Art. 151 fr. II) |
| DP-04 | Donativos (donations to authorized entities) | Up to 7% of prior-year income |
| DP-05 | Crédito hipotecario interest | Up to 750,000 UDIs of total credit (Art. 151 fr. IV) |
| DP-06 | Colegiaturas (education) | Capped by education level (peso caps not confirmed; see Not yet confirmed) |
| DP-07 | Aportaciones complementarias / voluntarias de retiro (AFORE, planes personales) | Up to 10% of the year's ingresos acumulables, max five annual general minimum wages (Art. 151 fr. V); outside the overall cap |

- **Total deducciones personales cap**: the lower of 15% of total income (including exempt income) or five times the annual value of the UMA (LISR Art. 151, final paragraph). Only fr. V retirement contributions are outside this cap; donations count inside it.

Statutory anchors for the limits above: the MXN 175,000 car cap is LISR Art. 36 fr. II; the MXN 2,000 cash-payment limit is Art. 27 fr. III; the 8.5% restaurant deduction follows from Art. 28 fr. XX, which makes 91.5% of restaurant consumption non-deductible; the overall cap on deducciones personales (lower of 5 UMA a year or 15% of total income) and the 7% donations limit are Art. 151.

### IMSS / ISSSTE Social Security

- **IMSS obligation for personas físicas**: Personas físicas with actividades profesionales (autónomas) pay IMSS voluntarily (seguro voluntario) or have no mandatory IMSS obligation (unless registered as patron). Mandatory regime applies when they have employees.
- **Voluntary IMSS deductibility**: Voluntary IMSS contributions: deductible in Declaración Anual as deducciones personales.

### Tier 1 rules (apply without exception)

### T1-MX-1: Always strip IVA before ISR computation

- **T1-MX-1**: Mexican professional services carry 16% IVA. All income and expense figures for ISR purposes must be ex-IVA (subtotal on CFDI). IVA is collected and remitted separately. Never include IVA in ISR base calculations.

### T1-MX-2: No CFDI = no deduction

- **T1-MX-2**: Under LISR, deductible expenses require a valid CFDI (Comprobante Fiscal Digital por Internet) from the supplier with the taxpayer's RFC. Cash payments > MXN 2,000 are explicitly non-deductible. Reject any expense claim without a CFDI.

### T1-MX-3: RESICO prohibits expense deductions

- **T1-MX-3**: RESICO applies a flat rate to gross income without any deductions. Never apply deducciones autorizadas to a RESICO taxpayer. The two regimes are mutually exclusive for the same activity in the same year.

### T1-MX-4: 10% ISR retenido is a credit, not income reduction

- **T1-MX-4**: Clients withholding 10% ISR on honorarios CFDI do not reduce the taxpayer's gross income, they reduce the final tax balance payable. Always gross up received amounts by the 10% retention to compute the income figure, then credit the retention against annual ISR.

### T1-MX-5: Meals deduction: 8.5% cap

- **T1-MX-5**: Restaurant consumption (consumos en restaurantes) deductible at only 8.5% of the CFDI amount (Art. 28 LISR). Apply 8.5% to all restaurant narrations where a CFDI exists. Never apply 100% to meals. The 8.5% is deductible only when paid by card or SAT-authorised e-wallet.  _(Art. 28 fr. XX LISR)_

### T1-MX-6: Fuel: electronic payment mandatory

- **T1-MX-6**: Gasoline and diesel expenses are only deductible when paid electronically (CFDI with electronic payment method). Cash fuel purchases are explicitly disallowed. Apply zero deduction to any fuel expense that appears to be a cash purchase.

### T1-MX-7: Pagos provisionales are not deductible

- **T1-MX-7**: Monthly ISR advance payments made to SAT (línea de captura / complemento de pago) are not deductible expenses. They are credits against the annual tax balance.

### Tier 2 catalogue (reviewer judgement required)

| Code | Situation | Escalation Reason | Suggested Treatment |
| --- | --- | --- | --- |
| T2-MX-1 | RESICO vs. Régimen General comparison | Regime choice has major tax impact; cannot be changed mid-year | Present both calculations; advise formal enrollment at SAT for following year |
| T2-MX-2 | Foreign income without retention | No ISR withheld by foreign payer; pago provisional required each month on that income | Compute pagos provisionales on foreign income; flag FX conversion (SAT rates) |
| T2-MX-3 | Subcontractor payments (honorarios a terceros) | If paying a freelancer > MXN 2,000, client must issue CFDI and subcontractor is obligated to emit CFDI | Flag, verify CFDI chain; both CFDIs must exist for the deduction |
| T2-MX-4 | Rental income (arrendamiento) alongside professional | Capítulo III income; different pago provisional regime and deductions | Flag, separate the two income streams in Declaración Anual |
| T2-MX-5 | Vehicle expenses (deducción de automóvil) | Cars deductible up to MXN 175,000 purchase value; annual depreciation 25% (Art. 34 fr. VI); strict fuel rules | Flag, vehicle deduction calculations require SAT-compliant depreciation schedule |
| T2-MX-6 | Prior-year tax losses (pérdidas fiscales) | Losses can offset income for up to 10 years with inflation adjustment | Flag, review prior-year declaraciones for carryforward losses |

### CFDI Cross-Reference

- **CFDI Cross-Reference**: Always cross-reference bank statement credits with CFDI de ingresos in SAT portal: - SAT Portal: cfdiv4.sat.gob.mx → "Factura Electrónica" → "Consultar CFDI emitidos" - Confirm total CFDI subtotals (ex-IVA) = bank statement gross receipts - Gaps may indicate income received outside CFDI obligations

## Deadlines and filing

### Filing deadlines

| Deadline | Event |
| --- | --- |
| Day 17 of each month | Pago provisional ISR for prior month |
| Day 17 of each month | IVA monthly payment |
| April of the following year (April 2027 for 2026) | Declaración Anual PF (Régimen General), LISR Art. 150 |
| April (following year) | Declaración Anual RESICO due in April (LISR Art. 113-F) |

Pagos provisionales are due by the 17th of the following month (LISR Art. 106). The annual return for Régimen General is filed in April of the following year (LISR Art. 150). RESICO taxpayers file monthly by the 17th (Art. 113-E) and an annual return in April (Art. 113-F).

### Where to file and check

- SAT Portal: sat.gob.mx
- Mi Portal SAT: portalsat.plataforma.sat.gob.mx
- CFDI validation: verificacfdi.facturaelectronica.sat.gob.mx
- Exchange rates (SAT): sat.gob.mx/consultas/18038/consulta-de-tipo-de-cambio
- RESICO enrollment: sat.gob.mx → "Trámites" → "RFC y obligaciones"

## Penalties and interest

No penalty, recargo or interest figure is confirmed in this skill yet; see the "Not yet confirmed" line under Sources. The red flags below mark the situations that lead to multas and recargos or SAT scrutiny.

### Red Flag Thresholds

**Red Flag Thresholds**

| Flag | Threshold |
| --- | --- |
| Gross income > MXN 3,500,000 | RESICO not available: Régimen General mandatory |
| No CFDI emitted for services | SAT audit risk: CFDI de honorarios required for every PJ client |
| No pagos provisionales | Multa and recargos, verify monthly obligations met |
| Cash income without CFDI | Non-deductible for client; high SAT scrutiny for taxpayer |
| One client paid more than 50% of prior-year professional income and the work is done at that client's premises | Fees are treated as wages (asimilados) under LISR Art. 94 fr. V; check before invoicing the year |

## Cross-border points

- **Foreign client income** is taxable in Mexico; the foreign payer withholds no Mexican ISR, so pagos provisionales are due on it each month (R-MX-4, T2-MX-2).
- **Currency conversion:** convert foreign-currency receipts at the SAT-published exchange rate for the date of each receipt (see the onboarding wording under Ask the client first).
- **Foreign tax credit:** foreign tax withheld on that income may be credited against Mexican ISR (LISR Art. 5); flag for treaty review (Example 4).

## Worked examples

Example 1 (Régimen General, 2026 tariff) and Example 2 (RESICO) carry the recomputing `oa-check` blocks. The bank-statement walkthroughs after them are kept from earlier versions of this skill and use the **2025** tariff (2025 returns filed in April 2026). All client facts (names, banks, amounts) in the examples are hypothetical; the only real figures are the tariff and RESICO rates from the confirmed tables above.

### Worked example 1: Banamex / Citibanamex (Monterrey, Architect, Régimen General)

**Bank:** Banamex statement
**Client:** Ricardo Vega, architect, Monterrey, Régimen General

Complex deductions:
- Studio rent (commercial): MXN 84,000/yr → require CFDI arrendamiento
- AutoCAD / BIM software: MXN 18,000 → CFDI
- Subcontractor (structural engineer): MXN 120,000 → require CFDI honorarios

Gross income: MXN 800,000
Total deductions: MXN 300,000 (including subcontractor)
Taxable: MXN 500,000

ISR (2026 tariff): MXN 67,981.92 + (MXN 500,000 − MXN 424,353.98) × 23.52%
= MXN 67,981.92 + MXN 75,646.02 × 23.52%
= MXN 67,981.92 + MXN 17,791.94 = **MXN 85,773.86**

(On the 2025 tariff the same income gave MXN 89,487.53; the 2026 update lowers it by MXN 3,713.67.)

Flag: Subcontractor paid MXN 120,000, did Ricardo issue CFDI to subcontractor? If subcontractor has RFC and Andrés is acting as client, no issue. But if Ricardo paid as employer, IMSS and payroll taxes may apply.

```oa-check
name: MX Régimen General annual ISR, taxable income MXN 500,000 (2026 tariff)
inputs:
  taxable: 500000
  lower_limit: 424353.98
  fixed_fee: 67981.92
  rate: 0.2352
steps:
  - excess: taxable - lower_limit
  - marginal_tax: excess * rate
  - isr: fixed_fee + marginal_tax
expected:
  excess: 75646.02
  marginal_tax: 17791.94
  isr: 85773.86
```

### Worked example 2: Santander México (Guadalajara, Developer: RESICO)

**Bank:** Santander Cuenta Digital
**Client:** Sofía Ramírez, software developer, Guadalajara, enrolled in RESICO

Gross income (all CFDI invoiced): MXN 480,000 (ex-IVA)
RESICO bracket: MXN 300,001–600,000 → 1.10%

Annual ISR RESICO: MXN 480,000 × 1.10% = **MXN 5,280**

Key points:
- No deducciones autorizadas allowed under RESICO
- Monthly pago provisional: (monthly income) × 1.10% via SAT portal
- Annual declaration filed in April of the following year at the Art. 113-F annual table (monthly ISR paid is credited)
- IVA still applies separately (collect 16%, remit to SAT)

```oa-check
name: MX RESICO annual ISR, income MXN 480,000 (LISR Art. 113-F table)
inputs:
  income: 480000
  rate: 0.011
steps:
  - isr: income * rate
expected:
  isr: 5280.00
```

### Further bank-statement walkthroughs

#### Worked example 3: BBVA México (CDMX, Marketing Consultant: Régimen General)

**Bank:** BBVA Bancomer CoDi/SPEI statement
**Client:** Andrés Torres, marketing consultant, CDMX, Régimen de Actividades Profesionales

```
Fecha;Concepto;Cargo;Abono;Saldo
05/01/2025;SPEI DE EMPRESA ALPHA SA DE CV;;87500.00;
15/01/2025;COMISION BANCARIA;150.00;;
10/02/2025;SPEI DE MARKETING CORP SA;;57500.00;
28/02/2025;TELMEX PAGO;850.00;;
15/03/2025;STRIPE PAYMENTS MEXICO;;34800.00;
01/04/2025;ADOBE CREATIVE CLOUD MEXICO;1250.00;;
20/04/2025;SPEI DE BETA CONSULTORES SC;;69000.00;
15/06/2025;PAGO PROVISIONAL ISR SAT;12500.00;;
10/07/2025;DESPACHO CONTABLE GOMEZ;4640.00;;
10/10/2025;AEROMEXICO MONTERREY;3480.00;;
```

**Step 1: Income (ex-IVA)**

| Narration | Pattern | Received | IVA (if incl.) | Ex-IVA Gross |
| --- | --- | --- | --- | --- |
| SPEI DE EMPRESA ALPHA | I-01 | MXN 87,500 | ÷ 1.16 if incl. | MXN 75,431 |
| SPEI DE MARKETING CORP | I-01 | MXN 57,500 |  | MXN 49,569 |
| STRIPE PAYMENTS MX | I-04 | MXN 34,800 | gross-up | ~MXN 35,900 |
| SPEI DE BETA CONSULTORES | I-01 | MXN 69,000 |  | MXN 59,483 |

Note: If amounts received are already net of IVA that Andrés already remitted to SAT, the ex-IVA gross = CFDI subtotal. Confirm with CFDI records. For simplicity, assume SPEI amounts are already net received after clients withheld 10% ISR.

Gross income from CFDIs (annualised): MXN 520,000
IRSR retenido 10% by PJ clients: MXN 52,000

**Step 2: Deducciones Autorizadas**

| Concept | Amount | Deductible |
| --- | --- | --- |
| TELMEX (80% business) | MXN 10,200/yr × 80% = MXN 8,160 | MXN 8,160 |
| ADOBE | MXN 15,000/yr | MXN 15,000 |
| DESPACHO CONTABLE | MXN 55,680/yr | MXN 55,680 |
| AEROMEXICO (business trip) | MXN 3,480 | MXN 3,480 |
| COMISION BANCARIA | MXN 1,800/yr | MXN 1,800 |
| STRIPE FEES | ~MXN 1,100 | MXN 1,100 |
| PAGO PROVISIONAL ISR | MXN 12,500 | MXN 0 |
| **Total deducciones** |  | **MXN 85,220** |

```
Gross income:         MXN 520,000
Less deducciones:     MXN  85,220
Taxable income:       MXN 434,780
```

```
Bracket: MXN 374,837.89 – MXN 590,795.99
Fixed fee:         MXN 60,049.40
(434,780 − 374,837.89) × 23.52% = MXN 59,942.11 × 23.52% = MXN 14,098.38
ISR gross:         MXN 74,147.78

Less retenciones:  MXN 52,000
Less pagos provisionales: MXN 12,500 × months
ISR balance:       MXN 74,147.78 − MXN 52,000 − MXN [provisional total]
```

#### Worked example 4: HSBC México (CDMX, Consultant with Foreign Clients)

**Bank:** HSBC Advance statement
**Client:** Laura Pérez, management consultant, CDMX, 40% of income from US clients (USD)

US client income: USD 24,000 → at SAT exchange rate (~MXN 17.50) = MXN 420,000
Note: No ISR retention made by US client. Laura must pay pagos provisionales on this income each month.

Domestic PJ income: MXN 280,000 (with 10% retention = MXN 28,000 withheld)

Total gross: MXN 700,000
Deducciones: MXN 95,000
Taxable: MXN 605,000

ISR: MXN 110,842.74 + (MXN 605,000 − MXN 590,796) × 30% = MXN 110,842.74 + MXN 4,261.20 = **MXN 115,103.94**

Foreign tax credit: If US withholding tax was paid, may credit against Mexican ISR (Art. 5 LISR). Flag for treaty review.

#### Worked example 5: Banorte (Puebla, Physician)

**Bank:** Banorte statement
**Client:** Dr. Martín Cruz, physician, Puebla, hospital PJ fees + private patients (PF)

Hospital PJ (CFDI emitidos): MXN 360,000; 10% ISR retenido = MXN 36,000
Private patients (PF, no retention): MXN 120,000, pagos provisionales required

Total gross: MXN 480,000
Deductions: consulting room rent MXN 36,000, medical equipment depreciation MXN 24,000, professional insurance MXN 8,400, accounting MXN 18,000 = MXN 86,400

Taxable: MXN 480,000 − MXN 86,400 = MXN 393,600

ISR: MXN 60,049.40 + (MXN 393,600 − MXN 374,837.89) × 23.52%
= MXN 60,049.40 + MXN 18,762.11 × 23.52% = MXN 60,049.40 + MXN 4,412.85 = **MXN 64,462.25**

Deducciones personales: gastos médicos propios MXN 12,000 + colegiaturas hijo MXN 8,900 = MXN 20,900 (reduces ISR ~ MXN 4,000 at marginal rate).

#### Worked example 6: Nu México / Hey Banco (CDMX, Freelance Designer)

**Bank:** Nu México statement (digital bank)
**Client:** Valentina Cruz, graphic designer, CDMX, multiple small PF clients + one PJ

Nu México narrations:
- `Transferencia recibida de [client name]`: PF clients
- `SPEI recibido de EMPRESA X SA DE CV`: PJ client

PF income (no retention): MXN 90,000, pagos provisionales required monthly
PJ income (10% retention): MXN 60,000; retention = MXN 6,000

Total gross: MXN 150,000
RESICO check: MXN 150,000 < MXN 3,500,000 → RESICO available
RESICO rate at MXN 150,000: 1.00%
RESICO ISR: MXN 150,000 × 1.00% = **MXN 1,500**

vs. Régimen General:
Deductions ~MXN 20,000; taxable MXN 130,000
ISR (bracket MXN 133,536.08 at 16%): MXN 10,723.55 + (130,000 − 133,536 → below bracket; use MXN 75,984.56–133,536.07 at 10.88%): MXN 4,461.94 + (MXN 130,000 − MXN 75,984.56) × 10.88% = MXN 4,461.94 + MXN 5,876.88 = MXN 10,338.82 − retención MXN 6,000 = MXN 4,338.82

RESICO (MXN 1,500) significantly better → recommend RESICO (client must be formally enrolled). Under RESICO the PJ client withholds 1.25% (MXN 750), not 10% (LISR Art. 113-J).

### Excel working paper template

```
MEXICAN ISR WORKING PAPER (PERSONA FÍSICA: ACTIVIDADES PROFESIONALES)
Taxpayer: _______________  RFC: _______________  FY: 2025

SECTION A: INCOME (INGRESOS COBRADOS, EX-IVA)
                                        MXN
Domestic PJ clients (CFDI issued):    ___________
Domestic PF clients (pagos provisionales): ________
Foreign income (converted at SAT rate): ___________
Platform payouts (grossed up, ex-IVA): ___________
TOTAL GROSS INCOME                     ___________

SECTION B: DEDUCCIONES AUTORIZADAS (LISR Art. 105)
(Only for Régimen General: NOT for RESICO)
Office rent (CFDI required):           ___________
Utilities (business proportion, CFDI): ___________
Phone/internet (%, CFDI):              ___________
Software subscriptions (CFDI):         ___________
Accounting/legal fees (CFDI):          ___________
Air travel (CFDI, business purpose):   ___________
Accommodation (CFDI):                  ___________
Restaurant meals (8.5% of CFDI):       ___________
Fuel (electronic payment only, CFDI):  ___________
Vehicle depreciation (to MXN 175k cap):___________
Training/CPD (CFDI):                   ___________
Office supplies (CFDI):                ___________
Bank commissions (CFDI):               ___________
Subcontractor payments (CFDI):         ___________
TOTAL DEDUCCIONES                      ___________

SECTION C: ISR BASE
Gross income − Deducciones             ___________

SECTION D: ISR CALCULATION (Régimen General)
ISR at bracket rates:                  ___________
RESICO check (if applicable):          ___________

SECTION E: TAX CREDITS
ISR retenido (10% by PJ clients):      (___________)
Pagos provisionales paid:              (___________)
ISR BALANCE DUE / (REFUND)             ___________

SECTION F: DEDUCCIONES PERSONALES (Declaración Anual)
Medical/dental/hospital (CFDI):        ___________
Medical insurance (CFDI):              ___________
Education/colegiaturas (CFDI):         ___________
Other personales:                      ___________
Cap check (15% of gross or 5 UMA):     ___________

SECTION G: REVIEWER FLAGS
[ ] IVA stripped from all income/expense figures?
[ ] CFDI verified for every deducción autorizada?
[ ] Cash fuel purchases excluded (non-deductible)?
[ ] Restaurant meals limited to 8.5%?
[ ] RESICO vs. Régimen General comparison done?
[ ] Retenciones certificates collected from all PJ clients?
[ ] Pagos provisionales reconciled vs. SAT account?
[ ] Foreign income converted at SAT publication rate?
[ ] CFDI de honorarios emitidos match total income?
```

### Bank statement export formats

#### BBVA México

- Export: CSV/Excel via "Mis Finanzas" → "Descargar movimientos"
- Columns: `Fecha;Concepto;Cargo;Abono;Saldo`
- Amount format: no thousands separator, period decimal (varies) or comma depending on locale
- Date: DD/MM/YYYY
- SPEI credits: `SPEI DE [RFC/name] [reference]`; CoDi: `CoDi COBRO`

#### Santander México

- Export: CSV/PDF from Santander Online
- Columns: `Fecha;Descripción;Monto;Saldo`
- Positive Monto = credit; negative = debit (or separate columns)
- SPEI narrations: `TRANSF SPEI DE [name]`

#### Banamex (Citibanamex)

- Export: PDF or XLS from Banca en Línea
- Columns: `Fecha;Descripción;Retiros;Depósitos;Saldo`
- Deposits = credits; Retiros = debits

#### Banorte

- Export: CSV/Excel from Banorte En Línea
- Standard format: `Fecha;Movimiento;Cargo;Abono;Saldo`

#### HSBC México

- Export: CSV from HSBC Personal Banking portal
- Columns: `Fecha;Descripción;Débitos;Créditos;Saldo`

#### Nu México (Nubank México)

- Export: CSV from Nu app ("Movimientos" → export)
- Simple format: `Fecha,Descripción,Valor`
- Positive = credit; negative = debit; period decimal

#### Hey Banco / Clip / Konfio (digital banks)

- Export varies; typically CSV with `Fecha;Concepto;Monto;Tipo` (CARGO/ABONO)

## Ask the client first

1. **Which regime is the client in: RESICO or Régimen General?** It decides the whole computation.
2. **Do income figures include IVA?** Strip 16% IVA before computing ISR.
3. **Is there a CFDI for every expense to be deducted?** No CFDI, no deduction.
4. **Which clients withheld 10% ISR, and are the retention certificates on file?**
5. **Any foreign-client income, and were pagos provisionales paid on it?**
6. **Were pagos provisionales paid by the 17th each month?**

### Required Inputs

Before computing Mexican ISR, collect:

1. **Total gross income** (ingresos cobrados), all amounts received, ex-IVA, for the fiscal year
2. **CFDI de honorarios emitidos**: all CFDIs issued to clients (SAT portal or accounting system)
3. **Retenciones comprobantes**: withholding certificates from PJ clients (10% ISR)
4. **Pagos provisionales made**: monthly ISR payments (línea de captura / recibos from SAT)
5. **Deducciones autorizadas**: documented expenses with CFDI de proveedores
6. **Deducciones personales**: medical, dental, hospital, education, mortgage, IMSS voluntary (with CFDI/facturas)
7. **Bank statements**: 12 months of the fiscal year
8. **RFC**: client's Registro Federal de Contribuyentes
9. **Declaración anual prior year** (if available), to verify prior pagos provisionales and carryforward losses
10. **RESICO status**: confirm if enrolled in RESICO or Régimen de Actividades Empresariales y Profesionales

### Conservative Defaults

**Conservative Defaults**

| Situation | Default Assumption |
| --- | --- |
| RESICO vs. Régimen General unclear | Flag, regime determines entire calculation approach |
| IVA included in income figures | Strip 16% IVA before ISR computation |
| Retention rate unclear (PJ client) | Apply 10% ISR retention as default |
| Deducción autorizada without CFDI | Reject, no CFDI = not deductible under SAT rules |
| Pago provisional amount unknown | Estimate using monthly bracket table; flag for actual |
| Foreign client income (no RFC) | Treat as taxable; no retention from foreign payer; pagos provisionales required |

### Refusal Catalogue

**Refusal Catalogue**

| Code | Situation | Action |
| --- | --- | --- |
| R-MX-1 | Client in RESICO but claims deducciones autorizadas | Stop: RESICO does not allow expense deductions; apply gross income × rate only |
| R-MX-2 | No CFDI for claimed expense > MXN 2,000 | Reject expense: SAT requires CFDI for all deductible expenses; cash payments > MXN 2,000 not deductible |
| R-MX-3 | Income from employment (asalariado) mixed with professional | Flag, empleos simultáneos con honorarios require careful coordination; employer withholds IRPF; consolidated return required |
| R-MX-4 | Foreign-source income without RFC from payer | Treat as taxable; no retention was made; pago provisional required for each month |
| R-MX-5 | Client claiming RIF (Régimen de Incorporación Fiscal) | RIF was abolished January 2022, now RESICO; stop if client still references RIF |

- **R-MX-1**: Client in RESICO but claims deducciones autorizadas  _(Stop: RESICO does not allow expense deductions; apply gross income × rate only)_
- **R-MX-2**: No CFDI for claimed expense > MXN 2,000  _(Reject expense: SAT requires CFDI for all deductible expenses; cash payments > MXN 2,000 not deductible)_
- **R-MX-3**: Income from employment (asalariado) mixed with professional  _(Flag, empleos simultáneos con honorarios require careful coordination; employer withholds IRPF; consolidated return required)_
- **R-MX-4**: Foreign-source income without RFC from payer  _(Treat as taxable; no retention was made; pago provisional required for each month)_
- **R-MX-5**: Client claiming RIF (Régimen de Incorporación Fiscal)  _(RIF was abolished January 2022, now RESICO; stop if client still references RIF)_

### Onboarding fallback

**RESICO vs. Régimen General:**
> "Before I compute your ISR, I need to confirm which regime you are in: RESICO (Régimen Simplificado de Confianza) or Régimen de Actividades Empresariales y Profesionales (Régimen General). RESICO applies a flat rate to gross income (no expense deductions), while Régimen General allows deductions but uses higher rates. If your annual income is below MXN 3,500,000, both may be available. Check your RFC status on the SAT portal to confirm your current enrollment."

**Missing CFDI:**
> "To deduct any expense under Mexican tax law, a valid CFDI (Comprobante Fiscal Digital por Internet) is mandatory. For each expense you want to deduct, please provide the CFDI PDF or XML. Without a CFDI, the expense cannot be included regardless of the bank statement entry. Cash payments above MXN 2,000 are specifically excluded by LISR."

**No pagos provisionales:**
> "Personas físicas with actividades profesionales must make monthly advance ISR payments (pagos provisionales) by the 17th of each following month. Do you have confirmation of payments made on your SAT account? If payments were missed, we need to calculate the recargos (interest) and multas that apply. You can check your SAT account at satid.sat.gob.mx."

**Foreign income:**
> "I see payments from foreign clients. These amounts must be: (1) converted to MXN at the SAT-published exchange rate for the date of each receipt, and (2) included in monthly pagos provisionales since the foreign payer does not withhold Mexican ISR. Do you have bank records showing the MXN equivalent received, or can you provide the dates and foreign currency amounts?"

## Sources

| Source | URL | Read on |
|---|---|---|
| SAT, Resolución Miscelánea Fiscal 2026, Anexo 8 (DOF 28-12-2025): annual tariffs for 2025 (C.I) and 2026 (C.II), monthly Art. 96 tariff for 2026 (A.V); sat.gob.mx timed out, read from the Internet Archive copy | https://www.sat.gob.mx/minisitio/NormatividadRMFyRGCE/documentos2026/rmf/anexos/Anexo-8-RMF-2026_DOF-28122025.pdf | 2026-10-29 |
| SAT, Resolución Miscelánea Fiscal 2025, Anexo 8 (ISR tariffs for 2025, incl. the annual tariff for LISR Art. 152) | http://omawww.sat.gob.mx/normatividad_RMF_RGCE/Paginas/documentos2025/rmf/anexos/Anexo8_RMF2025-30122024.pdf | 2026-10-28 |
| Ley del Impuesto Sobre la Renta, consolidated (Cámara de Diputados, last reform DOF 01-04-2024), Arts. 5, 27, 28, 34, 36, 94, 106, 113-E, 113-F, 113-J, 150, 151 (still last reformed DOF 01-04-2024 in the October 2026 copy) | https://www.diputados.gob.mx/LeyesBiblio/pdf/LISR.pdf | 2026-10-29 |
| Ley del Impuesto al Valor Agregado, consolidated (Cámara de Diputados), 16% general rate | https://www.diputados.gob.mx/LeyesBiblio/pdf/LIVA.pdf | 2026-10-28 |

Not yet confirmed: whether a RESICO taxpayer may combine RESICO with Régimen General in the same year; the 2/3 IVA retention (10.667% of the invoice) by corporate clients and the same obligation for individual clients with business activity; the colegiaturas caps by education level (v2.2 carried "preparatoria MXN 14,200" and said the LIF sets them; the caps come from a presidential decree of fiscal incentives, not read here) and the peso value of the 5-UMA overall cap; deductibility of voluntary IMSS contributions as deducciones personales and the IMSS position of self-employed persons; the SAT pre-filled proposal timing; multas and recargos for missed pagos provisionales; the ~MXN 17.50 exchange rate in Example 4 (a hypothetical client fact); the bank export formats and narrations (not statutory); the reference to "IRPF" in R-MX-3 (a Spanish term; Mexico's employer withholding is ISR).

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
