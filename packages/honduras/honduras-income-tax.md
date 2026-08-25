---
name: honduras-income-tax
description: Use this skill whenever asked about Honduras personal income tax (ISR — Impuesto Sobre la Renta) for individuals (personas naturales), including self-employed professionals. Trigger on phrases like "how much ISR do I pay", "Honduras income tax", "Declaración Jurada", "Form 102", "tabla progresiva", "aportación solidaria", "solidarity contribution", "IHSS contributions", "RAP", "Honduran tax return", "renta neta gravable", "self-employed tax Honduras", "ingreso exento", or any question about filing or computing ISR for an individual or self-employed client in Honduras. Also trigger when preparing or reviewing a Declaración Jurada de ISR — Persona Natural, classifying deductible expenses, advising on Pagos a Cuenta (advance payments), or the solidarity contribution. This skill covers the progressive ISR table, solidarity contribution, alternative minimum tax, capital gains, non-resident withholding, IHSS/RAP social security, filing forms and deadlines. ALWAYS read this skill before touching any Honduras income tax work.
version: 0.1
jurisdiction: HN
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Honduras Personal Income Tax (ISR) — Individuals

## Section 1 — Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Honduras (República de Honduras) |
| Tax | Impuesto Sobre la Renta (ISR) — personal income tax on individuals |
| Currency | Honduran Lempira (HNL / "L") only |
| Tax year | Calendar year (1 January — 31 December) [PwC, tax administration] |
| Basis of taxation | Territorial — Honduran-source income; non-residents taxed only on Honduran-source income [PwC] |
| Primary legislation | Ley del Impuesto Sobre la Renta; Código Tributario (Decreto 170-2016) |
| Solidarity contribution | Decreto 278-2013 (Aportación Solidaria) |
| Tax authority | SAR — Servicio de Administración de Rentas (sar.gob.hn) |
| Filing portal | DET Live (detlive.sar.gob.hn) |
| Annual return form | Declaración Jurada del ISR — Persona Natural, Form 102 / 102-1 [SAR DET Live] |
| Filing & payment deadline | 30 April of the year following the tax year [Radio HRN; PwC] |
| Validated by | Pending — requires sign-off by a Honduran-licensed accountant (Perito Mercantil / Contador Público) |
| Validation date | Pending |
| Skill version | 0.1 |

### ISR Progressive Table — 2026 (CURRENT)

**ISR Progressive Table — 2026 (CURRENT)**  _(SAR Comunicado 02-2026; Deloitte HN 12 Jan 2026; PwC, updated 27 Feb 2026)_

| Annual net taxable income (HNL) | Monthly equivalent (HNL) | Rate | Cumulative tax at top of band |
| --- | --- | --- | --- |
| 0.01 – 228,324.32 | 0.01 – 22,360.36 | Exempt (0%) | L 0.00 |
| 228,324.33 – 348,154.10 | 22,360.37 – 32,346.18 | 15% | L 17,974.47 |
| 348,154.11 – 809,660.75 | 32,346.19 – 70,805.06 | 20% | L 110,275.80 |
| 809,660.76 and above | 70,805.07 and above | 25% | — |

Indexed for inflation each year by SAR using the prior year's interannual CPI (4.98% for 2026). [SAR Comunicado 02-2026; Deloitte HN 12 Jan 2026; PwC, updated 27 Feb 2026]

**Cumulative-tax derivation (recomputed):**
- Band 2: (348,154.10 − 228,324.32) × 15% = 119,829.78 × 0.15 = **L 17,974.47**
- Band 3: (809,660.75 − 348,154.10) × 20% = 461,506.65 × 0.20 = 92,301.33; plus L 17,974.47 = **L 110,275.80**

### ISR Progressive Table — 2025 (FY2025 returns, filed by 30 Apr 2026)

**ISR Progressive Table — 2025 (FY2025 returns, filed by 30 Apr 2026)**  _(KPMG TaxNewsFlash 14 Jan 2025; Bloomberg Línea; SAR)_

| Annual net taxable income (HNL) | Monthly equivalent (HNL) | Rate |
| --- | --- | --- |
| 0 – 217,493.16 | 0 – 21,457.76 | Exempt (0%) |
| 217,493.17 – 331,638 [RESEARCH GAP — reviewer to confirm exact centavos] | 21,457.77 – 30,969 | 15% |
| 331,638 – 771,252 [RESEARCH GAP — reviewer to confirm exact centavos] | 30,969 – 67,604 | 20% |
| 771,252 and above [RESEARCH GAP — reviewer to confirm exact centavos] | 67,604 and above | 25% |

