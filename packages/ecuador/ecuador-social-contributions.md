---
name: ecuador-social-contributions
description: Use this skill whenever asked about Ecuador social security contributions (IESS), payroll, or personal income tax (Impuesto a la Renta) for a dependent worker, employer, or self-employed/voluntary affiliate. Trigger on phrases like "how much IESS do I pay", "aporte personal IESS", "aporte patronal", "9.45% IESS", "11.15% employer contribution", "fondos de reserva", "decimo tercero", "decimo cuarto", "Ecuador payroll cost", "retencion en relacion de dependencia", "Formulario 102", "Formulario 107", "planilla IESS", "afiliado voluntario", or any question about Ecuadorian social-insurance or wage-tax obligations. Also trigger when classifying bank-statement transactions that relate to IESS debits, SRI tax payments, planilla payments, fondos de reserva, or decimos from Banco Pichincha, Banco del Pacifico, Produbanco, Banco Guayaquil, or other Ecuadorian banks. This skill covers IESS employee/employer rates and their internal breakdown, IECE/SECAP levies, fondos de reserva, the SBU minimum-wage floor, decimo tercero/cuarto, utilidades, the FY2025 and FY2026 progressive income-tax tables, filing forms and deadlines, penalties, bank-statement classification patterns, and edge cases. ALWAYS read this skill before touching any Ecuador IESS, payroll, or income-tax work.
version: 0.1
jurisdiction: EC
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - social-contributions-workflow-base
category: international
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Ecuador Social Security Contributions (IESS) and Personal Income Tax

## Ecuador Social Security Contributions (IESS) and Personal Income Tax -- Skill v0.1

> Tier 2 (research-verified). All figures carry inline citations to IESS, SRI, the Ministerio del Trabajo, or Big-4-adjacent sources. Where a figure is secondary or unconfirmed, it is marked **[RESEARCH GAP -- reviewer to confirm]**. This skill MUST be signed off by a qualified Ecuadorian professional (contador publico autorizado / abogado tributario) before filing.

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Ecuador (Republica del Ecuador) |
| Currency | USD only (Ecuador is dollarized) |
| Social-insurance authority | Instituto Ecuatoriano de Seguridad Social (IESS) -- www.iess.gob.ec |
| Tax authority | Servicio de Rentas Internas (SRI) -- www.sri.gob.ec |
| Wage / benefits authority | Ministerio del Trabajo -- www.trabajo.gob.ec |
| Social-insurance legislation | Ley de Seguridad Social |
| Labour-benefits legislation | Codigo del Trabajo (decimo tercero, decimo cuarto, fondos de reserva) |
| Income-tax legislation | Ley de Regimen Tributario Interno (LRTI) and its Reglamento |
| FY2025 income-tax table | SRI Resolution NAC-DGERCGC24-00000041 |
| FY2026 income-tax table | SRI Resolution NAC-DGERCGC25-00000043 |
| Employee IESS rate (private dependent) | 9.45% of materia gravada [misalario.ec; PwC] |
| Employer IESS base rate | 11.15% of materia gravada [misalario.ec; tagline-soluciones] |
| Employer IESS rate (PwC, incl. IECE+SECAP) | 12.15% [PwC] |
| Combined base IESS rate | 20.60% (9.45% + 11.15%) [misalario.ec] |
| Fondos de reserva | 8.33%, employer, from the 13th month of service [misalario.ec; PwC] |
| Voluntary affiliate rate | 17.60% of declared income [PwC; ecuador.unir.net] |
| Contribution floor (SBU) 2025 | USD 470/month [Ministerio del Trabajo] |
| Contribution floor (SBU) 2026 | USD 482/month [Acuerdo MDT-2025-195; nmslaw.com.ec] |
| Contribution ceiling | None for dependent workers [misalario.ec] |
| IESS payment deadline | Within 15 days after each month-end [IESS] |
| Income-tax-free fraction (FY2025) | USD 12,081 [SRI Res. NAC-DGERCGC24-00000041] |
| Income-tax-free fraction (FY2026) | USD 12,208 [SRI Res. NAC-DGERCGC25-00000043] |
| Top income-tax rate | 37% (FY2025 above USD 108,810; FY2026 above USD 109,956) [SRI] |
| Validated by | Pending -- requires sign-off by an Ecuadorian contador publico / abogado tributario |
| Validation date | Pending |

**Contribution overview (full-time private-sector dependent worker)**

