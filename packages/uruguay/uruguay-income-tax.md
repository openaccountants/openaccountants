---
name: uruguay-income-tax
description: Use this skill whenever asked about Uruguay personal income tax (IRPF) for resident individuals, employees, and the self-employed. Trigger on phrases like "how much IRPF do I pay", "Impuesto a la Renta de las Personas Físicas", "Categoría I", "Categoría II", "rentas del trabajo", "rentas del capital", "declaración jurada IRPF", "Formulario 1102", "Formulario 1103", "núcleo familiar", "deducciones IRPF", "aportes BPS", "FONASA", "monotributo", "unipersonal", "servicios personales", "IRNR", "non-resident Uruguay tax", or any question about computing or filing income tax for a Uruguayan-resident individual. Also trigger when preparing or reviewing an IRPF annual return, computing the deduction credit, or advising on BPS social-security contributions. This skill covers the IRPF dual scheme (Category I capital income at 12% flat; Category II labour income on a 0%–36% progressive scale), the deduction-credit mechanic, BPS contributions, monotributo, filing forms/deadlines, and DGI penalties. ALWAYS read this skill before touching any Uruguay income tax work.
version: 0.1
jurisdiction: UY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on:
  - income-tax-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Uruguay Income Tax (IRPF) -- Resident Individual

## Uruguay Income Tax (IRPF) -- Resident Individual Skill v0.1

## Section 1 -- Quick Reference

**Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Uruguay (República Oriental del Uruguay) |
| Tax | IRPF -- Impuesto a la Renta de las Personas Físicas |
| Currency | UYU (Uruguayan peso, $U) only |
| Tax year | Calendar year (1 January -- 31 December) |
| Reference unit | BPC (Base de Prestaciones y Contribuciones) = UYU 6,576/month for 2025 (Decreto N° 5/025, 10 Jan 2025) |
| Tax authority (income tax) | DGI -- Dirección General Impositiva |
| Social security authority | BPS -- Banco de Previsión Social |
| Basis of taxation | Quasi-territorial -- Uruguayan-source income; limited foreign capital income for residents (PwC Tax Summaries, TY2025) |
| System | Dual / scheduler -- Category I (capital) and Category II (labour) taxed separately |
| Filing portal | DGI servicios en línea |
| Annual return forms | Formulario 1102 (individual); Formulario 1103 (núcleo familiar) (EY UY, May 2025) |
| Filing window (FY2024 filed 2025) | 7 July -- 28 August 2025, staggered by RUT/CI ending (EY UY; DGI vencimientos 2025) |
| Validated by | Pending -- requires sign-off by a Uruguayan contador público |
| Validation date | Pending |
| Skill version | 0.1 |

### IRPF Category II -- Labour Income (Rentas del Trabajo) -- Resident, Individual Filing

**Category II resident individual progressive scale**  _(PwC Tax Summaries (Uruguay, individual taxes, TY2025); brackets are BPC multiples (84/120/180/360/600/900/1,380 BPC) confirmed against BPC = UYU 6,576 and corroborated by BPS Comunicado R 2/2025.)_

| Annual taxable income (UYU) | BPC multiple | Rate | Cumulative tax at top of band (UYU) |
| --- | --- | --- | --- |
| 0 -- 552,384 | 0 -- 84 | 0% | 0.00 |
| 552,384 -- 789,120 | 84 -- 120 | 10% | 23,673.60 |
| 789,120 -- 1,183,680 | 120 -- 180 | 15% | 82,857.60 |
| 1,183,680 -- 2,367,360 | 180 -- 360 | 24% | 366,940.80 |
| 2,367,360 -- 3,945,600 | 360 -- 600 | 25% | 761,500.80 |
| 3,945,600 -- 5,918,400 | 600 -- 900 | 27% | 1,294,156.80 |
| 5,918,400 -- 9,074,880 | 900 -- 1,380 | 31% | 2,272,665.60 |
| Over 9,074,880 | > 1,380 | 36% | -- |

Progressive scale, 8 brackets, 0%–36%. Figures = annual UYU, TY2025 (BPC = UYU 6,576). Source: PwC Tax Summaries (Uruguay, individual taxes, TY2025); brackets are BPC multiples (84/120/180/360/600/900/1,380 BPC) confirmed against BPC = UYU 6,576 and corroborated by BPS Comunicado R 2/2025. Cumulative figures recomputed band-by-band (see Section 5.1).

### IRPF Category II -- Núcleo Familiar (Family-Unit Filing)

