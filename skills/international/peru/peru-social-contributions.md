---
name: peru-social-contributions
description: Use this skill whenever asked about Peru payroll contributions, social security, health insurance, pensions, or employment income tax. Trigger on phrases like "EsSalud contribution", "how much is EsSalud", "ONP vs AFP", "AFP deductions", "pension contribution Peru", "quinta categoría tax", "fifth-category income tax", "PLAME filing", "Formulario 0601", "Peru payroll tax", "renta de quinta", "descuentos de planilla", "CTS calculation", "gratificaciones", "Peru minimum wage", "RMV", "UIT", or any question about Peruvian payroll, social contributions, or employment income tax. Also trigger when classifying bank statement transactions that relate to SUNAT payments, EsSalud, ONP, AFP/AFPnet debits, or payroll runs from BCP, BBVA, Interbank, or Scotiabank Peru. This skill covers EsSalud (9% health), ONP (13% public pension), AFP/SPP (private pension ~12.84%–13.06%), fifth-category income tax (8%–30% on UIT brackets), the 7-UIT exemption, minimum wage (RMV), CTS, gratificaciones, PLAME/Form 0601 monthly filing, the annual return, registration, bank statement classification patterns, and edge cases. ALWAYS read this skill before touching any Peru payroll or contribution work.
version: 0.1
jurisdiction: PE
tax_year: 2026
last_updated: 2026-07-13
reviewed_by: Maria Clemencia Valverde Rios
review_status: current
depends_on:
  - social-contributions-workflow-base
category: international
tier: 1
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Peru Social Security, Health & Payroll Contributions

## Peru Social Security, Health & Payroll Contributions Skill v0.1

## Verified rates & thresholds (accountant-reviewed)

> Reviewed against the cited tax authorities by **Maria Clemencia Valverde Rios** on 2026-06-29.
> Items flagged for further clarification are tracked separately and excluded here.
> This block is generated from verified `skill_facts` — edit the facts, not the prose.

### peru-social-contributions

- **Currency** — PEN (Peruvian Sol, S/)
- **Indexing unit (UIT) 2025** — PEN 5,350
- **Indexing unit (UIT) 2026** — PEN 5,500
- **Minimum wage (RMV)** — PEN 1,130/month from 1 Jan 2025  _(D.S. 006-2024-TR)_
- **EsSalud (health) rate** — 9% of remuneration, employer-borne, no cap
- **ONP (public pension) rate** — 13% of remuneration, employee-borne
- **AFP (private pension) total rate** — ~12.84%–13.06% of remuneration, employee-borne
- **Monthly filing form** — Electronic Payroll is PLAME, Virtual Form 0601, version v4.6, which is mandatory for tax returns as of the January 2026  _(Art. 2 RS No000016-2026 SUNAT)_
- **Monthly PLAME filing deadline** — Monthly, by date matching last digit of employer's RUC per SUNAT annual cronograma;  _(Art. 4°-b DS N° 018-2007-TR)_
- **Annual return deadline (FY2025)** — Due 27 May – 10 Jun 2026 by RUC digit
- **EsSalud minimum base** — min base = RMV (apply 9% on the RMV PEN 1,130 minimum base if salary below RMV)
- **Fifth-category income tax rate range** — 8%–30% progressive (UIT brackets)
- **AFP mandatory contribution (aporte obligatorio)** — 10%
- **AFP disability/survivor insurance premium (prima)** — 1.37% (capped at RMA, uniform across all AFPs)
- **AFP Habitat commission (flujo) and total** — Habitat flujo commission 1.47%; total 12.84%
- **AFP Integra commission (flujo) and total** — Integra flujo commission 1.55%; total 12.92%
- **AFP Prima commission (flujo) and total** — Prima flujo commission 1.60%; total 12.97%
- **AFP Profuturo commission (flujo) and total** — Profuturo flujo commission 1.69%; total 13.06%
- **AFP comisión mixta flow commission** — 0% for all four AFPs (since Feb 2023); on-salary deduction is 10% + 1.37% = 11.37%
- **AFP comisión mixta annual charge on fund balance** — Profuturo 0.68%, Integra 0.78%, Habitat & Prima 1.25%
- **Remuneración Máxima Asegurable (RMA) for prima ceiling** — ~PEN 12,209.11 (early 2026) and PEN 12,598.91 for Apr–Jun 2026; updated quarterly by SBS
- **EPS private health plan credit against EsSalud** — Up to 25% of the EsSalud obligation credited to EPS (~2.25% to EPS, ~6.75% still to EsSalud)
- **Fifth-category bracket 1** — Up to 5 UIT (0 – 27,500 PEN 2026): 8%
- **Fifth-category bracket 2** — Over 5 to 20 UIT (27,500 – 110,000 PEN 2026): 14%
- **Fifth-category bracket 3** — Over 20 to 35 UIT (110,000 – 192,500 PEN 2026): 17%
- **Fifth-category bracket 4** — Over 35 to 45 UIT (192,500 – 247,500 PEN 2026): 20%
- **Fifth-category bracket 5** — Over 45 UIT (Over 247,500 PEN 2026): 30%
- **7-UIT exemption (residents) 2025** — 7 × 5,350 = PEN 37,450
- **7-UIT exemption (residents) 2026** — 7 × 5,500 = PEN 38,500
- **Additional documented-expense deduction** — Up to 3 UIT deductible for documented expenses (property lease, professional services, hotels, restaurants, etc.)
- **Non-domiciled flat income tax rate** — Flat 30% on gross Peruvian-source employment income, NO 7-UIT exemption, NO additional deductions
- **PLAME version mandatory** — Version 4.5 mandatory for periods from Oct 2025
- **Employer registration trigger** — Triggered by employing staff, not by a wage threshold; no monetary registration threshold found
- **CTS (Compensación por Tiempo de Servicios)** — ~9.72% of annual salary, deposited by 15 May & 15 Nov; base includes 1/6 of gratificación
- **Gratificaciones (statutory bonus)** — Two per year (July Fiestas Patrias, December Navidad), ≈ one month's salary each, prorated if <6 months
- **Penalty schedule** — RESEARCH GAP — no authoritative penalty schedule obtained; verify against SUNAT Código Tributario Tabla de Infracciones y Sanciones and SUNAFIL; do not invent figures  _(SUNAT Código Tributario Tabla de Infracciones y Sanciones)_
- **SUNAFIL cumulative fine scale** — The official cumulative fine scale based on the number of affected employees is current under the comprehensive replacement ordered by DS No. 008-2020-TR, which amended Art. 48 of the Regulations of the General Labor Inspection Law (D.S No. 019-2006-TR), applied indexed to the current UIT value for the 2026 period.  _(Decreto Supremo N.° 008-2020-TR)_
- **SUNAT infractions and sanctions governance** — Infractions and sanctions are governed by Art. 172° TUO del Código Tributario (D.S. N.° 133-2013-EF), but its text and actual application are amended and current under Decreto Legislativo N.° 1524 (which restructured registration offenses) in mandatory conjunction with the Regulations for the Leniency Regime Resolución de Superintendencia N.° 063-2007/SUNAT  _(Art. 13°-b RS N.° 000007-2025 SUNAT)_