| Component | Who pays | Rate | Base |
| --- | --- | --- | --- |
| IESS aporte personal | Employee (withheld) | 9.45% | Materia gravada [misalario.ec; PwC] |
| IESS aporte patronal (base) | Employer | 11.15% | Materia gravada [misalario.ec] |
| **Combined base IESS** | **Shared** | **20.60%** | **Materia gravada [misalario.ec]** |
| IECE | Employer | 0.50% | Total payroll [tagline-soluciones] |
| SECAP | Employer | 0.50% | Total payroll [tagline-soluciones] |
| Fondos de reserva | Employer | 8.33% | Remuneration, from month 13 [misalario.ec; PwC] |

> Arithmetic check: 9.45 + 11.15 = 20.60. Employer total per PwC presentation = 11.15 + 0.50 + 0.50 = 12.15 [PwC].

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown worker type | Assume private-sector dependent worker (9.45% / 11.15%) |
| Employer rate basis in cost model | Use 11.15% base; add 1.00% (IECE+SECAP) for ~12.15% per PwC -- STATE the basis used |
| Worker under 12 months' service | Do NOT include 8.33% fondos de reserva |
| Unknown remuneration | Apply SBU floor (USD 470 in 2025 / USD 482 in 2026) |
| Unknown tax year | Use FY2025 table; flag FY2026 if period falls in 2026 |
| Unknown whether decimos/utilidades are in base | EXCLUDE them -- they are NOT materia gravada [PwC] |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** -- worker type (private dependent / public / voluntary affiliate / self-employed), the tax/contribution period, and the monthly remuneration (materia gravada). Without the worker type and the period, STOP.

**Recommended** -- months of continuous service with the same employer (drives fondos de reserva eligibility), region (Coast/Galapagos vs Sierra/Amazon -- drives decimo cuarto deadline), and whether decimos are paid monthly or accumulated.

**Ideal** -- IESS planilla / aviso de entrada, Formulario 107 (annual employment-income certificate), bank statements showing IESS planilla debits and SRI tax payments, prior-year Formulario 102/102A.

### Refusal catalogue

- **R-EC-IESS-1 -- Employer rate basis not specified** — Trigger: a payroll-cost or net-pay computation where the user has not stated which employer rate to apply. Message: "The employer IESS rate is reported two ways: 11.15% (base, local Ecuadorian sources) or 12.15% (PwC, including 0.5% IECE + 0.5% SECAP). Confirm which basis the client wants before I model employer cost."
- **R-EC-IESS-2 -- Fondos de reserva on a worker under 12 months** — Trigger: request to include 8.33% fondos de reserva for a worker with under one year of continuous service. Message: "Fondos de reserva are not owed until the 13th month of continuous service with the same employer [misalario.ec]. I will not include them for a worker under 12 months without reviewer confirmation of the start date."  _(misalario.ec)_
- **R-EC-IESS-3 -- IESS mora patronal / arrears quantification** — Trigger: client has unpaid IESS contributions. Message: "Mora patronal interest accrues at the Banco Central maximum conventional rate plus 4 points, plus fines and responsabilidad patronal [IESS]. Do not quantify arrears without an IESS statement. Escalate to an Ecuadorian professional immediately."  _(IESS)_
- **R-EC-IESS-4 -- Special/disability sub-rates and the alleged extra 0.1%** — Trigger: request relying on a special disability-pension sub-rate (a secondary source mentioned an additional ~0.1%). Message: "An additional ~0.1% special disability-pension contribution is referenced by a secondary source but is NOT independently confirmed. **[RESEARCH GAP -- reviewer to confirm]** before relying on it."
- **R-EC-IESS-5 -- The 11.15% internal sub-breakdown** — Trigger: a request that depends on the exact internal allocation of the 11.15% (IVM/Salud/Riesgos/Cesantia/SSC/admin). Message: "The internal sub-breakdown comes from a secondary Ecuadorian payroll source (tagline-soluciones), not directly from the official IESS Tasas de Aportacion PDF, which could not be parsed. **[RESEARCH GAP -- reviewer to confirm]** against iess.gob.ec before publishing the sub-allocation."  _(tagline-soluciones)_

## Section 3 -- Payment pattern library

Deterministic pre-classifier for Ecuadorian bank-statement transactions. Match by case-insensitive substring on the counterparty/reference. IESS contributions and income-tax payments are statutory personal/employer obligations -- they are NOT VAT-able supplies and EXCLUDE from any IVA (VAT) return.

**How to read this table.** In Ecuador, IESS planilla debits and SRI tax payments are usually paid by the employer/taxpayer via the bank's "pago de servicios" or "convenio de debito" facility. They are outgoing (DEBIT). Inbound IESS credits are pensions or loan disbursements, not contributions.