**Núcleo familiar progressive scale**  _(PwC Tax Summaries (Uruguay, individual).)_

| Annual taxable income (UYU) | BPC multiple | Rate |
| --- | --- | --- |
| 0 -- 1,104,768 | 0 -- 168 | 0% |
| 1,104,768 -- 1,183,680 | 168 -- 180 | 15% |
| 1,183,680 -- 2,367,360 | 180 -- 360 | 24% |
| 2,367,360 -- 3,945,600 | 360 -- 600 | 25% |
| 3,945,600 -- 5,918,400 | 600 -- 900 | 27% |
| 5,918,400 -- 9,074,880 | 900 -- 1,380 | 31% |
| Over 9,074,880 | > 1,380 | 36% |

Optional when all members earn ≥ 12 minimum salaries; the lowest non-taxable band roughly doubles. Note: the 10% band is collapsed in family-unit filing; income above the 0% band enters at 15% then follows the same 24%–36% scale.

### IRPF Category I -- Capital Income (Rentas del Capital)

**Category I rates**  _(PwC Tax Summaries (Uruguay, individual).)_

| Item | Rate |
| --- | --- |
| General capital income (interest, rents, royalties, capital gains) | 12% flat |
| Certain interest income (specific instruments) | 3% / 5% / 7% (item-specific) |
| Dividends | 7% |

The headline rate is a flat 12%; the reduced rates are item-specific exceptions. [RESEARCH GAP — reviewer to confirm exact instrument lists and conditions for the 3%/5%/7% interest rates against DGI / Título 7.]

### Conservative Defaults

**Conservative defaults table**

| Ambiguity | Default |
| --- | --- |
| Unknown filing unit (individual vs núcleo familiar) | Individual (Formulario 1102) |
| Unknown residency | STOP -- do not apply resident scale without confirming tax residency |
| Unknown income category | STOP -- Category I (capital) and Category II (labour) use different scales |
| Unknown deduction-credit rate (8% vs 10%) | 8% (higher-income default; less favourable to taxpayer) |
| Unknown dependent-child status | 0 children (no fictitious child deduction) |
| Unknown self-employment regime | IRPF general (servicios personales), NOT monotributo |
| Unknown business-use % (vehicle, phone, home) | 0% |

## Section 2 -- Required Inputs and Refusal Catalogue

### Required Inputs

**Minimum viable** -- confirmation of tax residency, income category (labour Category II and/or capital Category I), filing unit (individual vs núcleo familiar), and either payroll/recibos de sueldo or a bank statement for the full tax year (CSV, PDF, or pasted text).

**Recommended** -- BPS contribution records (aportes), FONASA family situation, number of dependent children (and disability status), housing rent or mortgage-interest documentation, prior-year IRPF declaración jurada.

**Ideal** -- complete income statement, full BPS aportes detail by month, prior-year Formulario 1102/1103, withholding certificates from employers (retenciones), and any IRNR / foreign-income documentation.

**Refusal if minimum is missing -- SOFT WARN.** No income data at all = hard stop. Bank statement without payroll records = proceed with reviewer warning: "This IRPF computation was produced from a bank statement alone. The reviewer must confirm that BPS aportes, FONASA family situation, and the deduction credit are correctly captured, and that nothing belongs to Category I vs Category II in error."

### Refusal Catalogue

- **R-UY-1** — Tax residency unknown. (Residency determines whether the resident IRPF scale or the non-resident IRNR regime applies. This skill cannot compute tax without confirming the client is a Uruguayan tax resident. Please confirm before proceeding.)
- **R-UY-2** — Non-resident income (IRNR). (Non-resident taxation under IRNR (general rates 7%–25%; 25% for low/no-tax jurisdiction residents) has different rules and is out of scope. Escalate to a contador público.)
- **R-UY-3** — Companies / corporate income (IRAE). (Corporate and business income under IRAE is a separate tax and is out of scope. This skill covers individuals only. Escalate to a contador público.)
- **R-UY-4** — Capital gains on real estate / complex disposals. (Property and complex capital-gains computations under Category I require specialised analysis. Escalate to a contador público.)
- **R-UY-5** — New-resident tax holiday / global mobility. (Tax-holiday elections for new residents and inbound expat planning are highly fact-specific and subject to proposed 2026 changes. Out of scope. Escalate to a contador público.)
- **R-UY-6** — IASS (pension income tax) requested. (IASS (Impuesto de Asistencia a la Seguridad Social) on pensions/retirement income is a separate tax from IRPF and is out of scope for this skill.)
- **R-UY-7** — Arrears / DGI enforcement. (Client has outstanding tax arrears or is subject to DGI enforcement. Mora and recargos compound and are severe. Do not advise. Escalate to a contador público immediately.)

