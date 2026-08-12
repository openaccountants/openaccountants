---
name: uruguay-payroll
description: "Use this skill whenever asked about Uruguay payroll processing for employed persons. Trigger on phrases like \"Uruguay payroll\", \"Uruguayan payroll\", \"nómina Uruguay\", \"planilla de trabajo\", \"BPS Uruguay\", \"Banco de Previsión Social\", \"aporte jubilatorio\", \"montepío\", \"15% BPS\", \"7.5% patronal\", \"FONASA Uruguay\", \"FRL Uruguay\", \"Fondo de Reconversión Laboral\", \"IRPF Uruguay\", \"IRPF Categoría II\", \"rentas de trabajo\", \"retención IRPF\", \"BPC Uruguay\", \"Base de Prestaciones y Contribuciones\", \"mínimo no imponible\", \"MNIG\", \"salario mínimo nacional Uruguay\", \"minimum wage Uruguay\", \"aguinaldo Uruguay\", \"ajuste anual IRPF\", \"DGI Uruguay\", \"net salary Uruguay\", \"salario líquido\", \"salario nominal\", \"gross to net Uruguay\", \"employer contribution Uruguay\", \"tope de cotización\", \"Formulario 1102\", or any question about computing employee pay, IRPF withholding, or social-security (BPS) contributions for Uruguay-based employees. CRITICAL STRUCTURAL FACT: unlike many Latin-American jurisdictions, in Uruguay the employer IS an IRPF withholding agent on dependent salaries — IRPF (Categoría II) is withheld monthly on a progressive scale and reconciled by a year-end ajuste anual, on top of mandatory BPS contributions. This skill covers IRPF withholding, BPS contributions (jubilatorio, FONASA, FRL, FGCL), the retirement contribution ceiling, the minimum wage, the IRPF annual sworn declaration, and filing/payslip obligations. ALWAYS read this skill before processing any Uruguay payroll."
version: 0.1
jurisdiction: UY
tax_year: 2025
last_updated: 2026-07-13
review_status: pending_review
depends_on: - payroll-workflow-base
category: payroll
tier: 2
license: AGPL-3.0-or-later (code) / OpenAccountants Guide License v1.0 (content)
---

# Uruguay Payroll Skill v0.1 (Tier 2 — research-verified, reviewer sign-off pending)

## Uruguay Payroll Skill v0.1 (Tier 2 — research-verified, reviewer sign-off pending)

> **Tier 2 status.** Every rate, threshold, and deadline below is sourced to a named authority (BPS, DGI, IMPO) or a Big-4 summary (PwC Worldwide Tax Summaries) or a named advisory (EY Uruguay) and cited inline. It has **not** yet been section-by-section verified by a licensed Uruguayan accountant (contador público). Items marked **[RESEARCH GAP — reviewer to confirm]** carry residual uncertainty and must be confirmed against primary sources before reliance.

> **READ THIS FIRST — the single most important structural fact.** Uruguay **does** levy a personal income tax on labour income (**IRPF — Impuesto a la Renta de las Personas Físicas, Categoría II / rentas de trabajo**), and — unlike Paraguay or many other LATAM jurisdictions — **the employer IS the withholding agent.** IRPF is **withheld monthly** on a progressive 0%–36% scale and reconciled at year end via the **ajuste anual** performed through BPS. On top of IRPF the employer also withholds and pays **BPS** social-security contributions (retirement/montepío, FONASA, FRL). Almost every IRPF threshold is expressed in units of the **BPC** (Base de Prestaciones y Contribuciones); for 2025 **BPC = UYU 6,576/month**. See Section 2.

## Section 1 -- Quick Reference

**Section 1 Quick Reference table**

| Field | Value |
| --- | --- |
| Country | Uruguay (Oriental Republic of Uruguay) |
| Currency | UYU (Uruguayan peso, "$") only |
| Standard pay frequency | Monthly |
| Tax year | Calendar year (1 January -- 31 December) |
| Income-tax withholding on salaries | **Yes — employer withholds IRPF Categoría II monthly** on a progressive scale, with a year-end ajuste anual (BPS Comunicado R 2/2025; DGI) |
| Reference unit | **BPC = UYU 6,576/month** for 2025 (+4.38% over 2024) (BPS Comunicado R 2/2025) |
| IRPF non-taxable minimum (MNIG) | **UYU 46,032/month** (= 7 BPC); first peso above this is taxed (BPS Comunicado R 2/2025) |
| IRPF scale | Progressive **0% – 36%** across 8 monthly brackets (BPS Comunicado R 2/2025) |
| Employee retirement (jubilatorio/montepío) | **15%** of nominal salary, withheld by employer (BPS Tasas; PwC) |
| Employer retirement (patronal) | **7.5%** of nominal salary (general private-sector rate) (BPS Tasas; PwC) |
| FONASA (health) | Employer **5%** flat; employee **3%–8%** by income & family situation (BPS Tasas Fonasa; PwC) |
| FRL (Fondo de Reconversión Laboral) | **0.1%** employee + **0.1%** employer (BPS Tasas; PwC) |
| FGCL (labour-credit guarantee) | **0.025%** employer only (BPS Tasas; PwC) |
| Retirement contribution ceiling | Retirement contributions apply only up to **UYU 272,564/month** (until 31 Dec 2025) (PwC Other taxes; BPS Topes de cotización) |
| Minimum wage (from 1 Jan 2025) | **UYU 23,604/month** (+6%) (Decreto N° 369/024, IMPO) |
| Tax authority (IRPF) | **DGI** — Dirección General Impositiva |
| Social-security authority | **BPS** — Banco de Previsión Social (also IRPF withholding calculator/agent for employees) |
| IRPF annual sworn declaration | **Form 1102** (individual) / **Form 1103** (family unit) — most single-employer employees do NOT file (employer ajuste anual instead) (EY Uruguay) |
| Filing portals | DGI (servicios en línea); BPS (nómina / GAFI) |
| Validated by | Pending — requires sign-off by a licensed Uruguayan accountant (contador público) |
| Skill version | 0.1 (Tier 2) |

## Section 2 -- Income Tax Withholding (IRPF Categoría II — employer-withheld)

Uruguay levies **IRPF (Impuesto a la Renta de las Personas Físicas), Categoría II — rentas de trabajo**, on labour income. The employer **IS** the withholding agent and withholds IRPF **monthly** on the progressive scale below, reconciling over the year via the **ajuste anual** through BPS. (Source: BPS Comunicado R 2/2025 "IRPF Ejercicio 2025: Valores Mensuales", official, vigencia 1/2025.)

### 2.1 Monthly progressive income scale (escala mensual progresional de rentas), 2025

**Monthly progressive IRPF scale 2025**  _(BPS Comunicado R 2/2025; DGI IRPF Cat. II escalas)_