### 3.1 IESS contribution debits (planilla)

**IESS contribution debits (planilla)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IESS, INST ECUATORIANO SEGURIDAD SOCIAL | EXCLUDE -- IESS contribution | Monthly planilla (employee + employer) |
| PLANILLA IESS, APORTES IESS | EXCLUDE -- IESS contribution | Monthly planilla reference |
| APORTE PATRONAL, APORTE PERSONAL | EXCLUDE -- IESS contribution | Explicit aporte reference |
| FONDOS DE RESERVA, FONDO RESERVA | EXCLUDE -- IESS reserve fund | 8.33% from month 13 |
| SEGURIDAD SOCIAL | EXCLUDE -- IESS contribution | Generic reference |

### 3.2 IESS debits on specific Ecuadorian banks

**IESS debits on specific Ecuadorian banks**

| Bank | Typical debit description | Treatment |
| --- | --- | --- |
| Banco Pichincha | "PAGO IESS" / "CONVENIO IESS" / "PLANILLA IESS" | EXCLUDE -- IESS |
| Banco del Pacifico | "IESS APORTES" / "SEGURIDAD SOCIAL" | EXCLUDE -- IESS |
| Produbanco | "IESS" / "PLANILLA DE APORTES" | EXCLUDE -- IESS |
| Banco Guayaquil | "PAGO IESS" / "APORTES IESS" | EXCLUDE -- IESS |
| Banco Internacional / others | "IESS" / "SEGURIDAD SOCIAL" | EXCLUDE -- IESS |

### 3.3 SRI tax payments (income tax / VAT -- NOT IESS)

**SRI tax payments (income tax / VAT -- NOT IESS)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SRI, SERVICIO DE RENTAS INTERNAS | EXCLUDE -- tax payment, not IESS | Income tax or IVA |
| IMPUESTO A LA RENTA, FORM 102 | EXCLUDE -- income tax | Not a social contribution |
| RETENCION EN LA FUENTE | EXCLUDE -- withholding remittance | PIT withheld on payroll, not IESS |
| IVA, FORMULARIO 104 | EXCLUDE -- VAT remittance | Not IESS |

### 3.4 Salary, decimos and utilidades (exclude from IESS classification)

**Salary, decimos and utilidades (exclude from IESS classification)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SUELDO, ROL DE PAGOS, NOMINA (outgoing) | EXCLUDE -- payroll expense | Wage payment, not a contribution |
| DECIMO TERCERO, DECIMO CUARTO (outgoing) | EXCLUDE -- statutory bonus | NOT materia gravada [PwC] |
| UTILIDADES (outgoing) | EXCLUDE -- profit sharing | Labour obligation, not a contribution |
| SUELDO, ROL DE PAGOS (incoming) | EXCLUDE -- employment income received | Not a contribution |

### 3.5 IESS credits received (NOT contributions)

**IESS credits received (NOT contributions)**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| IESS PENSION, JUBILACION | EXCLUDE -- pension income received | Not a contribution paid |
| PRESTAMO IESS, QUIROGRAFARIO | EXCLUDE -- IESS loan disbursement/repayment | Not a contribution |
| FONDOS DE RESERVA (incoming) | EXCLUDE -- reserve-fund withdrawal received | Not a contribution paid |

## Section 4 -- Worked examples

Six bank-statement and payroll classifications for a hypothetical Quito-based SME and its employees. All amounts in USD. Computations reconcile to the cent.

### Example 1 -- Employee IESS withholding on a USD 1,200 salary (FY2025)

**Input line:**
`31.03.2025 ; PLANILLA IESS BANCO PICHINCHA ; DEBIT ; APORTES MARZO 2025 ; -247.20 ; USD`

**Reasoning:**
Worker earns USD 1,200/month materia gravada. Employee aporte personal = 1,200 x 9.45% = USD 113.40 [misalario.ec]. Employer aporte patronal (base) = 1,200 x 11.15% = USD 133.80 [misalario.ec]. The planilla debit combines both: 113.40 + 133.80 = USD 247.20. Matches "PLANILLA IESS" (pattern 3.1/3.2). Excludes from IVA.

**Classification:** EXCLUDE -- IESS contribution (employee USD 113.40 + employer USD 133.80 = USD 247.20).

### Example 2 -- Employee net pay (FY2025, USD 1,200, no PIT)

**Input:** Monthly gross USD 1,200; annualised USD 14,400.