Indexed using 3.88% CPI. [KPMG TaxNewsFlash 14 Jan 2025; Bloomberg Línea; SAR]

**Note:** The exempt base **L217,493.16** is also the legal FY2025 filing threshold cited by SAR. The two upper 2025 thresholds come from a secondary SAR/Bloomberg summary and are rounded — confirm exact centavos from the SAR 2025 comunicado PDF before filing a FY2025 return.

### Surtaxes, Minimum Tax and Capital Gains

**Surtaxes, Minimum Tax and Capital Gains**  _(Decreto 278-2013; PwC)_

| Item | Rate / threshold | Source |
| --- | --- | --- |
| Solidarity Contribution (Aportación Solidaria) | 5% surtax on net taxable income **exceeding L1,000,000** | Decreto 278-2013 |
| Alternative Minimum Tax (high earners) | 1.5% of **gross income** for domiciled individuals with gross income **≥ L10,000,000**, when it exceeds progressive ISR otherwise due | PwC |
| Capital gains | Flat **10%** | PwC |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residence/domicile status | STOP — do not apply the resident progressive table without confirming domicile |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown income source (Honduran vs foreign) | Treat as Honduran-source (taxable) pending confirmation |
| Pure salaried employee with PAYE withholding | Assume no separate filing obligation unless other income exists |
| Income ≥ L10,000,000 gross | Flag alternative minimum tax for reviewer |
| Net taxable income > L1,000,000 | Flag solidarity contribution |

## Section 2 — Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** — bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of residence/domicile status and whether the client is purely salaried (PAYE) or has self-employment / professional / rental / investment income.

**Recommended** — all sales invoices and fiscal receipts (facturas), purchase invoices/receipts, IHSS/RAP contribution records, prior year Declaración Jurada or SAR assessment, RTN (Registro Tributario Nacional), Pagos a Cuenta payment confirmations.

**Ideal** — complete income and expenditure account, asset register, employer salary certificate (constancia de sueldo), evidence of any solidarity-contribution advance instalments paid.

**Refusal if minimum is missing — SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This ISR computation was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid fiscal documentation (facturas with RTN) and that income is correctly classified as Honduran-source."

### Refusal Catalogue

- **R-HN-1 — Residence/domicile unknown** — "Honduras taxes residents and non-residents differently; non-residents bear final withholding at flat rates and generally do not file the progressive return. This skill cannot compute ISR without confirming domicile. Please confirm before proceeding."  _(R-HN-1)_
- **R-HN-2 — Companies / legal persons** — "This skill covers individuals (personas naturales) only. Legal persons (personas jurídicas) file Form 103 with Activo Neto and Aportación Solidaria, and face the corporate ISR regime. Escalate to a Honduran-licensed accountant."  _(R-HN-2)_
- **R-HN-3 — Special regimes** — "Export, free-zone (Zona Libre/maquila), tourism, and other special regimes have bespoke rules and exemptions. Out of scope. Escalate to a Honduran-licensed accountant."  _(R-HN-3)_
- **R-HN-4 — Capital gains / property disposals** — "Capital gains are taxed at a flat 10% and require specialised computation of basis and proceeds. Out of scope for the progressive-income workflow. Escalate to a Honduran-licensed accountant."  _(R-HN-4)_
- **R-HN-5 — Arrears / SAR enforcement** — "Client has outstanding tax arrears or is subject to SAR enforcement. Penalties and surcharges under Código Tributario Art. 160 apply. Do not advise. Escalate to a Honduran-licensed accountant immediately."  _(R-HN-5)_
- **R-HN-6 — Sales tax (ISV/VAT) requested** — "This skill covers income tax (ISR) only. Honduras sales tax (ISV) is a separate 15% (18% on certain premium services) regime — escalate to the appropriate ISV skill or a licensed accountant."  _(R-HN-6)_

## Section 3 — Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Honduran statements are typically in Spanish. Match by case-insensitive substring on the counterparty/description as it appears in the statement. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules in Section 5.

### 3.1 Income Patterns (Credits / Créditos)

