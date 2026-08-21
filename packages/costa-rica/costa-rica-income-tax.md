---
name: costa-rica-income-tax
description: Use this skill whenever asked about Costa Rica income tax for self-employed individuals or persons with profit-generating activity. Trigger on phrases like "how much tax do I pay in Costa Rica", "impuesto sobre la renta", "D-101", "declaración de renta", "renta del trabajo dependiente", "impuesto a las utilidades", "deducción del 25%", "Ley 10667", "trabajador independiente", "CCSS self-employed", "pagos parciales", "régimen simplificado", "TRIBU-CR", "salario base", "self-employed tax Costa Rica", "Costa Rica freelancer tax", or any question about filing or computing income tax for a self-employed Costa Rican client. Also trigger when preparing or reviewing a D-101, computing the 25% standard deduction vs documented expenses, advising on CCSS (Caja) self-employed contributions, or advising on partial-payment instalments. This skill covers the annual self-employed brackets, salaried monthly brackets, the Law 10667 25% standard deduction, CCSS contributions, family tax credits, VAT (IVA) interaction, the simplified regime, penalties, and the TRIBU-CR platform. ALWAYS read this skill before touching any Costa Rica income tax work.
version: 0.1
jurisdiction: CR
tax_year: 2026
last_updated: 2026-07-13
review_status: pending_review
depends_on: - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Costa Rica Income Tax -- Self-Employed

## Costa Rica Income Tax -- Self-Employed Skill v0.1

> **Tier 2 (research-verified).** Figures below are drawn from Big-4 / law-firm summaries (PwC, BDO, García & Bodán, EY, ICS), reputable payroll guides, the CCSS contribution scale, and reporting of the 2026 decrees. Several rates trace to secondary reporting of Decreto Ejecutivo 45333-H and the CCSS scale rather than a directly-fetched primary government page. Every figure with weak provenance or a known reconciliation issue carries an explicit **[RESEARCH GAP — reviewer to confirm]** marker. A licensed Costa Rican contador público autorizado (CPA) must sign off before filing.

## Section 1 -- Quick Reference

- **Country** — Costa Rica (República de Costa Rica, ISO CR)
- **Tax** — Impuesto sobre la Renta (income tax) — personal / self-employed
- **Currency** — CRC (Costa Rican colón, ₡)
- **Tax year** — Calendar year (1 January -- 31 December); old Oct–Sep fiscal year abolished (PwC; Alegra)  _(PwC; Alegra)_
- **Primary legislation** — Ley del Impuesto sobre la Renta No. 7092 (and reglamento)
- **Supporting legislation** — Ley No. 10667 (self-employed 25% standard deduction, eff. 1 Jan 2026); Ley No. 9635 "Fortalecimiento de las Finanzas Públicas" (IVA + capital income tax); Código de Normas y Procedimientos Tributarios No. 4755 (penalties); Ley Constitutiva de la CCSS No. 17; Decreto Ejecutivo 45333-H (2026 brackets); Decreto Ejecutivo 44772-H (2025 brackets); Decreto Ejecutivo 45303-MTSS (2026 minimum wages)
- **Tax authority** — Ministerio de Hacienda — Dirección General de Tributación (DGT)
- **Social security** — Caja Costarricense de Seguro Social (CCSS)
- **Filing portal** — TRIBU-CR (replaced ATV on 4 Aug 2025) — hacienda.go.cr
- **Filing deadline** — D-101 annual return: 15 March of the following year  _(PwC; Alegra)_
- **Tax basis** — Territorial — only Costa Rica-source income is taxable  _(Ley 7092)_
- **Validated by** — Pending — requires sign-off by a Costa Rican contador público autorizado
- **Validation date** — Pending
- **Skill version** — 0.1

**Section 1 -- Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Costa Rica (República de Costa Rica, ISO CR) |
| Tax | Impuesto sobre la Renta (income tax) — personal / self-employed |
| Currency | CRC (Costa Rican colón, ₡) |
| Tax year | Calendar year (1 January -- 31 December); old Oct–Sep fiscal year abolished (PwC; Alegra) |
| Primary legislation | Ley del Impuesto sobre la Renta No. 7092 (and reglamento) |
| Supporting legislation | Ley No. 10667 (self-employed 25% standard deduction, eff. 1 Jan 2026); Ley No. 9635 "Fortalecimiento de las Finanzas Públicas" (IVA + capital income tax); Código de Normas y Procedimientos Tributarios No. 4755 (penalties); Ley Constitutiva de la CCSS No. 17; Decreto Ejecutivo 45333-H (2026 brackets); Decreto Ejecutivo 44772-H (2025 brackets); Decreto Ejecutivo 45303-MTSS (2026 minimum wages) |
| Tax authority | Ministerio de Hacienda — Dirección General de Tributación (DGT) |
| Social security | Caja Costarricense de Seguro Social (CCSS) |
| Filing portal | TRIBU-CR (replaced ATV on 4 Aug 2025) — hacienda.go.cr |
| Filing deadline | D-101 annual return: 15 March of the following year (PwC; Alegra) |
| Tax basis | Territorial — only Costa Rica-source income is taxable (Ley 7092) |
| Validated by | Pending — requires sign-off by a Costa Rican contador público autorizado |
| Validation date | Pending |
| Skill version | 0.1 |

### Tax Rate Brackets

- **Two parallel labor-income schedules** — Costa Rica runs two parallel labor-income schedules: salaried employees are taxed on MONTHLY brackets (final withholding by the employer), while the self-employed / persons with profit-generating activity are taxed on ANNUAL brackets. Both run 0/10/15/20/25%.  _(PwC; Decreto 45333-H via García & Bodán / BDO)_

**Self-Employed / Profit-Generating Activity — Annual (impuesto a las utilidades, 2026)**  _(Decreto 45333-H; García & Bodán; Tico Times)_

| Annual Net Income (₡) | Rate | Cumulative Tax at Top of Band |
| --- | --- | --- |
| 0 -- 6,244,000 | 0% (exempt) | ₡0 |
| 6,244,000 -- 8,329,000 | 10% | ₡208,500 |
| 8,329,000 -- 10,414,000 | 15% | ₡521,250 |
| 10,414,000 -- 20,872,000 | 20% | ₡2,612,850 |
| over 20,872,000 | 25% | -- |

