---
name: el-salvador-income-tax
description: Use this skill whenever asked about El Salvador personal income tax (Impuesto sobre la Renta) for self-employed individuals and individuals. Trigger on phrases like "how much income tax do I pay in El Salvador", "Impuesto sobre la Renta", "ISR", "declaración de renta", "F-11", "F-14", "retención de renta", "pago a cuenta", "honorarios", "10% withholding professional fees", "ISSS", "AFP", "self-employed tax El Salvador", "renta El Salvador", or any question about filing or computing income tax for a self-employed individual or salaried person in El Salvador. Also trigger when preparing or reviewing an F-11 annual return, computing deductible expenses or the 10% professional-fee withholding, or advising on the progressive renta table, social-security (ISSS) or pension (AFP) contributions. This skill covers the progressive ISR table (0/10/20/30%), the 2025 reform raising the exempt threshold to USD 6,600, monthly retención tables, ISSS and AFP contributions, the 10% honorarios withholding, deductions, filing forms and penalties, and interaction with IVA. ALWAYS read this skill before touching any El Salvador income tax work.
version: 0.1
jurisdiction: SV
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# El Salvador Income Tax (Impuesto sobre la Renta) -- Self-Employed & Individuals

## El Salvador Income Tax (Impuesto sobre la Renta) -- Self-Employed & Individuals Skill v0.1

> **Tier 2 (research-verified) skill — confidence: medium.** The 2025 reform (Decreto Legislativo 293 / Decreto Ejecutivo 10) published official **monthly** retención tables; the exact **annual** Art. 37 breakpoints and middle-bracket fixed amounts are partly inferred by annualising the monthly table and should be re-verified by a Salvadoran CPA against Decreto Ejecutivo 10 before Q1 verification. Items marked **[RESEARCH GAP — reviewer to confirm]** are not fully sourced.

## Section 1 -- Quick Reference

**Quick Reference**

| Field | Value |
| --- | --- |
| Country | El Salvador (República de El Salvador) |
| Tax | Impuesto sobre la Renta (ISR) -- personal income tax |
| Currency | USD only (El Salvador is fully dollarized; Bitcoin legal-tender mandate repealed effective January 2025 — USD is the sole unit of account for tax) |
| Tax year | Calendar year (1 January -- 31 December), per Art. 13 LISR |
| Primary legislation | Ley de Impuesto sobre la Renta (LISR), Decreto No. 134, as reformed by **Decreto Legislativo No. 293 (30 Apr 2025)** and implemented by **Decreto Ejecutivo No. 10 (2025)** |
| Supporting legislation | Código Tributario (Decreto No. 230) — filing/penalties; Ley Integral del Sistema de Pensiones (AFP); Ley del Seguro Social (ISSS); Ley del IVA (13%) |
| Tax authority | Ministerio de Hacienda -- Dirección General de Impuestos Internos (DGII); portal mh.gob.sv |
| Social security (health) | Instituto Salvadoreño del Seguro Social (ISSS), isss.gob.sv |
| Pensions | AFPs supervised by Superintendencia del Sistema Financiero (SSF), ssf.gob.sv |
| Annual filing deadline | Within 4 months of fiscal year-end → **by 30 April** of the following year (Código Tributario; Art. 48 LISR) |
| Validated by | Pending — requires sign-off by a Salvadoran CPA familiar with LISR |
| Validation date | Pending |
| Skill version | 0.1 |

### Tax Rate Brackets -- Annual ISR Table (Art. 37 LISR, effective tax year 2025)

**Annual ISR Table**  _(Art. 37 LISR table as reformed for tax year 2025; Diario El Mundo (citing Ministerio de Hacienda Decreto Ejecutivo 10, 2025); PwC Worldwide Tax Summaries.)_

| Tramo | Annual Net Income (USD) | Marginal rate on excess | Cuota fija (fixed amount) |
| --- | --- | --- | --- |
| I | 0.00 -- 6,600.00 | Exempt (0%) | USD 0.00 |
| II | 6,600.01 -- 10,742.86 | 10% over 6,600.00 | + USD 212.12 |
| III | 10,742.87 -- 24,457.14 | 20% over 10,742.86 | + USD 720.00 |
| IV | 24,457.15 and above | 30% over 24,457.14 | + USD 3,462.86 |

**Domiciled individuals — progressive scale (0% / 10% / 20% / 30%).** ISR = cuota fija (statutory fixed amount) + marginal rate × (net income − band floor).

> **Note on the cuotas fijas.** The statutory fixed amounts are **USD 212.12 (Tramo II), USD 720.00 (Tramo III), USD 3,462.86 (Tramo IV)** — unchanged by the 2025 reform, which moved only the band thresholds (Tramo I exempt ceiling 4,064 → 6,600; Tramo III floor 9,142.86 → 10,742.86; Tramo IV floor 22,857.14 → 24,457.14). Confirmed across Diario El Mundo, Contaportable, Miranda Corporation and 2026 ISR calculators against Decreto Legislativo 293 / Decreto Ejecutivo 10. **[RESEARCH GAP — reviewer to confirm the exact Tramo II floor treatment and the small cuota-fija discontinuity at the exempt threshold against the consolidated Art. 37 LISR text.]**

### Tax Rate Brackets -- Monthly Withholding Table (Retención, Decreto Ejecutivo 10, 2025)

**Monthly Withholding Table**  _(Diario El Mundo / Ministerio de Hacienda Decreto Ejecutivo 10 (2025); DGII Tablas de Retención 700-DGII-DC-2025-01.)_

