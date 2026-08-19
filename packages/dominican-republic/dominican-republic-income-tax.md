---
name: dominican-republic-income-tax
description: Use this skill whenever asked about Dominican Republic personal income tax (Impuesto Sobre la Renta / ISR) for self-employed individuals, independent professionals, and salaried persons. Trigger on phrases like "how much ISR do I pay", "declaración jurada", "IR-1", "IR-3", "retención de ISR", "deducible expenses Dominican Republic", "TSS contributions", "AFP", "SFS", "seguridad social", "regalía pascual", "honorarios", "RNC registration", "ITBIS interaction", "personas físicas", "self-employed tax Dominican Republic", or any question about filing or computing income tax for an individual or sole proprietor in the Dominican Republic. Also trigger when preparing or reviewing an IR-1 return, computing deductible expenses, advising on withholding on professional/technical services, or reconciling social-security (SDSS) contributions. This skill covers the progressive ISR scale, the annual exempt threshold, the IR-1/IR-3/IR-17 form structure, SDSS contributions (AFP, SFS, SRL, INFOTEP), withholding on payments to individuals, penalties, and interaction with ITBIS (VAT). ALWAYS read this skill before touching any Dominican Republic income tax work.
version: 0.1
jurisdiction: DO
tax_year: 2025
last_updated: 2026-07-13
reviewed_by: Miguel Lantigua
review_status: current
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Dominican Republic Income Tax (ISR) -- Self-Employed and Individuals

## Dominican Republic Income Tax (ISR) -- Self-Employed and Individuals Skill v0.1

> **Tier 2 (research-verified).** Figures below are sourced from PwC Worldwide Tax Summaries, the DGII, the TSS, and Dominican law-firm guidance. Where a figure could not be confirmed against a primary source it is marked **[RESEARCH GAP -- reviewer to confirm]**. A Dominican CPA (Contador Público Autorizado) must sign off before filing.

## Section 1 -- Quick Reference

**Section 1 -- Quick Reference**

| Field | Value |
| --- | --- |
| Country | Dominican Republic (República Dominicana) |
| Tax | Impuesto Sobre la Renta (ISR) -- personal income tax |
| Currency | DOP (Dominican peso, RD$) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Primary legislation | Código Tributario (Ley No. 11-92) and its regulations [Código Tributario] |
| Social security | Ley No. 87-01 (Sistema Dominicano de Seguridad Social / SDSS); Ley No. 116-80 (INFOTEP) |
| Tax authority (ISR) | Dirección General de Impuestos Internos (DGII) -- dgii.gov.do |
| Social-security authority | Tesorería de la Seguridad Social (TSS) -- tss.gob.do |
| Filing portal | DGII Oficina Virtual (OFV); TSS / SUIRPLUS for SDSS |
| Individual filing deadline | 31 March of the following year (IR-1). FY2025 due 31 March 2026 [DGII] |
| Tax system | Territorial -- residents taxed on DR-source income [PwC] |
| Validated by | Pending -- requires sign-off by a Dominican Contador Público Autorizado (CPA) |
| Validation date | Pending |
| Skill version | 0.1 |

### ISR Rate Brackets (FY2025) -- Individuals (personas físicas)

**ISR Rate Brackets (FY2025) -- Individuals (personas físicas)**  _(PwC Worldwide Tax Summaries (updated 05 Dec 2025); DGII escala salarial FY2025)_

| Annual Taxable Income (RD$) | Tax on Lower Limit | Rate on Excess | Cumulative Tax at Top of Band |
| --- | --- | --- | --- |
| 0 -- 416,220.00 | 0 | 0% (exempt) | RD$0 |
| 416,220.01 -- 624,329.00 | 0 | 15% of excess over 416,220.01 | RD$31,216 |
| 624,329.01 -- 867,123.00 | RD$31,216 | 20% of excess over 624,329.01 | RD$79,775 |
| 867,123.01 and above | RD$79,776 | 25% of excess over 867,123.01 | -- (top marginal rate 25%) |

**Arithmetic check of band bases:**
- Top of 15% band: (624,329.00 − 416,220.01) × 15% = 208,108.99 × 0.15 = RD$31,216.35 ≈ **RD$31,216** ✓
- Top of 20% band: 31,216 + (867,123.00 − 624,329.01) × 20% = 31,216 + 242,793.99 × 0.20 = 31,216 + 48,558.80 = **RD$79,774.80 ≈ RD$79,775** (DGII publishes the next-band base as RD$79,776 owing to rounding) ✓

