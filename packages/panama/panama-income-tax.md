---
name: panama-income-tax
description: Use this skill whenever asked about Panama personal income tax (ISR — Impuesto sobre la Renta) for individuals, self-employed persons, or payroll. Trigger on phrases like "how much income tax do I pay in Panama", "Panama ISR", "declaración jurada de rentas", "income tax return Panama", "allowable deductions Panama", "CSS contributions", "Caja de Seguro Social", "seguro educativo", "territorial taxation", "Panama-source income", "self-employed CSS Law 462", "décimo tercer mes", "estimated tax instalments", "DGI filing", "non-resident withholding Panama", or any question about filing or computing personal income tax or social security for an individual or self-employed client in Panama. Also trigger when classifying a Panamanian bank statement, computing CSS/educational-insurance payroll deductions, or advising on the 15 March filing deadline. This skill covers the progressive ISR brackets, personal deductions, CSS + educational insurance under Law 462 of 2025, filing deadlines, estimated tax, penalties, minimum wage, and the territorial source rule. ALWAYS read this skill before touching any Panama income tax work.
version: 0.1
jurisdiction: PA
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Panama Personal Income Tax (ISR) — Self-Employed & Payroll

## Section 1 — Quick Reference

**Section 1 Quick Reference table**  _(PwC, taxes-on-personal-income; PwC, tax-administration)_

| Field | Value |
| --- | --- |
| Country | Panama (Republic of Panama / República de Panamá) |
| Tax | Personal income tax — ISR (Impuesto sobre la Renta), natural persons |
| Currency | USD (the Balboa B/. is pegged 1:1 and circulates as coin; USD notes are legal tender) |
| Tax year | Calendar year (1 January – 31 December) |
| Tax basis | **Territorial** — only Panamanian-source income is taxed, for residents and non-residents alike (PwC, taxes-on-personal-income) |
| Tax authority | Dirección General de Ingresos (DGI), under the Ministerio de Economía y Finanzas (MEF) |
| Social security | Caja de Seguro Social (CSS) |
| Filing portal | e-Tax 2.0 (DGI online portal) (PwC, tax-administration) |
| Filing deadline (individuals) | **15 March** of the following year; one-month extension available on request (PwC, tax-administration) |
| Estimated tax instalments | 30 June, 30 September, 31 December (PwC, tax-administration) |
| Local/municipal income tax | None (PwC, taxes-on-personal-income) |
| Alternate minimum tax for individuals | None (PwC, taxes-on-personal-income) |
| Validated by | Pending — requires sign-off by a Panamanian licensed accountant (CPA) |
| Validation date | Pending |
| Skill version | 0.1 |

### Income Tax Rate Brackets (tax year 2025)

**Income Tax Rate Brackets (tax year 2025)**  _(PwC, taxes-on-personal-income — reviewed 18 Jan 2026)_

| Taxable Income (USD) | Tax on this band | Cumulative Tax at Top of Band |
| --- | --- | --- |
| 0 – 11,000 | 0% | USD 0 |
| 11,001 – 50,000 | 15% on excess over 11,000 | USD 5,850 |
| Over 50,000 | USD 5,850 fixed + 25% on excess over 50,000 | — |

- **Arithmetic check** — Top of the 15% band: (50,000 − 11,000) × 15% = 39,000 × 15% = USD 5,850. The "Over 50,000" row therefore carries a fixed base of USD 5,850 plus 25% on the excess.  _(PwC, taxes-on-personal-income)_
- **Territorial rule** — Citizens, residents, and non-residents are taxed only on Panama-source income. Non-residents' Panama-source income is generally subject to withholding by the payer.  _(PwC, taxes-on-personal-income)_

### Personal Deductions / Allowances (tax year 2025)

**Personal Deductions / Allowances table**  _(PwC, deductions)_

| Deduction | Cap | Source |
| --- | --- | --- |
| Personal exemption (married individual) | USD 800 | PwC, deductions |
| Per-dependent deduction (USD 250) | **[RESEARCH GAP — reviewer to confirm]** secondary sources cite "$800 basic + $250 per dependent" but PwC authoritative page does not confirm the $250 figure | Unconfirmed |
| Mortgage interest (primary home in Panama or home improvements) | up to USD 15,000/year | PwC, deductions |
| Retirement / pension fund contributions | up to USD 15,000 | PwC, deductions |
| Education expenses | up to USD 3,600 per student (since Jan 2019) | PwC, deductions |
| Medical expenses incurred in Panama | deductible, documented; no cap stated | PwC, deductions |
| Charitable donations (approved local educational/charitable institutions + non-profit dues) | max USD 50,000/year | PwC, deductions |
| Unreimbursed employment expenses (moving, travel, entertainment) | NOT deductible | PwC, deductions |

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Source of income unknown (Panama vs foreign) | STOP — territorial rule means foreign-source income is exempt; confirm source before including |
| Resident vs non-resident unknown | Treat as STOP — non-residents are subject to withholding, not self-assessment |
| Unknown marital status | Apply no personal exemption (the USD 800 exemption is married-only per PwC) |
| Unknown dependent count | 0 dependents (the $250/dependent figure is unconfirmed anyway) |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Deduction lacks documentation | Not deductible |
| Whether worker is employee or independent | STOP — determines CSS treatment (9.75% employee vs 9.36% IVM independent) |