## Section 3 -- Transaction Pattern Library

This is the deterministic pre-classifier. When a bank statement transaction matches a pattern below, apply the treatment directly. Do not second-guess. If none match, fall through to Tier 1 rules in Section 5.

**How to read this table.** Match by case-insensitive substring on the counterparty name or description as it appears in the bank statement (Spanish terms common in Uruguayan statements). If multiple patterns match, use the most specific. If none match, fall through to Tier 1 rules.

### 3.1 Income Patterns (Credits / Créditos)

**Income patterns table**

| Pattern | IRPF Category | Treatment | Notes |
| --- | --- | --- | --- |
| SUELDO, HABERES, NÓMINA, REMUNERACIÓN, EMPLEADOR [name] | Category II | Labour income | Employee salary -- normally withheld at source |
| HONORARIOS, FACTURA, SERVICIOS PROFESIONALES | Category II | Labour income (servicios personales) | Independent professional fees |
| AGUINALDO, SALARIO VACACIONAL | Category II | Labour income | 13th-salary / holiday salary -- taxable |
| ALQUILER COBRADO, RENTA INMUEBLE | Category I | Capital income (rents) | 12% flat band (Section 1) |
| INTERESES, INTERÉS GANADO | Category I | Capital income (interest) | 12% headline; some instruments 3%/5%/7% |
| DIVIDENDOS, UTILIDADES | Category I | Capital income (dividends) | 7% (Section 1) |
| DEVOLUCIÓN DGI, REINTEGRO IRPF | EXCLUDE | Not income | Prior-year tax refund |
| TRANSFERENCIA PROPIA, CUENTA PROPIA | EXCLUDE | Own-account transfer | Not income |

### 3.2 Deductible / Credit Items (Debits feeding the deduction credit)

The Uruguayan IRPF does NOT subtract deductions from the base; allowable deductions are summed and multiplied by the deduction rate (8% or 10%), and that credit reduces gross tax (Section 5.3). Capture these for the credit calculation, not as base reductions.

**Deductible/credit items table**

| Pattern | Category | Treatment | Notes |
| --- | --- | --- | --- |
| BPS, APORTE JUBILATORIO, MONTEPÍO | Deduction credit | Personal BPS pension contribution | 15% jubilatorio (Section 4) |
| FONASA, APORTE FONASA | Deduction credit | Personal health contribution | Rate depends on income / family (Section 4) |
| FRL, FONDO RECONVERSIÓN LABORAL | Deduction credit | 0.10% employee FRL | Component of personal aportes |
| ALQUILER VIVIENDA, ARRENDAMIENTO (housing) | Deduction credit | 6% of housing rent | Deductible item per DGI (Section 5.3) |
| HIPOTECA, INTERÉS PRÉSTAMO VIVIENDA | Deduction credit | Mortgage interest (capped) | Deductible item, capped |

### 3.3 Non-Deductible / Personal (Debits)

**Non-deductible items table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SUPERMERCADO, TIENDA INGLESA, DISCO, DEVOTO | NOT deductible | Personal groceries |
| MULTA, SANCIÓN, RECARGO | NOT deductible | Fines/penalties |
| IRPF, PAGO DGI, DECLARACIÓN JURADA | NOT deductible | Tax payment is not an expense |
| RETIRO PERSONAL, CAJERO (personal), ATM | NOT deductible | Personal drawings |

### 3.4 Exclusions (Neither Income nor Deduction)

**Exclusions table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| TRANSFERENCIA ENTRE CUENTAS, CUENTA PROPIA | EXCLUDE | Own-account transfer |
| PRÉSTAMO, CUOTA PRÉSTAMO, AMORTIZACIÓN | EXCLUDE | Loan principal movement |
| IVA, PAGO IVA | EXCLUDE | VAT liability, not income/expense |
| PAGO A CUENTA IRPF, ANTICIPO | Credit against liability | Advance/withholding -- credit, not expense |

### 3.5 Uruguayan Banks -- Statement Format Reference

**Bank statement format reference table**