- **Annual exempt threshold FY2025** — RD$416,220 DOP (inflation-indexed each year (up ~4.2% from FY2024's RD$399,923))  _([PwC; DGII Comunidad de Ayuda CA687])_
- **Monthly salary level at which withholding begins** — ~RD$34,685/month DOP (416,220 ÷ 12)  _([P&H Law; DGII])_
- **Top marginal ISR rate** — 25%  _([PwC; DGII])_

**[RESEARCH GAP -- reviewer to confirm]** The FY2026 scale had not been separately confirmed as published by DGII at research time. Use the FY2025 scale for income earned in calendar 2025 and re-pull the DGII escala salarial for any later filing year.

### Social-Security (SDSS) Contribution Rates -- Monthly Salary

**Social-Security (SDSS) Contribution Rates -- Monthly Salary**  _(PwC Worldwide Tax Summaries; TSS / SDSS (Ley 87-01); INFOTEP (Ley 116-80))_

| Component | Employee | Employer | Total | Statutory base / ceiling |
| --- | --- | --- | --- | --- |
| AFP -- Seguro de Vejez, Discapacidad y Sobrevivencia (pension) | 2.87% | 7.10% | 9.97% | Floor 1× / ceiling 20× minimum cotizable wage [TSS] |
| SFS -- Seguro Familiar de Salud (health) | 3.04% | 7.09% | 10.13% | Floor 1× / ceiling 10× minimum cotizable wage [TSS] |
| SRL -- Seguro de Riesgos Laborales (occupational risk) | 0.00% | ~1.20% | ~1.20% | Ceiling 4× minimum cotizable wage; employer-only [TSS] |
| **SDSS subtotal** | **5.91%** | **15.39%** | **21.30%** | -- |
| INFOTEP (vocational training levy) | 0.5% on year-end bonus only | 1.00% of payroll | -- | Separate from SDSS; collected via TSS [INFOTEP, Ley 116-80] |

**Arithmetic check of the SDSS subtotal:**
- Employee: 2.87 + 3.04 + 0.00 = **5.91%** ✓
- Employer: 7.10 + 7.09 + 1.20 = **15.39%** ✓
- Total: 9.97 + 10.13 + 1.20 = **21.30%** (= 5.91 + 15.39) ✓
- Employer cost incl. INFOTEP: 15.39 + 1.00 = **~16.39% of payroll** [PwC; RemotePeople; Contadom]

**Notes / caveats:**
- **SRL rate ~1.20% is approximate.** It is a fixed component (~1.0% for all employers) plus a variable surcharge based on the company's risk classification (Type I–IV); sources differ on the maximum variable (cited as up to 0.3%, occasionally up to 0.6%). **Confirm the specific company's assigned SRL rate from its TSS classification** rather than assuming a flat 1.20% [TSS; Contadom].
- **AFP 7.10% employer / 2.87% employee** per PwC; some payroll guides itemize small allocations to solidarity/disability/operating funds differently (e.g. splitting out a 0.4% solidarity fund). Reconcile against current TSS technical instructions if exact sub-allocations are needed [PwC; caveat].
- INFOTEP's 0.5% employee charge is withheld from the **Christmas bonus (regalía pascual)**, not from regular salary [INFOTEP].

### SDSS Contribution Ceilings (multiplier of the minimum cotizable wage)

**SDSS Contribution Ceilings (multiplier of the minimum cotizable wage)**

| Period | Minimum cotizable wage | AFP ceiling (20×) | SFS ceiling (10×) | SRL ceiling (4×) |
| --- | --- | --- | --- | --- |
| From 1 Feb 2026 | RD$23,223/mo [TSS] | RD$464,460/mo | RD$232,230/mo | RD$92,892/mo |
| 1 Apr 2025 -- 31 Jan 2026 | RD$21,674.80/mo [TSS Res. 01-2025] | RD$433,496/mo | RD$216,748/mo | RD$86,699.20/mo |

**Arithmetic check (1 Feb 2026 base RD$23,223):** 23,223 × 20 = 464,460 ✓; × 10 = 232,230 ✓; × 4 = 92,892 ✓. (1 Apr 2025 base RD$21,674.80): × 20 = 433,496 ✓; × 10 = 216,748 ✓; × 4 = 86,699.20 ✓. Each ceiling ≥ the 1× floor. **Use the ceiling matching the contribution month** [TSS; conservative default].

> **[RESEARCH GAP -- reviewer to confirm]** Direct fetches of tss.gob.do and the official Resolution 01-2025 PDF returned 403/timeout at research time. Ceiling figures were corroborated via Acento and P&H Law citing the official TSS announcement plus PwC. A reviewer should confirm the exact DOP ceilings and effective dates against the primary TSS resolution.

### Withholding on Payments to Individuals (retención de ISR)

**Withholding on Payments to Individuals (retención de ISR)**  _(P&H Law; Decreto 139-98)_

| Payment type | Withholding rate | Authority |
| --- | --- | --- |
| Professional services / honorarios (legal, accounting, engineering, consultancy) | 10% ISR | Decreto 139-98 |
| Technical services (masonry, plumbing, carpentry, etc.) | 2% ISR | Decreto 139-98 |
| Rentals paid to individuals | 10% ISR | Decreto 139-98 |

### Conservative Defaults

**Conservative Defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residence / source of income | Treat as DR tax resident taxed on DR-source income (territorial) [PwC] |
| Unknown whether freelancer is SDSS-affiliated | Do NOT auto-apply employee SDSS deductions to a pure self-employed person (voluntary only) [TSS] |
| Unknown contribution month for SDSS ceilings | Use the ceiling set matching the contribution month (Feb-2026 set for current periods) [TSS] |
| Unknown tax year for ISR scale | Apply the FY2025 scale (exempt RD$416,220) for income earned in calendar 2025 [DGII] |
| Unknown expense category | Not deductible |
| Unknown business-use % (vehicle, phone, home) | 0% deduction |
| Unknown ITBIS registration | Assume registered if taxable supplies are made; charge 18% [DGII] |
| Unknown RNC status | Self-employed carrying on business/professional activity must register (free) [DGII] |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

- **Minimum viable inputs** — bank statement for the full tax year in CSV, PDF, or pasted text, plus confirmation of (a) residence status, (b) whether the person is salaried, self-employed, or both, and (c) RNC registration status.
- **Recommended inputs** — all sales invoices (comprobantes fiscales / NCF), purchase invoices/receipts, evidence of ISR withheld by payers (certificaciones de retención), TSS contribution records (if affiliated), prior-year IR-1 or assessment, ITBIS registration status.
- **Ideal inputs** — complete income and expenditure account, asset register with depreciation schedule, monthly IR-3/IR-17/IT-1 filings, withholding certificates, and regalía pascual records.
- **Refusal if minimum is missing** — SOFT WARN. No bank statement at all = hard stop. Bank statement without invoices = proceed with reviewer warning: "This IR-1 was produced from bank statement alone. The reviewer must verify that all deductions claimed are supported by valid fiscal receipts (NCF) and that the income is wholly DR-source business/professional income."

### Refusal Catalogue

- **R-DO-1 -- Residence / source uncertain** — "Dominican Republic uses a territorial system, and the taxation of foreign-source income depends on residence facts and the 3-year rule for newly-resident individuals. This skill cannot determine residence. Please confirm before proceeding, or escalate to a Dominican CPA."  _([PwC])_
- **R-DO-2 -- Companies / partnerships** — "This skill covers individuals and sole proprietors (personas físicas) only. Sociedades and other personas jurídicas file the IR-2 corporate return under different rules. Escalate to a Dominican CPA."
- **R-DO-3 -- Foreign-source income / expatriates** — "Foreign-source investment income of a newly-resident individual is generally only taxed from the 3rd year of residence, and treaty relief may apply. Out of scope. Escalate to a Dominican CPA."  _([PwC])_
- **R-DO-4 -- Capital gains / asset disposals** — "Capital gains computations require specialised analysis under the Código Tributario. Escalate to a Dominican CPA."
- **R-DO-5 -- Arrears / enforcement** — "Client has outstanding ISR or SDSS arrears or is subject to DGII/TSS enforcement. Surcharges of 10% (first month) + 4%/month plus 1.10%/month interest compound quickly. Do not advise. Escalate to a Dominican CPA immediately."  _([DGII])_
- **R-DO-6 -- ITBIS (VAT) return requested** — "This skill covers income tax (ISR / IR-1) only. For Dominican ITBIS, use the dominican-republic-itbis skill (Form IT-1)."

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement. Dominican statements are usually in Spanish. If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits / Créditos on Bank Statement)

**3.1 Income Patterns (Credits / Créditos on Bank Statement)**

| Pattern | IR-1 Line | Treatment | Notes |
| --- | --- | --- | --- |
| Client name + TRANSFERENCIA, DEPÓSITO, PAGO RECIBIDO, ABONO | Gross business income | Business income | If ITBIS-registered, extract net (excl. 18% ITBIS) |
| HONORARIOS, FACTURA, SERVICIOS PROFESIONALES, CONSULTORÍA | Gross business income | Professional fees | Typical for self-employed; check if 10% was withheld at source |
| STRIPE PAYOUT, PAYPAL, WISE, DLOCAL | Gross business income | Platform payout | Match to underlying invoices; net of platform fee |
| UPWORK, FIVERR, TOPTAL, DEEL | Gross business income | Freelance platform | Net of platform commission |
| NÓMINA, SALARIO, SUELDO, PAGO EMPLEADOR [name] | Employment income (separate) | Salary -- already withheld | NOT self-employment; ISR already withheld via IR-3 |
| ALQUILER RECIBIDO, RENTA RECIBIDA | Rental income | Rental income | Not business income; 10% may have been withheld |
| INTERESES, INTERÉS GANADO | Investment income | Interest income | Check withholding |
| DIVIDENDOS | Investment income | Dividend income | Subject to separate dividend rules -- flag |
| DEVOLUCIÓN DGII, REEMBOLSO ISR | EXCLUDE | Not income | Tax refund from prior year |

### 3.2 Expense Patterns (Debits / Débitos) -- Deductible Business Expenses

**3.2 Expense Patterns (Debits / Débitos) -- Deductible Business Expenses**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| ALQUILER OFICINA, RENTA LOCAL, OFFICE RENT | Office rent | Deductible | Must be backed by NCF; 10% ISR withholding obligation if paid to an individual |
| SEGURO RESPONSABILIDAD, SEGURO PROFESIONAL | Professional insurance | Deductible |  |
| CONTADOR, AUDITOR, CPA, HONORARIOS LEGALES, ABOGADO | Accountancy / legal fees | Deductible | Business-related; 10% ISR withholding if paid to an individual |
| PAPELERÍA, MATERIALES OFICINA, OFFICE DEPOT | Office supplies | Deductible |  |
| PUBLICIDAD, GOOGLE ADS, META ADS, FACEBOOK ADS | Marketing/advertising | Deductible |  |
| CAPACITACIÓN, CURSO, SEMINARIO, CONFERENCIA | Training | Deductible | Must relate to current business |
| COMISIÓN BANCARIA, CARGO BANCO, BANRESERVAS CARGO, POPULAR CARGO | Bank charges | Deductible | Business account only |
| COMISIÓN STRIPE, COMISIÓN PAYPAL | Payment processing fees | Deductible |  |
| DOMINIO, HOSTING, AWS, DIGITALOCEAN, CLOUDFLARE | IT infrastructure | Deductible | Capitalise if a long-lived asset (flag) |

### 3.3 Expense Patterns (Debits) -- SaaS and Software

**3.3 Expense Patterns (Debits) -- SaaS and Software**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| GOOGLE WORKSPACE, MICROSOFT 365, OFFICE 365 | Software subscription | Deductible | Recurring subscription = operating expense |
| ADOBE, CANVA, FIGMA, NOTION, SLACK, ZOOM | Software subscription | Deductible |  |
| ANTHROPIC, OPENAI, GITHUB, ATLASSIAN, DROPBOX | Software subscription | Deductible |  |
| LICENCIA PERPETUA SOFTWARE (high value) | Capital item | Capitalise / depreciate | Flag for reviewer; not an immediate expense |

### 3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)

**3.4 Expense Patterns (Debits) -- Utilities (may need apportionment)**

| Pattern | Category | Tier | Notes |
| --- | --- | --- | --- |
| EDESUR, EDENORTE, EDEESTE, CEPM | Electricity | T2 if home office | 100% if dedicated office; proportional if home |
| CLARO, ALTICE, VIVA, WIND TELECOM | Telecoms/broadband | T2 | Business-use portion only; default 0% if mixed |
| CAASD, INAPA, AGUA | Water | T2 if home office | Proportional if home |

### 3.5 Expense Patterns (Debits) -- Travel

**3.5 Expense Patterns (Debits) -- Travel**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| ARAJET, JETBLUE, AMERICAN, COPA, AVIANCA | Flights | Deductible if business travel | Must be wholly business purpose |
| HOTEL, BOOKING.COM, AIRBNB | Accommodation | Deductible if business travel |  |
| UBER, DIDI, CABIFY, TAXI | Local transport | Deductible if business purpose |  |
| COMBUSTIBLE, GASOLINA, GASOLINERA | Vehicle fuel | T2 -- business % only | Requires mileage log |
| PARQUEO, PEAJE | Parking / tolls | T2 -- business % only |  |

### 3.6 Expense Patterns (Debits) -- NOT Deductible

**3.6 Expense Patterns (Debits) -- NOT Deductible**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| RESTAURANTE, CENA, ALMUERZO, ENTRETENIMIENTO | Entertainment | NOT deductible | Personal/entertainment -- flag any client-meal claim for reviewer |
| PERSONAL, SUPERMERCADO, JUMBO, NACIONAL, BRAVO, LA SIRENA | Personal expenses | NOT deductible | Private living costs |
| MULTA, RECARGO, PENALIDAD | Fines/penalties | NOT deductible | Public policy |
| PAGO ISR, IMPUESTO RENTA, DGII PAGO | Tax payments | NOT deductible | Income tax cannot reduce income |
| RETIRO PERSONAL, RETIRO EFECTIVO (personal) | Drawings | NOT deductible | Not an expense |

### 3.7 Expense Patterns (Debits) -- Capital Items (depreciate)

**3.7 Expense Patterns (Debits) -- Capital Items (depreciate)**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| LAPTOP, COMPUTADORA, MACBOOK, DESKTOP | Computer hardware | Depreciate | Asset register; not an immediate expense |
| IMPRESORA, ESCÁNER, COPIADORA | Office equipment | Depreciate |  |
| MOBILIARIO, ESCRITORIO, SILLA, ARCHIVO | Furniture/fittings | Depreciate |  |
| VEHÍCULO, CARRO (business) | Motor vehicle | Depreciate | Business % only |
| AIRE ACONDICIONADO, INVERSOR | Equipment | Depreciate |  |

> **[RESEARCH GAP -- reviewer to confirm]** Specific Dominican depreciation categories and rates under the Código Tributario (Art. 287 categories I/II/III) were not in the research data set. Treat capital items as depreciable and flag the rate for the reviewer; do not invent a percentage.

### 3.8 Exclusions (Neither Income nor Expense)

**3.8 Exclusions (Neither Income nor Expense)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERENCIA PROPIA, ENTRE CUENTAS, CUENTA PROPIA | EXCLUDE | Own-account transfer |
| PAGO PRÉSTAMO, CAPITAL PRÉSTAMO | EXCLUDE | Loan principal movement |
| TSS, AFP, ARS, SEGURIDAD SOCIAL | SDSS contribution | Only if voluntarily affiliated; treat per Section 5 |
| PAGO ITBIS, IT-1 | EXCLUDE | ITBIS liability payment, not an expense |
| RETENCIÓN ISR (suffered) | Credit against ISR | Not an expense -- offsets the annual liability |

### 3.9 Dominican Banks -- Statement Format Reference

**3.9 Dominican Banks -- Statement Format Reference**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| Banreservas | TRANSFERENCIA, DÉBITO, CRÉDITO, CARGO | PDF/CSV; description holds counterparty + reference |
| Banco Popular Dominicano | TRF, PAGO, DÉBITO AUTOMÁTICO, COMISIÓN | PDF/CSV |
| BHD | TRANSFERENCIA, ACH, CARGO, ABONO | PDF/CSV |
| Scotiabank RD | PAYMENT, TRF, FEE, CARGO | PDF/CSV |
| Banco BHD / Asociación Popular (APAP) | DÉBITO, CRÉDITO, CARGO | PDF; shorter descriptions |

## Section 4 -- Worked Examples

### Example 1 -- Client Payment (ITBIS-registered, 10% withheld at source)

**Input line:**
`15/03/2025 ; BANRESERVAS TRANSFERENCIA RECIBIDA ; CONSTRUCTORA DEL CARIBE SRL ; PAGO FACT B0100000045 ; +106,200.00 ; DOP`

**Reasoning:**
Client payment for professional services. Provider is ITBIS-registered, so the gross billed was net + 18% ITBIS. If the RD$106,200 received already reflects the invoice net of any ISR withholding, confirm the certificación de retención. Assume the bank credit is the cash received and the underlying invoice net of ITBIS is the business income line.
- If RD$106,200 is **inclusive** of 18% ITBIS: net business income = 106,200 ÷ 1.18 = RD$90,000; ITBIS collected = RD$16,200 (a liability to DGII, excluded from income).

**Classification:** Business income = RD$90,000 (net of ITBIS). ITBIS RD$16,200 excluded. Note any 10% ISR withheld by the payer as a credit against the annual ISR.

### Example 2 -- SaaS Subscription (Fully Deductible)

**Input line:**
`01/04/2025 ; POPULAR DÉBITO AUTOMÁTICO ; ADOBE SYSTEMS ; CREATIVE CLOUD ABR ; -1,770.00 ; DOP`

**Reasoning:**
Monthly SaaS subscription, recurring, business use. Fully deductible operating expense. ITBIS on imported digital services may apply separately; for income tax the business cost is the net charge.

**Classification:** Deductible business expense = RD$1,770 (or net of recoverable ITBIS if registered and reclaimable).

### Example 3 -- Honorarios Paid to an Individual (Withholding obligation)

**Input line:**
`22/04/2025 ; BHD TRANSFERENCIA ; JUAN PÉREZ (abogado) ; HONORARIOS ASESORÍA ; -50,000.00 ; DOP`

**Reasoning:**
Payment for professional services to an individual. Deductible expense, but the payer has an obligation to **withhold 10% ISR** (RD$5,000) and remit it on Form IR-17 by the 10th of the following month [Decreto 139-98]. If the RD$50,000 is the net paid after withholding, gross fee = RD$55,555.56 and RD$5,555.56 withheld; if RD$50,000 is the gross fee, RD$5,000 should have been withheld and RD$45,000 paid. Confirm the contract basis.

**Classification:** Deductible expense (gross fee). Flag the 10% IR-17 withholding obligation for the reviewer.

### Example 4 -- Salary Received (Already Withheld -- not self-employment)

**Input line:**
`30/04/2025 ; POPULAR ABONO ; NÓMINA EMPRESA XYZ SRL ; SUELDO ABRIL ; +60,000.00 ; DOP`

**Reasoning:**
Employment income. The employer withholds ISR monthly via the annualized scale and reports on Form IR-3. No tax is due until annualized salary exceeds RD$416,220 (~RD$34,685/month) [P&H Law; DGII]. A purely salaried person whose wages are fully withheld generally need not file IR-1. This is NOT self-employment income.

**Classification:** Employment income (separate stream). Exclude from self-employed business income; confirm withholding via the employee's payslip.

### Example 5 -- ISR Computation for a Self-Employed Professional

**Inputs:** Self-employed consultant, DR-resident, RNC-registered. Gross professional income RD$1,200,000; deductible business expenses RD$300,000; not SDSS-affiliated.

**Reasoning:**
- Net taxable income = 1,200,000 − 300,000 = **RD$900,000**.
- RD$900,000 falls in the top band (over RD$867,123).
- ISR = base RD$79,776 + 25% × (900,000 − 867,123.01) = 79,776 + 25% × 32,876.99 = 79,776 + 8,219.25 = **RD$87,995.25**.
- If RD$30,000 of ISR was withheld at source (certificaciones de retención), ISR due on IR-1 = 87,995.25 − 30,000 = **RD$57,995.25**.

**Classification:** IR-1 net taxable income RD$900,000; ISR before credits RD$87,995.25; ISR due after withholding credit RD$57,995.25.

### Example 6 -- Internal Transfer (Exclude)

**Input line:**
`15/05/2025 ; BHD TRANSFERENCIA ; CUENTA PROPIA - AHORROS ; ; -100,000.00 ; DOP`

**Reasoning:**
Transfer between the client's own accounts. Neither income nor expense. Exclude entirely.

**Classification:** EXCLUDE.

## Section 5 -- Tier 1 Rules (When Data Is Clear)

### 5.1 Territorial System and Residence

- **Territorial system and residence** — The Dominican Republic uses a **territorial** system: residents are taxed on DR-source income. Foreign-source investment/financial income of a newly-resident individual is taxed only **from the 3rd year of residence**. Default to DR-source income unless residence facts indicate otherwise [PwC].  _(Código Tributario (Ley 11-92); PwC)_

### 5.2 The Progressive ISR Scale (FY2025)

- **Progressive ISR scale application** — Apply the Section 1 scale: 0% up to RD$416,220; 15% on 416,220–624,329; base RD$31,216 + 20% on 624,329–867,123; base RD$79,776 + 25% above 867,123. Top marginal rate 25%. The exempt threshold is inflation-indexed annually [PwC; DGII].  _(PwC; DGII)_

### 5.3 Tax Year and Filing

- **Tax year and filing** — Tax year is the calendar year ending 31 December. Individuals / sole proprietors file **Form IR-1** by **31 March** of the following year. Salaried employees with only fully-withheld wages generally need not file [DGII].  _(DGII)_

### 5.4 Employee Withholding (PAYE-style)

- **Employee withholding** — Employers withhold ISR monthly using the annualized scale (no tax until salary exceeds ~RD$34,685/month) and report on **Form IR-3 by the 10th** of the following month, even if nil [P&H Law; DGII].  _(P&H Law; DGII)_

### 5.5 Deductibility of Business Expenses

- **Deductibility of business expenses** — Expenses incurred to obtain, maintain, or conserve taxable income are deductible if supported by a valid fiscal receipt (NCF). Personal, entertainment, fines, drawings, and the income tax itself are not deductible. Mixed-use expenses must be apportioned on a reasonable, documented basis.

### 5.6 Social Security (SDSS) -- Dependent Workers

- **SDSS for dependent workers** — For salaried workers, the employer withholds the employee SDSS share (**5.91%** = 2.87% AFP + 3.04% SFS) and pays the employer share (**~15.39%** = 7.10% AFP + 7.09% SFS + ~1.20% SRL) plus **1% INFOTEP**, each subject to its component ceiling [PwC; TSS]. Use the ceiling set matching the contribution month (Section 1).  _(PwC; TSS)_

### 5.7 Self-Employed and SDSS

- **Self-employed and SDSS** — Self-employed and independent professionals are **NOT mandatorily** enrolled in SDSS (the TSS mandatory contributory regime applies to dependent workers). They may affiliate **voluntarily** to access pension (AFP) and health (ARS/SFS) benefits. Do not auto-apply employee SDSS deductions to a pure freelancer unless they have opted in [TSS Preguntas Frecuentes].  _(TSS Preguntas Frecuentes)_

### 5.8 RNC Registration

- **RNC registration** — Any person carrying on business or independent professional/commercial activity must register with DGII to obtain an **RNC** (Registro Nacional del Contribuyente). Registration is free (~25 days). There is no de-minimis turnover threshold for RNC for business activity [DGII; BizLatin Hub].  _(DGII; BizLatin Hub)_

### 5.9 Withholding on Payments to Individuals

- **Withholding on payments to individuals** — When the client **pays** an individual, withholding obligations arise: **10%** on professional services (honorarios) and rentals; **2%** on technical services; remitted on **Form IR-17 by the 10th** of the following month [Decreto 139-98; P&H Law].  _(Decreto 139-98; P&H Law)_

### 5.10 ITBIS (VAT) Interaction

**5.10 ITBIS (VAT) Interaction**

| Scenario | Income Tax Treatment |
| --- | --- |
| ITBIS collected on sales (registered) | NOT income -- exclude from business income |
| Input ITBIS recovered (registered) | NOT an expense -- exclude from deductions |
| Input ITBIS blocked/non-recoverable | IS an expense -- include gross |
| Unregistered for ITBIS | Gross amounts paid are the cost |

- **ITBIS standard rate and reverse-perception** — ITBIS standard rate is **18%** (16% reduced on certain foods). Registered persons file **Form IT-1 by the 20th** of the following month. A **18% reverse-perception** applies on operations over **RD$300,000** with unregistered/suspended-RNC providers (Norma General 06-23) [DGII; EY].  _(DGII; EY)_

### 5.11 Regalía Pascual (Christmas Bonus / 13th salary)

- **Regalía Pascual** — Mandatory: 1/12 of total ordinary salary earned in the calendar year, paid by **20 December**. The legal twelfth is **ISR-exempt**; INFOTEP takes **0.5%** from the bonus [Labor Code; INFOTEP].  _(Labor Code; INFOTEP)_

### 5.12 Filing Deadlines and Penalties

**5.12 Filing Deadlines and Penalties**

| Item | Detail |
| --- | --- |
| IR-1 (individual annual ISR) | 31 March of following year [DGII] |
| IR-3 (monthly employer ISR withheld) | 10th of each month, even if nil [DGII] |
| IR-17 (other ISR withholdings / services / rentals) | 10th of the following month [DGII] |
| IT-1 (monthly ITBIS) | 20th of the following month [DGII] |
| TSS planilla (Autodeterminación SDSS) | First working days of the following month [TSS] **[RESEARCH GAP -- reviewer to confirm exact window]** |
| Late-payment surcharge (recargo) | 10% for the first month + 4% per additional month or fraction [DGII] |
| Indemnizatory interest | 1.10% per month (or fraction) on the unpaid balance [DGII] |
| Late filing | Surcharge/interest on tax due; additional fixed fines possible under the Código Tributario [DGII] |
| Late/non-payment of SDSS (TSS) | Recargos and interest per TSS rules; collection actions and employer liability [TSS] |

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Home Office Deduction

- **Home office deduction** — - Calculate the proportion of the home used for business (dedicated room(s) as a percentage of total area). - Apply that percentage to rent, electricity (EDESUR/EDENORTE/EDEESTE), water, internet. - Must be a genuinely dedicated workspace; a dual-use room does not qualify. **Conservative default:** 0% until the reviewer confirms the arrangement. **Flag for reviewer:** confirm floor-area basis and supporting NCF.

### 6.2 Motor Vehicle Business Use

- **Motor vehicle business use** — - Only the business-use percentage of fuel, insurance, maintenance, and depreciation is deductible. - Client must maintain a mileage log (business vs total). **Conservative default:** 0% business use until a mileage log is provided. **Flag for reviewer.**

### 6.3 Phone / Internet Mixed Use

- **Phone / internet mixed use** — - Business-use portion only (CLARO/ALTICE/VIVA). Client must provide a reasonable estimate. **Conservative default:** 0% until business percentage confirmed.

### 6.4 Bad Debt Write-Off

- **Bad debt write-off** — Deductible only if income was previously declared, recovery steps were taken, and the debt is genuinely irrecoverable. Flag all three for the reviewer.

### 6.5 Depreciation of Capital Assets

- **Depreciation of capital assets** — Capital items must be depreciated over their useful life under the Código Tributario rather than expensed. **[RESEARCH GAP -- reviewer to confirm]** the applicable category and rate (Art. 287 asset categories). Do not assume a rate.

### 6.6 Voluntary SDSS Affiliation for the Self-Employed

- **Voluntary SDSS affiliation for the self-employed** — If a freelancer has voluntarily affiliated, contributions are based on a declared income and may be partly deductible. Confirm the affiliation basis, the cotizable income, and the rates actually applied with the TSS.

### 6.7 Foreign-Source Income and the 3-Year Rule

- **Foreign-source income and the 3-year rule** — For a newly-resident individual, foreign-source investment/financial income is taxed only from the 3rd year of residence. Flag the residence start date and income source for the reviewer [PwC].  _(PwC)_

## Section 7 -- Excel Working Paper Template

```
DOMINICAN REPUBLIC ISR -- IR-1 WORKING PAPER
Tax Year: 2025                    Currency: DOP (RD$)
Client: ___________________________  RNC: ______________
Residence: DR resident / Non-resident
Status: Self-employed / Salaried / Both
SDSS affiliation (self-employed): None / Voluntary

A. GROSS BUSINESS / PROFESSIONAL INCOME
  A1. Client payments (net of ITBIS if registered)   ___________
  A2. Platform payouts (Stripe, PayPal, Wise, etc.)  ___________
  A3. Other business income                           ___________
  A4. TOTAL gross income                              ___________

B. DEDUCTIBLE BUSINESS EXPENSES (NCF-supported)
  B1. Office rent                                     ___________
  B2. Professional insurance                          ___________
  B3. Accountancy / legal fees                        ___________
  B4. Office supplies                                 ___________
  B5. Software subscriptions                          ___________
  B6. Marketing / advertising                         ___________
  B7. Bank / payment processing fees                  ___________
  B8. Training                                        ___________
  B9. Travel (business)                               ___________
  B10. Telecoms (business %)                          ___________
  B11. Home office (% of utilities/rent)              ___________
  B12. Vehicle (business %)                           ___________
  B13. Depreciation (per Código Tributario)           ___________
  B14. Other allowable expenses                       ___________
  B15. TOTAL deductible expenses                      ___________

C. NET TAXABLE INCOME (A4 - B15)                      ___________

D. ISR COMPUTATION (FY2025 scale -- pass to engine)
  D1. ISR before credits                              ___________
  D2. Less: ISR withheld at source (10%/2%)           ___________
  D3. Less: provisional / other credits               ___________
  D4. ISR DUE / (refund)                              ___________

E. ITBIS (if registered -- separate IT-1)
  E1. ITBIS collected on sales (NOT income)           ___________
  E2. Input ITBIS recovered (NOT expense)             ___________

REVIEWER FLAGS:
  [ ] Residence / DR-source confirmed?
  [ ] RNC registration confirmed?
  [ ] All expenses NCF-supported?
  [ ] Home office % confirmed?
  [ ] Vehicle business % confirmed with mileage log?
  [ ] Phone/internet business % confirmed?
  [ ] Depreciation rate confirmed (RESEARCH GAP)?
  [ ] Withholding suffered reconciled to certificaciones?
  [ ] Withholding OBLIGATIONS on payments to individuals (IR-17) met?
  [ ] ITBIS excluded from income and expenses?
  [ ] SDSS only if voluntarily affiliated?
```

## Section 8 -- Bank Statement Reading Guide

### Dominican Bank Statement Formats

**Dominican Bank Statement Formats**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| Banreservas | PDF, CSV | Fecha, Descripción, Débito, Crédito, Balance | State-owned; most common |
| Banco Popular Dominicano | PDF, CSV | Fecha, Concepto, Monto, Balance | Card transactions show merchant |
| BHD | PDF, CSV | Fecha, Descripción, Cargo, Abono, Saldo | ACH transfers labelled clearly |
| Scotiabank RD | PDF, CSV | Date/Fecha, Description, Amount, Balance | Bilingual fields |
| APAP (Asociación Popular) | PDF | Fecha, Concepto, Retiro, Depósito | Shorter descriptions |

### Key Dominican Banking / Tax Terms

**Key Dominican Banking / Tax Terms**

| Term | English | Classification Hint |
| --- | --- | --- |
| TRANSFERENCIA / TRF | Transfer | Check direction for income/expense |
| DÉBITO AUTOMÁTICO | Direct debit | Regular expense (utility, subscription) |
| CARGO / COMISIÓN | Charge / fee | Bank charge (deductible) |
| ABONO / DEPÓSITO | Credit / deposit | Potential income |
| RETIRO | Withdrawal | Ask what cash was spent on |
| INTERESES | Interest | Interest income or bank charge |
| NÓMINA / SUELDO | Payroll / salary | Employment income (already withheld) |
| HONORARIOS | Professional fees | Business income (check 10% withholding) |
| NCF | Comprobante Fiscal | Fiscal receipt required to support deductions |
| RETENCIÓN | Withholding | ISR withheld at source -- credit against liability |
| ITBIS | VAT | Exclude from income/expense if registered |
| REGALÍA PASCUAL | Christmas bonus | 13th salary; legal twelfth ISR-exempt |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3).
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1).
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