**Reasoning:**
- IESS employee withholding: 1,200 x 9.45% = USD 113.40.
- Pay after IESS: 1,200 - 113.40 = USD 1,086.60.
- Income tax: annual taxable base (after the IESS deduction) = (1,200 - 113.40) x 12 = 1,086.60 x 12 = USD 13,039.20. This exceeds the FY2025 tax-free fraction of USD 12,081 [SRI Res. NAC-DGERCGC24-00000041]. PIT = (13,039.20 - 12,081) x 5% = 958.20 x 5% = USD 47.91 for the year = USD 3.99/month (employer prorates via retencion en relacion de dependencia).
- Monthly net (approx) = 1,086.60 - 3.99 = **USD 1,082.61**.

> Note: the income-tax base after deducting personal expenses/IESS is simplified here; in practice the employer projects annual taxable income net of allowable personal-expense deductions. PIT figure is illustrative.

**Classification:** Net pay approx USD 1,082.61/month; employer additionally bears 11.15% (USD 133.80) + IECE/SECAP + fondos de reserva (if past month 12).

### Example 3 -- Full employer cost of a USD 1,200 worker past 12 months (FY2025)

**Reasoning (PwC basis, employer side):**
- Aporte patronal base: 1,200 x 11.15% = USD 133.80 [misalario.ec].
- IECE: 1,200 x 0.50% = USD 6.00 [tagline-soluciones].
- SECAP: 1,200 x 0.50% = USD 6.00 [tagline-soluciones].
- Fondos de reserva: 1,200 x 8.33% = USD 99.96 [misalario.ec].
- Employer statutory add-on total: 133.80 + 6.00 + 6.00 + 99.96 = **USD 245.76**.
- Total employer monthly cost (excl. decimos/utilidades): 1,200 + 245.76 = **USD 1,445.76**.

> Decimo tercero (approx 1/12 = USD 100.00) and decimo cuarto (USD 470/12 = USD 39.17 in 2025) are additional labour costs but are NOT materia gravada [PwC; ecuadorlegalonline.com].

**Classification:** Employer statutory cost USD 245.76 on top of the USD 1,200 wage (worker past 12 months).

### Example 4 -- SBU-floor minimum-wage worker (FY2026)

**Input:** Worker on the 2026 SBU of USD 482/month [Acuerdo MDT-2025-195].

**Reasoning:**
- Employee IESS: 482 x 9.45% = USD 45.55.
- Employer IESS base: 482 x 11.15% = USD 53.74.
- Combined base IESS: 482 x 20.60% = USD 99.29 (check: 45.55 + 53.74 = 99.29). [misalario.ec]
- No income tax: USD 482 x 12 = USD 5,784 annual, well below the FY2026 tax-free fraction of USD 12,208 [SRI Res. NAC-DGERCGC25-00000043].

**Classification:** EXCLUDE IESS debit USD 99.29 combined; zero PIT.

### Example 5 -- SRI income-tax payment (NOT IESS)

**Input line:**
`26.03.2026 ; SRI IMPUESTO RENTA FORM 102A ; DEBIT ; DECLARACION 2025 ; -624.00 ; USD`

**Reasoning:**
Matches "SRI" / "IMPUESTO RENTA" (pattern 3.3). This is the annual income-tax settlement (Formulario 102A), NOT an IESS contribution. USD 624 corresponds to the FY2025 cumulative tax at the top of the third bracket (taxable income USD 19,978) [SRI Res. NAC-DGERCGC24-00000041]. Exclude from IVA; do not classify as social security.

**Classification:** EXCLUDE -- SRI income-tax payment. NOT IESS.

### Example 6 -- Ambiguous IESS lump sum (mora patronal / arrears)

**Input line:**
`14.07.2025 ; IESS CONVENIO PAGO ; DEBIT ; PLANILLA + MORA ; -1,820.00 ; USD`

**Reasoning:**
Matches "IESS" (pattern 3.1) but the reference says "PLANILLA + MORA" and the amount is irregular. This likely combines unpaid contributions with mora patronal interest (Banco Central max conventional rate +4 points) and fines [IESS]. Principal cannot be separated from interest/fines without an IESS statement.

**Classification:** EXCLUDE from IVA. Flag for reviewer -- request IESS detalle to split contribution principal (deductible expense) from interest/fines (non-deductible).

## Section 5 -- Tier 1 rules

Apply exactly as written when worker type, period and remuneration are known.

### Rule 1 -- Employee IESS contribution

- **employee_IESS** — employee_IESS = materia_gravada x 9.45% (Private-sector dependent worker, withheld by the employer)  _([misalario.ec; PwC])_

### Rule 2 -- Employer IESS contribution