| Tramo | Monthly Income (USD) | Withholding | Cumulative at Top |
| --- | --- | --- | --- |
| I | 0.01 -- 550.00 | None (0) | USD 0.00 |
| II | 550.01 -- 895.24 | USD 17.67 + 10% on excess over 550.00 | USD 52.19 |
| III | 895.25 -- 2,038.10 | USD 60.00 + 20% on excess over 895.24 | USD 288.57 |
| IV | 2,038.11 and above | USD 288.57 + 30% on excess over 2,038.10 | -- |

**This is the authoritative published 2025 source. Annualise (×12) for the annual computation.**

> **Note on the USD 17.67 fixed amount (band II monthly):** the official decree publishes a small fixed amount in band II that is a rounding/transition artifact of the table (10% × (550.01 − 550.00) ≈ 0 at the lower bound). Apply the table figures **exactly as published** for monthly retención; for the annual settlement use the annual Art. 37 table above. **[RESEARCH GAP — reviewer to confirm]** the precise band-II fixed amount and lower-bound treatment.

### Non-Domiciled Individuals

**Non-Domiciled Individuals**  _(PwC El Salvador — Taxes on personal income.)_

| Basis | Rate |
| --- | --- |
| Salvadoran-source income (non-domiciled) | **30% flat** |

### Key Thresholds

**Key Thresholds**

| Threshold | Amount (USD) | Effective / Note | Source |
| --- | --- | --- | --- |
| Personal income-tax exempt threshold | 6,600.00 / year (550.00 / month) | Tax year 2025, raised from USD 4,064; Decreto Legislativo 293 / Decreto Ejecutivo 10 | Diario El Mundo; Ministerio de Hacienda |
| Filing exemption for salaried individuals | ≤ 9,100.00 / year | Salaried individuals with income ≤ USD 9,100 whose tax was fully withheld are **not required to file**; receive an embedded single deduction of USD 1,600 | PwC — Deductions / Tax administration |
| Embedded single deduction (no-file salaried) | 1,600.00 | Built into the ≤ USD 9,100 no-file regime | PwC — Deductions |
| IVA mandatory registration threshold | annual taxable + exempt operations > 5,714.29 (or total assets > 2,285.71) | Must register as IVA contributor (F-210); below both = "sujeto excluido" | Ministerio de Hacienda / DGII / Consortium Legal |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown domicile/residency status | STOP — do not apply a rate table without confirming domiciled vs non-domiciled |
| Unknown employment vs self-employment | Treat salaried income via retención table; self-employment via honorarios + annual settlement |
| Self-employed social contributions (AFP/ISSS) | Treat as **voluntary** (NOT compulsory for independent professionals) — do not auto-deduct |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown whether deduction limit applies | Apply statutory cap (medical/education USD 800/item; donations 20% of net income; voluntary pension 10% of reported income) |
| Unknown IVA registration status | Assume "sujeto excluido" (not registered) until threshold confirmed |
| Annual band III/IV fixed amounts | Use annualised monthly table; flag for reviewer (see RESEARCH GAP) |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** — bank statement for the full tax year (CSV, PDF, or pasted text), plus confirmation of (a) domicile status (domiciled vs non-domiciled), and (b) source of income (salaried employment vs independent professional / honorarios vs business).

**Recommended** — sales/honorarios invoices, F-14 monthly withholding records (10% professional-fee retención), prior year F-11, ISSS and AFP payment records (if applicable), IVA registration status (F-210 / NRC).

**Ideal** — complete income and expenditure account, asset register, retención certificates (constancias de retención) from payers, employment income details with retención de renta already withheld, voluntary pension contribution records.

**Refusal if minimum is missing — SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices/constancias = proceed with reviewer warning: "This F-11 was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid documentation and that income is Salvadoran-source."

### Refusal Catalogue

- **R-SV-1** — Domicile/residency unknown. "Domicile status determines whether the progressive table (domiciled) or the 30% flat rate (non-domiciled) applies. This skill cannot compute ISR without confirming whether the client is domiciled in El Salvador. Please confirm before proceeding."
- **R-SV-2** — Companies / partnerships / persona jurídica. "This skill covers individuals (persona natural) — salaried and independent professionals — only. Companies (persona jurídica) file a separate renta return with a different rate (corporate ISR). Escalate to a Salvadoran CPA."
- **R-SV-3** — Foreign-source income. "El Salvador operates a territorial system — only Salvadoran-source income is taxable for individuals. Foreign-source income, dual residency, or treaty positions require specialised analysis. Escalate to a Salvadoran CPA."
- **R-SV-4** — Capital gains / property disposals. "Capital gains (ganancia de capital) are taxed under a separate regime (generally 10%) and are out of scope for this income-tax skill. Escalate to a Salvadoran CPA."
- **R-SV-5** — Free zone / Zona Franca / maquila. "Free-zone and maquila incentive regimes (Ley de Zonas Francas) have special exemptions. Out of scope. Escalate to a Salvadoran CPA."
- **R-SV-6** — Arrears / DGII enforcement. "Client has outstanding ISR arrears or is subject to DGII enforcement. Late-payment surcharges and moratorium interest are severe. Do not advise. Escalate to a Salvadoran CPA immediately."
- **R-SV-7** — IVA return requested. "This skill covers income tax (ISR: F-11/F-14) only. For El Salvador IVA (F-07), use the el-salvador-iva skill."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement (Spanish terms common in Salvadoran banks: Banco Agrícola, Banco Cuscatlán, Davivienda, Banco Hipotecario, BAC). If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits / Abonos on Bank Statement)