**Income Patterns (Credits / Créditos)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Client name + TRANSFERENCIA, DEPOSITO, ABONO, PAGO RECIBIDO | Business / professional income | Renta gravable; if ISV-registered, extract net of 15% ISV |
| HONORARIOS, SERVICIOS PROFESIONALES, CONSULTORIA | Business / professional income | Professional fees — typical for self-employed |
| COMISION, COMISIONES | Business income | Commissions are taxable |
| STRIPE PAYOUT, PAYPAL, WISE, PAYONEER | Business income | Platform payout — match to underlying invoices |
| UPWORK, FIVERR, FREELANCER | Business income | Freelance platform — net of platform commission |
| SUELDO, SALARIO, PLANILLA, NOMINA, [employer name] | Employment income | PAYE-withheld; generally not in the self-employment base |
| ALQUILER, RENTA RECIBIDA, ARRENDAMIENTO | Rental income | Taxable income, separate source |
| INTERESES RECIBIDOS, INTERES | Investment income | Interest income (resident WHT 10% may apply) |
| DIVIDENDOS | Investment income | Dividends (WHT 10%) |
| DEVOLUCION SAR, REINTEGRO ISR | EXCLUDE | Tax refund — not income |
| BONO GOBIERNO, SUBSIDIO (capital) | EXCLUDE unless revenue subsidy | Capital grants EXCLUDE; revenue subsidies = income |

### 3.2 Expense Patterns (Debits / Débitos) — Deductible

**Expense Patterns (Debits / Débitos) — Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| ALQUILER OFICINA, RENTA LOCAL | Office rent | Deductible | Dedicated business premises; needs factura with RTN |
| CONTADOR, AUDITOR, CONTABILIDAD | Accountancy fees | Deductible | Business-related |
| ABOGADO, NOTARIO, LEGAL (negocio) | Legal fees | Deductible | Must be business-related |
| PAPELERIA, UTILES DE OFICINA | Office supplies | Deductible |  |
| PUBLICIDAD, MARKETING, GOOGLE ADS, META ADS | Marketing/advertising | Deductible |  |
| CAPACITACION, CURSO, SEMINARIO, COLEGIO PROFESIONAL | Training / professional subs | Deductible | Must relate to current business |
| COMISION BANCARIA, CARGO BANCARIO, MANTENIMIENTO CUENTA | Bank charges | Deductible | Business account only |
| COMISION STRIPE, COMISION PAYPAL | Payment processing fees | Deductible |  |
| SOFTWARE, SUSCRIPCION, MICROSOFT 365, ADOBE, ANTHROPIC, OPENAI | Software subscription | Deductible | Recurring subscription = operating expense |
| INTERNET, TIGO, CLARO, HONDUTEL (negocio) | Telecoms/broadband | Deductible (business %) | Apportion if mixed; default 0% if personal line |

### 3.3 Statutory Deductions / Contributions

**Statutory Deductions / Contributions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IHSS, SEGURO SOCIAL, COTIZACION IHSS | Statutory deduction | Employee EM+IVM contributions — see Section 5 |
| RAP, APORTACION RAP, REGIMEN APORTACIONES PRIVADAS | Statutory deduction | Mandatory private pension/severance — see Section 5 |
| INFOP | Employer-only levy | 1% employer only — NOT an employee deduction [PwC] |
| IMPUESTO VECINAL, IMPUESTO PERSONAL MUNICIPAL | Municipal tax | Withheld by employers with 5+ workers, graduated 1.50–5.25 per thousand of gross [PwC] |

### 3.4 Expense Patterns — NOT Deductible

**Expense Patterns — NOT Deductible**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| RESTAURANTE, CENA, ALMUERZO, ENTRETENIMIENTO | NOT deductible | Personal/entertainment — flag any business-meal claim for reviewer |
| SUPERMERCADO, LA COLONIA, WALMART, DESPENSA | NOT deductible | Private living costs |
| MULTA, SANCION, RECARGO, MORA | NOT deductible | Fines/penalties — public policy |
| PAGO ISR, IMPUESTO SOBRE LA RENTA | NOT deductible | Income tax cannot reduce its own base |
| RETIRO PERSONAL, CAJERO (personal), GASTOS PERSONALES | NOT deductible | Drawings / private withdrawals |

### 3.5 Exclusions (Neither Income nor Expense)

**Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERENCIA PROPIA, ENTRE CUENTAS PROPIAS | EXCLUDE | Own-account transfer |
| PRESTAMO, ABONO PRESTAMO, CAPITAL PRESTAMO | EXCLUDE | Loan principal movement |
| PAGO ISV, IMPUESTO SOBRE VENTAS | EXCLUDE | ISV liability payment, not an income-tax expense |
| PAGO A CUENTA, ANTICIPO ISR | Credit against ISR liability | Advance payment — not an expense; offsets final tax |
| APORTACION SOLIDARIA (anticipo) | Credit against solidarity contribution | Quarterly advance instalment |

### 3.6 Honduran Banks — Statement Format Reference