- **employer_IESS** — employer_IESS_base = materia_gravada x 11.15% employer_IESS_PwC = materia_gravada x 12.15% (= 11.15% + 0.5% IECE + 0.5% SECAP) (State which basis is used. Local Ecuadorian sources cite 11.15% base and list IECE/SECAP separately; PwC consolidates to 12.15%)  _([misalario.ec; tagline-soluciones; PwC])_

### Rule 3 -- Combined base IESS rate

- **combined_base_IESS** — combined_base_IESS = materia_gravada x 20.60% (= 9.45% + 11.15%)  _([misalario.ec])_

### Rule 4 -- Employer 11.15% internal breakdown

- **11.15% internal breakdown** — IVM/pensions 3.10% + Salud 5.71% + Riesgos del Trabajo 0.55% + Cesantia 1.00% + Seguro Social Campesino 0.35% + gastos administrativos 0.44% = 11.15%. **[RESEARCH GAP -- reviewer to confirm against the official IESS Tasas de Aportacion PDF before publishing the sub-allocation.]**  _([tagline-soluciones])_

### Rule 5 -- Fondos de reserva (8.33%, from month 13)

- **fondos_de_reserva** — fondos_de_reserva = remuneration x 8.33% (employer, only from the 13th month of continuous service) (Paid monthly in payroll unless the worker requests accumulation at IESS. Not owed in the first 12 months)  _([misalario.ec; PwC])_

### Rule 6 -- SBU floor, no ceiling

- **SBU floor, no ceiling** — The SBU is the effective minimum contribution base for a full-time worker: USD 470/month in 2025, USD 482/month in 2026. There is NO general upper ceiling on the dependent-worker contribution base.  _([Ministerio del Trabajo; Acuerdo MDT-2025-195; misalario.ec])_

### Rule 7 -- Voluntary affiliate rate

- **voluntary_affiliate_IESS** — voluntary_affiliate_IESS = declared_monthly_income x 17.60%  _([PwC; ecuador.unir.net])_

### Rule 8 -- Decimos and utilidades are NOT materia gravada

- **Decimos/utilidades excluded from base** — Decimo tercero, decimo cuarto, fondos de reserva and utilidades are excluded from the IESS contributable base. Do not apply the 9.45% / 11.15% to these items.  _([PwC])_

### Rule 9 -- Personal income tax (progressive, FY2025)

FY2025 table per SRI Resolution NAC-DGERCGC24-00000041 (declared in 2026). Tax-free fraction USD 12,081; top rate 37% above USD 108,810.

**FY2025 progressive income-tax table**  _([SRI Res. NAC-DGERCGC24-00000041, via JEZL Auditores])_

| Basic fraction (from) | Up to | Tax on basic fraction | Rate on excess |
| --- | --- | --- | --- |
| 0 | 12,081 | 0 | 0% |
| 12,081 | 15,387 | 0 | 5% |
| 15,387 | 19,978 | 165 | 10% |
| 19,978 | 26,422 | 624 | 12% |
| 26,422 | 34,770 | 1,398 | 15% |
| 34,770 | 46,089 | 2,650 | 20% |
| 46,089 | 61,359 | 4,914 | 25% |
| 61,359 | 81,817 | 8,731 | 30% |
| 81,817 | 108,810 | 14,869 | 35% |
| 108,810 | -- | 24,316 | 37% |

### Rule 10 -- Personal income tax (progressive, FY2026)

FY2026 table per SRI Resolution NAC-DGERCGC25-00000043 (declared in 2027). Tax-free fraction USD 12,208; top rate 37% above USD 109,956.

**FY2026 progressive income-tax table**  _([SRI Res. NAC-DGERCGC25-00000043, via JEZL Auditores])_

| Basic fraction (from) | Up to | Tax on basic fraction | Rate on excess |
| --- | --- | --- | --- |
| 0 | 12,208 | 0 | 0% |
| 12,208 | 15,549 | 0 | 5% |
| 15,549 | 20,188 | 167 | 10% |
| 20,188 | 26,700 | 631 | 12% |
| 26,700 | 35,136 | 1,412 | 15% |
| 35,136 | 46,575 | 2,678 | 20% |
| 46,575 | 62,005 | 4,965 | 25% |
| 62,005 | 82,679 | 8,823 | 30% |
| 82,679 | 109,956 | 15,025 | 35% |
| 109,956 | -- | 24,572 | 37% |

### Rule 11 -- IESS payment deadline

- **IESS payment deadline** — The employer files and pays the monthly planilla (employee + employer + fondos de reserva) within 15 days after each month-end. Lateness triggers mora patronal.  _([IESS])_

### Rule 12 -- Mandatory affiliation from day one

