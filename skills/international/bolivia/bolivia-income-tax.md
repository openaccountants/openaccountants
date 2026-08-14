---
name: bolivia-income-tax
description: Use this skill whenever asked about Bolivia personal income tax for self-employed individuals, independent professionals, or employees. Trigger on phrases like "how much tax do I pay in Bolivia", "RC-IVA", "Regimen Complementario al IVA", "Formulario 610", "Formulario 110", "impuesto a la renta Bolivia", "retencion RC-IVA", "aportes a la Gestora", "independent professional tax Bolivia", "aguinaldo", "salario minimo nacional", "IUE-BE", "beneficiarios del exterior", "impuesto a las grandes fortunas", "IGF", or any question about computing or filing personal income tax for a Bolivian individual, self-employed person, or independent professional. Also trigger when classifying a Bolivian bank statement, computing the 13% RC-IVA, the VAT-credit offset on Form 110, social security contributions (Gestora/Caja de Salud), or non-resident withholding. This skill covers RC-IVA (13% flat), the VAT-credit invoice mechanism, social security contributions, the IUE-BE non-resident withholding, the IGF wealth tax, forms 610/110/530, deadlines, and penalties. ALWAYS read this skill before touching any Bolivian income tax work.
version: 0.1
jurisdiction: BO
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Bolivia Income Tax (RC-IVA) -- Self-Employed and Individuals

## Bolivia Income Tax (RC-IVA) -- Self-Employed and Individuals Skill v0.1

Tier 2 (research-verified). Figures below are drawn from PwC Worldwide Tax Summaries, the official SIN/SIAT site, the LexiVox text of DS 5383, and Bolivian professional sources. They have NOT yet been signed off by a Bolivian-licensed accountant (Contador Público Autorizado / auditor). Treat every output as a draft for professional review. Items marked **[RESEARCH GAP -- reviewer to confirm]** require verification against primary statute before filing.

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Bolivia (Estado Plurinacional de Bolivia) |
| Tax | RC-IVA -- Regimen Complementario al Impuesto al Valor Agregado (personal income tax) |
| Currency | BOB only (Boliviano, Bs) |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Ley 843 (Texto Ordenado), Titulo II, arts. 19-36 (RC-IVA); reglamento DS 21531 |
| Supporting legislation | Ley 1448 (2021) + DS 4850 -- independent professionals moved to RC-IVA from 1 Jan 2023; Ley 065 de Pensiones (2010), modified by Ley 1582 (2024); Ley 1357 (IGF wealth tax, 2020); Ley 843 art. 51 (IUE-BE non-resident WHT); DS 5383 (1 May 2025, minimum wage); Codigo Tributario Ley 2492 (penalties) |
| Tax authority | Servicio de Impuestos Nacionales (SIN) -- siat.impuestos.gob.bo / impuestos.gob.bo |
| Social security | Gestora Publica de la Seguridad Social de Largo Plazo (gestora.bo); APS (regulator) |
| Labor / minimum wage | Ministerio de Trabajo, Empleo y Prevision Social (mintrabajo.gob.bo) |
| Filing portal | SIAT (Oficina Virtual) |
| Filing deadline (self-employed / direct) | Quarterly, within 20 days after quarter-end (20 Apr / 20 Jul / 20 Oct / 20 Jan) -- Form 610 |
| Filing deadline (employees) | None -- employer withholds and files a monthly consolidated return |
| Validated by | Pending -- requires sign-off by a Bolivian-licensed accountant (CPA / auditor) |
| Validation date | Pending |
| Skill version | 0.1 |

### The Headline: Bolivia Has a FLAT 13% Personal Income Tax

- **RC-IVA flat rate** — RC-IVA is Bolivia's personal income tax: a flat 13% on Bolivian-source income from labour and capital under Ley 843, Titulo II. There are no progressive brackets.  _(PwC, https://taxsummaries.pwc.com/bolivia/individual/taxes-on-personal-income)_
- **Territorial taxation** — Individuals are taxed only on Bolivian-source income regardless of residency or citizenship; foreign-source income is not taxed. The only exception is the IGF wealth tax, which reaches residents' worldwide assets.  _(PwC, taxes-on-personal-income)_

### Personal Income Tax Rate

**Personal Income Tax Rate table**  _(PwC, taxes-on-personal-income)_

| Tax | Type | Rate | Base | Source |
| --- | --- | --- | --- | --- |
| RC-IVA (personal income tax) | Flat | **13%** | Bolivian-source net income (gross less social security contributions and statutory deductions); offset by VAT credits | PwC, taxes-on-personal-income |

### IGF -- Impuesto a las Grandes Fortunas (Wealth Tax) -- STATUS UNCERTAIN

[RESEARCH GAP -- reviewer to confirm status.] Ley 1357 (2020) and PwC confirm the IGF was in force with the brackets below. However Bolivian press (El Pais, 25 Nov 2025) reports the new Rodrigo Paz government eliminated the IGF as one of its first measures. The exact repeal instrument, its effective date, and whether it still applies for fiscal year 2025 (assessed at 31 Dec 2025) could not be confirmed from an authoritative source. Verify the current legal status before computing. Do NOT compute IGF unless net wealth clearly exceeds Bs 30,000,000 AND you have confirmed the law is still in force.

