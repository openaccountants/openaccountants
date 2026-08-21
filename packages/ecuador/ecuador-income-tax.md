---
name: ecuador-income-tax
description: Use this skill whenever asked about Ecuador personal income tax (Impuesto a la Renta) for self-employed individuals and natural persons. Trigger on phrases like "how much income tax do I pay in Ecuador", "Impuesto a la Renta", "Formulario 102", "Formulario 102A", "declaración de renta personas naturales", "gastos personales", "rebaja por gastos personales", "RIMPE", "Negocio Popular", "Emprendedor", "aporte IESS", "décimo tercero", "décimo cuarto", "fondos de reserva", "noveno dígito", "self-employed tax Ecuador", "non-resident 25%", or any question about filing or computing income tax for a self-employed person, professional, or individual resident/non-resident in Ecuador. Also trigger when preparing or reviewing a Formulario 102/102A, the Anexo de Gastos Personales, an IESS contribution computation, or advising on the RIMPE simplified regime. This skill covers the progressive 0%-37% PIT table, the personal-expense rebate, IESS contributions, the 13th/14th salaries, RIMPE, residency, penalties, and interaction with IVA and social security. ALWAYS read this skill before touching any Ecuador income tax work.
version: 0.1
jurisdiction: EC
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ecuador Income Tax -- Personas Naturales / Self-Employed

## Ecuador Income Tax -- Personas Naturales / Self-Employed Skill v0.1

Tier 2 (research-verified). NOT yet accountant-verified. The 2026 PIT table is read verbatim from the official SRI Resolution NAC-DGERCGC25-00000043 PDF (high confidence). The 2025 table and several social-security / gastos-personales figures rely on Big-4 (PwC) and reputable Ecuadorian sources (JEZL, Russell Bedford, HLB Ecuador) rather than line-by-line re-extraction of the original SRI resolutions; those points carry inline [RESEARCH GAP — reviewer to confirm] markers. A licensed Ecuadorian contador/CPA must sign off before filing.

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Ecuador (República del Ecuador) |
| Tax | Impuesto a la Renta -- Personas Naturales (Personal Income Tax) |
| Currency | USD only -- Ecuador is officially dollarized; the US dollar is legal tender |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Ley de Régimen Tributario Interno (LRTI), art. 36 (PIT tables), art. 100 (late-filing fine) |
| Supporting legislation | Reglamento para la Aplicación de la LRTI; Código Tributario (art. 21 interest; sanciones); Ley de Seguridad Social (IESS); Código del Trabajo (13th/14th salary, fondos de reserva); RIMPE rules in LRTI |
| Tax authority | Servicio de Rentas Internas (SRI) -- https://www.sri.gob.ec |
| Social security authority | Instituto Ecuatoriano de Seguridad Social (IESS) -- https://www.iess.gob.ec |
| Minimum wage authority | Ministerio del Trabajo -- https://www.trabajo.gob.ec |
| Filing portal | SRI en línea |
| Annual PIT return | Formulario 102 / 102A (Personas Naturales) |
| Filing deadline | March of the following year, staggered by ninth digit of cédula/RUC (SRI) |
| Validated by | Pending -- requires sign-off by a licensed Ecuadorian contador/CPA |
| Validation date | Pending |
| Skill version | 0.1 |

### Tax Rate Brackets -- General Regime (Personas Naturales)

- **PIT progressivity and indexation** — PIT is progressive 0%-37% on net taxable income. The table is indexed annually to the urban CPI (INEC) at 30 November; the 2026 indexation was 1.0534712934405%.  _(LRTI art. 36; SRI Resolution NAC-DGERCGC25-00000043)_

**2025 (fiscal year filed March 2026) PIT brackets**  _(SRI Resolution NAC-DGERCGC24-00000041, applies from 2025-01-01; exempt base USD 12,081. Source: SRI; JEZL Auditores; PwC. [RESEARCH GAP — reviewer to confirm the 2025 bracket figures line-by-line against the original 2024 SRI resolution PDF, which was binary-encoded.])_

| Net taxable income (USD) | Tax on base (USD) | Marginal rate | Cumulative tax at top |
| --- | --- | --- | --- |
| 0 -- 12,081 | 0 | 0% | USD 0 |
| 12,081 -- 15,387 | 0 | 5% | USD 165 |
| 15,387 -- 19,978 | 165 | 10% | USD 624 |
| 19,978 -- 26,422 | 624 | 12% | USD 1,398 |
| 26,422 -- 34,770 | 1,398 | 15% | USD 2,650 |
| 34,770 -- 46,089 | 2,650 | 20% | USD 4,914 |
| 46,089 -- 61,359 | 4,914 | 25% | USD 8,731 |
| 61,359 -- 81,817 | 8,731 | 30% | USD 14,869 |
| 81,817 -- 108,810 | 14,869 | 35% | USD 24,316 |
| 108,810 + | 24,316 | 37% | -- |

**2026 (applies from 2026-01-01) PIT brackets**  _(SRI Resolution NAC-DGERCGC25-00000043 (signed 2025-12-29); exempt base USD 12,208; confirmed verbatim from the official SRI PDF.)_

| Net taxable income (USD) | Tax on base (USD) | Marginal rate | Cumulative tax at top |
| --- | --- | --- | --- |
| 0 -- 12,208 | 0 | 0% | USD 0 |
| 12,208 -- 15,549 | 0 | 5% | USD 167 |
| 15,549 -- 20,188 | 167 | 10% | USD 631 |
| 20,188 -- 26,700 | 631 | 12% | USD 1,412 |
| 26,700 -- 35,136 | 1,412 | 15% | USD 2,678 |
| 35,136 -- 46,575 | 2,678 | 20% | USD 4,965 |
| 46,575 -- 62,005 | 4,965 | 25% | USD 8,823 |
| 62,005 -- 82,679 | 8,823 | 30% | USD 15,025 |
| 82,679 -- 109,956 | 15,025 | 35% | USD 24,572 |
| 109,956 + | 24,572 | 37% | -- |