| Bracket (BPC) | Desde (UYU/month) | Hasta (UYU/month) | Rate | Cumulative tax at top of bracket (UYU) |
| --- | --- | --- | --- | --- |
| Up to 7 BPC | 0 | 46,032 | 0% | 0.00 |
| Over 7–10 BPC | 46,033 | 65,760 | 10% | 1,972.80 |
| Over 10–15 BPC | 65,761 | 98,640 | 15% | 6,904.80 |
| Over 15–30 BPC | 98,641 | 197,280 | 24% | 30,578.40 |
| Over 30–50 BPC | 197,281 | 328,800 | 25% | 63,458.40 |
| Over 50–75 BPC | 328,801 | 493,200 | 27% | 107,846.40 |
| Over 75–115 BPC | 493,201 | 756,240 | 31% | 189,388.80 |
| Over 115 BPC | 756,241 | — | 36% | — |

- **Tax computed bracket-by-bracket** — Tax is computed bracket-by-bracket (progressive marginal), NOT flat. BPC = UYU 6,576.  _(BPS Comunicado R 2/2025; DGI IRPF Cat. II escalas)_
- **General non-taxable minimum (MNIG)** — UYU 46,032/month (= 7 BPC). Below this, no IRPF.  _(BPS Comunicado R 2/2025)_

**Cumulative-tax check (recomputed bracket by bracket):**
- 10% × (65,760 − 46,032) = 10% × 19,728 = **1,972.80** ✓
- + 15% × (98,640 − 65,760) = 15% × 32,880 = 4,932.00 → **6,904.80** ✓
- + 24% × (197,280 − 98,640) = 24% × 98,640 = 23,673.60 → **30,578.40** ✓
- + 25% × (328,800 − 197,280) = 25% × 131,520 = 32,880.00 → **63,458.40** ✓
- + 27% × (493,200 − 328,800) = 27% × 164,400 = 44,388.00 → **107,846.40** ✓
- + 31% × (756,240 − 493,200) = 31% × 263,040 = 81,542.40 → **189,388.80** ✓ (Self-verified.)

- **Annual scale figures (PwC)** — Annual figures (PwC, tax year 2025) are the same scale at 12× monthly: 0% to 552,384; 10% 552,384–789,120; 15% 789,120–1,183,680; 24% 1,183,680–2,367,360; 25% 2,367,360–3,945,600; 27% 3,945,600–5,918,400; 31% 5,918,400–9,074,880; 36% above 9,074,880.  _(PwC — Taxes on personal income)_

Note on the BPC value: PwC's worldwide summary mislabels BPC as "165.50" — that is a currency-conversion artifact, not the BPC. The authoritative value is **UYU 6,576** (BPS Comunicado R 2/2025). This skill uses UYU 6,576.

### 2.2 Deductions mechanism (escala de deducciones), 2025

- **Deductions mechanism overview** — IRPF allows specified deductions, but the tax benefit of deductions is computed on a separate progressive deductions scale and then subtracted from the gross IRPF on income.  _(BPS Comunicado R 2/2025)_

**Fixed monthly deduction-credit rate table**  _(BPS Comunicado R 2/2025)_

| Nominal IRPF income | Deduction credit rate | Source |
| --- | --- | --- |
| ≤ UYU 98,640 (≤ 15 BPC) | **14%** | BPS Comunicado R 2/2025 |
| > UYU 98,640 (> 15 BPC) | **8%** | BPS Comunicado R 2/2025 |

**Deductible items (monthly values, 2025) table**  _(BPS Comunicado R 2/2025)_

| Item | Monthly value (UYU) | Source |
| --- | --- | --- |
| Personal social-security contributions (montepío 15% + FONASA + FRL employee shares) | actual amounts withheld | BPS Comunicado R 2/2025 |
| Dependent minor child | **10,960** per child (= 20 BPC annual / 12) | BPS Comunicado R 2/2025 |
| Dependent child with disability | **21,920** per child (= 40 BPC annual / 12) | BPS Comunicado R 2/2025 |
| Fondo de Solidaridad — Cat.1 / Cat.2 / Cat.3 / Cat.4 / Cat.5 | 274 / 548 / 1,096 / 1,005 / 1,553 | BPS Comunicado R 2/2025 |
| Caja de Profesionales Universitarios (categories 1st–11th) | range 6,447 to 33,855 (11th/special = 3,241) | BPS Comunicado R 2/2025 |
| Option to exclude from withholding regime — importe límite | **65,400** | BPS Comunicado R 2/2025 |

- **IRPF due formula** — The deduction credit is computed as `credit rate × (sum of deductible items)`, then `IRPF due = max(0, gross IRPF on income − deduction credit)`. If the credit exceeds the gross IRPF, IRPF due is zero (it does not create a negative/refundable amount within the monthly withholding).  _(BPS Comunicado R 2/2025)_

### 2.3 IRPF annual sworn declaration (declaración jurada) and the ajuste anual

**Annual sworn declaration / ajuste anual table**  _(EY Uruguay)_

| Item | Detail | Source |
| --- | --- | --- |
| Year-end mechanism for single-employer employees | Employer performs an automatic **ajuste anual** via BPS; refunds typically issued from mid-June | BPS; EY Uruguay |
| Annual filing window (FY2025, filed 2026) | **29 June – 31 August 2026** | Uruguayan tax-advisory sources — **[RESEARCH GAP — reviewer to confirm exact 2026 dates]** |
| Annual filing window (FY2024, for reference) | 7 July – 28 August 2025 | EY Uruguay |
| Forms | **Form 1102** (individual) / **Form 1103** (family unit / núcleo familiar) | EY Uruguay |
| Mandatory filers | Independent workers; employees with multiple employers exceeding 150,000 UI; those electing the family-unit 5% withholding reduction; employees not employed on 31 December | EY Uruguay |
| Payment (if owed) | Up to 5 equal installments (FY2024: first 29 Aug 2025, last 30 Dec 2025) | EY Uruguay |

Most single-employer employees are **NOT** required to file — the employer's ajuste anual settles the year (EY Uruguay).

### 2.4 IRNR (non-resident income tax) — out of scope but flagged

- **IRNR regime for non-residents** — Non-residents are taxed under IRNR on Uruguayan-source gross income at 7%–25% (12% or 25% typical for services; 25% for low/no-tax jurisdictions). IRNR is a distinct regime from the employer IRPF withholding covered here; route IRNR questions to a specialist.  _(PwC — Taxes on personal income)_

## Section 3 -- Social Security (BPS) -- Employee Deductions

Uruguay's mandatory social-security scheme is BPS (Banco de Previsión Social). The employer withholds the employee shares and remits them with the employer shares via the monthly BPS nómina. (Source: BPS Tasas; BPS Tasas Fonasa; PwC — Other taxes, tax year 2025.)