- **Mandatory affiliation from day one** — All dependent workers must be affiliated (Aviso de Entrada) from the first day of work; there is no minimum income or hours threshold for mandatory affiliation.  _([IESS / AfiliacionIESS])_

### Rule 13 -- Decimo tercero and decimo cuarto

- **Decimo tercero and decimo cuarto** — Decimo tercer sueldo = 1/12 of annual ordinary remuneration, payable by 24 December (or monthly if elected) [lexis.com.ec]. Decimo cuarto sueldo = one SBU per year (USD 470 in 2025; USD 39.17/month accumulated), payable by 15 March (Coast/Galapagos) or 15 August (Sierra/Amazon) [ecuadorlegalonline.com].  _([lexis.com.ec; ecuadorlegalonline.com])_

### Rule 14 -- Annual income-tax return

- **Annual income-tax return** — Formulario 102/102A is due in March of the following year, on a date set by the 9th digit of the taxpayer's RUC/cedula (window approx 10-28 March). Employees with only employment income and no other income may rely on employer withholding and Formulario 107 instead of filing 102 separately.  _([SRI; gob.ec])_

## Section 6 -- Tier 2 catalogue

Flag these for reviewer confirmation when data is ambiguous.

### T2-1 -- Employer rate basis (11.15% vs 12.15%)

- **T2-1** — Trigger: any employer-cost model. Issue: local sources cite 11.15% base + separate IECE/SECAP; PwC consolidates to 12.15%. Action: confirm which presentation the client uses; state it explicitly in the working paper.

### T2-2 -- Internal 11.15% sub-allocation

- **T2-2** — Trigger: a report depending on the IVM/Salud/Riesgos/Cesantia/SSC/admin split. Issue: the split comes from a secondary source, not the official IESS PDF (which could not be parsed). Action: **[RESEARCH GAP -- reviewer to confirm]** against iess.gob.ec/documents/13718/54965/Tasasdeaportacion.pdf.

### T2-3 -- Alleged extra 0.1% disability-pension contribution

- **T2-3** — Trigger: a model relying on an additional ~0.1%. Issue: referenced by a secondary source only, not independently confirmed. Action: **[RESEARCH GAP -- reviewer to confirm]**; do NOT include in headline rates.

### T2-4 -- Fondos de reserva timing

- **T2-4** — Trigger: worker near the 12-month mark. Issue: 8.33% begins only from month 13 of continuous service with the same employer. Action: confirm the exact start date before including.

### T2-5 -- IESS mora patronal / responsabilidad patronal

- **T2-5** — Trigger: unpaid contributions. Issue: interest at Banco Central max conventional rate +4 points, plus fines and employer liability for benefits paid in Health/Pensions/Work Risk/Cesantia. Action: do NOT quantify without an IESS statement; escalate.

### T2-6 -- Region-dependent decimo cuarto deadline

- **T2-6** — Trigger: decimo cuarto provision. Issue: deadline is 15 March (Coast/Galapagos) vs 15 August (Sierra/Amazon). Action: confirm the worksite region.

### T2-7 -- FY2026 forward-looking figures

- **T2-7** — Trigger: computations for periods in 2026. Issue: FY2026 SBU (USD 482) and the FY2026 income-tax table are officially confirmed but forward-looking. Action: confirm the period; cross-check the literal SRI resolution on sri.gob.ec.

## Section 7 -- Excel working paper template

```
ECUADOR PAYROLL / IESS COMPUTATION -- WORKING PAPER
Client: [name]                 RUC: [____]
Tax/Contribution Period:       [month/year]
Prepared: [date]

INPUT DATA
  Worker type:                 [private dependent / public / voluntary / self-employed]
  Region (worksite):           [Coast-Galapagos / Sierra-Amazon]
  Months continuous service:   [____]   (>=13 => fondos de reserva due)
  Monthly remuneration (materia gravada): USD [____]
  SBU floor applied:           USD [470 (2025) / 482 (2026)]
  Employer rate basis:         [11.15% base / 12.15% PwC incl. IECE+SECAP]

IESS COMPUTATION
  Employee aporte personal (9.45%):   USD [____]
  Employer aporte patronal (11.15%):  USD [____]
  IECE (0.50%):                       USD [____]
  SECAP (0.50%):                      USD [____]
  Fondos de reserva (8.33%, if >=13m): USD [____]
  Combined base IESS (20.60%):        USD [____]
  Total employer statutory cost:      USD [____]

INCOME TAX (retencion en relacion de dependencia)
  Annual projected taxable income:    USD [____]
  Tax-free fraction (12,081 / 12,208): USD [____]
  Bracket / rate on excess:           [____]
  Annual PIT:                         USD [____]
  Monthly withholding:                USD [____]

LABOUR BENEFITS (not materia gravada)
  Decimo tercero (1/12):              USD [____]
  Decimo cuarto (one SBU / 12):       USD [____]
  Utilidades (15% of profit, if any): USD [____]

REVIEWER FLAGS
  [List any Tier 2 / RESEARCH GAP flags here]

CONSERVATIVE DEFAULTS APPLIED
  [List any defaults applied and their cost impact]
```