```
ONBOARDING QUESTIONS -- DOMINICAN REPUBLIC ISR
1. Residence: are you a Dominican tax resident? When did residence start?
2. Income type: self-employed, salaried, or both?
3. RNC: are you registered with DGII? What is your RNC?
4. ITBIS: are you registered for ITBIS (Form IT-1)?
5. Withholding suffered: do you have certificaciones de retención (10%/2% ISR withheld by payers)?
6. Withholding obligations: did you pay any individuals for professional (10%) or technical (2%) services or rent (10%)?
7. Home office: dedicated room or shared space? If dedicated, what % of floor area?
8. Vehicle: do you use a car for business? What % is business? Do you keep a mileage log?
9. Phone/internet: what % is business use?
10. SDSS: are you voluntarily affiliated to AFP/SFS as a self-employed person?
11. Any other income (employment, rental, dividends, interest, foreign-source)?
12. Any capital assets purchased during the year?
```

## Section 10 -- Reference Material

### Key Legislation / Authority References

**Key Legislation / Authority References**

| Topic | Reference |
| --- | --- |
| Income tax (ISR) | Código Tributario (Ley No. 11-92) and regulations [DGII] |
| ISR scale FY2025 | DGII escala salarial FY2025; PwC (updated 05 Dec 2025) |
| Social security (SDSS) | Ley No. 87-01; TSS resolutions |
| SDSS ceilings | TSS Resolution 01-2025 (1 Apr 2025); updated 1 Feb 2026 [TSS] |
| INFOTEP levy | Ley No. 116-80 |
| Withholding on individuals | Decreto 139-98 |
| ITBIS standard rate / reverse-perception | DGII; Norma General 06-23 [EY] |
| Minimum wage (non-sectorized) | CNS-01-2025 [WageIndicator] |
| Penalties / surcharges | Código Tributario; DGII |