## Section 2 — Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** — bank statement for the full tax year in CSV, PDF, or pasted text; confirmation of residency status (resident/non-resident); confirmation of whether income is Panama-source; and worker classification (employee vs self-employed/independent).

**Recommended** — all invoices/receipts (facturas) issued and received, CSS payment records, prior-year declaración jurada de rentas or DGI assessment, RUC (Registro Único de Contribuyente) number, marital status and dependent count.

**Ideal** — complete income and expenditure account, mortgage interest certificate, pension contribution certificates, education and medical receipts, estimated-tax instalment confirmations, employer payroll records (planilla).

**Refusal if minimum is missing — SOFT WARN.** No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This return was produced from bank statement alone. The reviewer must verify Panama-source classification and that all deductions claimed are supported by valid documentation."

### Refusal Catalogue

- **R-PA-1** — Source of income unclear. "Panama taxes on a strictly territorial basis. Income from foreign sources is not taxable. This skill cannot proceed until the Panama-source vs foreign-source split is confirmed for each income stream. Escalate to a licensed accountant if the source is genuinely ambiguous (e.g. services partly performed abroad)."
- **R-PA-2** — Non-resident self-assessment. "Non-residents' Panama-source income is generally taxed by withholding at the payer, not by self-assessed return. This skill covers resident individual returns. Escalate to a licensed accountant for non-resident withholding analysis."
- **R-PA-3** — Companies, partnerships, foundations. "This skill covers natural persons (individuals and self-employed) only. Corporations (sociedades anónimas), partnerships, and private-interest foundations file separate corporate returns. Escalate to a licensed accountant."
- **R-PA-4** — Capital gains / real-estate transfers. "Gains on disposal of real estate and securities are taxed under separate regimes (transfer tax / advance ISR on real estate). Out of scope. Escalate to a licensed accountant."
- **R-PA-5** — Arrears / enforcement. "Client has outstanding DGI arrears or risk of suspension of the Aviso de Operación. Penalties can be automatically generated from USD 500 upward [RESEARCH GAP — reviewer to confirm the DGI primary penalty schedule]. Do not advise. Escalate to a licensed accountant immediately."
- **R-PA-6** — Special regimes (SEM, City of Knowledge, Colón Free Zone, Panama-Pacífico). "These regimes have bespoke income tax and social-security treatment. Out of scope. Escalate to a licensed accountant."

## Section 3 — Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. Panamanian statements are usually in Spanish. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules. **Always confirm Panama-source before treating any credit as taxable income.**

### 3.1 Income Patterns (Credits / Créditos)

**Income Patterns table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| Client name + TRANSFERENCIA, DEPÓSITO, PAGO RECIBIDO, ABONO | Business income (Panama-source) | Confirm services performed in Panama |
| HONORARIOS, FACTURA, SERVICIOS PROFESIONALES, CONSULTORÍA | Business income | Professional fees — typical for self-employed |
| STRIPE PAYOUT, STRIPE TRANSFER | Business income | Platform payout — match to underlying facturas; confirm source |
| PAYPAL, WISE, REVOLUT PAYOUT | Business income | Verify against invoices; confirm Panama-source |
| UPWORK, FIVERR, TOPTAL | Business income | Freelance platform — net of platform commission; **likely foreign-source if client and work are abroad — confirm** |
| SALARIO, PLANILLA, SUELDO, EMPLEADOR [name] | Employment income | Subject to CSS + educational insurance + ISR withholding by employer |
| ALQUILER, RENTA RECIBIDA | Rental income | Panama-source if property in Panama |
| INTERESES (cuenta de ahorro / depósito a plazo panameño) | EXCLUDE | Interest on Panamanian bank savings and time deposits is exempt (PwC, taxes-on-personal-income) |
| INTERESES (valores del Estado / government securities) | EXCLUDE | Interest on Panamanian government securities is exempt (PwC, taxes-on-personal-income) |
| DEVOLUCIÓN DGI, REINTEGRO IMPUESTO | EXCLUDE | Tax refund from prior year |
| DÉCIMO TERCER MES, XIII MES | Special — see Section 6 | 13th-month bonus; CSS/ISR treatment flagged [RESEARCH GAP] |

### 3.2 Expense Patterns (Debits / Débitos) — Potentially Deductible