**Income Patterns**

| Pattern | F-11 Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + TRANSFERENCIA, ABONO, DEPÓSITO, PAGO RECIBIDO | Renta gravada (business/professional income) | Salvadoran-source income | If IVA-registered, extract net (excl. 13% IVA) |
| HONORARIOS, SERVICIOS PROFESIONALES, CONSULTORÍA | Renta gravada (honorarios) | Professional income | Payer should have withheld 10% ISR (pago a cuenta) — see Section 5 |
| STRIPE PAYOUT, STRIPE TRANSFER | Renta gravada | Business income | Platform payout — match to underlying invoices; confirm Salvadoran-source |
| PAYPAL PAYOUT, PAYPAL TRANSFER | Renta gravada | Business income | Verify against invoices |
| WISE PAYOUT, WISE TRANSFER | Renta gravada | Business income | International platform payout — confirm source |
| UPWORK, FIVERR, TOPTAL | Renta gravada | Business income | Freelance platform — net of platform commission; confirm source |
| SALARIO, SUELDO, PLANILLA, NÓMINA, [employer name] | Renta de trabajo (salaried) | Employment income | Subject to monthly retención de renta — NOT honorarios |
| ALQUILER RECIBIDO, RENTA DE INMUEBLE | Renta de capital / arrendamiento | Rental income | Separate income category |
| INTERESES, INTERÉS GANADO | Renta de capital | Interest income | May be subject to separate withholding |
| DIVIDENDOS, REPARTO DE UTILIDADES | Renta de capital | Dividend income | Subject to separate dividend tax |
| DEVOLUCIÓN DGII, REINTEGRO RENTA, REINTEGRO HACIENDA | EXCLUDE | Not income | Tax refund from prior year |
| REMESA, REMESA FAMILIAR | EXCLUDE (generally) | Not taxable income | Family remittances are not ISR income — confirm nature |

### 3.2 Expense Patterns (Debits / Cargos) -- Fully Deductible (business / professional)

**Fully Deductible Expense Patterns**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| ALQUILER OFICINA, RENTA LOCAL, ARRENDAMIENTO [commercial] | Office rent | Deductible | Dedicated business premises |
| CONTADOR, AUDITOR, CONTABILIDAD, CPA | Accountancy fees | Deductible |  |
| ABOGADO, NOTARIO, ASESORÍA LEGAL (business) | Legal fees | Deductible | Must be business-related |
| PAPELERÍA, ÚTILES DE OFICINA, LIBRERÍA | Office supplies | Deductible |  |
| PUBLICIDAD, MARKETING, GOOGLE ADS, META ADS, FACEBOOK ADS | Marketing/advertising | Deductible |  |
| CAPACITACIÓN, CURSO, SEMINARIO, CONGRESO | Training/CPD | Deductible | Must relate to current business |
| COMISIÓN BANCARIA, CARGO BANCARIO, MANTENIMIENTO CUENTA | Bank charges | Deductible | Business account only |
| STRIPE FEE, PAYPAL FEE, COMISIÓN PROCESAMIENTO | Payment processing fees | Deductible |  |
| DOMINIO, HOSTING, CLOUDFLARE, AWS, DIGITALOCEAN | IT infrastructure | Deductible | Capitalise if a long-lived asset (see 3.7) |

> **Important:** Deductibility of business expenses applies to **business income and independent professionals operating a business**. Salaried individuals do **not** deduct business expenses against salary; they use the embedded single deduction / capped personal deductions (Section 5). Confirm income type before deducting.

### 3.3 Expense Patterns (Debits) -- SaaS and Software

**SaaS and Software**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring subscription = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |
| LICENCIA PERPETUA / SOFTWARE (capital) | Capital item | Capitalise & depreciate | Long-lived perpetual licence — see 3.7 |

### 3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)

**Utilities**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| AES, DELSUR, CAESS, EEO (electricity) | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| ANDA (agua) | Water | T2 if home office | Business portion only |
| TIGO, CLARO, MOVISTAR (internet/fixed) | Telecoms/broadband | T2 | Business use portion only; default 0% if mixed |
| TIGO, CLARO, MOVISTAR (mobile) | Phone | T2 | Business use portion only |

### 3.5 Expense Patterns (Debits) -- Travel

**Travel**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| AVIANCA, COPA, VOLARIS, AEROMÉXICO | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| UBER, INDRIVE, TAXI | Local transport | Deductible if business purpose |  |
| COMBUSTIBLE, GASOLINA, PUMA, UNO, TEXACO, GASOLINERA | Vehicle fuel | T2 — business % only | Requires mileage log |
| PARQUEO, ESTACIONAMIENTO | Parking | T2 — business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANTE, ALMUERZO, CENA, ENTRETENIMIENTO | Entertainment/meals | NOT deductible | Personal/entertainment — generally blocked |
| SUPERMERCADO, SÚPER SELECTOS, WALMART, DESPENSA, GROCERIES | Personal expenses | NOT deductible | Private living costs |
| MULTA, RECARGO, INFRACCIÓN, MORA | Fines/penalties | NOT deductible | Public policy |
| PAGO RENTA DGII, PAGO ISR, IMPUESTO SOBRE LA RENTA | Income tax payments | NOT deductible | Income tax cannot reduce income |
| RETIRO PERSONAL, RETIRO CAJERO (personal), GASTO PERSONAL | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- Capital Items (depreciate)