| Bank | Common Patterns | Notes |
| --- | --- | --- |
| BROU (Banco República) | TRANSFERENCIA, DÉBITO, CRÉDITO, SUELDO | PDF/CSV; date format DD/MM/YYYY |
| Itaú Uruguay | TRANSF, DÉBITO AUTOMÁTICO, COMPRA | PDF/CSV; merchant in description |
| Santander Uruguay | TRANSFERENCIA, PAGO, COBRO | PDF; counterparty in description |
| BBVA Uruguay | TRANSF, DÉBITO, ABONO | PDF/CSV |
| Scotiabank Uruguay | TRANSFER, DEBIT, PAYMENT | PDF/CSV; some English labels |
| Prex / Mi Dinero (wallets) | RECARGA, PAGO, TRANSFERENCIA | CSV export; clean counterparty names |

## Section 4 -- BPS Social Security Contributions (Industria y Comercio, dependent workers, 2025)

These are NOT income tax but are deductible items feeding the IRPF deduction credit (Section 5.3) and must be captured.

### 4.1 Jubilatorio (Pension)

**Jubilatorio rates table**  _(BPS, Tasas de aportación (bps.gub.uy/835/tasas.html).)_

| Party | Rate |
| --- | --- |
| Employee (personal) | 15% |
| Employer (patronal) | 7.5% |

### 4.2 FONASA (Health) -- Employee Personal Rate

**FONASA employee rate table**  _(BPS, Tasas FONASA (bps.gub.uy/10314/tasas-fonasa.html).)_

| Monthly income | Family situation | Employee rate |
| --- | --- | --- |
| ≤ 2.5 BPC | single, no children | 3% |
| ≤ 2.5 BPC | single, with children | 3% |
| ≤ 2.5 BPC | with spouse (no SNIS cover), ± children | 5% |
| > 2.5 BPC | single, no children | 4.5% |
| > 2.5 BPC | single, with children | 6% |
| > 2.5 BPC | with spouse, no children | 6.5% |
| > 2.5 BPC | with spouse, with children | 8% |

- **Employer FONASA rate** — 5% (plus Complemento de Cuota Mutual where applicable)  _(BPS, Tasas FONASA (bps.gub.uy/10314/tasas-fonasa.html).)_
- **2.5 BPC monthly threshold value** — UYU 16,440/month UYU (at BPC 6,576)  _(BPS, Tasas FONASA (bps.gub.uy/10314/tasas-fonasa.html).)_

### 4.3 Other BPS Funds

**Other BPS funds table**  _(BPS, Tasas de aportación (bps.gub.uy/835/tasas.html).)_

| Fund | Employee | Employer |
| --- | --- | --- |
| FRL (Fondo de Reconversión Laboral) | 0.10% | 0.10% |
| FGCL (Fondo de Garantía de Créditos Laborales) | -- | 0.025% |

[RESEARCH GAP — reviewer to confirm the exact FRL employee/employer split and the FGCL 0.025% against the BPS official tasas page; secondary guides vary.]

### 4.4 Approximate Totals (Industria y Comercio)

**Approximate totals table**

| Party | Component breakdown | Approx. total |
| --- | --- | --- |
| Employee (personal) | 15% jubilatorio + 3%–8% FONASA + 0.10% FRL | 18.10% – 23.10% |
| Employer (patronal) | 7.5% jubilatorio + 5% FONASA + 0.10% FRL + 0.025% FGCL | 12.625% |

Employee total range arithmetic: minimum = 15 + 3 + 0.10 = 18.10%; maximum = 15 + 8 + 0.10 = 23.10%. Employer total = 7.5 + 5 + 0.10 + 0.025 = 12.625%. Employer figure excludes BSE (accident insurance), which varies by activity. Sources: BPS tasas pages above; aggregation corroborated by secondary calculators (calculame.uy). [RESEARCH GAP — reviewer to confirm employee FRL inclusion and BSE rate by activity.]

### 4.5 Contribution Ceiling (Tope Jubilatorio) 2025

**Contribution ceiling table**

| Item | Value |
| --- | --- |
| Max nominal monthly income subject to jubilatorio | UYU 272,564/month |
| Max personal jubilatorio contribution | UYU 40,885/month |

[RESEARCH GAP — reviewer to confirm the 2025 tope jubilatorio (UYU 272,564 income / UYU 40,885 contribution) against the BPS official ceiling table; this figure was found only in a secondary calculator (misalario.uy) and must be re-verified before reliance.]

### 4.6 Minimum Wage

- **Salario Mínimo Nacional 2025** — UYU 23,604/month UYU (effective 1 Jan 2025 (+6%); used as reference for the '12 minimum salaries' núcleo-familiar eligibility test)  _(MTSS (gub.uy/ministerio-trabajo-seguridad-social))_