Cumulative check: band 2 = 2,085,000 × 10% = 208,500; band 3 = 2,085,000 × 15% = 312,750 (→521,250); band 4 = 10,458,000 × 20% = 2,091,600 (→2,612,850).

**Salaried Employees — Monthly (renta del trabajo dependiente, 2026)**  _(Decreto 45333-H via García & Bodán; PwC)_

| Monthly Gross (₡) | Rate | Cumulative Tax at Top of Band |
| --- | --- | --- |
| 0 -- 918,000 | 0% | ₡0 |
| 918,000 -- 1,347,000 | 10% | ₡42,900 |
| 1,347,000 -- 2,364,000 | 15% | ₡195,450 |
| 2,364,000 -- 4,727,000 | 20% | ₡668,050 |
| over 4,727,000 | 25% | -- |

Cumulative check: band 2 = 429,000 × 10% = 42,900; band 3 = 1,017,000 × 15% = 152,550 (→195,450); band 4 = 2,363,000 × 20% = 472,600 (→668,050).

**Self-Employed — Annual (PRIOR period 2025, governs FY2025 returns filed in 2026)**  _(PwC; Decreto 44772-H)_

| Annual Net Income (₡) | Rate | Cumulative Tax at Top of Band |
| --- | --- | --- |
| 0 -- 4,094,000 | 0% | ₡0 |
| 4,094,000 -- 6,115,000 | 10% | ₡202,100 |
| 6,115,000 -- 10,200,000 | 15% | ₡814,850 |
| 10,200,000 -- 20,442,000 | 20% | ₡2,863,250 |
| over 20,442,000 | 25% | -- |

Cumulative check: band 2 = 2,021,000 × 10% = 202,100; band 3 = 4,085,000 × 15% = 612,750 (→814,850); band 4 = 10,242,000 × 20% = 2,048,400 (→2,863,250).

[RESEARCH GAP — reviewer to confirm] The 2026 salaried (₡918k/1,347k/2,364k/4,727k) and self-employed (₡6,244k/8,329k/10,414k/20,872k) thresholds come from García & Bodán / BDO / ICS / Tico Times reporting of Decreto Ejecutivo 45333-H (published in La Gaceta 5 Dec 2025; in force 1 Jan 2026), not the decree text in La Gaceta. Note: 2026 brackets were reindexed by a -0.38% CPI deflation vs 2025 (García & Bodán; ICS), so some thresholds nudged DOWN — e.g. the self-employed top-rate floor fell from ₡20,442,000 (2025) to ₡20,872,000 only in nominal terms because of the prior-year reform; confirm direction band-by-band against La Gaceta. Caution on PwC: as of the date of writing, PwC Worldwide Tax Summaries still shows the 2025 self-employed schedule (0 / ₡4,094,000 / ₡6,115,000 / ₡10,200,000 / ₡20,442,000) under a "2026" heading — do NOT rely on the PwC page for the current self-employed thresholds; use the Decreto 45333-H figures above. Verify against La Gaceta before filing.

### Schedular & Withholding Rates (separate from labor income)

**Schedular & Withholding Rates**  _(PwC; Fonoa)_

| Item | Rate | Source |
| --- | --- | --- |
| Capital income — movable & immovable (rentas de capital, Ley 9635) | 15% | PwC |
| Dividends | 15% (lower in limited cases) | PwC |
| Capital gains | 15% (one-time 2.25% election for assets acquired before 1 Jul 2019) | PwC |
| VAT (IVA) standard rate | 13% (reduced 4% / 2% / 1%) | Fonoa; PwC |
| Non-resident remittances (remesas al exterior) | 8.5%–30% by income type (≈10% professional fees, 15% dividends, 25% salaries/pensions) | PwC |

### Family Tax Credits (2026, against computed income tax)

**Family Tax Credits**  _(García & Bodán; BDO (Decreto 45333-H))_

| Credit | Monthly | Annual | Source |
| --- | --- | --- | --- |
| Per child | ₡1,710 | ₡20,520 | García & Bodán; BDO (Decreto 45333-H) |
| Spouse | ₡2,590 | ₡31,080 | García & Bodán; BDO (Decreto 45333-H) |

Annual figures are the authoritative ones (García & Bodán; BDO both give per-child ₡20,520/yr and spouse ₡31,080/yr). The monthly spouse figure reconciles as ₡31,080 ÷ 12 = ₡2,590 exactly; some secondary sources (e.g. PwC reporting) round this to ₡2,600 — use ₡2,590 for monthly withholding to stay consistent with the annual ₡31,080. Per-child monthly ₡20,520 ÷ 12 = ₡1,710 ✓.

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Self-employed expense basis | 25% standard deduction (Law 10667) unless documented receipts clearly exceed 25% of gross — take whichever is greater |
| Income type (salaried vs self-employed) | STOP — schedule and brackets differ entirely |
| Self-employed CCSS income category | Confirm category from the CCSS Escala Contributiva; never below the minimum contributory base (BMC) |
| Source of income | Costa Rica-source only (territorial); foreign-source income generally not taxed |
| Filing platform | TRIBU-CR (ATV decommissioned 4 Aug 2025) |
| Pure salary earner — annual return | None required; monthly withholding is final |
| Unknown family-credit eligibility | Claim ₡0 until dependants confirmed |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable** — Bank statement for the full tax year (CSV, PDF, or pasted text), plus confirmation of income type (salaried vs self-employed / profit-generating activity) and the fiscal year being filed.
- **Recommended** — Sales/electronic invoices (TicoFactura / comprobantes electrónicos), purchase invoices/receipts, CCSS contribution records, prior-year D-101 or assessment, VAT (IVA) registration status, RTS (simplified regime) status, dependants for family credits.
- **Ideal** — Complete income and expenditure account, asset register, partial-payment (pago parcial) confirmations, RUT/D-140 registration detail, capital-income statements.
- **Refusal if minimum is missing -- SOFT WARN** — No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This D-101 was produced from the bank statement alone. The reviewer must verify that the 25%-deduction vs documented-expense election is correct and that all income shown is Costa Rica-source."

### Refusal Catalogue