**Capital Items**

| Pattern | Category | Indicative Rate | Notes |
| --- | --- | --- | --- |
| LAPTOP, COMPUTADORA, MACBOOK, EQUIPO DE CÓMPUTO | Computer hardware | [confirm Art. 30 LISR] | Capitalise & depreciate |
| IMPRESORA, ESCÁNER, FOTOCOPIADORA | Office equipment | [confirm Art. 30 LISR] | Capitalise & depreciate |
| MOBILIARIO, ESCRITORIO, SILLA, ARCHIVO | Furniture/fittings | [confirm Art. 30 LISR] | Capitalise & depreciate |
| VEHÍCULO, CARRO (business) | Motor vehicle | [confirm Art. 30 LISR] | Business % only |

> **[RESEARCH GAP — reviewer to confirm]** Specific statutory depreciation rates/useful lives under Art. 30 LISR were not re-confirmed in this research pass. Treat the rates below as **indicative only** and confirm against Art. 30 LISR before applying.

### 3.8 Exclusions (Neither Income nor Expense)

**Exclusions**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERENCIA PROPIA, CUENTA PROPIA, ENTRE CUENTAS | EXCLUDE | Own-account transfer |
| PAGO PRÉSTAMO, ABONO PRÉSTAMO, CUOTA PRÉSTAMO | EXCLUDE | Loan principal movement |
| ISSS, COTIZACIÓN ISSS | See Section 5 | Health contribution — relevant only if employed/voluntarily affiliated |
| AFP, AFP CONFÍA, AFP CRECER, COTIZACIÓN AFP | See Section 5 | Pension contribution — relevant only if employed/voluntarily affiliated |
| PAGO IVA DGII, F-07 PAGO | EXCLUDE | IVA liability payment, not income-tax expense |
| PAGO A CUENTA, ANTICIPO RENTA, RETENCIÓN 10% | Credit against annual ISR | Advance/withholding — credited, not an expense |

### 3.9 Salvadoran Banks -- Statement Format Reference

**Bank Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Banco Agrícola | TRANSFERENCIA, ABONO, CARGO, COMISIÓN | PDF/CSV; date DD/MM/YYYY; description holds counterparty + reference |
| Banco Cuscatlán | TRANSFERENCIA, PAGO, CARGO | PDF/CSV |
| Davivienda SV | ABONO, CARGO, TRANSFERENCIA | PDF; merchant name in description |
| BAC Credomatic | PAGO, COMPRA, TRANSFERENCIA | CSV available; card transactions show merchant |
| Banco Hipotecario | TRANSFERENCIA, CARGO, ABONO | PDF; shorter descriptions |

## Section 4 -- Worked Examples

All amounts in **USD** (El Salvador is dollarized). Each example recomputed end-to-end.

### Example 1 -- Salaried Employee Monthly Retención (mid-band)

**Input line:**
`30/04/2025 ; ABONO PLANILLA ; EMPRESA TECNOSV S.A. DE C.V. ; SALARIO ABRIL ; +1,200.00 ; USD`

**Reasoning:**
Salaried income of USD 1,200/month. Falls in monthly band III (895.25 – 2,038.10): withholding = USD 60.00 + 20% × (1,200.00 − 895.24) = 60.00 + 20% × 304.76 = 60.00 + 60.952 = **USD 120.95**. (ISSS/AFP are withheld separately — see Section 5.)

**Classification:** Retención de renta = USD 120.95 for the month (employment income).

### Example 2 -- Independent Professional Fee with 10% Withholding (honorarios)

**Input line:**
`15/03/2025 ; ABONO ; ALCALDÍA DE SANTA TECLA ; HONORARIOS CONSULTORÍA ; +900.00 ; USD`

**Reasoning:**
Professional fee. The payer should withhold 10% ISR as pago a cuenta on the gross fee: 10% × USD 1,000 gross = USD 100, so the net deposit of USD 900 implies gross USD 1,000 (if the USD 900 is the net after withholding). The USD 100 withheld is an **advance** credited against the annual progressive ISR on the F-11 — it is not a final tax. If the client is IVA-registered, the gross also carries 13% IVA handled separately on F-07.

**Classification:** Renta gravada (honorarios) gross USD 1,000; pago a cuenta credit USD 100 (reported on F-14 by the payer).

### Example 3 -- SaaS Subscription (Deductible — business income)

**Input line:**
`01/04/2025 ; CARGO ; ADOBE SYSTEMS ; CREATIVE CLOUD ABR ; -29.99 ; USD`

**Reasoning:**
Monthly SaaS subscription used in the business. Recurring operating expense, fully deductible against business/professional income. (Not available to a purely salaried client.)

**Classification:** Deductible business expense = USD 29.99.

### Example 4 -- Personal Expense (Not Deductible)

**Input line:**
`22/04/2025 ; COMPRA ; SÚPER SELECTOS ; ; -85.40 ; USD`

**Reasoning:**
Supermarket purchase — private living cost. Not wholly-and-exclusively for the business. Not deductible.

**Classification:** NOT deductible. Exclude from expenses.

### Example 5 -- Annual ISR Settlement (self-employed professional)

**Inputs:** Domiciled independent professional. Gross honorarios USD 30,000; deductible business expenses USD 8,000; pago a cuenta (10%) already withheld during year USD 3,000. No compulsory AFP/ISSS (independent professional — voluntary only, none paid).