## Section 8 -- Bank statement reading guide

### How IESS and SRI payments appear on Ecuadorian bank statements

**Banco Pichincha:**
- Description: "PAGO IESS", "CONVENIO IESS", "PLANILLA IESS"
- Timing: within 15 days after month-end
- Amount: combined employee + employer (+ fondos de reserva if applicable)

**Banco del Pacifico / Produbanco / Banco Guayaquil:**
- Description: "IESS APORTES", "PLANILLA DE APORTES", "SEGURIDAD SOCIAL"
- Timing: same monthly cycle

**SRI tax debits (do NOT confuse with IESS):**
- Description: "SRI", "IMPUESTO RENTA", "FORM 102/102A", "FORMULARIO 104" (IVA), "RETENCION EN LA FUENTE"
- These are tax remittances, not contributions

**Key identification tips:**
1. IESS contribution debits are outgoing (DEBIT), recurring monthly, roughly 20.6% of payroll (+ fondos de reserva).
2. Inbound IESS credits (PENSION, JUBILACION, PRESTAMO/QUIROGRAFARIO) are benefits/loans, not contributions.
3. SRI references mean income tax or IVA, never IESS.
4. Irregular "IESS + MORA / CONVENIO" lump sums likely include penalties -- flag for reviewer.
5. Decimo tercero/cuarto and utilidades are payroll/labour outflows, not contributions.

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for IESS debits** -- identify all outgoing payments matching Section 3.1/3.2 patterns.
2. **Sum monthly IESS paid** -- total the planilla debits.
3. **Reverse-engineer payroll:** combined base IESS is 20.60% of materia gravada, so approximate payroll = total IESS debit / 0.206 (before fondos de reserva) [misalario.ec].
4. **Separate SRI debits** -- classify "SRI / IMPUESTO RENTA / FORM 102 / 104" as tax, never IESS.
5. **Flag for reviewer:** "IESS/payroll figures derived from bank statement amounts only. Worker type, service tenure, SBU floor, employer-rate basis and FY2025-vs-FY2026 period have not been independently verified. Reviewer must confirm before filing."

## Section 10 -- Reference material

### Income-tax cumulative-tax verification (FY2025) [SRI Res. NAC-DGERCGC24-00000041]

**Cumulative-tax verification**  _([SRI Res. NAC-DGERCGC24-00000041])_

| Up to | Cumulative tax (table) | Recompute from prior bracket |
| --- | --- | --- |
| 15,387 | 165 | (15,387-12,081) x 5% = 165.30 |
| 19,978 | 624 | 165 + (19,978-15,387) x 10% = 624.10 |
| 26,422 | 1,398 | 624 + (26,422-19,978) x 12% = 1,397.28 |
| 34,770 | 2,650 | 1,398 + (34,770-26,422) x 15% = 2,650.20 |
| 46,089 | 4,914 | 2,650 + (46,089-34,770) x 20% = 4,913.80 |
| 61,359 | 8,731 | 4,914 + (61,359-46,089) x 25% = 8,731.50 |
| 81,817 | 14,869 | 8,731 + (81,817-61,359) x 30% = 14,868.40 |
| 108,810 | 24,316 | 14,869 + (108,810-81,817) x 35% = 24,316.55 |

(Recomputed values reconcile to the published rounded figures.)

### Thresholds

**Thresholds table**

| Threshold | Value | Source |
| --- | --- | --- |
| Income-tax filing trigger (FY2025) | Annual gross above USD 12,081 | SRI Res. NAC-DGERCGC24-00000041 |
| Tax-free fraction (FY2026) | USD 12,208 | SRI Res. NAC-DGERCGC25-00000043 |
| IESS mandatory affiliation | From day 1; no income/hours minimum | IESS / AfiliacionIESS |
| Fondos de reserva eligibility | From the 13th month of continuous service | misalario.ec |
| SBU 2025 (contribution floor) | USD 470/month | Ministerio del Trabajo |
| SBU 2026 (contribution floor) | USD 482/month | Acuerdo MDT-2025-195; nmslaw.com.ec |