- **How to compute tax in any bracket** — tax = (tax on base) + (net taxable income − bracket floor) × marginal rate. Then subtract the personal-expense rebate (see Section 1, Personal-Expense Rebate). Never compute tax directly in prose -- pass the chargeable figure to the deterministic engine.
- **Non-residents flat rate** — 25% percent (flat, on Ecuadorian-source income, withheld at source, NO brackets and NO personal allowance)  _(PwC Worldwide Tax Summaries -- Ecuador Individual)_

### IESS Social Security Contributions

- **Materia gravada base definition** — Base = materia gravada (salary + habitual remuneration: commissions, overtime, etc.). Floor = 1 SBU. No upper ceiling.  _(IESS Tasas de Aportación (as reported by EcuadorLegalOnline; misalario.ec). [RESEARCH GAP — the IESS official PDF was binary/unreadable; the 9.45% / 11.15% / 20.50% rates rely on EcuadorLegalOnline and misalario.ec, not the IESS document itself; fund-by-fund split (IVM/salud/riesgos/cesantía) not obtained — reviewer to confirm.])_

**Private-sector dependent worker contributions**

| Contribution | Payer | Rate | Base |
| --- | --- | --- | --- |
| Aporte personal (employee) | Employee | 9.45% | materia gravada, floor 1 SBU, no ceiling |
| Aporte patronal (employer) | Employer | 11.15% | same materia gravada |
| **Total (private-sector dependent)** | **Employee + Employer** | **20.60%** | **(9.45% + 11.15%)** |

**Other IESS situations**

| Situation | Payer | Rate | Notes |
| --- | --- | --- | --- |
| Afiliado voluntario / independiente (self-employed, no labour relationship) | Self (full amount) | 20.50% | On declared income, floor 1 SBU; relevant for self-employed not under dependency |
| Public sector (reference only) | Worker 11.45% / State 9.15% | -- | Split differs from private sector [RESEARCH GAP — reviewer to confirm] |
| Fondos de Reserva (Reserve Fund) | Employer | 8.33% | Paid from the worker's 13th month of continuous service (= one month's pay / 12); monthly or accumulated at IESS at the worker's choice (Código del Trabajo) |

### Key Payroll / Benefit Items

**Payroll / benefit items 2025/2026**

| Item | 2025 | 2026 | Source |
| --- | --- | --- | --- |
| Salario Básico Unificado (SBU / minimum wage) | USD 470.00/month | USD 482.00/month (Acuerdo Ministerial MDT-2025-195, from 2026-01-01) | Ministerio del Trabajo; NMS Law; CorralRosales |
| Décimo Tercer Sueldo (13th salary / Christmas bonus) | = 1/12 of total remuneration earned 1 Dec–30 Nov; paid by 24 Dec | same | EXEMPT from PIT; NOT part of IESS base (Código del Trabajo; PwC) |
| Décimo Cuarto Sueldo (14th salary / education bonus) | = 1 SBU (USD 470) | = 1 SBU (USD 482) | EXEMPT from PIT; paid by 15 Mar (Costa/Insular) or 15 Aug (Sierra/Amazonía) (Código del Trabajo) |
| IESS remittance deadline | within 15 days following the worked month | same | EcuadorLegalOnline |

### Personal-Expense Rebate (Rebaja por Gastos Personales)

- **Rebate formula** — rebate = 18% × the lesser of (a) declared documented personal expenses, or (b) the canasta cap  _(SRI; Russell Bedford; HLB Ecuador; Buró Tributario)_

**Canasta multiplier and caps by dependents**

| Dependents | Canasta multiplier | 2025 cap (canasta USD 798.31) | 2026 cap (canasta USD 821.80) |
| --- | --- | --- | --- |
| 0 (base case) | 7 canastas | ≈ USD 5,588.17 → max rebate ≈ USD 1,005.87 | ≈ USD 5,752.60 → max rebate ≈ USD 1,035.47 |
| 1 | 9 canastas | [RESEARCH GAP — per-dependent USD cap for 2025 not extracted line-by-line] | ≈ USD 7,396.20 (9 × 821.80) |
| 2 | 11 canastas | [RESEARCH GAP] | ≈ USD 9,039.80 |
| 3 | 14 canastas | [RESEARCH GAP] | ≈ USD 11,505.20 |
| 4 | 17 canastas | [RESEARCH GAP] | ≈ USD 13,970.60 |
| 5+ | 20 canastas | [RESEARCH GAP] | ≈ USD 16,436.00 |

The canasta-multiplier structure (7/9/11/14/17/20) is sourced from HLB Ecuador for 2026; the same structure applies in 2025 with canasta USD 798.31 (Russell Bedford), but the exact per-dependent USD caps for 2025 were not extracted from an SRI boletín. Canasta básica = USD 798.31 (Jan 2025) and USD 821.80 (Jan 2026).

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown regime (general vs RIMPE) | General-regime art. 36 table -- apply RIMPE ONLY if the individual is registered in RIMPE and within the revenue band (≤ USD 300,000) |
| Unknown residency | Treat as fiscally resident (worldwide income) ONLY if 183-day test met; otherwise flat 25% on Ecuadorian-source income |
| Unknown dependents for rebate | No-dependents case (7 canastas) |
| Unknown personal-expense documentation | Rebate = 18% of declared expenses (lesser value); 0 if no documented expenses |
| 13th / 14th salaries | EXCLUDE from taxable income and from the IESS base |
| Self-employed not under labour dependency | Model IESS as the 20.50% voluntary/independent rate on declared income (min 1 SBU), NOT the 9.45/11.15 split |
| Unknown expense category | Not deductible |
| Unknown year | Use 2025 (current filing year, return due March 2026) |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs** — Bank statement for the full tax year (CSV, PDF, or pasted text), plus confirmation of (a) residency (resident vs non-resident / 183-day test), (b) regime (general vs RIMPE), and (c) number of dependents (for the gastos-personales rebate).
- **Recommended inputs** — All facturas (sales and purchase invoices with RUC), IESS contribution / planilla records, prior-year Formulario 102, RUC registration showing regime, RIMPE category (Negocio Popular vs Emprendedor) if applicable.
- **Ideal inputs** — Complete income and expenditure account, Anexo de Gastos Personales (APS) detail with documented facturas by category (vivienda, salud, educación, alimentación, vestimenta, turismo), 13th/14th salary records, withholding certificates (comprobantes de retención).
- **Refusal if minimum missing** — SOFT WARN. No bank statement at all = hard stop. Bank statement without facturas = proceed with reviewer warning: "This Formulario 102 was produced from bank statement alone. The reviewer must verify that every deductible expense and every gasto personal claimed is supported by a valid factura with RUC, and that residency and regime are correctly determined."