### 3.1 Retirement / pension (Jubilatorio — "montepío")

**Retirement employee rate table**  _(BPS Tasas; PwC)_

| Item | Employee rate | Base | Source |
| --- | --- | --- | --- |
| Retirement (montepío) | **15%** of nominal salary | Nominal salary up to the retirement ceiling (Section 4.4) | BPS Tasas; PwC |

### 3.2 FONASA (national health fund) — variable employee rate

- **FONASA employee variability** — Employee FONASA is 3%–8% by income level and family situation. 2.5 BPC = UYU 16,440 in 2025.  _(BPS Tasas Fonasa; PwC)_

**FONASA employee rate by income and family situation**  _(BPS Tasas Fonasa; PwC)_

| Monthly income | No dependents (single) | Single, with children | With spouse/partner, no children | With spouse/partner + children |
| --- | --- | --- | --- | --- |
| ≤ 2.5 BPC (≤ UYU 16,440) | 3% | 3% | 5% | 5% |
| > 2.5 BPC (> UYU 16,440) | 4.5% | 6% | 6.5% | 8% |

- **Spouse surcharge condition** — The spouse/partner surcharge applies only if the spouse lacks own SNIS coverage.  _(BPS Tasas Fonasa)_
- **FONASA not subject to retirement ceiling** — FONASA is NOT subject to the retirement ceiling — it applies to the full nominal salary.  _(PwC; BPS)_

### 3.3 FRL — Fondo de Reconversión Laboral

**FRL employee rate table**  _(BPS Tasas; PwC)_

| Item | Employee rate | Source |
| --- | --- | --- |
| FRL | **0.1%** of nominal salary | BPS Tasas; PwC |

- **FRL not subject to retirement ceiling** — FRL is NOT subject to the retirement ceiling — it applies to the full nominal salary.  _(PwC; BPS)_

### 3.4 Employee total (illustrative, single, no dependents, > 2.5 BPC, below ceiling)

**Employee total illustrative table**  _(sum of the three rows)_

| Component | Rate | Source |
| --- | --- | --- |
| Retirement (montepío) | 15% | BPS Tasas; PwC |
| FONASA | 4.5% | BPS Tasas Fonasa; PwC |
| FRL | 0.1% | BPS Tasas; PwC |
| **Employee BPS total (this case)** | **19.6%** | sum of the three rows |

**Total-row check (recomputed):** 15 + 4.5 + 0.1 = **19.6** ✓ (Self-verified.) Note the FONASA rate (and hence this total) changes with income band and family situation (Section 3.2).

## Section 4 -- Social Security (BPS) -- Employer Contributions

(Source: BPS Tasas; BPS Tasas Fonasa; PwC — Other taxes, tax year 2025.)

### 4.1 Employer contribution rates (general private sector)

**Employer contribution rates table**  _(BPS Tasas; BPS Tasas Fonasa; PwC)_

| Component | Employer rate | Base | Source |
| --- | --- | --- | --- |
| Retirement (patronal/jubilatorio) | **7.5%** | Nominal salary up to the retirement ceiling (Section 4.4) | BPS Tasas; PwC |
| FONASA | **5%** flat (+ CCM where applicable) | Full nominal salary | BPS Tasas Fonasa; PwC |
| FRL | **0.1%** | Full nominal salary | BPS Tasas; PwC |
| FGCL (Fondo de Garantía de Créditos Laborales) | **0.025%** | Full nominal salary | BPS Tasas; PwC |

- **Civil/public organism note** — Civil/public organisms use different patronal rates; this skill applies the general private-sector 7.5% unless told otherwise.

### 4.2 Employer total (PwC headline)

- **Employer total headline** — PwC states the employer total ≈ 12.625% = 7.5% jubilatorio + 5% FONASA + 0.1% FRL + 0.025% FGCL, before BSE accident insurance and CCM.  _(PwC — Other taxes)_

**Total-row check (recomputed):** 7.5 + 5 + 0.1 + 0.025 = **12.625** ✓ (Self-verified.)

> This 12.625% bundles FONASA at the base 5%. Effective employer cost rises with the Complemento de Cuota Mutual (CCM) and the activity-specific BSE (Banco de Seguros del Estado) workplace-accident premium (mandatory, rate varies by risk class — **[RESEARCH GAP — reviewer to confirm]**, no single national rate).

### 4.3 Combined headline burden (employee illustrative + employer)

**Combined headline burden table**

| Side | Components | Total |
| --- | --- | --- |
| Employee (single, >2.5 BPC, below ceiling) | 15% + 4.5% + 0.1% | **19.6%** |
| Employer (general private sector) | 7.5% + 5% + 0.1% + 0.025% | **12.625%** |

**Total-row check:** employee 15 + 4.5 + 0.1 = 19.6 ✓; employer 7.5 + 5 + 0.1 + 0.025 = 12.625 ✓ (Self-verified.) (Employee total varies with the FONASA band/family situation; this row shows the single, >2.5 BPC, no-dependents case.)

### 4.4 Retirement contribution ceiling (tope de cotización)

**Retirement contribution ceiling table**  _(PwC — Other taxes; BPS Topes de cotización)_

| Item | Detail | Source |
| --- | --- | --- |
| Retirement ceiling | Retirement contributions (employee 15% **and** employer 7.5%) apply **only up to UYU 272,564/month** (until 31 December 2025); salary above this cap is exempt from retirement contribution | PwC — Other taxes; BPS Topes de cotización |
| FONASA / FRL / FGCL | **NOT** subject to the retirement cap — apply to the full nominal salary | PwC; BPS |

### 4.5 AFAP (private pension pillar)

- **AFAP mixed regime description** — Part of the 15% employee retirement contribution is channelled to a private AFAP for workers in the mixed regime, based on income franjas updated annually.

> **[RESEARCH GAP — reviewer to confirm]** The 2025 AFAP income-franja thresholds (allocation between BPS and the private AFAP) were **not** confirmed from a primary BPS "Valores" page in this research. Do **not** publish AFAP allocation thresholds until verified against BPS "Topes de cotización → Valores". This does not affect the **total** 15% employee retirement withholding — only its split.

### 4.6 Payment / filing

**Payment/filing table**  _(BPS)_

| Item | Detail | Source |
| --- | --- | --- |
| Monthly | BPS **nómina** (payroll declaration): employee + employer BPS shares + IRPF withheld | BPS |
| Registration | Any dependent worker triggers mandatory BPS employer registration; no income floor exempts the employer | BPS |

## Section 5 -- Minimum Wage (Salario Mínimo Nacional)

- **Minimum wage authority** — Authority: Executive (Decreto). Current: Decreto N° 369/024, effective 1 January 2025 (+6%).  _(Decreto N° 369/024 (IMPO))_

