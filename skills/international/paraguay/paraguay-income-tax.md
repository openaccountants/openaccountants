---
name: paraguay-income-tax
description: Use this skill whenever asked about Paraguay personal income tax (IRP) for self-employed individuals and personal-service providers. Trigger on phrases like "how much tax do I pay in Paraguay", "IRP", "Impuesto a la Renta Personal", "Form 715", "Form 716", "RSP", "RGC", "renta neta", "declaración jurada", "allowable deductions Paraguay", "IPS contributions", "aporte obrero", "aporte patronal", "Marangatú", "RUC registration", "salario mínimo", "self-employed tax Paraguay", or any question about filing or computing income tax for a Paraguayan resident with Paraguay-source income. Also trigger when preparing or reviewing an IRP RSP (715) or IRP RGC (716) return, computing documented deductible expenses, or advising on IPS social-security contributions and IVA interaction. This skill covers the territorial basis, the 8%/9%/10% progressive scale (personal services), the flat 8% capital regime, the gross-income filing threshold, IPS rates, minimum wage, penalties, and interaction with IVA. ALWAYS read this skill before touching any Paraguay income tax work.
version: 0.1
jurisdiction: PY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Paraguay Personal Income Tax (IRP) -- Self-Employed

## Paraguay Personal Income Tax (IRP) -- Self-Employed Skill v0.1

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Paraguay (Republic of Paraguay) |
| Tax | Personal Income Tax -- IRP (Impuesto a la Renta Personal) |
| Currency | Guaraní (PYG / ₲) only |
| Tax year | Calendar year (1 January -- 31 December); liability originates at close of fiscal year (31 Dec) [PwC tax administration] |
| Basis | **Territorial** -- only Paraguay-source income is taxed; foreign-source income generally exempt [Ley 6380/19; PwC] |
| Primary legislation | Ley N° 6380/2019 ("Modernización y Simplificación del Sistema Tributario Nacional"), in force since Jan 2020 |
| Supporting legislation | Arts. 14-15, 64 Ley 6380/19 (deductions); Ley N° 125/1991 (Tax Code -- penalties); RG N° 90/2021 (Marangatú e-filing) |
| Tax authority | DNIT -- Dirección Nacional de Ingresos Tributarios (formerly SET) |
| Social security authority | IPS -- Instituto de Previsión Social |
| Labour / minimum wage authority | MTESS -- Ministerio de Trabajo, Empleo y Seguridad Social |
| Filing portal | Marangatú (electronic; RG N° 90/2021) |
| Filing deadline | Annual return + payment in **March** of the following year; exact day set by last digit of RUC ("calendario perpetuo") [PwC; DNIT IRP] |
| Validated by | Pending -- requires sign-off by a Paraguayan licensed accountant / DNIT-registered professional |
| Validation date | Pending |
| Skill version | 0.1 |

### IRP Categories and Forms

**IRP Categories and Forms table**

| Category | Form / obligation code | Basis | Rate |
| --- | --- | --- | --- |
| Personal services income (RSP -- Rentas de Servicios Personales) | **715 -- IRP RSP** | Net income (renta neta) | Progressive 8% / 9% / 10% [PwC; Ley 6380/19] |
| Capital gains & income (RGC -- Rentas y Ganancias del Capital) | **716 -- IRP RGC** | Net income | Flat **8%** [PwC; DNIT IRP] |

### Tax Rate Brackets -- Personal Services (RSP), tax year 2025