**Honduran Banks — Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Banco Atlántida | TRANSFERENCIA, ABONO, CARGO, COMISION | PDF/CSV; date DD/MM/YYYY |
| BAC Credomatic | PAGO, TRANSFERENCIA, DEBITO, CARGO | PDF/CSV; merchant in description |
| Banco Ficohsa | DEPOSITO, RETIRO, COMISION | PDF; Spanish descriptions |
| Banco de Occidente | ABONO, CARGO, TRANSFERENCIA | PDF |
| Davivienda Honduras | PAGO, TRANSFERENCIA, COMISION | PDF/CSV |

## Section 4 — Worked Examples

All figures in Honduran Lempira (HNL / "L"). Statement lines are illustrative.

### Example 1 — Professional fee received (self-employed)

**Input line:**
`12/03/2026 ; BAC TRANSFERENCIA RECIBIDA ; CONSTRUCTORA MAYA SA ; PAGO HONORARIOS FAC-0042 ; +34,500.00 ; HNL`

**Reasoning:**
Professional fee for services. Honduran-source, taxable. If the client is ISV-registered and the L34,500 includes 15% ISV, the net is L34,500 / 1.15 = L30,000 (ISV L4,500 is a liability to SAR, excluded from the income-tax base). Assume here the client is NOT ISV-registered, so the full L34,500 is gross income.

**Classification:** Renta gravable = L34,500.00 (or L30,000.00 net if ISV-registered).

### Example 2 — Software subscription (deductible)

**Input line:**
`01/04/2026 ; FICOHSA CARGO ; ADOBE SYSTEMS ; CREATIVE CLOUD ABR ; -780.00 ; HNL`

**Reasoning:**
Monthly recurring SaaS subscription used for the business. Fully deductible operating expense, provided a valid factura with the client's RTN is retained.

**Classification:** Deductible expense = L780.00.

### Example 3 — IHSS + RAP employee contributions (statutory deduction)

**Input line (monthly salary at the contribution ceiling):**
`30/04/2026 ; ATLANTIDA PLANILLA ; COTIZACION IHSS + RAP ; ABR 2026 ; -773.70 ; HNL`

**Reasoning:**
Employee social-security burden on a salary at or above the 2025 ceiling of **L11,903.13/month**: EM 2.5% + IVM 2.5% + RAP 1.5% = **6.5%** combined employee share. [El Heraldo; Dinero HN; RAP comunicado 2025]

Computation: L11,903.13 × 6.5% = L773.70 (11,903.13 × 0.065 = 773.70345, rounded to L773.70).

**Classification:** Statutory employee contribution = L773.70 for the month. [RESEARCH GAP — confirm 2026 IHSS/RAP ceiling; only the 2025 ceiling of L11,903.13 is authoritatively confirmed.]

### Example 4 — Solidarity contribution (high net income)

**Input:**
Self-employed individual, FY2026, net taxable income (renta neta gravable) = **L1,400,000**.

**Reasoning:**
The solidarity contribution (Aportación Solidaria, Decreto 278-2013) is 5% on the portion of net taxable income exceeding L1,000,000. It is NOT deductible from ISR and is settled separately.

Computation: (1,400,000 − 1,000,000) × 5% = 400,000 × 0.05 = **L20,000.00**.

This is in addition to the progressive ISR on the full L1,400,000.

**Classification:** Solidarity contribution = L20,000.00 (separate line from progressive ISR).

### Example 5 — Drawings (exclude)

**Input line:**
`15/05/2026 ; OCCIDENTE TRANSFERENCIA ; CUENTA PROPIA AHORRO ; ; -25,000.00 ; HNL`

**Reasoning:**
Transfer between the client's own accounts. Neither income nor expense.

**Classification:** EXCLUDE.

### Example 6 — Pago a Cuenta (advance ISR payment)

**Input line:**
`30/06/2026 ; BAC PAGO SAR ; PAGO A CUENTA ISR ; 1ER ANTICIPO ; -18,000.00 ; HNL`

**Reasoning:**
Advance income-tax instalment (Pago a Cuenta). Not an expense — it is a credit against the final annual ISR liability, settled with the Declaración Jurada on 30 April.

**Classification:** Credit against ISR = L18,000.00. NOT a deduction.

## Section 5 — Tier 1 Rules (When Data Is Clear)

### 5.1 Territorial Scope

- **Territorial Scope** — Honduras taxes on a territorial basis — only Honduran-source income is taxable for both residents and non-residents. Foreign-source income of residents is generally outside scope; confirm source before including any item.  _(Ley del ISR; PwC)_

### 5.2 Progressive ISR — Resident Individuals