Note: Panama allows employment/business expenses only where wholly business-related and documented; unreimbursed employment expenses (moving, travel, entertainment) are not deductible (PwC, deductions). For self-employed, ordinary and necessary business expenses to produce Panama-source income are deductible.

**Potentially Deductible Expenses table**  _(PwC, deductions)_

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| ALQUILER OFICINA, RENTA LOCAL COMERCIAL | Office rent | Deductible (business) | Dedicated business premises |
| HONORARIOS CONTADOR, AUDITOR, CONTABILIDAD | Accountancy fees | Deductible (business) |  |
| ABOGADO, LEGAL, NOTARÍA (business) | Legal fees | Deductible (business) | Must be business-related |
| PUBLICIDAD, MARKETING, GOOGLE ADS, META ADS | Marketing/advertising | Deductible (business) |  |
| SUMINISTROS, PAPELERÍA, OFFICE SUPPLIES | Office supplies | Deductible (business) |  |
| GOOGLE WORKSPACE, MICROSOFT 365, ADOBE, CANVA, ZOOM | Software subscription | Deductible (business) | Recurring SaaS = operating expense |
| ANTHROPIC, OPENAI, GITHUB, AWS, HOSTING, DOMINIO | IT infrastructure | Deductible (business) |  |
| COMISIÓN BANCARIA, CARGO BANCO, MANTENIMIENTO CUENTA | Bank charges | Deductible (business) | Business account only |
| INTERÉS HIPOTECARIO, HIPOTECA (vivienda principal) | Mortgage interest | Personal deduction up to USD 15,000/yr (PwC, deductions) | Primary home in Panama or improvements |
| FONDO DE PENSIÓN, JUBILACIÓN, APORTE PENSIÓN | Pension contribution | Personal deduction up to USD 15,000 (PwC, deductions) |  |
| COLEGIO, UNIVERSIDAD, MATRÍCULA, EDUCACIÓN | Education | Personal deduction up to USD 3,600 per student (PwC, deductions) |  |
| CLÍNICA, HOSPITAL, FARMACIA, MÉDICO (en Panamá) | Medical | Personal deduction, documented, no cap stated (PwC, deductions) | Must be incurred in Panama |
| DONACIÓN (institución aprobada) | Charitable donation | Personal deduction max USD 50,000/yr (PwC, deductions) | Approved local institutions |

### 3.3 Expense Patterns (Debits) — NOT Deductible

**NOT Deductible Expenses table**  _(PwC, deductions)_

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANTE, ALMUERZO, CENA, ENTRETENIMIENTO | Entertainment | NOT deductible | Unreimbursed employment entertainment blocked (PwC, deductions) |
| SUPERMERCADO, RIBA SMITH, EL REY, SUPER 99, PERSONAL | Personal expenses | NOT deductible | Private living costs |
| MULTA, SANCIÓN, INFRACCIÓN | Fines/penalties | NOT deductible | Public policy |
| PAGO ISR, IMPUESTO SOBRE LA RENTA, DGI | Tax payment | NOT deductible | Income tax cannot reduce income |
| RETIRO, RETIRO PERSONAL, CAJERO (personal) | Drawings | NOT deductible | Not an expense |
| MUDANZA, VIAJE PERSONAL (employee, unreimbursed) | Moving/travel | NOT deductible | Blocked for employees (PwC, deductions) |

### 3.4 Social Security & Statutory (Debits)

**Social Security & Statutory table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| CSS, CAJA DE SEGURO SOCIAL, CUOTA OBRERO | CSS contribution | Statutory — see Section 5.5 | Employee 9.75%; independent 9.36% IVM |
| SEGURO EDUCATIVO | Educational insurance | Statutory — see Section 5.5 | Employee 1.25% / employer 1.50% |
| ESTIMADA, IMPUESTO ESTIMADO, CUOTA ESTIMADA | Estimated tax instalment | Credit against liability | 30 Jun / 30 Sep / 31 Dec instalments |

### 3.5 Exclusions (Neither Income nor Expense)

**Exclusions table**  _(PwC, taxes-on-personal-income)_

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERENCIA PROPIA, ENTRE CUENTAS, CUENTA PROPIA | EXCLUDE | Own-account transfer |
| PRÉSTAMO, ABONO PRÉSTAMO, CAPITAL (loan principal) | EXCLUDE | Loan principal movement |
| INTERESES (ahorro/plazo panameño, valores del Estado) | EXCLUDE | Exempt income (PwC, taxes-on-personal-income) |

### 3.6 Panamanian Banks — Statement Format Reference

**Panamanian Banks table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Banco General | TRANSFERENCIA, ACH, DÉBITO, CRÉDITO, ABONO | PDF/CSV; descriptions in Spanish |
| Banistmo | PAGO, TRF, DÉBITO DIRECTO, COMISIÓN | PDF/CSV |
| Banco Nacional de Panamá (BNP) | DEPÓSITO, RETIRO, CARGO | PDF; state bank |
| BAC Credomatic | COMPRA, PAGO, TRANSFERENCIA, CARGO | CSV; card transactions show merchant |
| Multibank / MMG | TRANSFERENCIA, ACH, CARGO | PDF |