**Tax Rate Brackets -- Personal Services (RSP), tax year 2025**  _([Source: PwC, last reviewed 7 Feb 2026, https://taxsummaries.pwc.com/paraguay/individual/taxes-on-personal-income ; statutory basis Ley 6380/19])_

| Annual net taxable income (PYG) | Marginal rate | Cumulative tax at top of band |
| --- | --- | --- |
| Up to 50,000,000 | 8% | ₲4,000,000 |
| 50,000,001 -- 150,000,000 | 9% | ₲13,000,000 |
| 150,000,001 and above | 10% | -- |

- **Cumulative-tax check** — band 1 = 50,000,000 × 8% = ₲4,000,000. Band 2 = 100,000,000 × 9% = ₲9,000,000; cumulative at ₲150,000,000 = 4,000,000 + 9,000,000 = ₲13,000,000. Band 3 marginal 10% above ₲150,000,000.

### Capital Gains & Income (RGC) -- Form 716

**Capital Gains & Income (RGC) -- Form 716 table**

| Income type | Rate |
| --- | --- |
| Dividends, interest, royalties, rentals, capital gains | Flat **8%** on net income [PwC; DNIT IRP] |

### Gross-Income Filing / Payment Threshold (RSP)

**Gross-Income Filing / Payment Threshold (RSP) table**

| Item | Value |
| --- | --- |
| Annual gross personal-services income below which IRP is **not payable** | ₲80,000,000 per year [PwC] |
| Above the threshold | Progressive 8% / 9% / 10% scale applies on **net** income |

- **Important distinction** — the ₲80,000,000 figure is the gross-income registration/payment threshold. The 8%/9%/10% brackets are applied to net taxable income (renta neta), not to gross turnover.  _([PwC])_

### Conservative Defaults

**Conservative Defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown IRP category (RSP 715 vs RGC 716) | STOP -- ask whether income is from personal services or from capital |
| Unknown whether expense is documented with legal invoice | NOT deductible (no invoice = no deduction) |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown expense category | Not deductible |
| Unknown residency / RUC registration | STOP -- confirm RUC registration before computing |
| "Standard deduction %" requested | Do NOT apply a fixed % -- deductions are documentation-based [RESEARCH GAP -- no statutory standard deduction; see Section 5.3] |
| Unknown whether income is Paraguay-source | Treat as out of scope until source confirmed (territorial system) |
| IPS contribution base unknown | Use actual gross salary; never below the legal minimum wage floor |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable** — bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of RUC registration, IRP category (RSP 715 / RGC 716), and that the income is Paraguay-source.
- **Recommended** — all legal invoices (facturas) issued and received, IPS contribution records (if an employer or employee), prior-year declaración jurada or DNIT assessment, IVA registration status.
- **Ideal** — complete income and expenditure account, asset/expense register cross-referenced to legal invoices, Marangatú voucher register, evidence that deductions were funded from IRP-taxed income (Arts. 14-15 Ley 6380/19).  _(Arts. 14-15 Ley 6380/19)_
- **Refusal if minimum is missing -- SOFT WARN** — No bank statement at all = hard stop. Bank statement without legal invoices = proceed with reviewer warning: "This IRP computation was produced from bank statement alone. Under Art. 64 Ley 6380/19, deductions require a properly documented legal invoice (factura legal) representing a real expense directly related to the taxed activity. The reviewer must verify documentation before any deduction is claimed."  _(Art. 64 Ley 6380/19)_

### Refusal Catalogue

- **R-PY-1 -- IRP category unknown** — "IRP has two regimes: RSP (Form 715, personal services, progressive 8%/9%/10%) and RGC (Form 716, capital, flat 8%). This skill cannot compute tax without knowing which applies. Please confirm the nature of the income."
- **R-PY-2 -- Companies / corporate income** — "This skill covers resident individuals (IRP) only. Corporate income (IRE -- Impuesto a la Renta Empresarial) and simplified business regimes have separate rules. Escalate to a Paraguayan licensed accountant."
- **R-PY-3 -- Non-resident / foreign-source income** — "Paraguay's IRP is territorial. Non-resident taxation and the source classification of cross-border income require specialised analysis. Out of scope. Escalate to a Paraguayan licensed accountant."
- **R-PY-4 -- Complex capital gains / property disposals** — "Capital gains computations under the RGC regime (real estate, securities, share transfers) require specialised analysis of cost basis and source. Escalate to a Paraguayan licensed accountant."
- **R-PY-5 -- Arrears / enforcement** — "Client has outstanding tax debt or is subject to DNIT enforcement. Mora, omisión de pago and defraudación penalties under Ley 125/1991 are severe. Note the exceptional regularization regime running to 31 Aug 2026 for periods closed up to December 2023. Do not advise. Escalate to a Paraguayan licensed accountant immediately."
- **R-PY-6 -- IVA (VAT) return requested** — "This skill covers personal income tax (IRP) only. For Paraguay IVA, use the paraguay-vat skill if available."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. Paraguay statements are in Spanish. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules. **Every claimed deduction additionally requires a legal invoice (factura legal) under Art. 64 Ley 6380/19 -- bank match alone is not sufficient.**

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns table**

| Pattern | IRP Treatment | Notes |
| --- | --- | --- |
| Client name + TRANSFERENCIA, DEPOSITO, PAGO RECIBIDO, COBRO | RSP gross income (715) | Personal-services income. If IVA-registered, extract net (excl. 10% IVA) |
| HONORARIOS, SERVICIOS PROFESIONALES, CONSULTORIA | RSP gross income (715) | Professional fees -- typical self-employed |
| STRIPE PAYOUT, STRIPE TRANSFER | RSP gross income (715) | Confirm income is Paraguay-source before including (territorial) |
| PAYPAL, WISE, PAYONEER, MERCADO PAGO | RSP gross income (715) | Platform payout -- confirm source and match to invoices |
| UPWORK, FIVERR, WORKANA | RSP gross income (715) | Freelance platform -- confirm Paraguay-source |
| SALARIO, SUELDO, REMUNERACION, EMPLEADOR [name] | Employment income | NOT self-employment -- subject to employer IRP/IPS withholding, not Form 715 self-employed line |
| ALQUILER RECIBIDO, RENTA INMUEBLE | RGC income (716) | Rental income -- flat 8% capital regime |
| INTERESES RECIBIDOS, INTERES | RGC income (716) | Interest income -- flat 8% |
| DIVIDENDOS, DIVIDENDO | RGC income (716) | Dividend income -- flat 8% |
| DEVOLUCION DNIT, DEVOLUCION SET, REINTEGRO IMPUESTO | EXCLUDE | Tax refund from prior period |
| SUBSIDIO, APORTE ESTATAL | Check nature | Revenue subsidy may be income; confirm with reviewer |

### 3.2 Expense Patterns (Debits) -- Deductible if Directly Related + Invoiced (RSP only)

**Expense Patterns (deductible) table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| ALQUILER OFICINA, ALQUILER LOCAL | Office rent | Deductible | Dedicated business premises; factura legal required |
| HONORARIOS CONTADOR, AUDITORIA, CONTABILIDAD | Accountancy fees | Deductible | Directly related to activity |
| HONORARIOS ABOGADO, GASTOS LEGALES (business) | Legal fees | Deductible | Must be business-related |
| UTILES, PAPELERIA, LIBRERIA, INSUMOS OFICINA | Office supplies | Deductible |  |
| PUBLICIDAD, MARKETING, GOOGLE ADS, META ADS | Marketing/advertising | Deductible |  |
| CAPACITACION, CURSO, SEMINARIO, CONGRESO | Training | Deductible | Must relate to current activity |
| COMISION BANCARIA, GASTOS BANCARIOS, MANTENIMIENTO CUENTA | Bank charges | Deductible | Business account only |
| INTERNET, FIBRA, TIGO, PERSONAL, CLARO, COPACO (business) | Telecoms | Deductible -- business % only | Default 0% if mixed-use (T2) |
| DOMINIO, HOSTING, AWS, CLOUDFLARE | IT infrastructure | Deductible | Software/services directly related |

- **Deduction condition intro** — Under Art. 64 Ley 6380/19, RSP taxpayers may deduct expenses directly related to the taxed activity, properly documented with a legal invoice (factura legal), representing a real expense, and funded from IRP-taxed income (Arts. 14-15).  _(Art. 64 Ley 6380/19; Arts. 14-15)_

### 3.3 Expense Patterns (Debits) -- SaaS and Software

**SaaS and Software table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring subscription = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, DROPBOX | Software subscription | Deductible |  |

### 3.4 Expense Patterns (Debits) -- 1% Cap / Special Cases

**1% Cap / Special Cases table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| Purchases from RESIMPLE contributors | Capped purchases | Deductible only up to 1% of gross income | Flag for reviewer |
| Donations / specific listed items (arts. items 7,8,20,21,22) | Capped items | Deductible only up to 1% of gross income | [RESEARCH GAP -- reviewer to confirm exact item list against current Ley 6380/19 text] |

- **1% of gross income cap** — A 1% of gross income deductibility cap applies in specific cases (items 7, 8, 20, 21, 22 of the relevant article, and purchases from RESIMPLE contributors).  _([Source: Ley 6380/19 via impuestospy.com; rsa.com.py])_

### 3.5 Expense Patterns (Debits) -- Travel

**Travel table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| AEROLINEAS, LATAM, GOL, BOLETO AEREO | Flights | Deductible if business travel | Must be directly related to activity |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| TAXI, UBER, BOLT, MUV | Local transport | Deductible if business purpose |  |
| COMBUSTIBLE, NAFTA, GASOIL, PETROBRAS, PUMA | Vehicle fuel | Deductible -- business % only (T2) | Requires usage log |
| ESTACIONAMIENTO, PEAJE | Parking/tolls | Deductible -- business % only (T2) |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**NOT Deductible table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANTE, ALMUERZO, CENA (personal/entertainment) | Personal/entertainment | NOT deductible | Not directly related to activity |
| SUPERMERCADO, DESPENSA, COMPRAS PERSONALES, SUPER | Personal expenses | NOT deductible | Private living costs |
| MULTA, INFRACCION, SANCION | Fines/penalties | NOT deductible | Public policy |
| PAGO IRP, PAGO IMPUESTO, PAGO DNIT | Tax payments | NOT deductible | Income tax cannot reduce income |
| RETIRO PERSONAL, EXTRACCION ATM (personal) | Drawings | NOT deductible | Not an expense |
| Expense without factura legal | Undocumented | NOT deductible | Art. 64 Ley 6380/19 requires legal invoice |

### 3.7 Exclusions (Neither Income nor Expense)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERENCIA PROPIA, CUENTA PROPIA, ENTRE CUENTAS | EXCLUDE | Own-account transfer |
| PAGO PRESTAMO, CUOTA PRESTAMO, AMORTIZACION | EXCLUDE | Loan principal movement (interest may be relevant -- flag) |
| IPS, APORTE OBRERO, APORTE PATRONAL | IPS contribution | Social security, not an IRP deduction line -- record separately (see Section 5.6) |
| PAGO IVA, IVA DNIT | EXCLUDE | IVA liability payment, not an expense |

### 3.8 Paraguayan Banks -- Statement Format Reference

**Statement Format Reference table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Banco Itaú Paraguay | TRANSFERENCIA, DEBITO AUTOMATICO, COMISION | PDF/Excel; Spanish descriptions; date DD/MM/AAAA |
| Banco Continental | TRANSFERENCIA, PAGO, EXTRACCION | PDF; counterparty in description field |
| Banco Nacional de Fomento (BNF) | DEPOSITO, RETIRO, TRANSFERENCIA | PDF; shorter descriptions |
| Sudameris Bank | TRANSFERENCIA, DEBITO, CARGO | PDF/Excel |
| Ueno Bank / digital wallets | TRANSFERENCIA, QR, PAGO | App export; clean counterparty names |

## Section 4 -- Worked Examples

### Example 1 -- Client Payment (IVA-registered, RSP)

**Input line:**
`15/03/2025 ; ITAU TRANSFERENCIA RECIBIDA ; ESTUDIO LOPEZ S.A. ; PAGO FACTURA 001-001-0000123 ; +11,000,000 ; PYG`

**Reasoning:**
Client payment for personal services. Client is IVA-registered, so ₲11,000,000 includes 10% IVA. Net = ₲11,000,000 / 1.10 = ₲10,000,000 (RSP gross income, Form 715). The ₲1,000,000 IVA is collected on behalf of DNIT (excluded from income -- it is a liability).

**Classification:** RSP gross income = ₲10,000,000. IVA ₲1,000,000 excluded.

### Example 2 -- SaaS Subscription (Deductible, RSP)

**Input line:**
`01/04/2025 ; ITAU DEBITO AUTOMATICO ; ADOBE SYSTEMS ; CREATIVE CLOUD ABRIL ; -250,000 ; PYG`

**Reasoning:**
Monthly software subscription directly related to the taxed activity, supported by a legal invoice. Fully deductible operating expense under Art. 64 Ley 6380/19.

**Classification:** Deductible expense = ₲250,000 (subject to factura legal verification).

### Example 3 -- Personal Supermarket Spend (Not Deductible)

**Input line:**
`22/04/2025 ; ITAU TARJETA ; SUPERSEIS ; COMPRA ; -480,000 ; PYG`

**Reasoning:**
Supermarket / private living expense. Not directly related to the taxed activity. No deduction. No apportionment.

**Classification:** NOT deductible. Exclude from deductions.

### Example 4 -- IPS Employee Contribution at Minimum Wage

**Input line:**
`10/01/2025 ; ITAU DEBITO ; IPS APORTE OBRERO ; ENERO 2025 ; -260,914 ; PYG`

**Reasoning:**
Employee IPS contribution (aporte obrero) of 9.0% on the legal minimum wage of ₲2,899,048. Check: 2,899,048 × 9.0% = ₲260,914.32 → ₲260,914. [PwC other-taxes; MTESS Res. 677/2025] IPS is social security, recorded separately from the IRP deduction analysis; it is not a Box-style IRP expense line.

**Classification:** IPS aporte obrero = ₲260,914. Record under social security, not as an IRP business deduction.

### Example 5 -- Rental Income (RGC, Form 716)

**Input line:**
`05/06/2025 ; CONTINENTAL TRANSFERENCIA ; INQUILINO P. GIMENEZ ; ALQUILER JUNIO ; +3,000,000 ; PYG`

**Reasoning:**
Rental income falls under the capital regime (RGC, Form 716), taxed at a flat 8% on net income -- NOT under the progressive RSP scale. Net of any documented deductible rental costs.

**Classification:** RGC income (716) = ₲3,000,000. If no deductible costs, tax = 3,000,000 × 8% = ₲240,000.

### Example 6 -- Own-Account Transfer (Exclude)

**Input line:**
`15/05/2025 ; ITAU TRANSFERENCIA ; CUENTA PROPIA AHORRO ; ; -5,000,000 ; PYG`

**Reasoning:**
Transfer between the taxpayer's own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Territorial Basis

- **Territorial basis** — Paraguay taxes only Paraguay-source income. Foreign-source income is generally exempt. Before including any cross-border platform payout in RSP income, confirm the income is Paraguay-source.  _(Legislation: Ley N° 6380/2019 [PwC])_

### 5.2 The "Directly Related + Documented" Deduction Test

- **Deduction test** — An RSP expense is deductible only if it is (1) directly related to the taxed activity, (2) supported by a legal invoice (factura legal), (3) a real expense, and (4) funded from IRP-taxed income of the fiscal year (or from bank/financial/cooperative loans, or remaining IRP-taxed income from the prior 5 fiscal years). Mixed-use expenses must be apportioned to the business portion.  _(Art. 64 Ley 6380/19 (deduction principle); Arts. 14-15 Ley 6380/19 (general conditions))_

### 5.3 No Statutory Standard Deduction

- **No standard deduction** — There is no statutory fixed "standard deduction" percentage for IRP. Deductions are documentation-based. Some secondary guides cite an illustrative ~30% estimate, but this is not statutory and must not be applied as an official allowance.  _([RESEARCH GAP -- no published standard/automatic deduction; deductions are invoice-based. Reviewer to confirm.])_

### 5.4 The 1% Deductibility Cap

- **1% deductibility cap** — Certain expenses (items 7, 8, 20, 21, 22 of the relevant article, and purchases from RESIMPLE contributors) are deductible only up to 1% of gross income.  _([Source: Ley 6380/19 via impuestospy.com; rsa.com.py] [RESEARCH GAP -- reviewer to confirm exact item list against current statute.])_

### 5.5 Revenue Recognition and IVA

**Revenue Recognition and IVA table**

| Scenario | IRP Treatment |
| --- | --- |
| IVA collected on sales (IVA-registered) | NOT income -- exclude from RSP gross income |
| Input IVA recovered | NOT an expense -- exclude from deductions |
| Input IVA non-recoverable / not registered | IS a cost -- gross amount is the expense |

- **Standard/reduced IVA rate** — Standard IVA rate is 10%; a reduced 5% applies to certain goods (basic food basket, some real estate, pharmaceuticals).  _([Source: Ley 6380/19; PwC other-taxes])_

### 5.6 IPS Social Security (Recorded Separately)

- **IPS recorded separately** — IPS contributions are social security, computed on gross salary, and recorded separately from the IRP deduction analysis. See Section 5.7 for rates. They are not an IRP "business expense" line for a self-employed RSP taxpayer's own contributions; independent directors/managers/administrators may contribute to IPS optionally.  _([PwC other-taxes])_

### 5.7 IPS Contribution Rates

**Standard IPS contribution rates**  _([Source: PwC other-taxes, last reviewed Feb 2026])_

| Party | Rate |
| --- | --- |
| Employee (Aporte Obrero) | 9.0% of gross salary (withheld by employer) |
| Employer (Aporte Patronal) | 16.5% of gross salary |
| **Total** | **25.5%** |

- **Standard IPS total check** — 9.0% + 16.5% = 25.5%. ✓ (Employer 16.5% commonly described as 14% pension/health/maternity + 2.5% other worker-protection/training levies -- secondary breakdown only; the 25.5% total is authoritative.)

**Banks/financial institutions IPS contribution rates**  _([Source: PwC other-taxes])_

| Party | Rate |
| --- | --- |
| Employee | 11% |
| Employer | 17% |
| **Total** | **28%** |

- **Bank sector total check** — 11% + 17% = 28%. ✓
- **Contribution base floor** — Contribution base may not be below the legal monthly minimum wage (floor).  _([Source: IPS portal])_
- **No published cap** — No upper ceiling/cap on the general IPS contribution base was found in authoritative sources.  _([RESEARCH GAP -- no published cap; treat absence as default but flag for reviewer.])_
- **Contribution scope exclusions** — Contributions are on all wage items in cash or kind, EXCEPT the annual mandatory bonus (aguinaldo) and family allowance.  _([PwC])_
- **Micro & Small Enterprises IPS rules** — Micro & Small Enterprises (Ley N° 7444/2025, reglamented 2026): IPS = 25.5% on the established minimum taxable base; for owners/responsibles of Small Enterprises, base = 80% of the SMLV for 36 months from issuance of the MIPYMES card.  _([Source: MTESS Res. 220/2026; irunvillamayor.com.py])_
- **Payment timing** — contributions for a month are due in the first days of the following month.

### 5.8 Minimum Wage (MTESS)

**Minimum Wage table**  _(Legislation: Resolución MTESS N° 677/2025, effective 1 July 2025 (3.6% increase) [Source: mtess.gov.py/?p=30682; vouga.com.py])_

| Item | Amount (PYG) |
| --- | --- |
| Monthly minimum wage (Salario Mínimo Legal) | ₲2,899,048 |
| Daily wage -- jornaleros (day-rate) | ₲111,502 |
| Daily wage -- mensualizados | ₲96,635 |
| Hourly wage -- mensualizados | ₲12,080 |
| Night-shift monthly minimum (+30%, Labour Code) | ₲3,768,763 |

- **Night-shift check** — 2,899,048 × 1.30 = ₲3,768,762.40 → ₲3,768,763 (rounded). ✓ [RESEARCH GAP -- a further mid-2026 minimum-wage adjustment is typical but unconfirmed as of this research; use ₲2,899,048 until updated.]

### 5.9 Filing and Payment

**Filing and Payment table**  _(Legislation: RG N° 90/2021 (Marangatú e-filing); PwC tax administration)_

| Item | Detail |
| --- | --- |
| Tax year | Calendar year; liability originates 31 December |
| Return type | Annual declaración jurada |
| Filing & payment | March of the following year; exact day set by last digit of RUC ("calendario perpetuo") |
| FY2025 deadline | March 2026 |
| Filing method | Electronic via Marangatú |

- **Obligations per DNIT IRP page** — issue receipts/vouchers; communicate document numbering; register vouchers in Marangatú; file the declaración jurada; pay the tax.  _(DNIT IRP page)_

### 5.10 Non-Deductible Expenses

**Non-Deductible Expenses table**

| Expense | Reason |
| --- | --- |
| Expenses without a legal invoice (factura legal) | Art. 64 Ley 6380/19 |
| Expenses not directly related to the taxed activity | Art. 64 Ley 6380/19 |
| Personal living expenses | Not business-related |
| Fines and penalties | Public policy |
| Income tax itself (IRP) | Tax on income |
| Drawings / personal withdrawals | Not an expense |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Apportionment

- **Home office apportionment** — Calculate the proportion of the home used for business (dedicated room / floor area). Apply that percentage to rent, electricity, water, internet directly related to the activity, with legal invoices. A dual-use space does not qualify cleanly. Conservative default: 0% deduction until reviewer confirms arrangement.

### 6.2 Vehicle Business Use

- **Vehicle business use** — Only the business-use portion of fuel and running costs is deductible, supported by invoices and a usage log. Conservative default: 0% business use until log provided.

### 6.3 Phone / Internet Mixed Use

- **Phone/internet mixed use** — Business-use portion only, with a reasonable documented estimate. Conservative default: 0% deduction until business percentage confirmed.

### 6.4 1% Capped Items

- **1% capped items reviewer flag** — Confirm whether an expense falls under the 1% cap (RESIMPLE purchases, listed items 7/8/20/21/22) and recompute the cap against gross income. Flag for reviewer: Confirm item list against current Ley 6380/19 and apply the 1% gross-income ceiling.

### 6.5 Source Classification (Territorial)

- **Source classification** — For platform / cross-border payouts, confirm whether income is Paraguay-source before including. Flag for reviewer: Confirm source; foreign-source income is generally exempt.

### 6.6 RSP vs RGC Classification

- **RSP vs RGC classification** — Confirm whether income is personal services (715) or capital (716). Rental, interest, dividends and capital gains go to RGC (flat 8%); fees for services go to RSP (progressive). Flag for reviewer: Confirm category before applying any rate.

### 6.7 IPS Optional Contributions

- **IPS optional contributions** — For directors/managers/administrators, IPS contribution is optional; confirm whether the client elected to contribute.

## Section 7 -- Excel Working Paper Template

```
PARAGUAY IRP -- WORKING PAPER
Tax Year: 2025
Client: ___________________________
RUC: ___________________________
IRP Category: RSP (715) / RGC (716)
IVA-registered: Yes / No

A. RSP GROSS INCOME (Form 715, net of IVA if registered)
  A1. Client payments for services             ___________
  A2. Platform payouts (Paraguay-source only)   ___________
  A3. Other personal-services income            ___________
  A4. TOTAL RSP gross income                     ___________

B. RSP DEDUCTIBLE EXPENSES (directly related + factura legal)
  B1. Office rent                                ___________
  B2. Accountancy / legal fees                   ___________
  B3. Office supplies                            ___________
  B4. Software subscriptions                     ___________
  B5. Marketing / advertising                    ___________
  B6. Training                                   ___________
  B7. Bank charges                               ___________
  B8. Telecoms (business %)                      ___________
  B9. Travel (business purpose)                  ___________
  B10. Vehicle (business %)                      ___________
  B11. Home office (% apportioned)               ___________
  B12. 1%-capped items (apply ceiling)           ___________
  B13. Other documented expenses                 ___________
  B14. TOTAL RSP deductions                       ___________

C. RSP NET TAXABLE INCOME (renta neta) (A4 - B14)  ___________

D. RGC INCOME (Form 716, flat 8%)
  D1. Rental income (net)                         ___________
  D2. Interest                                    ___________
  D3. Dividends                                   ___________
  D4. Capital gains                               ___________
  D5. TOTAL RGC net income                        ___________

E. TAX COMPUTATION (pass to deterministic engine)
  E1. RSP threshold check (gross > ₲80,000,000?)  ___________
  E2. RSP tax (8%/9%/10% on C)                    ___________
  E3. RGC tax (8% on D5)                          ___________
  E4. TOTAL IRP due                               ___________

SEPARATE -- IPS (if applicable):
  Employee aporte obrero (9.0% / 11% banks)       ___________
  Employer aporte patronal (16.5% / 17% banks)    ___________

REVIEWER FLAGS:
  [ ] RUC registration confirmed?
  [ ] IRP category (RSP/RGC) confirmed?
  [ ] All income confirmed Paraguay-source?
  [ ] Every deduction has a factura legal?
  [ ] Home office / vehicle / phone business % documented?
  [ ] 1% cap applied where relevant?
  [ ] IVA excluded from income and from input-recovered expenses?
  [ ] IPS recorded separately (not as IRP deduction)?
  [ ] Gross-income threshold (₲80,000,000) checked?
```

## Section 8 -- Bank Statement Reading Guide

### Paraguayan Bank Statement Formats

**Paraguayan Bank Statement Formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Banco Itaú Paraguay | PDF, Excel | Fecha, Descripción, Débito, Crédito, Saldo | Most common; Spanish; date DD/MM/AAAA |
| Banco Continental | PDF | Fecha, Concepto, Importe, Saldo | Counterparty in concept field |
| Banco Nacional de Fomento (BNF) | PDF | Fecha, Detalle, Débito, Crédito | Shorter descriptions |
| Sudameris Bank | PDF, Excel | Fecha, Descripción, Monto, Saldo |  |
| Ueno / digital wallets | App export / CSV | Fecha, Contraparte, Monto, Referencia | Clean counterparty names; QR payments |

### Key Paraguayan / Spanish Banking Terms

**Key Banking Terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| TRANSFERENCIA / TRF | Transfer | Check direction for income/expense |
| DÉBITO AUTOMÁTICO | Direct debit | Regular expense (utility, subscription) |
| DEPÓSITO | Deposit | Potential income |
| EXTRACCIÓN / RETIRO | Withdrawal | Cash withdrawal -- ask what it funded |
| COMISIÓN / CARGO | Charge / fee | Bank charge (deductible if business) |
| INTERESES | Interest | RGC income (716) or bank cost |
| HONORARIOS | Professional fees | RSP income (715) if received |
| ALQUILER | Rent | RGC income if received; deductible if paid (office) |
| FACTURA | Invoice | The deduction-supporting document (factura legal) |
| IPS / APORTE | Social security contribution | Record separately |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items and any deduction lacking a factura legal as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- PARAGUAY IRP
1. Are you registered with a RUC? Which IRP obligation(s) -- 715 (RSP) and/or 716 (RGC)?
2. Is your income from personal services (RSP) or from capital -- rent/interest/dividends/gains (RGC)?
3. Is all the income Paraguay-source? Any foreign-source income?
4. Are you registered for IVA? At 10% or with 5% items?
5. Do you have legal invoices (facturas) for the expenses you want to deduct?
6. Home office: dedicated space? What % of floor area?
7. Vehicle: business use? What %? Do you keep a usage log?
8. Phone/internet: what % is business use?
9. Are you an employee/employer paying IPS? What gross salary base?
10. Was your gross personal-services income above or below ₲80,000,000 this year?
```

## Section 10 -- Reference Material

### Key Legislation and Authority References

**Key Legislation and Authority References table**

| Topic | Reference |
| --- | --- |
| IRP framework, rates, regimes | Ley N° 6380/2019 (https://www.bacn.gov.py/archivos/9332/Ley+6380.pdf) |
| RSP deduction principle | Art. 64 Ley 6380/19 |
| General deduction conditions | Arts. 14-15 Ley 6380/19 |
| Penalties / infractions | Ley N° 125/1991 (Tax Code) |
| Electronic filing | RG N° 90/2021 (Marangatú) |
| Minimum wage | Resolución MTESS N° 677/2025 |
| Authoritative individual-tax summary | PwC Paraguay (https://taxsummaries.pwc.com/paraguay/individual/taxes-on-personal-income) |
| DNIT IRP page | https://www.dnit.gov.py/en/web/portal-institucional/irp |

### Penalties (Ley N° 125/1991; Anexo RG 13/2019)

Paraguay's tax infractions: mora (late payment), contravención (formal breach), omisión de pago (underpayment), defraudación (fraud).

**Penalties table**

| Infraction | Penalty |
| --- | --- |
| Contravención (late filing / formality breach, no fiscal harm) | Single fine of ₲50,000 per Resolución General N° 1 (DNIT/SET) [Source: ultimahora.com; RG 13/19 anexo] |
| Mora (late payment of tax) | 4% up to 14% of tax owed, escalating by length of delay (Art. 171 Ley 125/1991) |
| Late-payment interest (recargo moratorio) | 0.05% per day ≈ 1.5% per month, on tax owed [Ley 125/1991] |
| Omisión de pago | Generally 50% of unpaid tax (Ley 125/1991) |
| Defraudación (fraud) | 1× to 3× the defrauded tax (Ley 125/1991) |

- **Transitional regularization regime** — An exceptional regularization regime (running to 31 Aug 2026) lets taxpayers settle obligations for periods closed up to December 2023 without moratorium interest.  _([Source: DNIT])_
- **Reform watch** — A draft new Código Tributario (MEF, Sept 2025) is in consultation but NOT enacted; the omisión/defraudación ranges above are under the current Ley 125 and subject to pending reform.  _([Source: MEF draft])_

### Test Suite

Input: RSP, gross personal-services income ₲70,000,000 (below ₲80,000,000), net ₲55,000,000.
Expected: Gross is below ₲80,000,000 → IRP not payable for the year. Filing obligations may still apply; tax due = ₲0. [PwC]

Input: RSP, net taxable income ₲120,000,000 (gross above ₲80,000,000).
Expected: First ₲50,000,000 × 8% = ₲4,000,000; next ₲70,000,000 × 9% = ₲6,300,000. Total tax = 4,000,000 + 6,300,000 = ₲10,300,000.

Input: RSP, net taxable income ₲200,000,000.
Expected: ₲4,000,000 (band 1) + ₲9,000,000 (band 2 full) + (50,000,000 × 10% = ₲5,000,000) = ₲18,000,000.

Input: RGC net income ₲40,000,000 (rental + interest).
Expected: 40,000,000 × 8% = ₲3,200,000.

Input: ₲5,000,000 expense claimed with no factura legal.
Expected: Disallow. Not deductible under Art. 64 Ley 6380/19.

Input: Employee on minimum wage ₲2,899,048, general regime.
Expected: Aporte obrero 9.0% = 2,899,048 × 0.09 = ₲260,914.32 → ₲260,914. Aporte patronal 16.5% = ₲478,343 (2,899,048 × 0.165 = 478,342.92 → ₲478,343). Combined 25.5% = ₲739,257.

Input: Bank employee, gross salary ₲10,000,000.
Expected: Employee 11% = ₲1,100,000; employer 17% = ₲1,700,000; total 28% = ₲2,800,000.

## PROHIBITIONS

- NEVER apply an IRP rate without confirming the category (RSP 715 vs RGC 716)
- NEVER apply the progressive 8%/9%/10% scale to RGC (capital) income -- RGC is a flat 8%
- NEVER apply the 8%/9%/10% brackets to gross turnover -- they apply to net income (renta neta)
- NEVER treat the ₲80,000,000 figure as a net-income bracket -- it is the gross-income payment threshold
- NEVER allow a deduction without a legal invoice (factura legal)
- NEVER apply a fixed "standard deduction %" -- there is no statutory standard deduction
- NEVER include foreign-source income without confirming Paraguay-source (territorial system)
- NEVER include IVA collected on sales in RSP income
- NEVER record IPS contributions as an IRP business deduction line
- NEVER present tax calculations as definitive -- always label as estimated and pass to the deterministic engine

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