- **Progressive ISR — Resident Individuals** — Apply the 2026 progressive table (Section 1) to annual net taxable income (renta neta gravable = gross taxable income less allowable deductions and the exempt base). The table is re-indexed annually by SAR. Cumulative-tax figures are pre-derived in Section 1 — pass the chargeable base to the deterministic engine rather than computing band tax by hand.  _(SAR Comunicado 02-2026)_

### 5.3 Solidarity Contribution

- **Solidarity Contribution** — A 5% surtax on net taxable income exceeding L1,000,000. Not deductible from ISR. Paid via three quarterly advance instalments (30 Jun, 30 Sep, 31 Dec) and settled with the annual return on 30 April. Excludes special export/tourism regimes.  _(Decreto 278-2013)_

### 5.4 Alternative Minimum Tax

- **Alternative Minimum Tax** — Domiciled individuals with gross income ≥ L10,000,000 pay the greater of progressive ISR or 1.5% of gross income. Flag any client at or above this threshold for reviewer.  _(PwC)_

### 5.5 Capital Gains

- **Capital Gains** — Flat 10% on the gain. Out of scope for the progressive workflow — see R-HN-4.  _(PwC)_

### 5.6 Deductibility — General Test

- **Deductibility — General Test** — Expenses are deductible only if ordinary, necessary, and incurred to produce or maintain Honduran-source taxable income, and supported by a valid factura bearing the supplier's RTN. Mixed-use expenses must be apportioned on a reasonable, documented basis.

### 5.7 Non-Deductible Items

**Non-Deductible Items**

| Item | Reason |
| --- | --- |
| Entertainment / personal meals | Private consumption |
| Personal living expenses | Not business-related |
| Fines, penalties, surcharges (multas/recargos) | Public policy |
| Income tax (ISR) itself | Tax on income |
| Solidarity contribution | Expressly non-deductible from ISR |
| Drawings / personal withdrawals | Not an expense |

### 5.8 Social Security & Payroll Contributions (2025 reform)

**Social Security & Payroll Contributions (2025 reform)**  _(El Heraldo; Dinero HN; RAP comunicado 2025)_

| Regime | Employee | Employer | State |
| --- | --- | --- | --- |
| EM (Enfermedad y Maternidad — health/maternity) | 2.5% | 5.0% | — |
| IVM (Invalidez, Vejez y Muerte — pensions) | 2.5% | 3.5% | 0.5% |
| RAP (Régimen de Aportaciones Privadas) | 1.5% | 1.5% | — |
| **TOTAL** | **6.5%** | **10.0%** | **0.5%** |

**Legislation:** Ley del Sistema Integral de Protección Social (approved 30 Apr 2024); new rates effective Jan 2025. Administered by IHSS (Instituto Hondureño de Seguridad Social) and RAP (Régimen de Aportaciones Privadas). Applied on salary up to the 2025 monthly ceiling of L11,903.13 (unified for EM and IVM; also the RAP piso/techo de cotización). [El Heraldo; Dinero HN; RAP comunicado 2025]

**Totals verification (recomputed):** Employee 2.5 + 2.5 + 1.5 = **6.5%** ✓; Employer 5.0 + 3.5 + 1.5 = **10.0%** ✓; State 0.5% on IVM only.

**Employer-only:** INFOP (training fund) 1% of payroll, no employee portion. [PwC]

**Caveat:** PwC's "other taxes" page lists pre-reform IHSS ceilings (L11,109 EM / L11,336 IVM) and a 1% employee IVM rate. The 2025 reform figures above (2.5% employee IVM, unified L11,903.13 ceiling) supersede them. [RESEARCH GAP — confirm 2026 IHSS/RAP ceiling directly with IHSS/RAP; only the 2025 ceiling is confirmed.]

### 5.9 Non-Resident Withholding (Honduran-source income)

**Non-Resident Withholding (Honduran-source income)**  _(PwC, withholding taxes)_

| Payment type | WHT rate |
| --- | --- |
| Dividends | 10% |
| Interest (commercial ops, bonds, securities) | 10% |
| Royalties (incl. mining/natural resources) | 25% |
| Salaries/fees for services (in or outside HN) | 25% |
| Any other income not specified | 10% |

Honduras has no double-tax treaties (only TIEAs with the US and some Central American countries). [PwC]

### 5.10 Filing, Forms & Deadlines

**Filing, Forms & Deadlines**