## Section 1 -- Quick reference

**Read this whole section before computing or classifying anything.**

**Quick reference field table**

| Field | Value |
| --- | --- |
| Country | Peru (Republic of Peru) |
| Currency | PEN (Peruvian Sol, S/) |
| Income tax | YES — Impuesto a la Renta, fifth category (renta de quinta) on employment income |
| Tax authority | SUNAT (Superintendencia Nacional de Aduanas y de Administración Tributaria) |
| Health authority | EsSalud (Seguro Social de Salud) |
| Public pension | ONP (Oficina de Normalización Previsional) — Sistema Nacional de Pensiones |
| Private pension | AFP / SPP (Sistema Privado de Pensiones), regulated by the SBS |
| Indexing unit (UIT) 2025 | PEN 5,350 ([PwC, individual taxes on personal income](https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income)) |
| Indexing unit (UIT) 2026 | PEN 5,500 ([PwC, reviewed 21 Jan 2026](https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income)) |
| Minimum wage (RMV) | PEN 1,130/month from 1 Jan 2025 (D.S. 006-2024-TR) — still in force ([Andina](https://andina.pe/agencia/noticia-remuneracion-minima-vital-sube-a-1130-soles-a-partir-del-1-enero-2025-1012953.aspx)) |
| EsSalud (health) | 9% of remuneration, employer-borne, no cap ([PwC, other taxes](https://taxsummaries.pwc.com/peru/individual/other-taxes)) |
| ONP (public pension) | 13% of remuneration, employee-borne ([PwC, other taxes](https://taxsummaries.pwc.com/peru/individual/other-taxes)) |
| AFP (private pension) | ~12.84%–13.06% of remuneration, employee-borne ([PwC](https://taxsummaries.pwc.com/peru/individual/other-taxes); [TrámitesPerú](https://tramitesperu.com/comparadores/afp-comisiones/)) |
| Monthly filing | PLAME (Planilla Electrónica), Formulario Virtual 0601, v4.5 mandatory from Oct 2025 ([SUNAT](https://orientacion.sunat.gob.pe/pdt-plame)) |
| Filing deadline | Monthly, by last digit of employer RUC per SUNAT cronograma (≈14th–24th of following month) ([SUNAT](https://orientacion.sunat.gob.pe/pdt-plame)) |
| Annual return (FY2025) | Due 27 May – 10 Jun 2026 by RUC digit ([NVC Abogados](https://nvcabogados.com/annual-income-tax-return-2025-in-peru/)) |
| Validated by | Verified by Maria Clemencia Valverde Rios (CPA) on 2026-06-29 |
| Validation date | Verified by Maria Clemencia Valverde Rios (CPA) on 2026-06-29 |

**Who pays what (monthly payroll):**

**Who pays what (monthly payroll)**

| Item | Rate | Borne by | Cap |
| --- | --- | --- | --- |
| EsSalud (health) | 9% | Employer | None; min base = RMV ([PwC](https://taxsummaries.pwc.com/peru/individual/other-taxes)) |
| ONP (public pension) — IF employee in ONP | 13% | Employee | None ([PwC](https://taxsummaries.pwc.com/peru/individual/other-taxes)) |
| AFP (private pension) — IF employee in AFP | ~12.84%–13.06% | Employee | None on the 10%; prima capped at RMA ([TrámitesPerú](https://tramitesperu.com/comparadores/afp-comisiones/)) |
| Fifth-category income tax | 8%–30% progressive (UIT brackets) | Employee (withheld) | n/a ([PwC](https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income)) |

- **Pension is one OR the other** — Every employee belongs to EITHER ONP (public) OR an AFP (private), never both. The employer withholds whichever applies. Employers do NOT pay a separate pension match.

**Conservative defaults:**

**Conservative defaults**

| Ambiguity | Default |
| --- | --- |
| Unknown residency status | Assume resident (domiciled) — flag for reviewer |
| Unknown pension regime (ONP vs AFP) | STOP — ask; the rate differs (13% vs ~12.84%–13.06%) |
| Unknown AFP | Use the highest documented total to be conservative; flag for reviewer |
| Salary below RMV (for EsSalud) | Apply 9% on the RMV (PEN 1,130) minimum base |
| Unknown tax year | Assume 2026 (UIT = 5,500) and state assumption |
| Unknown whether non-domiciled | Do not apply 7-UIT exemption until confirmed; flag |
| Penalty figures | STOP — not in scope; escalate (see Section 10) |

## Section 2 -- Required inputs and refusal catalogue

### Required inputs

**Minimum viable** — gross monthly remuneration (PEN), residency status (domiciled / non-domiciled), and pension regime (ONP or AFP). Without the pension regime, STOP — the deduction rate cannot be determined.

**Recommended** — for AFP members, which AFP and which commission regime (comisión por flujo vs comisión mixta); tax year (for UIT and RMV); whether other employers or income exist.

**Ideal** — boleta de pago (payslip), PLAME export, AFPnet / ONP statements, the employer's RUC ending digit (for deadlines), and prior boletas to confirm the year-to-date withholding projection.

### Refusal catalogue

- **R-PE-1 — Pension regime unknown** — Trigger: not told whether the employee is in ONP or an AFP. Message: "The pension deduction is 13% (ONP) or ~12.84%–13.06% (AFP), and the two are mutually exclusive. Cannot compute the net deduction without confirming the regime. Please provide the worker's pension affiliation."
- **R-PE-2 — AFP insurance ceiling (RMA)** — Trigger: high earner where the prima de seguro ceiling (RMA) bites. Message: "The disability/survivor insurance premium (1.37%) is capped at the Remuneración Máxima Asegurable, which the SBS updates EVERY QUARTER. I cannot apply a stale figure. The current-quarter RMA must be re-verified on the SBS page before computing. Escalate to a reviewer."
- **R-PE-3 — Penalties / late filing** — Trigger: late PLAME, unpaid contributions, CTS non-deposit, or any sanction quantification. Message: "Peruvian penalty schedules (SUNAT Código Tributario Tabla de Infracciones, SUNAFIL labour fines) were not obtained from an authoritative source for this skill. Do not estimate. Escalate to a Peruvian contador público colegiado."
- **R-PE-4 — Non-domiciled / expat treatment** — Trigger: client claims non-resident status, split year, or treaty relief. Message: "Non-domiciled individuals are taxed at a flat 30% on gross Peruvian-source employment income with NO 7-UIT exemption and NO deductions. Residency determination and any treaty relief require case-specific confirmation. Escalate to a reviewer."
- **R-PE-5 — CTS / gratificaciones quantification at the cent** — Trigger: request for an exact CTS or gratificación figure to deposit. Message: "CTS and gratificaciones depend on the computation base (including 1/6 of the gratificación for CTS, family allowance, average variable pay, and months of service). I can explain the framework but the exact deposit must be confirmed by the reviewer against payslips."

## Section 3 -- Payment pattern library

This is the deterministic pre-classifier for bank statement transactions related to Peruvian payroll, social contributions, and tax. When a transaction matches a pattern below, apply the treatment directly. Do not second-guess.

**How to read this table.** Match by case-insensitive substring on the counterparty/reference as it appears in the bank statement. Statutory contributions and tax withholdings remitted to SUNAT/AFP are EXCLUDED from any IGV (VAT) input-tax claim — they are payroll/tax obligations, not taxable supplies.

### 3.1 SUNAT payments (income tax withholding, EsSalud, ONP via PLAME)

**SUNAT payments pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| SUNAT, PAGO SUNAT | EXCLUDE — tax/contribution remittance | PLAME / Form 0601 monthly payment |
| PLAME, PLANILLA ELECTRONICA | EXCLUDE — payroll declaration payment | Covers renta 5ta, EsSalud, ONP |
| RENTA QUINTA, RENTA 5TA, 5TA CATEGORIA | EXCLUDE — income tax withheld | Employee PIT remitted to SUNAT |
| ESSALUD, ES SALUD | EXCLUDE — employer health contribution | 9%, employer cost |
| ONP, SNP | EXCLUDE — public pension withheld | 13%, employee-borne |
| FORMULARIO 0601, FORM 0601 | EXCLUDE — PLAME payment | Monthly form |

### 3.2 AFP / private pension payments (AFPnet)

**AFP payment pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| AFPNET, AFP NET | EXCLUDE — private pension remittance | Employer collects/remits employee deduction |
| AFP HABITAT, AFP INTEGRA, AFP PRIMA, AFP PROFUTURO | EXCLUDE — pension remittance | Name of the AFP |
| SPP, SISTEMA PRIVADO PENSIONES | EXCLUDE — private pension | Same |
| APORTE OBLIGATORIO, COMISION AFP, PRIMA SEGURO | EXCLUDE — AFP components | 10% / commission / 1.37% |

### 3.3 Employer-borne benefits (CTS, gratificaciones)

**Employer-borne benefits pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| CTS, COMP TIEMPO SERVICIOS | EXCLUDE — severance deposit | Twice-yearly bank deposit (15 May / 15 Nov) |
| GRATIFICACION, GRATI, FIESTAS PATRIAS, AGUINALDO | EXCLUDE — statutory bonus | July & December |

### 3.4 Salary and payroll (exclude from contribution classification)

**Salary and payroll pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| ABONO HABERES, PAGO PLANILLA (outgoing) | EXCLUDE — payroll expense | Net wage to employee |
| SUELDO, REMUNERACION, HABERES (incoming) | EXCLUDE — employment income received | Not a contribution |
| TELECREDITO, PAGO DE HABERES | EXCLUDE — payroll batch | Bank payroll module |

### 3.5 Pension income received (NOT a contribution)

**Pension income received pattern table**

| Pattern | Treatment | Notes |
| --- | --- | --- |
| PENSION ONP, PENSION SNP | EXCLUDE — pension income received | Not a contribution paid |
| PENSION AFP, RETIRO AFP, JUBILACION | EXCLUDE — pension/withdrawal received | Not a contribution |

## Section 4 -- Worked examples

Six bank statement classifications and computations for a hypothetical Lima employer and its staff. All figures in PEN, tax year 2026 (UIT = 5,500, RMV = 1,130).

### Example 1 — Monthly PLAME remittance to SUNAT (BCP)

**Input line:**
`16.02.2026 ; SUNAT PAGO PLAME 0601 ; DEBIT ; PERIODO ENE-2026 ; -3,250.00 ; PEN`

**Reasoning:**
Matches "SUNAT" and "PLAME 0601" (pattern 3.1). This is the monthly Planilla Electrónica payment covering fifth-category income tax withheld, EsSalud (9% employer), and ONP (13% employee). The Feb date for the January period is consistent with the SUNAT cronograma (deadline by RUC digit, ≈14th–24th of the following month). Exclude from IGV input claim — it is tax/contribution remittance.

**Classification:** EXCLUDE — SUNAT payroll remittance (renta 5ta + EsSalud + ONP).

### Example 2 — AFP remittance via AFPnet (BBVA)

**Input line:**
`05.02.2026 ; AFPNET AFP INTEGRA ; DEBIT ; APORTES ENE-2026 ; -1,940.00 ; PEN`

**Reasoning:**
Matches "AFPNET" / "AFP INTEGRA" (pattern 3.2). This is the employer remitting employees' AFP deductions (mandatory 10% + prima 1.37% + Integra commission) to AFP Integra. It is an employee-borne deduction remitted by the employer, not an employer pension cost. Exclude from IGV.

**Classification:** EXCLUDE — AFP private pension remittance (employee deductions).

### Example 3 — EsSalud on a single PEN 5,000 salary

**Scenario (not a bank line — a computation):** Employee earns PEN 5,000/month gross.

**Reasoning:**
EsSalud = 9% of remuneration, employer-borne, no cap, minimum base RMV ([PwC, other taxes](https://taxsummaries.pwc.com/peru/individual/other-taxes)). 5,000 × 9% = **PEN 450.00**. As actual pay (5,000) exceeds the RMV (1,130), the minimum base does not bite. This is an employer cost — NOT deducted from the employee.

**Classification:** Employer EsSalud cost = PEN 450.00/month. Excluded from the employee's net pay computation.

### Example 4 — AFP deduction detail (Habitat, comisión por flujo)

**Scenario:** Employee earns PEN 5,000/month gross, affiliated to AFP Habitat on comisión por flujo.

**Reasoning (rates: [TrámitesPerú](https://tramitesperu.com/comparadores/afp-comisiones/), [Misha](https://misha.pe/laboral/prima-seguro-afp/)):**
- Mandatory contribution (aporte obligatorio): 10% × 5,000 = 500.00
- Disability/survivor insurance (prima): 1.37% × 5,000 = 68.50 *(below the RMA ceiling, so full base applies)*
- Habitat commission (comisión por flujo): 1.47% × 5,000 = 73.50
- **Total AFP deduction = 12.84% × 5,000 = 642.00** (500.00 + 68.50 + 73.50 = 642.00 ✓)

**Classification:** Employee AFP deduction = PEN 642.00/month, withheld from gross.

### Example 5 — ONP deduction (same PEN 5,000 salary, public regime)

**Scenario:** Same PEN 5,000/month employee, but affiliated to ONP, not an AFP.

**Reasoning:**
ONP = 13% of remuneration, employee-borne ([PwC, other taxes](https://taxsummaries.pwc.com/peru/individual/other-taxes)). 5,000 × 13% = **PEN 650.00/month** withheld. Note this exceeds the AFP total in Example 4 (642.00) — the regimes genuinely differ. The employee is in ONP OR AFP, never both.

**Classification:** Employee ONP deduction = PEN 650.00/month, withheld from gross.

### Example 6 — CTS deposit (Interbank)

**Input line:**
`14.05.2026 ; CTS DEPOSITO BCP CTA ; DEBIT ; CTS MAY-2026 ; -2,500.00 ; PEN`

**Reasoning:**
Matches "CTS DEPOSITO" (pattern 3.3). CTS (Compensación por Tiempo de Servicios) is a statutory severance fund deposited to the employee's bank CTS account in two tranches — by 15 May and by 15 November ([EY Peru](https://www.ey.com/es_pe/insights/workforce/cts)). This is an employer labour cost, not a SUNAT/AFP contribution. The exact amount depends on the computation base (including 1/6 of the gratificación) — confirm against payslips (see R-PE-5). Exclude from IGV.

**Classification:** EXCLUDE — CTS severance deposit (employer cost). Exact base to be confirmed by reviewer.

## Section 5 -- Tier 1 rules

These rules apply when payslip/bank data is clear and all required inputs are available. Apply exactly as written.

### Rule 1 — EsSalud formula

- **EsSalud formula** — EsSalud = max(remuneration, RMV) × 9%      [employer-borne, no upper cap]  _(RMV = PEN 1,130 (from 1 Jan 2025; [Andina](https://andina.pe/agencia/noticia-remuneracion-minima-vital-sube-a-1130-soles-a-partir-del-1-enero-2025-1012953.aspx)). 9% rate ([PwC](https://taxsummaries.pwc.com/peru/individual/other-taxes)). If the employer runs a private EPS plan, up to 25% of the EsSalud obligation is credited to the EPS (~2.25% to EPS, ~6.75% still to EsSalud) ([PwC](https://taxsummaries.pwc.com/peru/individual/other-taxes)).)_

### Rule 2 — Pension is ONP OR AFP, never both

- **Pension is ONP OR AFP, never both** — If ONP: 13% × remuneration, employee-borne. If AFP: 10% + 1.37% prima + AFP commission, employee-borne. Determine the regime before computing.  _([PwC](https://taxsummaries.pwc.com/peru/individual/other-taxes))_

### Rule 3 — AFP three components

- **AFP deduction formula** — AFP deduction = 10% (mandatory) + 1.37% (prima, capped at RMA) + commission  _([TrámitesPerú](https://tramitesperu.com/comparadores/afp-comisiones/))_

**AFP commission table**  _([TrámitesPerú](https://tramitesperu.com/comparadores/afp-comisiones/))_

| AFP | Flujo commission | Total (flujo) |
| --- | --- | --- |
| Habitat | 1.47% | 12.84% |
| Integra | 1.55% | 12.92% |
| Prima | 1.60% | 12.97% |
| Profuturo | 1.69% | 13.06% |

- **AFP totals derivation and prima uniformity** — Each total = 10% + 1.37% + commission. (Habitat: 10 + 1.37 + 1.47 = 12.84 ✓; Profuturo: 10 + 1.37 + 1.69 = 13.06 ✓.) The prima (1.37%) is uniform across all AFPs ([Misha](https://misha.pe/laboral/prima-seguro-afp/)).  _([Misha](https://misha.pe/laboral/prima-seguro-afp/))_

### Rule 4 — AFP comisión mixta

- **AFP comisión mixta** — Under comisión mixta the flow commission is 0% for all four AFPs (since Feb 2023), replaced by an annual charge on the fund balance: Profuturo 0.68%, Integra 0.78%, Habitat & Prima 1.25%. Under comisión mixta the on-salary deduction is therefore 10% + 1.37% = 11.37% only.  _([TrámitesPerú](https://tramitesperu.com/comparadores/afp-comisiones/))_

### Rule 5 — Prima ceiling (RMA)

- **Prima ceiling (RMA)** — The 1.37% prima applies only up to the Remuneración Máxima Asegurable (RMA), updated quarterly by the SBS. Reported ~PEN 12,209.11 (early 2026) and PEN 12,598.91 for Apr–Jun 2026. [RESEARCH GAP — reviewer to confirm the exact current-quarter RMA on the SBS page before applying; it changes every quarter.] The 10% mandatory contribution and the commission have NO ceiling.  _([SBS schedule](https://www.sbs.gob.pe/app/spp/empleadores/comisiones_spp/Paginas/comision_prima.aspx))_

### Rule 6 — Fifth-category income tax brackets (residents)

**Fifth-category income tax brackets table**  _([PwC](https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income))_

| Bracket | Annual taxable income (UIT) | 2026 PEN range | Rate |
| --- | --- | --- | --- |
| 1 | Up to 5 UIT | 0 – 27,500 | 8% |
| 2 | Over 5 to 20 UIT | 27,500 – 110,000 | 14% |
| 3 | Over 20 to 35 UIT | 110,000 – 192,500 | 17% |
| 4 | Over 35 to 45 UIT | 192,500 – 247,500 | 20% |
| 5 | Over 45 UIT | Over 247,500 | 30% |

### Rule 7 — The 7-UIT exemption (residents only)

- **Taxable base formula** — Taxable base = annual gross employment income − 7 UIT [− up to 3 UIT documented expenses]  _([PwC](https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income))_
- **7 UIT values and additional deduction** — 7 UIT: 2025 = 7 × 5,350 = PEN 37,450; 2026 = 7 × 5,500 = PEN 38,500. An additional up to 3 UIT is deductible for documented expenses (property lease, professional services, hotels, restaurants, etc.)  _([PwC](https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income))_

### Rule 8 — Non-domiciled flat rate

- **Non-domiciled flat rate** — flat 30% on gross Peruvian-source employment income, NO 7-UIT exemption, NO additional deductions  _([PwC](https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income))_

### Rule 9 — Monthly PLAME filing

- **Monthly PLAME filing** — File PLAME (Planilla Electrónica), Formulario Virtual 0601, monthly. Version 4.5 mandatory for periods from Oct 2025. Deadline by the last digit of the employer's RUC per SUNAT's annual cronograma (≈14th–24th of the following month). AFP remittance via AFPnet on a similar monthly cycle.  _([SUNAT](https://orientacion.sunat.gob.pe/pdt-plame))_

### Rule 10 — Annual return

- **Annual return** — FY2025 return filed in 2026: due 27 May – 10 Jun 2026 by last RUC digit. Most pure-payroll (5th-category) employees do NOT file — the employer withholds monthly. Filing is required for: multiple employers, additional-deduction claims, other income categories not fully withheld, or SUNAT-designated obligors.  _([NVC Abogados](https://nvcabogados.com/annual-income-tax-return-2025-in-peru/))_

### Rule 11 — Registration

- **Registration** — Employers obtain a RUC from SUNAT and register workers in the Planilla Electrónica / T-Registro before payroll. Registration is triggered by employing staff, not by a wage threshold. [RESEARCH GAP — no monetary registration threshold found; reviewer to confirm none exists.]  _([cadanapay](https://cadanapay.com/blog/employer-payroll-compliance-in-peru-complete-guide-to-sunat-essalud-afp-onp-and-plame))_

## Section 6 -- Tier 2 catalogue

When payslip/bank data is ambiguous or client circumstances are unclear, flag these for reviewer confirmation.

### T2-1 — Pension regime not evidenced

**Trigger:** A deduction appears but it is unclear whether the worker is ONP or AFP.

**Issue:** 13% (ONP) vs ~12.84%–13.06% (AFP) — a meaningful difference, and the AFP components are not deductible the same way. Cannot assume.

**Action:** Flag for reviewer; request AFPnet/ONP affiliation evidence.

### T2-2 — High earner near the RMA ceiling

**Trigger:** Monthly remuneration approaches or exceeds the RMA (~PEN 12,200–12,600).

**Issue:** The 1.37% prima is capped at the RMA, which changes quarterly; the 10% and commission are not capped. A stale RMA produces a wrong figure.

**Action:** Re-verify the current-quarter RMA on the SBS page. Flag for reviewer. [RESEARCH GAP — exact RMA per quarter.]

### T2-3 — EPS (private health plan) credit

**Trigger:** Employer offers an EPS plan alongside EsSalud.

**Issue:** Up to 25% of the EsSalud obligation is credited to the EPS (~2.25% redirected, ~6.75% still to EsSalud). The split depends on the plan.

**Action:** Flag for reviewer; confirm the EPS contract and the credited percentage.

### T2-4 — Multiple employers / additional deductions

**Trigger:** Worker has more than one employer, or wants to claim the additional 3-UIT expenses.

**Issue:** Withholding by a single employer will under- or over-state the annual liability; an annual return may be required.

**Action:** Flag for reviewer; an annual Declaración Jurada may be due.

### T2-5 — Non-domiciled / split-year residency

**Trigger:** Foreign worker, partial-year presence, or treaty claim.

**Issue:** Flat 30% with no exemption applies to non-domiciled; residency determination and treaty relief are case-specific.

**Action:** Flag for reviewer. Do not apply the 7-UIT exemption until residency is confirmed.

### T2-6 — CTS / gratificaciones exact base

**Trigger:** Request for the exact CTS or gratificación amount.

**Issue:** Base includes 1/6 of the gratificación (for CTS), family allowance, average variable pay, and months of service.

**Action:** Explain framework only; reviewer confirms the deposit against payslips.

## Section 7 -- Excel working paper template

When producing a Peru payroll/contribution computation, structure the working paper as follows:

```
PERU PAYROLL & CONTRIBUTIONS -- WORKING PAPER
Client / Employee: [name]
Tax Year: [year]   UIT: PEN [5,350 (2025) / 5,500 (2026)]   RMV: PEN 1,130
Prepared: [date]

INPUT DATA
  Residency:                     [Domiciled / Non-domiciled]
  Gross monthly remuneration:    PEN [____]
  Pension regime:                [ONP / AFP]
  If AFP — which AFP:            [Habitat / Integra / Prima / Profuturo]
  If AFP — commission regime:    [Flujo / Mixta]
  EPS plan in place:             [YES/NO]

MONTHLY CONTRIBUTIONS
  Base for EsSalud (max(rem,RMV)): PEN [____]
  EsSalud 9% (EMPLOYER):           PEN [____]
  ONP 13% (EMPLOYEE)  -- if ONP:   PEN [____]
  AFP mandatory 10%   -- if AFP:   PEN [____]
  AFP prima 1.37% (≤RMA)-- if AFP: PEN [____]
  AFP commission %    -- if AFP:   PEN [____]
  Total employee pension deduction: PEN [____]

INCOME TAX (5TH CATEGORY) -- ANNUAL PROJECTION (residents)
  Annual gross employment income:  PEN [____]
  Less 7 UIT exemption:            PEN [____]
  Less up to 3 UIT documented exp: PEN [____]
  Annual taxable base:             PEN [____]
  Bracket 1  8%  (0–5 UIT):        PEN [____]
  Bracket 2  14% (5–20 UIT):       PEN [____]
  Bracket 3  17% (20–35 UIT):      PEN [____]
  Bracket 4  20% (35–45 UIT):      PEN [____]
  Bracket 5  30% (>45 UIT):        PEN [____]
  Annual income tax:               PEN [____]
  Monthly withholding (÷12 approx):PEN [____]

NET PAY (monthly, employee)
  Gross:                           PEN [____]
  Less pension (ONP or AFP):       PEN [____]
  Less income tax withheld:        PEN [____]
  Net pay:                         PEN [____]

EMPLOYER-BORNE COSTS
  EsSalud 9%:                      PEN [____]
  CTS (twice yearly):              PEN [____]  [reviewer to confirm base]
  Gratificaciones (Jul & Dec):     PEN [____]  [reviewer to confirm base]

REVIEWER FLAGS / RESEARCH GAPS
  [List Tier 2 flags, RMA quarter, penalties, etc.]
```

## Section 8 -- Bank statement reading guide

### How Peru payroll/contribution debits appear

**BCP (Banco de Crédito del Perú):**
- SUNAT: "SUNAT PAGO", "PAGO PLAME", "TRIBUTOS SUNAT" — monthly, ≈14th–24th of the following month
- Payroll: "TELECREDITO HABERES", "ABONO DE HABERES" — net wages out
- CTS: "CTS DEPOSITO" — May and November

**BBVA Perú:**
- "AFPNET", "AFP [name]", "SUNAT", "PAGO DE PLANILLA"

**Interbank / Scotiabank Perú:**
- "PAGO HABERES", "SUNAT TRIBUTOS", "AFPNET", "CTS"

**Key identification tips:**
1. SUNAT debits cover renta 5ta + EsSalud + ONP together (via PLAME) — one payment, multiple obligations.
2. AFP deductions are remitted separately via AFPnet (not bundled into the SUNAT payment).
3. EsSalud is an employer cost (9%); ONP/AFP are employee deductions withheld then remitted.
4. CTS and gratificaciones are employer labour costs, NOT social contributions — twice-yearly (CTS) and July/December (gratis).
5. Inbound "PENSION ONP/AFP" credits are pension income received, not contributions paid.

### Spanish terminology quick guide

**Spanish terminology quick guide table**

| Term | Meaning |
| --- | --- |
| Remuneración / haberes | Salary / wages |
| Boleta de pago | Payslip |
| Planilla | Payroll |
| Descuentos | Deductions |
| Aporte obligatorio | Mandatory (10%) AFP contribution |
| Comisión | AFP administration fee |
| Prima de seguro | AFP disability/survivor insurance premium (1.37%) |
| Renta de quinta categoría | Fifth-category (employment) income tax |
| Gratificación / aguinaldo | Statutory bonus (July & December) |
| CTS | Compensación por Tiempo de Servicios (severance fund) |
| RMV | Remuneración Mínima Vital (minimum wage) |
| UIT | Unidad Impositiva Tributaria (tax indexing unit) |

## Section 9 -- Onboarding fallback

If the client provides only a bank statement and no other information:

1. **Scan for SUNAT debits** — identify monthly "SUNAT / PLAME / 0601" payments; these bundle renta 5ta + EsSalud + ONP.
2. **Scan for AFPnet debits** — separate from SUNAT; indicates AFP-affiliated employees.
3. **Infer the pension regime mix:** if AFPnet debits exist → some/all staff in AFP; if ONP appears in PLAME only → ONP staff. Do not assume a single regime across all employees.
4. **Identify CTS (May/Nov) and gratificaciones (Jul/Dec)** as employer benefit costs, not contributions.
5. **Flag for reviewer:** "Contribution split derived from bank statement descriptions only. Pension regime per employee, residency status, UIT/RMV year, and the RMA ceiling have not been independently verified. Reviewer must confirm before relying on any figure."

## Section 10 -- Reference material

### Contribution & rate summary (2026)

**Contribution & rate summary (2026)**

| Item | Rate | Borne by | Source |
| --- | --- | --- | --- |
| EsSalud (health) | 9% (min base RMV, no cap) | Employer | [PwC, other taxes](https://taxsummaries.pwc.com/peru/individual/other-taxes) |
| ONP (public pension) | 13% | Employee | [PwC, other taxes](https://taxsummaries.pwc.com/peru/individual/other-taxes) |
| AFP mandatory | 10% | Employee | [AFP Habitat](https://www.afphabitat.com.pe/aprende-de-prevision/cuanto-te-cobra-tu-afp-descuentos-comisiones-y-seguro/) |
| AFP prima (≤RMA) | 1.37% | Employee | [Misha](https://misha.pe/laboral/prima-seguro-afp/) |
| AFP commission (flujo) | 1.47%–1.69% | Employee | [TrámitesPerú](https://tramitesperu.com/comparadores/afp-comisiones/) |
| AFP total (flujo) | 12.84%–13.06% | Employee | derived (10 + 1.37 + commission) |

### Income tax brackets (residents, by UIT)

**Income tax brackets (residents, by UIT)**

| Bracket | UIT range | Rate | Source |
| --- | --- | --- | --- |
| 1 | Up to 5 UIT | 8% | [PwC](https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income) |
| 2 | 5–20 UIT | 14% | [PwC](https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income) |
| 3 | 20–35 UIT | 17% | [PwC](https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income) |
| 4 | 35–45 UIT | 20% | [PwC](https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income) |
| 5 | Over 45 UIT | 30% | [PwC](https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income) |

- **Non-domiciled note** — Non-domiciled: flat 30%, no exemption ([PwC](https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income)).  _([PwC](https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income))_

### Key indexing values

**Key indexing values table**

| Value | 2025 | 2026 | Source |
| --- | --- | --- | --- |
| UIT | PEN 5,350 | PEN 5,500 | [PwC](https://taxsummaries.pwc.com/peru/individual/taxes-on-personal-income) |
| 7-UIT exemption | PEN 37,450 | PEN 38,500 | derived (7 × UIT) |
| RMV (minimum wage) | PEN 1,130 (from 1 Jan 2025) | PEN 1,130 | [Andina](https://andina.pe/agencia/noticia-remuneracion-minima-vital-sube-a-1130-soles-a-partir-del-1-enero-2025-1012953.aspx) |

### Employer-borne benefits

**Employer-borne benefits table**

| Benefit | Detail | Source |
| --- | --- | --- |
| CTS | ~9.72% of annual salary, deposited by 15 May & 15 Nov; base includes 1/6 of gratificación | [EY Peru](https://www.ey.com/es_pe/insights/workforce/cts), [Serviap](https://www.serviapgroup.com/blog/cts-payment-in-peru-2025/) |
| Gratificaciones | Two per year (July Fiestas Patrias, December Navidad), ≈ one month's salary each, prorated if <6 months | [Serviap](https://www.serviapgroup.com/blog/cts-payment-in-peru-2025/), [Rivermate](https://rivermate.com/guides/peru/benefits) |

### Penalties

[RESEARCH GAP — reviewer to confirm.] A precise, authority-published penalty schedule (UIT-multiples / interest for late PLAME filing, late contribution payment, or CTS non-deposit) was NOT obtained from SUNAT or a Big-4 source for this skill. Verify directly against SUNAT's Código Tributario Tabla de Infracciones y Sanciones and SUNAFIL's labour-fine schedule before quoting any figure. Do not invent penalty numbers.

### Worked tax computation (resident, 2026, UIT = 5,500)

Annual gross employment income PEN 150,000:
- Less 7 UIT (38,500) = 111,500 taxable base (no additional 3-UIT expenses claimed)
- Bracket 1: 27,500 × 8% = 2,200.00
- Bracket 2: (110,000 − 27,500 = 82,500) × 14% = 11,550.00
- Bracket 3: (111,500 − 110,000 = 1,500) × 17% = 255.00
- **Annual income tax = 2,200.00 + 11,550.00 + 255.00 = PEN 14,005.00** ✓

### Test suite

**Test 1 — EsSalud, PEN 6,000 salary, 2026.** 6,000 × 9% = **PEN 540.00** (employer). RMV min base not binding.

**Test 2 — EsSalud, PEN 900 salary (below RMV).** Base = max(900, 1,130) = 1,130; 1,130 × 9% = **PEN 101.70** (employer).

**Test 3 — ONP, PEN 4,000 salary.** 4,000 × 13% = **PEN 520.00** (employee deduction).

**Test 4 — AFP Habitat (flujo), PEN 4,000 salary.** 10% = 400.00; prima 1.37% = 54.80; commission 1.47% = 58.80; total 12.84% = **PEN 513.60** (400 + 54.80 + 58.80 = 513.60 ✓).

**Test 5 — AFP Profuturo (flujo), PEN 4,000 salary.** 10% = 400.00; prima 1.37% = 54.80; commission 1.69% = 67.60; total 13.06% = **PEN 522.40** (400 + 54.80 + 67.60 = 522.40 ✓).

**Test 6 — Resident income tax, annual income PEN 38,500 (2026).** Less 7 UIT (38,500) = 0 taxable base. **Income tax = PEN 0.00** (income equals the exemption).

**Test 7 — Resident income tax, annual income PEN 60,000 (2026).** Less 7 UIT (38,500) = 21,500 base. All within bracket 1 (≤27,500): 21,500 × 8% = **PEN 1,720.00**.

**Test 8 — Non-domiciled, monthly Peruvian-source salary PEN 10,000.** Flat 30%, no exemption: 10,000 × 30% = **PEN 3,000.00** withheld.

**Test 9 — Net pay, ONP member, PEN 5,000 salary, 2026 (illustrative).** Gross 5,000 − ONP 650.00 (13%) − monthly income tax. Annual income 60,000 → annual tax 1,720.00 (Test 7) → ≈ 143.33/month. Net ≈ 5,000 − 650.00 − 143.33 = **PEN 4,206.67**. (Employer separately pays EsSalud 450.00.)

**Test 10 — Pension regime unknown.** STOP. Refuse per R-PE-1; cannot pick 13% vs ~12.84%–13.06%.

### Prohibitions

- NEVER compute a pension deduction without confirming ONP vs AFP — they are mutually exclusive and differ.
- NEVER charge both ONP and AFP to the same worker.
- NEVER apply the 1.37% prima above the RMA without re-verifying the current-quarter RMA on the SBS page.
- NEVER apply the 7-UIT exemption to a non-domiciled individual — they pay flat 30% with no exemption.
- NEVER use a stale UIT — confirm the tax year (2025 = 5,350; 2026 = 5,500).
- NEVER treat EsSalud as an employee deduction — it is an employer cost.
- NEVER quote a Peru penalty figure from this skill — none was authoritatively sourced; escalate.
- NEVER state an exact CTS or gratificación deposit without the reviewer confirming the computation base.
- NEVER present any figure as definitive — label as estimated and direct the client to SUNAT/AFPnet/payslip records.
- NEVER confuse inbound pension income (PENSION ONP/AFP credits) with outbound contributions.

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a contador público colegiado, CPA, EA, tax attorney, or equivalent licensed practitioner in your jurisdiction) before filing or acting upon.

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