### Thresholds and Reference Figures

**Thresholds and Reference Figures**

| Item | Value | Source |
| --- | --- | --- |
| ISR annual exempt threshold (FY2025) | RD$416,220 | PwC; DGII |
| Monthly salary withholding trigger | ~RD$34,685/month | P&H Law; DGII |
| Self-employed filing requirement (IR-1) | Income > RD$416,220 or carrying on business/professional activity | DGII |
| ITBIS standard rate | 18% (16% reduced on certain foods) | DGII |
| ITBIS reverse-perception trigger (unregistered providers) | Operations > RD$300,000 (Norma General 06-23) | DGII; EY |
| Minimum cotizable wage (1 Feb 2026) | RD$23,223/month | TSS |
| Minimum cotizable wage (1 Apr 2025) | RD$21,674.80/month | TSS Res. 01-2025 |
| AFP ceiling (20×, 1 Feb 2026) | RD$464,460/month | TSS |
| SFS ceiling (10×, 1 Feb 2026) | RD$232,230/month | TSS |
| SRL ceiling (4×, 1 Feb 2026) | RD$92,892/month | TSS |
| Minimum wage -- Large enterprise (1 Apr 2025) | RD$27,988.80/month | CNS-01-2025 |
| Minimum wage -- Medium enterprise (1 Apr 2025) | RD$25,656.96/month | CNS-01-2025 |
| Minimum wage -- Small enterprise (1 Apr 2025) | RD$17,193.12/month | CNS-01-2025 |
| Minimum wage -- Micro enterprise (1 Apr 2025) | RD$15,860.32/month | CNS-01-2025 |
| Free-zone (zona franca) minimum wage (1 Jun 2025) | RD$18,871/month (rising to RD$20,875 from 1 Jun 2026) | CNS-01-2025 |