### 5.1 Category II Progressive Tax -- Cumulative Computation

**Cumulative computation table**  _(PwC Tax Summaries; band widths from BPC multiples.)_

| Band top (UYU) | Band rate | Band width (UYU) | Tax on band (UYU) | Cumulative (UYU) |
| --- | --- | --- | --- | --- |
| 552,384 | 0% | 552,384 | 0.00 | 0.00 |
| 789,120 | 10% | 236,736 | 23,673.60 | 23,673.60 |
| 1,183,680 | 15% | 394,560 | 59,184.00 | 82,857.60 |
| 2,367,360 | 24% | 1,183,680 | 284,083.20 | 366,940.80 |
| 3,945,600 | 25% | 1,578,240 | 394,560.00 | 761,500.80 |
| 5,918,400 | 27% | 1,972,800 | 532,656.00 | 1,294,156.80 |
| 9,074,880 | 31% | 3,156,480 | 978,508.80 | 2,272,665.60 |
| above | 36% | -- | -- | -- |

- **Band tax computation formula** — tax = cumulative-at-previous-band-top + (X − previous-band-top) × band-n-rate  _(PwC Tax Summaries; band widths from BPC multiples.)_

### 5.2 Category I Capital Income

- **Category I taxed separately** — Capital income is taxed separately at a flat 12% (with item-specific 3%/5%/7% interest rates and 7% dividends per Section 1). It is NOT pooled with Category II labour income.  _(PwC Tax Summaries.)_

### 5.3 The Deduction Credit Mechanic (Key Uruguayan Specificity)

- **Deduction credit mechanic** — Uruguayan IRPF does NOT subtract deductions from the taxable base. Instead: 1. Sum all allowable deductions (personal BPS, FONASA, FRL, fictitious child deduction, 6% of housing rent, capped mortgage interest). 2. Multiply that sum by the deduction rate: 10% if annual labour income ≤ the 15 BPC/month equivalent; 8% if income above that threshold. 3. Subtract the resulting credit from the gross Category II tax (from Section 5.1).  _(certificadodeingresos.uy (unipersonal guide 2025); corroborated by etti.edu.uy.)_
- **15 BPC/month equivalent threshold** — UYU 98,640/month UYU (at BPC 6,576)  _(certificadodeingresos.uy (unipersonal guide 2025); corroborated by etti.edu.uy.)_

[RESEARCH GAP — reviewer to confirm the 8%/10% threshold and the exact annual mechanic against DGI; some 2025 payroll guides phrase the monthly mechanic as 14%/8%.]

### 5.4 Deductible Items (for the credit)

**Deductible items table**  _(certificadodeingresos.uy; etti.edu.uy.)_

| Item | Amount |
| --- | --- |
| Personal BPS jubilatorio contribution | Actual (15%) |
| FONASA + FRL personal contributions | Actual |
| Fictitious deduction per dependent child | 13 BPC/year (UYU 85,488 at BPC 6,576) |
| Fictitious deduction per disabled child | 26 BPC/year (UYU 170,976 at BPC 6,576) |
| Housing rent | 6% of rent paid |
| Mortgage interest | Capped (see DGI cap) |

Peso conversions are 13 BPC × 6,576 = 85,488 and 26 BPC × 6,576 = 170,976. [RESEARCH GAP — reviewer to confirm the mortgage-interest cap amount against DGI.]

### 5.5 Self-Employed / Independent Regimes

**Self-employed regimes table**  _(certificadodeingresos.uy; auren.com/uy; BPS monotributo pages (bps.gub.uy/4659, /10444, /844).)_

| Regime | Treatment |
| --- | --- |
| Servicios personales (independent professionals) | IRPF Category II base; BPS computed on 70% of billed income (real); total contribution burden ≈ 29.6%–33.1% of invoicing |
| Unipersonal owner without employees | Minimum fictitious base (ficto) = 11 BPC |
| Monotributo (micro-business simplified) | Replaces most national taxes; e.g. 8% on 1 BPC without medical coverage; replaces IRPF/IVA below revenue caps |