**Computation:**
- Net taxable income = 30,000 − 8,000 = **USD 22,000**.
- Band III applies (10,742.87 – 24,457.14): ISR = cuota fija 720.00 + 20% × (22,000.00 − 10,742.86) = 720.00 + 20% × 11,257.14 = 720.00 + 2,251.43 = **USD 2,971.43**.
- Less pago a cuenta credit USD 3,000 → **refund of USD 28.57** (3,000 − 2,971.43).

**Classification:** Annual ISR liability USD 2,971.43; net position = USD 28.57 refund on F-11.

### Example 6 -- High-Earner Annual ISR (top band)

**Inputs:** Domiciled individual, annual net income USD 40,000.

**Computation:**
- Band IV applies (≥ 24,457.15): ISR = cuota fija 3,462.86 + 30% × (40,000.00 − 24,457.14) = 3,462.86 + 30% × 15,542.86 = 3,462.86 + 4,662.86 = **USD 8,125.72**.

**Classification:** Annual ISR liability USD 8,125.72.

### Example 7 -- Own-Account Transfer (Exclude)

**Input line:**
`15/05/2025 ; TRANSFERENCIA ; CUENTA PROPIA - AHORRO ; ; -2,000.00 ; USD`

**Reasoning:**
Transfer between own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Territorial System

- **Territorial system** — Only Salvadoran-source income is taxable for individuals. Foreign-source income of residents is generally outside scope. Confirm source before including any item in renta gravada.  _(LISR (Decreto No. 134).)_

### 5.2 Fiscal Year and Filing

- **Fiscal year and filing** — Fiscal year = calendar year (1 Jan – 31 Dec). Annual income tax return (F-11) due within 4 months of year-end → tax payable by 30 April of the following year.  _(Art. 13 LISR; Código Tributario; Art. 48 LISR)_

### 5.3 Exempt Threshold and Progressive Scale

- **Exempt threshold and progressive scale** — Personal income-tax exempt threshold = USD 6,600/year (USD 550/month) for tax year 2025 (raised from USD 4,064). Domiciled individuals taxed on the 4-band progressive scale 0% / 10% / 20% / 30%. Top marginal rate 30% applies above ~USD 24,457.14 annual net income. Non-domiciled individuals: flat 30% on Salvadoran-source income.  _(Decreto Legislativo 293 / Decreto Ejecutivo 10; Art. 37 LISR)_

### 5.4 Monthly Salary Withholding (Retención de Renta)

**Monthly Salary Withholding**  _(Diario El Mundo / Ministerio de Hacienda Decreto Ejecutivo 10 (2025).)_

| Monthly Income (USD) | Withholding |
| --- | --- |
| 0.01 – 550.00 | None |
| 550.01 – 895.24 | USD 17.67 + 10% over 550.00 |
| 895.25 – 2,038.10 | USD 60.00 + 20% over 895.24 |
| 2,038.11 and above | USD 288.57 + 30% over 2,038.10 |

Employers withhold monthly per the official retención table (Decreto Ejecutivo 10/2025) and remit to DGII on **F-14**:

### 5.5 Self-Employed Professionals — 10% Withholding (Pago a Cuenta)

- **10% withholding pago a cuenta** — Payers of professional fees (honorarios) withhold 10% ISR as an advance (pago a cuenta) on the gross fee. This advance is credited against the annual progressive ISR on the F-11 — it is not a final tax. Reported monthly by the payer on F-14.  _(Código Tributario; DGII OPJ rulings (Retención del 10% de Renta a servicios profesionales).)_

### 5.6 Filing Exemption for Salaried Individuals

- **Filing exemption for salaried individuals** — Salaried individuals earning ≤ USD 9,100/year whose tax was fully withheld are not required to file F-11. They receive an embedded single deduction of USD 1,600.  _(PwC — Deductions / Tax administration)_

### 5.7 Deductions for Filers (over USD 9,100)

**Deductions for Filers**  _(PwC — Deductions; LISR)_

| Deduction | Limit |
| --- | --- |
| Medical expenses | up to USD 800 |
| Education expenses | up to USD 800 |
| Charitable donations | up to 20% of net income |
| Voluntary pension contributions | up to 10% of reported income |

Individuals over the USD 9,100 threshold may deduct (PwC — Deductions; LISR). *Apply caps strictly. Medical and education are separate USD 800 limits per item per PwC.*

### 5.8 ISSS (Health / Social Security)

**ISSS**  _(Ley del Seguro Social)_

| Party | Rate | Cap | Max Monthly |
| --- | --- | --- | --- |
| Employee | 3% of monthly salary | insurable salary capped at USD 1,000/month | USD 30 |
| Employer | 7.50% of monthly salary | insurable salary capped at USD 1,000/month | USD 75 |

- **ISSS cap and applicability** — Above USD 1,000 insurable salary, the contribution is fixed at USD 30 (employee) / USD 75 (employer). ISSS is mandatory for employees, NOT compulsory for independent professionals (voluntary affiliation possible).  _(PwC — Other taxes; ISSS.)_

### 5.9 AFP (Pension Fund)

**AFP**  _(Ley Integral del Sistema de Pensiones)_

| Party | Rate |
| --- | --- |
| Employee | 7.25% of Ingreso Base de Cotización (IBC) |
| Employer | 8.75% of IBC |
| **Total** | **16.00%** |

- **No cap since Jan 2023** — No statutory maximum insurable salary since January 2023 — the tope cotizable was eliminated; contributions apply to the full IBC. Some payroll calculators cite a referential cap (~USD 7,045.06 in 2026) but this is not a current legal ceiling — apply no cap. **[RESEARCH GAP — reviewer to confirm]** whether any referential maximum insurable salary applies in 2025.  _(PwC — Other taxes; SSF; Ley Integral del Sistema de Pensiones.)_