### Test Suite

Input: DR resident, gross professional income RD$1,200,000, deductible expenses RD$300,000, no SDSS, no withholding suffered.
Expected: Net taxable income RD$900,000. ISR = 79,776 + 25% × (900,000 − 867,123.01) = 79,776 + 8,219.25 = **RD$87,995.25**. ISR due RD$87,995.25 (no credits).

Input: Net taxable income RD$700,000.
Expected: ISR = 31,216 + 20% × (700,000 − 624,329.01) = 31,216 + 20% × 75,670.99 = 31,216 + 15,134.20 = **RD$46,350.20**.

Input: Net taxable income RD$500,000.
Expected: ISR = 0 + 15% × (500,000 − 416,220.01) = 15% × 83,779.99 = **RD$12,567.00** (RD$12,566.9985 rounded).

Input: Net taxable income RD$400,000.
Expected: RD$400,000 ≤ RD$416,220 exempt threshold → **ISR = RD$0**.

Input: Net taxable income RD$900,000 (ISR before credits RD$87,995.25); RD$30,000 ISR withheld at source on honorarios.
Expected: ISR due on IR-1 = 87,995.25 − 30,000 = **RD$57,995.25**.

Input: Monthly salary RD$50,000, below AFP/SFS ceilings (Feb-2026 set).
Expected: Employee deduction = 5.91% × 50,000 = **RD$2,955** (2.87% AFP = RD$1,435 + 3.04% SFS = RD$1,520). Employer cost ≈ 16.39% × 50,000 = **RD$8,195** (subject to SRL 4× ceiling check) [PwC; TSS].

Input: Gross fee RD$55,555.56 paid to an individual lawyer.
Expected: Withhold 10% = **RD$5,555.56** on Form IR-17; pay net RD$50,000.00. Expense deductible at gross RD$55,555.56.

## PROHIBITIONS

- NEVER apply the ISR scale to foreign-source income without confirming residence and the 3-year rule
- NEVER compute final ISR figures as definitive -- pass net taxable income to the deterministic engine and label outputs as estimated
- NEVER treat ITBIS collected on sales as business income
- NEVER treat recoverable input ITBIS as a deductible expense
- NEVER allow entertainment, personal expenses, fines, or the income tax itself as deductions
- NEVER auto-apply employee SDSS deductions to a pure self-employed person (voluntary only)
- NEVER mix SDSS ceiling sets across periods -- use the set matching the contribution month
- NEVER claim a deduction without a valid fiscal receipt (NCF)
- NEVER invent a depreciation rate -- it is a RESEARCH GAP for the reviewer
- NEVER forget the payer's own 10%/2% withholding obligations (IR-17) when paying individuals
- NEVER use an unverified FY2026 ISR scale for FY2025 income

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