### Refusal Catalogue

- **R-EC-1 -- Residency unknown** — Residency determines the entire computation: residents are taxed on worldwide income at the progressive 0%-37% table; non-residents pay a flat 25% on Ecuadorian-source income with no allowance. This skill cannot compute tax without resolving the 183-day test. Please confirm before proceeding.
- **R-EC-2 -- Companies / partnerships / sociedades** — This skill covers natural persons (personas naturales) and self-employed individuals only. Sociedades, companies, and other legal entities file under the corporate regime (Impuesto a la Renta de Sociedades). Escalate to a licensed Ecuadorian contador.
- **R-EC-3 -- Cross-border / treaty cases** — Worldwide income, foreign tax credits, double-tax treaties, and CAN Decision 578 (Andean Community) require specialised analysis. Out of scope. Escalate to a licensed Ecuadorian contador.
- **R-EC-4 -- Capital gains / property disposals / herencias** — Gains on shares or real property, inheritance/gift tax, and asset disposals require separate analysis. Escalate to a licensed Ecuadorian contador.
- **R-EC-5 -- Arrears / SRI enforcement** — Client has outstanding tax arrears or is subject to SRI enforcement. Interest on mora is variable (Banco Central 90-day reference rate, set quarterly) and a 20% recargo applies where the SRI detects the omission. Do not advise. Escalate immediately.
- **R-EC-6 -- IVA return requested** — This skill covers income tax (Formulario 102/102A) only. For Ecuador IVA, use the ecuador-iva skill.

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank-statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement (Spanish terms common in Ecuadorian statements). If multiple patterns match, use the most specific. If none match, fall through to Tier 1.

### 3.1 Income Patterns (Credits / Créditos on Bank Statement)

**Income patterns table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Client name + TRANSFERENCIA, DEPOSITO, PAGO RECIBIDO, ABONO | Business income (renta gravada) | If IVA-registered, extract net (excl. 15% IVA) |
| HONORARIOS, FACTURA, SERVICIOS PROFESIONALES, CONSULTORIA | Professional fees -- business income | Typical for self-employed professionals |
| STRIPE PAYOUT, PAYPAL, WISE, PAYONEER | Platform payout -- business income | Match to underlying facturas; net of platform commission |
| UPWORK, FIVERR, FREELANCER | Freelance platform -- business income | Net of platform commission |
| SUELDO, ROL DE PAGOS, NOMINA, EMPLEADOR [name] | Employment income (renta del trabajo en relación de dependencia) | NOT self-employment; net of IESS 9.45% and excludes 13th/14th |
| ARRIENDO RECIBIDO, ALQUILER | Rental income | Reported separately (renta de capital) |
| INTERESES, RENDIMIENTOS | Investment income | Interest / yield |
| DIVIDENDOS | Investment income | Dividend income |
| DEVOLUCION SRI, NOTA DE CREDITO SRI | EXCLUDE -- not income | Tax refund from prior period |
| DECIMO TERCERO, DECIMO CUARTO | EXCLUDE -- exempt | 13th/14th salaries are PIT-exempt |
| FONDOS DE RESERVA | EXCLUDE from taxable income | Reserve fund payout [RESEARCH GAP — confirm PIT treatment with reviewer] |

### 3.2 Expense Patterns (Debits) -- Deductible Business Costs (self-employed / professional)

**Deductible business costs table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| ARRIENDO OFICINA, ALQUILER LOCAL | Office rent | Deductible | Must have factura with RUC |
| HONORARIOS CONTADOR, AUDITORIA, ASESORIA | Accountancy / professional fees | Deductible |  |
| HONORARIOS ABOGADO, NOTARIA (business) | Legal fees | Deductible | Must be business-related |
| SUMINISTROS, PAPELERIA, UTILES DE OFICINA | Office supplies | Deductible |  |
| PUBLICIDAD, MARKETING, GOOGLE ADS, META ADS | Marketing / advertising | Deductible |  |
| CAPACITACION, CURSO, SEMINARIO, CONFERENCIA | Training | Deductible | Must relate to current activity |
| COMISIONES BANCARIAS, MANTENIMIENTO CUENTA | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, COMISION PLATAFORMA | Payment-processing fees | Deductible |  |
| HOSTING, DOMINIO, AWS, GOOGLE CLOUD, SOFTWARE | IT infrastructure / SaaS | Deductible (recurring); capitalise if a long-lived asset |  |

### 3.3 Expense Patterns (Debits) -- Utilities (may need apportionment)

**Utilities patterns table**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| EMPRESA ELECTRICA, CNEL, LUZ, AGUA EPMAPS | Electricity / water | T2 if home office | 100% if dedicated office; apportion if home-based |
| CLARO, MOVISTAR, CNT, TUENTI | Telecoms / internet / mobile | T2 | Business-use portion only; default 0% if mixed |

### 3.4 Expense Patterns (Debits) -- Travel