### 5.10 Combined Payroll Contribution Summary (Employee on Salary)

**Combined Payroll Contribution Summary**

| Contribution | Employee | Employer | Combined |
| --- | --- | --- | --- |
| ISSS (health) | 3.00% | 7.50% | 10.50% |
| AFP (pension) | 7.25% | 8.75% | 16.00% |
| **TOTAL social contributions** | **10.25%** | **16.25%** | **26.50%** |

For an employee earning at or below USD 1,000/month (so ISSS is not yet capped and AFP has no cap), the social-contribution percentages are as shown. *Employee column: 3.00 + 7.25 = 10.25%. Employer column: 7.50 + 8.75 = 16.25%. Combined: 10.50 + 16.00 = 26.50%; cross-check 10.25 + 16.25 = 26.50%. ✓ Above USD 1,000/month, ISSS becomes a fixed USD 30 (employee) / USD 75 (employer) while AFP percentages continue uncapped. Income-tax retención de renta (Section 5.4) is in addition to these. INSAFORP employer training levy is separate — see 5.11.*

### 5.11 INSAFORP (Employer Training Levy)

- **INSAFORP** — Employers with 10+ workers pay a training contribution of approximately 1% of payroll (employee 0%). **[RESEARCH GAP — reviewer to confirm]** the precise current INSAFORP/INCAF rate and threshold — not re-confirmed against primary sources this pass.

### 5.12 IVA Interaction

- **IVA interaction** — Standard IVA rate 13% (Ley del IVA). Mandatory IVA registration once annual taxable+exempt operations exceed USD 5,714.29 (or total assets > USD 2,285.71); below both, a "sujeto excluido" regime applies. For IVA-registered self-employed: report business income net of 13% IVA; IVA collected on sales is a liability to DGII, not income. (For the IVA return itself, use el-salvador-iva / F-07.)  _(Ley del IVA)_

### 5.13 Non-Deductible Expenses

**Non-Deductible Expenses**

| Expense | Reason |
| --- | --- |
| Entertainment / personal meals | Not wholly-and-exclusively business |
| Personal living expenses | Not business-related |
| Fines and penalties (multas/recargos) | Public policy |
| Income tax (ISR) itself | Tax on income |
| Drawings / personal withdrawals | Not an expense |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction

- **Home office deduction** — Calculate proportion of home used for business (dedicated room(s) / floor area). Apply that percentage to rent, electricity (AES/DELSUR/CAESS), water (ANDA), internet. Dual-use rooms do NOT qualify. Conservative default: 0% until reviewer confirms arrangement. Flag for reviewer.

### 6.2 Motor Vehicle Business Use

- **Motor vehicle business use** — Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible. Client must keep a mileage log. Conservative default: 0% business use until log provided. Flag for reviewer.

### 6.3 Phone / Internet Mixed Use

- **Phone / internet mixed use** — Business-use portion only; client provides reasonable estimate. Conservative default: 0% until business percentage confirmed.

### 6.4 Bad Debt Write-Off

- **Bad debt write-off** — Deductible only if income was previously declared, all recovery steps taken, and debt genuinely irrecoverable. Flag for reviewer to confirm all three.

### 6.5 Depreciation Method & Rates (Art. 30 LISR)

- **Depreciation method & rates** — Capital assets must be depreciated, not expensed. **[RESEARCH GAP — reviewer to confirm]** the statutory rates/useful lives under Art. 30 LISR. Flag for reviewer.  _(Art. 30 LISR)_

### 6.6 Voluntary AFP/ISSS for Self-Employed

- **Voluntary AFP/ISSS for self-employed** — Independent professionals may affiliate voluntarily; voluntary pension contributions deductible up to 10% of reported income (Section 5.7). Flag for reviewer to confirm affiliation and amounts.

### 6.7 Source of Income (Territoriality)

- **Source of income territoriality** — Whether platform/foreign-client income is Salvadoran-source can be borderline. Flag for reviewer where source is unclear.

## Section 7 -- Excel Working Paper Template