| Item | Detail | Source |
| --- | --- | --- |
| Tax year | Calendar year ending 31 December | PwC |
| Annual return | Declaración Jurada del ISR — Persona Natural, Form 102 / 102-1, via DET Live | SAR DET Live |
| Filing & payment deadline | 30 April of the following year | Radio HRN; PwC |
| Who must file | Individuals with annual net income exceeding the exempt base (L217,493.16 for FY2025); self-employed earning fees, commissions, royalties, service income, interest or rental income | Radio HRN; PwC |
| Pure salaried employees | ISR withheld monthly via PAYE; generally need not file unless other income exists | PwC |
| Suspension | If below the exempt base but previously filed, file a Notification of Suspension before 30 Apr | Radio HRN |
| Advance payments | Pagos a Cuenta paid in instalments during the year, settled with the annual return | PwC; SAR |
| RTN | Registro Tributario Nacional required to file and operate | SAR |

### 5.11 Penalties

- **Penalties** — Late filing of the Declaración Jurada is subject to fines and surcharges under Article 160 of the Código Tributario (Decreto 170-2016). [RESEARCH GAP — reviewer to confirm] the exact graduated lempira fine/surcharge schedule directly from Decreto 170-2016 Art. 160 before advising on penalty amounts.  _(Radio HRN; Código Tributario (Decreto 170-2016) Art. 160)_

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction

- **Home Office Deduction** — Calculate the business-use proportion of the home (dedicated room as % of total floor area). Apply that percentage to rent, electricity, water, internet, maintenance. Must be a genuinely dedicated workspace; dual-use rooms do not qualify. Conservative default: 0% deduction until reviewer confirms the arrangement.

### 6.2 Vehicle Business Use

- **Vehicle Business Use** — Only the business-use percentage of fuel, insurance, and maintenance is deductible. Client must keep a usage log (business vs total km). Conservative default: 0% business use until a log is provided.

### 6.3 Phone / Internet Mixed Use

- **Phone / Internet Mixed Use** — Business-use portion only; client must provide a reasonable estimate. Conservative default: 0% deduction until business percentage confirmed.

### 6.4 Source of Income (Honduran vs Foreign)

- **Source of Income (Honduran vs Foreign)** — Territorial system: only Honduran-source income is taxable. For platform/foreign-client receipts, the source can be ambiguous — flag for reviewer to confirm where the service was rendered/used. Conservative default: treat as Honduran-source (taxable) pending confirmation.

### 6.5 Bad Debt Write-Off

- **Bad Debt Write-Off** — Deductible only if the income was previously declared, recovery steps were taken, and the debt is genuinely irrecoverable. Flag all three for reviewer.

### 6.6 ISV (Sales Tax) Interaction

- **ISV (Sales Tax) Interaction** — ISV collected on sales (15%, or 18% on premium services) is a liability to SAR, not income; input ISV recovered is not an expense for ISR-registered taxpayers. For non-ISV-registered individuals, ISV paid on purchases forms part of the gross cost. Flag ISV registration status for reviewer.

### 6.7 Alternative Minimum Tax / Solidarity Contribution Application

- **Alternative Minimum Tax / Solidarity Contribution Application** — Flag any client with gross income ≥ L10,000,000 (AMT) or net taxable income > L1,000,000 (solidarity contribution) for reviewer confirmation of the additional charge.

## Section 7 — Excel Working Paper Template

```
HONDURAS ISR -- DECLARACIÓN JURADA PERSONA NATURAL -- WORKING PAPER
Tax Year: 2026
Client: ___________________________   RTN: ___________________________
Residence/Domicile: Resident / Non-resident
ISV-registered: Yes / No

A. GROSS TAXABLE INCOME (Renta Bruta Gravable)
  A1. Professional fees / honorarios (net of ISV if registered) ___________
  A2. Commissions / comisiones                                  ___________
  A3. Platform payouts                                          ___________
  A4. Rental income (alquiler)                                  ___________
  A5. Interest / dividends (Honduran-source)                    ___________
  A6. TOTAL gross taxable income                                ___________

B. ALLOWABLE DEDUCTIONS (with factura + RTN)
  B1. Office rent                                               ___________
  B2. Accountancy / legal fees                                  ___________
  B3. Office supplies / papelería                               ___________
  B4. Software subscriptions                                    ___________
  B5. Marketing / publicidad                                    ___________
  B6. Bank / payment processing charges                         ___________
  B7. Training / professional subscriptions                     ___________
  B8. Telecoms (business %)                                     ___________
  B9. Home office (business %)                                  ___________
  B10. Vehicle expenses (business %)                            ___________
  B11. IHSS + RAP statutory contributions                       ___________
  B12. Other allowable expenses                                 ___________
  B13. TOTAL deductions                                         ___________

C. NET TAXABLE INCOME (Renta Neta Gravable) (A6 - B13)         ___________

D. ISR COMPUTATION (pass C to deterministic engine)
  D1. Progressive ISR on C                                      ___________
  D2. Less: Pagos a Cuenta (advance payments)                   ___________
  D3. Less: ISR withheld at source                              ___________
  D4. ISR due / (refund)                                        ___________

E. SOLIDARITY CONTRIBUTION (if C > 1,000,000)
  E1. (C - 1,000,000) x 5%                                      ___________
  E2. Less: solidarity advance instalments                      ___________
  E3. Solidarity contribution due                               ___________

F. ALTERNATIVE MINIMUM TAX (if gross income >= 10,000,000)
  F1. Gross income x 1.5%                                       ___________
  F2. Greater of D1 or F1 applies                               ___________

REVIEWER FLAGS:
  [ ] Residence/domicile confirmed?
  [ ] ISV registration status confirmed?
  [ ] All income confirmed Honduran-source?
  [ ] Home office / vehicle / phone business % confirmed?
  [ ] All deductions supported by factura + RTN?
  [ ] Solidarity contribution checked (net > L1,000,000)?
  [ ] AMT checked (gross >= L10,000,000)?
  [ ] 2026 IHSS/RAP ceiling and minimum-wage table confirmed?
```