## Section 4 — Worked Examples

### Example 1 — Client Payment (Panama-source professional fee)

**Input line:**
`15/03/2025 ; TRANSFERENCIA ACH ; CORPORACIÓN ISTMO S.A. ; HONORARIOS FACTURA 0042 ; +3,500.00 ; USD`

**Reasoning:**
Professional fee from a Panamanian company for services performed in Panama. Panama-source business income. No VAT-style gross-up applies to ISR base (Panama's consumption tax is ITBMS, handled separately). Full USD 3,500 is taxable income.

**Classification:** Taxable income = USD 3,500.

### Example 2 — Software Subscription (Deductible business expense)

**Input line:**
`01/04/2025 ; CARGO TARJETA ; ADOBE SYSTEMS ; CREATIVE CLOUD ABRIL ; -52.99 ; USD`

**Reasoning:**
Recurring SaaS subscription used to produce business income. Ordinary and necessary business expense, fully deductible for a self-employed taxpayer.

**Classification:** Deductible business expense = USD 52.99.

### Example 3 — Client Entertainment (Blocked)

**Input line:**
`22/04/2025 ; COMPRA TARJETA ; RESTAURANTE MARKET ; CENA CLIENTE ; -120.00 ; USD`

**Reasoning:**
Entertainment. Unreimbursed entertainment is not deductible per PwC deductions guidance. No partial deduction.

**Classification:** NOT deductible. Remove entirely.

### Example 4 — Employee CSS + Educational Insurance Deduction (payroll)

**Input:** Monthly gross salary USD 2,000, employee, current (from April 2025) rates.

**Reasoning:**
- Employee CSS: 2,000 × 9.75% = USD 195.00 (PwC, other-taxes)
- Educational insurance (employee): 2,000 × 1.25% = USD 25.00 (PwC, other-taxes; FMM)
- Total employee statutory withholding = 195.00 + 25.00 = **USD 220.00**
- No salary ceiling applies (PwC, other-taxes)

**Classification:** Employee statutory deductions = USD 220.00/month. (ISR withholding computed separately on the progressive table.)

### Example 5 — Self-Employed Annual ISR (mid-range, Panama-source)

**Input:** Resident self-employed, Panama-source net taxable income USD 40,000 (after allowable business expenses), no confirmed personal deductions.

**Reasoning:**
- Falls in the 11,001–50,000 band.
- Tax = (40,000 − 11,000) × 15% = 29,000 × 15% = **USD 4,350.00**

**Classification:** ISR due = USD 4,350.00.

### Example 6 — Higher-Income Self-Employed (top bracket)

**Input:** Resident self-employed, Panama-source net taxable income USD 75,000.

**Reasoning:**
- Falls in the "Over 50,000" band.
- Tax = 5,850 fixed + (75,000 − 50,000) × 25% = 5,850 + 25,000 × 25% = 5,850 + 6,250 = **USD 12,100.00**

**Classification:** ISR due = USD 12,100.00.

## Section 5 — Tier 1 Rules (When Data Is Clear)

### 5.1 The Territorial Source Rule

- **Territorial source rule** — Only Panamanian-source income is taxable, for residents and non-residents alike. Income from services performed, or assets located, outside Panama is not taxable regardless of where it is received or banked. Classify the source of every income stream before computing tax. When source is genuinely ambiguous (e.g. cross-border services), invoke R-PA-1.  _(PwC, taxes-on-personal-income)_

### 5.2 Progressive ISR Computation (natural persons)

**Progressive ISR Computation table**  _(PwC, taxes-on-personal-income (reviewed 18 Jan 2026))_

| Taxable Income (USD) | Computation |
| --- | --- |
| 0 – 11,000 | USD 0 |
| 11,001 – 50,000 | (income − 11,000) × 15% |
| Over 50,000 | 5,850 + (income − 50,000) × 25% |

- **No local or AMT** — No local/municipal income tax; no individual alternate minimum tax.  _(PwC, taxes-on-personal-income)_

### 5.3 Exempt Income

- **Exempt income list** — Interest on Panamanian government securities. Interest on Panamanian bank savings accounts and time deposits. Foreign-source income (territorial rule).  _(PwC, taxes-on-personal-income)_

### 5.4 Personal Deductions

- **Personal Deductions key caps** — See Section 1 table. Key caps: personal exemption USD 800 (married); mortgage interest USD 15,000; pension USD 15,000; education USD 3,600/student; charitable donations USD 50,000; medical (no cap stated). All require documentation. The USD 250/dependent figure is [RESEARCH GAP — reviewer to confirm].  _(PwC, deductions)_

### 5.5 Social Security (CSS) + Educational Insurance — Law 462 of 18 March 2025

**Basis:** PwC, other-taxes; Fábrega Molino (FMM); Morgan & Morgan.

**Employees (current, from April 2025 payroll) table**  _(PwC, other-taxes; FMM)_

| Component | Rate | Source |
| --- | --- | --- |
| CSS (employee) | 9.75% of gross salary | PwC, other-taxes; FMM |
| Educational insurance (employee) | 1.25% of salary | PwC, other-taxes; FMM |
| **Total employee** | **11.00%** | sum: 9.75 + 1.25 = 11.00 |

**Employers (phased increase under Law 462) table**  _(PwC, other-taxes; Morgan & Morgan)_

| Component | Rate | Source |
| --- | --- | --- |
| CSS (employer) — from 1 Apr 2025 | 13.25% | PwC, other-taxes; Morgan & Morgan |
| CSS (employer) — from 1 Mar 2027 | 14.25% | Morgan & Morgan |
| CSS (employer) — from 1 Mar 2029 | 15.25% | Morgan & Morgan |
| Educational insurance (employer) | 1.50% of salary | PwC, other-taxes |
| **Total employer (current, from Apr 2025)** | **14.75%** | sum: 13.25 + 1.50 = 14.75 |

**Combined headline (current, from April 2025) table**  _(PwC, other-taxes; Morgan & Morgan)_

| Party | CSS | Educational insurance | Total |
| --- | --- | --- | --- |
| Employee | 9.75% | 1.25% | 11.00% |
| Employer | 13.25% | 1.50% | 14.75% |
| **Combined** | **23.00%** | **2.75%** | **25.75%** |

- **Arithmetic check** — Employee column: 9.75 + 1.25 = 11.00. Employer column: 13.25 + 1.50 = 14.75. Combined CSS: 9.75 + 13.25 = 23.00. Combined education: 1.25 + 1.50 = 2.75. Combined total: 11.00 + 14.75 = 25.75 (= 23.00 + 2.75). All reconcile.
- **Salary ceiling/floor** — CSS and educational insurance apply with no maximum taxable limit (no ceiling) and no floor for employees.  _(PwC, other-taxes)_

### 5.6 Self-Employed / Independent Workers (NEW under Law 462)

**Self-Employed / Independent Workers table**  _(Morgan & Morgan; Pension Policy International)_

| Component | Rate | Status |
| --- | --- | --- |
| IVM (Disability, Old Age, Death) | 9.36% of taxable income | Mandatory |
| Health & maternity program | additional 8.5% of declared contributory income | Voluntary (opt-in); if opted in, declared base ≥ USD 800/month |

- **Registration and gap** — Independent/self-employed workers must now register with CSS for the first time. [RESEARCH GAP — reviewer to confirm] the income threshold (if any) below which independents are exempt from the mandatory 9.36% IVM contribution; verify against CSS / Law 462 primary text.  _(Morgan & Morgan; Pension Policy International)_

### 5.7 Retirement Age (unchanged by Law 462)

- **Retirement age** — Women: 57. Men: 62. Subject to future actuarial review.  _(FMM)_

### 5.8 Filing, Estimated Tax, and Withholding

**Filing, Estimated Tax, and Withholding table**  _(PwC, tax-administration; Casattis)_

| Item | Detail |
| --- | --- |
| Tax year | Calendar year |
| Filing deadline (individuals) | 15 March following the tax year (FY2025 due 15 March 2026) |
| Extension | One-month extension on request before the deadline |
| Filing platform | e-Tax 2.0 (DGI online portal) |
| Estimated tax instalments | Three equal instalments: 30 June, 30 September, 31 December |
| Who must file | All taxpayers **except** employees with a single salary source where the employer withholds. Must file if claiming non-business expenses, or receiving representation allowances / salary in kind |
| Non-residents | Panama-source income subject to withholding by the payer |
| Form code | **[RESEARCH GAP — reviewer to confirm]** the exact DGI individual return form code (commonly the "Declaración Jurada de Rentas" for personas naturales; PwC does not give a form number) |

### 5.9 Non-Deductible Expenses (summary)

**Non-Deductible Expenses table**  _(PwC, deductions)_

| Expense | Reason |
| --- | --- |
| Entertainment (unreimbursed) | Blocked (PwC, deductions) |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax (ISR) itself | Tax on income |
| Unreimbursed moving/travel (employees) | Blocked (PwC, deductions) |
| Drawings / personal withdrawals | Not an expense |
| Foreign-source-related expenses | Match exempt foreign income — not deductible against Panama-source |

## Section 6 — Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Panama-Source vs Foreign-Source Split

- **Panama-source vs foreign-source split** — Where services are partly performed in Panama and partly abroad, the source split drives the entire computation. Conservative default: STOP and flag — do not allocate without reviewer confirmation. Flag for reviewer: Confirm place of performance and contractual situs for each income stream.

### 6.2 Home Office / Mixed-Use Business Expenses

- **Home office / mixed-use expenses** — Only the business-use portion of home utilities, rent, phone, and internet is deductible for a self-employed taxpayer. Conservative default: 0% deduction until apportionment is documented. Flag for reviewer: Confirm dedicated workspace and apportionment basis.

### 6.3 Motor Vehicle Business Use

- **Motor vehicle business use** — Only the business-use percentage of fuel, insurance, and maintenance is deductible. Conservative default: 0% business use until a usage log is provided. Flag for reviewer: Confirm business percentage is documented and reasonable.

### 6.4 13th-Month Bonus (Décimo Tercer Mes)

- **13th-month bonus treatment** — Panama mandates a 13th-month bonus paid in three parts (15 April, 15 August, 15 December) under labour law. [RESEARCH GAP — reviewer to confirm] the exact CSS and ISR treatment of the décimo (e.g. whether it is subject to reduced CSS treatment); not re-verified against a primary source in this pass. Flag for reviewer: Confirm payroll and tax treatment of the décimo before finalising.

### 6.5 Self-Employed Health & Maternity Opt-In

- **Health & maternity opt-in** — The 8.5% health & maternity CSS contribution for independents is voluntary; if elected, the declared base may not be below USD 800/month. Flag for reviewer: Confirm whether the client has opted in and the declared contributory income.

### 6.6 Dependent Deductions

- **Dependent deductions** — The USD 250/dependent deduction is unconfirmed against the authoritative PwC page. Conservative default: 0 dependent deduction. Flag for reviewer: Confirm the current dependent-deduction figure against DGI / Código Fiscal before claiming.

### 6.7 Medical Expenses (no stated cap)

- **Medical expenses** — PwC states medical expenses incurred in Panama are deductible (documented) with no cap stated. Flag for reviewer: Confirm documentation and that expenses were incurred in Panama.  _(PwC, deductions)_

## Section 7 — Excel Working Paper Template

```
PANAMA PERSONAL INCOME TAX (ISR) — WORKING PAPER
Tax Year: 2025
Client: ___________________________
Residency: Resident / Non-resident
Marital Status: Single / Married   Dependents: ____
Worker Type: Employee / Self-employed (independent)
RUC: ___________________________

A. PANAMA-SOURCE GROSS INCOME
  A1. Business / professional income (Panama-source)   ___________
  A2. Employment income (planilla)                     ___________
  A3. Rental income (property in Panama)               ___________
  A4. Other Panama-source income                       ___________
  A5. TOTAL Panama-source gross income                 ___________

  (EXCLUDE: foreign-source income; exempt PA bank/govt interest)

B. ALLOWABLE BUSINESS EXPENSES (self-employed)
  B1. Office rent                                      ___________
  B2. Accountancy / legal fees                         ___________
  B3. Software subscriptions / IT                      ___________
  B4. Marketing / advertising                          ___________
  B5. Bank charges                                     ___________
  B6. Office supplies                                  ___________
  B7. Other allowable business expenses                ___________
  B8. TOTAL business expenses                          ___________

C. NET BUSINESS INCOME (A1 - B8)                       ___________

D. PERSONAL DEDUCTIONS (with caps)
  D1. Personal exemption (married, USD 800)            ___________
  D2. Mortgage interest (max 15,000)                   ___________
  D3. Pension contributions (max 15,000)               ___________
  D4. Education (max 3,600 per student)                ___________
  D5. Medical (Panama, documented)                     ___________
  D6. Charitable donations (max 50,000)                ___________
  D7. Dependent deduction [RESEARCH GAP - confirm]     ___________
  D8. TOTAL personal deductions                        ___________

E. TAXABLE INCOME (C + A2 + A3 + A4 - D8)              ___________

F. ISR COMPUTATION (pass to deterministic engine)
  0-11,000: 0
  11,001-50,000: (E - 11,000) x 15%
  Over 50,000: 5,850 + (E - 50,000) x 25%
  F1. ISR liability                                    ___________
  F2. Less: estimated tax paid (Jun/Sep/Dec)           ___________
  F3. Less: ISR withheld at source                     ___________
  F4. ISR due / refund                                 ___________

G. SOCIAL SECURITY (CSS) — informational
  G1. Employee CSS 9.75% / Independent IVM 9.36%       ___________
  G2. Educational insurance (employee 1.25%)           ___________

REVIEWER FLAGS:
  [ ] Panama-source vs foreign-source confirmed for each stream?
  [ ] Residency status confirmed?
  [ ] Worker type confirmed (employee vs independent)?
  [ ] Personal deduction caps respected?
  [ ] Dependent deduction figure confirmed? [RESEARCH GAP]
  [ ] Home-office / vehicle apportionment documented?
  [ ] Exempt interest (PA bank/govt) excluded?
  [ ] Décimo tercer mes treatment confirmed? [RESEARCH GAP]
  [ ] DGI return form code confirmed? [RESEARCH GAP]
```

## Section 8 — Bank Statement Reading Guide

### Panamanian Bank Statement Formats

**Panamanian Bank Statement Formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Banco General | PDF, CSV | Fecha, Descripción, Débito, Crédito, Saldo | Most common; Spanish descriptions |
| Banistmo | PDF, CSV | Fecha valor, Descripción, Monto, Saldo | Card transactions show merchant |
| Banco Nacional (BNP) | PDF | Fecha, Concepto, Retiro, Depósito | State bank; shorter descriptions |
| BAC Credomatic | CSV | Fecha, Comercio/Concepto, Monto, Moneda | Clean merchant names |
| Multibank / MMG | PDF | Fecha, Detalle, Cargo, Abono | Less common CSV |

### Key Panamanian / Spanish Banking Terms

**Key Banking Terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| TRANSFERENCIA / TRF | Transfer | Check direction for income/expense |
| ACH | Automated clearing house transfer | Common for payroll and bills |
| DÉBITO DIRECTO | Direct debit | Regular expense (utility, subscription) |
| ABONO | Credit/deposit | Potential income |
| CARGO | Charge/debit | Expense — check merchant |
| RETIRO / CAJERO | Withdrawal / ATM | Ask what cash was spent on |
| COMISIÓN / SPEJJEZ→ COMISIÓN BANCARIA | Bank charge | Deductible (business account) |
| INTERESES | Interest | Often exempt income (PA bank/govt) |
| HONORARIOS / FACTURA | Fees / invoice | Business income |
| PLANILLA / SALARIO / SUELDO | Payroll / salary | Employment income |
| DÉCIMO / XIII MES | 13th-month bonus | Special treatment — flag |
| CSS / SEGURO EDUCATIVO | Social security / educational insurance | Statutory deduction |

## Section 9 — Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all source-ambiguous credits and all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1) — including 0% personal deductions where undocumented and excluding foreign-source income only where confirmed.
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS — PANAMA INCOME TAX
1. Are you a Panama tax resident or non-resident?
2. For each income stream: were the services performed (or assets located) in Panama, or abroad?
3. Worker type: employee (on a planilla) or self-employed/independent?
4. Marital status (single/married) and number of dependents?
5. Do you have deductible: mortgage interest, pension contributions, education,
   medical (in Panama), or charitable donations? Amounts and receipts?
6. Do you operate a business? If so, do you have a RUC and Aviso de Operación?
7. CSS: how much was contributed in the year? (employee 9.75% / independent IVM 9.36%)
8. Did you make estimated tax instalments (Jun/Sep/Dec)? Amounts?
9. Was any ISR withheld at source?
10. Did you receive a décimo tercer mes (13th-month bonus)?
```

## Section 10 — Reference Material

### Key References

**Key References table**

| Topic | Reference |
| --- | --- |
| Income tax rates (natural persons) | PwC Worldwide Tax Summaries — Panama, taxes-on-personal-income (reviewed 18 Jan 2026): https://taxsummaries.pwc.com/panama/individual/taxes-on-personal-income |
| Personal deductions | PwC — Panama, deductions: https://taxsummaries.pwc.com/panama/individual/deductions |
| Social security & educational insurance | PwC — Panama, other-taxes: https://taxsummaries.pwc.com/panama/individual/other-taxes |
| Filing / estimated tax / administration | PwC — Panama, tax-administration: https://taxsummaries.pwc.com/panama/individual/tax-administration |
| Law 462 of 2025 (CSS reform) — highlights | Fábrega Molino: https://fmm.com.pa/panama-social-security-reform-2025-key-highlights-of-law-no-462/ |
| Law 462 of 2025 — employer phased rates & self-employed | Morgan & Morgan: https://morimor.com/law-no-462-of-march-18-2025-key-reforms-to-the-social-security-fund-css-of-panama/ |
| Self-employed CSS obligations | Pension Policy International: https://www.pensionpolicyinternational.com/panama-la-ley-462-de-la-css-beneficios-y-nuevas-obligaciones-a-trabajadores-independientes/ |
| Filing deadlines & extensions | Casattis: https://casattis.com/en/presentaciones-de-la-declaracion-de-renta-en-panama-y-sus-prorrogas/ |
| Penalties (non-primary) | Limitless Legal: https://www.limitlesslegal.com/en-us/blog/avoid-fines-for-non-declaration-panama-business |
| Minimum wage (Decree 13/2025) | Galindo Arias & López; Lovill; MITRADEL (see Section 10.2) |
| MEF official CSS reform PDF (primary, unparsed) | https://www.mef.gob.pa/wp-content/uploads/2025/05/250428-Republic-of-Panama-CSS-Reform-Takeaways.pdf |

### 10.1 Penalties (less authoritative — law-firm sourced)

- **Penalties** — Late/non-filing fines can be automatically generated from USD 500 (B/. 500.00) upward, with risk of tax audit or suspension of the Aviso de Operación (Limitless Legal). Companies with an active Aviso de Operación but zero income must still file a zero-income return or face automatic fines (Limitless Legal). [RESEARCH GAP — reviewer to confirm] no DGI primary-source penalty schedule (late-payment interest rate, surcharge %) was located; verify against the Código Fiscal / DGI.  _(Limitless Legal)_

### 10.2 Minimum Wage

- **Minimum wage** — Panama sets minimum wage by hourly rate, differentiated across 59 rates covering 74 economic activities, by region (Region 1 / Region 2), sector, and company size. There is no single national monthly figure (Galindo Arias & López; MITRADEL). Current (2026–2027 period): Executive Decree No. 13 of 31 Dec 2025, published 6 Jan 2026, effective 16 January 2026. Example cited: ~USD 320.00/month for some Region 2 categories (Lovill; Galindo Arias & López). [RESEARCH GAP — reviewer to confirm] the exact applicable cell must be read per activity/region/company-size from Decree No. 13/2025 (Gaceta Oficial). No single number applies.  _(Galindo Arias & López; Lovill; MITRADEL)_

### 10.3 Registration

- **Registration** — Taxpayers register via the RUC (Registro Único de Contribuyente); DGI ran mandatory RUC/TIN update campaigns through 2025. Businesses need an Aviso de Operación (KPMG; FMM — general, not re-verified to a primary source in this pass).  _(KPMG; FMM)_

### Test Suite

Input: Resident self-employed, Panama-source taxable income USD 40,000, no confirmed personal deductions.
Expected: 40,000 in the 11,001–50,000 band. ISR = (40,000 − 11,000) × 15% = 29,000 × 15% = **USD 4,350.00**.

Input: Resident self-employed, Panama-source taxable income USD 75,000.
Expected: ISR = 5,850 + (75,000 − 50,000) × 25% = 5,850 + 6,250 = **USD 12,100.00**.

Input: Resident, Panama-source taxable income USD 11,000.
Expected: ISR = **USD 0.00** (top of the 0% band).

Input: Resident, Panama-source taxable income USD 25,000.
Expected: ISR = (25,000 − 11,000) × 15% = 14,000 × 15% = **USD 2,100.00**.

Input: Employee, monthly gross salary USD 2,000 (current rates from April 2025).
Expected: Employee CSS = 2,000 × 9.75% = 195.00; educational insurance = 2,000 × 1.25% = 25.00; total employee statutory = **USD 220.00**. No salary ceiling.

Input: Same USD 2,000 salary, employer side (from April 2025).
Expected: Employer CSS = 2,000 × 13.25% = 265.00; employer educational insurance = 2,000 × 1.50% = 30.00; total employer statutory = **USD 295.00** (14.75% of 2,000).

Input: USD 1,200 interest credited from a Panamanian bank time deposit.
Expected: EXCLUDE — exempt income (PwC, taxes-on-personal-income). Not in taxable income.

Input: USD 5,000 received for consulting work performed entirely abroad for a foreign client.
Expected: EXCLUDE — foreign-source income is not taxable under the territorial rule. Confirm source with reviewer (R-PA-1).

Input: Self-employed independent, taxable income base USD 30,000/year, did not opt into health & maternity.
Expected: Mandatory IVM = 30,000 × 9.36% = **USD 2,808.00**. No 8.5% health/maternity (not opted in). [Confirm any exemption threshold — RESEARCH GAP.]

## PROHIBITIONS

- NEVER tax foreign-source income — Panama is strictly territorial.
- NEVER include exempt interest (Panamanian bank savings/time deposits, government securities) in taxable income.
- NEVER compute ISR for a non-resident as a self-assessed return — non-residents are taxed by withholding (R-PA-2).
- NEVER claim a personal deduction above its statutory cap (mortgage 15,000; pension 15,000; education 3,600/student; donations 50,000).
- NEVER claim the USD 250/dependent deduction as fact — it is unconfirmed [RESEARCH GAP].
- NEVER allow entertainment, fines, ISR itself, or drawings as deductions.
- NEVER apply a salary ceiling to CSS or educational insurance — there is none.
- NEVER confuse the employee CSS rate (9.75%) with the independent IVM rate (9.36%).
- NEVER state a penalty schedule or a minimum-wage figure as confirmed — both carry RESEARCH GAP markers.
- NEVER present tax calculations as definitive — always label as estimated and pass the bracket computation to the deterministic engine.

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