**Travel patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LATAM, AVIANCA, EQUAIR, BOLETO AEREO | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, HOSPEDAJE, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| UBER, CABIFY, DIDI, TAXI | Local transport | Deductible if business purpose |  |
| COMBUSTIBLE, GASOLINA, PRIMAX, PETROECUADOR | Vehicle fuel | T2 -- business % only | Requires mileage log |
| PARQUEADERO, PEAJE | Parking / tolls | T2 -- business % only |  |

### 3.5 Expense Patterns (Debits) -- Gastos Personales (feed the rebate, NOT business expense)

These do not reduce business profit; they feed the **rebaja por gastos personales** (18% of the lesser value -- Section 1). Must have facturas with the taxpayer's RUC/cédula.

**Gastos personales patterns table**

| Pattern | Gasto-personal category | Notes |
| --- | --- | --- |
| ARRIENDO VIVIENDA, HIPOTECA (interés), PREDIO | Vivienda (housing) | Personal residence |
| CLINICA, FARMACIA, MEDICO, SEGURO SALUD | Salud (health) |  |
| COLEGIO, UNIVERSIDAD, MATRICULA, PENSION ESCOLAR | Educación (education) |  |
| SUPERMERCADO, MERCADO, ALIMENTOS | Alimentación (food) | Documented food spend |
| ROPA, CALZADO, VESTIMENTA | Vestimenta (clothing) |  |
| TURISMO, HOTEL (personal), AGENCIA DE VIAJE | Turismo (tourism) |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible / Exclude

**Not deductible patterns table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MULTA, SANCION, INTERES POR MORA | NOT deductible | Fines/penalties -- public policy |
| PAGO SRI, IMPUESTO A LA RENTA | NOT deductible | Income tax cannot reduce income |
| RETIRO PERSONAL, CONSUMO PERSONAL, CAJERO (personal) | NOT deductible | Drawings / private spend |
| DONACION (non-qualifying) | NOT deductible | Unless qualifying under LRTI [RESEARCH GAP — reviewer to confirm] |

### 3.7 Exclusions (Neither Income nor Business Expense)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERENCIA ENTRE CUENTAS PROPIAS, CUENTA AHORRO | EXCLUDE | Own-account transfer |
| PAGO PRESTAMO, CUOTA CREDITO (principal) | EXCLUDE (principal) | Loan principal movement; interest may be deductible if business |
| APORTE IESS, PLANILLA IESS | Treated as IESS contribution | Deductible from employment income (9.45%) or self-employed base, NOT a business cost line |
| PAGO IVA, FORMULARIO 104 | EXCLUDE | IVA liability payment, not an expense |
| ANTICIPO IMPUESTO RENTA, RETENCION EN LA FUENTE | Credit against liability | Withholding/advance -- not an expense |

### 3.8 Ecuadorian Banks -- Statement Format Reference

**Banks statement format reference table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Banco Pichincha | TRANSFERENCIA, DEBITO, NOTA DE DEBITO, COMISION | PDF/Excel; date format DD/MM/YYYY |
| Banco Guayaquil | TRANSFERENCIA, PAGO, DEBITO AUTOMATICO | PDF/CSV |
| Banco del Pacífico | TRANSFERENCIA, DEPOSITO, RETIRO | PDF |
| Produbanco | TRANSFERENCIA, DEBITO, COMISION | PDF/CSV |
| Banco Internacional | TRANSFERENCIA, PAGO, CARGO | PDF |

## Section 4 -- Worked Examples

All amounts in USD (Ecuador is dollarized). Tax figures use the 2025 general-regime table unless noted.

### Example 1 -- Self-Employed Professional Fee (Income)

**Input line:**
`15/03/2025 ; PICHINCHA ; TRANSFERENCIA RECIBIDA ; ACME CIA LTDA ; HONORARIOS FACTURA 001-001-000234 ; +1,150.00 ; USD`

**Reasoning:**
Professional fee. If the professional is IVA-registered, USD 1,150 includes 15% IVA → net = USD 1,000 (renta gravada); USD 150 is IVA collected (a liability to the SRI, excluded from income). If not IVA-registered, the full USD 1,150 is income.

**Classification:** Renta gravada = USD 1,000 (IVA-registered) or USD 1,150 (not registered). IVA USD 150 excluded.

### Example 2 -- Self-Employed Annual PIT with Rebate (2025)

**Input:** Resident professional, net taxable income (after deductible business costs and IESS) = USD 30,000. Documented personal expenses ≥ the cap, no dependents.

**Reasoning:**
- USD 30,000 falls in the 26,422–34,770 bracket (15%).
- Tax = 1,398 + (30,000 − 26,422) × 15% = 1,398 + 3,578 × 0.15 = 1,398 + 536.70 = **USD 1,934.70**.
- Personal-expense rebate (no dependents): 18% × min(declared expenses, 7 canastas = 5,588.17) = 5,588.17 × 0.18 = **USD 1,005.87**.
- Tax after rebate = 1,934.70 − 1,005.87 = **USD 928.83**.

**Classification:** Impuesto causado USD 1,934.70; rebaja USD 1,005.87; tax due USD 928.83 (before withholding credits).

### Example 3 -- Employee Monthly IESS Withholding (2025)

**Input line:**
`30/04/2025 ; GUAYAQUIL ; ROL DE PAGOS ; EMPLEADOR XYZ SA ; SUELDO ABRIL ; +1,358.25 ; USD`

**Reasoning:**
Gross monthly salary USD 1,500. Employee IESS aporte personal = 9.45% × 1,500 = USD 141.75. Net deposited to the worker = 1,500 − 141.75 = USD 1,358.25 (before any PIT withholding). The 13th/14th salaries are paid separately and are exempt; they are NOT part of the IESS base.

**Classification:** IESS employee USD 141.75; taxable employment base (this month) USD 1,358.25 before PIT withholding.

### Example 4 -- Non-Resident Ecuadorian-Source Fee

**Input line:**
`10/06/2025 ; PICHINCHA ; TRANSFERENCIA ; CLIENTE EC ; SERVICIOS PRESTADOS EN ECUADOR ; +10,000.00 ; USD`