### Forms

**Forms table**

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| Formulario 102 / 102A | Annual PIT return for natural persons (102 = keeps books; 102A = not) | March (by 9th digit of RUC, approx 10-28) | SRI; gob.ec |
| Formulario 107 | Annual employment-income & withholding certificate (employer to employee) | By end of January following the tax year | SRI |
| IESS Planilla de aportes | Monthly contribution/payroll return to IESS | Within 15 days after month-end | IESS |
| Aviso de Entrada / Salida | Register/notify each worker's start/separation | From day 1 of employment | IESS / AfiliacionIESS |

### Penalties

**Penalties table**

| Penalty | Rule | Source |
| --- | --- | --- |
| IESS mora patronal | Interest at Banco Central max conventional rate +4 points, plus fines, plus responsabilidad patronal | IESS |
| Late income-tax filing | 3% of tax caused per month of delay, capped at 100%; interest also accrues | extra.ec (LRTI) |
| Failure to affiliate | Unpaid contributions + interest/fines; non-affiliation is criminalized | IESS / AfiliacionIESS |

### Utilidades (profit sharing -- labour obligation, not a contribution)

- **Utilidades** — 15% of company pre-tax profits distributed to workers (10% to all workers, 5% by family burden), payable by 15 April. Separate from IESS.  _([PwC])_

### Test suite

Private dependent worker, materia gravada USD 1,000, FY2025. Employee IESS = 1,000 x 9.45% = USD 94.50. Employer base = 1,000 x 11.15% = USD 111.50. Combined base = USD 206.00. (Check 94.50 + 111.50 = 206.00.) [misalario.ec]

Same worker, employer total per PwC basis = 1,000 x 12.15% = USD 121.50 (= 111.50 + 5.00 IECE + 5.00 SECAP). [PwC]

Worker past 12 months, USD 1,000 base. Fondos de reserva = 1,000 x 8.33% = USD 83.30. [misalario.ec]

Worker under 12 months, USD 1,000. Fondos de reserva = USD 0.00 (not yet owed). [misalario.ec]

SBU worker FY2026, USD 482. Employee IESS = 482 x 9.45% = USD 45.55. Employer base = 482 x 11.15% = USD 53.74. Combined = USD 99.29. No PIT (5,784 annual < 12,208). [misalario.ec; SRI Res. NAC-DGERCGC25-00000043]

Natural person, FY2025 taxable income USD 30,000. PIT = 1,398 + (30,000 - 26,422) x 15% = 1,398 + 3,578 x 15% = 1,398 + 536.70 = **USD 1,934.70**. [SRI Res. NAC-DGERCGC24-00000041]

Natural person, FY2025 taxable income USD 50,000. PIT = 4,914 + (50,000 - 46,089) x 25% = 4,914 + 3,911 x 25% = 4,914 + 977.75 = **USD 5,891.75**. [SRI Res. NAC-DGERCGC24-00000041]

Natural person, FY2025 taxable income USD 12,000 (below USD 12,081). PIT = USD 0.00; generally not required to file. [SRI Res. NAC-DGERCGC24-00000041]

Natural person, FY2026 taxable income USD 30,000. PIT = 1,412 + (30,000 - 26,700) x 15% = 1,412 + 3,300 x 15% = 1,412 + 495.00 = **USD 1,907.00**. [SRI Res. NAC-DGERCGC25-00000043]

Voluntary affiliate, declared income USD 1,000. IESS = 1,000 x 17.60% = USD 176.00. [PwC; ecuador.unir.net]

### Prohibitions

- NEVER apply the 9.45% / 11.15% rates to decimo tercero, decimo cuarto, fondos de reserva or utilidades -- they are NOT materia gravada.
- NEVER include 8.33% fondos de reserva for a worker under 12 months of continuous service.
- NEVER mix the 11.15% (base) and 12.15% (PwC) employer figures in the same total without stating the basis.
- NEVER publish the internal 11.15% sub-breakdown as definitive -- it is a RESEARCH GAP until verified against the official IESS PDF.
- NEVER include the alleged extra ~0.1% disability sub-rate in headline figures without reviewer confirmation.
- NEVER apply a contribution ceiling for dependent workers -- there is none.
- NEVER use a contribution base below the SBU floor for a full-time worker.
- NEVER confuse SRI tax debits with IESS contribution debits.
- NEVER quantify IESS mora patronal or arrears without an IESS statement -- escalate.
- NEVER present figures as definitive -- this is a Tier 2 research-verified skill pending professional sign-off.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador publico autorizado, abogado tributario, CPA, EA, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