```
EL SALVADOR ISR -- F-11 WORKING PAPER (PERSONA NATURAL)
Tax Year: 2025
Client: ___________________________
Domicile: Domiciled / Non-domiciled
Income type: Salaried / Independent professional (honorarios) / Business

A. RENTA GRAVADA (TAXABLE INCOME)
  A1. Salaried income (renta de trabajo)         ___________
  A2. Professional fees / honorarios (gross)      ___________
  A3. Business income (net of 13% IVA if reg.)    ___________
  A4. Rental / capital income (if in scope)       ___________
  A5. TOTAL renta gravada                          ___________

B. DEDUCCIONES (business income / professionals only)
  B1. Office rent / arrendamiento                 ___________
  B2. Accountancy / legal fees                     ___________
  B3. Office supplies / papelería                  ___________
  B4. Software subscriptions                       ___________
  B5. Marketing / publicidad                       ___________
  B6. Bank charges / comisiones                    ___________
  B7. Travel (business)                            ___________
  B8. Telecoms (business %)                         ___________
  B9. Home office (% of utilities/rent)            ___________
  B10. Vehicle expenses (business %)               ___________
  B11. Depreciation (Art. 30 LISR — confirm rate)  ___________
  B12. Other allowable expenses                    ___________
  B13. TOTAL deducciones                           ___________

C. PERSONAL DEDUCTIONS (filers over USD 9,100)
  C1. Medical (max USD 800)                        ___________
  C2. Education (max USD 800)                       ___________
  C3. Donations (max 20% of net income)            ___________
  C4. Voluntary pension (max 10% of income)        ___________
  C5. TOTAL personal deductions                    ___________

D. NET TAXABLE INCOME (A5 - B13 - C5)             ___________

E. ISR COMPUTATION (pass to deterministic engine)
  E1. ISR per Art. 37 table                        ___________
  E2. Less: pago a cuenta / 10% retención          ___________
  E3. Less: retención de renta (salary)            ___________
  E4. ISR due / refund                             ___________

REVIEWER FLAGS:
  [ ] Domicile status confirmed (domiciled/non-domiciled)?
  [ ] Income source confirmed (Salvadoran-source only)?
  [ ] Income type confirmed (salaried / honorarios / business)?
  [ ] Annual band III/IV fixed amounts re-verified vs Decreto Ejecutivo 10?
  [ ] Depreciation rates confirmed vs Art. 30 LISR?
  [ ] Home office / vehicle / phone business % confirmed?
  [ ] Personal deduction caps applied (USD 800 / 20% / 10%)?
  [ ] IVA registration status confirmed (sujeto excluido vs registered)?
  [ ] Pago a cuenta / retención credits supported by constancias?
```

## Section 8 -- Bank Statement Reading Guide

### Salvadoran Bank Statement Formats

**Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Banco Agrícola | PDF, CSV | Fecha, Descripción, Cargo, Abono, Saldo | Most common; description contains counterparty + reference |
| Banco Cuscatlán | PDF, CSV | Fecha, Concepto, Débito, Crédito, Saldo |  |
| Davivienda SV | PDF | Fecha, Descripción, Valor, Saldo | Merchant name in description |
| BAC Credomatic | PDF, CSV | Fecha, Referencia, Débito, Crédito | Card transactions show merchant |
| Banco Hipotecario | PDF | Fecha, Detalle, Cargo, Abono | Shorter descriptions |

### Key Salvadoran Banking / Tax Terms

**Key Terms**