**Minimum wage 2025 table**  _(Decreto N° 369/024 (IMPO))_

| Item | 2025 value | Source |
| --- | --- | --- |
| Monthly national minimum wage | **UYU 23,604** | Decreto N° 369/024 (IMPO) |

- **Minimum wage below IRPF threshold** — UYU 23,604 is below the IRPF non-taxable minimum of UYU 46,032, so a minimum-wage earner pays no IRPF but still pays BPS contributions (Section 3).

> **[RESEARCH GAP — reviewer to confirm]** Any 2026 minimum-wage adjustment would supersede this from 1/1/2026; use UYU 23,604 as the current authoritative figure until a 2026 decree is published.

## Section 6 -- Conservative Defaults

When inputs are ambiguous, apply these defaults and flag the assumption to the user:

1. **Employer withholds IRPF.** Uruguay's employer IS an IRPF withholding agent — compute monthly IRPF on the progressive scale (Section 2) AND BPS contributions (Sections 3–4). Do not skip IRPF as if it were self-assessed.
2. **Family/FONASA situation = single, no dependents.** Apply FONASA at 3% (≤ 2.5 BPC) or 4.5% (> 2.5 BPC) unless the user states children/spouse (which change the FONASA band and add child deductions). Flag the assumption.
3. **Sector = general private sector.** Employer retirement 7.5%; do not apply civil/public-organism rates without confirmation.
4. **Retirement ceiling applied** at UYU 272,564/month to the 15% employee and 7.5% employer retirement only; FONASA/FRL/FGCL on full nominal salary (Section 4.4).
5. **No deductions beyond personal BPS contributions** unless the user provides them. Apply the deduction-credit rate (14% if nominal income ≤ 98,640, else 8%) to the sum of deductible items (Section 2.2). Do not invent Fondo de Solidaridad / Caja Profesional / mortgage figures.
6. **Currency:** all amounts in **UYU**. Never assume USD or any other currency.
7. **Pay period:** assume **FY2025** figures (BPC 6,576; MNIG 46,032; minimum wage 23,604; retirement ceiling 272,564 until 31 Dec 2025). Do not apply unconfirmed 2026 figures.
8. **AFAP split:** do not state AFAP allocation thresholds — research gap (Section 4.5). The total 15% employee retirement withholding is unaffected.

### 7.1 Required inputs (must have before computing payroll)

**Required inputs table**

| Input | Why needed |
| --- | --- |
| Monthly **nominal** salary in UYU | Drives the IRPF scale, BPS bases, and both contribution sides |
| Family / FONASA situation (single / with children / with spouse w/o SNIS cover) | Selects the FONASA employee band (3%–8%) and child deductions |
| Number of dependent minor children (and any with disability) | Each adds a monthly IRPF deduction (10,960 / 21,920) |
| Employer sector (general private vs civil/public organism) | Confirms the 7.5% patronal rate |
| Pay period (month/year) | Confirms FY2025 BPC, MNIG, minimum wage, and retirement ceiling |
| Whether the employee has multiple employers / elects family-unit regime | Affects annual filing obligation and withholding option |
| Employer registration with BPS | Must be registered before running payroll |

### 7.2 Refusal catalogue — STOP and ask rather than guess

**Refusal catalogue table**

| Situation | Action |
| --- | --- |
| Salary stated in USD or another currency | **Refuse to compute.** Ask for the UYU nominal amount (or the FX basis used). |
| User asks to skip IRPF withholding ("they self-assess") | Do **not** skip. Explain Uruguay's employer IS an IRPF withholding agent (Section 2); compute monthly IRPF and the year-end ajuste anual. |
| FONASA family situation not stated | Default to single/no-dependents and **flag it** — do not silently apply a spouse/children band. |
| Pay period in 2026 or later | Flag that FY2025 figures (BPC 6,576, ceiling 272,564 to 31 Dec 2025) apply until 2026 values are published; do not invent 2026 figures. |
| Civil/public-organism employer | Confirm the patronal rate; do not apply 7.5% blindly. |
| Request for the AFAP split of the 15% retirement | State the total 15% withholding and flag the AFAP franja thresholds as a research gap (Section 4.5). |
| Request for exact DGI/BPS penalty amounts | Flag as a research gap (Section 13) — do not present a precise figure as confirmed. |
| Non-resident employee | IRNR regime (7%–25%, Section 2.4) — out of scope for this employer-withholding skill; route to a specialist. |
| Salary above UYU 272,564 | Apply the retirement ceiling to the 15%/7.5% retirement only; keep FONASA/FRL/FGCL on the full nominal. |

## Section 8 -- Transaction / Payment Pattern Library (deterministic)

**Transaction/payment pattern library table**

| Trigger | Deterministic action |
| --- | --- |
| Nominal salary ≤ 46,032 (7 BPC) | IRPF = 0. Still compute BPS (retirement 15%, FONASA per band, FRL 0.1%). |
| Nominal salary > 46,032 | Compute gross IRPF bracket-by-bracket (Section 2.1), then subtract the deduction credit (Section 2.2); IRPF due = max(0, gross IRPF − credit). |
| Nominal income ≤ 98,640 | Deduction credit rate = 14%. |
| Nominal income > 98,640 | Deduction credit rate = 8%. |
| Nominal income ≤ 16,440 (2.5 BPC) | FONASA employee = 3% (single) / 5% (with spouse w/o SNIS). |
| Nominal income > 16,440 | FONASA employee = 4.5% / 6% / 6.5% / 8% per family situation (Section 3.2). |
| Nominal salary ≤ 272,564 | Retirement base = full nominal (15% employee, 7.5% employer). |
| Nominal salary > 272,564 | Retirement base = 272,564 (cap); FONASA/FRL/FGCL still on full nominal. |
| Each dependent minor child | Add 10,960 to the deductible-items sum (21,920 if disabled). |
| Aguinaldo / sueldo anual complementario | Treat per its own rules — **[RESEARCH GAP — reviewer to confirm]** aguinaldo BPS/IRPF treatment not separately sourced in this pass; do not assume exemption. |
| Bank credit `SUELDO`/`SALARIO` to an employee | Net salary payment. |
| Bank debit to `BPS`/`DGI` | BPS contribution remittance / IRPF remittance. |

## Section 9 -- Worked Examples

All figures in UYU, tax year 2025, **general private sector**. BPC = 6,576; MNIG = 46,032; retirement ceiling = 272,564. Employer withholds IRPF and BPS. Unless stated, the employee is **single, no dependents**. Each line is recomputed end-to-end.

### Example A — Minimum wage, nominal UYU 23,604/month (below MNIG)

23,604 < 46,032 → IRPF = 0. 23,604 > 16,440 → FONASA 4.5% (single).