- **R-CR-1 -- Income type unknown** — Costa Rica taxes salaried income on MONTHLY brackets (final withholding) and self-employed income on ANNUAL brackets. This skill cannot compute tax without knowing the income type. Please confirm before proceeding.  _(R-CR-1)_
- **R-CR-2 -- Companies / legal entities (personas jurídicas)** — While entities also file the D-101, corporate income tax (different deductions, minimum-tax and book-tax rules) is out of scope here. Escalate to a contador público autorizado.  _(R-CR-2)_
- **R-CR-3 -- Foreign-source income** — Costa Rica uses a territorial system — only Costa Rica-source income is taxable. Classifying whether income is CR-source can be complex (digital services, cross-border contracts). Escalate to a contador público autorizado.  _(R-CR-3)_
- **R-CR-4 -- Capital gains / capital income / property disposals** — Capital income and capital gains are a separate schedular tax under Ley 9635 (15%, with a one-time 2.25% election). Out of scope. Escalate to a contador público autorizado.  _(R-CR-4)_
- **R-CR-5 -- Arrears / TRIBU-CR migration issues** — Client has outstanding tax arrears, uncorrected legacy ATV obligations, or is subject to DGT enforcement. Late-payment charges (1%/month plus statutory interest) and migration penalties are material. Do not advise. Escalate to a contador público autorizado immediately.  _(R-CR-5)_
- **R-CR-6 -- VAT (IVA) return requested** — This skill covers income tax (D-101) only. For Costa Rica VAT (D-104), use the dedicated VAT skill.  _(R-CR-6)_
- **R-CR-7 -- CCSS exact contributory category unknown** — Self-employed CCSS is progressive by income category and subject to a minimum contributory base (BMC). Do not state a precise CCSS amount until the category is confirmed against the CCSS Escala Contributiva.  _(R-CR-7)_

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. If none match, fall through to Tier 1 rules in Section 5.

How to read this table. Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement (Spanish terms are common). If multiple patterns match, use the most specific. Amounts are in ₡ unless a foreign currency is shown.

### 3.1 Income Patterns (Credits on Bank Statement)

**Income Patterns table**

| Pattern | D-101 Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + TRANSFERENCIA, DEPOSITO, PAGO RECIBIDO, SINPE | Gross income (renta bruta) | Business income | If IVA-registered, extract net (excl. 13% IVA) |
| HONORARIOS, SERVICIOS PROFESIONALES, CONSULTORIA | Gross income | Business income | Professional fees — typical self-employed |
| STRIPE PAYOUT, STRIPE TRANSFER | Gross income | Business income | Platform payout — match to invoices; confirm CR-source |
| PAYPAL, WISE, PAYONEER PAYOUT | Gross income | Business income | International platform payout — verify CR-source |
| UPWORK, FIVERR, FREELANCER | Gross income | Business income | Net of platform commission; CR-source test |
| SALARIO, PLANILLA, EMPLEADOR [name] | EXCLUDE from D-101 | Employment income | Salary is taxed by monthly withholding, not the D-101 |
| ALQUILER RECIBIDO, RENTA INMUEBLE | Separate schedule | Capital income | Rentas de capital inmobiliario (Ley 9635) — out of D-101 utilidades unless an active rental business |
| INTERESES, DIVIDENDOS | Separate schedule | Capital income | Rentas de capital — 15% schedular |
| DEVOLUCION HACIENDA, REINTEGRO TRIBU | EXCLUDE | Not income | Tax refund from a prior period |
| SINPE MOVIL (personal) | EXCLUDE / verify | Check nature | Personal SINPE transfers are not automatically income |

### 3.2 Expense Patterns (Debits) -- Deductible (documented-expense election only)

> Only relevant if the client elects documented actual expenses over the 25% standard deduction (Law 10667). If using the 25% flat deduction, individual expenses are NOT itemised.

**Deductible Expense Patterns table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| ALQUILER OFICINA, RENTA LOCAL | Office rent | Deductible | Dedicated business premises |
| CONTADOR, AUDITOR, CPA | Accountancy fees | Deductible |  |
| ABOGADO, NOTARIO, LEGAL (business) | Legal fees | Deductible | Must be business-related |
| PAPELERIA, UTILES, OFICINA | Office supplies | Deductible |  |
| PUBLICIDAD, GOOGLE ADS, META ADS, FACEBOOK ADS | Marketing/advertising | Deductible |  |
| CAPACITACION, CURSO, SEMINARIO | Training | Deductible | Must relate to current activity |
| COMISION BANCARIA, CARGO BCR, BAC | Bank charges | Deductible | Business account only |
| COMISION STRIPE, COMISION PAYPAL | Payment processing fees | Deductible |  |
| HOSTING, DOMINIO, AWS, CLOUDFLARE | IT infrastructure | Deductible | Recurring = expense; large one-off = capital |

### 3.3 Expense Patterns (Debits) -- SaaS and Software

**SaaS and Software table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365 | Software subscription | Deductible | Recurring = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, DROPBOX | Software subscription | Deductible |  |
| LICENCIA PERPETUA (large) | Capital item | Capitalise / amortise | Above operating-expense norm — flag for reviewer |

### 3.4 Expense Patterns (Debits) -- Utilities (apportion if home office)

**Utilities table**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| ICE, CNFL, ESPH, JASEC (electricity) | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| AYA, ACUEDUCTOS (water) | Water | T2 if home office | Apportion |
| KOLBI, CLARO, MOVISTAR, LIBERTY (internet/phone) | Telecoms | T2 | Business-use portion only; default 0% if mixed |

### 3.5 Expense Patterns (Debits) -- Travel

**Travel table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| AVIANCA, COPA, SANSA, VOLARIS | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| UBER, DIDI, TAXI | Local transport | Deductible if business purpose |  |
| COMBUSTIBLE, GASOLINA, DELTA, GASOLINERA | Vehicle fuel | T2 — business % only | Requires mileage log |
| PARQUEO, ESTACIONAMIENTO | Parking | T2 — business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**NOT Deductible table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANTE, ALMUERZO, CENA, ENTRETENIMIENTO | Entertainment/meals | NOT deductible | Personal/entertainment — flag for reviewer |
| SUPERMERCADO, AUTOMERCADO, WALMART, PALI, MASXMENOS | Personal/groceries | NOT deductible | Private living costs |
| MULTA, SANCION, INFRACCION | Fines/penalties | NOT deductible | Public policy |
| IMPUESTO RENTA, PAGO HACIENDA (income tax) | Income tax payment | NOT deductible | Income tax cannot reduce income |
| RETIRO PERSONAL, CAJERO (personal) | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- CCSS, IVA, Tax (special handling)