## Section 8 — Bank Statement Reading Guide

### Honduran Bank Statement Formats

**Honduran Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Banco Atlántida | PDF, CSV | Fecha, Descripción, Débito, Crédito, Saldo | Date DD/MM/YYYY |
| BAC Credomatic | PDF, CSV | Fecha, Concepto, Monto, Saldo | Card transactions show merchant |
| Banco Ficohsa | PDF | Fecha, Descripción, Cargo, Abono, Saldo | Spanish descriptions |
| Banco de Occidente | PDF | Fecha, Detalle, Débito, Crédito | Shorter descriptions |
| Davivienda Honduras | PDF, CSV | Fecha, Concepto, Monto, Saldo |  |

### Key Honduran Banking / Tax Terms

**Key Honduran Banking / Tax Terms**

| Term | English | Classification Hint |
| --- | --- | --- |
| ABONO / DEPÓSITO | Deposit / credit | Potential income |
| CARGO / DÉBITO | Charge / debit | Expense — check counterparty |
| TRANSFERENCIA | Transfer | Check direction and whether own-account |
| HONORARIOS | Professional fees | Business income |
| COMISIÓN | Commission / bank fee | Income if received; bank charge if debited |
| SUELDO / SALARIO / PLANILLA | Salary / payroll | Employment income (PAYE) |
| ALQUILER / ARRENDAMIENTO | Rent | Income if received; deductible if business premises |
| INTERESES | Interest | Investment income or bank charge |
| FACTURA | Tax invoice | Required to support a deduction (must carry RTN) |
| RTN | National Tax ID | Identifies the taxpayer/supplier |
| ISV | Sales tax (VAT) | Exclude from ISR base |
| PAGO A CUENTA | Advance ISR payment | Credit against final ISR |