**Example A table**  _(23,604.00)_

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Nominal salary | — | 23,604.00 |
| Employee retirement | 15% × 23,604 | 3,540.60 |
| Employee FONASA | 4.5% × 23,604 | 1,062.18 |
| Employee FRL | 0.1% × 23,604 | 23.60 |
| Employee BPS total | 3,540.60 + 1,062.18 + 23.60 | 4,626.38 |
| IRPF withheld | nominal < MNIG | 0.00 |
| **Net pay** | 23,604 − 4,626.38 − 0 | **18,977.62** |
| Employer retirement | 7.5% × 23,604 | 1,770.30 |
| Employer FONASA | 5% × 23,604 | 1,180.20 |
| Employer FRL | 0.1% × 23,604 | 23.60 |
| Employer FGCL | 0.025% × 23,604 | 5.90 |
| Employer BPS total | 1,770.30 + 1,180.20 + 23.60 + 5.90 | 2,980.00 |
| **Total employer cost** | 23,604 + 2,980.00 | **26,584.00** |

### Example B — Nominal UYU 60,000/month (just into the 10% IRPF band)

60,000 in 10% band; nominal ≤ 98,640 → deduction credit rate 14%. FONASA 4.5%.

**Example B table**  _(60,000.00)_

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Nominal salary | — | 60,000.00 |
| Employee retirement | 15% × 60,000 | 9,000.00 |
| Employee FONASA | 4.5% × 60,000 | 2,700.00 |
| Employee FRL | 0.1% × 60,000 | 60.00 |
| Employee BPS total (deductible) | 9,000 + 2,700 + 60 | 11,760.00 |
| Gross IRPF on income | 10% × (60,000 − 46,032) = 10% × 13,968 | 1,396.80 |
| Deduction credit | 14% × 11,760 | 1,646.40 |
| IRPF due | max(0, 1,396.80 − 1,646.40) | 0.00 |
| **Net pay** | 60,000 − 11,760 − 0 | **48,240.00** |
| Employer BPS | 12.625% × 60,000 | 7,575.00 |
| **Total employer cost** | 60,000 + 7,575.00 | **67,575.00** |

The deduction credit (1,646.40) exceeds the gross IRPF (1,396.80), so IRPF due is 0 (no negative/refund within monthly withholding).

### Example C — Nominal UYU 120,000/month (24% band, non-zero IRPF)

120,000 in 24% band; nominal > 98,640 → deduction credit rate 8%. FONASA 4.5%.

**Example C table**  _(120,000.00)_

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Nominal salary | — | 120,000.00 |
| Employee retirement | 15% × 120,000 | 18,000.00 |
| Employee FONASA | 4.5% × 120,000 | 5,400.00 |
| Employee FRL | 0.1% × 120,000 | 120.00 |
| Employee BPS total (deductible) | 18,000 + 5,400 + 120 | 23,520.00 |
| Gross IRPF on income | 6,904.80 + 24% × (120,000 − 98,640) = 6,904.80 + 24% × 21,360 | 12,031.20 |
| Deduction credit | 8% × 23,520 | 1,881.60 |
| IRPF due | 12,031.20 − 1,881.60 | 10,149.60 |
| **Net pay** | 120,000 − 23,520 − 10,149.60 | **86,330.40** |
| Employer BPS | 12.625% × 120,000 | 15,150.00 |
| **Total employer cost** | 120,000 + 15,150.00 | **135,150.00** |

### Example D — Nominal UYU 300,000/month (retirement ceiling bites; 25% band)

300,000 > 272,564 → retirement on 272,564; FONASA/FRL/FGCL on full 300,000. 25% IRPF band; credit rate 8%.

**Example D table**  _(300,000.00)_

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Nominal salary | — | 300,000.00 |
| Retirement base (capped) | min(300,000, 272,564) | 272,564.00 |
| Employee retirement | 15% × 272,564 | 40,884.60 |
| Employee FONASA | 4.5% × 300,000 | 13,500.00 |
| Employee FRL | 0.1% × 300,000 | 300.00 |
| Employee BPS total (deductible) | 40,884.60 + 13,500 + 300 | 54,684.60 |
| Gross IRPF on income | 30,578.40 + 25% × (300,000 − 197,280) = 30,578.40 + 25% × 102,720 | 56,258.40 |
| Deduction credit | 8% × 54,684.60 | 4,374.77 |
| IRPF due | 56,258.40 − 4,374.77 | 51,883.63 |
| **Net pay** | 300,000 − 54,684.60 − 51,883.63 | **193,431.77** |
| Employer retirement | 7.5% × 272,564 | 20,442.30 |
| Employer FONASA | 5% × 300,000 | 15,000.00 |
| Employer FRL | 0.1% × 300,000 | 300.00 |
| Employer FGCL | 0.025% × 300,000 | 75.00 |
| Employer BPS total | 20,442.30 + 15,000 + 300 + 75 | 35,817.30 |
| **Total employer cost** | 300,000 + 35,817.30 | **335,817.30** |

### Example E — Nominal UYU 120,000/month, single with 1 minor child

Single with children, > 2.5 BPC → FONASA 6%. One child deduction = 10,960. Credit rate 8% (income > 98,640).

**Example E table**  _(120,000.00)_

| Line | Computation | Amount (UYU) |
| --- | --- | --- |
| Nominal salary | — | 120,000.00 |
| Employee retirement | 15% × 120,000 | 18,000.00 |
| Employee FONASA | 6% × 120,000 | 7,200.00 |
| Employee FRL | 0.1% × 120,000 | 120.00 |
| Employee BPS total | 18,000 + 7,200 + 120 | 25,320.00 |
| Deductible-items sum | 25,320 (BPS) + 10,960 (1 child) | 36,280.00 |
| Gross IRPF on income | 6,904.80 + 24% × (120,000 − 98,640) | 12,031.20 |
| Deduction credit | 8% × 36,280 | 2,902.40 |
| IRPF due | 12,031.20 − 2,902.40 | 9,128.80 |
| **Net pay** | 120,000 − 25,320 − 9,128.80 | **85,551.20** |
| Employer BPS | 12.625% × 120,000 | 15,150.00 |
| **Total employer cost** | 120,000 + 15,150.00 | **135,150.00** |

Versus Example C (same salary, no child, FONASA 4.5%): the child deduction and FONASA band change net pay from 86,330.40 to 85,551.20 — the higher FONASA (6% vs 4.5%) outweighs the extra child deduction at this income.

### Example F — IRPF scale verification (reference)

Gross IRPF on income only (before deduction credit), at each bracket top, must match Section 2.1:

**Example F table**