**CCSS, IVA, Tax table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CCSS, CAJA, SEGURO SOCIAL, CUOTA OBRERO | Self-employed CCSS — deductible / mandatory | Deductible as a cost of activity for the self-employed; verify category and BMC |
| PAGO IVA, D-104 HACIENDA | EXCLUDE | VAT liability payment, not an expense |
| PAGO PARCIAL, ANTICIPO RENTA, D-103 | Credit against liability | Not an expense — credited against the D-101 |
| INS, RIESGOS DEL TRABAJO | Deductible (if employer) | Workers' comp premium |

### 3.8 Exclusions (Neither Income nor Expense)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERENCIA PROPIA, CUENTA PROPIA, ENTRE CUENTAS | EXCLUDE | Own-account transfer |
| PAGO PRESTAMO, ABONO CREDITO (principal) | EXCLUDE | Loan principal movement |
| APORTE CAPITAL, RETIRO CAPITAL | EXCLUDE | Capital movement, not income/expense |

### 3.9 Costa Rican Banks -- Statement Format Reference

**Banks Statement Format table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| BCR (Banco de Costa Rica) | TRANSFERENCIA, SINPE, DEBITO, CARGO | PDF/CSV; date DD/MM/YYYY |
| BNCR (Banco Nacional) | TRANSF, SINPE MOVIL, PAGO | PDF/CSV; counterparty in description |
| BAC Credomatic | COMPRA, TRANSFERENCIA, COMISION | CSV common; card merchant names |
| Banco Popular | TRANSFERENCIA, SINPE, DEBITO | PDF |
| Scotiabank / Davivienda / Promerica | PAGO, TRANSFERENCIA, COMISION | PDF/CSV |

SINPE / SINPE Móvil is the national real-time transfer system — direction and counterparty must be checked to classify.

## Section 4 -- Worked Examples

### Example 1 -- Client Payment (IVA-registered)

**Input line:**
`15/03/2026 ; BCR TRANSFERENCIA ENTRANTE ; ESTUDIO KREBS S.A. ; PAGO FACTURA FE-2026-003 ; +1,130,000.00 ; CRC`

**Reasoning:**
Client payment for services. Client is IVA-registered, so ₡1,130,000 includes 13% IVA. Net = 1,130,000 / 1.13 = ₡1,000,000 (gross income). The ₡130,000 is IVA collected — excluded from income (it is a liability to Hacienda).

**Classification:** Gross income = ₡1,000,000. IVA ₡130,000 excluded.

### Example 2 -- 25% Standard Deduction vs Documented Expenses (Law 10667)

**Input:** Self-employed consultant, FY2026. Gross income ₡18,000,000. Documented allowable expenses on file = ₡3,600,000.

**Reasoning (Law 10667, eff. 1 Jan 2026):** The self-employed may deduct the greater of (a) 25% of gross = 18,000,000 × 25% = ₡4,500,000, or (b) documented expenses = ₡3,600,000. The 25% flat deduction is greater, so use ₡4,500,000.

**Net income = 18,000,000 − 4,500,000 = ₡13,500,000.**

**Classification:** Use the 25% standard deduction. Net income ₡13,500,000 → carried to the bracket engine (see Example 4).

### Example 3 -- Salaried Employee Monthly Withholding (2026)

**Input:** Employee, monthly gross salary ₡2,000,000.

**Reasoning (monthly brackets):**
- 0 – 918,000 @ 0% = ₡0
- 918,000 – 1,347,000 @ 10% = 429,000 × 10% = ₡42,900
- 1,347,000 – 2,000,000 @ 15% = 653,000 × 15% = ₡97,950
- **Monthly income tax withheld = 42,900 + 97,950 = ₡140,850.**

CCSS employee deduction (2026, 10.83%) = 2,000,000 × 10.83% = ₡216,600.

**Net pay ≈ 2,000,000 − 140,850 − 216,600 = ₡1,642,550.** This is a final tax — no D-101 required for a pure salary earner.

**Classification:** Final monthly withholding ₡140,850; no annual return.

### Example 4 -- Self-Employed Annual Tax (2026)

**Input:** Net income (after 25% deduction) = ₡13,500,000 (from Example 2).

**Reasoning (annual brackets):**
- 0 – 6,244,000 @ 0% = ₡0
- 6,244,000 – 8,329,000 @ 10% = 2,085,000 × 10% = ₡208,500
- 8,329,000 – 10,414,000 @ 15% = 2,085,000 × 15% = ₡312,750
- 10,414,000 – 13,500,000 @ 20% = 3,086,000 × 20% = ₡617,200
- **Income tax before credits = 208,500 + 312,750 + 617,200 = ₡1,138,450.**

Less family credits if applicable (e.g. 2 children = 2 × ₡20,520 = ₡41,040).
**Tax after credits (2 children) = 1,138,450 − 41,040 = ₡1,097,410.**

**Classification:** D-101 tax before credits ₡1,138,450; ₡1,097,410 after a 2-child credit.

### Example 5 -- Self-Employed CCSS (progressive)

**Input line:**
`05/02/2026 ; BNCR DEBITO ; CCSS CUOTA TRABAJADOR INDEPENDIENTE ; ENERO 2026 ; -450,000.00 ; CRC`

**Reasoning:**
Self-employed CCSS is progressive by income category (combined affiliate SALUD + IVM ≈ 6.89%–18.95% of declared income, 2025 scale), subject to the minimum contributory base (BMC). It is a mandatory cost of the activity, NOT a Hacienda income-tax payment. Confirm the exact category from the CCSS Escala Contributiva before stating any precise rate.

**Classification:** CCSS contribution — deductible cost of activity (if documented-expense election); confirm category. NOT an income-tax credit.

### Example 6 -- Internal Transfer (Exclude)

**Input line:**
`20/05/2026 ; BAC TRANSFERENCIA ; CUENTA PROPIA - AHORROS ; ; -2,000,000.00 ; CRC`

**Reasoning:**
Transfer between the client's own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Territorial Basis

- **Territorial basis** — Only Costa Rica-source income is taxable, irrespective of nationality or residency. Foreign-source income of residents is generally exempt. If income source is ambiguous, STOP and escalate (R-CR-3).  _(Ley del Impuesto sobre la Renta No. 7092; PwC)_