## Section 9 — Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- HONDURAS ISR
1. Are you a Honduran resident/domiciled individual?
2. Are you purely salaried (PAYE) or do you have self-employment / fees / rental / investment income?
3. Are you ISV-registered? If yes, are your invoices net or gross of 15% ISV?
4. Do you have an RTN (national tax ID)?
5. Home office: dedicated room? If yes, what % of floor area?
6. Vehicle: used for business? If yes, what % business use, and do you keep a log?
7. Phone/internet: what % is business use?
8. IHSS + RAP: total contributions in the tax year?
9. Pagos a Cuenta (advance ISR) and any ISR withheld at source: amounts paid?
10. Did your net taxable income exceed L1,000,000, or gross income reach L10,000,000?
```

## Section 10 — Reference Material

### Key Legislation & Authorities

**Key Legislation & Authorities**

| Topic | Reference |
| --- | --- |
| Personal income tax | Ley del Impuesto Sobre la Renta (ISR) |
| Progressive table indexing | SAR annual Comunicado (2026: Comunicado 02-2026) |
| Solidarity contribution | Decreto 278-2013 (Aportación Solidaria) |
| Tax procedure / penalties | Código Tributario, Decreto 170-2016 (incl. Art. 160) |
| Social security | Ley del Sistema Integral de Protección Social (2024); IHSS / RAP |
| Tax authority | SAR — Servicio de Administración de Rentas (sar.gob.hn) |
| Filing system | DET Live (detlive.sar.gob.hn) — Form 102 / 102-1 |

### Authoritative Sources

**Authoritative Sources**

| Item | Source |
| --- | --- |
| 2026 progressive table (exact) | Deloitte HN 12 Jan 2026; SAR Comunicado 02-2026; PwC (27 Feb 2026); Bloomberg Línea |
| 2025 progressive table | KPMG TaxNewsFlash 14 Jan 2025; Bloomberg Línea; SAR |
| Solidarity contribution | Decreto 278-2013; SEFIN consolidated text (25 Jun 2018) |
| AMT, capital gains, WHT | PwC Honduras — taxes on personal income / withholding taxes |
| Social security rates & 2025 ceiling | El Heraldo; Dinero HN; RAP comunicado 2025 |
| Filing, deadline, who files | Radio HRN; PwC tax administration; SAR |
| ISV, municipal tax, INFOP | PwC Honduras — other taxes / taxes on personal income |

### Minimum Wage (2025 reference, Commerce & Construction)

**Minimum Wage (2025 reference, Commerce & Construction)**  _(Secretaría de Trabajo, trabajo.gob.hn; La Prensa)_

| Company size | Monthly wage (HNL) |
| --- | --- |
| 1–10 workers | 12,539.68 |
| 11–50 workers | 12,937.94 |
| 151+ workers | 17,557.35 |

Set by Acuerdo Ejecutivo SETRASS-109-2024 (2024–2025 band), effective 1 Jan 2025; varies by sector and company size. [Secretaría de Trabajo, trabajo.gob.hn; La Prensa]

Maquila/Free Zone: +7.5% adjustment. [RESEARCH GAP — reviewer to confirm] the 2026 minimum-wage table against trabajo.gob.hn before relying on it for FY2026.

### Other Taxes (context)

**Other Taxes (context)**

| Tax | Rate | Source |
| --- | --- | --- |
| Sales tax (ISV/VAT) | 15% general; 18% on certain premium services | PwC |
| Municipal tax (impuesto vecinal/personal) | 1.50–5.25 per thousand of gross, withheld by employers with 5+ workers | PwC |

### Test Suite

**Test 1 — Exempt salaried individual (2026).**
Input: Resident, annual net income L210,000, purely salaried, PAYE withheld.
Expected: Below 2026 exempt base of L228,324.32 → ISR = L0. Generally no filing obligation (may file Notification of Suspension if previously filed).

**Test 2 — Mid-range self-employed (2026).**
Input: Resident self-employed, net taxable income L500,000.
Expected: Band 2 fully (L17,974.47) + Band 3 portion: (500,000 − 348,154.10) × 20% = 151,845.90 × 0.20 = L30,369.18. Total ISR = 17,974.47 + 30,369.18 = **L48,343.65**. No solidarity contribution (net < L1,000,000).

**Test 3 — Top-band with solidarity contribution (2026).**
Input: Resident self-employed, net taxable income L1,400,000.
Expected: ISR = cumulative at L809,660.76 (L110,275.80) + (1,400,000 − 809,660.75) × 25% = 590,339.25 × 0.25 = L147,584.81; total ISR = 110,275.80 + 147,584.81 = **L257,860.61**. Plus solidarity contribution (1,400,000 − 1,000,000) × 5% = **L20,000.00** (separate, non-deductible).

**Test 4 — Employee social security at ceiling (2025).**
Input: Monthly salary ≥ L11,903.13.
Expected: Employee contributions = 6.5% × L11,903.13 = **L773.70/month** (EM 2.5% + IVM 2.5% + RAP 1.5%).

**Test 5 — Alternative minimum tax flag.**
Input: Domiciled individual, gross income L12,000,000, progressive ISR computed at L150,000.
Expected: AMT = 1.5% × 12,000,000 = L180,000 > L150,000 → AMT applies; tax = **L180,000**.

**Test 6 — Drawings excluded.**
Input: L25,000 own-account transfer recorded as expense.
Expected: EXCLUDE. Not an expense, not income.

## PROHIBITIONS

- NEVER apply the resident progressive table without confirming residence/domicile.
- NEVER compute band tax by hand for filing — pass net taxable income to the deterministic engine.
- NEVER deduct entertainment or personal living expenses.
- NEVER deduct the ISR or the solidarity contribution itself.
- NEVER deduct fines, penalties, or surcharges (multas/recargos).
- NEVER include ISV collected on sales in the income-tax base for ISV-registered clients.
- NEVER treat a Pago a Cuenta as an expense — it is a credit against the final liability.
- NEVER claim a deduction without a valid factura bearing the supplier's RTN.
- NEVER apply foreign-source income to the Honduran base without confirming source (territorial system).
- NEVER present tax calculations as definitive — always label as estimated and flag the marked RESEARCH GAPs.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