| Nominal income | Gross IRPF | Recomputation |
| --- | --- | --- |
| 65,760 | 1,972.80 | 10% × (65,760 − 46,032) |
| 98,640 | 6,904.80 | 1,972.80 + 15% × 32,880 |
| 197,280 | 30,578.40 | 6,904.80 + 24% × 98,640 |
| 328,800 | 63,458.40 | 30,578.40 + 25% × 131,520 |
| 493,200 | 107,846.40 | 63,458.40 + 27% × 164,400 |
| 756,240 | 189,388.80 | 107,846.40 + 31% × 263,040 |

(Self-verified — matches the cumulative column in Section 2.1.)

## Section 10 -- Tier 1 Rules (deterministic — apply mechanically)

- **Employer as IRPF withholding agent** — The employer IS an IRPF withholding agent on dependent salaries — withhold IRPF monthly on the progressive scale and reconcile via the ajuste anual  _(BPS Comunicado R 2/2025; DGI)_
- **BPC (2025)** — UYU 6,576/month  _(BPS Comunicado R 2/2025)_
- **MNIG (2025)** — UYU 46,032/month (7 BPC); first peso above MNIG is taxed  _(BPS Comunicado R 2/2025)_

**IRPF scale (monthly)**  _(BPS Comunicado R 2/2025)_

| Band | Rate |
| --- | --- |
| 0 to 46,032 | 0% |
| to 65,760 | 10% |
| to 98,640 | 15% |
| to 197,280 | 24% |
| to 328,800 | 25% |
| to 493,200 | 27% |
| to 756,240 | 31% |
| above 756,240 | 36% |

- **IRPF due formula** — IRPF due = max(0, gross IRPF on income − deduction credit). Credit rate = 14% if nominal income ≤ 98,640, else 8%  _(BPS Comunicado R 2/2025)_
- **Deductible items** — Deductible items include personal BPS contributions plus 10,960/child (21,920 if disabled) and other listed items (Section 2.2)  _(BPS Comunicado R 2/2025)_
- **Employee BPS rates** — retirement 15% + FONASA 3%–8% (by income band & family) + FRL 0.1%  _(BPS Tasas; BPS Tasas Fonasa; PwC)_
- **Employer BPS rates (general private)** — retirement 7.5% + FONASA 5% + FRL 0.1% + FGCL 0.025% = 12.625% before BSE/CCM  _(BPS Tasas; PwC)_
- **Retirement contribution ceiling** — Retirement contributions (15% + 7.5%) apply only up to UYU 272,564/month (until 31 Dec 2025); FONASA/FRL/FGCL on full nominal  _(PwC; BPS Topes de cotización)_
- **Minimum wage** — UYU 23,604/month from 1 Jan 2025. A min-wage earner pays no IRPF but pays BPS.  _(Decreto N° 369/024)_
- **Year-end ajuste anual** — Year-end: employer ajuste anual settles most single-employer employees; Form 1102/1103 filed only by mandatory filers  _(EY Uruguay)_
- **Currency requirement** — All payroll amounts in UYU — never another currency.
- **Total employee retirement withholding** — The total employee retirement withholding is 15% regardless of the (unconfirmed) AFAP split (Section 4.5).

## Section 11 -- Tier 2 Catalogue (reviewer judgement required)

These items require a licensed Uruguayan accountant's judgement and/or confirmation against primary sources before reliance.
1. **AFAP income-franja thresholds (2025)** (Section 4.5) — the split of the 15% retirement between BPS and the private AFAP was not confirmed from a primary BPS "Valores" page.
2. **Exact 2026 IRPF annual-filing dates** (Section 2.3) — the 29 Jun–31 Aug 2026 window is from advisory sources, not yet a primary DGI calendar.
3. **BSE workplace-accident insurance premium** (Section 4.2) — varies by activity/risk class; no single national rate.
4. **CCM (Complemento de Cuota Mutual)** — when and how it adds to employer FONASA cost.
5. **Aguinaldo (sueldo anual complementario) treatment** for BPS/IRPF (Section 8) — not separately sourced in this pass.
6. **Exact DGI/BPS penalty percentages and minimum fines for 2025** (Section 13).
7. **Civil/public-organism patronal rates** — differ from the 7.5% general private-sector rate used here.

## Section 12 -- Filing Obligations

### 12.1 Monthly — BPS nómina + IRPF remittance

**BPS nómina table**  _(BPS)_

| Item | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| BPS **nómina** (payroll declaration) | Declare and pay employee + employer BPS shares and IRPF withheld | Per BPS monthly calendar — **[RESEARCH GAP — reviewer to confirm exact monthly due date]** | BPS |

### 12.2 Annual — IRPF declaración jurada (employee's own filing, where required)

**Annual IRPF declaración jurada table**  _(EY Uruguay)_

| Form | Purpose | Deadline | Source |
| --- | --- | --- | --- |
| **Form 1102** (individual) / **Form 1103** (family unit) | Annual IRPF sworn declaration for mandatory filers | FY2025: **29 Jun – 31 Aug 2026** — **[RESEARCH GAP — reviewer to confirm exact dates]** | EY Uruguay |

Most single-employer employees do NOT file — the employer's ajuste anual settles the year, with refunds typically from mid-June (EY Uruguay).
Mandatory filers: independent workers; employees with multiple employers > 150,000 UI; family-unit electors; employees not employed on 31 December (EY Uruguay).

## Section 13 -- Penalties

Specific 2025 penalty amounts were **not** retrieved from a primary DGI source in this research pass.

**Penalties table**  _(DGI; Código Tributario (IMPO); BPS)_

| Penalty | Detail | Source |
| --- | --- | --- |
| Mora (late payment) | Recargos plus interest under the general regime (Código Tributario / Título 1) — **[RESEARCH GAP — reviewer to confirm exact percentages]** | DGI; Código Tributario (IMPO) |
| Multa por mora | Typically 5% / 10% / 20% of the tax depending on lateness — **[RESEARCH GAP — reviewer to confirm]** | DGI; Código Tributario (IMPO) |
| Contravención / defraudación | Fines under the general regime — **[RESEARCH GAP — reviewer to confirm exact amounts]** | DGI; Código Tributario (IMPO) |
| BPS Mora Patronal | Employer default surcharges under BPS rules — **[RESEARCH GAP — reviewer to confirm]** | BPS |

Authoritative starting point: DGI (gub.uy/direccion-general-impositiva) and the Código Tributario via IMPO. Do not state exact penalty figures as confirmed.

## Section 14 -- Excel Working Paper Template

Reproduce this layout in a single worksheet (one column per employee, or one row per employee for a register). All cells in UYU. FY2025 constants: BPC 6,576; MNIG 46,032; retirement ceiling 272,564.

**Excel working paper template table**