### 5.2 Two Parallel Labor Schedules

**Two Parallel Labor Schedules table**

| Income type | Schedule | 2026 exemption | Final? |
| --- | --- | --- | --- |
| Salaried (renta del trabajo dependiente) | Monthly brackets 0/10/15/20/25% | ₡918,000/month | Yes — employer withholding is final (PwC) |
| Self-employed / utilidades | Annual brackets 0/10/15/20/25% | ₡6,244,000/year | No — annual D-101 required |

### 5.3 Law 10667 — 25% Standard Deduction (eff. 1 Jan 2026)

- **25% Standard Deduction election** — The self-employed may deduct a flat 25% of GROSS income without receipts, OR claim documented actual expenses — whichever yields the greater deduction (per-taxpayer election). Applies to professionals, technicians, personal-service providers, sales/commission and insurance agents working without an employment relationship.  _(Tico Times; Ley 10667)_

### 5.4 Revenue Recognition

- **Revenue recognition** — All Costa Rica-source business income is gross income. For IVA-registered taxpayers, report net of the 13% IVA collected. IVA collected on sales is NOT income — it is a liability to Hacienda.

### 5.5 Family Tax Credits (2026)

- **Family tax credits** — Per child ₡1,710/month (₡20,520/yr); spouse ₡2,590/month (₡31,080/yr). Applied against computed income tax. Monthly spouse = ₡31,080 ÷ 12 = ₡2,590; some secondary sources round to ₡2,600.  _(García & Bodán; BDO — Decreto 45333-H)_

### 5.6 CCSS — Employee and Employer (salaried)

**CCSS Employee and Employer table**

| Class | Year | Rate | Breakdown | Source |
| --- | --- | --- | --- | --- |
| Employee total (cuota obrera) | 2025 | **10.67%** | SEM 5.50% + IVM 4.17% + Banco Popular 1.00% | CRIE; BDO; BLP |
| Employee total (cuota obrera) | 2026 | **10.83%** | SEM 5.50% + IVM 4.33% + Banco Popular 1.00% | BDO |
| Employer (cargas sociales, incl. INS riesgos) | 2025 | **26.67%** | see breakdown below | La Nación; BDO; AG Legal |
| Employer (cargas sociales, incl. INS riesgos) | 2026 | **26.83%** | IVM rises 5.42%→5.58% (+0.16pp) | La Nación; BDO; AG Legal |

Employee column checks: 2025 = 5.50 + 4.17 + 1.00 = 10.67% ✓. 2026 = 5.50 + 4.33 + 1.00 = 10.83% ✓. No salary ceiling.