| Term | English | Classification Hint |
| --- | --- | --- |
| ABONO | Credit / deposit | Potential income |
| CARGO / DÉBITO | Debit / charge | Expense — check merchant |
| TRANSFERENCIA / TRF | Transfer | Check direction for income/expense |
| HONORARIOS | Professional fees | Renta gravada — 10% withholding likely |
| SALARIO / SUELDO / PLANILLA | Salary / payroll | Employment income (retención de renta) |
| RETENCIÓN | Withholding | 10% honorarios or salary retención — credit |
| PAGO A CUENTA | Advance income tax | Credit against annual ISR |
| COMISIÓN | Fee / commission | Bank charge (deductible) or platform fee |
| INTERESES | Interest | Interest income or bank charge |
| REMESA | Remittance | Generally not ISR income — confirm |
| DEVOLUCIÓN / REINTEGRO | Refund | Exclude (prior-year tax refund) |
| ISSS / AFP | Health / pension contribution | Social security — see Section 5 |
| IVA | Value added tax (13%) | Liability, not income-tax expense |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDIENTE — reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- EL SALVADOR INCOME TAX (ISR)
1. Are you domiciled in El Salvador for tax purposes (domiciled / non-domiciled)?
2. What is your main income type: salaried employee, independent professional (honorarios), or business?
3. Is all your income Salvadoran-source, or do you have foreign-source income?
4. Are you registered for IVA (have an NRC), or below the USD 5,714.29 threshold (sujeto excluido)?
5. Did payers withhold 10% on your professional fees (do you have constancias de retención)?
6. Were you in an employer payroll with ISSS/AFP withheld? Or do you contribute voluntarily?
7. Home office: dedicated room or shared space? If dedicated, what % of floor area?
8. Vehicle: used for business? What % is business use? Mileage log kept?
9. Phone/internet: what % is business use?
10. Personal deductions: medical, education, donations, voluntary pension amounts?
11. Any capital assets purchased during the year?
```

## Section 10 -- Reference Material

### Key Legislation & Authority References

**Key Legislation & Authority References**

| Topic | Reference |
| --- | --- |
| Income tax rates / progressive table | Art. 37 LISR (Decreto No. 134), as reformed 2025 |
| Exempt threshold (USD 6,600) | Decreto Legislativo 293 (30 Apr 2025) / Decreto Ejecutivo 10 (2025) |
| Monthly retención table | Decreto Ejecutivo 10 (2025); DGII Tablas de Retención 700-DGII-DC-2025-01 |
| 10% professional-fee withholding | Código Tributario; DGII OPJ ruling (12101-OPJ-0248-2005) |
| Territorial system | LISR (Decreto No. 134) |
| Filing / penalties | Código Tributario (Decreto No. 230); Art. 48 LISR |
| ISSS (health) | Ley del Seguro Social |
| AFP (pensions) | Ley Integral del Sistema de Pensiones; SSF parameters |
| IVA (13%) | Ley del IVA |
| Minimum wage (eff. 1 Jun 2025) | Decreto Ejecutivo 11 (2025); MTPS |

### Forms (DGII e-services, mh.gob.sv)

**Forms**

| Form | Purpose | Deadline |
| --- | --- | --- |
| **F-11** — Declaración del Impuesto sobre la Renta | Annual personal/business income tax return (domiciled individuals), filed online | Within 4 months of year-end → by 30 April of following year |
| **F-14** — Declaración mensual de Pago a Cuenta e Impuesto Retenido Renta | Monthly remittance of income tax withheld (incl. 10% on professional fees) and pago a cuenta | First 10 business days of the following month |
| **F-07** — Declaración de IVA | Monthly VAT return (13%) for registered contributors | First 10 business days of the following month |
| **F-210** — Inscripción / Registro de Contribuyente (NRC) | Register as IVA contributor (required once IVA threshold USD 5,714.29 reached) | Before/within 15 days of commencing taxable activity |

> **[RESEARCH GAP — reviewer to confirm]** Form codes (F-11/F-14/F-07/F-210) reflect standard DGII practice; confirm current form codes on the Ministerio de Hacienda e-services portal.

### Minimum Wage (effective 1 June 2025, Decreto Ejecutivo 11)

**Minimum Wage**

| Sector | Monthly (USD) | Daily (USD) | Source |
| --- | --- | --- | --- |
| Industry / Commerce / Services | 408.80 | 13.44 | MTPS; Consortium Legal |
| Textile maquila / apparel | 402.32 | 13.23 | Consortium Legal / MTPS |
| Agriculture (coffee, sugar, livestock, fishing) | 305.23 | 10.04 | Consortium Legal / MTPS |

*Industry/Commerce/Services: USD 408.80/month, USD 13.44/day, USD 1.68/hour (Decreto Ejecutivo 11, +12%).*

### Penalties (Código Tributario)

**Penalties**  _(Código Tributario; Consortium Legal.)_

| Type | Amount |
| --- | --- |
| Late filing of income tax return (presentación extemporánea) | 5% of tax if ≤1 month late; 10% if 1–2 months; 15% if 2–3 months; 20% if >3 months. Minimum: not less than 2 minimum salaries; if no tax due, 1 minimum salary |
| Interest on late payment | Statutory moratorium interest (Ley de Interés Moratorio), higher rate after 60 days. **[RESEARCH GAP — reviewer to confirm]** exact current rate |
| Failure to register as taxpayer | Fines under Código Tributario formal-obligation provisions (Art. 235+), generally in minimum salaries |

### Test Suite

**Test 1 — Salaried monthly retención (band III).**
Input: Monthly salary USD 1,200, domiciled employee.
Expected: Retención = 60.00 + 20% × (1,200.00 − 895.24) = 60.00 + 60.95 = **USD 120.95**.

**Test 2 — Salaried monthly retención (band II).**
Input: Monthly salary USD 700.
Expected: Retención = 17.67 + 10% × (700.00 − 550.00) = 17.67 + 15.00 = **USD 32.67**.

**Test 3 — Exempt salary.**
Input: Monthly salary USD 500.
Expected: Retención = **USD 0.00** (below USD 550 threshold).

**Test 4 — Self-employed annual settlement (band III).**
Input: Domiciled professional, net taxable income USD 22,000, pago a cuenta withheld USD 3,000.
Expected: ISR = 720.00 + 20% × (22,000.00 − 10,742.86) = 720.00 + 2,251.43 = **USD 2,971.43**; net = **USD 28.57 refund**.

**Test 5 — High-earner annual (band IV).**
Input: Domiciled individual, annual net income USD 40,000.
Expected: ISR = 3,462.86 + 30% × (40,000.00 − 24,457.14) = 3,462.86 + 4,662.86 = **USD 8,125.72**.

**Test 6 — Non-domiciled flat rate.**
Input: Non-domiciled individual, Salvadoran-source income USD 20,000.
Expected: ISR = 30% × 20,000.00 = **USD 6,000.00** (flat, no progressive bands).

**Test 7 — ISSS cap.**
Input: Employee salary USD 1,500/month.
Expected: ISSS employee = min(3% × 1,500, 30) = min(45, 30) = **USD 30.00**; ISSS employer = min(7.50% × 1,500, 75) = min(112.50, 75) = **USD 75.00** (insurable salary capped at USD 1,000).

**Test 8 — AFP no cap.**
Input: Employee IBC USD 2,000/month.
Expected: AFP employee = 7.25% × 2,000 = **USD 145.00**; AFP employer = 8.75% × 2,000 = **USD 175.00** (no statutory ceiling since Jan 2023).

**Test 9 — No-file salaried exemption.**
Input: Salaried individual, annual income USD 8,500, fully withheld.
Expected: **Not required to file** F-11 (≤ USD 9,100); embedded single deduction USD 1,600 applies.

## PROHIBITIONS

- NEVER apply a rate table without confirming domicile (domiciled vs non-domiciled)
- NEVER include foreign-source income for an individual — El Salvador is territorial
- NEVER present the annual band III/IV fixed amounts as definitive — they are annualised/inferred and flagged for reviewer
- NEVER auto-deduct ISSS/AFP for an independent professional — they are NOT compulsory (voluntary only)
- NEVER apply a maximum insurable salary cap to AFP — the cap was eliminated in January 2023
- NEVER deduct business expenses against pure salaried income — use the embedded/capped personal deductions
- NEVER allow income tax (ISR) itself as a deduction
- NEVER allow fines or penalties (multas/recargos) as a deduction
- NEVER treat the 10% pago a cuenta as a final tax — it is an advance credited on the F-11
- NEVER include IVA collected on sales in renta gravada for IVA-registered clients
- NEVER exceed the personal deduction caps (medical/education USD 800 each; donations 20%; voluntary pension 10%)
- NEVER present tax calculations as definitive — always label as estimated and pending reviewer sign-off

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