| Row | Label | Formula / source |
| --- | --- | --- |
| 1 | Employee name | input |
| 2 | Pay period (month/year) | input |
| 3 | Nominal salary | input |
| 4 | FONASA employee rate (decimal) | input (0.03 / 0.045 / 0.05 / 0.06 / 0.065 / 0.08 per Section 3.2) |
| 5 | Dependent minor children (count) | input |
| 6 | Children with disability (count) | input |
| 7 | Retirement base (capped) | `=MIN(B3,272564)` |
| 8 | Employee retirement | `=B7*0.15` |
| 9 | Employee FONASA | `=B3*B4` |
| 10 | Employee FRL | `=B3*0.001` |
| 11 | **Employee BPS total (deductible)** | `=B8+B9+B10` |
| 12 | Gross IRPF on income | progressive on B3 per Section 2.1 (see note) |
| 13 | Deductible-items sum | `=B11 + B5*10960 + B6*21920` |
| 14 | Deduction credit rate | `=IF(B3<=98640,0.14,0.08)` |
| 15 | Deduction credit | `=B13*B14` |
| 16 | **IRPF due** | `=MAX(0,B12-B15)` |
| 17 | **Net pay** | `=B3-B11-B16` |
| 18 | Employer retirement | `=B7*0.075` |
| 19 | Employer FONASA | `=B3*0.05` |
| 20 | Employer FRL | `=B3*0.001` |
| 21 | Employer FGCL | `=B3*0.00025` |
| 22 | **Employer BPS total** | `=B18+B19+B20+B21` |
| 23 | **Total employer cost** | `=B3+B22` |
| 24 | Monthly BPS remittance | `=B11+B22` (employee + employer BPS) |

- **Row 12 gross IRPF helper formula** — =IF(B3<=46032,0, IF(B3<=65760,(B3-46032)*0.1, IF(B3<=98640,1972.8+(B3-65760)*0.15, IF(B3<=197280,6904.8+(B3-98640)*0.24, IF(B3<=328800,30578.4+(B3-197280)*0.25, IF(B3<=493200,63458.4+(B3-328800)*0.27, IF(B3<=756240,107846.4+(B3-493200)*0.31, 189388.8+(B3-756240)*0.36)))))))

Cross-check against Example C (nominal 120,000, FONASA 4.5%, no children): row 7 = 120,000; row 8 = 18,000; row 9 = 5,400; row 10 = 120; row 11 = 23,520; row 12 = 12,031.20; row 13 = 23,520; row 14 = 0.08; row 15 = 1,881.60; row 16 = 10,149.60; row 17 = 86,330.40; row 22 = 15,150; row 23 = 135,150. ✓ Matches Example C exactly.

## Section 15 -- Bank Statement / Terminology Reading Guide

Common Uruguayan payroll terms (Spanish → English) and typical bank-statement patterns. Match on the **uppercased** description.

### 15.1 Salary credits (to employees)

**Salary credits table**

| Pattern (UYU bank statement) | Classification |
| --- | --- |
| `SUELDO`, `SALARIO`, `HABERES`, `LIQUIDO` | Net salary payment (salario líquido) |
| `PAGO NOMINA`, `TRANSFERENCIA SUELDO`, `ACREDITACION SUELDO` | Net salary payment |
| `AGUINALDO`, `SUELDO ANUAL COMPLEMENTARIO`, `SAC` | Aguinaldo / 13th salary (treatment flagged — Section 8) |
| `ADELANTO`, `ANTICIPO DE SUELDO` | Salary advance — reconcile against month-end net |
| `PARTIDA`, `PRIMA`, `INCENTIVO` | Bonus / allowance — review IRPF & BPS-base inclusion |
| `DEVOLUCION IRPF`, `AJUSTE ANUAL` | IRPF year-end refund/adjustment — not new income |

### 15.2 Employer debits to the State (BPS / DGI)

**Employer debits to the state table**

| Pattern | Classification |
| --- | --- |
| `BPS`, `BANCO DE PREVISION SOCIAL`, `APORTES BPS` | BPS contribution remittance (employee + employer shares) |
| `MONTEPIO`, `JUBILATORIO`, `APORTE PERSONAL` | Retirement contribution share |
| `FONASA` | Health-fund contribution |
| `FRL`, `FONDO DE RECONVERSION` | FRL contribution |
| `DGI`, `IRPF`, `RETENCION IRPF` | DGI / IRPF remittance |
| `BSE`, `SEGURO DE ACCIDENTES` | BSE workplace-accident premium (varies by risk class — research gap) |

### 15.3 Non-payroll / not income

**Non-payroll table**

| Pattern | Classification |
| --- | --- |
| `REINTEGRO`, `REEMBOLSO` | Reimbursement / refund — not salary |
| `VIATICOS`, `GASTOS DE VIAJE` | Travel allowance/expense — review for treatment |
| `CUOTA PRESTAMO`, `DESCUENTO PRESTAMO` | Loan deduction — not an employer cost |

## Section 16 -- Onboarding Fallback

If the user has not provided enough to run payroll, collect in this order:
1. Monthly **nominal** salary in UYU — refuse if given in USD or another currency (Section 7.2).
2. **Family / FONASA situation** — single / single with children / with spouse (own SNIS cover or not) — selects the FONASA band.
3. Number of dependent **minor children** (and any with disability) — for the IRPF deduction.
4. Employer **sector** — general private (7.5% patronal) or civil/public organism.
5. **Pay period** (month + year) — confirm FY2025 constants (BPC 6,576; MNIG 46,032; ceiling 272,564).
6. Whether the employee has **multiple employers** or elects the family-unit regime — affects annual filing.
7. Confirm the employer is **registered with BPS**.

If any required input is missing, state what is missing and **do not** fabricate a figure.

## Section 17 -- Interaction with Other Skills

**Interaction with other skills table**