- **Employer breakdown (2026)** — SEM/health 9.25% + IVM/pension 5.58% + FODESAF (Asignaciones Familiares) 5.00% + INA 1.50% + FCL (Fondo de Capitalización Laboral, Ley 7983) 1.50% + ROP/OPC (Operadora de Pensiones Complementarias) 2.00% + IMAS 0.50% + Banco Popular patrono 0.50% (0.25% recaudación + 0.25% protección al trabajador) + INS Riesgos del Trabajo (workers' comp) 1.00% = 26.83%.  _(La Nación 2026 CCSS cargas-sociales table)_

Employer column check (2026): 9.25 + 5.58 + 5.00 + 1.50 + 1.50 + 2.00 + 0.50 + 0.50 + 1.00 = 26.83% ✓. For 2025, IVM is 5.42% (not 5.58%), so the total is 26.83 − 0.16 = 26.67% ✓. The INS Riesgos del Trabajo premium varies by activity risk class; ~1% is the common default and is the figure embedded in the headline 26.67%/26.83% totals — confirm the policy-specific rate on the INS póliza.

### 5.7 CCSS — Self-Employed (trabajador independiente)

- **CCSS self-employed structure** — Self-employed CCSS is progressive by income category, not flat, and is subject to a minimum contributory base (BMC).  _(2025 scale, CCSS Escala Contributiva AV-TI Enero 2025, E-GF-USIN-030)_

**CCSS Self-Employed Categories table**  _(CCSS Escala Contributiva AV-TI Enero 2025, E-GF-USIN-030)_

| Category | Affiliate SALUD share | Affiliate IVM share | Combined affiliate burden |
| --- | --- | --- | --- |
| Cat 1 (lowest) | 2.89% | 4.00% | ≈6.89% |
| Cat 2 | 4.33% | 5.49% | ≈9.82% |
| Cat 3 | 6.24% | 7.37% | ≈13.61% |
| Cat 4 | 8.02% | 7.82% | ≈15.84% |
| Cat 5 (highest) | 10.69% | 8.26% | ≈18.95% |

The state tops up SALUD so each category totals 12.00%; the state + LPT (Art. 78 Ley de Protección al Trabajador) top up IVM so each category totals 9.59%. Self-employed pay MORE than salaried employees — upheld by the Sala IV (Constitutional Chamber, 19 Feb 2025). (CCSS scale; ICS; Delfino.)

[RESEARCH GAP — reviewer to confirm] This is the 2025 CCSS scale. A 2026-updated scale likely exists following the Jan-2026 minimum-wage and IVM changes. The exact colón minimum contributory base (BMC) for 2025/2026 was not isolated from a CCSS authority page in research. Pull the current scale and BMC before quoting a precise contribution.

### 5.8 VAT (IVA) Interaction

**VAT Interaction table**

| Scenario | Income Tax Treatment |
| --- | --- |
| IVA collected on sales | NOT income — exclude from gross |
| Input IVA recovered | NOT an expense — exclude |
| Input IVA blocked / non-recoverable | IS an expense (documented-expense election) |
| Non-recoverable foreign VAT | IS an expense — full gross is cost |

- **IVA standard rate and registration threshold** — 13% (reduced 4%/2%/1%); no registration threshold — registration required for any habitual or incidental sale of goods/services.  _(Fonoa; PwC)_

### 5.9 Régimen de Tributación Simplificada (RTS)

- **RTS eligibility and treatment** — Small taxpayers — annual purchases ≤ 186 base salaries ≈ ₡85,969,200 (IVA-incl., 2026 simplified-regime base) and ≤ 5 employees excl. owner (Ley 10512/2024) — pay a fixed quarterly fee covering BOTH VAT and income tax via form D-105. If a client qualifies for and uses RTS, the progressive brackets above do not apply — flag for reviewer.  _(Alegra; Finube)_

### 5.10 Partial Payments (Pagos Parciales / Anticipos)

- **Partial payments** — Self-employed/businesses pay advance income-tax instalments during the year (form D-103), credited against the D-101. Typically quarterly. Not an expense — a credit against the final liability.  _(PwC; ICS)_

### 5.11 Filing Deadlines and Forms

**Filing Deadlines and Forms table**  _(Hacienda; Alegra; PwC)_

| Form | Purpose | Deadline | Via |
| --- | --- | --- | --- |
| D-101 | Annual income tax return (self-employed/individuals/entities, traditional regime) | 15 March of following year (2 months 15 days after FY close); for FY2025 the statutory 15 March 2026 is a Sunday, so Hacienda's calendar (CP-11-2026) sets the due date as Mon 16 March 2026 | TRIBU-CR |
| D-103 | Partial payments / anticipos | Quarterly | TRIBU-CR |
| D-104 | Monthly VAT (IVA) return | Within first 15 calendar days of following month | TRIBU-CR |
| D-105 | Régimen Simplificado (VAT + income tax) | Quarterly (within 15 days after quarter-end) | TRIBU-CR |
| D-151 | Annual informative return (clients/suppliers/expenses) | Generally late February for prior calendar year | TRIBU-CR |
| D-140 / RUT | Taxpayer registration before commencing activity | Before starting activity (≤10 business days) | TRIBU-CR |

All persons doing lucrative activity must file the D-101 even with zero income. (Hacienda; Alegra; PwC.)

[RESEARCH GAP — reviewer to confirm] D-104 monthly, D-151 February, and D-103 quarterly schedules are standard but TRIBU-CR (live since 4 Aug 2025) may have restated form codes/calendars. Confirm on the TRIBU-CR portal.

### 5.12 Penalties (Código de Normas y Procedimientos Tributarios No. 4755)

- **Base salary (salario base) reference 2026** — ₡462,200 (unchanged from 2025)  _(Consejo Superior del Poder Judicial, Circular 246-2025; EY; Globalex)_

**Penalties table**

| Infraction | Amount | Source |
| --- | --- | --- |
| Failure to register (Art. 78) | 0.5 base salary/month (≈₡231,100), max 3 base salaries (cap ₡1,386,600) | CNPT 4755; Hacienda |
| Late/omitted self-assessed return (Art. 79) | 0.5 base salary = ₡231,100 (reducible under Art. 88 if voluntary) | CNPT; EY |
| Failure to supply information (Art. 83) | 2% of prior-period gross income, min 3 / max 100 base salaries | CNPT 4755 |
| Late payment (morosidad, Art. 80/80 bis) | 1%/month of unpaid tax (capped) + statutory interest (DGT, revised semi-annually) | CNPT; Osa Property Mgmt |
| TRIBU-CR migration — uncorrected ATV obligations | Administrative penalties ≈ US$110–US$2,600/month of delay | EY; Tactic |

Check: 0.5 × ₡462,200 = ₡231,100 ✓; 3 × ₡462,200 = ₡1,386,600 ✓.

### 5.13 Aguinaldo (13th-Month Pay)

- **Aguinaldo** — Mandatory year-end bonus ≈ 1/12 of annual earnings (Dec–Nov), payable by 20 December, exempt from income tax and CCSS.  _(Labor Code; payroll guides)_

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 25% Standard Deduction vs Documented Expenses

- **25% vs documented expenses** — Compute both: 25% of gross vs total documented allowable expenses. Use the greater (Law 10667). Flag for reviewer: confirm documentation supports the actual-expense figure if that route is taken, and that the election is applied consistently.  _(Law 10667)_

### 6.2 Home Office Apportionment

- **Home office apportionment** — Apportion electricity (ICE/CNFL), water (AYA), internet (Kolbi/Liberty), rent by business-use proportion. Must be a dedicated workspace. Conservative default: 0% until reviewer confirms the arrangement (and only relevant under the documented-expense election).

### 6.3 Motor Vehicle Business Use

- **Motor vehicle business use** — Only the business-use percentage of fuel, insurance, maintenance is deductible; requires a mileage log. Conservative default: 0% business use until a log is provided.

### 6.4 Phone / Internet Mixed Use

- **Phone/internet mixed use** — Business-use portion only; client provides a reasonable estimate. Conservative default: 0% until confirmed.

### 6.5 Self-Employed CCSS Category & BMC

- **CCSS category and BMC** — The combined affiliate burden ranges ≈6.89%–18.95% by income category, never below the minimum contributory base. Flag for reviewer: confirm the exact category and the current-year BMC against the CCSS scale before quoting a contribution figure.

### 6.6 Income Source (Territorial Test)

- **Territorial test** — Digital/cross-border income may or may not be Costa Rica-source. Flag for reviewer: confirm CR-source classification for any platform/foreign-client income.

### 6.7 RTS Eligibility

- **RTS eligibility** — ≤186 base salaries in annual purchases and ≤5 employees — confirm eligibility and whether the fixed-fee regime is more favourable than the traditional D-101. Flag for reviewer.

### 6.8 Capital Income vs Business Income

- **Capital income vs business income** — Rental, interest, dividends may fall under the separate 15% capital-income schedule rather than utilidades. Flag for reviewer to confirm the correct schedule.

## Section 7 -- Excel Working Paper Template

```
COSTA RICA INCOME TAX -- D-101 WORKING PAPER
Tax Year: 2026 (1 Jan – 31 Dec)
Client: ___________________________
Income type: Self-employed / Profit-generating activity
Source check: All income confirmed Costa Rica-source? Y / N
Deduction election: 25% standard  /  Documented expenses

A. GROSS INCOME (renta bruta, CR-source, net of IVA)
  A1. Client payments (net of 13% IVA)           ___________
  A2. Platform payouts (Stripe, PayPal, etc.)    ___________
  A3. Other CR-source business income            ___________
  A4. TOTAL GROSS INCOME                          ___________

B. DEDUCTION (Law 10667 — greater of B1 or B2)
  B1. 25% standard deduction (A4 × 25%)           ___________
  B2. Documented allowable expenses (itemised)    ___________
  B3. DEDUCTION USED (greater of B1, B2)          ___________

C. NET INCOME (A4 - B3)                            ___________

D. TAX COMPUTATION (annual brackets — pass to engine)
  D1. Tax before credits                          ___________
  D2. Family credits (children + spouse)          ___________
  D3. Tax after credits (D1 - D2)                 ___________
  D4. Less: partial payments paid (D-103)         ___________
  D5. TAX DUE / REFUND (D3 - D4)                   ___________

E. CCSS (separate, mandatory)
  E1. Self-employed category (1–5)                ___________
  E2. Combined affiliate rate (from CCSS scale)   ___________
  E3. Annual CCSS contribution                    ___________
  E4. Confirmed ≥ minimum contributory base?      ___________

REVIEWER FLAGS:
  [ ] Income type confirmed (self-employed vs salaried)?
  [ ] All income confirmed Costa Rica-source?
  [ ] 25% vs documented-expense election optimal?
  [ ] IVA excluded from gross income?
  [ ] CCSS category + BMC confirmed against CCSS scale?
  [ ] Family credits supported by dependants?
  [ ] Partial payments (D-103) credited?
  [ ] RTS eligibility considered?
  [ ] Capital income routed to the 15% schedule, not utilidades?
  [ ] Filed via TRIBU-CR by 15 March?
```

## Section 8 -- Bank Statement Reading Guide

### Costa Rican Bank Statement Formats

**Bank Statement Formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| BCR (Banco de Costa Rica) | PDF, CSV | Fecha, Descripción, Débito, Crédito, Saldo | Most common; description has counterparty + reference |
| BNCR (Banco Nacional) | PDF, CSV | Fecha valor, Detalle, Monto, Saldo | SINPE Móvil lines frequent |
| BAC Credomatic | CSV, PDF | Fecha, Concepto, Monto, Saldo | Card merchant names shown |
| Banco Popular | PDF | Fecha, Detalle, Débito, Crédito |  |
| Scotiabank / Davivienda / Promerica | PDF, CSV | Fecha, Descripción, Monto |  |

### Key Costa Rican Banking / Tax Terms

**Key Terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| TRANSFERENCIA / TRANSF | Transfer | Check direction for income/expense |
| SINPE / SINPE MÓVIL | Real-time interbank/mobile transfer | Check counterparty + direction |
| DÉBITO / CARGO | Debit / charge | Expense — check merchant |
| CRÉDITO / DEPÓSITO | Credit / deposit | Potential income |
| HONORARIOS | Professional fees | Income (utilidades) |
| COMISIÓN | Commission / fee | Bank/processing fee (deductible) or income |
| INTERESES | Interest | Capital-income schedule (not utilidades) |
| ALQUILER | Rent | Expense, or capital-income if received |
| CCSS / CAJA | Social security | Mandatory CCSS contribution |
| IVA / D-104 | Value-added tax | Liability payment — exclude |
| PAGO PARCIAL / ANTICIPO | Partial/advance tax payment | Credit against D-101 |
| AGUINALDO | 13th-month bonus | Exempt from income tax + CCSS |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING — reviewer must confirm".
3. Apply conservative defaults (Section 1) — default to the 25% standard deduction.
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- COSTA RICA INCOME TAX
1. Income type: self-employed / profit-generating activity, or salaried employee?
2. Is ALL of your income Costa Rica-source? Any foreign-source income?
3. Are you IVA-registered? Standard 13% or a reduced rate?
4. Do you keep documented expense receipts, or prefer the 25% standard deduction?
5. Are you (or could you be) in the Régimen Simplificado (RTS)?
6. CCSS: are you registered as a trabajador independiente? Which income category?
7. Dependants: number of children and spouse for family credits?
8. Partial payments (D-103): total paid during the year?
9. Any capital income (rent, interest, dividends) — taxed on a separate 15% schedule?
10. Which fiscal year are we filing (calendar 1 Jan – 31 Dec)?
```

### Key Legislation / Authority References

**Key Legislation / Authority References**  _(Section 10 -- Reference Material)_

| Topic | Reference |
| --- | --- |
| Income tax (general) | Ley del Impuesto sobre la Renta No. 7092 + reglamento |
| 25% self-employed standard deduction | Ley No. 10667 (eff. 1 Jan 2026) |
| VAT (IVA) + capital income | Ley No. 9635 "Fortalecimiento de las Finanzas Públicas" |
| 2026 income tax brackets | Decreto Ejecutivo 45333-H |
| 2025 income tax brackets | Decreto Ejecutivo 44772-H |
| Penalties | Código de Normas y Procedimientos Tributarios No. 4755 |
| Social security | Ley Constitutiva de la CCSS No. 17; CCSS Escala Contributiva AV-TI Enero 2025 (E-GF-USIN-030) |
| Minimum wages 2026 | Decreto Ejecutivo 45303-MTSS |
| Base salary (penalties) 2026 | ₡462,200 — Consejo Superior del Poder Judicial, Circular 246-2025 |
| Filing platform | TRIBU-CR (sole platform since 4 Aug 2025; replaced ATV, TRAVI, EDDI-7, Declara7, DeclaraWeb) |
| Electronic invoicing | TicoFactura v4.4 (from 1 Sep 2025) |

### Minimum Wages 2026 (selected — Decreto 45303-MTSS; general private-sector +1.63%)

**Minimum Wages 2026 (selected — Decreto 45303-MTSS; general private-sector +1.63%)**  _(Decreto Ejecutivo 45303-MTSS)_

| Category | Rate | Source |
| --- | --- | --- |
| Unskilled day-worker (TONC) | ₡12,436.41/day | MTSS CP-051-2025; AG Legal |
| Semi-skilled (TOSC) | ₡13,523.69/day | MTSS; AG Legal |
| Skilled (TOC) | ₡13,991.86/day | MTSS; AG Legal |
| Specialized (TOE) | ₡16,244.50/day | MTSS; AG Legal |
| Bachiller Universitario | ₡664,078.07/month | MTSS; AG Legal |
| Licenciado Universitario | ₡796,921.00/month | MTSS; AG Legal |
| Domestic work (+3.96%) | ₡268,607.92/month | MTSS; AG Legal |

### Sources

- PwC Worldwide Tax Summaries — Costa Rica (Individual: taxes on personal income; other taxes), reviewed 29 Dec 2025.
- García & Bodán — "Costa Rica updates income tax brackets for 2026" (Decreto 45333-H; brackets + credits).
- BDO Costa Rica — "New income tax brackets for 2026" (confirms salaried + self-employed 2026 thresholds and credits); "Adjustment to CCSS Employer-Employee Contributions Effective January 2026" (employee 10.83%, employer 26.83%).
- ICS Costa Rica — 2026 brackets (Decreto 45333-H; -0.38% CPI reindex); self-employed social charges note.
- Tico Times — "How Costa Rica's 2026 Tax Changes Benefit Digital Nomads and Expats" (Law 10667 25% deduction).
- La Nación — "Cargas sociales suben en 2026" (full 2026 component table: employer total 26.83%, employee total 10.83%); AG Legal — "Aumento cuotas obrero patronales CCSS 2026" (employer 26.67%→26.83%).
- CCSS — Escala Contributiva AV-TI Enero 2025 (E-GF-USIN-030; La Gaceta 232/10-Dec-2024); Base Mínima Contributiva per Decreto 44756-MTSS (La Gaceta 232/10-Dec-2024).
- CRIE; BLP Legal — 2025 CCSS contribution rates (employee 10.67%).
- MTSS CP-051-2025; AG Legal — 2026 minimum wages.
- Alegra; Finube — D-101 / Régimen Simplificado guides (RTS limit 186 base salaries ≈ ₡85,969,200 IVA-incl.; ≤5 employees; D-105/D-105-2, Ley 10512/2024).
- EY — TRIBU-CR launch; salario base 2026. Poder Judicial Circular N° 246-2025 (Consejo Superior, sesión 113-2025, 16 Dec 2025) — salario base 2026 = ₡462,200 (unchanged, 6th consecutive year).
- Ministerio de Hacienda — Comunicado CP-11-2026 (FY2025 D-101 due Mon 16 Mar 2026, as 15 Mar is a Sunday); Hacienda SalariosBaseActualEHistorico.
- Fonoa — Costa Rica VAT guide.
- Ministerio de Hacienda — Infracciones y Sanciones Administrativas (Jan 2026) [PDF fetch returned 400 — confirm].

### Test Suite

Test Suite (see individual Test blocks for content).

### Test 1 -- Self-employed, 25% deduction, mid income (2026).

Input: Gross ₡18,000,000; documented expenses ₡3,600,000; no dependants.
Expected: deduction = max(4,500,000, 3,600,000) = ₡4,500,000. Net = ₡13,500,000. Tax = 208,500 + 312,750 + (3,086,000 × 20% = 617,200) = **₡1,138,450**.

### Test 2 -- Self-employed below exemption (2026).

Input: Gross ₡7,000,000; 25% deduction = ₡1,750,000; net = ₡5,250,000.
Expected: ₡5,250,000 < ₡6,244,000 → **₡0 tax** (still must file the D-101).

### Test 3 -- Salaried monthly withholding (2026).

Input: Monthly gross ₡2,000,000.
Expected: 42,900 + (653,000 × 15% = 97,950) = **₡140,850/month**, final tax; CCSS employee 10.83% = ₡216,600; net ≈ ₡1,642,550. No D-101.

### Test 4 -- Documented expenses beat 25% (2026).

Input: Gross ₡20,000,000; documented expenses ₡7,000,000 (> 25% = ₡5,000,000).
Expected: use ₡7,000,000. Net = ₡13,000,000. Tax = 208,500 + 312,750 + (2,586,000 × 20% = 517,200) = **₡1,038,450**.

### Test 5 -- Family credit applied.

Input: Net income ₡13,500,000 (Test 1), 2 children + spouse.
Expected: credit = (2 × 20,520) + 31,080 = ₡72,120. Tax after credits = 1,138,450 − 72,120 = **₡1,066,330**.

### Test 6 -- Top bracket (2026).

Input: Net income ₡25,000,000.
Expected: cumulative to ₡20,872,000 = ₡2,612,850; plus (4,128,000 × 25% = 1,032,000) = **₡3,644,850**.

### Test 7 -- 2025 self-employed (FY2025 return filed in 2026).

Input: Net income ₡12,000,000 on 2025 brackets.
Expected: cumulative to ₡10,200,000 = ₡814,850; plus (1,800,000 × 20% = 360,000) = **₡1,174,850**.

### Test 8 -- Late return penalty.

Input: Self-assessed D-101 filed late (Art. 79).
Expected: 0.5 × ₡462,200 = **₡231,100** (reducible under Art. 88 if voluntary), plus 1%/month + interest on any unpaid tax.

## PROHIBITIONS

- **Never apply annual brackets to salaried income or monthly brackets to self-employed income** — NEVER apply the annual brackets to salaried income or the monthly brackets to self-employed income — the schedules are separate.  _(Section: PROHIBITIONS)_
- **Never compute bracket tax by hand for delivery** — NEVER compute the bracket tax figures by hand for delivery — pass net income to the deterministic engine; the worked figures here are for validation only.  _(Section: PROHIBITIONS)_
- **Never tax foreign-source income** — NEVER tax foreign-source income — Costa Rica is territorial; escalate if source is unclear.  _(Section: PROHIBITIONS)_
- **Never include IVA collected on sales in gross income** — NEVER include IVA collected on sales in gross income.  _(Section: PROHIBITIONS)_
- **Never state precise self-employed CCSS amount without confirming income category and BMC** — NEVER state a precise self-employed CCSS amount without confirming the income category and the minimum contributory base (BMC) against the CCSS scale.  _(Section: PROHIBITIONS)_
- **Never itemise individual expenses when 25% standard deduction elected** — NEVER itemise individual expenses when the 25% standard deduction is elected.  _(Section: PROHIBITIONS)_
- **Never treat partial payments (D-103) or income tax itself as deductible expense** — NEVER treat partial payments (D-103) or income tax itself as a deductible expense.  _(Section: PROHIBITIONS)_
- **Never quote 2025 CCSS scale as confirmed 2026 scale** — NEVER quote the 2025 CCSS scale as if it is the confirmed 2026 scale — flag the gap.  _(Section: PROHIBITIONS)_
- **Never allow fines, penalties, or personal/living costs as deductions** — NEVER allow fines, penalties, or personal/living costs as deductions.  _(Section: PROHIBITIONS)_
- **Never present tax calculations as definitive** — NEVER present tax calculations as definitive — always label as estimated and pending CPA review.  _(Section: PROHIBITIONS)_

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