**Reasoning:**
Payee is a non-resident (183-day test NOT met). Ecuadorian-source income is taxed at a flat 25% withheld at source, with no brackets and no personal allowance (PwC). Tax = 10,000 × 25% = USD 2,500.

**Classification:** Flat 25% non-resident withholding = USD 2,500. No rebate, no table.

### Example 5 -- RIMPE Negocio Popular (Small Self-Employed)

**Input:** Resident natural person, gross annual revenue USD 18,000, registered in RIMPE as Negocio Popular.

**Reasoning:**
Negocio Popular ceiling is gross annual income ≤ USD 20,000 (SRI RIMPE; JEZL). Negocios Populares pay a fixed-fee table (USD 0 / 5 / 15 / 35 / 60 across revenue bands), not the progressive PIT table. [RESEARCH GAP — the exact band thresholds mapping revenue to each fixed fee were not extracted from the SRI RIMPE resolution; reviewer to confirm which fixed fee applies to USD 18,000.] RIMPE income tax is declared in May of the following year (SRI Boletín NAC-COM-25-0020).

**Classification:** RIMPE Negocio Popular fixed fee (USD 0/5/15/35/60) -- exact figure pending reviewer confirmation of the band. NOT the art. 36 table.

### Example 6 -- IESS for Self-Employed Voluntary Affiliate

**Input line:**
`05/02/2025 ; PRODUBANCO ; DEBITO ; IESS ; APORTE VOLUNTARIO ENERO ; -96.35 ; USD`

**Reasoning:**
Self-employed individual not under labour dependency is a voluntary/independent IESS affiliate at 20.50% on declared income, minimum 1 SBU (USD 470 in 2025), paid entirely by the individual. On the SBU floor: 470 × 20.50% = USD 96.35/month.

**Classification:** IESS voluntary contribution USD 96.35 (on SBU floor). Deductible from the self-employed's income base, not a business expense line.

### Example 7 -- Own-Account Transfer (Exclude)

**Input line:**
`15/05/2025 ; PICHINCHA ; TRANSFERENCIA ENTRE CUENTAS PROPIAS ; AHORRO ; ; -2,000.00 ; USD`

**Reasoning:**
Transfer between the taxpayer's own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Progressive PIT, Exempt Base and Filing Obligation

- **Exempt base and filing obligation** — PIT is progressive 0%-37% on net taxable income (LRTI art. 36). The 2025 exempt base is USD 12,081 (SRI Resolution NAC-DGERCGC24-00000041); 2026 is USD 12,208 with the top 37% bracket starting at USD 109,956 (SRI Resolution NAC-DGERCGC25-00000043). Filing obligation: natural persons with gross income above the exempt base (USD 12,081 for 2025, ≈ USD 1,006.75/month) must file the annual return EVEN IF the rebate reduces tax to zero (SRI; Primicias).  _(LRTI art. 36; SRI Resolution NAC-DGERCGC24-00000041; SRI Resolution NAC-DGERCGC25-00000043; SRI; Primicias)_

### 5.2 Taxable Employment Income

- **Taxable employment income definition** — Taxable employment income = total labour compensation NET of employee IESS contributions (9.45%), and EXCLUDING the 13th (Christmas) and 14th (education) salaries, which are exempt. Employers compute monthly PIT withholding on projected annual taxable income (salary net of IESS, excluding 13th/14th) using the art. 36 table, less the projected personal-expense rebate, reconciled annually.  _(LRTI; Código del Trabajo; PwC; Reglamento LRTI)_

### 5.3 Personal-Expense Rebate (Rebaja por Gastos Personales)

- **Rebate formula** — rebate = 18% × the lesser of (a) declared documented personal expenses, or (b) the canasta cap. Cap = 7 canastas with no dependents, scaling to 9/11/14/17/20 canastas for 1/2/3/4/5+ dependents. Canasta básica = USD 798.31 (Jan 2025) and USD 821.80 (Jan 2026). All gastos personales must be backed by facturas with the taxpayer's RUC/cédula. See Section 1 for the full multiplier table and [RESEARCH GAP] markers on the 2025 per-dependent caps.  _(SRI; Russell Bedford; HLB Ecuador)_

### 5.4 Residency and Worldwide Income