[RESEARCH GAP — reviewer to confirm the unipersonal ficto minimum peso value; the source's UYU 12,094 figure appears to use a prior BPC. At BPC 6,576, 11 BPC = UYU 72,336/year, but the monthly ficto base differs — re-verify against BPS aportes mínimos.]

### 5.6 Non-Resident Income (IRNR) -- Reference Only

- **IRNR rates, out of scope** — General rates 7%–25%; 25% for residents of low/no-tax jurisdictions; technical services 12% or 25%. Out of scope (see R-UY-2).  _(PwC Tax Summaries.)_

### 5.7 Filing and Payment

**Filing and payment table**  _(EY UY (May 2025); DGI vencimientos 2025; Montevideo Portal.)_

| Item | Detail |
| --- | --- |
| Forms | Formulario 1102 (individual); Formulario 1103 (núcleo familiar) |
| Filing window (FY2024 / 2025) | 7 July -- 28 August 2025, staggered by RUT/CI ending |
| Balance payment | Up to 5 equal monthly instalments; 1st on 29 Aug 2025, 5th by 30 Dec 2025 |
| Pure-wage single-employer earners | Generally NOT required to file -- employer withholds; automatic devolution |

### 5.8 Penalties (DGI)

**Penalties table**  _(DGI publicación, Resolución DGI 97/026.)_

| Item | Detail |
| --- | --- |
| Late filing of a sworn return (contravención) | Fixed fine UYU 870/return (2025); UYU 910/return (2026) -- applies even with zero balance |
| Mora (late payment) | Graduated 5% / 10% / 20% of unpaid tax (20% after ~90 days late) |
| Recargos (interest) | ~1% monthly, capitalised every 4 months; rate set periodically by DGI |

[RESEARCH GAP — reviewer to confirm the mora tiers (5/10/20%) and current recargo rate against the Código Tributario / DGI recargo calculator; the tier breakdown is from a secondary summary (memory.com.uy).]

## Section 6 -- Tier 2 Catalogue (Reviewer Judgement Required)

### 6.1 Individual vs Núcleo Familiar Election

- Núcleo familiar filing is optional and only beneficial in specific income splits; it doubles the lowest non-taxable band but collapses the 10% bracket.
- Eligibility requires all members to earn ≥ 12 minimum salaries.
- **Conservative default:** individual filing (Formulario 1102) until reviewer models both.
- **Flag for reviewer:** run both computations and elect the lower total.

### 6.2 Deduction-Credit Rate (8% vs 10%)

- The rate depends on whether annual labour income exceeds the 15 BPC/month equivalent.
- **Conservative default:** 8% (less favourable) until income level confirmed.
- **Flag for reviewer:** confirm the threshold crossing and applicable rate.

### 6.3 FONASA Family Situation

- The personal FONASA rate (3%–8%) depends on income relative to 2.5 BPC and on spouse/child coverage.
- **Conservative default:** confirm family situation before applying any rate above 3%.
- **Flag for reviewer:** confirm spouse SNIS coverage and number of covered children.

### 6.4 Dependent-Child Fictitious Deduction

- 13 BPC/child/year (26 BPC if disabled), splittable between parents.
- **Flag for reviewer:** confirm number of children, disability status, and any split with the other parent.

### 6.5 Servicios Personales vs Monotributo vs IRPF

- The optimal regime depends on revenue, whether the client has employees, and revenue caps.
- **Conservative default:** IRPF general (servicios personales).
- **Flag for reviewer:** confirm monotributo eligibility against current revenue caps.

### 6.6 Foreign Capital Income (Residents)

- Uruguay's quasi-territorial system taxes certain foreign capital income for residents.
- **Flag for reviewer:** confirm scope of any foreign interest/dividend income and available foreign-tax credits.

### 6.7 Housing Rent / Mortgage Interest Deduction

- 6% of housing rent and capped mortgage interest feed the deduction credit.
- **Flag for reviewer:** confirm documentation and the mortgage-interest cap.

## Section 7 -- Excel Working Paper Template

URUGUAY IRPF -- WORKING PAPER
Tax Year: 2025  (BPC = UYU 6,576/month)
Client: ___________________________
Filing unit: Individual (F.1102) / Núcleo Familiar (F.1103)

A. CATEGORY II -- LABOUR INCOME (annual, UYU)
  A1. Salary / haberes                            ___________
  A2. Aguinaldo / salario vacacional              ___________
  A3. Honorarios / servicios personales           ___________
  A4. TOTAL gross Category II                      ___________

B. TAXABLE BASE (Category II)
  B1. Less: items excluded from base (per DGI)     ___________
  B2. Category II taxable income                   ___________

C. GROSS CATEGORY II TAX (pass to deterministic engine, Section 5.1)
  C1. Gross tax on B2                              ___________

D. DEDUCTION CREDIT (Section 5.3)
  D1. Personal BPS jubilatorio (15%)              ___________
  D2. FONASA + FRL personal                        ___________
  D3. Fictitious child deduction (13/26 BPC each)  ___________
  D4. 6% of housing rent                           ___________
  D5. Mortgage interest (capped)                   ___________
  D6. SUM of deductions (D1..D5)                   ___________
  D7. Deduction rate (8% or 10%)                   ___________
  D8. Deduction credit (D6 x D7)                   ___________

E. CATEGORY II TAX DUE (C1 - D8, floored at 0)    ___________

F. CATEGORY I -- CAPITAL INCOME (separate)
  F1. Rents / interest / capital gains             ___________
  F2. Rate (12% / 7% / item-specific)              ___________
  F3. Category I tax                               ___________

G. CREDITS
  G1. Less: withholdings / anticipos (retenciones) ___________
  G2. TOTAL IRPF DUE / REFUND (E + F3 - G1)        ___________

REVIEWER FLAGS:
  [ ] Tax residency confirmed?
  [ ] Filing unit modelled both ways (1102 vs 1103)?
  [ ] Deduction rate (8% vs 10%) confirmed?
  [ ] FONASA family situation confirmed?
  [ ] Dependent-child deduction confirmed?
  [ ] Category I vs Category II split correct?
  [ ] Tope jubilatorio applied if income > ceiling?
  [ ] Monotributo eligibility checked (self-employed)?

## Section 8 -- Bank Statement Reading Guide

### Uruguayan Bank Statement Formats

**Bank statement formats table**

| Bank | Format | Key Fields | Notes |
| --- | --- | --- | --- |
| BROU (Banco República) | PDF, CSV | Fecha, Concepto/Detalle, Débito, Crédito, Saldo | Most common; description holds counterparty + reference |
| Itaú Uruguay | PDF, CSV | Fecha, Descripción, Importe, Saldo | Card transactions show merchant |
| Santander Uruguay | PDF | Fecha, Concepto, Débito, Crédito, Saldo | Counterparty in concepto field |
| BBVA Uruguay | PDF, CSV | Fecha, Movimiento, Importe, Saldo |  |
| Scotiabank Uruguay | PDF, CSV | Date/Fecha, Description, Amount | Some English labels |
| Prex / Mi Dinero | CSV | Fecha, Detalle, Monto | Wallet exports; clean names |

### Key Uruguayan Banking / Tax Terms

**Banking/tax terms table**

| Term | English | Classification Hint |
| --- | --- | --- |
| SUELDO / HABERES | Salary / wages | Category II income |
| HONORARIOS | Professional fees | Category II (servicios personales) |
| AGUINALDO | 13th-month salary | Category II income |
| ALQUILER | Rent | Category I if received; deduction-credit item if housing paid |
| INTERESES | Interest | Category I income |
| DIVIDENDOS / UTILIDADES | Dividends | Category I income (7%) |
| APORTE / MONTEPÍO | BPS contribution | Deduction-credit item (Box D) |
| FONASA | Health contribution | Deduction-credit item |
| DÉBITO AUTOMÁTICO | Direct debit | Regular expense -- check counterparty |
| TRANSFERENCIA | Transfer | Check direction for income/expense |
| RETENCIÓN | Withholding | Credit against IRPF liability |
| DEVOLUCIÓN DGI | Tax refund | Exclude -- not income |

## Section 9 -- Onboarding Fallback

If the client provides a bank statement but cannot answer onboarding questions immediately:

1. Classify all transactions using the pattern library (Section 3), separating Category I from Category II.
2. Mark all Tier 2 items as "PENDING -- reviewer must confirm".
3. Apply conservative defaults (Section 1) -- individual filing, 8% deduction rate, 0 children, FONASA 3% floor.
4. Generate the working paper (Section 7) with clear flags.
5. Present the following questions to the client:

ONBOARDING QUESTIONS -- URUGUAY IRPF
1. Are you a Uruguayan tax resident for the full year?
2. Filing unit: individual or núcleo familiar (and does your spouse earn >= 12 minimum salaries)?
3. Income types: salary, professional fees (honorarios), rents, interest, dividends?
4. Do you have a single employer who withholds IRPF, or multiple income sources?
5. Number of dependent children (and any with a disability)?
6. FONASA family situation: single or with spouse? Does your spouse have their own SNIS coverage?
7. Do you pay housing rent or a mortgage? Amounts?
8. Self-employed? If so: servicios personales, unipersonal, or monotributo?
9. Any foreign capital income (interest/dividends abroad)?
10. Total BPS aportes and any withholdings (retenciones) for the year?

## Section 10 -- Reference Material

### Key References

**Key references table**

| Topic | Reference |
| --- | --- |
| IRPF rates (Category I & II) | PwC Tax Summaries -- Uruguay, individual; Título 7 Texto Ordenado DGI |
| IRPF scale (official) | BPS Comunicado R 2/2025 (PDF) -- valores y escalas IRPF 2025 |
| BPC 2025 value | Decreto N° 5/025 (10 Jan 2025); BPS Comunicado R 2/2025 |
| BPS contribution rates | BPS Tasas de aportación (bps.gub.uy/835/tasas.html) |
| FONASA rates | BPS Tasas FONASA (bps.gub.uy/10314/tasas-fonasa.html) |
| Monotributo | BPS (bps.gub.uy/4659, /10444, /844) |
| Minimum wage 2025 | MTSS (gub.uy/ministerio-trabajo-seguridad-social) |
| Filing forms / deadlines | EY UY (May 2025); DGI vencimientos 2025 |
| Penalties (contravención) | DGI publicación; Resolución DGI 97/026 |
| Self-employed regimes | certificadodeingresos.uy; auren.com/uy |
| Non-resident (IRNR) | PwC Tax Summaries -- Uruguay |

### BPC Reference Values

**BPC reference values table**

| Year | BPC (UYU/month) | Source |
| --- | --- | --- |
| 2024 | 6,177 | Secondary (misalario.uy / datosUruguay) |
| 2025 | 6,576 | Decreto N° 5/025 (primary) |
| 2026 | 6,864 | Secondary (misalario.uy / datosUruguay) |

Only the 2025 value is decree-confirmed; 2024 and 2026 are secondary citations.

### Forthcoming Changes (NOT 2025-effective)

The Budget bill 2025–2029 proposes IRPF/IASS changes and stricter new-resident tax-holiday conditions from 2026. Sources: KPMG TaxNewsFlash (Oct 2025); Vialto Partners regional alert. Treat as proposals, NOT enacted 2025 law. Do not apply.

### Test Suite

Input: Resident, individual, Category II taxable income UYU 552,384.
Expected: Gross tax = 0.00 (top of 0% band).

Input: Resident, individual, Category II taxable income UYU 1,000,000.
Expected: Cumulative to 789,120 = 23,673.60; plus (1,000,000 − 789,120 = 210,880) × 15% = 31,632.00. Gross tax = 55,305.60.

Input: Category II taxable income UYU 1,500,000.
Expected: Cumulative to 1,183,680 = 82,857.60; plus (1,500,000 − 1,183,680 = 316,320) × 24% = 75,916.80. Gross tax = 158,774.40.

Input: Gross Category II tax = 55,305.60 (from Test 2); allowable deductions sum = 180,000; deduction rate = 8%.
Expected: Credit = 180,000 × 8% = 14,400.00. Tax due = 55,305.60 − 14,400.00 = 40,905.60.

Input: Rental income UYU 240,000 (Category I, general 12%).
Expected: Category I tax = 240,000 × 12% = 28,800.00. Taxed separately from Category II.

Input: Dividends UYU 100,000 (Category I).
Expected: Tax = 100,000 × 7% = 7,000.00.

Input: Núcleo familiar, combined Category II taxable income UYU 1,104,768.
Expected: Gross tax = 0.00 (top of the doubled 0% band, 168 BPC).

Input: Industria y Comercio employer rates.
Expected: 7.5% + 5% + 0.10% + 0.025% = 12.625%.

## PROHIBITIONS

- NEVER apply the resident IRPF scale without confirming tax residency
- NEVER pool Category I (capital) and Category II (labour) income -- they are taxed separately
- NEVER subtract deductions from the IRPF base -- deductions feed a credit (sum × 8% or 10%) against gross tax
- NEVER assume the 10% deduction rate -- default to 8% until the income threshold is confirmed
- NEVER apply a FONASA rate above 3% without confirming income level and family situation
- NEVER apply monotributo without confirming revenue-cap eligibility
- NEVER treat IRNR (non-resident) or IRAE (corporate) income with this skill -- escalate
- NEVER treat a BPS or FONASA payment as a base reduction -- it is a deduction-credit item
- NEVER rely on a [RESEARCH GAP] figure without reviewer confirmation
- NEVER present tax calculations as definitive -- always label as estimated

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a CPA, EA, tax attorney, contador público, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