**IGF net wealth band table**  _(https://impuestos.com.bo/impuesto-a-las-grandes-fortunas-ley-1357/)_

| Net wealth band (Bs) | Rate | Source |
| --- | --- | --- |
| 30,000,000 -- 40,000,000 | 1.4% | https://impuestos.com.bo/impuesto-a-las-grandes-fortunas-ley-1357/ |
| 40,000,000 -- 50,000,000 | 1.9% | https://impuestos.com.bo/impuesto-a-las-grandes-fortunas-ley-1357/ |
| over 50,000,000 | 2.4% | https://impuestos.com.bo/impuesto-a-las-grandes-fortunas-ley-1357/ |

- **IGF threshold and residency test** — net wealth exceeding Bs 30,000,000 at 31 December; residency test = 183 days in any 12-month period  _(impuestos.com.bo / Ley 1357)_

### Key Thresholds (2025)

**Key Thresholds (2025) table**

| Item | Value | Source |
| --- | --- | --- |
| National minimum wage (Salario Minimo Nacional, SMN) 2025 | **Bs 2,750/month** (+10% over 2024's Bs 2,500), retroactive to 1 Jan 2025 | DS 5383 art. 7, https://www.lexivox.org/norms/BO-DS-N5383.html |
| RC-IVA non-taxable minimum (employees) | **2 x SMN = 2 x Bs 2,750 = Bs 5,500/month** deducted from net taxable base | https://www.rigobertoparedes.com/en/bolivia-2025-salary-increase/ |
| RC-IVA presumed VAT credit (employees, 2025 onward) | **13% of 1 SMN = Bs 357.50/month** (cut in 2025 from 13% of 2 SMN = Bs 715 under DS 5383) | https://www.rigobertoparedes.com/en/bolivia-2025-salary-increase/ |
| Practical RC-IVA withholding bite (employees, 2025) | approx **Bs 9,451/month gross** -- above this, employees generally owe RC-IVA unless they present sufficient VAT-credit invoices on Form 110 | https://www.rigobertoparedes.com/en/bolivia-2025-salary-increase/ |
| RE-IVA VAT refund program (Ley 1355) | individuals earning up to **Bs 9,000/month** can claim a refund of 5% of invoiced purchases | https://taxsummaries.pwc.com/bolivia/individual/significant-developments |
| IGF wealth tax threshold | net wealth exceeding **Bs 30,000,000** at 31 Dec (status uncertain -- see above) | https://impuestos.com.bo/impuesto-a-las-grandes-fortunas-ley-1357/ |
| IUE-BE non-resident WHT | effective **12.5%** of gross remitted (50% presumed profit x 25%) | https://impuestos.com.bo/iue-be-impuestos-sobre-las-utilidades-beneficiarios-del-exterior/ |

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown employment status | STOP -- do not compute without knowing employee vs self-employed/independent professional |
| Employee with no VAT-credit invoices | Apply RC-IVA 13% on (gross - 12.71% SS - 2 SMN), minus only the presumed credit (Bs 357.50/month for 2025) |
| Self-employed / independent professional | Treat under RC-IVA (13%, quarterly Form 610), NOT IUE -- independents moved out of IUE from 1 Jan 2023; also liable to IVA 13% and IT 3% on services billed |
| Unknown whether VAT invoices exist | Assume none -- compute full 13% net of presumed credit only |
| Unknown net wealth (IGF) | Assume NOT applicable (threshold Bs 30M) AND flag uncertain legal status for 2025/2026 |
| Payment to a non-resident | Apply IUE-BE 12.5% withholding unless a treaty rate is confirmed |
| Unknown social security band | Apply standard 12.71% employee total; flag Aporte Nacional Solidario only if gross > Bs 13,000 |
| Aguinaldo (Christmas bonus) | Exclude from RC-IVA taxable income |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

Minimum viable -- bank statement for the full tax year (or quarter) in CSV, PDF, or pasted text, PLUS confirmation of employment status (dependent employee vs self-employed / independent professional / direct contributor) and gross monthly income.

Recommended -- all purchase invoices (facturas) supporting the 13% VAT credit, social security contribution records (Gestora / Caja de Salud), prior-period RC-IVA filings (Form 610 / Form 110), and details of any non-resident payments.

Ideal -- complete income and expenditure records, NIT (tax ID) and its last digit (for the filing calendar), payroll register if an employer, and a statement of net wealth if IGF may apply.

Refusal if minimum is missing -- SOFT WARN. No bank statement at all = hard stop. Bank statement without facturas = proceed with reviewer warning: "This RC-IVA computation was produced from bank statement alone. Without valid facturas on Form 110 the full 13% liability stands (less only the presumed credit). The reviewer must verify VAT-credit invoices before reducing the liability."

### Refusal Catalogue

- **R-BO-1 -- Employment status unknown** — RC-IVA is computed differently for dependent employees (employer withholds monthly, no annual return) versus self-employed / independent professionals (quarterly Form 610). This skill cannot proceed without knowing the client's status. Please confirm.
- **R-BO-2 -- Corporate income tax (IUE) requested** — This skill covers personal income tax (RC-IVA) for individuals and independent professionals only. Corporate profits tax (IUE, 25%) for companies is a separate regime. Escalate to a Bolivian-licensed accountant.
- **R-BO-3 -- VAT (IVA) or transactions tax (IT) return requested** — This skill covers RC-IVA only. The 13% IVA and 3% IT on services are separate returns. Independent professionals owe all three -- flag for a Bolivian accountant to handle IVA and IT.
- **R-BO-4 -- IGF wealth tax with uncertain status** — The Impuesto a las Grandes Fortunas (Ley 1357) is reported to have been eliminated by the new government in late 2025, but no authoritative repeal instrument could be confirmed. Do not compute or advise on IGF. Escalate to a Bolivian-licensed accountant to confirm current law. [RESEARCH GAP]
- **R-BO-5 -- Mining / hydrocarbons / special regimes** — Sector-specific surtaxes (mining royalties, hydrocarbons, regimen agropecuario, regimen simplificado) are out of scope. Escalate to a Bolivian-licensed accountant.
- **R-BO-6 -- Tax arrears / SIN enforcement** — Client has outstanding RC-IVA arrears or is subject to SIN enforcement. Value-maintenance (UFV) updates, interest, and omission penalties (up to 100% of omitted tax) under Codigo Tributario Ley 2492 are severe. Do not advise. Escalate to a Bolivian-licensed accountant immediately.

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

How to read this table. Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. Descriptions are commonly in Spanish. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits / Abonos on Bank Statement)

**Income Patterns table**

| Pattern | RC-IVA Treatment | Notes |
| --- | --- | --- |
| HONORARIOS, FACTURA, PAGO SERVICIOS, CONSULTORIA | Bolivian-source income | Professional fees -- independent professional income (Form 610 base) |
| TRANSFERENCIA, ABONO, DEPOSITO + client name | Bolivian-source income | Business income -- match to facturas issued |
| SUELDO, SALARIO, HABER, PLANILLA, REMUNERACION | Employment income | Employer withholds RC-IVA -- NOT self-employed base |
| AGUINALDO, DOBLE AGUINALDO | EXCLUDE from RC-IVA | Christmas bonus -- statutorily excluded from RC-IVA income |
| ALQUILER COBRADO, RENTA INMUEBLE | Bolivian-source income (capital) | Rental income -- RC-IVA applies to capital income too |
| INTERESES GANADOS, RENDIMIENTO | Bolivian-source income (capital) | Interest income -- Bolivian-source only |
| DIVIDENDOS, REPARTO UTILIDADES (from BO company) | EXCLUDE | Dividends from Bolivian companies to residents are NOT subject to RC-IVA |
| DEVOLUCION IMPUESTOS, REINTEGRO SIN, RE-IVA | EXCLUDE | Tax refund / RE-IVA refund -- not income |
| BONO GOBIERNO, SUBSIDIO | Check nature | Capital grants EXCLUDE; revenue subsidies may be income -- flag |
| STRIPE PAYOUT, PAYPAL, WISE, MERCADO PAGO | Bolivian-source income if BO services | Platform payout -- match to underlying facturas; confirm source |

### 3.2 Statutory Deductions (Debits) -- Reduce RC-IVA Base / Liability

**Statutory Deductions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| GESTORA, APORTE AFP, JUBILACION, PENSIONES | Deduct from gross before RC-IVA base | Part of the 12.71% employee social security |
| CAJA DE SALUD, SEGURO SALUD | Employer cost (10%) | NOT an employee deduction from RC-IVA base |
| RIESGO COMUN, COMISION GESTORA, APORTE SOLIDARIO | Deduct from gross before RC-IVA base | Components of the 12.71% employee total |
| FACTURA COMPRA, NOTA FISCAL (with NIT) | 13% VAT credit -> Form 110 | Offsets RC-IVA liability; 13% of invoice value is the credit |

### 3.3 Expense Patterns (Debits / Cargos) -- Business Costs for Independent Professionals

For independent professionals, RC-IVA is charged on income; business costs are NOT a direct RC-IVA deduction the way they are in an income-tax-on-profit system. The principal offset is the 13% VAT credit from facturas (Form 110). Treat the patterns below as VAT-credit-bearing purchases, not profit deductions.

**Expense Patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| ALQUILER OFICINA, RENTA LOCAL | Office rent | Factura -> 13% VAT credit (Form 110) | Must have valid nota fiscal |
| SERVICIOS PROFESIONALES, CONTADOR, ABOGADO | Professional services | Factura -> 13% VAT credit | Business-related only |
| UTILES, PAPELERIA, LIBRERIA | Office supplies | Factura -> 13% VAT credit |  |
| PUBLICIDAD, GOOGLE ADS, META ADS, MARKETING | Marketing | Factura -> 13% VAT credit | Foreign invoices may not bear Bolivian VAT -- no credit |
| SOFTWARE, SUSCRIPCION, LICENCIA | Software | Factura -> 13% VAT credit if Bolivian nota fiscal | Foreign SaaS -- usually no Bolivian VAT credit |

### 3.4 Utilities (Debits)

**Utilities table**

| Pattern | Category | Notes |
| --- | --- | --- |
| ELECTRICIDAD, LUZ, CRE, ELECTROPAZ, ENDE | Electricity | Factura -> 13% VAT credit if business use; apportion if home |
| AGUA, SAGUAPAC, EPSAS | Water | Factura -> 13% VAT credit if business use |
| ENTEL, TIGO, VIVA, INTERNET | Telecoms | Business-use portion; default 0% if mixed |

### 3.5 NOT Deductible / No Credit

**Not Deductible table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| MULTA, SANCION, INFRACCION | NOT deductible / no credit | Fines and penalties |
| GASTO PERSONAL, SUPERMERCADO, HIPERMAXI, FIDALGA | Personal -- no business credit | Private living costs (unless RE-IVA refund applies for low earners) |
| PAGO IMPUESTOS, SIN, RC-IVA, IVA, IT | EXCLUDE | Tax payments are not expenses |
| RETIRO, CAJERO, ATM (personal) | EXCLUDE | Drawings / cash withdrawal |

### 3.6 Exclusions (Neither Income nor Expense)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERENCIA PROPIA, CUENTA PROPIA, ENTRE CUENTAS | EXCLUDE | Own-account transfer |
| PRESTAMO, CREDITO, AMORTIZACION CAPITAL | EXCLUDE | Loan principal movement |
| PAGO BENEFICIARIO EXTERIOR, REMESA EXTERIOR | IUE-BE withholding (12.5%) | Payment to non-resident -- withholding obligation (Form 530) |
| AGUINALDO | EXCLUDE from RC-IVA | Statutorily excluded |

### 3.7 Bolivian Banks -- Statement Format Reference

**Bolivian Banks table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Banco Nacional de Bolivia (BNB) | TRANSFERENCIA, ABONO, CARGO, COMISION | PDF/CSV; date format DD/MM/YYYY |
| Banco Mercantil Santa Cruz (BMSC) | DEPOSITO, DEBITO, PAGO | PDF; counterparty in glosa field |
| Banco Union | TRANSFERENCIA, ABONO, CARGO | State bank; PDF common |
| Banco BISA | TRANSFERENCIA, PAGO QR, COMISION | CSV available |
| Banco de Credito (BCP) | ABONO, CARGO, COMISION | PDF/CSV |

## Section 4 -- Worked Examples

All examples use the 2025 figures: SMN = Bs 2,750; non-taxable minimum 2 SMN = Bs 5,500/month; presumed credit Bs 357.50/month; employee social security 12.71%. RC-IVA flat rate 13%.

### Example 1 -- Employee, mid income, NO facturas

Input line:
`30/04/2025 ; BNB ; PLANILLA SUELDO ABRIL ; EMPRESA XYZ SRL ; +12,000.00 ; Bs`

Reasoning:
Gross monthly Bs 12,000. Deduct employee social security 12.71% = Bs 1,525.20. Net = Bs 10,474.80. Deduct non-taxable minimum 2 SMN = Bs 5,500. RC-IVA base = Bs 4,974.80. Gross 13% liability = Bs 646.72. Offset by presumed credit Bs 357.50 (no facturas presented). RC-IVA payable = Bs 289.22. (Source: rigobertoparedes.com/en/bolivia-2025-salary-increase.)

Classification: RC-IVA withheld by employer = Bs 289.22. Net pay = 12,000 - 1,525.20 - 289.22 = Bs 10,185.58. No annual return required from employee.

### Example 2 -- Employee, same income, WITH facturas on Form 110

Input line:
`Same Bs 12,000 salary, plus Bs 3,000 of valid facturas presented on Form 110`

Reasoning:
Liability before credits = Bs 646.72 (as Example 1). Presumed credit Bs 357.50 + invoice credit (13% x 3,000 = Bs 390.00) = total credit Bs 747.50. Credit exceeds the Bs 646.72 liability, so RC-IVA payable = Bs 0. Excess credit (Bs 100.78) carries forward to future periods; it is NOT refunded in cash. (Source: SIN, siatinfo.impuestos.gob.bo/.../rc-iva.)

Classification: RC-IVA withheld = Bs 0. Surplus credit Bs 100.78 carried forward.

### Example 3 -- Employee below the bite threshold

Input line:
`30/04/2025 ; BMSC ; SUELDO ; +6,000.00 ; Bs`

Reasoning:
Gross Bs 6,000. Less 12.71% SS = Bs 762.60. Net = Bs 5,237.40. Less 2 SMN (Bs 5,500) = negative (Bs -262.60). RC-IVA base is nil. No RC-IVA due. This is consistent with the practical bite at approx Bs 9,451 gross. (Source: rigobertoparedes.com/en/bolivia-2025-salary-increase.)

Classification: RC-IVA = Bs 0.

### Example 4 -- Independent professional, quarterly Form 610

Input line:
`Quarter Q2 2025 (Apr-Jun): total honorarios billed Bs 60,000; no facturas presented`

Reasoning:
Direct contributors deduct 2 SMN per month over the quarter = 2 x 2,750 x 3 = Bs 16,500. RC-IVA base = 60,000 - 16,500 = Bs 43,500. Gross 13% = Bs 5,655.00. Presumed credit = 13% of 1 SMN x 3 months = 357.50 x 3 = Bs 1,072.50. RC-IVA payable before facturas = Bs 4,582.50, due on Form 610 by 20 July 2025. (Source: SIN Form 610, siatinfo.impuestos.gob.bo.) Note: the independent professional ALSO owes IVA 13% and IT 3% on the services billed -- out of scope here, flag for the IVA/IT skill. (Source: Ferrere, ferrere.com.)

Classification: Form 610 RC-IVA payable = Bs 4,582.50 (before any factura credits).

[RESEARCH GAP -- reviewer to confirm.] The exact statutory deduction allowed to direct contributors (whether 2 SMN per month, a single 2 SMN, or another figure) for the Form 610 base should be confirmed against the DS 21531 reglamento and current SIN guidance. The figure used here mirrors the employee monthly mechanism.

### Example 5 -- Payment to a non-resident (IUE-BE)

Input line:
`15/05/2025 ; BCP ; REMESA EXTERIOR ; CONSULTOR USA ; -10,000.00 ; Bs`

Reasoning:
Payment to a non-domiciled beneficiary for services. IUE-BE under Ley 843 art. 51 presumes 50% net taxable profit, taxed at 25% = effective 12.5% of the gross remitted. 10,000 x 12.5% = Bs 1,250 withholding, declared on Form 530 in the month following remittance (per NIT calendar). (Source: impuestos.com.bo/iue-be.)

Classification: IUE-BE withholding = Bs 1,250.00 (Form 530). Confirm whether a tax treaty reduces this.

### Example 6 -- Aguinaldo (excluded)

Input line:
`20/12/2025 ; BNB ; AGUINALDO NAVIDAD ; +12,000.00 ; Bs`

Reasoning:
The Christmas bonus (aguinaldo) is mandatory (one month's salary) and is statutorily excluded from RC-IVA taxable income. (Source: PwC, income-determination.)

Classification: EXCLUDE from RC-IVA. No 13% applies.

### Example 7 -- Dividend from a Bolivian company (excluded)

Input line:
`28/03/2025 ; BISA ; DIVIDENDOS SA BOLIVIANA ; +20,000.00 ; Bs`

Reasoning:
Dividends paid by a Bolivian company to a resident individual are NOT subject to RC-IVA. (Source: PwC, income-determination.)

Classification: EXCLUDE from RC-IVA.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 RC-IVA Is a Flat 13%

- **RC-IVA flat 13% rule** — RC-IVA is a flat 13% on Bolivian-source income from labour and capital. There are no progressive brackets.  _(Ley 843, Titulo II, arts. 19-36; PwC, taxes-on-personal-income)_

### 5.2 Territorial Taxation

- **Territorial taxation rule** — Individuals are taxed only on Bolivian-source income, regardless of residency or citizenship. Foreign-source income is not subject to RC-IVA.  _(PwC, taxes-on-personal-income)_

### 5.3 Employee RC-IVA Mechanism

- **Monthly computation steps** — 1. Start with gross monthly remuneration (excluding aguinaldo). 2. Deduct employee social security contributions (standard 12.71%). 3. Deduct the non-taxable minimum: 2 SMN = Bs 5,500/month (2025). 4. Apply 13% to the resulting base. 5. Offset against (a) the presumed VAT credit Bs 357.50/month (13% of 1 SMN, 2025) and (b) 13% of valid facturas presented on Form 110. 6. Any residual is RC-IVA withheld by the employer. Excess credit carries forward; it is not refunded.  _(rigobertoparedes.com/en/bolivia-2025-salary-increase; SIN RC-IVA page)_
- **No annual return for employees** — Employees do NOT file an annual RC-IVA return. The employer (withholding agent) files a monthly consolidated return; the employee only interacts via Form 110 (invoice detail) given to the employer.  _(PwC, tax-administration)_

### 5.4 The 2025 Change (DS 5383)

- **Presumed credit cut 2025** — The presumed VAT credit was cut from 13% of 2 SMN (Bs 715) to 13% of 1 SMN (Bs 357.50/month), raising effective RC-IVA for employees who do not submit facturas; the practical withholding now bites at approx Bs 9,451/month gross.  _(rigobertoparedes.com/en/bolivia-2025-salary-increase)_

### 5.5 Independent Professionals -> RC-IVA (not IUE)

- **Independent professionals moved to RC-IVA** — Independent professionals were moved from IUE (25%) to RC-IVA (13%). They file RC-IVA quarterly on Form 610 and also pay IVA 13% and IT 3% on services.  _(Ferrere, ferrere.com; Ley 1448 (2021) + DS 4850, effective 1 Jan 2023)_

### 5.6 Self-Employed / Direct Contributor Filing

- **Quarterly filing deadlines** — Direct contributors (contribuyentes directos) file RC-IVA quarterly on Form 610 within 20 days after quarter-end: Q1 by 20 Apr, Q2 by 20 Jul, Q3 by 20 Oct, Q4 by 20 Jan. Form 110 (factura detail) is attached to claim the 13% credit.  _(SIN Form 610, siatinfo.impuestos.gob.bo)_

### 5.7 Social Security Contributions (2025)

**Standard employee contribution table**  _(planifica.com.bo)_

| Component | Rate | Source |
| --- | --- | --- |
| Cuenta individual de vejez (pension) | 10% | planifica.com.bo |
| Prima por Riesgo Comun | 1.71% | rigobertoparedes.com/es |
| Comision Gestora Publica | 0.5% | rigobertoparedes.com/es |
| Aporte Solidario del Asegurado | 0.5% | planifica.com.bo |
| **Total employee (standard)** | **12.71%** | planifica.com.bo |

Arithmetic check: 10 + 1.71 + 0.5 + 0.5 = 12.71%. ✓

**Aporte Nacional Solidario table**  _(rigobertoparedes.com/es)_

| Income band (Bs) | Additional rate on the excess in band | Source |
| --- | --- | --- |
| portion above 13,000 | +1% | rigobertoparedes.com/es |
| portion above 25,000 | +5% | rigobertoparedes.com/es |
| portion above 35,000 | +10% | rigobertoparedes.com/es |

- **Solidarity bands applied to excess** — These are applied to the excess in each band, in addition to the 12.71%.  _(rigobertoparedes.com/es; brackets per Ley 065)_

[RESEARCH GAP -- reviewer to confirm.] Ley 1582 (2024) revised the solidarity-fund parameters; one source cites an effective recalculated burden of ~1.15% / 5.74% / 11.48%. The precise current statutory percentages should be confirmed against the consolidated Ley 065 text. A pension-contribution salary ceiling (commonly cited as 60 SMN) could not be confirmed from an authoritative source -- confirm whether a ceiling applies.

**Employer social security table**  _(planifica.com.bo)_

| Component | Rate | Source |
| --- | --- | --- |
| Caja de Salud (health insurance) | 10% | planifica.com.bo |
| Riesgo Profesional | 1.71% | planifica.com.bo |
| Pro-Vivienda (housing fund) | 2% | planifica.com.bo |
| Aporte Patronal Solidario | 3% (raised to 3.5% under Ley 1582 per some sources) | economiayfinanzas.gob.bo |
| **Total employer (at 3%)** | **16.71%** | planifica.com.bo |
| **Total employer (at 3.5%)** | **17.21%** | economiayfinanzas.gob.bo |

Arithmetic check: 10 + 1.71 + 2 + 3 = 16.71%; with 3.5% solidarity = 17.21%. ✓

[RESEARCH GAP -- reviewer to confirm.] The Aporte Patronal Solidario rate (3% vs 3.5% under Ley 1582; mining employer solidarity 2% vs 2.3%) should be confirmed against the consolidated statute.

### 5.8 Minimum Wage and Salary Increase (2025)

- **Minimum wage 2025** — National minimum wage (SMN) for 2025 = Bs 2,750/month, +10% over 2024's Bs 2,500, retroactive to 1 Jan 2025 (art. 7). General private-sector salary increase up to 5% on the basico.  _(DS 5383 (1 May 2025); lexivox.org/norms/BO-DS-N5383)_

### 5.9 Capital Gains and Dividends

- **Capital gains and dividends treatment** — Capital gains are not subject to a separate capital gains tax for individuals. Dividends paid by Bolivian companies to resident individuals are NOT subject to RC-IVA.  _(PwC, income-determination)_

### 5.10 Non-Resident Withholding (IUE-BE)

- **IUE-BE effective rate** — 12.5% of the gross remitted (50% presumed net profit x 25%), declared on Form 530 in the month following the remittance per the NIT calendar  _(Ley 843, art. 51; impuestos.com.bo/iue-be)_

### 5.11 Non-Resident Employees of Foreign Employers

- **Non-resident employee filing obligation** — Non-resident employees with foreign employers must declare and pay RC-IVA monthly or on departure from Bolivia, whichever is first.  _(PwC, taxes-on-personal-income)_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 IGF Wealth Tax Applicability and Status

- **IGF applicability and status** — Threshold: net wealth over Bs 30,000,000 at 31 Dec; 1.4% / 1.9% / 2.4% bands; reaches residents' worldwide assets and non-residents' Bolivian assets. Status uncertain -- reportedly eliminated by the Paz government in late 2025 (El Pais, 25 Nov 2025), but no authoritative repeal instrument confirmed. Conservative default: do NOT compute. Flag for reviewer to confirm both applicability (net wealth > Bs 30M) and current legal status. [RESEARCH GAP]  _(impuestos.com.bo/igf; Ley 1357)_

### 6.2 Source of Income (Bolivian vs Foreign)

- **Source of income determination** — RC-IVA reaches only Bolivian-source income. Platform payouts (Stripe, PayPal, Wise) and cross-border fees require a source determination. Conservative default: treat ambiguous income as Bolivian-source until reviewer confirms; flag foreign-source items for exclusion.

### 6.3 Factura Validity for VAT Credit

- **Factura validity requirements** — The 13% VAT credit requires a valid nota fiscal (factura) with the correct NIT, date within the period, and a business purpose. Foreign invoices generally bear no Bolivian VAT and yield no credit. Conservative default: exclude any invoice lacking a valid Bolivian nota fiscal. Flag for reviewer.

### 6.4 Mixed-Use Utilities (Home Office)

- **Mixed-use utilities apportionment** — Electricity, water, telecoms used partly for business: only the business-use portion bears a credit. Conservative default: 0% until reviewer confirms apportionment basis.

### 6.5 Aporte Nacional Solidario Bands

- **Solidario bands default** — For gross above Bs 13,000, the progressive solidarity contributions apply. Conservative default: apply only standard 12.71% unless gross clearly exceeds Bs 13,000; flag the solidarity computation for reviewer given the [RESEARCH GAP] on current rates.

### 6.6 Treaty Relief on IUE-BE

- **Treaty relief default** — A tax treaty may reduce the 12.5% non-resident withholding. Conservative default: apply 12.5%; flag for reviewer to check treaty eligibility.

### 6.7 RE-IVA Refund Eligibility (Low Earners)

- **RE-IVA refund eligibility** — Individuals earning up to Bs 9,000/month may claim a 5%-of-invoices refund under Ley 1355. Conservative default: flag eligibility for reviewer; do not auto-claim.  _(PwC, significant-developments)_

## Section 7 -- Excel Working Paper Template

BOLIVIA RC-IVA -- WORKING PAPER
Tax Year: 2025   (SMN = Bs 2,750; 2 SMN = Bs 5,500; presumed credit = Bs 357.50)
Client: ___________________________
Status: Employee / Independent professional / Direct contributor
NIT: ___________   NIT last digit (filing calendar): ____

A. EMPLOYEE MONTHLY RC-IVA (repeat per month)
  A1. Gross remuneration (excl. aguinaldo)        ___________
  A2. Less employee social security (12.71%)      ___________
  A3. Net after SS (A1 - A2)                       ___________
  A4. Less non-taxable minimum (2 SMN = 5,500)    ___________
  A5. RC-IVA base (A3 - A4, floor at 0)            ___________
  A6. Gross 13% liability (A5 x 13%)               ___________
  A7. Less presumed credit (357.50)                ___________
  A8. Less 13% of facturas (Form 110)              ___________
  A9. RC-IVA withheld (A6 - A7 - A8, floor 0)      ___________
  A10. Credit carried forward (if negative A9)     ___________

B. INDEPENDENT / DIRECT CONTRIBUTOR QUARTERLY (Form 610)
  B1. Total honorarios billed (quarter)            ___________
  B2. Less 2 SMN x 3 months (16,500)  [GAP]        ___________
  B3. RC-IVA base (B1 - B2)                         ___________
  B4. Gross 13% liability (B3 x 13%)               ___________
  B5. Less presumed credit (357.50 x 3 = 1,072.50) ___________
  B6. Less 13% of facturas (Form 110)              ___________
  B7. RC-IVA payable on Form 610 (B4-B5-B6, floor 0)__________

C. NON-RESIDENT PAYMENTS (Form 530)
  C1. Gross remitted to non-resident               ___________
  C2. IUE-BE withholding (12.5%)                   ___________

D. IGF WEALTH TAX -- DO NOT COMPUTE unless > Bs 30M AND status confirmed [GAP]
  D1. Net wealth at 31 Dec                          ___________
  D2. IGF (1.4% / 1.9% / 2.4%)  [REVIEWER ONLY]    ___________

REVIEWER FLAGS:
  [ ] Employment status confirmed?
  [ ] Facturas (Form 110) validity checked?
  [ ] Aguinaldo excluded from base?
  [ ] Source of income (Bolivian vs foreign) confirmed?
  [ ] Aporte Nacional Solidario rates confirmed? [GAP]
  [ ] Form 610 direct-contributor deduction confirmed? [GAP]
  [ ] IGF status confirmed (Ley 1357 repeal)? [GAP]
  [ ] IUE-BE treaty relief checked?
  [ ] IVA 13% and IT 3% handled separately (independents)?

## Section 8 -- Bank Statement Reading Guide

### Bolivian Bank Statement Formats

**Bank statement formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Banco Nacional de Bolivia (BNB) | PDF, CSV | Fecha, Glosa/Descripcion, Debito, Credito, Saldo | Glosa contains counterparty + reference |
| Banco Mercantil Santa Cruz (BMSC) | PDF | Fecha, Concepto, Cargo, Abono, Saldo | Shorter descriptions |
| Banco Union | PDF | Fecha, Detalle, Debito, Credito | State bank |
| Banco BISA | PDF, CSV | Fecha, Glosa, Monto, Saldo | QR payments common |
| Banco de Credito (BCP) | PDF, CSV | Fecha, Descripcion, Cargo, Abono |  |

### Key Bolivian Banking / Tax Terms

**Key terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| ABONO / DEPOSITO | Credit / deposit | Potential income |
| CARGO / DEBITO | Debit | Expense -- check counterparty |
| TRANSFERENCIA | Transfer | Check direction and own-account |
| GLOSA / CONCEPTO | Description / memo | Counterparty detail |
| HONORARIOS | Professional fees | RC-IVA income (independents) |
| SUELDO / HABER / PLANILLA | Salary / payroll | Employment -- employer withholds |
| AGUINALDO | Christmas bonus | EXCLUDE from RC-IVA |
| FACTURA / NOTA FISCAL | Tax invoice | 13% VAT credit (Form 110) |
| NIT | Tax ID number | Needed for filing calendar |
| GESTORA / AFP | Pension fund | Social security deduction |
| CAJA DE SALUD | Health insurance fund | Employer cost (10%) |
| RETENCION | Withholding | RC-IVA / IUE-BE withheld |
| REMESA / BENEFICIARIO EXTERIOR | Remittance abroad / non-resident | IUE-BE 12.5% (Form 530) |
| COMISION | Commission / bank charge | Bank charge |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDIENTE -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

ONBOARDING QUESTIONS -- BOLIVIA RC-IVA
1. Status: dependent employee, independent professional, or direct contributor?
2. If employee: gross monthly salary, and does the employer withhold RC-IVA?
3. Do you present facturas (notas fiscales) on Form 110 to offset RC-IVA? Roughly how much per month?
4. Do you have your NIT and know its last digit (for the filing calendar)?
5. Any income from rent, interest, or Bolivian-source capital?
6. Any payments to non-residents (consultants, suppliers abroad)?
7. Is any of your income foreign-source (paid for services performed outside Bolivia)?
8. Is your gross monthly income above Bs 13,000 (for the solidarity contribution)?
9. Net wealth above Bs 30,000,000? (IGF -- status uncertain, reviewer to confirm)
10. Do you also need IVA (13%) and IT (3%) returns handled (independents)?

## Section 10 -- Reference Material

### Key Legislation References

**Legislation references table**

| Topic | Reference |
| --- | --- |
| RC-IVA (personal income tax) | Ley 843, Titulo II, arts. 19-36; reglamento DS 21531 |
| Independent professionals -> RC-IVA | Ley 1448 (2021) + DS 4850 (from 1 Jan 2023) |
| Social security / pensions | Ley 065 de Pensiones (2010), modified by Ley 1582 (2024) |
| Minimum wage 2025 | DS 5383 (1 May 2025), art. 7 |
| Non-resident withholding (IUE-BE) | Ley 843, art. 51 |
| Wealth tax (IGF) | Ley 1357 (2020) -- status uncertain [GAP] |
| Penalties | Codigo Tributario, Ley 2492 |

### Forms

**Forms table**

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Formulario 610 (RC-IVA Contribuyentes Directos) | Quarterly RC-IVA for self-employed / independent professionals / rental & investment income | Within 20 days after quarter-end: 20 Apr / 20 Jul / 20 Oct / 20 Jan | siatinfo.impuestos.gob.bo (610) |
| Formulario 110 | Detail of purchase facturas supporting the 13% VAT credit; attached to Form 610 (direct) or given to employer (dependents) | With the corresponding RC-IVA period | siatinfo.impuestos.gob.bo (rc-iva) |
| Formulario 608 / consolidado RC-IVA (Agentes de Retencion) | Monthly consolidated RC-IVA filed by employers (withholding agents) | Monthly, per NIT last-digit calendar | PwC, tax-administration |
| Formulario 530 (IUE-BE) | Withholding on payments/remittances to non-domiciled beneficiaries | Per NIT last-digit monthly calendar of the month following remittance | siatinfo.impuestos.gob.bo (530) |

[RESEARCH GAP -- reviewer to confirm.] The monthly employer RC-IVA consolidated return form number (cited as ~608/consolidado) should be confirmed against the current SIAT form catalog.

### Penalties

**Penalties table**

| Type | Detail | Source |
| --- | --- | --- |
| Late RC-IVA payment | Tax updated for inflation (mantenimiento de valor / UFV), plus interest and a penalty surcharge (multa por incumplimiento) per Codigo Tributario Ley 2492; omission penalty generally 100% of the omitted tax | siatinfo.impuestos.gob.bo (rc-iva) |

Penalty figures are general (Codigo Tributario Ley 2492) and not RC-IVA-specific. [RESEARCH GAP -- reviewer to confirm specific RC-IVA penalty schedule.]

### Primary Sources

**Primary Sources table**

| Title | URL | Publisher |
| --- | --- | --- |
| Bolivia - Individual - Taxes on personal income | https://taxsummaries.pwc.com/bolivia/individual/taxes-on-personal-income | PwC Worldwide Tax Summaries (reviewed 26 Mar 2026) |
| Bolivia - Individual - Deductions | https://taxsummaries.pwc.com/bolivia/individual/deductions | PwC |
| Bolivia - Individual - Tax administration | https://taxsummaries.pwc.com/bolivia/individual/tax-administration | PwC |
| Bolivia - Individual - Income determination | https://taxsummaries.pwc.com/bolivia/individual/income-determination | PwC |
| Bolivia - Individual - Significant developments (wealth tax, RE-IVA) | https://taxsummaries.pwc.com/bolivia/individual/significant-developments | PwC |
| RC-IVA -- SIAT (official tax authority) | https://siatinfo.impuestos.gob.bo/index.php/impuesto-asunto/rc-iva | Servicio de Impuestos Nacionales (SIN) |
| 610 - RC-IVA - Contribuyente Directo | https://siatinfo.impuestos.gob.bo/index.php/declaraciones-juradas-en-formato-electronico/regimen-complementario-al-iva/610-regimen-complementario-del-iva-contribuyente-directo | SIN |
| Decreto Supremo N 5383 (1 May 2025) | https://www.lexivox.org/norms/BO-DS-N5383.html | Gaceta Oficial / LexiVox |
| Bolivia 2025 salary increase: impact on RC-IVA | https://www.rigobertoparedes.com/en/bolivia-2025-salary-increase/ | Rigoberto Paredes & Asociados |
| Aportes a la Gestora y Caja de Salud | https://www.planifica.com.bo/aportes-afp-caja-salud-bolivia-guia-empleado-empleador/ | Planifica Consultores |
| Aportes e impuestos al trabajador en Bolivia | https://www.rigobertoparedes.com/es/aportes-e-impuestos-al-trabajador-en-bolivia/ | Rigoberto Paredes & Asociados |
| Profesionales independientes incluidos en RC-IVA (Ley 1448 / DS 4850) | https://www.ferrere.com/es/novedades/profesionales-independientes-son-incluidos-en-el-regimen-rc-iva/ | Ferrere Abogados |
| IUE-BE -- Beneficiarios del exterior | https://impuestos.com.bo/iue-be-impuestos-sobre-las-utilidades-beneficiarios-del-exterior/ | Impuestos de Bolivia |
| Impuesto a las Grandes Fortunas (Ley 1357) | https://impuestos.com.bo/impuesto-a-las-grandes-fortunas-ley-1357/ | Impuestos de Bolivia |
| Que es el IGF y quien lo paga(ba) -- IGF elimination | https://elpais.bo/nacional/20251125_que-es-el-impuesto-a-las-grandes-fortunas-y-quien-lo-paga-ba.html | El Pais (Bolivia) |
| Ley 1582 incrementa limites solidarios | https://www.economiayfinanzas.gob.bo/node/11448 | Ministerio de Economia y Finanzas Publicas (MEFP) |

### Test Suite

Test 1 -- Employee, mid income, no facturas.
Input: gross Bs 12,000/month, 12.71% SS, no facturas.
Expected: SS = Bs 1,525.20; net = Bs 10,474.80; less 2 SMN (5,500) = base Bs 4,974.80; 13% = Bs 646.72; less presumed credit Bs 357.50; RC-IVA = Bs 289.22; net pay = Bs 10,185.58.

Test 2 -- Employee with facturas.
Input: same Bs 12,000 plus Bs 3,000 facturas on Form 110.
Expected: liability Bs 646.72; credit = 357.50 + (13% x 3,000 = 390.00) = Bs 747.50; RC-IVA = Bs 0; carry-forward credit Bs 100.78 (not refunded).

Test 3 -- Employee below bite threshold.
Input: gross Bs 6,000.
Expected: SS Bs 762.60; net Bs 5,237.40; less 2 SMN (5,500) = negative; base nil; RC-IVA = Bs 0.

Test 4 -- Independent professional quarterly.
Input: Q2 honorarios Bs 60,000, no facturas.
Expected: less 2 SMN x 3 (16,500) = base Bs 43,500; 13% = Bs 5,655.00; less presumed credit 357.50 x 3 = Bs 1,072.50; Form 610 payable = Bs 4,582.50 by 20 Jul 2025. (Form 610 direct-contributor deduction flagged [GAP].)

Test 5 -- Non-resident payment (IUE-BE).
Input: Bs 10,000 remitted to a non-resident consultant.
Expected: IUE-BE = 12.5% x 10,000 = Bs 1,250.00 (Form 530).

Test 6 -- Aguinaldo excluded.
Input: aguinaldo Bs 12,000 received.
Expected: EXCLUDE from RC-IVA. Bs 0 tax.

Test 7 -- IGF (high net wealth, status caveat).
Input: net wealth Bs 45,000,000 at 31 Dec.
Expected (IF Ley 1357 still in force -- [GAP]): band 30-40M (Bs 10M x 1.4% = Bs 140,000) + band 40-45M (Bs 5M x 1.9% = Bs 95,000) = Bs 235,000. Do NOT file until repeal status confirmed.

Test 8 -- Dividend from Bolivian company.
Input: Bs 20,000 dividend from a Bolivian SA.
Expected: NOT subject to RC-IVA. Bs 0 tax.

## PROHIBITIONS

- NEVER apply RC-IVA without confirming employment status (employee vs independent/direct contributor)
- NEVER treat independent professionals under IUE (25%) -- they are under RC-IVA (13%) from 1 Jan 2023
- NEVER compute IGF wealth tax without confirming both net wealth > Bs 30M AND that Ley 1357 is still in force [GAP]
- NEVER include aguinaldo in the RC-IVA base
- NEVER treat dividends from Bolivian companies to residents as RC-IVA income
- NEVER tax foreign-source income under RC-IVA -- Bolivia is territorial
- NEVER reduce RC-IVA below zero into a cash refund -- excess factura credit carries forward
- NEVER use the old presumed credit of Bs 715 for 2025 -- it was cut to Bs 357.50 by DS 5383
- NEVER omit the IUE-BE 12.5% withholding on payments to non-residents
- NEVER present tax calculations as definitive -- always label as estimated and pending professional review
- NEVER rely on a [RESEARCH GAP] figure for filing without a Bolivian-licensed accountant's confirmation

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