- **Residency trigger and effects** — Tax residency triggers at 183 days (consecutive or not) in a fiscal year, OR 183+ days over 12 months spanning two fiscal periods. Residents are taxed on worldwide income with a foreign tax credit (pay the Ecuadorian excess if Ecuador's rate is higher). Non-residents pay only on Ecuadorian-source income at a flat 25% withheld at source.  _(SRI; LRTI art. 4.1; Russell Bedford)_

### 5.5 IESS Contributions

**IESS contributions summary table**

| Worker type | Employee | Employer | Total | Base |
| --- | --- | --- | --- | --- |
| Private-sector dependent | 9.45% | 11.15% | **20.60%** | materia gravada, floor 1 SBU, no ceiling |
| Self-employed voluntary/independent | 20.50% (self) | -- | **20.50%** | declared income, floor 1 SBU |

- **Fondos de Reserva and remittance deadline** — Employer must also pay Fondos de Reserva at 8.33% of remuneration from the worker's 13th month of continuous service (Código del Trabajo). IESS contributions are remitted within 15 days following the worked month (EcuadorLegalOnline). [RESEARCH GAP — IESS official PDF unreadable; rates per EcuadorLegalOnline / misalario.ec.]  _(Código del Trabajo; EcuadorLegalOnline)_

### 5.6 13th and 14th Salaries

- **Décimo Tercer Sueldo** — = 1/12 of total remuneration earned 1 Dec–30 Nov; paid by 24 Dec. EXEMPT from PIT; NOT in IESS base.  _(Código del Trabajo; PwC; EcuadorLegalOnline)_
- **Décimo Cuarto Sueldo** — = 1 SBU (USD 470 in 2025; USD 482 in 2026); paid by 15 Mar (Costa/Insular) or 15 Aug (Sierra/Amazonía). EXEMPT from PIT.  _(Código del Trabajo; PwC; EcuadorLegalOnline)_

### 5.7 Non-Deductible Expenses

**Non-deductible expenses table**

| Expense | Reason |
| --- | --- |
| Fines, penalties, interés por mora | Public policy |
| Income tax itself | Tax on income |
| Drawings / personal consumption | Not a business expense |
| Personal expenses (except via the gastos-personales rebate) | Private living costs feed the rebate, not business profit |

### 5.8 RIMPE Simplified Regime (Small Self-Employed)

**RIMPE categories table**

| RIMPE category | Revenue band (gross annual) | Tax treatment |
| --- | --- | --- |
| Negocio Popular | ≤ USD 20,000 | Fixed-fee table: USD 0 / 5 / 15 / 35 / 60 across bands [RESEARCH GAP — exact band thresholds to confirm] |
| Emprendedor | USD 20,000.01 – 300,000 | 0%-2% marginal on gross income |

- **RIMPE filing timing and applicability** — RIMPE income tax is declared in May of the following year (e.g. 2025 RIMPE return due May 2026), by ninth digit. Apply RIMPE ONLY if the taxpayer is registered in RIMPE and within the band.  _(SRI RIMPE; JEZL; Bloomberg Línea; Primicias)_

### 5.9 IVA Interaction

**IVA interaction table**

| Scenario | Income Tax Treatment |
| --- | --- |
| IVA collected on sales (registered) | NOT income -- exclude from renta gravada |
| Input IVA recovered (crédito tributario) | NOT an expense -- exclude |
| Input IVA not recoverable | IS a cost -- include gross |

[RESEARCH GAP — current IVA standard rate is 15%; confirm in the ecuador-iva skill before applying to net-of-IVA extractions.]

### 5.10 Filing Deadlines and Penalties

**Filing deadlines and penalties table**

| Item | Detail |
| --- | --- |
| Formulario 102/102A (annual PIT) | March of the following year, staggered by ninth digit of cédula/RUC (see Section 6) |
| Anexo de Gastos Personales (APS) | February of the following year, when personal expenses exceed 50% of the exempt base |
| RIMPE income tax | May of the following year |
| Late-filing fine (tax due) | 3% of tax due per month or fraction, capped at 100% of the tax (LRTI art. 100) |
| Late-filing fine (no tax due but income exists) | 0.1% per month/fraction of gross income / sales, with statutory cap (LRTI art. 100) |
| Interest on overdue tax (interés por mora) | Banco Central 90-day reference rate, set quarterly; 1.3× that rate where SRI notifies non-filing before voluntary correction (Código Tributario art. 21) [RESEARCH GAP — variable rate, no fixed %] |
| Recargo on omitted tax detected by SRI | 20% of the omitted tax, in addition to fine and interest (Código Tributario) |
| Failure to file Anexo de Gastos Personales | Sanción pecuniaria per SRI sanctions schedule (SRI Preguntas frecuentes sanciones) |

## Section 6 -- Filing Calendar (Ninth Digit of Cédula/RUC)

Annual PIT (Formulario 102/102A) for fiscal 2025 is due in March 2026, staggered by the ninth digit of the cédula/RUC (SRI; Primicias):

**Filing calendar by ninth digit**  _(SRI; Primicias)_

| Ninth digit | Deadline (March, following year) |
| --- | --- |
| 1 | 10 Mar |
| 2 | 12 Mar |
| 3 | 14 Mar |
| 4 | 16 Mar |
| 5 | 18 Mar |
| 6 | 20 Mar |
| 7 | 22 Mar |
| 8 | 24 Mar |
| 9 | 26 Mar |
| 0 | 28 Mar |

Special taxpayers (contribuyentes especiales) up to 11 Mar; Galápagos up to 28 Mar. The Anexo de Gastos Personales is filed in February (same ninth-digit staggering). The Proyección de Gastos Personales (Formulario GP) is filed with the employer at year-start (Jan/Feb) to lower monthly withholding (SRI Boletín NAC-COM-25-006).

## Section 7 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 7.1 Home Office Apportionment

- **Home office apportionment** — For a self-employed person working from home, apportion electricity, water, internet, rent to the business-use proportion. Must have facturas with RUC. Conservative default: 0% deduction until reviewer confirms the apportionment basis.

### 7.2 Motor Vehicle Business Use

- **Motor vehicle business use** — Only the business-use percentage of fuel, insurance, maintenance is deductible; requires a mileage log. Conservative default: 0% business use until a log is provided.

### 7.3 Phone / Internet Mixed Use

- **Phone/internet mixed use** — Business-use portion only. Conservative default: 0% deduction until business percentage confirmed.

### 7.4 Gastos Personales Documentation and Dependents

- **Gastos personales documentation and dependents** — The rebate depends on documented facturas by category and on the number of dependents (drives the canasta multiplier). Flag for reviewer to confirm dependents and that each factura carries the taxpayer's RUC/cédula and falls in an allowed category. [RESEARCH GAP — 2025 per-dependent caps to confirm.]

### 7.5 Regime Choice (General vs RIMPE)

- **Regime choice** — Confirm RUC registration and revenue band. RIMPE is mandatory/elective per the taxpayer's registration; do not assume. Flag for reviewer where revenue is near the USD 20,000 (Negocio Popular) or USD 300,000 (Emprendedor) thresholds.

### 7.6 Foreign Income and Treaty Relief (Residents)

- **Foreign income and treaty relief** — Worldwide income with foreign tax credit; treaty relief and CAN Decision 578 may apply. Flag for reviewer in any cross-border case.

## Section 8 -- Excel Working Paper Template

```
ECUADOR INCOME TAX -- FORMULARIO 102/102A WORKING PAPER
Tax Year: 2025
Client: ___________________________
Cédula/RUC (ninth digit): _____   Residency: Resident / Non-resident (183-day test)
Regime: General / RIMPE Negocio Popular / RIMPE Emprendedor
Dependents (for rebate): _____

A. INGRESOS GRAVADOS (TAXABLE INCOME)
  A1. Honorarios / professional fees (net of IVA if registered)  ___________
  A2. Platform payouts (Stripe, PayPal, etc.)                    ___________
  A3. Employment income (net of IESS 9.45%, excl. 13th/14th)     ___________
  A4. Other taxable income (rental, interest, dividends)         ___________
  A5. TOTAL ingresos gravados                                    ___________

B. DEDUCCIONES (self-employed business costs)
  B1. Office rent / arriendo                                     ___________
  B2. Professional / accountancy / legal fees                    ___________
  B3. Supplies, marketing, training                              ___________
  B4. Bank & payment-processing fees                             ___________
  B5. Travel (business %)                                        ___________
  B6. Utilities / telecoms (business %)                          ___________
  B7. IESS contributions (self-employed)                         ___________
  B8. Other deductible costs                                     ___________
  B9. TOTAL deducciones                                          ___________

C. BASE IMPONIBLE (A5 - B9)                                      ___________

D. IMPUESTO CAUSADO (apply art. 36 table to C)
  D1. Tax on base + marginal (per bracket)                       ___________

E. REBAJA POR GASTOS PERSONALES
  E1. Declared documented personal expenses                      ___________
  E2. Canasta cap (7/9/11/14/17/20 canastas by dependents)       ___________
  E3. Rebate = 18% x min(E1, E2)                                 ___________

F. IMPUESTO A PAGAR (D1 - E3)                                    ___________
  F1. Less: retenciones en la fuente / withholding               ___________
  F2. Less: anticipo / advance paid                               ___________
  F3. SALDO A PAGAR / (a favor)                                  ___________

REVIEWER FLAGS:
  [ ] Residency (183-day test) confirmed?
  [ ] Regime (general vs RIMPE) confirmed against RUC?
  [ ] Dependents confirmed for canasta multiplier?
  [ ] 13th/14th salaries excluded from income and IESS base?
  [ ] IESS modelled correctly (9.45/11.15 dependent vs 20.50 voluntary)?
  [ ] All gastos personales backed by facturas with RUC?
  [ ] All business deductions backed by facturas with RUC?
  [ ] Non-resident flat 25% applied where 183-day test not met?
  [ ] 2025 bracket figures verified against original SRI resolution?
```

## Section 9 -- Bank Statement Reading Guide

### Ecuadorian Bank Statement Formats

**Bank statement formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Banco Pichincha | PDF, Excel | Fecha, Descripción, Débito, Crédito, Saldo | Most common; description holds counterparty + reference |
| Banco Guayaquil | PDF, CSV | Fecha, Concepto, Valor, Saldo |  |
| Banco del Pacífico | PDF | Fecha, Detalle, Retiro, Depósito |  |
| Produbanco | PDF, CSV | Fecha, Descripción, Débito, Crédito |  |
| Banco Internacional | PDF | Fecha, Concepto, Cargo, Abono |  |

### Key Spanish Banking / Tax Terms

**Spanish banking/tax terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| TRANSFERENCIA / TRF | Transfer | Check direction for income/expense |
| DÉBITO AUTOMÁTICO | Direct debit | Regular expense (utility, subscription) |
| DEPÓSITO / ABONO | Deposit / credit | Potential income |
| RETIRO / CAJERO | Withdrawal / ATM | Ask what cash was spent on |
| COMISIÓN / MANTENIMIENTO | Bank charge | Deductible (business account) |
| INTERESES | Interest | Interest income or bank charge |
| HONORARIOS | Professional fees | Business income (self-employed) |
| ROL DE PAGOS / SUELDO / NÓMINA | Payroll / salary | Employment income (net of IESS) |
| APORTE IESS / PLANILLA | Social security | IESS contribution |
| DÉCIMO TERCERO / CUARTO | 13th / 14th salary | EXEMPT -- exclude |
| FONDOS DE RESERVA | Reserve fund | Excluded from taxable income |
| RETENCIÓN EN LA FUENTE | Withholding at source | Credit against liability |
| ANTICIPO | Advance tax | Credit against liability |
| FACTURA | Invoice (with RUC) | Supports income or deduction |

## Section 10 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 8) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- ECUADOR INCOME TAX
1. Residency: were you physically in Ecuador 183+ days this year (or over 12 months across two periods)?
2. Regime: general regime, or registered in RIMPE (Negocio Popular ≤ USD 20,000 / Emprendedor ≤ USD 300,000)?
3. Status: self-employed/professional, employee, or both?
4. Dependents: how many (for the gastos-personales rebate)?
5. Gastos personales: do you have facturas (with your RUC/cédula) for vivienda, salud, educación, alimentación, vestimenta, turismo? Approximate total?
6. IESS: are you a dependent worker (9.45% withheld) or a voluntary/independent affiliate (20.50%)?
7. Home office: dedicated space or shared? If apportioning, what %?
8. Vehicle: business use? % and mileage log?
9. Phone/internet: business %?
10. Withholding/anticipo: total retenciones en la fuente and advances paid this year?
11. Any foreign-source income (residents only)?
```

## Section 11 -- Reference Material

### Key Legislation / Authority References

**Key legislation/authority references table**

| Topic | Reference |
| --- | --- |
| PIT tables (progressive 0%-37%) | LRTI art. 36; SRI Resolutions NAC-DGERCGC24-00000041 (2025), NAC-DGERCGC25-00000043 (2026) |
| Late-filing fine | LRTI art. 100 |
| Interest on mora; recargo; sanciones | Código Tributario art. 21 |
| IESS contributions | Ley de Seguridad Social; IESS Tasas de Aportación |
| 13th/14th salary; fondos de reserva | Código del Trabajo |
| RIMPE | LRTI (Régimen Simplificado para Emprendedores y Negocios Populares); SRI RIMPE |
| Residency (183 days) | LRTI art. 4.1; SRI |
| Minimum wage (SBU) | Ministerio del Trabajo; Acuerdo Ministerial MDT-2025-195 (2026) |
| Annual return | Formulario 102 / 102A (SRI) |

### Primary Sources

- Resolución NAC-DGERCGC25-00000043 -- Tabla Impuesto a la Renta Personas Naturales 2026 (official PDF), SRI: https://www.sri.gob.ec/o/sri-portlet-biblioteca-alfresco-internet/descargar?id=bb7aac3c-251d-4243-9477-10a3ba8e7355&nombre=NAC-DGERCGC25-00000043.pdf
- Impuesto a la Renta -- quiénes declaran y calendario por noveno dígito, SRI: https://www.sri.gob.ec/en/impuesto-renta
- Régimen Simplificado para Emprendedores y Negocios Populares (RIMPE), SRI: https://www.sri.gob.ec/en/rimpe
- Ecuador -- Individual -- Taxes on personal income, PwC Worldwide Tax Summaries: https://taxsummaries.pwc.com/ecuador/individual/taxes-on-personal-income
- Tabla de impuesto a la renta (IR) 2026, 2025 -- Personas Naturales, JEZL Auditores: https://www.jezl-auditores.com/index.php/tributario/101-tabla-de-impuesto-a-la-renta-ir-2026-2025-personas-naturales-ecuador
- Régimen Impositivo RIMPE -- tablas Negocios Populares y Emprendedores, JEZL: https://www.jezl-auditores.com/index.php/tributario/152-regimen-impositivo-rimpe
- Aporte personal al IESS (9.45% / 11.15% / 20.5%), EcuadorLegalOnline: https://www.ecuadorlegalonline.com/laboral/aporte-personal-iess/
- Tabla Aportes IESS Ecuador, misalario.ec (WageIndicator): https://misalario.ec/tabla-aportes-iess-ecuador/
- Salario básico unificado 2026 (USD 482, Acuerdo MDT-2025-195), NMS Law: https://nmslaw.com.ec/blog/2025/12/22/ecuador-salario-basico-unificado-2026/
- Gastos personales 2026 (canastas table + USD 821.80), HLB Ecuador: https://www.hlbecuador.com/gastos-personales-2026-el-limite-que-define-la-rebaja-del-impuesto-a-la-renta/
- Anexo de Gastos Personales 2025 (canasta USD 798.31, 18% formula), Russell Bedford Ecuador: https://russellbedford.com.ec/anexo-de-gastos-personales-2025-ecuador-rebaja-del-impuesto-a-la-renta/
- Multas e intereses por mora (3% mensual, recargo 20%), Primicias: https://www.primicias.ec/economia/impuesto-renta-sri-multas-intereses-91745/
- Residencia Fiscal de Extranjeros en Ecuador: Guía 2025 (183-day test), Russell Bedford: https://russellbedford.com.ec/residencia-fiscal-de-extranjeros-en-ecuador-guia-2025/

### Test Suite

**Test 1 -- Self-employed, mid-range income, full rebate (2025).**
Input: Resident, net taxable income USD 30,000, no dependents, documented personal expenses ≥ cap.
Expected: Impuesto causado = 1,398 + (30,000 − 26,422) × 15% = USD 1,934.70. Rebate = 5,588.17 × 18% = USD 1,005.87. Tax due = USD 928.83.

**Test 2 -- Income at the exempt base (2025).**
Input: Resident, net taxable income USD 12,081.
Expected: USD 0 tax (top of the 0% band). Filing still REQUIRED because gross income reaches the threshold.

**Test 3 -- Top bracket entry (2026).**
Input: Resident, net taxable income USD 109,956.
Expected: Cumulative tax = USD 24,572 at the start of the 37% band (next dollar taxed at 37%).

**Test 4 -- Non-resident flat 25%.**
Input: Non-resident, Ecuadorian-source income USD 10,000.
Expected: Tax = 10,000 × 25% = USD 2,500. No table, no rebate.

**Test 5 -- Employee monthly IESS (2025).**
Input: Gross monthly salary USD 1,500, private-sector dependent worker.
Expected: Employee IESS = 1,500 × 9.45% = USD 141.75; employer IESS = 1,500 × 11.15% = USD 167.25; total IESS = USD 309.00 (20.60%).

**Test 6 -- Self-employed voluntary IESS on SBU floor (2025).**
Input: Voluntary/independent affiliate at the SBU floor (USD 470).
Expected: Monthly contribution = 470 × 20.50% = USD 96.35.

**Test 7 -- RIMPE band check.**
Input: Resident, gross annual revenue USD 250,000.
Expected: Within the Emprendedor band (USD 20,000.01–300,000); taxed 0%-2% marginal on gross under RIMPE if registered -- NOT the art. 36 table.

## PROHIBITIONS

- NEVER apply the progressive table without confirming residency -- non-residents pay a flat 25% with no allowance
- NEVER compute the impuesto causado in prose -- pass the base imponible to the deterministic engine
- NEVER include the 13th or 14th salary in taxable income or in the IESS base
- NEVER apply the 9.45/11.15 split to a self-employed person not under labour dependency -- use 20.50% voluntary
- NEVER allow fines, penalties, interés por mora, or income tax itself as a deduction
- NEVER include IVA collected on sales in renta gravada for IVA-registered taxpayers
- NEVER claim a gasto personal or business deduction without a factura carrying the taxpayer's RUC/cédula
- NEVER exceed the canasta cap on the personal-expense rebate -- it is 18% of the LESSER value
- NEVER apply RIMPE unless the taxpayer is registered in RIMPE and within the revenue band
- NEVER present a figure marked [RESEARCH GAP] as confirmed -- escalate to the reviewer
- NEVER present tax calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

The most up-to-date, verified version of this skill is maintained at openaccountants.com. Log in to access the latest version, request a professional review from a licensed accountant, and track updates as tax law changes.

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