| Scenario | Skill to Use |
| --- | --- |
| Employee payroll (IRPF + BPS) | **This skill (uruguay-payroll.md)** |
| Uruguay VAT (IVA) returns | uruguay-iva.md |
| Individual IRPF annual return (Form 1102/1103) | uruguay-income-tax.md (employee's own filing, where required) |
| Uruguay corporate income tax (IRAE) | uruguay-corporate-tax.md |
| Uruguay bookkeeping | uruguay-bookkeeping.md |

### Key handoff points

**Payroll → Bookkeeping:** nominal wages and the 12.625% employer BPS are expenses; the employee BPS (~19.6%) and IRPF withheld are liabilities until remitted to BPS/DGI.
**Payroll → IRPF return:** the employer's ajuste anual settles most single-employer employees; the employee files Form 1102/1103 only if a mandatory filer (Section 2.3).

### 18.1 Sources

**Sources**  _(see individual rows)_

| # | Title | Publisher | URL |
| --- | --- | --- | --- |
| 1 | BPS Comunicado R 2/2025 — IRPF 2025 monthly values (escalas) | Banco de Previsión Social (BPS) | https://www.bps.gub.uy/bps/file/22584/2/2025---comunicado-r-2---valores-escalas-irpf-2025.pdf |
| 2 | BPS — Tasas (contribution rates) | BPS | https://www.bps.gub.uy/835/tasas.html |
| 3 | BPS — Tasas Fonasa | BPS | https://www.bps.gub.uy/10314/tasas-fonasa.html |
| 4 | BPS — Topes de cotización (contribution ceiling) | BPS | https://www.bps.gub.uy/10306/topes-de-cotizacion.html |
| 5 | DGI — IRPF Categoría 2 escalas y alícuotas | DGI (gub.uy) | https://www.gub.uy/direccion-general-impositiva/politicas-y-gestion/irpf-categoria-2-escalas-alicuotas |
| 6 | Uruguay — Individual — Taxes on personal income | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/uruguay/individual/taxes-on-personal-income |
| 7 | Uruguay — Individual — Other taxes (social security) | PwC Worldwide Tax Summaries | https://taxsummaries.pwc.com/uruguay/individual/other-taxes |
| 8 | IRPF — vencimiento declaración jurada 2025 | EY Uruguay | https://www.ey.com/es_uy/newsroom/2025/05/irpf-vencimiento-para-la-presentacion-de-la-declaracion-jurada-en-2025 |
| 9 | Decreto N° 369/024 — salario mínimo nacional (1 Jan 2025) | IMPO | https://www.impo.com.uy/bases/decretos/369-2024/1 |

### 18.2 Test Suite (numbered — recompute to confirm any change)

**Test Suite**  _(see individual rows)_

| # | Input | Expected output | Recomputation |
| --- | --- | --- | --- |
| 1 | Min wage, nominal 23,604, single | IRPF 0; net 18,977.62; employer cost 26,584.00 | Ex. A — employee BPS 4,626.38; employer BPS 2,980.00 |
| 2 | Nominal 60,000, single | IRPF 0 (credit > gross); net 48,240.00; employer cost 67,575.00 | Ex. B — gross IRPF 1,396.80 < credit 1,646.40 |
| 3 | Nominal 120,000, single | IRPF 10,149.60; net 86,330.40; employer cost 135,150.00 | Ex. C — gross IRPF 12,031.20; credit 1,881.60 |
| 4 | Nominal 300,000, single (ceiling) | IRPF 51,883.63; net 193,431.77; employer cost 335,817.30 | Ex. D — retirement on 272,564; gross IRPF 56,258.40 |
| 5 | Nominal 120,000, single + 1 child | IRPF 9,128.80; net 85,551.20; employer cost 135,150.00 | Ex. E — FONASA 6%; child deduction 10,960 |
| 6 | IRPF scale cumulative | 1,972.80 / 6,904.80 / 30,578.40 / 63,458.40 / 107,846.40 / 189,388.80 | Ex. F — bracket tops match Section 2.1 |
| 7 | Employer total rate | 12.625% (7.5 + 5 + 0.1 + 0.025) | Section 4.2 |
| 8 | Employee total rate (single, >2.5 BPC, below ceiling) | 19.6% (15 + 4.5 + 0.1) | Section 3.4 |
| 9 | Monthly BPS remittance, nominal 120,000 (Ex. C) | 23,520 + 15,150 = 38,670 | Template row 24 |
| 10 | Deadlines | BPS nómina monthly; IRPF DJ 1102/1103 Jun–Aug (mandatory filers only) | Section 12 |
| 11 | Below MNIG (≤ 46,032) | IRPF = 0, BPS still due | Tier 1 rule 2; Ex. A |
| 12 | Above retirement ceiling (> 272,564) | Retirement capped; FONASA/FRL/FGCL on full nominal | Tier 1 rule 8; Ex. D |

## PROHIBITIONS

- **Never skip IRPF withholding** — NEVER skip IRPF withholding — Uruguay's employer IS an IRPF withholding agent on dependent salaries; compute monthly IRPF and the year-end ajuste anual.  _(PROHIBITIONS section)_
- **Never compute payroll in non-UYU currency** — NEVER compute Uruguayan payroll in USD or any non-UYU currency — refuse and ask for the UYU nominal salary.  _(PROHIBITIONS section)_
- **Never apply IRPF as flat rate** — NEVER apply IRPF as a flat rate — it is progressive bracket-by-bracket (Section 2.1).  _(PROHIBITIONS section)_
- **Never forget deduction credit** — NEVER forget the deduction credit (14% / 8%) — IRPF due = max(0, gross IRPF − credit), and it can drive IRPF to zero.  _(PROHIBITIONS section)_
- **Never apply retirement contributions above ceiling** — NEVER apply retirement contributions (15% / 7.5%) above the UYU 272,564 ceiling, and never cap FONASA/FRL/FGCL — those apply to the full nominal salary.  _(PROHIBITIONS section)_
- **Never assume FONASA employee rate** — NEVER assume the FONASA employee rate — it varies 3%–8% by income band and family situation; ask if unknown.  _(PROHIBITIONS section)_
- **Never tax minimum-wage earner under IRPF** — NEVER tax a minimum-wage earner under IRPF (UYU 23,604 < MNIG 46,032), but always still compute BPS.  _(PROHIBITIONS section)_
- **Never state AFAP allocation thresholds as confirmed** — NEVER state AFAP allocation thresholds as confirmed — they are a research gap (the total 15% employee retirement is unaffected).  _(PROHIBITIONS section)_
- **Never state exact penalty amounts as confirmed** — NEVER state exact DGI/BPS penalty amounts, BSE accident premiums, or aguinaldo treatment as confirmed — they are research gaps.  _(PROHIBITIONS section)_
- **Never apply unconfirmed 2026 figures** — NEVER apply unconfirmed 2026 figures (BPC, MNIG, minimum wage, retirement ceiling) — use FY2025 values until 2026 values are published.  _(PROHIBITIONS section)_
- **Never present computations as definitive** — NEVER present payroll computations as definitive — label them estimated and direct the user to a licensed Uruguayan accountant (contador público).  _(PROHIBITIONS section)_

## Disclaimer

This skill and its outputs are provided for informational and computational purposes only and do not constitute tax, legal, or financial advice. Open Accountants and its contributors accept no liability for any errors, omissions, or outcomes arising from the use of this skill. All outputs must be reviewed and signed off by a qualified professional (such as a licensed accountant in Uruguay) before implementation. This is a Tier 2 (research-verified) skill: figures are sourced to named authorities (BPS, DGI, IMPO), Big-4 summaries (PwC), and named advisories (EY Uruguay) but have not yet been verified section-by-section by a licensed Uruguayan accountant, and items marked "[RESEARCH GAP — reviewer to confirm]" carry residual uncertainty.

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
